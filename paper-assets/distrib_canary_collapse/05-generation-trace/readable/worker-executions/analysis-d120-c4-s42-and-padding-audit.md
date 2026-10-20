# analysis d120 c4 s42 and padding audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 71
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/workers/worker_analysis_d120_c4_s42_and_padding_audit_20260520T060208.log`
- **Structured JSON:** [`fcd62821e8cfb003770e.json`](../../sessions/fc/fcd62821e8cfb003770e.json)

## Before a recorded user message

71 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
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
  "uuid": "c9e08a48-b9d6-43fc-ab8b-89ed4b4d1ad0",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
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
    "resetsAt": 1779273600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f5fb51e3-fef4-4cf9-a535-534a5138133c",
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down this task:

1. Find actual directory names for C4 s42 experiments and padding_robustness on westd-17855
2. Confirm the script version has D105 true 3σ fix
3. Run analysis for each experiment
4. Collect results
5. Pay special attention to padding_robustness
6. Update registry
7. Write report to artifacts

Let me start by finding the directories and confirming the script version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "83012288-5d5e-43da-ac55-d5b955ac2011",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpJgoqjgZtU2JR6xeD9d4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13445,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13445
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

开始执行 D120 重算。先探测目录和脚本版本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "c606f2cc-774b-42d8-9582-6bbfdf47f08c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpJgoqjgZtU2JR6xeD9d4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13445,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13445
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QNqZoS7GHAB122hgSBffGZ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
  "max_results": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "83f5384c-b8e4-495c-af0c-e7bd4affd4ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpJgoqjgZtU2JR6xeD9d4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13445,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13445
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

_source line 7 · 2026-05-20T06:02:26.907Z_

<details><summary>↩ Tool result · `toolu_01QNqZoS7GHAB122hgSBffGZ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
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
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "6dc5f07e-da6b-42fd-9b95-d8baa846815d",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 29
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014Vi5jZTCqcPbHTagF5NHDN`</summary>

```json
{
  "server": "westd-17855",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && ls -d results/alpha_sweep/c4_* results/padding_robustness/* 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "97f56fea-ef91-4bc6-881d-b9836d915e43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcLQS2WwUGs5gzcE58MB6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2531,
      "cache_read_input_tokens": 25286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2531
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 9 · 2026-05-20T06:02:31.036Z_

<details><summary>↩ Tool result · `toolu_014Vi5jZTCqcPbHTagF5NHDN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "e8302eac-c5a5-4556-8fb3-57578d0fc960",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WetgRCYGoQgLFsfTcG8zPJ`</summary>

```json
{
  "server": "westd-17855",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && grep -A10 \"def _onset_gen\" run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "2bdace9b-f674-4ec0-9c49-b9885fba3b71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcLQS2WwUGs5gzcE58MB6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2531,
      "cache_read_input_tokens": 25286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2531
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 11 · 2026-05-20T06:02:32.561Z_

<details><summary>↩ Tool result · `toolu_01WetgRCYGoQgLFsfTcG8zPJ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "92236421-fb58-46b8-8797-27e9cd075f57",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CjvhpNBp3MgZJGnRWQuMLU`</summary>

```json
{
  "server": "westd-17855",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && python run_5method_analysis_d102.py --help 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "4207a5c8-7826-48bb-b5ab-b92bc6f89184",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcLQS2WwUGs5gzcE58MB6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2531,
      "cache_read_input_tokens": 25286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2531
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 13 · 2026-05-20T06:02:33.374Z_

<details><summary>↩ Tool result · `toolu_01CjvhpNBp3MgZJGnRWQuMLU`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "27439952-3fdc-4ab1-9662-2d2d599f12b1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
The ssh_read_only tool doesn't allow shell metacharacters like `&&`. I need to use simple commands without chaining.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "5cc8a167-9d09-4c26-b088-941b57e5957f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnbfoAaj6HGdyPn1MvJrEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 755,
      "cache_read_input_tokens": 27817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 755
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

_source line 15_

需要避免 `&&` 在 read_only 中。重新用单条命令探测。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "a0c6d465-38c6-44c1-a62f-b737e05c7d5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnbfoAaj6HGdyPn1MvJrEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 755,
      "cache_read_input_tokens": 27817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 755
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

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EwGHvD3WZS8pmzEAc7W6AX`</summary>

```json
{
  "server": "westd-17855",
  "command": "ls -d /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "ad26b95c-c052-4ae8-91be-7c08a279a1c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnbfoAaj6HGdyPn1MvJrEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 755,
      "cache_read_input_tokens": 27817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 755
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

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011tKYPPeiAoDDDWCaEMp7b6`</summary>

```json
{
  "server": "westd-17855",
  "command": "ls -d /root/autodl-tmp/distrib_canary_collapse/results/padding_robustness/*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "dc6459f4-74f4-46cf-ab10-6242d77328f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnbfoAaj6HGdyPn1MvJrEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 755,
      "cache_read_input_tokens": 27817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 755
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

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KzgC2xWYrw7W2WT75kF8bR`</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -A10 \"def _onset_gen\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "6acb80f3-205d-4830-8519-116ea4a54246",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnbfoAaj6HGdyPn1MvJrEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 755,
      "cache_read_input_tokens": 27817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 755
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

_source line 19 · 2026-05-20T06:02:42.721Z_

<details><summary>↩ Tool result · `toolu_01EwGHvD3WZS8pmzEAc7W6AX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a025_s42_fp32\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s42_fp32\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "f97d81ab-0922-4b4b-97c6-41cd4d54af94",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a025_s42_fp32\\\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32\\\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s42_fp32\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a025_s42_fp32\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s42_fp32\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.77}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T06:02:49.609Z_

<details><summary>↩ Tool result · `toolu_011tKYPPeiAoDDDWCaEMp7b6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/padding_robustness/a100_s42_fp32\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.87}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "88c3c21e-979c-4f26-ac7c-a53ef3e291fa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/padding_robustness/a100_s42_fp32\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.87}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/padding_robustness/a100_s42_fp32\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.87}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T06:02:50.902Z_

<details><summary>↩ Tool result · `toolu_01KzgC2xWYrw7W2WT75kF8bR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"def _onset_gen(series, name):\\n    s = orient(series, name)\\n    base, sigma = s[0], np.std(s)\\n    if sigma < 1e-12:\\n        return None\\n    thresh = base + 3.0 * sigma\\n    for i in range(1, len(s)):\\n        if s[i] > thresh:\\n            return i\\n    return None\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.28}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "9f2be75a-788f-45e5-9333-2f1ab056e43e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"def _onset_gen(series, name):\\\\n    s = orient(series, name)\\\\n    base, sigma = s[0], np.std(s)\\\\n    if sigma < 1e-12:\\\\n        return None\\\\n    thresh = base + 3.0 * sigma\\\\n    for i in range(1, len(s)):\\\\n        if s[i] > thresh:\\\\n            return i\\\\n    return None\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.28}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"def _onset_gen(series, name):\\n    s = orient(series, name)\\n    base, sigma = s[0], np.std(s)\\n    if sigma < 1e-12:\\n        return None\\n    thresh = base + 3.0 * sigma\\n    for i in range(1, len(s)):\\n        if s[i] > thresh:\\n            return i\\n    return None\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.28}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Good. Directory names found:
- `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a025_s42_fp32`
- `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32`
- `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s42_fp32`


- `/root/autodl-tmp/distrib_canary_collapse/results/padding_robustness/a100_s42_fp32`

The script version is confirmed to use the full series standard deviation for the onset calculation, which is the correct D105 fix. Let me check the script help to understand the argument format before running the analyses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "54044655-36ca-4045-93ab-32e6db7463ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yNw3PyFLc3VB6stJhuq9J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 984,
      "cache_read_input_tokens": 28572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 984
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

_source line 23_

目录和脚本都确认了。`_onset_gen` 使用 `np.std(s)` — D105 true 3σ 已就绪。检查脚本参数格式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "a332cfcb-4a4c-4111-8392-d974d32b0561",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yNw3PyFLc3VB6stJhuq9J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 984,
      "cache_read_input_tokens": 28572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 984
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01GRwAs9c1Ncg1tH1oUv9m37`</summary>

```json
{
  "server": "westd-17855",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python run_5method_analysis_d102.py --help 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "a9e6b306-425d-407b-aa35-e7a8ffd5deee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yNw3PyFLc3VB6stJhuq9J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 984,
      "cache_read_input_tokens": 28572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 984
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

_source line 25 · 2026-05-20T06:03:02.891Z_

<details><summary>↩ Tool result · `toolu_01GRwAs9c1Ncg1tH1oUv9m37`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: run_5method_analysis_d102.py [-h] --data_dir DATA_DIR --alpha ALPHA\\n                                    --seed SEED [--dry-run]\\n\\n5-method lead-lag analysis\\n\\noptions:\\n  -h, --help           show this help message and exit\\n  --data_dir DATA_DIR  Path to experiment directory (e.g.\\n                       results/alpha_sweep/a000_s43)\\n  --alpha ALPHA        Alpha value (e.g. 0.0, 0.75)\\n  --seed SEED          Random seed\\n  --dry-run            Check data availability without running analysis\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.85}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "8eedbaf2-c70d-4599-a6e2-5a49e3417454",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"usage: run_5method_analysis_d102.py [-h] --data_dir DATA_DIR --alpha ALPHA\\\\n                                    --seed SEED [--dry-run]\\\\n\\\\n5-method lead-lag analysis\\\\n\\\\noptions:\\\\n  -h, --help           show this help message and exit\\\\n  --data_dir DATA_DIR  Path to experiment directory (e.g.\\\\n                       results/alpha_sweep/a000_s43)\\\\n  --alpha ALPHA        Alpha value (e.g. 0.0, 0.75)\\\\n  --seed SEED          Random seed\\\\n  --dry-run            Check data availability without running analysis\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.85}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"usage: run_5method_analysis_d102.py [-h] --data_dir DATA_DIR --alpha ALPHA\\n                                    --seed SEED [--dry-run]\\n\\n5-method lead-lag analysis\\n\\noptions:\\n  -h, --help           show this help message and exit\\n  --data_dir DATA_DIR  Path to experiment directory (e.g.\\n                       results/alpha_sweep/a000_s43)\\n  --alpha ALPHA        Alpha value (e.g. 0.0, 0.75)\\n  --seed SEED          Random seed\\n  --dry-run            Check data availability without running analysis\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.85}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Parameters: `--data_dir`, `--alpha`, `--seed`. Now I can run all 4 experiments. Let me run them sequentially since they're CPU tasks and I want to capture each output. Actually, let me run them in parallel since they're independent.

For C4 experiments:
- c4_a025_s42_fp32: alpha=0.25, seed=42
- c4_a050_s42_fp32: alpha=0.50, seed=42


- c4_a075_s42_fp32: alpha=0.75, seed=42

For padding:
- a100_s42_fp32: alpha=1.0, seed=42

I'll execute all 4 in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "64a5f950-2661-491c-a30f-5483ce21c135",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdUcFwg1yeoHjABw5GQwGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 29556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 771
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

_source line 27_

参数格式确认：`--data_dir`, `--alpha`, `--seed`。并行运行 4 个实验分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "538eb2c3-1727-457d-99e7-9baa70329d78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdUcFwg1yeoHjABw5GQwGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 29556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 771
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01EwQudCeakVceLNnkSAGfwc`</summary>

```json
{
  "server": "westd-17855",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python run_5method_analysis_d102.py --data_dir results/alpha_sweep/c4_a025_s42_fp32 --alpha 0.25 --seed 42 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "c68726c5-af9b-49ef-8c9e-30c363fc6ad5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdUcFwg1yeoHjABw5GQwGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 29556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 771
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_015vZvi4RDMnoHCANKanVjfG`</summary>

```json
{
  "server": "westd-17855",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python run_5method_analysis_d102.py --data_dir results/alpha_sweep/c4_a050_s42_fp32 --alpha 0.50 --seed 42 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "a5417f69-2c4e-43f2-afb6-ee2704a75300",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdUcFwg1yeoHjABw5GQwGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 29556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 771
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

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_017QLp2L9NPEkpX6JiSPZkHL`</summary>

```json
{
  "server": "westd-17855",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python run_5method_analysis_d102.py --data_dir results/alpha_sweep/c4_a075_s42_fp32 --alpha 0.75 --seed 42 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "b78ffa89-656b-4357-9e29-79ef204468ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdUcFwg1yeoHjABw5GQwGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 29556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 771
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

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01VqnLi5GT9wYjujewj6XwcR`</summary>

```json
{
  "server": "westd-17855",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python run_5method_analysis_d102.py --data_dir results/padding_robustness/a100_s42_fp32 --alpha 1.0 --seed 42 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "8a3478dd-449f-4135-856f-7b1a0e147337",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdUcFwg1yeoHjABw5GQwGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 29556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 771
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

_source line 32 · 2026-05-20T06:03:16.257Z_

<details><summary>↩ Tool result · `toolu_01EwQudCeakVceLNnkSAGfwc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"==== ================================================================================================\\n5-METHOD LEAD-LAG ANALYSIS | alpha=0.25 | seed=42\\nData: results/alpha_sweep/c4_a025_s42_fp32\\n==== ================================================================================================\\nLoaded 11 generations\\n\\n====================================================================================================\\nFORWARD (canary ₆ downstream)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ntoken_entropy&lt;distinct_1   -0.945    -2  -0.962    -3   0.0022     -1  10.981   0.0942              N/A     N/A     0\\ntoken_entropy&lt;distinct_2    0.770     1  -0.883    -3   0.0138   None   9.327   0.0942              N/A     N/A     1\\ntoken_entropy&lt;distinct_3    0.921     3   0.774    -1   0.0164      6  13.005   0.0942              N/A     N/A     1\\ntoken_entropy&lt;mauve         0.903    -1   0.795    -1   0.0138   None  14.951   0.0942              N/A     N/A     0\\nece&lt;distinct_1             -0.942    -2  -0.962    -3   0.0022     -2  10.770   0.0942              N/A     N/A     1\\nece&lt;distinct_2              0.782     0  -0.891    -3   0.0138   None   8.953   0.0942              N/A     N/A     1\\nece&lt;distinct_3              0.894     2   0.744    -1   0.0216      5  12.440   0.0942              N/A     N/A     1\\nece&lt;mauve                   0.894    -1   0.797    -1   0.0138   None  17.913   0.0942              N/A     N/A     1\\n\\n====================================================================================================\\nREVERSE (downstream ₆ canary)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ndistinct_1&lt;token_entropy   -0.945     2  -0.962     3   0.0022      1   1.068   0.0942              N/A     N/A     0\\ndistinct_2&lt;token_entropy    0.770    -1  -0.883     3   0.0138   None   1.095   0.0942              N/A     N/A     1\\ndistinct_3&lt;token_entropy    0.921    -3   0.774     1   0.0164     -6   1.167   0.0942              N/A     N/A     1\\nmauve&lt;token_entropy         0.903     1   0.795     1   0.0138   None   0.000   0.0942              N/A     N/A     0\\ndistinct_1&lt;ece             -0.942     2  -0.962     3   0.0022      2   7.542   0.0942              N/A     N/A     1\\ndistinct_2&lt;ece              0.782     0  -0.891     3   0.0138   None   6.558   0.0942              N/A     N/A     1\\ndistinct_3&lt;ece              0.894    -2   0.744     1   0.0216     -5   7.490   0.0942              N/A     N/A     1\\nmauve&lt;ece                   0.894     1   0.797     1   0.0138   None  15.404   0.0942              N/A     N/A     1\\n\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nCONSENSUS (methods agreeing on forward significance)\\n====================================================================================================\\n  token_entropy&lt;distinct_1  2/5  [naive, diff]\\n  token_entropy&lt;distinct_2  1/5  [diff]\\n  token_entropy&lt;distinct_3  2/5  [diff, threshold]\\n  token_entropy&lt;mauve       2/5  [naive, diff]\\n  ece&lt;distinct_1            2/5  [naive, diff]\\n  ece&lt;distinct_2            1/5  [diff]\\n  ece&lt;distinct_3            2/5  [diff, threshold]\\n  ece&lt;mauve                 2/5  [naive, diff]\\n\\n  Robust pairs (>=3/5 methods): 0/8\\n  Perm Granger FDR sig (fwd): 0/8\\n\\nSaved: results/alpha_sweep/c4_a025_s42_fp32/analysis/5method_leadlag.json\\nSaved: results/alpha_sweep/c4_a025_s42_fp32/analysis/5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.88}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "2ab4a01f-9831-4b96-be9d-938433acc76b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"==== ================================================================================================\\\\n5-METHOD LEAD-LAG ANALYSIS | alpha=0.25 | seed=42\\\\nData: results/alpha_sweep/c4_a025_s42_fp32\\\\n==== ================================================================================================\\\\nLoaded 11 generations\\\\n\\\\n====================================================================================================\\\\nFORWARD (canary ₆ downstream)\\\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\\\n----------------------------------------------------------------------------------------------------\\\\ntoken_entropy&lt;distinct_1   -0.945    -2  -0.962    -3   0.0022     -1  10.981   0.0942              N/A     N/A     0\\\\ntoken_entropy&lt;distinct_2    0.770     1  -0.883    -3   0.0138   None   9.327   0.0942              N/A     N/A     1\\\\ntoken_entropy&lt;distinct_3    0.921     3   0.774    -1   0.0164      6  13.005   0.0942              N/A     N/A     1\\\\ntoken_entropy&lt;mauve         0.903    -1   0.795    -1   0.0138   None  14.951   0.0942              N/A     N/A     0\\\\nece&lt;distinct_1             -0.942    -2  -0.962    -3   0.0022     -2  10.770   0.0942              N/A     N/A     1\\\\nece&lt;distinct_2              0.782     0  -0.891    -3   0.0138   None   8.953   0.0942              N/A     N/A     1\\\\nece&lt;distinct_3              0.894     2   0.744    -1   0.0216      5  12.440   0.0942              N/A     N/A     1\\\\nece&lt;mauve                   0.894    -1   0.797    -1   0.0138   None  17.913   0.0942              N/A     N/A     1\\\\n\\\\n====================================================================================================\\\\nREVERSE (downstream ₆ canary)\\\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\\\n----------------------------------------------------------------------------------------------------\\\\ndistinct_1&lt;token_entropy   -0.945     2  -0.962     3   0.0022      1   1.068   0.0942              N/A     N/A     0\\\\ndistinct_2&lt;token_entropy    0.770    -1  -0.883     3   0.0138   None   1.095   0.0942              N/A     N/A     1\\\\ndistinct_3&lt;token_entropy    0.921    -3   0.774     1   0.0164     -6   1.167   0.0942              N/A     N/A     1\\\\nmauve&lt;token_entropy         0.903     1   0.795     1   0.0138   None   0.000   0.0942              N/A     N/A     0\\\\ndistinct_1&lt;ece             -0.942     2  -0.962     3   0.0022      2   7.542   0.0942              N/A     N/A     1\\\\ndistinct_2&lt;ece              0.782     0  -0.891     3   0.0138   None   6.558   0.0942              N/A     N/A     1\\\\ndistinct_3&lt;ece              0.894    -2   0.744     1   0.0216     -5   7.490   0.0942              N/A     N/A     1\\\\nmauve&lt;ece                   0.894     1   0.797     1   0.0138   None  15.404   0.0942              N/A     N/A     1\\\\n\\\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\nCONSENSUS (methods agreeing on forward significance)\\\\n====================================================================================================\\\\n  token_entropy&lt;distinct_1  2/5  [naive, diff]\\\\n  token_entropy&lt;distinct_2  1/5  [diff]\\\\n  token_entropy&lt;distinct_3  2/5  [diff, threshold]\\\\n  token_entropy&lt;mauve       2/5  [naive, diff]\\\\n  ece&lt;distinct_1            2/5  [naive, diff]\\\\n  ece&lt;distinct_2            1/5  [diff]\\\\n  ece&lt;distinct_3            2/5  [diff, threshold]\\\\n  ece&lt;mauve                 2/5  [naive, diff]\\\\n\\\\n  Robust pairs (>=3/5 methods): 0/8\\\\n  Perm Granger FDR sig (fwd): 0/8\\\\n\\\\nSaved: results/alpha_sweep/c4_a025_s42_fp32/analysis/5method_leadlag.json\\\\nSaved: results/alpha_sweep/c4_a025_s42_fp32/analysis/5method_summary.txt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.88}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"==== ================================================================================================\\n5-METHOD LEAD-LAG ANALYSIS | alpha=0.25 | seed=42\\nData: results/alpha_sweep/c4_a025_s42_fp32\\n==== ================================================================================================\\nLoaded 11 generations\\n\\n====================================================================================================\\nFORWARD (canary ₆ downstream)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ntoken_entropy&lt;distinct_1   -0.945    -2  -0.962    -3   0.0022     -1  10.981   0.0942              N/A     N/A     0\\ntoken_entropy&lt;distinct_2    0.770     1  -0.883    -3   0.0138   None   9.327   0.0942              N/A     N/A     1\\ntoken_entropy&lt;distinct_3    0.921     3   0.774    -1   0.0164      6  13.005   0.0942              N/A     N/A     1\\ntoken_entropy&lt;mauve         0.903    -1   0.795    -1   0.0138   None  14.951   0.0942              N/A     N/A     0\\nece&lt;distinct_1             -0.942    -2  -0.962    -3   0.0022     -2  10.770   0.0942              N/A     N/A     1\\nece&lt;distinct_2              0.782     0  -0.891    -3   0.0138   None   8.953   0.0942              N/A     N/A     1\\nece&lt;distinct_3              0.894     2   0.744    -1   0.0216      5  12.440   0.0942              N/A     N/A     1\\nece&lt;mauve                   0.894    -1   0.797    -1   0.0138   None  17.913   0.0942              N/A     N/A     1\\n\\n====================================================================================================\\nREVERSE (downstream ₆ canary)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ndistinct_1&lt;token_entropy   -0.945     2  -0.962     3   0.0022      1   1.068   0.0942              N/A     N/A     0\\ndistinct_2&lt;token_entropy    0.770    -1  -0.883     3   0.0138   None   1.095   0.0942              N/A     N/A     1\\ndistinct_3&lt;token_entropy    0.921    -3   0.774     1   0.0164     -6   1.167   0.0942              N/A     N/A     1\\nmauve&lt;token_entropy         0.903     1   0.795     1   0.0138   None   0.000   0.0942              N/A     N/A     0\\ndistinct_1&lt;ece             -0.942     2  -0.962     3   0.0022      2   7.542   0.0942              N/A     N/A     1\\ndistinct_2&lt;ece              0.782     0  -0.891     3   0.0138   None   6.558   0.0942              N/A     N/A     1\\ndistinct_3&lt;ece              0.894    -2   0.744     1   0.0216     -5   7.490   0.0942              N/A     N/A     1\\nmauve&lt;ece                   0.894     1   0.797     1   0.0138   None  15.404   0.0942              N/A     N/A     1\\n\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nCONSENSUS (methods agreeing on forward significance)\\n====================================================================================================\\n  token_entropy&lt;distinct_1  2/5  [naive, diff]\\n  token_entropy&lt;distinct_2  1/5  [diff]\\n  token_entropy&lt;distinct_3  2/5  [diff, threshold]\\n  token_entropy&lt;mauve       2/5  [naive, diff]\\n  ece&lt;distinct_1            2/5  [naive, diff]\\n  ece&lt;distinct_2            1/5  [diff]\\n  ece&lt;distinct_3            2/5  [diff, threshold]\\n  ece&lt;mauve                 2/5  [naive, diff]\\n\\n  Robust pairs (>=3/5 methods): 0/8\\n  Perm Granger FDR sig (fwd): 0/8\\n\\nSaved: results/alpha_sweep/c4_a025_s42_fp32/analysis/5method_leadlag.json\\nSaved: results/alpha_sweep/c4_a025_s42_fp32/analysis/5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.88}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T06:03:23.941Z_

<details><summary>↩ Tool result · `toolu_015vZvi4RDMnoHCANKanVjfG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"==== ================================================================================================\\n5-METHOD LEAD-LAG ANALYSIS | alpha=0.5 | seed=42\\nData: results/alpha_sweep/c4_a050_s42_fp32\\n==== ================================================================================================\\nLoaded 11 generations\\n\\n====================================================================================================\\nFORWARD (canary ₆ downstream)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ntoken_entropy&lt;distinct_1   -0.954    -5   0.973    -1   0.0000   None 157.412   0.0029        *     N/A     N/A     0\\ntoken_entropy&lt;distinct_2    0.946     4   0.993    -1   0.0000   None 398.952   0.0029        *     N/A     N/A     0\\ntoken_entropy&lt;distinct_3    0.981    -1   0.977    -1   0.0000   None 310.192   0.0029        *     N/A     N/A     0\\ntoken_entropy&lt;mauve         0.952    -1   0.946    -1   0.0002   None 136.751   0.0029        *     N/A     N/A     1\\nece&lt;distinct_1             -0.974    -5   0.924    -1   0.0004   None 137.936   0.0029        *     N/A     N/A     1\\nece&lt;distinct_2              0.959     5   0.972    -1   0.0000   None 391.991   0.0029        *     N/A     N/A     1\\nece&lt;distinct_3              0.972     4   0.989    -1   0.0000   None 229.429   0.0029        *     N/A     N/A     1\\nece&lt;mauve                   0.930     5   0.880    -1   0.0017   None 153.783   0.0029        *     N/A     N/A     1\\n\\n====================================================================================================\\nREVERSE (downstream ₆ canary)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ndistinct_1&lt;token_entropy   -0.954     5   0.973     1   0.0000   None  50.390   0.0029        *     N/A     N/A     0\\ndistinct_2&lt;token_entropy    0.946    -4   0.993     1   0.0000   None  67.626   0.0029        *     N/A     N/A     0\\ndistinct_3&lt;token_entropy    0.981     1   0.977     1   0.0000   None  41.681   0.0029        *     N/A     N/A     0\\nmauve&lt;token_entropy         0.952     1   0.946     1   0.0002   None  18.631   0.0029              N/A     N/A     1\\ndistinct_1&lt;ece             -0.974     5   0.924     1   0.0004   None  11.284   0.0029        *     N/A     N/A     1\\ndistinct_2&lt;ece              0.959    -5   0.972     1   0.0000   None  14.518   0.0029        *     N/A     N/A     1\\ndistinct_3&lt;ece              0.972    -4   0.989     1   0.0000   None  13.892   0.0029        *     N/A     N/A     1\\nmauve&lt;ece                   0.930    -5   0.880     1   0.0017   None  11.431   0.0029        *     N/A     N/A     1\\n\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nCONSENSUS (methods agreeing on forward significance)\\n====================================================================================================\\n  token_entropy&lt;distinct_1  3/5  [naive, diff, perm]\\n  token_entropy&lt;distinct_2  2/5  [diff, perm]\\n  token_entropy&lt;distinct_3  3/5  [naive, diff, perm]\\n  token_entropy&lt;mauve       3/5  [naive, diff, perm]\\n  ece&lt;distinct_1            3/5  [naive, diff, perm]\\n  ece&lt;distinct_2            2/5  [diff, perm]\\n  ece&lt;distinct_3            2/5  [diff, perm]\\n  ece&lt;mauve                 2/5  [diff, perm]\\n\\n  Robust pairs (>=3/5 methods): 4/8\\n  Perm Granger FDR sig (fwd): 8/8\\n\\nSaved: results/alpha_sweep/c4_a050_s42_fp32/analysis/5method_leadlag.json\\nSaved: results/alpha_sweep/c4_a050_s42_fp32/analysis/5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.67}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "87c56715-d35b-4001-ad31-cf106cea3bfe",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"==== ================================================================================================\\\\n5-METHOD LEAD-LAG ANALYSIS | alpha=0.5 | seed=42\\\\nData: results/alpha_sweep/c4_a050_s42_fp32\\\\n==== ================================================================================================\\\\nLoaded 11 generations\\\\n\\\\n====================================================================================================\\\\nFORWARD (canary ₆ downstream)\\\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\\\n----------------------------------------------------------------------------------------------------\\\\ntoken_entropy&lt;distinct_1   -0.954    -5   0.973    -1   0.0000   None 157.412   0.0029        *     N/A     N/A     0\\\\ntoken_entropy&lt;distinct_2    0.946     4   0.993    -1   0.0000   None 398.952   0.0029        *     N/A     N/A     0\\\\ntoken_entropy&lt;distinct_3    0.981    -1   0.977    -1   0.0000   None 310.192   0.0029        *     N/A     N/A     0\\\\ntoken_entropy&lt;mauve         0.952    -1   0.946    -1   0.0002   None 136.751   0.0029        *     N/A     N/A     1\\\\nece&lt;distinct_1             -0.974    -5   0.924    -1   0.0004   None 137.936   0.0029        *     N/A     N/A     1\\\\nece&lt;distinct_2              0.959     5   0.972    -1   0.0000   None 391.991   0.0029        *     N/A     N/A     1\\\\nece&lt;distinct_3              0.972     4   0.989    -1   0.0000   None 229.429   0.0029        *     N/A     N/A     1\\\\nece&lt;mauve                   0.930     5   0.880    -1   0.0017   None 153.783   0.0029        *     N/A     N/A     1\\\\n\\\\n====================================================================================================\\\\nREVERSE (downstream ₆ canary)\\\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\\\n----------------------------------------------------------------------------------------------------\\\\ndistinct_1&lt;token_entropy   -0.954     5   0.973     1   0.0000   None  50.390   0.0029        *     N/A     N/A     0\\\\ndistinct_2&lt;token_entropy    0.946    -4   0.993     1   0.0000   None  67.626   0.0029        *     N/A     N/A     0\\\\ndistinct_3&lt;token_entropy    0.981     1   0.977     1   0.0000   None  41.681   0.0029        *     N/A     N/A     0\\\\nmauve&lt;token_entropy         0.952     1   0.946     1   0.0002   None  18.631   0.0029              N/A     N/A     1\\\\ndistinct_1&lt;ece             -0.974     5   0.924     1   0.0004   None  11.284   0.0029        *     N/A     N/A     1\\\\ndistinct_2&lt;ece              0.959    -5   0.972     1   0.0000   None  14.518   0.0029        *     N/A     N/A     1\\\\ndistinct_3&lt;ece              0.972    -4   0.989     1   0.0000   None  13.892   0.0029        *     N/A     N/A     1\\\\nmauve&lt;ece                   0.930    -5   0.880     1   0.0017   None  11.431   0.0029        *     N/A     N/A     1\\\\n\\\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\nCONSENSUS (methods agreeing on forward significance)\\\\n====================================================================================================\\\\n  token_entropy&lt;distinct_1  3/5  [naive, diff, perm]\\\\n  token_entropy&lt;distinct_2  2/5  [diff, perm]\\\\n  token_entropy&lt;distinct_3  3/5  [naive, diff, perm]\\\\n  token_entropy&lt;mauve       3/5  [naive, diff, perm]\\\\n  ece&lt;distinct_1            3/5  [naive, diff, perm]\\\\n  ece&lt;distinct_2            2/5  [diff, perm]\\\\n  ece&lt;distinct_3            2/5  [diff, perm]\\\\n  ece&lt;mauve                 2/5  [diff, perm]\\\\n\\\\n  Robust pairs (>=3/5 methods): 4/8\\\\n  Perm Granger FDR sig (fwd): 8/8\\\\n\\\\nSaved: results/alpha_sweep/c4_a050_s42_fp32/analysis/5method_leadlag.json\\\\nSaved: results/alpha_sweep/c4_a050_s42_fp32/analysis/5method_summary.txt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 7.67}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"==== ================================================================================================\\n5-METHOD LEAD-LAG ANALYSIS | alpha=0.5 | seed=42\\nData: results/alpha_sweep/c4_a050_s42_fp32\\n==== ================================================================================================\\nLoaded 11 generations\\n\\n====================================================================================================\\nFORWARD (canary ₆ downstream)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ntoken_entropy&lt;distinct_1   -0.954    -5   0.973    -1   0.0000   None 157.412   0.0029        *     N/A     N/A     0\\ntoken_entropy&lt;distinct_2    0.946     4   0.993    -1   0.0000   None 398.952   0.0029        *     N/A     N/A     0\\ntoken_entropy&lt;distinct_3    0.981    -1   0.977    -1   0.0000   None 310.192   0.0029        *     N/A     N/A     0\\ntoken_entropy&lt;mauve         0.952    -1   0.946    -1   0.0002   None 136.751   0.0029        *     N/A     N/A     1\\nece&lt;distinct_1             -0.974    -5   0.924    -1   0.0004   None 137.936   0.0029        *     N/A     N/A     1\\nece&lt;distinct_2              0.959     5   0.972    -1   0.0000   None 391.991   0.0029        *     N/A     N/A     1\\nece&lt;distinct_3              0.972     4   0.989    -1   0.0000   None 229.429   0.0029        *     N/A     N/A     1\\nece&lt;mauve                   0.930     5   0.880    -1   0.0017   None 153.783   0.0029        *     N/A     N/A     1\\n\\n====================================================================================================\\nREVERSE (downstream ₆ canary)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ndistinct_1&lt;token_entropy   -0.954     5   0.973     1   0.0000   None  50.390   0.0029        *     N/A     N/A     0\\ndistinct_2&lt;token_entropy    0.946    -4   0.993     1   0.0000   None  67.626   0.0029        *     N/A     N/A     0\\ndistinct_3&lt;token_entropy    0.981     1   0.977     1   0.0000   None  41.681   0.0029        *     N/A     N/A     0\\nmauve&lt;token_entropy         0.952     1   0.946     1   0.0002   None  18.631   0.0029              N/A     N/A     1\\ndistinct_1&lt;ece             -0.974     5   0.924     1   0.0004   None  11.284   0.0029        *     N/A     N/A     1\\ndistinct_2&lt;ece              0.959    -5   0.972     1   0.0000   None  14.518   0.0029        *     N/A     N/A     1\\ndistinct_3&lt;ece              0.972    -4   0.989     1   0.0000   None  13.892   0.0029        *     N/A     N/A     1\\nmauve&lt;ece                   0.930    -5   0.880     1   0.0017   None  11.431   0.0029        *     N/A     N/A     1\\n\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nCONSENSUS (methods agreeing on forward significance)\\n====================================================================================================\\n  token_entropy&lt;distinct_1  3/5  [naive, diff, perm]\\n  token_entropy&lt;distinct_2  2/5  [diff, perm]\\n  token_entropy&lt;distinct_3  3/5  [naive, diff, perm]\\n  token_entropy&lt;mauve       3/5  [naive, diff, perm]\\n  ece&lt;distinct_1            3/5  [naive, diff, perm]\\n  ece&lt;distinct_2            2/5  [diff, perm]\\n  ece&lt;distinct_3            2/5  [diff, perm]\\n  ece&lt;mauve                 2/5  [diff, perm]\\n\\n  Robust pairs (>=3/5 methods): 4/8\\n  Perm Granger FDR sig (fwd): 8/8\\n\\nSaved: results/alpha_sweep/c4_a050_s42_fp32/analysis/5method_leadlag.json\\nSaved: results/alpha_sweep/c4_a050_s42_fp32/analysis/5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.67}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T06:03:28.304Z_

<details><summary>↩ Tool result · `toolu_017QLp2L9NPEkpX6JiSPZkHL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"==== ================================================================================================\\n5-METHOD LEAD-LAG ANALYSIS | alpha=0.75 | seed=42\\nData: results/alpha_sweep/c4_a075_s42_fp32\\n==== ================================================================================================\\nLoaded 11 generations\\n\\n====================================================================================================\\nFORWARD (canary ₆ downstream)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ntoken_entropy&lt;distinct_1    0.973    -1   0.996    -1   0.0000   None 772.556   0.0032        *     N/A     N/A     1\\ntoken_entropy&lt;distinct_2    0.995    -1   0.992    -2   0.0000   None 701.574   0.0032        *     N/A     N/A     1\\ntoken_entropy&lt;distinct_3    0.998    -2   0.993    -2   0.0000   None 289.720   0.0032        *     N/A     N/A     1\\ntoken_entropy&lt;mauve         0.962    -1   0.944    -1   0.0001   None 239.436   0.0032        *     N/A     N/A     1\\nece&lt;distinct_1             -0.882    -5   0.992    -1   0.0000   None 858.497   0.0032        *     N/A     N/A     0\\nece&lt;distinct_2              0.949    -1   0.997    -1   0.0000   None 1390.379   0.0032        *     N/A     N/A     0\\nece&lt;distinct_3              0.987    -1   0.992    -2   0.0000   None 561.722   0.0032        *     N/A     N/A     0\\nece&lt;mauve                   0.851    -1   0.908    -1   0.0007   None 300.350   0.0032        *     N/A     N/A     1\\n\\n====================================================================================================\\nREVERSE (downstream ₆ canary)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ndistinct_1&lt;token_entropy    0.973     1   0.996     1   0.0000   None   0.346   0.0032              N/A     N/A     1\\ndistinct_2&lt;token_entropy    0.995     1   0.992     2   0.0000   None   0.326   0.0032              N/A     N/A     1\\ndistinct_3&lt;token_entropy    0.998     2   0.993     2   0.0000   None   0.269   0.0032              N/A     N/A     1\\nmauve&lt;token_entropy         0.962     1   0.944     1   0.0001   None   0.702   0.0032              N/A     N/A     1\\ndistinct_1&lt;ece             -0.882     5   0.992     1   0.0000   None   0.161   0.0032              N/A     N/A     0\\ndistinct_2&lt;ece              0.949     1   0.997     1   0.0000   None   0.064   0.0032              N/A     N/A     0\\ndistinct_3&lt;ece              0.987     1   0.992     2   0.0000   None   0.018   0.0032              N/A     N/A     0\\nmauve&lt;ece                   0.851     1   0.908     1   0.0007   None   0.061   0.0032              N/A     N/A     1\\n\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nCONSENSUS (methods agreeing on forward significance)\\n====================================================================================================\\n  token_entropy&lt;distinct_1  3/5  [naive, diff, perm]\\n  token_entropy&lt;distinct_2  3/5  [naive, diff, perm]\\n  token_entropy&lt;distinct_3  3/5  [naive, diff, perm]\\n  token_entropy&lt;mauve       3/5  [naive, diff, perm]\\n  ece&lt;distinct_1            3/5  [naive, diff, perm]\\n  ece&lt;distinct_2            3/5  [naive, diff, perm]\\n  ece&lt;distinct_3            3/5  [naive, diff, perm]\\n  ece&lt;mauve                 3/5  [naive, diff, perm]\\n\\n  Robust pairs (>=3/5 methods): 8/8\\n  Perm Granger FDR sig (fwd): 8/8\\n\\nSaved: results/alpha_sweep/c4_a075_s42_fp32/analysis/5method_leadlag.json\\nSaved: results/alpha_sweep/c4_a075_s42_fp32/analysis/5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "3b5c22cf-09e3-4312-bd6c-e6577094086d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"==== ================================================================================================\\\\n5-METHOD LEAD-LAG ANALYSIS | alpha=0.75 | seed=42\\\\nData: results/alpha_sweep/c4_a075_s42_fp32\\\\n==== ================================================================================================\\\\nLoaded 11 generations\\\\n\\\\n====================================================================================================\\\\nFORWARD (canary ₆ downstream)\\\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\\\n----------------------------------------------------------------------------------------------------\\\\ntoken_entropy&lt;distinct_1    0.973    -1   0.996    -1   0.0000   None 772.556   0.0032        *     N/A     N/A     1\\\\ntoken_entropy&lt;distinct_2    0.995    -1   0.992    -2   0.0000   None 701.574   0.0032        *     N/A     N/A     1\\\\ntoken_entropy&lt;distinct_3    0.998    -2   0.993    -2   0.0000   None 289.720   0.0032        *     N/A     N/A     1\\\\ntoken_entropy&lt;mauve         0.962    -1   0.944    -1   0.0001   None 239.436   0.0032        *     N/A     N/A     1\\\\nece&lt;distinct_1             -0.882    -5   0.992    -1   0.0000   None 858.497   0.0032        *     N/A     N/A     0\\\\nece&lt;distinct_2              0.949    -1   0.997    -1   0.0000   None 1390.379   0.0032        *     N/A     N/A     0\\\\nece&lt;distinct_3              0.987    -1   0.992    -2   0.0000   None 561.722   0.0032        *     N/A     N/A     0\\\\nece&lt;mauve                   0.851    -1   0.908    -1   0.0007   None 300.350   0.0032        *     N/A     N/A     1\\\\n\\\\n====================================================================================================\\\\nREVERSE (downstream ₆ canary)\\\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\\\n----------------------------------------------------------------------------------------------------\\\\ndistinct_1&lt;token_entropy    0.973     1   0.996     1   0.0000   None   0.346   0.0032              N/A     N/A     1\\\\ndistinct_2&lt;token_entropy    0.995     1   0.992     2   0.0000   None   0.326   0.0032              N/A     N/A     1\\\\ndistinct_3&lt;token_entropy    0.998     2   0.993     2   0.0000   None   0.269   0.0032              N/A     N/A     1\\\\nmauve&lt;token_entropy         0.962     1   0.944     1   0.0001   None   0.702   0.0032              N/A     N/A     1\\\\ndistinct_1&lt;ece             -0.882     5   0.992     1   0.0000   None   0.161   0.0032              N/A     N/A     0\\\\ndistinct_2&lt;ece              0.949     1   0.997     1   0.0000   None   0.064   0.0032              N/A     N/A     0\\\\ndistinct_3&lt;ece              0.987     1   0.992     2   0.0000   None   0.018   0.0032              N/A     N/A     0\\\\nmauve&lt;ece                   0.851     1   0.908     1   0.0007   None   0.061   0.0032              N/A     N/A     1\\\\n\\\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\nCONSENSUS (methods agreeing on forward significance)\\\\n====================================================================================================\\\\n  token_entropy&lt;distinct_1  3/5  [naive, diff, perm]\\\\n  token_entropy&lt;distinct_2  3/5  [naive, diff, perm]\\\\n  token_entropy&lt;distinct_3  3/5  [naive, diff, perm]\\\\n  token_entropy&lt;mauve       3/5  [naive, diff, perm]\\\\n  ece&lt;distinct_1            3/5  [naive, diff, perm]\\\\n  ece&lt;distinct_2            3/5  [naive, diff, perm]\\\\n  ece&lt;distinct_3            3/5  [naive, diff, perm]\\\\n  ece&lt;mauve                 3/5  [naive, diff, perm]\\\\n\\\\n  Robust pairs (>=3/5 methods): 8/8\\\\n  Perm Granger FDR sig (fwd): 8/8\\\\n\\\\nSaved: results/alpha_sweep/c4_a075_s42_fp32/analysis/5method_leadlag.json\\\\nSaved: results/alpha_sweep/c4_a075_s42_fp32/analysis/5method_summary.txt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"==== ================================================================================================\\n5-METHOD LEAD-LAG ANALYSIS | alpha=0.75 | seed=42\\nData: results/alpha_sweep/c4_a075_s42_fp32\\n==== ================================================================================================\\nLoaded 11 generations\\n\\n====================================================================================================\\nFORWARD (canary ₆ downstream)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ntoken_entropy&lt;distinct_1    0.973    -1   0.996    -1   0.0000   None 772.556   0.0032        *     N/A     N/A     1\\ntoken_entropy&lt;distinct_2    0.995    -1   0.992    -2   0.0000   None 701.574   0.0032        *     N/A     N/A     1\\ntoken_entropy&lt;distinct_3    0.998    -2   0.993    -2   0.0000   None 289.720   0.0032        *     N/A     N/A     1\\ntoken_entropy&lt;mauve         0.962    -1   0.944    -1   0.0001   None 239.436   0.0032        *     N/A     N/A     1\\nece&lt;distinct_1             -0.882    -5   0.992    -1   0.0000   None 858.497   0.0032        *     N/A     N/A     0\\nece&lt;distinct_2              0.949    -1   0.997    -1   0.0000   None 1390.379   0.0032        *     N/A     N/A     0\\nece&lt;distinct_3              0.987    -1   0.992    -2   0.0000   None 561.722   0.0032        *     N/A     N/A     0\\nece&lt;mauve                   0.851    -1   0.908    -1   0.0007   None 300.350   0.0032        *     N/A     N/A     1\\n\\n====================================================================================================\\nREVERSE (downstream ₆ canary)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ndistinct_1&lt;token_entropy    0.973     1   0.996     1   0.0000   None   0.346   0.0032              N/A     N/A     1\\ndistinct_2&lt;token_entropy    0.995     1   0.992     2   0.0000   None   0.326   0.0032              N/A     N/A     1\\ndistinct_3&lt;token_entropy    0.998     2   0.993     2   0.0000   None   0.269   0.0032              N/A     N/A     1\\nmauve&lt;token_entropy         0.962     1   0.944     1   0.0001   None   0.702   0.0032              N/A     N/A     1\\ndistinct_1&lt;ece             -0.882     5   0.992     1   0.0000   None   0.161   0.0032              N/A     N/A     0\\ndistinct_2&lt;ece              0.949     1   0.997     1   0.0000   None   0.064   0.0032              N/A     N/A     0\\ndistinct_3&lt;ece              0.987     1   0.992     2   0.0000   None   0.018   0.0032              N/A     N/A     0\\nmauve&lt;ece                   0.851     1   0.908     1   0.0007   None   0.061   0.0032              N/A     N/A     1\\n\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nCONSENSUS (methods agreeing on forward significance)\\n====================================================================================================\\n  token_entropy&lt;distinct_1  3/5  [naive, diff, perm]\\n  token_entropy&lt;distinct_2  3/5  [naive, diff, perm]\\n  token_entropy&lt;distinct_3  3/5  [naive, diff, perm]\\n  token_entropy&lt;mauve       3/5  [naive, diff, perm]\\n  ece&lt;distinct_1            3/5  [naive, diff, perm]\\n  ece&lt;distinct_2            3/5  [naive, diff, perm]\\n  ece&lt;distinct_3            3/5  [naive, diff, perm]\\n  ece&lt;mauve                 3/5  [naive, diff, perm]\\n\\n  Robust pairs (>=3/5 methods): 8/8\\n  Perm Granger FDR sig (fwd): 8/8\\n\\nSaved: results/alpha_sweep/c4_a075_s42_fp32/analysis/5method_leadlag.json\\nSaved: results/alpha_sweep/c4_a075_s42_fp32/analysis/5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.34}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T06:03:32.950Z_

<details><summary>↩ Tool result · `toolu_01VqnLi5GT9wYjujewj6XwcR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"==== ================================================================================================\\n5-METHOD LEAD-LAG ANALYSIS | alpha=1.0 | seed=42\\nData: results/padding_robustness/a100_s42_fp32\\n==== ================================================================================================\\nLoaded 11 generations\\n\\n====================================================================================================\\nFORWARD (canary ₆ downstream)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ntoken_entropy&lt;distinct_1    0.992    -1   0.989    -1   0.0000   None 461.551   0.5187        *     N/A     N/A     1\\ntoken_entropy&lt;distinct_2    0.998    -1   0.994    -1   0.0000   None 480.014   0.5187        *     N/A     N/A     1\\ntoken_entropy&lt;distinct_3    0.999    -2   0.995    -2   0.0000   None 511.408   0.5187        *     N/A     N/A     1\\ntoken_entropy&lt;mauve        -0.436    -4   0.707    -5   0.2081   None   0.895   0.5187              N/A     N/A     0\\nece&lt;distinct_1              0.954    -2   0.946    -2   0.0005   None 698.672   0.5187        *     N/A     N/A     1\\nece&lt;distinct_2              0.992    -3   0.966    -1   0.0000   None 1024.529   0.5187        *     N/A     N/A     1\\nece&lt;distinct_3              0.997    -3   0.986    -1   0.0000   None 1671.380   0.5187        *     N/A     N/A     1\\nece&lt;mauve                  -0.432    -4   0.625    -5   0.2594   None   0.496   0.5187              N/A     N/A     0\\n\\n====================================================================================================\\nREVERSE (downstream ₆ canary)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ndistinct_1&lt;token_entropy    0.992     1   0.989     1   0.0000   None   0.001   0.5187              N/A     N/A     1\\ndistinct_2&lt;token_entropy    0.998     1   0.994     1   0.0000   None   0.004   0.5187              N/A     N/A     1\\ndistinct_3&lt;token_entropy    0.999     2   0.995     2   0.0000   None   0.006   0.5187              N/A     N/A     1\\nmauve&lt;token_entropy        -0.436     4   0.707     5   0.2081   None   1.635   0.5187              N/A     N/A     0\\ndistinct_1&lt;ece              0.954     2   0.946     2   0.0005   None  12.774   0.5187              N/A     N/A     1\\ndistinct_2&lt;ece              0.992     3   0.966     1   0.0000   None  11.502   0.5187              N/A     N/A     1\\ndistinct_3&lt;ece              0.997     3   0.986     1   0.0000   None  10.017   0.5187              N/A     N/A     1\\nmauve&lt;ece                  -0.432     4   0.625     5   0.2594   None   0.271   0.5187              N/A     N/A     0\\n\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nCONSENSUS (methods agreeing on forward significance)\\n====================================================================================================\\n  token_entropy&lt;distinct_1  3/5  [naive, diff, perm]\\n  token_entropy&lt;distinct_2  3/5  [naive, diff, perm]\\n  token_entropy&lt;distinct_3  3/5  [naive, diff, perm]\\n  token_entropy&lt;mauve       0/5  [none]\\n  ece&lt;distinct_1            3/5  [naive, diff, perm]\\n  ece&lt;distinct_2            3/5  [naive, diff, perm]\\n  ece&lt;distinct_3            3/5  [naive, diff, perm]\\n  ece&lt;mauve                 0/5  [none]\\n\\n  Robust pairs (>=3/5 methods): 6/8\\n  Perm Granger FDR sig (fwd): 6/8\\n\\nSaved: results/padding_robustness/a100_s42_fp32/analysis/5method_leadlag.json\\nSaved: results/padding_robustness/a100_s42_fp32/analysis/5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.62}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "98a9c691-6546-4628-809e-bc487c6cff25",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"==== ================================================================================================\\\\n5-METHOD LEAD-LAG ANALYSIS | alpha=1.0 | seed=42\\\\nData: results/padding_robustness/a100_s42_fp32\\\\n==== ================================================================================================\\\\nLoaded 11 generations\\\\n\\\\n====================================================================================================\\\\nFORWARD (canary ₆ downstream)\\\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\\\n----------------------------------------------------------------------------------------------------\\\\ntoken_entropy&lt;distinct_1    0.992    -1   0.989    -1   0.0000   None 461.551   0.5187        *     N/A     N/A     1\\\\ntoken_entropy&lt;distinct_2    0.998    -1   0.994    -1   0.0000   None 480.014   0.5187        *     N/A     N/A     1\\\\ntoken_entropy&lt;distinct_3    0.999    -2   0.995    -2   0.0000   None 511.408   0.5187        *     N/A     N/A     1\\\\ntoken_entropy&lt;mauve        -0.436    -4   0.707    -5   0.2081   None   0.895   0.5187              N/A     N/A     0\\\\nece&lt;distinct_1              0.954    -2   0.946    -2   0.0005   None 698.672   0.5187        *     N/A     N/A     1\\\\nece&lt;distinct_2              0.992    -3   0.966    -1   0.0000   None 1024.529   0.5187        *     N/A     N/A     1\\\\nece&lt;distinct_3              0.997    -3   0.986    -1   0.0000   None 1671.380   0.5187        *     N/A     N/A     1\\\\nece&lt;mauve                  -0.432    -4   0.625    -5   0.2594   None   0.496   0.5187              N/A     N/A     0\\\\n\\\\n====================================================================================================\\\\nREVERSE (downstream ₆ canary)\\\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\\\n----------------------------------------------------------------------------------------------------\\\\ndistinct_1&lt;token_entropy    0.992     1   0.989     1   0.0000   None   0.001   0.5187              N/A     N/A     1\\\\ndistinct_2&lt;token_entropy    0.998     1   0.994     1   0.0000   None   0.004   0.5187              N/A     N/A     1\\\\ndistinct_3&lt;token_entropy    0.999     2   0.995     2   0.0000   None   0.006   0.5187              N/A     N/A     1\\\\nmauve&lt;token_entropy        -0.436     4   0.707     5   0.2081   None   1.635   0.5187              N/A     N/A     0\\\\ndistinct_1&lt;ece              0.954     2   0.946     2   0.0005   None  12.774   0.5187              N/A     N/A     1\\\\ndistinct_2&lt;ece              0.992     3   0.966     1   0.0000   None  11.502   0.5187              N/A     N/A     1\\\\ndistinct_3&lt;ece              0.997     3   0.986     1   0.0000   None  10.017   0.5187              N/A     N/A     1\\\\nmauve&lt;ece                  -0.432     4   0.625     5   0.2594   None   0.271   0.5187              N/A     N/A     0\\\\n\\\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\nCONSENSUS (methods agreeing on forward significance)\\\\n====================================================================================================\\\\n  token_entropy&lt;distinct_1  3/5  [naive, diff, perm]\\\\n  token_entropy&lt;distinct_2  3/5  [naive, diff, perm]\\\\n  token_entropy&lt;distinct_3  3/5  [naive, diff, perm]\\\\n  token_entropy&lt;mauve       0/5  [none]\\\\n  ece&lt;distinct_1            3/5  [naive, diff, perm]\\\\n  ece&lt;distinct_2            3/5  [naive, diff, perm]\\\\n  ece&lt;distinct_3            3/5  [naive, diff, perm]\\\\n  ece&lt;mauve                 0/5  [none]\\\\n\\\\n  Robust pairs (>=3/5 methods): 6/8\\\\n  Perm Granger FDR sig (fwd): 6/8\\\\n\\\\nSaved: results/padding_robustness/a100_s42_fp32/analysis/5method_leadlag.json\\\\nSaved: results/padding_robustness/a100_s42_fp32/analysis/5method_summary.txt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.62}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"==== ================================================================================================\\n5-METHOD LEAD-LAG ANALYSIS | alpha=1.0 | seed=42\\nData: results/padding_robustness/a100_s42_fp32\\n==== ================================================================================================\\nLoaded 11 generations\\n\\n====================================================================================================\\nFORWARD (canary ₆ downstream)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ntoken_entropy&lt;distinct_1    0.992    -1   0.989    -1   0.0000   None 461.551   0.5187        *     N/A     N/A     1\\ntoken_entropy&lt;distinct_2    0.998    -1   0.994    -1   0.0000   None 480.014   0.5187        *     N/A     N/A     1\\ntoken_entropy&lt;distinct_3    0.999    -2   0.995    -2   0.0000   None 511.408   0.5187        *     N/A     N/A     1\\ntoken_entropy&lt;mauve        -0.436    -4   0.707    -5   0.2081   None   0.895   0.5187              N/A     N/A     0\\nece&lt;distinct_1              0.954    -2   0.946    -2   0.0005   None 698.672   0.5187        *     N/A     N/A     1\\nece&lt;distinct_2              0.992    -3   0.966    -1   0.0000   None 1024.529   0.5187        *     N/A     N/A     1\\nece&lt;distinct_3              0.997    -3   0.986    -1   0.0000   None 1671.380   0.5187        *     N/A     N/A     1\\nece&lt;mauve                  -0.432    -4   0.625    -5   0.2594   None   0.496   0.5187              N/A     N/A     0\\n\\n====================================================================================================\\nREVERSE (downstream ₆ canary)\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nPair                       NaiveR  NLag   DiffR  DLag  DiffFDR  Onset   PermF  PermFDR  PermSig    TY_F    TY_p  dmax\\n----------------------------------------------------------------------------------------------------\\ndistinct_1&lt;token_entropy    0.992     1   0.989     1   0.0000   None   0.001   0.5187              N/A     N/A     1\\ndistinct_2&lt;token_entropy    0.998     1   0.994     1   0.0000   None   0.004   0.5187              N/A     N/A     1\\ndistinct_3&lt;token_entropy    0.999     2   0.995     2   0.0000   None   0.006   0.5187              N/A     N/A     1\\nmauve&lt;token_entropy        -0.436     4   0.707     5   0.2081   None   1.635   0.5187              N/A     N/A     0\\ndistinct_1&lt;ece              0.954     2   0.946     2   0.0005   None  12.774   0.5187              N/A     N/A     1\\ndistinct_2&lt;ece              0.992     3   0.966     1   0.0000   None  11.502   0.5187              N/A     N/A     1\\ndistinct_3&lt;ece              0.997     3   0.986     1   0.0000   None  10.017   0.5187              N/A     N/A     1\\nmauve&lt;ece                  -0.432     4   0.625     5   0.2594   None   0.271   0.5187              N/A     N/A     0\\n\\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\nCONSENSUS (methods agreeing on forward significance)\\n====================================================================================================\\n  token_entropy&lt;distinct_1  3/5  [naive, diff, perm]\\n  token_entropy&lt;distinct_2  3/5  [naive, diff, perm]\\n  token_entropy&lt;distinct_3  3/5  [naive, diff, perm]\\n  token_entropy&lt;mauve       0/5  [none]\\n  ece&lt;distinct_1            3/5  [naive, diff, perm]\\n  ece&lt;distinct_2            3/5  [naive, diff, perm]\\n  ece&lt;distinct_3            3/5  [naive, diff, perm]\\n  ece&lt;mauve                 0/5  [none]\\n\\n  Robust pairs (>=3/5 methods): 6/8\\n  Perm Granger FDR sig (fwd): 6/8\\n\\nSaved: results/padding_robustness/a100_s42_fp32/analysis/5method_leadlag.json\\nSaved: results/padding_robustness/a100_s42_fp32/analysis/5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.62}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
All 4 analyses completed successfully. Let me summarize the results:

### C4 α=0.25 s42 (c4_a025_s42_fp32)
- PermG fwd: 0/8 sig (all PermFDR=0.0942, none marked *)
- PermG rev: 0/8 sig
- K≥3: 0/8
- K≥4: 0/8
- TY: N/A (all dmax=0 or 1, T=11 too short)


- Threshold onset: sparse results with only a few pairs showing onset values (-1, -2, 6, 5 for token_entropy/ece comparisons), while the other configurations show no onset values at all
- The "Onset" column in the output represents threshold_onset_3sigma computed via the D105 true 3σ method, which is exactly what C008 requires for registry updates
- Now I need to examine the JSON output files to extract the structured data and compare against the wiki a100 s42 experiment to validate the results
- Looking at the metrics table, I'm seeing some unexpected results in the c4_a050 reverse permutation tests that need verification, particularly where distinct metrics show significance but mauve doesn't

. For padding at α=1.0, the K≥3 consensus is 6/8 while K≥4 is consistently 0/8 across all pairs. I need to pull the exact threshold values from the registry files to properly compare against the wiki baseline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "35fa43f6-90b0-4514-a03b-c26069a19326",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvKiLCXbeJkrwhYNm36ufe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10210,
      "cache_read_input_tokens": 30327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10210
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

全部 4 个分析完成。读取 JSON 结果获取精确数值，同时查询 registry 中 wiki α=1.0 实验用于 padding 对比。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "b55addfa-398b-49bf-91ea-6b4d5879b9cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvKiLCXbeJkrwhYNm36ufe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10210,
      "cache_read_input_tokens": 30327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10210
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01K1i9yw95pmobaFQbfu2tVZ`</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a025_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "5c07e07a-f10a-483a-9ccb-8e50b4dda2be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvKiLCXbeJkrwhYNm36ufe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10210,
      "cache_read_input_tokens": 30327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10210
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016NLo24VXDKuTLwwHibqLFd`</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "e4482a04-46c9-4738-afd2-6db8af3c3d94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvKiLCXbeJkrwhYNm36ufe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10210,
      "cache_read_input_tokens": 30327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10210
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Kgq2A2PRJKqY2UmaZQTjcU`</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "9ef9a7d6-9649-41ba-892e-a007256df8ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvKiLCXbeJkrwhYNm36ufe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10210,
      "cache_read_input_tokens": 30327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10210
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VUkNsborA9nnW3tmhhW6XN`</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/padding_robustness/a100_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "93f86893-eafe-4200-88dd-a8317e10d70b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvKiLCXbeJkrwhYNm36ufe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10210,
      "cache_read_input_tokens": 30327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10210
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

_source line 42 · 2026-05-20T06:04:05.314Z_

<details><summary>↩ Tool result · `toolu_01K1i9yw95pmobaFQbfu2tVZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 0.25,\\n    \\\"seed\\\": 42,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"results/alpha_sweep/c4_a025_s42_fp32\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -2,\\n          \\\"r\\\": -0.9445,\\n          \\\"p_value\\\": 0.000125,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.6061,\\n              \\\"p\\\": 0.202159\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.3688,\\n              \\\"p\\\": 0.415638\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": -0.8964,\\n              \\\"p\\\": 0.00257\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": -0.9445,\\n              \\\"p\\\": 0.000125\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.2197,\\n              \\\"p\\\": 0.541961\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.4647,\\n              \\\"p\\\": 0.149807\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.4843,\\n              \\\"p\\\": 0.156012\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.41,\\n              \\\"p\\\": 0.273075\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.4233,\\n              \\\"p\\\": 0.296083\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.3993,\\n              \\\"p\\\": 0.374825\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.4462,\\n              \\\"p\\\": 0.375117\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": -3,\\n          \\\"r\\\": -0.9616,\\n          \\\"p_value\\\": 0.000543,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": -0.3981,\\n              \\\"p\\\": 0.506796\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.8342,\\n              \\\"p\\\": 0.038944\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": -0.9616,\\n              \\\"p\\\": 0.000543\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": -0.6871,\\n              \\\"p\\\": 0.059753\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.7393,\\n              \\\"p\\\": 0.022817\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.2348,\\n              \\\"p\\\": 0.513826\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.2771,\\n              \\\"p\\\": 0.470418\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.0156,\\n              \\\"p\\\": 0.970844\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.4948,\\n              \\\"p\\\": 0.25891\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.0841,\\n              \\\"p\\\": 0.87419\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.3449,\\n              \\\"p\\\": 0.569708\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.002184,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": 3,\\n          \\\"downstream_onset\\\": 2,\\n          \\\"lead_time\\\": -1,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 10.9809,\\n          \\\"p_value\\\": 0.093381,\\n          \\\"significant\\\": false,\\n          \\\"p_fdr\\\": 0.094181,\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_gra\\n\\n... [截断: 输出过长，省略 53454 字符] ...\\n\\n2\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.4001,\\n              \\\"p\\\": 0.285932\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.0477,\\n              \\\"p\\\": 0.910605\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.7337,\\n              \\\"p\\\": 0.060518\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.2275,\\n              \\\"p\\\": 0.664574\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": 1,\\n          \\\"r\\\": 0.797,\\n          \\\"p_value\\\": 0.010113,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.0297,\\n              \\\"p\\\": 0.962223\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.3246,\\n              \\\"p\\\": 0.530169\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.0885,\\n              \\\"p\\\": 0.85036\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.0373,\\n              \\\"p\\\": 0.930147\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.0573,\\n              \\\"p\\\": 0.883574\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.2347,\\n              \\\"p\\\": 0.514029\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.797,\\n              \\\"p\\\": 0.010113\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.1589,\\n              \\\"p\\\": 0.70698\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": -0.4446,\\n              \\\"p\\\": 0.317515\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.4444,\\n              \\\"p\\\": 0.377334\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.1613,\\n              \\\"p\\\": 0.795471\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.013805,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": null,\\n          \\\"downstream_onset\\\": 4,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 15.4036,\\n          \\\"p_value\\\": 0.028394,\\n          \\\"significant\\\": true,\\n          \\\"p_fdr\\\": 0.227152,\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n          \\\"f_stat\\\": null,\\n          \\\"p_value\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"error\\\": \\\"VARResults.test_causality() got an unexpected keyword argument 'signonly'\\\",\\n          \\\"order\\\": 3,\\n          \\\"k_opt\\\": 2,\\n          \\\"d_max\\\": 1\\n        }\\n      }\\n    }\\n  ],\\n  \\\"consensus\\\": [\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_1\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_2\\\",\\n      \\\"votes\\\": 1,\\n      \\\"methods\\\": [\\n        \\\"diff\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_3\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"threshold\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<mauve\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_1\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_2\\\",\\n      \\\"votes\\\": 1,\\n      \\\"methods\\\": [\\n        \\\"diff\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_3\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"threshold\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<mauve\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\"\\n      ]\\n    }\\n  ],\\n  \\\"summary\\\": {\\n    \\\"perm_granger_fdr_forward_sig\\\": 0,\\n    \\\"perm_granger_fdr_reverse_sig\\\": 0,\\n    \\\"diff_xcorr_fdr_forward_sig\\\": 8,\\n    \\\"diff_xcorr_fdr_reverse_sig\\\": 8,\\n    \\\"threshold_forward_sig\\\": 2,\\n    \\\"ty_forward_sig\\\": 0,\\n    \\\"robust_pairs\\\": 0\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.18}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "b5e0bb84-d8c8-4024-9b24-9f538b4e4a16",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"meta\\\\\\\": {\\\\n    \\\\\\\"alpha\\\\\\\": 0.25,\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"n_gens\\\\\\\": 11,\\\\n    \\\\\\\"data_dir\\\\\\\": \\\\\\\"results/alpha_sweep/c4_a025_s42_fp32\\\\\\\",\\\\n    \\\\\\\"methods\\\\\\\": [\\\\n      \\\\\\\"naive_xcorr\\\\\\\",\\\\n      \\\\\\\"diff_xcorr\\\\\\\",\\\\n      \\\\\\\"threshold_onset\\\\\\\",\\\\n      \\\\\\\"perm_granger\\\\\\\",\\\\n      \\\\\\\"ty_granger\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"n_perm\\\\\\\": 5000,\\\\n    \\\\\\\"canaries\\\\\\\": [\\\\n      \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"ece\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"downstreams\\\\\\\": [\\\\n      \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"distinct_3\\\\\\\",\\\\n      \\\\\\\"mauve\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"threshold_criterion\\\\\\\": \\\\\\\"true_3sigma_d105\\\\\\\"\\\\n  },\\\\n  \\\\\\\"pairs\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"forward\\\\\\\": {\\\\n        \\\\\\\"naive_xcorr\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"naive_xcorr\\\\\\\",\\\\n          \\\\\\\"peak_lag\\\\\\\": -2,\\\\n          \\\\\\\"r\\\\\\\": -0.9445,\\\\n          \\\\\\\"p_value\\\\\\\": 0.000125,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"all_lags\\\\\\\": [\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -5,\\\\n              \\\\\\\"r\\\\\\\": 0.6061,\\\\n              \\\\\\\"p\\\\\\\": 0.202159\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -4,\\\\n              \\\\\\\"r\\\\\\\": -0.3688,\\\\n              \\\\\\\"p\\\\\\\": 0.415638\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -3,\\\\n              \\\\\\\"r\\\\\\\": -0.8964,\\\\n              \\\\\\\"p\\\\\\\": 0.00257\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -2,\\\\n              \\\\\\\"r\\\\\\\": -0.9445,\\\\n              \\\\\\\"p\\\\\\\": 0.000125\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -1,\\\\n              \\\\\\\"r\\\\\\\": 0.2197,\\\\n              \\\\\\\"p\\\\\\\": 0.541961\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 0,\\\\n              \\\\\\\"r\\\\\\\": 0.4647,\\\\n              \\\\\\\"p\\\\\\\": 0.149807\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 1,\\\\n              \\\\\\\"r\\\\\\\": 0.4843,\\\\n              \\\\\\\"p\\\\\\\": 0.156012\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": 0.41,\\\\n              \\\\\\\"p\\\\\\\": 0.273075\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": 0.4233,\\\\n              \\\\\\\"p\\\\\\\": 0.296083\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": 0.3993,\\\\n              \\\\\\\"p\\\\\\\": 0.374825\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": 0.4462,\\\\n              \\\\\\\"p\\\\\\\": 0.375117\\\\n            }\\\\n          ]\\\\n        },\\\\n        \\\\\\\"diff_xcorr\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"diff_xcorr\\\\\\\",\\\\n          \\\\\\\"peak_lag\\\\\\\": -3,\\\\n          \\\\\\\"r\\\\\\\": -0.9616,\\\\n          \\\\\\\"p_value\\\\\\\": 0.000543,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"all_lags\\\\\\\": [\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -5,\\\\n              \\\\\\\"r\\\\\\\": -0.3981,\\\\n              \\\\\\\"p\\\\\\\": 0.506796\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -4,\\\\n              \\\\\\\"r\\\\\\\": -0.8342,\\\\n              \\\\\\\"p\\\\\\\": 0.038944\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -3,\\\\n              \\\\\\\"r\\\\\\\": -0.9616,\\\\n              \\\\\\\"p\\\\\\\": 0.000543\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -2,\\\\n              \\\\\\\"r\\\\\\\": -0.6871,\\\\n              \\\\\\\"p\\\\\\\": 0.059753\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -1,\\\\n              \\\\\\\"r\\\\\\\": 0.7393,\\\\n              \\\\\\\"p\\\\\\\": 0.022817\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 0,\\\\n              \\\\\\\"r\\\\\\\": 0.2348,\\\\n              \\\\\\\"p\\\\\\\": 0.513826\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 1,\\\\n              \\\\\\\"r\\\\\\\": 0.2771,\\\\n              \\\\\\\"p\\\\\\\": 0.470418\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": 0.0156,\\\\n              \\\\\\\"p\\\\\\\": 0.970844\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": 0.4948,\\\\n              \\\\\\\"p\\\\\\\": 0.25891\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": 0.0841,\\\\n              \\\\\\\"p\\\\\\\": 0.87419\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": 0.3449,\\\\n              \\\\\\\"p\\\\\\\": 0.569708\\\\n            }\\\\n          ],\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.002184,\\\\n          \\\\\\\"significant_fdr\\\\\\\": true\\\\n        },\\\\n        \\\\\\\"threshold_onset\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"threshold_onset\\\\\\\",\\\\n          \\\\\\\"canary_onset\\\\\\\": 3,\\\\n          \\\\\\\"downstream_onset\\\\\\\": 2,\\\\n          \\\\\\\"lead_time\\\\\\\": -1,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"threshold\\\\\\\": \\\\\\\"true_3sigma_d105\\\\\\\"\\\\n        },\\\\n        \\\\\\\"perm_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"perm_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": 10.9809,\\\\n          \\\\\\\"p_value\\\\\\\": 0.093381,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.094181,\\\\n          \\\\\\\"significant_fdr\\\\\\\": false\\\\n        },\\\\n        \\\\\\\"ty_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"ty_gra\\\\n\\\\n... [截断: 输出过长，省略 53454 字符] ...\\\\n\\\\n2\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": 0.4001,\\\\n              \\\\\\\"p\\\\\\\": 0.285932\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": 0.0477,\\\\n              \\\\\\\"p\\\\\\\": 0.910605\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": 0.7337,\\\\n              \\\\\\\"p\\\\\\\": 0.060518\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": 0.2275,\\\\n              \\\\\\\"p\\\\\\\": 0.664574\\\\n            }\\\\n          ]\\\\n        },\\\\n        \\\\\\\"diff_xcorr\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"diff_xcorr\\\\\\\",\\\\n          \\\\\\\"peak_lag\\\\\\\": 1,\\\\n          \\\\\\\"r\\\\\\\": 0.797,\\\\n          \\\\\\\"p_value\\\\\\\": 0.010113,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"all_lags\\\\\\\": [\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -5,\\\\n              \\\\\\\"r\\\\\\\": 0.0297,\\\\n              \\\\\\\"p\\\\\\\": 0.962223\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -4,\\\\n              \\\\\\\"r\\\\\\\": 0.3246,\\\\n              \\\\\\\"p\\\\\\\": 0.530169\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -3,\\\\n              \\\\\\\"r\\\\\\\": 0.0885,\\\\n              \\\\\\\"p\\\\\\\": 0.85036\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -2,\\\\n              \\\\\\\"r\\\\\\\": 0.0373,\\\\n              \\\\\\\"p\\\\\\\": 0.930147\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -1,\\\\n              \\\\\\\"r\\\\\\\": 0.0573,\\\\n              \\\\\\\"p\\\\\\\": 0.883574\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 0,\\\\n              \\\\\\\"r\\\\\\\": 0.2347,\\\\n              \\\\\\\"p\\\\\\\": 0.514029\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 1,\\\\n              \\\\\\\"r\\\\\\\": 0.797,\\\\n              \\\\\\\"p\\\\\\\": 0.010113\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": 0.1589,\\\\n              \\\\\\\"p\\\\\\\": 0.70698\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": -0.4446,\\\\n              \\\\\\\"p\\\\\\\": 0.317515\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": 0.4444,\\\\n              \\\\\\\"p\\\\\\\": 0.377334\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": -0.1613,\\\\n              \\\\\\\"p\\\\\\\": 0.795471\\\\n            }\\\\n          ],\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.013805,\\\\n          \\\\\\\"significant_fdr\\\\\\\": true\\\\n        },\\\\n        \\\\\\\"threshold_onset\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"threshold_onset\\\\\\\",\\\\n          \\\\\\\"canary_onset\\\\\\\": null,\\\\n          \\\\\\\"downstream_onset\\\\\\\": 4,\\\\n          \\\\\\\"lead_time\\\\\\\": null,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"threshold\\\\\\\": \\\\\\\"true_3sigma_d105\\\\\\\"\\\\n        },\\\\n        \\\\\\\"perm_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"perm_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": 15.4036,\\\\n          \\\\\\\"p_value\\\\\\\": 0.028394,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.227152,\\\\n          \\\\\\\"significant_fdr\\\\\\\": false\\\\n        },\\\\n        \\\\\\\"ty_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"ty_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": null,\\\\n          \\\\\\\"p_value\\\\\\\": null,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"error\\\\\\\": \\\\\\\"VARResults.test_causality() got an unexpected keyword argument 'signonly'\\\\\\\",\\\\n          \\\\\\\"order\\\\\\\": 3,\\\\n          \\\\\\\"k_opt\\\\\\\": 2,\\\\n          \\\\\\\"d_max\\\\\\\": 1\\\\n        }\\\\n      }\\\\n    }\\\\n  ],\\\\n  \\\\\\\"consensus\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<distinct_1\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 2,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<distinct_2\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 1,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"diff\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<distinct_3\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 2,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"threshold\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<mauve\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 2,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<distinct_1\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 2,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<distinct_2\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 1,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"diff\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<distinct_3\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 2,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"threshold\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<mauve\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 2,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\"\\\\n      ]\\\\n    }\\\\n  ],\\\\n  \\\\\\\"summary\\\\\\\": {\\\\n    \\\\\\\"perm_granger_fdr_forward_sig\\\\\\\": 0,\\\\n    \\\\\\\"perm_granger_fdr_reverse_sig\\\\\\\": 0,\\\\n    \\\\\\\"diff_xcorr_fdr_forward_sig\\\\\\\": 8,\\\\n    \\\\\\\"diff_xcorr_fdr_reverse_sig\\\\\\\": 8,\\\\n    \\\\\\\"threshold_forward_sig\\\\\\\": 2,\\\\n    \\\\\\\"ty_forward_sig\\\\\\\": 0,\\\\n    \\\\\\\"robust_pairs\\\\\\\": 0\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.18}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 0.25,\\n    \\\"seed\\\": 42,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"results/alpha_sweep/c4_a025_s42_fp32\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -2,\\n          \\\"r\\\": -0.9445,\\n          \\\"p_value\\\": 0.000125,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.6061,\\n              \\\"p\\\": 0.202159\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.3688,\\n              \\\"p\\\": 0.415638\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": -0.8964,\\n              \\\"p\\\": 0.00257\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": -0.9445,\\n              \\\"p\\\": 0.000125\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.2197,\\n              \\\"p\\\": 0.541961\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.4647,\\n              \\\"p\\\": 0.149807\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.4843,\\n              \\\"p\\\": 0.156012\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.41,\\n              \\\"p\\\": 0.273075\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.4233,\\n              \\\"p\\\": 0.296083\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.3993,\\n              \\\"p\\\": 0.374825\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.4462,\\n              \\\"p\\\": 0.375117\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": -3,\\n          \\\"r\\\": -0.9616,\\n          \\\"p_value\\\": 0.000543,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": -0.3981,\\n              \\\"p\\\": 0.506796\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.8342,\\n              \\\"p\\\": 0.038944\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": -0.9616,\\n              \\\"p\\\": 0.000543\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": -0.6871,\\n              \\\"p\\\": 0.059753\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.7393,\\n              \\\"p\\\": 0.022817\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.2348,\\n              \\\"p\\\": 0.513826\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.2771,\\n              \\\"p\\\": 0.470418\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.0156,\\n              \\\"p\\\": 0.970844\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.4948,\\n              \\\"p\\\": 0.25891\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.0841,\\n              \\\"p\\\": 0.87419\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.3449,\\n              \\\"p\\\": 0.569708\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.002184,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": 3,\\n          \\\"downstream_onset\\\": 2,\\n          \\\"lead_time\\\": -1,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 10.9809,\\n          \\\"p_value\\\": 0.093381,\\n          \\\"significant\\\": false,\\n          \\\"p_fdr\\\": 0.094181,\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_gra\\n\\n... [截断: 输出过长，省略 53454 字符] ...\\n\\n2\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.4001,\\n              \\\"p\\\": 0.285932\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.0477,\\n              \\\"p\\\": 0.910605\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.7337,\\n              \\\"p\\\": 0.060518\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.2275,\\n              \\\"p\\\": 0.664574\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": 1,\\n          \\\"r\\\": 0.797,\\n          \\\"p_value\\\": 0.010113,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.0297,\\n              \\\"p\\\": 0.962223\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.3246,\\n              \\\"p\\\": 0.530169\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.0885,\\n              \\\"p\\\": 0.85036\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.0373,\\n              \\\"p\\\": 0.930147\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.0573,\\n              \\\"p\\\": 0.883574\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.2347,\\n              \\\"p\\\": 0.514029\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.797,\\n              \\\"p\\\": 0.010113\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.1589,\\n              \\\"p\\\": 0.70698\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": -0.4446,\\n              \\\"p\\\": 0.317515\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.4444,\\n              \\\"p\\\": 0.377334\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.1613,\\n              \\\"p\\\": 0.795471\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.013805,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": null,\\n          \\\"downstream_onset\\\": 4,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 15.4036,\\n          \\\"p_value\\\": 0.028394,\\n          \\\"significant\\\": true,\\n          \\\"p_fdr\\\": 0.227152,\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n          \\\"f_stat\\\": null,\\n          \\\"p_value\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"error\\\": \\\"VARResults.test_causality() got an unexpected keyword argument 'signonly'\\\",\\n          \\\"order\\\": 3,\\n          \\\"k_opt\\\": 2,\\n          \\\"d_max\\\": 1\\n        }\\n      }\\n    }\\n  ],\\n  \\\"consensus\\\": [\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_1\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_2\\\",\\n      \\\"votes\\\": 1,\\n      \\\"methods\\\": [\\n        \\\"diff\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_3\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"threshold\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<mauve\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_1\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_2\\\",\\n      \\\"votes\\\": 1,\\n      \\\"methods\\\": [\\n        \\\"diff\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_3\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"threshold\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<mauve\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\"\\n      ]\\n    }\\n  ],\\n  \\\"summary\\\": {\\n    \\\"perm_granger_fdr_forward_sig\\\": 0,\\n    \\\"perm_granger_fdr_reverse_sig\\\": 0,\\n    \\\"diff_xcorr_fdr_forward_sig\\\": 8,\\n    \\\"diff_xcorr_fdr_reverse_sig\\\": 8,\\n    \\\"threshold_forward_sig\\\": 2,\\n    \\\"ty_forward_sig\\\": 0,\\n    \\\"robust_pairs\\\": 0\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.18}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011gzqAMHiMnL2JVDmDx9LFk`</summary>

```json
{
  "filters": {
    "exp_id": "generalize_pythia410m_wiki_a100_s42"
  },
  "project": "distrib_canary_collapse",
  "fields": [
    "*"
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
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "176afe40-cabd-48a5-b71b-5215b8bf765c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvKiLCXbeJkrwhYNm36ufe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10210,
      "cache_read_input_tokens": 30327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10210
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

_source line 44 · 2026-05-20T06:04:08.157Z_

<details><summary>↩ Tool result · `toolu_016NLo24VXDKuTLwwHibqLFd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 0.5,\\n    \\\"seed\\\": 42,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"results/alpha_sweep/c4_a050_s42_fp32\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -5,\\n          \\\"r\\\": -0.9542,\\n          \\\"p_value\\\": 0.003102,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": -0.9542,\\n              \\\"p\\\": 0.003102\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.932,\\n              \\\"p\\\": 0.002232\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": -0.8115,\\n              \\\"p\\\": 0.01447\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": -0.4843,\\n              \\\"p\\\": 0.186443\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.6323,\\n              \\\"p\\\": 0.049809\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.739,\\n              \\\"p\\\": 0.009364\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.791,\\n              \\\"p\\\": 0.006431\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.8178,\\n              \\\"p\\\": 0.007083\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.8355,\\n              \\\"p\\\": 0.009797\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.8924,\\n              \\\"p\\\": 0.006871\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.9165,\\n              \\\"p\\\": 0.010161\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.973,\\n          \\\"p_value\\\": 1e-05,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": -0.7215,\\n              \\\"p\\\": 0.168842\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.6524,\\n              \\\"p\\\": 0.160232\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.5487,\\n              \\\"p\\\": 0.202175\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.8728,\\n              \\\"p\\\": 0.004668\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.973,\\n              \\\"p\\\": 1e-05\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.2365,\\n              \\\"p\\\": 0.510676\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.4434,\\n              \\\"p\\\": 0.231927\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.3332,\\n              \\\"p\\\": 0.41994\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.2007,\\n              \\\"p\\\": 0.666138\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.3459,\\n              \\\"p\\\": 0.501894\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.4361,\\n              \\\"p\\\": 0.46291\\n            }\\n          ],\\n          \\\"p_fdr\\\": 1.9e-05,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": 4,\\n          \\\"downstream_onset\\\": null,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 157.4118,\\n          \\\"p_value\\\": 0.003199,\\n          \\\"significant\\\": true,\\n          \\\"p_fdr\\\": 0.003599,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n  \\n\\n... [截断: 输出过长，省略 53412 字符] ...\\n\\n            \\\"p\\\": 0.004056\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.5368,\\n              \\\"p\\\": 0.170178\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.3895,\\n              \\\"p\\\": 0.387763\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.1853,\\n              \\\"p\\\": 0.725202\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": 1,\\n          \\\"r\\\": 0.88,\\n          \\\"p_value\\\": 0.001748,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.295,\\n              \\\"p\\\": 0.629857\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.3233,\\n              \\\"p\\\": 0.531976\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.0386,\\n              \\\"p\\\": 0.93452\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.1574,\\n              \\\"p\\\": 0.709649\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.1862,\\n              \\\"p\\\": 0.631373\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.2894,\\n              \\\"p\\\": 0.417328\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.88,\\n              \\\"p\\\": 0.001748\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.5685,\\n              \\\"p\\\": 0.141429\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.5171,\\n              \\\"p\\\": 0.234619\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.5537,\\n              \\\"p\\\": 0.254315\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.5443,\\n              \\\"p\\\": 0.342916\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.001748,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": null,\\n          \\\"downstream_onset\\\": 5,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 11.4314,\\n          \\\"p_value\\\": 0.031394,\\n          \\\"significant\\\": true,\\n          \\\"p_fdr\\\": 0.041859,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n          \\\"f_stat\\\": null,\\n          \\\"p_value\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"error\\\": \\\"VARResults.test_causality() got an unexpected keyword argument 'signonly'\\\",\\n          \\\"order\\\": 3,\\n          \\\"k_opt\\\": 2,\\n          \\\"d_max\\\": 1\\n        }\\n      }\\n    }\\n  ],\\n  \\\"consensus\\\": [\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_2\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_3\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<mauve\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_2\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_3\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<mauve\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    }\\n  ],\\n  \\\"summary\\\": {\\n    \\\"perm_granger_fdr_forward_sig\\\": 8,\\n    \\\"perm_granger_fdr_reverse_sig\\\": 7,\\n    \\\"diff_xcorr_fdr_forward_sig\\\": 8,\\n    \\\"diff_xcorr_fdr_reverse_sig\\\": 8,\\n    \\\"threshold_forward_sig\\\": 0,\\n    \\\"ty_forward_sig\\\": 0,\\n    \\\"robust_pairs\\\": 4\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.82}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "6b63d93e-5da9-4e3e-af6e-b633ba87a214",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"meta\\\\\\\": {\\\\n    \\\\\\\"alpha\\\\\\\": 0.5,\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"n_gens\\\\\\\": 11,\\\\n    \\\\\\\"data_dir\\\\\\\": \\\\\\\"results/alpha_sweep/c4_a050_s42_fp32\\\\\\\",\\\\n    \\\\\\\"methods\\\\\\\": [\\\\n      \\\\\\\"naive_xcorr\\\\\\\",\\\\n      \\\\\\\"diff_xcorr\\\\\\\",\\\\n      \\\\\\\"threshold_onset\\\\\\\",\\\\n      \\\\\\\"perm_granger\\\\\\\",\\\\n      \\\\\\\"ty_granger\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"n_perm\\\\\\\": 5000,\\\\n    \\\\\\\"canaries\\\\\\\": [\\\\n      \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"ece\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"downstreams\\\\\\\": [\\\\n      \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"distinct_3\\\\\\\",\\\\n      \\\\\\\"mauve\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"threshold_criterion\\\\\\\": \\\\\\\"true_3sigma_d105\\\\\\\"\\\\n  },\\\\n  \\\\\\\"pairs\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"forward\\\\\\\": {\\\\n        \\\\\\\"naive_xcorr\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"naive_xcorr\\\\\\\",\\\\n          \\\\\\\"peak_lag\\\\\\\": -5,\\\\n          \\\\\\\"r\\\\\\\": -0.9542,\\\\n          \\\\\\\"p_value\\\\\\\": 0.003102,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"all_lags\\\\\\\": [\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -5,\\\\n              \\\\\\\"r\\\\\\\": -0.9542,\\\\n              \\\\\\\"p\\\\\\\": 0.003102\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -4,\\\\n              \\\\\\\"r\\\\\\\": -0.932,\\\\n              \\\\\\\"p\\\\\\\": 0.002232\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -3,\\\\n              \\\\\\\"r\\\\\\\": -0.8115,\\\\n              \\\\\\\"p\\\\\\\": 0.01447\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -2,\\\\n              \\\\\\\"r\\\\\\\": -0.4843,\\\\n              \\\\\\\"p\\\\\\\": 0.186443\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -1,\\\\n              \\\\\\\"r\\\\\\\": 0.6323,\\\\n              \\\\\\\"p\\\\\\\": 0.049809\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 0,\\\\n              \\\\\\\"r\\\\\\\": 0.739,\\\\n              \\\\\\\"p\\\\\\\": 0.009364\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 1,\\\\n              \\\\\\\"r\\\\\\\": 0.791,\\\\n              \\\\\\\"p\\\\\\\": 0.006431\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": 0.8178,\\\\n              \\\\\\\"p\\\\\\\": 0.007083\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": 0.8355,\\\\n              \\\\\\\"p\\\\\\\": 0.009797\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": 0.8924,\\\\n              \\\\\\\"p\\\\\\\": 0.006871\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": 0.9165,\\\\n              \\\\\\\"p\\\\\\\": 0.010161\\\\n            }\\\\n          ]\\\\n        },\\\\n        \\\\\\\"diff_xcorr\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"diff_xcorr\\\\\\\",\\\\n          \\\\\\\"peak_lag\\\\\\\": -1,\\\\n          \\\\\\\"r\\\\\\\": 0.973,\\\\n          \\\\\\\"p_value\\\\\\\": 1e-05,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"all_lags\\\\\\\": [\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -5,\\\\n              \\\\\\\"r\\\\\\\": -0.7215,\\\\n              \\\\\\\"p\\\\\\\": 0.168842\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -4,\\\\n              \\\\\\\"r\\\\\\\": -0.6524,\\\\n              \\\\\\\"p\\\\\\\": 0.160232\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -3,\\\\n              \\\\\\\"r\\\\\\\": 0.5487,\\\\n              \\\\\\\"p\\\\\\\": 0.202175\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -2,\\\\n              \\\\\\\"r\\\\\\\": 0.8728,\\\\n              \\\\\\\"p\\\\\\\": 0.004668\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -1,\\\\n              \\\\\\\"r\\\\\\\": 0.973,\\\\n              \\\\\\\"p\\\\\\\": 1e-05\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 0,\\\\n              \\\\\\\"r\\\\\\\": 0.2365,\\\\n              \\\\\\\"p\\\\\\\": 0.510676\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 1,\\\\n              \\\\\\\"r\\\\\\\": 0.4434,\\\\n              \\\\\\\"p\\\\\\\": 0.231927\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": 0.3332,\\\\n              \\\\\\\"p\\\\\\\": 0.41994\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": 0.2007,\\\\n              \\\\\\\"p\\\\\\\": 0.666138\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": 0.3459,\\\\n              \\\\\\\"p\\\\\\\": 0.501894\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": 0.4361,\\\\n              \\\\\\\"p\\\\\\\": 0.46291\\\\n            }\\\\n          ],\\\\n          \\\\\\\"p_fdr\\\\\\\": 1.9e-05,\\\\n          \\\\\\\"significant_fdr\\\\\\\": true\\\\n        },\\\\n        \\\\\\\"threshold_onset\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"threshold_onset\\\\\\\",\\\\n          \\\\\\\"canary_onset\\\\\\\": 4,\\\\n          \\\\\\\"downstream_onset\\\\\\\": null,\\\\n          \\\\\\\"lead_time\\\\\\\": null,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"threshold\\\\\\\": \\\\\\\"true_3sigma_d105\\\\\\\"\\\\n        },\\\\n        \\\\\\\"perm_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"perm_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": 157.4118,\\\\n          \\\\\\\"p_value\\\\\\\": 0.003199,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.003599,\\\\n          \\\\\\\"significant_fdr\\\\\\\": true\\\\n        },\\\\n        \\\\\\\"ty_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"ty_granger\\\\\\\",\\\\n  \\\\n\\\\n... [截断: 输出过长，省略 53412 字符] ...\\\\n\\\\n            \\\\\\\"p\\\\\\\": 0.004056\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": 0.5368,\\\\n              \\\\\\\"p\\\\\\\": 0.170178\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": -0.3895,\\\\n              \\\\\\\"p\\\\\\\": 0.387763\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": 0.1853,\\\\n              \\\\\\\"p\\\\\\\": 0.725202\\\\n            }\\\\n          ]\\\\n        },\\\\n        \\\\\\\"diff_xcorr\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"diff_xcorr\\\\\\\",\\\\n          \\\\\\\"peak_lag\\\\\\\": 1,\\\\n          \\\\\\\"r\\\\\\\": 0.88,\\\\n          \\\\\\\"p_value\\\\\\\": 0.001748,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"all_lags\\\\\\\": [\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -5,\\\\n              \\\\\\\"r\\\\\\\": 0.295,\\\\n              \\\\\\\"p\\\\\\\": 0.629857\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -4,\\\\n              \\\\\\\"r\\\\\\\": 0.3233,\\\\n              \\\\\\\"p\\\\\\\": 0.531976\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -3,\\\\n              \\\\\\\"r\\\\\\\": 0.0386,\\\\n              \\\\\\\"p\\\\\\\": 0.93452\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -2,\\\\n              \\\\\\\"r\\\\\\\": 0.1574,\\\\n              \\\\\\\"p\\\\\\\": 0.709649\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -1,\\\\n              \\\\\\\"r\\\\\\\": 0.1862,\\\\n              \\\\\\\"p\\\\\\\": 0.631373\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 0,\\\\n              \\\\\\\"r\\\\\\\": 0.2894,\\\\n              \\\\\\\"p\\\\\\\": 0.417328\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 1,\\\\n              \\\\\\\"r\\\\\\\": 0.88,\\\\n              \\\\\\\"p\\\\\\\": 0.001748\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": 0.5685,\\\\n              \\\\\\\"p\\\\\\\": 0.141429\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": 0.5171,\\\\n              \\\\\\\"p\\\\\\\": 0.234619\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": -0.5537,\\\\n              \\\\\\\"p\\\\\\\": 0.254315\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": -0.5443,\\\\n              \\\\\\\"p\\\\\\\": 0.342916\\\\n            }\\\\n          ],\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.001748,\\\\n          \\\\\\\"significant_fdr\\\\\\\": true\\\\n        },\\\\n        \\\\\\\"threshold_onset\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"threshold_onset\\\\\\\",\\\\n          \\\\\\\"canary_onset\\\\\\\": null,\\\\n          \\\\\\\"downstream_onset\\\\\\\": 5,\\\\n          \\\\\\\"lead_time\\\\\\\": null,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"threshold\\\\\\\": \\\\\\\"true_3sigma_d105\\\\\\\"\\\\n        },\\\\n        \\\\\\\"perm_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"perm_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": 11.4314,\\\\n          \\\\\\\"p_value\\\\\\\": 0.031394,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.041859,\\\\n          \\\\\\\"significant_fdr\\\\\\\": true\\\\n        },\\\\n        \\\\\\\"ty_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"ty_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": null,\\\\n          \\\\\\\"p_value\\\\\\\": null,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"error\\\\\\\": \\\\\\\"VARResults.test_causality() got an unexpected keyword argument 'signonly'\\\\\\\",\\\\n          \\\\\\\"order\\\\\\\": 3,\\\\n          \\\\\\\"k_opt\\\\\\\": 2,\\\\n          \\\\\\\"d_max\\\\\\\": 1\\\\n        }\\\\n      }\\\\n    }\\\\n  ],\\\\n  \\\\\\\"consensus\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<distinct_1\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<distinct_2\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 2,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<distinct_3\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<mauve\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<distinct_1\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<distinct_2\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 2,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<distinct_3\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 2,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<mauve\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 2,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    }\\\\n  ],\\\\n  \\\\\\\"summary\\\\\\\": {\\\\n    \\\\\\\"perm_granger_fdr_forward_sig\\\\\\\": 8,\\\\n    \\\\\\\"perm_granger_fdr_reverse_sig\\\\\\\": 7,\\\\n    \\\\\\\"diff_xcorr_fdr_forward_sig\\\\\\\": 8,\\\\n    \\\\\\\"diff_xcorr_fdr_reverse_sig\\\\\\\": 8,\\\\n    \\\\\\\"threshold_forward_sig\\\\\\\": 0,\\\\n    \\\\\\\"ty_forward_sig\\\\\\\": 0,\\\\n    \\\\\\\"robust_pairs\\\\\\\": 4\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.82}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 0.5,\\n    \\\"seed\\\": 42,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"results/alpha_sweep/c4_a050_s42_fp32\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -5,\\n          \\\"r\\\": -0.9542,\\n          \\\"p_value\\\": 0.003102,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": -0.9542,\\n              \\\"p\\\": 0.003102\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.932,\\n              \\\"p\\\": 0.002232\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": -0.8115,\\n              \\\"p\\\": 0.01447\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": -0.4843,\\n              \\\"p\\\": 0.186443\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.6323,\\n              \\\"p\\\": 0.049809\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.739,\\n              \\\"p\\\": 0.009364\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.791,\\n              \\\"p\\\": 0.006431\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.8178,\\n              \\\"p\\\": 0.007083\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.8355,\\n              \\\"p\\\": 0.009797\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.8924,\\n              \\\"p\\\": 0.006871\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.9165,\\n              \\\"p\\\": 0.010161\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.973,\\n          \\\"p_value\\\": 1e-05,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": -0.7215,\\n              \\\"p\\\": 0.168842\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.6524,\\n              \\\"p\\\": 0.160232\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.5487,\\n              \\\"p\\\": 0.202175\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.8728,\\n              \\\"p\\\": 0.004668\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.973,\\n              \\\"p\\\": 1e-05\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.2365,\\n              \\\"p\\\": 0.510676\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.4434,\\n              \\\"p\\\": 0.231927\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.3332,\\n              \\\"p\\\": 0.41994\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.2007,\\n              \\\"p\\\": 0.666138\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.3459,\\n              \\\"p\\\": 0.501894\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.4361,\\n              \\\"p\\\": 0.46291\\n            }\\n          ],\\n          \\\"p_fdr\\\": 1.9e-05,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": 4,\\n          \\\"downstream_onset\\\": null,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 157.4118,\\n          \\\"p_value\\\": 0.003199,\\n          \\\"significant\\\": true,\\n          \\\"p_fdr\\\": 0.003599,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n  \\n\\n... [截断: 输出过长，省略 53412 字符] ...\\n\\n            \\\"p\\\": 0.004056\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.5368,\\n              \\\"p\\\": 0.170178\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.3895,\\n              \\\"p\\\": 0.387763\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.1853,\\n              \\\"p\\\": 0.725202\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": 1,\\n          \\\"r\\\": 0.88,\\n          \\\"p_value\\\": 0.001748,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.295,\\n              \\\"p\\\": 0.629857\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.3233,\\n              \\\"p\\\": 0.531976\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.0386,\\n              \\\"p\\\": 0.93452\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.1574,\\n              \\\"p\\\": 0.709649\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.1862,\\n              \\\"p\\\": 0.631373\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.2894,\\n              \\\"p\\\": 0.417328\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.88,\\n              \\\"p\\\": 0.001748\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.5685,\\n              \\\"p\\\": 0.141429\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.5171,\\n              \\\"p\\\": 0.234619\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.5537,\\n              \\\"p\\\": 0.254315\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.5443,\\n              \\\"p\\\": 0.342916\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.001748,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": null,\\n          \\\"downstream_onset\\\": 5,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 11.4314,\\n          \\\"p_value\\\": 0.031394,\\n          \\\"significant\\\": true,\\n          \\\"p_fdr\\\": 0.041859,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n          \\\"f_stat\\\": null,\\n          \\\"p_value\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"error\\\": \\\"VARResults.test_causality() got an unexpected keyword argument 'signonly'\\\",\\n          \\\"order\\\": 3,\\n          \\\"k_opt\\\": 2,\\n          \\\"d_max\\\": 1\\n        }\\n      }\\n    }\\n  ],\\n  \\\"consensus\\\": [\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_2\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_3\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<mauve\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_2\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_3\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<mauve\\\",\\n      \\\"votes\\\": 2,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    }\\n  ],\\n  \\\"summary\\\": {\\n    \\\"perm_granger_fdr_forward_sig\\\": 8,\\n    \\\"perm_granger_fdr_reverse_sig\\\": 7,\\n    \\\"diff_xcorr_fdr_forward_sig\\\": 8,\\n    \\\"diff_xcorr_fdr_reverse_sig\\\": 8,\\n    \\\"threshold_forward_sig\\\": 0,\\n    \\\"ty_forward_sig\\\": 0,\\n    \\\"robust_pairs\\\": 4\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.82}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T06:04:10.111Z_

<details><summary>↩ Tool result · `toolu_01Kgq2A2PRJKqY2UmaZQTjcU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 0.75,\\n    \\\"seed\\\": 42,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"results/alpha_sweep/c4_a075_s42_fp32\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.973,\\n          \\\"p_value\\\": 2e-06,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": -0.7884,\\n              \\\"p\\\": 0.062412\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.6741,\\n              \\\"p\\\": 0.096813\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": -0.5522,\\n              \\\"p\\\": 0.155818\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.1153,\\n              \\\"p\\\": 0.767656\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.973,\\n              \\\"p\\\": 2e-06\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.7507,\\n              \\\"p\\\": 0.007764\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.4824,\\n              \\\"p\\\": 0.157938\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": -0.3291,\\n              \\\"p\\\": 0.387171\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": -0.6352,\\n              \\\"p\\\": 0.090556\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.8619,\\n              \\\"p\\\": 0.01263\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.9236,\\n              \\\"p\\\": 0.008541\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.9961,\\n          \\\"p_value\\\": 0.0,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.0391,\\n              \\\"p\\\": 0.950235\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.2836,\\n              \\\"p\\\": 0.586023\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.438,\\n              \\\"p\\\": 0.325688\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.9656,\\n              \\\"p\\\": 0.0001\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.9961,\\n              \\\"p\\\": 0.0\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.0491,\\n              \\\"p\\\": 0.892929\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.1239,\\n              \\\"p\\\": 0.750742\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.0755,\\n              \\\"p\\\": 0.858957\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.2418,\\n              \\\"p\\\": 0.601356\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.4305,\\n              \\\"p\\\": 0.394154\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.5255,\\n              \\\"p\\\": 0.363177\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.0,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": 2,\\n          \\\"downstream_onset\\\": null,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 772.5559,\\n          \\\"p_value\\\": 0.004799,\\n          \\\"significant\\\": true,\\n          \\\"p_fdr\\\": 0.006399,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n          \\\"\\n\\n... [截断: 输出过长，省略 53428 字符] ...\\n\\n\\n              \\\"r\\\": -0.3008,\\n              \\\"p\\\": 0.469174\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.8329,\\n              \\\"p\\\": 0.019993\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.4131,\\n              \\\"p\\\": 0.415552\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": 1,\\n          \\\"r\\\": 0.9083,\\n          \\\"p_value\\\": 0.000701,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": -0.8423,\\n              \\\"p\\\": 0.073403\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.0949,\\n              \\\"p\\\": 0.858005\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.3454,\\n              \\\"p\\\": 0.448014\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.1558,\\n              \\\"p\\\": 0.712603\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.0911,\\n              \\\"p\\\": 0.815633\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.1235,\\n              \\\"p\\\": 0.733865\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.9083,\\n              \\\"p\\\": 0.000701\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": -0.0508,\\n              \\\"p\\\": 0.904972\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.5409,\\n              \\\"p\\\": 0.209952\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.5113,\\n              \\\"p\\\": 0.299925\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.7099,\\n              \\\"p\\\": 0.179222\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.000701,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": null,\\n          \\\"downstream_onset\\\": 3,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 0.0612,\\n          \\\"p_value\\\": 0.885023,\\n          \\\"significant\\\": false,\\n          \\\"p_fdr\\\": 0.917017,\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n          \\\"f_stat\\\": null,\\n          \\\"p_value\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"error\\\": \\\"VARResults.test_causality() got an unexpected keyword argument 'signonly'\\\",\\n          \\\"order\\\": 3,\\n          \\\"k_opt\\\": 2,\\n          \\\"d_max\\\": 1\\n        }\\n      }\\n    }\\n  ],\\n  \\\"consensus\\\": [\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_2\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_3\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<mauve\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_2\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_3\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<mauve\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    }\\n  ],\\n  \\\"summary\\\": {\\n    \\\"perm_granger_fdr_forward_sig\\\": 8,\\n    \\\"perm_granger_fdr_reverse_sig\\\": 0,\\n    \\\"diff_xcorr_fdr_forward_sig\\\": 8,\\n    \\\"diff_xcorr_fdr_reverse_sig\\\": 8,\\n    \\\"threshold_forward_sig\\\": 0,\\n    \\\"ty_forward_sig\\\": 0,\\n    \\\"robust_pairs\\\": 8\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.93}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "44c71a28-d9e5-41b6-8c73-e9db1b71000d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"meta\\\\\\\": {\\\\n    \\\\\\\"alpha\\\\\\\": 0.75,\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"n_gens\\\\\\\": 11,\\\\n    \\\\\\\"data_dir\\\\\\\": \\\\\\\"results/alpha_sweep/c4_a075_s42_fp32\\\\\\\",\\\\n    \\\\\\\"methods\\\\\\\": [\\\\n      \\\\\\\"naive_xcorr\\\\\\\",\\\\n      \\\\\\\"diff_xcorr\\\\\\\",\\\\n      \\\\\\\"threshold_onset\\\\\\\",\\\\n      \\\\\\\"perm_granger\\\\\\\",\\\\n      \\\\\\\"ty_granger\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"n_perm\\\\\\\": 5000,\\\\n    \\\\\\\"canaries\\\\\\\": [\\\\n      \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"ece\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"downstreams\\\\\\\": [\\\\n      \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"distinct_3\\\\\\\",\\\\n      \\\\\\\"mauve\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"threshold_criterion\\\\\\\": \\\\\\\"true_3sigma_d105\\\\\\\"\\\\n  },\\\\n  \\\\\\\"pairs\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"forward\\\\\\\": {\\\\n        \\\\\\\"naive_xcorr\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"naive_xcorr\\\\\\\",\\\\n          \\\\\\\"peak_lag\\\\\\\": -1,\\\\n          \\\\\\\"r\\\\\\\": 0.973,\\\\n          \\\\\\\"p_value\\\\\\\": 2e-06,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"all_lags\\\\\\\": [\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -5,\\\\n              \\\\\\\"r\\\\\\\": -0.7884,\\\\n              \\\\\\\"p\\\\\\\": 0.062412\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -4,\\\\n              \\\\\\\"r\\\\\\\": -0.6741,\\\\n              \\\\\\\"p\\\\\\\": 0.096813\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -3,\\\\n              \\\\\\\"r\\\\\\\": -0.5522,\\\\n              \\\\\\\"p\\\\\\\": 0.155818\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -2,\\\\n              \\\\\\\"r\\\\\\\": 0.1153,\\\\n              \\\\\\\"p\\\\\\\": 0.767656\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -1,\\\\n              \\\\\\\"r\\\\\\\": 0.973,\\\\n              \\\\\\\"p\\\\\\\": 2e-06\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 0,\\\\n              \\\\\\\"r\\\\\\\": 0.7507,\\\\n              \\\\\\\"p\\\\\\\": 0.007764\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 1,\\\\n              \\\\\\\"r\\\\\\\": 0.4824,\\\\n              \\\\\\\"p\\\\\\\": 0.157938\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": -0.3291,\\\\n              \\\\\\\"p\\\\\\\": 0.387171\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": -0.6352,\\\\n              \\\\\\\"p\\\\\\\": 0.090556\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": -0.8619,\\\\n              \\\\\\\"p\\\\\\\": 0.01263\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": -0.9236,\\\\n              \\\\\\\"p\\\\\\\": 0.008541\\\\n            }\\\\n          ]\\\\n        },\\\\n        \\\\\\\"diff_xcorr\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"diff_xcorr\\\\\\\",\\\\n          \\\\\\\"peak_lag\\\\\\\": -1,\\\\n          \\\\\\\"r\\\\\\\": 0.9961,\\\\n          \\\\\\\"p_value\\\\\\\": 0.0,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"all_lags\\\\\\\": [\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -5,\\\\n              \\\\\\\"r\\\\\\\": 0.0391,\\\\n              \\\\\\\"p\\\\\\\": 0.950235\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -4,\\\\n              \\\\\\\"r\\\\\\\": 0.2836,\\\\n              \\\\\\\"p\\\\\\\": 0.586023\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -3,\\\\n              \\\\\\\"r\\\\\\\": 0.438,\\\\n              \\\\\\\"p\\\\\\\": 0.325688\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -2,\\\\n              \\\\\\\"r\\\\\\\": 0.9656,\\\\n              \\\\\\\"p\\\\\\\": 0.0001\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -1,\\\\n              \\\\\\\"r\\\\\\\": 0.9961,\\\\n              \\\\\\\"p\\\\\\\": 0.0\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 0,\\\\n              \\\\\\\"r\\\\\\\": 0.0491,\\\\n              \\\\\\\"p\\\\\\\": 0.892929\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 1,\\\\n              \\\\\\\"r\\\\\\\": 0.1239,\\\\n              \\\\\\\"p\\\\\\\": 0.750742\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": 0.0755,\\\\n              \\\\\\\"p\\\\\\\": 0.858957\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": 0.2418,\\\\n              \\\\\\\"p\\\\\\\": 0.601356\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": -0.4305,\\\\n              \\\\\\\"p\\\\\\\": 0.394154\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": -0.5255,\\\\n              \\\\\\\"p\\\\\\\": 0.363177\\\\n            }\\\\n          ],\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.0,\\\\n          \\\\\\\"significant_fdr\\\\\\\": true\\\\n        },\\\\n        \\\\\\\"threshold_onset\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"threshold_onset\\\\\\\",\\\\n          \\\\\\\"canary_onset\\\\\\\": 2,\\\\n          \\\\\\\"downstream_onset\\\\\\\": null,\\\\n          \\\\\\\"lead_time\\\\\\\": null,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"threshold\\\\\\\": \\\\\\\"true_3sigma_d105\\\\\\\"\\\\n        },\\\\n        \\\\\\\"perm_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"perm_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": 772.5559,\\\\n          \\\\\\\"p_value\\\\\\\": 0.004799,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.006399,\\\\n          \\\\\\\"significant_fdr\\\\\\\": true\\\\n        },\\\\n        \\\\\\\"ty_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"ty_granger\\\\\\\",\\\\n          \\\\\\\"\\\\n\\\\n... [截断: 输出过长，省略 53428 字符] ...\\\\n\\\\n\\\\n              \\\\\\\"r\\\\\\\": -0.3008,\\\\n              \\\\\\\"p\\\\\\\": 0.469174\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": -0.8329,\\\\n              \\\\\\\"p\\\\\\\": 0.019993\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": -0.4131,\\\\n              \\\\\\\"p\\\\\\\": 0.415552\\\\n            }\\\\n          ]\\\\n        },\\\\n        \\\\\\\"diff_xcorr\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"diff_xcorr\\\\\\\",\\\\n          \\\\\\\"peak_lag\\\\\\\": 1,\\\\n          \\\\\\\"r\\\\\\\": 0.9083,\\\\n          \\\\\\\"p_value\\\\\\\": 0.000701,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"all_lags\\\\\\\": [\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -5,\\\\n              \\\\\\\"r\\\\\\\": -0.8423,\\\\n              \\\\\\\"p\\\\\\\": 0.073403\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -4,\\\\n              \\\\\\\"r\\\\\\\": 0.0949,\\\\n              \\\\\\\"p\\\\\\\": 0.858005\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -3,\\\\n              \\\\\\\"r\\\\\\\": 0.3454,\\\\n              \\\\\\\"p\\\\\\\": 0.448014\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -2,\\\\n              \\\\\\\"r\\\\\\\": 0.1558,\\\\n              \\\\\\\"p\\\\\\\": 0.712603\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -1,\\\\n              \\\\\\\"r\\\\\\\": 0.0911,\\\\n              \\\\\\\"p\\\\\\\": 0.815633\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 0,\\\\n              \\\\\\\"r\\\\\\\": 0.1235,\\\\n              \\\\\\\"p\\\\\\\": 0.733865\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 1,\\\\n              \\\\\\\"r\\\\\\\": 0.9083,\\\\n              \\\\\\\"p\\\\\\\": 0.000701\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": -0.0508,\\\\n              \\\\\\\"p\\\\\\\": 0.904972\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": 0.5409,\\\\n              \\\\\\\"p\\\\\\\": 0.209952\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": -0.5113,\\\\n              \\\\\\\"p\\\\\\\": 0.299925\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": 0.7099,\\\\n              \\\\\\\"p\\\\\\\": 0.179222\\\\n            }\\\\n          ],\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.000701,\\\\n          \\\\\\\"significant_fdr\\\\\\\": true\\\\n        },\\\\n        \\\\\\\"threshold_onset\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"threshold_onset\\\\\\\",\\\\n          \\\\\\\"canary_onset\\\\\\\": null,\\\\n          \\\\\\\"downstream_onset\\\\\\\": 3,\\\\n          \\\\\\\"lead_time\\\\\\\": null,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"threshold\\\\\\\": \\\\\\\"true_3sigma_d105\\\\\\\"\\\\n        },\\\\n        \\\\\\\"perm_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"perm_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": 0.0612,\\\\n          \\\\\\\"p_value\\\\\\\": 0.885023,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.917017,\\\\n          \\\\\\\"significant_fdr\\\\\\\": false\\\\n        },\\\\n        \\\\\\\"ty_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"ty_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": null,\\\\n          \\\\\\\"p_value\\\\\\\": null,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"error\\\\\\\": \\\\\\\"VARResults.test_causality() got an unexpected keyword argument 'signonly'\\\\\\\",\\\\n          \\\\\\\"order\\\\\\\": 3,\\\\n          \\\\\\\"k_opt\\\\\\\": 2,\\\\n          \\\\\\\"d_max\\\\\\\": 1\\\\n        }\\\\n      }\\\\n    }\\\\n  ],\\\\n  \\\\\\\"consensus\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<distinct_1\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<distinct_2\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<distinct_3\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<mauve\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<distinct_1\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<distinct_2\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<distinct_3\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<mauve\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    }\\\\n  ],\\\\n  \\\\\\\"summary\\\\\\\": {\\\\n    \\\\\\\"perm_granger_fdr_forward_sig\\\\\\\": 8,\\\\n    \\\\\\\"perm_granger_fdr_reverse_sig\\\\\\\": 0,\\\\n    \\\\\\\"diff_xcorr_fdr_forward_sig\\\\\\\": 8,\\\\n    \\\\\\\"diff_xcorr_fdr_reverse_sig\\\\\\\": 8,\\\\n    \\\\\\\"threshold_forward_sig\\\\\\\": 0,\\\\n    \\\\\\\"ty_forward_sig\\\\\\\": 0,\\\\n    \\\\\\\"robust_pairs\\\\\\\": 8\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.93}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 0.75,\\n    \\\"seed\\\": 42,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"results/alpha_sweep/c4_a075_s42_fp32\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.973,\\n          \\\"p_value\\\": 2e-06,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": -0.7884,\\n              \\\"p\\\": 0.062412\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.6741,\\n              \\\"p\\\": 0.096813\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": -0.5522,\\n              \\\"p\\\": 0.155818\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.1153,\\n              \\\"p\\\": 0.767656\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.973,\\n              \\\"p\\\": 2e-06\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.7507,\\n              \\\"p\\\": 0.007764\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.4824,\\n              \\\"p\\\": 0.157938\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": -0.3291,\\n              \\\"p\\\": 0.387171\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": -0.6352,\\n              \\\"p\\\": 0.090556\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.8619,\\n              \\\"p\\\": 0.01263\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.9236,\\n              \\\"p\\\": 0.008541\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.9961,\\n          \\\"p_value\\\": 0.0,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.0391,\\n              \\\"p\\\": 0.950235\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.2836,\\n              \\\"p\\\": 0.586023\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.438,\\n              \\\"p\\\": 0.325688\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.9656,\\n              \\\"p\\\": 0.0001\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.9961,\\n              \\\"p\\\": 0.0\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.0491,\\n              \\\"p\\\": 0.892929\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.1239,\\n              \\\"p\\\": 0.750742\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.0755,\\n              \\\"p\\\": 0.858957\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.2418,\\n              \\\"p\\\": 0.601356\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.4305,\\n              \\\"p\\\": 0.394154\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.5255,\\n              \\\"p\\\": 0.363177\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.0,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": 2,\\n          \\\"downstream_onset\\\": null,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 772.5559,\\n          \\\"p_value\\\": 0.004799,\\n          \\\"significant\\\": true,\\n          \\\"p_fdr\\\": 0.006399,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n          \\\"\\n\\n... [截断: 输出过长，省略 53428 字符] ...\\n\\n\\n              \\\"r\\\": -0.3008,\\n              \\\"p\\\": 0.469174\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.8329,\\n              \\\"p\\\": 0.019993\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.4131,\\n              \\\"p\\\": 0.415552\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": 1,\\n          \\\"r\\\": 0.9083,\\n          \\\"p_value\\\": 0.000701,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": -0.8423,\\n              \\\"p\\\": 0.073403\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.0949,\\n              \\\"p\\\": 0.858005\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.3454,\\n              \\\"p\\\": 0.448014\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.1558,\\n              \\\"p\\\": 0.712603\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.0911,\\n              \\\"p\\\": 0.815633\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.1235,\\n              \\\"p\\\": 0.733865\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.9083,\\n              \\\"p\\\": 0.000701\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": -0.0508,\\n              \\\"p\\\": 0.904972\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.5409,\\n              \\\"p\\\": 0.209952\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.5113,\\n              \\\"p\\\": 0.299925\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.7099,\\n              \\\"p\\\": 0.179222\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.000701,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": null,\\n          \\\"downstream_onset\\\": 3,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 0.0612,\\n          \\\"p_value\\\": 0.885023,\\n          \\\"significant\\\": false,\\n          \\\"p_fdr\\\": 0.917017,\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n          \\\"f_stat\\\": null,\\n          \\\"p_value\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"error\\\": \\\"VARResults.test_causality() got an unexpected keyword argument 'signonly'\\\",\\n          \\\"order\\\": 3,\\n          \\\"k_opt\\\": 2,\\n          \\\"d_max\\\": 1\\n        }\\n      }\\n    }\\n  ],\\n  \\\"consensus\\\": [\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_2\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_3\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<mauve\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_2\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_3\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<mauve\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    }\\n  ],\\n  \\\"summary\\\": {\\n    \\\"perm_granger_fdr_forward_sig\\\": 8,\\n    \\\"perm_granger_fdr_reverse_sig\\\": 0,\\n    \\\"diff_xcorr_fdr_forward_sig\\\": 8,\\n    \\\"diff_xcorr_fdr_reverse_sig\\\": 8,\\n    \\\"threshold_forward_sig\\\": 0,\\n    \\\"ty_forward_sig\\\": 0,\\n    \\\"robust_pairs\\\": 8\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.93}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T06:04:13.073Z_

<details><summary>↩ Tool result · `toolu_01VUkNsborA9nnW3tmhhW6XN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 1.0,\\n    \\\"seed\\\": 42,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"results/padding_robustness/a100_s42_fp32\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.9915,\\n          \\\"p_value\\\": 0.0,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.9052,\\n              \\\"p\\\": 0.013041\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.6205,\\n              \\\"p\\\": 0.137094\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.9753,\\n              \\\"p\\\": 3.7e-05\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.9914,\\n              \\\"p\\\": 0.0\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.9915,\\n              \\\"p\\\": 0.0\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.8601,\\n              \\\"p\\\": 0.000684\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.8649,\\n              \\\"p\\\": 0.001235\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.8376,\\n              \\\"p\\\": 0.004832\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.6115,\\n              \\\"p\\\": 0.107199\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.7333,\\n              \\\"p\\\": 0.06073\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.4505,\\n              \\\"p\\\": 0.370007\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.9887,\\n          \\\"p_value\\\": 0.0,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.7514,\\n              \\\"p\\\": 0.14314\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.4602,\\n              \\\"p\\\": 0.358416\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.9191,\\n              \\\"p\\\": 0.003422\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.9886,\\n              \\\"p\\\": 4e-06\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.9887,\\n              \\\"p\\\": 0.0\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.1676,\\n              \\\"p\\\": 0.643447\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.141,\\n              \\\"p\\\": 0.717391\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.1835,\\n              \\\"p\\\": 0.663583\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": -0.4009,\\n              \\\"p\\\": 0.372798\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.6846,\\n              \\\"p\\\": 0.133539\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.4432,\\n              \\\"p\\\": 0.45478\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.0,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": 2,\\n          \\\"downstream_onset\\\": null,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 461.551,\\n          \\\"p_value\\\": 0.004599,\\n          \\\"significant\\\": true,\\n          \\\"p_fdr\\\": 0.006132,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n          \\\"f_stat\\\": null,\\n\\n\\n... [截断: 输出过长，省略 53234 字符] ...\\n\\n              \\\"r\\\": 0.2991,\\n              \\\"p\\\": 0.434241\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": -0.2046,\\n              \\\"p\\\": 0.626884\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.4323,\\n              \\\"p\\\": 0.332699\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.16,\\n              \\\"p\\\": 0.762117\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": 5,\\n          \\\"r\\\": 0.6252,\\n          \\\"p_value\\\": 0.259368,\\n          \\\"significant\\\": false,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": -0.1829,\\n              \\\"p\\\": 0.768468\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.2003,\\n              \\\"p\\\": 0.703513\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": -0.3273,\\n              \\\"p\\\": 0.473677\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": -0.0482,\\n              \\\"p\\\": 0.909796\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": -0.1714,\\n              \\\"p\\\": 0.659217\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": -0.1035,\\n              \\\"p\\\": 0.775986\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": -0.1023,\\n              \\\"p\\\": 0.793427\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.4906,\\n              \\\"p\\\": 0.217088\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.2792,\\n              \\\"p\\\": 0.544288\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.0002,\\n              \\\"p\\\": 0.999657\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.6252,\\n              \\\"p\\\": 0.259368\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.259368,\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": null,\\n          \\\"downstream_onset\\\": 4,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 0.2711,\\n          \\\"p_value\\\": 0.628074,\\n          \\\"significant\\\": false,\\n          \\\"p_fdr\\\": 0.981604,\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n          \\\"f_stat\\\": null,\\n          \\\"p_value\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"error\\\": \\\"VARResults.test_causality() got an unexpected keyword argument 'signonly'\\\",\\n          \\\"order\\\": 1,\\n          \\\"k_opt\\\": 1,\\n          \\\"d_max\\\": 0\\n        }\\n      }\\n    }\\n  ],\\n  \\\"consensus\\\": [\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_2\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_3\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<mauve\\\",\\n      \\\"votes\\\": 0,\\n      \\\"methods\\\": []\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_2\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_3\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<mauve\\\",\\n      \\\"votes\\\": 0,\\n      \\\"methods\\\": []\\n    }\\n  ],\\n  \\\"summary\\\": {\\n    \\\"perm_granger_fdr_forward_sig\\\": 6,\\n    \\\"perm_granger_fdr_reverse_sig\\\": 0,\\n    \\\"diff_xcorr_fdr_forward_sig\\\": 6,\\n    \\\"diff_xcorr_fdr_reverse_sig\\\": 6,\\n    \\\"threshold_forward_sig\\\": 0,\\n    \\\"ty_forward_sig\\\": 0,\\n    \\\"robust_pairs\\\": 6\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.94}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "b46b63e8-d392-44e5-8536-b251abd3f0ec",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"meta\\\\\\\": {\\\\n    \\\\\\\"alpha\\\\\\\": 1.0,\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"n_gens\\\\\\\": 11,\\\\n    \\\\\\\"data_dir\\\\\\\": \\\\\\\"results/padding_robustness/a100_s42_fp32\\\\\\\",\\\\n    \\\\\\\"methods\\\\\\\": [\\\\n      \\\\\\\"naive_xcorr\\\\\\\",\\\\n      \\\\\\\"diff_xcorr\\\\\\\",\\\\n      \\\\\\\"threshold_onset\\\\\\\",\\\\n      \\\\\\\"perm_granger\\\\\\\",\\\\n      \\\\\\\"ty_granger\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"n_perm\\\\\\\": 5000,\\\\n    \\\\\\\"canaries\\\\\\\": [\\\\n      \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"ece\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"downstreams\\\\\\\": [\\\\n      \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"distinct_3\\\\\\\",\\\\n      \\\\\\\"mauve\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"threshold_criterion\\\\\\\": \\\\\\\"true_3sigma_d105\\\\\\\"\\\\n  },\\\\n  \\\\\\\"pairs\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"forward\\\\\\\": {\\\\n        \\\\\\\"naive_xcorr\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"naive_xcorr\\\\\\\",\\\\n          \\\\\\\"peak_lag\\\\\\\": -1,\\\\n          \\\\\\\"r\\\\\\\": 0.9915,\\\\n          \\\\\\\"p_value\\\\\\\": 0.0,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"all_lags\\\\\\\": [\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -5,\\\\n              \\\\\\\"r\\\\\\\": 0.9052,\\\\n              \\\\\\\"p\\\\\\\": 0.013041\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -4,\\\\n              \\\\\\\"r\\\\\\\": 0.6205,\\\\n              \\\\\\\"p\\\\\\\": 0.137094\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -3,\\\\n              \\\\\\\"r\\\\\\\": 0.9753,\\\\n              \\\\\\\"p\\\\\\\": 3.7e-05\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -2,\\\\n              \\\\\\\"r\\\\\\\": 0.9914,\\\\n              \\\\\\\"p\\\\\\\": 0.0\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -1,\\\\n              \\\\\\\"r\\\\\\\": 0.9915,\\\\n              \\\\\\\"p\\\\\\\": 0.0\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 0,\\\\n              \\\\\\\"r\\\\\\\": 0.8601,\\\\n              \\\\\\\"p\\\\\\\": 0.000684\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 1,\\\\n              \\\\\\\"r\\\\\\\": 0.8649,\\\\n              \\\\\\\"p\\\\\\\": 0.001235\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": 0.8376,\\\\n              \\\\\\\"p\\\\\\\": 0.004832\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": 0.6115,\\\\n              \\\\\\\"p\\\\\\\": 0.107199\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": 0.7333,\\\\n              \\\\\\\"p\\\\\\\": 0.06073\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": 0.4505,\\\\n              \\\\\\\"p\\\\\\\": 0.370007\\\\n            }\\\\n          ]\\\\n        },\\\\n        \\\\\\\"diff_xcorr\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"diff_xcorr\\\\\\\",\\\\n          \\\\\\\"peak_lag\\\\\\\": -1,\\\\n          \\\\\\\"r\\\\\\\": 0.9887,\\\\n          \\\\\\\"p_value\\\\\\\": 0.0,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"all_lags\\\\\\\": [\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -5,\\\\n              \\\\\\\"r\\\\\\\": 0.7514,\\\\n              \\\\\\\"p\\\\\\\": 0.14314\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -4,\\\\n              \\\\\\\"r\\\\\\\": -0.4602,\\\\n              \\\\\\\"p\\\\\\\": 0.358416\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -3,\\\\n              \\\\\\\"r\\\\\\\": 0.9191,\\\\n              \\\\\\\"p\\\\\\\": 0.003422\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -2,\\\\n              \\\\\\\"r\\\\\\\": 0.9886,\\\\n              \\\\\\\"p\\\\\\\": 4e-06\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -1,\\\\n              \\\\\\\"r\\\\\\\": 0.9887,\\\\n              \\\\\\\"p\\\\\\\": 0.0\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 0,\\\\n              \\\\\\\"r\\\\\\\": 0.1676,\\\\n              \\\\\\\"p\\\\\\\": 0.643447\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 1,\\\\n              \\\\\\\"r\\\\\\\": 0.141,\\\\n              \\\\\\\"p\\\\\\\": 0.717391\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": 0.1835,\\\\n              \\\\\\\"p\\\\\\\": 0.663583\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": -0.4009,\\\\n              \\\\\\\"p\\\\\\\": 0.372798\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": 0.6846,\\\\n              \\\\\\\"p\\\\\\\": 0.133539\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": -0.4432,\\\\n              \\\\\\\"p\\\\\\\": 0.45478\\\\n            }\\\\n          ],\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.0,\\\\n          \\\\\\\"significant_fdr\\\\\\\": true\\\\n        },\\\\n        \\\\\\\"threshold_onset\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"threshold_onset\\\\\\\",\\\\n          \\\\\\\"canary_onset\\\\\\\": 2,\\\\n          \\\\\\\"downstream_onset\\\\\\\": null,\\\\n          \\\\\\\"lead_time\\\\\\\": null,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"threshold\\\\\\\": \\\\\\\"true_3sigma_d105\\\\\\\"\\\\n        },\\\\n        \\\\\\\"perm_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"perm_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": 461.551,\\\\n          \\\\\\\"p_value\\\\\\\": 0.004599,\\\\n          \\\\\\\"significant\\\\\\\": true,\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.006132,\\\\n          \\\\\\\"significant_fdr\\\\\\\": true\\\\n        },\\\\n        \\\\\\\"ty_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"ty_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": null,\\\\n\\\\n\\\\n... [截断: 输出过长，省略 53234 字符] ...\\\\n\\\\n              \\\\\\\"r\\\\\\\": 0.2991,\\\\n              \\\\\\\"p\\\\\\\": 0.434241\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": -0.2046,\\\\n              \\\\\\\"p\\\\\\\": 0.626884\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": -0.4323,\\\\n              \\\\\\\"p\\\\\\\": 0.332699\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": -0.16,\\\\n              \\\\\\\"p\\\\\\\": 0.762117\\\\n            }\\\\n          ]\\\\n        },\\\\n        \\\\\\\"diff_xcorr\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"diff_xcorr\\\\\\\",\\\\n          \\\\\\\"peak_lag\\\\\\\": 5,\\\\n          \\\\\\\"r\\\\\\\": 0.6252,\\\\n          \\\\\\\"p_value\\\\\\\": 0.259368,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"all_lags\\\\\\\": [\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -5,\\\\n              \\\\\\\"r\\\\\\\": -0.1829,\\\\n              \\\\\\\"p\\\\\\\": 0.768468\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -4,\\\\n              \\\\\\\"r\\\\\\\": 0.2003,\\\\n              \\\\\\\"p\\\\\\\": 0.703513\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -3,\\\\n              \\\\\\\"r\\\\\\\": -0.3273,\\\\n              \\\\\\\"p\\\\\\\": 0.473677\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -2,\\\\n              \\\\\\\"r\\\\\\\": -0.0482,\\\\n              \\\\\\\"p\\\\\\\": 0.909796\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": -1,\\\\n              \\\\\\\"r\\\\\\\": -0.1714,\\\\n              \\\\\\\"p\\\\\\\": 0.659217\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 0,\\\\n              \\\\\\\"r\\\\\\\": -0.1035,\\\\n              \\\\\\\"p\\\\\\\": 0.775986\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 1,\\\\n              \\\\\\\"r\\\\\\\": -0.1023,\\\\n              \\\\\\\"p\\\\\\\": 0.793427\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 2,\\\\n              \\\\\\\"r\\\\\\\": 0.4906,\\\\n              \\\\\\\"p\\\\\\\": 0.217088\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 3,\\\\n              \\\\\\\"r\\\\\\\": 0.2792,\\\\n              \\\\\\\"p\\\\\\\": 0.544288\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 4,\\\\n              \\\\\\\"r\\\\\\\": 0.0002,\\\\n              \\\\\\\"p\\\\\\\": 0.999657\\\\n            },\\\\n            {\\\\n              \\\\\\\"lag\\\\\\\": 5,\\\\n              \\\\\\\"r\\\\\\\": 0.6252,\\\\n              \\\\\\\"p\\\\\\\": 0.259368\\\\n            }\\\\n          ],\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.259368,\\\\n          \\\\\\\"significant_fdr\\\\\\\": false\\\\n        },\\\\n        \\\\\\\"threshold_onset\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"threshold_onset\\\\\\\",\\\\n          \\\\\\\"canary_onset\\\\\\\": null,\\\\n          \\\\\\\"downstream_onset\\\\\\\": 4,\\\\n          \\\\\\\"lead_time\\\\\\\": null,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"threshold\\\\\\\": \\\\\\\"true_3sigma_d105\\\\\\\"\\\\n        },\\\\n        \\\\\\\"perm_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"perm_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": 0.2711,\\\\n          \\\\\\\"p_value\\\\\\\": 0.628074,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"p_fdr\\\\\\\": 0.981604,\\\\n          \\\\\\\"significant_fdr\\\\\\\": false\\\\n        },\\\\n        \\\\\\\"ty_granger\\\\\\\": {\\\\n          \\\\\\\"method\\\\\\\": \\\\\\\"ty_granger\\\\\\\",\\\\n          \\\\\\\"f_stat\\\\\\\": null,\\\\n          \\\\\\\"p_value\\\\\\\": null,\\\\n          \\\\\\\"significant\\\\\\\": false,\\\\n          \\\\\\\"error\\\\\\\": \\\\\\\"VARResults.test_causality() got an unexpected keyword argument 'signonly'\\\\\\\",\\\\n          \\\\\\\"order\\\\\\\": 1,\\\\n          \\\\\\\"k_opt\\\\\\\": 1,\\\\n          \\\\\\\"d_max\\\\\\\": 0\\\\n        }\\\\n      }\\\\n    }\\\\n  ],\\\\n  \\\\\\\"consensus\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<distinct_1\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<distinct_2\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<distinct_3\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy<mauve\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 0,\\\\n      \\\\\\\"methods\\\\\\\": []\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<distinct_1\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<distinct_2\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<distinct_3\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 3,\\\\n      \\\\\\\"methods\\\\\\\": [\\\\n        \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"diff\\\\\\\",\\\\n        \\\\\\\"perm\\\\\\\"\\\\n      ]\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair\\\\\\\": \\\\\\\"ece<mauve\\\\\\\",\\\\n      \\\\\\\"votes\\\\\\\": 0,\\\\n      \\\\\\\"methods\\\\\\\": []\\\\n    }\\\\n  ],\\\\n  \\\\\\\"summary\\\\\\\": {\\\\n    \\\\\\\"perm_granger_fdr_forward_sig\\\\\\\": 6,\\\\n    \\\\\\\"perm_granger_fdr_reverse_sig\\\\\\\": 0,\\\\n    \\\\\\\"diff_xcorr_fdr_forward_sig\\\\\\\": 6,\\\\n    \\\\\\\"diff_xcorr_fdr_reverse_sig\\\\\\\": 6,\\\\n    \\\\\\\"threshold_forward_sig\\\\\\\": 0,\\\\n    \\\\\\\"ty_forward_sig\\\\\\\": 0,\\\\n    \\\\\\\"robust_pairs\\\\\\\": 6\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.94}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 1.0,\\n    \\\"seed\\\": 42,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"results/padding_robustness/a100_s42_fp32\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.9915,\\n          \\\"p_value\\\": 0.0,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.9052,\\n              \\\"p\\\": 0.013041\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.6205,\\n              \\\"p\\\": 0.137094\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.9753,\\n              \\\"p\\\": 3.7e-05\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.9914,\\n              \\\"p\\\": 0.0\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.9915,\\n              \\\"p\\\": 0.0\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.8601,\\n              \\\"p\\\": 0.000684\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.8649,\\n              \\\"p\\\": 0.001235\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.8376,\\n              \\\"p\\\": 0.004832\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.6115,\\n              \\\"p\\\": 0.107199\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.7333,\\n              \\\"p\\\": 0.06073\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.4505,\\n              \\\"p\\\": 0.370007\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.9887,\\n          \\\"p_value\\\": 0.0,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.7514,\\n              \\\"p\\\": 0.14314\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.4602,\\n              \\\"p\\\": 0.358416\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.9191,\\n              \\\"p\\\": 0.003422\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.9886,\\n              \\\"p\\\": 4e-06\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.9887,\\n              \\\"p\\\": 0.0\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.1676,\\n              \\\"p\\\": 0.643447\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.141,\\n              \\\"p\\\": 0.717391\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.1835,\\n              \\\"p\\\": 0.663583\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": -0.4009,\\n              \\\"p\\\": 0.372798\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.6846,\\n              \\\"p\\\": 0.133539\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.4432,\\n              \\\"p\\\": 0.45478\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.0,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": 2,\\n          \\\"downstream_onset\\\": null,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 461.551,\\n          \\\"p_value\\\": 0.004599,\\n          \\\"significant\\\": true,\\n          \\\"p_fdr\\\": 0.006132,\\n          \\\"significant_fdr\\\": true\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n          \\\"f_stat\\\": null,\\n\\n\\n... [截断: 输出过长，省略 53234 字符] ...\\n\\n              \\\"r\\\": 0.2991,\\n              \\\"p\\\": 0.434241\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": -0.2046,\\n              \\\"p\\\": 0.626884\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": -0.4323,\\n              \\\"p\\\": 0.332699\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": -0.16,\\n              \\\"p\\\": 0.762117\\n            }\\n          ]\\n        },\\n        \\\"diff_xcorr\\\": {\\n          \\\"method\\\": \\\"diff_xcorr\\\",\\n          \\\"peak_lag\\\": 5,\\n          \\\"r\\\": 0.6252,\\n          \\\"p_value\\\": 0.259368,\\n          \\\"significant\\\": false,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": -0.1829,\\n              \\\"p\\\": 0.768468\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.2003,\\n              \\\"p\\\": 0.703513\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": -0.3273,\\n              \\\"p\\\": 0.473677\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": -0.0482,\\n              \\\"p\\\": 0.909796\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": -0.1714,\\n              \\\"p\\\": 0.659217\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": -0.1035,\\n              \\\"p\\\": 0.775986\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": -0.1023,\\n              \\\"p\\\": 0.793427\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.4906,\\n              \\\"p\\\": 0.217088\\n            },\\n            {\\n              \\\"lag\\\": 3,\\n              \\\"r\\\": 0.2792,\\n              \\\"p\\\": 0.544288\\n            },\\n            {\\n              \\\"lag\\\": 4,\\n              \\\"r\\\": 0.0002,\\n              \\\"p\\\": 0.999657\\n            },\\n            {\\n              \\\"lag\\\": 5,\\n              \\\"r\\\": 0.6252,\\n              \\\"p\\\": 0.259368\\n            }\\n          ],\\n          \\\"p_fdr\\\": 0.259368,\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"method\\\": \\\"threshold_onset\\\",\\n          \\\"canary_onset\\\": null,\\n          \\\"downstream_onset\\\": 4,\\n          \\\"lead_time\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"threshold\\\": \\\"true_3sigma_d105\\\"\\n        },\\n        \\\"perm_granger\\\": {\\n          \\\"method\\\": \\\"perm_granger\\\",\\n          \\\"f_stat\\\": 0.2711,\\n          \\\"p_value\\\": 0.628074,\\n          \\\"significant\\\": false,\\n          \\\"p_fdr\\\": 0.981604,\\n          \\\"significant_fdr\\\": false\\n        },\\n        \\\"ty_granger\\\": {\\n          \\\"method\\\": \\\"ty_granger\\\",\\n          \\\"f_stat\\\": null,\\n          \\\"p_value\\\": null,\\n          \\\"significant\\\": false,\\n          \\\"error\\\": \\\"VARResults.test_causality() got an unexpected keyword argument 'signonly'\\\",\\n          \\\"order\\\": 1,\\n          \\\"k_opt\\\": 1,\\n          \\\"d_max\\\": 0\\n        }\\n      }\\n    }\\n  ],\\n  \\\"consensus\\\": [\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_2\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_3\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<mauve\\\",\\n      \\\"votes\\\": 0,\\n      \\\"methods\\\": []\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_2\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_3\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<mauve\\\",\\n      \\\"votes\\\": 0,\\n      \\\"methods\\\": []\\n    }\\n  ],\\n  \\\"summary\\\": {\\n    \\\"perm_granger_fdr_forward_sig\\\": 6,\\n    \\\"perm_granger_fdr_reverse_sig\\\": 0,\\n    \\\"diff_xcorr_fdr_forward_sig\\\": 6,\\n    \\\"diff_xcorr_fdr_reverse_sig\\\": 6,\\n    \\\"threshold_forward_sig\\\": 0,\\n    \\\"ty_forward_sig\\\": 0,\\n    \\\"robust_pairs\\\": 6\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.94}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-20T06:04:13.467Z_

<details><summary>↩ Tool result · `toolu_011gzqAMHiMnL2JVDmDx9LFk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3816}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "2296aa57-fb84-40ef-bbc2-d2c793744f0a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3816}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3816}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
The registry query for `generalize_pythia410m_wiki_a100_s42` returned empty. Let me search with a broader filter to find the wiki α=1.0 experiment.

Now let me compile the results:

### c4_a025_s42_fp32 (α=0.25, C4)
- PermG_fwd: 0/8 (FDR all 0.094)
- PermG_rev: 0/8
- threshold_onset: 2/8 sig (onset lead_time: -1 and -2 for ent/ece&lt;d1; 6/5 for ent/ece&lt;d3 — but these have lead > 0 meaning downstream leads canary, so not forward)


- Looking at the output table more carefully, the Onset column shows -1, None, 6, None, and - for the c4_a025_s42 results, where negative values indicate the canary onset precedes the downstream onset.
- The JSON confirms this pattern: token_entropy shows canary_onset=3, downstream_onset=2 (lead_time=-1), and ece shows canary_onset=3, downstream_onset=1 (lead_time=-2), but both are marked as not significant.
- I'm realizing the threshold_onset significance field operates differently than I expected—checking the summary data shows c4_a025 has threshold forward sig=2 while c4_a050, c4_a075, and padding all have 0, suggesting this is what actually determines whether the onset detection is meaningful.
- Now I'm compiling the final summary table with all the key metrics across experiments.

Generating markdown table...

I'm realizing that K≥4 consensus is impossible across all experiments since the maximum possible votes is 3 out of 5 (from naive, differential, and permutation methods), with TY always unavailable and threshold voting at zero for higher alpha values. So K≥4 will be zero across the board.

Now I need to look up the α=1.0 experiment in the registry to find the specific experiment ID.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "fad3385e-fdad-44b3-bd56-14a74ff6471d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149hqAMk9aev8pJrajTUnez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19278,
      "cache_read_input_tokens": 40537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19278
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

_source line 49_

Registry 中未找到 `generalize_pythia410m_wiki_a100_s42`。搜索所有 α=1.0 实验对比 padding。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "b9144fb9-6c75-4f48-9010-63c3a37421fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149hqAMk9aev8pJrajTUnez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19278,
      "cache_read_input_tokens": 40537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19278
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

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01HAoydW7HBN8qHw8GgyhsNv`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "limit": 50,
  "fields": [
    "exp_id",
    "status",
    "metrics"
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
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "fe25a888-bd69-4f11-b792-d5a6c62728d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149hqAMk9aev8pJrajTUnez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19278,
      "cache_read_input_tokens": 40537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19278
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

_source line 51 · 2026-05-20T06:04:40.203Z_

<details><summary>↩ Tool result · `toolu_01HAoydW7HBN8qHw8GgyhsNv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"interv_pred_a075_s42\": {\"status\": \"DONE\"}, \"alpha_sweep_a045_s43_fp32\": {\"status\": \"RUNNING\"}, \"scale_14b_a050_s42_fp32\": {\"status\": \"RUNNING\"}, \"interv_pred_14b_s42_fp32\": {\"status\": \"DONE\"}, \"data_strategy_ablation_s43\": {\"status\": \"RUNNING\", \"metrics\": {\"data_strategy\": \"accumulate\", \"baseline_exp\": \"alpha_sweep_a050_s43_fp32\"}}, \"data_strategy_ablation_s42\": {\"status\": \"RUNNING\"}, \"generalize_pythia14b_wiki_a100_s43\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"3x_sigma_drift→true_3sigma\", \"K3_3sigma_m037\": \"3/8\", \"K3_3sigma_d111_detail\": \"naive=0/8 diff=6/8 thr3s=0/8 pg=6/8 ty=3/8\", \"note\": \"D111 reduces K3 from 6/8 to 3/8 (all naive peak_lag>0)\"}}, \"generalize_pythia14b_wiki_a100_s42\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"3x_sigma_drift→true_3sigma\", \"K3_3sigma_m037\": \"1/8\", \"K3_3sigma_d111_detail\": \"naive=6/8 diff=6/8 thr3s=0/8 pg=2/8 ty=0/8\"}}, \"pythia410m_wiki_a100_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"unknown→true_3sigma\", \"K3_3sigma_m037\": \"6/8\", \"K3_3sigma_d111_detail\": \"naive=6/8 diff=6/8 thr3s=0/8 pg=6/8 ty=6/8\", \"caveat\": \"xcorr recomputed from raw metrics without FDR\"}}, \"alpha_sweep_a050_postd093_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"unknown→true_3sigma\", \"K3_3sigma_m037\": \"3/8\", \"K3_3sigma_d111_detail\": \"naive=3/8 diff=2/8 thr3s=0/8 pg=6/8 ty=4/8\"}}, \"generalize_pythia1b_c4_a100_s43\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"3x_sigma_drift→true_3sigma\", \"K3_3sigma_m037\": \"6/8\", \"K3_3sigma_d111_detail\": \"naive=4/8 diff=8/8 thr3s=2/8 pg=8/8 ty=4/8\"}}, \"opt13b_wiki_a100_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"already_3sigma_d105\", \"K3_3sigma_m037\": \"6/8\", \"K3_3sigma_d111_detail\": \"naive=8/8 diff=6/8 thr3s=0/8 pg=6/8 ty=5/8\"}}, \"generalize_opt1b_wiki_a100_s42\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"3x_sigma_drift→true_3sigma\", \"K3_3sigma_m037\": \"6/8\", \"K3_3sigma_d111_detail\": \"naive=7/8 diff=6/8 thr3s=2/8 pg=6/8 ty=0/8\"}}, \"gen_gpt2m_a100_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"3x_sigma_drift→true_3sigma\", \"K3_3sigma_m037\": \"6/8\", \"K3_3sigma_d111_detail\": \"naive=7/8 diff=6/8 thr3s=0/8 pg=6/8 ty=4/8\"}}, \"generalize_pythia410m_wiki_a100_s42\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"3x_sigma_drift→true_3sigma\", \"K3_3sigma_m037\": \"6/8\", \"K3_3sigma_d111_detail\": \"naive=7/8 diff=6/8 thr3s=2/8 pg=6/8 ty=1/8\"}}, \"c4_a050_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"8/8\", \"PermG_rev\": \"1/8\", \"K_ge_3_3sigma\": \"3/8\", \"K_ge_4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"0/8\", \"naive_xcorr\": \"4/8\", \"diff_xcorr\": \"6/8\", \"TY_granger\": \"0/8\", \"drift_token_entropy\": -47.98, \"drift_ece\": 3102.5, \"drift_perplexity\": 2957.1, \"drift_distinct_1\": -9.9, \"drift_distinct_2\": -16, \"drift_distinct_3\": -17.5, \"drift_mauve\": -47.5, \"drift_effective_rank\": 113.4, \"gen0_token_entropy\": 3.1094, \"D111_direction_check\": \"applied: naive_xcorr peak_lag<0, diff_xcorr peak_lag<0\", \"D102_8pair\": \"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\", \"D105_3sigma\": \"true 3sigma (std of full series)\", \"analysis_script\": \"run_5method_analysis_d102.py + D105 inline recompute\", \"n_perm\": 5000}}, \"c4_a075_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"8/8\", \"PermG_rev\": \"0/8\", \"K_ge_3_3sigma\": \"8/8\", \"K_ge_4_3sigma\": \"1/8\", \"threshold_onset_3sigma\": \"0/8\", \"naive_xcorr\": \"8/8\", \"diff_xcorr\": \"8/8\", \"TY_granger\": \"1/8\", \"drift_token_entropy\": -34.12, \"drift_ece\": 2781.6, \"drift_perplexity\": 2149.2, \"drift_distinct_1\": -12.6, \"drift_distinct_2\": -16.2, \"drift_distinct_3\": -15.7, \"drift_mauve\": -52.8, \"drift_effective_rank\": 111, \"gen0_token_entropy\": 3.1094, \"D111_direction_check\": \"applied: naive_xcorr peak_lag<0, diff_xcorr peak_lag<0\", \"D102_8pair\": \"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\", \"D105_3sigma\": \"true 3sigma (std of full series)\", \"analysis_script\": \"run_5method_analysis_d102.py + D105 inline recompute\", \"n_perm\": 5000}}, \"alpha_sweep_a075_s43\": {\"status\": \"DONE\", \"metrics\": {\"gen0\": {\"token_entropy\": 3.234, \"ece\": 0.0108, \"perplexity\": 26.95, \"distinct_1\": 0.0983, \"distinct_2\": 0.5132, \"distinct_3\": 0.8057, \"effective_rank\": 46.61, \"mauve\": 0.0335}, \"gen10\": {\"token_entropy\": 2.349, \"ece\": 0.204, \"perplexity\": 76.08, \"distinct_1\": 0.0666, \"distinct_2\": 0.2984, \"distinct_3\": 0.4838, \"effective_rank\": 79.4, \"mauve\": 0.0289}, \"drift_pct\": {\"token_entropy\": -27.38, \"ece\": 1791.96, \"perplexity\": 182.3, \"distinct_1\": -32.3, \"distinct_2\": -41.86, \"distinct_3\": -39.96, \"effective_rank\": 70.36, \"mauve\": -13.63}, \"PermG_fwd\": \"5/8\", \"PermG_rev\": \"0/8\", \"naive_xcorr_fwd_D111\": \"2/8\", \"diff_xcorr_fwd_D111\": \"6/8\", \"threshold_onset_3sigma\": \"8/8\", \"TY_granger\": \"6/8\", \"K3_3sigma\": \"7/8\", \"K4_3sigma\": \"5/8\", \"perm_granger_fdr_forward_sig\": \"5/8\", \"D105_D111_compliant\": true, \"M035_direction\": \"peak_lag < 0\", \"precision\": \"fp32\", \"n_perm\": 5000, \"pair_config\": \"canary=[token_entropy,ece] x downstream=[distinct_1,distinct_2,distinct_3,mauve]\"}}, \"alpha_sweep_a050_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"token_entropy_gen0\": 3.2342, \"token_entropy_gen10\": 2.7227, \"token_entropy_drift_pct\": -15.81, \"ece_gen0\": 0.0108, \"ece_gen10\": 0.0842, \"ece_drift_pct\": 679.56, \"distinct_1_gen0\": 0.0929, \"distinct_1_gen10\": 0.066, \"distinct_1_drift_pct\": -29, \"perplexity_gen0\": 26.95, \"perplexity_gen10\": 31.58, \"perplexity_drift_pct\": 17.17, \"mauve_drift_pct\": -23.54, \"PermG_fwd\": \"6/8\", \"PermG_rev\": \"0/8\", \"naive_xcorr_fwd_D111\": \"2/8\", \"diff_xcorr_fwd_D111\": \"6/8\", \"threshold_onset_3sigma\": \"8/8\", \"TY_granger\": \"5/8\", \"K3_3sigma\": \"6/8\", \"K4_3sigma\": \"5/8\", \"perm_granger_fdr_forward_sig\": \"6/8\", \"D105_D111_compliant\": true, \"M035_direction\": \"peak_lag < 0\", \"precision\": \"fp32\", \"n_perm\": 5000, \"pair_config\": \"canary=[token_entropy,ece] x downstream=[distinct_1,distinct_2,distinct_3,mauve]\"}}, \"alpha_sweep_a060_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"perm_granger_fwd_fdr\": \"0/8\", \"perm_granger_rev_fdr\": \"0/8\", \"consensus_k4_3sigma\": \"3/8\", \"consensus_k3_3sigma\": \"7/8\", \"threshold_onset_3sigma\": \"8/8\", \"naive_xcorr\": \"7/8\", \"diff_xcorr_fdr\": \"6/8\", \"ty_granger\": \"4/8\", \"drift_pct\": {\"token_entropy\": -28.61, \"distinct_1\": -31.02, \"distinct_2\": -39.02, \"distinct_3\": -37.3, \"ece\": 1530.81, \"perplexity\": 85.11, \"mauve\": -10.96, \"effective_rank\": 61}, \"gen0\": {\"token_entropy\": 3.234, \"perplexity\": 26.949, \"distinct_1\": 0.098}, \"gen9\": {\"token_entropy\": 2.309, \"perplexity\": 49.885, \"distinct_1\": 0.068}, \"note\": \"T=10 (gen_0-9, gen_10 timeout EXIT_CODE=124), D108 non-monotonicity confirmed\"}}, \"generalize_pythia1b_c4_a100_s42\": {\"status\": \"DONE\", \"metrics\": {\"D102_reanalysis\": \"→mauve (replacing →ppl)\", \"pair_config\": \"canary=[token_entropy,ece] × downstream=[distinct_1,distinct_2,distinct_3,mauve]\", \"n_perm\": 5000, \"perm_granger_fdr_forward_sig\": \"8/8\", \"diff_xcorr_fdr_forward_sig\": \"8/8\", \"threshold_forward_sig\": \"8/8\", \"ty_forward_sig\": \"4/8\", \"robust_pairs_K3\": \"8/8\", \"robust_pairs_K4\": \"8/8\", \"D102_note\": \"ppl→mauve统一后: robust 2→8, perm_fdr 6→8, diff_fdr 6→8, ty 1→4.\", \"K_ge3_D116\": \"~1/8\", \"K_ge4_D116\": \"0/8\", \"D116_note\": \"D105+D111 joint: threshold JSON 3x_sigma_drift=8/8 but registry threshold_onset_3sigma=0/8 (M034). D111 kills diff_fwd. Reviewer estimate ~1/8.\"}}, \"alpha_sweep_a000_s42\": {\"status\": \"DONE\", \"metrics\": {\"gen0_token_entropy\": 3.2342, \"gen10_token_entropy\": 3.0693, \"gen0_ece\": 0.0108, \"gen10_ece\": 0.0164, \"gen0_perplexity\": 26.95, \"gen10_perplexity\": 21.11, \"gen0_distinct_1\": 0.0982, \"gen10_distinct_1\": 0.0847, \"token_entropy_drift_pct\": -5.1, \"ece_drift_pct\": 51.7, \"perplexity_drift_pct\": -21.7, \"distinct_1_drift_pct\": -13.8, \"distinct_2_drift_pct\": -9.8, \"distinct_3_drift_pct\": -4.5, \"gen1_10_perplexity_drift_pct\": 9.4, \"gen1_10_distinct_1_drift_pct\": -13.1, \"gen1_10_entropy_drift_pct\": 2.6}}, \"smollm3_3b_wiki_a100_s43_fp32\": {\"status\": \"RUNNING\"}, \"padding_robustness_a100_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"robust_pairs_K4_3sigma\": \"6/8\", \"robust_pairs_K3_3sigma\": \"6/8\", \"threshold_onset_3sigma\": \"0/8\", \"D105_3sigma_note\": \"True 3sigma recompute. threshold_onset dropped 5/8->0/8. K4 unchanged at 6/8. PermG/TY unchanged.\"}}, \"alpha_sweep_a075_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"n_generations\": 11, \"gen0\": {\"token_entropy\": 3.2342, \"ece\": 0.0108, \"perplexity\": 26.949, \"distinct_1\": 0.098, \"distinct_2\": 0.5141, \"distinct_3\": 0.8127, \"effective_rank\": 46.613, \"mauve\": 0.0311}, \"gen10\": {\"token_entropy\": 2.283, \"ece\": 0.2145, \"perplexity\": 77.697, \"distinct_1\": 0.0731, \"distinct_2\": 0.357, \"distinct_3\": 0.5957, \"effective_rank\": 78.06, \"mauve\": 0.0299}, \"drift_pct\": {\"token_entropy\": -29.41, \"ece\": 1885.41, \"perplexity\": 188.31, \"distinct_1\": -25.38, \"distinct_2\": -30.55, \"distinct_3\": -26.7, \"effective_rank\": 67.47, \"mauve\": -3.73}, \"lead_lag\": {\"PermG_fwd\": \"6/8\", \"PermG_rev\": \"0/8\", \"K_ge_4\": \"6/8\", \"MMCT_detection\": 0.75, \"TY_granger\": \"8/8\", \"naive_xcorr\": \"7/8\", \"diff_xcorr\": \"6/8\", \"threshold_onset\": \"8/8\"}, \"asymmetry\": \"strong (fwd=6, rev=0)\"}}, \"alpha_sweep_a060_s42_fp32_v3\": {\"status\": \"DONE\", \"metrics\": {\"final_ppl\": 45.41, \"final_entropy\": 2.48, \"final_eff_rank\": 69.3, \"final_mauve\": 0.023, \"precision\": \"fp32\", \"token_entropy_drift\": -23.36, \"ece_drift\": 1260.23, \"perplexity_drift\": 68.52, \"distinct_1_drift\": -28.17, \"distinct_2_drift\": -37.22, \"distinct_3_drift\": -35.35, \"perm_granger_fwd\": \"3/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"8/8\", \"threshold_onset_fwd\": \"8/8\", \"consensus_k4\": \"7/8\", \"mmct_wpair_fwd\": 0.875}}, \"alpha_sweep_a050_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"token_entropy_gen0\": 3.2342, \"token_entropy_gen10\": 2.7075, \"token_entropy_drift_pct\": -16.3, \"distinct_1_gen0\": 0.0916, \"distinct_1_gen10\": 0.0649, \"distinct_1_drift_pct\": -29.2, \"perplexity_gen0\": 26.95, \"perplexity_gen10\": 31.46, \"perplexity_drift_pct\": 16.8, \"ece_gen0\": 0.0108, \"ece_gen10\": 0.0868, \"ece_drift_pct\": 703.4, \"perm_granger_fwd\": \"6/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"4/8\", \"consensus_k4\": \"6/8\", \"mmct_wpair_fwd\": \"6/8\", \"precision\": \"fp32\", \"n_perm\": 5000, \"padding_side\": \"right (D093 fix NOT applied)\"}}, \"alpha_sweep_a035_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"0/8\", \"PermG_rev\": \"0/8\", \"K_ge3_3sigma\": \"6/8\", \"K_ge4_3sigma\": \"2/8\", \"threshold_onset\": \"8/8\", \"TY_granger\": \"4/8\", \"naive_xcorr_fwd\": \"8/8\", \"diff_xcorr_fwd\": \"4/8\", \"detection_rate_k4\": 0.25, \"drift_pct\": {\"token_entropy\": -18.53, \"ece\": 651.26, \"perplexity\": -1.27, \"distinct_1\": -36.38, \"distinct_2\": -49.45, \"distinct_3\": -50.04, \"effective_rank\": 22.21, \"mauve\": -17.78}, \"gen0\": {\"token_entropy\": 3.234, \"ece\": 0.0108, \"perplexity\": 26.95, \"distinct_1\": 0.098, \"distinct_2\": 0.514, \"distinct_3\": 0.813, \"effective_rank\": 46.61, \"mauve\": 0.0311}, \"gen10\": {\"token_entropy\": 2.635, \"ece\": 0.0812, \"perplexity\": 26.61, \"distinct_1\": 0.0623, \"distinct_2\": 0.26, \"distinct_3\": 0.406, \"effective_rank\": 56.96, \"mauve\": 0.0256}, \"consensus_detail\": {\"K4_pairs\": [\"token_entropy->distinct_1\", \"ece->distinct_1\"], \"K3_pairs\": [\"token_entropy->distinct_2\", \"token_entropy->mauve\", \"ece->distinct_2\", \"ece->mauve\"], \"K2_pairs\": [\"token_entropy->distinct_3\", \"ece->distinct_3\"]}, \"n_generations\": 11, \"precision\": \"fp32\", \"onset_conclusion\": \"PermG=0/8 confirms onset >= 0.35; combined with a040(0/8) and a050(6/8), onset in [0.40, 0.50]\"}}, \"alpha_sweep_a025_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"0/8\", \"PermG_rev\": \"0/8\", \"K_ge_4\": \"0/8\", \"MMCT\": \"0/8\", \"MMCT_detection_rate\": 0, \"d1_drift_pct\": -39.15, \"d2_drift_pct\": -54.75, \"d3_drift_pct\": -56.98, \"mauve_drift_pct\": -41.86, \"entropy_drift_pct\": -4.79, \"ece_drift_pct\": 79.17, \"ppl_drift_pct\": -18.09, \"eff_rank_drift_pct\": -3.78, \"ppl_by_gen\": [26.95, 19.39, 20.37, 20.75, 21.14, 21.3, 21.48, 21.88, 21.9, 22.25, 22.07], \"entropy_by_gen\": [3.234, 2.983, 3.015, 3.039, 3.051, 3.034, 3.049, 3.067, 3.063, 3.104, 3.079], \"d1_by_gen\": [0.098, 0.0976, 0.0815, 0.0737, 0.0688, 0.0657, 0.0635, 0.0614, 0.061, 0.0601, 0.0596], \"mauve_by_gen\": [0.0311, 0.0314, 0.0326, 0.0318, 0.0314, 0.0272, 0.0242, 0.0221, 0.0207, 0.0207, 0.0181], \"naive_xcorr_fwd\": \"8/8\", \"diff_xcorr_fwd\": \"3/8\", \"threshold_onset_fwd\": \"5/8\", \"ty_granger_sig\": \"3/8\", \"consensus_detail_max_votes\": 3, \"hypothesis_validated\": true, \"note\": \"PermG=0/8 confirms α=0.25 is below phase transition. d1_drift=-39.15% is surprisingly large (> α=0.50's -28.7%), suggesting diversity collapse proceeds without Granger-detectable lead-lag at this α. token_entropy→distinct_1 had raw PermG p=0.007 but FDR-corrected p=0.053 (borderline).\"}}, \"alpha_sweep_a010_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"token_entropy_drift_pct\": -4.59, \"distinct_1_drift_pct\": -23.8, \"distinct_2_drift_pct\": -27.15, \"distinct_3_drift_pct\": -19.36, \"perplexity_drift_pct\": -18.94, \"perm_granger_fwd\": \"0/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"3/8\", \"threshold_onset_fwd\": \"5/8\", \"consensus_k4\": \"2/8\", \"mmct_wpair_fwd\": \"2/8\", \"mmct_detection_rate\": 0.25, \"precision\": \"fp32\", \"padding_side_fix\": \"D093 applied\", \"blind_zone_confirmed\": true, \"cross_seed_permg_stable\": true}}, \"alpha_sweep_a005_s42_v3\": {\"status\": \"DONE\", \"metrics\": {\"final_ppl\": 20.81, \"final_entropy\": 3.04, \"final_eff_rank\": 45.3, \"final_mauve\": 0.023, \"precision\": \"fp32\", \"token_entropy_drift\": -5.96, \"ece_drift\": 55.41, \"perplexity_drift\": -22.78, \"distinct_1_drift\": -24.86, \"distinct_2_drift\": -28.42, \"distinct_3_drift\": -19.54, \"perm_granger_fwd\": \"0/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"3/8\", \"threshold_onset_fwd\": \"5/8\", \"consensus_k4\": \"0/8\", \"mmct_wpair_fwd\": 0}}, \"alpha_sweep_a010_s42_bf16\": {\"status\": \"PREPARING\"}, \"scale_14b_a050_s42_bf16\": {\"status\": \"PREPARING\"}, \"interv_react_s43\": {\"status\": \"PREPARING\"}, \"alpha_sweep_a040_s42_fp32_v2\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"0/8\", \"PermG_rev\": \"0/8\", \"K4_3sigma\": \"0/8\", \"K3_3sigma\": \"1/8\", \"threshold_onset_3sigma\": \"8/8\", \"naive_xcorr\": \"4/8\", \"diff_xcorr\": \"0/8\", \"TY_granger\": \"4/8\", \"drift_token_entropy\": \"-19.13%\", \"drift_ece\": \"+736.90%\", \"drift_distinct1\": \"-35.48%\", \"drift_distinct2\": \"-48.01%\", \"drift_distinct3\": \"-48.42%\", \"drift_mauve\": \"-23.04%\", \"drift_perplexity\": \"+5.36%\", \"D111_direction_check\": \"applied: naive 8/8→4/8, diff 3/8→0/8, K3 6/8→1/8, K4 1/8→0/8\"}}, \"alpha_sweep_a030_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"permg_fwd\": \"0/8\", \"permg_rev\": \"0/8\", \"k_ge3\": \"3/8\", \"k_ge4\": \"3/8\", \"naive_xcorr\": \"5/8\", \"diff_xcorr\": \"3/8\", \"threshold_onset\": \"8/8\", \"ty_granger\": \"5/8\", \"drift_entropy_pct\": -17.32, \"drift_ece_pct\": 549.38, \"drift_d1_pct\": -36.72, \"drift_d2_pct\": -49.75, \"drift_d3_pct\": -50.09, \"drift_mauve_pct\": -26.09, \"n_generations\": 11, \"n_perm\": 5000, \"D111_direction_check\": \"applied: naive 8/8→5/8, diff 4/8→3/8, K3 6/8→3/8, K4 unchanged 3/8\"}}, \"alpha_sweep_a045_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"permg_fwd\": 0, \"permg_rev\": 0, \"k_ge3\": 3, \"k_ge4\": 0, \"naive_xcorr\": 7, \"diff_xcorr\": 3, \"threshold_onset\": 8, \"ty_granger\": 1, \"total_pairs\": 8, \"drift_entropy_pct\": -18.73, \"drift_ece_pct\": 770.37, \"drift_d1_pct\": -35.39, \"drift_d2_pct\": -47.87, \"drift_d3_pct\": -47.79, \"drift_perplexity_pct\": 12.19, \"drift_mauve_pct\": -24.89, \"drift_effrank_pct\": 23.41, \"gen0_token_entropy\": 3.2342, \"gen10_token_entropy\": 2.6283, \"gen0_ece\": 0.0108, \"gen10_ece\": 0.094, \"gen0_distinct_1\": 0.098, \"gen10_distinct_1\": 0.0633, \"gen0_perplexity\": 26.949, \"gen10_perplexity\": 30.234, \"gen0_mauve\": 0.0311, \"gen10_mauve\": 0.0234, \"onset_boundary\": \"[0.45, 0.50]\"}}, \"c4_a075_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"8/8\", \"PermG_rev\": \"0/8\", \"K_ge_3_3sigma\": \"6/8\", \"K_ge_4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"8/8\", \"naive_xcorr\": \"0/8\", \"diff_xcorr\": \"0/8\", \"TY_granger\": \"6/8\", \"drift_token_entropy\": -35.32, \"drift_ece\": 2809.23, \"drift_perplexity\": 2152.6, \"drift_distinct_1\": -12.4, \"drift_distinct_2\": -15.41, \"drift_distinct_3\": -14.59, \"drift_mauve\": -42.26, \"drift_effective_rank\": 110.31, \"gen0_token_entropy\": 3.1094, \"D111_direction_check\": \"applied: naive 8/8→0/8, diff 8/8→0/8, K3 8/8→6/8, K4 8/8→0/8\"}}, \"c4_a050_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"permg_fwd_fdr_sig\": \"8/8\", \"permg_rev_fdr_sig\": \"7/8\", \"consensus_K4_3sigma\": \"2/8\", \"consensus_K3_3sigma\": \"6/8\", \"threshold_onset_3sigma\": \"8/8\", \"naive_xcorr_sig\": \"4/8\", \"diff_xcorr_fdr_sig\": \"0/8\", \"ty_granger_sig\": \"4/8\", \"mmct_detection_rate\": 0.75, \"drift_token_entropy_pct\": -47.99, \"drift_distinct1_pct\": -9.78, \"drift_distinct2_pct\": -15.72, \"drift_distinct3_pct\": -17.75, \"drift_perplexity_pct\": 2931.59, \"drift_mauve_pct\": -54.25, \"drift_ece_pct\": 3103.74, \"gen0_token_entropy\": 3.109, \"gen10_token_entropy\": 1.617, \"D111_direction_check\": \"applied: naive 8/8→4/8, diff 8/8→0/8, K3 8/8→6/8, K4 8/8→2/8\"}}, \"c4_a025_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"permg_fwd_fdr\": \"0/8\", \"permg_rev_fdr\": \"0/8\", \"consensus_K3_3sigma\": \"0/8\", \"consensus_K4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"8/8\", \"naive_xcorr\": \"3/8\", \"diff_xcorr\": \"0/8\", \"ty_granger\": \"3/8\", \"drift_token_entropy\": \"-53.01%\", \"drift_ece\": \"+3242.80%\", \"drift_perplexity\": \"+3617.05%\", \"drift_d1\": \"-4.10%\", \"drift_d2\": \"-8.78%\", \"drift_d3\": \"-11.95%\", \"drift_mauve\": \"-52.08%\", \"drift_effective_rank\": \"+111.90%\", \"D111_direction_check\": \"applied: naive 8/8→3/8, diff 8/8→0/8, K3 8/8→0/8, K4 3/8→0/8\"}}, \"scale_14b_c4_s42_fp32\": {\"status\": \"RUNNING\"}, \"method_ablation_phase3\": {\"status\": \"DONE\", \"metrics\": {\"n_alpha_points\": 10, \"alphas\": [0, 0.05, 0.1, 0.25, 0.35, 0.4, 0.5, 0.6, 0.75, 1], \"naive_sig_rates\": [1, 0.875, 0.875, 1, 1, 1, 1, 0.875, 0.875, 1], \"diff_sig_rates\": [0.5, 0.375, 0.75, 0.375, 0.5, 0.375, 0.875, 1, 0.75, 0.75], \"thresh_3sigma_rates\": [0.5, 0.625, 0.625, 0.625, 1, 1, 1, 1, 1, 1], \"permG_fwd_rates\": [0, 0, 0, 0, 0, 0, 0.75, 0.375, 0.75, 0.75], \"permG_rev_rates\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"TY_rates\": [0.25, 0.375, 0.375, 0.375, 0.5, 0.5, 0.5, 1, 1, 0.375], \"K_ge3_rates\": [0.375, 0.375, 0.5, 0.5, 0.75, 0.75, 0.875, 1, 0.875, 0.75], \"K_ge4_rates\": [0, 0, 0.25, 0, 0.25, 0.125, 0.75, 0.875, 0.75, 0.75], \"regime_structure\": {\"null\": \"alpha<=0.40: PermG=0%, naive=87-100% FPR. 11 data points all PermG=0/8\", \"onset\": \"alpha=[0.40,0.50]: PermG jumps 0→75%, K≥4 jumps 0→75%\", \"sync_collapse\": \"alpha=0.60: PermG drops to 37.5% (non-monotonic, D108). BUT K≥4 peaks at 87.5% — TY complements PermG (TY=100% here vs 50% at α=0.50). MMCT multi-method consensus strongest at this α\", \"detection\": \"alpha>=0.75: PermG=75%, TY non-monotonic drop to 37.5-100%\"}, \"claim3_support\": \"strong: 4-regime dose-response with non-monotonic PermG at α=0.60 (sync collapse) and TY complementarity. Method choice directly determines conclusion validity. PermG 0% FPR in null regime = cleanest discriminator.\", \"D105_standard\": \"3sigma + FDR BH + n_perm=5000 + unified 8-pair\"}}, \"smollm3_3b_wiki_a100_s42_v3\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"3/8\", \"PermG_rev\": \"0/8\", \"robust_pairs_K4_3sigma\": \"0/8\", \"robust_pairs_K3_3sigma\": \"0/8\", \"robust_pairs_K3_2sigma\": \"6/8\", \"robust_pairs_K4_2sigma\": \"3/8\", \"threshold_onset_3sigma\": \"0/8\", \"threshold_onset_2sigma\": \"8/8\", \"naive_xcorr\": \"4/8\", \"diff_xcorr\": \"6/8\", \"ty_granger\": \"0/8\", \"note\": \"D105+D111: FDR per-method, 3sigma, direction-checked. K≥3 corrected 3/8→0/8: 3sigma_recompute_v2 had naive_xcorr direction-blind bug (ECE pairs peak_lag<0 wrongly counted). Authoritative source: 5method_leadlag.json with peak_lag>0 check. PermG_fwd=3/8 (ECE→d1/d2/d3 via diff_xcorr+permG). naive_xcorr corrected 8/8→4/8 (entropy pairs only, ECE pairs all lag<0).\"}}, \"gen_gpt2m_a100_s43\": {\"status\": \"PREPARING\"}, \"qwen35_dryrun_launch\": {\"status\": \"PREPARING\"}, \"scale_69b_a100_s43_fp32\": {\"status\": \"PREPARING\"}, \"interv_react_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"trigger_gen\": 2, \"trigger_distinct1_drop_pct\": -15.83, \"gen2_ppl\": 158.22, \"recovery_ppl\": 21.98, \"recovery_complete_by_gen\": 3, \"intervention_metric\": \"distinct_1\", \"intervention_threshold\": 0.1, \"intervention_alpha\": 0, \"gen0\": {\"token_entropy\": 3.234, \"perplexity\": 26.949, \"distinct_1\": 0.098}, \"gen9\": {\"token_entropy\": 3.079, \"perplexity\": 21.357, \"distinct_1\": 0.089}, \"gen10\": {\"token_entropy\": 3.088, \"perplexity\": 21.387, \"distinct_1\": 0.083}, \"note\": \"reactive intervention triggered at gen2 (d1=0.083 < threshold=0.1), alpha 1.0→0.0; ppl spike 26.9→158.2 recovered by gen3 to 22.0; d1 partial recovery 0.098→0.083→0.089\"}}, \"scale_69b_a100_s43\": {\"status\": \"RUNNING\"}, \"qwen35_08b_wiki_a100_s43_fp32\": {\"status\": \"RUNNING\"}, \"generalize_pythia1b_c4_a100_s42_v2\": {\"status\": \"DONE\", \"metrics\": {\"robust_pairs_K4_3sigma\": \"4/8\", \"robust_pairs_K3_3sigma\": \"8/8\", \"threshold_onset_3sigma\": \"0/8\", \"D105_3sigma_note\": \"D105 backfill: true 3sigma, fdr_permethod, unified 8-pair (canary={token_entropy,ece} x downstream={d1,d2,d3,mauve})\"}}}, \"count\": 50, \"total\": 118, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4314}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "e3b41c53-e574-4089-91d9-c66ff1d6fc38",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"interv_pred_a075_s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"alpha_sweep_a045_s43_fp32\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"scale_14b_a050_s42_fp32\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"interv_pred_14b_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"data_strategy_ablation_s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"metrics\\\": {\\\"data_strategy\\\": \\\"accumulate\\\", \\\"baseline_exp\\\": \\\"alpha_sweep_a050_s43_fp32\\\"}}, \\\"data_strategy_ablation_s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"generalize_pythia14b_wiki_a100_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"threshold_onset_3sigma_m037\\\": \\\"3x_sigma_drift→true_3sigma\\\", \\\"K3_3sigma_m037\\\": \\\"3/8\\\", \\\"K3_3sigma_d111_detail\\\": \\\"naive=0/8 diff=6/8 thr3s=0/8 pg=6/8 ty=3/8\\\", \\\"note\\\": \\\"D111 reduces K3 from 6/8 to 3/8 (all naive peak_lag>0)\\\"}}, \\\"generalize_pythia14b_wiki_a100_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"threshold_onset_3sigma_m037\\\": \\\"3x_sigma_drift→true_3sigma\\\", \\\"K3_3sigma_m037\\\": \\\"1/8\\\", \\\"K3_3sigma_d111_detail\\\": \\\"naive=6/8 diff=6/8 thr3s=0/8 pg=2/8 ty=0/8\\\"}}, \\\"pythia410m_wiki_a100_s43_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"threshold_onset_3sigma_m037\\\": \\\"unknown→true_3sigma\\\", \\\"K3_3sigma_m037\\\": \\\"6/8\\\", \\\"K3_3sigma_d111_detail\\\": \\\"naive=6/8 diff=6/8 thr3s=0/8 pg=6/8 ty=6/8\\\", \\\"caveat\\\": \\\"xcorr recomputed from raw metrics without FDR\\\"}}, \\\"alpha_sweep_a050_postd093_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"threshold_onset_3sigma_m037\\\": \\\"unknown→true_3sigma\\\", \\\"K3_3sigma_m037\\\": \\\"3/8\\\", \\\"K3_3sigma_d111_detail\\\": \\\"naive=3/8 diff=2/8 thr3s=0/8 pg=6/8 ty=4/8\\\"}}, \\\"generalize_pythia1b_c4_a100_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"threshold_onset_3sigma_m037\\\": \\\"3x_sigma_drift→true_3sigma\\\", \\\"K3_3sigma_m037\\\": \\\"6/8\\\", \\\"K3_3sigma_d111_detail\\\": \\\"naive=4/8 diff=8/8 thr3s=2/8 pg=8/8 ty=4/8\\\"}}, \\\"opt13b_wiki_a100_s43_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"threshold_onset_3sigma_m037\\\": \\\"already_3sigma_d105\\\", \\\"K3_3sigma_m037\\\": \\\"6/8\\\", \\\"K3_3sigma_d111_detail\\\": \\\"naive=8/8 diff=6/8 thr3s=0/8 pg=6/8 ty=5/8\\\"}}, \\\"generalize_opt1b_wiki_a100_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"threshold_onset_3sigma_m037\\\": \\\"3x_sigma_drift→true_3sigma\\\", \\\"K3_3sigma_m037\\\": \\\"6/8\\\", \\\"K3_3sigma_d111_detail\\\": \\\"naive=7/8 diff=6/8 thr3s=2/8 pg=6/8 ty=0/8\\\"}}, \\\"gen_gpt2m_a100_s43_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"threshold_onset_3sigma_m037\\\": \\\"3x_sigma_drift→true_3sigma\\\", \\\"K3_3sigma_m037\\\": \\\"6/8\\\", \\\"K3_3sigma_d111_detail\\\": \\\"naive=7/8 diff=6/8 thr3s=0/8 pg=6/8 ty=4/8\\\"}}, \\\"generalize_pythia410m_wiki_a100_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"threshold_onset_3sigma_m037\\\": \\\"3x_sigma_drift→true_3sigma\\\", \\\"K3_3sigma_m037\\\": \\\"6/8\\\", \\\"K3_3sigma_d111_detail\\\": \\\"naive=7/8 diff=6/8 thr3s=2/8 pg=6/8 ty=1/8\\\"}}, \\\"c4_a050_s43_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"PermG_fwd\\\": \\\"8/8\\\", \\\"PermG_rev\\\": \\\"1/8\\\", \\\"K_ge_3_3sigma\\\": \\\"3/8\\\", \\\"K_ge_4_3sigma\\\": \\\"0/8\\\", \\\"threshold_onset_3sigma\\\": \\\"0/8\\\", \\\"naive_xcorr\\\": \\\"4/8\\\", \\\"diff_xcorr\\\": \\\"6/8\\\", \\\"TY_granger\\\": \\\"0/8\\\", \\\"drift_token_entropy\\\": -47.98, \\\"drift_ece\\\": 3102.5, \\\"drift_perplexity\\\": 2957.1, \\\"drift_distinct_1\\\": -9.9, \\\"drift_distinct_2\\\": -16, \\\"drift_distinct_3\\\": -17.5, \\\"drift_mauve\\\": -47.5, \\\"drift_effective_rank\\\": 113.4, \\\"gen0_token_entropy\\\": 3.1094, \\\"D111_direction_check\\\": \\\"applied: naive_xcorr peak_lag<0, diff_xcorr peak_lag<0\\\", \\\"D102_8pair\\\": \\\"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\\\", \\\"D105_3sigma\\\": \\\"true 3sigma (std of full series)\\\", \\\"analysis_script\\\": \\\"run_5method_analysis_d102.py + D105 inline recompute\\\", \\\"n_perm\\\": 5000}}, \\\"c4_a075_s43_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"PermG_fwd\\\": \\\"8/8\\\", \\\"PermG_rev\\\": \\\"0/8\\\", \\\"K_ge_3_3sigma\\\": \\\"8/8\\\", \\\"K_ge_4_3sigma\\\": \\\"1/8\\\", \\\"threshold_onset_3sigma\\\": \\\"0/8\\\", \\\"naive_xcorr\\\": \\\"8/8\\\", \\\"diff_xcorr\\\": \\\"8/8\\\", \\\"TY_granger\\\": \\\"1/8\\\", \\\"drift_token_entropy\\\": -34.12, \\\"drift_ece\\\": 2781.6, \\\"drift_perplexity\\\": 2149.2, \\\"drift_distinct_1\\\": -12.6, \\\"drift_distinct_2\\\": -16.2, \\\"drift_distinct_3\\\": -15.7, \\\"drift_mauve\\\": -52.8, \\\"drift_effective_rank\\\": 111, \\\"gen0_token_entropy\\\": 3.1094, \\\"D111_direction_check\\\": \\\"applied: naive_xcorr peak_lag<0, diff_xcorr peak_lag<0\\\", \\\"D102_8pair\\\": \\\"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\\\", \\\"D105_3sigma\\\": \\\"true 3sigma (std of full series)\\\", \\\"analysis_script\\\": \\\"run_5method_analysis_d102.py + D105 inline recompute\\\", \\\"n_perm\\\": 5000}}, \\\"alpha_sweep_a075_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"gen0\\\": {\\\"token_entropy\\\": 3.234, \\\"ece\\\": 0.0108, \\\"perplexity\\\": 26.95, \\\"distinct_1\\\": 0.0983, \\\"distinct_2\\\": 0.5132, \\\"distinct_3\\\": 0.8057, \\\"effective_rank\\\": 46.61, \\\"mauve\\\": 0.0335}, \\\"gen10\\\": {\\\"token_entropy\\\": 2.349, \\\"ece\\\": 0.204, \\\"perplexity\\\": 76.08, \\\"distinct_1\\\": 0.0666, \\\"distinct_2\\\": 0.2984, \\\"distinct_3\\\": 0.4838, \\\"effective_rank\\\": 79.4, \\\"mauve\\\": 0.0289}, \\\"drift_pct\\\": {\\\"token_entropy\\\": -27.38, \\\"ece\\\": 1791.96, \\\"perplexity\\\": 182.3, \\\"distinct_1\\\": -32.3, \\\"distinct_2\\\": -41.86, \\\"distinct_3\\\": -39.96, \\\"effective_rank\\\": 70.36, \\\"mauve\\\": -13.63}, \\\"PermG_fwd\\\": \\\"5/8\\\", \\\"PermG_rev\\\": \\\"0/8\\\", \\\"naive_xcorr_fwd_D111\\\": \\\"2/8\\\", \\\"diff_xcorr_fwd_D111\\\": \\\"6/8\\\", \\\"threshold_onset_3sigma\\\": \\\"8/8\\\", \\\"TY_granger\\\": \\\"6/8\\\", \\\"K3_3sigma\\\": \\\"7/8\\\", \\\"K4_3sigma\\\": \\\"5/8\\\", \\\"perm_granger_fdr_forward_sig\\\": \\\"5/8\\\", \\\"D105_D111_compliant\\\": true, \\\"M035_direction\\\": \\\"peak_lag < 0\\\", \\\"precision\\\": \\\"fp32\\\", \\\"n_perm\\\": 5000, \\\"pair_config\\\": \\\"canary=[token_entropy,ece] x downstream=[distinct_1,distinct_2,distinct_3,mauve]\\\"}}, \\\"alpha_sweep_a050_s43_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"token_entropy_gen0\\\": 3.2342, \\\"token_entropy_gen10\\\": 2.7227, \\\"token_entropy_drift_pct\\\": -15.81, \\\"ece_gen0\\\": 0.0108, \\\"ece_gen10\\\": 0.0842, \\\"ece_drift_pct\\\": 679.56, \\\"distinct_1_gen0\\\": 0.0929, \\\"distinct_1_gen10\\\": 0.066, \\\"distinct_1_drift_pct\\\": -29, \\\"perplexity_gen0\\\": 26.95, \\\"perplexity_gen10\\\": 31.58, \\\"perplexity_drift_pct\\\": 17.17, \\\"mauve_drift_pct\\\": -23.54, \\\"PermG_fwd\\\": \\\"6/8\\\", \\\"PermG_rev\\\": \\\"0/8\\\", \\\"naive_xcorr_fwd_D111\\\": \\\"2/8\\\", \\\"diff_xcorr_fwd_D111\\\": \\\"6/8\\\", \\\"threshold_onset_3sigma\\\": \\\"8/8\\\", \\\"TY_granger\\\": \\\"5/8\\\", \\\"K3_3sigma\\\": \\\"6/8\\\", \\\"K4_3sigma\\\": \\\"5/8\\\", \\\"perm_granger_fdr_forward_sig\\\": \\\"6/8\\\", \\\"D105_D111_compliant\\\": true, \\\"M035_direction\\\": \\\"peak_lag < 0\\\", \\\"precision\\\": \\\"fp32\\\", \\\"n_perm\\\": 5000, \\\"pair_config\\\": \\\"canary=[token_entropy,ece] x downstream=[distinct_1,distinct_2,distinct_3,mauve]\\\"}}, \\\"alpha_sweep_a060_s43_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"perm_granger_fwd_fdr\\\": \\\"0/8\\\", \\\"perm_granger_rev_fdr\\\": \\\"0/8\\\", \\\"consensus_k4_3sigma\\\": \\\"3/8\\\", \\\"consensus_k3_3sigma\\\": \\\"7/8\\\", \\\"threshold_onset_3sigma\\\": \\\"8/8\\\", \\\"naive_xcorr\\\": \\\"7/8\\\", \\\"diff_xcorr_fdr\\\": \\\"6/8\\\", \\\"ty_granger\\\": \\\"4/8\\\", \\\"drift_pct\\\": {\\\"token_entropy\\\": -28.61, \\\"distinct_1\\\": -31.02, \\\"distinct_2\\\": -39.02, \\\"distinct_3\\\": -37.3, \\\"ece\\\": 1530.81, \\\"perplexity\\\": 85.11, \\\"mauve\\\": -10.96, \\\"effective_rank\\\": 61}, \\\"gen0\\\": {\\\"token_entropy\\\": 3.234, \\\"perplexity\\\": 26.949, \\\"distinct_1\\\": 0.098}, \\\"gen9\\\": {\\\"token_entropy\\\": 2.309, \\\"perplexity\\\": 49.885, \\\"distinct_1\\\": 0.068}, \\\"note\\\": \\\"T=10 (gen_0-9, gen_10 timeout EXIT_CODE=124), D108 non-monotonicity confirmed\\\"}}, \\\"generalize_pythia1b_c4_a100_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"D102_reanalysis\\\": \\\"→mauve (replacing →ppl)\\\", \\\"pair_config\\\": \\\"canary=[token_entropy,ece] × downstream=[distinct_1,distinct_2,distinct_3,mauve]\\\", \\\"n_perm\\\": 5000, \\\"perm_granger_fdr_forward_sig\\\": \\\"8/8\\\", \\\"diff_xcorr_fdr_forward_sig\\\": \\\"8/8\\\", \\\"threshold_forward_sig\\\": \\\"8/8\\\", \\\"ty_forward_sig\\\": \\\"4/8\\\", \\\"robust_pairs_K3\\\": \\\"8/8\\\", \\\"robust_pairs_K4\\\": \\\"8/8\\\", \\\"D102_note\\\": \\\"ppl→mauve统一后: robust 2→8, perm_fdr 6→8, diff_fdr 6→8, ty 1→4.\\\", \\\"K_ge3_D116\\\": \\\"~1/8\\\", \\\"K_ge4_D116\\\": \\\"0/8\\\", \\\"D116_note\\\": \\\"D105+D111 joint: threshold JSON 3x_sigma_drift=8/8 but registry threshold_onset_3sigma=0/8 (M034). D111 kills diff_fwd. Reviewer estimate ~1/8.\\\"}}, \\\"alpha_sweep_a000_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.2342, \\\"gen10_token_entropy\\\": 3.0693, \\\"gen0_ece\\\": 0.0108, \\\"gen10_ece\\\": 0.0164, \\\"gen0_perplexity\\\": 26.95, \\\"gen10_perplexity\\\": 21.11, \\\"gen0_distinct_1\\\": 0.0982, \\\"gen10_distinct_1\\\": 0.0847, \\\"token_entropy_drift_pct\\\": -5.1, \\\"ece_drift_pct\\\": 51.7, \\\"perplexity_drift_pct\\\": -21.7, \\\"distinct_1_drift_pct\\\": -13.8, \\\"distinct_2_drift_pct\\\": -9.8, \\\"distinct_3_drift_pct\\\": -4.5, \\\"gen1_10_perplexity_drift_pct\\\": 9.4, \\\"gen1_10_distinct_1_drift_pct\\\": -13.1, \\\"gen1_10_entropy_drift_pct\\\": 2.6}}, \\\"smollm3_3b_wiki_a100_s43_fp32\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"padding_robustness_a100_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"robust_pairs_K4_3sigma\\\": \\\"6/8\\\", \\\"robust_pairs_K3_3sigma\\\": \\\"6/8\\\", \\\"threshold_onset_3sigma\\\": \\\"0/8\\\", \\\"D105_3sigma_note\\\": \\\"True 3sigma recompute. threshold_onset dropped 5/8->0/8. K4 unchanged at 6/8. PermG/TY unchanged.\\\"}}, \\\"alpha_sweep_a075_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"n_generations\\\": 11, \\\"gen0\\\": {\\\"token_entropy\\\": 3.2342, \\\"ece\\\": 0.0108, \\\"perplexity\\\": 26.949, \\\"distinct_1\\\": 0.098, \\\"distinct_2\\\": 0.5141, \\\"distinct_3\\\": 0.8127, \\\"effective_rank\\\": 46.613, \\\"mauve\\\": 0.0311}, \\\"gen10\\\": {\\\"token_entropy\\\": 2.283, \\\"ece\\\": 0.2145, \\\"perplexity\\\": 77.697, \\\"distinct_1\\\": 0.0731, \\\"distinct_2\\\": 0.357, \\\"distinct_3\\\": 0.5957, \\\"effective_rank\\\": 78.06, \\\"mauve\\\": 0.0299}, \\\"drift_pct\\\": {\\\"token_entropy\\\": -29.41, \\\"ece\\\": 1885.41, \\\"perplexity\\\": 188.31, \\\"distinct_1\\\": -25.38, \\\"distinct_2\\\": -30.55, \\\"distinct_3\\\": -26.7, \\\"effective_rank\\\": 67.47, \\\"mauve\\\": -3.73}, \\\"lead_lag\\\": {\\\"PermG_fwd\\\": \\\"6/8\\\", \\\"PermG_rev\\\": \\\"0/8\\\", \\\"K_ge_4\\\": \\\"6/8\\\", \\\"MMCT_detection\\\": 0.75, \\\"TY_granger\\\": \\\"8/8\\\", \\\"naive_xcorr\\\": \\\"7/8\\\", \\\"diff_xcorr\\\": \\\"6/8\\\", \\\"threshold_onset\\\": \\\"8/8\\\"}, \\\"asymmetry\\\": \\\"strong (fwd=6, rev=0)\\\"}}, \\\"alpha_sweep_a060_s42_fp32_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"final_ppl\\\": 45.41, \\\"final_entropy\\\": 2.48, \\\"final_eff_rank\\\": 69.3, \\\"final_mauve\\\": 0.023, \\\"precision\\\": \\\"fp32\\\", \\\"token_entropy_drift\\\": -23.36, \\\"ece_drift\\\": 1260.23, \\\"perplexity_drift\\\": 68.52, \\\"distinct_1_drift\\\": -28.17, \\\"distinct_2_drift\\\": -37.22, \\\"distinct_3_drift\\\": -35.35, \\\"perm_granger_fwd\\\": \\\"3/8\\\", \\\"perm_granger_rev\\\": \\\"0/8\\\", \\\"ty_granger_fwd\\\": \\\"8/8\\\", \\\"threshold_onset_fwd\\\": \\\"8/8\\\", \\\"consensus_k4\\\": \\\"7/8\\\", \\\"mmct_wpair_fwd\\\": 0.875}}, \\\"alpha_sweep_a050_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"token_entropy_gen0\\\": 3.2342, \\\"token_entropy_gen10\\\": 2.7075, \\\"token_entropy_drift_pct\\\": -16.3, \\\"distinct_1_gen0\\\": 0.0916, \\\"distinct_1_gen10\\\": 0.0649, \\\"distinct_1_drift_pct\\\": -29.2, \\\"perplexity_gen0\\\": 26.95, \\\"perplexity_gen10\\\": 31.46, \\\"perplexity_drift_pct\\\": 16.8, \\\"ece_gen0\\\": 0.0108, \\\"ece_gen10\\\": 0.0868, \\\"ece_drift_pct\\\": 703.4, \\\"perm_granger_fwd\\\": \\\"6/8\\\", \\\"perm_granger_rev\\\": \\\"0/8\\\", \\\"ty_granger_fwd\\\": \\\"4/8\\\", \\\"consensus_k4\\\": \\\"6/8\\\", \\\"mmct_wpair_fwd\\\": \\\"6/8\\\", \\\"precision\\\": \\\"fp32\\\", \\\"n_perm\\\": 5000, \\\"padding_side\\\": \\\"right (D093 fix NOT applied)\\\"}}, \\\"alpha_sweep_a035_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"PermG_fwd\\\": \\\"0/8\\\", \\\"PermG_rev\\\": \\\"0/8\\\", \\\"K_ge3_3sigma\\\": \\\"6/8\\\", \\\"K_ge4_3sigma\\\": \\\"2/8\\\", \\\"threshold_onset\\\": \\\"8/8\\\", \\\"TY_granger\\\": \\\"4/8\\\", \\\"naive_xcorr_fwd\\\": \\\"8/8\\\", \\\"diff_xcorr_fwd\\\": \\\"4/8\\\", \\\"detection_rate_k4\\\": 0.25, \\\"drift_pct\\\": {\\\"token_entropy\\\": -18.53, \\\"ece\\\": 651.26, \\\"perplexity\\\": -1.27, \\\"distinct_1\\\": -36.38, \\\"distinct_2\\\": -49.45, \\\"distinct_3\\\": -50.04, \\\"effective_rank\\\": 22.21, \\\"mauve\\\": -17.78}, \\\"gen0\\\": {\\\"token_entropy\\\": 3.234, \\\"ece\\\": 0.0108, \\\"perplexity\\\": 26.95, \\\"distinct_1\\\": 0.098, \\\"distinct_2\\\": 0.514, \\\"distinct_3\\\": 0.813, \\\"effective_rank\\\": 46.61, \\\"mauve\\\": 0.0311}, \\\"gen10\\\": {\\\"token_entropy\\\": 2.635, \\\"ece\\\": 0.0812, \\\"perplexity\\\": 26.61, \\\"distinct_1\\\": 0.0623, \\\"distinct_2\\\": 0.26, \\\"distinct_3\\\": 0.406, \\\"effective_rank\\\": 56.96, \\\"mauve\\\": 0.0256}, \\\"consensus_detail\\\": {\\\"K4_pairs\\\": [\\\"token_entropy->distinct_1\\\", \\\"ece->distinct_1\\\"], \\\"K3_pairs\\\": [\\\"token_entropy->distinct_2\\\", \\\"token_entropy->mauve\\\", \\\"ece->distinct_2\\\", \\\"ece->mauve\\\"], \\\"K2_pairs\\\": [\\\"token_entropy->distinct_3\\\", \\\"ece->distinct_3\\\"]}, \\\"n_generations\\\": 11, \\\"precision\\\": \\\"fp32\\\", \\\"onset_conclusion\\\": \\\"PermG=0/8 confirms onset >= 0.35; combined with a040(0/8) and a050(6/8), onset in [0.40, 0.50]\\\"}}, \\\"alpha_sweep_a025_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"PermG_fwd\\\": \\\"0/8\\\", \\\"PermG_rev\\\": \\\"0/8\\\", \\\"K_ge_4\\\": \\\"0/8\\\", \\\"MMCT\\\": \\\"0/8\\\", \\\"MMCT_detection_rate\\\": 0, \\\"d1_drift_pct\\\": -39.15, \\\"d2_drift_pct\\\": -54.75, \\\"d3_drift_pct\\\": -56.98, \\\"mauve_drift_pct\\\": -41.86, \\\"entropy_drift_pct\\\": -4.79, \\\"ece_drift_pct\\\": 79.17, \\\"ppl_drift_pct\\\": -18.09, \\\"eff_rank_drift_pct\\\": -3.78, \\\"ppl_by_gen\\\": [26.95, 19.39, 20.37, 20.75, 21.14, 21.3, 21.48, 21.88, 21.9, 22.25, 22.07], \\\"entropy_by_gen\\\": [3.234, 2.983, 3.015, 3.039, 3.051, 3.034, 3.049, 3.067, 3.063, 3.104, 3.079], \\\"d1_by_gen\\\": [0.098, 0.0976, 0.0815, 0.0737, 0.0688, 0.0657, 0.0635, 0.0614, 0.061, 0.0601, 0.0596], \\\"mauve_by_gen\\\": [0.0311, 0.0314, 0.0326, 0.0318, 0.0314, 0.0272, 0.0242, 0.0221, 0.0207, 0.0207, 0.0181], \\\"naive_xcorr_fwd\\\": \\\"8/8\\\", \\\"diff_xcorr_fwd\\\": \\\"3/8\\\", \\\"threshold_onset_fwd\\\": \\\"5/8\\\", \\\"ty_granger_sig\\\": \\\"3/8\\\", \\\"consensus_detail_max_votes\\\": 3, \\\"hypothesis_validated\\\": true, \\\"note\\\": \\\"PermG=0/8 confirms α=0.25 is below phase transition. d1_drift=-39.15% is surprisingly large (> α=0.50's -28.7%), suggesting diversity collapse proceeds without Granger-detectable lead-lag at this α. token_entropy→distinct_1 had raw PermG p=0.007 but FDR-corrected p=0.053 (borderline).\\\"}}, \\\"alpha_sweep_a010_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"token_entropy_drift_pct\\\": -4.59, \\\"distinct_1_drift_pct\\\": -23.8, \\\"distinct_2_drift_pct\\\": -27.15, \\\"distinct_3_drift_pct\\\": -19.36, \\\"perplexity_drift_pct\\\": -18.94, \\\"perm_granger_fwd\\\": \\\"0/8\\\", \\\"perm_granger_rev\\\": \\\"0/8\\\", \\\"ty_granger_fwd\\\": \\\"3/8\\\", \\\"threshold_onset_fwd\\\": \\\"5/8\\\", \\\"consensus_k4\\\": \\\"2/8\\\", \\\"mmct_wpair_fwd\\\": \\\"2/8\\\", \\\"mmct_detection_rate\\\": 0.25, \\\"precision\\\": \\\"fp32\\\", \\\"padding_side_fix\\\": \\\"D093 applied\\\", \\\"blind_zone_confirmed\\\": true, \\\"cross_seed_permg_stable\\\": true}}, \\\"alpha_sweep_a005_s42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"final_ppl\\\": 20.81, \\\"final_entropy\\\": 3.04, \\\"final_eff_rank\\\": 45.3, \\\"final_mauve\\\": 0.023, \\\"precision\\\": \\\"fp32\\\", \\\"token_entropy_drift\\\": -5.96, \\\"ece_drift\\\": 55.41, \\\"perplexity_drift\\\": -22.78, \\\"distinct_1_drift\\\": -24.86, \\\"distinct_2_drift\\\": -28.42, \\\"distinct_3_drift\\\": -19.54, \\\"perm_granger_fwd\\\": \\\"0/8\\\", \\\"perm_granger_rev\\\": \\\"0/8\\\", \\\"ty_granger_fwd\\\": \\\"3/8\\\", \\\"threshold_onset_fwd\\\": \\\"5/8\\\", \\\"consensus_k4\\\": \\\"0/8\\\", \\\"mmct_wpair_fwd\\\": 0}}, \\\"alpha_sweep_a010_s42_bf16\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"scale_14b_a050_s42_bf16\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"interv_react_s43\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"alpha_sweep_a040_s42_fp32_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"PermG_fwd\\\": \\\"0/8\\\", \\\"PermG_rev\\\": \\\"0/8\\\", \\\"K4_3sigma\\\": \\\"0/8\\\", \\\"K3_3sigma\\\": \\\"1/8\\\", \\\"threshold_onset_3sigma\\\": \\\"8/8\\\", \\\"naive_xcorr\\\": \\\"4/8\\\", \\\"diff_xcorr\\\": \\\"0/8\\\", \\\"TY_granger\\\": \\\"4/8\\\", \\\"drift_token_entropy\\\": \\\"-19.13%\\\", \\\"drift_ece\\\": \\\"+736.90%\\\", \\\"drift_distinct1\\\": \\\"-35.48%\\\", \\\"drift_distinct2\\\": \\\"-48.01%\\\", \\\"drift_distinct3\\\": \\\"-48.42%\\\", \\\"drift_mauve\\\": \\\"-23.04%\\\", \\\"drift_perplexity\\\": \\\"+5.36%\\\", \\\"D111_direction_check\\\": \\\"applied: naive 8/8→4/8, diff 3/8→0/8, K3 6/8→1/8, K4 1/8→0/8\\\"}}, \\\"alpha_sweep_a030_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"permg_fwd\\\": \\\"0/8\\\", \\\"permg_rev\\\": \\\"0/8\\\", \\\"k_ge3\\\": \\\"3/8\\\", \\\"k_ge4\\\": \\\"3/8\\\", \\\"naive_xcorr\\\": \\\"5/8\\\", \\\"diff_xcorr\\\": \\\"3/8\\\", \\\"threshold_onset\\\": \\\"8/8\\\", \\\"ty_granger\\\": \\\"5/8\\\", \\\"drift_entropy_pct\\\": -17.32, \\\"drift_ece_pct\\\": 549.38, \\\"drift_d1_pct\\\": -36.72, \\\"drift_d2_pct\\\": -49.75, \\\"drift_d3_pct\\\": -50.09, \\\"drift_mauve_pct\\\": -26.09, \\\"n_generations\\\": 11, \\\"n_perm\\\": 5000, \\\"D111_direction_check\\\": \\\"applied: naive 8/8→5/8, diff 4/8→3/8, K3 6/8→3/8, K4 unchanged 3/8\\\"}}, \\\"alpha_sweep_a045_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"permg_fwd\\\": 0, \\\"permg_rev\\\": 0, \\\"k_ge3\\\": 3, \\\"k_ge4\\\": 0, \\\"naive_xcorr\\\": 7, \\\"diff_xcorr\\\": 3, \\\"threshold_onset\\\": 8, \\\"ty_granger\\\": 1, \\\"total_pairs\\\": 8, \\\"drift_entropy_pct\\\": -18.73, \\\"drift_ece_pct\\\": 770.37, \\\"drift_d1_pct\\\": -35.39, \\\"drift_d2_pct\\\": -47.87, \\\"drift_d3_pct\\\": -47.79, \\\"drift_perplexity_pct\\\": 12.19, \\\"drift_mauve_pct\\\": -24.89, \\\"drift_effrank_pct\\\": 23.41, \\\"gen0_token_entropy\\\": 3.2342, \\\"gen10_token_entropy\\\": 2.6283, \\\"gen0_ece\\\": 0.0108, \\\"gen10_ece\\\": 0.094, \\\"gen0_distinct_1\\\": 0.098, \\\"gen10_distinct_1\\\": 0.0633, \\\"gen0_perplexity\\\": 26.949, \\\"gen10_perplexity\\\": 30.234, \\\"gen0_mauve\\\": 0.0311, \\\"gen10_mauve\\\": 0.0234, \\\"onset_boundary\\\": \\\"[0.45, 0.50]\\\"}}, \\\"c4_a075_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"PermG_fwd\\\": \\\"8/8\\\", \\\"PermG_rev\\\": \\\"0/8\\\", \\\"K_ge_3_3sigma\\\": \\\"6/8\\\", \\\"K_ge_4_3sigma\\\": \\\"0/8\\\", \\\"threshold_onset_3sigma\\\": \\\"8/8\\\", \\\"naive_xcorr\\\": \\\"0/8\\\", \\\"diff_xcorr\\\": \\\"0/8\\\", \\\"TY_granger\\\": \\\"6/8\\\", \\\"drift_token_entropy\\\": -35.32, \\\"drift_ece\\\": 2809.23, \\\"drift_perplexity\\\": 2152.6, \\\"drift_distinct_1\\\": -12.4, \\\"drift_distinct_2\\\": -15.41, \\\"drift_distinct_3\\\": -14.59, \\\"drift_mauve\\\": -42.26, \\\"drift_effective_rank\\\": 110.31, \\\"gen0_token_entropy\\\": 3.1094, \\\"D111_direction_check\\\": \\\"applied: naive 8/8→0/8, diff 8/8→0/8, K3 8/8→6/8, K4 8/8→0/8\\\"}}, \\\"c4_a050_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"permg_fwd_fdr_sig\\\": \\\"8/8\\\", \\\"permg_rev_fdr_sig\\\": \\\"7/8\\\", \\\"consensus_K4_3sigma\\\": \\\"2/8\\\", \\\"consensus_K3_3sigma\\\": \\\"6/8\\\", \\\"threshold_onset_3sigma\\\": \\\"8/8\\\", \\\"naive_xcorr_sig\\\": \\\"4/8\\\", \\\"diff_xcorr_fdr_sig\\\": \\\"0/8\\\", \\\"ty_granger_sig\\\": \\\"4/8\\\", \\\"mmct_detection_rate\\\": 0.75, \\\"drift_token_entropy_pct\\\": -47.99, \\\"drift_distinct1_pct\\\": -9.78, \\\"drift_distinct2_pct\\\": -15.72, \\\"drift_distinct3_pct\\\": -17.75, \\\"drift_perplexity_pct\\\": 2931.59, \\\"drift_mauve_pct\\\": -54.25, \\\"drift_ece_pct\\\": 3103.74, \\\"gen0_token_entropy\\\": 3.109, \\\"gen10_token_entropy\\\": 1.617, \\\"D111_direction_check\\\": \\\"applied: naive 8/8→4/8, diff 8/8→0/8, K3 8/8→6/8, K4 8/8→2/8\\\"}}, \\\"c4_a025_s42_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"permg_fwd_fdr\\\": \\\"0/8\\\", \\\"permg_rev_fdr\\\": \\\"0/8\\\", \\\"consensus_K3_3sigma\\\": \\\"0/8\\\", \\\"consensus_K4_3sigma\\\": \\\"0/8\\\", \\\"threshold_onset_3sigma\\\": \\\"8/8\\\", \\\"naive_xcorr\\\": \\\"3/8\\\", \\\"diff_xcorr\\\": \\\"0/8\\\", \\\"ty_granger\\\": \\\"3/8\\\", \\\"drift_token_entropy\\\": \\\"-53.01%\\\", \\\"drift_ece\\\": \\\"+3242.80%\\\", \\\"drift_perplexity\\\": \\\"+3617.05%\\\", \\\"drift_d1\\\": \\\"-4.10%\\\", \\\"drift_d2\\\": \\\"-8.78%\\\", \\\"drift_d3\\\": \\\"-11.95%\\\", \\\"drift_mauve\\\": \\\"-52.08%\\\", \\\"drift_effective_rank\\\": \\\"+111.90%\\\", \\\"D111_direction_check\\\": \\\"applied: naive 8/8→3/8, diff 8/8→0/8, K3 8/8→0/8, K4 3/8→0/8\\\"}}, \\\"scale_14b_c4_s42_fp32\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"method_ablation_phase3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"n_alpha_points\\\": 10, \\\"alphas\\\": [0, 0.05, 0.1, 0.25, 0.35, 0.4, 0.5, 0.6, 0.75, 1], \\\"naive_sig_rates\\\": [1, 0.875, 0.875, 1, 1, 1, 1, 0.875, 0.875, 1], \\\"diff_sig_rates\\\": [0.5, 0.375, 0.75, 0.375, 0.5, 0.375, 0.875, 1, 0.75, 0.75], \\\"thresh_3sigma_rates\\\": [0.5, 0.625, 0.625, 0.625, 1, 1, 1, 1, 1, 1], \\\"permG_fwd_rates\\\": [0, 0, 0, 0, 0, 0, 0.75, 0.375, 0.75, 0.75], \\\"permG_rev_rates\\\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \\\"TY_rates\\\": [0.25, 0.375, 0.375, 0.375, 0.5, 0.5, 0.5, 1, 1, 0.375], \\\"K_ge3_rates\\\": [0.375, 0.375, 0.5, 0.5, 0.75, 0.75, 0.875, 1, 0.875, 0.75], \\\"K_ge4_rates\\\": [0, 0, 0.25, 0, 0.25, 0.125, 0.75, 0.875, 0.75, 0.75], \\\"regime_structure\\\": {\\\"null\\\": \\\"alpha<=0.40: PermG=0%, naive=87-100% FPR. 11 data points all PermG=0/8\\\", \\\"onset\\\": \\\"alpha=[0.40,0.50]: PermG jumps 0→75%, K≥4 jumps 0→75%\\\", \\\"sync_collapse\\\": \\\"alpha=0.60: PermG drops to 37.5% (non-monotonic, D108). BUT K≥4 peaks at 87.5% — TY complements PermG (TY=100% here vs 50% at α=0.50). MMCT multi-method consensus strongest at this α\\\", \\\"detection\\\": \\\"alpha>=0.75: PermG=75%, TY non-monotonic drop to 37.5-100%\\\"}, \\\"claim3_support\\\": \\\"strong: 4-regime dose-response with non-monotonic PermG at α=0.60 (sync collapse) and TY complementarity. Method choice directly determines conclusion validity. PermG 0% FPR in null regime = cleanest discriminator.\\\", \\\"D105_standard\\\": \\\"3sigma + FDR BH + n_perm=5000 + unified 8-pair\\\"}}, \\\"smollm3_3b_wiki_a100_s42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"PermG_fwd\\\": \\\"3/8\\\", \\\"PermG_rev\\\": \\\"0/8\\\", \\\"robust_pairs_K4_3sigma\\\": \\\"0/8\\\", \\\"robust_pairs_K3_3sigma\\\": \\\"0/8\\\", \\\"robust_pairs_K3_2sigma\\\": \\\"6/8\\\", \\\"robust_pairs_K4_2sigma\\\": \\\"3/8\\\", \\\"threshold_onset_3sigma\\\": \\\"0/8\\\", \\\"threshold_onset_2sigma\\\": \\\"8/8\\\", \\\"naive_xcorr\\\": \\\"4/8\\\", \\\"diff_xcorr\\\": \\\"6/8\\\", \\\"ty_granger\\\": \\\"0/8\\\", \\\"note\\\": \\\"D105+D111: FDR per-method, 3sigma, direction-checked. K≥3 corrected 3/8→0/8: 3sigma_recompute_v2 had naive_xcorr direction-blind bug (ECE pairs peak_lag<0 wrongly counted). Authoritative source: 5method_leadlag.json with peak_lag>0 check. PermG_fwd=3/8 (ECE→d1/d2/d3 via diff_xcorr+permG). naive_xcorr corrected 8/8→4/8 (entropy pairs only, ECE pairs all lag<0).\\\"}}, \\\"gen_gpt2m_a100_s43\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"qwen35_dryrun_launch\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"scale_69b_a100_s43_fp32\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"interv_react_s43_fp32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"trigger_gen\\\": 2, \\\"trigger_distinct1_drop_pct\\\": -15.83, \\\"gen2_ppl\\\": 158.22, \\\"recovery_ppl\\\": 21.98, \\\"recovery_complete_by_gen\\\": 3, \\\"intervention_metric\\\": \\\"distinct_1\\\", \\\"intervention_threshold\\\": 0.1, \\\"intervention_alpha\\\": 0, \\\"gen0\\\": {\\\"token_entropy\\\": 3.234, \\\"perplexity\\\": 26.949, \\\"distinct_1\\\": 0.098}, \\\"gen9\\\": {\\\"token_entropy\\\": 3.079, \\\"perplexity\\\": 21.357, \\\"distinct_1\\\": 0.089}, \\\"gen10\\\": {\\\"token_entropy\\\": 3.088, \\\"perplexity\\\": 21.387, \\\"distinct_1\\\": 0.083}, \\\"note\\\": \\\"reactive intervention triggered at gen2 (d1=0.083 < threshold=0.1), alpha 1.0→0.0; ppl spike 26.9→158.2 recovered by gen3 to 22.0; d1 partial recovery 0.098→0.083→0.089\\\"}}, \\\"scale_69b_a100_s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"qwen35_08b_wiki_a100_s43_fp32\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"generalize_pythia1b_c4_a100_s42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"robust_pairs_K4_3sigma\\\": \\\"4/8\\\", \\\"robust_pairs_K3_3sigma\\\": \\\"8/8\\\", \\\"threshold_onset_3sigma\\\": \\\"0/8\\\", \\\"D105_3sigma_note\\\": \\\"D105 backfill: true 3sigma, fdr_permethod, unified 8-pair (canary={token_entropy,ece} x downstream={d1,d2,d3,mauve})\\\"}}}, \\\"count\\\": 50, \\\"total\\\": 118, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4314}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"interv_pred_a075_s42\": {\"status\": \"DONE\"}, \"alpha_sweep_a045_s43_fp32\": {\"status\": \"RUNNING\"}, \"scale_14b_a050_s42_fp32\": {\"status\": \"RUNNING\"}, \"interv_pred_14b_s42_fp32\": {\"status\": \"DONE\"}, \"data_strategy_ablation_s43\": {\"status\": \"RUNNING\", \"metrics\": {\"data_strategy\": \"accumulate\", \"baseline_exp\": \"alpha_sweep_a050_s43_fp32\"}}, \"data_strategy_ablation_s42\": {\"status\": \"RUNNING\"}, \"generalize_pythia14b_wiki_a100_s43\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"3x_sigma_drift→true_3sigma\", \"K3_3sigma_m037\": \"3/8\", \"K3_3sigma_d111_detail\": \"naive=0/8 diff=6/8 thr3s=0/8 pg=6/8 ty=3/8\", \"note\": \"D111 reduces K3 from 6/8 to 3/8 (all naive peak_lag>0)\"}}, \"generalize_pythia14b_wiki_a100_s42\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"3x_sigma_drift→true_3sigma\", \"K3_3sigma_m037\": \"1/8\", \"K3_3sigma_d111_detail\": \"naive=6/8 diff=6/8 thr3s=0/8 pg=2/8 ty=0/8\"}}, \"pythia410m_wiki_a100_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"unknown→true_3sigma\", \"K3_3sigma_m037\": \"6/8\", \"K3_3sigma_d111_detail\": \"naive=6/8 diff=6/8 thr3s=0/8 pg=6/8 ty=6/8\", \"caveat\": \"xcorr recomputed from raw metrics without FDR\"}}, \"alpha_sweep_a050_postd093_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"unknown→true_3sigma\", \"K3_3sigma_m037\": \"3/8\", \"K3_3sigma_d111_detail\": \"naive=3/8 diff=2/8 thr3s=0/8 pg=6/8 ty=4/8\"}}, \"generalize_pythia1b_c4_a100_s43\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"3x_sigma_drift→true_3sigma\", \"K3_3sigma_m037\": \"6/8\", \"K3_3sigma_d111_detail\": \"naive=4/8 diff=8/8 thr3s=2/8 pg=8/8 ty=4/8\"}}, \"opt13b_wiki_a100_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"already_3sigma_d105\", \"K3_3sigma_m037\": \"6/8\", \"K3_3sigma_d111_detail\": \"naive=8/8 diff=6/8 thr3s=0/8 pg=6/8 ty=5/8\"}}, \"generalize_opt1b_wiki_a100_s42\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"3x_sigma_drift→true_3sigma\", \"K3_3sigma_m037\": \"6/8\", \"K3_3sigma_d111_detail\": \"naive=7/8 diff=6/8 thr3s=2/8 pg=6/8 ty=0/8\"}}, \"gen_gpt2m_a100_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"3x_sigma_drift→true_3sigma\", \"K3_3sigma_m037\": \"6/8\", \"K3_3sigma_d111_detail\": \"naive=7/8 diff=6/8 thr3s=0/8 pg=6/8 ty=4/8\"}}, \"generalize_pythia410m_wiki_a100_s42\": {\"status\": \"DONE\", \"metrics\": {\"threshold_onset_3sigma_m037\": \"3x_sigma_drift→true_3sigma\", \"K3_3sigma_m037\": \"6/8\", \"K3_3sigma_d111_detail\": \"naive=7/8 diff=6/8 thr3s=2/8 pg=6/8 ty=1/8\"}}, \"c4_a050_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"8/8\", \"PermG_rev\": \"1/8\", \"K_ge_3_3sigma\": \"3/8\", \"K_ge_4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"0/8\", \"naive_xcorr\": \"4/8\", \"diff_xcorr\": \"6/8\", \"TY_granger\": \"0/8\", \"drift_token_entropy\": -47.98, \"drift_ece\": 3102.5, \"drift_perplexity\": 2957.1, \"drift_distinct_1\": -9.9, \"drift_distinct_2\": -16, \"drift_distinct_3\": -17.5, \"drift_mauve\": -47.5, \"drift_effective_rank\": 113.4, \"gen0_token_entropy\": 3.1094, \"D111_direction_check\": \"applied: naive_xcorr peak_lag<0, diff_xcorr peak_lag<0\", \"D102_8pair\": \"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\", \"D105_3sigma\": \"true 3sigma (std of full series)\", \"analysis_script\": \"run_5method_analysis_d102.py + D105 inline recompute\", \"n_perm\": 5000}}, \"c4_a075_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"8/8\", \"PermG_rev\": \"0/8\", \"K_ge_3_3sigma\": \"8/8\", \"K_ge_4_3sigma\": \"1/8\", \"threshold_onset_3sigma\": \"0/8\", \"naive_xcorr\": \"8/8\", \"diff_xcorr\": \"8/8\", \"TY_granger\": \"1/8\", \"drift_token_entropy\": -34.12, \"drift_ece\": 2781.6, \"drift_perplexity\": 2149.2, \"drift_distinct_1\": -12.6, \"drift_distinct_2\": -16.2, \"drift_distinct_3\": -15.7, \"drift_mauve\": -52.8, \"drift_effective_rank\": 111, \"gen0_token_entropy\": 3.1094, \"D111_direction_check\": \"applied: naive_xcorr peak_lag<0, diff_xcorr peak_lag<0\", \"D102_8pair\": \"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\", \"D105_3sigma\": \"true 3sigma (std of full series)\", \"analysis_script\": \"run_5method_analysis_d102.py + D105 inline recompute\", \"n_perm\": 5000}}, \"alpha_sweep_a075_s43\": {\"status\": \"DONE\", \"metrics\": {\"gen0\": {\"token_entropy\": 3.234, \"ece\": 0.0108, \"perplexity\": 26.95, \"distinct_1\": 0.0983, \"distinct_2\": 0.5132, \"distinct_3\": 0.8057, \"effective_rank\": 46.61, \"mauve\": 0.0335}, \"gen10\": {\"token_entropy\": 2.349, \"ece\": 0.204, \"perplexity\": 76.08, \"distinct_1\": 0.0666, \"distinct_2\": 0.2984, \"distinct_3\": 0.4838, \"effective_rank\": 79.4, \"mauve\": 0.0289}, \"drift_pct\": {\"token_entropy\": -27.38, \"ece\": 1791.96, \"perplexity\": 182.3, \"distinct_1\": -32.3, \"distinct_2\": -41.86, \"distinct_3\": -39.96, \"effective_rank\": 70.36, \"mauve\": -13.63}, \"PermG_fwd\": \"5/8\", \"PermG_rev\": \"0/8\", \"naive_xcorr_fwd_D111\": \"2/8\", \"diff_xcorr_fwd_D111\": \"6/8\", \"threshold_onset_3sigma\": \"8/8\", \"TY_granger\": \"6/8\", \"K3_3sigma\": \"7/8\", \"K4_3sigma\": \"5/8\", \"perm_granger_fdr_forward_sig\": \"5/8\", \"D105_D111_compliant\": true, \"M035_direction\": \"peak_lag < 0\", \"precision\": \"fp32\", \"n_perm\": 5000, \"pair_config\": \"canary=[token_entropy,ece] x downstream=[distinct_1,distinct_2,distinct_3,mauve]\"}}, \"alpha_sweep_a050_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"token_entropy_gen0\": 3.2342, \"token_entropy_gen10\": 2.7227, \"token_entropy_drift_pct\": -15.81, \"ece_gen0\": 0.0108, \"ece_gen10\": 0.0842, \"ece_drift_pct\": 679.56, \"distinct_1_gen0\": 0.0929, \"distinct_1_gen10\": 0.066, \"distinct_1_drift_pct\": -29, \"perplexity_gen0\": 26.95, \"perplexity_gen10\": 31.58, \"perplexity_drift_pct\": 17.17, \"mauve_drift_pct\": -23.54, \"PermG_fwd\": \"6/8\", \"PermG_rev\": \"0/8\", \"naive_xcorr_fwd_D111\": \"2/8\", \"diff_xcorr_fwd_D111\": \"6/8\", \"threshold_onset_3sigma\": \"8/8\", \"TY_granger\": \"5/8\", \"K3_3sigma\": \"6/8\", \"K4_3sigma\": \"5/8\", \"perm_granger_fdr_forward_sig\": \"6/8\", \"D105_D111_compliant\": true, \"M035_direction\": \"peak_lag < 0\", \"precision\": \"fp32\", \"n_perm\": 5000, \"pair_config\": \"canary=[token_entropy,ece] x downstream=[distinct_1,distinct_2,distinct_3,mauve]\"}}, \"alpha_sweep_a060_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"perm_granger_fwd_fdr\": \"0/8\", \"perm_granger_rev_fdr\": \"0/8\", \"consensus_k4_3sigma\": \"3/8\", \"consensus_k3_3sigma\": \"7/8\", \"threshold_onset_3sigma\": \"8/8\", \"naive_xcorr\": \"7/8\", \"diff_xcorr_fdr\": \"6/8\", \"ty_granger\": \"4/8\", \"drift_pct\": {\"token_entropy\": -28.61, \"distinct_1\": -31.02, \"distinct_2\": -39.02, \"distinct_3\": -37.3, \"ece\": 1530.81, \"perplexity\": 85.11, \"mauve\": -10.96, \"effective_rank\": 61}, \"gen0\": {\"token_entropy\": 3.234, \"perplexity\": 26.949, \"distinct_1\": 0.098}, \"gen9\": {\"token_entropy\": 2.309, \"perplexity\": 49.885, \"distinct_1\": 0.068}, \"note\": \"T=10 (gen_0-9, gen_10 timeout EXIT_CODE=124), D108 non-monotonicity confirmed\"}}, \"generalize_pythia1b_c4_a100_s42\": {\"status\": \"DONE\", \"metrics\": {\"D102_reanalysis\": \"→mauve (replacing →ppl)\", \"pair_config\": \"canary=[token_entropy,ece] × downstream=[distinct_1,distinct_2,distinct_3,mauve]\", \"n_perm\": 5000, \"perm_granger_fdr_forward_sig\": \"8/8\", \"diff_xcorr_fdr_forward_sig\": \"8/8\", \"threshold_forward_sig\": \"8/8\", \"ty_forward_sig\": \"4/8\", \"robust_pairs_K3\": \"8/8\", \"robust_pairs_K4\": \"8/8\", \"D102_note\": \"ppl→mauve统一后: robust 2→8, perm_fdr 6→8, diff_fdr 6→8, ty 1→4.\", \"K_ge3_D116\": \"~1/8\", \"K_ge4_D116\": \"0/8\", \"D116_note\": \"D105+D111 joint: threshold JSON 3x_sigma_drift=8/8 but registry threshold_onset_3sigma=0/8 (M034). D111 kills diff_fwd. Reviewer estimate ~1/8.\"}}, \"alpha_sweep_a000_s42\": {\"status\": \"DONE\", \"metrics\": {\"gen0_token_entropy\": 3.2342, \"gen10_token_entropy\": 3.0693, \"gen0_ece\": 0.0108, \"gen10_ece\": 0.0164, \"gen0_perplexity\": 26.95, \"gen10_perplexity\": 21.11, \"gen0_distinct_1\": 0.0982, \"gen10_distinct_1\": 0.0847, \"token_entropy_drift_pct\": -5.1, \"ece_drift_pct\": 51.7, \"perplexity_drift_pct\": -21.7, \"distinct_1_drift_pct\": -13.8, \"distinct_2_drift_pct\": -9.8, \"distinct_3_drift_pct\": -4.5, \"gen1_10_perplexity_drift_pct\": 9.4, \"gen1_10_distinct_1_drift_pct\": -13.1, \"gen1_10_entropy_drift_pct\": 2.6}}, \"smollm3_3b_wiki_a100_s43_fp32\": {\"status\": \"RUNNING\"}, \"padding_robustness_a100_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"robust_pairs_K4_3sigma\": \"6/8\", \"robust_pairs_K3_3sigma\": \"6/8\", \"threshold_onset_3sigma\": \"0/8\", \"D105_3sigma_note\": \"True 3sigma recompute. threshold_onset dropped 5/8->0/8. K4 unchanged at 6/8. PermG/TY unchanged.\"}}, \"alpha_sweep_a075_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"n_generations\": 11, \"gen0\": {\"token_entropy\": 3.2342, \"ece\": 0.0108, \"perplexity\": 26.949, \"distinct_1\": 0.098, \"distinct_2\": 0.5141, \"distinct_3\": 0.8127, \"effective_rank\": 46.613, \"mauve\": 0.0311}, \"gen10\": {\"token_entropy\": 2.283, \"ece\": 0.2145, \"perplexity\": 77.697, \"distinct_1\": 0.0731, \"distinct_2\": 0.357, \"distinct_3\": 0.5957, \"effective_rank\": 78.06, \"mauve\": 0.0299}, \"drift_pct\": {\"token_entropy\": -29.41, \"ece\": 1885.41, \"perplexity\": 188.31, \"distinct_1\": -25.38, \"distinct_2\": -30.55, \"distinct_3\": -26.7, \"effective_rank\": 67.47, \"mauve\": -3.73}, \"lead_lag\": {\"PermG_fwd\": \"6/8\", \"PermG_rev\": \"0/8\", \"K_ge_4\": \"6/8\", \"MMCT_detection\": 0.75, \"TY_granger\": \"8/8\", \"naive_xcorr\": \"7/8\", \"diff_xcorr\": \"6/8\", \"threshold_onset\": \"8/8\"}, \"asymmetry\": \"strong (fwd=6, rev=0)\"}}, \"alpha_sweep_a060_s42_fp32_v3\": {\"status\": \"DONE\", \"metrics\": {\"final_ppl\": 45.41, \"final_entropy\": 2.48, \"final_eff_rank\": 69.3, \"final_mauve\": 0.023, \"precision\": \"fp32\", \"token_entropy_drift\": -23.36, \"ece_drift\": 1260.23, \"perplexity_drift\": 68.52, \"distinct_1_drift\": -28.17, \"distinct_2_drift\": -37.22, \"distinct_3_drift\": -35.35, \"perm_granger_fwd\": \"3/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"8/8\", \"threshold_onset_fwd\": \"8/8\", \"consensus_k4\": \"7/8\", \"mmct_wpair_fwd\": 0.875}}, \"alpha_sweep_a050_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"token_entropy_gen0\": 3.2342, \"token_entropy_gen10\": 2.7075, \"token_entropy_drift_pct\": -16.3, \"distinct_1_gen0\": 0.0916, \"distinct_1_gen10\": 0.0649, \"distinct_1_drift_pct\": -29.2, \"perplexity_gen0\": 26.95, \"perplexity_gen10\": 31.46, \"perplexity_drift_pct\": 16.8, \"ece_gen0\": 0.0108, \"ece_gen10\": 0.0868, \"ece_drift_pct\": 703.4, \"perm_granger_fwd\": \"6/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"4/8\", \"consensus_k4\": \"6/8\", \"mmct_wpair_fwd\": \"6/8\", \"precision\": \"fp32\", \"n_perm\": 5000, \"padding_side\": \"right (D093 fix NOT applied)\"}}, \"alpha_sweep_a035_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"0/8\", \"PermG_rev\": \"0/8\", \"K_ge3_3sigma\": \"6/8\", \"K_ge4_3sigma\": \"2/8\", \"threshold_onset\": \"8/8\", \"TY_granger\": \"4/8\", \"naive_xcorr_fwd\": \"8/8\", \"diff_xcorr_fwd\": \"4/8\", \"detection_rate_k4\": 0.25, \"drift_pct\": {\"token_entropy\": -18.53, \"ece\": 651.26, \"perplexity\": -1.27, \"distinct_1\": -36.38, \"distinct_2\": -49.45, \"distinct_3\": -50.04, \"effective_rank\": 22.21, \"mauve\": -17.78}, \"gen0\": {\"token_entropy\": 3.234, \"ece\": 0.0108, \"perplexity\": 26.95, \"distinct_1\": 0.098, \"distinct_2\": 0.514, \"distinct_3\": 0.813, \"effective_rank\": 46.61, \"mauve\": 0.0311}, \"gen10\": {\"token_entropy\": 2.635, \"ece\": 0.0812, \"perplexity\": 26.61, \"distinct_1\": 0.0623, \"distinct_2\": 0.26, \"distinct_3\": 0.406, \"effective_rank\": 56.96, \"mauve\": 0.0256}, \"consensus_detail\": {\"K4_pairs\": [\"token_entropy->distinct_1\", \"ece->distinct_1\"], \"K3_pairs\": [\"token_entropy->distinct_2\", \"token_entropy->mauve\", \"ece->distinct_2\", \"ece->mauve\"], \"K2_pairs\": [\"token_entropy->distinct_3\", \"ece->distinct_3\"]}, \"n_generations\": 11, \"precision\": \"fp32\", \"onset_conclusion\": \"PermG=0/8 confirms onset >= 0.35; combined with a040(0/8) and a050(6/8), onset in [0.40, 0.50]\"}}, \"alpha_sweep_a025_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"0/8\", \"PermG_rev\": \"0/8\", \"K_ge_4\": \"0/8\", \"MMCT\": \"0/8\", \"MMCT_detection_rate\": 0, \"d1_drift_pct\": -39.15, \"d2_drift_pct\": -54.75, \"d3_drift_pct\": -56.98, \"mauve_drift_pct\": -41.86, \"entropy_drift_pct\": -4.79, \"ece_drift_pct\": 79.17, \"ppl_drift_pct\": -18.09, \"eff_rank_drift_pct\": -3.78, \"ppl_by_gen\": [26.95, 19.39, 20.37, 20.75, 21.14, 21.3, 21.48, 21.88, 21.9, 22.25, 22.07], \"entropy_by_gen\": [3.234, 2.983, 3.015, 3.039, 3.051, 3.034, 3.049, 3.067, 3.063, 3.104, 3.079], \"d1_by_gen\": [0.098, 0.0976, 0.0815, 0.0737, 0.0688, 0.0657, 0.0635, 0.0614, 0.061, 0.0601, 0.0596], \"mauve_by_gen\": [0.0311, 0.0314, 0.0326, 0.0318, 0.0314, 0.0272, 0.0242, 0.0221, 0.0207, 0.0207, 0.0181], \"naive_xcorr_fwd\": \"8/8\", \"diff_xcorr_fwd\": \"3/8\", \"threshold_onset_fwd\": \"5/8\", \"ty_granger_sig\": \"3/8\", \"consensus_detail_max_votes\": 3, \"hypothesis_validated\": true, \"note\": \"PermG=0/8 confirms α=0.25 is below phase transition. d1_drift=-39.15% is surprisingly large (> α=0.50's -28.7%), suggesting diversity collapse proceeds without Granger-detectable lead-lag at this α. token_entropy→distinct_1 had raw PermG p=0.007 but FDR-corrected p=0.053 (borderline).\"}}, \"alpha_sweep_a010_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"token_entropy_drift_pct\": -4.59, \"distinct_1_drift_pct\": -23.8, \"distinct_2_drift_pct\": -27.15, \"distinct_3_drift_pct\": -19.36, \"perplexity_drift_pct\": -18.94, \"perm_granger_fwd\": \"0/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"3/8\", \"threshold_onset_fwd\": \"5/8\", \"consensus_k4\": \"2/8\", \"mmct_wpair_fwd\": \"2/8\", \"mmct_detection_rate\": 0.25, \"precision\": \"fp32\", \"padding_side_fix\": \"D093 applied\", \"blind_zone_confirmed\": true, \"cross_seed_permg_stable\": true}}, \"alpha_sweep_a005_s42_v3\": {\"status\": \"DONE\", \"metrics\": {\"final_ppl\": 20.81, \"final_entropy\": 3.04, \"final_eff_rank\": 45.3, \"final_mauve\": 0.023, \"precision\": \"fp32\", \"token_entropy_drift\": -5.96, \"ece_drift\": 55.41, \"perplexity_drift\": -22.78, \"distinct_1_drift\": -24.86, \"distinct_2_drift\": -28.42, \"distinct_3_drift\": -19.54, \"perm_granger_fwd\": \"0/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"3/8\", \"threshold_onset_fwd\": \"5/8\", \"consensus_k4\": \"0/8\", \"mmct_wpair_fwd\": 0}}, \"alpha_sweep_a010_s42_bf16\": {\"status\": \"PREPARING\"}, \"scale_14b_a050_s42_bf16\": {\"status\": \"PREPARING\"}, \"interv_react_s43\": {\"status\": \"PREPARING\"}, \"alpha_sweep_a040_s42_fp32_v2\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"0/8\", \"PermG_rev\": \"0/8\", \"K4_3sigma\": \"0/8\", \"K3_3sigma\": \"1/8\", \"threshold_onset_3sigma\": \"8/8\", \"naive_xcorr\": \"4/8\", \"diff_xcorr\": \"0/8\", \"TY_granger\": \"4/8\", \"drift_token_entropy\": \"-19.13%\", \"drift_ece\": \"+736.90%\", \"drift_distinct1\": \"-35.48%\", \"drift_distinct2\": \"-48.01%\", \"drift_distinct3\": \"-48.42%\", \"drift_mauve\": \"-23.04%\", \"drift_perplexity\": \"+5.36%\", \"D111_direction_check\": \"applied: naive 8/8→4/8, diff 3/8→0/8, K3 6/8→1/8, K4 1/8→0/8\"}}, \"alpha_sweep_a030_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"permg_fwd\": \"0/8\", \"permg_rev\": \"0/8\", \"k_ge3\": \"3/8\", \"k_ge4\": \"3/8\", \"naive_xcorr\": \"5/8\", \"diff_xcorr\": \"3/8\", \"threshold_onset\": \"8/8\", \"ty_granger\": \"5/8\", \"drift_entropy_pct\": -17.32, \"drift_ece_pct\": 549.38, \"drift_d1_pct\": -36.72, \"drift_d2_pct\": -49.75, \"drift_d3_pct\": -50.09, \"drift_mauve_pct\": -26.09, \"n_generations\": 11, \"n_perm\": 5000, \"D111_direction_check\": \"applied: naive 8/8→5/8, diff 4/8→3/8, K3 6/8→3/8, K4 unchanged 3/8\"}}, \"alpha_sweep_a045_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"permg_fwd\": 0, \"permg_rev\": 0, \"k_ge3\": 3, \"k_ge4\": 0, \"naive_xcorr\": 7, \"diff_xcorr\": 3, \"threshold_onset\": 8, \"ty_granger\": 1, \"total_pairs\": 8, \"drift_entropy_pct\": -18.73, \"drift_ece_pct\": 770.37, \"drift_d1_pct\": -35.39, \"drift_d2_pct\": -47.87, \"drift_d3_pct\": -47.79, \"drift_perplexity_pct\": 12.19, \"drift_mauve_pct\": -24.89, \"drift_effrank_pct\": 23.41, \"gen0_token_entropy\": 3.2342, \"gen10_token_entropy\": 2.6283, \"gen0_ece\": 0.0108, \"gen10_ece\": 0.094, \"gen0_distinct_1\": 0.098, \"gen10_distinct_1\": 0.0633, \"gen0_perplexity\": 26.949, \"gen10_perplexity\": 30.234, \"gen0_mauve\": 0.0311, \"gen10_mauve\": 0.0234, \"onset_boundary\": \"[0.45, 0.50]\"}}, \"c4_a075_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"8/8\", \"PermG_rev\": \"0/8\", \"K_ge_3_3sigma\": \"6/8\", \"K_ge_4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"8/8\", \"naive_xcorr\": \"0/8\", \"diff_xcorr\": \"0/8\", \"TY_granger\": \"6/8\", \"drift_token_entropy\": -35.32, \"drift_ece\": 2809.23, \"drift_perplexity\": 2152.6, \"drift_distinct_1\": -12.4, \"drift_distinct_2\": -15.41, \"drift_distinct_3\": -14.59, \"drift_mauve\": -42.26, \"drift_effective_rank\": 110.31, \"gen0_token_entropy\": 3.1094, \"D111_direction_check\": \"applied: naive 8/8→0/8, diff 8/8→0/8, K3 8/8→6/8, K4 8/8→0/8\"}}, \"c4_a050_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"permg_fwd_fdr_sig\": \"8/8\", \"permg_rev_fdr_sig\": \"7/8\", \"consensus_K4_3sigma\": \"2/8\", \"consensus_K3_3sigma\": \"6/8\", \"threshold_onset_3sigma\": \"8/8\", \"naive_xcorr_sig\": \"4/8\", \"diff_xcorr_fdr_sig\": \"0/8\", \"ty_granger_sig\": \"4/8\", \"mmct_detection_rate\": 0.75, \"drift_token_entropy_pct\": -47.99, \"drift_distinct1_pct\": -9.78, \"drift_distinct2_pct\": -15.72, \"drift_distinct3_pct\": -17.75, \"drift_perplexity_pct\": 2931.59, \"drift_mauve_pct\": -54.25, \"drift_ece_pct\": 3103.74, \"gen0_token_entropy\": 3.109, \"gen10_token_entropy\": 1.617, \"D111_direction_check\": \"applied: naive 8/8→4/8, diff 8/8→0/8, K3 8/8→6/8, K4 8/8→2/8\"}}, \"c4_a025_s42_fp32\": {\"status\": \"DONE\", \"metrics\": {\"permg_fwd_fdr\": \"0/8\", \"permg_rev_fdr\": \"0/8\", \"consensus_K3_3sigma\": \"0/8\", \"consensus_K4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"8/8\", \"naive_xcorr\": \"3/8\", \"diff_xcorr\": \"0/8\", \"ty_granger\": \"3/8\", \"drift_token_entropy\": \"-53.01%\", \"drift_ece\": \"+3242.80%\", \"drift_perplexity\": \"+3617.05%\", \"drift_d1\": \"-4.10%\", \"drift_d2\": \"-8.78%\", \"drift_d3\": \"-11.95%\", \"drift_mauve\": \"-52.08%\", \"drift_effective_rank\": \"+111.90%\", \"D111_direction_check\": \"applied: naive 8/8→3/8, diff 8/8→0/8, K3 8/8→0/8, K4 3/8→0/8\"}}, \"scale_14b_c4_s42_fp32\": {\"status\": \"RUNNING\"}, \"method_ablation_phase3\": {\"status\": \"DONE\", \"metrics\": {\"n_alpha_points\": 10, \"alphas\": [0, 0.05, 0.1, 0.25, 0.35, 0.4, 0.5, 0.6, 0.75, 1], \"naive_sig_rates\": [1, 0.875, 0.875, 1, 1, 1, 1, 0.875, 0.875, 1], \"diff_sig_rates\": [0.5, 0.375, 0.75, 0.375, 0.5, 0.375, 0.875, 1, 0.75, 0.75], \"thresh_3sigma_rates\": [0.5, 0.625, 0.625, 0.625, 1, 1, 1, 1, 1, 1], \"permG_fwd_rates\": [0, 0, 0, 0, 0, 0, 0.75, 0.375, 0.75, 0.75], \"permG_rev_rates\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"TY_rates\": [0.25, 0.375, 0.375, 0.375, 0.5, 0.5, 0.5, 1, 1, 0.375], \"K_ge3_rates\": [0.375, 0.375, 0.5, 0.5, 0.75, 0.75, 0.875, 1, 0.875, 0.75], \"K_ge4_rates\": [0, 0, 0.25, 0, 0.25, 0.125, 0.75, 0.875, 0.75, 0.75], \"regime_structure\": {\"null\": \"alpha<=0.40: PermG=0%, naive=87-100% FPR. 11 data points all PermG=0/8\", \"onset\": \"alpha=[0.40,0.50]: PermG jumps 0→75%, K≥4 jumps 0→75%\", \"sync_collapse\": \"alpha=0.60: PermG drops to 37.5% (non-monotonic, D108). BUT K≥4 peaks at 87.5% — TY complements PermG (TY=100% here vs 50% at α=0.50). MMCT multi-method consensus strongest at this α\", \"detection\": \"alpha>=0.75: PermG=75%, TY non-monotonic drop to 37.5-100%\"}, \"claim3_support\": \"strong: 4-regime dose-response with non-monotonic PermG at α=0.60 (sync collapse) and TY complementarity. Method choice directly determines conclusion validity. PermG 0% FPR in null regime = cleanest discriminator.\", \"D105_standard\": \"3sigma + FDR BH + n_perm=5000 + unified 8-pair\"}}, \"smollm3_3b_wiki_a100_s42_v3\": {\"status\": \"DONE\", \"metrics\": {\"PermG_fwd\": \"3/8\", \"PermG_rev\": \"0/8\", \"robust_pairs_K4_3sigma\": \"0/8\", \"robust_pairs_K3_3sigma\": \"0/8\", \"robust_pairs_K3_2sigma\": \"6/8\", \"robust_pairs_K4_2sigma\": \"3/8\", \"threshold_onset_3sigma\": \"0/8\", \"threshold_onset_2sigma\": \"8/8\", \"naive_xcorr\": \"4/8\", \"diff_xcorr\": \"6/8\", \"ty_granger\": \"0/8\", \"note\": \"D105+D111: FDR per-method, 3sigma, direction-checked. K≥3 corrected 3/8→0/8: 3sigma_recompute_v2 had naive_xcorr direction-blind bug (ECE pairs peak_lag<0 wrongly counted). Authoritative source: 5method_leadlag.json with peak_lag>0 check. PermG_fwd=3/8 (ECE→d1/d2/d3 via diff_xcorr+permG). naive_xcorr corrected 8/8→4/8 (entropy pairs only, ECE pairs all lag<0).\"}}, \"gen_gpt2m_a100_s43\": {\"status\": \"PREPARING\"}, \"qwen35_dryrun_launch\": {\"status\": \"PREPARING\"}, \"scale_69b_a100_s43_fp32\": {\"status\": \"PREPARING\"}, \"interv_react_s43_fp32\": {\"status\": \"DONE\", \"metrics\": {\"trigger_gen\": 2, \"trigger_distinct1_drop_pct\": -15.83, \"gen2_ppl\": 158.22, \"recovery_ppl\": 21.98, \"recovery_complete_by_gen\": 3, \"intervention_metric\": \"distinct_1\", \"intervention_threshold\": 0.1, \"intervention_alpha\": 0, \"gen0\": {\"token_entropy\": 3.234, \"perplexity\": 26.949, \"distinct_1\": 0.098}, \"gen9\": {\"token_entropy\": 3.079, \"perplexity\": 21.357, \"distinct_1\": 0.089}, \"gen10\": {\"token_entropy\": 3.088, \"perplexity\": 21.387, \"distinct_1\": 0.083}, \"note\": \"reactive intervention triggered at gen2 (d1=0.083 < threshold=0.1), alpha 1.0→0.0; ppl spike 26.9→158.2 recovered by gen3 to 22.0; d1 partial recovery 0.098→0.083→0.089\"}}, \"scale_69b_a100_s43\": {\"status\": \"RUNNING\"}, \"qwen35_08b_wiki_a100_s43_fp32\": {\"status\": \"RUNNING\"}, \"generalize_pythia1b_c4_a100_s42_v2\": {\"status\": \"DONE\", \"metrics\": {\"robust_pairs_K4_3sigma\": \"4/8\", \"robust_pairs_K3_3sigma\": \"8/8\", \"threshold_onset_3sigma\": \"0/8\", \"D105_3sigma_note\": \"D105 backfill: true 3sigma, fdr_permethod, unified 8-pair (canary={token_entropy,ece} x downstream={d1,d2,d3,mauve})\"}}}, \"count\": 50, \"total\": 118, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4314}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also check the existing registry entries for the experiments I'm updating to see what the old metrics look like and compare.

Key findings from registry:

1. **generalize_pythia410m_wiki_a100_s42** (wiki α=1.0, 410M baseline): K3=6/8 (from D111 metrics)
2. **padding_robustness_a100_s42_fp32** (padding α=1.0): Existing metrics show K4=6/8, K3=6/8, threshold_onset_3sigma=0/8
   
Now I'm compiling the D120 results and comparing them against the existing registry data. The key difference is that the old metrics were computed using the D111 direction checking method with naive/diff applied separately, while the D120 recomputation uses the integrated analysis pipeline with D105 true 3σ thresholds. Looking at the c4_a025_s42_fp32 experiment results showing all zeros across permutation FDR and K metrics.

Let me recount the method consensus across the different metrics—I'm seeing token_entropy and ece metrics each with 5 variants (distinct_1, distinct_2, distinct_3, and mauve), and I need to tally which methods appear in each to get an accurate count of naive versus diff versus threshold approaches.

Now looking at the forward significance results, diff_xcorr is showing perfect agreement across all 8 pairs in both directions, while naive only captures 4 pairs and threshold just 2, with permutation and TY methods not detecting any significant relationships.

The diff_xcorr bidirectional significance at this FDR threshold is suspicious given its high false positive rate, but the direction filter should already be working since the consensus data has the D111 check applied through peak lag values—all the forward lags are negative, indicating the canary consistently leads. Yet somehow diff_xcorr is still reporting significance in both directions, which suggests the reverse direction might be picking up spurious correlations that the lag-based filter isn't catching.

Looking at the consensus output more carefully, it's filtering for methods that agree on forward significance specifically, so the voting mechanism across all methods (naive, diff, threshold, perm, TY) is checking both the statistical significance and the direction constraint—whether that's through peak lag, lead time, or whatever directional information each method provides. For c4_a025, the consensus shows zero robust pairs where three or more methods agree on forward significance, which is the key takeaway.

Generating markdown table... Generating markdown table...

Now I'm double-checking the naive_fwd counts across the different configurations. For c4_a025, naive appears in 4 out of 8 cases while diff shows up in all 8. For c4_a050, naive only appears in 4 cases as well, but I need to verify this more carefully across the entropy and ECE metrics. Looking at the performance metrics for c4_a075, all methods are performing consistently well across both token entropy and ECE metrics, with perfect scores on the forward FDR tests for both naive and diff approaches.

Now examining the padding configuration, I'm seeing a different pattern—the mauve metric shows no successful methods while the distinct variants maintain the same 3/5 success rate, and the overall forward FDR scores drop to 6/8 for both naive and diff approaches.

Looking at the consensus votes, there's a constraint I need to account for: TY consistently returns N/A and threshold_onset caps at 0/8 when α≥0.50, which means K≥4 should theoretically be 0/8 across all experiments. But the old registry entries for c4_a075_s42 and c4_a050_s42 show different values—6/8 and 2/8 respectively—which suggests the earlier computations either used a different threshold_onset calculation, applied different D111 direction filtering, or had TY working in some capacity.

Examining the old registry data more closely, I can see that the previous analysis had TY=8/8 and threshold_onset=8/8, yielding K≥4=6/8. The D120 recomputation reveals a critical divergence: TY now fails with an API error (VARResults.test_causality() doesn't accept the 'signonly' argument) and threshold_onset drops to 0/8 under the stricter 3σ threshold. This represents a substantial shift in the results.

Looking at the pattern across samples, K≥4 collapses from 6/8 down to 0/8 for c4_a075_s42, and similarly for c4_a050_s42 where it goes from 6/8 or 2/8 to 0/8. The TY error appears to be a statsmodels API incompatibility rather than a genuine scientific finding, which I should flag separately. Checking back at the s43 experiments, I notice TY_granger does produce values there (0/8 for c4_a050_s43 and 1/8 for c4_a075_s43), so the issue might be specific to certain configurations or the method_ablation_phase3 setup.

The `signonly` keyword argument error is likely due to a statsmodels version mismatch between westd-17855 and where the earlier analyses ran. I'll note this in the report and focus on the core D120 metrics instead. Now comparing the padding robustness results against the wiki baseline at α=1.0, where the registry shows K3=6/8 with detailed breakdowns across different methods, while the D120 recomputation shows PermG_fwd at 6/8.

Looking at the full padding experiment results, I see PermG_rev drops to 0/8 and the mauve pairs both fail with 0/5 votes, whereas the wiki baseline may have handled these differently. The PermG asymmetry (6/8 forward, 0/8 reverse) mirrors the wiki pattern, and the threshold_onset_3sigma stays at 0/8. Checking the existing padding registry entry to verify these metrics are properly recorded...

Writing config JSON... The maximum vote across methods is only 3 out of 5 since TY is broken, which explains why K≥4 drops to zero. This TY failure on this particular environment is artificially suppressing the consensus metrics. Looking at the old C4 registry data, I can see the direction check applied different filters to each method—naive went from 8/8 down to 3/8, diff collapsed to 0/8, and the consensus metrics also dropped significantly.

Now recomputing D120 shows some striking shifts: threshold_onset plummets from 8/8 to 2/8 when using the true 3σ calculation from D105, while diff_xcorr unexpectedly jumps from 0/8 to 8/8 with FDR significance, and naive_xcorr ticks up slightly to 4/8.

Let me trace back through the direction check logic—the old metrics show diff was zeroed out to 0/8 after D111's direction filtering, but now the JSON clearly shows diff_xcorr_fdr_forward_sig at 8, meaning diff is appearing across all pairs. Checking the actual peak lags in the data confirms the forward direction signals are there, so something about how the direction check was applied has shifted. The bidirectional significance in diff_xcorr confirms there's no real directional signal here, just high correlation at low α values. Now I'm ready to write the report and update the registry, but I need to verify which D120 field names are already in use so I can maintain consistency. I see that the D120-recomputed metrics use the same field names as the regular metrics, so they're replacements rather than separate entries. Now I need to update the four experiments by replacing their existing metrics with the D120-recomputed values, being careful to preserve the structure while updating each one.

I'm noticing the TY error is significant enough to flag in the report—it might be a statsmodels version mismatch on that machine. My plan is to batch update the registry for all four experiments by updating their metrics fields, then write up the report and register the artifact.

The tricky part is figuring out whether update_registry replaces the entire metrics object or merges into it. Looking at the API, it seems to take individual field updates, so I need to decide whether to pass the complete metrics dict or update specific subfields to avoid wiping existing data. I'm looking at the complete metrics for this experiment and need to preserve the drift measurements while swapping in the new D120 lead-lag values. Let me construct the full updated metrics dictionary by combining the existing drift data with the fresh D120 results for each experiment. Now I'm looking at the performance metrics for another model configuration, c4_a050_s42_fp32, which shows different results across the same set of tests—some passing more permutation tests, others showing varying levels of drift across different metrics. Looking at the performance metrics for the c4_a075_s42_fp32 configuration, I'm seeing strong directional agreement in the permutation tests with perfect forward correlation but no reverse correlation, and consistent 3-sigma threshold detection across all eight runs. Now I'm looking at the robustness metrics for the A100 with FP32 precision, checking the permutation test results and cross-correlation scores across different detection methods.

I notice the K4 threshold metric dropped from 6/8 to 0/8 compared to the previous padding configuration—the Granger causality test was contributing before but is now broken with an API error. The mauve token pairs consistently fail across all methods with weak or reversed correlations, suggesting they're just noise rather than genuine signal. My results align with the wiki baseline for K3 matching, and switching the padding side doesn't seem to affect the lead-lag detection in any meaningful way.

This TY_granger breakage is affecting all D120 analyses on this server, which is a significant issue I should track. I'm checking whether the c4_a075_s43 entry, which shows TY_granger working at 1/8, was computed on a different server or if there's something else explaining the inconsistency.

The root cause appears to be a statsmodels version mismatch on westd-17855 — the test_causality method doesn't recognize the signonly parameter being passed. Since the other four methods (naive, diff, perm, threshold_onset) still work and K≥3 is achievable without TY, I can proceed with the analysis. However, K≥4 becomes impossible without TY or threshold_onset, so those results will naturally be 0/8 across all experiments.

Now I'm checking the old metrics to verify the K_ge_4 count for c4_a075_s42 — looking at the breakdown where TY and threshold_onset both hit 8/8, I need to trace through which pairs had 4+ methods agreeing to confirm that 6/8 figure.

With D120, the situation changes dramatically: TY is broken at 0/8 and threshold_onset drops to 0/8 as well, leaving only naive, diff, and perm as viable methods — a maximum of 3 out of 5, which means K≥4 becomes impossible at 0/8. The real question is whether this collapse is a genuine effect or partly an artifact of TY failing, since if TY had worked, the threshold_onset drop alone wouldn't have killed K≥4 entirely.

I should separate the TY issue from the D120 analysis and focus on what's actually changed with threshold_onset. Then I'll move on to writing the report and updating the registry, starting with a careful recount of the naive_xcorr consensus across the method pairs.

Looking at the significance patterns for c4_a025_s42, naive methods show up in 4 out of 8 pairs, diff is consistent across all of them, threshold only appears in 2 pairs, and permutation and TY don't register at all. For c4_a050_s42, I'm seeing a different distribution where naive, diff, and permutation all appear more frequently across the pairs.

Now examining c4_a075_s42, all eight pairs respond to naive, diff, and permutation methods equally, with perfect agreement on the K≥3 threshold but nothing reaching K≥4. Moving into padding_a100_s42, the token entropy and distinct metrics are starting to show similar patterns with naive and diff methods appearing across the first two pairs. Comparing the padding experiment to the wiki baseline, both show K3=6/8 and PermG=6/8, suggesting the padding side doesn't influence the lead-lag detection signature. The wiki baseline had some threshold and type-checking failures that the padding experiment doesn't replicate, but the core permutation and naive/diff pattern remains consistent. Now I'm checking the FDR values for the padding PermG_fwd results to understand the statistical significance better. I'm noticing a discrepancy between the displayed FDR value of 0.5187 and what's actually in the JSON data, which shows p_fdr=0.006132 and marks it as significant. The 0.5187 appears to be either a display error or coming from a different calculation, so I need to figure out which column is actually being referenced in the output. The F statistic matches between the table and JSON, but the PermFDR values are completely different — 0.5187 in the table versus 0.006132 in the JSON — which suggests either the columns are misaligned in the output or the table is displaying a different metric altogether, possibly an overall FDR across both directions rather than the directional p-value. the JSON is the authoritative source here—it shows significant_fdr=true for 6 out of 8 forward pairs with a p_fdr of 0.006132, which is what the consensus actually uses rather than the table's combined PermFDR across all 16 tests. Checking the consensus confirms this: perm_granger appears in 6 of 8 pairs and the summary shows perm_granger_fdr_forward_sig=6, so the numbers align.

Now I need to update the registry with the new metrics and write up the report. I'll structure the registry fields following the naming convention from the s43 D120 entries, including PermG_fdr forward and reverse, K-sigma thresholds, xcorr metrics, Granger analysis results, and experiment-specific parameters like drift metrics and permutation counts. Let me work through the registry updates and report writing together.

For the registry metrics field, I'm preserving all the existing metrics from c4_a025_s42_fp32 while incorporating the D120 analysis results...

Updating registry metrics... Compiling the full metrics snapshot for D120, including the Granger causality result that errored out, along with the drift measurements across entropy, perplexity, and ranking metrics, plus the analysis parameters and timestamp for when this was recomputed.

Now I'm noticing a dramatic shift in the diff_xcorr results — it went from completely failing the direction check to passing all eight cases, which is unexpected. The old D111 logic was filtering out pairs where the peak lag pointed the wrong way, but something's changed in how that's being evaluated or computed. The C009 fix corrected the peak_lag sign check from > 0 to < 0, which properly identifies forward direction (canary leading downstream), explaining why the diff_xcorr results jumped from 0/8 to 8/8 forward pairs. The naive_xcorr improvement from 3/8 to 4/8 likely stems from this direction fix combined with the integrated FDR computation. D120's recomputation cleanly applies all the fixes together—the true 3σ threshold, corrected direction filtering, and sign adjustment—so the results are now consistent. Now I'm ready to update the registry for all four experiments and compile the report, though I'm curious about that c4_a050_s42 PermG_rev result of 7/8.

Looking at the JSON data, PermG shows 7 out of 8 reverse pairs are significant at α=0.50 for C4, which is striking—this indicates bidirectional Granger causality in the cross-domain setting, whereas the wiki domain typically shows 6/8 forward and 0/8 reverse at the same threshold. The C4 corpus appears to create much stronger mutual feedback between canary and downstream metrics, likely because it's more diverse and the synthetic contamination at α=0.50 generates tighter coupling in both directions.

Now I'll organize the report with a summary table, per-experiment breakdowns, padding versus wiki comparisons, the TY API error note, and key findings, then proceed with the registry updates.

Generating markdown table... Generating markdown table...

There's a statsmodels version incompatibility causing the Granger API to fail across all four experiments on this server—it's throwing an error about an unexpected keyword argument. This means TY is returning N/A for everything, which caps the maximum possible score at 0/8 since only three methods can contribute without it. Interestingly, the same experiments worked fine on other servers, so this is isolated to the current setup.

Looking at the comparison between the old registry and D120, I'm seeing some significant shifts: the threshold onset detection improved dramatically from 8/8 to 2/8 with the 3σ adjustment, the differential cross-correlation went from completely failing to working perfectly after the C009 sign fix, and there's a notable recovery in bidirectional PermG at the higher alpha level. However, some methods like naive cross-correlation and K3 show minor degradation, and K4 is now completely broken due to the TY issue. I'm seeing conflicting entries for c4_a075_s42 across different registry versions—one shows naive_xcorr at 7/8 in the lead_lag metrics, while another update has it at 0/8 with a D111 direction check applied. I need to determine which is the authoritative current state before updating the comparison table. Generating comparison table...

I'm noticing the PermG_fwd metric jumped from 6/8 to 8/8 between versions, which suggests either the D105 3σ threshold adjustment or a change in how FDR was computed affected this result. Let me trace back when that shift occurred in the update history.

For c4_a075_s42 at D120, K3 is restored to 8/8 thanks to the C009 fix that recovered the naive and diff metrics from their broken 0/8 state, while K4 remains at 0/8 due to the TY issue. Now looking at c4_a025_s42, I'm seeing a different pattern where naive dropped from 8/8 down to 3/8 after the buggy update, then partially recovered to 4/8 by D120, while diff went 8/8 → 0/8 → 8/8, and K3 stayed stuck at 0/8 throughout.

Let me trace through the naive cross-correlation peak lags for c4_a025 to understand which comparisons are actually showing forward causality at α=0.25—I'm checking each metric pair to see if the peak lag is negative (forward) or positive (reverse).

Looking at the complete set: token_entropy pairs give me 2/4 forward (d1 and mauve), while ece pairs also give 2/4 forward (d1 and mauve). So across both metrics, only the d1 and mauve comparisons align with the expected direction, confirming that the signal at this lower alpha is quite noisy.

Now I'm ready to move forward with the registry updates and write up the findings. The key takeaway for the report is the dose-response pattern across alpha values: at α=0.25 both PermG and K3 fall below detection threshold, α=0.50 shows the transition zone where PermG fully detects but K3 is partial, and α=0.75 achieves full detection across both methods.

The C4 domain shows something unusual at α=0.50 with 7/8 reverse PermG results, which doesn't match the typical wiki baseline of 0/8 reverse at this alpha level—this could point to mutual feedback dynamics in the cross-domain setting. The padding audit confirms K3 stays at 6/8 matching the wiki baseline, so padding placement isn't introducing artifacts. I'll note that K4 is completely broken on token 17855 due to a statsmodels API issue, so those results are unusable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "05b9c3ee-8612-44ab-9e1b-8eb1b2914745",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011q1hRicRWvR9r2VpbvK1Dh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12377,
      "cache_read_input_tokens": 59815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12377
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

_source line 53_

全部 4 个实验的 JSON 已获取。现在查到 wiki α=1.0 基线 (`generalize_pythia410m_wiki_a100_s42`) 的 K3=6/8。开始更新 registry 和写报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "9a29a68c-6cb9-4096-a353-75f9208c3836",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011q1hRicRWvR9r2VpbvK1Dh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12377,
      "cache_read_input_tokens": 59815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12377
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

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Ev68k4AfvusibnLnRUNsNx`</summary>

```json
{
  "exp_id": "c4_a025_s42_fp32",
  "field": "metrics",
  "value": {
    "PermG_fwd": "0/8",
    "PermG_rev": "0/8",
    "K_ge_3_3sigma": "0/8",
    "K_ge_4_3sigma": "0/8",
    "threshold_onset_3sigma": "2/8",
    "naive_xcorr": "4/8",
    "diff_xcorr": "8/8",
    "TY_granger": "N/A (signonly API error on 17855)",
    "drift_token_entropy": "-53.01%",
    "drift_ece": "+3242.80%",
    "drift_perplexity": "+3617.05%",
    "drift_d1": "-4.10%",
    "drift_d2": "-8.78%",
    "drift_d3": "-11.95%",
    "drift_mauve": "-52.08%",
    "drift_effective_rank": "+111.90%",
    "D105_3sigma": "true 3sigma (std of full series)",
    "D111_direction": "peak_lag < 0 (C009 corrected)",
    "analysis_script": "run_5method_analysis_d102.py",
    "n_perm": 5000,
    "D120_recomputed": "2026-05-20",
    "D102_8pair": "canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]"
  },
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "35bb06c6-d209-4bc3-b45b-46704a2960cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011q1hRicRWvR9r2VpbvK1Dh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12377,
      "cache_read_input_tokens": 59815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12377
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

_source line 55 · 2026-05-20T06:09:20.373Z_

<details><summary>↩ Tool result · `toolu_01Ev68k4AfvusibnLnRUNsNx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"c4_a025_s42_fp32\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T18:30:39.613Z\", \"updated_at\": \"2026-05-20T06:09:19.816Z\", \"hypothesis\": \"C4 跨域 onset 比较：WikiText onset ∈ (0.40, 0.50) 全部 PermG=0/8。C4 在 α=0.50 已是 8/8（fp32）。如果 C4 α=0.25 PermG>0 → C4 onset 显著低于 WikiText，跨域灵敏度差异是论文级发现。Claim 2 cross-domain。\", \"parent\": \"c4_a050_s42_fp32\", \"spec\": {\"command\": \"python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/c4_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/c4_a025_s42_fp32\", \"server\": \"westd-17855\", \"data_path\": \"data/c4_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"precision\": \"fp32\", \"gpu\": [\"cuda:5\"], \"pid\": \"178625\", \"checkpoint_source\": \"EleutherAI/pythia-410m (training from scratch)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"results/alpha_sweep/c4_a025_s42_fp32/gen_10/checkpoint\", \"log_path\": \"results/alpha_sweep/c4_a025_s42_fp32/analysis_results.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T22:14:56.027Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T22:14:59.957789+00:00\"}]}, \"metrics\": {\"PermG_fwd\": \"0/8\", \"PermG_rev\": \"0/8\", \"K_ge_3_3sigma\": \"0/8\", \"K_ge_4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"2/8\", \"naive_xcorr\": \"4/8\", \"diff_xcorr\": \"8/8\", \"TY_granger\": \"N/A (signonly API error on 17855)\", \"drift_token_entropy\": \"-53.01%\", \"drift_ece\": \"+3242.80%\", \"drift_perplexity\": \"+3617.05%\", \"drift_d1\": \"-4.10%\", \"drift_d2\": \"-8.78%\", \"drift_d3\": \"-11.95%\", \"drift_mauve\": \"-52.08%\", \"drift_effective_rank\": \"+111.90%\", \"D105_3sigma\": \"true 3sigma (std of full series)\", \"D111_direction\": \"peak_lag < 0 (C009 corrected)\", \"analysis_script\": \"run_5method_analysis_d102.py\", \"n_perm\": 5000, \"D120_recomputed\": \"2026-05-20\", \"D102_8pair\": \"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T22:20:21.543Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2665}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "75e4eba2-75b0-463f-93aa-d0444f29ba78",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"c4_a025_s42_fp32\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T18:30:39.613Z\\\", \\\"updated_at\\\": \\\"2026-05-20T06:09:19.816Z\\\", \\\"hypothesis\\\": \\\"C4 跨域 onset 比较：WikiText onset ∈ (0.40, 0.50) 全部 PermG=0/8。C4 在 α=0.50 已是 8/8（fp32）。如果 C4 α=0.25 PermG>0 → C4 onset 显著低于 WikiText，跨域灵敏度差异是论文级发现。Claim 2 cross-domain。\\\", \\\"parent\\\": \\\"c4_a050_s42_fp32\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/c4_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/c4_a025_s42_fp32\\\", \\\"server\\\": \\\"westd-17855\\\", \\\"data_path\\\": \\\"data/c4_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 42, \\\"precision\\\": \\\"fp32\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"178625\\\", \\\"checkpoint_source\\\": \\\"EleutherAI/pythia-410m (training from scratch)\\\", \\\"eval_data\\\": \\\"N/A (training experiment)\\\", \\\"checkpoint_path\\\": \\\"results/alpha_sweep/c4_a025_s42_fp32/gen_10/checkpoint\\\", \\\"log_path\\\": \\\"results/alpha_sweep/c4_a025_s42_fp32/analysis_results.json\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-19T22:14:56.027Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-19T22:14:59.957789+00:00\\\"}]}, \\\"metrics\\\": {\\\"PermG_fwd\\\": \\\"0/8\\\", \\\"PermG_rev\\\": \\\"0/8\\\", \\\"K_ge_3_3sigma\\\": \\\"0/8\\\", \\\"K_ge_4_3sigma\\\": \\\"0/8\\\", \\\"threshold_onset_3sigma\\\": \\\"2/8\\\", \\\"naive_xcorr\\\": \\\"4/8\\\", \\\"diff_xcorr\\\": \\\"8/8\\\", \\\"TY_granger\\\": \\\"N/A (signonly API error on 17855)\\\", \\\"drift_token_entropy\\\": \\\"-53.01%\\\", \\\"drift_ece\\\": \\\"+3242.80%\\\", \\\"drift_perplexity\\\": \\\"+3617.05%\\\", \\\"drift_d1\\\": \\\"-4.10%\\\", \\\"drift_d2\\\": \\\"-8.78%\\\", \\\"drift_d3\\\": \\\"-11.95%\\\", \\\"drift_mauve\\\": \\\"-52.08%\\\", \\\"drift_effective_rank\\\": \\\"+111.90%\\\", \\\"D105_3sigma\\\": \\\"true 3sigma (std of full series)\\\", \\\"D111_direction\\\": \\\"peak_lag < 0 (C009 corrected)\\\", \\\"analysis_script\\\": \\\"run_5method_analysis_d102.py\\\", \\\"n_perm\\\": 5000, \\\"D120_recomputed\\\": \\\"2026-05-20\\\", \\\"D102_8pair\\\": \\\"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T22:20:21.543Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.2665}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"c4_a025_s42_fp32\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T18:30:39.613Z\", \"updated_at\": \"2026-05-20T06:09:19.816Z\", \"hypothesis\": \"C4 跨域 onset 比较：WikiText onset ∈ (0.40, 0.50) 全部 PermG=0/8。C4 在 α=0.50 已是 8/8（fp32）。如果 C4 α=0.25 PermG>0 → C4 onset 显著低于 WikiText，跨域灵敏度差异是论文级发现。Claim 2 cross-domain。\", \"parent\": \"c4_a050_s42_fp32\", \"spec\": {\"command\": \"python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/c4_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/c4_a025_s42_fp32\", \"server\": \"westd-17855\", \"data_path\": \"data/c4_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"precision\": \"fp32\", \"gpu\": [\"cuda:5\"], \"pid\": \"178625\", \"checkpoint_source\": \"EleutherAI/pythia-410m (training from scratch)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"results/alpha_sweep/c4_a025_s42_fp32/gen_10/checkpoint\", \"log_path\": \"results/alpha_sweep/c4_a025_s42_fp32/analysis_results.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T22:14:56.027Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T22:14:59.957789+00:00\"}]}, \"metrics\": {\"PermG_fwd\": \"0/8\", \"PermG_rev\": \"0/8\", \"K_ge_3_3sigma\": \"0/8\", \"K_ge_4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"2/8\", \"naive_xcorr\": \"4/8\", \"diff_xcorr\": \"8/8\", \"TY_granger\": \"N/A (signonly API error on 17855)\", \"drift_token_entropy\": \"-53.01%\", \"drift_ece\": \"+3242.80%\", \"drift_perplexity\": \"+3617.05%\", \"drift_d1\": \"-4.10%\", \"drift_d2\": \"-8.78%\", \"drift_d3\": \"-11.95%\", \"drift_mauve\": \"-52.08%\", \"drift_effective_rank\": \"+111.90%\", \"D105_3sigma\": \"true 3sigma (std of full series)\", \"D111_direction\": \"peak_lag < 0 (C009 corrected)\", \"analysis_script\": \"run_5method_analysis_d102.py\", \"n_perm\": 5000, \"D120_recomputed\": \"2026-05-20\", \"D102_8pair\": \"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T22:20:21.543Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2665}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Nxb2SvU4C2Hmcpun8BqEtz`</summary>

```json
{
  "exp_id": "c4_a050_s42_fp32",
  "field": "metrics",
  "value": {
    "PermG_fwd": "8/8",
    "PermG_rev": "7/8",
    "K_ge_3_3sigma": "4/8",
    "K_ge_4_3sigma": "0/8",
    "threshold_onset_3sigma": "0/8",
    "naive_xcorr": "4/8",
    "diff_xcorr": "8/8",
    "TY_granger": "N/A (signonly API error on 17855)",
    "drift_token_entropy_pct": -47.99,
    "drift_ece_pct": 3103.74,
    "drift_perplexity_pct": 2931.59,
    "drift_d1_pct": -9.78,
    "drift_d2_pct": -15.72,
    "drift_d3_pct": -17.75,
    "drift_mauve_pct": -54.25,
    "gen0_token_entropy": 3.109,
    "D105_3sigma": "true 3sigma (std of full series)",
    "D111_direction": "peak_lag < 0 (C009 corrected)",
    "analysis_script": "run_5method_analysis_d102.py",
    "n_perm": 5000,
    "D120_recomputed": "2026-05-20",
    "D102_8pair": "canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]",
    "note": "PermG bidirectional (fwd=8/8 rev=7/8) — unique to C4 cross-domain at α=0.50"
  },
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "3aa23acc-51da-4494-ab28-669a015f6e95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011q1hRicRWvR9r2VpbvK1Dh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12377,
      "cache_read_input_tokens": 59815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12377
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

_source line 57 · 2026-05-20T06:09:25.416Z_

<details><summary>↩ Tool result · `toolu_01Nxb2SvU4C2Hmcpun8BqEtz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"c4_a050_s42_fp32\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:37:57.965Z\", \"updated_at\": \"2026-05-20T06:09:25.116Z\", \"hypothesis\": \"bf16 precision destroys PermG causal signal at C4 α=0.50; fp32 rerun should recover non-zero PermG fwd if the 0/8 was a precision artifact rather than a true blind zone\", \"parent\": \"alpha_sweep_c4_a050_s42\", \"spec\": {\"data_path\": \"data/c4_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"precision\": \"fp32\", \"padding_side_fix\": \"D093 applied\"}, \"server\": \"westd-17855\", \"gpu\": \"cuda:5\", \"pid\": \"152615\", \"log_path\": \"~/runs/distrib_canary_collapse/c4_a050_s42_fp32.log\", \"reproduce\": {\"command\": \"bash -c \\\"export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/c4_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/c4_a050_s42_fp32 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch\\\"\", \"finished_at\": \"2026-05-19T18:20:17.068Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:20:20.777203+00:00\"}]}, \"metrics\": {\"PermG_fwd\": \"8/8\", \"PermG_rev\": \"7/8\", \"K_ge_3_3sigma\": \"4/8\", \"K_ge_4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"0/8\", \"naive_xcorr\": \"4/8\", \"diff_xcorr\": \"8/8\", \"TY_granger\": \"N/A (signonly API error on 17855)\", \"drift_token_entropy_pct\": -47.99, \"drift_ece_pct\": 3103.74, \"drift_perplexity_pct\": 2931.59, \"drift_d1_pct\": -9.78, \"drift_d2_pct\": -15.72, \"drift_d3_pct\": -17.75, \"drift_mauve_pct\": -54.25, \"gen0_token_entropy\": 3.109, \"D105_3sigma\": \"true 3sigma (std of full series)\", \"D111_direction\": \"peak_lag < 0 (C009 corrected)\", \"analysis_script\": \"run_5method_analysis_d102.py\", \"n_perm\": 5000, \"D120_recomputed\": \"2026-05-20\", \"D102_8pair\": \"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\", \"note\": \"PermG bidirectional (fwd=8/8 rev=7/8) — unique to C4 cross-domain at α=0.50\"}, \"checkpoint_path\": \"westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:26:00.846Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7089}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "ffa94ffb-21ed-4df2-8e81-4efad64eb104",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"c4_a050_s42_fp32\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T14:37:57.965Z\\\", \\\"updated_at\\\": \\\"2026-05-20T06:09:25.116Z\\\", \\\"hypothesis\\\": \\\"bf16 precision destroys PermG causal signal at C4 α=0.50; fp32 rerun should recover non-zero PermG fwd if the 0/8 was a precision artifact rather than a true blind zone\\\", \\\"parent\\\": \\\"alpha_sweep_c4_a050_s42\\\", \\\"spec\\\": {\\\"data_path\\\": \\\"data/c4_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 42, \\\"precision\\\": \\\"fp32\\\", \\\"padding_side_fix\\\": \\\"D093 applied\\\"}, \\\"server\\\": \\\"westd-17855\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": \\\"152615\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/c4_a050_s42_fp32.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/c4_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/c4_a050_s42_fp32 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-19T18:20:17.068Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-19T18:20:20.777203+00:00\\\"}]}, \\\"metrics\\\": {\\\"PermG_fwd\\\": \\\"8/8\\\", \\\"PermG_rev\\\": \\\"7/8\\\", \\\"K_ge_3_3sigma\\\": \\\"4/8\\\", \\\"K_ge_4_3sigma\\\": \\\"0/8\\\", \\\"threshold_onset_3sigma\\\": \\\"0/8\\\", \\\"naive_xcorr\\\": \\\"4/8\\\", \\\"diff_xcorr\\\": \\\"8/8\\\", \\\"TY_granger\\\": \\\"N/A (signonly API error on 17855)\\\", \\\"drift_token_entropy_pct\\\": -47.99, \\\"drift_ece_pct\\\": 3103.74, \\\"drift_perplexity_pct\\\": 2931.59, \\\"drift_d1_pct\\\": -9.78, \\\"drift_d2_pct\\\": -15.72, \\\"drift_d3_pct\\\": -17.75, \\\"drift_mauve_pct\\\": -54.25, \\\"gen0_token_entropy\\\": 3.109, \\\"D105_3sigma\\\": \\\"true 3sigma (std of full series)\\\", \\\"D111_direction\\\": \\\"peak_lag < 0 (C009 corrected)\\\", \\\"analysis_script\\\": \\\"run_5method_analysis_d102.py\\\", \\\"n_perm\\\": 5000, \\\"D120_recomputed\\\": \\\"2026-05-20\\\", \\\"D102_8pair\\\": \\\"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\\\", \\\"note\\\": \\\"PermG bidirectional (fwd=8/8 rev=7/8) — unique to C4 cross-domain at α=0.50\\\"}, \\\"checkpoint_path\\\": \\\"westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T18:26:00.846Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7089}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"c4_a050_s42_fp32\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:37:57.965Z\", \"updated_at\": \"2026-05-20T06:09:25.116Z\", \"hypothesis\": \"bf16 precision destroys PermG causal signal at C4 α=0.50; fp32 rerun should recover non-zero PermG fwd if the 0/8 was a precision artifact rather than a true blind zone\", \"parent\": \"alpha_sweep_c4_a050_s42\", \"spec\": {\"data_path\": \"data/c4_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"precision\": \"fp32\", \"padding_side_fix\": \"D093 applied\"}, \"server\": \"westd-17855\", \"gpu\": \"cuda:5\", \"pid\": \"152615\", \"log_path\": \"~/runs/distrib_canary_collapse/c4_a050_s42_fp32.log\", \"reproduce\": {\"command\": \"bash -c \\\"export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/c4_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/c4_a050_s42_fp32 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch\\\"\", \"finished_at\": \"2026-05-19T18:20:17.068Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:20:20.777203+00:00\"}]}, \"metrics\": {\"PermG_fwd\": \"8/8\", \"PermG_rev\": \"7/8\", \"K_ge_3_3sigma\": \"4/8\", \"K_ge_4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"0/8\", \"naive_xcorr\": \"4/8\", \"diff_xcorr\": \"8/8\", \"TY_granger\": \"N/A (signonly API error on 17855)\", \"drift_token_entropy_pct\": -47.99, \"drift_ece_pct\": 3103.74, \"drift_perplexity_pct\": 2931.59, \"drift_d1_pct\": -9.78, \"drift_d2_pct\": -15.72, \"drift_d3_pct\": -17.75, \"drift_mauve_pct\": -54.25, \"gen0_token_entropy\": 3.109, \"D105_3sigma\": \"true 3sigma (std of full series)\", \"D111_direction\": \"peak_lag < 0 (C009 corrected)\", \"analysis_script\": \"run_5method_analysis_d102.py\", \"n_perm\": 5000, \"D120_recomputed\": \"2026-05-20\", \"D102_8pair\": \"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\", \"note\": \"PermG bidirectional (fwd=8/8 rev=7/8) — unique to C4 cross-domain at α=0.50\"}, \"checkpoint_path\": \"westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:26:00.846Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7089}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_019DB9uZdmWBcDQj68qhhwvk`</summary>

```json
{
  "exp_id": "c4_a075_s42_fp32",
  "field": "metrics",
  "value": {
    "PermG_fwd": "8/8",
    "PermG_rev": "0/8",
    "K_ge_3_3sigma": "8/8",
    "K_ge_4_3sigma": "0/8",
    "threshold_onset_3sigma": "0/8",
    "naive_xcorr": "8/8",
    "diff_xcorr": "8/8",
    "TY_granger": "N/A (signonly API error on 17855)",
    "drift_token_entropy": -35.32,
    "drift_ece": 2809.23,
    "drift_perplexity": 2152.6,
    "drift_distinct_1": -12.4,
    "drift_distinct_2": -15.41,
    "drift_distinct_3": -14.59,
    "drift_mauve": -42.26,
    "drift_effective_rank": 110.31,
    "gen0_token_entropy": 3.1094,
    "D105_3sigma": "true 3sigma (std of full series)",
    "D111_direction": "peak_lag < 0 (C009 corrected)",
    "analysis_script": "run_5method_analysis_d102.py",
    "n_perm": 5000,
    "D120_recomputed": "2026-05-20",
    "D102_8pair": "canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]"
  },
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "d6065738-e523-4f2c-85cf-56082b146c0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011q1hRicRWvR9r2VpbvK1Dh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12377,
      "cache_read_input_tokens": 59815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12377
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

_source line 59 · 2026-05-20T06:09:30.577Z_

<details><summary>↩ Tool result · `toolu_019DB9uZdmWBcDQj68qhhwvk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"c4_a075_s42_fp32\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:37:54.299Z\", \"updated_at\": \"2026-05-20T06:09:30.290Z\", \"hypothesis\": \"Claim 2 cross-domain validation: canary lead-lag generalizes from WikiText to C4 at α=0.75 regime boundary, expecting PermG_fwd signal comparable to WikiText parent (6/8)\", \"parent\": \"alpha_sweep_a075_s42_fp32\", \"spec\": {\"data_path\": \"data/c4_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"precision\": \"fp32\", \"padding_side_fix\": \"D093 applied\"}, \"server\": \"westd-17855\", \"gpu\": \"cuda:2\", \"pid\": \"151771\", \"log_path\": \"~/runs/distrib_canary_collapse/c4_a075_s42_fp32.log\", \"reproduce\": {\"command\": \"bash -c \\\"export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/c4_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.75 --output_dir results/alpha_sweep/c4_a075_s42_fp32 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch\\\"\", \"finished_at\": \"2026-05-19T18:20:08.048Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:20:11.695721+00:00\"}]}, \"checkpoint_path\": \"results/alpha_sweep/c4_a075_s42_fp32/gen_10/checkpoint\", \"metrics\": {\"PermG_fwd\": \"8/8\", \"PermG_rev\": \"0/8\", \"K_ge_3_3sigma\": \"8/8\", \"K_ge_4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"0/8\", \"naive_xcorr\": \"8/8\", \"diff_xcorr\": \"8/8\", \"TY_granger\": \"N/A (signonly API error on 17855)\", \"drift_token_entropy\": -35.32, \"drift_ece\": 2809.23, \"drift_perplexity\": 2152.6, \"drift_distinct_1\": -12.4, \"drift_distinct_2\": -15.41, \"drift_distinct_3\": -14.59, \"drift_mauve\": -42.26, \"drift_effective_rank\": 110.31, \"gen0_token_entropy\": 3.1094, \"D105_3sigma\": \"true 3sigma (std of full series)\", \"D111_direction\": \"peak_lag < 0 (C009 corrected)\", \"analysis_script\": \"run_5method_analysis_d102.py\", \"n_perm\": 5000, \"D120_recomputed\": \"2026-05-20\", \"D102_8pair\": \"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:26:33.496Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7176}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "ab4577e7-d8aa-475d-a932-068ec570e535",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"c4_a075_s42_fp32\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T14:37:54.299Z\\\", \\\"updated_at\\\": \\\"2026-05-20T06:09:30.290Z\\\", \\\"hypothesis\\\": \\\"Claim 2 cross-domain validation: canary lead-lag generalizes from WikiText to C4 at α=0.75 regime boundary, expecting PermG_fwd signal comparable to WikiText parent (6/8)\\\", \\\"parent\\\": \\\"alpha_sweep_a075_s42_fp32\\\", \\\"spec\\\": {\\\"data_path\\\": \\\"data/c4_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 42, \\\"precision\\\": \\\"fp32\\\", \\\"padding_side_fix\\\": \\\"D093 applied\\\"}, \\\"server\\\": \\\"westd-17855\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": \\\"151771\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/c4_a075_s42_fp32.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/c4_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.75 --output_dir results/alpha_sweep/c4_a075_s42_fp32 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-19T18:20:08.048Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-19T18:20:11.695721+00:00\\\"}]}, \\\"checkpoint_path\\\": \\\"results/alpha_sweep/c4_a075_s42_fp32/gen_10/checkpoint\\\", \\\"metrics\\\": {\\\"PermG_fwd\\\": \\\"8/8\\\", \\\"PermG_rev\\\": \\\"0/8\\\", \\\"K_ge_3_3sigma\\\": \\\"8/8\\\", \\\"K_ge_4_3sigma\\\": \\\"0/8\\\", \\\"threshold_onset_3sigma\\\": \\\"0/8\\\", \\\"naive_xcorr\\\": \\\"8/8\\\", \\\"diff_xcorr\\\": \\\"8/8\\\", \\\"TY_granger\\\": \\\"N/A (signonly API error on 17855)\\\", \\\"drift_token_entropy\\\": -35.32, \\\"drift_ece\\\": 2809.23, \\\"drift_perplexity\\\": 2152.6, \\\"drift_distinct_1\\\": -12.4, \\\"drift_distinct_2\\\": -15.41, \\\"drift_distinct_3\\\": -14.59, \\\"drift_mauve\\\": -42.26, \\\"drift_effective_rank\\\": 110.31, \\\"gen0_token_entropy\\\": 3.1094, \\\"D105_3sigma\\\": \\\"true 3sigma (std of full series)\\\", \\\"D111_direction\\\": \\\"peak_lag < 0 (C009 corrected)\\\", \\\"analysis_script\\\": \\\"run_5method_analysis_d102.py\\\", \\\"n_perm\\\": 5000, \\\"D120_recomputed\\\": \\\"2026-05-20\\\", \\\"D102_8pair\\\": \\\"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T18:26:33.496Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7176}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"c4_a075_s42_fp32\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:37:54.299Z\", \"updated_at\": \"2026-05-20T06:09:30.290Z\", \"hypothesis\": \"Claim 2 cross-domain validation: canary lead-lag generalizes from WikiText to C4 at α=0.75 regime boundary, expecting PermG_fwd signal comparable to WikiText parent (6/8)\", \"parent\": \"alpha_sweep_a075_s42_fp32\", \"spec\": {\"data_path\": \"data/c4_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"precision\": \"fp32\", \"padding_side_fix\": \"D093 applied\"}, \"server\": \"westd-17855\", \"gpu\": \"cuda:2\", \"pid\": \"151771\", \"log_path\": \"~/runs/distrib_canary_collapse/c4_a075_s42_fp32.log\", \"reproduce\": {\"command\": \"bash -c \\\"export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/c4_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.75 --output_dir results/alpha_sweep/c4_a075_s42_fp32 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch\\\"\", \"finished_at\": \"2026-05-19T18:20:08.048Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:20:11.695721+00:00\"}]}, \"checkpoint_path\": \"results/alpha_sweep/c4_a075_s42_fp32/gen_10/checkpoint\", \"metrics\": {\"PermG_fwd\": \"8/8\", \"PermG_rev\": \"0/8\", \"K_ge_3_3sigma\": \"8/8\", \"K_ge_4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"0/8\", \"naive_xcorr\": \"8/8\", \"diff_xcorr\": \"8/8\", \"TY_granger\": \"N/A (signonly API error on 17855)\", \"drift_token_entropy\": -35.32, \"drift_ece\": 2809.23, \"drift_perplexity\": 2152.6, \"drift_distinct_1\": -12.4, \"drift_distinct_2\": -15.41, \"drift_distinct_3\": -14.59, \"drift_mauve\": -42.26, \"drift_effective_rank\": 110.31, \"gen0_token_entropy\": 3.1094, \"D105_3sigma\": \"true 3sigma (std of full series)\", \"D111_direction\": \"peak_lag < 0 (C009 corrected)\", \"analysis_script\": \"run_5method_analysis_d102.py\", \"n_perm\": 5000, \"D120_recomputed\": \"2026-05-20\", \"D102_8pair\": \"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:26:33.496Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7176}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01CEWa5c9KZMfZeC7soEzM8H`</summary>

```json
{
  "exp_id": "padding_robustness_a100_s42_fp32",
  "field": "metrics",
  "value": {
    "PermG_fwd": "6/8",
    "PermG_rev": "0/8",
    "K_ge_3_3sigma": "6/8",
    "K_ge_4_3sigma": "0/8",
    "threshold_onset_3sigma": "0/8",
    "naive_xcorr": "6/8",
    "diff_xcorr": "6/8",
    "TY_granger": "N/A (signonly API error on 17855)",
    "D105_3sigma": "true 3sigma (std of full series)",
    "D111_direction": "peak_lag < 0 (C009 corrected)",
    "analysis_script": "run_5method_analysis_d102.py",
    "n_perm": 5000,
    "D120_recomputed": "2026-05-20",
    "D102_8pair": "canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]",
    "failing_pairs": "token_entropy<mauve (0/5), ece<mauve (0/5)",
    "vs_wiki_baseline": "K3=6/8 matches generalize_pythia410m_wiki_a100_s42 (6/8). Both fail mauve pairs. Padding side has no detectable effect on lead-lag."
  },
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "1bbe52d2-10fb-4298-92b4-c0b88ece2c7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011q1hRicRWvR9r2VpbvK1Dh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12377,
      "cache_read_input_tokens": 59815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12377
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

_source line 61 · 2026-05-20T06:09:34.706Z_

<details><summary>↩ Tool result · `toolu_01CEWa5c9KZMfZeC7soEzM8H`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"padding_robustness_a100_s42_fp32\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:54:17.535Z\", \"updated_at\": \"2026-05-20T06:09:34.410Z\", \"hypothesis\": \"D093 padding_side='left' 修复后重跑 α=1.0 s42 fp32，对比修复前 mvp_v4_rep42 结果，验证 right-padding bug 对 collapse 轨迹和 lead-lag 信号的影响程度。预期：相对趋势不变，绝对数值可能有小幅差异\", \"spec\": {\"command\": \"bash -c \\\"export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --output_dir results/padding_robustness/a100_s42_fp32 --seed 42 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch\\\"\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:2\"], \"pid\": \"122877\", \"log_path\": \"~/runs/distrib_canary_collapse/padding_robustness_a100_s42_fp32.log\", \"submitted_at\": \"2026-05-19T10:04:16.220Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"wall_clock_seconds\": 16952.1, \"gpu_hours\": 4.71}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:17:27.871Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:17:33.010198+00:00\"}]}, \"metrics\": {\"PermG_fwd\": \"6/8\", \"PermG_rev\": \"0/8\", \"K_ge_3_3sigma\": \"6/8\", \"K_ge_4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"0/8\", \"naive_xcorr\": \"6/8\", \"diff_xcorr\": \"6/8\", \"TY_granger\": \"N/A (signonly API error on 17855)\", \"D105_3sigma\": \"true 3sigma (std of full series)\", \"D111_direction\": \"peak_lag < 0 (C009 corrected)\", \"analysis_script\": \"run_5method_analysis_d102.py\", \"n_perm\": 5000, \"D120_recomputed\": \"2026-05-20\", \"D102_8pair\": \"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\", \"failing_pairs\": \"token_entropy<mauve (0/5), ece<mauve (0/5)\", \"vs_wiki_baseline\": \"K3=6/8 matches generalize_pythia410m_wiki_a100_s42 (6/8). Both fail mauve pairs. Padding side has no detectable effect on lead-lag.\"}, \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/padding_robustness/a100_s42_fp32/gen_10\", \"log_path\": \"~/runs/distrib_canary_collapse/padding_robustness_a100_s42_fp32.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T14:46:48.338Z\", \"note\": \"D111 direction-checked: naive 6/8→0/8, diff 6/8→0/8 (ALL lags negative), K≥3 6/8→6/8 (unchanged), K≥4 6/8→0/8. Forward evidence from threshold+permG+TY only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7772}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "fa4140ee-c6d7-4437-9aed-a407a92a3572",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"padding_robustness_a100_s42_fp32\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T09:54:17.535Z\\\", \\\"updated_at\\\": \\\"2026-05-20T06:09:34.410Z\\\", \\\"hypothesis\\\": \\\"D093 padding_side='left' 修复后重跑 α=1.0 s42 fp32，对比修复前 mvp_v4_rep42 结果，验证 right-padding bug 对 collapse 轨迹和 lead-lag 信号的影响程度。预期：相对趋势不变，绝对数值可能有小幅差异\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --output_dir results/padding_robustness/a100_s42_fp32 --seed 42 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch\\\\\\\"\\\", \\\"server\\\": \\\"westd-17855\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"122877\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/padding_robustness_a100_s42_fp32.log\\\", \\\"submitted_at\\\": \\\"2026-05-19T10:04:16.220Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 42, \\\"wall_clock_seconds\\\": 16952.1, \\\"gpu_hours\\\": 4.71}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-19T14:17:27.871Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-19T14:17:33.010198+00:00\\\"}]}, \\\"metrics\\\": {\\\"PermG_fwd\\\": \\\"6/8\\\", \\\"PermG_rev\\\": \\\"0/8\\\", \\\"K_ge_3_3sigma\\\": \\\"6/8\\\", \\\"K_ge_4_3sigma\\\": \\\"0/8\\\", \\\"threshold_onset_3sigma\\\": \\\"0/8\\\", \\\"naive_xcorr\\\": \\\"6/8\\\", \\\"diff_xcorr\\\": \\\"6/8\\\", \\\"TY_granger\\\": \\\"N/A (signonly API error on 17855)\\\", \\\"D105_3sigma\\\": \\\"true 3sigma (std of full series)\\\", \\\"D111_direction\\\": \\\"peak_lag < 0 (C009 corrected)\\\", \\\"analysis_script\\\": \\\"run_5method_analysis_d102.py\\\", \\\"n_perm\\\": 5000, \\\"D120_recomputed\\\": \\\"2026-05-20\\\", \\\"D102_8pair\\\": \\\"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\\\", \\\"failing_pairs\\\": \\\"token_entropy<mauve (0/5), ece<mauve (0/5)\\\", \\\"vs_wiki_baseline\\\": \\\"K3=6/8 matches generalize_pythia410m_wiki_a100_s42 (6/8). Both fail mauve pairs. Padding side has no detectable effect on lead-lag.\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/padding_robustness/a100_s42_fp32/gen_10\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/padding_robustness_a100_s42_fp32.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T14:46:48.338Z\\\", \\\"note\\\": \\\"D111 direction-checked: naive 6/8→0/8, diff 6/8→0/8 (ALL lags negative), K≥3 6/8→6/8 (unchanged), K≥4 6/8→0/8. Forward evidence from threshold+permG+TY only.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7772}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"padding_robustness_a100_s42_fp32\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:54:17.535Z\", \"updated_at\": \"2026-05-20T06:09:34.410Z\", \"hypothesis\": \"D093 padding_side='left' 修复后重跑 α=1.0 s42 fp32，对比修复前 mvp_v4_rep42 结果，验证 right-padding bug 对 collapse 轨迹和 lead-lag 信号的影响程度。预期：相对趋势不变，绝对数值可能有小幅差异\", \"spec\": {\"command\": \"bash -c \\\"export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --output_dir results/padding_robustness/a100_s42_fp32 --seed 42 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch\\\"\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:2\"], \"pid\": \"122877\", \"log_path\": \"~/runs/distrib_canary_collapse/padding_robustness_a100_s42_fp32.log\", \"submitted_at\": \"2026-05-19T10:04:16.220Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"wall_clock_seconds\": 16952.1, \"gpu_hours\": 4.71}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:17:27.871Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:17:33.010198+00:00\"}]}, \"metrics\": {\"PermG_fwd\": \"6/8\", \"PermG_rev\": \"0/8\", \"K_ge_3_3sigma\": \"6/8\", \"K_ge_4_3sigma\": \"0/8\", \"threshold_onset_3sigma\": \"0/8\", \"naive_xcorr\": \"6/8\", \"diff_xcorr\": \"6/8\", \"TY_granger\": \"N/A (signonly API error on 17855)\", \"D105_3sigma\": \"true 3sigma (std of full series)\", \"D111_direction\": \"peak_lag < 0 (C009 corrected)\", \"analysis_script\": \"run_5method_analysis_d102.py\", \"n_perm\": 5000, \"D120_recomputed\": \"2026-05-20\", \"D102_8pair\": \"canary=[token_entropy,ece] x downstream=[d1,d2,d3,mauve]\", \"failing_pairs\": \"token_entropy<mauve (0/5), ece<mauve (0/5)\", \"vs_wiki_baseline\": \"K3=6/8 matches generalize_pythia410m_wiki_a100_s42 (6/8). Both fail mauve pairs. Padding side has no detectable effect on lead-lag.\"}, \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/padding_robustness/a100_s42_fp32/gen_10\", \"log_path\": \"~/runs/distrib_canary_collapse/padding_robustness_a100_s42_fp32.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T14:46:48.338Z\", \"note\": \"D111 direction-checked: naive 6/8→0/8, diff 6/8→0/8 (ALL lags negative), K≥3 6/8→6/8 (unchanged), K≥4 6/8→0/8. Forward evidence from threshold+permG+TY only.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7772}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
All registry updates successful. Now let me write the report and register the artifact.

Let me create the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "3a456526-2005-4e25-aee8-6537a0f64ea3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011L112LAALXUxvD262JV2pz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21927,
      "cache_read_input_tokens": 72192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21927
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

_source line 63_

Registry 更新完成。写报告并注册 artifact。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "8e0e1dd4-3944-4473-9ecb-9d0f4a2f136a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011L112LAALXUxvD262JV2pz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21927,
      "cache_read_input_tokens": 72192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21927
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

_source line 64_

<details open><summary>🔧 Tool call — Bash · `toolu_018ycP6EhATMFghwLULU6dUT`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d120_c4_padding_audit",
  "description": "Create artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "88017729-d0b6-44e4-9575-bfcd8f96a074",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011L112LAALXUxvD262JV2pz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21927,
      "cache_read_input_tokens": 72192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21927
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

_source line 65 · 2026-05-20T06:09:40.779Z_

<details><summary>↩ Tool result · `toolu_018ycP6EhATMFghwLULU6dUT`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "c3599afa-a83f-4082-9ce6-22e707a1e9c6",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Write · `toolu_01HFH91zd1ZfNnjFisTr2fsR`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d120_c4_padding_audit/report.md",
  "content": "# D120 Recomputation: C4 s42 + Padding-410M Audit\n\n**Date**: 2026-05-20\n**Server**: westd-17855\n**Script**: `run_5method_analysis_d102.py` (D105 true 3σ + D111 direction integrated)\n**Parameters**: n_perm=5000, threshold=true_3sigma_d105, direction=peak_lag<0 (C009)\n\n## Summary Table\n\n| Experiment | α | Domain | PermG_fwd | PermG_rev | naive | diff | thresh_3σ | TY | K≥3 | K≥4 |\n|---|---|---|---|---|---|---|---|---|---|---|\n| c4_a025_s42_fp32 | 0.25 | C4 | 0/8 | 0/8 | 4/8 | 8/8 | 2/8 | N/A | 0/8 | 0/8 |\n| c4_a050_s42_fp32 | 0.50 | C4 | 8/8 | **7/8** | 4/8 | 8/8 | 0/8 | N/A | 4/8 | 0/8 |\n| c4_a075_s42_fp32 | 0.75 | C4 | 8/8 | 0/8 | 8/8 | 8/8 | 0/8 | N/A | 8/8 | 0/8 |\n| padding_a100_s42_fp32 | 1.0 | Wiki(pad) | 6/8 | 0/8 | 6/8 | 6/8 | 0/8 | N/A | 6/8 | 0/8 |\n\n## C4 Cross-Domain Dose-Response (D120)\n\nC4 α dose-response under D120 true 3σ:\n- **α=0.25**: PermG=0/8, K3=0/8. Below detection threshold. Consistent with wiki domain.\n- **α=0.50**: PermG=8/8, K3=4/8. Transition zone. **Notable: PermG_rev=7/8 (bidirectional)**. This is unique to C4 cross-domain — wiki α=0.50 typically shows 0/8 reverse. Indicates stronger mutual feedback in cross-domain contamination.\n- **α=0.75**: PermG=8/8, K3=8/8. Full detection. Strong unidirectional asymmetry (rev=0/8).\n\n### Comparison with s43 (same script, prior D120 batch)\n\n| α | s42 PermG | s43 PermG | s42 K≥3 | s43 K≥3 |\n|---|---|---|---|---|\n| 0.50 | 8/8 | 8/8 | 4/8 | 3/8 |\n| 0.75 | 8/8 | 8/8 | 8/8 | 8/8 |\n\nCross-seed consistent for PermG. K≥3 minor variation at α=0.50 (4 vs 3) from naive_xcorr variability.\n\n## Padding-410M Audit (Table 7)\n\n### D120 Results\n- **PermG_fwd**: 6/8 (FDR-corrected, per-direction)\n- **PermG_rev**: 0/8 → strong directional asymmetry\n- **K≥3**: 6/8\n- **Failing pairs**: token_entropy→mauve (0/5), ece→mauve (0/5)\n  - mauve NaiveR = -0.436 (weak, wrong sign), DiffR peak_lag=-4/-5 (too deep)\n\n### Comparison with Wiki Baseline\n\n| Metric | padding_a100_s42 | wiki_a100_s42 (registry) |\n|---|---|---|\n| K≥3 | 6/8 | 6/8 |\n| PermG_fwd | 6/8 | 6/8 |\n| Failing pairs | mauve | mauve (inferred) |\n\n**Conclusion**: Padding side (D093 right→left fix) has **no detectable effect** on lead-lag signal. K3=6/8 matches wiki baseline exactly. The 2 failing pairs are both mauve, consistent across padding variants.\n\n## TY Granger API Error\n\nAll 4 experiments hit `VARResults.test_causality() got an unexpected keyword argument 'signonly'` on westd-17855. This is a statsmodels version incompatibility specific to this server.\n\n**Impact**: TY returns N/A → max consensus = 3/5 (naive+diff+perm) → K≥4 capped at 0/8 for all D120 runs on this server. Previous analyses on other servers had working TY (e.g., c4_a075_s43 TY=1/8).\n\n**Mitigation**: K≥3 (the primary paper metric) is unaffected. K≥4 comparisons across servers require TY fix or exclusion from vote denominator.\n\n## Changes from Pre-D120 Registry\n\n| Exp | Field | Old | D120 | Reason |\n|---|---|---|---|---|\n| c4_a025 | threshold_onset | 8/8 | 2/8 | D105 true 3σ (std of full series) |\n| c4_a025 | diff_xcorr | 0/8 | 8/8 | C009 sign fix (peak_lag>0 → peak_lag<0) |\n| c4_a050 | PermG_rev | 0/8 | 7/8 | D120 integrated analysis detects bidirectional |\n| c4_a050 | K3 | 6/8 | 4/8 | C009 fix adjusts naive direction counts |\n| c4_a075 | naive_xcorr | 0/8 | 8/8 | C009 sign fix recovers naive |\n| c4_a075 | diff_xcorr | 0/8 | 8/8 | C009 sign fix recovers diff |\n| c4_a075 | K3 | 6/8 | 8/8 | C009 recovery of naive+diff |\n| padding | K4 | 6/8 | 0/8 | TY broken on 17855 (was 4th method) |\n\n## Per-Experiment Detail\n\n### c4_a025_s42_fp32 (α=0.25)\n\nForward consensus per pair:\n```\ntoken_entropy<distinct_1  2/5  [naive, diff]\ntoken_entropy<distinct_2  1/5  [diff]\ntoken_entropy<distinct_3  2/5  [diff, threshold]\ntoken_entropy<mauve       2/5  [naive, diff]\nece<distinct_1            2/5  [naive, diff]\nece<distinct_2            1/5  [diff]\nece<distinct_3            2/5  [diff, threshold]\nece<mauve                 2/5  [naive, diff]\n```\n\ndiff_xcorr bidirectional (fwd=8/8, rev=8/8) — no directional selectivity, consistent with α below onset. PermG 0/8 correctly identifies no signal.\n\n### c4_a050_s42_fp32 (α=0.50)\n\nForward consensus per pair:\n```\ntoken_entropy<distinct_1  3/5  [naive, diff, perm]\ntoken_entropy<distinct_2  2/5  [diff, perm]\ntoken_entropy<distinct_3  3/5  [naive, diff, perm]\ntoken_entropy<mauve       3/5  [naive, diff, perm]\nece<distinct_1            3/5  [naive, diff, perm]\nece<distinct_2            2/5  [diff, perm]\nece<distinct_3            2/5  [diff, perm]\nece<mauve                 2/5  [diff, perm]\n```\n\nPermG bidirectional note: 8/8 forward + 7/8 reverse. The only non-significant reverse pair is mauve→token_entropy (PermFDR not sig). This bidirectionality may reflect C4's domain diversity creating stronger feedback loops at moderate α.\n\n### c4_a075_s42_fp32 (α=0.75)\n\nAll 8 pairs: 3/5 [naive, diff, perm]. Perfect PermG asymmetry (8/8 fwd, 0/8 rev). PermG F-stats range 239-1390 (forward) vs 0.02-0.70 (reverse). Cleanest directional separation in the C4 sweep.\n\n### padding_robustness_a100_s42_fp32 (α=1.0)\n\n```\ntoken_entropy<distinct_1  3/5  [naive, diff, perm]\ntoken_entropy<distinct_2  3/5  [naive, diff, perm]\ntoken_entropy<distinct_3  3/5  [naive, diff, perm]\ntoken_entropy<mauve       0/5  [none]\nece<distinct_1            3/5  [naive, diff, perm]\nece<distinct_2            3/5  [naive, diff, perm]\nece<distinct_3            3/5  [naive, diff, perm]\nece<mauve                 0/5  [none]\n```\n\nMauve failure: NaiveR=-0.436 (weak negative), DiffR at lag=-4/-5 (too deep to be meaningful), PermG F<1 (no Granger signal). Mauve is measuring text quality at a coarser level that doesn't track the generation-by-generation canary signal.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "2b236d51-7596-4ba9-a311-55d5c697c969",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KWnFL2pzu6aFKZ7tWDvMQR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 187,
      "cache_read_input_tokens": 94119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 187
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

_source line 67 · 2026-05-20T06:10:31.478Z_

<details><summary>↩ Tool result · `toolu_01HFH91zd1ZfNnjFisTr2fsR`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d120_c4_padding_audit/report.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "85ea95ae-68de-4394-a9d1-36beda5d169f",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d120_c4_padding_audit/report.md",
    "content": "# D120 Recomputation: C4 s42 + Padding-410M Audit\n\n**Date**: 2026-05-20\n**Server**: westd-17855\n**Script**: `run_5method_analysis_d102.py` (D105 true 3σ + D111 direction integrated)\n**Parameters**: n_perm=5000, threshold=true_3sigma_d105, direction=peak_lag<0 (C009)\n\n## Summary Table\n\n| Experiment | α | Domain | PermG_fwd | PermG_rev | naive | diff | thresh_3σ | TY | K≥3 | K≥4 |\n|---|---|---|---|---|---|---|---|---|---|---|\n| c4_a025_s42_fp32 | 0.25 | C4 | 0/8 | 0/8 | 4/8 | 8/8 | 2/8 | N/A | 0/8 | 0/8 |\n| c4_a050_s42_fp32 | 0.50 | C4 | 8/8 | **7/8** | 4/8 | 8/8 | 0/8 | N/A | 4/8 | 0/8 |\n| c4_a075_s42_fp32 | 0.75 | C4 | 8/8 | 0/8 | 8/8 | 8/8 | 0/8 | N/A | 8/8 | 0/8 |\n| padding_a100_s42_fp32 | 1.0 | Wiki(pad) | 6/8 | 0/8 | 6/8 | 6/8 | 0/8 | N/A | 6/8 | 0/8 |\n\n## C4 Cross-Domain Dose-Response (D120)\n\nC4 α dose-response under D120 true 3σ:\n- **α=0.25**: PermG=0/8, K3=0/8. Below detection threshold. Consistent with wiki domain.\n- **α=0.50**: PermG=8/8, K3=4/8. Transition zone. **Notable: PermG_rev=7/8 (bidirectional)**. This is unique to C4 cross-domain — wiki α=0.50 typically shows 0/8 reverse. Indicates stronger mutual feedback in cross-domain contamination.\n- **α=0.75**: PermG=8/8, K3=8/8. Full detection. Strong unidirectional asymmetry (rev=0/8).\n\n### Comparison with s43 (same script, prior D120 batch)\n\n| α | s42 PermG | s43 PermG | s42 K≥3 | s43 K≥3 |\n|---|---|---|---|---|\n| 0.50 | 8/8 | 8/8 | 4/8 | 3/8 |\n| 0.75 | 8/8 | 8/8 | 8/8 | 8/8 |\n\nCross-seed consistent for PermG. K≥3 minor variation at α=0.50 (4 vs 3) from naive_xcorr variability.\n\n## Padding-410M Audit (Table 7)\n\n### D120 Results\n- **PermG_fwd**: 6/8 (FDR-corrected, per-direction)\n- **PermG_rev**: 0/8 → strong directional asymmetry\n- **K≥3**: 6/8\n- **Failing pairs**: token_entropy→mauve (0/5), ece→mauve (0/5)\n  - mauve NaiveR = -0.436 (weak, wrong sign), DiffR peak_lag=-4/-5 (too deep)\n\n### Comparison with Wiki Baseline\n\n| Metric | padding_a100_s42 | wiki_a100_s42 (registry) |\n|---|---|---|\n| K≥3 | 6/8 | 6/8 |\n| PermG_fwd | 6/8 | 6/8 |\n| Failing pairs | mauve | mauve (inferred) |\n\n**Conclusion**: Padding side (D093 right→left fix) has **no detectable effect** on lead-lag signal. K3=6/8 matches wiki baseline exactly. The 2 failing pairs are both mauve, consistent across padding variants.\n\n## TY Granger API Error\n\nAll 4 experiments hit `VARResults.test_causality() got an unexpected keyword argument 'signonly'` on westd-17855. This is a statsmodels version incompatibility specific to this server.\n\n**Impact**: TY returns N/A → max consensus = 3/5 (naive+diff+perm) → K≥4 capped at 0/8 for all D120 runs on this server. Previous analyses on other servers had working TY (e.g., c4_a075_s43 TY=1/8).\n\n**Mitigation**: K≥3 (the primary paper metric) is unaffected. K≥4 comparisons across servers require TY fix or exclusion from vote denominator.\n\n## Changes from Pre-D120 Registry\n\n| Exp | Field | Old | D120 | Reason |\n|---|---|---|---|---|\n| c4_a025 | threshold_onset | 8/8 | 2/8 | D105 true 3σ (std of full series) |\n| c4_a025 | diff_xcorr | 0/8 | 8/8 | C009 sign fix (peak_lag>0 → peak_lag<0) |\n| c4_a050 | PermG_rev | 0/8 | 7/8 | D120 integrated analysis detects bidirectional |\n| c4_a050 | K3 | 6/8 | 4/8 | C009 fix adjusts naive direction counts |\n| c4_a075 | naive_xcorr | 0/8 | 8/8 | C009 sign fix recovers naive |\n| c4_a075 | diff_xcorr | 0/8 | 8/8 | C009 sign fix recovers diff |\n| c4_a075 | K3 | 6/8 | 8/8 | C009 recovery of naive+diff |\n| padding | K4 | 6/8 | 0/8 | TY broken on 17855 (was 4th method) |\n\n## Per-Experiment Detail\n\n### c4_a025_s42_fp32 (α=0.25)\n\nForward consensus per pair:\n```\ntoken_entropy<distinct_1  2/5  [naive, diff]\ntoken_entropy<distinct_2  1/5  [diff]\ntoken_entropy<distinct_3  2/5  [diff, threshold]\ntoken_entropy<mauve       2/5  [naive, diff]\nece<distinct_1            2/5  [naive, diff]\nece<distinct_2            1/5  [diff]\nece<distinct_3            2/5  [diff, threshold]\nece<mauve                 2/5  [naive, diff]\n```\n\ndiff_xcorr bidirectional (fwd=8/8, rev=8/8) — no directional selectivity, consistent with α below onset. PermG 0/8 correctly identifies no signal.\n\n### c4_a050_s42_fp32 (α=0.50)\n\nForward consensus per pair:\n```\ntoken_entropy<distinct_1  3/5  [naive, diff, perm]\ntoken_entropy<distinct_2  2/5  [diff, perm]\ntoken_entropy<distinct_3  3/5  [naive, diff, perm]\ntoken_entropy<mauve       3/5  [naive, diff, perm]\nece<distinct_1            3/5  [naive, diff, perm]\nece<distinct_2            2/5  [diff, perm]\nece<distinct_3            2/5  [diff, perm]\nece<mauve                 2/5  [diff, perm]\n```\n\nPermG bidirectional note: 8/8 forward + 7/8 reverse. The only non-significant reverse pair is mauve→token_entropy (PermFDR not sig). This bidirectionality may reflect C4's domain diversity creating stronger feedback loops at moderate α.\n\n### c4_a075_s42_fp32 (α=0.75)\n\nAll 8 pairs: 3/5 [naive, diff, perm]. Perfect PermG asymmetry (8/8 fwd, 0/8 rev). PermG F-stats range 239-1390 (forward) vs 0.02-0.70 (reverse). Cleanest directional separation in the C4 sweep.\n\n### padding_robustness_a100_s42_fp32 (α=1.0)\n\n```\ntoken_entropy<distinct_1  3/5  [naive, diff, perm]\ntoken_entropy<distinct_2  3/5  [naive, diff, perm]\ntoken_entropy<distinct_3  3/5  [naive, diff, perm]\ntoken_entropy<mauve       0/5  [none]\nece<distinct_1            3/5  [naive, diff, perm]\nece<distinct_2            3/5  [naive, diff, perm]\nece<distinct_3            3/5  [naive, diff, perm]\nece<mauve                 0/5  [none]\n```\n\nMauve failure: NaiveR=-0.436 (weak negative), DiffR at lag=-4/-5 (too deep to be meaningful), PermG F<1 (no Granger signal). Mauve is measuring text quality at a coarser level that doesn't track the generation-by-generation canary signal.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_011DKqsxSLAor8Qb8k66XbBs`</summary>

```json
{
  "name": "D120 C4 s42 + Padding-410M Audit Report",
  "type": "report",
  "description": "D120 recomputation (true 3σ + C009 direction fix) for 3 C4 cross-domain s42 experiments (α=0.25/0.50/0.75) and padding_robustness_a100_s42 audit. Key findings: C4 dose-response confirmed (K3: 0→4→8), α=0.50 C4 shows bidirectional PermG (7/8 rev), padding K3=6/8 matches wiki baseline.",
  "project": "distrib_canary_collapse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d120_c4_padding_audit/report.md",
  "tags": [
    "D120",
    "C4",
    "padding",
    "audit",
    "table7"
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
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "cc5d6a51-4672-42af-b85d-e59dbb9eeb37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197tdPxFsdKbzTVwfr3TEJc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2751,
      "cache_read_input_tokens": 94306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2751
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 69 · 2026-05-20T06:10:40.879Z_

<details><summary>↩ Tool result · `toolu_011DKqsxSLAor8Qb8k66XbBs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_f699f2\", \"name\": \"D120 C4 s42 + Padding-410M Audit Report\", \"type\": \"report\", \"description\": \"D120 recomputation (true 3σ + C009 direction fix) for 3 C4 cross-domain s42 experiments (α=0.25/0.50/0.75) and padding_robustness_a100_s42 audit. Key findings: C4 dose-response confirmed (K3: 0→4→8), α=0.50 C4 shows bidirectional PermG (7/8 rev), padding K3=6/8 matches wiki baseline.\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/report/report_f699f2.md\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T06:10:40.529722+00:00\", \"tags\": [\"D120\", \"C4\", \"padding\", \"audit\", \"table7\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "24015aa7-ab76-4ed0-8f95-9eb3e10709e8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260520_f699f2\\\", \\\"name\\\": \\\"D120 C4 s42 + Padding-410M Audit Report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"D120 recomputation (true 3σ + C009 direction fix) for 3 C4 cross-domain s42 experiments (α=0.25/0.50/0.75) and padding_robustness_a100_s42 audit. Key findings: C4 dose-response confirmed (K3: 0→4→8), α=0.50 C4 shows bidirectional PermG (7/8 rev), padding K3=6/8 matches wiki baseline.\\\", \\\"path\\\": \\\"projects/distrib_canary_collapse/artifacts/_project/report/report_f699f2.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"distrib_canary_collapse\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-20T06:10:40.529722+00:00\\\", \\\"tags\\\": [\\\"D120\\\", \\\"C4\\\", \\\"padding\\\", \\\"audit\\\", \\\"table7\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_f699f2\", \"name\": \"D120 C4 s42 + Padding-410M Audit Report\", \"type\": \"report\", \"description\": \"D120 recomputation (true 3σ + C009 direction fix) for 3 C4 cross-domain s42 experiments (α=0.25/0.50/0.75) and padding_robustness_a100_s42 audit. Key findings: C4 dose-response confirmed (K3: 0→4→8), α=0.50 C4 shows bidirectional PermG (7/8 rev), padding K3=6/8 matches wiki baseline.\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/report/report_f699f2.md\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T06:10:40.529722+00:00\", \"tags\": [\"D120\", \"C4\", \"padding\", \"audit\", \"table7\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 70_

完成。4 个实验全部 D120 重算，registry 已更新，报告已注册。

### 结果摘要

| Experiment | α | PermG_fwd | PermG_rev | K≥3 | K≥4 |
|---|---|---|---|---|---|
| c4_a025_s42 | 0.25 | 0/8 | 0/8 | 0/8 | 0/8 |
| c4_a050_s42 | 0.50 | 8/8 | **7/8** | 4/8 | 0/8 |
| c4_a075_s42 | 0.75 | 8/8 | 0/8 | 8/8 | 0/8 |
| padding_a100_s42 | 1.0 | 6/8 | 0/8 | 6/8 | 0/8 |

### 关键发现

1. **C4 dose-response 确认**: K3 从 0→4→8 随 α 递增，与 wiki domain 一致
2. **C4 α=0.50 双向 PermG**: rev=7/8，wiki 域从未出现。可能反映 C4 跨域环境下更强的双向反馈
3. **Padding 审计通过**: K3=6/8 与 wiki baseline (`generalize_pythia410m_wiki_a100_s42`) 完全一致。Padding side 对 lead-lag 无影响。2 个失败 pair 均为 mauve
4. **TY Granger 在 17855 上不可用**: `signonly` API error，导致所有 K≥4=0/8。K≥3 不受影响

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "uuid": "1a0009d0-7217-4a2b-948c-3da2f2e2e912",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVfdjj8rRffktenS9ffSD6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 97057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 734
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

_source line 71_

完成。4 个实验全部 D120 重算，registry 已更新，报告已注册。

### 结果摘要

| Experiment | α | PermG_fwd | PermG_rev | K≥3 | K≥4 |
|---|---|---|---|---|---|
| c4_a025_s42 | 0.25 | 0/8 | 0/8 | 0/8 | 0/8 |
| c4_a050_s42 | 0.50 | 8/8 | **7/8** | 4/8 | 0/8 |
| c4_a075_s42 | 0.75 | 8/8 | 0/8 | 8/8 | 0/8 |
| padding_a100_s42 | 1.0 | 6/8 | 0/8 | 6/8 | 0/8 |

### 关键发现

1. **C4 dose-response 确认**: K3 从 0→4→8 随 α 递增，与 wiki domain 一致
2. **C4 α=0.50 双向 PermG**: rev=7/8，wiki 域从未出现。可能反映 C4 跨域环境下更强的双向反馈
3. **Padding 审计通过**: K3=6/8 与 wiki baseline (`generalize_pythia410m_wiki_a100_s42`) 完全一致。Padding side 对 lead-lag 无影响。2 个失败 pair 均为 mauve
4. **TY Granger 在 17855 上不可用**: `signonly` API error，导致所有 K≥4=0/8。K≥3 不受影响

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 513871,
  "duration_api_ms": 471348,
  "num_turns": 26,
  "stop_reason": "end_turn",
  "session_id": "81f33179-b27d-4b91-b742-61130609ff1c",
  "total_cost_usd": 1.5005959999999996,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 85950,
    "cache_read_input_tokens": 611425,
    "output_tokens": 26190,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 85950,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 472,
        "cache_read_input_tokens": 97057,
        "cache_creation_input_tokens": 734,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 734
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2751,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002866,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 26190,
      "cacheReadInputTokens": 611425,
      "cacheCreationInputTokens": 85950,
      "webSearchRequests": 0,
      "costUSD": 1.49773,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0bae646d-f415-47aa-9e63-c74bd06263c8"
}
```

</details>

---
