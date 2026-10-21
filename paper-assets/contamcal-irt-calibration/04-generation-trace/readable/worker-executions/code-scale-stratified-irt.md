# code scale stratified irt

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 123
- **Recorded user turns:** 1
- **Tool calls:** 40
- **Original source:** `logs/workers/worker_code_scale-stratified-irt_20260516T052844.log`
- **Structured JSON:** [`1450b9bae3f18cfcdf18.json`](../../sessions/14/1450b9bae3f18cfcdf18.json)

## Before a recorded user message

7 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "5dc6c02b-8c82-4668-a240-e9862316a0ea",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
  "uuid": "85780bd7-29fa-4aeb-a7f0-7a49094039c5",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the task. I need to:

1. Find existing IRT fitting code in the project
2. Add a `--stratify-by-scale` parameter for per-scale IRT fitting
3. Ensure proper output format
4. Modify existing code locally

Let me first explore the local project structure, especially the `exp006/` directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "01240af1-d574-45d7-b255-742cfcd6bd82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bk4CZppaySYWR6gX3AJxG8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13070,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13070
      },
      "output_tokens": 49,
      "service_tier": "standard",
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

先找现有 IRT fitting 代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "c9573581-7c38-4529-8a49-48051a066513",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bk4CZppaySYWR6gX3AJxG8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13070,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13070
      },
      "output_tokens": 49,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Agent · `toolu_01EGKeaHYJPMeg4LVnWfxQGo`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find IRT fitting code",
  "prompt": "Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ for IRT fitting scripts. Specifically:\n\n1. Look in exp006/ directory for any Python scripts related to IRT fitting (run_pooled_4bench_irt.py, run_irt.py, fit_irt.py, etc.)\n2. Also search the broader project for any IRT-related Python files\n3. Look for Stan model files (.stan)\n4. Look for any scripts that build response matrices or call Stan/CmdStan\n\nReport: file paths found, brief description of what each does, and which one appears to be the main IRT fitting script that would need modification.\n\nSearch breadth: very thorough"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "ce9ccffc-eb55-4250-a138-8a2d8885ca65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bk4CZppaySYWR6gX3AJxG8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13070,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13070
      },
      "output_tokens": 49,
      "service_tier": "standard",
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

_source line 7_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Find IRT fitting code",
  "task_type": "local_agent",
  "prompt": "Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ for IRT fitting scripts. Specifically:\n\n1. Look in exp006/ directory for any Python scripts related to IRT fitting (run_pooled_4bench_irt.py, run_irt.py, fit_irt.py, etc.)\n2. Also search the broader project for any IRT-related Python files\n3. Look for Stan model files (.stan)\n4. Look for any scripts that build response matrices or call Stan/CmdStan\n\nReport: file paths found, brief description of what each does, and which one appears to be the main IRT fitting script that would need modification.\n\nSearch breadth: very thorough",
  "uuid": "d8f867d5-21d0-4cbb-bcbb-4d763842e258",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

## Round 1

116 recorded events

### User

_source line 8 · 2026-05-16T05:29:00.988Z_

Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ for IRT fitting scripts. Specifically:

1. Look in exp006/ directory for any Python scripts related to IRT fitting (run_pooled_4bench_irt.py, run_irt.py, fit_irt.py, etc.)
2. Also search the broader project for any IRT-related Python files
3. Look for Stan model files (.stan)
4. Look for any scripts that build response matrices or call Stan/CmdStan

Report: file paths found, brief description of what each does, and which one appears to be the main IRT fitting script that would need modification.

Search breadth: very thorough

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "88e0161d-231c-4592-b353-139d77a275a2"
}
```

</details>

---

### System

_source line 9_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 18899,
    "tool_uses": 1,
    "duration_ms": 1388
  },
  "last_tool_name": "Bash",
  "uuid": "5ee4c382-42fe-4e77-a1ad-0d523d1b89b0",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Bash · `toolu_01SkP5jhDabkE3NbQE4MKoXG`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "eb851790-39d2-4bff-91e1-a33fbca4c26f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M72fBvwoCg1oeK3r1BrvhT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18890,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18890,
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

_source line 11 · 2026-05-16T05:29:02.577Z_

<details><summary>↩ Tool result · `toolu_01SkP5jhDabkE3NbQE4MKoXG`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_pipeline.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_dose_response.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/mpl_axes.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/axes_divider.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/anchored_artists.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/axes_size.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/tests/conftest.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/tests/test_axes_grid1.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/tests/__init__.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/axes_rgb.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/parasite_axes.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/axes_grid.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/__init__.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/inset_locator.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axisartist/axis_artist.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axisartist/axes_divider.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axisartist/floating_axes.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axisartist/tests/test_axislines.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axisartist/tests/test_grid_finder.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/lib/python3.14/site-packages/mpl_toolkits/axisartist/tests/test_floating_axes.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "8dca0891-0a09-45b3-a44f-0f56c4f01d25"
}
```

</details>

---

### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Finding **/exp006/*.py",
  "usage": {
    "total_tokens": 21129,
    "tool_uses": 2,
    "duration_ms": 3465
  },
  "last_tool_name": "Glob",
  "uuid": "d23d70c9-2100-456d-8fd6-62091d67b678",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_01H9fTexwaYcygi1WfLP4fYp`</summary>

```json
{
  "pattern": "**/exp006/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "12acc7a0-ad0d-43af-bd70-fc51eb6546ad",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Tb34coaxvewW6AXQTdcrYT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2226,
      "cache_read_input_tokens": 18890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2226,
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

_source line 14 · 2026-05-16T05:29:04.516Z_

<details><summary>↩ Tool result · `toolu_01H9fTexwaYcygi1WfLP4fYp`</summary>

```text
artifacts/exp006/run_irt_calibration.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "4e464113-1db0-49e7-818e-42ebe4364ea9"
}
```

</details>

---

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Finding **/*irt*.py",
  "usage": {
    "total_tokens": 21130,
    "tool_uses": 3,
    "duration_ms": 3905
  },
  "last_tool_name": "Glob",
  "uuid": "8c893d13-2374-447c-a11a-a00836ccf004",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Glob · `toolu_01UbPYwsmVJTgkaU9kVcH5Q4`</summary>

```json
{
  "pattern": "**/*irt*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "092683ca-63c5-449b-99dd-b566bdf49cd5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Tb34coaxvewW6AXQTdcrYT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2226,
      "cache_read_input_tokens": 18890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2226,
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

_source line 17 · 2026-05-16T05:29:04.959Z_

<details><summary>↩ Tool result · `toolu_01UbPYwsmVJTgkaU9kVcH5Q4`</summary>

```text
.venv/lib/python3.14/site-packages/pip/_internal/utils/virtualenv.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/utils/virtualenv.py
artifacts/exp006_irt_calibration/fit_irt.py
artifacts/exp006/run_irt_calibration.py
artifacts/exp006/intermediate/run_irt_stan.py
artifacts/run_stratified_irt.py
patch_irt_lr_filter.py
artifacts/exp006_irt_calibration/run_irt_stan.py
artifacts/run_pooled_4bench_irt.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "4ac43932-c86a-49d6-a456-384880cfae30"
}
```

</details>

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Finding **/*.stan",
  "usage": {
    "total_tokens": 21131,
    "tool_uses": 4,
    "duration_ms": 4071
  },
  "last_tool_name": "Glob",
  "uuid": "a244976f-ce73-4920-aa07-4ffc00bfe463",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Glob · `toolu_01WATQFvmMKac7ZtGD8xDG3z`</summary>

```json
{
  "pattern": "**/*.stan",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "4a50d085-fc22-41a4-a800-7dea51777e41",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Tb34coaxvewW6AXQTdcrYT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2226,
      "cache_read_input_tokens": 18890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2226,
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

_source line 20 · 2026-05-16T05:29:05.121Z_

<details><summary>↩ Tool result · `toolu_01WATQFvmMKac7ZtGD8xDG3z`</summary>

```text
artifacts/mvp_simulation/contam_irt_4pl.stan
artifacts/mvp_simulation/contam_irt_2pl.stan
artifacts/simulation_sweep/contam_irt_4pl_sweep.stan
artifacts/exp006_irt_calibration/contam_irt_2pl.stan
artifacts/exp006_irt_calibration/contam_irt_4pl_me_analytic.stan
artifacts/exp006_irt_calibration/contam_irt_4pl_me.stan
artifacts/exp006_irt_calibration/contam_irt_4pl_simple.stan
artifacts/exp006_baselines/stan_models/vanilla_4pl.stan
artifacts/exp006_baselines/stan_models/contam_irt_2pl_gamma.stan
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "ed4f9c65-c3e8-4f5f-adbd-3f1f12910544"
}
```

</details>

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 21892,
    "tool_uses": 5,
    "duration_ms": 5697
  },
  "last_tool_name": "Bash",
  "uuid": "f21b43a6-464d-4c4f-b485-a577ab5cff64",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01GwrP7n1xAahVSyhRwmY45F`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "3fb81e6d-b1e8-4649-8630-2bc7caef4ce7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UTEstgHPUJ7Yv2Y1WLW78k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 21116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 750,
        "ephemeral_1h_input_tokens": 0
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

_source line 23 · 2026-05-16T05:29:06.752Z_

<details><summary>↩ Tool result · `toolu_01GwrP7n1xAahVSyhRwmY45F`</summary>

```text
total 44
drwxr-xr-x  5 ubuntu ubuntu  4096 May 14 23:13 .
drwxr-xr-x 31 ubuntu ubuntu  4096 May 16 05:14 ..
drwxr-xr-x  2 ubuntu ubuntu  4096 May 14 23:13 data
drwxr-xr-x  2 ubuntu ubuntu  4096 May 14 05:03 intermediate
drwxr-xr-x  2 ubuntu ubuntu  4096 May 15 10:43 report
-rw-r--r--  1 ubuntu ubuntu 20750 May 14 00:40 run_irt_calibration.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "ad41df43-a0cf-46e1-8e6b-fa63c342c442"
}
```

</details>

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 21897,
    "tool_uses": 6,
    "duration_ms": 5888
  },
  "last_tool_name": "Bash",
  "uuid": "74c40132-ee89-4e53-a817-0e38e6e9395d",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01XhVsE9z8Zyjj6GoQaXNy6T`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "e5953c5e-115b-4127-92b2-0ed425aaf299",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UTEstgHPUJ7Yv2Y1WLW78k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 21116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 750,
        "ephemeral_1h_input_tokens": 0
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

_source line 26 · 2026-05-16T05:29:06.946Z_

<details><summary>↩ Tool result · `toolu_01XhVsE9z8Zyjj6GoQaXNy6T`</summary>

```text
total 9080
drwxr-xr-x  2 ubuntu ubuntu    4096 May 16 04:47 .
drwxr-xr-x 31 ubuntu ubuntu    4096 May 16 05:14 ..
-rw-r--r--  1 ubuntu ubuntu   12538 May 13 18:49 compute_baselines.py
-rw-r--r--  1 ubuntu ubuntu    1241 May 13 17:41 contam_irt_2pl.stan
-rwxr-xr-x  1 ubuntu ubuntu 3125232 May 13 20:49 contam_irt_4pl_me
-rw-r--r--  1 ubuntu ubuntu    1935 May 13 20:46 contam_irt_4pl_me.stan
-rwxr-xr-x  1 ubuntu ubuntu 3026960 May 14 00:18 contam_irt_4pl_me_analytic
-rw-r--r--  1 ubuntu ubuntu    2369 May 13 18:49 contam_irt_4pl_me_analytic.stan
-rwxr-xr-x  1 ubuntu ubuntu 3045224 May 13 20:50 contam_irt_4pl_simple
-rw-r--r--  1 ubuntu ubuntu    1676 May 13 20:46 contam_irt_4pl_simple.stan
-rw-r--r--  1 ubuntu ubuntu    8887 May 13 17:54 evaluate_calibration.py
-rw-r--r--  1 ubuntu ubuntu   12079 May 13 18:49 fit_irt.py
-rwxr-xr-x  1 ubuntu ubuntu    3972 May 13 17:55 run_exp006.sh
-rw-r--r--  1 ubuntu ubuntu   20780 May 16 04:47 run_irt_stan.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "d4eef9bb-2267-4579-b9ea-53e4295b0341"
}
```

</details>

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Reading artifacts/exp006/run_irt_calibration.py",
  "usage": {
    "total_tokens": 21902,
    "tool_uses": 7,
    "duration_ms": 6222
  },
  "last_tool_name": "Read",
  "uuid": "fa4909cf-1bba-41d9-8a4a-93feb890378b",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01EA3FdJwPobTu2Q7XsiNukG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "2942d06d-1a48-4ca9-abaa-70bc3db83cc7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UTEstgHPUJ7Yv2Y1WLW78k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 21116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 750,
        "ephemeral_1h_input_tokens": 0
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

_source line 29 · 2026-05-16T05:29:07.229Z_

<details><summary>↩ Tool result · `toolu_01EA3FdJwPobTu2Q7XsiNukG`</summary>

```text
1	"""
2	IRT parameter estimation for contamination-aware calibration.
3	
4	Fits two models to item-level correctness data from benchmark evaluations:
5	  1) Standard 2PL IRT (baseline)
6	  2) 4PL+γ contamination-aware IRT
7	
8	Input:
9	  --eval-dir      Directory containing per-model eval subdirectories
10	                  (each with eval_results.json / correctness_matrix.json)
11	  --exposure-file (optional) JSON mapping benchmark -> [τ_i, ...] exposure scores
12	  --benchmarks    Which benchmarks to analyze (default: all found)
13	  --output-dir    Where to write results JSON
14	
15	Output (per benchmark):
16	  irt_results.json with θ, γ, item params, calibrated scores, CIs
17	
18	Dependencies: torch, numpy, scipy
19	"""
20	
21	import argparse
22	import json
23	import logging
24	import math
25	import os
26	import re
27	import sys
28	from pathlib import Path
29	
30	import numpy as np
31	import torch
32	import torch.nn as nn
33	from scipy import stats
34	
35	logger = logging.getLogger(__name__)
36	
37	# ── Data Loading ──
38	
39	DOSAGE_PATTERN = re.compile(r"_d(\d+)_s(\d+)(_para)?$")
40	
41	
42	def parse_model_dir_name(dirname: str) -> dict | None:
43	    """Extract model name, dosage, seed from directory like qwen2.5-0.5b_d025_s123."""
44	    m = DOSAGE_PATTERN.search(dirname)
45	    if not m:
46	        return None
47	    dosage = int(m.group(1))
48	    seed = int(m.group(2))
49	    is_para = m.group(3) is not None
50	    model_name = dirname[: m.start()]
51	    return {
52	        "dirname": dirname,
53	        "model_name": model_name,
54	        "dosage": dosage,
55	        "seed": seed,
56	        "is_para": is_para,
57	    }
58	
59	
60	def load_eval_results(eval_dir: str, benchmarks: list[str] | None = None,
61	                      skip_para: bool = True) -> dict:
62	    eval_path = Path(eval_dir)
63	    model_dirs = sorted([
64	        d for d in eval_path.iterdir()
65	        if d.is_dir() and (d / "eval_results.json").exists()
66	    ])
67	
68	    models = []
69	    for d in model_dirs:
70	        info = parse_model_dir_name(d.name)
71	        if info is None:
72	            logger.warning("Skipping unrecognized directory: %s", d.name)
73	            continue
74	        if skip_para and info["is_para"]:
75	            continue
76	        info["path"] = str(d)
77	        models.append(info)
78	
79	    if not models:
80	        raise ValueError(f"No valid eval results found in {eval_dir}")
81	
82	    logger.info("Found %d model evaluations", len(models))
83	
84	    with open(Path(models[0]["path"]) / "eval_results.json") as f:
85	        sample = json.load(f)
86	    available_benchmarks = list(sample["benchmarks"].keys())
87	
88	    if benchmarks:
89	        benchmarks = [b for b in benchmarks if b in available_benchmarks]
90	    else:
91	        benchmarks = available_benchmarks
92	
93	    logger.info("Benchmarks: %s", benchmarks)
94	
95	    result = {"models": models, "benchmarks": {}, "dosages": np.array([m["dosage"] for m in models])}
96	
97	    for bench in benchmarks:
98	        responses = []
99	        for m in models:
100	            results_file = Path(m["path"]) / "eval_results.json"
101	            with open(results_file) as f:
102	                data = json.load(f)
103	
104	            if bench not in data["benchmarks"]:
105	                logger.warning("Benchmark %s missing for %s, filling with NaN", bench, m["dirname"])
106	                responses.append(None)
107	                continue
108	
109	            per_item = data["benchmarks"][bench]["per_item"]
110	            correct = [int(item["correct"]) for item in per_item]
111	            responses.append(correct)
112	
113	        lengths = [len(r) for r in responses if r is not None]
114	        if not lengths:
115	            logger.warning("No data for benchmark %s, skipping", bench)
116	            continue
117	
118	        n_items = lengths[0]
119	        if not all(l == n_items for l in lengths):
120	            logger.warning("Inconsistent item counts for %s: %s", bench, lengths)
121	            n_items = min(lengths)
122	
123	        matrix = np.zeros((len(models), n_items), dtype=np.float32)
124	        mask = np.ones((len(models), n_items), dtype=np.float32)
125	        for j, r in enumerate(responses):
126	            if r is None:
127	                mask[j, :] = 0.0
128	            else:
129	                matrix[j, :n_items] = r[:n_items]
130	
131	        result["benchmarks"][bench] = {
132	            "responses": matrix,
133	            "mask": mask,
134	            "n_items": n_items,
135	        }
136	
137	    return result
138	
139	
140	def load_exposure_scores(exposure_file: str | None, benchmarks: dict) -> dict:
141	    if exposure_file and os.path.exists(exposure_file):
142	        with open(exposure_file) as f:
143	            raw = json.load(f)
144	        scores = {}
145	        for bench, bench_data in benchmarks.items():
146	            n_items = bench_data["n_items"]
147	            if bench in raw:
148	                s = np.array(raw[bench], dtype=np.float32)[:n_items]
149	                if len(s) < n_items:
150	                    s = np.pad(s, (0, n_items - len(s)), constant_values=0.0)
151	                scores[bench] = s
152	            else:
153	                scores[bench] = np.ones(n_items, dtype=np.float32)
154	        return scores
155	
156	    return {bench: np.ones(d["n_items"], dtype=np.float32) for bench, d in benchmarks.items()}
157	
158	
159	# ── IRT Models (PyTorch) ──
160	
161	class IRT2PL(nn.Module):
162	    """Standard 2-parameter logistic IRT model."""
163	
164	    def __init__(self, n_persons: int, n_items: int):
165	        super().__init__()
166	        self.theta = nn.Parameter(torch.zeros(n_persons))
167	        self.a_raw = nn.Parameter(torch.zeros(n_items))
168	        self.b = nn.Parameter(torch.zeros(n_items))
169	
170	    @property
171	    def a(self):
172	        return torch.exp(self.a_raw).clamp(min=0.1, max=5.0)
173	
174	    def forward(self):
175	        theta = self.theta.unsqueeze(1)
176	        a = self.a.unsqueeze(0)
177	        b = self.b.unsqueeze(0)
178	        logit = a * (theta - b)
179	        return torch.sigmoid(logit).clamp(1e-6, 1.0 - 1e-6)
180	
181	
182	class IRT4PLGamma(nn.Module):
183	    """
184	    4PL + γ contamination-aware IRT model.
185	
186	    P(Y_ji = 1) = c_i + (d_i - c_i) * σ(a_i * (θ_j - b_i + γ_j * τ_i))
187	
188	    where γ_j captures contamination advantage proportional to item exposure τ_i.
189	    """
190	
191	    def __init__(self, n_persons: int, n_items: int, tau: torch.Tensor,
192	                 dosages: torch.Tensor | None = None):
193	        super().__init__()
194	        self.n_persons = n_persons
195	        self.n_items = n_items
196	        self.register_buffer("tau", tau)
197	
198	        self.theta = nn.Parameter(torch.zeros(n_persons))
199	        self.gamma_raw = nn.Parameter(torch.zeros(n_persons))
200	        self.a_raw = nn.Parameter(torch.zeros(n_items))
201	        self.b = nn.Parameter(torch.zeros(n_items))
202	        self.c_raw = nn.Parameter(torch.full((n_items,), -2.0))
203	        self.d_raw = nn.Parameter(torch.full((n_items,), 2.0))
204	
205	        if dosages is not None:
206	            with torch.no_grad():
207	                normed = dosages / (dosages.max() + 1e-8)
208	                self.gamma_raw.copy_(normed * 0.5)
209	
210	    @property
211	    def a(self):
212	        return torch.exp(self.a_raw).clamp(min=0.1, max=5.0)
213	
214	    @property
215	    def c(self):
216	        return torch.sigmoid(self.c_raw).clamp(max=0.5)
217	
218	    @property
219	    def d(self):
220	        return (0.5 + 0.5 * torch.sigmoid(self.d_raw))
221	
222	    @property
223	    def gamma(self):
224	        return torch.relu(self.gamma_raw)
225	
226	    def forward(self):
227	        theta = self.theta.unsqueeze(1)
228	        gamma = self.gamma.unsqueeze(1)
229	        tau = self.tau.unsqueeze(0)
230	        a = self.a.unsqueeze(0)
231	        b = self.b.unsqueeze(0)
232	        c = self.c.unsqueeze(0)
233	        d = self.d.unsqueeze(0)
234	
235	        ability = theta - b + gamma * tau
236	        logit = a * ability
237	        prob = c + (d - c) * torch.sigmoid(logit)
238	        return prob.clamp(1e-6, 1.0 - 1e-6)
239	
240	
241	# ── Estimation ──
242	
243	def fit_irt_model(model: nn.Module, responses: torch.Tensor, mask: torch.Tensor,
244	                  lr: float = 0.01, max_iter: int = 5000, tol: float = 1e-6,
245	                  l2_lambda: float = 0.001) -> dict:
246	    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
247	    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
248	        optimizer, patience=200, factor=0.5, min_lr=1e-5
249	    )
250	
251	    prev_loss = float("inf")
252	    best_loss = float("inf")
253	    best_state = None
254	    patience_counter = 0
255	
256	    for epoch in range(max_iter):
257	        optimizer.zero_grad()
258	        probs = model()
259	
260	        log_lik = (
261	            responses * torch.log(probs) + (1 - responses) * torch.log(1 - probs)
262	        )
263	        loss = -(log_lik * mask).sum() / mask.sum()
264	
265	        if hasattr(model, "theta"):
266	            loss = loss + l2_lambda * (model.theta ** 2).mean()
267	        if hasattr(model, "gamma_raw"):
268	            loss = loss + l2_lambda * (model.gamma_raw ** 2).mean()
269	
270	        if torch.isnan(loss):
271	            logger.warning("NaN loss at epoch %d, restoring best state", epoch)
272	            if best_state is not None:
273	                model.load_state_dict(best_state)
274	            break
275	
276	        loss.backward()
277	        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=5.0)
278	        optimizer.step()
279	
280	        loss_val = loss.item()
281	        scheduler.step(loss_val)
282	
283	        if loss_val < best_loss:
284	            best_loss = loss_val
285	            best_state = {k: v.clone() for k, v in model.state_dict().items()}
286	            patience_counter = 0
287	        else:
288	            patience_counter += 1
289	
290	        if abs(prev_loss - loss_val) < tol and epoch > 100:
291	            logger.info("Converged at epoch %d (loss=%.6f)", epoch, loss_val)
292	            break
293	
294	        if patience_counter > 500:
295	            logger.info("Early stopping at epoch %d (best_loss=%.6f)", epoch, best_loss)
296	            break
297	
298	        prev_loss = loss_val
299	
300	        if epoch % 500 == 0:
301	            logger.info("Epoch %d: loss=%.6f, lr=%.2e", epoch, loss_val,
302	                        optimizer.param_groups[0]["lr"])
303	
304	    if best_state is not None:
305	        model.load_state_dict(best_state)
306	
307	    return {"final_loss": best_loss, "epochs": epoch + 1}
308	
309	
310	def compute_standard_errors(model: nn.Module, responses: torch.Tensor,
311	                            mask: torch.Tensor) -> dict:
312	    ses = {}
313	    eps = 1e-4
314	
315	    for name, param in model.named_parameters():
316	        if name in ("theta", "gamma_raw", "b"):
317	            se = torch.zeros_like(param)
318	            original = param.data.clone()
319	
320	            for i in range(param.shape[0]):
321	                losses = []
322	                for delta in [-eps, 0, eps]:
323	                    param.data[i] = original[i] + delta
324	                    with torch.no_grad():
325	                        probs = model()
326	                        log_lik = (
327	                            responses * torch.log(probs) +
328	                            (1 - responses) * torch.log(1 - probs)
329	                        )
330	                        nll = -(log_lik * mask).sum()
331	                    losses.append(nll.item())
332	
333	                hessian_diag = (losses[2] - 2 * losses[1] + losses[0]) / (eps ** 2)
334	                se[i] = 1.0 / math.sqrt(max(hessian_diag, 1e-8))
335	                param.data[i] = original[i]
336	
337	            ses[name] = se.numpy()
338	
339	    return ses
340	
341	
342	# ── Main Pipeline ──
343	
344	def run_2pl(responses: np.ndarray, mask: np.ndarray) -> dict:
345	    J, I = responses.shape
346	    resp_t = torch.tensor(responses, dtype=torch.float32)
347	    mask_t = torch.tensor(mask, dtype=torch.float32)
348	
349	    model = IRT2PL(J, I)
350	    fit_info = fit_irt_model(model, resp_t, mask_t, lr=0.005)
351	
352	    ses = compute_standard_errors(model, resp_t, mask_t)
353	
354	    with torch.no_grad():
355	        theta = model.theta.numpy()
356	        a = model.a.numpy()
357	        b = model.b.numpy()
358	
359	    theta_se = ses.get("theta", np.full(J, np.nan))
360	    b_se = ses.get("b", np.full(I, np.nan))
361	
362	    return {
363	        "model": "2PL",
364	        "fit": fit_info,
365	        "theta": theta.tolist(),
366	        "theta_se": theta_se.tolist(),
367	        "theta_ci_95": [
368	            [float(theta[j] - 1.96 * theta_se[j]), float(theta[j] + 1.96 * theta_se[j])]
369	            for j in range(J)
370	        ],
371	        "items": {
372	            "a": a.tolist(),
373	            "b": b.tolist(),
374	            "b_se": b_se.tolist(),
375	        },
376	    }
377	
378	
379	def run_4pl_gamma(responses: np.ndarray, mask: np.ndarray,
380	                  tau: np.ndarray, dosages: np.ndarray) -> dict:
381	    J, I = responses.shape
382	    resp_t = torch.tensor(responses, dtype=torch.float32)
383	    mask_t = torch.tensor(mask, dtype=torch.float32)
384	    tau_t = torch.tensor(tau, dtype=torch.float32)
385	    dos_t = torch.tensor(dosages, dtype=torch.float32)
386	
387	    model = IRT4PLGamma(J, I, tau_t, dos_t)
388	    fit_info = fit_irt_model(model, resp_t, mask_t, lr=0.005, max_iter=8000)
389	
390	    ses = compute_standard_errors(model, resp_t, mask_t)
391	
392	    with torch.no_grad():
393	        theta = model.theta.numpy()
394	        gamma = model.gamma.numpy()
395	        a = model.a.numpy()
396	        b = model.b.numpy()
397	        c = model.c.numpy()
398	        d = model.d.numpy()
399	
400	    theta_se = ses.get("theta", np.full(J, np.nan))
401	    gamma_se = ses.get("gamma_raw", np.full(J, np.nan))
402	    b_se = ses.get("b", np.full(I, np.nan))
403	
404	    raw_accuracy = (responses * mask).sum(axis=1) / mask.sum(axis=1)
405	    calibrated_theta = theta
406	
407	    return {
408	        "model": "4PL+gamma",
409	        "fit": fit_info,
410	        "theta": theta.tolist(),
411	        "theta_se": theta_se.tolist(),
412	        "theta_ci_95": [
413	            [float(theta[j] - 1.96 * theta_se[j]), float(theta[j] + 1.96 * theta_se[j])]
414	            for j in range(J)
415	        ],
416	        "gamma": gamma.tolist(),
417	        "gamma_se": gamma_se.tolist(),
418	        "gamma_ci_95": [
419	            [float(gamma[j] - 1.96 * gamma_se[j]), float(gamma[j] + 1.96 * gamma_se[j])]
420	            for j in range(J)
421	        ],
422	        "raw_accuracy": raw_accuracy.tolist(),
423	        "calibrated_theta": calibrated_theta.tolist(),
424	        "items": {
425	            "a": a.tolist(),
426	            "b": b.tolist(),
427	            "b_se": b_se.tolist(),
428	            "c": c.tolist(),
429	            "d": d.tolist(),
430	        },
431	    }
432	
433	
434	def generate_synthetic_data(n_persons: int = 15, n_items: int = 50,
435	                            seed: int = 42) -> dict:
436	    rng = np.random.default_rng(seed)
437	
438	    dosages = np.array([0, 0, 0, 5, 5, 5, 25, 25, 25, 50, 50, 50, 100, 100, 100],
439	                       dtype=np.float32)[:n_persons]
440	    true_theta = rng.normal(0, 1, n_persons).astype(np.float32)
441	    true_gamma = (dosages / 100.0 * rng.uniform(0.5, 1.5, n_persons)).astype(np.float32)
442	    tau = rng.uniform(0.2, 1.0, n_items).astype(np.float32)
443	
444	    a = rng.uniform(0.5, 2.0, n_items).astype(np.float32)
445	    b = rng.normal(0, 1, n_items).astype(np.float32)
446	    c = rng.uniform(0.05, 0.25, n_items).astype(np.float32)
447	    d = rng.uniform(0.9, 1.0, n_items).astype(np.float32)
448	
449	    responses = np.zeros((n_persons, n_items), dtype=np.float32)
450	    for j in range(n_persons):
451	        for i in range(n_items):
452	            ability = true_theta[j] - b[i] + true_gamma[j] * tau[i]
453	            prob = c[i] + (d[i] - c[i]) / (1.0 + np.exp(-a[i] * ability))
454	            responses[j, i] = float(rng.random() < prob)
455	
456	    return {
457	        "responses": responses,
458	        "mask": np.ones_like(responses),
459	        "dosages": dosages,
460	        "tau": tau,
461	        "true_params": {
462	            "theta": true_theta.tolist(),
463	            "gamma": true_gamma.tolist(),
464	            "a": a.tolist(),
465	            "b": b.tolist(),
466	            "c": c.tolist(),
467	            "d": d.tolist(),
468	        },
469	    }
470	
471	
472	def main():
473	    parser = argparse.ArgumentParser(
474	        description="IRT parameter estimation for contamination-aware calibration",
475	        formatter_class=argparse.RawDescriptionHelpFormatter,
476	        epilog="""
477	Examples:
478	  # Run on eval results
479	  python run_irt_calibration.py --eval-dir /path/to/eval_results --output-dir ./irt_output
480	
481	  # Run with exposure scores
482	  python run_irt_calibration.py --eval-dir /path/to/eval_results \\
483	      --exposure-file /path/to/exposure_scores.json --output-dir ./irt_output
484	
485	  # Synthetic data test
486	  python run_irt_calibration.py --synthetic --output-dir ./irt_test
487	        """,
488	    )
489	    parser.add_argument("--eval-dir", type=str, default=None,
490	                        help="Directory containing per-model eval subdirectories")
491	    parser.add_argument("--exposure-file", type=str, default=None,
492	                        help="JSON with per-benchmark exposure scores τ_i")
493	    parser.add_argument("--benchmarks", type=str, nargs="+", default=None,
494	                        help="Benchmarks to analyze (default: all found)")
495	    parser.add_argument("--output-dir", type=str, required=True,
496	                        help="Output directory for IRT results")
497	    parser.add_argument("--synthetic", action="store_true",
498	                        help="Run on synthetic data for validation")
499	    parser.add_argument("--seed", type=int, default=42)
500	    parser.add_argument("--lr", type=float, default=0.01, help="Learning rate")
501	    parser.add_argument("--max-iter", type=int, default=5000, help="Max optimization iterations")
502	    args = parser.parse_args()
503	
504	    logging.basicConfig(
505	        level=logging.INFO,
506	        format="%(asctime)s [%(levelname)s] %(message)s",
507	    )
508	    torch.manual_seed(args.seed)
509	    np.random.seed(args.seed)
510	
511	    output_dir = Path(args.output_dir)
512	    output_dir.mkdir(parents=True, exist_ok=True)
513	
514	    if args.synthetic:
515	        logger.info("Running synthetic data validation")
516	        synth = generate_synthetic_data()
517	        responses = synth["responses"]
518	        mask = synth["mask"]
519	        dosages = synth["dosages"]
520	        tau = synth["tau"]
521	
522	        logger.info("Response matrix: %d persons x %d items", *responses.shape)
523	        logger.info("Mean accuracy: %.3f", responses.mean())
524	
525	        logger.info("Fitting 2PL model...")
526	        result_2pl = run_2pl(responses, mask)
527	
528	        logger.info("Fitting 4PL+gamma model...")
529	        result_4plg = run_4pl_gamma(responses, mask, tau, dosages)
530	
531	        true = synth["true_params"]
532	        theta_corr_2pl = float(np.corrcoef(true["theta"], result_2pl["theta"])[0, 1])
533	        theta_corr_4plg = float(np.corrcoef(true["theta"], result_4plg["theta"])[0, 1])
534	        gamma_corr = float(np.corrcoef(true["gamma"], result_4plg["gamma"])[0, 1])
535	
536	        recovery = {
537	            "theta_corr_2pl": theta_corr_2pl,
538	            "theta_corr_4plg": theta_corr_4plg,
539	            "gamma_corr_4plg": gamma_corr,
540	        }
541	        logger.info("Recovery -- theta corr (2PL): %.4f, theta corr (4PL+g): %.4f, gamma corr: %.4f",
542	                     theta_corr_2pl, theta_corr_4plg, gamma_corr)
543	
544	        output = {
545	            "mode": "synthetic",
546	            "n_persons": int(responses.shape[0]),
547	            "n_items": int(responses.shape[1]),
548	            "true_params": true,
549	            "results_2pl": result_2pl,
550	            "results_4plg": result_4plg,
551	            "recovery": recovery,
552	        }
553	
554	        out_file = output_dir / "synthetic_validation.json"
555	        with open(out_file, "w") as f:
556	            json.dump(output, f, indent=2)
557	        logger.info("Saved to %s", out_file)
558	        return
559	
560	    # ── Real data mode ──
561	    if not args.eval_dir:
562	        parser.error("--eval-dir is required when not using --synthetic")
563	
564	    data = load_eval_results(args.eval_dir, args.benchmarks)
565	    exposure = load_exposure_scores(args.exposure_file, data["benchmarks"])
566	    dosages = data["dosages"]
567	
568	    all_results = {
569	        "mode": "real",
570	        "eval_dir": args.eval_dir,
571	        "models": [
572	            {"dirname": m["dirname"], "model_name": m["model_name"],
573	             "dosage": m["dosage"], "seed": m["seed"]}
574	            for m in data["models"]
575	        ],
576	        "benchmarks": {},
577	    }
578	
579	    for bench, bench_data in data["benchmarks"].items():
580	        logger.info("=== Benchmark: %s (%d persons x %d items) ===",
581	                     bench, bench_data["responses"].shape[0], bench_data["n_items"])
582	
583	        responses = bench_data["responses"]
584	        mask = bench_data["mask"]
585	        tau = exposure[bench]
586	
587	        logger.info("Mean accuracy: %.3f", (responses * mask).sum() / mask.sum())
588	
589	        logger.info("Fitting 2PL...")
590	        result_2pl = run_2pl(responses, mask)
591	
592	        logger.info("Fitting 4PL+gamma...")
593	        result_4plg = run_4pl_gamma(responses, mask, tau, dosages)
594	
595	        all_results["benchmarks"][bench] = {
596	            "n_items": int(bench_data["n_items"]),
597	            "results_2pl": result_2pl,
598	            "results_4plg": result_4plg,
599	        }
600	
601	        logger.info("Per-model estimates:")
602	        for j, m in enumerate(data["models"]):
603	            logger.info(
604	                "  %s: dosage=%d, theta_2pl=%.3f, theta_4plg=%.3f, gamma=%.3f, raw_acc=%.3f",
605	                m["dirname"], m["dosage"],
606	                result_2pl["theta"][j], result_4plg["theta"][j],
607	                result_4plg["gamma"][j], result_4plg["raw_accuracy"][j],
608	            )
609	
610	    out_file = output_dir / "irt_results.json"
611	    with open(out_file, "w") as f:
612	        json.dump(all_results, f, indent=2)
613	    logger.info("Results saved to %s", out_file)
614	
615	
616	if __name__ == "__main__":
617	    main()
618	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "5d1895db-4717-448e-8d68-3a5118f2c416"
}
```

</details>

---

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Reading artifacts/exp006_irt_calibration/fit_irt.py",
  "usage": {
    "total_tokens": 31285,
    "tool_uses": 8,
    "duration_ms": 8408
  },
  "last_tool_name": "Read",
  "uuid": "5bc9fca5-73d3-4803-8fcb-7f34d0d5c3d2",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01NL532z9EWnasmxEy9RmF5C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/fit_irt.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "7957332c-b327-4ed6-b66e-8c9605913a1b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UiFrZDtp1Wu3U9VPr9Xaxy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9381,
      "cache_read_input_tokens": 21866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9381,
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

_source line 32 · 2026-05-16T05:29:09.409Z_

<details><summary>↩ Tool result · `toolu_01NL532z9EWnasmxEy9RmF5C`</summary>

```text
1	# exp-006: IRT model fitting with CmdStanPy NUTS
2	# Fits 4PL+γ (with or without measurement error) per benchmark
3	
4	import argparse
5	import json
6	import logging
7	import os
8	import sys
9	import time
10	
11	import numpy as np
12	import cmdstanpy
13	
14	logging.basicConfig(
15	    level=logging.INFO,
16	    format="%(asctime)s [%(levelname)s] %(message)s",
17	    datefmt="%H:%M:%S",
18	)
19	log = logging.getLogger(__name__)
20	
21	SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
22	STAN_MODELS = {
23	    "me": os.path.join(SCRIPT_DIR, "contam_irt_4pl_me.stan"),
24	    "me_analytic": os.path.join(SCRIPT_DIR, "contam_irt_4pl_me_analytic.stan"),
25	    "simple": os.path.join(SCRIPT_DIR, "contam_irt_4pl_simple.stan"),
26	    "2pl": os.path.join(SCRIPT_DIR, "contam_irt_2pl.stan"),
27	}
28	
29	NUTS_DEFAULTS = {
30	    "chains": 4,
31	    "iter_warmup": 1000,
32	    "iter_sampling": 2000,
33	    "adapt_delta": 0.95,
34	    "max_treedepth": 10,
35	    "seed": 42,
36	}
37	
38	
39	def load_matrix(path):
40	    ext = os.path.splitext(path)[1].lower()
41	    if ext == ".npy":
42	        return np.load(path)
43	    elif ext == ".csv":
44	        return np.loadtxt(path, delimiter=",", skiprows=1)
45	    elif ext == ".json":
46	        with open(path) as f:
47	            return np.array(json.load(f))
48	    else:
49	        raise ValueError(f"Unsupported format: {ext}")
50	
51	
52	def compute_analytical_tau_posterior(exposure, mu_tau=0.0, sigma_tau=1.0, sigma_e=0.5):
53	    """Analytical posterior of τ given observed exposure e.
54	
55	    τ prior: N(mu_tau, sigma_tau²)
56	    Observation: e ~ N(τ, sigma_e²)
57	    Posterior: τ|e ~ N(E[τ|e], Var[τ|e])
58	
59	    Returns (tau_post_mean, tau_post_var) matrices.
60	    """
61	    sigma_tau_sq = sigma_tau ** 2
62	    sigma_e_sq = sigma_e ** 2
63	    denom = sigma_tau_sq + sigma_e_sq
64	
65	    tau_post_mean = (exposure * sigma_tau_sq + mu_tau * sigma_e_sq) / denom
66	    tau_post_var = np.full_like(exposure, (sigma_tau_sq * sigma_e_sq) / denom)
67	
68	    return tau_post_mean, tau_post_var
69	
70	
71	def prepare_stan_data(response_path, exposure_path, model_type="me"):
72	    y = load_matrix(response_path)
73	    exposure = load_matrix(exposure_path)
74	    assert y.shape == exposure.shape, (
75	        f"Shape mismatch: response {y.shape} vs exposure {exposure.shape}"
76	    )
77	    N_models, N_items = y.shape
78	    y_int = y.astype(int)
79	    assert np.all((y_int == 0) | (y_int == 1)), "Response matrix must be binary"
80	
81	    data = {
82	        "N_models": int(N_models),
83	        "N_items": int(N_items),
84	        "y": y_int.tolist(),
85	    }
86	
87	    if model_type == "me_analytic":
88	        tau_post_mean, tau_post_var = compute_analytical_tau_posterior(exposure)
89	        data["tau_post_mean"] = tau_post_mean.tolist()
90	        data["tau_post_var"] = tau_post_var.tolist()
91	        log.info("Analytical ME: eliminated %d latent τ params (N=%d × J=%d)",
92	                 N_models * N_items, N_models, N_items)
93	    else:
94	        data["exposure"] = exposure.tolist()
95	
96	    return data
97	
98	
99	def fit_model(stan_file, stan_data, nuts_kwargs=None):
100	    kwargs = {**NUTS_DEFAULTS}
101	    if nuts_kwargs:
102	        kwargs.update(nuts_kwargs)
103	
104	    log.info("Compiling Stan model: %s", os.path.basename(stan_file))
105	    model = cmdstanpy.CmdStanModel(stan_file=stan_file)
106	
107	    log.info(
108	        "Fitting: %d models × %d items, %d chains × %d samples",
109	        stan_data["N_models"],
110	        stan_data["N_items"],
111	        kwargs["chains"],
112	        kwargs["iter_sampling"],
113	    )
114	    t0 = time.time()
115	    fit = model.sample(data=stan_data, show_progress=True, **kwargs)
116	    elapsed = time.time() - t0
117	    log.info("Sampling completed in %.1fs", elapsed)
118	
119	    return fit, elapsed
120	
121	
122	def check_convergence(fit):
123	    summary = fit.summary()
124	    diagnostics = {}
125	
126	    if "R_hat" in summary.columns:
127	        rhat_col = "R_hat"
128	    elif "Rhat" in summary.columns:
129	        rhat_col = "Rhat"
130	    else:
131	        rhat_col = summary.columns[-1]
132	
133	    max_rhat = float(summary[rhat_col].max())
134	    diagnostics["max_rhat"] = round(max_rhat, 4)
135	    diagnostics["rhat_ok"] = max_rhat < 1.01
136	
137	    for col in ["N_Eff", "ESS_bulk", "N_eff"]:
138	        if col in summary.columns:
139	            min_ess = float(summary[col].min())
140	            diagnostics["min_ess"] = round(min_ess, 1)
141	            diagnostics["ess_ok"] = min_ess > 400
142	            break
143	
144	    diag_text = fit.diagnose()
145	    divergent = 0
146	    for line in diag_text.split("\n"):
147	        if "divergent" in line.lower():
148	            parts = [w for w in line.split() if w.isdigit()]
149	            if parts:
150	                divergent = int(parts[0])
151	                break
152	    total_draws = fit.chains * NUTS_DEFAULTS["iter_sampling"]
153	    divergent_pct = 100.0 * divergent / total_draws
154	    diagnostics["divergent_count"] = divergent
155	    diagnostics["divergent_pct"] = round(divergent_pct, 4)
156	    diagnostics["divergent_ok"] = divergent_pct < 0.1
157	
158	    diagnostics["all_ok"] = all(
159	        diagnostics.get(k, True) for k in ["rhat_ok", "ess_ok", "divergent_ok"]
160	    )
161	
162	    return diagnostics
163	
164	
165	def _summarize_draws(draws):
166	    """Summarize MCMC draws into mean/sd/quantiles."""
167	    return {
168	        "mean": np.round(np.mean(draws, axis=0), 4).tolist(),
169	        "sd": np.round(np.std(draws, axis=0), 4).tolist(),
170	        "q025": np.round(np.percentile(draws, 2.5, axis=0), 4).tolist(),
171	        "q975": np.round(np.percentile(draws, 97.5, axis=0), 4).tolist(),
172	        "q10": np.round(np.percentile(draws, 10, axis=0), 4).tolist(),
173	        "q90": np.round(np.percentile(draws, 90, axis=0), 4).tolist(),
174	        "q25": np.round(np.percentile(draws, 25, axis=0), 4).tolist(),
175	        "q75": np.round(np.percentile(draws, 75, axis=0), 4).tolist(),
176	    }
177	
178	
179	def extract_results(fit, stan_data, model_type):
180	    results = {}
181	
182	    gamma_draws = fit.stan_variable("gamma")
183	    results["gamma"] = {
184	        "mean": round(float(np.mean(gamma_draws)), 4),
185	        "sd": round(float(np.std(gamma_draws)), 4),
186	        "q025": round(float(np.percentile(gamma_draws, 2.5)), 4),
187	        "q975": round(float(np.percentile(gamma_draws, 97.5)), 4),
188	        "q05": round(float(np.percentile(gamma_draws, 5)), 4),
189	        "q95": round(float(np.percentile(gamma_draws, 95)), 4),
190	        "q10": round(float(np.percentile(gamma_draws, 10)), 4),
191	        "q90": round(float(np.percentile(gamma_draws, 90)), 4),
192	        "q25": round(float(np.percentile(gamma_draws, 25)), 4),
193	        "q75": round(float(np.percentile(gamma_draws, 75)), 4),
194	    }
195	
196	    theta_draws = fit.stan_variable("theta")  # (n_draws, N_models)
197	    theta_mean = np.mean(theta_draws, axis=0)
198	    theta_sd = np.std(theta_draws, axis=0)
199	    results["theta"] = {
200	        "mean": np.round(theta_mean, 4).tolist(),
201	        "sd": np.round(theta_sd, 4).tolist(),
202	    }
203	
204	    for param in ["a", "b"]:
205	        draws = fit.stan_variable(param)
206	        results[param] = {
207	            "mean": np.round(np.mean(draws, axis=0), 4).tolist(),
208	            "sd": np.round(np.std(draws, axis=0), 4).tolist(),
209	        }
210	
211	    if model_type != "2pl":
212	        for param in ["c", "d"]:
213	            draws = fit.stan_variable(param)
214	            results[param] = {
215	                "mean": np.round(np.mean(draws, axis=0), 4).tolist(),
216	                "sd": np.round(np.std(draws, axis=0), 4).tolist(),
217	            }
218	
219	    if model_type == "me":
220	        sigma_e_draws = fit.stan_variable("sigma_e")
221	        results["sigma_e"] = {
222	            "mean": round(float(np.mean(sigma_e_draws)), 4),
223	            "sd": round(float(np.std(sigma_e_draws)), 4),
224	            "q025": round(float(np.percentile(sigma_e_draws, 2.5)), 4),
225	            "q975": round(float(np.percentile(sigma_e_draws, 97.5)), 4),
226	        }
227	
228	    # ME correction operates through fitting (wider gamma posteriors from E[τ|e]),
229	    # so calibrated_score already reflects ME uncertainty for me_analytic model.
230	    cal_draws = fit.stan_variable("calibrated_score")  # (n_draws, N_models)
231	    cal_mean = np.mean(cal_draws, axis=0)
232	    cal_sd = np.std(cal_draws, axis=0)
233	    cal_q025 = np.percentile(cal_draws, 2.5, axis=0)
234	    cal_q975 = np.percentile(cal_draws, 97.5, axis=0)
235	    cal_q10 = np.percentile(cal_draws, 10, axis=0)
236	    cal_q90 = np.percentile(cal_draws, 90, axis=0)
237	    cal_q25 = np.percentile(cal_draws, 25, axis=0)
238	    cal_q75 = np.percentile(cal_draws, 75, axis=0)
239	
240	    results["calibrated_scores"] = {
241	        "mean": np.round(cal_mean, 4).tolist(),
242	        "sd": np.round(cal_sd, 4).tolist(),
243	        "q025": np.round(cal_q025, 4).tolist(),
244	        "q975": np.round(cal_q975, 4).tolist(),
245	        "q10": np.round(cal_q10, 4).tolist(),
246	        "q90": np.round(cal_q90, 4).tolist(),
247	        "q25": np.round(cal_q25, 4).tolist(),
248	        "q75": np.round(cal_q75, 4).tolist(),
249	    }
250	
251	    return results
252	
253	
254	def main():
255	    parser = argparse.ArgumentParser(description="Fit contamination-augmented IRT model")
256	    parser.add_argument("--response-matrix", required=True, help="Path to binary response matrix (N_models × N_items)")
257	    parser.add_argument("--exposure-matrix", required=True, help="Path to exposure score matrix (N_models × N_items)")
258	    parser.add_argument("--benchmark", required=True, help="Benchmark name (for output labeling)")
259	    parser.add_argument("--output-dir", required=True, help="Output directory")
260	    parser.add_argument("--model-type", choices=["me", "me_analytic", "simple", "2pl"], default="me_analytic",
261	                        help="Stan model variant. me_analytic recommended for large benchmarks (no latent τ).")
262	    parser.add_argument("--adapt-delta", type=float, default=0.95)
263	    parser.add_argument("--max-treedepth", type=int, default=10)
264	    parser.add_argument("--chains", type=int, default=4)
265	    parser.add_argument("--warmup", type=int, default=1000)
266	    parser.add_argument("--samples", type=int, default=2000)
267	    parser.add_argument("--seed", type=int, default=42)
268	    args = parser.parse_args()
269	
270	    os.makedirs(args.output_dir, exist_ok=True)
271	
272	    log.info("Benchmark: %s | Model: %s", args.benchmark, args.model_type)
273	
274	    stan_file = STAN_MODELS[args.model_type]
275	    stan_data = prepare_stan_data(args.response_matrix, args.exposure_matrix, args.model_type)
276	    log.info("Data: %d models × %d items", stan_data["N_models"], stan_data["N_items"])
277	
278	    nuts_kwargs = {
279	        "chains": args.chains,
280	        "iter_warmup": args.warmup,
281	        "iter_sampling": args.samples,
282	        "adapt_delta": args.adapt_delta,
283	        "max_treedepth": args.max_treedepth,
284	        "seed": args.seed,
285	    }
286	
287	    fit, elapsed = fit_model(stan_file, stan_data, nuts_kwargs)
288	    diagnostics = check_convergence(fit)
289	    log.info(
290	        "Convergence: Rhat_max=%.4f, ESS_min=%.0f, divergent=%.2f%% → %s",
291	        diagnostics["max_rhat"],
292	        diagnostics.get("min_ess", float("nan")),
293	        diagnostics["divergent_pct"],
294	        "OK" if diagnostics["all_ok"] else "WARNING",
295	    )
296	
297	    if not diagnostics["all_ok"]:
298	        log.warning("Convergence issues detected. Consider increasing adapt_delta or warmup.")
299	
300	    results = extract_results(fit, stan_data, args.model_type)
301	
302	    output = {
303	        "benchmark": args.benchmark,
304	        "model_type": args.model_type,
305	        "stan_file": os.path.basename(stan_file),
306	        "fit_time_sec": round(elapsed, 1),
307	        "nuts_config": nuts_kwargs,
308	        "diagnostics": diagnostics,
309	        "parameters": results,
310	    }
311	
312	    out_path = os.path.join(
313	        args.output_dir, f"{args.benchmark}_{args.model_type}_results.json"
314	    )
315	    with open(out_path, "w") as f:
316	        json.dump(output, f, indent=2)
317	    log.info("Results written to %s", out_path)
318	
319	    cal = results["calibrated_scores"]
320	    cal_path = os.path.join(
321	        args.output_dir, f"{args.benchmark}_{args.model_type}_calibrated.csv"
322	    )
323	    with open(cal_path, "w") as f:
324	        f.write("model_idx,cal_mean,cal_sd,cal_q025,cal_q975,cal_q10,cal_q90,cal_q25,cal_q75\n")
325	        for i in range(len(cal["mean"])):
326	            f.write(
327	                f"{i},{cal['mean'][i]},{cal['sd'][i]},"
328	                f"{cal['q025'][i]},{cal['q975'][i]},"
329	                f"{cal['q10'][i]},{cal['q90'][i]},"
330	                f"{cal['q25'][i]},{cal['q75'][i]}\n"
331	            )
332	    log.info("Calibrated scores written to %s", cal_path)
333	
334	
335	if __name__ == "__main__":
336	    main()
337	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "5428790a-2730-4f1b-8d51-04b0a237372d"
}
```

</details>

---

### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Reading artifacts/exp006_irt_calibration/run_irt_stan.py",
  "usage": {
    "total_tokens": 31286,
    "tool_uses": 9,
    "duration_ms": 8858
  },
  "last_tool_name": "Read",
  "uuid": "2cf9cbdd-b0f1-4f8f-b95a-cadfb5e8ba69",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_017rnRpe8iYX4oK811Yh8g4r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/run_irt_stan.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "a3dbd630-ff04-4bd8-8fdb-0beca379528d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UiFrZDtp1Wu3U9VPr9Xaxy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9381,
      "cache_read_input_tokens": 21866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9381,
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

_source line 35 · 2026-05-16T05:29:09.852Z_

<details><summary>↩ Tool result · `toolu_017rnRpe8iYX4oK811Yh8g4r`</summary>

```text
1	# CmdStanPy Bayesian IRT calibration pipeline (replaces PyTorch MLE version)
2	# 4PL+γ model: P(y=1) = c + (d-c) * logit^{-1}(a*(theta - b) + gamma * exposure)
3	
4	import argparse
5	import json
6	import logging
7	import os
8	import re
9	import sys
10	import time
11	from pathlib import Path
12	
13	import numpy as np
14	import cmdstanpy
15	
16	logger = logging.getLogger(__name__)
17	
18	DOSAGE_PATTERN = re.compile(r"_d(\d+)_s(\d+)(_para)?$")
19	
20	
21	def parse_model_dir_name(dirname: str) -> dict | None:
22	    m = DOSAGE_PATTERN.search(dirname)
23	    if not m:
24	        return None
25	    dosage = int(m.group(1))
26	    seed = int(m.group(2))
27	    is_para = m.group(3) is not None
28	    model_name = dirname[: m.start()]
29	    return {
30	        "dirname": dirname,
31	        "model_name": model_name,
32	        "dosage": dosage,
33	        "seed": seed,
34	        "is_para": is_para,
35	    }
36	
37	
38	def load_eval_results(eval_dir: str, benchmarks: list[str] | None = None,
39	                      skip_para: bool = True) -> dict:
40	    eval_path = Path(eval_dir)
41	    model_dirs = sorted([
42	        d for d in eval_path.iterdir()
43	        if d.is_dir() and (d / "eval_results.json").exists()
44	    ])
45	
46	    models = []
47	    for d in model_dirs:
48	        info = parse_model_dir_name(d.name)
49	        if info is None:
50	            logger.warning("Skipping unrecognized directory: %s", d.name)
51	            continue
52	        if skip_para and info["is_para"]:
53	            continue
54	        info["path"] = str(d)
55	        models.append(info)
56	
57	    if not models:
58	        raise ValueError(f"No valid eval results found in {eval_dir}")
59	
60	    logger.info("Found %d model evaluations", len(models))
61	
62	    with open(Path(models[0]["path"]) / "eval_results.json") as f:
63	        sample = json.load(f)
64	    available_benchmarks = list(sample["benchmarks"].keys())
65	
66	    if benchmarks:
67	        benchmarks = [b for b in benchmarks if b in available_benchmarks]
68	    else:
69	        benchmarks = available_benchmarks
70	
71	    logger.info("Benchmarks: %s", benchmarks)
72	
73	    result = {"models": models, "benchmarks": {}, "dosages": np.array([m["dosage"] for m in models])}
74	
75	    for bench in benchmarks:
76	        responses = []
77	        for m in models:
78	            results_file = Path(m["path"]) / "eval_results.json"
79	            with open(results_file) as f:
80	                data = json.load(f)
81	
82	            if bench not in data["benchmarks"]:
83	                logger.warning("Benchmark %s missing for %s", bench, m["dirname"])
84	                responses.append(None)
85	                continue
86	
87	            per_item = data["benchmarks"][bench]["per_item"]
88	            correct = [int(item["correct"]) for item in per_item]
89	            responses.append(correct)
90	
91	        lengths = [len(r) for r in responses if r is not None]
92	        if not lengths:
93	            continue
94	
95	        n_items = min(lengths)
96	        matrix = np.zeros((len(models), n_items), dtype=int)
97	        valid_mask = np.ones(len(models), dtype=bool)
98	        for j, r in enumerate(responses):
99	            if r is None:
100	                valid_mask[j] = False
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "b04c7b00-9c8b-4a64-b0a4-7df52aaebf1a"
}
```

</details>

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Reading artifacts/exp006/intermediate/run_irt_stan.py",
  "usage": {
    "total_tokens": 31287,
    "tool_uses": 10,
    "duration_ms": 9197
  },
  "last_tool_name": "Read",
  "uuid": "39a6fd89-632c-4ef9-8f81-836400227ecf",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01Nzw2WujoYtwCfPD6G7hjb2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006/intermediate/run_irt_stan.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "d6a6d544-9059-48e9-aaf3-161c16093b8a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UiFrZDtp1Wu3U9VPr9Xaxy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9381,
      "cache_read_input_tokens": 21866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9381,
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

_source line 38 · 2026-05-16T05:29:10.190Z_

<details><summary>↩ Tool result · `toolu_01Nzw2WujoYtwCfPD6G7hjb2`</summary>

```text
1	# CmdStanPy Bayesian IRT calibration pipeline (replaces PyTorch MLE version)
2	# 4PL+γ model: P(y=1) = c + (d-c) * logit^{-1}(a*(theta - b) + gamma * exposure)
3	
4	import argparse
5	import json
6	import logging
7	import os
8	import re
9	import sys
10	import time
11	from pathlib import Path
12	
13	import numpy as np
14	import cmdstanpy
15	
16	logger = logging.getLogger(__name__)
17	
18	DOSAGE_PATTERN = re.compile(r"_d(\d+)_s(\d+)(_para)?$")
19	
20	
21	def parse_model_dir_name(dirname: str) -> dict | None:
22	    m = DOSAGE_PATTERN.search(dirname)
23	    if not m:
24	        return None
25	    dosage = int(m.group(1))
26	    seed = int(m.group(2))
27	    is_para = m.group(3) is not None
28	    model_name = dirname[: m.start()]
29	    return {
30	        "dirname": dirname,
31	        "model_name": model_name,
32	        "dosage": dosage,
33	        "seed": seed,
34	        "is_para": is_para,
35	    }
36	
37	
38	def load_eval_results(eval_dir: str, benchmarks: list[str] | None = None,
39	                      skip_para: bool = True) -> dict:
40	    eval_path = Path(eval_dir)
41	    model_dirs = sorted([
42	        d for d in eval_path.iterdir()
43	        if d.is_dir() and (d / "eval_results.json").exists()
44	    ])
45	
46	    models = []
47	    for d in model_dirs:
48	        info = parse_model_dir_name(d.name)
49	        if info is None:
50	            logger.warning("Skipping unrecognized directory: %s", d.name)
51	            continue
52	        if skip_para and info["is_para"]:
53	            continue
54	        info["path"] = str(d)
55	        models.append(info)
56	
57	    if not models:
58	        raise ValueError(f"No valid eval results found in {eval_dir}")
59	
60	    logger.info("Found %d model evaluations", len(models))
61	
62	    with open(Path(models[0]["path"]) / "eval_results.json") as f:
63	        sample = json.load(f)
64	    available_benchmarks = list(sample["benchmarks"].keys())
65	
66	    if benchmarks:
67	        benchmarks = [b for b in benchmarks if b in available_benchmarks]
68	    else:
69	        benchmarks = available_benchmarks
70	
71	    logger.info("Benchmarks: %s", benchmarks)
72	
73	    result = {"models": models, "benchmarks": {}, "dosages": np.array([m["dosage"] for m in models])}
74	
75	    for bench in benchmarks:
76	        responses = []
77	        for m in models:
78	            results_file = Path(m["path"]) / "eval_results.json"
79	            with open(results_file) as f:
80	                data = json.load(f)
81	
82	            if bench not in data["benchmarks"]:
83	                logger.warning("Benchmark %s missing for %s", bench, m["dirname"])
84	                responses.append(None)
85	                continue
86	
87	            per_item = data["benchmarks"][bench]["per_item"]
88	            correct = [int(item["correct"]) for item in per_item]
89	            responses.append(correct)
90	
91	        lengths = [len(r) for r in responses if r is not None]
92	        if not lengths:
93	            continue
94	
95	        n_items = min(lengths)
96	        matrix = np.zeros((len(models), n_items), dtype=int)
97	        valid_mask = np.ones(len(models), dtype=bool)
98	        for j, r in enumerate(responses):
99	            if r is None:
100	                valid_mask[j] = False
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "bb13bb58-07f0-429f-b6e0-c2bd0b64cf70"
}
```

</details>

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Reading artifacts/run_pooled_4bench_irt.py",
  "usage": {
    "total_tokens": 39082,
    "tool_uses": 11,
    "duration_ms": 11776
  },
  "last_tool_name": "Read",
  "uuid": "508e8b5c-ed01-40ea-b795-4088d09e67e2",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01JYWa6khcZKPNdRBSYrjYSV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "46c906ae-051e-4630-8613-90874e4c5a41",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018j53aMXY2k1fKvjTVwbSjp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7793,
      "cache_read_input_tokens": 31247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7793,
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

_source line 41 · 2026-05-16T05:29:12.771Z_

<details><summary>↩ Tool result · `toolu_01JYWa6khcZKPNdRBSYrjYSV`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Pooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.
4	
5	Runs:
6	  1. Per-benchmark IRT fits (with per-benchmark model exclusions)
7	  2. Joint fit (shared gamma) across benchmarks using intersection models
8	
9	Exclusion rules:
10	  D044: GSM8K exclude d000 configs (format confound)
11	  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept
12	  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)
13	  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)
14	
15	Exposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.
16	"""
17	
18	import argparse
19	import json
20	import logging
21	import os
22	import sys
23	import time
24	from pathlib import Path
25	
26	import numpy as np
27	
28	sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
29	from run_irt_calibration import (
30	    load_pooled_eval_results,
31	    prepare_stan_data,
32	    fit_stan_model,
33	    check_convergence,
34	    posterior_predictive_check,
35	    extract_results,
36	    _summarize_vector,
37	    STAN_MODELS,
38	)
39	
40	log = logging.getLogger(__name__)
41	
42	BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge", "humaneval"]
43	SCALES = ["0.5B", "1.5B", "3B"]
44	MODEL_TYPE = "2pl_gamma"
45	STAN_FILE = STAN_MODELS[MODEL_TYPE]
46	
47	OUTPUT_DIR = Path("/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl")
48	EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
49	
50	
51	def apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):
52	    """Apply D044/D045/D046/D047/D018 per-benchmark exclusions."""
53	    keep = np.ones(len(models), dtype=bool)
54	    reasons = []
55	
56	    for i, m in enumerate(models):
57	        dirname = m.get("dirname", "")
58	        scale = m.get("scale", "")
59	        dosage = m.get("dosage", 0)
60	
61	        # D046/D047: base pretrained
62	        if "base_pretrained" in dirname:
63	            keep[i] = False
64	            reasons.append(f"  D046/D047: {dirname} (base pretrained)")
65	            continue
66	
67	        # D018: deprecated check (dirname contains DEPRECATED)
68	        if "DEPRECATED" in dirname:
69	            keep[i] = False
70	            reasons.append(f"  D018: {dirname} (deprecated)")
71	            continue
72	
73	        # D045: 0.5B MMLU/ARC excluded (position bias)
74	        if "0.5B" in scale and benchmark in ("mmlu", "arc_challenge"):
75	            keep[i] = False
76	            reasons.append(f"  D045: {dirname} (0.5B on {benchmark})")
77	            continue
78	
79	        # D044: GSM8K exclude d000 (format confound)
80	        if benchmark == "gsm8k" and dosage == 0:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "27d8db5b-0afc-4300-87b3-11963336de27"
}
```

</details>

---

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Reading artifacts/run_stratified_irt.py",
  "usage": {
    "total_tokens": 39083,
    "tool_uses": 12,
    "duration_ms": 12182
  },
  "last_tool_name": "Read",
  "uuid": "1c9726f9-5a84-4eef-9801-1e9f36ae4e23",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01QxwDmWdMVoC6zsnLMJZ8Li`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_stratified_irt.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "bec45aa3-4de7-4f4e-ba9f-0e2668f1c43f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018j53aMXY2k1fKvjTVwbSjp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7793,
      "cache_read_input_tokens": 31247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7793,
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

_source line 44 · 2026-05-16T05:29:13.178Z_

<details><summary>↩ Tool result · `toolu_01QxwDmWdMVoC6zsnLMJZ8Li`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Stratified IRT analysis: dose-response and model-size strata.
4	
5	Scheme A: by dosage (d000/d005/d025/d100) — checks dose-response in gamma
6	Scheme B: by model size (0.5B/1.5B/3B) — checks if gamma varies by capacity
7	
8	Same exclusion rules as pooled analysis (D044/D045/D046/D047/D018).
9	Oracle dosage as exposure (dosage/100 global normalization). 2PL+gamma model.
10	"""
11	
12	import argparse
13	import json
14	import logging
15	import os
16	import sys
17	import time
18	from pathlib import Path
19	
20	import numpy as np
21	
22	sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
23	from run_irt_calibration import (
24	    load_pooled_eval_results,
25	    prepare_stan_data,
26	    fit_stan_model,
27	    check_convergence,
28	    posterior_predictive_check,
29	    extract_results,
30	    STAN_MODELS,
31	)
32	
33	log = logging.getLogger(__name__)
34	
35	BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge", "humaneval"]
36	SCALES = ["0.5B", "1.5B", "3B"]
37	MODEL_TYPE = "2pl_gamma"
38	STAN_FILE = STAN_MODELS[MODEL_TYPE]
39	
40	EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
41	OUTPUT_DIR = Path("/root/autodl-tmp/exp006/results_stratified_irt")
42	
43	MAX_ITEMS = 2000
44	
45	DOSAGE_GROUPS = {
46	    "d000": [0],
47	    "d005": [5],
48	    "d025": [25],
49	    "d100": [100],
50	}
51	
52	SCALE_GROUPS = {
53	    "scale_0.5B": ["0.5B"],
54	    "scale_1.5B": ["1.5B"],
55	    "scale_3B": ["3B"],
56	}
57	
58	
59	def apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):
60	    keep = np.ones(len(models), dtype=bool)
61	    reasons = []
62	
63	    for i, m in enumerate(models):
64	        dirname = m.get("dirname", "")
65	        scale = m.get("scale", "")
66	        dosage = m.get("dosage", 0)
67	
68	        if "base_pretrained" in dirname:
69	            keep[i] = False
70	            reasons.append(f"  D046/D047: {dirname}")
71	            continue
72	        if "DEPRECATED" in dirname:
73	            keep[i] = False
74	            reasons.append(f"  D018: {dirname}")
75	            continue
76	        if "0.5B" in scale and benchmark in ("mmlu", "arc_challenge"):
77	            keep[i] = False
78	            reasons.append(f"  D045: {dirname}")
79	            continue
80	        if benchmark == "gsm8k" and dosage == 0:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "12f9b17e-6801-4c8d-afc4-3cda29b58e60"
}
```

</details>

---

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Reading patch_irt_lr_filter.py",
  "usage": {
    "total_tokens": 39084,
    "tool_uses": 13,
    "duration_ms": 12432
  },
  "last_tool_name": "Read",
  "uuid": "d05e58e2-afba-492a-94f9-1b1fef463d96",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01DXeLsUYTnKecdEJp7c2Z6t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/patch_irt_lr_filter.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "7ffb6c11-9790-488a-a89e-8616a53a47dc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018j53aMXY2k1fKvjTVwbSjp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7793,
      "cache_read_input_tokens": 31247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7793,
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

_source line 47 · 2026-05-16T05:29:13.427Z_

<details><summary>↩ Tool result · `toolu_01DXeLsUYTnKecdEJp7c2Z6t`</summary>

```text
1	#!/usr/bin/env python3
2	"""D076: Add lr filter to IRT scripts. Reads lr from train_config.json."""
3	import sys
4	
5	# ── Patch run_irt_calibration.py ──
6	fpath = "/root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
7	with open(fpath) as f:
8	    code = f.read()
9	
10	# 1. Add get_train_lr before load_matrix
11	old = 'def load_matrix(path):'
12	new = '''def get_train_lr(dirname, checkpoint_dir):
13	    """Read lr from checkpoint's train_config.json (D076)."""
14	    ckpt_name = re.sub(r'(_para)?(_aligned)?$', '', dirname)
15	    config_path = os.path.join(checkpoint_dir, ckpt_name, "train_config.json")
16	    try:
17	        with open(config_path) as f:
18	            return json.load(f).get("lr")
19	    except (FileNotFoundError, json.JSONDecodeError):
20	        return None
21	
22	
23	def load_matrix(path):'''
24	assert old in code, "FAIL: cannot find load_matrix"
25	code = code.replace(old, new, 1)
26	
27	# 2. Modify load_eval_results signature
28	old = ('def load_eval_results(eval_dir, benchmarks=None, skip_para=True,\n'
29	       '                      model_scale=None, seed_filter=None, aligned_only=False):')
30	new = ('def load_eval_results(eval_dir, benchmarks=None, skip_para=True,\n'
31	       '                      model_scale=None, seed_filter=None, aligned_only=False,\n'
32	       '                      lr_filter=None, checkpoint_dir=None):')
33	assert old in code, "FAIL: cannot find load_eval_results signature"
34	code = code.replace(old, new, 1)
35	
36	# 3. Add lr filter after seed_filter check
37	old = ('        if seed_filter is not None and info["seed"] != seed_filter:\n'
38	       '            log.info("Skipping dir (seed mismatch): %s", d.name)\n'
39	       '            continue\n'
40	       '        info["path"] = str(d)')
41	new = ('        if seed_filter is not None and info["seed"] != seed_filter:\n'
42	       '            log.info("Skipping dir (seed mismatch): %s", d.name)\n'
43	       '            continue\n'
44	       '        # D076: lr filter — exclude checkpoints trained with non-standard lr\n'
45	       '        if lr_filter is not None and checkpoint_dir:\n'
46	       '            lr = get_train_lr(d.name, checkpoint_dir)\n'
47	       '            if lr is None or abs(lr - lr_filter) > 1e-6:\n'
48	       '                log.info("Skipping dir (lr=%s, want %.1e): %s",\n'
49	       '                         f"{lr:.1e}" if lr is not None else "unknown",\n'
50	       '                         lr_filter, d.name)\n'
51	       '                continue\n'
52	       '        info["path"] = str(d)')
53	assert ('        if seed_filter is not None and info["seed"] != seed_filter:\n'
54	        '            log.info("Skipping dir (seed mismatch): %s", d.name)\n'
55	        '            continue\n'
56	        '        info["path"] = str(d)') in code, "FAIL: cannot find seed check block"
57	code = code.replace(
58	    '        if seed_filter is not None and info["seed"] != seed_filter:\n'
59	    '            log.info("Skipping dir (seed mismatch): %s", d.name)\n'
60	    '            continue\n'
61	    '        info["path"] = str(d)',
62	    new, 1)
63	
64	# 4. Modify load_pooled_eval_results signature
65	old = 'def load_pooled_eval_results(eval_dir, scales, benchmarks=None, **kwargs):'
66	new = ('def load_pooled_eval_results(eval_dir, scales, benchmarks=None,\n'
67	       '                              lr_filter=None, lr_filter_scales=None,\n'
68	       '                              checkpoint_dir=None, **kwargs):')
69	assert old in code, "FAIL: cannot find load_pooled_eval_results signature"
70	code = code.replace(old, new, 1)
71	
72	# 5. Modify data loading in pooled loop
73	old = '        data = load_eval_results(eval_dir, benchmarks, model_scale=scale, **kwargs)'
74	new = ('        kw = dict(kwargs)\n'
75	       '        if lr_filter is not None and checkpoint_dir:\n'
76	       '            if lr_filter_scales is None or scale in lr_filter_scales:\n'
77	       '                kw["lr_filter"] = lr_filter\n'
78	       '                kw["checkpoint_dir"] = checkpoint_dir\n'
79	       '        data = load_eval_results(eval_dir, benchmarks, model_scale=scale, **kw)')
80	assert old in code, "FAIL: cannot find pooled load line"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "18ffe3b4-1420-42c8-ad8c-addfd6d50f83"
}
```

</details>

---

### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 42863,
    "tool_uses": 14,
    "duration_ms": 15250
  },
  "last_tool_name": "Bash",
  "uuid": "1e0e9a3c-e763-4483-af44-e341f7102dd4",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01QNUL1YwC56KF9ohvDV6fW1`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration -type f -name \"*.py\" | grep -E \"(irt|fit|run)\" | grep -v \".venv\" | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "37fff09a-1be7-41c4-9d24-34b5885775be",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MapnNgBxmnn3CXpYaXSc8f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3777,
      "cache_read_input_tokens": 39040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3777,
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

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Reading artifacts/exp006_irt_calibration/contam_irt_4pl_me.stan",
  "usage": {
    "total_tokens": 42864,
    "tool_uses": 15,
    "duration_ms": 15384
  },
  "last_tool_name": "Read",
  "uuid": "73fe16a6-ca3c-4c6c-8d4c-845cc02bd6ef",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01W5fFU5hn2e2CYLWN8NGLfm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/contam_irt_4pl_me.stan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "5b40ffb3-0d65-440b-9377-4678ee1d130d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MapnNgBxmnn3CXpYaXSc8f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3777,
      "cache_read_input_tokens": 39040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3777,
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

_source line 52 · 2026-05-16T05:29:16.386Z_

<details><summary>↩ Tool result · `toolu_01QNUL1YwC56KF9ohvDV6fW1`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/compile_eval_summary.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp001_sft_injection/evaluate.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp001_sft_injection/paraphrase_gen.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp001_sft_injection/prepare_sft_data.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp001_sft_injection/train_sft.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp002_signal_pipeline/aggregate_rrf.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp002_signal_pipeline/compute_signals.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp002_signal_pipeline/signal_constat.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp002_signal_pipeline/signal_embedding.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp002_signal_pipeline/signal_minkpp.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp002_signal_pipeline/signal_selfcritique.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp003_rrf_ablation/analyze_rrf_ablation.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/diag_analytic_me.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/diag_nmodels50.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/reanalysis_gamma_attenuation.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/run_noise_propagation.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/run_noise_propagation_v3.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/stan_diagnostic.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/stan_diagnostic_v2.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006/intermediate/run_irt_stan.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006/run_irt_calibration.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_baselines/baselines/__init__.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_baselines/baselines/dcr_fuzzy.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_baselines/baselines/emperor_mitigation.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_baselines/baselines/linear_regression.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_baselines/baselines/raw_scores.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_baselines/baselines/remove_rescore.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_baselines/baselines/single_signal_2pl_gamma.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_baselines/baselines/utils.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_baselines/baselines/vanilla_4pl.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_baselines/run_all_baselines.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/compute_baselines.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/evaluate_calibration.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/fit_irt.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/run_irt_stan.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp008_v2/plot_survival.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp008_v2/run_signal_survival.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp008_v2/signal_survival_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/fisher_info_derivation/verify_fisher_info.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/run_p1_base.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/run_p1_variants.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/run_p2_confounding.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_stratified_irt.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/analyze_incremental.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/run_sweep.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp002/compute_signals.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp002/signal_minkpp.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp002/signal_selfcritique.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp002/signals/__init__.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp002/signals/s1_embedding.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp002/signals/s2_minkpp.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp002/signals/s3_constat.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp002/signals/s4_selfcritique.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp002/utils.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp008/analyze_survival.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp008/compute_signals_on_model.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp008/run_signal_survival.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_dose_response.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_pipeline.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/patch_irt_lr_filter.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "aa4dfa73-f6b6-4fd7-bc60-914801046993"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-16T05:29:16.382Z_

<details><summary>↩ Tool result · `toolu_01W5fFU5hn2e2CYLWN8NGLfm`</summary>

```text
1	// 4PL+γ IRT with measurement error on exposure
2	// P(y_ij = 1) = c_j + (d_j - c_j) * inv_logit(a_j * (theta_i - b_j) + gamma * tau_ij)
3	// exposure_ij ~ N(tau_ij, sigma_e^2) where tau_ij is latent true exposure
4	
5	data {
6	  int&lt;lower=1> N_models;
7	  int&lt;lower=1> N_items;
8	  array[N_models, N_items] int&lt;lower=0, upper=1> y;
9	  matrix[N_models, N_items] exposure;
10	}
11	
12	parameters {
13	  vector[N_models] theta;
14	  vector&lt;lower=0>[N_items] a;
15	  vector[N_items] b;
16	  vector&lt;lower=0.001, upper=0.999>[N_items] c;
17	  vector&lt;lower=0.001, upper=0.999>[N_items] d;
18	  real gamma;
19	  matrix[N_models, N_items] tau;
20	  real&lt;lower=1e-4> sigma_e;
21	}
22	
23	model {
24	  // Priors
25	  theta ~ std_normal();
26	  a ~ lognormal(0, 0.5);
27	  b ~ std_normal();
28	  c ~ beta(5, 20);
29	  d ~ beta(20, 5);
30	  gamma ~ std_normal();
31	  sigma_e ~ normal(0, 0.5);
32	
33	  // Latent exposure prior (weakly informative)
34	  to_vector(tau) ~ std_normal();
35	
36	  // Measurement error model
37	  to_vector(exposure) ~ normal(to_vector(tau), sigma_e);
38	
39	  // Likelihood
40	  for (i in 1:N_models) {
41	    for (j in 1:N_items) {
42	      real eta = a[j] * (theta[i] - b[j]) + gamma * tau[i, j];
43	      real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
44	      y[i, j] ~ bernoulli(p);
45	    }
46	  }
47	}
48	
49	generated quantities {
50	  // Calibrated scores: P(y=1 | exposure=0)
51	  array[N_models] real calibrated_score;
52	  for (i in 1:N_models) {
53	    real total = 0.0;
54	    for (j in 1:N_items) {
55	      real eta_clean = a[j] * (theta[i] - b[j]);
56	      real p_clean = c[j] + (d[j] - c[j]) * inv_logit(eta_clean);
57	      total += p_clean;
58	    }
59	    calibrated_score[i] = total / N_items;
60	  }
61	
62	  // Log-likelihood for LOO-CV
63	  vector[N_models * N_items] log_lik;
64	  {
65	    int idx = 0;
66	    for (i in 1:N_models) {
67	      for (j in 1:N_items) {
68	        idx += 1;
69	        real eta = a[j] * (theta[i] - b[j]) + gamma * tau[i, j];
70	        real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
71	        log_lik[idx] = bernoulli_lpmf(y[i, j] | p);
72	      }
73	    }
74	  }
75	}
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "60b0020c-d55d-4bf4-a3b3-510e2bebc496"
}
```

</details>

---

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Reading artifacts/exp006_irt_calibration/contam_irt_4pl_simple.stan",
  "usage": {
    "total_tokens": 47181,
    "tool_uses": 16,
    "duration_ms": 17942
  },
  "last_tool_name": "Read",
  "uuid": "a881425c-6e8d-44da-8b2e-3edcb69e7bae",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01NvnVGyQZ7P4fzJPGmiZPKd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/contam_irt_4pl_simple.stan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "ee345df7-5683-4206-a9ef-0e0327b05216",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FfLsVrxArGXwdouXnhw4w5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4309,
      "cache_read_input_tokens": 42817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4309,
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

_source line 56 · 2026-05-16T05:29:18.936Z_

<details><summary>↩ Tool result · `toolu_01NvnVGyQZ7P4fzJPGmiZPKd`</summary>

```text
1	// 4PL+γ IRT without measurement error (ablation baseline)
2	// P(y_ij = 1) = c_j + (d_j - c_j) * inv_logit(a_j * (theta_i - b_j) + gamma * exposure_ij)
3	// Uses observed exposure directly as covariate
4	
5	data {
6	  int&lt;lower=1> N_models;
7	  int&lt;lower=1> N_items;
8	  array[N_models, N_items] int&lt;lower=0, upper=1> y;
9	  matrix[N_models, N_items] exposure;
10	}
11	
12	parameters {
13	  vector[N_models] theta;
14	  vector&lt;lower=0>[N_items] a;
15	  vector[N_items] b;
16	  vector&lt;lower=0.001, upper=0.999>[N_items] c;
17	  vector&lt;lower=0.001, upper=0.999>[N_items] d;
18	  real gamma;
19	}
20	
21	model {
22	  // Priors
23	  theta ~ std_normal();
24	  a ~ lognormal(0, 0.5);
25	  b ~ std_normal();
26	  c ~ beta(5, 20);
27	  d ~ beta(20, 5);
28	  gamma ~ std_normal();
29	
30	  // Likelihood
31	  for (i in 1:N_models) {
32	    for (j in 1:N_items) {
33	      real eta = a[j] * (theta[i] - b[j]) + gamma * exposure[i, j];
34	      real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
35	      y[i, j] ~ bernoulli(p);
36	    }
37	  }
38	}
39	
40	generated quantities {
41	  // Calibrated scores: P(y=1 | exposure=0)
42	  array[N_models] real calibrated_score;
43	  for (i in 1:N_models) {
44	    real total = 0.0;
45	    for (j in 1:N_items) {
46	      real eta_clean = a[j] * (theta[i] - b[j]);
47	      real p_clean = c[j] + (d[j] - c[j]) * inv_logit(eta_clean);
48	      total += p_clean;
49	    }
50	    calibrated_score[i] = total / N_items;
51	  }
52	
53	  // Log-likelihood for LOO-CV
54	  vector[N_models * N_items] log_lik;
55	  {
56	    int idx = 0;
57	    for (i in 1:N_models) {
58	      for (j in 1:N_items) {
59	        idx += 1;
60	        real eta = a[j] * (theta[i] - b[j]) + gamma * exposure[i, j];
61	        real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
62	        log_lik[idx] = bernoulli_lpmf(y[i, j] | p);
63	      }
64	    }
65	  }
66	}
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "9c74e119-ef6a-49ca-a29e-f73d137c09af"
}
```

</details>

---

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "description": "Reading artifacts/exp006_irt_calibration/contam_irt_4pl_me_analytic.stan",
  "usage": {
    "total_tokens": 47185,
    "tool_uses": 17,
    "duration_ms": 18086
  },
  "last_tool_name": "Read",
  "uuid": "28c9dd98-e9cb-4888-8a4a-d4e4d7cac635",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_01XLa18vDgeHzZ3Kivsu5Yda`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/contam_irt_4pl_me_analytic.stan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "d75dce91-9db9-4f9b-a7df-6a2f36645653",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FfLsVrxArGXwdouXnhw4w5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4309,
      "cache_read_input_tokens": 42817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4309,
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

_source line 59 · 2026-05-16T05:29:19.080Z_

<details><summary>↩ Tool result · `toolu_01XLa18vDgeHzZ3Kivsu5Yda`</summary>

```text
1	// 4PL+γ IRT with analytical measurement error integration
2	// Eliminates latent τ parameters via conjugate normal posterior:
3	//   τ|e ~ N(E[τ|e], Var[τ|e])  where
4	//   E[τ|e] = (e * σ_τ² + μ_τ * σ_e²) / (σ_τ² + σ_e²)
5	//   Var[τ|e] = (σ_τ² * σ_e²) / (σ_τ² + σ_e²)
6	//
7	// Python preprocessing computes tau_posterior_mean and tau_posterior_var
8	// from observed exposure scores. This model uses tau_posterior_mean as the
9	// exposure covariate (same parameter count as simple model).
10	
11	data {
12	  int&lt;lower=1> N_models;
13	  int&lt;lower=1> N_items;
14	  array[N_models, N_items] int&lt;lower=0, upper=1> y;
15	  matrix[N_models, N_items] tau_post_mean;   // E[τ|e] from analytical integration
16	  matrix&lt;lower=0>[N_models, N_items] tau_post_var;  // Var[τ|e] for CI correction
17	}
18	
19	parameters {
20	  vector[N_models] theta;
21	  vector&lt;lower=0>[N_items] a;
22	  vector[N_items] b;
23	  vector&lt;lower=0, upper=1>[N_items] c;
24	  vector&lt;lower=0, upper=1>[N_items] d;
25	  real gamma;
26	}
27	
28	model {
29	  // Priors
30	  theta ~ std_normal();
31	  a ~ lognormal(0, 0.5);
32	  b ~ std_normal();
33	  c ~ beta(5, 20);
34	  d ~ beta(20, 5);
35	  gamma ~ std_normal();
36	
37	  // Likelihood using posterior mean of τ as point estimate
38	  for (i in 1:N_models) {
39	    for (j in 1:N_items) {
40	      real eta = a[j] * (theta[i] - b[j]) + gamma * tau_post_mean[i, j];
41	      real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
42	      y[i, j] ~ bernoulli(p);
43	    }
44	  }
45	}
46	
47	generated quantities {
48	  // Calibrated scores: P(y=1 | exposure=0)
49	  // ME correction operates through the fitting stage: using E[τ|e] as
50	  // exposure yields wider gamma posteriors, which automatically widen
51	  // calibrated score CIs. No tau sampling needed in generated quantities.
52	  array[N_models] real calibrated_score;
53	  for (i in 1:N_models) {
54	    real total = 0.0;
55	    for (j in 1:N_items) {
56	      real eta_clean = a[j] * (theta[i] - b[j]);
57	      real p_clean = c[j] + (d[j] - c[j]) * inv_logit(eta_clean);
58	      total += p_clean;
59	    }
60	    calibrated_score[i] = total / N_items;
61	  }
62	
63	  // Log-likelihood for LOO-CV
64	  vector[N_models * N_items] log_lik;
65	  {
66	    int idx = 0;
67	    for (i in 1:N_models) {
68	      for (j in 1:N_items) {
69	        idx += 1;
70	        real eta = a[j] * (theta[i] - b[j]) + gamma * tau_post_mean[i, j];
71	        real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
72	        log_lik[idx] = bernoulli_lpmf(y[i, j] | p);
73	      }
74	    }
75	  }
76	}
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "9072b29c-0b7d-4cf6-91f2-70b02ca98424"
}
```

</details>

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a6ed12a3e9688dcc4",
  "tool_use_id": "toolu_01EGKeaHYJPMeg4LVnWfxQGo",
  "status": "completed",
  "output_file": "",
  "summary": "Find IRT fitting code",
  "usage": {
    "total_tokens": 49485,
    "tool_uses": 17,
    "duration_ms": 37231
  },
  "uuid": "e206bae2-dec2-4f64-a4d2-d7398b2e7cc9",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d"
}
```

---

### Tool result

_source line 61 · 2026-05-16T05:29:38.223Z_

<details><summary>↩ Tool result · `toolu_01EGKeaHYJPMeg4LVnWfxQGo`</summary>

```text
Perfect! Now I have a comprehensive view. Let me create a summary report with all the findings:

## Summary Report: IRT Fitting Scripts in contamcal-irt-calibration Project

I've conducted a thorough search of the project and identified all IRT-related scripts and Stan model files. Here's what I found:

### Key IRT Fitting Scripts

#### **Main IRT Fitting Scripts (in exp006_irt_calibration/)**

1. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/run_irt_stan.py**
   - **Purpose**: Main IRT fitting script using CmdStanPy (Bayesian MCMC)
   - **Function**: Loads response/exposure matrices, prepares Stan data, compiles Stan models, samples with NUTS algorithm, extracts results and diagnostics
   - **Models supported**: 4PL+ME (measurement error), 4PL+ME_analytic (analytical ME integration), 4PL simple, 2PL
   - **Key features**: Convergence checking (Rhat, ESS, divergent transitions), calibrated score generation, analytical measurement error support
   - **Status**: 20,780 bytes, recently updated (May 16 04:47)

2. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/fit_irt.py**
   - **Purpose**: Legacy PyTorch-based MLE IRT fitting
   - **Function**: Fits 2PL and 4PL+gamma models using gradient descent optimization in PyTorch
   - **Features**: Builds 4PL+gamma contamination-aware model with γ parameter proportional to item exposure τ
   - **Status**: 12,079 bytes, uses custom nn.Module implementations

3. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006/run_irt_calibration.py**
   - **Purpose**: PyTorch-based IRT calibration (appears to be main exp006 script)
   - **Function**: Comprehensive pipeline with data loading, model fitting, standard error computation
   - **Models**: 2PL (baseline) and 4PL+gamma (contamination-aware)
   - **Output**: Generates JSON with θ, γ, item parameters, calibrated scores, and CIs
   - **Key functions**: `load_eval_results()`, `fit_irt_model()`, `compute_standard_errors()`, `run_2pl()`, `run_4pl_gamma()`
   - **Features**: Supports synthetic data validation, exposure score loading, dosage-based weighting

#### **Intermediate/Derivative Scripts**

4. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006/intermediate/run_irt_stan.py**
   - **Purpose**: Intermediate version of Stan-based calibration pipeline
   - **Status**: Early CmdStanPy implementation (likely precursor to exp006_irt_calibration version)

5. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py**
   - **Purpose**: Multi-benchmark IRT analysis with exclusion rules
   - **Function**: Runs joint fits across MMLU, GSM8K, ARC, HumanEval with per-benchmark and per-scale exclusions (D044/D045/D046/D047/D018)
   - **Models**: Uses 2PL+gamma with oracle dosage exposure

6. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_stratified_irt.py**
   - **Purpose**: Stratified analysis by dosage and model size
   - **Function**: Dose-response analysis (d000/d005/d025/d100) and capacity effects (0.5B/1.5B/3B)
   - **Uses**: Same exclusion rules as pooled analysis

7. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/patch_irt_lr_filter.py**
   - **Purpose**: Patch script to add learning rate (lr) filtering to IRT scripts (D076)
   - **Function**: Reads lr from train_config.json to exclude checkpoints trained with non-standard learning rates

### Stan Model Files

All Stan models implement 4PL+γ IRT with different measurement error approaches:

1. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/contam_irt_4pl_me.stan**
   - Full measurement error model with latent τ parameters (most flexible)
   - Includes sigma_e parameter estimation

2. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/contam_irt_4pl_me_analytic.stan**
   - Analytical measurement error integration (eliminates latent τ)
   - Uses tau_posterior_mean and tau_posterior_var computed in Python
   - **Recommended for large benchmarks** (lower parameter count, same inference)

3. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/contam_irt_4pl_simple.stan**
   - No measurement error baseline
   - Uses observed exposure directly as covariate

4. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/contam_irt_2pl.stan**
   - Simplified 2PL variant (no guessing/inattention parameters c, d)

5. Additional models in other directories:
   - `/artifacts/mvp_simulation/contam_irt_4pl.stan` and `contam_irt_2pl.stan` (simulation)
   - `/artifacts/simulation_sweep/contam_irt_4pl_sweep.stan`
   - `/artifacts/exp006_baselines/stan_models/vanilla_4pl.stan` and `contam_irt_2pl_gamma.stan`

### Which is the Main IRT Fitting Script?

**Primary recommendation: `/artifacts/exp006_irt_calibration/run_irt_stan.py`**

This is the current production IRT fitting script because:
1. Uses **Bayesian MCMC (CmdStanPy)** rather than point estimates
2. Provides **posterior distributions** with CIs and quantiles
3. Includes **convergence diagnostics** (Rhat, ESS, divergent transitions)
4. Supports **analytical measurement error integration** (recommended for benchmarks with many items)
5. Recently updated and actively maintained
6. Generates **calibrated scores** with uncertainty quantification
7. Most flexible model selection (me, me_analytic, simple, 2pl variants)

**Secondary/Legacy: `/artifacts/exp006/run_irt_calibration.py` and `/artifacts/exp006_irt_calibration/fit_irt.py`**

These PyTorch-based scripts provide:
- **MLE point estimates** (faster, no MCMC sampling)
- Useful for exploratory analysis or when posterior distribution not needed
- Standard error calculation via Hessian estimation
- Simpler to modify for quick prototyping

### Modification Points

If you need to modify the main IRT fitting pipeline:
- **Model specification**: Edit `/artifacts/exp006_irt_calibration/contam_irt_4pl_*.stan`
- **Data preparation**: Modify `prepare_stan_data()` in `run_irt_stan.py`
- **Parameter extraction**: Edit `extract_results()` function
- **Convergence settings**: Adjust `NUTS_DEFAULTS` dictionary
- **Priors**: Change prior specifications in Stan `.stan` files
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "f8f42766-b59f-4eff-b031-b7d1b971ecbf",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ for IRT fitting scripts. Specifically:\n\n1. Look in exp006/ directory for any Python scripts related to IRT fitting (run_pooled_4bench_irt.py, run_irt.py, fit_irt.py, etc.)\n2. Also search the broader project for any IRT-related Python files\n3. Look for Stan model files (.stan)\n4. Look for any scripts that build response matrices or call Stan/CmdStan\n\nReport: file paths found, brief description of what each does, and which one appears to be the main IRT fitting script that would need modification.\n\nSearch breadth: very thorough",
    "agentId": "a6ed12a3e9688dcc4",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have a comprehensive view. Let me create a summary report with all the findings:\n\n## Summary Report: IRT Fitting Scripts in contamcal-irt-calibration Project\n\nI've conducted a thorough search of the project and identified all IRT-related scripts and Stan model files. Here's what I found:\n\n### Key IRT Fitting Scripts\n\n#### **Main IRT Fitting Scripts (in exp006_irt_calibration/)**\n\n1. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/run_irt_stan.py**\n   - **Purpose**: Main IRT fitting script using CmdStanPy (Bayesian MCMC)\n   - **Function**: Loads response/exposure matrices, prepares Stan data, compiles Stan models, samples with NUTS algorithm, extracts results and diagnostics\n   - **Models supported**: 4PL+ME (measurement error), 4PL+ME_analytic (analytical ME integration), 4PL simple, 2PL\n   - **Key features**: Convergence checking (Rhat, ESS, divergent transitions), calibrated score generation, analytical measurement error support\n   - **Status**: 20,780 bytes, recently updated (May 16 04:47)\n\n2. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/fit_irt.py**\n   - **Purpose**: Legacy PyTorch-based MLE IRT fitting\n   - **Function**: Fits 2PL and 4PL+gamma models using gradient descent optimization in PyTorch\n   - **Features**: Builds 4PL+gamma contamination-aware model with γ parameter proportional to item exposure τ\n   - **Status**: 12,079 bytes, uses custom nn.Module implementations\n\n3. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006/run_irt_calibration.py**\n   - **Purpose**: PyTorch-based IRT calibration (appears to be main exp006 script)\n   - **Function**: Comprehensive pipeline with data loading, model fitting, standard error computation\n   - **Models**: 2PL (baseline) and 4PL+gamma (contamination-aware)\n   - **Output**: Generates JSON with θ, γ, item parameters, calibrated scores, and CIs\n   - **Key functions**: `load_eval_results()`, `fit_irt_model()`, `compute_standard_errors()`, `run_2pl()`, `run_4pl_gamma()`\n   - **Features**: Supports synthetic data validation, exposure score loading, dosage-based weighting\n\n#### **Intermediate/Derivative Scripts**\n\n4. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006/intermediate/run_irt_stan.py**\n   - **Purpose**: Intermediate version of Stan-based calibration pipeline\n   - **Status**: Early CmdStanPy implementation (likely precursor to exp006_irt_calibration version)\n\n5. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py**\n   - **Purpose**: Multi-benchmark IRT analysis with exclusion rules\n   - **Function**: Runs joint fits across MMLU, GSM8K, ARC, HumanEval with per-benchmark and per-scale exclusions (D044/D045/D046/D047/D018)\n   - **Models**: Uses 2PL+gamma with oracle dosage exposure\n\n6. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_stratified_irt.py**\n   - **Purpose**: Stratified analysis by dosage and model size\n   - **Function**: Dose-response analysis (d000/d005/d025/d100) and capacity effects (0.5B/1.5B/3B)\n   - **Uses**: Same exclusion rules as pooled analysis\n\n7. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/patch_irt_lr_filter.py**\n   - **Purpose**: Patch script to add learning rate (lr) filtering to IRT scripts (D076)\n   - **Function**: Reads lr from train_config.json to exclude checkpoints trained with non-standard learning rates\n\n### Stan Model Files\n\nAll Stan models implement 4PL+γ IRT with different measurement error approaches:\n\n1. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/contam_irt_4pl_me.stan**\n   - Full measurement error model with latent τ parameters (most flexible)\n   - Includes sigma_e parameter estimation\n\n2. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/contam_irt_4pl_me_analytic.stan**\n   - Analytical measurement error integration (eliminates latent τ)\n   - Uses tau_posterior_mean and tau_posterior_var computed in Python\n   - **Recommended for large benchmarks** (lower parameter count, same inference)\n\n3. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/contam_irt_4pl_simple.stan**\n   - No measurement error baseline\n   - Uses observed exposure directly as covariate\n\n4. **/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/contam_irt_2pl.stan**\n   - Simplified 2PL variant (no guessing/inattention parameters c, d)\n\n5. Additional models in other directories:\n   - `/artifacts/mvp_simulation/contam_irt_4pl.stan` and `contam_irt_2pl.stan` (simulation)\n   - `/artifacts/simulation_sweep/contam_irt_4pl_sweep.stan`\n   - `/artifacts/exp006_baselines/stan_models/vanilla_4pl.stan` and `contam_irt_2pl_gamma.stan`\n\n### Which is the Main IRT Fitting Script?\n\n**Primary recommendation: `/artifacts/exp006_irt_calibration/run_irt_stan.py`**\n\nThis is the current production IRT fitting script because:\n1. Uses **Bayesian MCMC (CmdStanPy)** rather than point estimates\n2. Provides **posterior distributions** with CIs and quantiles\n3. Includes **convergence diagnostics** (Rhat, ESS, divergent transitions)\n4. Supports **analytical measurement error integration** (recommended for benchmarks with many items)\n5. Recently updated and actively maintained\n6. Generates **calibrated scores** with uncertainty quantification\n7. Most flexible model selection (me, me_analytic, simple, 2pl variants)\n\n**Secondary/Legacy: `/artifacts/exp006/run_irt_calibration.py` and `/artifacts/exp006_irt_calibration/fit_irt.py`**\n\nThese PyTorch-based scripts provide:\n- **MLE point estimates** (faster, no MCMC sampling)\n- Useful for exploratory analysis or when posterior distribution not needed\n- Standard error calculation via Hessian estimation\n- Simpler to modify for quick prototyping\n\n### Modification Points\n\nIf you need to modify the main IRT fitting pipeline:\n- **Model specification**: Edit `/artifacts/exp006_irt_calibration/contam_irt_4pl_*.stan`\n- **Data preparation**: Modify `prepare_stan_data()` in `run_irt_stan.py`\n- **Parameter extraction**: Edit `extract_results()` function\n- **Convergence settings**: Adjust `NUTS_DEFAULTS` dictionary\n- **Priors**: Change prior specifications in Stan `.stan` files"
      }
    ],
    "totalDurationMs": 37234,
    "totalTokens": 51479,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2299,
      "cache_read_input_tokens": 47126,
      "output_tokens": 2048,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2299
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2048,
          "cache_read_input_tokens": 47126,
          "cache_creation_input_tokens": 2299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2299,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
      "searchCount": 3,
      "bashCount": 4,
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

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_018tuXuXXFJkzT37MMmU3xeg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "c337d708-188a-4cd2-acb0-1b64c6042e0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nZhofBNDPSTvM5mecper2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2440,
      "cache_read_input_tokens": 24911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2440
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

_source line 63 · 2026-05-16T05:29:40.875Z_

<details><summary>↩ Tool result · `toolu_018tuXuXXFJkzT37MMmU3xeg`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Pooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.
4	
5	Runs:
6	  1. Per-benchmark IRT fits (with per-benchmark model exclusions)
7	  2. Joint fit (shared gamma) across benchmarks using intersection models
8	
9	Exclusion rules:
10	  D044: GSM8K exclude d000 configs (format confound)
11	  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept
12	  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)
13	  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)
14	
15	Exposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.
16	"""
17	
18	import argparse
19	import json
20	import logging
21	import os
22	import sys
23	import time
24	from pathlib import Path
25	
26	import numpy as np
27	
28	sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
29	from run_irt_calibration import (
30	    load_pooled_eval_results,
31	    prepare_stan_data,
32	    fit_stan_model,
33	    check_convergence,
34	    posterior_predictive_check,
35	    extract_results,
36	    _summarize_vector,
37	    STAN_MODELS,
38	)
39	
40	log = logging.getLogger(__name__)
41	
42	BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge", "humaneval"]
43	SCALES = ["0.5B", "1.5B", "3B"]
44	MODEL_TYPE = "2pl_gamma"
45	STAN_FILE = STAN_MODELS[MODEL_TYPE]
46	
47	OUTPUT_DIR = Path("/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl")
48	EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
49	
50	
51	def apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):
52	    """Apply D044/D045/D046/D047/D018 per-benchmark exclusions."""
53	    keep = np.ones(len(models), dtype=bool)
54	    reasons = []
55	
56	    for i, m in enumerate(models):
57	        dirname = m.get("dirname", "")
58	        scale = m.get("scale", "")
59	        dosage = m.get("dosage", 0)
60	
61	        # D046/D047: base pretrained
62	        if "base_pretrained" in dirname:
63	            keep[i] = False
64	            reasons.append(f"  D046/D047: {dirname} (base pretrained)")
65	            continue
66	
67	        # D018: deprecated check (dirname contains DEPRECATED)
68	        if "DEPRECATED" in dirname:
69	            keep[i] = False
70	            reasons.append(f"  D018: {dirname} (deprecated)")
71	            continue
72	
73	        # D045: 0.5B MMLU/ARC excluded (position bias)
74	        if "0.5B" in scale and benchmark in ("mmlu", "arc_challenge"):
75	            keep[i] = False
76	            reasons.append(f"  D045: {dirname} (0.5B on {benchmark})")
77	            continue
78	
79	        # D044: GSM8K exclude d000 (format confound)
80	        if benchmark == "gsm8k" and dosage == 0:
81	            keep[i] = False
82	            reasons.append(f"  D044: {dirname} (d000 on gsm8k)")
83	            continue
84	
85	        # Instruct model (no dosage pattern) - keep if aligned
86	        # but skip if not part of dose-response (dosage not parseable)
87	        # Actually Instruct models have dosage=base, which won't parse
88	        # as dosage int. They'll appear with dosage=0 from the loader
89	        # if dirname ends with _aligned without _dXXX pattern.
90	        # The loader sets dosage from parsing, so Instruct models
91	        # are already excluded by parse_model_dir_name returning None.
92	
93	    if reasons:
94	        log.info("Excluded from %s (%d models):", benchmark, len(reasons))
95	        for r in reasons[:10]:
96	            log.info(r)
97	        if len(reasons) > 10:
98	            log.info("  ... and %d more", len(reasons) - 10)
99	
100	    return (
101	        [m for m, k in zip(models, keep) if k],
102	        dosages[keep],
103	        responses[keep],
104	        valid_mask[keep],
105	    )
106	
107	
108	def build_oracle_exposure(dosages, n_items):
109	    """Oracle exposure: dosage_fraction * uniform tau."""
110	    max_d = dosages.max() if dosages.max() > 0 else 1.0
111	    fracs = dosages / max_d
112	    return np.outer(fracs, np.ones(n_items))
113	
114	
115	def filter_items(responses, benchmark, exclude_set=None, min_variance=0.0):
116	    """Remove items by exclusion list and/or low cross-model variance.
117	
118	    Returns (filtered_responses, kept_indices, stats_dict).
119	    """
120	    n_models, n_items = responses.shape
121	    keep = np.ones(n_items, dtype=bool)
122	
123	    n_excluded_by_list = 0
124	    if exclude_set:
125	        for j in range(n_items):
126	            if f"{benchmark}_{j}" in exclude_set:
127	                keep[j] = False
128	                n_excluded_by_list += 1
129	
130	    n_excluded_by_var = 0
131	    if min_variance > 0:
132	        item_var = np.var(responses, axis=0)
133	        low_var = item_var < min_variance
134	        low_var &= keep
135	        n_excluded_by_var = int(low_var.sum())
136	        keep[low_var] = False
137	
138	    kept_indices = np.where(keep)[0]
139	    stats = {
140	        "original": n_items,
141	        "excluded_by_list": n_excluded_by_list,
142	        "excluded_by_variance": n_excluded_by_var,
143	        "remaining": int(keep.sum()),
144	    }
145	    return responses[:, keep], kept_indices, stats
146	
147	
148	def run_single_benchmark_fit(bench, data, args_dict, exclude_set=None, min_item_variance=0.0):
149	    """Run IRT fit for a single benchmark with exclusions."""
150	    if bench not in data["benchmarks"]:
151	        log.warning("Benchmark %s not in data, skipping", bench)
152	        return None
153	
154	    bd = data["benchmarks"][bench]
155	    models_filt, dosages_filt, responses_filt, valid_filt = apply_per_benchmark_exclusions(
156	        data["models"], data["dosages"],
157	        bd["responses"], bd["valid_mask"], bench
158	    )
159	
160	    # Apply valid mask
161	    if not valid_filt.all():
162	        active = valid_filt.astype(bool)
163	        models_filt = [m for m, v in zip(models_filt, active) if v]
164	        dosages_filt = dosages_filt[active]
165	        responses_filt = responses_filt[active]
166	
167	    n_models = len(models_filt)
168	    n_items = bd["n_items"]
169	
170	    if exclude_set or min_item_variance > 0:
171	        responses_filt, kept_indices, fstats = filter_items(
172	            responses_filt, bench, exclude_set, min_item_variance
173	        )
174	        n_items = fstats["remaining"]
175	        log.info("[%s] Item filter: %d -> %d (list=%d, variance=%d)",
176	                 bench, fstats["original"], n_items,
177	                 fstats["excluded_by_list"], fstats["excluded_by_variance"])
178	
179	    log.info("[%s] N_models=%d, N_items=%d", bench, n_models, n_items)
180	
181	    if n_models < 3:
182	        log.warning("[%s] Too few models (%d), skipping", bench, n_models)
183	        return None
184	
185	    exposure = build_oracle_exposure(dosages_filt, n_items)
186	    stan_data = prepare_stan_data(responses_filt, exposure, MODEL_TYPE)
187	
188	    fit, elapsed = fit_stan_model(
189	        STAN_FILE, stan_data,
190	        chains=args_dict["chains"],
191	        iter_warmup=args_dict["warmup"],
192	        iter_sampling=args_dict["samples"],
193	        adapt_delta=args_dict["adapt_delta"],
194	        max_treedepth=args_dict["max_treedepth"],
195	        seed=args_dict["seed"],
196	        parallel_chains=args_dict["parallel_chains"],
197	    )
198	
199	    diagnostics = check_convergence(fit)
200	    ppc = posterior_predictive_check(fit, responses_filt)
201	    results = extract_results(fit, responses_filt, MODEL_TYPE)
202	
203	    return {
204	        "benchmark": bench,
205	        "n_models": n_models,
206	        "n_items": n_items,
207	        "models": [{"dirname": m["dirname"], "dosage": m["dosage"],
208	                     "scale": m.get("scale", "")} for m in models_filt],
209	        "dosages": dosages_filt.tolist(),
210	        "fit_time_sec": round(elapsed, 1),
211	        "diagnostics": diagnostics,
212	        "posterior_predictive": ppc,
213	        "gamma": results.get("gamma", {}),
214	        "calibrated_scores": results.get("calibrated_scores", {}),
215	    }
216	
217	
218	def run_joint_fit(data, benchmarks_to_include, args_dict, exclude_set=None, min_item_variance=0.0):
219	    """Concatenate benchmark items and fit shared-gamma model.
220	
221	    Uses intersection of valid models across all benchmarks (after exclusions).
222	    """
223	    per_bench_filtered = {}
224	    for bench in benchmarks_to_include:
225	        if bench not in data["benchmarks"]:
226	            continue
227	        bd = data["benchmarks"][bench]
228	        models_f, dosages_f, resp_f, valid_f = apply_per_benchmark_exclusions(
229	            data["models"], data["dosages"],
230	            bd["responses"], bd["valid_mask"], bench
231	        )
232	        if not valid_f.all():
233	            active = valid_f.astype(bool)
234	            models_f = [m for m, v in zip(models_f, active) if v]
235	            dosages_f = dosages_f[active]
236	            resp_f = resp_f[active]
237	
238	        per_bench_filtered[bench] = {
239	            "models": models_f,
240	            "dosages": dosages_f,
241	            "responses": resp_f,
242	            "n_items": bd["n_items"],
243	        }
244	
245	    # Find intersection of valid model dirnames across benchmarks
246	    dirname_sets = [set(m["dirname"] for m in bf["models"])
247	                    for bf in per_bench_filtered.values()]
248	    common_dirnames = set.intersection(*dirname_sets) if dirname_sets else set()
249	    log.info("Joint fit: %d common models across %d benchmarks",
250	             len(common_dirnames), len(per_bench_filtered))
251	
252	    if len(common_dirnames) < 3:
253	        log.warning("Too few common models (%d) for joint fit", len(common_dirnames))
254	        return None
255	
256	    # Build concatenated matrices using common model order
257	    ref_bench = list(per_bench_filtered.keys())[0]
258	    ref_models = per_bench_filtered[ref_bench]["models"]
259	    ordered_dirnames = [m["dirname"] for m in ref_models if m["dirname"] in common_dirnames]
260	
261	    all_y = []
262	    all_exp = []
263	    slices = {}
264	    col_offset = 0
265	    joint_models = None
266	    joint_dosages = None
267	
268	    for bench, bf in per_bench_filtered.items():
269	        dirname_to_idx = {m["dirname"]: i for i, m in enumerate(bf["models"])}
270	        indices = [dirname_to_idx[d] for d in ordered_dirnames]
271	
272	        resp_ordered = bf["responses"][indices]
273	        dosages_ordered = bf["dosages"][indices]
274	        n_items = bf["n_items"]
275	
276	        if exclude_set or min_item_variance > 0:
277	            resp_ordered, kept_indices, fstats = filter_items(
278	                resp_ordered, bench, exclude_set, min_item_variance
279	            )
280	            n_items = fstats["remaining"]
281	            log.info("[joint/%s] Item filter: %d -> %d (list=%d, variance=%d)",
282	                     bench, fstats["original"], n_items,
283	                     fstats["excluded_by_list"], fstats["excluded_by_variance"])
284	
285	        exposure = build_oracle_exposure(dosages_ordered, n_items)
286	
287	        all_y.append(resp_ordered)
288	        all_exp.append(exposure)
289	        slices[bench] = (col_offset, col_offset + n_items)
290	        col_offset += n_items
291	
292	        if joint_models is None:
293	            joint_models = [bf["models"][i] for i in indices]
294	            joint_dosages = dosages_ordered
295	
296	    y_concat = np.concatenate(all_y, axis=1)
297	    exp_concat = np.concatenate(all_exp, axis=1)
298	
299	    n_models, n_total = y_concat.shape
300	    log.info("Joint fit: %d models x %d total items", n_models, n_total)
301	    log.info("Joint fit slices: %s", {b: f"{s[0]}-{s[1]}" for b, s in slices.items()})
302	
303	    stan_data = prepare_stan_data(y_concat, exp_concat, MODEL_TYPE)
304	
305	    fit, elapsed = fit_stan_model(
306	        STAN_FILE, stan_data,
307	        chains=args_dict["chains"],
308	        iter_warmup=args_dict["warmup"],
309	        iter_sampling=args_dict["samples"],
310	        adapt_delta=args_dict["adapt_delta"],
311	        max_treedepth=args_dict["max_treedepth"],
312	        seed=args_dict["seed"],
313	        parallel_chains=args_dict["parallel_chains"],
314	    )
315	
316	    diagnostics = check_convergence(fit)
317	    ppc = posterior_predictive_check(fit, y_concat)
318	    results = extract_results(fit, y_concat, MODEL_TYPE)
319	
320	    # Per-benchmark calibrated scores from joint model
321	    gamma_draws = fit.stan_variable("gamma")
322	    theta_draws = fit.stan_variable("theta")
323	    a_draws = fit.stan_variable("a")
324	    b_draws = fit.stan_variable("b")
325	
326	    per_bench_cal = {}
327	    for bench, (start, end) in slices.items():
328	        n_bench_items = end - start
329	        n_draws = gamma_draws.shape[0]
330	        bench_cal = np.zeros((n_draws, n_models))
331	        for draw in range(n_draws):
332	            for i in range(n_models):
333	                total = 0.0
334	                for j in range(start, end):
335	                    eta_clean = a_draws[draw, j] * (theta_draws[draw, i] - b_draws[draw, j])
336	                    total += 1.0 / (1.0 + np.exp(-eta_clean))
337	                bench_cal[draw, i] = total / n_bench_items
338	        per_bench_cal[bench] = {
339	            "mean": bench_cal.mean(axis=0).tolist(),
340	            "sd": bench_cal.std(axis=0).tolist(),
341	        }
342	
343	    return {
344	        "mode": "joint_fit_4bench",
345	        "model_type": MODEL_TYPE,
346	        "n_models": n_models,
347	        "n_total_items": n_total,
348	        "benchmark_slices": {k: list(v) for k, v in slices.items()},
349	        "models": [{"dirname": m["dirname"], "dosage": m["dosage"],
350	                     "scale": m.get("scale", "")} for m in joint_models],
351	        "dosages": joint_dosages.tolist(),
352	        "fit_time_sec": round(elapsed, 1),
353	        "diagnostics": diagnostics,
354	        "posterior_predictive": ppc,
355	        "global_gamma": results.get("gamma", {}),
356	        "calibrated_scores": results.get("calibrated_scores", {}),
357	        "calibrated_scores_per_benchmark": per_bench_cal,
358	    }
359	
360	
361	def parse_args():
362	    parser = argparse.ArgumentParser(
363	        description="Pooled 4-benchmark IRT analysis (2PL+gamma)"
364	    )
365	    parser.add_argument(
366	        "--exclude-items", type=str, default=None,
367	        help="JSON file with list of item_ids to exclude (e.g. [\"mmlu_42\", \"mmlu_103\"])",
368	    )
369	    parser.add_argument(
370	        "--min-item-variance", type=float, default=0.0,
371	        help="Exclude items with cross-model variance below this threshold (default: 0, disabled)",
372	    )
373	    return parser.parse_args()
374	
375	
376	def main():
377	    logging.basicConfig(
378	        level=logging.INFO,
379	        format="%(asctime)s [%(levelname)s] %(message)s",
380	    )
381	
382	    args = parse_args()
383	
384	    exclude_set = None
385	    if args.exclude_items:
386	        with open(args.exclude_items) as f:
387	            exclude_list = json.load(f)
388	        exclude_set = set(exclude_list)
389	        log.info("Loaded %d item_ids to exclude from %s", len(exclude_set), args.exclude_items)
390	
391	    args_dict = {
392	        "chains": 4,
393	        "warmup": 1000,
394	        "samples": 1000,
395	        "adapt_delta": 0.95,
396	        "max_treedepth": 12,
397	        "seed": 42,
398	        "parallel_chains": 1,
399	    }
400	
401	    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
402	
403	    log.info("Loading pooled eval results: scales=%s, benchmarks=%s", SCALES, BENCHMARKS)
404	    t0 = time.time()
405	    data = load_pooled_eval_results(
406	        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True
407	    )
408	    log.info("Loaded %d models in %.1fs", len(data["models"]), time.time() - t0)
409	    log.info("Dosages: %s", data["dosages"].tolist())
410	    log.info("Benchmarks: %s", list(data["benchmarks"].keys()))
411	
412	    all_results = {
413	        "config": {
414	            "model_type": MODEL_TYPE,
415	            "scales": SCALES,
416	            "benchmarks": BENCHMARKS,
417	            "exposure": "oracle_dosage",
418	            "exclusions": ["D044_gsm8k_d000", "D045_05B_mmlu_arc",
419	                           "D046_D047_base_pretrained", "D018_deprecated"],
420	            "item_filter": {
421	                "exclude_items_file": args.exclude_items,
422	                "exclude_items_count": len(exclude_set) if exclude_set else 0,
423	                "min_item_variance": args.min_item_variance,
424	            },
425	            "stan_config": args_dict,
426	        },
427	        "per_benchmark": {},
428	        "joint_fit": None,
429	    }
430	
431	    # Phase 1: Per-benchmark IRT fits
432	    log.info("=" * 60)
433	    log.info("PHASE 1: Per-benchmark IRT fits")
434	    log.info("=" * 60)
435	
436	    for bench in BENCHMARKS:
437	        log.info("-" * 40)
438	        log.info("Fitting %s...", bench)
439	        result = run_single_benchmark_fit(
440	            bench, data, args_dict, exclude_set, args.min_item_variance
441	        )
442	        if result:
443	            all_results["per_benchmark"][bench] = result
444	            g = result["gamma"]
445	            d = result["diagnostics"]
446	            log.info("[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d",
447	                     bench, g["mean"], g["q025"], g["q975"],
448	                     d.get("max_rhat", 0), d.get("min_ess", 0),
449	                     d.get("divergent_count", 0))
450	
451	            bench_dir = OUTPUT_DIR / bench
452	            bench_dir.mkdir(parents=True, exist_ok=True)
453	            with open(bench_dir / "irt_results.json", "w") as f:
454	                json.dump(result, f, indent=2)
455	
456	    # Phase 2: Joint fit (shared gamma)
457	    log.info("=" * 60)
458	    log.info("PHASE 2: Joint fit (shared gamma across benchmarks)")
459	    log.info("=" * 60)
460	
461	    included_benchmarks = list(all_results["per_benchmark"].keys())
462	    joint_result = run_joint_fit(
463	        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance
464	    )
465	    if joint_result:
466	        all_results["joint_fit"] = joint_result
467	        g = joint_result["global_gamma"]
468	        d = joint_result["diagnostics"]
469	        log.info("JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d",
470	                 g["mean"], g["q025"], g["q975"],
471	                 d.get("max_rhat", 0), d.get("min_ess", 0),
472	                 d.get("divergent_count", 0))
473	
474	        with open(OUTPUT_DIR / "joint_fit_results.json", "w") as f:
475	            json.dump(joint_result, f, indent=2)
476	
477	    # Save full results
478	    with open(OUTPUT_DIR / "pooled_4bench_results.json", "w") as f:
479	        json.dump(all_results, f, indent=2)
480	
481	    # Print summary
482	    print("\n" + "=" * 60)
483	    print("POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)")
484	    print("=" * 60)
485	
486	    if joint_result:
487	        g = joint_result["global_gamma"]
488	        d = joint_result["diagnostics"]
489	        ppc = joint_result["posterior_predictive"]
490	
491	        # Coverage from calibrated scores
492	        cal = joint_result["calibrated_scores"]
493	        if "ci95_lower" in cal and "ci95_upper" in cal:
494	            lowers = np.array(cal["ci95_lower"])
495	            uppers = np.array(cal["ci95_upper"])
496	            # Ground truth approximation: d0 models have raw accuracy as truth
497	            dosages_arr = np.array(joint_result["dosages"])
498	            # For d0 models, calibrated score IS the ground truth
499	            # For d>0 models, compare calibrated CI with d0 mean
500	            # This is a simplified coverage check
501	            n_total = len(dosages_arr)
502	            in_ci = 0
503	            for i in range(n_total):
504	                # Coverage: does 95% CI contain a reasonable reference?
505	                # For overall coverage, check if CI width > 0
506	                if uppers[i] > lowers[i]:
507	                    in_ci += 1
508	            coverage = in_ci / n_total * 100 if n_total > 0 else 0
509	            print(f"COVERAGE: C95={coverage:.0f}% (all CIs valid)")
510	        else:
511	            # Use mean/sd to compute coverage
512	            means = np.array(cal.get("mean", []))
513	            sds = np.array(cal.get("sd", []))
514	            print(f"COVERAGE: need ground truth reference for proper C95")
515	
516	        print(f"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, "
517	              f"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]")
518	        print(f"PPP: {ppc.get('overall_ppp', 'N/A')}")
519	        print(f"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, "
520	              f"ESS={d.get('min_ess', 'N/A')}, "
521	              f"divergences={d.get('divergent_count', 'N/A')}")
522	        print(f"N_MODELS: {joint_result['n_models']}, "
523	              f"N_ITEMS: {joint_result['n_total_items']}")
524	
525	    print("\nPER_BENCHMARK_GAMMA:")
526	    for bench in BENCHMARKS:
527	        if bench in all_results["per_benchmark"]:
528	            g = all_results["per_benchmark"][bench]["gamma"]
529	            n = all_results["per_benchmark"][bench]["n_models"]
530	            ni = all_results["per_benchmark"][bench]["n_items"]
531	            print(f"  {bench}: gamma={g['mean']:.4f} "
532	                  f"[{g['q025']:.4f}, {g['q975']:.4f}] "
533	                  f"(N={n}, items={ni})")
534	        else:
535	            print(f"  {bench}: SKIPPED")
536	
537	    print(f"\nResults saved to {OUTPUT_DIR}")
538	
539	
540	if __name__ == "__main__":
541	    main()
542	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "1c13f73c-3172-437f-9e4a-830310580dcf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nPooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.\n\nRuns:\n  1. Per-benchmark IRT fits (with per-benchmark model exclusions)\n  2. Joint fit (shared gamma) across benchmarks using intersection models\n\nExclusion rules:\n  D044: GSM8K exclude d000 configs (format confound)\n  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept\n  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)\n  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)\n\nExposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\n\nsys.path.insert(0, \"/root/contamcal-irt-calibration/exp006\")\nfrom run_irt_calibration import (\n    load_pooled_eval_results,\n    prepare_stan_data,\n    fit_stan_model,\n    check_convergence,\n    posterior_predictive_check,\n    extract_results,\n    _summarize_vector,\n    STAN_MODELS,\n)\n\nlog = logging.getLogger(__name__)\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\", \"humaneval\"]\nSCALES = [\"0.5B\", \"1.5B\", \"3B\"]\nMODEL_TYPE = \"2pl_gamma\"\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\n\nOUTPUT_DIR = Path(\"/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl\")\nEVAL_DIR = \"/root/autodl-tmp/exp001/eval_results\"\n\n\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\n    \"\"\"Apply D044/D045/D046/D047/D018 per-benchmark exclusions.\"\"\"\n    keep = np.ones(len(models), dtype=bool)\n    reasons = []\n\n    for i, m in enumerate(models):\n        dirname = m.get(\"dirname\", \"\")\n        scale = m.get(\"scale\", \"\")\n        dosage = m.get(\"dosage\", 0)\n\n        # D046/D047: base pretrained\n        if \"base_pretrained\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D046/D047: {dirname} (base pretrained)\")\n            continue\n\n        # D018: deprecated check (dirname contains DEPRECATED)\n        if \"DEPRECATED\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D018: {dirname} (deprecated)\")\n            continue\n\n        # D045: 0.5B MMLU/ARC excluded (position bias)\n        if \"0.5B\" in scale and benchmark in (\"mmlu\", \"arc_challenge\"):\n            keep[i] = False\n            reasons.append(f\"  D045: {dirname} (0.5B on {benchmark})\")\n            continue\n\n        # D044: GSM8K exclude d000 (format confound)\n        if benchmark == \"gsm8k\" and dosage == 0:\n            keep[i] = False\n            reasons.append(f\"  D044: {dirname} (d000 on gsm8k)\")\n            continue\n\n        # Instruct model (no dosage pattern) - keep if aligned\n        # but skip if not part of dose-response (dosage not parseable)\n        # Actually Instruct models have dosage=base, which won't parse\n        # as dosage int. They'll appear with dosage=0 from the loader\n        # if dirname ends with _aligned without _dXXX pattern.\n        # The loader sets dosage from parsing, so Instruct models\n        # are already excluded by parse_model_dir_name returning None.\n\n    if reasons:\n        log.info(\"Excluded from %s (%d models):\", benchmark, len(reasons))\n        for r in reasons[:10]:\n            log.info(r)\n        if len(reasons) > 10:\n            log.info(\"  ... and %d more\", len(reasons) - 10)\n\n    return (\n        [m for m, k in zip(models, keep) if k],\n        dosages[keep],\n        responses[keep],\n        valid_mask[keep],\n    )\n\n\ndef build_oracle_exposure(dosages, n_items):\n    \"\"\"Oracle exposure: dosage_fraction * uniform tau.\"\"\"\n    max_d = dosages.max() if dosages.max() > 0 else 1.0\n    fracs = dosages / max_d\n    return np.outer(fracs, np.ones(n_items))\n\n\ndef filter_items(responses, benchmark, exclude_set=None, min_variance=0.0):\n    \"\"\"Remove items by exclusion list and/or low cross-model variance.\n\n    Returns (filtered_responses, kept_indices, stats_dict).\n    \"\"\"\n    n_models, n_items = responses.shape\n    keep = np.ones(n_items, dtype=bool)\n\n    n_excluded_by_list = 0\n    if exclude_set:\n        for j in range(n_items):\n            if f\"{benchmark}_{j}\" in exclude_set:\n                keep[j] = False\n                n_excluded_by_list += 1\n\n    n_excluded_by_var = 0\n    if min_variance > 0:\n        item_var = np.var(responses, axis=0)\n        low_var = item_var < min_variance\n        low_var &= keep\n        n_excluded_by_var = int(low_var.sum())\n        keep[low_var] = False\n\n    kept_indices = np.where(keep)[0]\n    stats = {\n        \"original\": n_items,\n        \"excluded_by_list\": n_excluded_by_list,\n        \"excluded_by_variance\": n_excluded_by_var,\n        \"remaining\": int(keep.sum()),\n    }\n    return responses[:, keep], kept_indices, stats\n\n\ndef run_single_benchmark_fit(bench, data, args_dict, exclude_set=None, min_item_variance=0.0):\n    \"\"\"Run IRT fit for a single benchmark with exclusions.\"\"\"\n    if bench not in data[\"benchmarks\"]:\n        log.warning(\"Benchmark %s not in data, skipping\", bench)\n        return None\n\n    bd = data[\"benchmarks\"][bench]\n    models_filt, dosages_filt, responses_filt, valid_filt = apply_per_benchmark_exclusions(\n        data[\"models\"], data[\"dosages\"],\n        bd[\"responses\"], bd[\"valid_mask\"], bench\n    )\n\n    # Apply valid mask\n    if not valid_filt.all():\n        active = valid_filt.astype(bool)\n        models_filt = [m for m, v in zip(models_filt, active) if v]\n        dosages_filt = dosages_filt[active]\n        responses_filt = responses_filt[active]\n\n    n_models = len(models_filt)\n    n_items = bd[\"n_items\"]\n\n    if exclude_set or min_item_variance > 0:\n        responses_filt, kept_indices, fstats = filter_items(\n            responses_filt, bench, exclude_set, min_item_variance\n        )\n        n_items = fstats[\"remaining\"]\n        log.info(\"[%s] Item filter: %d -> %d (list=%d, variance=%d)\",\n                 bench, fstats[\"original\"], n_items,\n                 fstats[\"excluded_by_list\"], fstats[\"excluded_by_variance\"])\n\n    log.info(\"[%s] N_models=%d, N_items=%d\", bench, n_models, n_items)\n\n    if n_models < 3:\n        log.warning(\"[%s] Too few models (%d), skipping\", bench, n_models)\n        return None\n\n    exposure = build_oracle_exposure(dosages_filt, n_items)\n    stan_data = prepare_stan_data(responses_filt, exposure, MODEL_TYPE)\n\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, responses_filt)\n    results = extract_results(fit, responses_filt, MODEL_TYPE)\n\n    return {\n        \"benchmark\": bench,\n        \"n_models\": n_models,\n        \"n_items\": n_items,\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in models_filt],\n        \"dosages\": dosages_filt.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n    }\n\n\ndef run_joint_fit(data, benchmarks_to_include, args_dict, exclude_set=None, min_item_variance=0.0):\n    \"\"\"Concatenate benchmark items and fit shared-gamma model.\n\n    Uses intersection of valid models across all benchmarks (after exclusions).\n    \"\"\"\n    per_bench_filtered = {}\n    for bench in benchmarks_to_include:\n        if bench not in data[\"benchmarks\"]:\n            continue\n        bd = data[\"benchmarks\"][bench]\n        models_f, dosages_f, resp_f, valid_f = apply_per_benchmark_exclusions(\n            data[\"models\"], data[\"dosages\"],\n            bd[\"responses\"], bd[\"valid_mask\"], bench\n        )\n        if not valid_f.all():\n            active = valid_f.astype(bool)\n            models_f = [m for m, v in zip(models_f, active) if v]\n            dosages_f = dosages_f[active]\n            resp_f = resp_f[active]\n\n        per_bench_filtered[bench] = {\n            \"models\": models_f,\n            \"dosages\": dosages_f,\n            \"responses\": resp_f,\n            \"n_items\": bd[\"n_items\"],\n        }\n\n    # Find intersection of valid model dirnames across benchmarks\n    dirname_sets = [set(m[\"dirname\"] for m in bf[\"models\"])\n                    for bf in per_bench_filtered.values()]\n    common_dirnames = set.intersection(*dirname_sets) if dirname_sets else set()\n    log.info(\"Joint fit: %d common models across %d benchmarks\",\n             len(common_dirnames), len(per_bench_filtered))\n\n    if len(common_dirnames) < 3:\n        log.warning(\"Too few common models (%d) for joint fit\", len(common_dirnames))\n        return None\n\n    # Build concatenated matrices using common model order\n    ref_bench = list(per_bench_filtered.keys())[0]\n    ref_models = per_bench_filtered[ref_bench][\"models\"]\n    ordered_dirnames = [m[\"dirname\"] for m in ref_models if m[\"dirname\"] in common_dirnames]\n\n    all_y = []\n    all_exp = []\n    slices = {}\n    col_offset = 0\n    joint_models = None\n    joint_dosages = None\n\n    for bench, bf in per_bench_filtered.items():\n        dirname_to_idx = {m[\"dirname\"]: i for i, m in enumerate(bf[\"models\"])}\n        indices = [dirname_to_idx[d] for d in ordered_dirnames]\n\n        resp_ordered = bf[\"responses\"][indices]\n        dosages_ordered = bf[\"dosages\"][indices]\n        n_items = bf[\"n_items\"]\n\n        if exclude_set or min_item_variance > 0:\n            resp_ordered, kept_indices, fstats = filter_items(\n                resp_ordered, bench, exclude_set, min_item_variance\n            )\n            n_items = fstats[\"remaining\"]\n            log.info(\"[joint/%s] Item filter: %d -> %d (list=%d, variance=%d)\",\n                     bench, fstats[\"original\"], n_items,\n                     fstats[\"excluded_by_list\"], fstats[\"excluded_by_variance\"])\n\n        exposure = build_oracle_exposure(dosages_ordered, n_items)\n\n        all_y.append(resp_ordered)\n        all_exp.append(exposure)\n        slices[bench] = (col_offset, col_offset + n_items)\n        col_offset += n_items\n\n        if joint_models is None:\n            joint_models = [bf[\"models\"][i] for i in indices]\n            joint_dosages = dosages_ordered\n\n    y_concat = np.concatenate(all_y, axis=1)\n    exp_concat = np.concatenate(all_exp, axis=1)\n\n    n_models, n_total = y_concat.shape\n    log.info(\"Joint fit: %d models x %d total items\", n_models, n_total)\n    log.info(\"Joint fit slices: %s\", {b: f\"{s[0]}-{s[1]}\" for b, s in slices.items()})\n\n    stan_data = prepare_stan_data(y_concat, exp_concat, MODEL_TYPE)\n\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, y_concat)\n    results = extract_results(fit, y_concat, MODEL_TYPE)\n\n    # Per-benchmark calibrated scores from joint model\n    gamma_draws = fit.stan_variable(\"gamma\")\n    theta_draws = fit.stan_variable(\"theta\")\n    a_draws = fit.stan_variable(\"a\")\n    b_draws = fit.stan_variable(\"b\")\n\n    per_bench_cal = {}\n    for bench, (start, end) in slices.items():\n        n_bench_items = end - start\n        n_draws = gamma_draws.shape[0]\n        bench_cal = np.zeros((n_draws, n_models))\n        for draw in range(n_draws):\n            for i in range(n_models):\n                total = 0.0\n                for j in range(start, end):\n                    eta_clean = a_draws[draw, j] * (theta_draws[draw, i] - b_draws[draw, j])\n                    total += 1.0 / (1.0 + np.exp(-eta_clean))\n                bench_cal[draw, i] = total / n_bench_items\n        per_bench_cal[bench] = {\n            \"mean\": bench_cal.mean(axis=0).tolist(),\n            \"sd\": bench_cal.std(axis=0).tolist(),\n        }\n\n    return {\n        \"mode\": \"joint_fit_4bench\",\n        \"model_type\": MODEL_TYPE,\n        \"n_models\": n_models,\n        \"n_total_items\": n_total,\n        \"benchmark_slices\": {k: list(v) for k, v in slices.items()},\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in joint_models],\n        \"dosages\": joint_dosages.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"global_gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n        \"calibrated_scores_per_benchmark\": per_bench_cal,\n    }\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(\n        description=\"Pooled 4-benchmark IRT analysis (2PL+gamma)\"\n    )\n    parser.add_argument(\n        \"--exclude-items\", type=str, default=None,\n        help=\"JSON file with list of item_ids to exclude (e.g. [\\\"mmlu_42\\\", \\\"mmlu_103\\\"])\",\n    )\n    parser.add_argument(\n        \"--min-item-variance\", type=float, default=0.0,\n        help=\"Exclude items with cross-model variance below this threshold (default: 0, disabled)\",\n    )\n    return parser.parse_args()\n\n\ndef main():\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    args = parse_args()\n\n    exclude_set = None\n    if args.exclude_items:\n        with open(args.exclude_items) as f:\n            exclude_list = json.load(f)\n        exclude_set = set(exclude_list)\n        log.info(\"Loaded %d item_ids to exclude from %s\", len(exclude_set), args.exclude_items)\n\n    args_dict = {\n        \"chains\": 4,\n        \"warmup\": 1000,\n        \"samples\": 1000,\n        \"adapt_delta\": 0.95,\n        \"max_treedepth\": 12,\n        \"seed\": 42,\n        \"parallel_chains\": 1,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    log.info(\"Loading pooled eval results: scales=%s, benchmarks=%s\", SCALES, BENCHMARKS)\n    t0 = time.time()\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n    )\n    log.info(\"Loaded %d models in %.1fs\", len(data[\"models\"]), time.time() - t0)\n    log.info(\"Dosages: %s\", data[\"dosages\"].tolist())\n    log.info(\"Benchmarks: %s\", list(data[\"benchmarks\"].keys()))\n\n    all_results = {\n        \"config\": {\n            \"model_type\": MODEL_TYPE,\n            \"scales\": SCALES,\n            \"benchmarks\": BENCHMARKS,\n            \"exposure\": \"oracle_dosage\",\n            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",\n                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],\n            \"item_filter\": {\n                \"exclude_items_file\": args.exclude_items,\n                \"exclude_items_count\": len(exclude_set) if exclude_set else 0,\n                \"min_item_variance\": args.min_item_variance,\n            },\n            \"stan_config\": args_dict,\n        },\n        \"per_benchmark\": {},\n        \"joint_fit\": None,\n    }\n\n    # Phase 1: Per-benchmark IRT fits\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 1: Per-benchmark IRT fits\")\n    log.info(\"=\" * 60)\n\n    for bench in BENCHMARKS:\n        log.info(\"-\" * 40)\n        log.info(\"Fitting %s...\", bench)\n        result = run_single_benchmark_fit(\n            bench, data, args_dict, exclude_set, args.min_item_variance\n        )\n        if result:\n            all_results[\"per_benchmark\"][bench] = result\n            g = result[\"gamma\"]\n            d = result[\"diagnostics\"]\n            log.info(\"[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                     bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                     d.get(\"divergent_count\", 0))\n\n            bench_dir = OUTPUT_DIR / bench\n            bench_dir.mkdir(parents=True, exist_ok=True)\n            with open(bench_dir / \"irt_results.json\", \"w\") as f:\n                json.dump(result, f, indent=2)\n\n    # Phase 2: Joint fit (shared gamma)\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 2: Joint fit (shared gamma across benchmarks)\")\n    log.info(\"=\" * 60)\n\n    included_benchmarks = list(all_results[\"per_benchmark\"].keys())\n    joint_result = run_joint_fit(\n        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance\n    )\n    if joint_result:\n        all_results[\"joint_fit\"] = joint_result\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        log.info(\"JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                 g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                 d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                 d.get(\"divergent_count\", 0))\n\n        with open(OUTPUT_DIR / \"joint_fit_results.json\", \"w\") as f:\n            json.dump(joint_result, f, indent=2)\n\n    # Save full results\n    with open(OUTPUT_DIR / \"pooled_4bench_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Print summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)\")\n    print(\"=\" * 60)\n\n    if joint_result:\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        ppc = joint_result[\"posterior_predictive\"]\n\n        # Coverage from calibrated scores\n        cal = joint_result[\"calibrated_scores\"]\n        if \"ci95_lower\" in cal and \"ci95_upper\" in cal:\n            lowers = np.array(cal[\"ci95_lower\"])\n            uppers = np.array(cal[\"ci95_upper\"])\n            # Ground truth approximation: d0 models have raw accuracy as truth\n            dosages_arr = np.array(joint_result[\"dosages\"])\n            # For d0 models, calibrated score IS the ground truth\n            # For d>0 models, compare calibrated CI with d0 mean\n            # This is a simplified coverage check\n            n_total = len(dosages_arr)\n            in_ci = 0\n            for i in range(n_total):\n                # Coverage: does 95% CI contain a reasonable reference?\n                # For overall coverage, check if CI width > 0\n                if uppers[i] > lowers[i]:\n                    in_ci += 1\n            coverage = in_ci / n_total * 100 if n_total > 0 else 0\n            print(f\"COVERAGE: C95={coverage:.0f}% (all CIs valid)\")\n        else:\n            # Use mean/sd to compute coverage\n            means = np.array(cal.get(\"mean\", []))\n            sds = np.array(cal.get(\"sd\", []))\n            print(f\"COVERAGE: need ground truth reference for proper C95\")\n\n        print(f\"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, \"\n              f\"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]\")\n        print(f\"PPP: {ppc.get('overall_ppp', 'N/A')}\")\n        print(f\"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, \"\n              f\"ESS={d.get('min_ess', 'N/A')}, \"\n              f\"divergences={d.get('divergent_count', 'N/A')}\")\n        print(f\"N_MODELS: {joint_result['n_models']}, \"\n              f\"N_ITEMS: {joint_result['n_total_items']}\")\n\n    print(\"\\nPER_BENCHMARK_GAMMA:\")\n    for bench in BENCHMARKS:\n        if bench in all_results[\"per_benchmark\"]:\n            g = all_results[\"per_benchmark\"][bench][\"gamma\"]\n            n = all_results[\"per_benchmark\"][bench][\"n_models\"]\n            ni = all_results[\"per_benchmark\"][bench][\"n_items\"]\n            print(f\"  {bench}: gamma={g['mean']:.4f} \"\n                  f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                  f\"(N={n}, items={ni})\")\n        else:\n            print(f\"  {bench}: SKIPPED\")\n\n    print(f\"\\nResults saved to {OUTPUT_DIR}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 542,
      "startLine": 1,
      "totalLines": 542
    }
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_014ZhnBUxuyTRztfk2hDJDXx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_stratified_irt.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "d8ec4f79-4ac3-4393-8188-9dda783b867c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nZhofBNDPSTvM5mecper2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2440,
      "cache_read_input_tokens": 24911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2440
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

_source line 65 · 2026-05-16T05:29:41.351Z_

<details><summary>↩ Tool result · `toolu_014ZhnBUxuyTRztfk2hDJDXx`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Stratified IRT analysis: dose-response and model-size strata.
4	
5	Scheme A: by dosage (d000/d005/d025/d100) — checks dose-response in gamma
6	Scheme B: by model size (0.5B/1.5B/3B) — checks if gamma varies by capacity
7	
8	Same exclusion rules as pooled analysis (D044/D045/D046/D047/D018).
9	Oracle dosage as exposure (dosage/100 global normalization). 2PL+gamma model.
10	"""
11	
12	import argparse
13	import json
14	import logging
15	import os
16	import sys
17	import time
18	from pathlib import Path
19	
20	import numpy as np
21	
22	sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
23	from run_irt_calibration import (
24	    load_pooled_eval_results,
25	    prepare_stan_data,
26	    fit_stan_model,
27	    check_convergence,
28	    posterior_predictive_check,
29	    extract_results,
30	    STAN_MODELS,
31	)
32	
33	log = logging.getLogger(__name__)
34	
35	BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge", "humaneval"]
36	SCALES = ["0.5B", "1.5B", "3B"]
37	MODEL_TYPE = "2pl_gamma"
38	STAN_FILE = STAN_MODELS[MODEL_TYPE]
39	
40	EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
41	OUTPUT_DIR = Path("/root/autodl-tmp/exp006/results_stratified_irt")
42	
43	MAX_ITEMS = 2000
44	
45	DOSAGE_GROUPS = {
46	    "d000": [0],
47	    "d005": [5],
48	    "d025": [25],
49	    "d100": [100],
50	}
51	
52	SCALE_GROUPS = {
53	    "scale_0.5B": ["0.5B"],
54	    "scale_1.5B": ["1.5B"],
55	    "scale_3B": ["3B"],
56	}
57	
58	
59	def apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):
60	    keep = np.ones(len(models), dtype=bool)
61	    reasons = []
62	
63	    for i, m in enumerate(models):
64	        dirname = m.get("dirname", "")
65	        scale = m.get("scale", "")
66	        dosage = m.get("dosage", 0)
67	
68	        if "base_pretrained" in dirname:
69	            keep[i] = False
70	            reasons.append(f"  D046/D047: {dirname}")
71	            continue
72	        if "DEPRECATED" in dirname:
73	            keep[i] = False
74	            reasons.append(f"  D018: {dirname}")
75	            continue
76	        if "0.5B" in scale and benchmark in ("mmlu", "arc_challenge"):
77	            keep[i] = False
78	            reasons.append(f"  D045: {dirname}")
79	            continue
80	        if benchmark == "gsm8k" and dosage == 0:
81	            keep[i] = False
82	            reasons.append(f"  D044: {dirname}")
83	            continue
84	
85	    if reasons:
86	        log.info("Excluded from %s (%d):", benchmark, len(reasons))
87	        for r in reasons[:5]:
88	            log.info(r)
89	        if len(reasons) > 5:
90	            log.info("  ... +%d more", len(reasons) - 5)
91	
92	    return (
93	        [m for m, k in zip(models, keep) if k],
94	        dosages[keep],
95	        responses[keep],
96	        valid_mask[keep],
97	    )
98	
99	
100	def build_oracle_exposure_global(dosages, n_items):
101	    """Oracle exposure with global normalization: dosage/100."""
102	    fracs = dosages.astype(float) / 100.0
103	    return np.outer(fracs, np.ones(n_items))
104	
105	
106	def filter_by_dosage(models, dosages, benchmarks_data, target_dosages):
107	    keep = np.array([d in target_dosages for d in dosages])
108	    filt_models = [m for m, k in zip(models, keep) if k]
109	    filt_dosages = dosages[keep]
110	    filt_bench = {}
111	    for bench, bd in benchmarks_data.items():
112	        filt_bench[bench] = {
113	            "responses": bd["responses"][keep],
114	            "n_items": bd["n_items"],
115	            "valid_mask": bd["valid_mask"][keep],
116	        }
117	    return filt_models, filt_dosages, filt_bench
118	
119	
120	def filter_by_scale(models, dosages, benchmarks_data, target_scales):
121	    keep = np.array([m.get("scale", "") in target_scales for m in models])
122	    filt_models = [m for m, k in zip(models, keep) if k]
123	    filt_dosages = dosages[keep]
124	    filt_bench = {}
125	    for bench, bd in benchmarks_data.items():
126	        filt_bench[bench] = {
127	            "responses": bd["responses"][keep],
128	            "n_items": bd["n_items"],
129	            "valid_mask": bd["valid_mask"][keep],
130	        }
131	    return filt_models, filt_dosages, filt_bench
132	
133	
134	def run_stratum_fit(stratum_name, models, dosages, bench_data, benchmark, args_dict):
135	    responses = bench_data["responses"]
136	    valid_mask = bench_data["valid_mask"]
137	    n_items = bench_data["n_items"]
138	
139	    models_f, dosages_f, responses_f, valid_f = apply_per_benchmark_exclusions(
140	        models, dosages, responses, valid_mask, benchmark
141	    )
142	
143	    if not valid_f.all():
144	        active = valid_f.astype(bool)
145	        models_f = [m for m, v in zip(models_f, active) if v]
146	        dosages_f = dosages_f[active]
147	        responses_f = responses_f[active]
148	
149	    n_models = len(models_f)
150	    original_n_items = n_items
151	    subsampled = False
152	    if n_items > MAX_ITEMS:
153	        np.random.seed(42)
154	        indices = np.random.choice(n_items, MAX_ITEMS, replace=False)
155	        indices.sort()
156	        responses_f = responses_f[:, indices]
157	        n_items = MAX_ITEMS
158	        subsampled = True
159	
160	    if n_models < 3:
161	        log.warning("[%s/%s] Too few models (%d), skipping", stratum_name, benchmark, n_models)
162	        return None
163	
164	    unique_dosages = np.unique(dosages_f)
165	    has_dosage_variation = len(unique_dosages) > 1
166	
167	    exposure = build_oracle_exposure_global(dosages_f, n_items)
168	
169	    log.info("[%s/%s] %d models x %d items, dosages=%s",
170	             stratum_name, benchmark, n_models, n_items, unique_dosages.tolist())
171	
172	    stan_data = prepare_stan_data(responses_f, exposure, MODEL_TYPE)
173	    fit, elapsed = fit_stan_model(
174	        STAN_FILE, stan_data,
175	        chains=args_dict["chains"],
176	        iter_warmup=args_dict["warmup"],
177	        iter_sampling=args_dict["samples"],
178	        adapt_delta=args_dict["adapt_delta"],
179	        max_treedepth=args_dict["max_treedepth"],
180	        seed=args_dict["seed"],
181	        parallel_chains=args_dict["parallel_chains"],
182	    )
183	
184	    diagnostics = check_convergence(fit)
185	    ppc = posterior_predictive_check(fit, responses_f)
186	    results = extract_results(fit, responses_f, MODEL_TYPE)
187	
188	    return {
189	        "stratum": stratum_name,
190	        "benchmark": benchmark,
191	        "n_models": n_models,
192	        "n_items": n_items,
193	        "original_n_items": original_n_items,
194	        "subsampled": subsampled,
195	        "unique_dosages": unique_dosages.tolist(),
196	        "has_dosage_variation": has_dosage_variation,
197	        "models": [{"dirname": m["dirname"], "dosage": m["dosage"],
198	                     "scale": m.get("scale", "")} for m in models_f],
199	        "dosages": dosages_f.tolist(),
200	        "fit_time_sec": round(elapsed, 1),
201	        "diagnostics": diagnostics,
202	        "posterior_predictive": ppc,
203	        "gamma": results.get("gamma", {}),
204	        "calibrated_scores": results.get("calibrated_scores", {}),
205	    }
206	
207	
208	def dry_run(data):
209	    print("=" * 70)
210	    print("STRATIFIED IRT DRY-RUN")
211	    print("=" * 70)
212	
213	    models = data["models"]
214	    dosages = data["dosages"]
215	    unique_d, counts_d = np.unique(dosages, return_counts=True)
216	    scales = [m.get("scale", "?") for m in models]
217	    unique_s, counts_s = np.unique(scales, return_counts=True)
218	
219	    print(f"\nTotal models: {len(models)}")
220	    print(f"Dosages: {dict(zip(unique_d.tolist(), counts_d.tolist()))}")
221	    print(f"Scales:  {dict(zip(unique_s.tolist(), counts_s.tolist()))}")
222	
223	    # Scheme A
224	    print("\n" + "=" * 70)
225	    print("SCHEME A: by Dosage")
226	    print("=" * 70)
227	    for gname, target_d in DOSAGE_GROUPS.items():
228	        mf, df, bf = filter_by_dosage(models, dosages, data["benchmarks"], target_d)
229	        print(f"\n--- {gname} (dosages={target_d}, N={len(mf)}) ---")
230	        for bench in BENCHMARKS:
231	            if bench not in bf:
232	                print(f"  {bench}: NOT AVAILABLE")
233	                continue
234	            bd = bf[bench]
235	            me, de, re, ve = apply_per_benchmark_exclusions(
236	                mf, df, bd["responses"], bd["valid_mask"], bench
237	            )
238	            if not ve.all():
239	                active = ve.astype(bool)
240	                me = [m for m, v in zip(me, active) if v]
241	                re = re[active]
242	                de = de[active]
243	            nm = len(me)
244	            ni = min(bd["n_items"], MAX_ITEMS)
245	            sub = f" (subsampled from {bd['n_items']})" if bd["n_items"] > MAX_ITEMS else ""
246	            status = "OK" if nm >= 4 else ("MARGINAL" if nm >= 3 else "SKIP")
247	            print(f"  {bench}: {nm} models x {ni} items{sub} [{status}]")
248	            for m in me:
249	                print(f"    {m['dirname']} (d{m['dosage']:03d}, {m.get('scale','')})")
250	
251	    # Scheme B
252	    print("\n" + "=" * 70)
253	    print("SCHEME B: by Model Size")
254	    print("=" * 70)
255	    for gname, target_s in SCALE_GROUPS.items():
256	        mf, df, bf = filter_by_scale(models, dosages, data["benchmarks"], target_s)
257	        unique_df = np.unique(df)
258	        has_var = len(unique_df) > 1
259	        print(f"\n--- {gname} (N={len(mf)}, dosages={unique_df.tolist()}) ---")
260	        print(f"  Gamma identifiable: {'YES' if has_var else 'NO'}")
261	        for bench in BENCHMARKS:
262	            if bench not in bf:
263	                print(f"  {bench}: NOT AVAILABLE")
264	                continue
265	            bd = bf[bench]
266	            me, de, re, ve = apply_per_benchmark_exclusions(
267	                mf, df, bd["responses"], bd["valid_mask"], bench
268	            )
269	            if not ve.all():
270	                active = ve.astype(bool)
271	                me = [m for m, v in zip(me, active) if v]
272	                de = de[active]
273	                re = re[active]
274	            nm = len(me)
275	            ni = min(bd["n_items"], MAX_ITEMS)
276	            sub = f" (subsampled from {bd['n_items']})" if bd["n_items"] > MAX_ITEMS else ""
277	            ud = np.unique(de).tolist() if nm > 0 else []
278	            status = "OK" if nm >= 4 else ("MARGINAL" if nm >= 3 else "SKIP")
279	            print(f"  {bench}: {nm} models x {ni} items, dosages={ud}{sub} [{status}]")
280	            for m in me:
281	                print(f"    {m['dirname']} (d{m['dosage']:03d})")
282	
283	    # Power assessment
284	    print("\n" + "=" * 70)
285	    print("IDENTIFIABILITY NOTE")
286	    print("=" * 70)
287	    print("Scheme A: Single-dosage strata have constant exposure across models.")
288	    print("  d000: exposure=0 everywhere -> gamma unconstrained (prior only)")
289	    print("  d005/d025/d100: exposure=constant -> gamma confounded with b_j")
290	    print("  Interpretation: compare gamma posteriors across strata as")
291	    print("  'how much does the model need gamma to explain response patterns'")
292	    print("  rather than strict point-identification.")
293	    print("Scheme B: Varying dosages within each scale -> gamma IS point-identified.")
294	    print("  This is the primary analysis for dose-response signal.")
295	
296	
297	def main():
298	    parser = argparse.ArgumentParser(description="Stratified IRT analysis")
299	    parser.add_argument("--dry-run", action="store_true")
300	    parser.add_argument("--scheme", choices=["A", "B", "both"], default="both")
301	    parser.add_argument("--chains", type=int, default=4)
302	    parser.add_argument("--warmup", type=int, default=1000)
303	    parser.add_argument("--samples", type=int, default=1000)
304	    parser.add_argument("--adapt-delta", type=float, default=0.95)
305	    parser.add_argument("--max-treedepth", type=int, default=12)
306	    parser.add_argument("--seed", type=int, default=42)
307	    parser.add_argument("--parallel-chains", type=int, default=1)
308	    args = parser.parse_args()
309	
310	    logging.basicConfig(level=logging.INFO,
311	                        format="%(asctime)s [%(levelname)s] %(message)s")
312	
313	    os.environ.setdefault("TMPDIR", "/home/ubuntu/tmp_cmdstan")
314	    os.makedirs(os.environ["TMPDIR"], exist_ok=True)
315	
316	    log.info("Loading pooled eval results...")
317	    data = load_pooled_eval_results(
318	        EVAL_DIR, SCALES, benchmarks=BENCHMARKS,
319	        aligned_only=True, skip_para=True,
320	    )
321	    log.info("Loaded %d models, %d benchmarks",
322	             len(data["models"]), len(data["benchmarks"]))
323	
324	    if args.dry_run:
325	        dry_run(data)
326	        return
327	
328	    args_dict = {
329	        "chains": args.chains,
330	        "warmup": args.warmup,
331	        "samples": args.samples,
332	        "adapt_delta": args.adapt_delta,
333	        "max_treedepth": args.max_treedepth,
334	        "seed": args.seed,
335	        "parallel_chains": args.parallel_chains,
336	    }
337	
338	    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
339	    all_results = {"scheme_A": {}, "scheme_B": {}}
340	    t0_total = time.time()
341	
342	    # Scheme A
343	    if args.scheme in ("A", "both"):
344	        log.info("=" * 60)
345	        log.info("SCHEME A: by Dosage")
346	        log.info("=" * 60)
347	
348	        for gname, target_d in DOSAGE_GROUPS.items():
349	            mf, df, bf = filter_by_dosage(
350	                data["models"], data["dosages"], data["benchmarks"], target_d
351	            )
352	            log.info("--- %s: %d models ---", gname, len(mf))
353	            group_results = {}
354	
355	            for bench in BENCHMARKS:
356	                if bench not in bf:
357	                    continue
358	                result = run_stratum_fit(
359	                    f"A_{gname}", mf, df, bf[bench], bench, args_dict
360	                )
361	                if result:
362	                    group_results[bench] = result
363	                    g = result["gamma"]
364	                    d = result["diagnostics"]
365	                    log.info("[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d",
366	                             gname, bench, g["mean"], g["q025"], g["q975"],
367	                             d.get("max_rhat", 0), d.get("divergent_count", 0))
368	
369	            all_results["scheme_A"][gname] = group_results
370	            gdir = OUTPUT_DIR / "scheme_A" / gname
371	            gdir.mkdir(parents=True, exist_ok=True)
372	            for bench, result in group_results.items():
373	                with open(gdir / f"{bench}_results.json", "w") as f:
374	                    json.dump(result, f, indent=2)
375	
376	    # Scheme B
377	    if args.scheme in ("B", "both"):
378	        log.info("=" * 60)
379	        log.info("SCHEME B: by Model Size")
380	        log.info("=" * 60)
381	
382	        for gname, target_s in SCALE_GROUPS.items():
383	            mf, df, bf = filter_by_scale(
384	                data["models"], data["dosages"], data["benchmarks"], target_s
385	            )
386	            log.info("--- %s: %d models ---", gname, len(mf))
387	            group_results = {}
388	
389	            for bench in BENCHMARKS:
390	                if bench not in bf:
391	                    continue
392	                result = run_stratum_fit(
393	                    f"B_{gname}", mf, df, bf[bench], bench, args_dict
394	                )
395	                if result:
396	                    group_results[bench] = result
397	                    g = result["gamma"]
398	                    d = result["diagnostics"]
399	                    log.info("[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d",
400	                             gname, bench, g["mean"], g["q025"], g["q975"],
401	                             d.get("max_rhat", 0), d.get("divergent_count", 0))
402	
403	            all_results["scheme_B"][gname] = group_results
404	            gdir = OUTPUT_DIR / "scheme_B" / gname
405	            gdir.mkdir(parents=True, exist_ok=True)
406	            for bench, result in group_results.items():
407	                with open(gdir / f"{bench}_results.json", "w") as f:
408	                    json.dump(result, f, indent=2)
409	
410	    elapsed_total = time.time() - t0_total
411	
412	    with open(OUTPUT_DIR / "stratified_irt_results.json", "w") as f:
413	        json.dump(all_results, f, indent=2)
414	
415	    # Summary
416	    print("\n" + "=" * 70)
417	    print("STRATIFIED IRT RESULTS")
418	    print("=" * 70)
419	    print(f"Total time: {elapsed_total:.0f}s")
420	
421	    for scheme_key, scheme_label in [("scheme_A", "SCHEME A (by dosage)"),
422	                                      ("scheme_B", "SCHEME B (by model size)")]:
423	        if not all_results[scheme_key]:
424	            continue
425	        print(f"\n{scheme_label}:")
426	        for gname, gresults in all_results[scheme_key].items():
427	            print(f"  {gname}:")
428	            for bench, r in gresults.items():
429	                g = r["gamma"]
430	                var = "" if r.get("has_dosage_variation") else " [CONST EXP]"
431	                print(f"    {bench}: gamma={g['mean']:.4f} "
432	                      f"[{g['q025']:.4f}, {g['q975']:.4f}] "
433	                      f"N={r['n_models']}{var}")
434	
435	    print(f"\nSaved to {OUTPUT_DIR}")
436	
437	
438	if __name__ == "__main__":
439	    main()
440	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "39c33dbc-7176-4e66-8c1d-073f509ebffa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_stratified_irt.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nStratified IRT analysis: dose-response and model-size strata.\n\nScheme A: by dosage (d000/d005/d025/d100) — checks dose-response in gamma\nScheme B: by model size (0.5B/1.5B/3B) — checks if gamma varies by capacity\n\nSame exclusion rules as pooled analysis (D044/D045/D046/D047/D018).\nOracle dosage as exposure (dosage/100 global normalization). 2PL+gamma model.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\n\nsys.path.insert(0, \"/root/contamcal-irt-calibration/exp006\")\nfrom run_irt_calibration import (\n    load_pooled_eval_results,\n    prepare_stan_data,\n    fit_stan_model,\n    check_convergence,\n    posterior_predictive_check,\n    extract_results,\n    STAN_MODELS,\n)\n\nlog = logging.getLogger(__name__)\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\", \"humaneval\"]\nSCALES = [\"0.5B\", \"1.5B\", \"3B\"]\nMODEL_TYPE = \"2pl_gamma\"\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\n\nEVAL_DIR = \"/root/autodl-tmp/exp001/eval_results\"\nOUTPUT_DIR = Path(\"/root/autodl-tmp/exp006/results_stratified_irt\")\n\nMAX_ITEMS = 2000\n\nDOSAGE_GROUPS = {\n    \"d000\": [0],\n    \"d005\": [5],\n    \"d025\": [25],\n    \"d100\": [100],\n}\n\nSCALE_GROUPS = {\n    \"scale_0.5B\": [\"0.5B\"],\n    \"scale_1.5B\": [\"1.5B\"],\n    \"scale_3B\": [\"3B\"],\n}\n\n\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\n    keep = np.ones(len(models), dtype=bool)\n    reasons = []\n\n    for i, m in enumerate(models):\n        dirname = m.get(\"dirname\", \"\")\n        scale = m.get(\"scale\", \"\")\n        dosage = m.get(\"dosage\", 0)\n\n        if \"base_pretrained\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D046/D047: {dirname}\")\n            continue\n        if \"DEPRECATED\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D018: {dirname}\")\n            continue\n        if \"0.5B\" in scale and benchmark in (\"mmlu\", \"arc_challenge\"):\n            keep[i] = False\n            reasons.append(f\"  D045: {dirname}\")\n            continue\n        if benchmark == \"gsm8k\" and dosage == 0:\n            keep[i] = False\n            reasons.append(f\"  D044: {dirname}\")\n            continue\n\n    if reasons:\n        log.info(\"Excluded from %s (%d):\", benchmark, len(reasons))\n        for r in reasons[:5]:\n            log.info(r)\n        if len(reasons) > 5:\n            log.info(\"  ... +%d more\", len(reasons) - 5)\n\n    return (\n        [m for m, k in zip(models, keep) if k],\n        dosages[keep],\n        responses[keep],\n        valid_mask[keep],\n    )\n\n\ndef build_oracle_exposure_global(dosages, n_items):\n    \"\"\"Oracle exposure with global normalization: dosage/100.\"\"\"\n    fracs = dosages.astype(float) / 100.0\n    return np.outer(fracs, np.ones(n_items))\n\n\ndef filter_by_dosage(models, dosages, benchmarks_data, target_dosages):\n    keep = np.array([d in target_dosages for d in dosages])\n    filt_models = [m for m, k in zip(models, keep) if k]\n    filt_dosages = dosages[keep]\n    filt_bench = {}\n    for bench, bd in benchmarks_data.items():\n        filt_bench[bench] = {\n            \"responses\": bd[\"responses\"][keep],\n            \"n_items\": bd[\"n_items\"],\n            \"valid_mask\": bd[\"valid_mask\"][keep],\n        }\n    return filt_models, filt_dosages, filt_bench\n\n\ndef filter_by_scale(models, dosages, benchmarks_data, target_scales):\n    keep = np.array([m.get(\"scale\", \"\") in target_scales for m in models])\n    filt_models = [m for m, k in zip(models, keep) if k]\n    filt_dosages = dosages[keep]\n    filt_bench = {}\n    for bench, bd in benchmarks_data.items():\n        filt_bench[bench] = {\n            \"responses\": bd[\"responses\"][keep],\n            \"n_items\": bd[\"n_items\"],\n            \"valid_mask\": bd[\"valid_mask\"][keep],\n        }\n    return filt_models, filt_dosages, filt_bench\n\n\ndef run_stratum_fit(stratum_name, models, dosages, bench_data, benchmark, args_dict):\n    responses = bench_data[\"responses\"]\n    valid_mask = bench_data[\"valid_mask\"]\n    n_items = bench_data[\"n_items\"]\n\n    models_f, dosages_f, responses_f, valid_f = apply_per_benchmark_exclusions(\n        models, dosages, responses, valid_mask, benchmark\n    )\n\n    if not valid_f.all():\n        active = valid_f.astype(bool)\n        models_f = [m for m, v in zip(models_f, active) if v]\n        dosages_f = dosages_f[active]\n        responses_f = responses_f[active]\n\n    n_models = len(models_f)\n    original_n_items = n_items\n    subsampled = False\n    if n_items > MAX_ITEMS:\n        np.random.seed(42)\n        indices = np.random.choice(n_items, MAX_ITEMS, replace=False)\n        indices.sort()\n        responses_f = responses_f[:, indices]\n        n_items = MAX_ITEMS\n        subsampled = True\n\n    if n_models < 3:\n        log.warning(\"[%s/%s] Too few models (%d), skipping\", stratum_name, benchmark, n_models)\n        return None\n\n    unique_dosages = np.unique(dosages_f)\n    has_dosage_variation = len(unique_dosages) > 1\n\n    exposure = build_oracle_exposure_global(dosages_f, n_items)\n\n    log.info(\"[%s/%s] %d models x %d items, dosages=%s\",\n             stratum_name, benchmark, n_models, n_items, unique_dosages.tolist())\n\n    stan_data = prepare_stan_data(responses_f, exposure, MODEL_TYPE)\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, responses_f)\n    results = extract_results(fit, responses_f, MODEL_TYPE)\n\n    return {\n        \"stratum\": stratum_name,\n        \"benchmark\": benchmark,\n        \"n_models\": n_models,\n        \"n_items\": n_items,\n        \"original_n_items\": original_n_items,\n        \"subsampled\": subsampled,\n        \"unique_dosages\": unique_dosages.tolist(),\n        \"has_dosage_variation\": has_dosage_variation,\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in models_f],\n        \"dosages\": dosages_f.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n    }\n\n\ndef dry_run(data):\n    print(\"=\" * 70)\n    print(\"STRATIFIED IRT DRY-RUN\")\n    print(\"=\" * 70)\n\n    models = data[\"models\"]\n    dosages = data[\"dosages\"]\n    unique_d, counts_d = np.unique(dosages, return_counts=True)\n    scales = [m.get(\"scale\", \"?\") for m in models]\n    unique_s, counts_s = np.unique(scales, return_counts=True)\n\n    print(f\"\\nTotal models: {len(models)}\")\n    print(f\"Dosages: {dict(zip(unique_d.tolist(), counts_d.tolist()))}\")\n    print(f\"Scales:  {dict(zip(unique_s.tolist(), counts_s.tolist()))}\")\n\n    # Scheme A\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SCHEME A: by Dosage\")\n    print(\"=\" * 70)\n    for gname, target_d in DOSAGE_GROUPS.items():\n        mf, df, bf = filter_by_dosage(models, dosages, data[\"benchmarks\"], target_d)\n        print(f\"\\n--- {gname} (dosages={target_d}, N={len(mf)}) ---\")\n        for bench in BENCHMARKS:\n            if bench not in bf:\n                print(f\"  {bench}: NOT AVAILABLE\")\n                continue\n            bd = bf[bench]\n            me, de, re, ve = apply_per_benchmark_exclusions(\n                mf, df, bd[\"responses\"], bd[\"valid_mask\"], bench\n            )\n            if not ve.all():\n                active = ve.astype(bool)\n                me = [m for m, v in zip(me, active) if v]\n                re = re[active]\n                de = de[active]\n            nm = len(me)\n            ni = min(bd[\"n_items\"], MAX_ITEMS)\n            sub = f\" (subsampled from {bd['n_items']})\" if bd[\"n_items\"] > MAX_ITEMS else \"\"\n            status = \"OK\" if nm >= 4 else (\"MARGINAL\" if nm >= 3 else \"SKIP\")\n            print(f\"  {bench}: {nm} models x {ni} items{sub} [{status}]\")\n            for m in me:\n                print(f\"    {m['dirname']} (d{m['dosage']:03d}, {m.get('scale','')})\")\n\n    # Scheme B\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SCHEME B: by Model Size\")\n    print(\"=\" * 70)\n    for gname, target_s in SCALE_GROUPS.items():\n        mf, df, bf = filter_by_scale(models, dosages, data[\"benchmarks\"], target_s)\n        unique_df = np.unique(df)\n        has_var = len(unique_df) > 1\n        print(f\"\\n--- {gname} (N={len(mf)}, dosages={unique_df.tolist()}) ---\")\n        print(f\"  Gamma identifiable: {'YES' if has_var else 'NO'}\")\n        for bench in BENCHMARKS:\n            if bench not in bf:\n                print(f\"  {bench}: NOT AVAILABLE\")\n                continue\n            bd = bf[bench]\n            me, de, re, ve = apply_per_benchmark_exclusions(\n                mf, df, bd[\"responses\"], bd[\"valid_mask\"], bench\n            )\n            if not ve.all():\n                active = ve.astype(bool)\n                me = [m for m, v in zip(me, active) if v]\n                de = de[active]\n                re = re[active]\n            nm = len(me)\n            ni = min(bd[\"n_items\"], MAX_ITEMS)\n            sub = f\" (subsampled from {bd['n_items']})\" if bd[\"n_items\"] > MAX_ITEMS else \"\"\n            ud = np.unique(de).tolist() if nm > 0 else []\n            status = \"OK\" if nm >= 4 else (\"MARGINAL\" if nm >= 3 else \"SKIP\")\n            print(f\"  {bench}: {nm} models x {ni} items, dosages={ud}{sub} [{status}]\")\n            for m in me:\n                print(f\"    {m['dirname']} (d{m['dosage']:03d})\")\n\n    # Power assessment\n    print(\"\\n\" + \"=\" * 70)\n    print(\"IDENTIFIABILITY NOTE\")\n    print(\"=\" * 70)\n    print(\"Scheme A: Single-dosage strata have constant exposure across models.\")\n    print(\"  d000: exposure=0 everywhere -> gamma unconstrained (prior only)\")\n    print(\"  d005/d025/d100: exposure=constant -> gamma confounded with b_j\")\n    print(\"  Interpretation: compare gamma posteriors across strata as\")\n    print(\"  'how much does the model need gamma to explain response patterns'\")\n    print(\"  rather than strict point-identification.\")\n    print(\"Scheme B: Varying dosages within each scale -> gamma IS point-identified.\")\n    print(\"  This is the primary analysis for dose-response signal.\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Stratified IRT analysis\")\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--scheme\", choices=[\"A\", \"B\", \"both\"], default=\"both\")\n    parser.add_argument(\"--chains\", type=int, default=4)\n    parser.add_argument(\"--warmup\", type=int, default=1000)\n    parser.add_argument(\"--samples\", type=int, default=1000)\n    parser.add_argument(\"--adapt-delta\", type=float, default=0.95)\n    parser.add_argument(\"--max-treedepth\", type=int, default=12)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--parallel-chains\", type=int, default=1)\n    args = parser.parse_args()\n\n    logging.basicConfig(level=logging.INFO,\n                        format=\"%(asctime)s [%(levelname)s] %(message)s\")\n\n    os.environ.setdefault(\"TMPDIR\", \"/home/ubuntu/tmp_cmdstan\")\n    os.makedirs(os.environ[\"TMPDIR\"], exist_ok=True)\n\n    log.info(\"Loading pooled eval results...\")\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS,\n        aligned_only=True, skip_para=True,\n    )\n    log.info(\"Loaded %d models, %d benchmarks\",\n             len(data[\"models\"]), len(data[\"benchmarks\"]))\n\n    if args.dry_run:\n        dry_run(data)\n        return\n\n    args_dict = {\n        \"chains\": args.chains,\n        \"warmup\": args.warmup,\n        \"samples\": args.samples,\n        \"adapt_delta\": args.adapt_delta,\n        \"max_treedepth\": args.max_treedepth,\n        \"seed\": args.seed,\n        \"parallel_chains\": args.parallel_chains,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    all_results = {\"scheme_A\": {}, \"scheme_B\": {}}\n    t0_total = time.time()\n\n    # Scheme A\n    if args.scheme in (\"A\", \"both\"):\n        log.info(\"=\" * 60)\n        log.info(\"SCHEME A: by Dosage\")\n        log.info(\"=\" * 60)\n\n        for gname, target_d in DOSAGE_GROUPS.items():\n            mf, df, bf = filter_by_dosage(\n                data[\"models\"], data[\"dosages\"], data[\"benchmarks\"], target_d\n            )\n            log.info(\"--- %s: %d models ---\", gname, len(mf))\n            group_results = {}\n\n            for bench in BENCHMARKS:\n                if bench not in bf:\n                    continue\n                result = run_stratum_fit(\n                    f\"A_{gname}\", mf, df, bf[bench], bench, args_dict\n                )\n                if result:\n                    group_results[bench] = result\n                    g = result[\"gamma\"]\n                    d = result[\"diagnostics\"]\n                    log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d\",\n                             gname, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                             d.get(\"max_rhat\", 0), d.get(\"divergent_count\", 0))\n\n            all_results[\"scheme_A\"][gname] = group_results\n            gdir = OUTPUT_DIR / \"scheme_A\" / gname\n            gdir.mkdir(parents=True, exist_ok=True)\n            for bench, result in group_results.items():\n                with open(gdir / f\"{bench}_results.json\", \"w\") as f:\n                    json.dump(result, f, indent=2)\n\n    # Scheme B\n    if args.scheme in (\"B\", \"both\"):\n        log.info(\"=\" * 60)\n        log.info(\"SCHEME B: by Model Size\")\n        log.info(\"=\" * 60)\n\n        for gname, target_s in SCALE_GROUPS.items():\n            mf, df, bf = filter_by_scale(\n                data[\"models\"], data[\"dosages\"], data[\"benchmarks\"], target_s\n            )\n            log.info(\"--- %s: %d models ---\", gname, len(mf))\n            group_results = {}\n\n            for bench in BENCHMARKS:\n                if bench not in bf:\n                    continue\n                result = run_stratum_fit(\n                    f\"B_{gname}\", mf, df, bf[bench], bench, args_dict\n                )\n                if result:\n                    group_results[bench] = result\n                    g = result[\"gamma\"]\n                    d = result[\"diagnostics\"]\n                    log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d\",\n                             gname, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                             d.get(\"max_rhat\", 0), d.get(\"divergent_count\", 0))\n\n            all_results[\"scheme_B\"][gname] = group_results\n            gdir = OUTPUT_DIR / \"scheme_B\" / gname\n            gdir.mkdir(parents=True, exist_ok=True)\n            for bench, result in group_results.items():\n                with open(gdir / f\"{bench}_results.json\", \"w\") as f:\n                    json.dump(result, f, indent=2)\n\n    elapsed_total = time.time() - t0_total\n\n    with open(OUTPUT_DIR / \"stratified_irt_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Summary\n    print(\"\\n\" + \"=\" * 70)\n    print(\"STRATIFIED IRT RESULTS\")\n    print(\"=\" * 70)\n    print(f\"Total time: {elapsed_total:.0f}s\")\n\n    for scheme_key, scheme_label in [(\"scheme_A\", \"SCHEME A (by dosage)\"),\n                                      (\"scheme_B\", \"SCHEME B (by model size)\")]:\n        if not all_results[scheme_key]:\n            continue\n        print(f\"\\n{scheme_label}:\")\n        for gname, gresults in all_results[scheme_key].items():\n            print(f\"  {gname}:\")\n            for bench, r in gresults.items():\n                g = r[\"gamma\"]\n                var = \"\" if r.get(\"has_dosage_variation\") else \" [CONST EXP]\"\n                print(f\"    {bench}: gamma={g['mean']:.4f} \"\n                      f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                      f\"N={r['n_models']}{var}\")\n\n    print(f\"\\nSaved to {OUTPUT_DIR}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 440,
      "startLine": 1,
      "totalLines": 440
    }
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_01M1DZ5T2nHBjhzvZgJq7rbX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/run_irt_stan.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "d579db9b-a88c-4484-b3ad-4767dbe7182b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nZhofBNDPSTvM5mecper2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2440,
      "cache_read_input_tokens": 24911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2440
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

_source line 67 · 2026-05-16T05:29:41.856Z_

<details><summary>↩ Tool result · `toolu_01M1DZ5T2nHBjhzvZgJq7rbX`</summary>

```text
1	# CmdStanPy Bayesian IRT calibration pipeline (replaces PyTorch MLE version)
2	# 4PL+γ model: P(y=1) = c + (d-c) * logit^{-1}(a*(theta - b) + gamma * exposure)
3	
4	import argparse
5	import json
6	import logging
7	import os
8	import re
9	import sys
10	import time
11	from pathlib import Path
12	
13	import numpy as np
14	import cmdstanpy
15	
16	logger = logging.getLogger(__name__)
17	
18	DOSAGE_PATTERN = re.compile(r"_d(\d+)_s(\d+)(_para)?$")
19	
20	
21	def parse_model_dir_name(dirname: str) -> dict | None:
22	    m = DOSAGE_PATTERN.search(dirname)
23	    if not m:
24	        return None
25	    dosage = int(m.group(1))
26	    seed = int(m.group(2))
27	    is_para = m.group(3) is not None
28	    model_name = dirname[: m.start()]
29	    return {
30	        "dirname": dirname,
31	        "model_name": model_name,
32	        "dosage": dosage,
33	        "seed": seed,
34	        "is_para": is_para,
35	    }
36	
37	
38	def load_eval_results(eval_dir: str, benchmarks: list[str] | None = None,
39	                      skip_para: bool = True) -> dict:
40	    eval_path = Path(eval_dir)
41	    model_dirs = sorted([
42	        d for d in eval_path.iterdir()
43	        if d.is_dir() and (d / "eval_results.json").exists()
44	    ])
45	
46	    models = []
47	    for d in model_dirs:
48	        info = parse_model_dir_name(d.name)
49	        if info is None:
50	            logger.warning("Skipping unrecognized directory: %s", d.name)
51	            continue
52	        if skip_para and info["is_para"]:
53	            continue
54	        info["path"] = str(d)
55	        models.append(info)
56	
57	    if not models:
58	        raise ValueError(f"No valid eval results found in {eval_dir}")
59	
60	    logger.info("Found %d model evaluations", len(models))
61	
62	    with open(Path(models[0]["path"]) / "eval_results.json") as f:
63	        sample = json.load(f)
64	    available_benchmarks = list(sample["benchmarks"].keys())
65	
66	    if benchmarks:
67	        benchmarks = [b for b in benchmarks if b in available_benchmarks]
68	    else:
69	        benchmarks = available_benchmarks
70	
71	    logger.info("Benchmarks: %s", benchmarks)
72	
73	    result = {"models": models, "benchmarks": {}, "dosages": np.array([m["dosage"] for m in models])}
74	
75	    for bench in benchmarks:
76	        responses = []
77	        for m in models:
78	            results_file = Path(m["path"]) / "eval_results.json"
79	            with open(results_file) as f:
80	                data = json.load(f)
81	
82	            if bench not in data["benchmarks"]:
83	                logger.warning("Benchmark %s missing for %s", bench, m["dirname"])
84	                responses.append(None)
85	                continue
86	
87	            per_item = data["benchmarks"][bench]["per_item"]
88	            correct = [int(item["correct"]) for item in per_item]
89	            responses.append(correct)
90	
91	        lengths = [len(r) for r in responses if r is not None]
92	        if not lengths:
93	            continue
94	
95	        n_items = min(lengths)
96	        matrix = np.zeros((len(models), n_items), dtype=int)
97	        valid_mask = np.ones(len(models), dtype=bool)
98	        for j, r in enumerate(responses):
99	            if r is None:
100	                valid_mask[j] = False
101	            else:
102	                matrix[j, :n_items] = r[:n_items]
103	
104	        result["benchmarks"][bench] = {
105	            "responses": matrix,
106	            "n_items": n_items,
107	            "valid_mask": valid_mask,
108	        }
109	
110	    return result
111	
112	
113	def filter_low_variance_items(bench_data: dict, min_variance: float = 0.01) -> dict:
114	    """Remove items with near-zero response variance (uninformative for IRT).
115	
116	    Items where all respondents answer identically provide no discrimination
117	    information. IRT parameters (especially discrimination 'a') cannot be
118	    estimated for such items.
119	    """
120	    matrix = bench_data["responses"]
121	    valid = bench_data["valid_mask"]
122	    responses_valid = matrix[valid]
123	
124	    item_var = responses_valid.var(axis=0)
125	    keep_mask = item_var >= min_variance
126	    n_excluded = int((~keep_mask).sum())
127	
128	    if n_excluded > 0:
129	        excluded_indices = np.where(~keep_mask)[0].tolist()
130	        logger.info(
131	            "Filtered %d/%d items with variance < %.3f (indices: %s...)",
132	            n_excluded, len(keep_mask), min_variance,
133	            excluded_indices[:10],
134	        )
135	        matrix = matrix[:, keep_mask]
136	        return {
137	            "responses": matrix,
138	            "n_items": int(keep_mask.sum()),
139	            "valid_mask": bench_data["valid_mask"],
140	            "excluded_item_indices": excluded_indices,
141	            "n_excluded": n_excluded,
142	            "item_keep_mask": keep_mask,
143	        }
144	
145	    n_items = bench_data["n_items"]
146	    return {
147	        **bench_data,
148	        "excluded_item_indices": [],
149	        "n_excluded": 0,
150	        "item_keep_mask": np.ones(n_items, dtype=bool),
151	    }
152	
153	
154	def load_exposure_scores(exposure_file: str | None, benchmarks: dict) -> dict:
155	    if exposure_file and os.path.exists(exposure_file):
156	        with open(exposure_file) as f:
157	            raw = json.load(f)
158	        exposure = {}
159	        for bench in benchmarks:
160	            if bench in raw:
161	                exposure[bench] = np.array(raw[bench], dtype=float)
162	            else:
163	                n_items = benchmarks[bench]["n_items"]
164	                exposure[bench] = np.ones(n_items)
165	        return exposure
166	
167	    exposure = {}
168	    for bench, bdata in benchmarks.items():
169	        exposure[bench] = np.ones(bdata["n_items"])
170	    return exposure
171	
172	
173	def build_exposure_matrix(dosages: np.ndarray, tau: np.ndarray) -> np.ndarray:
174	    """Build exposure matrix: exposure[i,j] = dosage[i] * tau[j] / max_dosage."""
175	    max_d = dosages.max() if dosages.max() > 0 else 1.0
176	    dosage_norm = dosages / max_d
177	    return np.outer(dosage_norm, tau)
178	
179	
180	def generate_synthetic_data(n_models=50, n_items=100, gamma_true=0.5,
181	                            exposure_rate=0.3, seed=42):
182	    """Generate synthetic data for sanity checking."""
183	    rng = np.random.default_rng(seed)
184	    theta = rng.standard_normal(n_models)
185	    a = rng.lognormal(0, 0.5, n_items)
186	    b = rng.standard_normal(n_items)
187	    c = rng.beta(5, 20, n_items)
188	    d = rng.beta(20, 5, n_items)
189	    exposure = rng.binomial(1, exposure_rate, (n_models, n_items)).astype(float)
190	
191	    from scipy.special import expit
192	    eta = np.outer(np.ones(n_models), a) * (theta[:, None] - b[None, :]) + gamma_true * exposure
193	    prob = c[None, :] + (d[None, :] - c[None, :]) * expit(eta)
194	    y = rng.binomial(1, prob)
195	
196	    return {
197	        "y": y,
198	        "exposure": exposure,
199	        "true_params": {
200	            "theta": theta.tolist(),
201	            "a": a.tolist(),
202	            "b": b.tolist(),
203	            "c": c.tolist(),
204	            "d": d.tolist(),
205	            "gamma": gamma_true,
206	        },
207	        "N_models": n_models,
208	        "N_items": n_items,
209	    }
210	
211	
212	def run_stan_fit(stan_file: str, stan_data: dict, chains: int = 4,
213	                 iter_sampling: int = 1000, iter_warmup: int = 500,
214	                 adapt_delta: float = 0.95, max_treedepth: int = 12,
215	                 seed: int = 42) -> cmdstanpy.CmdStanMCMC:
216	    model = cmdstanpy.CmdStanModel(stan_file=stan_file)
217	    fit = model.sample(
218	        data=stan_data,
219	        chains=chains,
220	        iter_warmup=iter_warmup,
221	        iter_sampling=iter_sampling,
222	        seed=seed,
223	        adapt_delta=adapt_delta,
224	        max_treedepth=max_treedepth,
225	        parallel_chains=min(chains, 4),
226	        show_progress=True,
227	    )
228	    return fit
229	
230	
231	def extract_diagnostics(fit: cmdstanpy.CmdStanMCMC) -> dict:
232	    summary = fit.summary()
233	
234	    diag_text = fit.diagnose()
235	    divergent = 0
236	    for line in diag_text.split('\n'):
237	        if 'divergent' in line.lower():
238	            parts = [w for w in line.split() if w.isdigit()]
239	            if parts:
240	                divergent = int(parts[0])
241	                break
242	
243	    total_draws = fit.chains * fit.num_draws_sampling
244	    divergent_pct = 100.0 * divergent / total_draws if total_draws > 0 else 0.0
245	
246	    max_rhat = float(summary['R_hat'].max()) if 'R_hat' in summary.columns else None
247	    if 'ESS_bulk' in summary.columns:
248	        min_ess_bulk = float(summary['ESS_bulk'].min())
249	    elif 'N_Eff' in summary.columns:
250	        min_ess_bulk = float(summary['N_Eff'].min())
251	    else:
252	        min_ess_bulk = None
253	
254	    return {
255	        "divergent_count": divergent,
256	        "divergent_pct": round(divergent_pct, 4),
257	        "max_rhat": round(max_rhat, 5) if max_rhat else None,
258	        "min_ess_bulk": round(min_ess_bulk, 1) if min_ess_bulk else None,
259	        "total_draws": total_draws,
260	        "chains": fit.chains,
261	    }
262	
263	
264	def extract_item_parameters(fit: cmdstanpy.CmdStanMCMC, n_items: int) -> dict:
265	    a_draws = fit.stan_variable("a")  # shape: (n_draws, n_items)
266	    b_draws = fit.stan_variable("b")
267	    c_draws = fit.stan_variable("c")
268	    d_draws = fit.stan_variable("d")
269	
270	    items = []
271	    for j in range(n_items):
272	        items.append({
273	            "item_idx": j,
274	            "a_mean": round(float(np.mean(a_draws[:, j])), 4),
275	            "a_sd": round(float(np.std(a_draws[:, j])), 4),
276	            "b_mean": round(float(np.mean(b_draws[:, j])), 4),
277	            "b_sd": round(float(np.std(b_draws[:, j])), 4),
278	            "c_mean": round(float(np.mean(c_draws[:, j])), 4),
279	            "c_sd": round(float(np.std(c_draws[:, j])), 4),
280	            "d_mean": round(float(np.mean(d_draws[:, j])), 4),
281	            "d_sd": round(float(np.std(d_draws[:, j])), 4),
282	        })
283	
284	    return {"items": items, "n_items": n_items}
285	
286	
287	def extract_model_parameters(fit: cmdstanpy.CmdStanMCMC, n_models: int,
288	                             model_info: list[dict] | None = None) -> dict:
289	    theta_draws = fit.stan_variable("theta")  # (n_draws, n_models)
290	    gamma_draws = fit.stan_variable("gamma")  # (n_draws,) scalar
291	
292	    gamma_mean = float(np.mean(gamma_draws))
293	    gamma_sd = float(np.std(gamma_draws))
294	    gamma_q025 = float(np.percentile(gamma_draws, 2.5))
295	    gamma_q975 = float(np.percentile(gamma_draws, 97.5))
296	
297	    models = []
298	    for i in range(n_models):
299	        theta_i = theta_draws[:, i]
300	        entry = {
301	            "model_idx": i,
302	            "theta_mean": round(float(np.mean(theta_i)), 4),
303	            "theta_sd": round(float(np.std(theta_i)), 4),
304	            "theta_q025": round(float(np.percentile(theta_i, 2.5)), 4),
305	            "theta_q975": round(float(np.percentile(theta_i, 97.5)), 4),
306	        }
307	        if model_info and i < len(model_info):
308	            entry["dirname"] = model_info[i]["dirname"]
309	            entry["model_name"] = model_info[i]["model_name"]
310	            entry["dosage"] = model_info[i]["dosage"]
311	        models.append(entry)
312	
313	    return {
314	        "gamma": {
315	            "mean": round(gamma_mean, 4),
316	            "sd": round(gamma_sd, 4),
317	            "q025": round(gamma_q025, 4),
318	            "q975": round(gamma_q975, 4),
319	            "ci_excludes_zero": bool(gamma_q025 > 0 or gamma_q975 < 0),
320	        },
321	        "models": models,
322	    }
323	
324	
325	def extract_calibrated_scores(fit: cmdstanpy.CmdStanMCMC, n_models: int,
326	                              responses: np.ndarray) -> dict:
327	    cal_draws = fit.stan_variable("calibrated_score")  # (n_draws, n_models)
328	
329	    raw_scores = responses.mean(axis=1).tolist()
330	    entries = []
331	    for i in range(n_models):
332	        cal_i = cal_draws[:, i]
333	        entries.append({
334	            "model_idx": i,
335	            "raw_accuracy": round(raw_scores[i], 4),
336	            "calibrated_mean": round(float(np.mean(cal_i)), 4),
337	            "calibrated_sd": round(float(np.std(cal_i)), 4),
338	            "calibrated_q025": round(float(np.percentile(cal_i, 2.5)), 4),
339	            "calibrated_q975": round(float(np.percentile(cal_i, 97.5)), 4),
340	            "adjustment": round(float(np.mean(cal_i)) - raw_scores[i], 4),
341	        })
342	
343	    return {"scores": entries}
344	
345	
346	def run_synthetic_validation(stan_file: str, output_dir: Path, args):
347	    logger.info("Generating synthetic data...")
348	    synth = generate_synthetic_data()
349	    y = synth["y"]
350	    exposure = synth["exposure"]
351	    true = synth["true_params"]
352	
353	    stan_data = {
354	        "N_models": synth["N_models"],
355	        "N_items": synth["N_items"],
356	        "y": y.tolist(),
357	        "exposure": exposure.tolist(),
358	    }
359	
360	    logger.info("Fitting Stan model (synthetic, %d models x %d items)...",
361	                synth["N_models"], synth["N_items"])
362	    t0 = time.time()
363	    fit = run_stan_fit(
364	        stan_file, stan_data,
365	        chains=args.chains,
366	        iter_sampling=args.iter_sampling,
367	        adapt_delta=args.adapt_delta,
368	        max_treedepth=args.max_treedepth,
369	        seed=args.seed,
370	    )
371	    elapsed = time.time() - t0
372	    logger.info("Sampling done in %.1fs", elapsed)
373	
374	    # Recovery metrics
375	    theta_draws = fit.stan_variable("theta")
376	    theta_post = np.mean(theta_draws, axis=0)
377	    theta_corr = float(np.corrcoef(theta_post, true["theta"])[0, 1])
378	
379	    gamma_draws = fit.stan_variable("gamma")
380	    gamma_mean = float(np.mean(gamma_draws))
381	    gamma_sd = float(np.std(gamma_draws))
382	
383	    a_draws = fit.stan_variable("a")
384	    a_post = np.mean(a_draws, axis=0)
385	    a_corr = float(np.corrcoef(a_post, true["a"])[0, 1])
386	
387	    b_draws = fit.stan_variable("b")
388	    b_post = np.mean(b_draws, axis=0)
389	    b_corr = float(np.corrcoef(b_post, true["b"])[0, 1])
390	
391	    diag = extract_diagnostics(fit)
392	
393	    result = {
394	        "mode": "synthetic_validation",
395	        "true_gamma": true["gamma"],
396	        "estimated_gamma_mean": round(gamma_mean, 4),
397	        "estimated_gamma_sd": round(gamma_sd, 4),
398	        "gamma_bias": round(gamma_mean - true["gamma"], 4),
399	        "gamma_rel_bias": round(abs(gamma_mean - true["gamma"]) / abs(true["gamma"]), 4),
400	        "theta_corr": round(theta_corr, 4),
401	        "a_corr": round(a_corr, 4),
402	        "b_corr": round(b_corr, 4),
403	        "diagnostics": diag,
404	        "elapsed_sec": round(elapsed, 1),
405	    }
406	
407	    logger.info("Recovery: gamma=%.4f (true=%.4f), theta_corr=%.4f, a_corr=%.4f, b_corr=%.4f",
408	                gamma_mean, true["gamma"], theta_corr, a_corr, b_corr)
409	    logger.info("Diagnostics: R-hat=%.4f, divergent=%d (%.2f%%)",
410	                diag["max_rhat"] or 0, diag["divergent_count"], diag["divergent_pct"])
411	
412	    output_dir.mkdir(parents=True, exist_ok=True)
413	    out_file = output_dir / "synthetic_validation.json"
414	    with open(out_file, "w") as f:
415	        json.dump(result, f, indent=2)
416	    logger.info("Saved: %s", out_file)
417	    return result
418	
419	
420	def run_real_data(eval_dir: str, stan_file: str, output_dir: Path,
421	                  exposure_file: str | None, benchmarks_filter: list[str] | None,
422	                  args):
423	    data = load_eval_results(eval_dir, benchmarks_filter)
424	    exposure_scores = load_exposure_scores(exposure_file, data["benchmarks"])
425	    dosages = data["dosages"]
426	
427	    output_dir.mkdir(parents=True, exist_ok=True)
428	
429	    all_results = {
430	        "mode": "real",
431	        "eval_dir": eval_dir,
432	        "stan_model": stan_file,
433	        "models": [
434	            {"dirname": m["dirname"], "model_name": m["model_name"],
435	             "dosage": m["dosage"], "seed": m["seed"]}
436	            for m in data["models"]
437	        ],
438	        "benchmarks": {},
439	    }
440	
441	    for bench, bench_data in data["benchmarks"].items():
442	        min_var = getattr(args, 'min_item_variance', 0.01)
443	        bench_data = filter_low_variance_items(bench_data, min_variance=min_var)
444	        n_models = bench_data["responses"].shape[0]
445	        n_items = bench_data["n_items"]
446	        responses = bench_data["responses"]
447	        valid = bench_data["valid_mask"]
448	        item_keep_mask = bench_data["item_keep_mask"]
449	        tau_full = exposure_scores[bench]
450	        tau = tau_full[:len(item_keep_mask)][item_keep_mask]
451	
452	        # Filter to valid models
453	        if not valid.all():
454	            responses = responses[valid]
455	            dosages_bench = dosages[valid]
456	            n_models = responses.shape[0]
457	        else:
458	            dosages_bench = dosages
459	
460	        exposure_matrix = build_exposure_matrix(dosages_bench, tau)
461	
462	        logger.info("=== %s: %d models x %d items ===", bench, n_models, n_items)
463	        logger.info("Mean accuracy: %.3f", responses.mean())
464	        logger.info("Dosage range: %d - %d", dosages_bench.min(), dosages_bench.max())
465	
466	        stan_data = {
467	            "N_models": int(n_models),
468	            "N_items": int(n_items),
469	            "y": responses.tolist(),
470	            "exposure": exposure_matrix.tolist(),
471	        }
472	
473	        t0 = time.time()
474	        fit = run_stan_fit(
475	            stan_file, stan_data,
476	            chains=args.chains,
477	            iter_sampling=args.iter_sampling,
478	            adapt_delta=args.adapt_delta,
479	            max_treedepth=args.max_treedepth,
480	            seed=args.seed,
481	        )
482	        elapsed = time.time() - t0
483	        logger.info("Sampling done in %.1fs", elapsed)
484	
485	        diag = extract_diagnostics(fit)
486	        item_params = extract_item_parameters(fit, n_items)
487	        model_params = extract_model_parameters(fit, n_models,
488	                                                [data["models"][i] for i, v in enumerate(valid) if v])
489	        cal_scores = extract_calibrated_scores(fit, n_models, responses)
490	
491	        bench_result = {
492	            "n_models": n_models,
493	            "n_items": n_items,
494	            "n_items_excluded": bench_data["n_excluded"],
495	            "excluded_item_indices": bench_data["excluded_item_indices"],
496	            "elapsed_sec": round(elapsed, 1),
497	            "diagnostics": diag,
498	            "gamma": model_params["gamma"],
499	            "item_parameters": item_params,
500	            "model_parameters": model_params["models"],
501	            "calibrated_scores": cal_scores["scores"],
502	        }
503	        all_results["benchmarks"][bench] = bench_result
504	
505	        logger.info("gamma: mean=%.4f, sd=%.4f, 95%%CI=[%.4f, %.4f]",
506	                    model_params["gamma"]["mean"], model_params["gamma"]["sd"],
507	                    model_params["gamma"]["q025"], model_params["gamma"]["q975"])
508	        logger.info("Diagnostics: R-hat=%.4f, divergent=%d (%.2f%%)",
509	                    diag["max_rhat"] or 0, diag["divergent_count"], diag["divergent_pct"])
510	
511	    # Save outputs
512	    with open(output_dir / "stan_fit_summary.json", "w") as f:
513	        json.dump(all_results, f, indent=2)
514	
515	    # Separate files for convenience
516	    for bench, br in all_results["benchmarks"].items():
517	        bench_dir = output_dir / bench
518	        bench_dir.mkdir(parents=True, exist_ok=True)
519	
520	        with open(bench_dir / "item_parameters.json", "w") as f:
521	            json.dump(br["item_parameters"], f, indent=2)
522	        with open(bench_dir / "model_parameters.json", "w") as f:
523	            json.dump({"gamma": br["gamma"], "models": br["model_parameters"]}, f, indent=2)
524	        with open(bench_dir / "calibrated_scores.json", "w") as f:
525	            json.dump(br["calibrated_scores"], f, indent=2)
526	        with open(bench_dir / "diagnostics.json", "w") as f:
527	            json.dump(br["diagnostics"], f, indent=2)
528	
529	    logger.info("Results saved to %s", output_dir)
530	    return all_results
531	
532	
533	def main():
534	    parser = argparse.ArgumentParser(
535	        description="Bayesian IRT calibration via CmdStanPy (4PL+γ NUTS)")
536	    parser.add_argument("--eval-dir", type=str,
537	                        help="Directory with per-model eval subdirectories")
538	    parser.add_argument("--stan-model", type=str, required=True,
539	                        help="Path to .stan model file")
540	    parser.add_argument("--output-dir", type=str, required=True,
541	                        help="Output directory for results")
542	    parser.add_argument("--exposure-file", type=str, default=None,
543	                        help="JSON with per-benchmark exposure scores")
544	    parser.add_argument("--benchmarks", nargs="*", default=None,
545	                        help="Benchmarks to analyze (default: all)")
546	    parser.add_argument("--chains", type=int, default=4)
547	    parser.add_argument("--iter-sampling", type=int, default=1000)
548	    parser.add_argument("--iter-warmup", type=int, default=500)
549	    parser.add_argument("--adapt-delta", type=float, default=0.95)
550	    parser.add_argument("--max-treedepth", type=int, default=12)
551	    parser.add_argument("--seed", type=int, default=42)
552	    parser.add_argument("--min-item-variance", type=float, default=0.01,
553	                        help="Minimum item response variance to keep (default: 0.01)")
554	    parser.add_argument("--synthetic", action="store_true",
555	                        help="Run synthetic data validation instead of real data")
556	
557	    args = parser.parse_args()
558	
559	    logging.basicConfig(
560	        level=logging.INFO,
561	        format="%(asctime)s [%(levelname)s] %(message)s",
562	    )
563	
564	    output_dir = Path(args.output_dir)
565	
566	    if args.synthetic:
567	        run_synthetic_validation(args.stan_model, output_dir, args)
568	    else:
569	        if not args.eval_dir:
570	            parser.error("--eval-dir is required when not using --synthetic")
571	        run_real_data(args.eval_dir, args.stan_model, output_dir,
572	                      args.exposure_file, args.benchmarks, args)
573	
574	
575	if __name__ == "__main__":
576	    main()
577	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "4a99ef3d-5917-4610-afe8-01b777d73762",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_irt_calibration/run_irt_stan.py",
      "content": "# CmdStanPy Bayesian IRT calibration pipeline (replaces PyTorch MLE version)\n# 4PL+γ model: P(y=1) = c + (d-c) * logit^{-1}(a*(theta - b) + gamma * exposure)\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nimport cmdstanpy\n\nlogger = logging.getLogger(__name__)\n\nDOSAGE_PATTERN = re.compile(r\"_d(\\d+)_s(\\d+)(_para)?$\")\n\n\ndef parse_model_dir_name(dirname: str) -> dict | None:\n    m = DOSAGE_PATTERN.search(dirname)\n    if not m:\n        return None\n    dosage = int(m.group(1))\n    seed = int(m.group(2))\n    is_para = m.group(3) is not None\n    model_name = dirname[: m.start()]\n    return {\n        \"dirname\": dirname,\n        \"model_name\": model_name,\n        \"dosage\": dosage,\n        \"seed\": seed,\n        \"is_para\": is_para,\n    }\n\n\ndef load_eval_results(eval_dir: str, benchmarks: list[str] | None = None,\n                      skip_para: bool = True) -> dict:\n    eval_path = Path(eval_dir)\n    model_dirs = sorted([\n        d for d in eval_path.iterdir()\n        if d.is_dir() and (d / \"eval_results.json\").exists()\n    ])\n\n    models = []\n    for d in model_dirs:\n        info = parse_model_dir_name(d.name)\n        if info is None:\n            logger.warning(\"Skipping unrecognized directory: %s\", d.name)\n            continue\n        if skip_para and info[\"is_para\"]:\n            continue\n        info[\"path\"] = str(d)\n        models.append(info)\n\n    if not models:\n        raise ValueError(f\"No valid eval results found in {eval_dir}\")\n\n    logger.info(\"Found %d model evaluations\", len(models))\n\n    with open(Path(models[0][\"path\"]) / \"eval_results.json\") as f:\n        sample = json.load(f)\n    available_benchmarks = list(sample[\"benchmarks\"].keys())\n\n    if benchmarks:\n        benchmarks = [b for b in benchmarks if b in available_benchmarks]\n    else:\n        benchmarks = available_benchmarks\n\n    logger.info(\"Benchmarks: %s\", benchmarks)\n\n    result = {\"models\": models, \"benchmarks\": {}, \"dosages\": np.array([m[\"dosage\"] for m in models])}\n\n    for bench in benchmarks:\n        responses = []\n        for m in models:\n            results_file = Path(m[\"path\"]) / \"eval_results.json\"\n            with open(results_file) as f:\n                data = json.load(f)\n\n            if bench not in data[\"benchmarks\"]:\n                logger.warning(\"Benchmark %s missing for %s\", bench, m[\"dirname\"])\n                responses.append(None)\n                continue\n\n            per_item = data[\"benchmarks\"][bench][\"per_item\"]\n            correct = [int(item[\"correct\"]) for item in per_item]\n            responses.append(correct)\n\n        lengths = [len(r) for r in responses if r is not None]\n        if not lengths:\n            continue\n\n        n_items = min(lengths)\n        matrix = np.zeros((len(models), n_items), dtype=int)\n        valid_mask = np.ones(len(models), dtype=bool)\n        for j, r in enumerate(responses):\n            if r is None:\n                valid_mask[j] = False\n            else:\n                matrix[j, :n_items] = r[:n_items]\n\n        result[\"benchmarks\"][bench] = {\n            \"responses\": matrix,\n            \"n_items\": n_items,\n            \"valid_mask\": valid_mask,\n        }\n\n    return result\n\n\ndef filter_low_variance_items(bench_data: dict, min_variance: float = 0.01) -> dict:\n    \"\"\"Remove items with near-zero response variance (uninformative for IRT).\n\n    Items where all respondents answer identically provide no discrimination\n    information. IRT parameters (especially discrimination 'a') cannot be\n    estimated for such items.\n    \"\"\"\n    matrix = bench_data[\"responses\"]\n    valid = bench_data[\"valid_mask\"]\n    responses_valid = matrix[valid]\n\n    item_var = responses_valid.var(axis=0)\n    keep_mask = item_var >= min_variance\n    n_excluded = int((~keep_mask).sum())\n\n    if n_excluded > 0:\n        excluded_indices = np.where(~keep_mask)[0].tolist()\n        logger.info(\n            \"Filtered %d/%d items with variance < %.3f (indices: %s...)\",\n            n_excluded, len(keep_mask), min_variance,\n            excluded_indices[:10],\n        )\n        matrix = matrix[:, keep_mask]\n        return {\n            \"responses\": matrix,\n            \"n_items\": int(keep_mask.sum()),\n            \"valid_mask\": bench_data[\"valid_mask\"],\n            \"excluded_item_indices\": excluded_indices,\n            \"n_excluded\": n_excluded,\n            \"item_keep_mask\": keep_mask,\n        }\n\n    n_items = bench_data[\"n_items\"]\n    return {\n        **bench_data,\n        \"excluded_item_indices\": [],\n        \"n_excluded\": 0,\n        \"item_keep_mask\": np.ones(n_items, dtype=bool),\n    }\n\n\ndef load_exposure_scores(exposure_file: str | None, benchmarks: dict) -> dict:\n    if exposure_file and os.path.exists(exposure_file):\n        with open(exposure_file) as f:\n            raw = json.load(f)\n        exposure = {}\n        for bench in benchmarks:\n            if bench in raw:\n                exposure[bench] = np.array(raw[bench], dtype=float)\n            else:\n                n_items = benchmarks[bench][\"n_items\"]\n                exposure[bench] = np.ones(n_items)\n        return exposure\n\n    exposure = {}\n    for bench, bdata in benchmarks.items():\n        exposure[bench] = np.ones(bdata[\"n_items\"])\n    return exposure\n\n\ndef build_exposure_matrix(dosages: np.ndarray, tau: np.ndarray) -> np.ndarray:\n    \"\"\"Build exposure matrix: exposure[i,j] = dosage[i] * tau[j] / max_dosage.\"\"\"\n    max_d = dosages.max() if dosages.max() > 0 else 1.0\n    dosage_norm = dosages / max_d\n    return np.outer(dosage_norm, tau)\n\n\ndef generate_synthetic_data(n_models=50, n_items=100, gamma_true=0.5,\n                            exposure_rate=0.3, seed=42):\n    \"\"\"Generate synthetic data for sanity checking.\"\"\"\n    rng = np.random.default_rng(seed)\n    theta = rng.standard_normal(n_models)\n    a = rng.lognormal(0, 0.5, n_items)\n    b = rng.standard_normal(n_items)\n    c = rng.beta(5, 20, n_items)\n    d = rng.beta(20, 5, n_items)\n    exposure = rng.binomial(1, exposure_rate, (n_models, n_items)).astype(float)\n\n    from scipy.special import expit\n    eta = np.outer(np.ones(n_models), a) * (theta[:, None] - b[None, :]) + gamma_true * exposure\n    prob = c[None, :] + (d[None, :] - c[None, :]) * expit(eta)\n    y = rng.binomial(1, prob)\n\n    return {\n        \"y\": y,\n        \"exposure\": exposure,\n        \"true_params\": {\n            \"theta\": theta.tolist(),\n            \"a\": a.tolist(),\n            \"b\": b.tolist(),\n            \"c\": c.tolist(),\n            \"d\": d.tolist(),\n            \"gamma\": gamma_true,\n        },\n        \"N_models\": n_models,\n        \"N_items\": n_items,\n    }\n\n\ndef run_stan_fit(stan_file: str, stan_data: dict, chains: int = 4,\n                 iter_sampling: int = 1000, iter_warmup: int = 500,\n                 adapt_delta: float = 0.95, max_treedepth: int = 12,\n                 seed: int = 42) -> cmdstanpy.CmdStanMCMC:\n    model = cmdstanpy.CmdStanModel(stan_file=stan_file)\n    fit = model.sample(\n        data=stan_data,\n        chains=chains,\n        iter_warmup=iter_warmup,\n        iter_sampling=iter_sampling,\n        seed=seed,\n        adapt_delta=adapt_delta,\n        max_treedepth=max_treedepth,\n        parallel_chains=min(chains, 4),\n        show_progress=True,\n    )\n    return fit\n\n\ndef extract_diagnostics(fit: cmdstanpy.CmdStanMCMC) -> dict:\n    summary = fit.summary()\n\n    diag_text = fit.diagnose()\n    divergent = 0\n    for line in diag_text.split('\\n'):\n        if 'divergent' in line.lower():\n            parts = [w for w in line.split() if w.isdigit()]\n            if parts:\n                divergent = int(parts[0])\n                break\n\n    total_draws = fit.chains * fit.num_draws_sampling\n    divergent_pct = 100.0 * divergent / total_draws if total_draws > 0 else 0.0\n\n    max_rhat = float(summary['R_hat'].max()) if 'R_hat' in summary.columns else None\n    if 'ESS_bulk' in summary.columns:\n        min_ess_bulk = float(summary['ESS_bulk'].min())\n    elif 'N_Eff' in summary.columns:\n        min_ess_bulk = float(summary['N_Eff'].min())\n    else:\n        min_ess_bulk = None\n\n    return {\n        \"divergent_count\": divergent,\n        \"divergent_pct\": round(divergent_pct, 4),\n        \"max_rhat\": round(max_rhat, 5) if max_rhat else None,\n        \"min_ess_bulk\": round(min_ess_bulk, 1) if min_ess_bulk else None,\n        \"total_draws\": total_draws,\n        \"chains\": fit.chains,\n    }\n\n\ndef extract_item_parameters(fit: cmdstanpy.CmdStanMCMC, n_items: int) -> dict:\n    a_draws = fit.stan_variable(\"a\")  # shape: (n_draws, n_items)\n    b_draws = fit.stan_variable(\"b\")\n    c_draws = fit.stan_variable(\"c\")\n    d_draws = fit.stan_variable(\"d\")\n\n    items = []\n    for j in range(n_items):\n        items.append({\n            \"item_idx\": j,\n            \"a_mean\": round(float(np.mean(a_draws[:, j])), 4),\n            \"a_sd\": round(float(np.std(a_draws[:, j])), 4),\n            \"b_mean\": round(float(np.mean(b_draws[:, j])), 4),\n            \"b_sd\": round(float(np.std(b_draws[:, j])), 4),\n            \"c_mean\": round(float(np.mean(c_draws[:, j])), 4),\n            \"c_sd\": round(float(np.std(c_draws[:, j])), 4),\n            \"d_mean\": round(float(np.mean(d_draws[:, j])), 4),\n            \"d_sd\": round(float(np.std(d_draws[:, j])), 4),\n        })\n\n    return {\"items\": items, \"n_items\": n_items}\n\n\ndef extract_model_parameters(fit: cmdstanpy.CmdStanMCMC, n_models: int,\n                             model_info: list[dict] | None = None) -> dict:\n    theta_draws = fit.stan_variable(\"theta\")  # (n_draws, n_models)\n    gamma_draws = fit.stan_variable(\"gamma\")  # (n_draws,) scalar\n\n    gamma_mean = float(np.mean(gamma_draws))\n    gamma_sd = float(np.std(gamma_draws))\n    gamma_q025 = float(np.percentile(gamma_draws, 2.5))\n    gamma_q975 = float(np.percentile(gamma_draws, 97.5))\n\n    models = []\n    for i in range(n_models):\n        theta_i = theta_draws[:, i]\n        entry = {\n            \"model_idx\": i,\n            \"theta_mean\": round(float(np.mean(theta_i)), 4),\n            \"theta_sd\": round(float(np.std(theta_i)), 4),\n            \"theta_q025\": round(float(np.percentile(theta_i, 2.5)), 4),\n            \"theta_q975\": round(float(np.percentile(theta_i, 97.5)), 4),\n        }\n        if model_info and i < len(model_info):\n            entry[\"dirname\"] = model_info[i][\"dirname\"]\n            entry[\"model_name\"] = model_info[i][\"model_name\"]\n            entry[\"dosage\"] = model_info[i][\"dosage\"]\n        models.append(entry)\n\n    return {\n        \"gamma\": {\n            \"mean\": round(gamma_mean, 4),\n            \"sd\": round(gamma_sd, 4),\n            \"q025\": round(gamma_q025, 4),\n            \"q975\": round(gamma_q975, 4),\n            \"ci_excludes_zero\": bool(gamma_q025 > 0 or gamma_q975 < 0),\n        },\n        \"models\": models,\n    }\n\n\ndef extract_calibrated_scores(fit: cmdstanpy.CmdStanMCMC, n_models: int,\n                              responses: np.ndarray) -> dict:\n    cal_draws = fit.stan_variable(\"calibrated_score\")  # (n_draws, n_models)\n\n    raw_scores = responses.mean(axis=1).tolist()\n    entries = []\n    for i in range(n_models):\n        cal_i = cal_draws[:, i]\n        entries.append({\n            \"model_idx\": i,\n            \"raw_accuracy\": round(raw_scores[i], 4),\n            \"calibrated_mean\": round(float(np.mean(cal_i)), 4),\n            \"calibrated_sd\": round(float(np.std(cal_i)), 4),\n            \"calibrated_q025\": round(float(np.percentile(cal_i, 2.5)), 4),\n            \"calibrated_q975\": round(float(np.percentile(cal_i, 97.5)), 4),\n            \"adjustment\": round(float(np.mean(cal_i)) - raw_scores[i], 4),\n        })\n\n    return {\"scores\": entries}\n\n\ndef run_synthetic_validation(stan_file: str, output_dir: Path, args):\n    logger.info(\"Generating synthetic data...\")\n    synth = generate_synthetic_data()\n    y = synth[\"y\"]\n    exposure = synth[\"exposure\"]\n    true = synth[\"true_params\"]\n\n    stan_data = {\n        \"N_models\": synth[\"N_models\"],\n        \"N_items\": synth[\"N_items\"],\n        \"y\": y.tolist(),\n        \"exposure\": exposure.tolist(),\n    }\n\n    logger.info(\"Fitting Stan model (synthetic, %d models x %d items)...\",\n                synth[\"N_models\"], synth[\"N_items\"])\n    t0 = time.time()\n    fit = run_stan_fit(\n        stan_file, stan_data,\n        chains=args.chains,\n        iter_sampling=args.iter_sampling,\n        adapt_delta=args.adapt_delta,\n        max_treedepth=args.max_treedepth,\n        seed=args.seed,\n    )\n    elapsed = time.time() - t0\n    logger.info(\"Sampling done in %.1fs\", elapsed)\n\n    # Recovery metrics\n    theta_draws = fit.stan_variable(\"theta\")\n    theta_post = np.mean(theta_draws, axis=0)\n    theta_corr = float(np.corrcoef(theta_post, true[\"theta\"])[0, 1])\n\n    gamma_draws = fit.stan_variable(\"gamma\")\n    gamma_mean = float(np.mean(gamma_draws))\n    gamma_sd = float(np.std(gamma_draws))\n\n    a_draws = fit.stan_variable(\"a\")\n    a_post = np.mean(a_draws, axis=0)\n    a_corr = float(np.corrcoef(a_post, true[\"a\"])[0, 1])\n\n    b_draws = fit.stan_variable(\"b\")\n    b_post = np.mean(b_draws, axis=0)\n    b_corr = float(np.corrcoef(b_post, true[\"b\"])[0, 1])\n\n    diag = extract_diagnostics(fit)\n\n    result = {\n        \"mode\": \"synthetic_validation\",\n        \"true_gamma\": true[\"gamma\"],\n        \"estimated_gamma_mean\": round(gamma_mean, 4),\n        \"estimated_gamma_sd\": round(gamma_sd, 4),\n        \"gamma_bias\": round(gamma_mean - true[\"gamma\"], 4),\n        \"gamma_rel_bias\": round(abs(gamma_mean - true[\"gamma\"]) / abs(true[\"gamma\"]), 4),\n        \"theta_corr\": round(theta_corr, 4),\n        \"a_corr\": round(a_corr, 4),\n        \"b_corr\": round(b_corr, 4),\n        \"diagnostics\": diag,\n        \"elapsed_sec\": round(elapsed, 1),\n    }\n\n    logger.info(\"Recovery: gamma=%.4f (true=%.4f), theta_corr=%.4f, a_corr=%.4f, b_corr=%.4f\",\n                gamma_mean, true[\"gamma\"], theta_corr, a_corr, b_corr)\n    logger.info(\"Diagnostics: R-hat=%.4f, divergent=%d (%.2f%%)\",\n                diag[\"max_rhat\"] or 0, diag[\"divergent_count\"], diag[\"divergent_pct\"])\n\n    output_dir.mkdir(parents=True, exist_ok=True)\n    out_file = output_dir / \"synthetic_validation.json\"\n    with open(out_file, \"w\") as f:\n        json.dump(result, f, indent=2)\n    logger.info(\"Saved: %s\", out_file)\n    return result\n\n\ndef run_real_data(eval_dir: str, stan_file: str, output_dir: Path,\n                  exposure_file: str | None, benchmarks_filter: list[str] | None,\n                  args):\n    data = load_eval_results(eval_dir, benchmarks_filter)\n    exposure_scores = load_exposure_scores(exposure_file, data[\"benchmarks\"])\n    dosages = data[\"dosages\"]\n\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    all_results = {\n        \"mode\": \"real\",\n        \"eval_dir\": eval_dir,\n        \"stan_model\": stan_file,\n        \"models\": [\n            {\"dirname\": m[\"dirname\"], \"model_name\": m[\"model_name\"],\n             \"dosage\": m[\"dosage\"], \"seed\": m[\"seed\"]}\n            for m in data[\"models\"]\n        ],\n        \"benchmarks\": {},\n    }\n\n    for bench, bench_data in data[\"benchmarks\"].items():\n        min_var = getattr(args, 'min_item_variance', 0.01)\n        bench_data = filter_low_variance_items(bench_data, min_variance=min_var)\n        n_models = bench_data[\"responses\"].shape[0]\n        n_items = bench_data[\"n_items\"]\n        responses = bench_data[\"responses\"]\n        valid = bench_data[\"valid_mask\"]\n        item_keep_mask = bench_data[\"item_keep_mask\"]\n        tau_full = exposure_scores[bench]\n        tau = tau_full[:len(item_keep_mask)][item_keep_mask]\n\n        # Filter to valid models\n        if not valid.all():\n            responses = responses[valid]\n            dosages_bench = dosages[valid]\n            n_models = responses.shape[0]\n        else:\n            dosages_bench = dosages\n\n        exposure_matrix = build_exposure_matrix(dosages_bench, tau)\n\n        logger.info(\"=== %s: %d models x %d items ===\", bench, n_models, n_items)\n        logger.info(\"Mean accuracy: %.3f\", responses.mean())\n        logger.info(\"Dosage range: %d - %d\", dosages_bench.min(), dosages_bench.max())\n\n        stan_data = {\n            \"N_models\": int(n_models),\n            \"N_items\": int(n_items),\n            \"y\": responses.tolist(),\n            \"exposure\": exposure_matrix.tolist(),\n        }\n\n        t0 = time.time()\n        fit = run_stan_fit(\n            stan_file, stan_data,\n            chains=args.chains,\n            iter_sampling=args.iter_sampling,\n            adapt_delta=args.adapt_delta,\n            max_treedepth=args.max_treedepth,\n            seed=args.seed,\n        )\n        elapsed = time.time() - t0\n        logger.info(\"Sampling done in %.1fs\", elapsed)\n\n        diag = extract_diagnostics(fit)\n        item_params = extract_item_parameters(fit, n_items)\n        model_params = extract_model_parameters(fit, n_models,\n                                                [data[\"models\"][i] for i, v in enumerate(valid) if v])\n        cal_scores = extract_calibrated_scores(fit, n_models, responses)\n\n        bench_result = {\n            \"n_models\": n_models,\n            \"n_items\": n_items,\n            \"n_items_excluded\": bench_data[\"n_excluded\"],\n            \"excluded_item_indices\": bench_data[\"excluded_item_indices\"],\n            \"elapsed_sec\": round(elapsed, 1),\n            \"diagnostics\": diag,\n            \"gamma\": model_params[\"gamma\"],\n            \"item_parameters\": item_params,\n            \"model_parameters\": model_params[\"models\"],\n            \"calibrated_scores\": cal_scores[\"scores\"],\n        }\n        all_results[\"benchmarks\"][bench] = bench_result\n\n        logger.info(\"gamma: mean=%.4f, sd=%.4f, 95%%CI=[%.4f, %.4f]\",\n                    model_params[\"gamma\"][\"mean\"], model_params[\"gamma\"][\"sd\"],\n                    model_params[\"gamma\"][\"q025\"], model_params[\"gamma\"][\"q975\"])\n        logger.info(\"Diagnostics: R-hat=%.4f, divergent=%d (%.2f%%)\",\n                    diag[\"max_rhat\"] or 0, diag[\"divergent_count\"], diag[\"divergent_pct\"])\n\n    # Save outputs\n    with open(output_dir / \"stan_fit_summary.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Separate files for convenience\n    for bench, br in all_results[\"benchmarks\"].items():\n        bench_dir = output_dir / bench\n        bench_dir.mkdir(parents=True, exist_ok=True)\n\n        with open(bench_dir / \"item_parameters.json\", \"w\") as f:\n            json.dump(br[\"item_parameters\"], f, indent=2)\n        with open(bench_dir / \"model_parameters.json\", \"w\") as f:\n            json.dump({\"gamma\": br[\"gamma\"], \"models\": br[\"model_parameters\"]}, f, indent=2)\n        with open(bench_dir / \"calibrated_scores.json\", \"w\") as f:\n            json.dump(br[\"calibrated_scores\"], f, indent=2)\n        with open(bench_dir / \"diagnostics.json\", \"w\") as f:\n            json.dump(br[\"diagnostics\"], f, indent=2)\n\n    logger.info(\"Results saved to %s\", output_dir)\n    return all_results\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Bayesian IRT calibration via CmdStanPy (4PL+γ NUTS)\")\n    parser.add_argument(\"--eval-dir\", type=str,\n                        help=\"Directory with per-model eval subdirectories\")\n    parser.add_argument(\"--stan-model\", type=str, required=True,\n                        help=\"Path to .stan model file\")\n    parser.add_argument(\"--output-dir\", type=str, required=True,\n                        help=\"Output directory for results\")\n    parser.add_argument(\"--exposure-file\", type=str, default=None,\n                        help=\"JSON with per-benchmark exposure scores\")\n    parser.add_argument(\"--benchmarks\", nargs=\"*\", default=None,\n                        help=\"Benchmarks to analyze (default: all)\")\n    parser.add_argument(\"--chains\", type=int, default=4)\n    parser.add_argument(\"--iter-sampling\", type=int, default=1000)\n    parser.add_argument(\"--iter-warmup\", type=int, default=500)\n    parser.add_argument(\"--adapt-delta\", type=float, default=0.95)\n    parser.add_argument(\"--max-treedepth\", type=int, default=12)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--min-item-variance\", type=float, default=0.01,\n                        help=\"Minimum item response variance to keep (default: 0.01)\")\n    parser.add_argument(\"--synthetic\", action=\"store_true\",\n                        help=\"Run synthetic data validation instead of real data\")\n\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    output_dir = Path(args.output_dir)\n\n    if args.synthetic:\n        run_synthetic_validation(args.stan_model, output_dir, args)\n    else:\n        if not args.eval_dir:\n            parser.error(\"--eval-dir is required when not using --synthetic\")\n        run_real_data(args.eval_dir, args.stan_model, output_dir,\n                      args.exposure_file, args.benchmarks, args)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 577,
      "startLine": 1,
      "totalLines": 577
    }
  }
}
```

</details>

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the codebase. Let me also read the `run_irt_calibration.py` on the remote server (since it's imported by both `run_pooled_4bench_irt.py` and `run_stratified_irt.py`), to understand `prepare_stan_data`, `fit_stan_model`, `check_convergence`, `posterior_predictive_check`, `extract_results`, and `STAN_MODELS`.

Wait, I see that `run_stratified_irt.py` already does exactly what the task asks — Scheme B stratifies by model size (0.5B/1.5B/3B). 

Looking more closely at the code, `run_stratified_irt.py` already has the scale groups defined, includes a filter function for them, and uses `--scheme B` to run per-scale IRT fits with a dry-run mode available. It seems like this script is already implementing the per-scale IRT fitting that the task is asking for.

But re-reading the requirements, the task actually wants me to modify the main pooled script `run_pooled_4bench_irt.py` by adding a `--stratify-by-scale` flag that switches between pooled and per-scale fitting modes, while maintaining backward compatibility when the flag isn't used. The output also needs to match a specific summary table format that the existing script doesn't produce. Looking at what both scripts import from `run_irt_calibration.py`, I can see they share most of the same functions — `load_pooled_eval_results`, `prepare_stan_data`, `fit_stan_model`, and the others. This means I can modify `run_pooled_4bench_irt.py` to add the stratification option by reusing the existing filtering logic rather than duplicating code. py` is the main pooled analysis script, I should add the `--stratify-by-scale` flag there to let users toggle between pooled and per-scale fitting modes. This keeps the default behavior intact while adding the new stratification option when needed.

Now I'm planning the implementation: add the flag to argument parsing, then in the main function check if stratification is enabled — if so, loop through each scale, filter the data accordingly, run the IRT fitting for each benchmark with that filtered subset, and compile everything into the summary table format. I need to check how the existing stratified script handles the filtering so I can reuse that logic.

Writing filter function... I'm realizing there's a tension here — the D045 exclusion already removes 0.5B from mmlu and arc_challenge, so when running per-scale analysis with the stratify flag, those cells will naturally be empty. But that actually serves the purpose of D105, which is investigating whether ARC's negative γ is specific to 0.5B models. If 0.5B is already excluded from ARC by D045, then the per-scale breakdown won't help isolate that artifact.

I think the safest approach is to keep D045 active and let the code warn when it skips those cells — the user will see that only 1.5B and 3B have results for ARC, and they can decide if they want to override the exclusion for this specific analysis. The task mentions fitting IRT separately for each scale group, which suggests they want to estimate θ_j and item parameters independently per scale.

Now I'm working on the implementation. I need to modify the existing code to handle the output format with γ̂ and confidence intervals, plus JSON output. The tricky part is that `run_single_benchmark_fit` applies exclusions internally, so I need to think through how to pass the pre-filtered data correctly.

Modifying the fit function... I need to figure out what diagnostic information is available for gamma specifically — the current `extract_results` function gives me the posterior summaries but not the convergence metrics like R̂ and ESS that are needed for the output table. Let me trace through what `run_irt_stan.py` actually returns to see if I can access those convergence diagnostics at the gamma level.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "37de01a8-a77f-42a1-851f-b310b2a4ae32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174qVWgHDB9K2TjwLo9sh7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22160,
      "cache_read_input_tokens": 27351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22160
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

_source line 69_

Now let me check the core module that both scripts import from, and also look at what's on the remote server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "d74a9c24-fa1a-4c2d-989c-15b8375779db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174qVWgHDB9K2TjwLo9sh7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22160,
      "cache_read_input_tokens": 27351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22160
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

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Glob · `toolu_01GwnASUbXdtfXmRSmyzczmj`</summary>

```json
{
  "pattern": "**/run_irt_calibration.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "295e5b9e-16cc-406e-be0e-37f92c20b79e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174qVWgHDB9K2TjwLo9sh7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22160,
      "cache_read_input_tokens": 27351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22160
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

### Tool result

_source line 71 · 2026-05-16T05:30:47.648Z_

<details><summary>↩ Tool result · `toolu_01GwnASUbXdtfXmRSmyzczmj`</summary>

```text
artifacts/exp006/run_irt_calibration.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "0b34b2ed-71f2-4439-843e-a3dfbf28124e",
  "tool_use_result": {
    "filenames": [
      "artifacts/exp006/run_irt_calibration.py"
    ],
    "durationMs": 50,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Glob · `toolu_017fCeeXhBZWWvBWjhsC2bcs`</summary>

```json
{
  "pattern": "**/exp006/**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "71e2fa35-dca2-4da3-a737-d31d7f90465a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174qVWgHDB9K2TjwLo9sh7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22160,
      "cache_read_input_tokens": 27351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22160
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

### Tool result

_source line 73 · 2026-05-16T05:30:48.013Z_

<details><summary>↩ Tool result · `toolu_017fCeeXhBZWWvBWjhsC2bcs`</summary>

```text
artifacts/exp006/run_irt_calibration.py
artifacts/exp006/intermediate/run_irt_stan.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "05cb7816-5e41-440a-b045-0ea43265c670",
  "tool_use_result": {
    "filenames": [
      "artifacts/exp006/run_irt_calibration.py",
      "artifacts/exp006/intermediate/run_irt_stan.py"
    ],
    "durationMs": 51,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Read · `toolu_015KJy2hHfgNL9vCWQFqRgFh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "77f46776-8a74-4b9e-9efd-0c958954f96f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LViBdH3CvRm2FpyWAAhM3y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3660,
      "cache_read_input_tokens": 49511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3660
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

_source line 75 · 2026-05-16T05:30:50.795Z_

<details><summary>↩ Tool result · `toolu_015KJy2hHfgNL9vCWQFqRgFh`</summary>

```text
1	"""
2	IRT parameter estimation for contamination-aware calibration.
3	
4	Fits two models to item-level correctness data from benchmark evaluations:
5	  1) Standard 2PL IRT (baseline)
6	  2) 4PL+γ contamination-aware IRT
7	
8	Input:
9	  --eval-dir      Directory containing per-model eval subdirectories
10	                  (each with eval_results.json / correctness_matrix.json)
11	  --exposure-file (optional) JSON mapping benchmark -> [τ_i, ...] exposure scores
12	  --benchmarks    Which benchmarks to analyze (default: all found)
13	  --output-dir    Where to write results JSON
14	
15	Output (per benchmark):
16	  irt_results.json with θ, γ, item params, calibrated scores, CIs
17	
18	Dependencies: torch, numpy, scipy
19	"""
20	
21	import argparse
22	import json
23	import logging
24	import math
25	import os
26	import re
27	import sys
28	from pathlib import Path
29	
30	import numpy as np
31	import torch
32	import torch.nn as nn
33	from scipy import stats
34	
35	logger = logging.getLogger(__name__)
36	
37	# ── Data Loading ──
38	
39	DOSAGE_PATTERN = re.compile(r"_d(\d+)_s(\d+)(_para)?$")
40	
41	
42	def parse_model_dir_name(dirname: str) -> dict | None:
43	    """Extract model name, dosage, seed from directory like qwen2.5-0.5b_d025_s123."""
44	    m = DOSAGE_PATTERN.search(dirname)
45	    if not m:
46	        return None
47	    dosage = int(m.group(1))
48	    seed = int(m.group(2))
49	    is_para = m.group(3) is not None
50	    model_name = dirname[: m.start()]
51	    return {
52	        "dirname": dirname,
53	        "model_name": model_name,
54	        "dosage": dosage,
55	        "seed": seed,
56	        "is_para": is_para,
57	    }
58	
59	
60	def load_eval_results(eval_dir: str, benchmarks: list[str] | None = None,
61	                      skip_para: bool = True) -> dict:
62	    eval_path = Path(eval_dir)
63	    model_dirs = sorted([
64	        d for d in eval_path.iterdir()
65	        if d.is_dir() and (d / "eval_results.json").exists()
66	    ])
67	
68	    models = []
69	    for d in model_dirs:
70	        info = parse_model_dir_name(d.name)
71	        if info is None:
72	            logger.warning("Skipping unrecognized directory: %s", d.name)
73	            continue
74	        if skip_para and info["is_para"]:
75	            continue
76	        info["path"] = str(d)
77	        models.append(info)
78	
79	    if not models:
80	        raise ValueError(f"No valid eval results found in {eval_dir}")
81	
82	    logger.info("Found %d model evaluations", len(models))
83	
84	    with open(Path(models[0]["path"]) / "eval_results.json") as f:
85	        sample = json.load(f)
86	    available_benchmarks = list(sample["benchmarks"].keys())
87	
88	    if benchmarks:
89	        benchmarks = [b for b in benchmarks if b in available_benchmarks]
90	    else:
91	        benchmarks = available_benchmarks
92	
93	    logger.info("Benchmarks: %s", benchmarks)
94	
95	    result = {"models": models, "benchmarks": {}, "dosages": np.array([m["dosage"] for m in models])}
96	
97	    for bench in benchmarks:
98	        responses = []
99	        for m in models:
100	            results_file = Path(m["path"]) / "eval_results.json"
101	            with open(results_file) as f:
102	                data = json.load(f)
103	
104	            if bench not in data["benchmarks"]:
105	                logger.warning("Benchmark %s missing for %s, filling with NaN", bench, m["dirname"])
106	                responses.append(None)
107	                continue
108	
109	            per_item = data["benchmarks"][bench]["per_item"]
110	            correct = [int(item["correct"]) for item in per_item]
111	            responses.append(correct)
112	
113	        lengths = [len(r) for r in responses if r is not None]
114	        if not lengths:
115	            logger.warning("No data for benchmark %s, skipping", bench)
116	            continue
117	
118	        n_items = lengths[0]
119	        if not all(l == n_items for l in lengths):
120	            logger.warning("Inconsistent item counts for %s: %s", bench, lengths)
121	            n_items = min(lengths)
122	
123	        matrix = np.zeros((len(models), n_items), dtype=np.float32)
124	        mask = np.ones((len(models), n_items), dtype=np.float32)
125	        for j, r in enumerate(responses):
126	            if r is None:
127	                mask[j, :] = 0.0
128	            else:
129	                matrix[j, :n_items] = r[:n_items]
130	
131	        result["benchmarks"][bench] = {
132	            "responses": matrix,
133	            "mask": mask,
134	            "n_items": n_items,
135	        }
136	
137	    return result
138	
139	
140	def load_exposure_scores(exposure_file: str | None, benchmarks: dict) -> dict:
141	    if exposure_file and os.path.exists(exposure_file):
142	        with open(exposure_file) as f:
143	            raw = json.load(f)
144	        scores = {}
145	        for bench, bench_data in benchmarks.items():
146	            n_items = bench_data["n_items"]
147	            if bench in raw:
148	                s = np.array(raw[bench], dtype=np.float32)[:n_items]
149	                if len(s) < n_items:
150	                    s = np.pad(s, (0, n_items - len(s)), constant_values=0.0)
151	                scores[bench] = s
152	            else:
153	                scores[bench] = np.ones(n_items, dtype=np.float32)
154	        return scores
155	
156	    return {bench: np.ones(d["n_items"], dtype=np.float32) for bench, d in benchmarks.items()}
157	
158	
159	# ── IRT Models (PyTorch) ──
160	
161	class IRT2PL(nn.Module):
162	    """Standard 2-parameter logistic IRT model."""
163	
164	    def __init__(self, n_persons: int, n_items: int):
165	        super().__init__()
166	        self.theta = nn.Parameter(torch.zeros(n_persons))
167	        self.a_raw = nn.Parameter(torch.zeros(n_items))
168	        self.b = nn.Parameter(torch.zeros(n_items))
169	
170	    @property
171	    def a(self):
172	        return torch.exp(self.a_raw).clamp(min=0.1, max=5.0)
173	
174	    def forward(self):
175	        theta = self.theta.unsqueeze(1)
176	        a = self.a.unsqueeze(0)
177	        b = self.b.unsqueeze(0)
178	        logit = a * (theta - b)
179	        return torch.sigmoid(logit).clamp(1e-6, 1.0 - 1e-6)
180	
181	
182	class IRT4PLGamma(nn.Module):
183	    """
184	    4PL + γ contamination-aware IRT model.
185	
186	    P(Y_ji = 1) = c_i + (d_i - c_i) * σ(a_i * (θ_j - b_i + γ_j * τ_i))
187	
188	    where γ_j captures contamination advantage proportional to item exposure τ_i.
189	    """
190	
191	    def __init__(self, n_persons: int, n_items: int, tau: torch.Tensor,
192	                 dosages: torch.Tensor | None = None):
193	        super().__init__()
194	        self.n_persons = n_persons
195	        self.n_items = n_items
196	        self.register_buffer("tau", tau)
197	
198	        self.theta = nn.Parameter(torch.zeros(n_persons))
199	        self.gamma_raw = nn.Parameter(torch.zeros(n_persons))
200	        self.a_raw = nn.Parameter(torch.zeros(n_items))
201	        self.b = nn.Parameter(torch.zeros(n_items))
202	        self.c_raw = nn.Parameter(torch.full((n_items,), -2.0))
203	        self.d_raw = nn.Parameter(torch.full((n_items,), 2.0))
204	
205	        if dosages is not None:
206	            with torch.no_grad():
207	                normed = dosages / (dosages.max() + 1e-8)
208	                self.gamma_raw.copy_(normed * 0.5)
209	
210	    @property
211	    def a(self):
212	        return torch.exp(self.a_raw).clamp(min=0.1, max=5.0)
213	
214	    @property
215	    def c(self):
216	        return torch.sigmoid(self.c_raw).clamp(max=0.5)
217	
218	    @property
219	    def d(self):
220	        return (0.5 + 0.5 * torch.sigmoid(self.d_raw))
221	
222	    @property
223	    def gamma(self):
224	        return torch.relu(self.gamma_raw)
225	
226	    def forward(self):
227	        theta = self.theta.unsqueeze(1)
228	        gamma = self.gamma.unsqueeze(1)
229	        tau = self.tau.unsqueeze(0)
230	        a = self.a.unsqueeze(0)
231	        b = self.b.unsqueeze(0)
232	        c = self.c.unsqueeze(0)
233	        d = self.d.unsqueeze(0)
234	
235	        ability = theta - b + gamma * tau
236	        logit = a * ability
237	        prob = c + (d - c) * torch.sigmoid(logit)
238	        return prob.clamp(1e-6, 1.0 - 1e-6)
239	
240	
241	# ── Estimation ──
242	
243	def fit_irt_model(model: nn.Module, responses: torch.Tensor, mask: torch.Tensor,
244	                  lr: float = 0.01, max_iter: int = 5000, tol: float = 1e-6,
245	                  l2_lambda: float = 0.001) -> dict:
246	    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
247	    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
248	        optimizer, patience=200, factor=0.5, min_lr=1e-5
249	    )
250	
251	    prev_loss = float("inf")
252	    best_loss = float("inf")
253	    best_state = None
254	    patience_counter = 0
255	
256	    for epoch in range(max_iter):
257	        optimizer.zero_grad()
258	        probs = model()
259	
260	        log_lik = (
261	            responses * torch.log(probs) + (1 - responses) * torch.log(1 - probs)
262	        )
263	        loss = -(log_lik * mask).sum() / mask.sum()
264	
265	        if hasattr(model, "theta"):
266	            loss = loss + l2_lambda * (model.theta ** 2).mean()
267	        if hasattr(model, "gamma_raw"):
268	            loss = loss + l2_lambda * (model.gamma_raw ** 2).mean()
269	
270	        if torch.isnan(loss):
271	            logger.warning("NaN loss at epoch %d, restoring best state", epoch)
272	            if best_state is not None:
273	                model.load_state_dict(best_state)
274	            break
275	
276	        loss.backward()
277	        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=5.0)
278	        optimizer.step()
279	
280	        loss_val = loss.item()
281	        scheduler.step(loss_val)
282	
283	        if loss_val < best_loss:
284	            best_loss = loss_val
285	            best_state = {k: v.clone() for k, v in model.state_dict().items()}
286	            patience_counter = 0
287	        else:
288	            patience_counter += 1
289	
290	        if abs(prev_loss - loss_val) < tol and epoch > 100:
291	            logger.info("Converged at epoch %d (loss=%.6f)", epoch, loss_val)
292	            break
293	
294	        if patience_counter > 500:
295	            logger.info("Early stopping at epoch %d (best_loss=%.6f)", epoch, best_loss)
296	            break
297	
298	        prev_loss = loss_val
299	
300	        if epoch % 500 == 0:
301	            logger.info("Epoch %d: loss=%.6f, lr=%.2e", epoch, loss_val,
302	                        optimizer.param_groups[0]["lr"])
303	
304	    if best_state is not None:
305	        model.load_state_dict(best_state)
306	
307	    return {"final_loss": best_loss, "epochs": epoch + 1}
308	
309	
310	def compute_standard_errors(model: nn.Module, responses: torch.Tensor,
311	                            mask: torch.Tensor) -> dict:
312	    ses = {}
313	    eps = 1e-4
314	
315	    for name, param in model.named_parameters():
316	        if name in ("theta", "gamma_raw", "b"):
317	            se = torch.zeros_like(param)
318	            original = param.data.clone()
319	
320	            for i in range(param.shape[0]):
321	                losses = []
322	                for delta in [-eps, 0, eps]:
323	                    param.data[i] = original[i] + delta
324	                    with torch.no_grad():
325	                        probs = model()
326	                        log_lik = (
327	                            responses * torch.log(probs) +
328	                            (1 - responses) * torch.log(1 - probs)
329	                        )
330	                        nll = -(log_lik * mask).sum()
331	                    losses.append(nll.item())
332	
333	                hessian_diag = (losses[2] - 2 * losses[1] + losses[0]) / (eps ** 2)
334	                se[i] = 1.0 / math.sqrt(max(hessian_diag, 1e-8))
335	                param.data[i] = original[i]
336	
337	            ses[name] = se.numpy()
338	
339	    return ses
340	
341	
342	# ── Main Pipeline ──
343	
344	def run_2pl(responses: np.ndarray, mask: np.ndarray) -> dict:
345	    J, I = responses.shape
346	    resp_t = torch.tensor(responses, dtype=torch.float32)
347	    mask_t = torch.tensor(mask, dtype=torch.float32)
348	
349	    model = IRT2PL(J, I)
350	    fit_info = fit_irt_model(model, resp_t, mask_t, lr=0.005)
351	
352	    ses = compute_standard_errors(model, resp_t, mask_t)
353	
354	    with torch.no_grad():
355	        theta = model.theta.numpy()
356	        a = model.a.numpy()
357	        b = model.b.numpy()
358	
359	    theta_se = ses.get("theta", np.full(J, np.nan))
360	    b_se = ses.get("b", np.full(I, np.nan))
361	
362	    return {
363	        "model": "2PL",
364	        "fit": fit_info,
365	        "theta": theta.tolist(),
366	        "theta_se": theta_se.tolist(),
367	        "theta_ci_95": [
368	            [float(theta[j] - 1.96 * theta_se[j]), float(theta[j] + 1.96 * theta_se[j])]
369	            for j in range(J)
370	        ],
371	        "items": {
372	            "a": a.tolist(),
373	            "b": b.tolist(),
374	            "b_se": b_se.tolist(),
375	        },
376	    }
377	
378	
379	def run_4pl_gamma(responses: np.ndarray, mask: np.ndarray,
380	                  tau: np.ndarray, dosages: np.ndarray) -> dict:
381	    J, I = responses.shape
382	    resp_t = torch.tensor(responses, dtype=torch.float32)
383	    mask_t = torch.tensor(mask, dtype=torch.float32)
384	    tau_t = torch.tensor(tau, dtype=torch.float32)
385	    dos_t = torch.tensor(dosages, dtype=torch.float32)
386	
387	    model = IRT4PLGamma(J, I, tau_t, dos_t)
388	    fit_info = fit_irt_model(model, resp_t, mask_t, lr=0.005, max_iter=8000)
389	
390	    ses = compute_standard_errors(model, resp_t, mask_t)
391	
392	    with torch.no_grad():
393	        theta = model.theta.numpy()
394	        gamma = model.gamma.numpy()
395	        a = model.a.numpy()
396	        b = model.b.numpy()
397	        c = model.c.numpy()
398	        d = model.d.numpy()
399	
400	    theta_se = ses.get("theta", np.full(J, np.nan))
401	    gamma_se = ses.get("gamma_raw", np.full(J, np.nan))
402	    b_se = ses.get("b", np.full(I, np.nan))
403	
404	    raw_accuracy = (responses * mask).sum(axis=1) / mask.sum(axis=1)
405	    calibrated_theta = theta
406	
407	    return {
408	        "model": "4PL+gamma",
409	        "fit": fit_info,
410	        "theta": theta.tolist(),
411	        "theta_se": theta_se.tolist(),
412	        "theta_ci_95": [
413	            [float(theta[j] - 1.96 * theta_se[j]), float(theta[j] + 1.96 * theta_se[j])]
414	            for j in range(J)
415	        ],
416	        "gamma": gamma.tolist(),
417	        "gamma_se": gamma_se.tolist(),
418	        "gamma_ci_95": [
419	            [float(gamma[j] - 1.96 * gamma_se[j]), float(gamma[j] + 1.96 * gamma_se[j])]
420	            for j in range(J)
421	        ],
422	        "raw_accuracy": raw_accuracy.tolist(),
423	        "calibrated_theta": calibrated_theta.tolist(),
424	        "items": {
425	            "a": a.tolist(),
426	            "b": b.tolist(),
427	            "b_se": b_se.tolist(),
428	            "c": c.tolist(),
429	            "d": d.tolist(),
430	        },
431	    }
432	
433	
434	def generate_synthetic_data(n_persons: int = 15, n_items: int = 50,
435	                            seed: int = 42) -> dict:
436	    rng = np.random.default_rng(seed)
437	
438	    dosages = np.array([0, 0, 0, 5, 5, 5, 25, 25, 25, 50, 50, 50, 100, 100, 100],
439	                       dtype=np.float32)[:n_persons]
440	    true_theta = rng.normal(0, 1, n_persons).astype(np.float32)
441	    true_gamma = (dosages / 100.0 * rng.uniform(0.5, 1.5, n_persons)).astype(np.float32)
442	    tau = rng.uniform(0.2, 1.0, n_items).astype(np.float32)
443	
444	    a = rng.uniform(0.5, 2.0, n_items).astype(np.float32)
445	    b = rng.normal(0, 1, n_items).astype(np.float32)
446	    c = rng.uniform(0.05, 0.25, n_items).astype(np.float32)
447	    d = rng.uniform(0.9, 1.0, n_items).astype(np.float32)
448	
449	    responses = np.zeros((n_persons, n_items), dtype=np.float32)
450	    for j in range(n_persons):
451	        for i in range(n_items):
452	            ability = true_theta[j] - b[i] + true_gamma[j] * tau[i]
453	            prob = c[i] + (d[i] - c[i]) / (1.0 + np.exp(-a[i] * ability))
454	            responses[j, i] = float(rng.random() < prob)
455	
456	    return {
457	        "responses": responses,
458	        "mask": np.ones_like(responses),
459	        "dosages": dosages,
460	        "tau": tau,
461	        "true_params": {
462	            "theta": true_theta.tolist(),
463	            "gamma": true_gamma.tolist(),
464	            "a": a.tolist(),
465	            "b": b.tolist(),
466	            "c": c.tolist(),
467	            "d": d.tolist(),
468	        },
469	    }
470	
471	
472	def main():
473	    parser = argparse.ArgumentParser(
474	        description="IRT parameter estimation for contamination-aware calibration",
475	        formatter_class=argparse.RawDescriptionHelpFormatter,
476	        epilog="""
477	Examples:
478	  # Run on eval results
479	  python run_irt_calibration.py --eval-dir /path/to/eval_results --output-dir ./irt_output
480	
481	  # Run with exposure scores
482	  python run_irt_calibration.py --eval-dir /path/to/eval_results \\
483	      --exposure-file /path/to/exposure_scores.json --output-dir ./irt_output
484	
485	  # Synthetic data test
486	  python run_irt_calibration.py --synthetic --output-dir ./irt_test
487	        """,
488	    )
489	    parser.add_argument("--eval-dir", type=str, default=None,
490	                        help="Directory containing per-model eval subdirectories")
491	    parser.add_argument("--exposure-file", type=str, default=None,
492	                        help="JSON with per-benchmark exposure scores τ_i")
493	    parser.add_argument("--benchmarks", type=str, nargs="+", default=None,
494	                        help="Benchmarks to analyze (default: all found)")
495	    parser.add_argument("--output-dir", type=str, required=True,
496	                        help="Output directory for IRT results")
497	    parser.add_argument("--synthetic", action="store_true",
498	                        help="Run on synthetic data for validation")
499	    parser.add_argument("--seed", type=int, default=42)
500	    parser.add_argument("--lr", type=float, default=0.01, help="Learning rate")
501	    parser.add_argument("--max-iter", type=int, default=5000, help="Max optimization iterations")
502	    args = parser.parse_args()
503	
504	    logging.basicConfig(
505	        level=logging.INFO,
506	        format="%(asctime)s [%(levelname)s] %(message)s",
507	    )
508	    torch.manual_seed(args.seed)
509	    np.random.seed(args.seed)
510	
511	    output_dir = Path(args.output_dir)
512	    output_dir.mkdir(parents=True, exist_ok=True)
513	
514	    if args.synthetic:
515	        logger.info("Running synthetic data validation")
516	        synth = generate_synthetic_data()
517	        responses = synth["responses"]
518	        mask = synth["mask"]
519	        dosages = synth["dosages"]
520	        tau = synth["tau"]
521	
522	        logger.info("Response matrix: %d persons x %d items", *responses.shape)
523	        logger.info("Mean accuracy: %.3f", responses.mean())
524	
525	        logger.info("Fitting 2PL model...")
526	        result_2pl = run_2pl(responses, mask)
527	
528	        logger.info("Fitting 4PL+gamma model...")
529	        result_4plg = run_4pl_gamma(responses, mask, tau, dosages)
530	
531	        true = synth["true_params"]
532	        theta_corr_2pl = float(np.corrcoef(true["theta"], result_2pl["theta"])[0, 1])
533	        theta_corr_4plg = float(np.corrcoef(true["theta"], result_4plg["theta"])[0, 1])
534	        gamma_corr = float(np.corrcoef(true["gamma"], result_4plg["gamma"])[0, 1])
535	
536	        recovery = {
537	            "theta_corr_2pl": theta_corr_2pl,
538	            "theta_corr_4plg": theta_corr_4plg,
539	            "gamma_corr_4plg": gamma_corr,
540	        }
541	        logger.info("Recovery -- theta corr (2PL): %.4f, theta corr (4PL+g): %.4f, gamma corr: %.4f",
542	                     theta_corr_2pl, theta_corr_4plg, gamma_corr)
543	
544	        output = {
545	            "mode": "synthetic",
546	            "n_persons": int(responses.shape[0]),
547	            "n_items": int(responses.shape[1]),
548	            "true_params": true,
549	            "results_2pl": result_2pl,
550	            "results_4plg": result_4plg,
551	            "recovery": recovery,
552	        }
553	
554	        out_file = output_dir / "synthetic_validation.json"
555	        with open(out_file, "w") as f:
556	            json.dump(output, f, indent=2)
557	        logger.info("Saved to %s", out_file)
558	        return
559	
560	    # ── Real data mode ──
561	    if not args.eval_dir:
562	        parser.error("--eval-dir is required when not using --synthetic")
563	
564	    data = load_eval_results(args.eval_dir, args.benchmarks)
565	    exposure = load_exposure_scores(args.exposure_file, data["benchmarks"])
566	    dosages = data["dosages"]
567	
568	    all_results = {
569	        "mode": "real",
570	        "eval_dir": args.eval_dir,
571	        "models": [
572	            {"dirname": m["dirname"], "model_name": m["model_name"],
573	             "dosage": m["dosage"], "seed": m["seed"]}
574	            for m in data["models"]
575	        ],
576	        "benchmarks": {},
577	    }
578	
579	    for bench, bench_data in data["benchmarks"].items():
580	        logger.info("=== Benchmark: %s (%d persons x %d items) ===",
581	                     bench, bench_data["responses"].shape[0], bench_data["n_items"])
582	
583	        responses = bench_data["responses"]
584	        mask = bench_data["mask"]
585	        tau = exposure[bench]
586	
587	        logger.info("Mean accuracy: %.3f", (responses * mask).sum() / mask.sum())
588	
589	        logger.info("Fitting 2PL...")
590	        result_2pl = run_2pl(responses, mask)
591	
592	        logger.info("Fitting 4PL+gamma...")
593	        result_4plg = run_4pl_gamma(responses, mask, tau, dosages)
594	
595	        all_results["benchmarks"][bench] = {
596	            "n_items": int(bench_data["n_items"]),
597	            "results_2pl": result_2pl,
598	            "results_4plg": result_4plg,
599	        }
600	
601	        logger.info("Per-model estimates:")
602	        for j, m in enumerate(data["models"]):
603	            logger.info(
604	                "  %s: dosage=%d, theta_2pl=%.3f, theta_4plg=%.3f, gamma=%.3f, raw_acc=%.3f",
605	                m["dirname"], m["dosage"],
606	                result_2pl["theta"][j], result_4plg["theta"][j],
607	                result_4plg["gamma"][j], result_4plg["raw_accuracy"][j],
608	            )
609	
610	    out_file = output_dir / "irt_results.json"
611	    with open(out_file, "w") as f:
612	        json.dump(all_results, f, indent=2)
613	    logger.info("Results saved to %s", out_file)
614	
615	
616	if __name__ == "__main__":
617	    main()
618	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "03058026-5196-4c97-b33c-44e244cc821a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006/run_irt_calibration.py",
      "content": "\"\"\"\nIRT parameter estimation for contamination-aware calibration.\n\nFits two models to item-level correctness data from benchmark evaluations:\n  1) Standard 2PL IRT (baseline)\n  2) 4PL+γ contamination-aware IRT\n\nInput:\n  --eval-dir      Directory containing per-model eval subdirectories\n                  (each with eval_results.json / correctness_matrix.json)\n  --exposure-file (optional) JSON mapping benchmark -> [τ_i, ...] exposure scores\n  --benchmarks    Which benchmarks to analyze (default: all found)\n  --output-dir    Where to write results JSON\n\nOutput (per benchmark):\n  irt_results.json with θ, γ, item params, calibrated scores, CIs\n\nDependencies: torch, numpy, scipy\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport math\nimport os\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom scipy import stats\n\nlogger = logging.getLogger(__name__)\n\n# ── Data Loading ──\n\nDOSAGE_PATTERN = re.compile(r\"_d(\\d+)_s(\\d+)(_para)?$\")\n\n\ndef parse_model_dir_name(dirname: str) -> dict | None:\n    \"\"\"Extract model name, dosage, seed from directory like qwen2.5-0.5b_d025_s123.\"\"\"\n    m = DOSAGE_PATTERN.search(dirname)\n    if not m:\n        return None\n    dosage = int(m.group(1))\n    seed = int(m.group(2))\n    is_para = m.group(3) is not None\n    model_name = dirname[: m.start()]\n    return {\n        \"dirname\": dirname,\n        \"model_name\": model_name,\n        \"dosage\": dosage,\n        \"seed\": seed,\n        \"is_para\": is_para,\n    }\n\n\ndef load_eval_results(eval_dir: str, benchmarks: list[str] | None = None,\n                      skip_para: bool = True) -> dict:\n    eval_path = Path(eval_dir)\n    model_dirs = sorted([\n        d for d in eval_path.iterdir()\n        if d.is_dir() and (d / \"eval_results.json\").exists()\n    ])\n\n    models = []\n    for d in model_dirs:\n        info = parse_model_dir_name(d.name)\n        if info is None:\n            logger.warning(\"Skipping unrecognized directory: %s\", d.name)\n            continue\n        if skip_para and info[\"is_para\"]:\n            continue\n        info[\"path\"] = str(d)\n        models.append(info)\n\n    if not models:\n        raise ValueError(f\"No valid eval results found in {eval_dir}\")\n\n    logger.info(\"Found %d model evaluations\", len(models))\n\n    with open(Path(models[0][\"path\"]) / \"eval_results.json\") as f:\n        sample = json.load(f)\n    available_benchmarks = list(sample[\"benchmarks\"].keys())\n\n    if benchmarks:\n        benchmarks = [b for b in benchmarks if b in available_benchmarks]\n    else:\n        benchmarks = available_benchmarks\n\n    logger.info(\"Benchmarks: %s\", benchmarks)\n\n    result = {\"models\": models, \"benchmarks\": {}, \"dosages\": np.array([m[\"dosage\"] for m in models])}\n\n    for bench in benchmarks:\n        responses = []\n        for m in models:\n            results_file = Path(m[\"path\"]) / \"eval_results.json\"\n            with open(results_file) as f:\n                data = json.load(f)\n\n            if bench not in data[\"benchmarks\"]:\n                logger.warning(\"Benchmark %s missing for %s, filling with NaN\", bench, m[\"dirname\"])\n                responses.append(None)\n                continue\n\n            per_item = data[\"benchmarks\"][bench][\"per_item\"]\n            correct = [int(item[\"correct\"]) for item in per_item]\n            responses.append(correct)\n\n        lengths = [len(r) for r in responses if r is not None]\n        if not lengths:\n            logger.warning(\"No data for benchmark %s, skipping\", bench)\n            continue\n\n        n_items = lengths[0]\n        if not all(l == n_items for l in lengths):\n            logger.warning(\"Inconsistent item counts for %s: %s\", bench, lengths)\n            n_items = min(lengths)\n\n        matrix = np.zeros((len(models), n_items), dtype=np.float32)\n        mask = np.ones((len(models), n_items), dtype=np.float32)\n        for j, r in enumerate(responses):\n            if r is None:\n                mask[j, :] = 0.0\n            else:\n                matrix[j, :n_items] = r[:n_items]\n\n        result[\"benchmarks\"][bench] = {\n            \"responses\": matrix,\n            \"mask\": mask,\n            \"n_items\": n_items,\n        }\n\n    return result\n\n\ndef load_exposure_scores(exposure_file: str | None, benchmarks: dict) -> dict:\n    if exposure_file and os.path.exists(exposure_file):\n        with open(exposure_file) as f:\n            raw = json.load(f)\n        scores = {}\n        for bench, bench_data in benchmarks.items():\n            n_items = bench_data[\"n_items\"]\n            if bench in raw:\n                s = np.array(raw[bench], dtype=np.float32)[:n_items]\n                if len(s) < n_items:\n                    s = np.pad(s, (0, n_items - len(s)), constant_values=0.0)\n                scores[bench] = s\n            else:\n                scores[bench] = np.ones(n_items, dtype=np.float32)\n        return scores\n\n    return {bench: np.ones(d[\"n_items\"], dtype=np.float32) for bench, d in benchmarks.items()}\n\n\n# ── IRT Models (PyTorch) ──\n\nclass IRT2PL(nn.Module):\n    \"\"\"Standard 2-parameter logistic IRT model.\"\"\"\n\n    def __init__(self, n_persons: int, n_items: int):\n        super().__init__()\n        self.theta = nn.Parameter(torch.zeros(n_persons))\n        self.a_raw = nn.Parameter(torch.zeros(n_items))\n        self.b = nn.Parameter(torch.zeros(n_items))\n\n    @property\n    def a(self):\n        return torch.exp(self.a_raw).clamp(min=0.1, max=5.0)\n\n    def forward(self):\n        theta = self.theta.unsqueeze(1)\n        a = self.a.unsqueeze(0)\n        b = self.b.unsqueeze(0)\n        logit = a * (theta - b)\n        return torch.sigmoid(logit).clamp(1e-6, 1.0 - 1e-6)\n\n\nclass IRT4PLGamma(nn.Module):\n    \"\"\"\n    4PL + γ contamination-aware IRT model.\n\n    P(Y_ji = 1) = c_i + (d_i - c_i) * σ(a_i * (θ_j - b_i + γ_j * τ_i))\n\n    where γ_j captures contamination advantage proportional to item exposure τ_i.\n    \"\"\"\n\n    def __init__(self, n_persons: int, n_items: int, tau: torch.Tensor,\n                 dosages: torch.Tensor | None = None):\n        super().__init__()\n        self.n_persons = n_persons\n        self.n_items = n_items\n        self.register_buffer(\"tau\", tau)\n\n        self.theta = nn.Parameter(torch.zeros(n_persons))\n        self.gamma_raw = nn.Parameter(torch.zeros(n_persons))\n        self.a_raw = nn.Parameter(torch.zeros(n_items))\n        self.b = nn.Parameter(torch.zeros(n_items))\n        self.c_raw = nn.Parameter(torch.full((n_items,), -2.0))\n        self.d_raw = nn.Parameter(torch.full((n_items,), 2.0))\n\n        if dosages is not None:\n            with torch.no_grad():\n                normed = dosages / (dosages.max() + 1e-8)\n                self.gamma_raw.copy_(normed * 0.5)\n\n    @property\n    def a(self):\n        return torch.exp(self.a_raw).clamp(min=0.1, max=5.0)\n\n    @property\n    def c(self):\n        return torch.sigmoid(self.c_raw).clamp(max=0.5)\n\n    @property\n    def d(self):\n        return (0.5 + 0.5 * torch.sigmoid(self.d_raw))\n\n    @property\n    def gamma(self):\n        return torch.relu(self.gamma_raw)\n\n    def forward(self):\n        theta = self.theta.unsqueeze(1)\n        gamma = self.gamma.unsqueeze(1)\n        tau = self.tau.unsqueeze(0)\n        a = self.a.unsqueeze(0)\n        b = self.b.unsqueeze(0)\n        c = self.c.unsqueeze(0)\n        d = self.d.unsqueeze(0)\n\n        ability = theta - b + gamma * tau\n        logit = a * ability\n        prob = c + (d - c) * torch.sigmoid(logit)\n        return prob.clamp(1e-6, 1.0 - 1e-6)\n\n\n# ── Estimation ──\n\ndef fit_irt_model(model: nn.Module, responses: torch.Tensor, mask: torch.Tensor,\n                  lr: float = 0.01, max_iter: int = 5000, tol: float = 1e-6,\n                  l2_lambda: float = 0.001) -> dict:\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr)\n    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(\n        optimizer, patience=200, factor=0.5, min_lr=1e-5\n    )\n\n    prev_loss = float(\"inf\")\n    best_loss = float(\"inf\")\n    best_state = None\n    patience_counter = 0\n\n    for epoch in range(max_iter):\n        optimizer.zero_grad()\n        probs = model()\n\n        log_lik = (\n            responses * torch.log(probs) + (1 - responses) * torch.log(1 - probs)\n        )\n        loss = -(log_lik * mask).sum() / mask.sum()\n\n        if hasattr(model, \"theta\"):\n            loss = loss + l2_lambda * (model.theta ** 2).mean()\n        if hasattr(model, \"gamma_raw\"):\n            loss = loss + l2_lambda * (model.gamma_raw ** 2).mean()\n\n        if torch.isnan(loss):\n            logger.warning(\"NaN loss at epoch %d, restoring best state\", epoch)\n            if best_state is not None:\n                model.load_state_dict(best_state)\n            break\n\n        loss.backward()\n        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=5.0)\n        optimizer.step()\n\n        loss_val = loss.item()\n        scheduler.step(loss_val)\n\n        if loss_val < best_loss:\n            best_loss = loss_val\n            best_state = {k: v.clone() for k, v in model.state_dict().items()}\n            patience_counter = 0\n        else:\n            patience_counter += 1\n\n        if abs(prev_loss - loss_val) < tol and epoch > 100:\n            logger.info(\"Converged at epoch %d (loss=%.6f)\", epoch, loss_val)\n            break\n\n        if patience_counter > 500:\n            logger.info(\"Early stopping at epoch %d (best_loss=%.6f)\", epoch, best_loss)\n            break\n\n        prev_loss = loss_val\n\n        if epoch % 500 == 0:\n            logger.info(\"Epoch %d: loss=%.6f, lr=%.2e\", epoch, loss_val,\n                        optimizer.param_groups[0][\"lr\"])\n\n    if best_state is not None:\n        model.load_state_dict(best_state)\n\n    return {\"final_loss\": best_loss, \"epochs\": epoch + 1}\n\n\ndef compute_standard_errors(model: nn.Module, responses: torch.Tensor,\n                            mask: torch.Tensor) -> dict:\n    ses = {}\n    eps = 1e-4\n\n    for name, param in model.named_parameters():\n        if name in (\"theta\", \"gamma_raw\", \"b\"):\n            se = torch.zeros_like(param)\n            original = param.data.clone()\n\n            for i in range(param.shape[0]):\n                losses = []\n                for delta in [-eps, 0, eps]:\n                    param.data[i] = original[i] + delta\n                    with torch.no_grad():\n                        probs = model()\n                        log_lik = (\n                            responses * torch.log(probs) +\n                            (1 - responses) * torch.log(1 - probs)\n                        )\n                        nll = -(log_lik * mask).sum()\n                    losses.append(nll.item())\n\n                hessian_diag = (losses[2] - 2 * losses[1] + losses[0]) / (eps ** 2)\n                se[i] = 1.0 / math.sqrt(max(hessian_diag, 1e-8))\n                param.data[i] = original[i]\n\n            ses[name] = se.numpy()\n\n    return ses\n\n\n# ── Main Pipeline ──\n\ndef run_2pl(responses: np.ndarray, mask: np.ndarray) -> dict:\n    J, I = responses.shape\n    resp_t = torch.tensor(responses, dtype=torch.float32)\n    mask_t = torch.tensor(mask, dtype=torch.float32)\n\n    model = IRT2PL(J, I)\n    fit_info = fit_irt_model(model, resp_t, mask_t, lr=0.005)\n\n    ses = compute_standard_errors(model, resp_t, mask_t)\n\n    with torch.no_grad():\n        theta = model.theta.numpy()\n        a = model.a.numpy()\n        b = model.b.numpy()\n\n    theta_se = ses.get(\"theta\", np.full(J, np.nan))\n    b_se = ses.get(\"b\", np.full(I, np.nan))\n\n    return {\n        \"model\": \"2PL\",\n        \"fit\": fit_info,\n        \"theta\": theta.tolist(),\n        \"theta_se\": theta_se.tolist(),\n        \"theta_ci_95\": [\n            [float(theta[j] - 1.96 * theta_se[j]), float(theta[j] + 1.96 * theta_se[j])]\n            for j in range(J)\n        ],\n        \"items\": {\n            \"a\": a.tolist(),\n            \"b\": b.tolist(),\n            \"b_se\": b_se.tolist(),\n        },\n    }\n\n\ndef run_4pl_gamma(responses: np.ndarray, mask: np.ndarray,\n                  tau: np.ndarray, dosages: np.ndarray) -> dict:\n    J, I = responses.shape\n    resp_t = torch.tensor(responses, dtype=torch.float32)\n    mask_t = torch.tensor(mask, dtype=torch.float32)\n    tau_t = torch.tensor(tau, dtype=torch.float32)\n    dos_t = torch.tensor(dosages, dtype=torch.float32)\n\n    model = IRT4PLGamma(J, I, tau_t, dos_t)\n    fit_info = fit_irt_model(model, resp_t, mask_t, lr=0.005, max_iter=8000)\n\n    ses = compute_standard_errors(model, resp_t, mask_t)\n\n    with torch.no_grad():\n        theta = model.theta.numpy()\n        gamma = model.gamma.numpy()\n        a = model.a.numpy()\n        b = model.b.numpy()\n        c = model.c.numpy()\n        d = model.d.numpy()\n\n    theta_se = ses.get(\"theta\", np.full(J, np.nan))\n    gamma_se = ses.get(\"gamma_raw\", np.full(J, np.nan))\n    b_se = ses.get(\"b\", np.full(I, np.nan))\n\n    raw_accuracy = (responses * mask).sum(axis=1) / mask.sum(axis=1)\n    calibrated_theta = theta\n\n    return {\n        \"model\": \"4PL+gamma\",\n        \"fit\": fit_info,\n        \"theta\": theta.tolist(),\n        \"theta_se\": theta_se.tolist(),\n        \"theta_ci_95\": [\n            [float(theta[j] - 1.96 * theta_se[j]), float(theta[j] + 1.96 * theta_se[j])]\n            for j in range(J)\n        ],\n        \"gamma\": gamma.tolist(),\n        \"gamma_se\": gamma_se.tolist(),\n        \"gamma_ci_95\": [\n            [float(gamma[j] - 1.96 * gamma_se[j]), float(gamma[j] + 1.96 * gamma_se[j])]\n            for j in range(J)\n        ],\n        \"raw_accuracy\": raw_accuracy.tolist(),\n        \"calibrated_theta\": calibrated_theta.tolist(),\n        \"items\": {\n            \"a\": a.tolist(),\n            \"b\": b.tolist(),\n            \"b_se\": b_se.tolist(),\n            \"c\": c.tolist(),\n            \"d\": d.tolist(),\n        },\n    }\n\n\ndef generate_synthetic_data(n_persons: int = 15, n_items: int = 50,\n                            seed: int = 42) -> dict:\n    rng = np.random.default_rng(seed)\n\n    dosages = np.array([0, 0, 0, 5, 5, 5, 25, 25, 25, 50, 50, 50, 100, 100, 100],\n                       dtype=np.float32)[:n_persons]\n    true_theta = rng.normal(0, 1, n_persons).astype(np.float32)\n    true_gamma = (dosages / 100.0 * rng.uniform(0.5, 1.5, n_persons)).astype(np.float32)\n    tau = rng.uniform(0.2, 1.0, n_items).astype(np.float32)\n\n    a = rng.uniform(0.5, 2.0, n_items).astype(np.float32)\n    b = rng.normal(0, 1, n_items).astype(np.float32)\n    c = rng.uniform(0.05, 0.25, n_items).astype(np.float32)\n    d = rng.uniform(0.9, 1.0, n_items).astype(np.float32)\n\n    responses = np.zeros((n_persons, n_items), dtype=np.float32)\n    for j in range(n_persons):\n        for i in range(n_items):\n            ability = true_theta[j] - b[i] + true_gamma[j] * tau[i]\n            prob = c[i] + (d[i] - c[i]) / (1.0 + np.exp(-a[i] * ability))\n            responses[j, i] = float(rng.random() < prob)\n\n    return {\n        \"responses\": responses,\n        \"mask\": np.ones_like(responses),\n        \"dosages\": dosages,\n        \"tau\": tau,\n        \"true_params\": {\n            \"theta\": true_theta.tolist(),\n            \"gamma\": true_gamma.tolist(),\n            \"a\": a.tolist(),\n            \"b\": b.tolist(),\n            \"c\": c.tolist(),\n            \"d\": d.tolist(),\n        },\n    }\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"IRT parameter estimation for contamination-aware calibration\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n        epilog=\"\"\"\nExamples:\n  # Run on eval results\n  python run_irt_calibration.py --eval-dir /path/to/eval_results --output-dir ./irt_output\n\n  # Run with exposure scores\n  python run_irt_calibration.py --eval-dir /path/to/eval_results \\\\\n      --exposure-file /path/to/exposure_scores.json --output-dir ./irt_output\n\n  # Synthetic data test\n  python run_irt_calibration.py --synthetic --output-dir ./irt_test\n        \"\"\",\n    )\n    parser.add_argument(\"--eval-dir\", type=str, default=None,\n                        help=\"Directory containing per-model eval subdirectories\")\n    parser.add_argument(\"--exposure-file\", type=str, default=None,\n                        help=\"JSON with per-benchmark exposure scores τ_i\")\n    parser.add_argument(\"--benchmarks\", type=str, nargs=\"+\", default=None,\n                        help=\"Benchmarks to analyze (default: all found)\")\n    parser.add_argument(\"--output-dir\", type=str, required=True,\n                        help=\"Output directory for IRT results\")\n    parser.add_argument(\"--synthetic\", action=\"store_true\",\n                        help=\"Run on synthetic data for validation\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--lr\", type=float, default=0.01, help=\"Learning rate\")\n    parser.add_argument(\"--max-iter\", type=int, default=5000, help=\"Max optimization iterations\")\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n    torch.manual_seed(args.seed)\n    np.random.seed(args.seed)\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    if args.synthetic:\n        logger.info(\"Running synthetic data validation\")\n        synth = generate_synthetic_data()\n        responses = synth[\"responses\"]\n        mask = synth[\"mask\"]\n        dosages = synth[\"dosages\"]\n        tau = synth[\"tau\"]\n\n        logger.info(\"Response matrix: %d persons x %d items\", *responses.shape)\n        logger.info(\"Mean accuracy: %.3f\", responses.mean())\n\n        logger.info(\"Fitting 2PL model...\")\n        result_2pl = run_2pl(responses, mask)\n\n        logger.info(\"Fitting 4PL+gamma model...\")\n        result_4plg = run_4pl_gamma(responses, mask, tau, dosages)\n\n        true = synth[\"true_params\"]\n        theta_corr_2pl = float(np.corrcoef(true[\"theta\"], result_2pl[\"theta\"])[0, 1])\n        theta_corr_4plg = float(np.corrcoef(true[\"theta\"], result_4plg[\"theta\"])[0, 1])\n        gamma_corr = float(np.corrcoef(true[\"gamma\"], result_4plg[\"gamma\"])[0, 1])\n\n        recovery = {\n            \"theta_corr_2pl\": theta_corr_2pl,\n            \"theta_corr_4plg\": theta_corr_4plg,\n            \"gamma_corr_4plg\": gamma_corr,\n        }\n        logger.info(\"Recovery -- theta corr (2PL): %.4f, theta corr (4PL+g): %.4f, gamma corr: %.4f\",\n                     theta_corr_2pl, theta_corr_4plg, gamma_corr)\n\n        output = {\n            \"mode\": \"synthetic\",\n            \"n_persons\": int(responses.shape[0]),\n            \"n_items\": int(responses.shape[1]),\n            \"true_params\": true,\n            \"results_2pl\": result_2pl,\n            \"results_4plg\": result_4plg,\n            \"recovery\": recovery,\n        }\n\n        out_file = output_dir / \"synthetic_validation.json\"\n        with open(out_file, \"w\") as f:\n            json.dump(output, f, indent=2)\n        logger.info(\"Saved to %s\", out_file)\n        return\n\n    # ── Real data mode ──\n    if not args.eval_dir:\n        parser.error(\"--eval-dir is required when not using --synthetic\")\n\n    data = load_eval_results(args.eval_dir, args.benchmarks)\n    exposure = load_exposure_scores(args.exposure_file, data[\"benchmarks\"])\n    dosages = data[\"dosages\"]\n\n    all_results = {\n        \"mode\": \"real\",\n        \"eval_dir\": args.eval_dir,\n        \"models\": [\n            {\"dirname\": m[\"dirname\"], \"model_name\": m[\"model_name\"],\n             \"dosage\": m[\"dosage\"], \"seed\": m[\"seed\"]}\n            for m in data[\"models\"]\n        ],\n        \"benchmarks\": {},\n    }\n\n    for bench, bench_data in data[\"benchmarks\"].items():\n        logger.info(\"=== Benchmark: %s (%d persons x %d items) ===\",\n                     bench, bench_data[\"responses\"].shape[0], bench_data[\"n_items\"])\n\n        responses = bench_data[\"responses\"]\n        mask = bench_data[\"mask\"]\n        tau = exposure[bench]\n\n        logger.info(\"Mean accuracy: %.3f\", (responses * mask).sum() / mask.sum())\n\n        logger.info(\"Fitting 2PL...\")\n        result_2pl = run_2pl(responses, mask)\n\n        logger.info(\"Fitting 4PL+gamma...\")\n        result_4plg = run_4pl_gamma(responses, mask, tau, dosages)\n\n        all_results[\"benchmarks\"][bench] = {\n            \"n_items\": int(bench_data[\"n_items\"]),\n            \"results_2pl\": result_2pl,\n            \"results_4plg\": result_4plg,\n        }\n\n        logger.info(\"Per-model estimates:\")\n        for j, m in enumerate(data[\"models\"]):\n            logger.info(\n                \"  %s: dosage=%d, theta_2pl=%.3f, theta_4plg=%.3f, gamma=%.3f, raw_acc=%.3f\",\n                m[\"dirname\"], m[\"dosage\"],\n                result_2pl[\"theta\"][j], result_4plg[\"theta\"][j],\n                result_4plg[\"gamma\"][j], result_4plg[\"raw_accuracy\"][j],\n            )\n\n    out_file = output_dir / \"irt_results.json\"\n    with open(out_file, \"w\") as f:\n        json.dump(all_results, f, indent=2)\n    logger.info(\"Results saved to %s\", out_file)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 618,
      "startLine": 1,
      "totalLines": 618
    }
  }
}
```

</details>

---

### Assistant

_source line 76_

<details><summary>Logged reasoning block</summary>

```text
Now I see that `run_irt_calibration.py` is a PyTorch-based MLE pipeline. But the imports in `run_pooled_4bench_irt.py` and `run_stratified_irt.py` reference functions like `load_pooled_eval_results`, `prepare_stan_data`, `fit_stan_model`, `check_convergence`, `posterior_predictive_check`, `extract_results`, and `STAN_MODELS`, which are NOT in the local copy of `run_irt_calibration.py`.

This means the remote `run_irt_calibration.py` at `/root/contamcal-irt-calibration/exp006/run_irt_calibration.py` has been updated with additional functions (Stan-based) since the local copy was last synced.


I need to check the remote version to understand what functions are actually available there, then modify the local scripts accordingly to work with the remote implementation. stratify-by-scale`
3. Then sync to remote

But wait, the local `run_irt_calibration.py` at `artifacts/exp006/run_irt_calibration.py` doesn't have `load_pooled_eval_results`, `prepare_stan_data`, etc. These must be in the remote version. Let me SSH to check.

Actually, let me also look at `run_stratified_irt.py` more carefully. It already does exactly what we need (Scheme B = per-scale IRT). The question is whether to:
A. Modify `run_pooled_4bench_irt.py` to add `--stratify-by-scale`
B. Modify `run_stratified_irt.py` to improve its output format

Since the task specifically asks to add `--stratify-by-scale`, I think option A is correct. But I need to check the remote version to see what functions are actually available in `run_irt_calibration`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "8633c626-a9b8-41bd-a55b-327037c6caf3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F24PR4fkw8FhW4R7pdx9QV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8362,
      "cache_read_input_tokens": 53171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8362
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

_source line 77_

The local `run_irt_calibration.py` doesn't have the Stan-based functions that both scripts import. Need to check the remote version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "9ebf98be-01ea-40a7-99a5-b5eb29641b5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F24PR4fkw8FhW4R7pdx9QV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8362,
      "cache_read_input_tokens": 53171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8362
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

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MyicGJEApgsdmCeb9kqhJP`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "5e89f962-db52-432c-8b12-77c64770bedf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F24PR4fkw8FhW4R7pdx9QV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8362,
      "cache_read_input_tokens": 53171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8362
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

### Tool result

_source line 79 · 2026-05-16T05:31:06.187Z_

<details><summary>↩ Tool result · `toolu_01MyicGJEApgsdmCeb9kqhJP`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "3b85a652-3798-443f-8fee-03db79a6fe7c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013TGmYhkyXieJYpxprHZVze`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -100 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "371cc182-7ed9-4e9d-a3b0-20e5d8934d5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YdUroosCdSKgduXbPrXsq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 61533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1160
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

_source line 81 · 2026-05-16T05:31:10.299Z_

<details><summary>↩ Tool result · `toolu_013TGmYhkyXieJYpxprHZVze`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nIRT calibration for contamination-aware benchmark score correction.\\nFits 4PL+gamma IRT model via CmdStanPy MCMC (NUTS) per benchmark.\\n\\nInput:\\n  - Correctness matrix (N_models x N_items): binary 0/1\\n  - Exposure matrix (N_models x N_items): continuous exposure scores\\n  OR\\n  - eval-dir with per-model eval results + per-benchmark exposure scores\\n\\nOutput (per benchmark):\\n  - Posterior: gamma, theta, item params (a, b, c, d)\\n  - Calibrated scores (exposure=0 counterfactual) with 50/80/95% CIs\\n  - Convergence diagnostics (Rhat, ESS, divergences)\\n  - Posterior predictive checks\\n\\nDependencies: cmdstanpy (CmdStan 2.38+), numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport cmdstanpy\\n\\nlog = logging.getLogger(__name__)\\n\\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\\nSTAN_MODEL_DIR = \\\"/root/contamcal-irt-calibration/stan_models\\\"\\nSTAN_MODELS = {\\n    \\\"4pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple.stan\\\"),\\n    \\\"2pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_2pl_gamma.stan\\\"),\\n    \\\"vanilla_4pl\\\": os.path.join(STAN_MODEL_DIR, \\\"vanilla_4pl.stan\\\"),\\n    \\\"4pl_gamma_wider\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple_wider.stan\\\"),\\n}\\n\\nDOSAGE_PATTERN = re.compile(r\\\"_d(\\\\d+)(?:_v\\\\d+)?_s(\\\\d+)(_para)?(_aligned)?(?:_v\\\\d+)?$\\\")\\n\\n\\n# ── Data Loading ──\\n\\ndef parse_model_dir_name(dirname):\\n    \\\"\\\"\\\"Extract model name, dosage, seed from directory like Qwen2.5-0.5B_d025_s42.\\\"\\\"\\\"\\n    m = DOSAGE_PATTERN.search(dirname)\\n    if not m:\\n        return None\\n    return {\\n        \\\"dirname\\\": dirname,\\n        \\\"model_name\\\": dirname[:m.start()],\\n        \\\"dosage\\\": int(m.group(1)),\\n        \\\"seed\\\": int(m.group(2)),\\n        \\\"is_para\\\": m.group(3) is not None,\\n        \\\"is_aligned\\\": m.group(4) is not None,\\n    }\\n\\n\\ndef get_train_lr(dirname, checkpoint_dir):\\n    \\\"\\\"\\\"Read lr from checkpoint's train_config.json (D076).\\\"\\\"\\\"\\n    ckpt_name = re.sub(r'(_para)?(_aligned)?$', '', dirname)\\n    config_path = os.path.join(checkpoint_dir, ckpt_name, \\\"train_config.json\\\")\\n    try:\\n        with open(config_path) as f:\\n            return json.load(f).get(\\\"lr\\\")\\n    except (FileNotFoundError, json.JSONDecodeError):\\n        pass\\n    # Fallback: eval dir may have version suffix not in checkpoint name\\n    ckpt_fallback = re.sub(r'_v\\\\d+(?=_s\\\\d+$)', '', ckpt_name)\\n    if ckpt_fallback != ckpt_name:\\n        config_path = os.path.join(checkpoint_dir, ckpt_fallback, \\\"train_config.json\\\")\\n        try:\\n            with open(config_path) as f:\\n                return json.load(f).get(\\\"lr\\\")\\n        except (FileNotFoundError, json.JSONDecodeError):\\n            pass\\n    return None\\n\\n\\ndef load_matrix(path):\\n    \\\"\\\"\\\"Load matrix from .npy, .csv, or .json.\\\"\\\"\\\"\\n    ext = os.path.splitext(path)[1].lower()\\n    if ext == \\\".npy\\\":\\n        return np.load(path)\\n    elif ext == \\\".csv\\\":\\n        return np.loadtxt(path, delimiter=\\\",\\\", skiprows=1)\\n    elif ext == \\\".json\\\":\\n        with open(path) as f:\\n            return np.array(json.load(f))\\n    raise ValueError(f\\\"Unsupported format: {ext}\\\")\\n\\n\\ndef load_eval_results(eval_dir, benchmarks=None, skip_para=True,\\n                      model_scale=None, seed_filter=None, aligned_only=False,\\n                      lr_filter=None, checkpoint_dir=None):\\n    \\\"\\\"\\\"Load per-model eval results into response matrices per benchmark.\\\"\\\"\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.97}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "18c19013-65ce-4cff-acb4-b6828eb75b6f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nIRT calibration for contamination-aware benchmark score correction.\\\\nFits 4PL+gamma IRT model via CmdStanPy MCMC (NUTS) per benchmark.\\\\n\\\\nInput:\\\\n  - Correctness matrix (N_models x N_items): binary 0/1\\\\n  - Exposure matrix (N_models x N_items): continuous exposure scores\\\\n  OR\\\\n  - eval-dir with per-model eval results + per-benchmark exposure scores\\\\n\\\\nOutput (per benchmark):\\\\n  - Posterior: gamma, theta, item params (a, b, c, d)\\\\n  - Calibrated scores (exposure=0 counterfactual) with 50/80/95% CIs\\\\n  - Convergence diagnostics (Rhat, ESS, divergences)\\\\n  - Posterior predictive checks\\\\n\\\\nDependencies: cmdstanpy (CmdStan 2.38+), numpy, scipy\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport re\\\\nimport sys\\\\nimport time\\\\nfrom pathlib import Path\\\\n\\\\nimport numpy as np\\\\nimport cmdstanpy\\\\n\\\\nlog = logging.getLogger(__name__)\\\\n\\\\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\\\\nSTAN_MODEL_DIR = \\\\\\\"/root/contamcal-irt-calibration/stan_models\\\\\\\"\\\\nSTAN_MODELS = {\\\\n    \\\\\\\"4pl_gamma\\\\\\\": os.path.join(STAN_MODEL_DIR, \\\\\\\"contam_irt_4pl_simple.stan\\\\\\\"),\\\\n    \\\\\\\"2pl_gamma\\\\\\\": os.path.join(STAN_MODEL_DIR, \\\\\\\"contam_irt_2pl_gamma.stan\\\\\\\"),\\\\n    \\\\\\\"vanilla_4pl\\\\\\\": os.path.join(STAN_MODEL_DIR, \\\\\\\"vanilla_4pl.stan\\\\\\\"),\\\\n    \\\\\\\"4pl_gamma_wider\\\\\\\": os.path.join(STAN_MODEL_DIR, \\\\\\\"contam_irt_4pl_simple_wider.stan\\\\\\\"),\\\\n}\\\\n\\\\nDOSAGE_PATTERN = re.compile(r\\\\\\\"_d(\\\\\\\\d+)(?:_v\\\\\\\\d+)?_s(\\\\\\\\d+)(_para)?(_aligned)?(?:_v\\\\\\\\d+)?$\\\\\\\")\\\\n\\\\n\\\\n# ── Data Loading ──\\\\n\\\\ndef parse_model_dir_name(dirname):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Extract model name, dosage, seed from directory like Qwen2.5-0.5B_d025_s42.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    m = DOSAGE_PATTERN.search(dirname)\\\\n    if not m:\\\\n        return None\\\\n    return {\\\\n        \\\\\\\"dirname\\\\\\\": dirname,\\\\n        \\\\\\\"model_name\\\\\\\": dirname[:m.start()],\\\\n        \\\\\\\"dosage\\\\\\\": int(m.group(1)),\\\\n        \\\\\\\"seed\\\\\\\": int(m.group(2)),\\\\n        \\\\\\\"is_para\\\\\\\": m.group(3) is not None,\\\\n        \\\\\\\"is_aligned\\\\\\\": m.group(4) is not None,\\\\n    }\\\\n\\\\n\\\\ndef get_train_lr(dirname, checkpoint_dir):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Read lr from checkpoint's train_config.json (D076).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    ckpt_name = re.sub(r'(_para)?(_aligned)?$', '', dirname)\\\\n    config_path = os.path.join(checkpoint_dir, ckpt_name, \\\\\\\"train_config.json\\\\\\\")\\\\n    try:\\\\n        with open(config_path) as f:\\\\n            return json.load(f).get(\\\\\\\"lr\\\\\\\")\\\\n    except (FileNotFoundError, json.JSONDecodeError):\\\\n        pass\\\\n    # Fallback: eval dir may have version suffix not in checkpoint name\\\\n    ckpt_fallback = re.sub(r'_v\\\\\\\\d+(?=_s\\\\\\\\d+$)', '', ckpt_name)\\\\n    if ckpt_fallback != ckpt_name:\\\\n        config_path = os.path.join(checkpoint_dir, ckpt_fallback, \\\\\\\"train_config.json\\\\\\\")\\\\n        try:\\\\n            with open(config_path) as f:\\\\n                return json.load(f).get(\\\\\\\"lr\\\\\\\")\\\\n        except (FileNotFoundError, json.JSONDecodeError):\\\\n            pass\\\\n    return None\\\\n\\\\n\\\\ndef load_matrix(path):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load matrix from .npy, .csv, or .json.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    ext = os.path.splitext(path)[1].lower()\\\\n    if ext == \\\\\\\".npy\\\\\\\":\\\\n        return np.load(path)\\\\n    elif ext == \\\\\\\".csv\\\\\\\":\\\\n        return np.loadtxt(path, delimiter=\\\\\\\",\\\\\\\", skiprows=1)\\\\n    elif ext == \\\\\\\".json\\\\\\\":\\\\n        with open(path) as f:\\\\n            return np.array(json.load(f))\\\\n    raise ValueError(f\\\\\\\"Unsupported format: {ext}\\\\\\\")\\\\n\\\\n\\\\ndef load_eval_results(eval_dir, benchmarks=None, skip_para=True,\\\\n                      model_scale=None, seed_filter=None, aligned_only=False,\\\\n                      lr_filter=None, checkpoint_dir=None):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load per-model eval results into response matrices per benchmark.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.97}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nIRT calibration for contamination-aware benchmark score correction.\\nFits 4PL+gamma IRT model via CmdStanPy MCMC (NUTS) per benchmark.\\n\\nInput:\\n  - Correctness matrix (N_models x N_items): binary 0/1\\n  - Exposure matrix (N_models x N_items): continuous exposure scores\\n  OR\\n  - eval-dir with per-model eval results + per-benchmark exposure scores\\n\\nOutput (per benchmark):\\n  - Posterior: gamma, theta, item params (a, b, c, d)\\n  - Calibrated scores (exposure=0 counterfactual) with 50/80/95% CIs\\n  - Convergence diagnostics (Rhat, ESS, divergences)\\n  - Posterior predictive checks\\n\\nDependencies: cmdstanpy (CmdStan 2.38+), numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport cmdstanpy\\n\\nlog = logging.getLogger(__name__)\\n\\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\\nSTAN_MODEL_DIR = \\\"/root/contamcal-irt-calibration/stan_models\\\"\\nSTAN_MODELS = {\\n    \\\"4pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple.stan\\\"),\\n    \\\"2pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_2pl_gamma.stan\\\"),\\n    \\\"vanilla_4pl\\\": os.path.join(STAN_MODEL_DIR, \\\"vanilla_4pl.stan\\\"),\\n    \\\"4pl_gamma_wider\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple_wider.stan\\\"),\\n}\\n\\nDOSAGE_PATTERN = re.compile(r\\\"_d(\\\\d+)(?:_v\\\\d+)?_s(\\\\d+)(_para)?(_aligned)?(?:_v\\\\d+)?$\\\")\\n\\n\\n# ── Data Loading ──\\n\\ndef parse_model_dir_name(dirname):\\n    \\\"\\\"\\\"Extract model name, dosage, seed from directory like Qwen2.5-0.5B_d025_s42.\\\"\\\"\\\"\\n    m = DOSAGE_PATTERN.search(dirname)\\n    if not m:\\n        return None\\n    return {\\n        \\\"dirname\\\": dirname,\\n        \\\"model_name\\\": dirname[:m.start()],\\n        \\\"dosage\\\": int(m.group(1)),\\n        \\\"seed\\\": int(m.group(2)),\\n        \\\"is_para\\\": m.group(3) is not None,\\n        \\\"is_aligned\\\": m.group(4) is not None,\\n    }\\n\\n\\ndef get_train_lr(dirname, checkpoint_dir):\\n    \\\"\\\"\\\"Read lr from checkpoint's train_config.json (D076).\\\"\\\"\\\"\\n    ckpt_name = re.sub(r'(_para)?(_aligned)?$', '', dirname)\\n    config_path = os.path.join(checkpoint_dir, ckpt_name, \\\"train_config.json\\\")\\n    try:\\n        with open(config_path) as f:\\n            return json.load(f).get(\\\"lr\\\")\\n    except (FileNotFoundError, json.JSONDecodeError):\\n        pass\\n    # Fallback: eval dir may have version suffix not in checkpoint name\\n    ckpt_fallback = re.sub(r'_v\\\\d+(?=_s\\\\d+$)', '', ckpt_name)\\n    if ckpt_fallback != ckpt_name:\\n        config_path = os.path.join(checkpoint_dir, ckpt_fallback, \\\"train_config.json\\\")\\n        try:\\n            with open(config_path) as f:\\n                return json.load(f).get(\\\"lr\\\")\\n        except (FileNotFoundError, json.JSONDecodeError):\\n            pass\\n    return None\\n\\n\\ndef load_matrix(path):\\n    \\\"\\\"\\\"Load matrix from .npy, .csv, or .json.\\\"\\\"\\\"\\n    ext = os.path.splitext(path)[1].lower()\\n    if ext == \\\".npy\\\":\\n        return np.load(path)\\n    elif ext == \\\".csv\\\":\\n        return np.loadtxt(path, delimiter=\\\",\\\", skiprows=1)\\n    elif ext == \\\".json\\\":\\n        with open(path) as f:\\n            return np.array(json.load(f))\\n    raise ValueError(f\\\"Unsupported format: {ext}\\\")\\n\\n\\ndef load_eval_results(eval_dir, benchmarks=None, skip_para=True,\\n                      model_scale=None, seed_filter=None, aligned_only=False,\\n                      lr_filter=None, checkpoint_dir=None):\\n    \\\"\\\"\\\"Load per-model eval results into response matrices per benchmark.\\\"\\\"\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.97}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01R7rKBgvNchMTgB1FyPRQ7F`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "87d8b8e6-2827-46dd-bb29-324e5aa56a62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112jGJACoKx9i16AHvk2s1E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 62693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1633
      },
      "output_tokens": 64,
      "service_tier": "standard",
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

_source line 83 · 2026-05-16T05:31:13.552Z_

<details><summary>↩ Tool result · `toolu_01R7rKBgvNchMTgB1FyPRQ7F`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"639 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "dababc13-cbbe-4cdf-a88b-5870b91f2c31",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"639 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"639 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MRSd7yBJTV6FDYMFHzAtp5`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"^def \\|^class \" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "32d7b8b2-d6a7-4de4-a88f-dc7e4c233fc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kT34ncCPWFwzyhEmh8e4a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 216,
      "cache_read_input_tokens": 64326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 216
      },
      "output_tokens": 68,
      "service_tier": "standard",
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

_source line 85 · 2026-05-16T05:31:16.874Z_

<details><summary>↩ Tool result · `toolu_01MRSd7yBJTV6FDYMFHzAtp5`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "01fe8c0c-135e-4c5a-bf9d-db1863830ec2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BK3Dad9eZnPe6f8TiXmpov`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"^def \\|^class \" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "6a656b46-7d19-41f4-b6c0-74a010b5c753",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEXLpYdRuwgD2JqSRKF43A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 64542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 214
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

_source line 87 · 2026-05-16T05:31:19.912Z_

<details><summary>↩ Tool result · `toolu_01BK3Dad9eZnPe6f8TiXmpov`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "ca6cd72d-5a63-443b-b0eb-798e34fd9130",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HHwTsPkC8pdsrmwm1WUjjy`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"^def \" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "b762ece5-e315-466c-ae1e-0ca5fafb37a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9w6Bp9VgSw94gMSyKAJQW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 64756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 214
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

_source line 89 · 2026-05-16T05:31:23.300Z_

<details><summary>↩ Tool result · `toolu_01HHwTsPkC8pdsrmwm1WUjjy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"48:def parse_model_dir_name(dirname):\\n63:def get_train_lr(dirname, checkpoint_dir):\\n84:def load_matrix(path):\\n97:def load_eval_results(eval_dir, benchmarks=None, skip_para=True,\\n183:def load_exposure_scores(exposure_file, benchmarks_data, model_id=None):\\n226:def build_exposure_matrix(dosages, tau):\\n232:def load_pooled_eval_results(eval_dir, scales, benchmarks=None,\\n287:def prepare_stan_data(y, exposure, model_type=\\\"4pl_gamma\\\"):\\n300:def fit_stan_model(stan_file, stan_data, chains=4, iter_warmup=1000,\\n330:def check_convergence(fit):\\n365:def posterior_predictive_check(fit, y):\\n386:def _summarize_vector(draws):\\n400:def extract_results(fit, y, model_type):\\n456:def run_benchmark_fit(bench_name, y, exposure, model_type, args, **kwargs):\\n512:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "f9333847-c0fa-4e75-9706-4f53e09fc26b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"48:def parse_model_dir_name(dirname):\\\\n63:def get_train_lr(dirname, checkpoint_dir):\\\\n84:def load_matrix(path):\\\\n97:def load_eval_results(eval_dir, benchmarks=None, skip_para=True,\\\\n183:def load_exposure_scores(exposure_file, benchmarks_data, model_id=None):\\\\n226:def build_exposure_matrix(dosages, tau):\\\\n232:def load_pooled_eval_results(eval_dir, scales, benchmarks=None,\\\\n287:def prepare_stan_data(y, exposure, model_type=\\\\\\\"4pl_gamma\\\\\\\"):\\\\n300:def fit_stan_model(stan_file, stan_data, chains=4, iter_warmup=1000,\\\\n330:def check_convergence(fit):\\\\n365:def posterior_predictive_check(fit, y):\\\\n386:def _summarize_vector(draws):\\\\n400:def extract_results(fit, y, model_type):\\\\n456:def run_benchmark_fit(bench_name, y, exposure, model_type, args, **kwargs):\\\\n512:def main():\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.67}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"48:def parse_model_dir_name(dirname):\\n63:def get_train_lr(dirname, checkpoint_dir):\\n84:def load_matrix(path):\\n97:def load_eval_results(eval_dir, benchmarks=None, skip_para=True,\\n183:def load_exposure_scores(exposure_file, benchmarks_data, model_id=None):\\n226:def build_exposure_matrix(dosages, tau):\\n232:def load_pooled_eval_results(eval_dir, scales, benchmarks=None,\\n287:def prepare_stan_data(y, exposure, model_type=\\\"4pl_gamma\\\"):\\n300:def fit_stan_model(stan_file, stan_data, chains=4, iter_warmup=1000,\\n330:def check_convergence(fit):\\n365:def posterior_predictive_check(fit, y):\\n386:def _summarize_vector(draws):\\n400:def extract_results(fit, y, model_type):\\n456:def run_benchmark_fit(bench_name, y, exposure, model_type, args, **kwargs):\\n512:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XnHTQ1Yd7cMQAYm7DA9oPZ`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -n +232 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "7f305518-6485-438e-8ee5-b974b07586aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTPDgTrwEXrF6EdYjsovzk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 478,
      "cache_read_input_tokens": 64970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 478
      },
      "output_tokens": 64,
      "service_tier": "standard",
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

_source line 91 · 2026-05-16T05:31:26.832Z_

<details><summary>↩ Tool result · `toolu_01XnHTQ1Yd7cMQAYm7DA9oPZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"def load_pooled_eval_results(eval_dir, scales, benchmarks=None,\\n                              lr_filter=None, lr_filter_scales=None,\\n                              checkpoint_dir=None, **kwargs):\\n    \\\"\\\"\\\"Load and merge eval results across multiple model scales.\\n\\n    Calls load_eval_results once per scale, tags each model with its scale,\\n    and stacks response matrices vertically. Items are truncated to the\\n    minimum count across scales for consistency.\\n    \\\"\\\"\\\"\\n    all_models = []\\n    all_dosages = []\\n    bench_accum = {}\\n\\n    for scale in scales:\\n        kw = dict(kwargs)\\n        if lr_filter is not None and checkpoint_dir:\\n            if lr_filter_scales is None or scale in lr_filter_scales:\\n                kw[\\\"lr_filter\\\"] = lr_filter\\n                kw[\\\"checkpoint_dir\\\"] = checkpoint_dir\\n        data = load_eval_results(eval_dir, benchmarks, model_scale=scale, **kw)\\n        log.info(\\\"Pool scale %s: %d models, dosages=%s\\\",\\n                 scale, len(data[\\\"models\\\"]), data[\\\"dosages\\\"].tolist())\\n        for m in data[\\\"models\\\"]:\\n            m[\\\"scale\\\"] = scale\\n        all_models.extend(data[\\\"models\\\"])\\n        all_dosages.extend(data[\\\"dosages\\\"].tolist())\\n\\n        for bench, bd in data[\\\"benchmarks\\\"].items():\\n            if bench not in bench_accum:\\n                bench_accum[bench] = {\\\"n_items\\\": bd[\\\"n_items\\\"],\\n                                      \\\"responses\\\": [], \\\"valid\\\": []}\\n            bench_accum[bench][\\\"n_items\\\"] = min(\\n                bench_accum[bench][\\\"n_items\\\"], bd[\\\"n_items\\\"])\\n            bench_accum[bench][\\\"responses\\\"].append(bd[\\\"responses\\\"])\\n            bench_accum[bench][\\\"valid\\\"].append(bd[\\\"valid_mask\\\"])\\n\\n    result_benchmarks = {}\\n    for bench, acc in bench_accum.items():\\n        ni = acc[\\\"n_items\\\"]\\n        responses = np.vstack([r[:, :ni] for r in acc[\\\"responses\\\"]])\\n        valid = np.concatenate(acc[\\\"valid\\\"])\\n        result_benchmarks[bench] = {\\n            \\\"responses\\\": responses, \\\"n_items\\\": ni, \\\"valid_mask\\\": valid,\\n        }\\n\\n    return {\\n        \\\"models\\\": all_models,\\n        \\\"dosages\\\": np.array(all_dosages),\\n        \\\"benchmarks\\\": result_benchmarks,\\n    }\\n\\n\\n\\n# ── Stan Fitting ──\\n\\ndef prepare_stan_data(y, exposure, model_type=\\\"4pl_gamma\\\"):\\n    \\\"\\\"\\\"Prepare data dict for Stan model.\\\"\\\"\\\"\\n    N_models, N_items = y.shape\\n    data = {\\n        \\\"N_models\\\": int(N_models),\\n        \\\"N_items\\\": int(N_items),\\n        \\\"y\\\": y.astype(int).tolist(),\\n    }\\n    if model_type != \\\"vanilla_4pl\\\":\\n        data[\\\"exposure\\\"] = exposure.tolist()\\n    return data\\n\\n\\ndef fit_stan_model(stan_file, stan_data, chains=4, iter_warmup=1000,\\n                   iter_sampling=1000, adapt_delta=0.95, max_treedepth=12,\\n                   seed=42, parallel_chains=None):\\n    \\\"\\\"\\\"Fit Stan model via CmdStanPy NUTS sampler.\\\"\\\"\\\"\\n    log.info(\\\"Compiling Stan model: %s\\\", os.path.basename(stan_file))\\n    model = cmdstanpy.CmdStanModel(stan_file=stan_file)\\n\\n    log.info(\\\"Fitting: %d models x %d items, %d chains x %d samples\\\",\\n             stan_data[\\\"N_models\\\"], stan_data[\\\"N_items\\\"], chains, iter_sampling)\\n    t0 = time.time()\\n    fit = model.sample(\\n        data=stan_data,\\n        chains=chains,\\n        iter_warmup=iter_warmup,\\n        iter_sampling=iter_sampling,\\n        seed=seed,\\n        adapt_delta=adapt_delta,\\n        max_treedepth=max_treedepth,\\n        parallel_chains=parallel_chains if parallel_chains is not None else min(chains, 4),\\n        show_progress=True,\\n    )\\n    elapsed = time.time() - t0\\n    log.info(\\\"Sampling completed in %.1fs\\\", elapsed)\\n    return fit, elapsed\\n\\n\\n\\n\\n# ── Diagnostics ──\\n\\ndef check_convergence(fit):\\n    \\\"\\\"\\\"Check Rhat, ESS, divergences.\\\"\\\"\\\"\\n    summary = fit.summary()\\n    diag = {}\\n\\n    for col in [\\\"R_hat\\\", \\\"Rhat\\\"]:\\n        if col in summary.columns:\\n            diag[\\\"max_rhat\\\"] = round(float(summary[col].max()), 4)\\n            diag[\\\"rhat_ok\\\"] = diag[\\\"max_rhat\\\"] < 1.01\\n            break\\n\\n    for col in [\\\"ESS_bulk\\\", \\\"N_Eff\\\", \\\"N_eff\\\"]:\\n        if col in summary.columns:\\n            diag[\\\"min_ess\\\"] = round(float(summary[col].min()), 1)\\n        \\n\\n... [截断: 输出过长，省略 7996 字符] ...\\n\\nOnly load aligned-format eval directories.\\\")\\n    parser.add_argument(\\\"--checkpoint-dir\\\", type=str, default=None,\\n                        help=\\\"Checkpoint dir for lr verification (D076)\\\")\\n    parser.add_argument(\\\"--lr-filter\\\", type=float, default=None,\\n                        help=\\\"Only accept checkpoints with this lr (D076)\\\")\\n    parser.add_argument(\\\"--output-dir\\\", type=str, required=True)\\n\\n    parser.add_argument(\\\"--chains\\\", type=int, default=4)\\n    parser.add_argument(\\\"--warmup\\\", type=int, default=1000)\\n    parser.add_argument(\\\"--samples\\\", type=int, default=1000)\\n    parser.add_argument(\\\"--adapt-delta\\\", type=float, default=0.95)\\n    parser.add_argument(\\\"--max-treedepth\\\", type=int, default=12)\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42)\\n\\n    args = parser.parse_args()\\n\\n    logging.basicConfig(level=logging.INFO,\\n                        format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\")\\n\\n    output_dir = Path(args.output_dir)\\n    output_dir.mkdir(parents=True, exist_ok=True)\\n\\n    # Mode 1: direct matrix input\\n    if args.response_matrix:\\n        if not args.exposure_matrix and args.model_type != \\\"vanilla_4pl\\\":\\n            parser.error(\\\"--exposure-matrix required with --response-matrix \\\"\\n                         \\\"(unless --model-type=vanilla_4pl)\\\")\\n        y = load_matrix(args.response_matrix).astype(int)\\n        if args.exposure_matrix:\\n            exposure = load_matrix(args.exposure_matrix)\\n            assert y.shape == exposure.shape, (\\n                f\\\"Shape mismatch: response {y.shape} vs exposure {exposure.shape}\\\")\\n        else:\\n            exposure = np.zeros_like(y, dtype=float)\\n        bench_name = args.benchmark or \\\"benchmark\\\"\\n\\n        result = run_benchmark_fit(bench_name, y, exposure, args.model_type, args)\\n\\n        out_path = output_dir / f\\\"{bench_name}_{args.model_type}_results.json\\\"\\n        with open(out_path, \\\"w\\\") as f:\\n            json.dump(result, f, indent=2)\\n        log.info(\\\"Results saved to %s\\\", out_path)\\n        return\\n\\n    # Mode 2: eval-dir input\\n    if not args.eval_dir:\\n        parser.error(\\\"Specify --eval-dir or --response-matrix\\\")\\n\\n    data = load_eval_results(args.eval_dir, args.benchmarks,\\n                              model_scale=args.model_scale,\\n                              seed_filter=args.data_seed,\\n                              aligned_only=args.aligned_only,\\n                              lr_filter=args.lr_filter,\\n                              checkpoint_dir=args.checkpoint_dir)\\n    exposure_scores = load_exposure_scores(args.exposure_file, data[\\\"benchmarks\\\"],\\n                                           model_id=args.tau_model_id)\\n    dosages = data[\\\"dosages\\\"]\\n\\n    all_results = {\\n        \\\"mode\\\": \\\"eval_dir\\\",\\n        \\\"eval_dir\\\": args.eval_dir,\\n        \\\"model_type\\\": args.model_type,\\n        \\\"models\\\": [\\n            {\\\"dirname\\\": m[\\\"dirname\\\"], \\\"model_name\\\": m[\\\"model_name\\\"],\\n             \\\"dosage\\\": m[\\\"dosage\\\"], \\\"seed\\\": m[\\\"seed\\\"]}\\n            for m in data[\\\"models\\\"]\\n        ],\\n        \\\"benchmarks\\\": {},\\n    }\\n\\n    for bench, bench_data in data[\\\"benchmarks\\\"].items():\\n        responses = bench_data[\\\"responses\\\"]\\n        valid = bench_data[\\\"valid_mask\\\"]\\n        tau = exposure_scores[bench]\\n\\n        if not valid.all():\\n            responses = responses[valid]\\n            dosages_bench = dosages[valid]\\n        else:\\n            dosages_bench = dosages\\n\\n        exposure_matrix = build_exposure_matrix(dosages_bench, tau[:bench_data[\\\"n_items\\\"]])\\n        result = run_benchmark_fit(bench, responses, exposure_matrix, args.model_type, args)\\n        all_results[\\\"benchmarks\\\"][bench] = result\\n\\n        bench_dir = output_dir / bench\\n        bench_dir.mkdir(parents=True, exist_ok=True)\\n        with open(bench_dir / f\\\"{args.model_type}_results.json\\\", \\\"w\\\") as f:\\n            json.dump(result, f, indent=2)\\n\\n    with open(output_dir / \\\"irt_calibration_results.json\\\", \\\"w\\\") as f:\\n        json.dump(all_results, f, indent=2)\\n    log.info(\\\"All results saved to %s\\\", output_dir)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.61}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "5770fa53-6f85-4e70-a70f-fd1d0508e618",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"def load_pooled_eval_results(eval_dir, scales, benchmarks=None,\\\\n                              lr_filter=None, lr_filter_scales=None,\\\\n                              checkpoint_dir=None, **kwargs):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load and merge eval results across multiple model scales.\\\\n\\\\n    Calls load_eval_results once per scale, tags each model with its scale,\\\\n    and stacks response matrices vertically. Items are truncated to the\\\\n    minimum count across scales for consistency.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    all_models = []\\\\n    all_dosages = []\\\\n    bench_accum = {}\\\\n\\\\n    for scale in scales:\\\\n        kw = dict(kwargs)\\\\n        if lr_filter is not None and checkpoint_dir:\\\\n            if lr_filter_scales is None or scale in lr_filter_scales:\\\\n                kw[\\\\\\\"lr_filter\\\\\\\"] = lr_filter\\\\n                kw[\\\\\\\"checkpoint_dir\\\\\\\"] = checkpoint_dir\\\\n        data = load_eval_results(eval_dir, benchmarks, model_scale=scale, **kw)\\\\n        log.info(\\\\\\\"Pool scale %s: %d models, dosages=%s\\\\\\\",\\\\n                 scale, len(data[\\\\\\\"models\\\\\\\"]), data[\\\\\\\"dosages\\\\\\\"].tolist())\\\\n        for m in data[\\\\\\\"models\\\\\\\"]:\\\\n            m[\\\\\\\"scale\\\\\\\"] = scale\\\\n        all_models.extend(data[\\\\\\\"models\\\\\\\"])\\\\n        all_dosages.extend(data[\\\\\\\"dosages\\\\\\\"].tolist())\\\\n\\\\n        for bench, bd in data[\\\\\\\"benchmarks\\\\\\\"].items():\\\\n            if bench not in bench_accum:\\\\n                bench_accum[bench] = {\\\\\\\"n_items\\\\\\\": bd[\\\\\\\"n_items\\\\\\\"],\\\\n                                      \\\\\\\"responses\\\\\\\": [], \\\\\\\"valid\\\\\\\": []}\\\\n            bench_accum[bench][\\\\\\\"n_items\\\\\\\"] = min(\\\\n                bench_accum[bench][\\\\\\\"n_items\\\\\\\"], bd[\\\\\\\"n_items\\\\\\\"])\\\\n            bench_accum[bench][\\\\\\\"responses\\\\\\\"].append(bd[\\\\\\\"responses\\\\\\\"])\\\\n            bench_accum[bench][\\\\\\\"valid\\\\\\\"].append(bd[\\\\\\\"valid_mask\\\\\\\"])\\\\n\\\\n    result_benchmarks = {}\\\\n    for bench, acc in bench_accum.items():\\\\n        ni = acc[\\\\\\\"n_items\\\\\\\"]\\\\n        responses = np.vstack([r[:, :ni] for r in acc[\\\\\\\"responses\\\\\\\"]])\\\\n        valid = np.concatenate(acc[\\\\\\\"valid\\\\\\\"])\\\\n        result_benchmarks[bench] = {\\\\n            \\\\\\\"responses\\\\\\\": responses, \\\\\\\"n_items\\\\\\\": ni, \\\\\\\"valid_mask\\\\\\\": valid,\\\\n        }\\\\n\\\\n    return {\\\\n        \\\\\\\"models\\\\\\\": all_models,\\\\n        \\\\\\\"dosages\\\\\\\": np.array(all_dosages),\\\\n        \\\\\\\"benchmarks\\\\\\\": result_benchmarks,\\\\n    }\\\\n\\\\n\\\\n\\\\n# ── Stan Fitting ──\\\\n\\\\ndef prepare_stan_data(y, exposure, model_type=\\\\\\\"4pl_gamma\\\\\\\"):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Prepare data dict for Stan model.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    N_models, N_items = y.shape\\\\n    data = {\\\\n        \\\\\\\"N_models\\\\\\\": int(N_models),\\\\n        \\\\\\\"N_items\\\\\\\": int(N_items),\\\\n        \\\\\\\"y\\\\\\\": y.astype(int).tolist(),\\\\n    }\\\\n    if model_type != \\\\\\\"vanilla_4pl\\\\\\\":\\\\n        data[\\\\\\\"exposure\\\\\\\"] = exposure.tolist()\\\\n    return data\\\\n\\\\n\\\\ndef fit_stan_model(stan_file, stan_data, chains=4, iter_warmup=1000,\\\\n                   iter_sampling=1000, adapt_delta=0.95, max_treedepth=12,\\\\n                   seed=42, parallel_chains=None):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Fit Stan model via CmdStanPy NUTS sampler.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    log.info(\\\\\\\"Compiling Stan model: %s\\\\\\\", os.path.basename(stan_file))\\\\n    model = cmdstanpy.CmdStanModel(stan_file=stan_file)\\\\n\\\\n    log.info(\\\\\\\"Fitting: %d models x %d items, %d chains x %d samples\\\\\\\",\\\\n             stan_data[\\\\\\\"N_models\\\\\\\"], stan_data[\\\\\\\"N_items\\\\\\\"], chains, iter_sampling)\\\\n    t0 = time.time()\\\\n    fit = model.sample(\\\\n        data=stan_data,\\\\n        chains=chains,\\\\n        iter_warmup=iter_warmup,\\\\n        iter_sampling=iter_sampling,\\\\n        seed=seed,\\\\n        adapt_delta=adapt_delta,\\\\n        max_treedepth=max_treedepth,\\\\n        parallel_chains=parallel_chains if parallel_chains is not None else min(chains, 4),\\\\n        show_progress=True,\\\\n    )\\\\n    elapsed = time.time() - t0\\\\n    log.info(\\\\\\\"Sampling completed in %.1fs\\\\\\\", elapsed)\\\\n    return fit, elapsed\\\\n\\\\n\\\\n\\\\n\\\\n# ── Diagnostics ──\\\\n\\\\ndef check_convergence(fit):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Check Rhat, ESS, divergences.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    summary = fit.summary()\\\\n    diag = {}\\\\n\\\\n    for col in [\\\\\\\"R_hat\\\\\\\", \\\\\\\"Rhat\\\\\\\"]:\\\\n        if col in summary.columns:\\\\n            diag[\\\\\\\"max_rhat\\\\\\\"] = round(float(summary[col].max()), 4)\\\\n            diag[\\\\\\\"rhat_ok\\\\\\\"] = diag[\\\\\\\"max_rhat\\\\\\\"] < 1.01\\\\n            break\\\\n\\\\n    for col in [\\\\\\\"ESS_bulk\\\\\\\", \\\\\\\"N_Eff\\\\\\\", \\\\\\\"N_eff\\\\\\\"]:\\\\n        if col in summary.columns:\\\\n            diag[\\\\\\\"min_ess\\\\\\\"] = round(float(summary[col].min()), 1)\\\\n        \\\\n\\\\n... [截断: 输出过长，省略 7996 字符] ...\\\\n\\\\nOnly load aligned-format eval directories.\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--checkpoint-dir\\\\\\\", type=str, default=None,\\\\n                        help=\\\\\\\"Checkpoint dir for lr verification (D076)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--lr-filter\\\\\\\", type=float, default=None,\\\\n                        help=\\\\\\\"Only accept checkpoints with this lr (D076)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output-dir\\\\\\\", type=str, required=True)\\\\n\\\\n    parser.add_argument(\\\\\\\"--chains\\\\\\\", type=int, default=4)\\\\n    parser.add_argument(\\\\\\\"--warmup\\\\\\\", type=int, default=1000)\\\\n    parser.add_argument(\\\\\\\"--samples\\\\\\\", type=int, default=1000)\\\\n    parser.add_argument(\\\\\\\"--adapt-delta\\\\\\\", type=float, default=0.95)\\\\n    parser.add_argument(\\\\\\\"--max-treedepth\\\\\\\", type=int, default=12)\\\\n    parser.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n\\\\n    args = parser.parse_args()\\\\n\\\\n    logging.basicConfig(level=logging.INFO,\\\\n                        format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\")\\\\n\\\\n    output_dir = Path(args.output_dir)\\\\n    output_dir.mkdir(parents=True, exist_ok=True)\\\\n\\\\n    # Mode 1: direct matrix input\\\\n    if args.response_matrix:\\\\n        if not args.exposure_matrix and args.model_type != \\\\\\\"vanilla_4pl\\\\\\\":\\\\n            parser.error(\\\\\\\"--exposure-matrix required with --response-matrix \\\\\\\"\\\\n                         \\\\\\\"(unless --model-type=vanilla_4pl)\\\\\\\")\\\\n        y = load_matrix(args.response_matrix).astype(int)\\\\n        if args.exposure_matrix:\\\\n            exposure = load_matrix(args.exposure_matrix)\\\\n            assert y.shape == exposure.shape, (\\\\n                f\\\\\\\"Shape mismatch: response {y.shape} vs exposure {exposure.shape}\\\\\\\")\\\\n        else:\\\\n            exposure = np.zeros_like(y, dtype=float)\\\\n        bench_name = args.benchmark or \\\\\\\"benchmark\\\\\\\"\\\\n\\\\n        result = run_benchmark_fit(bench_name, y, exposure, args.model_type, args)\\\\n\\\\n        out_path = output_dir / f\\\\\\\"{bench_name}_{args.model_type}_results.json\\\\\\\"\\\\n        with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(result, f, indent=2)\\\\n        log.info(\\\\\\\"Results saved to %s\\\\\\\", out_path)\\\\n        return\\\\n\\\\n    # Mode 2: eval-dir input\\\\n    if not args.eval_dir:\\\\n        parser.error(\\\\\\\"Specify --eval-dir or --response-matrix\\\\\\\")\\\\n\\\\n    data = load_eval_results(args.eval_dir, args.benchmarks,\\\\n                              model_scale=args.model_scale,\\\\n                              seed_filter=args.data_seed,\\\\n                              aligned_only=args.aligned_only,\\\\n                              lr_filter=args.lr_filter,\\\\n                              checkpoint_dir=args.checkpoint_dir)\\\\n    exposure_scores = load_exposure_scores(args.exposure_file, data[\\\\\\\"benchmarks\\\\\\\"],\\\\n                                           model_id=args.tau_model_id)\\\\n    dosages = data[\\\\\\\"dosages\\\\\\\"]\\\\n\\\\n    all_results = {\\\\n        \\\\\\\"mode\\\\\\\": \\\\\\\"eval_dir\\\\\\\",\\\\n        \\\\\\\"eval_dir\\\\\\\": args.eval_dir,\\\\n        \\\\\\\"model_type\\\\\\\": args.model_type,\\\\n        \\\\\\\"models\\\\\\\": [\\\\n            {\\\\\\\"dirname\\\\\\\": m[\\\\\\\"dirname\\\\\\\"], \\\\\\\"model_name\\\\\\\": m[\\\\\\\"model_name\\\\\\\"],\\\\n             \\\\\\\"dosage\\\\\\\": m[\\\\\\\"dosage\\\\\\\"], \\\\\\\"seed\\\\\\\": m[\\\\\\\"seed\\\\\\\"]}\\\\n            for m in data[\\\\\\\"models\\\\\\\"]\\\\n        ],\\\\n        \\\\\\\"benchmarks\\\\\\\": {},\\\\n    }\\\\n\\\\n    for bench, bench_data in data[\\\\\\\"benchmarks\\\\\\\"].items():\\\\n        responses = bench_data[\\\\\\\"responses\\\\\\\"]\\\\n        valid = bench_data[\\\\\\\"valid_mask\\\\\\\"]\\\\n        tau = exposure_scores[bench]\\\\n\\\\n        if not valid.all():\\\\n            responses = responses[valid]\\\\n            dosages_bench = dosages[valid]\\\\n        else:\\\\n            dosages_bench = dosages\\\\n\\\\n        exposure_matrix = build_exposure_matrix(dosages_bench, tau[:bench_data[\\\\\\\"n_items\\\\\\\"]])\\\\n        result = run_benchmark_fit(bench, responses, exposure_matrix, args.model_type, args)\\\\n        all_results[\\\\\\\"benchmarks\\\\\\\"][bench] = result\\\\n\\\\n        bench_dir = output_dir / bench\\\\n        bench_dir.mkdir(parents=True, exist_ok=True)\\\\n        with open(bench_dir / f\\\\\\\"{args.model_type}_results.json\\\\\\\", \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(result, f, indent=2)\\\\n\\\\n    with open(output_dir / \\\\\\\"irt_calibration_results.json\\\\\\\", \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(all_results, f, indent=2)\\\\n    log.info(\\\\\\\"All results saved to %s\\\\\\\", output_dir)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.61}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"def load_pooled_eval_results(eval_dir, scales, benchmarks=None,\\n                              lr_filter=None, lr_filter_scales=None,\\n                              checkpoint_dir=None, **kwargs):\\n    \\\"\\\"\\\"Load and merge eval results across multiple model scales.\\n\\n    Calls load_eval_results once per scale, tags each model with its scale,\\n    and stacks response matrices vertically. Items are truncated to the\\n    minimum count across scales for consistency.\\n    \\\"\\\"\\\"\\n    all_models = []\\n    all_dosages = []\\n    bench_accum = {}\\n\\n    for scale in scales:\\n        kw = dict(kwargs)\\n        if lr_filter is not None and checkpoint_dir:\\n            if lr_filter_scales is None or scale in lr_filter_scales:\\n                kw[\\\"lr_filter\\\"] = lr_filter\\n                kw[\\\"checkpoint_dir\\\"] = checkpoint_dir\\n        data = load_eval_results(eval_dir, benchmarks, model_scale=scale, **kw)\\n        log.info(\\\"Pool scale %s: %d models, dosages=%s\\\",\\n                 scale, len(data[\\\"models\\\"]), data[\\\"dosages\\\"].tolist())\\n        for m in data[\\\"models\\\"]:\\n            m[\\\"scale\\\"] = scale\\n        all_models.extend(data[\\\"models\\\"])\\n        all_dosages.extend(data[\\\"dosages\\\"].tolist())\\n\\n        for bench, bd in data[\\\"benchmarks\\\"].items():\\n            if bench not in bench_accum:\\n                bench_accum[bench] = {\\\"n_items\\\": bd[\\\"n_items\\\"],\\n                                      \\\"responses\\\": [], \\\"valid\\\": []}\\n            bench_accum[bench][\\\"n_items\\\"] = min(\\n                bench_accum[bench][\\\"n_items\\\"], bd[\\\"n_items\\\"])\\n            bench_accum[bench][\\\"responses\\\"].append(bd[\\\"responses\\\"])\\n            bench_accum[bench][\\\"valid\\\"].append(bd[\\\"valid_mask\\\"])\\n\\n    result_benchmarks = {}\\n    for bench, acc in bench_accum.items():\\n        ni = acc[\\\"n_items\\\"]\\n        responses = np.vstack([r[:, :ni] for r in acc[\\\"responses\\\"]])\\n        valid = np.concatenate(acc[\\\"valid\\\"])\\n        result_benchmarks[bench] = {\\n            \\\"responses\\\": responses, \\\"n_items\\\": ni, \\\"valid_mask\\\": valid,\\n        }\\n\\n    return {\\n        \\\"models\\\": all_models,\\n        \\\"dosages\\\": np.array(all_dosages),\\n        \\\"benchmarks\\\": result_benchmarks,\\n    }\\n\\n\\n\\n# ── Stan Fitting ──\\n\\ndef prepare_stan_data(y, exposure, model_type=\\\"4pl_gamma\\\"):\\n    \\\"\\\"\\\"Prepare data dict for Stan model.\\\"\\\"\\\"\\n    N_models, N_items = y.shape\\n    data = {\\n        \\\"N_models\\\": int(N_models),\\n        \\\"N_items\\\": int(N_items),\\n        \\\"y\\\": y.astype(int).tolist(),\\n    }\\n    if model_type != \\\"vanilla_4pl\\\":\\n        data[\\\"exposure\\\"] = exposure.tolist()\\n    return data\\n\\n\\ndef fit_stan_model(stan_file, stan_data, chains=4, iter_warmup=1000,\\n                   iter_sampling=1000, adapt_delta=0.95, max_treedepth=12,\\n                   seed=42, parallel_chains=None):\\n    \\\"\\\"\\\"Fit Stan model via CmdStanPy NUTS sampler.\\\"\\\"\\\"\\n    log.info(\\\"Compiling Stan model: %s\\\", os.path.basename(stan_file))\\n    model = cmdstanpy.CmdStanModel(stan_file=stan_file)\\n\\n    log.info(\\\"Fitting: %d models x %d items, %d chains x %d samples\\\",\\n             stan_data[\\\"N_models\\\"], stan_data[\\\"N_items\\\"], chains, iter_sampling)\\n    t0 = time.time()\\n    fit = model.sample(\\n        data=stan_data,\\n        chains=chains,\\n        iter_warmup=iter_warmup,\\n        iter_sampling=iter_sampling,\\n        seed=seed,\\n        adapt_delta=adapt_delta,\\n        max_treedepth=max_treedepth,\\n        parallel_chains=parallel_chains if parallel_chains is not None else min(chains, 4),\\n        show_progress=True,\\n    )\\n    elapsed = time.time() - t0\\n    log.info(\\\"Sampling completed in %.1fs\\\", elapsed)\\n    return fit, elapsed\\n\\n\\n\\n\\n# ── Diagnostics ──\\n\\ndef check_convergence(fit):\\n    \\\"\\\"\\\"Check Rhat, ESS, divergences.\\\"\\\"\\\"\\n    summary = fit.summary()\\n    diag = {}\\n\\n    for col in [\\\"R_hat\\\", \\\"Rhat\\\"]:\\n        if col in summary.columns:\\n            diag[\\\"max_rhat\\\"] = round(float(summary[col].max()), 4)\\n            diag[\\\"rhat_ok\\\"] = diag[\\\"max_rhat\\\"] < 1.01\\n            break\\n\\n    for col in [\\\"ESS_bulk\\\", \\\"N_Eff\\\", \\\"N_eff\\\"]:\\n        if col in summary.columns:\\n            diag[\\\"min_ess\\\"] = round(float(summary[col].min()), 1)\\n        \\n\\n... [截断: 输出过长，省略 7996 字符] ...\\n\\nOnly load aligned-format eval directories.\\\")\\n    parser.add_argument(\\\"--checkpoint-dir\\\", type=str, default=None,\\n                        help=\\\"Checkpoint dir for lr verification (D076)\\\")\\n    parser.add_argument(\\\"--lr-filter\\\", type=float, default=None,\\n                        help=\\\"Only accept checkpoints with this lr (D076)\\\")\\n    parser.add_argument(\\\"--output-dir\\\", type=str, required=True)\\n\\n    parser.add_argument(\\\"--chains\\\", type=int, default=4)\\n    parser.add_argument(\\\"--warmup\\\", type=int, default=1000)\\n    parser.add_argument(\\\"--samples\\\", type=int, default=1000)\\n    parser.add_argument(\\\"--adapt-delta\\\", type=float, default=0.95)\\n    parser.add_argument(\\\"--max-treedepth\\\", type=int, default=12)\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42)\\n\\n    args = parser.parse_args()\\n\\n    logging.basicConfig(level=logging.INFO,\\n                        format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\")\\n\\n    output_dir = Path(args.output_dir)\\n    output_dir.mkdir(parents=True, exist_ok=True)\\n\\n    # Mode 1: direct matrix input\\n    if args.response_matrix:\\n        if not args.exposure_matrix and args.model_type != \\\"vanilla_4pl\\\":\\n            parser.error(\\\"--exposure-matrix required with --response-matrix \\\"\\n                         \\\"(unless --model-type=vanilla_4pl)\\\")\\n        y = load_matrix(args.response_matrix).astype(int)\\n        if args.exposure_matrix:\\n            exposure = load_matrix(args.exposure_matrix)\\n            assert y.shape == exposure.shape, (\\n                f\\\"Shape mismatch: response {y.shape} vs exposure {exposure.shape}\\\")\\n        else:\\n            exposure = np.zeros_like(y, dtype=float)\\n        bench_name = args.benchmark or \\\"benchmark\\\"\\n\\n        result = run_benchmark_fit(bench_name, y, exposure, args.model_type, args)\\n\\n        out_path = output_dir / f\\\"{bench_name}_{args.model_type}_results.json\\\"\\n        with open(out_path, \\\"w\\\") as f:\\n            json.dump(result, f, indent=2)\\n        log.info(\\\"Results saved to %s\\\", out_path)\\n        return\\n\\n    # Mode 2: eval-dir input\\n    if not args.eval_dir:\\n        parser.error(\\\"Specify --eval-dir or --response-matrix\\\")\\n\\n    data = load_eval_results(args.eval_dir, args.benchmarks,\\n                              model_scale=args.model_scale,\\n                              seed_filter=args.data_seed,\\n                              aligned_only=args.aligned_only,\\n                              lr_filter=args.lr_filter,\\n                              checkpoint_dir=args.checkpoint_dir)\\n    exposure_scores = load_exposure_scores(args.exposure_file, data[\\\"benchmarks\\\"],\\n                                           model_id=args.tau_model_id)\\n    dosages = data[\\\"dosages\\\"]\\n\\n    all_results = {\\n        \\\"mode\\\": \\\"eval_dir\\\",\\n        \\\"eval_dir\\\": args.eval_dir,\\n        \\\"model_type\\\": args.model_type,\\n        \\\"models\\\": [\\n            {\\\"dirname\\\": m[\\\"dirname\\\"], \\\"model_name\\\": m[\\\"model_name\\\"],\\n             \\\"dosage\\\": m[\\\"dosage\\\"], \\\"seed\\\": m[\\\"seed\\\"]}\\n            for m in data[\\\"models\\\"]\\n        ],\\n        \\\"benchmarks\\\": {},\\n    }\\n\\n    for bench, bench_data in data[\\\"benchmarks\\\"].items():\\n        responses = bench_data[\\\"responses\\\"]\\n        valid = bench_data[\\\"valid_mask\\\"]\\n        tau = exposure_scores[bench]\\n\\n        if not valid.all():\\n            responses = responses[valid]\\n            dosages_bench = dosages[valid]\\n        else:\\n            dosages_bench = dosages\\n\\n        exposure_matrix = build_exposure_matrix(dosages_bench, tau[:bench_data[\\\"n_items\\\"]])\\n        result = run_benchmark_fit(bench, responses, exposure_matrix, args.model_type, args)\\n        all_results[\\\"benchmarks\\\"][bench] = result\\n\\n        bench_dir = output_dir / bench\\n        bench_dir.mkdir(parents=True, exist_ok=True)\\n        with open(bench_dir / f\\\"{args.model_type}_results.json\\\", \\\"w\\\") as f:\\n            json.dump(result, f, indent=2)\\n\\n    with open(output_dir / \\\"irt_calibration_results.json\\\", \\\"w\\\") as f:\\n        json.dump(all_results, f, indent=2)\\n    log.info(\\\"All results saved to %s\\\", output_dir)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.61}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 92_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clearer picture. Let me also read the middle part of the remote file to understand `check_convergence`, `extract_results`, and `_summarize_vector` fully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "ff89d6fe-a425-4dda-8d58-64afe988a405",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKxP9p8Ee4mDmize6JEDfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 65448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
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

_source line 93_

Let me get the truncated part (check_convergence, extract_results, etc.).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "fa74b194-349e-4372-90c2-54b5061b4792",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKxP9p8Ee4mDmize6JEDfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 65448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
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

_source line 94_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013K3xQ6BsLypsHC6Bc55pgu`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -460 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "cac145a1-7e19-441d-bbba-3741eb172806",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKxP9p8Ee4mDmize6JEDfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 65448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
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

_source line 95 · 2026-05-16T05:31:31.471Z_

<details><summary>↩ Tool result · `toolu_013K3xQ6BsLypsHC6Bc55pgu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nIRT calibration for contamination-aware benchmark score correction.\\nFits 4PL+gamma IRT model via CmdStanPy MCMC (NUTS) per benchmark.\\n\\nInput:\\n  - Correctness matrix (N_models x N_items): binary 0/1\\n  - Exposure matrix (N_models x N_items): continuous exposure scores\\n  OR\\n  - eval-dir with per-model eval results + per-benchmark exposure scores\\n\\nOutput (per benchmark):\\n  - Posterior: gamma, theta, item params (a, b, c, d)\\n  - Calibrated scores (exposure=0 counterfactual) with 50/80/95% CIs\\n  - Convergence diagnostics (Rhat, ESS, divergences)\\n  - Posterior predictive checks\\n\\nDependencies: cmdstanpy (CmdStan 2.38+), numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport cmdstanpy\\n\\nlog = logging.getLogger(__name__)\\n\\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\\nSTAN_MODEL_DIR = \\\"/root/contamcal-irt-calibration/stan_models\\\"\\nSTAN_MODELS = {\\n    \\\"4pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple.stan\\\"),\\n    \\\"2pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_2pl_gamma.stan\\\"),\\n    \\\"vanilla_4pl\\\": os.path.join(STAN_MODEL_DIR, \\\"vanilla_4pl.stan\\\"),\\n    \\\"4pl_gamma_wider\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple_wider.stan\\\"),\\n}\\n\\nDOSAGE_PATTERN = re.compile(r\\\"_d(\\\\d+)(?:_v\\\\d+)?_s(\\\\d+)(_para)?(_aligned)?(?:_v\\\\d+)?$\\\")\\n\\n\\n# ── Data Loading ──\\n\\ndef parse_model_dir_name(dirname):\\n    \\\"\\\"\\\"Extract model name, dosage, seed from directory like Qwen2.5-0.5B_d025_s42.\\\"\\\"\\\"\\n    m = DOSAGE_PATTERN.search(dirname)\\n    if not m:\\n        return None\\n    return {\\n        \\\"dirname\\\": dirname,\\n        \\\"model_name\\\": dirname[:m.start()],\\n        \\\"dosage\\\": int(m.group(1)),\\n        \\\"seed\\\": int(m.group(2)),\\n        \\\"is_para\\\": m.group(3) is not None,\\n        \\\"is_aligned\\\": m.group(4) is not None,\\n    }\\n\\n\\ndef get_train_lr(dirname, checkpoint_dir):\\n    \\\"\\\"\\\"Read lr from checkpoint's train_config.json (D076).\\\"\\\"\\\"\\n    ckpt_name = re.sub(r'(_para)?(_aligned)?$', '', dirname)\\n    config_path = os.path.join(checkpoint_dir, ckpt_name, \\\"train_config.json\\\")\\n    try:\\n        with open(config_path) as f:\\n            return json.load(f).get(\\\"lr\\\")\\n    except (FileNotFoundError, json.JSONDecodeError):\\n        pass\\n    # Fallback: eval dir may have version suffix not in checkpoint name\\n    ckpt_fallback = re.sub(r'_v\\\\d+(?=_s\\\\d+$)', '', ckpt_name)\\n    if ckpt_fallback != ckpt_name:\\n        config_path = os.path.join(checkpoint_dir, ckpt_fallback, \\\"train_config.json\\\")\\n        try:\\n            with open(config_path) as f:\\n                return json.load(f).get(\\\"lr\\\")\\n        except (FileNotFoundError, json.JSONDecodeError):\\n            pass\\n    return None\\n\\n\\ndef load_matrix(path):\\n    \\\"\\\"\\\"Load matrix from .npy, .csv, or .json.\\\"\\\"\\\"\\n    ext = os.path.splitext(path)[1].lower()\\n    if ext == \\\".npy\\\":\\n        return np.load(path)\\n    elif ext == \\\".csv\\\":\\n        return np.loadtxt(path, delimiter=\\\",\\\", skiprows=1)\\n    elif ext == \\\".json\\\":\\n        with open(path) as f:\\n            return np.array(json.load(f))\\n    raise ValueError(f\\\"Unsupported format: {ext}\\\")\\n\\n\\ndef load_eval_results(eval_dir, benchmarks=None, skip_para=True,\\n                      model_scale=None, seed_filter=None, aligned_only=False,\\n                      lr_filter=None, checkpoint_dir=None):\\n    \\\"\\\"\\\"Load per-model eval results into response matrices per benchmark.\\\"\\\"\\\"\\n    eval_path = Path(eval_dir)\\n    model_dirs = sorted([\\n        d for d in eval_path.iterdir()\\n        if d.is_dir() and (d / \\\"eval_results.json\\\").exists()\\n    ])\\n\\n    models = []\\n    for d in model_dirs:\\n        info = parse_model_dir_name(d.name)\\n        if info is None:\\n            log.warning(\\\"Skipping unrecognized dir: %s\\\", d.name)\\n            continue\\n        if skip_para and info[\\\"is_para\\\"]:\\n            continue\\n        if aligned_only and not info.get(\\\"is_aligned\\\", False):\\n            log.info(\\\"Skipping non-aligned dir: %s\\\", d.name)\\n            continue\\n        if model_scale and model_scale not in d.name:\\n            log.info\\n\\n... [截断: 输出过长，省略 8864 字符] ...\\n\\ngent_count\\\"] = divergent\\n    diag[\\\"divergent_pct\\\"] = round(100.0 * divergent / total_draws, 4)\\n    diag[\\\"divergent_ok\\\"] = diag[\\\"divergent_pct\\\"] < 0.1\\n    diag[\\\"total_draws\\\"] = total_draws\\n    diag[\\\"all_ok\\\"] = all(diag.get(k, True) for k in [\\\"rhat_ok\\\", \\\"ess_ok\\\", \\\"divergent_ok\\\"])\\n\\n    return diag\\n\\n\\ndef posterior_predictive_check(fit, y):\\n    \\\"\\\"\\\"Posterior predictive check: compare observed vs predicted accuracy.\\\"\\\"\\\"\\n    cal_draws = fit.stan_variable(\\\"calibrated_score\\\")  # (n_draws, N_models)\\n    obs_acc = y.mean()\\n    pred_acc_per_draw = cal_draws.mean(axis=1)\\n    ppp = float(np.mean(pred_acc_per_draw >= obs_acc))\\n\\n    obs_model_acc = y.mean(axis=1)\\n    pred_model_acc = np.mean(cal_draws, axis=0)\\n    residual_mae = float(np.mean(np.abs(pred_model_acc - obs_model_acc)))\\n\\n    return {\\n        \\\"overall_ppp\\\": round(ppp, 4),\\n        \\\"obs_mean_acc\\\": round(float(obs_acc), 4),\\n        \\\"pred_mean_acc\\\": round(float(pred_acc_per_draw.mean()), 4),\\n        \\\"residual_mae\\\": round(residual_mae, 4),\\n    }\\n\\n\\n# ── Result Extraction ──\\n\\ndef _summarize_vector(draws):\\n    \\\"\\\"\\\"Summarize posterior draws into point estimates and quantiles.\\\"\\\"\\\"\\n    return {\\n        \\\"mean\\\": np.round(np.mean(draws, axis=0), 4).tolist(),\\n        \\\"sd\\\": np.round(np.std(draws, axis=0), 4).tolist(),\\n        \\\"q025\\\": np.round(np.percentile(draws, 2.5, axis=0), 4).tolist(),\\n        \\\"q975\\\": np.round(np.percentile(draws, 97.5, axis=0), 4).tolist(),\\n        \\\"q10\\\": np.round(np.percentile(draws, 10, axis=0), 4).tolist(),\\n        \\\"q90\\\": np.round(np.percentile(draws, 90, axis=0), 4).tolist(),\\n        \\\"q25\\\": np.round(np.percentile(draws, 25, axis=0), 4).tolist(),\\n        \\\"q75\\\": np.round(np.percentile(draws, 75, axis=0), 4).tolist(),\\n    }\\n\\n\\ndef extract_results(fit, y, model_type):\\n    \\\"\\\"\\\"Extract all posterior summaries from fitted model.\\\"\\\"\\\"\\n    results = {}\\n\\n    # Gamma\\n    if model_type != \\\"vanilla_4pl\\\":\\n        gamma_draws = fit.stan_variable(\\\"gamma\\\")\\n        results[\\\"gamma\\\"] = {\\n            \\\"mean\\\": round(float(np.mean(gamma_draws)), 4),\\n            \\\"sd\\\": round(float(np.std(gamma_draws)), 4),\\n            \\\"q025\\\": round(float(np.percentile(gamma_draws, 2.5)), 4),\\n            \\\"q975\\\": round(float(np.percentile(gamma_draws, 97.5)), 4),\\n            \\\"q10\\\": round(float(np.percentile(gamma_draws, 10)), 4),\\n            \\\"q90\\\": round(float(np.percentile(gamma_draws, 90)), 4),\\n            \\\"q25\\\": round(float(np.percentile(gamma_draws, 25)), 4),\\n            \\\"q75\\\": round(float(np.percentile(gamma_draws, 75)), 4),\\n            \\\"ci_excludes_zero\\\": bool(\\n                np.percentile(gamma_draws, 2.5) > 0 or\\n                np.percentile(gamma_draws, 97.5) < 0\\n            ),\\n        }\\n\\n    # Theta\\n    theta_draws = fit.stan_variable(\\\"theta\\\")\\n    results[\\\"theta\\\"] = {\\n        \\\"mean\\\": np.round(np.mean(theta_draws, axis=0), 4).tolist(),\\n        \\\"sd\\\": np.round(np.std(theta_draws, axis=0), 4).tolist(),\\n    }\\n\\n    # Item parameters\\n    for param in [\\\"a\\\", \\\"b\\\"]:\\n        draws = fit.stan_variable(param)\\n        results[param] = {\\n            \\\"mean\\\": np.round(np.mean(draws, axis=0), 4).tolist(),\\n            \\\"sd\\\": np.round(np.std(draws, axis=0), 4).tolist(),\\n        }\\n    if model_type != \\\"2pl_gamma\\\":\\n        for param in [\\\"c\\\", \\\"d\\\"]:\\n            draws = fit.stan_variable(param)\\n            results[param] = {\\n                \\\"mean\\\": np.round(np.mean(draws, axis=0), 4).tolist(),\\n                \\\"sd\\\": np.round(np.std(draws, axis=0), 4).tolist(),\\n            }\\n\\n    # Calibrated scores with multi-level CIs\\n    cal_draws = fit.stan_variable(\\\"calibrated_score\\\")\\n    results[\\\"calibrated_scores\\\"] = _summarize_vector(cal_draws)\\n\\n    # Raw accuracy for reference\\n    results[\\\"raw_accuracy\\\"] = np.round(y.mean(axis=1), 4).tolist()\\n\\n    return results\\n\\n\\n# ── Per-Benchmark Fitting ──\\n\\ndef run_benchmark_fit(bench_name, y, exposure, model_type, args, **kwargs):\\n    \\\"\\\"\\\"Fit IRT model for a single benchmark via NUTS.\\\"\\\"\\\"\\n    N_models, N_items = y.shape\\n    log.info(\\\"=== %s: %d models x %d items ===\\\",\\n             bench_name, N_models, N_items)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "05fa0390-1723-4b62-bc2b-9c2a01cf9c1e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nIRT calibration for contamination-aware benchmark score correction.\\\\nFits 4PL+gamma IRT model via CmdStanPy MCMC (NUTS) per benchmark.\\\\n\\\\nInput:\\\\n  - Correctness matrix (N_models x N_items): binary 0/1\\\\n  - Exposure matrix (N_models x N_items): continuous exposure scores\\\\n  OR\\\\n  - eval-dir with per-model eval results + per-benchmark exposure scores\\\\n\\\\nOutput (per benchmark):\\\\n  - Posterior: gamma, theta, item params (a, b, c, d)\\\\n  - Calibrated scores (exposure=0 counterfactual) with 50/80/95% CIs\\\\n  - Convergence diagnostics (Rhat, ESS, divergences)\\\\n  - Posterior predictive checks\\\\n\\\\nDependencies: cmdstanpy (CmdStan 2.38+), numpy, scipy\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport re\\\\nimport sys\\\\nimport time\\\\nfrom pathlib import Path\\\\n\\\\nimport numpy as np\\\\nimport cmdstanpy\\\\n\\\\nlog = logging.getLogger(__name__)\\\\n\\\\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\\\\nSTAN_MODEL_DIR = \\\\\\\"/root/contamcal-irt-calibration/stan_models\\\\\\\"\\\\nSTAN_MODELS = {\\\\n    \\\\\\\"4pl_gamma\\\\\\\": os.path.join(STAN_MODEL_DIR, \\\\\\\"contam_irt_4pl_simple.stan\\\\\\\"),\\\\n    \\\\\\\"2pl_gamma\\\\\\\": os.path.join(STAN_MODEL_DIR, \\\\\\\"contam_irt_2pl_gamma.stan\\\\\\\"),\\\\n    \\\\\\\"vanilla_4pl\\\\\\\": os.path.join(STAN_MODEL_DIR, \\\\\\\"vanilla_4pl.stan\\\\\\\"),\\\\n    \\\\\\\"4pl_gamma_wider\\\\\\\": os.path.join(STAN_MODEL_DIR, \\\\\\\"contam_irt_4pl_simple_wider.stan\\\\\\\"),\\\\n}\\\\n\\\\nDOSAGE_PATTERN = re.compile(r\\\\\\\"_d(\\\\\\\\d+)(?:_v\\\\\\\\d+)?_s(\\\\\\\\d+)(_para)?(_aligned)?(?:_v\\\\\\\\d+)?$\\\\\\\")\\\\n\\\\n\\\\n# ── Data Loading ──\\\\n\\\\ndef parse_model_dir_name(dirname):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Extract model name, dosage, seed from directory like Qwen2.5-0.5B_d025_s42.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    m = DOSAGE_PATTERN.search(dirname)\\\\n    if not m:\\\\n        return None\\\\n    return {\\\\n        \\\\\\\"dirname\\\\\\\": dirname,\\\\n        \\\\\\\"model_name\\\\\\\": dirname[:m.start()],\\\\n        \\\\\\\"dosage\\\\\\\": int(m.group(1)),\\\\n        \\\\\\\"seed\\\\\\\": int(m.group(2)),\\\\n        \\\\\\\"is_para\\\\\\\": m.group(3) is not None,\\\\n        \\\\\\\"is_aligned\\\\\\\": m.group(4) is not None,\\\\n    }\\\\n\\\\n\\\\ndef get_train_lr(dirname, checkpoint_dir):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Read lr from checkpoint's train_config.json (D076).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    ckpt_name = re.sub(r'(_para)?(_aligned)?$', '', dirname)\\\\n    config_path = os.path.join(checkpoint_dir, ckpt_name, \\\\\\\"train_config.json\\\\\\\")\\\\n    try:\\\\n        with open(config_path) as f:\\\\n            return json.load(f).get(\\\\\\\"lr\\\\\\\")\\\\n    except (FileNotFoundError, json.JSONDecodeError):\\\\n        pass\\\\n    # Fallback: eval dir may have version suffix not in checkpoint name\\\\n    ckpt_fallback = re.sub(r'_v\\\\\\\\d+(?=_s\\\\\\\\d+$)', '', ckpt_name)\\\\n    if ckpt_fallback != ckpt_name:\\\\n        config_path = os.path.join(checkpoint_dir, ckpt_fallback, \\\\\\\"train_config.json\\\\\\\")\\\\n        try:\\\\n            with open(config_path) as f:\\\\n                return json.load(f).get(\\\\\\\"lr\\\\\\\")\\\\n        except (FileNotFoundError, json.JSONDecodeError):\\\\n            pass\\\\n    return None\\\\n\\\\n\\\\ndef load_matrix(path):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load matrix from .npy, .csv, or .json.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    ext = os.path.splitext(path)[1].lower()\\\\n    if ext == \\\\\\\".npy\\\\\\\":\\\\n        return np.load(path)\\\\n    elif ext == \\\\\\\".csv\\\\\\\":\\\\n        return np.loadtxt(path, delimiter=\\\\\\\",\\\\\\\", skiprows=1)\\\\n    elif ext == \\\\\\\".json\\\\\\\":\\\\n        with open(path) as f:\\\\n            return np.array(json.load(f))\\\\n    raise ValueError(f\\\\\\\"Unsupported format: {ext}\\\\\\\")\\\\n\\\\n\\\\ndef load_eval_results(eval_dir, benchmarks=None, skip_para=True,\\\\n                      model_scale=None, seed_filter=None, aligned_only=False,\\\\n                      lr_filter=None, checkpoint_dir=None):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load per-model eval results into response matrices per benchmark.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    eval_path = Path(eval_dir)\\\\n    model_dirs = sorted([\\\\n        d for d in eval_path.iterdir()\\\\n        if d.is_dir() and (d / \\\\\\\"eval_results.json\\\\\\\").exists()\\\\n    ])\\\\n\\\\n    models = []\\\\n    for d in model_dirs:\\\\n        info = parse_model_dir_name(d.name)\\\\n        if info is None:\\\\n            log.warning(\\\\\\\"Skipping unrecognized dir: %s\\\\\\\", d.name)\\\\n            continue\\\\n        if skip_para and info[\\\\\\\"is_para\\\\\\\"]:\\\\n            continue\\\\n        if aligned_only and not info.get(\\\\\\\"is_aligned\\\\\\\", False):\\\\n            log.info(\\\\\\\"Skipping non-aligned dir: %s\\\\\\\", d.name)\\\\n            continue\\\\n        if model_scale and model_scale not in d.name:\\\\n            log.info\\\\n\\\\n... [截断: 输出过长，省略 8864 字符] ...\\\\n\\\\ngent_count\\\\\\\"] = divergent\\\\n    diag[\\\\\\\"divergent_pct\\\\\\\"] = round(100.0 * divergent / total_draws, 4)\\\\n    diag[\\\\\\\"divergent_ok\\\\\\\"] = diag[\\\\\\\"divergent_pct\\\\\\\"] < 0.1\\\\n    diag[\\\\\\\"total_draws\\\\\\\"] = total_draws\\\\n    diag[\\\\\\\"all_ok\\\\\\\"] = all(diag.get(k, True) for k in [\\\\\\\"rhat_ok\\\\\\\", \\\\\\\"ess_ok\\\\\\\", \\\\\\\"divergent_ok\\\\\\\"])\\\\n\\\\n    return diag\\\\n\\\\n\\\\ndef posterior_predictive_check(fit, y):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Posterior predictive check: compare observed vs predicted accuracy.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    cal_draws = fit.stan_variable(\\\\\\\"calibrated_score\\\\\\\")  # (n_draws, N_models)\\\\n    obs_acc = y.mean()\\\\n    pred_acc_per_draw = cal_draws.mean(axis=1)\\\\n    ppp = float(np.mean(pred_acc_per_draw >= obs_acc))\\\\n\\\\n    obs_model_acc = y.mean(axis=1)\\\\n    pred_model_acc = np.mean(cal_draws, axis=0)\\\\n    residual_mae = float(np.mean(np.abs(pred_model_acc - obs_model_acc)))\\\\n\\\\n    return {\\\\n        \\\\\\\"overall_ppp\\\\\\\": round(ppp, 4),\\\\n        \\\\\\\"obs_mean_acc\\\\\\\": round(float(obs_acc), 4),\\\\n        \\\\\\\"pred_mean_acc\\\\\\\": round(float(pred_acc_per_draw.mean()), 4),\\\\n        \\\\\\\"residual_mae\\\\\\\": round(residual_mae, 4),\\\\n    }\\\\n\\\\n\\\\n# ── Result Extraction ──\\\\n\\\\ndef _summarize_vector(draws):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Summarize posterior draws into point estimates and quantiles.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    return {\\\\n        \\\\\\\"mean\\\\\\\": np.round(np.mean(draws, axis=0), 4).tolist(),\\\\n        \\\\\\\"sd\\\\\\\": np.round(np.std(draws, axis=0), 4).tolist(),\\\\n        \\\\\\\"q025\\\\\\\": np.round(np.percentile(draws, 2.5, axis=0), 4).tolist(),\\\\n        \\\\\\\"q975\\\\\\\": np.round(np.percentile(draws, 97.5, axis=0), 4).tolist(),\\\\n        \\\\\\\"q10\\\\\\\": np.round(np.percentile(draws, 10, axis=0), 4).tolist(),\\\\n        \\\\\\\"q90\\\\\\\": np.round(np.percentile(draws, 90, axis=0), 4).tolist(),\\\\n        \\\\\\\"q25\\\\\\\": np.round(np.percentile(draws, 25, axis=0), 4).tolist(),\\\\n        \\\\\\\"q75\\\\\\\": np.round(np.percentile(draws, 75, axis=0), 4).tolist(),\\\\n    }\\\\n\\\\n\\\\ndef extract_results(fit, y, model_type):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Extract all posterior summaries from fitted model.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    results = {}\\\\n\\\\n    # Gamma\\\\n    if model_type != \\\\\\\"vanilla_4pl\\\\\\\":\\\\n        gamma_draws = fit.stan_variable(\\\\\\\"gamma\\\\\\\")\\\\n        results[\\\\\\\"gamma\\\\\\\"] = {\\\\n            \\\\\\\"mean\\\\\\\": round(float(np.mean(gamma_draws)), 4),\\\\n            \\\\\\\"sd\\\\\\\": round(float(np.std(gamma_draws)), 4),\\\\n            \\\\\\\"q025\\\\\\\": round(float(np.percentile(gamma_draws, 2.5)), 4),\\\\n            \\\\\\\"q975\\\\\\\": round(float(np.percentile(gamma_draws, 97.5)), 4),\\\\n            \\\\\\\"q10\\\\\\\": round(float(np.percentile(gamma_draws, 10)), 4),\\\\n            \\\\\\\"q90\\\\\\\": round(float(np.percentile(gamma_draws, 90)), 4),\\\\n            \\\\\\\"q25\\\\\\\": round(float(np.percentile(gamma_draws, 25)), 4),\\\\n            \\\\\\\"q75\\\\\\\": round(float(np.percentile(gamma_draws, 75)), 4),\\\\n            \\\\\\\"ci_excludes_zero\\\\\\\": bool(\\\\n                np.percentile(gamma_draws, 2.5) > 0 or\\\\n                np.percentile(gamma_draws, 97.5) < 0\\\\n            ),\\\\n        }\\\\n\\\\n    # Theta\\\\n    theta_draws = fit.stan_variable(\\\\\\\"theta\\\\\\\")\\\\n    results[\\\\\\\"theta\\\\\\\"] = {\\\\n        \\\\\\\"mean\\\\\\\": np.round(np.mean(theta_draws, axis=0), 4).tolist(),\\\\n        \\\\\\\"sd\\\\\\\": np.round(np.std(theta_draws, axis=0), 4).tolist(),\\\\n    }\\\\n\\\\n    # Item parameters\\\\n    for param in [\\\\\\\"a\\\\\\\", \\\\\\\"b\\\\\\\"]:\\\\n        draws = fit.stan_variable(param)\\\\n        results[param] = {\\\\n            \\\\\\\"mean\\\\\\\": np.round(np.mean(draws, axis=0), 4).tolist(),\\\\n            \\\\\\\"sd\\\\\\\": np.round(np.std(draws, axis=0), 4).tolist(),\\\\n        }\\\\n    if model_type != \\\\\\\"2pl_gamma\\\\\\\":\\\\n        for param in [\\\\\\\"c\\\\\\\", \\\\\\\"d\\\\\\\"]:\\\\n            draws = fit.stan_variable(param)\\\\n            results[param] = {\\\\n                \\\\\\\"mean\\\\\\\": np.round(np.mean(draws, axis=0), 4).tolist(),\\\\n                \\\\\\\"sd\\\\\\\": np.round(np.std(draws, axis=0), 4).tolist(),\\\\n            }\\\\n\\\\n    # Calibrated scores with multi-level CIs\\\\n    cal_draws = fit.stan_variable(\\\\\\\"calibrated_score\\\\\\\")\\\\n    results[\\\\\\\"calibrated_scores\\\\\\\"] = _summarize_vector(cal_draws)\\\\n\\\\n    # Raw accuracy for reference\\\\n    results[\\\\\\\"raw_accuracy\\\\\\\"] = np.round(y.mean(axis=1), 4).tolist()\\\\n\\\\n    return results\\\\n\\\\n\\\\n# ── Per-Benchmark Fitting ──\\\\n\\\\ndef run_benchmark_fit(bench_name, y, exposure, model_type, args, **kwargs):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Fit IRT model for a single benchmark via NUTS.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    N_models, N_items = y.shape\\\\n    log.info(\\\\\\\"=== %s: %d models x %d items ===\\\\\\\",\\\\n             bench_name, N_models, N_items)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nIRT calibration for contamination-aware benchmark score correction.\\nFits 4PL+gamma IRT model via CmdStanPy MCMC (NUTS) per benchmark.\\n\\nInput:\\n  - Correctness matrix (N_models x N_items): binary 0/1\\n  - Exposure matrix (N_models x N_items): continuous exposure scores\\n  OR\\n  - eval-dir with per-model eval results + per-benchmark exposure scores\\n\\nOutput (per benchmark):\\n  - Posterior: gamma, theta, item params (a, b, c, d)\\n  - Calibrated scores (exposure=0 counterfactual) with 50/80/95% CIs\\n  - Convergence diagnostics (Rhat, ESS, divergences)\\n  - Posterior predictive checks\\n\\nDependencies: cmdstanpy (CmdStan 2.38+), numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport cmdstanpy\\n\\nlog = logging.getLogger(__name__)\\n\\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\\nSTAN_MODEL_DIR = \\\"/root/contamcal-irt-calibration/stan_models\\\"\\nSTAN_MODELS = {\\n    \\\"4pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple.stan\\\"),\\n    \\\"2pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_2pl_gamma.stan\\\"),\\n    \\\"vanilla_4pl\\\": os.path.join(STAN_MODEL_DIR, \\\"vanilla_4pl.stan\\\"),\\n    \\\"4pl_gamma_wider\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple_wider.stan\\\"),\\n}\\n\\nDOSAGE_PATTERN = re.compile(r\\\"_d(\\\\d+)(?:_v\\\\d+)?_s(\\\\d+)(_para)?(_aligned)?(?:_v\\\\d+)?$\\\")\\n\\n\\n# ── Data Loading ──\\n\\ndef parse_model_dir_name(dirname):\\n    \\\"\\\"\\\"Extract model name, dosage, seed from directory like Qwen2.5-0.5B_d025_s42.\\\"\\\"\\\"\\n    m = DOSAGE_PATTERN.search(dirname)\\n    if not m:\\n        return None\\n    return {\\n        \\\"dirname\\\": dirname,\\n        \\\"model_name\\\": dirname[:m.start()],\\n        \\\"dosage\\\": int(m.group(1)),\\n        \\\"seed\\\": int(m.group(2)),\\n        \\\"is_para\\\": m.group(3) is not None,\\n        \\\"is_aligned\\\": m.group(4) is not None,\\n    }\\n\\n\\ndef get_train_lr(dirname, checkpoint_dir):\\n    \\\"\\\"\\\"Read lr from checkpoint's train_config.json (D076).\\\"\\\"\\\"\\n    ckpt_name = re.sub(r'(_para)?(_aligned)?$', '', dirname)\\n    config_path = os.path.join(checkpoint_dir, ckpt_name, \\\"train_config.json\\\")\\n    try:\\n        with open(config_path) as f:\\n            return json.load(f).get(\\\"lr\\\")\\n    except (FileNotFoundError, json.JSONDecodeError):\\n        pass\\n    # Fallback: eval dir may have version suffix not in checkpoint name\\n    ckpt_fallback = re.sub(r'_v\\\\d+(?=_s\\\\d+$)', '', ckpt_name)\\n    if ckpt_fallback != ckpt_name:\\n        config_path = os.path.join(checkpoint_dir, ckpt_fallback, \\\"train_config.json\\\")\\n        try:\\n            with open(config_path) as f:\\n                return json.load(f).get(\\\"lr\\\")\\n        except (FileNotFoundError, json.JSONDecodeError):\\n            pass\\n    return None\\n\\n\\ndef load_matrix(path):\\n    \\\"\\\"\\\"Load matrix from .npy, .csv, or .json.\\\"\\\"\\\"\\n    ext = os.path.splitext(path)[1].lower()\\n    if ext == \\\".npy\\\":\\n        return np.load(path)\\n    elif ext == \\\".csv\\\":\\n        return np.loadtxt(path, delimiter=\\\",\\\", skiprows=1)\\n    elif ext == \\\".json\\\":\\n        with open(path) as f:\\n            return np.array(json.load(f))\\n    raise ValueError(f\\\"Unsupported format: {ext}\\\")\\n\\n\\ndef load_eval_results(eval_dir, benchmarks=None, skip_para=True,\\n                      model_scale=None, seed_filter=None, aligned_only=False,\\n                      lr_filter=None, checkpoint_dir=None):\\n    \\\"\\\"\\\"Load per-model eval results into response matrices per benchmark.\\\"\\\"\\\"\\n    eval_path = Path(eval_dir)\\n    model_dirs = sorted([\\n        d for d in eval_path.iterdir()\\n        if d.is_dir() and (d / \\\"eval_results.json\\\").exists()\\n    ])\\n\\n    models = []\\n    for d in model_dirs:\\n        info = parse_model_dir_name(d.name)\\n        if info is None:\\n            log.warning(\\\"Skipping unrecognized dir: %s\\\", d.name)\\n            continue\\n        if skip_para and info[\\\"is_para\\\"]:\\n            continue\\n        if aligned_only and not info.get(\\\"is_aligned\\\", False):\\n            log.info(\\\"Skipping non-aligned dir: %s\\\", d.name)\\n            continue\\n        if model_scale and model_scale not in d.name:\\n            log.info\\n\\n... [截断: 输出过长，省略 8864 字符] ...\\n\\ngent_count\\\"] = divergent\\n    diag[\\\"divergent_pct\\\"] = round(100.0 * divergent / total_draws, 4)\\n    diag[\\\"divergent_ok\\\"] = diag[\\\"divergent_pct\\\"] < 0.1\\n    diag[\\\"total_draws\\\"] = total_draws\\n    diag[\\\"all_ok\\\"] = all(diag.get(k, True) for k in [\\\"rhat_ok\\\", \\\"ess_ok\\\", \\\"divergent_ok\\\"])\\n\\n    return diag\\n\\n\\ndef posterior_predictive_check(fit, y):\\n    \\\"\\\"\\\"Posterior predictive check: compare observed vs predicted accuracy.\\\"\\\"\\\"\\n    cal_draws = fit.stan_variable(\\\"calibrated_score\\\")  # (n_draws, N_models)\\n    obs_acc = y.mean()\\n    pred_acc_per_draw = cal_draws.mean(axis=1)\\n    ppp = float(np.mean(pred_acc_per_draw >= obs_acc))\\n\\n    obs_model_acc = y.mean(axis=1)\\n    pred_model_acc = np.mean(cal_draws, axis=0)\\n    residual_mae = float(np.mean(np.abs(pred_model_acc - obs_model_acc)))\\n\\n    return {\\n        \\\"overall_ppp\\\": round(ppp, 4),\\n        \\\"obs_mean_acc\\\": round(float(obs_acc), 4),\\n        \\\"pred_mean_acc\\\": round(float(pred_acc_per_draw.mean()), 4),\\n        \\\"residual_mae\\\": round(residual_mae, 4),\\n    }\\n\\n\\n# ── Result Extraction ──\\n\\ndef _summarize_vector(draws):\\n    \\\"\\\"\\\"Summarize posterior draws into point estimates and quantiles.\\\"\\\"\\\"\\n    return {\\n        \\\"mean\\\": np.round(np.mean(draws, axis=0), 4).tolist(),\\n        \\\"sd\\\": np.round(np.std(draws, axis=0), 4).tolist(),\\n        \\\"q025\\\": np.round(np.percentile(draws, 2.5, axis=0), 4).tolist(),\\n        \\\"q975\\\": np.round(np.percentile(draws, 97.5, axis=0), 4).tolist(),\\n        \\\"q10\\\": np.round(np.percentile(draws, 10, axis=0), 4).tolist(),\\n        \\\"q90\\\": np.round(np.percentile(draws, 90, axis=0), 4).tolist(),\\n        \\\"q25\\\": np.round(np.percentile(draws, 25, axis=0), 4).tolist(),\\n        \\\"q75\\\": np.round(np.percentile(draws, 75, axis=0), 4).tolist(),\\n    }\\n\\n\\ndef extract_results(fit, y, model_type):\\n    \\\"\\\"\\\"Extract all posterior summaries from fitted model.\\\"\\\"\\\"\\n    results = {}\\n\\n    # Gamma\\n    if model_type != \\\"vanilla_4pl\\\":\\n        gamma_draws = fit.stan_variable(\\\"gamma\\\")\\n        results[\\\"gamma\\\"] = {\\n            \\\"mean\\\": round(float(np.mean(gamma_draws)), 4),\\n            \\\"sd\\\": round(float(np.std(gamma_draws)), 4),\\n            \\\"q025\\\": round(float(np.percentile(gamma_draws, 2.5)), 4),\\n            \\\"q975\\\": round(float(np.percentile(gamma_draws, 97.5)), 4),\\n            \\\"q10\\\": round(float(np.percentile(gamma_draws, 10)), 4),\\n            \\\"q90\\\": round(float(np.percentile(gamma_draws, 90)), 4),\\n            \\\"q25\\\": round(float(np.percentile(gamma_draws, 25)), 4),\\n            \\\"q75\\\": round(float(np.percentile(gamma_draws, 75)), 4),\\n            \\\"ci_excludes_zero\\\": bool(\\n                np.percentile(gamma_draws, 2.5) > 0 or\\n                np.percentile(gamma_draws, 97.5) < 0\\n            ),\\n        }\\n\\n    # Theta\\n    theta_draws = fit.stan_variable(\\\"theta\\\")\\n    results[\\\"theta\\\"] = {\\n        \\\"mean\\\": np.round(np.mean(theta_draws, axis=0), 4).tolist(),\\n        \\\"sd\\\": np.round(np.std(theta_draws, axis=0), 4).tolist(),\\n    }\\n\\n    # Item parameters\\n    for param in [\\\"a\\\", \\\"b\\\"]:\\n        draws = fit.stan_variable(param)\\n        results[param] = {\\n            \\\"mean\\\": np.round(np.mean(draws, axis=0), 4).tolist(),\\n            \\\"sd\\\": np.round(np.std(draws, axis=0), 4).tolist(),\\n        }\\n    if model_type != \\\"2pl_gamma\\\":\\n        for param in [\\\"c\\\", \\\"d\\\"]:\\n            draws = fit.stan_variable(param)\\n            results[param] = {\\n                \\\"mean\\\": np.round(np.mean(draws, axis=0), 4).tolist(),\\n                \\\"sd\\\": np.round(np.std(draws, axis=0), 4).tolist(),\\n            }\\n\\n    # Calibrated scores with multi-level CIs\\n    cal_draws = fit.stan_variable(\\\"calibrated_score\\\")\\n    results[\\\"calibrated_scores\\\"] = _summarize_vector(cal_draws)\\n\\n    # Raw accuracy for reference\\n    results[\\\"raw_accuracy\\\"] = np.round(y.mean(axis=1), 4).tolist()\\n\\n    return results\\n\\n\\n# ── Per-Benchmark Fitting ──\\n\\ndef run_benchmark_fit(bench_name, y, exposure, model_type, args, **kwargs):\\n    \\\"\\\"\\\"Fit IRT model for a single benchmark via NUTS.\\\"\\\"\\\"\\n    N_models, N_items = y.shape\\n    log.info(\\\"=== %s: %d models x %d items ===\\\",\\n             bench_name, N_models, N_items)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 96_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the remote `run_irt_calibration.py` module. Key functions:

- `load_pooled_eval_results(eval_dir, scales, benchmarks, ...)` → loads multi-scale data with model `scale` tags
- `prepare_stan_data(y, exposure, model_type)` → prepares Stan data dict
- `fit_stan_model(stan_file, stan_data, ...)` → fits via CmdStanPy NUTS
- `check_convergence(fit)` → returns dict with max_rhat, min_ess, divergent_count, etc.


- `posterior_predictive_check(fit, y)` → runs PPC
- `extract_results(fit, y, model_type)` → extracts gamma, theta, item params, and calibrated scores
- `_summarize_vector(draws)` → computes mean, sd, and quantiles
- `STAN_MODELS` → maps model types to their stan file paths

The existing `run_stratified_irt.py` already implements per-scale IRT (Scheme B), so the task is to add a `--stratify-by-scale` flag to the pooled script to give it the same capability. I need to figure out whether modifying `run_pooled_4bench_irt.py` or creating a new approach makes more sense.

Since the constraint is to modify existing scripts rather than create new ones, I'll enhance `run_pooled_4bench_irt.py` with the stratification flag. When enabled, it'll filter each scale separately and run per-benchmark fits for that scale, then output a summary table with gamma estimates, confidence intervals, convergence diagnostics, and model counts organized by scale and benchmark.

Now I'm adding the `--stratify-by-scale` argument to the argument parser...

Implementing the helper function and main stratified analysis loop... I'm checking if each scale has enough dosage variation to fit the model properly, then iterating through benchmarks to run individual IRT fits for each scale-benchmark combination, storing results as I go. Building the output structure...

Now I need to handle where these results get saved—I'll create a separate subdirectory for scale-stratified analysis rather than mixing it with the main output. I'm also thinking through the edge cases: when certain scale-benchmark combinations have no data (like 0.5B models on MMLU), those cells will be empty and return None, which the summary will correctly show as 0 models. Small scale groups are already handled by the existing fit logic, and single dosage levels might cause issues with gamma estimation, but I'll address that if it comes up.

Writing the implementation now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "65e98785-9efc-4e28-80e1-cc3c388d1bda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C4C6s6NrYrpDMV6uXn7Cji",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3783,
      "cache_read_input_tokens": 68757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3783
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

_source line 97_

Now I have full understanding of the codebase. The remote `run_irt_calibration.py` has Stan-based functions that both `run_pooled_4bench_irt.py` and `run_stratified_irt.py` import. 

Key insight: `run_stratified_irt.py` already has Scheme B (per-scale IRT), but the task asks for `--stratify-by-scale` on the pooled script with a specific output format. I'll modify `run_pooled_4bench_irt.py`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "a43b8bdf-ba46-4d0a-8d72-b82637f8c5a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C4C6s6NrYrpDMV6uXn7Cji",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3783,
      "cache_read_input_tokens": 68757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3783
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

_source line 98_

<details open><summary>🔧 Tool call — Read · `toolu_01CQHcjy7mnWXNRRHiRMpsHy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
  "offset": 360,
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
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "86a798ef-ac7c-42cb-b42f-1cf89e8dbd6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C4C6s6NrYrpDMV6uXn7Cji",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3783,
      "cache_read_input_tokens": 68757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3783
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

_source line 99 · 2026-05-16T05:32:10.785Z_

<details><summary>↩ Tool result · `toolu_01CQHcjy7mnWXNRRHiRMpsHy`</summary>

```text
360	
361	def parse_args():
362	    parser = argparse.ArgumentParser(
363	        description="Pooled 4-benchmark IRT analysis (2PL+gamma)"
364	    )
365	    parser.add_argument(
366	        "--exclude-items", type=str, default=None,
367	        help="JSON file with list of item_ids to exclude (e.g. [\"mmlu_42\", \"mmlu_103\"])",
368	    )
369	    parser.add_argument(
370	        "--min-item-variance", type=float, default=0.0,
371	        help="Exclude items with cross-model variance below this threshold (default: 0, disabled)",
372	    )
373	    return parser.parse_args()
374	
375	
376	def main():
377	    logging.basicConfig(
378	        level=logging.INFO,
379	        format="%(asctime)s [%(levelname)s] %(message)s",
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "188baf33-1250-41d1-8169-dda2d0c04515",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
      "content": "\ndef parse_args():\n    parser = argparse.ArgumentParser(\n        description=\"Pooled 4-benchmark IRT analysis (2PL+gamma)\"\n    )\n    parser.add_argument(\n        \"--exclude-items\", type=str, default=None,\n        help=\"JSON file with list of item_ids to exclude (e.g. [\\\"mmlu_42\\\", \\\"mmlu_103\\\"])\",\n    )\n    parser.add_argument(\n        \"--min-item-variance\", type=float, default=0.0,\n        help=\"Exclude items with cross-model variance below this threshold (default: 0, disabled)\",\n    )\n    return parser.parse_args()\n\n\ndef main():\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",",
      "numLines": 20,
      "startLine": 360,
      "totalLines": 542
    }
  }
}
```

</details>

---

### Assistant

_source line 100_

Now I'll implement the changes. Adding `--stratify-by-scale` to `run_pooled_4bench_irt.py` with:
1. `filter_data_by_scale()` helper
2. Scale-stratified analysis loop
3. Summary table output (JSON + stdout)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "c34d173d-e8a7-4e42-afde-a1bcf2404897",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf4r5fJhmfAUqcDsT8MGwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2665,
      "cache_read_input_tokens": 72540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2665
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

_source line 101_

<details open><summary>🔧 Tool call — Edit · `toolu_01DWwg2Vdtjez1crSX73kk68`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
  "old_string": "def build_oracle_exposure(dosages, n_items):\n    \"\"\"Oracle exposure: dosage_fraction * uniform tau.\"\"\"\n    max_d = dosages.max() if dosages.max() > 0 else 1.0\n    fracs = dosages / max_d\n    return np.outer(fracs, np.ones(n_items))",
  "new_string": "def filter_data_by_scale(data, target_scale):\n    \"\"\"Filter pooled data to only include models of a single scale.\"\"\"\n    keep = np.array([m.get(\"scale\", \"\") == target_scale for m in data[\"models\"]])\n    if not keep.any():\n        return None\n    return {\n        \"models\": [m for m, k in zip(data[\"models\"], keep) if k],\n        \"dosages\": data[\"dosages\"][keep],\n        \"benchmarks\": {\n            bench: {\n                \"responses\": bd[\"responses\"][keep],\n                \"n_items\": bd[\"n_items\"],\n                \"valid_mask\": bd[\"valid_mask\"][keep],\n            }\n            for bench, bd in data[\"benchmarks\"].items()\n        },\n    }\n\n\ndef build_oracle_exposure(dosages, n_items):\n    \"\"\"Oracle exposure: dosage_fraction * uniform tau.\"\"\"\n    max_d = dosages.max() if dosages.max() > 0 else 1.0\n    fracs = dosages / max_d\n    return np.outer(fracs, np.ones(n_items))"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "4fb2acac-c77e-4f8d-b352-84d5956e50d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf4r5fJhmfAUqcDsT8MGwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2665,
      "cache_read_input_tokens": 72540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2665
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

_source line 102 · 2026-05-16T05:32:19.155Z_

<details><summary>↩ Tool result · `toolu_01DWwg2Vdtjez1crSX73kk68`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "d963de2b-6a37-4ac0-b6a4-c3943a116a31",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
    "oldString": "def build_oracle_exposure(dosages, n_items):\n    \"\"\"Oracle exposure: dosage_fraction * uniform tau.\"\"\"\n    max_d = dosages.max() if dosages.max() > 0 else 1.0\n    fracs = dosages / max_d\n    return np.outer(fracs, np.ones(n_items))",
    "newString": "def filter_data_by_scale(data, target_scale):\n    \"\"\"Filter pooled data to only include models of a single scale.\"\"\"\n    keep = np.array([m.get(\"scale\", \"\") == target_scale for m in data[\"models\"]])\n    if not keep.any():\n        return None\n    return {\n        \"models\": [m for m, k in zip(data[\"models\"], keep) if k],\n        \"dosages\": data[\"dosages\"][keep],\n        \"benchmarks\": {\n            bench: {\n                \"responses\": bd[\"responses\"][keep],\n                \"n_items\": bd[\"n_items\"],\n                \"valid_mask\": bd[\"valid_mask\"][keep],\n            }\n            for bench, bd in data[\"benchmarks\"].items()\n        },\n    }\n\n\ndef build_oracle_exposure(dosages, n_items):\n    \"\"\"Oracle exposure: dosage_fraction * uniform tau.\"\"\"\n    max_d = dosages.max() if dosages.max() > 0 else 1.0\n    fracs = dosages / max_d\n    return np.outer(fracs, np.ones(n_items))",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nPooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.\n\nRuns:\n  1. Per-benchmark IRT fits (with per-benchmark model exclusions)\n  2. Joint fit (shared gamma) across benchmarks using intersection models\n\nExclusion rules:\n  D044: GSM8K exclude d000 configs (format confound)\n  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept\n  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)\n  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)\n\nExposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\n\nsys.path.insert(0, \"/root/contamcal-irt-calibration/exp006\")\nfrom run_irt_calibration import (\n    load_pooled_eval_results,\n    prepare_stan_data,\n    fit_stan_model,\n    check_convergence,\n    posterior_predictive_check,\n    extract_results,\n    _summarize_vector,\n    STAN_MODELS,\n)\n\nlog = logging.getLogger(__name__)\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\", \"humaneval\"]\nSCALES = [\"0.5B\", \"1.5B\", \"3B\"]\nMODEL_TYPE = \"2pl_gamma\"\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\n\nOUTPUT_DIR = Path(\"/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl\")\nEVAL_DIR = \"/root/autodl-tmp/exp001/eval_results\"\n\n\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\n    \"\"\"Apply D044/D045/D046/D047/D018 per-benchmark exclusions.\"\"\"\n    keep = np.ones(len(models), dtype=bool)\n    reasons = []\n\n    for i, m in enumerate(models):\n        dirname = m.get(\"dirname\", \"\")\n        scale = m.get(\"scale\", \"\")\n        dosage = m.get(\"dosage\", 0)\n\n        # D046/D047: base pretrained\n        if \"base_pretrained\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D046/D047: {dirname} (base pretrained)\")\n            continue\n\n        # D018: deprecated check (dirname contains DEPRECATED)\n        if \"DEPRECATED\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D018: {dirname} (deprecated)\")\n            continue\n\n        # D045: 0.5B MMLU/ARC excluded (position bias)\n        if \"0.5B\" in scale and benchmark in (\"mmlu\", \"arc_challenge\"):\n            keep[i] = False\n            reasons.append(f\"  D045: {dirname} (0.5B on {benchmark})\")\n            continue\n\n        # D044: GSM8K exclude d000 (format confound)\n        if benchmark == \"gsm8k\" and dosage == 0:\n            keep[i] = False\n            reasons.append(f\"  D044: {dirname} (d000 on gsm8k)\")\n            continue\n\n        # Instruct model (no dosage pattern) - keep if aligned\n        # but skip if not part of dose-response (dosage not parseable)\n        # Actually Instruct models have dosage=base, which won't parse\n        # as dosage int. They'll appear with dosage=0 from the loader\n        # if dirname ends with _aligned without _dXXX pattern.\n        # The loader sets dosage from parsing, so Instruct models\n        # are already excluded by parse_model_dir_name returning None.\n\n    if reasons:\n        log.info(\"Excluded from %s (%d models):\", benchmark, len(reasons))\n        for r in reasons[:10]:\n            log.info(r)\n        if len(reasons) > 10:\n            log.info(\"  ... and %d more\", len(reasons) - 10)\n\n    return (\n        [m for m, k in zip(models, keep) if k],\n        dosages[keep],\n        responses[keep],\n        valid_mask[keep],\n    )\n\n\ndef build_oracle_exposure(dosages, n_items):\n    \"\"\"Oracle exposure: dosage_fraction * uniform tau.\"\"\"\n    max_d = dosages.max() if dosages.max() > 0 else 1.0\n    fracs = dosages / max_d\n    return np.outer(fracs, np.ones(n_items))\n\n\ndef filter_items(responses, benchmark, exclude_set=None, min_variance=0.0):\n    \"\"\"Remove items by exclusion list and/or low cross-model variance.\n\n    Returns (filtered_responses, kept_indices, stats_dict).\n    \"\"\"\n    n_models, n_items = responses.shape\n    keep = np.ones(n_items, dtype=bool)\n\n    n_excluded_by_list = 0\n    if exclude_set:\n        for j in range(n_items):\n            if f\"{benchmark}_{j}\" in exclude_set:\n                keep[j] = False\n                n_excluded_by_list += 1\n\n    n_excluded_by_var = 0\n    if min_variance > 0:\n        item_var = np.var(responses, axis=0)\n        low_var = item_var < min_variance\n        low_var &= keep\n        n_excluded_by_var = int(low_var.sum())\n        keep[low_var] = False\n\n    kept_indices = np.where(keep)[0]\n    stats = {\n        \"original\": n_items,\n        \"excluded_by_list\": n_excluded_by_list,\n        \"excluded_by_variance\": n_excluded_by_var,\n        \"remaining\": int(keep.sum()),\n    }\n    return responses[:, keep], kept_indices, stats\n\n\ndef run_single_benchmark_fit(bench, data, args_dict, exclude_set=None, min_item_variance=0.0):\n    \"\"\"Run IRT fit for a single benchmark with exclusions.\"\"\"\n    if bench not in data[\"benchmarks\"]:\n        log.warning(\"Benchmark %s not in data, skipping\", bench)\n        return None\n\n    bd = data[\"benchmarks\"][bench]\n    models_filt, dosages_filt, responses_filt, valid_filt = apply_per_benchmark_exclusions(\n        data[\"models\"], data[\"dosages\"],\n        bd[\"responses\"], bd[\"valid_mask\"], bench\n    )\n\n    # Apply valid mask\n    if not valid_filt.all():\n        active = valid_filt.astype(bool)\n        models_filt = [m for m, v in zip(models_filt, active) if v]\n        dosages_filt = dosages_filt[active]\n        responses_filt = responses_filt[active]\n\n    n_models = len(models_filt)\n    n_items = bd[\"n_items\"]\n\n    if exclude_set or min_item_variance > 0:\n        responses_filt, kept_indices, fstats = filter_items(\n            responses_filt, bench, exclude_set, min_item_variance\n        )\n        n_items = fstats[\"remaining\"]\n        log.info(\"[%s] Item filter: %d -> %d (list=%d, variance=%d)\",\n                 bench, fstats[\"original\"], n_items,\n                 fstats[\"excluded_by_list\"], fstats[\"excluded_by_variance\"])\n\n    log.info(\"[%s] N_models=%d, N_items=%d\", bench, n_models, n_items)\n\n    if n_models < 3:\n        log.warning(\"[%s] Too few models (%d), skipping\", bench, n_models)\n        return None\n\n    exposure = build_oracle_exposure(dosages_filt, n_items)\n    stan_data = prepare_stan_data(responses_filt, exposure, MODEL_TYPE)\n\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, responses_filt)\n    results = extract_results(fit, responses_filt, MODEL_TYPE)\n\n    return {\n        \"benchmark\": bench,\n        \"n_models\": n_models,\n        \"n_items\": n_items,\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in models_filt],\n        \"dosages\": dosages_filt.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n    }\n\n\ndef run_joint_fit(data, benchmarks_to_include, args_dict, exclude_set=None, min_item_variance=0.0):\n    \"\"\"Concatenate benchmark items and fit shared-gamma model.\n\n    Uses intersection of valid models across all benchmarks (after exclusions).\n    \"\"\"\n    per_bench_filtered = {}\n    for bench in benchmarks_to_include:\n        if bench not in data[\"benchmarks\"]:\n            continue\n        bd = data[\"benchmarks\"][bench]\n        models_f, dosages_f, resp_f, valid_f = apply_per_benchmark_exclusions(\n            data[\"models\"], data[\"dosages\"],\n            bd[\"responses\"], bd[\"valid_mask\"], bench\n        )\n        if not valid_f.all():\n            active = valid_f.astype(bool)\n            models_f = [m for m, v in zip(models_f, active) if v]\n            dosages_f = dosages_f[active]\n            resp_f = resp_f[active]\n\n        per_bench_filtered[bench] = {\n            \"models\": models_f,\n            \"dosages\": dosages_f,\n            \"responses\": resp_f,\n            \"n_items\": bd[\"n_items\"],\n        }\n\n    # Find intersection of valid model dirnames across benchmarks\n    dirname_sets = [set(m[\"dirname\"] for m in bf[\"models\"])\n                    for bf in per_bench_filtered.values()]\n    common_dirnames = set.intersection(*dirname_sets) if dirname_sets else set()\n    log.info(\"Joint fit: %d common models across %d benchmarks\",\n             len(common_dirnames), len(per_bench_filtered))\n\n    if len(common_dirnames) < 3:\n        log.warning(\"Too few common models (%d) for joint fit\", len(common_dirnames))\n        return None\n\n    # Build concatenated matrices using common model order\n    ref_bench = list(per_bench_filtered.keys())[0]\n    ref_models = per_bench_filtered[ref_bench][\"models\"]\n    ordered_dirnames = [m[\"dirname\"] for m in ref_models if m[\"dirname\"] in common_dirnames]\n\n    all_y = []\n    all_exp = []\n    slices = {}\n    col_offset = 0\n    joint_models = None\n    joint_dosages = None\n\n    for bench, bf in per_bench_filtered.items():\n        dirname_to_idx = {m[\"dirname\"]: i for i, m in enumerate(bf[\"models\"])}\n        indices = [dirname_to_idx[d] for d in ordered_dirnames]\n\n        resp_ordered = bf[\"responses\"][indices]\n        dosages_ordered = bf[\"dosages\"][indices]\n        n_items = bf[\"n_items\"]\n\n        if exclude_set or min_item_variance > 0:\n            resp_ordered, kept_indices, fstats = filter_items(\n                resp_ordered, bench, exclude_set, min_item_variance\n            )\n            n_items = fstats[\"remaining\"]\n            log.info(\"[joint/%s] Item filter: %d -> %d (list=%d, variance=%d)\",\n                     bench, fstats[\"original\"], n_items,\n                     fstats[\"excluded_by_list\"], fstats[\"excluded_by_variance\"])\n\n        exposure = build_oracle_exposure(dosages_ordered, n_items)\n\n        all_y.append(resp_ordered)\n        all_exp.append(exposure)\n        slices[bench] = (col_offset, col_offset + n_items)\n        col_offset += n_items\n\n        if joint_models is None:\n            joint_models = [bf[\"models\"][i] for i in indices]\n            joint_dosages = dosages_ordered\n\n    y_concat = np.concatenate(all_y, axis=1)\n    exp_concat = np.concatenate(all_exp, axis=1)\n\n    n_models, n_total = y_concat.shape\n    log.info(\"Joint fit: %d models x %d total items\", n_models, n_total)\n    log.info(\"Joint fit slices: %s\", {b: f\"{s[0]}-{s[1]}\" for b, s in slices.items()})\n\n    stan_data = prepare_stan_data(y_concat, exp_concat, MODEL_TYPE)\n\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, y_concat)\n    results = extract_results(fit, y_concat, MODEL_TYPE)\n\n    # Per-benchmark calibrated scores from joint model\n    gamma_draws = fit.stan_variable(\"gamma\")\n    theta_draws = fit.stan_variable(\"theta\")\n    a_draws = fit.stan_variable(\"a\")\n    b_draws = fit.stan_variable(\"b\")\n\n    per_bench_cal = {}\n    for bench, (start, end) in slices.items():\n        n_bench_items = end - start\n        n_draws = gamma_draws.shape[0]\n        bench_cal = np.zeros((n_draws, n_models))\n        for draw in range(n_draws):\n            for i in range(n_models):\n                total = 0.0\n                for j in range(start, end):\n                    eta_clean = a_draws[draw, j] * (theta_draws[draw, i] - b_draws[draw, j])\n                    total += 1.0 / (1.0 + np.exp(-eta_clean))\n                bench_cal[draw, i] = total / n_bench_items\n        per_bench_cal[bench] = {\n            \"mean\": bench_cal.mean(axis=0).tolist(),\n            \"sd\": bench_cal.std(axis=0).tolist(),\n        }\n\n    return {\n        \"mode\": \"joint_fit_4bench\",\n        \"model_type\": MODEL_TYPE,\n        \"n_models\": n_models,\n        \"n_total_items\": n_total,\n        \"benchmark_slices\": {k: list(v) for k, v in slices.items()},\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in joint_models],\n        \"dosages\": joint_dosages.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"global_gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n        \"calibrated_scores_per_benchmark\": per_bench_cal,\n    }\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(\n        description=\"Pooled 4-benchmark IRT analysis (2PL+gamma)\"\n    )\n    parser.add_argument(\n        \"--exclude-items\", type=str, default=None,\n        help=\"JSON file with list of item_ids to exclude (e.g. [\\\"mmlu_42\\\", \\\"mmlu_103\\\"])\",\n    )\n    parser.add_argument(\n        \"--min-item-variance\", type=float, default=0.0,\n        help=\"Exclude items with cross-model variance below this threshold (default: 0, disabled)\",\n    )\n    return parser.parse_args()\n\n\ndef main():\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    args = parse_args()\n\n    exclude_set = None\n    if args.exclude_items:\n        with open(args.exclude_items) as f:\n            exclude_list = json.load(f)\n        exclude_set = set(exclude_list)\n        log.info(\"Loaded %d item_ids to exclude from %s\", len(exclude_set), args.exclude_items)\n\n    args_dict = {\n        \"chains\": 4,\n        \"warmup\": 1000,\n        \"samples\": 1000,\n        \"adapt_delta\": 0.95,\n        \"max_treedepth\": 12,\n        \"seed\": 42,\n        \"parallel_chains\": 1,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    log.info(\"Loading pooled eval results: scales=%s, benchmarks=%s\", SCALES, BENCHMARKS)\n    t0 = time.time()\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n    )\n    log.info(\"Loaded %d models in %.1fs\", len(data[\"models\"]), time.time() - t0)\n    log.info(\"Dosages: %s\", data[\"dosages\"].tolist())\n    log.info(\"Benchmarks: %s\", list(data[\"benchmarks\"].keys()))\n\n    all_results = {\n        \"config\": {\n            \"model_type\": MODEL_TYPE,\n            \"scales\": SCALES,\n            \"benchmarks\": BENCHMARKS,\n            \"exposure\": \"oracle_dosage\",\n            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",\n                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],\n            \"item_filter\": {\n                \"exclude_items_file\": args.exclude_items,\n                \"exclude_items_count\": len(exclude_set) if exclude_set else 0,\n                \"min_item_variance\": args.min_item_variance,\n            },\n            \"stan_config\": args_dict,\n        },\n        \"per_benchmark\": {},\n        \"joint_fit\": None,\n    }\n\n    # Phase 1: Per-benchmark IRT fits\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 1: Per-benchmark IRT fits\")\n    log.info(\"=\" * 60)\n\n    for bench in BENCHMARKS:\n        log.info(\"-\" * 40)\n        log.info(\"Fitting %s...\", bench)\n        result = run_single_benchmark_fit(\n            bench, data, args_dict, exclude_set, args.min_item_variance\n        )\n        if result:\n            all_results[\"per_benchmark\"][bench] = result\n            g = result[\"gamma\"]\n            d = result[\"diagnostics\"]\n            log.info(\"[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                     bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                     d.get(\"divergent_count\", 0))\n\n            bench_dir = OUTPUT_DIR / bench\n            bench_dir.mkdir(parents=True, exist_ok=True)\n            with open(bench_dir / \"irt_results.json\", \"w\") as f:\n                json.dump(result, f, indent=2)\n\n    # Phase 2: Joint fit (shared gamma)\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 2: Joint fit (shared gamma across benchmarks)\")\n    log.info(\"=\" * 60)\n\n    included_benchmarks = list(all_results[\"per_benchmark\"].keys())\n    joint_result = run_joint_fit(\n        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance\n    )\n    if joint_result:\n        all_results[\"joint_fit\"] = joint_result\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        log.info(\"JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                 g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                 d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                 d.get(\"divergent_count\", 0))\n\n        with open(OUTPUT_DIR / \"joint_fit_results.json\", \"w\") as f:\n            json.dump(joint_result, f, indent=2)\n\n    # Save full results\n    with open(OUTPUT_DIR / \"pooled_4bench_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Print summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)\")\n    print(\"=\" * 60)\n\n    if joint_result:\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        ppc = joint_result[\"posterior_predictive\"]\n\n        # Coverage from calibrated scores\n        cal = joint_result[\"calibrated_scores\"]\n        if \"ci95_lower\" in cal and \"ci95_upper\" in cal:\n            lowers = np.array(cal[\"ci95_lower\"])\n            uppers = np.array(cal[\"ci95_upper\"])\n            # Ground truth approximation: d0 models have raw accuracy as truth\n            dosages_arr = np.array(joint_result[\"dosages\"])\n            # For d0 models, calibrated score IS the ground truth\n            # For d>0 models, compare calibrated CI with d0 mean\n            # This is a simplified coverage check\n            n_total = len(dosages_arr)\n            in_ci = 0\n            for i in range(n_total):\n                # Coverage: does 95% CI contain a reasonable reference?\n                # For overall coverage, check if CI width > 0\n                if uppers[i] > lowers[i]:\n                    in_ci += 1\n            coverage = in_ci / n_total * 100 if n_total > 0 else 0\n            print(f\"COVERAGE: C95={coverage:.0f}% (all CIs valid)\")\n        else:\n            # Use mean/sd to compute coverage\n            means = np.array(cal.get(\"mean\", []))\n            sds = np.array(cal.get(\"sd\", []))\n            print(f\"COVERAGE: need ground truth reference for proper C95\")\n\n        print(f\"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, \"\n              f\"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]\")\n        print(f\"PPP: {ppc.get('overall_ppp', 'N/A')}\")\n        print(f\"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, \"\n              f\"ESS={d.get('min_ess', 'N/A')}, \"\n              f\"divergences={d.get('divergent_count', 'N/A')}\")\n        print(f\"N_MODELS: {joint_result['n_models']}, \"\n              f\"N_ITEMS: {joint_result['n_total_items']}\")\n\n    print(\"\\nPER_BENCHMARK_GAMMA:\")\n    for bench in BENCHMARKS:\n        if bench in all_results[\"per_benchmark\"]:\n            g = all_results[\"per_benchmark\"][bench][\"gamma\"]\n            n = all_results[\"per_benchmark\"][bench][\"n_models\"]\n            ni = all_results[\"per_benchmark\"][bench][\"n_items\"]\n            print(f\"  {bench}: gamma={g['mean']:.4f} \"\n                  f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                  f\"(N={n}, items={ni})\")\n        else:\n            print(f\"  {bench}: SKIPPED\")\n\n    print(f\"\\nResults saved to {OUTPUT_DIR}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 105,
        "oldLines": 6,
        "newStart": 105,
        "newLines": 25,
        "lines": [
          "     )",
          " ",
          " ",
          "+def filter_data_by_scale(data, target_scale):",
          "+    \"\"\"Filter pooled data to only include models of a single scale.\"\"\"",
          "+    keep = np.array([m.get(\"scale\", \"\") == target_scale for m in data[\"models\"]])",
          "+    if not keep.any():",
          "+        return None",
          "+    return {",
          "+        \"models\": [m for m, k in zip(data[\"models\"], keep) if k],",
          "+        \"dosages\": data[\"dosages\"][keep],",
          "+        \"benchmarks\": {",
          "+            bench: {",
          "+                \"responses\": bd[\"responses\"][keep],",
          "+                \"n_items\": bd[\"n_items\"],",
          "+                \"valid_mask\": bd[\"valid_mask\"][keep],",
          "+            }",
          "+            for bench, bd in data[\"benchmarks\"].items()",
          "+        },",
          "+    }",
          "+",
          "+",
          " def build_oracle_exposure(dosages, n_items):",
          "     \"\"\"Oracle exposure: dosage_fraction * uniform tau.\"\"\"",
          "     max_d = dosages.max() if dosages.max() > 0 else 1.0"
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

_source line 103_

Now add the `--stratify-by-scale` argument to `parse_args()`:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "d8920491-d2f3-48a3-974a-530119989261",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tv5rDtH2EXLTARFhrfoLC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 75205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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

_source line 104_

<details open><summary>🔧 Tool call — Edit · `toolu_01XUPgjd5Wv9FUZH2YGgN4Wb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
  "old_string": "    parser.add_argument(\n        \"--min-item-variance\", type=float, default=0.0,\n        help=\"Exclude items with cross-model variance below this threshold (default: 0, disabled)\",\n    )\n    return parser.parse_args()",
  "new_string": "    parser.add_argument(\n        \"--min-item-variance\", type=float, default=0.0,\n        help=\"Exclude items with cross-model variance below this threshold (default: 0, disabled)\",\n    )\n    parser.add_argument(\n        \"--stratify-by-scale\", action=\"store_true\",\n        help=\"Fit IRT independently per model scale (0.5B/1.5B/3B) instead of pooled\",\n    )\n    parser.add_argument(\"--chains\", type=int, default=4)\n    parser.add_argument(\"--warmup\", type=int, default=1000)\n    parser.add_argument(\"--samples\", type=int, default=1000)\n    parser.add_argument(\"--adapt-delta\", type=float, default=0.95)\n    parser.add_argument(\"--max-treedepth\", type=int, default=12)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--parallel-chains\", type=int, default=1)\n    return parser.parse_args()"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "c52dcd78-74f8-4423-826a-e5e727c581ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tv5rDtH2EXLTARFhrfoLC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 75205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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

_source line 105 · 2026-05-16T05:32:26.523Z_

<details><summary>↩ Tool result · `toolu_01XUPgjd5Wv9FUZH2YGgN4Wb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "75a6aff8-bd19-4332-9729-b7126ba79c2f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
    "oldString": "    parser.add_argument(\n        \"--min-item-variance\", type=float, default=0.0,\n        help=\"Exclude items with cross-model variance below this threshold (default: 0, disabled)\",\n    )\n    return parser.parse_args()",
    "newString": "    parser.add_argument(\n        \"--min-item-variance\", type=float, default=0.0,\n        help=\"Exclude items with cross-model variance below this threshold (default: 0, disabled)\",\n    )\n    parser.add_argument(\n        \"--stratify-by-scale\", action=\"store_true\",\n        help=\"Fit IRT independently per model scale (0.5B/1.5B/3B) instead of pooled\",\n    )\n    parser.add_argument(\"--chains\", type=int, default=4)\n    parser.add_argument(\"--warmup\", type=int, default=1000)\n    parser.add_argument(\"--samples\", type=int, default=1000)\n    parser.add_argument(\"--adapt-delta\", type=float, default=0.95)\n    parser.add_argument(\"--max-treedepth\", type=int, default=12)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--parallel-chains\", type=int, default=1)\n    return parser.parse_args()",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nPooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.\n\nRuns:\n  1. Per-benchmark IRT fits (with per-benchmark model exclusions)\n  2. Joint fit (shared gamma) across benchmarks using intersection models\n\nExclusion rules:\n  D044: GSM8K exclude d000 configs (format confound)\n  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept\n  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)\n  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)\n\nExposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\n\nsys.path.insert(0, \"/root/contamcal-irt-calibration/exp006\")\nfrom run_irt_calibration import (\n    load_pooled_eval_results,\n    prepare_stan_data,\n    fit_stan_model,\n    check_convergence,\n    posterior_predictive_check,\n    extract_results,\n    _summarize_vector,\n    STAN_MODELS,\n)\n\nlog = logging.getLogger(__name__)\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\", \"humaneval\"]\nSCALES = [\"0.5B\", \"1.5B\", \"3B\"]\nMODEL_TYPE = \"2pl_gamma\"\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\n\nOUTPUT_DIR = Path(\"/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl\")\nEVAL_DIR = \"/root/autodl-tmp/exp001/eval_results\"\n\n\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\n    \"\"\"Apply D044/D045/D046/D047/D018 per-benchmark exclusions.\"\"\"\n    keep = np.ones(len(models), dtype=bool)\n    reasons = []\n\n    for i, m in enumerate(models):\n        dirname = m.get(\"dirname\", \"\")\n        scale = m.get(\"scale\", \"\")\n        dosage = m.get(\"dosage\", 0)\n\n        # D046/D047: base pretrained\n        if \"base_pretrained\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D046/D047: {dirname} (base pretrained)\")\n            continue\n\n        # D018: deprecated check (dirname contains DEPRECATED)\n        if \"DEPRECATED\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D018: {dirname} (deprecated)\")\n            continue\n\n        # D045: 0.5B MMLU/ARC excluded (position bias)\n        if \"0.5B\" in scale and benchmark in (\"mmlu\", \"arc_challenge\"):\n            keep[i] = False\n            reasons.append(f\"  D045: {dirname} (0.5B on {benchmark})\")\n            continue\n\n        # D044: GSM8K exclude d000 (format confound)\n        if benchmark == \"gsm8k\" and dosage == 0:\n            keep[i] = False\n            reasons.append(f\"  D044: {dirname} (d000 on gsm8k)\")\n            continue\n\n        # Instruct model (no dosage pattern) - keep if aligned\n        # but skip if not part of dose-response (dosage not parseable)\n        # Actually Instruct models have dosage=base, which won't parse\n        # as dosage int. They'll appear with dosage=0 from the loader\n        # if dirname ends with _aligned without _dXXX pattern.\n        # The loader sets dosage from parsing, so Instruct models\n        # are already excluded by parse_model_dir_name returning None.\n\n    if reasons:\n        log.info(\"Excluded from %s (%d models):\", benchmark, len(reasons))\n        for r in reasons[:10]:\n            log.info(r)\n        if len(reasons) > 10:\n            log.info(\"  ... and %d more\", len(reasons) - 10)\n\n    return (\n        [m for m, k in zip(models, keep) if k],\n        dosages[keep],\n        responses[keep],\n        valid_mask[keep],\n    )\n\n\ndef filter_data_by_scale(data, target_scale):\n    \"\"\"Filter pooled data to only include models of a single scale.\"\"\"\n    keep = np.array([m.get(\"scale\", \"\") == target_scale for m in data[\"models\"]])\n    if not keep.any():\n        return None\n    return {\n        \"models\": [m for m, k in zip(data[\"models\"], keep) if k],\n        \"dosages\": data[\"dosages\"][keep],\n        \"benchmarks\": {\n            bench: {\n                \"responses\": bd[\"responses\"][keep],\n                \"n_items\": bd[\"n_items\"],\n                \"valid_mask\": bd[\"valid_mask\"][keep],\n            }\n            for bench, bd in data[\"benchmarks\"].items()\n        },\n    }\n\n\ndef build_oracle_exposure(dosages, n_items):\n    \"\"\"Oracle exposure: dosage_fraction * uniform tau.\"\"\"\n    max_d = dosages.max() if dosages.max() > 0 else 1.0\n    fracs = dosages / max_d\n    return np.outer(fracs, np.ones(n_items))\n\n\ndef filter_items(responses, benchmark, exclude_set=None, min_variance=0.0):\n    \"\"\"Remove items by exclusion list and/or low cross-model variance.\n\n    Returns (filtered_responses, kept_indices, stats_dict).\n    \"\"\"\n    n_models, n_items = responses.shape\n    keep = np.ones(n_items, dtype=bool)\n\n    n_excluded_by_list = 0\n    if exclude_set:\n        for j in range(n_items):\n            if f\"{benchmark}_{j}\" in exclude_set:\n                keep[j] = False\n                n_excluded_by_list += 1\n\n    n_excluded_by_var = 0\n    if min_variance > 0:\n        item_var = np.var(responses, axis=0)\n        low_var = item_var < min_variance\n        low_var &= keep\n        n_excluded_by_var = int(low_var.sum())\n        keep[low_var] = False\n\n    kept_indices = np.where(keep)[0]\n    stats = {\n        \"original\": n_items,\n        \"excluded_by_list\": n_excluded_by_list,\n        \"excluded_by_variance\": n_excluded_by_var,\n        \"remaining\": int(keep.sum()),\n    }\n    return responses[:, keep], kept_indices, stats\n\n\ndef run_single_benchmark_fit(bench, data, args_dict, exclude_set=None, min_item_variance=0.0):\n    \"\"\"Run IRT fit for a single benchmark with exclusions.\"\"\"\n    if bench not in data[\"benchmarks\"]:\n        log.warning(\"Benchmark %s not in data, skipping\", bench)\n        return None\n\n    bd = data[\"benchmarks\"][bench]\n    models_filt, dosages_filt, responses_filt, valid_filt = apply_per_benchmark_exclusions(\n        data[\"models\"], data[\"dosages\"],\n        bd[\"responses\"], bd[\"valid_mask\"], bench\n    )\n\n    # Apply valid mask\n    if not valid_filt.all():\n        active = valid_filt.astype(bool)\n        models_filt = [m for m, v in zip(models_filt, active) if v]\n        dosages_filt = dosages_filt[active]\n        responses_filt = responses_filt[active]\n\n    n_models = len(models_filt)\n    n_items = bd[\"n_items\"]\n\n    if exclude_set or min_item_variance > 0:\n        responses_filt, kept_indices, fstats = filter_items(\n            responses_filt, bench, exclude_set, min_item_variance\n        )\n        n_items = fstats[\"remaining\"]\n        log.info(\"[%s] Item filter: %d -> %d (list=%d, variance=%d)\",\n                 bench, fstats[\"original\"], n_items,\n                 fstats[\"excluded_by_list\"], fstats[\"excluded_by_variance\"])\n\n    log.info(\"[%s] N_models=%d, N_items=%d\", bench, n_models, n_items)\n\n    if n_models < 3:\n        log.warning(\"[%s] Too few models (%d), skipping\", bench, n_models)\n        return None\n\n    exposure = build_oracle_exposure(dosages_filt, n_items)\n    stan_data = prepare_stan_data(responses_filt, exposure, MODEL_TYPE)\n\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, responses_filt)\n    results = extract_results(fit, responses_filt, MODEL_TYPE)\n\n    return {\n        \"benchmark\": bench,\n        \"n_models\": n_models,\n        \"n_items\": n_items,\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in models_filt],\n        \"dosages\": dosages_filt.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n    }\n\n\ndef run_joint_fit(data, benchmarks_to_include, args_dict, exclude_set=None, min_item_variance=0.0):\n    \"\"\"Concatenate benchmark items and fit shared-gamma model.\n\n    Uses intersection of valid models across all benchmarks (after exclusions).\n    \"\"\"\n    per_bench_filtered = {}\n    for bench in benchmarks_to_include:\n        if bench not in data[\"benchmarks\"]:\n            continue\n        bd = data[\"benchmarks\"][bench]\n        models_f, dosages_f, resp_f, valid_f = apply_per_benchmark_exclusions(\n            data[\"models\"], data[\"dosages\"],\n            bd[\"responses\"], bd[\"valid_mask\"], bench\n        )\n        if not valid_f.all():\n            active = valid_f.astype(bool)\n            models_f = [m for m, v in zip(models_f, active) if v]\n            dosages_f = dosages_f[active]\n            resp_f = resp_f[active]\n\n        per_bench_filtered[bench] = {\n            \"models\": models_f,\n            \"dosages\": dosages_f,\n            \"responses\": resp_f,\n            \"n_items\": bd[\"n_items\"],\n        }\n\n    # Find intersection of valid model dirnames across benchmarks\n    dirname_sets = [set(m[\"dirname\"] for m in bf[\"models\"])\n                    for bf in per_bench_filtered.values()]\n    common_dirnames = set.intersection(*dirname_sets) if dirname_sets else set()\n    log.info(\"Joint fit: %d common models across %d benchmarks\",\n             len(common_dirnames), len(per_bench_filtered))\n\n    if len(common_dirnames) < 3:\n        log.warning(\"Too few common models (%d) for joint fit\", len(common_dirnames))\n        return None\n\n    # Build concatenated matrices using common model order\n    ref_bench = list(per_bench_filtered.keys())[0]\n    ref_models = per_bench_filtered[ref_bench][\"models\"]\n    ordered_dirnames = [m[\"dirname\"] for m in ref_models if m[\"dirname\"] in common_dirnames]\n\n    all_y = []\n    all_exp = []\n    slices = {}\n    col_offset = 0\n    joint_models = None\n    joint_dosages = None\n\n    for bench, bf in per_bench_filtered.items():\n        dirname_to_idx = {m[\"dirname\"]: i for i, m in enumerate(bf[\"models\"])}\n        indices = [dirname_to_idx[d] for d in ordered_dirnames]\n\n        resp_ordered = bf[\"responses\"][indices]\n        dosages_ordered = bf[\"dosages\"][indices]\n        n_items = bf[\"n_items\"]\n\n        if exclude_set or min_item_variance > 0:\n            resp_ordered, kept_indices, fstats = filter_items(\n                resp_ordered, bench, exclude_set, min_item_variance\n            )\n            n_items = fstats[\"remaining\"]\n            log.info(\"[joint/%s] Item filter: %d -> %d (list=%d, variance=%d)\",\n                     bench, fstats[\"original\"], n_items,\n                     fstats[\"excluded_by_list\"], fstats[\"excluded_by_variance\"])\n\n        exposure = build_oracle_exposure(dosages_ordered, n_items)\n\n        all_y.append(resp_ordered)\n        all_exp.append(exposure)\n        slices[bench] = (col_offset, col_offset + n_items)\n        col_offset += n_items\n\n        if joint_models is None:\n            joint_models = [bf[\"models\"][i] for i in indices]\n            joint_dosages = dosages_ordered\n\n    y_concat = np.concatenate(all_y, axis=1)\n    exp_concat = np.concatenate(all_exp, axis=1)\n\n    n_models, n_total = y_concat.shape\n    log.info(\"Joint fit: %d models x %d total items\", n_models, n_total)\n    log.info(\"Joint fit slices: %s\", {b: f\"{s[0]}-{s[1]}\" for b, s in slices.items()})\n\n    stan_data = prepare_stan_data(y_concat, exp_concat, MODEL_TYPE)\n\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, y_concat)\n    results = extract_results(fit, y_concat, MODEL_TYPE)\n\n    # Per-benchmark calibrated scores from joint model\n    gamma_draws = fit.stan_variable(\"gamma\")\n    theta_draws = fit.stan_variable(\"theta\")\n    a_draws = fit.stan_variable(\"a\")\n    b_draws = fit.stan_variable(\"b\")\n\n    per_bench_cal = {}\n    for bench, (start, end) in slices.items():\n        n_bench_items = end - start\n        n_draws = gamma_draws.shape[0]\n        bench_cal = np.zeros((n_draws, n_models))\n        for draw in range(n_draws):\n            for i in range(n_models):\n                total = 0.0\n                for j in range(start, end):\n                    eta_clean = a_draws[draw, j] * (theta_draws[draw, i] - b_draws[draw, j])\n                    total += 1.0 / (1.0 + np.exp(-eta_clean))\n                bench_cal[draw, i] = total / n_bench_items\n        per_bench_cal[bench] = {\n            \"mean\": bench_cal.mean(axis=0).tolist(),\n            \"sd\": bench_cal.std(axis=0).tolist(),\n        }\n\n    return {\n        \"mode\": \"joint_fit_4bench\",\n        \"model_type\": MODEL_TYPE,\n        \"n_models\": n_models,\n        \"n_total_items\": n_total,\n        \"benchmark_slices\": {k: list(v) for k, v in slices.items()},\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in joint_models],\n        \"dosages\": joint_dosages.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"global_gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n        \"calibrated_scores_per_benchmark\": per_bench_cal,\n    }\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(\n        description=\"Pooled 4-benchmark IRT analysis (2PL+gamma)\"\n    )\n    parser.add_argument(\n        \"--exclude-items\", type=str, default=None,\n        help=\"JSON file with list of item_ids to exclude (e.g. [\\\"mmlu_42\\\", \\\"mmlu_103\\\"])\",\n    )\n    parser.add_argument(\n        \"--min-item-variance\", type=float, default=0.0,\n        help=\"Exclude items with cross-model variance below this threshold (default: 0, disabled)\",\n    )\n    return parser.parse_args()\n\n\ndef main():\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    args = parse_args()\n\n    exclude_set = None\n    if args.exclude_items:\n        with open(args.exclude_items) as f:\n            exclude_list = json.load(f)\n        exclude_set = set(exclude_list)\n        log.info(\"Loaded %d item_ids to exclude from %s\", len(exclude_set), args.exclude_items)\n\n    args_dict = {\n        \"chains\": 4,\n        \"warmup\": 1000,\n        \"samples\": 1000,\n        \"adapt_delta\": 0.95,\n        \"max_treedepth\": 12,\n        \"seed\": 42,\n        \"parallel_chains\": 1,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    log.info(\"Loading pooled eval results: scales=%s, benchmarks=%s\", SCALES, BENCHMARKS)\n    t0 = time.time()\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n    )\n    log.info(\"Loaded %d models in %.1fs\", len(data[\"models\"]), time.time() - t0)\n    log.info(\"Dosages: %s\", data[\"dosages\"].tolist())\n    log.info(\"Benchmarks: %s\", list(data[\"benchmarks\"].keys()))\n\n    all_results = {\n        \"config\": {\n            \"model_type\": MODEL_TYPE,\n            \"scales\": SCALES,\n            \"benchmarks\": BENCHMARKS,\n            \"exposure\": \"oracle_dosage\",\n            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",\n                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],\n            \"item_filter\": {\n                \"exclude_items_file\": args.exclude_items,\n                \"exclude_items_count\": len(exclude_set) if exclude_set else 0,\n                \"min_item_variance\": args.min_item_variance,\n            },\n            \"stan_config\": args_dict,\n        },\n        \"per_benchmark\": {},\n        \"joint_fit\": None,\n    }\n\n    # Phase 1: Per-benchmark IRT fits\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 1: Per-benchmark IRT fits\")\n    log.info(\"=\" * 60)\n\n    for bench in BENCHMARKS:\n        log.info(\"-\" * 40)\n        log.info(\"Fitting %s...\", bench)\n        result = run_single_benchmark_fit(\n            bench, data, args_dict, exclude_set, args.min_item_variance\n        )\n        if result:\n            all_results[\"per_benchmark\"][bench] = result\n            g = result[\"gamma\"]\n            d = result[\"diagnostics\"]\n            log.info(\"[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                     bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                     d.get(\"divergent_count\", 0))\n\n            bench_dir = OUTPUT_DIR / bench\n            bench_dir.mkdir(parents=True, exist_ok=True)\n            with open(bench_dir / \"irt_results.json\", \"w\") as f:\n                json.dump(result, f, indent=2)\n\n    # Phase 2: Joint fit (shared gamma)\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 2: Joint fit (shared gamma across benchmarks)\")\n    log.info(\"=\" * 60)\n\n    included_benchmarks = list(all_results[\"per_benchmark\"].keys())\n    joint_result = run_joint_fit(\n        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance\n    )\n    if joint_result:\n        all_results[\"joint_fit\"] = joint_result\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        log.info(\"JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                 g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                 d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                 d.get(\"divergent_count\", 0))\n\n        with open(OUTPUT_DIR / \"joint_fit_results.json\", \"w\") as f:\n            json.dump(joint_result, f, indent=2)\n\n    # Save full results\n    with open(OUTPUT_DIR / \"pooled_4bench_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Print summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)\")\n    print(\"=\" * 60)\n\n    if joint_result:\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        ppc = joint_result[\"posterior_predictive\"]\n\n        # Coverage from calibrated scores\n        cal = joint_result[\"calibrated_scores\"]\n        if \"ci95_lower\" in cal and \"ci95_upper\" in cal:\n            lowers = np.array(cal[\"ci95_lower\"])\n            uppers = np.array(cal[\"ci95_upper\"])\n            # Ground truth approximation: d0 models have raw accuracy as truth\n            dosages_arr = np.array(joint_result[\"dosages\"])\n            # For d0 models, calibrated score IS the ground truth\n            # For d>0 models, compare calibrated CI with d0 mean\n            # This is a simplified coverage check\n            n_total = len(dosages_arr)\n            in_ci = 0\n            for i in range(n_total):\n                # Coverage: does 95% CI contain a reasonable reference?\n                # For overall coverage, check if CI width > 0\n                if uppers[i] > lowers[i]:\n                    in_ci += 1\n            coverage = in_ci / n_total * 100 if n_total > 0 else 0\n            print(f\"COVERAGE: C95={coverage:.0f}% (all CIs valid)\")\n        else:\n            # Use mean/sd to compute coverage\n            means = np.array(cal.get(\"mean\", []))\n            sds = np.array(cal.get(\"sd\", []))\n            print(f\"COVERAGE: need ground truth reference for proper C95\")\n\n        print(f\"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, \"\n              f\"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]\")\n        print(f\"PPP: {ppc.get('overall_ppp', 'N/A')}\")\n        print(f\"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, \"\n              f\"ESS={d.get('min_ess', 'N/A')}, \"\n              f\"divergences={d.get('divergent_count', 'N/A')}\")\n        print(f\"N_MODELS: {joint_result['n_models']}, \"\n              f\"N_ITEMS: {joint_result['n_total_items']}\")\n\n    print(\"\\nPER_BENCHMARK_GAMMA:\")\n    for bench in BENCHMARKS:\n        if bench in all_results[\"per_benchmark\"]:\n            g = all_results[\"per_benchmark\"][bench][\"gamma\"]\n            n = all_results[\"per_benchmark\"][bench][\"n_models\"]\n            ni = all_results[\"per_benchmark\"][bench][\"n_items\"]\n            print(f\"  {bench}: gamma={g['mean']:.4f} \"\n                  f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                  f\"(N={n}, items={ni})\")\n        else:\n            print(f\"  {bench}: SKIPPED\")\n\n    print(f\"\\nResults saved to {OUTPUT_DIR}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 389,
        "oldLines": 6,
        "newStart": 389,
        "newLines": 17,
        "lines": [
          "         \"--min-item-variance\", type=float, default=0.0,",
          "         help=\"Exclude items with cross-model variance below this threshold (default: 0, disabled)\",",
          "     )",
          "+    parser.add_argument(",
          "+        \"--stratify-by-scale\", action=\"store_true\",",
          "+        help=\"Fit IRT independently per model scale (0.5B/1.5B/3B) instead of pooled\",",
          "+    )",
          "+    parser.add_argument(\"--chains\", type=int, default=4)",
          "+    parser.add_argument(\"--warmup\", type=int, default=1000)",
          "+    parser.add_argument(\"--samples\", type=int, default=1000)",
          "+    parser.add_argument(\"--adapt-delta\", type=float, default=0.95)",
          "+    parser.add_argument(\"--max-treedepth\", type=int, default=12)",
          "+    parser.add_argument(\"--seed\", type=int, default=42)",
          "+    parser.add_argument(\"--parallel-chains\", type=int, default=1)",
          "     return parser.parse_args()",
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

### Assistant

_source line 106_

Now refactor `main()` to use CLI args for Stan config and add the scale-stratified branch:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "3dbfa0d5-1489-46be-90bf-04f69b0b90f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgQ8PacZ7VmbfKViKzZvUq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 565,
      "cache_read_input_tokens": 75842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 565
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

_source line 107_

<details open><summary>🔧 Tool call — Edit · `toolu_01FpWxebjGZp2nzJjwbGygcF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
  "old_string": "    args_dict = {\n        \"chains\": 4,\n        \"warmup\": 1000,\n        \"samples\": 1000,\n        \"adapt_delta\": 0.95,\n        \"max_treedepth\": 12,\n        \"seed\": 42,\n        \"parallel_chains\": 1,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    log.info(\"Loading pooled eval results: scales=%s, benchmarks=%s\", SCALES, BENCHMARKS)\n    t0 = time.time()\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n    )\n    log.info(\"Loaded %d models in %.1fs\", len(data[\"models\"]), time.time() - t0)\n    log.info(\"Dosages: %s\", data[\"dosages\"].tolist())\n    log.info(\"Benchmarks: %s\", list(data[\"benchmarks\"].keys()))\n\n    all_results = {\n        \"config\": {\n            \"model_type\": MODEL_TYPE,\n            \"scales\": SCALES,\n            \"benchmarks\": BENCHMARKS,\n            \"exposure\": \"oracle_dosage\",\n            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",\n                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],\n            \"item_filter\": {\n                \"exclude_items_file\": args.exclude_items,\n                \"exclude_items_count\": len(exclude_set) if exclude_set else 0,\n                \"min_item_variance\": args.min_item_variance,\n            },\n            \"stan_config\": args_dict,\n        },\n        \"per_benchmark\": {},\n        \"joint_fit\": None,\n    }\n\n    # Phase 1: Per-benchmark IRT fits\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 1: Per-benchmark IRT fits\")\n    log.info(\"=\" * 60)\n\n    for bench in BENCHMARKS:\n        log.info(\"-\" * 40)\n        log.info(\"Fitting %s...\", bench)\n        result = run_single_benchmark_fit(\n            bench, data, args_dict, exclude_set, args.min_item_variance\n        )\n        if result:\n            all_results[\"per_benchmark\"][bench] = result\n            g = result[\"gamma\"]\n            d = result[\"diagnostics\"]\n            log.info(\"[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                     bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                     d.get(\"divergent_count\", 0))\n\n            bench_dir = OUTPUT_DIR / bench\n            bench_dir.mkdir(parents=True, exist_ok=True)\n            with open(bench_dir / \"irt_results.json\", \"w\") as f:\n                json.dump(result, f, indent=2)\n\n    # Phase 2: Joint fit (shared gamma)\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 2: Joint fit (shared gamma across benchmarks)\")\n    log.info(\"=\" * 60)\n\n    included_benchmarks = list(all_results[\"per_benchmark\"].keys())\n    joint_result = run_joint_fit(\n        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance\n    )\n    if joint_result:\n        all_results[\"joint_fit\"] = joint_result\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        log.info(\"JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                 g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                 d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                 d.get(\"divergent_count\", 0))\n\n        with open(OUTPUT_DIR / \"joint_fit_results.json\", \"w\") as f:\n            json.dump(joint_result, f, indent=2)\n\n    # Save full results\n    with open(OUTPUT_DIR / \"pooled_4bench_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Print summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)\")\n    print(\"=\" * 60)\n\n    if joint_result:\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        ppc = joint_result[\"posterior_predictive\"]\n\n        # Coverage from calibrated scores\n        cal = joint_result[\"calibrated_scores\"]\n        if \"ci95_lower\" in cal and \"ci95_upper\" in cal:\n            lowers = np.array(cal[\"ci95_lower\"])\n            uppers = np.array(cal[\"ci95_upper\"])\n            # Ground truth approximation: d0 models have raw accuracy as truth\n            dosages_arr = np.array(joint_result[\"dosages\"])\n            # For d0 models, calibrated score IS the ground truth\n            # For d>0 models, compare calibrated CI with d0 mean\n            # This is a simplified coverage check\n            n_total = len(dosages_arr)\n            in_ci = 0\n            for i in range(n_total):\n                # Coverage: does 95% CI contain a reasonable reference?\n                # For overall coverage, check if CI width > 0\n                if uppers[i] > lowers[i]:\n                    in_ci += 1\n            coverage = in_ci / n_total * 100 if n_total > 0 else 0\n            print(f\"COVERAGE: C95={coverage:.0f}% (all CIs valid)\")\n        else:\n            # Use mean/sd to compute coverage\n            means = np.array(cal.get(\"mean\", []))\n            sds = np.array(cal.get(\"sd\", []))\n            print(f\"COVERAGE: need ground truth reference for proper C95\")\n\n        print(f\"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, \"\n              f\"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]\")\n        print(f\"PPP: {ppc.get('overall_ppp', 'N/A')}\")\n        print(f\"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, \"\n              f\"ESS={d.get('min_ess', 'N/A')}, \"\n              f\"divergences={d.get('divergent_count', 'N/A')}\")\n        print(f\"N_MODELS: {joint_result['n_models']}, \"\n              f\"N_ITEMS: {joint_result['n_total_items']}\")\n\n    print(\"\\nPER_BENCHMARK_GAMMA:\")\n    for bench in BENCHMARKS:\n        if bench in all_results[\"per_benchmark\"]:\n            g = all_results[\"per_benchmark\"][bench][\"gamma\"]\n            n = all_results[\"per_benchmark\"][bench][\"n_models\"]\n            ni = all_results[\"per_benchmark\"][bench][\"n_items\"]\n            print(f\"  {bench}: gamma={g['mean']:.4f} \"\n                  f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                  f\"(N={n}, items={ni})\")\n        else:\n            print(f\"  {bench}: SKIPPED\")\n\n    print(f\"\\nResults saved to {OUTPUT_DIR}\")",
  "new_string": "    args_dict = {\n        \"chains\": args.chains,\n        \"warmup\": args.warmup,\n        \"samples\": args.samples,\n        \"adapt_delta\": args.adapt_delta,\n        \"max_treedepth\": args.max_treedepth,\n        \"seed\": args.seed,\n        \"parallel_chains\": args.parallel_chains,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    log.info(\"Loading pooled eval results: scales=%s, benchmarks=%s\", SCALES, BENCHMARKS)\n    t0 = time.time()\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n    )\n    log.info(\"Loaded %d models in %.1fs\", len(data[\"models\"]), time.time() - t0)\n    log.info(\"Dosages: %s\", data[\"dosages\"].tolist())\n    log.info(\"Benchmarks: %s\", list(data[\"benchmarks\"].keys()))\n\n    if args.stratify_by_scale:\n        run_scale_stratified(data, args_dict, exclude_set, args.min_item_variance)\n    else:\n        run_pooled(data, args_dict, exclude_set, args)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "ad30e56f-d065-4744-996a-5142a5580731",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgQ8PacZ7VmbfKViKzZvUq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 565,
      "cache_read_input_tokens": 75842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 565
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

_source line 108 · 2026-05-16T05:32:59.716Z_

<details><summary>↩ Tool result · `toolu_01FpWxebjGZp2nzJjwbGygcF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "c953e067-c221-4cb6-aeb4-21a7701aed43",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
    "oldString": "    args_dict = {\n        \"chains\": 4,\n        \"warmup\": 1000,\n        \"samples\": 1000,\n        \"adapt_delta\": 0.95,\n        \"max_treedepth\": 12,\n        \"seed\": 42,\n        \"parallel_chains\": 1,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    log.info(\"Loading pooled eval results: scales=%s, benchmarks=%s\", SCALES, BENCHMARKS)\n    t0 = time.time()\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n    )\n    log.info(\"Loaded %d models in %.1fs\", len(data[\"models\"]), time.time() - t0)\n    log.info(\"Dosages: %s\", data[\"dosages\"].tolist())\n    log.info(\"Benchmarks: %s\", list(data[\"benchmarks\"].keys()))\n\n    all_results = {\n        \"config\": {\n            \"model_type\": MODEL_TYPE,\n            \"scales\": SCALES,\n            \"benchmarks\": BENCHMARKS,\n            \"exposure\": \"oracle_dosage\",\n            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",\n                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],\n            \"item_filter\": {\n                \"exclude_items_file\": args.exclude_items,\n                \"exclude_items_count\": len(exclude_set) if exclude_set else 0,\n                \"min_item_variance\": args.min_item_variance,\n            },\n            \"stan_config\": args_dict,\n        },\n        \"per_benchmark\": {},\n        \"joint_fit\": None,\n    }\n\n    # Phase 1: Per-benchmark IRT fits\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 1: Per-benchmark IRT fits\")\n    log.info(\"=\" * 60)\n\n    for bench in BENCHMARKS:\n        log.info(\"-\" * 40)\n        log.info(\"Fitting %s...\", bench)\n        result = run_single_benchmark_fit(\n            bench, data, args_dict, exclude_set, args.min_item_variance\n        )\n        if result:\n            all_results[\"per_benchmark\"][bench] = result\n            g = result[\"gamma\"]\n            d = result[\"diagnostics\"]\n            log.info(\"[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                     bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                     d.get(\"divergent_count\", 0))\n\n            bench_dir = OUTPUT_DIR / bench\n            bench_dir.mkdir(parents=True, exist_ok=True)\n            with open(bench_dir / \"irt_results.json\", \"w\") as f:\n                json.dump(result, f, indent=2)\n\n    # Phase 2: Joint fit (shared gamma)\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 2: Joint fit (shared gamma across benchmarks)\")\n    log.info(\"=\" * 60)\n\n    included_benchmarks = list(all_results[\"per_benchmark\"].keys())\n    joint_result = run_joint_fit(\n        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance\n    )\n    if joint_result:\n        all_results[\"joint_fit\"] = joint_result\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        log.info(\"JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                 g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                 d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                 d.get(\"divergent_count\", 0))\n\n        with open(OUTPUT_DIR / \"joint_fit_results.json\", \"w\") as f:\n            json.dump(joint_result, f, indent=2)\n\n    # Save full results\n    with open(OUTPUT_DIR / \"pooled_4bench_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Print summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)\")\n    print(\"=\" * 60)\n\n    if joint_result:\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        ppc = joint_result[\"posterior_predictive\"]\n\n        # Coverage from calibrated scores\n        cal = joint_result[\"calibrated_scores\"]\n        if \"ci95_lower\" in cal and \"ci95_upper\" in cal:\n            lowers = np.array(cal[\"ci95_lower\"])\n            uppers = np.array(cal[\"ci95_upper\"])\n            # Ground truth approximation: d0 models have raw accuracy as truth\n            dosages_arr = np.array(joint_result[\"dosages\"])\n            # For d0 models, calibrated score IS the ground truth\n            # For d>0 models, compare calibrated CI with d0 mean\n            # This is a simplified coverage check\n            n_total = len(dosages_arr)\n            in_ci = 0\n            for i in range(n_total):\n                # Coverage: does 95% CI contain a reasonable reference?\n                # For overall coverage, check if CI width > 0\n                if uppers[i] > lowers[i]:\n                    in_ci += 1\n            coverage = in_ci / n_total * 100 if n_total > 0 else 0\n            print(f\"COVERAGE: C95={coverage:.0f}% (all CIs valid)\")\n        else:\n            # Use mean/sd to compute coverage\n            means = np.array(cal.get(\"mean\", []))\n            sds = np.array(cal.get(\"sd\", []))\n            print(f\"COVERAGE: need ground truth reference for proper C95\")\n\n        print(f\"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, \"\n              f\"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]\")\n        print(f\"PPP: {ppc.get('overall_ppp', 'N/A')}\")\n        print(f\"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, \"\n              f\"ESS={d.get('min_ess', 'N/A')}, \"\n              f\"divergences={d.get('divergent_count', 'N/A')}\")\n        print(f\"N_MODELS: {joint_result['n_models']}, \"\n              f\"N_ITEMS: {joint_result['n_total_items']}\")\n\n    print(\"\\nPER_BENCHMARK_GAMMA:\")\n    for bench in BENCHMARKS:\n        if bench in all_results[\"per_benchmark\"]:\n            g = all_results[\"per_benchmark\"][bench][\"gamma\"]\n            n = all_results[\"per_benchmark\"][bench][\"n_models\"]\n            ni = all_results[\"per_benchmark\"][bench][\"n_items\"]\n            print(f\"  {bench}: gamma={g['mean']:.4f} \"\n                  f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                  f\"(N={n}, items={ni})\")\n        else:\n            print(f\"  {bench}: SKIPPED\")\n\n    print(f\"\\nResults saved to {OUTPUT_DIR}\")",
    "newString": "    args_dict = {\n        \"chains\": args.chains,\n        \"warmup\": args.warmup,\n        \"samples\": args.samples,\n        \"adapt_delta\": args.adapt_delta,\n        \"max_treedepth\": args.max_treedepth,\n        \"seed\": args.seed,\n        \"parallel_chains\": args.parallel_chains,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    log.info(\"Loading pooled eval results: scales=%s, benchmarks=%s\", SCALES, BENCHMARKS)\n    t0 = time.time()\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n    )\n    log.info(\"Loaded %d models in %.1fs\", len(data[\"models\"]), time.time() - t0)\n    log.info(\"Dosages: %s\", data[\"dosages\"].tolist())\n    log.info(\"Benchmarks: %s\", list(data[\"benchmarks\"].keys()))\n\n    if args.stratify_by_scale:\n        run_scale_stratified(data, args_dict, exclude_set, args.min_item_variance)\n    else:\n        run_pooled(data, args_dict, exclude_set, args)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nPooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.\n\nRuns:\n  1. Per-benchmark IRT fits (with per-benchmark model exclusions)\n  2. Joint fit (shared gamma) across benchmarks using intersection models\n\nExclusion rules:\n  D044: GSM8K exclude d000 configs (format confound)\n  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept\n  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)\n  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)\n\nExposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\n\nsys.path.insert(0, \"/root/contamcal-irt-calibration/exp006\")\nfrom run_irt_calibration import (\n    load_pooled_eval_results,\n    prepare_stan_data,\n    fit_stan_model,\n    check_convergence,\n    posterior_predictive_check,\n    extract_results,\n    _summarize_vector,\n    STAN_MODELS,\n)\n\nlog = logging.getLogger(__name__)\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\", \"humaneval\"]\nSCALES = [\"0.5B\", \"1.5B\", \"3B\"]\nMODEL_TYPE = \"2pl_gamma\"\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\n\nOUTPUT_DIR = Path(\"/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl\")\nEVAL_DIR = \"/root/autodl-tmp/exp001/eval_results\"\n\n\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\n    \"\"\"Apply D044/D045/D046/D047/D018 per-benchmark exclusions.\"\"\"\n    keep = np.ones(len(models), dtype=bool)\n    reasons = []\n\n    for i, m in enumerate(models):\n        dirname = m.get(\"dirname\", \"\")\n        scale = m.get(\"scale\", \"\")\n        dosage = m.get(\"dosage\", 0)\n\n        # D046/D047: base pretrained\n        if \"base_pretrained\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D046/D047: {dirname} (base pretrained)\")\n            continue\n\n        # D018: deprecated check (dirname contains DEPRECATED)\n        if \"DEPRECATED\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D018: {dirname} (deprecated)\")\n            continue\n\n        # D045: 0.5B MMLU/ARC excluded (position bias)\n        if \"0.5B\" in scale and benchmark in (\"mmlu\", \"arc_challenge\"):\n            keep[i] = False\n            reasons.append(f\"  D045: {dirname} (0.5B on {benchmark})\")\n            continue\n\n        # D044: GSM8K exclude d000 (format confound)\n        if benchmark == \"gsm8k\" and dosage == 0:\n            keep[i] = False\n            reasons.append(f\"  D044: {dirname} (d000 on gsm8k)\")\n            continue\n\n        # Instruct model (no dosage pattern) - keep if aligned\n        # but skip if not part of dose-response (dosage not parseable)\n        # Actually Instruct models have dosage=base, which won't parse\n        # as dosage int. They'll appear with dosage=0 from the loader\n        # if dirname ends with _aligned without _dXXX pattern.\n        # The loader sets dosage from parsing, so Instruct models\n        # are already excluded by parse_model_dir_name returning None.\n\n    if reasons:\n        log.info(\"Excluded from %s (%d models):\", benchmark, len(reasons))\n        for r in reasons[:10]:\n            log.info(r)\n        if len(reasons) > 10:\n            log.info(\"  ... and %d more\", len(reasons) - 10)\n\n    return (\n        [m for m, k in zip(models, keep) if k],\n        dosages[keep],\n        responses[keep],\n        valid_mask[keep],\n    )\n\n\ndef filter_data_by_scale(data, target_scale):\n    \"\"\"Filter pooled data to only include models of a single scale.\"\"\"\n    keep = np.array([m.get(\"scale\", \"\") == target_scale for m in data[\"models\"]])\n    if not keep.any():\n        return None\n    return {\n        \"models\": [m for m, k in zip(data[\"models\"], keep) if k],\n        \"dosages\": data[\"dosages\"][keep],\n        \"benchmarks\": {\n            bench: {\n                \"responses\": bd[\"responses\"][keep],\n                \"n_items\": bd[\"n_items\"],\n                \"valid_mask\": bd[\"valid_mask\"][keep],\n            }\n            for bench, bd in data[\"benchmarks\"].items()\n        },\n    }\n\n\ndef build_oracle_exposure(dosages, n_items):\n    \"\"\"Oracle exposure: dosage_fraction * uniform tau.\"\"\"\n    max_d = dosages.max() if dosages.max() > 0 else 1.0\n    fracs = dosages / max_d\n    return np.outer(fracs, np.ones(n_items))\n\n\ndef filter_items(responses, benchmark, exclude_set=None, min_variance=0.0):\n    \"\"\"Remove items by exclusion list and/or low cross-model variance.\n\n    Returns (filtered_responses, kept_indices, stats_dict).\n    \"\"\"\n    n_models, n_items = responses.shape\n    keep = np.ones(n_items, dtype=bool)\n\n    n_excluded_by_list = 0\n    if exclude_set:\n        for j in range(n_items):\n            if f\"{benchmark}_{j}\" in exclude_set:\n                keep[j] = False\n                n_excluded_by_list += 1\n\n    n_excluded_by_var = 0\n    if min_variance > 0:\n        item_var = np.var(responses, axis=0)\n        low_var = item_var < min_variance\n        low_var &= keep\n        n_excluded_by_var = int(low_var.sum())\n        keep[low_var] = False\n\n    kept_indices = np.where(keep)[0]\n    stats = {\n        \"original\": n_items,\n        \"excluded_by_list\": n_excluded_by_list,\n        \"excluded_by_variance\": n_excluded_by_var,\n        \"remaining\": int(keep.sum()),\n    }\n    return responses[:, keep], kept_indices, stats\n\n\ndef run_single_benchmark_fit(bench, data, args_dict, exclude_set=None, min_item_variance=0.0):\n    \"\"\"Run IRT fit for a single benchmark with exclusions.\"\"\"\n    if bench not in data[\"benchmarks\"]:\n        log.warning(\"Benchmark %s not in data, skipping\", bench)\n        return None\n\n    bd = data[\"benchmarks\"][bench]\n    models_filt, dosages_filt, responses_filt, valid_filt = apply_per_benchmark_exclusions(\n        data[\"models\"], data[\"dosages\"],\n        bd[\"responses\"], bd[\"valid_mask\"], bench\n    )\n\n    # Apply valid mask\n    if not valid_filt.all():\n        active = valid_filt.astype(bool)\n        models_filt = [m for m, v in zip(models_filt, active) if v]\n        dosages_filt = dosages_filt[active]\n        responses_filt = responses_filt[active]\n\n    n_models = len(models_filt)\n    n_items = bd[\"n_items\"]\n\n    if exclude_set or min_item_variance > 0:\n        responses_filt, kept_indices, fstats = filter_items(\n            responses_filt, bench, exclude_set, min_item_variance\n        )\n        n_items = fstats[\"remaining\"]\n        log.info(\"[%s] Item filter: %d -> %d (list=%d, variance=%d)\",\n                 bench, fstats[\"original\"], n_items,\n                 fstats[\"excluded_by_list\"], fstats[\"excluded_by_variance\"])\n\n    log.info(\"[%s] N_models=%d, N_items=%d\", bench, n_models, n_items)\n\n    if n_models < 3:\n        log.warning(\"[%s] Too few models (%d), skipping\", bench, n_models)\n        return None\n\n    exposure = build_oracle_exposure(dosages_filt, n_items)\n    stan_data = prepare_stan_data(responses_filt, exposure, MODEL_TYPE)\n\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, responses_filt)\n    results = extract_results(fit, responses_filt, MODEL_TYPE)\n\n    return {\n        \"benchmark\": bench,\n        \"n_models\": n_models,\n        \"n_items\": n_items,\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in models_filt],\n        \"dosages\": dosages_filt.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n    }\n\n\ndef run_joint_fit(data, benchmarks_to_include, args_dict, exclude_set=None, min_item_variance=0.0):\n    \"\"\"Concatenate benchmark items and fit shared-gamma model.\n\n    Uses intersection of valid models across all benchmarks (after exclusions).\n    \"\"\"\n    per_bench_filtered = {}\n    for bench in benchmarks_to_include:\n        if bench not in data[\"benchmarks\"]:\n            continue\n        bd = data[\"benchmarks\"][bench]\n        models_f, dosages_f, resp_f, valid_f = apply_per_benchmark_exclusions(\n            data[\"models\"], data[\"dosages\"],\n            bd[\"responses\"], bd[\"valid_mask\"], bench\n        )\n        if not valid_f.all():\n            active = valid_f.astype(bool)\n            models_f = [m for m, v in zip(models_f, active) if v]\n            dosages_f = dosages_f[active]\n            resp_f = resp_f[active]\n\n        per_bench_filtered[bench] = {\n            \"models\": models_f,\n            \"dosages\": dosages_f,\n            \"responses\": resp_f,\n            \"n_items\": bd[\"n_items\"],\n        }\n\n    # Find intersection of valid model dirnames across benchmarks\n    dirname_sets = [set(m[\"dirname\"] for m in bf[\"models\"])\n                    for bf in per_bench_filtered.values()]\n    common_dirnames = set.intersection(*dirname_sets) if dirname_sets else set()\n    log.info(\"Joint fit: %d common models across %d benchmarks\",\n             len(common_dirnames), len(per_bench_filtered))\n\n    if len(common_dirnames) < 3:\n        log.warning(\"Too few common models (%d) for joint fit\", len(common_dirnames))\n        return None\n\n    # Build concatenated matrices using common model order\n    ref_bench = list(per_bench_filtered.keys())[0]\n    ref_models = per_bench_filtered[ref_bench][\"models\"]\n    ordered_dirnames = [m[\"dirname\"] for m in ref_models if m[\"dirname\"] in common_dirnames]\n\n    all_y = []\n    all_exp = []\n    slices = {}\n    col_offset = 0\n    joint_models = None\n    joint_dosages = None\n\n    for bench, bf in per_bench_filtered.items():\n        dirname_to_idx = {m[\"dirname\"]: i for i, m in enumerate(bf[\"models\"])}\n        indices = [dirname_to_idx[d] for d in ordered_dirnames]\n\n        resp_ordered = bf[\"responses\"][indices]\n        dosages_ordered = bf[\"dosages\"][indices]\n        n_items = bf[\"n_items\"]\n\n        if exclude_set or min_item_variance > 0:\n            resp_ordered, kept_indices, fstats = filter_items(\n                resp_ordered, bench, exclude_set, min_item_variance\n            )\n            n_items = fstats[\"remaining\"]\n            log.info(\"[joint/%s] Item filter: %d -> %d (list=%d, variance=%d)\",\n                     bench, fstats[\"original\"], n_items,\n                     fstats[\"excluded_by_list\"], fstats[\"excluded_by_variance\"])\n\n        exposure = build_oracle_exposure(dosages_ordered, n_items)\n\n        all_y.append(resp_ordered)\n        all_exp.append(exposure)\n        slices[bench] = (col_offset, col_offset + n_items)\n        col_offset += n_items\n\n        if joint_models is None:\n            joint_models = [bf[\"models\"][i] for i in indices]\n            joint_dosages = dosages_ordered\n\n    y_concat = np.concatenate(all_y, axis=1)\n    exp_concat = np.concatenate(all_exp, axis=1)\n\n    n_models, n_total = y_concat.shape\n    log.info(\"Joint fit: %d models x %d total items\", n_models, n_total)\n    log.info(\"Joint fit slices: %s\", {b: f\"{s[0]}-{s[1]}\" for b, s in slices.items()})\n\n    stan_data = prepare_stan_data(y_concat, exp_concat, MODEL_TYPE)\n\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, y_concat)\n    results = extract_results(fit, y_concat, MODEL_TYPE)\n\n    # Per-benchmark calibrated scores from joint model\n    gamma_draws = fit.stan_variable(\"gamma\")\n    theta_draws = fit.stan_variable(\"theta\")\n    a_draws = fit.stan_variable(\"a\")\n    b_draws = fit.stan_variable(\"b\")\n\n    per_bench_cal = {}\n    for bench, (start, end) in slices.items():\n        n_bench_items = end - start\n        n_draws = gamma_draws.shape[0]\n        bench_cal = np.zeros((n_draws, n_models))\n        for draw in range(n_draws):\n            for i in range(n_models):\n                total = 0.0\n                for j in range(start, end):\n                    eta_clean = a_draws[draw, j] * (theta_draws[draw, i] - b_draws[draw, j])\n                    total += 1.0 / (1.0 + np.exp(-eta_clean))\n                bench_cal[draw, i] = total / n_bench_items\n        per_bench_cal[bench] = {\n            \"mean\": bench_cal.mean(axis=0).tolist(),\n            \"sd\": bench_cal.std(axis=0).tolist(),\n        }\n\n    return {\n        \"mode\": \"joint_fit_4bench\",\n        \"model_type\": MODEL_TYPE,\n        \"n_models\": n_models,\n        \"n_total_items\": n_total,\n        \"benchmark_slices\": {k: list(v) for k, v in slices.items()},\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in joint_models],\n        \"dosages\": joint_dosages.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"global_gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n        \"calibrated_scores_per_benchmark\": per_bench_cal,\n    }\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(\n        description=\"Pooled 4-benchmark IRT analysis (2PL+gamma)\"\n    )\n    parser.add_argument(\n        \"--exclude-items\", type=str, default=None,\n        help=\"JSON file with list of item_ids to exclude (e.g. [\\\"mmlu_42\\\", \\\"mmlu_103\\\"])\",\n    )\n    parser.add_argument(\n        \"--min-item-variance\", type=float, default=0.0,\n        help=\"Exclude items with cross-model variance below this threshold (default: 0, disabled)\",\n    )\n    parser.add_argument(\n        \"--stratify-by-scale\", action=\"store_true\",\n        help=\"Fit IRT independently per model scale (0.5B/1.5B/3B) instead of pooled\",\n    )\n    parser.add_argument(\"--chains\", type=int, default=4)\n    parser.add_argument(\"--warmup\", type=int, default=1000)\n    parser.add_argument(\"--samples\", type=int, default=1000)\n    parser.add_argument(\"--adapt-delta\", type=float, default=0.95)\n    parser.add_argument(\"--max-treedepth\", type=int, default=12)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--parallel-chains\", type=int, default=1)\n    return parser.parse_args()\n\n\ndef main():\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    args = parse_args()\n\n    exclude_set = None\n    if args.exclude_items:\n        with open(args.exclude_items) as f:\n            exclude_list = json.load(f)\n        exclude_set = set(exclude_list)\n        log.info(\"Loaded %d item_ids to exclude from %s\", len(exclude_set), args.exclude_items)\n\n    args_dict = {\n        \"chains\": 4,\n        \"warmup\": 1000,\n        \"samples\": 1000,\n        \"adapt_delta\": 0.95,\n        \"max_treedepth\": 12,\n        \"seed\": 42,\n        \"parallel_chains\": 1,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    log.info(\"Loading pooled eval results: scales=%s, benchmarks=%s\", SCALES, BENCHMARKS)\n    t0 = time.time()\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n    )\n    log.info(\"Loaded %d models in %.1fs\", len(data[\"models\"]), time.time() - t0)\n    log.info(\"Dosages: %s\", data[\"dosages\"].tolist())\n    log.info(\"Benchmarks: %s\", list(data[\"benchmarks\"].keys()))\n\n    all_results = {\n        \"config\": {\n            \"model_type\": MODEL_TYPE,\n            \"scales\": SCALES,\n            \"benchmarks\": BENCHMARKS,\n            \"exposure\": \"oracle_dosage\",\n            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",\n                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],\n            \"item_filter\": {\n                \"exclude_items_file\": args.exclude_items,\n                \"exclude_items_count\": len(exclude_set) if exclude_set else 0,\n                \"min_item_variance\": args.min_item_variance,\n            },\n            \"stan_config\": args_dict,\n        },\n        \"per_benchmark\": {},\n        \"joint_fit\": None,\n    }\n\n    # Phase 1: Per-benchmark IRT fits\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 1: Per-benchmark IRT fits\")\n    log.info(\"=\" * 60)\n\n    for bench in BENCHMARKS:\n        log.info(\"-\" * 40)\n        log.info(\"Fitting %s...\", bench)\n        result = run_single_benchmark_fit(\n            bench, data, args_dict, exclude_set, args.min_item_variance\n        )\n        if result:\n            all_results[\"per_benchmark\"][bench] = result\n            g = result[\"gamma\"]\n            d = result[\"diagnostics\"]\n            log.info(\"[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                     bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                     d.get(\"divergent_count\", 0))\n\n            bench_dir = OUTPUT_DIR / bench\n            bench_dir.mkdir(parents=True, exist_ok=True)\n            with open(bench_dir / \"irt_results.json\", \"w\") as f:\n                json.dump(result, f, indent=2)\n\n    # Phase 2: Joint fit (shared gamma)\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 2: Joint fit (shared gamma across benchmarks)\")\n    log.info(\"=\" * 60)\n\n    included_benchmarks = list(all_results[\"per_benchmark\"].keys())\n    joint_result = run_joint_fit(\n        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance\n    )\n    if joint_result:\n        all_results[\"joint_fit\"] = joint_result\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        log.info(\"JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                 g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                 d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                 d.get(\"divergent_count\", 0))\n\n        with open(OUTPUT_DIR / \"joint_fit_results.json\", \"w\") as f:\n            json.dump(joint_result, f, indent=2)\n\n    # Save full results\n    with open(OUTPUT_DIR / \"pooled_4bench_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Print summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)\")\n    print(\"=\" * 60)\n\n    if joint_result:\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        ppc = joint_result[\"posterior_predictive\"]\n\n        # Coverage from calibrated scores\n        cal = joint_result[\"calibrated_scores\"]\n        if \"ci95_lower\" in cal and \"ci95_upper\" in cal:\n            lowers = np.array(cal[\"ci95_lower\"])\n            uppers = np.array(cal[\"ci95_upper\"])\n            # Ground truth approximation: d0 models have raw accuracy as truth\n            dosages_arr = np.array(joint_result[\"dosages\"])\n            # For d0 models, calibrated score IS the ground truth\n            # For d>0 models, compare calibrated CI with d0 mean\n            # This is a simplified coverage check\n            n_total = len(dosages_arr)\n            in_ci = 0\n            for i in range(n_total):\n                # Coverage: does 95% CI contain a reasonable reference?\n                # For overall coverage, check if CI width > 0\n                if uppers[i] > lowers[i]:\n                    in_ci += 1\n            coverage = in_ci / n_total * 100 if n_total > 0 else 0\n            print(f\"COVERAGE: C95={coverage:.0f}% (all CIs valid)\")\n        else:\n            # Use mean/sd to compute coverage\n            means = np.array(cal.get(\"mean\", []))\n            sds = np.array(cal.get(\"sd\", []))\n            print(f\"COVERAGE: need ground truth reference for proper C95\")\n\n        print(f\"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, \"\n              f\"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]\")\n        print(f\"PPP: {ppc.get('overall_ppp', 'N/A')}\")\n        print(f\"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, \"\n              f\"ESS={d.get('min_ess', 'N/A')}, \"\n              f\"divergences={d.get('divergent_count', 'N/A')}\")\n        print(f\"N_MODELS: {joint_result['n_models']}, \"\n              f\"N_ITEMS: {joint_result['n_total_items']}\")\n\n    print(\"\\nPER_BENCHMARK_GAMMA:\")\n    for bench in BENCHMARKS:\n        if bench in all_results[\"per_benchmark\"]:\n            g = all_results[\"per_benchmark\"][bench][\"gamma\"]\n            n = all_results[\"per_benchmark\"][bench][\"n_models\"]\n            ni = all_results[\"per_benchmark\"][bench][\"n_items\"]\n            print(f\"  {bench}: gamma={g['mean']:.4f} \"\n                  f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                  f\"(N={n}, items={ni})\")\n        else:\n            print(f\"  {bench}: SKIPPED\")\n\n    print(f\"\\nResults saved to {OUTPUT_DIR}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 419,
        "oldLines": 13,
        "newStart": 419,
        "newLines": 13,
        "lines": [
          "         log.info(\"Loaded %d item_ids to exclude from %s\", len(exclude_set), args.exclude_items)",
          " ",
          "     args_dict = {",
          "-        \"chains\": 4,",
          "-        \"warmup\": 1000,",
          "-        \"samples\": 1000,",
          "-        \"adapt_delta\": 0.95,",
          "-        \"max_treedepth\": 12,",
          "-        \"seed\": 42,",
          "-        \"parallel_chains\": 1,",
          "+        \"chains\": args.chains,",
          "+        \"warmup\": args.warmup,",
          "+        \"samples\": args.samples,",
          "+        \"adapt_delta\": args.adapt_delta,",
          "+        \"max_treedepth\": args.max_treedepth,",
          "+        \"seed\": args.seed,",
          "+        \"parallel_chains\": args.parallel_chains,",
          "     }",
          " ",
          "     OUTPUT_DIR.mkdir(parents=True, exist_ok=True)"
        ]
      },
      {
        "oldStart": 439,
        "oldLines": 133,
        "newStart": 439,
        "newLines": 11,
        "lines": [
          "     log.info(\"Dosages: %s\", data[\"dosages\"].tolist())",
          "     log.info(\"Benchmarks: %s\", list(data[\"benchmarks\"].keys()))",
          " ",
          "-    all_results = {",
          "-        \"config\": {",
          "-            \"model_type\": MODEL_TYPE,",
          "-            \"scales\": SCALES,",
          "-            \"benchmarks\": BENCHMARKS,",
          "-            \"exposure\": \"oracle_dosage\",",
          "-            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",",
          "-                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],",
          "-            \"item_filter\": {",
          "-                \"exclude_items_file\": args.exclude_items,",
          "-                \"exclude_items_count\": len(exclude_set) if exclude_set else 0,",
          "-                \"min_item_variance\": args.min_item_variance,",
          "-            },",
          "-            \"stan_config\": args_dict,",
          "-        },",
          "-        \"per_benchmark\": {},",
          "-        \"joint_fit\": None,",
          "-    }",
          "+    if args.stratify_by_scale:",
          "+        run_scale_stratified(data, args_dict, exclude_set, args.min_item_variance)",
          "+    else:",
          "+        run_pooled(data, args_dict, exclude_set, args)",
          " ",
          "-    # Phase 1: Per-benchmark IRT fits",
          "-    log.info(\"=\" * 60)",
          "-    log.info(\"PHASE 1: Per-benchmark IRT fits\")",
          "-    log.info(\"=\" * 60)",
          " ",
          "-    for bench in BENCHMARKS:",
          "-        log.info(\"-\" * 40)",
          "-        log.info(\"Fitting %s...\", bench)",
          "-        result = run_single_benchmark_fit(",
          "-            bench, data, args_dict, exclude_set, args.min_item_variance",
          "-        )",
          "-        if result:",
          "-            all_results[\"per_benchmark\"][bench] = result",
          "-            g = result[\"gamma\"]",
          "-            d = result[\"diagnostics\"]",
          "-            log.info(\"[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",",
          "-                     bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],",
          "-                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),",
          "-                     d.get(\"divergent_count\", 0))",
          "-",
          "-            bench_dir = OUTPUT_DIR / bench",
          "-            bench_dir.mkdir(parents=True, exist_ok=True)",
          "-            with open(bench_dir / \"irt_results.json\", \"w\") as f:",
          "-                json.dump(result, f, indent=2)",
          "-",
          "-    # Phase 2: Joint fit (shared gamma)",
          "-    log.info(\"=\" * 60)",
          "-    log.info(\"PHASE 2: Joint fit (shared gamma across benchmarks)\")",
          "-    log.info(\"=\" * 60)",
          "-",
          "-    included_benchmarks = list(all_results[\"per_benchmark\"].keys())",
          "-    joint_result = run_joint_fit(",
          "-        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance",
          "-    )",
          "-    if joint_result:",
          "-        all_results[\"joint_fit\"] = joint_result",
          "-        g = joint_result[\"global_gamma\"]",
          "-        d = joint_result[\"diagnostics\"]",
          "-        log.info(\"JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",",
          "-                 g[\"mean\"], g[\"q025\"], g[\"q975\"],",
          "-                 d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),",
          "-                 d.get(\"divergent_count\", 0))",
          "-",
          "-        with open(OUTPUT_DIR / \"joint_fit_results.json\", \"w\") as f:",
          "-            json.dump(joint_result, f, indent=2)",
          "-",
          "-    # Save full results",
          "-    with open(OUTPUT_DIR / \"pooled_4bench_results.json\", \"w\") as f:",
          "-        json.dump(all_results, f, indent=2)",
          "-",
          "-    # Print summary",
          "-    print(\"\\n\" + \"=\" * 60)",
          "-    print(\"POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)\")",
          "-    print(\"=\" * 60)",
          "-",
          "-    if joint_result:",
          "-        g = joint_result[\"global_gamma\"]",
          "-        d = joint_result[\"diagnostics\"]",
          "-        ppc = joint_result[\"posterior_predictive\"]",
          "-",
          "-        # Coverage from calibrated scores",
          "-        cal = joint_result[\"calibrated_scores\"]",
          "-        if \"ci95_lower\" in cal and \"ci95_upper\" in cal:",
          "-            lowers = np.array(cal[\"ci95_lower\"])",
          "-            uppers = np.array(cal[\"ci95_upper\"])",
          "-            # Ground truth approximation: d0 models have raw accuracy as truth",
          "-            dosages_arr = np.array(joint_result[\"dosages\"])",
          "-            # For d0 models, calibrated score IS the ground truth",
          "-            # For d>0 models, compare calibrated CI with d0 mean",
          "-            # This is a simplified coverage check",
          "-            n_total = len(dosages_arr)",
          "-            in_ci = 0",
          "-            for i in range(n_total):",
          "-                # Coverage: does 95% CI contain a reasonable reference?",
          "-                # For overall coverage, check if CI width > 0",
          "-                if uppers[i] > lowers[i]:",
          "-                    in_ci += 1",
          "-            coverage = in_ci / n_total * 100 if n_total > 0 else 0",
          "-            print(f\"COVERAGE: C95={coverage:.0f}% (all CIs valid)\")",
          "-        else:",
          "-            # Use mean/sd to compute coverage",
          "-            means = np.array(cal.get(\"mean\", []))",
          "-            sds = np.array(cal.get(\"sd\", []))",
          "-            print(f\"COVERAGE: need ground truth reference for proper C95\")",
          "-",
          "-        print(f\"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, \"",
          "-              f\"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]\")",
          "-        print(f\"PPP: {ppc.get('overall_ppp', 'N/A')}\")",
          "-        print(f\"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, \"",
          "-              f\"ESS={d.get('min_ess', 'N/A')}, \"",
          "-              f\"divergences={d.get('divergent_count', 'N/A')}\")",
          "-        print(f\"N_MODELS: {joint_result['n_models']}, \"",
          "-              f\"N_ITEMS: {joint_result['n_total_items']}\")",
          "-",
          "-    print(\"\\nPER_BENCHMARK_GAMMA:\")",
          "-    for bench in BENCHMARKS:",
          "-        if bench in all_results[\"per_benchmark\"]:",
          "-            g = all_results[\"per_benchmark\"][bench][\"gamma\"]",
          "-            n = all_results[\"per_benchmark\"][bench][\"n_models\"]",
          "-            ni = all_results[\"per_benchmark\"][bench][\"n_items\"]",
          "-            print(f\"  {bench}: gamma={g['mean']:.4f} \"",
          "-                  f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"",
          "-                  f\"(N={n}, items={ni})\")",
          "-        else:",
          "-            print(f\"  {bench}: SKIPPED\")",
          "-",
          "-    print(f\"\\nResults saved to {OUTPUT_DIR}\")",
          "-",
          "-",
          " if __name__ == \"__main__\":",
          "     main()"
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

_source line 109_

Now I need to add the two new functions (`run_scale_stratified` and `run_pooled`) before `main()`. Let me add them right before `parse_args()`:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "97407e35-b7fe-4063-aa9e-53e3f0057bc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Nv5f3BexqoBz18zGGiKST",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2522,
      "cache_read_input_tokens": 76407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2522
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

_source line 110_

<details open><summary>🔧 Tool call — Edit · `toolu_01RLDEoQoVq3KTkjtDpd3ZyC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
  "old_string": "def parse_args():",
  "new_string": "def run_scale_stratified(data, args_dict, exclude_set, min_item_variance):\n    \"\"\"Per-scale per-benchmark IRT fits (D105).\"\"\"\n    output_dir = OUTPUT_DIR / \"scale_stratified\"\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    per_scale_results = {}\n    summary_rows = []\n\n    for scale in SCALES:\n        scale_data = filter_data_by_scale(data, scale)\n        if scale_data is None:\n            log.warning(\"No models for scale %s, skipping\", scale)\n            continue\n\n        n_total = len(scale_data[\"models\"])\n        unique_dosages = np.unique(scale_data[\"dosages\"]).tolist()\n        log.info(\"=\" * 60)\n        log.info(\"SCALE %s: %d models, dosages=%s\", scale, n_total, unique_dosages)\n        log.info(\"=\" * 60)\n\n        if len(unique_dosages) < 2:\n            log.warning(\"Scale %s has only 1 dosage level — gamma not identifiable \"\n                        \"(prior-dominated)\", scale)\n\n        per_scale_results[scale] = {}\n        scale_dir = output_dir / scale.replace(\".\", \"_\")\n        scale_dir.mkdir(parents=True, exist_ok=True)\n\n        for bench in BENCHMARKS:\n            log.info(\"--- %s / %s ---\", scale, bench)\n            result = run_single_benchmark_fit(\n                bench, scale_data, args_dict, exclude_set, min_item_variance\n            )\n            if result is None:\n                summary_rows.append({\n                    \"scale\": scale, \"benchmark\": bench,\n                    \"gamma_mean\": None, \"ci_low\": None, \"ci_high\": None,\n                    \"rhat\": None, \"ess\": None, \"n_models\": 0, \"n_items\": 0,\n                    \"skipped\": True,\n                })\n                continue\n\n            result[\"scale\"] = scale\n            per_scale_results[scale][bench] = result\n\n            g = result[\"gamma\"]\n            d = result[\"diagnostics\"]\n            row = {\n                \"scale\": scale,\n                \"benchmark\": bench,\n                \"gamma_mean\": g[\"mean\"],\n                \"ci_low\": g[\"q025\"],\n                \"ci_high\": g[\"q975\"],\n                \"rhat\": d.get(\"max_rhat\"),\n                \"ess\": d.get(\"min_ess\"),\n                \"n_models\": result[\"n_models\"],\n                \"n_items\": result[\"n_items\"],\n                \"skipped\": False,\n            }\n            summary_rows.append(row)\n\n            log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, N=%d\",\n                     scale, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0), result[\"n_models\"])\n\n            with open(scale_dir / f\"{bench}_results.json\", \"w\") as f:\n                json.dump(result, f, indent=2)\n\n    # Save combined results\n    output = {\n        \"config\": {\n            \"mode\": \"scale_stratified\",\n            \"model_type\": MODEL_TYPE,\n            \"scales\": SCALES,\n            \"benchmarks\": BENCHMARKS,\n            \"exposure\": \"oracle_dosage\",\n            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",\n                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],\n            \"stan_config\": args_dict,\n        },\n        \"per_scale\": per_scale_results,\n        \"summary\": summary_rows,\n    }\n    with open(output_dir / \"scale_stratified_results.json\", \"w\") as f:\n        json.dump(output, f, indent=2)\n\n    # Print summary table\n    print(\"\\n\" + \"=\" * 100)\n    print(\"SCALE-STRATIFIED IRT RESULTS (D105)\")\n    print(\"=\" * 100)\n    hdr = f\"{'Scale':<8} {'Benchmark':<16} {'γ̂':>8} {'CI_low':>8} {'CI_high':>8} {'R̂':>8} {'ESS':>8} {'N_models':>10} {'N_items':>8}\"\n    print(hdr)\n    print(\"-\" * len(hdr))\n    for row in summary_rows:\n        if row.get(\"skipped\"):\n            print(f\"{row['scale']:<8} {row['benchmark']:<16} {'SKIPPED':>8} \"\n                  f\"{'':>8} {'':>8} {'':>8} {'':>8} {row['n_models']:>10} {'':>8}\")\n        else:\n            rhat_str = f\"{row['rhat']:.4f}\" if row['rhat'] is not None else \"N/A\"\n            ess_str = f\"{row['ess']:.0f}\" if row['ess'] is not None else \"N/A\"\n            print(f\"{row['scale']:<8} {row['benchmark']:<16} \"\n                  f\"{row['gamma_mean']:>8.4f} {row['ci_low']:>8.4f} {row['ci_high']:>8.4f} \"\n                  f\"{rhat_str:>8} {ess_str:>8} {row['n_models']:>10} {row['n_items']:>8}\")\n    print(\"-\" * len(hdr))\n\n    # Flag convergence issues\n    for row in summary_rows:\n        if row.get(\"skipped\"):\n            continue\n        warnings = []\n        if row[\"rhat\"] is not None and row[\"rhat\"] > 1.01:\n            warnings.append(f\"R̂={row['rhat']:.4f} > 1.01\")\n        if row[\"ess\"] is not None and row[\"ess\"] < 400:\n            warnings.append(f\"ESS={row['ess']:.0f} < 400\")\n        if row[\"n_models\"] < 5:\n            warnings.append(f\"N_models={row['n_models']} (small sample)\")\n        if warnings:\n            print(f\"  WARNING [{row['scale']}/{row['benchmark']}]: {', '.join(warnings)}\")\n\n    print(f\"\\nResults saved to {output_dir}\")\n\n\ndef run_pooled(data, args_dict, exclude_set, args):\n    \"\"\"Original pooled analysis (backward-compatible).\"\"\"\n    all_results = {\n        \"config\": {\n            \"model_type\": MODEL_TYPE,\n            \"scales\": SCALES,\n            \"benchmarks\": BENCHMARKS,\n            \"exposure\": \"oracle_dosage\",\n            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",\n                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],\n            \"item_filter\": {\n                \"exclude_items_file\": args.exclude_items,\n                \"exclude_items_count\": len(exclude_set) if exclude_set else 0,\n                \"min_item_variance\": args.min_item_variance,\n            },\n            \"stan_config\": args_dict,\n        },\n        \"per_benchmark\": {},\n        \"joint_fit\": None,\n    }\n\n    # Phase 1: Per-benchmark IRT fits\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 1: Per-benchmark IRT fits\")\n    log.info(\"=\" * 60)\n\n    for bench in BENCHMARKS:\n        log.info(\"-\" * 40)\n        log.info(\"Fitting %s...\", bench)\n        result = run_single_benchmark_fit(\n            bench, data, args_dict, exclude_set, args.min_item_variance\n        )\n        if result:\n            all_results[\"per_benchmark\"][bench] = result\n            g = result[\"gamma\"]\n            d = result[\"diagnostics\"]\n            log.info(\"[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                     bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                     d.get(\"divergent_count\", 0))\n\n            bench_dir = OUTPUT_DIR / bench\n            bench_dir.mkdir(parents=True, exist_ok=True)\n            with open(bench_dir / \"irt_results.json\", \"w\") as f:\n                json.dump(result, f, indent=2)\n\n    # Phase 2: Joint fit (shared gamma)\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 2: Joint fit (shared gamma across benchmarks)\")\n    log.info(\"=\" * 60)\n\n    included_benchmarks = list(all_results[\"per_benchmark\"].keys())\n    joint_result = run_joint_fit(\n        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance\n    )\n    if joint_result:\n        all_results[\"joint_fit\"] = joint_result\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        log.info(\"JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                 g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                 d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                 d.get(\"divergent_count\", 0))\n\n        with open(OUTPUT_DIR / \"joint_fit_results.json\", \"w\") as f:\n            json.dump(joint_result, f, indent=2)\n\n    # Save full results\n    with open(OUTPUT_DIR / \"pooled_4bench_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Print summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)\")\n    print(\"=\" * 60)\n\n    if joint_result:\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        ppc = joint_result[\"posterior_predictive\"]\n\n        cal = joint_result[\"calibrated_scores\"]\n        if \"ci95_lower\" in cal and \"ci95_upper\" in cal:\n            lowers = np.array(cal[\"ci95_lower\"])\n            uppers = np.array(cal[\"ci95_upper\"])\n            dosages_arr = np.array(joint_result[\"dosages\"])\n            n_total = len(dosages_arr)\n            in_ci = sum(1 for i in range(n_total) if uppers[i] > lowers[i])\n            coverage = in_ci / n_total * 100 if n_total > 0 else 0\n            print(f\"COVERAGE: C95={coverage:.0f}% (all CIs valid)\")\n        else:\n            print(\"COVERAGE: need ground truth reference for proper C95\")\n\n        print(f\"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, \"\n              f\"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]\")\n        print(f\"PPP: {ppc.get('overall_ppp', 'N/A')}\")\n        print(f\"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, \"\n              f\"ESS={d.get('min_ess', 'N/A')}, \"\n              f\"divergences={d.get('divergent_count', 'N/A')}\")\n        print(f\"N_MODELS: {joint_result['n_models']}, \"\n              f\"N_ITEMS: {joint_result['n_total_items']}\")\n\n    print(\"\\nPER_BENCHMARK_GAMMA:\")\n    for bench in BENCHMARKS:\n        if bench in all_results[\"per_benchmark\"]:\n            g = all_results[\"per_benchmark\"][bench][\"gamma\"]\n            n = all_results[\"per_benchmark\"][bench][\"n_models\"]\n            ni = all_results[\"per_benchmark\"][bench][\"n_items\"]\n            print(f\"  {bench}: gamma={g['mean']:.4f} \"\n                  f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                  f\"(N={n}, items={ni})\")\n        else:\n            print(f\"  {bench}: SKIPPED\")\n\n    print(f\"\\nResults saved to {OUTPUT_DIR}\")\n\n\ndef parse_args():"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "c189a080-410a-4c6b-b1d5-ab0e9ede78c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Nv5f3BexqoBz18zGGiKST",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2522,
      "cache_read_input_tokens": 76407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2522
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

_source line 111 · 2026-05-16T05:33:45.061Z_

<details><summary>↩ Tool result · `toolu_01RLDEoQoVq3KTkjtDpd3ZyC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "70f9f2dc-2a60-497d-b8fe-6560907c0bef",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
    "oldString": "def parse_args():",
    "newString": "def run_scale_stratified(data, args_dict, exclude_set, min_item_variance):\n    \"\"\"Per-scale per-benchmark IRT fits (D105).\"\"\"\n    output_dir = OUTPUT_DIR / \"scale_stratified\"\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    per_scale_results = {}\n    summary_rows = []\n\n    for scale in SCALES:\n        scale_data = filter_data_by_scale(data, scale)\n        if scale_data is None:\n            log.warning(\"No models for scale %s, skipping\", scale)\n            continue\n\n        n_total = len(scale_data[\"models\"])\n        unique_dosages = np.unique(scale_data[\"dosages\"]).tolist()\n        log.info(\"=\" * 60)\n        log.info(\"SCALE %s: %d models, dosages=%s\", scale, n_total, unique_dosages)\n        log.info(\"=\" * 60)\n\n        if len(unique_dosages) < 2:\n            log.warning(\"Scale %s has only 1 dosage level — gamma not identifiable \"\n                        \"(prior-dominated)\", scale)\n\n        per_scale_results[scale] = {}\n        scale_dir = output_dir / scale.replace(\".\", \"_\")\n        scale_dir.mkdir(parents=True, exist_ok=True)\n\n        for bench in BENCHMARKS:\n            log.info(\"--- %s / %s ---\", scale, bench)\n            result = run_single_benchmark_fit(\n                bench, scale_data, args_dict, exclude_set, min_item_variance\n            )\n            if result is None:\n                summary_rows.append({\n                    \"scale\": scale, \"benchmark\": bench,\n                    \"gamma_mean\": None, \"ci_low\": None, \"ci_high\": None,\n                    \"rhat\": None, \"ess\": None, \"n_models\": 0, \"n_items\": 0,\n                    \"skipped\": True,\n                })\n                continue\n\n            result[\"scale\"] = scale\n            per_scale_results[scale][bench] = result\n\n            g = result[\"gamma\"]\n            d = result[\"diagnostics\"]\n            row = {\n                \"scale\": scale,\n                \"benchmark\": bench,\n                \"gamma_mean\": g[\"mean\"],\n                \"ci_low\": g[\"q025\"],\n                \"ci_high\": g[\"q975\"],\n                \"rhat\": d.get(\"max_rhat\"),\n                \"ess\": d.get(\"min_ess\"),\n                \"n_models\": result[\"n_models\"],\n                \"n_items\": result[\"n_items\"],\n                \"skipped\": False,\n            }\n            summary_rows.append(row)\n\n            log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, N=%d\",\n                     scale, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0), result[\"n_models\"])\n\n            with open(scale_dir / f\"{bench}_results.json\", \"w\") as f:\n                json.dump(result, f, indent=2)\n\n    # Save combined results\n    output = {\n        \"config\": {\n            \"mode\": \"scale_stratified\",\n            \"model_type\": MODEL_TYPE,\n            \"scales\": SCALES,\n            \"benchmarks\": BENCHMARKS,\n            \"exposure\": \"oracle_dosage\",\n            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",\n                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],\n            \"stan_config\": args_dict,\n        },\n        \"per_scale\": per_scale_results,\n        \"summary\": summary_rows,\n    }\n    with open(output_dir / \"scale_stratified_results.json\", \"w\") as f:\n        json.dump(output, f, indent=2)\n\n    # Print summary table\n    print(\"\\n\" + \"=\" * 100)\n    print(\"SCALE-STRATIFIED IRT RESULTS (D105)\")\n    print(\"=\" * 100)\n    hdr = f\"{'Scale':<8} {'Benchmark':<16} {'γ̂':>8} {'CI_low':>8} {'CI_high':>8} {'R̂':>8} {'ESS':>8} {'N_models':>10} {'N_items':>8}\"\n    print(hdr)\n    print(\"-\" * len(hdr))\n    for row in summary_rows:\n        if row.get(\"skipped\"):\n            print(f\"{row['scale']:<8} {row['benchmark']:<16} {'SKIPPED':>8} \"\n                  f\"{'':>8} {'':>8} {'':>8} {'':>8} {row['n_models']:>10} {'':>8}\")\n        else:\n            rhat_str = f\"{row['rhat']:.4f}\" if row['rhat'] is not None else \"N/A\"\n            ess_str = f\"{row['ess']:.0f}\" if row['ess'] is not None else \"N/A\"\n            print(f\"{row['scale']:<8} {row['benchmark']:<16} \"\n                  f\"{row['gamma_mean']:>8.4f} {row['ci_low']:>8.4f} {row['ci_high']:>8.4f} \"\n                  f\"{rhat_str:>8} {ess_str:>8} {row['n_models']:>10} {row['n_items']:>8}\")\n    print(\"-\" * len(hdr))\n\n    # Flag convergence issues\n    for row in summary_rows:\n        if row.get(\"skipped\"):\n            continue\n        warnings = []\n        if row[\"rhat\"] is not None and row[\"rhat\"] > 1.01:\n            warnings.append(f\"R̂={row['rhat']:.4f} > 1.01\")\n        if row[\"ess\"] is not None and row[\"ess\"] < 400:\n            warnings.append(f\"ESS={row['ess']:.0f} < 400\")\n        if row[\"n_models\"] < 5:\n            warnings.append(f\"N_models={row['n_models']} (small sample)\")\n        if warnings:\n            print(f\"  WARNING [{row['scale']}/{row['benchmark']}]: {', '.join(warnings)}\")\n\n    print(f\"\\nResults saved to {output_dir}\")\n\n\ndef run_pooled(data, args_dict, exclude_set, args):\n    \"\"\"Original pooled analysis (backward-compatible).\"\"\"\n    all_results = {\n        \"config\": {\n            \"model_type\": MODEL_TYPE,\n            \"scales\": SCALES,\n            \"benchmarks\": BENCHMARKS,\n            \"exposure\": \"oracle_dosage\",\n            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",\n                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],\n            \"item_filter\": {\n                \"exclude_items_file\": args.exclude_items,\n                \"exclude_items_count\": len(exclude_set) if exclude_set else 0,\n                \"min_item_variance\": args.min_item_variance,\n            },\n            \"stan_config\": args_dict,\n        },\n        \"per_benchmark\": {},\n        \"joint_fit\": None,\n    }\n\n    # Phase 1: Per-benchmark IRT fits\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 1: Per-benchmark IRT fits\")\n    log.info(\"=\" * 60)\n\n    for bench in BENCHMARKS:\n        log.info(\"-\" * 40)\n        log.info(\"Fitting %s...\", bench)\n        result = run_single_benchmark_fit(\n            bench, data, args_dict, exclude_set, args.min_item_variance\n        )\n        if result:\n            all_results[\"per_benchmark\"][bench] = result\n            g = result[\"gamma\"]\n            d = result[\"diagnostics\"]\n            log.info(\"[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                     bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                     d.get(\"divergent_count\", 0))\n\n            bench_dir = OUTPUT_DIR / bench\n            bench_dir.mkdir(parents=True, exist_ok=True)\n            with open(bench_dir / \"irt_results.json\", \"w\") as f:\n                json.dump(result, f, indent=2)\n\n    # Phase 2: Joint fit (shared gamma)\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 2: Joint fit (shared gamma across benchmarks)\")\n    log.info(\"=\" * 60)\n\n    included_benchmarks = list(all_results[\"per_benchmark\"].keys())\n    joint_result = run_joint_fit(\n        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance\n    )\n    if joint_result:\n        all_results[\"joint_fit\"] = joint_result\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        log.info(\"JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                 g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                 d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                 d.get(\"divergent_count\", 0))\n\n        with open(OUTPUT_DIR / \"joint_fit_results.json\", \"w\") as f:\n            json.dump(joint_result, f, indent=2)\n\n    # Save full results\n    with open(OUTPUT_DIR / \"pooled_4bench_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Print summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)\")\n    print(\"=\" * 60)\n\n    if joint_result:\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        ppc = joint_result[\"posterior_predictive\"]\n\n        cal = joint_result[\"calibrated_scores\"]\n        if \"ci95_lower\" in cal and \"ci95_upper\" in cal:\n            lowers = np.array(cal[\"ci95_lower\"])\n            uppers = np.array(cal[\"ci95_upper\"])\n            dosages_arr = np.array(joint_result[\"dosages\"])\n            n_total = len(dosages_arr)\n            in_ci = sum(1 for i in range(n_total) if uppers[i] > lowers[i])\n            coverage = in_ci / n_total * 100 if n_total > 0 else 0\n            print(f\"COVERAGE: C95={coverage:.0f}% (all CIs valid)\")\n        else:\n            print(\"COVERAGE: need ground truth reference for proper C95\")\n\n        print(f\"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, \"\n              f\"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]\")\n        print(f\"PPP: {ppc.get('overall_ppp', 'N/A')}\")\n        print(f\"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, \"\n              f\"ESS={d.get('min_ess', 'N/A')}, \"\n              f\"divergences={d.get('divergent_count', 'N/A')}\")\n        print(f\"N_MODELS: {joint_result['n_models']}, \"\n              f\"N_ITEMS: {joint_result['n_total_items']}\")\n\n    print(\"\\nPER_BENCHMARK_GAMMA:\")\n    for bench in BENCHMARKS:\n        if bench in all_results[\"per_benchmark\"]:\n            g = all_results[\"per_benchmark\"][bench][\"gamma\"]\n            n = all_results[\"per_benchmark\"][bench][\"n_models\"]\n            ni = all_results[\"per_benchmark\"][bench][\"n_items\"]\n            print(f\"  {bench}: gamma={g['mean']:.4f} \"\n                  f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                  f\"(N={n}, items={ni})\")\n        else:\n            print(f\"  {bench}: SKIPPED\")\n\n    print(f\"\\nResults saved to {OUTPUT_DIR}\")\n\n\ndef parse_args():",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nPooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.\n\nRuns:\n  1. Per-benchmark IRT fits (with per-benchmark model exclusions)\n  2. Joint fit (shared gamma) across benchmarks using intersection models\n\nExclusion rules:\n  D044: GSM8K exclude d000 configs (format confound)\n  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept\n  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)\n  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)\n\nExposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\n\nsys.path.insert(0, \"/root/contamcal-irt-calibration/exp006\")\nfrom run_irt_calibration import (\n    load_pooled_eval_results,\n    prepare_stan_data,\n    fit_stan_model,\n    check_convergence,\n    posterior_predictive_check,\n    extract_results,\n    _summarize_vector,\n    STAN_MODELS,\n)\n\nlog = logging.getLogger(__name__)\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\", \"humaneval\"]\nSCALES = [\"0.5B\", \"1.5B\", \"3B\"]\nMODEL_TYPE = \"2pl_gamma\"\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\n\nOUTPUT_DIR = Path(\"/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl\")\nEVAL_DIR = \"/root/autodl-tmp/exp001/eval_results\"\n\n\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\n    \"\"\"Apply D044/D045/D046/D047/D018 per-benchmark exclusions.\"\"\"\n    keep = np.ones(len(models), dtype=bool)\n    reasons = []\n\n    for i, m in enumerate(models):\n        dirname = m.get(\"dirname\", \"\")\n        scale = m.get(\"scale\", \"\")\n        dosage = m.get(\"dosage\", 0)\n\n        # D046/D047: base pretrained\n        if \"base_pretrained\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D046/D047: {dirname} (base pretrained)\")\n            continue\n\n        # D018: deprecated check (dirname contains DEPRECATED)\n        if \"DEPRECATED\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D018: {dirname} (deprecated)\")\n            continue\n\n        # D045: 0.5B MMLU/ARC excluded (position bias)\n        if \"0.5B\" in scale and benchmark in (\"mmlu\", \"arc_challenge\"):\n            keep[i] = False\n            reasons.append(f\"  D045: {dirname} (0.5B on {benchmark})\")\n            continue\n\n        # D044: GSM8K exclude d000 (format confound)\n        if benchmark == \"gsm8k\" and dosage == 0:\n            keep[i] = False\n            reasons.append(f\"  D044: {dirname} (d000 on gsm8k)\")\n            continue\n\n        # Instruct model (no dosage pattern) - keep if aligned\n        # but skip if not part of dose-response (dosage not parseable)\n        # Actually Instruct models have dosage=base, which won't parse\n        # as dosage int. They'll appear with dosage=0 from the loader\n        # if dirname ends with _aligned without _dXXX pattern.\n        # The loader sets dosage from parsing, so Instruct models\n        # are already excluded by parse_model_dir_name returning None.\n\n    if reasons:\n        log.info(\"Excluded from %s (%d models):\", benchmark, len(reasons))\n        for r in reasons[:10]:\n            log.info(r)\n        if len(reasons) > 10:\n            log.info(\"  ... and %d more\", len(reasons) - 10)\n\n    return (\n        [m for m, k in zip(models, keep) if k],\n        dosages[keep],\n        responses[keep],\n        valid_mask[keep],\n    )\n\n\ndef filter_data_by_scale(data, target_scale):\n    \"\"\"Filter pooled data to only include models of a single scale.\"\"\"\n    keep = np.array([m.get(\"scale\", \"\") == target_scale for m in data[\"models\"]])\n    if not keep.any():\n        return None\n    return {\n        \"models\": [m for m, k in zip(data[\"models\"], keep) if k],\n        \"dosages\": data[\"dosages\"][keep],\n        \"benchmarks\": {\n            bench: {\n                \"responses\": bd[\"responses\"][keep],\n                \"n_items\": bd[\"n_items\"],\n                \"valid_mask\": bd[\"valid_mask\"][keep],\n            }\n            for bench, bd in data[\"benchmarks\"].items()\n        },\n    }\n\n\ndef build_oracle_exposure(dosages, n_items):\n    \"\"\"Oracle exposure: dosage_fraction * uniform tau.\"\"\"\n    max_d = dosages.max() if dosages.max() > 0 else 1.0\n    fracs = dosages / max_d\n    return np.outer(fracs, np.ones(n_items))\n\n\ndef filter_items(responses, benchmark, exclude_set=None, min_variance=0.0):\n    \"\"\"Remove items by exclusion list and/or low cross-model variance.\n\n    Returns (filtered_responses, kept_indices, stats_dict).\n    \"\"\"\n    n_models, n_items = responses.shape\n    keep = np.ones(n_items, dtype=bool)\n\n    n_excluded_by_list = 0\n    if exclude_set:\n        for j in range(n_items):\n            if f\"{benchmark}_{j}\" in exclude_set:\n                keep[j] = False\n                n_excluded_by_list += 1\n\n    n_excluded_by_var = 0\n    if min_variance > 0:\n        item_var = np.var(responses, axis=0)\n        low_var = item_var < min_variance\n        low_var &= keep\n        n_excluded_by_var = int(low_var.sum())\n        keep[low_var] = False\n\n    kept_indices = np.where(keep)[0]\n    stats = {\n        \"original\": n_items,\n        \"excluded_by_list\": n_excluded_by_list,\n        \"excluded_by_variance\": n_excluded_by_var,\n        \"remaining\": int(keep.sum()),\n    }\n    return responses[:, keep], kept_indices, stats\n\n\ndef run_single_benchmark_fit(bench, data, args_dict, exclude_set=None, min_item_variance=0.0):\n    \"\"\"Run IRT fit for a single benchmark with exclusions.\"\"\"\n    if bench not in data[\"benchmarks\"]:\n        log.warning(\"Benchmark %s not in data, skipping\", bench)\n        return None\n\n    bd = data[\"benchmarks\"][bench]\n    models_filt, dosages_filt, responses_filt, valid_filt = apply_per_benchmark_exclusions(\n        data[\"models\"], data[\"dosages\"],\n        bd[\"responses\"], bd[\"valid_mask\"], bench\n    )\n\n    # Apply valid mask\n    if not valid_filt.all():\n        active = valid_filt.astype(bool)\n        models_filt = [m for m, v in zip(models_filt, active) if v]\n        dosages_filt = dosages_filt[active]\n        responses_filt = responses_filt[active]\n\n    n_models = len(models_filt)\n    n_items = bd[\"n_items\"]\n\n    if exclude_set or min_item_variance > 0:\n        responses_filt, kept_indices, fstats = filter_items(\n            responses_filt, bench, exclude_set, min_item_variance\n        )\n        n_items = fstats[\"remaining\"]\n        log.info(\"[%s] Item filter: %d -> %d (list=%d, variance=%d)\",\n                 bench, fstats[\"original\"], n_items,\n                 fstats[\"excluded_by_list\"], fstats[\"excluded_by_variance\"])\n\n    log.info(\"[%s] N_models=%d, N_items=%d\", bench, n_models, n_items)\n\n    if n_models < 3:\n        log.warning(\"[%s] Too few models (%d), skipping\", bench, n_models)\n        return None\n\n    exposure = build_oracle_exposure(dosages_filt, n_items)\n    stan_data = prepare_stan_data(responses_filt, exposure, MODEL_TYPE)\n\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, responses_filt)\n    results = extract_results(fit, responses_filt, MODEL_TYPE)\n\n    return {\n        \"benchmark\": bench,\n        \"n_models\": n_models,\n        \"n_items\": n_items,\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in models_filt],\n        \"dosages\": dosages_filt.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n    }\n\n\ndef run_joint_fit(data, benchmarks_to_include, args_dict, exclude_set=None, min_item_variance=0.0):\n    \"\"\"Concatenate benchmark items and fit shared-gamma model.\n\n    Uses intersection of valid models across all benchmarks (after exclusions).\n    \"\"\"\n    per_bench_filtered = {}\n    for bench in benchmarks_to_include:\n        if bench not in data[\"benchmarks\"]:\n            continue\n        bd = data[\"benchmarks\"][bench]\n        models_f, dosages_f, resp_f, valid_f = apply_per_benchmark_exclusions(\n            data[\"models\"], data[\"dosages\"],\n            bd[\"responses\"], bd[\"valid_mask\"], bench\n        )\n        if not valid_f.all():\n            active = valid_f.astype(bool)\n            models_f = [m for m, v in zip(models_f, active) if v]\n            dosages_f = dosages_f[active]\n            resp_f = resp_f[active]\n\n        per_bench_filtered[bench] = {\n            \"models\": models_f,\n            \"dosages\": dosages_f,\n            \"responses\": resp_f,\n            \"n_items\": bd[\"n_items\"],\n        }\n\n    # Find intersection of valid model dirnames across benchmarks\n    dirname_sets = [set(m[\"dirname\"] for m in bf[\"models\"])\n                    for bf in per_bench_filtered.values()]\n    common_dirnames = set.intersection(*dirname_sets) if dirname_sets else set()\n    log.info(\"Joint fit: %d common models across %d benchmarks\",\n             len(common_dirnames), len(per_bench_filtered))\n\n    if len(common_dirnames) < 3:\n        log.warning(\"Too few common models (%d) for joint fit\", len(common_dirnames))\n        return None\n\n    # Build concatenated matrices using common model order\n    ref_bench = list(per_bench_filtered.keys())[0]\n    ref_models = per_bench_filtered[ref_bench][\"models\"]\n    ordered_dirnames = [m[\"dirname\"] for m in ref_models if m[\"dirname\"] in common_dirnames]\n\n    all_y = []\n    all_exp = []\n    slices = {}\n    col_offset = 0\n    joint_models = None\n    joint_dosages = None\n\n    for bench, bf in per_bench_filtered.items():\n        dirname_to_idx = {m[\"dirname\"]: i for i, m in enumerate(bf[\"models\"])}\n        indices = [dirname_to_idx[d] for d in ordered_dirnames]\n\n        resp_ordered = bf[\"responses\"][indices]\n        dosages_ordered = bf[\"dosages\"][indices]\n        n_items = bf[\"n_items\"]\n\n        if exclude_set or min_item_variance > 0:\n            resp_ordered, kept_indices, fstats = filter_items(\n                resp_ordered, bench, exclude_set, min_item_variance\n            )\n            n_items = fstats[\"remaining\"]\n            log.info(\"[joint/%s] Item filter: %d -> %d (list=%d, variance=%d)\",\n                     bench, fstats[\"original\"], n_items,\n                     fstats[\"excluded_by_list\"], fstats[\"excluded_by_variance\"])\n\n        exposure = build_oracle_exposure(dosages_ordered, n_items)\n\n        all_y.append(resp_ordered)\n        all_exp.append(exposure)\n        slices[bench] = (col_offset, col_offset + n_items)\n        col_offset += n_items\n\n        if joint_models is None:\n            joint_models = [bf[\"models\"][i] for i in indices]\n            joint_dosages = dosages_ordered\n\n    y_concat = np.concatenate(all_y, axis=1)\n    exp_concat = np.concatenate(all_exp, axis=1)\n\n    n_models, n_total = y_concat.shape\n    log.info(\"Joint fit: %d models x %d total items\", n_models, n_total)\n    log.info(\"Joint fit slices: %s\", {b: f\"{s[0]}-{s[1]}\" for b, s in slices.items()})\n\n    stan_data = prepare_stan_data(y_concat, exp_concat, MODEL_TYPE)\n\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, y_concat)\n    results = extract_results(fit, y_concat, MODEL_TYPE)\n\n    # Per-benchmark calibrated scores from joint model\n    gamma_draws = fit.stan_variable(\"gamma\")\n    theta_draws = fit.stan_variable(\"theta\")\n    a_draws = fit.stan_variable(\"a\")\n    b_draws = fit.stan_variable(\"b\")\n\n    per_bench_cal = {}\n    for bench, (start, end) in slices.items():\n        n_bench_items = end - start\n        n_draws = gamma_draws.shape[0]\n        bench_cal = np.zeros((n_draws, n_models))\n        for draw in range(n_draws):\n            for i in range(n_models):\n                total = 0.0\n                for j in range(start, end):\n                    eta_clean = a_draws[draw, j] * (theta_draws[draw, i] - b_draws[draw, j])\n                    total += 1.0 / (1.0 + np.exp(-eta_clean))\n                bench_cal[draw, i] = total / n_bench_items\n        per_bench_cal[bench] = {\n            \"mean\": bench_cal.mean(axis=0).tolist(),\n            \"sd\": bench_cal.std(axis=0).tolist(),\n        }\n\n    return {\n        \"mode\": \"joint_fit_4bench\",\n        \"model_type\": MODEL_TYPE,\n        \"n_models\": n_models,\n        \"n_total_items\": n_total,\n        \"benchmark_slices\": {k: list(v) for k, v in slices.items()},\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in joint_models],\n        \"dosages\": joint_dosages.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"global_gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n        \"calibrated_scores_per_benchmark\": per_bench_cal,\n    }\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(\n        description=\"Pooled 4-benchmark IRT analysis (2PL+gamma)\"\n    )\n    parser.add_argument(\n        \"--exclude-items\", type=str, default=None,\n        help=\"JSON file with list of item_ids to exclude (e.g. [\\\"mmlu_42\\\", \\\"mmlu_103\\\"])\",\n    )\n    parser.add_argument(\n        \"--min-item-variance\", type=float, default=0.0,\n        help=\"Exclude items with cross-model variance below this threshold (default: 0, disabled)\",\n    )\n    parser.add_argument(\n        \"--stratify-by-scale\", action=\"store_true\",\n        help=\"Fit IRT independently per model scale (0.5B/1.5B/3B) instead of pooled\",\n    )\n    parser.add_argument(\"--chains\", type=int, default=4)\n    parser.add_argument(\"--warmup\", type=int, default=1000)\n    parser.add_argument(\"--samples\", type=int, default=1000)\n    parser.add_argument(\"--adapt-delta\", type=float, default=0.95)\n    parser.add_argument(\"--max-treedepth\", type=int, default=12)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--parallel-chains\", type=int, default=1)\n    return parser.parse_args()\n\n\ndef main():\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    args = parse_args()\n\n    exclude_set = None\n    if args.exclude_items:\n        with open(args.exclude_items) as f:\n            exclude_list = json.load(f)\n        exclude_set = set(exclude_list)\n        log.info(\"Loaded %d item_ids to exclude from %s\", len(exclude_set), args.exclude_items)\n\n    args_dict = {\n        \"chains\": args.chains,\n        \"warmup\": args.warmup,\n        \"samples\": args.samples,\n        \"adapt_delta\": args.adapt_delta,\n        \"max_treedepth\": args.max_treedepth,\n        \"seed\": args.seed,\n        \"parallel_chains\": args.parallel_chains,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    log.info(\"Loading pooled eval results: scales=%s, benchmarks=%s\", SCALES, BENCHMARKS)\n    t0 = time.time()\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n    )\n    log.info(\"Loaded %d models in %.1fs\", len(data[\"models\"]), time.time() - t0)\n    log.info(\"Dosages: %s\", data[\"dosages\"].tolist())\n    log.info(\"Benchmarks: %s\", list(data[\"benchmarks\"].keys()))\n\n    if args.stratify_by_scale:\n        run_scale_stratified(data, args_dict, exclude_set, args.min_item_variance)\n    else:\n        run_pooled(data, args_dict, exclude_set, args)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 377,
        "oldLines": 6,
        "newStart": 377,
        "newLines": 245,
        "lines": [
          "     }",
          " ",
          " ",
          "+def run_scale_stratified(data, args_dict, exclude_set, min_item_variance):",
          "+    \"\"\"Per-scale per-benchmark IRT fits (D105).\"\"\"",
          "+    output_dir = OUTPUT_DIR / \"scale_stratified\"",
          "+    output_dir.mkdir(parents=True, exist_ok=True)",
          "+",
          "+    per_scale_results = {}",
          "+    summary_rows = []",
          "+",
          "+    for scale in SCALES:",
          "+        scale_data = filter_data_by_scale(data, scale)",
          "+        if scale_data is None:",
          "+            log.warning(\"No models for scale %s, skipping\", scale)",
          "+            continue",
          "+",
          "+        n_total = len(scale_data[\"models\"])",
          "+        unique_dosages = np.unique(scale_data[\"dosages\"]).tolist()",
          "+        log.info(\"=\" * 60)",
          "+        log.info(\"SCALE %s: %d models, dosages=%s\", scale, n_total, unique_dosages)",
          "+        log.info(\"=\" * 60)",
          "+",
          "+        if len(unique_dosages) < 2:",
          "+            log.warning(\"Scale %s has only 1 dosage level — gamma not identifiable \"",
          "+                        \"(prior-dominated)\", scale)",
          "+",
          "+        per_scale_results[scale] = {}",
          "+        scale_dir = output_dir / scale.replace(\".\", \"_\")",
          "+        scale_dir.mkdir(parents=True, exist_ok=True)",
          "+",
          "+        for bench in BENCHMARKS:",
          "+            log.info(\"--- %s / %s ---\", scale, bench)",
          "+            result = run_single_benchmark_fit(",
          "+                bench, scale_data, args_dict, exclude_set, min_item_variance",
          "+            )",
          "+            if result is None:",
          "+                summary_rows.append({",
          "+                    \"scale\": scale, \"benchmark\": bench,",
          "+                    \"gamma_mean\": None, \"ci_low\": None, \"ci_high\": None,",
          "+                    \"rhat\": None, \"ess\": None, \"n_models\": 0, \"n_items\": 0,",
          "+                    \"skipped\": True,",
          "+                })",
          "+                continue",
          "+",
          "+            result[\"scale\"] = scale",
          "+            per_scale_results[scale][bench] = result",
          "+",
          "+            g = result[\"gamma\"]",
          "+            d = result[\"diagnostics\"]",
          "+            row = {",
          "+                \"scale\": scale,",
          "+                \"benchmark\": bench,",
          "+                \"gamma_mean\": g[\"mean\"],",
          "+                \"ci_low\": g[\"q025\"],",
          "+                \"ci_high\": g[\"q975\"],",
          "+                \"rhat\": d.get(\"max_rhat\"),",
          "+                \"ess\": d.get(\"min_ess\"),",
          "+                \"n_models\": result[\"n_models\"],",
          "+                \"n_items\": result[\"n_items\"],",
          "+                \"skipped\": False,",
          "+            }",
          "+            summary_rows.append(row)",
          "+",
          "+            log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, N=%d\",",
          "+                     scale, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],",
          "+                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0), result[\"n_models\"])",
          "+",
          "+            with open(scale_dir / f\"{bench}_results.json\", \"w\") as f:",
          "+                json.dump(result, f, indent=2)",
          "+",
          "+    # Save combined results",
          "+    output = {",
          "+        \"config\": {",
          "+            \"mode\": \"scale_stratified\",",
          "+            \"model_type\": MODEL_TYPE,",
          "+            \"scales\": SCALES,",
          "+            \"benchmarks\": BENCHMARKS,",
          "+            \"exposure\": \"oracle_dosage\",",
          "+            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",",
          "+                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],",
          "+            \"stan_config\": args_dict,",
          "+        },",
          "+        \"per_scale\": per_scale_results,",
          "+        \"summary\": summary_rows,",
          "+    }",
          "+    with open(output_dir / \"scale_stratified_results.json\", \"w\") as f:",
          "+        json.dump(output, f, indent=2)",
          "+",
          "+    # Print summary table",
          "+    print(\"\\n\" + \"=\" * 100)",
          "+    print(\"SCALE-STRATIFIED IRT RESULTS (D105)\")",
          "+    print(\"=\" * 100)",
          "+    hdr = f\"{'Scale':<8} {'Benchmark':<16} {'γ̂':>8} {'CI_low':>8} {'CI_high':>8} {'R̂':>8} {'ESS':>8} {'N_models':>10} {'N_items':>8}\"",
          "+    print(hdr)",
          "+    print(\"-\" * len(hdr))",
          "+    for row in summary_rows:",
          "+        if row.get(\"skipped\"):",
          "+            print(f\"{row['scale']:<8} {row['benchmark']:<16} {'SKIPPED':>8} \"",
          "+                  f\"{'':>8} {'':>8} {'':>8} {'':>8} {row['n_models']:>10} {'':>8}\")",
          "+        else:",
          "+            rhat_str = f\"{row['rhat']:.4f}\" if row['rhat'] is not None else \"N/A\"",
          "+            ess_str = f\"{row['ess']:.0f}\" if row['ess'] is not None else \"N/A\"",
          "+            print(f\"{row['scale']:<8} {row['benchmark']:<16} \"",
          "+                  f\"{row['gamma_mean']:>8.4f} {row['ci_low']:>8.4f} {row['ci_high']:>8.4f} \"",
          "+                  f\"{rhat_str:>8} {ess_str:>8} {row['n_models']:>10} {row['n_items']:>8}\")",
          "+    print(\"-\" * len(hdr))",
          "+",
          "+    # Flag convergence issues",
          "+    for row in summary_rows:",
          "+        if row.get(\"skipped\"):",
          "+            continue",
          "+        warnings = []",
          "+        if row[\"rhat\"] is not None and row[\"rhat\"] > 1.01:",
          "+            warnings.append(f\"R̂={row['rhat']:.4f} > 1.01\")",
          "+        if row[\"ess\"] is not None and row[\"ess\"] < 400:",
          "+            warnings.append(f\"ESS={row['ess']:.0f} < 400\")",
          "+        if row[\"n_models\"] < 5:",
          "+            warnings.append(f\"N_models={row['n_models']} (small sample)\")",
          "+        if warnings:",
          "+            print(f\"  WARNING [{row['scale']}/{row['benchmark']}]: {', '.join(warnings)}\")",
          "+",
          "+    print(f\"\\nResults saved to {output_dir}\")",
          "+",
          "+",
          "+def run_pooled(data, args_dict, exclude_set, args):",
          "+    \"\"\"Original pooled analysis (backward-compatible).\"\"\"",
          "+    all_results = {",
          "+        \"config\": {",
          "+            \"model_type\": MODEL_TYPE,",
          "+            \"scales\": SCALES,",
          "+            \"benchmarks\": BENCHMARKS,",
          "+            \"exposure\": \"oracle_dosage\",",
          "+            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",",
          "+                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],",
          "+            \"item_filter\": {",
          "+                \"exclude_items_file\": args.exclude_items,",
          "+                \"exclude_items_count\": len(exclude_set) if exclude_set else 0,",
          "+                \"min_item_variance\": args.min_item_variance,",
          "+            },",
          "+            \"stan_config\": args_dict,",
          "+        },",
          "+        \"per_benchmark\": {},",
          "+        \"joint_fit\": None,",
          "+    }",
          "+",
          "+    # Phase 1: Per-benchmark IRT fits",
          "+    log.info(\"=\" * 60)",
          "+    log.info(\"PHASE 1: Per-benchmark IRT fits\")",
          "+    log.info(\"=\" * 60)",
          "+",
          "+    for bench in BENCHMARKS:",
          "+        log.info(\"-\" * 40)",
          "+        log.info(\"Fitting %s...\", bench)",
          "+        result = run_single_benchmark_fit(",
          "+            bench, data, args_dict, exclude_set, args.min_item_variance",
          "+        )",
          "+        if result:",
          "+            all_results[\"per_benchmark\"][bench] = result",
          "+            g = result[\"gamma\"]",
          "+            d = result[\"diagnostics\"]",
          "+            log.info(\"[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",",
          "+                     bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],",
          "+                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),",
          "+                     d.get(\"divergent_count\", 0))",
          "+",
          "+            bench_dir = OUTPUT_DIR / bench",
          "+            bench_dir.mkdir(parents=True, exist_ok=True)",
          "+            with open(bench_dir / \"irt_results.json\", \"w\") as f:",
          "+                json.dump(result, f, indent=2)",
          "+",
          "+    # Phase 2: Joint fit (shared gamma)",
          "+    log.info(\"=\" * 60)",
          "+    log.info(\"PHASE 2: Joint fit (shared gamma across benchmarks)\")",
          "+    log.info(\"=\" * 60)",
          "+",
          "+    included_benchmarks = list(all_results[\"per_benchmark\"].keys())",
          "+    joint_result = run_joint_fit(",
          "+        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance",
          "+    )",
          "+    if joint_result:",
          "+        all_results[\"joint_fit\"] = joint_result",
          "+        g = joint_result[\"global_gamma\"]",
          "+        d = joint_result[\"diagnostics\"]",
          "+        log.info(\"JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",",
          "+                 g[\"mean\"], g[\"q025\"], g[\"q975\"],",
          "+                 d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),",
          "+                 d.get(\"divergent_count\", 0))",
          "+",
          "+        with open(OUTPUT_DIR / \"joint_fit_results.json\", \"w\") as f:",
          "+            json.dump(joint_result, f, indent=2)",
          "+",
          "+    # Save full results",
          "+    with open(OUTPUT_DIR / \"pooled_4bench_results.json\", \"w\") as f:",
          "+        json.dump(all_results, f, indent=2)",
          "+",
          "+    # Print summary",
          "+    print(\"\\n\" + \"=\" * 60)",
          "+    print(\"POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)\")",
          "+    print(\"=\" * 60)",
          "+",
          "+    if joint_result:",
          "+        g = joint_result[\"global_gamma\"]",
          "+        d = joint_result[\"diagnostics\"]",
          "+        ppc = joint_result[\"posterior_predictive\"]",
          "+",
          "+        cal = joint_result[\"calibrated_scores\"]",
          "+        if \"ci95_lower\" in cal and \"ci95_upper\" in cal:",
          "+            lowers = np.array(cal[\"ci95_lower\"])",
          "+            uppers = np.array(cal[\"ci95_upper\"])",
          "+            dosages_arr = np.array(joint_result[\"dosages\"])",
          "+            n_total = len(dosages_arr)",
          "+            in_ci = sum(1 for i in range(n_total) if uppers[i] > lowers[i])",
          "+            coverage = in_ci / n_total * 100 if n_total > 0 else 0",
          "+            print(f\"COVERAGE: C95={coverage:.0f}% (all CIs valid)\")",
          "+        else:",
          "+            print(\"COVERAGE: need ground truth reference for proper C95\")",
          "+",
          "+        print(f\"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, \"",
          "+              f\"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]\")",
          "+        print(f\"PPP: {ppc.get('overall_ppp', 'N/A')}\")",
          "+        print(f\"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, \"",
          "+              f\"ESS={d.get('min_ess', 'N/A')}, \"",
          "+              f\"divergences={d.get('divergent_count', 'N/A')}\")",
          "+        print(f\"N_MODELS: {joint_result['n_models']}, \"",
          "+              f\"N_ITEMS: {joint_result['n_total_items']}\")",
          "+",
          "+    print(\"\\nPER_BENCHMARK_GAMMA:\")",
          "+    for bench in BENCHMARKS:",
          "+        if bench in all_results[\"per_benchmark\"]:",
          "+            g = all_results[\"per_benchmark\"][bench][\"gamma\"]",
          "+            n = all_results[\"per_benchmark\"][bench][\"n_models\"]",
          "+            ni = all_results[\"per_benchmark\"][bench][\"n_items\"]",
          "+            print(f\"  {bench}: gamma={g['mean']:.4f} \"",
          "+                  f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"",
          "+                  f\"(N={n}, items={ni})\")",
          "+        else:",
          "+            print(f\"  {bench}: SKIPPED\")",
          "+",
          "+    print(f\"\\nResults saved to {OUTPUT_DIR}\")",
          "+",
          "+",
          " def parse_args():",
          "     parser = argparse.ArgumentParser(",
          "         description=\"Pooled 4-benchmark IRT analysis (2PL+gamma)\""
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

_source line 112_

Now let me verify the full file is syntactically correct:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "30fff38f-55ba-48fd-8dde-29e67d6af071",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bpfcSz1YNRJ4vHV1zkKst",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3484,
      "cache_read_input_tokens": 78929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3484
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

_source line 113_

<details open><summary>🔧 Tool call — Read · `toolu_01DTrB9VuM9iyHGWzuuHrXeY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "321cfd84-2b78-47a7-a661-6163e6253374",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bpfcSz1YNRJ4vHV1zkKst",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3484,
      "cache_read_input_tokens": 78929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3484
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

_source line 114 · 2026-05-16T05:33:51.194Z_

<details><summary>↩ Tool result · `toolu_01DTrB9VuM9iyHGWzuuHrXeY`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Pooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.
4	
5	Runs:
6	  1. Per-benchmark IRT fits (with per-benchmark model exclusions)
7	  2. Joint fit (shared gamma) across benchmarks using intersection models
8	
9	Exclusion rules:
10	  D044: GSM8K exclude d000 configs (format confound)
11	  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept
12	  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)
13	  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)
14	
15	Exposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.
16	"""
17	
18	import argparse
19	import json
20	import logging
21	import os
22	import sys
23	import time
24	from pathlib import Path
25	
26	import numpy as np
27	
28	sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
29	from run_irt_calibration import (
30	    load_pooled_eval_results,
31	    prepare_stan_data,
32	    fit_stan_model,
33	    check_convergence,
34	    posterior_predictive_check,
35	    extract_results,
36	    _summarize_vector,
37	    STAN_MODELS,
38	)
39	
40	log = logging.getLogger(__name__)
41	
42	BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge", "humaneval"]
43	SCALES = ["0.5B", "1.5B", "3B"]
44	MODEL_TYPE = "2pl_gamma"
45	STAN_FILE = STAN_MODELS[MODEL_TYPE]
46	
47	OUTPUT_DIR = Path("/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl")
48	EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
49	
50	
51	def apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):
52	    """Apply D044/D045/D046/D047/D018 per-benchmark exclusions."""
53	    keep = np.ones(len(models), dtype=bool)
54	    reasons = []
55	
56	    for i, m in enumerate(models):
57	        dirname = m.get("dirname", "")
58	        scale = m.get("scale", "")
59	        dosage = m.get("dosage", 0)
60	
61	        # D046/D047: base pretrained
62	        if "base_pretrained" in dirname:
63	            keep[i] = False
64	            reasons.append(f"  D046/D047: {dirname} (base pretrained)")
65	            continue
66	
67	        # D018: deprecated check (dirname contains DEPRECATED)
68	        if "DEPRECATED" in dirname:
69	            keep[i] = False
70	            reasons.append(f"  D018: {dirname} (deprecated)")
71	            continue
72	
73	        # D045: 0.5B MMLU/ARC excluded (position bias)
74	        if "0.5B" in scale and benchmark in ("mmlu", "arc_challenge"):
75	            keep[i] = False
76	            reasons.append(f"  D045: {dirname} (0.5B on {benchmark})")
77	            continue
78	
79	        # D044: GSM8K exclude d000 (format confound)
80	        if benchmark == "gsm8k" and dosage == 0:
81	            keep[i] = False
82	            reasons.append(f"  D044: {dirname} (d000 on gsm8k)")
83	            continue
84	
85	        # Instruct model (no dosage pattern) - keep if aligned
86	        # but skip if not part of dose-response (dosage not parseable)
87	        # Actually Instruct models have dosage=base, which won't parse
88	        # as dosage int. They'll appear with dosage=0 from the loader
89	        # if dirname ends with _aligned without _dXXX pattern.
90	        # The loader sets dosage from parsing, so Instruct models
91	        # are already excluded by parse_model_dir_name returning None.
92	
93	    if reasons:
94	        log.info("Excluded from %s (%d models):", benchmark, len(reasons))
95	        for r in reasons[:10]:
96	            log.info(r)
97	        if len(reasons) > 10:
98	            log.info("  ... and %d more", len(reasons) - 10)
99	
100	    return (
101	        [m for m, k in zip(models, keep) if k],
102	        dosages[keep],
103	        responses[keep],
104	        valid_mask[keep],
105	    )
106	
107	
108	def filter_data_by_scale(data, target_scale):
109	    """Filter pooled data to only include models of a single scale."""
110	    keep = np.array([m.get("scale", "") == target_scale for m in data["models"]])
111	    if not keep.any():
112	        return None
113	    return {
114	        "models": [m for m, k in zip(data["models"], keep) if k],
115	        "dosages": data["dosages"][keep],
116	        "benchmarks": {
117	            bench: {
118	                "responses": bd["responses"][keep],
119	                "n_items": bd["n_items"],
120	                "valid_mask": bd["valid_mask"][keep],
121	            }
122	            for bench, bd in data["benchmarks"].items()
123	        },
124	    }
125	
126	
127	def build_oracle_exposure(dosages, n_items):
128	    """Oracle exposure: dosage_fraction * uniform tau."""
129	    max_d = dosages.max() if dosages.max() > 0 else 1.0
130	    fracs = dosages / max_d
131	    return np.outer(fracs, np.ones(n_items))
132	
133	
134	def filter_items(responses, benchmark, exclude_set=None, min_variance=0.0):
135	    """Remove items by exclusion list and/or low cross-model variance.
136	
137	    Returns (filtered_responses, kept_indices, stats_dict).
138	    """
139	    n_models, n_items = responses.shape
140	    keep = np.ones(n_items, dtype=bool)
141	
142	    n_excluded_by_list = 0
143	    if exclude_set:
144	        for j in range(n_items):
145	            if f"{benchmark}_{j}" in exclude_set:
146	                keep[j] = False
147	                n_excluded_by_list += 1
148	
149	    n_excluded_by_var = 0
150	    if min_variance > 0:
151	        item_var = np.var(responses, axis=0)
152	        low_var = item_var < min_variance
153	        low_var &= keep
154	        n_excluded_by_var = int(low_var.sum())
155	        keep[low_var] = False
156	
157	    kept_indices = np.where(keep)[0]
158	    stats = {
159	        "original": n_items,
160	        "excluded_by_list": n_excluded_by_list,
161	        "excluded_by_variance": n_excluded_by_var,
162	        "remaining": int(keep.sum()),
163	    }
164	    return responses[:, keep], kept_indices, stats
165	
166	
167	def run_single_benchmark_fit(bench, data, args_dict, exclude_set=None, min_item_variance=0.0):
168	    """Run IRT fit for a single benchmark with exclusions."""
169	    if bench not in data["benchmarks"]:
170	        log.warning("Benchmark %s not in data, skipping", bench)
171	        return None
172	
173	    bd = data["benchmarks"][bench]
174	    models_filt, dosages_filt, responses_filt, valid_filt = apply_per_benchmark_exclusions(
175	        data["models"], data["dosages"],
176	        bd["responses"], bd["valid_mask"], bench
177	    )
178	
179	    # Apply valid mask
180	    if not valid_filt.all():
181	        active = valid_filt.astype(bool)
182	        models_filt = [m for m, v in zip(models_filt, active) if v]
183	        dosages_filt = dosages_filt[active]
184	        responses_filt = responses_filt[active]
185	
186	    n_models = len(models_filt)
187	    n_items = bd["n_items"]
188	
189	    if exclude_set or min_item_variance > 0:
190	        responses_filt, kept_indices, fstats = filter_items(
191	            responses_filt, bench, exclude_set, min_item_variance
192	        )
193	        n_items = fstats["remaining"]
194	        log.info("[%s] Item filter: %d -> %d (list=%d, variance=%d)",
195	                 bench, fstats["original"], n_items,
196	                 fstats["excluded_by_list"], fstats["excluded_by_variance"])
197	
198	    log.info("[%s] N_models=%d, N_items=%d", bench, n_models, n_items)
199	
200	    if n_models < 3:
201	        log.warning("[%s] Too few models (%d), skipping", bench, n_models)
202	        return None
203	
204	    exposure = build_oracle_exposure(dosages_filt, n_items)
205	    stan_data = prepare_stan_data(responses_filt, exposure, MODEL_TYPE)
206	
207	    fit, elapsed = fit_stan_model(
208	        STAN_FILE, stan_data,
209	        chains=args_dict["chains"],
210	        iter_warmup=args_dict["warmup"],
211	        iter_sampling=args_dict["samples"],
212	        adapt_delta=args_dict["adapt_delta"],
213	        max_treedepth=args_dict["max_treedepth"],
214	        seed=args_dict["seed"],
215	        parallel_chains=args_dict["parallel_chains"],
216	    )
217	
218	    diagnostics = check_convergence(fit)
219	    ppc = posterior_predictive_check(fit, responses_filt)
220	    results = extract_results(fit, responses_filt, MODEL_TYPE)
221	
222	    return {
223	        "benchmark": bench,
224	        "n_models": n_models,
225	        "n_items": n_items,
226	        "models": [{"dirname": m["dirname"], "dosage": m["dosage"],
227	                     "scale": m.get("scale", "")} for m in models_filt],
228	        "dosages": dosages_filt.tolist(),
229	        "fit_time_sec": round(elapsed, 1),
230	        "diagnostics": diagnostics,
231	        "posterior_predictive": ppc,
232	        "gamma": results.get("gamma", {}),
233	        "calibrated_scores": results.get("calibrated_scores", {}),
234	    }
235	
236	
237	def run_joint_fit(data, benchmarks_to_include, args_dict, exclude_set=None, min_item_variance=0.0):
238	    """Concatenate benchmark items and fit shared-gamma model.
239	
240	    Uses intersection of valid models across all benchmarks (after exclusions).
241	    """
242	    per_bench_filtered = {}
243	    for bench in benchmarks_to_include:
244	        if bench not in data["benchmarks"]:
245	            continue
246	        bd = data["benchmarks"][bench]
247	        models_f, dosages_f, resp_f, valid_f = apply_per_benchmark_exclusions(
248	            data["models"], data["dosages"],
249	            bd["responses"], bd["valid_mask"], bench
250	        )
251	        if not valid_f.all():
252	            active = valid_f.astype(bool)
253	            models_f = [m for m, v in zip(models_f, active) if v]
254	            dosages_f = dosages_f[active]
255	            resp_f = resp_f[active]
256	
257	        per_bench_filtered[bench] = {
258	            "models": models_f,
259	            "dosages": dosages_f,
260	            "responses": resp_f,
261	            "n_items": bd["n_items"],
262	        }
263	
264	    # Find intersection of valid model dirnames across benchmarks
265	    dirname_sets = [set(m["dirname"] for m in bf["models"])
266	                    for bf in per_bench_filtered.values()]
267	    common_dirnames = set.intersection(*dirname_sets) if dirname_sets else set()
268	    log.info("Joint fit: %d common models across %d benchmarks",
269	             len(common_dirnames), len(per_bench_filtered))
270	
271	    if len(common_dirnames) < 3:
272	        log.warning("Too few common models (%d) for joint fit", len(common_dirnames))
273	        return None
274	
275	    # Build concatenated matrices using common model order
276	    ref_bench = list(per_bench_filtered.keys())[0]
277	    ref_models = per_bench_filtered[ref_bench]["models"]
278	    ordered_dirnames = [m["dirname"] for m in ref_models if m["dirname"] in common_dirnames]
279	
280	    all_y = []
281	    all_exp = []
282	    slices = {}
283	    col_offset = 0
284	    joint_models = None
285	    joint_dosages = None
286	
287	    for bench, bf in per_bench_filtered.items():
288	        dirname_to_idx = {m["dirname"]: i for i, m in enumerate(bf["models"])}
289	        indices = [dirname_to_idx[d] for d in ordered_dirnames]
290	
291	        resp_ordered = bf["responses"][indices]
292	        dosages_ordered = bf["dosages"][indices]
293	        n_items = bf["n_items"]
294	
295	        if exclude_set or min_item_variance > 0:
296	            resp_ordered, kept_indices, fstats = filter_items(
297	                resp_ordered, bench, exclude_set, min_item_variance
298	            )
299	            n_items = fstats["remaining"]
300	            log.info("[joint/%s] Item filter: %d -> %d (list=%d, variance=%d)",
301	                     bench, fstats["original"], n_items,
302	                     fstats["excluded_by_list"], fstats["excluded_by_variance"])
303	
304	        exposure = build_oracle_exposure(dosages_ordered, n_items)
305	
306	        all_y.append(resp_ordered)
307	        all_exp.append(exposure)
308	        slices[bench] = (col_offset, col_offset + n_items)
309	        col_offset += n_items
310	
311	        if joint_models is None:
312	            joint_models = [bf["models"][i] for i in indices]
313	            joint_dosages = dosages_ordered
314	
315	    y_concat = np.concatenate(all_y, axis=1)
316	    exp_concat = np.concatenate(all_exp, axis=1)
317	
318	    n_models, n_total = y_concat.shape
319	    log.info("Joint fit: %d models x %d total items", n_models, n_total)
320	    log.info("Joint fit slices: %s", {b: f"{s[0]}-{s[1]}" for b, s in slices.items()})
321	
322	    stan_data = prepare_stan_data(y_concat, exp_concat, MODEL_TYPE)
323	
324	    fit, elapsed = fit_stan_model(
325	        STAN_FILE, stan_data,
326	        chains=args_dict["chains"],
327	        iter_warmup=args_dict["warmup"],
328	        iter_sampling=args_dict["samples"],
329	        adapt_delta=args_dict["adapt_delta"],
330	        max_treedepth=args_dict["max_treedepth"],
331	        seed=args_dict["seed"],
332	        parallel_chains=args_dict["parallel_chains"],
333	    )
334	
335	    diagnostics = check_convergence(fit)
336	    ppc = posterior_predictive_check(fit, y_concat)
337	    results = extract_results(fit, y_concat, MODEL_TYPE)
338	
339	    # Per-benchmark calibrated scores from joint model
340	    gamma_draws = fit.stan_variable("gamma")
341	    theta_draws = fit.stan_variable("theta")
342	    a_draws = fit.stan_variable("a")
343	    b_draws = fit.stan_variable("b")
344	
345	    per_bench_cal = {}
346	    for bench, (start, end) in slices.items():
347	        n_bench_items = end - start
348	        n_draws = gamma_draws.shape[0]
349	        bench_cal = np.zeros((n_draws, n_models))
350	        for draw in range(n_draws):
351	            for i in range(n_models):
352	                total = 0.0
353	                for j in range(start, end):
354	                    eta_clean = a_draws[draw, j] * (theta_draws[draw, i] - b_draws[draw, j])
355	                    total += 1.0 / (1.0 + np.exp(-eta_clean))
356	                bench_cal[draw, i] = total / n_bench_items
357	        per_bench_cal[bench] = {
358	            "mean": bench_cal.mean(axis=0).tolist(),
359	            "sd": bench_cal.std(axis=0).tolist(),
360	        }
361	
362	    return {
363	        "mode": "joint_fit_4bench",
364	        "model_type": MODEL_TYPE,
365	        "n_models": n_models,
366	        "n_total_items": n_total,
367	        "benchmark_slices": {k: list(v) for k, v in slices.items()},
368	        "models": [{"dirname": m["dirname"], "dosage": m["dosage"],
369	                     "scale": m.get("scale", "")} for m in joint_models],
370	        "dosages": joint_dosages.tolist(),
371	        "fit_time_sec": round(elapsed, 1),
372	        "diagnostics": diagnostics,
373	        "posterior_predictive": ppc,
374	        "global_gamma": results.get("gamma", {}),
375	        "calibrated_scores": results.get("calibrated_scores", {}),
376	        "calibrated_scores_per_benchmark": per_bench_cal,
377	    }
378	
379	
380	def run_scale_stratified(data, args_dict, exclude_set, min_item_variance):
381	    """Per-scale per-benchmark IRT fits (D105)."""
382	    output_dir = OUTPUT_DIR / "scale_stratified"
383	    output_dir.mkdir(parents=True, exist_ok=True)
384	
385	    per_scale_results = {}
386	    summary_rows = []
387	
388	    for scale in SCALES:
389	        scale_data = filter_data_by_scale(data, scale)
390	        if scale_data is None:
391	            log.warning("No models for scale %s, skipping", scale)
392	            continue
393	
394	        n_total = len(scale_data["models"])
395	        unique_dosages = np.unique(scale_data["dosages"]).tolist()
396	        log.info("=" * 60)
397	        log.info("SCALE %s: %d models, dosages=%s", scale, n_total, unique_dosages)
398	        log.info("=" * 60)
399	
400	        if len(unique_dosages) < 2:
401	            log.warning("Scale %s has only 1 dosage level — gamma not identifiable "
402	                        "(prior-dominated)", scale)
403	
404	        per_scale_results[scale] = {}
405	        scale_dir = output_dir / scale.replace(".", "_")
406	        scale_dir.mkdir(parents=True, exist_ok=True)
407	
408	        for bench in BENCHMARKS:
409	            log.info("--- %s / %s ---", scale, bench)
410	            result = run_single_benchmark_fit(
411	                bench, scale_data, args_dict, exclude_set, min_item_variance
412	            )
413	            if result is None:
414	                summary_rows.append({
415	                    "scale": scale, "benchmark": bench,
416	                    "gamma_mean": None, "ci_low": None, "ci_high": None,
417	                    "rhat": None, "ess": None, "n_models": 0, "n_items": 0,
418	                    "skipped": True,
419	                })
420	                continue
421	
422	            result["scale"] = scale
423	            per_scale_results[scale][bench] = result
424	
425	            g = result["gamma"]
426	            d = result["diagnostics"]
427	            row = {
428	                "scale": scale,
429	                "benchmark": bench,
430	                "gamma_mean": g["mean"],
431	                "ci_low": g["q025"],
432	                "ci_high": g["q975"],
433	                "rhat": d.get("max_rhat"),
434	                "ess": d.get("min_ess"),
435	                "n_models": result["n_models"],
436	                "n_items": result["n_items"],
437	                "skipped": False,
438	            }
439	            summary_rows.append(row)
440	
441	            log.info("[%s/%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, N=%d",
442	                     scale, bench, g["mean"], g["q025"], g["q975"],
443	                     d.get("max_rhat", 0), d.get("min_ess", 0), result["n_models"])
444	
445	            with open(scale_dir / f"{bench}_results.json", "w") as f:
446	                json.dump(result, f, indent=2)
447	
448	    # Save combined results
449	    output = {
450	        "config": {
451	            "mode": "scale_stratified",
452	            "model_type": MODEL_TYPE,
453	            "scales": SCALES,
454	            "benchmarks": BENCHMARKS,
455	            "exposure": "oracle_dosage",
456	            "exclusions": ["D044_gsm8k_d000", "D045_05B_mmlu_arc",
457	                           "D046_D047_base_pretrained", "D018_deprecated"],
458	            "stan_config": args_dict,
459	        },
460	        "per_scale": per_scale_results,
461	        "summary": summary_rows,
462	    }
463	    with open(output_dir / "scale_stratified_results.json", "w") as f:
464	        json.dump(output, f, indent=2)
465	
466	    # Print summary table
467	    print("\n" + "=" * 100)
468	    print("SCALE-STRATIFIED IRT RESULTS (D105)")
469	    print("=" * 100)
470	    hdr = f"{'Scale':<8} {'Benchmark':<16} {'γ̂':>8} {'CI_low':>8} {'CI_high':>8} {'R̂':>8} {'ESS':>8} {'N_models':>10} {'N_items':>8}"
471	    print(hdr)
472	    print("-" * len(hdr))
473	    for row in summary_rows:
474	        if row.get("skipped"):
475	            print(f"{row['scale']:<8} {row['benchmark']:<16} {'SKIPPED':>8} "
476	                  f"{'':>8} {'':>8} {'':>8} {'':>8} {row['n_models']:>10} {'':>8}")
477	        else:
478	            rhat_str = f"{row['rhat']:.4f}" if row['rhat'] is not None else "N/A"
479	            ess_str = f"{row['ess']:.0f}" if row['ess'] is not None else "N/A"
480	            print(f"{row['scale']:<8} {row['benchmark']:<16} "
481	                  f"{row['gamma_mean']:>8.4f} {row['ci_low']:>8.4f} {row['ci_high']:>8.4f} "
482	                  f"{rhat_str:>8} {ess_str:>8} {row['n_models']:>10} {row['n_items']:>8}")
483	    print("-" * len(hdr))
484	
485	    # Flag convergence issues
486	    for row in summary_rows:
487	        if row.get("skipped"):
488	            continue
489	        warnings = []
490	        if row["rhat"] is not None and row["rhat"] > 1.01:
491	            warnings.append(f"R̂={row['rhat']:.4f} > 1.01")
492	        if row["ess"] is not None and row["ess"] < 400:
493	            warnings.append(f"ESS={row['ess']:.0f} < 400")
494	        if row["n_models"] < 5:
495	            warnings.append(f"N_models={row['n_models']} (small sample)")
496	        if warnings:
497	            print(f"  WARNING [{row['scale']}/{row['benchmark']}]: {', '.join(warnings)}")
498	
499	    print(f"\nResults saved to {output_dir}")
500	
501	
502	def run_pooled(data, args_dict, exclude_set, args):
503	    """Original pooled analysis (backward-compatible)."""
504	    all_results = {
505	        "config": {
506	            "model_type": MODEL_TYPE,
507	            "scales": SCALES,
508	            "benchmarks": BENCHMARKS,
509	            "exposure": "oracle_dosage",
510	            "exclusions": ["D044_gsm8k_d000", "D045_05B_mmlu_arc",
511	                           "D046_D047_base_pretrained", "D018_deprecated"],
512	            "item_filter": {
513	                "exclude_items_file": args.exclude_items,
514	                "exclude_items_count": len(exclude_set) if exclude_set else 0,
515	                "min_item_variance": args.min_item_variance,
516	            },
517	            "stan_config": args_dict,
518	        },
519	        "per_benchmark": {},
520	        "joint_fit": None,
521	    }
522	
523	    # Phase 1: Per-benchmark IRT fits
524	    log.info("=" * 60)
525	    log.info("PHASE 1: Per-benchmark IRT fits")
526	    log.info("=" * 60)
527	
528	    for bench in BENCHMARKS:
529	        log.info("-" * 40)
530	        log.info("Fitting %s...", bench)
531	        result = run_single_benchmark_fit(
532	            bench, data, args_dict, exclude_set, args.min_item_variance
533	        )
534	        if result:
535	            all_results["per_benchmark"][bench] = result
536	            g = result["gamma"]
537	            d = result["diagnostics"]
538	            log.info("[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d",
539	                     bench, g["mean"], g["q025"], g["q975"],
540	                     d.get("max_rhat", 0), d.get("min_ess", 0),
541	                     d.get("divergent_count", 0))
542	
543	            bench_dir = OUTPUT_DIR / bench
544	            bench_dir.mkdir(parents=True, exist_ok=True)
545	            with open(bench_dir / "irt_results.json", "w") as f:
546	                json.dump(result, f, indent=2)
547	
548	    # Phase 2: Joint fit (shared gamma)
549	    log.info("=" * 60)
550	    log.info("PHASE 2: Joint fit (shared gamma across benchmarks)")
551	    log.info("=" * 60)
552	
553	    included_benchmarks = list(all_results["per_benchmark"].keys())
554	    joint_result = run_joint_fit(
555	        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance
556	    )
557	    if joint_result:
558	        all_results["joint_fit"] = joint_result
559	        g = joint_result["global_gamma"]
560	        d = joint_result["diagnostics"]
561	        log.info("JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d",
562	                 g["mean"], g["q025"], g["q975"],
563	                 d.get("max_rhat", 0), d.get("min_ess", 0),
564	                 d.get("divergent_count", 0))
565	
566	        with open(OUTPUT_DIR / "joint_fit_results.json", "w") as f:
567	            json.dump(joint_result, f, indent=2)
568	
569	    # Save full results
570	    with open(OUTPUT_DIR / "pooled_4bench_results.json", "w") as f:
571	        json.dump(all_results, f, indent=2)
572	
573	    # Print summary
574	    print("\n" + "=" * 60)
575	    print("POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)")
576	    print("=" * 60)
577	
578	    if joint_result:
579	        g = joint_result["global_gamma"]
580	        d = joint_result["diagnostics"]
581	        ppc = joint_result["posterior_predictive"]
582	
583	        cal = joint_result["calibrated_scores"]
584	        if "ci95_lower" in cal and "ci95_upper" in cal:
585	            lowers = np.array(cal["ci95_lower"])
586	            uppers = np.array(cal["ci95_upper"])
587	            dosages_arr = np.array(joint_result["dosages"])
588	            n_total = len(dosages_arr)
589	            in_ci = sum(1 for i in range(n_total) if uppers[i] > lowers[i])
590	            coverage = in_ci / n_total * 100 if n_total > 0 else 0
591	            print(f"COVERAGE: C95={coverage:.0f}% (all CIs valid)")
592	        else:
593	            print("COVERAGE: need ground truth reference for proper C95")
594	
595	        print(f"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, "
596	              f"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]")
597	        print(f"PPP: {ppc.get('overall_ppp', 'N/A')}")
598	        print(f"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, "
599	              f"ESS={d.get('min_ess', 'N/A')}, "
600	              f"divergences={d.get('divergent_count', 'N/A')}")
601	        print(f"N_MODELS: {joint_result['n_models']}, "
602	              f"N_ITEMS: {joint_result['n_total_items']}")
603	
604	    print("\nPER_BENCHMARK_GAMMA:")
605	    for bench in BENCHMARKS:
606	        if bench in all_results["per_benchmark"]:
607	            g = all_results["per_benchmark"][bench]["gamma"]
608	            n = all_results["per_benchmark"][bench]["n_models"]
609	            ni = all_results["per_benchmark"][bench]["n_items"]
610	            print(f"  {bench}: gamma={g['mean']:.4f} "
611	                  f"[{g['q025']:.4f}, {g['q975']:.4f}] "
612	                  f"(N={n}, items={ni})")
613	        else:
614	            print(f"  {bench}: SKIPPED")
615	
616	    print(f"\nResults saved to {OUTPUT_DIR}")
617	
618	
619	def parse_args():
620	    parser = argparse.ArgumentParser(
621	        description="Pooled 4-benchmark IRT analysis (2PL+gamma)"
622	    )
623	    parser.add_argument(
624	        "--exclude-items", type=str, default=None,
625	        help="JSON file with list of item_ids to exclude (e.g. [\"mmlu_42\", \"mmlu_103\"])",
626	    )
627	    parser.add_argument(
628	        "--min-item-variance", type=float, default=0.0,
629	        help="Exclude items with cross-model variance below this threshold (default: 0, disabled)",
630	    )
631	    parser.add_argument(
632	        "--stratify-by-scale", action="store_true",
633	        help="Fit IRT independently per model scale (0.5B/1.5B/3B) instead of pooled",
634	    )
635	    parser.add_argument("--chains", type=int, default=4)
636	    parser.add_argument("--warmup", type=int, default=1000)
637	    parser.add_argument("--samples", type=int, default=1000)
638	    parser.add_argument("--adapt-delta", type=float, default=0.95)
639	    parser.add_argument("--max-treedepth", type=int, default=12)
640	    parser.add_argument("--seed", type=int, default=42)
641	    parser.add_argument("--parallel-chains", type=int, default=1)
642	    return parser.parse_args()
643	
644	
645	def main():
646	    logging.basicConfig(
647	        level=logging.INFO,
648	        format="%(asctime)s [%(levelname)s] %(message)s",
649	    )
650	
651	    args = parse_args()
652	
653	    exclude_set = None
654	    if args.exclude_items:
655	        with open(args.exclude_items) as f:
656	            exclude_list = json.load(f)
657	        exclude_set = set(exclude_list)
658	        log.info("Loaded %d item_ids to exclude from %s", len(exclude_set), args.exclude_items)
659	
660	    args_dict = {
661	        "chains": args.chains,
662	        "warmup": args.warmup,
663	        "samples": args.samples,
664	        "adapt_delta": args.adapt_delta,
665	        "max_treedepth": args.max_treedepth,
666	        "seed": args.seed,
667	        "parallel_chains": args.parallel_chains,
668	    }
669	
670	    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
671	
672	    log.info("Loading pooled eval results: scales=%s, benchmarks=%s", SCALES, BENCHMARKS)
673	    t0 = time.time()
674	    data = load_pooled_eval_results(
675	        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True
676	    )
677	    log.info("Loaded %d models in %.1fs", len(data["models"]), time.time() - t0)
678	    log.info("Dosages: %s", data["dosages"].tolist())
679	    log.info("Benchmarks: %s", list(data["benchmarks"].keys()))
680	
681	    if args.stratify_by_scale:
682	        run_scale_stratified(data, args_dict, exclude_set, args.min_item_variance)
683	    else:
684	        run_pooled(data, args_dict, exclude_set, args)
685	
686	
687	if __name__ == "__main__":
688	    main()
689	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "536b3f84-3d40-4447-b2f0-dd8a81cb8ea3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_pooled_4bench_irt.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nPooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.\n\nRuns:\n  1. Per-benchmark IRT fits (with per-benchmark model exclusions)\n  2. Joint fit (shared gamma) across benchmarks using intersection models\n\nExclusion rules:\n  D044: GSM8K exclude d000 configs (format confound)\n  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept\n  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)\n  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)\n\nExposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\n\nsys.path.insert(0, \"/root/contamcal-irt-calibration/exp006\")\nfrom run_irt_calibration import (\n    load_pooled_eval_results,\n    prepare_stan_data,\n    fit_stan_model,\n    check_convergence,\n    posterior_predictive_check,\n    extract_results,\n    _summarize_vector,\n    STAN_MODELS,\n)\n\nlog = logging.getLogger(__name__)\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\", \"humaneval\"]\nSCALES = [\"0.5B\", \"1.5B\", \"3B\"]\nMODEL_TYPE = \"2pl_gamma\"\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\n\nOUTPUT_DIR = Path(\"/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl\")\nEVAL_DIR = \"/root/autodl-tmp/exp001/eval_results\"\n\n\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\n    \"\"\"Apply D044/D045/D046/D047/D018 per-benchmark exclusions.\"\"\"\n    keep = np.ones(len(models), dtype=bool)\n    reasons = []\n\n    for i, m in enumerate(models):\n        dirname = m.get(\"dirname\", \"\")\n        scale = m.get(\"scale\", \"\")\n        dosage = m.get(\"dosage\", 0)\n\n        # D046/D047: base pretrained\n        if \"base_pretrained\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D046/D047: {dirname} (base pretrained)\")\n            continue\n\n        # D018: deprecated check (dirname contains DEPRECATED)\n        if \"DEPRECATED\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D018: {dirname} (deprecated)\")\n            continue\n\n        # D045: 0.5B MMLU/ARC excluded (position bias)\n        if \"0.5B\" in scale and benchmark in (\"mmlu\", \"arc_challenge\"):\n            keep[i] = False\n            reasons.append(f\"  D045: {dirname} (0.5B on {benchmark})\")\n            continue\n\n        # D044: GSM8K exclude d000 (format confound)\n        if benchmark == \"gsm8k\" and dosage == 0:\n            keep[i] = False\n            reasons.append(f\"  D044: {dirname} (d000 on gsm8k)\")\n            continue\n\n        # Instruct model (no dosage pattern) - keep if aligned\n        # but skip if not part of dose-response (dosage not parseable)\n        # Actually Instruct models have dosage=base, which won't parse\n        # as dosage int. They'll appear with dosage=0 from the loader\n        # if dirname ends with _aligned without _dXXX pattern.\n        # The loader sets dosage from parsing, so Instruct models\n        # are already excluded by parse_model_dir_name returning None.\n\n    if reasons:\n        log.info(\"Excluded from %s (%d models):\", benchmark, len(reasons))\n        for r in reasons[:10]:\n            log.info(r)\n        if len(reasons) > 10:\n            log.info(\"  ... and %d more\", len(reasons) - 10)\n\n    return (\n        [m for m, k in zip(models, keep) if k],\n        dosages[keep],\n        responses[keep],\n        valid_mask[keep],\n    )\n\n\ndef filter_data_by_scale(data, target_scale):\n    \"\"\"Filter pooled data to only include models of a single scale.\"\"\"\n    keep = np.array([m.get(\"scale\", \"\") == target_scale for m in data[\"models\"]])\n    if not keep.any():\n        return None\n    return {\n        \"models\": [m for m, k in zip(data[\"models\"], keep) if k],\n        \"dosages\": data[\"dosages\"][keep],\n        \"benchmarks\": {\n            bench: {\n                \"responses\": bd[\"responses\"][keep],\n                \"n_items\": bd[\"n_items\"],\n                \"valid_mask\": bd[\"valid_mask\"][keep],\n            }\n            for bench, bd in data[\"benchmarks\"].items()\n        },\n    }\n\n\ndef build_oracle_exposure(dosages, n_items):\n    \"\"\"Oracle exposure: dosage_fraction * uniform tau.\"\"\"\n    max_d = dosages.max() if dosages.max() > 0 else 1.0\n    fracs = dosages / max_d\n    return np.outer(fracs, np.ones(n_items))\n\n\ndef filter_items(responses, benchmark, exclude_set=None, min_variance=0.0):\n    \"\"\"Remove items by exclusion list and/or low cross-model variance.\n\n    Returns (filtered_responses, kept_indices, stats_dict).\n    \"\"\"\n    n_models, n_items = responses.shape\n    keep = np.ones(n_items, dtype=bool)\n\n    n_excluded_by_list = 0\n    if exclude_set:\n        for j in range(n_items):\n            if f\"{benchmark}_{j}\" in exclude_set:\n                keep[j] = False\n                n_excluded_by_list += 1\n\n    n_excluded_by_var = 0\n    if min_variance > 0:\n        item_var = np.var(responses, axis=0)\n        low_var = item_var < min_variance\n        low_var &= keep\n        n_excluded_by_var = int(low_var.sum())\n        keep[low_var] = False\n\n    kept_indices = np.where(keep)[0]\n    stats = {\n        \"original\": n_items,\n        \"excluded_by_list\": n_excluded_by_list,\n        \"excluded_by_variance\": n_excluded_by_var,\n        \"remaining\": int(keep.sum()),\n    }\n    return responses[:, keep], kept_indices, stats\n\n\ndef run_single_benchmark_fit(bench, data, args_dict, exclude_set=None, min_item_variance=0.0):\n    \"\"\"Run IRT fit for a single benchmark with exclusions.\"\"\"\n    if bench not in data[\"benchmarks\"]:\n        log.warning(\"Benchmark %s not in data, skipping\", bench)\n        return None\n\n    bd = data[\"benchmarks\"][bench]\n    models_filt, dosages_filt, responses_filt, valid_filt = apply_per_benchmark_exclusions(\n        data[\"models\"], data[\"dosages\"],\n        bd[\"responses\"], bd[\"valid_mask\"], bench\n    )\n\n    # Apply valid mask\n    if not valid_filt.all():\n        active = valid_filt.astype(bool)\n        models_filt = [m for m, v in zip(models_filt, active) if v]\n        dosages_filt = dosages_filt[active]\n        responses_filt = responses_filt[active]\n\n    n_models = len(models_filt)\n    n_items = bd[\"n_items\"]\n\n    if exclude_set or min_item_variance > 0:\n        responses_filt, kept_indices, fstats = filter_items(\n            responses_filt, bench, exclude_set, min_item_variance\n        )\n        n_items = fstats[\"remaining\"]\n        log.info(\"[%s] Item filter: %d -> %d (list=%d, variance=%d)\",\n                 bench, fstats[\"original\"], n_items,\n                 fstats[\"excluded_by_list\"], fstats[\"excluded_by_variance\"])\n\n    log.info(\"[%s] N_models=%d, N_items=%d\", bench, n_models, n_items)\n\n    if n_models < 3:\n        log.warning(\"[%s] Too few models (%d), skipping\", bench, n_models)\n        return None\n\n    exposure = build_oracle_exposure(dosages_filt, n_items)\n    stan_data = prepare_stan_data(responses_filt, exposure, MODEL_TYPE)\n\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, responses_filt)\n    results = extract_results(fit, responses_filt, MODEL_TYPE)\n\n    return {\n        \"benchmark\": bench,\n        \"n_models\": n_models,\n        \"n_items\": n_items,\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in models_filt],\n        \"dosages\": dosages_filt.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n    }\n\n\ndef run_joint_fit(data, benchmarks_to_include, args_dict, exclude_set=None, min_item_variance=0.0):\n    \"\"\"Concatenate benchmark items and fit shared-gamma model.\n\n    Uses intersection of valid models across all benchmarks (after exclusions).\n    \"\"\"\n    per_bench_filtered = {}\n    for bench in benchmarks_to_include:\n        if bench not in data[\"benchmarks\"]:\n            continue\n        bd = data[\"benchmarks\"][bench]\n        models_f, dosages_f, resp_f, valid_f = apply_per_benchmark_exclusions(\n            data[\"models\"], data[\"dosages\"],\n            bd[\"responses\"], bd[\"valid_mask\"], bench\n        )\n        if not valid_f.all():\n            active = valid_f.astype(bool)\n            models_f = [m for m, v in zip(models_f, active) if v]\n            dosages_f = dosages_f[active]\n            resp_f = resp_f[active]\n\n        per_bench_filtered[bench] = {\n            \"models\": models_f,\n            \"dosages\": dosages_f,\n            \"responses\": resp_f,\n            \"n_items\": bd[\"n_items\"],\n        }\n\n    # Find intersection of valid model dirnames across benchmarks\n    dirname_sets = [set(m[\"dirname\"] for m in bf[\"models\"])\n                    for bf in per_bench_filtered.values()]\n    common_dirnames = set.intersection(*dirname_sets) if dirname_sets else set()\n    log.info(\"Joint fit: %d common models across %d benchmarks\",\n             len(common_dirnames), len(per_bench_filtered))\n\n    if len(common_dirnames) < 3:\n        log.warning(\"Too few common models (%d) for joint fit\", len(common_dirnames))\n        return None\n\n    # Build concatenated matrices using common model order\n    ref_bench = list(per_bench_filtered.keys())[0]\n    ref_models = per_bench_filtered[ref_bench][\"models\"]\n    ordered_dirnames = [m[\"dirname\"] for m in ref_models if m[\"dirname\"] in common_dirnames]\n\n    all_y = []\n    all_exp = []\n    slices = {}\n    col_offset = 0\n    joint_models = None\n    joint_dosages = None\n\n    for bench, bf in per_bench_filtered.items():\n        dirname_to_idx = {m[\"dirname\"]: i for i, m in enumerate(bf[\"models\"])}\n        indices = [dirname_to_idx[d] for d in ordered_dirnames]\n\n        resp_ordered = bf[\"responses\"][indices]\n        dosages_ordered = bf[\"dosages\"][indices]\n        n_items = bf[\"n_items\"]\n\n        if exclude_set or min_item_variance > 0:\n            resp_ordered, kept_indices, fstats = filter_items(\n                resp_ordered, bench, exclude_set, min_item_variance\n            )\n            n_items = fstats[\"remaining\"]\n            log.info(\"[joint/%s] Item filter: %d -> %d (list=%d, variance=%d)\",\n                     bench, fstats[\"original\"], n_items,\n                     fstats[\"excluded_by_list\"], fstats[\"excluded_by_variance\"])\n\n        exposure = build_oracle_exposure(dosages_ordered, n_items)\n\n        all_y.append(resp_ordered)\n        all_exp.append(exposure)\n        slices[bench] = (col_offset, col_offset + n_items)\n        col_offset += n_items\n\n        if joint_models is None:\n            joint_models = [bf[\"models\"][i] for i in indices]\n            joint_dosages = dosages_ordered\n\n    y_concat = np.concatenate(all_y, axis=1)\n    exp_concat = np.concatenate(all_exp, axis=1)\n\n    n_models, n_total = y_concat.shape\n    log.info(\"Joint fit: %d models x %d total items\", n_models, n_total)\n    log.info(\"Joint fit slices: %s\", {b: f\"{s[0]}-{s[1]}\" for b, s in slices.items()})\n\n    stan_data = prepare_stan_data(y_concat, exp_concat, MODEL_TYPE)\n\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, y_concat)\n    results = extract_results(fit, y_concat, MODEL_TYPE)\n\n    # Per-benchmark calibrated scores from joint model\n    gamma_draws = fit.stan_variable(\"gamma\")\n    theta_draws = fit.stan_variable(\"theta\")\n    a_draws = fit.stan_variable(\"a\")\n    b_draws = fit.stan_variable(\"b\")\n\n    per_bench_cal = {}\n    for bench, (start, end) in slices.items():\n        n_bench_items = end - start\n        n_draws = gamma_draws.shape[0]\n        bench_cal = np.zeros((n_draws, n_models))\n        for draw in range(n_draws):\n            for i in range(n_models):\n                total = 0.0\n                for j in range(start, end):\n                    eta_clean = a_draws[draw, j] * (theta_draws[draw, i] - b_draws[draw, j])\n                    total += 1.0 / (1.0 + np.exp(-eta_clean))\n                bench_cal[draw, i] = total / n_bench_items\n        per_bench_cal[bench] = {\n            \"mean\": bench_cal.mean(axis=0).tolist(),\n            \"sd\": bench_cal.std(axis=0).tolist(),\n        }\n\n    return {\n        \"mode\": \"joint_fit_4bench\",\n        \"model_type\": MODEL_TYPE,\n        \"n_models\": n_models,\n        \"n_total_items\": n_total,\n        \"benchmark_slices\": {k: list(v) for k, v in slices.items()},\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in joint_models],\n        \"dosages\": joint_dosages.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"global_gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n        \"calibrated_scores_per_benchmark\": per_bench_cal,\n    }\n\n\ndef run_scale_stratified(data, args_dict, exclude_set, min_item_variance):\n    \"\"\"Per-scale per-benchmark IRT fits (D105).\"\"\"\n    output_dir = OUTPUT_DIR / \"scale_stratified\"\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    per_scale_results = {}\n    summary_rows = []\n\n    for scale in SCALES:\n        scale_data = filter_data_by_scale(data, scale)\n        if scale_data is None:\n            log.warning(\"No models for scale %s, skipping\", scale)\n            continue\n\n        n_total = len(scale_data[\"models\"])\n        unique_dosages = np.unique(scale_data[\"dosages\"]).tolist()\n        log.info(\"=\" * 60)\n        log.info(\"SCALE %s: %d models, dosages=%s\", scale, n_total, unique_dosages)\n        log.info(\"=\" * 60)\n\n        if len(unique_dosages) < 2:\n            log.warning(\"Scale %s has only 1 dosage level — gamma not identifiable \"\n                        \"(prior-dominated)\", scale)\n\n        per_scale_results[scale] = {}\n        scale_dir = output_dir / scale.replace(\".\", \"_\")\n        scale_dir.mkdir(parents=True, exist_ok=True)\n\n        for bench in BENCHMARKS:\n            log.info(\"--- %s / %s ---\", scale, bench)\n            result = run_single_benchmark_fit(\n                bench, scale_data, args_dict, exclude_set, min_item_variance\n            )\n            if result is None:\n                summary_rows.append({\n                    \"scale\": scale, \"benchmark\": bench,\n                    \"gamma_mean\": None, \"ci_low\": None, \"ci_high\": None,\n                    \"rhat\": None, \"ess\": None, \"n_models\": 0, \"n_items\": 0,\n                    \"skipped\": True,\n                })\n                continue\n\n            result[\"scale\"] = scale\n            per_scale_results[scale][bench] = result\n\n            g = result[\"gamma\"]\n            d = result[\"diagnostics\"]\n            row = {\n                \"scale\": scale,\n                \"benchmark\": bench,\n                \"gamma_mean\": g[\"mean\"],\n                \"ci_low\": g[\"q025\"],\n                \"ci_high\": g[\"q975\"],\n                \"rhat\": d.get(\"max_rhat\"),\n                \"ess\": d.get(\"min_ess\"),\n                \"n_models\": result[\"n_models\"],\n                \"n_items\": result[\"n_items\"],\n                \"skipped\": False,\n            }\n            summary_rows.append(row)\n\n            log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, N=%d\",\n                     scale, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0), result[\"n_models\"])\n\n            with open(scale_dir / f\"{bench}_results.json\", \"w\") as f:\n                json.dump(result, f, indent=2)\n\n    # Save combined results\n    output = {\n        \"config\": {\n            \"mode\": \"scale_stratified\",\n            \"model_type\": MODEL_TYPE,\n            \"scales\": SCALES,\n            \"benchmarks\": BENCHMARKS,\n            \"exposure\": \"oracle_dosage\",\n            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",\n                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],\n            \"stan_config\": args_dict,\n        },\n        \"per_scale\": per_scale_results,\n        \"summary\": summary_rows,\n    }\n    with open(output_dir / \"scale_stratified_results.json\", \"w\") as f:\n        json.dump(output, f, indent=2)\n\n    # Print summary table\n    print(\"\\n\" + \"=\" * 100)\n    print(\"SCALE-STRATIFIED IRT RESULTS (D105)\")\n    print(\"=\" * 100)\n    hdr = f\"{'Scale':<8} {'Benchmark':<16} {'γ̂':>8} {'CI_low':>8} {'CI_high':>8} {'R̂':>8} {'ESS':>8} {'N_models':>10} {'N_items':>8}\"\n    print(hdr)\n    print(\"-\" * len(hdr))\n    for row in summary_rows:\n        if row.get(\"skipped\"):\n            print(f\"{row['scale']:<8} {row['benchmark']:<16} {'SKIPPED':>8} \"\n                  f\"{'':>8} {'':>8} {'':>8} {'':>8} {row['n_models']:>10} {'':>8}\")\n        else:\n            rhat_str = f\"{row['rhat']:.4f}\" if row['rhat'] is not None else \"N/A\"\n            ess_str = f\"{row['ess']:.0f}\" if row['ess'] is not None else \"N/A\"\n            print(f\"{row['scale']:<8} {row['benchmark']:<16} \"\n                  f\"{row['gamma_mean']:>8.4f} {row['ci_low']:>8.4f} {row['ci_high']:>8.4f} \"\n                  f\"{rhat_str:>8} {ess_str:>8} {row['n_models']:>10} {row['n_items']:>8}\")\n    print(\"-\" * len(hdr))\n\n    # Flag convergence issues\n    for row in summary_rows:\n        if row.get(\"skipped\"):\n            continue\n        warnings = []\n        if row[\"rhat\"] is not None and row[\"rhat\"] > 1.01:\n            warnings.append(f\"R̂={row['rhat']:.4f} > 1.01\")\n        if row[\"ess\"] is not None and row[\"ess\"] < 400:\n            warnings.append(f\"ESS={row['ess']:.0f} < 400\")\n        if row[\"n_models\"] < 5:\n            warnings.append(f\"N_models={row['n_models']} (small sample)\")\n        if warnings:\n            print(f\"  WARNING [{row['scale']}/{row['benchmark']}]: {', '.join(warnings)}\")\n\n    print(f\"\\nResults saved to {output_dir}\")\n\n\ndef run_pooled(data, args_dict, exclude_set, args):\n    \"\"\"Original pooled analysis (backward-compatible).\"\"\"\n    all_results = {\n        \"config\": {\n            \"model_type\": MODEL_TYPE,\n            \"scales\": SCALES,\n            \"benchmarks\": BENCHMARKS,\n            \"exposure\": \"oracle_dosage\",\n            \"exclusions\": [\"D044_gsm8k_d000\", \"D045_05B_mmlu_arc\",\n                           \"D046_D047_base_pretrained\", \"D018_deprecated\"],\n            \"item_filter\": {\n                \"exclude_items_file\": args.exclude_items,\n                \"exclude_items_count\": len(exclude_set) if exclude_set else 0,\n                \"min_item_variance\": args.min_item_variance,\n            },\n            \"stan_config\": args_dict,\n        },\n        \"per_benchmark\": {},\n        \"joint_fit\": None,\n    }\n\n    # Phase 1: Per-benchmark IRT fits\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 1: Per-benchmark IRT fits\")\n    log.info(\"=\" * 60)\n\n    for bench in BENCHMARKS:\n        log.info(\"-\" * 40)\n        log.info(\"Fitting %s...\", bench)\n        result = run_single_benchmark_fit(\n            bench, data, args_dict, exclude_set, args.min_item_variance\n        )\n        if result:\n            all_results[\"per_benchmark\"][bench] = result\n            g = result[\"gamma\"]\n            d = result[\"diagnostics\"]\n            log.info(\"[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                     bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                     d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                     d.get(\"divergent_count\", 0))\n\n            bench_dir = OUTPUT_DIR / bench\n            bench_dir.mkdir(parents=True, exist_ok=True)\n            with open(bench_dir / \"irt_results.json\", \"w\") as f:\n                json.dump(result, f, indent=2)\n\n    # Phase 2: Joint fit (shared gamma)\n    log.info(\"=\" * 60)\n    log.info(\"PHASE 2: Joint fit (shared gamma across benchmarks)\")\n    log.info(\"=\" * 60)\n\n    included_benchmarks = list(all_results[\"per_benchmark\"].keys())\n    joint_result = run_joint_fit(\n        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance\n    )\n    if joint_result:\n        all_results[\"joint_fit\"] = joint_result\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        log.info(\"JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d\",\n                 g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                 d.get(\"max_rhat\", 0), d.get(\"min_ess\", 0),\n                 d.get(\"divergent_count\", 0))\n\n        with open(OUTPUT_DIR / \"joint_fit_results.json\", \"w\") as f:\n            json.dump(joint_result, f, indent=2)\n\n    # Save full results\n    with open(OUTPUT_DIR / \"pooled_4bench_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Print summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)\")\n    print(\"=\" * 60)\n\n    if joint_result:\n        g = joint_result[\"global_gamma\"]\n        d = joint_result[\"diagnostics\"]\n        ppc = joint_result[\"posterior_predictive\"]\n\n        cal = joint_result[\"calibrated_scores\"]\n        if \"ci95_lower\" in cal and \"ci95_upper\" in cal:\n            lowers = np.array(cal[\"ci95_lower\"])\n            uppers = np.array(cal[\"ci95_upper\"])\n            dosages_arr = np.array(joint_result[\"dosages\"])\n            n_total = len(dosages_arr)\n            in_ci = sum(1 for i in range(n_total) if uppers[i] > lowers[i])\n            coverage = in_ci / n_total * 100 if n_total > 0 else 0\n            print(f\"COVERAGE: C95={coverage:.0f}% (all CIs valid)\")\n        else:\n            print(\"COVERAGE: need ground truth reference for proper C95\")\n\n        print(f\"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, \"\n              f\"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]\")\n        print(f\"PPP: {ppc.get('overall_ppp', 'N/A')}\")\n        print(f\"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, \"\n              f\"ESS={d.get('min_ess', 'N/A')}, \"\n              f\"divergences={d.get('divergent_count', 'N/A')}\")\n        print(f\"N_MODELS: {joint_result['n_models']}, \"\n              f\"N_ITEMS: {joint_result['n_total_items']}\")\n\n    print(\"\\nPER_BENCHMARK_GAMMA:\")\n    for bench in BENCHMARKS:\n        if bench in all_results[\"per_benchmark\"]:\n            g = all_results[\"per_benchmark\"][bench][\"gamma\"]\n            n = all_results[\"per_benchmark\"][bench][\"n_models\"]\n            ni = all_results[\"per_benchmark\"][bench][\"n_items\"]\n            print(f\"  {bench}: gamma={g['mean']:.4f} \"\n                  f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                  f\"(N={n}, items={ni})\")\n        else:\n            print(f\"  {bench}: SKIPPED\")\n\n    print(f\"\\nResults saved to {OUTPUT_DIR}\")\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(\n        description=\"Pooled 4-benchmark IRT analysis (2PL+gamma)\"\n    )\n    parser.add_argument(\n        \"--exclude-items\", type=str, default=None,\n        help=\"JSON file with list of item_ids to exclude (e.g. [\\\"mmlu_42\\\", \\\"mmlu_103\\\"])\",\n    )\n    parser.add_argument(\n        \"--min-item-variance\", type=float, default=0.0,\n        help=\"Exclude items with cross-model variance below this threshold (default: 0, disabled)\",\n    )\n    parser.add_argument(\n        \"--stratify-by-scale\", action=\"store_true\",\n        help=\"Fit IRT independently per model scale (0.5B/1.5B/3B) instead of pooled\",\n    )\n    parser.add_argument(\"--chains\", type=int, default=4)\n    parser.add_argument(\"--warmup\", type=int, default=1000)\n    parser.add_argument(\"--samples\", type=int, default=1000)\n    parser.add_argument(\"--adapt-delta\", type=float, default=0.95)\n    parser.add_argument(\"--max-treedepth\", type=int, default=12)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--parallel-chains\", type=int, default=1)\n    return parser.parse_args()\n\n\ndef main():\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    args = parse_args()\n\n    exclude_set = None\n    if args.exclude_items:\n        with open(args.exclude_items) as f:\n            exclude_list = json.load(f)\n        exclude_set = set(exclude_list)\n        log.info(\"Loaded %d item_ids to exclude from %s\", len(exclude_set), args.exclude_items)\n\n    args_dict = {\n        \"chains\": args.chains,\n        \"warmup\": args.warmup,\n        \"samples\": args.samples,\n        \"adapt_delta\": args.adapt_delta,\n        \"max_treedepth\": args.max_treedepth,\n        \"seed\": args.seed,\n        \"parallel_chains\": args.parallel_chains,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    log.info(\"Loading pooled eval results: scales=%s, benchmarks=%s\", SCALES, BENCHMARKS)\n    t0 = time.time()\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n    )\n    log.info(\"Loaded %d models in %.1fs\", len(data[\"models\"]), time.time() - t0)\n    log.info(\"Dosages: %s\", data[\"dosages\"].tolist())\n    log.info(\"Benchmarks: %s\", list(data[\"benchmarks\"].keys()))\n\n    if args.stratify_by_scale:\n        run_scale_stratified(data, args_dict, exclude_set, args.min_item_variance)\n    else:\n        run_pooled(data, args_dict, exclude_set, args)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 689,
      "startLine": 1,
      "totalLines": 689
    }
  }
}
```

</details>

---

### Assistant

_source line 115_

<details><summary>Logged reasoning block</summary>

```text
The file looks good. Let me verify it with a Python syntax check locally.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "baa503f0-851e-4b9f-9566-f55936b068b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016p3Bx4JJgwCPvPF59qj9AV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10074,
      "cache_read_input_tokens": 82413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10074
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

_source line 116_

File looks clean. Let me do a syntax check:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "ccba043a-b5a3-436c-9502-aad1315dac47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016p3Bx4JJgwCPvPF59qj9AV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10074,
      "cache_read_input_tokens": 82413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10074
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

_source line 117_

<details open><summary>🔧 Tool call — Bash · `toolu_01GhPd99EeVAkSxddYYYQvrF`</summary>

```json
{
  "command": "python3 -c \"import ast; ast.parse(open('artifacts/run_pooled_4bench_irt.py').read()); print('OK')\"",
  "description": "Syntax check the modified script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "4f6f97ef-6971-48bb-b0e2-26bdeb536403",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016p3Bx4JJgwCPvPF59qj9AV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10074,
      "cache_read_input_tokens": 82413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10074
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

_source line 118 · 2026-05-16T05:33:56.787Z_

<details><summary>↩ Tool result · `toolu_01GhPd99EeVAkSxddYYYQvrF`</summary>

```text
OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "b3e08ed4-1ad4-4309-9cc8-6995d398c947",
  "tool_use_result": {
    "stdout": "OK",
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

_source line 119_

Now let me verify `--help` shows the new argument (won't be able to import the remote module, but we can test the argparser logic separately):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "615225af-ac3d-4c00-9d92-c8966d8cbdcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ei4R4fdcHaTDTFYRkvA73x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 167,
      "cache_read_input_tokens": 92487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 167
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

_source line 120_

<details open><summary>🔧 Tool call — Bash · `toolu_01XYwoxG6sFsPZYFQor18yoS`</summary>

```json
{
  "command": "python3 -c \"\nimport sys, argparse\n\n# Simulate just the argparser\nparser = argparse.ArgumentParser(description='Pooled 4-benchmark IRT analysis (2PL+gamma)')\nparser.add_argument('--exclude-items', type=str, default=None)\nparser.add_argument('--min-item-variance', type=float, default=0.0)\nparser.add_argument('--stratify-by-scale', action='store_true',\n    help='Fit IRT independently per model scale (0.5B/1.5B/3B) instead of pooled')\nparser.add_argument('--chains', type=int, default=4)\nparser.add_argument('--warmup', type=int, default=1000)\nparser.add_argument('--samples', type=int, default=1000)\nparser.add_argument('--adapt-delta', type=float, default=0.95)\nparser.add_argument('--max-treedepth', type=int, default=12)\nparser.add_argument('--seed', type=int, default=42)\nparser.add_argument('--parallel-chains', type=int, default=1)\n\n# Test parsing\nargs = parser.parse_args(['--stratify-by-scale'])\nassert args.stratify_by_scale == True\nassert args.chains == 4\n\nargs2 = parser.parse_args([])\nassert args2.stratify_by_scale == False\n\nprint('Argparse OK')\n\n# Test filter_data_by_scale logic\nimport numpy as np\n\ndef filter_data_by_scale(data, target_scale):\n    keep = np.array([m.get('scale', '') == target_scale for m in data['models']])\n    if not keep.any():\n        return None\n    return {\n        'models': [m for m, k in zip(data['models'], keep) if k],\n        'dosages': data['dosages'][keep],\n        'benchmarks': {\n            bench: {\n                'responses': bd['responses'][keep],\n                'n_items': bd['n_items'],\n                'valid_mask': bd['valid_mask'][keep],\n            }\n            for bench, bd in data['benchmarks'].items()\n        },\n    }\n\n# Mock data\ndata = {\n    'models': [\n        {'dirname': 'Qwen2.5-0.5B_d000_s42', 'scale': '0.5B', 'dosage': 0},\n        {'dirname': 'Qwen2.5-0.5B_d025_s42', 'scale': '0.5B', 'dosage': 25},\n        {'dirname': 'Qwen2.5-1.5B_d000_s42', 'scale': '1.5B', 'dosage': 0},\n        {'dirname': 'Qwen2.5-1.5B_d025_s42', 'scale': '1.5B', 'dosage': 25},\n        {'dirname': 'Qwen2.5-3B_d000_s42', 'scale': '3B', 'dosage': 0},\n        {'dirname': 'Qwen2.5-3B_d100_s42', 'scale': '3B', 'dosage': 100},\n    ],\n    'dosages': np.array([0, 25, 0, 25, 0, 100]),\n    'benchmarks': {\n        'arc_challenge': {\n            'responses': np.random.randint(0, 2, (6, 10)),\n            'n_items': 10,\n            'valid_mask': np.ones(6, dtype=bool),\n        }\n    },\n}\n\n# Test filtering\nresult_05 = filter_data_by_scale(data, '0.5B')\nassert len(result_05['models']) == 2\nassert result_05['dosages'].tolist() == [0, 25]\nassert result_05['benchmarks']['arc_challenge']['responses'].shape == (2, 10)\n\nresult_3b = filter_data_by_scale(data, '3B')\nassert len(result_3b['models']) == 2\n\nresult_7b = filter_data_by_scale(data, '7B')\nassert result_7b is None\n\nprint('filter_data_by_scale OK')\nprint('All tests passed')\n\"\n",
  "description": "Test argparse and filter_data_by_scale logic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "603625c1-e660-4a3e-bf0c-9761bdbfa9d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ei4R4fdcHaTDTFYRkvA73x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 167,
      "cache_read_input_tokens": 92487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 167
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

_source line 121 · 2026-05-16T05:34:14.390Z_

<details><summary>↩ Tool result · `toolu_01XYwoxG6sFsPZYFQor18yoS`</summary>

```text
Argparse OK
filter_data_by_scale OK
All tests passed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "a1a36912-3fe5-4158-b208-4f4e6a62d9cd",
  "tool_use_result": {
    "stdout": "Argparse OK\nfilter_data_by_scale OK\nAll tests passed",
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

_source line 122_

Implementation complete. Summary of changes to `run_pooled_4bench_irt.py`:

**New function: `filter_data_by_scale(data, target_scale)`** (line 108)
- Filters the pooled data dict to only models of a given scale
- Returns None if no models match

**New function: `run_scale_stratified(data, args_dict, exclude_set, min_item_variance)`** (line 380)
- Loops over 0.5B / 1.5B / 3B, filters data per scale
- Runs `run_single_benchmark_fit` for each scale × benchmark combination
- Warns when only 1 dosage level (gamma prior-dominated)
- Saves per-scale JSON results to `OUTPUT_DIR/scale_stratified/&lt;scale>/`
- Prints summary table with γ̂, CI, R̂, ESS, N_models, N_items
- Flags convergence issues (R̂ > 1.01, ESS < 400, small N)

**Refactored: `run_pooled(data, args_dict, exclude_set, args)`** (line 502)
- Extracted from `main()` — identical behavior to before

**Modified: `parse_args()`** (line 619)
- Added `--stratify-by-scale` flag
- Added CLI args for Stan config (`--chains`, `--warmup`, `--samples`, etc.) — previously hardcoded

**Modified: `main()`** (line 645)
- Branches on `args.stratify_by_scale`: calls `run_scale_stratified` or `run_pooled`

D045 exclusion remains active — 0.5B on mmlu/arc_challenge will show as SKIPPED in the table, which is the expected behavior (position bias confound).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "uuid": "fdb05ec5-af51-4a1a-8636-d0a81582c785",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GR1YrTUkmVG5obP7P7krMS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1217,
      "cache_read_input_tokens": 92654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1217
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

_source line 123_

Implementation complete. Summary of changes to `run_pooled_4bench_irt.py`:

**New function: `filter_data_by_scale(data, target_scale)`** (line 108)
- Filters the pooled data dict to only models of a given scale
- Returns None if no models match

**New function: `run_scale_stratified(data, args_dict, exclude_set, min_item_variance)`** (line 380)
- Loops over 0.5B / 1.5B / 3B, filters data per scale
- Runs `run_single_benchmark_fit` for each scale × benchmark combination
- Warns when only 1 dosage level (gamma prior-dominated)
- Saves per-scale JSON results to `OUTPUT_DIR/scale_stratified/&lt;scale>/`
- Prints summary table with γ̂, CI, R̂, ESS, N_models, N_items
- Flags convergence issues (R̂ > 1.01, ESS < 400, small N)

**Refactored: `run_pooled(data, args_dict, exclude_set, args)`** (line 502)
- Extracted from `main()` — identical behavior to before

**Modified: `parse_args()`** (line 619)
- Added `--stratify-by-scale` flag
- Added CLI args for Stan config (`--chains`, `--warmup`, `--samples`, etc.) — previously hardcoded

**Modified: `main()`** (line 645)
- Branches on `args.stratify_by_scale`: calls `run_scale_stratified` or `run_pooled`

D045 exclusion remains active — 0.5B on mmlu/arc_challenge will show as SKIPPED in the table, which is the expected behavior (position bias confound).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 331361,
  "duration_api_ms": 328177,
  "num_turns": 24,
  "stop_reason": "end_turn",
  "session_id": "6bce7c3a-59bf-41ef-807b-d35cbe02bb5d",
  "total_cost_usd": 1.7115344499999998,
  "usage": {
    "input_tokens": 25,
    "cache_creation_input_tokens": 82030,
    "cache_read_input_tokens": 1330287,
    "output_tokens": 17102,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 82030,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 438,
        "cache_read_input_tokens": 92654,
        "cache_creation_input_tokens": 1217,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1217
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2907,
      "outputTokens": 3826,
      "cacheReadInputTokens": 222102,
      "cacheCreationInputTokens": 49425,
      "webSearchRequests": 0,
      "costUSD": 0.10602845000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 25,
      "outputTokens": 17102,
      "cacheReadInputTokens": 1330287,
      "cacheCreationInputTokens": 82030,
      "webSearchRequests": 0,
      "costUSD": 1.605506,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "356ae247-6a81-4a96-961b-d9aa979e6449"
}
```

</details>

---
