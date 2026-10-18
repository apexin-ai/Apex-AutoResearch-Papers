# paper compile check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/workers/worker_paper_compile_check_20260514T121430.log`
- **Structured JSON:** [`4eb60f0fcac0302e68bf.json`](../../sessions/4e/4eb60f0fcac0302e68bf.json)

## Before a recorded user message

73 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
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
  "uuid": "cedc0624-db48-44d7-b78e-b91558abcb35",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/memory/"
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
    "resetsAt": 1778922000,
    "rateLimitType": "seven_day",
    "utilization": 0.89,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "5bf93f83-4503-4533-943c-524757f96871",
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8"
}
```

---

### Assistant

_source line 4_

Let me check the paper directory structure and contents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "b6d93ea2-4e13-45c7-b2cd-24850bd88952",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Am67xCx19eW2vQJFJUJ6fX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11462,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11462
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

<details open><summary>🔧 Tool call — Glob · `toolu_01KZTyG1dHfUfMXNaU78X1t2`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "376694e1-603a-4914-bd7b-48c05417550f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Am67xCx19eW2vQJFJUJ6fX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11462,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11462
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

_source line 6 · 2026-05-14T12:14:40.705Z_

<details><summary>↩ Tool result · reported error · `toolu_01KZTyG1dHfUfMXNaU78X1t2`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/docs/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "8f35b27f-fe0b-47b7-bfae-1ab09873bb57",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/docs/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01J7PEtS6sBX4aCzniKP9zU1`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/docs/paper/figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "2950e383-5b42-496d-a8b4-63e42a84da92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Am67xCx19eW2vQJFJUJ6fX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11462,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11462
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

_source line 8 · 2026-05-14T12:14:40.872Z_

<details><summary>↩ Tool result · reported error · `toolu_01J7PEtS6sBX4aCzniKP9zU1`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/docs/paper/figures. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "d8c4d1dc-786c-45d6-8d6b-d0c5176e9117",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/docs/paper/figures. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv."
}
```

</details>

---

### Assistant

_source line 9_

论文目录不存在于指定路径。让我搜索实际位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "c80b8704-3531-4e01-8657-2cb51f7e19d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnQ3MFbDu2J3fU1R2mPB1T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 23303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
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

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_01EjJhmrvCPgVjr4e6hwaQvh`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "2a325d10-32ae-4110-805f-32c94307d03f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnQ3MFbDu2J3fU1R2mPB1T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 23303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
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

_source line 11 · 2026-05-14T12:14:44.153Z_

<details><summary>↩ Tool result · `toolu_01EjJhmrvCPgVjr4e6hwaQvh`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/worst/paper.tex
artifacts/dream_reports/dream_20260514T002109/best/paper.tex
artifacts/dream_reports/dream_20260514T002109/median/paper.tex
artifacts/dream_reports/dream_20260514T002109/worst/paper.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/conclusion.tex
docs/paper/analysis.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "c73bd452-c8d7-4ce6-b9cd-52d2eaa97bc0",
  "tool_use_result": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/best/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/median/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/worst/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/best/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/median/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/worst/paper.tex",
      "artifacts/dream_reports/dream_20260514T002109/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T002109/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T002109/worst/paper.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/introduction.tex",
      "docs/paper/main.tex",
      "docs/paper/method.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/related_work.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/analysis.tex",
      "docs/paper/experiments.tex"
    ],
    "durationMs": 17,
    "numFiles": 19,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_018KNU8qF9oDCTZjG8ppgVwe`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "f1b9a3d6-6415-4b49-94c3-560b370280fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnQ3MFbDu2J3fU1R2mPB1T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 23303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
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

_source line 13 · 2026-05-14T12:14:44.618Z_

<details><summary>↩ Tool result · `toolu_018KNU8qF9oDCTZjG8ppgVwe`</summary>

```text
artifacts/dream_reports/dream_20260514T002109/best/paper.tex
artifacts/dream_reports/dream_20260514T002109/median/paper.tex
artifacts/dream_reports/dream_20260514T002109/worst/paper.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/conclusion.tex
docs/paper/analysis.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "fdcee9c1-9fd7-4946-ad2b-d5c1be681822",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260514T002109/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T002109/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T002109/worst/paper.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/introduction.tex",
      "docs/paper/main.tex",
      "docs/paper/method.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/related_work.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/analysis.tex",
      "docs/paper/experiments.tex"
    ],
    "durationMs": 8,
    "numFiles": 13,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_013hEFwFJLYx689sDwXpUd2j`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -name \"*.tex\" -o -name \"*.bib\" 2>/dev/null | head -50",
  "description": "Find all tex and bib files in the project tree"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "7b311986-2ae1-4830-b801-16e72cead04d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnQ3MFbDu2J3fU1R2mPB1T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 23303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
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

_source line 15 · 2026-05-14T12:14:46.294Z_

<details><summary>↩ Tool result · `toolu_013hEFwFJLYx689sDwXpUd2j`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "a2aa5c5b-4104-4d7f-b501-c25542df205a",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/median/paper.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/worst/paper.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/best/paper.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/median/paper.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/worst/paper.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/best/paper.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/_project/paper/introduction.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/_project/paper/method.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/median/paper.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/worst/paper.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/paper.tex",
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

_source line 16_

论文在 `docs/paper/` 下（相对于项目根目录）。现在并行执行所有检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "a2c81602-6b31-45f9-9aa6-4908484879f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMExyHZP3Hy55cvtVe9T78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1798
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

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_01S2vHNP8wEpbJU2dZawJaBW`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "6aba47da-4f9e-4aad-bf27-c35215553378",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMExyHZP3Hy55cvtVe9T78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1798
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

_source line 18 · 2026-05-14T12:14:50.147Z_

<details><summary>↩ Tool result · `toolu_01S2vHNP8wEpbJU2dZawJaBW`</summary>

```text
docs/paper/figures/fig1_head_delta_heatmap.pdf
docs/paper/figures/fig2_compounding_curve.pdf
docs/paper/figures/fig3_allocation_comparison.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "5e0c20c3-a71a-418e-ad0a-e31c555ed3e8",
  "tool_use_result": {
    "filenames": [
      "docs/paper/figures/fig1_head_delta_heatmap.pdf",
      "docs/paper/figures/fig2_compounding_curve.pdf",
      "docs/paper/figures/fig3_allocation_comparison.pdf"
    ],
    "durationMs": 6,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Glob · `toolu_011dZUE9AmtD9nzbwUQoQXdD`</summary>

```json
{
  "pattern": "figures/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "e141a0b2-55e6-4aab-863d-a260d7515090",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMExyHZP3Hy55cvtVe9T78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1798
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

_source line 20 · 2026-05-14T12:14:50.976Z_

<details><summary>↩ Tool result · `toolu_011dZUE9AmtD9nzbwUQoQXdD`</summary>

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
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "48aa26bf-56dd-4434-8eb6-4634a3d289f6",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 12,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01GfG5gn9EGjFSqbDTX16rZL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "e9e927e9-8018-440c-aedf-ae419b35442c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMExyHZP3Hy55cvtVe9T78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1798
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

_source line 22 · 2026-05-14T12:14:51.491Z_

<details><summary>↩ Tool result · `toolu_01GfG5gn9EGjFSqbDTX16rZL`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{enumitem}
10	
11	\title{When Does Non-Uniform KV Cache Quantization Help?\\Cardinality Constraints and a Heterogeneity Diagnostic}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	\input{abstract}
20	\end{abstract}
21	
22	\input{introduction}
23	\input{related_work}
24	\input{method}
25	\input{experiments}
26	\input{analysis}
27	\input{conclusion}
28	
29	\bibliography{references}
30	
31	\end{document}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "336b6566-4952-46c8-9e33-b6cdbcc5a744",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\n\\title{When Does Non-Uniform KV Cache Quantization Help?\\\\Cardinality Constraints and a Heterogeneity Diagnostic}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{analysis}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\end{document}\n",
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

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01D3VRhjzMLoeFRUks1FLrhM`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/*.tex",
  "description": "Count lines in all tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "b8834175-35be-454e-9a57-dc5847be63d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMExyHZP3Hy55cvtVe9T78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1798
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

_source line 24 · 2026-05-14T12:14:52.043Z_

<details><summary>↩ Tool result · `toolu_01D3VRhjzMLoeFRUks1FLrhM`</summary>

```text
    7 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex
  110 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex
   19 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex
  177 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex
   50 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex
   31 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex
  118 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex
   17 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex
  529 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "b5bba331-2e96-49d6-b4fe-db73d48dca0d",
  "tool_use_result": {
    "stdout": "    7 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex\n  110 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex\n   19 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex\n  177 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex\n   50 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex\n   31 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex\n  118 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex\n   17 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex\n  529 total",
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

_source line 25_

<details open><summary>🔧 Tool call — Grep · `toolu_012KwtzfKsX6vttcmbPjMnwr`</summary>

```json
{
  "pattern": "\\\\includegraphics",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "ed052586-ad92-4020-8948-5c9ef611df89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMExyHZP3Hy55cvtVe9T78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1798
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

_source line 26 · 2026-05-14T12:14:53.127Z_

<details><summary>↩ Tool result · `toolu_012KwtzfKsX6vttcmbPjMnwr`</summary>

```text
docs/paper/analysis.tex:37:\includegraphics[width=\textwidth]{figures/fig1_head_delta_heatmap.pdf}
docs/paper/experiments.tex:74:\includegraphics[width=\columnwidth]{figures/fig3_allocation_comparison.pdf}
docs/paper/method.tex:41:\includegraphics[width=\columnwidth]{figures/fig2_compounding_curve.pdf}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "7b59178c-22a2-4094-a7f8-94661e4acc2b",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:37:\\includegraphics[width=\\textwidth]{figures/fig1_head_delta_heatmap.pdf}\ndocs/paper/experiments.tex:74:\\includegraphics[width=\\columnwidth]{figures/fig3_allocation_comparison.pdf}\ndocs/paper/method.tex:41:\\includegraphics[width=\\columnwidth]{figures/fig2_compounding_curve.pdf}",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_01GgJ2fx9hm82gdgX3LH6NJ3`</summary>

```json
{
  "pattern": "\\\\ref\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "ce91e860-2e77-41ff-a82a-ffa595859e07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMExyHZP3Hy55cvtVe9T78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1798
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

_source line 28 · 2026-05-14T12:14:53.871Z_

<details><summary>↩ Tool result · `toolu_01GgJ2fx9hm82gdgX3LH6NJ3`</summary>

```text
docs/paper/analysis.tex:42:Figure~\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.
docs/paper/experiments.tex:70:Figure~\ref{fig:allocation} visualizes the bit-width allocation on Qwen, showing how constrained MCKP protects Layer-0 heads at 8-bit while selectively assigning only the 8 least-sensitive heads to 2-bit.
docs/paper/method.tex:55:Figure~\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\times$ compression.
docs/paper/method.tex:67:The constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\ref{fig:compounding}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "0f4b7886-ccb7-4ba9-a407-4ac3251598ea",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:42:Figure~\\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.\ndocs/paper/experiments.tex:70:Figure~\\ref{fig:allocation} visualizes the bit-width allocation on Qwen, showing how constrained MCKP protects Layer-0 heads at 8-bit while selectively assigning only the 8 least-sensitive heads to 2-bit.\ndocs/paper/method.tex:55:Figure~\\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\\times$ compression.\ndocs/paper/method.tex:67:The constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\\ref{fig:compounding}).",
    "numLines": 4
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Grep · `toolu_015wiPucpZGA9uU9jYPXNwK6`</summary>

```json
{
  "pattern": "\\\\label\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "d4be6ea3-66c5-4521-bbf3-aca49a13e4eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMExyHZP3Hy55cvtVe9T78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1798
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

_source line 30 · 2026-05-14T12:14:57.673Z_

<details><summary>↩ Tool result · `toolu_015wiPucpZGA9uU9jYPXNwK6`</summary>

```text
docs/paper/analysis.tex:39:\label{fig:heatmap}
docs/paper/experiments.tex:76:\label{fig:allocation}
docs/paper/method.tex:43:\label{fig:compounding}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "e406e8f5-40b1-4c01-87d2-d09a7f12e459",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:39:\\label{fig:heatmap}\ndocs/paper/experiments.tex:76:\\label{fig:allocation}\ndocs/paper/method.tex:43:\\label{fig:compounding}",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Grep · `toolu_01Fe6RLoH3tvMPPt4b8aCGHc`</summary>

```json
{
  "pattern": "\\\\ref\\{tab:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "982a59f7-ebc0-4b53-a2f4-38565225e0ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMExyHZP3Hy55cvtVe9T78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1798
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

_source line 32 · 2026-05-14T12:14:57.911Z_

<details><summary>↩ Tool result · `toolu_01Fe6RLoH3tvMPPt4b8aCGHc`</summary>

```text
docs/paper/analysis.tex:11:Table~\ref{tab:heterogeneity} summarizes the results across three architectures at $4\times$ compression.
docs/paper/experiments.tex:55:Table~\ref{tab:main_results} summarizes the main results.
docs/paper/experiments.tex:98:Table~\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.
docs/paper/experiments.tex:130:Table~\ref{tab:heuristic} compares profiling-guided MCKP against heuristic baselines that use the same Layer-0 protection but assign 2-bit heads without profiling.
docs/paper/experiments.tex:164:Table~\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.
docs/paper/method.tex:102:Table~\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "1173879d-edac-4699-829a-e7479490f4fd",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:11:Table~\\ref{tab:heterogeneity} summarizes the results across three architectures at $4\\times$ compression.\ndocs/paper/experiments.tex:55:Table~\\ref{tab:main_results} summarizes the main results.\ndocs/paper/experiments.tex:98:Table~\\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.\ndocs/paper/experiments.tex:130:Table~\\ref{tab:heuristic} compares profiling-guided MCKP against heuristic baselines that use the same Layer-0 protection but assign 2-bit heads without profiling.\ndocs/paper/experiments.tex:164:Table~\\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.\ndocs/paper/method.tex:102:Table~\\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.",
    "numLines": 6
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Grep · `toolu_01Dc3yxbRp39trpkHZHkPdgx`</summary>

```json
{
  "pattern": "\\\\label\\{tab:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "a3b1dbe9-3a09-4986-b619-7a601d0b4047",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMExyHZP3Hy55cvtVe9T78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 23693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1798
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

_source line 34 · 2026-05-14T12:14:57.977Z_

<details><summary>↩ Tool result · `toolu_01Dc3yxbRp39trpkHZHkPdgx`</summary>

```text
docs/paper/analysis.tex:22:\label{tab:heterogeneity}
docs/paper/experiments.tex:42:\label{tab:main_results}
docs/paper/experiments.tex:86:\label{tab:budget_sweep}
docs/paper/experiments.tex:117:\label{tab:heuristic}
docs/paper/experiments.tex:148:\label{tab:downstream}
docs/paper/method.tex:85:\label{tab:solver_equiv}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "af5ab945-e54b-4a60-b811-a39f3f444ca0",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:22:\\label{tab:heterogeneity}\ndocs/paper/experiments.tex:42:\\label{tab:main_results}\ndocs/paper/experiments.tex:86:\\label{tab:budget_sweep}\ndocs/paper/experiments.tex:117:\\label{tab:heuristic}\ndocs/paper/experiments.tex:148:\\label{tab:downstream}\ndocs/paper/method.tex:85:\\label{tab:solver_equiv}",
    "numLines": 6
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Good, I have all the key data. Now let me check the numerical precision of PPL values. Let me also read the tex files to check for PPL numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "52731d78-5cee-4e8e-a405-f16d2624106b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjhWxv6RbQMS2ndFHik41y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2726,
      "cache_read_input_tokens": 25491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2726
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

现在检查 PPL 数字精度一致性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "1cffeb61-3243-4220-8e65-b16686f4ddc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjhWxv6RbQMS2ndFHik41y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2726,
      "cache_read_input_tokens": 25491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2726
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

<details open><summary>🔧 Tool call — Grep · `toolu_01NcXnzE8pnJKkbsNNRNUXWg`</summary>

```json
{
  "pattern": "\\d+\\.\\d+",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "328853a1-b4e2-495f-823a-caf39834960c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjhWxv6RbQMS2ndFHik41y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2726,
      "cache_read_input_tokens": 25491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2726
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

_source line 38 · 2026-05-14T12:15:02.640Z_

<details><summary>↩ Tool result · `toolu_01NcXnzE8pnJKkbsNNRNUXWg`</summary>

```text
docs/paper/analysis.tex:12:Qwen2.5-7B exhibits the highest heterogeneity (top-5\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.
docs/paper/analysis.tex:13:Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\% improvement over uniform 4-bit.
docs/paper/analysis.tex:14:Llama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\ $+$0.38).
docs/paper/analysis.tex:15:Mistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.
docs/paper/analysis.tex:16:Here, constrained MCKP is slightly \emph{worse} than uniform ($+$0.13 vs.\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.
docs/paper/analysis.tex:28:Qwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\
docs/paper/analysis.tex:29:Llama-3.1-8B$^\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\
docs/paper/analysis.tex:30:Mistral-7B-v0.3$^\dagger$ & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\
docs/paper/analysis.tex:38:\caption{Per-head 2-bit quantization sensitivity across three models. Qwen2.5-7B (left) shows high concentration in Layer-0 heads; Llama-3.1-8B (center) shows moderate spread; Mistral-7B-v0.3 (right) shows near-zero sensitivity across all heads. Color intensity indicates PPL increase when the head is quantized to 2-bit.}
docs/paper/analysis.tex:55:  \item Concentration ${>}\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\% PPL improvement).
docs/paper/analysis.tex:56:  \item Concentration $0.30$--$0.50$: marginal benefit; depends on target compression ratio (Llama case; 0.2\% at $4\times$).
docs/paper/analysis.tex:69:At more aggressive ratios, the picture changes: at $5.3\times$ (average 3 bits), constrained MCKP achieves $45\times$ lower PPL than uniform on Llama (57.60 vs.\ 2643.77) and $44\times$ on Mistral (11.91 vs.\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.
docs/paper/analysis.tex:71:The intermediate regime ($5.3\times$) provides the largest relative benefit.
docs/paper/analysis.tex:76:We compare standard-resolution profiling (16 sequences $\times$ 512 tokens) against high-resolution profiling (64 sequences $\times$ 2048 tokens) on Qwen2.5-7B at $4\times$ compression.
docs/paper/analysis.tex:78:High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
docs/paper/analysis.tex:79:Relative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\% reduction.
docs/paper/analysis.tex:80:The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\times$ more).
docs/paper/analysis.tex:87:Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\%.
docs/paper/analysis.tex:88:The bit distribution is identical across all seeds ($\{$2-bit: 8, 4-bit: 100, 8-bit: 4$\}$), and 101 of 112 heads (90.2\%) receive the same assignment in all three runs.
docs/paper/analysis.tex:92:To validate the additive distortion assumption underlying the MCKP formulation, we compare constrained MCKP against a per-layer brute-force oracle that exhaustively enumerates all $4^4 = 256$ bit-width combinations within each 4-head group on Qwen2.5-7B (hires profiling).
docs/paper/analysis.tex:93:Of the 8 layers admitting multiple feasible allocations, MCKP matches the oracle exactly in 5; the remaining 3 show gaps of 0.018 (Layer~1), 0.014 (Layer~11), and 0.005 (Layer~4) PPL.
docs/paper/analysis.tex:95:The negligible total gap ($<0.04$ PPL) confirms that the per-head additive distortion model closely approximates the true layer-level interaction.
docs/paper/analysis.tex:102:Joint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).
docs/paper/experiments.tex:9:\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\times$ 4 KV heads = 112 KV heads),
docs/paper/experiments.tex:10:\textbf{Llama-3.1-8B} (4:1, 32 $\times$ 8 = 256 KV heads),
docs/paper/experiments.tex:11:and \textbf{Mistral-7B-v0.3} (4:1, 32 $\times$ 8 = 256 KV heads, sliding window attention).
docs/paper/experiments.tex:24:The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
docs/paper/experiments.tex:41:[Omitted long matching line]
docs/paper/experiments.tex:48:Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{11.23}$\pm$0.06 \\
docs/paper/experiments.tex:49:Llama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \textbf{8.45}$^\dagger$ \\
docs/paper/experiments.tex:50:Mistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\dagger\ddagger}$ \\
docs/paper/experiments.tex:56:On Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\% reduction over uniform 4-bit (15.45).
docs/paper/experiments.tex:57:Higher-resolution profiling (64 seq $\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in \S\ref{sec:profiling_resolution}.
docs/paper/experiments.tex:58:Without the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.
docs/paper/experiments.tex:60:Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 (std is 1.3\% of the uniform gap), with 90.2\% three-way allocation agreement, confirming profiling stability.
docs/paper/experiments.tex:62:On Llama-3.1-8B, the improvement is marginal: 8.45 vs.\ 8.47 (0.2\%).
docs/paper/experiments.tex:65:On Mistral-7B-v0.3, constrained MCKP (7.16) is slightly worse than uniform (7.13, $+$0.4\%).
docs/paper/experiments.tex:75:\caption{Bit-width allocation on Qwen2.5-7B at 4$\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}
docs/paper/experiments.tex:85:\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\geq$4$\times$). Standard-resolution profiling; hires results in \S\ref{sec:profiling_resolution}.}
docs/paper/experiments.tex:91:2$\times$ & 10.10 & 10.66 & $-$0.56 \\
docs/paper/experiments.tex:92:4$\times$ & 15.45 & 11.23 & $+$4.21 \\
docs/paper/experiments.tex:98:Table~\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.
docs/paper/experiments.tex:100:At 2$\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\ 9.81 bf16, $+$0.29).
docs/paper/experiments.tex:101:Per-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.
docs/paper/experiments.tex:103:At 4$\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\% improvement.
docs/paper/experiments.tex:104:Hires profiling further reduces this to 10.91 (\S\ref{sec:profiling_resolution}).
docs/paper/experiments.tex:123:Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\pm$0.47 & 12.23 \\
docs/paper/experiments.tex:124:Llama-3.1-8B    & 8.45  & 8.62  & 8.62$\pm$0.07  & 8.58 \\
docs/paper/experiments.tex:125:Mistral-7B-v0.3 & 7.16  & 7.24  & 7.24$\pm$0.07  & 7.21 \\
docs/paper/experiments.tex:132:On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.
docs/paper/experiments.tex:134:On Llama ($k{=}2$), the gap between methods is small: MCKP achieves 8.45 vs.\ L0-random 8.62 and naive positional 8.58.
docs/paper/experiments.tex:135:With only 2 heads assigned to 2-bit, the choice of which heads to compress has limited impact, and all methods cluster within 0.17 PPL.
docs/paper/experiments.tex:138:On Mistral ($k{=}4$), all non-uniform strategies are worse than uniform 4-bit (7.13): MCKP 7.16, naive 7.21, L0-random 7.24$\pm$0.07.
docs/paper/experiments.tex:139:MCKP outperforms both heuristics, but the best non-uniform result (7.16) still exceeds uniform by 0.03 PPL, reinforcing that non-uniform allocation is counterproductive when heterogeneity is low.
docs/paper/experiments.tex:147:\caption{0-shot accuracy on Qwen2.5-7B at 4$\times$ compression. Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization.}
docs/paper/experiments.tex:154:ARC-C      & ---   & 0.482 & 0.514 & $+$3.2 pts \\
docs/paper/experiments.tex:155:HellaSwag  & ---   & 0.728 & 0.768 & $+$4.0 pts \\
docs/paper/experiments.tex:156:PIQA       & ---   & 0.766 & 0.779 & $+$1.3 pts \\
docs/paper/experiments.tex:157:WinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\
docs/paper/experiments.tex:159:Average    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\
docs/paper/experiments.tex:164:Table~\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.
docs/paper/experiments.tex:165:Constrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\ 0.660), with gains on all four benchmarks.
docs/paper/experiments.tex:166:The largest gain appears on HellaSwag ($+$4.0 pts), where language modeling quality is most directly reflected.
docs/paper/experiments.tex:173:To verify that the profiled allocation is not overfit to the calibration corpus, we profile on C4 and evaluate on WikiText-2, and vice versa, on Qwen2.5-7B at $4\times$ compression.
docs/paper/experiments.tex:174:C4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\ 15.45 uniform, a 27\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).
docs/paper/experiments.tex:175:In the reverse direction, WikiText-2-calibrated MCKP achieves 20.56 PPL on C4 (vs.\ 35.42 uniform, a 42\% reduction; C4 bf16 baseline is 12.65).
docs/paper/experiments.tex:176:The two calibration corpora produce 96.4\% identical head assignments (108/112 heads), confirming that the profiled sensitivity ranking is stable across domains.
docs/paper/experiments.tex:178:These results are reported for Qwen2.5-7B only; cross-dataset validation on Llama and Mistral is left for future work.
docs/paper/conclusion.tex:4:A single constraint---limiting simultaneously active 2-bit heads to $k \leq 8$ (7\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\% improvement at $4\times$ compression.
docs/paper/conclusion.tex:5:Under the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\Delta = 0.0000$), so a simple $O(H \log H)$ greedy algorithm suffices.
docs/paper/conclusion.tex:6:The benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) is slightly counterproductive (7.16 vs.\ 7.13 PPL).
docs/paper/introduction.tex:12:On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
docs/paper/introduction.tex:23:On Qwen2.5-7B, setting $k{=}8$ (7\% of heads) yields 11.23 PPL---a 27.3\% reduction over uniform 4-bit.
docs/paper/introduction.tex:28:Constrained greedy and constrained MCKP produce identical allocations---not approximately, but exactly: all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3 (the single difference is a zero-distortion tie with no PPL impact).
docs/paper/introduction.tex:30:A per-layer brute-force oracle confirms near-optimality: the maximum gap across 28 layers is 0.02 PPL, 0.4\% of the total improvement (\S\ref{sec:solver_equiv}).
docs/paper/introduction.tex:33:On Llama-3.1-8B, constrained MCKP achieves 8.45 PPL vs.\ uniform 8.47---a marginal 0.2\% improvement.
docs/paper/introduction.tex:34:On Mistral-7B-v0.3, it is slightly \emph{worse}: 7.16 vs.\ 7.13.
docs/paper/introduction.tex:40:On our three architectures, the metric distinguishes the beneficial case (Qwen, concentration 0.59--0.66, 27.3\% PPL improvement) from the neutral case (Llama, 0.34--0.59, marginal) and the counterproductive case (Mistral, 0.42, slightly worse than uniform) across the three tested architectures.
docs/paper/introduction.tex:45:\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
docs/paper/abstract.tex:1:Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\{2, 4, 8, 16\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).
docs/paper/abstract.tex:4:On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
docs/paper/abstract.tex:5:The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
docs/paper/abstract.tex:6:However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\ 7.13).
docs/paper/method.tex:10:Given a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\times$ compression), we seek the allocation that minimizes total distortion:
docs/paper/method.tex:28:This holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.
docs/paper/method.tex:42:\caption{PPL on Qwen2.5-7B ($4\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}
docs/paper/method.tex:47:On Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).
docs/paper/method.tex:52:At 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).
docs/paper/method.tex:55:Figure~\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\times$ compression.
docs/paper/method.tex:56:The curve is U-shaped: at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond this point, compounding drives PPL upward, reaching 35.35 at $k{=}75$.
docs/paper/method.tex:68:For Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\sim$7\% of heads).
docs/paper/method.tex:73:On Qwen2.5-7B, the profiler assigns very high distortion to Layer-0 heads at 2-bit: L0H0 increases PPL by 31.9\% relative to the bf16 baseline (9.81 $\to$ 12.94), L0H2 by 23.2\% (9.81 $\to$ 12.09), L0H3 by 11.7\% (9.81 $\to$ 10.96).
docs/paper/method.tex:84:\caption{Solver comparison on Qwen2.5-7B at $4\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\leq}8$) makes greedy and MCKP produce identical allocations.\protect\footnotemark}
docs/paper/method.tex:91:Greedy & None & 32.45 & 68 & 30 & 14 \\
docs/paper/method.tex:92:MCKP & None & 36.92 & 75 & 33 & 4 \\
docs/paper/method.tex:93:Greedy & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
docs/paper/method.tex:94:MCKP & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
docs/paper/method.tex:95:Uniform & --- & 15.45 & 0 & 112 & 0 \\
docs/paper/method.tex:99:\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\times$ 2048 tok) achieves 10.91 (\S\ref{sec:profiling_resolution}).}
docs/paper/method.tex:102:Table~\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.
docs/paper/method.tex:106:\item \textbf{Qwen2.5-7B:} 112/112 heads receive identical bit-widths.
docs/paper/method.tex:107:\item \textbf{Llama-3.1-8B:} 256/256 heads identical.
docs/paper/method.tex:108:\item \textbf{Mistral-7B-v0.3:} 255/256 heads identical. The single difference is a zero-distortion tie between two heads at 4-bit and 8-bit, with no PPL impact.
docs/paper/method.tex:117:To verify that constrained MCKP is near-optimal, we perform a per-layer brute-force oracle on Qwen2.5-7B: for each of the 28 layers, we enumerate all $4^4{=}256$ bit-width assignments to the 4 KV heads and select the allocation minimizing per-layer PPL.
docs/paper/method.tex:118:Of the 8 layers with non-trivial (non-all-4-bit) allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.0183 PPL---0.4\% of the constrained-vs-uniform improvement (4.53 PPL)---due to within-layer 2-bit head position swaps with no change to the per-layer bit budget.
docs/paper/method.tex:119:Combined with the greedy--MCKP equivalence above, this closes the optimality chain: a simple $O(H \log H)$ greedy algorithm (runtime 0.005s) produces allocations within 0.02 PPL of the brute-force optimum.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "76d5a783-e648-4e0e-925e-6f56c79ee248",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:12:Qwen2.5-7B exhibits the highest heterogeneity (top-5\\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.\ndocs/paper/analysis.tex:13:Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\\% improvement over uniform 4-bit.\ndocs/paper/analysis.tex:14:Llama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\\ $+$0.38).\ndocs/paper/analysis.tex:15:Mistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.\ndocs/paper/analysis.tex:16:Here, constrained MCKP is slightly \\emph{worse} than uniform ($+$0.13 vs.\\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.\ndocs/paper/analysis.tex:28:Qwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\\\\ndocs/paper/analysis.tex:29:Llama-3.1-8B$^\\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\\\\ndocs/paper/analysis.tex:30:Mistral-7B-v0.3$^\\dagger$ & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\\\\ndocs/paper/analysis.tex:38:\\caption{Per-head 2-bit quantization sensitivity across three models. Qwen2.5-7B (left) shows high concentration in Layer-0 heads; Llama-3.1-8B (center) shows moderate spread; Mistral-7B-v0.3 (right) shows near-zero sensitivity across all heads. Color intensity indicates PPL increase when the head is quantized to 2-bit.}\ndocs/paper/analysis.tex:55:  \\item Concentration ${>}\\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\\% PPL improvement).\ndocs/paper/analysis.tex:56:  \\item Concentration $0.30$--$0.50$: marginal benefit; depends on target compression ratio (Llama case; 0.2\\% at $4\\times$).\ndocs/paper/analysis.tex:69:At more aggressive ratios, the picture changes: at $5.3\\times$ (average 3 bits), constrained MCKP achieves $45\\times$ lower PPL than uniform on Llama (57.60 vs.\\ 2643.77) and $44\\times$ on Mistral (11.91 vs.\\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.\ndocs/paper/analysis.tex:71:The intermediate regime ($5.3\\times$) provides the largest relative benefit.\ndocs/paper/analysis.tex:76:We compare standard-resolution profiling (16 sequences $\\times$ 512 tokens) against high-resolution profiling (64 sequences $\\times$ 2048 tokens) on Qwen2.5-7B at $4\\times$ compression.\ndocs/paper/analysis.tex:78:High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).\ndocs/paper/analysis.tex:79:Relative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\\% reduction.\ndocs/paper/analysis.tex:80:The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\\times$ more).\ndocs/paper/analysis.tex:87:Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \\pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\\%.\ndocs/paper/analysis.tex:88:The bit distribution is identical across all seeds ($\\{$2-bit: 8, 4-bit: 100, 8-bit: 4$\\}$), and 101 of 112 heads (90.2\\%) receive the same assignment in all three runs.\ndocs/paper/analysis.tex:92:To validate the additive distortion assumption underlying the MCKP formulation, we compare constrained MCKP against a per-layer brute-force oracle that exhaustively enumerates all $4^4 = 256$ bit-width combinations within each 4-head group on Qwen2.5-7B (hires profiling).\ndocs/paper/analysis.tex:93:Of the 8 layers admitting multiple feasible allocations, MCKP matches the oracle exactly in 5; the remaining 3 show gaps of 0.018 (Layer~1), 0.014 (Layer~11), and 0.005 (Layer~4) PPL.\ndocs/paper/analysis.tex:95:The negligible total gap ($<0.04$ PPL) confirms that the per-head additive distortion model closely approximates the true layer-level interaction.\ndocs/paper/analysis.tex:102:Joint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).\ndocs/paper/experiments.tex:9:\\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\\times$ 4 KV heads = 112 KV heads),\ndocs/paper/experiments.tex:10:\\textbf{Llama-3.1-8B} (4:1, 32 $\\times$ 8 = 256 KV heads),\ndocs/paper/experiments.tex:11:and \\textbf{Mistral-7B-v0.3} (4:1, 32 $\\times$ 8 = 256 KV heads, sliding window attention).\ndocs/paper/experiments.tex:24:The default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\ndocs/paper/experiments.tex:41:[Omitted long matching line]\ndocs/paper/experiments.tex:48:Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{11.23}$\\pm$0.06 \\\\\ndocs/paper/experiments.tex:49:Llama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \\textbf{8.45}$^\\dagger$ \\\\\ndocs/paper/experiments.tex:50:Mistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\\dagger\\ddagger}$ \\\\\ndocs/paper/experiments.tex:56:On Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\\% reduction over uniform 4-bit (15.45).\ndocs/paper/experiments.tex:57:Higher-resolution profiling (64 seq $\\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in \\S\\ref{sec:profiling_resolution}.\ndocs/paper/experiments.tex:58:Without the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.\ndocs/paper/experiments.tex:60:Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 (std is 1.3\\% of the uniform gap), with 90.2\\% three-way allocation agreement, confirming profiling stability.\ndocs/paper/experiments.tex:62:On Llama-3.1-8B, the improvement is marginal: 8.45 vs.\\ 8.47 (0.2\\%).\ndocs/paper/experiments.tex:65:On Mistral-7B-v0.3, constrained MCKP (7.16) is slightly worse than uniform (7.13, $+$0.4\\%).\ndocs/paper/experiments.tex:75:\\caption{Bit-width allocation on Qwen2.5-7B at 4$\\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}\ndocs/paper/experiments.tex:85:\\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\\geq$4$\\times$). Standard-resolution profiling; hires results in \\S\\ref{sec:profiling_resolution}.}\ndocs/paper/experiments.tex:91:2$\\times$ & 10.10 & 10.66 & $-$0.56 \\\\\ndocs/paper/experiments.tex:92:4$\\times$ & 15.45 & 11.23 & $+$4.21 \\\\\ndocs/paper/experiments.tex:98:Table~\\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.\ndocs/paper/experiments.tex:100:At 2$\\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\\ 9.81 bf16, $+$0.29).\ndocs/paper/experiments.tex:101:Per-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.\ndocs/paper/experiments.tex:103:At 4$\\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\\% improvement.\ndocs/paper/experiments.tex:104:Hires profiling further reduces this to 10.91 (\\S\\ref{sec:profiling_resolution}).\ndocs/paper/experiments.tex:123:Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\\pm$0.47 & 12.23 \\\\\ndocs/paper/experiments.tex:124:Llama-3.1-8B    & 8.45  & 8.62  & 8.62$\\pm$0.07  & 8.58 \\\\\ndocs/paper/experiments.tex:125:Mistral-7B-v0.3 & 7.16  & 7.24  & 7.24$\\pm$0.07  & 7.21 \\\\\ndocs/paper/experiments.tex:132:On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.\ndocs/paper/experiments.tex:134:On Llama ($k{=}2$), the gap between methods is small: MCKP achieves 8.45 vs.\\ L0-random 8.62 and naive positional 8.58.\ndocs/paper/experiments.tex:135:With only 2 heads assigned to 2-bit, the choice of which heads to compress has limited impact, and all methods cluster within 0.17 PPL.\ndocs/paper/experiments.tex:138:On Mistral ($k{=}4$), all non-uniform strategies are worse than uniform 4-bit (7.13): MCKP 7.16, naive 7.21, L0-random 7.24$\\pm$0.07.\ndocs/paper/experiments.tex:139:MCKP outperforms both heuristics, but the best non-uniform result (7.16) still exceeds uniform by 0.03 PPL, reinforcing that non-uniform allocation is counterproductive when heterogeneity is low.\ndocs/paper/experiments.tex:147:\\caption{0-shot accuracy on Qwen2.5-7B at 4$\\times$ compression. Constrained MCKP recovers approximately 73\\% of the accuracy lost by uniform 4-bit quantization.}\ndocs/paper/experiments.tex:154:ARC-C      & ---   & 0.482 & 0.514 & $+$3.2 pts \\\\\ndocs/paper/experiments.tex:155:HellaSwag  & ---   & 0.728 & 0.768 & $+$4.0 pts \\\\\ndocs/paper/experiments.tex:156:PIQA       & ---   & 0.766 & 0.779 & $+$1.3 pts \\\\\ndocs/paper/experiments.tex:157:WinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\\\\ndocs/paper/experiments.tex:159:Average    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\\\\ndocs/paper/experiments.tex:164:Table~\\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.\ndocs/paper/experiments.tex:165:Constrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\\ 0.660), with gains on all four benchmarks.\ndocs/paper/experiments.tex:166:The largest gain appears on HellaSwag ($+$4.0 pts), where language modeling quality is most directly reflected.\ndocs/paper/experiments.tex:173:To verify that the profiled allocation is not overfit to the calibration corpus, we profile on C4 and evaluate on WikiText-2, and vice versa, on Qwen2.5-7B at $4\\times$ compression.\ndocs/paper/experiments.tex:174:C4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\\ 15.45 uniform, a 27\\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).\ndocs/paper/experiments.tex:175:In the reverse direction, WikiText-2-calibrated MCKP achieves 20.56 PPL on C4 (vs.\\ 35.42 uniform, a 42\\% reduction; C4 bf16 baseline is 12.65).\ndocs/paper/experiments.tex:176:The two calibration corpora produce 96.4\\% identical head assignments (108/112 heads), confirming that the profiled sensitivity ranking is stable across domains.\ndocs/paper/experiments.tex:178:These results are reported for Qwen2.5-7B only; cross-dataset validation on Llama and Mistral is left for future work.\ndocs/paper/conclusion.tex:4:A single constraint---limiting simultaneously active 2-bit heads to $k \\leq 8$ (7\\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\\% improvement at $4\\times$ compression.\ndocs/paper/conclusion.tex:5:Under the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\\Delta = 0.0000$), so a simple $O(H \\log H)$ greedy algorithm suffices.\ndocs/paper/conclusion.tex:6:The benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) is slightly counterproductive (7.16 vs.\\ 7.13 PPL).\ndocs/paper/introduction.tex:12:On Qwen2.5-7B at $4\\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \\emph{far worse} than uniform 4-bit (15.45).\ndocs/paper/introduction.tex:23:On Qwen2.5-7B, setting $k{=}8$ (7\\% of heads) yields 11.23 PPL---a 27.3\\% reduction over uniform 4-bit.\ndocs/paper/introduction.tex:28:Constrained greedy and constrained MCKP produce identical allocations---not approximately, but exactly: all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3 (the single difference is a zero-distortion tie with no PPL impact).\ndocs/paper/introduction.tex:30:A per-layer brute-force oracle confirms near-optimality: the maximum gap across 28 layers is 0.02 PPL, 0.4\\% of the total improvement (\\S\\ref{sec:solver_equiv}).\ndocs/paper/introduction.tex:33:On Llama-3.1-8B, constrained MCKP achieves 8.45 PPL vs.\\ uniform 8.47---a marginal 0.2\\% improvement.\ndocs/paper/introduction.tex:34:On Mistral-7B-v0.3, it is slightly \\emph{worse}: 7.16 vs.\\ 7.13.\ndocs/paper/introduction.tex:40:On our three architectures, the metric distinguishes the beneficial case (Qwen, concentration 0.59--0.66, 27.3\\% PPL improvement) from the neutral case (Llama, 0.34--0.59, marginal) and the counterproductive case (Mistral, 0.42, slightly worse than uniform) across the three tested architectures.\ndocs/paper/introduction.tex:45:\\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\\times$ compression (\\S\\ref{sec:compounding}, \\S\\ref{sec:experiments}).\ndocs/paper/abstract.tex:1:Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\\{2, 4, 8, 16\\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).\ndocs/paper/abstract.tex:4:On Qwen2.5-7B at $4\\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\\% reduction over uniform 4-bit.\ndocs/paper/abstract.tex:5:The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\\Delta{=}0.0000$), enabling use of a simple $O(H \\log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).\ndocs/paper/abstract.tex:6:However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\\ 7.13).\ndocs/paper/method.tex:10:Given a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\\times$ compression), we seek the allocation that minimizes total distortion:\ndocs/paper/method.tex:28:This holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.\ndocs/paper/method.tex:42:\\caption{PPL on Qwen2.5-7B ($4\\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}\ndocs/paper/method.tex:47:On Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).\ndocs/paper/method.tex:52:At 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).\ndocs/paper/method.tex:55:Figure~\\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\\times$ compression.\ndocs/paper/method.tex:56:The curve is U-shaped: at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond this point, compounding drives PPL upward, reaching 35.35 at $k{=}75$.\ndocs/paper/method.tex:68:For Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\\sim$7\\% of heads).\ndocs/paper/method.tex:73:On Qwen2.5-7B, the profiler assigns very high distortion to Layer-0 heads at 2-bit: L0H0 increases PPL by 31.9\\% relative to the bf16 baseline (9.81 $\\to$ 12.94), L0H2 by 23.2\\% (9.81 $\\to$ 12.09), L0H3 by 11.7\\% (9.81 $\\to$ 10.96).\ndocs/paper/method.tex:84:\\caption{Solver comparison on Qwen2.5-7B at $4\\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\\leq}8$) makes greedy and MCKP produce identical allocations.\\protect\\footnotemark}\ndocs/paper/method.tex:91:Greedy & None & 32.45 & 68 & 30 & 14 \\\\\ndocs/paper/method.tex:92:MCKP & None & 36.92 & 75 & 33 & 4 \\\\\ndocs/paper/method.tex:93:Greedy & $k{\\leq}8$ & 11.23 & 8 & 100 & 4 \\\\\ndocs/paper/method.tex:94:MCKP & $k{\\leq}8$ & 11.23 & 8 & 100 & 4 \\\\\ndocs/paper/method.tex:95:Uniform & --- & 15.45 & 0 & 112 & 0 \\\\\ndocs/paper/method.tex:99:\\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\\times$ 2048 tok) achieves 10.91 (\\S\\ref{sec:profiling_resolution}).}\ndocs/paper/method.tex:102:Table~\\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.\ndocs/paper/method.tex:106:\\item \\textbf{Qwen2.5-7B:} 112/112 heads receive identical bit-widths.\ndocs/paper/method.tex:107:\\item \\textbf{Llama-3.1-8B:} 256/256 heads identical.\ndocs/paper/method.tex:108:\\item \\textbf{Mistral-7B-v0.3:} 255/256 heads identical. The single difference is a zero-distortion tie between two heads at 4-bit and 8-bit, with no PPL impact.\ndocs/paper/method.tex:117:To verify that constrained MCKP is near-optimal, we perform a per-layer brute-force oracle on Qwen2.5-7B: for each of the 28 layers, we enumerate all $4^4{=}256$ bit-width assignments to the 4 KV heads and select the allocation minimizing per-layer PPL.\ndocs/paper/method.tex:118:Of the 8 layers with non-trivial (non-all-4-bit) allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.0183 PPL---0.4\\% of the constrained-vs-uniform improvement (4.53 PPL)---due to within-layer 2-bit head position swaps with no change to the per-layer bit budget.\ndocs/paper/method.tex:119:Combined with the greedy--MCKP equivalence above, this closes the optimality chain: a simple $O(H \\log H)$ greedy algorithm (runtime 0.005s) produces allocations within 0.02 PPL of the brute-force optimum.",
    "numLines": 106
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01CYskBwCvYoQ5R54Lfox84G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "a7fabf45-5cb3-4bd0-b54b-19d8ff9ed664",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjhWxv6RbQMS2ndFHik41y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2726,
      "cache_read_input_tokens": 25491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2726
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

_source line 40 · 2026-05-14T12:15:03.134Z_

<details><summary>↩ Tool result · `toolu_01CYskBwCvYoQ5R54Lfox84G`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate on three architectures spanning different grouped-query attention (GQA) configurations:
9	\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\times$ 4 KV heads = 112 KV heads),
10	\textbf{Llama-3.1-8B} (4:1, 32 $\times$ 8 = 256 KV heads),
11	and \textbf{Mistral-7B-v0.3} (4:1, 32 $\times$ 8 = 256 KV heads, sliding window attention).
12	This selection covers the two dominant KV head counts (112 vs.\ 256) and both standard and sliding-window attention.
13	
14	\paragraph{Evaluation.}
15	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
16	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
17	
18	\paragraph{Profiling.}
19	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
20	We use two profiling resolutions: \emph{standard} (16 sequences $\times$ 512 tokens) and \emph{high-resolution} (64 sequences $\times$ 2048 tokens), both from WikiText-2 train.
21	Unless marked with $\dagger$, all results use standard-resolution profiling; \S\ref{sec:profiling_resolution} analyzes the effect of resolution.
22	
23	\paragraph{Compression and constraint.}
24	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
25	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).
26	
27	\paragraph{Baselines.}
28	We compare against:
29	(1)~uniform 4-bit quantization;
30	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
31	(3)~unconstrained MCKP allocation;
32	(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
33	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
34	
35	\subsection{Main Results}
36	\label{sec:main_results}
37	
38	\begin{table}[t]
39	\centering
40	\small
41	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained allocation fails catastrophically on $\{2,4,8,16\}$; our cardinality constraint restores performance. Best constrained result per model in \textbf{bold}. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok); standard profiling does not improve over uniform on these architectures. $^\ddagger$Best $k$ from ablation ($k{=}4$). The $\pm$0.06 on Qwen reports std over 3 calibration seeds (hires profiling); bit distributions are identical across seeds.}
42	\label{tab:main_results}
43	\begin{tabular}{lcccccc}
44	\toprule
45	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
46	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
47	\midrule
48	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{11.23}$\pm$0.06 \\
49	Llama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \textbf{8.45}$^\dagger$ \\
50	Mistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\dagger\ddagger}$ \\
51	\bottomrule
52	\end{tabular}
53	\end{table}
54	
55	Table~\ref{tab:main_results} summarizes the main results.
56	On Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\% reduction over uniform 4-bit (15.45).
57	Higher-resolution profiling (64 seq $\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in \S\ref{sec:profiling_resolution}.
58	Without the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.
59	The constraint eliminates this failure mode entirely.
60	Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 (std is 1.3\% of the uniform gap), with 90.2\% three-way allocation agreement, confirming profiling stability.
61	
62	On Llama-3.1-8B, the improvement is marginal: 8.45 vs.\ 8.47 (0.2\%).
63	The profiler finds low sensitivity heterogeneity across Llama's 256 KV heads, leaving little room for non-uniform allocation to improve over uniform.
64	
65	On Mistral-7B-v0.3, constrained MCKP (7.16) is slightly worse than uniform (7.13, $+$0.4\%).
66	This is a genuine negative result: the profiler reports near-zero sensitivity differences across heads, meaning the optimization has no reliable signal to exploit.
67	Mistral's sliding-window attention may contribute to this uniformity by limiting head-level variation in effective context length.
68	
69	Unconstrained results for Llama and Mistral are omitted (---) as those experiments were conducted only on Qwen, where the failure mode is most pronounced.
70	Figure~\ref{fig:allocation} visualizes the bit-width allocation on Qwen, showing how constrained MCKP protects Layer-0 heads at 8-bit while selectively assigning only the 8 least-sensitive heads to 2-bit.
71	
72	\begin{figure}[t]
73	\centering
74	\includegraphics[width=\columnwidth]{figures/fig3_allocation_comparison.pdf}
75	\caption{Bit-width allocation on Qwen2.5-7B at 4$\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}
76	\label{fig:allocation}
77	\end{figure}
78	
79	\subsection{Budget Sweep}
80	\label{sec:budget_sweep}
81	
82	\begin{table}[t]
83	\centering
84	\small
85	\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\geq$4$\times$). Standard-resolution profiling; hires results in \S\ref{sec:profiling_resolution}.}
86	\label{tab:budget_sweep}
87	\begin{tabular}{cccc}
88	\toprule
89	Compression & Uniform PPL & Constr.\ MCKP PPL & $\Delta$ PPL \\
90	\midrule
91	2$\times$ & 10.10 & 10.66 & $-$0.56 \\
92	4$\times$ & 15.45 & 11.23 & $+$4.21 \\
93	8$\times$ & 14{,}759 & 907 & $+$13{,}852 \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	Table~\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.
99	
100	At 2$\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\ 9.81 bf16, $+$0.29).
101	Per-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.
102	
103	At 4$\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\% improvement.
104	Hires profiling further reduces this to 10.91 (\S\ref{sec:profiling_resolution}).
105	
106	At 8$\times$, both methods degrade catastrophically---the budget is too aggressive for any allocation to preserve model quality.
107	However, constrained MCKP (907) is an order of magnitude better than uniform (14{,}759) because the constraint still protects Layer-0 heads at 8-bit, preventing total representational collapse.
108	Neither result is practically usable, but the gap demonstrates the protection mechanism at work.
109	
110	\subsection{Heuristic Baselines}
111	\label{sec:heuristic}
112	
113	\begin{table}[t]
114	\centering
115	\small
116	\caption{Constrained MCKP vs.\ heuristic baselines at 4$\times$ compression. L0-random reports median and mean$\pm$std over 5 seeds. All methods use per-model optimal $k$ ($k{=}8$ for Qwen, $k{=}2$ for Llama, $k{=}4$ for Mistral).}
117	\label{tab:heuristic}
118	\begin{tabular}{lcccc}
119	\toprule
120	Model & MCKP & \multicolumn{2}{c}{L0-random} & Naive \\
121	 & & Median & Mean$\pm$Std & Positional \\
122	\midrule
123	Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\pm$0.47 & 12.23 \\
124	Llama-3.1-8B    & 8.45  & 8.62  & 8.62$\pm$0.07  & 8.58 \\
125	Mistral-7B-v0.3 & 7.16  & 7.24  & 7.24$\pm$0.07  & 7.21 \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	Table~\ref{tab:heuristic} compares profiling-guided MCKP against heuristic baselines that use the same Layer-0 protection but assign 2-bit heads without profiling.
131	
132	On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.
133	
134	On Llama ($k{=}2$), the gap between methods is small: MCKP achieves 8.45 vs.\ L0-random 8.62 and naive positional 8.58.
135	With only 2 heads assigned to 2-bit, the choice of which heads to compress has limited impact, and all methods cluster within 0.17 PPL.
136	MCKP still achieves the best result, but the practical advantage of profiling-guided selection is marginal at this constraint level.
137	
138	On Mistral ($k{=}4$), all non-uniform strategies are worse than uniform 4-bit (7.13): MCKP 7.16, naive 7.21, L0-random 7.24$\pm$0.07.
139	MCKP outperforms both heuristics, but the best non-uniform result (7.16) still exceeds uniform by 0.03 PPL, reinforcing that non-uniform allocation is counterproductive when heterogeneity is low.
140	
141	\subsection{Downstream Evaluation}
142	\label{sec:downstream}
143	
144	\begin{table}[t]
145	\centering
146	\small
147	\caption{0-shot accuracy on Qwen2.5-7B at 4$\times$ compression. Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization.}
148	\label{tab:downstream}
149	\begin{tabular}{lcccc}
150	\toprule
151	Task & Baseline & Uniform & MCKP & $\Delta$ vs \\
152	 & (bf16) & (4-bit) & (Ours) & Uniform \\
153	\midrule
154	ARC-C      & ---   & 0.482 & 0.514 & $+$3.2 pts \\
155	HellaSwag  & ---   & 0.728 & 0.768 & $+$4.0 pts \\
156	PIQA       & ---   & 0.766 & 0.779 & $+$1.3 pts \\
157	WinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\
158	\midrule
159	Average    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\
160	\bottomrule
161	\end{tabular}
162	\end{table}
163	
164	Table~\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.
165	Constrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\ 0.660), with gains on all four benchmarks.
166	The largest gain appears on HellaSwag ($+$4.0 pts), where language modeling quality is most directly reflected.
167	
168	Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization, indicating that per-head bit allocation addresses much of the degradation, though a gap to bf16 remains.
169	
170	\subsection{Cross-Dataset Stability}
171	\label{sec:cross_dataset}
172	
173	To verify that the profiled allocation is not overfit to the calibration corpus, we profile on C4 and evaluate on WikiText-2, and vice versa, on Qwen2.5-7B at $4\times$ compression.
174	C4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\ 15.45 uniform, a 27\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).
175	In the reverse direction, WikiText-2-calibrated MCKP achieves 20.56 PPL on C4 (vs.\ 35.42 uniform, a 42\% reduction; C4 bf16 baseline is 12.65).
176	The two calibration corpora produce 96.4\% identical head assignments (108/112 heads), confirming that the profiled sensitivity ranking is stable across domains.
177	In both directions, constrained MCKP substantially outperforms uniform 4-bit quantization regardless of whether calibration and evaluation corpora are matched.
178	These results are reported for Qwen2.5-7B only; cross-dataset validation on Llama and Mistral is left for future work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "f87c2b8d-ed2b-4840-9b81-e31027036b50",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate on three architectures spanning different grouped-query attention (GQA) configurations:\n\\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\\times$ 4 KV heads = 112 KV heads),\n\\textbf{Llama-3.1-8B} (4:1, 32 $\\times$ 8 = 256 KV heads),\nand \\textbf{Mistral-7B-v0.3} (4:1, 32 $\\times$ 8 = 256 KV heads, sliding window attention).\nThis selection covers the two dominant KV head counts (112 vs.\\ 256) and both standard and sliding-window attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nWe use two profiling resolutions: \\emph{standard} (16 sequences $\\times$ 512 tokens) and \\emph{high-resolution} (64 sequences $\\times$ 2048 tokens), both from WikiText-2 train.\nUnless marked with $\\dagger$, all results use standard-resolution profiling; \\S\\ref{sec:profiling_resolution} analyzes the effect of resolution.\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained allocation fails catastrophically on $\\{2,4,8,16\\}$; our cardinality constraint restores performance. Best constrained result per model in \\textbf{bold}. $^\\dagger$Hires profiling (64 seq $\\times$ 2048 tok); standard profiling does not improve over uniform on these architectures. $^\\ddagger$Best $k$ from ablation ($k{=}4$). The $\\pm$0.06 on Qwen reports std over 3 calibration seeds (hires profiling); bit distributions are identical across seeds.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{11.23}$\\pm$0.06 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \\textbf{8.45}$^\\dagger$ \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\\dagger\\ddagger}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:main_results} summarizes the main results.\nOn Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\\% reduction over uniform 4-bit (15.45).\nHigher-resolution profiling (64 seq $\\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in \\S\\ref{sec:profiling_resolution}.\nWithout the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.\nThe constraint eliminates this failure mode entirely.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 (std is 1.3\\% of the uniform gap), with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the improvement is marginal: 8.45 vs.\\ 8.47 (0.2\\%).\nThe profiler finds low sensitivity heterogeneity across Llama's 256 KV heads, leaving little room for non-uniform allocation to improve over uniform.\n\nOn Mistral-7B-v0.3, constrained MCKP (7.16) is slightly worse than uniform (7.13, $+$0.4\\%).\nThis is a genuine negative result: the profiler reports near-zero sensitivity differences across heads, meaning the optimization has no reliable signal to exploit.\nMistral's sliding-window attention may contribute to this uniformity by limiting head-level variation in effective context length.\n\nUnconstrained results for Llama and Mistral are omitted (---) as those experiments were conducted only on Qwen, where the failure mode is most pronounced.\nFigure~\\ref{fig:allocation} visualizes the bit-width allocation on Qwen, showing how constrained MCKP protects Layer-0 heads at 8-bit while selectively assigning only the 8 least-sensitive heads to 2-bit.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_allocation_comparison.pdf}\n\\caption{Bit-width allocation on Qwen2.5-7B at 4$\\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}\n\\label{fig:allocation}\n\\end{figure}\n\n\\subsection{Budget Sweep}\n\\label{sec:budget_sweep}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\\geq$4$\\times$). Standard-resolution profiling; hires results in \\S\\ref{sec:profiling_resolution}.}\n\\label{tab:budget_sweep}\n\\begin{tabular}{cccc}\n\\toprule\nCompression & Uniform PPL & Constr.\\ MCKP PPL & $\\Delta$ PPL \\\\\n\\midrule\n2$\\times$ & 10.10 & 10.66 & $-$0.56 \\\\\n4$\\times$ & 15.45 & 11.23 & $+$4.21 \\\\\n8$\\times$ & 14{,}759 & 907 & $+$13{,}852 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.\n\nAt 2$\\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\\ 9.81 bf16, $+$0.29).\nPer-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.\n\nAt 4$\\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\\% improvement.\nHires profiling further reduces this to 10.91 (\\S\\ref{sec:profiling_resolution}).\n\nAt 8$\\times$, both methods degrade catastrophically---the budget is too aggressive for any allocation to preserve model quality.\nHowever, constrained MCKP (907) is an order of magnitude better than uniform (14{,}759) because the constraint still protects Layer-0 heads at 8-bit, preventing total representational collapse.\nNeither result is practically usable, but the gap demonstrates the protection mechanism at work.\n\n\\subsection{Heuristic Baselines}\n\\label{sec:heuristic}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Constrained MCKP vs.\\ heuristic baselines at 4$\\times$ compression. L0-random reports median and mean$\\pm$std over 5 seeds. All methods use per-model optimal $k$ ($k{=}8$ for Qwen, $k{=}2$ for Llama, $k{=}4$ for Mistral).}\n\\label{tab:heuristic}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & MCKP & \\multicolumn{2}{c}{L0-random} & Naive \\\\\n & & Median & Mean$\\pm$Std & Positional \\\\\n\\midrule\nQwen2.5-7B      & 11.23 & 11.52 & 11.69$\\pm$0.47 & 12.23 \\\\\nLlama-3.1-8B    & 8.45  & 8.62  & 8.62$\\pm$0.07  & 8.58 \\\\\nMistral-7B-v0.3 & 7.16  & 7.24  & 7.24$\\pm$0.07  & 7.21 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:heuristic} compares profiling-guided MCKP against heuristic baselines that use the same Layer-0 protection but assign 2-bit heads without profiling.\n\nOn Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.\n\nOn Llama ($k{=}2$), the gap between methods is small: MCKP achieves 8.45 vs.\\ L0-random 8.62 and naive positional 8.58.\nWith only 2 heads assigned to 2-bit, the choice of which heads to compress has limited impact, and all methods cluster within 0.17 PPL.\nMCKP still achieves the best result, but the practical advantage of profiling-guided selection is marginal at this constraint level.\n\nOn Mistral ($k{=}4$), all non-uniform strategies are worse than uniform 4-bit (7.13): MCKP 7.16, naive 7.21, L0-random 7.24$\\pm$0.07.\nMCKP outperforms both heuristics, but the best non-uniform result (7.16) still exceeds uniform by 0.03 PPL, reinforcing that non-uniform allocation is counterproductive when heterogeneity is low.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy on Qwen2.5-7B at 4$\\times$ compression. Constrained MCKP recovers approximately 73\\% of the accuracy lost by uniform 4-bit quantization.}\n\\label{tab:downstream}\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Baseline & Uniform & MCKP & $\\Delta$ vs \\\\\n & (bf16) & (4-bit) & (Ours) & Uniform \\\\\n\\midrule\nARC-C      & ---   & 0.482 & 0.514 & $+$3.2 pts \\\\\nHellaSwag  & ---   & 0.728 & 0.768 & $+$4.0 pts \\\\\nPIQA       & ---   & 0.766 & 0.779 & $+$1.3 pts \\\\\nWinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\\\\n\\midrule\nAverage    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.\nConstrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\\ 0.660), with gains on all four benchmarks.\nThe largest gain appears on HellaSwag ($+$4.0 pts), where language modeling quality is most directly reflected.\n\nConstrained MCKP recovers approximately 73\\% of the accuracy lost by uniform 4-bit quantization, indicating that per-head bit allocation addresses much of the degradation, though a gap to bf16 remains.\n\n\\subsection{Cross-Dataset Stability}\n\\label{sec:cross_dataset}\n\nTo verify that the profiled allocation is not overfit to the calibration corpus, we profile on C4 and evaluate on WikiText-2, and vice versa, on Qwen2.5-7B at $4\\times$ compression.\nC4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\\ 15.45 uniform, a 27\\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).\nIn the reverse direction, WikiText-2-calibrated MCKP achieves 20.56 PPL on C4 (vs.\\ 35.42 uniform, a 42\\% reduction; C4 bf16 baseline is 12.65).\nThe two calibration corpora produce 96.4\\% identical head assignments (108/112 heads), confirming that the profiled sensitivity ranking is stable across domains.\nIn both directions, constrained MCKP substantially outperforms uniform 4-bit quantization regardless of whether calibration and evaluation corpora are matched.\nThese results are reported for Qwen2.5-7B only; cross-dataset validation on Llama and Mistral is left for future work.",
      "numLines": 178,
      "startLine": 1,
      "totalLines": 178
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01NYNR6QPuLReU5Kz3SgBK1y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "96a82cfd-e6c3-47e4-a5ca-18bab7375566",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjhWxv6RbQMS2ndFHik41y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2726,
      "cache_read_input_tokens": 25491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2726
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

_source line 42 · 2026-05-14T12:15:03.580Z_

<details><summary>↩ Tool result · `toolu_01NYNR6QPuLReU5Kz3SgBK1y`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across three architectures at $4\times$ compression.
12	Qwen2.5-7B exhibits the highest heterogeneity (top-5\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.
13	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\% improvement over uniform 4-bit.
14	Llama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\ $+$0.38).
15	Mistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.
16	Here, constrained MCKP is slightly \emph{worse} than uniform ($+$0.13 vs.\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\times$ compression. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok).}
22	\label{tab:heterogeneity}
23	\begin{tabular}{lccccc}
24	\toprule
25	Model & GQA & Top-5\% & $\Delta$ PPL & $\Delta$ PPL & Recommendation \\
26	 & Ratio & Conc. & (Uniform) & (Ours) & \\
27	\midrule
28	Qwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\
29	Llama-3.1-8B$^\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\
30	Mistral-7B-v0.3$^\dagger$ & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\begin{figure*}[t]
36	\centering
37	\includegraphics[width=\textwidth]{figures/fig1_head_delta_heatmap.pdf}
38	\caption{Per-head 2-bit quantization sensitivity across three models. Qwen2.5-7B (left) shows high concentration in Layer-0 heads; Llama-3.1-8B (center) shows moderate spread; Mistral-7B-v0.3 (right) shows near-zero sensitivity across all heads. Color intensity indicates PPL increase when the head is quantized to 2-bit.}
39	\label{fig:heatmap}
40	\end{figure*}
41	
42	Figure~\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.
43	The contrast is stark: Qwen's Layer-0 heads show high distortion (dark cells) while mid-to-deep layers are near-zero; Mistral shows uniformly low distortion across all layers and heads.
44	
45	\subsection{Diagnostic Framework}
46	\label{sec:diagnostic}
47	
48	The heterogeneity characterization yields a preliminary guideline, based on three architectures, for deciding when non-uniform allocation is worthwhile:
49	
50	\begin{enumerate}[nosep]
51	\item Run per-head profiling as described in \S\ref{sec:profiling}.
52	\item Compute the top-5\% concentration from the resulting distortion table.
53	\item Select allocation strategy:
54	  \begin{itemize}[nosep]
55	  \item Concentration ${>}\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\% PPL improvement).
56	  \item Concentration $0.30$--$0.50$: marginal benefit; depends on target compression ratio (Llama case; 0.2\% at $4\times$).
57	  \item Near-zero absolute distortion for most heads: use uniform directly (Mistral case; non-uniform is counterproductive).
58	  \end{itemize}
59	\end{enumerate}
60	
61	The diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver.
62	This avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.
63	The thresholds above are derived from three architectures and should be validated on a broader set of models before being treated as general rules.
64	
65	\subsection{Aggressive Compression Amplifies Benefit}
66	\label{sec:aggressive}
67	
68	At $4\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.
69	At more aggressive ratios, the picture changes: at $5.3\times$ (average 3 bits), constrained MCKP achieves $45\times$ lower PPL than uniform on Llama (57.60 vs.\ 2643.77) and $44\times$ on Mistral (11.91 vs.\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.
70	At $8\times$, the budget is too constrained for any allocation to preserve quality (both methods degrade catastrophically).
71	The intermediate regime ($5.3\times$) provides the largest relative benefit.
72	
73	\subsection{Profiling Resolution}
74	\label{sec:profiling_resolution}
75	
76	We compare standard-resolution profiling (16 sequences $\times$ 512 tokens) against high-resolution profiling (64 sequences $\times$ 2048 tokens) on Qwen2.5-7B at $4\times$ compression.
77	
78	High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
79	Relative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\% reduction.
80	The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\times$ more).
81	
82	The additional signal changes 8 of 112 head assignments.
83	High-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.
84	
85	\paragraph{Multi-seed stability.}
86	The profiled allocation is stable across calibration subsets.
87	Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\%.
88	The bit distribution is identical across all seeds ($\{$2-bit: 8, 4-bit: 100, 8-bit: 4$\}$), and 101 of 112 heads (90.2\%) receive the same assignment in all three runs.
89	This stability confirms that the per-head sensitivity ranking is robust to calibration sampling noise.
90	
91	\paragraph{Per-layer optimality.}
92	To validate the additive distortion assumption underlying the MCKP formulation, we compare constrained MCKP against a per-layer brute-force oracle that exhaustively enumerates all $4^4 = 256$ bit-width combinations within each 4-head group on Qwen2.5-7B (hires profiling).
93	Of the 8 layers admitting multiple feasible allocations, MCKP matches the oracle exactly in 5; the remaining 3 show gaps of 0.018 (Layer~1), 0.014 (Layer~11), and 0.005 (Layer~4) PPL.
94	All three gaps involve repositioning a 2-bit assignment among heads with near-identical sensitivity within the same layer bit budget.
95	The negligible total gap ($<0.04$ PPL) confirms that the per-head additive distortion model closely approximates the true layer-level interaction.
96	
97	\subsection{KV Separation Ablation}
98	\label{sec:kv_separation}
99	
100	We test whether treating K and V caches as independent items in the MCKP solver---allowing different bit-widths for K and V within the same head---improves over joint allocation where K and V share a bit-width.
101	
102	Joint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).
103	The degradation stems from K-side over-compression: the separated solver doubles the maximum number of 2-bit K items to 16 (vs.\ 8 in the joint formulation), since K and V are counted independently against the cardinality constraint.
104	Meanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.
105	
106	Of the 112 heads, 21 show K$\neq$V asymmetry in the separated allocation, all with K receiving a lower bit-width than V.
107	This systematic asymmetry suggests that K caches are inherently more compressible than V caches, consistent with the observation that key vectors primarily encode positional information while value vectors carry content.
108	
109	Joint allocation is sufficient under the current constraint formulation.
110	Separated K/V allocation with per-side cardinality constraints---limiting 2-bit assignments independently for K and V---is a direction for future work.
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "4c210ee0-c21c-4af5-95c2-cbce57cedcae",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Heterogeneity Characterization}\n\\label{sec:heterogeneity}\n\nThe benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.\nWe quantify this with a \\emph{top-5\\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\\% of heads.\nHigh concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.\n\nTable~\\ref{tab:heterogeneity} summarizes the results across three architectures at $4\\times$ compression.\nQwen2.5-7B exhibits the highest heterogeneity (top-5\\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\\% improvement over uniform 4-bit.\nLlama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\\ $+$0.38).\nMistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.\nHere, constrained MCKP is slightly \\emph{worse} than uniform ($+$0.13 vs.\\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\\times$ compression. $^\\dagger$Hires profiling (64 seq $\\times$ 2048 tok).}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & GQA & Top-5\\% & $\\Delta$ PPL & $\\Delta$ PPL & Recommendation \\\\\n & Ratio & Conc. & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\\\\nLlama-3.1-8B$^\\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\\\\nMistral-7B-v0.3$^\\dagger$ & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_head_delta_heatmap.pdf}\n\\caption{Per-head 2-bit quantization sensitivity across three models. Qwen2.5-7B (left) shows high concentration in Layer-0 heads; Llama-3.1-8B (center) shows moderate spread; Mistral-7B-v0.3 (right) shows near-zero sensitivity across all heads. Color intensity indicates PPL increase when the head is quantized to 2-bit.}\n\\label{fig:heatmap}\n\\end{figure*}\n\nFigure~\\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.\nThe contrast is stark: Qwen's Layer-0 heads show high distortion (dark cells) while mid-to-deep layers are near-zero; Mistral shows uniformly low distortion across all layers and heads.\n\n\\subsection{Diagnostic Framework}\n\\label{sec:diagnostic}\n\nThe heterogeneity characterization yields a preliminary guideline, based on three architectures, for deciding when non-uniform allocation is worthwhile:\n\n\\begin{enumerate}[nosep]\n\\item Run per-head profiling as described in \\S\\ref{sec:profiling}.\n\\item Compute the top-5\\% concentration from the resulting distortion table.\n\\item Select allocation strategy:\n  \\begin{itemize}[nosep]\n  \\item Concentration ${>}\\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\\% PPL improvement).\n  \\item Concentration $0.30$--$0.50$: marginal benefit; depends on target compression ratio (Llama case; 0.2\\% at $4\\times$).\n  \\item Near-zero absolute distortion for most heads: use uniform directly (Mistral case; non-uniform is counterproductive).\n  \\end{itemize}\n\\end{enumerate}\n\nThe diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver.\nThis avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.\nThe thresholds above are derived from three architectures and should be validated on a broader set of models before being treated as general rules.\n\n\\subsection{Aggressive Compression Amplifies Benefit}\n\\label{sec:aggressive}\n\nAt $4\\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.\nAt more aggressive ratios, the picture changes: at $5.3\\times$ (average 3 bits), constrained MCKP achieves $45\\times$ lower PPL than uniform on Llama (57.60 vs.\\ 2643.77) and $44\\times$ on Mistral (11.91 vs.\\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.\nAt $8\\times$, the budget is too constrained for any allocation to preserve quality (both methods degrade catastrophically).\nThe intermediate regime ($5.3\\times$) provides the largest relative benefit.\n\n\\subsection{Profiling Resolution}\n\\label{sec:profiling_resolution}\n\nWe compare standard-resolution profiling (16 sequences $\\times$ 512 tokens) against high-resolution profiling (64 sequences $\\times$ 2048 tokens) on Qwen2.5-7B at $4\\times$ compression.\n\nHigh-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).\nRelative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\\% reduction.\nThe improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\\times$ more).\n\nThe additional signal changes 8 of 112 head assignments.\nHigh-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.\n\n\\paragraph{Multi-seed stability.}\nThe profiled allocation is stable across calibration subsets.\nUnder hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \\pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\\%.\nThe bit distribution is identical across all seeds ($\\{$2-bit: 8, 4-bit: 100, 8-bit: 4$\\}$), and 101 of 112 heads (90.2\\%) receive the same assignment in all three runs.\nThis stability confirms that the per-head sensitivity ranking is robust to calibration sampling noise.\n\n\\paragraph{Per-layer optimality.}\nTo validate the additive distortion assumption underlying the MCKP formulation, we compare constrained MCKP against a per-layer brute-force oracle that exhaustively enumerates all $4^4 = 256$ bit-width combinations within each 4-head group on Qwen2.5-7B (hires profiling).\nOf the 8 layers admitting multiple feasible allocations, MCKP matches the oracle exactly in 5; the remaining 3 show gaps of 0.018 (Layer~1), 0.014 (Layer~11), and 0.005 (Layer~4) PPL.\nAll three gaps involve repositioning a 2-bit assignment among heads with near-identical sensitivity within the same layer bit budget.\nThe negligible total gap ($<0.04$ PPL) confirms that the per-head additive distortion model closely approximates the true layer-level interaction.\n\n\\subsection{KV Separation Ablation}\n\\label{sec:kv_separation}\n\nWe test whether treating K and V caches as independent items in the MCKP solver---allowing different bit-widths for K and V within the same head---improves over joint allocation where K and V share a bit-width.\n\nJoint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).\nThe degradation stems from K-side over-compression: the separated solver doubles the maximum number of 2-bit K items to 16 (vs.\\ 8 in the joint formulation), since K and V are counted independently against the cardinality constraint.\nMeanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.\n\nOf the 112 heads, 21 show K$\\neq$V asymmetry in the separated allocation, all with K receiving a lower bit-width than V.\nThis systematic asymmetry suggests that K caches are inherently more compressible than V caches, consistent with the observation that key vectors primarily encode positional information while value vectors carry content.\n\nJoint allocation is sufficient under the current constraint formulation.\nSeparated K/V allocation with per-side cardinality constraints---limiting 2-bit assignments independently for K and V---is a direction for future work.\n",
      "numLines": 111,
      "startLine": 1,
      "totalLines": 111
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3zYv95RwqT8HWYyGjUNG8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "d7598a1f-c936-4ade-a568-69102a32781e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjhWxv6RbQMS2ndFHik41y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2726,
      "cache_read_input_tokens": 25491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2726
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

_source line 44 · 2026-05-14T12:15:04.078Z_

<details><summary>↩ Tool result · `toolu_01Q3zYv95RwqT8HWYyGjUNG8`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:formulation}
6	
7	We formulate per-head KV cache quantization as a constrained optimization problem.
8	Let $h \in \{1,\ldots,H\}$ index the KV heads across all layers, $b_h \in \mathcal{B}$ the bit-width assigned to head $h$, and $\mathcal{B} = \{2, 4, 8, 16\}$ the set of hardware-aligned bit-widths.
9	Each head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.
10	Given a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\times$ compression), we seek the allocation that minimizes total distortion:
11	\begin{equation}
12	\label{eq:objective}
13	\min_{\{b_h\}} \sum_{h=1}^{H} d_h(b_h) \quad \text{s.t.} \quad \frac{1}{H \cdot 16}\sum_{h=1}^{H} b_h \leq R.
14	\end{equation}
15	
16	This is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\mathcal{B}$ to minimize total distortion under a budget.
17	RateQuant~\cite{zuo2026ratequant} solves this for consecutive bit-widths $\{2,3,4,5,6\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).
18	Hardware-aligned bit-widths $\{2,4,8,16\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.
19	Moreover, as we show in \S\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.
20	
21	\subsection{PPL-based Per-Head Profiling}
22	\label{sec:profiling}
23	
24	We profile each KV head independently by quantizing it to each $b \in \mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\times$ 2048 tokens from WikiText-2 train.
25	This yields a distortion table of $H \times |\mathcal{B}|$ entries that serves as input to the solver.
26	
27	The optimization in Eq.~\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\sum_h d_h(b_h)$.
28	This holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.
29	At 2-bit, however, individual distortions are orders of magnitude larger, and the additive assumption breaks down.
30	
31	\subsection{Compounding Effect}
32	\label{sec:compounding}
33	
34	When many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively.
35	The mechanism is straightforward: each head's quantized output feeds into the residual stream, and truncation errors from multiple 2-bit heads accumulate through subsequent layers.
36	When the number of 2-bit heads is small, these errors are absorbed by the remaining high-precision heads.
37	As the count grows, cumulative errors exceed the capacity of the residual stream to compensate, and PPL degrades super-linearly.
38	
39	\begin{figure}[t]
40	\centering
41	\includegraphics[width=\columnwidth]{figures/fig2_compounding_curve.pdf}
42	\caption{PPL on Qwen2.5-7B ($4\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}
43	\label{fig:compounding}
44	\end{figure}
45	
46	Unconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.
47	On Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).
48	Standard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \approx 0$, so most 2-bit assignments appear free to the additive objective.
49	The resulting additive prediction is $\sum_h d_h(b_h) + \text{baseline} \approx 11$ PPL---$3\text{--}4\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.
50	
51	This compounding is specific to 2-bit quantization.
52	At 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).
53	The qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.
54	
55	Figure~\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\times$ compression.
56	The curve is U-shaped: at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond this point, compounding drives PPL upward, reaching 35.35 at $k{=}75$.
57	
58	\subsection{Cardinality Constraint}
59	\label{sec:cardinality}
60	
61	The compounding effect motivates a simple addition to Eq.~\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.
62	\begin{equation}
63	\label{eq:constraint}
64	\sum_{h=1}^{H} \mathbb{1}[b_h = 2] \leq k.
65	\end{equation}
66	
67	The constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\ref{fig:compounding}).
68	For Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\sim$7\% of heads).
69	
70	The constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.
71	
72	A natural question is whether Layer-0 heads require explicit protection, since attention heads in the first layer are known to carry disproportionate importance.
73	On Qwen2.5-7B, the profiler assigns very high distortion to Layer-0 heads at 2-bit: L0H0 increases PPL by 31.9\% relative to the bf16 baseline (9.81 $\to$ 12.94), L0H2 by 23.2\% (9.81 $\to$ 12.09), L0H3 by 11.7\% (9.81 $\to$ 10.96).
74	These values are large enough that no solver would assign 2-bit to Layer-0 under any reasonable budget.
75	We verify this empirically: running the solver with and without manual Layer-0 exclusion produces identical allocations across all 112 heads.
76	No manual exclusion rule is needed; the profiler signal is sufficient.
77	
78	\subsection{Solver Equivalence}
79	\label{sec:solver_equiv}
80	
81	\begin{table}[t]
82	\centering
83	\small
84	\caption{Solver comparison on Qwen2.5-7B at $4\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\leq}8$) makes greedy and MCKP produce identical allocations.\protect\footnotemark}
85	\label{tab:solver_equiv}
86	\begin{tabular}{llcccc}
87	\toprule
88	Solver & Constraint & PPL & \multicolumn{3}{c}{Bit distribution} \\
89	 & & & 2-bit & 4-bit & 8/16-bit \\
90	\midrule
91	Greedy & None & 32.45 & 68 & 30 & 14 \\
92	MCKP & None & 36.92 & 75 & 33 & 4 \\
93	Greedy & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
94	MCKP & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
95	Uniform & --- & 15.45 & 0 & 112 & 0 \\
96	\bottomrule
97	\end{tabular}
98	\end{table}
99	\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\times$ 2048 tok) achieves 10.91 (\S\ref{sec:profiling_resolution}).}
100	
101	With the cardinality constraint in place, greedy and MCKP produce identical results---not approximately, but exactly.
102	Table~\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.
103	We verify this at the per-head level across three models:
104	
105	\begin{itemize}[nosep]
106	\item \textbf{Qwen2.5-7B:} 112/112 heads receive identical bit-widths.
107	\item \textbf{Llama-3.1-8B:} 256/256 heads identical.
108	\item \textbf{Mistral-7B-v0.3:} 255/256 heads identical. The single difference is a zero-distortion tie between two heads at 4-bit and 8-bit, with no PPL impact.
109	\end{itemize}
110	
111	The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal.
112	Without it, greedy cascades into excessive 2-bit allocation: each additional 2-bit head looks locally beneficial (freeing budget) but contributes to the compounding effect that degrades global PPL.
113	The cardinality constraint breaks this cascade by capping the number of 2-bit heads, aligning local and global optima.
114	
115	The practical implication is that practitioners can use the simpler $O(H \log H)$ greedy algorithm instead of MCKP without sacrificing optimality.
116	
117	To verify that constrained MCKP is near-optimal, we perform a per-layer brute-force oracle on Qwen2.5-7B: for each of the 28 layers, we enumerate all $4^4{=}256$ bit-width assignments to the 4 KV heads and select the allocation minimizing per-layer PPL.
118	Of the 8 layers with non-trivial (non-all-4-bit) allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.0183 PPL---0.4\% of the constrained-vs-uniform improvement (4.53 PPL)---due to within-layer 2-bit head position swaps with no change to the per-layer bit budget.
119	Combined with the greedy--MCKP equivalence above, this closes the optimality chain: a simple $O(H \log H)$ greedy algorithm (runtime 0.005s) produces allocations within 0.02 PPL of the brute-force optimum.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "6430ad46-2b25-446e-b2aa-a710eeeb8344",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nWe formulate per-head KV cache quantization as a constrained optimization problem.\nLet $h \\in \\{1,\\ldots,H\\}$ index the KV heads across all layers, $b_h \\in \\mathcal{B}$ the bit-width assigned to head $h$, and $\\mathcal{B} = \\{2, 4, 8, 16\\}$ the set of hardware-aligned bit-widths.\nEach head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.\nGiven a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\\times$ compression), we seek the allocation that minimizes total distortion:\n\\begin{equation}\n\\label{eq:objective}\n\\min_{\\{b_h\\}} \\sum_{h=1}^{H} d_h(b_h) \\quad \\text{s.t.} \\quad \\frac{1}{H \\cdot 16}\\sum_{h=1}^{H} b_h \\leq R.\n\\end{equation}\n\nThis is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\\mathcal{B}$ to minimize total distortion under a budget.\nRateQuant~\\cite{zuo2026ratequant} solves this for consecutive bit-widths $\\{2,3,4,5,6\\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).\nHardware-aligned bit-widths $\\{2,4,8,16\\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.\nMoreover, as we show in \\S\\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.\n\n\\subsection{PPL-based Per-Head Profiling}\n\\label{sec:profiling}\n\nWe profile each KV head independently by quantizing it to each $b \\in \\mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\\times$ 2048 tokens from WikiText-2 train.\nThis yields a distortion table of $H \\times |\\mathcal{B}|$ entries that serves as input to the solver.\n\nThe optimization in Eq.~\\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\\sum_h d_h(b_h)$.\nThis holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.\nAt 2-bit, however, individual distortions are orders of magnitude larger, and the additive assumption breaks down.\n\n\\subsection{Compounding Effect}\n\\label{sec:compounding}\n\nWhen many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively.\nThe mechanism is straightforward: each head's quantized output feeds into the residual stream, and truncation errors from multiple 2-bit heads accumulate through subsequent layers.\nWhen the number of 2-bit heads is small, these errors are absorbed by the remaining high-precision heads.\nAs the count grows, cumulative errors exceed the capacity of the residual stream to compensate, and PPL degrades super-linearly.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_compounding_curve.pdf}\n\\caption{PPL on Qwen2.5-7B ($4\\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}\n\\label{fig:compounding}\n\\end{figure}\n\nUnconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.\nOn Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).\nStandard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \\approx 0$, so most 2-bit assignments appear free to the additive objective.\nThe resulting additive prediction is $\\sum_h d_h(b_h) + \\text{baseline} \\approx 11$ PPL---$3\\text{--}4\\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.\n\nThis compounding is specific to 2-bit quantization.\nAt 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).\nThe qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.\n\nFigure~\\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\\times$ compression.\nThe curve is U-shaped: at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond this point, compounding drives PPL upward, reaching 35.35 at $k{=}75$.\n\n\\subsection{Cardinality Constraint}\n\\label{sec:cardinality}\n\nThe compounding effect motivates a simple addition to Eq.~\\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.\n\\begin{equation}\n\\label{eq:constraint}\n\\sum_{h=1}^{H} \\mathbb{1}[b_h = 2] \\leq k.\n\\end{equation}\n\nThe constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\\ref{fig:compounding}).\nFor Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\\sim$7\\% of heads).\n\nThe constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.\n\nA natural question is whether Layer-0 heads require explicit protection, since attention heads in the first layer are known to carry disproportionate importance.\nOn Qwen2.5-7B, the profiler assigns very high distortion to Layer-0 heads at 2-bit: L0H0 increases PPL by 31.9\\% relative to the bf16 baseline (9.81 $\\to$ 12.94), L0H2 by 23.2\\% (9.81 $\\to$ 12.09), L0H3 by 11.7\\% (9.81 $\\to$ 10.96).\nThese values are large enough that no solver would assign 2-bit to Layer-0 under any reasonable budget.\nWe verify this empirically: running the solver with and without manual Layer-0 exclusion produces identical allocations across all 112 heads.\nNo manual exclusion rule is needed; the profiler signal is sufficient.\n\n\\subsection{Solver Equivalence}\n\\label{sec:solver_equiv}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Solver comparison on Qwen2.5-7B at $4\\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\\leq}8$) makes greedy and MCKP produce identical allocations.\\protect\\footnotemark}\n\\label{tab:solver_equiv}\n\\begin{tabular}{llcccc}\n\\toprule\nSolver & Constraint & PPL & \\multicolumn{3}{c}{Bit distribution} \\\\\n & & & 2-bit & 4-bit & 8/16-bit \\\\\n\\midrule\nGreedy & None & 32.45 & 68 & 30 & 14 \\\\\nMCKP & None & 36.92 & 75 & 33 & 4 \\\\\nGreedy & $k{\\leq}8$ & 11.23 & 8 & 100 & 4 \\\\\nMCKP & $k{\\leq}8$ & 11.23 & 8 & 100 & 4 \\\\\nUniform & --- & 15.45 & 0 & 112 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\\times$ 2048 tok) achieves 10.91 (\\S\\ref{sec:profiling_resolution}).}\n\nWith the cardinality constraint in place, greedy and MCKP produce identical results---not approximately, but exactly.\nTable~\\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.\nWe verify this at the per-head level across three models:\n\n\\begin{itemize}[nosep]\n\\item \\textbf{Qwen2.5-7B:} 112/112 heads receive identical bit-widths.\n\\item \\textbf{Llama-3.1-8B:} 256/256 heads identical.\n\\item \\textbf{Mistral-7B-v0.3:} 255/256 heads identical. The single difference is a zero-distortion tie between two heads at 4-bit and 8-bit, with no PPL impact.\n\\end{itemize}\n\nThe constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal.\nWithout it, greedy cascades into excessive 2-bit allocation: each additional 2-bit head looks locally beneficial (freeing budget) but contributes to the compounding effect that degrades global PPL.\nThe cardinality constraint breaks this cascade by capping the number of 2-bit heads, aligning local and global optima.\n\nThe practical implication is that practitioners can use the simpler $O(H \\log H)$ greedy algorithm instead of MCKP without sacrificing optimality.\n\nTo verify that constrained MCKP is near-optimal, we perform a per-layer brute-force oracle on Qwen2.5-7B: for each of the 28 layers, we enumerate all $4^4{=}256$ bit-width assignments to the 4 KV heads and select the allocation minimizing per-layer PPL.\nOf the 8 layers with non-trivial (non-all-4-bit) allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.0183 PPL---0.4\\% of the constrained-vs-uniform improvement (4.53 PPL)---due to within-layer 2-bit head position swaps with no change to the per-layer bit budget.\nCombined with the greedy--MCKP equivalence above, this closes the optimality chain: a simple $O(H \\log H)$ greedy algorithm (runtime 0.005s) produces allocations within 0.02 PPL of the brute-force optimum.",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Grep · `toolu_01RyuJcxAzeTihCcjPN8AvmU`</summary>

```json
{
  "pattern": "\\\\bibliographystyle",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "232e753d-15ec-4fb2-9134-4a06bfce0237",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjhWxv6RbQMS2ndFHik41y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2726,
      "cache_read_input_tokens": 25491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2726
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

_source line 46 · 2026-05-14T12:15:04.920Z_

<details><summary>↩ Tool result · `toolu_01RyuJcxAzeTihCcjPN8AvmU`</summary>

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
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "b67b96e3-19d7-4b06-ae5d-c267cefbda6e",
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

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Let me now also read the remaining files to complete the check.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "768f5694-40de-4575-84d7-e699dc29bac8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gs7iRTcrrHBbCuogPd31q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17903,
      "cache_read_input_tokens": 28217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17903
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

_source line 48_

Let me read the remaining files and check for a few more potential issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "2eafc655-f42a-4872-ab2d-8f282133f8d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gs7iRTcrrHBbCuogPd31q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17903,
      "cache_read_input_tokens": 28217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17903
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

<details open><summary>🔧 Tool call — Read · `toolu_01Gaz3m4Jvc6fXeK9uLa2iHm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "7230cae1-af4f-46b1-aeb7-3e1ced705ac9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gs7iRTcrrHBbCuogPd31q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17903,
      "cache_read_input_tokens": 28217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17903
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

_source line 50 · 2026-05-14T12:15:12.663Z_

<details><summary>↩ Tool result · `toolu_01Gaz3m4Jvc6fXeK9uLa2iHm`</summary>

```text
1	Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\{2, 4, 8, 16\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).
2	We trace this failure to \emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.
3	We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
4	On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
5	The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
6	However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\ 7.13).
7	We propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that can indicate, before any allocation, whether a given architecture will benefit from non-uniform quantization.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "d8a73328-187c-404c-bf3a-c68b42667dbb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex",
      "content": "Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\\{2, 4, 8, 16\\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).\nWe trace this failure to \\emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.\nWe show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.\nOn Qwen2.5-7B at $4\\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\\% reduction over uniform 4-bit.\nThe constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\\Delta{=}0.0000$), enabling use of a simple $O(H \\log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).\nHowever, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\\ 7.13).\nWe propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that can indicate, before any allocation, whether a given architecture will benefit from non-uniform quantization.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01FTafToygqQuwu2PatGn9uv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "59430396-6983-4121-8ad7-a835a10a01a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gs7iRTcrrHBbCuogPd31q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17903,
      "cache_read_input_tokens": 28217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17903
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

_source line 52 · 2026-05-14T12:15:12.880Z_

<details><summary>↩ Tool result · `toolu_01FTafToygqQuwu2PatGn9uv`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Per-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.
5	Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
6	RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
7	
8	In practice, hardware-efficient inference requires bit-widths drawn from $\{2, 4, 8, 16\}$---the formats natively supported by modern accelerators.
9	On this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.
10	One might expect that exact MCKP solvers would fill this gap.
11	They do not.
12	On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
13	The optimization does not merely underperform; it fails catastrophically.
14	
15	The root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.
17	The additive model predicts $\sim$11 PPL for these allocations; the actual PPL is $3$--$4\times$ higher.
18	At 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves close to its additive prediction---but 2-bit distortions are orders of magnitude larger.
19	When most heads are quantized to 2-bit simultaneously, cumulative truncation errors exceed the network's capacity to compensate, and perplexity degrades super-linearly.
20	
21	This observation points to a minimal intervention: cap the number of 2-bit assignments.
22	We add a single cardinality constraint $\sum_h \mathbb{1}[b_h{=}2] \leq k$ to the standard MCKP formulation (\S\ref{sec:method}).
23	On Qwen2.5-7B, setting $k{=}8$ (7\% of heads) yields 11.23 PPL---a 27.3\% reduction over uniform 4-bit.
24	The constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.
25	This is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.
26	
27	A surprising consequence is that, under the cardinality constraint, the choice of solver becomes irrelevant.
28	Constrained greedy and constrained MCKP produce identical allocations---not approximately, but exactly: all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3 (the single difference is a zero-distortion tie with no PPL impact).
29	The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal (\S\ref{sec:solver_equiv}), enabling practitioners to use the simpler $O(H \log H)$ greedy algorithm without sacrificing solution quality.
30	A per-layer brute-force oracle confirms near-optimality: the maximum gap across 28 layers is 0.02 PPL, 0.4\% of the total improvement (\S\ref{sec:solver_equiv}).
31	
32	However, non-uniform allocation does not help universally.
33	On Llama-3.1-8B, constrained MCKP achieves 8.45 PPL vs.\ uniform 8.47---a marginal 0.2\% improvement.
34	On Mistral-7B-v0.3, it is slightly \emph{worse}: 7.16 vs.\ 7.13.
35	The difference across architectures traces to head sensitivity heterogeneity: Qwen's KV heads vary widely in 2-bit distortion, with Layer-0 heads contributing a disproportionate share, while Mistral's heads are nearly uniform in sensitivity.
36	When there is no heterogeneity to exploit, non-uniform allocation adds noise without benefit.
37	
38	This motivates a diagnostic question that prior work does not address: \emph{when} should a practitioner use per-head mixed-precision quantization?
39	We propose a heterogeneity diagnostic based on the top-5\% concentration of per-head distortion (\S\ref{sec:heterogeneity}).
40	On our three architectures, the metric distinguishes the beneficial case (Qwen, concentration 0.59--0.66, 27.3\% PPL improvement) from the neutral case (Llama, 0.34--0.59, marginal) and the counterproductive case (Mistral, 0.42, slightly worse than uniform) across the three tested architectures.
41	The diagnostic reuses profiling data already required by the solver and adds no computational overhead.
42	
43	Our contributions are:
44	\begin{enumerate}[nosep]
45	\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
46	
47	\item We demonstrate that the cardinality constraint makes solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent per-head allocations across three architectures, enabling use of a simple greedy algorithm (\S\ref{sec:solver_equiv}).
48	
49	\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes (\S\ref{sec:heterogeneity}).
50	\end{enumerate}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "962cc0e7-80d3-4380-a6e6-c71b82446c7a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nPer-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.\nRecent work on KV cache quantization explores both uniform schemes~\\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\\cite{zhang2023h2o,li2024snapkv}.\nRateQuant~\\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\\{2,3,4,5,6\\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).\n\nIn practice, hardware-efficient inference requires bit-widths drawn from $\\{2, 4, 8, 16\\}$---the formats natively supported by modern accelerators.\nOn this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.\nOne might expect that exact MCKP solvers would fill this gap.\nThey do not.\nOn Qwen2.5-7B at $4\\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \\emph{far worse} than uniform 4-bit (15.45).\nThe optimization does not merely underperform; it fails catastrophically.\n\nThe root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.\nBoth solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.\nThe additive model predicts $\\sim$11 PPL for these allocations; the actual PPL is $3$--$4\\times$ higher.\nAt 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves close to its additive prediction---but 2-bit distortions are orders of magnitude larger.\nWhen most heads are quantized to 2-bit simultaneously, cumulative truncation errors exceed the network's capacity to compensate, and perplexity degrades super-linearly.\n\nThis observation points to a minimal intervention: cap the number of 2-bit assignments.\nWe add a single cardinality constraint $\\sum_h \\mathbb{1}[b_h{=}2] \\leq k$ to the standard MCKP formulation (\\S\\ref{sec:method}).\nOn Qwen2.5-7B, setting $k{=}8$ (7\\% of heads) yields 11.23 PPL---a 27.3\\% reduction over uniform 4-bit.\nThe constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.\nThis is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.\n\nA surprising consequence is that, under the cardinality constraint, the choice of solver becomes irrelevant.\nConstrained greedy and constrained MCKP produce identical allocations---not approximately, but exactly: all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3 (the single difference is a zero-distortion tie with no PPL impact).\nThe constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal (\\S\\ref{sec:solver_equiv}), enabling practitioners to use the simpler $O(H \\log H)$ greedy algorithm without sacrificing solution quality.\nA per-layer brute-force oracle confirms near-optimality: the maximum gap across 28 layers is 0.02 PPL, 0.4\\% of the total improvement (\\S\\ref{sec:solver_equiv}).\n\nHowever, non-uniform allocation does not help universally.\nOn Llama-3.1-8B, constrained MCKP achieves 8.45 PPL vs.\\ uniform 8.47---a marginal 0.2\\% improvement.\nOn Mistral-7B-v0.3, it is slightly \\emph{worse}: 7.16 vs.\\ 7.13.\nThe difference across architectures traces to head sensitivity heterogeneity: Qwen's KV heads vary widely in 2-bit distortion, with Layer-0 heads contributing a disproportionate share, while Mistral's heads are nearly uniform in sensitivity.\nWhen there is no heterogeneity to exploit, non-uniform allocation adds noise without benefit.\n\nThis motivates a diagnostic question that prior work does not address: \\emph{when} should a practitioner use per-head mixed-precision quantization?\nWe propose a heterogeneity diagnostic based on the top-5\\% concentration of per-head distortion (\\S\\ref{sec:heterogeneity}).\nOn our three architectures, the metric distinguishes the beneficial case (Qwen, concentration 0.59--0.66, 27.3\\% PPL improvement) from the neutral case (Llama, 0.34--0.59, marginal) and the counterproductive case (Mistral, 0.42, slightly worse than uniform) across the three tested architectures.\nThe diagnostic reuses profiling data already required by the solver and adds no computational overhead.\n\nOur contributions are:\n\\begin{enumerate}[nosep]\n\\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\\times$ compression (\\S\\ref{sec:compounding}, \\S\\ref{sec:experiments}).\n\n\\item We demonstrate that the cardinality constraint makes solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent per-head allocations across three architectures, enabling use of a simple greedy algorithm (\\S\\ref{sec:solver_equiv}).\n\n\\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes (\\S\\ref{sec:heterogeneity}).\n\\end{enumerate}\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_019buN7XoEjB6tnmgizkAwy7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "c82bed33-3a56-45e2-9612-3a5ce53b23e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gs7iRTcrrHBbCuogPd31q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17903,
      "cache_read_input_tokens": 28217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17903
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

_source line 54 · 2026-05-14T12:15:17.481Z_

<details><summary>↩ Tool result · `toolu_019buN7XoEjB6tnmgizkAwy7`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{KV Cache Quantization.}
4	Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\cite{lin2024qserve}, salient-token identification~\cite{he2024zipcache}, low-rank plus sparse correction~\cite{kang2024gear}, and sliding-window adaptation~\cite{duanmu2024skvq}.
5	We extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\{2,4,8,16\}$.
6	
7	\paragraph{KV Cache Eviction.}
8	Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
9	Our work focuses exclusively on the quantization allocation problem.
10	
11	\paragraph{Mixed-Precision Rate-Distortion Allocation.}
12	RateQuant~\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\{2,\ldots,6\}$ via the polymatroid structure.
13	On hardware-aligned $\{2,4,8,16\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.
14	Related mixed-precision work operates at coarser granularity (layer-level~\cite{li2025kvmix}, memory-budget-level~\cite{lei2026arkv}), at the weight level~\cite{kim2024squeezellm}, or dynamically at inference time~\cite{zhang2025mixkvq}; our allocation is static and per-head.
15	
16	\paragraph{Attention Head Analysis.}
17	Prior work studies head redundancy and pruning~\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.
18	Our analysis asks a different question: which heads are sensitive to \emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\S\ref{sec:heterogeneity}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "d159e2a5-b040-4365-8a4c-c62e7006aa52",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{KV Cache Quantization.}\nUniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\\cite{lin2024qserve}, salient-token identification~\\cite{he2024zipcache}, low-rank plus sparse correction~\\cite{kang2024gear}, and sliding-window adaptation~\\cite{duanmu2024skvq}.\nWe extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\\{2,4,8,16\\}$.\n\n\\paragraph{KV Cache Eviction.}\nComplementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\\cite{zhang2023h2o}, per-head important tokens~\\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\\cite{liu2024scissorhands}, attention sinks~\\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\\cite{yang2024pyramidinfer}.\nOur work focuses exclusively on the quantization allocation problem.\n\n\\paragraph{Mixed-Precision Rate-Distortion Allocation.}\nRateQuant~\\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\\{2,\\ldots,6\\}$ via the polymatroid structure.\nOn hardware-aligned $\\{2,4,8,16\\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.\nRelated mixed-precision work operates at coarser granularity (layer-level~\\cite{li2025kvmix}, memory-budget-level~\\cite{lei2026arkv}), at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.\n\n\\paragraph{Attention Head Analysis.}\nPrior work studies head redundancy and pruning~\\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.\nOur analysis asks a different question: which heads are sensitive to \\emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_013xKM98j3x8ZfEpga2bZTHz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "fc3043a1-6409-4e8e-8fdf-4e5f11fb49ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gs7iRTcrrHBbCuogPd31q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17903,
      "cache_read_input_tokens": 28217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17903
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

_source line 56 · 2026-05-14T12:15:17.723Z_

<details><summary>↩ Tool result · `toolu_013xKM98j3x8ZfEpga2bZTHz`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.
4	A single constraint---limiting simultaneously active 2-bit heads to $k \leq 8$ (7\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\% improvement at $4\times$ compression.
5	Under the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\Delta = 0.0000$), so a simple $O(H \log H)$ greedy algorithm suffices.
6	The benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) is slightly counterproductive (7.16 vs.\ 7.13 PPL).
7	This diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \emph{before deployment} whether non-uniform quantization is worthwhile for a given model.
8	
9	\paragraph{Limitations.}
10	Our study has several limitations that temper the generality of the findings.
11	First, we evaluate only three 7B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.
12	Second, profiling relies on a single sensitivity metric (perplexity-based per-head distortion); alternative measures such as gradient-based or activation-norm diagnostics remain unexplored and could yield different allocation decisions.
13	Third, we report perplexity and downstream accuracy but no real-kernel latency benchmarks, leaving the practical inference speedup from mixed-precision allocation unquantified.
14	Fourth, we have not verified whether these findings transfer to larger scales (70B+), where head counts and attention patterns differ substantially.
15	Finally, although we validate on four downstream tasks, profiling and primary evaluation use a single dataset (WikiText-2).
16	
17	\paragraph{Future Work.}
18	Extending evaluation to 70B+ models would test whether the heterogeneity--benefit relationship holds at scale.
19	Integration with production inference engines (vLLM, TensorRT-LLM) would enable real-kernel latency measurement, and investigating per-side K/V cardinality constraints (\S\ref{sec:kv_separation}) or dynamic per-request allocation could further improve the framework.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "14901da3-ef3e-493d-a758-2105f229068e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \\{2, 4, 8, 16\\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.\nA single constraint---limiting simultaneously active 2-bit heads to $k \\leq 8$ (7\\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\\% improvement at $4\\times$ compression.\nUnder the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\\Delta = 0.0000$), so a simple $O(H \\log H)$ greedy algorithm suffices.\nThe benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) is slightly counterproductive (7.16 vs.\\ 7.13 PPL).\nThis diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \\emph{before deployment} whether non-uniform quantization is worthwhile for a given model.\n\n\\paragraph{Limitations.}\nOur study has several limitations that temper the generality of the findings.\nFirst, we evaluate only three 7B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.\nSecond, profiling relies on a single sensitivity metric (perplexity-based per-head distortion); alternative measures such as gradient-based or activation-norm diagnostics remain unexplored and could yield different allocation decisions.\nThird, we report perplexity and downstream accuracy but no real-kernel latency benchmarks, leaving the practical inference speedup from mixed-precision allocation unquantified.\nFourth, we have not verified whether these findings transfer to larger scales (70B+), where head counts and attention patterns differ substantially.\nFinally, although we validate on four downstream tasks, profiling and primary evaluation use a single dataset (WikiText-2).\n\n\\paragraph{Future Work.}\nExtending evaluation to 70B+ models would test whether the heterogeneity--benefit relationship holds at scale.\nIntegration with production inference engines (vLLM, TensorRT-LLM) would enable real-kernel latency measurement, and investigating per-side K/V cardinality constraints (\\S\\ref{sec:kv_separation}) or dynamic per-request allocation could further improve the framework.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01SfKYg9mWaBZakhG5dJHS9E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "900ae23e-433d-4808-b073-8dbd9bcabdf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gs7iRTcrrHBbCuogPd31q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17903,
      "cache_read_input_tokens": 28217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17903
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

_source line 58 · 2026-05-14T12:15:17.898Z_

<details><summary>↩ Tool result · `toolu_01SfKYg9mWaBZakhG5dJHS9E`</summary>

```text
1	% Auto-generated from literature_map.yaml (verified=true entries)
2	
3	@inproceedings{liu2024kivi,
4	  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},
5	  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},
6	  year = {2024},
7	  booktitle = {ICML 2024},
8	  url = {https://arxiv.org/abs/2402.02750},
9	}
10	
11	@inproceedings{hooper2024kvquant,
12	  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},
13	  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},
14	  year = {2024},
15	  booktitle = {NeurIPS 2024},
16	  url = {https://arxiv.org/abs/2401.18079},
17	}
18	
19	@inproceedings{lin2024qserve,
20	  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},
21	  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},
22	  year = {2025},
23	  booktitle = {MLSys 2025},
24	  url = {https://arxiv.org/abs/2405.04532},
25	}
26	
27	@inproceedings{he2024zipcache,
28	  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},
29	  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},
30	  year = {2024},
31	  booktitle = {NeurIPS 2024},
32	  url = {https://arxiv.org/abs/2405.14256},
33	}
34	
35	@misc{kang2024gear,
36	  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},
37	  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},
38	  year = {2024},
39	  note = {arXiv preprint},
40	  url = {https://arxiv.org/abs/2403.05527},
41	  eprint = {2403.05527},
42	  archivePrefix = {arXiv},
43	}
44	
45	@misc{duanmu2024skvq,
46	  title = {{SKVQ}: Sliding-window Key and Value Cache Quantization for Large Language Models},
47	  author = {Haojie Duanmu and Zhihang Yuan and Xiuhong Li and Jiangfei Duan and Xingcheng Zhang and Dahua Lin},
48	  year = {2024},
49	  note = {arXiv preprint},
50	  url = {https://arxiv.org/abs/2405.06219},
51	  eprint = {2405.06219},
52	  archivePrefix = {arXiv},
53	}
54	
55	@inproceedings{zhang2023h2o,
56	  title = {{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
57	  author = {Zhenyu Zhang and Ying Sheng and Tianyi Zhou and Tianlong Chen and Lianmin Zheng and Ruisi Cai and Zhao Song and Yuandong Tian and Christopher R{\'{e}} and Clark Barrett and Zhangyang Wang and Beidi Chen},
58	  year = {2023},
59	  booktitle = {NeurIPS 2023},
60	  url = {https://arxiv.org/abs/2306.14048},
61	}
62	
63	@inproceedings{li2024snapkv,
64	  title = {{SnapKV}: {LLM} Knows What You are Looking for Before Generation},
65	  author = {Yuhong Li and Yingbing Huang and Bowen Yang and Bharat Venkitesh and Acyr Locatelli and Hanchen Ye and Tianle Cai and Patrick Lewis and Deming Chen},
66	  year = {2024},
67	  booktitle = {NeurIPS 2024},
68	  url = {https://arxiv.org/abs/2404.14469},
69	}
70	
71	@inproceedings{ge2024fastgen,
72	  title = {Model Tells You What to Discard: Adaptive {KV} Cache Compression for {LLMs}},
73	  author = {Suyu Ge and Yunan Zhang and Liyuan Liu and Minjia Zhang and Jiawei Han and Jianfeng Gao},
74	  year = {2024},
75	  booktitle = {ICLR 2024},
76	  url = {https://arxiv.org/abs/2310.01801},
77	}
78	
79	@inproceedings{xiao2024streamingllm,
80	  title = {Efficient Streaming Language Models with Attention Sinks},
81	  author = {Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis},
82	  year = {2024},
83	  booktitle = {ICLR 2024},
84	  url = {https://arxiv.org/abs/2309.17453},
85	}
86	
87	@inproceedings{liu2024scissorhands,
88	  title = {Scissorhands: Exploiting the Persistence of Importance Hypothesis for {LLM} {KV} Cache Compression at Test Time},
89	  author = {Zichang Liu and Aditya Desai and Fangshuo Liao and Weitao Wang and Victor Xie and Zhaozhuo Xu and Anastasios Kyrillidis and Anshumali Shrivastava},
90	  year = {2023},
91	  booktitle = {NeurIPS 2023},
92	  url = {https://arxiv.org/abs/2305.17118},
93	}
94	
95	@inproceedings{yang2024pyramidinfer,
96	  title = {{PyramidInfer}: Pyramid {KV} Cache Compression for High-throughput {LLM} Inference},
97	  author = {Dongjie Yang and Xiaodong Han and Yan Gao and Yao Hu and Shilin Zhang and Hai Zhao},
98	  year = {2024},
99	  booktitle = {Findings of ACL 2024},
100	  url = {https://arxiv.org/abs/2405.12532},
101	}
102	
103	@misc{zuo2026ratequant,
104	  title = {{RateQuant}: Optimal Mixed-Precision {KV} Cache Quantization via Rate-Distortion Theory},
105	  author = {Fei Zuo and Zikang Zhou and Hao Cong and Xiaoyan Xi and Ho Fai Leung},
106	  year = {2026},
107	  note = {arXiv preprint},
108	  url = {https://arxiv.org/abs/2605.06675},
109	  eprint = {2605.06675},
110	  archivePrefix = {arXiv},
111	}
112	
113	@misc{lei2026arkv,
114	  title = {{ARKV}: Adaptive and Resource-Efficient {KV} Cache Management under Limited Memory Budget for Long-Context Inference in {LLMs}},
115	  author = {Jianlong Lei and Shashikant Ilager},
116	  year = {2026},
117	  note = {arXiv preprint},
118	  url = {https://arxiv.org/abs/2603.08727},
119	  eprint = {2603.08727},
120	  archivePrefix = {arXiv},
121	}
122	
123	@misc{li2025kvmix,
124	  title = {{KVmix}: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for {KV} Cache},
125	  author = {Fei Li and Song Liu and Weiguo Wu and Shiqiang Nie and Jinyu Wang},
126	  year = {2025},
127	  note = {arXiv preprint},
128	  url = {https://arxiv.org/abs/2506.08018},
129	  eprint = {2506.08018},
130	  archivePrefix = {arXiv},
131	}
132	
133	@misc{zhang2025mixkvq,
134	  title = {{MixKVQ}: Query-Aware Mixed-Precision {KV} Cache Quantization for Long-Context Reasoning},
135	  author = {Tao Zhang and Ziqian Zeng and Hao Peng and Huiping Zhuang and Cen Chen},
136	  year = {2025},
137	  note = {arXiv preprint},
138	  url = {https://arxiv.org/abs/2512.19206},
139	  eprint = {2512.19206},
140	  archivePrefix = {arXiv},
141	}
142	
143	@inproceedings{kim2024squeezellm,
144	  title = {{SqueezeLLM}: Dense-and-Sparse Quantization},
145	  author = {Sehoon Kim and Coleman Hooper and Amir Gholami and Zhen Dong and Xiuyu Li and Sheng Shen and Michael W. Mahoney and Kurt Keutzer},
146	  year = {2024},
147	  booktitle = {ICML 2024},
148	  url = {https://arxiv.org/abs/2306.07629},
149	}
150	
151	@inproceedings{voita2019analyzing,
152	  title = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},
153	  author = {Elena Voita and David Talbot and Fedor Moiseev and Rico Sennrich and Ivan Titov},
154	  year = {2019},
155	  booktitle = {ACL 2019},
156	  url = {https://arxiv.org/abs/1905.09418},
157	}
158	
159	@inproceedings{michel2019sixteen,
160	  title = {Are Sixteen Heads Really Better than One?},
161	  author = {Paul Michel and Omer Levy and Graham Neubig},
162	  year = {2019},
163	  booktitle = {NeurIPS 2019},
164	  url = {https://arxiv.org/abs/1905.10650},
165	}
166	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "01528d01-0a0f-4f1c-aeb4-35c1d442bf6a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml (verified=true entries)\n\n@inproceedings{liu2024kivi,\n  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},\n  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},\n  year = {2024},\n  booktitle = {ICML 2024},\n  url = {https://arxiv.org/abs/2402.02750},\n}\n\n@inproceedings{hooper2024kvquant,\n  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},\n  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},\n  year = {2024},\n  booktitle = {NeurIPS 2024},\n  url = {https://arxiv.org/abs/2401.18079},\n}\n\n@inproceedings{lin2024qserve,\n  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},\n  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},\n  year = {2025},\n  booktitle = {MLSys 2025},\n  url = {https://arxiv.org/abs/2405.04532},\n}\n\n@inproceedings{he2024zipcache,\n  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},\n  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},\n  year = {2024},\n  booktitle = {NeurIPS 2024},\n  url = {https://arxiv.org/abs/2405.14256},\n}\n\n@misc{kang2024gear,\n  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},\n  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},\n  year = {2024},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2403.05527},\n  eprint = {2403.05527},\n  archivePrefix = {arXiv},\n}\n\n@misc{duanmu2024skvq,\n  title = {{SKVQ}: Sliding-window Key and Value Cache Quantization for Large Language Models},\n  author = {Haojie Duanmu and Zhihang Yuan and Xiuhong Li and Jiangfei Duan and Xingcheng Zhang and Dahua Lin},\n  year = {2024},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2405.06219},\n  eprint = {2405.06219},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{zhang2023h2o,\n  title = {{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author = {Zhenyu Zhang and Ying Sheng and Tianyi Zhou and Tianlong Chen and Lianmin Zheng and Ruisi Cai and Zhao Song and Yuandong Tian and Christopher R{\\'{e}} and Clark Barrett and Zhangyang Wang and Beidi Chen},\n  year = {2023},\n  booktitle = {NeurIPS 2023},\n  url = {https://arxiv.org/abs/2306.14048},\n}\n\n@inproceedings{li2024snapkv,\n  title = {{SnapKV}: {LLM} Knows What You are Looking for Before Generation},\n  author = {Yuhong Li and Yingbing Huang and Bowen Yang and Bharat Venkitesh and Acyr Locatelli and Hanchen Ye and Tianle Cai and Patrick Lewis and Deming Chen},\n  year = {2024},\n  booktitle = {NeurIPS 2024},\n  url = {https://arxiv.org/abs/2404.14469},\n}\n\n@inproceedings{ge2024fastgen,\n  title = {Model Tells You What to Discard: Adaptive {KV} Cache Compression for {LLMs}},\n  author = {Suyu Ge and Yunan Zhang and Liyuan Liu and Minjia Zhang and Jiawei Han and Jianfeng Gao},\n  year = {2024},\n  booktitle = {ICLR 2024},\n  url = {https://arxiv.org/abs/2310.01801},\n}\n\n@inproceedings{xiao2024streamingllm,\n  title = {Efficient Streaming Language Models with Attention Sinks},\n  author = {Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis},\n  year = {2024},\n  booktitle = {ICLR 2024},\n  url = {https://arxiv.org/abs/2309.17453},\n}\n\n@inproceedings{liu2024scissorhands,\n  title = {Scissorhands: Exploiting the Persistence of Importance Hypothesis for {LLM} {KV} Cache Compression at Test Time},\n  author = {Zichang Liu and Aditya Desai and Fangshuo Liao and Weitao Wang and Victor Xie and Zhaozhuo Xu and Anastasios Kyrillidis and Anshumali Shrivastava},\n  year = {2023},\n  booktitle = {NeurIPS 2023},\n  url = {https://arxiv.org/abs/2305.17118},\n}\n\n@inproceedings{yang2024pyramidinfer,\n  title = {{PyramidInfer}: Pyramid {KV} Cache Compression for High-throughput {LLM} Inference},\n  author = {Dongjie Yang and Xiaodong Han and Yan Gao and Yao Hu and Shilin Zhang and Hai Zhao},\n  year = {2024},\n  booktitle = {Findings of ACL 2024},\n  url = {https://arxiv.org/abs/2405.12532},\n}\n\n@misc{zuo2026ratequant,\n  title = {{RateQuant}: Optimal Mixed-Precision {KV} Cache Quantization via Rate-Distortion Theory},\n  author = {Fei Zuo and Zikang Zhou and Hao Cong and Xiaoyan Xi and Ho Fai Leung},\n  year = {2026},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2605.06675},\n  eprint = {2605.06675},\n  archivePrefix = {arXiv},\n}\n\n@misc{lei2026arkv,\n  title = {{ARKV}: Adaptive and Resource-Efficient {KV} Cache Management under Limited Memory Budget for Long-Context Inference in {LLMs}},\n  author = {Jianlong Lei and Shashikant Ilager},\n  year = {2026},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2603.08727},\n  eprint = {2603.08727},\n  archivePrefix = {arXiv},\n}\n\n@misc{li2025kvmix,\n  title = {{KVmix}: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for {KV} Cache},\n  author = {Fei Li and Song Liu and Weiguo Wu and Shiqiang Nie and Jinyu Wang},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2506.08018},\n  eprint = {2506.08018},\n  archivePrefix = {arXiv},\n}\n\n@misc{zhang2025mixkvq,\n  title = {{MixKVQ}: Query-Aware Mixed-Precision {KV} Cache Quantization for Long-Context Reasoning},\n  author = {Tao Zhang and Ziqian Zeng and Hao Peng and Huiping Zhuang and Cen Chen},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2512.19206},\n  eprint = {2512.19206},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{kim2024squeezellm,\n  title = {{SqueezeLLM}: Dense-and-Sparse Quantization},\n  author = {Sehoon Kim and Coleman Hooper and Amir Gholami and Zhen Dong and Xiuyu Li and Sheng Shen and Michael W. Mahoney and Kurt Keutzer},\n  year = {2024},\n  booktitle = {ICML 2024},\n  url = {https://arxiv.org/abs/2306.07629},\n}\n\n@inproceedings{voita2019analyzing,\n  title = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},\n  author = {Elena Voita and David Talbot and Fedor Moiseev and Rico Sennrich and Ivan Titov},\n  year = {2019},\n  booktitle = {ACL 2019},\n  url = {https://arxiv.org/abs/1905.09418},\n}\n\n@inproceedings{michel2019sixteen,\n  title = {Are Sixteen Heads Really Better than One?},\n  author = {Paul Michel and Omer Levy and Graham Neubig},\n  year = {2019},\n  booktitle = {NeurIPS 2019},\n  url = {https://arxiv.org/abs/1905.10650},\n}\n",
      "numLines": 166,
      "startLine": 1,
      "totalLines": 166
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check for `\cite` references and verify they all exist in the bib file. Let me also check for `\bibliographystyle` which seems missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "8cc5ffbf-4936-4cc0-a253-33da304ad45f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CujnU4V7D4ivyhqC98ppyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7307,
      "cache_read_input_tokens": 46120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7307
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

_source line 60_

Let me check cite references match bib entries, and look for a few more issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "0edcaadf-09bf-4763-9ff9-4a49d0fc3ca7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CujnU4V7D4ivyhqC98ppyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7307,
      "cache_read_input_tokens": 46120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7307
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

_source line 61_

<details open><summary>🔧 Tool call — Grep · `toolu_0121axy236qjaDnaUQ4bMXtm`</summary>

```json
{
  "pattern": "\\\\cite\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "def0f0f0-f3ea-4e4c-a79a-f30ea73ca465",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CujnU4V7D4ivyhqC98ppyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7307,
      "cache_read_input_tokens": 46120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7307
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

_source line 62 · 2026-05-14T12:15:24.732Z_

<details><summary>↩ Tool result · `toolu_0121axy236qjaDnaUQ4bMXtm`</summary>

```text
docs/paper/related_work.tex:4:Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\cite{lin2024qserve}, salient-token identification~\cite{he2024zipcache}, low-rank plus sparse correction~\cite{kang2024gear}, and sliding-window adaptation~\cite{duanmu2024skvq}.
docs/paper/related_work.tex:8:Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
docs/paper/related_work.tex:12:RateQuant~\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\{2,\ldots,6\}$ via the polymatroid structure.
docs/paper/related_work.tex:14:Related mixed-precision work operates at coarser granularity (layer-level~\cite{li2025kvmix}, memory-budget-level~\cite{lei2026arkv}), at the weight level~\cite{kim2024squeezellm}, or dynamically at inference time~\cite{zhang2025mixkvq}; our allocation is static and per-head.
docs/paper/related_work.tex:17:Prior work studies head redundancy and pruning~\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.
docs/paper/experiments.tex:30:(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
docs/paper/method.tex:17:RateQuant~\cite{zuo2026ratequant} solves this for consecutive bit-widths $\{2,3,4,5,6\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).
docs/paper/introduction.tex:5:Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
docs/paper/introduction.tex:6:RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "e2a1f9ba-56b6-4af7-9e9a-237f00a05a03",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:4:Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\\cite{lin2024qserve}, salient-token identification~\\cite{he2024zipcache}, low-rank plus sparse correction~\\cite{kang2024gear}, and sliding-window adaptation~\\cite{duanmu2024skvq}.\ndocs/paper/related_work.tex:8:Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\\cite{zhang2023h2o}, per-head important tokens~\\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\\cite{liu2024scissorhands}, attention sinks~\\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\\cite{yang2024pyramidinfer}.\ndocs/paper/related_work.tex:12:RateQuant~\\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\\{2,\\ldots,6\\}$ via the polymatroid structure.\ndocs/paper/related_work.tex:14:Related mixed-precision work operates at coarser granularity (layer-level~\\cite{li2025kvmix}, memory-budget-level~\\cite{lei2026arkv}), at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.\ndocs/paper/related_work.tex:17:Prior work studies head redundancy and pruning~\\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.\ndocs/paper/experiments.tex:30:(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\ndocs/paper/method.tex:17:RateQuant~\\cite{zuo2026ratequant} solves this for consecutive bit-widths $\\{2,3,4,5,6\\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).\ndocs/paper/introduction.tex:5:Recent work on KV cache quantization explores both uniform schemes~\\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\\cite{zhang2023h2o,li2024snapkv}.\ndocs/paper/introduction.tex:6:RateQuant~\\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\\{2,3,4,5,6\\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).",
    "numLines": 9
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Grep · `toolu_012GMKojcWKpVJYMPZ1xNt9g`</summary>

```json
{
  "pattern": "\\\\ref\\{sec:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "0b21ffe4-81f8-4c40-94ee-70071149d6c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CujnU4V7D4ivyhqC98ppyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7307,
      "cache_read_input_tokens": 46120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7307
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

_source line 64 · 2026-05-14T12:15:26.435Z_

<details><summary>↩ Tool result · `toolu_012GMKojcWKpVJYMPZ1xNt9g`</summary>

```text
docs/paper/analysis.tex:51:\item Run per-head profiling as described in \S\ref{sec:profiling}.
docs/paper/related_work.tex:18:Our analysis asks a different question: which heads are sensitive to \emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\S\ref{sec:heterogeneity}).
docs/paper/experiments.tex:21:Unless marked with $\dagger$, all results use standard-resolution profiling; \S\ref{sec:profiling_resolution} analyzes the effect of resolution.
docs/paper/experiments.tex:25:The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).
docs/paper/experiments.tex:57:Higher-resolution profiling (64 seq $\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in \S\ref{sec:profiling_resolution}.
docs/paper/experiments.tex:85:\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\geq$4$\times$). Standard-resolution profiling; hires results in \S\ref{sec:profiling_resolution}.}
docs/paper/experiments.tex:104:Hires profiling further reduces this to 10.91 (\S\ref{sec:profiling_resolution}).
docs/paper/conclusion.tex:19:Integration with production inference engines (vLLM, TensorRT-LLM) would enable real-kernel latency measurement, and investigating per-side K/V cardinality constraints (\S\ref{sec:kv_separation}) or dynamic per-request allocation could further improve the framework.
docs/paper/method.tex:19:Moreover, as we show in \S\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.
docs/paper/method.tex:99:\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\times$ 2048 tok) achieves 10.91 (\S\ref{sec:profiling_resolution}).}
docs/paper/introduction.tex:22:We add a single cardinality constraint $\sum_h \mathbb{1}[b_h{=}2] \leq k$ to the standard MCKP formulation (\S\ref{sec:method}).
docs/paper/introduction.tex:29:The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal (\S\ref{sec:solver_equiv}), enabling practitioners to use the simpler $O(H \log H)$ greedy algorithm without sacrificing solution quality.
docs/paper/introduction.tex:30:A per-layer brute-force oracle confirms near-optimality: the maximum gap across 28 layers is 0.02 PPL, 0.4\% of the total improvement (\S\ref{sec:solver_equiv}).
docs/paper/introduction.tex:39:We propose a heterogeneity diagnostic based on the top-5\% concentration of per-head distortion (\S\ref{sec:heterogeneity}).
docs/paper/introduction.tex:45:\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
docs/paper/introduction.tex:47:\item We demonstrate that the cardinality constraint makes solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent per-head allocations across three architectures, enabling use of a simple greedy algorithm (\S\ref{sec:solver_equiv}).
docs/paper/introduction.tex:49:\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes (\S\ref{sec:heterogeneity}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "71495fbe-6410-46ba-91da-68d34b934ea5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:51:\\item Run per-head profiling as described in \\S\\ref{sec:profiling}.\ndocs/paper/related_work.tex:18:Our analysis asks a different question: which heads are sensitive to \\emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).\ndocs/paper/experiments.tex:21:Unless marked with $\\dagger$, all results use standard-resolution profiling; \\S\\ref{sec:profiling_resolution} analyzes the effect of resolution.\ndocs/paper/experiments.tex:25:The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).\ndocs/paper/experiments.tex:57:Higher-resolution profiling (64 seq $\\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in \\S\\ref{sec:profiling_resolution}.\ndocs/paper/experiments.tex:85:\\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\\geq$4$\\times$). Standard-resolution profiling; hires results in \\S\\ref{sec:profiling_resolution}.}\ndocs/paper/experiments.tex:104:Hires profiling further reduces this to 10.91 (\\S\\ref{sec:profiling_resolution}).\ndocs/paper/conclusion.tex:19:Integration with production inference engines (vLLM, TensorRT-LLM) would enable real-kernel latency measurement, and investigating per-side K/V cardinality constraints (\\S\\ref{sec:kv_separation}) or dynamic per-request allocation could further improve the framework.\ndocs/paper/method.tex:19:Moreover, as we show in \\S\\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.\ndocs/paper/method.tex:99:\\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\\times$ 2048 tok) achieves 10.91 (\\S\\ref{sec:profiling_resolution}).}\ndocs/paper/introduction.tex:22:We add a single cardinality constraint $\\sum_h \\mathbb{1}[b_h{=}2] \\leq k$ to the standard MCKP formulation (\\S\\ref{sec:method}).\ndocs/paper/introduction.tex:29:The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal (\\S\\ref{sec:solver_equiv}), enabling practitioners to use the simpler $O(H \\log H)$ greedy algorithm without sacrificing solution quality.\ndocs/paper/introduction.tex:30:A per-layer brute-force oracle confirms near-optimality: the maximum gap across 28 layers is 0.02 PPL, 0.4\\% of the total improvement (\\S\\ref{sec:solver_equiv}).\ndocs/paper/introduction.tex:39:We propose a heterogeneity diagnostic based on the top-5\\% concentration of per-head distortion (\\S\\ref{sec:heterogeneity}).\ndocs/paper/introduction.tex:45:\\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\\times$ compression (\\S\\ref{sec:compounding}, \\S\\ref{sec:experiments}).\ndocs/paper/introduction.tex:47:\\item We demonstrate that the cardinality constraint makes solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent per-head allocations across three architectures, enabling use of a simple greedy algorithm (\\S\\ref{sec:solver_equiv}).\ndocs/paper/introduction.tex:49:\\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes (\\S\\ref{sec:heterogeneity}).",
    "numLines": 17
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Grep · `toolu_01UTvyRSQ2BGP9wVCrqRXQmY`</summary>

```json
{
  "pattern": "\\\\label\\{sec:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "907125e8-796a-4253-84e0-df6ca68c63c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CujnU4V7D4ivyhqC98ppyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7307,
      "cache_read_input_tokens": 46120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7307
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

_source line 66 · 2026-05-14T12:15:26.608Z_

<details><summary>↩ Tool result · `toolu_01UTvyRSQ2BGP9wVCrqRXQmY`</summary>

```text
docs/paper/analysis.tex:2:\label{sec:analysis}
docs/paper/analysis.tex:5:\label{sec:heterogeneity}
docs/paper/analysis.tex:46:\label{sec:diagnostic}
docs/paper/analysis.tex:66:\label{sec:aggressive}
docs/paper/analysis.tex:74:\label{sec:profiling_resolution}
docs/paper/analysis.tex:98:\label{sec:kv_separation}
docs/paper/related_work.tex:1:\section{Related Work}\label{sec:related_work}
docs/paper/experiments.tex:2:\label{sec:experiments}
docs/paper/experiments.tex:5:\label{sec:setup}
docs/paper/experiments.tex:36:\label{sec:main_results}
docs/paper/experiments.tex:80:\label{sec:budget_sweep}
docs/paper/experiments.tex:111:\label{sec:heuristic}
docs/paper/experiments.tex:142:\label{sec:downstream}
docs/paper/experiments.tex:171:\label{sec:cross_dataset}
docs/paper/conclusion.tex:1:\section{Conclusion}\label{sec:conclusion}
docs/paper/method.tex:2:\label{sec:method}
docs/paper/method.tex:5:\label{sec:formulation}
docs/paper/method.tex:22:\label{sec:profiling}
docs/paper/method.tex:32:\label{sec:compounding}
docs/paper/method.tex:59:\label{sec:cardinality}
docs/paper/method.tex:79:\label{sec:solver_equiv}
docs/paper/introduction.tex:2:\label{sec:introduction}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "559bf59c-5072-4067-9730-8c68238e2864",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:2:\\label{sec:analysis}\ndocs/paper/analysis.tex:5:\\label{sec:heterogeneity}\ndocs/paper/analysis.tex:46:\\label{sec:diagnostic}\ndocs/paper/analysis.tex:66:\\label{sec:aggressive}\ndocs/paper/analysis.tex:74:\\label{sec:profiling_resolution}\ndocs/paper/analysis.tex:98:\\label{sec:kv_separation}\ndocs/paper/related_work.tex:1:\\section{Related Work}\\label{sec:related_work}\ndocs/paper/experiments.tex:2:\\label{sec:experiments}\ndocs/paper/experiments.tex:5:\\label{sec:setup}\ndocs/paper/experiments.tex:36:\\label{sec:main_results}\ndocs/paper/experiments.tex:80:\\label{sec:budget_sweep}\ndocs/paper/experiments.tex:111:\\label{sec:heuristic}\ndocs/paper/experiments.tex:142:\\label{sec:downstream}\ndocs/paper/experiments.tex:171:\\label{sec:cross_dataset}\ndocs/paper/conclusion.tex:1:\\section{Conclusion}\\label{sec:conclusion}\ndocs/paper/method.tex:2:\\label{sec:method}\ndocs/paper/method.tex:5:\\label{sec:formulation}\ndocs/paper/method.tex:22:\\label{sec:profiling}\ndocs/paper/method.tex:32:\\label{sec:compounding}\ndocs/paper/method.tex:59:\\label{sec:cardinality}\ndocs/paper/method.tex:79:\\label{sec:solver_equiv}\ndocs/paper/introduction.tex:2:\\label{sec:introduction}",
    "numLines": 22
  }
}
```

</details>

---

### Runtime record

_source line 67_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1778922000,
    "rateLimitType": "seven_day",
    "utilization": 0.9,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "2b289a42-8c4b-44c9-aae6-f24becf530d2",
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8"
}
```

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
Now let me compile the full report. Let me analyze all findings:

**1. Figure 文件完整性**
- `figures/fig1_head_delta_heatmap.pdf` ✅
- `figures/fig2_compounding_curve.pdf` ✅
- `figures/fig3_allocation_comparison.pdf` ✅

All three figures exist.

**2. LaTeX 引用完整性**

Figure references:
- `\includegraphics{figures/fig1_head_delta_heatmap.pdf}` in analysis.tex → file exists ✅


- `\includegraphics{figures/fig2_compounding_curve.pdf}` in method.tex → file exists ✅
- `\includegraphics{figures/fig3_allocation_comparison.pdf}` in experiments.tex → file exists ✅

All figure labels match their references correctly, with the compounding figure referenced twice throughout the document. Now checking table labels...

All six table labels have corresponding references in place. I'm also verifying section references, and the profiling section label is properly linked.

Now checking the remaining section references across the files—heterogeneity, profiling resolution, method, compounding, experiments, and solver equivalence all have their labels defined and matched correctly.

I'm verifying all the citation keys used throughout the document, and they're all accounted for across the various papers on KV cache optimization techniques.

Now I'm checking the overall paper structure—looking at the file organization, line counts for each section, and confirming the proper input order in main.tex. The document flows logically from abstract through introduction, related work, methodology, experiments, analysis, and conclusion, with all required sections present.

Regarding the bibliography setup, the ACL package with the review option should handle the bibliography style automatically through its internal configuration, so the explicit `\bibliographystyle` declaration isn't necessary here.

Now I'm checking the precision of the PPL values throughout the document — the main perplexity metrics are all consistently formatted to two decimal places, the delta values match that same precision, and even the extreme compression values maintain two decimal places where applicable. The per-layer oracle gaps use a different precision level at three decimal places, but that's appropriate for those smaller values.

However, I'm noticing some inconsistencies in how these small gap values are reported across different sections. The Layer 1 gap appears as both 0.018 and 0.0183 in different files, and the abstract rounds it to 0.02, which creates a mismatch. These should all align to the same decimal precision throughout the paper.

I'm also seeing that the downstream table intentionally omits individual bf16 baseline values for most benchmarks, showing only dashes with the average reported separately — this is a deliberate stylistic choice rather than an error. And I need to verify that the equation references for the objective and constraint are properly linked throughout the document. is used in method.tex:27 ✅
- I don't see `\eqref{eq:constraint}` or `\ref{eq:constraint}` used anywhere. The equation is defined but never cross-referenced. Minor — equations don't need to be referenced, but it's worth noting.

5. **The conclusion mentions `$k \leq 8$ (7\% of heads)`** but this is specific to Qwen. The notation is correct.

6. **Budget sweep table (tab:budget_sweep)**: Looking at the $\Delta$ column values, I need to verify the arithmetic. At 2×, the delta is $-$0.56, which matches 10.10 - 10.66 = -0.56, so uniform minus constrained gives a negative value when constrained performs worse. But at 4×, the table shows 4.21 while my calculation gives 15.45 - 11.23 = 4.22 — there's a discrepancy of 0.01 that might be a rounding error or typo in the table.

Let me verify the 8× row: 14,759 - 907 = 13,852, which matches the table's 13,852 ✅

So the 4× entry appears to have a minor arithmetic inconsistency.

Now I'm checking whether the ACL package and its style files are actually present in the paper directory, since the document uses `\usepackage[review]{acl}` which requires acl.sty and acl_natbib.bst to compile properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "3c2773d8-1196-4960-a013-fc39697d1642",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTfsNGJF8KQiJcWUWHAmpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 53427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2869
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

_source line 69_

Let me check if the ACL style files are present.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "b46c0983-09e0-447d-b8d8-812c87749e4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTfsNGJF8KQiJcWUWHAmpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 53427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2869
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

_source line 70_

<details open><summary>🔧 Tool call — Glob · `toolu_01TXEmzcFWTPaaSPgR6d37ep`</summary>

```json
{
  "pattern": "**/*.{sty,bst,cls}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "28e2e108-381f-4da0-b483-52e00edcde56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTfsNGJF8KQiJcWUWHAmpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 53427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2869
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

_source line 71 · 2026-05-14T12:16:20.345Z_

<details><summary>↩ Tool result · `toolu_01TXEmzcFWTPaaSPgR6d37ep`</summary>

```text
docs/paper/acl.sty
docs/paper/acl_natbib.bst
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "854d053c-f97a-4930-9f6e-48348c5cff00",
  "tool_use_result": {
    "filenames": [
      "docs/paper/acl.sty",
      "docs/paper/acl_natbib.bst"
    ],
    "durationMs": 5,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 72_

ACL 模板文件齐全。以下是完整检查报告。

---

## 论文编译 & Figure 完整性检查报告

### 1. Figure 文件完整性 ✅

`docs/paper/figures/` 下 3 个 PDF 文件，全部存在：
| 文件 | 状态 |
|------|------|
| `fig1_head_delta_heatmap.pdf` | ✅ |
| `fig2_compounding_curve.pdf` | ✅ |
| `fig3_allocation_comparison.pdf` | ✅ |

### 2. LaTeX 引用完整性 ✅

**Figure 引用**：3 个 `\includegraphics` 全部指向存在的文件，3 个 `\label{fig:*}` 均有对应 `\ref{fig:*}`。

**Table 引用**：6 个 table label（`main_results`, `budget_sweep`, `heuristic`, `downstream`, `solver_equiv`, `heterogeneity`）全部有对应 `\ref`。

**Section 引用**：所有 `\S\ref{sec:*}` 引用（`profiling`, `heterogeneity`, `profiling_resolution`, `method`, `compounding`, `experiments`, `solver_equiv`, `kv_separation`）均有对应 `\label`。

**Bibliography 引用**：19 个 `\cite` key 全部在 `references.bib` 中有对应条目。ACL 模板文件（`acl.sty`, `acl_natbib.bst`）存在。

### 3. 论文结构 ✅

| 文件 | 行数 | 章节 |
|------|------|------|
| main.tex | 31 | 入口文件 |
| abstract.tex | 7 | Abstract |
| introduction.tex | 50 | Introduction |
| related_work.tex | 17 | Related Work |
| method.tex | 118 | Method |
| experiments.tex | 177 | Experiments |
| analysis.tex | 110 | Analysis |
| conclusion.tex | 19 | Conclusion |
| **Total** | **529** | |

`main.tex` 的 `\input` 顺序：abstract → introduction → related_work → method → experiments → analysis → conclusion。结构完整。

### 4. 数字精度一致性

**PPL 值**：主要结果统一为小数点后 2 位（9.81, 15.45, 11.23, 8.45, 7.16 等）。✅

**发现 1 个问题**：

- **Tab 2 (budget_sweep) 算术误差**：Uniform 15.45 − Constrained 11.23 = **4.22**，但表中写的是 **4.21**。需修正。(`experiments.tex:92`)

**发现 1 个精度不一致**：

- Layer 1 oracle gap 在两处精度不同：`analysis.tex:93` 写 "0.018"，`method.tex:118` 写 "0.0183"。建议统一为 0.018 或 0.0183。

### 5. 其他观察

- `\bibliographystyle` 未显式声明——`acl.sty` 内部处理，编译应无问题。
- 论文总行数 529 行（不含 bib），对 ARR 8 页正文限制来说篇幅合理。

### 总结

**需修复**：1 项（budget_sweep 表 Δ 值 4.21 → 4.22）
**建议统一**：1 项（oracle gap 精度 0.018 vs 0.0183）
**其余检查项全部通过。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "uuid": "cb9e283e-1b42-47d3-b70a-193a02ec1322",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QpxM1RNQ88wN93xmjt2v8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3114,
      "cache_read_input_tokens": 56296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3114
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

_source line 73_

ACL 模板文件齐全。以下是完整检查报告。

---

## 论文编译 & Figure 完整性检查报告

### 1. Figure 文件完整性 ✅

`docs/paper/figures/` 下 3 个 PDF 文件，全部存在：
| 文件 | 状态 |
|------|------|
| `fig1_head_delta_heatmap.pdf` | ✅ |
| `fig2_compounding_curve.pdf` | ✅ |
| `fig3_allocation_comparison.pdf` | ✅ |

### 2. LaTeX 引用完整性 ✅

**Figure 引用**：3 个 `\includegraphics` 全部指向存在的文件，3 个 `\label{fig:*}` 均有对应 `\ref{fig:*}`。

**Table 引用**：6 个 table label（`main_results`, `budget_sweep`, `heuristic`, `downstream`, `solver_equiv`, `heterogeneity`）全部有对应 `\ref`。

**Section 引用**：所有 `\S\ref{sec:*}` 引用（`profiling`, `heterogeneity`, `profiling_resolution`, `method`, `compounding`, `experiments`, `solver_equiv`, `kv_separation`）均有对应 `\label`。

**Bibliography 引用**：19 个 `\cite` key 全部在 `references.bib` 中有对应条目。ACL 模板文件（`acl.sty`, `acl_natbib.bst`）存在。

### 3. 论文结构 ✅

| 文件 | 行数 | 章节 |
|------|------|------|
| main.tex | 31 | 入口文件 |
| abstract.tex | 7 | Abstract |
| introduction.tex | 50 | Introduction |
| related_work.tex | 17 | Related Work |
| method.tex | 118 | Method |
| experiments.tex | 177 | Experiments |
| analysis.tex | 110 | Analysis |
| conclusion.tex | 19 | Conclusion |
| **Total** | **529** | |

`main.tex` 的 `\input` 顺序：abstract → introduction → related_work → method → experiments → analysis → conclusion。结构完整。

### 4. 数字精度一致性

**PPL 值**：主要结果统一为小数点后 2 位（9.81, 15.45, 11.23, 8.45, 7.16 等）。✅

**发现 1 个问题**：

- **Tab 2 (budget_sweep) 算术误差**：Uniform 15.45 − Constrained 11.23 = **4.22**，但表中写的是 **4.21**。需修正。(`experiments.tex:92`)

**发现 1 个精度不一致**：

- Layer 1 oracle gap 在两处精度不同：`analysis.tex:93` 写 "0.018"，`method.tex:118` 写 "0.0183"。建议统一为 0.018 或 0.0183。

### 5. 其他观察

- `\bibliographystyle` 未显式声明——`acl.sty` 内部处理，编译应无问题。
- 论文总行数 529 行（不含 bib），对 ARR 8 页正文限制来说篇幅合理。

### 总结

**需修复**：1 项（budget_sweep 表 Δ 值 4.21 → 4.22）
**建议统一**：1 项（oracle gap 精度 0.018 vs 0.0183）
**其余检查项全部通过。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 121264,
  "duration_api_ms": 121934,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "c2444b83-0957-48d4-b24c-4d6abb61d0a8",
  "total_cost_usd": 0.60697925,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 47569,
    "cache_read_input_tokens": 268388,
    "output_tokens": 6974,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 47569,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1021,
        "cache_read_input_tokens": 56296,
        "cache_creation_input_tokens": 3114,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3114
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1004,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001084,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 6974,
      "cacheReadInputTokens": 268388,
      "cacheCreationInputTokens": 47569,
      "webSearchRequests": 0,
      "costUSD": 0.6058952500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c48c4c8f-28bd-4c45-ad28-3930e0962b07"
}
```

</details>

---
