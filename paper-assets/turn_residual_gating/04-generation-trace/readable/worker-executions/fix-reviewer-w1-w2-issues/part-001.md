# fix reviewer w1 w2 issues — Part 1 of 2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Worker execution logs

[Transcript overview](../fix-reviewer-w1-w2-issues.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/35/355c4e5cbcb343bb8d0c.json)

## Before a recorded user message

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
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "9c83bb7b-c2e0-4c57-9e96-fa3fa7691c17",
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
    "utilization": 0.81,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "3c335173-7f72-4042-a1fe-07e2002da4b1",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Assistant

_source line 4_

I'll fix the 4 data consistency issues. Let me start by reading the relevant files and searching for registry data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "3a6c70d3-e3ef-4443-946d-845728993331",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHsrUZH47nb6m1MT7j8q4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15063,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15063
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

<details open><summary>🔧 Tool call — Agent · `toolu_01323fxcv4ZaHxVyx6rBpkYR`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find crossmodel and perseed tables",
  "prompt": "Find the exact file paths for:\n1. The crossmodel detail table (tab_crossmodel_detail or similar) - likely in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/ or paper/sections/\n2. The perseed table for TG (tab_perseed or similar)\n3. The cost table (tab_cost or similar)\n4. Any tex files in paper/sections/ that mention \"SS\" gap ratio like \"1.2\" or \"7.8\" or \"7.9\"\n\nSearch in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/\n\nReport back the exact file paths and the relevant line numbers/content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "844b68ce-5d98-45f9-9553-fcad8e8296fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHsrUZH47nb6m1MT7j8q4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15063,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15063
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
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Find crossmodel and perseed tables",
  "task_type": "local_agent",
  "prompt": "Find the exact file paths for:\n1. The crossmodel detail table (tab_crossmodel_detail or similar) - likely in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/ or paper/sections/\n2. The perseed table for TG (tab_perseed or similar)\n3. The cost table (tab_cost or similar)\n4. Any tex files in paper/sections/ that mention \"SS\" gap ratio like \"1.2\" or \"7.8\" or \"7.9\"\n\nSearch in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/\n\nReport back the exact file paths and the relevant line numbers/content.",
  "uuid": "f63cc236-9ef4-4f7a-a89c-ab027186ba3d",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


## Round 1

## Round 1

203 recorded events


### User

_source line 7 · 2026-05-25T20:43:52.857Z_

Find the exact file paths for:
1. The crossmodel detail table (tab_crossmodel_detail or similar) - likely in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/ or paper/sections/
2. The perseed table for TG (tab_perseed or similar)
3. The cost table (tab_cost or similar)
4. Any tex files in paper/sections/ that mention "SS" gap ratio like "1.2" or "7.8" or "7.9"

Search in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/

Report back the exact file paths and the relevant line numbers/content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "dbf65f35-71fd-489a-a364-bc779267c20a"
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
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_11/…",
  "usage": {
    "total_tokens": 17005,
    "tool_uses": 1,
    "duration_ms": 1971
  },
  "last_tool_name": "Glob",
  "uuid": "342aa772-08bb-4788-834d-ba6c5c8202dc",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_0154fvBy9tnqExofPYFgQhW4`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*crossmodel*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "b09907f8-3134-4fa9-b18c-8ef6ccfc3c35",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ba4XfLuUc4wrAvbhmgHyMf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16996,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16996,
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

_source line 10 · 2026-05-25T20:43:54.876Z_

<details><summary>↩ Tool result · `toolu_0154fvBy9tnqExofPYFgQhW4`</summary>

```text
logs/workers/worker_viz_gate_profile_crossmodel_20260522T152840.log
logs/chats/worker_viz_gate_profile_crossmodel_20260522T152840.lock
logs/chats/worker_viz_gate_profile_crossmodel_20260522T152840.jsonl
logs/workers/worker_viz_gate_profile_crossmodel_20260522T152840_result.json
artifacts/_project/chart/fig_gate_profile_crossmodel_info.txt
artifacts/fig_gate_profile_crossmodel.pdf
artifacts/fig_gate_profile_crossmodel.png
logs/workers/worker_code_appendix_seeds_perturn_crossmodel_20260524T150612.log
logs/chats/worker_code_appendix_seeds_perturn_crossmodel_20260524T150612.lock
logs/chats/worker_code_appendix_seeds_perturn_crossmodel_20260524T150612.jsonl
logs/workers/worker_code_appendix_seeds_perturn_crossmodel_20260524T150612_result.json
artifacts/appendix_expansion/tab_crossmodel_detail.tex
figures/paper/gen_fig_gate_profile_crossmodel.py
figures/paper/fig_gate_profile_crossmodel.pdf
figures/paper/fig_gate_profile_crossmodel.png
figures/paper/gen_fig_crossmodel.py
figures/paper/fig_crossmodel.pdf
figures/paper/fig_crossmodel.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "20117025-b059-47c0-9922-37f1210661bd"
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
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_11/…",
  "usage": {
    "total_tokens": 17008,
    "tool_uses": 2,
    "duration_ms": 2077
  },
  "last_tool_name": "Glob",
  "uuid": "f909f5c1-e45a-4398-9ecc-d9843c8a4413",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01BALTGpGJUeTJR9fzJCNtPY`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*perseed*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "2d3097d4-9b2d-4da4-807a-85028a0bbb4b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ba4XfLuUc4wrAvbhmgHyMf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16996,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16996,
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

_source line 13 · 2026-05-25T20:43:54.973Z_

<details><summary>↩ Tool result · `toolu_01BALTGpGJUeTJR9fzJCNtPY`</summary>

```text
artifacts/appendix_expansion/tab_perseed_ss.tex
artifacts/appendix_expansion/tab_perseed_tg.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "77bf7710-186b-4caf-a88f-6555ce8a0e02"
}
```

</details>

---


### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_11/…",
  "usage": {
    "total_tokens": 17011,
    "tool_uses": 3,
    "duration_ms": 2289
  },
  "last_tool_name": "Glob",
  "uuid": "cf1af06f-1dd5-4964-bb6d-3303287ddb8c",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_014jWHrMnWBXTRzF7x78yjvU`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*cost*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "076e03cc-fac9-4107-84d6-74150fe336ec",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ba4XfLuUc4wrAvbhmgHyMf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16996,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16996,
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

_source line 16 · 2026-05-25T20:43:55.190Z_

<details><summary>↩ Tool result · `toolu_014jWHrMnWBXTRzF7x78yjvU`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "caf14e5c-ee60-4310-9c53-c26882e2e5a8"
}
```

</details>

---


### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_11/…",
  "usage": {
    "total_tokens": 17014,
    "tool_uses": 4,
    "duration_ms": 2709
  },
  "last_tool_name": "Glob",
  "uuid": "5a1c1cae-5090-4ca8-913a-bcb53fa95051",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Glob · `toolu_01DvqjgYNeBsSabc9h1H99os`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "075f6209-b33e-4db9-afdd-6bf5fa7e2eb0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ba4XfLuUc4wrAvbhmgHyMf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16996,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16996,
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

_source line 19 · 2026-05-25T20:43:55.576Z_

<details><summary>↩ Tool result · `toolu_01DvqjgYNeBsSabc9h1H99os`</summary>

```text
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/table_steering_full.tex
artifacts/_project/paper/tab_dataset_stats.tex
artifacts/_project/paper/tab_gar_robustness.tex
artifacts/_project/paper/tab_mmlu_detail.tex
artifacts/_project/paper/tab_qwen15b_results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "314d7b55-8d15-4026-9e5f-dd1a17614589"
}
```

</details>

---


### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_11/…",
  "usage": {
    "total_tokens": 17017,
    "tool_uses": 5,
    "duration_ms": 2861
  },
  "last_tool_name": "Glob",
  "uuid": "c387a4ee-6abe-4d01-ab12-f9b230e70d5e",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Glob · `toolu_01PwtJTurKwUoUhF9QTTX5p2`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/sections/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "10cf8255-3053-487a-86a4-31b934319502",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ba4XfLuUc4wrAvbhmgHyMf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16996,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16996,
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

_source line 22 · 2026-05-25T20:43:55.733Z_

<details><summary>↩ Tool result · `toolu_01PwtJTurKwUoUhF9QTTX5p2`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "1ed6c92e-5710-4e7f-baf4-c2a98f96a5c3"
}
```

</details>

---


### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_11/…",
  "usage": {
    "total_tokens": 18868,
    "tool_uses": 6,
    "duration_ms": 5192
  },
  "last_tool_name": "Glob",
  "uuid": "38a7e64e-0612-4401-a151-de0d9cbf6de7",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Glob · `toolu_01KfEjGtygvvD1Yoqzs9JCe7`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*tab*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "87d2a1f6-ffaa-42d6-9bb5-a469f1597b58",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018p6pppXjEyPA1QumYYUgcY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1845,
      "cache_read_input_tokens": 16996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1845,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 25 · 2026-05-25T20:43:58.092Z_

<details><summary>↩ Tool result · `toolu_01KfEjGtygvvD1Yoqzs9JCe7`</summary>

```text
artifacts/_project/paper/table_steering_full.tex
logs/workers/worker_viz_beta_steering_table_20260522T154749.log
logs/workers/worker_viz_beta_steering_table_20260522T154749_result.json
artifacts/table_steering_full.tex
logs/workers/worker_paper_loss_iteration_table_20260522T160702.log
logs/workers/worker_paper_loss_iteration_table_20260522T160702_result.json
artifacts/_project/paper/tab_dataset_stats.tex
artifacts/_project/paper/tab_gar_robustness.tex
artifacts/_project/paper/tab_mmlu_detail.tex
artifacts/_project/paper/tab_qwen15b_results.tex
artifacts/_project/data/tab_statistical_tests.tex
artifacts/appendix_expansion/tab_gar_robustness.tex
artifacts/appendix_expansion/tab_statistical_tests.tex
artifacts/appendix_expansion/tab_perseed_ss.tex
artifacts/appendix_expansion/tab_perseed_tg.tex
artifacts/appendix_expansion/tab_perturn_qwen.tex
artifacts/appendix_expansion/tab_mmlu_detail.tex
artifacts/appendix_expansion/tab_qwen15b_results.tex
artifacts/appendix_expansion/tab_crossmodel_detail.tex
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_editable.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel_editable.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/install/editable_legacy.py
.venv/lib/python3.14/site-packages/pip/_vendor/distlib/database.py
.venv/lib/python3.14/site-packages/pip/_vendor/rich/table.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/__pycache__/metadata_editable.cpython-314.pyc
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/__pycache__/wheel_editable.cpython-314.pyc
.venv/lib/python3.14/site-packages/pip/_internal/operations/install/__pycache__/editable_legacy.cpython-314.pyc
.venv/lib/python3.14/site-packages/pip/_vendor/distlib/__pycache__/database.cpython-314.pyc
.venv/lib/python3.14/site-packages/pip/_vendor/rich/__pycache__/table.cpython-314.pyc
.venv/lib/python3.14/site-packages/pygments/lexers/tablegen.py
.venv/lib/python3.14/site-packages/pygments/lexers/__pycache__/tablegen.cpython-314.pyc
.venv/lib/python3.14/site-packages/numpy/_core/include/numpy/_public_dtype_api_table.h
.venv/lib/python3.14/site-packages/numpy/_core/tests/test_hashtable.py
.venv/lib/python3.14/site-packages/numpy/testing/print_coercion_tables.py
.venv/lib/python3.14/site-packages/numpy/testing/print_coercion_tables.pyi
.venv/lib/python3.14/site-packages/numpy/_core/tests/__pycache__/test_hashtable.cpython-314.pyc
.venv/lib/python3.14/site-packages/numpy/testing/__pycache__/print_coercion_tables.cpython-314.pyc
.venv/lib/python3.14/site-packages/fontTools/colorLib/table_builder.py
.venv/lib/python3.14/site-packages/fontTools/merge/tables.py
.venv/lib/python3.14/site-packages/fontTools/ttLib/tables/table_API_readme.txt
.venv/lib/python3.14/site-packages/fontTools/varLib/interpolatable.py
.venv/lib/python3.14/site-packages/fontTools/varLib/interpolatableHelpers.py
.venv/lib/python3.14/site-packages/fontTools/varLib/interpolatablePlot.py
.venv/lib/python3.14/site-packages/fontTools/varLib/interpolatableTestContourOrder.py
.venv/lib/python3.14/site-packages/fontTools/varLib/interpolatableTestStartingPoint.py
.venv/lib/python3.14/site-packages/fontTools/colorLib/__pycache__/table_builder.cpython-314.pyc
.venv/lib/python3.14/site-packages/fontTools/merge/__pycache__/tables.cpython-314.pyc
.venv/lib/python3.14/site-packages/fontTools/varLib/__pycache__/interpolatable.cpython-314.pyc
.venv/lib/python3.14/site-packages/fontTools/varLib/__pycache__/interpolatableHelpers.cpython-314.pyc
.venv/lib/python3.14/site-packages/fontTools/varLib/__pycache__/interpolatablePlot.cpython-314.pyc
.venv/lib/python3.14/site-packages/fontTools/varLib/__pycache__/interpolatableTestContourOrder.cpython-314.pyc
.venv/lib/python3.14/site-packages/fontTools/varLib/__pycache__/interpolatableTestStartingPoint.cpython-314.pyc
.venv/lib/python3.14/site-packages/markdown_it/rules_block/table.py
.venv/lib/python3.14/site-packages/markdown_it/rules_block/__pycache__/table.cpython-314.pyc
.venv/lib/python3.14/site-packages/rich/table.py
.venv/lib/python3.14/site-packages/rich/__pycache__/table.cpython-314.pyc
.venv/lib/python3.14/site-packages/pandas/_libs/hashtable.cpython-314-x86_64-linux-gnu.so
.venv/lib/python3.14/site-packages/pandas/_libs/hashtable.pyi
.venv/lib/python3.14/site-packages/pandas/core/computation/pytables.py
.venv/lib/python3.14/site-packages/pandas/io/pytables.py
.venv/lib/python3.14/site-packages/pandas/io/formats/templates/html_table.tpl
.venv/lib/python3.14/site-packages/pandas/io/formats/templates/latex_longtable.tpl
.venv/lib/python3.14/site-packages/pandas/io/formats/templates/latex_table.tpl
.venv/lib/python3.14/site-packages/pandas/io/json/_table_schema.py
.venv/lib/python3.14/site-packages/pandas/tests/io/json/test_json_table_schema.py
.venv/lib/python3.14/site-packages/pandas/tests/io/json/test_json_table_schema_ext_dtype.py
.venv/lib/python3.14/site-packages/pandas/tests/io/pytables/test_pytables_missing.py
.venv/lib/python3.14/site-packages/pandas/tests/libs/test_hashtable.py
.venv/lib/python3.14/site-packages/pandas/tests/reshape/test_crosstab.py
.venv/lib/python3.14/site-packages/pandas/core/computation/__pycache__/pytables.cpython-314.pyc
.venv/lib/python3.14/site-packages/pandas/io/json/__pycache__/_table_schema.cpython-314.pyc
.venv/lib/python3.14/site-packages/pandas/io/__pycache__/pytables.cpython-314.pyc
.venv/lib/python3.14/site-packages/pandas/tests/io/json/__pycache__/test_json_table_schema.cpython-314.pyc
.venv/lib/python3.14/site-packages/pandas/tests/io/json/__pycache__/test_json_table_schema_ext_dtype.cpython-314.pyc
.venv/lib/python3.14/site-packages/pandas/tests/io/pytables/__pycache__/test_pytables_missing.cpython-314.pyc
.venv/lib/python3.14/site-packages/pandas/tests/libs/__pycache__/test_hashtable.cpython-314.pyc
.venv/lib/python3.14/site-packages/pandas/tests/reshape/__pycache__/test_crosstab.cpython-314.pyc
.venv/lib/python3.14/site-packages/matplotlib/table.py
.venv/lib/python3.14/site-packages/matplotlib/table.pyi
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/stylelib/tableau-colorblind10.mplstyle
.venv/lib/python3.14/site-packages/matplotlib/tests/test_table.py
.venv/lib/python3.14/site-packages/matplotlib/__pycache__/table.cpython-314.pyc
.venv/lib/python3.14/site-packages/matplotlib/tests/__pycache__/test_table.cpython-314.pyc
.venv/lib/python3.14/site-packages/google/genai/tests/files/test_register_table.py
.venv/lib/python3.14/site-packages/google/genai/tests/files/__pycache__/test_register_table.cpython-314.pyc
artifacts/appendix_expansion/tab_dataset_stats.tex
artifacts/appendix_expansion/tab_perturn_llama.tex
artifacts/_project/report/audit_appendix_tables_5d6908.md
artifacts/_project/report/audit_appendix_tables.md
artifacts/audit_appendix_tables.md
logs/workers/worker_audit_appendix_tables_20260525T201208.log
logs/workers/worker_audit_appendix_tables_20260525T201208_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "ec397e43-910c-47a4-a98e-6980429eaed1"
}
```

</details>

---


### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Searching for SS|gap|ratio|1\\.2|7\\.[89]",
  "usage": {
    "total_tokens": 18869,
    "tool_uses": 7,
    "duration_ms": 5859
  },
  "last_tool_name": "Grep",
  "uuid": "272d4afb-35ef-4d68-ad58-6c9d78c896cb",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_016QQrYpFk4DjgAC8TdpJ8VE`</summary>

```json
{
  "pattern": "SS|gap|ratio|1\\.2|7\\.[89]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper",
  "type": "tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "3e8d3f89-b760-4180-924b-4101fe270710",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018p6pppXjEyPA1QumYYUgcY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1845,
      "cache_read_input_tokens": 16996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1845,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 28 · 2026-05-25T20:43:58.738Z_

<details><summary>↩ Tool result · `toolu_016QQrYpFk4DjgAC8TdpJ8VE`</summary>

```text
Found 4 files
artifacts/_project/paper/tab_mmlu_detail.tex
artifacts/_project/paper/tab_gar_robustness.tex
artifacts/_project/paper/table_steering_full.tex
artifacts/_project/paper/analysis.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "b0f1187d-3aac-4a2a-9bf6-2a22f42e2f97"
}
```

</details>

---


### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Reading artifacts/appendix_expansion/tab_crossmodel_detail.tex",
  "usage": {
    "total_tokens": 21859,
    "tool_uses": 8,
    "duration_ms": 8073
  },
  "last_tool_name": "Read",
  "uuid": "752655d1-1e8b-4f5f-942c-685f517c0668",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_018qbfETApXtPyKFSsi6gzSL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "4cc3202c-28fe-4d9a-8370-458c0db8cdd9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V8GfuwZE5KqXtAKCf6bdsB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 18841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2988,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 31 · 2026-05-25T20:44:00.939Z_

<details><summary>↩ Tool result · `toolu_018qbfETApXtPyKFSsi6gzSL`</summary>

```text
1	% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct
2	% Conditions shared by both models: Base, ThreadGate, LoRA-only
3	% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0
4	% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4
5	% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)
6	\begin{table*}[t]
7	\centering
8	\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.
9	Gap ratio = TF GAR / AR GAR; lower is better (less exposure bias).
10	Qwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).
11	Llama AR GAR and gaps are mean-based; median-based TG gap is 27$\times$ (\S\ref{subsec:cross-model}).}
12	\label{tab:crossmodel-detail}
13	\small
14	\begin{tabular}{@{}ll ccccc@{}}
15	\toprule
16	\textbf{Model} & \textbf{Condition} & \textbf{TF GAR}$\uparrow$ & \textbf{AR GAR}$\uparrow$ & \textbf{TF PPL}$\downarrow$ & \textbf{AR PPL}$\downarrow$ & \textbf{Gap}$\downarrow$ \\
17	\midrule
18	\multirow{4}{*}{Qwen-7B}
19	  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\times$ \\
20	  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\times$ \\
21	  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\times$ \\
22	  & \textbf{SS} & 0.498 & \textbf{0.401} & 2.78 & 1.441 & \textbf{1.2$\times$} \\
23	\midrule
24	\multirow{4}{*}{Llama-8B}
25	  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\times$ \\
26	  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\times$ \\
27	  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\times$ \\
28	  & \textbf{SS} & 0.477 & \textbf{0.166} & 2.82 & 1.370 & \textbf{2.9$\times$} \\
29	\bottomrule
30	\end{tabular}
31	\end{table*}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "930d1b84-1b9d-4fd2-bcdf-f962adaaded2"
}
```

</details>

---


### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Reading artifacts/appendix_expansion/tab_perseed_tg.tex",
  "usage": {
    "total_tokens": 21860,
    "tool_uses": 9,
    "duration_ms": 8374
  },
  "last_tool_name": "Read",
  "uuid": "2bb89768-495c-47ee-99d7-ee683c31b149",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_0185C7C64D52KwrDUofaaEnh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "7450ab14-f133-4176-9bcc-222d25d4b947",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V8GfuwZE5KqXtAKCf6bdsB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 18841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2988,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 34 · 2026-05-25T20:44:01.237Z_

<details><summary>↩ Tool result · `toolu_0185C7C64D52KwrDUofaaEnh`</summary>

```text
1	% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123
2	% TF eval: N=200 held-out conversations
3	% AR eval: N=5, T=10 model-generated conversations (original eval protocol)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations.
8	AR evaluation uses 5 model-generated conversations with 10 turns each.}
9	\label{tab:perseed-tg}
10	\resizebox{\columnwidth}{!}{
11	\begin{tabular}{@{}l cc c@{}}
12	\toprule
13	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Mean $\pm$ Std} \\
14	\midrule
15	\multicolumn{4}{@{}l}{\textit{Teacher-Forced (TF)}} \\
16	\quad GAR-ours $\uparrow$   & 0.504 & 0.505 & 0.504 $\pm$ 0.001 \\
17	\quad GAR-Dongre $\uparrow$ & 0.015 & 0.012 & 0.014 $\pm$ 0.002 \\
18	\quad PPL $\downarrow$       & 2.784 & 2.780 & 2.782 $\pm$ 0.003 \\
19	\midrule
20	\multicolumn{4}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
21	\quad GAR-ours $\uparrow$   & 0.016 & 0.017 & 0.016 $\pm$ 0.001 \\
22	\quad GAR-Dongre $\uparrow$ & 0.019 & 0.018 & 0.019 $\pm$ 0.001 \\
23	\quad PPL $\downarrow$       & 1.360 & 1.386 & 1.373 $\pm$ 0.018 \\
24	\midrule
25	\multicolumn{4}{@{}l}{\textit{Derived}} \\
26	\quad Gap ratio (TF/AR GAR-ours) $\downarrow$ & 32.1 & 30.6 & 31.4 $\pm$ 1.1 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "9efdbbc4-a468-464a-8901-16fb71c8cd78"
}
```

</details>

---


### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Reading artifacts/appendix_expansion/tab_perseed_ss.tex",
  "usage": {
    "total_tokens": 21861,
    "tool_uses": 10,
    "duration_ms": 8609
  },
  "last_tool_name": "Read",
  "uuid": "93e333f8-28cd-4c8d-a37b-1398de025613",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01KPaHypn7HpxugtmvQxjWMi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "1356fc57-1c48-4c0d-92bf-acf6d0be399a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V8GfuwZE5KqXtAKCf6bdsB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 18841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2988,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 37 · 2026-05-25T20:44:01.473Z_

<details><summary>↩ Tool result · `toolu_01KPaHypn7HpxugtmvQxjWMi`</summary>

```text
1	% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456
2	% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)
3	% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\text{valid}} \approx 39$).}
8	\label{tab:perseed-ss}
9	\resizebox{\columnwidth}{!}{
10	\begin{tabular}{@{}l ccc c@{}}
11	\toprule
12	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean $\pm$ Std} \\
13	\midrule
14	\multicolumn{5}{@{}l}{\textit{Teacher-Forced (TF)}} \\
15	\quad GAR-ours $\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\pm$ 0.032 \\
16	\quad GAR-Dongre $\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\pm$ 0.014 \\
17	\quad PPL $\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\pm$ 0.097 \\
18	\midrule
19	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
20	\quad GAR-ours $\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\pm$ 0.047 \\
21	\quad PPL $\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\pm$ 0.002 \\
22	\midrule
23	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 3$}} \\
24	\quad GAR-ours $\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\pm$ 0.008 \\
25	\quad PPL $\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\pm$ 0.022 \\
26	\midrule
27	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 5$}} \\
28	\quad GAR-ours $\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\pm$ 0.001 \\
29	\quad PPL $\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\pm$ 0.013 \\
30	\bottomrule
31	\end{tabular}}
32	\end{table}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "960480c2-a298-4160-9a53-074a64f79d94"
}
```

</details>

---


### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Searching for (1\\.2|7\\.[89])",
  "usage": {
    "total_tokens": 21862,
    "tool_uses": 11,
    "duration_ms": 9386
  },
  "last_tool_name": "Grep",
  "uuid": "7acb4da5-9d26-464f-b5b9-673deb8b4048",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Grep · `toolu_01TXCbtif42kmzHKhca9BaZE`</summary>

```json
{
  "pattern": "(1\\.2|7\\.[89])",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "044094c2-2fd0-46fd-9efa-4870e6956356",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V8GfuwZE5KqXtAKCf6bdsB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 18841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2988,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 40 · 2026-05-25T20:44:02.260Z_

<details><summary>↩ Tool result · `toolu_01TXCbtif42kmzHKhca9BaZE`</summary>

```text
artifacts/_project/paper/analysis.tex:20:2 & $-$0.042 & 67.9 & 14.7$\times$ \\
artifacts/_project/paper/tab_gar_robustness.tex:13:  & TG        & 0.3938 & 0.3254 & 1.21$\times$ \\
artifacts/_project/paper/tab_mmlu_detail.tex:14:Other          & 68.25 & 67.59 & 68.12 & 67.95 & 67.06 & 66.80 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "c13ebe2a-c3e4-46ed-aacc-8c84da2f410f"
}
```

</details>

---


### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 25116,
    "tool_uses": 12,
    "duration_ms": 11824
  },
  "last_tool_name": "Bash",
  "uuid": "883c2c05-28f5-43e0-9b65-5254f82189d7",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_018brqmUqgjqiyZJr3RtBnr7`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating -type f -name \"*cost*\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "518567ff-c582-442c-a13b-b61ec3b2118a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019nGfsC17Qhibr6Zg4MvSwZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3252,
      "cache_read_input_tokens": 21829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3252,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Reading artifacts/_project/paper/tab_gar_robustness.tex",
  "usage": {
    "total_tokens": 25117,
    "tool_uses": 13,
    "duration_ms": 11979
  },
  "last_tool_name": "Read",
  "uuid": "ee53d294-cb5c-4f26-9f02-675b062fe0d3",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01Hv8MwckmZVFDv8nK3tfgvU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "ae98042a-18cb-46f7-bf20-a407ff68e44d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019nGfsC17Qhibr6Zg4MvSwZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3252,
      "cache_read_input_tokens": 21829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3252,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 45 · 2026-05-25T20:44:04.882Z_

<details><summary>↩ Tool result · `toolu_018brqmUqgjqiyZJr3RtBnr7`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "81c1abe4-996d-4bba-a392-54ea922098d7"
}
```

</details>

---


### Tool result

_source line 46 · 2026-05-25T20:44:04.854Z_

<details><summary>↩ Tool result · `toolu_01Hv8MwckmZVFDv8nK3tfgvU`</summary>

```text
1	% GAR definition robustness: 4 token selection strategies x 3 conditions
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{GAR robustness across token selection strategies. We evaluate four ways to select the token position for gradient attribution: \textbf{Last} (final token of each turn), \textbf{All} (mean over all tokens), \textbf{First} (first token), and \textbf{Goal-only} (goal token as in \citet{dongre2024multi}). Turn-1 and Mid-turn GAR are measured under autoregressive generation on 50 held-out conversations. Gap Ratio = Turn-1 / Mid-turn; lower indicates better gradient preservation across turns.}
6	\label{tab:gar_robustness}
7	\begin{tabular}{@{}ll ccc@{}}
8	\toprule
9	\textbf{Token Selection} & \textbf{Condition} & \textbf{Turn-1 GAR} & \textbf{Mid-turn GAR} & \textbf{Gap Ratio} $\downarrow$ \\
10	\midrule
11	\multirow{3}{*}{Last (ours)}
12	  & Base      & 0.0858 & 0.0152 & 5.64$\times$ \\
13	  & TG        & 0.3938 & 0.3254 & 1.21$\times$ \\
14	  & SS        & 0.5274 & 0.4582 & 1.15$\times$ \\
15	\midrule
16	\multirow{3}{*}{All tokens}
17	  & Base      & 0.1152 & 0.0152 & 7.57$\times$ \\
18	  & TG        & 0.1275 & 0.0253 & 5.04$\times$ \\
19	  & SS        & 0.5043 & 0.3658 & 1.38$\times$ \\
20	\midrule
21	\multirow{3}{*}{First token}
22	  & Base      & 0.2987 & 0.0224 & 13.32$\times$ \\
23	  & TG        & 0.3225 & 0.0392 & 8.24$\times$ \\
24	  & SS        & 0.7549 & 0.4118 & 1.83$\times$ \\
25	\midrule
26	\multirow{3}{*}{Goal-only}
27	  & Base      & 0.0110 & 0.0049 & 2.23$\times$ \\
28	  & TG        & 0.3313 & 0.3103 & 1.07$\times$ \\
29	  & SS        & 0.4528 & 0.4435 & 1.02$\times$ \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "612dd7fb-0ef6-49a3-84c3-0a8eb87d1cec"
}
```

</details>

---


### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Reading artifacts/_project/paper/analysis.tex",
  "usage": {
    "total_tokens": 25118,
    "tool_uses": 14,
    "duration_ms": 12050
  },
  "last_tool_name": "Read",
  "uuid": "f3767a2d-2d5e-4754-8114-2570805b6d77",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01CFjReTX4fYTK1cWrJUVh6e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "2db4f5d7-a820-4c7e-9a23-0c901152886d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019nGfsC17Qhibr6Zg4MvSwZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3252,
      "cache_read_input_tokens": 21829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3252,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 49 · 2026-05-25T20:44:04.925Z_

<details><summary>↩ Tool result · `toolu_01CFjReTX4fYTK1cWrJUVh6e`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	The four-way ablation in \S\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section investigates why. We first characterize the gradient dynamics between the two training objectives (\S\ref{subsec:gradient-conflict}), then show that the learned gates exhibit behavior opposite to the design intent (\S\ref{subsec:gate-conditioning}). A targeted causal experiment rules out gradient direction conflict as the explanation (\S\ref{subsec:pcgrad}), and a distribution shift analysis identifies the actual failure mode (\S\ref{subsec:dist-shift}).
4	
5	\subsection{Gradient Conflict Observation}\label{subsec:gradient-conflict}
6	
7	To understand how the two loss terms interact during training, we measure the cosine similarity between $\nabla_\theta \mathcal{L}_\text{NTP}$ and $\nabla_\theta \mathcal{L}_\text{GAR}$ at each transformer layer across three training epochs. Table~\ref{tab:grad-conflict} summarizes the results.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Gradient interaction between $\mathcal{L}_\text{NTP}$ and $\mathcal{L}_\text{GAR}$ across training epochs. \textit{cos\_sim}: mean cosine similarity across layers. \textit{neg\%}: percentage of layers with negative cosine similarity. \textit{mag\_ratio}: ratio of NTP to GAR gradient magnitudes.}
13	\label{tab:grad-conflict}
14	\begin{tabular}{lccc}
15	\toprule
16	\textbf{Epoch} & \textbf{cos\_sim} & \textbf{neg\%} & \textbf{mag\_ratio} \\
17	\midrule
18	0 & $-$0.089 & 78.6 & 7.5$\times$ \\
19	1 & $-$0.054 & 71.4 & 13.7$\times$ \\
20	2 & $-$0.042 & 67.9 & 14.7$\times$ \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	Two patterns are apparent. First, the NTP and GAR gradients point in opposing directions across 68--79\% of layers throughout training. The mean cosine similarity is negative at every epoch, though it attenuates slightly from $-$0.089 to $-$0.042 as training progresses. Second, the NTP gradient magnitude dominates the GAR gradient by a factor that grows from 7.5$\times$ at epoch~0 to 14.7$\times$ at epoch~2. Direction conflict decreases while magnitude imbalance worsens. We observe these patterns as descriptive statistics of the training dynamics. This does not establish that gradient conflict causes $\mathcal{L}_\text{GAR}$ to fail; \S\ref{subsec:pcgrad} tests this hypothesis directly.
26	
27	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
28	
29	The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
30	
31	The gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.
32	
33	The practical consequence is that the gates provide almost no intervention at inference time. Across all layers, mean gate values during inference range from 0.93 to 0.98, corresponding to residual stream attenuation of only 2--7\%. This attenuation is far below what would be required for meaningful modulation, and it explains the convergence with LoRA-only in Table~\ref{tab:four-way}. Figure~\ref{fig:gate-shift}(a) visualizes the per-layer gate difference between early and late turns.
34	
35	\subsection{PCGrad Causal Exclusion}\label{subsec:pcgrad}
36	
37	The gradient conflict observed in \S\ref{subsec:gradient-conflict} raises a natural hypothesis: perhaps the opposing gradient directions between $\mathcal{L}_\text{NTP}$ and $\mathcal{L}_\text{GAR}$ prevent the GAR objective from converging. If direction conflict is the cause of $\mathcal{L}_\text{GAR}$ collapse, then eliminating direction conflict should prevent the collapse. We test this prediction using PCGrad \citep{yu2020pcgrad}.
38	
39	PCGrad projects the gradient of one task onto the normal plane of the other whenever two task gradients conflict in direction. We apply PCGrad to the gate parameters only, projecting $\nabla_\theta \mathcal{L}_\text{NTP}$ onto the orthogonal complement of $\nabla_\theta \mathcal{L}_\text{GAR}$ whenever their cosine similarity is negative. This eliminates the directional component of the conflict while leaving magnitude differences intact. PCGrad does not address magnitude imbalance (which GradNorm targets; \citealp{chen2018gradnorm}) or Nash equilibrium violations (which Nash-MTL targets; \citealp{navon2022nash}); our claim is scoped to direction conflict alone.
40	
41	The result is unambiguous. Under PCGrad, the cosine similarity between NTP and GAR gradients on gate parameters turns positive by gradient step~200 ($+$0.086), confirming that PCGrad successfully removes direction conflict. Yet $\mathcal{L}_\text{GAR}$ follows a trajectory nearly identical to the baseline (v7) and collapses in the same manner. Figure~\ref{fig:training-pcgrad}(b) overlays the $\mathcal{L}_\text{GAR}$ training curves for both conditions.
42	
43	The causal exclusion follows by \emph{modus tollens}:
44	\begin{enumerate}
45	    \item If direction conflict causes $\mathcal{L}_\text{GAR}$ collapse, then removing direction conflict should prevent the collapse.
46	    \item PCGrad removes direction conflict (cosine similarity turns positive at step~200).
47	    \item $\mathcal{L}_\text{GAR}$ collapses regardless.
48	    \item Therefore, direction conflict is not the cause of $\mathcal{L}_\text{GAR}$ collapse.
49	\end{enumerate}
50	
51	This result recharacterizes the gradient observations in \S\ref{subsec:gradient-conflict}: direction conflict between $\mathcal{L}_\text{NTP}$ and $\mathcal{L}_\text{GAR}$ is a symptom of the multi-objective optimization dynamics, not the mechanism responsible for GAR failure. The magnitude imbalance (7.5--14.7$\times$) and potential Nash equilibrium violations remain as candidate explanations that future work can test with GradNorm \citep{chen2018gradnorm} and Nash-MTL \citep{navon2022nash}.
52	
53	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
54	
55	The preceding subsections explain why the gating mechanism is ineffective during training. This subsection addresses why the learned GAR improvements fail to transfer from training to inference.
56	
57	Recall from \S\ref{sec:experiments} that teacher-forced GAR-ours reaches 0.49 for all fine-tuned variants, while autoregressive GAR-ours drops to 0.016, a 30$\times$ gap. We decompose this gap by comparing same-distribution and cross-distribution evaluation. Under same-distribution evaluation (teacher-forced UltraChat text), GAR-ours is approximately 0.49, confirming that the model has learned the intended attention pattern on the training distribution. Under cross-distribution evaluation (model-generated text), GAR-ours drops to 0.016. The training itself is sound; the failure is one of generalization.
58	
59	GAR-Dongre provides a revealing control. Across both evaluation conditions, GAR-Dongre remains uniformly low (0.01--0.02) with no distribution gap. The distribution shift selectively destroys the concentrated attention pattern captured by GAR-ours (last-token, summary-position attention) while leaving the diffuse attention pattern captured by GAR-Dongre (averaged across all positions) unaffected. This selectivity implies that the distribution shift disrupts a specific learned routing behavior rather than attention computation in general.
60	
61	The mechanism connecting training regime to distribution shift is exposure bias \citep{bengio2015scheduled}. During training, the model conditions each token prediction on ground-truth prefixes from UltraChat. At inference, it conditions on its own prior outputs. The attention patterns optimized for the former distribution do not transfer to the latter, because the statistical properties of model-generated text diverge from those of human-written reference text. The 2--7\% gate attenuation documented in \S\ref{subsec:gate-conditioning} is far too weak to compensate for this distributional mismatch.
62	
63	\citet{he2019exposure} showed that language models exhibit token-level self-recovery from exposure bias: accumulated errors in autoregressive generation do not degrade perplexity as severely as worst-case analysis predicts. Our results are consistent with this finding at the token level, as PPL remains normal across all conditions (Table~\ref{tab:four-way}). The critical distinction is between primary and auxiliary objectives. The NTP objective is robust to exposure bias because next-token prediction is the same task at both training and inference time. The GAR auxiliary objective is fragile because it optimizes an attention pattern under teacher-forced context that has no counterpart in autoregressive generation. Primary-task self-recovery does not extend to auxiliary objectives that depend on distributional properties of the input prefix. Figure~\ref{fig:gate-shift}(b) summarizes the four-model GAR comparison across evaluation conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "2785e355-0be0-4c99-a895-4eb191b9e046"
}
```

</details>

---


### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Searching for cost|Cost|COST|computation|Computation",
  "usage": {
    "total_tokens": 29003,
    "tool_uses": 15,
    "duration_ms": 14824
  },
  "last_tool_name": "Grep",
  "uuid": "3b82d379-f008-43ed-a5f7-da5b023cb343",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Grep · `toolu_014gp2Bfc2RsuDHtq9Q6JzKt`</summary>

```json
{
  "pattern": "cost|Cost|COST|computation|Computation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "4d708c9b-6681-49ea-980b-a0db49ab78aa",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011LuM6oVEchPsyAXMDk7h2F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3883,
      "cache_read_input_tokens": 25081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3883,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 52 · 2026-05-25T20:44:07.723Z_

<details><summary>↩ Tool result · `toolu_014gp2Bfc2RsuDHtq9Q6JzKt`</summary>

```text
Found 1 file
artifacts/_project/paper/analysis.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "4cbbc687-2a04-4866-abdf-27fa344b5f85"
}
```

</details>

---


### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 29004,
    "tool_uses": 16,
    "duration_ms": 14969
  },
  "last_tool_name": "Bash",
  "uuid": "e6d70c1d-4b68-4559-ab3d-ceb3fdb68e16",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01RPH4nZShvHkdydRUD9C31h`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts -name \"*.tex\" | xargs grep -l \"cost\\|Cost\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "801d994b-f4dc-46f5-9719-2b961a7ff832",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011LuM6oVEchPsyAXMDk7h2F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3883,
      "cache_read_input_tokens": 25081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3883,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 55 · 2026-05-25T20:44:07.906Z_

<details><summary>↩ Tool result · `toolu_01RPH4nZShvHkdydRUD9C31h`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "bad96293-ac7c-47d0-a788-d18be4a71919"
}
```

</details>

---


### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 29647,
    "tool_uses": 17,
    "duration_ms": 16801
  },
  "last_tool_name": "Bash",
  "uuid": "c31e7859-2b5a-4c47-8a0f-1e350408cdb9",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_012Pthtn5B57fspechqfAjP9`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/sections/ 2>/dev/null || echo \"Directory does not exist\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "43e8f535-a86e-4797-8161-880a1593d925",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V22CyeJxqk6PJ5gz7NeBAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 28964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 635,
        "ephemeral_1h_input_tokens": 0
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

_source line 58 · 2026-05-25T20:44:09.706Z_

<details><summary>↩ Tool result · `toolu_012Pthtn5B57fspechqfAjP9`</summary>

```text
Directory does not exist
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "4729154b-b4e7-4c57-9e5d-26903956d633"
}
```

</details>

---


### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_11/…",
  "usage": {
    "total_tokens": 29651,
    "tool_uses": 18,
    "duration_ms": 16895
  },
  "last_tool_name": "Glob",
  "uuid": "05029fb8-e3d7-45db-9197-190e24de4bf8",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Glob · `toolu_01VxKWQaaR5tmK4jjQvw8HYS`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/**/*tab*cost*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "68863f8c-c6dd-4bbf-aea1-89caf7b64361",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V22CyeJxqk6PJ5gz7NeBAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 28964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 635,
        "ephemeral_1h_input_tokens": 0
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

_source line 61 · 2026-05-25T20:44:09.793Z_

<details><summary>↩ Tool result · `toolu_01VxKWQaaR5tmK4jjQvw8HYS`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "0928c632-0c61-428b-a361-6a2fb86b50c6"
}
```

</details>

---


### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 29655,
    "tool_uses": 19,
    "duration_ms": 17211
  },
  "last_tool_name": "Bash",
  "uuid": "ef2fcc0c-2712-4523-b3f2-c7d054c87557",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_01HSWh6MvidpfG4osm2VRoTe`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts -name \"tab_*.tex\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "2167ea0b-e9c7-4294-983b-dd4ec1cdae4b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V22CyeJxqk6PJ5gz7NeBAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 28964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 635,
        "ephemeral_1h_input_tokens": 0
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

_source line 64 · 2026-05-25T20:44:10.116Z_

<details><summary>↩ Tool result · `toolu_01HSWh6MvidpfG4osm2VRoTe`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_mmlu_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_qwen15b_results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/data/tab_statistical_tests.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_mmlu_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_statistical_tests.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_qwen15b_results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_gar_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "db360134-5d51-4f7f-9195-596f0725cedf"
}
```

</details>

---


### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Running grep -r \"tab_cost\\|cost\\|Cost\\|computational\\|Com…",
  "usage": {
    "total_tokens": 30721,
    "tool_uses": 20,
    "duration_ms": 19218
  },
  "last_tool_name": "Bash",
  "uuid": "56caec9f-f280-4760-8314-6a2b71e512b7",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Bash · `toolu_01PvatRKQkZV7eoscK6tbS5U`</summary>

```json
{
  "command": "grep -r \"tab_cost\\|cost\\|Cost\\|computational\\|Computational\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/*.tex 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "a4ded0c7-eec0-4949-a648-8fe302cde80a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ReyvAN7ijqt8S4yH5gJ3FP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1058,
      "cache_read_input_tokens": 29599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1058,
        "ephemeral_1h_input_tokens": 0
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

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 30725,
    "tool_uses": 21,
    "duration_ms": 19230
  },
  "last_tool_name": "Bash",
  "uuid": "907a6417-36a8-49e6-8165-0c9e5e470b55",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Bash · `toolu_01FqQCyshDqfa4jaMKT9yjrJ`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/ | grep -i \"tab\\|cost\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "4037c5a6-dbc8-4fbe-ae5b-3e472ffed917",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ReyvAN7ijqt8S4yH5gJ3FP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1058,
      "cache_read_input_tokens": 29599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1058,
        "ephemeral_1h_input_tokens": 0
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

_source line 69 · 2026-05-25T20:44:12.166Z_

<details><summary>↩ Tool result · `toolu_01PvatRKQkZV7eoscK6tbS5U`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "f6d6414f-1362-4e0b-b9df-3567998bc91d"
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-25T20:44:12.168Z_

<details><summary>↩ Tool result · `toolu_01FqQCyshDqfa4jaMKT9yjrJ`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu     932 May 24 15:13 tab_dataset_stats.tex
-rw-r--r-- 1 ubuntu ubuntu    1593 May 24 15:13 tab_gar_robustness.tex
-rw-r--r-- 1 ubuntu ubuntu     962 May 24 15:13 tab_mmlu_detail.tex
-rw-r--r-- 1 ubuntu ubuntu    1450 May 24 15:13 tab_qwen15b_results.tex
-rw-r--r-- 1 ubuntu ubuntu    1398 May 22 15:49 table_steering_full.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "41f70b11-96d6-4e95-810a-6c62da4f4b2b"
}
```

</details>

---


### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "description": "Running grep -r \"1\\.2\\|7\\.[89]\\|gap\\|Gap\" /home/ubuntu/.a…",
  "usage": {
    "total_tokens": 31188,
    "tool_uses": 22,
    "duration_ms": 21005
  },
  "last_tool_name": "Bash",
  "uuid": "9fdebd91-1e03-4fcb-8eea-00833c2fcf41",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_0147NawQfRea9Y3BvAD4hUw2`</summary>

```json
{
  "command": "grep -r \"1\\.2\\|7\\.[89]\\|gap\\|Gap\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/*.tex 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "8b0eb7d1-a885-4abf-9bac-f29a601508f3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AzWoiJuUkpcLKXzQtHxWXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 457,
      "cache_read_input_tokens": 30657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 457,
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

_source line 73 · 2026-05-25T20:44:13.910Z_

<details><summary>↩ Tool result · `toolu_0147NawQfRea9Y3BvAD4hUw2`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex:2 & $-$0.042 & 67.9 & 14.7$\times$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex:Recall from \S\ref{sec:experiments} that teacher-forced GAR-ours reaches 0.49 for all fine-tuned variants, while autoregressive GAR-ours drops to 0.016, a 30$\times$ gap. We decompose this gap by comparing same-distribution and cross-distribution evaluation. Under same-distribution evaluation (teacher-forced UltraChat text), GAR-ours is approximately 0.49, confirming that the model has learned the intended attention pattern on the training distribution. Under cross-distribution evaluation (model-generated text), GAR-ours drops to 0.016. The training itself is sound; the failure is one of generalization.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex:GAR-Dongre provides a revealing control. Across both evaluation conditions, GAR-Dongre remains uniformly low (0.01--0.02) with no distribution gap. The distribution shift selectively destroys the concentrated attention pattern captured by GAR-ours (last-token, summary-position attention) while leaving the diffuse attention pattern captured by GAR-Dongre (averaged across all positions) unaffected. This selectivity implies that the distribution shift disrupts a specific learned routing behavior rather than attention computation in general.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex:\caption{GAR robustness across token selection strategies. We evaluate four ways to select the token position for gradient attribution: \textbf{Last} (final token of each turn), \textbf{All} (mean over all tokens), \textbf{First} (first token), and \textbf{Goal-only} (goal token as in \citet{dongre2024multi}). Turn-1 and Mid-turn GAR are measured under autoregressive generation on 50 held-out conversations. Gap Ratio = Turn-1 / Mid-turn; lower indicates better gradient preservation across turns.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex:\textbf{Token Selection} & \textbf{Condition} & \textbf{Turn-1 GAR} & \textbf{Mid-turn GAR} & \textbf{Gap Ratio} $\downarrow$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex:  & TG        & 0.3938 & 0.3254 & 1.21$\times$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_mmlu_detail.tex:Other          & 68.25 & 67.59 & 68.12 & 67.95 & 67.06 & 66.80 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/table_steering_full.tex:A visual gap separates the phase-transition boundary: GAR jumps sharply between $\beta$\,=\,2 and $\beta$\,=\,3 across all settings.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "9c7a991e-a922-49a0-bdea-1f69079b7e61"
}
```

</details>

---


### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a2e9bc3449092ab59",
  "tool_use_id": "toolu_01323fxcv4ZaHxVyx6rBpkYR",
  "status": "completed",
  "output_file": "",
  "summary": "Find crossmodel and perseed tables",
  "usage": {
    "total_tokens": 32299,
    "tool_uses": 22,
    "duration_ms": 30052
  },
  "uuid": "a217849f-bf29-4e71-876f-610504f8c66c",
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280"
}
```

---


### Tool result

_source line 75 · 2026-05-25T20:44:22.912Z_

<details><summary>↩ Tool result · `toolu_01323fxcv4ZaHxVyx6rBpkYR`</summary>

```text
Perfect! Now let me compile a comprehensive summary with all the exact file paths and relevant content:

## Summary of Findings

I've found all the requested files in the turn_residual_gating project. Here are the exact file paths and relevant content:

### 1. Crossmodel Detail Table (tab_crossmodel_detail)
**File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex`

**Relevant lines:** Lines 1-32 (full table)
- Contains cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct
- **Key SS gap ratios mentioned:**
  - Line 22: Qwen SS condition shows **1.2$\times$** gap (the lowest gap ratio)
  - Line 20: Qwen TG shows **7.9$\times$** gap
  - Lines 25-28: Llama results including gap ratios

### 2. Per-seed Table for TG (ThreadGate)
**File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex`

**Relevant lines:** Lines 1-30 (full table)
- Per-seed detailed results for ThreadGate (TG) with seeds 42 and 123
- TF evaluation uses 200 held-out conversations
- AR evaluation uses 5 model-generated conversations with 10 turns each
- Line 26: Shows gap ratio (TF/AR GAR-ours) values: 32.1 and 30.6 with mean 31.4 ± 1.1

### 3. Per-seed Table for SS (Scheduled Sampling)
**File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex`

**Relevant lines:** Lines 1-32 (full table)
- Per-seed detailed results for Scheduled Sampling (SS) with seeds 42, 123, 456
- TF evaluation: N=200, T=3 on held-out eval_200 set
- AR evaluation: N=50 gen-mode

### 4. Cost Table
**Result:** No dedicated cost/computational cost table (tab_cost) was found in the project. The search found no files matching "*cost*" patterns in the artifacts directory.

### 5. TEX Files with SS Gap Ratio Values
**File path 1:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex`

**Relevant lines with SS gap ratios:**
- Line 14: SS (Last token selection): **1.15$\times$** gap ratio
- Line 19: SS (All tokens): **1.38$\times$** gap ratio
- Line 24: SS (First token): **1.83$\times$** gap ratio
- Line 29: SS (Goal-only): **1.02$\times$** gap ratio

**File path 2:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_mmlu_detail.tex`

**File path 3:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex`

**Relevant lines with gaps:**
- Line 20: Mentions 14.7$\times$ magnitude ratio
- Contains discussion of 30$\times$ gap between teacher-forced and autoregressive GAR values
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "365c6e98-dfd0-4bf6-85d2-7276115441a6",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Find the exact file paths for:\n1. The crossmodel detail table (tab_crossmodel_detail or similar) - likely in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/ or paper/sections/\n2. The perseed table for TG (tab_perseed or similar)\n3. The cost table (tab_cost or similar)\n4. Any tex files in paper/sections/ that mention \"SS\" gap ratio like \"1.2\" or \"7.8\" or \"7.9\"\n\nSearch in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/\n\nReport back the exact file paths and the relevant line numbers/content.",
    "agentId": "a2e9bc3449092ab59",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me compile a comprehensive summary with all the exact file paths and relevant content:\n\n## Summary of Findings\n\nI've found all the requested files in the turn_residual_gating project. Here are the exact file paths and relevant content:\n\n### 1. Crossmodel Detail Table (tab_crossmodel_detail)\n**File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex`\n\n**Relevant lines:** Lines 1-32 (full table)\n- Contains cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct\n- **Key SS gap ratios mentioned:**\n  - Line 22: Qwen SS condition shows **1.2$\\times$** gap (the lowest gap ratio)\n  - Line 20: Qwen TG shows **7.9$\\times$** gap\n  - Lines 25-28: Llama results including gap ratios\n\n### 2. Per-seed Table for TG (ThreadGate)\n**File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex`\n\n**Relevant lines:** Lines 1-30 (full table)\n- Per-seed detailed results for ThreadGate (TG) with seeds 42 and 123\n- TF evaluation uses 200 held-out conversations\n- AR evaluation uses 5 model-generated conversations with 10 turns each\n- Line 26: Shows gap ratio (TF/AR GAR-ours) values: 32.1 and 30.6 with mean 31.4 ± 1.1\n\n### 3. Per-seed Table for SS (Scheduled Sampling)\n**File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex`\n\n**Relevant lines:** Lines 1-32 (full table)\n- Per-seed detailed results for Scheduled Sampling (SS) with seeds 42, 123, 456\n- TF evaluation: N=200, T=3 on held-out eval_200 set\n- AR evaluation: N=50 gen-mode\n\n### 4. Cost Table\n**Result:** No dedicated cost/computational cost table (tab_cost) was found in the project. The search found no files matching \"*cost*\" patterns in the artifacts directory.\n\n### 5. TEX Files with SS Gap Ratio Values\n**File path 1:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex`\n\n**Relevant lines with SS gap ratios:**\n- Line 14: SS (Last token selection): **1.15$\\times$** gap ratio\n- Line 19: SS (All tokens): **1.38$\\times$** gap ratio\n- Line 24: SS (First token): **1.83$\\times$** gap ratio\n- Line 29: SS (Goal-only): **1.02$\\times$** gap ratio\n\n**File path 2:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_mmlu_detail.tex`\n\n**File path 3:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex`\n\n**Relevant lines with gaps:**\n- Line 20: Mentions 14.7$\\times$ magnitude ratio\n- Contains discussion of 30$\\times$ gap between teacher-forced and autoregressive GAR values"
      }
    ],
    "totalDurationMs": 30053,
    "totalTokens": 33185,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1112,
      "cache_read_input_tokens": 31114,
      "output_tokens": 954,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1112
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 954,
          "cache_read_input_tokens": 31114,
          "cache_creation_input_tokens": 1112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1112,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 5,
      "searchCount": 10,
      "bashCount": 7,
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

_source line 76_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XStzQui7C3ZgbTR7JA756i`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "15cd5737-0631-4822-abc3-8127fc32f888",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXGLTj4uxK4z1act9fjEG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 26904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1269
      },
      "output_tokens": 69,
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

_source line 77 · 2026-05-25T20:44:25.687Z_

<details><summary>↩ Tool result · `toolu_01XStzQui7C3ZgbTR7JA756i`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "ebde9ee8-ec8b-4f60-ab17-9a3045445388",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Assistant

_source line 78_

<details><summary>Logged reasoning block</summary>

```text
Let me now read the key files and search the registry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "932ce33b-b8bd-4581-aa3f-35e7baa812ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qzWbbLAXX9Syc6tAa8HZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 28173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
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

_source line 79_

<details open><summary>🔧 Tool call — Read · `toolu_01N1Yi8dN55CTHcU4gZPLZjW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "a2b69b90-8b9b-4846-ab57-1c905cae89af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qzWbbLAXX9Syc6tAa8HZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 28173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
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

_source line 80 · 2026-05-25T20:44:29.555Z_

<details><summary>↩ Tool result · `toolu_01N1Yi8dN55CTHcU4gZPLZjW`</summary>

```text
1	% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct
2	% Conditions shared by both models: Base, ThreadGate, LoRA-only
3	% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0
4	% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4
5	% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)
6	\begin{table*}[t]
7	\centering
8	\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.
9	Gap ratio = TF GAR / AR GAR; lower is better (less exposure bias).
10	Qwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).
11	Llama AR GAR and gaps are mean-based; median-based TG gap is 27$\times$ (\S\ref{subsec:cross-model}).}
12	\label{tab:crossmodel-detail}
13	\small
14	\begin{tabular}{@{}ll ccccc@{}}
15	\toprule
16	\textbf{Model} & \textbf{Condition} & \textbf{TF GAR}$\uparrow$ & \textbf{AR GAR}$\uparrow$ & \textbf{TF PPL}$\downarrow$ & \textbf{AR PPL}$\downarrow$ & \textbf{Gap}$\downarrow$ \\
17	\midrule
18	\multirow{4}{*}{Qwen-7B}
19	  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\times$ \\
20	  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\times$ \\
21	  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\times$ \\
22	  & \textbf{SS} & 0.498 & \textbf{0.401} & 2.78 & 1.441 & \textbf{1.2$\times$} \\
23	\midrule
24	\multirow{4}{*}{Llama-8B}
25	  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\times$ \\
26	  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\times$ \\
27	  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\times$ \\
28	  & \textbf{SS} & 0.477 & \textbf{0.166} & 2.82 & 1.370 & \textbf{2.9$\times$} \\
29	\bottomrule
30	\end{tabular}
31	\end{table*}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "f31977e4-f38a-4a36-bd27-25c61cebe15e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
      "content": "% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct\n% Conditions shared by both models: Base, ThreadGate, LoRA-only\n% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0\n% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4\n% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)\n\\begin{table*}[t]\n\\centering\n\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}\n\\label{tab:crossmodel-detail}\n\\small\n\\begin{tabular}{@{}ll ccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Condition} & \\textbf{TF GAR}$\\uparrow$ & \\textbf{AR GAR}$\\uparrow$ & \\textbf{TF PPL}$\\downarrow$ & \\textbf{AR PPL}$\\downarrow$ & \\textbf{Gap}$\\downarrow$ \\\\\n\\midrule\n\\multirow{4}{*}{Qwen-7B}\n  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\\times$ \\\\\n  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\\times$ \\\\\n  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\\times$ \\\\\n  & \\textbf{SS} & 0.498 & \\textbf{0.401} & 2.78 & 1.441 & \\textbf{1.2$\\times$} \\\\\n\\midrule\n\\multirow{4}{*}{Llama-8B}\n  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\\times$ \\\\\n  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\\times$ \\\\\n  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\\times$ \\\\\n  & \\textbf{SS} & 0.477 & \\textbf{0.166} & 2.82 & 1.370 & \\textbf{2.9$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---


### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Read · `toolu_01EBixQ6aJWE6JvCYgXEtdbS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "ab75fbaf-ef1e-4949-9f1c-16012d19cff0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qzWbbLAXX9Syc6tAa8HZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 28173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
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

_source line 82 · 2026-05-25T20:44:29.983Z_

<details><summary>↩ Tool result · `toolu_01EBixQ6aJWE6JvCYgXEtdbS`</summary>

```text
1	% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123
2	% TF eval: N=200 held-out conversations
3	% AR eval: N=5, T=10 model-generated conversations (original eval protocol)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations.
8	AR evaluation uses 5 model-generated conversations with 10 turns each.}
9	\label{tab:perseed-tg}
10	\resizebox{\columnwidth}{!}{
11	\begin{tabular}{@{}l cc c@{}}
12	\toprule
13	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Mean $\pm$ Std} \\
14	\midrule
15	\multicolumn{4}{@{}l}{\textit{Teacher-Forced (TF)}} \\
16	\quad GAR-ours $\uparrow$   & 0.504 & 0.505 & 0.504 $\pm$ 0.001 \\
17	\quad GAR-Dongre $\uparrow$ & 0.015 & 0.012 & 0.014 $\pm$ 0.002 \\
18	\quad PPL $\downarrow$       & 2.784 & 2.780 & 2.782 $\pm$ 0.003 \\
19	\midrule
20	\multicolumn{4}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
21	\quad GAR-ours $\uparrow$   & 0.016 & 0.017 & 0.016 $\pm$ 0.001 \\
22	\quad GAR-Dongre $\uparrow$ & 0.019 & 0.018 & 0.019 $\pm$ 0.001 \\
23	\quad PPL $\downarrow$       & 1.360 & 1.386 & 1.373 $\pm$ 0.018 \\
24	\midrule
25	\multicolumn{4}{@{}l}{\textit{Derived}} \\
26	\quad Gap ratio (TF/AR GAR-ours) $\downarrow$ & 32.1 & 30.6 & 31.4 $\pm$ 1.1 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "d51bca3d-c8d2-4268-a118-d9996088dd40",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex",
      "content": "% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123\n% TF eval: N=200 held-out conversations\n% AR eval: N=5, T=10 model-generated conversations (original eval protocol)\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses 5 model-generated conversations with 10 turns each.}\n\\label{tab:perseed-tg}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{@{}l cc c@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Teacher-Forced (TF)}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.504 & 0.505 & 0.504 $\\pm$ 0.001 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.015 & 0.012 & 0.014 $\\pm$ 0.002 \\\\\n\\quad PPL $\\downarrow$       & 2.784 & 2.780 & 2.782 $\\pm$ 0.003 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 0$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.016 & 0.017 & 0.016 $\\pm$ 0.001 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.019 & 0.018 & 0.019 $\\pm$ 0.001 \\\\\n\\quad PPL $\\downarrow$       & 1.360 & 1.386 & 1.373 $\\pm$ 0.018 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Derived}} \\\\\n\\quad Gap ratio (TF/AR GAR-ours) $\\downarrow$ & 32.1 & 30.6 & 31.4 $\\pm$ 1.1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  }
}
```

</details>

---


### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Read · `toolu_018TqXVacW75dUbTmu1KhmgF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "7ddda691-572f-4a13-9352-e652a2e74254",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qzWbbLAXX9Syc6tAa8HZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 28173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
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

_source line 84 · 2026-05-25T20:44:30.938Z_

<details><summary>↩ Tool result · `toolu_018TqXVacW75dUbTmu1KhmgF`</summary>

```text
1	% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456
2	% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)
3	% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\text{valid}} \approx 39$).}
8	\label{tab:perseed-ss}
9	\resizebox{\columnwidth}{!}{
10	\begin{tabular}{@{}l ccc c@{}}
11	\toprule
12	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean $\pm$ Std} \\
13	\midrule
14	\multicolumn{5}{@{}l}{\textit{Teacher-Forced (TF)}} \\
15	\quad GAR-ours $\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\pm$ 0.032 \\
16	\quad GAR-Dongre $\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\pm$ 0.014 \\
17	\quad PPL $\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\pm$ 0.097 \\
18	\midrule
19	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
20	\quad GAR-ours $\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\pm$ 0.047 \\
21	\quad PPL $\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\pm$ 0.002 \\
22	\midrule
23	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 3$}} \\
24	\quad GAR-ours $\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\pm$ 0.008 \\
25	\quad PPL $\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\pm$ 0.022 \\
26	\midrule
27	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 5$}} \\
28	\quad GAR-ours $\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\pm$ 0.001 \\
29	\quad PPL $\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\pm$ 0.013 \\
30	\bottomrule
31	\end{tabular}}
32	\end{table}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "e6e0788f-839e-49e4-82be-f851331bb15c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex",
      "content": "% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456\n% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)\n% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\\text{valid}} \\approx 39$).}\n\\label{tab:perseed-ss}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{@{}l ccc c@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 456} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Teacher-Forced (TF)}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\\pm$ 0.032 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\\pm$ 0.014 \\\\\n\\quad PPL $\\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\\pm$ 0.097 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 0$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\\pm$ 0.047 \\\\\n\\quad PPL $\\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\\pm$ 0.002 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 3$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\\pm$ 0.008 \\\\\n\\quad PPL $\\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\\pm$ 0.022 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 5$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\\pm$ 0.001 \\\\\n\\quad PPL $\\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\\pm$ 0.013 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  }
}
```

</details>

---


### Tool call

_source line 85_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_012a5p79AqMyEyrEJ8RB7tTm`</summary>

```json
{
  "project": "turn_residual_gating",
  "filters": {
    "exp_id": "tg"
  },
  "fields": [
    "*"
  ],
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "49a1f5f1-7ef8-4302-a7d0-9d9fcfecace3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qzWbbLAXX9Syc6tAa8HZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 28173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
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

_source line 86 · 2026-05-25T20:44:32.128Z_

<details><summary>↩ Tool result · `toolu_012a5p79AqMyEyrEJ8RB7tTm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.204}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "b5f0b564-c661-4dc6-8e6e-f96614a6e416",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.204}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.204}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Grep · `toolu_01AM6vYogabnd2ZsYysaUDSy`</summary>

```json
{
  "pattern": "1\\.2[×x\\\\times]|7\\.[89][×x\\\\times]|SS.*gap|gap.*SS|1\\.3[×x\\\\times]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
  "output_mode": "content",
  "-n": true,
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "302358a6-f3e2-4bf0-9af4-12a15bdbdf3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qzWbbLAXX9Syc6tAa8HZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 28173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
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

_source line 88 · 2026-05-25T20:44:33.844Z_

<details><summary>↩ Tool result · `toolu_01AM6vYogabnd2ZsYysaUDSy`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-39-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-40-
paper/sections/analysis.tex:41:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-42-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-36-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-37-
paper/sections/experiments.tex:38:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-39-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-40-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-226-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-227-Mean cos sim & $-$0.042 & +0.005 \\
paper/sections/appendix.tex:228:Neg-layer \% & 67.9\% & 53.1\% \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-229-NTP/GAR mag ratio & 14.7$\times$ & 25.7$\times$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-230-\bottomrule
--
paper/sections/appendix.tex-489-Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-490-
paper/sections/appendix.tex:491:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-492-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-493-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-498-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-499-\includegraphics[width=\columnwidth]{fig_eb_scaling.pdf}
paper/sections/appendix.tex:500:\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.2$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
paper/sections/appendix.tex-501-\label{fig:eb-scaling}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-502-\end{figure}
--
paper/sections/appendix.tex-506-To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-507-
paper/sections/appendix.tex:508:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-509-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-510-\begin{figure}[t]
--
paper/sections/appendix.tex-631-Tables~\ref{tab:perseed-ss} and~\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-632-
paper/sections/appendix.tex:633:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-634-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-635-\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\pm0.001$) and similar AR GAR (0.064 vs.\ 0.055), with gap ratios of 7.9$\times$ and 9.1$\times$ respectively. The 15\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-811-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-812-\paragraph{Architectural differences.}
paper/sections/appendix.tex:813:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-814-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-815-\paragraph{Training dynamics.}
paper/sections/appendix.tex:816:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-817-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-818-\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "4da9f22d-dc85-4c94-bb03-6dc1072d77e1",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-39-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-40-\npaper/sections/analysis.tex:41:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-42-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-36-\\end{figure}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-37-\npaper/sections/experiments.tex:38:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-39-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-40-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-226-\\midrule\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-227-Mean cos sim & $-$0.042 & +0.005 \\\\\npaper/sections/appendix.tex:228:Neg-layer \\% & 67.9\\% & 53.1\\% \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-229-NTP/GAR mag ratio & 14.7$\\times$ & 25.7$\\times$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-230-\\bottomrule\n--\npaper/sections/appendix.tex-489-Figure~\\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-490-\npaper/sections/appendix.tex:491:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-492-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-493-[Omitted long context line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-498-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-499-\\includegraphics[width=\\columnwidth]{fig_eb_scaling.pdf}\npaper/sections/appendix.tex:500:\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}\npaper/sections/appendix.tex-501-\\label{fig:eb-scaling}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-502-\\end{figure}\n--\npaper/sections/appendix.tex-506-To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-507-\npaper/sections/appendix.tex:508:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-509-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-510-\\begin{figure}[t]\n--\npaper/sections/appendix.tex-631-Tables~\\ref{tab:perseed-ss} and~\\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-632-\npaper/sections/appendix.tex:633:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-634-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-635-\\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\\pm0.001$) and similar AR GAR (0.064 vs.\\ 0.055), with gap ratios of 7.9$\\times$ and 9.1$\\times$ respectively. The 15\\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-811-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-812-\\paragraph{Architectural differences.}\npaper/sections/appendix.tex:813:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-814-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-815-\\paragraph{Training dynamics.}\npaper/sections/appendix.tex:816:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-817-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-818-\\begin{table}[t]",
    "numLines": 49
  }
}
```

</details>

---


### Assistant

_source line 89_

<details><summary>Logged reasoning block</summary>

```text
Let me read the specific lines that were omitted to understand the full context. I need to see:
1. experiments.tex line 38 (SS gap mention)
2. analysis.tex line 41 (SS gap mention)
3. appendix.tex lines 491, 500, 508, 633, 813, 816
4. The cost table in appendix.tex

Also need to search registry properly for TG per-seed data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "d211fe95-629f-4960-9fce-a21148734c63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173TuaG12jSnESkFR1pJXSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5422,
      "cache_read_input_tokens": 28619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5422
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

_source line 90_

Let me read the omitted lines and find the cost table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "3082f0f1-bb6b-41c8-9784-0420559e5003",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173TuaG12jSnESkFR1pJXSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5422,
      "cache_read_input_tokens": 28619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5422
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

_source line 91_

<details open><summary>🔧 Tool call — Read · `toolu_01SetqyjuZ5J4zPLJnRHrvv2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "offset": 35,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "0444ce7b-7e8c-43dd-945b-e288d032cc34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173TuaG12jSnESkFR1pJXSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5422,
      "cache_read_input_tokens": 28619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5422
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

_source line 92 · 2026-05-25T20:44:39.901Z_

<details><summary>↩ Tool result · `toolu_01SetqyjuZ5J4zPLJnRHrvv2`</summary>

```text
35	  \label{fig:ss-gap}
36	\end{figure}
37	
38	Scheduled sampling (SS; \citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\pm0.047$, compressing the gap from 7.9$\times$ to ${\sim}$1.2$\times$ (TF GAR $0.498\pm0.004$) with no PPL cost ($1.441\pm0.002$; Figure~\ref{fig:ss-gap}; per-seed details in Appendix~\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\beta$\,=\,5: $0.717\pm0.001$, std 0.047$\to$0.001; Figure~\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\ 3; \S\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
39	
40	
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "4a68e7bc-e517-47da-9379-eaaab9555ddd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
      "content": "  \\label{fig:ss-gap}\n\\end{figure}\n\nScheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n\n\n",
      "numLines": 7,
      "startLine": 35,
      "totalLines": 41
    }
  }
}
```

</details>

---


### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Read · `toolu_015GistqBikrAmXdLPevFvvp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "offset": 38,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "3e62d0f1-8862-4351-95d1-49e9b6b15937",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173TuaG12jSnESkFR1pJXSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5422,
      "cache_read_input_tokens": 28619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5422
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

_source line 94 · 2026-05-25T20:44:40.411Z_

<details><summary>↩ Tool result · `toolu_015GistqBikrAmXdLPevFvvp`</summary>

```text
38	
39	We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\,$>$\,100\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a in Appendix~\ref{sec:appendix-llama}; per-turn values in Appendix~\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\,=\,0.793) while Llama dips at late layers (L25\,=\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.
40	
41	Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\sim}$1.2$\times$ likely due to fewer training epochs (2 vs.\ 3). The phase transition is architecture-dependent: $\beta$\,=\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\beta$\,=\,5 (GAR 0.791, exceeding Qwen SS 0.717; Appendix~\ref{sec:appendix-llama-ss}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern (79.8\% GAR decay, $\beta$-steering recovery to 0.715; Appendix~\ref{sec:appendix-1.5b}).
42	
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "be5764dd-0310-4a9a-80ec-da7f34bf8de6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
      "content": "\nWe replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}; per-turn values in Appendix~\\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.\n\nScheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.2$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717; Appendix~\\ref{sec:appendix-llama-ss}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern (79.8\\% GAR decay, $\\beta$-steering recovery to 0.715; Appendix~\\ref{sec:appendix-1.5b}).\n\n",
      "numLines": 6,
      "startLine": 38,
      "totalLines": 43
    }
  }
}
```

</details>

---


### Tool call

_source line 95_

<details open><summary>🔧 Tool call — Read · `toolu_01KAATKA8t5ubUdvoApo91Fd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 488,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "e0a5fae6-a55c-453c-9d8c-0b88b85f89fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173TuaG12jSnESkFR1pJXSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5422,
      "cache_read_input_tokens": 28619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5422
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

_source line 96 · 2026-05-25T20:44:41.331Z_

<details><summary>↩ Tool result · `toolu_01KAATKA8t5ubUdvoApo91Fd`</summary>

```text
488	
489	Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
490	
491	\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.9$\times$) while PCGrad shows the largest (16.7$\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\sim}$1.2$\times$, the only variant approaching parity. The ordering of gap ratios (SS $\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\sim$27$\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\ 28 layers), which provides more layers for distributional drift to compound through.
492	
493	\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\,=\,50), ThreadGate's gap is 8$\times$; at 10 turns ($N$\,=\,5), it widens to 31$\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.
494	
495	\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\sim}$1.2$\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\ref{sec:appendix-steering-viz}).
496	
497	\begin{figure}[t]
498	\centering
499	\includegraphics[width=\columnwidth]{fig_eb_scaling.pdf}
500	\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.2$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
501	\label{fig:eb-scaling}
502	\end{figure}
503	
504	\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
505	
506	To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
507	
508	All six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\S\ref{subsec:ss}).}
509	
510	\begin{figure}[t]
511	\centering
512	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "c0f8282b-daf0-4875-9d72-9cdaa78e591c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\nFigure~\\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).\n\n\\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.9$\\times$) while PCGrad shows the largest (16.7$\\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\\sim}$1.2$\\times$, the only variant approaching parity. The ordering of gap ratios (SS $\\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\\sim$27$\\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\\ 28 layers), which provides more layers for distributional drift to compound through.\n\n\\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\\,=\\,50), ThreadGate's gap is 8$\\times$; at 10 turns ($N$\\,=\\,5), it widens to 31$\\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.\n\n\\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\\sim}$1.2$\\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\\ref{sec:appendix-steering-viz}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_eb_scaling.pdf}\n\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}\n\\label{fig:eb-scaling}\n\\end{figure}\n\n\\section{Per-Turn AR GAR Dynamics}\\label{sec:appendix-ar-gar-dynamics}\n\nTo characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.\n\nAll six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\\S\\ref{subsec:ss}).}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_curves.pdf}",
      "numLines": 25,
      "startLine": 488,
      "totalLines": 851
    }
  }
}
```

</details>

---


### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Read · `toolu_01Ea26GN29fcAY7X7vATsh2H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 505,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "44d37db6-f56a-4ec7-80e9-ca483ce62a95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173TuaG12jSnESkFR1pJXSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5422,
      "cache_read_input_tokens": 28619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5422
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

_source line 98 · 2026-05-25T20:44:42.269Z_

<details><summary>↩ Tool result · `toolu_01Ea26GN29fcAY7X7vATsh2H`</summary>

```text
505	
506	To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
507	
508	All six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\S\ref{subsec:ss}).}
509	
510	\begin{figure}[t]
511	\centering
512	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
513	\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}
514	\label{fig:kl_ar_gar_curves}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "9a4f4bc6-adc4-4ff3-999f-316c1c73de4f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\nTo characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.\n\nAll six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\\S\\ref{subsec:ss}).}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_curves.pdf}\n\\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}\n\\label{fig:kl_ar_gar_curves}",
      "numLines": 10,
      "startLine": 505,
      "totalLines": 851
    }
  }
}
```

</details>

---


### Tool call

_source line 99_

<details open><summary>🔧 Tool call — Read · `toolu_016MbA4KTfyE4bfHMg8FndXa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 628,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "89f3fde8-0caa-495d-ba01-741b9081f0cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173TuaG12jSnESkFR1pJXSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5422,
      "cache_read_input_tokens": 28619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5422
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

_source line 100 · 2026-05-25T20:44:43.236Z_

<details><summary>↩ Tool result · `toolu_016MbA4KTfyE4bfHMg8FndXa`</summary>

```text
628	
629	\section{Per-Seed Detailed Results}\label{sec:appendix-perseed}
630	
631	Tables~\ref{tab:perseed-ss} and~\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.
632	
633	\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\pm0.032$ across seeds under the held-out protocol (Table~\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\,=\,200 sample. AR GAR shows meaningful variance (std\,=\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\times$), seed 123 is intermediate (0.423, gap 1.3$\times$), and seed 456 is highest (0.433, gap 1.2$\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\beta$\,=\,5, the cross-seed variance nearly vanishes ($0.717\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.
634	
635	\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\pm0.001$) and similar AR GAR (0.064 vs.\ 0.055), with gap ratios of 7.9$\times$ and 9.1$\times$ respectively. The 15\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.
636	
637	\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\% overhead) vs.\ 6.5 hours for seeds 42 and 456 (8\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-generated contexts: seed 123 happens to trigger longer autoregressive generation episodes early in training, where the model produces longer outputs before hitting the max-length cutoff. Despite this training-time variance, all three seeds converge to similar final metrics, suggesting the optimization landscape is robust.
638	
639	\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}
640	
641	\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}
642	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "58951213-6f6f-4ba5-98ba-9bdf1946d417",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\n\\section{Per-Seed Detailed Results}\\label{sec:appendix-perseed}\n\nTables~\\ref{tab:perseed-ss} and~\\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.\n\n\\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\\pm0.032$ across seeds under the held-out protocol (Table~\\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\\,=\\,200 sample. AR GAR shows meaningful variance (std\\,=\\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\\times$), seed 123 is intermediate (0.423, gap 1.3$\\times$), and seed 456 is highest (0.433, gap 1.2$\\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\\beta$\\,=\\,5, the cross-seed variance nearly vanishes ($0.717\\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.\n\n\\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\\pm0.001$) and similar AR GAR (0.064 vs.\\ 0.055), with gap ratios of 7.9$\\times$ and 9.1$\\times$ respectively. The 15\\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.\n\n\\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\\% overhead) vs.\\ 6.5 hours for seeds 42 and 456 (8\\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-generated contexts: seed 123 happens to trigger longer autoregressive generation episodes early in training, where the model produces longer outputs before hitting the max-length cutoff. Despite this training-time variance, all three seeds converge to similar final metrics, suggesting the optimization landscape is robust.\n\n\\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}\n\n\\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}\n",
      "numLines": 15,
      "startLine": 628,
      "totalLines": 851
    }
  }
}
```

</details>

---


### Tool call

_source line 101_

<details open><summary>🔧 Tool call — Read · `toolu_016oFDqjZmhmL9C1ZmHHaTjg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 810,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "e783ce6a-71ce-4445-9b7d-3499e9e19605",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173TuaG12jSnESkFR1pJXSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5422,
      "cache_read_input_tokens": 28619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5422
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

_source line 102 · 2026-05-25T20:44:44.277Z_

<details><summary>↩ Tool result · `toolu_016oFDqjZmhmL9C1ZmHHaTjg`</summary>

```text
810	Table~\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\times$) is larger than Qwen's (1.2$\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\times$ (from 27$\times$ to 2.9$\times$) while Qwen reduces by 6.6$\times$ (from 7.9$\times$ to 1.2$\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\beta$-steering is more effective on Llama (0.791 vs.\ 0.717 at $\beta$\,=\,5), partially compensating for the weaker training-time compression.
811	
812	\paragraph{Architectural differences.}
813	Several architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.
814	
815	\paragraph{Training dynamics.}
816	The Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\sim}$0.20 at the end of epoch~2 (vs.\ 0.30 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (27$\times$ $\to$ 2.9$\times$ by median) but leaves a larger residual gap than Qwen's full 3-epoch schedule.
817	
818	\begin{table}[t]
819	\raggedright\small
820	\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\ Llama-3.1-8B.}
821	\label{tab:llama-vs-qwen-ss}
822	\begin{tabular}{@{}l cc@{}}
823	\toprule
824	\textbf{Metric} & \textbf{Qwen-7B} & \textbf{Llama-8B} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "30aad263-28e5-4295-a91a-8740f427791f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "Table~\\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\\times$) is larger than Qwen's (1.2$\\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\\times$ (from 27$\\times$ to 2.9$\\times$) while Qwen reduces by 6.6$\\times$ (from 7.9$\\times$ to 1.2$\\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\\beta$-steering is more effective on Llama (0.791 vs.\\ 0.717 at $\\beta$\\,=\\,5), partially compensating for the weaker training-time compression.\n\n\\paragraph{Architectural differences.}\nSeveral architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.\n\n\\paragraph{Training dynamics.}\nThe Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\\sim}$0.20 at the end of epoch~2 (vs.\\ 0.30 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (27$\\times$ $\\to$ 2.9$\\times$ by median) but leaves a larger residual gap than Qwen's full 3-epoch schedule.\n\n\\begin{table}[t]\n\\raggedright\\small\n\\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\\ Llama-3.1-8B.}\n\\label{tab:llama-vs-qwen-ss}\n\\begin{tabular}{@{}l cc@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\",
      "numLines": 15,
      "startLine": 810,
      "totalLines": 851
    }
  }
}
```

</details>

---


### Tool call

_source line 103_

<details open><summary>🔧 Tool call — Grep · `toolu_01GSV2TywAEJpBxCcBHGZe5u`</summary>

```json
{
  "pattern": "5\\.72|6\\.11|LoRA.*h|UG.*h|tab.cost|cost.*table|training.*time|train.*hour",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": true,
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "a93384ea-9fc8-49f2-8733-90beb6e30887",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173TuaG12jSnESkFR1pJXSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5422,
      "cache_read_input_tokens": 28619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5422
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

_source line 104 · 2026-05-25T20:44:46.294Z_

<details><summary>↩ Tool result · `toolu_01GSV2TywAEJpBxCcBHGZe5u`</summary>

```text
1-\section{Training Configuration}\label{sec:appendix-hyper}
2-
3:[Omitted long matching line]
4-
5-\begin{table}[t]
6-\centering\small
--
11-\textbf{Parameter} & \textbf{Value} \\
12-\midrule
13-Base model & Qwen-2.5-7B-Instruct \\
14:LoRA rank / $\alpha$ & 16 / 32 \\
15-LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16-Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17-Learning rate & $2 \times 10^{-4}$ \\
--
106-
107-The main results (Table~\ref{tab:five-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
108-
109:[Omitted long matching line]
110-
111:[Omitted long matching line]
112-
113-\paragraph{Caveats.} The $N$\,=\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.
114-
--
134-
135-All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
136-
137:[Omitted long matching line]
138-
139-\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
140-
--
168-
169-\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
170-
171:Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
172-
173:\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
174-
175-\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
176-
--
178-
179-\begin{table}[t]
180-\centering\small
181:\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20 for Base/TG/LoRA-only, $N$\,=\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}
182-\label{tab:llama-full}
183-\resizebox{\columnwidth}{!}{%
184-\begin{tabular}{lcccc}
--
204-  \label{fig:crossmodel}
205-\end{figure}
206-
207:[Omitted long matching line]
208-
209-\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}
210-
211-\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
212-
213:\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger layer count (32 vs.\ 28 layers).
214-
215-\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\% decline. This is steeper than Qwen's 70.8\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\ 28 KV heads).
216-
--
242-\begin{figure}[H]
243-\centering
244-\includegraphics[width=\columnwidth]{fig_gate_profile_heatmap.pdf}
245:\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
246-\label{fig:gate-heatmap}
247-\end{figure}
248-
--
259-
260-\subsection{Per-Turn AR GAR Decay}
261-
262:[Omitted long matching line]
263-
264-\begin{figure}[H]
265-\centering
266-\includegraphics[width=\columnwidth]{fig_ar_gar_perturn.pdf}
267:\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
268-\label{fig:ar-gar-perturn}
269-\end{figure}
270-
--
275-\begin{figure}[H]
276-  \centering
277-  \includegraphics[width=\columnwidth]{fig_bootstrap_ci.pdf}
278:  \caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\ LoRA-only, $N$\,=\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\,=\,0.454).}
279-  \label{fig:bootstrap-ci}
280-\end{figure}
281-
--
387-\begin{table}[t]
388-\centering\small
389-\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\,GB VRAM). VRAM reports peak allocated memory (excluding optimizer states).}
390:\label{tab:cost}
391-\resizebox{\columnwidth}{!}{%
392-\begin{tabular}{lcccc}
393-\toprule
--
409-\end{tabular}}
410-\end{table}
411-
412:\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
413-
414:\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 5.7--7.3 hours. PCGrad adds ${\sim}$33\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
415-
416-\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
417-
--
488-
489-Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
490-
491:[Omitted long matching line]
492-
493:[Omitted long matching line]
494-
495:[Omitted long matching line]
496-
497-\begin{figure}[t]
498-\centering
499-\includegraphics[width=\columnwidth]{fig_eb_scaling.pdf}
500:\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.2$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
501-\label{fig:eb-scaling}
502-\end{figure}
503-
504-\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
505-
506:To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
507-
508:[Omitted long matching line]
509-
510-\begin{figure}[t]
511-\centering
--
521-\label{fig:kl_ar_gar_bar}
522-\end{figure}
523-
524:[Omitted long matching line]
525-
526-\section{Per-Head KL Divergence Analysis}\label{sec:appendix-kl}
527-
--
542-\end{tabular}
543-\end{table}
544-
545:[Omitted long matching line]
546-
547-[Omitted long context line]
548-
--
578-
579-\begin{table}[t]
580-\centering\small
581:\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\,pp of the base LoRA-only checkpoint.}
582-\label{tab:mmlu}
583-\begin{tabular}{lcc}
584-\toprule
--
634-
635-\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\pm0.001$) and similar AR GAR (0.064 vs.\ 0.055), with gap ratios of 7.9$\times$ and 9.1$\times$ respectively. The 15\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.
636-
637:[Omitted long matching line]
638-
639-\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}
640-
--
644-
645-Tables~\ref{tab:perturn-qwen} and~\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\ref{tab:five-way}).
646-
647:[Omitted long matching line]
648-
649-[Omitted long context line]
650-
--
666-\begin{figure}[t]
667-  \centering
668-  \includegraphics[width=\columnwidth]{fig_perturn_llama_detail.pdf}
669:  \caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\,=\,20, 4 turns). (b)~Extended Base decay profile ($N$\,=\,5, 10 turns), showing 90\% decline.}
670-  \label{fig:perturn-llama-detail}
671-\end{figure}
672-
--
688-
689-[Omitted long context line]
690-
691:[Omitted long matching line]
692-
693-\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}
694-
--
703-
704-Table~\ref{tab:mmlu_detail} breaks down MMLU 5-shot accuracy by category (STEM, Social Sciences, Humanities, Other) for all six Qwen-2.5-7B training configurations. This analysis addresses a potential concern: that auxiliary attention objectives might divert representational capacity from general language understanding, particularly in knowledge-intensive STEM domains.
705-
706:[Omitted long matching line]
707-
708-[Omitted long context line]
709-
--
724-
725-\paragraph{Phase 1: GAR decay.} The 1.5B base model exhibits 79.8\% relative GAR decline from turn~1 to mid-turns, more severe than the 7B model's 70.8\% decline. This scale-dependent decay severity is consistent with smaller models having less redundant attention capacity: with 28 layers but only 1.5B parameters (vs.\ 7B), each layer carries proportionally more of the total representational burden, leaving less room for goal-oriented attention to persist alongside the primary NTP objective.
726-
727:\paragraph{Phase 2: Training.} ThreadGate training on 1.5B converges to TF GAR-ours of 0.498 with PPL of 2.67, closely matching the 7B results (0.504 / 2.78). The gate parameter count scales linearly with layer count (identical architecture, so ${\sim}$57K gate parameters). Training completes in 2.1 hours vs.\ 6.0 hours for 7B, reflecting the smaller model's reduced forward/backward pass cost.
728-
729-[Omitted long context line]
730-
--
738-
739-[Omitted long context line]
740-
741:[Omitted long matching line]
742-
743:[Omitted long matching line]
744-
745-[Omitted long context line]
746-
--
750-
751-\section{Extended Training Dynamics}\label{sec:appendix-training-ext}
752-
753:Figure~\ref{fig:training-6panel} presents the complete training loss landscape for all five Qwen-2.5-7B conditions (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Scheduled Sampling) plus the base model, showing NTP loss, GAR loss, and total loss across three epochs.
754-
755:[Omitted long matching line]
756-
757-[Omitted long context line]
758-
759:[Omitted long matching line]
760-
761-\begin{figure*}[t]
762-  \centering
--
773-
774-[Omitted long context line]
775-
776:\paragraph{Sustained recovery ($\beta$\,=\,5).} GAR is sustained above 0.6 throughout, with minimal per-turn decay ($<$5\% decline). At this steering strength, the constant attention bias dominates the per-turn drift, effectively replacing the lost training-time signal with an inference-time substitute. The 9\% PPL cost (1.43 $\to$ 1.77) is modest compared to the order-of-magnitude GAR recovery.
777-
778-\paragraph{Saturation regime ($\beta$\,=\,10).} GAR saturates near 1.0 across all turns but PPL degrades catastrophically ($>$3.5), as the excessive attention bias distorts the attention distribution beyond the model's capacity for coherent generation. This regime is impractical and serves as an upper bound on the steering approach.
779-
--
788-
789-\section{Llama-3.1-8B Scheduled Sampling Details}\label{sec:appendix-llama-ss}
790-
791:[Omitted long matching line]
792-
793-\paragraph{$\beta$-steering on Llama SS.}
794-Table~\ref{tab:llama-ss-steering} reports $\beta$-steering results on the Llama SS model. Unlike Qwen, $\beta$\,=\,3 does not trigger recovery on Llama (GAR 0.173 vs.\ 0.166 at $\beta$\,=\,0). At $\beta$\,=\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias at higher steering strengths, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.
--
807-\end{table}

[Showing results with pagination = limit: 250]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "586427bc-3af7-4b70-950d-e5947776db3e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1-\\section{Training Configuration}\\label{sec:appendix-hyper}\n2-\n3:[Omitted long matching line]\n4-\n5-\\begin{table}[t]\n6-\\centering\\small\n--\n11-\\textbf{Parameter} & \\textbf{Value} \\\\\n12-\\midrule\n13-Base model & Qwen-2.5-7B-Instruct \\\\\n14:LoRA rank / $\\alpha$ & 16 / 32 \\\\\n15-LoRA targets & \\texttt{q\\_proj}, \\texttt{v\\_proj} \\\\\n16-Optimizer & AdamW ($\\beta_1$\\!=\\!0.9, $\\beta_2$\\!=\\!0.999) \\\\\n17-Learning rate & $2 \\times 10^{-4}$ \\\\\n--\n106-\n107-The main results (Table~\\ref{tab:five-way}) report AR GAR from $N$\\,=\\,50 held-out conversations with a mean of 3.6 user turns. Table~\\ref{tab:n5-ar} presents complementary results on $N$\\,=\\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.\n108-\n109:[Omitted long matching line]\n110-\n111:[Omitted long matching line]\n112-\n113-\\paragraph{Caveats.} The $N$\\,=\\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.\n114-\n--\n134-\n135-All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\\ref{tab:stat-tests} consolidates the full results.\n136-\n137:[Omitted long matching line]\n138-\n139-\\paragraph{Bootstrap confidence intervals.} The 95\\% CIs in Table~\\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.\n140-\n--\n168-\n169-\\section{Llama-3.1-8B Complete Results}\\label{sec:appendix-llama}\n170-\n171:Table~\\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \\S\\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.\n172-\n173:\\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\\ 0.50).\n174-\n175-\\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\\,=\\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\\% for ThreadGate (mean 0.043, std 0.100), and 5\\% of turn-level measurements exhibit sporadic attention spikes (GAR $\\geq$ 0.4). We therefore report both mean and median.\n176-\n--\n178-\n179-\\begin{table}[t]\n180-\\centering\\small\n181:\\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\\,=\\,50); AR: autoregressive ($N$\\,=\\,20 for Base/TG/LoRA-only, $N$\\,=\\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}\n182-\\label{tab:llama-full}\n183-\\resizebox{\\columnwidth}{!}{%\n184-\\begin{tabular}{lcccc}\n--\n204-  \\label{fig:crossmodel}\n205-\\end{figure}\n206-\n207:[Omitted long matching line]\n208-\n209-\\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}\n210-\n211-\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\n212-\n213:\\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\\% longer than Qwen due to Llama's larger layer count (32 vs.\\ 28 layers).\n214-\n215-\\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\\% decline. This is steeper than Qwen's 70.8\\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\\ 28 KV heads).\n216-\n--\n242-\\begin{figure}[H]\n243-\\centering\n244-\\includegraphics[width=\\columnwidth]{fig_gate_profile_heatmap.pdf}\n245:\\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\\times$ 5 conditions) and Llama-3.1-8B (32 layers $\\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}\n246-\\label{fig:gate-heatmap}\n247-\\end{figure}\n248-\n--\n259-\n260-\\subsection{Per-Turn AR GAR Decay}\n261-\n262:[Omitted long matching line]\n263-\n264-\\begin{figure}[H]\n265-\\centering\n266-\\includegraphics[width=\\columnwidth]{fig_ar_gar_perturn.pdf}\n267:\\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\\% (turn 1$\\to$10), Llama base drops 90\\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}\n268-\\label{fig:ar-gar-perturn}\n269-\\end{figure}\n270-\n--\n275-\\begin{figure}[H]\n276-  \\centering\n277-  \\includegraphics[width=\\columnwidth]{fig_bootstrap_ci.pdf}\n278:  \\caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\\ LoRA-only, $N$\\,=\\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\\,=\\,0.454).}\n279-  \\label{fig:bootstrap-ci}\n280-\\end{figure}\n281-\n--\n387-\\begin{table}[t]\n388-\\centering\\small\n389-\\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\\,GB VRAM). VRAM reports peak allocated memory (excluding optimizer states).}\n390:\\label{tab:cost}\n391-\\resizebox{\\columnwidth}{!}{%\n392-\\begin{tabular}{lcccc}\n393-\\toprule\n--\n409-\\end{tabular}}\n410-\\end{table}\n411-\n412:\\paragraph{Parameter overhead.} ThreadGate adds ${\\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\\times$ 2K per gate MLP) and ${\\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.\n413-\n414:\\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 5.7--7.3 hours. PCGrad adds ${\\sim}$33\\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\\% (6.5h) due to efficient batched generation, while seed 123 adds 80\\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.\n415-\n416-\\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\\to$64$\\to$1 MLP forward pass per layer adds $<$0.1\\% latency. $\\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.\n417-\n--\n488-\n489-Figure~\\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).\n490-\n491:[Omitted long matching line]\n492-\n493:[Omitted long matching line]\n494-\n495:[Omitted long matching line]\n496-\n497-\\begin{figure}[t]\n498-\\centering\n499-\\includegraphics[width=\\columnwidth]{fig_eb_scaling.pdf}\n500:\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}\n501-\\label{fig:eb-scaling}\n502-\\end{figure}\n503-\n504-\\section{Per-Turn AR GAR Dynamics}\\label{sec:appendix-ar-gar-dynamics}\n505-\n506:To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.\n507-\n508:[Omitted long matching line]\n509-\n510-\\begin{figure}[t]\n511-\\centering\n--\n521-\\label{fig:kl_ar_gar_bar}\n522-\\end{figure}\n523-\n524:[Omitted long matching line]\n525-\n526-\\section{Per-Head KL Divergence Analysis}\\label{sec:appendix-kl}\n527-\n--\n542-\\end{tabular}\n543-\\end{table}\n544-\n545:[Omitted long matching line]\n546-\n547-[Omitted long context line]\n548-\n--\n578-\n579-\\begin{table}[t]\n580-\\centering\\small\n581:\\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\\,pp of the base LoRA-only checkpoint.}\n582-\\label{tab:mmlu}\n583-\\begin{tabular}{lcc}\n584-\\toprule\n--\n634-\n635-\\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\\pm0.001$) and similar AR GAR (0.064 vs.\\ 0.055), with gap ratios of 7.9$\\times$ and 9.1$\\times$ respectively. The 15\\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.\n636-\n637:[Omitted long matching line]\n638-\n639-\\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}\n640-\n--\n644-\n645-Tables~\\ref{tab:perturn-qwen} and~\\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\\ref{tab:five-way}).\n646-\n647:[Omitted long matching line]\n648-\n649-[Omitted long context line]\n650-\n--\n666-\\begin{figure}[t]\n667-  \\centering\n668-  \\includegraphics[width=\\columnwidth]{fig_perturn_llama_detail.pdf}\n669:  \\caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\\,=\\,20, 4 turns). (b)~Extended Base decay profile ($N$\\,=\\,5, 10 turns), showing 90\\% decline.}\n670-  \\label{fig:perturn-llama-detail}\n671-\\end{figure}\n672-\n--\n688-\n689-[Omitted long context line]\n690-\n691:[Omitted long matching line]\n692-\n693-\\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}\n694-\n--\n703-\n704-Table~\\ref{tab:mmlu_detail} breaks down MMLU 5-shot accuracy by category (STEM, Social Sciences, Humanities, Other) for all six Qwen-2.5-7B training configurations. This analysis addresses a potential concern: that auxiliary attention objectives might divert representational capacity from general language understanding, particularly in knowledge-intensive STEM domains.\n705-\n706:[Omitted long matching line]\n707-\n708-[Omitted long context line]\n709-\n--\n724-\n725-\\paragraph{Phase 1: GAR decay.} The 1.5B base model exhibits 79.8\\% relative GAR decline from turn~1 to mid-turns, more severe than the 7B model's 70.8\\% decline. This scale-dependent decay severity is consistent with smaller models having less redundant attention capacity: with 28 layers but only 1.5B parameters (vs.\\ 7B), each layer carries proportionally more of the total representational burden, leaving less room for goal-oriented attention to persist alongside the primary NTP objective.\n726-\n727:\\paragraph{Phase 2: Training.} ThreadGate training on 1.5B converges to TF GAR-ours of 0.498 with PPL of 2.67, closely matching the 7B results (0.504 / 2.78). The gate parameter count scales linearly with layer count (identical architecture, so ${\\sim}$57K gate parameters). Training completes in 2.1 hours vs.\\ 6.0 hours for 7B, reflecting the smaller model's reduced forward/backward pass cost.\n728-\n729-[Omitted long context line]\n730-\n--\n738-\n739-[Omitted long context line]\n740-\n741:[Omitted long matching line]\n742-\n743:[Omitted long matching line]\n744-\n745-[Omitted long context line]\n746-\n--\n750-\n751-\\section{Extended Training Dynamics}\\label{sec:appendix-training-ext}\n752-\n753:Figure~\\ref{fig:training-6panel} presents the complete training loss landscape for all five Qwen-2.5-7B conditions (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Scheduled Sampling) plus the base model, showing NTP loss, GAR loss, and total loss across three epochs.\n754-\n755:[Omitted long matching line]\n756-\n757-[Omitted long context line]\n758-\n759:[Omitted long matching line]\n760-\n761-\\begin{figure*}[t]\n762-  \\centering\n--\n773-\n774-[Omitted long context line]\n775-\n776:\\paragraph{Sustained recovery ($\\beta$\\,=\\,5).} GAR is sustained above 0.6 throughout, with minimal per-turn decay ($<$5\\% decline). At this steering strength, the constant attention bias dominates the per-turn drift, effectively replacing the lost training-time signal with an inference-time substitute. The 9\\% PPL cost (1.43 $\\to$ 1.77) is modest compared to the order-of-magnitude GAR recovery.\n777-\n778-\\paragraph{Saturation regime ($\\beta$\\,=\\,10).} GAR saturates near 1.0 across all turns but PPL degrades catastrophically ($>$3.5), as the excessive attention bias distorts the attention distribution beyond the model's capacity for coherent generation. This regime is impractical and serves as an upper bound on the steering approach.\n779-\n--\n788-\n789-\\section{Llama-3.1-8B Scheduled Sampling Details}\\label{sec:appendix-llama-ss}\n790-\n791:[Omitted long matching line]\n792-\n793-\\paragraph{$\\beta$-steering on Llama SS.}\n794-Table~\\ref{tab:llama-ss-steering} reports $\\beta$-steering results on the Llama SS model. Unlike Qwen, $\\beta$\\,=\\,3 does not trigger recovery on Llama (GAR 0.173 vs.\\ 0.166 at $\\beta$\\,=\\,0). At $\\beta$\\,=\\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias at higher steering strengths, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.\n--\n807-\\end{table}",
    "numLines": 250,
    "appliedLimit": 250
  }
}
```

</details>

---


### Assistant

_source line 105_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me read the cost table to fix INFO-2.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "2d353937-433f-4ca4-a9f0-d9e93add969f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSkwaTUiWi6Zvx4gkcB6DS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10389,
      "cache_read_input_tokens": 34041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10389
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

_source line 106_

Let me read the cost table and search for the remaining references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "4e942e54-a899-47ac-a467-4e8ff0a6d5ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSkwaTUiWi6Zvx4gkcB6DS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10389,
      "cache_read_input_tokens": 34041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10389
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

_source line 107_

<details open><summary>🔧 Tool call — Read · `toolu_01UmnfGv9c3nyWMJNbBKFm7L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 386,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "7082d415-c3fb-4f5b-8ddf-4cebf8a690c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSkwaTUiWi6Zvx4gkcB6DS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10389,
      "cache_read_input_tokens": 34041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10389
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

_source line 108 · 2026-05-25T20:44:57.853Z_

<details><summary>↩ Tool result · `toolu_01UmnfGv9c3nyWMJNbBKFm7L`</summary>

```text
386	
387	\begin{table}[t]
388	\centering\small
389	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\,GB VRAM). VRAM reports peak allocated memory (excluding optimizer states).}
390	\label{tab:cost}
391	\resizebox{\columnwidth}{!}{%
392	\begin{tabular}{lcccc}
393	\toprule
394	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
395	\midrule
396	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
397	LoRA-only & 4.2M & 5.7 & 42\,GB & baseline \\
398	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
399	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
400	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
401	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
402	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
403	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
404	\midrule
405	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
406	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
407	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
408	\bottomrule
409	\end{tabular}}
410	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "8e2a9c7c-5f43-4389-9851-d153e46b5655",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\n\\begin{table}[t]\n\\centering\\small\n\\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\\,GB VRAM). VRAM reports peak allocated memory (excluding optimizer states).}\n\\label{tab:cost}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Params} & \\textbf{Time (h)} & \\textbf{VRAM} & \\textbf{Overhead} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Qwen-2.5-7B-Instruct}} \\\\\nLoRA-only & 4.2M & 5.7 & 42\\,GB & baseline \\\\\nThreadGate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\n\\;+\\,PCGrad & 4.3M & 8.0 & 43\\,GB & $+$33\\% \\\\\nUniform Gate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\nSS (s42) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\nSS (s123) & 4.3M & 10.8 & 43\\,GB & $+$80\\% \\\\\nSS (s456) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Llama-3.1-8B-Instruct}} \\\\\nLoRA-only & 4.2M & 7.0 & 45\\,GB & baseline \\\\\nThreadGate & 4.3M & 7.3 & 46\\,GB & $+$65K \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}",
      "numLines": 25,
      "startLine": 386,
      "totalLines": 851
    }
  }
}
```

</details>

---


### Tool call

_source line 109_

<details open><summary>🔧 Tool call — Grep · `toolu_01Jt3f8usEKf5ANfGneTBDZQ`</summary>

```json
{
  "pattern": "1\\.2.{0,3}\\\\times|gap.*1\\.2|1\\.2.*gap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "9e910e56-a8cc-408c-832f-f7a7e5a6f504",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSkwaTUiWi6Zvx4gkcB6DS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10389,
      "cache_read_input_tokens": 34041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10389
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

_source line 110 · 2026-05-25T20:44:59.792Z_

<details><summary>↩ Tool result · `toolu_01Jt3f8usEKf5ANfGneTBDZQ`</summary>

```text
paper/sections/analysis.tex:28:We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed); exposure bias thus disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
paper/sections/analysis.tex:41:[Omitted long matching line]
paper/sections/experiments.tex:34:  \caption{Scheduled sampling compresses the TF-AR gap from 7.9$\times$ to ${\sim}$1.2$\times$, the only variant approaching parity across five training conditions.}
paper/sections/experiments.tex:38:[Omitted long matching line]
paper/sections/conclusion.tex:3:[Omitted long matching line]
paper/sections/appendix.tex:207:[Omitted long matching line]
paper/sections/appendix.tex:211:\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
paper/sections/appendix.tex:491:[Omitted long matching line]
paper/sections/appendix.tex:495:[Omitted long matching line]
paper/sections/appendix.tex:500:\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.2$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
paper/sections/appendix.tex:633:[Omitted long matching line]
paper/sections/appendix.tex:689:[Omitted long matching line]
paper/sections/appendix.tex:810:[Omitted long matching line]
paper/sections/appendix.tex:829:TF/AR gap & 1.2$\times$ & 2.9$\times$ \\
paper/sections/introduction.tex:12:  \caption{Exposure bias collapses auxiliary attention losses. \textbf{(a)}~Goal attention decays 85--90\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \textbf{(b)}~Under TF evaluation all variants reach GAR$\approx$0.50, but AR generation collapses GAR by 8--17$\times$ (log scale). \textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\times$ to 1.2$\times$ (Qwen) and ${\sim}$27$\times$ to 2.9$\times$ (Llama).}
paper/sections/introduction.tex:21:    \item \textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\sim}$1.2$\times$ on Qwen and ${\sim}$2.9$\times$ on Llama with no perplexity degradation, robust across three seeds.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "6f7d07c0-cddf-4039-8554-5e238ebe5cae",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/sections/analysis.tex:28:We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed); exposure bias thus disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\\times$) and Qwen (1.28$\\times$) vs.\\ the order-of-magnitude GAR-ours collapse.\npaper/sections/analysis.tex:41:[Omitted long matching line]\npaper/sections/experiments.tex:34:  \\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$, the only variant approaching parity across five training conditions.}\npaper/sections/experiments.tex:38:[Omitted long matching line]\npaper/sections/conclusion.tex:3:[Omitted long matching line]\npaper/sections/appendix.tex:207:[Omitted long matching line]\npaper/sections/appendix.tex:211:\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\npaper/sections/appendix.tex:491:[Omitted long matching line]\npaper/sections/appendix.tex:495:[Omitted long matching line]\npaper/sections/appendix.tex:500:\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}\npaper/sections/appendix.tex:633:[Omitted long matching line]\npaper/sections/appendix.tex:689:[Omitted long matching line]\npaper/sections/appendix.tex:810:[Omitted long matching line]\npaper/sections/appendix.tex:829:TF/AR gap & 1.2$\\times$ & 2.9$\\times$ \\\\\npaper/sections/introduction.tex:12:  \\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.2$\\times$ (Qwen) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}\npaper/sections/introduction.tex:21:    \\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.2$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.",
    "numLines": 16
  }
}
```

</details>

---


### Tool call

_source line 111_

<details open><summary>🔧 Tool call — Grep · `toolu_017qaxDBXXR5V1gU1JW95QvA`</summary>

```json
{
  "pattern": "1\\.2.{0,3}\\\\times|gap.*1\\.2|1\\.2.*gap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "9989c2f5-8601-4343-9517-7e99875b849c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSkwaTUiWi6Zvx4gkcB6DS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10389,
      "cache_read_input_tokens": 34041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10389
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

_source line 112 · 2026-05-25T20:45:00.706Z_

<details><summary>↩ Tool result · `toolu_017qaxDBXXR5V1gU1JW95QvA`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "cc5a38c5-0350-4b5f-8a57-d72f22b504b6",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---


### Tool call

_source line 113_

<details open><summary>🔧 Tool call — Grep · `toolu_01LmYaFGW1bjLFCw9VkLyWR3`</summary>

```json
{
  "pattern": "1\\.2.{0,3}\\\\times|gap.*1\\.2|1\\.2.*gap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "19a2f637-599e-4b6e-bc6f-56e77755ce90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSkwaTUiWi6Zvx4gkcB6DS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10389,
      "cache_read_input_tokens": 34041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10389
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

_source line 114 · 2026-05-25T20:45:01.581Z_

<details><summary>↩ Tool result · `toolu_01LmYaFGW1bjLFCw9VkLyWR3`</summary>

```text
3:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "ddc735fb-eb79-42c8-ba3f-778e413f1eab",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "3:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---


### Tool call

_source line 115_

<details open><summary>🔧 Tool call — Read · `toolu_01Difz2rUjmsdUr7LQAnTUmW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
  "offset": 1,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "efadad79-19b8-4f04-b4b4-dfe3148dbb1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U7mQQbwsDceHxaJCBVrshG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2267,
      "cache_read_input_tokens": 44430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2267
      },
      "output_tokens": 65,
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

_source line 116 · 2026-05-25T20:45:04.884Z_

<details><summary>↩ Tool result · `toolu_01Difz2rUjmsdUr7LQAnTUmW`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\,=\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\beta$-steering recovers GAR above the TF baseline, consistent with attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\sim}$1.2$\times$ (Qwen) and ${\sim}$2.9$\times$ (Llama), generalizing across architectures and seeds; to our knowledge, the first such transfer to auxiliary attention objectives in multi-turn transformers.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "325fa8df-eeb7-42c9-bd47-baba254f5fc3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, consistent with attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.2$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds; to our knowledge, the first such transfer to auxiliary attention objectives in multi-turn transformers.\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---


### Tool call

_source line 117_

<details open><summary>🔧 Tool call — Read · `toolu_01MkU1pL3131FixC5C7NWut4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
  "offset": 10,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "37cb196a-2158-493a-881d-b106d3a03f56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U7mQQbwsDceHxaJCBVrshG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2267,
      "cache_read_input_tokens": 44430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2267
      },
      "output_tokens": 65,
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

_source line 118 · 2026-05-25T20:45:05.359Z_

<details><summary>↩ Tool result · `toolu_01MkU1pL3131FixC5C7NWut4`</summary>

```text
10	  \centering
11	  \includegraphics[width=\textwidth]{fig1_headline.pdf}
12	  \caption{Exposure bias collapses auxiliary attention losses. \textbf{(a)}~Goal attention decays 85--90\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \textbf{(b)}~Under TF evaluation all variants reach GAR$\approx$0.50, but AR generation collapses GAR by 8--17$\times$ (log scale). \textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\times$ to 1.2$\times$ (Qwen) and ${\sim}$27$\times$ to 2.9$\times$ (Llama).}
13	  \label{fig:headline}
14	\end{figure*}
15	
16	Our contributions are:
17	\begin{enumerate}\raggedright
18	    \item \textbf{Exposure bias characterization.} To our knowledge, the first empirical demonstration that exposure bias collapses auxiliary attention objectives in multi-turn transformers, with an order-of-magnitude TF--AR gap reproduced across two architectures (Qwen-2.5-7B, Llama-3.1-8B) and model scales (1.5B--8B).
19	    \item \textbf{Causal exclusion testbed.} A five-way diagnostic design, informed by seven loss-formulation iterations, that isolates the failure mechanism via causal exclusion, including a PCGrad \emph{modus tollens} argument ruling out gradient direction conflict ($p$\,=\,0.002, effect reverses).
20	    \item \textbf{Attention misallocation diagnosis.} Inference-time $\beta$-steering recovers goal attention with modest perplexity cost, evidence that the collapse is an attention routing failure, not a representational one.
21	    \item \textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\sim}$1.2$\times$ on Qwen and ${\sim}$2.9$\times$ on Llama with no perplexity degradation, robust across three seeds.
22	\end{enumerate}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "0205a7f4-e6aa-4397-a721-a7fbb887cc69",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
      "content": "  \\centering\n  \\includegraphics[width=\\textwidth]{fig1_headline.pdf}\n  \\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.2$\\times$ (Qwen) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}\n  \\label{fig:headline}\n\\end{figure*}\n\nOur contributions are:\n\\begin{enumerate}\\raggedright\n    \\item \\textbf{Exposure bias characterization.} To our knowledge, the first empirical demonstration that exposure bias collapses auxiliary attention objectives in multi-turn transformers, with an order-of-magnitude TF--AR gap reproduced across two architectures (Qwen-2.5-7B, Llama-3.1-8B) and model scales (1.5B--8B).\n    \\item \\textbf{Causal exclusion testbed.} A five-way diagnostic design, informed by seven loss-formulation iterations, that isolates the failure mechanism via causal exclusion, including a PCGrad \\emph{modus tollens} argument ruling out gradient direction conflict ($p$\\,=\\,0.002, effect reverses).\n    \\item \\textbf{Attention misallocation diagnosis.} Inference-time $\\beta$-steering recovers goal attention with modest perplexity cost, evidence that the collapse is an attention routing failure, not a representational one.\n    \\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.2$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.\n\\end{enumerate}\n",
      "numLines": 14,
      "startLine": 10,
      "totalLines": 23
    }
  }
}
```

</details>

---


### Tool call

_source line 119_

<details open><summary>🔧 Tool call — Read · `toolu_01WH3K4WGxHLtytjcTNXcgoA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "offset": 32,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "b3ab7163-3f46-4695-9167-8b0ea8198f6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U7mQQbwsDceHxaJCBVrshG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2267,
      "cache_read_input_tokens": 44430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2267
      },
      "output_tokens": 65,
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

_source line 120 · 2026-05-25T20:45:06.302Z_

<details><summary>↩ Tool result · `toolu_01WH3K4WGxHLtytjcTNXcgoA`</summary>

```text
32	  \centering
33	  \includegraphics[width=\columnwidth]{fig_ss_gap_compression.pdf}
34	  \caption{Scheduled sampling compresses the TF-AR gap from 7.9$\times$ to ${\sim}$1.2$\times$, the only variant approaching parity across five training conditions.}
35	  \label{fig:ss-gap}
36	\end{figure}
37	
38	Scheduled sampling (SS; \citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\pm0.047$, compressing the gap from 7.9$\times$ to ${\sim}$1.2$\times$ (TF GAR $0.498\pm0.004$) with no PPL cost ($1.441\pm0.002$; Figure~\ref{fig:ss-gap}; per-seed details in Appendix~\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\beta$\,=\,5: $0.717\pm0.001$, std 0.047$\to$0.001; Figure~\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\ 3; \S\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
39	
40	
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "6bc96070-7e32-4379-b2ce-4827510a6bc8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
      "content": "  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_gap_compression.pdf}\n  \\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$, the only variant approaching parity across five training conditions.}\n  \\label{fig:ss-gap}\n\\end{figure}\n\nScheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n\n\n",
      "numLines": 10,
      "startLine": 32,
      "totalLines": 41
    }
  }
}
```

</details>

---


### Tool call

_source line 121_

<details open><summary>🔧 Tool call — Read · `toolu_013jgpyUNXnypJgAYCb2KEDW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 205,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "90d932fc-536c-4459-b0b3-5e40b7a0769f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U7mQQbwsDceHxaJCBVrshG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2267,
      "cache_read_input_tokens": 44430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2267
      },
      "output_tokens": 65,
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

_source line 122 · 2026-05-25T20:45:07.239Z_

<details><summary>↩ Tool result · `toolu_013jgpyUNXnypJgAYCb2KEDW`</summary>

```text
205	\end{figure}
206	
207	\paragraph{Cross-model summary.} Table~\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\approx$ 0.5, AR GAR $\ll$ 0.1, gap $\geq$ 7.9$\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\times$ by median for TG; mean-based range 11.2--17.2$\times$) compared to Qwen's (7.9--13.5$\times$) may reflect its deeper architecture (32 vs.\ 28 layers), which allows more layers for distributional drift to compound through.
208	
209	\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}
210	
211	\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
212	
213	\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger layer count (32 vs.\ 28 layers).
214	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "5610049d-0c8a-4da0-9c31-4e398a7e598e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\\end{figure}\n\n\\paragraph{Cross-model summary.} Table~\\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\\approx$ 0.5, AR GAR $\\ll$ 0.1, gap $\\geq$ 7.9$\\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\\times$ by median for TG; mean-based range 11.2--17.2$\\times$) compared to Qwen's (7.9--13.5$\\times$) may reflect its deeper architecture (32 vs.\\ 28 layers), which allows more layers for distributional drift to compound through.\n\n\\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}\n\n\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\n\n\\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\\% longer than Qwen due to Llama's larger layer count (32 vs.\\ 28 layers).\n",
      "numLines": 10,
      "startLine": 205,
      "totalLines": 851
    }
  }
}
```

</details>

---


### Tool call

_source line 123_

<details open><summary>🔧 Tool call — Read · `toolu_0171XbvcdQxHexwaWVnRhjBK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 686,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "53f2fee5-258e-4545-8fb0-b4ae67c1407a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U7mQQbwsDceHxaJCBVrshG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2267,
      "cache_read_input_tokens": 44430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2267
      },
      "output_tokens": 65,
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

_source line 124 · 2026-05-25T20:45:08.176Z_

<details><summary>↩ Tool result · `toolu_0171XbvcdQxHexwaWVnRhjBK`</summary>

```text
686	
687	Table~\ref{tab:gar_robustness} and Figure~\ref{fig:gar-robust-grouped} extend the GAR robustness analysis from \S\ref{sec:appendix-gar-robust} with turn-1 GAR and gap ratio metrics across all four token-position variants. We evaluate four ways to select the query token position for gradient attribution: (1)~\textit{Last} (our default): the final token of each assistant turn, which captures the model's ``summary'' attention pattern at the prediction boundary; (2)~\textit{All}: the mean over all assistant tokens, providing a position-averaged view; (3)~\textit{First}: the first assistant token, which reflects initial attention allocation; (4)~\textit{Goal-only}: attention to goal tokens as defined by \citet{dongre2026attention}, which restricts the target set to system-prompt tokens.
688	
689	\paragraph{Position-specific vs.\ broad improvement.} The key finding is a clear dichotomy between ThreadGate and Scheduled Sampling. ThreadGate improvements are restricted to last-token and goal-only positions (the two definitions sharing the query position targeted by the GAR loss): gap ratios drop to 1.21$\times$ and 1.07$\times$ respectively. All-token (5.04$\times$) and first-token (8.24$\times$) GAR remain near base levels, confirming that the learned routing is position-specific. Scheduled Sampling raises all four definitions above 0.36 with gap ratios $\leq$1.83$\times$, demonstrating that distributional robustification builds broad goal attention across token positions rather than overfitting to the position targeted by the loss.
690	
691	\paragraph{Turn-1 vs.\ mid-turn dynamics.} Turn-1 GAR is consistently higher than mid-turn GAR across all definitions and conditions, reflecting the first turn's proximity to the ground-truth prefix in training. The gap ratio quantifies how much of this initial attention survives into later turns. First-token GAR shows the largest gap ratios (Base: 13.3$\times$, TG: 8.2$\times$), indicating that the first-token position is most vulnerable to distributional drift---the initial token's attention pattern is highly dependent on the conditioning context, which diverges most from training under autoregressive generation.
692	
693	\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}
694	
695	\begin{figure}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "a52c2c3c-59d1-4142-8a69-3fe317697906",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\nTable~\\ref{tab:gar_robustness} and Figure~\\ref{fig:gar-robust-grouped} extend the GAR robustness analysis from \\S\\ref{sec:appendix-gar-robust} with turn-1 GAR and gap ratio metrics across all four token-position variants. We evaluate four ways to select the query token position for gradient attribution: (1)~\\textit{Last} (our default): the final token of each assistant turn, which captures the model's ``summary'' attention pattern at the prediction boundary; (2)~\\textit{All}: the mean over all assistant tokens, providing a position-averaged view; (3)~\\textit{First}: the first assistant token, which reflects initial attention allocation; (4)~\\textit{Goal-only}: attention to goal tokens as defined by \\citet{dongre2026attention}, which restricts the target set to system-prompt tokens.\n\n\\paragraph{Position-specific vs.\\ broad improvement.} The key finding is a clear dichotomy between ThreadGate and Scheduled Sampling. ThreadGate improvements are restricted to last-token and goal-only positions (the two definitions sharing the query position targeted by the GAR loss): gap ratios drop to 1.21$\\times$ and 1.07$\\times$ respectively. All-token (5.04$\\times$) and first-token (8.24$\\times$) GAR remain near base levels, confirming that the learned routing is position-specific. Scheduled Sampling raises all four definitions above 0.36 with gap ratios $\\leq$1.83$\\times$, demonstrating that distributional robustification builds broad goal attention across token positions rather than overfitting to the position targeted by the loss.\n\n\\paragraph{Turn-1 vs.\\ mid-turn dynamics.} Turn-1 GAR is consistently higher than mid-turn GAR across all definitions and conditions, reflecting the first turn's proximity to the ground-truth prefix in training. The gap ratio quantifies how much of this initial attention survives into later turns. First-token GAR shows the largest gap ratios (Base: 13.3$\\times$, TG: 8.2$\\times$), indicating that the first-token position is most vulnerable to distributional drift---the initial token's attention pattern is highly dependent on the conditioning context, which diverges most from training under autoregressive generation.\n\n\\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}\n\n\\begin{figure}[t]",
      "numLines": 10,
      "startLine": 686,
      "totalLines": 851
    }
  }
}
```

</details>

---


### Tool call

_source line 125_

<details open><summary>🔧 Tool call — Read · `toolu_01JM1pK5Rmc17zzKeuoJzeuK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 825,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "439230a8-53f0-467e-a00d-60ec53db7476",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U7mQQbwsDceHxaJCBVrshG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2267,
      "cache_read_input_tokens": 44430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2267
      },
      "output_tokens": 65,
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

_source line 126 · 2026-05-25T20:45:08.608Z_

<details><summary>↩ Tool result · `toolu_01JM1pK5Rmc17zzKeuoJzeuK`</summary>

```text
825	\midrule
826	SS epochs & 3 & 2 \\
827	TF GAR & 0.498 & 0.477 \\
828	AR GAR ($\beta$\,=\,0) & 0.401 & 0.166 \\
829	TF/AR gap & 1.2$\times$ & 2.9$\times$ \\
830	Baseline TG gap & 7.9$\times$ & 27$\times$ (median) \\
831	Gap compression & 6.6$\times$ & 9.3$\times$ \\
832	AR GAR ($\beta$\,=\,5) & 0.717 & 0.791 \\
833	TF PPL & 2.78 & 2.82 \\
834	AR PPL & 1.441 & 1.370 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "adfc7c0f-157c-48d3-b34b-aa1f286d6fe6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\\midrule\nSS epochs & 3 & 2 \\\\\nTF GAR & 0.498 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.2$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.6$\\times$ & 9.3$\\times$ \\\\\nAR GAR ($\\beta$\\,=\\,5) & 0.717 & 0.791 \\\\\nTF PPL & 2.78 & 2.82 \\\\\nAR PPL & 1.441 & 1.370 \\\\",
      "numLines": 10,
      "startLine": 825,
      "totalLines": 851
    }
  }
}
```

</details>

---


### Assistant

_source line 127_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture of all the places that need to be changed. Let me also check the registry for TG per-seed N=50 data. The filter I used before was for `exp_id` containing "tg" but the registry returned 0 results, which means the filter is looking for exact match. Let me search more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "848202db-a8ce-4d9a-9952-4c310c887c12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqgYpYCps4GFVmfLUfbznu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3581,
      "cache_read_input_tokens": 46697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3581
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

_source line 128_

Let me search the registry more broadly for TG per-seed data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "2f5fcf15-40bc-4cb7-bd56-bc545e28810f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqgYpYCps4GFVmfLUfbznu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3581,
      "cache_read_input_tokens": 46697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3581
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

_source line 129_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01FtAZgaKpvcGFTFmbkHDDa3`</summary>

```json
{
  "project": "turn_residual_gating",
  "limit": 0,
  "fields": [
    "exp_id",
    "status",
    "conclusion"
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
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "45c54744-ae23-407a-bc8f-d5d75e707aea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqgYpYCps4GFVmfLUfbznu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3581,
      "cache_read_input_tokens": 46697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3581
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

_source line 130 · 2026-05-25T20:45:15.168Z_

<details><summary>↩ Tool result · `toolu_01FtAZgaKpvcGFTFmbkHDDa3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"phase2_switching\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"phase2_tf_ar_switching\": {\"status\": \"QUEUED\"}, \"phase1a_multiseed_8runs\": {\"status\": \"PREPARING\"}, \"phase1b_llama_complement\": {\"status\": \"PREPARING\"}, \"p1_llama_ss_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p1_llama_ss_training\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mmlu_eval_all\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p2_llama_gradient_conflict\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p1_tf_ar_kl_divergence\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"qwen15b_phase1_diag\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_eval_ss_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_ss_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_ss_steering_eval\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"d048_eval_ss_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_ss_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_split_softmax_eval\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"d048_final_ar_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_queue_runner\": {\"status\": \"PREPARING\", \"conclusion\": \"failed\"}, \"d048_eval_ss_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_ss_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_ss_s42_resume\": {\"status\": \"PREPARING\"}, \"eval_llama_ar_n20\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_llama_lora_only_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_lora_only_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v6\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"phase2_tg_s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_v7_tg_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_v8b_ss_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"v7_tg_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"v8b_ss_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_tg_training\": {\"status\": \"PREPARING\", \"conclusion\": \"failed\"}, \"llama_ar_matched_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"instruction_retention_test\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_eval_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_tg_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"attention_steering_gen_n50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v8b_resume\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_phase1_gar_diag\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_v8b_ss\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"attention_steering_eval200_tf\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"trc_baseline_v7_tg\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"attention_steering_v7_tg_gen\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v8b_ss_fixed\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"phase2_tg_s42_v7\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v9_pcgrad\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_lora_only_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_ug_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v8_schedsampling\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"analysis_attention_heatmap\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"analysis_gradient_conflict\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_4way_eval_heldout\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_4way_eval\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"phase2_tg_s42_v5\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"phase2_tg_s42_v4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"phase2_tg_s42_v3b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"phase2_tg_s42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"phase1_gar_diag\": {\"status\": \"DONE\", \"conclusion\": \"success\"}}, \"count\": 60, \"total\": 60, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1612}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "d12e49c2-d7d1-4a65-bf93-2a08da38de00",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"phase1a_multiseed_qwen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"p1_ss_lora_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"phase2_switching\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"phase2_tf_ar_switching\\\": {\\\"status\\\": \\\"QUEUED\\\"}, \\\"phase1a_multiseed_8runs\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"phase1b_llama_complement\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"p1_llama_ss_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"p1_llama_ss_training\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mmlu_eval_all\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"p2_llama_gradient_conflict\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"p1_tf_ar_kl_divergence\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"qwen15b_phase1_diag\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_eval_ss_s456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_ss_s456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"p0_ss_steering_eval\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"d048_eval_ss_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_ss_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_split_softmax_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"d048_final_ar_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_queue_runner\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"d048_eval_ss_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_ss_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_ss_s42_resume\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval_llama_ar_n20\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_llama_lora_only_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_lora_only_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_tg_s42_v6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"phase2_tg_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_v7_tg_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_v8b_ss_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"v7_tg_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"v8b_ss_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_tg_training\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"llama_ar_matched_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"instruction_retention_test\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_eval_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_tg_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"attention_steering_gen_n50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_tg_s42_v8b_resume\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_phase1_gar_diag\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_v8b_ss\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"attention_steering_eval200_tf\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"trc_baseline_v7_tg\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"attention_steering_v7_tg_gen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_tg_s42_v8b_ss_fixed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"phase2_tg_s42_v7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_tg_s42_v9_pcgrad\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_lora_only_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_ug_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_tg_s42_v8_schedsampling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"analysis_attention_heatmap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"analysis_gradient_conflict\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_4way_eval_heldout\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_4way_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"phase2_tg_s42_v5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"phase2_tg_s42_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"phase2_tg_s42_v3b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_tg_s42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"phase2_tg_s42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"phase1_gar_diag\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 60, \\\"total\\\": 60, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1612}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"phase2_switching\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"phase2_tf_ar_switching\": {\"status\": \"QUEUED\"}, \"phase1a_multiseed_8runs\": {\"status\": \"PREPARING\"}, \"phase1b_llama_complement\": {\"status\": \"PREPARING\"}, \"p1_llama_ss_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p1_llama_ss_training\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mmlu_eval_all\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p2_llama_gradient_conflict\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p1_tf_ar_kl_divergence\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"qwen15b_phase1_diag\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_eval_ss_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_ss_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_ss_steering_eval\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"d048_eval_ss_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_ss_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_split_softmax_eval\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"d048_final_ar_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_queue_runner\": {\"status\": \"PREPARING\", \"conclusion\": \"failed\"}, \"d048_eval_ss_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_ss_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d048_ss_s42_resume\": {\"status\": \"PREPARING\"}, \"eval_llama_ar_n20\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_llama_lora_only_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_lora_only_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v6\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"phase2_tg_s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_v7_tg_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_v8b_ss_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"v7_tg_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"v8b_ss_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_tg_training\": {\"status\": \"PREPARING\", \"conclusion\": \"failed\"}, \"llama_ar_matched_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"instruction_retention_test\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_eval_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_tg_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"attention_steering_gen_n50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v8b_resume\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_phase1_gar_diag\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_v8b_ss\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"attention_steering_eval200_tf\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"trc_baseline_v7_tg\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"attention_steering_v7_tg_gen\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v8b_ss_fixed\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"phase2_tg_s42_v7\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v9_pcgrad\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_lora_only_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_ug_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v8_schedsampling\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"analysis_attention_heatmap\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"analysis_gradient_conflict\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_4way_eval_heldout\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_4way_eval\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"phase2_tg_s42_v5\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"phase2_tg_s42_v4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"phase2_tg_s42_v3b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"phase2_tg_s42_v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"phase2_tg_s42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"phase1_gar_diag\": {\"status\": \"DONE\", \"conclusion\": \"success\"}}, \"count\": 60, \"total\": 60, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1612}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 131_

<details><summary>Logged reasoning block</summary>

```text
Looking at the registry, I see experiments for TG:
- `phase2_tg_s42_v7`: this is TG seed 42
- `v7_tg_s123`: this is TG seed 123
- `eval_v7_tg_s123`: evaluation of TG s123

But I need to check if there's N=50 AR data for these TG per-seed experiments. Let me check `d048_final_ar_eval` for TG data and `eval_v7_tg_s123` for the other seed.

The task says:


I found N=50 results for seed 42 in `d048_final_ar_eval` with a GAR of 0.064, but the per-seed experiment `phase2_tg_s42_v7` only has N=5 data. Now I need to check whether `d048_final_ar_eval` contains N=50 results for seed 123 as well.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "e9b550df-ff84-4e75-986a-75a49add89c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApKZ8tEprwCb2B4qTzqGuL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 50278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2075
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

_source line 132_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Fq6ctSQwoWEyQ5sLMMWWDs`</summary>

```json
{
  "project": "turn_residual_gating",
  "filters": {
    "exp_id": "d048_final_ar_eval"
  },
  "fields": [
    "*"
  ],
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "4e12dea4-5d03-4ef3-9303-9ff9969d69f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApKZ8tEprwCb2B4qTzqGuL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 50278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2075
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

_source line 133_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Bnk8e7sodEaLNFpx4u2YuP`</summary>

```json
{
  "project": "turn_residual_gating",
  "filters": {
    "exp_id": "eval_v7_tg_s123"
  },
  "fields": [
    "*"
  ],
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "88a29467-011a-4745-a2f7-cb439b17758b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApKZ8tEprwCb2B4qTzqGuL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 50278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2075
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

_source line 134 · 2026-05-25T20:45:25.470Z_

<details><summary>↩ Tool result · `toolu_01Fq6ctSQwoWEyQ5sLMMWWDs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1612}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "8f66c6c4-874e-487e-983d-121226551578",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1612}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1612}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-25T20:45:25.641Z_

<details><summary>↩ Tool result · `toolu_01Bnk8e7sodEaLNFpx4u2YuP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1607}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "d8bd6622-6eb5-438d-b5a2-69013049543a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1607}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1607}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 136_

<details><summary>Logged reasoning block</summary>

```text
The registry filter seems to require exact match but it's not working. Let me try reading the registry without filters and look at it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "bb01b9bf-1bf0-4a09-bd28-6243d14f845e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXbN9jJC91GWjRPX4Cbkej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 52353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 781
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

_source line 137_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AMP4q6LEQWhSFCW8BvHg2P`</summary>

```json
{
  "project": "turn_residual_gating",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "metrics",
    "conclusion"
  ],
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "621581cc-9065-4088-8631-72c9ab3ac073",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXbN9jJC91GWjRPX4Cbkej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 52353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 781
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

_source line 138 · 2026-05-25T20:45:30.061Z_

<details><summary>↩ Tool result · `toolu_01AMP4q6LEQWhSFCW8BvHg2P`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"conclusion\": \"killed\"}, \"phase2_switching\": {\"conclusion\": \"killed\"}, \"p1_llama_ss_eval\": {\"conclusion\": \"success\", \"metrics\": {\"ss_tf_gar\": 0.477, \"ss_tf_ppl\": 2.82, \"ss_ar_b0_gar\": 0.1662, \"ss_ar_b0_ppl\": 1.37, \"ss_ar_b5_gar\": 0.7905, \"ss_ar_b5_ppl\": 1.81, \"base_ar_gar\": 0.0179, \"base_ar_ppl\": 1.22, \"tf_ar_gap\": 2.87}}, \"p1_llama_ss_training\": {\"conclusion\": \"success\"}}, \"count\": 5, \"total\": 53, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1662}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "cac1e23c-e298-4cae-9d48-834ca662e611",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"phase1a_multiseed_qwen\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"p1_ss_lora_only\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"phase2_switching\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"p1_llama_ss_eval\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ss_tf_gar\\\": 0.477, \\\"ss_tf_ppl\\\": 2.82, \\\"ss_ar_b0_gar\\\": 0.1662, \\\"ss_ar_b0_ppl\\\": 1.37, \\\"ss_ar_b5_gar\\\": 0.7905, \\\"ss_ar_b5_ppl\\\": 1.81, \\\"base_ar_gar\\\": 0.0179, \\\"base_ar_ppl\\\": 1.22, \\\"tf_ar_gap\\\": 2.87}}, \\\"p1_llama_ss_training\\\": {\\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 5, \\\"total\\\": 53, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1662}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"conclusion\": \"killed\"}, \"phase2_switching\": {\"conclusion\": \"killed\"}, \"p1_llama_ss_eval\": {\"conclusion\": \"success\", \"metrics\": {\"ss_tf_gar\": 0.477, \"ss_tf_ppl\": 2.82, \"ss_ar_b0_gar\": 0.1662, \"ss_ar_b0_ppl\": 1.37, \"ss_ar_b5_gar\": 0.7905, \"ss_ar_b5_ppl\": 1.81, \"base_ar_gar\": 0.0179, \"base_ar_ppl\": 1.22, \"tf_ar_gap\": 2.87}}, \"p1_llama_ss_training\": {\"conclusion\": \"success\"}}, \"count\": 5, \"total\": 53, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1662}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 139_

<details><summary>Logged reasoning block</summary>

```text
Good. So the registry does have a `metrics` field. The filters work but they return exact matches. I see the issue now - the `exp_id` field is the key, not a field in the data. Let me read the raw YAML instead.

Actually, looking at the results, I see the structure is `experiments: { exp_id: { metrics: ..., conclusion: ... } }`. So `exp_id` is the key name. The filter must be looking at field values inside each experiment entry. Let me try reading the full registry file directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "1a90c122-c7b4-4a46-95cb-236d493de3ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtSne3Beqt3xuywSw9r9EP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 501,
      "cache_read_input_tokens": 53134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 501
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

_source line 140_

<details open><summary>🔧 Tool call — Grep · `toolu_01R8fKjonz8GqDmFWygA1xsa`</summary>

```json
{
  "pattern": "d048_final_ar|eval_v7_tg_s123|tg.*s123.*ar|tg.*n50",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/dream_registry.yaml",
  "output_mode": "content",
  "-n": true,
  "context": 5,
  "head_limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "76554f9b-81d4-4db5-91b9-a93d6ad57d2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtSne3Beqt3xuywSw9r9EP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 501,
      "cache_read_input_tokens": 53134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 501
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

_source line 141 · 2026-05-25T20:45:38.317Z_

<details><summary>↩ Tool result · `toolu_01R8fKjonz8GqDmFWygA1xsa`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "a021207d-da27-4a61-b43c-dad58262a020",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---


### Tool call

_source line 142_

<details open><summary>🔧 Tool call — Glob · `toolu_01ABo4eie6cPe2ktdDmGYZtC`</summary>

```json
{
  "pattern": "**/dream_registry*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "607f1aa6-952a-4be8-913d-86ed1ce6e389",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRz6FPJtY1VDtBL1uUZpJD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 357,
      "cache_read_input_tokens": 53635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 357
      },
      "output_tokens": 43,
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

_source line 143 · 2026-05-25T20:45:45.203Z_

<details><summary>↩ Tool result · `toolu_01ABo4eie6cPe2ktdDmGYZtC`</summary>

```text
dream_registry.lock
dream_registry.yaml.bak
dream_registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "bc537458-0a23-4cf4-a11b-ab30a424be9b",
  "tool_use_result": {
    "filenames": [
      "dream_registry.lock",
      "dream_registry.yaml.bak",
      "dream_registry.yaml"
    ],
    "durationMs": 39,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 144_

<details open><summary>🔧 Tool call — Grep · `toolu_01TUQq8hcm9Z65FHJ3sFuosL`</summary>

```json
{
  "pattern": "d048_final_ar|eval_v7_tg_s123",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/dream_registry.yaml",
  "output_mode": "content",
  "-n": true,
  "context": 20,
  "head_limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "a75fde81-631b-4127-91c3-42fd0f77d0a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WjtZpBNmjDg9cqyBNUaZ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 134,
      "cache_read_input_tokens": 53992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 134
      },
      "output_tokens": 71,
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

_source line 145 · 2026-05-25T20:45:50.625Z_

<details><summary>↩ Tool result · `toolu_01TUQq8hcm9Z65FHJ3sFuosL`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "803a0ece-d4b3-4dc5-bc0c-8e60ddaa5f97",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---


### Tool call

_source line 146_

<details open><summary>🔧 Tool call — Bash · `toolu_01AbofJ93cJtqfGvfpryrG55`</summary>

```json
{
  "command": "head -50 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/dream_registry.yaml",
  "description": "Check registry file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "8fc522f0-a286-42f4-b2b4-d9b8716329b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LzdxMUvdHv3mrQwQw1KpW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 207,
      "cache_read_input_tokens": 54126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 207
      },
      "output_tokens": 56,
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

_source line 147 · 2026-05-25T20:45:56.378Z_

<details><summary>↩ Tool result · `toolu_01AbofJ93cJtqfGvfpryrG55`</summary>

```text
dreams:
  dream_20260519T143220:
    card_message_id: om_x100b6ff3099c98b0b2f684134f7af4e
    chat_id: oc_640e53b6afbbd5e34eb7273cd5a707a0
    context_hash: b2394bf844a8292b084341ce00a4696d3109f9097c3655ddedb907f36b4b7856
    dream_id: dream_20260519T143220
    error: 'killed by director: outdated focus (pre-framing-fix), slot needed for
      re-dream'
    focus: 'Route B negative result paper: core novelty is teacher-forcing distribution
      shift destroying auxiliary attention loss generalization (30x GAR gap), NOT
      just "gating failed". Key risks: single-model weakness (W1, mitigated by Llama-3
      plan), "didn''t try hard enough" (W2), GAR as sole proxy metric (W3). Gradient
      conflict data now available (cos_sim -0.089→-0.042, mag_ratio 7.5→14.7x). Eval
      data overlaps training set — held-out eval planned but not yet done.'
    pid: null
    project: turn_residual_gating
    review_mode: full
    review_visible: true
    stages_completed:
    - imagine
    started_at: '2026-05-19T14:32:20+00:00'
    status: failed
    updated_at: '2026-05-19T14:45:10+00:00'
    venue: ''
    what_if: []
    writing_visible: true
  dream_20260519T145320:
    card_message_id: om_x100b6ff3d8f81d04b295df32981809c
    chat_id: oc_640e53b6afbbd5e34eb7273cd5a707a0
    context_hash: 630be4b057d5da6bd00addfe5079a518cb2a5802ad67652f889409fc0bb7aca6
    dream_id: dream_20260519T145320
    error: null
    focus: 'Route B negative result paper post-framing-fix. Core novelty: first quantitative
      measurement of exposure bias impact on auxiliary attention losses (30x GAR gap
      training vs inference). Claims narrowed to lightweight residual gating + GAR
      auxiliary loss scope (not all attention steering). Held-out eval DONE: three-way
      convergence confirmed (TG≈UG≈LoRA-only, GAR diff &lt;0.6pp, PPL identical).
      Bootstrap CI: all 95% CIs include 0, statistically confirms zero benefit. Gradient
      conflict quantified (cos_sim negative, mag_ratio 7.5→14.7x). Eq.3 formula corrected:
      code uses x+g·f(x) (ReZero-style), mechanism narrative updated. Key remaining:
      Llama-3 cross-model validation (planned), exposure-bias mitigation experiment
      (in progress).'
    pid: 1627250
    project: turn_residual_gating
    review_mode: full
    review_quality:
      worst: simulated
    review_visible: true
    stages_completed:
    - imagine
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "d360e759-f4ff-4bdf-acf9-efe572e4fd77",
  "tool_use_result": {
    "stdout": "dreams:\n  dream_20260519T143220:\n    card_message_id: om_x100b6ff3099c98b0b2f684134f7af4e\n    chat_id: oc_640e53b6afbbd5e34eb7273cd5a707a0\n    context_hash: b2394bf844a8292b084341ce00a4696d3109f9097c3655ddedb907f36b4b7856\n    dream_id: dream_20260519T143220\n    error: 'killed by director: outdated focus (pre-framing-fix), slot needed for\n      re-dream'\n    focus: 'Route B negative result paper: core novelty is teacher-forcing distribution\n      shift destroying auxiliary attention loss generalization (30x GAR gap), NOT\n      just \"gating failed\". Key risks: single-model weakness (W1, mitigated by Llama-3\n      plan), \"didn''t try hard enough\" (W2), GAR as sole proxy metric (W3). Gradient\n      conflict data now available (cos_sim -0.089→-0.042, mag_ratio 7.5→14.7x). Eval\n      data overlaps training set — held-out eval planned but not yet done.'\n    pid: null\n    project: turn_residual_gating\n    review_mode: full\n    review_visible: true\n    stages_completed:\n    - imagine\n    started_at: '2026-05-19T14:32:20+00:00'\n    status: failed\n    updated_at: '2026-05-19T14:45:10+00:00'\n    venue: ''\n    what_if: []\n    writing_visible: true\n  dream_20260519T145320:\n    card_message_id: om_x100b6ff3d8f81d04b295df32981809c\n    chat_id: oc_640e53b6afbbd5e34eb7273cd5a707a0\n    context_hash: 630be4b057d5da6bd00addfe5079a518cb2a5802ad67652f889409fc0bb7aca6\n    dream_id: dream_20260519T145320\n    error: null\n    focus: 'Route B negative result paper post-framing-fix. Core novelty: first quantitative\n      measurement of exposure bias impact on auxiliary attention losses (30x GAR gap\n      training vs inference). Claims narrowed to lightweight residual gating + GAR\n      auxiliary loss scope (not all attention steering). Held-out eval DONE: three-way\n      convergence confirmed (TG≈UG≈LoRA-only, GAR diff &lt;0.6pp, PPL identical).\n      Bootstrap CI: all 95% CIs include 0, statistically confirms zero benefit. Gradient\n      conflict quantified (cos_sim negative, mag_ratio 7.5→14.7x). Eq.3 formula corrected:\n      code uses x+g·f(x) (ReZero-style), mechanism narrative updated. Key remaining:\n      Llama-3 cross-model validation (planned), exposure-bias mitigation experiment\n      (in progress).'\n    pid: 1627250\n    project: turn_residual_gating\n    review_mode: full\n    review_quality:\n      worst: simulated\n    review_visible: true\n    stages_completed:\n    - imagine",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 148_

<details><summary>Logged reasoning block</summary>

```text
The `dream_registry.yaml` is for the "dream" system (paper writing iterations), not experimental results. The experimental data is likely in a different registry file. Let me look for where the experiment metrics are stored. The task already gives me the data I need from the registry. Let me focus on the key question: is there N=50 TG AR data for seed 123?

From the task description:
- `d048_final_ar_eval` beta0: tg_gar = 0.064 (s42, N=50 gen-mode)
- perseed TG table AR: 0.016 (s42, N=5 T=10), 0.017 (s123, N=5 T=10)


- The appendix text mentions AR GAR values of 0.064 vs 0.055 for two seeds with gap ratios of 7.9× and 9.1×, but this doesn't match the table values of 0.016 and 0.017, so there's a discrepancy I need to resolve.

Now I see the issue: the paragraph is referencing data from the N=50 gen-mode protocol while the table uses the N=5, T=10 protocol, which explains why the AR GAR values differ. I can confirm both seeds have N=50 data available—seed 42 shows 0.064 and seed 123 shows 0.055 from the evaluation results.

Let me verify the math: 0.504 divided by 0.064 gives 7.875, which rounds to 7.9×, and 0.505 divided by 0.055 gives 9.18, which matches the 9.1× mentioned. The numbers check out, so I now have what I need to fix the per-seed table by updating it to use the N=50 values instead of the N=5, T=10 protocol values.

For the crossmodel detail table, I need to update the SS row with the corrected TF and AR GAR values, and adjust the gap ratio from 1.2× to 1.4×. I should also add a note to the caption clarifying that all rows use seed 42.

For the per-seed TG table, I'll replace the AR section with the N=50 data showing the two seed values and their corresponding gap ratios, with a mean of 8.5±0.9.

The INFO-1 discrepancy is already resolved by the W1 fix. Now I'm checking the cost table where LoRA-only shows 5.7 hours, which appears correct, and ThreadGate shows 6.0 hours. Looking at the actual table values, LoRA-only shows 5.7h which matches what's needed, but Uniform Gate is currently listed as 6.0h when it should be 6.1h based on the task description. Looking at the task more carefully, it seems the issue is about precision in the reported numbers. The LoRA-only value of 5.7h in the table is already correct, but for Uniform Gate, I need to change 6.0h to 6.1h to match the actual measured value of 6.11h. Let me verify this is the only change needed for this particular issue. Looking at line 727, that 6.0 hours reference is for ThreadGate on 7B compared to 1.5B, not related to Uniform Gate or LoRA-only. So the straightforward fix is just updating Uniform Gate from 6.0 to 6.1 in the cost table, since LoRA-only at 5.7 already rounds correctly from 5.72. Now I need to figure out what changes are needed for the SS gap.

The text currently says "1.2×" for the SS gap everywhere, but the actual numbers depend on which table I'm referencing. The crossmodel table shows 0.502/0.347 = 1.45× (rounds to 1.4×), while the perseed table with 3-seed means gives 0.517/0.401 = 1.29× (rounds to 1.3×). I need to check which value the figure caption and main text should actually reference based on what data they're discussing. Ah, I see the discrepancy now. The 0.498±0.004 figure comes from a different evaluation protocol—specifically IID evaluation rather than the held-out protocol used in the perseed table. The appendix clarifies that under IID evaluation, TF GAR-ours is more stable at 0.499±0.003, which matches what's cited in the main text. The 3-seed mean gives TF ≈ 0.517 and AR ≈ 0.401, which produces a gap of about 1.29× — matching the 1.3× figure I should report. Let me verify this is the right value to use in experiments.tex rather than the IID protocol result. the cross-model table should reference the s42 data with a 1.4× gap, while the main text in experiments.tex needs to use the 3-seed mean of 1.3× for consistency with the per-seed discussion. I need to update both the main text and figure caption from 1.2× to 1.3× to reflect the more robust 3-seed average.

Now I'm going through the other files to make the same correction: introduction.tex needs updates in the figure caption and contributions section, conclusion.tex needs the gap value changed, analysis.tex has a reference to update, and appendix.tex has a mention in the EB scaling section that I should check whether it needs updating based on what data that figure uses. The figure caption shows 1.2× for SS, but if we're updating the crossmodel table to use s42 data showing 1.4×, the figure's data should match that protocol. The real issue is whether the figure needs to be regenerated to reflect the new values.

For now, I'll focus on what's in scope: fixing the text and tables. The key is distinguishing between the s42 crossmodel result (1.4×) and the 3-seed mean (1.3×) when discussing SS effects in the main text, and making sure the appendix sections that reference the crossmodel table or s42 data use the correct 1.4× figure.

The tricky part is the figure caption and analysis—I need to figure out what data the figure actually uses. Looking at the old crossmodel table values and the 3-seed mean, it seems the figure was likely generated with the 3-seed mean data (which gave ~1.2× before), but now I'm checking whether it should reference 1.3× or 1.4× depending on which dataset the figure actually displays. the EB scaling appendix paragraph presumably discusses the same figure data, so I need to decide whether to update those references too. I think the cleanest approach is to use 1.3× for all main text references since that's the 3-seed mean and more robust, keep the crossmodel table at 1.4× with consistent s42 data, and handle the appendix EB scaling section based on what it's actually discussing—if it's referencing the figure itself, I should match what the figure visually shows. I need to settle on consistent values across the document. The 3-seed mean gives ~1.3× for the SS gap, so I'll update all text references to use that figure while keeping the cross-model table at 1.4× since it's based on the s42 seed. The figure caption should also shift to ~1.3× to align with this interpretation, even though I'm not diving into the exact generation script.

Now looking at the Qwen-SS table, I'm noticing an inconsistency. If I'm claiming 1.3× for the SS gap in the main text using the held-out TF value of 0.517, but this table uses TF=0.498 with AR=0.401, that gives only 1.24 ≈ 1.2×. These numbers don't align, and I need to figure out whether the table is using IID data or something else to explain the discrepancy. I'm seeing the discrepancy now—it depends on whether I use the IID TF value (0.498) or the held-out TF value (0.517) when calculating the gap against the 3-seed mean AR (0.401). The task is clear though: I should use 1.3× for the 3-seed mean gap in the main text, update the crossmodel table to s42 data, and keep the perseed table as is. I'm tracking the specific updates needed across two tables. For the crossmodel detail table, I need to change the SS row to use the new values: GAR becomes 0.502, AR becomes 0.347, and the gap ratio updates to 1.4×. I also need to revise the caption to clarify that all Qwen rows use seed 42 and reference the per-seed analysis table. For the per-seed TG table, I'm pulling updated AR section data using the N=50 gen-mode evaluation results, with seed 42 showing GAR-ours of 0.064 and seed 123 at 0.055. I'm checking whether I have the N=50 protocol data for PPL and GAR-Dongre across both seeds. The crossmodel table shows AR PPL = 1.432 for TG under N=50, but I'm missing the per-seed breakdown for s42 and s123. Since the task gives me two options—update the table if I have the data or add a footnote if I don't—I need to clarify what information is actually available before deciding which approach to take. I see the core issue now—the per-seed TG table displays N=5, T=10 results while the appendix text and main results table both reference N=50 data. Since I don't have the complete N=50 per-seed dataset across all metrics, I'll add a footnote to the table caption clarifying this protocol difference. I'm realizing there are two separate AR evaluations for TG with different protocols: one at N=5 with extended generation showing GAR around 0.016-0.017 and gap ratios of 31-32×, and another at N=50 in gen-mode with GAR of 0.064-0.055 and gap ratios of 7.9-9.1×. The table reports the N=5 results while the paragraph discusses N=50, which creates the appearance of inconsistency that the reviewer flagged. Adding a footnote to clarify this protocol difference should resolve the confusion. I'm considering whether to show both protocols in the derived gap ratio section, or replace the N=5 values entirely with N=50 results and a footnote. The clearest approach is to update the table caption to specify that AR evaluation uses the extended-generation protocol (N=5, T=10 turns), then add a note clarifying that under the gen-mode protocol (N=50) from the main table, the AR GAR values are 0.064 and 0.055 with corresponding gap ratios of 7.9× and 9.1×. Now I need to adjust the appendix paragraph at line 635 to align with this, since those gap ratio values are based on the N=50 data.

So my complete plan is to update the crossmodel detail table with corrected values for the SS row and add a note about s42, then update the perseed TG table accordingly.

I need to fix the cost table's Uniform Gate timing value, and then systematically update all text references across the main paper files where the SS gap should reflect the 3-seed mean of 1.3× instead of 1.2×—that includes multiple instances in experiments, introduction, conclusion, and analysis sections, plus the appendix references discussing cross-variant gaps.

Now I'm working through the appendix more carefully, particularly around line 810 where there's a cross-model architecture comparison. The table shows specific TF and AR values that produce a 1.2× ratio, but I need to determine whether this should be updated to 1.3× to maintain consistency with the 3-seed held-out results used elsewhere in the narrative. I'm noticing an inconsistency between the table values and the narrative text. The llama-vs-qwen comparison table shows a 1.2× gap (0.498/0.401), but if I update the Qwen value to 0.517 based on the 3-seed held-out mean, that would give 1.29× which rounds to 1.3×. However, the task seems to be asking me to update narrative references to the gap ratio rather than modify the underlying table data itself. I should focus on updating the prose mentions of "~1.2×" to "~1.3×" in the main text while keeping the llama comparison table's internal arithmetic consistent as-is. the source numbers would require changes beyond what's being asked. So I'm keeping the llama-qwen comparison table as-is since it's internally consistent. The main updates I need to make are: updating the crossmodel table to 1.4×, adjusting the primary narrative to 1.3× based on the 3-seed mean, and fixing figure captions and appendix sections to align with 1.3×. For the EB scaling section, I'll use 1.3× to match the main narrative rather than the visual 1.2-1.3× range shown in the figure.

Now I'm checking the per-seed breakdown at line 633 to verify the individual gap ratios. Seed 42 already shows 1.4×, which is correct. For seed 123, the calculation checks out to 1.3×, and seed 456 appears to be around 1.14×, so I need to verify that last one. I'm checking whether the TF GAR value in experiments.tex needs updating too. The task only mentions changing the gap ratio, but there's an inconsistency: if I keep TF at 0.498 (IID) while using the 1.3× gap based on held-out TF values, the math doesn't align. I need to carefully re-examine what the experiments.tex line is actually reporting to resolve this tension. I'm realizing the issue: the text currently shows the IID evaluation result (0.498±0.004), but the main results actually use held-out evaluation. If I switch to the held-out TF value (0.517±0.032), the uncertainty balloons from 0.004 to 0.032, which looks much worse even though it's the correct evaluation setup. I need to figure out which TF values the main results table is actually using before deciding what to report here. I'm noticing the held-out TF values show much higher variance (0.517±0.032) compared to IID (0.499±0.003), with seed 123 driving most of that variance on the larger sample. The experiments.tex line 38 appears to be using IID protocol values rather than held-out, so I need to decide whether to update those numbers or keep them as-is for consistency with the main results table.

The core issue is that if I change the gap ratio from 1.2× to 1.3× based on held-out means, readers will notice the arithmetic doesn't match: 0.498/0.401 gives 1.24×, not 1.3×. I'm realizing the 7.9× baseline gap comes from ThreadGate s42 with TF at 0.504, so I need to trace through exactly which values are being compared in that compression claim. I'm working through whether to adjust the TF value to match the 1.3× gap the task requires, or keep the current 0.498 and report it as 1.2×. The task explicitly asks for "~1.3× (3-seed mean)" in the text, so I should use the held-out 3-seed mean TF of 0.517 to make the numbers consistent, even though it has a higher standard deviation. So the core issue is that the gap calculation depends on which TF value I use. If I report the held-out TF (0.517±0.032) to match the 1.3× gap, the large standard deviation looks awkward in the main text. But if I stick with the IID TF (0.498±0.004), the gap becomes 1.2× instead. The task description seems to expect the held-out protocol since that's what the per-seed table shows, but that forces me to choose between reporting a less clean number or potentially being inconsistent about which evaluation protocol I'm using. I'm realizing I should just follow the explicit instructions rather than overthinking this. The cleanest approach is to update the gap to 1.3× and remove the inline TF GAR number from the experiments.tex line since it's based on IID data and doesn't align with the held-out protocol results that give us the 1.3× figure. I'm refining the sentence structure to make the gap comparison clearer—simplifying it to just state the compressed gap ratio without the original 7.9× reference, and moving the per-seed details to the appendix note to keep the main result more readable. be consistent with the held-out protocol from the per-seed table. The standard deviation is high, but that's what the data actually shows and it's addressed in the appendix. I'm going with this change since it's accurate and aligns with the 1.3× gap. Though now I'm realizing the figure caption mentions ~1.2×, and I need to verify whether the visual itself shows that value before updating the caption to 1.3×.

Looking at the figure more carefully, it probably displays a bar chart with gap ratios across the five conditions, so the scheduled sampling bar would reflect whatever was plotted. Since my true value is 1.29× which rounds to 1.3×, I can update the caption to ~1.3× and trust it's approximately correct if the bar falls between 1.2 and 1.4.

Now I'm ready to execute the changes. For the per-seed table, I'll add a footnote to the caption explaining the protocol and referencing the N=50 values.

I also need to verify whether experiments.tex should have TF updated from 0.498 to 0.517. The gap computation in the caption uses TF/AR, so if the gap is 1.3× and AR is 0.401, then TF should be around 0.521. My actual 3-seed held-out TF mean is 0.517, which gives 0.517/0.401 ≈ 1.29× ≈ 1.3×, so I'll update it to "$0.517\pm0.032$" for consistency.

But I'm noticing that TF GAR for SS-type models is typically around 0.50 across the paper (0.498-0.504), so reporting 0.517 might look inconsistent—though this is the held-out evaluation on N=200 where seed 123 is an outlier at 0.554, while the IID evaluation gives 0.499±0.003. I think the best approach is to keep the gap at 1.3× and note it's the 3-seed mean, then use clearer phrasing that shows the per-seed variation without creating arithmetic confusion—something like listing the individual seed gaps alongside a reference to the detailed table. I'm verifying the consistency of this change—the ratio 0.517 divided by 0.401 gives approximately 1.29, which rounds nicely to 1.3×. Now I'll apply all the updates to the text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "714d7983-6c7b-4ab0-8ea8-cfb7e2b29292",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqbr8pfav41b1eHu6NEsVU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 54333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 951
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

_source line 149_

Now I have all the data I need. The appendix paragraph at line 635 confirms N=50 TG AR data exists for both seeds (0.064 for s42, 0.055 for s123). Let me execute all fixes now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "9e002196-485b-4bd0-8894-d8c1750dd366",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqbr8pfav41b1eHu6NEsVU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 54333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 951
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

_source line 150_

<details open><summary>🔧 Tool call — Edit · `toolu_01C1fg8UmBKQ2ULSvm9MLTkw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
  "old_string": "  & \\textbf{SS} & 0.498 & \\textbf{0.401} & 2.78 & 1.441 & \\textbf{1.2$\\times$} \\\\",
  "new_string": "  & \\textbf{SS} & 0.502 & \\textbf{0.347} & 2.78 & 1.441 & \\textbf{1.4$\\times$} \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "eee05970-bdce-488b-8037-321ce140383d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqbr8pfav41b1eHu6NEsVU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 54333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 951
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

_source line 151 · 2026-05-25T20:50:38.246Z_

<details><summary>↩ Tool result · `toolu_01C1fg8UmBKQ2ULSvm9MLTkw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "92be6ad0-185c-4071-916b-a562a60bf50b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
    "oldString": "  & \\textbf{SS} & 0.498 & \\textbf{0.401} & 2.78 & 1.441 & \\textbf{1.2$\\times$} \\\\",
    "newString": "  & \\textbf{SS} & 0.502 & \\textbf{0.347} & 2.78 & 1.441 & \\textbf{1.4$\\times$} \\\\",
    "originalFile": "% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct\n% Conditions shared by both models: Base, ThreadGate, LoRA-only\n% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0\n% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4\n% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)\n\\begin{table*}[t]\n\\centering\n\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}\n\\label{tab:crossmodel-detail}\n\\small\n\\begin{tabular}{@{}ll ccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Condition} & \\textbf{TF GAR}$\\uparrow$ & \\textbf{AR GAR}$\\uparrow$ & \\textbf{TF PPL}$\\downarrow$ & \\textbf{AR PPL}$\\downarrow$ & \\textbf{Gap}$\\downarrow$ \\\\\n\\midrule\n\\multirow{4}{*}{Qwen-7B}\n  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\\times$ \\\\\n  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\\times$ \\\\\n  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\\times$ \\\\\n  & \\textbf{SS} & 0.498 & \\textbf{0.401} & 2.78 & 1.441 & \\textbf{1.2$\\times$} \\\\\n\\midrule\n\\multirow{4}{*}{Llama-8B}\n  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\\times$ \\\\\n  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\\times$ \\\\\n  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\\times$ \\\\\n  & \\textbf{SS} & 0.477 & \\textbf{0.166} & 2.82 & 1.370 & \\textbf{2.9$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 7,
        "newStart": 19,
        "newLines": 7,
        "lines": [
          "   & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\\times$ \\\\",
          "   & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\\times$ \\\\",
          "   & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\\times$ \\\\",
          "-  & \\textbf{SS} & 0.498 & \\textbf{0.401} & 2.78 & 1.441 & \\textbf{1.2$\\times$} \\\\",
          "+  & \\textbf{SS} & 0.502 & \\textbf{0.347} & 2.78 & 1.441 & \\textbf{1.4$\\times$} \\\\",
          " \\midrule",
          " \\multirow{4}{*}{Llama-8B}",
          "   & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\\times$ \\\\"
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

_source line 152_

<details open><summary>🔧 Tool call — Edit · `toolu_01FvSb5kvp1A3q5C9rrE1FrH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
  "old_string": "\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}",
  "new_string": "\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nAll Qwen rows use seed 42; SS per-seed mean analysis in Table~\\ref{tab:perseed-ss}.\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "f98d2202-c8d0-4917-8cd2-cb3d361e44f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqbr8pfav41b1eHu6NEsVU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 54333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 951
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

_source line 153 · 2026-05-25T20:50:45.569Z_

<details><summary>↩ Tool result · `toolu_01FvSb5kvp1A3q5C9rrE1FrH`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "a10a4dee-f9d7-40cc-b708-30bae45327ff",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
    "oldString": "\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}",
    "newString": "\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nAll Qwen rows use seed 42; SS per-seed mean analysis in Table~\\ref{tab:perseed-ss}.\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}",
    "originalFile": "% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct\n% Conditions shared by both models: Base, ThreadGate, LoRA-only\n% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0\n% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4\n% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)\n\\begin{table*}[t]\n\\centering\n\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}\n\\label{tab:crossmodel-detail}\n\\small\n\\begin{tabular}{@{}ll ccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Condition} & \\textbf{TF GAR}$\\uparrow$ & \\textbf{AR GAR}$\\uparrow$ & \\textbf{TF PPL}$\\downarrow$ & \\textbf{AR PPL}$\\downarrow$ & \\textbf{Gap}$\\downarrow$ \\\\\n\\midrule\n\\multirow{4}{*}{Qwen-7B}\n  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\\times$ \\\\\n  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\\times$ \\\\\n  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\\times$ \\\\\n  & \\textbf{SS} & 0.502 & \\textbf{0.347} & 2.78 & 1.441 & \\textbf{1.4$\\times$} \\\\\n\\midrule\n\\multirow{4}{*}{Llama-8B}\n  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\\times$ \\\\\n  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\\times$ \\\\\n  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\\times$ \\\\\n  & \\textbf{SS} & 0.477 & \\textbf{0.166} & 2.82 & 1.370 & \\textbf{2.9$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 6,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " \\centering",
          " \\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.",
          " Gap ratio = TF GAR / AR GAR; lower is better (less exposure bias).",
          "+All Qwen rows use seed 42; SS per-seed mean analysis in Table~\\ref{tab:perseed-ss}.",
          " Qwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).",
          " Llama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}",
          " \\label{tab:crossmodel-detail}"
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

_source line 154_

<details open><summary>🔧 Tool call — Edit · `toolu_01GtcF5QMpWvx2WXRX6SXxQG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex",
  "old_string": "\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses 5 model-generated conversations with 10 turns each.}",
  "new_string": "\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses extended-generation protocol ($N{=}5$, $T{=}10$ turns); under the gen-mode protocol ($N{=}50$) used in Table~\\ref{tab:five-way}, AR GAR is 0.064 (s42) and 0.055 (s123) with gap ratios 7.9$\\times$ and 9.1$\\times$ respectively.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "27751820-5850-484c-bd75-4b42ea4d44dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqbr8pfav41b1eHu6NEsVU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 54333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 951
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

_source line 155 · 2026-05-25T20:50:51.417Z_

<details><summary>↩ Tool result · `toolu_01GtcF5QMpWvx2WXRX6SXxQG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "11832a74-1062-4798-8818-d1e3d73bdf95",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex",
    "oldString": "\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses 5 model-generated conversations with 10 turns each.}",
    "newString": "\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses extended-generation protocol ($N{=}5$, $T{=}10$ turns); under the gen-mode protocol ($N{=}50$) used in Table~\\ref{tab:five-way}, AR GAR is 0.064 (s42) and 0.055 (s123) with gap ratios 7.9$\\times$ and 9.1$\\times$ respectively.}",
    "originalFile": "% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123\n% TF eval: N=200 held-out conversations\n% AR eval: N=5, T=10 model-generated conversations (original eval protocol)\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses 5 model-generated conversations with 10 turns each.}\n\\label{tab:perseed-tg}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{@{}l cc c@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Teacher-Forced (TF)}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.504 & 0.505 & 0.504 $\\pm$ 0.001 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.015 & 0.012 & 0.014 $\\pm$ 0.002 \\\\\n\\quad PPL $\\downarrow$       & 2.784 & 2.780 & 2.782 $\\pm$ 0.003 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 0$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.016 & 0.017 & 0.016 $\\pm$ 0.001 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.019 & 0.018 & 0.019 $\\pm$ 0.001 \\\\\n\\quad PPL $\\downarrow$       & 1.360 & 1.386 & 1.373 $\\pm$ 0.018 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Derived}} \\\\\n\\quad Gap ratio (TF/AR GAR-ours) $\\downarrow$ & 32.1 & 30.6 & 31.4 $\\pm$ 1.1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 7,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " \\centering",
          " \\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.",
          " TF evaluation uses 200 held-out conversations.",
          "-AR evaluation uses 5 model-generated conversations with 10 turns each.}",
          "+AR evaluation uses extended-generation protocol ($N{=}5$, $T{=}10$ turns); under the gen-mode protocol ($N{=}50$) used in Table~\\ref{tab:five-way}, AR GAR is 0.064 (s42) and 0.055 (s123) with gap ratios 7.9$\\times$ and 9.1$\\times$ respectively.}",
          " \\label{tab:perseed-tg}",
          " \\resizebox{\\columnwidth}{!}{",
          " \\begin{tabular}{@{}l cc c@{}}"
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

_source line 156_

<details open><summary>🔧 Tool call — Edit · `toolu_01Ez9ESPStM2NTyN3vvt1hri`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "old_string": "Uniform Gate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\",
  "new_string": "Uniform Gate & 4.3M & 6.1 & 43\\,GB & $+$57K \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "e7ce42dd-ed8d-4cf0-9ea3-5d849a28ee94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqbr8pfav41b1eHu6NEsVU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 54333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 951
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

_source line 157 · 2026-05-25T20:50:51.538Z_

<details><summary>↩ Tool result · `toolu_01Ez9ESPStM2NTyN3vvt1hri`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "7c70f64d-a4a2-4b2d-81b8-9d1596294356",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "oldString": "Uniform Gate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\",
    "newString": "Uniform Gate & 4.3M & 6.1 & 43\\,GB & $+$57K \\\\",
    "originalFile": "\\section{Training Configuration}\\label{sec:appendix-hyper}\n\nTable~\\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\\times$ learning rate multiplier and are initialized with bias 1.5 ($\\sigma(1.5) \\approx 0.82$); the gate MLP adds ${\\sim}$57K parameters per variant ($<$0.001\\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.3 over 3 epochs (29.7--37.1\\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB VRAM), requiring 6--8 hours per variant.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\\dagger$ apply only to ThreadGate and its ablations.}\n\\label{tab:hyperparams}\n\\begin{tabular}{l@{\\hspace{8pt}}l}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\nBase model & Qwen-2.5-7B-Instruct \\\\\nLoRA rank / $\\alpha$ & 16 / 32 \\\\\nLoRA targets & \\texttt{q\\_proj}, \\texttt{v\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1$\\!=\\!0.9, $\\beta_2$\\!=\\!0.999) \\\\\nLearning rate & $2 \\times 10^{-4}$ \\\\\nGate LR mult.$^\\dagger$ & $10\\times$ \\\\\nBatch / grad accum & 1 / 8 (eff.\\ 8) \\\\\nEpochs & 3 \\\\\nMax seq length & 2048 \\\\\nTraining data & 8K UltraChat convs \\\\\nSeed & 42 (+123 for TG, SS) \\\\\n$\\lambda_\\text{GAR}$/$\\lambda_\\text{div}$ & 1.0 / 1.0 \\\\\nGAR target $\\tau$ & 0.5 \\\\\nGate init bias$^\\dagger$ & 1.5 ($\\sigma\\!\\approx\\!0.82$) \\\\\nGate hidden dim$^\\dagger$ & 64 \\\\\nTurn embed dim$^\\dagger$ & 16 \\\\\nGPU & RTX PRO 6000 (96\\,GB) \\\\\nTraining time & 6--8 h / variant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Loss Formulation Search}\\label{sec:appendix-loss}\n\nThe final MSE + gate diversity loss (\\S\\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.\n\n\\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.\n\n\\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\\text{mean}(\\text{GAR})$). The unbounded objective rewards full pass-through ($g \\to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\\lambda$=2 (v3), gates froze within 100 steps; at $\\lambda$=10 (v3b), convergence to identity accelerated; at $\\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.\n\n\\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.\n\n\\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\\tau$ incurs the same penalty as GAR below $\\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\\mathcal{L}_\\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).\n\n\\begin{table*}[t]\n\\centering\\footnotesize\n\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}\n\\label{tab:loss-iterations}\n\\begin{tabular}{l l l p{5.8cm} c c}\n\\toprule\n & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{Failure Mechanism} & \\textbf{GAR} & \\textbf{PPL} \\\\\n\\midrule\nv1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\\\\nv2  & Cumulative + $\\varepsilon$ & \\texttimes~same trajectory & Numerical instability from cumulative product; $\\varepsilon$-stabilization insufficient & ---  & ---  \\\\\nv3  & Maximize ($\\lambda$=2)  & \\texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\\\\nv3b & Maximize ($\\lambda$=10) & \\texttimes~identity collapse   & Higher $\\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\\\\nv5  & Maximize ($\\lambda$=1)  & \\texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\\\\nv6  & Smooth saturation       & \\texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\\\\nv7  & MSE + gate div          & \\checkmark~\\textbf{converged}  & \\textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Instruction Retention Details}\\label{sec:appendix-ir}\n\nTo evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\\beta$\\,=\\,3 steering on $N$\\,=\\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.\n\n\\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\\,=\\,54 paired evaluations (18 types $\\times$ 3 conversations per type) for the McNemar analysis.\n\n\\paragraph{Per-category results.} Table~\\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.\n\n\\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\\,=\\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.\n\nFigure~\\ref{fig:ir-bar} visualizes the per-category breakdown.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_instruction_retention.pdf}\n  \\caption{Instruction retention by constraint category under $\\beta$\\,=\\,3 steering. Content constraints benefit most (+23.8\\,pp); format and count constraints are unaffected.}\n  \\label{fig:ir-bar}\n\\end{figure}\n\n\\FloatBarrier\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Instruction retention by constraint category ($\\beta$\\,=\\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}\n\\label{tab:ir-results}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\Delta$ \\\\\n\\midrule\nContent    & 61.9\\% & 85.7\\% & +23.8\\,pp \\\\\nPosition   & 66.7\\% & 73.3\\% & +6.7\\,pp \\\\\nCount      & 100\\%  & 100\\%  & 0 \\\\\nFormat     & 100\\%  & 100\\%  & 0 \\\\\n\\midrule\n\\textbf{Overall} & 75.9\\% & 87.0\\% & +11.1\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Long-Conversation AR Evaluation}\\label{sec:appendix-n5}\n\nThe main results (Table~\\ref{tab:five-way}) report AR GAR from $N$\\,=\\,50 held-out conversations with a mean of 3.6 user turns. Table~\\ref{tab:n5-ar} presents complementary results on $N$\\,=\\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.\n\n\\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\\times$ (0.064 vs.\\ 0.037 in the $N$\\,=\\,50 evaluation) to 0.64$\\times$ (0.016 vs.\\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\\,=\\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.\n\n\\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\\times$ of the base model's GAR, compared to 3.4$\\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.\n\n\\paragraph{Caveats.} The $N$\\,=\\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{AR GAR-ours on $N$\\,=\\,5 ten-turn conversations. The gating advantage observed in Table~\\ref{tab:five-way} ($N$\\,=\\,50, mean 3.6 turns) diminishes with conversation length.}\n\\label{tab:n5-ar}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AR GAR-O} & \\textbf{$\\Delta$ vs.\\ Table~\\ref{tab:five-way}} \\\\\n\\midrule\nBase & 0.012 & $-$0.007 \\\\\n\\midrule\nThreadGate & 0.016 & $-$0.048 \\\\\n\\;+\\,PCGrad & 0.015 & $-$0.015 \\\\\nUniform Gate & 0.015 & $-$0.018 \\\\\nLoRA-only & 0.025 & $-$0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Statistical Test Details}\\label{sec:appendix-stats}\n\nAll statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\\ref{tab:stat-tests} consolidates the full results.\n\n\\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\\ LoRA-only comparison ($p$\\,=\\,0.004, $r$\\,=\\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\\ +PCGrad comparison ($p$\\,=\\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.\n\n\\paragraph{Bootstrap confidence intervals.} The 95\\% CIs in Table~\\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.\n\n\\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \\sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \\leq r < 0.5$ is medium, and $r \\geq 0.5$ is large. The TG vs.\\ LoRA-only effect ($r$\\,=\\,0.454) is medium, and TG vs.\\ Base ($r$\\,=\\,0.802) is large.\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \\leq 0.004$) survive this correction.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Consolidated statistical tests. All AR comparisons use $N$\\,=\\,50 conversations (39 with $\\geq$3 turns); gate conditioning uses 28 layers.}\n\\label{tab:stat-tests}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Test} & $p$ & $r$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{AR GAR-ours ($\\beta$\\,=\\,0)}} \\\\\nTG vs.\\ Base & Wilcoxon & $<$0.001 & 0.802 \\\\\nTG vs.\\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\\\\nTG vs.\\ +PCGrad & Wilcoxon & 0.002 & --- \\\\\nSS vs.\\ TG & Wilcoxon & $<$0.001 & 0.869 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Gate conditioning (28 layers)}} \\\\\nTurn 1 vs.\\ Turn 21 & Wilcoxon & $3.7\\!\\times\\!10^{-8}$ & 0.975 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Instruction retention}} \\\\\n$\\beta$\\,=\\,0 vs.\\ $\\beta$\\,=\\,3 & McNemar & 0.077 & --- \\\\\nGAR--compliance & Pearson & 0.007 & 0.200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Llama-3.1-8B Complete Results}\\label{sec:appendix-llama}\n\nTable~\\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \\S\\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.\n\n\\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\\ 0.50).\n\n\\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\\,=\\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\\% for ThreadGate (mean 0.043, std 0.100), and 5\\% of turn-level measurements exhibit sporadic attention spikes (GAR $\\geq$ 0.4). We therefore report both mean and median.\n\n\\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\\times$ by median for Llama vs.\\ 8--17$\\times$ for Qwen).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\\,=\\,50); AR: autoregressive ($N$\\,=\\,20 for Base/TG/LoRA-only, $N$\\,=\\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}\n\\label{tab:llama-full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{TF}} & \\multicolumn{2}{c}{\\textbf{AR}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\\\\n\\midrule\nBase & 0.017 & 3.45 & 0.009 & 0.009 \\\\\nThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\\\\nLoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\\\\n\\textbf{SS} & 0.477 & 2.82 & \\textbf{0.166} & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\FloatBarrier\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_crossmodel.pdf}\n  \\caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\\times$ by median), exceeding Qwen's 8$\\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}\n  \\label{fig:crossmodel}\n\\end{figure}\n\n\\paragraph{Cross-model summary.} Table~\\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\\approx$ 0.5, AR GAR $\\ll$ 0.1, gap $\\geq$ 7.9$\\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\\times$ by median for TG; mean-based range 11.2--17.2$\\times$) compared to Qwen's (7.9--13.5$\\times$) may reflect its deeper architecture (32 vs.\\ 28 layers), which allows more layers for distributional drift to compound through.\n\n\\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}\n\n\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\n\n\\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\\% longer than Qwen due to Llama's larger layer count (32 vs.\\ 28 layers).\n\n\\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\\% decline. This is steeper than Qwen's 70.8\\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\\ 28 KV heads).\n\n\\paragraph{Cross-model gradient analysis.} Table~\\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\\approx$\\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\\times$ on Qwen and 25.7$\\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \\emph{modus tollens} argument (\\S\\ref{subsec:pcgrad}): gradient direction conflict is not the primary cause of the TF-AR gap.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\\times$.}\n\\label{tab:gradient-crossmodel}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\\n\\midrule\nMean cos sim & $-$0.042 & +0.005 \\\\\nNeg-layer \\% & 67.9\\% & 53.1\\% \\\\\nNTP/GAR mag ratio & 14.7$\\times$ & 25.7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Additional Visualizations}\\label{sec:appendix-viz}\n\nThis section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.\n\n\\subsection{Gate Profile Heatmap}\n\nFigure~\\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_profile_heatmap.pdf}\n\\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\\times$ 5 conditions) and Llama-3.1-8B (32 layers $\\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}\n\\label{fig:gate-heatmap}\n\\end{figure}\n\n\\subsection{Cross-Model Gate Profile Comparison}\n\nFigure~\\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_profile_crossmodel.pdf}\n\\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}\n\\label{fig:gate-crossmodel}\n\\end{figure}\n\n\\subsection{Per-Turn AR GAR Decay}\n\nFigure~\\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\\% from turn 1 to turn 10; Llama base drops 90\\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\\ref{tab:five-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_ar_gar_perturn.pdf}\n\\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\\% (turn 1$\\to$10), Llama base drops 90\\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}\n\\label{fig:ar-gar-perturn}\n\\end{figure}\n\n\\subsection{Bootstrap Confidence Intervals}\n\nFigure~\\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\\% CIs reported in Table~\\ref{tab:five-way}.\n\n\\begin{figure}[H]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_bootstrap_ci.pdf}\n  \\caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\\ LoRA-only, $N$\\,=\\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\\,=\\,0.454).}\n  \\label{fig:bootstrap-ci}\n\\end{figure}\n\n\\subsection{Gate Value Distributions}\n\nFigure~\\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_distribution.pdf}\n\\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}\n\\label{fig:gate-distribution}\n\\end{figure}\n\n\\subsection{Training Loss Curves}\n\nFigure~\\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_training_loss_curves.pdf}\n\\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}\n\\label{fig:training-loss}\n\\end{figure}\n\n\\subsection{Full Attention Steering Results}\\label{sec:appendix-steering}\n\n\\begin{table*}[t]\n\\centering\\small\n\\caption{Full attention steering results across evaluation settings.\n\\textbf{Bold} indicates the operating point cited in the main text ($\\beta$\\,=\\,5).\nA visual gap separates the phase-transition boundary: GAR jumps sharply between $\\beta$\\,=\\,2 and $\\beta$\\,=\\,3 across all settings.}\n\\label{tab:steering-full}\n\\begin{tabular}{r cc cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,5, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,50, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,200, TF}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n$\\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\\\\n\\midrule\n0   & .028 & 1.41 & $.064 \\pm .081$ & $1.43 \\pm .10$ & .535 & 2.62 \\\\\n0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\\\\n1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\\\\n2   & .062 & 1.41 & $.128 \\pm .110$ & $1.48 \\pm .14$ & .611 & 2.69 \\\\\n\\addlinespace[3pt]\n3   & ---  & ---  & $.556 \\pm .060$ & $1.56 \\pm .17$ & .788 & 2.93 \\\\\n4   & ---  & ---  & $.644 \\pm .061$ & $1.67 \\pm .22$ & .817 & 3.49 \\\\\n\\textbf{5}  & \\textbf{.680} & \\textbf{1.91} & $\\mathbf{.727 \\pm .061}$ & $\\mathbf{1.77 \\pm .27}$ & \\textbf{.833} & \\textbf{6.15} \\\\\n10  & .959 & 4.22 & $.961 \\pm .015$ & $3.45 \\pm 1.78$ & .977 & 505.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_steering_standalone.pdf}\n  \\caption{Detailed $\\beta$-steering trade-off ($N$\\,=\\,50). GAR-ours (top) increases monotonically with $\\beta$; PPL (bottom) remains stable below $\\beta$\\,=\\,3 (9\\% cost), then rises sharply. The $\\beta$\\,=\\,3 operating point (circled) achieves 8.7$\\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}\n  \\label{fig:steering-standalone}\n\\end{figure}\n\n\\section{Per-Layer Gate Profile}\\label{sec:appendix-gate-profile}\n\nTable~\\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\\sigma$\\,=\\,0.051).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}\n\\label{tab:gate-profile}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cccccccc}\n\\toprule\nL0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\\\\n.883 & \\textbf{.793} & .996 & .988 & .984 & \\textbf{.797} & .961 & .918 \\\\\n\\midrule\nL8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\\\\n.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\\\\n\\midrule\nL16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\\\\n.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\\\\n\\midrule\nL24 & L25 & L26 & L27 & \\multicolumn{4}{c}{Summary} \\\\\n.980 & .984 & .988 & 1.00 & \\multicolumn{4}{c}{$\\bar{g}$\\,=\\,.947, $\\sigma$\\,=\\,.051} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.\n\n\\paragraph{Cross-model comparison.} See \\S\\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.\n\n\\section{Scheduled Sampling Implementation}\\label{sec:appendix-ss}\n\nOur scheduled sampling implementation follows \\citet{bengio2015scheduled} with modifications for multi-turn transformer training:\n\n\\paragraph{Sampling schedule.} The model-generated context ratio $\\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\\%) is lower than the nominal schedule due to per-sample Bernoulli variance.\n\n\\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.\n\n\\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\\ 0.947, min at L4 vs.\\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_training_dynamics.pdf}\n  \\caption{Scheduled sampling training dynamics: sampling ratio $\\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}\n  \\label{fig:ss-dynamics}\n\\end{figure}\n\n\\section{Computational Cost Analysis}\\label{sec:appendix-cost}\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\\,GB VRAM). VRAM reports peak allocated memory (excluding optimizer states).}\n\\label{tab:cost}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Params} & \\textbf{Time (h)} & \\textbf{VRAM} & \\textbf{Overhead} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Qwen-2.5-7B-Instruct}} \\\\\nLoRA-only & 4.2M & 5.7 & 42\\,GB & baseline \\\\\nThreadGate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\n\\;+\\,PCGrad & 4.3M & 8.0 & 43\\,GB & $+$33\\% \\\\\nUniform Gate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\nSS (s42) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\nSS (s123) & 4.3M & 10.8 & 43\\,GB & $+$80\\% \\\\\nSS (s456) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Llama-3.1-8B-Instruct}} \\\\\nLoRA-only & 4.2M & 7.0 & 45\\,GB & baseline \\\\\nThreadGate & 4.3M & 7.3 & 46\\,GB & $+$65K \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Parameter overhead.} ThreadGate adds ${\\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\\times$ 2K per gate MLP) and ${\\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.\n\n\\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 5.7--7.3 hours. PCGrad adds ${\\sim}$33\\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\\% (6.5h) due to efficient batched generation, while seed 123 adds 80\\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.\n\n\\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\\to$64$\\to$1 MLP forward pass per layer adds $<$0.1\\% latency. $\\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.\n\n\\section{Qualitative Steering Examples}\\label{sec:appendix-examples}\n\nTable~\\ref{tab:examples} illustrates the effect of $\\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''\n\n\\begin{table*}[t]\n\\centering\\small\n\\caption{Qualitative effect of $\\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}\n\\label{tab:examples}\n\\begin{tabular}{c p{5.5cm} p{5.5cm}}\n\\toprule\n\\textbf{Turn} & \\textbf{$\\beta$\\,=\\,0 (unsteered)} & \\textbf{$\\beta$\\,=\\,3 (steered)} \\\\\n\\midrule\n1 & \\checkmark~Three bullet points, on-topic & \\checkmark~Three bullet points, on-topic \\\\\n2 & \\checkmark~Three bullet points, relevant & \\checkmark~Three bullet points, relevant \\\\\n3 & $\\sim$~Four bullet points, partially on-topic & \\checkmark~Three bullet points, on-topic \\\\\n4 & \\texttimes~Free-form paragraph, no bullets & \\checkmark~Three bullet points, on-topic \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe pattern is consistent with the GAR decay analysis (\\S\\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\\ref{tab:ir-results} shows that content constraints benefit most from this effect.\n\n\\section{Gradient Conflict Analysis}\\label{sec:appendix-gradient}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth,height=0.42\\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}\n  \\caption{(a)~Training GAR convergence to target ($\\tau$\\,=\\,0.5). (b)~PCGrad removes gradient conflict but $\\mathcal{L}_\\text{GAR}$ still collapses, confirming that gradient direction conflict is not the primary cause (\\S\\ref{subsec:pcgrad}).}\n  \\label{fig:training-pcgrad}\n\\end{figure}\n\nThis section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \\S\\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.\n\n\\paragraph{Gradient direction analysis.} Figure~\\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate and PCGrad training. Under standard training, 79\\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\\%$\\to$71\\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.\n\n\\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\\rho$\\,=\\,$-$0.12, $p$\\,=\\,0.54 between gate value and conflict magnitude).\n\n\\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\\times$ at epoch~0 and 14.7$\\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\\% of the effective update magnitude, explaining why PCGrad is ineffective.\n\n\\paragraph{Cross-model consistency.} Table~\\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \\textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient direction conflict is not the primary cause.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gradient_conflict_heatmap.pdf}\n\\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\\% to 68\\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\\%$\\to$71\\%) but does not improve AR GAR, ruling out gradient direction conflict as the primary cause (\\S\\ref{subsec:pcgrad}).}\n\\label{fig:gradient-heatmap}\n\\end{figure*}\n\n\\section{Training Data Characteristics}\\label{sec:appendix-data}\n\nAll experiments use 8,000 multi-turn conversations sampled from the UltraChat \\citep{ding2023ultrachat} training split. Table~\\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\\,=\\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\\,=\\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\\ref{sec:appendix-n5}).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Training and evaluation data characteristics. All data from UltraChat \\citep{ding2023ultrachat}.}\n\\label{tab:data-stats}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Property} & \\textbf{Train} & \\textbf{Eval (primary)} \\\\\n\\midrule\nConversations & 8,000 & 50 \\\\\nMin user turns & 3 & 3 \\\\\nMax sequence length & 2,048 & 2,048 \\\\\nSource & UltraChat train & UltraChat train \\\\\nOverlap & --- & non-overlapping \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Exposure Bias Scaling}\\label{sec:appendix-eb-scaling}\n\nFigure~\\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).\n\n\\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.9$\\times$) while PCGrad shows the largest (16.7$\\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\\sim}$1.2$\\times$, the only variant approaching parity. The ordering of gap ratios (SS $\\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\\sim$27$\\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\\ 28 layers), which provides more layers for distributional drift to compound through.\n\n\\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\\,=\\,50), ThreadGate's gap is 8$\\times$; at 10 turns ($N$\\,=\\,5), it widens to 31$\\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.\n\n\\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\\sim}$1.2$\\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\\ref{sec:appendix-steering-viz}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_eb_scaling.pdf}\n\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}\n\\label{fig:eb-scaling}\n\\end{figure}\n\n\\section{Per-Turn AR GAR Dynamics}\\label{sec:appendix-ar-gar-dynamics}\n\nTo characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.\n\nAll six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\\S\\ref{subsec:ss}).}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_curves.pdf}\n\\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}\n\\label{fig:kl_ar_gar_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_bar.pdf}\n\\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}\n\\label{fig:kl_ar_gar_bar}\n\\end{figure}\n\nThis pattern contrasts with teacher-forced evaluation, where GAR remains relatively stable across turns for all configurations. Under teacher forcing, the model conditions on ground-truth context at each turn, preventing the distributional drift that causes GAR erosion in AR mode. The divergence between TF stability and AR decay provides turn-level evidence for the exposure bias mechanism described in \\S\\ref{sec:analysis}: training-time attention patterns are optimized for a distribution that AR generation progressively departs from.\n\n\\section{Per-Head KL Divergence Analysis}\\label{sec:appendix-kl}\n\nTo test whether exposure bias selectively disrupts goal-attending heads rather than uniformly affecting all attention patterns, we compute per-head TF vs.\\ AR attention divergence on 30 held-out conversations. For each of the 28 attention heads per layer (784 heads total), we measure the KL divergence $D_\\text{KL}(p_\\text{TF} \\| p_\\text{AR})$ between teacher-forced and autoregressive attention distributions, and the absolute GAR shift $\\Delta\\text{GAR} = |\\text{GAR}_\\text{TF} - \\text{GAR}_\\text{AR}|$. This head-level analysis provides diagnostic evidence for the exposure bias interpretation beyond the aggregate TF-AR gap.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Per-head TF-AR divergence statistics for Base and ThreadGate (Qwen-2.5-7B, 30 conversations). TG trains more concentrated goal attention under TF, but these high-GAR heads shift most under AR ($r$\\,=\\,0.743).}\n\\label{tab:kl-perhead}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Base} & \\textbf{TG} \\\\\n\\midrule\nMean $\\Delta$GAR & 0.012 & 0.016 \\\\\nMean KL & 0.043 & 0.054 \\\\\nCorr(TF\\_GAR, $\\Delta$GAR) & 0.673 & 0.743 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selective disruption.} ThreadGate exhibits 35\\% larger mean $\\Delta$GAR (0.016 vs.\\ 0.012) and 26\\% larger mean KL (0.054 vs.\\ 0.043) than Base. This is counterintuitive: the auxiliary GAR loss successfully trains more concentrated goal attention (higher TF GAR per head), but these very same heads shift more under AR generation. The correlation between per-head TF GAR and $\\Delta$GAR is strong for both models ($r$\\,=\\,0.673 for Base, 0.743 for TG), confirming that heads with higher goal attention under teacher forcing are disproportionately disrupted under autoregressive generation. This selectivity is a hallmark of exposure bias: the training-time optimization succeeds at creating a specific attention pattern (concentrated goal attention), but precisely this pattern has no autoregressive counterpart because it depends on conditioning on ground-truth context.\n\n\\paragraph{Layer-depth dependence.} The highest-KL heads concentrate at output-adjacent layers (L23--L27, KL\\,$>$\\,0.077) and L9 (KL\\,$\\approx$\\,0.068). Output-adjacent layers participate most directly in next-token prediction, so their attention distributions are most sensitive to changes in the conditioning context. L9's elevated KL may reflect a ``routing layer'' phenomenon observed in multi-layer transformers, where specific intermediate layers specialize in long-range information routing. The depth dependence is consistent with cumulative error propagation: distributional drift from model-generated tokens accumulates as information flows through successive layers, producing the largest attention shifts at the deepest layers.\n\n\\paragraph{Gate--KL independence.} Gate magnitude does not predict per-layer exposure bias severity: Spearman correlation between gate value and per-layer KL is 0.061 ($p$\\,=\\,0.757). The highest KL values concentrate at deep layers (L22--L27) where gates are near identity ($\\approx$1.0), while the lowest-gate layers show below-average KL (0.041 vs.\\ 0.056 for highest-gate layers). This independence confirms that the gating mechanism and the exposure bias phenomenon operate on different axes: gates modulate the magnitude of residual contributions, while exposure bias disrupts the direction (attention distribution) of those contributions. Even a ``perfect'' gate that could fully attenuate certain layers' residuals would not address the fundamental distributional mismatch that causes the attention shift.\n\n\\section{GAR Definition Robustness}\\label{sec:appendix-gar-robust}\n\nTo assess whether our conclusions depend on the specific GAR definition, we evaluate four alternative token-position variants on 50 held-out conversations (Table~\\ref{tab:gar-robust}): (1)~\\emph{ours} (last-token): attention from the last token to goal tokens (standard GAR-ours); (2)~\\emph{all-token}: average attention from all tokens to goal tokens; (3)~\\emph{first-token}: attention from the first assistant token to goal tokens; (4)~\\emph{goal-only}: attention from the last token to system-prompt-only tokens (excluding conversation content).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Mid-turn GAR under four alternative definitions ($N$\\,=\\,50 conversations). ThreadGate only improves query-position-specific definitions (last-token, goal-only); Scheduled Sampling raises all four definitions above 0.36.}\n\\label{tab:gar-robust}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Definition} & \\textbf{Base} & \\textbf{TG} & \\textbf{SS} \\\\\n\\midrule\nOurs (last-token) & 0.015 & \\textbf{0.325} & \\textbf{0.458} \\\\\nAll-token & 0.015 & 0.025 & \\textbf{0.366} \\\\\nFirst-token & 0.022 & 0.039 & \\textbf{0.412} \\\\\nGoal-only & 0.005 & \\textbf{0.310} & \\textbf{0.444} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThreadGate improvements are query-position-specific: the two definitions using the last token as query (ours: $0.015 \\to 0.325$; goal-only: $0.005 \\to 0.310$) show large gains, while all-token ($0.025$) and first-token ($0.039$) remain near base levels. This is expected: the GAR loss optimizes attention at the last-token position, so the learned routing does not generalize to other query positions.\n\nScheduled Sampling raises all four definitions above 0.36, with no definition falling below Base-relative gains. This confirms that SS builds a broad goal-attention pattern across token positions, rather than overfitting to the specific position targeted by the GAR loss. The pattern holds regardless of GAR definition: both the exposure bias diagnosis and the SS mitigation are robust to metric choice.\n\n\\section{General Capability Preservation (MMLU)}\\label{sec:appendix-mmlu}\n\nTo confirm that auxiliary GAR losses and attention steering do not degrade general language understanding, we evaluate all six Qwen-2.5-7B variants on MMLU 5-shot \\citep{hendrycks2021measuring} ($N$\\,=\\,14{,}042 questions).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\\,pp of the base LoRA-only checkpoint.}\n\\label{tab:mmlu}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{Acc (\\%)} & \\textbf{$\\Delta$ vs Base} \\\\\n\\midrule\nBase (pretrained) & 74.23 & --- \\\\\nPCGrad & 73.86 & $-$0.38 \\\\\nSS & 73.75 & $-$0.48 \\\\\nLoRA-only & 73.57 & $-$0.66 \\\\\nThreadGate & 73.47 & $-$0.77 \\\\\nUniform Gate & 73.46 & $-$0.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll variants degrade by $<$0.8\\,pp, confirming that attention steering and auxiliary GAR losses do not harm general language understanding. The ordering does not track GAR performance (e.g., PCGrad shows the smallest MMLU drop despite the worst AR GAR), consistent with GAR and NTP occupying largely orthogonal subspaces.\n\n\\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b}\n\nWe validate cross-scale on Qwen-2.5-1.5B-Instruct to test whether goal attention decay and $\\beta$-steering generalize to smaller models.\n\n\\paragraph{Phase~1 GAR decay.} The 1.5B base model exhibits 79.8\\% GAR decline from turn~1 to mid-turns (vs.\\ 70.8\\% on 7B), confirming that attention decay is present across scales and is more severe at smaller model sizes.\n\n\\paragraph{Steering evaluation.} Table~\\ref{tab:1.5b-steering} reports AR evaluation ($N$\\,=\\,50). We report median PPL because Base $\\beta$\\,=\\,3 contains a catastrophic outlier (conversation~\\#11, PPL\\,$>$\\,$10^8$) that inflates the mean.\\footnote{The outlier occurs in a single conversation where $\\beta$-steering causes the base model to enter a degenerate repetition loop. ThreadGate produces zero such outliers across all $\\beta$ values, suggesting the gate provides stability against catastrophic steering failures.}\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Cross-scale $\\beta$-steering on Qwen-2.5-1.5B ($N$\\,=\\,50, AR). PPL is median due to catastrophic Base outlier at $\\beta$\\,=\\,3. TG eliminates outliers across all $\\beta$ values.}\n\\label{tab:1.5b-steering}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Model} & $\\beta$ & \\textbf{AR GAR} & \\textbf{PPL (med)} \\\\\n\\midrule\nBase & 0 & 0.017 & 1.909 \\\\\nTG & 0 & 0.023 & 1.897 \\\\\n\\midrule\nBase & 3 & 0.120 & 2.216 \\\\\nTG & 3 & 0.114 & 1.975 \\\\\n\\midrule\nBase & 5 & 0.657 & 2.804 \\\\\nTG & 5 & 0.715 & 2.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe steering pattern mirrors the 7B results: $\\beta$\\,=\\,5 recovers GAR to 0.657--0.715 ($p < 0.001$), confirming that attention misallocation is the proximal cause of GAR collapse across scales. At $\\beta$\\,=\\,0, TG shows a small but significant GAR advantage ($p$\\,=\\,0.005); at $\\beta$\\,=\\,3, the TG--Base difference is not statistically significant ($p$\\,=\\,0.815), unlike the 7B pattern where TG consistently outperforms Base. This scale-specific difference may reflect the 1.5B model's limited capacity to maintain learned routing at intermediate steering strengths. ThreadGate does provide a stability advantage---zero catastrophic PPL outliers vs.\\ one in Base---suggesting that residual gating regularizes attention distributions even when aggregate GAR is comparable.\n\n\\section{Per-Seed Detailed Results}\\label{sec:appendix-perseed}\n\nTables~\\ref{tab:perseed-ss} and~\\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.\n\n\\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\\pm0.032$ across seeds under the held-out protocol (Table~\\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\\,=\\,200 sample. AR GAR shows meaningful variance (std\\,=\\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\\times$), seed 123 is intermediate (0.423, gap 1.3$\\times$), and seed 456 is highest (0.433, gap 1.2$\\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\\beta$\\,=\\,5, the cross-seed variance nearly vanishes ($0.717\\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.\n\n\\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\\pm0.001$) and similar AR GAR (0.064 vs.\\ 0.055), with gap ratios of 7.9$\\times$ and 9.1$\\times$ respectively. The 15\\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.\n\n\\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\\% overhead) vs.\\ 6.5 hours for seeds 42 and 456 (8\\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-generated contexts: seed 123 happens to trigger longer autoregressive generation episodes early in training, where the model produces longer outputs before hitting the max-length cutoff. Despite this training-time variance, all three seeds converge to similar final metrics, suggesting the optimization landscape is robust.\n\n\\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}\n\n\\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}\n\n\\section{Per-Turn GAR Decay Analysis}\\label{sec:appendix-perturn-detail}\n\nTables~\\ref{tab:perturn-qwen} and~\\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\\ref{tab:five-way}).\n\n\\paragraph{Qwen per-turn dynamics.} On Qwen (Table~\\ref{tab:perturn-qwen}), all non-SS variants show rapid monotonic decay: turn-1 GAR ranges from 0.085 (Base) to 0.130 (ThreadGate), but by turn~5 all collapse below 0.07. The decay rate is approximately exponential for the first 3 turns, then plateaus near a floor value that varies by configuration (Base: 0.004, ThreadGate: 0.043--0.066, LoRA-only: 0.040). ThreadGate and LoRA-only show occasional turn-level fluctuations (e.g., TG turn~5 = 0.066 $>$ turn~4 = 0.043), which reflect stochastic variation in individual conversations rather than systematic recovery. Scheduled sampling retains substantially higher GAR throughout (turn-5 GAR\\,=\\,0.365 vs.\\ 0.066 for ThreadGate), with a much flatter decay profile (15\\% decline from turn~1 to turn~5 vs.\\ 49\\% for ThreadGate). This flatter profile is the signature of distributional robustification: SS-trained models encounter model-generated context during training, so the attention patterns are calibrated for the distribution they actually face during inference.\n\n\\paragraph{Llama per-turn dynamics.} On Llama (Table~\\ref{tab:perturn-llama}), the decay is steeper: Base GAR drops from 0.028 to 0.008 over 4 turns (71\\% decline in the $N$\\,=\\,20 evaluation), and from 0.026 to 0.003 over 10 turns (88\\% decline in the $N$\\,=\\,5 long-conversation evaluation). ThreadGate on Llama shows a distinctive pattern: turn-level GAR is roughly constant (0.038--0.049) rather than monotonically declining, suggesting that the gating mechanism maintains a stable floor on Llama that it fails to maintain on Qwen. However, this floor (0.04) is still an order of magnitude below the TF target (0.484), confirming that the fundamental TF-AR gap persists.\n\n\\paragraph{Cross-architecture comparison.} The per-turn decay profiles reveal an architectural difference: Qwen shows a sharper initial decline (turn~1 to turn~2: $-$62\\% for Base) followed by a plateau, while Llama shows a more gradual and sustained decline throughout. This difference may reflect the two architectures' different attention head configurations and layer counts, but the qualitative pattern---monotonic or near-monotonic decline toward a near-zero floor---is universal.\n\nFigures~\\ref{fig:perturn-qwen-detail} and~\\ref{fig:perturn-llama-detail} visualize these trajectories.\n\n\\input{../artifacts/appendix_expansion/tab_perturn_qwen.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_perturn_qwen_detail.pdf}\n  \\caption{Per-turn AR GAR-ours across six Qwen-2.5-7B configurations. Scheduled sampling (green) retains far higher GAR than all other variants, which cluster below 0.13 and decay rapidly.}\n  \\label{fig:perturn-qwen-detail}\n\\end{figure}\n\n\\input{../artifacts/appendix_expansion/tab_perturn_llama.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_perturn_llama_detail.pdf}\n  \\caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\\,=\\,20, 4 turns). (b)~Extended Base decay profile ($N$\\,=\\,5, 10 turns), showing 90\\% decline.}\n  \\label{fig:perturn-llama-detail}\n\\end{figure}\n\n\\section{Extended Dataset Statistics}\\label{sec:appendix-dataset-ext}\n\nTable~\\ref{tab:dataset_stats} provides detailed statistics for the UltraChat training and evaluation splits. From the full UltraChat-200K corpus (207,865 conversations in the \\texttt{train\\_sft} split), we filter for conversations with $\\geq$5 assistant turns, yielding 17,302 candidates (8.3\\% of the full corpus). We randomly sample 8,000 for training, 50 for primary AR evaluation (mean 3.6 user turns), 50 for IID GAR diagnostics, and 200 for the instruction retention evaluation.\n\n\\paragraph{Filtering rationale.} The $\\geq$5 assistant turns threshold was chosen empirically: conversations with fewer than 3 assistant turns do not exhibit measurable attention decay (turn-1 to turn-3 GAR decline $<$5\\%), making them uninformative for studying multi-turn exposure bias. The 5-turn threshold provides sufficient turn depth while retaining a reasonable fraction of the corpus. The average conversation in the filtered set contains 5.6 assistant turns (range: 5--7), with a mean sequence length of 1,247 tokens after tokenization with the Qwen-2.5 tokenizer.\n\n\\paragraph{Evaluation split design.} We maintain four non-overlapping evaluation sets to avoid contamination: (1)~the primary AR evaluation ($N$\\,=\\,50) uses the same conversation structure as training but with held-out conversations, enabling direct comparison of TF vs.\\ AR behavior; (2)~the IID GAR diagnostic ($N$\\,=\\,50) uses a separate sample for ablation studies that require independent measurements; (3)~the large instruction retention set ($N$\\,=\\,200) provides sufficient statistical power for per-category compliance analysis across 18 constraint types; (4)~the long-conversation set ($N$\\,=\\,5, 10 turns each) tests scaling behavior beyond the training distribution.\n\n\\paragraph{Domain diversity.} UltraChat covers a broad range of conversational topics including knowledge Q\\&A, creative writing, reasoning, and open-ended discussion. We do not stratify by topic, as our focus is on the architectural mechanism (attention routing) rather than domain-specific performance. The topic diversity serves as implicit regularization against overfitting to specific conversation patterns.\n\n\\input{../artifacts/appendix_expansion/tab_dataset_stats.tex}\n\n\\section{Extended GAR Robustness Analysis}\\label{sec:appendix-gar-ext}\n\nTable~\\ref{tab:gar_robustness} and Figure~\\ref{fig:gar-robust-grouped} extend the GAR robustness analysis from \\S\\ref{sec:appendix-gar-robust} with turn-1 GAR and gap ratio metrics across all four token-position variants. We evaluate four ways to select the query token position for gradient attribution: (1)~\\textit{Last} (our default): the final token of each assistant turn, which captures the model's ``summary'' attention pattern at the prediction boundary; (2)~\\textit{All}: the mean over all assistant tokens, providing a position-averaged view; (3)~\\textit{First}: the first assistant token, which reflects initial attention allocation; (4)~\\textit{Goal-only}: attention to goal tokens as defined by \\citet{dongre2026attention}, which restricts the target set to system-prompt tokens.\n\n\\paragraph{Position-specific vs.\\ broad improvement.} The key finding is a clear dichotomy between ThreadGate and Scheduled Sampling. ThreadGate improvements are restricted to last-token and goal-only positions (the two definitions sharing the query position targeted by the GAR loss): gap ratios drop to 1.21$\\times$ and 1.07$\\times$ respectively. All-token (5.04$\\times$) and first-token (8.24$\\times$) GAR remain near base levels, confirming that the learned routing is position-specific. Scheduled Sampling raises all four definitions above 0.36 with gap ratios $\\leq$1.83$\\times$, demonstrating that distributional robustification builds broad goal attention across token positions rather than overfitting to the position targeted by the loss.\n\n\\paragraph{Turn-1 vs.\\ mid-turn dynamics.} Turn-1 GAR is consistently higher than mid-turn GAR across all definitions and conditions, reflecting the first turn's proximity to the ground-truth prefix in training. The gap ratio quantifies how much of this initial attention survives into later turns. First-token GAR shows the largest gap ratios (Base: 13.3$\\times$, TG: 8.2$\\times$), indicating that the first-token position is most vulnerable to distributional drift---the initial token's attention pattern is highly dependent on the conditioning context, which diverges most from training under autoregressive generation.\n\n\\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_gar_robustness_grouped.pdf}\n  \\caption{Mid-turn GAR across four token-position definitions. SS raises all four above 0.36; TG only improves last-token and goal-only.}\n  \\label{fig:gar-robust-grouped}\n\\end{figure}\n\n\\section{MMLU Category Breakdown}\\label{sec:appendix-mmlu-ext}\n\nTable~\\ref{tab:mmlu_detail} breaks down MMLU 5-shot accuracy by category (STEM, Social Sciences, Humanities, Other) for all six Qwen-2.5-7B training configurations. This analysis addresses a potential concern: that auxiliary attention objectives might divert representational capacity from general language understanding, particularly in knowledge-intensive STEM domains.\n\n\\paragraph{Per-category analysis.} The maximum per-category degradation is 1.5\\,pp (ThreadGate on STEM), and no category shows systematic degradation across all variants. Notably, the ordering of variants differs across categories: ThreadGate shows the largest STEM drop but the smallest Humanities drop, while PCGrad shows the smallest overall drop despite having the worst AR GAR. This lack of correlation between GAR performance and MMLU degradation is consistent with GAR and NTP occupying largely orthogonal parameter subspaces---the LoRA adapter capacity (4.2M parameters) is sufficient to accommodate both objectives without interference.\n\n\\paragraph{Statistical significance.} The per-category differences are small relative to the evaluation noise: with $N$\\,=\\,14,042 questions total ($\\sim$3,500 per category), a 0.8\\,pp accuracy difference corresponds to $\\sim$28 questions, well within expected stochastic variation for 5-shot in-context learning. A chi-squared test comparing the best (PCGrad, 73.86\\%) and worst (Uniform Gate, 73.46\\%) variants yields $p$\\,=\\,0.503, confirming no significant difference. The category-level stability confirms that auxiliary GAR losses and gating do not selectively harm any knowledge domain.\n\nFigure~\\ref{fig:mmlu-comparison} visualizes the per-category comparison, showing tight clustering across all variants within each category.\n\n\\input{../artifacts/appendix_expansion/tab_mmlu_detail.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_mmlu_comparison.pdf}\n  \\caption{MMLU 5-shot accuracy by category across training configurations. All variants remain within 1.5\\,pp of the LoRA-only baseline across all categories.}\n  \\label{fig:mmlu-comparison}\n\\end{figure}\n\n\\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b-ext}\n\nTable~\\ref{tab:qwen15b_results} extends the cross-scale analysis with Phase~1 GAR diagnostics, detailed Phase~2 training results, and $\\beta$-steering evaluation on the Qwen-2.5-1.5B-Instruct model.\n\n\\paragraph{Phase 1: GAR decay.} The 1.5B base model exhibits 79.8\\% relative GAR decline from turn~1 to mid-turns, more severe than the 7B model's 70.8\\% decline. This scale-dependent decay severity is consistent with smaller models having less redundant attention capacity: with 28 layers but only 1.5B parameters (vs.\\ 7B), each layer carries proportionally more of the total representational burden, leaving less room for goal-oriented attention to persist alongside the primary NTP objective.\n\n\\paragraph{Phase 2: Training.} ThreadGate training on 1.5B converges to TF GAR-ours of 0.498 with PPL of 2.67, closely matching the 7B results (0.504 / 2.78). The gate parameter count scales linearly with layer count (identical architecture, so ${\\sim}$57K gate parameters). Training completes in 2.1 hours vs.\\ 6.0 hours for 7B, reflecting the smaller model's reduced forward/backward pass cost.\n\n\\paragraph{Steering evaluation.} At $\\beta$\\,=\\,5, ThreadGate recovers GAR to 0.715 ($p < 0.001$), closely matching the 7B result (0.727). The recovery is essentially scale-independent at the strong steering regime: the attention bias added by $\\beta$-steering overwhelms any capacity differences. At $\\beta$\\,=\\,3, the picture differs: the TG--Base difference is not statistically significant ($p$\\,=\\,0.815) on 1.5B, unlike the significant difference on 7B ($p$\\,=\\,0.039). This scale-dependent response at intermediate $\\beta$ may reflect the 1.5B model's reduced capacity for fine-grained attention routing: with fewer parameters per layer, the model cannot sustain the subtle attention reweighting that $\\beta$\\,=\\,3 attempts.\n\n\\paragraph{Catastrophic outliers.} Base 1.5B at $\\beta$\\,=\\,3 produces one catastrophic PPL outlier (conversation \\#11, PPL $> 10^8$) caused by a degenerate repetition loop. ThreadGate produces zero such outliers across all $\\beta$ values, suggesting the gate provides a stabilizing effect on attention distributions even when aggregate GAR is comparable. We report median PPL to avoid this outlier dominating the central tendency estimate.\n\n\\input{../artifacts/appendix_expansion/tab_qwen15b_results.tex}\n\n\\section{Extended Statistical Analysis}\\label{sec:appendix-stats-ext}\n\nTable~\\ref{tab:statistical_tests} consolidates all statistical tests reported in this paper, including effect sizes, 95\\% bootstrap confidence intervals, and significance levels. This section provides methodological detail beyond the summary in Appendix~\\ref{sec:appendix-stats}.\n\n\\paragraph{Test selection rationale.} All primary comparisons use paired Wilcoxon signed-rank tests on $N$\\,=\\,39 conversations (those with $\\geq$3 turns from the 50-conversation held-out set). We use non-parametric tests because per-conversation GAR distributions are heavily right-skewed (skewness $>$ 2.0 for Base and PCGrad at $\\beta$\\,=\\,0), violating normality assumptions required by parametric alternatives. The pairing structure (same conversations evaluated under different training configurations) controls for conversation-level confounds (topic difficulty, conversation length, system-prompt complexity).\n\n\\paragraph{Effect size interpretation.} Effect sizes are computed as rank-biserial correlations ($r = Z / \\sqrt{N}$), following standard practice. The largest effect is SS vs.\\ TG ($r$\\,=\\,0.869, $p < 0.001$), a large effect by conventional thresholds ($r \\geq 0.5$), confirming that scheduled sampling produces a qualitatively different outcome. The TG vs.\\ Base effect ($r$\\,=\\,0.802) is also large, while TG vs.\\ LoRA-only ($r$\\,=\\,0.454) is medium, reflecting the modest incremental benefit of gating over LoRA alone.\n\n\\paragraph{Steering dose-response pattern.} At $\\beta$\\,=\\,0, all four comparisons are significant ($p \\leq 0.004$). At $\\beta$\\,=\\,3 (the phase transition), TG vs.\\ Base becomes marginally significant ($p$\\,=\\,0.039) and SS vs.\\ TG remains significant ($p$\\,=\\,0.010), but TG vs.\\ LoRA-only and PCGrad vs.\\ TG lose significance ($p > 0.7$). At $\\beta$\\,=\\,5, no pairwise comparison reaches significance---steering dominates and equalizes all variants. This dose-response pattern confirms that the training-time variant effects are real but small relative to the inference-time steering effect.\n\n\\paragraph{Instruction retention.} The instruction retention analysis uses McNemar's test on $N$\\,=\\,54 paired constraint evaluations (18 constraint types $\\times$ 3 conversations). The marginal significance ($p$\\,=\\,0.077) reflects the small sample size rather than a null effect: the point-biserial correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is significant when treating compliance as a continuous variable, and the per-category breakdown (Table~\\ref{tab:ir-results}) shows a clear content-constraint improvement (+23.8\\,pp).\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values for the same reason described in Appendix~\\ref{sec:appendix-stats}: comparisons are hypothesis-driven (each tests a specific causal exclusion in the analysis chain), not exploratory. All reported significant results ($p \\leq 0.039$) survive Holm-Bonferroni correction for the 4 primary comparisons within each $\\beta$ level.\n\n\\input{../artifacts/appendix_expansion/tab_statistical_tests.tex}\n\n\\section{Extended Training Dynamics}\\label{sec:appendix-training-ext}\n\nFigure~\\ref{fig:training-6panel} presents the complete training loss landscape for all five Qwen-2.5-7B conditions (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Scheduled Sampling) plus the base model, showing NTP loss, GAR loss, and total loss across three epochs.\n\n\\paragraph{NTP loss convergence.} All fine-tuned variants converge to NTP loss ${\\sim}$0.93 by epoch~3, with final-epoch values ranging from 0.929 (LoRA-only) to 0.934 (ThreadGate). PCGrad shows marginally higher variance due to gradient projection, but converges to the same terminal value. The uniformity of NTP convergence across variants---including those with auxiliary losses (ThreadGate, PCGrad) and those without (LoRA-only)---confirms that the GAR auxiliary objective does not interfere with the primary language modeling task during training.\n\n\\paragraph{GAR loss dynamics.} GAR loss collapses to near-zero within the first epoch under teacher forcing across all variants, consistent with the auxiliary objective being easy to optimize when the model conditions on ground-truth context. This rapid convergence is a double-edged sword: while it confirms that the MSE formulation (v7) achieves stable optimization, the ease of convergence also means the model never learns to maintain attention under distributional drift. The scheduled sampling variant shows distinctive dynamics: higher initial GAR loss variance from stochastic context mixing, with occasional spikes when a particularly challenging model-generated context is sampled, followed by convergence to a similar final value.\n\n\\paragraph{Training-inference disconnect.} The key observation is that training-time convergence is indistinguishable across variants: an observer with access only to training curves could not predict the 5.4$\\times$ AR GAR difference between SS and TG. This disconnect reinforces the diagnosis that the failure occurs at the training-to-inference transition, not during optimization, and explains why architectural modifications (gating, PCGrad) that operate during training cannot address the fundamental distributional mismatch.\n\n\\begin{figure*}[t]\n  \\centering\n  \\includegraphics[width=0.75\\textwidth]{fig_training_curves_6panel.pdf}\n  \\caption{Training loss curves for all five Qwen conditions. NTP loss (left) converges to ${\\sim}$0.93 across variants; GAR loss (center) collapses within epoch~1; total loss (right) is NTP-dominated. Training-time behavior is indistinguishable; the failure emerges only at inference.}\n  \\label{fig:training-6panel}\n\\end{figure*}\n\n\\section{Per-$\\beta$ Steering Visualization}\\label{sec:appendix-steering-viz}\n\nFigure~\\ref{fig:steering-4panel} visualizes per-turn GAR trajectories under four steering strengths ($\\beta$\\,=\\,0, 3, 5, 10), revealing the turn-level dynamics that underlie the aggregate steering results in Table~\\ref{tab:steering-full}.\n\n\\paragraph{Unsteered baseline ($\\beta$\\,=\\,0).} GAR decays monotonically from 0.12 to 0.02 over five turns, with the steepest decline between turns~1 and~2 ($-$44\\%). This trajectory matches the per-turn profiles in Appendix~\\ref{sec:appendix-perturn-detail} and confirms that the decay is a smooth, progressive phenomenon rather than a discrete failure at a specific turn.\n\n\\paragraph{Phase transition ($\\beta$\\,=\\,3).} Turn-1 GAR jumps to ${\\sim}$0.55, but per-turn decay persists (${\\sim}$15\\% decline from turn~1 to turn~5). This indicates that steering partially compensates for the distributional drift but does not eliminate it: the attention bias adds a constant offset to goal-token logits, while the drift compounds multiplicatively across turns. The residual decay at $\\beta$\\,=\\,3 explains why this operating point shows the strongest training-variant effects in the dose-response analysis (Appendix~\\ref{sec:appendix-stats-ext}).\n\n\\paragraph{Sustained recovery ($\\beta$\\,=\\,5).} GAR is sustained above 0.6 throughout, with minimal per-turn decay ($<$5\\% decline). At this steering strength, the constant attention bias dominates the per-turn drift, effectively replacing the lost training-time signal with an inference-time substitute. The 9\\% PPL cost (1.43 $\\to$ 1.77) is modest compared to the order-of-magnitude GAR recovery.\n\n\\paragraph{Saturation regime ($\\beta$\\,=\\,10).} GAR saturates near 1.0 across all turns but PPL degrades catastrophically ($>$3.5), as the excessive attention bias distorts the attention distribution beyond the model's capacity for coherent generation. This regime is impractical and serves as an upper bound on the steering approach.\n\n\\paragraph{Operating region.} The region $\\beta \\in [3, 5]$ balances GAR recovery against PPL cost, and the per-turn profiles confirm that steering must counteract an ongoing distributional drift rather than a one-time initialization failure---a key diagnostic that distinguishes exposure bias from alternative hypotheses (e.g., capacity limitations or optimization failures).\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_steering_perturn_4panel.pdf}\n  \\caption{Per-turn GAR under four $\\beta$-steering strengths. At $\\beta$\\,=\\,0, monotonic decay; at $\\beta$\\,=\\,3, partial recovery with residual decay; at $\\beta$\\,=\\,5, sustained high GAR; at $\\beta$\\,=\\,10, saturation with catastrophic PPL.}\n  \\label{fig:steering-4panel}\n\\end{figure}\n\n\\section{Llama-3.1-8B Scheduled Sampling Details}\\label{sec:appendix-llama-ss}\n\nLlama-3.1-8B-Instruct was trained with scheduled sampling using the same protocol as Qwen (\\S\\ref{sec:appendix-ss}), with one key difference: training was stopped at 2 epochs (${\\sim}$14{,}400 steps) instead of 3, because Llama's per-step wall-clock time was ${\\sim}$4$\\times$ slower than Qwen on the same hardware (624 steps/h vs.\\ ${\\sim}$2{,}400 steps/h for Qwen). This is attributable to different vocabulary sizes (Llama 128K vs.\\ Qwen 152K tokens) and attention implementation. The 2-epoch checkpoint was selected based on convergence of TF GAR (0.477, within 0.02 of Qwen's 3-epoch value 0.498).\n\n\\paragraph{$\\beta$-steering on Llama SS.}\nTable~\\ref{tab:llama-ss-steering} reports $\\beta$-steering results on the Llama SS model. Unlike Qwen, $\\beta$\\,=\\,3 does not trigger recovery on Llama (GAR 0.173 vs.\\ 0.166 at $\\beta$\\,=\\,0). At $\\beta$\\,=\\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias at higher steering strengths, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{$\\beta$-steering on Llama-3.1-8B SS model ($N$\\,=\\,50, $T$\\,=\\,4).}\n\\label{tab:llama-ss-steering}\n\\begin{tabular}{@{}l ccc@{}}\n\\toprule\n& $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\beta$\\,=\\,5 \\\\\n\\midrule\nAR GAR & 0.166 & 0.173 & 0.791 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-model comparison.}\nTable~\\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\\times$) is larger than Qwen's (1.2$\\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\\times$ (from 27$\\times$ to 2.9$\\times$) while Qwen reduces by 6.6$\\times$ (from 7.9$\\times$ to 1.2$\\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\\beta$-steering is more effective on Llama (0.791 vs.\\ 0.717 at $\\beta$\\,=\\,5), partially compensating for the weaker training-time compression.\n\n\\paragraph{Architectural differences.}\nSeveral architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.\n\n\\paragraph{Training dynamics.}\nThe Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\\sim}$0.20 at the end of epoch~2 (vs.\\ 0.30 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (27$\\times$ $\\to$ 2.9$\\times$ by median) but leaves a larger residual gap than Qwen's full 3-epoch schedule.\n\n\\begin{table}[t]\n\\raggedright\\small\n\\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\\ Llama-3.1-8B.}\n\\label{tab:llama-vs-qwen-ss}\n\\begin{tabular}{@{}l cc@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\\n\\midrule\nSS epochs & 3 & 2 \\\\\nTF GAR & 0.498 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.2$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.6$\\times$ & 9.3$\\times$ \\\\\nAR GAR ($\\beta$\\,=\\,5) & 0.717 & 0.791 \\\\\nTF PPL & 2.78 & 2.82 \\\\\nAR PPL & 1.441 & 1.370 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Use of AI Assistants}\\label{sec:appendix-ai}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 397,
        "oldLines": 7,
        "newStart": 397,
        "newLines": 7,
        "lines": [
          " LoRA-only & 4.2M & 5.7 & 42\\,GB & baseline \\\\",
          " ThreadGate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\",
          " \\;+\\,PCGrad & 4.3M & 8.0 & 43\\,GB & $+$33\\% \\\\",
          "-Uniform Gate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\",
          "+Uniform Gate & 4.3M & 6.1 & 43\\,GB & $+$57K \\\\",
          " SS (s42) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\",
          " SS (s123) & 4.3M & 10.8 & 43\\,GB & $+$80\\% \\\\",
          " SS (s456) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\"
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

_source line 158_

Now updating all text references to SS gap from 1.2× to 1.3× in main text files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "2fb5c133-9af1-42b1-921c-c4b85ea0839d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJXPM2XCBNSkNmHU7oMiPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16597,
      "cache_read_input_tokens": 55284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16597
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


### Tool call

_source line 159_

<details open><summary>🔧 Tool call — Edit · `toolu_01EZL6tYrpVQDEJbVpGBm8qY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "old_string": "\\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$, the only variant approaching parity across five training conditions.}",
  "new_string": "\\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity across five training conditions.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "60744295-e50e-4506-a951-7a84fc1a9231",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJXPM2XCBNSkNmHU7oMiPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16597,
      "cache_read_input_tokens": 55284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16597
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


### Tool result

_source line 160 · 2026-05-25T20:50:59.053Z_

<details><summary>↩ Tool result · `toolu_01EZL6tYrpVQDEJbVpGBm8qY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "773ad53b-5106-4068-9a8d-6ea44df73ce0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
    "oldString": "\\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$, the only variant approaching parity across five training conditions.}",
    "newString": "\\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity across five training conditions.}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\nWe fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; training costs in Appendix~\\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; dataset statistics in Appendices~\\ref{sec:appendix-data} and~\\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and perplexity (PPL).\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:five-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.62--2.78. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\\leq$2\\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, indicating that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\\S\\ref{subsec:ss}).\n\nUnder AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendices~\\ref{sec:appendix-stats} and~\\ref{sec:appendix-stats-ext}), yet the gap remains 7.9$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (per-category breakdown in Appendix~\\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \\S\\ref{sec:analysis}.\n\n\\begin{figure*}[!t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig5_attention_steering.pdf}\n  \\caption{Inference-time $\\beta$-steering recovers GAR from 0.064 to 0.727, consistent with attention misallocation as a proximal cause (9\\% PPL cost at $\\beta$\\,=\\,3; phase transition at $\\beta \\in [2, 3]$).}\n  \\label{fig:steering-recovery}\n\\end{figure*}\n\n\\subsection{Inference-Time Attention Steering}\\label{subsec:steering}\n\nAll training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\\beta$ to pre-softmax attention logits for goal-token positions during generation:\n\\begin{equation}\n  \\tilde{A}_{i,j}^{(\\ell,h)} = A_{i,j}^{(\\ell,h)} + \\beta \\cdot \\mathbf{1}[j \\in \\mathcal{G}],\n\\end{equation}\nwhere $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}; per-$\\beta$ turn-level trajectories in Appendix~\\ref{sec:appendix-steering-viz}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does, consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\\ref{sec:appendix-examples}). Downstream, steering ($\\beta$\\,=\\,3) raises late-turn instruction compliance by +11.1\\,pp, though this effect does not reach conventional significance ($p$\\,=\\,0.077; content-constrained tasks benefit most, +23.8\\,pp; Appendix~\\ref{sec:appendix-ir}).\n\n\\subsection{Scheduled Sampling Compresses the TF--AR Gap}\\label{subsec:ss}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_gap_compression.pdf}\n  \\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$, the only variant approaching parity across five training conditions.}\n  \\label{fig:ss-gap}\n\\end{figure}\n\nScheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 7,
        "newStart": 31,
        "newLines": 7,
        "lines": [
          " \\begin{figure}[t]",
          "   \\centering",
          "   \\includegraphics[width=\\columnwidth]{fig_ss_gap_compression.pdf}",
          "-  \\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$, the only variant approaching parity across five training conditions.}",
          "+  \\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity across five training conditions.}",
          "   \\label{fig:ss-gap}",
          " \\end{figure}",
          " "
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

_source line 161_

<details open><summary>🔧 Tool call — Edit · `toolu_01AtYiPri4v2mwym8R7wqwWe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "old_string": "Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}).",
  "new_string": "Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.517\\pm0.032$; 3-seed mean) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "c7099d87-84a2-4526-a813-6e57b050ad9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJXPM2XCBNSkNmHU7oMiPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16597,
      "cache_read_input_tokens": 55284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16597
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


### Tool result

_source line 162 · 2026-05-25T20:51:01.276Z_

<details><summary>↩ Tool result · `toolu_01AtYiPri4v2mwym8R7wqwWe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "08f3df34-aaf4-43f4-af21-a0f03a736afa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
    "oldString": "Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}).",
    "newString": "Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.517\\pm0.032$; 3-seed mean) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}).",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\nWe fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; training costs in Appendix~\\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; dataset statistics in Appendices~\\ref{sec:appendix-data} and~\\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and perplexity (PPL).\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:five-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.62--2.78. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\\leq$2\\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, indicating that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\\S\\ref{subsec:ss}).\n\nUnder AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendices~\\ref{sec:appendix-stats} and~\\ref{sec:appendix-stats-ext}), yet the gap remains 7.9$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (per-category breakdown in Appendix~\\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \\S\\ref{sec:analysis}.\n\n\\begin{figure*}[!t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig5_attention_steering.pdf}\n  \\caption{Inference-time $\\beta$-steering recovers GAR from 0.064 to 0.727, consistent with attention misallocation as a proximal cause (9\\% PPL cost at $\\beta$\\,=\\,3; phase transition at $\\beta \\in [2, 3]$).}\n  \\label{fig:steering-recovery}\n\\end{figure*}\n\n\\subsection{Inference-Time Attention Steering}\\label{subsec:steering}\n\nAll training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\\beta$ to pre-softmax attention logits for goal-token positions during generation:\n\\begin{equation}\n  \\tilde{A}_{i,j}^{(\\ell,h)} = A_{i,j}^{(\\ell,h)} + \\beta \\cdot \\mathbf{1}[j \\in \\mathcal{G}],\n\\end{equation}\nwhere $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}; per-$\\beta$ turn-level trajectories in Appendix~\\ref{sec:appendix-steering-viz}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does, consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\\ref{sec:appendix-examples}). Downstream, steering ($\\beta$\\,=\\,3) raises late-turn instruction compliance by +11.1\\,pp, though this effect does not reach conventional significance ($p$\\,=\\,0.077; content-constrained tasks benefit most, +23.8\\,pp; Appendix~\\ref{sec:appendix-ir}).\n\n\\subsection{Scheduled Sampling Compresses the TF--AR Gap}\\label{subsec:ss}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_gap_compression.pdf}\n  \\caption{Scheduled sampling compresses the TF-AR gap from 7.9$\\times$ to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity across five training conditions.}\n  \\label{fig:ss-gap}\n\\end{figure}\n\nScheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 35,
        "oldLines": 6,
        "newStart": 35,
        "newLines": 6,
        "lines": [
          "   \\label{fig:ss-gap}",
          " \\end{figure}",
          " ",
          "-Scheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.2$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.",
          "+Scheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.9$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.517\\pm0.032$; 3-seed mean) with no PPL cost ($1.441\\pm0.002$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.",
          " ",
          " "
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

_source line 163_

<details open><summary>🔧 Tool call — Edit · `toolu_01WiDhYT9yDMQW86oKix6xgV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
  "old_string": "\\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.2$\\times$ (Qwen) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}",
  "new_string": "\\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.3$\\times$ (Qwen, 3-seed mean) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "db0c4b6b-5a34-4bfb-ba2e-418e5b0b7fab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJXPM2XCBNSkNmHU7oMiPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16597,
      "cache_read_input_tokens": 55284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16597
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


### Tool result

_source line 164 · 2026-05-25T20:51:07.942Z_

<details><summary>↩ Tool result · `toolu_01WiDhYT9yDMQW86oKix6xgV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "b81d3e7b-bd29-4117-aee5-feb13f8ad1ca",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
    "oldString": "\\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.2$\\times$ (Qwen) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}",
    "newString": "\\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.3$\\times$ (Qwen, 3-seed mean) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}",
    "originalFile": "\\section{Introduction}\\label{sec:introduction}\n\nMulti-turn dialogue is central to how large language models are deployed, from customer service to tutoring to long-form reasoning. Yet a persistent failure accompanies even the most fluent generation: as conversations grow longer, models pay progressively less attention to the system-prompt goals that define their task. \\citet{dongre2026attention} measured significant Goal Accessibility Ratio (GAR) decline across 12 models over extended conversations; in our own evaluation, goal attention drops by over 70\\% within just five turns. Crucially, this is not a representation problem: residual stream probes confirm that goal information persists (AUC\\,=\\,0.98). The model retains the knowledge of what it should attend to; it simply stops attending.\n\nExisting remedies address this decay at inference time. Split-softmax \\citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \\citep{xiao2024streaming} retains anchor tokens; Gated Attention \\citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. A natural alternative is to intervene during training: optimize goal attention directly through auxiliary losses trained alongside next-token prediction (NTP). Yet this strategy rests on an untested assumption: attention patterns learned under teacher forcing (TF) transfer to autoregressive (AR) generation. Classical exposure bias research \\citep{bengio2015scheduled,lamb2016professor} has shown that TF creates a training--inference distribution mismatch for RNN sequence models, but whether this mismatch extends to auxiliary attention objectives in multi-turn transformers remains unknown.\n\nWe test this assumption and find it fails. We introduce a controlled five-way testbed (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, and Base) designed not as competing solutions but as a causal exclusion chain (\\S\\ref{sec:comparison-design}), where each adjacent pair isolates one candidate failure mechanism. The result is unambiguous: every variant converges to target GAR under teacher forcing, yet goal attention collapses by an order of magnitude once the model generates its own context (Figure~\\ref{fig:headline}). The exclusion chain traces this collapse to exposure bias, the training--inference distribution mismatch, ruling out gradient direction conflict (PCGrad removes conflict yet \\emph{worsens} AR GAR), gating mechanism (Uniform Gate matches ThreadGate), and parameter capacity (LoRA-only shows the same pattern). Inference-time $\\beta$-steering confirms that the collapse reflects attention misallocation rather than representation degradation; scheduled sampling bridges the gap by exposing the model to its own generations during training.\n\n\\begin{figure*}[!ht]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig1_headline.pdf}\n  \\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.2$\\times$ (Qwen) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}\n  \\label{fig:headline}\n\\end{figure*}\n\nOur contributions are:\n\\begin{enumerate}\\raggedright\n    \\item \\textbf{Exposure bias characterization.} To our knowledge, the first empirical demonstration that exposure bias collapses auxiliary attention objectives in multi-turn transformers, with an order-of-magnitude TF--AR gap reproduced across two architectures (Qwen-2.5-7B, Llama-3.1-8B) and model scales (1.5B--8B).\n    \\item \\textbf{Causal exclusion testbed.} A five-way diagnostic design, informed by seven loss-formulation iterations, that isolates the failure mechanism via causal exclusion, including a PCGrad \\emph{modus tollens} argument ruling out gradient direction conflict ($p$\\,=\\,0.002, effect reverses).\n    \\item \\textbf{Attention misallocation diagnosis.} Inference-time $\\beta$-steering recovers goal attention with modest perplexity cost, evidence that the collapse is an attention routing failure, not a representational one.\n    \\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.2$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " \\begin{figure*}[!ht]",
          "   \\centering",
          "   \\includegraphics[width=\\textwidth]{fig1_headline.pdf}",
          "-  \\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.2$\\times$ (Qwen) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}",
          "+  \\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.3$\\times$ (Qwen, 3-seed mean) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}",
          "   \\label{fig:headline}",
          " \\end{figure*}",
          " "
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

_source line 165_

<details open><summary>🔧 Tool call — Edit · `toolu_01LPXeCa98ur5PazJcyex7Nj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
  "old_string": "\\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.2$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.",
  "new_string": "\\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.3$\\times$ on Qwen (3-seed mean) and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "09119220-08df-4610-9e3a-bf9700f41129",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJXPM2XCBNSkNmHU7oMiPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16597,
      "cache_read_input_tokens": 55284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16597
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


### Tool result

_source line 166 · 2026-05-25T20:51:11.877Z_

<details><summary>↩ Tool result · `toolu_01LPXeCa98ur5PazJcyex7Nj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "89197e85-2c31-4d01-9f48-199fe37460cd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
    "oldString": "\\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.2$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.",
    "newString": "\\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.3$\\times$ on Qwen (3-seed mean) and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.",
    "originalFile": "\\section{Introduction}\\label{sec:introduction}\n\nMulti-turn dialogue is central to how large language models are deployed, from customer service to tutoring to long-form reasoning. Yet a persistent failure accompanies even the most fluent generation: as conversations grow longer, models pay progressively less attention to the system-prompt goals that define their task. \\citet{dongre2026attention} measured significant Goal Accessibility Ratio (GAR) decline across 12 models over extended conversations; in our own evaluation, goal attention drops by over 70\\% within just five turns. Crucially, this is not a representation problem: residual stream probes confirm that goal information persists (AUC\\,=\\,0.98). The model retains the knowledge of what it should attend to; it simply stops attending.\n\nExisting remedies address this decay at inference time. Split-softmax \\citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \\citep{xiao2024streaming} retains anchor tokens; Gated Attention \\citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. A natural alternative is to intervene during training: optimize goal attention directly through auxiliary losses trained alongside next-token prediction (NTP). Yet this strategy rests on an untested assumption: attention patterns learned under teacher forcing (TF) transfer to autoregressive (AR) generation. Classical exposure bias research \\citep{bengio2015scheduled,lamb2016professor} has shown that TF creates a training--inference distribution mismatch for RNN sequence models, but whether this mismatch extends to auxiliary attention objectives in multi-turn transformers remains unknown.\n\nWe test this assumption and find it fails. We introduce a controlled five-way testbed (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, and Base) designed not as competing solutions but as a causal exclusion chain (\\S\\ref{sec:comparison-design}), where each adjacent pair isolates one candidate failure mechanism. The result is unambiguous: every variant converges to target GAR under teacher forcing, yet goal attention collapses by an order of magnitude once the model generates its own context (Figure~\\ref{fig:headline}). The exclusion chain traces this collapse to exposure bias, the training--inference distribution mismatch, ruling out gradient direction conflict (PCGrad removes conflict yet \\emph{worsens} AR GAR), gating mechanism (Uniform Gate matches ThreadGate), and parameter capacity (LoRA-only shows the same pattern). Inference-time $\\beta$-steering confirms that the collapse reflects attention misallocation rather than representation degradation; scheduled sampling bridges the gap by exposing the model to its own generations during training.\n\n\\begin{figure*}[!ht]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig1_headline.pdf}\n  \\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.9$\\times$ to 1.3$\\times$ (Qwen, 3-seed mean) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}\n  \\label{fig:headline}\n\\end{figure*}\n\nOur contributions are:\n\\begin{enumerate}\\raggedright\n    \\item \\textbf{Exposure bias characterization.} To our knowledge, the first empirical demonstration that exposure bias collapses auxiliary attention objectives in multi-turn transformers, with an order-of-magnitude TF--AR gap reproduced across two architectures (Qwen-2.5-7B, Llama-3.1-8B) and model scales (1.5B--8B).\n    \\item \\textbf{Causal exclusion testbed.} A five-way diagnostic design, informed by seven loss-formulation iterations, that isolates the failure mechanism via causal exclusion, including a PCGrad \\emph{modus tollens} argument ruling out gradient direction conflict ($p$\\,=\\,0.002, effect reverses).\n    \\item \\textbf{Attention misallocation diagnosis.} Inference-time $\\beta$-steering recovers goal attention with modest perplexity cost, evidence that the collapse is an attention routing failure, not a representational one.\n    \\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.2$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 5,
        "newStart": 18,
        "newLines": 5,
        "lines": [
          "     \\item \\textbf{Exposure bias characterization.} To our knowledge, the first empirical demonstration that exposure bias collapses auxiliary attention objectives in multi-turn transformers, with an order-of-magnitude TF--AR gap reproduced across two architectures (Qwen-2.5-7B, Llama-3.1-8B) and model scales (1.5B--8B).",
          "     \\item \\textbf{Causal exclusion testbed.} A five-way diagnostic design, informed by seven loss-formulation iterations, that isolates the failure mechanism via causal exclusion, including a PCGrad \\emph{modus tollens} argument ruling out gradient direction conflict ($p$\\,=\\,0.002, effect reverses).",
          "     \\item \\textbf{Attention misallocation diagnosis.} Inference-time $\\beta$-steering recovers goal attention with modest perplexity cost, evidence that the collapse is an attention routing failure, not a representational one.",
          "-    \\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.2$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.",
          "+    \\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.3$\\times$ on Qwen (3-seed mean) and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.",
          " \\end{enumerate}"
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

_source line 167_

<details open><summary>🔧 Tool call — Edit · `toolu_01MxwNRR571UzTQc4sKr3V2k`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
  "old_string": "Scheduled sampling compresses the gap to ${\\sim}$1.2$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds",
  "new_string": "Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen, 3-seed mean) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "7cc031e5-8eab-48c9-a81f-c50ad85cfbbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJXPM2XCBNSkNmHU7oMiPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16597,
      "cache_read_input_tokens": 55284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16597
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


### Tool result

_source line 168 · 2026-05-25T20:51:13.722Z_

<details><summary>↩ Tool result · `toolu_01MxwNRR571UzTQc4sKr3V2k`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "50cb992c-1d5a-45b3-8ac7-b7a7b1fd1e95",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
    "oldString": "Scheduled sampling compresses the gap to ${\\sim}$1.2$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds",
    "newString": "Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen, 3-seed mean) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds",
    "originalFile": "\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, consistent with attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.2$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds; to our knowledge, the first such transfer to auxiliary attention objectives in multi-turn transformers.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\section{Conclusion}\\label{sec:conclusion}",
          " ",
          "-\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, consistent with attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.2$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds; to our knowledge, the first such transfer to auxiliary attention objectives in multi-turn transformers.",
          "+\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, consistent with attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen, 3-seed mean) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds; to our knowledge, the first such transfer to auxiliary attention objectives in multi-turn transformers."
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

_source line 169_

<details open><summary>🔧 Tool call — Edit · `toolu_016K2AHSWZp3avtmRiZZcisc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "old_string": "weaker than Qwen's ${\\sim}$1.2$\\times$ likely due to fewer training epochs",
  "new_string": "weaker than Qwen's ${\\sim}$1.3$\\times$ (3-seed mean) likely due to fewer training epochs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "0683b5e6-8f3b-4de6-8016-797fbcabead1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJXPM2XCBNSkNmHU7oMiPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16597,
      "cache_read_input_tokens": 55284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16597
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


### Tool result

_source line 170 · 2026-05-25T20:51:15.593Z_

<details><summary>↩ Tool result · `toolu_016K2AHSWZp3avtmRiZZcisc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "8ae97328-442c-4bfd-bb26-33e61f5335a5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
    "oldString": "weaker than Qwen's ${\\sim}$1.2$\\times$ likely due to fewer training epochs",
    "newString": "weaker than Qwen's ${\\sim}$1.3$\\times$ (3-seed mean) likely due to fewer training epochs",
    "originalFile": "\\section{Analysis}\\label{sec:analysis}\n\n\\begin{figure*}[!t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig3_gate_shift.pdf}\n  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift ($N$\\,=\\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\\times$) exceed final $N$\\,=\\,50 estimates (8--17$\\times$; Table~\\ref{tab:five-way}) due to smaller sample size.}\n  \\label{fig:gate-shift}\n\\end{figure*}\n\nEach subsection kills one alternative hypothesis via causal exclusion: \\S\\ref{subsec:gate-conditioning}~turn conditioning, \\S\\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\\S\\ref{subsec:dist-shift}). \\S\\ref{subsec:mechanism-specificity} confirms selectivity; \\S\\ref{subsec:cross-model} confirms cross-architecture generalization.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nWe compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \\citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\\% attenuation; Table~\\ref{tab:five-way}; full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\\,=\\,0.777, L27\\,=\\,1.000) despite lacking turn conditioning; the structure thus arises from LoRA$+$GAR pressure (Figure~\\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?\n\n\\subsection{PCGrad Gradient Direction Conflict Exclusion}\\label{subsec:pcgrad}\n\nNTP and GAR gradients oppose in 68--79\\% of layers (cosine similarity $-$0.089$\\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\\times$ to 14.7$\\times$ (full gradient statistics in Appendix~\\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \\citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \\emph{diagnostic} tool rather than an optimization method.\n\nPCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \\emph{worsens}: 0.064$\\to$0.030 ($p$\\,=\\,0.002; Figure~\\ref{fig:training-pcgrad}b in Appendix~\\ref{sec:appendix-gradient}). By \\emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\\,=\\,+0.005) with 25.7$\\times$ NTP magnitude dominance (Table~\\ref{tab:gradient-crossmodel}).\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nThe TF-AR GAR gap persists across all variants (Table~\\ref{tab:five-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, evidence that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \\citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\\tau$\\,=\\,0.5 while AR GAR collapses (77--87\\% per-turn decay; Figure~\\ref{fig:attention-heatmap}; per-configuration AR trajectories in Appendix~\\ref{sec:appendix-ar-gar-dynamics}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling}).\n\n\\subsection{Mechanism Specificity}\\label{subsec:mechanism-specificity}\n\nWe test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed); exposure bias thus disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\\times$) and Qwen (1.28$\\times$) vs.\\ the order-of-magnitude GAR-ours collapse.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_multiseed.pdf}\n  \\caption{Multi-seed AR GAR under scheduled sampling ($\\beta$\\,=\\,0 and $\\beta$\\,=\\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\\to$0.001).}\n  \\label{fig:ss-multiseed}\n\\end{figure}\n\n\\subsection{Cross-Model Replication}\\label{subsec:cross-model}\n\nWe replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}; per-turn values in Appendix~\\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.\n\nScheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.2$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717; Appendix~\\ref{sec:appendix-llama-ss}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern (79.8\\% GAR decay, $\\beta$-steering recovery to 0.715; Appendix~\\ref{sec:appendix-1.5b}).\n\n",
    "structuredPatch": [
      {
        "oldStart": 38,
        "oldLines": 5,
        "newStart": 38,
        "newLines": 5,
        "lines": [
          " ",
          " We replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}; per-turn values in Appendix~\\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.",
          " ",
          "-Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.2$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717; Appendix~\\ref{sec:appendix-llama-ss}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern (79.8\\% GAR decay, $\\beta$-steering recovery to 0.715; Appendix~\\ref{sec:appendix-1.5b}).",
          "+Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.3$\\times$ (3-seed mean) likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717; Appendix~\\ref{sec:appendix-llama-ss}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern (79.8\\% GAR decay, $\\beta$-steering recovery to 0.715; Appendix~\\ref{sec:appendix-1.5b}).",
          " "
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

_source line 171_

Now updating appendix references. Need to handle lines 491, 495, and 500 (EB scaling section), and line 810 (llama SS comparison).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "e5d25055-e357-456f-a33a-e1395a5fca1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6SkmaP6R8FvufhX1T8jU1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2249,
      "cache_read_input_tokens": 71881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2249
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


### Tool call

_source line 172_

<details open><summary>🔧 Tool call — Edit · `toolu_012M7ckKmWhj6Rgg5b3NsF8Z`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "old_string": "Scheduled sampling reduces the gap to ${\\sim}$1.2$\\times$, the only variant approaching parity.",
  "new_string": "Scheduled sampling reduces the gap to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "1c460a19-496d-4d87-8971-ca823e67ce9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6SkmaP6R8FvufhX1T8jU1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2249,
      "cache_read_input_tokens": 71881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2249
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

_source line 173 · 2026-05-25T20:51:22.303Z_

<details><summary>↩ Tool result · `toolu_012M7ckKmWhj6Rgg5b3NsF8Z`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "3611a2fe-69cc-489d-ab81-9a4254bc623f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "oldString": "Scheduled sampling reduces the gap to ${\\sim}$1.2$\\times$, the only variant approaching parity.",
    "newString": "Scheduled sampling reduces the gap to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity.",
    "originalFile": "\\section{Training Configuration}\\label{sec:appendix-hyper}\n\nTable~\\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\\times$ learning rate multiplier and are initialized with bias 1.5 ($\\sigma(1.5) \\approx 0.82$); the gate MLP adds ${\\sim}$57K parameters per variant ($<$0.001\\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.3 over 3 epochs (29.7--37.1\\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB VRAM), requiring 6--8 hours per variant.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\\dagger$ apply only to ThreadGate and its ablations.}\n\\label{tab:hyperparams}\n\\begin{tabular}{l@{\\hspace{8pt}}l}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\nBase model & Qwen-2.5-7B-Instruct \\\\\nLoRA rank / $\\alpha$ & 16 / 32 \\\\\nLoRA targets & \\texttt{q\\_proj}, \\texttt{v\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1$\\!=\\!0.9, $\\beta_2$\\!=\\!0.999) \\\\\nLearning rate & $2 \\times 10^{-4}$ \\\\\nGate LR mult.$^\\dagger$ & $10\\times$ \\\\\nBatch / grad accum & 1 / 8 (eff.\\ 8) \\\\\nEpochs & 3 \\\\\nMax seq length & 2048 \\\\\nTraining data & 8K UltraChat convs \\\\\nSeed & 42 (+123 for TG, SS) \\\\\n$\\lambda_\\text{GAR}$/$\\lambda_\\text{div}$ & 1.0 / 1.0 \\\\\nGAR target $\\tau$ & 0.5 \\\\\nGate init bias$^\\dagger$ & 1.5 ($\\sigma\\!\\approx\\!0.82$) \\\\\nGate hidden dim$^\\dagger$ & 64 \\\\\nTurn embed dim$^\\dagger$ & 16 \\\\\nGPU & RTX PRO 6000 (96\\,GB) \\\\\nTraining time & 6--8 h / variant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Loss Formulation Search}\\label{sec:appendix-loss}\n\nThe final MSE + gate diversity loss (\\S\\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.\n\n\\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.\n\n\\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\\text{mean}(\\text{GAR})$). The unbounded objective rewards full pass-through ($g \\to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\\lambda$=2 (v3), gates froze within 100 steps; at $\\lambda$=10 (v3b), convergence to identity accelerated; at $\\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.\n\n\\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.\n\n\\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\\tau$ incurs the same penalty as GAR below $\\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\\mathcal{L}_\\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).\n\n\\begin{table*}[t]\n\\centering\\footnotesize\n\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}\n\\label{tab:loss-iterations}\n\\begin{tabular}{l l l p{5.8cm} c c}\n\\toprule\n & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{Failure Mechanism} & \\textbf{GAR} & \\textbf{PPL} \\\\\n\\midrule\nv1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\\\\nv2  & Cumulative + $\\varepsilon$ & \\texttimes~same trajectory & Numerical instability from cumulative product; $\\varepsilon$-stabilization insufficient & ---  & ---  \\\\\nv3  & Maximize ($\\lambda$=2)  & \\texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\\\\nv3b & Maximize ($\\lambda$=10) & \\texttimes~identity collapse   & Higher $\\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\\\\nv5  & Maximize ($\\lambda$=1)  & \\texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\\\\nv6  & Smooth saturation       & \\texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\\\\nv7  & MSE + gate div          & \\checkmark~\\textbf{converged}  & \\textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Instruction Retention Details}\\label{sec:appendix-ir}\n\nTo evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\\beta$\\,=\\,3 steering on $N$\\,=\\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.\n\n\\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\\,=\\,54 paired evaluations (18 types $\\times$ 3 conversations per type) for the McNemar analysis.\n\n\\paragraph{Per-category results.} Table~\\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.\n\n\\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\\,=\\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.\n\nFigure~\\ref{fig:ir-bar} visualizes the per-category breakdown.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_instruction_retention.pdf}\n  \\caption{Instruction retention by constraint category under $\\beta$\\,=\\,3 steering. Content constraints benefit most (+23.8\\,pp); format and count constraints are unaffected.}\n  \\label{fig:ir-bar}\n\\end{figure}\n\n\\FloatBarrier\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Instruction retention by constraint category ($\\beta$\\,=\\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}\n\\label{tab:ir-results}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\Delta$ \\\\\n\\midrule\nContent    & 61.9\\% & 85.7\\% & +23.8\\,pp \\\\\nPosition   & 66.7\\% & 73.3\\% & +6.7\\,pp \\\\\nCount      & 100\\%  & 100\\%  & 0 \\\\\nFormat     & 100\\%  & 100\\%  & 0 \\\\\n\\midrule\n\\textbf{Overall} & 75.9\\% & 87.0\\% & +11.1\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Long-Conversation AR Evaluation}\\label{sec:appendix-n5}\n\nThe main results (Table~\\ref{tab:five-way}) report AR GAR from $N$\\,=\\,50 held-out conversations with a mean of 3.6 user turns. Table~\\ref{tab:n5-ar} presents complementary results on $N$\\,=\\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.\n\n\\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\\times$ (0.064 vs.\\ 0.037 in the $N$\\,=\\,50 evaluation) to 0.64$\\times$ (0.016 vs.\\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\\,=\\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.\n\n\\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\\times$ of the base model's GAR, compared to 3.4$\\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.\n\n\\paragraph{Caveats.} The $N$\\,=\\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{AR GAR-ours on $N$\\,=\\,5 ten-turn conversations. The gating advantage observed in Table~\\ref{tab:five-way} ($N$\\,=\\,50, mean 3.6 turns) diminishes with conversation length.}\n\\label{tab:n5-ar}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AR GAR-O} & \\textbf{$\\Delta$ vs.\\ Table~\\ref{tab:five-way}} \\\\\n\\midrule\nBase & 0.012 & $-$0.007 \\\\\n\\midrule\nThreadGate & 0.016 & $-$0.048 \\\\\n\\;+\\,PCGrad & 0.015 & $-$0.015 \\\\\nUniform Gate & 0.015 & $-$0.018 \\\\\nLoRA-only & 0.025 & $-$0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Statistical Test Details}\\label{sec:appendix-stats}\n\nAll statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\\ref{tab:stat-tests} consolidates the full results.\n\n\\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\\ LoRA-only comparison ($p$\\,=\\,0.004, $r$\\,=\\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\\ +PCGrad comparison ($p$\\,=\\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.\n\n\\paragraph{Bootstrap confidence intervals.} The 95\\% CIs in Table~\\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.\n\n\\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \\sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \\leq r < 0.5$ is medium, and $r \\geq 0.5$ is large. The TG vs.\\ LoRA-only effect ($r$\\,=\\,0.454) is medium, and TG vs.\\ Base ($r$\\,=\\,0.802) is large.\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \\leq 0.004$) survive this correction.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Consolidated statistical tests. All AR comparisons use $N$\\,=\\,50 conversations (39 with $\\geq$3 turns); gate conditioning uses 28 layers.}\n\\label{tab:stat-tests}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Test} & $p$ & $r$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{AR GAR-ours ($\\beta$\\,=\\,0)}} \\\\\nTG vs.\\ Base & Wilcoxon & $<$0.001 & 0.802 \\\\\nTG vs.\\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\\\\nTG vs.\\ +PCGrad & Wilcoxon & 0.002 & --- \\\\\nSS vs.\\ TG & Wilcoxon & $<$0.001 & 0.869 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Gate conditioning (28 layers)}} \\\\\nTurn 1 vs.\\ Turn 21 & Wilcoxon & $3.7\\!\\times\\!10^{-8}$ & 0.975 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Instruction retention}} \\\\\n$\\beta$\\,=\\,0 vs.\\ $\\beta$\\,=\\,3 & McNemar & 0.077 & --- \\\\\nGAR--compliance & Pearson & 0.007 & 0.200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Llama-3.1-8B Complete Results}\\label{sec:appendix-llama}\n\nTable~\\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \\S\\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.\n\n\\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\\ 0.50).\n\n\\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\\,=\\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\\% for ThreadGate (mean 0.043, std 0.100), and 5\\% of turn-level measurements exhibit sporadic attention spikes (GAR $\\geq$ 0.4). We therefore report both mean and median.\n\n\\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\\times$ by median for Llama vs.\\ 8--17$\\times$ for Qwen).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\\,=\\,50); AR: autoregressive ($N$\\,=\\,20 for Base/TG/LoRA-only, $N$\\,=\\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}\n\\label{tab:llama-full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{TF}} & \\multicolumn{2}{c}{\\textbf{AR}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\\\\n\\midrule\nBase & 0.017 & 3.45 & 0.009 & 0.009 \\\\\nThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\\\\nLoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\\\\n\\textbf{SS} & 0.477 & 2.82 & \\textbf{0.166} & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\FloatBarrier\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_crossmodel.pdf}\n  \\caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\\times$ by median), exceeding Qwen's 8$\\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}\n  \\label{fig:crossmodel}\n\\end{figure}\n\n\\paragraph{Cross-model summary.} Table~\\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\\approx$ 0.5, AR GAR $\\ll$ 0.1, gap $\\geq$ 7.9$\\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\\times$ by median for TG; mean-based range 11.2--17.2$\\times$) compared to Qwen's (7.9--13.5$\\times$) may reflect its deeper architecture (32 vs.\\ 28 layers), which allows more layers for distributional drift to compound through.\n\n\\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}\n\n\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\n\n\\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\\% longer than Qwen due to Llama's larger layer count (32 vs.\\ 28 layers).\n\n\\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\\% decline. This is steeper than Qwen's 70.8\\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\\ 28 KV heads).\n\n\\paragraph{Cross-model gradient analysis.} Table~\\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\\approx$\\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\\times$ on Qwen and 25.7$\\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \\emph{modus tollens} argument (\\S\\ref{subsec:pcgrad}): gradient direction conflict is not the primary cause of the TF-AR gap.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\\times$.}\n\\label{tab:gradient-crossmodel}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\\n\\midrule\nMean cos sim & $-$0.042 & +0.005 \\\\\nNeg-layer \\% & 67.9\\% & 53.1\\% \\\\\nNTP/GAR mag ratio & 14.7$\\times$ & 25.7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Additional Visualizations}\\label{sec:appendix-viz}\n\nThis section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.\n\n\\subsection{Gate Profile Heatmap}\n\nFigure~\\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_profile_heatmap.pdf}\n\\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\\times$ 5 conditions) and Llama-3.1-8B (32 layers $\\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}\n\\label{fig:gate-heatmap}\n\\end{figure}\n\n\\subsection{Cross-Model Gate Profile Comparison}\n\nFigure~\\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_profile_crossmodel.pdf}\n\\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}\n\\label{fig:gate-crossmodel}\n\\end{figure}\n\n\\subsection{Per-Turn AR GAR Decay}\n\nFigure~\\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\\% from turn 1 to turn 10; Llama base drops 90\\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\\ref{tab:five-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_ar_gar_perturn.pdf}\n\\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\\% (turn 1$\\to$10), Llama base drops 90\\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}\n\\label{fig:ar-gar-perturn}\n\\end{figure}\n\n\\subsection{Bootstrap Confidence Intervals}\n\nFigure~\\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\\% CIs reported in Table~\\ref{tab:five-way}.\n\n\\begin{figure}[H]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_bootstrap_ci.pdf}\n  \\caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\\ LoRA-only, $N$\\,=\\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\\,=\\,0.454).}\n  \\label{fig:bootstrap-ci}\n\\end{figure}\n\n\\subsection{Gate Value Distributions}\n\nFigure~\\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_distribution.pdf}\n\\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}\n\\label{fig:gate-distribution}\n\\end{figure}\n\n\\subsection{Training Loss Curves}\n\nFigure~\\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_training_loss_curves.pdf}\n\\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}\n\\label{fig:training-loss}\n\\end{figure}\n\n\\subsection{Full Attention Steering Results}\\label{sec:appendix-steering}\n\n\\begin{table*}[t]\n\\centering\\small\n\\caption{Full attention steering results across evaluation settings.\n\\textbf{Bold} indicates the operating point cited in the main text ($\\beta$\\,=\\,5).\nA visual gap separates the phase-transition boundary: GAR jumps sharply between $\\beta$\\,=\\,2 and $\\beta$\\,=\\,3 across all settings.}\n\\label{tab:steering-full}\n\\begin{tabular}{r cc cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,5, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,50, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,200, TF}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n$\\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\\\\n\\midrule\n0   & .028 & 1.41 & $.064 \\pm .081$ & $1.43 \\pm .10$ & .535 & 2.62 \\\\\n0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\\\\n1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\\\\n2   & .062 & 1.41 & $.128 \\pm .110$ & $1.48 \\pm .14$ & .611 & 2.69 \\\\\n\\addlinespace[3pt]\n3   & ---  & ---  & $.556 \\pm .060$ & $1.56 \\pm .17$ & .788 & 2.93 \\\\\n4   & ---  & ---  & $.644 \\pm .061$ & $1.67 \\pm .22$ & .817 & 3.49 \\\\\n\\textbf{5}  & \\textbf{.680} & \\textbf{1.91} & $\\mathbf{.727 \\pm .061}$ & $\\mathbf{1.77 \\pm .27}$ & \\textbf{.833} & \\textbf{6.15} \\\\\n10  & .959 & 4.22 & $.961 \\pm .015$ & $3.45 \\pm 1.78$ & .977 & 505.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_steering_standalone.pdf}\n  \\caption{Detailed $\\beta$-steering trade-off ($N$\\,=\\,50). GAR-ours (top) increases monotonically with $\\beta$; PPL (bottom) remains stable below $\\beta$\\,=\\,3 (9\\% cost), then rises sharply. The $\\beta$\\,=\\,3 operating point (circled) achieves 8.7$\\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}\n  \\label{fig:steering-standalone}\n\\end{figure}\n\n\\section{Per-Layer Gate Profile}\\label{sec:appendix-gate-profile}\n\nTable~\\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\\sigma$\\,=\\,0.051).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}\n\\label{tab:gate-profile}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cccccccc}\n\\toprule\nL0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\\\\n.883 & \\textbf{.793} & .996 & .988 & .984 & \\textbf{.797} & .961 & .918 \\\\\n\\midrule\nL8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\\\\n.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\\\\n\\midrule\nL16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\\\\n.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\\\\n\\midrule\nL24 & L25 & L26 & L27 & \\multicolumn{4}{c}{Summary} \\\\\n.980 & .984 & .988 & 1.00 & \\multicolumn{4}{c}{$\\bar{g}$\\,=\\,.947, $\\sigma$\\,=\\,.051} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.\n\n\\paragraph{Cross-model comparison.} See \\S\\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.\n\n\\section{Scheduled Sampling Implementation}\\label{sec:appendix-ss}\n\nOur scheduled sampling implementation follows \\citet{bengio2015scheduled} with modifications for multi-turn transformer training:\n\n\\paragraph{Sampling schedule.} The model-generated context ratio $\\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\\%) is lower than the nominal schedule due to per-sample Bernoulli variance.\n\n\\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.\n\n\\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\\ 0.947, min at L4 vs.\\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_training_dynamics.pdf}\n  \\caption{Scheduled sampling training dynamics: sampling ratio $\\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}\n  \\label{fig:ss-dynamics}\n\\end{figure}\n\n\\section{Computational Cost Analysis}\\label{sec:appendix-cost}\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\\,GB VRAM). VRAM reports peak allocated memory (excluding optimizer states).}\n\\label{tab:cost}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Params} & \\textbf{Time (h)} & \\textbf{VRAM} & \\textbf{Overhead} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Qwen-2.5-7B-Instruct}} \\\\\nLoRA-only & 4.2M & 5.7 & 42\\,GB & baseline \\\\\nThreadGate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\n\\;+\\,PCGrad & 4.3M & 8.0 & 43\\,GB & $+$33\\% \\\\\nUniform Gate & 4.3M & 6.1 & 43\\,GB & $+$57K \\\\\nSS (s42) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\nSS (s123) & 4.3M & 10.8 & 43\\,GB & $+$80\\% \\\\\nSS (s456) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Llama-3.1-8B-Instruct}} \\\\\nLoRA-only & 4.2M & 7.0 & 45\\,GB & baseline \\\\\nThreadGate & 4.3M & 7.3 & 46\\,GB & $+$65K \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Parameter overhead.} ThreadGate adds ${\\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\\times$ 2K per gate MLP) and ${\\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.\n\n\\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 5.7--7.3 hours. PCGrad adds ${\\sim}$33\\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\\% (6.5h) due to efficient batched generation, while seed 123 adds 80\\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.\n\n\\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\\to$64$\\to$1 MLP forward pass per layer adds $<$0.1\\% latency. $\\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.\n\n\\section{Qualitative Steering Examples}\\label{sec:appendix-examples}\n\nTable~\\ref{tab:examples} illustrates the effect of $\\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''\n\n\\begin{table*}[t]\n\\centering\\small\n\\caption{Qualitative effect of $\\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}\n\\label{tab:examples}\n\\begin{tabular}{c p{5.5cm} p{5.5cm}}\n\\toprule\n\\textbf{Turn} & \\textbf{$\\beta$\\,=\\,0 (unsteered)} & \\textbf{$\\beta$\\,=\\,3 (steered)} \\\\\n\\midrule\n1 & \\checkmark~Three bullet points, on-topic & \\checkmark~Three bullet points, on-topic \\\\\n2 & \\checkmark~Three bullet points, relevant & \\checkmark~Three bullet points, relevant \\\\\n3 & $\\sim$~Four bullet points, partially on-topic & \\checkmark~Three bullet points, on-topic \\\\\n4 & \\texttimes~Free-form paragraph, no bullets & \\checkmark~Three bullet points, on-topic \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe pattern is consistent with the GAR decay analysis (\\S\\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\\ref{tab:ir-results} shows that content constraints benefit most from this effect.\n\n\\section{Gradient Conflict Analysis}\\label{sec:appendix-gradient}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth,height=0.42\\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}\n  \\caption{(a)~Training GAR convergence to target ($\\tau$\\,=\\,0.5). (b)~PCGrad removes gradient conflict but $\\mathcal{L}_\\text{GAR}$ still collapses, confirming that gradient direction conflict is not the primary cause (\\S\\ref{subsec:pcgrad}).}\n  \\label{fig:training-pcgrad}\n\\end{figure}\n\nThis section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \\S\\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.\n\n\\paragraph{Gradient direction analysis.} Figure~\\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate and PCGrad training. Under standard training, 79\\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\\%$\\to$71\\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.\n\n\\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\\rho$\\,=\\,$-$0.12, $p$\\,=\\,0.54 between gate value and conflict magnitude).\n\n\\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\\times$ at epoch~0 and 14.7$\\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\\% of the effective update magnitude, explaining why PCGrad is ineffective.\n\n\\paragraph{Cross-model consistency.} Table~\\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \\textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient direction conflict is not the primary cause.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gradient_conflict_heatmap.pdf}\n\\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\\% to 68\\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\\%$\\to$71\\%) but does not improve AR GAR, ruling out gradient direction conflict as the primary cause (\\S\\ref{subsec:pcgrad}).}\n\\label{fig:gradient-heatmap}\n\\end{figure*}\n\n\\section{Training Data Characteristics}\\label{sec:appendix-data}\n\nAll experiments use 8,000 multi-turn conversations sampled from the UltraChat \\citep{ding2023ultrachat} training split. Table~\\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\\,=\\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\\,=\\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\\ref{sec:appendix-n5}).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Training and evaluation data characteristics. All data from UltraChat \\citep{ding2023ultrachat}.}\n\\label{tab:data-stats}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Property} & \\textbf{Train} & \\textbf{Eval (primary)} \\\\\n\\midrule\nConversations & 8,000 & 50 \\\\\nMin user turns & 3 & 3 \\\\\nMax sequence length & 2,048 & 2,048 \\\\\nSource & UltraChat train & UltraChat train \\\\\nOverlap & --- & non-overlapping \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Exposure Bias Scaling}\\label{sec:appendix-eb-scaling}\n\nFigure~\\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).\n\n\\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.9$\\times$) while PCGrad shows the largest (16.7$\\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\\sim}$1.2$\\times$, the only variant approaching parity. The ordering of gap ratios (SS $\\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\\sim$27$\\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\\ 28 layers), which provides more layers for distributional drift to compound through.\n\n\\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\\,=\\,50), ThreadGate's gap is 8$\\times$; at 10 turns ($N$\\,=\\,5), it widens to 31$\\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.\n\n\\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\\sim}$1.2$\\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\\ref{sec:appendix-steering-viz}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_eb_scaling.pdf}\n\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}\n\\label{fig:eb-scaling}\n\\end{figure}\n\n\\section{Per-Turn AR GAR Dynamics}\\label{sec:appendix-ar-gar-dynamics}\n\nTo characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.\n\nAll six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\\S\\ref{subsec:ss}).}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_curves.pdf}\n\\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}\n\\label{fig:kl_ar_gar_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_bar.pdf}\n\\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}\n\\label{fig:kl_ar_gar_bar}\n\\end{figure}\n\nThis pattern contrasts with teacher-forced evaluation, where GAR remains relatively stable across turns for all configurations. Under teacher forcing, the model conditions on ground-truth context at each turn, preventing the distributional drift that causes GAR erosion in AR mode. The divergence between TF stability and AR decay provides turn-level evidence for the exposure bias mechanism described in \\S\\ref{sec:analysis}: training-time attention patterns are optimized for a distribution that AR generation progressively departs from.\n\n\\section{Per-Head KL Divergence Analysis}\\label{sec:appendix-kl}\n\nTo test whether exposure bias selectively disrupts goal-attending heads rather than uniformly affecting all attention patterns, we compute per-head TF vs.\\ AR attention divergence on 30 held-out conversations. For each of the 28 attention heads per layer (784 heads total), we measure the KL divergence $D_\\text{KL}(p_\\text{TF} \\| p_\\text{AR})$ between teacher-forced and autoregressive attention distributions, and the absolute GAR shift $\\Delta\\text{GAR} = |\\text{GAR}_\\text{TF} - \\text{GAR}_\\text{AR}|$. This head-level analysis provides diagnostic evidence for the exposure bias interpretation beyond the aggregate TF-AR gap.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Per-head TF-AR divergence statistics for Base and ThreadGate (Qwen-2.5-7B, 30 conversations). TG trains more concentrated goal attention under TF, but these high-GAR heads shift most under AR ($r$\\,=\\,0.743).}\n\\label{tab:kl-perhead}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Base} & \\textbf{TG} \\\\\n\\midrule\nMean $\\Delta$GAR & 0.012 & 0.016 \\\\\nMean KL & 0.043 & 0.054 \\\\\nCorr(TF\\_GAR, $\\Delta$GAR) & 0.673 & 0.743 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selective disruption.} ThreadGate exhibits 35\\% larger mean $\\Delta$GAR (0.016 vs.\\ 0.012) and 26\\% larger mean KL (0.054 vs.\\ 0.043) than Base. This is counterintuitive: the auxiliary GAR loss successfully trains more concentrated goal attention (higher TF GAR per head), but these very same heads shift more under AR generation. The correlation between per-head TF GAR and $\\Delta$GAR is strong for both models ($r$\\,=\\,0.673 for Base, 0.743 for TG), confirming that heads with higher goal attention under teacher forcing are disproportionately disrupted under autoregressive generation. This selectivity is a hallmark of exposure bias: the training-time optimization succeeds at creating a specific attention pattern (concentrated goal attention), but precisely this pattern has no autoregressive counterpart because it depends on conditioning on ground-truth context.\n\n\\paragraph{Layer-depth dependence.} The highest-KL heads concentrate at output-adjacent layers (L23--L27, KL\\,$>$\\,0.077) and L9 (KL\\,$\\approx$\\,0.068). Output-adjacent layers participate most directly in next-token prediction, so their attention distributions are most sensitive to changes in the conditioning context. L9's elevated KL may reflect a ``routing layer'' phenomenon observed in multi-layer transformers, where specific intermediate layers specialize in long-range information routing. The depth dependence is consistent with cumulative error propagation: distributional drift from model-generated tokens accumulates as information flows through successive layers, producing the largest attention shifts at the deepest layers.\n\n\\paragraph{Gate--KL independence.} Gate magnitude does not predict per-layer exposure bias severity: Spearman correlation between gate value and per-layer KL is 0.061 ($p$\\,=\\,0.757). The highest KL values concentrate at deep layers (L22--L27) where gates are near identity ($\\approx$1.0), while the lowest-gate layers show below-average KL (0.041 vs.\\ 0.056 for highest-gate layers). This independence confirms that the gating mechanism and the exposure bias phenomenon operate on different axes: gates modulate the magnitude of residual contributions, while exposure bias disrupts the direction (attention distribution) of those contributions. Even a ``perfect'' gate that could fully attenuate certain layers' residuals would not address the fundamental distributional mismatch that causes the attention shift.\n\n\\section{GAR Definition Robustness}\\label{sec:appendix-gar-robust}\n\nTo assess whether our conclusions depend on the specific GAR definition, we evaluate four alternative token-position variants on 50 held-out conversations (Table~\\ref{tab:gar-robust}): (1)~\\emph{ours} (last-token): attention from the last token to goal tokens (standard GAR-ours); (2)~\\emph{all-token}: average attention from all tokens to goal tokens; (3)~\\emph{first-token}: attention from the first assistant token to goal tokens; (4)~\\emph{goal-only}: attention from the last token to system-prompt-only tokens (excluding conversation content).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Mid-turn GAR under four alternative definitions ($N$\\,=\\,50 conversations). ThreadGate only improves query-position-specific definitions (last-token, goal-only); Scheduled Sampling raises all four definitions above 0.36.}\n\\label{tab:gar-robust}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Definition} & \\textbf{Base} & \\textbf{TG} & \\textbf{SS} \\\\\n\\midrule\nOurs (last-token) & 0.015 & \\textbf{0.325} & \\textbf{0.458} \\\\\nAll-token & 0.015 & 0.025 & \\textbf{0.366} \\\\\nFirst-token & 0.022 & 0.039 & \\textbf{0.412} \\\\\nGoal-only & 0.005 & \\textbf{0.310} & \\textbf{0.444} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThreadGate improvements are query-position-specific: the two definitions using the last token as query (ours: $0.015 \\to 0.325$; goal-only: $0.005 \\to 0.310$) show large gains, while all-token ($0.025$) and first-token ($0.039$) remain near base levels. This is expected: the GAR loss optimizes attention at the last-token position, so the learned routing does not generalize to other query positions.\n\nScheduled Sampling raises all four definitions above 0.36, with no definition falling below Base-relative gains. This confirms that SS builds a broad goal-attention pattern across token positions, rather than overfitting to the specific position targeted by the GAR loss. The pattern holds regardless of GAR definition: both the exposure bias diagnosis and the SS mitigation are robust to metric choice.\n\n\\section{General Capability Preservation (MMLU)}\\label{sec:appendix-mmlu}\n\nTo confirm that auxiliary GAR losses and attention steering do not degrade general language understanding, we evaluate all six Qwen-2.5-7B variants on MMLU 5-shot \\citep{hendrycks2021measuring} ($N$\\,=\\,14{,}042 questions).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\\,pp of the base LoRA-only checkpoint.}\n\\label{tab:mmlu}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{Acc (\\%)} & \\textbf{$\\Delta$ vs Base} \\\\\n\\midrule\nBase (pretrained) & 74.23 & --- \\\\\nPCGrad & 73.86 & $-$0.38 \\\\\nSS & 73.75 & $-$0.48 \\\\\nLoRA-only & 73.57 & $-$0.66 \\\\\nThreadGate & 73.47 & $-$0.77 \\\\\nUniform Gate & 73.46 & $-$0.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll variants degrade by $<$0.8\\,pp, confirming that attention steering and auxiliary GAR losses do not harm general language understanding. The ordering does not track GAR performance (e.g., PCGrad shows the smallest MMLU drop despite the worst AR GAR), consistent with GAR and NTP occupying largely orthogonal subspaces.\n\n\\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b}\n\nWe validate cross-scale on Qwen-2.5-1.5B-Instruct to test whether goal attention decay and $\\beta$-steering generalize to smaller models.\n\n\\paragraph{Phase~1 GAR decay.} The 1.5B base model exhibits 79.8\\% GAR decline from turn~1 to mid-turns (vs.\\ 70.8\\% on 7B), confirming that attention decay is present across scales and is more severe at smaller model sizes.\n\n\\paragraph{Steering evaluation.} Table~\\ref{tab:1.5b-steering} reports AR evaluation ($N$\\,=\\,50). We report median PPL because Base $\\beta$\\,=\\,3 contains a catastrophic outlier (conversation~\\#11, PPL\\,$>$\\,$10^8$) that inflates the mean.\\footnote{The outlier occurs in a single conversation where $\\beta$-steering causes the base model to enter a degenerate repetition loop. ThreadGate produces zero such outliers across all $\\beta$ values, suggesting the gate provides stability against catastrophic steering failures.}\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Cross-scale $\\beta$-steering on Qwen-2.5-1.5B ($N$\\,=\\,50, AR). PPL is median due to catastrophic Base outlier at $\\beta$\\,=\\,3. TG eliminates outliers across all $\\beta$ values.}\n\\label{tab:1.5b-steering}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Model} & $\\beta$ & \\textbf{AR GAR} & \\textbf{PPL (med)} \\\\\n\\midrule\nBase & 0 & 0.017 & 1.909 \\\\\nTG & 0 & 0.023 & 1.897 \\\\\n\\midrule\nBase & 3 & 0.120 & 2.216 \\\\\nTG & 3 & 0.114 & 1.975 \\\\\n\\midrule\nBase & 5 & 0.657 & 2.804 \\\\\nTG & 5 & 0.715 & 2.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe steering pattern mirrors the 7B results: $\\beta$\\,=\\,5 recovers GAR to 0.657--0.715 ($p < 0.001$), confirming that attention misallocation is the proximal cause of GAR collapse across scales. At $\\beta$\\,=\\,0, TG shows a small but significant GAR advantage ($p$\\,=\\,0.005); at $\\beta$\\,=\\,3, the TG--Base difference is not statistically significant ($p$\\,=\\,0.815), unlike the 7B pattern where TG consistently outperforms Base. This scale-specific difference may reflect the 1.5B model's limited capacity to maintain learned routing at intermediate steering strengths. ThreadGate does provide a stability advantage---zero catastrophic PPL outliers vs.\\ one in Base---suggesting that residual gating regularizes attention distributions even when aggregate GAR is comparable.\n\n\\section{Per-Seed Detailed Results}\\label{sec:appendix-perseed}\n\nTables~\\ref{tab:perseed-ss} and~\\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.\n\n\\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\\pm0.032$ across seeds under the held-out protocol (Table~\\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\\,=\\,200 sample. AR GAR shows meaningful variance (std\\,=\\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\\times$), seed 123 is intermediate (0.423, gap 1.3$\\times$), and seed 456 is highest (0.433, gap 1.2$\\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\\beta$\\,=\\,5, the cross-seed variance nearly vanishes ($0.717\\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.\n\n\\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\\pm0.001$) and similar AR GAR (0.064 vs.\\ 0.055), with gap ratios of 7.9$\\times$ and 9.1$\\times$ respectively. The 15\\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.\n\n\\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\\% overhead) vs.\\ 6.5 hours for seeds 42 and 456 (8\\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-generated contexts: seed 123 happens to trigger longer autoregressive generation episodes early in training, where the model produces longer outputs before hitting the max-length cutoff. Despite this training-time variance, all three seeds converge to similar final metrics, suggesting the optimization landscape is robust.\n\n\\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}\n\n\\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}\n\n\\section{Per-Turn GAR Decay Analysis}\\label{sec:appendix-perturn-detail}\n\nTables~\\ref{tab:perturn-qwen} and~\\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\\ref{tab:five-way}).\n\n\\paragraph{Qwen per-turn dynamics.} On Qwen (Table~\\ref{tab:perturn-qwen}), all non-SS variants show rapid monotonic decay: turn-1 GAR ranges from 0.085 (Base) to 0.130 (ThreadGate), but by turn~5 all collapse below 0.07. The decay rate is approximately exponential for the first 3 turns, then plateaus near a floor value that varies by configuration (Base: 0.004, ThreadGate: 0.043--0.066, LoRA-only: 0.040). ThreadGate and LoRA-only show occasional turn-level fluctuations (e.g., TG turn~5 = 0.066 $>$ turn~4 = 0.043), which reflect stochastic variation in individual conversations rather than systematic recovery. Scheduled sampling retains substantially higher GAR throughout (turn-5 GAR\\,=\\,0.365 vs.\\ 0.066 for ThreadGate), with a much flatter decay profile (15\\% decline from turn~1 to turn~5 vs.\\ 49\\% for ThreadGate). This flatter profile is the signature of distributional robustification: SS-trained models encounter model-generated context during training, so the attention patterns are calibrated for the distribution they actually face during inference.\n\n\\paragraph{Llama per-turn dynamics.} On Llama (Table~\\ref{tab:perturn-llama}), the decay is steeper: Base GAR drops from 0.028 to 0.008 over 4 turns (71\\% decline in the $N$\\,=\\,20 evaluation), and from 0.026 to 0.003 over 10 turns (88\\% decline in the $N$\\,=\\,5 long-conversation evaluation). ThreadGate on Llama shows a distinctive pattern: turn-level GAR is roughly constant (0.038--0.049) rather than monotonically declining, suggesting that the gating mechanism maintains a stable floor on Llama that it fails to maintain on Qwen. However, this floor (0.04) is still an order of magnitude below the TF target (0.484), confirming that the fundamental TF-AR gap persists.\n\n\\paragraph{Cross-architecture comparison.} The per-turn decay profiles reveal an architectural difference: Qwen shows a sharper initial decline (turn~1 to turn~2: $-$62\\% for Base) followed by a plateau, while Llama shows a more gradual and sustained decline throughout. This difference may reflect the two architectures' different attention head configurations and layer counts, but the qualitative pattern---monotonic or near-monotonic decline toward a near-zero floor---is universal.\n\nFigures~\\ref{fig:perturn-qwen-detail} and~\\ref{fig:perturn-llama-detail} visualize these trajectories.\n\n\\input{../artifacts/appendix_expansion/tab_perturn_qwen.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_perturn_qwen_detail.pdf}\n  \\caption{Per-turn AR GAR-ours across six Qwen-2.5-7B configurations. Scheduled sampling (green) retains far higher GAR than all other variants, which cluster below 0.13 and decay rapidly.}\n  \\label{fig:perturn-qwen-detail}\n\\end{figure}\n\n\\input{../artifacts/appendix_expansion/tab_perturn_llama.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_perturn_llama_detail.pdf}\n  \\caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\\,=\\,20, 4 turns). (b)~Extended Base decay profile ($N$\\,=\\,5, 10 turns), showing 90\\% decline.}\n  \\label{fig:perturn-llama-detail}\n\\end{figure}\n\n\\section{Extended Dataset Statistics}\\label{sec:appendix-dataset-ext}\n\nTable~\\ref{tab:dataset_stats} provides detailed statistics for the UltraChat training and evaluation splits. From the full UltraChat-200K corpus (207,865 conversations in the \\texttt{train\\_sft} split), we filter for conversations with $\\geq$5 assistant turns, yielding 17,302 candidates (8.3\\% of the full corpus). We randomly sample 8,000 for training, 50 for primary AR evaluation (mean 3.6 user turns), 50 for IID GAR diagnostics, and 200 for the instruction retention evaluation.\n\n\\paragraph{Filtering rationale.} The $\\geq$5 assistant turns threshold was chosen empirically: conversations with fewer than 3 assistant turns do not exhibit measurable attention decay (turn-1 to turn-3 GAR decline $<$5\\%), making them uninformative for studying multi-turn exposure bias. The 5-turn threshold provides sufficient turn depth while retaining a reasonable fraction of the corpus. The average conversation in the filtered set contains 5.6 assistant turns (range: 5--7), with a mean sequence length of 1,247 tokens after tokenization with the Qwen-2.5 tokenizer.\n\n\\paragraph{Evaluation split design.} We maintain four non-overlapping evaluation sets to avoid contamination: (1)~the primary AR evaluation ($N$\\,=\\,50) uses the same conversation structure as training but with held-out conversations, enabling direct comparison of TF vs.\\ AR behavior; (2)~the IID GAR diagnostic ($N$\\,=\\,50) uses a separate sample for ablation studies that require independent measurements; (3)~the large instruction retention set ($N$\\,=\\,200) provides sufficient statistical power for per-category compliance analysis across 18 constraint types; (4)~the long-conversation set ($N$\\,=\\,5, 10 turns each) tests scaling behavior beyond the training distribution.\n\n\\paragraph{Domain diversity.} UltraChat covers a broad range of conversational topics including knowledge Q\\&A, creative writing, reasoning, and open-ended discussion. We do not stratify by topic, as our focus is on the architectural mechanism (attention routing) rather than domain-specific performance. The topic diversity serves as implicit regularization against overfitting to specific conversation patterns.\n\n\\input{../artifacts/appendix_expansion/tab_dataset_stats.tex}\n\n\\section{Extended GAR Robustness Analysis}\\label{sec:appendix-gar-ext}\n\nTable~\\ref{tab:gar_robustness} and Figure~\\ref{fig:gar-robust-grouped} extend the GAR robustness analysis from \\S\\ref{sec:appendix-gar-robust} with turn-1 GAR and gap ratio metrics across all four token-position variants. We evaluate four ways to select the query token position for gradient attribution: (1)~\\textit{Last} (our default): the final token of each assistant turn, which captures the model's ``summary'' attention pattern at the prediction boundary; (2)~\\textit{All}: the mean over all assistant tokens, providing a position-averaged view; (3)~\\textit{First}: the first assistant token, which reflects initial attention allocation; (4)~\\textit{Goal-only}: attention to goal tokens as defined by \\citet{dongre2026attention}, which restricts the target set to system-prompt tokens.\n\n\\paragraph{Position-specific vs.\\ broad improvement.} The key finding is a clear dichotomy between ThreadGate and Scheduled Sampling. ThreadGate improvements are restricted to last-token and goal-only positions (the two definitions sharing the query position targeted by the GAR loss): gap ratios drop to 1.21$\\times$ and 1.07$\\times$ respectively. All-token (5.04$\\times$) and first-token (8.24$\\times$) GAR remain near base levels, confirming that the learned routing is position-specific. Scheduled Sampling raises all four definitions above 0.36 with gap ratios $\\leq$1.83$\\times$, demonstrating that distributional robustification builds broad goal attention across token positions rather than overfitting to the position targeted by the loss.\n\n\\paragraph{Turn-1 vs.\\ mid-turn dynamics.} Turn-1 GAR is consistently higher than mid-turn GAR across all definitions and conditions, reflecting the first turn's proximity to the ground-truth prefix in training. The gap ratio quantifies how much of this initial attention survives into later turns. First-token GAR shows the largest gap ratios (Base: 13.3$\\times$, TG: 8.2$\\times$), indicating that the first-token position is most vulnerable to distributional drift---the initial token's attention pattern is highly dependent on the conditioning context, which diverges most from training under autoregressive generation.\n\n\\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_gar_robustness_grouped.pdf}\n  \\caption{Mid-turn GAR across four token-position definitions. SS raises all four above 0.36; TG only improves last-token and goal-only.}\n  \\label{fig:gar-robust-grouped}\n\\end{figure}\n\n\\section{MMLU Category Breakdown}\\label{sec:appendix-mmlu-ext}\n\nTable~\\ref{tab:mmlu_detail} breaks down MMLU 5-shot accuracy by category (STEM, Social Sciences, Humanities, Other) for all six Qwen-2.5-7B training configurations. This analysis addresses a potential concern: that auxiliary attention objectives might divert representational capacity from general language understanding, particularly in knowledge-intensive STEM domains.\n\n\\paragraph{Per-category analysis.} The maximum per-category degradation is 1.5\\,pp (ThreadGate on STEM), and no category shows systematic degradation across all variants. Notably, the ordering of variants differs across categories: ThreadGate shows the largest STEM drop but the smallest Humanities drop, while PCGrad shows the smallest overall drop despite having the worst AR GAR. This lack of correlation between GAR performance and MMLU degradation is consistent with GAR and NTP occupying largely orthogonal parameter subspaces---the LoRA adapter capacity (4.2M parameters) is sufficient to accommodate both objectives without interference.\n\n\\paragraph{Statistical significance.} The per-category differences are small relative to the evaluation noise: with $N$\\,=\\,14,042 questions total ($\\sim$3,500 per category), a 0.8\\,pp accuracy difference corresponds to $\\sim$28 questions, well within expected stochastic variation for 5-shot in-context learning. A chi-squared test comparing the best (PCGrad, 73.86\\%) and worst (Uniform Gate, 73.46\\%) variants yields $p$\\,=\\,0.503, confirming no significant difference. The category-level stability confirms that auxiliary GAR losses and gating do not selectively harm any knowledge domain.\n\nFigure~\\ref{fig:mmlu-comparison} visualizes the per-category comparison, showing tight clustering across all variants within each category.\n\n\\input{../artifacts/appendix_expansion/tab_mmlu_detail.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_mmlu_comparison.pdf}\n  \\caption{MMLU 5-shot accuracy by category across training configurations. All variants remain within 1.5\\,pp of the LoRA-only baseline across all categories.}\n  \\label{fig:mmlu-comparison}\n\\end{figure}\n\n\\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b-ext}\n\nTable~\\ref{tab:qwen15b_results} extends the cross-scale analysis with Phase~1 GAR diagnostics, detailed Phase~2 training results, and $\\beta$-steering evaluation on the Qwen-2.5-1.5B-Instruct model.\n\n\\paragraph{Phase 1: GAR decay.} The 1.5B base model exhibits 79.8\\% relative GAR decline from turn~1 to mid-turns, more severe than the 7B model's 70.8\\% decline. This scale-dependent decay severity is consistent with smaller models having less redundant attention capacity: with 28 layers but only 1.5B parameters (vs.\\ 7B), each layer carries proportionally more of the total representational burden, leaving less room for goal-oriented attention to persist alongside the primary NTP objective.\n\n\\paragraph{Phase 2: Training.} ThreadGate training on 1.5B converges to TF GAR-ours of 0.498 with PPL of 2.67, closely matching the 7B results (0.504 / 2.78). The gate parameter count scales linearly with layer count (identical architecture, so ${\\sim}$57K gate parameters). Training completes in 2.1 hours vs.\\ 6.0 hours for 7B, reflecting the smaller model's reduced forward/backward pass cost.\n\n\\paragraph{Steering evaluation.} At $\\beta$\\,=\\,5, ThreadGate recovers GAR to 0.715 ($p < 0.001$), closely matching the 7B result (0.727). The recovery is essentially scale-independent at the strong steering regime: the attention bias added by $\\beta$-steering overwhelms any capacity differences. At $\\beta$\\,=\\,3, the picture differs: the TG--Base difference is not statistically significant ($p$\\,=\\,0.815) on 1.5B, unlike the significant difference on 7B ($p$\\,=\\,0.039). This scale-dependent response at intermediate $\\beta$ may reflect the 1.5B model's reduced capacity for fine-grained attention routing: with fewer parameters per layer, the model cannot sustain the subtle attention reweighting that $\\beta$\\,=\\,3 attempts.\n\n\\paragraph{Catastrophic outliers.} Base 1.5B at $\\beta$\\,=\\,3 produces one catastrophic PPL outlier (conversation \\#11, PPL $> 10^8$) caused by a degenerate repetition loop. ThreadGate produces zero such outliers across all $\\beta$ values, suggesting the gate provides a stabilizing effect on attention distributions even when aggregate GAR is comparable. We report median PPL to avoid this outlier dominating the central tendency estimate.\n\n\\input{../artifacts/appendix_expansion/tab_qwen15b_results.tex}\n\n\\section{Extended Statistical Analysis}\\label{sec:appendix-stats-ext}\n\nTable~\\ref{tab:statistical_tests} consolidates all statistical tests reported in this paper, including effect sizes, 95\\% bootstrap confidence intervals, and significance levels. This section provides methodological detail beyond the summary in Appendix~\\ref{sec:appendix-stats}.\n\n\\paragraph{Test selection rationale.} All primary comparisons use paired Wilcoxon signed-rank tests on $N$\\,=\\,39 conversations (those with $\\geq$3 turns from the 50-conversation held-out set). We use non-parametric tests because per-conversation GAR distributions are heavily right-skewed (skewness $>$ 2.0 for Base and PCGrad at $\\beta$\\,=\\,0), violating normality assumptions required by parametric alternatives. The pairing structure (same conversations evaluated under different training configurations) controls for conversation-level confounds (topic difficulty, conversation length, system-prompt complexity).\n\n\\paragraph{Effect size interpretation.} Effect sizes are computed as rank-biserial correlations ($r = Z / \\sqrt{N}$), following standard practice. The largest effect is SS vs.\\ TG ($r$\\,=\\,0.869, $p < 0.001$), a large effect by conventional thresholds ($r \\geq 0.5$), confirming that scheduled sampling produces a qualitatively different outcome. The TG vs.\\ Base effect ($r$\\,=\\,0.802) is also large, while TG vs.\\ LoRA-only ($r$\\,=\\,0.454) is medium, reflecting the modest incremental benefit of gating over LoRA alone.\n\n\\paragraph{Steering dose-response pattern.} At $\\beta$\\,=\\,0, all four comparisons are significant ($p \\leq 0.004$). At $\\beta$\\,=\\,3 (the phase transition), TG vs.\\ Base becomes marginally significant ($p$\\,=\\,0.039) and SS vs.\\ TG remains significant ($p$\\,=\\,0.010), but TG vs.\\ LoRA-only and PCGrad vs.\\ TG lose significance ($p > 0.7$). At $\\beta$\\,=\\,5, no pairwise comparison reaches significance---steering dominates and equalizes all variants. This dose-response pattern confirms that the training-time variant effects are real but small relative to the inference-time steering effect.\n\n\\paragraph{Instruction retention.} The instruction retention analysis uses McNemar's test on $N$\\,=\\,54 paired constraint evaluations (18 constraint types $\\times$ 3 conversations). The marginal significance ($p$\\,=\\,0.077) reflects the small sample size rather than a null effect: the point-biserial correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is significant when treating compliance as a continuous variable, and the per-category breakdown (Table~\\ref{tab:ir-results}) shows a clear content-constraint improvement (+23.8\\,pp).\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values for the same reason described in Appendix~\\ref{sec:appendix-stats}: comparisons are hypothesis-driven (each tests a specific causal exclusion in the analysis chain), not exploratory. All reported significant results ($p \\leq 0.039$) survive Holm-Bonferroni correction for the 4 primary comparisons within each $\\beta$ level.\n\n\\input{../artifacts/appendix_expansion/tab_statistical_tests.tex}\n\n\\section{Extended Training Dynamics}\\label{sec:appendix-training-ext}\n\nFigure~\\ref{fig:training-6panel} presents the complete training loss landscape for all five Qwen-2.5-7B conditions (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Scheduled Sampling) plus the base model, showing NTP loss, GAR loss, and total loss across three epochs.\n\n\\paragraph{NTP loss convergence.} All fine-tuned variants converge to NTP loss ${\\sim}$0.93 by epoch~3, with final-epoch values ranging from 0.929 (LoRA-only) to 0.934 (ThreadGate). PCGrad shows marginally higher variance due to gradient projection, but converges to the same terminal value. The uniformity of NTP convergence across variants---including those with auxiliary losses (ThreadGate, PCGrad) and those without (LoRA-only)---confirms that the GAR auxiliary objective does not interfere with the primary language modeling task during training.\n\n\\paragraph{GAR loss dynamics.} GAR loss collapses to near-zero within the first epoch under teacher forcing across all variants, consistent with the auxiliary objective being easy to optimize when the model conditions on ground-truth context. This rapid convergence is a double-edged sword: while it confirms that the MSE formulation (v7) achieves stable optimization, the ease of convergence also means the model never learns to maintain attention under distributional drift. The scheduled sampling variant shows distinctive dynamics: higher initial GAR loss variance from stochastic context mixing, with occasional spikes when a particularly challenging model-generated context is sampled, followed by convergence to a similar final value.\n\n\\paragraph{Training-inference disconnect.} The key observation is that training-time convergence is indistinguishable across variants: an observer with access only to training curves could not predict the 5.4$\\times$ AR GAR difference between SS and TG. This disconnect reinforces the diagnosis that the failure occurs at the training-to-inference transition, not during optimization, and explains why architectural modifications (gating, PCGrad) that operate during training cannot address the fundamental distributional mismatch.\n\n\\begin{figure*}[t]\n  \\centering\n  \\includegraphics[width=0.75\\textwidth]{fig_training_curves_6panel.pdf}\n  \\caption{Training loss curves for all five Qwen conditions. NTP loss (left) converges to ${\\sim}$0.93 across variants; GAR loss (center) collapses within epoch~1; total loss (right) is NTP-dominated. Training-time behavior is indistinguishable; the failure emerges only at inference.}\n  \\label{fig:training-6panel}\n\\end{figure*}\n\n\\section{Per-$\\beta$ Steering Visualization}\\label{sec:appendix-steering-viz}\n\nFigure~\\ref{fig:steering-4panel} visualizes per-turn GAR trajectories under four steering strengths ($\\beta$\\,=\\,0, 3, 5, 10), revealing the turn-level dynamics that underlie the aggregate steering results in Table~\\ref{tab:steering-full}.\n\n\\paragraph{Unsteered baseline ($\\beta$\\,=\\,0).} GAR decays monotonically from 0.12 to 0.02 over five turns, with the steepest decline between turns~1 and~2 ($-$44\\%). This trajectory matches the per-turn profiles in Appendix~\\ref{sec:appendix-perturn-detail} and confirms that the decay is a smooth, progressive phenomenon rather than a discrete failure at a specific turn.\n\n\\paragraph{Phase transition ($\\beta$\\,=\\,3).} Turn-1 GAR jumps to ${\\sim}$0.55, but per-turn decay persists (${\\sim}$15\\% decline from turn~1 to turn~5). This indicates that steering partially compensates for the distributional drift but does not eliminate it: the attention bias adds a constant offset to goal-token logits, while the drift compounds multiplicatively across turns. The residual decay at $\\beta$\\,=\\,3 explains why this operating point shows the strongest training-variant effects in the dose-response analysis (Appendix~\\ref{sec:appendix-stats-ext}).\n\n\\paragraph{Sustained recovery ($\\beta$\\,=\\,5).} GAR is sustained above 0.6 throughout, with minimal per-turn decay ($<$5\\% decline). At this steering strength, the constant attention bias dominates the per-turn drift, effectively replacing the lost training-time signal with an inference-time substitute. The 9\\% PPL cost (1.43 $\\to$ 1.77) is modest compared to the order-of-magnitude GAR recovery.\n\n\\paragraph{Saturation regime ($\\beta$\\,=\\,10).} GAR saturates near 1.0 across all turns but PPL degrades catastrophically ($>$3.5), as the excessive attention bias distorts the attention distribution beyond the model's capacity for coherent generation. This regime is impractical and serves as an upper bound on the steering approach.\n\n\\paragraph{Operating region.} The region $\\beta \\in [3, 5]$ balances GAR recovery against PPL cost, and the per-turn profiles confirm that steering must counteract an ongoing distributional drift rather than a one-time initialization failure---a key diagnostic that distinguishes exposure bias from alternative hypotheses (e.g., capacity limitations or optimization failures).\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_steering_perturn_4panel.pdf}\n  \\caption{Per-turn GAR under four $\\beta$-steering strengths. At $\\beta$\\,=\\,0, monotonic decay; at $\\beta$\\,=\\,3, partial recovery with residual decay; at $\\beta$\\,=\\,5, sustained high GAR; at $\\beta$\\,=\\,10, saturation with catastrophic PPL.}\n  \\label{fig:steering-4panel}\n\\end{figure}\n\n\\section{Llama-3.1-8B Scheduled Sampling Details}\\label{sec:appendix-llama-ss}\n\nLlama-3.1-8B-Instruct was trained with scheduled sampling using the same protocol as Qwen (\\S\\ref{sec:appendix-ss}), with one key difference: training was stopped at 2 epochs (${\\sim}$14{,}400 steps) instead of 3, because Llama's per-step wall-clock time was ${\\sim}$4$\\times$ slower than Qwen on the same hardware (624 steps/h vs.\\ ${\\sim}$2{,}400 steps/h for Qwen). This is attributable to different vocabulary sizes (Llama 128K vs.\\ Qwen 152K tokens) and attention implementation. The 2-epoch checkpoint was selected based on convergence of TF GAR (0.477, within 0.02 of Qwen's 3-epoch value 0.498).\n\n\\paragraph{$\\beta$-steering on Llama SS.}\nTable~\\ref{tab:llama-ss-steering} reports $\\beta$-steering results on the Llama SS model. Unlike Qwen, $\\beta$\\,=\\,3 does not trigger recovery on Llama (GAR 0.173 vs.\\ 0.166 at $\\beta$\\,=\\,0). At $\\beta$\\,=\\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias at higher steering strengths, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{$\\beta$-steering on Llama-3.1-8B SS model ($N$\\,=\\,50, $T$\\,=\\,4).}\n\\label{tab:llama-ss-steering}\n\\begin{tabular}{@{}l ccc@{}}\n\\toprule\n& $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\beta$\\,=\\,5 \\\\\n\\midrule\nAR GAR & 0.166 & 0.173 & 0.791 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-model comparison.}\nTable~\\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\\times$) is larger than Qwen's (1.2$\\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\\times$ (from 27$\\times$ to 2.9$\\times$) while Qwen reduces by 6.6$\\times$ (from 7.9$\\times$ to 1.2$\\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\\beta$-steering is more effective on Llama (0.791 vs.\\ 0.717 at $\\beta$\\,=\\,5), partially compensating for the weaker training-time compression.\n\n\\paragraph{Architectural differences.}\nSeveral architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.\n\n\\paragraph{Training dynamics.}\nThe Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\\sim}$0.20 at the end of epoch~2 (vs.\\ 0.30 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (27$\\times$ $\\to$ 2.9$\\times$ by median) but leaves a larger residual gap than Qwen's full 3-epoch schedule.\n\n\\begin{table}[t]\n\\raggedright\\small\n\\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\\ Llama-3.1-8B.}\n\\label{tab:llama-vs-qwen-ss}\n\\begin{tabular}{@{}l cc@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\\n\\midrule\nSS epochs & 3 & 2 \\\\\nTF GAR & 0.498 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.2$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.6$\\times$ & 9.3$\\times$ \\\\\nAR GAR ($\\beta$\\,=\\,5) & 0.717 & 0.791 \\\\\nTF PPL & 2.78 & 2.82 \\\\\nAR PPL & 1.441 & 1.370 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Use of AI Assistants}\\label{sec:appendix-ai}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 488,
        "oldLines": 7,
        "newStart": 488,
        "newLines": 7,
        "lines": [
          " ",
          " Figure~\\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).",
          " ",
          "-\\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.9$\\times$) while PCGrad shows the largest (16.7$\\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\\sim}$1.2$\\times$, the only variant approaching parity. The ordering of gap ratios (SS $\\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\\sim$27$\\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\\ 28 layers), which provides more layers for distributional drift to compound through.",
          "+\\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.9$\\times$) while PCGrad shows the largest (16.7$\\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity. The ordering of gap ratios (SS $\\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\\sim$27$\\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\\ 28 layers), which provides more layers for distributional drift to compound through.",
          " ",
          " \\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\\,=\\,50), ThreadGate's gap is 8$\\times$; at 10 turns ($N$\\,=\\,5), it widens to 31$\\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.",
          " "
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

_source line 174_

<details open><summary>🔧 Tool call — Edit · `toolu_01NVnZjzWTFJYLpjmsQTZPQt`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "old_string": "the near-parity of scheduled sampling (${\\sim}$1.2$\\times$ gap) suggests that bridging",
  "new_string": "the near-parity of scheduled sampling (${\\sim}$1.3$\\times$ gap) suggests that bridging"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "db11bf53-d5d8-4e79-83f4-4cc9dfce8fcd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6SkmaP6R8FvufhX1T8jU1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2249,
      "cache_read_input_tokens": 71881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2249
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

_source line 175 · 2026-05-25T20:51:24.185Z_

<details><summary>↩ Tool result · `toolu_01NVnZjzWTFJYLpjmsQTZPQt`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "e3fe9d0c-435a-49d5-afef-c48f982f6ef5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "oldString": "the near-parity of scheduled sampling (${\\sim}$1.2$\\times$ gap) suggests that bridging",
    "newString": "the near-parity of scheduled sampling (${\\sim}$1.3$\\times$ gap) suggests that bridging",
    "originalFile": "\\section{Training Configuration}\\label{sec:appendix-hyper}\n\nTable~\\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\\times$ learning rate multiplier and are initialized with bias 1.5 ($\\sigma(1.5) \\approx 0.82$); the gate MLP adds ${\\sim}$57K parameters per variant ($<$0.001\\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.3 over 3 epochs (29.7--37.1\\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB VRAM), requiring 6--8 hours per variant.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\\dagger$ apply only to ThreadGate and its ablations.}\n\\label{tab:hyperparams}\n\\begin{tabular}{l@{\\hspace{8pt}}l}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\nBase model & Qwen-2.5-7B-Instruct \\\\\nLoRA rank / $\\alpha$ & 16 / 32 \\\\\nLoRA targets & \\texttt{q\\_proj}, \\texttt{v\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1$\\!=\\!0.9, $\\beta_2$\\!=\\!0.999) \\\\\nLearning rate & $2 \\times 10^{-4}$ \\\\\nGate LR mult.$^\\dagger$ & $10\\times$ \\\\\nBatch / grad accum & 1 / 8 (eff.\\ 8) \\\\\nEpochs & 3 \\\\\nMax seq length & 2048 \\\\\nTraining data & 8K UltraChat convs \\\\\nSeed & 42 (+123 for TG, SS) \\\\\n$\\lambda_\\text{GAR}$/$\\lambda_\\text{div}$ & 1.0 / 1.0 \\\\\nGAR target $\\tau$ & 0.5 \\\\\nGate init bias$^\\dagger$ & 1.5 ($\\sigma\\!\\approx\\!0.82$) \\\\\nGate hidden dim$^\\dagger$ & 64 \\\\\nTurn embed dim$^\\dagger$ & 16 \\\\\nGPU & RTX PRO 6000 (96\\,GB) \\\\\nTraining time & 6--8 h / variant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Loss Formulation Search}\\label{sec:appendix-loss}\n\nThe final MSE + gate diversity loss (\\S\\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.\n\n\\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.\n\n\\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\\text{mean}(\\text{GAR})$). The unbounded objective rewards full pass-through ($g \\to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\\lambda$=2 (v3), gates froze within 100 steps; at $\\lambda$=10 (v3b), convergence to identity accelerated; at $\\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.\n\n\\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.\n\n\\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\\tau$ incurs the same penalty as GAR below $\\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\\mathcal{L}_\\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).\n\n\\begin{table*}[t]\n\\centering\\footnotesize\n\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}\n\\label{tab:loss-iterations}\n\\begin{tabular}{l l l p{5.8cm} c c}\n\\toprule\n & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{Failure Mechanism} & \\textbf{GAR} & \\textbf{PPL} \\\\\n\\midrule\nv1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\\\\nv2  & Cumulative + $\\varepsilon$ & \\texttimes~same trajectory & Numerical instability from cumulative product; $\\varepsilon$-stabilization insufficient & ---  & ---  \\\\\nv3  & Maximize ($\\lambda$=2)  & \\texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\\\\nv3b & Maximize ($\\lambda$=10) & \\texttimes~identity collapse   & Higher $\\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\\\\nv5  & Maximize ($\\lambda$=1)  & \\texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\\\\nv6  & Smooth saturation       & \\texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\\\\nv7  & MSE + gate div          & \\checkmark~\\textbf{converged}  & \\textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Instruction Retention Details}\\label{sec:appendix-ir}\n\nTo evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\\beta$\\,=\\,3 steering on $N$\\,=\\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.\n\n\\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\\,=\\,54 paired evaluations (18 types $\\times$ 3 conversations per type) for the McNemar analysis.\n\n\\paragraph{Per-category results.} Table~\\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.\n\n\\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\\,=\\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.\n\nFigure~\\ref{fig:ir-bar} visualizes the per-category breakdown.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_instruction_retention.pdf}\n  \\caption{Instruction retention by constraint category under $\\beta$\\,=\\,3 steering. Content constraints benefit most (+23.8\\,pp); format and count constraints are unaffected.}\n  \\label{fig:ir-bar}\n\\end{figure}\n\n\\FloatBarrier\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Instruction retention by constraint category ($\\beta$\\,=\\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}\n\\label{tab:ir-results}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\Delta$ \\\\\n\\midrule\nContent    & 61.9\\% & 85.7\\% & +23.8\\,pp \\\\\nPosition   & 66.7\\% & 73.3\\% & +6.7\\,pp \\\\\nCount      & 100\\%  & 100\\%  & 0 \\\\\nFormat     & 100\\%  & 100\\%  & 0 \\\\\n\\midrule\n\\textbf{Overall} & 75.9\\% & 87.0\\% & +11.1\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Long-Conversation AR Evaluation}\\label{sec:appendix-n5}\n\nThe main results (Table~\\ref{tab:five-way}) report AR GAR from $N$\\,=\\,50 held-out conversations with a mean of 3.6 user turns. Table~\\ref{tab:n5-ar} presents complementary results on $N$\\,=\\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.\n\n\\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\\times$ (0.064 vs.\\ 0.037 in the $N$\\,=\\,50 evaluation) to 0.64$\\times$ (0.016 vs.\\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\\,=\\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.\n\n\\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\\times$ of the base model's GAR, compared to 3.4$\\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.\n\n\\paragraph{Caveats.} The $N$\\,=\\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{AR GAR-ours on $N$\\,=\\,5 ten-turn conversations. The gating advantage observed in Table~\\ref{tab:five-way} ($N$\\,=\\,50, mean 3.6 turns) diminishes with conversation length.}\n\\label{tab:n5-ar}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AR GAR-O} & \\textbf{$\\Delta$ vs.\\ Table~\\ref{tab:five-way}} \\\\\n\\midrule\nBase & 0.012 & $-$0.007 \\\\\n\\midrule\nThreadGate & 0.016 & $-$0.048 \\\\\n\\;+\\,PCGrad & 0.015 & $-$0.015 \\\\\nUniform Gate & 0.015 & $-$0.018 \\\\\nLoRA-only & 0.025 & $-$0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Statistical Test Details}\\label{sec:appendix-stats}\n\nAll statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\\ref{tab:stat-tests} consolidates the full results.\n\n\\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\\ LoRA-only comparison ($p$\\,=\\,0.004, $r$\\,=\\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\\ +PCGrad comparison ($p$\\,=\\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.\n\n\\paragraph{Bootstrap confidence intervals.} The 95\\% CIs in Table~\\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.\n\n\\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \\sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \\leq r < 0.5$ is medium, and $r \\geq 0.5$ is large. The TG vs.\\ LoRA-only effect ($r$\\,=\\,0.454) is medium, and TG vs.\\ Base ($r$\\,=\\,0.802) is large.\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \\leq 0.004$) survive this correction.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Consolidated statistical tests. All AR comparisons use $N$\\,=\\,50 conversations (39 with $\\geq$3 turns); gate conditioning uses 28 layers.}\n\\label{tab:stat-tests}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Test} & $p$ & $r$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{AR GAR-ours ($\\beta$\\,=\\,0)}} \\\\\nTG vs.\\ Base & Wilcoxon & $<$0.001 & 0.802 \\\\\nTG vs.\\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\\\\nTG vs.\\ +PCGrad & Wilcoxon & 0.002 & --- \\\\\nSS vs.\\ TG & Wilcoxon & $<$0.001 & 0.869 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Gate conditioning (28 layers)}} \\\\\nTurn 1 vs.\\ Turn 21 & Wilcoxon & $3.7\\!\\times\\!10^{-8}$ & 0.975 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Instruction retention}} \\\\\n$\\beta$\\,=\\,0 vs.\\ $\\beta$\\,=\\,3 & McNemar & 0.077 & --- \\\\\nGAR--compliance & Pearson & 0.007 & 0.200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Llama-3.1-8B Complete Results}\\label{sec:appendix-llama}\n\nTable~\\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \\S\\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.\n\n\\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\\ 0.50).\n\n\\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\\,=\\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\\% for ThreadGate (mean 0.043, std 0.100), and 5\\% of turn-level measurements exhibit sporadic attention spikes (GAR $\\geq$ 0.4). We therefore report both mean and median.\n\n\\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\\times$ by median for Llama vs.\\ 8--17$\\times$ for Qwen).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\\,=\\,50); AR: autoregressive ($N$\\,=\\,20 for Base/TG/LoRA-only, $N$\\,=\\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}\n\\label{tab:llama-full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{TF}} & \\multicolumn{2}{c}{\\textbf{AR}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\\\\n\\midrule\nBase & 0.017 & 3.45 & 0.009 & 0.009 \\\\\nThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\\\\nLoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\\\\n\\textbf{SS} & 0.477 & 2.82 & \\textbf{0.166} & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\FloatBarrier\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_crossmodel.pdf}\n  \\caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\\times$ by median), exceeding Qwen's 8$\\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}\n  \\label{fig:crossmodel}\n\\end{figure}\n\n\\paragraph{Cross-model summary.} Table~\\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\\approx$ 0.5, AR GAR $\\ll$ 0.1, gap $\\geq$ 7.9$\\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\\times$ by median for TG; mean-based range 11.2--17.2$\\times$) compared to Qwen's (7.9--13.5$\\times$) may reflect its deeper architecture (32 vs.\\ 28 layers), which allows more layers for distributional drift to compound through.\n\n\\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}\n\n\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\n\n\\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\\% longer than Qwen due to Llama's larger layer count (32 vs.\\ 28 layers).\n\n\\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\\% decline. This is steeper than Qwen's 70.8\\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\\ 28 KV heads).\n\n\\paragraph{Cross-model gradient analysis.} Table~\\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\\approx$\\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\\times$ on Qwen and 25.7$\\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \\emph{modus tollens} argument (\\S\\ref{subsec:pcgrad}): gradient direction conflict is not the primary cause of the TF-AR gap.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\\times$.}\n\\label{tab:gradient-crossmodel}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\\n\\midrule\nMean cos sim & $-$0.042 & +0.005 \\\\\nNeg-layer \\% & 67.9\\% & 53.1\\% \\\\\nNTP/GAR mag ratio & 14.7$\\times$ & 25.7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Additional Visualizations}\\label{sec:appendix-viz}\n\nThis section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.\n\n\\subsection{Gate Profile Heatmap}\n\nFigure~\\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_profile_heatmap.pdf}\n\\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\\times$ 5 conditions) and Llama-3.1-8B (32 layers $\\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}\n\\label{fig:gate-heatmap}\n\\end{figure}\n\n\\subsection{Cross-Model Gate Profile Comparison}\n\nFigure~\\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_profile_crossmodel.pdf}\n\\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}\n\\label{fig:gate-crossmodel}\n\\end{figure}\n\n\\subsection{Per-Turn AR GAR Decay}\n\nFigure~\\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\\% from turn 1 to turn 10; Llama base drops 90\\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\\ref{tab:five-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_ar_gar_perturn.pdf}\n\\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\\% (turn 1$\\to$10), Llama base drops 90\\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}\n\\label{fig:ar-gar-perturn}\n\\end{figure}\n\n\\subsection{Bootstrap Confidence Intervals}\n\nFigure~\\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\\% CIs reported in Table~\\ref{tab:five-way}.\n\n\\begin{figure}[H]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_bootstrap_ci.pdf}\n  \\caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\\ LoRA-only, $N$\\,=\\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\\,=\\,0.454).}\n  \\label{fig:bootstrap-ci}\n\\end{figure}\n\n\\subsection{Gate Value Distributions}\n\nFigure~\\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_distribution.pdf}\n\\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}\n\\label{fig:gate-distribution}\n\\end{figure}\n\n\\subsection{Training Loss Curves}\n\nFigure~\\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_training_loss_curves.pdf}\n\\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}\n\\label{fig:training-loss}\n\\end{figure}\n\n\\subsection{Full Attention Steering Results}\\label{sec:appendix-steering}\n\n\\begin{table*}[t]\n\\centering\\small\n\\caption{Full attention steering results across evaluation settings.\n\\textbf{Bold} indicates the operating point cited in the main text ($\\beta$\\,=\\,5).\nA visual gap separates the phase-transition boundary: GAR jumps sharply between $\\beta$\\,=\\,2 and $\\beta$\\,=\\,3 across all settings.}\n\\label{tab:steering-full}\n\\begin{tabular}{r cc cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,5, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,50, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,200, TF}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n$\\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\\\\n\\midrule\n0   & .028 & 1.41 & $.064 \\pm .081$ & $1.43 \\pm .10$ & .535 & 2.62 \\\\\n0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\\\\n1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\\\\n2   & .062 & 1.41 & $.128 \\pm .110$ & $1.48 \\pm .14$ & .611 & 2.69 \\\\\n\\addlinespace[3pt]\n3   & ---  & ---  & $.556 \\pm .060$ & $1.56 \\pm .17$ & .788 & 2.93 \\\\\n4   & ---  & ---  & $.644 \\pm .061$ & $1.67 \\pm .22$ & .817 & 3.49 \\\\\n\\textbf{5}  & \\textbf{.680} & \\textbf{1.91} & $\\mathbf{.727 \\pm .061}$ & $\\mathbf{1.77 \\pm .27}$ & \\textbf{.833} & \\textbf{6.15} \\\\\n10  & .959 & 4.22 & $.961 \\pm .015$ & $3.45 \\pm 1.78$ & .977 & 505.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_steering_standalone.pdf}\n  \\caption{Detailed $\\beta$-steering trade-off ($N$\\,=\\,50). GAR-ours (top) increases monotonically with $\\beta$; PPL (bottom) remains stable below $\\beta$\\,=\\,3 (9\\% cost), then rises sharply. The $\\beta$\\,=\\,3 operating point (circled) achieves 8.7$\\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}\n  \\label{fig:steering-standalone}\n\\end{figure}\n\n\\section{Per-Layer Gate Profile}\\label{sec:appendix-gate-profile}\n\nTable~\\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\\sigma$\\,=\\,0.051).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}\n\\label{tab:gate-profile}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cccccccc}\n\\toprule\nL0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\\\\n.883 & \\textbf{.793} & .996 & .988 & .984 & \\textbf{.797} & .961 & .918 \\\\\n\\midrule\nL8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\\\\n.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\\\\n\\midrule\nL16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\\\\n.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\\\\n\\midrule\nL24 & L25 & L26 & L27 & \\multicolumn{4}{c}{Summary} \\\\\n.980 & .984 & .988 & 1.00 & \\multicolumn{4}{c}{$\\bar{g}$\\,=\\,.947, $\\sigma$\\,=\\,.051} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.\n\n\\paragraph{Cross-model comparison.} See \\S\\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.\n\n\\section{Scheduled Sampling Implementation}\\label{sec:appendix-ss}\n\nOur scheduled sampling implementation follows \\citet{bengio2015scheduled} with modifications for multi-turn transformer training:\n\n\\paragraph{Sampling schedule.} The model-generated context ratio $\\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\\%) is lower than the nominal schedule due to per-sample Bernoulli variance.\n\n\\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.\n\n\\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\\ 0.947, min at L4 vs.\\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_training_dynamics.pdf}\n  \\caption{Scheduled sampling training dynamics: sampling ratio $\\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}\n  \\label{fig:ss-dynamics}\n\\end{figure}\n\n\\section{Computational Cost Analysis}\\label{sec:appendix-cost}\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\\,GB VRAM). VRAM reports peak allocated memory (excluding optimizer states).}\n\\label{tab:cost}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Params} & \\textbf{Time (h)} & \\textbf{VRAM} & \\textbf{Overhead} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Qwen-2.5-7B-Instruct}} \\\\\nLoRA-only & 4.2M & 5.7 & 42\\,GB & baseline \\\\\nThreadGate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\n\\;+\\,PCGrad & 4.3M & 8.0 & 43\\,GB & $+$33\\% \\\\\nUniform Gate & 4.3M & 6.1 & 43\\,GB & $+$57K \\\\\nSS (s42) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\nSS (s123) & 4.3M & 10.8 & 43\\,GB & $+$80\\% \\\\\nSS (s456) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Llama-3.1-8B-Instruct}} \\\\\nLoRA-only & 4.2M & 7.0 & 45\\,GB & baseline \\\\\nThreadGate & 4.3M & 7.3 & 46\\,GB & $+$65K \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Parameter overhead.} ThreadGate adds ${\\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\\times$ 2K per gate MLP) and ${\\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.\n\n\\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 5.7--7.3 hours. PCGrad adds ${\\sim}$33\\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\\% (6.5h) due to efficient batched generation, while seed 123 adds 80\\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.\n\n\\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\\to$64$\\to$1 MLP forward pass per layer adds $<$0.1\\% latency. $\\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.\n\n\\section{Qualitative Steering Examples}\\label{sec:appendix-examples}\n\nTable~\\ref{tab:examples} illustrates the effect of $\\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''\n\n\\begin{table*}[t]\n\\centering\\small\n\\caption{Qualitative effect of $\\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}\n\\label{tab:examples}\n\\begin{tabular}{c p{5.5cm} p{5.5cm}}\n\\toprule\n\\textbf{Turn} & \\textbf{$\\beta$\\,=\\,0 (unsteered)} & \\textbf{$\\beta$\\,=\\,3 (steered)} \\\\\n\\midrule\n1 & \\checkmark~Three bullet points, on-topic & \\checkmark~Three bullet points, on-topic \\\\\n2 & \\checkmark~Three bullet points, relevant & \\checkmark~Three bullet points, relevant \\\\\n3 & $\\sim$~Four bullet points, partially on-topic & \\checkmark~Three bullet points, on-topic \\\\\n4 & \\texttimes~Free-form paragraph, no bullets & \\checkmark~Three bullet points, on-topic \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe pattern is consistent with the GAR decay analysis (\\S\\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\\ref{tab:ir-results} shows that content constraints benefit most from this effect.\n\n\\section{Gradient Conflict Analysis}\\label{sec:appendix-gradient}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth,height=0.42\\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}\n  \\caption{(a)~Training GAR convergence to target ($\\tau$\\,=\\,0.5). (b)~PCGrad removes gradient conflict but $\\mathcal{L}_\\text{GAR}$ still collapses, confirming that gradient direction conflict is not the primary cause (\\S\\ref{subsec:pcgrad}).}\n  \\label{fig:training-pcgrad}\n\\end{figure}\n\nThis section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \\S\\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.\n\n\\paragraph{Gradient direction analysis.} Figure~\\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate and PCGrad training. Under standard training, 79\\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\\%$\\to$71\\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.\n\n\\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\\rho$\\,=\\,$-$0.12, $p$\\,=\\,0.54 between gate value and conflict magnitude).\n\n\\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\\times$ at epoch~0 and 14.7$\\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\\% of the effective update magnitude, explaining why PCGrad is ineffective.\n\n\\paragraph{Cross-model consistency.} Table~\\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \\textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient direction conflict is not the primary cause.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gradient_conflict_heatmap.pdf}\n\\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\\% to 68\\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\\%$\\to$71\\%) but does not improve AR GAR, ruling out gradient direction conflict as the primary cause (\\S\\ref{subsec:pcgrad}).}\n\\label{fig:gradient-heatmap}\n\\end{figure*}\n\n\\section{Training Data Characteristics}\\label{sec:appendix-data}\n\nAll experiments use 8,000 multi-turn conversations sampled from the UltraChat \\citep{ding2023ultrachat} training split. Table~\\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\\,=\\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\\,=\\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\\ref{sec:appendix-n5}).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Training and evaluation data characteristics. All data from UltraChat \\citep{ding2023ultrachat}.}\n\\label{tab:data-stats}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Property} & \\textbf{Train} & \\textbf{Eval (primary)} \\\\\n\\midrule\nConversations & 8,000 & 50 \\\\\nMin user turns & 3 & 3 \\\\\nMax sequence length & 2,048 & 2,048 \\\\\nSource & UltraChat train & UltraChat train \\\\\nOverlap & --- & non-overlapping \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Exposure Bias Scaling}\\label{sec:appendix-eb-scaling}\n\nFigure~\\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).\n\n\\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.9$\\times$) while PCGrad shows the largest (16.7$\\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity. The ordering of gap ratios (SS $\\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\\sim$27$\\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\\ 28 layers), which provides more layers for distributional drift to compound through.\n\n\\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\\,=\\,50), ThreadGate's gap is 8$\\times$; at 10 turns ($N$\\,=\\,5), it widens to 31$\\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.\n\n\\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\\sim}$1.2$\\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\\ref{sec:appendix-steering-viz}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_eb_scaling.pdf}\n\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}\n\\label{fig:eb-scaling}\n\\end{figure}\n\n\\section{Per-Turn AR GAR Dynamics}\\label{sec:appendix-ar-gar-dynamics}\n\nTo characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.\n\nAll six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\\S\\ref{subsec:ss}).}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_curves.pdf}\n\\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}\n\\label{fig:kl_ar_gar_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_bar.pdf}\n\\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}\n\\label{fig:kl_ar_gar_bar}\n\\end{figure}\n\nThis pattern contrasts with teacher-forced evaluation, where GAR remains relatively stable across turns for all configurations. Under teacher forcing, the model conditions on ground-truth context at each turn, preventing the distributional drift that causes GAR erosion in AR mode. The divergence between TF stability and AR decay provides turn-level evidence for the exposure bias mechanism described in \\S\\ref{sec:analysis}: training-time attention patterns are optimized for a distribution that AR generation progressively departs from.\n\n\\section{Per-Head KL Divergence Analysis}\\label{sec:appendix-kl}\n\nTo test whether exposure bias selectively disrupts goal-attending heads rather than uniformly affecting all attention patterns, we compute per-head TF vs.\\ AR attention divergence on 30 held-out conversations. For each of the 28 attention heads per layer (784 heads total), we measure the KL divergence $D_\\text{KL}(p_\\text{TF} \\| p_\\text{AR})$ between teacher-forced and autoregressive attention distributions, and the absolute GAR shift $\\Delta\\text{GAR} = |\\text{GAR}_\\text{TF} - \\text{GAR}_\\text{AR}|$. This head-level analysis provides diagnostic evidence for the exposure bias interpretation beyond the aggregate TF-AR gap.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Per-head TF-AR divergence statistics for Base and ThreadGate (Qwen-2.5-7B, 30 conversations). TG trains more concentrated goal attention under TF, but these high-GAR heads shift most under AR ($r$\\,=\\,0.743).}\n\\label{tab:kl-perhead}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Base} & \\textbf{TG} \\\\\n\\midrule\nMean $\\Delta$GAR & 0.012 & 0.016 \\\\\nMean KL & 0.043 & 0.054 \\\\\nCorr(TF\\_GAR, $\\Delta$GAR) & 0.673 & 0.743 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selective disruption.} ThreadGate exhibits 35\\% larger mean $\\Delta$GAR (0.016 vs.\\ 0.012) and 26\\% larger mean KL (0.054 vs.\\ 0.043) than Base. This is counterintuitive: the auxiliary GAR loss successfully trains more concentrated goal attention (higher TF GAR per head), but these very same heads shift more under AR generation. The correlation between per-head TF GAR and $\\Delta$GAR is strong for both models ($r$\\,=\\,0.673 for Base, 0.743 for TG), confirming that heads with higher goal attention under teacher forcing are disproportionately disrupted under autoregressive generation. This selectivity is a hallmark of exposure bias: the training-time optimization succeeds at creating a specific attention pattern (concentrated goal attention), but precisely this pattern has no autoregressive counterpart because it depends on conditioning on ground-truth context.\n\n\\paragraph{Layer-depth dependence.} The highest-KL heads concentrate at output-adjacent layers (L23--L27, KL\\,$>$\\,0.077) and L9 (KL\\,$\\approx$\\,0.068). Output-adjacent layers participate most directly in next-token prediction, so their attention distributions are most sensitive to changes in the conditioning context. L9's elevated KL may reflect a ``routing layer'' phenomenon observed in multi-layer transformers, where specific intermediate layers specialize in long-range information routing. The depth dependence is consistent with cumulative error propagation: distributional drift from model-generated tokens accumulates as information flows through successive layers, producing the largest attention shifts at the deepest layers.\n\n\\paragraph{Gate--KL independence.} Gate magnitude does not predict per-layer exposure bias severity: Spearman correlation between gate value and per-layer KL is 0.061 ($p$\\,=\\,0.757). The highest KL values concentrate at deep layers (L22--L27) where gates are near identity ($\\approx$1.0), while the lowest-gate layers show below-average KL (0.041 vs.\\ 0.056 for highest-gate layers). This independence confirms that the gating mechanism and the exposure bias phenomenon operate on different axes: gates modulate the magnitude of residual contributions, while exposure bias disrupts the direction (attention distribution) of those contributions. Even a ``perfect'' gate that could fully attenuate certain layers' residuals would not address the fundamental distributional mismatch that causes the attention shift.\n\n\\section{GAR Definition Robustness}\\label{sec:appendix-gar-robust}\n\nTo assess whether our conclusions depend on the specific GAR definition, we evaluate four alternative token-position variants on 50 held-out conversations (Table~\\ref{tab:gar-robust}): (1)~\\emph{ours} (last-token): attention from the last token to goal tokens (standard GAR-ours); (2)~\\emph{all-token}: average attention from all tokens to goal tokens; (3)~\\emph{first-token}: attention from the first assistant token to goal tokens; (4)~\\emph{goal-only}: attention from the last token to system-prompt-only tokens (excluding conversation content).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Mid-turn GAR under four alternative definitions ($N$\\,=\\,50 conversations). ThreadGate only improves query-position-specific definitions (last-token, goal-only); Scheduled Sampling raises all four definitions above 0.36.}\n\\label{tab:gar-robust}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Definition} & \\textbf{Base} & \\textbf{TG} & \\textbf{SS} \\\\\n\\midrule\nOurs (last-token) & 0.015 & \\textbf{0.325} & \\textbf{0.458} \\\\\nAll-token & 0.015 & 0.025 & \\textbf{0.366} \\\\\nFirst-token & 0.022 & 0.039 & \\textbf{0.412} \\\\\nGoal-only & 0.005 & \\textbf{0.310} & \\textbf{0.444} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThreadGate improvements are query-position-specific: the two definitions using the last token as query (ours: $0.015 \\to 0.325$; goal-only: $0.005 \\to 0.310$) show large gains, while all-token ($0.025$) and first-token ($0.039$) remain near base levels. This is expected: the GAR loss optimizes attention at the last-token position, so the learned routing does not generalize to other query positions.\n\nScheduled Sampling raises all four definitions above 0.36, with no definition falling below Base-relative gains. This confirms that SS builds a broad goal-attention pattern across token positions, rather than overfitting to the specific position targeted by the GAR loss. The pattern holds regardless of GAR definition: both the exposure bias diagnosis and the SS mitigation are robust to metric choice.\n\n\\section{General Capability Preservation (MMLU)}\\label{sec:appendix-mmlu}\n\nTo confirm that auxiliary GAR losses and attention steering do not degrade general language understanding, we evaluate all six Qwen-2.5-7B variants on MMLU 5-shot \\citep{hendrycks2021measuring} ($N$\\,=\\,14{,}042 questions).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\\,pp of the base LoRA-only checkpoint.}\n\\label{tab:mmlu}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{Acc (\\%)} & \\textbf{$\\Delta$ vs Base} \\\\\n\\midrule\nBase (pretrained) & 74.23 & --- \\\\\nPCGrad & 73.86 & $-$0.38 \\\\\nSS & 73.75 & $-$0.48 \\\\\nLoRA-only & 73.57 & $-$0.66 \\\\\nThreadGate & 73.47 & $-$0.77 \\\\\nUniform Gate & 73.46 & $-$0.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll variants degrade by $<$0.8\\,pp, confirming that attention steering and auxiliary GAR losses do not harm general language understanding. The ordering does not track GAR performance (e.g., PCGrad shows the smallest MMLU drop despite the worst AR GAR), consistent with GAR and NTP occupying largely orthogonal subspaces.\n\n\\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b}\n\nWe validate cross-scale on Qwen-2.5-1.5B-Instruct to test whether goal attention decay and $\\beta$-steering generalize to smaller models.\n\n\\paragraph{Phase~1 GAR decay.} The 1.5B base model exhibits 79.8\\% GAR decline from turn~1 to mid-turns (vs.\\ 70.8\\% on 7B), confirming that attention decay is present across scales and is more severe at smaller model sizes.\n\n\\paragraph{Steering evaluation.} Table~\\ref{tab:1.5b-steering} reports AR evaluation ($N$\\,=\\,50). We report median PPL because Base $\\beta$\\,=\\,3 contains a catastrophic outlier (conversation~\\#11, PPL\\,$>$\\,$10^8$) that inflates the mean.\\footnote{The outlier occurs in a single conversation where $\\beta$-steering causes the base model to enter a degenerate repetition loop. ThreadGate produces zero such outliers across all $\\beta$ values, suggesting the gate provides stability against catastrophic steering failures.}\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Cross-scale $\\beta$-steering on Qwen-2.5-1.5B ($N$\\,=\\,50, AR). PPL is median due to catastrophic Base outlier at $\\beta$\\,=\\,3. TG eliminates outliers across all $\\beta$ values.}\n\\label{tab:1.5b-steering}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Model} & $\\beta$ & \\textbf{AR GAR} & \\textbf{PPL (med)} \\\\\n\\midrule\nBase & 0 & 0.017 & 1.909 \\\\\nTG & 0 & 0.023 & 1.897 \\\\\n\\midrule\nBase & 3 & 0.120 & 2.216 \\\\\nTG & 3 & 0.114 & 1.975 \\\\\n\\midrule\nBase & 5 & 0.657 & 2.804 \\\\\nTG & 5 & 0.715 & 2.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe steering pattern mirrors the 7B results: $\\beta$\\,=\\,5 recovers GAR to 0.657--0.715 ($p < 0.001$), confirming that attention misallocation is the proximal cause of GAR collapse across scales. At $\\beta$\\,=\\,0, TG shows a small but significant GAR advantage ($p$\\,=\\,0.005); at $\\beta$\\,=\\,3, the TG--Base difference is not statistically significant ($p$\\,=\\,0.815), unlike the 7B pattern where TG consistently outperforms Base. This scale-specific difference may reflect the 1.5B model's limited capacity to maintain learned routing at intermediate steering strengths. ThreadGate does provide a stability advantage---zero catastrophic PPL outliers vs.\\ one in Base---suggesting that residual gating regularizes attention distributions even when aggregate GAR is comparable.\n\n\\section{Per-Seed Detailed Results}\\label{sec:appendix-perseed}\n\nTables~\\ref{tab:perseed-ss} and~\\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.\n\n\\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\\pm0.032$ across seeds under the held-out protocol (Table~\\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\\,=\\,200 sample. AR GAR shows meaningful variance (std\\,=\\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\\times$), seed 123 is intermediate (0.423, gap 1.3$\\times$), and seed 456 is highest (0.433, gap 1.2$\\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\\beta$\\,=\\,5, the cross-seed variance nearly vanishes ($0.717\\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.\n\n\\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\\pm0.001$) and similar AR GAR (0.064 vs.\\ 0.055), with gap ratios of 7.9$\\times$ and 9.1$\\times$ respectively. The 15\\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.\n\n\\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\\% overhead) vs.\\ 6.5 hours for seeds 42 and 456 (8\\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-generated contexts: seed 123 happens to trigger longer autoregressive generation episodes early in training, where the model produces longer outputs before hitting the max-length cutoff. Despite this training-time variance, all three seeds converge to similar final metrics, suggesting the optimization landscape is robust.\n\n\\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}\n\n\\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}\n\n\\section{Per-Turn GAR Decay Analysis}\\label{sec:appendix-perturn-detail}\n\nTables~\\ref{tab:perturn-qwen} and~\\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\\ref{tab:five-way}).\n\n\\paragraph{Qwen per-turn dynamics.} On Qwen (Table~\\ref{tab:perturn-qwen}), all non-SS variants show rapid monotonic decay: turn-1 GAR ranges from 0.085 (Base) to 0.130 (ThreadGate), but by turn~5 all collapse below 0.07. The decay rate is approximately exponential for the first 3 turns, then plateaus near a floor value that varies by configuration (Base: 0.004, ThreadGate: 0.043--0.066, LoRA-only: 0.040). ThreadGate and LoRA-only show occasional turn-level fluctuations (e.g., TG turn~5 = 0.066 $>$ turn~4 = 0.043), which reflect stochastic variation in individual conversations rather than systematic recovery. Scheduled sampling retains substantially higher GAR throughout (turn-5 GAR\\,=\\,0.365 vs.\\ 0.066 for ThreadGate), with a much flatter decay profile (15\\% decline from turn~1 to turn~5 vs.\\ 49\\% for ThreadGate). This flatter profile is the signature of distributional robustification: SS-trained models encounter model-generated context during training, so the attention patterns are calibrated for the distribution they actually face during inference.\n\n\\paragraph{Llama per-turn dynamics.} On Llama (Table~\\ref{tab:perturn-llama}), the decay is steeper: Base GAR drops from 0.028 to 0.008 over 4 turns (71\\% decline in the $N$\\,=\\,20 evaluation), and from 0.026 to 0.003 over 10 turns (88\\% decline in the $N$\\,=\\,5 long-conversation evaluation). ThreadGate on Llama shows a distinctive pattern: turn-level GAR is roughly constant (0.038--0.049) rather than monotonically declining, suggesting that the gating mechanism maintains a stable floor on Llama that it fails to maintain on Qwen. However, this floor (0.04) is still an order of magnitude below the TF target (0.484), confirming that the fundamental TF-AR gap persists.\n\n\\paragraph{Cross-architecture comparison.} The per-turn decay profiles reveal an architectural difference: Qwen shows a sharper initial decline (turn~1 to turn~2: $-$62\\% for Base) followed by a plateau, while Llama shows a more gradual and sustained decline throughout. This difference may reflect the two architectures' different attention head configurations and layer counts, but the qualitative pattern---monotonic or near-monotonic decline toward a near-zero floor---is universal.\n\nFigures~\\ref{fig:perturn-qwen-detail} and~\\ref{fig:perturn-llama-detail} visualize these trajectories.\n\n\\input{../artifacts/appendix_expansion/tab_perturn_qwen.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_perturn_qwen_detail.pdf}\n  \\caption{Per-turn AR GAR-ours across six Qwen-2.5-7B configurations. Scheduled sampling (green) retains far higher GAR than all other variants, which cluster below 0.13 and decay rapidly.}\n  \\label{fig:perturn-qwen-detail}\n\\end{figure}\n\n\\input{../artifacts/appendix_expansion/tab_perturn_llama.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_perturn_llama_detail.pdf}\n  \\caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\\,=\\,20, 4 turns). (b)~Extended Base decay profile ($N$\\,=\\,5, 10 turns), showing 90\\% decline.}\n  \\label{fig:perturn-llama-detail}\n\\end{figure}\n\n\\section{Extended Dataset Statistics}\\label{sec:appendix-dataset-ext}\n\nTable~\\ref{tab:dataset_stats} provides detailed statistics for the UltraChat training and evaluation splits. From the full UltraChat-200K corpus (207,865 conversations in the \\texttt{train\\_sft} split), we filter for conversations with $\\geq$5 assistant turns, yielding 17,302 candidates (8.3\\% of the full corpus). We randomly sample 8,000 for training, 50 for primary AR evaluation (mean 3.6 user turns), 50 for IID GAR diagnostics, and 200 for the instruction retention evaluation.\n\n\\paragraph{Filtering rationale.} The $\\geq$5 assistant turns threshold was chosen empirically: conversations with fewer than 3 assistant turns do not exhibit measurable attention decay (turn-1 to turn-3 GAR decline $<$5\\%), making them uninformative for studying multi-turn exposure bias. The 5-turn threshold provides sufficient turn depth while retaining a reasonable fraction of the corpus. The average conversation in the filtered set contains 5.6 assistant turns (range: 5--7), with a mean sequence length of 1,247 tokens after tokenization with the Qwen-2.5 tokenizer.\n\n\\paragraph{Evaluation split design.} We maintain four non-overlapping evaluation sets to avoid contamination: (1)~the primary AR evaluation ($N$\\,=\\,50) uses the same conversation structure as training but with held-out conversations, enabling direct comparison of TF vs.\\ AR behavior; (2)~the IID GAR diagnostic ($N$\\,=\\,50) uses a separate sample for ablation studies that require independent measurements; (3)~the large instruction retention set ($N$\\,=\\,200) provides sufficient statistical power for per-category compliance analysis across 18 constraint types; (4)~the long-conversation set ($N$\\,=\\,5, 10 turns each) tests scaling behavior beyond the training distribution.\n\n\\paragraph{Domain diversity.} UltraChat covers a broad range of conversational topics including knowledge Q\\&A, creative writing, reasoning, and open-ended discussion. We do not stratify by topic, as our focus is on the architectural mechanism (attention routing) rather than domain-specific performance. The topic diversity serves as implicit regularization against overfitting to specific conversation patterns.\n\n\\input{../artifacts/appendix_expansion/tab_dataset_stats.tex}\n\n\\section{Extended GAR Robustness Analysis}\\label{sec:appendix-gar-ext}\n\nTable~\\ref{tab:gar_robustness} and Figure~\\ref{fig:gar-robust-grouped} extend the GAR robustness analysis from \\S\\ref{sec:appendix-gar-robust} with turn-1 GAR and gap ratio metrics across all four token-position variants. We evaluate four ways to select the query token position for gradient attribution: (1)~\\textit{Last} (our default): the final token of each assistant turn, which captures the model's ``summary'' attention pattern at the prediction boundary; (2)~\\textit{All}: the mean over all assistant tokens, providing a position-averaged view; (3)~\\textit{First}: the first assistant token, which reflects initial attention allocation; (4)~\\textit{Goal-only}: attention to goal tokens as defined by \\citet{dongre2026attention}, which restricts the target set to system-prompt tokens.\n\n\\paragraph{Position-specific vs.\\ broad improvement.} The key finding is a clear dichotomy between ThreadGate and Scheduled Sampling. ThreadGate improvements are restricted to last-token and goal-only positions (the two definitions sharing the query position targeted by the GAR loss): gap ratios drop to 1.21$\\times$ and 1.07$\\times$ respectively. All-token (5.04$\\times$) and first-token (8.24$\\times$) GAR remain near base levels, confirming that the learned routing is position-specific. Scheduled Sampling raises all four definitions above 0.36 with gap ratios $\\leq$1.83$\\times$, demonstrating that distributional robustification builds broad goal attention across token positions rather than overfitting to the position targeted by the loss.\n\n\\paragraph{Turn-1 vs.\\ mid-turn dynamics.} Turn-1 GAR is consistently higher than mid-turn GAR across all definitions and conditions, reflecting the first turn's proximity to the ground-truth prefix in training. The gap ratio quantifies how much of this initial attention survives into later turns. First-token GAR shows the largest gap ratios (Base: 13.3$\\times$, TG: 8.2$\\times$), indicating that the first-token position is most vulnerable to distributional drift---the initial token's attention pattern is highly dependent on the conditioning context, which diverges most from training under autoregressive generation.\n\n\\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_gar_robustness_grouped.pdf}\n  \\caption{Mid-turn GAR across four token-position definitions. SS raises all four above 0.36; TG only improves last-token and goal-only.}\n  \\label{fig:gar-robust-grouped}\n\\end{figure}\n\n\\section{MMLU Category Breakdown}\\label{sec:appendix-mmlu-ext}\n\nTable~\\ref{tab:mmlu_detail} breaks down MMLU 5-shot accuracy by category (STEM, Social Sciences, Humanities, Other) for all six Qwen-2.5-7B training configurations. This analysis addresses a potential concern: that auxiliary attention objectives might divert representational capacity from general language understanding, particularly in knowledge-intensive STEM domains.\n\n\\paragraph{Per-category analysis.} The maximum per-category degradation is 1.5\\,pp (ThreadGate on STEM), and no category shows systematic degradation across all variants. Notably, the ordering of variants differs across categories: ThreadGate shows the largest STEM drop but the smallest Humanities drop, while PCGrad shows the smallest overall drop despite having the worst AR GAR. This lack of correlation between GAR performance and MMLU degradation is consistent with GAR and NTP occupying largely orthogonal parameter subspaces---the LoRA adapter capacity (4.2M parameters) is sufficient to accommodate both objectives without interference.\n\n\\paragraph{Statistical significance.} The per-category differences are small relative to the evaluation noise: with $N$\\,=\\,14,042 questions total ($\\sim$3,500 per category), a 0.8\\,pp accuracy difference corresponds to $\\sim$28 questions, well within expected stochastic variation for 5-shot in-context learning. A chi-squared test comparing the best (PCGrad, 73.86\\%) and worst (Uniform Gate, 73.46\\%) variants yields $p$\\,=\\,0.503, confirming no significant difference. The category-level stability confirms that auxiliary GAR losses and gating do not selectively harm any knowledge domain.\n\nFigure~\\ref{fig:mmlu-comparison} visualizes the per-category comparison, showing tight clustering across all variants within each category.\n\n\\input{../artifacts/appendix_expansion/tab_mmlu_detail.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_mmlu_comparison.pdf}\n  \\caption{MMLU 5-shot accuracy by category across training configurations. All variants remain within 1.5\\,pp of the LoRA-only baseline across all categories.}\n  \\label{fig:mmlu-comparison}\n\\end{figure}\n\n\\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b-ext}\n\nTable~\\ref{tab:qwen15b_results} extends the cross-scale analysis with Phase~1 GAR diagnostics, detailed Phase~2 training results, and $\\beta$-steering evaluation on the Qwen-2.5-1.5B-Instruct model.\n\n\\paragraph{Phase 1: GAR decay.} The 1.5B base model exhibits 79.8\\% relative GAR decline from turn~1 to mid-turns, more severe than the 7B model's 70.8\\% decline. This scale-dependent decay severity is consistent with smaller models having less redundant attention capacity: with 28 layers but only 1.5B parameters (vs.\\ 7B), each layer carries proportionally more of the total representational burden, leaving less room for goal-oriented attention to persist alongside the primary NTP objective.\n\n\\paragraph{Phase 2: Training.} ThreadGate training on 1.5B converges to TF GAR-ours of 0.498 with PPL of 2.67, closely matching the 7B results (0.504 / 2.78). The gate parameter count scales linearly with layer count (identical architecture, so ${\\sim}$57K gate parameters). Training completes in 2.1 hours vs.\\ 6.0 hours for 7B, reflecting the smaller model's reduced forward/backward pass cost.\n\n\\paragraph{Steering evaluation.} At $\\beta$\\,=\\,5, ThreadGate recovers GAR to 0.715 ($p < 0.001$), closely matching the 7B result (0.727). The recovery is essentially scale-independent at the strong steering regime: the attention bias added by $\\beta$-steering overwhelms any capacity differences. At $\\beta$\\,=\\,3, the picture differs: the TG--Base difference is not statistically significant ($p$\\,=\\,0.815) on 1.5B, unlike the significant difference on 7B ($p$\\,=\\,0.039). This scale-dependent response at intermediate $\\beta$ may reflect the 1.5B model's reduced capacity for fine-grained attention routing: with fewer parameters per layer, the model cannot sustain the subtle attention reweighting that $\\beta$\\,=\\,3 attempts.\n\n\\paragraph{Catastrophic outliers.} Base 1.5B at $\\beta$\\,=\\,3 produces one catastrophic PPL outlier (conversation \\#11, PPL $> 10^8$) caused by a degenerate repetition loop. ThreadGate produces zero such outliers across all $\\beta$ values, suggesting the gate provides a stabilizing effect on attention distributions even when aggregate GAR is comparable. We report median PPL to avoid this outlier dominating the central tendency estimate.\n\n\\input{../artifacts/appendix_expansion/tab_qwen15b_results.tex}\n\n\\section{Extended Statistical Analysis}\\label{sec:appendix-stats-ext}\n\nTable~\\ref{tab:statistical_tests} consolidates all statistical tests reported in this paper, including effect sizes, 95\\% bootstrap confidence intervals, and significance levels. This section provides methodological detail beyond the summary in Appendix~\\ref{sec:appendix-stats}.\n\n\\paragraph{Test selection rationale.} All primary comparisons use paired Wilcoxon signed-rank tests on $N$\\,=\\,39 conversations (those with $\\geq$3 turns from the 50-conversation held-out set). We use non-parametric tests because per-conversation GAR distributions are heavily right-skewed (skewness $>$ 2.0 for Base and PCGrad at $\\beta$\\,=\\,0), violating normality assumptions required by parametric alternatives. The pairing structure (same conversations evaluated under different training configurations) controls for conversation-level confounds (topic difficulty, conversation length, system-prompt complexity).\n\n\\paragraph{Effect size interpretation.} Effect sizes are computed as rank-biserial correlations ($r = Z / \\sqrt{N}$), following standard practice. The largest effect is SS vs.\\ TG ($r$\\,=\\,0.869, $p < 0.001$), a large effect by conventional thresholds ($r \\geq 0.5$), confirming that scheduled sampling produces a qualitatively different outcome. The TG vs.\\ Base effect ($r$\\,=\\,0.802) is also large, while TG vs.\\ LoRA-only ($r$\\,=\\,0.454) is medium, reflecting the modest incremental benefit of gating over LoRA alone.\n\n\\paragraph{Steering dose-response pattern.} At $\\beta$\\,=\\,0, all four comparisons are significant ($p \\leq 0.004$). At $\\beta$\\,=\\,3 (the phase transition), TG vs.\\ Base becomes marginally significant ($p$\\,=\\,0.039) and SS vs.\\ TG remains significant ($p$\\,=\\,0.010), but TG vs.\\ LoRA-only and PCGrad vs.\\ TG lose significance ($p > 0.7$). At $\\beta$\\,=\\,5, no pairwise comparison reaches significance---steering dominates and equalizes all variants. This dose-response pattern confirms that the training-time variant effects are real but small relative to the inference-time steering effect.\n\n\\paragraph{Instruction retention.} The instruction retention analysis uses McNemar's test on $N$\\,=\\,54 paired constraint evaluations (18 constraint types $\\times$ 3 conversations). The marginal significance ($p$\\,=\\,0.077) reflects the small sample size rather than a null effect: the point-biserial correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is significant when treating compliance as a continuous variable, and the per-category breakdown (Table~\\ref{tab:ir-results}) shows a clear content-constraint improvement (+23.8\\,pp).\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values for the same reason described in Appendix~\\ref{sec:appendix-stats}: comparisons are hypothesis-driven (each tests a specific causal exclusion in the analysis chain), not exploratory. All reported significant results ($p \\leq 0.039$) survive Holm-Bonferroni correction for the 4 primary comparisons within each $\\beta$ level.\n\n\\input{../artifacts/appendix_expansion/tab_statistical_tests.tex}\n\n\\section{Extended Training Dynamics}\\label{sec:appendix-training-ext}\n\nFigure~\\ref{fig:training-6panel} presents the complete training loss landscape for all five Qwen-2.5-7B conditions (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Scheduled Sampling) plus the base model, showing NTP loss, GAR loss, and total loss across three epochs.\n\n\\paragraph{NTP loss convergence.} All fine-tuned variants converge to NTP loss ${\\sim}$0.93 by epoch~3, with final-epoch values ranging from 0.929 (LoRA-only) to 0.934 (ThreadGate). PCGrad shows marginally higher variance due to gradient projection, but converges to the same terminal value. The uniformity of NTP convergence across variants---including those with auxiliary losses (ThreadGate, PCGrad) and those without (LoRA-only)---confirms that the GAR auxiliary objective does not interfere with the primary language modeling task during training.\n\n\\paragraph{GAR loss dynamics.} GAR loss collapses to near-zero within the first epoch under teacher forcing across all variants, consistent with the auxiliary objective being easy to optimize when the model conditions on ground-truth context. This rapid convergence is a double-edged sword: while it confirms that the MSE formulation (v7) achieves stable optimization, the ease of convergence also means the model never learns to maintain attention under distributional drift. The scheduled sampling variant shows distinctive dynamics: higher initial GAR loss variance from stochastic context mixing, with occasional spikes when a particularly challenging model-generated context is sampled, followed by convergence to a similar final value.\n\n\\paragraph{Training-inference disconnect.} The key observation is that training-time convergence is indistinguishable across variants: an observer with access only to training curves could not predict the 5.4$\\times$ AR GAR difference between SS and TG. This disconnect reinforces the diagnosis that the failure occurs at the training-to-inference transition, not during optimization, and explains why architectural modifications (gating, PCGrad) that operate during training cannot address the fundamental distributional mismatch.\n\n\\begin{figure*}[t]\n  \\centering\n  \\includegraphics[width=0.75\\textwidth]{fig_training_curves_6panel.pdf}\n  \\caption{Training loss curves for all five Qwen conditions. NTP loss (left) converges to ${\\sim}$0.93 across variants; GAR loss (center) collapses within epoch~1; total loss (right) is NTP-dominated. Training-time behavior is indistinguishable; the failure emerges only at inference.}\n  \\label{fig:training-6panel}\n\\end{figure*}\n\n\\section{Per-$\\beta$ Steering Visualization}\\label{sec:appendix-steering-viz}\n\nFigure~\\ref{fig:steering-4panel} visualizes per-turn GAR trajectories under four steering strengths ($\\beta$\\,=\\,0, 3, 5, 10), revealing the turn-level dynamics that underlie the aggregate steering results in Table~\\ref{tab:steering-full}.\n\n\\paragraph{Unsteered baseline ($\\beta$\\,=\\,0).} GAR decays monotonically from 0.12 to 0.02 over five turns, with the steepest decline between turns~1 and~2 ($-$44\\%). This trajectory matches the per-turn profiles in Appendix~\\ref{sec:appendix-perturn-detail} and confirms that the decay is a smooth, progressive phenomenon rather than a discrete failure at a specific turn.\n\n\\paragraph{Phase transition ($\\beta$\\,=\\,3).} Turn-1 GAR jumps to ${\\sim}$0.55, but per-turn decay persists (${\\sim}$15\\% decline from turn~1 to turn~5). This indicates that steering partially compensates for the distributional drift but does not eliminate it: the attention bias adds a constant offset to goal-token logits, while the drift compounds multiplicatively across turns. The residual decay at $\\beta$\\,=\\,3 explains why this operating point shows the strongest training-variant effects in the dose-response analysis (Appendix~\\ref{sec:appendix-stats-ext}).\n\n\\paragraph{Sustained recovery ($\\beta$\\,=\\,5).} GAR is sustained above 0.6 throughout, with minimal per-turn decay ($<$5\\% decline). At this steering strength, the constant attention bias dominates the per-turn drift, effectively replacing the lost training-time signal with an inference-time substitute. The 9\\% PPL cost (1.43 $\\to$ 1.77) is modest compared to the order-of-magnitude GAR recovery.\n\n\\paragraph{Saturation regime ($\\beta$\\,=\\,10).} GAR saturates near 1.0 across all turns but PPL degrades catastrophically ($>$3.5), as the excessive attention bias distorts the attention distribution beyond the model's capacity for coherent generation. This regime is impractical and serves as an upper bound on the steering approach.\n\n\\paragraph{Operating region.} The region $\\beta \\in [3, 5]$ balances GAR recovery against PPL cost, and the per-turn profiles confirm that steering must counteract an ongoing distributional drift rather than a one-time initialization failure---a key diagnostic that distinguishes exposure bias from alternative hypotheses (e.g., capacity limitations or optimization failures).\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_steering_perturn_4panel.pdf}\n  \\caption{Per-turn GAR under four $\\beta$-steering strengths. At $\\beta$\\,=\\,0, monotonic decay; at $\\beta$\\,=\\,3, partial recovery with residual decay; at $\\beta$\\,=\\,5, sustained high GAR; at $\\beta$\\,=\\,10, saturation with catastrophic PPL.}\n  \\label{fig:steering-4panel}\n\\end{figure}\n\n\\section{Llama-3.1-8B Scheduled Sampling Details}\\label{sec:appendix-llama-ss}\n\nLlama-3.1-8B-Instruct was trained with scheduled sampling using the same protocol as Qwen (\\S\\ref{sec:appendix-ss}), with one key difference: training was stopped at 2 epochs (${\\sim}$14{,}400 steps) instead of 3, because Llama's per-step wall-clock time was ${\\sim}$4$\\times$ slower than Qwen on the same hardware (624 steps/h vs.\\ ${\\sim}$2{,}400 steps/h for Qwen). This is attributable to different vocabulary sizes (Llama 128K vs.\\ Qwen 152K tokens) and attention implementation. The 2-epoch checkpoint was selected based on convergence of TF GAR (0.477, within 0.02 of Qwen's 3-epoch value 0.498).\n\n\\paragraph{$\\beta$-steering on Llama SS.}\nTable~\\ref{tab:llama-ss-steering} reports $\\beta$-steering results on the Llama SS model. Unlike Qwen, $\\beta$\\,=\\,3 does not trigger recovery on Llama (GAR 0.173 vs.\\ 0.166 at $\\beta$\\,=\\,0). At $\\beta$\\,=\\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias at higher steering strengths, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{$\\beta$-steering on Llama-3.1-8B SS model ($N$\\,=\\,50, $T$\\,=\\,4).}\n\\label{tab:llama-ss-steering}\n\\begin{tabular}{@{}l ccc@{}}\n\\toprule\n& $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\beta$\\,=\\,5 \\\\\n\\midrule\nAR GAR & 0.166 & 0.173 & 0.791 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-model comparison.}\nTable~\\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\\times$) is larger than Qwen's (1.2$\\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\\times$ (from 27$\\times$ to 2.9$\\times$) while Qwen reduces by 6.6$\\times$ (from 7.9$\\times$ to 1.2$\\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\\beta$-steering is more effective on Llama (0.791 vs.\\ 0.717 at $\\beta$\\,=\\,5), partially compensating for the weaker training-time compression.\n\n\\paragraph{Architectural differences.}\nSeveral architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.\n\n\\paragraph{Training dynamics.}\nThe Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\\sim}$0.20 at the end of epoch~2 (vs.\\ 0.30 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (27$\\times$ $\\to$ 2.9$\\times$ by median) but leaves a larger residual gap than Qwen's full 3-epoch schedule.\n\n\\begin{table}[t]\n\\raggedright\\small\n\\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\\ Llama-3.1-8B.}\n\\label{tab:llama-vs-qwen-ss}\n\\begin{tabular}{@{}l cc@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\\n\\midrule\nSS epochs & 3 & 2 \\\\\nTF GAR & 0.498 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.2$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.6$\\times$ & 9.3$\\times$ \\\\\nAR GAR ($\\beta$\\,=\\,5) & 0.717 & 0.791 \\\\\nTF PPL & 2.78 & 2.82 \\\\\nAR PPL & 1.441 & 1.370 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Use of AI Assistants}\\label{sec:appendix-ai}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 492,
        "oldLines": 7,
        "newStart": 492,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\\,=\\,50), ThreadGate's gap is 8$\\times$; at 10 turns ($N$\\,=\\,5), it widens to 31$\\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.",
          " ",
          "-\\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\\sim}$1.2$\\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\\ref{sec:appendix-steering-viz}).",
          "+\\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\\sim}$1.3$\\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\\ref{sec:appendix-steering-viz}).",
          " ",
          " \\begin{figure}[t]",
          " \\centering"
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

_source line 176_

<details open><summary>🔧 Tool call — Edit · `toolu_01C8Sre8o89xAXxL9YCNdqEc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "old_string": "\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}",
  "new_string": "\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.3$\\times$, 3-seed mean) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "fc604d74-0a75-4471-b1d8-f2384f9f4084",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6SkmaP6R8FvufhX1T8jU1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2249,
      "cache_read_input_tokens": 71881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2249
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

_source line 177 · 2026-05-25T20:51:28.855Z_

<details><summary>↩ Tool result · `toolu_01C8Sre8o89xAXxL9YCNdqEc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "cab5c426-be75-44c2-a3d7-84ffe15f71d3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
    "oldString": "\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}",
    "newString": "\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.3$\\times$, 3-seed mean) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}",
    "originalFile": "\\section{Training Configuration}\\label{sec:appendix-hyper}\n\nTable~\\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\\times$ learning rate multiplier and are initialized with bias 1.5 ($\\sigma(1.5) \\approx 0.82$); the gate MLP adds ${\\sim}$57K parameters per variant ($<$0.001\\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.3 over 3 epochs (29.7--37.1\\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB VRAM), requiring 6--8 hours per variant.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\\dagger$ apply only to ThreadGate and its ablations.}\n\\label{tab:hyperparams}\n\\begin{tabular}{l@{\\hspace{8pt}}l}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\nBase model & Qwen-2.5-7B-Instruct \\\\\nLoRA rank / $\\alpha$ & 16 / 32 \\\\\nLoRA targets & \\texttt{q\\_proj}, \\texttt{v\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1$\\!=\\!0.9, $\\beta_2$\\!=\\!0.999) \\\\\nLearning rate & $2 \\times 10^{-4}$ \\\\\nGate LR mult.$^\\dagger$ & $10\\times$ \\\\\nBatch / grad accum & 1 / 8 (eff.\\ 8) \\\\\nEpochs & 3 \\\\\nMax seq length & 2048 \\\\\nTraining data & 8K UltraChat convs \\\\\nSeed & 42 (+123 for TG, SS) \\\\\n$\\lambda_\\text{GAR}$/$\\lambda_\\text{div}$ & 1.0 / 1.0 \\\\\nGAR target $\\tau$ & 0.5 \\\\\nGate init bias$^\\dagger$ & 1.5 ($\\sigma\\!\\approx\\!0.82$) \\\\\nGate hidden dim$^\\dagger$ & 64 \\\\\nTurn embed dim$^\\dagger$ & 16 \\\\\nGPU & RTX PRO 6000 (96\\,GB) \\\\\nTraining time & 6--8 h / variant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Loss Formulation Search}\\label{sec:appendix-loss}\n\nThe final MSE + gate diversity loss (\\S\\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.\n\n\\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.\n\n\\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\\text{mean}(\\text{GAR})$). The unbounded objective rewards full pass-through ($g \\to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\\lambda$=2 (v3), gates froze within 100 steps; at $\\lambda$=10 (v3b), convergence to identity accelerated; at $\\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.\n\n\\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.\n\n\\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\\tau$ incurs the same penalty as GAR below $\\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\\mathcal{L}_\\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).\n\n\\begin{table*}[t]\n\\centering\\footnotesize\n\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}\n\\label{tab:loss-iterations}\n\\begin{tabular}{l l l p{5.8cm} c c}\n\\toprule\n & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{Failure Mechanism} & \\textbf{GAR} & \\textbf{PPL} \\\\\n\\midrule\nv1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\\\\nv2  & Cumulative + $\\varepsilon$ & \\texttimes~same trajectory & Numerical instability from cumulative product; $\\varepsilon$-stabilization insufficient & ---  & ---  \\\\\nv3  & Maximize ($\\lambda$=2)  & \\texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\\\\nv3b & Maximize ($\\lambda$=10) & \\texttimes~identity collapse   & Higher $\\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\\\\nv5  & Maximize ($\\lambda$=1)  & \\texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\\\\nv6  & Smooth saturation       & \\texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\\\\nv7  & MSE + gate div          & \\checkmark~\\textbf{converged}  & \\textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Instruction Retention Details}\\label{sec:appendix-ir}\n\nTo evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\\beta$\\,=\\,3 steering on $N$\\,=\\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.\n\n\\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\\,=\\,54 paired evaluations (18 types $\\times$ 3 conversations per type) for the McNemar analysis.\n\n\\paragraph{Per-category results.} Table~\\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.\n\n\\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\\,=\\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.\n\nFigure~\\ref{fig:ir-bar} visualizes the per-category breakdown.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_instruction_retention.pdf}\n  \\caption{Instruction retention by constraint category under $\\beta$\\,=\\,3 steering. Content constraints benefit most (+23.8\\,pp); format and count constraints are unaffected.}\n  \\label{fig:ir-bar}\n\\end{figure}\n\n\\FloatBarrier\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Instruction retention by constraint category ($\\beta$\\,=\\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}\n\\label{tab:ir-results}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\Delta$ \\\\\n\\midrule\nContent    & 61.9\\% & 85.7\\% & +23.8\\,pp \\\\\nPosition   & 66.7\\% & 73.3\\% & +6.7\\,pp \\\\\nCount      & 100\\%  & 100\\%  & 0 \\\\\nFormat     & 100\\%  & 100\\%  & 0 \\\\\n\\midrule\n\\textbf{Overall} & 75.9\\% & 87.0\\% & +11.1\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Long-Conversation AR Evaluation}\\label{sec:appendix-n5}\n\nThe main results (Table~\\ref{tab:five-way}) report AR GAR from $N$\\,=\\,50 held-out conversations with a mean of 3.6 user turns. Table~\\ref{tab:n5-ar} presents complementary results on $N$\\,=\\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.\n\n\\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\\times$ (0.064 vs.\\ 0.037 in the $N$\\,=\\,50 evaluation) to 0.64$\\times$ (0.016 vs.\\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\\,=\\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.\n\n\\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\\times$ of the base model's GAR, compared to 3.4$\\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.\n\n\\paragraph{Caveats.} The $N$\\,=\\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{AR GAR-ours on $N$\\,=\\,5 ten-turn conversations. The gating advantage observed in Table~\\ref{tab:five-way} ($N$\\,=\\,50, mean 3.6 turns) diminishes with conversation length.}\n\\label{tab:n5-ar}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AR GAR-O} & \\textbf{$\\Delta$ vs.\\ Table~\\ref{tab:five-way}} \\\\\n\\midrule\nBase & 0.012 & $-$0.007 \\\\\n\\midrule\nThreadGate & 0.016 & $-$0.048 \\\\\n\\;+\\,PCGrad & 0.015 & $-$0.015 \\\\\nUniform Gate & 0.015 & $-$0.018 \\\\\nLoRA-only & 0.025 & $-$0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Statistical Test Details}\\label{sec:appendix-stats}\n\nAll statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\\ref{tab:stat-tests} consolidates the full results.\n\n\\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\\ LoRA-only comparison ($p$\\,=\\,0.004, $r$\\,=\\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\\ +PCGrad comparison ($p$\\,=\\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.\n\n\\paragraph{Bootstrap confidence intervals.} The 95\\% CIs in Table~\\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.\n\n\\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \\sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \\leq r < 0.5$ is medium, and $r \\geq 0.5$ is large. The TG vs.\\ LoRA-only effect ($r$\\,=\\,0.454) is medium, and TG vs.\\ Base ($r$\\,=\\,0.802) is large.\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \\leq 0.004$) survive this correction.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Consolidated statistical tests. All AR comparisons use $N$\\,=\\,50 conversations (39 with $\\geq$3 turns); gate conditioning uses 28 layers.}\n\\label{tab:stat-tests}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Test} & $p$ & $r$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{AR GAR-ours ($\\beta$\\,=\\,0)}} \\\\\nTG vs.\\ Base & Wilcoxon & $<$0.001 & 0.802 \\\\\nTG vs.\\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\\\\nTG vs.\\ +PCGrad & Wilcoxon & 0.002 & --- \\\\\nSS vs.\\ TG & Wilcoxon & $<$0.001 & 0.869 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Gate conditioning (28 layers)}} \\\\\nTurn 1 vs.\\ Turn 21 & Wilcoxon & $3.7\\!\\times\\!10^{-8}$ & 0.975 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Instruction retention}} \\\\\n$\\beta$\\,=\\,0 vs.\\ $\\beta$\\,=\\,3 & McNemar & 0.077 & --- \\\\\nGAR--compliance & Pearson & 0.007 & 0.200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Llama-3.1-8B Complete Results}\\label{sec:appendix-llama}\n\nTable~\\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \\S\\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.\n\n\\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\\ 0.50).\n\n\\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\\,=\\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\\% for ThreadGate (mean 0.043, std 0.100), and 5\\% of turn-level measurements exhibit sporadic attention spikes (GAR $\\geq$ 0.4). We therefore report both mean and median.\n\n\\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\\times$ by median for Llama vs.\\ 8--17$\\times$ for Qwen).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\\,=\\,50); AR: autoregressive ($N$\\,=\\,20 for Base/TG/LoRA-only, $N$\\,=\\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}\n\\label{tab:llama-full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{TF}} & \\multicolumn{2}{c}{\\textbf{AR}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\\\\n\\midrule\nBase & 0.017 & 3.45 & 0.009 & 0.009 \\\\\nThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\\\\nLoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\\\\n\\textbf{SS} & 0.477 & 2.82 & \\textbf{0.166} & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\FloatBarrier\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_crossmodel.pdf}\n  \\caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\\times$ by median), exceeding Qwen's 8$\\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}\n  \\label{fig:crossmodel}\n\\end{figure}\n\n\\paragraph{Cross-model summary.} Table~\\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\\approx$ 0.5, AR GAR $\\ll$ 0.1, gap $\\geq$ 7.9$\\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\\times$ by median for TG; mean-based range 11.2--17.2$\\times$) compared to Qwen's (7.9--13.5$\\times$) may reflect its deeper architecture (32 vs.\\ 28 layers), which allows more layers for distributional drift to compound through.\n\n\\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}\n\n\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\n\n\\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\\% longer than Qwen due to Llama's larger layer count (32 vs.\\ 28 layers).\n\n\\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\\% decline. This is steeper than Qwen's 70.8\\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\\ 28 KV heads).\n\n\\paragraph{Cross-model gradient analysis.} Table~\\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\\approx$\\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\\times$ on Qwen and 25.7$\\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \\emph{modus tollens} argument (\\S\\ref{subsec:pcgrad}): gradient direction conflict is not the primary cause of the TF-AR gap.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\\times$.}\n\\label{tab:gradient-crossmodel}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\\n\\midrule\nMean cos sim & $-$0.042 & +0.005 \\\\\nNeg-layer \\% & 67.9\\% & 53.1\\% \\\\\nNTP/GAR mag ratio & 14.7$\\times$ & 25.7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Additional Visualizations}\\label{sec:appendix-viz}\n\nThis section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.\n\n\\subsection{Gate Profile Heatmap}\n\nFigure~\\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_profile_heatmap.pdf}\n\\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\\times$ 5 conditions) and Llama-3.1-8B (32 layers $\\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}\n\\label{fig:gate-heatmap}\n\\end{figure}\n\n\\subsection{Cross-Model Gate Profile Comparison}\n\nFigure~\\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_profile_crossmodel.pdf}\n\\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}\n\\label{fig:gate-crossmodel}\n\\end{figure}\n\n\\subsection{Per-Turn AR GAR Decay}\n\nFigure~\\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\\% from turn 1 to turn 10; Llama base drops 90\\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\\ref{tab:five-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_ar_gar_perturn.pdf}\n\\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\\% (turn 1$\\to$10), Llama base drops 90\\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}\n\\label{fig:ar-gar-perturn}\n\\end{figure}\n\n\\subsection{Bootstrap Confidence Intervals}\n\nFigure~\\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\\% CIs reported in Table~\\ref{tab:five-way}.\n\n\\begin{figure}[H]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_bootstrap_ci.pdf}\n  \\caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\\ LoRA-only, $N$\\,=\\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\\,=\\,0.454).}\n  \\label{fig:bootstrap-ci}\n\\end{figure}\n\n\\subsection{Gate Value Distributions}\n\nFigure~\\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_distribution.pdf}\n\\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}\n\\label{fig:gate-distribution}\n\\end{figure}\n\n\\subsection{Training Loss Curves}\n\nFigure~\\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_training_loss_curves.pdf}\n\\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}\n\\label{fig:training-loss}\n\\end{figure}\n\n\\subsection{Full Attention Steering Results}\\label{sec:appendix-steering}\n\n\\begin{table*}[t]\n\\centering\\small\n\\caption{Full attention steering results across evaluation settings.\n\\textbf{Bold} indicates the operating point cited in the main text ($\\beta$\\,=\\,5).\nA visual gap separates the phase-transition boundary: GAR jumps sharply between $\\beta$\\,=\\,2 and $\\beta$\\,=\\,3 across all settings.}\n\\label{tab:steering-full}\n\\begin{tabular}{r cc cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,5, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,50, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,200, TF}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n$\\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\\\\n\\midrule\n0   & .028 & 1.41 & $.064 \\pm .081$ & $1.43 \\pm .10$ & .535 & 2.62 \\\\\n0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\\\\n1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\\\\n2   & .062 & 1.41 & $.128 \\pm .110$ & $1.48 \\pm .14$ & .611 & 2.69 \\\\\n\\addlinespace[3pt]\n3   & ---  & ---  & $.556 \\pm .060$ & $1.56 \\pm .17$ & .788 & 2.93 \\\\\n4   & ---  & ---  & $.644 \\pm .061$ & $1.67 \\pm .22$ & .817 & 3.49 \\\\\n\\textbf{5}  & \\textbf{.680} & \\textbf{1.91} & $\\mathbf{.727 \\pm .061}$ & $\\mathbf{1.77 \\pm .27}$ & \\textbf{.833} & \\textbf{6.15} \\\\\n10  & .959 & 4.22 & $.961 \\pm .015$ & $3.45 \\pm 1.78$ & .977 & 505.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_steering_standalone.pdf}\n  \\caption{Detailed $\\beta$-steering trade-off ($N$\\,=\\,50). GAR-ours (top) increases monotonically with $\\beta$; PPL (bottom) remains stable below $\\beta$\\,=\\,3 (9\\% cost), then rises sharply. The $\\beta$\\,=\\,3 operating point (circled) achieves 8.7$\\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}\n  \\label{fig:steering-standalone}\n\\end{figure}\n\n\\section{Per-Layer Gate Profile}\\label{sec:appendix-gate-profile}\n\nTable~\\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\\sigma$\\,=\\,0.051).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}\n\\label{tab:gate-profile}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cccccccc}\n\\toprule\nL0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\\\\n.883 & \\textbf{.793} & .996 & .988 & .984 & \\textbf{.797} & .961 & .918 \\\\\n\\midrule\nL8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\\\\n.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\\\\n\\midrule\nL16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\\\\n.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\\\\n\\midrule\nL24 & L25 & L26 & L27 & \\multicolumn{4}{c}{Summary} \\\\\n.980 & .984 & .988 & 1.00 & \\multicolumn{4}{c}{$\\bar{g}$\\,=\\,.947, $\\sigma$\\,=\\,.051} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.\n\n\\paragraph{Cross-model comparison.} See \\S\\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.\n\n\\section{Scheduled Sampling Implementation}\\label{sec:appendix-ss}\n\nOur scheduled sampling implementation follows \\citet{bengio2015scheduled} with modifications for multi-turn transformer training:\n\n\\paragraph{Sampling schedule.} The model-generated context ratio $\\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\\%) is lower than the nominal schedule due to per-sample Bernoulli variance.\n\n\\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.\n\n\\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\\ 0.947, min at L4 vs.\\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_training_dynamics.pdf}\n  \\caption{Scheduled sampling training dynamics: sampling ratio $\\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}\n  \\label{fig:ss-dynamics}\n\\end{figure}\n\n\\section{Computational Cost Analysis}\\label{sec:appendix-cost}\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\\,GB VRAM). VRAM reports peak allocated memory (excluding optimizer states).}\n\\label{tab:cost}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Params} & \\textbf{Time (h)} & \\textbf{VRAM} & \\textbf{Overhead} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Qwen-2.5-7B-Instruct}} \\\\\nLoRA-only & 4.2M & 5.7 & 42\\,GB & baseline \\\\\nThreadGate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\n\\;+\\,PCGrad & 4.3M & 8.0 & 43\\,GB & $+$33\\% \\\\\nUniform Gate & 4.3M & 6.1 & 43\\,GB & $+$57K \\\\\nSS (s42) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\nSS (s123) & 4.3M & 10.8 & 43\\,GB & $+$80\\% \\\\\nSS (s456) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Llama-3.1-8B-Instruct}} \\\\\nLoRA-only & 4.2M & 7.0 & 45\\,GB & baseline \\\\\nThreadGate & 4.3M & 7.3 & 46\\,GB & $+$65K \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Parameter overhead.} ThreadGate adds ${\\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\\times$ 2K per gate MLP) and ${\\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.\n\n\\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 5.7--7.3 hours. PCGrad adds ${\\sim}$33\\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\\% (6.5h) due to efficient batched generation, while seed 123 adds 80\\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.\n\n\\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\\to$64$\\to$1 MLP forward pass per layer adds $<$0.1\\% latency. $\\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.\n\n\\section{Qualitative Steering Examples}\\label{sec:appendix-examples}\n\nTable~\\ref{tab:examples} illustrates the effect of $\\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''\n\n\\begin{table*}[t]\n\\centering\\small\n\\caption{Qualitative effect of $\\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}\n\\label{tab:examples}\n\\begin{tabular}{c p{5.5cm} p{5.5cm}}\n\\toprule\n\\textbf{Turn} & \\textbf{$\\beta$\\,=\\,0 (unsteered)} & \\textbf{$\\beta$\\,=\\,3 (steered)} \\\\\n\\midrule\n1 & \\checkmark~Three bullet points, on-topic & \\checkmark~Three bullet points, on-topic \\\\\n2 & \\checkmark~Three bullet points, relevant & \\checkmark~Three bullet points, relevant \\\\\n3 & $\\sim$~Four bullet points, partially on-topic & \\checkmark~Three bullet points, on-topic \\\\\n4 & \\texttimes~Free-form paragraph, no bullets & \\checkmark~Three bullet points, on-topic \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe pattern is consistent with the GAR decay analysis (\\S\\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\\ref{tab:ir-results} shows that content constraints benefit most from this effect.\n\n\\section{Gradient Conflict Analysis}\\label{sec:appendix-gradient}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth,height=0.42\\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}\n  \\caption{(a)~Training GAR convergence to target ($\\tau$\\,=\\,0.5). (b)~PCGrad removes gradient conflict but $\\mathcal{L}_\\text{GAR}$ still collapses, confirming that gradient direction conflict is not the primary cause (\\S\\ref{subsec:pcgrad}).}\n  \\label{fig:training-pcgrad}\n\\end{figure}\n\nThis section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \\S\\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.\n\n\\paragraph{Gradient direction analysis.} Figure~\\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate and PCGrad training. Under standard training, 79\\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\\%$\\to$71\\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.\n\n\\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\\rho$\\,=\\,$-$0.12, $p$\\,=\\,0.54 between gate value and conflict magnitude).\n\n\\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\\times$ at epoch~0 and 14.7$\\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\\% of the effective update magnitude, explaining why PCGrad is ineffective.\n\n\\paragraph{Cross-model consistency.} Table~\\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \\textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient direction conflict is not the primary cause.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gradient_conflict_heatmap.pdf}\n\\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\\% to 68\\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\\%$\\to$71\\%) but does not improve AR GAR, ruling out gradient direction conflict as the primary cause (\\S\\ref{subsec:pcgrad}).}\n\\label{fig:gradient-heatmap}\n\\end{figure*}\n\n\\section{Training Data Characteristics}\\label{sec:appendix-data}\n\nAll experiments use 8,000 multi-turn conversations sampled from the UltraChat \\citep{ding2023ultrachat} training split. Table~\\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\\,=\\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\\,=\\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\\ref{sec:appendix-n5}).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Training and evaluation data characteristics. All data from UltraChat \\citep{ding2023ultrachat}.}\n\\label{tab:data-stats}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Property} & \\textbf{Train} & \\textbf{Eval (primary)} \\\\\n\\midrule\nConversations & 8,000 & 50 \\\\\nMin user turns & 3 & 3 \\\\\nMax sequence length & 2,048 & 2,048 \\\\\nSource & UltraChat train & UltraChat train \\\\\nOverlap & --- & non-overlapping \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Exposure Bias Scaling}\\label{sec:appendix-eb-scaling}\n\nFigure~\\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).\n\n\\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.9$\\times$) while PCGrad shows the largest (16.7$\\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\\sim}$1.3$\\times$ (3-seed mean), the only variant approaching parity. The ordering of gap ratios (SS $\\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\\sim$27$\\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\\ 28 layers), which provides more layers for distributional drift to compound through.\n\n\\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\\,=\\,50), ThreadGate's gap is 8$\\times$; at 10 turns ($N$\\,=\\,5), it widens to 31$\\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.\n\n\\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\\sim}$1.3$\\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\\ref{sec:appendix-steering-viz}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_eb_scaling.pdf}\n\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}\n\\label{fig:eb-scaling}\n\\end{figure}\n\n\\section{Per-Turn AR GAR Dynamics}\\label{sec:appendix-ar-gar-dynamics}\n\nTo characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.\n\nAll six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\\S\\ref{subsec:ss}).}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_curves.pdf}\n\\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}\n\\label{fig:kl_ar_gar_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_bar.pdf}\n\\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}\n\\label{fig:kl_ar_gar_bar}\n\\end{figure}\n\nThis pattern contrasts with teacher-forced evaluation, where GAR remains relatively stable across turns for all configurations. Under teacher forcing, the model conditions on ground-truth context at each turn, preventing the distributional drift that causes GAR erosion in AR mode. The divergence between TF stability and AR decay provides turn-level evidence for the exposure bias mechanism described in \\S\\ref{sec:analysis}: training-time attention patterns are optimized for a distribution that AR generation progressively departs from.\n\n\\section{Per-Head KL Divergence Analysis}\\label{sec:appendix-kl}\n\nTo test whether exposure bias selectively disrupts goal-attending heads rather than uniformly affecting all attention patterns, we compute per-head TF vs.\\ AR attention divergence on 30 held-out conversations. For each of the 28 attention heads per layer (784 heads total), we measure the KL divergence $D_\\text{KL}(p_\\text{TF} \\| p_\\text{AR})$ between teacher-forced and autoregressive attention distributions, and the absolute GAR shift $\\Delta\\text{GAR} = |\\text{GAR}_\\text{TF} - \\text{GAR}_\\text{AR}|$. This head-level analysis provides diagnostic evidence for the exposure bias interpretation beyond the aggregate TF-AR gap.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Per-head TF-AR divergence statistics for Base and ThreadGate (Qwen-2.5-7B, 30 conversations). TG trains more concentrated goal attention under TF, but these high-GAR heads shift most under AR ($r$\\,=\\,0.743).}\n\\label{tab:kl-perhead}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Base} & \\textbf{TG} \\\\\n\\midrule\nMean $\\Delta$GAR & 0.012 & 0.016 \\\\\nMean KL & 0.043 & 0.054 \\\\\nCorr(TF\\_GAR, $\\Delta$GAR) & 0.673 & 0.743 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selective disruption.} ThreadGate exhibits 35\\% larger mean $\\Delta$GAR (0.016 vs.\\ 0.012) and 26\\% larger mean KL (0.054 vs.\\ 0.043) than Base. This is counterintuitive: the auxiliary GAR loss successfully trains more concentrated goal attention (higher TF GAR per head), but these very same heads shift more under AR generation. The correlation between per-head TF GAR and $\\Delta$GAR is strong for both models ($r$\\,=\\,0.673 for Base, 0.743 for TG), confirming that heads with higher goal attention under teacher forcing are disproportionately disrupted under autoregressive generation. This selectivity is a hallmark of exposure bias: the training-time optimization succeeds at creating a specific attention pattern (concentrated goal attention), but precisely this pattern has no autoregressive counterpart because it depends on conditioning on ground-truth context.\n\n\\paragraph{Layer-depth dependence.} The highest-KL heads concentrate at output-adjacent layers (L23--L27, KL\\,$>$\\,0.077) and L9 (KL\\,$\\approx$\\,0.068). Output-adjacent layers participate most directly in next-token prediction, so their attention distributions are most sensitive to changes in the conditioning context. L9's elevated KL may reflect a ``routing layer'' phenomenon observed in multi-layer transformers, where specific intermediate layers specialize in long-range information routing. The depth dependence is consistent with cumulative error propagation: distributional drift from model-generated tokens accumulates as information flows through successive layers, producing the largest attention shifts at the deepest layers.\n\n\\paragraph{Gate--KL independence.} Gate magnitude does not predict per-layer exposure bias severity: Spearman correlation between gate value and per-layer KL is 0.061 ($p$\\,=\\,0.757). The highest KL values concentrate at deep layers (L22--L27) where gates are near identity ($\\approx$1.0), while the lowest-gate layers show below-average KL (0.041 vs.\\ 0.056 for highest-gate layers). This independence confirms that the gating mechanism and the exposure bias phenomenon operate on different axes: gates modulate the magnitude of residual contributions, while exposure bias disrupts the direction (attention distribution) of those contributions. Even a ``perfect'' gate that could fully attenuate certain layers' residuals would not address the fundamental distributional mismatch that causes the attention shift.\n\n\\section{GAR Definition Robustness}\\label{sec:appendix-gar-robust}\n\nTo assess whether our conclusions depend on the specific GAR definition, we evaluate four alternative token-position variants on 50 held-out conversations (Table~\\ref{tab:gar-robust}): (1)~\\emph{ours} (last-token): attention from the last token to goal tokens (standard GAR-ours); (2)~\\emph{all-token}: average attention from all tokens to goal tokens; (3)~\\emph{first-token}: attention from the first assistant token to goal tokens; (4)~\\emph{goal-only}: attention from the last token to system-prompt-only tokens (excluding conversation content).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Mid-turn GAR under four alternative definitions ($N$\\,=\\,50 conversations). ThreadGate only improves query-position-specific definitions (last-token, goal-only); Scheduled Sampling raises all four definitions above 0.36.}\n\\label{tab:gar-robust}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Definition} & \\textbf{Base} & \\textbf{TG} & \\textbf{SS} \\\\\n\\midrule\nOurs (last-token) & 0.015 & \\textbf{0.325} & \\textbf{0.458} \\\\\nAll-token & 0.015 & 0.025 & \\textbf{0.366} \\\\\nFirst-token & 0.022 & 0.039 & \\textbf{0.412} \\\\\nGoal-only & 0.005 & \\textbf{0.310} & \\textbf{0.444} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThreadGate improvements are query-position-specific: the two definitions using the last token as query (ours: $0.015 \\to 0.325$; goal-only: $0.005 \\to 0.310$) show large gains, while all-token ($0.025$) and first-token ($0.039$) remain near base levels. This is expected: the GAR loss optimizes attention at the last-token position, so the learned routing does not generalize to other query positions.\n\nScheduled Sampling raises all four definitions above 0.36, with no definition falling below Base-relative gains. This confirms that SS builds a broad goal-attention pattern across token positions, rather than overfitting to the specific position targeted by the GAR loss. The pattern holds regardless of GAR definition: both the exposure bias diagnosis and the SS mitigation are robust to metric choice.\n\n\\section{General Capability Preservation (MMLU)}\\label{sec:appendix-mmlu}\n\nTo confirm that auxiliary GAR losses and attention steering do not degrade general language understanding, we evaluate all six Qwen-2.5-7B variants on MMLU 5-shot \\citep{hendrycks2021measuring} ($N$\\,=\\,14{,}042 questions).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\\,pp of the base LoRA-only checkpoint.}\n\\label{tab:mmlu}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{Acc (\\%)} & \\textbf{$\\Delta$ vs Base} \\\\\n\\midrule\nBase (pretrained) & 74.23 & --- \\\\\nPCGrad & 73.86 & $-$0.38 \\\\\nSS & 73.75 & $-$0.48 \\\\\nLoRA-only & 73.57 & $-$0.66 \\\\\nThreadGate & 73.47 & $-$0.77 \\\\\nUniform Gate & 73.46 & $-$0.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll variants degrade by $<$0.8\\,pp, confirming that attention steering and auxiliary GAR losses do not harm general language understanding. The ordering does not track GAR performance (e.g., PCGrad shows the smallest MMLU drop despite the worst AR GAR), consistent with GAR and NTP occupying largely orthogonal subspaces.\n\n\\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b}\n\nWe validate cross-scale on Qwen-2.5-1.5B-Instruct to test whether goal attention decay and $\\beta$-steering generalize to smaller models.\n\n\\paragraph{Phase~1 GAR decay.} The 1.5B base model exhibits 79.8\\% GAR decline from turn~1 to mid-turns (vs.\\ 70.8\\% on 7B), confirming that attention decay is present across scales and is more severe at smaller model sizes.\n\n\\paragraph{Steering evaluation.} Table~\\ref{tab:1.5b-steering} reports AR evaluation ($N$\\,=\\,50). We report median PPL because Base $\\beta$\\,=\\,3 contains a catastrophic outlier (conversation~\\#11, PPL\\,$>$\\,$10^8$) that inflates the mean.\\footnote{The outlier occurs in a single conversation where $\\beta$-steering causes the base model to enter a degenerate repetition loop. ThreadGate produces zero such outliers across all $\\beta$ values, suggesting the gate provides stability against catastrophic steering failures.}\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Cross-scale $\\beta$-steering on Qwen-2.5-1.5B ($N$\\,=\\,50, AR). PPL is median due to catastrophic Base outlier at $\\beta$\\,=\\,3. TG eliminates outliers across all $\\beta$ values.}\n\\label{tab:1.5b-steering}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Model} & $\\beta$ & \\textbf{AR GAR} & \\textbf{PPL (med)} \\\\\n\\midrule\nBase & 0 & 0.017 & 1.909 \\\\\nTG & 0 & 0.023 & 1.897 \\\\\n\\midrule\nBase & 3 & 0.120 & 2.216 \\\\\nTG & 3 & 0.114 & 1.975 \\\\\n\\midrule\nBase & 5 & 0.657 & 2.804 \\\\\nTG & 5 & 0.715 & 2.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe steering pattern mirrors the 7B results: $\\beta$\\,=\\,5 recovers GAR to 0.657--0.715 ($p < 0.001$), confirming that attention misallocation is the proximal cause of GAR collapse across scales. At $\\beta$\\,=\\,0, TG shows a small but significant GAR advantage ($p$\\,=\\,0.005); at $\\beta$\\,=\\,3, the TG--Base difference is not statistically significant ($p$\\,=\\,0.815), unlike the 7B pattern where TG consistently outperforms Base. This scale-specific difference may reflect the 1.5B model's limited capacity to maintain learned routing at intermediate steering strengths. ThreadGate does provide a stability advantage---zero catastrophic PPL outliers vs.\\ one in Base---suggesting that residual gating regularizes attention distributions even when aggregate GAR is comparable.\n\n\\section{Per-Seed Detailed Results}\\label{sec:appendix-perseed}\n\nTables~\\ref{tab:perseed-ss} and~\\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.\n\n\\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\\pm0.032$ across seeds under the held-out protocol (Table~\\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\\,=\\,200 sample. AR GAR shows meaningful variance (std\\,=\\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\\times$), seed 123 is intermediate (0.423, gap 1.3$\\times$), and seed 456 is highest (0.433, gap 1.2$\\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\\beta$\\,=\\,5, the cross-seed variance nearly vanishes ($0.717\\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.\n\n\\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\\pm0.001$) and similar AR GAR (0.064 vs.\\ 0.055), with gap ratios of 7.9$\\times$ and 9.1$\\times$ respectively. The 15\\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.\n\n\\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\\% overhead) vs.\\ 6.5 hours for seeds 42 and 456 (8\\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-generated contexts: seed 123 happens to trigger longer autoregressive generation episodes early in training, where the model produces longer outputs before hitting the max-length cutoff. Despite this training-time variance, all three seeds converge to similar final metrics, suggesting the optimization landscape is robust.\n\n\\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}\n\n\\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}\n\n\\section{Per-Turn GAR Decay Analysis}\\label{sec:appendix-perturn-detail}\n\nTables~\\ref{tab:perturn-qwen} and~\\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\\ref{tab:five-way}).\n\n\\paragraph{Qwen per-turn dynamics.} On Qwen (Table~\\ref{tab:perturn-qwen}), all non-SS variants show rapid monotonic decay: turn-1 GAR ranges from 0.085 (Base) to 0.130 (ThreadGate), but by turn~5 all collapse below 0.07. The decay rate is approximately exponential for the first 3 turns, then plateaus near a floor value that varies by configuration (Base: 0.004, ThreadGate: 0.043--0.066, LoRA-only: 0.040). ThreadGate and LoRA-only show occasional turn-level fluctuations (e.g., TG turn~5 = 0.066 $>$ turn~4 = 0.043), which reflect stochastic variation in individual conversations rather than systematic recovery. Scheduled sampling retains substantially higher GAR throughout (turn-5 GAR\\,=\\,0.365 vs.\\ 0.066 for ThreadGate), with a much flatter decay profile (15\\% decline from turn~1 to turn~5 vs.\\ 49\\% for ThreadGate). This flatter profile is the signature of distributional robustification: SS-trained models encounter model-generated context during training, so the attention patterns are calibrated for the distribution they actually face during inference.\n\n\\paragraph{Llama per-turn dynamics.} On Llama (Table~\\ref{tab:perturn-llama}), the decay is steeper: Base GAR drops from 0.028 to 0.008 over 4 turns (71\\% decline in the $N$\\,=\\,20 evaluation), and from 0.026 to 0.003 over 10 turns (88\\% decline in the $N$\\,=\\,5 long-conversation evaluation). ThreadGate on Llama shows a distinctive pattern: turn-level GAR is roughly constant (0.038--0.049) rather than monotonically declining, suggesting that the gating mechanism maintains a stable floor on Llama that it fails to maintain on Qwen. However, this floor (0.04) is still an order of magnitude below the TF target (0.484), confirming that the fundamental TF-AR gap persists.\n\n\\paragraph{Cross-architecture comparison.} The per-turn decay profiles reveal an architectural difference: Qwen shows a sharper initial decline (turn~1 to turn~2: $-$62\\% for Base) followed by a plateau, while Llama shows a more gradual and sustained decline throughout. This difference may reflect the two architectures' different attention head configurations and layer counts, but the qualitative pattern---monotonic or near-monotonic decline toward a near-zero floor---is universal.\n\nFigures~\\ref{fig:perturn-qwen-detail} and~\\ref{fig:perturn-llama-detail} visualize these trajectories.\n\n\\input{../artifacts/appendix_expansion/tab_perturn_qwen.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_perturn_qwen_detail.pdf}\n  \\caption{Per-turn AR GAR-ours across six Qwen-2.5-7B configurations. Scheduled sampling (green) retains far higher GAR than all other variants, which cluster below 0.13 and decay rapidly.}\n  \\label{fig:perturn-qwen-detail}\n\\end{figure}\n\n\\input{../artifacts/appendix_expansion/tab_perturn_llama.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_perturn_llama_detail.pdf}\n  \\caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\\,=\\,20, 4 turns). (b)~Extended Base decay profile ($N$\\,=\\,5, 10 turns), showing 90\\% decline.}\n  \\label{fig:perturn-llama-detail}\n\\end{figure}\n\n\\section{Extended Dataset Statistics}\\label{sec:appendix-dataset-ext}\n\nTable~\\ref{tab:dataset_stats} provides detailed statistics for the UltraChat training and evaluation splits. From the full UltraChat-200K corpus (207,865 conversations in the \\texttt{train\\_sft} split), we filter for conversations with $\\geq$5 assistant turns, yielding 17,302 candidates (8.3\\% of the full corpus). We randomly sample 8,000 for training, 50 for primary AR evaluation (mean 3.6 user turns), 50 for IID GAR diagnostics, and 200 for the instruction retention evaluation.\n\n\\paragraph{Filtering rationale.} The $\\geq$5 assistant turns threshold was chosen empirically: conversations with fewer than 3 assistant turns do not exhibit measurable attention decay (turn-1 to turn-3 GAR decline $<$5\\%), making them uninformative for studying multi-turn exposure bias. The 5-turn threshold provides sufficient turn depth while retaining a reasonable fraction of the corpus. The average conversation in the filtered set contains 5.6 assistant turns (range: 5--7), with a mean sequence length of 1,247 tokens after tokenization with the Qwen-2.5 tokenizer.\n\n\\paragraph{Evaluation split design.} We maintain four non-overlapping evaluation sets to avoid contamination: (1)~the primary AR evaluation ($N$\\,=\\,50) uses the same conversation structure as training but with held-out conversations, enabling direct comparison of TF vs.\\ AR behavior; (2)~the IID GAR diagnostic ($N$\\,=\\,50) uses a separate sample for ablation studies that require independent measurements; (3)~the large instruction retention set ($N$\\,=\\,200) provides sufficient statistical power for per-category compliance analysis across 18 constraint types; (4)~the long-conversation set ($N$\\,=\\,5, 10 turns each) tests scaling behavior beyond the training distribution.\n\n\\paragraph{Domain diversity.} UltraChat covers a broad range of conversational topics including knowledge Q\\&A, creative writing, reasoning, and open-ended discussion. We do not stratify by topic, as our focus is on the architectural mechanism (attention routing) rather than domain-specific performance. The topic diversity serves as implicit regularization against overfitting to specific conversation patterns.\n\n\\input{../artifacts/appendix_expansion/tab_dataset_stats.tex}\n\n\\section{Extended GAR Robustness Analysis}\\label{sec:appendix-gar-ext}\n\nTable~\\ref{tab:gar_robustness} and Figure~\\ref{fig:gar-robust-grouped} extend the GAR robustness analysis from \\S\\ref{sec:appendix-gar-robust} with turn-1 GAR and gap ratio metrics across all four token-position variants. We evaluate four ways to select the query token position for gradient attribution: (1)~\\textit{Last} (our default): the final token of each assistant turn, which captures the model's ``summary'' attention pattern at the prediction boundary; (2)~\\textit{All}: the mean over all assistant tokens, providing a position-averaged view; (3)~\\textit{First}: the first assistant token, which reflects initial attention allocation; (4)~\\textit{Goal-only}: attention to goal tokens as defined by \\citet{dongre2026attention}, which restricts the target set to system-prompt tokens.\n\n\\paragraph{Position-specific vs.\\ broad improvement.} The key finding is a clear dichotomy between ThreadGate and Scheduled Sampling. ThreadGate improvements are restricted to last-token and goal-only positions (the two definitions sharing the query position targeted by the GAR loss): gap ratios drop to 1.21$\\times$ and 1.07$\\times$ respectively. All-token (5.04$\\times$) and first-token (8.24$\\times$) GAR remain near base levels, confirming that the learned routing is position-specific. Scheduled Sampling raises all four definitions above 0.36 with gap ratios $\\leq$1.83$\\times$, demonstrating that distributional robustification builds broad goal attention across token positions rather than overfitting to the position targeted by the loss.\n\n\\paragraph{Turn-1 vs.\\ mid-turn dynamics.} Turn-1 GAR is consistently higher than mid-turn GAR across all definitions and conditions, reflecting the first turn's proximity to the ground-truth prefix in training. The gap ratio quantifies how much of this initial attention survives into later turns. First-token GAR shows the largest gap ratios (Base: 13.3$\\times$, TG: 8.2$\\times$), indicating that the first-token position is most vulnerable to distributional drift---the initial token's attention pattern is highly dependent on the conditioning context, which diverges most from training under autoregressive generation.\n\n\\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_gar_robustness_grouped.pdf}\n  \\caption{Mid-turn GAR across four token-position definitions. SS raises all four above 0.36; TG only improves last-token and goal-only.}\n  \\label{fig:gar-robust-grouped}\n\\end{figure}\n\n\\section{MMLU Category Breakdown}\\label{sec:appendix-mmlu-ext}\n\nTable~\\ref{tab:mmlu_detail} breaks down MMLU 5-shot accuracy by category (STEM, Social Sciences, Humanities, Other) for all six Qwen-2.5-7B training configurations. This analysis addresses a potential concern: that auxiliary attention objectives might divert representational capacity from general language understanding, particularly in knowledge-intensive STEM domains.\n\n\\paragraph{Per-category analysis.} The maximum per-category degradation is 1.5\\,pp (ThreadGate on STEM), and no category shows systematic degradation across all variants. Notably, the ordering of variants differs across categories: ThreadGate shows the largest STEM drop but the smallest Humanities drop, while PCGrad shows the smallest overall drop despite having the worst AR GAR. This lack of correlation between GAR performance and MMLU degradation is consistent with GAR and NTP occupying largely orthogonal parameter subspaces---the LoRA adapter capacity (4.2M parameters) is sufficient to accommodate both objectives without interference.\n\n\\paragraph{Statistical significance.} The per-category differences are small relative to the evaluation noise: with $N$\\,=\\,14,042 questions total ($\\sim$3,500 per category), a 0.8\\,pp accuracy difference corresponds to $\\sim$28 questions, well within expected stochastic variation for 5-shot in-context learning. A chi-squared test comparing the best (PCGrad, 73.86\\%) and worst (Uniform Gate, 73.46\\%) variants yields $p$\\,=\\,0.503, confirming no significant difference. The category-level stability confirms that auxiliary GAR losses and gating do not selectively harm any knowledge domain.\n\nFigure~\\ref{fig:mmlu-comparison} visualizes the per-category comparison, showing tight clustering across all variants within each category.\n\n\\input{../artifacts/appendix_expansion/tab_mmlu_detail.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_mmlu_comparison.pdf}\n  \\caption{MMLU 5-shot accuracy by category across training configurations. All variants remain within 1.5\\,pp of the LoRA-only baseline across all categories.}\n  \\label{fig:mmlu-comparison}\n\\end{figure}\n\n\\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b-ext}\n\nTable~\\ref{tab:qwen15b_results} extends the cross-scale analysis with Phase~1 GAR diagnostics, detailed Phase~2 training results, and $\\beta$-steering evaluation on the Qwen-2.5-1.5B-Instruct model.\n\n\\paragraph{Phase 1: GAR decay.} The 1.5B base model exhibits 79.8\\% relative GAR decline from turn~1 to mid-turns, more severe than the 7B model's 70.8\\% decline. This scale-dependent decay severity is consistent with smaller models having less redundant attention capacity: with 28 layers but only 1.5B parameters (vs.\\ 7B), each layer carries proportionally more of the total representational burden, leaving less room for goal-oriented attention to persist alongside the primary NTP objective.\n\n\\paragraph{Phase 2: Training.} ThreadGate training on 1.5B converges to TF GAR-ours of 0.498 with PPL of 2.67, closely matching the 7B results (0.504 / 2.78). The gate parameter count scales linearly with layer count (identical architecture, so ${\\sim}$57K gate parameters). Training completes in 2.1 hours vs.\\ 6.0 hours for 7B, reflecting the smaller model's reduced forward/backward pass cost.\n\n\\paragraph{Steering evaluation.} At $\\beta$\\,=\\,5, ThreadGate recovers GAR to 0.715 ($p < 0.001$), closely matching the 7B result (0.727). The recovery is essentially scale-independent at the strong steering regime: the attention bias added by $\\beta$-steering overwhelms any capacity differences. At $\\beta$\\,=\\,3, the picture differs: the TG--Base difference is not statistically significant ($p$\\,=\\,0.815) on 1.5B, unlike the significant difference on 7B ($p$\\,=\\,0.039). This scale-dependent response at intermediate $\\beta$ may reflect the 1.5B model's reduced capacity for fine-grained attention routing: with fewer parameters per layer, the model cannot sustain the subtle attention reweighting that $\\beta$\\,=\\,3 attempts.\n\n\\paragraph{Catastrophic outliers.} Base 1.5B at $\\beta$\\,=\\,3 produces one catastrophic PPL outlier (conversation \\#11, PPL $> 10^8$) caused by a degenerate repetition loop. ThreadGate produces zero such outliers across all $\\beta$ values, suggesting the gate provides a stabilizing effect on attention distributions even when aggregate GAR is comparable. We report median PPL to avoid this outlier dominating the central tendency estimate.\n\n\\input{../artifacts/appendix_expansion/tab_qwen15b_results.tex}\n\n\\section{Extended Statistical Analysis}\\label{sec:appendix-stats-ext}\n\nTable~\\ref{tab:statistical_tests} consolidates all statistical tests reported in this paper, including effect sizes, 95\\% bootstrap confidence intervals, and significance levels. This section provides methodological detail beyond the summary in Appendix~\\ref{sec:appendix-stats}.\n\n\\paragraph{Test selection rationale.} All primary comparisons use paired Wilcoxon signed-rank tests on $N$\\,=\\,39 conversations (those with $\\geq$3 turns from the 50-conversation held-out set). We use non-parametric tests because per-conversation GAR distributions are heavily right-skewed (skewness $>$ 2.0 for Base and PCGrad at $\\beta$\\,=\\,0), violating normality assumptions required by parametric alternatives. The pairing structure (same conversations evaluated under different training configurations) controls for conversation-level confounds (topic difficulty, conversation length, system-prompt complexity).\n\n\\paragraph{Effect size interpretation.} Effect sizes are computed as rank-biserial correlations ($r = Z / \\sqrt{N}$), following standard practice. The largest effect is SS vs.\\ TG ($r$\\,=\\,0.869, $p < 0.001$), a large effect by conventional thresholds ($r \\geq 0.5$), confirming that scheduled sampling produces a qualitatively different outcome. The TG vs.\\ Base effect ($r$\\,=\\,0.802) is also large, while TG vs.\\ LoRA-only ($r$\\,=\\,0.454) is medium, reflecting the modest incremental benefit of gating over LoRA alone.\n\n\\paragraph{Steering dose-response pattern.} At $\\beta$\\,=\\,0, all four comparisons are significant ($p \\leq 0.004$). At $\\beta$\\,=\\,3 (the phase transition), TG vs.\\ Base becomes marginally significant ($p$\\,=\\,0.039) and SS vs.\\ TG remains significant ($p$\\,=\\,0.010), but TG vs.\\ LoRA-only and PCGrad vs.\\ TG lose significance ($p > 0.7$). At $\\beta$\\,=\\,5, no pairwise comparison reaches significance---steering dominates and equalizes all variants. This dose-response pattern confirms that the training-time variant effects are real but small relative to the inference-time steering effect.\n\n\\paragraph{Instruction retention.} The instruction retention analysis uses McNemar's test on $N$\\,=\\,54 paired constraint evaluations (18 constraint types $\\times$ 3 conversations). The marginal significance ($p$\\,=\\,0.077) reflects the small sample size rather than a null effect: the point-biserial correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is significant when treating compliance as a continuous variable, and the per-category breakdown (Table~\\ref{tab:ir-results}) shows a clear content-constraint improvement (+23.8\\,pp).\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values for the same reason described in Appendix~\\ref{sec:appendix-stats}: comparisons are hypothesis-driven (each tests a specific causal exclusion in the analysis chain), not exploratory. All reported significant results ($p \\leq 0.039$) survive Holm-Bonferroni correction for the 4 primary comparisons within each $\\beta$ level.\n\n\\input{../artifacts/appendix_expansion/tab_statistical_tests.tex}\n\n\\section{Extended Training Dynamics}\\label{sec:appendix-training-ext}\n\nFigure~\\ref{fig:training-6panel} presents the complete training loss landscape for all five Qwen-2.5-7B conditions (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Scheduled Sampling) plus the base model, showing NTP loss, GAR loss, and total loss across three epochs.\n\n\\paragraph{NTP loss convergence.} All fine-tuned variants converge to NTP loss ${\\sim}$0.93 by epoch~3, with final-epoch values ranging from 0.929 (LoRA-only) to 0.934 (ThreadGate). PCGrad shows marginally higher variance due to gradient projection, but converges to the same terminal value. The uniformity of NTP convergence across variants---including those with auxiliary losses (ThreadGate, PCGrad) and those without (LoRA-only)---confirms that the GAR auxiliary objective does not interfere with the primary language modeling task during training.\n\n\\paragraph{GAR loss dynamics.} GAR loss collapses to near-zero within the first epoch under teacher forcing across all variants, consistent with the auxiliary objective being easy to optimize when the model conditions on ground-truth context. This rapid convergence is a double-edged sword: while it confirms that the MSE formulation (v7) achieves stable optimization, the ease of convergence also means the model never learns to maintain attention under distributional drift. The scheduled sampling variant shows distinctive dynamics: higher initial GAR loss variance from stochastic context mixing, with occasional spikes when a particularly challenging model-generated context is sampled, followed by convergence to a similar final value.\n\n\\paragraph{Training-inference disconnect.} The key observation is that training-time convergence is indistinguishable across variants: an observer with access only to training curves could not predict the 5.4$\\times$ AR GAR difference between SS and TG. This disconnect reinforces the diagnosis that the failure occurs at the training-to-inference transition, not during optimization, and explains why architectural modifications (gating, PCGrad) that operate during training cannot address the fundamental distributional mismatch.\n\n\\begin{figure*}[t]\n  \\centering\n  \\includegraphics[width=0.75\\textwidth]{fig_training_curves_6panel.pdf}\n  \\caption{Training loss curves for all five Qwen conditions. NTP loss (left) converges to ${\\sim}$0.93 across variants; GAR loss (center) collapses within epoch~1; total loss (right) is NTP-dominated. Training-time behavior is indistinguishable; the failure emerges only at inference.}\n  \\label{fig:training-6panel}\n\\end{figure*}\n\n\\section{Per-$\\beta$ Steering Visualization}\\label{sec:appendix-steering-viz}\n\nFigure~\\ref{fig:steering-4panel} visualizes per-turn GAR trajectories under four steering strengths ($\\beta$\\,=\\,0, 3, 5, 10), revealing the turn-level dynamics that underlie the aggregate steering results in Table~\\ref{tab:steering-full}.\n\n\\paragraph{Unsteered baseline ($\\beta$\\,=\\,0).} GAR decays monotonically from 0.12 to 0.02 over five turns, with the steepest decline between turns~1 and~2 ($-$44\\%). This trajectory matches the per-turn profiles in Appendix~\\ref{sec:appendix-perturn-detail} and confirms that the decay is a smooth, progressive phenomenon rather than a discrete failure at a specific turn.\n\n\\paragraph{Phase transition ($\\beta$\\,=\\,3).} Turn-1 GAR jumps to ${\\sim}$0.55, but per-turn decay persists (${\\sim}$15\\% decline from turn~1 to turn~5). This indicates that steering partially compensates for the distributional drift but does not eliminate it: the attention bias adds a constant offset to goal-token logits, while the drift compounds multiplicatively across turns. The residual decay at $\\beta$\\,=\\,3 explains why this operating point shows the strongest training-variant effects in the dose-response analysis (Appendix~\\ref{sec:appendix-stats-ext}).\n\n\\paragraph{Sustained recovery ($\\beta$\\,=\\,5).} GAR is sustained above 0.6 throughout, with minimal per-turn decay ($<$5\\% decline). At this steering strength, the constant attention bias dominates the per-turn drift, effectively replacing the lost training-time signal with an inference-time substitute. The 9\\% PPL cost (1.43 $\\to$ 1.77) is modest compared to the order-of-magnitude GAR recovery.\n\n\\paragraph{Saturation regime ($\\beta$\\,=\\,10).} GAR saturates near 1.0 across all turns but PPL degrades catastrophically ($>$3.5), as the excessive attention bias distorts the attention distribution beyond the model's capacity for coherent generation. This regime is impractical and serves as an upper bound on the steering approach.\n\n\\paragraph{Operating region.} The region $\\beta \\in [3, 5]$ balances GAR recovery against PPL cost, and the per-turn profiles confirm that steering must counteract an ongoing distributional drift rather than a one-time initialization failure---a key diagnostic that distinguishes exposure bias from alternative hypotheses (e.g., capacity limitations or optimization failures).\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_steering_perturn_4panel.pdf}\n  \\caption{Per-turn GAR under four $\\beta$-steering strengths. At $\\beta$\\,=\\,0, monotonic decay; at $\\beta$\\,=\\,3, partial recovery with residual decay; at $\\beta$\\,=\\,5, sustained high GAR; at $\\beta$\\,=\\,10, saturation with catastrophic PPL.}\n  \\label{fig:steering-4panel}\n\\end{figure}\n\n\\section{Llama-3.1-8B Scheduled Sampling Details}\\label{sec:appendix-llama-ss}\n\nLlama-3.1-8B-Instruct was trained with scheduled sampling using the same protocol as Qwen (\\S\\ref{sec:appendix-ss}), with one key difference: training was stopped at 2 epochs (${\\sim}$14{,}400 steps) instead of 3, because Llama's per-step wall-clock time was ${\\sim}$4$\\times$ slower than Qwen on the same hardware (624 steps/h vs.\\ ${\\sim}$2{,}400 steps/h for Qwen). This is attributable to different vocabulary sizes (Llama 128K vs.\\ Qwen 152K tokens) and attention implementation. The 2-epoch checkpoint was selected based on convergence of TF GAR (0.477, within 0.02 of Qwen's 3-epoch value 0.498).\n\n\\paragraph{$\\beta$-steering on Llama SS.}\nTable~\\ref{tab:llama-ss-steering} reports $\\beta$-steering results on the Llama SS model. Unlike Qwen, $\\beta$\\,=\\,3 does not trigger recovery on Llama (GAR 0.173 vs.\\ 0.166 at $\\beta$\\,=\\,0). At $\\beta$\\,=\\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias at higher steering strengths, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{$\\beta$-steering on Llama-3.1-8B SS model ($N$\\,=\\,50, $T$\\,=\\,4).}\n\\label{tab:llama-ss-steering}\n\\begin{tabular}{@{}l ccc@{}}\n\\toprule\n& $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\beta$\\,=\\,5 \\\\\n\\midrule\nAR GAR & 0.166 & 0.173 & 0.791 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-model comparison.}\nTable~\\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\\times$) is larger than Qwen's (1.2$\\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\\times$ (from 27$\\times$ to 2.9$\\times$) while Qwen reduces by 6.6$\\times$ (from 7.9$\\times$ to 1.2$\\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\\beta$-steering is more effective on Llama (0.791 vs.\\ 0.717 at $\\beta$\\,=\\,5), partially compensating for the weaker training-time compression.\n\n\\paragraph{Architectural differences.}\nSeveral architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.\n\n\\paragraph{Training dynamics.}\nThe Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\\sim}$0.20 at the end of epoch~2 (vs.\\ 0.30 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (27$\\times$ $\\to$ 2.9$\\times$ by median) but leaves a larger residual gap than Qwen's full 3-epoch schedule.\n\n\\begin{table}[t]\n\\raggedright\\small\n\\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\\ Llama-3.1-8B.}\n\\label{tab:llama-vs-qwen-ss}\n\\begin{tabular}{@{}l cc@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\\n\\midrule\nSS epochs & 3 & 2 \\\\\nTF GAR & 0.498 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.2$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.6$\\times$ & 9.3$\\times$ \\\\\nAR GAR ($\\beta$\\,=\\,5) & 0.717 & 0.791 \\\\\nTF PPL & 2.78 & 2.82 \\\\\nAR PPL & 1.441 & 1.370 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Use of AI Assistants}\\label{sec:appendix-ai}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 497,
        "oldLines": 7,
        "newStart": 497,
        "newLines": 7,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{fig_eb_scaling.pdf}",
          "-\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}",
          "+\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.3$\\times$, 3-seed mean) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}",
          " \\label{fig:eb-scaling}",
          " \\end{figure}",
          " "
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

_source line 178_

<details><summary>Logged reasoning block</summary>

```text
Now I need to check line 810 and 829 of appendix.tex. Line 810 says "residual gap on Llama (2.9×) is larger than Qwen's (1.2×)" and line 829 shows "TF/AR gap & 1.2× & 2.9×". 

These are in the llama-vs-qwen-ss comparison table which uses:
- Qwen: TF=0.498, AR=0.401 → gap=1.24≈1.2×
- Llama: TF=0.477, AR=0.166 → gap=2.87≈2.9×


The table is internally consistent, but there's a conflict: the appendix text reports Qwen's gap as 1.2× while the main text says 1.3×. I could either keep everything at 1.2× for consistency within the appendix, or update the table's Qwen TF value to 0.517 to match the 1.3× figure from the main text. Since this table is meant as a direct Qwen-Llama comparison using the same methodology, I need to decide whether internal consistency or alignment with the main text takes priority.

Looking closer at the data sources, the Qwen value (TF=0.498) is a 3-seed IID mean while the Llama value (TF=0.477) comes from a single run—they're already using different protocols. Given this mixing, I think it's better to keep the table as-is and accept that the 1.2× versus 1.3× difference reflects the different evaluation conditions rather than trying to force consistency by changing the underlying numbers. I'll update the table values to maintain consistency—changing the TF GAR value from 0.498 to 0.517 and the Qwen gap from 1.2× to 1.3×, then updating line 810 to reference this corrected value. So with the updated gap of 1.3×, the Qwen gap compression recalculates to 6.1× instead of 6.6×. Let me track down line 831 to see what else needs adjusting in that section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "2c463bb9-757b-4d9d-9c38-493c5b08b339",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mv8zYuA3xD8p6rfL1Yz7H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1098,
      "cache_read_input_tokens": 74130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1098
      },
      "output_tokens": 12,
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

_source line 179_

Let me also update the llama-vs-qwen-ss comparison table and its surrounding text for consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "db9e9dfa-4f39-47be-a17f-753a286f4957",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mv8zYuA3xD8p6rfL1Yz7H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1098,
      "cache_read_input_tokens": 74130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1098
      },
      "output_tokens": 12,
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

_source line 180_

<details open><summary>🔧 Tool call — Read · `toolu_01WqaES54VzY877UxjdY4PTr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 808,
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
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "b8f8fa37-a2ec-479e-82a7-ada89210921d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mv8zYuA3xD8p6rfL1Yz7H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1098,
      "cache_read_input_tokens": 74130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1098
      },
      "output_tokens": 12,
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

_source line 181 · 2026-05-25T20:51:57.793Z_

<details><summary>↩ Tool result · `toolu_01WqaES54VzY877UxjdY4PTr`</summary>

```text
808	
809	\paragraph{Cross-model comparison.}
810	Table~\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\times$) is larger than Qwen's (1.2$\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\times$ (from 27$\times$ to 2.9$\times$) while Qwen reduces by 6.6$\times$ (from 7.9$\times$ to 1.2$\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\beta$-steering is more effective on Llama (0.791 vs.\ 0.717 at $\beta$\,=\,5), partially compensating for the weaker training-time compression.
811	
812	\paragraph{Architectural differences.}
813	Several architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.
814	
815	\paragraph{Training dynamics.}
816	The Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\sim}$0.20 at the end of epoch~2 (vs.\ 0.30 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (27$\times$ $\to$ 2.9$\times$ by median) but leaves a larger residual gap than Qwen's full 3-epoch schedule.
817	
818	\begin{table}[t]
819	\raggedright\small
820	\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\ Llama-3.1-8B.}
821	\label{tab:llama-vs-qwen-ss}
822	\begin{tabular}{@{}l cc@{}}
823	\toprule
824	\textbf{Metric} & \textbf{Qwen-7B} & \textbf{Llama-8B} \\
825	\midrule
826	SS epochs & 3 & 2 \\
827	TF GAR & 0.498 & 0.477 \\
828	AR GAR ($\beta$\,=\,0) & 0.401 & 0.166 \\
829	TF/AR gap & 1.2$\times$ & 2.9$\times$ \\
830	Baseline TG gap & 7.9$\times$ & 27$\times$ (median) \\
831	Gap compression & 6.6$\times$ & 9.3$\times$ \\
832	AR GAR ($\beta$\,=\,5) & 0.717 & 0.791 \\
833	TF PPL & 2.78 & 2.82 \\
834	AR PPL & 1.441 & 1.370 \\
835	\bottomrule
836	\end{tabular}
837	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "12fa6231-4b6d-435c-97c6-2e0eb9c8ef25",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\n\\paragraph{Cross-model comparison.}\nTable~\\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\\times$) is larger than Qwen's (1.2$\\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\\times$ (from 27$\\times$ to 2.9$\\times$) while Qwen reduces by 6.6$\\times$ (from 7.9$\\times$ to 1.2$\\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\\beta$-steering is more effective on Llama (0.791 vs.\\ 0.717 at $\\beta$\\,=\\,5), partially compensating for the weaker training-time compression.\n\n\\paragraph{Architectural differences.}\nSeveral architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.\n\n\\paragraph{Training dynamics.}\nThe Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\\sim}$0.20 at the end of epoch~2 (vs.\\ 0.30 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (27$\\times$ $\\to$ 2.9$\\times$ by median) but leaves a larger residual gap than Qwen's full 3-epoch schedule.\n\n\\begin{table}[t]\n\\raggedright\\small\n\\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\\ Llama-3.1-8B.}\n\\label{tab:llama-vs-qwen-ss}\n\\begin{tabular}{@{}l cc@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\\n\\midrule\nSS epochs & 3 & 2 \\\\\nTF GAR & 0.498 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.2$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.6$\\times$ & 9.3$\\times$ \\\\\nAR GAR ($\\beta$\\,=\\,5) & 0.717 & 0.791 \\\\\nTF PPL & 2.78 & 2.82 \\\\\nAR PPL & 1.441 & 1.370 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
      "numLines": 30,
      "startLine": 808,
      "totalLines": 851
    }
  }
}
```

</details>

---


### Assistant

_source line 182_

<details><summary>Logged reasoning block</summary>

```text
Now I need to update this table and paragraph. The Qwen values should use 3-seed mean held-out TF (0.517) for consistency with the rest of the paper.

Changes:
- Line 827: TF GAR 0.498 → 0.517
- Line 829: TF/AR gap 1.2× → 1.3×
- Line 831: Gap compression 6.6× → 6.1× (7.9/1.3 = 6.08 ≈ 6.1×)


- Line 810: Updating the Qwen multiplier notation from 1.2× to ~1.3× and adjusting the gap compression language to reflect 6.1× (from 7.9× to ~1.3×)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "52721519-7dab-4a67-8f24-ceed92676152",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QnLKzpL5rCq2KySYESTTD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 75228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2461
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

_source line 183_

<details open><summary>🔧 Tool call — Edit · `toolu_01CrRYEapakXBGqAR8HLTkU2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "old_string": "TF GAR & 0.498 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.2$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.6$\\times$ & 9.3$\\times$ \\\\",
  "new_string": "TF GAR & 0.517 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.3$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.1$\\times$ & 9.3$\\times$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e143be5-ff60-46aa-b6d7-c21a267d4280",
  "uuid": "3ccf13a3-d221-40c0-b727-ed1ce6bce931",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QnLKzpL5rCq2KySYESTTD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 75228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2461
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
