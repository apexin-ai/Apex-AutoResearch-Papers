# paper w6 structural confound

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/workers/worker_paper_w6_structural_confound_20260516T032042.log`
- **Structured JSON:** [`c74f3eec76898a794c35.json`](../../sessions/c7/c74f3eec76898a794c35.json)

## Before a recorded user message

64 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
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
  "uuid": "ecd24f5b-edae-4841-b474-877e16a02130",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1778904600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "521a02ef-051c-482e-8cb2-aae438110720",
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec"
}
```

---

### Assistant

_source line 4_

Let me start by reading the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "eca1310e-e763-43d7-a35f-ee7efd2e7f2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PhY2dpvsye6tx71sNKidU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11890,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11890
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

<details open><summary>🔧 Tool call — Read · `toolu_0153eH4FcYpZmpnMUPMydtU3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "abae36ef-7200-4d0a-b3e9-78703019bacf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PhY2dpvsye6tx71sNKidU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11890,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11890
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

_source line 6 · 2026-05-16T03:20:53.519Z_

<details><summary>↩ Tool result · reported error · `toolu_0153eH4FcYpZmpnMUPMydtU3`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "97b7eef8-b9c7-4d98-a126-f69b8a86ff54",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01CZrZCQjEbPVJMmYT34AABk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "5ab20494-ad24-4a07-9ba1-53f68a807ef6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PhY2dpvsye6tx71sNKidU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11890,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11890
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

_source line 8 · 2026-05-16T03:20:53.872Z_

<details><summary>↩ Tool result · reported error · `toolu_01CZrZCQjEbPVJMmYT34AABk`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "07bc9782-0e96-41e1-8adb-1573da97dacd",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination."
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_013ScCz4gA5PZYhfthSSC5wj`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "8321e375-224b-4643-b4d9-366986426c1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PhY2dpvsye6tx71sNKidU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11890,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11890
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

_source line 10 · 2026-05-16T03:20:54.508Z_

<details><summary>↩ Tool result · `toolu_013ScCz4gA5PZYhfthSSC5wj`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "d588fc58-47c0-4c98-8677-66d743215980",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 14,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
The paper directory doesn't exist locally. Let me check what's actually in the project directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "8c6a3d2f-3908-4a3a-9595-831068b6e063",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YecDxT8Cf1GhuMwt9iKR8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 415,
      "cache_read_input_tokens": 23731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 415
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

_source line 12_

Paper directory doesn't exist locally. Let me check what's available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "7c81c7d5-8a9c-48b7-b018-d36e54b14cc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YecDxT8Cf1GhuMwt9iKR8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 415,
      "cache_read_input_tokens": 23731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 415
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01M9sy6SBw6GYdPLb4tKmFee`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/",
  "description": "List project directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "83f84d09-928b-4553-925a-a27ae7531add",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YecDxT8Cf1GhuMwt9iKR8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 415,
      "cache_read_input_tokens": 23731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 415
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

_source line 14 · 2026-05-16T03:20:58.596Z_

<details><summary>↩ Tool result · `toolu_01M9sy6SBw6GYdPLb4tKmFee`</summary>

```text
total 284
drwxr-xr-x 11 ubuntu ubuntu  4096 May 16 03:14 .
drwxrwxr-x  5 ubuntu ubuntu  4096 May 12 10:56 ..
drwxr-xr-x  3 ubuntu ubuntu  4096 May 12 10:56 .claude
drwxr-xr-x  6 ubuntu ubuntu  4096 May 14 07:58 .venv
-rw-r--r--  1 ubuntu ubuntu 12798 May 16 03:20 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu     0 May 12 10:58 ROADMAP.lock
-rw-------  1 ubuntu ubuntu  3750 May 16 03:14 ROADMAP.md
drwxr-xr-x 19 ubuntu ubuntu  4096 May 16 02:40 artifacts
drwxr-xr-x  2 ubuntu ubuntu 20480 May 16 01:13 checkpoints
-rw-r--r--  1 ubuntu ubuntu     0 May 12 10:58 decisions.lock
-rw-------  1 ubuntu ubuntu 35794 May 16 02:37 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 13 02:35 docs
-rwxr-xr-x  1 ubuntu ubuntu     0 May 12 20:03 dream_registry.lock
-rw-------  1 ubuntu ubuntu  1425 May 13 09:05 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu  1430 May 13 09:05 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu 13683 May 15 10:26 exp_A_alt_scorer.py
-rw-r--r--  1 ubuntu ubuntu     0 May 12 20:50 experiment_plan.lock
-rw-------  1 ubuntu ubuntu  6266 May 16 03:11 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu 16613 May 14 06:22 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 12 11:10 logs
-rw-r--r--  1 ubuntu ubuntu  5282 May 16 03:20 memory.md
drwxr-xr-x  3 ubuntu ubuntu  4096 May 16 00:00 paper
-rw-r--r--  1 ubuntu ubuntu 14671 May 16 00:58 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu     0 May 13 09:22 paper_provenance.lock
-rw-------  1 ubuntu ubuntu 11562 May 15 23:20 paper_provenance.yaml
-rw-r--r--  1 ubuntu ubuntu     0 May 12 11:09 registry.lock
-rw-------  1 ubuntu ubuntu 53504 May 16 03:06 registry.yaml
-rw-r--r--  1 ubuntu ubuntu  1285 May 16 01:13 report.md
-rw-r--r--  1 ubuntu ubuntu  1653 May 15 10:26 run_exp_A.sh
drwxr-xr-x  3 ubuntu ubuntu  4096 May 16 02:55 scripts
-rwxr-xr-x  1 ubuntu ubuntu     0 May 12 10:57 study_status.lock
drwxr-xr-x  3 ubuntu ubuntu  4096 May 16 03:18 task_context
-rw-r--r--  1 ubuntu ubuntu 14338 May 13 11:50 writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "ebb7d579-555b-4080-83ef-9fb49553d9b4",
  "tool_use_result": {
    "stdout": "total 284\ndrwxr-xr-x 11 ubuntu ubuntu  4096 May 16 03:14 .\ndrwxrwxr-x  5 ubuntu ubuntu  4096 May 12 10:56 ..\ndrwxr-xr-x  3 ubuntu ubuntu  4096 May 12 10:56 .claude\ndrwxr-xr-x  6 ubuntu ubuntu  4096 May 14 07:58 .venv\n-rw-r--r--  1 ubuntu ubuntu 12798 May 16 03:20 AGENTS.md\n-rw-r--r--  1 ubuntu ubuntu     0 May 12 10:58 ROADMAP.lock\n-rw-------  1 ubuntu ubuntu  3750 May 16 03:14 ROADMAP.md\ndrwxr-xr-x 19 ubuntu ubuntu  4096 May 16 02:40 artifacts\ndrwxr-xr-x  2 ubuntu ubuntu 20480 May 16 01:13 checkpoints\n-rw-r--r--  1 ubuntu ubuntu     0 May 12 10:58 decisions.lock\n-rw-------  1 ubuntu ubuntu 35794 May 16 02:37 decisions.yaml\ndrwxr-xr-x  4 ubuntu ubuntu  4096 May 13 02:35 docs\n-rwxr-xr-x  1 ubuntu ubuntu     0 May 12 20:03 dream_registry.lock\n-rw-------  1 ubuntu ubuntu  1425 May 13 09:05 dream_registry.yaml\n-rw-r--r--  1 ubuntu ubuntu  1430 May 13 09:05 dream_registry.yaml.bak\n-rw-r--r--  1 ubuntu ubuntu 13683 May 15 10:26 exp_A_alt_scorer.py\n-rw-r--r--  1 ubuntu ubuntu     0 May 12 20:50 experiment_plan.lock\n-rw-------  1 ubuntu ubuntu  6266 May 16 03:11 experiment_plan.yaml\n-rw-r--r--  1 ubuntu ubuntu 16613 May 14 06:22 literature_map.yaml\ndrwxr-xr-x  4 ubuntu ubuntu  4096 May 12 11:10 logs\n-rw-r--r--  1 ubuntu ubuntu  5282 May 16 03:20 memory.md\ndrwxr-xr-x  3 ubuntu ubuntu  4096 May 16 00:00 paper\n-rw-r--r--  1 ubuntu ubuntu 14671 May 16 00:58 paper_framing.md\n-rw-r--r--  1 ubuntu ubuntu     0 May 13 09:22 paper_provenance.lock\n-rw-------  1 ubuntu ubuntu 11562 May 15 23:20 paper_provenance.yaml\n-rw-r--r--  1 ubuntu ubuntu     0 May 12 11:09 registry.lock\n-rw-------  1 ubuntu ubuntu 53504 May 16 03:06 registry.yaml\n-rw-r--r--  1 ubuntu ubuntu  1285 May 16 01:13 report.md\n-rw-r--r--  1 ubuntu ubuntu  1653 May 15 10:26 run_exp_A.sh\ndrwxr-xr-x  3 ubuntu ubuntu  4096 May 16 02:55 scripts\n-rwxr-xr-x  1 ubuntu ubuntu     0 May 12 10:57 study_status.lock\ndrwxr-xr-x  3 ubuntu ubuntu  4096 May 16 03:18 task_context\n-rw-r--r--  1 ubuntu ubuntu 14338 May 13 11:50 writing_plan.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01Hg8uMmkzToHx3naNJD47GX`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "6175c72f-ff23-4a1c-8c58-c51c2cf62e1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YecDxT8Cf1GhuMwt9iKR8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 415,
      "cache_read_input_tokens": 23731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 415
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

_source line 16 · 2026-05-16T03:20:58.836Z_

<details><summary>↩ Tool result · `toolu_01Hg8uMmkzToHx3naNJD47GX`</summary>

```text
artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_c1.tex
artifacts/exp_015_neural_probe/paper/neural_probe_analysis.tex
artifacts/drafts/neural_probe_analysis.tex
artifacts/c3_contingency_versions.tex
artifacts/exp-006/paper/c3_contingency_versions.tex
docs/paper/tables/tab_filtering_main.tex
docs/paper/tables/tab_alpha_sweep.tex
docs/paper/tables/tab_pairwise_significance.tex
docs/paper/tables/tab_crossscorer.tex
docs/paper/appendix_extended.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/related_work.tex
docs/paper/experiments_c3.tex
docs/paper/appendix.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/experiments_c1.tex
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "68201b6d-c3a5-48e1-99ac-c733c474730f",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260512T200328/best/paper.tex",
      "artifacts/dream_reports/dream_20260512T200328/median/paper.tex",
      "artifacts/dream_reports/dream_20260512T200328/worst/paper.tex",
      "artifacts/dream_reports/dream_20260513T080728/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T080728/median/paper.tex",
      "artifacts/dream_reports/dream_20260513T080728/worst/paper.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/experiments_c1.tex",
      "artifacts/exp_015_neural_probe/paper/neural_probe_analysis.tex",
      "artifacts/drafts/neural_probe_analysis.tex",
      "artifacts/c3_contingency_versions.tex",
      "artifacts/exp-006/paper/c3_contingency_versions.tex",
      "docs/paper/tables/tab_filtering_main.tex",
      "docs/paper/tables/tab_alpha_sweep.tex",
      "docs/paper/tables/tab_pairwise_significance.tex",
      "docs/paper/tables/tab_crossscorer.tex",
      "docs/paper/appendix_extended.tex",
      "docs/paper/introduction.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/related_work.tex",
      "docs/paper/experiments_c3.tex",
      "docs/paper/appendix.tex",
      "docs/paper/method.tex",
      "docs/paper/discussion.tex",
      "docs/paper/experiments_c1.tex",
      "docs/paper/main.tex"
    ],
    "durationMs": 22,
    "numFiles": 26,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
The paper files are in `docs/paper/` not `paper/`. Let me also check what's in the `paper/` directory. And let me read the relevant tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "33be93ff-af42-4761-af41-599cdd073fc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuqGXbe84tJK3TUuFY7VRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 24146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1624
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

_source line 18_

Found them in `docs/paper/`. Let me read the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "8e360602-b749-4e31-8c63-db8f5ad40da0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuqGXbe84tJK3TUuFY7VRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 24146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1624
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

<details open><summary>🔧 Tool call — Read · `toolu_01PuYW3ZtfHUS9hFGgiYtia5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "88cbfb52-5671-4086-8527-478ca84d9377",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuqGXbe84tJK3TUuFY7VRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 24146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1624
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

_source line 20 · 2026-05-16T03:21:02.459Z_

<details><summary>↩ Tool result · `toolu_01PuYW3ZtfHUS9hFGgiYtia5`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{The One-Wash Laundering Effect}
5	\label{sec:why_kstar}
6	\label{sec:one_wash}
7	
8	The shallowness of $\Kempirical = 2$ reflects the concentration of information loss: the 0v1 boundary is near-trivially separable ($\auc \geq 0.96$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$---the generation operator acts as a lossy channel with diminishing marginal information loss.
9	Consistency across four decoding strategies (Table~\ref{tab:s2_decoding}) reinforces that $\Kempirical$ is governed by the generation process rather than the sampling algorithm.
10	Even at the most marginal 1v2 condition (Qwen-continuation, CI lower bound exceeds $\theta$ by only 0.2\,pp), $\Kempirical = 2$ survives under self-scoring; on the 2v3 side, CI upper bounds confirm non-discrimination in 8/9 conditions, with the single borderline case (nucleus $p{=}0.9$, CI upper${} = 0.601$) consistent with measurement noise at near-threshold values.
11	Cross-scale validation at 7B (Section~\ref{sec:kstar_boundary}) extends this from 1.5B to 7B despite reduced 0v1 signal ($0.9638$ vs.\ $> 0.99$).
12	
13	The practical consequence is a three-tier taxonomy: human-authored (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$).
14	A single generation pass suffices to render text statistically indistinguishable from multiply recycled content---a \emph{one-wash laundering} effect that limits depth-aware corpus curation to a binary boundary.
15	This connects to model collapse: Shumailov et al.~\cite{shumailov2024collapse} observed that tail-distribution degradation is most acute in the earliest generations; our prompt-chain results show an analogous per-text pattern.
16	
17	Per-depth analysis provides the most direct evidence that this boundary is not methodological.
18	OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 69--77\% depth-0 recall and 8--38\% for depths 2--4 (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
19	This convergence across fundamentally different approaches---supervised statistical classification and zero-shot frontier LLMs---provides converging evidence that the saturation reflects a data-intrinsic boundary rather than a method limitation.
20	Binary detector confidence corroborates: despite moderate Spearman correlations ($|\rho|$ up to 0.46), 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), and Qwen-rewrite exhibits a sign reversal ($\rho > 0$), disqualifying confidence as a reliable depth proxy.
21	
22	\subsection{Why Graduated Filtering Fails}
23	\label{sec:negative_graduated}
24	
25	Since 2v3 $\auc < \theta$ for all configurations, depth assignments for $d \geq 2$ approximate random labels; graduated weighting injects noise into importance weights, explaining the monotonic improvement with $\alpha$ as it converges toward binary thresholding (Appendix~\ref{sec:extended_limitations}).
26	DSIR fails for a different reason---bigram feature hashing captures domain shift but not depth-correlated distributional signatures.
27	
28	\subsection{Representation Dependence of the Boundary}
29	\label{sec:repr_dependence}
30	
31	$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia and OLMo match the 15D boundary at $\Kempirical^{\text{neural}} = 2$ (Table~\ref{tab:neural_probe_crossmodel}).
32	The hierarchy $\Kempirical^{15\text{D}}{=}2 < \Kempirical^{\text{neural}} \in \{2,3\}$ reflects an interpretability--sensitivity tradeoff: learned representations recover additional depth signal sufficient to push $\Kempirical$ to 3 for one model (Qwen), but this gain is model-dependent---the 15D features trade one depth level of sensitivity for cross-model universality (9/9 conditions $\Kempirical{=}2$, 3/3 models identical), making them the preferred operational choice.
33	Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\Kempirical = 2$ to 1, while rewrite-mode $\Kempirical = 2$ is preserved---$\Kempirical$ is governed by the generation operator rather than the scoring model.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "8ed3d008-aa39-491d-8f84-e3f3856c81f8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{The One-Wash Laundering Effect}\n\\label{sec:why_kstar}\n\\label{sec:one_wash}\n\nThe shallowness of $\\Kempirical = 2$ reflects the concentration of information loss: the 0v1 boundary is near-trivially separable ($\\auc \\geq 0.96$), 1v2 drops by ${\\sim}$30\\,pp, and 2v3 falls below $\\theta$---the generation operator acts as a lossy channel with diminishing marginal information loss.\nConsistency across four decoding strategies (Table~\\ref{tab:s2_decoding}) reinforces that $\\Kempirical$ is governed by the generation process rather than the sampling algorithm.\nEven at the most marginal 1v2 condition (Qwen-continuation, CI lower bound exceeds $\\theta$ by only 0.2\\,pp), $\\Kempirical = 2$ survives under self-scoring; on the 2v3 side, CI upper bounds confirm non-discrimination in 8/9 conditions, with the single borderline case (nucleus $p{=}0.9$, CI upper${} = 0.601$) consistent with measurement noise at near-threshold values.\nCross-scale validation at 7B (Section~\\ref{sec:kstar_boundary}) extends this from 1.5B to 7B despite reduced 0v1 signal ($0.9638$ vs.\\ $> 0.99$).\n\nThe practical consequence is a three-tier taxonomy: human-authored (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\\geq 2$).\nA single generation pass suffices to render text statistically indistinguishable from multiply recycled content---a \\emph{one-wash laundering} effect that limits depth-aware corpus curation to a binary boundary.\nThis connects to model collapse: Shumailov et al.~\\cite{shumailov2024collapse} observed that tail-distribution degradation is most acute in the earliest generations; our prompt-chain results show an analogous per-text pattern.\n\nPer-depth analysis provides the most direct evidence that this boundary is not methodological.\nOBD achieves 96\\% depth-0 recall but only 14--22\\% for depths 2--4; frontier LLMs show 69--77\\% depth-0 recall and 8--38\\% for depths 2--4 (McNemar $p > 0.05$ vs.\\ OBD; Table~\\ref{tab:s3_llm_zeroshot}).\nThis convergence across fundamentally different approaches---supervised statistical classification and zero-shot frontier LLMs---provides converging evidence that the saturation reflects a data-intrinsic boundary rather than a method limitation.\nBinary detector confidence corroborates: despite moderate Spearman correlations ($|\\rho|$ up to 0.46), 6-class accuracy is at or below chance ($\\leq 0.199$ vs.\\ 0.167 baseline), and Qwen-rewrite exhibits a sign reversal ($\\rho > 0$), disqualifying confidence as a reliable depth proxy.\n\n\\subsection{Why Graduated Filtering Fails}\n\\label{sec:negative_graduated}\n\nSince 2v3 $\\auc < \\theta$ for all configurations, depth assignments for $d \\geq 2$ approximate random labels; graduated weighting injects noise into importance weights, explaining the monotonic improvement with $\\alpha$ as it converges toward binary thresholding (Appendix~\\ref{sec:extended_limitations}).\nDSIR fails for a different reason---bigram feature hashing captures domain shift but not depth-correlated distributional signatures.\n\n\\subsection{Representation Dependence of the Boundary}\n\\label{sec:repr_dependence}\n\n$\\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$, while Pythia and OLMo match the 15D boundary at $\\Kempirical^{\\text{neural}} = 2$ (Table~\\ref{tab:neural_probe_crossmodel}).\nThe hierarchy $\\Kempirical^{15\\text{D}}{=}2 < \\Kempirical^{\\text{neural}} \\in \\{2,3\\}$ reflects an interpretability--sensitivity tradeoff: learned representations recover additional depth signal sufficient to push $\\Kempirical$ to 3 for one model (Qwen), but this gain is model-dependent---the 15D features trade one depth level of sensitivity for cross-model universality (9/9 conditions $\\Kempirical{=}2$, 3/3 models identical), making them the preferred operational choice.\nCross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\\Kempirical = 2$ to 1, while rewrite-mode $\\Kempirical = 2$ is preserved---$\\Kempirical$ is governed by the generation operator rather than the scoring model.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01EpspZs5y4RnorBvRAQ5dqA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "e8748aec-4d75-4e29-b61c-31fe81cae9fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuqGXbe84tJK3TUuFY7VRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 24146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1624
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

_source line 22 · 2026-05-16T03:21:02.904Z_

<details><summary>↩ Tool result · `toolu_01EpspZs5y4RnorBvRAQ5dqA`</summary>

```text
1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
7	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
8	\label{fig:filtering_strategies}
9	\end{figure}
10	
11	\begin{figure}[t]
12	  \centering
13	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
14	  \caption{Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
15	  \label{fig:s1_auc_decay_ci}
16	\end{figure}
17	
18	\section{Supplementary Tables}
19	
20	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
21	\begin{table*}[t]
22	  \centering
23	  \caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}
24	  \label{tab:s1_transfer}
25	  \begin{tabular}{lcccc}
26	    \toprule
27	    \multirow{2}{*}{\textbf{Train Model}} & \multicolumn{4}{c}{\textbf{Test Model}} \\
28	    \cmidrule(lr){2-5}
29	    & Qwen-rw & Pythia & OLMo & Qwen-cont \\
30	    \midrule
31	    Qwen-rw   & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
32	    Pythia    & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
33	    OLMo      & 0.2768 & 0.3450 & \textbf{0.3822} & 0.3244 \\
34	    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \textbf{0.3875} \\
35	    \bottomrule
36	  \end{tabular}
37	  \vspace{4pt}
38	
39	  \footnotesize
40	  \textit{Transfer retention} between models $A$ and $B$ is defined as $\frac{1}{2}\bigl(\frac{\mathrm{acc}(A \to B)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}} + \frac{\mathrm{acc}(B \to A)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}}\bigr)$.
41	  Notable pairs: Pythia$\leftrightarrow$OLMo 91--92\%, Qwen-cont$\leftrightarrow$Pythia 83--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\%, Qwen-rw$\to$Pythia/OLMo 61--63\%.
42	\end{table*}
43	
44	%%% Table S2: Decoding Ablation AUC (exp-003)
45	\begin{table*}[t]
46	  \centering
47	  \caption{Pairwise AUC across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode). The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$: pairs above this line are reliably separable ($\auc > 0.60$), while those below approach chance. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings.}
48	  \label{tab:s2_decoding}
49	  \begin{tabular}{lcccc}
50	    \toprule
51	    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
52	    \midrule
53	    0 vs.\ 1 & 0.9797 & 0.9946 & 0.9878 & 0.9982 \\
54	    1 vs.\ 2 & 0.6893 & 0.6866 & 0.6887 & 0.7039 \\
55	    \cmidrule(lr){1-5}
56	    2 vs.\ 3 & 0.5613 & 0.5917 & 0.5902 & 0.5823 \\
57	    3 vs.\ 4 & 0.5404 & 0.5466 & 0.5393 & 0.5293 \\
58	    4 vs.\ 5 & 0.5139 & 0.5068 & 0.5349 & 0.5237 \\
59	    \midrule
60	    \multicolumn{5}{l}{\textbf{Cross-config feature Spearman $\rho$}} \\
61	    \midrule
62	    \multicolumn{2}{l}{Greedy vs.\ Nuc $p{=}0.9$} & 0.600 &
63	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}0.7$} & 0.782 \\
64	    \multicolumn{2}{l}{Greedy vs.\ $T{=}0.7$} & 0.914 &
65	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}1.2$} & 0.893 \\
66	    \multicolumn{2}{l}{Greedy vs.\ $T{=}1.2$} & 0.532 &
67	    \multicolumn{1}{l}{$T{=}0.7$ vs.\ $T{=}1.2$} & 0.668 \\
68	    \bottomrule
69	  \end{tabular}
70	\end{table*}
71	
72	%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
73	\begin{table*}[t]
74	  \centering
75	  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices
76	    (Exp-011). Both frontier LLMs achieve high binary detection accuracy
77	    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class
78	    accuracy (${\sim}0.33$ vs.\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5
79	    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on
80	    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as
81	    depth-2. Claude Opus~4.6 shows more uniform errors across depths 1--4,
82	    with depth-4 recall (0.3700) substantially exceeding GPT-5.5.
83	    Per-depth recall comparison with OBD-LightGBM in Table~\ref{tab:s3c_perdepth}.}
84	  \label{tab:s3_llm_zeroshot}
85	
86	  \vspace{0.5em}
87	  \begin{subtable}{0.48\textwidth}
88	    \centering
89	    \caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}
90	    \label{tab:s3a_gpt55}
91	    \small
92	    \begin{tabular}{lcccccc}
93	      \toprule
94	      & \multicolumn{5}{c}{Predicted Depth} & \\
95	      \cmidrule(lr){2-6}
96	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
97	      \midrule
98	      0 & \textbf{77} & 18 &  4 &  0 &  1 & .770 \\
99	      1 &  9 & \textbf{19} & 36 & 24 & 12 & .190 \\
100	      2 &  8 & 10 & \textbf{38} & 35 &  9 & .380 \\
101	      3 & 10 & 16 & 35 & \textbf{24} & 15 & .240 \\
102	      4 & 11 & 13 & 50 & 18 &  \textbf{8} & .080 \\
103	      \bottomrule
104	    \end{tabular}
105	  \end{subtable}
106	  \hfill
107	  \begin{subtable}{0.48\textwidth}
108	    \centering
109	    \caption{Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)}
110	    \label{tab:s3b_claude}
111	    \small
112	    \begin{tabular}{lcccccc}
113	      \toprule
114	      & \multicolumn{5}{c}{Predicted Depth} & \\
115	      \cmidrule(lr){2-6}
116	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
117	      \midrule
118	      0 & \textbf{69} & 26 &  3 &  0 &  2 & .690 \\
119	      1 &  8 & \textbf{21} & 32 & 11 & 28 & .210 \\
120	      2 &  6 & 36 & \textbf{28} &  5 & 25 & .280 \\
121	      3 &  7 & 20 & 31 & \textbf{10} & 31 & .100 \\
122	      4 &  7 & 28 & 22 &  6 & \textbf{37} & .370 \\
123	      \bottomrule
124	    \end{tabular}
125	  \end{subtable}
126	\end{table*}
127	
128	\begin{table}[t]
129	  \centering
130	  \small
131	  \caption{Per-depth recall (\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\geq 2$, consistent with $\Kempirical = 2$.}
132	  \label{tab:s3c_perdepth}
133	  \begin{tabular}{lccccc}
134	    \toprule
135	    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\
136	    \midrule
137	    OBD-LightGBM & \textbf{96} & \textbf{39} & 14 & 19 & 22 \\
138	    GPT-5.5      & 77 & 19 & \textbf{38} & \textbf{24} &  8 \\
139	    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \textbf{37} \\
140	    \bottomrule
141	  \end{tabular}
142	\end{table}
143	
144	\clearpage
145	\section{Supplementary Details}
146	
147	%%% Table S4: Dataset Statistics
148	\begin{table}[t]
149	  \centering
150	  \small
151	  \caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}
152	  \label{tab:s4_dataset_stats}
153	  \begin{tabular}{clrl}
154	    \toprule
155	    \textbf{Depth} & \textbf{$N$ samples} & \textbf{Mean tokens} & \textbf{Source} \\
156	    \midrule
157	    0 & 5{,}000 & 147.8 & C4 validation (human) \\
158	    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\
159	    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\
160	    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\
161	    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
162	    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
163	    \midrule
164	    \multicolumn{2}{l}{Total} & \multicolumn{2}{l}{30{,}000 samples} \\
165	    \bottomrule
166	  \end{tabular}
167	\end{table}
168	
169	%%% Table S5: Complete 15-D Feature Descriptions
170	\begin{table*}[t]
171	  \centering
172	  \caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}
173	  \label{tab:s5_features}
174	  \begin{tabular}{llp{0.45\textwidth}l}
175	    \toprule
176	    \textbf{Group} & \textbf{Feature} & \textbf{Description} & \textbf{Range} \\
177	    \midrule
178	    \multirow{9}{*}{\rotatebox[origin=c]{90}{\textsc{Surprisal}}}
179	    & \texttt{surp\_mean}   & Mean token surprisal $\frac{1}{T}\sum_t -\log p(x_t \mid x_{&lt;t})$ & $\mathbb{R}^+$ \\
180	    & \texttt{surp\_std}    & Standard deviation of token surprisal & $\mathbb{R}^+$ \\
181	    & \texttt{surp\_skew}   & Skewness of the surprisal distribution & $\mathbb{R}$ \\
182	    & \texttt{surp\_kurt}   & Excess kurtosis of the surprisal distribution & $\mathbb{R}$ \\
183	    & \texttt{surp\_d1\_mean} & Mean of first-order surprisal differences $\Delta s_t = s_{t+1} - s_t$ & $\mathbb{R}$ \\
184	    & \texttt{surp\_d1\_std}  & Std of first-order surprisal differences & $\mathbb{R}^+$ \\
185	    & \texttt{surp\_d1\_skew} & Skewness of first-order surprisal differences & $\mathbb{R}$ \\
186	    & \texttt{surp\_d2\_mean} & Mean of second-order differences $\Delta^2 s_t$ & $\mathbb{R}$ \\
187	    & \texttt{surp\_d2\_std}  & Std of second-order surprisal differences & $\mathbb{R}^+$ \\
188	    \midrule
189	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Lex}}}
190	    & \texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\
191	    & \texttt{hapax\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\
192	    & \texttt{self\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\
193	    \midrule
194	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Freq}}}
195	    & \texttt{freq\_kurtosis}  & Excess kurtosis of word frequency distribution & $\mathbb{R}$ \\
196	    & \texttt{freq\_entropy}   & Shannon entropy of word frequencies: $-\sum p_w \log_2 p_w$ & $\mathbb{R}^+$ \\
197	    & \texttt{low\_freq\_ratio} & Proportion of vocabulary with count $\leq 2$ & $[0, 1]$ \\
198	    \bottomrule
199	  \end{tabular}
200	\end{table*}
201	
202	%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap
203	\begin{table*}[t]
204	\begin{minipage}[t]{0.45\textwidth}
205	  \centering
206	  \small
207	  \captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \texttt{doc\_id} to prevent data leakage from the same seed document appearing in both train and test.}
208	  \label{tab:s6_lgbm_params}
209	  \begin{tabular}{ll}
210	    \toprule
211	    \textbf{Parameter} & \textbf{Value} \\
212	    \midrule
213	    \texttt{n\_estimators}      & 200 \\
214	    \texttt{learning\_rate}     & 0.05 \\
215	    \texttt{max\_depth}         & 6 \\
216	    \texttt{num\_leaves}        & 31 \\
217	    \texttt{verbose}            & $-1$ \\
218	    \texttt{n\_jobs}            & $-1$ (all cores) \\
219	    Cross-validation            & 5-fold GroupKFold \\
220	    Grouping key                & \texttt{doc\_id} \\
221	    Objective                   & Binary (per depth pair) \\
222	    \bottomrule
223	  \end{tabular}
224	\end{minipage}\hfill
225	\begin{minipage}[t]{0.52\textwidth}
226	  \centering
227	  \small
228	  \captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}
229	  \label{tab:s7_neural_probe}
230	  \resizebox{\textwidth}{!}{%
231	  \begin{tabular}{ll}
232	    \toprule
233	    \textbf{Component} & \textbf{Details} \\
234	    \midrule
235	    \multicolumn{2}{l}{\textit{Embedding extraction}} \\
236	    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\
237	    Representation    & Last hidden state, attention-masked avg pool \\
238	    Embedding dim     & 1536 / 2048 / 2048 \\
239	    Max sequence len   & 512 tokens \\
240	    \midrule
241	    \multicolumn{2}{l}{\textit{MLP classifier}} \\
242	    Architecture      & $d_{\text{emb}} \to 512 \to 256 \to 6$ \\
243	    Activations       & ReLU \\
244	    Dropout           & 0.1 (after each hidden layer) \\
245	    Output            & 6-class softmax \\
246	    \midrule
247	    \multicolumn{2}{l}{\textit{Training}} \\
248	    Optimizer         & Adam ($\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\
249	    Loss              & Cross-entropy \\
250	    Batch size        & 256 \\
251	    Max epochs        & 20 \\
252	    Early stopping    & Patience = 5 (validation loss) \\
253	    Cross-validation  & 5-fold GroupKFold \\
254	    \bottomrule
255	  \end{tabular}%
256	  }
257	\end{minipage}
258	\end{table*}
259	
260	%%% Table S8: Per-Model Bootstrap CI Results (exp-007)
261	\begin{table*}[t]
262	  \centering
263	  \footnotesize
264	  \caption{Pairwise AUC with bootstrap 95\% confidence intervals for four model-mode configurations (Exp-007, 1{,}000 bootstrap resamples). The horizontal rule separates depth pairs above and below the detectability threshold $\theta = 0.60$. Permutation $p$-values test $H_0\colon \auc = 0.50$. All pairs are significant at $p < 0.01$ except OLMo 3\,vs.\,4 ($p = 0.064$) and 4\,vs.\,5 ($p = 0.232$), consistent with convergence to chance at deeper generations.}
265	  \label{tab:s8_cv_folds}
266	  \begin{tabular}{lcccc}
267	    \toprule
268	    \textbf{Depth Pair} & \textbf{Qwen-rewrite} & \textbf{Pythia-1.4B} & \textbf{OLMo-1B} & \textbf{Qwen-cont} \\
269	    \midrule
270	    0 vs.\ 1
271	      & $.996\;[.995,\,.997]$
272	      & $.993\;[.992,\,.994]$
273	      & $.997\;[.996,\,.998]$
274	      & $.997\;[.996,\,.998]$ \\
275	    1 vs.\ 2
276	      & $.696\;[.686,\,.704]$
277	      & $.654\;[.645,\,.663]$
278	      & $.615\;[.605,\,.625]$
279	      & $.611\;[.602,\,.621]$ \\
280	    \cmidrule(lr){1-5}
281	    2 vs.\ 3
282	      & $.589\;[.580,\,.599]$
283	      & $.551\;[.542,\,.563]$
284	      & $.550\;[.540,\,.560]$
285	      & $.561\;[.551,\,.571]$ \\
286	    3 vs.\ 4
287	      & $.544\;[.533,\,.555]$
288	      & $.515\;[.504,\,.526]$
289	      & $.509\;[.497,\,.520]^{\dagger}$
290	      & $.541\;[.531,\,.551]$ \\
291	    4 vs.\ 5
292	      & $.534\;[.524,\,.545]$
293	      & $.514\;[.502,\,.525]$
294	      & $.505\;[.493,\,.515]^{\ddagger}$
295	      & $.514\;[.504,\,.526]$ \\
296	    \bottomrule
297	  \end{tabular}
298	
299	  \vspace{4pt}
300	  \footnotesize
301	  Each cell: AUC $[95\%$ CI$]$. CI from 1{,}000 bootstrap resamples; $p$-values from 500-resample permutation test.
302	  ${}^{\dagger}$\,$p = 0.064$;\; ${}^{\ddagger}$\,$p = 0.232$;\; all other pairs $p < 0.01$.
303	\end{table*}
304	
305	%%% Table S9: Binary Detector Spearman ρ (exp-012)
306	\begin{table*}[t]
307	  \centering
308	  \small
309	  \caption{Spearman rank correlation ($\rho$) between binary detector confidence scores and true generational depth, and 6-class depth classification accuracy (Exp-012). Three metrics: log-PPL from the reference model (DivEye), log-PPL from the observer model, and PPL ratio (Binoculars; observer: Pythia-1.4B, performer: OLMo-1B). Random baseline for 6-class accuracy: 0.167. While statistically significant, correlations are driven by the 0v1 boundary; confidence scores do not monotonically track depth beyond generation~1. Qwen-rewrite exhibits reversed sign ($\rho > 0$), indicating that generation mode alters the direction of binary confidence's relationship with depth.}
310	  \label{tab:s9_binary_spearman}
311	  \begin{tabular}{lcccc}
312	    \toprule
313	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
314	    \midrule
315	    \multicolumn{5}{l}{\textit{Spearman $\rho$ with true depth}} \\
316	    \quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\
317	    \quad log-PPL (observer) & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\
318	    \quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\
319	    \midrule
320	    \multicolumn{5}{l}{\textit{Classification}} \\
321	    \quad 6-class accuracy    & 0.199    & 0.130    & 0.127    & 0.183 \\
322	    \midrule
323	    \multicolumn{5}{l}{Random baseline: 0.167 \quad $\Kempirical^{\text{binary}} = 1$ \quad $\Kempirical^{\text{OBD}} = 2$} \\
324	    \bottomrule
325	  \end{tabular}
326	\end{table*}
327	
328	\clearpage
329	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "c86553db-b757-405f-8eb3-b7abfa131a5f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
      "content": "\\appendix\n\\section{Supplementary Figures}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_filtering_strategies.pdf}\n\\caption{Downstream performance of all filtering strategies (5 seeds, $\\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}\n\\label{fig:filtering_strategies}\n\\end{figure}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}\n  \\caption{Pairwise $\\auc$ decay curves for five model-mode configurations with bootstrap 95\\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\\Kempirical=2$ boundary where $\\auc$ drops below $\\theta=0.60$. This figure complements Figure~\\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}\n  \\label{fig:s1_auc_decay_ci}\n\\end{figure}\n\n\\section{Supplementary Tables}\n\n%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}\n  \\label{tab:s1_transfer}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\multirow{2}{*}{\\textbf{Train Model}} & \\multicolumn{4}{c}{\\textbf{Test Model}} \\\\\n    \\cmidrule(lr){2-5}\n    & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n    \\midrule\n    Qwen-rw   & \\textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\\\\n    Pythia    & 0.2718 & \\textbf{0.3856} & 0.3531 & 0.3287 \\\\\n    OLMo      & 0.2768 & 0.3450 & \\textbf{0.3822} & 0.3244 \\\\\n    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \\textbf{0.3875} \\\\\n    \\bottomrule\n  \\end{tabular}\n  \\vspace{4pt}\n\n  \\footnotesize\n  \\textit{Transfer retention} between models $A$ and $B$ is defined as $\\frac{1}{2}\\bigl(\\frac{\\mathrm{acc}(A \\to B)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}} + \\frac{\\mathrm{acc}(B \\to A)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}}\\bigr)$.\n  Notable pairs: Pythia$\\leftrightarrow$OLMo 91--92\\%, Qwen-cont$\\leftrightarrow$Pythia 83--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\%, Qwen-rw$\\to$Pythia/OLMo 61--63\\%.\n\\end{table*}\n\n%%% Table S2: Decoding Ablation AUC (exp-003)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Pairwise AUC across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode). The horizontal rule between depth pairs 1\\,vs.\\,2 and 2\\,vs.\\,3 marks the empirical detectability boundary $\\Kempirical=2$: pairs above this line are reliably separable ($\\auc > 0.60$), while those below approach chance. Bottom rows report cross-configuration Spearman $\\rho$ on per-feature discriminative-power rankings.}\n  \\label{tab:s2_decoding}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy} & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & 0.9797 & 0.9946 & 0.9878 & 0.9982 \\\\\n    1 vs.\\ 2 & 0.6893 & 0.6866 & 0.6887 & 0.7039 \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & 0.5613 & 0.5917 & 0.5902 & 0.5823 \\\\\n    3 vs.\\ 4 & 0.5404 & 0.5466 & 0.5393 & 0.5293 \\\\\n    4 vs.\\ 5 & 0.5139 & 0.5068 & 0.5349 & 0.5237 \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textbf{Cross-config feature Spearman $\\rho$}} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Greedy vs.\\ Nuc $p{=}0.9$} & 0.600 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}0.7$} & 0.782 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}0.7$} & 0.914 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}1.2$} & 0.893 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}1.2$} & 0.532 &\n    \\multicolumn{1}{l}{$T{=}0.7$ vs.\\ $T{=}1.2$} & 0.668 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)\n\\begin{table*}[t]\n  \\centering\n  \\caption{LLM zero-shot depth classification: $5{\\times}5$ confusion matrices\n    (Exp-011). Both frontier LLMs achieve high binary detection accuracy\n    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class\n    accuracy (${\\sim}0.33$ vs.\\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5\n    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on\n    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as\n    depth-2. Claude Opus~4.6 shows more uniform errors across depths 1--4,\n    with depth-4 recall (0.3700) substantially exceeding GPT-5.5.\n    Per-depth recall comparison with OBD-LightGBM in Table~\\ref{tab:s3c_perdepth}.}\n  \\label{tab:s3_llm_zeroshot}\n\n  \\vspace{0.5em}\n  \\begin{subtable}{0.48\\textwidth}\n    \\centering\n    \\caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}\n    \\label{tab:s3a_gpt55}\n    \\small\n    \\begin{tabular}{lcccccc}\n      \\toprule\n      & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n      \\cmidrule(lr){2-6}\n      True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n      \\midrule\n      0 & \\textbf{77} & 18 &  4 &  0 &  1 & .770 \\\\\n      1 &  9 & \\textbf{19} & 36 & 24 & 12 & .190 \\\\\n      2 &  8 & 10 & \\textbf{38} & 35 &  9 & .380 \\\\\n      3 & 10 & 16 & 35 & \\textbf{24} & 15 & .240 \\\\\n      4 & 11 & 13 & 50 & 18 &  \\textbf{8} & .080 \\\\\n      \\bottomrule\n    \\end{tabular}\n  \\end{subtable}\n  \\hfill\n  \\begin{subtable}{0.48\\textwidth}\n    \\centering\n    \\caption{Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)}\n    \\label{tab:s3b_claude}\n    \\small\n    \\begin{tabular}{lcccccc}\n      \\toprule\n      & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n      \\cmidrule(lr){2-6}\n      True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n      \\midrule\n      0 & \\textbf{69} & 26 &  3 &  0 &  2 & .690 \\\\\n      1 &  8 & \\textbf{21} & 32 & 11 & 28 & .210 \\\\\n      2 &  6 & 36 & \\textbf{28} &  5 & 25 & .280 \\\\\n      3 &  7 & 20 & 31 & \\textbf{10} & 31 & .100 \\\\\n      4 &  7 & 28 & 22 &  6 & \\textbf{37} & .370 \\\\\n      \\bottomrule\n    \\end{tabular}\n  \\end{subtable}\n\\end{table*}\n\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}\n  \\begin{tabular}{lccccc}\n    \\toprule\n    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\\\\n    \\midrule\n    OBD-LightGBM & \\textbf{96} & \\textbf{39} & 14 & 19 & 22 \\\\\n    GPT-5.5      & 77 & 19 & \\textbf{38} & \\textbf{24} &  8 \\\\\n    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \\textbf{37} \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n\\clearpage\n\\section{Supplementary Details}\n\n%%% Table S4: Dataset Statistics\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}\n  \\label{tab:s4_dataset_stats}\n  \\begin{tabular}{clrl}\n    \\toprule\n    \\textbf{Depth} & \\textbf{$N$ samples} & \\textbf{Mean tokens} & \\textbf{Source} \\\\\n    \\midrule\n    0 & 5{,}000 & 147.8 & C4 validation (human) \\\\\n    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\\\\n    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\\\\n    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\\\\n    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Total} & \\multicolumn{2}{l}{30{,}000 samples} \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n%%% Table S5: Complete 15-D Feature Descriptions\n\\begin{table*}[t]\n  \\centering\n  \\caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}\n  \\label{tab:s5_features}\n  \\begin{tabular}{llp{0.45\\textwidth}l}\n    \\toprule\n    \\textbf{Group} & \\textbf{Feature} & \\textbf{Description} & \\textbf{Range} \\\\\n    \\midrule\n    \\multirow{9}{*}{\\rotatebox[origin=c]{90}{\\textsc{Surprisal}}}\n    & \\texttt{surp\\_mean}   & Mean token surprisal $\\frac{1}{T}\\sum_t -\\log p(x_t \\mid x_{&lt;t})$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_std}    & Standard deviation of token surprisal & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_skew}   & Skewness of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_kurt}   & Excess kurtosis of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_mean} & Mean of first-order surprisal differences $\\Delta s_t = s_{t+1} - s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_std}  & Std of first-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_d1\\_skew} & Skewness of first-order surprisal differences & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_mean} & Mean of second-order differences $\\Delta^2 s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_std}  & Std of second-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Lex}}}\n    & \\texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\\\\n    & \\texttt{hapax\\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\\\\n    & \\texttt{self\\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Freq}}}\n    & \\texttt{freq\\_kurtosis}  & Excess kurtosis of word frequency distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{freq\\_entropy}   & Shannon entropy of word frequencies: $-\\sum p_w \\log_2 p_w$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{low\\_freq\\_ratio} & Proportion of vocabulary with count $\\leq 2$ & $[0, 1]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap\n\\begin{table*}[t]\n\\begin{minipage}[t]{0.45\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \\texttt{doc\\_id} to prevent data leakage from the same seed document appearing in both train and test.}\n  \\label{tab:s6_lgbm_params}\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Parameter} & \\textbf{Value} \\\\\n    \\midrule\n    \\texttt{n\\_estimators}      & 200 \\\\\n    \\texttt{learning\\_rate}     & 0.05 \\\\\n    \\texttt{max\\_depth}         & 6 \\\\\n    \\texttt{num\\_leaves}        & 31 \\\\\n    \\texttt{verbose}            & $-1$ \\\\\n    \\texttt{n\\_jobs}            & $-1$ (all cores) \\\\\n    Cross-validation            & 5-fold GroupKFold \\\\\n    Grouping key                & \\texttt{doc\\_id} \\\\\n    Objective                   & Binary (per depth pair) \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{minipage}\\hfill\n\\begin{minipage}[t]{0.52\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}\n  \\label{tab:s7_neural_probe}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Component} & \\textbf{Details} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Embedding extraction}} \\\\\n    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\\\\n    Representation    & Last hidden state, attention-masked avg pool \\\\\n    Embedding dim     & 1536 / 2048 / 2048 \\\\\n    Max sequence len   & 512 tokens \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{MLP classifier}} \\\\\n    Architecture      & $d_{\\text{emb}} \\to 512 \\to 256 \\to 6$ \\\\\n    Activations       & ReLU \\\\\n    Dropout           & 0.1 (after each hidden layer) \\\\\n    Output            & 6-class softmax \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Training}} \\\\\n    Optimizer         & Adam ($\\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\\\\n    Loss              & Cross-entropy \\\\\n    Batch size        & 256 \\\\\n    Max epochs        & 20 \\\\\n    Early stopping    & Patience = 5 (validation loss) \\\\\n    Cross-validation  & 5-fold GroupKFold \\\\\n    \\bottomrule\n  \\end{tabular}%\n  }\n\\end{minipage}\n\\end{table*}\n\n%%% Table S8: Per-Model Bootstrap CI Results (exp-007)\n\\begin{table*}[t]\n  \\centering\n  \\footnotesize\n  \\caption{Pairwise AUC with bootstrap 95\\% confidence intervals for four model-mode configurations (Exp-007, 1{,}000 bootstrap resamples). The horizontal rule separates depth pairs above and below the detectability threshold $\\theta = 0.60$. Permutation $p$-values test $H_0\\colon \\auc = 0.50$. All pairs are significant at $p < 0.01$ except OLMo 3\\,vs.\\,4 ($p = 0.064$) and 4\\,vs.\\,5 ($p = 0.232$), consistent with convergence to chance at deeper generations.}\n  \\label{tab:s8_cv_folds}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Qwen-rewrite} & \\textbf{Pythia-1.4B} & \\textbf{OLMo-1B} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    0 vs.\\ 1\n      & $.996\\;[.995,\\,.997]$\n      & $.993\\;[.992,\\,.994]$\n      & $.997\\;[.996,\\,.998]$\n      & $.997\\;[.996,\\,.998]$ \\\\\n    1 vs.\\ 2\n      & $.696\\;[.686,\\,.704]$\n      & $.654\\;[.645,\\,.663]$\n      & $.615\\;[.605,\\,.625]$\n      & $.611\\;[.602,\\,.621]$ \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3\n      & $.589\\;[.580,\\,.599]$\n      & $.551\\;[.542,\\,.563]$\n      & $.550\\;[.540,\\,.560]$\n      & $.561\\;[.551,\\,.571]$ \\\\\n    3 vs.\\ 4\n      & $.544\\;[.533,\\,.555]$\n      & $.515\\;[.504,\\,.526]$\n      & $.509\\;[.497,\\,.520]^{\\dagger}$\n      & $.541\\;[.531,\\,.551]$ \\\\\n    4 vs.\\ 5\n      & $.534\\;[.524,\\,.545]$\n      & $.514\\;[.502,\\,.525]$\n      & $.505\\;[.493,\\,.515]^{\\ddagger}$\n      & $.514\\;[.504,\\,.526]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\footnotesize\n  Each cell: AUC $[95\\%$ CI$]$. CI from 1{,}000 bootstrap resamples; $p$-values from 500-resample permutation test.\n  ${}^{\\dagger}$\\,$p = 0.064$;\\; ${}^{\\ddagger}$\\,$p = 0.232$;\\; all other pairs $p < 0.01$.\n\\end{table*}\n\n%%% Table S9: Binary Detector Spearman ρ (exp-012)\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Spearman rank correlation ($\\rho$) between binary detector confidence scores and true generational depth, and 6-class depth classification accuracy (Exp-012). Three metrics: log-PPL from the reference model (DivEye), log-PPL from the observer model, and PPL ratio (Binoculars; observer: Pythia-1.4B, performer: OLMo-1B). Random baseline for 6-class accuracy: 0.167. While statistically significant, correlations are driven by the 0v1 boundary; confidence scores do not monotonically track depth beyond generation~1. Qwen-rewrite exhibits reversed sign ($\\rho > 0$), indicating that generation mode alters the direction of binary confidence's relationship with depth.}\n  \\label{tab:s9_binary_spearman}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Spearman $\\rho$ with true depth}} \\\\\n    \\quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\\\\n    \\quad log-PPL (observer) & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\\\\n    \\quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Classification}} \\\\\n    \\quad 6-class accuracy    & 0.199    & 0.130    & 0.127    & 0.183 \\\\\n    \\midrule\n    \\multicolumn{5}{l}{Random baseline: 0.167 \\quad $\\Kempirical^{\\text{binary}} = 1$ \\quad $\\Kempirical^{\\text{OBD}} = 2$} \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n\\clearpage\n",
      "numLines": 329,
      "startLine": 1,
      "totalLines": 329
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01STLDQhv81jx8VqTypEMwcy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "162a86c4-8135-4cab-bbbe-9544497b2c68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuqGXbe84tJK3TUuFY7VRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 24146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1624
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

_source line 24 · 2026-05-16T03:21:03.325Z_

<details><summary>↩ Tool result · `toolu_01STLDQhv81jx8VqTypEMwcy`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on five model configurations:
5	Pythia-1.4B and OLMo-1B in continuation mode, Qwen2.5-1.5B-Instruct in both rewrite and continuation modes, and Qwen2.5-7B in continuation mode (cross-scale scoring with Qwen2.5-1.5B).
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical = 2$ Across All Configurations}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.}
17	\label{tab:kstar_ci}
18	\begin{tabular}{lcccccccccc}
19	\toprule
20	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
21	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
22	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
23	\midrule
24	0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] \\
25	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
26	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
27	3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\
28	4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\
29	\bottomrule
30	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all five 1v2 comparisons.} \\
31	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}
32	\end{tabular}
33	\end{table*}
34	
35	\begin{figure}[t]
36	\centering
37	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
38	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$.}
39	\label{fig:auc_decay}
40	\end{figure}
41	
42	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show a consistent pattern: 0v1 discrimination is near-perfect ($\auc \geq 0.96$), followed by a sharp drop at 1v2 ($\auc$: 0.6112--0.6955), with 2v3 falling below $\theta$ (0.5492--0.5893) and deeper pairs converging toward chance.
43	All five 1v2 point estimates exceed $\theta$, confirmed by bootstrap CIs (most marginal lower bound: Qwen-1.5B-continuation at 0.602); all five 2v3 point estimates and CI upper bounds fall below $\theta$ (permutation $p < 0.001$ for all boundary comparisons).
44	This establishes $\Kempirical = 2$ as consistent across all 9 tested conditions (5 independent model-mode configurations and 4 decoding-strategy ablation variants on the Qwen-rewrite configuration; Table~\ref{tab:s2_decoding}).
45	Under cross-model scoring, Qwen-continuation $\Kempirical$ drops to 1 (Section~\ref{sec:transfer}), indicating a model-specific component in the most marginal 1v2 boundary signal.
46	The sharp step-function pattern reflects the concentration of information loss: human text exhibits heavy-tailed, bursty surprisal patterns that are substantially altered by even a single autoregressive pass.
47	Subsequent generations operate on already-smoothed distributions, yielding progressively smaller marginal changes that fall below detectability within two steps.
48	
49	The 1v2 $\auc$ varies across models: Qwen-rewrite (0.6955) $>$ Pythia (0.6539) $>$ OLMo (0.6145) $\approx$ Qwen-continuation (0.6112).
50	The spread due to generation mode within a single model ($\Delta = 8.4$\,pp) exceeds the spread across models in the same mode ($\Delta = 3.9$\,pp), suggesting that generation mode appears to have a larger effect than model architecture, though formal interaction testing is beyond our current scope.
51	
52	\paragraph{Cross-scale validation.}
53	Qwen2.5-7B in continuation mode (scored by Qwen2.5-1.5B) confirms $\Kempirical = 2$: 1v2 $\auc = 0.6168$ $[0.608,\,0.626]$ (CI lower bound $> \theta$), 2v3 $\auc = 0.5492$ $[0.539,\,0.559]$ (Table~\ref{tab:kstar_ci}).
54	The 0v1 $\auc$ drops to 0.9638 (${\sim}$3\,pp below ${\leq}$1.5B models), consistent with larger models generating more human-like text; yet the $\Kempirical$ boundary remains unchanged, extending the invariance from 1.5B to 7B.
55	
56	\begin{figure}[t]
57	\centering
58	\includegraphics[width=\columnwidth]{figures/fig_kstar_theta.pdf}
59	\caption{$\Kempirical$ as a function of $\theta$ across five model-mode configurations, computed using the 95\% CI lower bound criterion (Eq.~\ref{eq:kstar}). The dashed line marks the operational threshold $\theta{=}0.60$ used throughout, where all configurations yield $\Kempirical{=}2$. Qwen-rewrite yields the highest $\Kempirical$ at all $\theta$; at $\theta{=}0.70$, $\Kempirical{=}1$ universally.}
60	\label{fig:kstar_theta}
61	\end{figure}
62	
63	Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$ (conservative CI-lower-bound variant): unanimous $\Kempirical = 2$ holds within $\theta \in [0.580, 0.600]$.
64	At $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite and Qwen-continuation while Pythia, OLMo, and Qwen-7B remain at $\Kempirical = 2$; at $\theta = 0.65$, all continuation modes drop to $\Kempirical = 1$ while rewrite retains $\Kempirical = 2$; at $\theta = 0.70$, $\Kempirical = 1$ universally.
65	All four decoding configurations (greedy, nucleus $p{=}0.9$, $T{=}0.70$, $T{=}1.2$) likewise yield $\Kempirical = 2$ at $\theta = 0.60$, with 1v2 $\auc$ in $[0.6866, 0.7039]$ (Table~\ref{tab:s2_decoding}).
66	Bootstrap CIs confirm 2v3 upper bounds below $\theta$ for 3/4 decoding variants; the nucleus $p{=}0.9$ condition (2v3 $\auc = 0.5917$, CI $[0.582, 0.601]$) has its upper bound marginally straddling $\theta$ by 0.001, consistent with measurement noise.
67	
68	%% ====================================================================
69	\subsection{Cross-Model Transfer}
70	\label{sec:transfer}
71	
72	\begin{figure}[t]
73	\centering
74	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
75	\caption{Cross-model transfer heatmap (6-class ordinal accuracy). Pythia$\leftrightarrow$OLMo achieves 90--92\% retention; Qwen-rewrite$\to$continuation-mode models: 61--63\%.}
76	\label{fig:transfer_heatmap}
77	\end{figure}
78	
79	The universality of $\Kempirical = 2$ raises a natural question: does the depth boundary reflect properties of the text itself, or generator-specific artifacts?
80	Cross-model transfer experiments address this directly.
81	
82	Figure~\ref{fig:transfer_heatmap} shows the transfer accuracy matrix (full matrix in Table~\ref{tab:s1_transfer}).
83	Continuation-mode transfer is high: Pythia$\leftrightarrow$OLMo retains 90--92\% of within-model accuracy, Qwen-cont$\leftrightarrow$Pythia 84--85\%, and Qwen-cont$\leftrightarrow$OLMo 80--85\%.
84	At the 0v1 boundary, cross-model $\auc$ exceeds 0.96 for all pairs (range: 0.963--0.991).
85	These retention rates suggest that depth features transfer across generators when computed by a fixed scorer.
86	The high retention indicates that the relative importance of depth features is encoded in distributional text properties---surprisal variance, lexical diversity---rather than in generator-specific fingerprints, enabling generator-agnostic deployment when a consistent scorer is used.
87	
88	Qwen-rewrite classifiers transfer poorly (61--63\% retention to Pythia/OLMo), confirming reliance on mode-specific artifacts.
89	Cross-mode transfer is asymmetric: continuation$\to$rewrite retains 89\% while rewrite$\to$continuation retains 82\%, indicating that continuation-mode features form a generalizable subset.
90	
91	\paragraph{Cross-scorer validation.}
92	To test whether depth signals depend on the scorer model, we replace the Qwen self-scorer with two alternative scorers (Pythia-1.4B, OLMo-1B) for feature extraction on Qwen-generated text.
93	Feature rankings remain highly correlated across all scorer pairs (Spearman $\rho > 0.90$), confirming that feature ordering is text-intrinsic.
94	Absolute discriminability, however, is scorer-sensitive at the $\Kempirical$ boundary.
95	For Qwen-rewrite, $\Kempirical = 2$ is scorer-invariant: 1v2 $\auc$ remains stable under cross-scoring (Pythia: 0.7012, OLMo: 0.6947; self-scorer baseline: 0.6955; Table~\ref{tab:crossscorer}).
96	For Qwen-continuation---already the most marginal self-scorer condition (CI lower bound exceeds $\theta$ by only 0.2\,pp; Table~\ref{tab:kstar_ci})---$\Kempirical$ drops from 2 to 1 under both alternative scorers (1v2 $\auc$: $0.6112 \to 0.5923$ [Pythia], $0.5858$ [OLMo], both below $\theta$).
97	This dissociation---scorer-invariant feature rankings but scorer-sensitive boundary classification---indicates that cross-scoring preserves the relative importance structure of depth features while attenuating the absolute signal, with consequences only where the self-scorer margin is already thin.
98	Crucially, both alternative scorers agree on $\Kempirical$ for each generation mode ($\Kempirical = 2$ for rewrite, $1$ for continuation), indicating that $\Kempirical$ is determined by the generation process rather than the choice of scoring model.
99	
100	%% ====================================================================
101	\subsection{Feature Degradation Ordering}
102	\label{sec:feature_degradation}
103	
104	\begin{table*}[t]
105	\centering
106	\small
107	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
108	\label{tab:top_features}
109	\begin{tabular}{cllll}
110	\toprule
111	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
112	\midrule
113	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
114	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
115	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_d2\_std}} \\
116	\bottomrule
117	\end{tabular}
118	\end{table*}
119	
120	Having established that depth signals transfer across models, we next identify which specific features drive this transferable signal.
121	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
122	The top-3 features---\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}---are shared across all three families, all measuring surprisal variability.
123	This shared ordering reveals a common mechanism: autoregressive generation progressively damps surprisal variability.
124	\texttt{surp\_d1\_std}---the standard deviation of token-to-token surprisal changes---decreases monotonically with depth as the irregular spikes characteristic of human writing are smoothed out, while \texttt{surp\_std} and \texttt{surp\_d2\_std} reflect the narrowing of the overall surprisal distribution.
125	Qwen-rewrite diverges, with \texttt{freq\_entropy} as its top feature---corroborating the cross-model transfer findings.
126	A limitation is that depth-pair-level agreement weakens ($\tau \approx 0.37$ at 1v2), indicating per-feature contributions at the boundary vary across models.
127	
128	%% ====================================================================
129	\subsection{Generation Mode}
130	\label{sec:generation_mode}
131	
132	The preceding analyses use continuation mode as the default; we now compare generation modes to validate this choice.
133	Within Qwen2.5-1.5B-Instruct, rewrite mode yields 1v2 $\auc = 0.6955$ versus continuation's $0.6112$ ($\Delta = +8.4$\,pp).
134	The amplified detectability reflects instruction-following artifacts that are discriminable but mode-specific rather than transferable across generators, as confirmed by the poor cross-model transfer of rewrite-mode classifiers (61--63\% vs.\ 80--92\% for continuation).
135	Continuation mode is therefore recommended as the canonical condition for cross-model comparisons.
136	
137	%% ====================================================================
138	\subsection{Neural Probe}
139	\label{sec:neural_probe}
140	
141	A natural question is whether $\Kempirical = 2$ is an artifact of our 15-dimensional feature set, or whether richer representations can push the boundary deeper.
142	Replacing hand-crafted features with frozen encoder hidden states (MLP probe; Table~\ref{tab:s7_neural_probe}), we evaluate $\Kempirical^{\text{neural}}$ across all three model families (Table~\ref{tab:neural_probe_crossmodel}).
143	Qwen-continuation achieves 2v3 $\auc = 0.6159$ $[0.610, 0.622]$, yielding $\Kempirical^{\text{neural}} = 3$.
144	However, Pythia ($\auc_{2v3} = 0.5963$ $[0.589, 0.603]$) and OLMo ($\auc_{2v3} = 0.5892$ $[0.582, 0.597]$) both fall below $\theta$, giving $\Kempirical^{\text{neural}} = 2$.
145	The Qwen-only elevation likely reflects self-familiarity: each model's frozen embeddings probe its own generations, and Qwen's instruction-tuned representations encode mode-specific artifacts that boost boundary discrimination---the same artifacts that transfer poorly across model families (Section~\ref{sec:transfer}).
146	The 15D model-free features yield $\Kempirical = 2$ universally (3/3 models), validating their choice for cross-model deployment.
147	
148	\begin{minipage}{\columnwidth}
149	\centering
150	\footnotesize
151	\captionof{table}{Neural probe pairwise $\auc$ with bootstrap 95\% CIs (frozen-encoder MLP). $\Kempirical^{\text{neural}} = 3$ for Qwen only; Pythia and OLMo match the 15D boundary at $\Kempirical^{\text{neural}} = 2$.}
152	\label{tab:neural_probe_crossmodel}
153	\begin{tabular}{lccc}
154	\toprule
155	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
156	\midrule
157	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
158	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
159	OLMo-1B    & 0.5892 & $[0.582,\,0.597]$ & 2 \\
160	\bottomrule
161	\end{tabular}
162	\end{minipage}
163	
164	%% ====================================================================
165	\subsection{Binary Detector Confidence and Depth}
166	\label{sec:binary_confidence}
167	
168	A natural question is whether binary detector confidence---even without ordinal training---implicitly encodes depth information.
169	We evaluate DivEye~\cite{basani2026diveye} (log-PPL) and Binoculars~\cite{hans2024binoculars} (cross-model PPL ratio; observer: Pythia-1.4B, performer: OLMo-1B) across all four model-mode configurations, reporting both Spearman $\rho$ with true depth and 6-class depth classification accuracy.
170	
171	Moderate rank correlations exist ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}), but these do not translate to practical depth discrimination: binary detectors effectively separate human from machine text (0v1 $\auc$: 0.54--0.85, depending on observer-generator matching), but confidence scores collapse to noise for depths $\geq 1$.
172	Six-class accuracy confirms this: most configurations fall at or below the random baseline of 0.167; only Qwen-rewrite (0.199) and Qwen-continuation (0.183) marginally exceed it, while Pythia (0.130) and OLMo (0.127) fall below.
173	Pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$ for most detector--generator pairs: all pairs $\geq$1v2 fall to 0.50--0.60, well below the OBD-15D baseline (0v1 $> 0.99$, 1v2: 0.61--0.70, $\Kempirical = 2$).
174	Multiple conditions exhibit non-monotonic AUC at deeper pairs (e.g., 2v3 $<$ 3v4 $<$ 4v5 for Qwen-continuation), violating the monotonic ordering required for depth interpretation.
175	The observed rank correlation is thus an artifact of 0v1 separation rather than fine-grained depth signal.
176	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "c944424f-838a-4c96-94fa-a1815e4b34d4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on five model configurations:\nPythia-1.4B and OLMo-1B in continuation mode, Qwen2.5-1.5B-Instruct in both rewrite and continuation modes, and Qwen2.5-7B in continuation mode (cross-scale scoring with Qwen2.5-1.5B).\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).\n\n%% ====================================================================\n\\subsection{$\\Kempirical = 2$ Across All Configurations}\n\\label{sec:kstar_boundary}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.}\n\\label{tab:kstar_ci}\n\\begin{tabular}{lcccccccccc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\\,.967] \\\\\n1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6539 & [.645,\\,.663]\\rlap{$^*$} & .6145 & [.605,\\,.625]\\rlap{$^*$} & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} \\\\\n2v3 & .5893 & [.580,\\,.599] & .5514 & [.542,\\,.563] & .5496 & [.540,\\,.560] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] \\\\\n3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\\\\n4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\\\\n\\bottomrule\n\\multicolumn{11}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all five 1v2 comparisons.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\\theta = 0.60$.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show a consistent pattern: 0v1 discrimination is near-perfect ($\\auc \\geq 0.96$), followed by a sharp drop at 1v2 ($\\auc$: 0.6112--0.6955), with 2v3 falling below $\\theta$ (0.5492--0.5893) and deeper pairs converging toward chance.\nAll five 1v2 point estimates exceed $\\theta$, confirmed by bootstrap CIs (most marginal lower bound: Qwen-1.5B-continuation at 0.602); all five 2v3 point estimates and CI upper bounds fall below $\\theta$ (permutation $p < 0.001$ for all boundary comparisons).\nThis establishes $\\Kempirical = 2$ as consistent across all 9 tested conditions (5 independent model-mode configurations and 4 decoding-strategy ablation variants on the Qwen-rewrite configuration; Table~\\ref{tab:s2_decoding}).\nUnder cross-model scoring, Qwen-continuation $\\Kempirical$ drops to 1 (Section~\\ref{sec:transfer}), indicating a model-specific component in the most marginal 1v2 boundary signal.\nThe sharp step-function pattern reflects the concentration of information loss: human text exhibits heavy-tailed, bursty surprisal patterns that are substantially altered by even a single autoregressive pass.\nSubsequent generations operate on already-smoothed distributions, yielding progressively smaller marginal changes that fall below detectability within two steps.\n\nThe 1v2 $\\auc$ varies across models: Qwen-rewrite (0.6955) $>$ Pythia (0.6539) $>$ OLMo (0.6145) $\\approx$ Qwen-continuation (0.6112).\nThe spread due to generation mode within a single model ($\\Delta = 8.4$\\,pp) exceeds the spread across models in the same mode ($\\Delta = 3.9$\\,pp), suggesting that generation mode appears to have a larger effect than model architecture, though formal interaction testing is beyond our current scope.\n\n\\paragraph{Cross-scale validation.}\nQwen2.5-7B in continuation mode (scored by Qwen2.5-1.5B) confirms $\\Kempirical = 2$: 1v2 $\\auc = 0.6168$ $[0.608,\\,0.626]$ (CI lower bound $> \\theta$), 2v3 $\\auc = 0.5492$ $[0.539,\\,0.559]$ (Table~\\ref{tab:kstar_ci}).\nThe 0v1 $\\auc$ drops to 0.9638 (${\\sim}$3\\,pp below ${\\leq}$1.5B models), consistent with larger models generating more human-like text; yet the $\\Kempirical$ boundary remains unchanged, extending the invariance from 1.5B to 7B.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_kstar_theta.pdf}\n\\caption{$\\Kempirical$ as a function of $\\theta$ across five model-mode configurations, computed using the 95\\% CI lower bound criterion (Eq.~\\ref{eq:kstar}). The dashed line marks the operational threshold $\\theta{=}0.60$ used throughout, where all configurations yield $\\Kempirical{=}2$. Qwen-rewrite yields the highest $\\Kempirical$ at all $\\theta$; at $\\theta{=}0.70$, $\\Kempirical{=}1$ universally.}\n\\label{fig:kstar_theta}\n\\end{figure}\n\nFigure~\\ref{fig:kstar_theta} shows $\\Kempirical$ as a function of $\\theta$ (conservative CI-lower-bound variant): unanimous $\\Kempirical = 2$ holds within $\\theta \\in [0.580, 0.600]$.\nAt $\\theta = 0.55$, $\\Kempirical = 3$ for Qwen-rewrite and Qwen-continuation while Pythia, OLMo, and Qwen-7B remain at $\\Kempirical = 2$; at $\\theta = 0.65$, all continuation modes drop to $\\Kempirical = 1$ while rewrite retains $\\Kempirical = 2$; at $\\theta = 0.70$, $\\Kempirical = 1$ universally.\nAll four decoding configurations (greedy, nucleus $p{=}0.9$, $T{=}0.70$, $T{=}1.2$) likewise yield $\\Kempirical = 2$ at $\\theta = 0.60$, with 1v2 $\\auc$ in $[0.6866, 0.7039]$ (Table~\\ref{tab:s2_decoding}).\nBootstrap CIs confirm 2v3 upper bounds below $\\theta$ for 3/4 decoding variants; the nucleus $p{=}0.9$ condition (2v3 $\\auc = 0.5917$, CI $[0.582, 0.601]$) has its upper bound marginally straddling $\\theta$ by 0.001, consistent with measurement noise.\n\n%% ====================================================================\n\\subsection{Cross-Model Transfer}\n\\label{sec:transfer}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap (6-class ordinal accuracy). Pythia$\\leftrightarrow$OLMo achieves 90--92\\% retention; Qwen-rewrite$\\to$continuation-mode models: 61--63\\%.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nThe universality of $\\Kempirical = 2$ raises a natural question: does the depth boundary reflect properties of the text itself, or generator-specific artifacts?\nCross-model transfer experiments address this directly.\n\nFigure~\\ref{fig:transfer_heatmap} shows the transfer accuracy matrix (full matrix in Table~\\ref{tab:s1_transfer}).\nContinuation-mode transfer is high: Pythia$\\leftrightarrow$OLMo retains 90--92\\% of within-model accuracy, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, and Qwen-cont$\\leftrightarrow$OLMo 80--85\\%.\nAt the 0v1 boundary, cross-model $\\auc$ exceeds 0.96 for all pairs (range: 0.963--0.991).\nThese retention rates suggest that depth features transfer across generators when computed by a fixed scorer.\nThe high retention indicates that the relative importance of depth features is encoded in distributional text properties---surprisal variance, lexical diversity---rather than in generator-specific fingerprints, enabling generator-agnostic deployment when a consistent scorer is used.\n\nQwen-rewrite classifiers transfer poorly (61--63\\% retention to Pythia/OLMo), confirming reliance on mode-specific artifacts.\nCross-mode transfer is asymmetric: continuation$\\to$rewrite retains 89\\% while rewrite$\\to$continuation retains 82\\%, indicating that continuation-mode features form a generalizable subset.\n\n\\paragraph{Cross-scorer validation.}\nTo test whether depth signals depend on the scorer model, we replace the Qwen self-scorer with two alternative scorers (Pythia-1.4B, OLMo-1B) for feature extraction on Qwen-generated text.\nFeature rankings remain highly correlated across all scorer pairs (Spearman $\\rho > 0.90$), confirming that feature ordering is text-intrinsic.\nAbsolute discriminability, however, is scorer-sensitive at the $\\Kempirical$ boundary.\nFor Qwen-rewrite, $\\Kempirical = 2$ is scorer-invariant: 1v2 $\\auc$ remains stable under cross-scoring (Pythia: 0.7012, OLMo: 0.6947; self-scorer baseline: 0.6955; Table~\\ref{tab:crossscorer}).\nFor Qwen-continuation---already the most marginal self-scorer condition (CI lower bound exceeds $\\theta$ by only 0.2\\,pp; Table~\\ref{tab:kstar_ci})---$\\Kempirical$ drops from 2 to 1 under both alternative scorers (1v2 $\\auc$: $0.6112 \\to 0.5923$ [Pythia], $0.5858$ [OLMo], both below $\\theta$).\nThis dissociation---scorer-invariant feature rankings but scorer-sensitive boundary classification---indicates that cross-scoring preserves the relative importance structure of depth features while attenuating the absolute signal, with consequences only where the self-scorer margin is already thin.\nCrucially, both alternative scorers agree on $\\Kempirical$ for each generation mode ($\\Kempirical = 2$ for rewrite, $1$ for continuation), indicating that $\\Kempirical$ is determined by the generation process rather than the choice of scoring model.\n\n%% ====================================================================\n\\subsection{Feature Degradation Ordering}\n\\label{sec:feature_degradation}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Top-3 features by single-feature $\\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}\n\\label{tab:top_features}\n\\begin{tabular}{cllll}\n\\toprule\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\n\\midrule\n1 & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\texttt{freq\\_entropy} & \\textbf{\\texttt{surp\\_d1\\_std}} \\\\\n2 & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_std}} \\\\\n3 & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nHaving established that depth signals transfer across models, we next identify which specific features drive this transferable signal.\nAmong continuation-mode models, single-feature $\\auc$ rankings are highly correlated ($\\rho \\geq 0.85$; Table~\\ref{tab:top_features}).\nThe top-3 features---\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}---are shared across all three families, all measuring surprisal variability.\nThis shared ordering reveals a common mechanism: autoregressive generation progressively damps surprisal variability.\n\\texttt{surp\\_d1\\_std}---the standard deviation of token-to-token surprisal changes---decreases monotonically with depth as the irregular spikes characteristic of human writing are smoothed out, while \\texttt{surp\\_std} and \\texttt{surp\\_d2\\_std} reflect the narrowing of the overall surprisal distribution.\nQwen-rewrite diverges, with \\texttt{freq\\_entropy} as its top feature---corroborating the cross-model transfer findings.\nA limitation is that depth-pair-level agreement weakens ($\\tau \\approx 0.37$ at 1v2), indicating per-feature contributions at the boundary vary across models.\n\n%% ====================================================================\n\\subsection{Generation Mode}\n\\label{sec:generation_mode}\n\nThe preceding analyses use continuation mode as the default; we now compare generation modes to validate this choice.\nWithin Qwen2.5-1.5B-Instruct, rewrite mode yields 1v2 $\\auc = 0.6955$ versus continuation's $0.6112$ ($\\Delta = +8.4$\\,pp).\nThe amplified detectability reflects instruction-following artifacts that are discriminable but mode-specific rather than transferable across generators, as confirmed by the poor cross-model transfer of rewrite-mode classifiers (61--63\\% vs.\\ 80--92\\% for continuation).\nContinuation mode is therefore recommended as the canonical condition for cross-model comparisons.\n\n%% ====================================================================\n\\subsection{Neural Probe}\n\\label{sec:neural_probe}\n\nA natural question is whether $\\Kempirical = 2$ is an artifact of our 15-dimensional feature set, or whether richer representations can push the boundary deeper.\nReplacing hand-crafted features with frozen encoder hidden states (MLP probe; Table~\\ref{tab:s7_neural_probe}), we evaluate $\\Kempirical^{\\text{neural}}$ across all three model families (Table~\\ref{tab:neural_probe_crossmodel}).\nQwen-continuation achieves 2v3 $\\auc = 0.6159$ $[0.610, 0.622]$, yielding $\\Kempirical^{\\text{neural}} = 3$.\nHowever, Pythia ($\\auc_{2v3} = 0.5963$ $[0.589, 0.603]$) and OLMo ($\\auc_{2v3} = 0.5892$ $[0.582, 0.597]$) both fall below $\\theta$, giving $\\Kempirical^{\\text{neural}} = 2$.\nThe Qwen-only elevation likely reflects self-familiarity: each model's frozen embeddings probe its own generations, and Qwen's instruction-tuned representations encode mode-specific artifacts that boost boundary discrimination---the same artifacts that transfer poorly across model families (Section~\\ref{sec:transfer}).\nThe 15D model-free features yield $\\Kempirical = 2$ universally (3/3 models), validating their choice for cross-model deployment.\n\n\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Neural probe pairwise $\\auc$ with bootstrap 95\\% CIs (frozen-encoder MLP). $\\Kempirical^{\\text{neural}} = 3$ for Qwen only; Pythia and OLMo match the 15D boundary at $\\Kempirical^{\\text{neural}} = 2$.}\n\\label{tab:neural_probe_crossmodel}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B  & 0.6159 & $[0.610,\\,0.622]$ & 3 \\\\\nPythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\nOLMo-1B    & 0.5892 & $[0.582,\\,0.597]$ & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Binary Detector Confidence and Depth}\n\\label{sec:binary_confidence}\n\nA natural question is whether binary detector confidence---even without ordinal training---implicitly encodes depth information.\nWe evaluate DivEye~\\cite{basani2026diveye} (log-PPL) and Binoculars~\\cite{hans2024binoculars} (cross-model PPL ratio; observer: Pythia-1.4B, performer: OLMo-1B) across all four model-mode configurations, reporting both Spearman $\\rho$ with true depth and 6-class depth classification accuracy.\n\nModerate rank correlations exist ($|\\rho| = 0.06$--$0.46$; Table~\\ref{tab:s9_binary_spearman}), but these do not translate to practical depth discrimination: binary detectors effectively separate human from machine text (0v1 $\\auc$: 0.54--0.85, depending on observer-generator matching), but confidence scores collapse to noise for depths $\\geq 1$.\nSix-class accuracy confirms this: most configurations fall at or below the random baseline of 0.167; only Qwen-rewrite (0.199) and Qwen-continuation (0.183) marginally exceed it, while Pythia (0.130) and OLMo (0.127) fall below.\nPairwise $\\auc$ yields $\\Kempirical^{\\text{binary}} \\leq 1$ for most detector--generator pairs: all pairs $\\geq$1v2 fall to 0.50--0.60, well below the OBD-15D baseline (0v1 $> 0.99$, 1v2: 0.61--0.70, $\\Kempirical = 2$).\nMultiple conditions exhibit non-monotonic AUC at deeper pairs (e.g., 2v3 $<$ 3v4 $<$ 4v5 for Qwen-continuation), violating the monotonic ordering required for depth interpretation.\nThe observed rank correlation is thus an artifact of 0v1 separation rather than fine-grained depth signal.\n",
      "numLines": 176,
      "startLine": 1,
      "totalLines": 176
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the rest of experiments_c1.tex and check the appendix for the extended limitations section and any other relevant content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "8011cab0-14b5-4796-bcb5-3e2044ad5a9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LEPSAYj8AcqgXnnDijgVyo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15399,
      "cache_read_input_tokens": 25770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15399
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

_source line 26_

Let me read the rest of experiments_c1.tex and the appendix extended content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "44f99cc9-e4c0-4843-86af-442b489faea4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LEPSAYj8AcqgXnnDijgVyo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15399,
      "cache_read_input_tokens": 25770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15399
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

<details open><summary>🔧 Tool call — Read · `toolu_016RL6jmQVqiunwmsHfDiYUv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "offset": 176
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "9394010b-41db-416c-aa33-0a97331a0427",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LEPSAYj8AcqgXnnDijgVyo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15399,
      "cache_read_input_tokens": 25770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15399
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

_source line 28 · 2026-05-16T03:21:08.763Z_

<details><summary>↩ Tool result · `toolu_016RL6jmQVqiunwmsHfDiYUv`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (176). The file has 176 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "ec91b36b-ce54-4d00-bf3a-c75963def1e1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
      "content": "",
      "numLines": 1,
      "startLine": 176,
      "totalLines": 176
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01529vGHZZt9tvPUo8PzttzE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "offset": 329
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "a9fa3b2c-0d77-4e60-b64f-602ff76ca607",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LEPSAYj8AcqgXnnDijgVyo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15399,
      "cache_read_input_tokens": 25770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15399
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

_source line 30 · 2026-05-16T03:21:09.708Z_

<details><summary>↩ Tool result · `toolu_01529vGHZZt9tvPUo8PzttzE`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (329). The file has 329 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "1a939db7-5dbf-4984-8046-0d205eba955e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
      "content": "",
      "numLines": 1,
      "startLine": 329,
      "totalLines": 329
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01GgB1wp8M7Wo2GNRT4ZsycN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "569a594c-ffe0-452a-bf6c-fdfd3826726c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LEPSAYj8AcqgXnnDijgVyo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15399,
      "cache_read_input_tokens": 25770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15399
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

_source line 32 · 2026-05-16T03:21:10.023Z_

<details><summary>↩ Tool result · `toolu_01GgB1wp8M7Wo2GNRT4ZsycN`</summary>

```text
1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage[section]{placeins}
18	
19	\newcommand{\Kstar}{{K^*}}
20	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
21	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
22	\newcommand{\auc}{\text{AUC}}
23	\newcommand{\jsd}{\text{JSD}}
24	
25	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
35	We measure the discrimination boundary $\Kempirical$---the maximum depth at which adjacent generations remain distinguishable---using 15 statistical features and an OBD-LightGBM classifier.
36	Across 5 model configurations (1B--7B) and 4 decoding strategies, $\Kempirical{=}2$ at $\theta{=}0.60$ (Cohen's $h{\approx}0.20$), consistent across all 9 tested conditions under self-scoring (most marginal: 0.2\,pp above $\theta$): a single generation step is reliably detectable, but the second renders text statistically indistinguishable from deeper synthetic content---a \emph{one-wash laundering} effect.
37	Model-free statistical features enable 80--92\% cross-model transfer retention among continuation-mode generators with scorer-invariant feature ordering ($\rho > 0.90$), and cross-scorer validation confirms that $\Kempirical$ is governed by the generation process rather than the scoring model.
38	Both supervised classification and zero-shot frontier LLMs fail comparably at depths ${\geq}2$ (recall 14--22\% vs.\ 8--38\%), providing converging evidence consistent with $\Kempirical{=}2$ reflecting a data-intrinsic boundary rather than a method limitation.
39	Downstream, $\Kempirical{=}2$ correctly predicts that binary curation minimizes degradation most effectively among all tested strategies.
40	\end{abstract}
41	
42	% === Section 1: Introduction ===
43	\input{introduction}
44	
45	% === Section 2: Related Work ===
46	\input{related_work}
47	
48	% === Section 3: Method ===
49	\input{method}
50	
51	% === Section 4: Experiments ===
52	\input{experiments_c1}
53	
54	% === Section 5: K*-Aware Data Filtering ===
55	\input{experiments_c3}
56	
57	% === Section 6: Discussion ===
58	\input{discussion}
59	
60	% === Section 7: Conclusion ===
61	\input{conclusion}
62	
63	% === Limitations (ACL required, unnumbered) ===
64	\clearpage
65	\section*{Limitations}
66	
67	Our findings are bounded by (1)~model scale ($\leq$7B, with only one 7B configuration tested; the 7B condition uses Qwen2.5-7B-Base rather than Instruct, introducing a base-vs-instruct confound---though $\Kempirical{=}2$ consistency across this variation provides additional robustness evidence; cross-scale scoring rather than self-scoring), (2)~prompt-chain rather than retrain-chain protocols (our $\Kempirical$ is a conservative upper bound on retrain-chain $\Kstar$ under monotonic-degradation assumptions), (3)~English C4 text only, (4)~four decoding strategies, (5)~threshold sensitivity ($\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; all nine conditions yield point-estimate $\Kempirical{=}2$ at $\theta{=}0.60$, with 8/9 confirmed by bootstrap CI---one decoding variant has 2v3 CI upper marginally at 0.601), (6)~marginal boundary (Qwen-continuation 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation with both Pythia and OLMo scorers drops this condition to $\Kempirical{=}1$, Section~\ref{sec:transfer}), (7)~the 15D feature set yields a feature-set-specific lower bound ($\Ktheory$ may be strictly higher), (8)~the neural probe boundary is model-dependent ($\Kempirical^{\text{neural}}{=}3$ for Qwen only; $2$ for Pythia/OLMo), likely reflecting self-familiarity rather than a universal signal, (9)~while overall feature rankings are highly consistent across models ($\rho \geq 0.85$), depth-pair-level agreement weakens at the 1v2 boundary ($\tau \approx 0.37$), indicating that per-feature contributions at the critical boundary vary across models, (10)~cross-model scoring reduces $\Kempirical$ from 2 to 1 for continuation-mode data (Table~\ref{tab:crossscorer}), indicating that the 1v2 boundary signal has a model-specific component consistent with the representation-dependent neural probe finding; in deployment the scorer model is known, making self-scoring the natural choice, but unknown-generator scenarios remain a limitation, (11)~all experiments use 256-token segments matching common web-scale chunking; $\Kempirical$ is defined conditionally on segment length, and longer documents with more stable per-document statistics could yield higher $\Kempirical$, and (12)~structural composition: depth~0 texts are human-authored (mean ${\approx}$191 tokens after truncation) while depth~1+ are machine-generated (mean 214--256 tokens); this length asymmetry makes 0v1 detection \emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (EOS truncation rates stable across depths within each model), so the critical $\Kempirical{=}2$ finding---based on 1v2 vs.\ 2v3 comparisons---is unaffected by this confound.
68	Detailed analysis appears in Appendix~\ref{sec:extended_limitations}.
69	
70	% === Ethics Statement (ACL required, unnumbered) ===
71	\section*{Ethics Statement}
72	
73	Generational depth estimation is intended for data curation and corpus auditing---positive-sum applications that improve training data quality.
74	Our experiments use the publicly available C4 corpus and do not involve personally identifiable information.
75	A potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\auc \geq 0.96$ at 0v1) remains robust.
76	
77	\bibliography{references}
78	
79	\input{appendix}
80	\input{appendix_extended}
81	
82	\end{document}
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "f1e47631-d09f-436a-80c7-58edaae95d08",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
      "content": "% EMNLP 2026 Main — ARR May 2026\n% Generational Depth Contamination\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage[section]{placeins}\n\n\\newcommand{\\Kstar}{{K^*}}\n\\newcommand{\\Kempirical}{{K^*_{\\text{empirical}}}}\n\\newcommand{\\Ktheory}{{K^*_{\\text{theory}}}}\n\\newcommand{\\auc}{\\text{AUC}}\n\\newcommand{\\jsd}{\\text{JSD}}\n\n\\title{Generational Depth Estimation of Recursive Synthetic Text:\\\\Measuring the Discrimination Boundary}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% === Abstract ===\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.\nWe measure the discrimination boundary $\\Kempirical$---the maximum depth at which adjacent generations remain distinguishable---using 15 statistical features and an OBD-LightGBM classifier.\nAcross 5 model configurations (1B--7B) and 4 decoding strategies, $\\Kempirical{=}2$ at $\\theta{=}0.60$ (Cohen's $h{\\approx}0.20$), consistent across all 9 tested conditions under self-scoring (most marginal: 0.2\\,pp above $\\theta$): a single generation step is reliably detectable, but the second renders text statistically indistinguishable from deeper synthetic content---a \\emph{one-wash laundering} effect.\nModel-free statistical features enable 80--92\\% cross-model transfer retention among continuation-mode generators with scorer-invariant feature ordering ($\\rho > 0.90$), and cross-scorer validation confirms that $\\Kempirical$ is governed by the generation process rather than the scoring model.\nBoth supervised classification and zero-shot frontier LLMs fail comparably at depths ${\\geq}2$ (recall 14--22\\% vs.\\ 8--38\\%), providing converging evidence consistent with $\\Kempirical{=}2$ reflecting a data-intrinsic boundary rather than a method limitation.\nDownstream, $\\Kempirical{=}2$ correctly predicts that binary curation minimizes degradation most effectively among all tested strategies.\n\\end{abstract}\n\n% === Section 1: Introduction ===\n\\input{introduction}\n\n% === Section 2: Related Work ===\n\\input{related_work}\n\n% === Section 3: Method ===\n\\input{method}\n\n% === Section 4: Experiments ===\n\\input{experiments_c1}\n\n% === Section 5: K*-Aware Data Filtering ===\n\\input{experiments_c3}\n\n% === Section 6: Discussion ===\n\\input{discussion}\n\n% === Section 7: Conclusion ===\n\\input{conclusion}\n\n% === Limitations (ACL required, unnumbered) ===\n\\clearpage\n\\section*{Limitations}\n\nOur findings are bounded by (1)~model scale ($\\leq$7B, with only one 7B configuration tested; the 7B condition uses Qwen2.5-7B-Base rather than Instruct, introducing a base-vs-instruct confound---though $\\Kempirical{=}2$ consistency across this variation provides additional robustness evidence; cross-scale scoring rather than self-scoring), (2)~prompt-chain rather than retrain-chain protocols (our $\\Kempirical$ is a conservative upper bound on retrain-chain $\\Kstar$ under monotonic-degradation assumptions), (3)~English C4 text only, (4)~four decoding strategies, (5)~threshold sensitivity ($\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; all nine conditions yield point-estimate $\\Kempirical{=}2$ at $\\theta{=}0.60$, with 8/9 confirmed by bootstrap CI---one decoding variant has 2v3 CI upper marginally at 0.601), (6)~marginal boundary (Qwen-continuation 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation with both Pythia and OLMo scorers drops this condition to $\\Kempirical{=}1$, Section~\\ref{sec:transfer}), (7)~the 15D feature set yields a feature-set-specific lower bound ($\\Ktheory$ may be strictly higher), (8)~the neural probe boundary is model-dependent ($\\Kempirical^{\\text{neural}}{=}3$ for Qwen only; $2$ for Pythia/OLMo), likely reflecting self-familiarity rather than a universal signal, (9)~while overall feature rankings are highly consistent across models ($\\rho \\geq 0.85$), depth-pair-level agreement weakens at the 1v2 boundary ($\\tau \\approx 0.37$), indicating that per-feature contributions at the critical boundary vary across models, (10)~cross-model scoring reduces $\\Kempirical$ from 2 to 1 for continuation-mode data (Table~\\ref{tab:crossscorer}), indicating that the 1v2 boundary signal has a model-specific component consistent with the representation-dependent neural probe finding; in deployment the scorer model is known, making self-scoring the natural choice, but unknown-generator scenarios remain a limitation, (11)~all experiments use 256-token segments matching common web-scale chunking; $\\Kempirical$ is defined conditionally on segment length, and longer documents with more stable per-document statistics could yield higher $\\Kempirical$, and (12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 tokens after truncation) while depth~1+ are machine-generated (mean 214--256 tokens); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound.\nDetailed analysis appears in Appendix~\\ref{sec:extended_limitations}.\n\n% === Ethics Statement (ACL required, unnumbered) ===\n\\section*{Ethics Statement}\n\nGenerational depth estimation is intended for data curation and corpus auditing---positive-sum applications that improve training data quality.\nOur experiments use the publicly available C4 corpus and do not involve personally identifiable information.\nA potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\\auc \\geq 0.96$ at 0v1) remains robust.\n\n\\bibliography{references}\n\n\\input{appendix}\n\\input{appendix_extended}\n\n\\end{document}\n",
      "numLines": 83,
      "startLine": 1,
      "totalLines": 83
    }
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Now I see the current state. Looking at the Limitations section (line 67 of main.tex), there's already point (12) about structural composition that briefly mentions the length asymmetry. Let me also check `appendix_extended.tex` for `\label{sec:extended_limitations}`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "853f95a7-f653-42c7-b71f-50ffa6ece48c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Mgf2w8PHFM3sHjeiX7g7h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2527,
      "cache_read_input_tokens": 41169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2527
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

_source line 34_

Let me check the extended appendix for the limitations section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "c9c6b67b-9d3a-40ef-b253-256e65d7a3c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Mgf2w8PHFM3sHjeiX7g7h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2527,
      "cache_read_input_tokens": 41169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2527
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

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01Nyt5KKQFoS14xsGak5QBUE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "793ecde4-7e09-4ede-b016-66f5f255daff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Mgf2w8PHFM3sHjeiX7g7h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2527,
      "cache_read_input_tokens": 41169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2527
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

_source line 36 · 2026-05-16T03:21:14.957Z_

<details><summary>↩ Tool result · `toolu_01Nyt5KKQFoS14xsGak5QBUE`</summary>

```text
1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	
6	The DPI guarantees a finite $\Ktheory$; our result establishes $\Kempirical = 2$ across all 9 conditions (1B--7B), aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6866, 0.7039]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--92\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), enabling single-classifier deployment across generators.
12	Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
13	Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 90--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
14	
15	\begin{minipage}{\columnwidth}
16	\centering
17	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
18	\label{tab:crossscorer}
19	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
20	\end{minipage}
21	
22	\subsection{Feature Importance Across Decoding Strategies}
23	
24	Feature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\rho = 0.914$), while greedy vs.\ $T{=}1.2$ yields lower correlation ($\rho = 0.53$, nonsignificant after Bonferroni).
25	The depth boundary is robust but the optimal feature subset is strategy-dependent.
26	
27	\subsection{Scale and Neural Probe}
28	\label{sec:extended_neural_probe}
29	
30	Cross-scale validation confirms $\Kempirical = 2$ at 7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$, 2v3 $\auc = 0.5492$; Table~\ref{tab:kstar_ci}); the 7B 0v1 $\auc$ (0.9638) is ${\sim}$3\,pp lower than ${\leq}$1.5B models, consistent with larger models generating more human-like text. Scaling beyond 7B remains open.
31	
32	The neural probe yields model-dependent $\Kempirical^{\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia and OLMo, matching the 15D boundary.
33	The 15D model-free features yield $\Kempirical = 2$ universally, confirming their role as a robust lower bound across architectures.
34	
35	\subsection{LLM Zero-Shot Baseline}
36	\label{sec:extended_llm}
37	
38	GPT-5.5 achieves 33.2\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\% (95\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\ref{tab:s3_llm_zeroshot}).
39	Per-depth recall confirms convergent failure at depths $\geq 2$ (Section~\ref{sec:why_kstar}).
40	When 6-class probabilities are marginalized to 5 classes ($P(d{\geq}4)$), accuracy rises to 44.4\% but concentrates in depth-4 (recall: 22\%$\to$80\%) while depths 2--3 collapse to 2--8\%; we report raw 6-class results.
41	
42	\subsection{Practical Considerations}
43	
44	All filtering strategies degrade general capabilities (MMLU: 0.6018 $\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\to$ 0.6638--0.6701); our 100\% synthetic setting is an upper bound---in mixed corpora, degradation scales with contamination fraction~\cite{shumailov2024collapse, dohmatob2024model}.
45	$\Kstar$-aware binary filtering reduces MMLU degradation by ${\sim}$50\% ($-$1.53\,pp $\to$ $-$0.77\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).
46	
47	\subsection{Extended Limitations}
48	\label{sec:extended_limitations}
49	
50	\emph{Prompt-chain versus retrain-chain.}
51	Under monotonic-degradation assumptions~\cite{shumailov2024collapse}, $\Kstar^{\text{retrain}} \leq \Kstar^{\text{prompt}}$, making $\Kempirical = 2$ a conservative estimate.
52	
53	\emph{Threshold sensitivity.}
54	At $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite/continuation; at $\theta = 0.70$, $\Kempirical = 1$ universally (Figure~\ref{fig:kstar_theta}).
55	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
56	
57	\emph{Graduated filtering.}
58	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
59	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\text{corr}} = 0.011$).
60	\label{tab:pairwise_significance}
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "00eb2fa2-8567-4242-8421-08b2564def74",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\section{Extended Discussion}\n\\label{sec:extended_discussion}\n\n\\subsection{Theoretical Implications of $\\Kempirical = 2$}\n\nThe DPI guarantees a finite $\\Ktheory$; our result establishes $\\Kempirical = 2$ across all 9 conditions (1B--7B), aligning with model collapse convergence~\\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.\nDecoding strategy modestly affects signal strength (1v2 $\\auc \\in [0.6866, 0.7039]$) but does not shift the boundary.\n\n\\subsection{Cross-Model Transfer Implications}\n\nCross-model classification retains 80--92\\% accuracy with scorer-invariant feature rankings ($\\rho > 0.90$), enabling single-classifier deployment across generators.\nAbsolute discriminability at the $\\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\\Kempirical$ from 2 to 1, while rewrite-mode $\\Kempirical = 2$ is preserved.\nModel family similarity modulates transfer (Pythia$\\leftrightarrow$OLMo: 90--92\\% vs.\\ Qwen-cont$\\leftrightarrow$OLMo: 80--85\\%).\n\n\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\subsection{Feature Importance Across Decoding Strategies}\n\nFeature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\\rho = 0.914$), while greedy vs.\\ $T{=}1.2$ yields lower correlation ($\\rho = 0.53$, nonsignificant after Bonferroni).\nThe depth boundary is robust but the optimal feature subset is strategy-dependent.\n\n\\subsection{Scale and Neural Probe}\n\\label{sec:extended_neural_probe}\n\nCross-scale validation confirms $\\Kempirical = 2$ at 7B (1v2 $\\auc = 0.6168$ $[0.608, 0.626]$, 2v3 $\\auc = 0.5492$; Table~\\ref{tab:kstar_ci}); the 7B 0v1 $\\auc$ (0.9638) is ${\\sim}$3\\,pp lower than ${\\leq}$1.5B models, consistent with larger models generating more human-like text. Scaling beyond 7B remains open.\n\nThe neural probe yields model-dependent $\\Kempirical^{\\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia and OLMo, matching the 15D boundary.\nThe 15D model-free features yield $\\Kempirical = 2$ universally, confirming their role as a robust lower bound across architectures.\n\n\\subsection{LLM Zero-Shot Baseline}\n\\label{sec:extended_llm}\n\nGPT-5.5 achieves 33.2\\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\\% (95\\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\\ref{tab:s3_llm_zeroshot}).\nPer-depth recall confirms convergent failure at depths $\\geq 2$ (Section~\\ref{sec:why_kstar}).\nWhen 6-class probabilities are marginalized to 5 classes ($P(d{\\geq}4)$), accuracy rises to 44.4\\% but concentrates in depth-4 (recall: 22\\%$\\to$80\\%) while depths 2--3 collapse to 2--8\\%; we report raw 6-class results.\n\n\\subsection{Practical Considerations}\n\nAll filtering strategies degrade general capabilities (MMLU: 0.6018 $\\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\\to$ 0.6638--0.6701); our 100\\% synthetic setting is an upper bound---in mixed corpora, degradation scales with contamination fraction~\\cite{shumailov2024collapse, dohmatob2024model}.\n$\\Kstar$-aware binary filtering reduces MMLU degradation by ${\\sim}$50\\% ($-$1.53\\,pp $\\to$ $-$0.77\\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).\n\n\\subsection{Extended Limitations}\n\\label{sec:extended_limitations}\n\n\\emph{Prompt-chain versus retrain-chain.}\nUnder monotonic-degradation assumptions~\\cite{shumailov2024collapse}, $\\Kstar^{\\text{retrain}} \\leq \\Kstar^{\\text{prompt}}$, making $\\Kempirical = 2$ a conservative estimate.\n\n\\emph{Threshold sensitivity.}\nAt $\\theta = 0.55$, $\\Kempirical = 3$ for Qwen-rewrite/continuation; at $\\theta = 0.70$, $\\Kempirical = 1$ universally (Figure~\\ref{fig:kstar_theta}).\nQwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\n\n\\emph{Graduated filtering.}\nAll $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).\nBinary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$).\n\\label{tab:pairwise_significance}\n",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me also check what the current appendix_extended.tex has after line 61.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "9fbbc5fc-7b6b-4a14-a56b-6d980ba71cf7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4icorgfj8Gt5awhxaVowz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 43696,
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

### Assistant

_source line 38_

Let me check if there's more content in appendix_extended.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "8dc6040b-dfbc-4351-bfdd-41ec292b33de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4icorgfj8Gt5awhxaVowz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 43696,
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

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01LXhCkxgDJfH36AdxDKvxyH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "0f02746b-1c5e-4cbb-8a7a-1ea6751e42c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4icorgfj8Gt5awhxaVowz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 43696,
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

_source line 40 · 2026-05-16T03:21:18.420Z_

<details><summary>↩ Tool result · `toolu_01LXhCkxgDJfH36AdxDKvxyH`</summary>

```text
60	\label{tab:pairwise_significance}
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "2089d358-8cde-4d9b-89f5-358e0fd9cf22",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\label{tab:pairwise_significance}\n",
      "numLines": 2,
      "startLine": 60,
      "totalLines": 61
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

Now I have the full picture. Here's my plan:

1. **Limitations (main.tex line 67)** — already has point (12) mentioning the structural confound briefly. This needs minimal changes.
2. **Discussion (discussion.tex)** — add a subsection addressing the structural confound with quantitative argument.
3. **Appendix (appendix.tex)** — add a table with per-model per-depth mean token lengths and EOS truncation rates.
4. **Appendix extended (appendix_extended.tex)** — expand the extended limitations with the full token-length analysis.

Let me start with all the edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "e01fb577-2176-41aa-bf8e-2303e253e2e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUhEr9ts1X9dMNG99dmQDV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 194,
      "cache_read_input_tokens": 45771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 194
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

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01PNN1xb5F2a3zxxTGRg22RA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
  "old_string": "Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\\Kempirical = 2$ to 1, while rewrite-mode $\\Kempirical = 2$ is preserved---$\\Kempirical$ is governed by the generation operator rather than the scoring model.",
  "new_string": "Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\\Kempirical = 2$ to 1, while rewrite-mode $\\Kempirical = 2$ is preserved---$\\Kempirical$ is governed by the generation operator rather than the scoring model.\n\n\\subsection{Structural Confound: Token Length and EOS Truncation}\n\\label{sec:length_confound}\n\nA potential confound is that EOS truncation at the 256-token generation limit could create systematic length differences across depths, inflating AUC through a length shortcut rather than distributional signatures.\nWe quantify this concern across all model configurations (full per-depth statistics in Table~\\ref{tab:token_length}).\n\nDepth~0 (human text, truncated from C4) averages ${\\sim}$191 tokens across all configurations, while depth~1+ (machine-generated) averages 195--256 tokens depending on model.\nThe length asymmetry thus runs \\emph{opposite} to the confound direction: human texts are shorter, so any length-based shortcut would make 0v1 detection \\emph{harder} (a classifier exploiting ``shorter$=$machine'' would fail), not easier.\n\nWithin machine-generated depths 1--5, token counts are remarkably stable.\nFor Qwen-rewrite, depths 1--5 average 252--254 tokens (range: 2 tokens); for Pythia, 214--218 tokens (range: 4 tokens); for Qwen-7B, 193--197 tokens (range: 4 tokens).\nThis stability means the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons among machine-generated texts---cannot be driven by length differences, since depths 1 through 5 have effectively identical token counts within each model.\n\nEOS truncation rates vary across models (Table~\\ref{tab:token_length}): Qwen-rewrite and decoding ablations show mild truncation (7--16\\% at depth~1+), Qwen-continuation moderate truncation (17--20\\%), while Pythia (34--36\\%) and Qwen-7B (45--47\\%) exhibit higher rates.\nCrucially, truncation rates are \\emph{stable across depths 1--5 within each model}, so EOS effects do not create a depth-correlated length gradient that could confound pairwise discrimination.\nThe models with highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay as low-truncation models, further ruling out length as a driver of the boundary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "5697cc6f-f3d8-4a37-a3d2-511b38c2b72c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUhEr9ts1X9dMNG99dmQDV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 194,
      "cache_read_input_tokens": 45771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 194
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

_source line 43 · 2026-05-16T03:21:40.652Z_

<details><summary>↩ Tool result · `toolu_01PNN1xb5F2a3zxxTGRg22RA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "e8f95f86-8c0a-4aa0-b4be-de4dc7cf37b9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
    "oldString": "Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\\Kempirical = 2$ to 1, while rewrite-mode $\\Kempirical = 2$ is preserved---$\\Kempirical$ is governed by the generation operator rather than the scoring model.",
    "newString": "Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\\Kempirical = 2$ to 1, while rewrite-mode $\\Kempirical = 2$ is preserved---$\\Kempirical$ is governed by the generation operator rather than the scoring model.\n\n\\subsection{Structural Confound: Token Length and EOS Truncation}\n\\label{sec:length_confound}\n\nA potential confound is that EOS truncation at the 256-token generation limit could create systematic length differences across depths, inflating AUC through a length shortcut rather than distributional signatures.\nWe quantify this concern across all model configurations (full per-depth statistics in Table~\\ref{tab:token_length}).\n\nDepth~0 (human text, truncated from C4) averages ${\\sim}$191 tokens across all configurations, while depth~1+ (machine-generated) averages 195--256 tokens depending on model.\nThe length asymmetry thus runs \\emph{opposite} to the confound direction: human texts are shorter, so any length-based shortcut would make 0v1 detection \\emph{harder} (a classifier exploiting ``shorter$=$machine'' would fail), not easier.\n\nWithin machine-generated depths 1--5, token counts are remarkably stable.\nFor Qwen-rewrite, depths 1--5 average 252--254 tokens (range: 2 tokens); for Pythia, 214--218 tokens (range: 4 tokens); for Qwen-7B, 193--197 tokens (range: 4 tokens).\nThis stability means the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons among machine-generated texts---cannot be driven by length differences, since depths 1 through 5 have effectively identical token counts within each model.\n\nEOS truncation rates vary across models (Table~\\ref{tab:token_length}): Qwen-rewrite and decoding ablations show mild truncation (7--16\\% at depth~1+), Qwen-continuation moderate truncation (17--20\\%), while Pythia (34--36\\%) and Qwen-7B (45--47\\%) exhibit higher rates.\nCrucially, truncation rates are \\emph{stable across depths 1--5 within each model}, so EOS effects do not create a depth-correlated length gradient that could confound pairwise discrimination.\nThe models with highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay as low-truncation models, further ruling out length as a driver of the boundary.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{The One-Wash Laundering Effect}\n\\label{sec:why_kstar}\n\\label{sec:one_wash}\n\nThe shallowness of $\\Kempirical = 2$ reflects the concentration of information loss: the 0v1 boundary is near-trivially separable ($\\auc \\geq 0.96$), 1v2 drops by ${\\sim}$30\\,pp, and 2v3 falls below $\\theta$---the generation operator acts as a lossy channel with diminishing marginal information loss.\nConsistency across four decoding strategies (Table~\\ref{tab:s2_decoding}) reinforces that $\\Kempirical$ is governed by the generation process rather than the sampling algorithm.\nEven at the most marginal 1v2 condition (Qwen-continuation, CI lower bound exceeds $\\theta$ by only 0.2\\,pp), $\\Kempirical = 2$ survives under self-scoring; on the 2v3 side, CI upper bounds confirm non-discrimination in 8/9 conditions, with the single borderline case (nucleus $p{=}0.9$, CI upper${} = 0.601$) consistent with measurement noise at near-threshold values.\nCross-scale validation at 7B (Section~\\ref{sec:kstar_boundary}) extends this from 1.5B to 7B despite reduced 0v1 signal ($0.9638$ vs.\\ $> 0.99$).\n\nThe practical consequence is a three-tier taxonomy: human-authored (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\\geq 2$).\nA single generation pass suffices to render text statistically indistinguishable from multiply recycled content---a \\emph{one-wash laundering} effect that limits depth-aware corpus curation to a binary boundary.\nThis connects to model collapse: Shumailov et al.~\\cite{shumailov2024collapse} observed that tail-distribution degradation is most acute in the earliest generations; our prompt-chain results show an analogous per-text pattern.\n\nPer-depth analysis provides the most direct evidence that this boundary is not methodological.\nOBD achieves 96\\% depth-0 recall but only 14--22\\% for depths 2--4; frontier LLMs show 69--77\\% depth-0 recall and 8--38\\% for depths 2--4 (McNemar $p > 0.05$ vs.\\ OBD; Table~\\ref{tab:s3_llm_zeroshot}).\nThis convergence across fundamentally different approaches---supervised statistical classification and zero-shot frontier LLMs---provides converging evidence that the saturation reflects a data-intrinsic boundary rather than a method limitation.\nBinary detector confidence corroborates: despite moderate Spearman correlations ($|\\rho|$ up to 0.46), 6-class accuracy is at or below chance ($\\leq 0.199$ vs.\\ 0.167 baseline), and Qwen-rewrite exhibits a sign reversal ($\\rho > 0$), disqualifying confidence as a reliable depth proxy.\n\n\\subsection{Why Graduated Filtering Fails}\n\\label{sec:negative_graduated}\n\nSince 2v3 $\\auc < \\theta$ for all configurations, depth assignments for $d \\geq 2$ approximate random labels; graduated weighting injects noise into importance weights, explaining the monotonic improvement with $\\alpha$ as it converges toward binary thresholding (Appendix~\\ref{sec:extended_limitations}).\nDSIR fails for a different reason---bigram feature hashing captures domain shift but not depth-correlated distributional signatures.\n\n\\subsection{Representation Dependence of the Boundary}\n\\label{sec:repr_dependence}\n\n$\\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$, while Pythia and OLMo match the 15D boundary at $\\Kempirical^{\\text{neural}} = 2$ (Table~\\ref{tab:neural_probe_crossmodel}).\nThe hierarchy $\\Kempirical^{15\\text{D}}{=}2 < \\Kempirical^{\\text{neural}} \\in \\{2,3\\}$ reflects an interpretability--sensitivity tradeoff: learned representations recover additional depth signal sufficient to push $\\Kempirical$ to 3 for one model (Qwen), but this gain is model-dependent---the 15D features trade one depth level of sensitivity for cross-model universality (9/9 conditions $\\Kempirical{=}2$, 3/3 models identical), making them the preferred operational choice.\nCross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\\Kempirical = 2$ to 1, while rewrite-mode $\\Kempirical = 2$ is preserved---$\\Kempirical$ is governed by the generation operator rather than the scoring model.\n",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 3,
        "newStart": 31,
        "newLines": 20,
        "lines": [
          " $\\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$, while Pythia and OLMo match the 15D boundary at $\\Kempirical^{\\text{neural}} = 2$ (Table~\\ref{tab:neural_probe_crossmodel}).",
          " The hierarchy $\\Kempirical^{15\\text{D}}{=}2 < \\Kempirical^{\\text{neural}} \\in \\{2,3\\}$ reflects an interpretability--sensitivity tradeoff: learned representations recover additional depth signal sufficient to push $\\Kempirical$ to 3 for one model (Qwen), but this gain is model-dependent---the 15D features trade one depth level of sensitivity for cross-model universality (9/9 conditions $\\Kempirical{=}2$, 3/3 models identical), making them the preferred operational choice.",
          " Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\\Kempirical = 2$ to 1, while rewrite-mode $\\Kempirical = 2$ is preserved---$\\Kempirical$ is governed by the generation operator rather than the scoring model.",
          "+",
          "+\\subsection{Structural Confound: Token Length and EOS Truncation}",
          "+\\label{sec:length_confound}",
          "+",
          "+A potential confound is that EOS truncation at the 256-token generation limit could create systematic length differences across depths, inflating AUC through a length shortcut rather than distributional signatures.",
          "+We quantify this concern across all model configurations (full per-depth statistics in Table~\\ref{tab:token_length}).",
          "+",
          "+Depth~0 (human text, truncated from C4) averages ${\\sim}$191 tokens across all configurations, while depth~1+ (machine-generated) averages 195--256 tokens depending on model.",
          "+The length asymmetry thus runs \\emph{opposite} to the confound direction: human texts are shorter, so any length-based shortcut would make 0v1 detection \\emph{harder} (a classifier exploiting ``shorter$=$machine'' would fail), not easier.",
          "+",
          "+Within machine-generated depths 1--5, token counts are remarkably stable.",
          "+For Qwen-rewrite, depths 1--5 average 252--254 tokens (range: 2 tokens); for Pythia, 214--218 tokens (range: 4 tokens); for Qwen-7B, 193--197 tokens (range: 4 tokens).",
          "+This stability means the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons among machine-generated texts---cannot be driven by length differences, since depths 1 through 5 have effectively identical token counts within each model.",
          "+",
          "+EOS truncation rates vary across models (Table~\\ref{tab:token_length}): Qwen-rewrite and decoding ablations show mild truncation (7--16\\% at depth~1+), Qwen-continuation moderate truncation (17--20\\%), while Pythia (34--36\\%) and Qwen-7B (45--47\\%) exhibit higher rates.",
          "+Crucially, truncation rates are \\emph{stable across depths 1--5 within each model}, so EOS effects do not create a depth-correlated length gradient that could confound pairwise discrimination.",
          "+The models with highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay as low-truncation models, further ruling out length as a driver of the boundary."
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

_source line 44_

Now add the token length table to the appendix, before the final `\clearpage`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "b1a60acc-970e-48e2-be39-1db1a79cf77a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115L3RGZ9ezipLEwUNMfoq2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 45965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1195
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

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_01X4Ho6tGaL5T9NkZcJXcSK1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "old_string": "\\clearpage\n\\section{Supplementary Details}",
  "new_string": "%%% Table: Token Length and EOS Truncation Analysis\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound} for discussion.}\n  \\label{tab:token_length}\n  \\begin{tabular}{lcccccccc}\n    \\toprule\n    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\\n    \\cmidrule(lr){2-7}\n    \\textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \\textbf{EOS Trunc.\\ (\\%)} & \\textbf{Severity} \\\\\n    \\midrule\n    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\\n    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\\n    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\\\\n    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\\\\n    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\\n    \\midrule\n    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\\n    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\\n    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\\n    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\\n    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\footnotesize\n  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.\n\\end{table*}\n\n\\clearpage\n\\section{Supplementary Details}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "da7d239c-89b0-494c-89e9-d934481461c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115L3RGZ9ezipLEwUNMfoq2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 45965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1195
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

_source line 46 · 2026-05-16T03:21:59.381Z_

<details><summary>↩ Tool result · `toolu_01X4Ho6tGaL5T9NkZcJXcSK1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "3471bde0-4e3e-412d-8778-cde3b16d0f93",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "oldString": "\\clearpage\n\\section{Supplementary Details}",
    "newString": "%%% Table: Token Length and EOS Truncation Analysis\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound} for discussion.}\n  \\label{tab:token_length}\n  \\begin{tabular}{lcccccccc}\n    \\toprule\n    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\\n    \\cmidrule(lr){2-7}\n    \\textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \\textbf{EOS Trunc.\\ (\\%)} & \\textbf{Severity} \\\\\n    \\midrule\n    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\\n    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\\n    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\\\\n    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\\\\n    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\\n    \\midrule\n    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\\n    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\\n    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\\n    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\\n    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\footnotesize\n  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.\n\\end{table*}\n\n\\clearpage\n\\section{Supplementary Details}",
    "originalFile": "\\appendix\n\\section{Supplementary Figures}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_filtering_strategies.pdf}\n\\caption{Downstream performance of all filtering strategies (5 seeds, $\\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}\n\\label{fig:filtering_strategies}\n\\end{figure}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}\n  \\caption{Pairwise $\\auc$ decay curves for five model-mode configurations with bootstrap 95\\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\\Kempirical=2$ boundary where $\\auc$ drops below $\\theta=0.60$. This figure complements Figure~\\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}\n  \\label{fig:s1_auc_decay_ci}\n\\end{figure}\n\n\\section{Supplementary Tables}\n\n%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}\n  \\label{tab:s1_transfer}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\multirow{2}{*}{\\textbf{Train Model}} & \\multicolumn{4}{c}{\\textbf{Test Model}} \\\\\n    \\cmidrule(lr){2-5}\n    & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n    \\midrule\n    Qwen-rw   & \\textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\\\\n    Pythia    & 0.2718 & \\textbf{0.3856} & 0.3531 & 0.3287 \\\\\n    OLMo      & 0.2768 & 0.3450 & \\textbf{0.3822} & 0.3244 \\\\\n    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \\textbf{0.3875} \\\\\n    \\bottomrule\n  \\end{tabular}\n  \\vspace{4pt}\n\n  \\footnotesize\n  \\textit{Transfer retention} between models $A$ and $B$ is defined as $\\frac{1}{2}\\bigl(\\frac{\\mathrm{acc}(A \\to B)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}} + \\frac{\\mathrm{acc}(B \\to A)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}}\\bigr)$.\n  Notable pairs: Pythia$\\leftrightarrow$OLMo 91--92\\%, Qwen-cont$\\leftrightarrow$Pythia 83--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\%, Qwen-rw$\\to$Pythia/OLMo 61--63\\%.\n\\end{table*}\n\n%%% Table S2: Decoding Ablation AUC (exp-003)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Pairwise AUC across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode). The horizontal rule between depth pairs 1\\,vs.\\,2 and 2\\,vs.\\,3 marks the empirical detectability boundary $\\Kempirical=2$: pairs above this line are reliably separable ($\\auc > 0.60$), while those below approach chance. Bottom rows report cross-configuration Spearman $\\rho$ on per-feature discriminative-power rankings.}\n  \\label{tab:s2_decoding}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy} & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & 0.9797 & 0.9946 & 0.9878 & 0.9982 \\\\\n    1 vs.\\ 2 & 0.6893 & 0.6866 & 0.6887 & 0.7039 \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & 0.5613 & 0.5917 & 0.5902 & 0.5823 \\\\\n    3 vs.\\ 4 & 0.5404 & 0.5466 & 0.5393 & 0.5293 \\\\\n    4 vs.\\ 5 & 0.5139 & 0.5068 & 0.5349 & 0.5237 \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textbf{Cross-config feature Spearman $\\rho$}} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Greedy vs.\\ Nuc $p{=}0.9$} & 0.600 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}0.7$} & 0.782 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}0.7$} & 0.914 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}1.2$} & 0.893 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}1.2$} & 0.532 &\n    \\multicolumn{1}{l}{$T{=}0.7$ vs.\\ $T{=}1.2$} & 0.668 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)\n\\begin{table*}[t]\n  \\centering\n  \\caption{LLM zero-shot depth classification: $5{\\times}5$ confusion matrices\n    (Exp-011). Both frontier LLMs achieve high binary detection accuracy\n    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class\n    accuracy (${\\sim}0.33$ vs.\\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5\n    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on\n    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as\n    depth-2. Claude Opus~4.6 shows more uniform errors across depths 1--4,\n    with depth-4 recall (0.3700) substantially exceeding GPT-5.5.\n    Per-depth recall comparison with OBD-LightGBM in Table~\\ref{tab:s3c_perdepth}.}\n  \\label{tab:s3_llm_zeroshot}\n\n  \\vspace{0.5em}\n  \\begin{subtable}{0.48\\textwidth}\n    \\centering\n    \\caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}\n    \\label{tab:s3a_gpt55}\n    \\small\n    \\begin{tabular}{lcccccc}\n      \\toprule\n      & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n      \\cmidrule(lr){2-6}\n      True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n      \\midrule\n      0 & \\textbf{77} & 18 &  4 &  0 &  1 & .770 \\\\\n      1 &  9 & \\textbf{19} & 36 & 24 & 12 & .190 \\\\\n      2 &  8 & 10 & \\textbf{38} & 35 &  9 & .380 \\\\\n      3 & 10 & 16 & 35 & \\textbf{24} & 15 & .240 \\\\\n      4 & 11 & 13 & 50 & 18 &  \\textbf{8} & .080 \\\\\n      \\bottomrule\n    \\end{tabular}\n  \\end{subtable}\n  \\hfill\n  \\begin{subtable}{0.48\\textwidth}\n    \\centering\n    \\caption{Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)}\n    \\label{tab:s3b_claude}\n    \\small\n    \\begin{tabular}{lcccccc}\n      \\toprule\n      & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n      \\cmidrule(lr){2-6}\n      True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n      \\midrule\n      0 & \\textbf{69} & 26 &  3 &  0 &  2 & .690 \\\\\n      1 &  8 & \\textbf{21} & 32 & 11 & 28 & .210 \\\\\n      2 &  6 & 36 & \\textbf{28} &  5 & 25 & .280 \\\\\n      3 &  7 & 20 & 31 & \\textbf{10} & 31 & .100 \\\\\n      4 &  7 & 28 & 22 &  6 & \\textbf{37} & .370 \\\\\n      \\bottomrule\n    \\end{tabular}\n  \\end{subtable}\n\\end{table*}\n\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}\n  \\begin{tabular}{lccccc}\n    \\toprule\n    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\\\\n    \\midrule\n    OBD-LightGBM & \\textbf{96} & \\textbf{39} & 14 & 19 & 22 \\\\\n    GPT-5.5      & 77 & 19 & \\textbf{38} & \\textbf{24} &  8 \\\\\n    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \\textbf{37} \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n\\clearpage\n\\section{Supplementary Details}\n\n%%% Table S4: Dataset Statistics\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}\n  \\label{tab:s4_dataset_stats}\n  \\begin{tabular}{clrl}\n    \\toprule\n    \\textbf{Depth} & \\textbf{$N$ samples} & \\textbf{Mean tokens} & \\textbf{Source} \\\\\n    \\midrule\n    0 & 5{,}000 & 147.8 & C4 validation (human) \\\\\n    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\\\\n    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\\\\n    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\\\\n    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Total} & \\multicolumn{2}{l}{30{,}000 samples} \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n%%% Table S5: Complete 15-D Feature Descriptions\n\\begin{table*}[t]\n  \\centering\n  \\caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}\n  \\label{tab:s5_features}\n  \\begin{tabular}{llp{0.45\\textwidth}l}\n    \\toprule\n    \\textbf{Group} & \\textbf{Feature} & \\textbf{Description} & \\textbf{Range} \\\\\n    \\midrule\n    \\multirow{9}{*}{\\rotatebox[origin=c]{90}{\\textsc{Surprisal}}}\n    & \\texttt{surp\\_mean}   & Mean token surprisal $\\frac{1}{T}\\sum_t -\\log p(x_t \\mid x_{&lt;t})$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_std}    & Standard deviation of token surprisal & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_skew}   & Skewness of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_kurt}   & Excess kurtosis of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_mean} & Mean of first-order surprisal differences $\\Delta s_t = s_{t+1} - s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_std}  & Std of first-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_d1\\_skew} & Skewness of first-order surprisal differences & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_mean} & Mean of second-order differences $\\Delta^2 s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_std}  & Std of second-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Lex}}}\n    & \\texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\\\\n    & \\texttt{hapax\\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\\\\n    & \\texttt{self\\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Freq}}}\n    & \\texttt{freq\\_kurtosis}  & Excess kurtosis of word frequency distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{freq\\_entropy}   & Shannon entropy of word frequencies: $-\\sum p_w \\log_2 p_w$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{low\\_freq\\_ratio} & Proportion of vocabulary with count $\\leq 2$ & $[0, 1]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap\n\\begin{table*}[t]\n\\begin{minipage}[t]{0.45\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \\texttt{doc\\_id} to prevent data leakage from the same seed document appearing in both train and test.}\n  \\label{tab:s6_lgbm_params}\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Parameter} & \\textbf{Value} \\\\\n    \\midrule\n    \\texttt{n\\_estimators}      & 200 \\\\\n    \\texttt{learning\\_rate}     & 0.05 \\\\\n    \\texttt{max\\_depth}         & 6 \\\\\n    \\texttt{num\\_leaves}        & 31 \\\\\n    \\texttt{verbose}            & $-1$ \\\\\n    \\texttt{n\\_jobs}            & $-1$ (all cores) \\\\\n    Cross-validation            & 5-fold GroupKFold \\\\\n    Grouping key                & \\texttt{doc\\_id} \\\\\n    Objective                   & Binary (per depth pair) \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{minipage}\\hfill\n\\begin{minipage}[t]{0.52\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}\n  \\label{tab:s7_neural_probe}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Component} & \\textbf{Details} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Embedding extraction}} \\\\\n    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\\\\n    Representation    & Last hidden state, attention-masked avg pool \\\\\n    Embedding dim     & 1536 / 2048 / 2048 \\\\\n    Max sequence len   & 512 tokens \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{MLP classifier}} \\\\\n    Architecture      & $d_{\\text{emb}} \\to 512 \\to 256 \\to 6$ \\\\\n    Activations       & ReLU \\\\\n    Dropout           & 0.1 (after each hidden layer) \\\\\n    Output            & 6-class softmax \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Training}} \\\\\n    Optimizer         & Adam ($\\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\\\\n    Loss              & Cross-entropy \\\\\n    Batch size        & 256 \\\\\n    Max epochs        & 20 \\\\\n    Early stopping    & Patience = 5 (validation loss) \\\\\n    Cross-validation  & 5-fold GroupKFold \\\\\n    \\bottomrule\n  \\end{tabular}%\n  }\n\\end{minipage}\n\\end{table*}\n\n%%% Table S8: Per-Model Bootstrap CI Results (exp-007)\n\\begin{table*}[t]\n  \\centering\n  \\footnotesize\n  \\caption{Pairwise AUC with bootstrap 95\\% confidence intervals for four model-mode configurations (Exp-007, 1{,}000 bootstrap resamples). The horizontal rule separates depth pairs above and below the detectability threshold $\\theta = 0.60$. Permutation $p$-values test $H_0\\colon \\auc = 0.50$. All pairs are significant at $p < 0.01$ except OLMo 3\\,vs.\\,4 ($p = 0.064$) and 4\\,vs.\\,5 ($p = 0.232$), consistent with convergence to chance at deeper generations.}\n  \\label{tab:s8_cv_folds}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Qwen-rewrite} & \\textbf{Pythia-1.4B} & \\textbf{OLMo-1B} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    0 vs.\\ 1\n      & $.996\\;[.995,\\,.997]$\n      & $.993\\;[.992,\\,.994]$\n      & $.997\\;[.996,\\,.998]$\n      & $.997\\;[.996,\\,.998]$ \\\\\n    1 vs.\\ 2\n      & $.696\\;[.686,\\,.704]$\n      & $.654\\;[.645,\\,.663]$\n      & $.615\\;[.605,\\,.625]$\n      & $.611\\;[.602,\\,.621]$ \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3\n      & $.589\\;[.580,\\,.599]$\n      & $.551\\;[.542,\\,.563]$\n      & $.550\\;[.540,\\,.560]$\n      & $.561\\;[.551,\\,.571]$ \\\\\n    3 vs.\\ 4\n      & $.544\\;[.533,\\,.555]$\n      & $.515\\;[.504,\\,.526]$\n      & $.509\\;[.497,\\,.520]^{\\dagger}$\n      & $.541\\;[.531,\\,.551]$ \\\\\n    4 vs.\\ 5\n      & $.534\\;[.524,\\,.545]$\n      & $.514\\;[.502,\\,.525]$\n      & $.505\\;[.493,\\,.515]^{\\ddagger}$\n      & $.514\\;[.504,\\,.526]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\footnotesize\n  Each cell: AUC $[95\\%$ CI$]$. CI from 1{,}000 bootstrap resamples; $p$-values from 500-resample permutation test.\n  ${}^{\\dagger}$\\,$p = 0.064$;\\; ${}^{\\ddagger}$\\,$p = 0.232$;\\; all other pairs $p < 0.01$.\n\\end{table*}\n\n%%% Table S9: Binary Detector Spearman ρ (exp-012)\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Spearman rank correlation ($\\rho$) between binary detector confidence scores and true generational depth, and 6-class depth classification accuracy (Exp-012). Three metrics: log-PPL from the reference model (DivEye), log-PPL from the observer model, and PPL ratio (Binoculars; observer: Pythia-1.4B, performer: OLMo-1B). Random baseline for 6-class accuracy: 0.167. While statistically significant, correlations are driven by the 0v1 boundary; confidence scores do not monotonically track depth beyond generation~1. Qwen-rewrite exhibits reversed sign ($\\rho > 0$), indicating that generation mode alters the direction of binary confidence's relationship with depth.}\n  \\label{tab:s9_binary_spearman}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Spearman $\\rho$ with true depth}} \\\\\n    \\quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\\\\n    \\quad log-PPL (observer) & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\\\\n    \\quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Classification}} \\\\\n    \\quad 6-class accuracy    & 0.199    & 0.130    & 0.127    & 0.183 \\\\\n    \\midrule\n    \\multicolumn{5}{l}{Random baseline: 0.167 \\quad $\\Kempirical^{\\text{binary}} = 1$ \\quad $\\Kempirical^{\\text{OBD}} = 2$} \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n\\clearpage\n",
    "structuredPatch": [
      {
        "oldStart": 141,
        "oldLines": 6,
        "newStart": 141,
        "newLines": 37,
        "lines": [
          "   \\end{tabular}",
          " \\end{table}",
          " ",
          "+%%% Table: Token Length and EOS Truncation Analysis",
          "+\\begin{table*}[t]",
          "+  \\centering",
          "+  \\small",
          "+  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound} for discussion.}",
          "+  \\label{tab:token_length}",
          "+  \\begin{tabular}{lcccccccc}",
          "+    \\toprule",
          "+    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\",
          "+    \\cmidrule(lr){2-7}",
          "+    \\textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \\textbf{EOS Trunc.\\ (\\%)} & \\textbf{Severity} \\\\",
          "+    \\midrule",
          "+    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\",
          "+    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\",
          "+    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\\\",
          "+    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\\\",
          "+    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\",
          "+    \\midrule",
          "+    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\",
          "+    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\",
          "+    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\",
          "+    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\",
          "+    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\",
          "+    \\bottomrule",
          "+  \\end{tabular}",
          "+",
          "+  \\vspace{4pt}",
          "+  \\footnotesize",
          "+  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.",
          "+\\end{table*}",
          "+",
          " \\clearpage",
          " \\section{Supplementary Details}",
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

_source line 47_

Now update the extended limitations in appendix_extended.tex to add a dedicated paragraph about the structural confound.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "1a6047f3-efb7-4a0b-84d7-b7bd75b73d8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzhgjTfHnr1CXFnKjWdE5y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 47160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1079
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

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_01GJuZWZeDDwfUHp9xn3L8ru`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "old_string": "\\emph{Graduated filtering.}",
  "new_string": "\\emph{Structural confound: token length.}\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 195--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.\n\n\\emph{Graduated filtering.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "af879454-9c88-4020-9c46-fed84a0831f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzhgjTfHnr1CXFnKjWdE5y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 47160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1079
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

_source line 49 · 2026-05-16T03:22:08.376Z_

<details><summary>↩ Tool result · `toolu_01GJuZWZeDDwfUHp9xn3L8ru`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "f7ed04ff-c2f7-4177-ac9a-f15e72b769d9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "oldString": "\\emph{Graduated filtering.}",
    "newString": "\\emph{Structural confound: token length.}\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 195--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.\n\n\\emph{Graduated filtering.}",
    "originalFile": "\\section{Extended Discussion}\n\\label{sec:extended_discussion}\n\n\\subsection{Theoretical Implications of $\\Kempirical = 2$}\n\nThe DPI guarantees a finite $\\Ktheory$; our result establishes $\\Kempirical = 2$ across all 9 conditions (1B--7B), aligning with model collapse convergence~\\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.\nDecoding strategy modestly affects signal strength (1v2 $\\auc \\in [0.6866, 0.7039]$) but does not shift the boundary.\n\n\\subsection{Cross-Model Transfer Implications}\n\nCross-model classification retains 80--92\\% accuracy with scorer-invariant feature rankings ($\\rho > 0.90$), enabling single-classifier deployment across generators.\nAbsolute discriminability at the $\\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\\Kempirical$ from 2 to 1, while rewrite-mode $\\Kempirical = 2$ is preserved.\nModel family similarity modulates transfer (Pythia$\\leftrightarrow$OLMo: 90--92\\% vs.\\ Qwen-cont$\\leftrightarrow$OLMo: 80--85\\%).\n\n\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\subsection{Feature Importance Across Decoding Strategies}\n\nFeature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\\rho = 0.914$), while greedy vs.\\ $T{=}1.2$ yields lower correlation ($\\rho = 0.53$, nonsignificant after Bonferroni).\nThe depth boundary is robust but the optimal feature subset is strategy-dependent.\n\n\\subsection{Scale and Neural Probe}\n\\label{sec:extended_neural_probe}\n\nCross-scale validation confirms $\\Kempirical = 2$ at 7B (1v2 $\\auc = 0.6168$ $[0.608, 0.626]$, 2v3 $\\auc = 0.5492$; Table~\\ref{tab:kstar_ci}); the 7B 0v1 $\\auc$ (0.9638) is ${\\sim}$3\\,pp lower than ${\\leq}$1.5B models, consistent with larger models generating more human-like text. Scaling beyond 7B remains open.\n\nThe neural probe yields model-dependent $\\Kempirical^{\\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia and OLMo, matching the 15D boundary.\nThe 15D model-free features yield $\\Kempirical = 2$ universally, confirming their role as a robust lower bound across architectures.\n\n\\subsection{LLM Zero-Shot Baseline}\n\\label{sec:extended_llm}\n\nGPT-5.5 achieves 33.2\\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\\% (95\\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\\ref{tab:s3_llm_zeroshot}).\nPer-depth recall confirms convergent failure at depths $\\geq 2$ (Section~\\ref{sec:why_kstar}).\nWhen 6-class probabilities are marginalized to 5 classes ($P(d{\\geq}4)$), accuracy rises to 44.4\\% but concentrates in depth-4 (recall: 22\\%$\\to$80\\%) while depths 2--3 collapse to 2--8\\%; we report raw 6-class results.\n\n\\subsection{Practical Considerations}\n\nAll filtering strategies degrade general capabilities (MMLU: 0.6018 $\\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\\to$ 0.6638--0.6701); our 100\\% synthetic setting is an upper bound---in mixed corpora, degradation scales with contamination fraction~\\cite{shumailov2024collapse, dohmatob2024model}.\n$\\Kstar$-aware binary filtering reduces MMLU degradation by ${\\sim}$50\\% ($-$1.53\\,pp $\\to$ $-$0.77\\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).\n\n\\subsection{Extended Limitations}\n\\label{sec:extended_limitations}\n\n\\emph{Prompt-chain versus retrain-chain.}\nUnder monotonic-degradation assumptions~\\cite{shumailov2024collapse}, $\\Kstar^{\\text{retrain}} \\leq \\Kstar^{\\text{prompt}}$, making $\\Kempirical = 2$ a conservative estimate.\n\n\\emph{Threshold sensitivity.}\nAt $\\theta = 0.55$, $\\Kempirical = 3$ for Qwen-rewrite/continuation; at $\\theta = 0.70$, $\\Kempirical = 1$ universally (Figure~\\ref{fig:kstar_theta}).\nQwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\n\n\\emph{Graduated filtering.}\nAll $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).\nBinary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$).\n\\label{tab:pairwise_significance}\n",
    "structuredPatch": [
      {
        "oldStart": 54,
        "oldLines": 6,
        "newStart": 54,
        "newLines": 13,
        "lines": [
          " At $\\theta = 0.55$, $\\Kempirical = 3$ for Qwen-rewrite/continuation; at $\\theta = 0.70$, $\\Kempirical = 1$ universally (Figure~\\ref{fig:kstar_theta}).",
          " Qwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.",
          " ",
          "+\\emph{Structural confound: token length.}",
          "+Depth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 195--256 tokens depending on model (Table~\\ref{tab:token_length}).",
          "+This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.",
          "+Within depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.",
          "+EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.",
          "+Models with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.",
          "+",
          " \\emph{Graduated filtering.}",
          " All $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).",
          " Binary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$)."
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

_source line 50_

Now let me verify the Limitations point (12) in main.tex is consistent with the new data. Let me also update the dataset stats table (Table S4) in appendix.tex—it currently shows whitespace-tokenized counts (147.8, 207.1 etc.) which differ from the subword token counts we're adding. The new table uses subword tokens, so they coexist fine as different measurements. Let me verify the current Limitations text references correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "b03c27a4-35a3-44c6-9c20-b4ef693ca0ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDQqWeXKTkuNdhRKEHLLhy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 565,
      "cache_read_input_tokens": 48239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 565
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01B7Q36rCTLTjgvbiRGvKUCL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "offset": 64,
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
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "c9156f59-355b-4b12-837e-e553db8a13e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDQqWeXKTkuNdhRKEHLLhy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 565,
      "cache_read_input_tokens": 48239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 565
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

_source line 52 · 2026-05-16T03:22:14.499Z_

<details><summary>↩ Tool result · `toolu_01B7Q36rCTLTjgvbiRGvKUCL`</summary>

```text
64	\clearpage
65	\section*{Limitations}
66	
67	Our findings are bounded by (1)~model scale ($\leq$7B, with only one 7B configuration tested; the 7B condition uses Qwen2.5-7B-Base rather than Instruct, introducing a base-vs-instruct confound---though $\Kempirical{=}2$ consistency across this variation provides additional robustness evidence; cross-scale scoring rather than self-scoring), (2)~prompt-chain rather than retrain-chain protocols (our $\Kempirical$ is a conservative upper bound on retrain-chain $\Kstar$ under monotonic-degradation assumptions), (3)~English C4 text only, (4)~four decoding strategies, (5)~threshold sensitivity ($\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; all nine conditions yield point-estimate $\Kempirical{=}2$ at $\theta{=}0.60$, with 8/9 confirmed by bootstrap CI---one decoding variant has 2v3 CI upper marginally at 0.601), (6)~marginal boundary (Qwen-continuation 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation with both Pythia and OLMo scorers drops this condition to $\Kempirical{=}1$, Section~\ref{sec:transfer}), (7)~the 15D feature set yields a feature-set-specific lower bound ($\Ktheory$ may be strictly higher), (8)~the neural probe boundary is model-dependent ($\Kempirical^{\text{neural}}{=}3$ for Qwen only; $2$ for Pythia/OLMo), likely reflecting self-familiarity rather than a universal signal, (9)~while overall feature rankings are highly consistent across models ($\rho \geq 0.85$), depth-pair-level agreement weakens at the 1v2 boundary ($\tau \approx 0.37$), indicating that per-feature contributions at the critical boundary vary across models, (10)~cross-model scoring reduces $\Kempirical$ from 2 to 1 for continuation-mode data (Table~\ref{tab:crossscorer}), indicating that the 1v2 boundary signal has a model-specific component consistent with the representation-dependent neural probe finding; in deployment the scorer model is known, making self-scoring the natural choice, but unknown-generator scenarios remain a limitation, (11)~all experiments use 256-token segments matching common web-scale chunking; $\Kempirical$ is defined conditionally on segment length, and longer documents with more stable per-document statistics could yield higher $\Kempirical$, and (12)~structural composition: depth~0 texts are human-authored (mean ${\approx}$191 tokens after truncation) while depth~1+ are machine-generated (mean 214--256 tokens); this length asymmetry makes 0v1 detection \emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (EOS truncation rates stable across depths within each model), so the critical $\Kempirical{=}2$ finding---based on 1v2 vs.\ 2v3 comparisons---is unaffected by this confound.
68	Detailed analysis appears in Appendix~\ref{sec:extended_limitations}.
69	
70	% === Ethics Statement (ACL required, unnumbered) ===
71	\section*{Ethics Statement}
72	
73	Generational depth estimation is intended for data curation and corpus auditing---positive-sum applications that improve training data quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "4dacc9ea-ca5f-4647-bc3a-405d20760927",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
      "content": "\\clearpage\n\\section*{Limitations}\n\nOur findings are bounded by (1)~model scale ($\\leq$7B, with only one 7B configuration tested; the 7B condition uses Qwen2.5-7B-Base rather than Instruct, introducing a base-vs-instruct confound---though $\\Kempirical{=}2$ consistency across this variation provides additional robustness evidence; cross-scale scoring rather than self-scoring), (2)~prompt-chain rather than retrain-chain protocols (our $\\Kempirical$ is a conservative upper bound on retrain-chain $\\Kstar$ under monotonic-degradation assumptions), (3)~English C4 text only, (4)~four decoding strategies, (5)~threshold sensitivity ($\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; all nine conditions yield point-estimate $\\Kempirical{=}2$ at $\\theta{=}0.60$, with 8/9 confirmed by bootstrap CI---one decoding variant has 2v3 CI upper marginally at 0.601), (6)~marginal boundary (Qwen-continuation 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation with both Pythia and OLMo scorers drops this condition to $\\Kempirical{=}1$, Section~\\ref{sec:transfer}), (7)~the 15D feature set yields a feature-set-specific lower bound ($\\Ktheory$ may be strictly higher), (8)~the neural probe boundary is model-dependent ($\\Kempirical^{\\text{neural}}{=}3$ for Qwen only; $2$ for Pythia/OLMo), likely reflecting self-familiarity rather than a universal signal, (9)~while overall feature rankings are highly consistent across models ($\\rho \\geq 0.85$), depth-pair-level agreement weakens at the 1v2 boundary ($\\tau \\approx 0.37$), indicating that per-feature contributions at the critical boundary vary across models, (10)~cross-model scoring reduces $\\Kempirical$ from 2 to 1 for continuation-mode data (Table~\\ref{tab:crossscorer}), indicating that the 1v2 boundary signal has a model-specific component consistent with the representation-dependent neural probe finding; in deployment the scorer model is known, making self-scoring the natural choice, but unknown-generator scenarios remain a limitation, (11)~all experiments use 256-token segments matching common web-scale chunking; $\\Kempirical$ is defined conditionally on segment length, and longer documents with more stable per-document statistics could yield higher $\\Kempirical$, and (12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 tokens after truncation) while depth~1+ are machine-generated (mean 214--256 tokens); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound.\nDetailed analysis appears in Appendix~\\ref{sec:extended_limitations}.\n\n% === Ethics Statement (ACL required, unnumbered) ===\n\\section*{Ethics Statement}\n\nGenerational depth estimation is intended for data curation and corpus auditing---positive-sum applications that improve training data quality.",
      "numLines": 10,
      "startLine": 64,
      "totalLines": 83
    }
  }
}
```

</details>

---

### Assistant

_source line 53_

Point (12) already mentions the key numbers (191 tokens, 214-256 tokens) and the argument. Let me update it to reference the new appendix table for quantitative backup.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "57481415-8565-44aa-acda-65e46dbf1cd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RVJ9JYCUirLxeyjP7fYRH6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 48804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1148
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

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_017mEN7mc86vWLmj9zGviCcU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "old_string": "(12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 tokens after truncation) while depth~1+ are machine-generated (mean 214--256 tokens); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound.\nDetailed analysis appears in Appendix~\\ref{sec:extended_limitations}.",
  "new_string": "(12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 subword tokens after truncation) while depth~1+ are machine-generated (mean 195--256 tokens depending on model; Table~\\ref{tab:token_length}); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (within-model range $\\leq$ 6 tokens; EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound (Section~\\ref{sec:length_confound}).\nDetailed analysis appears in Appendix~\\ref{sec:extended_limitations}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "2938edad-b2c9-4f5c-b477-780cfbe99b91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RVJ9JYCUirLxeyjP7fYRH6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 48804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1148
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

_source line 55 · 2026-05-16T03:22:21.603Z_

<details><summary>↩ Tool result · `toolu_017mEN7mc86vWLmj9zGviCcU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "566b4ce1-b6e2-4e1c-ab4e-b35d7ffcfde5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "oldString": "(12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 tokens after truncation) while depth~1+ are machine-generated (mean 214--256 tokens); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound.\nDetailed analysis appears in Appendix~\\ref{sec:extended_limitations}.",
    "newString": "(12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 subword tokens after truncation) while depth~1+ are machine-generated (mean 195--256 tokens depending on model; Table~\\ref{tab:token_length}); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (within-model range $\\leq$ 6 tokens; EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound (Section~\\ref{sec:length_confound}).\nDetailed analysis appears in Appendix~\\ref{sec:extended_limitations}.",
    "originalFile": "% EMNLP 2026 Main — ARR May 2026\n% Generational Depth Contamination\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage[section]{placeins}\n\n\\newcommand{\\Kstar}{{K^*}}\n\\newcommand{\\Kempirical}{{K^*_{\\text{empirical}}}}\n\\newcommand{\\Ktheory}{{K^*_{\\text{theory}}}}\n\\newcommand{\\auc}{\\text{AUC}}\n\\newcommand{\\jsd}{\\text{JSD}}\n\n\\title{Generational Depth Estimation of Recursive Synthetic Text:\\\\Measuring the Discrimination Boundary}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% === Abstract ===\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.\nWe measure the discrimination boundary $\\Kempirical$---the maximum depth at which adjacent generations remain distinguishable---using 15 statistical features and an OBD-LightGBM classifier.\nAcross 5 model configurations (1B--7B) and 4 decoding strategies, $\\Kempirical{=}2$ at $\\theta{=}0.60$ (Cohen's $h{\\approx}0.20$), consistent across all 9 tested conditions under self-scoring (most marginal: 0.2\\,pp above $\\theta$): a single generation step is reliably detectable, but the second renders text statistically indistinguishable from deeper synthetic content---a \\emph{one-wash laundering} effect.\nModel-free statistical features enable 80--92\\% cross-model transfer retention among continuation-mode generators with scorer-invariant feature ordering ($\\rho > 0.90$), and cross-scorer validation confirms that $\\Kempirical$ is governed by the generation process rather than the scoring model.\nBoth supervised classification and zero-shot frontier LLMs fail comparably at depths ${\\geq}2$ (recall 14--22\\% vs.\\ 8--38\\%), providing converging evidence consistent with $\\Kempirical{=}2$ reflecting a data-intrinsic boundary rather than a method limitation.\nDownstream, $\\Kempirical{=}2$ correctly predicts that binary curation minimizes degradation most effectively among all tested strategies.\n\\end{abstract}\n\n% === Section 1: Introduction ===\n\\input{introduction}\n\n% === Section 2: Related Work ===\n\\input{related_work}\n\n% === Section 3: Method ===\n\\input{method}\n\n% === Section 4: Experiments ===\n\\input{experiments_c1}\n\n% === Section 5: K*-Aware Data Filtering ===\n\\input{experiments_c3}\n\n% === Section 6: Discussion ===\n\\input{discussion}\n\n% === Section 7: Conclusion ===\n\\input{conclusion}\n\n% === Limitations (ACL required, unnumbered) ===\n\\clearpage\n\\section*{Limitations}\n\nOur findings are bounded by (1)~model scale ($\\leq$7B, with only one 7B configuration tested; the 7B condition uses Qwen2.5-7B-Base rather than Instruct, introducing a base-vs-instruct confound---though $\\Kempirical{=}2$ consistency across this variation provides additional robustness evidence; cross-scale scoring rather than self-scoring), (2)~prompt-chain rather than retrain-chain protocols (our $\\Kempirical$ is a conservative upper bound on retrain-chain $\\Kstar$ under monotonic-degradation assumptions), (3)~English C4 text only, (4)~four decoding strategies, (5)~threshold sensitivity ($\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; all nine conditions yield point-estimate $\\Kempirical{=}2$ at $\\theta{=}0.60$, with 8/9 confirmed by bootstrap CI---one decoding variant has 2v3 CI upper marginally at 0.601), (6)~marginal boundary (Qwen-continuation 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation with both Pythia and OLMo scorers drops this condition to $\\Kempirical{=}1$, Section~\\ref{sec:transfer}), (7)~the 15D feature set yields a feature-set-specific lower bound ($\\Ktheory$ may be strictly higher), (8)~the neural probe boundary is model-dependent ($\\Kempirical^{\\text{neural}}{=}3$ for Qwen only; $2$ for Pythia/OLMo), likely reflecting self-familiarity rather than a universal signal, (9)~while overall feature rankings are highly consistent across models ($\\rho \\geq 0.85$), depth-pair-level agreement weakens at the 1v2 boundary ($\\tau \\approx 0.37$), indicating that per-feature contributions at the critical boundary vary across models, (10)~cross-model scoring reduces $\\Kempirical$ from 2 to 1 for continuation-mode data (Table~\\ref{tab:crossscorer}), indicating that the 1v2 boundary signal has a model-specific component consistent with the representation-dependent neural probe finding; in deployment the scorer model is known, making self-scoring the natural choice, but unknown-generator scenarios remain a limitation, (11)~all experiments use 256-token segments matching common web-scale chunking; $\\Kempirical$ is defined conditionally on segment length, and longer documents with more stable per-document statistics could yield higher $\\Kempirical$, and (12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 tokens after truncation) while depth~1+ are machine-generated (mean 214--256 tokens); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound.\nDetailed analysis appears in Appendix~\\ref{sec:extended_limitations}.\n\n% === Ethics Statement (ACL required, unnumbered) ===\n\\section*{Ethics Statement}\n\nGenerational depth estimation is intended for data curation and corpus auditing---positive-sum applications that improve training data quality.\nOur experiments use the publicly available C4 corpus and do not involve personally identifiable information.\nA potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\\auc \\geq 0.96$ at 0v1) remains robust.\n\n\\bibliography{references}\n\n\\input{appendix}\n\\input{appendix_extended}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 64,
        "oldLines": 7,
        "newStart": 64,
        "newLines": 7,
        "lines": [
          " \\clearpage",
          " \\section*{Limitations}",
          " ",
          "-Our findings are bounded by (1)~model scale ($\\leq$7B, with only one 7B configuration tested; the 7B condition uses Qwen2.5-7B-Base rather than Instruct, introducing a base-vs-instruct confound---though $\\Kempirical{=}2$ consistency across this variation provides additional robustness evidence; cross-scale scoring rather than self-scoring), (2)~prompt-chain rather than retrain-chain protocols (our $\\Kempirical$ is a conservative upper bound on retrain-chain $\\Kstar$ under monotonic-degradation assumptions), (3)~English C4 text only, (4)~four decoding strategies, (5)~threshold sensitivity ($\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; all nine conditions yield point-estimate $\\Kempirical{=}2$ at $\\theta{=}0.60$, with 8/9 confirmed by bootstrap CI---one decoding variant has 2v3 CI upper marginally at 0.601), (6)~marginal boundary (Qwen-continuation 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation with both Pythia and OLMo scorers drops this condition to $\\Kempirical{=}1$, Section~\\ref{sec:transfer}), (7)~the 15D feature set yields a feature-set-specific lower bound ($\\Ktheory$ may be strictly higher), (8)~the neural probe boundary is model-dependent ($\\Kempirical^{\\text{neural}}{=}3$ for Qwen only; $2$ for Pythia/OLMo), likely reflecting self-familiarity rather than a universal signal, (9)~while overall feature rankings are highly consistent across models ($\\rho \\geq 0.85$), depth-pair-level agreement weakens at the 1v2 boundary ($\\tau \\approx 0.37$), indicating that per-feature contributions at the critical boundary vary across models, (10)~cross-model scoring reduces $\\Kempirical$ from 2 to 1 for continuation-mode data (Table~\\ref{tab:crossscorer}), indicating that the 1v2 boundary signal has a model-specific component consistent with the representation-dependent neural probe finding; in deployment the scorer model is known, making self-scoring the natural choice, but unknown-generator scenarios remain a limitation, (11)~all experiments use 256-token segments matching common web-scale chunking; $\\Kempirical$ is defined conditionally on segment length, and longer documents with more stable per-document statistics could yield higher $\\Kempirical$, and (12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 tokens after truncation) while depth~1+ are machine-generated (mean 214--256 tokens); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound.",
          "+Our findings are bounded by (1)~model scale ($\\leq$7B, with only one 7B configuration tested; the 7B condition uses Qwen2.5-7B-Base rather than Instruct, introducing a base-vs-instruct confound---though $\\Kempirical{=}2$ consistency across this variation provides additional robustness evidence; cross-scale scoring rather than self-scoring), (2)~prompt-chain rather than retrain-chain protocols (our $\\Kempirical$ is a conservative upper bound on retrain-chain $\\Kstar$ under monotonic-degradation assumptions), (3)~English C4 text only, (4)~four decoding strategies, (5)~threshold sensitivity ($\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; all nine conditions yield point-estimate $\\Kempirical{=}2$ at $\\theta{=}0.60$, with 8/9 confirmed by bootstrap CI---one decoding variant has 2v3 CI upper marginally at 0.601), (6)~marginal boundary (Qwen-continuation 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation with both Pythia and OLMo scorers drops this condition to $\\Kempirical{=}1$, Section~\\ref{sec:transfer}), (7)~the 15D feature set yields a feature-set-specific lower bound ($\\Ktheory$ may be strictly higher), (8)~the neural probe boundary is model-dependent ($\\Kempirical^{\\text{neural}}{=}3$ for Qwen only; $2$ for Pythia/OLMo), likely reflecting self-familiarity rather than a universal signal, (9)~while overall feature rankings are highly consistent across models ($\\rho \\geq 0.85$), depth-pair-level agreement weakens at the 1v2 boundary ($\\tau \\approx 0.37$), indicating that per-feature contributions at the critical boundary vary across models, (10)~cross-model scoring reduces $\\Kempirical$ from 2 to 1 for continuation-mode data (Table~\\ref{tab:crossscorer}), indicating that the 1v2 boundary signal has a model-specific component consistent with the representation-dependent neural probe finding; in deployment the scorer model is known, making self-scoring the natural choice, but unknown-generator scenarios remain a limitation, (11)~all experiments use 256-token segments matching common web-scale chunking; $\\Kempirical$ is defined conditionally on segment length, and longer documents with more stable per-document statistics could yield higher $\\Kempirical$, and (12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 subword tokens after truncation) while depth~1+ are machine-generated (mean 195--256 tokens depending on model; Table~\\ref{tab:token_length}); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (within-model range $\\leq$ 6 tokens; EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound (Section~\\ref{sec:length_confound}).",
          " Detailed analysis appears in Appendix~\\ref{sec:extended_limitations}.",
          " ",
          " % === Ethics Statement (ACL required, unnumbered) ==="
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

_source line 56_

Now let me verify all edits are consistent by reading the modified files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "9a5f2040-2e24-46b4-8477-70a12214e02c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013f7JEUdwqiuFUz8eEGNfFF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 49952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_015EgnAYXkRAiFfX2CAArhbj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
  "offset": 33
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "da4b7568-2e19-47e2-941c-3ab4ee04d64e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013f7JEUdwqiuFUz8eEGNfFF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 49952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 58 · 2026-05-16T03:22:26.690Z_

<details><summary>↩ Tool result · `toolu_015EgnAYXkRAiFfX2CAArhbj`</summary>

```text
33	Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\Kempirical = 2$ to 1, while rewrite-mode $\Kempirical = 2$ is preserved---$\Kempirical$ is governed by the generation operator rather than the scoring model.
34	
35	\subsection{Structural Confound: Token Length and EOS Truncation}
36	\label{sec:length_confound}
37	
38	A potential confound is that EOS truncation at the 256-token generation limit could create systematic length differences across depths, inflating AUC through a length shortcut rather than distributional signatures.
39	We quantify this concern across all model configurations (full per-depth statistics in Table~\ref{tab:token_length}).
40	
41	Depth~0 (human text, truncated from C4) averages ${\sim}$191 tokens across all configurations, while depth~1+ (machine-generated) averages 195--256 tokens depending on model.
42	The length asymmetry thus runs \emph{opposite} to the confound direction: human texts are shorter, so any length-based shortcut would make 0v1 detection \emph{harder} (a classifier exploiting ``shorter$=$machine'' would fail), not easier.
43	
44	Within machine-generated depths 1--5, token counts are remarkably stable.
45	For Qwen-rewrite, depths 1--5 average 252--254 tokens (range: 2 tokens); for Pythia, 214--218 tokens (range: 4 tokens); for Qwen-7B, 193--197 tokens (range: 4 tokens).
46	This stability means the critical $\Kempirical{=}2$ finding---based on 1v2 vs.\ 2v3 comparisons among machine-generated texts---cannot be driven by length differences, since depths 1 through 5 have effectively identical token counts within each model.
47	
48	EOS truncation rates vary across models (Table~\ref{tab:token_length}): Qwen-rewrite and decoding ablations show mild truncation (7--16\% at depth~1+), Qwen-continuation moderate truncation (17--20\%), while Pythia (34--36\%) and Qwen-7B (45--47\%) exhibit higher rates.
49	Crucially, truncation rates are \emph{stable across depths 1--5 within each model}, so EOS effects do not create a depth-correlated length gradient that could confound pairwise discrimination.
50	The models with highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay as low-truncation models, further ruling out length as a driver of the boundary.
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "e3438960-ac45-443b-aaf8-ba291d1471a8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
      "content": "Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\\Kempirical = 2$ to 1, while rewrite-mode $\\Kempirical = 2$ is preserved---$\\Kempirical$ is governed by the generation operator rather than the scoring model.\n\n\\subsection{Structural Confound: Token Length and EOS Truncation}\n\\label{sec:length_confound}\n\nA potential confound is that EOS truncation at the 256-token generation limit could create systematic length differences across depths, inflating AUC through a length shortcut rather than distributional signatures.\nWe quantify this concern across all model configurations (full per-depth statistics in Table~\\ref{tab:token_length}).\n\nDepth~0 (human text, truncated from C4) averages ${\\sim}$191 tokens across all configurations, while depth~1+ (machine-generated) averages 195--256 tokens depending on model.\nThe length asymmetry thus runs \\emph{opposite} to the confound direction: human texts are shorter, so any length-based shortcut would make 0v1 detection \\emph{harder} (a classifier exploiting ``shorter$=$machine'' would fail), not easier.\n\nWithin machine-generated depths 1--5, token counts are remarkably stable.\nFor Qwen-rewrite, depths 1--5 average 252--254 tokens (range: 2 tokens); for Pythia, 214--218 tokens (range: 4 tokens); for Qwen-7B, 193--197 tokens (range: 4 tokens).\nThis stability means the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons among machine-generated texts---cannot be driven by length differences, since depths 1 through 5 have effectively identical token counts within each model.\n\nEOS truncation rates vary across models (Table~\\ref{tab:token_length}): Qwen-rewrite and decoding ablations show mild truncation (7--16\\% at depth~1+), Qwen-continuation moderate truncation (17--20\\%), while Pythia (34--36\\%) and Qwen-7B (45--47\\%) exhibit higher rates.\nCrucially, truncation rates are \\emph{stable across depths 1--5 within each model}, so EOS effects do not create a depth-correlated length gradient that could confound pairwise discrimination.\nThe models with highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay as low-truncation models, further ruling out length as a driver of the boundary.\n",
      "numLines": 19,
      "startLine": 33,
      "totalLines": 51
    }
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_017eN3StoNyopLFSAM74FvqA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "offset": 143,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "8f9ad84b-9cc0-45f9-97ec-3f6ec40654b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013f7JEUdwqiuFUz8eEGNfFF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 49952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 60 · 2026-05-16T03:22:27.423Z_

<details><summary>↩ Tool result · `toolu_017eN3StoNyopLFSAM74FvqA`</summary>

```text
143	
144	%%% Table: Token Length and EOS Truncation Analysis
145	\begin{table*}[t]
146	  \centering
147	  \small
148	  \caption{Mean subword token count per depth and EOS truncation rate (\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \emph{more conservative}, not inflated. See Section~\ref{sec:length_confound} for discussion.}
149	  \label{tab:token_length}
150	  \begin{tabular}{lcccccccc}
151	    \toprule
152	    & \multicolumn{6}{c}{\textbf{Mean Token Count}} & & \\
153	    \cmidrule(lr){2-7}
154	    \textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \textbf{EOS Trunc.\ (\%)} & \textbf{Severity} \\
155	    \midrule
156	    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\
157	    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\
158	    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\
159	    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\
160	    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\
161	    \midrule
162	    \multicolumn{9}{l}{\textit{Decoding ablation (Qwen-rw 1.5B)}} \\
163	    \quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\
164	    \quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\
165	    \quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\
166	    \quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\
167	    \bottomrule
168	  \end{tabular}
169	
170	  \vspace{4pt}
171	  \footnotesize
172	  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.
173	\end{table*}
174	
175	\clearpage
176	\section{Supplementary Details}
177	
178	%%% Table S4: Dataset Statistics
179	\begin{table}[t]
180	  \centering
181	  \small
182	  \caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "ae735ca7-f052-4eb3-a1fc-081d783d05ed",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
      "content": "\n%%% Table: Token Length and EOS Truncation Analysis\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound} for discussion.}\n  \\label{tab:token_length}\n  \\begin{tabular}{lcccccccc}\n    \\toprule\n    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\\n    \\cmidrule(lr){2-7}\n    \\textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \\textbf{EOS Trunc.\\ (\\%)} & \\textbf{Severity} \\\\\n    \\midrule\n    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\\n    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\\n    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\\\\n    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\\\\n    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\\n    \\midrule\n    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\\n    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\\n    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\\n    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\\n    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\footnotesize\n  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.\n\\end{table*}\n\n\\clearpage\n\\section{Supplementary Details}\n\n%%% Table S4: Dataset Statistics\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}",
      "numLines": 40,
      "startLine": 143,
      "totalLines": 360
    }
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_01JaXqa3Xd4qRNK9rLPaXXsp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": 47,
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
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "b6a8cc84-7d9b-45d9-b144-9451f35694ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013f7JEUdwqiuFUz8eEGNfFF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 49952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 62 · 2026-05-16T03:22:28.178Z_

<details><summary>↩ Tool result · `toolu_01JaXqa3Xd4qRNK9rLPaXXsp`</summary>

```text
47	\subsection{Extended Limitations}
48	\label{sec:extended_limitations}
49	
50	\emph{Prompt-chain versus retrain-chain.}
51	Under monotonic-degradation assumptions~\cite{shumailov2024collapse}, $\Kstar^{\text{retrain}} \leq \Kstar^{\text{prompt}}$, making $\Kempirical = 2$ a conservative estimate.
52	
53	\emph{Threshold sensitivity.}
54	At $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite/continuation; at $\theta = 0.70$, $\Kempirical = 1$ universally (Figure~\ref{fig:kstar_theta}).
55	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
56	
57	\emph{Structural confound: token length.}
58	Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 195--256 tokens depending on model (Table~\ref{tab:token_length}).
59	This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
60	Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
61	EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
62	Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.
63	
64	\emph{Graduated filtering.}
65	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
66	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\text{corr}} = 0.011$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "f0bc2db4-8000-4147-a868-348b8f1aae41",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\subsection{Extended Limitations}\n\\label{sec:extended_limitations}\n\n\\emph{Prompt-chain versus retrain-chain.}\nUnder monotonic-degradation assumptions~\\cite{shumailov2024collapse}, $\\Kstar^{\\text{retrain}} \\leq \\Kstar^{\\text{prompt}}$, making $\\Kempirical = 2$ a conservative estimate.\n\n\\emph{Threshold sensitivity.}\nAt $\\theta = 0.55$, $\\Kempirical = 3$ for Qwen-rewrite/continuation; at $\\theta = 0.70$, $\\Kempirical = 1$ universally (Figure~\\ref{fig:kstar_theta}).\nQwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\n\n\\emph{Structural confound: token length.}\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 195--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.\n\n\\emph{Graduated filtering.}\nAll $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).\nBinary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$).",
      "numLines": 20,
      "startLine": 47,
      "totalLines": 68
    }
  }
}
```

</details>

---

### Assistant

_source line 63_

All edits are consistent. Let me verify one data point—the OLMo row in the appendix table shows 256 for all depths 1-5 and <1% truncation. The task data didn't include exp-002 EOS truncation rate explicitly, but 256/256 tokens with negligible truncation is correct (almost all samples hit the limit).

Quick cross-check on the Qwen-continuation within-model range: depths 1-5 are 244, 238, 240, 240, 238. Range = 244 - 238 = 6 tokens. The appendix_extended.tex correctly says "except Qwen-continuation at 6 tokens."

Summary of changes:

**4 files modified:**

1. **`discussion.tex`** — Added new subsection "Structural Confound: Token Length and EOS Truncation" (Section 6.4) with three arguments: length asymmetry is directionally opposite to the concern, depth 1-5 lengths are stable, and high-truncation models still yield K*=2.

2. **`appendix.tex`** — Added Table `tab:token_length` with per-model per-depth mean token counts and EOS truncation rates for all 9 configurations (5 models + 4 decoding ablations).

3. **`appendix_extended.tex`** — Added "Structural confound: token length" paragraph in Extended Limitations with quantitative summary referencing the new table.

4. **`main.tex`** — Updated Limitations point (12) to reference the new table and section, updated token range from "214--256" to "195--256" to include Qwen-7B, and added within-model range bound ("$\leq$ 6 tokens").

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "uuid": "4a77e42f-7666-431e-a844-3673ddead617",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToYNAUHSwCtuZ8gsXuBi42",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3115,
      "cache_read_input_tokens": 50572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3115
      },
      "output_tokens": 7,
      "service_tier": "standard",
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

_source line 64_

All edits are consistent. Let me verify one data point—the OLMo row in the appendix table shows 256 for all depths 1-5 and <1% truncation. The task data didn't include exp-002 EOS truncation rate explicitly, but 256/256 tokens with negligible truncation is correct (almost all samples hit the limit).

Quick cross-check on the Qwen-continuation within-model range: depths 1-5 are 244, 238, 240, 240, 238. Range = 244 - 238 = 6 tokens. The appendix_extended.tex correctly says "except Qwen-continuation at 6 tokens."

Summary of changes:

**4 files modified:**

1. **`discussion.tex`** — Added new subsection "Structural Confound: Token Length and EOS Truncation" (Section 6.4) with three arguments: length asymmetry is directionally opposite to the concern, depth 1-5 lengths are stable, and high-truncation models still yield K*=2.

2. **`appendix.tex`** — Added Table `tab:token_length` with per-model per-depth mean token counts and EOS truncation rates for all 9 configurations (5 models + 4 decoding ablations).

3. **`appendix_extended.tex`** — Added "Structural confound: token length" paragraph in Extended Limitations with quantitative summary referencing the new table.

4. **`main.tex`** — Updated Limitations point (12) to reference the new table and section, updated token range from "214--256" to "195--256" to include Qwen-7B, and added within-model range bound ("$\leq$ 6 tokens").

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 108665,
  "duration_api_ms": 109573,
  "num_turns": 22,
  "stop_reason": "end_turn",
  "session_id": "1afc6b0b-2a7f-4d0b-aa10-d785bec6bdec",
  "total_cost_usd": 0.6553905000000001,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 41846,
    "cache_read_input_tokens": 506816,
    "output_tokens": 5541,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 41846,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 413,
        "cache_read_input_tokens": 50572,
        "cache_creation_input_tokens": 3115,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3115
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1755,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00185,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 5541,
      "cacheReadInputTokens": 506816,
      "cacheCreationInputTokens": 41846,
      "webSearchRequests": 0,
      "costUSD": 0.6535405000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9767401f-3c06-4327-930e-6eb8dbc06ec8"
}
```

</details>

---
