# paper c6 results appendix detector

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_c6-results-appendix-detector_20260518T113449.log`
- **Structured JSON:** [`0fc91ed301f56542f3d4.json`](../../sessions/0f/0fc91ed301f56542f3d4.json)

## Before a recorded user message

26 recorded events

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
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
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
  "uuid": "a37bcacb-5a85-4ef4-a1d1-b54be31b111a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779105000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d9aaf0e5-47c7-4ea8-9b5b-ec20b30b630d",
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070"
}
```

---

### Assistant

_source line 4_

I'll start by reading the relevant files to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "067b966e-e987-4627-be5e-de3ce22554a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ef5wMXFBB5L9KZgSNuQHM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13668,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13668
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

<details open><summary>🔧 Tool call — Read · `toolu_016ranNmbVuQWgTLPL86FGwK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "f9b88aa4-8efe-4d7f-a883-863ed431ea81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ef5wMXFBB5L9KZgSNuQHM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13668,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13668
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

_source line 6 · 2026-05-18T11:35:03.440Z_

<details><summary>↩ Tool result · reported error · `toolu_016ranNmbVuQWgTLPL86FGwK`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "b0f93561-c18a-46a2-984c-59534a93fe2a",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01Q9G4gwYhjyQLTFmDN7ot6d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "da349e7a-b2dd-499d-ac00-b2b7b2c6e581",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ef5wMXFBB5L9KZgSNuQHM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13668,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13668
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

_source line 8 · 2026-05-18T11:35:03.900Z_

<details><summary>↩ Tool result · reported error · `toolu_01Q9G4gwYhjyQLTFmDN7ot6d`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon. Did you mean results.md?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "921099bb-9ce0-4c50-b4d3-bd6fa2f873f2",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon. Did you mean results.md?"
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01SATyxiKgKDQUM5n32R8Jmu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/sections/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "f2d360e5-530e-4133-b17b-70defde5d617",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ef5wMXFBB5L9KZgSNuQHM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13668,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13668
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

_source line 10 · 2026-05-18T11:35:04.359Z_

<details><summary>↩ Tool result · reported error · `toolu_01SATyxiKgKDQUM5n32R8Jmu`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "02fb1500-47fe-4bfd-bef6-38495780db4e",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon."
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01XHGQXUuMLQCRv1QnTjj39F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "92374c9a-4dbb-4ffc-992c-e902a145aeab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ef5wMXFBB5L9KZgSNuQHM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13668,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13668
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

_source line 12 · 2026-05-18T11:35:04.672Z_

<details><summary>↩ Tool result · reported error · `toolu_01XHGQXUuMLQCRv1QnTjj39F`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "f5329fa0-0258-4d7c-9459-eb3b50b18643",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon."
}
```

</details>

---

### Assistant

_source line 13_

Let me find where the paper files actually are.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "70463606-ed54-4ba9-8d66-4caf2637afe1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNzgoo6vF2Mydk1JsiQoPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 608,
      "cache_read_input_tokens": 25115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 608
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

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_014TTjX7Gj4YgBbsm3zMjYvE`</summary>

```json
{
  "pattern": "**/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "5bbd3598-c57e-4610-9235-f13980283eae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNzgoo6vF2Mydk1JsiQoPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 608,
      "cache_read_input_tokens": 25115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 608
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

_source line 15 · 2026-05-18T11:35:07.397Z_

<details><summary>↩ Tool result · `toolu_014TTjX7Gj4YgBbsm3zMjYvE`</summary>

```text
docs/paper/_corl_template/corl_2026_template_submission/example.tex
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex
artifacts/_project/paper/nve_sensitivity_table_37b680.tex
paper/tables/nve_sensitivity_table.tex
artifacts/_project/paper/nve_sensitivity_table.tex
docs/paper/sections/related_work.tex
docs/paper/main.tex
docs/paper/sections/abstract_body.tex
docs/paper/sections/introduction.tex
docs/paper/sections/analysis.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/appendix.tex
docs/paper/sections/methodology.tex
docs/paper/sections/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "5806e245-eeb1-4b6e-9b0c-7a25b30b29bb",
  "tool_use_result": {
    "filenames": [
      "docs/paper/_corl_template/corl_2026_template_submission/example.tex",
      "docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex",
      "artifacts/_project/paper/nve_sensitivity_table_37b680.tex",
      "paper/tables/nve_sensitivity_table.tex",
      "artifacts/_project/paper/nve_sensitivity_table.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/abstract_body.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/analysis.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/sections/methodology.tex",
      "docs/paper/sections/results.tex"
    ],
    "durationMs": 27,
    "numFiles": 14,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Glob · `toolu_01HgCt6xyXvFYdhTZhzqfrx6`</summary>

```json
{
  "pattern": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "5651000b-6266-47db-a87e-2dbd4314a527",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNzgoo6vF2Mydk1JsiQoPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 608,
      "cache_read_input_tokens": 25115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 608
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

_source line 17 · 2026-05-18T11:35:07.637Z_

<details><summary>↩ Tool result · `toolu_01HgCt6xyXvFYdhTZhzqfrx6`</summary>

```text
docs/paper/_corl_template/corl_2026_template_submission/example.tex
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex
artifacts/dream_reports/dream_20260514T062606/best/paper.tex
artifacts/dream_reports/dream_20260514T062606/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/best/paper.tex
artifacts/dream_reports/dream_20260515T004704/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/worst/paper.tex
artifacts/figures/archive/tab_rssm_fidelity.tex
artifacts/_project/paper/nve_sensitivity_table_37b680.tex
artifacts/dream_reports/dream_20260514T062606/worst/paper.tex
artifacts/dream_reports/dream_20260516T115400/best/paper.tex
artifacts/dream_reports/dream_20260516T115400/median/paper.tex
artifacts/dream_reports/dream_20260516T115400/worst/paper.tex
artifacts/dream_reports/dream_20260516T133210/best/paper.tex
artifacts/dream_reports/dream_20260516T133210/median/paper.tex
artifacts/dream_reports/dream_20260516T133210/worst/paper.tex
artifacts/dream_reports/dream_20260516T172011/best/paper.tex
artifacts/dream_reports/dream_20260516T172011/median/paper.tex
artifacts/dream_reports/dream_20260516T172011/worst/paper.tex
artifacts/analysis/detector_table.tex
paper/tables/nve_sensitivity_table.tex
artifacts/_project/paper/nve_sensitivity_table.tex
docs/paper/sections/related_work.tex
docs/paper/main.tex
docs/paper/sections/abstract_body.tex
docs/paper/sections/introduction.tex
docs/paper/sections/analysis.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/appendix.tex
docs/paper/sections/methodology.tex
docs/paper/sections/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "760336b9-117b-4f69-9c5d-936e2ef6e6a3",
  "tool_use_result": {
    "filenames": [
      "docs/paper/_corl_template/corl_2026_template_submission/example.tex",
      "docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex",
      "artifacts/dream_reports/dream_20260514T062606/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T062606/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/worst/paper.tex",
      "artifacts/figures/archive/tab_rssm_fidelity.tex",
      "artifacts/_project/paper/nve_sensitivity_table_37b680.tex",
      "artifacts/dream_reports/dream_20260514T062606/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/worst/paper.tex",
      "artifacts/analysis/detector_table.tex",
      "paper/tables/nve_sensitivity_table.tex",
      "artifacts/_project/paper/nve_sensitivity_table.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/abstract_body.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/analysis.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/sections/methodology.tex",
      "docs/paper/sections/results.tex"
    ],
    "durationMs": 26,
    "numFiles": 31,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 18_

Files are under `docs/paper/sections/`. Let me read them all.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "c18e36c3-e1c8-4662-bfdf-1ce6398c1518",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJDsxhhooqcA3aFgoJqmJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 25723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 891
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

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01CVUhdffswtt3KQHxdYiYfP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "854cd430-e168-4e93-8ee5-b9d8f0738774",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJDsxhhooqcA3aFgoJqmJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 25723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 891
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

_source line 20 · 2026-05-18T11:35:10.980Z_

<details><summary>↩ Tool result · `toolu_01CVUhdffswtt3KQHxdYiYfP`</summary>

```text
1	% --- APPENDIX ---
2	
3	\section{Complete Experimental Results}
4	\label{sec:complete_results}
5	
6	Table~\ref{tab:complete_results} reports all 24 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
7	
8	\begin{table*}[t]
9	\centering
10	\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
11	\label{tab:complete_results}
12	\footnotesize
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{llcccccl}
15	\toprule
16	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
17	\midrule
18	001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
19	\rowcolor{gray!15}
20	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
21	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
22	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
23	\midrule
24	\rowcolor{gray!15}
25	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
26	\rowcolor{gray!15}
27	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
28	\rowcolor{gray!15}
29	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
30	\rowcolor{gray!15}
31	008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 3.03$\times$ & Full collapse \\
32	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
33	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
34	008a\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.43$\times$ & Healthy \\
35	008a\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.51$\times$ & Healthy \\
36	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
37	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
38	\midrule
39	018 s1 & Full-SGS & trn$^\ddagger$ & ON & 8 & \sgseval{} @105K & \sgsnve{}$\times$$^*$ & No collapse \\
40	\rowcolor{gray!15}
41	018 s2 & Full-SGS & trn$^\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\
42	008e\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\times$ & Healthy \\
43	008e\_v3 s2$^\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\times$ & Non-CIVO collapse \\
44	\midrule
45	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
46	\rowcolor{gray!15}
47	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
48	\rowcolor{gray!15}
49	010b\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 70.64$\times$ & Full collapse \\
50	\rowcolor{gray!15}
51	021 & Cheetah Run & trn$^\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\times$$^d$ & Recovery \\
52	024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\times$ & Healthy \\
53	024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\times$ & Healthy \\
54	\rowcolor{gray!15}
55	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
56	\bottomrule
57	\end{tabular}
58	\vspace{1pt}
59	{\raggedright\footnotesize
60	trn = trained ($d{=}32$, subsample ON);
61	trn$^\ddagger$ = full-pathway SGS (all non-KL gradients detached);
62	exp$^a$ = trained, subsample OFF;
63	frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
64	--- = removed ($d{=}0$).\\
65	$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\times$ at 35K, 1.66$\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\
66	$^\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\
67	$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).\\
68	$^d$ Peak NVE $9.94\times$ at 45K (transient, self-correcting to $<$1$\times$ by 55K); final eval 221.5.\par}
69	\end{table*}
70	
71	\section{NVE Threshold Sensitivity Analysis}
72	\label{sec:appendix_sensitivity}
73	
74	We report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\nve \geq 1.5\times$). Here we additionally present Task~B1, which restricts the positive class to \emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.
75	
76	\subsection{Per-Experiment NVE Values}
77	
78	Table~\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eight factorial experiments. Experiments are sorted by descending NVE. Experiment 008e\_v3\_s2 exhibits elevated NVE ($3.78\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks.
79	
80	\begin{table}[h]
81	\centering
82	\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\ = transient CIVO with self-correction.}
83	\label{tab:nve_raw}
84	\small
85	\begin{tabular}{@{}lrccc@{}}
86	\toprule
87	Experiment & NVE & Mechanism & B1 & B2 \\
88	\midrule
89	006          & 4.84 & sustained CIVO & $+$ & $+$ \\
90	008d         & 4.13 & sustained CIVO & $+$ & $+$ \\
91	008e\_v3\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\
92	009b         & 1.62 & transient CIVO & $-$ & $+$ \\
93	001          & 1.00 & non-CIVO       & $-$ & $-$ \\
94	008f         & 0.97 & non-CIVO       & $-$ & $-$ \\
95	008e\_v3\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\
96	008a         & 0.93 & non-CIVO       & $-$ & $-$ \\
97	\bottomrule
98	\end{tabular}
99	\end{table}
100	
101	\subsection{Multi-Threshold Classification Performance}
102	
103	Table~\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\text{AUROC} = 1.000$ because the minimum positive NVE ($4.13\times$, exp~008d) exceeds the maximum negative NVE ($3.78\times$, exp~008e\_v3\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.13]$; we report $\geq 3.9\times$ as a representative value. Table~\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\text{AUROC} = 0.933$, imperfect separation due to 008e\_v3\_s2).
104	
105	\begin{table*}[t]
106	\centering
107	\caption{\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\text{pos}}=2$, $n_{\text{neg}}=6$, $n=8$, $\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\alpha=0.05$). Thresholds 1.2$\times$/1.5$\times$ and 1.7$\times$/2.0$\times$ yield identical operating points (no NVE values in those intervals). $^\dagger$Optimal threshold in $(3.78, 4.13]$.}
108	\label{tab:sensitivity_b1}
109	\small
110	\setlength{\tabcolsep}{5pt}
111	\begin{tabular}{@{}lcccccccc@{}}
112	\toprule
113	Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
114	\midrule
115	$\geq 1.0\times$ & 2 & 3 & 0 & 3 & 62.5\% \; [24.5, 91.5] & 40.0\% & 100\% & 57.1\% \\
116	$\geq 1.2\times$ & 2 & 2 & 0 & 4 & 75.0\% \; [34.9, 96.8] & 50.0\% & 100\% & 66.7\% \\
117	$\geq 1.5\times$ & 2 & 2 & 0 & 4 & 75.0\% \; [34.9, 96.8] & 50.0\% & 100\% & 66.7\% \\
118	\rowcolor{gray!15}
119	$\geq 1.7\times$ & 2 & 1 & 0 & 5 & 87.5\% \; [47.3, 99.7] & 66.7\% & 100\% & 80.0\% \\
120	$\geq 2.0\times$ & 2 & 1 & 0 & 5 & 87.5\% \; [47.3, 99.7] & 66.7\% & 100\% & 80.0\% \\
121	\rowcolor{gray!15}
122	$\geq 3.9\times^\dagger$ & 2 & 0 & 0 & 6 & 100\% \; [63.1, 100] & 100\% & 100\% & 100\% \\
123	\bottomrule
124	\end{tabular}
125	\end{table*}
126	
127	\begin{table*}[t]
128	\centering
129	\caption{\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\text{pos}}=3$, $n_{\text{neg}}=5$, $n=8$, $\text{AUROC}=0.933$). The single false positive at $\geq 1.5\times$ is 008e\_v3\_s2 (IRD mechanism, not CIVO). The $1.5\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}
130	\label{tab:sensitivity_b2}
131	\small
132	\setlength{\tabcolsep}{5pt}
133	\begin{tabular}{@{}lcccccccc@{}}
134	\toprule
135	Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
136	\midrule
137	$\geq 1.0\times$ & 3 & 2 & 0 & 3 & 75.0\% \; [34.9, 96.8] & 60.0\% & 100\% & 75.0\% \\
138	$\geq 1.2\times$ & 3 & 1 & 0 & 4 & 87.5\% \; [47.3, 99.7] & 75.0\% & 100\% & 85.7\% \\
139	\rowcolor{gray!15}
140	$\geq 1.5\times$ & 3 & 1 & 0 & 4 & 87.5\% \; [47.3, 99.7] & 75.0\% & 100\% & 85.7\% \\
141	$\geq 1.7\times$ & 2 & 1 & 1 & 4 & 75.0\% \; [34.9, 96.8] & 66.7\% & 66.7\% & 66.7\% \\
142	$\geq 2.0\times$ & 2 & 1 & 1 & 4 & 75.0\% \; [34.9, 96.8] & 66.7\% & 66.7\% & 66.7\% \\
143	$\geq 3.9\times$ & 2 & 0 & 1 & 5 & 87.5\% \; [47.3, 99.7] & 100\% & 66.7\% & 80.0\% \\
144	\bottomrule
145	\end{tabular}
146	\end{table*}
147	
148	\subsection{Threshold Recommendation}
149	
150	For the main diagnostic (Task~B2), we recommend $\nve \geq 1.5\times$ as the operating threshold for three reasons:
151	
152	\begin{enumerate}[nosep,leftmargin=*]
153	\item \textbf{Maximum recall.} The $1.5\times$ threshold achieves 100\% recall, detecting all three CIVO cases including the transient case (009b, $\nve = 1.62\times$). Raising the threshold to $1.7\times$ loses 009b, dropping recall to 66.7\%.
154	\item \textbf{Best F1.} At $1.5\times$, F1 = 85.7\%, the highest among all tested thresholds for B2. The single false positive (008e\_v3\_s2) is mechanistically identifiable as IRD rather than CIVO.
155	\item \textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\times$) add false positives without gaining true positives. Higher thresholds ($\geq 1.7\times$) sacrifice recall without eliminating the 008e\_v3\_s2 false positive (which requires $\tau > 3.78$).
156	\end{enumerate}
157	
158	For Task~B1 (sustained CIVO only), perfect classification is achievable at $\nve \geq 3.9\times$, but with only $n_{\text{pos}} = 2$ the statistical power is severely limited (accuracy 95\% CI: [63.1\%, 100\%]).
159	
160	\paragraph{Limitations.} With $n = 8$ experiments, all Clopper-Pearson confidence intervals are wide (e.g., 87.5\% accuracy has 95\% CI [47.3\%, 99.7\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds.
161	
162	% --- APPENDIX B: Factorial Ablation Details ---
163	
164	\section{Factorial Ablation Details}
165	\label{sec:appendix_factorial}
166	
167	This appendix provides the full factorial ablation results summarized in \S\ref{sec:f3f5_summary} of the main text.
168	
169	\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}
170	\label{sec:f3}
171	
172	\begin{figure}[t]
173	\centering
174	\includegraphics[width=\columnwidth]{figures/paper/fig3_factorial_grid.pdf}
175	\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}
176	\label{fig:factorial_grid}
177	\end{figure}
178	
179	The causal claim that trained embedding \emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.
180	
181	\paragraph{Evidence A: exposure is necessary (exp\_008a).}
182	Exp\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\_008d, its NVE remains in the $0.43$--$0.93\times$ range across 3 seeds (105K steps). Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\dt{>}1$ state predictions within the RSSM.
183	
184	This contrasts with exp\_006 (trained $e_{\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\times$ at 45K to $2.31\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\dt{>}1$ transitions during training, confirming that multi-rate data exposure, not embedding architecture, is the operative variable.
185	
186	\paragraph{Evidence B: trainability is necessary (exp\_015b).}
187	Exp\_015b uses a frozen random-projection embedding ($d{=}32$, \texttt{requires\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\_008d, but with a non-trainable temporal signal. Despite full exposure to $\dt{>}1$ transitions, the NVE peaks at $1.45\times$ at 55K but does not sustain escalation: it retreats to $0.65\times$ by 65K and settles at $0.55\times$ by 105K (trajectory: $0.81 \rightarrow 1.26 \rightarrow 1.45 \rightarrow 0.65 \rightarrow 1.05 \rightarrow 0.60 \rightarrow 0.59 \rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \S\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.
188	
189	The contrast with exp\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\times$ with sustained monotonic escalation ($1.78 \rightarrow 1.71 \rightarrow 2.09 \rightarrow 4.12$) and triggers full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\times$ before self-correcting to $0.55\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\dt$-embedding must be able to \emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.
190	
191	Together, these two controls establish that CIVO requires the \emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.
192	
193	Cross-environment validation on Cheetah Run replicates the causal pattern: trained $e_{\dt}$ triggers CIVO in both tested seeds (exp\_010b, 2 seeds, NVE $8.27$--$70.64\times$, collapse to 51.7/0.83) while removing the embedding eliminates it (exp\_024b, 2 seeds, NVE $<0.2\times$, eval 96.5/77.3). This extends the necessary-condition finding from Walker Walk to a second locomotion environment with qualitatively different dynamics (6-joint vs.\ 2-joint).
194	
195	\begin{table}[h]
196	\centering
197	\small
198	\caption{Causal isolation: $e_{\dt}$ configuration $\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}
199	\label{tab:causal_matrix}
200	\begin{tabular}{lcc}
201	\toprule
202	& Multi-rate data (\textsc{on}) & Single-rate data (\textsc{off}) \\
203	\midrule
204	Trained $e_{\dt}$ & exp\_008d: \textbf{CIVO} & exp\_008a: healthy \\
205	 & NVE 4.12$\times$, collapse & NVE 0.93$\times$ \\
206	\midrule
207	Frozen $e_{\dt}$ & exp\_015b: grad.\ starvation & --- \\
208	 & peak NVE 1.45$\times$ (transient) & \\
209	\midrule
210	Removed $e_{\dt}$ & exp\_008f: no CIVO & --- \\
211	 & NVE $\leq$0.97$\times$ & \\
212	\bottomrule
213	\end{tabular}
214	\end{table}
215	
216	Only the upper-left cell (trained embedding with multi-rate exposure) triggers CIVO (Table~\ref{tab:causal_matrix}). This 2$\times$2 structure establishes that both factors are jointly necessary.
217	
218	\subsection{F4: Degradation Scales Monotonically with \texorpdfstring{$\dt$}{dt}}
219	\label{sec:f4}
220	
221	\begin{figure}[t]
222	\centering
223	\includegraphics[width=\columnwidth]{figures/paper/fig5_dt_amplification.pdf}
224	\caption{Peak evaluation return as a function of imagination $\dt$. Performance degrades monotonically: $\dt{=}1$ (915.7) $>$ $\dt{=}2$ (485.3, $-47\%$) $>$ $\dt{=}4$ (176.9, $-81\%$).}
225	\label{fig:dt_amplification}
226	\end{figure}
227	
228	The magnitude of degradation scales monotonically with the imagination step size (Figure~\ref{fig:dt_amplification}). From the $\dt{=}1$ baseline (915.7 at 105K), fixed $\dt{=}2$ (exp\_006) achieves a peak of only 485.3 ($-47\%$), and fixed $\dt{=}4$ (exp\_007) peaks at 176.9 ($-81\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.
229	
230	\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}
231	\label{sec:f5}
232	
233	Neither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\nve < 0.93\times$ (\S\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\nve = 4.12\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\ 009c: 148.3) but neither exhibits $\nve > 1.5\times$, confirming that low evaluation alone does not indicate CIVO.
234	
235	The $3.2\times$ performance gap (008a: 777.7 vs.\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\leq$0.93$\times$).
236	
237	% --- APPENDIX C: Full Analysis & Discussion ---
238	
239	\section{Full Analysis \& Discussion}
240	\label{sec:appendix_analysis}
241	
242	This appendix provides the complete mechanistic analysis summarized in Section~\ref{sec:discussion} of the main text.
243	
244	\subsection{The CIVO Mechanism}
245	\label{sec:civo_mechanism}
246	
247	The RSSM fidelity analysis (Table~\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\dt{=}1$ is $0.0568$, while at $\dt{=}2$ it rises to $0.1579$, a $2.78\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\times$ gap, and the baseline shows $1.56\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.
248	
249	This asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\dt$-embedding causes RSSM predictions at $\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\nve$ above $1.5\times$, followed by evaluation collapse.
250	
251	A random-policy control experiment ($N{=}100$ rollouts, 95\% bootstrap CI) decomposes CIVO into two necessary stages.  \textbf{Stage~1 (dynamics bias):} even under a random policy, $\dt{=}2$ imagination produces $1.68\times$ higher mean reward than $\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\dt > 1$, independent of actor behavior.  \textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\times$ and the trained-actor ratio is $0.98\times$.  The decomposition attributes $\approx 36\%$ of the total effect to dynamics bias and $\approx 64\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.
252	
253	This mechanism is analogous to delusional bias \citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced: the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.
254	
255	\subsection{Selective Gradient Stopping and Gradient Decomposition}
256	\label{sec:sgs_gradient_analysis}
257	
258	\subsubsection{Gradient Decomposition Results}
259	\label{sec:gradient_decomposition}
260	
261	\begin{figure}[t]
262	\centering
263	\includegraphics[width=0.75\columnwidth]{figures/fig3_gradient_decomposition.pdf}
264	\caption{Gradient contribution to $e_{\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\%) yet reward-only SGS (exp\_016e) fails; the observation decoder channel (16--22\%) carries the critical $\dt$-specific spatial information that drives the RSSM fidelity gap.}
265	\label{fig:gradient_decomp}
266	\end{figure}
267	
268	Exp\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\times$. The SGS intervention neither prevented nor attenuated CIVO.
269	
270	To explain this null result, we performed a gradient decomposition analysis using \texttt{torch.autograd.grad} to measure each loss component's contribution to $\nabla_\theta e_{\Delta t}$, where $\theta$ denotes the temporal embedding parameters. Table~\ref{tab:gradient_decomposition} reports the results.
271	
272	\begin{table}[h]
273	\centering
274	\caption{Gradient contributions to the temporal embedding $e_{\Delta t}$ by loss component, measured via \texttt{torch.autograd.grad} with training configuration \texttt{gate\_fixed\_dt=2}. Gradient norms are $\ell_2$ norms of $\nabla_\theta \mathcal{L}_i$ for each loss $\mathcal{L}_i$.}
275	\label{tab:gradient_decomposition}
276	\small
277	\begin{tabular}{lrrrr}
278	\toprule
279	& \multicolumn{2}{c}{\textbf{@55K}} & \multicolumn{2}{c}{\textbf{@112K}} \\
280	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
281	Loss component & Share & (\%) & Share & (\%) \\
282	\midrule
283	Reward head & --- & 49.0 & --- & 38.1 \\
284	KL dynamics & --- & 34.7 & --- & 40.4 \\
285	Observation decoders & --- & 16.3 & --- & 21.5 \\
286	\bottomrule
287	\end{tabular}
288	\end{table}
289	
290	The gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\% at 55K, 38.1\% at 112K), yet reward-only SGS (exp\_016e) fails catastrophically (NVE $10.42\times$). The observation decoder channel contributes the smallest share (16.3\% at 55K, 21.5\% at 112K) yet carries the critical $\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.
291	
292	The gradient structure is relatively stable across training (reward shifts from 49\% to 38\%, obs from 16\% to 22\%, KL from 35\% to 40\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.
293	
294	\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\times$ reward MAE ratio, Table~\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\Delta t}$, though its 50\% recovery rate (1/2 seeds) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.
295	
296	\subsubsection{Implications for the CIVO Mechanism}
297	\label{sec:sgs_implications}
298	
299	The gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.
300	
301	\paragraph{Gradient importance $\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\%) to $e_{\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\dt$-specific structural information: it adjusts $e_{\Delta t}$ to minimize a scalar prediction error that is largely $\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\Delta t}$ learns scale-dependent latent biases.
302	
303	\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\_016e (NVE $10.42\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\_018) detaches $e_{\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.
304	
305	Cross-environment validation on Cheetah Run (exp\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\times$ at 45K (comparable to the unmitigated exp\_010b's $8.27\times$).  However, unlike exp\_010b, which collapsed permanently to eval 51.7, exp\_021 self-corrected within ${\sim}$10K steps, with sustained NVE dropping to $0.34\times$ (55K--105K) and final evaluation recovering to 221.5.  This pattern reframes Full-SGS as \emph{enabling recovery from CIVO} rather than preventing its onset: the gradient detachment constrains value growth after the transient spike, allowing the critic to recalibrate.  Performance nonetheless remains at 38.7\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\_018's mixed Walker results (1/2 seeds), these findings indicate that gradient-level interventions alone do not fully eliminate the CIVO vulnerability, and that additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.
306	
307	\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\_008d) shows a $2.78\times$ reward gap between $\Delta t{=}1$ and $\Delta t{=}2$ transitions (Table~\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\Delta t}$ to produce latent states that are spatially biased at $\dt{>}1$, and the reward head inherits these biases \textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\Delta t}$'s parameters but not causal responsibility for the fidelity gap.
308	
309	\subsubsection{Entropy Dynamics Across Configurations}
310	\label{sec:entropy_dynamics}
311	
312	\begin{figure}[h]
313	\centering
314	\includegraphics[width=0.85\columnwidth]{figures/fig4_entropy_dynamics.pdf}
315	\caption{Actor entropy trajectories for three configurations. All start at ${\sim}8$ nats and converge to similar values (${\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}
316	\label{fig:entropy_dynamics}
317	\end{figure}
318	
319	\subsubsection{Exp\_016e Reinterpreted as Stochastic Variation}
320	\label{sec:016e_reinterp}
321	
322	The gradient decomposition establishes that exp\_016e targets the largest gradient pathway (reward: 38--49\%) but not the informationally critical one (observation decoders: 16--22\%).  The apparent timing differences between exp\_016e and exp\_008d (later collapse onset, 75K vs.\ 25K, and higher peak evaluation, 326.7 vs.\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\_008d, exp\_009b, exp\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\times$ pathological threshold at some point during training.
323	
324	\subsection{Post-CIVO Outcomes: Why Seeds Diverge}
325	\label{sec:seed_divergence}
326	
327	\begin{table}[h]
328	\centering
329	\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window.}
330	\label{tab:post_civo}
331	\footnotesize
332	\setlength{\tabcolsep}{3pt}
333	\begin{tabular}{lcccl}
334	\toprule
335	\textbf{Seed} & \textbf{Peak} & \textbf{Final} & \textbf{Eval} & \textbf{Outcome} \\
336	\midrule
337	s1 (008d) & 4.12$\times$ & 4.12$\times$ & 82.8 & Full collapse \\
338	s2 (009b) & 1.62$\times$ & 0.38$\times$ & 267.9 & Transient CIVO \\
339	\bottomrule
340	\end{tabular}
341	\end{table}
342	
343	The two post-CIVO outcomes (Table~\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\nve > 1.5\times$ threshold, yet the downstream damage is stochastic.\footnote{Exp\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control, confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).
344	
345	\subsection{Why MPC Is Immune}
346	\label{sec:mpc_immune}
347	
348	\citet{nhu2025tawm} show that $\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\dt > 1$ is amplified through the closed actor-critic loop.
349	
350	\subsection{The \texorpdfstring{$\dt$}{dt}-Embedding Dilemma}
351	\label{sec:embedding_dilemma}
352	
353	The factorial results reveal a fundamental tension: removing the $\dt$-embedding (008f) eliminates CIVO but at a $13\times$ cost to reward prediction quality ($0.7469$ vs.\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\dt{=}1$ while retaining the trained embedding (008e\_v3) avoids CIVO in 1 of 2 seeds but the other collapses via Pathway~B (\S\ref{sec:f6}).  Neither approach alone provides a complete solution.
354	
355	\subsection{Multiple Vulnerability Pathways}
356	\label{sec:pathways}
357	
358	The two collapse mechanisms identified in \S\ref{sec:f6}, CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing), have distinct diagnostic signatures but a shared root cause: the trained $\dt$-embedding's learned features affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B).  This explains why $\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\times$ for 008e\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse.
359	
360	\subsection{Implications for Temporal Abstraction in World Models}
361	\label{sec:implications}
362	
363	CIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \citep{gumbsch2024thick}, Hieros \citep{mattes2024hieros}, LS-Imagine \citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.
364	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "7426cf44-c638-4fab-a607-3595e958adc2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 24 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 3.03$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.43$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.51$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & No collapse \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 70.64$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Recovery \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\par}\n\\end{table*}\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eight factorial experiments. Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.84 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.13 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.13\\times$, exp~008d) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.13]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.933$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=2$, $n_{\\text{neg}}=6$, $n=8$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). Thresholds 1.2$\\times$/1.5$\\times$ and 1.7$\\times$/2.0$\\times$ yield identical operating points (no NVE values in those intervals). $^\\dagger$Optimal threshold in $(3.78, 4.13]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 2 & 3 & 0 & 3 & 62.5\\% \\; [24.5, 91.5] & 40.0\\% & 100\\% & 57.1\\% \\\\\n$\\geq 1.2\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.5\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 2 & 0 & 0 & 6 & 100\\% \\; [63.1, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=5$, $n=8$, $\\text{AUROC}=0.933$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 2 & 0 & 3 & 75.0\\% \\; [34.9, 96.8] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.2\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 1.7\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 3.9\\times$ & 2 & 0 & 1 & 5 & 87.5\\% \\; [47.3, 99.7] & 100\\% & 66.7\\% & 80.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all three CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 66.7\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 85.7\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 2$ the statistical power is severely limited (accuracy 95\\% CI: [63.1\\%, 100\\%]).\n\n\\paragraph{Limitations.} With $n = 8$ experiments, all Clopper-Pearson confidence intervals are wide (e.g., 87.5\\% accuracy has 95\\% CI [47.3\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.43$--$0.93\\times$ range across 3 seeds (105K steps). Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training, confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.55\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.60 \\rightarrow 0.59 \\rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and triggers full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.55\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\nCross-environment validation on Cheetah Run replicates the causal pattern: trained $e_{\\dt}$ triggers CIVO in both tested seeds (exp\\_010b, 2 seeds, NVE $8.27$--$70.64\\times$, collapse to 51.7/0.83) while removing the embedding eliminates it (exp\\_024b, 2 seeds, NVE $<0.2\\times$, eval 96.5/77.3). This extends the necessary-condition finding from Walker Walk to a second locomotion environment with qualitatively different dynamics (6-joint vs.\\ 2-joint).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$, confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced: the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 50\\% recovery rate (1/2 seeds) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.\n\nCross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This pattern reframes Full-SGS as \\emph{enabling recovery from CIVO} rather than preventing its onset: the gradient detachment constrains value growth after the transient spike, allowing the critic to recalibrate.  Performance nonetheless remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's mixed Walker results (1/2 seeds), these findings indicate that gradient-level interventions alone do not fully eliminate the CIVO vulnerability, and that additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe two post-CIVO outcomes (Table~\\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\\nve > 1.5\\times$ threshold, yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control, confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) avoids CIVO in 1 of 2 seeds but the other collapses via Pathway~B (\\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse mechanisms identified in \\S\\ref{sec:f6}, CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing), have distinct diagnostic signatures but a shared root cause: the trained $\\dt$-embedding's learned features affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B).  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse.\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.\n",
      "numLines": 364,
      "startLine": 1,
      "totalLines": 364
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_013Wvn9qLX3oDsaypDA1pmgH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "003771a2-1773-4e8a-90b0-593d5d262c31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJDsxhhooqcA3aFgoJqmJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 25723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 891
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

_source line 22 · 2026-05-18T11:35:11.651Z_

<details><summary>↩ Tool result · `toolu_013Wvn9qLX3oDsaypDA1pmgH`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{Key configurations and outcomes. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 24 configurations in Table~\ref{tab:complete_results}.}
13	\label{tab:main_results}
14	\footnotesize
15	\setlength{\tabcolsep}{4pt}
16	\begin{tabular}{llcccccl}
17	\toprule
18	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
19	\midrule
20	001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
21	\midrule
22	\rowcolor{gray!15}
23	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
24	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
25	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
26	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
27	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
28	\midrule
29	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
30	\rowcolor{gray!15}
31	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
32	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
33	\bottomrule
34	\end{tabular}
35	\vspace{1pt}
36	{\raggedright\footnotesize
37	trn = trained ($d{=}32$, subsample ON);
38	exp$^a$ = trained, subsample OFF;
39	frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
40	--- = removed ($d{=}0$).\\
41	$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).\par}
42	\end{table*}
43	
44	%% ============================================================
45	%% F1: All dt>1 degrade
46	%% ============================================================
47	
48	\subsection{F1: All Variable-Rate Configurations Degrade}
49	\label{sec:f1}
50	
51	Every configuration that introduces $\dt > 1$ imagination degrades relative to the $\dt{=}1$ baseline (Figure~\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\%$ of baseline); fixed $\dt{=}4$ (007) never exceeds 176.9 ($19\%$); the learned gate (005) collapses to 98.8 ($11\%$).
52	
53	\begin{figure}[t]
54	\centering
55	\includegraphics[width=0.65\columnwidth]{figures/paper/fig1_learning_curves.pdf}
56	\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}
57	\label{fig:learning_curves}
58	\end{figure}
59	
60	%% ============================================================
61	%% F2: Trained dt_embedding → nve > 1.5x
62	%% ============================================================
63	
64	\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}
65	\label{sec:f2}
66	
67	The factorial design isolates trained $\dt$-embedding as the causal trigger. Comparing exp\_008d (trained, subsample ON) against exp\_008f (no embedding, subsample ON): 008d reaches $\nve = 4.12\times$ and collapses (eval 82.8), while 008f maintains $\nve \leq 0.97\times$ (eval 503.0). The $\nve \geq 1.5\times$ threshold (35K+ window) correctly classifies 13 of 14 experimental configurations across two environments (AUROC${=}0.933$; Figure~\ref{fig:nve_trajectory}).\footnote{Excluding 3 baseline configurations, the 10-experiment subset yields accuracy$\,{=}\,$9/10 and AUROC$\,{=}\,$0.880.}
68	
69	\begin{figure}[t]
70	\centering
71	\includegraphics[width=0.65\columnwidth]{figures/fig1_nve_trajectory.pdf}
72	\caption{NVE trajectories (mean $\pm$ seed range). Trained $\dt$-embedding (red, Walker Walk, $n{=}3$ seeds plotted; seed~4 data in Table~\ref{tab:complete_results}) exceeds the $1.5\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}
73	\label{fig:nve_trajectory}
74	\end{figure}
75	
76	The trained $\dt$-embedding triggers CIVO in all four Walker Walk seeds (peak NVE: $4.12\times$, $3.03\times$, $1.62\times$, $1.53\times$; all $\geq 1.5\times$ threshold), universally degrading performance to below 30\% of baseline (mean eval 170.6, 18.6\% of baseline). Downstream trajectories diverge: seeds~1 and~4 (008d, 008d\_s4) undergo full collapse (eval 82.8 and 63.6), seed~3 (008d\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 29.3\% of baseline). Combined with Cheetah Run validation (\S\ref{sec:f6}), CIVO onset is universal across all six tested seeds ($n{=}6$, two environments): collapse is the majority outcome (5/6 seeds) with variable onset timing (35K to 85K steps). The 1/6 self-correction case (Walker seed~2) remains severely degraded. This confirms that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\ref{sec:seed_divergence}).
77	
78	%% ============================================================
79	%% F3--F5: Summary (details in Appendix B)
80	%% ============================================================
81	
82	\subsection{F3--F5: Factorial Ablation (Appendix~\ref{sec:appendix_factorial})}
83	\label{sec:f3f5_summary}
84	
85	Trained $\dt$-embedding and multi-rate data exposure are \emph{jointly necessary} for CIVO. Neither factor alone triggers pathological overestimation: trained embedding without multi-rate exposure (008a, 3 seeds, NVE $0.43$--$0.93\times$, eval 631--899, 3/3 no CIVO) and multi-rate exposure without embedding (008f, NVE $= 0.97\times$) both remain well below the $1.5\times$ diagnostic threshold, while frozen embedding under full exposure (015b) peaks near the diagnostic threshold ($1.45\times$ at 55K) but retreats to $0.55\times$ by 105K; frozen embedding thus prevents the sustained escalation characteristic of CIVO (Figure~\ref{fig:factorial_grid}). Degradation scales monotonically with $\dt$ ($-47\%$ at $\dt{=}2$, $-81\%$ at $\dt{=}4$; Figure~\ref{fig:dt_amplification}).
86	
87	%% ============================================================
88	%% F6--F7: Interventions and cross-environment
89	%% ============================================================
90	
91	\subsection{F6--F7: Interventions and Multiple Pathways}
92	\label{sec:f6}
93	
94	\paragraph{F6: $\dt{=}1$ imagination does not prevent all collapse.}
95	Exp\_008e\_v3 restricts imagination to $\dt{=}1$ while retaining the trained embedding. Seed~1 is healthy (eval 869.9, $\nve = 0.94\times$); seed~2 collapses (eval $715 \rightarrow 137$, $\nve = 3.78\times$), but via a qualitatively distinct mechanism (Figure~\ref{fig:multiple_pathways}). Classic CIVO (008d, Pathway~A) shows value explosion followed by evaluation decline with decreasing entropy; 008e\_v3\_s2 (Pathway~B) shows evaluation crash with \emph{increasing} entropy ($-5.21 \rightarrow -3.83$) while values remain stable. This produces the sole false positive in the NVE classification.
96	
97	\begin{figure}[t]
98	\centering
99	\includegraphics[width=0.65\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}
100	\caption{Contrasting collapse dynamics. \textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \textbf{Right:} 008e\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}
101	\label{fig:multiple_pathways}
102	\end{figure}
103	
104	\paragraph{F7: Full-pathway gradient stopping shows mixed results.}
105	Exp\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\dt}$; this blocks the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\dt$-embedding alone produces $-73\%$ peak and $-86\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \sgseval{}, $-51\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\%$); the overall recovery rate is 50\%. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable elimination. Reward-only SGS (016e) fails entirely (NVE $10.42\times$). Cross-environment validation on Cheetah Run (010b, 2 seeds) confirms CIVO generalization: both seeds collapse (peak NVE $8.27\times$ and $70.64\times$, final eval 51.7 and 0.83 at 105K). Full-SGS on Cheetah Run enables recovery from transient CIVO onset (NVE $9.94\times$ at 45K, eval 4.6) to functional performance (eval 221.5 at 105K), in contrast to permanent collapse without SGS (010b: eval 51.7, 0.83 across 2 seeds). Combined with Walker results (50\% recovery rate), SGS is necessary but not sufficient for CIVO elimination. Removing the embedding on Cheetah eliminates CIVO entirely (024b, 2 seeds, NVE $< 0.2\times$, eval 96.5/77.3), replicating the Walker causal control (008f) in a second environment.
106	
107	\begin{figure}[t]
108	\centering
109	\includegraphics[width=0.75\columnwidth]{figures/fig2_civo_decomposition.pdf}
110	\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \textbf{Trained dt-emb} (008d)\footnotemark: DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data. \textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\dt}$, two seeds. Trained $\dt$-embedding degrades peak eval by $73\%$ and final eval by $86\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\%$ final, no collapse) but seed~2 collapses ($-96\%$ final, marked ``collapsed''), indicating that SGS enables recovery from CIVO in some seeds but is not sufficient for reliable prevention (recovery rate $= 50\%$). All percentages relative to Baseline 001.}
111	\label{fig:civo_decomposition}
112	\end{figure}
113	\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}
114	
115	%% ============================================================
116	%% TABLE 2: RSSM Fidelity
117	%% ============================================================
118	
119	\begin{table}[t]
120	\centering
121	\caption{RSSM fidelity at $\dt{=}1$ vs.\ $\dt{=}2$. Trained embedding (008d) produces $2.78\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}
122	\label{tab:rssm_fidelity}
123	\footnotesize
124	\setlength{\tabcolsep}{4pt}
125	\begin{tabular}{lcccccc}
126	\toprule
127	& \multicolumn{3}{c}{\textbf{obs\_MSE}} & \multicolumn{3}{c}{\textbf{reward\_MAE}} \\
128	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
129	\textbf{Config} & $\dt{=}1$ & $\dt{=}2$ & Gap & $\dt{=}1$ & $\dt{=}2$ & Gap \\
130	\midrule
131	Baseline & 13.49 & 27.50 & 2.04$\times$ & 0.0102 & 0.0159 & 1.56$\times$ \\
132	008d (trained) & 41.31 & 53.67 & 1.30$\times$ & 0.0568 & 0.1579 & 2.78$\times$ \\
133	008f (no emb) & 8.01 & 22.04 & 2.75$\times$ & 0.7469 & 0.7526 & 1.01$\times$ \\
134	\bottomrule
135	\end{tabular}
136	\end{table}
137	
138	The trained embedding in 008d produces a $2.78\times$ reward prediction gap between $\dt{=}1$ and $\dt{=}2$ (Table~\ref{tab:rssm_fidelity}). This systematic bias is internalized by the critic as optimistic value estimates. Having established the mechanistic basis of CIVO, we now ask whether it can be detected during training without access to a reference baseline.
139	
140	%% ============================================================
141	%% F8: Online CIVO Detection
142	%% ============================================================
143	
144	\subsection{Online CIVO Detection}
145	\label{sec:detector}
146	
147	\paragraph{Motivation.}
148	The Normalized Value Excess ($\nve$) quantifies CIVO severity by comparing the value-to-evaluation ratio against a reference baseline that does not employ temporal abstraction. This comparison is informative for post-hoc diagnosis but unusable during deployment: no practitioner has access to a converged baseline run while training a new agent. A metric that requires a completed control experiment cannot serve as an early warning.
149	
150	We therefore ask whether the \emph{dynamics} of value overestimation, rather than its absolute magnitude relative to an external reference, contain sufficient signal to detect CIVO onset in real time. By tracking the trajectory of the value-to-evaluation ratio $r_t = \bar{V}_t / \max(\bar{E}_t, \varepsilon)$ (with $\varepsilon = 10^{-6}$ for numerical stability) across checkpoints, a lightweight rule-based detector can flag dangerous overestimation using only quantities available within a single run.
151	
152	The causal structure of CIVO motivates acceleration as the key detection signal. CIVO operates as a positive feedback loop: the trained embedding biases reward predictions, which inflate value estimates, which in turn distort actor gradients toward trajectories that reinforce the bias (\S\ref{sec:civo_mechanism}). This self-amplifying cycle produces superlinear growth in $r_t$. In healthy training, a natural negative feedback counteracts value growth: improved value estimates yield a better actor, which raises evaluation returns and stabilizes the ratio. CIVO breaks this negative feedback, so sustained positive acceleration in $r_t$ serves as a causal signature that distinguishes pathological divergence from normal value learning.
153	
154	\paragraph{Algorithm.}
155	The detector monitors $r_t$ and fires an alert only when four conditions hold simultaneously at checkpoint $t$ (Algorithm~\ref{alg:civo_detector}). The conjunction makes the detector conservative: any single noisy checkpoint is unlikely to satisfy magnitude, velocity, acceleration, and decline together. The computational cost is negligible (four scalar comparisons per checkpoint, no additional model inference).
156	
157	\begin{algorithm}[t]
158	\caption{Online CIVO Detector}
159	\label{alg:civo_detector}
160	\begin{algorithmic}[1]
161	\REQUIRE Stream of $(\bar{V}_t, \bar{E}_t)$ at each checkpoint $t$
162	\STATE $\tau_\text{mag} \leftarrow 0.49$, \quad $\tau_\text{vel} \leftarrow 0.1$, \quad $\varepsilon \leftarrow 10^{-6}$
163	\STATE Initialize $r_\text{prev} \leftarrow 0$, $\Delta r_\text{prev} \leftarrow 0$, $\mathcal{H} \leftarrow []$
164	\FOR{each checkpoint $t$}
165	  \STATE $r_t \leftarrow \bar{V}_t \,/\, \max(\bar{E}_t,\, \varepsilon)$
166	  \STATE $\Delta r_t \leftarrow r_t - r_\text{prev}$
167	  \STATE $c_\text{mag} \leftarrow (r_t \geq \tau_\text{mag})$
168	  \STATE $c_\text{vel} \leftarrow (\Delta r_t > \tau_\text{vel})$
169	  \STATE $c_\text{acc} \leftarrow (\Delta r_\text{prev} > \tau_\text{vel}) \wedge (\Delta r_t > \Delta r_\text{prev})$
170	  \STATE $c_\text{dec} \leftarrow \bigl|\{i : \mathcal{H}[i] < \mathcal{H}[i{-}1],\; i \in \text{last 3}\}\bigr| \geq 2$
171	  \IF{$c_\text{mag} \wedge c_\text{vel} \wedge c_\text{acc} \wedge c_\text{dec}$}
172	    \STATE \textbf{Alert:} CIVO onset at step $t$
173	  \ENDIF
174	  \STATE $r_\text{prev} \leftarrow r_t$, \quad $\Delta r_\text{prev} \leftarrow \Delta r_t$
175	  \STATE Append $\bar{E}_t$ to $\mathcal{H}$
176	\ENDFOR
177	\end{algorithmic}
178	\end{algorithm}
179	
180	The four conditions capture complementary signals: (1)~\emph{Magnitude} ($r_t \geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\emph{Velocity} ($\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\emph{Acceleration} ($\Delta r_t > \Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths where the ratio rises and falls without sustained divergence; (4)~\emph{Evaluation decline} ($\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A 2-of-3 majority threshold balances noise robustness against single-checkpoint evaluation variance with sensitivity to sustained decline.\footnote{A full comparison of window sizes (3/3, 2/3, 2/5) and their trade-offs appears in Appendix~\ref{sec:appendix_sensitivity}.}
181	
182	Sensitivity analysis over $\tau_\text{mag} \in [0.30, 0.70]$ confirms that $\tau_\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives, since both false alarms have $r_t > 0.70$ at trigger time. The velocity threshold $\tau_\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $5/5$); we retain $0.1$ to avoid overfitting to $n{=}13$ runs.
183	
184	\paragraph{Validation.}
185	We apply the detector retrospectively to thirteen runs: trained duration embedding with sustained overestimation (CIVO-positive, $n{=}5$), untrained or absent embedding (CIVO-negative, $n{=}3$), vanilla baselines ($n{=}4$), and one cross-simulator case (PickCube-v1 in ManiSkill3, trained embedding). Ground truth labels derive from manual inspection: a run is CIVO-positive if it exhibits sustained $\nve \geq 1.5\times$ with subsequent evaluation collapse. Table~\ref{tab:detector-validation} reports all results.
186	
187	\begin{table}[t]
188	\centering
189	\caption{Retrospective CIVO detector validation ($n{=}13$). Detection type: ``predictive'' = alert precedes 20\% eval decline; ``reactive'' = alert follows decline onset.}
190	\label{tab:detector-validation}
191	\footnotesize
192	\setlength{\tabcolsep}{3pt}
193	\begin{tabular}{llccccc}
194	\toprule
195	\textbf{Exp} & \textbf{Config} & \textbf{Verdict} & \textbf{Trigger} & \textbf{Type} & \textbf{Peak Eval} & $r_\text{ve}$ \\
196	\midrule
197	008d s0 & trained $\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\
198	010b & trained $\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\
199	008d s3 & trained $\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\
200	008d s4 & trained $\dt$-emb & TP & 105K & reactive & 383 & 3.03 \\
201	010b s0 & trained $\dt$-emb (Cheetah) & TP & 95K & reactive & 248 & 6.34 \\
202	\midrule
203	008f s3 & no $\dt$-emb & TN & -- & -- & 594 & -- \\
204	009b s2 & trained $\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\
205	baseline s1 & vanilla & TN & -- & -- & 970 & -- \\
206	009d s0 & vanilla & TN & -- & -- & 951 & -- \\
207	009d s1 & vanilla & TN & -- & -- & 920 & -- \\
208	019b & trained $\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\
209	\midrule
210	009c s2 & no $\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\
211	009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\
212	\midrule
213	\multicolumn{7}{l}{TPR = 5/5 (1.00), \quad FPR = 2/8 (0.25)} \\
214	\bottomrule
215	\end{tabular}
216	\end{table}
217	
218	\paragraph{Results.}
219	The detector identifies all five CIVO-positive runs (TPR = 5/5). Two of five are detected \emph{predictively}: 008d seed~0 triggers at 45K, one checkpoint before evaluation crosses the 20\% decline threshold; seed~3 triggers at 45K, a full 50K steps before decline begins. The remaining three cases trigger reactively: 010b seed~1 (Cheetah Run, 65K) involves single-step collapse; 008d seed~4 (105K) and 010b seed~0 (Cheetah Run, 95K) fire after sustained decline is already underway.
220	
221	Two false positives occur among eight negative cases (FPR = 2/8, precision = 5/7 = 0.71, F$_1$ = 0.83). Run 009c (no duration embedding) develops genuine late-stage value overestimation unrelated to CIVO; the detector correctly identifies value-performance dissociation, and the alert is arguably useful despite the label mismatch. Run 009a (vanilla baseline) triggers during a transient three-checkpoint eval dip at 85K; the model subsequently recovers to 966, constituting a pure false alarm. In practice, the cost of a false alert (manual checkpoint inspection, minutes) is orders of magnitude lower than the cost of undetected collapse (wasted GPU-hours, corrupted model); moderate FPR is therefore acceptable in this application.
222	
223	The three earliest true positives triggered before 65K steps (range 45--65K), while the two additional cases (008d s4, 010b s0) triggered later (95--105K), overlapping with the false positive range (85--105K). Early-training alerts (before 70K) carry higher diagnostic confidence; later alerts warrant manual inspection regardless of ground truth.
224	
225	\paragraph{Cross-simulator specificity (PickCube).}
226	Exp\_019b applies the CIVO-trigger configuration (trained $\dt$-embedding, subsample ON, $H{=}8$) to PickCube-v1 in ManiSkill3, a manipulation task with sparse rewards and qualitatively different dynamics from DMC locomotion. The V/E ratio exhibits an oscillatory pattern rather than monotonic divergence: it spikes to $r_t = 5.66$ at 52.5K (eval crashes from 24.9 to 3.7), then deflates to 1.38 by 72.5K as value estimates self-correct, eventually reaching 0.065$\times$ NVE at 202.5K. This spike-then-deflation trajectory prevents the acceleration condition from co-occurring with evaluation decline at any single checkpoint. When V/E accelerates during early training (22.5--32.5K, consecutive velocities $+0.50$, $+1.85$), evaluation has not yet declined (C4 fails). When evaluation does decline (42.5--52.5K), the preceding V/E velocity is negative ($-0.81$), so the acceleration condition (C3) fails. Across all 14 checkpoints evaluated through 132.5K, no checkpoint satisfies all four conditions simultaneously, and the detector correctly remains silent (TN). This confirms that the acceleration filter distinguishes transient overestimation spikes from the sustained monotonic divergence characteristic of CIVO. The result extends the detector's specificity validation to a second simulator and a sparse-reward manipulation domain.
227	
228	\paragraph{Limitations.}
229	Four constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse (the source of the 009a false alarm). Second, the acceleration condition assumes monotonically increasing overestimation during onset; oscillatory trajectories that eventually collapse could evade detection until acceleration stabilizes. Third, the detector identifies a \emph{pattern} (rising value-evaluation ratio with declining performance) rather than a \emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values ($\tau_\text{mag} = 0.49$, $\tau_\text{vel} = 0.1$) were calibrated on thirteen runs across three environments; generalization to different reward scales requires further validation. The detector targets sustained CIVO patterns; transient single-checkpoint spikes (as observed in SGS-protected runs) are by design not flagged, as they do not indicate impending permanent collapse.
230	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "98bb6398-2773-41f9-8bfc-736df52e3e2e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$, \\S\\ref{sec:metrics}).\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{Key configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 24 configurations in Table~\\ref{tab:complete_results}.}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the causal trigger. Comparing exp\\_008d (trained, subsample ON) against exp\\_008f (no embedding, subsample ON): 008d reaches $\\nve = 4.12\\times$ and collapses (eval 82.8), while 008f maintains $\\nve \\leq 0.97\\times$ (eval 503.0). The $\\nve \\geq 1.5\\times$ threshold (35K+ window) correctly classifies 13 of 14 experimental configurations across two environments (AUROC${=}0.933$; Figure~\\ref{fig:nve_trajectory}).\\footnote{Excluding 3 baseline configurations, the 10-experiment subset yields accuracy$\\,{=}\\,$9/10 and AUROC$\\,{=}\\,$0.880.}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{NVE trajectories (mean $\\pm$ seed range). Trained $\\dt$-embedding (red, Walker Walk, $n{=}3$ seeds plotted; seed~4 data in Table~\\ref{tab:complete_results}) exceeds the $1.5\\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding triggers CIVO in all four Walker Walk seeds (peak NVE: $4.12\\times$, $3.03\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 170.6, 18.6\\% of baseline). Downstream trajectories diverge: seeds~1 and~4 (008d, 008d\\_s4) undergo full collapse (eval 82.8 and 63.6), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 29.3\\% of baseline). Combined with Cheetah Run validation (\\S\\ref{sec:f6}), CIVO onset is universal across all six tested seeds ($n{=}6$, two environments): collapse is the majority outcome (5/6 seeds) with variable onset timing (35K to 85K steps). The 1/6 self-correction case (Walker seed~2) remains severely degraded. This confirms that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Factorial Ablation (Appendix~\\ref{sec:appendix_factorial})}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly necessary} for CIVO. Neither factor alone triggers pathological overestimation: trained embedding without multi-rate exposure (008a, 3 seeds, NVE $0.43$--$0.93\\times$, eval 631--899, 3/3 no CIVO) and multi-rate exposure without embedding (008f, NVE $= 0.97\\times$) both remain well below the $1.5\\times$ diagnostic threshold, while frozen embedding under full exposure (015b) peaks near the diagnostic threshold ($1.45\\times$ at 55K) but retreats to $0.55\\times$ by 105K; frozen embedding thus prevents the sustained escalation characteristic of CIVO (Figure~\\ref{fig:factorial_grid}). Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).\n\n%% ============================================================\n%% F6--F7: Interventions and cross-environment\n%% ============================================================\n\n\\subsection{F6--F7: Interventions and Multiple Pathways}\n\\label{sec:f6}\n\n\\paragraph{F6: $\\dt{=}1$ imagination does not prevent all collapse.}\nExp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained embedding. Seed~1 is healthy (eval 869.9, $\\nve = 0.94\\times$); seed~2 collapses (eval $715 \\rightarrow 137$, $\\nve = 3.78\\times$), but via a qualitatively distinct mechanism (Figure~\\ref{fig:multiple_pathways}). Classic CIVO (008d, Pathway~A) shows value explosion followed by evaluation decline with decreasing entropy; 008e\\_v3\\_s2 (Pathway~B) shows evaluation crash with \\emph{increasing} entropy ($-5.21 \\rightarrow -3.83$) while values remain stable. This produces the sole false positive in the NVE classification.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nExp\\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\\dt}$; this blocks the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\\dt$-embedding alone produces $-73\\%$ peak and $-86\\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \\sgseval{}, $-51\\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\\%$); the overall recovery rate is 50\\%. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable elimination. Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b, 2 seeds) confirms CIVO generalization: both seeds collapse (peak NVE $8.27\\times$ and $70.64\\times$, final eval 51.7 and 0.83 at 105K). Full-SGS on Cheetah Run enables recovery from transient CIVO onset (NVE $9.94\\times$ at 45K, eval 4.6) to functional performance (eval 221.5 at 105K), in contrast to permanent collapse without SGS (010b: eval 51.7, 0.83 across 2 seeds). Combined with Walker results (50\\% recovery rate), SGS is necessary but not sufficient for CIVO elimination. Removing the embedding on Cheetah eliminates CIVO entirely (024b, 2 seeds, NVE $< 0.2\\times$, eval 96.5/77.3), replicating the Walker causal control (008f) in a second environment.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d)\\footnotemark: DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS enables recovery from CIVO in some seeds but is not sufficient for reliable prevention (recovery rate $= 50\\%$). All percentages relative to Baseline 001.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe trained embedding in 008d produces a $2.78\\times$ reward prediction gap between $\\dt{=}1$ and $\\dt{=}2$ (Table~\\ref{tab:rssm_fidelity}). This systematic bias is internalized by the critic as optimistic value estimates. Having established the mechanistic basis of CIVO, we now ask whether it can be detected during training without access to a reference baseline.\n\n%% ============================================================\n%% F8: Online CIVO Detection\n%% ============================================================\n\n\\subsection{Online CIVO Detection}\n\\label{sec:detector}\n\n\\paragraph{Motivation.}\nThe Normalized Value Excess ($\\nve$) quantifies CIVO severity by comparing the value-to-evaluation ratio against a reference baseline that does not employ temporal abstraction. This comparison is informative for post-hoc diagnosis but unusable during deployment: no practitioner has access to a converged baseline run while training a new agent. A metric that requires a completed control experiment cannot serve as an early warning.\n\nWe therefore ask whether the \\emph{dynamics} of value overestimation, rather than its absolute magnitude relative to an external reference, contain sufficient signal to detect CIVO onset in real time. By tracking the trajectory of the value-to-evaluation ratio $r_t = \\bar{V}_t / \\max(\\bar{E}_t, \\varepsilon)$ (with $\\varepsilon = 10^{-6}$ for numerical stability) across checkpoints, a lightweight rule-based detector can flag dangerous overestimation using only quantities available within a single run.\n\nThe causal structure of CIVO motivates acceleration as the key detection signal. CIVO operates as a positive feedback loop: the trained embedding biases reward predictions, which inflate value estimates, which in turn distort actor gradients toward trajectories that reinforce the bias (\\S\\ref{sec:civo_mechanism}). This self-amplifying cycle produces superlinear growth in $r_t$. In healthy training, a natural negative feedback counteracts value growth: improved value estimates yield a better actor, which raises evaluation returns and stabilizes the ratio. CIVO breaks this negative feedback, so sustained positive acceleration in $r_t$ serves as a causal signature that distinguishes pathological divergence from normal value learning.\n\n\\paragraph{Algorithm.}\nThe detector monitors $r_t$ and fires an alert only when four conditions hold simultaneously at checkpoint $t$ (Algorithm~\\ref{alg:civo_detector}). The conjunction makes the detector conservative: any single noisy checkpoint is unlikely to satisfy magnitude, velocity, acceleration, and decline together. The computational cost is negligible (four scalar comparisons per checkpoint, no additional model inference).\n\n\\begin{algorithm}[t]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths where the ratio rises and falls without sustained divergence; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A 2-of-3 majority threshold balances noise robustness against single-checkpoint evaluation variance with sensitivity to sustained decline.\\footnote{A full comparison of window sizes (3/3, 2/3, 2/5) and their trade-offs appears in Appendix~\\ref{sec:appendix_sensitivity}.}\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives, since both false alarms have $r_t > 0.70$ at trigger time. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $5/5$); we retain $0.1$ to avoid overfitting to $n{=}13$ runs.\n\n\\paragraph{Validation.}\nWe apply the detector retrospectively to thirteen runs: trained duration embedding with sustained overestimation (CIVO-positive, $n{=}5$), untrained or absent embedding (CIVO-negative, $n{=}3$), vanilla baselines ($n{=}4$), and one cross-simulator case (PickCube-v1 in ManiSkill3, trained embedding). Ground truth labels derive from manual inspection: a run is CIVO-positive if it exhibits sustained $\\nve \\geq 1.5\\times$ with subsequent evaluation collapse. Table~\\ref{tab:detector-validation} reports all results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}13$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n008d s4 & trained $\\dt$-emb & TP & 105K & reactive & 383 & 3.03 \\\\\n010b s0 & trained $\\dt$-emb (Cheetah) & TP & 95K & reactive & 248 & 6.34 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n019b & trained $\\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 5/5 (1.00), \\quad FPR = 2/8 (0.25)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Results.}\nThe detector identifies all five CIVO-positive runs (TPR = 5/5). Two of five are detected \\emph{predictively}: 008d seed~0 triggers at 45K, one checkpoint before evaluation crosses the 20\\% decline threshold; seed~3 triggers at 45K, a full 50K steps before decline begins. The remaining three cases trigger reactively: 010b seed~1 (Cheetah Run, 65K) involves single-step collapse; 008d seed~4 (105K) and 010b seed~0 (Cheetah Run, 95K) fire after sustained decline is already underway.\n\nTwo false positives occur among eight negative cases (FPR = 2/8, precision = 5/7 = 0.71, F$_1$ = 0.83). Run 009c (no duration embedding) develops genuine late-stage value overestimation unrelated to CIVO; the detector correctly identifies value-performance dissociation, and the alert is arguably useful despite the label mismatch. Run 009a (vanilla baseline) triggers during a transient three-checkpoint eval dip at 85K; the model subsequently recovers to 966, constituting a pure false alarm. In practice, the cost of a false alert (manual checkpoint inspection, minutes) is orders of magnitude lower than the cost of undetected collapse (wasted GPU-hours, corrupted model); moderate FPR is therefore acceptable in this application.\n\nThe three earliest true positives triggered before 65K steps (range 45--65K), while the two additional cases (008d s4, 010b s0) triggered later (95--105K), overlapping with the false positive range (85--105K). Early-training alerts (before 70K) carry higher diagnostic confidence; later alerts warrant manual inspection regardless of ground truth.\n\n\\paragraph{Cross-simulator specificity (PickCube).}\nExp\\_019b applies the CIVO-trigger configuration (trained $\\dt$-embedding, subsample ON, $H{=}8$) to PickCube-v1 in ManiSkill3, a manipulation task with sparse rewards and qualitatively different dynamics from DMC locomotion. The V/E ratio exhibits an oscillatory pattern rather than monotonic divergence: it spikes to $r_t = 5.66$ at 52.5K (eval crashes from 24.9 to 3.7), then deflates to 1.38 by 72.5K as value estimates self-correct, eventually reaching 0.065$\\times$ NVE at 202.5K. This spike-then-deflation trajectory prevents the acceleration condition from co-occurring with evaluation decline at any single checkpoint. When V/E accelerates during early training (22.5--32.5K, consecutive velocities $+0.50$, $+1.85$), evaluation has not yet declined (C4 fails). When evaluation does decline (42.5--52.5K), the preceding V/E velocity is negative ($-0.81$), so the acceleration condition (C3) fails. Across all 14 checkpoints evaluated through 132.5K, no checkpoint satisfies all four conditions simultaneously, and the detector correctly remains silent (TN). This confirms that the acceleration filter distinguishes transient overestimation spikes from the sustained monotonic divergence characteristic of CIVO. The result extends the detector's specificity validation to a second simulator and a sparse-reward manipulation domain.\n\n\\paragraph{Limitations.}\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse (the source of the 009a false alarm). Second, the acceleration condition assumes monotonically increasing overestimation during onset; oscillatory trajectories that eventually collapse could evade detection until acceleration stabilizes. Third, the detector identifies a \\emph{pattern} (rising value-evaluation ratio with declining performance) rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values ($\\tau_\\text{mag} = 0.49$, $\\tau_\\text{vel} = 0.1$) were calibrated on thirteen runs across three environments; generalization to different reward scales requires further validation. The detector targets sustained CIVO patterns; transient single-checkpoint spikes (as observed in SGS-protected runs) are by design not flagged, as they do not indicate impending permanent collapse.\n",
      "numLines": 230,
      "startLine": 1,
      "totalLines": 230
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01LwaUqHX8GxbBPHBRb6eS9g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "49a83a97-23df-4088-bb90-4ec0a7b8c6bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJDsxhhooqcA3aFgoJqmJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 25723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 891
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

_source line 24 · 2026-05-18T11:35:12.184Z_

<details><summary>↩ Tool result · `toolu_01LwaUqHX8GxbBPHBRb6eS9g`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:methodology}
3	
4	\subsection{Base Architecture}
5	\label{sec:base_arch}
6	
7	All experiments build on DreamerV3 \citep{hafner2023dreamerv3}, which learns a recurrent state-space model (RSSM) with discrete latent states ($32$ categories $\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely within imagined trajectories. The standard configuration imagines $H{=}15$ steps at a fixed temporal resolution of $\dt{=}1$, meaning each imagination step corresponds to one environment transition.
8	
9	\subsection{Variable-Rate Imagination Mechanism}
10	\label{sec:variable_rate}
11	
12	We introduce three orthogonal architectural modifications that enable variable-rate imagination in DreamerV3. Each can be independently toggled to isolate its contribution.
13	
14	\paragraph{Temporal embedding.}
15	A learned embedding $e(\dt)$ is concatenated to the RSSM input at each imagination step to condition state predictions on the temporal scale. We test three modes:
16	\begin{itemize}[nosep,leftmargin=*]
17	\item \textbf{Trained}: embedding parameters are updated via backpropagation through the world model loss, so the RSSM can co-adapt its dynamics and reward predictions to the temporal scale.
18	\item \textbf{Frozen}: a fixed random projection of identical dimensionality (\texttt{requires\_grad=False}). The RSSM receives a temporal signal but cannot co-adapt to it.
19	\item \textbf{Removed}: embedding dimension set to zero; no temporal conditioning signal is provided.
20	\end{itemize}
21	We further distinguish \textbf{trained-and-exposed} (subsample ON: the RSSM trains on $\dt{>}1$ transitions) from \textbf{trained-but-unexposed} (subsample OFF: $\dt{>}1$ used only during imagination). This four-way classification (trained/exposed, trained/unexposed, frozen, removed) is the key causal structure of our factorial design.
22	
23	\paragraph{Temporal subsampling.}
24	When enabled, the replay buffer augments training data with variable-$\dt$ transitions by subsampling consecutive frames. Concretely, with a maximum subsampling factor of~2, the RSSM trains on both $\dt{=}1$ and $\dt{=}2$ transitions drawn from the same episodes. When disabled, only standard $\dt{=}1$ transitions are used. This factor controls whether the world model has seen multi-scale dynamics during training.
25	
26	\paragraph{Imagination horizon and step size.}
27	The imagination horizon $H$ sets the number of rollout steps. We test $H{=}15$ (default) and $H{=}8$. The reduced horizon controls for compounding error: $H{=}8$ steps at $\dt{=}2$ covers $16$ physical time steps, comparable to the $15$ physical steps of the default configuration. The parameter \texttt{gate\_fixed\_dt} forces all imagination steps to use a specific $\dt$ value ($1$, $2$, or $4$); this separates the effect of $\dt$-conditioning from any learned gating policy.
28	
29	\subsection{Factorial Design}
30	\label{sec:factorial}
31	
32	We adopt a structured factorial ablation across four factors: $\dt$-embedding mode (trained / frozen / none), temporal subsampling (on / off), imagination horizon ($H{=}15$ / $H{=}8$), and imagination step size ($\dt{=}1$, $2$, or $4$). Table~\ref{tab:factorial_design} summarizes the experimental configurations.
33	
34	\begin{table}[t]
35	\centering
36	\caption{Factorial design. Each row specifies one experimental configuration. \textbf{Emb}: $\dt$-embedding mode. \textbf{Sub}: temporal subsampling. \textbf{H}: imagination horizon. \textbf{Imag $\dt$}: temporal resolution used during imagination. Note: 006 enables subsample ON relative to the earlier 005 (learned gate) configuration; all other hyperparameters are shared.}
37	\label{tab:factorial_design}
38	\small
39	\setlength{\tabcolsep}{3.5pt}
40	\begin{tabular}{@{}llcccc@{}}
41	\toprule
42	\textbf{ID} & \textbf{Purpose} & \textbf{Emb} & \textbf{Sub} & \textbf{H} & \textbf{Imag $\dt$} \\
43	\midrule
44	001 & Reference baseline & --- & --- & 15 & 1 \\
45	006 & Fixed $\dt{=}2$ & trn & on & 15 & 2 \\
46	007 & Fixed $\dt{=}4$ & trn & on & 15 & 4 \\
47	\midrule
48	008a & Unexposed emb ctrl & exp$^a$ & off & 15 & 2 \\
49	008c & Horizon control & exp$^a$ & off & 8 & 2 \\
50	008d & Collapse condition & trn & on & 8 & 2 \\
51	008e\_v3 & $\dt{=}1$ imag control & trn & on & 15 & 1 \\
52	008f & Causal ablation & --- & on & 8 & 2 \\
53	\midrule
54	015b & Frozen-emb ctrl & frz$^b$ & on & 8 & 2 \\
55	016e & Stop-grad (reward) & trn$^\dagger$ & on & 8 & 2 \\
56	018 & Full-SGS & trn$^\ddagger$ & on & 8 & 2 \\
57	\midrule
58	005 & Learned gate & adaptive & off & 15 & learned \\
59	\bottomrule
60	\end{tabular}
61	\vspace{-2pt}
62	{\raggedright\footnotesize
63	trn = trained ($d{=}32$, exposed to $\dt{>}1$ data via subsample ON);
64	exp$^a$ = trained ($d{=}32$) but never exposed to $\dt{>}1$ data (subsample OFF);
65	frz$^b$ = frozen random projection ($d{=}32$, \texttt{requires\_grad=False});
66	--- = removed ($d{=}0$).\\
67	$^\dagger$ \texttt{reward\_dt\_emb\_detach=True}; $^\ddagger$ all non-KL gradients to \texttt{dt\_emb} detached.\par}
68	\end{table}
69	
70	The design isolates trained $\dt$-embedding and multi-rate data exposure as orthogonal factors, with 008d vs.\ 008f (embedding effect), 008d vs.\ 008a (exposure effect), and 008e\_v3 (imagination-channel control) as key contrasts. Most non-baseline configurations use 2 seeds; key configurations (008d, 008a) are extended to 3--4 seeds. Following \citet{agarwal2021precipice}, we report per-seed trajectories to surface stochastic divergence.
71	
72	\subsection{Diagnostic Metrics}
73	\label{sec:metrics}
74	
75	\paragraph{Evaluation return.}
76	The primary performance metric: mean return over 10 evaluation episodes, computed every 10K training steps with a deterministic policy.
77	
78	\paragraph{Value-to-eval ratio.}
79	We define the value-to-eval ratio $v/e$ as the ratio of the critic's mean imagined value to the evaluation return at each checkpoint. This tracks how well value estimates match realized performance. A ratio near~1 indicates calibrated value predictions; values substantially above~1 indicate systematic overestimation.
80	
81	\paragraph{Normalized value-to-eval ratio ($\nve$).}
82	To control for the baseline's natural $v/e$ dynamics (\eg, the ratio naturally increases during early training as the critic learns), we normalize:
83	\begin{equation}
84	\nve_t = \frac{(v/e)_{\text{config},\,t}}{(v/e)_{\text{baseline},\,t}}
85	\label{eq:nve}
86	\end{equation}
87	where $(v/e)_{\text{baseline},\,t}$ is from the single baseline seed (exp\_001, seed~1, 505K steps).  We restrict to a \textbf{35K+ window} ($t \geq 35\text{K}$) because the baseline $v/e$ is near zero in early training, causing spurious $\nve$ inflation.  We use $\nve \geq 1.5\times$ (peak within this window) as a warning threshold; across 14 experimental configurations in two environments, this achieves 13/14 accuracy (AUROC${=}0.933$), with one non-CIVO false positive (\S\ref{sec:f6}).  The threshold is sensitive but not perfectly specific to CIVO; mechanistic attribution requires joint analysis with collapse signatures (\S\ref{sec:pathways}).
88	
89	We distinguish two regimes above the threshold: \textbf{sustained CIVO}, characterized by monotonically escalating $\nve$ culminating in policy collapse (e.g., exp\_008d: $1.78\times \rightarrow 4.12\times$, eval $167 \rightarrow 82.8$), and \textbf{transient exceedance}, where $\nve$ briefly exceeds $1.5\times$ at isolated checkpoints but self-corrects without catastrophic collapse (e.g., exp\_009b: peak $1.62\times$ at 45K, self-correcting to $0.38\times$).  The pathological CIVO diagnosis requires sustained escalation with accompanying performance degradation, not merely a single checkpoint above the threshold.
90	
91	\paragraph{RSSM fidelity.}
92	To probe the mechanism underlying value drift, we evaluate world model prediction quality at different temporal scales from the same checkpoint. Specifically, we compute observation MSE and reward MAE on held-out $\dt{=}1$ versus $\dt{=}2$ transitions, and report the gap ratio between them. A large gap indicates that the world model produces systematically different prediction quality across temporal scales; this difference provides the channel for critic exploitation.
93	
94	\paragraph{Supplementary diagnostics.}
95	Two additional metrics target failure modes that $\nve$ may miss.
96	\emph{Actor loss sign}: DreamerV3's actor loss is normally negative (policy improvement direction). A sign flip to positive values directly signals that the critic is misleading the actor and serves as a more targeted marker of delusional-critic damage than the aggregate $\nve$ ratio.
97	\emph{Value standard deviation}: exponential growth in value variance across imagination rollouts captures oscillatory instability during ``false recovery'' phases where $\nve$ may temporarily decrease even as the underlying value landscape destabilizes.
98	
99	\subsection{Selective Gradient Stopping}
100	\label{sec:sgs_method}
101	
102	To identify which gradient pathway through $e_{\Delta t}$ drives CIVO, we introduce \textit{selective gradient stopping} (SGS): during the backward pass, $e_{\Delta t}$ is detached before entering selected prediction heads via the stop-gradient operator $\operatorname{sg}(\cdot)$, preventing those loss gradients from updating $e_{\Delta t}$'s parameters while preserving its forward-pass contribution.
103	
104	We test two variants. \textbf{Reward-only SGS} (exp\_016e) detaches $e_{\Delta t}$ from the reward head only: $\hat{r}_t = f_{\text{reward}}(\operatorname{sg}(e_{\Delta t}), h_t, z_t)$, testing whether the reward pathway drives CIVO. \textbf{Full-pathway SGS} (exp\_018) detaches $e_{\Delta t}$ from all non-KL gradient pathways (observation decoders, reward head, and continuation predictor), retaining only the KL dynamics loss signal. To quantify each pathway's contribution, we perform gradient decomposition using \texttt{torch.autograd.grad}, measuring the $\ell_2$ norm of $\nabla_\theta \mathcal{L}_i$ for each loss component $\mathcal{L}_i$, where $\theta$ denotes the temporal embedding parameters.
105	
106	\subsection{Environment and Training Details}
107	\label{sec:env_details}
108	
109	All experiments use Walker Walk and Cheetah Run from the DeepMind Control Suite \citep{tassa2018dmcontrol} with proprioceptive observations. The baseline runs for 500K environment steps, sufficient for convergence (peak return 970.4 on Walker Walk). Treatment configurations run for 105K steps, which is sufficient to observe both collapse onset and the diagnostic markers described above. All DreamerV3 hyperparameters follow the defaults from \citet{hafner2023dreamerv3} without task-specific tuning. The temporal embedding uses dimension $d{=}32$. Training uses a single NVIDIA RTX PRO 6000 GPU (96\,GB) with JIT compilation disabled (\texttt{-{}-compile False}) for reproducibility; wall-clock time is ${\sim}2.5$h per 105K-step run and ${\sim}12$h for the baseline (${\sim}80$ GPU-hours total). The codebase extends the official DreamerV3 implementation\footnote{\url{https://github.com/danijar/dreamerv3}, accessed March 2026.} with the variable-rate modules described in \S\ref{sec:variable_rate}; no other architectural modifications are made.
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "ddff76d5-051b-470d-8ec1-62609045ec2c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:methodology}\n\n\\subsection{Base Architecture}\n\\label{sec:base_arch}\n\nAll experiments build on DreamerV3 \\citep{hafner2023dreamerv3}, which learns a recurrent state-space model (RSSM) with discrete latent states ($32$ categories $\\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely within imagined trajectories. The standard configuration imagines $H{=}15$ steps at a fixed temporal resolution of $\\dt{=}1$, meaning each imagination step corresponds to one environment transition.\n\n\\subsection{Variable-Rate Imagination Mechanism}\n\\label{sec:variable_rate}\n\nWe introduce three orthogonal architectural modifications that enable variable-rate imagination in DreamerV3. Each can be independently toggled to isolate its contribution.\n\n\\paragraph{Temporal embedding.}\nA learned embedding $e(\\dt)$ is concatenated to the RSSM input at each imagination step to condition state predictions on the temporal scale. We test three modes:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Trained}: embedding parameters are updated via backpropagation through the world model loss, so the RSSM can co-adapt its dynamics and reward predictions to the temporal scale.\n\\item \\textbf{Frozen}: a fixed random projection of identical dimensionality (\\texttt{requires\\_grad=False}). The RSSM receives a temporal signal but cannot co-adapt to it.\n\\item \\textbf{Removed}: embedding dimension set to zero; no temporal conditioning signal is provided.\n\\end{itemize}\nWe further distinguish \\textbf{trained-and-exposed} (subsample ON: the RSSM trains on $\\dt{>}1$ transitions) from \\textbf{trained-but-unexposed} (subsample OFF: $\\dt{>}1$ used only during imagination). This four-way classification (trained/exposed, trained/unexposed, frozen, removed) is the key causal structure of our factorial design.\n\n\\paragraph{Temporal subsampling.}\nWhen enabled, the replay buffer augments training data with variable-$\\dt$ transitions by subsampling consecutive frames. Concretely, with a maximum subsampling factor of~2, the RSSM trains on both $\\dt{=}1$ and $\\dt{=}2$ transitions drawn from the same episodes. When disabled, only standard $\\dt{=}1$ transitions are used. This factor controls whether the world model has seen multi-scale dynamics during training.\n\n\\paragraph{Imagination horizon and step size.}\nThe imagination horizon $H$ sets the number of rollout steps. We test $H{=}15$ (default) and $H{=}8$. The reduced horizon controls for compounding error: $H{=}8$ steps at $\\dt{=}2$ covers $16$ physical time steps, comparable to the $15$ physical steps of the default configuration. The parameter \\texttt{gate\\_fixed\\_dt} forces all imagination steps to use a specific $\\dt$ value ($1$, $2$, or $4$); this separates the effect of $\\dt$-conditioning from any learned gating policy.\n\n\\subsection{Factorial Design}\n\\label{sec:factorial}\n\nWe adopt a structured factorial ablation across four factors: $\\dt$-embedding mode (trained / frozen / none), temporal subsampling (on / off), imagination horizon ($H{=}15$ / $H{=}8$), and imagination step size ($\\dt{=}1$, $2$, or $4$). Table~\\ref{tab:factorial_design} summarizes the experimental configurations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Factorial design. Each row specifies one experimental configuration. \\textbf{Emb}: $\\dt$-embedding mode. \\textbf{Sub}: temporal subsampling. \\textbf{H}: imagination horizon. \\textbf{Imag $\\dt$}: temporal resolution used during imagination. Note: 006 enables subsample ON relative to the earlier 005 (learned gate) configuration; all other hyperparameters are shared.}\n\\label{tab:factorial_design}\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{ID} & \\textbf{Purpose} & \\textbf{Emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Imag $\\dt$} \\\\\n\\midrule\n001 & Reference baseline & --- & --- & 15 & 1 \\\\\n006 & Fixed $\\dt{=}2$ & trn & on & 15 & 2 \\\\\n007 & Fixed $\\dt{=}4$ & trn & on & 15 & 4 \\\\\n\\midrule\n008a & Unexposed emb ctrl & exp$^a$ & off & 15 & 2 \\\\\n008c & Horizon control & exp$^a$ & off & 8 & 2 \\\\\n008d & Collapse condition & trn & on & 8 & 2 \\\\\n008e\\_v3 & $\\dt{=}1$ imag control & trn & on & 15 & 1 \\\\\n008f & Causal ablation & --- & on & 8 & 2 \\\\\n\\midrule\n015b & Frozen-emb ctrl & frz$^b$ & on & 8 & 2 \\\\\n016e & Stop-grad (reward) & trn$^\\dagger$ & on & 8 & 2 \\\\\n018 & Full-SGS & trn$^\\ddagger$ & on & 8 & 2 \\\\\n\\midrule\n005 & Learned gate & adaptive & off & 15 & learned \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^\\dagger$ \\texttt{reward\\_dt\\_emb\\_detach=True}; $^\\ddagger$ all non-KL gradients to \\texttt{dt\\_emb} detached.\\par}\n\\end{table}\n\nThe design isolates trained $\\dt$-embedding and multi-rate data exposure as orthogonal factors, with 008d vs.\\ 008f (embedding effect), 008d vs.\\ 008a (exposure effect), and 008e\\_v3 (imagination-channel control) as key contrasts. Most non-baseline configurations use 2 seeds; key configurations (008d, 008a) are extended to 3--4 seeds. Following \\citet{agarwal2021precipice}, we report per-seed trajectories to surface stochastic divergence.\n\n\\subsection{Diagnostic Metrics}\n\\label{sec:metrics}\n\n\\paragraph{Evaluation return.}\nThe primary performance metric: mean return over 10 evaluation episodes, computed every 10K training steps with a deterministic policy.\n\n\\paragraph{Value-to-eval ratio.}\nWe define the value-to-eval ratio $v/e$ as the ratio of the critic's mean imagined value to the evaluation return at each checkpoint. This tracks how well value estimates match realized performance. A ratio near~1 indicates calibrated value predictions; values substantially above~1 indicate systematic overestimation.\n\n\\paragraph{Normalized value-to-eval ratio ($\\nve$).}\nTo control for the baseline's natural $v/e$ dynamics (\\eg, the ratio naturally increases during early training as the critic learns), we normalize:\n\\begin{equation}\n\\nve_t = \\frac{(v/e)_{\\text{config},\\,t}}{(v/e)_{\\text{baseline},\\,t}}\n\\label{eq:nve}\n\\end{equation}\nwhere $(v/e)_{\\text{baseline},\\,t}$ is from the single baseline seed (exp\\_001, seed~1, 505K steps).  We restrict to a \\textbf{35K+ window} ($t \\geq 35\\text{K}$) because the baseline $v/e$ is near zero in early training, causing spurious $\\nve$ inflation.  We use $\\nve \\geq 1.5\\times$ (peak within this window) as a warning threshold; across 14 experimental configurations in two environments, this achieves 13/14 accuracy (AUROC${=}0.933$), with one non-CIVO false positive (\\S\\ref{sec:f6}).  The threshold is sensitive but not perfectly specific to CIVO; mechanistic attribution requires joint analysis with collapse signatures (\\S\\ref{sec:pathways}).\n\nWe distinguish two regimes above the threshold: \\textbf{sustained CIVO}, characterized by monotonically escalating $\\nve$ culminating in policy collapse (e.g., exp\\_008d: $1.78\\times \\rightarrow 4.12\\times$, eval $167 \\rightarrow 82.8$), and \\textbf{transient exceedance}, where $\\nve$ briefly exceeds $1.5\\times$ at isolated checkpoints but self-corrects without catastrophic collapse (e.g., exp\\_009b: peak $1.62\\times$ at 45K, self-correcting to $0.38\\times$).  The pathological CIVO diagnosis requires sustained escalation with accompanying performance degradation, not merely a single checkpoint above the threshold.\n\n\\paragraph{RSSM fidelity.}\nTo probe the mechanism underlying value drift, we evaluate world model prediction quality at different temporal scales from the same checkpoint. Specifically, we compute observation MSE and reward MAE on held-out $\\dt{=}1$ versus $\\dt{=}2$ transitions, and report the gap ratio between them. A large gap indicates that the world model produces systematically different prediction quality across temporal scales; this difference provides the channel for critic exploitation.\n\n\\paragraph{Supplementary diagnostics.}\nTwo additional metrics target failure modes that $\\nve$ may miss.\n\\emph{Actor loss sign}: DreamerV3's actor loss is normally negative (policy improvement direction). A sign flip to positive values directly signals that the critic is misleading the actor and serves as a more targeted marker of delusional-critic damage than the aggregate $\\nve$ ratio.\n\\emph{Value standard deviation}: exponential growth in value variance across imagination rollouts captures oscillatory instability during ``false recovery'' phases where $\\nve$ may temporarily decrease even as the underlying value landscape destabilizes.\n\n\\subsection{Selective Gradient Stopping}\n\\label{sec:sgs_method}\n\nTo identify which gradient pathway through $e_{\\Delta t}$ drives CIVO, we introduce \\textit{selective gradient stopping} (SGS): during the backward pass, $e_{\\Delta t}$ is detached before entering selected prediction heads via the stop-gradient operator $\\operatorname{sg}(\\cdot)$, preventing those loss gradients from updating $e_{\\Delta t}$'s parameters while preserving its forward-pass contribution.\n\nWe test two variants. \\textbf{Reward-only SGS} (exp\\_016e) detaches $e_{\\Delta t}$ from the reward head only: $\\hat{r}_t = f_{\\text{reward}}(\\operatorname{sg}(e_{\\Delta t}), h_t, z_t)$, testing whether the reward pathway drives CIVO. \\textbf{Full-pathway SGS} (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradient pathways (observation decoders, reward head, and continuation predictor), retaining only the KL dynamics loss signal. To quantify each pathway's contribution, we perform gradient decomposition using \\texttt{torch.autograd.grad}, measuring the $\\ell_2$ norm of $\\nabla_\\theta \\mathcal{L}_i$ for each loss component $\\mathcal{L}_i$, where $\\theta$ denotes the temporal embedding parameters.\n\n\\subsection{Environment and Training Details}\n\\label{sec:env_details}\n\nAll experiments use Walker Walk and Cheetah Run from the DeepMind Control Suite \\citep{tassa2018dmcontrol} with proprioceptive observations. The baseline runs for 500K environment steps, sufficient for convergence (peak return 970.4 on Walker Walk). Treatment configurations run for 105K steps, which is sufficient to observe both collapse onset and the diagnostic markers described above. All DreamerV3 hyperparameters follow the defaults from \\citet{hafner2023dreamerv3} without task-specific tuning. The temporal embedding uses dimension $d{=}32$. Training uses a single NVIDIA RTX PRO 6000 GPU (96\\,GB) with JIT compilation disabled (\\texttt{-{}-compile False}) for reproducibility; wall-clock time is ${\\sim}2.5$h per 105K-step run and ${\\sim}12$h for the baseline (${\\sim}80$ GPU-hours total). The codebase extends the official DreamerV3 implementation\\footnote{\\url{https://github.com/danijar/dreamerv3}, accessed March 2026.} with the variable-rate modules described in \\S\\ref{sec:variable_rate}; no other architectural modifications are made.\n",
      "numLines": 110,
      "startLine": 1,
      "totalLines": 110
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_016JhcjuA6AAw9ETXmman58h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "624d5e56-9feb-4f67-b045-792e3b862df0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJDsxhhooqcA3aFgoJqmJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 25723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 891
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

_source line 26 · 2026-05-18T11:35:12.391Z_

<details><summary>↩ Tool result · `toolu_016JhcjuA6AAw9ETXmman58h`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The results establish three insights that frame CIVO as a structural vulnerability of flat temporal conditioning in imagination-based RL. Full mechanistic analysis, gradient decomposition, and seed-divergence discussion are in Appendix~\ref{sec:appendix_analysis}.
5	
6	\paragraph{CIVO mechanism.}
7	The RSSM reward head develops a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$ under trained conditioning (Table~\ref{tab:rssm_fidelity}), providing the systematic bias that the critic internalizes and the actor exploits. This creates a four-stage feedback loop analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced.  Full-pathway SGS (exp\_018) targets the gradient channel that maintains this bias, yet yields mixed results (50\% recovery rate). This indicates that CIVO involves mechanisms beyond gradient-mediated co-adaptation of the temporal embedding.
8	
9	\paragraph{Gradient decomposition and intervention design.}
10	\label{sec:gradient_evolution_main}
11	Gradient decomposition (Figure~\ref{fig:gradient_decomp}, Table~\ref{tab:gradient_decomposition}) reveals a non-obvious structure: the reward head provides the largest gradient contribution to $e_{\Delta t}$ (49.0\% at 55K, 38.1\% at 112K), yet reward-only SGS (exp\_016e) is functionally insufficient (NVE $10.42\times$, collapse).  The observation decoder channel contributes the smallest share (16.3\% at 55K, 21.5\% at 112K) but encodes the critical $\dt$-specific spatial predictions that generate the RSSM fidelity gap.  Full-pathway SGS, which removes observation decoder \emph{and} reward gradients from $e_{\Delta t}$, \sgsclaim{} (seed~1: peak NVE $\sgsnve{}\times$, eval \sgseval{}; seed~2: collapsed, eval 40.8).  The 50\% recovery rate confirms that the observation decoder gradient pathway is causally involved but reveals that CIVO's feedback loop has redundant mechanisms not fully captured by gradient decomposition.
12	
13	\paragraph{Why does $\dt$-conditioning succeed in MPC but fail in imagination-based AC?}
14	TAWM \citep{nhu2025tawm} demonstrates that $\dt$-conditioning can be highly effective within the TD-MPC2 framework \citep{hansen2024tdmpc2}.  By conditioning the world model on $\dt$, TAWM achieves variable-rate planning that adapts temporal resolution to task demands and delivers state-of-the-art performance without value overestimation.  This success might appear to contradict our finding that $\dt$-conditioning induces CIVO.  The discrepancy is fully explained by the architectural difference between MPC and imagination-based actor-critic methods.
15	
16	TD-MPC2 is an MPC architecture that optimizes action sequences directly on model rollouts via the cross-entropy method, without training a value function on imagined trajectories.  When $\dt > 1$, the world model inevitably loses some predictive fidelity, but this error remains bounded because the agent re-plans from real observed states at every decision point.  Model errors at larger temporal strides are corrected before they can compound, and no value function is trained on the imprecise predictions.  There is therefore no channel through which systematic bias can be internalized and amplified.
17	
18	In DreamerV3, the architecture creates a closed feedback cycle: the RSSM generates imagined trajectories, the critic estimates values along these trajectories, and the actor optimizes against the critic's estimates.  When $\dt > 1$, the RSSM develops a fidelity gap (evidenced by the $2.78\times$ reward prediction disparity in Table~\ref{tab:rssm_fidelity}), and the observation decoder gradient pathway encodes $\dt$-specific spatial predictions that sustain this gap.  The critic, trained on these systematically biased imagined returns, develops inflated value estimates for $\dt > 1$ states.  The actor then preferentially selects actions that reach these overvalued states, which reinforces the bias and closes the CIVO loop.  This positive feedback mechanism has no counterpart in MPC, where no critic is trained on model outputs.
19	
20	The vulnerability is therefore specific to the imagination-based actor-critic architecture, not to $\dt$-conditioning itself.  MPC avoids value amplification through open-loop optimization with re-planning, which prevents model error from entering a self-reinforcing cycle.  This architectural distinction also clarifies why multiple vulnerability pathways exist within the imagination-based framework: both CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing, \S\ref{sec:f6}) originate from the same closed-loop structure that MPC lacks entirely.
21	
22	\paragraph{Practical monitoring.}
23	The online detector achieves perfect sensitivity (5/5 true positives) with a false positive rate of 2/8 (25\%).  Three of five true positives trigger at or before 65K steps (range 45--65K), while the remaining two trigger later (95--105K), overlapping with the false-positive window (85--105K).  This separation yields a practical deployment guideline where alerts before 70K steps indicate high-confidence CIVO onset, and later alerts require human inspection to distinguish genuine pathology from transient fluctuations.  The two false positive cases illustrate qualitatively different failure modes: case 009c exhibits genuine value-performance dissociation (a non-CIVO pathology where the alert retains diagnostic value), whereas case 009a reflects a transient evaluation dip from which the agent recovers to near-optimal performance (eval 966).  This distinction suggests the detector functions as a general value-health monitor rather than a CIVO-specific classifier.  The underlying signal (accelerating divergence between predicted value and realized performance) captures any sustained value-performance dissociation regardless of mechanistic origin, and the 009c case demonstrates that such dissociation is a useful early-warning signal even when the root cause is not CIVO.  The current thresholds were calibrated on thirteen runs across three environments; generalization to different reward scales and training regimes requires further validation.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb44b6c4-50ff-41c9-96c2-79e4d8dbf070",
  "uuid": "3f7ccf21-1945-450c-8382-f1e655f8a51b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\nThe results establish three insights that frame CIVO as a structural vulnerability of flat temporal conditioning in imagination-based RL. Full mechanistic analysis, gradient decomposition, and seed-divergence discussion are in Appendix~\\ref{sec:appendix_analysis}.\n\n\\paragraph{CIVO mechanism.}\nThe RSSM reward head develops a $2.78\\times$ prediction gap between $\\dt{=}1$ and $\\dt{=}2$ under trained conditioning (Table~\\ref{tab:rssm_fidelity}), providing the systematic bias that the critic internalizes and the actor exploits. This creates a four-stage feedback loop analogous to delusional bias \\citep{lu2018nondelusional} but model-induced rather than policy-class-induced.  Full-pathway SGS (exp\\_018) targets the gradient channel that maintains this bias, yet yields mixed results (50\\% recovery rate). This indicates that CIVO involves mechanisms beyond gradient-mediated co-adaptation of the temporal embedding.\n\n\\paragraph{Gradient decomposition and intervention design.}\n\\label{sec:gradient_evolution_main}\nGradient decomposition (Figure~\\ref{fig:gradient_decomp}, Table~\\ref{tab:gradient_decomposition}) reveals a non-obvious structure: the reward head provides the largest gradient contribution to $e_{\\Delta t}$ (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) is functionally insufficient (NVE $10.42\\times$, collapse).  The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) but encodes the critical $\\dt$-specific spatial predictions that generate the RSSM fidelity gap.  Full-pathway SGS, which removes observation decoder \\emph{and} reward gradients from $e_{\\Delta t}$, \\sgsclaim{} (seed~1: peak NVE $\\sgsnve{}\\times$, eval \\sgseval{}; seed~2: collapsed, eval 40.8).  The 50\\% recovery rate confirms that the observation decoder gradient pathway is causally involved but reveals that CIVO's feedback loop has redundant mechanisms not fully captured by gradient decomposition.\n\n\\paragraph{Why does $\\dt$-conditioning succeed in MPC but fail in imagination-based AC?}\nTAWM \\citep{nhu2025tawm} demonstrates that $\\dt$-conditioning can be highly effective within the TD-MPC2 framework \\citep{hansen2024tdmpc2}.  By conditioning the world model on $\\dt$, TAWM achieves variable-rate planning that adapts temporal resolution to task demands and delivers state-of-the-art performance without value overestimation.  This success might appear to contradict our finding that $\\dt$-conditioning induces CIVO.  The discrepancy is fully explained by the architectural difference between MPC and imagination-based actor-critic methods.\n\nTD-MPC2 is an MPC architecture that optimizes action sequences directly on model rollouts via the cross-entropy method, without training a value function on imagined trajectories.  When $\\dt > 1$, the world model inevitably loses some predictive fidelity, but this error remains bounded because the agent re-plans from real observed states at every decision point.  Model errors at larger temporal strides are corrected before they can compound, and no value function is trained on the imprecise predictions.  There is therefore no channel through which systematic bias can be internalized and amplified.\n\nIn DreamerV3, the architecture creates a closed feedback cycle: the RSSM generates imagined trajectories, the critic estimates values along these trajectories, and the actor optimizes against the critic's estimates.  When $\\dt > 1$, the RSSM develops a fidelity gap (evidenced by the $2.78\\times$ reward prediction disparity in Table~\\ref{tab:rssm_fidelity}), and the observation decoder gradient pathway encodes $\\dt$-specific spatial predictions that sustain this gap.  The critic, trained on these systematically biased imagined returns, develops inflated value estimates for $\\dt > 1$ states.  The actor then preferentially selects actions that reach these overvalued states, which reinforces the bias and closes the CIVO loop.  This positive feedback mechanism has no counterpart in MPC, where no critic is trained on model outputs.\n\nThe vulnerability is therefore specific to the imagination-based actor-critic architecture, not to $\\dt$-conditioning itself.  MPC avoids value amplification through open-loop optimization with re-planning, which prevents model error from entering a self-reinforcing cycle.  This architectural distinction also clarifies why multiple vulnerability pathways exist within the imagination-based framework: both CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing, \\S\\ref{sec:f6}) originate from the same closed-loop structure that MPC lacks entirely.\n\n\\paragraph{Practical monitoring.}\nThe online detector achieves perfect sensitivity (5/5 true positives) with a false positive rate of 2/8 (25\\%).  Three of five true positives trigger at or before 65K steps (range 45--65K), while the remaining two trigger later (95--105K), overlapping with the false-positive window (85--105K).  This separation yields a practical deployment guideline where alerts before 70K steps indicate high-confidence CIVO onset, and later alerts require human inspection to distinguish genuine pathology from transient fluctuations.  The two false positive cases illustrate qualitatively different failure modes: case 009c exhibits genuine value-performance dissociation (a non-CIVO pathology where the alert retains diagnostic value), whereas case 009a reflects a transient evaluation dip from which the agent recovers to near-optimal performance (eval 966).  This distinction suggests the detector functions as a general value-health monitor rather than a CIVO-specific classifier.  The underlying signal (accelerating divergence between predicted value and realized performance) captures any sustained value-performance dissociation regardless of mechanistic origin, and the 009c case demonstrates that such dissociation is a useful early-warning signal even when the root cause is not CIVO.  The current thresholds were calibrated on thirteen runs across three environments; generalization to different reward scales and training regimes requires further validation.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  }
}
```

</details>

---
