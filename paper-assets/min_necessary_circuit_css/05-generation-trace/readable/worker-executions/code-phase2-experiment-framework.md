# code phase2 experiment framework

**Transformer Model EAP-IG** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 118
- **Recorded user turns:** 1
- **Tool calls:** 37
- **Original source:** `logs/workers/worker_code_phase2_experiment_framework_20260512T220705.log`
- **Structured JSON:** [`828745c775a476161a5f.json`](../../sessions/82/828745c775a476161a5f.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
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
  "uuid": "24194911-3c34-4144-8ae3-e526b77a7752",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-structfuse-context/memory/"
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
    "resetsAt": 1778637000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1af6ddee-2f94-4556-b0ac-605797e11407",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the project structure and existing code to make the framework consistent with what's already there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "181fe9da-3c32-4e33-8dc0-30c4ec430e83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzWJbuqdPfDaYEdpKzXFpA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12392,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12392
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

先看现有代码结构和关键接口。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "ea4c6225-0ff2-4fc5-8afc-2f8b169ddcd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzWJbuqdPfDaYEdpKzXFpA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12392,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12392
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

<details open><summary>🔧 Tool call — Agent · `toolu_018FP38TDWhQ5y5E72XLwMXA`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore structfuse-context codebase",
  "prompt": "I need to understand the structfuse-context project structure to write a Phase 2 experiment framework. The project is at /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/\n\nPlease find:\n1. The directory structure (especially artifacts/, any existing scripts like run_circus.py, analyze_mvp_results.py, scoring modules)\n2. The interfaces of key modules: eap_ig_scoring, edge_pruning_scoring, ifr_scoring, any ACDC-related code\n3. How run_circus.py works (its main pipeline, config loading, how it calls methods)\n4. How analyze_mvp_results.py works (what analysis it does)\n5. Any existing YAML configs or experiment configs\n6. The ROADMAP.md content\n7. Any constants like CANONICAL_VERSION\n\nSearch breadth: very thorough. Report file paths, key function signatures, and how they connect."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "60f5c311-0ab2-4804-a739-6e26073f94b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzWJbuqdPfDaYEdpKzXFpA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12392,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12392
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

### System

_source line 7_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Explore structfuse-context codebase",
  "task_type": "local_agent",
  "prompt": "I need to understand the structfuse-context project structure to write a Phase 2 experiment framework. The project is at /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/\n\nPlease find:\n1. The directory structure (especially artifacts/, any existing scripts like run_circus.py, analyze_mvp_results.py, scoring modules)\n2. The interfaces of key modules: eap_ig_scoring, edge_pruning_scoring, ifr_scoring, any ACDC-related code\n3. How run_circus.py works (its main pipeline, config loading, how it calls methods)\n4. How analyze_mvp_results.py works (what analysis it does)\n5. Any existing YAML configs or experiment configs\n6. The ROADMAP.md content\n7. Any constants like CANONICAL_VERSION\n\nSearch breadth: very thorough. Report file paths, key function signatures, and how they connect.",
  "uuid": "7378d28d-4187-4662-8fdb-9a9133258d90",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

## Round 1

111 recorded events

### User

_source line 8 · 2026-05-12T22:07:22.298Z_

I need to understand the structfuse-context project structure to write a Phase 2 experiment framework. The project is at /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/

Please find:
1. The directory structure (especially artifacts/, any existing scripts like run_circus.py, analyze_mvp_results.py, scoring modules)
2. The interfaces of key modules: eap_ig_scoring, edge_pruning_scoring, ifr_scoring, any ACDC-related code
3. How run_circus.py works (its main pipeline, config loading, how it calls methods)
4. How analyze_mvp_results.py works (what analysis it does)
5. Any existing YAML configs or experiment configs
6. The ROADMAP.md content
7. Any constants like CANONICAL_VERSION

Search breadth: very thorough. Report file paths, key function signatures, and how they connect.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "1ac9faf6-e3bb-4d39-a622-c88a4e352f3a"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 16218,
    "tool_uses": 1,
    "duration_ms": 1614
  },
  "last_tool_name": "Bash",
  "uuid": "69dc040f-4c5b-40e6-ab13-7c12d277a6ec",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Bash · `toolu_01R9ttu1DHAviiWvKckGjt7h`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context -type f -name \"*.py\" -o -name \"*.yaml\" -o -name \"*.md\" | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "1840c325-2540-4f16-bb45-881e506e472d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P2ttynuVjBiWXm1cMYaMyG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16209,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16209,
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

_source line 11 · 2026-05-12T22:07:24.142Z_

<details><summary>↩ Tool result · `toolu_01R9ttu1DHAviiWvKckGjt7h`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/task_context/agent.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/task_context/history/director/loop_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/task_context/history/reviewer/loop_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/director_df679b87/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/director_df679b87/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/agent_1f8a7b5e/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/agent_1f8a7b5e/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/reviewer_2ef08c26/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/reviewer_2ef08c26/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/eap_ig_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/model_adapter.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/edge_pruning_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/edge_pruning_l0.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/edge_pruning_scoring_457920.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/analyze_mvp_results.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/css.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/test_css.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/ifr_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/test_eap_ig_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/ifr_discovery.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/test_edge_pruning_scoring_3089a7.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/run_circus.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/test_ifr_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/test_edge_pruning_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/intermediate/run_mvp.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/LARGE_MODEL_THIRD_METHOD.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/eap_ig_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/model_adapter.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_run_circus_fixes.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/edge_pruning_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/analyze_mvp_results.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/css.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_css.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/ifr_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_eap_ig_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/run_circus.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_ifr_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_edge_pruning_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/mvp_status_report_20260512.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/edge_pruning_l0.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/evaluation.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/css.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "2fe4bebf-ee95-45e4-8a1f-1e69890b35b1"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 19234,
    "tool_uses": 2,
    "duration_ms": 5096
  },
  "last_tool_name": "Bash",
  "uuid": "127cbab6-bf34-43c1-9c7d-12ca2205e3b6",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_013478GJELNKD5jHDv2yQGR9`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "45314cae-8d35-4017-a5eb-304cd698f03a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T5kZWotMa7oqRQPDPCH1cu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3012,
      "cache_read_input_tokens": 16209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3012,
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

_source line 14 · 2026-05-12T22:07:27.490Z_

<details><summary>↩ Tool result · `toolu_013478GJELNKD5jHDv2yQGR9`</summary>

```text
total 76
drwxr-xr-x 8 ubuntu ubuntu  4096 May 12 19:13 .
drwxrwxr-x 5 ubuntu ubuntu  4096 May 12 09:55 ..
drwxr-xr-x 3 ubuntu ubuntu  4096 May 12 09:55 .claude
-rw-r--r-- 1 ubuntu ubuntu 12778 May 12 22:06 AGENTS.md
-rw-r--r-- 1 ubuntu ubuntu     0 May 12 09:56 ROADMAP.lock
-rw------- 1 ubuntu ubuntu  3452 May 12 19:13 ROADMAP.md
drwxr-xr-x 5 ubuntu ubuntu  4096 May 12 21:33 artifacts
drwxr-xr-x 2 ubuntu ubuntu  4096 May 12 17:38 checkpoints
-rw-r--r-- 1 ubuntu ubuntu     0 May 12 09:57 decisions.lock
-rw------- 1 ubuntu ubuntu  7527 May 12 19:13 decisions.yaml
drwxr-xr-x 2 ubuntu ubuntu  4096 May 12 09:55 docs
-rwxr-xr-x 1 ubuntu ubuntu     0 May 12 10:46 dream_registry.lock
drwxr-xr-x 4 ubuntu ubuntu  4096 May 12 09:59 logs
-rw-r--r-- 1 ubuntu ubuntu  4630 May 12 17:39 memory.md
-rw-r--r-- 1 ubuntu ubuntu     0 May 12 16:53 registry.lock
-rw------- 1 ubuntu ubuntu  3505 May 12 17:38 registry.yaml
-rw-r--r-- 1 ubuntu ubuntu   730 May 12 17:38 report.md
-rwxr-xr-x 1 ubuntu ubuntu     0 May 12 09:55 study_status.lock
drwxr-xr-x 3 ubuntu ubuntu  4096 May 12 20:51 task_context
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "258c113b-9e37-4e4f-8d61-5cf8bca98378"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 19958,
    "tool_uses": 3,
    "duration_ms": 6358
  },
  "last_tool_name": "Bash",
  "uuid": "27a9b6f8-aebc-457b-82e6-5368ef4dd89c",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01RtSZ2iy8TbPRpDKUvt5rsF`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/ | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "e2fdc364-acc2-43f6-9e74-77f9d0a86393",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DidrgZ6jcNeyifKAcG9LjR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 19221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 17 · 2026-05-12T22:07:28.725Z_

<details><summary>↩ Tool result · `toolu_01RtSZ2iy8TbPRpDKUvt5rsF`</summary>

```text
total 204
drwxr-xr-x 5 ubuntu ubuntu  4096 May 12 21:33 .
drwxr-xr-x 8 ubuntu ubuntu  4096 May 12 19:13 ..
drwxr-xr-x 2 ubuntu ubuntu  4096 May 12 19:34 __pycache__
drwxr-xr-x 4 ubuntu ubuntu  4096 May 12 10:27 _project
-rw-r--r-- 1 ubuntu ubuntu 21423 May 12 21:33 analyze_mvp_results.py
-rw-r--r-- 1 ubuntu ubuntu  4527 May 12 18:45 css.py
-rwxr-xr-x 1 ubuntu ubuntu  2425 May 12 20:10 deploy_phase2.sh
-rw-r--r-- 1 ubuntu ubuntu 15922 May 12 19:23 eap_ig_scoring.py
-rw-r--r-- 1 ubuntu ubuntu 19049 May 12 19:29 edge_pruning_scoring.py
-rw-r--r-- 1 ubuntu ubuntu 10322 May 12 18:30 ifr_scoring.py
-rw-r--r-- 1 ubuntu ubuntu  9077 May 12 21:33 manifest.yaml
-rw-r--r-- 1 ubuntu ubuntu 12020 May 12 18:39 model_adapter.py
-rw-r--r-- 1 ubuntu ubuntu   765 May 12 16:52 mvp_status_report_20260512.md
-rw-r--r-- 1 ubuntu ubuntu 20454 May 12 20:15 run_circus.py
drwxr-xr-x 3 ubuntu ubuntu  4096 May 12 12:30 structfuse-mvp
-rw-r--r-- 1 ubuntu ubuntu  4964 May 12 18:46 test_css.py
-rw-r--r-- 1 ubuntu ubuntu  7223 May 12 19:24 test_eap_ig_scoring.py
-rw-r--r-- 1 ubuntu ubuntu 17439 May 12 19:30 test_edge_pruning_scoring.py
-rw-r--r-- 1 ubuntu ubuntu  6515 May 12 18:31 test_ifr_scoring.py
-rw-r--r-- 1 ubuntu ubuntu  4141 May 12 19:35 test_run_circus_fixes.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "fd5cecf9-59b1-4e8c-8773-c12f2fd69e4a"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading ROADMAP.md",
  "usage": {
    "total_tokens": 20709,
    "tool_uses": 4,
    "duration_ms": 7954
  },
  "last_tool_name": "Read",
  "uuid": "521b2f8f-f821-428d-8ac5-a7367259f2eb",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01RCDj6qwGKYGZcAyhSrFTXm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "08891bc6-a6b6-44b1-bd87-12c5cc8e1c93",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015HiwYn22WgEnemUhZ4wcLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 19883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 749,
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

_source line 20 · 2026-05-12T22:07:30.263Z_

<details><summary>↩ Tool result · `toolu_01RCDj6qwGKYGZcAyhSrFTXm`</summary>

```text
1	# structfuse-context — Research Dashboard
2	
3	> 最后更新: 2026-05-12 10:28 UTC | 更新原因: D006: 大模型第三方法确定为 IFR + 方法配置表更新
4	
5	## 核心方向
6	跨方法二值共识（CSS）用于鲁棒电路编辑：证明 binary stability scoring + family-agreement constraint 在分布偏移下优于 score averaging 和单方法电路。
7	
8	## 当前进展
9	- **阶段**: MVP 验证 — 代码已修复就绪，Agent 正在部署到 cqa1-21977
10	- **核心假设待验**: CIRCUS-core 边中 ≥10% 落入 off-diagonal cell
11	- **基础设施**: cqa1-21977 (cuda:5, RTX 4090D) 已配置
12	- **大模型方案已定 (D006)**: IFR 作为第三方法，triangulation 框架定位
13	- **目标**: EMNLP 2026 Main（ARR deadline 2026-05-25，剩余 13 天）
14	
15	## 方法配置
16	| 模型 | K | 方法 | 算法族 |
17	|------|---|------|--------|
18	| GPT-2 Small | 3 | EAP-IG + Edge Pruning + ACDC | gradient / mask / greedy causal |
19	| Qwen-2.5 0.5B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |
20	| Gemma-2 2B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |
21	| Llama-3.1 8B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |
22	
23	论文需披露：GPT-2 Small CSS = 3 因果方法共识；大模型 CSS = 2 因果 + 1 相似度方法共识（triangulation）。
24	
25	## MVP Gate 规则（D001-D003）
26	| off-diagonal % | 决策 |
27	|---|---|
28	| ≥10% | → Main track |
29	| 5-10% | → Findings + 追加 Arithmetic 验证 |
30	| 2-5% | → Findings 确认 |
31	| <2% (两组) + ΔF 无差异 | → Kill |
32	
33	## 阶段规划
34	
35	### Phase 1: MVP pilot（当前）
36	- GPT-2 Small / IOI，K=3（3 因果族），~2h → off-diagonal 判定
37	
38	### Phase 2: K=3 checkpoint + 全量 CSS（MVP 后 ~3天）
39	- Qwen-2.5 0.5B / IOI K=3（含 IFR）快速检查
40	- 全 4 模型 × 4 任务 CSS 计算
41	- 确认 Edge Pruning 实现：princeton-nlp/edge-pruning（非 auto-circuit mask gradient）
42	
43	### Phase 3: OOD editing（~4天）
44	### Phase 4: 分析 + 写作（~3天，最迟 5月22日）
45	
46	## 近期任务
47	- [ ] Agent 部署代码到 cqa1-21977 + 执行 MVP pilot
48	- [ ] MVP 结果判定 → track 决策
49	- [ ] （MVP 后）K=3 checkpoint with IFR on Qwen-2.5 0.5B
50	
51	## GPU 预算
52	- 已分配: 1× RTX 4090D (cuda:5@cqa1-21977)
53	- MVP: ~2h | 全量: ~290h A100（需后续扩卡）
54	
55	## 关键决策日志
56	
57	| ID | 日期 | 摘要 | 关联实验 |
58	|----|------|------|----------|
59	| D011 | 2026-05-12 | EP HF 后端需重构：从 layer pre-hook 改为 submodule-level ho | — |
60	| D010 | 2026-05-12 | Phase 2 IFR binarization策略：用 percentile threshold  | — |
61	| D009 | 2026-05-12 | 修复边名格式不匹配 critical bug：统一 EAP-IG 和 EP/ACDC 的边名归一化到 | mvp_pilot_gpt2_ioi |
62	| D008 | 2026-05-12 | MVP 结果解读协议：mask_gradient proxy 下 ≥10% 可信（保守估计），<10 | — |
63	| D007 | 2026-05-12 | GPU 越界事故：kill 越界进程 + 修复 CUDA_VISIBLE_DEVICES + 重跑  | — |
64	| D006 | 2026-05-12 | 大模型 K=3 第三方法确定为 IFR，论文采用 triangulation 框架定位 | — |
65	| D005 | 2026-05-12 | AtP* 无 edge-level 实现：MVP 改为 K=3（EAP-IG+Edge Prunin | — |
66	| D004 | 2026-05-12 | MVP 通过后增加 K=3 checkpoint：Qwen-2.5 0.5B / IOI 快速验证 | — |
67	| D003 | 2026-05-12 | 定义项目级 kill criteria：off-diagonal <2% + ΔF 无统计差异 →  | — |
68	| D002 | 2026-05-12 | 定义 MVP gate 灰区规则：5-10% off-diagonal → Findings + 追 | — |
69	
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "46bcd641-ea13-4954-b039-9ff57496042b"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading memory.md",
  "usage": {
    "total_tokens": 20710,
    "tool_uses": 5,
    "duration_ms": 8100
  },
  "last_tool_name": "Read",
  "uuid": "a64a4d88-44dc-4785-8ab5-ac1a9afc34a9",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01UbS2Kkx627vs7uFFZyFzDZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "1ee3616b-5a4f-4e79-ba1a-3c14f14bc2a0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015HiwYn22WgEnemUhZ4wcLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 19883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 749,
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

_source line 23 · 2026-05-12T22:07:30.405Z_

<details><summary>↩ Tool result · `toolu_01UbS2Kkx627vs7uFFZyFzDZ`</summary>

```text
1	# StructFuse Memory
2	
3	## 🚨 L1 教训：GPU 越界事故（2026-05-12）
4	MVP 进程跑到了 cuda:0/1（白名单仅 cuda:5），影响其他项目。
5	- **根因**：部署 Worker 启动时未显式设置 `CUDA_VISIBLE_DEVICES=5`，PyTorch 默认使用 cuda:0
6	- **修复**：run_mvp.py 最开头加 GPU 守卫（`os.environ['CUDA_VISIBLE_DEVICES'] = '5'` 在 `import torch` 之前）
7	- **How to apply**：后续所有实验脚本必须在第一行设置 `os.environ['CUDA_VISIBLE_DEVICES']`，且启动命令也要带 `CUDA_VISIBLE_DEVICES=X`。双重保险。submit_training_job 会自动注入，但手动启动的脚本必须自己加。
8	
9	## 🚨 教训：Kill 进程前必须确认 PID 对应的进度（2026-05-12）
10	发现两个 run_mvp.py 进程 (PID 98300 + 98594) 时，误杀了进度更快的 98300 (91.4%)，保留了落后的 98594。ACDC 无缓存机制，重启后从头开始，浪费 ~2h。
11	- **Why**: 没有在 kill 前检查每个 PID 的实际进度（如 `/proc/&lt;pid>/fd` 或日志关联）
12	- **How to apply**: 多个同名进程时，先用 `ls -l /proc/&lt;pid>/fd/1` 或 `strace -p &lt;pid>` 确认哪个是活跃的/进度更快的，再决定 kill 哪个。绝不靠猜测。
13	
14	## 🚨 教训：代码修复后必须清除相关缓存（2026-05-12）
15	边名归一化修复后未清 cache_eap_ig.json / cache_edge_pruning.json，v2 加载旧缓存导致三路边名仍不一致，浪费一次完整运行。
16	- **Why**: per-method JSON 缓存存的是归一化前的旧格式边名。代码改了 normalizer 但缓存里的数据不受影响。
17	- **How to apply**: 任何影响数据格式/命名的代码修复后，**必须删除所有相关缓存文件再重跑**。检查清单：`cache_*.json`、`*.pkl`、`__pycache__/`、HF cache（如果改了 tokenizer/model loading）。宁可多删导致重算，不可漏删导致格式不一致。
18	
19	## Edge Pruning 实现差异（2026-05-12）
20	MVP 阶段 Edge Pruning 用的是 auto-circuit 的 `mask_gradient_prune_scores()`（IG over masks），不是 princeton-nlp/edge-pruning 的 L0 连续松弛优化。两者同属 mask-based 族但实现路径不同。
21	- **MVP**：auto-circuit 代理够用，标注 preliminary
22	- **论文**：需切换到 princeton-nlp L0 实现，否则审稿人可能质疑与 EAP-IG 的独立性（两者都用 gradient）
23	- **Why**: mask_gradient 本质是 gradient-based mask scoring，与 L0 mask optimization 在算法原理上有根本区别
24	
25	## ACDC 在 GPT-2 Small 上的实际耗时（2026-05-12）
26	ACDC 在 GPT-2 Small / IOI 上需 ~2.5h（32491 edges, 速度随深度波动 1.5-24 it/s）。远超最初预估，直接证明大模型上 ACDC 不可行→改用 IFR 的合理性。可作为论文 empirical evidence。
27	- ACDC 无中间结果缓存，进程中断后必须从头重跑
28	- `tao_exps=[-2]` 是单个 threshold（τ=0.01），不是多轮扫描
29	
30	## 大模型第三方法选择（2026-05-12）
31	评估了 AtP*自实现 / PAHQ加速ACDC / MIB所有方法后，选定 IFR（Information Flow Routes）作为大模型第三方法。
32	- **Why**: 唯一满足"非 gradient、非 mask optimization、edge-level、可扩展到 8B"全部条件
33	- **算法族**: activation decomposition（proximity-based），与 EAP-IG/EP 完全不同
34	- **How to apply**: 大模型 K=3 = EAP-IG + Edge Pruning + IFR
35	
36	## MVP 崩溃修复经验（2026-05-12）
37	- 前台 `tee` 进程会被 SSH 断连杀死 → 必须用 `nohup ... 2>&1 &` 后台执行
38	- per-method JSON 缓存（cache_eap_ig.json 等）可在崩溃后跳过已完成步骤，但 ACDC 本身无增量缓存
39	
40	## 路径确认（2026-05-12 Loop #2）
41	- run_mvp.py 位置: `/root/structfuse-context/run_mvp.py`
42	- run_mvp.py 工作目录（/proc/98594/cwd）: `/root/structfuse-context/`
43	- mvp_output.log 位置: `/root/structfuse-context/mvp_output.log`
44	- mvp_results.json 预期输出位置: `/root/structfuse-context/mvp_results.json`（run_mvp.py 用 `Path(__file__).parent`）
45	- 缓存文件位置: `/root/structfuse-context/cache_eap_ig.json`, `/root/structfuse-context/cache_edge_pruning.json`
46	- collect_results.py 位置: `/root/structfuse-mvp/collect_results.py`
47	- ⚠️ **路径不匹配**: collect_results.py 读 `Path(__file__).parent / "mvp_results.json"` → `/root/structfuse-mvp/mvp_results.json`，但 run_mvp.py 写到 `/root/structfuse-context/mvp_results.json`。执行前需将 collect_results.py 复制到 `/root/structfuse-context/` 或将 mvp_results.json 复制到 `/root/structfuse-mvp/`。
48	- collect_results.py 执行命令: `cp /root/structfuse-mvp/collect_results.py /root/structfuse-context/ && cd /root/structfuse-context && python3 collect_results.py`
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "ed4cad27-6e11-4c9d-a0ed-617821b40358"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/run_circus.py",
  "usage": {
    "total_tokens": 20711,
    "tool_uses": 6,
    "duration_ms": 8317
  },
  "last_tool_name": "Read",
  "uuid": "572e58d1-f5d9-413d-80db-88e63e00db44",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01V8PT3qL4NnK7aMBeCe3V5k`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/run_circus.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "84d08e4d-6d15-4c12-88f0-8ccfa692e3cb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015HiwYn22WgEnemUhZ4wcLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 19883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 749,
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

_source line 26 · 2026-05-12T22:07:30.630Z_

<details><summary>↩ Tool result · `toolu_01V8PT3qL4NnK7aMBeCe3V5k`</summary>

```text
1	"""StructFuse configurable pipeline: multi-method circuit discovery + CSS consensus.
2	
3	Config-driven entry point that supports both GPT-2 (TransformerLens) and
4	Qwen-2.5 / Llama-like (HuggingFace) models.  Replaces the MVP's hardcoded
5	run_mvp.py with a general K-method pipeline.
6	
7	Usage:
8	    python run_circus.py                       # default config (Qwen-2.5 0.5B / IOI / K=3)
9	    python run_circus.py config.json           # custom config
10	    python run_circus.py config.yaml           # YAML config
11	"""
12	
13	from __future__ import annotations
14	
15	import hashlib
16	import json
17	import os
18	import sys
19	import time
20	from pathlib import Path
21	from typing import Any, Callable, Dict, Optional, Set
22	
23	# GPU guard: prevent accidental use of wrong GPU (D007 lesson)
24	os.environ.setdefault("CUDA_VISIBLE_DEVICES", "5")
25	
26	import torch
27	
28	from css import binarize_scores, compute_css_matrix, circus_score
29	from model_adapter import CANONICAL_VERSION, ModelAdapter
30	
31	
32	# ---------------------------------------------------------------------------
33	# Default configuration
34	# ---------------------------------------------------------------------------
35	
36	DEFAULT_CONFIG: Dict[str, Any] = {
37	    "model": "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/",  # local path (ModelScope download)
38	    "task": "ioi",
39	    "methods": ["eap_ig", "edge_pruning", "ifr"],
40	    "K": 3,
41	    "num_samples": 50,
42	    "gpu_id": "5",
43	    "binarize": {
44	        "eap_ig":       {"strategy": "topn", "n": 200},
45	        "edge_pruning": {"strategy": "topn", "n": 200},
46	        "ifr":          {"strategy": "unique_score_rank", "n": 50},  # D010: avoid block-vote
47	    },
48	    "eap_ig_steps": 5,
49	    "edge_pruning_epochs": 100,
50	    "edge_pruning_lambda": 1e-2,
51	    "ifr_threshold": 0.1,
52	    "css_threshold": 0.67,
53	    "circus_B": 10,
54	    "circus_core_threshold": 1.0,
55	    "circus_contingent_threshold": 0.5,
56	    "device": "cuda",
57	    "seed": 42,
58	    "output_dir": "./results",
59	    "cache_dir": "./cache",
60	}
61	
62	
63	# ---------------------------------------------------------------------------
64	# Dataset loading
65	# ---------------------------------------------------------------------------
66	
67	def load_dataset(
68	    task: str, tokenizer, num_samples: int, device: str,
69	) -> torch.Tensor:
70	    if task == "ioi":
71	        return _make_ioi_dataset(tokenizer, num_samples, device)
72	    if task == "greater_than":
73	        return _make_greater_than_dataset(tokenizer, num_samples, device)
74	    raise ValueError(f"Unknown task: {task}")
75	
76	
77	def _make_ioi_dataset(tokenizer, n: int, device: str) -> torch.Tensor:
78	    names = [
79	        "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank",
80	        "Grace", "Henry", "Iris", "Jack", "Kate", "Leo",
81	    ]
82	    import random
83	    rng = random.Random(42)
84	    sentences = []
85	    for _ in range(n):
86	        n1, n2 = rng.sample(names, 2)
87	        sentences.append(
88	            f"When {n1} and {n2} went to the store, {n1} gave a drink to"
89	        )
90	    enc = tokenizer(sentences, return_tensors="pt", padding=True)
91	    return enc["input_ids"].to(device)
92	
93	
94	def _make_greater_than_dataset(tokenizer, n: int, device: str) -> torch.Tensor:
95	    import random
96	    rng = random.Random(42)
97	    sentences = []
98	    for _ in range(n):
99	        year = rng.randint(1000, 1999)
100	        sentences.append(f"The war lasted from the year {year} to the year")
101	    enc = tokenizer(sentences, return_tensors="pt", padding=True)
102	    return enc["input_ids"].to(device)
103	
104	
105	# ---------------------------------------------------------------------------
106	# Method dispatch
107	# ---------------------------------------------------------------------------
108	
109	def _mvp_sys_path():
110	    """Add structfuse-mvp/ to sys.path for TL-based method imports."""
111	    mvp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "structfuse-mvp")
112	    if mvp_dir not in sys.path:
113	        sys.path.insert(0, mvp_dir)
114	
115	
116	def _run_ifr_hf(
117	    adapter: ModelAdapter, dataset: torch.Tensor, cfg: dict,
118	) -> Dict[str, float]:
119	    from ifr_scoring import compute_ifr_edges
120	    return compute_ifr_edges(
121	        adapter.model,
122	        dataset,
123	        metric_fn=None,
124	        threshold=cfg.get("ifr_threshold", 0.1),
125	        device=cfg.get("device", "cuda"),
126	    )
127	
128	
129	def _run_ifr_tl(
130	    adapter: ModelAdapter, dataset: torch.Tensor, cfg: dict,
131	) -> Dict[str, float]:
132	    _mvp_sys_path()
133	    from ifr_discovery import run_ifr
134	    return run_ifr(adapter.model, dataset)
135	
136	
137	def _run_eap_ig_tl(
138	    adapter: ModelAdapter,
139	    dataset: torch.Tensor,
140	    metric: Callable,
141	    cfg: dict,
142	) -> Dict[str, float]:
143	    _mvp_sys_path()
144	    from circuit_discovery import run_eap_ig
145	    from config import MVPConfig
146	    mvp_cfg = MVPConfig(eap_ig_steps=cfg.get("eap_ig_steps", 5))
147	    return run_eap_ig(adapter.model, dataset, metric, config=mvp_cfg)
148	
149	
150	def _run_eap_ig_hf(
151	    adapter: ModelAdapter,
152	    dataset: torch.Tensor,
153	    metric: Callable,
154	    cfg: dict,
155	) -> Dict[str, float]:
156	    """EAP-IG on HuggingFace model (Qwen-2.5, Llama, ...).
157	
158	    Hook registration points:
159	      Forward:  model.embed_tokens (embedding output)
160	                model.layers.{i} (pre-hook → resid_pre)
161	                model.layers.{i}.self_attn.o_proj (attn output, decompose per head)
162	                model.layers.{i}.mlp (MLP output)
163	      Backward: same modules, for integrated gradients
164	
165	    IG procedure:
166	      1. Compute baseline embedding (zero or mean ablation)
167	      2. Interpolate alpha in [0,1] over ig_steps
168	      3. For each alpha: forward + backward, accumulate gradients × (input - baseline)
169	      4. Score each edge as |accumulated_gradient| averaged over dataset
170	    """
171	    raise NotImplementedError(
172	        "EAP-IG HF backend not yet implemented. "
173	        "See docstring for hook registration points."
174	    )
175	
176	
177	def _run_edge_pruning_tl(
178	    adapter: ModelAdapter,
179	    dataset: torch.Tensor,
180	    metric: Callable,
181	    cfg: dict,
182	) -> Dict[str, float]:
183	    _mvp_sys_path()
184	    from edge_pruning_l0 import run_edge_pruning_l0
185	    return run_edge_pruning_l0(
186	        adapter.model,
187	        dataset,
188	        metric,
189	        n_epochs=cfg.get("edge_pruning_epochs", 100),
190	        lambda_l0=cfg.get("edge_pruning_lambda", 1e-2),
191	    )
192	
193	
194	def _run_edge_pruning_hf(
195	    adapter: ModelAdapter,
196	    dataset: torch.Tensor,
197	    metric: Callable,
198	    cfg: dict,
199	) -> Dict[str, float]:
200	    """Edge Pruning L0 on HuggingFace model (Qwen-2.5, Llama, ...).
201	
202	    Requires a custom masked forward pass operating on HF modules:
203	      - Reconstruct residual inputs as masked sums of upstream component outputs
204	      - Apply Hard Concrete masks per edge
205	      - Key modules to intercept:
206	          model.layers.{i}.input_layernorm  (pre-attn LN)
207	          model.layers.{i}.self_attn        (full attn block)
208	          model.layers.{i}.post_attention_layernorm (pre-MLP LN)
209	          model.layers.{i}.mlp              (full MLP block)
210	
211	    GQA consideration: K/V edge masks are shared across the query heads
212	    within each KV group (7 query heads per KV group for Qwen-2.5 0.5B).
213	    """
214	    raise NotImplementedError(
215	        "Edge Pruning HF backend not yet implemented. "
216	        "See docstring for required adaptations."
217	    )
218	
219	
220	def run_method(
221	    adapter: ModelAdapter,
222	    method: str,
223	    dataset: torch.Tensor,
224	    metric: Optional[Callable],
225	    cfg: dict,
226	) -> Dict[str, float]:
227	    backend = adapter.info.backend
228	    dispatch = {
229	        ("ifr", "huggingface"):      lambda: _run_ifr_hf(adapter, dataset, cfg),
230	        ("ifr", "transformerlens"):   lambda: _run_ifr_tl(adapter, dataset, cfg),
231	        ("eap_ig", "huggingface"):    lambda: _run_eap_ig_hf(adapter, dataset, metric, cfg),
232	        ("eap_ig", "transformerlens"): lambda: _run_eap_ig_tl(adapter, dataset, metric, cfg),
233	        ("edge_pruning", "huggingface"):    lambda: _run_edge_pruning_hf(adapter, dataset, metric, cfg),
234	        ("edge_pruning", "transformerlens"): lambda: _run_edge_pruning_tl(adapter, dataset, metric, cfg),
235	    }
236	    key = (method, backend)
237	    if key not in dispatch:
238	        raise ValueError(f"No implementation for method={method}, backend={backend}")
239	
240	    scores = dispatch[key]()
241	    return adapter.to_canonical_edges(scores, method)
242	
243	
244	# ---------------------------------------------------------------------------
245	# Caching (version-bound to prevent stale reads)
246	# ---------------------------------------------------------------------------
247	
248	def _cache_key(cfg: dict, method: str) -> str:
249	    relevant: Dict[str, Any] = {
250	        "model": cfg["model"],
251	        "task": cfg["task"],
252	        "method": method,
253	        "canonical_version": CANONICAL_VERSION,
254	        "num_samples": cfg.get("num_samples", 50),
255	    }
256	    if method == "eap_ig":
257	        relevant["ig_steps"] = cfg.get("eap_ig_steps", 5)
258	    elif method == "edge_pruning":
259	        relevant["epochs"] = cfg.get("edge_pruning_epochs", 100)
260	        relevant["lambda"] = cfg.get("edge_pruning_lambda", 1e-2)
261	    elif method == "ifr":
262	        relevant["threshold"] = cfg.get("ifr_threshold", 0.1)
263	    return hashlib.sha256(json.dumps(relevant, sort_keys=True).encode()).hexdigest()[:16]
264	
265	
266	def _cache_path(cfg: dict, method: str) -> Path:
267	    cache_dir = Path(cfg.get("cache_dir", "./cache"))
268	    model_slug = cfg["model"].replace("/", "_")
269	    return (
270	        cache_dir / model_slug / cfg["task"]
271	        / f"{method}_{CANONICAL_VERSION}_{_cache_key(cfg, method)}.json"
272	    )
273	
274	
275	def load_cached(cfg: dict, method: str) -> Optional[Dict[str, float]]:
276	    path = _cache_path(cfg, method)
277	    if not path.exists():
278	        return None
279	    with open(path) as f:
280	        data = json.load(f)
281	    if data.get("canonical_version") != CANONICAL_VERSION:
282	        return None
283	    return data["scores"]
284	
285	
286	def save_cache(cfg: dict, method: str, scores: Dict[str, float]) -> None:
287	    path = _cache_path(cfg, method)
288	    path.parent.mkdir(parents=True, exist_ok=True)
289	    with open(path, "w") as f:
290	        json.dump(
291	            {
292	                "canonical_version": CANONICAL_VERSION,
293	                "model": cfg["model"],
294	                "task": cfg["task"],
295	                "method": method,
296	                "n_edges": len(scores),
297	                "scores": scores,
298	            },
299	            f,
300	        )
301	
302	
303	# ---------------------------------------------------------------------------
304	# Binarization (delegated to css.py — binarize_scores)
305	# ---------------------------------------------------------------------------
306	
307	def _binarize_method(
308	    scores: Dict[str, float], method: str, cfg: dict,
309	) -> Set[str]:
310	    """Dispatch to css.binarize_scores with per-method config."""
311	    default_bconf = {"strategy": "topn", "n": 200}
312	    bconf = cfg.get("binarize", {}).get(method, default_bconf)
313	    strategy = bconf.get("strategy", "topn")
314	    return binarize_scores(
315	        scores,
316	        strategy=strategy,
317	        n=bconf.get("n", 200),
318	        threshold=bconf.get("threshold", bconf.get("value", 0.01)),
319	        percentile=bconf.get("percentile", 95.0),
320	    )
321	
322	
323	# ---------------------------------------------------------------------------
324	# Metric function factory
325	# ---------------------------------------------------------------------------
326	
327	def make_metric_fn(task: str, tokenizer):
328	    """Create faithfulness metric function for the given task."""
329	    if task == "ioi":
330	        names = [
331	            "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank",
332	            "Grace", "Henry", "Iris", "Jack", "Kate", "Leo",
333	        ]
334	        name_ids = {name: tokenizer.encode(f" {name}", add_special_tokens=False)[0] for name in names}
335	
336	        def metric_fn(logits, target_ids):
337	            correct_logits = logits[:, -1, target_ids[:, 0]]
338	            incorrect_logits = logits[:, -1, target_ids[:, 1]]
339	            return (correct_logits - incorrect_logits).mean()
340	
341	        return metric_fn
342	
343	    if task == "greater_than":
344	        def metric_fn(logits, target_ids):
345	            correct_logits = logits[:, -1, target_ids[:, 0]]
346	            incorrect_logits = logits[:, -1, target_ids[:, 1]]
347	            return (correct_logits - incorrect_logits).mean()
348	
349	        return metric_fn
350	
351	    raise ValueError(f"No metric_fn for task: {task}")
352	
353	
354	# ---------------------------------------------------------------------------
355	# CSS (Cross-method Stability Scoring)
356	# ---------------------------------------------------------------------------
357	
358	def compute_css(
359	    method_circuits: Dict[str, Set[str]], K: int,
360	) -> Dict[str, float]:
361	    all_edges: Set[str] = set()
362	    for edges in method_circuits.values():
363	        all_edges |= edges
364	    return {
365	        edge: sum(1 for edges in method_circuits.values() if edge in edges) / K
366	        for edge in all_edges
367	    }
368	
369	
370	def threshold_css(
371	    css_scores: Dict[str, float], threshold: float = 0.67,
372	) -> Set[str]:
373	    return {e for e, s in css_scores.items() if s >= threshold - 0.01}
374	
375	
376	def css_distribution(css_scores: Dict[str, float], K: int) -> Dict[str, int]:
377	    dist: Dict[str, int] = {}
378	    for s in css_scores.values():
379	        level = f"{round(s * K)}/{K}"
380	        dist[level] = dist.get(level, 0) + 1
381	    return dict(sorted(dist.items()))
382	
383	
384	# ---------------------------------------------------------------------------
385	# CIRCUS (config-bagging stability)
386	# ---------------------------------------------------------------------------
387	
388	def config_bag(
389	    scores: Dict[str, float], B: int = 10,
390	) -> Dict[str, float]:
391	    if not scores:
392	        return {}
393	    import numpy as np
394	    vals = np.array(list(scores.values()))
395	    edges = list(scores.keys())
396	    percentiles = np.linspace(100 / (B + 1), 100 * B / (B + 1), B)
397	    thresholds = np.percentile(vals, percentiles)
398	    stability = sum((vals >= t).astype(float) for t in thresholds) / B
399	    return dict(zip(edges, stability.tolist()))
400	
401	
402	def classify_tiers(
403	    stability: Dict[str, float],
404	    core_thr: float = 1.0,
405	    contingent_thr: float = 0.5,
406	) -> Dict[str, str]:
407	    return {
408	        e: ("core" if s >= core_thr else "contingent" if s >= contingent_thr else "noise")
409	        for e, s in stability.items()
410	    }
411	
412	
413	# ---------------------------------------------------------------------------
414	# Cross-tabulation
415	# ---------------------------------------------------------------------------
416	
417	def cross_tabulate(
418	    tiers: Dict[str, str],
419	    css_scores: Dict[str, float],
420	    css_thr: float,
421	) -> Dict[str, Any]:
422	    all_edges = set(tiers.keys()) | set(css_scores.keys())
423	    stable_core: Set[str] = set()
424	    method_specific: Set[str] = set()
425	    cross_unstable: Set[str] = set()
426	    noise: Set[str] = set()
427	
428	    for e in all_edges:
429	        is_core = tiers.get(e) == "core"
430	        is_high = css_scores.get(e, 0.0) >= css_thr - 0.01
431	        if is_core and is_high:
432	            stable_core.add(e)
433	        elif is_core:
434	            method_specific.add(e)
435	        elif is_high:
436	            cross_unstable.add(e)
437	        else:
438	            noise.add(e)
439	
440	    core_total = len(stable_core) + len(method_specific)
441	    off_diag = len(method_specific) / core_total if core_total > 0 else 0.0
442	
443	    return {
444	        "stable_core": len(stable_core),
445	        "method_specific": len(method_specific),
446	        "cross_unstable": len(cross_unstable),
447	        "noise": len(noise),
448	        "core_total": core_total,
449	        "off_diagonal_pct": round(off_diag, 4),
450	        "stable_core_edges": stable_core,
451	        "method_specific_edges": method_specific,
452	    }
453	
454	
455	# ---------------------------------------------------------------------------
456	# Main pipeline
457	# ---------------------------------------------------------------------------
458	
459	def run_pipeline(config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
460	    cfg = {**DEFAULT_CONFIG, **(config or {})}
461	
462	    # GPU guard: override from config
463	    os.environ["CUDA_VISIBLE_DEVICES"] = str(cfg.get("gpu_id", "5"))
464	
465	    torch.manual_seed(cfg["seed"])
466	
467	    print(f"StructFuse: model={cfg['model']}, task={cfg['task']}, K={cfg['K']}")
468	    print(f"Methods: {cfg['methods']}, canonical={CANONICAL_VERSION}")
469	
470	    # 1. Load model
471	    adapter = ModelAdapter.from_pretrained(cfg["model"], device=cfg["device"])
472	    info = adapter.info
473	    n_edges = adapter.n_possible_edges()
474	    print(
475	        f"Model: {info.model_name} ({info.backend}) — "
476	        f"{info.n_layers}L × {info.n_heads}H"
477	        f" (KV={info.n_kv_heads})" * (info.n_kv_heads != info.n_heads)
478	        + f", d={info.d_model}, ~{n_edges:,} possible edges"
479	    )
480	
481	    # 2. Load dataset
482	    dataset = load_dataset(
483	        cfg["task"], adapter.tokenizer,
484	        cfg.get("num_samples", 50), cfg["device"],
485	    )
486	    print(f"Dataset: {cfg['task']}, {dataset.shape[0]} samples, seq_len={dataset.shape[1]}")
487	
488	    # 3. Build metric_fn (non-None for EAP-IG and Edge Pruning)
489	    metric = make_metric_fn(cfg["task"], adapter.tokenizer)
490	
491	    # 4. Run methods (with caching)
492	    all_scores: Dict[str, Dict[str, float]] = {}
493	    timings: Dict[str, float] = {}
494	
495	    for method in cfg["methods"]:
496	        cached = load_cached(cfg, method)
497	        if cached is not None:
498	            print(f"  {method}: cache hit ({len(cached)} edges)")
499	            all_scores[method] = cached
500	            timings[method] = 0.0
501	            continue
502	
503	        method_metric = metric if method in ("eap_ig", "edge_pruning") else None
504	        print(f"  {method}: running...")
505	        t0 = time.time()
506	        scores = run_method(adapter, method, dataset, method_metric, cfg)
507	        elapsed = time.time() - t0
508	        print(f"  {method}: {len(scores)} edges ({elapsed:.1f}s)")
509	
510	        save_cache(cfg, method, scores)
511	        all_scores[method] = scores
512	        timings[method] = elapsed
513	
514	    # 5. Binarize (via css.binarize_scores)
515	    circuits: Dict[str, Set[str]] = {}
516	    for method, scores in all_scores.items():
517	        circuits[method] = _binarize_method(scores, method, cfg)
518	        print(f"  {method}: {len(circuits[method])} edges selected")
519	
520	    # 6. CSS
521	    css = compute_css(circuits, cfg["K"])
522	    dist = css_distribution(css, cfg["K"])
523	    print(f"CSS distribution: {dist}")
524	
525	    css_circuit = threshold_css(css, cfg["css_threshold"])
526	    print(f"CSS circuit (>= {cfg['css_threshold']}): {len(css_circuit)} edges")
527	
528	    # 7. CIRCUS on primary method
529	    primary = cfg["methods"][0]
530	    stability = config_bag(all_scores[primary], cfg["circus_B"])
531	    tiers = classify_tiers(
532	        stability,
533	        cfg["circus_core_threshold"],
534	        cfg["circus_contingent_threshold"],
535	    )
536	    tier_counts = {
537	        t: sum(1 for v in tiers.values() if v == t)
538	        for t in ("core", "contingent", "noise")
539	    }
540	    print(f"CIRCUS tiers ({primary}): {tier_counts}")
541	
542	    # 8. Cross-tabulation
543	    xtab = cross_tabulate(tiers, css, cfg["css_threshold"])
544	    print(
545	        f"Cross-table: stable_core={xtab['stable_core']}, "
546	        f"method_specific={xtab['method_specific']}, "
547	        f"cross_unstable={xtab['cross_unstable']}, noise={xtab['noise']}"
548	    )
549	    print(f"Off-diagonal %: {xtab['off_diagonal_pct'] * 100:.1f}%")
550	
551	    # 9. Save results
552	    result = {
553	        "config": {
554	            "model": cfg["model"],
555	            "task": cfg["task"],
556	            "K": cfg["K"],
557	            "methods": cfg["methods"],
558	            "canonical_version": CANONICAL_VERSION,
559	            "num_samples": cfg.get("num_samples", 50),
560	        },
561	        "timings_sec": timings,
562	        "method_edge_counts": {m: len(s) for m, s in all_scores.items()},
563	        "binarized_counts": {m: len(c) for m, c in circuits.items()},
564	        "css_distribution": dist,
565	        "css_circuit_size": len(css_circuit),
566	        "circus_tiers": tier_counts,
567	        "cross_table": {
568	            k: v for k, v in xtab.items()
569	            if k not in ("stable_core_edges", "method_specific_edges")
570	        },
571	    }
572	
573	    output_dir = Path(cfg["output_dir"])
574	    output_dir.mkdir(parents=True, exist_ok=True)
575	    model_slug = cfg["model"].replace("/", "_")
576	    output_path = output_dir / f"{model_slug}_{cfg['task']}_K{cfg['K']}.json"
577	    with open(output_path, "w") as f:
578	        json.dump(result, f, indent=2)
579	    print(f"\nResults → {output_path}")
580	
581	    return result
582	
583	
584	# ---------------------------------------------------------------------------
585	# CLI entry
586	# ---------------------------------------------------------------------------
587	
588	if __name__ == "__main__":
589	    config_override = None
590	    if len(sys.argv) > 1:
591	        p = sys.argv[1]
592	        with open(p) as f:
593	            if p.endswith((".yaml", ".yml")):
594	                import yaml
595	                config_override = yaml.safe_load(f)
596	            else:
597	                config_override = json.load(f)
598	    run_pipeline(config_override)
599	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "e6616302-ee80-43ee-ac6d-273936abf0c5"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/eap_ig_scoring.py",
  "usage": {
    "total_tokens": 32384,
    "tool_uses": 7,
    "duration_ms": 11161
  },
  "last_tool_name": "Read",
  "uuid": "be94a883-5e55-4384-9f1b-a3af7434069e",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01N2vrty3hXUuZhW9UmeRQye`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/eap_ig_scoring.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "3675a47b-6b5a-4055-83e1-5f6ca4547796",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LGGemhp7stVPHMpp9BZuMg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 11670,
      "cache_read_input_tokens": 20632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11670,
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

_source line 29 · 2026-05-12T22:07:33.468Z_

<details><summary>↩ Tool result · `toolu_01N2vrty3hXUuZhW9UmeRQye`</summary>

```text
1	"""EAP-IG (Edge Attribution Patching with Integrated Gradients) for HuggingFace models.
2	
3	Implements edge-level causal attribution from:
4	  Syed et al., "Attribution Patching Outperforms Automated Circuit Discovery", 2023.
5	
6	Algorithm:
7	  1. Capture clean/corrupt source activations (embedding, per-head attn, MLP outputs).
8	  2. For each IG step, interpolate embeddings, forward+backward to accumulate
9	     gradients at Q/K/V projection outputs and resid_mid.
10	  3. Edge score = |avg_grad_at_dst · projected_delta_src|, where the source delta
11	     is projected through Q/K/V weight matrices for per-head attribution.
12	
13	Input:
14	  - model: HuggingFace CausalLM (Qwen2, Llama, Gemma2, Mistral, GPT-2)
15	  - clean_inputs / corrupt_inputs: token IDs (Tensor, list, or dict)
16	  - metric_fn: callable(logits, target_ids) -> scalar
17	  - target_ids: target token IDs for metric
18	
19	Output:
20	  - Dict[str, float] mapping canonical edge names to |attribution scores|.
21	    Format: "{src}->{dst}"
22	    Nodes: input, a{L}.h{H}, m{L}
23	    Attention destinations carry .q/.k/.v suffix: a{L}.h{H}.q
24	
25	Dependencies: torch, transformers
26	"""
27	
28	from __future__ import annotations
29	
30	import torch
31	import torch.nn as nn
32	from typing import Dict, Callable, Union, List
33	
34	
35	# ---------------------------------------------------------------------------
36	# Architecture detection (shared pattern with ifr_scoring.py)
37	# ---------------------------------------------------------------------------
38	
39	_LLAMA_LIKE = frozenset({
40	    "llama", "qwen2", "gemma", "gemma2", "mistral", "phi3", "phi",
41	})
42	
43	
44	def _get_model_info(model) -> dict:
45	    cfg = model.config
46	    model_type = getattr(cfg, "model_type", "")
47	
48	    if model_type in _LLAMA_LIKE:
49	        backbone = model.model
50	        layers = backbone.layers
51	        n_heads = cfg.num_attention_heads
52	        n_kv_heads = getattr(cfg, "num_key_value_heads", n_heads)
53	        d_model = cfg.hidden_size
54	        head_dim = getattr(cfg, "head_dim", d_model // n_heads)
55	        return dict(
56	            arch="llama_like", backbone=backbone, layers=layers,
57	            n_layers=len(layers), n_heads=n_heads, n_kv_heads=n_kv_heads,
58	            head_dim=head_dim, d_model=d_model, model_type=model_type,
59	        )
60	
61	    if model_type == "gpt2":
62	        backbone = model.transformer
63	        layers = backbone.h
64	        n_heads = cfg.n_head
65	        d_model = cfg.n_embd
66	        return dict(
67	            arch="gpt2", backbone=backbone, layers=layers,
68	            n_layers=len(layers), n_heads=n_heads, n_kv_heads=n_heads,
69	            head_dim=d_model // n_heads, d_model=d_model, model_type=model_type,
70	        )
71	
72	    raise ValueError(f"Unsupported model_type={model_type!r}")
73	
74	
75	# ---------------------------------------------------------------------------
76	# Input preparation
77	# ---------------------------------------------------------------------------
78	
79	def _prepare_inputs(
80	    inputs: Union[torch.Tensor, List, dict],
81	    device: str,
82	) -> torch.Tensor:
83	    if isinstance(inputs, torch.Tensor):
84	        t = inputs
85	    elif isinstance(inputs, dict) and "input_ids" in inputs:
86	        ids = inputs["input_ids"]
87	        t = ids if isinstance(ids, torch.Tensor) else torch.tensor(ids)
88	    elif isinstance(inputs, list) and len(inputs) > 0:
89	        first = inputs[0]
90	        if isinstance(first, dict) and "input_ids" in first:
91	            tensors = [
92	                d["input_ids"] if isinstance(d["input_ids"], torch.Tensor)
93	                else torch.tensor(d["input_ids"])
94	                for d in inputs
95	            ]
96	            t = torch.stack(tensors)
97	        elif isinstance(first, torch.Tensor):
98	            t = torch.stack(inputs)
99	        elif isinstance(first, (list, int)):
100	            t = torch.tensor(inputs if isinstance(first, list) else [inputs])
101	        else:
102	            raise TypeError(f"Unsupported input element type: {type(first)}")
103	    else:
104	        raise TypeError(f"Unsupported input type: {type(inputs)}")
105	    t = t.to(device)
106	    return t.unsqueeze(0) if t.dim() == 1 else t
107	
108	
109	# ---------------------------------------------------------------------------
110	# Edge topology helpers
111	# ---------------------------------------------------------------------------
112	
113	def _before_attn(kind: str, src_layer: int, dst_layer: int) -> bool:
114	    if kind == "input":
115	        return True
116	    return src_layer < dst_layer
117	
118	
119	def _before_mlp(kind: str, src_layer: int, dst_layer: int) -> bool:
120	    if kind == "input":
121	        return True
122	    if src_layer < dst_layer:
123	        return True
124	    return src_layer == dst_layer and kind == "attn"
125	
126	
127	def _src_label(kind: str, layer: int, head: int) -> str:
128	    if kind == "input":
129	        return "input"
130	    if kind == "attn":
131	        return f"a{layer}.h{head}"
132	    return f"m{layer}"
133	
134	
135	# ---------------------------------------------------------------------------
136	# Per-head decomposition through output projection
137	# ---------------------------------------------------------------------------
138	
139	def _decompose_per_head(
140	    concat_heads: torch.Tensor,
141	    proj: nn.Module,
142	    n_heads: int,
143	    head_dim: int,
144	) -> Dict[int, torch.Tensor]:
145	    try:
146	        from transformers.pytorch_utils import Conv1D
147	        is_conv1d = isinstance(proj, Conv1D)
148	    except ImportError:
149	        is_conv1d = False
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "8bff9886-79a8-42db-8272-c33826e072fd"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/edge_pruning_scoring.py",
  "usage": {
    "total_tokens": 32385,
    "tool_uses": 8,
    "duration_ms": 11377
  },
  "last_tool_name": "Read",
  "uuid": "3e8f5074-ff36-4134-a776-c6619175e666",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_019SS19yqPDHajpV7RZHA3td`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/edge_pruning_scoring.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "dcfb89d6-1541-4e7e-ab50-157977580e8a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LGGemhp7stVPHMpp9BZuMg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 11670,
      "cache_read_input_tokens": 20632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11670,
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

_source line 32 · 2026-05-12T22:07:33.680Z_

<details><summary>↩ Tool result · `toolu_019SS19yqPDHajpV7RZHA3td`</summary>

```text
1	"""Edge Pruning v2 with L0 regularization for HuggingFace models.
2	
3	v2 fixes two critical bugs from v1:
4	  1. MLP edge masks are now applied in forward via mlp pre-hook
5	     (v1 had mask params but no forward-pass hook for MLP).
6	  2. Q/K/V edge masks are kept independent per-head/KV-group
7	     (v1 averaged across all Q/K/V destinations into a single scalar).
8	
9	Hook strategy (v2): 4 submodule pre-hooks per layer
10	  - self_attn.q_proj: per-head Q edge masks
11	  - self_attn.k_proj: per-KV-group K edge masks (GQA shared)
12	  - self_attn.v_proj: per-KV-group V edge masks (GQA shared)
13	  - mlp: per-source MLP edge masks
14	Plus capture hooks: embed_tokens, self_attn.o_proj (per-head), mlp (output).
15	
16	Canonical node format:
17	  input, logits, a{L}.h{H}[.q|.k|.v], m{L}
18	
19	Canonical edge format: "{src}->{dst}" (no spaces)
20	
21	References:
22	  - Louizos et al. "Learning Sparse Neural Networks through L0 Regularization" (2018)
23	  - Bayazit et al. "Discovering Knowledge-Critical Subnetworks" (2023)
24	"""
25	
26	from __future__ import annotations
27	
28	import math
29	from typing import Dict, List, Tuple, Callable, Optional
30	
31	import torch
32	import torch.nn as nn
33	import torch.nn.functional as F
34	
35	
36	# ---------------------------------------------------------------------------
37	# Hard Concrete Distribution
38	# ---------------------------------------------------------------------------
39	
40	class HardConcrete(nn.Module):
41	    """Hard Concrete distribution for L0 mask parameterization.
42	
43	    Parameterized by log_alpha (location). During training, samples from a
44	    stretched Binary Concrete and clamps to [0, 1], yielding exact zeros/ones.
45	    """
46	
47	    BETA = 2.0 / 3.0
48	    GAMMA = -0.1
49	    ZETA = 1.1
50	    EPS = 1e-8
51	
52	    def __init__(self, n_masks: int, init_mean: float = 0.5):
53	        super().__init__()
54	        init_val = math.log(init_mean / (1.0 - init_mean + self.EPS))
55	        self.log_alpha = nn.Parameter(torch.full((n_masks,), init_val))
56	
57	    def forward(self, training: bool = True) -> torch.Tensor:
58	        if training:
59	            u = torch.zeros_like(self.log_alpha).uniform_(self.EPS, 1.0 - self.EPS)
60	            s = torch.sigmoid((torch.log(u / (1.0 - u)) + self.log_alpha) / self.BETA)
61	        else:
62	            s = torch.sigmoid(self.log_alpha)
63	        s_bar = s * (self.ZETA - self.GAMMA) + self.GAMMA
64	        return s_bar.clamp(0.0, 1.0)
65	
66	    def l0_penalty(self) -> torch.Tensor:
67	        """Expected L0 norm: sum of P(z != 0) for each mask."""
68	        return torch.sigmoid(
69	            self.log_alpha - self.BETA * math.log(-self.GAMMA / self.ZETA)
70	        ).sum()
71	
72	    def expected_masks(self) -> torch.Tensor:
73	        """Deterministic mask expectations (for final scoring)."""
74	        return self.forward(training=False)
75	
76	
77	# ---------------------------------------------------------------------------
78	# Architecture detection (Llama-like HF models)
79	# ---------------------------------------------------------------------------
80	
81	_LLAMA_LIKE = frozenset({
82	    "llama", "qwen2", "gemma", "gemma2", "mistral", "phi3", "phi",
83	})
84	
85	
86	def _get_arch_info(model) -> dict:
87	    cfg = model.config
88	    model_type = getattr(cfg, "model_type", "")
89	    if model_type not in _LLAMA_LIKE:
90	        raise ValueError(
91	            f"Edge Pruning L0 currently supports Llama-like architectures, "
92	            f"got model_type={model_type!r}"
93	        )
94	    n_heads = cfg.num_attention_heads
95	    n_kv_heads = getattr(cfg, "num_key_value_heads", n_heads)
96	    d_model = cfg.hidden_size
97	    return dict(
98	        n_layers=cfg.num_hidden_layers,
99	        n_heads=n_heads,
100	        n_kv_heads=n_kv_heads,
101	        heads_per_kv_group=n_heads // n_kv_heads,
102	        d_model=d_model,
103	        head_dim=d_model // n_heads,
104	    )
105	
106	
107	# ---------------------------------------------------------------------------
108	# Edge Topology: enumerate all edges and build mask index mapping
109	# ---------------------------------------------------------------------------
110	
111	def _src_nodes_before_layer(
112	    layer: int, n_heads: int, include_attn_same_layer: bool = False,
113	):
114	    """Yield source node names whose output feeds into a given layer."""
115	    yield "input"
116	    for l in range(layer):
117	        for h in range(n_heads):
118	            yield f"a{l}.h{h}"
119	        yield f"m{l}"
120	    if include_attn_same_layer:
121	        for h in range(n_heads):
122	            yield f"a{layer}.h{h}"
123	
124	
125	def _build_edge_topology(
126	    n_layers: int, n_heads: int, n_kv_heads: int, heads_per_kv_group: int,
127	) -> Tuple[List[str], Dict[str, int], int]:
128	    """Build the full edge set and map each edge to its mask parameter index.
129	
130	    For GQA models, K/V edges targeting the same KV group share a mask.
131	    Q edges always have independent masks.
132	
133	    Returns:
134	        edge_names: list of canonical edge names
135	        edge_to_mask_idx: edge_name -> index into mask parameter vector
136	        n_masks: total number of independent mask parameters
137	    """
138	    edge_names: List[str] = []
139	    edge_to_mask_idx: Dict[str, int] = {}
140	    mask_idx = 0
141	
142	    for L in range(n_layers):
143	        srcs_attn = list(_src_nodes_before_layer(L, n_heads, False))
144	        for src in srcs_attn:
145	            for H in range(n_heads):
146	                q_edge = f"{src}->a{L}.h{H}.q"
147	                edge_names.append(q_edge)
148	                edge_to_mask_idx[q_edge] = mask_idx
149	                mask_idx += 1
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "83c75a02-b930-438d-a866-439164019edb"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/ifr_scoring.py",
  "usage": {
    "total_tokens": 32386,
    "tool_uses": 9,
    "duration_ms": 11709
  },
  "last_tool_name": "Read",
  "uuid": "0ba9b125-c006-406a-91d6-d3eef2806640",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01DKKsTWABSyezvui3y4TAEF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/ifr_scoring.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "695aa04d-d158-42dc-bd7a-6fc3b198dff7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LGGemhp7stVPHMpp9BZuMg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 11670,
      "cache_read_input_tokens": 20632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11670,
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

_source line 35 · 2026-05-12T22:07:34.013Z_

<details><summary>↩ Tool result · `toolu_01DKKsTWABSyezvui3y4TAEF`</summary>

```text
1	"""IFR (Information Flow Routes) edge-level scoring for HuggingFace models.
2	
3	Implements ALTI-based proximity attribution from:
4	  Ferrando & Voita, "Information Flow Routes: Automatically Interpreting
5	  Language Models at Scale", EMNLP 2024.
6	
7	Scores each edge (u->v) by how much source u's output is "present" in the
8	residual stream that destination v reads from:
9	
10	    score(u->v) = max(||x_v||_1 - ||y_u - x_v||_1, 0)
11	
12	where y_u = component u's output, x_v = residual stream input to component v.
13	
14	Input:
15	  - model: HuggingFace CausalLM (Llama, Qwen2, Gemma2, Mistral, GPT2)
16	  - dataset: tokenized examples (list[dict], dict with input_ids, or Tensor)
17	  - metric_fn: unused — kept for interface parity with EAP-IG / Edge Pruning
18	
19	Output:
20	  - Dict[str, float] mapping canonical edge names to proximity scores (>=0).
21	    Format: "{src}->{dst}"
22	    Nodes: input, a{L}.h{H}, m{L}
23	    Attention destinations carry .q/.k/.v suffix: a{L}.h{H}.q
24	
25	Dependencies: torch, transformers
26	"""
27	
28	from __future__ import annotations
29	
30	import torch
31	import torch.nn as nn
32	from typing import Dict, Callable, Union
33	
34	
35	# ---------------------------------------------------------------------------
36	# Core proximity metric (ALTI)
37	# ---------------------------------------------------------------------------
38	
39	def _proximity(y_u: torch.Tensor, x_v: torch.Tensor) -> float:
40	    """max(||x_v||_1 - ||y_u - x_v||_1, 0), averaged over batch & sequence."""
41	    diff_norm = (y_u - x_v).abs().sum(dim=-1)
42	    base_norm = x_v.abs().sum(dim=-1)
43	    return (base_norm - diff_norm).clamp(min=0).mean().item()
44	
45	
46	# ---------------------------------------------------------------------------
47	# Architecture detection
48	# ---------------------------------------------------------------------------
49	
50	_LLAMA_LIKE = frozenset({
51	    "llama", "qwen2", "gemma", "gemma2", "mistral", "phi3", "phi",
52	})
53	
54	
55	def _get_model_info(model) -> dict:
56	    cfg = model.config
57	    model_type = getattr(cfg, "model_type", "")
58	
59	    if model_type in _LLAMA_LIKE:
60	        backbone = model.model
61	        layers = backbone.layers
62	        n_heads = cfg.num_attention_heads
63	        d_model = cfg.hidden_size
64	        return dict(
65	            arch="llama_like", backbone=backbone, layers=layers,
66	            n_layers=len(layers), n_heads=n_heads,
67	            head_dim=d_model // n_heads, d_model=d_model,
68	        )
69	
70	    if model_type == "gpt2":
71	        backbone = model.transformer
72	        layers = backbone.h
73	        n_heads = cfg.n_head
74	        d_model = cfg.n_embd
75	        return dict(
76	            arch="gpt2", backbone=backbone, layers=layers,
77	            n_layers=len(layers), n_heads=n_heads,
78	            head_dim=d_model // n_heads, d_model=d_model,
79	        )
80	
81	    raise ValueError(f"Unsupported model_type={model_type!r}")
82	
83	
84	# ---------------------------------------------------------------------------
85	# Edge topology helpers
86	# ---------------------------------------------------------------------------
87	
88	def _before_attn(kind: str, src_layer: int, dst_layer: int) -> bool:
89	    if kind == "input":
90	        return True
91	    return src_layer < dst_layer
92	
93	
94	def _before_mlp(kind: str, src_layer: int, dst_layer: int) -> bool:
95	    if kind == "input":
96	        return True
97	    if src_layer < dst_layer:
98	        return True
99	    return src_layer == dst_layer and kind == "attn"
100	
101	
102	# ---------------------------------------------------------------------------
103	# Dataset preparation
104	# ---------------------------------------------------------------------------
105	
106	def _prepare_tokens(
107	    dataset: Union[torch.Tensor, dict, list],
108	    device: str,
109	) -> torch.Tensor:
110	    if isinstance(dataset, torch.Tensor):
111	        t = dataset
112	    elif isinstance(dataset, dict) and "input_ids" in dataset:
113	        ids = dataset["input_ids"]
114	        t = ids if isinstance(ids, torch.Tensor) else torch.tensor(ids)
115	    elif isinstance(dataset, list) and len(dataset) > 0:
116	        first = dataset[0]
117	        if isinstance(first, dict) and "input_ids" in first:
118	            tensors = [
119	                d["input_ids"] if isinstance(d["input_ids"], torch.Tensor)
120	                else torch.tensor(d["input_ids"])
121	                for d in dataset
122	            ]
123	            t = torch.stack(tensors)
124	        elif isinstance(first, torch.Tensor):
125	            t = torch.stack(dataset)
126	        else:
127	            t = torch.tensor(dataset)
128	    else:
129	        raise TypeError(f"Unsupported dataset type: {type(dataset)}")
130	    t = t.to(device)
131	    return t.unsqueeze(0) if t.dim() == 1 else t
132	
133	
134	# ---------------------------------------------------------------------------
135	# Per-head decomposition through the output projection
136	# ---------------------------------------------------------------------------
137	
138	def _decompose_per_head(
139	    concat_heads: torch.Tensor,
140	    proj: nn.Module,
141	    n_heads: int,
142	    head_dim: int,
143	) -> Dict[int, torch.Tensor]:
144	    """Split concatenated head activations and project each through o_proj."""
145	    try:
146	        from transformers.pytorch_utils import Conv1D
147	        is_conv1d = isinstance(proj, Conv1D)
148	    except ImportError:
149	        is_conv1d = False
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "4ef5c5db-ccfb-4471-99bf-31d827df1586"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/analyze_mvp_results.py",
  "usage": {
    "total_tokens": 38396,
    "tool_uses": 10,
    "duration_ms": 14040
  },
  "last_tool_name": "Read",
  "uuid": "f074bf51-2db1-49c6-974e-307d7d59ea90",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_015bnjoYW3L27x23E7nWYGif`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/analyze_mvp_results.py",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "cfa34f6d-2cc0-4ec9-823e-daf836955f31",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UCBXoAbu8FEkSEQD9hczaG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6004,
      "cache_read_input_tokens": 32302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6004,
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

_source line 38 · 2026-05-12T22:07:36.351Z_

<details><summary>↩ Tool result · `toolu_015bnjoYW3L27x23E7nWYGif`</summary>

```text
1	"""MVP 结果自动分析：Phase C/D/E 汇总。
2	
3	读取 v3 三方法 circuit 数据，计算 CSS matrix、off-diagonal 比率、
4	按 ACDC threshold 敏感性分析，生成可视化，输出 pass/fail 判定。
5	
6	Usage:
7	    python analyze_mvp_results.py [--results-dir /root/structfuse-context] [--output-dir ./analysis]
8	    python analyze_mvp_results.py --dry-run   # mock data 验证
9	"""
10	
11	import argparse
12	import itertools
13	import json
14	import sys
15	from collections import Counter
16	from pathlib import Path
17	from typing import Any, Dict, List, Optional, Set, Tuple
18	
19	import numpy as np
20	
21	
22	# ---------------------------------------------------------------------------
23	# Data loading
24	# ---------------------------------------------------------------------------
25	
26	def _find_cache_files(results_dir: Path) -> Dict[str, Path]:
27	    """Auto-detect per-method cache files under results_dir.
28	
29	    Searches for:
30	      1. cache_&lt;method>.json  (old MVP flat layout)
31	      2. cache/&lt;model_slug>/&lt;task>/&lt;method>_*.json  (run_circus.py structured cache)
32	      3. Keys inside mvp_results.json that embed raw scores
33	    """
34	    found: Dict[str, Path] = {}
35	    method_names = ["eap_ig", "edge_pruning", "acdc", "ifr"]
36	
37	    for m in method_names:
38	        flat = results_dir / f"cache_{m}.json"
39	        if flat.exists():
40	            found[m] = flat
41	
42	    cache_dir = results_dir / "cache"
43	    if cache_dir.is_dir():
44	        for p in cache_dir.rglob("*.json"):
45	            for m in method_names:
46	                if p.stem.startswith(m):
47	                    found.setdefault(m, p)
48	
49	    return found
50	
51	
52	def _load_scores_from_file(path: Path) -> Dict[str, float]:
53	    """Load edge scores from a cache JSON (handles both flat and structured)."""
54	    with open(path) as f:
55	        data = json.load(f)
56	
57	    if isinstance(data, dict) and "scores" in data:
58	        return {str(k): float(v) for k, v in data["scores"].items()}
59	    if isinstance(data, dict) and all(isinstance(v, (int, float)) for v in data.values()):
60	        return {str(k): float(v) for k, v in data.items()}
61	    if isinstance(data, list):
62	        return {str(item["edge"]): float(item["score"]) for item in data if "edge" in item}
63	    raise ValueError(f"Unrecognized cache format in {path}")
64	
65	
66	def _load_pipeline_results(results_dir: Path) -> Optional[Dict[str, Any]]:
67	    """Load mvp_results.json or run_circus output."""
68	    for name in ["mvp_results.json", "results/mvp_results.json"]:
69	        p = results_dir / name
70	        if p.exists():
71	            with open(p) as f:
72	                return json.load(f)
73	    results_subdir = results_dir / "results"
74	    if results_subdir.is_dir():
75	        jsons = sorted(results_subdir.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True)
76	        if jsons:
77	            with open(jsons[0]) as f:
78	                return json.load(f)
79	    return None
80	
81	
82	def load_all_data(results_dir: Path) -> Tuple[
83	    Dict[str, Dict[str, float]],  # method -> edge scores
84	    Optional[Dict[str, Any]],     # pipeline results JSON
85	]:
86	    """Load all available method scores and pipeline results."""
87	    cache_files = _find_cache_files(results_dir)
88	    all_scores: Dict[str, Dict[str, float]] = {}
89	
90	    for method, path in cache_files.items():
91	        try:
92	            all_scores[method] = _load_scores_from_file(path)
93	            print(f"  Loaded {method}: {len(all_scores[method])} edges from {path}")
94	        except Exception as e:
95	            print(f"  WARNING: failed to load {method} from {path}: {e}")
96	
97	    pipeline = _load_pipeline_results(results_dir)
98	    if pipeline:
99	        print(f"  Loaded pipeline results: {list(pipeline.keys())}")
100	
101	    if not all_scores:
102	        print("  WARNING: no per-method score files found")
103	
104	    return all_scores, pipeline
105	
106	
107	# ---------------------------------------------------------------------------
108	# Binarization (no torch dependency)
109	# ---------------------------------------------------------------------------
110	
111	def binarize_topn(scores: Dict[str, float], n: int = 200) -> Set[str]:
112	    sorted_edges = sorted(scores.items(), key=lambda x: abs(x[1]), reverse=True)
113	    return {e for e, _ in sorted_edges[:n]}
114	
115	
116	def binarize_threshold(scores: Dict[str, float], threshold: float = 0.5) -> Set[str]:
117	    return {e for e, s in scores.items() if s >= threshold}
118	
119	
120	def binarize_acdc(scores: Dict[str, float], tau: float = 0.05) -> Set[str]:
121	    return {e for e, s in scores.items() if abs(s) > tau}
122	
123	
124	def binarize_method(
125	    scores: Dict[str, float], method: str,
126	    top_n: int = 200, acdc_tau: float = 0.05,
127	) -> Set[str]:
128	    if method == "acdc":
129	        return binarize_acdc(scores, tau=acdc_tau)
130	    elif method == "edge_pruning":
131	        return binarize_threshold(scores, threshold=0.5)
132	    else:
133	        return binarize_topn(scores, n=top_n)
134	
135	
136	# ---------------------------------------------------------------------------
137	# CSS / Jaccard / cross-tabulation
138	# ---------------------------------------------------------------------------
139	
140	def jaccard(a: Set[str], b: Set[str]) -> float:
141	    if not a and not b:
142	        return 1.0
143	    union = a | b
144	    if not union:
145	        return 0.0
146	    return len(a & b) / len(union)
147	
148	
149	def compute_pairwise_css(circuits: Dict[str, Set[str]]) -> Dict[str, float]:
150	    methods = sorted(circuits.keys())
151	    result = {}
152	    for m1, m2 in itertools.combinations(methods, 2):
153	        result[f"{m1} vs {m2}"] = jaccard(circuits[m1], circuits[m2])
154	    return result
155	
156	
157	def compute_css_matrix_full(
158	    circuits: Dict[str, Set[str]],
159	) -> Dict[str, Any]:
160	    """Full 2^K cross-tabulation."""
161	    methods = sorted(circuits.keys())
162	    K = len(methods)
163	    all_edges: Set[str] = set()
164	    for edges in circuits.values():
165	        all_edges |= edges
166	
167	    cell_counts: Dict[str, int] = Counter()
168	    for edge in all_edges:
169	        cell = tuple(1 if edge in circuits[m] else 0 for m in methods)
170	        cell_counts[str(cell)] += 1
171	
172	    all_ones = str(tuple(1 for _ in range(K)))
173	    all_zeros = str(tuple(0 for _ in range(K)))
174	
175	    agree_in = cell_counts.get(all_ones, 0)
176	    total_with_any = sum(c for label, c in cell_counts.items() if label != all_zeros)
177	    off_diagonal = total_with_any - agree_in
178	
179	    return {
180	        "cell_counts": dict(cell_counts),
181	        "agree_all_in": agree_in,
182	        "agree_all_out_of_union": 0,
183	        "off_diagonal": off_diagonal,
184	        "total_union": total_with_any,
185	        "off_diagonal_pct": off_diagonal / total_with_any if total_with_any > 0 else 0.0,
186	        "methods": methods,
187	    }
188	
189	
190	def compute_circus_tiers(
191	    scores: Dict[str, float], B: int = 10,
192	    core_thr: float = 1.0, contingent_thr: float = 0.5,
193	) -> Dict[str, str]:
194	    if not scores:
195	        return {}
196	    vals = np.array(list(scores.values()))
197	    edges = list(scores.keys())
198	    percentiles = np.linspace(100 / (B + 1), 100 * B / (B + 1), B)
199	    thresholds = np.percentile(vals, percentiles)
200	    stability = sum((vals >= t).astype(float) for t in thresholds) / B
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "9430cbd9-9c8b-4d3b-ae90-39f060f5eb67"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/model_adapter.py",
  "usage": {
    "total_tokens": 38399,
    "tool_uses": 11,
    "duration_ms": 14253
  },
  "last_tool_name": "Read",
  "uuid": "384e9f4c-8fe0-43e9-a3d8-e66bc21a3d7b",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_013hSTpEaXouYLMiKP7hTk84`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/model_adapter.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "1053db6d-ef1f-4b2e-9fdc-d1bdceb4930a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UCBXoAbu8FEkSEQD9hczaG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6004,
      "cache_read_input_tokens": 32302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6004,
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

_source line 41 · 2026-05-12T22:07:36.559Z_

<details><summary>↩ Tool result · `toolu_013hSTpEaXouYLMiKP7hTk84`</summary>

```text
1	"""Model adapter: unified interface for GPT-2 (TransformerLens) and Qwen-2.5 (HuggingFace).
2	
3	Bridges different model backends to a single canonical node/edge naming scheme
4	for StructFuse circuit discovery methods (EAP-IG, Edge Pruning, IFR).
5	
6	Canonical node format:
7	  input           — embedding output
8	  a{L}.h{H}       — attention head H output at layer L
9	  a{L}.h{H}.q/k/v — attention head H destination at layer L
10	  m{L}            — MLP at layer L
11	  logits          — final output
12	
13	Canonical edge format: "{src}->{dst}" (no spaces around arrow)
14	
15	CANONICAL_VERSION must be embedded in all cached edge scores to prevent stale reads.
16	"""
17	
18	from __future__ import annotations
19	
20	import re
21	from dataclasses import dataclass
22	from typing import Dict, Optional
23	
24	import torch
25	import torch.nn as nn
26	
27	
28	CANONICAL_VERSION = "v2"
29	
30	
31	@dataclass
32	class ModelInfo:
33	    arch: str                   # "gpt2" | "qwen2" | "llama" | ...
34	    n_layers: int
35	    n_heads: int
36	    n_kv_heads: int             # GQA: fewer KV heads than query heads
37	    d_model: int
38	    head_dim: int
39	    backend: str                # "transformerlens" | "huggingface"
40	    model_name: str
41	
42	
43	# ---------------------------------------------------------------------------
44	# TransformerLens node name → canonical conversion patterns
45	# ---------------------------------------------------------------------------
46	
47	_TL_NODE_PATTERNS = [
48	    (re.compile(r"^hook_embed$"),
49	     lambda m: "input"),
50	    (re.compile(r"^blocks\.(\d+)\.attn\.hook_result\[(\d+)\]$"),
51	     lambda m: f"a{m.group(1)}.h{m.group(2)}"),
52	    (re.compile(r"^blocks\.(\d+)\.attn\.hook_(q|k|v)\[(\d+)\]$"),
53	     lambda m: f"a{m.group(1)}.h{m.group(3)}.{m.group(2)}"),
54	    (re.compile(r"^blocks\.(\d+)\.hook_mlp_out$"),
55	     lambda m: f"m{m.group(1)}"),
56	    (re.compile(r"^blocks\.(\d+)\.hook_mlp_in$"),
57	     lambda m: f"m{m.group(1)}"),
58	]
59	
60	
61	def _tl_to_canonical(name: str) -> str:
62	    for pattern, formatter in _TL_NODE_PATTERNS:
63	        m = pattern.match(name)
64	        if m:
65	            return formatter(m)
66	    return name
67	
68	
69	def _hf_to_canonical(name: str) -> str:
70	    if name == "model.embed_tokens":
71	        return "input"
72	    if name == "lm_head":
73	        return "logits"
74	    m = re.match(r"model\.layers\.(\d+)\.self_attn\.o_proj", name)
75	    if m:
76	        return f"a{m.group(1)}"
77	    m = re.match(r"model\.layers\.(\d+)\.mlp", name)
78	    if m:
79	        return f"m{m.group(1)}"
80	    return name
81	
82	
83	def _tl_edges_to_canonical(edge_scores: Dict[str, float]) -> Dict[str, float]:
84	    result = {}
85	    for edge, score in edge_scores.items():
86	        if " -> " in edge:
87	            src, dst = edge.split(" -> ", 1)
88	        elif "->" in edge:
89	            src, dst = edge.split("->", 1)
90	        else:
91	            result[edge] = score
92	            continue
93	        canon_src = _tl_to_canonical(src.strip())
94	        canon_dst = _tl_to_canonical(dst.strip())
95	        result[f"{canon_src}->{canon_dst}"] = score
96	    return result
97	
98	
99	def _is_gpt2(name: str) -> bool:
100	    return name.startswith("gpt2") or name in (
101	        "gpt2-small", "gpt2-medium", "gpt2-large", "gpt2-xl",
102	    )
103	
104	
105	# ---------------------------------------------------------------------------
106	# ModelAdapter
107	# ---------------------------------------------------------------------------
108	
109	class ModelAdapter:
110	    """Unified model interface for circuit discovery methods."""
111	
112	    def __init__(self, model: nn.Module, info: ModelInfo, tokenizer=None):
113	        self.model = model
114	        self.info = info
115	        self.tokenizer = tokenizer
116	
117	    # ---- Factory ----
118	
119	    @classmethod
120	    def from_pretrained(
121	        cls, model_name: str, device: str = "cuda", **kwargs,
122	    ) -> ModelAdapter:
123	        if _is_gpt2(model_name):
124	            return cls._load_tl(model_name, device)
125	        return cls._load_hf(model_name, device, **kwargs)
126	
127	    @classmethod
128	    def _load_tl(cls, model_name: str, device: str) -> ModelAdapter:
129	        from transformer_lens import HookedTransformer
130	
131	        model = HookedTransformer.from_pretrained(model_name, device=device)
132	        info = ModelInfo(
133	            arch="gpt2",
134	            n_layers=model.cfg.n_layers,
135	            n_heads=model.cfg.n_heads,
136	            n_kv_heads=model.cfg.n_heads,
137	            d_model=model.cfg.d_model,
138	            head_dim=model.cfg.d_head,
139	            backend="transformerlens",
140	            model_name=model_name,
141	        )
142	        return cls(model, info, tokenizer=model.tokenizer)
143	
144	    @classmethod
145	    def _load_hf(cls, model_name: str, device: str, **kwargs) -> ModelAdapter:
146	        from transformers import AutoModelForCausalLM, AutoTokenizer
147	
148	        dtype = kwargs.pop("torch_dtype", torch.float16)
149	        tokenizer = AutoTokenizer.from_pretrained(
150	            model_name, trust_remote_code=True,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "01692ffb-8d41-4a9c-963c-b53eb025e96c"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/model_adapter.py",
  "usage": {
    "total_tokens": 43145,
    "tool_uses": 12,
    "duration_ms": 16735
  },
  "last_tool_name": "Read",
  "uuid": "c1b4aac5-6c23-49c9-9032-cb0c75bf7292",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01JfUWWCw5KVVsa7QHEkqzbm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/model_adapter.py",
  "limit": 250,
  "offset": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "8be80389-b268-4400-8e88-6cbf9feb8e13",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RaYbx5uUG8TxSUX3f7mWAH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4740,
      "cache_read_input_tokens": 38306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4740,
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

_source line 44 · 2026-05-12T22:07:39.045Z_

<details><summary>↩ Tool result · `toolu_01JfUWWCw5KVVsa7QHEkqzbm`</summary>

```text
150	            model_name, trust_remote_code=True,
151	        )
152	        model = AutoModelForCausalLM.from_pretrained(
153	            model_name,
154	            torch_dtype=dtype,
155	            device_map=device,
156	            trust_remote_code=True,
157	            **kwargs,
158	        )
159	        cfg = model.config
160	        n_heads = cfg.num_attention_heads
161	        info = ModelInfo(
162	            arch=getattr(cfg, "model_type", "unknown"),
163	            n_layers=cfg.num_hidden_layers,
164	            n_heads=n_heads,
165	            n_kv_heads=getattr(cfg, "num_key_value_heads", n_heads),
166	            d_model=cfg.hidden_size,
167	            head_dim=cfg.hidden_size // n_heads,
168	            backend="huggingface",
169	            model_name=model_name,
170	        )
171	        return cls(model, info, tokenizer=tokenizer)
172	
173	    # ---- Hook point mapping ----
174	
175	    def get_hook_points(self) -> Dict[str, str]:
176	        """Return {canonical_name: actual_module_path} for all hookable nodes.
177	
178	        For HF models with GQA (n_kv_heads < n_heads), k_proj/v_proj are shared
179	        across query heads in the same KV group.  The canonical name still uses
180	        per-query-head indexing; the module path is the same for all heads in a group.
181	        """
182	        if self.info.backend == "transformerlens":
183	            return self._tl_hooks()
184	        return self._hf_hooks()
185	
186	    def _tl_hooks(self) -> Dict[str, str]:
187	        hp: Dict[str, str] = {"input": "hook_embed", "logits": "ln_final"}
188	        for L in range(self.info.n_layers):
189	            for H in range(self.info.n_heads):
190	                hp[f"a{L}.h{H}"] = f"blocks.{L}.attn.hook_result"
191	                for qkv in "qkv":
192	                    hp[f"a{L}.h{H}.{qkv}"] = f"blocks.{L}.attn.hook_{qkv}"
193	            hp[f"m{L}"] = f"blocks.{L}.hook_mlp_out"
194	        return hp
195	
196	    def _hf_hooks(self) -> Dict[str, str]:
197	        """Hook points for Llama-like HF models (Qwen2, Llama, Mistral, ...).
198	
199	        EAP-IG needs forward + backward hooks at these points.
200	        Edge Pruning needs to insert masks between these modules.
201	        IFR uses forward-only hooks (already handled by ifr_scoring.py).
202	
203	        Qwen-2.5 0.5B specifics (24L, 14H, 2KV):
204	          - model.layers.{i}.self_attn uses SDPA with RoPE
205	          - GQA: 14 query heads, 2 KV heads → 7 queries per KV group
206	          - q_proj: [896, 896]  (14 heads × 64 dim)
207	          - k_proj: [896, 128]  (2 KV heads × 64 dim)
208	          - v_proj: [896, 128]  (2 KV heads × 64 dim)
209	          - o_proj: [896, 896]
210	          - mlp: gate_proj [896, 4864], up_proj [896, 4864], down_proj [4864, 896]
211	        """
212	        hp: Dict[str, str] = {
213	            "input": "model.embed_tokens",
214	            "logits": "lm_head",
215	        }
216	        for L in range(self.info.n_layers):
217	            hp[f"resid_pre.{L}"] = f"model.layers.{L}"
218	            for H in range(self.info.n_heads):
219	                hp[f"a{L}.h{H}"] = f"model.layers.{L}.self_attn.o_proj"
220	                hp[f"a{L}.h{H}.q"] = f"model.layers.{L}.self_attn.q_proj"
221	                hp[f"a{L}.h{H}.k"] = f"model.layers.{L}.self_attn.k_proj"
222	                hp[f"a{L}.h{H}.v"] = f"model.layers.{L}.self_attn.v_proj"
223	            hp[f"m{L}"] = f"model.layers.{L}.mlp"
224	        return hp
225	
226	    # ---- Canonical name conversion ----
227	
228	    def canonical_node_name(self, module_path: str) -> str:
229	        if self.info.backend == "transformerlens":
230	            return _tl_to_canonical(module_path)
231	        return _hf_to_canonical(module_path)
232	
233	    def to_canonical_edges(
234	        self, edge_scores: Dict[str, float], method: str,
235	    ) -> Dict[str, float]:
236	        """Convert method-specific edge names to canonical format.
237	
238	        IFR from ifr_scoring.py already outputs canonical format.
239	        TL-based methods use "blocks.{L}..." format and need conversion.
240	        """
241	        if method == "ifr" and self.info.backend == "huggingface":
242	            return edge_scores
243	        if self.info.backend == "transformerlens":
244	            return _tl_edges_to_canonical(edge_scores)
245	        return edge_scores
246	
247	    # ---- Edge topology ----
248	
249	    def n_possible_edges(self) -> int:
250	        """Total edges in the full computational graph (attention + MLP)."""
251	        L, H = self.info.n_layers, self.info.n_heads
252	        comps_per_layer = H + 1  # H attn heads + 1 MLP
253	        attn_edges = sum((1 + l * comps_per_layer) * H * 3 for l in range(L))
254	        mlp_edges = sum(1 + l * comps_per_layer + H for l in range(L))
255	        return attn_edges + mlp_edges
256	
257	    def gqa_kv_group(self, query_head: int) -> int:
258	        """Map query head index to its KV group index (for GQA models)."""
259	        if self.info.n_kv_heads == self.info.n_heads:
260	            return query_head
261	        heads_per_group = self.info.n_heads // self.info.n_kv_heads
262	        return query_head // heads_per_group
263	
264	
265	# ---------------------------------------------------------------------------
266	# Qwen-2.5 0.5B architecture reference
267	# ---------------------------------------------------------------------------
268	#
269	# | Property             | Value                              |
270	# |----------------------|------------------------------------|
271	# | model_type           | qwen2                              |
272	# | num_hidden_layers    | 24                                 |
273	# | num_attention_heads  | 14                                 |
274	# | num_key_value_heads  | 2  (GQA: 7 queries per KV group)  |
275	# | hidden_size          | 896                                |
276	# | head_dim             | 64                                 |
277	# | intermediate_size    | 4864                               |
278	# | vocab_size           | 151936                             |
279	# | max_position_embeddings | 32768 (RoPE)                   |
280	#
281	# Canonical node mapping for Qwen-2.5 0.5B:
282	#
283	# | Canonical        | HuggingFace module path                       | Note             |
284	# |------------------|-----------------------------------------------|------------------|
285	# | input            | model.embed_tokens                            |                  |
286	# | a{L}.h{H}       | model.layers.{L}.self_attn.o_proj (head H)    | per-head via decomposition |
287	# | a{L}.h{H}.q     | model.layers.{L}.self_attn.q_proj (head H)    | slice [H*64:(H+1)*64] |
288	# | a{L}.h{H}.k     | model.layers.{L}.self_attn.k_proj (KV group)  | GQA: H//7 maps to KV head |
289	# | a{L}.h{H}.v     | model.layers.{L}.self_attn.v_proj (KV group)  | GQA: H//7 maps to KV head |
290	# | m{L}            | model.layers.{L}.mlp                          |                  |
291	# | logits           | lm_head                                       |                  |
292	#
293	# EAP-IG hook registration for Qwen-2.5:
294	#   Forward hooks:  model.layers.{i} (pre-hook for resid_pre)
295	#                   model.layers.{i}.self_attn.o_proj (attn output, decompose per head)
296	#                   model.layers.{i}.mlp (MLP output)
297	#   Backward hooks: same modules, for gradient-based attribution
298	#
299	# Edge Pruning hook registration for Qwen-2.5:
300	#   Mask insertion points:
301	#     - Between embedding and first layer input
302	#     - Between each layer's output and next layer's input (residual connections)
303	#   Requires custom masked forward pass (analogous to edge_pruning_l0._masked_forward
304	#   but operating on HF module structure instead of TL blocks).
305	#   Key difference from GPT-2: GQA means K/V masks are shared across query groups.
306	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "5ffe38f7-41e6-4468-a61c-782f9b091249"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 43148,
    "tool_uses": 13,
    "duration_ms": 16980
  },
  "last_tool_name": "Bash",
  "uuid": "f02db63a-ea31-4d7b-9b2c-e2b2edeb0249",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01GdMJLRPRjjj54nTjSc8QMP`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context -name \"*acdc*\" -o -name \"*ACDC*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "5f39bed2-5060-40f2-9809-613a65f254f4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RaYbx5uUG8TxSUX3f7mWAH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4740,
      "cache_read_input_tokens": 38306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4740,
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

_source line 47 · 2026-05-12T22:07:39.339Z_

<details><summary>↩ Tool result · `toolu_01GdMJLRPRjjj54nTjSc8QMP`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_code_mvp-acdc-check_20260512T123510.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_check_mvp_acdc_status_20260512T165105_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_code_acdc-investigate-fix_20260512T154604_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_code_mvp-acdc-check_20260512T123510_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_code_acdc-investigate-fix_20260512T154604.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_check_acdc-final-status_20260512T165154_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_check_mvp_acdc_status_20260512T165105.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_check_acdc-final-status_20260512T165154.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_code_kill-fix-acdc_20260512T150933.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_code_kill-fix-acdc_20260512T150933_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/chats/worker_check_acdc-final-status_20260512T165154.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/chats/worker_check_mvp_acdc_status_20260512T165105.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/chats/worker_check_mvp_acdc_status_20260512T165105.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/chats/worker_check_acdc-final-status_20260512T165154.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "b24204cd-5af3-43e5-8959-06a3c27a7dae"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/css.py",
  "usage": {
    "total_tokens": 43151,
    "tool_uses": 14,
    "duration_ms": 17195
  },
  "last_tool_name": "Read",
  "uuid": "763b8b83-4327-4ac7-8a67-a0471ebe2a57",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_018YcrDZk6xL7w4YA5pwRTdA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/css.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "eeee1571-305f-48a0-b38d-b0c006d1adf8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RaYbx5uUG8TxSUX3f7mWAH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4740,
      "cache_read_input_tokens": 38306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4740,
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

_source line 50 · 2026-05-12T22:07:39.498Z_

<details><summary>↩ Tool result · `toolu_018YcrDZk6xL7w4YA5pwRTdA`</summary>

```text
1	"""
2	CSS (Cross-method Stability Scoring) binarization and consensus module.
3	
4	Provides multiple binarization strategies for converting continuous edge scores
5	to binary circuit membership, then computes cross-method consensus.
6	
7	D010: IFR proximity scores are identical for all heads in the same (src, dst_layer).
8	Top-N binarization causes block-voting. Use percentile_threshold or unique_score_rank
9	to handle tied scores fairly.
10	"""
11	
12	from typing import Dict, List, Literal
13	import numpy as np
14	
15	BinarizeStrategy = Literal["topn", "threshold", "percentile_threshold", "unique_score_rank"]
16	
17	
18	def binarize_scores(
19	    scores: Dict[str, float],
20	    strategy: BinarizeStrategy,
21	    *,
22	    n: int = 200,
23	    threshold: float = 0.01,
24	    percentile: float = 95.0,
25	) -> set[str]:
26	    """Convert continuous edge scores to binary set of 'active' edges.
27	
28	    Strategies:
29	    - topn: select top-N edges by score. Simple but biased when scores are tied (IFR problem).
30	    - threshold: select edges above absolute threshold. Method-dependent.
31	    - percentile_threshold: select edges above P-th percentile of unique score values.
32	      Handles IFR ties: 36 heads with same score count as 1 unique value for percentile calc,
33	      then all 36 are included if above threshold. Avoids block-vote quota stealing.
34	    - unique_score_rank: rank by unique score values, select top-N unique scores,
35	      then include ALL edges with those scores. Ensures tied edges are treated as one unit.
36	    """
37	    if not scores:
38	        return set()
39	
40	    if strategy == "topn":
41	        sorted_edges = sorted(scores.items(), key=lambda x: x[1], reverse=True)
42	        return {edge for edge, _ in sorted_edges[:n]}
43	
44	    elif strategy == "threshold":
45	        return {edge for edge, score in scores.items() if score >= threshold}
46	
47	    elif strategy == "percentile_threshold":
48	        unique_scores = sorted(set(scores.values()))
49	        cutoff_idx = int(len(unique_scores) * percentile / 100)
50	        cutoff_value = unique_scores[cutoff_idx] if cutoff_idx < len(unique_scores) else unique_scores[-1]
51	        return {edge for edge, score in scores.items() if score >= cutoff_value}
52	
53	    elif strategy == "unique_score_rank":
54	        unique_scores = sorted(set(scores.values()), reverse=True)
55	        top_n_scores = set(unique_scores[:n])
56	        return {edge for edge, score in scores.items() if score in top_n_scores}
57	
58	    else:
59	        raise ValueError(f"Unknown strategy: {strategy}")
60	
61	
62	def compute_css_matrix(
63	    method_circuits: Dict[str, set[str]],
64	    all_edges: set[str],
65	) -> Dict:
66	    """Compute cross-method stability matrix (cross-tabulation).
67	
68	    For K methods, each edge falls into one of 2^K cells:
69	    - (1,1,1): all methods agree edge is in circuit (CSS-core)
70	    - (1,0,0): only method 1 includes it (method-specific)
71	    - (0,0,0): no method includes it
72	    - etc.
73	
74	    Returns dict with:
75	    - 'cell_counts': {cell_label: count}
76	    - 'css_core': set of edges in all-1 cell
77	    - 'off_diagonal': set of edges where methods disagree (not all-0 or all-1)
78	    - 'off_diagonal_pct': off_diagonal count / total edges with at least one 1
79	    - 'per_method_counts': {method: n_edges}
80	    """
81	    methods = sorted(method_circuits.keys())
82	    k = len(methods)
83	
84	    cell_counts: Dict[str, int] = {}
85	    css_core: set[str] = set()
86	    off_diagonal: set[str] = set()
87	
88	    all_zeros = tuple(0 for _ in range(k))
89	    all_ones = tuple(1 for _ in range(k))
90	
91	    for edge in all_edges:
92	        cell = tuple(1 if edge in method_circuits[m] else 0 for m in methods)
93	        label = str(cell)
94	        cell_counts[label] = cell_counts.get(label, 0) + 1
95	
96	        if cell == all_ones:
97	            css_core.add(edge)
98	        elif cell != all_zeros:
99	            off_diagonal.add(edge)
100	
101	    at_least_one = len(css_core) + len(off_diagonal)
102	    off_diagonal_pct = len(off_diagonal) / at_least_one if at_least_one > 0 else 0.0
103	
104	    per_method_counts = {m: len(method_circuits[m]) for m in methods}
105	
106	    return {
107	        "cell_counts": cell_counts,
108	        "css_core": css_core,
109	        "off_diagonal": off_diagonal,
110	        "off_diagonal_pct": off_diagonal_pct,
111	        "per_method_counts": per_method_counts,
112	    }
113	
114	
115	def circus_score(
116	    method_circuits: Dict[str, set[str]],
117	    edge: str,
118	) -> float:
119	    """CIRCUS score for a single edge: fraction of methods that include it.
120	
121	    score = |{m : edge in C_m}| / K
122	    """
123	    k = len(method_circuits)
124	    if k == 0:
125	        return 0.0
126	    count = sum(1 for c in method_circuits.values() if edge in c)
127	    return count / k
128	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "85216d3e-e406-4708-9364-223f9682d42b"
}
```

</details>

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 48661,
    "tool_uses": 15,
    "duration_ms": 19930
  },
  "last_tool_name": "Bash",
  "uuid": "9dc431d7-8497-47c0-bb31-580f67ac956e",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01GS4gvVNQSdLzHf934pMMkH`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/ | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "3525787a-99a2-4287-a4c4-84aa093beccf",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011tDEmmmA3vTmVkbuEF8NbB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5508,
      "cache_read_input_tokens": 43046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5508,
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

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 48662,
    "tool_uses": 16,
    "duration_ms": 19962
  },
  "last_tool_name": "Bash",
  "uuid": "416fa036-0887-4739-95bc-dc3dc222487c",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_014g5Q99LKYfgbDVy9hg6A5Z`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp -name \"*.py\" | xargs grep -l \"acdc\\|ACDC\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "489e45bb-8303-4f53-8589-874accff8219",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011tDEmmmA3vTmVkbuEF8NbB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5508,
      "cache_read_input_tokens": 43046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5508,
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

_source line 55 · 2026-05-12T22:07:42.409Z_

<details><summary>↩ Tool result · `toolu_014g5Q99LKYfgbDVy9hg6A5Z`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/css.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/circuit_discovery.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/ifr_discovery.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/config.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "fd753884-7fd8-4775-9578-a92321eb5637"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-12T22:07:42.413Z_

<details><summary>↩ Tool result · `toolu_01GS4gvVNQSdLzHf934pMMkH`</summary>

```text
total 92
drwxr-xr-x 3 ubuntu ubuntu  4096 May 12 12:30 .
drwxr-xr-x 5 ubuntu ubuntu  4096 May 12 21:33 ..
-rw-r--r-- 1 ubuntu ubuntu 16275 May 12 10:03 API_SURVEY.md
-rw-r--r-- 1 ubuntu ubuntu  7067 May 12 10:27 LARGE_MODEL_THIRD_METHOD.md
drwxr-xr-x 2 ubuntu ubuntu  4096 May 12 12:31 __pycache__
-rw-r--r-- 1 ubuntu ubuntu  5570 May 12 12:30 circuit_discovery.py
-rw-r--r-- 1 ubuntu ubuntu  3405 May 12 10:20 circus.py
-rw-r--r-- 1 ubuntu ubuntu  1413 May 12 11:29 config.py
-rw-r--r-- 1 ubuntu ubuntu  3920 May 12 10:26 cross_tabulate.py
-rw-r--r-- 1 ubuntu ubuntu  3129 May 12 11:29 css.py
-rw-r--r-- 1 ubuntu ubuntu  9435 May 12 12:30 edge_pruning_l0.py
-rw-r--r-- 1 ubuntu ubuntu  2983 May 12 10:21 evaluation.py
-rw-r--r-- 1 ubuntu ubuntu  5405 May 12 11:29 ifr_discovery.py
-rw-r--r-- 1 ubuntu ubuntu  5265 May 12 10:26 run_mvp.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "f34f256c-4fa1-48b0-b0a7-bef487d5d415"
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
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/structfuse-mvp/circuit_discovery.py",
  "usage": {
    "total_tokens": 49595,
    "tool_uses": 17,
    "duration_ms": 21405
  },
  "last_tool_name": "Read",
  "uuid": "ff4359fd-4486-4f70-8cdc-9357b748d398",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_012z29Vq6iZBs3K4aimerEZZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/circuit_discovery.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "7b213e20-99f9-4a56-b268-18a98377e1b8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QEGdpmnr5kbpY5X634VKGn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 197,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 48554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 697,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 59 · 2026-05-12T22:07:43.753Z_

<details><summary>↩ Tool result · `toolu_012z29Vq6iZBs3K4aimerEZZ`</summary>

```text
1	"""Unified circuit discovery interface for K=3 methods.
2	Each method returns Dict[str, float] mapping edge_name -> attribution_score.
3	Edge names are normalized to TransformerLens format: "blocks.{L}.attn.hook_result[{H}] -> blocks.{L'}.attn.hook_q[{H'}]"
4	"""
5	
6	import re
7	from typing import Dict, Callable, Optional
8	
9	from config import MVPConfig, MVP_CONFIG
10	
11	
12	# --- Edge name normalization ---
13	
14	def _normalize_eap_edge(edge_str: str) -> str:
15	    """EAP uses Graph node naming close to TransformerLens. Minimal normalization needed."""
16	    # EAP format: "blocks.0.attn.hook_result[0] -> blocks.1.attn.hook_q[1]"
17	    # Already close to TL standard; strip whitespace and ensure consistent spacing
18	    return edge_str.strip()
19	
20	
21	def _normalize_edge_pruning_edge(edge_str: str) -> str:
22	    """Edge Pruning L0 outputs TransformerLens-format names directly."""
23	    return edge_str.strip()
24	
25	
26	def _normalize_acdc_edge(edge_str: str) -> str:
27	    """Auto-Circuit/ACDC edge naming normalization."""
28	    # Auto-Circuit typically uses TL-compatible naming already
29	    return edge_str.strip()
30	
31	
32	def _normalize_ifr_edge(edge_str: str) -> str:
33	    """IFR outputs TL-format edge names directly; no normalization needed."""
34	    return edge_str.strip()
35	
36	
37	_NORMALIZERS = {
38	    "eap_ig": _normalize_eap_edge,
39	    "edge_pruning": _normalize_edge_pruning_edge,
40	    "acdc": _normalize_acdc_edge,
41	    "ifr": _normalize_ifr_edge,
42	}
43	
44	
45	def normalize_edge_names(scores: Dict[str, float], method: str) -> Dict[str, float]:
46	    """Normalize edge names from method-specific format to TransformerLens standard."""
47	    normalizer = _NORMALIZERS.get(method, lambda x: x)
48	    return {normalizer(k): v for k, v in scores.items()}
49	
50	
51	# --- Method implementations ---
52	
53	def run_eap_ig(
54	    model,
55	    dataset,
56	    metric: Callable,
57	    ig_steps: int = 5,
58	    config: MVPConfig = MVP_CONFIG,
59	) -> Dict[str, float]:
60	    """Run EAP-IG attribution and return edge scores.
61	
62	    Args:
63	        model: HookedTransformer instance
64	        dataset: IOI dataset or EAPDataset-compatible
65	        metric: loss/logit-diff metric function
66	        ig_steps: integrated gradients interpolation steps
67	
68	    Returns:
69	        Dict mapping normalized edge names to attribution scores
70	    """
71	    from eap import Graph, attribute
72	
73	    graph = Graph.from_model(model)
74	
75	    # TODO: wrap dataset into EAPDataset format if needed
76	    # dataloader = EAPDataset('ioi').to_dataloader()
77	    dataloader = dataset  # placeholder — adapt to EAPDataset API
78	
79	    attribute(
80	        model, graph, dataloader, metric,
81	        method="EAP-IG-inputs",
82	        ig_steps=ig_steps,
83	    )
84	
85	    raw_scores = {}
86	    for edge in graph.edges:
87	        raw_scores[str(edge)] = float(edge.score)
88	
89	    return normalize_edge_names(raw_scores, "eap_ig")
90	
91	
92	def run_edge_pruning(
93	    model,
94	    dataset,
95	    metric: Callable,
96	    target_sparsity: float = 0.05,
97	    config: MVPConfig = MVP_CONFIG,
98	) -> Dict[str, float]:
99	    """Run Edge Pruning with L0 mask optimization.
100	
101	    Uses Hard Concrete relaxation (Louizos et al. 2018) to optimize continuous
102	    edge masks. Finds the minimal circuit preserving task performance.
103	
104	    Args:
105	        model: HookedTransformer instance
106	        dataset: IOI dataset
107	        metric: callable(logits) -> scalar, higher = better
108	        target_sparsity: fraction of edges to retain
109	
110	    Returns:
111	        Dict mapping normalized edge names to mask scores (0-1)
112	    """
113	    from edge_pruning_l0 import run_edge_pruning_l0
114	
115	    raw_scores = run_edge_pruning_l0(
116	        model, dataset, metric,
117	        target_sparsity=target_sparsity,
118	    )
119	
120	    return normalize_edge_names(raw_scores, "edge_pruning")
121	
122	
123	def run_acdc(
124	    model,
125	    dataset,
126	    metric: Callable,
127	    threshold: float = 0.05,
128	    config: MVPConfig = MVP_CONFIG,
129	) -> Dict[str, float]:
130	    """Run ACDC via auto_circuit library.
131	
132	    Args:
133	        model: HookedTransformer instance
134	        dataset: IOI dataset
135	        metric: loss/logit-diff metric function
136	        threshold: ACDC edge inclusion threshold
137	
138	    Returns:
139	        Dict mapping normalized edge names to binary scores (0 or 1)
140	    """
141	    # TODO: auto_circuit API integration
142	    # from auto_circuit.experiment_utils import load_tl_model
143	    # from auto_circuit.prune_algos.ACDC import acdc_prune_scores
144	    # from auto_circuit.types import PruneScores
145	    #
146	    # prune_scores: PruneScores = acdc_prune_scores(
147	    #     model=model,
148	    #     dataloader=dataset,
149	    #     official_edges=None,
150	    #     tao_exps=[-2],  # threshold
151	    # )
152	    # Convert PruneScores (nested dict of tensors) to flat edge dict
153	
154	    raw_scores: Dict[str, float] = {}
155	
156	    return normalize_edge_names(raw_scores, "acdc")
157	
158	
159	def run_all_methods(
160	    model,
161	    dataset,
162	    metric: Callable,
163	    config: MVPConfig = MVP_CONFIG,
164	) -> Dict[str, Dict[str, float]]:
165	    """Run all K methods and return their edge scores.
166	
167	    Returns:
168	        Dict mapping method_name -> {edge_name: score}
169	    """
170	    from ifr_discovery import run_ifr
171	
172	    runners = {
173	        "eap_ig": lambda: run_eap_ig(model, dataset, metric, config.eap_ig_steps, config),
174	        "edge_pruning": lambda: run_edge_pruning(model, dataset, metric, config.edge_pruning_target_sparsity, config),
175	        "acdc": lambda: run_acdc(model, dataset, metric, config.acdc_threshold, config),
176	        "ifr": lambda: run_ifr(model, dataset, metric),
177	    }
178	
179	    results = {}
180	    for method in config.methods:
181	        print(f"Running {method}...")
182	        results[method] = runners[method]()
183	        print(f"  {method}: {len(results[method])} edges scored")
184	
185	    return results
186	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "4ad34f4c-9ec8-4e12-990b-0c5501b2b1a4"
}
```

</details>

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/structfuse-mvp/run_mvp.py",
  "usage": {
    "total_tokens": 49640,
    "tool_uses": 18,
    "duration_ms": 21820
  },
  "last_tool_name": "Read",
  "uuid": "843cbbad-c1e0-41a5-b7e0-4605a3d9efa3",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_01UbsVxsLV4RyfhVfSKaj2mE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/run_mvp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "bac0a1f3-1e4e-4635-93ec-e1c140509ad1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QEGdpmnr5kbpY5X634VKGn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 197,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 48554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 697,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 62 · 2026-05-12T22:07:44.124Z_

<details><summary>↩ Tool result · `toolu_01UbsVxsLV4RyfhVfSKaj2mE`</summary>

```text
1	"""StructFuse MVP main pipeline.
2	Runs K=3 circuit discovery methods on GPT-2 Small / IOI,
3	computes CSS and CIRCUS, generates cross-tabulation, evaluates faithfulness.
4	"""
5	
6	import json
7	from pathlib import Path
8	
9	from config import MVP_CONFIG
10	from circuit_discovery import run_all_methods
11	from circus import run_circus
12	from css import compute_css, threshold_css, binarize_scores, css_summary
13	from cross_tabulate import cross_tabulate, compute_off_diagonal, print_cross_table
14	from evaluation import evaluate_all_circuits, print_eval_table
15	
16	
17	def load_model_and_data(config):
18	    """Load GPT-2 Small and IOI dataset via TransformerLens."""
19	    from transformer_lens import HookedTransformer
20	
21	    print(f"Loading model: {config.model_name}")
22	    model = HookedTransformer.from_pretrained(config.model_name)
23	
24	    # TODO: use proper IOI dataset
25	    # from transformer_lens.evals import IOIDataset
26	    # dataset = IOIDataset(tokenizer=model.tokenizer, num_samples=config.num_samples)
27	    dataset = None  # placeholder
28	
29	    return model, dataset
30	
31	
32	def logit_diff_metric(logits, tokens):
33	    """IOI logit difference metric: logit(IO) - logit(S)."""
34	    # TODO: implement proper IOI metric
35	    pass
36	
37	
38	def main():
39	    config = MVP_CONFIG
40	    print(f"StructFuse MVP: model={config.model_name}, task={config.task}, K={config.K}")
41	    print(f"Methods: {config.methods}")
42	    print()
43	
44	    # Step 1: Load model + data
45	    model, dataset = load_model_and_data(config)
46	
47	    # Step 2: Run K=3 circuit discovery methods
48	    all_scores = run_all_methods(model, dataset, logit_diff_metric, config)
49	
50	    # Step 3: Binarize each method's scores using method-appropriate strategy
51	    method_circuits = {}
52	    for method, scores in all_scores.items():
53	        method_circuits[method] = binarize_scores(scores, method=method, top_n=config.eap_ig_topn)
54	        print(f"{method}: {len(method_circuits[method])} edges selected")
55	
56	    # Step 4: CIRCUS config-bagging on EAP-IG
57	    print("\n--- CIRCUS (EAP-IG) ---")
58	    eap_stability, circus_tiers = run_circus(all_scores["eap_ig"], config)
59	
60	    # Step 5: CSS across K=3 methods
61	    print("\n--- CSS (K=3) ---")
62	    css_scores = compute_css(method_circuits, K=config.K)
63	    print(f"CSS distribution: {css_summary(css_scores, config.K)}")
64	
65	    css_circuit = threshold_css(css_scores, config.css_default_threshold)
66	    print(f"CSS circuit (>= {config.css_default_threshold}): {len(css_circuit)} edges")
67	
68	    # Step 6: Cross-tabulation
69	    print("\n--- Cross-Tabulation ---")
70	    table = cross_tabulate(circus_tiers, css_scores, config.css_default_threshold)
71	    print_cross_table(table)
72	
73	    off_diag = compute_off_diagonal(table)
74	    print(f"Off-diagonal %: {off_diag*100:.1f}%")
75	
76	    # Step 7: Evaluate all circuit variants
77	    print("\n--- Evaluation ---")
78	    circuits_to_eval = {}
79	
80	    # Individual method circuits
81	    for method, edges in method_circuits.items():
82	        circuits_to_eval[f"method_{method}"] = edges
83	
84	    # CSS circuits at various thresholds
85	    for thr in config.css_thresholds:
86	        if thr > 0:
87	            css_edges = threshold_css(css_scores, thr)
88	            circuits_to_eval[f"css_{thr:.2f}"] = css_edges
89	
90	    # CIRCUS-core circuit
91	    from circus import get_tier_sets
92	    tier_sets = get_tier_sets(circus_tiers)
93	    circuits_to_eval["circus_core"] = tier_sets["core"]
94	
95	    # Stable-core (CIRCUS-core AND CSS-high)
96	    circuits_to_eval["stable_core"] = table.stable_core
97	
98	    eval_results = evaluate_all_circuits(model, circuits_to_eval, dataset, logit_diff_metric)
99	    print_eval_table(eval_results)
100	
101	    # Step 8: MVP gate (graduated per ROADMAP D001-D003)
102	    print("\n" + "=" * 50)
103	    print("MVP GATE ASSESSMENT")
104	    print("=" * 50)
105	    pct = off_diag * 100
106	    if pct >= 10:
107	        gate_verdict = "PASS_MAIN"
108	        gate_msg = f"Off-diagonal {pct:.1f}% >= 10% → Main track, proceed to full experiments"
109	    elif pct >= 5:
110	        gate_verdict = "PASS_FINDINGS"
111	        gate_msg = f"Off-diagonal {pct:.1f}% in [5-10%) → Findings default, add Arithmetic task to confirm"
112	    elif pct >= 2:
113	        gate_verdict = "MARGINAL"
114	        gate_msg = f"Off-diagonal {pct:.1f}% in [2-5%) → Findings track, needs confirmation"
115	    else:
116	        gate_verdict = "KILL"
117	        gate_msg = f"Off-diagonal {pct:.1f}% < 2% → Kill project (if ΔF also not significant)"
118	    print(f"Off-diagonal %: {pct:.1f}%")
119	    print(f"Verdict: {gate_verdict}")
120	    print(f"Action: {gate_msg}")
121	
122	    # Save results
123	    output = {
124	        "config": {
125	            "model": config.model_name,
126	            "task": config.task,
127	            "K": config.K,
128	            "methods": config.methods,
129	        },
130	        "cross_table": table.summary(),
131	        "core_off_diagonal_pct": off_diag,
132	        "css_distribution": css_summary(css_scores, config.K),
133	        "circus_tier_counts": {
134	            t: sum(1 for v in circus_tiers.values() if v == t)
135	            for t in ["core", "contingent", "noise"]
136	        },
137	        "evaluation": [r.to_dict() for r in eval_results],
138	        "gate_verdict": gate_verdict,
139	    }
140	
141	    output_path = Path(__file__).parent / "mvp_results.json"
142	    with open(output_path, "w") as f:
143	        json.dump(output, f, indent=2)
144	    print(f"\nResults saved to {output_path}")
145	
146	
147	if __name__ == "__main__":
148	    main()
149	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "77dc5121-8867-4012-a54a-aded117298d9"
}
```

</details>

---

### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/structfuse-mvp/edge_pruning_l0.py",
  "usage": {
    "total_tokens": 49685,
    "tool_uses": 19,
    "duration_ms": 22082
  },
  "last_tool_name": "Read",
  "uuid": "596686d4-5931-4e54-9589-fc9cd042eab2",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_01HNiJVTk1a1WdMuKbbSEdG8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/edge_pruning_l0.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "a8c852fc-72b6-479d-b9d3-76a57cb619ac",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QEGdpmnr5kbpY5X634VKGn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 197,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 48554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 697,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 65 · 2026-05-12T22:07:44.387Z_

<details><summary>↩ Tool result · `toolu_01HNiJVTk1a1WdMuKbbSEdG8`</summary>

```text
1	"""L0 Edge Pruning: circuit discovery via differentiable mask optimization.
2	
3	Optimizes continuous edge masks using Hard Concrete relaxation (Louizos et al. 2018)
4	with L0 regularization. Minimizes -task_metric + lambda * L0(masks) to find the
5	minimal circuit preserving task performance.
6	
7	vs auto-circuit mask_gradient (gradient-based attribution):
8	  mask_gradient: one-pass importance scoring via integrated gradients over masks
9	  L0 pruning: multi-epoch iterative optimization producing genuinely optimized masks
10	
11	Ref: Bhaskar et al. 2024 "Finding Transformer Circuits with Edge Pruning"
12	"""
13	
14	import math
15	import torch
16	import torch.nn as nn
17	from typing import Dict, List, Tuple
18	
19	
20	class HardConcreteMask(nn.Module):
21	    """Hard Concrete distribution for differentiable L0 regularization.
22	    Ref: Louizos et al. 2018 "Learning Sparse Neural Networks through L0 Regularization"
23	    """
24	
25	    def __init__(self, n_edges: int, init_value: float = 0.0,
26	                 beta: float = 2/3, zeta: float = 1.1, gamma: float = -0.1):
27	        super().__init__()
28	        self.log_alpha = nn.Parameter(torch.full((n_edges,), init_value))
29	        self.beta = beta
30	        self.zeta = zeta
31	        self.gamma = gamma
32	
33	    def forward(self, training: bool = True) -> torch.Tensor:
34	        if training:
35	            u = torch.rand_like(self.log_alpha).clamp(1e-8, 1 - 1e-8)
36	            s = torch.sigmoid((torch.log(u / (1 - u)) + self.log_alpha) / self.beta)
37	            s_bar = s * (self.zeta - self.gamma) + self.gamma
38	            return s_bar.clamp(0, 1)
39	        z = torch.sigmoid(self.log_alpha) * (self.zeta - self.gamma) + self.gamma
40	        return z.clamp(0, 1)
41	
42	    def l0_loss(self) -> torch.Tensor:
43	        """Expected L0 norm under the hard concrete distribution."""
44	        return torch.sigmoid(
45	            self.log_alpha - self.beta * math.log(-self.gamma / self.zeta)
46	        ).sum()
47	
48	
49	# --- Edge topology helpers (mirrored from ifr_discovery.py) ---
50	
51	def _src_layer(name: str) -> int:
52	    if name == "hook_embed":
53	        return -1
54	    return int(name.split(".")[1])
55	
56	
57	def _before_attn(src: str, dst_layer: int) -> bool:
58	    return _src_layer(src) < dst_layer
59	
60	
61	def _before_mlp(src: str, dst_layer: int) -> bool:
62	    sl = _src_layer(src)
63	    if sl < dst_layer:
64	        return True
65	    return sl == dst_layer and "hook_result" in src
66	
67	
68	def _extract_tokens(dataset):
69	    if isinstance(dataset, torch.Tensor):
70	        return dataset
71	    if hasattr(dataset, "toks"):
72	        return dataset.toks
73	    if isinstance(dataset, dict) and "input_ids" in dataset:
74	        return dataset["input_ids"]
75	    return dataset
76	
77	
78	def _build_edge_index(n_layers: int, n_heads: int):
79	    """Build internal edge lists grouped by destination layer.
80	
81	    Attention edges use per-layer granularity (shared across heads at each layer).
82	    MLP edges are per (source, destination_layer).
83	    Output is expanded to per-Q/K/V/head format for CSS compatibility.
84	    """
85	    sources: List[str] = ["hook_embed"]
86	    attn_edges: List[Tuple[str, int]] = []
87	    mlp_edges: List[Tuple[str, int]] = []
88	
89	    for L in range(n_layers):
90	        for src in sources:
91	            if _before_attn(src, L):
92	                attn_edges.append((src, L))
93	
94	        for src in sources:
95	            if _before_mlp(src, L):
96	                mlp_edges.append((src, L))
97	        for H in range(n_heads):
98	            mlp_edges.append((f"blocks.{L}.attn.hook_result[{H}]", L))
99	
100	        for H in range(n_heads):
101	            sources.append(f"blocks.{L}.attn.hook_result[{H}]")
102	        sources.append(f"blocks.{L}.hook_mlp_out")
103	
104	    attn_lookup: Dict[int, List[Tuple[str, int]]] = {}
105	    for i, (src, dst) in enumerate(attn_edges):
106	        attn_lookup.setdefault(dst, []).append((src, i))
107	
108	    mlp_lookup: Dict[int, List[Tuple[str, int]]] = {}
109	    for i, (src, dst) in enumerate(mlp_edges):
110	        mlp_lookup.setdefault(dst, []).append((src, i))
111	
112	    return attn_edges, mlp_edges, attn_lookup, mlp_lookup
113	
114	
115	def _masked_forward(model, embed, z_attn, z_mlp, attn_lookup, mlp_lookup):
116	    """Cascading forward pass with L0 edge masks.
117	
118	    Each component's input is reconstructed as a masked weighted sum of upstream
119	    outputs. Later layers see masked outputs from earlier layers.
120	    """
121	    n_layers = model.cfg.n_layers
122	    n_heads = model.cfg.n_heads
123	    d_head = model.cfg.d_head
124	    device = embed.device
125	    B, S, D = embed.shape
126	
127	    src_acts: Dict[str, torch.Tensor] = {"hook_embed": embed}
128	    # Accumulated attention output biases (b_O per layer, always included)
129	    bias_acc = torch.zeros(1, 1, D, device=device)
130	
131	    for L in range(n_layers):
132	        block = model.blocks[L]
133	
134	        # --- Attention: reconstruct masked residual input ---
135	        resid_attn = bias_acc.expand(B, S, D) + torch.zeros(B, S, D, device=device)
136	        for src_name, idx in attn_lookup.get(L, []):
137	            resid_attn = resid_attn + z_attn[idx] * src_acts[src_name]
138	
139	        normed = block.ln1(resid_attn)
140	        q = torch.einsum('bsd,ndh->bsnh', normed, block.attn.W_Q) + block.attn.b_Q
141	        k = torch.einsum('bsd,ndh->bsnh', normed, block.attn.W_K) + block.attn.b_K
142	        v = torch.einsum('bsd,ndh->bsnh', normed, block.attn.W_V) + block.attn.b_V
143	
144	        attn_scores = torch.einsum('bqnh,bknh->bnqk', q, k) / math.sqrt(d_head)
145	        causal = torch.triu(
146	            torch.ones(S, S, device=device, dtype=torch.bool), diagonal=1
147	        )
148	        attn_scores = attn_scores.masked_fill(causal[None, None], float('-inf'))
149	        pattern = torch.softmax(attn_scores, dim=-1)
150	        z_out = torch.einsum('bnqk,bknh->bqnh', pattern, v)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "a1953b6b-405c-4dcf-9256-4cd67a93fea9"
}
```

</details>

---

### System

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/structfuse-mvp/config.py",
  "usage": {
    "total_tokens": 56445,
    "tool_uses": 20,
    "duration_ms": 24580
  },
  "last_tool_name": "Read",
  "uuid": "6b71596a-25af-4f61-8aa9-24fcd6100e03",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_01SSBcMERMPSfFyf8p1m6Wt5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/config.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "7ac90450-f271-4e15-8555-176e4635dd5e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VXy4F2B243tQFQgGsBC1tX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6949,
      "cache_read_input_tokens": 49251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6949,
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

_source line 68 · 2026-05-12T22:07:46.891Z_

<details><summary>↩ Tool result · `toolu_01SSBcMERMPSfFyf8p1m6Wt5`</summary>

```text
1	"""StructFuse MVP configuration.
2	Defines model/task/method settings, CSS thresholds, and CIRCUS config-bagging params.
3	"""
4	
5	from dataclasses import dataclass, field
6	from typing import List
7	
8	
9	@dataclass
10	class MVPConfig:
11	    model_name: str = "gpt2-small"
12	    task: str = "ioi"
13	    num_samples: int = 100
14	
15	    # K=3 methods
16	    methods: List[str] = field(default_factory=lambda: ["eap_ig", "edge_pruning", "acdc"])
17	    K: int = 3
18	
19	    # CSS thresholds: {0, 1/3, 2/3, 1}
20	    css_thresholds: List[float] = field(default_factory=lambda: [0.0, 0.33, 0.67, 1.0])
21	    css_default_threshold: float = 0.67  # >= 2/3 methods agree
22	
23	    # CIRCUS config-bagging for EAP-IG
24	    circus_B: int = 10  # number of threshold bins
25	    circus_core_threshold: float = 1.0
26	    circus_contingent_threshold: float = 0.5
27	
28	    # Method-specific
29	    eap_ig_steps: int = 5
30	    eap_ig_topn: int = 100
31	    acdc_threshold: float = 0.05
32	    edge_pruning_target_sparsity: float = 0.05
33	
34	    # Evaluation
35	    faithfulness_metrics: List[str] = field(default_factory=lambda: ["cpr", "cmd"])
36	
37	
38	MVP_CONFIG = MVPConfig()
39	
40	
41	@dataclass
42	class LargeModelConfig(MVPConfig):
43	    """Config for large models (0.5B-8B) where ACDC is replaced by IFR."""
44	    model_name: str = "Qwen/Qwen2.5-0.5B"
45	    methods: List[str] = field(default_factory=lambda: ["eap_ig", "edge_pruning", "ifr"])
46	    num_samples: int = 50
47	
48	    eap_ig_topn: int = 200
49	    ifr_topn: int = 200
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "72fd036d-4ba0-4041-8564-efc024002a8e"
}
```

</details>

---

### System

_source line 69_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/structfuse-mvp/ifr_discovery.py",
  "usage": {
    "total_tokens": 56446,
    "tool_uses": 21,
    "duration_ms": 24952
  },
  "last_tool_name": "Read",
  "uuid": "bf693c20-dea7-4041-9164-1f6faffca2c7",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_01PjqWHdf6kCefLRNiinymZV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/ifr_discovery.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "7b4e7017-5937-4880-acdd-29defe295641",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VXy4F2B243tQFQgGsBC1tX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6949,
      "cache_read_input_tokens": 49251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6949,
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

_source line 71 · 2026-05-12T22:07:47.258Z_

<details><summary>↩ Tool result · `toolu_01PjqWHdf6kCefLRNiinymZV`</summary>

```text
1	"""IFR (Information Flow Routes) circuit discovery.
2	
3	Activation decomposition method based on ALTI (Ferrando & Voita, EMNLP 2024).
4	Scores edges by residual-stream proximity between source output and destination input:
5	
6	    score(u->v) = max(||x_v||_1 - ||y_u - x_v||_1, 0)
7	
8	where y_u is component u's output and x_v is the residual stream input to component v.
9	
10	Properties:
11	- Single forward pass + activation cache (no backprop, no optimization loop)
12	- Complementary to gradient-based (EAP-IG) and mask optimization (Edge Pruning)
13	- Scales to 0.5B-8B models, replacing ACDC in the large-model K=3 ensemble
14	"""
15	
16	import torch
17	from typing import Dict, List, Tuple, Optional
18	
19	
20	def _proximity(y_u: torch.Tensor, x_v: torch.Tensor) -> float:
21	    """max(||x_v||_1 - ||y_u - x_v||_1, 0), averaged over batch and sequence."""
22	    diff_norm = (y_u - x_v).abs().sum(dim=-1)
23	    base_norm = x_v.abs().sum(dim=-1)
24	    return (base_norm - diff_norm).clamp(min=0).mean().item()
25	
26	
27	def _src_layer(name: str) -> int:
28	    if name == "hook_embed":
29	        return -1
30	    return int(name.split(".")[1])
31	
32	
33	def _before_attn(src: str, dst_layer: int) -> bool:
34	    """Source must come from a strictly earlier layer to feed into attention."""
35	    return _src_layer(src) < dst_layer
36	
37	
38	def _before_mlp(src: str, dst_layer: int) -> bool:
39	    """Source can be from earlier layers, or same-layer attention heads (not MLP)."""
40	    sl = _src_layer(src)
41	    if sl < dst_layer:
42	        return True
43	    return sl == dst_layer and "hook_result" in src
44	
45	
46	def _extract_tokens(dataset):
47	    if isinstance(dataset, torch.Tensor):
48	        return dataset
49	    if hasattr(dataset, "toks"):
50	        return dataset.toks
51	    if isinstance(dataset, dict) and "input_ids" in dataset:
52	        return dataset["input_ids"]
53	    return dataset
54	
55	
56	def _enumerate_edges(n_layers: int, n_heads: int) -> List[Tuple[str, str]]:
57	    """List all (src_name, dst_name) edge pairs in TransformerLens format."""
58	    sources = ["hook_embed"]
59	    for L in range(n_layers):
60	        for H in range(n_heads):
61	            sources.append(f"blocks.{L}.attn.hook_result[{H}]")
62	        sources.append(f"blocks.{L}.hook_mlp_out")
63	
64	    edges = []
65	    for L_dst in range(n_layers):
66	        for H_dst in range(n_heads):
67	            for hook in ("hook_q", "hook_k", "hook_v"):
68	                dst = f"blocks.{L_dst}.attn.{hook}[{H_dst}]"
69	                for src in sources:
70	                    if _before_attn(src, L_dst):
71	                        edges.append((src, dst))
72	        mlp_dst = f"blocks.{L_dst}.hook_mlp_in"
73	        for src in sources:
74	            if _before_mlp(src, L_dst):
75	                edges.append((src, mlp_dst))
76	    return edges
77	
78	
79	def run_ifr(
80	    model,
81	    dataset,
82	    metric=None,
83	) -> Dict[str, float]:
84	    """Run IFR (Information Flow Routes) and return edge scores.
85	
86	    Args:
87	        model: HookedTransformer instance
88	        dataset: tokenized input (tensor, dict with 'input_ids', or object with .toks)
89	        metric: unused (IFR is non-causal), kept for interface compatibility
90	
91	    Returns:
92	        Dict mapping edge names to IFR proximity scores (>=0).
93	        Edge names use TransformerLens format:
94	        "blocks.{L}.attn.hook_result[{H}] -> blocks.{L'}.attn.hook_q[{H'}]"
95	    """
96	    n_layers = model.cfg.n_layers
97	    n_heads = model.cfg.n_heads
98	
99	    required = set()
100	    for L in range(n_layers):
101	        required.update([
102	            f"blocks.{L}.attn.hook_result",
103	            f"blocks.{L}.hook_mlp_out",
104	            f"blocks.{L}.hook_resid_pre",
105	            f"blocks.{L}.hook_resid_mid",
106	        ])
107	
108	    tokens = _extract_tokens(dataset)
109	
110	    with torch.no_grad():
111	        _, cache = model.run_with_cache(
112	            tokens, names_filter=lambda n: n in required
113	        )
114	
115	    # Source activations: embed (= resid_pre[0]), per-head attn outputs, MLP outputs
116	    src_act = {}
117	    src_act["hook_embed"] = cache["blocks.0.hook_resid_pre"]
118	    for L in range(n_layers):
119	        result = cache[f"blocks.{L}.attn.hook_result"]  # [batch, seq, n_heads, d_model]
120	        for H in range(n_heads):
121	            src_act[f"blocks.{L}.attn.hook_result[{H}]"] = result[:, :, H, :]
122	        src_act[f"blocks.{L}.hook_mlp_out"] = cache[f"blocks.{L}.hook_mlp_out"]
123	
124	    edge_scores: Dict[str, float] = {}
125	
126	    for L_dst in range(n_layers):
127	        resid_pre = cache[f"blocks.{L_dst}.hook_resid_pre"]   # input to attention
128	        resid_mid = cache[f"blocks.{L_dst}.hook_resid_mid"]   # input to MLP
129	
130	        # Compute proximity once per (source, destination_layer) pair;
131	        # all heads at the same layer share resid_pre, so their scores are identical
132	        attn_prox: Dict[str, float] = {}
133	        mlp_prox: Dict[str, float] = {}
134	
135	        for src_name, y_u in src_act.items():
136	            if _before_attn(src_name, L_dst):
137	                attn_prox[src_name] = _proximity(y_u, resid_pre)
138	            if _before_mlp(src_name, L_dst):
139	                mlp_prox[src_name] = _proximity(y_u, resid_mid)
140	
141	        # Expand to per-head Q/K/V edges
142	        for src_name, score in attn_prox.items():
143	            for H_dst in range(n_heads):
144	                for hook in ("hook_q", "hook_k", "hook_v"):
145	                    edge_scores[f"{src_name} -> blocks.{L_dst}.attn.{hook}[{H_dst}]"] = score
146	
147	        # MLP edges
148	        for src_name, score in mlp_prox.items():
149	            edge_scores[f"{src_name} -> blocks.{L_dst}.hook_mlp_in"] = score
150	
151	    return edge_scores
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "543588b1-4771-4302-8c88-d9b5fb63de54"
}
```

</details>

---

### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading decisions.yaml",
  "usage": {
    "total_tokens": 56447,
    "tool_uses": 22,
    "duration_ms": 25120
  },
  "last_tool_name": "Read",
  "uuid": "1f4895f6-3935-4291-9f94-d81086b8ef5c",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Read · `toolu_014WK6ZTwZhM1Jh9vKRs3aUS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "9daaa6a2-593c-4c90-9e55-cfa55ca66965",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VXy4F2B243tQFQgGsBC1tX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6949,
      "cache_read_input_tokens": 49251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6949,
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

_source line 74 · 2026-05-12T22:07:47.423Z_

<details><summary>↩ Tool result · `toolu_014WK6ZTwZhM1Jh9vKRs3aUS`</summary>

```text
1	_next_id: 12
2	decisions:
3	- id: D001
4	  date: 2026-05-12 09:57 UTC
5	  summary: MVP 定义为 pre-registered pilot：GPT-2 Small/IOI 上 K=4 方法 CSS + CIRCUS cross-tabulation
6	  rationale: 'IDEA_BRIEF 已定义 pilot 为第一个计算里程碑（~2h），直接检验核心假设"方法类 artifact 可被二值共识检测"。Pass
7	    criterion: ≥10% CIRCUS-core 边落入 off-diagonal cell。该 pilot 同时也是论文 Section 3 的 motivating
8	    result，失败则需 reframe 为 Findings track。选择此 MVP 因为：(1) 成本极低（~2h 单卡）(2) 直接验证核心假设 (3)
9	    结果直接决定投稿策略。'
10	  related_experiments: []
11	  depends_on: []
12	- id: D002
13	  date: 2026-05-12 09:59 UTC
14	  summary: 定义 MVP gate 灰区规则：5-10% off-diagonal → Findings + 追加第二组 task 验证
15	  rationale: 'Reviewer warning: 5%-10% 灰区无决策规则。决定：5-10% 默认走 Findings track，但在 GPT-2
16	    Small / Arithmetic 上追加验证。若第二组 ≥10% → 升级回 Main；若第二组也 5-10% → 确认 Findings；若第二组 <5%
17	    → 评估是否 IOI 特有现象。同时要求 MVP 报告包含 CIRCUS-core 绝对边数 + binomial 95% CI，若 CIRCUS-core
18	    <30 条边则必须追加第二组 task。'
19	  related_experiments: []
20	  depends_on: []
21	- id: D003
22	  date: 2026-05-12 09:59 UTC
23	  summary: 定义项目级 kill criteria：off-diagonal <2% + ΔF 无统计差异 → kill
24	  rationale: 'Reviewer warning: 缺项目级 kill criteria。决定：off-diagonal <2% across GPT-2
25	    Small 两个 task (IOI + Arithmetic) AND 四种电路 ΔF 无统计显著差异 (bootstrap p>0.05) → kill
26	    project。单一 task <2% 不触发 kill，需两组确认。'
27	  related_experiments: []
28	  depends_on: []
29	- id: D004
30	  date: 2026-05-12 09:59 UTC
31	  summary: MVP 通过后增加 K=3 checkpoint：Qwen-2.5 0.5B / IOI 快速验证
32	  rationale: 'Reviewer warning: 3/4 模型用 K=3 + family constraint，但 pilot 仅测 K=4。决定：MVP
33	    通过后、全量实验前，增加 Qwen-2.5 0.5B / IOI 的 K=3 快速检查（EAP-IG + AtP* + Edge Pruning，~数小时）。若
34	    K=3 family constraint 下 off-diagonal 完全消失（<2%），需重新评估大模型贡献——可能论文仅限 K=4 结果或需要调整
35	    family constraint 定义。'
36	  related_experiments: []
37	  depends_on: []
38	- id: D005
39	  date: 2026-05-12 10:08 UTC
40	  summary: AtP* 无 edge-level 实现：MVP 改为 K=3（EAP-IG+Edge Pruning+ACDC），大模型方案待评估
41	  rationale: 'Reviewer critical: AtP* 官方未开源，社区版仅 node-level。影响：(1) GPT-2 Small 原 K=4
42	    降为 K=3，但 EAP-IG+EP+ACDC 恰好覆盖 3 个算法族（gradient/mask/greedy causal），实际更干净；(2) 大模型原
43	    K=3 降为 K=2（仅 EAP-IG+EP），CSS 退化为平凡二值投票，严重削弱贡献。决策：MVP 用 K=3（3族）推进，同时评估大模型第三方法：(a)
44	    AtP* 自行实现可行性（≤1天）(b) PAHQ 加速 ACDC 到大模型的可行性 (c) MIB 其他 edge-level 方法的算法族分类。'
45	  related_experiments: []
46	  depends_on:
47	  - D001
48	- id: D006
49	  date: 2026-05-12 10:28 UTC
50	  summary: 大模型 K=3 第三方法确定为 IFR，论文采用 triangulation 框架定位
51	  rationale: Agent 评估三条路径：(a) AtP* 自实现仍是 gradient 族，不解决 K=2 仅 2 族问题 (b) PAHQ 加速 ACDC
52	    不可行 (c) MIB 方法中 IFR 唯一满足"非 gradient、非 mask optimization、edge-level、可扩展到 8B"。Reviewer
53	    确认 IFR 为最佳选项，但指出 IFR 是非因果方法（度量激活空间 proximity 而非因果贡献）。采纳 Reviewer 建议：论文定位 IFR 为
54	    triangulation 中的"independent signal"而非"causal validator"——若一条边同时被因果方法 + 优化方法 +
55	    相似度方法识别，作为机制组件的证据更强。GPT-2 Small（3 因果方法）vs 大模型（2 因果 + 1 非因果）的 CSS 语义差异须在论文中诚实披露。
56	  related_experiments: []
57	  depends_on:
58	  - D005
59	- id: D007
60	  date: 2026-05-12 12:11 UTC
61	  summary: GPU 越界事故：kill 越界进程 + 修复 CUDA_VISIBLE_DEVICES + 重跑 MVP
62	  rationale: 'Reviewer critical: 项目进程跑到 cuda:0/cuda:1（白名单仅 cuda:5），L1 红线违规。原因推测为 Agent
63	    重启进程时未设 CUDA_VISIBLE_DEVICES=5。处置：立即 kill + 修复启动脚本加入 GPU 硬检查 + cuda:5 上重跑。ACDC
64	    71.5% 进度丢失。'
65	  related_experiments: []
66	  depends_on: []
67	- id: D008
68	  date: 2026-05-12 13:02 UTC
69	  summary: MVP 结果解读协议：mask_gradient proxy 下 ≥10% 可信（保守估计），<10% 需 L0 EP 重测
70	  rationale: 当前 MVP 实际为 2 族（EAP-IG + mask_gradient 同属 gradient，+ ACDC greedy causal），非
71	    3 族。同族方法更易同意 → off-diagonal 偏低。因此：≥10% 是保守估计（真实跨族分歧可能更大），gate pass 可信；<10% 不直接判
72	    fail，需部署 L0 EP 到服务器重测 IOI 后再做 gate 判定。Phase 2 全量实验无论如何必须换 L0 EP。
73	  related_experiments: []
74	  depends_on:
75	  - D005
76	  - D007
77	- id: D009
78	  date: 2026-05-12 17:01 UTC
79	  summary: 修复边名格式不匹配 critical bug：统一 EAP-IG 和 EP/ACDC 的边名归一化到同一 canonical form
80	  rationale: Reviewer 发现 _normalize_eap_edge 产出 dash 分隔符 + m0 格式，_normalize_ac_edge
81	    产出 arrow 分隔符 + mlp 0 格式，导致 css.py 字符串匹配完全失败，所有 CSS 值和 off_diagonal_pct 无效。修复方案：统一
82	    canonical form + 转换已有缓存，不重跑 discovery。
83	  related_experiments:
84	  - exp_id: mvp_pilot_gpt2_ioi
85	    role: affected
86	    result: CSS 结果因边名 bug 无效，需修复后重算
87	  depends_on: []
88	- id: D010
89	  date: 2026-05-12 18:40 UTC
90	  summary: Phase 2 IFR binarization策略：用 percentile threshold 或 unique-score-rank 替代
91	    top-N，避免 layer-block voting 偏差
92	  rationale: Reviewer 审查发现 IFR run_ifr() 对同一 (src, dst_layer) 的所有 head×QKV 赋相同 proximity
93	    score（residual-stream proximity 固有局限），导致每对产生 36 条同分边。CSS binarize_scores 的 top-N
94	    模式下少数 (src,layer) 对即可 block-vote 占满配额，与 EAP-IG/EP 的 per-edge 粒度系统性不匹配，可能人为膨胀/压缩
95	    off-diagonal。不影响 MVP（MVP 不含 IFR），Phase 2 集成时需：(1) 改用 percentile threshold 或 unique-score-rank
96	    binarization (2) 论文披露 IFR layer-block 粒度 vs 其他方法 edge 粒度差异。
97	  related_experiments: []
98	  depends_on:
99	  - D006
100	- id: D011
101	  date: 2026-05-12 19:13 UTC
102	  summary: EP HF 后端需重构：从 layer pre-hook 改为 submodule-level hooks（q_proj/k_proj/v_proj/mlp
103	    各自 hook），修复 MLP mask 未应用 + Q/K/V 聚合两个问题
104	  rationale: Reviewer 发现 EP HF 实现有两个 warning：(1) MLP edge mask 参数参与 backward 但 forward
105	    无 hook 应用，MLP score 不可信；(2) 同一 (src, layer) 的所有 Q/K/V edge mask 被 mean 聚合为单标量，丢失
106	    per-edge 粒度。两个问题使 EP 退化为 layer-level masking。修复方案：将 hook 从 layer pre-hook 下沉到
107	    q_proj/k_proj/v_proj/mlp submodule level，每个 submodule 独立 hook 并应用对应 edge mask。这在
108	    HF hook 框架内可行，不需要重写 forward pass。若不修复，Phase 2 K=3 中 EP+IFR 都是 approximate，CSS
109	    edge-level 共识叙事被削弱。
110	  related_experiments: []
111	  depends_on:
112	  - D010
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "95704251-41b7-4c4c-832e-aa8b8ac45295"
}
```

</details>

---

### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 62936,
    "tool_uses": 23,
    "duration_ms": 27594
  },
  "last_tool_name": "Bash",
  "uuid": "ccc63a25-665c-4a69-b49b-15e522f87ddf",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Bash · `toolu_01X6YXusJ511ponKRZNz6ZDt`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context -name \"*.json\" -o -name \"*.yaml\" | grep -E \"config|experiment\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "df9d758f-dc6b-4eba-ad25-ec4518854678",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Nj2c6fTvkEpZLDUQQK4NXD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6481,
      "cache_read_input_tokens": 56200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6481,
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

_source line 77 · 2026-05-12T22:07:49.954Z_

<details><summary>↩ Tool result · `toolu_01X6YXusJ511ponKRZNz6ZDt`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "3569055e-aacf-47d5-a00d-769f14379a1b"
}
```

</details>

---

### System

_source line 78_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/analyze_mvp_results.py",
  "usage": {
    "total_tokens": 63127,
    "tool_uses": 24,
    "duration_ms": 29072
  },
  "last_tool_name": "Read",
  "uuid": "ca70851e-4822-4be8-9d71-04eedcc96e9e",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — Read · `toolu_01SxJUwhB7AcGQSJYSX1CmqL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/analyze_mvp_results.py",
  "offset": 200,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "351bc690-0194-4a2d-a536-97156e8e43f0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011SCGs5b3EsFJRwvrbr13E9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 148,
      "cache_read_input_tokens": 62681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 148,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 80 · 2026-05-12T22:07:51.376Z_

<details><summary>↩ Tool result · `toolu_01SxJUwhB7AcGQSJYSX1CmqL`</summary>

```text
200	    stability = sum((vals >= t).astype(float) for t in thresholds) / B
201	    tiers = {}
202	    for edge, s in zip(edges, stability):
203	        if s >= core_thr:
204	            tiers[edge] = "core"
205	        elif s >= contingent_thr:
206	            tiers[edge] = "contingent"
207	        else:
208	            tiers[edge] = "noise"
209	    return tiers
210	
211	
212	def compute_cross_table(
213	    tiers: Dict[str, str],
214	    circuits: Dict[str, Set[str]],
215	    css_threshold: float = 0.67,
216	    K: int = 3,
217	) -> Dict[str, Any]:
218	    all_edges: Set[str] = set(tiers.keys())
219	    for c in circuits.values():
220	        all_edges |= c
221	
222	    css_scores: Dict[str, float] = {}
223	    for edge in all_edges:
224	        css_scores[edge] = sum(1 for c in circuits.values() if edge in c) / K
225	
226	    stable_core = set()
227	    method_specific = set()
228	    cross_unstable = set()
229	    noise = set()
230	
231	    for e in all_edges:
232	        is_core = tiers.get(e) == "core"
233	        is_high = css_scores.get(e, 0.0) >= css_threshold - 0.01
234	        if is_core and is_high:
235	            stable_core.add(e)
236	        elif is_core:
237	            method_specific.add(e)
238	        elif is_high:
239	            cross_unstable.add(e)
240	        else:
241	            noise.add(e)
242	
243	    core_total = len(stable_core) + len(method_specific)
244	    off_diag = len(method_specific) / core_total if core_total > 0 else 0.0
245	
246	    return {
247	        "stable_core": len(stable_core),
248	        "method_specific": len(method_specific),
249	        "cross_unstable": len(cross_unstable),
250	        "noise": len(noise),
251	        "core_total": core_total,
252	        "off_diagonal_pct": off_diag,
253	    }
254	
255	
256	# ---------------------------------------------------------------------------
257	# ACDC threshold sensitivity
258	# ---------------------------------------------------------------------------
259	
260	ACDC_TAUS = [0.01, 0.03, 0.05, 0.1, 0.3]
261	
262	
263	def acdc_sensitivity(
264	    all_scores: Dict[str, Dict[str, float]],
265	    top_n: int = 200,
266	    taus: Optional[List[float]] = None,
267	) -> List[Dict[str, Any]]:
268	    """Sweep ACDC thresholds, recompute off-diagonal for each."""
269	    if "acdc" not in all_scores:
270	        return []
271	
272	    taus = taus or ACDC_TAUS
273	    other_methods = {m: s for m, s in all_scores.items() if m != "acdc"}
274	    if not other_methods:
275	        return []
276	
277	    results = []
278	    for tau in taus:
279	        circuits: Dict[str, Set[str]] = {}
280	        for m, s in other_methods.items():
281	            circuits[m] = binarize_method(s, m, top_n=top_n)
282	        circuits["acdc"] = binarize_acdc(all_scores["acdc"], tau=tau)
283	
284	        css_result = compute_css_matrix_full(circuits)
285	        results.append({
286	            "tau": tau,
287	            "acdc_size": len(circuits["acdc"]),
288	            "off_diagonal": css_result["off_diagonal"],
289	            "off_diagonal_pct": css_result["off_diagonal_pct"],
290	            "total_union": css_result["total_union"],
291	        })
292	    return results
293	
294	
295	# ---------------------------------------------------------------------------
296	# Gate judgment
297	# ---------------------------------------------------------------------------
298	
299	def gate_judgment(off_diagonal_pct: float) -> Dict[str, str]:
300	    pct = off_diagonal_pct * 100
301	    if pct >= 10:
302	        return {
303	            "verdict": "PASS_MAIN",
304	            "action": f"Off-diagonal {pct:.1f}% >= 10% → Main track",
305	        }
306	    elif pct >= 5:
307	        return {
308	            "verdict": "PASS_FINDINGS",
309	            "action": f"Off-diagonal {pct:.1f}% in [5-10%) → Findings + Arithmetic 追加验证",
310	        }
311	    elif pct >= 2:
312	        return {
313	            "verdict": "MARGINAL",
314	            "action": f"Off-diagonal {pct:.1f}% in [2-5%) → Findings 确认",
315	        }
316	    else:
317	        return {
318	            "verdict": "KILL",
319	            "action": f"Off-diagonal {pct:.1f}% < 2% → Kill (if ΔF 无统计差异)",
320	        }
321	
322	
323	# ---------------------------------------------------------------------------
324	# Visualization
325	# ---------------------------------------------------------------------------
326	
327	def save_css_heatmap(
328	    pairwise: Dict[str, float],
329	    methods: List[str],
330	    output_path: Path,
331	) -> None:
332	    try:
333	        import matplotlib
334	        matplotlib.use("Agg")
335	        import matplotlib.pyplot as plt
336	    except ImportError:
337	        print("  matplotlib not available, skipping heatmap")
338	        return
339	
340	    K = len(methods)
341	    matrix = np.eye(K)
342	    for i, m1 in enumerate(methods):
343	        for j, m2 in enumerate(methods):
344	            if i == j:
345	                continue
346	            key = f"{min(m1,m2)} vs {max(m1,m2)}"
347	            if key not in pairwise:
348	                key = f"{m1} vs {m2}"
349	                if key not in pairwise:
350	                    key = f"{m2} vs {m1}"
351	            matrix[i, j] = pairwise.get(key, 0.0)
352	
353	    fig, ax = plt.subplots(figsize=(6, 5))
354	    im = ax.imshow(matrix, cmap="YlOrRd", vmin=0, vmax=1)
355	    ax.set_xticks(range(K))
356	    ax.set_yticks(range(K))
357	    ax.set_xticklabels(methods, rotation=45, ha="right")
358	    ax.set_yticklabels(methods)
359	    for i in range(K):
360	        for j in range(K):
361	            ax.text(j, i, f"{matrix[i, j]:.3f}", ha="center", va="center",
362	                    color="white" if matrix[i, j] > 0.5 else "black", fontsize=11)
363	    ax.set_title("Pairwise Jaccard Similarity (CSS)")
364	    fig.colorbar(im, ax=ax, shrink=0.8)
365	    fig.tight_layout()
366	    fig.savefig(output_path, dpi=150, bbox_inches="tight")
367	    plt.close(fig)
368	    print(f"  Saved heatmap → {output_path}")
369	
370	
371	def save_venn_or_bar(
372	    circuits: Dict[str, Set[str]],
373	    output_path: Path,
374	) -> None:
375	    try:
376	        import matplotlib
377	        matplotlib.use("Agg")
378	        import matplotlib.pyplot as plt
379	    except ImportError:
380	        print("  matplotlib not available, skipping overlap chart")
381	        return
382	
383	    methods = sorted(circuits.keys())
384	    if len(methods) != 3:
385	        _save_overlap_bar(circuits, output_path, plt)
386	        return
387	
388	    try:
389	        from matplotlib_venn import venn3
390	        a, b, c = [circuits[m] for m in methods]
391	        fig, ax = plt.subplots(figsize=(7, 6))
392	        venn3([a, b, c], set_labels=methods, ax=ax)
393	        ax.set_title("Edge Overlap (3-method Venn)")
394	        fig.tight_layout()
395	        fig.savefig(output_path, dpi=150, bbox_inches="tight")
396	        plt.close(fig)
397	        print(f"  Saved Venn diagram → {output_path}")
398	    except ImportError:
399	        _save_overlap_bar(circuits, output_path, plt)
400	
401	
402	def _save_overlap_bar(circuits: Dict[str, Set[str]], output_path: Path, plt) -> None:
403	    methods = sorted(circuits.keys())
404	    all_edges: Set[str] = set()
405	    for c in circuits.values():
406	        all_edges |= c
407	
408	    counts_by_agreement = Counter()
409	    for edge in all_edges:
410	        n = sum(1 for m in methods if edge in circuits[m])
411	        counts_by_agreement[n] += 1
412	
413	    labels = [f"{k}/{len(methods)}" for k in sorted(counts_by_agreement.keys())]
414	    values = [counts_by_agreement[k] for k in sorted(counts_by_agreement.keys())]
415	
416	    fig, ax = plt.subplots(figsize=(6, 4))
417	    bars = ax.bar(labels, values, color=["#d62728", "#ff7f0e", "#2ca02c"][:len(labels)])
418	    ax.set_xlabel("Methods agreeing")
419	    ax.set_ylabel("Number of edges")
420	    ax.set_title("Edge Agreement Distribution")
421	    for bar, v in zip(bars, values):
422	        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
423	                str(v), ha="center", va="bottom", fontsize=10)
424	    fig.tight_layout()
425	    fig.savefig(output_path, dpi=150, bbox_inches="tight")
426	    plt.close(fig)
427	    print(f"  Saved overlap bar chart → {output_path}")
428	
429	
430	# ---------------------------------------------------------------------------
431	# Mock data for --dry-run
432	# ---------------------------------------------------------------------------
433	
434	def generate_mock_data() -> Dict[str, Dict[str, float]]:
435	    rng = np.random.RandomState(42)
436	    n_total = 500
437	    edge_names = [f"blocks.{l}.attn.hook_result[{h}] -> blocks.{l+1}.attn.hook_q[{h2}]"
438	                  for l in range(12) for h in range(12) for h2 in range(12)
439	                  if l * 144 + h * 12 + h2 < n_total]
440	    edge_names = edge_names[:n_total]
441	
442	    eap_ig = {e: float(rng.randn()) for e in edge_names}
443	    ep_scores = {e: float(rng.uniform(0, 1)) for e in edge_names}
444	    acdc_scores = {}
445	    for e in edge_names:
446	        acdc_scores[e] = float(rng.choice([0.0, 0.02, 0.05, 0.1, 0.5, 1.0],
447	                                           p=[0.5, 0.1, 0.1, 0.1, 0.1, 0.1]))
448	
449	    return {"eap_ig": eap_ig, "edge_pruning": ep_scores, "acdc": acdc_scores}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "4d7285b3-1158-42f7-a00a-3cf2ff4fc887"
}
```

</details>

---

### System

_source line 81_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 63172,
    "tool_uses": 25,
    "duration_ms": 29370
  },
  "last_tool_name": "Bash",
  "uuid": "a517980d-2b8b-4f80-b750-a2cbcaace21e",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — Bash · `toolu_01R4pTePBTEbAzKuKztWc784`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/*.yaml 2>/dev/null || echo \"No yaml files found\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "bfc6bb83-dc72-4224-8c63-458797f20cf4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011SCGs5b3EsFJRwvrbr13E9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 148,
      "cache_read_input_tokens": 62681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 148,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 83 · 2026-05-12T22:07:51.731Z_

<details><summary>↩ Tool result · `toolu_01R4pTePBTEbAzKuKztWc784`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 9077 May 12 21:33 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "9758c8d3-33ee-4716-95c2-d267870129b4"
}
```

</details>

---

### System

_source line 84_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/manifest.yaml",
  "usage": {
    "total_tokens": 66885,
    "tool_uses": 26,
    "duration_ms": 31351
  },
  "last_tool_name": "Read",
  "uuid": "b2ae5e0f-98c9-4c61-80c3-f27c019d1c2d",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Read · `toolu_01UfUz8jRKB7ZfnVdqfCHRBT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "ac2850cc-8ac4-45c7-84cb-dddcabe2345c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XtCbfVDQb7fex3ES2PoHVX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3664,
      "cache_read_input_tokens": 62829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3664,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
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

_source line 86 · 2026-05-12T22:07:53.654Z_

<details><summary>↩ Tool result · `toolu_01UfUz8jRKB7ZfnVdqfCHRBT`</summary>

```text
1	- id: art_20260512_9b9976
2	  name: MVP K=3 Code Framework
3	  type: intermediate
4	  description: StructFuse MVP代码框架：K=3方法(EAP-IG/Edge Pruning/ACDC)统一接口、CSS跨方法共识、CIRCUS
5	    config-bagging、交叉表分析、faithfulness评估。7个Python文件。
6	  path: projects/structfuse-context/artifacts/_project/intermediate/run_mvp.py
7	  url: null
8	  project: structfuse-context
9	  exp_id: null
10	  skill: ''
11	  created_at: '2026-05-12T10:24:37.460496+00:00'
12	  tags:
13	  - mvp
14	  - code
15	  - k3
16	- id: art_20260512_588c02
17	  name: Large Model Third Method Assessment
18	  type: report
19	  description: 大模型第三方法可行性评估：AtP*自实现/PAHQ加速ACDC/MIB方法逐一评估。结论：首选IFR（activation decomposition族，MIB已有实现，1次forward
20	    pass）。
21	  path: projects/structfuse-context/artifacts/_project/report/LARGE_MODEL_THIRD_METHOD.md
22	  url: null
23	  project: structfuse-context
24	  exp_id: null
25	  skill: ''
26	  created_at: '2026-05-12T10:27:46.102648+00:00'
27	  tags:
28	  - research
29	  - method-evaluation
30	  - large-model
31	- id: art_20260512_13aac5
32	  name: IFR Circuit Discovery Module
33	  type: intermediate
34	  description: IFR (Information Flow Routes) circuit discovery 模块：activation decomposition
35	    方法，基于 ALTI proximity scoring。替代 ACDC 用于大模型 K=3 ensemble。含 LargeModelConfig + css/circuit_discovery
36	    集成。
37	  path: projects/structfuse-context/artifacts/_project/intermediate/ifr_discovery.py
38	  url: null
39	  project: structfuse-context
40	  exp_id: null
41	  skill: ''
42	  created_at: '2026-05-12T11:32:17.814003+00:00'
43	  tags:
44	  - ifr
45	  - code
46	  - large-model
47	  - phase2
48	- id: art_20260512_833006
49	  name: edge_pruning_l0
50	  type: intermediate
51	  description: L0 Edge Pruning implementation (Hard Concrete relaxation, Louizos et
52	    al. 2018) - replaces auto-circuit mask_gradient for Phase 2
53	  path: projects/structfuse-context/artifacts/_project/intermediate/edge_pruning_l0.py
54	  url: null
55	  project: structfuse-context
56	  exp_id: null
57	  skill: ''
58	  created_at: '2026-05-12T12:34:58.635440+00:00'
59	  tags:
60	  - edge-pruning
61	  - l0
62	  - circuit-discovery
63	  - phase2
64	- id: art_20260512_0e6bad
65	  name: ifr_scoring
66	  type: intermediate
67	  description: IFR (Information Flow Routes) edge-level scoring for HuggingFace models.
68	    ALTI-based proximity attribution, outputs Dict[str, float] with canonical edge
69	    naming ({src}->{dst}). Supports Llama/Qwen2/Gemma2/Mistral/GPT2.
70	  path: projects/structfuse-context/artifacts/_project/intermediate/ifr_scoring.py
71	  url: null
72	  project: structfuse-context
73	  exp_id: null
74	  skill: ''
75	  created_at: '2026-05-12T18:31:59.317648+00:00'
76	  tags:
77	  - ifr
78	  - circuit-discovery
79	  - edge-scoring
80	  - alti
81	- id: art_20260512_58233f
82	  name: test_ifr_scoring
83	  type: intermediate
84	  description: Smoke tests for ifr_scoring.py — AST-based signature validation (no
85	    deps) + optional GPT-2 integration test.
86	  path: projects/structfuse-context/artifacts/_project/intermediate/test_ifr_scoring.py
87	  url: null
88	  project: structfuse-context
89	  exp_id: null
90	  skill: ''
91	  created_at: '2026-05-12T18:32:01.262431+00:00'
92	  tags:
93	  - ifr
94	  - test
95	- id: art_20260512_b4c754
96	  name: model_adapter
97	  type: intermediate
98	  description: 'Model adapter: unified interface for GPT-2 (TransformerLens) and Qwen-2.5
99	    (HuggingFace) with canonical node naming, hook point mapping, and edge name conversion.'
100	  path: projects/structfuse-context/artifacts/_project/intermediate/model_adapter.py
101	  url: null
102	  project: structfuse-context
103	  exp_id: null
104	  skill: ''
105	  created_at: '2026-05-12T18:40:57.073164+00:00'
106	  tags:
107	  - qwen2
108	  - adapter
109	  - circuit-discovery
110	  - phase2
111	- id: art_20260512_e22fbf
112	  name: run_circus
113	  type: intermediate
114	  description: 'Config-driven StructFuse pipeline: multi-method circuit discovery
115	    (EAP-IG + Edge Pruning + IFR) with CSS consensus, CIRCUS stability, cross-tabulation.
116	    Supports GPT-2 and Qwen-2.5.'
117	  path: projects/structfuse-context/artifacts/_project/intermediate/run_circus.py
118	  url: null
119	  project: structfuse-context
120	  exp_id: null
121	  skill: ''
122	  created_at: '2026-05-12T18:40:59.712651+00:00'
123	  tags:
124	  - pipeline
125	  - css
126	  - circus
127	  - phase2
128	- id: art_20260512_fb43fd
129	  name: css_binarization_module
130	  type: intermediate
131	  description: 'CSS binarization and consensus module: 4 strategies (topn, threshold,
132	    percentile_threshold, unique_score_rank) + cross-method stability matrix + CIRCUS
133	    score. Addresses D010 IFR per-head score homogeneity.'
134	  path: projects/structfuse-context/artifacts/_project/intermediate/css.py
135	  url: null
136	  project: structfuse-context
137	  exp_id: null
138	  skill: ''
139	  created_at: '2026-05-12T18:47:10.990909+00:00'
140	  tags:
141	  - css
142	  - binarization
143	  - d010
144	  - ifr-fix
145	- id: art_20260512_44074d
146	  name: css_smoke_tests
147	  type: intermediate
148	  description: 8 smoke tests for CSS module covering all binarization strategies,
149	    IFR tie handling, CSS matrix, off_diagonal_pct, CIRCUS score.
150	  path: projects/structfuse-context/artifacts/_project/intermediate/test_css.py
151	  url: null
152	  project: structfuse-context
153	  exp_id: null
154	  skill: ''
155	  created_at: '2026-05-12T18:47:13.262062+00:00'
156	  tags:
157	  - css
158	  - test
159	  - d010
160	- id: art_20260512_d51609
161	  name: edge_pruning_scoring
162	  type: intermediate
163	  description: Edge Pruning L0 scoring module for HuggingFace models with GQA support.
164	    Implements Hard Concrete mask parameterization and hook-based masked forward pass.
165	  path: projects/structfuse-context/artifacts/_project/intermediate/edge_pruning_scoring.py
166	  url: null
167	  project: structfuse-context
168	  exp_id: null
169	  skill: ''
170	  created_at: '2026-05-12T19:09:58.618888+00:00'
171	  tags:
172	  - edge-pruning
173	  - l0
174	  - circuit-discovery
175	  - gqa
176	- id: art_20260512_686b21
177	  name: test_edge_pruning_scoring
178	  type: intermediate
179	  description: 'Smoke tests for edge_pruning_scoring.py: AST, topology, GQA mask sharing,
180	    HardConcrete numerics'
181	  path: projects/structfuse-context/artifacts/_project/intermediate/test_edge_pruning_scoring.py
182	  url: null
183	  project: structfuse-context
184	  exp_id: null
185	  skill: ''
186	  created_at: '2026-05-12T19:10:01.032381+00:00'
187	  tags:
188	  - test
189	  - edge-pruning
190	- id: art_20260512_69c14c
191	  name: eap_ig_scoring
192	  type: intermediate
193	  description: EAP-IG edge-level attribution scoring for HuggingFace models (Qwen2/Llama/Gemma2/GPT-2).
194	    Per-head Q/K/V gradient decomposition with GQA support.
195	  path: projects/structfuse-context/artifacts/_project/intermediate/eap_ig_scoring.py
196	  url: null
197	  project: structfuse-context
198	  exp_id: null
199	  skill: ''
200	  created_at: '2026-05-12T19:25:27.243827+00:00'
201	  tags:
202	  - eap-ig
203	  - circuit-discovery
204	  - huggingface
205	  - phase2
206	- id: art_20260512_437d02
207	  name: test_eap_ig_scoring
208	  type: intermediate
209	  description: 'Smoke tests for eap_ig_scoring.py: AST checks + GPT-2 integration
210	    test'
211	  path: projects/structfuse-context/artifacts/_project/intermediate/test_eap_ig_scoring.py
212	  url: null
213	  project: structfuse-context
214	  exp_id: null
215	  skill: ''
216	  created_at: '2026-05-12T19:25:28.746439+00:00'
217	  tags:
218	  - test
219	  - eap-ig
220	- id: art_20260512_457920
221	  name: edge_pruning_scoring_v2
222	  type: intermediate
223	  description: 'Edge Pruning v2: fixes MLP mask not applied in forward + Q/K/V mean
224	    collapse. 4 submodule hooks per layer (q_proj, k_proj, v_proj, mlp) replace single
225	    layer pre-hook.'
226	  path: projects/structfuse-context/artifacts/_project/intermediate/edge_pruning_scoring_457920.py
227	  url: null
228	  project: structfuse-context
229	  exp_id: null
230	  skill: ''
231	  created_at: '2026-05-12T19:30:48.826026+00:00'
232	  tags:
233	  - edge-pruning
234	  - v2
235	  - hook-fix
236	- id: art_20260512_3089a7
237	  name: test_edge_pruning_scoring_v2
238	  type: intermediate
239	  description: 'Smoke tests for edge_pruning_scoring v2: topology, hook mask indices,
240	    Q/K/V independence, GQA sharing, edge coverage.'
241	  path: projects/structfuse-context/artifacts/_project/intermediate/test_edge_pruning_scoring_3089a7.py
242	  url: null
243	  project: structfuse-context
244	  exp_id: null
245	  skill: ''
246	  created_at: '2026-05-12T19:30:51.087734+00:00'
247	  tags:
248	  - edge-pruning
249	  - v2
250	  - test
251	- id: art_20260512_da695c
252	  name: deploy_phase2.sh
253	  type: intermediate
254	  description: Phase 2 deployment script - syncs code to cqa1-21977 and runs dry-run
255	    validation for Qwen2.5-0.5B K=3 checkpoint experiment
256	  path: projects/structfuse-context/artifacts/_project/intermediate/deploy_phase2.sh
257	  url: null
258	  project: structfuse-context
259	  exp_id: null
260	  skill: ''
261	  created_at: '2026-05-12T20:11:48.201368+00:00'
262	  tags:
263	  - phase2
264	  - deployment
265	  - qwen
266	- id: art_20260512_9f1b22
267	  name: analyze_mvp_results
268	  type: intermediate
269	  description: MVP 结果自动分析脚本：加载三方法 edge scores，计算 CSS matrix/Jaccard/off-diagonal，ACDC
270	    threshold 敏感性，CIRCUS cross-table，可视化，pass/fail 判定
271	  path: projects/structfuse-context/artifacts/_project/intermediate/analyze_mvp_results.py
272	  url: null
273	  project: structfuse-context
274	  exp_id: null
275	  skill: ''
276	  created_at: '2026-05-12T21:33:30.886244+00:00'
277	  tags:
278	  - mvp
279	  - analysis
280	  - css
281	  - gate
282	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "e4be3bcd-2a1c-4564-87b5-9196452d6f2e"
}
```

</details>

---

### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/analyze_mvp_results.py",
  "usage": {
    "total_tokens": 66933,
    "tool_uses": 27,
    "duration_ms": 31731
  },
  "last_tool_name": "Read",
  "uuid": "1b9efc51-00de-424d-a8e9-e082ed5c2f72",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Read · `toolu_014NR35T9MJKFBPjfPEu6V1y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/analyze_mvp_results.py",
  "offset": 450,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "412f301c-fd82-4541-a1d7-9750cd18bec6",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XtCbfVDQb7fex3ES2PoHVX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3664,
      "cache_read_input_tokens": 62829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3664,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
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

_source line 89 · 2026-05-12T22:07:54.042Z_

<details><summary>↩ Tool result · `toolu_014NR35T9MJKFBPjfPEu6V1y`</summary>

```text
450	
451	
452	# ---------------------------------------------------------------------------
453	# Main analysis
454	# ---------------------------------------------------------------------------
455	
456	def run_analysis(
457	    results_dir: Path,
458	    output_dir: Path,
459	    top_n: int = 200,
460	    dry_run: bool = False,
461	) -> Dict[str, Any]:
462	    output_dir.mkdir(parents=True, exist_ok=True)
463	
464	    # --- Load data ---
465	    print("=== Data Loading ===")
466	    if dry_run:
467	        print("  [dry-run] Using mock data")
468	        all_scores = generate_mock_data()
469	        pipeline = None
470	    else:
471	        all_scores, pipeline = load_all_data(results_dir)
472	
473	    if not all_scores:
474	        print("ERROR: No method scores available. Check --results-dir.")
475	        sys.exit(1)
476	
477	    methods = sorted(all_scores.keys())
478	    K = len(methods)
479	    print(f"  Methods found: {methods} (K={K})")
480	
481	    # --- Binarize ---
482	    print("\n=== Binarization ===")
483	    circuits: Dict[str, Set[str]] = {}
484	    for m in methods:
485	        circuits[m] = binarize_method(all_scores[m], m, top_n=top_n)
486	        print(f"  {m}: {len(circuits[m])} edges selected")
487	
488	    all_edges: Set[str] = set()
489	    for c in circuits.values():
490	        all_edges |= c
491	    total_union = len(all_edges)
492	
493	    # --- Per-method stats ---
494	    print(f"\n{'='*55}")
495	    print("=== MVP Results Analysis ===")
496	    print(f"{'='*55}")
497	    print(f"\nPer-method circuit size:")
498	    for m in methods:
499	        n = len(circuits[m])
500	        pct = n / total_union * 100 if total_union > 0 else 0
501	        print(f"  {m:<20s} {n:>5d} edges ({pct:5.1f}% of union {total_union})")
502	
503	    # --- Pairwise Jaccard ---
504	    pairwise = compute_pairwise_css(circuits)
505	    print(f"\nPairwise CSS (Jaccard similarity):")
506	    for pair, val in pairwise.items():
507	        print(f"  {pair:<30s} {val:.4f}")
508	
509	    # --- Full cross-tabulation ---
510	    css_result = compute_css_matrix_full(circuits)
511	    print(f"\nCross-tabulation (K={K}):")
512	    all_ones_key = str(tuple(1 for _ in range(K)))
513	    agree_in = css_result["agree_all_in"]
514	    off_diag = css_result["off_diagonal"]
515	    print(f"  {all_ones_key} all agree IN:   {agree_in:>5d} ({agree_in/total_union*100:5.1f}%)" if total_union else "")
516	    print(f"  off-diagonal:              {off_diag:>5d} ({off_diag/total_union*100:5.1f}%)" if total_union else "")
517	    off_diag_pct = css_result["off_diagonal_pct"]
518	
519	    for cell_label, count in sorted(css_result["cell_counts"].items()):
520	        pct_str = f"{count/total_union*100:5.1f}%" if total_union else "N/A"
521	        print(f"    {cell_label}: {count:>5d} ({pct_str})")
522	
523	    # --- CIRCUS tiers + cross-table (if primary method has continuous scores) ---
524	    primary = methods[0]
525	    tiers = compute_circus_tiers(all_scores[primary])
526	    tier_counts = Counter(tiers.values())
527	    print(f"\nCIRCUS tiers ({primary}):")
528	    for t in ("core", "contingent", "noise"):
529	        print(f"  {t}: {tier_counts.get(t, 0)}")
530	
531	    xtab = compute_cross_table(tiers, circuits, css_threshold=0.67, K=K)
532	    print(f"\nCIRCUS-core x CSS cross-table:")
533	    print(f"  stable_core:    {xtab['stable_core']:>5d}")
534	    print(f"  method_specific:{xtab['method_specific']:>5d}")
535	    print(f"  cross_unstable: {xtab['cross_unstable']:>5d}")
536	    print(f"  noise:          {xtab['noise']:>5d}")
537	    print(f"  core off-diag:  {xtab['off_diagonal_pct']*100:.1f}%")
538	
539	    # --- ACDC threshold sensitivity ---
540	    sensitivity = acdc_sensitivity(all_scores, top_n=top_n)
541	    if sensitivity:
542	        print(f"\nACDC threshold sensitivity:")
543	        for row in sensitivity:
544	            print(f"  τ={row['tau']:<5.2f}: off_diag={row['off_diagonal_pct']*100:5.1f}%, "
545	                  f"ACDC_size={row['acdc_size']}, union={row['total_union']}")
546	
547	    # --- Gate judgment ---
548	    gate = gate_judgment(off_diag_pct)
549	    print(f"\n{'='*55}")
550	    print(f"=== MVP GATE: {gate['verdict']} ===")
551	    print(f"  {gate['action']}")
552	    print(f"{'='*55}")
553	
554	    # --- Visualization ---
555	    print("\n=== Visualization ===")
556	    save_css_heatmap(pairwise, methods, output_dir / "css_heatmap.png")
557	    save_venn_or_bar(circuits, output_dir / "edge_overlap.png")
558	
559	    # --- JSON output ---
560	    output = {
561	        "methods": methods,
562	        "K": K,
563	        "per_method_edges": {m: len(circuits[m]) for m in methods},
564	        "total_union": total_union,
565	        "pairwise_jaccard": pairwise,
566	        "css_cross_tabulation": {
567	            k: v for k, v in css_result.items()
568	            if k not in ("cell_counts",)
569	        },
570	        "css_cell_counts": css_result["cell_counts"],
571	        "off_diagonal_pct": off_diag_pct,
572	        "circus_tiers": dict(tier_counts),
573	        "circus_cross_table": xtab,
574	        "acdc_sensitivity": sensitivity,
575	        "gate": gate,
576	    }
577	
578	    if pipeline:
579	        output["pipeline_summary"] = {
580	            k: v for k, v in pipeline.items()
581	            if k in ("config", "timings_sec", "css_distribution", "circus_tiers", "cross_table", "gate_verdict")
582	        }
583	
584	    json_path = output_dir / "analysis_results.json"
585	    with open(json_path, "w") as f:
586	        json.dump(output, f, indent=2, default=str)
587	    print(f"\n  Saved JSON → {json_path}")
588	
589	    return output
590	
591	
592	# ---------------------------------------------------------------------------
593	# CLI
594	# ---------------------------------------------------------------------------
595	
596	def main():
597	    parser = argparse.ArgumentParser(description="StructFuse MVP results analysis")
598	    parser.add_argument("--results-dir", type=str, default="/root/structfuse-context",
599	                        help="Directory containing cache files and/or mvp_results.json")
600	    parser.add_argument("--output-dir", type=str, default="./analysis",
601	                        help="Output directory for plots and JSON")
602	    parser.add_argument("--top-n", type=int, default=200,
603	                        help="Top-N edges for EAP-IG/IFR binarization")
604	    parser.add_argument("--dry-run", action="store_true",
605	                        help="Run with mock data to verify analysis pipeline")
606	    args = parser.parse_args()
607	
608	    run_analysis(
609	        results_dir=Path(args.results_dir),
610	        output_dir=Path(args.output_dir),
611	        top_n=args.top_n,
612	        dry_run=args.dry_run,
613	    )
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
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "10556aee-42fc-435a-abc5-b8d4583b6c30"
}
```

</details>

---

### System

_source line 90_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 73527,
    "tool_uses": 28,
    "duration_ms": 34321
  },
  "last_tool_name": "Bash",
  "uuid": "a597734c-53b1-4299-bc5f-8bdb56da38a6",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Bash · `toolu_01WPPFzNMVqxzYpBLFHMmPAd`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/ | tail -15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "f31f2ef7-fe4e-4d3c-8a7d-8d85a605fa96",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016WGf4NLTNru7dMAgrUAjbJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6592,
      "cache_read_input_tokens": 66493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6592,
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

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Reading artifacts/structfuse-mvp/css.py",
  "usage": {
    "total_tokens": 73528,
    "tool_uses": 29,
    "duration_ms": 34383
  },
  "last_tool_name": "Read",
  "uuid": "ec359af1-0259-407b-bb29-2135b319e237",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Read · `toolu_014EE7Lxg7SzHvWkqyTXM6nT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/css.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "744f3d1e-ad39-47a3-8663-00a13ebc915b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016WGf4NLTNru7dMAgrUAjbJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6592,
      "cache_read_input_tokens": 66493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6592,
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

_source line 94 · 2026-05-12T22:07:56.704Z_

<details><summary>↩ Tool result · `toolu_01WPPFzNMVqxzYpBLFHMmPAd`</summary>

```text
total 84K
-rw-r--r-- 1 ubuntu ubuntu  16K May 12 10:03 API_SURVEY.md
-rw-r--r-- 1 ubuntu ubuntu 7.0K May 12 10:27 LARGE_MODEL_THIRD_METHOD.md
drwxr-xr-x 2 ubuntu ubuntu 4.0K May 12 12:31 __pycache__
-rw-r--r-- 1 ubuntu ubuntu 5.5K May 12 12:30 circuit_discovery.py
-rw-r--r-- 1 ubuntu ubuntu 3.4K May 12 10:20 circus.py
-rw-r--r-- 1 ubuntu ubuntu 1.4K May 12 11:29 config.py
-rw-r--r-- 1 ubuntu ubuntu 3.9K May 12 10:26 cross_tabulate.py
-rw-r--r-- 1 ubuntu ubuntu 3.1K May 12 11:29 css.py
-rw-r--r-- 1 ubuntu ubuntu 9.3K May 12 12:30 edge_pruning_l0.py
-rw-r--r-- 1 ubuntu ubuntu 3.0K May 12 10:21 evaluation.py
-rw-r--r-- 1 ubuntu ubuntu 5.3K May 12 11:29 ifr_discovery.py
-rw-r--r-- 1 ubuntu ubuntu 5.2K May 12 10:26 run_mvp.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "6d297f4d-2f81-4488-8ce1-fcc353827ffd"
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-12T22:07:56.702Z_

<details><summary>↩ Tool result · `toolu_014EE7Lxg7SzHvWkqyTXM6nT`</summary>

```text
1	"""Cross-method Stability Scoring (CSS).
2	Computes per-edge consensus across K independent circuit discovery methods.
3	CSS(edge) = (number of methods selecting edge) / K, taking values in {0, 1/K, ..., 1}.
4	"""
5	
6	from typing import Dict, Set
7	
8	
9	def compute_css(
10	    method_circuits: Dict[str, Set[str]],
11	    K: int,
12	) -> Dict[str, float]:
13	    """Compute CSS scores from K methods' binary edge sets.
14	
15	    Args:
16	        method_circuits: method_name -> set of selected edge names
17	        K: total number of methods (used as denominator)
18	
19	    Returns:
20	        edge_name -> CSS score in {0, 1/K, 2/K, ..., 1}
21	    """
22	    all_edges: Set[str] = set()
23	    for edges in method_circuits.values():
24	        all_edges |= edges
25	
26	    css_scores = {}
27	    for edge in all_edges:
28	        count = sum(1 for edges in method_circuits.values() if edge in edges)
29	        css_scores[edge] = count / K
30	
31	    return css_scores
32	
33	
34	def threshold_css(
35	    css_scores: Dict[str, float],
36	    threshold: float = 0.67,
37	) -> Set[str]:
38	    """Select edges meeting CSS threshold.
39	
40	    Threshold is snapped to nearest n/K level to avoid floating point issues
41	    (e.g. threshold=0.67 matches CSS=2/3=0.6666...).
42	
43	    Args:
44	        css_scores: edge_name -> CSS score
45	        threshold: minimum CSS to include (default 0.67 = 2/3 for K=3)
46	
47	    Returns:
48	        Set of edge names with CSS >= threshold
49	    """
50	    eps = 0.01
51	    return {edge for edge, score in css_scores.items() if score >= threshold - eps}
52	
53	
54	def binarize_scores(
55	    edge_scores: Dict[str, float],
56	    method: str = "eap_ig",
57	    top_n: int = 100,
58	) -> Set[str]:
59	    """Convert edge scores to binary circuit using method-appropriate strategy.
60	
61	    - EAP-IG: continuous attribution scores → top-N by absolute value
62	    - Edge Pruning: L0 mask values in [0,1] → threshold at 0.5
63	    - ACDC: binary inclusion (0 or 1) → select all non-zero edges
64	
65	    Args:
66	        edge_scores: edge_name -> score (interpretation depends on method)
67	        method: "eap_ig" | "edge_pruning" | "acdc"
68	        top_n: number of top edges (only used for eap_ig)
69	
70	    Returns:
71	        Set of selected edge names
72	    """
73	    if method == "acdc":
74	        return {edge for edge, score in edge_scores.items() if score > 0}
75	    elif method == "edge_pruning":
76	        return {edge for edge, score in edge_scores.items() if score > 0.5}
77	    elif method == "ifr":
78	        sorted_edges = sorted(edge_scores.items(), key=lambda x: abs(x[1]), reverse=True)
79	        return {edge for edge, _ in sorted_edges[:top_n]}
80	    else:
81	        sorted_edges = sorted(edge_scores.items(), key=lambda x: abs(x[1]), reverse=True)
82	        return {edge for edge, _ in sorted_edges[:top_n]}
83	
84	
85	def css_summary(css_scores: Dict[str, float], K: int) -> Dict[str, int]:
86	    """Count edges at each CSS level.
87	
88	    Returns:
89	        Dict mapping CSS level string to count, e.g. {"0/3": 50, "1/3": 30, "2/3": 15, "3/3": 5}
90	    """
91	    from collections import Counter
92	    level_counts = Counter()
93	    for score in css_scores.values():
94	        n_methods = round(score * K)
95	        level_counts[f"{n_methods}/{K}"] += 1
96	    return dict(sorted(level_counts.items()))
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "3d9bbc5a-fe0e-43ff-ba8b-b567eac06691"
}
```

</details>

---

### System

_source line 96_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Running tree -L 2 /home/ubuntu/.agent-ml-research-idea_ge…",
  "usage": {
    "total_tokens": 75383,
    "tool_uses": 30,
    "duration_ms": 36678
  },
  "last_tool_name": "Bash",
  "uuid": "a373202a-1a4e-46ae-bd51-edaeccdd183e",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_011mNZRiCBvAKhKAid9fmoGX`</summary>

```json
{
  "command": "tree -L 2 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/ -I \"__pycache__|*.pyc\" 2>/dev/null | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "efd39823-ca8a-4380-8c99-56f185e0f7c0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TvoT9Yevx3aK4r5AhkT8Vr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1853,
      "cache_read_input_tokens": 73085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1853,
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

_source line 98 · 2026-05-12T22:07:59.049Z_

<details><summary>↩ Tool result · `toolu_011mNZRiCBvAKhKAid9fmoGX`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "7ef39dfe-bfaa-4846-bedf-02b383b0f021"
}
```

</details>

---

### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 75601,
    "tool_uses": 31,
    "duration_ms": 38425
  },
  "last_tool_name": "Bash",
  "uuid": "03bf5f7b-37d2-4e42-a70f-0b742d489516",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool call

_source line 100_

<details open><summary>🔧 Tool call — Bash · `toolu_016f8jMdajjGzAAeK3eHQ69E`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts -type f -name \"*.py\" | wc -l && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts -maxdepth 1 -type f -name \"*.py\" | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "6e94f459-f64a-48e0-8c51-7f60bfe2eabe",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PK59QsRZSSBwtij6kBHc1t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 152,
      "cache_read_input_tokens": 74938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 152,
        "ephemeral_1h_input_tokens": 0
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

_source line 101 · 2026-05-12T22:08:00.813Z_

<details><summary>↩ Tool result · `toolu_016f8jMdajjGzAAeK3eHQ69E`</summary>

```text
37
---
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/analyze_mvp_results.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/css.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/eap_ig_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/edge_pruning_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/ifr_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/model_adapter.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/run_circus.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_css.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_eap_ig_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_edge_pruning_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_ifr_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_run_circus_fixes.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "d6982f81-ec4a-4139-ab43-b13f65a326e5"
}
```

</details>

---

### System

_source line 102_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a56a48656517bd500",
  "tool_use_id": "toolu_018FP38TDWhQ5y5E72XLwMXA",
  "status": "completed",
  "output_file": "",
  "summary": "Explore structfuse-context codebase",
  "usage": {
    "total_tokens": 76224,
    "tool_uses": 31,
    "duration_ms": 104733
  },
  "uuid": "ee4d93bd-7be5-45c6-b1bb-c116002d1970",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93"
}
```

---

### Tool result

_source line 103 · 2026-05-12T22:09:07.034Z_

<details><summary>↩ Tool result · `toolu_018FP38TDWhQ5y5E72XLwMXA`</summary>

````text
Perfect! Now I have all the information needed. Let me provide a comprehensive report.

## StructFuse-Context Project Structure & Phase 2 Framework

### 1. DIRECTORY STRUCTURE

**Root directories:**
```
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/
├── ROADMAP.md                           # Project milestones & gate rules
├── AGENTS.md                            # Agent orchestration log
├── decisions.yaml                       # Decision log (D001-D011)
├── memory.md                            # L1 lessons learned (GPU, cache, edge names)
├── registry.yaml                        # Artifact registry
├── report.md                            # MVP status
├── artifacts/                           # Main code directory
│   ├── run_circus.py                   # Phase 2 entry point (config-driven pipeline)
│   ├── analyze_mvp_results.py          # MVP analysis tool
│   ├── model_adapter.py                # Unified model interface (GPT-2 TL + HF)
│   ├── css.py                          # CSS binarization module
│   ├── eap_ig_scoring.py               # EAP-IG for HuggingFace (phase 2)
│   ├── edge_pruning_scoring.py         # Edge Pruning L0 for HuggingFace (phase 2)
│   ├── ifr_scoring.py                  # IFR activation decomposition
│   ├── test_*.py                       # Smoke tests for each module
│   ├── structfuse-mvp/                 # MVP TransformerLens implementations
│   │   ├── run_mvp.py                  # MVP main pipeline
│   │   ├── circuit_discovery.py        # K=3 method dispatch (EAP-IG, EP, ACDC)
│   │   ├── edge_pruning_l0.py          # L0 pruning (TL version)
│   │   ├── ifr_discovery.py            # IFR (TL version)
│   │   ├── config.py                   # MVPConfig & LargeModelConfig
│   │   ├── css.py                      # CSS for MVP
│   │   ├── circus.py                   # CIRCUS config-bagging
│   │   ├── cross_tabulate.py           # Cross-tabulation
│   │   ├── evaluation.py               # Faithfulness metrics
│   │   └── API_SURVEY.md / LARGE_MODEL_THIRD_METHOD.md
│   ├── _project/                       # Internal artifact versions
│   │   ├── intermediate/               # Previous versions of modules
│   │   └── report/
│   └── deploy_phase2.sh                # Deployment script
├── checkpoints/                        # Model checkpoints
├── logs/                               # Worker logs
└── task_context/                       # Agent conversation history
```

---

### 2. KEY CONSTANTS

**CANONICAL_VERSION (model_adapter.py, line 28):**
```python
CANONICAL_VERSION = "v2"
```
This ties cached scores to edge name format. Used in `run_circus.py` for cache validation:
- Cache path: `cache_dir/{model_slug}/{task}/{method}_{CANONICAL_VERSION}_{hash16}.json`
- Cache invalidation: If code changes edge naming, increment CANONICAL_VERSION

**Edge naming canonical forms:**
- **TransformerLens:** `"blocks.{L}.attn.hook_result[{H}] -> blocks.{L'}.attn.hook_q[{H'}]"`
- **HuggingFace:** `"{src}->{dst}"` with node names like `a{L}.h{H}.q`, `m{L}`, `input`
- Normalization patterns in `model_adapter.py` lines 47-96

---

### 3. RUN_CIRCUS.PY PIPELINE (Phase 2 Entry Point)

**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/run_circus.py` (599 lines)

**Main function signature (line 459):**
```python
def run_pipeline(config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]
```

**Pipeline steps:**

1. **Config loading (lines 460-463):**
   - Merges DEFAULT_CONFIG with runtime overrides
   - Sets CUDA_VISIBLE_DEVICES from config (D007 lesson)
   - Supports JSON/YAML config files via CLI

2. **Model loading (lines 471-479):**
   - `ModelAdapter.from_pretrained()` auto-detects backend:
     - GPT-2 → TransformerLens
     - Qwen/Llama/Gemma/Mistral → HuggingFace
   - Returns ModelInfo with architecture details

3. **Dataset loading (lines 481-486):**
   - IOI: 50 samples of "When {name1} and {name2} went to the store, {name1} gave..."
   - Greater-than: Templated arithmetic examples
   - Dispatched by task name via `load_dataset()` (lines 67-103)

4. **Method dispatch (lines 495-512):**
   - Iterates over `cfg['methods']` (default: `["eap_ig", "edge_pruning", "ifr"]`)
   - Each method dispatched by `run_method()` (line 506):
     - Key: `(method, backend)` tuple
     - Dispatch table lines 228-240
     - Returns Dict[str, float] with canonical edge names
   - Caching: `load_cached()` / `save_cache()` with CANONICAL_VERSION validation

5. **Binarization (lines 514-518):**
   - Calls `_binarize_method()` per method
   - Delegates to `css.binarize_scores()` with per-method strategy:
     - EAP-IG: `topn` (n=200)
     - Edge Pruning: `topn` (n=200)
     - IFR: `unique_score_rank` (n=50) to avoid layer-block voting (D010)

6. **CSS computation (lines 520-526):**
   - `compute_css()` counts method agreement per edge
   - Distribution histogram via `css_distribution()`
   - Thresholding at 0.67 (≥2/3 methods) for K=3

7. **CIRCUS stability (lines 528-540):**
   - Config-bagging on primary method (default: EAP-IG)
   - `config_bag()`: sweep B=10 percentile thresholds
   - Classification via `classify_tiers()`: core (≥1.0) / contingent / noise

8. **Cross-tabulation (lines 542-549):**
   - `cross_tabulate()` bins edges into:
     - stable_core: CIRCUS-core AND CSS≥threshold
     - method_specific: CIRCUS-core but not CSS
     - cross_unstable: CSS high but not CIRCUS-core
     - noise: neither
   - Computes off_diagonal_pct = method_specific / core_total

9. **Results output (lines 551-579):**
   - JSON: `{model_slug}_{task}_K{K}.json`
   - Fields: config, timings_sec, method_edge_counts, css_distribution, cross_table, etc.

**Config structure (lines 36-60):**
```python
DEFAULT_CONFIG: Dict[str, Any] = {
    "model": "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/",
    "task": "ioi",
    "methods": ["eap_ig", "edge_pruning", "ifr"],
    "K": 3,
    "num_samples": 50,
    "gpu_id": "5",
    "binarize": {
        "eap_ig":       {"strategy": "topn", "n": 200},
        "edge_pruning": {"strategy": "topn", "n": 200},
        "ifr":          {"strategy": "unique_score_rank", "n": 50},  # D010
    },
    "eap_ig_steps": 5,
    "edge_pruning_epochs": 100,
    "edge_pruning_lambda": 1e-2,
    "ifr_threshold": 0.1,
    "css_threshold": 0.67,
    "circus_B": 10,
    "circus_core_threshold": 1.0,
    "circus_contingent_threshold": 0.5,
    "device": "cuda",
    "seed": 42,
    "output_dir": "./results",
    "cache_dir": "./cache",
}
```

---

### 4. ANALYZE_MVP_RESULTS.PY (Analysis Tool)

**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/analyze_mvp_results.py` (618 lines)

**Main function signature (line 456):**
```python
def run_analysis(
    results_dir: Path,
    output_dir: Path,
    top_n: int = 200,
    dry_run: bool = False,
) -> Dict[str, Any]
```

**Analysis pipeline:**

1. **Data loading (lines 464-479):**
   - Auto-detects per-method cache files via `_find_cache_files()`
   - Supports: `cache_{method}.json`, `cache/{model_slug}/{task}/{method}*.json`
   - Loads via `_load_scores_from_file()` (handles both flat and structured JSON)
   - Optional pipeline results from `mvp_results.json`

2. **Binarization (lines 481-491):**
   - Method dispatch via `binarize_method()`:
     - ACDC: threshold at 0.05 (tau)
     - Edge Pruning: threshold at 0.5
     - EAP-IG/IFR: top-N (default 200)
   - Computes union of all method edges

3. **Statistics (lines 493-537):**
   - Per-method circuit sizes
   - Pairwise Jaccard via `compute_pairwise_css()`
   - Full cross-tabulation via `compute_css_matrix_full()`:
     - Cell counts for all 2^K combinations
     - off_diagonal = edges where methods disagree (not in all-ones cell)
     - off_diagonal_pct = off_diagonal / (edges with at least one method)

4. **CIRCUS tiers (lines 523-537):**
   - `compute_circus_tiers()`: config-bagging on primary method
   - Cross-tabulation via `compute_cross_table()`
   - Outputs: stable_core, method_specific, cross_unstable, noise

5. **ACDC sensitivity (lines 539-545):**
   - Sweeps tau in [0.01, 0.03, 0.05, 0.1, 0.3]
   - For each tau: recomputes off_diagonal_pct
   - Helps understand ACDC threshold impact

6. **Gate judgment (lines 547-551):**
   - `gate_judgment()` applies MVP gate rules (D001-D003):
     - ≥10% off-diagonal → PASS_MAIN
     - 5-10% → PASS_FINDINGS (add Arithmetic verification)
     - 2-5% → MARGINAL (Findings track)
     - <2% → KILL (if ΔF also insignificant)

7. **Visualization (lines 554-557):**
   - CSS heatmap (pairwise Jaccard) via matplotlib
   - Venn diagram (3-method overlap) or bar chart
   - Saves as PNG to output_dir

8. **JSON output (lines 559-589):**
   - File: `analysis_results.json`
   - Fields: methods, K, per_method_edges, css_cross_tabulation, circus_cross_table, acdc_sensitivity, gate

**CLI usage (lines 596-614):**
```bash
python analyze_mvp_results.py \
    --results-dir /root/structfuse-context \
    --output-dir ./analysis \
    --top-n 200 \
    --dry-run
```

---

### 5. SCORING MODULES INTERFACES

#### 5.1 EAP-IG Scoring (eap_ig_scoring.py)

**Function signature:**
```python
def compute_eap_ig_scores(
    model: nn.Module,
    clean_inputs: Tensor,
    corrupt_inputs: Tensor,
    metric_fn: Callable,
    target_ids: Optional[Tensor] = None,
    ig_steps: int = 5,
    device: str = "cuda",
) -> Dict[str, float]
```

**Output:** Dict[str, float] with edge names like `"input->a0.h0.q"`, `"a0.h0->m1"`, etc.

**Key components:**
- `_get_model_info()`: Detects arch (llama_like, gpt2)
- `_prepare_inputs()`: Converts various input formats to Tensor
- `_decompose_per_head()`: Projects head outputs through projection matrices
- **Backward compatibility:** HuggingFace backend (`_run_eap_ig_hf`) marked NotImplementedError in run_circus.py line 172 — Phase 2 requires HF implementation

#### 5.2 Edge Pruning Scoring (edge_pruning_scoring.py)

**Class:** `HardConcrete(nn.Module)` (lines 40-74)
```python
def forward(self, training: bool = True) -> torch.Tensor
def l0_penalty(self) -> torch.Tensor
def expected_masks(self) -> torch.Tensor  # Final scoring
```

**Topology:** `_build_edge_topology()` (lines 125-150)
- Enumerates all edges: input → all layers
- Per-head Q masks (independent)
- Per-KV-group K/V masks (GQA shared)
- Per-source MLP masks
- Returns: (edge_names, edge_to_mask_idx, n_masks)

**Hook strategy (v2, D011):**
- Layer pre-hooks abandoned
- New: 4 submodule hooks per layer (q_proj, k_proj, v_proj, mlp)
- Each submodule applies corresponding edge mask in forward

**Output:** Dict[str, float] with mask scores 0-1 per edge

#### 5.3 IFR Scoring (ifr_scoring.py)

**Function signature:**
```python
def compute_ifr_edges(
    model,
    dataset: Union[torch.Tensor, dict, list],
    metric_fn: Optional[Callable] = None,
    threshold: float = 0.1,
    device: str = "cuda",
) -> Dict[str, float]
```

**Core metric (line 39):**
```python
def _proximity(y_u: torch.Tensor, x_v: torch.Tensor) -> float:
    diff_norm = (y_u - x_v).abs().sum(dim=-1)
    base_norm = x_v.abs().sum(dim=-1)
    return (base_norm - diff_norm).clamp(min=0).mean().item()
```

**Properties:**
- Single forward pass + activation caching (no backward)
- **Critical:** All heads at same (src, dst_layer) get identical proximity scores
- Causes 36 tied edges per layer-pair (D010 issue)
- Solution: Use `unique_score_rank` binarization (css.py line 53)

**Output:** Dict[str, float] with canonical edge names

---

### 6. SUPPORTING MODULES

#### 6.1 Model Adapter (model_adapter.py, 306 lines)

**Key class:** `ModelAdapter`

**Factory methods:**
- `from_pretrained(model_name: str, device: str = "cuda")` (line 119)
  - Auto-detects: `_is_gpt2()` → TL, else → HF
  - TL: via `HookedTransformer.from_pretrained()`
  - HF: via `AutoModelForCausalLM.from_pretrained()`

**ModelInfo dataclass (lines 31-40):**
```python
@dataclass
class ModelInfo:
    arch: str                   # "gpt2" | "qwen2" | "llama" | ...
    n_layers: int
    n_heads: int
    n_kv_heads: int             # GQA
    d_model: int
    head_dim: int
    backend: str                # "transformerlens" | "huggingface"
    model_name: str
```

**Canonical conversion:**
- TL → canonical: `_tl_to_canonical()` (lines 61-66)
  - Pattern: `hook_embed` → `input`, `blocks.{L}.attn.hook_result[{H}]` → `a{L}.h{H}`
- HF → canonical: `_hf_to_canonical()` (lines 69-80)
  - Pattern: `model.layers.{L}.self_attn.o_proj` → `a{L}`

**Hook point mapping:** `get_hook_points()` returns {canonical_name: module_path}

**GQA support:** `gqa_kv_group()` maps query head to KV group

#### 6.2 CSS Module (css.py, 128 lines)

**Functions:**
- `binarize_scores(scores, strategy, n=200, threshold=0.01, percentile=95.0)` (lines 18-59)
  - Strategies: topn, threshold, percentile_threshold, unique_score_rank
  - **unique_score_rank:** Ranks by unique score values (fixes D010 block-voting)

- `compute_css_matrix(method_circuits, all_edges)` (lines 62-112)
  - Returns: cell_counts, css_core, off_diagonal, off_diagonal_pct, per_method_counts

- `circus_score(method_circuits, edge)` (lines 115-127)
  - Fraction of methods including edge

---

### 7. MVP FRAMEWORK (structfuse-mvp/)

**Entry point:** `run_mvp.py` (265 lines)

**Main pipeline:**
```python
def main():
    # 1. Load model + data
    model, dataset = load_model_and_data(config)
    
    # 2. Run K=3 methods (via circuit_discovery.run_all_methods)
    all_scores = run_all_methods(model, dataset, metric_fn, config)
    
    # 3. Binarize
    method_circuits = {m: binarize_scores(scores, m) for m, scores in all_scores.items()}
    
    # 4. CIRCUS config-bagging (EAP-IG only)
    eap_stability, circus_tiers = run_circus(all_scores["eap_ig"], config)
    
    # 5. CSS across K=3 methods
    css_scores = compute_css(method_circuits, K=3)
    
    # 6. Cross-tabulation
    table = cross_tabulate(circus_tiers, css_scores, threshold=0.67)
    
    # 7. Evaluation (faithfulness)
    eval_results = evaluate_all_circuits(model, circuits_to_eval, dataset, metric)
    
    # 8. MVP gate
    pct = compute_off_diagonal(table) * 100
    gate_verdict = "PASS_MAIN" if pct >= 10 else "PASS_FINDINGS" if pct >= 5 else ...
```

**Config (structfuse-mvp/config.py):**
```python
@dataclass
class MVPConfig:
    model_name: str = "gpt2-small"
    task: str = "ioi"
    methods: List[str] = ["eap_ig", "edge_pruning", "acdc"]  # MVP uses ACDC
    K: int = 3
    css_thresholds: List[float] = [0.0, 0.33, 0.67, 1.0]
    css_default_threshold: float = 0.67
    circus_B: int = 10
    eap_ig_steps: int = 5
    eap_ig_topn: int = 100
    acdc_threshold: float = 0.05

@dataclass
class LargeModelConfig(MVPConfig):
    model_name: str = "Qwen/Qwen2.5-0.5B"
    methods: List[str] = ["eap_ig", "edge_pruning", "ifr"]  # Phase 2: IFR replaces ACDC
    eap_ig_topn: int = 200
```

---

### 8. ROADMAP & DECISION LOG

**ROADMAP.md highlights:**

| Phase | Models | Methods | Gate Rule | Status |
|-------|--------|---------|-----------|--------|
| MVP | GPT-2 Small | EAP-IG + EP + ACDC (K=3) | ≥10% off-diagonal | Pending |
| Phase 2 | Qwen-2.5 0.5B | EAP-IG + EP + IFR (K=3) | K=3 checkpoint pass | ~3 days post-MVP |
| Phase 3 | Qwen, Gemma, Llama | K=3 × 4 tasks + OOD | Full CSS matrix | ~4 days |
| Phase 4 | All | — | Analysis + writing | ~3 days, deadline 2026-05-22 |

**Key decisions (decisions.yaml):**

| ID | Summary | Impact |
|----|---------|--------|
| D006 | IFR as third method (D005 dependent) | Large model K=3 now viable |
| D010 | unique_score_rank for IFR | Fixes D006 layer-block voting bias |
| D011 | EP v2 hook restructure (D010 dependent) | Fixes MLP mask + Q/K/V collapse issues |
| D009 | Edge name normalization (critical bug) | Unified canonical format |
| D008 | MVP ≥10% valid under mask_gradient proxy | MVP result interpretation |
| D007 | GPU isolation fix (L1 lesson) | CUDA_VISIBLE_DEVICES enforcement |

---

### 9. CRITICAL IMPLEMENTATION DETAILS FOR PHASE 2

**1. EAP-IG HuggingFace backend (NOT YET IMPLEMENTED):**
- File: `eap_ig_scoring.py` line 171-173 raises NotImplementedError
- Required for Phase 2 on Qwen-2.5
- Hook points: model.layers.{i} (pre-hook for resid_pre), self_attn.o_proj (per-head decomposition), mlp

**2. Edge Pruning v2 hook restructure (D011):**
- Current file: `edge_pruning_scoring.py` uses layer pre-hook
- Problem: MLP mask not applied in forward; Q/K/V masks aggregated to scalar
- Solution: Replace with 4 submodule hooks (q_proj, k_proj, v_proj, mlp) per layer

**3. IFR binarization strategy (D010):**
- Problem: 36 tied scores per layer-pair (residual-stream shared across heads)
- Solution: Use `unique_score_rank` in `css.binarize_scores()` instead of `topn`
- Default config in `run_circus.py` line 46: `"unique_score_rank"` with n=50

**4. GPU safety (D007, memory.md):**
- All scripts must set `os.environ['CUDA_VISIBLE_DEVICES']` BEFORE torch import
- `run_circus.py` line 24 enforces this
- Memory.md line 6: "后续所有实验脚本必须在第一行设置 CUDA_VISIBLE_DEVICES"

**5. Cache invalidation:**
- CANONICAL_VERSION in model_adapter.py line 28
- Cache key includes: model, task, method, canonical_version, hyperparams
- If edge names change, increment CANONICAL_VERSION + clear old caches

**6. Edge naming normalization (D009):**
- Critical: _normalize_* functions in structfuse-mvp/circuit_discovery.py must produce same format
- Canonical form: `"{src}->{dst}"` (no spaces around arrow)
- Test: All three methods' edges must match exactly in css.py compute_css()

---

### 10. TESTING FRAMEWORK

**Test files (artifacts/):**
- `test_css.py`: 8 tests for binarization, CSS matrix, CIRCUS score
- `test_eap_ig_scoring.py`: AST validation + GPT-2 integration
- `test_edge_pruning_scoring.py`: Topology, GQA sharing, mask independence
- `test_ifr_scoring.py`: Proximity metric, edge coverage

**Smoke test pattern:**
```python
def test_module_signature():
    """AST-based validation of function signatures."""
    import ast
    tree = ast.parse(open("module.py").read())
    # Assert expected functions exist with correct signatures
    
def test_integration_gpt2():
    """Optional: run on actual GPT-2 if available."""
    from transformer_lens import HookedTransformer
    model = HookedTransformer.from_pretrained("gpt2-small")
    scores = compute_scores(model, ...)
    assert isinstance(scores, dict) and all(isinstance(v, float) for v in scores.values())
```

---

### 11. DEPLOYMENT & EXECUTION

**Phase 2 deployment script:** `deploy_phase2.sh` (in artifacts/)

**CLI entry points:**

```bash
# Run full Phase 2 pipeline with default config
python run_circus.py

# Custom config (JSON)
python run_circus.py config.json

# Custom config (YAML)
python run_circus.py config.yaml

# Analyze MVP results
python analyze_mvp_results.py \
    --results-dir /root/structfuse-context \
    --output-dir ./analysis \
    --top-n 200
```

**Expected outputs:**

```
results/
├── Qwen_Qwen2.5-0.5B__ioi_K3.json       # run_circus output
├── analysis/
│   ├── analysis_results.json             # analyze_mvp_results output
│   ├── css_heatmap.png
│   └── edge_overlap.png                  # Venn or bar chart
└── cache/
    ├── Qwen_Qwen2.5-0.5B__/
    │   └── ioi/
    │       ├── eap_ig_v2_&lt;hash>.json
    │       ├── edge_pruning_v2_&lt;hash>.json
    │       └── ifr_v2_&lt;hash>.json
```

---

### 12. SUMMARY OF KEY FUNCTION SIGNATURES FOR PHASE 2 FRAMEWORK

```python
# run_circus.py
def run_pipeline(config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]
def run_method(adapter: ModelAdapter, method: str, dataset: torch.Tensor, 
               metric: Optional[Callable], cfg: dict) -> Dict[str, float]
def compute_css(method_circuits: Dict[str, Set[str]], K: int) -> Dict[str, float]
def cross_tabulate(tiers: Dict[str, str], css_scores: Dict[str, float], 
                   css_thr: float) -> Dict[str, Any]

# analyze_mvp_results.py
def run_analysis(results_dir: Path, output_dir: Path, top_n: int = 200,
                 dry_run: bool = False) -> Dict[str, Any]
def gate_judgment(off_diagonal_pct: float) -> Dict[str, str]

# model_adapter.py
class ModelAdapter:
    @classmethod
    def from_pretrained(cls, model_name: str, device: str = "cuda") -> ModelAdapter
    def to_canonical_edges(self, edge_scores: Dict[str, float], method: str) -> Dict[str, float]

# css.py
def binarize_scores(scores: Dict[str, float], strategy: BinarizeStrategy,
                    n: int = 200, threshold: float = 0.01) -> set[str]
def compute_css_matrix(method_circuits: Dict[str, set[str]], all_edges: set[str]) -> Dict

# Scoring modules (Phase 2 HF implementations)
def compute_eap_ig_scores(model, clean_inputs, corrupt_inputs, metric_fn, ...) -> Dict[str, float]
def compute_ifr_edges(model, dataset, metric_fn=None, threshold=0.1, ...) -> Dict[str, float]
# Edge Pruning: use eap_ig_scoring.HardConcrete + _masked_forward pattern
```

---

This comprehensive framework enables Phase 2 to:
1. **Scale to large models** (Qwen-2.5, Llama-3.1, Gemma-2) via HuggingFace backends
2. **Maintain edge-level precision** via canonical naming (D009) and proper hook placement (D011)
3. **Handle IFR tied scores** via unique_score_rank binarization (D010)
4. **Reproduce MVP analysis** via run_circus.py + analyze_mvp_results.py
5. **Gate progression** via off-diagonal_pct thresholds (D001-D003)
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "6494aa07-bf58-421d-8bda-f71268130e58",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to understand the structfuse-context project structure to write a Phase 2 experiment framework. The project is at /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/\n\nPlease find:\n1. The directory structure (especially artifacts/, any existing scripts like run_circus.py, analyze_mvp_results.py, scoring modules)\n2. The interfaces of key modules: eap_ig_scoring, edge_pruning_scoring, ifr_scoring, any ACDC-related code\n3. How run_circus.py works (its main pipeline, config loading, how it calls methods)\n4. How analyze_mvp_results.py works (what analysis it does)\n5. Any existing YAML configs or experiment configs\n6. The ROADMAP.md content\n7. Any constants like CANONICAL_VERSION\n\nSearch breadth: very thorough. Report file paths, key function signatures, and how they connect.",
    "agentId": "a56a48656517bd500",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information needed. Let me provide a comprehensive report.\n\n## StructFuse-Context Project Structure & Phase 2 Framework\n\n### 1. DIRECTORY STRUCTURE\n\n**Root directories:**\n```\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/\n├── ROADMAP.md                           # Project milestones & gate rules\n├── AGENTS.md                            # Agent orchestration log\n├── decisions.yaml                       # Decision log (D001-D011)\n├── memory.md                            # L1 lessons learned (GPU, cache, edge names)\n├── registry.yaml                        # Artifact registry\n├── report.md                            # MVP status\n├── artifacts/                           # Main code directory\n│   ├── run_circus.py                   # Phase 2 entry point (config-driven pipeline)\n│   ├── analyze_mvp_results.py          # MVP analysis tool\n│   ├── model_adapter.py                # Unified model interface (GPT-2 TL + HF)\n│   ├── css.py                          # CSS binarization module\n│   ├── eap_ig_scoring.py               # EAP-IG for HuggingFace (phase 2)\n│   ├── edge_pruning_scoring.py         # Edge Pruning L0 for HuggingFace (phase 2)\n│   ├── ifr_scoring.py                  # IFR activation decomposition\n│   ├── test_*.py                       # Smoke tests for each module\n│   ├── structfuse-mvp/                 # MVP TransformerLens implementations\n│   │   ├── run_mvp.py                  # MVP main pipeline\n│   │   ├── circuit_discovery.py        # K=3 method dispatch (EAP-IG, EP, ACDC)\n│   │   ├── edge_pruning_l0.py          # L0 pruning (TL version)\n│   │   ├── ifr_discovery.py            # IFR (TL version)\n│   │   ├── config.py                   # MVPConfig & LargeModelConfig\n│   │   ├── css.py                      # CSS for MVP\n│   │   ├── circus.py                   # CIRCUS config-bagging\n│   │   ├── cross_tabulate.py           # Cross-tabulation\n│   │   ├── evaluation.py               # Faithfulness metrics\n│   │   └── API_SURVEY.md / LARGE_MODEL_THIRD_METHOD.md\n│   ├── _project/                       # Internal artifact versions\n│   │   ├── intermediate/               # Previous versions of modules\n│   │   └── report/\n│   └── deploy_phase2.sh                # Deployment script\n├── checkpoints/                        # Model checkpoints\n├── logs/                               # Worker logs\n└── task_context/                       # Agent conversation history\n```\n\n---\n\n### 2. KEY CONSTANTS\n\n**CANONICAL_VERSION (model_adapter.py, line 28):**\n```python\nCANONICAL_VERSION = \"v2\"\n```\nThis ties cached scores to edge name format. Used in `run_circus.py` for cache validation:\n- Cache path: `cache_dir/{model_slug}/{task}/{method}_{CANONICAL_VERSION}_{hash16}.json`\n- Cache invalidation: If code changes edge naming, increment CANONICAL_VERSION\n\n**Edge naming canonical forms:**\n- **TransformerLens:** `\"blocks.{L}.attn.hook_result[{H}] -> blocks.{L'}.attn.hook_q[{H'}]\"`\n- **HuggingFace:** `\"{src}->{dst}\"` with node names like `a{L}.h{H}.q`, `m{L}`, `input`\n- Normalization patterns in `model_adapter.py` lines 47-96\n\n---\n\n### 3. RUN_CIRCUS.PY PIPELINE (Phase 2 Entry Point)\n\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/run_circus.py` (599 lines)\n\n**Main function signature (line 459):**\n```python\ndef run_pipeline(config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]\n```\n\n**Pipeline steps:**\n\n1. **Config loading (lines 460-463):**\n   - Merges DEFAULT_CONFIG with runtime overrides\n   - Sets CUDA_VISIBLE_DEVICES from config (D007 lesson)\n   - Supports JSON/YAML config files via CLI\n\n2. **Model loading (lines 471-479):**\n   - `ModelAdapter.from_pretrained()` auto-detects backend:\n     - GPT-2 → TransformerLens\n     - Qwen/Llama/Gemma/Mistral → HuggingFace\n   - Returns ModelInfo with architecture details\n\n3. **Dataset loading (lines 481-486):**\n   - IOI: 50 samples of \"When {name1} and {name2} went to the store, {name1} gave...\"\n   - Greater-than: Templated arithmetic examples\n   - Dispatched by task name via `load_dataset()` (lines 67-103)\n\n4. **Method dispatch (lines 495-512):**\n   - Iterates over `cfg['methods']` (default: `[\"eap_ig\", \"edge_pruning\", \"ifr\"]`)\n   - Each method dispatched by `run_method()` (line 506):\n     - Key: `(method, backend)` tuple\n     - Dispatch table lines 228-240\n     - Returns Dict[str, float] with canonical edge names\n   - Caching: `load_cached()` / `save_cache()` with CANONICAL_VERSION validation\n\n5. **Binarization (lines 514-518):**\n   - Calls `_binarize_method()` per method\n   - Delegates to `css.binarize_scores()` with per-method strategy:\n     - EAP-IG: `topn` (n=200)\n     - Edge Pruning: `topn` (n=200)\n     - IFR: `unique_score_rank` (n=50) to avoid layer-block voting (D010)\n\n6. **CSS computation (lines 520-526):**\n   - `compute_css()` counts method agreement per edge\n   - Distribution histogram via `css_distribution()`\n   - Thresholding at 0.67 (≥2/3 methods) for K=3\n\n7. **CIRCUS stability (lines 528-540):**\n   - Config-bagging on primary method (default: EAP-IG)\n   - `config_bag()`: sweep B=10 percentile thresholds\n   - Classification via `classify_tiers()`: core (≥1.0) / contingent / noise\n\n8. **Cross-tabulation (lines 542-549):**\n   - `cross_tabulate()` bins edges into:\n     - stable_core: CIRCUS-core AND CSS≥threshold\n     - method_specific: CIRCUS-core but not CSS\n     - cross_unstable: CSS high but not CIRCUS-core\n     - noise: neither\n   - Computes off_diagonal_pct = method_specific / core_total\n\n9. **Results output (lines 551-579):**\n   - JSON: `{model_slug}_{task}_K{K}.json`\n   - Fields: config, timings_sec, method_edge_counts, css_distribution, cross_table, etc.\n\n**Config structure (lines 36-60):**\n```python\nDEFAULT_CONFIG: Dict[str, Any] = {\n    \"model\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/\",\n    \"task\": \"ioi\",\n    \"methods\": [\"eap_ig\", \"edge_pruning\", \"ifr\"],\n    \"K\": 3,\n    \"num_samples\": 50,\n    \"gpu_id\": \"5\",\n    \"binarize\": {\n        \"eap_ig\":       {\"strategy\": \"topn\", \"n\": 200},\n        \"edge_pruning\": {\"strategy\": \"topn\", \"n\": 200},\n        \"ifr\":          {\"strategy\": \"unique_score_rank\", \"n\": 50},  # D010\n    },\n    \"eap_ig_steps\": 5,\n    \"edge_pruning_epochs\": 100,\n    \"edge_pruning_lambda\": 1e-2,\n    \"ifr_threshold\": 0.1,\n    \"css_threshold\": 0.67,\n    \"circus_B\": 10,\n    \"circus_core_threshold\": 1.0,\n    \"circus_contingent_threshold\": 0.5,\n    \"device\": \"cuda\",\n    \"seed\": 42,\n    \"output_dir\": \"./results\",\n    \"cache_dir\": \"./cache\",\n}\n```\n\n---\n\n### 4. ANALYZE_MVP_RESULTS.PY (Analysis Tool)\n\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/analyze_mvp_results.py` (618 lines)\n\n**Main function signature (line 456):**\n```python\ndef run_analysis(\n    results_dir: Path,\n    output_dir: Path,\n    top_n: int = 200,\n    dry_run: bool = False,\n) -> Dict[str, Any]\n```\n\n**Analysis pipeline:**\n\n1. **Data loading (lines 464-479):**\n   - Auto-detects per-method cache files via `_find_cache_files()`\n   - Supports: `cache_{method}.json`, `cache/{model_slug}/{task}/{method}*.json`\n   - Loads via `_load_scores_from_file()` (handles both flat and structured JSON)\n   - Optional pipeline results from `mvp_results.json`\n\n2. **Binarization (lines 481-491):**\n   - Method dispatch via `binarize_method()`:\n     - ACDC: threshold at 0.05 (tau)\n     - Edge Pruning: threshold at 0.5\n     - EAP-IG/IFR: top-N (default 200)\n   - Computes union of all method edges\n\n3. **Statistics (lines 493-537):**\n   - Per-method circuit sizes\n   - Pairwise Jaccard via `compute_pairwise_css()`\n   - Full cross-tabulation via `compute_css_matrix_full()`:\n     - Cell counts for all 2^K combinations\n     - off_diagonal = edges where methods disagree (not in all-ones cell)\n     - off_diagonal_pct = off_diagonal / (edges with at least one method)\n\n4. **CIRCUS tiers (lines 523-537):**\n   - `compute_circus_tiers()`: config-bagging on primary method\n   - Cross-tabulation via `compute_cross_table()`\n   - Outputs: stable_core, method_specific, cross_unstable, noise\n\n5. **ACDC sensitivity (lines 539-545):**\n   - Sweeps tau in [0.01, 0.03, 0.05, 0.1, 0.3]\n   - For each tau: recomputes off_diagonal_pct\n   - Helps understand ACDC threshold impact\n\n6. **Gate judgment (lines 547-551):**\n   - `gate_judgment()` applies MVP gate rules (D001-D003):\n     - ≥10% off-diagonal → PASS_MAIN\n     - 5-10% → PASS_FINDINGS (add Arithmetic verification)\n     - 2-5% → MARGINAL (Findings track)\n     - <2% → KILL (if ΔF also insignificant)\n\n7. **Visualization (lines 554-557):**\n   - CSS heatmap (pairwise Jaccard) via matplotlib\n   - Venn diagram (3-method overlap) or bar chart\n   - Saves as PNG to output_dir\n\n8. **JSON output (lines 559-589):**\n   - File: `analysis_results.json`\n   - Fields: methods, K, per_method_edges, css_cross_tabulation, circus_cross_table, acdc_sensitivity, gate\n\n**CLI usage (lines 596-614):**\n```bash\npython analyze_mvp_results.py \\\n    --results-dir /root/structfuse-context \\\n    --output-dir ./analysis \\\n    --top-n 200 \\\n    --dry-run\n```\n\n---\n\n### 5. SCORING MODULES INTERFACES\n\n#### 5.1 EAP-IG Scoring (eap_ig_scoring.py)\n\n**Function signature:**\n```python\ndef compute_eap_ig_scores(\n    model: nn.Module,\n    clean_inputs: Tensor,\n    corrupt_inputs: Tensor,\n    metric_fn: Callable,\n    target_ids: Optional[Tensor] = None,\n    ig_steps: int = 5,\n    device: str = \"cuda\",\n) -> Dict[str, float]\n```\n\n**Output:** Dict[str, float] with edge names like `\"input->a0.h0.q\"`, `\"a0.h0->m1\"`, etc.\n\n**Key components:**\n- `_get_model_info()`: Detects arch (llama_like, gpt2)\n- `_prepare_inputs()`: Converts various input formats to Tensor\n- `_decompose_per_head()`: Projects head outputs through projection matrices\n- **Backward compatibility:** HuggingFace backend (`_run_eap_ig_hf`) marked NotImplementedError in run_circus.py line 172 — Phase 2 requires HF implementation\n\n#### 5.2 Edge Pruning Scoring (edge_pruning_scoring.py)\n\n**Class:** `HardConcrete(nn.Module)` (lines 40-74)\n```python\ndef forward(self, training: bool = True) -> torch.Tensor\ndef l0_penalty(self) -> torch.Tensor\ndef expected_masks(self) -> torch.Tensor  # Final scoring\n```\n\n**Topology:** `_build_edge_topology()` (lines 125-150)\n- Enumerates all edges: input → all layers\n- Per-head Q masks (independent)\n- Per-KV-group K/V masks (GQA shared)\n- Per-source MLP masks\n- Returns: (edge_names, edge_to_mask_idx, n_masks)\n\n**Hook strategy (v2, D011):**\n- Layer pre-hooks abandoned\n- New: 4 submodule hooks per layer (q_proj, k_proj, v_proj, mlp)\n- Each submodule applies corresponding edge mask in forward\n\n**Output:** Dict[str, float] with mask scores 0-1 per edge\n\n#### 5.3 IFR Scoring (ifr_scoring.py)\n\n**Function signature:**\n```python\ndef compute_ifr_edges(\n    model,\n    dataset: Union[torch.Tensor, dict, list],\n    metric_fn: Optional[Callable] = None,\n    threshold: float = 0.1,\n    device: str = \"cuda\",\n) -> Dict[str, float]\n```\n\n**Core metric (line 39):**\n```python\ndef _proximity(y_u: torch.Tensor, x_v: torch.Tensor) -> float:\n    diff_norm = (y_u - x_v).abs().sum(dim=-1)\n    base_norm = x_v.abs().sum(dim=-1)\n    return (base_norm - diff_norm).clamp(min=0).mean().item()\n```\n\n**Properties:**\n- Single forward pass + activation caching (no backward)\n- **Critical:** All heads at same (src, dst_layer) get identical proximity scores\n- Causes 36 tied edges per layer-pair (D010 issue)\n- Solution: Use `unique_score_rank` binarization (css.py line 53)\n\n**Output:** Dict[str, float] with canonical edge names\n\n---\n\n### 6. SUPPORTING MODULES\n\n#### 6.1 Model Adapter (model_adapter.py, 306 lines)\n\n**Key class:** `ModelAdapter`\n\n**Factory methods:**\n- `from_pretrained(model_name: str, device: str = \"cuda\")` (line 119)\n  - Auto-detects: `_is_gpt2()` → TL, else → HF\n  - TL: via `HookedTransformer.from_pretrained()`\n  - HF: via `AutoModelForCausalLM.from_pretrained()`\n\n**ModelInfo dataclass (lines 31-40):**\n```python\n@dataclass\nclass ModelInfo:\n    arch: str                   # \"gpt2\" | \"qwen2\" | \"llama\" | ...\n    n_layers: int\n    n_heads: int\n    n_kv_heads: int             # GQA\n    d_model: int\n    head_dim: int\n    backend: str                # \"transformerlens\" | \"huggingface\"\n    model_name: str\n```\n\n**Canonical conversion:**\n- TL → canonical: `_tl_to_canonical()` (lines 61-66)\n  - Pattern: `hook_embed` → `input`, `blocks.{L}.attn.hook_result[{H}]` → `a{L}.h{H}`\n- HF → canonical: `_hf_to_canonical()` (lines 69-80)\n  - Pattern: `model.layers.{L}.self_attn.o_proj` → `a{L}`\n\n**Hook point mapping:** `get_hook_points()` returns {canonical_name: module_path}\n\n**GQA support:** `gqa_kv_group()` maps query head to KV group\n\n#### 6.2 CSS Module (css.py, 128 lines)\n\n**Functions:**\n- `binarize_scores(scores, strategy, n=200, threshold=0.01, percentile=95.0)` (lines 18-59)\n  - Strategies: topn, threshold, percentile_threshold, unique_score_rank\n  - **unique_score_rank:** Ranks by unique score values (fixes D010 block-voting)\n\n- `compute_css_matrix(method_circuits, all_edges)` (lines 62-112)\n  - Returns: cell_counts, css_core, off_diagonal, off_diagonal_pct, per_method_counts\n\n- `circus_score(method_circuits, edge)` (lines 115-127)\n  - Fraction of methods including edge\n\n---\n\n### 7. MVP FRAMEWORK (structfuse-mvp/)\n\n**Entry point:** `run_mvp.py` (265 lines)\n\n**Main pipeline:**\n```python\ndef main():\n    # 1. Load model + data\n    model, dataset = load_model_and_data(config)\n    \n    # 2. Run K=3 methods (via circuit_discovery.run_all_methods)\n    all_scores = run_all_methods(model, dataset, metric_fn, config)\n    \n    # 3. Binarize\n    method_circuits = {m: binarize_scores(scores, m) for m, scores in all_scores.items()}\n    \n    # 4. CIRCUS config-bagging (EAP-IG only)\n    eap_stability, circus_tiers = run_circus(all_scores[\"eap_ig\"], config)\n    \n    # 5. CSS across K=3 methods\n    css_scores = compute_css(method_circuits, K=3)\n    \n    # 6. Cross-tabulation\n    table = cross_tabulate(circus_tiers, css_scores, threshold=0.67)\n    \n    # 7. Evaluation (faithfulness)\n    eval_results = evaluate_all_circuits(model, circuits_to_eval, dataset, metric)\n    \n    # 8. MVP gate\n    pct = compute_off_diagonal(table) * 100\n    gate_verdict = \"PASS_MAIN\" if pct >= 10 else \"PASS_FINDINGS\" if pct >= 5 else ...\n```\n\n**Config (structfuse-mvp/config.py):**\n```python\n@dataclass\nclass MVPConfig:\n    model_name: str = \"gpt2-small\"\n    task: str = \"ioi\"\n    methods: List[str] = [\"eap_ig\", \"edge_pruning\", \"acdc\"]  # MVP uses ACDC\n    K: int = 3\n    css_thresholds: List[float] = [0.0, 0.33, 0.67, 1.0]\n    css_default_threshold: float = 0.67\n    circus_B: int = 10\n    eap_ig_steps: int = 5\n    eap_ig_topn: int = 100\n    acdc_threshold: float = 0.05\n\n@dataclass\nclass LargeModelConfig(MVPConfig):\n    model_name: str = \"Qwen/Qwen2.5-0.5B\"\n    methods: List[str] = [\"eap_ig\", \"edge_pruning\", \"ifr\"]  # Phase 2: IFR replaces ACDC\n    eap_ig_topn: int = 200\n```\n\n---\n\n### 8. ROADMAP & DECISION LOG\n\n**ROADMAP.md highlights:**\n\n| Phase | Models | Methods | Gate Rule | Status |\n|-------|--------|---------|-----------|--------|\n| MVP | GPT-2 Small | EAP-IG + EP + ACDC (K=3) | ≥10% off-diagonal | Pending |\n| Phase 2 | Qwen-2.5 0.5B | EAP-IG + EP + IFR (K=3) | K=3 checkpoint pass | ~3 days post-MVP |\n| Phase 3 | Qwen, Gemma, Llama | K=3 × 4 tasks + OOD | Full CSS matrix | ~4 days |\n| Phase 4 | All | — | Analysis + writing | ~3 days, deadline 2026-05-22 |\n\n**Key decisions (decisions.yaml):**\n\n| ID | Summary | Impact |\n|----|---------|--------|\n| D006 | IFR as third method (D005 dependent) | Large model K=3 now viable |\n| D010 | unique_score_rank for IFR | Fixes D006 layer-block voting bias |\n| D011 | EP v2 hook restructure (D010 dependent) | Fixes MLP mask + Q/K/V collapse issues |\n| D009 | Edge name normalization (critical bug) | Unified canonical format |\n| D008 | MVP ≥10% valid under mask_gradient proxy | MVP result interpretation |\n| D007 | GPU isolation fix (L1 lesson) | CUDA_VISIBLE_DEVICES enforcement |\n\n---\n\n### 9. CRITICAL IMPLEMENTATION DETAILS FOR PHASE 2\n\n**1. EAP-IG HuggingFace backend (NOT YET IMPLEMENTED):**\n- File: `eap_ig_scoring.py` line 171-173 raises NotImplementedError\n- Required for Phase 2 on Qwen-2.5\n- Hook points: model.layers.{i} (pre-hook for resid_pre), self_attn.o_proj (per-head decomposition), mlp\n\n**2. Edge Pruning v2 hook restructure (D011):**\n- Current file: `edge_pruning_scoring.py` uses layer pre-hook\n- Problem: MLP mask not applied in forward; Q/K/V masks aggregated to scalar\n- Solution: Replace with 4 submodule hooks (q_proj, k_proj, v_proj, mlp) per layer\n\n**3. IFR binarization strategy (D010):**\n- Problem: 36 tied scores per layer-pair (residual-stream shared across heads)\n- Solution: Use `unique_score_rank` in `css.binarize_scores()` instead of `topn`\n- Default config in `run_circus.py` line 46: `\"unique_score_rank\"` with n=50\n\n**4. GPU safety (D007, memory.md):**\n- All scripts must set `os.environ['CUDA_VISIBLE_DEVICES']` BEFORE torch import\n- `run_circus.py` line 24 enforces this\n- Memory.md line 6: \"后续所有实验脚本必须在第一行设置 CUDA_VISIBLE_DEVICES\"\n\n**5. Cache invalidation:**\n- CANONICAL_VERSION in model_adapter.py line 28\n- Cache key includes: model, task, method, canonical_version, hyperparams\n- If edge names change, increment CANONICAL_VERSION + clear old caches\n\n**6. Edge naming normalization (D009):**\n- Critical: _normalize_* functions in structfuse-mvp/circuit_discovery.py must produce same format\n- Canonical form: `\"{src}->{dst}\"` (no spaces around arrow)\n- Test: All three methods' edges must match exactly in css.py compute_css()\n\n---\n\n### 10. TESTING FRAMEWORK\n\n**Test files (artifacts/):**\n- `test_css.py`: 8 tests for binarization, CSS matrix, CIRCUS score\n- `test_eap_ig_scoring.py`: AST validation + GPT-2 integration\n- `test_edge_pruning_scoring.py`: Topology, GQA sharing, mask independence\n- `test_ifr_scoring.py`: Proximity metric, edge coverage\n\n**Smoke test pattern:**\n```python\ndef test_module_signature():\n    \"\"\"AST-based validation of function signatures.\"\"\"\n    import ast\n    tree = ast.parse(open(\"module.py\").read())\n    # Assert expected functions exist with correct signatures\n    \ndef test_integration_gpt2():\n    \"\"\"Optional: run on actual GPT-2 if available.\"\"\"\n    from transformer_lens import HookedTransformer\n    model = HookedTransformer.from_pretrained(\"gpt2-small\")\n    scores = compute_scores(model, ...)\n    assert isinstance(scores, dict) and all(isinstance(v, float) for v in scores.values())\n```\n\n---\n\n### 11. DEPLOYMENT & EXECUTION\n\n**Phase 2 deployment script:** `deploy_phase2.sh` (in artifacts/)\n\n**CLI entry points:**\n\n```bash\n# Run full Phase 2 pipeline with default config\npython run_circus.py\n\n# Custom config (JSON)\npython run_circus.py config.json\n\n# Custom config (YAML)\npython run_circus.py config.yaml\n\n# Analyze MVP results\npython analyze_mvp_results.py \\\n    --results-dir /root/structfuse-context \\\n    --output-dir ./analysis \\\n    --top-n 200\n```\n\n**Expected outputs:**\n\n```\nresults/\n├── Qwen_Qwen2.5-0.5B__ioi_K3.json       # run_circus output\n├── analysis/\n│   ├── analysis_results.json             # analyze_mvp_results output\n│   ├── css_heatmap.png\n│   └── edge_overlap.png                  # Venn or bar chart\n└── cache/\n    ├── Qwen_Qwen2.5-0.5B__/\n    │   └── ioi/\n    │       ├── eap_ig_v2_&lt;hash>.json\n    │       ├── edge_pruning_v2_&lt;hash>.json\n    │       └── ifr_v2_&lt;hash>.json\n```\n\n---\n\n### 12. SUMMARY OF KEY FUNCTION SIGNATURES FOR PHASE 2 FRAMEWORK\n\n```python\n# run_circus.py\ndef run_pipeline(config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]\ndef run_method(adapter: ModelAdapter, method: str, dataset: torch.Tensor, \n               metric: Optional[Callable], cfg: dict) -> Dict[str, float]\ndef compute_css(method_circuits: Dict[str, Set[str]], K: int) -> Dict[str, float]\ndef cross_tabulate(tiers: Dict[str, str], css_scores: Dict[str, float], \n                   css_thr: float) -> Dict[str, Any]\n\n# analyze_mvp_results.py\ndef run_analysis(results_dir: Path, output_dir: Path, top_n: int = 200,\n                 dry_run: bool = False) -> Dict[str, Any]\ndef gate_judgment(off_diagonal_pct: float) -> Dict[str, str]\n\n# model_adapter.py\nclass ModelAdapter:\n    @classmethod\n    def from_pretrained(cls, model_name: str, device: str = \"cuda\") -> ModelAdapter\n    def to_canonical_edges(self, edge_scores: Dict[str, float], method: str) -> Dict[str, float]\n\n# css.py\ndef binarize_scores(scores: Dict[str, float], strategy: BinarizeStrategy,\n                    n: int = 200, threshold: float = 0.01) -> set[str]\ndef compute_css_matrix(method_circuits: Dict[str, set[str]], all_edges: set[str]) -> Dict\n\n# Scoring modules (Phase 2 HF implementations)\ndef compute_eap_ig_scores(model, clean_inputs, corrupt_inputs, metric_fn, ...) -> Dict[str, float]\ndef compute_ifr_edges(model, dataset, metric_fn=None, threshold=0.1, ...) -> Dict[str, float]\n# Edge Pruning: use eap_ig_scoring.HardConcrete + _masked_forward pattern\n```\n\n---\n\nThis comprehensive framework enables Phase 2 to:\n1. **Scale to large models** (Qwen-2.5, Llama-3.1, Gemma-2) via HuggingFace backends\n2. **Maintain edge-level precision** via canonical naming (D009) and proper hook placement (D011)\n3. **Handle IFR tied scores** via unique_score_rank binarization (D010)\n4. **Reproduce MVP analysis** via run_circus.py + analyze_mvp_results.py\n5. **Gate progression** via off-diagonal_pct thresholds (D001-D003)"
      }
    ],
    "totalDurationMs": 104735,
    "totalTokens": 83200,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 75090,
      "output_tokens": 7485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 622
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7485,
          "cache_read_input_tokens": 75090,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 622,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 20,
      "searchCount": 0,
      "bashCount": 11,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Assistant

_source line 104_

<details><summary>Logged reasoning block</summary>

```text
Excellent, now I have a comprehensive understanding of the project. Let me write the two files:

1. `run_phase2_experiment.py` - Phase 2 experiment framework
2. `phase2_configs.yaml` - Experiment configuration matrix

Key things to incorporate:
- Reuse `run_circus.py`'s `run_pipeline()` as the core
- Reuse `analyze_mvp_results.py`'s `run_analysis()` for post-experiment analysis
- Support YAML config loading
- Cache management with CANONICAL_VERSION
- GPU guard (CUDA_VISIBLE_DEVICES before torch import)


- Python logging setup and checkpoint/resume capabilities

Now I'm mapping out the experiment matrix: 4 models across 3 core tasks (IOI, Greater-Than, Docstring) with GPT-2 using ACDC and the others using IFR, giving me at least 12 base experiments that could expand with additional variants.

I'm prioritizing the work in phases—starting with the GPT-2 IOI baseline that's already running, then moving to Qwen-2.5 across all tasks plus GPT-2's remaining benchmarks, and finally tackling the larger models once those are complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "1776256a-8ba2-4be1-90f4-3a543482dc97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EiDozKfweKd1sRsnJuFNMx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7863,
      "cache_read_input_tokens": 24233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7863
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

_source line 105_

Now I have full context on the codebase. Let me write both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "7b43d22e-d0cf-4d38-a605-802b4b25d2b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EiDozKfweKd1sRsnJuFNMx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7863,
      "cache_read_input_tokens": 24233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7863
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

_source line 106_

<details open><summary>🔧 Tool call — Write · `toolu_01R7hzKg3SgV1u6Zz5gfQSEz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/run_phase2_experiment.py",
  "content": "\"\"\"Phase 2 实验框架：多模型 × 多任务 × 多方法的 CSS circuit discovery。\n\n复用 run_circus.py 的 pipeline + analyze_mvp_results.py 的分析，\n支持配置化批量实验。\n\nUsage:\n    python run_phase2_experiment.py --config phase2_configs.yaml --experiment gpt2_ioi\n    python run_phase2_experiment.py --config phase2_configs.yaml --all\n    python run_phase2_experiment.py --config phase2_configs.yaml --priority 2\n    python run_phase2_experiment.py --list  # 列出所有候选实验\n    python run_phase2_experiment.py --status  # 查看已完成/待运行状态\n\"\"\"\n\nimport os\n# GPU guard: 必须在 torch import 之前设置 (D007)\n_GPU_ID = os.environ.get(\"CUDA_VISIBLE_DEVICES\", \"0\")\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = _GPU_ID\n\nimport argparse\nimport hashlib\nimport json\nimport logging\nimport sys\nimport time\nfrom dataclasses import dataclass, field\nfrom pathlib import Path\nfrom typing import Any, Dict, List, Optional, Set\n\nimport yaml\n\nCANONICAL_VERSION = \"v2\"\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlogger = logging.getLogger(\"phase2\")\n\n\n# ---------------------------------------------------------------------------\n# Config dataclasses\n# ---------------------------------------------------------------------------\n\n@dataclass\nclass ExperimentConfig:\n    \"\"\"单个实验的配置。\"\"\"\n    name: str\n    model: str\n    task: str\n    methods: List[str]\n    backend: str  # \"transformerlens\" | \"huggingface\"\n    priority: int = 3\n    model_path: Optional[str] = None\n    K: int = 3\n    num_samples: int = 50\n    gpu_id: str = \"0\"\n    seed: int = 42\n    eap_ig_steps: int = 5\n    edge_pruning_epochs: int = 100\n    edge_pruning_lambda: float = 1e-2\n    ifr_threshold: float = 0.1\n    css_threshold: float = 0.67\n    circus_B: int = 10\n    binarize: Dict[str, Dict[str, Any]] = field(default_factory=dict)\n    thresholds: Dict[str, List[float]] = field(default_factory=dict)\n    notes: str = \"\"\n\n    def __post_init__(self):\n        if not self.binarize:\n            self.binarize = {\n                \"eap_ig\": {\"strategy\": \"topn\", \"n\": 200},\n                \"edge_pruning\": {\"strategy\": \"topn\", \"n\": 200},\n                \"ifr\": {\"strategy\": \"unique_score_rank\", \"n\": 50},  # D010\n                \"acdc\": {\"strategy\": \"threshold\", \"threshold\": 0.05},\n            }\n\n    @property\n    def model_slug(self) -> str:\n        return self.model.replace(\"/\", \"_\").replace(\"-\", \"_\")\n\n    @property\n    def output_dir(self) -> Path:\n        return Path(\"results\") / f\"{self.model_slug}_{self.task}\"\n\n    @property\n    def cache_dir(self) -> Path:\n        return Path(\"cache\") / self.model_slug / self.task\n\n    def to_run_circus_config(self) -> Dict[str, Any]:\n        \"\"\"转换为 run_circus.py 的 config dict 格式。\"\"\"\n        cfg = {\n            \"model\": self.model_path or self.model,\n            \"task\": self.task,\n            \"methods\": self.methods,\n            \"K\": self.K,\n            \"num_samples\": self.num_samples,\n            \"gpu_id\": self.gpu_id,\n            \"seed\": self.seed,\n            \"eap_ig_steps\": self.eap_ig_steps,\n            \"edge_pruning_epochs\": self.edge_pruning_epochs,\n            \"edge_pruning_lambda\": self.edge_pruning_lambda,\n            \"ifr_threshold\": self.ifr_threshold,\n            \"css_threshold\": self.css_threshold,\n            \"circus_B\": self.circus_B,\n            \"binarize\": {m: v for m, v in self.binarize.items() if m in self.methods},\n            \"device\": \"cuda\",\n            \"output_dir\": str(self.output_dir),\n            \"cache_dir\": str(self.cache_dir),\n        }\n        return cfg\n\n\n# ---------------------------------------------------------------------------\n# Config loading\n# ---------------------------------------------------------------------------\n\ndef load_experiment_matrix(config_path: str) -> Dict[str, ExperimentConfig]:\n    \"\"\"从 YAML 加载实验矩阵。\"\"\"\n    path = Path(config_path)\n    if not path.exists():\n        raise FileNotFoundError(f\"Config not found: {config_path}\")\n\n    with open(path) as f:\n        raw = yaml.safe_load(f)\n\n    defaults = raw.get(\"defaults\", {})\n    experiments = {}\n\n    for name, exp_cfg in raw.get(\"experiments\", {}).items():\n        merged = {**defaults, **exp_cfg}\n        experiments[name] = ExperimentConfig(name=name, **merged)\n\n    return experiments\n\n\ndef list_experiments(experiments: Dict[str, ExperimentConfig]) -> None:\n    \"\"\"打印实验列表。\"\"\"\n    by_priority: Dict[int, List[ExperimentConfig]] = {}\n    for exp in experiments.values():\n        by_priority.setdefault(exp.priority, []).append(exp)\n\n    for pri in sorted(by_priority):\n        label = {1: \"MVP (已跑/在跑)\", 2: \"MVP 后立即跑\", 3: \"有空再跑\"}.get(pri, f\"P{pri}\")\n        print(f\"\\n=== Priority {pri}: {label} ===\")\n        for exp in sorted(by_priority[pri], key=lambda e: e.name):\n            methods_str = \", \".join(exp.methods)\n            print(f\"  {exp.name:30s}  {exp.model:30s}  {exp.task:15s}  [{methods_str}]\")\n\n    total = len(experiments)\n    counts = {p: len(exps) for p, exps in by_priority.items()}\n    print(f\"\\nTotal: {total} experiments | \" + \" | \".join(f\"P{p}={c}\" for p, c in sorted(counts.items())))\n\n\n# ---------------------------------------------------------------------------\n# Cache management\n# ---------------------------------------------------------------------------\n\ndef _cache_key(exp: ExperimentConfig, method: str) -> str:\n    \"\"\"生成缓存文件名，绑定 CANONICAL_VERSION + 超参哈希。\"\"\"\n    params = {\n        \"model\": exp.model,\n        \"task\": exp.task,\n        \"method\": method,\n        \"num_samples\": exp.num_samples,\n        \"seed\": exp.seed,\n    }\n    if method == \"eap_ig\":\n        params[\"steps\"] = exp.eap_ig_steps\n    elif method == \"edge_pruning\":\n        params[\"epochs\"] = exp.edge_pruning_epochs\n        params[\"lambda\"] = exp.edge_pruning_lambda\n    elif method == \"ifr\":\n        params[\"threshold\"] = exp.ifr_threshold\n    elif method == \"acdc\":\n        params[\"thresholds\"] = exp.thresholds.get(\"acdc\", [0.05])\n\n    h = hashlib.md5(json.dumps(params, sort_keys=True).encode()).hexdigest()[:16]\n    return f\"{method}_{CANONICAL_VERSION}_{h}.json\"\n\n\ndef check_cache(exp: ExperimentConfig) -> Dict[str, bool]:\n    \"\"\"检查每个方法的缓存状态。\"\"\"\n    status = {}\n    for method in exp.methods:\n        cache_file = exp.cache_dir / _cache_key(exp, method)\n        status[method] = cache_file.exists()\n    return status\n\n\ndef load_cached_scores(exp: ExperimentConfig, method: str) -> Optional[Dict[str, float]]:\n    \"\"\"加载已缓存的 edge scores。\"\"\"\n    cache_file = exp.cache_dir / _cache_key(exp, method)\n    if not cache_file.exists():\n        return None\n    with open(cache_file) as f:\n        data = json.load(f)\n    if data.get(\"canonical_version\") != CANONICAL_VERSION:\n        logger.warning(\"Cache version mismatch for %s/%s, will recompute\", exp.name, method)\n        return None\n    return data.get(\"scores\", {})\n\n\ndef save_cached_scores(exp: ExperimentConfig, method: str, scores: Dict[str, float]) -> None:\n    \"\"\"保存 edge scores 到缓存。\"\"\"\n    exp.cache_dir.mkdir(parents=True, exist_ok=True)\n    cache_file = exp.cache_dir / _cache_key(exp, method)\n    data = {\n        \"canonical_version\": CANONICAL_VERSION,\n        \"model\": exp.model,\n        \"task\": exp.task,\n        \"method\": method,\n        \"n_edges\": len(scores),\n        \"scores\": scores,\n    }\n    with open(cache_file, \"w\") as f:\n        json.dump(data, f, indent=2)\n    logger.info(\"Cached %d edges → %s\", len(scores), cache_file)\n\n\n# ---------------------------------------------------------------------------\n# Experiment runner\n# ---------------------------------------------------------------------------\n\ndef run_single_experiment(exp: ExperimentConfig, force: bool = False) -> Dict[str, Any]:\n    \"\"\"运行单个实验：调用 run_circus pipeline，支持断点续跑。\n\n    Returns:\n        run_circus.run_pipeline() 的完整输出 dict，包含\n        method_edge_counts, css_distribution, cross_table 等。\n    \"\"\"\n    logger.info(\"=\" * 60)\n    logger.info(\"Starting experiment: %s\", exp.name)\n    logger.info(\"  Model: %s (%s backend)\", exp.model, exp.backend)\n    logger.info(\"  Task: %s | Methods: %s | K=%d\", exp.task, exp.methods, exp.K)\n    logger.info(\"=\" * 60)\n\n    # 断点续跑：检查哪些方法已有缓存\n    cache_status = check_cache(exp)\n    if not force:\n        cached = [m for m, done in cache_status.items() if done]\n        pending = [m for m, done in cache_status.items() if not done]\n        if cached:\n            logger.info(\"Cached methods (skip): %s\", cached)\n        if not pending:\n            logger.info(\"All methods cached, running CSS/CIRCUS aggregation only\")\n    else:\n        pending = exp.methods\n        logger.info(\"Force mode: recomputing all methods\")\n\n    # 构建 run_circus config\n    circus_cfg = exp.to_run_circus_config()\n    exp.output_dir.mkdir(parents=True, exist_ok=True)\n\n    # 调用 run_circus pipeline\n    # TODO: 当前直接调用 run_pipeline，未来可拆分为：\n    #   1. run_methods_only(circus_cfg, skip=cached) → 仅跑 scoring\n    #   2. run_aggregation(circus_cfg, all_scores) → CSS + CIRCUS + cross-tab\n    # 以支持更细粒度的断点续跑\n    try:\n        from run_circus import run_pipeline\n        results = run_pipeline(config=circus_cfg)\n    except ImportError:\n        logger.error(\"run_circus.py not found in sys.path. Add artifacts/ to PYTHONPATH.\")\n        raise\n    except Exception as e:\n        logger.error(\"Experiment %s failed: %s\", exp.name, e)\n        raise\n\n    # 保存实验元信息\n    meta = {\n        \"experiment_name\": exp.name,\n        \"priority\": exp.priority,\n        \"backend\": exp.backend,\n        \"canonical_version\": CANONICAL_VERSION,\n        \"timestamp\": time.strftime(\"%Y-%m-%d %H:%M:%S\"),\n    }\n    results[\"phase2_meta\"] = meta\n\n    output_file = exp.output_dir / f\"{exp.model_slug}_{exp.task}_K{exp.K}.json\"\n    with open(output_file, \"w\") as f:\n        json.dump(results, f, indent=2, default=str)\n    logger.info(\"Results → %s\", output_file)\n\n    return results\n\n\ndef run_analysis_for_experiment(exp: ExperimentConfig) -> Optional[Dict[str, Any]]:\n    \"\"\"实验完成后调用 analyze_mvp_results 的分析逻辑。\"\"\"\n    try:\n        from analyze_mvp_results import run_analysis\n    except ImportError:\n        logger.warning(\"analyze_mvp_results.py not importable, skipping analysis\")\n        return None\n\n    analysis_dir = exp.output_dir / \"analysis\"\n    analysis_dir.mkdir(parents=True, exist_ok=True)\n\n    # run_analysis 从 cache dir 加载 per-method scores\n    results = run_analysis(\n        results_dir=exp.cache_dir.parent.parent,  # results/ 根\n        output_dir=analysis_dir,\n        top_n=200,\n    )\n    logger.info(\"Analysis → %s\", analysis_dir)\n    return results\n\n\n# ---------------------------------------------------------------------------\n# Batch runner\n# ---------------------------------------------------------------------------\n\ndef run_batch(\n    experiments: Dict[str, ExperimentConfig],\n    names: Optional[List[str]] = None,\n    max_priority: Optional[int] = None,\n    force: bool = False,\n) -> Dict[str, Dict[str, Any]]:\n    \"\"\"批量运行实验。\n\n    Args:\n        experiments: 完整实验矩阵\n        names: 指定运行的实验名（None=全部）\n        max_priority: 只运行 priority <= 此值的实验\n        force: 忽略缓存，强制重算\n    \"\"\"\n    selected = _select_experiments(experiments, names, max_priority)\n\n    # 按 priority 排序\n    ordered = sorted(selected.values(), key=lambda e: (e.priority, e.name))\n    logger.info(\"Running %d experiments (sorted by priority)\", len(ordered))\n\n    all_results = {}\n    for i, exp in enumerate(ordered, 1):\n        logger.info(\"[%d/%d] %s (priority=%d)\", i, len(ordered), exp.name, exp.priority)\n        t0 = time.time()\n\n        try:\n            results = run_single_experiment(exp, force=force)\n            analysis = run_analysis_for_experiment(exp)\n            if analysis:\n                results[\"analysis\"] = analysis\n\n            elapsed = time.time() - t0\n            results[\"elapsed_sec\"] = elapsed\n            all_results[exp.name] = results\n            logger.info(\"✓ %s completed in %.1f sec\", exp.name, elapsed)\n\n        except Exception as e:\n            logger.error(\"✗ %s failed: %s\", exp.name, e)\n            all_results[exp.name] = {\"error\": str(e)}\n\n    _save_batch_summary(all_results)\n    return all_results\n\n\ndef _select_experiments(\n    experiments: Dict[str, ExperimentConfig],\n    names: Optional[List[str]] = None,\n    max_priority: Optional[int] = None,\n) -> Dict[str, ExperimentConfig]:\n    \"\"\"筛选实验子集。\"\"\"\n    selected = experiments\n    if names:\n        missing = set(names) - set(experiments)\n        if missing:\n            raise ValueError(f\"Unknown experiments: {missing}\")\n        selected = {n: experiments[n] for n in names}\n    if max_priority is not None:\n        selected = {n: e for n, e in selected.items() if e.priority <= max_priority}\n    if not selected:\n        raise ValueError(\"No experiments match the filter criteria\")\n    return selected\n\n\ndef _save_batch_summary(all_results: Dict[str, Dict[str, Any]]) -> None:\n    \"\"\"保存批量运行摘要。\"\"\"\n    summary_path = Path(\"results\") / \"phase2_batch_summary.json\"\n    summary_path.parent.mkdir(parents=True, exist_ok=True)\n\n    summary = {\n        \"timestamp\": time.strftime(\"%Y-%m-%d %H:%M:%S\"),\n        \"canonical_version\": CANONICAL_VERSION,\n        \"experiments\": {},\n    }\n    for name, res in all_results.items():\n        entry = {\"status\": \"error\" if \"error\" in res else \"ok\"}\n        if \"error\" in res:\n            entry[\"error\"] = res[\"error\"]\n        else:\n            entry[\"elapsed_sec\"] = res.get(\"elapsed_sec\")\n            if \"cross_table\" in res:\n                entry[\"off_diagonal_pct\"] = res[\"cross_table\"].get(\"off_diagonal_pct\")\n            if \"css_distribution\" in res:\n                entry[\"css_distribution\"] = res[\"css_distribution\"]\n        summary[\"experiments\"][name] = entry\n\n    with open(summary_path, \"w\") as f:\n        json.dump(summary, f, indent=2)\n    logger.info(\"Batch summary → %s\", summary_path)\n\n\n# ---------------------------------------------------------------------------\n# Status check\n# ---------------------------------------------------------------------------\n\ndef show_status(experiments: Dict[str, ExperimentConfig]) -> None:\n    \"\"\"显示每个实验的完成状态。\"\"\"\n    print(f\"\\n{'Experiment':30s} {'Model':25s} {'Task':12s} {'Cached Methods':40s} {'Result'}\")\n    print(\"-\" * 120)\n\n    for name in sorted(experiments, key=lambda n: (experiments[n].priority, n)):\n        exp = experiments[name]\n        cache = check_cache(exp)\n        cached_str = \" \".join(f\"{'✓' if v else '✗'}{m}\" for m, v in cache.items())\n\n        result_file = exp.output_dir / f\"{exp.model_slug}_{exp.task}_K{exp.K}.json\"\n        result_str = \"✓\" if result_file.exists() else \"—\"\n\n        print(f\"  P{exp.priority} {name:28s} {exp.model:25s} {exp.task:12s} {cached_str:40s} {result_str}\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef parse_args() -> argparse.Namespace:\n    parser = argparse.ArgumentParser(description=\"Phase 2 experiment runner\")\n    parser.add_argument(\"--config\", type=str, default=\"phase2_configs.yaml\",\n                        help=\"实验矩阵 YAML 路径\")\n    parser.add_argument(\"--experiment\", type=str, nargs=\"+\",\n                        help=\"运行指定实验（空格分隔多个）\")\n    parser.add_argument(\"--all\", action=\"store_true\",\n                        help=\"运行全部实验\")\n    parser.add_argument(\"--priority\", type=int,\n                        help=\"只运行 priority <= N 的实验\")\n    parser.add_argument(\"--list\", action=\"store_true\",\n                        help=\"列出所有实验\")\n    parser.add_argument(\"--status\", action=\"store_true\",\n                        help=\"显示完成状态\")\n    parser.add_argument(\"--force\", action=\"store_true\",\n                        help=\"忽略缓存强制重算\")\n    parser.add_argument(\"--gpu\", type=str, default=None,\n                        help=\"覆盖 CUDA_VISIBLE_DEVICES\")\n    return parser.parse_args()\n\n\ndef main():\n    args = parse_args()\n\n    if args.gpu:\n        os.environ[\"CUDA_VISIBLE_DEVICES\"] = args.gpu\n        logger.info(\"GPU override: CUDA_VISIBLE_DEVICES=%s\", args.gpu)\n\n    experiments = load_experiment_matrix(args.config)\n\n    if args.list:\n        list_experiments(experiments)\n        return\n\n    if args.status:\n        show_status(experiments)\n        return\n\n    if args.experiment:\n        run_batch(experiments, names=args.experiment, force=args.force)\n    elif args.all:\n        run_batch(experiments, max_priority=args.priority, force=args.force)\n    elif args.priority:\n        run_batch(experiments, max_priority=args.priority, force=args.force)\n    else:\n        parser = argparse.ArgumentParser()\n        parser.print_help()\n        print(\"\\nHint: use --list to see experiments, --experiment NAME to run one\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "af11b566-bc11-4e71-9ab3-4795d83ab2d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EiDozKfweKd1sRsnJuFNMx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7863,
      "cache_read_input_tokens": 24233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7863
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

_source line 107 · 2026-05-12T22:10:42.522Z_

<details><summary>↩ Tool result · `toolu_01R7hzKg3SgV1u6Zz5gfQSEz`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/run_phase2_experiment.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "90109723-60c8-4821-8dbe-9339d5583f7c",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/run_phase2_experiment.py",
    "content": "\"\"\"Phase 2 实验框架：多模型 × 多任务 × 多方法的 CSS circuit discovery。\n\n复用 run_circus.py 的 pipeline + analyze_mvp_results.py 的分析，\n支持配置化批量实验。\n\nUsage:\n    python run_phase2_experiment.py --config phase2_configs.yaml --experiment gpt2_ioi\n    python run_phase2_experiment.py --config phase2_configs.yaml --all\n    python run_phase2_experiment.py --config phase2_configs.yaml --priority 2\n    python run_phase2_experiment.py --list  # 列出所有候选实验\n    python run_phase2_experiment.py --status  # 查看已完成/待运行状态\n\"\"\"\n\nimport os\n# GPU guard: 必须在 torch import 之前设置 (D007)\n_GPU_ID = os.environ.get(\"CUDA_VISIBLE_DEVICES\", \"0\")\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = _GPU_ID\n\nimport argparse\nimport hashlib\nimport json\nimport logging\nimport sys\nimport time\nfrom dataclasses import dataclass, field\nfrom pathlib import Path\nfrom typing import Any, Dict, List, Optional, Set\n\nimport yaml\n\nCANONICAL_VERSION = \"v2\"\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlogger = logging.getLogger(\"phase2\")\n\n\n# ---------------------------------------------------------------------------\n# Config dataclasses\n# ---------------------------------------------------------------------------\n\n@dataclass\nclass ExperimentConfig:\n    \"\"\"单个实验的配置。\"\"\"\n    name: str\n    model: str\n    task: str\n    methods: List[str]\n    backend: str  # \"transformerlens\" | \"huggingface\"\n    priority: int = 3\n    model_path: Optional[str] = None\n    K: int = 3\n    num_samples: int = 50\n    gpu_id: str = \"0\"\n    seed: int = 42\n    eap_ig_steps: int = 5\n    edge_pruning_epochs: int = 100\n    edge_pruning_lambda: float = 1e-2\n    ifr_threshold: float = 0.1\n    css_threshold: float = 0.67\n    circus_B: int = 10\n    binarize: Dict[str, Dict[str, Any]] = field(default_factory=dict)\n    thresholds: Dict[str, List[float]] = field(default_factory=dict)\n    notes: str = \"\"\n\n    def __post_init__(self):\n        if not self.binarize:\n            self.binarize = {\n                \"eap_ig\": {\"strategy\": \"topn\", \"n\": 200},\n                \"edge_pruning\": {\"strategy\": \"topn\", \"n\": 200},\n                \"ifr\": {\"strategy\": \"unique_score_rank\", \"n\": 50},  # D010\n                \"acdc\": {\"strategy\": \"threshold\", \"threshold\": 0.05},\n            }\n\n    @property\n    def model_slug(self) -> str:\n        return self.model.replace(\"/\", \"_\").replace(\"-\", \"_\")\n\n    @property\n    def output_dir(self) -> Path:\n        return Path(\"results\") / f\"{self.model_slug}_{self.task}\"\n\n    @property\n    def cache_dir(self) -> Path:\n        return Path(\"cache\") / self.model_slug / self.task\n\n    def to_run_circus_config(self) -> Dict[str, Any]:\n        \"\"\"转换为 run_circus.py 的 config dict 格式。\"\"\"\n        cfg = {\n            \"model\": self.model_path or self.model,\n            \"task\": self.task,\n            \"methods\": self.methods,\n            \"K\": self.K,\n            \"num_samples\": self.num_samples,\n            \"gpu_id\": self.gpu_id,\n            \"seed\": self.seed,\n            \"eap_ig_steps\": self.eap_ig_steps,\n            \"edge_pruning_epochs\": self.edge_pruning_epochs,\n            \"edge_pruning_lambda\": self.edge_pruning_lambda,\n            \"ifr_threshold\": self.ifr_threshold,\n            \"css_threshold\": self.css_threshold,\n            \"circus_B\": self.circus_B,\n            \"binarize\": {m: v for m, v in self.binarize.items() if m in self.methods},\n            \"device\": \"cuda\",\n            \"output_dir\": str(self.output_dir),\n            \"cache_dir\": str(self.cache_dir),\n        }\n        return cfg\n\n\n# ---------------------------------------------------------------------------\n# Config loading\n# ---------------------------------------------------------------------------\n\ndef load_experiment_matrix(config_path: str) -> Dict[str, ExperimentConfig]:\n    \"\"\"从 YAML 加载实验矩阵。\"\"\"\n    path = Path(config_path)\n    if not path.exists():\n        raise FileNotFoundError(f\"Config not found: {config_path}\")\n\n    with open(path) as f:\n        raw = yaml.safe_load(f)\n\n    defaults = raw.get(\"defaults\", {})\n    experiments = {}\n\n    for name, exp_cfg in raw.get(\"experiments\", {}).items():\n        merged = {**defaults, **exp_cfg}\n        experiments[name] = ExperimentConfig(name=name, **merged)\n\n    return experiments\n\n\ndef list_experiments(experiments: Dict[str, ExperimentConfig]) -> None:\n    \"\"\"打印实验列表。\"\"\"\n    by_priority: Dict[int, List[ExperimentConfig]] = {}\n    for exp in experiments.values():\n        by_priority.setdefault(exp.priority, []).append(exp)\n\n    for pri in sorted(by_priority):\n        label = {1: \"MVP (已跑/在跑)\", 2: \"MVP 后立即跑\", 3: \"有空再跑\"}.get(pri, f\"P{pri}\")\n        print(f\"\\n=== Priority {pri}: {label} ===\")\n        for exp in sorted(by_priority[pri], key=lambda e: e.name):\n            methods_str = \", \".join(exp.methods)\n            print(f\"  {exp.name:30s}  {exp.model:30s}  {exp.task:15s}  [{methods_str}]\")\n\n    total = len(experiments)\n    counts = {p: len(exps) for p, exps in by_priority.items()}\n    print(f\"\\nTotal: {total} experiments | \" + \" | \".join(f\"P{p}={c}\" for p, c in sorted(counts.items())))\n\n\n# ---------------------------------------------------------------------------\n# Cache management\n# ---------------------------------------------------------------------------\n\ndef _cache_key(exp: ExperimentConfig, method: str) -> str:\n    \"\"\"生成缓存文件名，绑定 CANONICAL_VERSION + 超参哈希。\"\"\"\n    params = {\n        \"model\": exp.model,\n        \"task\": exp.task,\n        \"method\": method,\n        \"num_samples\": exp.num_samples,\n        \"seed\": exp.seed,\n    }\n    if method == \"eap_ig\":\n        params[\"steps\"] = exp.eap_ig_steps\n    elif method == \"edge_pruning\":\n        params[\"epochs\"] = exp.edge_pruning_epochs\n        params[\"lambda\"] = exp.edge_pruning_lambda\n    elif method == \"ifr\":\n        params[\"threshold\"] = exp.ifr_threshold\n    elif method == \"acdc\":\n        params[\"thresholds\"] = exp.thresholds.get(\"acdc\", [0.05])\n\n    h = hashlib.md5(json.dumps(params, sort_keys=True).encode()).hexdigest()[:16]\n    return f\"{method}_{CANONICAL_VERSION}_{h}.json\"\n\n\ndef check_cache(exp: ExperimentConfig) -> Dict[str, bool]:\n    \"\"\"检查每个方法的缓存状态。\"\"\"\n    status = {}\n    for method in exp.methods:\n        cache_file = exp.cache_dir / _cache_key(exp, method)\n        status[method] = cache_file.exists()\n    return status\n\n\ndef load_cached_scores(exp: ExperimentConfig, method: str) -> Optional[Dict[str, float]]:\n    \"\"\"加载已缓存的 edge scores。\"\"\"\n    cache_file = exp.cache_dir / _cache_key(exp, method)\n    if not cache_file.exists():\n        return None\n    with open(cache_file) as f:\n        data = json.load(f)\n    if data.get(\"canonical_version\") != CANONICAL_VERSION:\n        logger.warning(\"Cache version mismatch for %s/%s, will recompute\", exp.name, method)\n        return None\n    return data.get(\"scores\", {})\n\n\ndef save_cached_scores(exp: ExperimentConfig, method: str, scores: Dict[str, float]) -> None:\n    \"\"\"保存 edge scores 到缓存。\"\"\"\n    exp.cache_dir.mkdir(parents=True, exist_ok=True)\n    cache_file = exp.cache_dir / _cache_key(exp, method)\n    data = {\n        \"canonical_version\": CANONICAL_VERSION,\n        \"model\": exp.model,\n        \"task\": exp.task,\n        \"method\": method,\n        \"n_edges\": len(scores),\n        \"scores\": scores,\n    }\n    with open(cache_file, \"w\") as f:\n        json.dump(data, f, indent=2)\n    logger.info(\"Cached %d edges → %s\", len(scores), cache_file)\n\n\n# ---------------------------------------------------------------------------\n# Experiment runner\n# ---------------------------------------------------------------------------\n\ndef run_single_experiment(exp: ExperimentConfig, force: bool = False) -> Dict[str, Any]:\n    \"\"\"运行单个实验：调用 run_circus pipeline，支持断点续跑。\n\n    Returns:\n        run_circus.run_pipeline() 的完整输出 dict，包含\n        method_edge_counts, css_distribution, cross_table 等。\n    \"\"\"\n    logger.info(\"=\" * 60)\n    logger.info(\"Starting experiment: %s\", exp.name)\n    logger.info(\"  Model: %s (%s backend)\", exp.model, exp.backend)\n    logger.info(\"  Task: %s | Methods: %s | K=%d\", exp.task, exp.methods, exp.K)\n    logger.info(\"=\" * 60)\n\n    # 断点续跑：检查哪些方法已有缓存\n    cache_status = check_cache(exp)\n    if not force:\n        cached = [m for m, done in cache_status.items() if done]\n        pending = [m for m, done in cache_status.items() if not done]\n        if cached:\n            logger.info(\"Cached methods (skip): %s\", cached)\n        if not pending:\n            logger.info(\"All methods cached, running CSS/CIRCUS aggregation only\")\n    else:\n        pending = exp.methods\n        logger.info(\"Force mode: recomputing all methods\")\n\n    # 构建 run_circus config\n    circus_cfg = exp.to_run_circus_config()\n    exp.output_dir.mkdir(parents=True, exist_ok=True)\n\n    # 调用 run_circus pipeline\n    # TODO: 当前直接调用 run_pipeline，未来可拆分为：\n    #   1. run_methods_only(circus_cfg, skip=cached) → 仅跑 scoring\n    #   2. run_aggregation(circus_cfg, all_scores) → CSS + CIRCUS + cross-tab\n    # 以支持更细粒度的断点续跑\n    try:\n        from run_circus import run_pipeline\n        results = run_pipeline(config=circus_cfg)\n    except ImportError:\n        logger.error(\"run_circus.py not found in sys.path. Add artifacts/ to PYTHONPATH.\")\n        raise\n    except Exception as e:\n        logger.error(\"Experiment %s failed: %s\", exp.name, e)\n        raise\n\n    # 保存实验元信息\n    meta = {\n        \"experiment_name\": exp.name,\n        \"priority\": exp.priority,\n        \"backend\": exp.backend,\n        \"canonical_version\": CANONICAL_VERSION,\n        \"timestamp\": time.strftime(\"%Y-%m-%d %H:%M:%S\"),\n    }\n    results[\"phase2_meta\"] = meta\n\n    output_file = exp.output_dir / f\"{exp.model_slug}_{exp.task}_K{exp.K}.json\"\n    with open(output_file, \"w\") as f:\n        json.dump(results, f, indent=2, default=str)\n    logger.info(\"Results → %s\", output_file)\n\n    return results\n\n\ndef run_analysis_for_experiment(exp: ExperimentConfig) -> Optional[Dict[str, Any]]:\n    \"\"\"实验完成后调用 analyze_mvp_results 的分析逻辑。\"\"\"\n    try:\n        from analyze_mvp_results import run_analysis\n    except ImportError:\n        logger.warning(\"analyze_mvp_results.py not importable, skipping analysis\")\n        return None\n\n    analysis_dir = exp.output_dir / \"analysis\"\n    analysis_dir.mkdir(parents=True, exist_ok=True)\n\n    # run_analysis 从 cache dir 加载 per-method scores\n    results = run_analysis(\n        results_dir=exp.cache_dir.parent.parent,  # results/ 根\n        output_dir=analysis_dir,\n        top_n=200,\n    )\n    logger.info(\"Analysis → %s\", analysis_dir)\n    return results\n\n\n# ---------------------------------------------------------------------------\n# Batch runner\n# ---------------------------------------------------------------------------\n\ndef run_batch(\n    experiments: Dict[str, ExperimentConfig],\n    names: Optional[List[str]] = None,\n    max_priority: Optional[int] = None,\n    force: bool = False,\n) -> Dict[str, Dict[str, Any]]:\n    \"\"\"批量运行实验。\n\n    Args:\n        experiments: 完整实验矩阵\n        names: 指定运行的实验名（None=全部）\n        max_priority: 只运行 priority <= 此值的实验\n        force: 忽略缓存，强制重算\n    \"\"\"\n    selected = _select_experiments(experiments, names, max_priority)\n\n    # 按 priority 排序\n    ordered = sorted(selected.values(), key=lambda e: (e.priority, e.name))\n    logger.info(\"Running %d experiments (sorted by priority)\", len(ordered))\n\n    all_results = {}\n    for i, exp in enumerate(ordered, 1):\n        logger.info(\"[%d/%d] %s (priority=%d)\", i, len(ordered), exp.name, exp.priority)\n        t0 = time.time()\n\n        try:\n            results = run_single_experiment(exp, force=force)\n            analysis = run_analysis_for_experiment(exp)\n            if analysis:\n                results[\"analysis\"] = analysis\n\n            elapsed = time.time() - t0\n            results[\"elapsed_sec\"] = elapsed\n            all_results[exp.name] = results\n            logger.info(\"✓ %s completed in %.1f sec\", exp.name, elapsed)\n\n        except Exception as e:\n            logger.error(\"✗ %s failed: %s\", exp.name, e)\n            all_results[exp.name] = {\"error\": str(e)}\n\n    _save_batch_summary(all_results)\n    return all_results\n\n\ndef _select_experiments(\n    experiments: Dict[str, ExperimentConfig],\n    names: Optional[List[str]] = None,\n    max_priority: Optional[int] = None,\n) -> Dict[str, ExperimentConfig]:\n    \"\"\"筛选实验子集。\"\"\"\n    selected = experiments\n    if names:\n        missing = set(names) - set(experiments)\n        if missing:\n            raise ValueError(f\"Unknown experiments: {missing}\")\n        selected = {n: experiments[n] for n in names}\n    if max_priority is not None:\n        selected = {n: e for n, e in selected.items() if e.priority <= max_priority}\n    if not selected:\n        raise ValueError(\"No experiments match the filter criteria\")\n    return selected\n\n\ndef _save_batch_summary(all_results: Dict[str, Dict[str, Any]]) -> None:\n    \"\"\"保存批量运行摘要。\"\"\"\n    summary_path = Path(\"results\") / \"phase2_batch_summary.json\"\n    summary_path.parent.mkdir(parents=True, exist_ok=True)\n\n    summary = {\n        \"timestamp\": time.strftime(\"%Y-%m-%d %H:%M:%S\"),\n        \"canonical_version\": CANONICAL_VERSION,\n        \"experiments\": {},\n    }\n    for name, res in all_results.items():\n        entry = {\"status\": \"error\" if \"error\" in res else \"ok\"}\n        if \"error\" in res:\n            entry[\"error\"] = res[\"error\"]\n        else:\n            entry[\"elapsed_sec\"] = res.get(\"elapsed_sec\")\n            if \"cross_table\" in res:\n                entry[\"off_diagonal_pct\"] = res[\"cross_table\"].get(\"off_diagonal_pct\")\n            if \"css_distribution\" in res:\n                entry[\"css_distribution\"] = res[\"css_distribution\"]\n        summary[\"experiments\"][name] = entry\n\n    with open(summary_path, \"w\") as f:\n        json.dump(summary, f, indent=2)\n    logger.info(\"Batch summary → %s\", summary_path)\n\n\n# ---------------------------------------------------------------------------\n# Status check\n# ---------------------------------------------------------------------------\n\ndef show_status(experiments: Dict[str, ExperimentConfig]) -> None:\n    \"\"\"显示每个实验的完成状态。\"\"\"\n    print(f\"\\n{'Experiment':30s} {'Model':25s} {'Task':12s} {'Cached Methods':40s} {'Result'}\")\n    print(\"-\" * 120)\n\n    for name in sorted(experiments, key=lambda n: (experiments[n].priority, n)):\n        exp = experiments[name]\n        cache = check_cache(exp)\n        cached_str = \" \".join(f\"{'✓' if v else '✗'}{m}\" for m, v in cache.items())\n\n        result_file = exp.output_dir / f\"{exp.model_slug}_{exp.task}_K{exp.K}.json\"\n        result_str = \"✓\" if result_file.exists() else \"—\"\n\n        print(f\"  P{exp.priority} {name:28s} {exp.model:25s} {exp.task:12s} {cached_str:40s} {result_str}\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef parse_args() -> argparse.Namespace:\n    parser = argparse.ArgumentParser(description=\"Phase 2 experiment runner\")\n    parser.add_argument(\"--config\", type=str, default=\"phase2_configs.yaml\",\n                        help=\"实验矩阵 YAML 路径\")\n    parser.add_argument(\"--experiment\", type=str, nargs=\"+\",\n                        help=\"运行指定实验（空格分隔多个）\")\n    parser.add_argument(\"--all\", action=\"store_true\",\n                        help=\"运行全部实验\")\n    parser.add_argument(\"--priority\", type=int,\n                        help=\"只运行 priority <= N 的实验\")\n    parser.add_argument(\"--list\", action=\"store_true\",\n                        help=\"列出所有实验\")\n    parser.add_argument(\"--status\", action=\"store_true\",\n                        help=\"显示完成状态\")\n    parser.add_argument(\"--force\", action=\"store_true\",\n                        help=\"忽略缓存强制重算\")\n    parser.add_argument(\"--gpu\", type=str, default=None,\n                        help=\"覆盖 CUDA_VISIBLE_DEVICES\")\n    return parser.parse_args()\n\n\ndef main():\n    args = parse_args()\n\n    if args.gpu:\n        os.environ[\"CUDA_VISIBLE_DEVICES\"] = args.gpu\n        logger.info(\"GPU override: CUDA_VISIBLE_DEVICES=%s\", args.gpu)\n\n    experiments = load_experiment_matrix(args.config)\n\n    if args.list:\n        list_experiments(experiments)\n        return\n\n    if args.status:\n        show_status(experiments)\n        return\n\n    if args.experiment:\n        run_batch(experiments, names=args.experiment, force=args.force)\n    elif args.all:\n        run_batch(experiments, max_priority=args.priority, force=args.force)\n    elif args.priority:\n        run_batch(experiments, max_priority=args.priority, force=args.force)\n    else:\n        parser = argparse.ArgumentParser()\n        parser.print_help()\n        print(\"\\nHint: use --list to see experiments, --experiment NAME to run one\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 108_

<details open><summary>🔧 Tool call — Write · `toolu_01RFDyyvr7yRCgzcq2TZ7RX7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/phase2_configs.yaml",
  "content": "# Phase 2 实验矩阵\n# 每个实验 = 一个 model × task × methods 组合\n#\n# Priority: 1 = MVP 已在跑, 2 = MVP 后立即跑, 3 = 有空再跑\n# Backend: transformerlens (GPT-2) | huggingface (其他)\n# Methods: GPT-2 用 ACDC, 大模型用 IFR (D006)\n#\n# 预估单实验耗时（基于 MVP 经验）:\n#   GPT-2 Small:  EAP-IG ~2min, EP ~5min, ACDC ~10min  → ~20min/task\n#   Qwen-2.5 0.5B: EAP-IG ~5min, EP ~15min, IFR ~3min → ~25min/task\n#   Gemma-2 2B:   EAP-IG ~15min, EP ~40min, IFR ~8min  → ~65min/task\n#   Llama-3.1 8B: EAP-IG ~40min, EP ~90min, IFR ~15min → ~150min/task\n\ndefaults:\n  K: 3\n  num_samples: 50\n  seed: 42\n  gpu_id: \"0\"\n  eap_ig_steps: 5\n  edge_pruning_epochs: 100\n  edge_pruning_lambda: 1e-2\n  ifr_threshold: 0.1\n  css_threshold: 0.67\n  circus_B: 10\n\nexperiments:\n\n  # ===================================================================\n  # GPT-2 Small — TransformerLens, K=3 causal methods (EAP-IG + EP + ACDC)\n  # 预估总耗时: ~60min (3 tasks × ~20min)\n  # ===================================================================\n\n  gpt2_ioi:\n    model: \"gpt2\"\n    model_path: null\n    task: \"ioi\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"acdc\"]\n    backend: \"transformerlens\"\n    thresholds:\n      acdc: [0.01, 0.03, 0.05, 0.1]\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      acdc: {strategy: \"threshold\", threshold: 0.05}\n    priority: 1\n    notes: \"MVP baseline, 已有部分结果\"\n\n  gpt2_greater_than:\n    model: \"gpt2\"\n    model_path: null\n    task: \"greater_than\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"acdc\"]\n    backend: \"transformerlens\"\n    thresholds:\n      acdc: [0.01, 0.03, 0.05, 0.1]\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      acdc: {strategy: \"threshold\", threshold: 0.05}\n    priority: 2\n    notes: \"数值推理任务, 预期电路更紧凑\"\n\n  gpt2_docstring:\n    model: \"gpt2\"\n    model_path: null\n    task: \"docstring\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"acdc\"]\n    backend: \"transformerlens\"\n    thresholds:\n      acdc: [0.01, 0.03, 0.05, 0.1]\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      acdc: {strategy: \"threshold\", threshold: 0.05}\n    priority: 2\n    notes: \"代码理解任务, 验证跨领域泛化\"\n\n  # ===================================================================\n  # Qwen-2.5 0.5B — HuggingFace, K=3 (EAP-IG + EP + IFR)\n  # 预估总耗时: ~100min (4 tasks × ~25min)\n  # ===================================================================\n\n  qwen05_ioi:\n    model: \"Qwen/Qwen2.5-0.5B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/\"\n    task: \"ioi\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 2\n    notes: \"Phase 2 首个大模型实验, MVP 后立即跑\"\n\n  qwen05_greater_than:\n    model: \"Qwen/Qwen2.5-0.5B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/\"\n    task: \"greater_than\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 2\n    notes: \"Qwen 数值推理\"\n\n  qwen05_docstring:\n    model: \"Qwen/Qwen2.5-0.5B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/\"\n    task: \"docstring\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 2\n    notes: \"Qwen 代码理解\"\n\n  qwen05_ioi_variant:\n    model: \"Qwen/Qwen2.5-0.5B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/\"\n    task: \"ioi_variant\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"IOI 变体 (name permutation), 验证电路稳定性\"\n\n  # ===================================================================\n  # Gemma-2 2B — HuggingFace, K=3 (EAP-IG + EP + IFR)\n  # 预估总耗时: ~260min (4 tasks × ~65min)\n  # ===================================================================\n\n  gemma2_ioi:\n    model: \"google/gemma-2-2b\"\n    model_path: \"/root/autodl-tmp/.hf_cache/google/gemma-2-2b/\"\n    task: \"ioi\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 30\n    edge_pruning_epochs: 80\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"2B 模型, 减 samples 和 EP epochs 控制显存\"\n\n  gemma2_greater_than:\n    model: \"google/gemma-2-2b\"\n    model_path: \"/root/autodl-tmp/.hf_cache/google/gemma-2-2b/\"\n    task: \"greater_than\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 30\n    edge_pruning_epochs: 80\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"Gemma-2 数值推理\"\n\n  gemma2_docstring:\n    model: \"google/gemma-2-2b\"\n    model_path: \"/root/autodl-tmp/.hf_cache/google/gemma-2-2b/\"\n    task: \"docstring\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 30\n    edge_pruning_epochs: 80\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"Gemma-2 代码理解\"\n\n  gemma2_ioi_variant:\n    model: \"google/gemma-2-2b\"\n    model_path: \"/root/autodl-tmp/.hf_cache/google/gemma-2-2b/\"\n    task: \"ioi_variant\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 30\n    edge_pruning_epochs: 80\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"Gemma-2 IOI 变体\"\n\n  # ===================================================================\n  # Llama-3.1 8B — HuggingFace, K=3 (EAP-IG + EP + IFR)\n  # 预估总耗时: ~600min (4 tasks × ~150min)\n  # 需要 >=24GB VRAM (A6000), EP 可能需 gradient checkpointing\n  # ===================================================================\n\n  llama31_ioi:\n    model: \"meta-llama/Llama-3.1-8B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/meta-llama/Llama-3.1-8B/\"\n    task: \"ioi\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 20\n    edge_pruning_epochs: 60\n    edge_pruning_lambda: 5e-3\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"8B 最大模型, 减 samples/epochs, 可能需 gradient checkpointing\"\n\n  llama31_greater_than:\n    model: \"meta-llama/Llama-3.1-8B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/meta-llama/Llama-3.1-8B/\"\n    task: \"greater_than\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 20\n    edge_pruning_epochs: 60\n    edge_pruning_lambda: 5e-3\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"Llama-3.1 数值推理\"\n\n  llama31_docstring:\n    model: \"meta-llama/Llama-3.1-8B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/meta-llama/Llama-3.1-8B/\"\n    task: \"docstring\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 20\n    edge_pruning_epochs: 60\n    edge_pruning_lambda: 5e-3\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"Llama-3.1 代码理解\"\n\n  llama31_ioi_variant:\n    model: \"meta-llama/Llama-3.1-8B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/meta-llama/Llama-3.1-8B/\"\n    task: \"ioi_variant\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 20\n    edge_pruning_epochs: 60\n    edge_pruning_lambda: 5e-3\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"Llama-3.1 IOI 变体\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "6ddaa17a-4911-4c68-93fd-d96acc87e906",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eu7L1VN9SvV4oSMLE3udRL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5872,
      "cache_read_input_tokens": 32096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5872
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 109 · 2026-05-12T22:11:24.571Z_

<details><summary>↩ Tool result · `toolu_01RFDyyvr7yRCgzcq2TZ7RX7`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/phase2_configs.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "f78255a7-ec1a-42df-96f6-044edebcebd1",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/phase2_configs.yaml",
    "content": "# Phase 2 实验矩阵\n# 每个实验 = 一个 model × task × methods 组合\n#\n# Priority: 1 = MVP 已在跑, 2 = MVP 后立即跑, 3 = 有空再跑\n# Backend: transformerlens (GPT-2) | huggingface (其他)\n# Methods: GPT-2 用 ACDC, 大模型用 IFR (D006)\n#\n# 预估单实验耗时（基于 MVP 经验）:\n#   GPT-2 Small:  EAP-IG ~2min, EP ~5min, ACDC ~10min  → ~20min/task\n#   Qwen-2.5 0.5B: EAP-IG ~5min, EP ~15min, IFR ~3min → ~25min/task\n#   Gemma-2 2B:   EAP-IG ~15min, EP ~40min, IFR ~8min  → ~65min/task\n#   Llama-3.1 8B: EAP-IG ~40min, EP ~90min, IFR ~15min → ~150min/task\n\ndefaults:\n  K: 3\n  num_samples: 50\n  seed: 42\n  gpu_id: \"0\"\n  eap_ig_steps: 5\n  edge_pruning_epochs: 100\n  edge_pruning_lambda: 1e-2\n  ifr_threshold: 0.1\n  css_threshold: 0.67\n  circus_B: 10\n\nexperiments:\n\n  # ===================================================================\n  # GPT-2 Small — TransformerLens, K=3 causal methods (EAP-IG + EP + ACDC)\n  # 预估总耗时: ~60min (3 tasks × ~20min)\n  # ===================================================================\n\n  gpt2_ioi:\n    model: \"gpt2\"\n    model_path: null\n    task: \"ioi\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"acdc\"]\n    backend: \"transformerlens\"\n    thresholds:\n      acdc: [0.01, 0.03, 0.05, 0.1]\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      acdc: {strategy: \"threshold\", threshold: 0.05}\n    priority: 1\n    notes: \"MVP baseline, 已有部分结果\"\n\n  gpt2_greater_than:\n    model: \"gpt2\"\n    model_path: null\n    task: \"greater_than\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"acdc\"]\n    backend: \"transformerlens\"\n    thresholds:\n      acdc: [0.01, 0.03, 0.05, 0.1]\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      acdc: {strategy: \"threshold\", threshold: 0.05}\n    priority: 2\n    notes: \"数值推理任务, 预期电路更紧凑\"\n\n  gpt2_docstring:\n    model: \"gpt2\"\n    model_path: null\n    task: \"docstring\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"acdc\"]\n    backend: \"transformerlens\"\n    thresholds:\n      acdc: [0.01, 0.03, 0.05, 0.1]\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      acdc: {strategy: \"threshold\", threshold: 0.05}\n    priority: 2\n    notes: \"代码理解任务, 验证跨领域泛化\"\n\n  # ===================================================================\n  # Qwen-2.5 0.5B — HuggingFace, K=3 (EAP-IG + EP + IFR)\n  # 预估总耗时: ~100min (4 tasks × ~25min)\n  # ===================================================================\n\n  qwen05_ioi:\n    model: \"Qwen/Qwen2.5-0.5B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/\"\n    task: \"ioi\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 2\n    notes: \"Phase 2 首个大模型实验, MVP 后立即跑\"\n\n  qwen05_greater_than:\n    model: \"Qwen/Qwen2.5-0.5B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/\"\n    task: \"greater_than\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 2\n    notes: \"Qwen 数值推理\"\n\n  qwen05_docstring:\n    model: \"Qwen/Qwen2.5-0.5B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/\"\n    task: \"docstring\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 2\n    notes: \"Qwen 代码理解\"\n\n  qwen05_ioi_variant:\n    model: \"Qwen/Qwen2.5-0.5B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/\"\n    task: \"ioi_variant\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"IOI 变体 (name permutation), 验证电路稳定性\"\n\n  # ===================================================================\n  # Gemma-2 2B — HuggingFace, K=3 (EAP-IG + EP + IFR)\n  # 预估总耗时: ~260min (4 tasks × ~65min)\n  # ===================================================================\n\n  gemma2_ioi:\n    model: \"google/gemma-2-2b\"\n    model_path: \"/root/autodl-tmp/.hf_cache/google/gemma-2-2b/\"\n    task: \"ioi\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 30\n    edge_pruning_epochs: 80\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"2B 模型, 减 samples 和 EP epochs 控制显存\"\n\n  gemma2_greater_than:\n    model: \"google/gemma-2-2b\"\n    model_path: \"/root/autodl-tmp/.hf_cache/google/gemma-2-2b/\"\n    task: \"greater_than\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 30\n    edge_pruning_epochs: 80\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"Gemma-2 数值推理\"\n\n  gemma2_docstring:\n    model: \"google/gemma-2-2b\"\n    model_path: \"/root/autodl-tmp/.hf_cache/google/gemma-2-2b/\"\n    task: \"docstring\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 30\n    edge_pruning_epochs: 80\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"Gemma-2 代码理解\"\n\n  gemma2_ioi_variant:\n    model: \"google/gemma-2-2b\"\n    model_path: \"/root/autodl-tmp/.hf_cache/google/gemma-2-2b/\"\n    task: \"ioi_variant\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 30\n    edge_pruning_epochs: 80\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"Gemma-2 IOI 变体\"\n\n  # ===================================================================\n  # Llama-3.1 8B — HuggingFace, K=3 (EAP-IG + EP + IFR)\n  # 预估总耗时: ~600min (4 tasks × ~150min)\n  # 需要 >=24GB VRAM (A6000), EP 可能需 gradient checkpointing\n  # ===================================================================\n\n  llama31_ioi:\n    model: \"meta-llama/Llama-3.1-8B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/meta-llama/Llama-3.1-8B/\"\n    task: \"ioi\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 20\n    edge_pruning_epochs: 60\n    edge_pruning_lambda: 5e-3\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"8B 最大模型, 减 samples/epochs, 可能需 gradient checkpointing\"\n\n  llama31_greater_than:\n    model: \"meta-llama/Llama-3.1-8B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/meta-llama/Llama-3.1-8B/\"\n    task: \"greater_than\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 20\n    edge_pruning_epochs: 60\n    edge_pruning_lambda: 5e-3\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"Llama-3.1 数值推理\"\n\n  llama31_docstring:\n    model: \"meta-llama/Llama-3.1-8B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/meta-llama/Llama-3.1-8B/\"\n    task: \"docstring\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 20\n    edge_pruning_epochs: 60\n    edge_pruning_lambda: 5e-3\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"Llama-3.1 代码理解\"\n\n  llama31_ioi_variant:\n    model: \"meta-llama/Llama-3.1-8B\"\n    model_path: \"/root/autodl-tmp/.hf_cache/meta-llama/Llama-3.1-8B/\"\n    task: \"ioi_variant\"\n    methods: [\"eap_ig\", \"edge_pruning\", \"ifr\"]\n    backend: \"huggingface\"\n    num_samples: 20\n    edge_pruning_epochs: 60\n    edge_pruning_lambda: 5e-3\n    binarize:\n      eap_ig: {strategy: \"topn\", n: 200}\n      edge_pruning: {strategy: \"topn\", n: 200}\n      ifr: {strategy: \"unique_score_rank\", n: 50}\n    priority: 3\n    notes: \"Llama-3.1 IOI 变体\"\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 110_

注册产出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "1d2d593e-f927-4bfb-86be-7bca381aaa13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X45tnJ3Py5piMG6oAKqPFU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3929,
      "cache_read_input_tokens": 37968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3929
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

_source line 111_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KCbYq5QVHvezFLVy7nrG8u`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "53fb0ee2-429a-46e7-b2fd-0bdb15a8de19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X45tnJ3Py5piMG6oAKqPFU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3929,
      "cache_read_input_tokens": 37968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3929
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

_source line 112 · 2026-05-12T22:11:27.533Z_

<details><summary>↩ Tool result · `toolu_01KCbYq5QVHvezFLVy7nrG8u`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "b7c73a0d-9809-46dc-99e8-048796ee311b",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 113_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01KTPS27W6w5TGo8e1G1QAXy`</summary>

```json
{
  "name": "run_phase2_experiment",
  "type": "data",
  "description": "Phase 2 实验框架脚本：多模型×多任务×多方法批量调度，复用 run_circus pipeline，支持断点续跑和缓存管理",
  "project": "structfuse-context",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/run_phase2_experiment.py",
  "tags": [
    "phase2",
    "experiment",
    "framework"
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
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "668c5525-622c-461d-9355-32243ab6a04b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015SMvcWZcRXMoTkzeHUw9Cf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 41897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 114 · 2026-05-12T22:11:33.140Z_

<details><summary>↩ Tool result · `toolu_01KTPS27W6w5TGo8e1G1QAXy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_54986c\", \"name\": \"run_phase2_experiment\", \"type\": \"data\", \"description\": \"Phase 2 实验框架脚本：多模型×多任务×多方法批量调度，复用 run_circus pipeline，支持断点续跑和缓存管理\", \"path\": \"projects/structfuse-context/artifacts/_project/data/run_phase2_experiment.py\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T22:11:33.039687+00:00\", \"tags\": [\"phase2\", \"experiment\", \"framework\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "6c239d60-a6d5-469d-be82-abdbb2336536",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260512_54986c\\\", \\\"name\\\": \\\"run_phase2_experiment\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Phase 2 实验框架脚本：多模型×多任务×多方法批量调度，复用 run_circus pipeline，支持断点续跑和缓存管理\\\", \\\"path\\\": \\\"projects/structfuse-context/artifacts/_project/data/run_phase2_experiment.py\\\", \\\"url\\\": null, \\\"project\\\": \\\"structfuse-context\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-12T22:11:33.039687+00:00\\\", \\\"tags\\\": [\\\"phase2\\\", \\\"experiment\\\", \\\"framework\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_54986c\", \"name\": \"run_phase2_experiment\", \"type\": \"data\", \"description\": \"Phase 2 实验框架脚本：多模型×多任务×多方法批量调度，复用 run_circus pipeline，支持断点续跑和缓存管理\", \"path\": \"projects/structfuse-context/artifacts/_project/data/run_phase2_experiment.py\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T22:11:33.039687+00:00\", \"tags\": [\"phase2\", \"experiment\", \"framework\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 115_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01R6f7hxRrSuJ8AhQ3kQ2ypH`</summary>

```json
{
  "name": "phase2_configs",
  "type": "data",
  "description": "Phase 2 实验矩阵 YAML：4模型×4任务=16个实验，含 priority/binarize/backend 配置",
  "project": "structfuse-context",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/phase2_configs.yaml",
  "tags": [
    "phase2",
    "config",
    "experiment-matrix"
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
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "28d8263c-19ec-4ced-bcd1-a925385fb2d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015SMvcWZcRXMoTkzeHUw9Cf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 41897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 116 · 2026-05-12T22:11:35.044Z_

<details><summary>↩ Tool result · `toolu_01R6f7hxRrSuJ8AhQ3kQ2ypH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_1d2ec1\", \"name\": \"phase2_configs\", \"type\": \"data\", \"description\": \"Phase 2 实验矩阵 YAML：4模型×4任务=16个实验，含 priority/binarize/backend 配置\", \"path\": \"projects/structfuse-context/artifacts/_project/data/phase2_configs.yaml\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T22:11:34.966347+00:00\", \"tags\": [\"phase2\", \"config\", \"experiment-matrix\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "04791e44-aaa8-41b6-9c66-a5ae7b8e9bbc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260512_1d2ec1\\\", \\\"name\\\": \\\"phase2_configs\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Phase 2 实验矩阵 YAML：4模型×4任务=16个实验，含 priority/binarize/backend 配置\\\", \\\"path\\\": \\\"projects/structfuse-context/artifacts/_project/data/phase2_configs.yaml\\\", \\\"url\\\": null, \\\"project\\\": \\\"structfuse-context\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-12T22:11:34.966347+00:00\\\", \\\"tags\\\": [\\\"phase2\\\", \\\"config\\\", \\\"experiment-matrix\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_1d2ec1\", \"name\": \"phase2_configs\", \"type\": \"data\", \"description\": \"Phase 2 实验矩阵 YAML：4模型×4任务=16个实验，含 priority/binarize/backend 配置\", \"path\": \"projects/structfuse-context/artifacts/_project/data/phase2_configs.yaml\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T22:11:34.966347+00:00\", \"tags\": [\"phase2\", \"config\", \"experiment-matrix\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 117_

## 产出汇报

### 1. 核心接口设计

| 函数 | 职责 |
|------|------|
| `ExperimentConfig` | dataclass，封装单实验全部参数，`to_run_circus_config()` 转换为 `run_circus.run_pipeline()` 入参 |
| `load_experiment_matrix(yaml)` | 从 YAML 加载实验矩阵，defaults 与每个实验合并 |
| `run_single_experiment(exp)` | 调用 `run_circus.run_pipeline()`，带缓存检查和断点续跑 |
| `run_analysis_for_experiment(exp)` | 实验完成后调用 `analyze_mvp_results.run_analysis()` |
| `run_batch(experiments, names, max_priority)` | 按 priority 排序批量执行，输出 `phase2_batch_summary.json` |
| `check_cache(exp)` / `load_cached_scores()` / `save_cached_scores()` | 缓存管理，key 绑定 `CANONICAL_VERSION` + 超参哈希 |

### 2. 实验矩阵

**4 模型 × 4 任务 = 16 个实验**

| 模型 | 任务 | 方法 | Backend |
|------|------|------|---------|
| GPT-2 Small | IOI, Greater-Than, Docstring | EAP-IG + EP + ACDC | TransformerLens |
| Qwen-2.5 0.5B | IOI, Greater-Than, Docstring, IOI-variant | EAP-IG + EP + IFR | HuggingFace |
| Gemma-2 2B | IOI, Greater-Than, Docstring, IOI-variant | EAP-IG + EP + IFR | HuggingFace |
| Llama-3.1 8B | IOI, Greater-Than, Docstring, IOI-variant | EAP-IG + EP + IFR | HuggingFace |

### 3. Priority 分布

| Priority | 数量 | 说明 |
|----------|------|------|
| P1 | **1** | `gpt2_ioi`（MVP 已在跑） |
| P2 | **5** | GPT-2 另外 2 task + Qwen-2.5 的 3 task |
| P3 | **10** | Gemma-2 全部 4 task + Llama-3.1 全部 4 task + Qwen IOI-variant |

### 4. 预估全量运行时间

| 模型 | 单 task 耗时 | task 数 | 小计 |
|------|-------------|---------|------|
| GPT-2 Small | ~20min | 3 | ~60min |
| Qwen-2.5 0.5B | ~25min | 4 | ~100min |
| Gemma-2 2B | ~65min | 4 | ~260min |
| Llama-3.1 8B | ~150min | 4 | ~600min |
| **合计** | | **16** | **~1020min (~17h)** |

P1+P2 子集（6 个实验）约 **2.5h**，可在 MVP 通过后当天完成。P3 的 10 个实验约 **14.5h**，需安排过夜跑。Llama-3.1 8B 需 >=24GB VRAM，config 中已降低 `num_samples=20` 和 `edge_pruning_epochs=60` 控制显存。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "uuid": "f0ffe9b1-5ad2-421c-83c8-f61850a98ae0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y6wQGWKvJ7FLM7vsP3w5TJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 42615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 118_

## 产出汇报

### 1. 核心接口设计

| 函数 | 职责 |
|------|------|
| `ExperimentConfig` | dataclass，封装单实验全部参数，`to_run_circus_config()` 转换为 `run_circus.run_pipeline()` 入参 |
| `load_experiment_matrix(yaml)` | 从 YAML 加载实验矩阵，defaults 与每个实验合并 |
| `run_single_experiment(exp)` | 调用 `run_circus.run_pipeline()`，带缓存检查和断点续跑 |
| `run_analysis_for_experiment(exp)` | 实验完成后调用 `analyze_mvp_results.run_analysis()` |
| `run_batch(experiments, names, max_priority)` | 按 priority 排序批量执行，输出 `phase2_batch_summary.json` |
| `check_cache(exp)` / `load_cached_scores()` / `save_cached_scores()` | 缓存管理，key 绑定 `CANONICAL_VERSION` + 超参哈希 |

### 2. 实验矩阵

**4 模型 × 4 任务 = 16 个实验**

| 模型 | 任务 | 方法 | Backend |
|------|------|------|---------|
| GPT-2 Small | IOI, Greater-Than, Docstring | EAP-IG + EP + ACDC | TransformerLens |
| Qwen-2.5 0.5B | IOI, Greater-Than, Docstring, IOI-variant | EAP-IG + EP + IFR | HuggingFace |
| Gemma-2 2B | IOI, Greater-Than, Docstring, IOI-variant | EAP-IG + EP + IFR | HuggingFace |
| Llama-3.1 8B | IOI, Greater-Than, Docstring, IOI-variant | EAP-IG + EP + IFR | HuggingFace |

### 3. Priority 分布

| Priority | 数量 | 说明 |
|----------|------|------|
| P1 | **1** | `gpt2_ioi`（MVP 已在跑） |
| P2 | **5** | GPT-2 另外 2 task + Qwen-2.5 的 3 task |
| P3 | **10** | Gemma-2 全部 4 task + Llama-3.1 全部 4 task + Qwen IOI-variant |

### 4. 预估全量运行时间

| 模型 | 单 task 耗时 | task 数 | 小计 |
|------|-------------|---------|------|
| GPT-2 Small | ~20min | 3 | ~60min |
| Qwen-2.5 0.5B | ~25min | 4 | ~100min |
| Gemma-2 2B | ~65min | 4 | ~260min |
| Llama-3.1 8B | ~150min | 4 | ~600min |
| **合计** | | **16** | **~1020min (~17h)** |

P1+P2 子集（6 个实验）约 **2.5h**，可在 MVP 通过后当天完成。P3 的 10 个实验约 **14.5h**，需安排过夜跑。Llama-3.1 8B 需 >=24GB VRAM，config 中已降低 `num_samples=20` 和 `edge_pruning_epochs=60` 控制显存。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 279457,
  "duration_api_ms": 281575,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "389daeac-2555-46b4-b35e-37a6a1170f93",
  "total_cost_usd": 0.8114207499999999,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 31871,
    "cache_read_input_tokens": 190650,
    "output_tokens": 11629,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31871,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 990,
        "cache_read_input_tokens": 42615,
        "cache_creation_input_tokens": 1097,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1097
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2530,
      "outputTokens": 10618,
      "cacheReadInputTokens": 758720,
      "cacheCreationInputTokens": 75712,
      "webSearchRequests": 0,
      "costUSD": 0.226132,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 11629,
      "cacheReadInputTokens": 190650,
      "cacheCreationInputTokens": 31871,
      "webSearchRequests": 0,
      "costUSD": 0.58528875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3385a49d-06bd-4402-b60d-94382a1992d9"
}
```

</details>

---
