# ops exp 029a completion

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_ops_exp_029a_completion_20260520T164804.log`
- **Structured JSON:** [`8bd5758778dc599be547.json`](../../sessions/8b/8bd5758778dc599be547.json)

## Before a recorded user message

39 recorded events

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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "b739dff9-adf4-44dd-9c67-46408ad244f1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779311400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d97b085b-e9f5-4af4-9f66-4d5f43551228",
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me execute the tasks step by step. First, I need to confirm the exit status and find logs/checkpoints on the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "a90124a1-5fd1-4397-b2a4-be6ed47dfc78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZJ3si9yCd5xjQocTs64JT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11828,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11828
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

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JEsS4bM4J4JgxBiM289uCA`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,CronDelete",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "0fd0fdf3-3d4e-45c5-a956-dda71714bf1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZJ3si9yCd5xjQocTs64JT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11828,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11828
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

_source line 6 · 2026-05-20T16:48:18.726Z_

<details><summary>↩ Tool result · `toolu_01JEsS4bM4J4JgxBiM289uCA`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "CronDelete"
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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "f45fab16-e418-4771-ab2f-31961cfc2f7d",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__read_registry",
      "CronDelete"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,CronDelete",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me execute the steps. First, confirm exit status and find logs/checkpoints in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "f3c8aa15-9555-488b-9a11-46925b3324c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhdY5KRsobKQvvhjWJyiX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 23275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1668
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CWZxyEvjGn1rL7EJjo72JY`</summary>

```json
{
  "server": "bjb1-40020",
  "command": "ps -p 50924 -o pid= 2>/dev/null && echo RUNNING || echo EXITED",
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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "5dfcb01e-f440-4e18-883d-11b81b1a4966",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhdY5KRsobKQvvhjWJyiX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 23275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1668
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

_source line 9 · 2026-05-20T16:48:23.634Z_

<details><summary>↩ Tool result · `toolu_01CWZxyEvjGn1rL7EJjo72JY`</summary>

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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "815047f8-be9a-49e3-848e-9d913fe37f35",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014KGTKzhoKbmzGCoQX32WPs`</summary>

```json
{
  "server": "bjb1-40020",
  "command": "find /root/runs/event-gated-adaptive-horizon/ -name \"*.log\" 2>/dev/null",
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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "d064dcab-e18f-4618-8a47-d84ca28ad251",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhdY5KRsobKQvvhjWJyiX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 23275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1668
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

_source line 11 · 2026-05-20T16:48:24.449Z_

<details><summary>↩ Tool result · `toolu_014KGTKzhoKbmzGCoQX32WPs`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "c67dc7cb-1b95-4f32-93c2-bdfa7ec5cb18",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017DXHuu2ZWzG3AoicZ8aK56`</summary>

```json
{
  "server": "bjb1-40020",
  "command": "find /root/runs/ /root/autodl-tmp/ -path \"*029a*\" -name \"latest.pt\" 2>/dev/null",
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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "4e1f18dc-83ec-4fee-9545-26d1381a6acf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhdY5KRsobKQvvhjWJyiX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 23275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1668
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

_source line 13 · 2026-05-20T16:48:25.399Z_

<details><summary>↩ Tool result · `toolu_017DXHuu2ZWzG3AoicZ8aK56`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "0d1aecf0-a056-4ece-86c2-528f41ebbf0b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01GTyTiMq51mPQC8UJxULsxY`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "filters": {
    "exp_id": "exp_029a"
  },
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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "95244ac4-7d3e-499c-b191-f105d6b50690",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhdY5KRsobKQvvhjWJyiX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 23275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1668
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

_source line 15 · 2026-05-20T16:48:26.094Z_

<details><summary>↩ Tool result · `toolu_01GTyTiMq51mPQC8UJxULsxY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4537}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "4c9cb7e2-2c8c-4e77-8084-1e0b6109805b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4537}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4537}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
The ssh_read_only tool blocks shell metacharacters like `&&`, `>`, and `|`. I need to use simpler commands. Also the registry filter by exp_id didn't work - let me try without filter or with a different approach.

Let me retry with proper commands.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "bfc80c74-d52f-45d6-95da-d4625e2c8573",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7XtWWcZo8DUATnCbzf52z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 24943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

_source line 17_

`ssh_read_only` 不允许 `&&` 和 `>`，需要拆分命令。同时 registry 里没找到 exp_029a，让我换方式查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "e02b84fd-7d70-4a43-86f1-6cddf1a2b93b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7XtWWcZo8DUATnCbzf52z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 24943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FScNsyhcn5KMN64R51Wp8t`</summary>

```json
{
  "server": "bjb1-40020",
  "command": "ps -p 50924 -o pid=",
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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "8d44a223-812d-4357-96e2-fa6effbabc67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7XtWWcZo8DUATnCbzf52z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 24943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KyATadUTHG3PXQ9j9SjjhH`</summary>

```json
{
  "server": "bjb1-40020",
  "command": "find /root/runs/ -name \"*.log\"",
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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "2d3e66b8-d787-4e6c-8d77-790c640fe2fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7XtWWcZo8DUATnCbzf52z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 24943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

_source line 20 · 2026-05-20T16:48:33.668Z_

<details><summary>↩ Tool result · `toolu_01FScNsyhcn5KMN64R51Wp8t`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.04}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "c433ee5e-b482-4046-8b28-74b881373837",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.04}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.04}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T16:48:34.118Z_

<details><summary>↩ Tool result · `toolu_01KyATadUTHG3PXQ9j9SjjhH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\\n/root/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\\n/root/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "1db90cc2-dc13-4e5f-8a01-46dbb6be9b77",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\\\\n/root/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\\\\n/root/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\\n/root/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\\n/root/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018Zg19uoQN6qUbeKwgBPU3u`</summary>

```json
{
  "server": "bjb1-40020",
  "command": "find /root/runs/ -name \"latest.pt\"",
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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "ccc57935-0e71-4ddc-8806-431495d1bf50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7XtWWcZo8DUATnCbzf52z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 24943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

_source line 23 · 2026-05-20T16:48:34.929Z_

<details><summary>↩ Tool result · `toolu_018Zg19uoQN6qUbeKwgBPU3u`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\\n/root/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/latest.pt\\n/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "eaeebfbf-e2dc-4e6c-9cde-fc90c399a0d8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\\\\n/root/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/latest.pt\\\\n/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\\n/root/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/latest.pt\\n/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01ME9do7Lz3aTB6fbXwzgVh4`</summary>

```json
{
  "server": "bjb1-40020",
  "command": "find /root/autodl-tmp/ -name \"latest.pt\"",
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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "d4a28a13-88a0-4496-b9fd-fa43dc616057",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7XtWWcZo8DUATnCbzf52z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 24943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

_source line 25 · 2026-05-20T16:48:35.425Z_

<details><summary>↩ Tool result · `toolu_01ME9do7Lz3aTB6fbXwzgVh4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_025_obs_sgs_walker_s1/latest.pt\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_025_obs_sgs_walker_s2/latest.pt\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_026_obs_sgs_cheetah_s0/latest.pt\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_026_obs_sgs_cheetah_s1/latest.pt\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "88c8ec58-b298-42bc-8d25-3ddfbc81fc50",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_025_obs_sgs_walker_s1/latest.pt\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_025_obs_sgs_walker_s2/latest.pt\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_026_obs_sgs_cheetah_s0/latest.pt\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_026_obs_sgs_cheetah_s1/latest.pt\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_025_obs_sgs_walker_s1/latest.pt\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_025_obs_sgs_walker_s2/latest.pt\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_026_obs_sgs_cheetah_s0/latest.pt\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_026_obs_sgs_cheetah_s1/latest.pt\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01X4aTdorKgzqSxCGJwhq9nh`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "limit": 20,
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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "23577758-3e3e-41dd-965c-a22126249857",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7XtWWcZo8DUATnCbzf52z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 24943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

_source line 27 · 2026-05-20T16:48:36.104Z_

<details><summary>↩ Tool result · `toolu_01X4aTdorKgzqSxCGJwhq9nh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_029a_tcn_walker_s1_sigma02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:31:29.514Z\", \"updated_at\": \"2026-05-20T16:47:55.888Z\", \"hypothesis\": \"TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02 which shows NVE<1.0× and eval reaching baseline at 135K. Tests whether CIVO suppression is reproducible across seeds. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.2. If s1 also shows NVE<1.0× → TCN σ=0.2 is a robust intervention.\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"spec\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"pid\": \"50924\", \"seed\": 1, \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\", \"model_name\": \"dreamerv3\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/metrics.jsonl\"}, \"metrics\": {\"eval_return_5K\": 36.7, \"eval_return_15K\": 137.7, \"eval_return_25K\": 180.9, \"eval_return_35K\": 124, \"eval_return_45K\": 124.2, \"eval_return_55K\": 133.9, \"eval_return_65K\": 169.7, \"eval_return_75K\": 171.2, \"eval_return_85K\": 151.8, \"eval_return_95K\": 180.3, \"eval_return_105K\": 319.4, \"eval_return_115K\": 345.5, \"eval_return_125K\": 401, \"eval_return_135K\": 307.8, \"eval_return_145K\": 380.8, \"eval_return_155K\": 307.3, \"eval_return_165K\": 320.3, \"eval_return_175K\": 159, \"eval_return_185K\": 278.2, \"eval_return_195K\": 301.2, \"eval_return_205K\": 204.6, \"eval_return_215K\": 161.3, \"ve_ratio_15K\": 0.0248, \"ve_ratio_25K\": 0.1165, \"ve_ratio_35K\": 0.3574, \"ve_ratio_45K\": 0.5147, \"ve_ratio_55K\": 0.6428, \"ve_ratio_65K\": 0.4777, \"ve_ratio_75K\": 0.398, \"ve_ratio_85K\": 0.4033, \"ve_ratio_95K\": 0.3007, \"ve_ratio_105K\": 0.1554, \"ve_ratio_115K\": 0.1348, \"ve_ratio_125K\": 0.116, \"ve_ratio_135K\": 0.1449, \"ve_ratio_145K\": 0.1088, \"ve_ratio_155K\": 0.1287, \"ve_ratio_165K\": 0.1142, \"ve_ratio_175K\": 0.2138, \"ve_ratio_185K\": 0.121, \"ve_ratio_195K\": 0.1075, \"ve_ratio_205K\": 0.1503, \"ve_ratio_215K\": 0.1864, \"eval_peak\": 401, \"eval_peak_step\": \"125K\", \"nve_max\": 0.6428, \"nve_max_step\": \"55K\", \"nve_final\": 0.1864, \"current_step\": 215000, \"target_steps\": 210000, \"eval_last10_mean\": 282.15}, \"reproduce\": {\"finished_at\": \"2026-05-20T16:47:17.713Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:47:18.789Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T16:47:29.902718+00:00\"}]}}, \"exp_030c_tcn_cheetah_s0_sigma10\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:26:11.800Z\", \"updated_at\": \"2026-05-20T16:26:18.487Z\", \"hypothesis\": \"Cheetah CIVO intensity (NVE 8-108×) requires proportionally higher TCN noise; σ=1.0 may match Cheetah's CIVO severity as σ=0.2 matched Walker's. Based on exp_030a (σ=0.2 negative, NVE=1.903) and exp_030b (σ=0.5 negative, NVE=10.67).\", \"parent\": \"exp_030b_tcn_cheetah_s0_sigma05\"}, \"exp_031_tcn_pickcube_s0_sigma02\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:09:56.923Z\", \"updated_at\": \"2026-05-20T16:20:39.337Z\", \"hypothesis\": \"TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination rollout will suppress CIVO in ManiSkill PickCube-v1, as it did in Walker Walk, by preventing the world model from overfitting to fixed dt signals.\", \"parent\": \"exp_019b_pickcube_civo_trigger\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\"\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"pid\": \"908459\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\", \"submitted_at\": \"2026-05-20T12:42:41.707Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"maniskill_PickCube-v1\", \"data_count\": \"200000(online)\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"checkpoint_source\": \"none(train_from_scratch)\", \"eval_data\": \"maniskill_PickCube-v1(online_eval)\"}, \"metrics\": {\"eval_return_2.5K\": 2.4, \"eval_return_12.5K\": 19.2, \"eval_return_22.5K\": 17.7, \"eval_return_32.5K\": 11.5, \"eval_return_42.5K\": 7.8, \"eval_return_52.5K\": 4.8, \"eval_return_62.5K\": 10.4, \"ve_ratio_12.5K\": 0.1989, \"ve_ratio_22.5K\": 1.0128, \"ve_ratio_32.5K\": 2.2946, \"ve_ratio_42.5K\": 3.0555, \"ve_ratio_52.5K\": 3.7109, \"ve_ratio_62.5K\": 1.1999, \"nve_max\": 3.7109, \"nve_max_step\": \"52.5K\", \"current_step\": 62500, \"target_steps\": 200000}}, \"exp_030b_tcn_cheetah_s0_sigma05\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:07:53.975Z\", \"updated_at\": \"2026-05-20T16:20:36.095Z\", \"hypothesis\": \"Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the environment-appropriate dose (Walker σ=0.5 = overdose causing oscillatory CIVO, Cheetah σ=0.2 = underdose with NVE 1.903@55K). Tests whether TCN effectiveness is environment-dependent with σ scaling to CIVO severity. If NVE<1.5× and eval maintained → TCN is generalizable with environment-tuned σ.\", \"parent\": \"\", \"spec\": {\"gpu\": \"cuda:0\"}, \"metrics\": {\"eval_return_5K\": 8.3, \"eval_return_15K\": 78.3, \"eval_return_25K\": 219.3, \"eval_return_35K\": 296.5, \"eval_return_45K\": 32.8, \"eval_return_55K\": 6, \"eval_return_65K\": 71.2, \"eval_return_75K\": 23.3, \"eval_return_85K\": 34, \"eval_return_95K\": 143.6, \"eval_return_105K\": 104.4, \"eval_return_115K\": 137.7, \"eval_return_125K\": 211.7, \"eval_return_135K\": 97.2, \"eval_return_145K\": 79.4, \"eval_return_155K\": 76.8, \"eval_return_165K\": 77.5, \"eval_return_175K\": 85.7, \"eval_return_185K\": 68.7, \"eval_return_195K\": 77.6, \"ve_ratio_15K\": 0.0202, \"ve_ratio_25K\": 0.0636, \"ve_ratio_35K\": 0.1238, \"ve_ratio_45K\": 1.9141, \"ve_ratio_55K\": 10.6657, \"ve_ratio_65K\": 0.8371, \"ve_ratio_75K\": 1.9823, \"ve_ratio_85K\": 1.0946, \"ve_ratio_95K\": 0.2253, \"ve_ratio_105K\": 0.2686, \"ve_ratio_115K\": 0.1789, \"ve_ratio_125K\": 0.1037, \"ve_ratio_135K\": 0.2153, \"ve_ratio_145K\": 0.2478, \"ve_ratio_155K\": 0.2392, \"ve_ratio_165K\": 0.202, \"ve_ratio_175K\": 0.1591, \"ve_ratio_185K\": 0.1834, \"ve_ratio_195K\": 0.1534, \"nve_max\": 10.6657, \"nve_max_step\": \"55K\", \"nve_final\": 0.1534, \"current_step\": 195000, \"target_steps\": 210000}}, \"exp_029c_tcn_walker_s0_sigma01\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:09:50.913Z\", \"updated_at\": \"2026-05-20T16:20:28.451Z\", \"hypothesis\": \"σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2 prevents CIVO and σ=0.1 does not, establishes minimum effective dose. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8). Three-point dose-response: σ=0.1 (this), σ=0.2 (success), σ=0.5 (oscillatory failure).\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\"\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:0\"], \"pid\": \"59395\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\", \"submitted_at\": \"2026-05-20T11:42:56.447Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 0, \"model_name\": \"dreamer\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dmc_walker_walk\"}, \"metrics\": {\"eval_return_5K\": 35.6, \"eval_return_15K\": 99.1, \"eval_return_25K\": 140.7, \"eval_return_35K\": 155.7, \"eval_return_45K\": 160.9, \"eval_return_55K\": 254.8, \"eval_return_65K\": 268.7, \"eval_return_75K\": 295.5, \"eval_return_85K\": 220.8, \"eval_return_95K\": 188.6, \"eval_return_105K\": 204.7, \"eval_return_115K\": 296.4, \"eval_return_125K\": 232.3, \"eval_return_135K\": 247.4, \"ve_ratio_15K\": 0.0306, \"ve_ratio_25K\": 0.1606, \"ve_ratio_35K\": 0.3162, \"ve_ratio_45K\": 0.4807, \"ve_ratio_55K\": 0.4368, \"ve_ratio_65K\": 0.5432, \"ve_ratio_75K\": 0.6211, \"ve_ratio_85K\": 0.9533, \"ve_ratio_95K\": 1.0218, \"ve_ratio_105K\": 0.761, \"ve_ratio_115K\": 0.4514, \"ve_ratio_125K\": 0.4899, \"ve_ratio_135K\": 0.3995, \"nve_max\": 1.0218, \"nve_max_step\": \"95K\", \"current_step\": 135000, \"target_steps\": 210000}}, \"exp_027_tcn_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:51:53.479Z\", \"updated_at\": \"2026-05-20T12:45:31.028Z\", \"hypothesis\": \"TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different seed to verify that the NVE self-correction phenomenon (transient CIVO at 55K → NVE recovery to 0.83 by 75K) is reproducible across seeds, not a stochastic artifact. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.5.\", \"parent\": \"exp_027_tcn_walker_s0\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\"}, \"metrics\": {\"total_steps\": 215000, \"eval_return\": {\"5000\": 31, \"15000\": 140.5, \"25000\": 163.6, \"35000\": 153, \"45000\": 136.8, \"55000\": 158.3, \"65000\": 298.5, \"75000\": 364.9, \"85000\": 134, \"95000\": 94.6, \"105000\": 216.7, \"115000\": 318.9, \"125000\": 309.1, \"135000\": 216.1, \"145000\": 175.4, \"155000\": 171, \"165000\": 209.5, \"175000\": 120.4, \"185000\": 355.4, \"195000\": 183.3, \"205000\": 240.2, \"215000\": 350.8}, \"ve_ratio\": {\"15000\": 0.0246, \"25000\": 0.1416, \"35000\": 0.3585, \"45000\": 0.6101, \"55000\": 0.7092, \"65000\": 0.4875, \"75000\": 0.4902, \"85000\": 1.4104, \"95000\": 1.6367, \"105000\": 0.6444, \"115000\": 0.4021, \"125000\": 0.38, \"135000\": 0.5078, \"145000\": 0.8469, \"155000\": 0.8568, \"165000\": 0.5393, \"175000\": 0.7355, \"185000\": 0.211, \"195000\": 0.3513, \"205000\": 0.2376, \"215000\": 0.1476}, \"eval_peak\": 364.9, \"eval_peak_step\": 75000, \"eval_last10_mean\": 233.1, \"nve_max\": 1.6367, \"nve_max_step\": 95000, \"nve_final\": 0.1476}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:35:38.092Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:35:42.576855+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T12:38:02.085Z\"}, \"exp_027_tcn_walker_s0_sigma02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:25:32.533Z\", \"updated_at\": \"2026-05-20T12:06:21.855Z\", \"hypothesis\": \"TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding during imagination) but with σ=0.2 instead of 0.5. Tests whether smaller noise magnitude is sufficient to disrupt dt-specific value bias. If σ=0.5 works but σ=0.2 doesn't → noise magnitude matters; if both work → method is robust to σ choice.\", \"parent\": \"exp_027_tcn_walker_s0\", \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:0\", \"seed\": 0, \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\", \"model_name\": \"dreamerv3\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 215000}, \"metrics\": {\"eval_return_5K\": 35.6, \"eval_return_15K\": 150.6, \"eval_return_25K\": 199.4, \"eval_return_35K\": 278.2, \"eval_return_45K\": 315.6, \"eval_return_55K\": 278.6, \"eval_return_65K\": 331, \"eval_return_75K\": 293.1, \"eval_return_85K\": 363.9, \"eval_return_95K\": 171.4, \"eval_return_105K\": 236.4, \"eval_return_115K\": 543.8, \"eval_return_125K\": 458.4, \"eval_return_135K\": 496.7, \"eval_return_145K\": 542.7, \"eval_return_155K\": 660.5, \"eval_return_165K\": 653.3, \"eval_return_175K\": 821.1, \"eval_return_185K\": 560.5, \"eval_return_195K\": 567.9, \"eval_return_205K\": 558.7, \"eval_return_215K\": 551, \"ve_ratio_15K\": 0.0192, \"ve_ratio_25K\": 0.0961, \"ve_ratio_35K\": 0.1875, \"ve_ratio_45K\": 0.3009, \"ve_ratio_55K\": 0.5231, \"ve_ratio_65K\": 0.5654, \"ve_ratio_75K\": 0.611, \"ve_ratio_85K\": 0.4665, \"ve_ratio_95K\": 0.9081, \"ve_ratio_105K\": 0.5625, \"ve_ratio_115K\": 0.2105, \"ve_ratio_125K\": 0.2182, \"ve_ratio_135K\": 0.1764, \"ve_ratio_145K\": 0.143, \"ve_ratio_155K\": 0.106, \"ve_ratio_165K\": 0.0979, \"ve_ratio_175K\": 0.0729, \"ve_ratio_185K\": 0.1048, \"ve_ratio_195K\": 0.1026, \"ve_ratio_205K\": 0.0995, \"ve_ratio_215K\": 0.0955, \"eval_peak\": 821.1, \"eval_peak_step\": \"175K\", \"eval_last10_mean\": 587.1, \"nve_max\": 0.9081, \"nve_max_step\": \"95K\", \"nve_final\": 0.0955, \"total_steps\": 215000}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T11:19:31.331Z\"}, \"exp_030a_tcn_cheetah_s0_sigma02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:24:38.711Z\", \"updated_at\": \"2026-05-20T11:10:00.827Z\", \"hypothesis\": \"TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether CIVO suppression generalizes beyond Walker Walk. Cheetah exhibits stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) + TCN σ=0.2. If NVE<1.5× and eval maintained → TCN is environment-agnostic intervention.\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": \"210000 env steps\", \"model_name\": \"dreamerv3_tcn_sigma02_cheetah\", \"seed\": 0, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dmc_cheetah_run\", \"checkpoint_path\": \"logdir/exp_030a_tcn_cheetah_s0_sigma02/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\"}, \"metrics\": {\"eval_return_35K\": 299.5, \"eval_return_55K\": 31.9, \"ve_ratio_55K\": 1.903, \"current_step\": 64000, \"target_steps\": 210000, \"note\": \"WARNING: NVE breached 1.5× at 55K (1.903), eval crashed 299→32. Possible CIVO despite TCN.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T11:10:00.827Z\"}, \"exp_027_tcn_walker_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:44:51.820Z\", \"updated_at\": \"2026-05-20T09:24:09.016Z\", \"hypothesis\": \"Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5) to dt_embedding during imagination rollouts reduces dt conditioning precision, preventing critic from learning dt-specific value bias. Predicts CIVO suppression (NVE < 1.5×) with eval > 50% baseline (~450+). Based on obs-decoder SGS failure (gradient-level intervention insufficient) → need forward-pass/representation-level intervention.\", \"parent\": \"exp_025_obs_sgs_walker_s1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"888715\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"submitted_at\": \"2026-05-20T06:13:35.505Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11433.5, \"gpu_hours\": 3.18}, \"metrics\": {\"eval_return_5K\": 37.4, \"eval_return_15K\": 154.6, \"eval_return_25K\": 223.6, \"eval_return_35K\": 240, \"eval_return_45K\": 101.2, \"eval_return_55K\": 70, \"eval_return_65K\": 95.1, \"eval_return_75K\": 189.2, \"eval_return_85K\": 36, \"eval_return_95K\": 166.4, \"eval_return_105K\": 95.5, \"eval_return_112K\": 99.5, \"ve_ratio_15K\": 0.02, \"ve_ratio_25K\": 0.11, \"ve_ratio_35K\": 0.235, \"ve_ratio_45K\": 0.86, \"ve_ratio_55K\": 1.679, \"ve_ratio_65K\": 1.544, \"ve_ratio_75K\": 0.831, \"ve_ratio_85K\": 3.965, \"ve_ratio_95K\": 0.675, \"ve_ratio_105K\": 0.916, \"peak_eval\": 240, \"peak_eval_step\": \"35K\", \"peak_nve\": 3.965, \"peak_nve_step\": \"85K\", \"last_5_eval_avg\": 117.3, \"nve_breach_count\": 3, \"nve_breach_steps\": \"55K(1.68), 65K(1.54), 85K(3.97)\", \"final_step\": 120000, \"target_steps\": 210000, \"gate_dt_mean\": 2, \"gate_dt_entropy\": 0}, \"reproduce\": {\"finished_at\": \"2026-05-20T06:06:30.806Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T06:06:34.898602+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s0/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"analysis_summary\": \"TCN (σ=0.5 noise on dt_embedding) FAILED to suppress CIVO. NVE breached 1.5× threshold 3 times: 55K(1.68×), 65K(1.54×), 85K(3.97×). Peak NVE 3.97× at 85K is HIGHER than typical CIVO, suggesting TCN destabilizes value learning. Eval peaked at 240 (35K), then collapsed to avg 117 in latter half — far below 450 target. Gate remained fixed at dt=2 throughout (zero entropy). The noise magnitude was insufficient to decorrelate critic estimates from dt conditioning. Training reached 120K/210K planned. Hypothesis falsified: forward-pass noise at σ=0.5 does not prevent critic from exploiting dt-specific value structure.\", \"completed_at\": \"2026-05-20T09:24:09.016Z\"}, \"exp_028_rave_walker_s0_ceil15\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:25:34.045Z\", \"updated_at\": \"2026-05-20T08:31:12.389Z\", \"hypothesis\": \"RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value cap) but with ceiling=1.5 instead of 2.0. Tighter constraint tests whether more aggressive capping improves CIVO suppression without harming learning. If ceiling=2.0 works and 1.5 also works → method robust; if 1.5 hurts eval → ceiling choice is critical.\", \"parent\": \"exp_028_rave_walker_s0\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:1\"], \"pid\": \"38372\", \"tmux_session\": \"exp_028_rave_walker_s0_ceil15\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"210000 env steps\", \"model_name\": \"dreamerv3_rave_ceil15\", \"seed\": 0, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\", \"checkpoint_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\", \"checkpoint_source\": \"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"note\": \"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\"}, \"metrics\": {\"eval_return_5K\": 31.6, \"eval_return_15K\": 99.4, \"eval_return_25K\": 155.3, \"eval_return_35K\": 180.1, \"eval_return_45K\": 166.9, \"eval_return_55K\": 131, \"eval_return_65K\": 91.5, \"eval_return_75K\": 120.9, \"eval_return_85K\": 137.3, \"eval_return_95K\": 70.2, \"eval_return_105K\": 76.2, \"eval_return_115K\": 41.2, \"eval_return_125K\": 36.6, \"eval_return_135K\": 39.1, \"ve_ratio_15K\": 0.03, \"ve_ratio_25K\": 0.128, \"ve_ratio_35K\": 0.247, \"ve_ratio_45K\": 0.428, \"ve_ratio_55K\": 0.737, \"ve_ratio_65K\": 1.294, \"ve_ratio_75K\": 0.937, \"ve_ratio_85K\": 0.727, \"ve_ratio_95K\": 1.28, \"ve_ratio_105K\": 0.984, \"ve_ratio_115K\": 1.513, \"ve_ratio_125K\": 1.462, \"ve_ratio_135K\": 1.171, \"current_step\": 135000, \"target_steps\": 210000}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T08:31:12.389Z\"}, \"exp_028_rave_walker_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:44:53.882Z\", \"updated_at\": \"2026-05-20T06:14:31.720Z\", \"hypothesis\": \"Reality-Anchored Value Estimation (RAVE): cap imagination critic values at ceiling*v_anchor (ceiling=2.0, v_anchor=EMA of real-state critic values). Directly prevents pathological value inflation (NVE>1.5×) by bounding imagination/reality value ratio. Based on CIVO core mechanism being imagination value explosion → this directly caps the ratio without modifying gradients or training dynamics.\", \"parent\": \"exp_025_obs_sgs_walker_s1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"879636\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\", \"submitted_at\": \"2026-05-20T02:54:26.022Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"105000 env steps (52.5K agent steps, action_repeat=2)\", \"model_name\": \"dreamerv3_rave_ceil20\", \"seed\": 0, \"checkpoint_source\": \"N/A (trained from scratch, derives from SGS failure line)\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"wall_clock_seconds\": 12005.7, \"gpu_hours\": 3.33}, \"metrics\": {\"current_steps\": 105000, \"eval_trajectory\": {\"5K\": {\"eval_return\": 37.4, \"value_mean\": 0.001}, \"15K\": {\"eval_return\": 105.3, \"ve_ratio\": 0.028, \"value_mean\": 2.93}, \"25K\": {\"eval_return\": 191.9, \"ve_ratio\": 0.127, \"value_mean\": 24.4}, \"35K\": {\"eval_return\": 204.6, \"ve_ratio\": 0.267}, \"45K\": {\"eval_return\": 197.7, \"ve_ratio\": 0.439}, \"55K\": {\"eval_return\": 193, \"ve_ratio\": 0.62}, \"65K\": {\"eval_return\": 79.8, \"ve_ratio\": 1.832}, \"75K\": {\"eval_return\": 44.5, \"ve_ratio\": 3.415}, \"85K\": {\"eval_return\": 57.7, \"ve_ratio\": 2.126}, \"95K\": {\"eval_return\": 25.9, \"ve_ratio\": 4.086, \"value_mean\": 105.87}, \"105K\": {\"eval_return\": 29, \"ve_ratio\": 3.183, \"value_mean\": 92.2}}, \"note\": \"NEGATIVE. NVE diverged from 55K onward (0.62→4.09), eval collapsed 193→29. No self-correction.\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/checkpoint.ckpt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/\", \"completed_at\": \"2026-05-20T06:14:31.720Z\"}, \"exp_025_obs_sgs_walker_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:39:26.941Z\", \"updated_at\": \"2026-05-20T03:17:26.061Z\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:1\"], \"pid\": \"7989\", \"tmux_session\": \"exp_025_s2\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"210000 env steps (105K agent steps)\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"seed\": 2, \"log_path\": \"logdir/exp_025_obs_sgs_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s2/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval during training)\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T03:14:07.466Z\"}, \"failure_reason\": \"Reclassified: experiment completed 224K/210K steps normally. Cron misclassified as failed due to missing W&B sentinel. Actual result is negative — obs-decoder SGS suppressed CIVO (ve_ratio 0.8-1.4) but eval collapsed to ~90 (baseline ~930).\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T03:14:06.591Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T03:14:13.011509+00:00\"}]}, \"metrics\": {\"eval_return_215K\": 89.6, \"ve_ratio_215K\": 0.8, \"ve_ratio_185K\": 1.4, \"ve_ratio_175K\": 1.2, \"train_steps_completed\": 224000, \"target_steps\": 210000}, \"notes\": \"Obs-decoder SGS s2 完成全部训练（224K/210K steps）。ve_ratio 全程 0.8-1.4（CIVO 部分抑制），但 eval_return 仅 66-90（baseline ~930，远低于 70% 阈值 ~650）。与 s1/s3/s4 一致：obs-decoder SGS 无法在抑制 CIVO 的同时保持性能。梯度干预路线全面否定（Full SGS 0/3 + Obs-decoder SGS 0/6 有效）。\"}, \"exp_026_obs_sgs_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T20:19:29.171Z\", \"updated_at\": \"2026-05-20T03:02:46.556Z\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:1\"], \"pid\": \"16346\", \"tmux_session\": \"exp_026_s1\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": \"105000 env steps\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"seed\": 1, \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/train.log\", \"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:46.556Z\"}, \"exp_026_obs_sgs_cheetah_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T20:19:27.608Z\", \"updated_at\": \"2026-05-20T03:02:43.170Z\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:0\"], \"pid\": \"16208\", \"tmux_session\": \"exp_026_s0\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": \"105000 env steps\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"seed\": 0, \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/train.log\", \"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:43.170Z\"}, \"exp_025_obs_sgs_walker_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:39:29.810Z\", \"updated_at\": \"2026-05-20T03:02:39.948Z\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"851593\", \"tmux_session\": \"exp_025_s4\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"210000 env steps (105K agent steps)\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"seed\": 4, \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/train.log\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval during training)\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:39.948Z\"}, \"exp_025_obs_sgs_walker_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:39:28.402Z\", \"updated_at\": \"2026-05-20T03:02:36.670Z\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"847597\", \"tmux_session\": \"exp_025_s3\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"210000 env steps (105K agent steps)\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"seed\": 3, \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/train.log\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval during training)\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:36.670Z\"}, \"exp_025_obs_sgs_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:39:25.583Z\", \"updated_at\": \"2026-05-20T03:02:32.583Z\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:0\"], \"pid\": \"7833\", \"tmux_session\": \"exp_025_s1\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"210000 env steps (105K agent steps)\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"seed\": 1, \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval during training)\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:32.583Z\"}, \"exp_001_baseline_s4_extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:02:31.737Z\", \"updated_at\": \"2026-05-19T23:06:42.122Z\", \"hypothesis\": \"Walker Walk baseline seed=4 extended to 505K. Third long-run baseline seed for multi-seed NVE normalization. s4@105K=922.8 (highest), obtaining full ve_ratio profile.\", \"parent\": \"exp_001_baseline_s4\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"tmux_session\": \"exp_s4_ext\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"505000 env steps\", \"model_name\": \"dreamerv3_baseline\", \"seed\": 4, \"resumed_from_step\": 112000, \"target_steps\": 505000, \"checkpoint_source\": \"logdir/exp_001_baseline_s4/latest.pt\", \"checkpoint_path\": \"logdir/exp_001_baseline_s4/\", \"log_path\": \"logdir/exp_001_baseline_s4/train_extended.log\", \"eval_data\": \"dmc_walker_walk (online eval during training)\"}, \"conclusion\": \"success\", \"metrics\": {\"final_step\": 520000, \"final_eval_return\": 938.86, \"peak_eval_return\": 960.6, \"convergence_mean_250k_plus\": 935}, \"completed_at\": \"2026-05-19T23:06:42.122Z\"}, \"exp_001_baseline_s3_extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:02:30.382Z\", \"updated_at\": \"2026-05-19T21:23:44.025Z\", \"hypothesis\": \"Walker Walk baseline seed=3 extended to 505K. Second long-run baseline seed (alongside s2_ext) for multi-seed NVE normalization robustness. s3@105K=869.0, testing convergence to 920+ level.\", \"parent\": \"exp_001_baseline_s3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"tmux_session\": \"exp_s3_ext\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"505000 env steps\", \"model_name\": \"dreamerv3_baseline\", \"seed\": 3, \"resumed_from_step\": 120000, \"target_steps\": 505000, \"checkpoint_source\": \"logdir/exp_001_baseline_s3/latest.pt\", \"checkpoint_path\": \"logdir/exp_001_baseline_s3/\", \"log_path\": \"logdir/exp_001_baseline_s3/train_extended.log\", \"eval_data\": \"dmc_walker_walk (online eval during training)\"}, \"conclusion\": \"success\", \"metrics\": {\"final_step\": 520000, \"final_eval_return\": 947.68, \"final_train_return_avg\": 945.4, \"eval_profile\": {\"5000\": 42.15, \"15000\": 224.27, \"25000\": 329.99, \"35000\": 413.12, \"45000\": 332.69, \"55000\": 519.91, \"65000\": 667.42, \"72000\": 771.33, \"82000\": 772.88, \"92000\": 854.6, \"102000\": 869.03, \"112000\": 898.89, \"120000\": 898.38, \"130000\": 837.74, \"140000\": 876.64, \"150000\": 899.47, \"160000\": 922.77, \"170000\": 925.77, \"180000\": 912.89, \"190000\": 915.07, \"200000\": 894.77, \"210000\": 899.79, \"220000\": 951.18, \"230000\": 930.56, \"240000\": 910.47, \"250000\": 914.02, \"260000\": 931.33, \"270000\": 954.65, \"280000\": 928.01, \"290000\": 947.4, \"300000\": 853.32, \"310000\": 906.35, \"320000\": 847.16, \"330000\": 934.78, \"340000\": 921.08, \"350000\": 922.63, \"360000\": 844.99, \"370000\": 911.36, \"380000\": 917.73, \"390000\": 937.21, \"400000\": 928, \"410000\": 945.88, \"420000\": 897.2, \"430000\": 949.45, \"440000\": 937.28, \"450000\": 924.24, \"460000\": 967.25, \"470000\": 940.55, \"480000\": 936.24, \"490000\": 944.67, \"500000\": 957.09, \"510000\": 947.68}}, \"completed_at\": \"2026-05-19T21:23:44.025Z\"}, \"exp_001_baseline_s2_extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:10:10.948Z\", \"updated_at\": \"2026-05-19T17:44:27.212Z\", \"hypothesis\": \"Walker Walk baseline seed=2 extended to 505K. Tests whether low eval (443.5 @105K) is due to slow convergence or seed-level difference. s1=915.7, s3=869.0 at 105K.\", \"parent\": \"exp_001_baseline_s2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 2 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s2\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"tmux_session\": \"exp_s2_ext\", \"seed\": 2, \"model_name\": \"dreamerv3\", \"data_path\": \"logdir/exp_001_baseline_s2\", \"data_count\": 0, \"checkpoint_source\": \"logdir/exp_001_baseline_s2/latest.pt\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"resumed_from_step\": 112000, \"target_steps\": 505000, \"checkpoint_path\": \"logdir/exp_001_baseline_s2/latest.pt\", \"log_path\": \"logdir/exp_001_baseline_s2/train_extended.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 945.7, \"eval_return_peak\": 962.6, \"eval_return_at_105K\": 443.5, \"ve_ratio_at_105K\": 0.7422, \"value_mean_at_105K\": 329.16, \"ve_ratio_converged_range\": \"0.69-0.77\", \"value_mean_plateau\": 665, \"total_steps\": 512000}, \"completed_at\": \"2026-05-19T17:44:27.212Z\"}}, \"count\": 20, \"total\": 100, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4166}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "9c6dc953-8b6b-4a5c-8f6b-89d7963ad3eb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_029a_tcn_walker_s1_sigma02\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T08:31:29.514Z\\\", \\\"updated_at\\\": \\\"2026-05-20T16:47:55.888Z\\\", \\\"hypothesis\\\": \\\"TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02 which shows NVE<1.0× and eval reaching baseline at 135K. Tests whether CIVO suppression is reproducible across seeds. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.2. If s1 also shows NVE<1.0× → TCN σ=0.2 is a robust intervention.\\\", \\\"parent\\\": \\\"exp_027_tcn_walker_s0_sigma02\\\", \\\"spec\\\": {\\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"50924\\\", \\\"seed\\\": 1, \\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\\\", \\\"model_name\\\": \\\"dreamerv3\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 210000, \\\"checkpoint_path\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\\\", \\\"log_path\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/metrics.jsonl\\\"}, \\\"metrics\\\": {\\\"eval_return_5K\\\": 36.7, \\\"eval_return_15K\\\": 137.7, \\\"eval_return_25K\\\": 180.9, \\\"eval_return_35K\\\": 124, \\\"eval_return_45K\\\": 124.2, \\\"eval_return_55K\\\": 133.9, \\\"eval_return_65K\\\": 169.7, \\\"eval_return_75K\\\": 171.2, \\\"eval_return_85K\\\": 151.8, \\\"eval_return_95K\\\": 180.3, \\\"eval_return_105K\\\": 319.4, \\\"eval_return_115K\\\": 345.5, \\\"eval_return_125K\\\": 401, \\\"eval_return_135K\\\": 307.8, \\\"eval_return_145K\\\": 380.8, \\\"eval_return_155K\\\": 307.3, \\\"eval_return_165K\\\": 320.3, \\\"eval_return_175K\\\": 159, \\\"eval_return_185K\\\": 278.2, \\\"eval_return_195K\\\": 301.2, \\\"eval_return_205K\\\": 204.6, \\\"eval_return_215K\\\": 161.3, \\\"ve_ratio_15K\\\": 0.0248, \\\"ve_ratio_25K\\\": 0.1165, \\\"ve_ratio_35K\\\": 0.3574, \\\"ve_ratio_45K\\\": 0.5147, \\\"ve_ratio_55K\\\": 0.6428, \\\"ve_ratio_65K\\\": 0.4777, \\\"ve_ratio_75K\\\": 0.398, \\\"ve_ratio_85K\\\": 0.4033, \\\"ve_ratio_95K\\\": 0.3007, \\\"ve_ratio_105K\\\": 0.1554, \\\"ve_ratio_115K\\\": 0.1348, \\\"ve_ratio_125K\\\": 0.116, \\\"ve_ratio_135K\\\": 0.1449, \\\"ve_ratio_145K\\\": 0.1088, \\\"ve_ratio_155K\\\": 0.1287, \\\"ve_ratio_165K\\\": 0.1142, \\\"ve_ratio_175K\\\": 0.2138, \\\"ve_ratio_185K\\\": 0.121, \\\"ve_ratio_195K\\\": 0.1075, \\\"ve_ratio_205K\\\": 0.1503, \\\"ve_ratio_215K\\\": 0.1864, \\\"eval_peak\\\": 401, \\\"eval_peak_step\\\": \\\"125K\\\", \\\"nve_max\\\": 0.6428, \\\"nve_max_step\\\": \\\"55K\\\", \\\"nve_final\\\": 0.1864, \\\"current_step\\\": 215000, \\\"target_steps\\\": 210000, \\\"eval_last10_mean\\\": 282.15}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-20T16:47:17.713Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T16:47:18.789Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T16:47:29.902718+00:00\\\"}]}}, \\\"exp_030c_tcn_cheetah_s0_sigma10\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T16:26:11.800Z\\\", \\\"updated_at\\\": \\\"2026-05-20T16:26:18.487Z\\\", \\\"hypothesis\\\": \\\"Cheetah CIVO intensity (NVE 8-108×) requires proportionally higher TCN noise; σ=1.0 may match Cheetah's CIVO severity as σ=0.2 matched Walker's. Based on exp_030a (σ=0.2 negative, NVE=1.903) and exp_030b (σ=0.5 negative, NVE=10.67).\\\", \\\"parent\\\": \\\"exp_030b_tcn_cheetah_s0_sigma05\\\"}, \\\"exp_031_tcn_pickcube_s0_sigma02\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:09:56.923Z\\\", \\\"updated_at\\\": \\\"2026-05-20T16:20:39.337Z\\\", \\\"hypothesis\\\": \\\"TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination rollout will suppress CIVO in ManiSkill PickCube-v1, as it did in Walker Walk, by preventing the world model from overfitting to fixed dt signals.\\\", \\\"parent\\\": \\\"exp_019b_pickcube_civo_trigger\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"908459\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T12:42:41.707Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"maniskill_PickCube-v1\\\", \\\"data_count\\\": \\\"200000(online)\\\", \\\"model_name\\\": \\\"dreamerv3\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"none(train_from_scratch)\\\", \\\"eval_data\\\": \\\"maniskill_PickCube-v1(online_eval)\\\"}, \\\"metrics\\\": {\\\"eval_return_2.5K\\\": 2.4, \\\"eval_return_12.5K\\\": 19.2, \\\"eval_return_22.5K\\\": 17.7, \\\"eval_return_32.5K\\\": 11.5, \\\"eval_return_42.5K\\\": 7.8, \\\"eval_return_52.5K\\\": 4.8, \\\"eval_return_62.5K\\\": 10.4, \\\"ve_ratio_12.5K\\\": 0.1989, \\\"ve_ratio_22.5K\\\": 1.0128, \\\"ve_ratio_32.5K\\\": 2.2946, \\\"ve_ratio_42.5K\\\": 3.0555, \\\"ve_ratio_52.5K\\\": 3.7109, \\\"ve_ratio_62.5K\\\": 1.1999, \\\"nve_max\\\": 3.7109, \\\"nve_max_step\\\": \\\"52.5K\\\", \\\"current_step\\\": 62500, \\\"target_steps\\\": 200000}}, \\\"exp_030b_tcn_cheetah_s0_sigma05\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:07:53.975Z\\\", \\\"updated_at\\\": \\\"2026-05-20T16:20:36.095Z\\\", \\\"hypothesis\\\": \\\"Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the environment-appropriate dose (Walker σ=0.5 = overdose causing oscillatory CIVO, Cheetah σ=0.2 = underdose with NVE 1.903@55K). Tests whether TCN effectiveness is environment-dependent with σ scaling to CIVO severity. If NVE<1.5× and eval maintained → TCN is generalizable with environment-tuned σ.\\\", \\\"parent\\\": \\\"\\\", \\\"spec\\\": {\\\"gpu\\\": \\\"cuda:0\\\"}, \\\"metrics\\\": {\\\"eval_return_5K\\\": 8.3, \\\"eval_return_15K\\\": 78.3, \\\"eval_return_25K\\\": 219.3, \\\"eval_return_35K\\\": 296.5, \\\"eval_return_45K\\\": 32.8, \\\"eval_return_55K\\\": 6, \\\"eval_return_65K\\\": 71.2, \\\"eval_return_75K\\\": 23.3, \\\"eval_return_85K\\\": 34, \\\"eval_return_95K\\\": 143.6, \\\"eval_return_105K\\\": 104.4, \\\"eval_return_115K\\\": 137.7, \\\"eval_return_125K\\\": 211.7, \\\"eval_return_135K\\\": 97.2, \\\"eval_return_145K\\\": 79.4, \\\"eval_return_155K\\\": 76.8, \\\"eval_return_165K\\\": 77.5, \\\"eval_return_175K\\\": 85.7, \\\"eval_return_185K\\\": 68.7, \\\"eval_return_195K\\\": 77.6, \\\"ve_ratio_15K\\\": 0.0202, \\\"ve_ratio_25K\\\": 0.0636, \\\"ve_ratio_35K\\\": 0.1238, \\\"ve_ratio_45K\\\": 1.9141, \\\"ve_ratio_55K\\\": 10.6657, \\\"ve_ratio_65K\\\": 0.8371, \\\"ve_ratio_75K\\\": 1.9823, \\\"ve_ratio_85K\\\": 1.0946, \\\"ve_ratio_95K\\\": 0.2253, \\\"ve_ratio_105K\\\": 0.2686, \\\"ve_ratio_115K\\\": 0.1789, \\\"ve_ratio_125K\\\": 0.1037, \\\"ve_ratio_135K\\\": 0.2153, \\\"ve_ratio_145K\\\": 0.2478, \\\"ve_ratio_155K\\\": 0.2392, \\\"ve_ratio_165K\\\": 0.202, \\\"ve_ratio_175K\\\": 0.1591, \\\"ve_ratio_185K\\\": 0.1834, \\\"ve_ratio_195K\\\": 0.1534, \\\"nve_max\\\": 10.6657, \\\"nve_max_step\\\": \\\"55K\\\", \\\"nve_final\\\": 0.1534, \\\"current_step\\\": 195000, \\\"target_steps\\\": 210000}}, \\\"exp_029c_tcn_walker_s0_sigma01\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:09:50.913Z\\\", \\\"updated_at\\\": \\\"2026-05-20T16:20:28.451Z\\\", \\\"hypothesis\\\": \\\"σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2 prevents CIVO and σ=0.1 does not, establishes minimum effective dose. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8). Three-point dose-response: σ=0.1 (this), σ=0.2 (success), σ=0.5 (oscillatory failure).\\\", \\\"parent\\\": \\\"exp_027_tcn_walker_s0_sigma02\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"59395\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T11:42:56.447Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"seed\\\": 0, \\\"model_name\\\": \\\"dreamer\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 210000, \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"eval_data\\\": \\\"dmc_walker_walk\\\"}, \\\"metrics\\\": {\\\"eval_return_5K\\\": 35.6, \\\"eval_return_15K\\\": 99.1, \\\"eval_return_25K\\\": 140.7, \\\"eval_return_35K\\\": 155.7, \\\"eval_return_45K\\\": 160.9, \\\"eval_return_55K\\\": 254.8, \\\"eval_return_65K\\\": 268.7, \\\"eval_return_75K\\\": 295.5, \\\"eval_return_85K\\\": 220.8, \\\"eval_return_95K\\\": 188.6, \\\"eval_return_105K\\\": 204.7, \\\"eval_return_115K\\\": 296.4, \\\"eval_return_125K\\\": 232.3, \\\"eval_return_135K\\\": 247.4, \\\"ve_ratio_15K\\\": 0.0306, \\\"ve_ratio_25K\\\": 0.1606, \\\"ve_ratio_35K\\\": 0.3162, \\\"ve_ratio_45K\\\": 0.4807, \\\"ve_ratio_55K\\\": 0.4368, \\\"ve_ratio_65K\\\": 0.5432, \\\"ve_ratio_75K\\\": 0.6211, \\\"ve_ratio_85K\\\": 0.9533, \\\"ve_ratio_95K\\\": 1.0218, \\\"ve_ratio_105K\\\": 0.761, \\\"ve_ratio_115K\\\": 0.4514, \\\"ve_ratio_125K\\\": 0.4899, \\\"ve_ratio_135K\\\": 0.3995, \\\"nve_max\\\": 1.0218, \\\"nve_max_step\\\": \\\"95K\\\", \\\"current_step\\\": 135000, \\\"target_steps\\\": 210000}}, \\\"exp_027_tcn_walker_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T05:51:53.479Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:45:31.028Z\\\", \\\"hypothesis\\\": \\\"TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different seed to verify that the NVE self-correction phenomenon (transient CIVO at 55K → NVE recovery to 0.83 by 75K) is reproducible across seeds, not a stochastic artifact. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.5.\\\", \\\"parent\\\": \\\"exp_027_tcn_walker_s0\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\\\"}, \\\"metrics\\\": {\\\"total_steps\\\": 215000, \\\"eval_return\\\": {\\\"5000\\\": 31, \\\"15000\\\": 140.5, \\\"25000\\\": 163.6, \\\"35000\\\": 153, \\\"45000\\\": 136.8, \\\"55000\\\": 158.3, \\\"65000\\\": 298.5, \\\"75000\\\": 364.9, \\\"85000\\\": 134, \\\"95000\\\": 94.6, \\\"105000\\\": 216.7, \\\"115000\\\": 318.9, \\\"125000\\\": 309.1, \\\"135000\\\": 216.1, \\\"145000\\\": 175.4, \\\"155000\\\": 171, \\\"165000\\\": 209.5, \\\"175000\\\": 120.4, \\\"185000\\\": 355.4, \\\"195000\\\": 183.3, \\\"205000\\\": 240.2, \\\"215000\\\": 350.8}, \\\"ve_ratio\\\": {\\\"15000\\\": 0.0246, \\\"25000\\\": 0.1416, \\\"35000\\\": 0.3585, \\\"45000\\\": 0.6101, \\\"55000\\\": 0.7092, \\\"65000\\\": 0.4875, \\\"75000\\\": 0.4902, \\\"85000\\\": 1.4104, \\\"95000\\\": 1.6367, \\\"105000\\\": 0.6444, \\\"115000\\\": 0.4021, \\\"125000\\\": 0.38, \\\"135000\\\": 0.5078, \\\"145000\\\": 0.8469, \\\"155000\\\": 0.8568, \\\"165000\\\": 0.5393, \\\"175000\\\": 0.7355, \\\"185000\\\": 0.211, \\\"195000\\\": 0.3513, \\\"205000\\\": 0.2376, \\\"215000\\\": 0.1476}, \\\"eval_peak\\\": 364.9, \\\"eval_peak_step\\\": 75000, \\\"eval_last10_mean\\\": 233.1, \\\"nve_max\\\": 1.6367, \\\"nve_max_step\\\": 95000, \\\"nve_final\\\": 0.1476}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-20T12:35:38.092Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T12:35:42.576855+00:00\\\"}]}, \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-20T12:38:02.085Z\\\"}, \\\"exp_027_tcn_walker_s0_sigma02\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T03:25:32.533Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:06:21.855Z\\\", \\\"hypothesis\\\": \\\"TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding during imagination) but with σ=0.2 instead of 0.5. Tests whether smaller noise magnitude is sufficient to disrupt dt-specific value bias. If σ=0.5 works but σ=0.2 doesn't → noise magnitude matters; if both work → method is robust to σ choice.\\\", \\\"parent\\\": \\\"exp_027_tcn_walker_s0\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\\\", \\\"log_path\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"seed\\\": 0, \\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\\\", \\\"model_name\\\": \\\"dreamerv3\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 215000}, \\\"metrics\\\": {\\\"eval_return_5K\\\": 35.6, \\\"eval_return_15K\\\": 150.6, \\\"eval_return_25K\\\": 199.4, \\\"eval_return_35K\\\": 278.2, \\\"eval_return_45K\\\": 315.6, \\\"eval_return_55K\\\": 278.6, \\\"eval_return_65K\\\": 331, \\\"eval_return_75K\\\": 293.1, \\\"eval_return_85K\\\": 363.9, \\\"eval_return_95K\\\": 171.4, \\\"eval_return_105K\\\": 236.4, \\\"eval_return_115K\\\": 543.8, \\\"eval_return_125K\\\": 458.4, \\\"eval_return_135K\\\": 496.7, \\\"eval_return_145K\\\": 542.7, \\\"eval_return_155K\\\": 660.5, \\\"eval_return_165K\\\": 653.3, \\\"eval_return_175K\\\": 821.1, \\\"eval_return_185K\\\": 560.5, \\\"eval_return_195K\\\": 567.9, \\\"eval_return_205K\\\": 558.7, \\\"eval_return_215K\\\": 551, \\\"ve_ratio_15K\\\": 0.0192, \\\"ve_ratio_25K\\\": 0.0961, \\\"ve_ratio_35K\\\": 0.1875, \\\"ve_ratio_45K\\\": 0.3009, \\\"ve_ratio_55K\\\": 0.5231, \\\"ve_ratio_65K\\\": 0.5654, \\\"ve_ratio_75K\\\": 0.611, \\\"ve_ratio_85K\\\": 0.4665, \\\"ve_ratio_95K\\\": 0.9081, \\\"ve_ratio_105K\\\": 0.5625, \\\"ve_ratio_115K\\\": 0.2105, \\\"ve_ratio_125K\\\": 0.2182, \\\"ve_ratio_135K\\\": 0.1764, \\\"ve_ratio_145K\\\": 0.143, \\\"ve_ratio_155K\\\": 0.106, \\\"ve_ratio_165K\\\": 0.0979, \\\"ve_ratio_175K\\\": 0.0729, \\\"ve_ratio_185K\\\": 0.1048, \\\"ve_ratio_195K\\\": 0.1026, \\\"ve_ratio_205K\\\": 0.0995, \\\"ve_ratio_215K\\\": 0.0955, \\\"eval_peak\\\": 821.1, \\\"eval_peak_step\\\": \\\"175K\\\", \\\"eval_last10_mean\\\": 587.1, \\\"nve_max\\\": 0.9081, \\\"nve_max_step\\\": \\\"95K\\\", \\\"nve_final\\\": 0.0955, \\\"total_steps\\\": 215000}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T11:19:31.331Z\\\"}, \\\"exp_030a_tcn_cheetah_s0_sigma02\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T09:24:38.711Z\\\", \\\"updated_at\\\": \\\"2026-05-20T11:10:00.827Z\\\", \\\"hypothesis\\\": \\\"TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether CIVO suppression generalizes beyond Walker Walk. Cheetah exhibits stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) + TCN σ=0.2. If NVE<1.5× and eval maintained → TCN is environment-agnostic intervention.\\\", \\\"parent\\\": \\\"exp_027_tcn_walker_s0_sigma02\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"data_count\\\": \\\"210000 env steps\\\", \\\"model_name\\\": \\\"dreamerv3_tcn_sigma02_cheetah\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_030a_tcn_cheetah_s0_sigma02/\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\\\"}, \\\"metrics\\\": {\\\"eval_return_35K\\\": 299.5, \\\"eval_return_55K\\\": 31.9, \\\"ve_ratio_55K\\\": 1.903, \\\"current_step\\\": 64000, \\\"target_steps\\\": 210000, \\\"note\\\": \\\"WARNING: NVE breached 1.5× at 55K (1.903), eval crashed 299→32. Possible CIVO despite TCN.\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-20T11:10:00.827Z\\\"}, \\\"exp_027_tcn_walker_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T02:44:51.820Z\\\", \\\"updated_at\\\": \\\"2026-05-20T09:24:09.016Z\\\", \\\"hypothesis\\\": \\\"Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5) to dt_embedding during imagination rollouts reduces dt conditioning precision, preventing critic from learning dt-specific value bias. Predicts CIVO suppression (NVE < 1.5×) with eval > 50% baseline (~450+). Based on obs-decoder SGS failure (gradient-level intervention insufficient) → need forward-pass/representation-level intervention.\\\", \\\"parent\\\": \\\"exp_025_obs_sgs_walker_s1\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"888715\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T06:13:35.505Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 11433.5, \\\"gpu_hours\\\": 3.18}, \\\"metrics\\\": {\\\"eval_return_5K\\\": 37.4, \\\"eval_return_15K\\\": 154.6, \\\"eval_return_25K\\\": 223.6, \\\"eval_return_35K\\\": 240, \\\"eval_return_45K\\\": 101.2, \\\"eval_return_55K\\\": 70, \\\"eval_return_65K\\\": 95.1, \\\"eval_return_75K\\\": 189.2, \\\"eval_return_85K\\\": 36, \\\"eval_return_95K\\\": 166.4, \\\"eval_return_105K\\\": 95.5, \\\"eval_return_112K\\\": 99.5, \\\"ve_ratio_15K\\\": 0.02, \\\"ve_ratio_25K\\\": 0.11, \\\"ve_ratio_35K\\\": 0.235, \\\"ve_ratio_45K\\\": 0.86, \\\"ve_ratio_55K\\\": 1.679, \\\"ve_ratio_65K\\\": 1.544, \\\"ve_ratio_75K\\\": 0.831, \\\"ve_ratio_85K\\\": 3.965, \\\"ve_ratio_95K\\\": 0.675, \\\"ve_ratio_105K\\\": 0.916, \\\"peak_eval\\\": 240, \\\"peak_eval_step\\\": \\\"35K\\\", \\\"peak_nve\\\": 3.965, \\\"peak_nve_step\\\": \\\"85K\\\", \\\"last_5_eval_avg\\\": 117.3, \\\"nve_breach_count\\\": 3, \\\"nve_breach_steps\\\": \\\"55K(1.68), 65K(1.54), 85K(3.97)\\\", \\\"final_step\\\": 120000, \\\"target_steps\\\": 210000, \\\"gate_dt_mean\\\": 2, \\\"gate_dt_entropy\\\": 0}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-20T06:06:30.806Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T06:06:34.898602+00:00\\\"}]}, \\\"conclusion\\\": \\\"negative\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s0/latest.pt\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\\\", \\\"analysis_summary\\\": \\\"TCN (σ=0.5 noise on dt_embedding) FAILED to suppress CIVO. NVE breached 1.5× threshold 3 times: 55K(1.68×), 65K(1.54×), 85K(3.97×). Peak NVE 3.97× at 85K is HIGHER than typical CIVO, suggesting TCN destabilizes value learning. Eval peaked at 240 (35K), then collapsed to avg 117 in latter half — far below 450 target. Gate remained fixed at dt=2 throughout (zero entropy). The noise magnitude was insufficient to decorrelate critic estimates from dt conditioning. Training reached 120K/210K planned. Hypothesis falsified: forward-pass noise at σ=0.5 does not prevent critic from exploiting dt-specific value structure.\\\", \\\"completed_at\\\": \\\"2026-05-20T09:24:09.016Z\\\"}, \\\"exp_028_rave_walker_s0_ceil15\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T03:25:34.045Z\\\", \\\"updated_at\\\": \\\"2026-05-20T08:31:12.389Z\\\", \\\"hypothesis\\\": \\\"RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value cap) but with ceiling=1.5 instead of 2.0. Tighter constraint tests whether more aggressive capping improves CIVO suppression without harming learning. If ceiling=2.0 works and 1.5 also works → method robust; if 1.5 hurts eval → ceiling choice is critical.\\\", \\\"parent\\\": \\\"exp_028_rave_walker_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"38372\\\", \\\"tmux_session\\\": \\\"exp_028_rave_walker_s0_ceil15\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": \\\"210000 env steps\\\", \\\"model_name\\\": \\\"dreamerv3_rave_ceil15\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\\\", \\\"checkpoint_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\", \\\"note\\\": \\\"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\\\"}, \\\"metrics\\\": {\\\"eval_return_5K\\\": 31.6, \\\"eval_return_15K\\\": 99.4, \\\"eval_return_25K\\\": 155.3, \\\"eval_return_35K\\\": 180.1, \\\"eval_return_45K\\\": 166.9, \\\"eval_return_55K\\\": 131, \\\"eval_return_65K\\\": 91.5, \\\"eval_return_75K\\\": 120.9, \\\"eval_return_85K\\\": 137.3, \\\"eval_return_95K\\\": 70.2, \\\"eval_return_105K\\\": 76.2, \\\"eval_return_115K\\\": 41.2, \\\"eval_return_125K\\\": 36.6, \\\"eval_return_135K\\\": 39.1, \\\"ve_ratio_15K\\\": 0.03, \\\"ve_ratio_25K\\\": 0.128, \\\"ve_ratio_35K\\\": 0.247, \\\"ve_ratio_45K\\\": 0.428, \\\"ve_ratio_55K\\\": 0.737, \\\"ve_ratio_65K\\\": 1.294, \\\"ve_ratio_75K\\\": 0.937, \\\"ve_ratio_85K\\\": 0.727, \\\"ve_ratio_95K\\\": 1.28, \\\"ve_ratio_105K\\\": 0.984, \\\"ve_ratio_115K\\\": 1.513, \\\"ve_ratio_125K\\\": 1.462, \\\"ve_ratio_135K\\\": 1.171, \\\"current_step\\\": 135000, \\\"target_steps\\\": 210000}, \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-20T08:31:12.389Z\\\"}, \\\"exp_028_rave_walker_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T02:44:53.882Z\\\", \\\"updated_at\\\": \\\"2026-05-20T06:14:31.720Z\\\", \\\"hypothesis\\\": \\\"Reality-Anchored Value Estimation (RAVE): cap imagination critic values at ceiling*v_anchor (ceiling=2.0, v_anchor=EMA of real-state critic values). Directly prevents pathological value inflation (NVE>1.5×) by bounding imagination/reality value ratio. Based on CIVO core mechanism being imagination value explosion → this directly caps the ratio without modifying gradients or training dynamics.\\\", \\\"parent\\\": \\\"exp_025_obs_sgs_walker_s1\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"879636\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T02:54:26.022Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": \\\"105000 env steps (52.5K agent steps, action_repeat=2)\\\", \\\"model_name\\\": \\\"dreamerv3_rave_ceil20\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (trained from scratch, derives from SGS failure line)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\", \\\"wall_clock_seconds\\\": 12005.7, \\\"gpu_hours\\\": 3.33}, \\\"metrics\\\": {\\\"current_steps\\\": 105000, \\\"eval_trajectory\\\": {\\\"5K\\\": {\\\"eval_return\\\": 37.4, \\\"value_mean\\\": 0.001}, \\\"15K\\\": {\\\"eval_return\\\": 105.3, \\\"ve_ratio\\\": 0.028, \\\"value_mean\\\": 2.93}, \\\"25K\\\": {\\\"eval_return\\\": 191.9, \\\"ve_ratio\\\": 0.127, \\\"value_mean\\\": 24.4}, \\\"35K\\\": {\\\"eval_return\\\": 204.6, \\\"ve_ratio\\\": 0.267}, \\\"45K\\\": {\\\"eval_return\\\": 197.7, \\\"ve_ratio\\\": 0.439}, \\\"55K\\\": {\\\"eval_return\\\": 193, \\\"ve_ratio\\\": 0.62}, \\\"65K\\\": {\\\"eval_return\\\": 79.8, \\\"ve_ratio\\\": 1.832}, \\\"75K\\\": {\\\"eval_return\\\": 44.5, \\\"ve_ratio\\\": 3.415}, \\\"85K\\\": {\\\"eval_return\\\": 57.7, \\\"ve_ratio\\\": 2.126}, \\\"95K\\\": {\\\"eval_return\\\": 25.9, \\\"ve_ratio\\\": 4.086, \\\"value_mean\\\": 105.87}, \\\"105K\\\": {\\\"eval_return\\\": 29, \\\"ve_ratio\\\": 3.183, \\\"value_mean\\\": 92.2}}, \\\"note\\\": \\\"NEGATIVE. NVE diverged from 55K onward (0.62→4.09), eval collapsed 193→29. No self-correction.\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/checkpoint.ckpt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/\\\", \\\"completed_at\\\": \\\"2026-05-20T06:14:31.720Z\\\"}, \\\"exp_025_obs_sgs_walker_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T16:39:26.941Z\\\", \\\"updated_at\\\": \\\"2026-05-20T03:17:26.061Z\\\", \\\"hypothesis\\\": \\\"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\\\", \\\"parent\\\": \\\"exp_018_full_sgs_walker_s1\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"7989\\\", \\\"tmux_session\\\": \\\"exp_025_s2\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": \\\"210000 env steps (105K agent steps)\\\", \\\"model_name\\\": \\\"dreamerv3_obs_decoder_sgs\\\", \\\"seed\\\": 2, \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s2/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s2/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-20T03:14:07.466Z\\\"}, \\\"failure_reason\\\": \\\"Reclassified: experiment completed 224K/210K steps normally. Cron misclassified as failed due to missing W&B sentinel. Actual result is negative — obs-decoder SGS suppressed CIVO (ve_ratio 0.8-1.4) but eval collapsed to ~90 (baseline ~930).\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-20T03:14:06.591Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T03:14:13.011509+00:00\\\"}]}, \\\"metrics\\\": {\\\"eval_return_215K\\\": 89.6, \\\"ve_ratio_215K\\\": 0.8, \\\"ve_ratio_185K\\\": 1.4, \\\"ve_ratio_175K\\\": 1.2, \\\"train_steps_completed\\\": 224000, \\\"target_steps\\\": 210000}, \\\"notes\\\": \\\"Obs-decoder SGS s2 完成全部训练（224K/210K steps）。ve_ratio 全程 0.8-1.4（CIVO 部分抑制），但 eval_return 仅 66-90（baseline ~930，远低于 70% 阈值 ~650）。与 s1/s3/s4 一致：obs-decoder SGS 无法在抑制 CIVO 的同时保持性能。梯度干预路线全面否定（Full SGS 0/3 + Obs-decoder SGS 0/6 有效）。\\\"}, \\\"exp_026_obs_sgs_cheetah_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T20:19:29.171Z\\\", \\\"updated_at\\\": \\\"2026-05-20T03:02:46.556Z\\\", \\\"hypothesis\\\": \\\"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\\\", \\\"parent\\\": \\\"exp_010b_cheetah_civo_trigger\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"16346\\\", \\\"tmux_session\\\": \\\"exp_026_s1\\\", \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"data_count\\\": \\\"105000 env steps\\\", \\\"model_name\\\": \\\"dreamerv3_obs_decoder_sgs_cheetah\\\", \\\"seed\\\": 1, \\\"log_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s1/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s1/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch)\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval during training)\\\"}, \\\"failure_reason\\\": \\\"startup recovery: process dead, no active cron monitor\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-20T03:02:46.556Z\\\"}, \\\"exp_026_obs_sgs_cheetah_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T20:19:27.608Z\\\", \\\"updated_at\\\": \\\"2026-05-20T03:02:43.170Z\\\", \\\"hypothesis\\\": \\\"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\\\", \\\"parent\\\": \\\"exp_010b_cheetah_civo_trigger_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"16208\\\", \\\"tmux_session\\\": \\\"exp_026_s0\\\", \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"data_count\\\": \\\"105000 env steps\\\", \\\"model_name\\\": \\\"dreamerv3_obs_decoder_sgs_cheetah\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s0/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s0/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch)\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval during training)\\\"}, \\\"failure_reason\\\": \\\"startup recovery: process dead, no active cron monitor\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-20T03:02:43.170Z\\\"}, \\\"exp_025_obs_sgs_walker_s4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T16:39:29.810Z\\\", \\\"updated_at\\\": \\\"2026-05-20T03:02:39.948Z\\\", \\\"hypothesis\\\": \\\"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\\\", \\\"parent\\\": \\\"exp_018_full_sgs_walker_s1\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"851593\\\", \\\"tmux_session\\\": \\\"exp_025_s4\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": \\\"210000 env steps (105K agent steps)\\\", \\\"model_name\\\": \\\"dreamerv3_obs_decoder_sgs\\\", \\\"seed\\\": 4, \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s4/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s4/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\"}, \\\"failure_reason\\\": \\\"startup recovery: process dead, no active cron monitor\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-20T03:02:39.948Z\\\"}, \\\"exp_025_obs_sgs_walker_s3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T16:39:28.402Z\\\", \\\"updated_at\\\": \\\"2026-05-20T03:02:36.670Z\\\", \\\"hypothesis\\\": \\\"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\\\", \\\"parent\\\": \\\"exp_018_full_sgs_walker_s1\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"847597\\\", \\\"tmux_session\\\": \\\"exp_025_s3\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": \\\"210000 env steps (105K agent steps)\\\", \\\"model_name\\\": \\\"dreamerv3_obs_decoder_sgs\\\", \\\"seed\\\": 3, \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s3/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s3/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\"}, \\\"failure_reason\\\": \\\"startup recovery: process dead, no active cron monitor\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-20T03:02:36.670Z\\\"}, \\\"exp_025_obs_sgs_walker_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T16:39:25.583Z\\\", \\\"updated_at\\\": \\\"2026-05-20T03:02:32.583Z\\\", \\\"hypothesis\\\": \\\"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\\\", \\\"parent\\\": \\\"exp_018_full_sgs_walker_s1\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"7833\\\", \\\"tmux_session\\\": \\\"exp_025_s1\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": \\\"210000 env steps (105K agent steps)\\\", \\\"model_name\\\": \\\"dreamerv3_obs_decoder_sgs\\\", \\\"seed\\\": 1, \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s1/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s1/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\"}, \\\"failure_reason\\\": \\\"startup recovery: process dead, no active cron monitor\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-20T03:02:32.583Z\\\"}, \\\"exp_001_baseline_s4_extended\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T09:02:31.737Z\\\", \\\"updated_at\\\": \\\"2026-05-19T23:06:42.122Z\\\", \\\"hypothesis\\\": \\\"Walker Walk baseline seed=4 extended to 505K. Third long-run baseline seed for multi-seed NVE normalization. s4@105K=922.8 (highest), obtaining full ve_ratio profile.\\\", \\\"parent\\\": \\\"exp_001_baseline_s4\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"tmux_session\\\": \\\"exp_s4_ext\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": \\\"505000 env steps\\\", \\\"model_name\\\": \\\"dreamerv3_baseline\\\", \\\"seed\\\": 4, \\\"resumed_from_step\\\": 112000, \\\"target_steps\\\": 505000, \\\"checkpoint_source\\\": \\\"logdir/exp_001_baseline_s4/latest.pt\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_001_baseline_s4/\\\", \\\"log_path\\\": \\\"logdir/exp_001_baseline_s4/train_extended.log\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_step\\\": 520000, \\\"final_eval_return\\\": 938.86, \\\"peak_eval_return\\\": 960.6, \\\"convergence_mean_250k_plus\\\": 935}, \\\"completed_at\\\": \\\"2026-05-19T23:06:42.122Z\\\"}, \\\"exp_001_baseline_s3_extended\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T09:02:30.382Z\\\", \\\"updated_at\\\": \\\"2026-05-19T21:23:44.025Z\\\", \\\"hypothesis\\\": \\\"Walker Walk baseline seed=3 extended to 505K. Second long-run baseline seed (alongside s2_ext) for multi-seed NVE normalization robustness. s3@105K=869.0, testing convergence to 920+ level.\\\", \\\"parent\\\": \\\"exp_001_baseline_s3\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"tmux_session\\\": \\\"exp_s3_ext\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": \\\"505000 env steps\\\", \\\"model_name\\\": \\\"dreamerv3_baseline\\\", \\\"seed\\\": 3, \\\"resumed_from_step\\\": 120000, \\\"target_steps\\\": 505000, \\\"checkpoint_source\\\": \\\"logdir/exp_001_baseline_s3/latest.pt\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_001_baseline_s3/\\\", \\\"log_path\\\": \\\"logdir/exp_001_baseline_s3/train_extended.log\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_step\\\": 520000, \\\"final_eval_return\\\": 947.68, \\\"final_train_return_avg\\\": 945.4, \\\"eval_profile\\\": {\\\"5000\\\": 42.15, \\\"15000\\\": 224.27, \\\"25000\\\": 329.99, \\\"35000\\\": 413.12, \\\"45000\\\": 332.69, \\\"55000\\\": 519.91, \\\"65000\\\": 667.42, \\\"72000\\\": 771.33, \\\"82000\\\": 772.88, \\\"92000\\\": 854.6, \\\"102000\\\": 869.03, \\\"112000\\\": 898.89, \\\"120000\\\": 898.38, \\\"130000\\\": 837.74, \\\"140000\\\": 876.64, \\\"150000\\\": 899.47, \\\"160000\\\": 922.77, \\\"170000\\\": 925.77, \\\"180000\\\": 912.89, \\\"190000\\\": 915.07, \\\"200000\\\": 894.77, \\\"210000\\\": 899.79, \\\"220000\\\": 951.18, \\\"230000\\\": 930.56, \\\"240000\\\": 910.47, \\\"250000\\\": 914.02, \\\"260000\\\": 931.33, \\\"270000\\\": 954.65, \\\"280000\\\": 928.01, \\\"290000\\\": 947.4, \\\"300000\\\": 853.32, \\\"310000\\\": 906.35, \\\"320000\\\": 847.16, \\\"330000\\\": 934.78, \\\"340000\\\": 921.08, \\\"350000\\\": 922.63, \\\"360000\\\": 844.99, \\\"370000\\\": 911.36, \\\"380000\\\": 917.73, \\\"390000\\\": 937.21, \\\"400000\\\": 928, \\\"410000\\\": 945.88, \\\"420000\\\": 897.2, \\\"430000\\\": 949.45, \\\"440000\\\": 937.28, \\\"450000\\\": 924.24, \\\"460000\\\": 967.25, \\\"470000\\\": 940.55, \\\"480000\\\": 936.24, \\\"490000\\\": 944.67, \\\"500000\\\": 957.09, \\\"510000\\\": 947.68}}, \\\"completed_at\\\": \\\"2026-05-19T21:23:44.025Z\\\"}, \\\"exp_001_baseline_s2_extended\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T04:10:10.948Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:44:27.212Z\\\", \\\"hypothesis\\\": \\\"Walker Walk baseline seed=2 extended to 505K. Tests whether low eval (443.5 @105K) is due to slow convergence or seed-level difference. s1=915.7, s3=869.0 at 105K.\\\", \\\"parent\\\": \\\"exp_001_baseline_s2\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 2 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s2\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"tmux_session\\\": \\\"exp_s2_ext\\\", \\\"seed\\\": 2, \\\"model_name\\\": \\\"dreamerv3\\\", \\\"data_path\\\": \\\"logdir/exp_001_baseline_s2\\\", \\\"data_count\\\": 0, \\\"checkpoint_source\\\": \\\"logdir/exp_001_baseline_s2/latest.pt\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval)\\\", \\\"resumed_from_step\\\": 112000, \\\"target_steps\\\": 505000, \\\"checkpoint_path\\\": \\\"logdir/exp_001_baseline_s2/latest.pt\\\", \\\"log_path\\\": \\\"logdir/exp_001_baseline_s2/train_extended.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_return_final\\\": 945.7, \\\"eval_return_peak\\\": 962.6, \\\"eval_return_at_105K\\\": 443.5, \\\"ve_ratio_at_105K\\\": 0.7422, \\\"value_mean_at_105K\\\": 329.16, \\\"ve_ratio_converged_range\\\": \\\"0.69-0.77\\\", \\\"value_mean_plateau\\\": 665, \\\"total_steps\\\": 512000}, \\\"completed_at\\\": \\\"2026-05-19T17:44:27.212Z\\\"}}, \\\"count\\\": 20, \\\"total\\\": 100, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4166}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_029a_tcn_walker_s1_sigma02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:31:29.514Z\", \"updated_at\": \"2026-05-20T16:47:55.888Z\", \"hypothesis\": \"TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02 which shows NVE<1.0× and eval reaching baseline at 135K. Tests whether CIVO suppression is reproducible across seeds. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.2. If s1 also shows NVE<1.0× → TCN σ=0.2 is a robust intervention.\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"spec\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"pid\": \"50924\", \"seed\": 1, \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\", \"model_name\": \"dreamerv3\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/metrics.jsonl\"}, \"metrics\": {\"eval_return_5K\": 36.7, \"eval_return_15K\": 137.7, \"eval_return_25K\": 180.9, \"eval_return_35K\": 124, \"eval_return_45K\": 124.2, \"eval_return_55K\": 133.9, \"eval_return_65K\": 169.7, \"eval_return_75K\": 171.2, \"eval_return_85K\": 151.8, \"eval_return_95K\": 180.3, \"eval_return_105K\": 319.4, \"eval_return_115K\": 345.5, \"eval_return_125K\": 401, \"eval_return_135K\": 307.8, \"eval_return_145K\": 380.8, \"eval_return_155K\": 307.3, \"eval_return_165K\": 320.3, \"eval_return_175K\": 159, \"eval_return_185K\": 278.2, \"eval_return_195K\": 301.2, \"eval_return_205K\": 204.6, \"eval_return_215K\": 161.3, \"ve_ratio_15K\": 0.0248, \"ve_ratio_25K\": 0.1165, \"ve_ratio_35K\": 0.3574, \"ve_ratio_45K\": 0.5147, \"ve_ratio_55K\": 0.6428, \"ve_ratio_65K\": 0.4777, \"ve_ratio_75K\": 0.398, \"ve_ratio_85K\": 0.4033, \"ve_ratio_95K\": 0.3007, \"ve_ratio_105K\": 0.1554, \"ve_ratio_115K\": 0.1348, \"ve_ratio_125K\": 0.116, \"ve_ratio_135K\": 0.1449, \"ve_ratio_145K\": 0.1088, \"ve_ratio_155K\": 0.1287, \"ve_ratio_165K\": 0.1142, \"ve_ratio_175K\": 0.2138, \"ve_ratio_185K\": 0.121, \"ve_ratio_195K\": 0.1075, \"ve_ratio_205K\": 0.1503, \"ve_ratio_215K\": 0.1864, \"eval_peak\": 401, \"eval_peak_step\": \"125K\", \"nve_max\": 0.6428, \"nve_max_step\": \"55K\", \"nve_final\": 0.1864, \"current_step\": 215000, \"target_steps\": 210000, \"eval_last10_mean\": 282.15}, \"reproduce\": {\"finished_at\": \"2026-05-20T16:47:17.713Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:47:18.789Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T16:47:29.902718+00:00\"}]}}, \"exp_030c_tcn_cheetah_s0_sigma10\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:26:11.800Z\", \"updated_at\": \"2026-05-20T16:26:18.487Z\", \"hypothesis\": \"Cheetah CIVO intensity (NVE 8-108×) requires proportionally higher TCN noise; σ=1.0 may match Cheetah's CIVO severity as σ=0.2 matched Walker's. Based on exp_030a (σ=0.2 negative, NVE=1.903) and exp_030b (σ=0.5 negative, NVE=10.67).\", \"parent\": \"exp_030b_tcn_cheetah_s0_sigma05\"}, \"exp_031_tcn_pickcube_s0_sigma02\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:09:56.923Z\", \"updated_at\": \"2026-05-20T16:20:39.337Z\", \"hypothesis\": \"TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination rollout will suppress CIVO in ManiSkill PickCube-v1, as it did in Walker Walk, by preventing the world model from overfitting to fixed dt signals.\", \"parent\": \"exp_019b_pickcube_civo_trigger\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\"\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"pid\": \"908459\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\", \"submitted_at\": \"2026-05-20T12:42:41.707Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"maniskill_PickCube-v1\", \"data_count\": \"200000(online)\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"checkpoint_source\": \"none(train_from_scratch)\", \"eval_data\": \"maniskill_PickCube-v1(online_eval)\"}, \"metrics\": {\"eval_return_2.5K\": 2.4, \"eval_return_12.5K\": 19.2, \"eval_return_22.5K\": 17.7, \"eval_return_32.5K\": 11.5, \"eval_return_42.5K\": 7.8, \"eval_return_52.5K\": 4.8, \"eval_return_62.5K\": 10.4, \"ve_ratio_12.5K\": 0.1989, \"ve_ratio_22.5K\": 1.0128, \"ve_ratio_32.5K\": 2.2946, \"ve_ratio_42.5K\": 3.0555, \"ve_ratio_52.5K\": 3.7109, \"ve_ratio_62.5K\": 1.1999, \"nve_max\": 3.7109, \"nve_max_step\": \"52.5K\", \"current_step\": 62500, \"target_steps\": 200000}}, \"exp_030b_tcn_cheetah_s0_sigma05\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:07:53.975Z\", \"updated_at\": \"2026-05-20T16:20:36.095Z\", \"hypothesis\": \"Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the environment-appropriate dose (Walker σ=0.5 = overdose causing oscillatory CIVO, Cheetah σ=0.2 = underdose with NVE 1.903@55K). Tests whether TCN effectiveness is environment-dependent with σ scaling to CIVO severity. If NVE<1.5× and eval maintained → TCN is generalizable with environment-tuned σ.\", \"parent\": \"\", \"spec\": {\"gpu\": \"cuda:0\"}, \"metrics\": {\"eval_return_5K\": 8.3, \"eval_return_15K\": 78.3, \"eval_return_25K\": 219.3, \"eval_return_35K\": 296.5, \"eval_return_45K\": 32.8, \"eval_return_55K\": 6, \"eval_return_65K\": 71.2, \"eval_return_75K\": 23.3, \"eval_return_85K\": 34, \"eval_return_95K\": 143.6, \"eval_return_105K\": 104.4, \"eval_return_115K\": 137.7, \"eval_return_125K\": 211.7, \"eval_return_135K\": 97.2, \"eval_return_145K\": 79.4, \"eval_return_155K\": 76.8, \"eval_return_165K\": 77.5, \"eval_return_175K\": 85.7, \"eval_return_185K\": 68.7, \"eval_return_195K\": 77.6, \"ve_ratio_15K\": 0.0202, \"ve_ratio_25K\": 0.0636, \"ve_ratio_35K\": 0.1238, \"ve_ratio_45K\": 1.9141, \"ve_ratio_55K\": 10.6657, \"ve_ratio_65K\": 0.8371, \"ve_ratio_75K\": 1.9823, \"ve_ratio_85K\": 1.0946, \"ve_ratio_95K\": 0.2253, \"ve_ratio_105K\": 0.2686, \"ve_ratio_115K\": 0.1789, \"ve_ratio_125K\": 0.1037, \"ve_ratio_135K\": 0.2153, \"ve_ratio_145K\": 0.2478, \"ve_ratio_155K\": 0.2392, \"ve_ratio_165K\": 0.202, \"ve_ratio_175K\": 0.1591, \"ve_ratio_185K\": 0.1834, \"ve_ratio_195K\": 0.1534, \"nve_max\": 10.6657, \"nve_max_step\": \"55K\", \"nve_final\": 0.1534, \"current_step\": 195000, \"target_steps\": 210000}}, \"exp_029c_tcn_walker_s0_sigma01\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:09:50.913Z\", \"updated_at\": \"2026-05-20T16:20:28.451Z\", \"hypothesis\": \"σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2 prevents CIVO and σ=0.1 does not, establishes minimum effective dose. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8). Three-point dose-response: σ=0.1 (this), σ=0.2 (success), σ=0.5 (oscillatory failure).\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\"\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:0\"], \"pid\": \"59395\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\", \"submitted_at\": \"2026-05-20T11:42:56.447Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 0, \"model_name\": \"dreamer\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dmc_walker_walk\"}, \"metrics\": {\"eval_return_5K\": 35.6, \"eval_return_15K\": 99.1, \"eval_return_25K\": 140.7, \"eval_return_35K\": 155.7, \"eval_return_45K\": 160.9, \"eval_return_55K\": 254.8, \"eval_return_65K\": 268.7, \"eval_return_75K\": 295.5, \"eval_return_85K\": 220.8, \"eval_return_95K\": 188.6, \"eval_return_105K\": 204.7, \"eval_return_115K\": 296.4, \"eval_return_125K\": 232.3, \"eval_return_135K\": 247.4, \"ve_ratio_15K\": 0.0306, \"ve_ratio_25K\": 0.1606, \"ve_ratio_35K\": 0.3162, \"ve_ratio_45K\": 0.4807, \"ve_ratio_55K\": 0.4368, \"ve_ratio_65K\": 0.5432, \"ve_ratio_75K\": 0.6211, \"ve_ratio_85K\": 0.9533, \"ve_ratio_95K\": 1.0218, \"ve_ratio_105K\": 0.761, \"ve_ratio_115K\": 0.4514, \"ve_ratio_125K\": 0.4899, \"ve_ratio_135K\": 0.3995, \"nve_max\": 1.0218, \"nve_max_step\": \"95K\", \"current_step\": 135000, \"target_steps\": 210000}}, \"exp_027_tcn_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:51:53.479Z\", \"updated_at\": \"2026-05-20T12:45:31.028Z\", \"hypothesis\": \"TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different seed to verify that the NVE self-correction phenomenon (transient CIVO at 55K → NVE recovery to 0.83 by 75K) is reproducible across seeds, not a stochastic artifact. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.5.\", \"parent\": \"exp_027_tcn_walker_s0\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\"}, \"metrics\": {\"total_steps\": 215000, \"eval_return\": {\"5000\": 31, \"15000\": 140.5, \"25000\": 163.6, \"35000\": 153, \"45000\": 136.8, \"55000\": 158.3, \"65000\": 298.5, \"75000\": 364.9, \"85000\": 134, \"95000\": 94.6, \"105000\": 216.7, \"115000\": 318.9, \"125000\": 309.1, \"135000\": 216.1, \"145000\": 175.4, \"155000\": 171, \"165000\": 209.5, \"175000\": 120.4, \"185000\": 355.4, \"195000\": 183.3, \"205000\": 240.2, \"215000\": 350.8}, \"ve_ratio\": {\"15000\": 0.0246, \"25000\": 0.1416, \"35000\": 0.3585, \"45000\": 0.6101, \"55000\": 0.7092, \"65000\": 0.4875, \"75000\": 0.4902, \"85000\": 1.4104, \"95000\": 1.6367, \"105000\": 0.6444, \"115000\": 0.4021, \"125000\": 0.38, \"135000\": 0.5078, \"145000\": 0.8469, \"155000\": 0.8568, \"165000\": 0.5393, \"175000\": 0.7355, \"185000\": 0.211, \"195000\": 0.3513, \"205000\": 0.2376, \"215000\": 0.1476}, \"eval_peak\": 364.9, \"eval_peak_step\": 75000, \"eval_last10_mean\": 233.1, \"nve_max\": 1.6367, \"nve_max_step\": 95000, \"nve_final\": 0.1476}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:35:38.092Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:35:42.576855+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T12:38:02.085Z\"}, \"exp_027_tcn_walker_s0_sigma02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:25:32.533Z\", \"updated_at\": \"2026-05-20T12:06:21.855Z\", \"hypothesis\": \"TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding during imagination) but with σ=0.2 instead of 0.5. Tests whether smaller noise magnitude is sufficient to disrupt dt-specific value bias. If σ=0.5 works but σ=0.2 doesn't → noise magnitude matters; if both work → method is robust to σ choice.\", \"parent\": \"exp_027_tcn_walker_s0\", \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:0\", \"seed\": 0, \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\", \"model_name\": \"dreamerv3\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 215000}, \"metrics\": {\"eval_return_5K\": 35.6, \"eval_return_15K\": 150.6, \"eval_return_25K\": 199.4, \"eval_return_35K\": 278.2, \"eval_return_45K\": 315.6, \"eval_return_55K\": 278.6, \"eval_return_65K\": 331, \"eval_return_75K\": 293.1, \"eval_return_85K\": 363.9, \"eval_return_95K\": 171.4, \"eval_return_105K\": 236.4, \"eval_return_115K\": 543.8, \"eval_return_125K\": 458.4, \"eval_return_135K\": 496.7, \"eval_return_145K\": 542.7, \"eval_return_155K\": 660.5, \"eval_return_165K\": 653.3, \"eval_return_175K\": 821.1, \"eval_return_185K\": 560.5, \"eval_return_195K\": 567.9, \"eval_return_205K\": 558.7, \"eval_return_215K\": 551, \"ve_ratio_15K\": 0.0192, \"ve_ratio_25K\": 0.0961, \"ve_ratio_35K\": 0.1875, \"ve_ratio_45K\": 0.3009, \"ve_ratio_55K\": 0.5231, \"ve_ratio_65K\": 0.5654, \"ve_ratio_75K\": 0.611, \"ve_ratio_85K\": 0.4665, \"ve_ratio_95K\": 0.9081, \"ve_ratio_105K\": 0.5625, \"ve_ratio_115K\": 0.2105, \"ve_ratio_125K\": 0.2182, \"ve_ratio_135K\": 0.1764, \"ve_ratio_145K\": 0.143, \"ve_ratio_155K\": 0.106, \"ve_ratio_165K\": 0.0979, \"ve_ratio_175K\": 0.0729, \"ve_ratio_185K\": 0.1048, \"ve_ratio_195K\": 0.1026, \"ve_ratio_205K\": 0.0995, \"ve_ratio_215K\": 0.0955, \"eval_peak\": 821.1, \"eval_peak_step\": \"175K\", \"eval_last10_mean\": 587.1, \"nve_max\": 0.9081, \"nve_max_step\": \"95K\", \"nve_final\": 0.0955, \"total_steps\": 215000}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T11:19:31.331Z\"}, \"exp_030a_tcn_cheetah_s0_sigma02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:24:38.711Z\", \"updated_at\": \"2026-05-20T11:10:00.827Z\", \"hypothesis\": \"TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether CIVO suppression generalizes beyond Walker Walk. Cheetah exhibits stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) + TCN σ=0.2. If NVE<1.5× and eval maintained → TCN is environment-agnostic intervention.\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": \"210000 env steps\", \"model_name\": \"dreamerv3_tcn_sigma02_cheetah\", \"seed\": 0, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"dmc_cheetah_run\", \"checkpoint_path\": \"logdir/exp_030a_tcn_cheetah_s0_sigma02/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\"}, \"metrics\": {\"eval_return_35K\": 299.5, \"eval_return_55K\": 31.9, \"ve_ratio_55K\": 1.903, \"current_step\": 64000, \"target_steps\": 210000, \"note\": \"WARNING: NVE breached 1.5× at 55K (1.903), eval crashed 299→32. Possible CIVO despite TCN.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T11:10:00.827Z\"}, \"exp_027_tcn_walker_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:44:51.820Z\", \"updated_at\": \"2026-05-20T09:24:09.016Z\", \"hypothesis\": \"Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5) to dt_embedding during imagination rollouts reduces dt conditioning precision, preventing critic from learning dt-specific value bias. Predicts CIVO suppression (NVE < 1.5×) with eval > 50% baseline (~450+). Based on obs-decoder SGS failure (gradient-level intervention insufficient) → need forward-pass/representation-level intervention.\", \"parent\": \"exp_025_obs_sgs_walker_s1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"888715\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"submitted_at\": \"2026-05-20T06:13:35.505Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11433.5, \"gpu_hours\": 3.18}, \"metrics\": {\"eval_return_5K\": 37.4, \"eval_return_15K\": 154.6, \"eval_return_25K\": 223.6, \"eval_return_35K\": 240, \"eval_return_45K\": 101.2, \"eval_return_55K\": 70, \"eval_return_65K\": 95.1, \"eval_return_75K\": 189.2, \"eval_return_85K\": 36, \"eval_return_95K\": 166.4, \"eval_return_105K\": 95.5, \"eval_return_112K\": 99.5, \"ve_ratio_15K\": 0.02, \"ve_ratio_25K\": 0.11, \"ve_ratio_35K\": 0.235, \"ve_ratio_45K\": 0.86, \"ve_ratio_55K\": 1.679, \"ve_ratio_65K\": 1.544, \"ve_ratio_75K\": 0.831, \"ve_ratio_85K\": 3.965, \"ve_ratio_95K\": 0.675, \"ve_ratio_105K\": 0.916, \"peak_eval\": 240, \"peak_eval_step\": \"35K\", \"peak_nve\": 3.965, \"peak_nve_step\": \"85K\", \"last_5_eval_avg\": 117.3, \"nve_breach_count\": 3, \"nve_breach_steps\": \"55K(1.68), 65K(1.54), 85K(3.97)\", \"final_step\": 120000, \"target_steps\": 210000, \"gate_dt_mean\": 2, \"gate_dt_entropy\": 0}, \"reproduce\": {\"finished_at\": \"2026-05-20T06:06:30.806Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T06:06:34.898602+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s0/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"analysis_summary\": \"TCN (σ=0.5 noise on dt_embedding) FAILED to suppress CIVO. NVE breached 1.5× threshold 3 times: 55K(1.68×), 65K(1.54×), 85K(3.97×). Peak NVE 3.97× at 85K is HIGHER than typical CIVO, suggesting TCN destabilizes value learning. Eval peaked at 240 (35K), then collapsed to avg 117 in latter half — far below 450 target. Gate remained fixed at dt=2 throughout (zero entropy). The noise magnitude was insufficient to decorrelate critic estimates from dt conditioning. Training reached 120K/210K planned. Hypothesis falsified: forward-pass noise at σ=0.5 does not prevent critic from exploiting dt-specific value structure.\", \"completed_at\": \"2026-05-20T09:24:09.016Z\"}, \"exp_028_rave_walker_s0_ceil15\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:25:34.045Z\", \"updated_at\": \"2026-05-20T08:31:12.389Z\", \"hypothesis\": \"RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value cap) but with ceiling=1.5 instead of 2.0. Tighter constraint tests whether more aggressive capping improves CIVO suppression without harming learning. If ceiling=2.0 works and 1.5 also works → method robust; if 1.5 hurts eval → ceiling choice is critical.\", \"parent\": \"exp_028_rave_walker_s0\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:1\"], \"pid\": \"38372\", \"tmux_session\": \"exp_028_rave_walker_s0_ceil15\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"210000 env steps\", \"model_name\": \"dreamerv3_rave_ceil15\", \"seed\": 0, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\", \"checkpoint_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\", \"checkpoint_source\": \"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"note\": \"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\"}, \"metrics\": {\"eval_return_5K\": 31.6, \"eval_return_15K\": 99.4, \"eval_return_25K\": 155.3, \"eval_return_35K\": 180.1, \"eval_return_45K\": 166.9, \"eval_return_55K\": 131, \"eval_return_65K\": 91.5, \"eval_return_75K\": 120.9, \"eval_return_85K\": 137.3, \"eval_return_95K\": 70.2, \"eval_return_105K\": 76.2, \"eval_return_115K\": 41.2, \"eval_return_125K\": 36.6, \"eval_return_135K\": 39.1, \"ve_ratio_15K\": 0.03, \"ve_ratio_25K\": 0.128, \"ve_ratio_35K\": 0.247, \"ve_ratio_45K\": 0.428, \"ve_ratio_55K\": 0.737, \"ve_ratio_65K\": 1.294, \"ve_ratio_75K\": 0.937, \"ve_ratio_85K\": 0.727, \"ve_ratio_95K\": 1.28, \"ve_ratio_105K\": 0.984, \"ve_ratio_115K\": 1.513, \"ve_ratio_125K\": 1.462, \"ve_ratio_135K\": 1.171, \"current_step\": 135000, \"target_steps\": 210000}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T08:31:12.389Z\"}, \"exp_028_rave_walker_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:44:53.882Z\", \"updated_at\": \"2026-05-20T06:14:31.720Z\", \"hypothesis\": \"Reality-Anchored Value Estimation (RAVE): cap imagination critic values at ceiling*v_anchor (ceiling=2.0, v_anchor=EMA of real-state critic values). Directly prevents pathological value inflation (NVE>1.5×) by bounding imagination/reality value ratio. Based on CIVO core mechanism being imagination value explosion → this directly caps the ratio without modifying gradients or training dynamics.\", \"parent\": \"exp_025_obs_sgs_walker_s1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"879636\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\", \"submitted_at\": \"2026-05-20T02:54:26.022Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"105000 env steps (52.5K agent steps, action_repeat=2)\", \"model_name\": \"dreamerv3_rave_ceil20\", \"seed\": 0, \"checkpoint_source\": \"N/A (trained from scratch, derives from SGS failure line)\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"wall_clock_seconds\": 12005.7, \"gpu_hours\": 3.33}, \"metrics\": {\"current_steps\": 105000, \"eval_trajectory\": {\"5K\": {\"eval_return\": 37.4, \"value_mean\": 0.001}, \"15K\": {\"eval_return\": 105.3, \"ve_ratio\": 0.028, \"value_mean\": 2.93}, \"25K\": {\"eval_return\": 191.9, \"ve_ratio\": 0.127, \"value_mean\": 24.4}, \"35K\": {\"eval_return\": 204.6, \"ve_ratio\": 0.267}, \"45K\": {\"eval_return\": 197.7, \"ve_ratio\": 0.439}, \"55K\": {\"eval_return\": 193, \"ve_ratio\": 0.62}, \"65K\": {\"eval_return\": 79.8, \"ve_ratio\": 1.832}, \"75K\": {\"eval_return\": 44.5, \"ve_ratio\": 3.415}, \"85K\": {\"eval_return\": 57.7, \"ve_ratio\": 2.126}, \"95K\": {\"eval_return\": 25.9, \"ve_ratio\": 4.086, \"value_mean\": 105.87}, \"105K\": {\"eval_return\": 29, \"ve_ratio\": 3.183, \"value_mean\": 92.2}}, \"note\": \"NEGATIVE. NVE diverged from 55K onward (0.62→4.09), eval collapsed 193→29. No self-correction.\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/checkpoint.ckpt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/\", \"completed_at\": \"2026-05-20T06:14:31.720Z\"}, \"exp_025_obs_sgs_walker_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:39:26.941Z\", \"updated_at\": \"2026-05-20T03:17:26.061Z\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:1\"], \"pid\": \"7989\", \"tmux_session\": \"exp_025_s2\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"210000 env steps (105K agent steps)\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"seed\": 2, \"log_path\": \"logdir/exp_025_obs_sgs_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s2/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval during training)\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T03:14:07.466Z\"}, \"failure_reason\": \"Reclassified: experiment completed 224K/210K steps normally. Cron misclassified as failed due to missing W&B sentinel. Actual result is negative — obs-decoder SGS suppressed CIVO (ve_ratio 0.8-1.4) but eval collapsed to ~90 (baseline ~930).\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T03:14:06.591Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T03:14:13.011509+00:00\"}]}, \"metrics\": {\"eval_return_215K\": 89.6, \"ve_ratio_215K\": 0.8, \"ve_ratio_185K\": 1.4, \"ve_ratio_175K\": 1.2, \"train_steps_completed\": 224000, \"target_steps\": 210000}, \"notes\": \"Obs-decoder SGS s2 完成全部训练（224K/210K steps）。ve_ratio 全程 0.8-1.4（CIVO 部分抑制），但 eval_return 仅 66-90（baseline ~930，远低于 70% 阈值 ~650）。与 s1/s3/s4 一致：obs-decoder SGS 无法在抑制 CIVO 的同时保持性能。梯度干预路线全面否定（Full SGS 0/3 + Obs-decoder SGS 0/6 有效）。\"}, \"exp_026_obs_sgs_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T20:19:29.171Z\", \"updated_at\": \"2026-05-20T03:02:46.556Z\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:1\"], \"pid\": \"16346\", \"tmux_session\": \"exp_026_s1\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": \"105000 env steps\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"seed\": 1, \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/train.log\", \"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:46.556Z\"}, \"exp_026_obs_sgs_cheetah_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T20:19:27.608Z\", \"updated_at\": \"2026-05-20T03:02:43.170Z\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:0\"], \"pid\": \"16208\", \"tmux_session\": \"exp_026_s0\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": \"105000 env steps\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"seed\": 0, \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/train.log\", \"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:43.170Z\"}, \"exp_025_obs_sgs_walker_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:39:29.810Z\", \"updated_at\": \"2026-05-20T03:02:39.948Z\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"851593\", \"tmux_session\": \"exp_025_s4\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"210000 env steps (105K agent steps)\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"seed\": 4, \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/train.log\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval during training)\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:39.948Z\"}, \"exp_025_obs_sgs_walker_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:39:28.402Z\", \"updated_at\": \"2026-05-20T03:02:36.670Z\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"847597\", \"tmux_session\": \"exp_025_s3\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"210000 env steps (105K agent steps)\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"seed\": 3, \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/train.log\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval during training)\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:36.670Z\"}, \"exp_025_obs_sgs_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:39:25.583Z\", \"updated_at\": \"2026-05-20T03:02:32.583Z\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:0\"], \"pid\": \"7833\", \"tmux_session\": \"exp_025_s1\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"210000 env steps (105K agent steps)\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"seed\": 1, \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval during training)\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:32.583Z\"}, \"exp_001_baseline_s4_extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:02:31.737Z\", \"updated_at\": \"2026-05-19T23:06:42.122Z\", \"hypothesis\": \"Walker Walk baseline seed=4 extended to 505K. Third long-run baseline seed for multi-seed NVE normalization. s4@105K=922.8 (highest), obtaining full ve_ratio profile.\", \"parent\": \"exp_001_baseline_s4\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"tmux_session\": \"exp_s4_ext\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"505000 env steps\", \"model_name\": \"dreamerv3_baseline\", \"seed\": 4, \"resumed_from_step\": 112000, \"target_steps\": 505000, \"checkpoint_source\": \"logdir/exp_001_baseline_s4/latest.pt\", \"checkpoint_path\": \"logdir/exp_001_baseline_s4/\", \"log_path\": \"logdir/exp_001_baseline_s4/train_extended.log\", \"eval_data\": \"dmc_walker_walk (online eval during training)\"}, \"conclusion\": \"success\", \"metrics\": {\"final_step\": 520000, \"final_eval_return\": 938.86, \"peak_eval_return\": 960.6, \"convergence_mean_250k_plus\": 935}, \"completed_at\": \"2026-05-19T23:06:42.122Z\"}, \"exp_001_baseline_s3_extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:02:30.382Z\", \"updated_at\": \"2026-05-19T21:23:44.025Z\", \"hypothesis\": \"Walker Walk baseline seed=3 extended to 505K. Second long-run baseline seed (alongside s2_ext) for multi-seed NVE normalization robustness. s3@105K=869.0, testing convergence to 920+ level.\", \"parent\": \"exp_001_baseline_s3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"tmux_session\": \"exp_s3_ext\", \"data_path\": \"dmc_walker_walk\", \"data_count\": \"505000 env steps\", \"model_name\": \"dreamerv3_baseline\", \"seed\": 3, \"resumed_from_step\": 120000, \"target_steps\": 505000, \"checkpoint_source\": \"logdir/exp_001_baseline_s3/latest.pt\", \"checkpoint_path\": \"logdir/exp_001_baseline_s3/\", \"log_path\": \"logdir/exp_001_baseline_s3/train_extended.log\", \"eval_data\": \"dmc_walker_walk (online eval during training)\"}, \"conclusion\": \"success\", \"metrics\": {\"final_step\": 520000, \"final_eval_return\": 947.68, \"final_train_return_avg\": 945.4, \"eval_profile\": {\"5000\": 42.15, \"15000\": 224.27, \"25000\": 329.99, \"35000\": 413.12, \"45000\": 332.69, \"55000\": 519.91, \"65000\": 667.42, \"72000\": 771.33, \"82000\": 772.88, \"92000\": 854.6, \"102000\": 869.03, \"112000\": 898.89, \"120000\": 898.38, \"130000\": 837.74, \"140000\": 876.64, \"150000\": 899.47, \"160000\": 922.77, \"170000\": 925.77, \"180000\": 912.89, \"190000\": 915.07, \"200000\": 894.77, \"210000\": 899.79, \"220000\": 951.18, \"230000\": 930.56, \"240000\": 910.47, \"250000\": 914.02, \"260000\": 931.33, \"270000\": 954.65, \"280000\": 928.01, \"290000\": 947.4, \"300000\": 853.32, \"310000\": 906.35, \"320000\": 847.16, \"330000\": 934.78, \"340000\": 921.08, \"350000\": 922.63, \"360000\": 844.99, \"370000\": 911.36, \"380000\": 917.73, \"390000\": 937.21, \"400000\": 928, \"410000\": 945.88, \"420000\": 897.2, \"430000\": 949.45, \"440000\": 937.28, \"450000\": 924.24, \"460000\": 967.25, \"470000\": 940.55, \"480000\": 936.24, \"490000\": 944.67, \"500000\": 957.09, \"510000\": 947.68}}, \"completed_at\": \"2026-05-19T21:23:44.025Z\"}, \"exp_001_baseline_s2_extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:10:10.948Z\", \"updated_at\": \"2026-05-19T17:44:27.212Z\", \"hypothesis\": \"Walker Walk baseline seed=2 extended to 505K. Tests whether low eval (443.5 @105K) is due to slow convergence or seed-level difference. s1=915.7, s3=869.0 at 105K.\", \"parent\": \"exp_001_baseline_s2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 2 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s2\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"tmux_session\": \"exp_s2_ext\", \"seed\": 2, \"model_name\": \"dreamerv3\", \"data_path\": \"logdir/exp_001_baseline_s2\", \"data_count\": 0, \"checkpoint_source\": \"logdir/exp_001_baseline_s2/latest.pt\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"resumed_from_step\": 112000, \"target_steps\": 505000, \"checkpoint_path\": \"logdir/exp_001_baseline_s2/latest.pt\", \"log_path\": \"logdir/exp_001_baseline_s2/train_extended.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 945.7, \"eval_return_peak\": 962.6, \"eval_return_at_105K\": 443.5, \"ve_ratio_at_105K\": 0.7422, \"value_mean_at_105K\": 329.16, \"ve_ratio_converged_range\": \"0.69-0.77\", \"value_mean_plateau\": 665, \"total_steps\": 512000}, \"completed_at\": \"2026-05-19T17:44:27.212Z\"}}, \"count\": 20, \"total\": 100, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4166}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me summarize what I found:

1. **PID 50924**: EXITED (ps returned exit code 1, meaning process not found)
2. **Logs**: No log file with "029a" in the name under `/root/runs/event-gated-adaptive-horizon/`. The logs found are for exp_027, exp_028, and exp_029c.
3. **Checkpoint**: Found at `/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt`
4. **Registry**: exp_029a_tcn_walker_s1_sigma02 already exists and is already marked as DONE with conclusion=success!


5. **Registry details**: The experiment shows status DONE with conclusion success, checkpoint and log paths already set, and completed at 2026-05-20T16:47:18.789Z. There's a discrepancy where the failure_reason mentions "process dead 5× with no sentinel/W&B — auto-resolved as failed" but the conclusion is success, suggesting it was updated after auto-resolution. I should verify the log shows a clean exit before proceeding to delete.

6. **Log verification**: I need to check the metrics.jsonl file at `/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/metrics.jsonl` to confirm the process exited cleanly, though I'm not finding a matching .log file for 029a yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "de4ea8fa-73bc-400b-a286-7037c14a10e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNwC7J2C2LsyqSiBd31qa1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19391,
      "cache_read_input_tokens": 25898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19391
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

_source line 29_

PID 50924 已退出。Checkpoint 找到：`/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt`。Registry 中 exp_029a 已标记 DONE/success，checkpoint_path 和 log_path 已设置。

检查日志确认退出状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "3c9955b4-15c9-42ef-97b4-da16c0175c5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNwC7J2C2LsyqSiBd31qa1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19391,
      "cache_read_input_tokens": 25898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19391
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BYtLM3LzzvXJgpnxCtWaao`</summary>

```json
{
  "server": "bjb1-40020",
  "command": "ls /root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/",
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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "32d178fa-8fb4-4b5e-be41-60657f1019d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNwC7J2C2LsyqSiBd31qa1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19391,
      "cache_read_input_tokens": 25898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19391
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

_source line 31 · 2026-05-20T16:48:52.512Z_

<details><summary>↩ Tool result · `toolu_01BYtLM3LzzvXJgpnxCtWaao`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_eps\\nevents.out.tfevents.1779265965.autodl-container-2e984fa248-568e58ca.50924.0\\nlatest.pt\\nmetrics.jsonl\\ntrain_eps\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "0158265c-17e0-4880-be53-f0a42826d7d4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_eps\\\\nevents.out.tfevents.1779265965.autodl-container-2e984fa248-568e58ca.50924.0\\\\nlatest.pt\\\\nmetrics.jsonl\\\\ntrain_eps\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_eps\\nevents.out.tfevents.1779265965.autodl-container-2e984fa248-568e58ca.50924.0\\nlatest.pt\\nmetrics.jsonl\\ntrain_eps\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KWmQDft3W6uCvS5aikYhni`</summary>

```json
{
  "server": "bjb1-40020",
  "command": "tail -20 /root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/metrics.jsonl",
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
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "8b315a3b-08cc-493d-a8b2-14849b1a0715",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNwC7J2C2LsyqSiBd31qa1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19391,
      "cache_read_input_tokens": 25898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19391
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

_source line 33 · 2026-05-20T16:48:53.337Z_

<details><summary>↩ Tool result · `toolu_01KWmQDft3W6uCvS5aikYhni`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 208000, \\\"dataset_size\\\": 104000.0, \\\"train_return\\\": 235.7844696044922, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 208.0}\\n{\\\"step\\\": 212000, \\\"dataset_size\\\": 106000.0, \\\"train_return\\\": 202.37445068359375, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 212.0}\\n{\\\"step\\\": 212000, \\\"dataset_size\\\": 106000.0, \\\"train_return\\\": 187.92965698242188, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 212.0}\\n{\\\"step\\\": 212000, \\\"dataset_size\\\": 106000.0, \\\"train_return\\\": 221.29074096679688, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 212.0}\\n{\\\"step\\\": 212000, \\\"dataset_size\\\": 106000.0, \\\"train_return\\\": 177.21722412109375, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 212.0}\\n{\\\"step\\\": 215000}\\n{\\\"step\\\": 215000, \\\"eval_return\\\": 161.29613189697267, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 215000, \\\"civo/ve_ratio\\\": 0.18638920647786983, \\\"civo/delta_ve\\\": 0.03609233506818024, \\\"civo/alert\\\": 0.0, \\\"model_loss\\\": 5.0361433029174805, \\\"model_grad_norm\\\": 6.7952117919921875, \\\"height_loss\\\": 0.0008423591498285532, \\\"orientations_loss\\\": 0.08522764593362808, \\\"velocity_loss\\\": 0.6637676954269409, \\\"reward_loss\\\": 0.5471906065940857, \\\"cont_loss\\\": 1.3152444411357322e-11, \\\"kl_free\\\": 1.0, \\\"dyn_scale\\\": 0.5, \\\"rep_scale\\\": 0.09999999999999999, \\\"dyn_loss\\\": 6.231858730316162, \\\"rep_loss\\\": 6.231858730316162, \\\"kl\\\": 6.0892558097839355, \\\"prior_ent\\\": 39.70130157470703, \\\"post_ent\\\": 33.5832633972168, \\\"normed_target_mean\\\": 0.3667752146720886, \\\"normed_target_std\\\": 0.33563467860221863, \\\"normed_target_min\\\": -0.0027024284936487675, \\\"normed_target_max\\\": 1.3731828927993774, \\\"EMA_005\\\": 6.1768269538879395, \\\"EMA_095\\\": 71.7769775390625, \\\"value_mean\\\": 30.065412521362305, \\\"value_std\\\": 21.7001895904541, \\\"value_min\\\": 6.19986629486084, \\\"value_max\\\": 93.3718032836914, \\\"target_mean\\\": 30.239381790161133, \\\"target_std\\\": 22.016340255737305, \\\"target_min\\\": 5.9993510246276855, \\\"target_max\\\": 96.25286102294922, \\\"imag_reward_mean\\\": 0.8545054793357849, \\\"imag_reward_std\\\": 1.1082724332809448, \\\"imag_reward_min\\\": -1.2769699253567524e-07, \\\"imag_reward_max\\\": 4.069231033325195, \\\"imag_action_mean\\\": 0.05791507661342621, \\\"imag_action_std\\\": 0.7327951192855835, \\\"imag_action_min\\\": -1.0, \\\"imag_action_max\\\": 1.0, \\\"actor_entropy\\\": -2.7363696098327637, \\\"gate_dt_mean\\\": 2.0, \\\"gate_dt_std\\\": 0.0, \\\"gate_dt_min\\\": 2.0, \\\"gate_dt_max\\\": 2.0, \\\"gate_dt_1_frac\\\": 0.0, \\\"gate_dt_2_frac\\\": 1.0, \\\"gate_dt_3_frac\\\": 0.0, \\\"gate_dt_4_frac\\\": 0.0, \\\"gate_dt_5_frac\\\": 0.0, \\\"gate_dt_6_frac\\\": 0.0, \\\"gate_dt_7_frac\\\": 0.0, \\\"gate_dt_8_frac\\\": 0.0, \\\"gate_empirical_entropy\\\": 0.0, \\\"gate_entropy_ratio\\\": 0.0, \\\"gate_dt_autocorr\\\": 0.0, \\\"actor_loss\\\": -0.0017599775455892086, \\\"actor_grad_norm\\\": 0.09420984238386154, \\\"value_loss\\\": 1.7037900686264038, \\\"value_grad_norm\\\": 1.1889382600784302, \\\"update_count\\\": 52599.0, \\\"fps\\\": 7.3352344898245}\\n{\\\"step\\\": 216000, \\\"dataset_size\\\": 108000.0, \\\"train_return\\\": 85.15019226074219, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 216.0}\\n{\\\"step\\\": 216000, \\\"dataset_size\\\": 108000.0, \\\"train_return\\\": 190.03192138671875, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 216.0}\\n{\\\"step\\\": 216000, \\\"dataset_size\\\": 108000.0, \\\"train_return\\\": 276.46295166015625, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 216.0}\\n{\\\"step\\\": 216000, \\\"dataset_size\\\": 108000.0, \\\"train_return\\\": 215.5836181640625, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 216.0}\\n{\\\"step\\\": 220000, \\\"dataset_size\\\": 110000.0, \\\"train_return\\\": 214.92422485351562, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 220.0}\\n{\\\"step\\\": 220000, \\\"dataset_size\\\": 110000.0, \\\"train_return\\\": 244.76931762695312, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 220.0}\\n{\\\"step\\\": 220000, \\\"dataset_size\\\": 110000.0, \\\"train_return\\\": 211.2147216796875, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 220.0}\\n{\\\"step\\\": 220000, \\\"dataset_size\\\": 110000.0, \\\"train_return\\\": 212.54171752929688, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 220.0}\\n{\\\"step\\\": 224000, \\\"dataset_size\\\": 112000.0, \\\"train_return\\\": 200.2361297607422, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 224.0}\\n{\\\"step\\\": 224000, \\\"dataset_size\\\": 112000.0, \\\"train_return\\\": 187.08714294433594, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 224.0}\\n{\\\"step\\\": 224000, \\\"dataset_size\\\": 112000.0, \\\"train_return\\\": 192.78289794921875, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 224.0}\\n{\\\"step\\\": 224000, \\\"dataset_size\\\": 112000.0, \\\"train_return\\\": 247.33250427246094, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 224.0}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "c6ca4596-31b9-4776-a11c-ad41deaff2e0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\\\\"step\\\\\\\": 208000, \\\\\\\"dataset_size\\\\\\\": 104000.0, \\\\\\\"train_return\\\\\\\": 235.7844696044922, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 208.0}\\\\n{\\\\\\\"step\\\\\\\": 212000, \\\\\\\"dataset_size\\\\\\\": 106000.0, \\\\\\\"train_return\\\\\\\": 202.37445068359375, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 212.0}\\\\n{\\\\\\\"step\\\\\\\": 212000, \\\\\\\"dataset_size\\\\\\\": 106000.0, \\\\\\\"train_return\\\\\\\": 187.92965698242188, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 212.0}\\\\n{\\\\\\\"step\\\\\\\": 212000, \\\\\\\"dataset_size\\\\\\\": 106000.0, \\\\\\\"train_return\\\\\\\": 221.29074096679688, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 212.0}\\\\n{\\\\\\\"step\\\\\\\": 212000, \\\\\\\"dataset_size\\\\\\\": 106000.0, \\\\\\\"train_return\\\\\\\": 177.21722412109375, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 212.0}\\\\n{\\\\\\\"step\\\\\\\": 215000}\\\\n{\\\\\\\"step\\\\\\\": 215000, \\\\\\\"eval_return\\\\\\\": 161.29613189697267, \\\\\\\"eval_length\\\\\\\": 500.0, \\\\\\\"eval_episodes\\\\\\\": 10.0}\\\\n{\\\\\\\"step\\\\\\\": 215000, \\\\\\\"civo/ve_ratio\\\\\\\": 0.18638920647786983, \\\\\\\"civo/delta_ve\\\\\\\": 0.03609233506818024, \\\\\\\"civo/alert\\\\\\\": 0.0, \\\\\\\"model_loss\\\\\\\": 5.0361433029174805, \\\\\\\"model_grad_norm\\\\\\\": 6.7952117919921875, \\\\\\\"height_loss\\\\\\\": 0.0008423591498285532, \\\\\\\"orientations_loss\\\\\\\": 0.08522764593362808, \\\\\\\"velocity_loss\\\\\\\": 0.6637676954269409, \\\\\\\"reward_loss\\\\\\\": 0.5471906065940857, \\\\\\\"cont_loss\\\\\\\": 1.3152444411357322e-11, \\\\\\\"kl_free\\\\\\\": 1.0, \\\\\\\"dyn_scale\\\\\\\": 0.5, \\\\\\\"rep_scale\\\\\\\": 0.09999999999999999, \\\\\\\"dyn_loss\\\\\\\": 6.231858730316162, \\\\\\\"rep_loss\\\\\\\": 6.231858730316162, \\\\\\\"kl\\\\\\\": 6.0892558097839355, \\\\\\\"prior_ent\\\\\\\": 39.70130157470703, \\\\\\\"post_ent\\\\\\\": 33.5832633972168, \\\\\\\"normed_target_mean\\\\\\\": 0.3667752146720886, \\\\\\\"normed_target_std\\\\\\\": 0.33563467860221863, \\\\\\\"normed_target_min\\\\\\\": -0.0027024284936487675, \\\\\\\"normed_target_max\\\\\\\": 1.3731828927993774, \\\\\\\"EMA_005\\\\\\\": 6.1768269538879395, \\\\\\\"EMA_095\\\\\\\": 71.7769775390625, \\\\\\\"value_mean\\\\\\\": 30.065412521362305, \\\\\\\"value_std\\\\\\\": 21.7001895904541, \\\\\\\"value_min\\\\\\\": 6.19986629486084, \\\\\\\"value_max\\\\\\\": 93.3718032836914, \\\\\\\"target_mean\\\\\\\": 30.239381790161133, \\\\\\\"target_std\\\\\\\": 22.016340255737305, \\\\\\\"target_min\\\\\\\": 5.9993510246276855, \\\\\\\"target_max\\\\\\\": 96.25286102294922, \\\\\\\"imag_reward_mean\\\\\\\": 0.8545054793357849, \\\\\\\"imag_reward_std\\\\\\\": 1.1082724332809448, \\\\\\\"imag_reward_min\\\\\\\": -1.2769699253567524e-07, \\\\\\\"imag_reward_max\\\\\\\": 4.069231033325195, \\\\\\\"imag_action_mean\\\\\\\": 0.05791507661342621, \\\\\\\"imag_action_std\\\\\\\": 0.7327951192855835, \\\\\\\"imag_action_min\\\\\\\": -1.0, \\\\\\\"imag_action_max\\\\\\\": 1.0, \\\\\\\"actor_entropy\\\\\\\": -2.7363696098327637, \\\\\\\"gate_dt_mean\\\\\\\": 2.0, \\\\\\\"gate_dt_std\\\\\\\": 0.0, \\\\\\\"gate_dt_min\\\\\\\": 2.0, \\\\\\\"gate_dt_max\\\\\\\": 2.0, \\\\\\\"gate_dt_1_frac\\\\\\\": 0.0, \\\\\\\"gate_dt_2_frac\\\\\\\": 1.0, \\\\\\\"gate_dt_3_frac\\\\\\\": 0.0, \\\\\\\"gate_dt_4_frac\\\\\\\": 0.0, \\\\\\\"gate_dt_5_frac\\\\\\\": 0.0, \\\\\\\"gate_dt_6_frac\\\\\\\": 0.0, \\\\\\\"gate_dt_7_frac\\\\\\\": 0.0, \\\\\\\"gate_dt_8_frac\\\\\\\": 0.0, \\\\\\\"gate_empirical_entropy\\\\\\\": 0.0, \\\\\\\"gate_entropy_ratio\\\\\\\": 0.0, \\\\\\\"gate_dt_autocorr\\\\\\\": 0.0, \\\\\\\"actor_loss\\\\\\\": -0.0017599775455892086, \\\\\\\"actor_grad_norm\\\\\\\": 0.09420984238386154, \\\\\\\"value_loss\\\\\\\": 1.7037900686264038, \\\\\\\"value_grad_norm\\\\\\\": 1.1889382600784302, \\\\\\\"update_count\\\\\\\": 52599.0, \\\\\\\"fps\\\\\\\": 7.3352344898245}\\\\n{\\\\\\\"step\\\\\\\": 216000, \\\\\\\"dataset_size\\\\\\\": 108000.0, \\\\\\\"train_return\\\\\\\": 85.15019226074219, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 216.0}\\\\n{\\\\\\\"step\\\\\\\": 216000, \\\\\\\"dataset_size\\\\\\\": 108000.0, \\\\\\\"train_return\\\\\\\": 190.03192138671875, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 216.0}\\\\n{\\\\\\\"step\\\\\\\": 216000, \\\\\\\"dataset_size\\\\\\\": 108000.0, \\\\\\\"train_return\\\\\\\": 276.46295166015625, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 216.0}\\\\n{\\\\\\\"step\\\\\\\": 216000, \\\\\\\"dataset_size\\\\\\\": 108000.0, \\\\\\\"train_return\\\\\\\": 215.5836181640625, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 216.0}\\\\n{\\\\\\\"step\\\\\\\": 220000, \\\\\\\"dataset_size\\\\\\\": 110000.0, \\\\\\\"train_return\\\\\\\": 214.92422485351562, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 220.0}\\\\n{\\\\\\\"step\\\\\\\": 220000, \\\\\\\"dataset_size\\\\\\\": 110000.0, \\\\\\\"train_return\\\\\\\": 244.76931762695312, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 220.0}\\\\n{\\\\\\\"step\\\\\\\": 220000, \\\\\\\"dataset_size\\\\\\\": 110000.0, \\\\\\\"train_return\\\\\\\": 211.2147216796875, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 220.0}\\\\n{\\\\\\\"step\\\\\\\": 220000, \\\\\\\"dataset_size\\\\\\\": 110000.0, \\\\\\\"train_return\\\\\\\": 212.54171752929688, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 220.0}\\\\n{\\\\\\\"step\\\\\\\": 224000, \\\\\\\"dataset_size\\\\\\\": 112000.0, \\\\\\\"train_return\\\\\\\": 200.2361297607422, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 224.0}\\\\n{\\\\\\\"step\\\\\\\": 224000, \\\\\\\"dataset_size\\\\\\\": 112000.0, \\\\\\\"train_return\\\\\\\": 187.08714294433594, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 224.0}\\\\n{\\\\\\\"step\\\\\\\": 224000, \\\\\\\"dataset_size\\\\\\\": 112000.0, \\\\\\\"train_return\\\\\\\": 192.78289794921875, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 224.0}\\\\n{\\\\\\\"step\\\\\\\": 224000, \\\\\\\"dataset_size\\\\\\\": 112000.0, \\\\\\\"train_return\\\\\\\": 247.33250427246094, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 224.0}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 208000, \\\"dataset_size\\\": 104000.0, \\\"train_return\\\": 235.7844696044922, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 208.0}\\n{\\\"step\\\": 212000, \\\"dataset_size\\\": 106000.0, \\\"train_return\\\": 202.37445068359375, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 212.0}\\n{\\\"step\\\": 212000, \\\"dataset_size\\\": 106000.0, \\\"train_return\\\": 187.92965698242188, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 212.0}\\n{\\\"step\\\": 212000, \\\"dataset_size\\\": 106000.0, \\\"train_return\\\": 221.29074096679688, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 212.0}\\n{\\\"step\\\": 212000, \\\"dataset_size\\\": 106000.0, \\\"train_return\\\": 177.21722412109375, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 212.0}\\n{\\\"step\\\": 215000}\\n{\\\"step\\\": 215000, \\\"eval_return\\\": 161.29613189697267, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n{\\\"step\\\": 215000, \\\"civo/ve_ratio\\\": 0.18638920647786983, \\\"civo/delta_ve\\\": 0.03609233506818024, \\\"civo/alert\\\": 0.0, \\\"model_loss\\\": 5.0361433029174805, \\\"model_grad_norm\\\": 6.7952117919921875, \\\"height_loss\\\": 0.0008423591498285532, \\\"orientations_loss\\\": 0.08522764593362808, \\\"velocity_loss\\\": 0.6637676954269409, \\\"reward_loss\\\": 0.5471906065940857, \\\"cont_loss\\\": 1.3152444411357322e-11, \\\"kl_free\\\": 1.0, \\\"dyn_scale\\\": 0.5, \\\"rep_scale\\\": 0.09999999999999999, \\\"dyn_loss\\\": 6.231858730316162, \\\"rep_loss\\\": 6.231858730316162, \\\"kl\\\": 6.0892558097839355, \\\"prior_ent\\\": 39.70130157470703, \\\"post_ent\\\": 33.5832633972168, \\\"normed_target_mean\\\": 0.3667752146720886, \\\"normed_target_std\\\": 0.33563467860221863, \\\"normed_target_min\\\": -0.0027024284936487675, \\\"normed_target_max\\\": 1.3731828927993774, \\\"EMA_005\\\": 6.1768269538879395, \\\"EMA_095\\\": 71.7769775390625, \\\"value_mean\\\": 30.065412521362305, \\\"value_std\\\": 21.7001895904541, \\\"value_min\\\": 6.19986629486084, \\\"value_max\\\": 93.3718032836914, \\\"target_mean\\\": 30.239381790161133, \\\"target_std\\\": 22.016340255737305, \\\"target_min\\\": 5.9993510246276855, \\\"target_max\\\": 96.25286102294922, \\\"imag_reward_mean\\\": 0.8545054793357849, \\\"imag_reward_std\\\": 1.1082724332809448, \\\"imag_reward_min\\\": -1.2769699253567524e-07, \\\"imag_reward_max\\\": 4.069231033325195, \\\"imag_action_mean\\\": 0.05791507661342621, \\\"imag_action_std\\\": 0.7327951192855835, \\\"imag_action_min\\\": -1.0, \\\"imag_action_max\\\": 1.0, \\\"actor_entropy\\\": -2.7363696098327637, \\\"gate_dt_mean\\\": 2.0, \\\"gate_dt_std\\\": 0.0, \\\"gate_dt_min\\\": 2.0, \\\"gate_dt_max\\\": 2.0, \\\"gate_dt_1_frac\\\": 0.0, \\\"gate_dt_2_frac\\\": 1.0, \\\"gate_dt_3_frac\\\": 0.0, \\\"gate_dt_4_frac\\\": 0.0, \\\"gate_dt_5_frac\\\": 0.0, \\\"gate_dt_6_frac\\\": 0.0, \\\"gate_dt_7_frac\\\": 0.0, \\\"gate_dt_8_frac\\\": 0.0, \\\"gate_empirical_entropy\\\": 0.0, \\\"gate_entropy_ratio\\\": 0.0, \\\"gate_dt_autocorr\\\": 0.0, \\\"actor_loss\\\": -0.0017599775455892086, \\\"actor_grad_norm\\\": 0.09420984238386154, \\\"value_loss\\\": 1.7037900686264038, \\\"value_grad_norm\\\": 1.1889382600784302, \\\"update_count\\\": 52599.0, \\\"fps\\\": 7.3352344898245}\\n{\\\"step\\\": 216000, \\\"dataset_size\\\": 108000.0, \\\"train_return\\\": 85.15019226074219, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 216.0}\\n{\\\"step\\\": 216000, \\\"dataset_size\\\": 108000.0, \\\"train_return\\\": 190.03192138671875, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 216.0}\\n{\\\"step\\\": 216000, \\\"dataset_size\\\": 108000.0, \\\"train_return\\\": 276.46295166015625, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 216.0}\\n{\\\"step\\\": 216000, \\\"dataset_size\\\": 108000.0, \\\"train_return\\\": 215.5836181640625, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 216.0}\\n{\\\"step\\\": 220000, \\\"dataset_size\\\": 110000.0, \\\"train_return\\\": 214.92422485351562, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 220.0}\\n{\\\"step\\\": 220000, \\\"dataset_size\\\": 110000.0, \\\"train_return\\\": 244.76931762695312, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 220.0}\\n{\\\"step\\\": 220000, \\\"dataset_size\\\": 110000.0, \\\"train_return\\\": 211.2147216796875, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 220.0}\\n{\\\"step\\\": 220000, \\\"dataset_size\\\": 110000.0, \\\"train_return\\\": 212.54171752929688, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 220.0}\\n{\\\"step\\\": 224000, \\\"dataset_size\\\": 112000.0, \\\"train_return\\\": 200.2361297607422, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 224.0}\\n{\\\"step\\\": 224000, \\\"dataset_size\\\": 112000.0, \\\"train_return\\\": 187.08714294433594, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 224.0}\\n{\\\"step\\\": 224000, \\\"dataset_size\\\": 112000.0, \\\"train_return\\\": 192.78289794921875, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 224.0}\\n{\\\"step\\\": 224000, \\\"dataset_size\\\": 112000.0, \\\"train_return\\\": 247.33250427246094, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 224.0}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
The log shows the experiment ran to 224K steps (beyond the 210K target), with the last eval at step 215K. The metrics.jsonl ends with training episodes at step 224K. This is a normal completion - the process ran past its target steps and exited cleanly.

Now let me check the registry status. From the read_registry earlier, exp_029a_tcn_walker_s1_sigma02 already has:
- status: DONE
- conclusion: success
- checkpoint_path: /root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt


- log_path: /root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/metrics.jsonl

The registry is already fully updated. The failure_reason about process dead events seems to be a monitoring false alarm that got overridden once the experiment completed successfully. I'll delete the cron now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "0b9a00c4-29e3-4601-897a-4dea4b9ba0f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013c8FXwTru6F7AFJLTqQwKs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3619,
      "cache_read_input_tokens": 45289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3619
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

_source line 35_

训练正常完成：224K 步（超过 210K 目标），最后 eval 在 215K 步，NVE 0.1864。Registry 已标记 DONE/success，checkpoint_path 和 log_path 已设。

删除 cron 监控。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "0668a2e0-fc40-4492-9b6e-447836b58a46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013c8FXwTru6F7AFJLTqQwKs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3619,
      "cache_read_input_tokens": 45289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3619
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

_source line 36_

<details open><summary>🔧 Tool call — CronDelete · `toolu_01F78ScGL2CcuajivK6Wj7r7`</summary>

```json
{
  "id": "exp_029a_tcn_walker_s1_sigma02"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "75612adb-719a-4772-ae79-491dd6e86a37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013c8FXwTru6F7AFJLTqQwKs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3619,
      "cache_read_input_tokens": 45289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3619
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

_source line 37 · 2026-05-20T16:49:02.646Z_

<details><summary>↩ Tool result · reported error · `toolu_01F78ScGL2CcuajivK6Wj7r7`</summary>

```text
&lt;tool_use_error>No scheduled job with id 'exp_029a_tcn_walker_s1_sigma02'&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "c6c1d44f-3214-49a7-999f-4c6724467e7c",
  "tool_use_result": "Error: No scheduled job with id 'exp_029a_tcn_walker_s1_sigma02'"
}
```

</details>

---

### Assistant

_source line 38_

Cron 不存在（可能已被自动清除或未在当前 session 注册）。

**总结：**

| 项目 | 结果 |
|------|------|
| PID 50924 | EXITED |
| 退出状态 | 正常完成，224K/210K 步 |
| Checkpoint | `/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt` |
| Registry | 已是 DONE/success，checkpoint_path + log_path 已设 |
| Cron | 不存在，无需删除 |

exp_029a 已完结，无需额外操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "uuid": "501ef873-26ef-4a39-993e-bf8dc3a9f530",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012v51VV2sLQQ4eX42URpapT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 485,
      "cache_read_input_tokens": 48908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 485
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

### Task result

_source line 39_

Cron 不存在（可能已被自动清除或未在当前 session 注册）。

**总结：**

| 项目 | 结果 |
|------|------|
| PID 50924 | EXITED |
| 退出状态 | 正常完成，224K/210K 步 |
| Checkpoint | `/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt` |
| Registry | 已是 DONE/success，checkpoint_path + log_path 已设 |
| Cron | 不存在，无需删除 |

exp_029a 已完结，无需额外操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 53105,
  "duration_api_ms": 52994,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "7c035c77-a489-448b-bfe8-b98139830554",
  "total_cost_usd": 0.3969535,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 37946,
    "cache_read_input_tokens": 179760,
    "output_tokens": 2746,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37946,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 191,
        "cache_read_input_tokens": 48908,
        "cache_creation_input_tokens": 485,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 485
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1121,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001211,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 2746,
      "cacheReadInputTokens": 179760,
      "cacheCreationInputTokens": 37946,
      "webSearchRequests": 0,
      "costUSD": 0.39574250000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5a2f6bd4-a55f-4d48-bf8c-aeb3878f23f8"
}
```

</details>

---
