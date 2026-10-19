# kill and redeploy bjb2 bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 122
- **Recorded user turns:** 0
- **Tool calls:** 43
- **Original source:** `logs/workers/worker_kill-and-redeploy_bjb2-bjb1-32546_20260528T044006.log`
- **Structured JSON:** [`6b957eb1ac1efda447a3.json`](../../sessions/6b/6b957eb1ac1efda447a3.json)

## Before a recorded user message

122 recorded events

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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
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
    "mcp__agent-ml-research__submit_training_job",
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
  "uuid": "07d68eab-9a51-4d5d-a76a-4d00f046ded2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779960600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "de307d48-d06e-4a11-93bb-32b98051ede8",
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this down into steps:

1. Kill ghost processes on bjb2-28827 and bjb1-32546
2. Deploy replacement experiments

Let me start by loading the necessary tools and killing the processes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "c60c047c-cde8-4c32-a46f-0e30596b2cec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hN5HrAFLC923iWkasbDST",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12954,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12954
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

开始执行。先加载工具并同时在两台服务器上 kill 进程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "b3bf8da4-8f7f-4030-8d96-9bed2893e84f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hN5HrAFLC923iWkasbDST",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12954,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12954
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Py6uuiGPjW7kamhJqchAMC`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__kill_job,mcp__agent-ml-research__detect_image",
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "cdeb61f1-87ac-43a8-bef6-da326583a293",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hN5HrAFLC923iWkasbDST",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12954,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12954
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

_source line 7 · 2026-05-28T04:40:22.381Z_

<details><summary>↩ Tool result · `toolu_01Py6uuiGPjW7kamhJqchAMC`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_training_job"
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
  "tool_name": "mcp__agent-ml-research__kill_job"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "808a9ba0-b8ec-41e9-b0a9-3140b5b38422",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__kill_job,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 27
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me execute the kills on both servers in parallel, and also query the registry for the reference experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "8519583a-2ec9-4e1d-8e76-8affc608e5c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwgK9QA37cPh15BoKWmsCz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2322,
      "cache_read_input_tokens": 24405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2322
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

_source line 9_

同时在两台服务器 kill 进程并查 registry 获取参考命令。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "7af172e1-029a-49d8-81a1-5b496f31fe3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwgK9QA37cPh15BoKWmsCz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2322,
      "cache_read_input_tokens": 24405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2322
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01KaUdnicbY2pvKA7ZspsPFW`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "kill -9 95782 97560 2>&1; echo \"EXIT=$?\"",
  "account": "root",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "5c8205e2-e48d-43b2-a727-95c63d6f6529",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwgK9QA37cPh15BoKWmsCz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2322,
      "cache_read_input_tokens": 24405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2322
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

_source line 11 · 2026-05-28T04:40:29.635Z_

<details><summary>↩ Tool result · `toolu_01KaUdnicbY2pvKA7ZspsPFW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.99}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "99cf6198-e8d0-49eb-bb9f-90bda5f73dc3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"EXIT=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.99}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"EXIT=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.99}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01V2u9i1ePHrD1Z66N91QEyj`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "kill -9 515230 515586 2>&1; echo \"EXIT=$?\"",
  "account": "root",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "d700db26-21f8-4473-81dc-e43ff1b16add",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwgK9QA37cPh15BoKWmsCz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2322,
      "cache_read_input_tokens": 24405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2322
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

_source line 13 · 2026-05-28T04:40:30.934Z_

<details><summary>↩ Tool result · `toolu_01V2u9i1ePHrD1Z66N91QEyj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "12bb47a1-b6cf-4bf5-b130-b747bb21971e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"EXIT=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.85}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"EXIT=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Mw9GvfMVxKba7i3u8MHkeL`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "eval-random-selection-object-seed42"
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "5442d46f-633b-4702-ba72-99615a95e1ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwgK9QA37cPh15BoKWmsCz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2322,
      "cache_read_input_tokens": 24405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2322
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01RbA7rX5m1PfrDWq1L28SJZ`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "eval-ksweep-k20-obs-object-s43"
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "fcba22c2-2b63-4898-a2db-ab53381acdbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwgK9QA37cPh15BoKWmsCz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2322,
      "cache_read_input_tokens": 24405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2322
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

_source line 16 · 2026-05-28T04:40:35.682Z_

<details><summary>↩ Tool result · `toolu_01Mw9GvfMVxKba7i3u8MHkeL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1047}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "2e4e306e-0f34-4968-94d0-4326502764ef",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.1047}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1047}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T04:40:40.296Z_

<details><summary>↩ Tool result · `toolu_01RbA7rX5m1PfrDWq1L28SJZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.5913}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "234abc00-58fc-4ea4-8b2c-18a6c1207595",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.5913}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.5913}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Kill commands succeeded on both servers. Now I need to:
1. Verify GPU release with nvidia-smi on both servers
2. Find the reference experiments in registry (the exact exp_ids might be different)

Let me check nvidia-smi on both servers and search the registry more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "4940ca7a-8f98-4a48-aa94-287f308b10b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDZcpqzXapjfEgVbMgJYf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 26727,
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

_source line 19_

Kill 成功。现在验证 GPU 释放，同时搜索 registry 找参考实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "66d1eb4a-7371-4b9b-a800-a7ca3f53ad29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDZcpqzXapjfEgVbMgJYf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 26727,
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

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FqnPbeS94yynkKSPvJ8LMA`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "65227721-a0fd-414d-9bf1-10d89750ff95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDZcpqzXapjfEgVbMgJYf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 26727,
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

_source line 21 · 2026-05-28T04:40:47.925Z_

<details><summary>↩ Tool result · `toolu_01FqnPbeS94yynkKSPvJ8LMA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 MiB, 24564 MiB\\n1, 0 MiB, 24564 MiB\\n2, 0 MiB, 24564 MiB\\n3, 0 MiB, 24564 MiB\\n4, 0 MiB, 24564 MiB\\n5, 0 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "07678adb-43f3-4b3a-8e29-edcae95da09a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 0 MiB, 24564 MiB\\\\n1, 0 MiB, 24564 MiB\\\\n2, 0 MiB, 24564 MiB\\\\n3, 0 MiB, 24564 MiB\\\\n4, 0 MiB, 24564 MiB\\\\n5, 0 MiB, 24564 MiB\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 0 MiB, 24564 MiB\\n1, 0 MiB, 24564 MiB\\n2, 0 MiB, 24564 MiB\\n3, 0 MiB, 24564 MiB\\n4, 0 MiB, 24564 MiB\\n5, 0 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013PfW4ZenhbuXpVDsWAkSgP`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "63fd7bd2-2388-49b1-aa3b-3d509617e7d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDZcpqzXapjfEgVbMgJYf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 26727,
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

_source line 23 · 2026-05-28T04:40:48.954Z_

<details><summary>↩ Tool result · `toolu_013PfW4ZenhbuXpVDsWAkSgP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 12612 MiB, 24564 MiB\\n1, 12612 MiB, 24564 MiB\\n2, 12693 MiB, 24564 MiB\\n3, 2 MiB, 24564 MiB\\n4, 2 MiB, 24564 MiB\\n5, 2 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "74656651-9bec-42f2-8ed9-4c6dad3a867c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 12612 MiB, 24564 MiB\\\\n1, 12612 MiB, 24564 MiB\\\\n2, 12693 MiB, 24564 MiB\\\\n3, 2 MiB, 24564 MiB\\\\n4, 2 MiB, 24564 MiB\\\\n5, 2 MiB, 24564 MiB\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 12612 MiB, 24564 MiB\\n1, 12612 MiB, 24564 MiB\\n2, 12693 MiB, 24564 MiB\\n3, 2 MiB, 24564 MiB\\n4, 2 MiB, 24564 MiB\\n5, 2 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01884kWZAmLiQyYdmMKwpofw`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "spec.command",
    "status"
  ],
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "e7392118-d536-4c09-9369-edfa7e5f7c97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDZcpqzXapjfEgVbMgJYf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 26727,
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

_source line 25 · 2026-05-28T04:40:52.768Z_

<details><summary>↩ Tool result · `toolu_01884kWZAmLiQyYdmMKwpofw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"smolvla-tau020-long-s42\": {\"status\": \"DONE\"}, \"smolvla-tau015-spatial-s42-fix\": {\"status\": \"DONE\"}, \"crm-always-on-long-s45\": {\"status\": \"DONE\"}, \"pi05-crm-always-on-object-s43\": {\"status\": \"DONE\"}, \"smolvla-tau045-long-s42\": {\"status\": \"DONE\"}, \"smolvla-tau040-long-s42\": {\"status\": \"DONE\"}, \"pi05-crm-always-on-object-s42\": {\"status\": \"DONE\"}, \"pi05-crm-always-on-goal-s42\": {\"status\": \"DONE\"}, \"smolvla-tau020-long-s43-r2\": {\"status\": \"DONE\"}, \"eval-tau005-spatial-s42\": {\"status\": \"DONE\"}, \"pi05-crm-always-on-spatial-s42\": {\"status\": \"DONE\"}, \"eval-tau040-spatial-s42\": {\"status\": \"DONE\"}, \"eval-tau045-spatial-s42\": {\"status\": \"DONE\"}, \"crm-always-on-object-s46\": {\"status\": \"DONE\"}, \"smolvla-tau005-long-s42\": {\"status\": \"DONE\"}, \"crm-always-on-object-s45\": {\"status\": \"DONE\"}, \"smolvla-tau010-long-s42\": {\"status\": \"DONE\"}, \"pi05-tau-sweep-goal-tau070-s42-r2\": {\"status\": \"DONE\"}, \"pi05-tau-sweep-goal-tau050-s42-r2\": {\"status\": \"DONE\"}, \"pi05-goal-tau035-s43-r3\": {\"status\": \"DONE\"}, \"crm-always-on-long-s44\": {\"status\": \"DONE\"}, \"crm-always-on-spatial-s46\": {\"status\": \"DONE\"}, \"crm-always-on-goal-s46\": {\"status\": \"DONE\"}, \"crm-always-on-goal-s45\": {\"status\": \"DONE\"}, \"crm-always-on-spatial-s45\": {\"status\": \"DONE\"}, \"pi05-goal-tau025-s43-r3\": {\"status\": \"DONE\"}, \"pi05-tau-sweep-goal-tau050-s42-r3\": {\"status\": \"DONE\"}, \"pi05-goal-tau015-s43-r3\": {\"status\": \"DONE\"}, \"smolvla-tau035-long-s42\": {\"status\": \"DONE\"}, \"smolvla-tau030-long-s42\": {\"status\": \"DONE\"}, \"smolvla-tau015-long-s42\": {\"status\": \"DONE\"}, \"smolvla-tau045-object-s42\": {\"status\": \"DONE\"}, \"smolvla-tau040-object-s42\": {\"status\": \"DONE\"}, \"smolvla-tau030-object-s42\": {\"status\": \"DONE\"}, \"crm-always-on-long-s43\": {\"status\": \"DONE\"}, \"crm-always-on-long-s42\": {\"status\": \"DONE\"}, \"smolvla-tau025-long-s42\": {\"status\": \"DONE\"}, \"pi05-long-tau015-s43-r3\": {\"status\": \"DONE\"}, \"pi05-k2mean-spatial-s42-r3\": {\"status\": \"DONE\"}, \"pi05-k2mean-long-s42-r3\": {\"status\": \"DONE\"}, \"pi05-k2mean-object-s42-r3\": {\"status\": \"DONE\"}, \"smolvla-tau035-object-s42-r3\": {\"status\": \"DONE\"}, \"smolvla-tau025-object-s42-r3\": {\"status\": \"DONE\"}, \"smolvla-tau020-object-s42\": {\"status\": \"DONE\"}, \"smolvla-tau010-object-s42\": {\"status\": \"DONE\"}, \"smolvla-tau005-object-s42\": {\"status\": \"DONE\"}, \"crm-always-on-goal-s43\": {\"status\": \"DONE\"}, \"crm-always-on-goal-s42\": {\"status\": \"DONE\"}, \"crm-always-on-spatial-s44\": {\"status\": \"DONE\"}, \"crm-always-on-spatial-s43\": {\"status\": \"DONE\"}}, \"count\": 50, \"total\": 1223, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.2478}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "1bafc70e-5779-4b8b-921b-97444034150f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"smolvla-tau020-long-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau015-spatial-s42-fix\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-long-s45\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-crm-always-on-object-s43\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau045-long-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau040-long-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-crm-always-on-object-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-crm-always-on-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau020-long-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"eval-tau005-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-crm-always-on-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"eval-tau040-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"eval-tau045-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-object-s46\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau005-long-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-object-s45\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau010-long-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-tau-sweep-goal-tau070-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-tau-sweep-goal-tau050-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-goal-tau035-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-long-s44\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-spatial-s46\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-goal-s46\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-goal-s45\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-goal-tau025-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-tau-sweep-goal-tau050-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-goal-tau015-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau035-long-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau030-long-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau015-long-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau045-object-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau040-object-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau030-object-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-long-s43\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-long-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau025-long-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-long-tau015-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-k2mean-spatial-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-k2mean-long-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pi05-k2mean-object-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau035-object-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau025-object-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau020-object-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau010-object-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"smolvla-tau005-object-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-goal-s43\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-spatial-s44\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"crm-always-on-spatial-s43\\\": {\\\"status\\\": \\\"DONE\\\"}}, \\\"count\\\": 50, \\\"total\\\": 1223, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.2478}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"smolvla-tau020-long-s42\": {\"status\": \"DONE\"}, \"smolvla-tau015-spatial-s42-fix\": {\"status\": \"DONE\"}, \"crm-always-on-long-s45\": {\"status\": \"DONE\"}, \"pi05-crm-always-on-object-s43\": {\"status\": \"DONE\"}, \"smolvla-tau045-long-s42\": {\"status\": \"DONE\"}, \"smolvla-tau040-long-s42\": {\"status\": \"DONE\"}, \"pi05-crm-always-on-object-s42\": {\"status\": \"DONE\"}, \"pi05-crm-always-on-goal-s42\": {\"status\": \"DONE\"}, \"smolvla-tau020-long-s43-r2\": {\"status\": \"DONE\"}, \"eval-tau005-spatial-s42\": {\"status\": \"DONE\"}, \"pi05-crm-always-on-spatial-s42\": {\"status\": \"DONE\"}, \"eval-tau040-spatial-s42\": {\"status\": \"DONE\"}, \"eval-tau045-spatial-s42\": {\"status\": \"DONE\"}, \"crm-always-on-object-s46\": {\"status\": \"DONE\"}, \"smolvla-tau005-long-s42\": {\"status\": \"DONE\"}, \"crm-always-on-object-s45\": {\"status\": \"DONE\"}, \"smolvla-tau010-long-s42\": {\"status\": \"DONE\"}, \"pi05-tau-sweep-goal-tau070-s42-r2\": {\"status\": \"DONE\"}, \"pi05-tau-sweep-goal-tau050-s42-r2\": {\"status\": \"DONE\"}, \"pi05-goal-tau035-s43-r3\": {\"status\": \"DONE\"}, \"crm-always-on-long-s44\": {\"status\": \"DONE\"}, \"crm-always-on-spatial-s46\": {\"status\": \"DONE\"}, \"crm-always-on-goal-s46\": {\"status\": \"DONE\"}, \"crm-always-on-goal-s45\": {\"status\": \"DONE\"}, \"crm-always-on-spatial-s45\": {\"status\": \"DONE\"}, \"pi05-goal-tau025-s43-r3\": {\"status\": \"DONE\"}, \"pi05-tau-sweep-goal-tau050-s42-r3\": {\"status\": \"DONE\"}, \"pi05-goal-tau015-s43-r3\": {\"status\": \"DONE\"}, \"smolvla-tau035-long-s42\": {\"status\": \"DONE\"}, \"smolvla-tau030-long-s42\": {\"status\": \"DONE\"}, \"smolvla-tau015-long-s42\": {\"status\": \"DONE\"}, \"smolvla-tau045-object-s42\": {\"status\": \"DONE\"}, \"smolvla-tau040-object-s42\": {\"status\": \"DONE\"}, \"smolvla-tau030-object-s42\": {\"status\": \"DONE\"}, \"crm-always-on-long-s43\": {\"status\": \"DONE\"}, \"crm-always-on-long-s42\": {\"status\": \"DONE\"}, \"smolvla-tau025-long-s42\": {\"status\": \"DONE\"}, \"pi05-long-tau015-s43-r3\": {\"status\": \"DONE\"}, \"pi05-k2mean-spatial-s42-r3\": {\"status\": \"DONE\"}, \"pi05-k2mean-long-s42-r3\": {\"status\": \"DONE\"}, \"pi05-k2mean-object-s42-r3\": {\"status\": \"DONE\"}, \"smolvla-tau035-object-s42-r3\": {\"status\": \"DONE\"}, \"smolvla-tau025-object-s42-r3\": {\"status\": \"DONE\"}, \"smolvla-tau020-object-s42\": {\"status\": \"DONE\"}, \"smolvla-tau010-object-s42\": {\"status\": \"DONE\"}, \"smolvla-tau005-object-s42\": {\"status\": \"DONE\"}, \"crm-always-on-goal-s43\": {\"status\": \"DONE\"}, \"crm-always-on-goal-s42\": {\"status\": \"DONE\"}, \"crm-always-on-spatial-s44\": {\"status\": \"DONE\"}, \"crm-always-on-spatial-s43\": {\"status\": \"DONE\"}}, \"count\": 50, \"total\": 1223, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.2478}}"
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
GPU status:
- bjb2-28827: All GPUs at 0 MiB — cuda:4 and cuda:5 confirmed released ✓
- bjb1-32546: cuda:0/1/2 busy (12612-12693 MiB), cuda:3/4/5 at 2 MiB — confirmed released ✓

Now I need to find the reference experiments. The exact exp_ids I was given don't exist. Let me search more broadly for "random-selection" and "ksweep" experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "33e70f34-9642-4a55-9218-094e20105285",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EinJnCKpeRKJzqkqve9JW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2353,
      "cache_read_input_tokens": 27678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2353
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

GPU 释放确认：
- **bjb2-28827**: 全部 6 GPU 均 0 MiB ✓
- **bjb1-32546**: cuda:3 = 2 MiB, cuda:4 = 2 MiB ✓（cuda:0/1/2 有其他实验在跑）

搜索参考实验命令。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "c1de43a4-e778-4d44-838c-e6794c6d4da0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EinJnCKpeRKJzqkqve9JW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2353,
      "cache_read_input_tokens": 27678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2353
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01FaipdrKyYoFVV7MzQD5hZQ`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "spec.command"
  ],
  "limit": 1223
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "0b9f6e37-a65d-40a3-b527-6270fd2cc471",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EinJnCKpeRKJzqkqve9JW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2353,
      "cache_read_input_tokens": 27678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2353
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

_source line 29 · 2026-05-28T04:41:09.714Z_

<details><summary>↩ Tool result · `toolu_01FaipdrKyYoFVV7MzQD5hZQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"smolvla-tau020-long-s42\": {}, \"smolvla-tau015-spatial-s42-fix\": {}, \"crm-always-on-long-s45\": {}, \"pi05-crm-always-on-object-s43\": {}, \"smolvla-tau045-long-s42\": {}, \"smolvla-tau040-long-s42\": {}, \"pi05-crm-always-on-object-s42\": {}, \"pi05-crm-always-on-goal-s42\": {}, \"smolvla-tau020-long-s43-r2\": {}, \"eval-tau005-spatial-s42\": {}, \"pi05-crm-always-on-spatial-s42\": {}, \"eval-tau040-spatial-s42\": {}, \"eval-tau045-spatial-s42\": {}, \"crm-always-on-object-s46\": {}, \"smolvla-tau005-long-s42\": {}, \"crm-always-on-object-s45\": {}, \"smolvla-tau010-long-s42\": {}, \"pi05-tau-sweep-goal-tau070-s42-r2\": {}, \"pi05-tau-sweep-goal-tau050-s42-r2\": {}, \"pi05-goal-tau035-s43-r3\": {}, \"crm-always-on-long-s44\": {}, \"crm-always-on-spatial-s46\": {}, \"crm-always-on-goal-s46\": {}, \"crm-always-on-goal-s45\": {}, \"crm-always-on-spatial-s45\": {}, \"pi05-goal-tau025-s43-r3\": {}, \"pi05-tau-sweep-goal-tau050-s42-r3\": {}, \"pi05-goal-tau015-s43-r3\": {}, \"smolvla-tau035-long-s42\": {}, \"smolvla-tau030-long-s42\": {}, \"smolvla-tau015-long-s42\": {}, \"smolvla-tau045-object-s42\": {}, \"smolvla-tau040-object-s42\": {}, \"smolvla-tau030-object-s42\": {}, \"crm-always-on-long-s43\": {}, \"crm-always-on-long-s42\": {}, \"smolvla-tau025-long-s42\": {}, \"pi05-long-tau015-s43-r3\": {}, \"pi05-k2mean-spatial-s42-r3\": {}, \"pi05-k2mean-long-s42-r3\": {}, \"pi05-k2mean-object-s42-r3\": {}, \"smolvla-tau035-object-s42-r3\": {}, \"smolvla-tau025-object-s42-r3\": {}, \"smolvla-tau020-object-s42\": {}, \"smolvla-tau010-object-s42\": {}, \"smolvla-tau005-object-s42\": {}, \"crm-always-on-goal-s43\": {}, \"crm-always-on-goal-s42\": {}, \"crm-always-on-spatial-s44\": {}, \"crm-always-on-spatial-s43\": {}, \"smolvla-tau030-long-s42-r2\": {}, \"smolvla-tau030-long-s43-r2\": {}, \"tau-sweep-goal-tau035-s42\": {}, \"tau-sweep-long-tau015-s42\": {}, \"tau-sweep-long-tau035-s42\": {}, \"smolvla-tau020-long-s42-r2\": {}, \"tau-sweep-goal-tau015-s42\": {}, \"tau-sweep-spatial-tau035-s42\": {}, \"tau-sweep-spatial-tau015-s42\": {}, \"smolvla-tau035-object-s42-r2\": {}, \"smolvla-tau035-object-s43-r3\": {}, \"smolvla-tau025-object-s43-r3\": {}, \"crm-always-on-spatial-s42\": {}, \"crm-always-on-goal-s44\": {}, \"crm-always-on-object-s44\": {}, \"crm-always-on-object-s43\": {}, \"crm-always-on-object-s42\": {}, \"eval-obs-object-norm003-s45\": {}, \"eval-obs-object-norm005-s45\": {}, \"eval-obs-object-norm003-s46\": {}, \"pi05-k2mean-goal-s43\": {}, \"pi05-k2mean-long-s42\": {}, \"pi05-k2mean-object-s42\": {}, \"pi05-vla-only-spatial-s42-4090\": {}, \"pi05-vla-only-goal-s42-4090\": {}, \"pi05-k2mean-spatial-s42\": {}, \"pi05-vla-only-spatial-s42-4090-r2\": {}, \"pi05-vla-only-object-s42-4090-r2\": {}, \"pi05-vla-only-goal-s42-4090-r2\": {}, \"eval-k2-tau010-015-spatial-s42\": {}, \"eval-k2-tau010-spatial-s42\": {}, \"eval-pi05-vla-only-long-seed42-r4-std\": {}, \"eval-obs-only-object-norm02-k20-seed44\": {}, \"eval-obs-only-object-norm02-k20-seed43\": {}, \"eval-obs-only-object-norm02-k20-seed42\": {}, \"eval-pi05-baseline-object-seed42-r2\": {}, \"pi05-vla-only-object-s42-4090\": {}, \"pi05-vla-only-long-s42-4090\": {}, \"smolvla-tau020-long-s43\": {}, \"smolvla-tau030-long-s43\": {}, \"eval-pi05-vla-only-object-s43-r5\": {}, \"eval-perdof-object-norm005-s44-westd\": {}, \"eval-perdof-object-norm003-s44-westd\": {}, \"eval-obs-object-norm005-s45-bjb2\": {}, \"eval-obs-object-norm005-s44-bjb2\": {}, \"eval-obs-object-norm003-s44-bjb2\": {}, \"eval-obs-object-norm005-s43-bjb2\": {}, \"eval-obs-object-norm003-s43-bjb2\": {}, \"eval-obs-object-norm005-s46\": {}, \"eval-perdof-object-norm005-s43-v3\": {}, \"eval-perdof-object-norm003-s43-v3\": {}, \"pi05-vla-only-goal-s44-4090\": {}, \"pi05-vla-only-object-s43-4090\": {}, \"pi05-vla-only-long-s44-4090\": {}, \"pi05-vla-only-long-s43-4090\": {}, \"pi05-vla-only-long-s42-4090-r3\": {}, \"eval-ksweep-k5-obs-object-s43\": {}, \"eval-obs-object-norm005-s44-westd\": {}, \"eval-k2-tau035-spatial-s42-v2\": {}, \"eval-obs-object-norm005-s43-westd\": {}, \"eval-obs-object-norm003-s43\": {}, \"eval-obs-object-norm005-s43\": {}, \"eval-obs-object-norm003-s44\": {}, \"eval-ksweep-k20-obs-object-s43\": {}, \"eval-ksweep-k20-obs-object-s42\": {}, \"eval-k2-tau025-spatial-s42-v2\": {}, \"eval-obs-object-norm003-s43-westd\": {}, \"eval-obs-object-norm003-s44-westd\": {}, \"eval-obs-object-norm005-s44\": {}, \"eval-ksweep-k5-obs-object-s42\": {}, \"smolvla-vla-only-long-n20-s43\": {}, \"smolvla-vla-only-long-n20-s42\": {}, \"pi05-object-adaptive-s44-cqa1\": {}, \"pi05-object-adaptive-s43-cqa1\": {}, \"pi05-object-adaptive-s42-cqa1\": {}, \"eval-pi05-vla-only-object-s43-v2\": {}, \"eval-pi05-vla-only-object-s42-v2\": {}, \"eval-pi05-vla-only-goal-s43-v2\": {}, \"eval-pi05-vla-only-goal-s42-v2\": {}, \"eval-pi05-vla-only-spatial-s43-v2\": {}, \"eval-pi05-vla-only-spatial-s42-v2\": {}, \"smolvla-tau025-long-s43\": {}, \"smolvla-tau015-long-s43\": {}, \"smolvla-tau025-object-s42-r2\": {}, \"smolvla-tau035-long-s43\": {}, \"pi05-goal-tau015-s43\": {}, \"smolvla-tau035-spatial-s43\": {}, \"smolvla-tau025-spatial-s43\": {}, \"smolvla-tau015-spatial-s43\": {}, \"pi05-goal-tau035-s43\": {}, \"pi05-goal-tau025-s43\": {}, \"pi05-adaptive-long-s43-cqa1-r3\": {}, \"pi05-spatial-tau015-s43\": {}, \"pi05-spatial-tau035-s43\": {}, \"pi05-spatial-tau025-s43\": {}, \"pi05-object-tau035-s42-bjb2\": {}, \"E_smolvla_crm_norm005_spatial_s42_d149\": {}, \"pi05-object-tau015-s42-bjb2\": {}, \"E_smolvla_adaptive_tau045_spatial_s42\": {}, \"E_smolvla_adaptive_tau035_spatial_s42\": {}, \"E_smolvla_adaptive_tau015_spatial_s42\": {}, \"pi05-adaptive-object-s42-tau045-bjb2\": {}, \"smolvla-tau035-spatial-s42-bjb1\": {}, \"smolvla-tau015-spatial-s42-bjb1\": {}, \"smolvla-crm-norm005-spatial-s42-d149\": {}, \"smolvla-tau045-spatial-s42\": {}, \"pi05-adaptive-long-s44-bjb1\": {}, \"pi05-adaptive-long-s43-bjb1\": {}, \"eval-k2-tau045-spatial-s42-bjb2\": {}, \"smolvla-crm-norm005-k10-object-s44-cqa1\": {}, \"smolvla-adapt-tau015-object-s44-cqa1\": {}, \"smolvla-adapt-tau015-object-s43-cqa1\": {}, \"smolvla-adapt-tau015-object-s42-cqa1\": {}, \"smolvla-tau015-object-s42\": {}, \"smolvla-tau025-object-s43\": {}, \"smolvla-tau035-goal-s42\": {}, \"smolvla-tau025-goal-s42\": {}, \"smolvla-tau015-goal-s42\": {}, \"smolvla-tau015-object-s43\": {}, \"smolvla-tau035-object-s43\": {}, \"pi05-adaptive-long-s42-tau035-bjb2\": {}, \"smolvla-tau015-goal-s43\": {}, \"smolvla-tau025-goal-s43\": {}, \"smolvla-tau035-goal-s43\": {}, \"pi05-adaptive-long-s42-tau015-bjb2\": {}, \"smolvla-tau035-object-s43-bjb1\": {}, \"smolvla-tau025-object-s43-bjb1\": {}, \"smolvla-tau015-object-s43-bjb1\": {}, \"smolvla-tau035-goal-s43-bjb1\": {}, \"smolvla-tau025-goal-s43-bjb1\": {}, \"smolvla-tau015-goal-s43-bjb1\": {}, \"pi05-adaptive-goal-s42-tau035-bjb2\": {}, \"westd-pi05-adaptive-object-s44-paired\": {}, \"westd-pi05-adaptive-object-s43-paired\": {}, \"westd-pi05-adaptive-object-s42-paired\": {}, \"westd-pi05-crm-k2-object-s44\": {}, \"westd-pi05-crm-k2-object-s43\": {}, \"westd-pi05-crm-k2-object-s42\": {}, \"eval-crm-goal-s43-d149-bjb1\": {}, \"eval-crm-object-s43-d149-bjb1\": {}, \"eval-crm-object-s42-d149-bjb1\": {}, \"eval-crm-spatial-s48-d149-bjb1\": {}, \"pi05-adaptive-long-s44-cqa1-r3\": {}, \"pi05-adaptive-object-s44-cqa1-r3\": {}, \"pi05-adaptive-object-s43-cqa1-r3\": {}, \"pi05-adaptive-goal-s42-tau015-bjb2\": {}, \"pi05-adaptive-spatial-s42-tau015-bjb2\": {}, \"pi05-adaptive-spatial-s42-tau035-bjb2\": {}, \"eval-crm-goal-s43-d149\": {}, \"eval-crm-goal-s44-d149\": {}, \"eval-crm-object-s42-d149\": {}, \"eval-crm-object-s43-d149\": {}, \"eval-crm-object-s44-d149\": {}, \"eval-crm-spatial-s48-d149\": {}, \"pi05-adaptive-long-s43-cqa1\": {}, \"eval-supp-goal-k2mean-s47\": {}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {}, \"eval-smolvla-lerobot-goal-seed43-v3\": {}, \"precompute-pi05-object-2048-r2\": {}, \"precompute-pi05-long-2048-r2\": {}, \"pi05-adaptive-long-s44-cqa1\": {}, \"eval-supp-goal-adapt-tau025-s47\": {}, \"eval-supp-goal-crm-norm005-s47\": {}, \"eval-supp-goal-reconvla-s47\": {}, \"eval-supp-obj-reconvla-s47\": {}, \"eval-supp-reconvla-obj-s45\": {}, \"eval-supp-spatial-k2mean-s46\": {}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {}, \"eval-supp-spatial-reconvla-s46\": {}, \"pi05-crm-k2-long-s44-cqa1\": {}, \"pi05-crm-k2-object-s42-bjb1-r2\": {}, \"pi05-crm-k2-object-s43-bjb1-r2\": {}, \"pi05-crm-k2-object-s44-bjb1-r2\": {}, \"pi05-adaptive-goal-s44-bjb1\": {}, \"pi05-adaptive-spatial-s44-bjb2-r2\": {}, \"pi05-adaptive-spatial-s43-bjb2-r2\": {}, \"pi05-adaptive-spatial-s42-bjb2-r2\": {}, \"pi05-crm-k2-spatial-s44-bjb2-r2\": {}, \"pi05-crm-k2-spatial-s43-bjb2-r2\": {}, \"pi05-crm-k2-spatial-s42-bjb2-r2\": {}, \"pi05-crm-k2-goal-s44-bjb1-r2\": {}, \"pi05-crm-k2-goal-s43-bjb1-r2\": {}, \"pi05-crm-k2-goal-s42-bjb1-r2\": {}, \"westd-pi05-vla-only-long-s44-paired\": {}, \"pi05-crm-k2-long-s42-r2\": {}, \"pi05-crm-k2-long-s43-r2\": {}, \"westd-pi05-vla-only-long-s43-paired\": {}, \"pi05-crm-k2-long-s43-cqa1\": {}, \"westd-pi05-vla-only-spatial-s43-paired\": {}, \"westd-pi05-vla-only-spatial-s42-paired\": {}, \"westd-pi05-vla-only-spatial-s44-paired\": {}, \"westd-pi05-vla-only-long-s42-paired\": {}, \"westd-pi05-vla-only-object-s44-paired\": {}, \"westd-pi05-vla-only-object-s43-paired\": {}, \"westd-pi05-vla-only-object-s42-paired\": {}, \"westd-pi05-vla-only-goal-s44-paired\": {}, \"westd-pi05-vla-only-goal-s43-paired\": {}, \"westd-pi05-vla-only-goal-s42-paired\": {}, \"pi05-adaptive-object-s42-cqa1\": {}, \"pi05-adaptive-long-s42-r2\": {}, \"pi05-adaptive-object-s43-bjb2-24035\": {}, \"pi05-adaptive-long-s44-cqa1-r2\": {}, \"pi05-adaptive-long-s43-cqa1-r2\": {}, \"pi05-adaptive-goal-s42-cqa1\": {}, \"westd-pi05-crm-k2-goal-s42\": {}, \"westd-pi05-adaptive-object-s42\": {}, \"westd-pi05-adaptive-goal-s43\": {}, \"westd-pi05-adaptive-goal-s42\": {}, \"pi05-adaptive-object-s44-cqa1-r2\": {}, \"pi05-adaptive-goal-s43-bjb1-18228\": {}, \"westd-pi05-adaptive-object-s43\": {}, \"pi05-crm-k2-spatial-s44-bjb2\": {}, \"pi05-crm-k2-spatial-s43-bjb2\": {}, \"pi05-crm-k2-spatial-s42-bjb2\": {}, \"pi05-adaptive-spatial-s44-bjb2\": {}, \"pi05-adaptive-spatial-s43-bjb2\": {}, \"pi05-adaptive-spatial-s42-bjb2\": {}, \"pi05-crm-k2-object-s44-bjb1\": {}, \"pi05-crm-k2-object-s43-bjb1\": {}, \"pi05-crm-k2-object-s42-bjb1\": {}, \"pi05-crm-k2-goal-s44-bjb1\": {}, \"pi05-crm-k2-goal-s43-bjb1\": {}, \"pi05-crm-k2-goal-s42-bjb1\": {}, \"eval-adaptive-spatial-s44-d149\": {}, \"eval-adaptive-spatial-s43-d149\": {}, \"eval-adaptive-goal-s44-d149\": {}, \"eval-adaptive-goal-s43-d149\": {}, \"eval-adaptive-object-s44-d149\": {}, \"eval-adaptive-object-s43-d149\": {}, \"eval-supp-crm-norm005-obj-s44\": {}, \"eval-adaptive-spatial-k1-s42\": {}, \"westd-pi05-vla-only-goal-s42\": {}, \"eval-supp-goal-vla-only-wrapper-s43\": {}, \"westd-pi05-adaptive-goal-s44\": {}, \"tau_sweep_goal_tau090_s42_cqa1\": {}, \"tau_sweep_goal_tau070_s42_cqa1\": {}, \"tau_sweep_goal_tau050_s42_cqa1\": {}, \"tau_sweep_spatial_tau025_s42\": {}, \"tau_sweep_goal_tau025_s42\": {}, \"tau_sweep_goal_tau040_s42\": {}, \"tau_sweep_goal_tau045_s42\": {}, \"goal_vla_only_s48\": {}, \"goal_adapt_s48\": {}, \"westd-pi05-k2mean-goal-s42\": {}, \"eval-goal-vla-only-s49-paired\": {}, \"eval-goal-adapt-tau025-s49-paired\": {}, \"eval-spatial-vla-only-s48-paired\": {}, \"eval-spatial-vla-only-s46-paired\": {}, \"eval-spatial-adapt-tau025-s48-paired\": {}, \"eval-spatial-adapt-tau025-s46-paired\": {}, \"pi05-adaptive-long-s42\": {}, \"pi05-adaptive-object-s42-v2\": {}, \"pi05-k2mean-goal-s42\": {}, \"pi05-crm-k2-long-s44\": {}, \"eval-k2-goal-vla-only-s49\": {}, \"eval-mechanism-goal-adapt-s42\": {}, \"pi05-crm-k2-long-s43\": {}, \"pi05-crm-k2-long-s42\": {}, \"eval-k2-tau030-spatial-s42\": {}, \"eval-k2-tau020-spatial-s42\": {}, \"eval-pi05-vla-spatial-s44\": {}, \"eval-pi05-adaptive-goal-s44\": {}, \"eval-pi05-adaptive-object-s44\": {}, \"eval-pi05-crm-object-s42\": {}, \"eval-pi05-crm-goal-s42\": {}, \"eval-pi05-crm-goal-s43\": {}, \"eval-pi05-crm-goal-s44\": {}, \"eval-pi05-crm-spatial-s42\": {}, \"eval-pi05-crm-spatial-s43\": {}, \"eval-pi05-crm-goal-s42-d149\": {}, \"eval-pi05-crm-spatial-s42-d149\": {}, \"eval-pi05-crm-spatial-s43-d149\": {}, \"eval-pi05-crm-goal-s43-d149\": {}, \"eval-pi05-crm-goal-s44-d149\": {}, \"eval-vla-only-long-s44-d149\": {}, \"eval-adaptive-long-s43-d149\": {}, \"eval-crm-long-s44-d149\": {}, \"eval-crm-long-s43-d149\": {}, \"eval-pi05-adaptive-object-s43\": {}, \"eval-pi05-adaptive-object-s42\": {}, \"eval-pi05-adaptive-goal-s43\": {}, \"eval-smolvla-crm-goal-s42\": {}, \"eval-crm-long-s42-d149\": {}, \"eval-pi05-vla-only-object-s43\": {}, \"eval-pi05-vla-only-goal-s44\": {}, \"eval-smolvla-crm-goal-seed44\": {}, \"eval-vla-only-spatial-bjb1-s49\": {}, \"eval-vla-only-spatial-bjb1-s48\": {}, \"eval-adaptive-long-s44-d149\": {}, \"eval-adaptive-long-s42-d149\": {}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {}, \"eval-k2-spatial-adapt-s44-paired-r2\": {}, \"eval-k2-spatial-adapt-s43-paired-r2\": {}, \"eval-k2-spatial-adapt-s42-paired-r2\": {}, \"eval-vla-only-spatial-s47-d149\": {}, \"eval-adaptive-object-s42-d149\": {}, \"eval-smolvla-crm-spatial-s47\": {}, \"eval-pi05-adaptive-goal-s42-dryrun\": {}, \"eval-adaptive-spatial-s47-bjb1-d149\": {}, \"eval-adaptive-spatial-s47-d149\": {}, \"eval-adaptive-goal-s42-d149\": {}, \"eval-pi05-vla-only-object-s42-r2\": {}, \"eval-pi05-adaptive-spatial-s42-r2\": {}, \"eval-pi05-vla-only-spatial-s44-d149\": {}, \"eval-pi05-adaptive-goal-s42\": {}, \"eval-k2-tau010-spatial-s42-r3\": {}, \"eval-k2-tau0075-spatial-s42\": {}, \"eval-k2-tau015-spatial-s42-r2\": {}, \"eval-k2-goal-vla-only-s46-paired\": {}, \"eval-k2-goal-vla-only-s45-paired\": {}, \"eval-k2-goal-adapt-s47-paired\": {}, \"eval-k2-goal-adapt-s46-paired\": {}, \"eval-k2-goal-vla-only-s47-paired\": {}, \"eval-k2-goal-adapt-s45-paired\": {}, \"eval-vla-only-spatial-bjb1-s46\": {}, \"eval-k2-adaptive-spatial-s49\": {}, \"eval-k2-adaptive-spatial-s48\": {}, \"eval-k2-adaptive-spatial-s46\": {}, \"eval-pi05-vla-only-spatial-s43-r2\": {}, \"eval-k2-adaptive-spatial-s43\": {}, \"eval-k2-adaptive-spatial-s42\": {}, \"eval-vla-only-spatial-cqa1-s44\": {}, \"eval-vla-only-spatial-cqa1-s43\": {}, \"eval-vla-only-spatial-cqa1-s42\": {}, \"eval-k2-adaptive-spatial-s44\": {}, \"eval-canonical-adaptive-k10-spatial-s42\": {}, \"eval-k10-tau025-spatial-s45\": {}, \"eval-k10-tau025-spatial-s47\": {}, \"eval-long-adaptive-k10-s42\": {}, \"eval-pi05-vla-only-spatial-s42-paired\": {}, \"eval-pi05-vla-only-goal-s42-paired\": {}, \"eval-long-adaptive-k10-s43\": {}, \"eval-long-adaptive-k10-s44\": {}, \"eval-canonical-adaptive-k10-spatial-s43\": {}, \"eval-canonical-adaptive-k10-spatial-s44\": {}, \"eval-canonical-adaptive-k10-spatial-s48\": {}, \"eval-canonical-adaptive-k10-spatial-s49\": {}, \"eval-k10-tau025-spatial-s46\": {}, \"eval-pi05-adaptive-spatial-s42\": {}, \"eval-pi05-vla-only-goal-s43\": {}, \"eval-pi05-vla-only-spatial-s43\": {}, \"eval-pi05-vla-only-object-s42\": {}, \"eval-supp-long-vla-only-s42\": {}, \"eval-supp-long-adapt-tau025-s42\": {}, \"eval-k2-tau010-spatial-s42-r2\": {}, \"eval-pi05-vla-only-spatial-s45\": {}, \"eval-pi05-vla-only-object-s44\": {}, \"eval-k2-tau015-spatial-s42\": {}, \"eval-pi05-vla-only-goal-s42\": {}, \"eval-pi05-vla-only-spatial-s42\": {}, \"eval-supp-crm-norm005-goal-s48\": {}, \"eval-supp-crm-norm005-spatial-s49\": {}, \"eval-supp-crm-norm005-spatial-s48\": {}, \"eval-supp-long-vla-only-s43-r2\": {}, \"eval-supp-goal-vla-only-s42-bjb1\": {}, \"crm-norm005-goal-s49\": {}, \"eval-supp-obj-vla-only-s44\": {}, \"crm-norm005-object-s48\": {}, \"eval-supp-obj-vla-only-s43\": {}, \"eval-supp-obj-vla-only-s42\": {}, \"eval-supp-long-vla-only-s48\": {}, \"eval-supp-goal-vla-only-s50\": {}, \"eval-supp-goal-vla-only-s44\": {}, \"eval-supp-spatial-vla-only-smolvla-s42\": {}, \"eval-supp-goal-vla-only-s43\": {}, \"eval-supp-goal-vla-only-s42\": {}, \"train-crm-pi05-unified-3suite-r2\": {}, \"eval-supp-vla-only-spatial-s49\": {}, \"eval-supp-vla-only-spatial-s48\": {}, \"eval-supp-vla-only-obj-s49\": {}, \"eval-supp-vla-only-obj-s48\": {}, \"eval-supp-vla-only-goal-s49\": {}, \"eval-supp-vla-only-goal-s48\": {}, \"eval-k5-spatial-s42-sweep\": {}, \"eval-supp-long-vla-only-s43\": {}, \"eval-supp-goal-vla-only-s45\": {}, \"eval-supp-long-vla-only-s45\": {}, \"eval-supp-long-vla-only-s44\": {}, \"eval-supp-spatial-vla-only-s42\": {}, \"eval-pi05-vla-only-object-seed43-r4\": {}, \"eval-supp-obj-vla-only-s50\": {}, \"eval-supp-long-adapt-tau025-s47-r2\": {}, \"eval-supp-long-k2mean-s47-r2\": {}, \"eval-supp-spatial-reconvla-s47\": {}, \"eval-a1-baseline-object-s42\": {}, \"eval-supp-long-vla-only-s47-r4\": {}, \"eval-supp-obj-k2mean-s47-r2\": {}, \"eval-supp-obj-adapt-tau025-s47-r2\": {}, \"eval-supp-obj-crm-norm005-s47-r2\": {}, \"eval-supp-obj-vla-only-s47-r2\": {}, \"eval-supp-k2mean-spatial-s47\": {}, \"eval-supp-spatial-vla-only-s47\": {}, \"eval-supp-spatial-adapt-tau025-s47\": {}, \"eval-supp-adapt-tau025-spatial-s47\": {}, \"eval-supp-spatial-k2mean-s47\": {}, \"eval-supp-reconvla-spatial-s47\": {}, \"eval-supp-vla-only-spatial-s47\": {}, \"eval-supp-long-reconvla-s47\": {}, \"eval-supp-long-crm-norm005-s47\": {}, \"eval-supp-obj-k2mean-s47\": {}, \"eval-supp-obj-crm-norm005-s47\": {}, \"eval-supp-obj-adapt-tau025-s47\": {}, \"eval-supp-obj-vla-only-s47\": {}, \"eval-supp-goal-vla-only-s47-r3\": {}, \"eval-supp-long-k2mean-s47\": {}, \"eval-supp-long-adapt-tau025-s47\": {}, \"eval-supp-spatial-crm-norm005-s47\": {}, \"eval-supp-long-crm-norm005-s46\": {}, \"train-crm-pi05-unified-3suite\": {}, \"eval-openvla-object-vla-only-seed42-v3\": {}, \"eval-supp-vla-only-spatial-s46\": {}, \"eval-supp-adapt-tau025-spatial-s45\": {}, \"eval-supp-crm-norm005-spatial-s45\": {}, \"eval-supp-vla-only-spatial-s45\": {}, \"eval-supp-crm-norm005-spatial-s46\": {}, \"train-crm-pi05-spatial-k1\": {}, \"train-crm-pi05-goal-k1\": {}, \"eval-supp-goal-vla-only-s47-r2\": {}, \"eval-supp-long-vla-only-s47-r3\": {}, \"eval-supp-long-vla-only-s47-r2\": {}, \"eval-supp-goal-vla-only-s47\": {}, \"eval-supp-long-reconvla-s46\": {}, \"eval-supp-long-k2mean-s46\": {}, \"eval-supp-adapt-tau025-spatial-s46\": {}, \"eval-supp-long-adapt-tau025-s46\": {}, \"crm-train-openvla-k1-multiscale-object\": {}, \"eval-supp-long-k2mean-s46-r2\": {}, \"eval-supp-long-reconvla-s46-r2\": {}, \"eval-supp-long-crm-norm005-s46-r2\": {}, \"eval-supp-long-adapt-tau025-s46-r2\": {}, \"eval-supp-obj-crm-norm005-s45\": {}, \"eval-supp-obj-adapt-tau025-s45\": {}, \"eval-supp-obj-vla-only-s45\": {}, \"eval-supp-spatial-crm-norm005-s45\": {}, \"eval-supp-spatial-vla-only-s45\": {}, \"precompute-pi05-goal-2048-r2\": {}, \"eval-supp-long-vla-only-s46\": {}, \"precompute-pi05-spatial-2048-r2\": {}, \"precompute-smolvla-goal-bjb1-32546\": {}, \"eval-supp-goal-vla-only-s46\": {}, \"eval-supp-goal-reconvla-s46\": {}, \"crm-train-pi05-spatial-full\": {}, \"eval-obs-only-spatial-v2\": {}, \"eval-perdof-object-norm003-seed44\": {}, \"eval-random-selection-spatial-seed42\": {}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {}, \"eval-supp-goal-vla-only-wrapper-s44\": {}, \"eval-supp-long-reconvla-s45\": {}, \"eval-pi05-vla-only-long-seed42-r4\": {}, \"eval-pi05-vla-only-object-seed42\": {}, \"eval-pi05-vla-only-object-seed43\": {}, \"eval-pi05-vla-only-object-seed44\": {}, \"eval-supp-long-k2mean-s45\": {}, \"eval-supp-goal-k2mean-s46\": {}, \"eval-supp-goal-adapt-tau025-s46\": {}, \"eval-supp-goal-crm-norm005-s46\": {}, \"eval-supp-spatial-k2mean-s45\": {}, \"eval-supp-spatial-vla-only-s46\": {}, \"eval-supp-spatial-adapt-tau025-s46\": {}, \"eval-supp-spatial-crm-norm005-s46\": {}, \"eval-supp-long-crm-norm005-s45\": {}, \"eval-supp-long-adapt-tau025-s45\": {}, \"eval-supp-spatial-reconvla-s45\": {}, \"eval-supp-goal-k2mean-s45\": {}, \"eval-supp-adapt-tau025-obj-s45\": {}, \"eval-supp-obj-k2mean-s45\": {}, \"eval-supp-crm-obj-s46\": {}, \"eval-supp-long-k2mean-s44\": {}, \"eval-supp-long-reconvla-s44\": {}, \"eval-supp-goal-reconvla-s45\": {}, \"eval-supp-crm-norm005-obj-s46\": {}, \"eval-supp-goal-crm-norm005-s45\": {}, \"eval-supp-crm-norm005-obj-s45\": {}, \"eval-supp-reconvla-obj-s46\": {}, \"eval-supp-goal-adapt-tau025-s45\": {}, \"eval-supp-long-crm-norm005-s44\": {}, \"eval-supp-long-adapt-tau025-s44\": {}, \"eval-supp-k2mean-obj-s46\": {}, \"eval-supp-k2mean-obj-s45\": {}, \"eval-supp-adapt-tau025-obj-s46\": {}, \"eval-supp-long-k2mean-s42\": {}, \"eval-supp-obj-vla-only-s46\": {}, \"eval-supp-long-k2mean-s43\": {}, \"eval-supp-long-reconvla-s43\": {}, \"eval-supp-long-crm-norm005-s43\": {}, \"eval-supp-long-adapt-tau025-s43\": {}, \"eval-supp-obj-adapt-tau025-s45-r2\": {}, \"eval-supp-long-crm-norm005-s42\": {}, \"eval-supp-long-reconvla-s42\": {}, \"eval-ablation-tau040-goal-s42\": {}, \"eval-ablation-tau015-goal-s42\": {}, \"eval-supp-k2mean-object-s44\": {}, \"eval-ablation-tau010-goal-s42\": {}, \"eval-supp-obj-reconvla-s44\": {}, \"eval-supp-spatial-vla-only-s44\": {}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {}, \"eval-supp-k2mean-spatial-s44\": {}, \"eval-supp-spatial-vla-only-s43\": {}, \"eval-supp-k2mean-goal-s44\": {}, \"eval-supp-adapt-tau025-obj-s44\": {}, \"eval-supp-goal-reconvla-s44\": {}, \"eval-supp-obj-reconvla-s43\": {}, \"eval-supp-crm-norm005-goal-s44\": {}, \"eval-supp-k2mean-object-s43\": {}, \"eval-supp-k2mean-goal-s42-r2\": {}, \"eval-supp-adapt-tau025-goal-s44\": {}, \"eval-supp-crm-norm005-obj-s43\": {}, \"eval-supp-adapt-tau025-goal-s43\": {}, \"eval-supp-crm-norm005-goal-s43\": {}, \"eval-supp-adapt-tau025-obj-s43\": {}, \"eval-supp-goal-reconvla-s43\": {}, \"eval-supp-k2mean-spatial-s43\": {}, \"eval-supp-reconvla-spatial-s44\": {}, \"eval-supp-reconvla-spatial-s43\": {}, \"eval-supp-k2mean-goal-s43\": {}, \"eval-supp-k2mean-object-s42\": {}, \"eval-supp-goal-adapt-tau025-s42\": {}, \"eval-supp-goal-crm005-s42\": {}, \"eval-supp-goal-reconvla-s42\": {}, \"train-crm-unified-4suite-r6\": {}, \"eval-goal-vla-only-wrapper-s42\": {}, \"eval-supp-obj-adapt-tau025-s42\": {}, \"eval-supp-k2mean-spatial-s42\": {}, \"eval-supp-crm-norm005-spatial-s44\": {}, \"eval-supp-adapt-tau025-spatial-s44\": {}, \"eval-supp-reconvla-k2-spatial-s42\": {}, \"eval-supp-adapt-tau025-spatial-s43\": {}, \"eval-supp-crm-norm005-spatial-s43\": {}, \"eval-supp-k2mean-goal-s42\": {}, \"eval-supp-obj-adapt-s42-r2\": {}, \"eval-object-vla-only-wrapper-s44-r2\": {}, \"eval-object-vla-only-wrapper-s43-r2\": {}, \"eval-object-vla-only-wrapper-s42-r2\": {}, \"eval-supp-obj-reconvla-s42\": {}, \"eval-supp-obj-crm005-s42-r2\": {}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {}, \"eval-supp-crm-norm02-spatial-s42-r2\": {}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {}, \"eval-openvla-object-baseline-seed42-r2\": {}, \"eval-obs-only-object-norm02-seed55\": {}, \"precompute-pi05-features-object\": {}, \"precompute-smolvla-goal-shard2\": {}, \"precompute-smolvla-goal-shard1\": {}, \"precompute-smolvla-goal-shard0\": {}, \"eval-smolvla-long-seed2\": {}, \"eval-smolvla-long-seed1\": {}, \"eval-smolvla-long-seed0\": {}, \"eval-smolvla-crm-spatial-seed42-v1\": {}, \"eval-smolvla-crm-spatial-seed43-v1\": {}, \"eval-smolvla-crm-spatial-seed44-v1\": {}, \"eval-smolvla-crm-goal-seed42-v1\": {}, \"eval-smolvla-crm-goal-seed43-v1\": {}, \"eval-smolvla-crm-goal-seed44-v1\": {}, \"eval-supp-obj-adapt-s42\": {}, \"eval-crm-norm02-spatial-s42\": {}, \"eval-adaptive-tau015-spatial-s42\": {}, \"eval-adaptive-tau025-spatial-s42\": {}, \"eval-adaptive-tau035-spatial-s42\": {}, \"train-crm-unified-4suite-r5-resumed\": {}, \"eval-object-vla-only-wrapper-s44\": {}, \"eval-object-vla-only-wrapper-s43\": {}, \"eval-object-vla-only-wrapper-s42\": {}, \"eval-supp-obj-crm005-s42\": {}, \"eval-supp-adapt-tau035-spatial-s42\": {}, \"eval-supp-adapt-tau025-spatial-s42\": {}, \"eval-supp-adapt-tau015-spatial-s42\": {}, \"eval-supp-crm-norm02-spatial-s42\": {}, \"eval-3dir-adaptive-spatial-s42\": {}, \"eval-3dir-norm03-spatial-s42\": {}, \"eval-3dir-reconvla-spatial-s42\": {}, \"eval-3dir-norm01-spatial-s42\": {}, \"eval-3dir-norm005-spatial-s42\": {}, \"precompute-pi05-goal-2048\": {}, \"precompute-pi05-spatial-2048\": {}, \"precompute-pi05-object-2048\": {}, \"eval-smolvla-crm-object-seed43-v1\": {}, \"eval-smolvla-crm-object-seed42-v1\": {}, \"eval-smolvla-crm-object-seed44-v1\": {}, \"train-crm-unified-4suite-r5\": {}, \"eval-smolvla-crm-goal-seed43\": {}, \"eval-smolvla-crm-goal-seed42\": {}, \"eval-smolvla-crm-spatial-seed44\": {}, \"eval-smolvla-crm-spatial-seed43\": {}, \"eval-smolvla-crm-spatial-seed42\": {}, \"precompute-pi05-long-2048\": {}, \"eval-smolvla-lerobot-goal-seed44-v3\": {}, \"train-crm-smolvla-3suite-v1\": {}, \"eval-smolvla-lerobot-goal-seed43-v2\": {}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {}, \"eval-smolvla-lerobot-object-seed44-v2\": {}, \"eval-smolvla-lerobot-object-seed43-v2\": {}, \"eval-smolvla-lerobot-goal-seed43\": {}, \"eval-smolvla-lerobot-spatial-seed43\": {}, \"eval-smolvla-lerobot-object-seed44\": {}, \"eval-smolvla-lerobot-object-seed43\": {}, \"eval-smolvla-lerobot-spatial-seed44\": {}, \"precompute-smolvla-long-wrapper-bjb1\": {}, \"eval-smolvla-lerobot-long-seed44\": {}, \"eval-smolvla-lerobot-long-seed43\": {}, \"eval-smolvla-lerobot-long-seed42\": {}, \"train-crm-unified-4suite-r4\": {}, \"eval-pi05-vla-only-long-seed42-r4-rerun\": {}, \"eval-pi05-crm-object-seed44\": {}, \"eval-pi05-crm-object-seed43\": {}, \"eval-pi05-crm-object-seed42\": {}, \"eval-pi05-vla-only-long-seed43-r4-std\": {}, \"eval-pi05-vla-only-goal-seed44-r4-std\": {}, \"eval-pi05-vla-only-goal-seed42-r4-std\": {}, \"eval-pi05-vla-only-long-seed44-r4-std\": {}, \"eval-pi05-vla-only-goal-seed43-r4-std\": {}, \"eval-pi05-vla-only-goal-seed42-r4\": {}, \"precompute-smolvla-long-k2\": {}, \"train-crm-unified-4suite-r3\": {}, \"train-crm-unified-4suite-r2\": {}, \"precompute-smolvla-goal-bjb2-28827\": {}, \"precompute-smolvla-long-bjb2-28827\": {}, \"eval-pi05-vla-only-spatial-seed44-r4\": {}, \"eval-pi05-vla-only-spatial-seed43-r4\": {}, \"eval-pi05-vla-only-spatial-seed42-r4\": {}, \"eval-pi05-vla-only-long-seed44-r4\": {}, \"eval-pi05-vla-only-long-seed43-r4\": {}, \"eval-pi05-vla-only-goal-seed44-r4\": {}, \"eval-pi05-vla-only-goal-seed43-r4\": {}, \"eval-openvla-oft-official-object\": {}, \"eval-pi05-crm-spatial-seed44\": {}, \"eval-pi05-crm-spatial-seed43\": {}, \"eval-pi05-crm-spatial-seed42\": {}, \"eval-pi05-vla-only-object-seed44-r4\": {}, \"eval-smolvla-lerobot-official-object\": {}, \"eval-pi05-vla-only-object-seed42-r4\": {}, \"train-crm-unified-4suite\": {}, \"precompute-smolvla-long-bjb1-32546-r2\": {}, \"precompute-smolvla-long-bjb1-32546\": {}, \"eval-loss-perdof-object-seed42\": {}, \"eval-loss-combined-object-seed42\": {}, \"eval-loss-conformal-object-seed42\": {}, \"eval-loss-mse-object-seed42\": {}, \"eval-openvla-oft-object-baseline-seed42\": {}, \"precompute-smolvla-long-bjb1-18228\": {}, \"crm-loss-combined\": {}, \"crm-loss-conformal\": {}, \"precompute-smolvla-goal-bjb1-18228\": {}, \"crm-loss-perdof\": {}, \"crm-loss-mse-baseline\": {}, \"eval-smolvla-acr-goal-seed43\": {}, \"eval-smolvla-crm-long-seed44-v2\": {}, \"eval-smolvla-crm-goal-seed44-v2\": {}, \"eval-smolvla-crm-long-seed43-v2\": {}, \"eval-smolvla-acr-long-seed42\": {}, \"eval-smolvla-acr-goal-seed42\": {}, \"crm-train-pi05-spatial-v2\": {}, \"crm-train-pi05-object-full\": {}, \"crm-train-pi05-spatial\": {}, \"crm-train-pi05-object\": {}, \"eval-pi05-vla-only-spatial-seed45\": {}, \"eval-pi05-vla-only-spatial-seed43-r3\": {}, \"eval-pi05-vla-only-spatial-seed42-r3\": {}, \"eval-pi05-vla-only-object-seed44-r3\": {}, \"eval-pi05-vla-only-object-seed43-r3\": {}, \"eval-pi05-vla-only-object-seed42-r3\": {}, \"eval-spatial-obs-only-seed45\": {}, \"eval-pi05-vla-only-spatial-seed44\": {}, \"eval-pi05-vla-only-spatial-seed43\": {}, \"eval-pi05-vla-only-spatial-seed42\": {}, \"eval-k20-obs-only-spatial-seed44\": {}, \"eval-k20-obs-only-spatial-seed43\": {}, \"eval-k20-obs-only-spatial-seed42\": {}, \"eval-k20-obs-only-object-seed45\": {}, \"eval-obs-only-object-norm003-seed66\": {}, \"eval-obs-only-object-norm01-seed66\": {}, \"eval-obs-only-object-norm005-seed66\": {}, \"eval-obs-only-object-norm003-seed67\": {}, \"eval-k20-obs-only-object-seed44\": {}, \"eval-k20-obs-only-object-seed43\": {}, \"eval-k20-obs-only-object-seed42\": {}, \"eval-crm-object-k20-seed44\": {}, \"eval-crm-object-k20-seed42\": {}, \"eval-obs-only-object-norm02-seed53\": {}, \"eval-obs-only-object-norm02-seed52\": {}, \"eval-obs-only-object-norm02-seed51\": {}, \"eval-obs-only-object-norm02-seed50\": {}, \"eval-obs-only-object-norm02-seed48-r2\": {}, \"eval-obs-only-object-norm02-seed47\": {}, \"eval-obs-only-object-norm02-seed46\": {}, \"eval-obs-only-object-norm02-seed45\": {}, \"eval-obs-only-object-norm02-seed44-r2\": {}, \"eval-obs-only-object-norm02-seed43-r3\": {}, \"eval-obs-only-object-norm02-seed43-r2\": {}, \"eval-obs-only-object-norm005-seed67\": {}, \"eval-obs-only-object-norm01-seed67\": {}, \"eval-vla-only-object-seed50\": {}, \"eval-vla-only-object-seed49\": {}, \"eval-vla-only-object-seed48\": {}, \"eval-vla-only-object-seed46\": {}, \"eval-vla-only-object-seed45\": {}, \"eval-vla-only-object-seed44-r2\": {}, \"eval-plan-a-object-seed42\": {}, \"eval-vla-only-object-seed43\": {}, \"eval-vla-only-object\": {}, \"eval-plan-a-spatial-seed43\": {}, \"eval-plan-a-object-seed44\": {}, \"eval-plan-a-spatial-seed42\": {}, \"eval-plan-a-spatial-seed44\": {}, \"eval-plan-a-object-seed43\": {}, \"eval-random-selection-object-seed44\": {}, \"eval-random-selection-object-seed43\": {}, \"eval-obs-only-object-norm01-seed60\": {}, \"eval-pi05-baseline-object-seed42\": {}, \"eval-obs-only-object-norm01-seed54\": {}, \"eval-obs-only-object-norm01-seed53\": {}, \"eval-obs-only-object-norm01-seed52\": {}, \"eval-obs-only-object-norm01-seed50\": {}, \"eval-obs-only-object-norm01-seed49\": {}, \"eval-obs-only-object-norm01-seed48\": {}, \"eval-obs-only-object-norm01-seed47\": {}, \"eval-obs-only-object-norm01-seed45-r2\": {}, \"eval-obs-only-object-norm01-seed44\": {}, \"eval-obs-only-object-norm005-seed55\": {}, \"eval-obs-only-object-norm005-seed50\": {}, \"eval-obs-only-object-norm005-seed49\": {}, \"eval-obs-only-object-norm005-seed48\": {}, \"eval-obs-only-object-norm005-seed47\": {}, \"eval-obs-only-object-norm005-seed44\": {}, \"eval-obs-only-object-norm005-seed43-r2\": {}, \"eval-obs-only-object-norm005-seed43\": {}, \"eval-obs-only-object-norm003-seed48\": {}, \"eval-obs-only-object-norm003-seed47-r2\": {}, \"eval-obs-only-object-norm003-seed46\": {}, \"eval-obs-only-object-norm003-seed45\": {}, \"eval-obs-only-object-norm003-seed44-bjb2\": {}, \"eval-obs-only-object-norm003-seed44\": {}, \"eval-obs-only-object-norm003-seed43-r2\": {}, \"eval-obs-only-object-norm003-seed43\": {}, \"eval-obs-only-object-norm01-seed57\": {}, \"eval-obs-only-object-norm005-seed65\": {}, \"eval-obs-only-object-norm005-seed61\": {}, \"eval-obs-only-object-norm005-seed58\": {}, \"eval-obs-only-object-norm003-seed59\": {}, \"eval-obs-only-object-norm003-seed56\": {}, \"eval-obs-only-object-norm005-seed75\": {}, \"eval-obs-only-object-norm01-seed74\": {}, \"eval-obs-only-object-norm005-seed72\": {}, \"eval-obs-only-object-norm003-seed63-r2\": {}, \"eval-obs-only-object-norm01-seed71\": {}, \"eval-obs-only-object-norm003-seed62-r2\": {}, \"eval-obs-only-object-norm003-seed73\": {}, \"eval-obs-only-object-norm01-seed51-r3\": {}, \"eval-obs-only-object-norm01-seed52-r3\": {}, \"eval-obs-only-object-norm01-seed65\": {}, \"eval-obs-only-object-norm01-seed64\": {}, \"eval-obs-only-object-norm005-seed64\": {}, \"eval-obs-only-object-norm003-seed65\": {}, \"eval-obs-only-object-norm003-seed64\": {}, \"eval-obs-only-object-norm005-seed62\": {}, \"eval-obs-only-object-norm005-seed63\": {}, \"eval-obs-only-object-norm01-seed61\": {}, \"eval-obs-only-object-norm003-seed64-bjb2\": {}, \"eval-obs-only-object-norm003-seed63\": {}, \"eval-obs-only-object-norm003-seed62\": {}, \"eval-obs-only-object-norm01-seed51-r2\": {}, \"eval-obs-only-object-norm01-seed52-r2\": {}, \"eval-obs-only-object-norm01-seed51\": {}, \"eval-obs-only-object-norm005-seed49-r2\": {}, \"eval-obs-only-object-norm005-seed55-r2\": {}, \"eval-openvla-crm-object-seed42\": {}, \"eval-obs-only-object-norm003-seed44-r2\": {}, \"eval-random-selection-object-seed49\": {}, \"eval-random-selection-object-seed48\": {}, \"eval-k5-obs-only-object-seed44\": {}, \"eval-obs-only-spatial-norm02-seed52\": {}, \"eval-obs-only-object-norm02-seed54\": {}, \"D088-eval-adaptive-unc-head-object-seed44\": {}, \"D088-eval-adaptive-unc-head-object-seed43\": {}, \"D088-eval-adaptive-unc-head-object-seed42\": {}, \"eval-adaptive-unc-head-object-seed42\": {}, \"eval-adaptive-unc-head-object-seed43\": {}, \"eval-perdof-object-norm02-seed50\": {}, \"eval-adaptive-unc-head-object-seed44\": {}, \"eval-random-selection-spatial-seed42-r3\": {}, \"eval-obs-only-spatial-norm02-seed50\": {}, \"train-crm-openvla-obs-only\": {}, \"openvla-precompute-k1\": {}, \"eval-random-selection-object-seed46-r3\": {}, \"eval-perdof-object-norm02-seed49\": {}, \"eval-random-selection-object-seed47\": {}, \"eval-obs-only-spatial-norm02-seed42-r2\": {}, \"eval-k5-obs-only-object-seed43\": {}, \"eval-random-selection-spatial-seed43-r2\": {}, \"eval-random-selection-spatial-seed44\": {}, \"eval-crm-k1-object-seed43-plan702\": {}, \"eval-crm-k1-object-seed42-plan702\": {}, \"eval-crm-k1-object-seed44-plan702\": {}, \"eval-random-selection-object-seed46-r2\": {}, \"eval-random-selection-spatial-seed43\": {}, \"eval-random-selection-object-seed46\": {}, \"eval-obs-only-spatial-seed48\": {}, \"eval-vla-only-spatial-seed48\": {}, \"eval-obs-only-spatial-norm02-seed42\": {}, \"eval-obs-only-spatial-norm02-seed49\": {}, \"eval-adaptive-k-spatial-p90-seed44\": {}, \"eval-argmin-object-seed50\": {}, \"eval-vla-only-object-seed48-r2\": {}, \"eval-vla-only-goal-seed51\": {}, \"eval-random-selection-spatial-seed42-r2\": {}, \"eval-random-selection-object-seed45\": {}, \"eval-crm-k1-object-seed44-plan702-r2\": {}, \"eval-crm-k1-object-seed43-plan702-r2\": {}, \"eval-crm-k1-object-seed42-plan702-r2\": {}, \"eval-perdof-object-norm02-seed48\": {}, \"eval-argmin-object-k5-seed44-r2\": {}, \"eval-vla-only-goal-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-seed46-r2\": {}, \"eval-latency-profiling-v1\": {}, \"eval-adaptive-k-spatial-p75-seed44\": {}, \"eval-obs-only-goal-norm02-seed51\": {}, \"eval-adaptive-k-spatial-p25-seed44\": {}, \"eval-openvla-object-baseline-seed42\": {}, \"eval-argmin-object-seed49\": {}, \"eval-argmin-object-seed48\": {}, \"eval-obs-only-spatial-norm02-seed48\": {}, \"eval-obs-only-goal-norm02-seed52\": {}, \"eval-adaptive-k-spatial-p90-seed43\": {}, \"eval-perdof-object-norm02-seed45-r3\": {}, \"eval-adaptive-k-spatial-p90-seed42\": {}, \"eval-obs-only-object-norm02-seed49\": {}, \"eval-vla-only-goal-seed47\": {}, \"eval-adaptive-k-spatial-p50-seed44\": {}, \"eval-adaptive-k-spatial-p50-seed43\": {}, \"eval-adaptive-k-spatial-p50-seed42\": {}, \"eval-adaptive-k-spatial-p25-seed42\": {}, \"eval-adaptive-k-spatial-p25-seed43\": {}, \"eval-adaptive-k-spatial-p75-seed43\": {}, \"eval-crm-object-k20-seed43\": {}, \"eval-vla-only-long-seed49-r2\": {}, \"eval-adaptive-k-spatial-p75-seed42\": {}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {}, \"eval-adaptive-k-p75-seed42\": {}, \"eval-adaptive-k-p75-seed43\": {}, \"eval-adaptive-k-p50-seed42\": {}, \"eval-adaptive-k-p50-seed43\": {}, \"eval-random-selection-object-seed42\": {}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {}, \"eval-obs-only-object-norm02-seed42\": {}, \"latency-profile-n1000\": {}, \"eval-adaptive-k-p90-seed44\": {}, \"eval-adaptive-k-p25-seed43\": {}, \"eval-crm-spatial-k10-seed51\": {}, \"eval-vla-only-goal-seed49\": {}, \"eval-vla-only-long-seed52\": {}, \"eval-vla-only-long-seed51\": {}, \"eval-vla-only-long-seed50\": {}, \"eval-crm-long-seed50\": {}, \"eval-adaptive-k-p25-seed44-r2\": {}, \"calibrate-crm-correction-signal\": {}, \"eval-adaptive-k-p25-seed42\": {}, \"eval-vla-only-goal-seed48-r2\": {}, \"eval-vla-only-goal-seed47-r2\": {}, \"eval-crm-goal-seed46\": {}, \"eval-adaptive-k-p50-seed44\": {}, \"eval-adaptive-k-p75-seed44\": {}, \"eval-adaptive-k-p90-seed43\": {}, \"eval-adaptive-k-p90-seed42\": {}, \"eval-vla-only-spatial-seed47\": {}, \"eval-crm-long-seed47\": {}, \"eval-vla-only-long-seed48\": {}, \"eval-crm-long-seed46\": {}, \"eval-crm-goal-seed45-r2\": {}, \"eval-crm-goal-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-seed43-r2\": {}, \"k2-l2-calibration-phase1\": {}, \"eval-crm-long-seed45\": {}, \"eval-vla-only-spatial-seed49\": {}, \"eval-vla-only-goal-seed48\": {}, \"eval-vla-only-goal-seed43\": {}, \"eval-vla-only-goal-seed42\": {}, \"eval-vla-only-object-seed47\": {}, \"eval-crm-long-seed44\": {}, \"eval-crm-long-seed43\": {}, \"eval-crm-long-seed42\": {}, \"eval-crm-goal-seed42\": {}, \"eval-crm-goal-seed43\": {}, \"eval-vla-only-spatial-seed46\": {}, \"eval-vla-only-long-seed47\": {}, \"eval-crm-goal-seed45\": {}, \"eval-crm-goal-seed44\": {}, \"eval-vla-only-goal-seed45\": {}, \"eval-vla-only-goal-seed46\": {}, \"eval-vla-only-long-seed46\": {}, \"fmvd-calibration-phase1\": {}, \"eval-vla-only-long-seed45\": {}, \"eval-perdof-object-norm003-seed47\": {}, \"eval-perdof-object-norm005-seed47\": {}, \"eval-vla-only-long-seed44\": {}, \"eval-vla-only-long-seed42\": {}, \"eval-vla-only-long-seed43\": {}, \"eval-obs-only-spatial-norm02-seed43\": {}, \"eval-obs-only-spatial-norm02-seed47\": {}, \"eval-obs-only-spatial-norm02-seed46\": {}, \"eval-argmin-object-k5-seed44\": {}, \"eval-vla-only-goal-seed44\": {}, \"eval-random-selection-object-k5-seed45-r2\": {}, \"eval-random-selection-object-k5-seed44-r2\": {}, \"eval-random-selection-object-k5-seed43-r2\": {}, \"eval-random-selection-object-k5-seed42-r2\": {}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {}, \"plan_602-latency-profiling\": {}, \"eval-vla-only-spatial-seed45\": {}, \"eval-perdof-object-norm005-seed45-r2\": {}, \"eval-vla-only-spatial-seed44\": {}, \"eval-obs-only-object-default-seed48-r2\": {}, \"eval-vla-only-spatial-seed43\": {}, \"eval-vla-only-spatial-seed42\": {}, \"eval-obs-only-spatial-norm02-k5-seed45\": {}, \"eval-obs-only-spatial-norm02-k5-seed44\": {}, \"eval-random-selection-object-k5-seed45\": {}, \"eval-random-selection-object-k5-seed44\": {}, \"eval-random-selection-object-k5-seed43\": {}, \"eval-random-selection-object-k5-seed42\": {}, \"eval-obs-only-spatial-norm02-seed44\": {}, \"eval-perdof-object-norm01-seed43\": {}, \"eval-obs-only-object-default-seed45-r2\": {}, \"eval-argmin-object-k5-seed42\": {}, \"eval-argmin-object-k5-seed45\": {}, \"eval-argmin-object-k5-seed43\": {}, \"eval-perdof-object-norm03-seed43\": {}, \"eval-obs-only-spatial-norm02-seed45\": {}, \"train-crm-k1-accg-object-seed42-full\": {}, \"plan_701-precompute-k1-spatial\": {}, \"plan_701-crm-k1-train\": {}, \"eval_obs_only_norm03_seed48\": {}, \"eval_obs_only_norm01_seed48\": {}, \"eval-lto-splitA-vla-only-r3\": {}, \"eval-lto-splitA-vla-only-r2\": {}, \"eval-lto-splitA-heldout-r2\": {}, \"crm-lto-splitA-train\": {}, \"eval-perdof-object-norm003-seed48\": {}, \"eval-scalar-object-seed45-r2\": {}, \"eval-obs-only-spatial-norm02-k5-seed43\": {}, \"eval-obs-only-object-norm02-k5-seed48\": {}, \"eval-obs-only-spatial-norm02-k5-seed42\": {}, \"eval-obs-only-object-norm02-k5-seed46\": {}, \"eval-lto-splitA-vla-only-v2\": {}, \"eval-lto-splitA-heldout-v2\": {}, \"eval-perdof-object-default-seed47\": {}, \"eval-perdof-object-norm03-seed47\": {}, \"eval-obs-only-object-default-seed48\": {}, \"eval-perdof-object-norm003-seed46\": {}, \"eval-perdof-object-norm005-seed46\": {}, \"eval-perdof-object-norm003-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed47\": {}, \"eval-perdof-object-norm01-seed48\": {}, \"eval-obs-only-object-default-seed47\": {}, \"eval-perdof-object-norm03-seed46\": {}, \"eval-obs-only-object-norm03-seed46\": {}, \"eval-scalar-object-seed46\": {}, \"eval-obs-only-object-norm003-seed45-r2\": {}, \"eval-lto-splitA-vla-only\": {}, \"eval-lto-splitA-heldout\": {}, \"eval-obs-only-object-norm005-seed46\": {}, \"eval-perdof-object-norm03-seed48\": {}, \"eval-obs-only-object-norm003-seed49\": {}, \"crm-lto-splitA-train-fixed\": {}, \"eval-obs-only-object-norm003-seed47\": {}, \"eval-perdof-object-norm003-seed43\": {}, \"eval-perdof-object-norm005-seed43\": {}, \"eval-perdof-object-default-seed43\": {}, \"eval-perdof-object-default-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed45\": {}, \"eval-perdof-object-norm005-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed44\": {}, \"eval-perdof-object-norm003-seed44-r2\": {}, \"eval-obs-only-object-norm01-seed46-r3\": {}, \"eval-perdof-object-norm005-seed44\": {}, \"eval-vla-only-object-seed45-r2\": {}, \"eval-obs-only-object-norm03-seed48\": {}, \"eval-obs-only-object-norm02-k5-seed43\": {}, \"eval-perdof-object-norm01-seed42-r2\": {}, \"eval-obs-only-object-norm01-seed42-r2\": {}, \"eval-perdof-object-norm02-seed43\": {}, \"eval-perdof-object-norm01-seed46\": {}, \"eval-obs-only-object-norm01-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed42\": {}, \"eval-perdof-object-default-seed46\": {}, \"eval-perdof-object-default-seed44\": {}, \"eval-mag-perdof-norm02\": {}, \"eval-acr-spatial-v4-scalar\": {}, \"eval-acr-spatial-v4-small\": {}, \"eval-acr-spatial-v4-obs-only-r2\": {}, \"eval-argmin-only-spatial\": {}, \"eval-acr-spatial-v3\": {}, \"eval-acr-object-v3\": {}, \"eval-openvla-object-vla-only-seed42\": {}, \"eval-perdof-object-norm02-seed47\": {}, \"eval-obs-only-object-norm02-seed48\": {}, \"eval-obs-only-object-default-seed46\": {}, \"eval-perdof-object-norm02-seed46\": {}, \"eval-obs-only-object-norm01-seed46\": {}, \"mag_obs_only_norm01_seed47\": {}, \"mag_obs_only_norm01_seed46\": {}, \"eval-perdof-object-norm02-seed43-r3\": {}, \"mag_perdof_norm02_seed43_r3\": {}, \"eval-perdof-object-norm01-seed47-bjb1\": {}, \"eval-openvla-object-vla-only-seed42-v2\": {}, \"eval-k1-crm-multiscale-object-seed44-r2\": {}, \"eval-k1-crm-multiscale-object-seed44\": {}, \"eval-k1-crm-multiscale-object-seed43\": {}, \"eval-k1-crm-multiscale-object-seed42\": {}, \"eval-perdof-object-norm01-seed46-r2\": {}, \"eval-k1-crm-multiscale-object-seed43-r2\": {}, \"eval-perdof-object-norm02-seed45-r2\": {}, \"eval-obs-only-object-norm005-seed43-r3\": {}, \"plan_602-latency-profile\": {}, \"train-crm-k1-accg-object-seed42-v2\": {}, \"eval-k1-crm-accg-object-seed44\": {}, \"eval-k1-crm-accg-object-seed43\": {}, \"eval-k1-crm-accg-object-seed42\": {}, \"eval-obs-only-object-default-seed45\": {}, \"eval-scalar-object-seed45\": {}, \"eval-perdof-object-norm02-seed45\": {}, \"eval-perdof-object-norm02-seed44\": {}, \"train-crm-k1-accg-object-seed42-fallback\": {}, \"train-crm-k1-accg-object-seed42\": {}, \"eval-perdof-object-norm02-seed45-deploy\": {}, \"eval-obs-only-object-norm01-seed47-r2\": {}, \"eval-perdof-object-norm03-seed45-r2\": {}, \"eval-perdof-object-norm03-seed44-r2\": {}, \"eval-obs-only-object-norm03-seed47\": {}, \"eval-perdof-object-norm03-seed46-r2\": {}, \"eval-perdof-object-norm01-seed44\": {}, \"eval-obs-only-object-norm01-seed47-bjb2\": {}, \"eval-obs-only-object-norm01-seed46-bjb2\": {}, \"eval-argmin-object-seed47\": {}, \"eval-perdof-object-norm01-seed45\": {}, \"eval-perdof-object-norm01-seed47\": {}, \"eval-argmin-object-seed46\": {}, \"eval-obs-only-object-norm03-seed45-r2\": {}, \"eval-vla-mean-object-seed45\": {}, \"eval-argmin-object-seed45\": {}, \"eval-direct-correction-object-seed42-r3\": {}, \"eval-perdof-object-norm03-seed44\": {}, \"eval-mag-perdof-norm02-object\": {}, \"eval-acr-object-v4-scalar\": {}, \"eval-mag-obsonly-norm02\": {}, \"eval-mag-perdof-norm03\": {}, \"eval-mag-perdof-norm005\": {}, \"eval-mag-perdof-norm003\": {}, \"eval-vla-mean-spatial\": {}, \"eval-acr-object-obs-only-norm02\": {}, \"eval-spatial-v7-full\": {}, \"eval-object-v8-full\": {}, \"precompute-v5-shard2\": {}, \"precompute-v5-shard1\": {}, \"precompute-v5-shard0\": {}, \"precompute-v4-shard2\": {}, \"precompute-v4-shard1\": {}, \"precompute-v4-shard0\": {}, \"eval-vla-mean-spatial-t10\": {}, \"eval-reconvla-spatial-v3\": {}, \"crm-train-v2-scalar-unc\": {}, \"crm-train-v2-perdof\": {}, \"crm-train-v2-obs-only\": {}, \"precompute-shard2\": {}, \"precompute-shard1\": {}, \"precompute-shard0\": {}, \"precompute-k5\": {}, \"plan_014-reconvla-baseline\": {}, \"plan_001-crm-smolvla\": {}, \"mvp-point-reaching\": {}, \"eval-smolvla-libero-spatial\": {}, \"eval-obs-only-spatial\": {}, \"eval-obs-only-object-default-seed44\": {}, \"eval-mag-perdof-norm005-object\": {}, \"eval-mag-perdof-norm02-seed43-object-r3\": {}, \"eval-mag-perdof-norm03-object-r3\": {}, \"eval-mag-obsonly-norm005\": {}, \"eval-mag-obsonly-norm003-b2\": {}, \"eval-mag-obsonly-norm03-object\": {}, \"eval-mag-obsonly-norm005-object\": {}, \"eval-direct-correction-object-seed42-r2\": {}, \"eval-direct-correction-object-seed42\": {}, \"eval-scalar-object-seed44-r2\": {}, \"eval-perdof-object-seed44\": {}, \"eval-obs-only-object-norm03-seed44\": {}, \"eval-vla-mean-object-seed44\": {}, \"eval-obs-only-object-norm02-seed44-r4\": {}, \"eval-argmin-object-seed44-r2\": {}, \"eval-obs-only-object-norm03-seed45\": {}, \"eval-acr-object-v4-default-r2\": {}, \"eval-mag-perdof-norm003-object\": {}, \"eval-acr-object-obs-only-default\": {}, \"eval-scalar-object-seed43\": {}, \"eval-mag-obsonly-norm003-object\": {}, \"eval-scalar-object-seed44\": {}, \"eval-obs-only-object-norm02-seed44-r3\": {}, \"eval-argmin-object-seed44-r3\": {}, \"eval-vla-mean-object-seed43\": {}, \"eval-perdof-object-seed43\": {}, \"eval-vla-only-object-seed44\": {}, \"eval-obs-only-object-norm02-seed44\": {}, \"eval-argmin-object-seed44\": {}, \"eval-obs-only-object-seed43\": {}, \"eval-mag-obsonly-norm03-b2\": {}, \"eval-argmin-object-seed43\": {}, \"eval-mag-perdof-norm02-seed43-object-r2\": {}, \"eval-mag-obsonly-norm03\": {}, \"eval-mag-obsonly-norm02-object\": {}, \"eval-mag-obsonly-norm03-b4\": {}, \"eval-mag-obsonly-norm03-b3\": {}, \"eval-mag-perdof-norm02-seed43-object\": {}, \"eval-mag-perdof-norm03-object-r2\": {}, \"eval-acr-object-v4-scalar-b2\": {}, \"eval-acr-object-v4-obs-only-b2\": {}, \"eval-spatial-v4-full\": {}, \"eval-reconvla-spatial-v1\": {}, \"eval-object-v6-full\": {}, \"precompute-v3-shard2\": {}, \"precompute-v3-shard1\": {}, \"precompute-v3-shard0\": {}, \"precompute-v2-shard2\": {}, \"precompute-v2-shard1\": {}, \"precompute-v2-shard0\": {}, \"eval-mag-perdof-norm0p3-object-r2\": {}, \"eval-mag-perdof-norm0p3-object\": {}, \"eval-obs-only-object-norm02-seed43\": {}, \"eval-acr-object-v4-default\": {}, \"eval-mag-obsonly-norm03-r2\": {}, \"eval-vla-mean-object\": {}, \"eval-reconvla-object\": {}, \"eval-acr-object-v4-obs-only\": {}, \"eval-acr-object-v4-perdof\": {}, \"eval-acr-spatial-v4-scalar-r2\": {}, \"eval-acr-spatial-v4-obs-only-r3\": {}, \"eval-obs-only-spatial-seed43\": {}, \"eval-acr-spatial-v4-small-r2\": {}, \"eval-mag-obsonly-norm-0.3-r3\": {}, \"eval-mag-obsonly-norm-0p3-r3\": {}, \"eval-argmin-only-spatial-r2\": {}, \"eval-mag-obsonly-norm003\": {}, \"eval-vla-only-object-k1\": {}, \"eval-acr-spatial-v4-default-r3\": {}, \"eval-tiny-correction-spatial\": {}, \"eval-acr-spatial-v4-default-r2\": {}, \"eval-acr-spatial-v4-obs-only\": {}, \"eval-acr-spatial-v4-default\": {}, \"crm-train-v3-norm-scalar-unc\": {}, \"crm-train-v3-norm-obs-only\": {}, \"crm-train-v3-norm\": {}, \"crm-train-v3-scalar-unc\": {}, \"crm-train-v3-obs-only\": {}, \"crm-train-v3-perdof\": {}, \"eval-obs-only-spatial-v3\": {}, \"eval-scalar-unc-spatial-v2\": {}, \"crm-train-a4-scalar-unc\": {}, \"crm-train-a3-obs-only\": {}, \"crm-train-v1\": {}, \"crm-train-k5\": {}, \"eval-scalar-unc-spatial\": {}, \"eval-acr-spatial-v2\": {}, \"eval-k5-spatial\": {}, \"eval-object-v7-full\": {}, \"eval-spatial-v6-full\": {}, \"eval-object-v5-full\": {}, \"eval-acr-vla-spatial-v1\": {}, \"eval-acr-spatial-v1\": {}, \"eval-reconvla-spatial-v2\": {}, \"eval-object-v4-full\": {}, \"eval-spatial-v5-full\": {}, \"eval-spatial-v3-full\": {}, \"eval-spatial-reeval-v2\": {}}, \"count\": 1223, \"total\": 1223, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.5652}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "f04f4734-a932-4dac-b195-9c4e29565c17",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"smolvla-tau020-long-s42\\\": {}, \\\"smolvla-tau015-spatial-s42-fix\\\": {}, \\\"crm-always-on-long-s45\\\": {}, \\\"pi05-crm-always-on-object-s43\\\": {}, \\\"smolvla-tau045-long-s42\\\": {}, \\\"smolvla-tau040-long-s42\\\": {}, \\\"pi05-crm-always-on-object-s42\\\": {}, \\\"pi05-crm-always-on-goal-s42\\\": {}, \\\"smolvla-tau020-long-s43-r2\\\": {}, \\\"eval-tau005-spatial-s42\\\": {}, \\\"pi05-crm-always-on-spatial-s42\\\": {}, \\\"eval-tau040-spatial-s42\\\": {}, \\\"eval-tau045-spatial-s42\\\": {}, \\\"crm-always-on-object-s46\\\": {}, \\\"smolvla-tau005-long-s42\\\": {}, \\\"crm-always-on-object-s45\\\": {}, \\\"smolvla-tau010-long-s42\\\": {}, \\\"pi05-tau-sweep-goal-tau070-s42-r2\\\": {}, \\\"pi05-tau-sweep-goal-tau050-s42-r2\\\": {}, \\\"pi05-goal-tau035-s43-r3\\\": {}, \\\"crm-always-on-long-s44\\\": {}, \\\"crm-always-on-spatial-s46\\\": {}, \\\"crm-always-on-goal-s46\\\": {}, \\\"crm-always-on-goal-s45\\\": {}, \\\"crm-always-on-spatial-s45\\\": {}, \\\"pi05-goal-tau025-s43-r3\\\": {}, \\\"pi05-tau-sweep-goal-tau050-s42-r3\\\": {}, \\\"pi05-goal-tau015-s43-r3\\\": {}, \\\"smolvla-tau035-long-s42\\\": {}, \\\"smolvla-tau030-long-s42\\\": {}, \\\"smolvla-tau015-long-s42\\\": {}, \\\"smolvla-tau045-object-s42\\\": {}, \\\"smolvla-tau040-object-s42\\\": {}, \\\"smolvla-tau030-object-s42\\\": {}, \\\"crm-always-on-long-s43\\\": {}, \\\"crm-always-on-long-s42\\\": {}, \\\"smolvla-tau025-long-s42\\\": {}, \\\"pi05-long-tau015-s43-r3\\\": {}, \\\"pi05-k2mean-spatial-s42-r3\\\": {}, \\\"pi05-k2mean-long-s42-r3\\\": {}, \\\"pi05-k2mean-object-s42-r3\\\": {}, \\\"smolvla-tau035-object-s42-r3\\\": {}, \\\"smolvla-tau025-object-s42-r3\\\": {}, \\\"smolvla-tau020-object-s42\\\": {}, \\\"smolvla-tau010-object-s42\\\": {}, \\\"smolvla-tau005-object-s42\\\": {}, \\\"crm-always-on-goal-s43\\\": {}, \\\"crm-always-on-goal-s42\\\": {}, \\\"crm-always-on-spatial-s44\\\": {}, \\\"crm-always-on-spatial-s43\\\": {}, \\\"smolvla-tau030-long-s42-r2\\\": {}, \\\"smolvla-tau030-long-s43-r2\\\": {}, \\\"tau-sweep-goal-tau035-s42\\\": {}, \\\"tau-sweep-long-tau015-s42\\\": {}, \\\"tau-sweep-long-tau035-s42\\\": {}, \\\"smolvla-tau020-long-s42-r2\\\": {}, \\\"tau-sweep-goal-tau015-s42\\\": {}, \\\"tau-sweep-spatial-tau035-s42\\\": {}, \\\"tau-sweep-spatial-tau015-s42\\\": {}, \\\"smolvla-tau035-object-s42-r2\\\": {}, \\\"smolvla-tau035-object-s43-r3\\\": {}, \\\"smolvla-tau025-object-s43-r3\\\": {}, \\\"crm-always-on-spatial-s42\\\": {}, \\\"crm-always-on-goal-s44\\\": {}, \\\"crm-always-on-object-s44\\\": {}, \\\"crm-always-on-object-s43\\\": {}, \\\"crm-always-on-object-s42\\\": {}, \\\"eval-obs-object-norm003-s45\\\": {}, \\\"eval-obs-object-norm005-s45\\\": {}, \\\"eval-obs-object-norm003-s46\\\": {}, \\\"pi05-k2mean-goal-s43\\\": {}, \\\"pi05-k2mean-long-s42\\\": {}, \\\"pi05-k2mean-object-s42\\\": {}, \\\"pi05-vla-only-spatial-s42-4090\\\": {}, \\\"pi05-vla-only-goal-s42-4090\\\": {}, \\\"pi05-k2mean-spatial-s42\\\": {}, \\\"pi05-vla-only-spatial-s42-4090-r2\\\": {}, \\\"pi05-vla-only-object-s42-4090-r2\\\": {}, \\\"pi05-vla-only-goal-s42-4090-r2\\\": {}, \\\"eval-k2-tau010-015-spatial-s42\\\": {}, \\\"eval-k2-tau010-spatial-s42\\\": {}, \\\"eval-pi05-vla-only-long-seed42-r4-std\\\": {}, \\\"eval-obs-only-object-norm02-k20-seed44\\\": {}, \\\"eval-obs-only-object-norm02-k20-seed43\\\": {}, \\\"eval-obs-only-object-norm02-k20-seed42\\\": {}, \\\"eval-pi05-baseline-object-seed42-r2\\\": {}, \\\"pi05-vla-only-object-s42-4090\\\": {}, \\\"pi05-vla-only-long-s42-4090\\\": {}, \\\"smolvla-tau020-long-s43\\\": {}, \\\"smolvla-tau030-long-s43\\\": {}, \\\"eval-pi05-vla-only-object-s43-r5\\\": {}, \\\"eval-perdof-object-norm005-s44-westd\\\": {}, \\\"eval-perdof-object-norm003-s44-westd\\\": {}, \\\"eval-obs-object-norm005-s45-bjb2\\\": {}, \\\"eval-obs-object-norm005-s44-bjb2\\\": {}, \\\"eval-obs-object-norm003-s44-bjb2\\\": {}, \\\"eval-obs-object-norm005-s43-bjb2\\\": {}, \\\"eval-obs-object-norm003-s43-bjb2\\\": {}, \\\"eval-obs-object-norm005-s46\\\": {}, \\\"eval-perdof-object-norm005-s43-v3\\\": {}, \\\"eval-perdof-object-norm003-s43-v3\\\": {}, \\\"pi05-vla-only-goal-s44-4090\\\": {}, \\\"pi05-vla-only-object-s43-4090\\\": {}, \\\"pi05-vla-only-long-s44-4090\\\": {}, \\\"pi05-vla-only-long-s43-4090\\\": {}, \\\"pi05-vla-only-long-s42-4090-r3\\\": {}, \\\"eval-ksweep-k5-obs-object-s43\\\": {}, \\\"eval-obs-object-norm005-s44-westd\\\": {}, \\\"eval-k2-tau035-spatial-s42-v2\\\": {}, \\\"eval-obs-object-norm005-s43-westd\\\": {}, \\\"eval-obs-object-norm003-s43\\\": {}, \\\"eval-obs-object-norm005-s43\\\": {}, \\\"eval-obs-object-norm003-s44\\\": {}, \\\"eval-ksweep-k20-obs-object-s43\\\": {}, \\\"eval-ksweep-k20-obs-object-s42\\\": {}, \\\"eval-k2-tau025-spatial-s42-v2\\\": {}, \\\"eval-obs-object-norm003-s43-westd\\\": {}, \\\"eval-obs-object-norm003-s44-westd\\\": {}, \\\"eval-obs-object-norm005-s44\\\": {}, \\\"eval-ksweep-k5-obs-object-s42\\\": {}, \\\"smolvla-vla-only-long-n20-s43\\\": {}, \\\"smolvla-vla-only-long-n20-s42\\\": {}, \\\"pi05-object-adaptive-s44-cqa1\\\": {}, \\\"pi05-object-adaptive-s43-cqa1\\\": {}, \\\"pi05-object-adaptive-s42-cqa1\\\": {}, \\\"eval-pi05-vla-only-object-s43-v2\\\": {}, \\\"eval-pi05-vla-only-object-s42-v2\\\": {}, \\\"eval-pi05-vla-only-goal-s43-v2\\\": {}, \\\"eval-pi05-vla-only-goal-s42-v2\\\": {}, \\\"eval-pi05-vla-only-spatial-s43-v2\\\": {}, \\\"eval-pi05-vla-only-spatial-s42-v2\\\": {}, \\\"smolvla-tau025-long-s43\\\": {}, \\\"smolvla-tau015-long-s43\\\": {}, \\\"smolvla-tau025-object-s42-r2\\\": {}, \\\"smolvla-tau035-long-s43\\\": {}, \\\"pi05-goal-tau015-s43\\\": {}, \\\"smolvla-tau035-spatial-s43\\\": {}, \\\"smolvla-tau025-spatial-s43\\\": {}, \\\"smolvla-tau015-spatial-s43\\\": {}, \\\"pi05-goal-tau035-s43\\\": {}, \\\"pi05-goal-tau025-s43\\\": {}, \\\"pi05-adaptive-long-s43-cqa1-r3\\\": {}, \\\"pi05-spatial-tau015-s43\\\": {}, \\\"pi05-spatial-tau035-s43\\\": {}, \\\"pi05-spatial-tau025-s43\\\": {}, \\\"pi05-object-tau035-s42-bjb2\\\": {}, \\\"E_smolvla_crm_norm005_spatial_s42_d149\\\": {}, \\\"pi05-object-tau015-s42-bjb2\\\": {}, \\\"E_smolvla_adaptive_tau045_spatial_s42\\\": {}, \\\"E_smolvla_adaptive_tau035_spatial_s42\\\": {}, \\\"E_smolvla_adaptive_tau015_spatial_s42\\\": {}, \\\"pi05-adaptive-object-s42-tau045-bjb2\\\": {}, \\\"smolvla-tau035-spatial-s42-bjb1\\\": {}, \\\"smolvla-tau015-spatial-s42-bjb1\\\": {}, \\\"smolvla-crm-norm005-spatial-s42-d149\\\": {}, \\\"smolvla-tau045-spatial-s42\\\": {}, \\\"pi05-adaptive-long-s44-bjb1\\\": {}, \\\"pi05-adaptive-long-s43-bjb1\\\": {}, \\\"eval-k2-tau045-spatial-s42-bjb2\\\": {}, \\\"smolvla-crm-norm005-k10-object-s44-cqa1\\\": {}, \\\"smolvla-adapt-tau015-object-s44-cqa1\\\": {}, \\\"smolvla-adapt-tau015-object-s43-cqa1\\\": {}, \\\"smolvla-adapt-tau015-object-s42-cqa1\\\": {}, \\\"smolvla-tau015-object-s42\\\": {}, \\\"smolvla-tau025-object-s43\\\": {}, \\\"smolvla-tau035-goal-s42\\\": {}, \\\"smolvla-tau025-goal-s42\\\": {}, \\\"smolvla-tau015-goal-s42\\\": {}, \\\"smolvla-tau015-object-s43\\\": {}, \\\"smolvla-tau035-object-s43\\\": {}, \\\"pi05-adaptive-long-s42-tau035-bjb2\\\": {}, \\\"smolvla-tau015-goal-s43\\\": {}, \\\"smolvla-tau025-goal-s43\\\": {}, \\\"smolvla-tau035-goal-s43\\\": {}, \\\"pi05-adaptive-long-s42-tau015-bjb2\\\": {}, \\\"smolvla-tau035-object-s43-bjb1\\\": {}, \\\"smolvla-tau025-object-s43-bjb1\\\": {}, \\\"smolvla-tau015-object-s43-bjb1\\\": {}, \\\"smolvla-tau035-goal-s43-bjb1\\\": {}, \\\"smolvla-tau025-goal-s43-bjb1\\\": {}, \\\"smolvla-tau015-goal-s43-bjb1\\\": {}, \\\"pi05-adaptive-goal-s42-tau035-bjb2\\\": {}, \\\"westd-pi05-adaptive-object-s44-paired\\\": {}, \\\"westd-pi05-adaptive-object-s43-paired\\\": {}, \\\"westd-pi05-adaptive-object-s42-paired\\\": {}, \\\"westd-pi05-crm-k2-object-s44\\\": {}, \\\"westd-pi05-crm-k2-object-s43\\\": {}, \\\"westd-pi05-crm-k2-object-s42\\\": {}, \\\"eval-crm-goal-s43-d149-bjb1\\\": {}, \\\"eval-crm-object-s43-d149-bjb1\\\": {}, \\\"eval-crm-object-s42-d149-bjb1\\\": {}, \\\"eval-crm-spatial-s48-d149-bjb1\\\": {}, \\\"pi05-adaptive-long-s44-cqa1-r3\\\": {}, \\\"pi05-adaptive-object-s44-cqa1-r3\\\": {}, \\\"pi05-adaptive-object-s43-cqa1-r3\\\": {}, \\\"pi05-adaptive-goal-s42-tau015-bjb2\\\": {}, \\\"pi05-adaptive-spatial-s42-tau015-bjb2\\\": {}, \\\"pi05-adaptive-spatial-s42-tau035-bjb2\\\": {}, \\\"eval-crm-goal-s43-d149\\\": {}, \\\"eval-crm-goal-s44-d149\\\": {}, \\\"eval-crm-object-s42-d149\\\": {}, \\\"eval-crm-object-s43-d149\\\": {}, \\\"eval-crm-object-s44-d149\\\": {}, \\\"eval-crm-spatial-s48-d149\\\": {}, \\\"pi05-adaptive-long-s43-cqa1\\\": {}, \\\"eval-supp-goal-k2mean-s47\\\": {}, \\\"eval-smolvla-lerobot-spatial-seed43-v3\\\": {}, \\\"eval-smolvla-lerobot-goal-seed43-v3\\\": {}, \\\"precompute-pi05-object-2048-r2\\\": {}, \\\"precompute-pi05-long-2048-r2\\\": {}, \\\"pi05-adaptive-long-s44-cqa1\\\": {}, \\\"eval-supp-goal-adapt-tau025-s47\\\": {}, \\\"eval-supp-goal-crm-norm005-s47\\\": {}, \\\"eval-supp-goal-reconvla-s47\\\": {}, \\\"eval-supp-obj-reconvla-s47\\\": {}, \\\"eval-supp-reconvla-obj-s45\\\": {}, \\\"eval-supp-spatial-k2mean-s46\\\": {}, \\\"eval-supp-spatial-adapt-tau025-s45-r3\\\": {}, \\\"eval-supp-spatial-reconvla-s46\\\": {}, \\\"pi05-crm-k2-long-s44-cqa1\\\": {}, \\\"pi05-crm-k2-object-s42-bjb1-r2\\\": {}, \\\"pi05-crm-k2-object-s43-bjb1-r2\\\": {}, \\\"pi05-crm-k2-object-s44-bjb1-r2\\\": {}, \\\"pi05-adaptive-goal-s44-bjb1\\\": {}, \\\"pi05-adaptive-spatial-s44-bjb2-r2\\\": {}, \\\"pi05-adaptive-spatial-s43-bjb2-r2\\\": {}, \\\"pi05-adaptive-spatial-s42-bjb2-r2\\\": {}, \\\"pi05-crm-k2-spatial-s44-bjb2-r2\\\": {}, \\\"pi05-crm-k2-spatial-s43-bjb2-r2\\\": {}, \\\"pi05-crm-k2-spatial-s42-bjb2-r2\\\": {}, \\\"pi05-crm-k2-goal-s44-bjb1-r2\\\": {}, \\\"pi05-crm-k2-goal-s43-bjb1-r2\\\": {}, \\\"pi05-crm-k2-goal-s42-bjb1-r2\\\": {}, \\\"westd-pi05-vla-only-long-s44-paired\\\": {}, \\\"pi05-crm-k2-long-s42-r2\\\": {}, \\\"pi05-crm-k2-long-s43-r2\\\": {}, \\\"westd-pi05-vla-only-long-s43-paired\\\": {}, \\\"pi05-crm-k2-long-s43-cqa1\\\": {}, \\\"westd-pi05-vla-only-spatial-s43-paired\\\": {}, \\\"westd-pi05-vla-only-spatial-s42-paired\\\": {}, \\\"westd-pi05-vla-only-spatial-s44-paired\\\": {}, \\\"westd-pi05-vla-only-long-s42-paired\\\": {}, \\\"westd-pi05-vla-only-object-s44-paired\\\": {}, \\\"westd-pi05-vla-only-object-s43-paired\\\": {}, \\\"westd-pi05-vla-only-object-s42-paired\\\": {}, \\\"westd-pi05-vla-only-goal-s44-paired\\\": {}, \\\"westd-pi05-vla-only-goal-s43-paired\\\": {}, \\\"westd-pi05-vla-only-goal-s42-paired\\\": {}, \\\"pi05-adaptive-object-s42-cqa1\\\": {}, \\\"pi05-adaptive-long-s42-r2\\\": {}, \\\"pi05-adaptive-object-s43-bjb2-24035\\\": {}, \\\"pi05-adaptive-long-s44-cqa1-r2\\\": {}, \\\"pi05-adaptive-long-s43-cqa1-r2\\\": {}, \\\"pi05-adaptive-goal-s42-cqa1\\\": {}, \\\"westd-pi05-crm-k2-goal-s42\\\": {}, \\\"westd-pi05-adaptive-object-s42\\\": {}, \\\"westd-pi05-adaptive-goal-s43\\\": {}, \\\"westd-pi05-adaptive-goal-s42\\\": {}, \\\"pi05-adaptive-object-s44-cqa1-r2\\\": {}, \\\"pi05-adaptive-goal-s43-bjb1-18228\\\": {}, \\\"westd-pi05-adaptive-object-s43\\\": {}, \\\"pi05-crm-k2-spatial-s44-bjb2\\\": {}, \\\"pi05-crm-k2-spatial-s43-bjb2\\\": {}, \\\"pi05-crm-k2-spatial-s42-bjb2\\\": {}, \\\"pi05-adaptive-spatial-s44-bjb2\\\": {}, \\\"pi05-adaptive-spatial-s43-bjb2\\\": {}, \\\"pi05-adaptive-spatial-s42-bjb2\\\": {}, \\\"pi05-crm-k2-object-s44-bjb1\\\": {}, \\\"pi05-crm-k2-object-s43-bjb1\\\": {}, \\\"pi05-crm-k2-object-s42-bjb1\\\": {}, \\\"pi05-crm-k2-goal-s44-bjb1\\\": {}, \\\"pi05-crm-k2-goal-s43-bjb1\\\": {}, \\\"pi05-crm-k2-goal-s42-bjb1\\\": {}, \\\"eval-adaptive-spatial-s44-d149\\\": {}, \\\"eval-adaptive-spatial-s43-d149\\\": {}, \\\"eval-adaptive-goal-s44-d149\\\": {}, \\\"eval-adaptive-goal-s43-d149\\\": {}, \\\"eval-adaptive-object-s44-d149\\\": {}, \\\"eval-adaptive-object-s43-d149\\\": {}, \\\"eval-supp-crm-norm005-obj-s44\\\": {}, \\\"eval-adaptive-spatial-k1-s42\\\": {}, \\\"westd-pi05-vla-only-goal-s42\\\": {}, \\\"eval-supp-goal-vla-only-wrapper-s43\\\": {}, \\\"westd-pi05-adaptive-goal-s44\\\": {}, \\\"tau_sweep_goal_tau090_s42_cqa1\\\": {}, \\\"tau_sweep_goal_tau070_s42_cqa1\\\": {}, \\\"tau_sweep_goal_tau050_s42_cqa1\\\": {}, \\\"tau_sweep_spatial_tau025_s42\\\": {}, \\\"tau_sweep_goal_tau025_s42\\\": {}, \\\"tau_sweep_goal_tau040_s42\\\": {}, \\\"tau_sweep_goal_tau045_s42\\\": {}, \\\"goal_vla_only_s48\\\": {}, \\\"goal_adapt_s48\\\": {}, \\\"westd-pi05-k2mean-goal-s42\\\": {}, \\\"eval-goal-vla-only-s49-paired\\\": {}, \\\"eval-goal-adapt-tau025-s49-paired\\\": {}, \\\"eval-spatial-vla-only-s48-paired\\\": {}, \\\"eval-spatial-vla-only-s46-paired\\\": {}, \\\"eval-spatial-adapt-tau025-s48-paired\\\": {}, \\\"eval-spatial-adapt-tau025-s46-paired\\\": {}, \\\"pi05-adaptive-long-s42\\\": {}, \\\"pi05-adaptive-object-s42-v2\\\": {}, \\\"pi05-k2mean-goal-s42\\\": {}, \\\"pi05-crm-k2-long-s44\\\": {}, \\\"eval-k2-goal-vla-only-s49\\\": {}, \\\"eval-mechanism-goal-adapt-s42\\\": {}, \\\"pi05-crm-k2-long-s43\\\": {}, \\\"pi05-crm-k2-long-s42\\\": {}, \\\"eval-k2-tau030-spatial-s42\\\": {}, \\\"eval-k2-tau020-spatial-s42\\\": {}, \\\"eval-pi05-vla-spatial-s44\\\": {}, \\\"eval-pi05-adaptive-goal-s44\\\": {}, \\\"eval-pi05-adaptive-object-s44\\\": {}, \\\"eval-pi05-crm-object-s42\\\": {}, \\\"eval-pi05-crm-goal-s42\\\": {}, \\\"eval-pi05-crm-goal-s43\\\": {}, \\\"eval-pi05-crm-goal-s44\\\": {}, \\\"eval-pi05-crm-spatial-s42\\\": {}, \\\"eval-pi05-crm-spatial-s43\\\": {}, \\\"eval-pi05-crm-goal-s42-d149\\\": {}, \\\"eval-pi05-crm-spatial-s42-d149\\\": {}, \\\"eval-pi05-crm-spatial-s43-d149\\\": {}, \\\"eval-pi05-crm-goal-s43-d149\\\": {}, \\\"eval-pi05-crm-goal-s44-d149\\\": {}, \\\"eval-vla-only-long-s44-d149\\\": {}, \\\"eval-adaptive-long-s43-d149\\\": {}, \\\"eval-crm-long-s44-d149\\\": {}, \\\"eval-crm-long-s43-d149\\\": {}, \\\"eval-pi05-adaptive-object-s43\\\": {}, \\\"eval-pi05-adaptive-object-s42\\\": {}, \\\"eval-pi05-adaptive-goal-s43\\\": {}, \\\"eval-smolvla-crm-goal-s42\\\": {}, \\\"eval-crm-long-s42-d149\\\": {}, \\\"eval-pi05-vla-only-object-s43\\\": {}, \\\"eval-pi05-vla-only-goal-s44\\\": {}, \\\"eval-smolvla-crm-goal-seed44\\\": {}, \\\"eval-vla-only-spatial-bjb1-s49\\\": {}, \\\"eval-vla-only-spatial-bjb1-s48\\\": {}, \\\"eval-adaptive-long-s44-d149\\\": {}, \\\"eval-adaptive-long-s42-d149\\\": {}, \\\"eval-k2-spatial-vla-only-s44-paired-r2\\\": {}, \\\"eval-k2-spatial-vla-only-s43-paired-r2\\\": {}, \\\"eval-k2-spatial-vla-only-s42-paired-r2\\\": {}, \\\"eval-k2-spatial-adapt-s44-paired-r2\\\": {}, \\\"eval-k2-spatial-adapt-s43-paired-r2\\\": {}, \\\"eval-k2-spatial-adapt-s42-paired-r2\\\": {}, \\\"eval-vla-only-spatial-s47-d149\\\": {}, \\\"eval-adaptive-object-s42-d149\\\": {}, \\\"eval-smolvla-crm-spatial-s47\\\": {}, \\\"eval-pi05-adaptive-goal-s42-dryrun\\\": {}, \\\"eval-adaptive-spatial-s47-bjb1-d149\\\": {}, \\\"eval-adaptive-spatial-s47-d149\\\": {}, \\\"eval-adaptive-goal-s42-d149\\\": {}, \\\"eval-pi05-vla-only-object-s42-r2\\\": {}, \\\"eval-pi05-adaptive-spatial-s42-r2\\\": {}, \\\"eval-pi05-vla-only-spatial-s44-d149\\\": {}, \\\"eval-pi05-adaptive-goal-s42\\\": {}, \\\"eval-k2-tau010-spatial-s42-r3\\\": {}, \\\"eval-k2-tau0075-spatial-s42\\\": {}, \\\"eval-k2-tau015-spatial-s42-r2\\\": {}, \\\"eval-k2-goal-vla-only-s46-paired\\\": {}, \\\"eval-k2-goal-vla-only-s45-paired\\\": {}, \\\"eval-k2-goal-adapt-s47-paired\\\": {}, \\\"eval-k2-goal-adapt-s46-paired\\\": {}, \\\"eval-k2-goal-vla-only-s47-paired\\\": {}, \\\"eval-k2-goal-adapt-s45-paired\\\": {}, \\\"eval-vla-only-spatial-bjb1-s46\\\": {}, \\\"eval-k2-adaptive-spatial-s49\\\": {}, \\\"eval-k2-adaptive-spatial-s48\\\": {}, \\\"eval-k2-adaptive-spatial-s46\\\": {}, \\\"eval-pi05-vla-only-spatial-s43-r2\\\": {}, \\\"eval-k2-adaptive-spatial-s43\\\": {}, \\\"eval-k2-adaptive-spatial-s42\\\": {}, \\\"eval-vla-only-spatial-cqa1-s44\\\": {}, \\\"eval-vla-only-spatial-cqa1-s43\\\": {}, \\\"eval-vla-only-spatial-cqa1-s42\\\": {}, \\\"eval-k2-adaptive-spatial-s44\\\": {}, \\\"eval-canonical-adaptive-k10-spatial-s42\\\": {}, \\\"eval-k10-tau025-spatial-s45\\\": {}, \\\"eval-k10-tau025-spatial-s47\\\": {}, \\\"eval-long-adaptive-k10-s42\\\": {}, \\\"eval-pi05-vla-only-spatial-s42-paired\\\": {}, \\\"eval-pi05-vla-only-goal-s42-paired\\\": {}, \\\"eval-long-adaptive-k10-s43\\\": {}, \\\"eval-long-adaptive-k10-s44\\\": {}, \\\"eval-canonical-adaptive-k10-spatial-s43\\\": {}, \\\"eval-canonical-adaptive-k10-spatial-s44\\\": {}, \\\"eval-canonical-adaptive-k10-spatial-s48\\\": {}, \\\"eval-canonical-adaptive-k10-spatial-s49\\\": {}, \\\"eval-k10-tau025-spatial-s46\\\": {}, \\\"eval-pi05-adaptive-spatial-s42\\\": {}, \\\"eval-pi05-vla-only-goal-s43\\\": {}, \\\"eval-pi05-vla-only-spatial-s43\\\": {}, \\\"eval-pi05-vla-only-object-s42\\\": {}, \\\"eval-supp-long-vla-only-s42\\\": {}, \\\"eval-supp-long-adapt-tau025-s42\\\": {}, \\\"eval-k2-tau010-spatial-s42-r2\\\": {}, \\\"eval-pi05-vla-only-spatial-s45\\\": {}, \\\"eval-pi05-vla-only-object-s44\\\": {}, \\\"eval-k2-tau015-spatial-s42\\\": {}, \\\"eval-pi05-vla-only-goal-s42\\\": {}, \\\"eval-pi05-vla-only-spatial-s42\\\": {}, \\\"eval-supp-crm-norm005-goal-s48\\\": {}, \\\"eval-supp-crm-norm005-spatial-s49\\\": {}, \\\"eval-supp-crm-norm005-spatial-s48\\\": {}, \\\"eval-supp-long-vla-only-s43-r2\\\": {}, \\\"eval-supp-goal-vla-only-s42-bjb1\\\": {}, \\\"crm-norm005-goal-s49\\\": {}, \\\"eval-supp-obj-vla-only-s44\\\": {}, \\\"crm-norm005-object-s48\\\": {}, \\\"eval-supp-obj-vla-only-s43\\\": {}, \\\"eval-supp-obj-vla-only-s42\\\": {}, \\\"eval-supp-long-vla-only-s48\\\": {}, \\\"eval-supp-goal-vla-only-s50\\\": {}, \\\"eval-supp-goal-vla-only-s44\\\": {}, \\\"eval-supp-spatial-vla-only-smolvla-s42\\\": {}, \\\"eval-supp-goal-vla-only-s43\\\": {}, \\\"eval-supp-goal-vla-only-s42\\\": {}, \\\"train-crm-pi05-unified-3suite-r2\\\": {}, \\\"eval-supp-vla-only-spatial-s49\\\": {}, \\\"eval-supp-vla-only-spatial-s48\\\": {}, \\\"eval-supp-vla-only-obj-s49\\\": {}, \\\"eval-supp-vla-only-obj-s48\\\": {}, \\\"eval-supp-vla-only-goal-s49\\\": {}, \\\"eval-supp-vla-only-goal-s48\\\": {}, \\\"eval-k5-spatial-s42-sweep\\\": {}, \\\"eval-supp-long-vla-only-s43\\\": {}, \\\"eval-supp-goal-vla-only-s45\\\": {}, \\\"eval-supp-long-vla-only-s45\\\": {}, \\\"eval-supp-long-vla-only-s44\\\": {}, \\\"eval-supp-spatial-vla-only-s42\\\": {}, \\\"eval-pi05-vla-only-object-seed43-r4\\\": {}, \\\"eval-supp-obj-vla-only-s50\\\": {}, \\\"eval-supp-long-adapt-tau025-s47-r2\\\": {}, \\\"eval-supp-long-k2mean-s47-r2\\\": {}, \\\"eval-supp-spatial-reconvla-s47\\\": {}, \\\"eval-a1-baseline-object-s42\\\": {}, \\\"eval-supp-long-vla-only-s47-r4\\\": {}, \\\"eval-supp-obj-k2mean-s47-r2\\\": {}, \\\"eval-supp-obj-adapt-tau025-s47-r2\\\": {}, \\\"eval-supp-obj-crm-norm005-s47-r2\\\": {}, \\\"eval-supp-obj-vla-only-s47-r2\\\": {}, \\\"eval-supp-k2mean-spatial-s47\\\": {}, \\\"eval-supp-spatial-vla-only-s47\\\": {}, \\\"eval-supp-spatial-adapt-tau025-s47\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s47\\\": {}, \\\"eval-supp-spatial-k2mean-s47\\\": {}, \\\"eval-supp-reconvla-spatial-s47\\\": {}, \\\"eval-supp-vla-only-spatial-s47\\\": {}, \\\"eval-supp-long-reconvla-s47\\\": {}, \\\"eval-supp-long-crm-norm005-s47\\\": {}, \\\"eval-supp-obj-k2mean-s47\\\": {}, \\\"eval-supp-obj-crm-norm005-s47\\\": {}, \\\"eval-supp-obj-adapt-tau025-s47\\\": {}, \\\"eval-supp-obj-vla-only-s47\\\": {}, \\\"eval-supp-goal-vla-only-s47-r3\\\": {}, \\\"eval-supp-long-k2mean-s47\\\": {}, \\\"eval-supp-long-adapt-tau025-s47\\\": {}, \\\"eval-supp-spatial-crm-norm005-s47\\\": {}, \\\"eval-supp-long-crm-norm005-s46\\\": {}, \\\"train-crm-pi05-unified-3suite\\\": {}, \\\"eval-openvla-object-vla-only-seed42-v3\\\": {}, \\\"eval-supp-vla-only-spatial-s46\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s45\\\": {}, \\\"eval-supp-crm-norm005-spatial-s45\\\": {}, \\\"eval-supp-vla-only-spatial-s45\\\": {}, \\\"eval-supp-crm-norm005-spatial-s46\\\": {}, \\\"train-crm-pi05-spatial-k1\\\": {}, \\\"train-crm-pi05-goal-k1\\\": {}, \\\"eval-supp-goal-vla-only-s47-r2\\\": {}, \\\"eval-supp-long-vla-only-s47-r3\\\": {}, \\\"eval-supp-long-vla-only-s47-r2\\\": {}, \\\"eval-supp-goal-vla-only-s47\\\": {}, \\\"eval-supp-long-reconvla-s46\\\": {}, \\\"eval-supp-long-k2mean-s46\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s46\\\": {}, \\\"eval-supp-long-adapt-tau025-s46\\\": {}, \\\"crm-train-openvla-k1-multiscale-object\\\": {}, \\\"eval-supp-long-k2mean-s46-r2\\\": {}, \\\"eval-supp-long-reconvla-s46-r2\\\": {}, \\\"eval-supp-long-crm-norm005-s46-r2\\\": {}, \\\"eval-supp-long-adapt-tau025-s46-r2\\\": {}, \\\"eval-supp-obj-crm-norm005-s45\\\": {}, \\\"eval-supp-obj-adapt-tau025-s45\\\": {}, \\\"eval-supp-obj-vla-only-s45\\\": {}, \\\"eval-supp-spatial-crm-norm005-s45\\\": {}, \\\"eval-supp-spatial-vla-only-s45\\\": {}, \\\"precompute-pi05-goal-2048-r2\\\": {}, \\\"eval-supp-long-vla-only-s46\\\": {}, \\\"precompute-pi05-spatial-2048-r2\\\": {}, \\\"precompute-smolvla-goal-bjb1-32546\\\": {}, \\\"eval-supp-goal-vla-only-s46\\\": {}, \\\"eval-supp-goal-reconvla-s46\\\": {}, \\\"crm-train-pi05-spatial-full\\\": {}, \\\"eval-obs-only-spatial-v2\\\": {}, \\\"eval-perdof-object-norm003-seed44\\\": {}, \\\"eval-random-selection-spatial-seed42\\\": {}, \\\"eval-adaptive-k-spatial-p90-seed44-bjb2\\\": {}, \\\"eval-supp-goal-vla-only-wrapper-s44\\\": {}, \\\"eval-supp-long-reconvla-s45\\\": {}, \\\"eval-pi05-vla-only-long-seed42-r4\\\": {}, \\\"eval-pi05-vla-only-object-seed42\\\": {}, \\\"eval-pi05-vla-only-object-seed43\\\": {}, \\\"eval-pi05-vla-only-object-seed44\\\": {}, \\\"eval-supp-long-k2mean-s45\\\": {}, \\\"eval-supp-goal-k2mean-s46\\\": {}, \\\"eval-supp-goal-adapt-tau025-s46\\\": {}, \\\"eval-supp-goal-crm-norm005-s46\\\": {}, \\\"eval-supp-spatial-k2mean-s45\\\": {}, \\\"eval-supp-spatial-vla-only-s46\\\": {}, \\\"eval-supp-spatial-adapt-tau025-s46\\\": {}, \\\"eval-supp-spatial-crm-norm005-s46\\\": {}, \\\"eval-supp-long-crm-norm005-s45\\\": {}, \\\"eval-supp-long-adapt-tau025-s45\\\": {}, \\\"eval-supp-spatial-reconvla-s45\\\": {}, \\\"eval-supp-goal-k2mean-s45\\\": {}, \\\"eval-supp-adapt-tau025-obj-s45\\\": {}, \\\"eval-supp-obj-k2mean-s45\\\": {}, \\\"eval-supp-crm-obj-s46\\\": {}, \\\"eval-supp-long-k2mean-s44\\\": {}, \\\"eval-supp-long-reconvla-s44\\\": {}, \\\"eval-supp-goal-reconvla-s45\\\": {}, \\\"eval-supp-crm-norm005-obj-s46\\\": {}, \\\"eval-supp-goal-crm-norm005-s45\\\": {}, \\\"eval-supp-crm-norm005-obj-s45\\\": {}, \\\"eval-supp-reconvla-obj-s46\\\": {}, \\\"eval-supp-goal-adapt-tau025-s45\\\": {}, \\\"eval-supp-long-crm-norm005-s44\\\": {}, \\\"eval-supp-long-adapt-tau025-s44\\\": {}, \\\"eval-supp-k2mean-obj-s46\\\": {}, \\\"eval-supp-k2mean-obj-s45\\\": {}, \\\"eval-supp-adapt-tau025-obj-s46\\\": {}, \\\"eval-supp-long-k2mean-s42\\\": {}, \\\"eval-supp-obj-vla-only-s46\\\": {}, \\\"eval-supp-long-k2mean-s43\\\": {}, \\\"eval-supp-long-reconvla-s43\\\": {}, \\\"eval-supp-long-crm-norm005-s43\\\": {}, \\\"eval-supp-long-adapt-tau025-s43\\\": {}, \\\"eval-supp-obj-adapt-tau025-s45-r2\\\": {}, \\\"eval-supp-long-crm-norm005-s42\\\": {}, \\\"eval-supp-long-reconvla-s42\\\": {}, \\\"eval-ablation-tau040-goal-s42\\\": {}, \\\"eval-ablation-tau015-goal-s42\\\": {}, \\\"eval-supp-k2mean-object-s44\\\": {}, \\\"eval-ablation-tau010-goal-s42\\\": {}, \\\"eval-supp-obj-reconvla-s44\\\": {}, \\\"eval-supp-spatial-vla-only-s44\\\": {}, \\\"eval-supp-goal-vla-only-wrapper-s44-r2\\\": {}, \\\"eval-supp-k2mean-spatial-s44\\\": {}, \\\"eval-supp-spatial-vla-only-s43\\\": {}, \\\"eval-supp-k2mean-goal-s44\\\": {}, \\\"eval-supp-adapt-tau025-obj-s44\\\": {}, \\\"eval-supp-goal-reconvla-s44\\\": {}, \\\"eval-supp-obj-reconvla-s43\\\": {}, \\\"eval-supp-crm-norm005-goal-s44\\\": {}, \\\"eval-supp-k2mean-object-s43\\\": {}, \\\"eval-supp-k2mean-goal-s42-r2\\\": {}, \\\"eval-supp-adapt-tau025-goal-s44\\\": {}, \\\"eval-supp-crm-norm005-obj-s43\\\": {}, \\\"eval-supp-adapt-tau025-goal-s43\\\": {}, \\\"eval-supp-crm-norm005-goal-s43\\\": {}, \\\"eval-supp-adapt-tau025-obj-s43\\\": {}, \\\"eval-supp-goal-reconvla-s43\\\": {}, \\\"eval-supp-k2mean-spatial-s43\\\": {}, \\\"eval-supp-reconvla-spatial-s44\\\": {}, \\\"eval-supp-reconvla-spatial-s43\\\": {}, \\\"eval-supp-k2mean-goal-s43\\\": {}, \\\"eval-supp-k2mean-object-s42\\\": {}, \\\"eval-supp-goal-adapt-tau025-s42\\\": {}, \\\"eval-supp-goal-crm005-s42\\\": {}, \\\"eval-supp-goal-reconvla-s42\\\": {}, \\\"train-crm-unified-4suite-r6\\\": {}, \\\"eval-goal-vla-only-wrapper-s42\\\": {}, \\\"eval-supp-obj-adapt-tau025-s42\\\": {}, \\\"eval-supp-k2mean-spatial-s42\\\": {}, \\\"eval-supp-crm-norm005-spatial-s44\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s44\\\": {}, \\\"eval-supp-reconvla-k2-spatial-s42\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s43\\\": {}, \\\"eval-supp-crm-norm005-spatial-s43\\\": {}, \\\"eval-supp-k2mean-goal-s42\\\": {}, \\\"eval-supp-obj-adapt-s42-r2\\\": {}, \\\"eval-object-vla-only-wrapper-s44-r2\\\": {}, \\\"eval-object-vla-only-wrapper-s43-r2\\\": {}, \\\"eval-object-vla-only-wrapper-s42-r2\\\": {}, \\\"eval-supp-obj-reconvla-s42\\\": {}, \\\"eval-supp-obj-crm005-s42-r2\\\": {}, \\\"eval-supp-adapt-tau035-spatial-s42-r2\\\": {}, \\\"eval-supp-adapt-tau015-spatial-s42-r2\\\": {}, \\\"eval-supp-crm-norm02-spatial-s42-r2\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s42-r2\\\": {}, \\\"eval-openvla-object-baseline-seed42-r2\\\": {}, \\\"eval-obs-only-object-norm02-seed55\\\": {}, \\\"precompute-pi05-features-object\\\": {}, \\\"precompute-smolvla-goal-shard2\\\": {}, \\\"precompute-smolvla-goal-shard1\\\": {}, \\\"precompute-smolvla-goal-shard0\\\": {}, \\\"eval-smolvla-long-seed2\\\": {}, \\\"eval-smolvla-long-seed1\\\": {}, \\\"eval-smolvla-long-seed0\\\": {}, \\\"eval-smolvla-crm-spatial-seed42-v1\\\": {}, \\\"eval-smolvla-crm-spatial-seed43-v1\\\": {}, \\\"eval-smolvla-crm-spatial-seed44-v1\\\": {}, \\\"eval-smolvla-crm-goal-seed42-v1\\\": {}, \\\"eval-smolvla-crm-goal-seed43-v1\\\": {}, \\\"eval-smolvla-crm-goal-seed44-v1\\\": {}, \\\"eval-supp-obj-adapt-s42\\\": {}, \\\"eval-crm-norm02-spatial-s42\\\": {}, \\\"eval-adaptive-tau015-spatial-s42\\\": {}, \\\"eval-adaptive-tau025-spatial-s42\\\": {}, \\\"eval-adaptive-tau035-spatial-s42\\\": {}, \\\"train-crm-unified-4suite-r5-resumed\\\": {}, \\\"eval-object-vla-only-wrapper-s44\\\": {}, \\\"eval-object-vla-only-wrapper-s43\\\": {}, \\\"eval-object-vla-only-wrapper-s42\\\": {}, \\\"eval-supp-obj-crm005-s42\\\": {}, \\\"eval-supp-adapt-tau035-spatial-s42\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s42\\\": {}, \\\"eval-supp-adapt-tau015-spatial-s42\\\": {}, \\\"eval-supp-crm-norm02-spatial-s42\\\": {}, \\\"eval-3dir-adaptive-spatial-s42\\\": {}, \\\"eval-3dir-norm03-spatial-s42\\\": {}, \\\"eval-3dir-reconvla-spatial-s42\\\": {}, \\\"eval-3dir-norm01-spatial-s42\\\": {}, \\\"eval-3dir-norm005-spatial-s42\\\": {}, \\\"precompute-pi05-goal-2048\\\": {}, \\\"precompute-pi05-spatial-2048\\\": {}, \\\"precompute-pi05-object-2048\\\": {}, \\\"eval-smolvla-crm-object-seed43-v1\\\": {}, \\\"eval-smolvla-crm-object-seed42-v1\\\": {}, \\\"eval-smolvla-crm-object-seed44-v1\\\": {}, \\\"train-crm-unified-4suite-r5\\\": {}, \\\"eval-smolvla-crm-goal-seed43\\\": {}, \\\"eval-smolvla-crm-goal-seed42\\\": {}, \\\"eval-smolvla-crm-spatial-seed44\\\": {}, \\\"eval-smolvla-crm-spatial-seed43\\\": {}, \\\"eval-smolvla-crm-spatial-seed42\\\": {}, \\\"precompute-pi05-long-2048\\\": {}, \\\"eval-smolvla-lerobot-goal-seed44-v3\\\": {}, \\\"train-crm-smolvla-3suite-v1\\\": {}, \\\"eval-smolvla-lerobot-goal-seed43-v2\\\": {}, \\\"eval-smolvla-lerobot-spatial-seed43-v2\\\": {}, \\\"eval-smolvla-lerobot-object-seed44-v2\\\": {}, \\\"eval-smolvla-lerobot-object-seed43-v2\\\": {}, \\\"eval-smolvla-lerobot-goal-seed43\\\": {}, \\\"eval-smolvla-lerobot-spatial-seed43\\\": {}, \\\"eval-smolvla-lerobot-object-seed44\\\": {}, \\\"eval-smolvla-lerobot-object-seed43\\\": {}, \\\"eval-smolvla-lerobot-spatial-seed44\\\": {}, \\\"precompute-smolvla-long-wrapper-bjb1\\\": {}, \\\"eval-smolvla-lerobot-long-seed44\\\": {}, \\\"eval-smolvla-lerobot-long-seed43\\\": {}, \\\"eval-smolvla-lerobot-long-seed42\\\": {}, \\\"train-crm-unified-4suite-r4\\\": {}, \\\"eval-pi05-vla-only-long-seed42-r4-rerun\\\": {}, \\\"eval-pi05-crm-object-seed44\\\": {}, \\\"eval-pi05-crm-object-seed43\\\": {}, \\\"eval-pi05-crm-object-seed42\\\": {}, \\\"eval-pi05-vla-only-long-seed43-r4-std\\\": {}, \\\"eval-pi05-vla-only-goal-seed44-r4-std\\\": {}, \\\"eval-pi05-vla-only-goal-seed42-r4-std\\\": {}, \\\"eval-pi05-vla-only-long-seed44-r4-std\\\": {}, \\\"eval-pi05-vla-only-goal-seed43-r4-std\\\": {}, \\\"eval-pi05-vla-only-goal-seed42-r4\\\": {}, \\\"precompute-smolvla-long-k2\\\": {}, \\\"train-crm-unified-4suite-r3\\\": {}, \\\"train-crm-unified-4suite-r2\\\": {}, \\\"precompute-smolvla-goal-bjb2-28827\\\": {}, \\\"precompute-smolvla-long-bjb2-28827\\\": {}, \\\"eval-pi05-vla-only-spatial-seed44-r4\\\": {}, \\\"eval-pi05-vla-only-spatial-seed43-r4\\\": {}, \\\"eval-pi05-vla-only-spatial-seed42-r4\\\": {}, \\\"eval-pi05-vla-only-long-seed44-r4\\\": {}, \\\"eval-pi05-vla-only-long-seed43-r4\\\": {}, \\\"eval-pi05-vla-only-goal-seed44-r4\\\": {}, \\\"eval-pi05-vla-only-goal-seed43-r4\\\": {}, \\\"eval-openvla-oft-official-object\\\": {}, \\\"eval-pi05-crm-spatial-seed44\\\": {}, \\\"eval-pi05-crm-spatial-seed43\\\": {}, \\\"eval-pi05-crm-spatial-seed42\\\": {}, \\\"eval-pi05-vla-only-object-seed44-r4\\\": {}, \\\"eval-smolvla-lerobot-official-object\\\": {}, \\\"eval-pi05-vla-only-object-seed42-r4\\\": {}, \\\"train-crm-unified-4suite\\\": {}, \\\"precompute-smolvla-long-bjb1-32546-r2\\\": {}, \\\"precompute-smolvla-long-bjb1-32546\\\": {}, \\\"eval-loss-perdof-object-seed42\\\": {}, \\\"eval-loss-combined-object-seed42\\\": {}, \\\"eval-loss-conformal-object-seed42\\\": {}, \\\"eval-loss-mse-object-seed42\\\": {}, \\\"eval-openvla-oft-object-baseline-seed42\\\": {}, \\\"precompute-smolvla-long-bjb1-18228\\\": {}, \\\"crm-loss-combined\\\": {}, \\\"crm-loss-conformal\\\": {}, \\\"precompute-smolvla-goal-bjb1-18228\\\": {}, \\\"crm-loss-perdof\\\": {}, \\\"crm-loss-mse-baseline\\\": {}, \\\"eval-smolvla-acr-goal-seed43\\\": {}, \\\"eval-smolvla-crm-long-seed44-v2\\\": {}, \\\"eval-smolvla-crm-goal-seed44-v2\\\": {}, \\\"eval-smolvla-crm-long-seed43-v2\\\": {}, \\\"eval-smolvla-acr-long-seed42\\\": {}, \\\"eval-smolvla-acr-goal-seed42\\\": {}, \\\"crm-train-pi05-spatial-v2\\\": {}, \\\"crm-train-pi05-object-full\\\": {}, \\\"crm-train-pi05-spatial\\\": {}, \\\"crm-train-pi05-object\\\": {}, \\\"eval-pi05-vla-only-spatial-seed45\\\": {}, \\\"eval-pi05-vla-only-spatial-seed43-r3\\\": {}, \\\"eval-pi05-vla-only-spatial-seed42-r3\\\": {}, \\\"eval-pi05-vla-only-object-seed44-r3\\\": {}, \\\"eval-pi05-vla-only-object-seed43-r3\\\": {}, \\\"eval-pi05-vla-only-object-seed42-r3\\\": {}, \\\"eval-spatial-obs-only-seed45\\\": {}, \\\"eval-pi05-vla-only-spatial-seed44\\\": {}, \\\"eval-pi05-vla-only-spatial-seed43\\\": {}, \\\"eval-pi05-vla-only-spatial-seed42\\\": {}, \\\"eval-k20-obs-only-spatial-seed44\\\": {}, \\\"eval-k20-obs-only-spatial-seed43\\\": {}, \\\"eval-k20-obs-only-spatial-seed42\\\": {}, \\\"eval-k20-obs-only-object-seed45\\\": {}, \\\"eval-obs-only-object-norm003-seed66\\\": {}, \\\"eval-obs-only-object-norm01-seed66\\\": {}, \\\"eval-obs-only-object-norm005-seed66\\\": {}, \\\"eval-obs-only-object-norm003-seed67\\\": {}, \\\"eval-k20-obs-only-object-seed44\\\": {}, \\\"eval-k20-obs-only-object-seed43\\\": {}, \\\"eval-k20-obs-only-object-seed42\\\": {}, \\\"eval-crm-object-k20-seed44\\\": {}, \\\"eval-crm-object-k20-seed42\\\": {}, \\\"eval-obs-only-object-norm02-seed53\\\": {}, \\\"eval-obs-only-object-norm02-seed52\\\": {}, \\\"eval-obs-only-object-norm02-seed51\\\": {}, \\\"eval-obs-only-object-norm02-seed50\\\": {}, \\\"eval-obs-only-object-norm02-seed48-r2\\\": {}, \\\"eval-obs-only-object-norm02-seed47\\\": {}, \\\"eval-obs-only-object-norm02-seed46\\\": {}, \\\"eval-obs-only-object-norm02-seed45\\\": {}, \\\"eval-obs-only-object-norm02-seed44-r2\\\": {}, \\\"eval-obs-only-object-norm02-seed43-r3\\\": {}, \\\"eval-obs-only-object-norm02-seed43-r2\\\": {}, \\\"eval-obs-only-object-norm005-seed67\\\": {}, \\\"eval-obs-only-object-norm01-seed67\\\": {}, \\\"eval-vla-only-object-seed50\\\": {}, \\\"eval-vla-only-object-seed49\\\": {}, \\\"eval-vla-only-object-seed48\\\": {}, \\\"eval-vla-only-object-seed46\\\": {}, \\\"eval-vla-only-object-seed45\\\": {}, \\\"eval-vla-only-object-seed44-r2\\\": {}, \\\"eval-plan-a-object-seed42\\\": {}, \\\"eval-vla-only-object-seed43\\\": {}, \\\"eval-vla-only-object\\\": {}, \\\"eval-plan-a-spatial-seed43\\\": {}, \\\"eval-plan-a-object-seed44\\\": {}, \\\"eval-plan-a-spatial-seed42\\\": {}, \\\"eval-plan-a-spatial-seed44\\\": {}, \\\"eval-plan-a-object-seed43\\\": {}, \\\"eval-random-selection-object-seed44\\\": {}, \\\"eval-random-selection-object-seed43\\\": {}, \\\"eval-obs-only-object-norm01-seed60\\\": {}, \\\"eval-pi05-baseline-object-seed42\\\": {}, \\\"eval-obs-only-object-norm01-seed54\\\": {}, \\\"eval-obs-only-object-norm01-seed53\\\": {}, \\\"eval-obs-only-object-norm01-seed52\\\": {}, \\\"eval-obs-only-object-norm01-seed50\\\": {}, \\\"eval-obs-only-object-norm01-seed49\\\": {}, \\\"eval-obs-only-object-norm01-seed48\\\": {}, \\\"eval-obs-only-object-norm01-seed47\\\": {}, \\\"eval-obs-only-object-norm01-seed45-r2\\\": {}, \\\"eval-obs-only-object-norm01-seed44\\\": {}, \\\"eval-obs-only-object-norm005-seed55\\\": {}, \\\"eval-obs-only-object-norm005-seed50\\\": {}, \\\"eval-obs-only-object-norm005-seed49\\\": {}, \\\"eval-obs-only-object-norm005-seed48\\\": {}, \\\"eval-obs-only-object-norm005-seed47\\\": {}, \\\"eval-obs-only-object-norm005-seed44\\\": {}, \\\"eval-obs-only-object-norm005-seed43-r2\\\": {}, \\\"eval-obs-only-object-norm005-seed43\\\": {}, \\\"eval-obs-only-object-norm003-seed48\\\": {}, \\\"eval-obs-only-object-norm003-seed47-r2\\\": {}, \\\"eval-obs-only-object-norm003-seed46\\\": {}, \\\"eval-obs-only-object-norm003-seed45\\\": {}, \\\"eval-obs-only-object-norm003-seed44-bjb2\\\": {}, \\\"eval-obs-only-object-norm003-seed44\\\": {}, \\\"eval-obs-only-object-norm003-seed43-r2\\\": {}, \\\"eval-obs-only-object-norm003-seed43\\\": {}, \\\"eval-obs-only-object-norm01-seed57\\\": {}, \\\"eval-obs-only-object-norm005-seed65\\\": {}, \\\"eval-obs-only-object-norm005-seed61\\\": {}, \\\"eval-obs-only-object-norm005-seed58\\\": {}, \\\"eval-obs-only-object-norm003-seed59\\\": {}, \\\"eval-obs-only-object-norm003-seed56\\\": {}, \\\"eval-obs-only-object-norm005-seed75\\\": {}, \\\"eval-obs-only-object-norm01-seed74\\\": {}, \\\"eval-obs-only-object-norm005-seed72\\\": {}, \\\"eval-obs-only-object-norm003-seed63-r2\\\": {}, \\\"eval-obs-only-object-norm01-seed71\\\": {}, \\\"eval-obs-only-object-norm003-seed62-r2\\\": {}, \\\"eval-obs-only-object-norm003-seed73\\\": {}, \\\"eval-obs-only-object-norm01-seed51-r3\\\": {}, \\\"eval-obs-only-object-norm01-seed52-r3\\\": {}, \\\"eval-obs-only-object-norm01-seed65\\\": {}, \\\"eval-obs-only-object-norm01-seed64\\\": {}, \\\"eval-obs-only-object-norm005-seed64\\\": {}, \\\"eval-obs-only-object-norm003-seed65\\\": {}, \\\"eval-obs-only-object-norm003-seed64\\\": {}, \\\"eval-obs-only-object-norm005-seed62\\\": {}, \\\"eval-obs-only-object-norm005-seed63\\\": {}, \\\"eval-obs-only-object-norm01-seed61\\\": {}, \\\"eval-obs-only-object-norm003-seed64-bjb2\\\": {}, \\\"eval-obs-only-object-norm003-seed63\\\": {}, \\\"eval-obs-only-object-norm003-seed62\\\": {}, \\\"eval-obs-only-object-norm01-seed51-r2\\\": {}, \\\"eval-obs-only-object-norm01-seed52-r2\\\": {}, \\\"eval-obs-only-object-norm01-seed51\\\": {}, \\\"eval-obs-only-object-norm005-seed49-r2\\\": {}, \\\"eval-obs-only-object-norm005-seed55-r2\\\": {}, \\\"eval-openvla-crm-object-seed42\\\": {}, \\\"eval-obs-only-object-norm003-seed44-r2\\\": {}, \\\"eval-random-selection-object-seed49\\\": {}, \\\"eval-random-selection-object-seed48\\\": {}, \\\"eval-k5-obs-only-object-seed44\\\": {}, \\\"eval-obs-only-spatial-norm02-seed52\\\": {}, \\\"eval-obs-only-object-norm02-seed54\\\": {}, \\\"D088-eval-adaptive-unc-head-object-seed44\\\": {}, \\\"D088-eval-adaptive-unc-head-object-seed43\\\": {}, \\\"D088-eval-adaptive-unc-head-object-seed42\\\": {}, \\\"eval-adaptive-unc-head-object-seed42\\\": {}, \\\"eval-adaptive-unc-head-object-seed43\\\": {}, \\\"eval-perdof-object-norm02-seed50\\\": {}, \\\"eval-adaptive-unc-head-object-seed44\\\": {}, \\\"eval-random-selection-spatial-seed42-r3\\\": {}, \\\"eval-obs-only-spatial-norm02-seed50\\\": {}, \\\"train-crm-openvla-obs-only\\\": {}, \\\"openvla-precompute-k1\\\": {}, \\\"eval-random-selection-object-seed46-r3\\\": {}, \\\"eval-perdof-object-norm02-seed49\\\": {}, \\\"eval-random-selection-object-seed47\\\": {}, \\\"eval-obs-only-spatial-norm02-seed42-r2\\\": {}, \\\"eval-k5-obs-only-object-seed43\\\": {}, \\\"eval-random-selection-spatial-seed43-r2\\\": {}, \\\"eval-random-selection-spatial-seed44\\\": {}, \\\"eval-crm-k1-object-seed43-plan702\\\": {}, \\\"eval-crm-k1-object-seed42-plan702\\\": {}, \\\"eval-crm-k1-object-seed44-plan702\\\": {}, \\\"eval-random-selection-object-seed46-r2\\\": {}, \\\"eval-random-selection-spatial-seed43\\\": {}, \\\"eval-random-selection-object-seed46\\\": {}, \\\"eval-obs-only-spatial-seed48\\\": {}, \\\"eval-vla-only-spatial-seed48\\\": {}, \\\"eval-obs-only-spatial-norm02-seed42\\\": {}, \\\"eval-obs-only-spatial-norm02-seed49\\\": {}, \\\"eval-adaptive-k-spatial-p90-seed44\\\": {}, \\\"eval-argmin-object-seed50\\\": {}, \\\"eval-vla-only-object-seed48-r2\\\": {}, \\\"eval-vla-only-goal-seed51\\\": {}, \\\"eval-random-selection-spatial-seed42-r2\\\": {}, \\\"eval-random-selection-object-seed45\\\": {}, \\\"eval-crm-k1-object-seed44-plan702-r2\\\": {}, \\\"eval-crm-k1-object-seed43-plan702-r2\\\": {}, \\\"eval-crm-k1-object-seed42-plan702-r2\\\": {}, \\\"eval-perdof-object-norm02-seed48\\\": {}, \\\"eval-argmin-object-k5-seed44-r2\\\": {}, \\\"eval-vla-only-goal-seed44-r2\\\": {}, \\\"eval-obs-only-spatial-norm02-seed46-r2\\\": {}, \\\"eval-latency-profiling-v1\\\": {}, \\\"eval-adaptive-k-spatial-p75-seed44\\\": {}, \\\"eval-obs-only-goal-norm02-seed51\\\": {}, \\\"eval-adaptive-k-spatial-p25-seed44\\\": {}, \\\"eval-openvla-object-baseline-seed42\\\": {}, \\\"eval-argmin-object-seed49\\\": {}, \\\"eval-argmin-object-seed48\\\": {}, \\\"eval-obs-only-spatial-norm02-seed48\\\": {}, \\\"eval-obs-only-goal-norm02-seed52\\\": {}, \\\"eval-adaptive-k-spatial-p90-seed43\\\": {}, \\\"eval-perdof-object-norm02-seed45-r3\\\": {}, \\\"eval-adaptive-k-spatial-p90-seed42\\\": {}, \\\"eval-obs-only-object-norm02-seed49\\\": {}, \\\"eval-vla-only-goal-seed47\\\": {}, \\\"eval-adaptive-k-spatial-p50-seed44\\\": {}, \\\"eval-adaptive-k-spatial-p50-seed43\\\": {}, \\\"eval-adaptive-k-spatial-p50-seed42\\\": {}, \\\"eval-adaptive-k-spatial-p25-seed42\\\": {}, \\\"eval-adaptive-k-spatial-p25-seed43\\\": {}, \\\"eval-adaptive-k-spatial-p75-seed43\\\": {}, \\\"eval-crm-object-k20-seed43\\\": {}, \\\"eval-vla-only-long-seed49-r2\\\": {}, \\\"eval-adaptive-k-spatial-p75-seed42\\\": {}, \\\"eval-adaptive-k-spatial-p50-seed44-r2\\\": {}, \\\"eval-adaptive-k-p75-seed42\\\": {}, \\\"eval-adaptive-k-p75-seed43\\\": {}, \\\"eval-adaptive-k-p50-seed42\\\": {}, \\\"eval-adaptive-k-p50-seed43\\\": {}, \\\"eval-random-selection-object-seed42\\\": {}, \\\"eval-adaptive-k-spatial-p50-seed43-r2\\\": {}, \\\"eval-obs-only-object-norm02-seed42\\\": {}, \\\"latency-profile-n1000\\\": {}, \\\"eval-adaptive-k-p90-seed44\\\": {}, \\\"eval-adaptive-k-p25-seed43\\\": {}, \\\"eval-crm-spatial-k10-seed51\\\": {}, \\\"eval-vla-only-goal-seed49\\\": {}, \\\"eval-vla-only-long-seed52\\\": {}, \\\"eval-vla-only-long-seed51\\\": {}, \\\"eval-vla-only-long-seed50\\\": {}, \\\"eval-crm-long-seed50\\\": {}, \\\"eval-adaptive-k-p25-seed44-r2\\\": {}, \\\"calibrate-crm-correction-signal\\\": {}, \\\"eval-adaptive-k-p25-seed42\\\": {}, \\\"eval-vla-only-goal-seed48-r2\\\": {}, \\\"eval-vla-only-goal-seed47-r2\\\": {}, \\\"eval-crm-goal-seed46\\\": {}, \\\"eval-adaptive-k-p50-seed44\\\": {}, \\\"eval-adaptive-k-p75-seed44\\\": {}, \\\"eval-adaptive-k-p90-seed43\\\": {}, \\\"eval-adaptive-k-p90-seed42\\\": {}, \\\"eval-vla-only-spatial-seed47\\\": {}, \\\"eval-crm-long-seed47\\\": {}, \\\"eval-vla-only-long-seed48\\\": {}, \\\"eval-crm-long-seed46\\\": {}, \\\"eval-crm-goal-seed45-r2\\\": {}, \\\"eval-crm-goal-seed44-r2\\\": {}, \\\"eval-obs-only-spatial-norm02-seed43-r2\\\": {}, \\\"k2-l2-calibration-phase1\\\": {}, \\\"eval-crm-long-seed45\\\": {}, \\\"eval-vla-only-spatial-seed49\\\": {}, \\\"eval-vla-only-goal-seed48\\\": {}, \\\"eval-vla-only-goal-seed43\\\": {}, \\\"eval-vla-only-goal-seed42\\\": {}, \\\"eval-vla-only-object-seed47\\\": {}, \\\"eval-crm-long-seed44\\\": {}, \\\"eval-crm-long-seed43\\\": {}, \\\"eval-crm-long-seed42\\\": {}, \\\"eval-crm-goal-seed42\\\": {}, \\\"eval-crm-goal-seed43\\\": {}, \\\"eval-vla-only-spatial-seed46\\\": {}, \\\"eval-vla-only-long-seed47\\\": {}, \\\"eval-crm-goal-seed45\\\": {}, \\\"eval-crm-goal-seed44\\\": {}, \\\"eval-vla-only-goal-seed45\\\": {}, \\\"eval-vla-only-goal-seed46\\\": {}, \\\"eval-vla-only-long-seed46\\\": {}, \\\"fmvd-calibration-phase1\\\": {}, \\\"eval-vla-only-long-seed45\\\": {}, \\\"eval-perdof-object-norm003-seed47\\\": {}, \\\"eval-perdof-object-norm005-seed47\\\": {}, \\\"eval-vla-only-long-seed44\\\": {}, \\\"eval-vla-only-long-seed42\\\": {}, \\\"eval-vla-only-long-seed43\\\": {}, \\\"eval-obs-only-spatial-norm02-seed43\\\": {}, \\\"eval-obs-only-spatial-norm02-seed47\\\": {}, \\\"eval-obs-only-spatial-norm02-seed46\\\": {}, \\\"eval-argmin-object-k5-seed44\\\": {}, \\\"eval-vla-only-goal-seed44\\\": {}, \\\"eval-random-selection-object-k5-seed45-r2\\\": {}, \\\"eval-random-selection-object-k5-seed44-r2\\\": {}, \\\"eval-random-selection-object-k5-seed43-r2\\\": {}, \\\"eval-random-selection-object-k5-seed42-r2\\\": {}, \\\"eval-obs-only-spatial-norm02-k5-seed44-r2\\\": {}, \\\"eval-obs-only-spatial-norm02-k5-seed45-r2\\\": {}, \\\"plan_602-latency-profiling\\\": {}, \\\"eval-vla-only-spatial-seed45\\\": {}, \\\"eval-perdof-object-norm005-seed45-r2\\\": {}, \\\"eval-vla-only-spatial-seed44\\\": {}, \\\"eval-obs-only-object-default-seed48-r2\\\": {}, \\\"eval-vla-only-spatial-seed43\\\": {}, \\\"eval-vla-only-spatial-seed42\\\": {}, \\\"eval-obs-only-spatial-norm02-k5-seed45\\\": {}, \\\"eval-obs-only-spatial-norm02-k5-seed44\\\": {}, \\\"eval-random-selection-object-k5-seed45\\\": {}, \\\"eval-random-selection-object-k5-seed44\\\": {}, \\\"eval-random-selection-object-k5-seed43\\\": {}, \\\"eval-random-selection-object-k5-seed42\\\": {}, \\\"eval-obs-only-spatial-norm02-seed44\\\": {}, \\\"eval-perdof-object-norm01-seed43\\\": {}, \\\"eval-obs-only-object-default-seed45-r2\\\": {}, \\\"eval-argmin-object-k5-seed42\\\": {}, \\\"eval-argmin-object-k5-seed45\\\": {}, \\\"eval-argmin-object-k5-seed43\\\": {}, \\\"eval-perdof-object-norm03-seed43\\\": {}, \\\"eval-obs-only-spatial-norm02-seed45\\\": {}, \\\"train-crm-k1-accg-object-seed42-full\\\": {}, \\\"plan_701-precompute-k1-spatial\\\": {}, \\\"plan_701-crm-k1-train\\\": {}, \\\"eval_obs_only_norm03_seed48\\\": {}, \\\"eval_obs_only_norm01_seed48\\\": {}, \\\"eval-lto-splitA-vla-only-r3\\\": {}, \\\"eval-lto-splitA-vla-only-r2\\\": {}, \\\"eval-lto-splitA-heldout-r2\\\": {}, \\\"crm-lto-splitA-train\\\": {}, \\\"eval-perdof-object-norm003-seed48\\\": {}, \\\"eval-scalar-object-seed45-r2\\\": {}, \\\"eval-obs-only-spatial-norm02-k5-seed43\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed48\\\": {}, \\\"eval-obs-only-spatial-norm02-k5-seed42\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed46\\\": {}, \\\"eval-lto-splitA-vla-only-v2\\\": {}, \\\"eval-lto-splitA-heldout-v2\\\": {}, \\\"eval-perdof-object-default-seed47\\\": {}, \\\"eval-perdof-object-norm03-seed47\\\": {}, \\\"eval-obs-only-object-default-seed48\\\": {}, \\\"eval-perdof-object-norm003-seed46\\\": {}, \\\"eval-perdof-object-norm005-seed46\\\": {}, \\\"eval-perdof-object-norm003-seed45\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed47\\\": {}, \\\"eval-perdof-object-norm01-seed48\\\": {}, \\\"eval-obs-only-object-default-seed47\\\": {}, \\\"eval-perdof-object-norm03-seed46\\\": {}, \\\"eval-obs-only-object-norm03-seed46\\\": {}, \\\"eval-scalar-object-seed46\\\": {}, \\\"eval-obs-only-object-norm003-seed45-r2\\\": {}, \\\"eval-lto-splitA-vla-only\\\": {}, \\\"eval-lto-splitA-heldout\\\": {}, \\\"eval-obs-only-object-norm005-seed46\\\": {}, \\\"eval-perdof-object-norm03-seed48\\\": {}, \\\"eval-obs-only-object-norm003-seed49\\\": {}, \\\"crm-lto-splitA-train-fixed\\\": {}, \\\"eval-obs-only-object-norm003-seed47\\\": {}, \\\"eval-perdof-object-norm003-seed43\\\": {}, \\\"eval-perdof-object-norm005-seed43\\\": {}, \\\"eval-perdof-object-default-seed43\\\": {}, \\\"eval-perdof-object-default-seed45\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed45\\\": {}, \\\"eval-perdof-object-norm005-seed45\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed44\\\": {}, \\\"eval-perdof-object-norm003-seed44-r2\\\": {}, \\\"eval-obs-only-object-norm01-seed46-r3\\\": {}, \\\"eval-perdof-object-norm005-seed44\\\": {}, \\\"eval-vla-only-object-seed45-r2\\\": {}, \\\"eval-obs-only-object-norm03-seed48\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed43\\\": {}, \\\"eval-perdof-object-norm01-seed42-r2\\\": {}, \\\"eval-obs-only-object-norm01-seed42-r2\\\": {}, \\\"eval-perdof-object-norm02-seed43\\\": {}, \\\"eval-perdof-object-norm01-seed46\\\": {}, \\\"eval-obs-only-object-norm01-seed45\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed42\\\": {}, \\\"eval-perdof-object-default-seed46\\\": {}, \\\"eval-perdof-object-default-seed44\\\": {}, \\\"eval-mag-perdof-norm02\\\": {}, \\\"eval-acr-spatial-v4-scalar\\\": {}, \\\"eval-acr-spatial-v4-small\\\": {}, \\\"eval-acr-spatial-v4-obs-only-r2\\\": {}, \\\"eval-argmin-only-spatial\\\": {}, \\\"eval-acr-spatial-v3\\\": {}, \\\"eval-acr-object-v3\\\": {}, \\\"eval-openvla-object-vla-only-seed42\\\": {}, \\\"eval-perdof-object-norm02-seed47\\\": {}, \\\"eval-obs-only-object-norm02-seed48\\\": {}, \\\"eval-obs-only-object-default-seed46\\\": {}, \\\"eval-perdof-object-norm02-seed46\\\": {}, \\\"eval-obs-only-object-norm01-seed46\\\": {}, \\\"mag_obs_only_norm01_seed47\\\": {}, \\\"mag_obs_only_norm01_seed46\\\": {}, \\\"eval-perdof-object-norm02-seed43-r3\\\": {}, \\\"mag_perdof_norm02_seed43_r3\\\": {}, \\\"eval-perdof-object-norm01-seed47-bjb1\\\": {}, \\\"eval-openvla-object-vla-only-seed42-v2\\\": {}, \\\"eval-k1-crm-multiscale-object-seed44-r2\\\": {}, \\\"eval-k1-crm-multiscale-object-seed44\\\": {}, \\\"eval-k1-crm-multiscale-object-seed43\\\": {}, \\\"eval-k1-crm-multiscale-object-seed42\\\": {}, \\\"eval-perdof-object-norm01-seed46-r2\\\": {}, \\\"eval-k1-crm-multiscale-object-seed43-r2\\\": {}, \\\"eval-perdof-object-norm02-seed45-r2\\\": {}, \\\"eval-obs-only-object-norm005-seed43-r3\\\": {}, \\\"plan_602-latency-profile\\\": {}, \\\"train-crm-k1-accg-object-seed42-v2\\\": {}, \\\"eval-k1-crm-accg-object-seed44\\\": {}, \\\"eval-k1-crm-accg-object-seed43\\\": {}, \\\"eval-k1-crm-accg-object-seed42\\\": {}, \\\"eval-obs-only-object-default-seed45\\\": {}, \\\"eval-scalar-object-seed45\\\": {}, \\\"eval-perdof-object-norm02-seed45\\\": {}, \\\"eval-perdof-object-norm02-seed44\\\": {}, \\\"train-crm-k1-accg-object-seed42-fallback\\\": {}, \\\"train-crm-k1-accg-object-seed42\\\": {}, \\\"eval-perdof-object-norm02-seed45-deploy\\\": {}, \\\"eval-obs-only-object-norm01-seed47-r2\\\": {}, \\\"eval-perdof-object-norm03-seed45-r2\\\": {}, \\\"eval-perdof-object-norm03-seed44-r2\\\": {}, \\\"eval-obs-only-object-norm03-seed47\\\": {}, \\\"eval-perdof-object-norm03-seed46-r2\\\": {}, \\\"eval-perdof-object-norm01-seed44\\\": {}, \\\"eval-obs-only-object-norm01-seed47-bjb2\\\": {}, \\\"eval-obs-only-object-norm01-seed46-bjb2\\\": {}, \\\"eval-argmin-object-seed47\\\": {}, \\\"eval-perdof-object-norm01-seed45\\\": {}, \\\"eval-perdof-object-norm01-seed47\\\": {}, \\\"eval-argmin-object-seed46\\\": {}, \\\"eval-obs-only-object-norm03-seed45-r2\\\": {}, \\\"eval-vla-mean-object-seed45\\\": {}, \\\"eval-argmin-object-seed45\\\": {}, \\\"eval-direct-correction-object-seed42-r3\\\": {}, \\\"eval-perdof-object-norm03-seed44\\\": {}, \\\"eval-mag-perdof-norm02-object\\\": {}, \\\"eval-acr-object-v4-scalar\\\": {}, \\\"eval-mag-obsonly-norm02\\\": {}, \\\"eval-mag-perdof-norm03\\\": {}, \\\"eval-mag-perdof-norm005\\\": {}, \\\"eval-mag-perdof-norm003\\\": {}, \\\"eval-vla-mean-spatial\\\": {}, \\\"eval-acr-object-obs-only-norm02\\\": {}, \\\"eval-spatial-v7-full\\\": {}, \\\"eval-object-v8-full\\\": {}, \\\"precompute-v5-shard2\\\": {}, \\\"precompute-v5-shard1\\\": {}, \\\"precompute-v5-shard0\\\": {}, \\\"precompute-v4-shard2\\\": {}, \\\"precompute-v4-shard1\\\": {}, \\\"precompute-v4-shard0\\\": {}, \\\"eval-vla-mean-spatial-t10\\\": {}, \\\"eval-reconvla-spatial-v3\\\": {}, \\\"crm-train-v2-scalar-unc\\\": {}, \\\"crm-train-v2-perdof\\\": {}, \\\"crm-train-v2-obs-only\\\": {}, \\\"precompute-shard2\\\": {}, \\\"precompute-shard1\\\": {}, \\\"precompute-shard0\\\": {}, \\\"precompute-k5\\\": {}, \\\"plan_014-reconvla-baseline\\\": {}, \\\"plan_001-crm-smolvla\\\": {}, \\\"mvp-point-reaching\\\": {}, \\\"eval-smolvla-libero-spatial\\\": {}, \\\"eval-obs-only-spatial\\\": {}, \\\"eval-obs-only-object-default-seed44\\\": {}, \\\"eval-mag-perdof-norm005-object\\\": {}, \\\"eval-mag-perdof-norm02-seed43-object-r3\\\": {}, \\\"eval-mag-perdof-norm03-object-r3\\\": {}, \\\"eval-mag-obsonly-norm005\\\": {}, \\\"eval-mag-obsonly-norm003-b2\\\": {}, \\\"eval-mag-obsonly-norm03-object\\\": {}, \\\"eval-mag-obsonly-norm005-object\\\": {}, \\\"eval-direct-correction-object-seed42-r2\\\": {}, \\\"eval-direct-correction-object-seed42\\\": {}, \\\"eval-scalar-object-seed44-r2\\\": {}, \\\"eval-perdof-object-seed44\\\": {}, \\\"eval-obs-only-object-norm03-seed44\\\": {}, \\\"eval-vla-mean-object-seed44\\\": {}, \\\"eval-obs-only-object-norm02-seed44-r4\\\": {}, \\\"eval-argmin-object-seed44-r2\\\": {}, \\\"eval-obs-only-object-norm03-seed45\\\": {}, \\\"eval-acr-object-v4-default-r2\\\": {}, \\\"eval-mag-perdof-norm003-object\\\": {}, \\\"eval-acr-object-obs-only-default\\\": {}, \\\"eval-scalar-object-seed43\\\": {}, \\\"eval-mag-obsonly-norm003-object\\\": {}, \\\"eval-scalar-object-seed44\\\": {}, \\\"eval-obs-only-object-norm02-seed44-r3\\\": {}, \\\"eval-argmin-object-seed44-r3\\\": {}, \\\"eval-vla-mean-object-seed43\\\": {}, \\\"eval-perdof-object-seed43\\\": {}, \\\"eval-vla-only-object-seed44\\\": {}, \\\"eval-obs-only-object-norm02-seed44\\\": {}, \\\"eval-argmin-object-seed44\\\": {}, \\\"eval-obs-only-object-seed43\\\": {}, \\\"eval-mag-obsonly-norm03-b2\\\": {}, \\\"eval-argmin-object-seed43\\\": {}, \\\"eval-mag-perdof-norm02-seed43-object-r2\\\": {}, \\\"eval-mag-obsonly-norm03\\\": {}, \\\"eval-mag-obsonly-norm02-object\\\": {}, \\\"eval-mag-obsonly-norm03-b4\\\": {}, \\\"eval-mag-obsonly-norm03-b3\\\": {}, \\\"eval-mag-perdof-norm02-seed43-object\\\": {}, \\\"eval-mag-perdof-norm03-object-r2\\\": {}, \\\"eval-acr-object-v4-scalar-b2\\\": {}, \\\"eval-acr-object-v4-obs-only-b2\\\": {}, \\\"eval-spatial-v4-full\\\": {}, \\\"eval-reconvla-spatial-v1\\\": {}, \\\"eval-object-v6-full\\\": {}, \\\"precompute-v3-shard2\\\": {}, \\\"precompute-v3-shard1\\\": {}, \\\"precompute-v3-shard0\\\": {}, \\\"precompute-v2-shard2\\\": {}, \\\"precompute-v2-shard1\\\": {}, \\\"precompute-v2-shard0\\\": {}, \\\"eval-mag-perdof-norm0p3-object-r2\\\": {}, \\\"eval-mag-perdof-norm0p3-object\\\": {}, \\\"eval-obs-only-object-norm02-seed43\\\": {}, \\\"eval-acr-object-v4-default\\\": {}, \\\"eval-mag-obsonly-norm03-r2\\\": {}, \\\"eval-vla-mean-object\\\": {}, \\\"eval-reconvla-object\\\": {}, \\\"eval-acr-object-v4-obs-only\\\": {}, \\\"eval-acr-object-v4-perdof\\\": {}, \\\"eval-acr-spatial-v4-scalar-r2\\\": {}, \\\"eval-acr-spatial-v4-obs-only-r3\\\": {}, \\\"eval-obs-only-spatial-seed43\\\": {}, \\\"eval-acr-spatial-v4-small-r2\\\": {}, \\\"eval-mag-obsonly-norm-0.3-r3\\\": {}, \\\"eval-mag-obsonly-norm-0p3-r3\\\": {}, \\\"eval-argmin-only-spatial-r2\\\": {}, \\\"eval-mag-obsonly-norm003\\\": {}, \\\"eval-vla-only-object-k1\\\": {}, \\\"eval-acr-spatial-v4-default-r3\\\": {}, \\\"eval-tiny-correction-spatial\\\": {}, \\\"eval-acr-spatial-v4-default-r2\\\": {}, \\\"eval-acr-spatial-v4-obs-only\\\": {}, \\\"eval-acr-spatial-v4-default\\\": {}, \\\"crm-train-v3-norm-scalar-unc\\\": {}, \\\"crm-train-v3-norm-obs-only\\\": {}, \\\"crm-train-v3-norm\\\": {}, \\\"crm-train-v3-scalar-unc\\\": {}, \\\"crm-train-v3-obs-only\\\": {}, \\\"crm-train-v3-perdof\\\": {}, \\\"eval-obs-only-spatial-v3\\\": {}, \\\"eval-scalar-unc-spatial-v2\\\": {}, \\\"crm-train-a4-scalar-unc\\\": {}, \\\"crm-train-a3-obs-only\\\": {}, \\\"crm-train-v1\\\": {}, \\\"crm-train-k5\\\": {}, \\\"eval-scalar-unc-spatial\\\": {}, \\\"eval-acr-spatial-v2\\\": {}, \\\"eval-k5-spatial\\\": {}, \\\"eval-object-v7-full\\\": {}, \\\"eval-spatial-v6-full\\\": {}, \\\"eval-object-v5-full\\\": {}, \\\"eval-acr-vla-spatial-v1\\\": {}, \\\"eval-acr-spatial-v1\\\": {}, \\\"eval-reconvla-spatial-v2\\\": {}, \\\"eval-object-v4-full\\\": {}, \\\"eval-spatial-v5-full\\\": {}, \\\"eval-spatial-v3-full\\\": {}, \\\"eval-spatial-reeval-v2\\\": {}}, \\\"count\\\": 1223, \\\"total\\\": 1223, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.5652}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"smolvla-tau020-long-s42\": {}, \"smolvla-tau015-spatial-s42-fix\": {}, \"crm-always-on-long-s45\": {}, \"pi05-crm-always-on-object-s43\": {}, \"smolvla-tau045-long-s42\": {}, \"smolvla-tau040-long-s42\": {}, \"pi05-crm-always-on-object-s42\": {}, \"pi05-crm-always-on-goal-s42\": {}, \"smolvla-tau020-long-s43-r2\": {}, \"eval-tau005-spatial-s42\": {}, \"pi05-crm-always-on-spatial-s42\": {}, \"eval-tau040-spatial-s42\": {}, \"eval-tau045-spatial-s42\": {}, \"crm-always-on-object-s46\": {}, \"smolvla-tau005-long-s42\": {}, \"crm-always-on-object-s45\": {}, \"smolvla-tau010-long-s42\": {}, \"pi05-tau-sweep-goal-tau070-s42-r2\": {}, \"pi05-tau-sweep-goal-tau050-s42-r2\": {}, \"pi05-goal-tau035-s43-r3\": {}, \"crm-always-on-long-s44\": {}, \"crm-always-on-spatial-s46\": {}, \"crm-always-on-goal-s46\": {}, \"crm-always-on-goal-s45\": {}, \"crm-always-on-spatial-s45\": {}, \"pi05-goal-tau025-s43-r3\": {}, \"pi05-tau-sweep-goal-tau050-s42-r3\": {}, \"pi05-goal-tau015-s43-r3\": {}, \"smolvla-tau035-long-s42\": {}, \"smolvla-tau030-long-s42\": {}, \"smolvla-tau015-long-s42\": {}, \"smolvla-tau045-object-s42\": {}, \"smolvla-tau040-object-s42\": {}, \"smolvla-tau030-object-s42\": {}, \"crm-always-on-long-s43\": {}, \"crm-always-on-long-s42\": {}, \"smolvla-tau025-long-s42\": {}, \"pi05-long-tau015-s43-r3\": {}, \"pi05-k2mean-spatial-s42-r3\": {}, \"pi05-k2mean-long-s42-r3\": {}, \"pi05-k2mean-object-s42-r3\": {}, \"smolvla-tau035-object-s42-r3\": {}, \"smolvla-tau025-object-s42-r3\": {}, \"smolvla-tau020-object-s42\": {}, \"smolvla-tau010-object-s42\": {}, \"smolvla-tau005-object-s42\": {}, \"crm-always-on-goal-s43\": {}, \"crm-always-on-goal-s42\": {}, \"crm-always-on-spatial-s44\": {}, \"crm-always-on-spatial-s43\": {}, \"smolvla-tau030-long-s42-r2\": {}, \"smolvla-tau030-long-s43-r2\": {}, \"tau-sweep-goal-tau035-s42\": {}, \"tau-sweep-long-tau015-s42\": {}, \"tau-sweep-long-tau035-s42\": {}, \"smolvla-tau020-long-s42-r2\": {}, \"tau-sweep-goal-tau015-s42\": {}, \"tau-sweep-spatial-tau035-s42\": {}, \"tau-sweep-spatial-tau015-s42\": {}, \"smolvla-tau035-object-s42-r2\": {}, \"smolvla-tau035-object-s43-r3\": {}, \"smolvla-tau025-object-s43-r3\": {}, \"crm-always-on-spatial-s42\": {}, \"crm-always-on-goal-s44\": {}, \"crm-always-on-object-s44\": {}, \"crm-always-on-object-s43\": {}, \"crm-always-on-object-s42\": {}, \"eval-obs-object-norm003-s45\": {}, \"eval-obs-object-norm005-s45\": {}, \"eval-obs-object-norm003-s46\": {}, \"pi05-k2mean-goal-s43\": {}, \"pi05-k2mean-long-s42\": {}, \"pi05-k2mean-object-s42\": {}, \"pi05-vla-only-spatial-s42-4090\": {}, \"pi05-vla-only-goal-s42-4090\": {}, \"pi05-k2mean-spatial-s42\": {}, \"pi05-vla-only-spatial-s42-4090-r2\": {}, \"pi05-vla-only-object-s42-4090-r2\": {}, \"pi05-vla-only-goal-s42-4090-r2\": {}, \"eval-k2-tau010-015-spatial-s42\": {}, \"eval-k2-tau010-spatial-s42\": {}, \"eval-pi05-vla-only-long-seed42-r4-std\": {}, \"eval-obs-only-object-norm02-k20-seed44\": {}, \"eval-obs-only-object-norm02-k20-seed43\": {}, \"eval-obs-only-object-norm02-k20-seed42\": {}, \"eval-pi05-baseline-object-seed42-r2\": {}, \"pi05-vla-only-object-s42-4090\": {}, \"pi05-vla-only-long-s42-4090\": {}, \"smolvla-tau020-long-s43\": {}, \"smolvla-tau030-long-s43\": {}, \"eval-pi05-vla-only-object-s43-r5\": {}, \"eval-perdof-object-norm005-s44-westd\": {}, \"eval-perdof-object-norm003-s44-westd\": {}, \"eval-obs-object-norm005-s45-bjb2\": {}, \"eval-obs-object-norm005-s44-bjb2\": {}, \"eval-obs-object-norm003-s44-bjb2\": {}, \"eval-obs-object-norm005-s43-bjb2\": {}, \"eval-obs-object-norm003-s43-bjb2\": {}, \"eval-obs-object-norm005-s46\": {}, \"eval-perdof-object-norm005-s43-v3\": {}, \"eval-perdof-object-norm003-s43-v3\": {}, \"pi05-vla-only-goal-s44-4090\": {}, \"pi05-vla-only-object-s43-4090\": {}, \"pi05-vla-only-long-s44-4090\": {}, \"pi05-vla-only-long-s43-4090\": {}, \"pi05-vla-only-long-s42-4090-r3\": {}, \"eval-ksweep-k5-obs-object-s43\": {}, \"eval-obs-object-norm005-s44-westd\": {}, \"eval-k2-tau035-spatial-s42-v2\": {}, \"eval-obs-object-norm005-s43-westd\": {}, \"eval-obs-object-norm003-s43\": {}, \"eval-obs-object-norm005-s43\": {}, \"eval-obs-object-norm003-s44\": {}, \"eval-ksweep-k20-obs-object-s43\": {}, \"eval-ksweep-k20-obs-object-s42\": {}, \"eval-k2-tau025-spatial-s42-v2\": {}, \"eval-obs-object-norm003-s43-westd\": {}, \"eval-obs-object-norm003-s44-westd\": {}, \"eval-obs-object-norm005-s44\": {}, \"eval-ksweep-k5-obs-object-s42\": {}, \"smolvla-vla-only-long-n20-s43\": {}, \"smolvla-vla-only-long-n20-s42\": {}, \"pi05-object-adaptive-s44-cqa1\": {}, \"pi05-object-adaptive-s43-cqa1\": {}, \"pi05-object-adaptive-s42-cqa1\": {}, \"eval-pi05-vla-only-object-s43-v2\": {}, \"eval-pi05-vla-only-object-s42-v2\": {}, \"eval-pi05-vla-only-goal-s43-v2\": {}, \"eval-pi05-vla-only-goal-s42-v2\": {}, \"eval-pi05-vla-only-spatial-s43-v2\": {}, \"eval-pi05-vla-only-spatial-s42-v2\": {}, \"smolvla-tau025-long-s43\": {}, \"smolvla-tau015-long-s43\": {}, \"smolvla-tau025-object-s42-r2\": {}, \"smolvla-tau035-long-s43\": {}, \"pi05-goal-tau015-s43\": {}, \"smolvla-tau035-spatial-s43\": {}, \"smolvla-tau025-spatial-s43\": {}, \"smolvla-tau015-spatial-s43\": {}, \"pi05-goal-tau035-s43\": {}, \"pi05-goal-tau025-s43\": {}, \"pi05-adaptive-long-s43-cqa1-r3\": {}, \"pi05-spatial-tau015-s43\": {}, \"pi05-spatial-tau035-s43\": {}, \"pi05-spatial-tau025-s43\": {}, \"pi05-object-tau035-s42-bjb2\": {}, \"E_smolvla_crm_norm005_spatial_s42_d149\": {}, \"pi05-object-tau015-s42-bjb2\": {}, \"E_smolvla_adaptive_tau045_spatial_s42\": {}, \"E_smolvla_adaptive_tau035_spatial_s42\": {}, \"E_smolvla_adaptive_tau015_spatial_s42\": {}, \"pi05-adaptive-object-s42-tau045-bjb2\": {}, \"smolvla-tau035-spatial-s42-bjb1\": {}, \"smolvla-tau015-spatial-s42-bjb1\": {}, \"smolvla-crm-norm005-spatial-s42-d149\": {}, \"smolvla-tau045-spatial-s42\": {}, \"pi05-adaptive-long-s44-bjb1\": {}, \"pi05-adaptive-long-s43-bjb1\": {}, \"eval-k2-tau045-spatial-s42-bjb2\": {}, \"smolvla-crm-norm005-k10-object-s44-cqa1\": {}, \"smolvla-adapt-tau015-object-s44-cqa1\": {}, \"smolvla-adapt-tau015-object-s43-cqa1\": {}, \"smolvla-adapt-tau015-object-s42-cqa1\": {}, \"smolvla-tau015-object-s42\": {}, \"smolvla-tau025-object-s43\": {}, \"smolvla-tau035-goal-s42\": {}, \"smolvla-tau025-goal-s42\": {}, \"smolvla-tau015-goal-s42\": {}, \"smolvla-tau015-object-s43\": {}, \"smolvla-tau035-object-s43\": {}, \"pi05-adaptive-long-s42-tau035-bjb2\": {}, \"smolvla-tau015-goal-s43\": {}, \"smolvla-tau025-goal-s43\": {}, \"smolvla-tau035-goal-s43\": {}, \"pi05-adaptive-long-s42-tau015-bjb2\": {}, \"smolvla-tau035-object-s43-bjb1\": {}, \"smolvla-tau025-object-s43-bjb1\": {}, \"smolvla-tau015-object-s43-bjb1\": {}, \"smolvla-tau035-goal-s43-bjb1\": {}, \"smolvla-tau025-goal-s43-bjb1\": {}, \"smolvla-tau015-goal-s43-bjb1\": {}, \"pi05-adaptive-goal-s42-tau035-bjb2\": {}, \"westd-pi05-adaptive-object-s44-paired\": {}, \"westd-pi05-adaptive-object-s43-paired\": {}, \"westd-pi05-adaptive-object-s42-paired\": {}, \"westd-pi05-crm-k2-object-s44\": {}, \"westd-pi05-crm-k2-object-s43\": {}, \"westd-pi05-crm-k2-object-s42\": {}, \"eval-crm-goal-s43-d149-bjb1\": {}, \"eval-crm-object-s43-d149-bjb1\": {}, \"eval-crm-object-s42-d149-bjb1\": {}, \"eval-crm-spatial-s48-d149-bjb1\": {}, \"pi05-adaptive-long-s44-cqa1-r3\": {}, \"pi05-adaptive-object-s44-cqa1-r3\": {}, \"pi05-adaptive-object-s43-cqa1-r3\": {}, \"pi05-adaptive-goal-s42-tau015-bjb2\": {}, \"pi05-adaptive-spatial-s42-tau015-bjb2\": {}, \"pi05-adaptive-spatial-s42-tau035-bjb2\": {}, \"eval-crm-goal-s43-d149\": {}, \"eval-crm-goal-s44-d149\": {}, \"eval-crm-object-s42-d149\": {}, \"eval-crm-object-s43-d149\": {}, \"eval-crm-object-s44-d149\": {}, \"eval-crm-spatial-s48-d149\": {}, \"pi05-adaptive-long-s43-cqa1\": {}, \"eval-supp-goal-k2mean-s47\": {}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {}, \"eval-smolvla-lerobot-goal-seed43-v3\": {}, \"precompute-pi05-object-2048-r2\": {}, \"precompute-pi05-long-2048-r2\": {}, \"pi05-adaptive-long-s44-cqa1\": {}, \"eval-supp-goal-adapt-tau025-s47\": {}, \"eval-supp-goal-crm-norm005-s47\": {}, \"eval-supp-goal-reconvla-s47\": {}, \"eval-supp-obj-reconvla-s47\": {}, \"eval-supp-reconvla-obj-s45\": {}, \"eval-supp-spatial-k2mean-s46\": {}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {}, \"eval-supp-spatial-reconvla-s46\": {}, \"pi05-crm-k2-long-s44-cqa1\": {}, \"pi05-crm-k2-object-s42-bjb1-r2\": {}, \"pi05-crm-k2-object-s43-bjb1-r2\": {}, \"pi05-crm-k2-object-s44-bjb1-r2\": {}, \"pi05-adaptive-goal-s44-bjb1\": {}, \"pi05-adaptive-spatial-s44-bjb2-r2\": {}, \"pi05-adaptive-spatial-s43-bjb2-r2\": {}, \"pi05-adaptive-spatial-s42-bjb2-r2\": {}, \"pi05-crm-k2-spatial-s44-bjb2-r2\": {}, \"pi05-crm-k2-spatial-s43-bjb2-r2\": {}, \"pi05-crm-k2-spatial-s42-bjb2-r2\": {}, \"pi05-crm-k2-goal-s44-bjb1-r2\": {}, \"pi05-crm-k2-goal-s43-bjb1-r2\": {}, \"pi05-crm-k2-goal-s42-bjb1-r2\": {}, \"westd-pi05-vla-only-long-s44-paired\": {}, \"pi05-crm-k2-long-s42-r2\": {}, \"pi05-crm-k2-long-s43-r2\": {}, \"westd-pi05-vla-only-long-s43-paired\": {}, \"pi05-crm-k2-long-s43-cqa1\": {}, \"westd-pi05-vla-only-spatial-s43-paired\": {}, \"westd-pi05-vla-only-spatial-s42-paired\": {}, \"westd-pi05-vla-only-spatial-s44-paired\": {}, \"westd-pi05-vla-only-long-s42-paired\": {}, \"westd-pi05-vla-only-object-s44-paired\": {}, \"westd-pi05-vla-only-object-s43-paired\": {}, \"westd-pi05-vla-only-object-s42-paired\": {}, \"westd-pi05-vla-only-goal-s44-paired\": {}, \"westd-pi05-vla-only-goal-s43-paired\": {}, \"westd-pi05-vla-only-goal-s42-paired\": {}, \"pi05-adaptive-object-s42-cqa1\": {}, \"pi05-adaptive-long-s42-r2\": {}, \"pi05-adaptive-object-s43-bjb2-24035\": {}, \"pi05-adaptive-long-s44-cqa1-r2\": {}, \"pi05-adaptive-long-s43-cqa1-r2\": {}, \"pi05-adaptive-goal-s42-cqa1\": {}, \"westd-pi05-crm-k2-goal-s42\": {}, \"westd-pi05-adaptive-object-s42\": {}, \"westd-pi05-adaptive-goal-s43\": {}, \"westd-pi05-adaptive-goal-s42\": {}, \"pi05-adaptive-object-s44-cqa1-r2\": {}, \"pi05-adaptive-goal-s43-bjb1-18228\": {}, \"westd-pi05-adaptive-object-s43\": {}, \"pi05-crm-k2-spatial-s44-bjb2\": {}, \"pi05-crm-k2-spatial-s43-bjb2\": {}, \"pi05-crm-k2-spatial-s42-bjb2\": {}, \"pi05-adaptive-spatial-s44-bjb2\": {}, \"pi05-adaptive-spatial-s43-bjb2\": {}, \"pi05-adaptive-spatial-s42-bjb2\": {}, \"pi05-crm-k2-object-s44-bjb1\": {}, \"pi05-crm-k2-object-s43-bjb1\": {}, \"pi05-crm-k2-object-s42-bjb1\": {}, \"pi05-crm-k2-goal-s44-bjb1\": {}, \"pi05-crm-k2-goal-s43-bjb1\": {}, \"pi05-crm-k2-goal-s42-bjb1\": {}, \"eval-adaptive-spatial-s44-d149\": {}, \"eval-adaptive-spatial-s43-d149\": {}, \"eval-adaptive-goal-s44-d149\": {}, \"eval-adaptive-goal-s43-d149\": {}, \"eval-adaptive-object-s44-d149\": {}, \"eval-adaptive-object-s43-d149\": {}, \"eval-supp-crm-norm005-obj-s44\": {}, \"eval-adaptive-spatial-k1-s42\": {}, \"westd-pi05-vla-only-goal-s42\": {}, \"eval-supp-goal-vla-only-wrapper-s43\": {}, \"westd-pi05-adaptive-goal-s44\": {}, \"tau_sweep_goal_tau090_s42_cqa1\": {}, \"tau_sweep_goal_tau070_s42_cqa1\": {}, \"tau_sweep_goal_tau050_s42_cqa1\": {}, \"tau_sweep_spatial_tau025_s42\": {}, \"tau_sweep_goal_tau025_s42\": {}, \"tau_sweep_goal_tau040_s42\": {}, \"tau_sweep_goal_tau045_s42\": {}, \"goal_vla_only_s48\": {}, \"goal_adapt_s48\": {}, \"westd-pi05-k2mean-goal-s42\": {}, \"eval-goal-vla-only-s49-paired\": {}, \"eval-goal-adapt-tau025-s49-paired\": {}, \"eval-spatial-vla-only-s48-paired\": {}, \"eval-spatial-vla-only-s46-paired\": {}, \"eval-spatial-adapt-tau025-s48-paired\": {}, \"eval-spatial-adapt-tau025-s46-paired\": {}, \"pi05-adaptive-long-s42\": {}, \"pi05-adaptive-object-s42-v2\": {}, \"pi05-k2mean-goal-s42\": {}, \"pi05-crm-k2-long-s44\": {}, \"eval-k2-goal-vla-only-s49\": {}, \"eval-mechanism-goal-adapt-s42\": {}, \"pi05-crm-k2-long-s43\": {}, \"pi05-crm-k2-long-s42\": {}, \"eval-k2-tau030-spatial-s42\": {}, \"eval-k2-tau020-spatial-s42\": {}, \"eval-pi05-vla-spatial-s44\": {}, \"eval-pi05-adaptive-goal-s44\": {}, \"eval-pi05-adaptive-object-s44\": {}, \"eval-pi05-crm-object-s42\": {}, \"eval-pi05-crm-goal-s42\": {}, \"eval-pi05-crm-goal-s43\": {}, \"eval-pi05-crm-goal-s44\": {}, \"eval-pi05-crm-spatial-s42\": {}, \"eval-pi05-crm-spatial-s43\": {}, \"eval-pi05-crm-goal-s42-d149\": {}, \"eval-pi05-crm-spatial-s42-d149\": {}, \"eval-pi05-crm-spatial-s43-d149\": {}, \"eval-pi05-crm-goal-s43-d149\": {}, \"eval-pi05-crm-goal-s44-d149\": {}, \"eval-vla-only-long-s44-d149\": {}, \"eval-adaptive-long-s43-d149\": {}, \"eval-crm-long-s44-d149\": {}, \"eval-crm-long-s43-d149\": {}, \"eval-pi05-adaptive-object-s43\": {}, \"eval-pi05-adaptive-object-s42\": {}, \"eval-pi05-adaptive-goal-s43\": {}, \"eval-smolvla-crm-goal-s42\": {}, \"eval-crm-long-s42-d149\": {}, \"eval-pi05-vla-only-object-s43\": {}, \"eval-pi05-vla-only-goal-s44\": {}, \"eval-smolvla-crm-goal-seed44\": {}, \"eval-vla-only-spatial-bjb1-s49\": {}, \"eval-vla-only-spatial-bjb1-s48\": {}, \"eval-adaptive-long-s44-d149\": {}, \"eval-adaptive-long-s42-d149\": {}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {}, \"eval-k2-spatial-adapt-s44-paired-r2\": {}, \"eval-k2-spatial-adapt-s43-paired-r2\": {}, \"eval-k2-spatial-adapt-s42-paired-r2\": {}, \"eval-vla-only-spatial-s47-d149\": {}, \"eval-adaptive-object-s42-d149\": {}, \"eval-smolvla-crm-spatial-s47\": {}, \"eval-pi05-adaptive-goal-s42-dryrun\": {}, \"eval-adaptive-spatial-s47-bjb1-d149\": {}, \"eval-adaptive-spatial-s47-d149\": {}, \"eval-adaptive-goal-s42-d149\": {}, \"eval-pi05-vla-only-object-s42-r2\": {}, \"eval-pi05-adaptive-spatial-s42-r2\": {}, \"eval-pi05-vla-only-spatial-s44-d149\": {}, \"eval-pi05-adaptive-goal-s42\": {}, \"eval-k2-tau010-spatial-s42-r3\": {}, \"eval-k2-tau0075-spatial-s42\": {}, \"eval-k2-tau015-spatial-s42-r2\": {}, \"eval-k2-goal-vla-only-s46-paired\": {}, \"eval-k2-goal-vla-only-s45-paired\": {}, \"eval-k2-goal-adapt-s47-paired\": {}, \"eval-k2-goal-adapt-s46-paired\": {}, \"eval-k2-goal-vla-only-s47-paired\": {}, \"eval-k2-goal-adapt-s45-paired\": {}, \"eval-vla-only-spatial-bjb1-s46\": {}, \"eval-k2-adaptive-spatial-s49\": {}, \"eval-k2-adaptive-spatial-s48\": {}, \"eval-k2-adaptive-spatial-s46\": {}, \"eval-pi05-vla-only-spatial-s43-r2\": {}, \"eval-k2-adaptive-spatial-s43\": {}, \"eval-k2-adaptive-spatial-s42\": {}, \"eval-vla-only-spatial-cqa1-s44\": {}, \"eval-vla-only-spatial-cqa1-s43\": {}, \"eval-vla-only-spatial-cqa1-s42\": {}, \"eval-k2-adaptive-spatial-s44\": {}, \"eval-canonical-adaptive-k10-spatial-s42\": {}, \"eval-k10-tau025-spatial-s45\": {}, \"eval-k10-tau025-spatial-s47\": {}, \"eval-long-adaptive-k10-s42\": {}, \"eval-pi05-vla-only-spatial-s42-paired\": {}, \"eval-pi05-vla-only-goal-s42-paired\": {}, \"eval-long-adaptive-k10-s43\": {}, \"eval-long-adaptive-k10-s44\": {}, \"eval-canonical-adaptive-k10-spatial-s43\": {}, \"eval-canonical-adaptive-k10-spatial-s44\": {}, \"eval-canonical-adaptive-k10-spatial-s48\": {}, \"eval-canonical-adaptive-k10-spatial-s49\": {}, \"eval-k10-tau025-spatial-s46\": {}, \"eval-pi05-adaptive-spatial-s42\": {}, \"eval-pi05-vla-only-goal-s43\": {}, \"eval-pi05-vla-only-spatial-s43\": {}, \"eval-pi05-vla-only-object-s42\": {}, \"eval-supp-long-vla-only-s42\": {}, \"eval-supp-long-adapt-tau025-s42\": {}, \"eval-k2-tau010-spatial-s42-r2\": {}, \"eval-pi05-vla-only-spatial-s45\": {}, \"eval-pi05-vla-only-object-s44\": {}, \"eval-k2-tau015-spatial-s42\": {}, \"eval-pi05-vla-only-goal-s42\": {}, \"eval-pi05-vla-only-spatial-s42\": {}, \"eval-supp-crm-norm005-goal-s48\": {}, \"eval-supp-crm-norm005-spatial-s49\": {}, \"eval-supp-crm-norm005-spatial-s48\": {}, \"eval-supp-long-vla-only-s43-r2\": {}, \"eval-supp-goal-vla-only-s42-bjb1\": {}, \"crm-norm005-goal-s49\": {}, \"eval-supp-obj-vla-only-s44\": {}, \"crm-norm005-object-s48\": {}, \"eval-supp-obj-vla-only-s43\": {}, \"eval-supp-obj-vla-only-s42\": {}, \"eval-supp-long-vla-only-s48\": {}, \"eval-supp-goal-vla-only-s50\": {}, \"eval-supp-goal-vla-only-s44\": {}, \"eval-supp-spatial-vla-only-smolvla-s42\": {}, \"eval-supp-goal-vla-only-s43\": {}, \"eval-supp-goal-vla-only-s42\": {}, \"train-crm-pi05-unified-3suite-r2\": {}, \"eval-supp-vla-only-spatial-s49\": {}, \"eval-supp-vla-only-spatial-s48\": {}, \"eval-supp-vla-only-obj-s49\": {}, \"eval-supp-vla-only-obj-s48\": {}, \"eval-supp-vla-only-goal-s49\": {}, \"eval-supp-vla-only-goal-s48\": {}, \"eval-k5-spatial-s42-sweep\": {}, \"eval-supp-long-vla-only-s43\": {}, \"eval-supp-goal-vla-only-s45\": {}, \"eval-supp-long-vla-only-s45\": {}, \"eval-supp-long-vla-only-s44\": {}, \"eval-supp-spatial-vla-only-s42\": {}, \"eval-pi05-vla-only-object-seed43-r4\": {}, \"eval-supp-obj-vla-only-s50\": {}, \"eval-supp-long-adapt-tau025-s47-r2\": {}, \"eval-supp-long-k2mean-s47-r2\": {}, \"eval-supp-spatial-reconvla-s47\": {}, \"eval-a1-baseline-object-s42\": {}, \"eval-supp-long-vla-only-s47-r4\": {}, \"eval-supp-obj-k2mean-s47-r2\": {}, \"eval-supp-obj-adapt-tau025-s47-r2\": {}, \"eval-supp-obj-crm-norm005-s47-r2\": {}, \"eval-supp-obj-vla-only-s47-r2\": {}, \"eval-supp-k2mean-spatial-s47\": {}, \"eval-supp-spatial-vla-only-s47\": {}, \"eval-supp-spatial-adapt-tau025-s47\": {}, \"eval-supp-adapt-tau025-spatial-s47\": {}, \"eval-supp-spatial-k2mean-s47\": {}, \"eval-supp-reconvla-spatial-s47\": {}, \"eval-supp-vla-only-spatial-s47\": {}, \"eval-supp-long-reconvla-s47\": {}, \"eval-supp-long-crm-norm005-s47\": {}, \"eval-supp-obj-k2mean-s47\": {}, \"eval-supp-obj-crm-norm005-s47\": {}, \"eval-supp-obj-adapt-tau025-s47\": {}, \"eval-supp-obj-vla-only-s47\": {}, \"eval-supp-goal-vla-only-s47-r3\": {}, \"eval-supp-long-k2mean-s47\": {}, \"eval-supp-long-adapt-tau025-s47\": {}, \"eval-supp-spatial-crm-norm005-s47\": {}, \"eval-supp-long-crm-norm005-s46\": {}, \"train-crm-pi05-unified-3suite\": {}, \"eval-openvla-object-vla-only-seed42-v3\": {}, \"eval-supp-vla-only-spatial-s46\": {}, \"eval-supp-adapt-tau025-spatial-s45\": {}, \"eval-supp-crm-norm005-spatial-s45\": {}, \"eval-supp-vla-only-spatial-s45\": {}, \"eval-supp-crm-norm005-spatial-s46\": {}, \"train-crm-pi05-spatial-k1\": {}, \"train-crm-pi05-goal-k1\": {}, \"eval-supp-goal-vla-only-s47-r2\": {}, \"eval-supp-long-vla-only-s47-r3\": {}, \"eval-supp-long-vla-only-s47-r2\": {}, \"eval-supp-goal-vla-only-s47\": {}, \"eval-supp-long-reconvla-s46\": {}, \"eval-supp-long-k2mean-s46\": {}, \"eval-supp-adapt-tau025-spatial-s46\": {}, \"eval-supp-long-adapt-tau025-s46\": {}, \"crm-train-openvla-k1-multiscale-object\": {}, \"eval-supp-long-k2mean-s46-r2\": {}, \"eval-supp-long-reconvla-s46-r2\": {}, \"eval-supp-long-crm-norm005-s46-r2\": {}, \"eval-supp-long-adapt-tau025-s46-r2\": {}, \"eval-supp-obj-crm-norm005-s45\": {}, \"eval-supp-obj-adapt-tau025-s45\": {}, \"eval-supp-obj-vla-only-s45\": {}, \"eval-supp-spatial-crm-norm005-s45\": {}, \"eval-supp-spatial-vla-only-s45\": {}, \"precompute-pi05-goal-2048-r2\": {}, \"eval-supp-long-vla-only-s46\": {}, \"precompute-pi05-spatial-2048-r2\": {}, \"precompute-smolvla-goal-bjb1-32546\": {}, \"eval-supp-goal-vla-only-s46\": {}, \"eval-supp-goal-reconvla-s46\": {}, \"crm-train-pi05-spatial-full\": {}, \"eval-obs-only-spatial-v2\": {}, \"eval-perdof-object-norm003-seed44\": {}, \"eval-random-selection-spatial-seed42\": {}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {}, \"eval-supp-goal-vla-only-wrapper-s44\": {}, \"eval-supp-long-reconvla-s45\": {}, \"eval-pi05-vla-only-long-seed42-r4\": {}, \"eval-pi05-vla-only-object-seed42\": {}, \"eval-pi05-vla-only-object-seed43\": {}, \"eval-pi05-vla-only-object-seed44\": {}, \"eval-supp-long-k2mean-s45\": {}, \"eval-supp-goal-k2mean-s46\": {}, \"eval-supp-goal-adapt-tau025-s46\": {}, \"eval-supp-goal-crm-norm005-s46\": {}, \"eval-supp-spatial-k2mean-s45\": {}, \"eval-supp-spatial-vla-only-s46\": {}, \"eval-supp-spatial-adapt-tau025-s46\": {}, \"eval-supp-spatial-crm-norm005-s46\": {}, \"eval-supp-long-crm-norm005-s45\": {}, \"eval-supp-long-adapt-tau025-s45\": {}, \"eval-supp-spatial-reconvla-s45\": {}, \"eval-supp-goal-k2mean-s45\": {}, \"eval-supp-adapt-tau025-obj-s45\": {}, \"eval-supp-obj-k2mean-s45\": {}, \"eval-supp-crm-obj-s46\": {}, \"eval-supp-long-k2mean-s44\": {}, \"eval-supp-long-reconvla-s44\": {}, \"eval-supp-goal-reconvla-s45\": {}, \"eval-supp-crm-norm005-obj-s46\": {}, \"eval-supp-goal-crm-norm005-s45\": {}, \"eval-supp-crm-norm005-obj-s45\": {}, \"eval-supp-reconvla-obj-s46\": {}, \"eval-supp-goal-adapt-tau025-s45\": {}, \"eval-supp-long-crm-norm005-s44\": {}, \"eval-supp-long-adapt-tau025-s44\": {}, \"eval-supp-k2mean-obj-s46\": {}, \"eval-supp-k2mean-obj-s45\": {}, \"eval-supp-adapt-tau025-obj-s46\": {}, \"eval-supp-long-k2mean-s42\": {}, \"eval-supp-obj-vla-only-s46\": {}, \"eval-supp-long-k2mean-s43\": {}, \"eval-supp-long-reconvla-s43\": {}, \"eval-supp-long-crm-norm005-s43\": {}, \"eval-supp-long-adapt-tau025-s43\": {}, \"eval-supp-obj-adapt-tau025-s45-r2\": {}, \"eval-supp-long-crm-norm005-s42\": {}, \"eval-supp-long-reconvla-s42\": {}, \"eval-ablation-tau040-goal-s42\": {}, \"eval-ablation-tau015-goal-s42\": {}, \"eval-supp-k2mean-object-s44\": {}, \"eval-ablation-tau010-goal-s42\": {}, \"eval-supp-obj-reconvla-s44\": {}, \"eval-supp-spatial-vla-only-s44\": {}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {}, \"eval-supp-k2mean-spatial-s44\": {}, \"eval-supp-spatial-vla-only-s43\": {}, \"eval-supp-k2mean-goal-s44\": {}, \"eval-supp-adapt-tau025-obj-s44\": {}, \"eval-supp-goal-reconvla-s44\": {}, \"eval-supp-obj-reconvla-s43\": {}, \"eval-supp-crm-norm005-goal-s44\": {}, \"eval-supp-k2mean-object-s43\": {}, \"eval-supp-k2mean-goal-s42-r2\": {}, \"eval-supp-adapt-tau025-goal-s44\": {}, \"eval-supp-crm-norm005-obj-s43\": {}, \"eval-supp-adapt-tau025-goal-s43\": {}, \"eval-supp-crm-norm005-goal-s43\": {}, \"eval-supp-adapt-tau025-obj-s43\": {}, \"eval-supp-goal-reconvla-s43\": {}, \"eval-supp-k2mean-spatial-s43\": {}, \"eval-supp-reconvla-spatial-s44\": {}, \"eval-supp-reconvla-spatial-s43\": {}, \"eval-supp-k2mean-goal-s43\": {}, \"eval-supp-k2mean-object-s42\": {}, \"eval-supp-goal-adapt-tau025-s42\": {}, \"eval-supp-goal-crm005-s42\": {}, \"eval-supp-goal-reconvla-s42\": {}, \"train-crm-unified-4suite-r6\": {}, \"eval-goal-vla-only-wrapper-s42\": {}, \"eval-supp-obj-adapt-tau025-s42\": {}, \"eval-supp-k2mean-spatial-s42\": {}, \"eval-supp-crm-norm005-spatial-s44\": {}, \"eval-supp-adapt-tau025-spatial-s44\": {}, \"eval-supp-reconvla-k2-spatial-s42\": {}, \"eval-supp-adapt-tau025-spatial-s43\": {}, \"eval-supp-crm-norm005-spatial-s43\": {}, \"eval-supp-k2mean-goal-s42\": {}, \"eval-supp-obj-adapt-s42-r2\": {}, \"eval-object-vla-only-wrapper-s44-r2\": {}, \"eval-object-vla-only-wrapper-s43-r2\": {}, \"eval-object-vla-only-wrapper-s42-r2\": {}, \"eval-supp-obj-reconvla-s42\": {}, \"eval-supp-obj-crm005-s42-r2\": {}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {}, \"eval-supp-crm-norm02-spatial-s42-r2\": {}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {}, \"eval-openvla-object-baseline-seed42-r2\": {}, \"eval-obs-only-object-norm02-seed55\": {}, \"precompute-pi05-features-object\": {}, \"precompute-smolvla-goal-shard2\": {}, \"precompute-smolvla-goal-shard1\": {}, \"precompute-smolvla-goal-shard0\": {}, \"eval-smolvla-long-seed2\": {}, \"eval-smolvla-long-seed1\": {}, \"eval-smolvla-long-seed0\": {}, \"eval-smolvla-crm-spatial-seed42-v1\": {}, \"eval-smolvla-crm-spatial-seed43-v1\": {}, \"eval-smolvla-crm-spatial-seed44-v1\": {}, \"eval-smolvla-crm-goal-seed42-v1\": {}, \"eval-smolvla-crm-goal-seed43-v1\": {}, \"eval-smolvla-crm-goal-seed44-v1\": {}, \"eval-supp-obj-adapt-s42\": {}, \"eval-crm-norm02-spatial-s42\": {}, \"eval-adaptive-tau015-spatial-s42\": {}, \"eval-adaptive-tau025-spatial-s42\": {}, \"eval-adaptive-tau035-spatial-s42\": {}, \"train-crm-unified-4suite-r5-resumed\": {}, \"eval-object-vla-only-wrapper-s44\": {}, \"eval-object-vla-only-wrapper-s43\": {}, \"eval-object-vla-only-wrapper-s42\": {}, \"eval-supp-obj-crm005-s42\": {}, \"eval-supp-adapt-tau035-spatial-s42\": {}, \"eval-supp-adapt-tau025-spatial-s42\": {}, \"eval-supp-adapt-tau015-spatial-s42\": {}, \"eval-supp-crm-norm02-spatial-s42\": {}, \"eval-3dir-adaptive-spatial-s42\": {}, \"eval-3dir-norm03-spatial-s42\": {}, \"eval-3dir-reconvla-spatial-s42\": {}, \"eval-3dir-norm01-spatial-s42\": {}, \"eval-3dir-norm005-spatial-s42\": {}, \"precompute-pi05-goal-2048\": {}, \"precompute-pi05-spatial-2048\": {}, \"precompute-pi05-object-2048\": {}, \"eval-smolvla-crm-object-seed43-v1\": {}, \"eval-smolvla-crm-object-seed42-v1\": {}, \"eval-smolvla-crm-object-seed44-v1\": {}, \"train-crm-unified-4suite-r5\": {}, \"eval-smolvla-crm-goal-seed43\": {}, \"eval-smolvla-crm-goal-seed42\": {}, \"eval-smolvla-crm-spatial-seed44\": {}, \"eval-smolvla-crm-spatial-seed43\": {}, \"eval-smolvla-crm-spatial-seed42\": {}, \"precompute-pi05-long-2048\": {}, \"eval-smolvla-lerobot-goal-seed44-v3\": {}, \"train-crm-smolvla-3suite-v1\": {}, \"eval-smolvla-lerobot-goal-seed43-v2\": {}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {}, \"eval-smolvla-lerobot-object-seed44-v2\": {}, \"eval-smolvla-lerobot-object-seed43-v2\": {}, \"eval-smolvla-lerobot-goal-seed43\": {}, \"eval-smolvla-lerobot-spatial-seed43\": {}, \"eval-smolvla-lerobot-object-seed44\": {}, \"eval-smolvla-lerobot-object-seed43\": {}, \"eval-smolvla-lerobot-spatial-seed44\": {}, \"precompute-smolvla-long-wrapper-bjb1\": {}, \"eval-smolvla-lerobot-long-seed44\": {}, \"eval-smolvla-lerobot-long-seed43\": {}, \"eval-smolvla-lerobot-long-seed42\": {}, \"train-crm-unified-4suite-r4\": {}, \"eval-pi05-vla-only-long-seed42-r4-rerun\": {}, \"eval-pi05-crm-object-seed44\": {}, \"eval-pi05-crm-object-seed43\": {}, \"eval-pi05-crm-object-seed42\": {}, \"eval-pi05-vla-only-long-seed43-r4-std\": {}, \"eval-pi05-vla-only-goal-seed44-r4-std\": {}, \"eval-pi05-vla-only-goal-seed42-r4-std\": {}, \"eval-pi05-vla-only-long-seed44-r4-std\": {}, \"eval-pi05-vla-only-goal-seed43-r4-std\": {}, \"eval-pi05-vla-only-goal-seed42-r4\": {}, \"precompute-smolvla-long-k2\": {}, \"train-crm-unified-4suite-r3\": {}, \"train-crm-unified-4suite-r2\": {}, \"precompute-smolvla-goal-bjb2-28827\": {}, \"precompute-smolvla-long-bjb2-28827\": {}, \"eval-pi05-vla-only-spatial-seed44-r4\": {}, \"eval-pi05-vla-only-spatial-seed43-r4\": {}, \"eval-pi05-vla-only-spatial-seed42-r4\": {}, \"eval-pi05-vla-only-long-seed44-r4\": {}, \"eval-pi05-vla-only-long-seed43-r4\": {}, \"eval-pi05-vla-only-goal-seed44-r4\": {}, \"eval-pi05-vla-only-goal-seed43-r4\": {}, \"eval-openvla-oft-official-object\": {}, \"eval-pi05-crm-spatial-seed44\": {}, \"eval-pi05-crm-spatial-seed43\": {}, \"eval-pi05-crm-spatial-seed42\": {}, \"eval-pi05-vla-only-object-seed44-r4\": {}, \"eval-smolvla-lerobot-official-object\": {}, \"eval-pi05-vla-only-object-seed42-r4\": {}, \"train-crm-unified-4suite\": {}, \"precompute-smolvla-long-bjb1-32546-r2\": {}, \"precompute-smolvla-long-bjb1-32546\": {}, \"eval-loss-perdof-object-seed42\": {}, \"eval-loss-combined-object-seed42\": {}, \"eval-loss-conformal-object-seed42\": {}, \"eval-loss-mse-object-seed42\": {}, \"eval-openvla-oft-object-baseline-seed42\": {}, \"precompute-smolvla-long-bjb1-18228\": {}, \"crm-loss-combined\": {}, \"crm-loss-conformal\": {}, \"precompute-smolvla-goal-bjb1-18228\": {}, \"crm-loss-perdof\": {}, \"crm-loss-mse-baseline\": {}, \"eval-smolvla-acr-goal-seed43\": {}, \"eval-smolvla-crm-long-seed44-v2\": {}, \"eval-smolvla-crm-goal-seed44-v2\": {}, \"eval-smolvla-crm-long-seed43-v2\": {}, \"eval-smolvla-acr-long-seed42\": {}, \"eval-smolvla-acr-goal-seed42\": {}, \"crm-train-pi05-spatial-v2\": {}, \"crm-train-pi05-object-full\": {}, \"crm-train-pi05-spatial\": {}, \"crm-train-pi05-object\": {}, \"eval-pi05-vla-only-spatial-seed45\": {}, \"eval-pi05-vla-only-spatial-seed43-r3\": {}, \"eval-pi05-vla-only-spatial-seed42-r3\": {}, \"eval-pi05-vla-only-object-seed44-r3\": {}, \"eval-pi05-vla-only-object-seed43-r3\": {}, \"eval-pi05-vla-only-object-seed42-r3\": {}, \"eval-spatial-obs-only-seed45\": {}, \"eval-pi05-vla-only-spatial-seed44\": {}, \"eval-pi05-vla-only-spatial-seed43\": {}, \"eval-pi05-vla-only-spatial-seed42\": {}, \"eval-k20-obs-only-spatial-seed44\": {}, \"eval-k20-obs-only-spatial-seed43\": {}, \"eval-k20-obs-only-spatial-seed42\": {}, \"eval-k20-obs-only-object-seed45\": {}, \"eval-obs-only-object-norm003-seed66\": {}, \"eval-obs-only-object-norm01-seed66\": {}, \"eval-obs-only-object-norm005-seed66\": {}, \"eval-obs-only-object-norm003-seed67\": {}, \"eval-k20-obs-only-object-seed44\": {}, \"eval-k20-obs-only-object-seed43\": {}, \"eval-k20-obs-only-object-seed42\": {}, \"eval-crm-object-k20-seed44\": {}, \"eval-crm-object-k20-seed42\": {}, \"eval-obs-only-object-norm02-seed53\": {}, \"eval-obs-only-object-norm02-seed52\": {}, \"eval-obs-only-object-norm02-seed51\": {}, \"eval-obs-only-object-norm02-seed50\": {}, \"eval-obs-only-object-norm02-seed48-r2\": {}, \"eval-obs-only-object-norm02-seed47\": {}, \"eval-obs-only-object-norm02-seed46\": {}, \"eval-obs-only-object-norm02-seed45\": {}, \"eval-obs-only-object-norm02-seed44-r2\": {}, \"eval-obs-only-object-norm02-seed43-r3\": {}, \"eval-obs-only-object-norm02-seed43-r2\": {}, \"eval-obs-only-object-norm005-seed67\": {}, \"eval-obs-only-object-norm01-seed67\": {}, \"eval-vla-only-object-seed50\": {}, \"eval-vla-only-object-seed49\": {}, \"eval-vla-only-object-seed48\": {}, \"eval-vla-only-object-seed46\": {}, \"eval-vla-only-object-seed45\": {}, \"eval-vla-only-object-seed44-r2\": {}, \"eval-plan-a-object-seed42\": {}, \"eval-vla-only-object-seed43\": {}, \"eval-vla-only-object\": {}, \"eval-plan-a-spatial-seed43\": {}, \"eval-plan-a-object-seed44\": {}, \"eval-plan-a-spatial-seed42\": {}, \"eval-plan-a-spatial-seed44\": {}, \"eval-plan-a-object-seed43\": {}, \"eval-random-selection-object-seed44\": {}, \"eval-random-selection-object-seed43\": {}, \"eval-obs-only-object-norm01-seed60\": {}, \"eval-pi05-baseline-object-seed42\": {}, \"eval-obs-only-object-norm01-seed54\": {}, \"eval-obs-only-object-norm01-seed53\": {}, \"eval-obs-only-object-norm01-seed52\": {}, \"eval-obs-only-object-norm01-seed50\": {}, \"eval-obs-only-object-norm01-seed49\": {}, \"eval-obs-only-object-norm01-seed48\": {}, \"eval-obs-only-object-norm01-seed47\": {}, \"eval-obs-only-object-norm01-seed45-r2\": {}, \"eval-obs-only-object-norm01-seed44\": {}, \"eval-obs-only-object-norm005-seed55\": {}, \"eval-obs-only-object-norm005-seed50\": {}, \"eval-obs-only-object-norm005-seed49\": {}, \"eval-obs-only-object-norm005-seed48\": {}, \"eval-obs-only-object-norm005-seed47\": {}, \"eval-obs-only-object-norm005-seed44\": {}, \"eval-obs-only-object-norm005-seed43-r2\": {}, \"eval-obs-only-object-norm005-seed43\": {}, \"eval-obs-only-object-norm003-seed48\": {}, \"eval-obs-only-object-norm003-seed47-r2\": {}, \"eval-obs-only-object-norm003-seed46\": {}, \"eval-obs-only-object-norm003-seed45\": {}, \"eval-obs-only-object-norm003-seed44-bjb2\": {}, \"eval-obs-only-object-norm003-seed44\": {}, \"eval-obs-only-object-norm003-seed43-r2\": {}, \"eval-obs-only-object-norm003-seed43\": {}, \"eval-obs-only-object-norm01-seed57\": {}, \"eval-obs-only-object-norm005-seed65\": {}, \"eval-obs-only-object-norm005-seed61\": {}, \"eval-obs-only-object-norm005-seed58\": {}, \"eval-obs-only-object-norm003-seed59\": {}, \"eval-obs-only-object-norm003-seed56\": {}, \"eval-obs-only-object-norm005-seed75\": {}, \"eval-obs-only-object-norm01-seed74\": {}, \"eval-obs-only-object-norm005-seed72\": {}, \"eval-obs-only-object-norm003-seed63-r2\": {}, \"eval-obs-only-object-norm01-seed71\": {}, \"eval-obs-only-object-norm003-seed62-r2\": {}, \"eval-obs-only-object-norm003-seed73\": {}, \"eval-obs-only-object-norm01-seed51-r3\": {}, \"eval-obs-only-object-norm01-seed52-r3\": {}, \"eval-obs-only-object-norm01-seed65\": {}, \"eval-obs-only-object-norm01-seed64\": {}, \"eval-obs-only-object-norm005-seed64\": {}, \"eval-obs-only-object-norm003-seed65\": {}, \"eval-obs-only-object-norm003-seed64\": {}, \"eval-obs-only-object-norm005-seed62\": {}, \"eval-obs-only-object-norm005-seed63\": {}, \"eval-obs-only-object-norm01-seed61\": {}, \"eval-obs-only-object-norm003-seed64-bjb2\": {}, \"eval-obs-only-object-norm003-seed63\": {}, \"eval-obs-only-object-norm003-seed62\": {}, \"eval-obs-only-object-norm01-seed51-r2\": {}, \"eval-obs-only-object-norm01-seed52-r2\": {}, \"eval-obs-only-object-norm01-seed51\": {}, \"eval-obs-only-object-norm005-seed49-r2\": {}, \"eval-obs-only-object-norm005-seed55-r2\": {}, \"eval-openvla-crm-object-seed42\": {}, \"eval-obs-only-object-norm003-seed44-r2\": {}, \"eval-random-selection-object-seed49\": {}, \"eval-random-selection-object-seed48\": {}, \"eval-k5-obs-only-object-seed44\": {}, \"eval-obs-only-spatial-norm02-seed52\": {}, \"eval-obs-only-object-norm02-seed54\": {}, \"D088-eval-adaptive-unc-head-object-seed44\": {}, \"D088-eval-adaptive-unc-head-object-seed43\": {}, \"D088-eval-adaptive-unc-head-object-seed42\": {}, \"eval-adaptive-unc-head-object-seed42\": {}, \"eval-adaptive-unc-head-object-seed43\": {}, \"eval-perdof-object-norm02-seed50\": {}, \"eval-adaptive-unc-head-object-seed44\": {}, \"eval-random-selection-spatial-seed42-r3\": {}, \"eval-obs-only-spatial-norm02-seed50\": {}, \"train-crm-openvla-obs-only\": {}, \"openvla-precompute-k1\": {}, \"eval-random-selection-object-seed46-r3\": {}, \"eval-perdof-object-norm02-seed49\": {}, \"eval-random-selection-object-seed47\": {}, \"eval-obs-only-spatial-norm02-seed42-r2\": {}, \"eval-k5-obs-only-object-seed43\": {}, \"eval-random-selection-spatial-seed43-r2\": {}, \"eval-random-selection-spatial-seed44\": {}, \"eval-crm-k1-object-seed43-plan702\": {}, \"eval-crm-k1-object-seed42-plan702\": {}, \"eval-crm-k1-object-seed44-plan702\": {}, \"eval-random-selection-object-seed46-r2\": {}, \"eval-random-selection-spatial-seed43\": {}, \"eval-random-selection-object-seed46\": {}, \"eval-obs-only-spatial-seed48\": {}, \"eval-vla-only-spatial-seed48\": {}, \"eval-obs-only-spatial-norm02-seed42\": {}, \"eval-obs-only-spatial-norm02-seed49\": {}, \"eval-adaptive-k-spatial-p90-seed44\": {}, \"eval-argmin-object-seed50\": {}, \"eval-vla-only-object-seed48-r2\": {}, \"eval-vla-only-goal-seed51\": {}, \"eval-random-selection-spatial-seed42-r2\": {}, \"eval-random-selection-object-seed45\": {}, \"eval-crm-k1-object-seed44-plan702-r2\": {}, \"eval-crm-k1-object-seed43-plan702-r2\": {}, \"eval-crm-k1-object-seed42-plan702-r2\": {}, \"eval-perdof-object-norm02-seed48\": {}, \"eval-argmin-object-k5-seed44-r2\": {}, \"eval-vla-only-goal-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-seed46-r2\": {}, \"eval-latency-profiling-v1\": {}, \"eval-adaptive-k-spatial-p75-seed44\": {}, \"eval-obs-only-goal-norm02-seed51\": {}, \"eval-adaptive-k-spatial-p25-seed44\": {}, \"eval-openvla-object-baseline-seed42\": {}, \"eval-argmin-object-seed49\": {}, \"eval-argmin-object-seed48\": {}, \"eval-obs-only-spatial-norm02-seed48\": {}, \"eval-obs-only-goal-norm02-seed52\": {}, \"eval-adaptive-k-spatial-p90-seed43\": {}, \"eval-perdof-object-norm02-seed45-r3\": {}, \"eval-adaptive-k-spatial-p90-seed42\": {}, \"eval-obs-only-object-norm02-seed49\": {}, \"eval-vla-only-goal-seed47\": {}, \"eval-adaptive-k-spatial-p50-seed44\": {}, \"eval-adaptive-k-spatial-p50-seed43\": {}, \"eval-adaptive-k-spatial-p50-seed42\": {}, \"eval-adaptive-k-spatial-p25-seed42\": {}, \"eval-adaptive-k-spatial-p25-seed43\": {}, \"eval-adaptive-k-spatial-p75-seed43\": {}, \"eval-crm-object-k20-seed43\": {}, \"eval-vla-only-long-seed49-r2\": {}, \"eval-adaptive-k-spatial-p75-seed42\": {}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {}, \"eval-adaptive-k-p75-seed42\": {}, \"eval-adaptive-k-p75-seed43\": {}, \"eval-adaptive-k-p50-seed42\": {}, \"eval-adaptive-k-p50-seed43\": {}, \"eval-random-selection-object-seed42\": {}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {}, \"eval-obs-only-object-norm02-seed42\": {}, \"latency-profile-n1000\": {}, \"eval-adaptive-k-p90-seed44\": {}, \"eval-adaptive-k-p25-seed43\": {}, \"eval-crm-spatial-k10-seed51\": {}, \"eval-vla-only-goal-seed49\": {}, \"eval-vla-only-long-seed52\": {}, \"eval-vla-only-long-seed51\": {}, \"eval-vla-only-long-seed50\": {}, \"eval-crm-long-seed50\": {}, \"eval-adaptive-k-p25-seed44-r2\": {}, \"calibrate-crm-correction-signal\": {}, \"eval-adaptive-k-p25-seed42\": {}, \"eval-vla-only-goal-seed48-r2\": {}, \"eval-vla-only-goal-seed47-r2\": {}, \"eval-crm-goal-seed46\": {}, \"eval-adaptive-k-p50-seed44\": {}, \"eval-adaptive-k-p75-seed44\": {}, \"eval-adaptive-k-p90-seed43\": {}, \"eval-adaptive-k-p90-seed42\": {}, \"eval-vla-only-spatial-seed47\": {}, \"eval-crm-long-seed47\": {}, \"eval-vla-only-long-seed48\": {}, \"eval-crm-long-seed46\": {}, \"eval-crm-goal-seed45-r2\": {}, \"eval-crm-goal-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-seed43-r2\": {}, \"k2-l2-calibration-phase1\": {}, \"eval-crm-long-seed45\": {}, \"eval-vla-only-spatial-seed49\": {}, \"eval-vla-only-goal-seed48\": {}, \"eval-vla-only-goal-seed43\": {}, \"eval-vla-only-goal-seed42\": {}, \"eval-vla-only-object-seed47\": {}, \"eval-crm-long-seed44\": {}, \"eval-crm-long-seed43\": {}, \"eval-crm-long-seed42\": {}, \"eval-crm-goal-seed42\": {}, \"eval-crm-goal-seed43\": {}, \"eval-vla-only-spatial-seed46\": {}, \"eval-vla-only-long-seed47\": {}, \"eval-crm-goal-seed45\": {}, \"eval-crm-goal-seed44\": {}, \"eval-vla-only-goal-seed45\": {}, \"eval-vla-only-goal-seed46\": {}, \"eval-vla-only-long-seed46\": {}, \"fmvd-calibration-phase1\": {}, \"eval-vla-only-long-seed45\": {}, \"eval-perdof-object-norm003-seed47\": {}, \"eval-perdof-object-norm005-seed47\": {}, \"eval-vla-only-long-seed44\": {}, \"eval-vla-only-long-seed42\": {}, \"eval-vla-only-long-seed43\": {}, \"eval-obs-only-spatial-norm02-seed43\": {}, \"eval-obs-only-spatial-norm02-seed47\": {}, \"eval-obs-only-spatial-norm02-seed46\": {}, \"eval-argmin-object-k5-seed44\": {}, \"eval-vla-only-goal-seed44\": {}, \"eval-random-selection-object-k5-seed45-r2\": {}, \"eval-random-selection-object-k5-seed44-r2\": {}, \"eval-random-selection-object-k5-seed43-r2\": {}, \"eval-random-selection-object-k5-seed42-r2\": {}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {}, \"plan_602-latency-profiling\": {}, \"eval-vla-only-spatial-seed45\": {}, \"eval-perdof-object-norm005-seed45-r2\": {}, \"eval-vla-only-spatial-seed44\": {}, \"eval-obs-only-object-default-seed48-r2\": {}, \"eval-vla-only-spatial-seed43\": {}, \"eval-vla-only-spatial-seed42\": {}, \"eval-obs-only-spatial-norm02-k5-seed45\": {}, \"eval-obs-only-spatial-norm02-k5-seed44\": {}, \"eval-random-selection-object-k5-seed45\": {}, \"eval-random-selection-object-k5-seed44\": {}, \"eval-random-selection-object-k5-seed43\": {}, \"eval-random-selection-object-k5-seed42\": {}, \"eval-obs-only-spatial-norm02-seed44\": {}, \"eval-perdof-object-norm01-seed43\": {}, \"eval-obs-only-object-default-seed45-r2\": {}, \"eval-argmin-object-k5-seed42\": {}, \"eval-argmin-object-k5-seed45\": {}, \"eval-argmin-object-k5-seed43\": {}, \"eval-perdof-object-norm03-seed43\": {}, \"eval-obs-only-spatial-norm02-seed45\": {}, \"train-crm-k1-accg-object-seed42-full\": {}, \"plan_701-precompute-k1-spatial\": {}, \"plan_701-crm-k1-train\": {}, \"eval_obs_only_norm03_seed48\": {}, \"eval_obs_only_norm01_seed48\": {}, \"eval-lto-splitA-vla-only-r3\": {}, \"eval-lto-splitA-vla-only-r2\": {}, \"eval-lto-splitA-heldout-r2\": {}, \"crm-lto-splitA-train\": {}, \"eval-perdof-object-norm003-seed48\": {}, \"eval-scalar-object-seed45-r2\": {}, \"eval-obs-only-spatial-norm02-k5-seed43\": {}, \"eval-obs-only-object-norm02-k5-seed48\": {}, \"eval-obs-only-spatial-norm02-k5-seed42\": {}, \"eval-obs-only-object-norm02-k5-seed46\": {}, \"eval-lto-splitA-vla-only-v2\": {}, \"eval-lto-splitA-heldout-v2\": {}, \"eval-perdof-object-default-seed47\": {}, \"eval-perdof-object-norm03-seed47\": {}, \"eval-obs-only-object-default-seed48\": {}, \"eval-perdof-object-norm003-seed46\": {}, \"eval-perdof-object-norm005-seed46\": {}, \"eval-perdof-object-norm003-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed47\": {}, \"eval-perdof-object-norm01-seed48\": {}, \"eval-obs-only-object-default-seed47\": {}, \"eval-perdof-object-norm03-seed46\": {}, \"eval-obs-only-object-norm03-seed46\": {}, \"eval-scalar-object-seed46\": {}, \"eval-obs-only-object-norm003-seed45-r2\": {}, \"eval-lto-splitA-vla-only\": {}, \"eval-lto-splitA-heldout\": {}, \"eval-obs-only-object-norm005-seed46\": {}, \"eval-perdof-object-norm03-seed48\": {}, \"eval-obs-only-object-norm003-seed49\": {}, \"crm-lto-splitA-train-fixed\": {}, \"eval-obs-only-object-norm003-seed47\": {}, \"eval-perdof-object-norm003-seed43\": {}, \"eval-perdof-object-norm005-seed43\": {}, \"eval-perdof-object-default-seed43\": {}, \"eval-perdof-object-default-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed45\": {}, \"eval-perdof-object-norm005-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed44\": {}, \"eval-perdof-object-norm003-seed44-r2\": {}, \"eval-obs-only-object-norm01-seed46-r3\": {}, \"eval-perdof-object-norm005-seed44\": {}, \"eval-vla-only-object-seed45-r2\": {}, \"eval-obs-only-object-norm03-seed48\": {}, \"eval-obs-only-object-norm02-k5-seed43\": {}, \"eval-perdof-object-norm01-seed42-r2\": {}, \"eval-obs-only-object-norm01-seed42-r2\": {}, \"eval-perdof-object-norm02-seed43\": {}, \"eval-perdof-object-norm01-seed46\": {}, \"eval-obs-only-object-norm01-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed42\": {}, \"eval-perdof-object-default-seed46\": {}, \"eval-perdof-object-default-seed44\": {}, \"eval-mag-perdof-norm02\": {}, \"eval-acr-spatial-v4-scalar\": {}, \"eval-acr-spatial-v4-small\": {}, \"eval-acr-spatial-v4-obs-only-r2\": {}, \"eval-argmin-only-spatial\": {}, \"eval-acr-spatial-v3\": {}, \"eval-acr-object-v3\": {}, \"eval-openvla-object-vla-only-seed42\": {}, \"eval-perdof-object-norm02-seed47\": {}, \"eval-obs-only-object-norm02-seed48\": {}, \"eval-obs-only-object-default-seed46\": {}, \"eval-perdof-object-norm02-seed46\": {}, \"eval-obs-only-object-norm01-seed46\": {}, \"mag_obs_only_norm01_seed47\": {}, \"mag_obs_only_norm01_seed46\": {}, \"eval-perdof-object-norm02-seed43-r3\": {}, \"mag_perdof_norm02_seed43_r3\": {}, \"eval-perdof-object-norm01-seed47-bjb1\": {}, \"eval-openvla-object-vla-only-seed42-v2\": {}, \"eval-k1-crm-multiscale-object-seed44-r2\": {}, \"eval-k1-crm-multiscale-object-seed44\": {}, \"eval-k1-crm-multiscale-object-seed43\": {}, \"eval-k1-crm-multiscale-object-seed42\": {}, \"eval-perdof-object-norm01-seed46-r2\": {}, \"eval-k1-crm-multiscale-object-seed43-r2\": {}, \"eval-perdof-object-norm02-seed45-r2\": {}, \"eval-obs-only-object-norm005-seed43-r3\": {}, \"plan_602-latency-profile\": {}, \"train-crm-k1-accg-object-seed42-v2\": {}, \"eval-k1-crm-accg-object-seed44\": {}, \"eval-k1-crm-accg-object-seed43\": {}, \"eval-k1-crm-accg-object-seed42\": {}, \"eval-obs-only-object-default-seed45\": {}, \"eval-scalar-object-seed45\": {}, \"eval-perdof-object-norm02-seed45\": {}, \"eval-perdof-object-norm02-seed44\": {}, \"train-crm-k1-accg-object-seed42-fallback\": {}, \"train-crm-k1-accg-object-seed42\": {}, \"eval-perdof-object-norm02-seed45-deploy\": {}, \"eval-obs-only-object-norm01-seed47-r2\": {}, \"eval-perdof-object-norm03-seed45-r2\": {}, \"eval-perdof-object-norm03-seed44-r2\": {}, \"eval-obs-only-object-norm03-seed47\": {}, \"eval-perdof-object-norm03-seed46-r2\": {}, \"eval-perdof-object-norm01-seed44\": {}, \"eval-obs-only-object-norm01-seed47-bjb2\": {}, \"eval-obs-only-object-norm01-seed46-bjb2\": {}, \"eval-argmin-object-seed47\": {}, \"eval-perdof-object-norm01-seed45\": {}, \"eval-perdof-object-norm01-seed47\": {}, \"eval-argmin-object-seed46\": {}, \"eval-obs-only-object-norm03-seed45-r2\": {}, \"eval-vla-mean-object-seed45\": {}, \"eval-argmin-object-seed45\": {}, \"eval-direct-correction-object-seed42-r3\": {}, \"eval-perdof-object-norm03-seed44\": {}, \"eval-mag-perdof-norm02-object\": {}, \"eval-acr-object-v4-scalar\": {}, \"eval-mag-obsonly-norm02\": {}, \"eval-mag-perdof-norm03\": {}, \"eval-mag-perdof-norm005\": {}, \"eval-mag-perdof-norm003\": {}, \"eval-vla-mean-spatial\": {}, \"eval-acr-object-obs-only-norm02\": {}, \"eval-spatial-v7-full\": {}, \"eval-object-v8-full\": {}, \"precompute-v5-shard2\": {}, \"precompute-v5-shard1\": {}, \"precompute-v5-shard0\": {}, \"precompute-v4-shard2\": {}, \"precompute-v4-shard1\": {}, \"precompute-v4-shard0\": {}, \"eval-vla-mean-spatial-t10\": {}, \"eval-reconvla-spatial-v3\": {}, \"crm-train-v2-scalar-unc\": {}, \"crm-train-v2-perdof\": {}, \"crm-train-v2-obs-only\": {}, \"precompute-shard2\": {}, \"precompute-shard1\": {}, \"precompute-shard0\": {}, \"precompute-k5\": {}, \"plan_014-reconvla-baseline\": {}, \"plan_001-crm-smolvla\": {}, \"mvp-point-reaching\": {}, \"eval-smolvla-libero-spatial\": {}, \"eval-obs-only-spatial\": {}, \"eval-obs-only-object-default-seed44\": {}, \"eval-mag-perdof-norm005-object\": {}, \"eval-mag-perdof-norm02-seed43-object-r3\": {}, \"eval-mag-perdof-norm03-object-r3\": {}, \"eval-mag-obsonly-norm005\": {}, \"eval-mag-obsonly-norm003-b2\": {}, \"eval-mag-obsonly-norm03-object\": {}, \"eval-mag-obsonly-norm005-object\": {}, \"eval-direct-correction-object-seed42-r2\": {}, \"eval-direct-correction-object-seed42\": {}, \"eval-scalar-object-seed44-r2\": {}, \"eval-perdof-object-seed44\": {}, \"eval-obs-only-object-norm03-seed44\": {}, \"eval-vla-mean-object-seed44\": {}, \"eval-obs-only-object-norm02-seed44-r4\": {}, \"eval-argmin-object-seed44-r2\": {}, \"eval-obs-only-object-norm03-seed45\": {}, \"eval-acr-object-v4-default-r2\": {}, \"eval-mag-perdof-norm003-object\": {}, \"eval-acr-object-obs-only-default\": {}, \"eval-scalar-object-seed43\": {}, \"eval-mag-obsonly-norm003-object\": {}, \"eval-scalar-object-seed44\": {}, \"eval-obs-only-object-norm02-seed44-r3\": {}, \"eval-argmin-object-seed44-r3\": {}, \"eval-vla-mean-object-seed43\": {}, \"eval-perdof-object-seed43\": {}, \"eval-vla-only-object-seed44\": {}, \"eval-obs-only-object-norm02-seed44\": {}, \"eval-argmin-object-seed44\": {}, \"eval-obs-only-object-seed43\": {}, \"eval-mag-obsonly-norm03-b2\": {}, \"eval-argmin-object-seed43\": {}, \"eval-mag-perdof-norm02-seed43-object-r2\": {}, \"eval-mag-obsonly-norm03\": {}, \"eval-mag-obsonly-norm02-object\": {}, \"eval-mag-obsonly-norm03-b4\": {}, \"eval-mag-obsonly-norm03-b3\": {}, \"eval-mag-perdof-norm02-seed43-object\": {}, \"eval-mag-perdof-norm03-object-r2\": {}, \"eval-acr-object-v4-scalar-b2\": {}, \"eval-acr-object-v4-obs-only-b2\": {}, \"eval-spatial-v4-full\": {}, \"eval-reconvla-spatial-v1\": {}, \"eval-object-v6-full\": {}, \"precompute-v3-shard2\": {}, \"precompute-v3-shard1\": {}, \"precompute-v3-shard0\": {}, \"precompute-v2-shard2\": {}, \"precompute-v2-shard1\": {}, \"precompute-v2-shard0\": {}, \"eval-mag-perdof-norm0p3-object-r2\": {}, \"eval-mag-perdof-norm0p3-object\": {}, \"eval-obs-only-object-norm02-seed43\": {}, \"eval-acr-object-v4-default\": {}, \"eval-mag-obsonly-norm03-r2\": {}, \"eval-vla-mean-object\": {}, \"eval-reconvla-object\": {}, \"eval-acr-object-v4-obs-only\": {}, \"eval-acr-object-v4-perdof\": {}, \"eval-acr-spatial-v4-scalar-r2\": {}, \"eval-acr-spatial-v4-obs-only-r3\": {}, \"eval-obs-only-spatial-seed43\": {}, \"eval-acr-spatial-v4-small-r2\": {}, \"eval-mag-obsonly-norm-0.3-r3\": {}, \"eval-mag-obsonly-norm-0p3-r3\": {}, \"eval-argmin-only-spatial-r2\": {}, \"eval-mag-obsonly-norm003\": {}, \"eval-vla-only-object-k1\": {}, \"eval-acr-spatial-v4-default-r3\": {}, \"eval-tiny-correction-spatial\": {}, \"eval-acr-spatial-v4-default-r2\": {}, \"eval-acr-spatial-v4-obs-only\": {}, \"eval-acr-spatial-v4-default\": {}, \"crm-train-v3-norm-scalar-unc\": {}, \"crm-train-v3-norm-obs-only\": {}, \"crm-train-v3-norm\": {}, \"crm-train-v3-scalar-unc\": {}, \"crm-train-v3-obs-only\": {}, \"crm-train-v3-perdof\": {}, \"eval-obs-only-spatial-v3\": {}, \"eval-scalar-unc-spatial-v2\": {}, \"crm-train-a4-scalar-unc\": {}, \"crm-train-a3-obs-only\": {}, \"crm-train-v1\": {}, \"crm-train-k5\": {}, \"eval-scalar-unc-spatial\": {}, \"eval-acr-spatial-v2\": {}, \"eval-k5-spatial\": {}, \"eval-object-v7-full\": {}, \"eval-spatial-v6-full\": {}, \"eval-object-v5-full\": {}, \"eval-acr-vla-spatial-v1\": {}, \"eval-acr-spatial-v1\": {}, \"eval-reconvla-spatial-v2\": {}, \"eval-object-v4-full\": {}, \"eval-spatial-v5-full\": {}, \"eval-spatial-v3-full\": {}, \"eval-spatial-reeval-v2\": {}}, \"count\": 1223, \"total\": 1223, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.5652}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
The registry returned results but without the `spec.command` field populated. I see `eval-random-selection-object-seed42` and `eval-ksweep-k20-obs-object-s43` exist. Let me query them specifically with all fields to get the command.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "f14e33e9-d204-44df-8e4f-e9bbe955b121",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqnQqvjud4bHjMhTHcBtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22743,
      "cache_read_input_tokens": 30031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22743
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

_source line 31_

GPU 释放确认完成。现在查参考实验的具体命令。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "3d572eff-ba1b-44cf-aaea-d8e45cfa2a53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqnQqvjud4bHjMhTHcBtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22743,
      "cache_read_input_tokens": 30031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22743
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

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01WXCMtUeH1Gsr9Qb2ijttoK`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "eval-random-selection-object-seed42"
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "2a7667d2-4853-4048-9249-5c57c6e9d8aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqnQqvjud4bHjMhTHcBtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22743,
      "cache_read_input_tokens": 30031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22743
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

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01NakMEdeX5oj5FXBqnLfDPs`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "eval-ksweep-k20-obs-object-s43"
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "bd4be3b9-edf3-4349-bf25-f57aa1346e6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqnQqvjud4bHjMhTHcBtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22743,
      "cache_read_input_tokens": 30031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22743
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

_source line 34_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01QJaqFtDU16ReyeqcuqSJ2K`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "eval-random-selection-object-seed44"
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "4d8c247b-3fe7-4037-813e-aa0555660e0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqnQqvjud4bHjMhTHcBtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22743,
      "cache_read_input_tokens": 30031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22743
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

_source line 35 · 2026-05-28T04:41:20.222Z_

<details><summary>↩ Tool result · `toolu_01WXCMtUeH1Gsr9Qb2ijttoK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.094}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "e4344644-dc53-4112-a30d-13a8d9ec722b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.094}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.094}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T04:41:23.395Z_

<details><summary>↩ Tool result · `toolu_01NakMEdeX5oj5FXBqnLfDPs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1512}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "e67404cc-6a93-435d-a80a-d20447088364",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.1512}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1512}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-28T04:41:28.101Z_

<details><summary>↩ Tool result · `toolu_01QJaqFtDU16ReyeqcuqSJ2K`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.6476}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "54df7192-b408-4a7e-8eba-47f8a5a26d2a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.6476}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.6476}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
The `exp_id` filter doesn't seem to work properly. The experiments exist in the list (I can see `eval-random-selection-object-seed42`, `eval-random-selection-object-seed44`, `eval-ksweep-k20-obs-object-s43` in the earlier query results), but the exact filter isn't matching. Let me try to get specific fields from those experiments.

Actually wait, looking at the earlier results, they are returned as a dict with exp_id as keys. But when I filter by `exp_id`, it returns 0 results. Maybe the filter field name is different. 

I'll try fetching the experiments without the filter constraint and just pull the commands I need. Or maybe I should check the registry YAML file directly on the server to understand the structure better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "929c9485-b46c-47fd-b349-5b07be104674",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wia5DRPzbuhSgHcbBYEwx3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 52774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 805
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 39_

Registry 的 exp_id 过滤不工作。直接从服务器读取 registry 文件获取参考命令。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "443a0d5a-7bb6-47ca-86fb-63f6177b7008",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wia5DRPzbuhSgHcbBYEwx3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 52774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 805
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DTRucdG3QSc61oTYs86QfF`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -A 20 \"eval-random-selection-object-seed42:\" /root/acr-vla-conformal-refinement/registry.yaml",
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "354f3efb-8181-4d7a-9862-c16b1f6e508c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wia5DRPzbuhSgHcbBYEwx3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 52774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 805
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0184VKAE8TNHLVvc3ZVrBsWi`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -A 20 \"eval-ksweep-k20-obs-object-s43:\" /root/acr-vla-conformal-refinement/registry.yaml",
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "5515bb61-af3a-47d4-9d41-4dd5885bfcb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wia5DRPzbuhSgHcbBYEwx3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 52774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 805
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 42 · 2026-05-28T04:41:37.737Z_

<details><summary>↩ Tool result · `toolu_01DTRucdG3QSc61oTYs86QfF`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/acr-vla-conformal-refinement/registry.yaml: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.01}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "0a342ae1-3d09-4ca6-b8ba-2c7bb3b1b969",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"grep: /root/acr-vla-conformal-refinement/registry.yaml: No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.01}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/acr-vla-conformal-refinement/registry.yaml: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.01}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-28T04:41:38.159Z_

<details><summary>↩ Tool result · `toolu_0184VKAE8TNHLVvc3ZVrBsWi`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/acr-vla-conformal-refinement/registry.yaml: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "4f77afab-c498-46bc-aee6-e511f0bc9cb3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"grep: /root/acr-vla-conformal-refinement/registry.yaml: No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/acr-vla-conformal-refinement/registry.yaml: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
The registry file isn't at that path. Let me find the actual registry location. The registry is managed by the MCP tools, so it's probably somewhere in the agent-ml-research project directory. Let me look for it locally.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "2b98e203-4ea1-45de-b182-278873956669",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCktRSQkiLQ4sEKC3cgwPy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 759,
      "cache_read_input_tokens": 53579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 759
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

_source line 45_

<details open><summary>🔧 Tool call — Glob · `toolu_01BeaTmhVYFAfYRHy2pcbyr8`</summary>

```json
{
  "pattern": "**/registry*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "c3ba2efd-b65d-4115-9ca1-47f2630d39a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCktRSQkiLQ4sEKC3cgwPy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 759,
      "cache_read_input_tokens": 53579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 759
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

_source line 46 · 2026-05-28T04:41:42.619Z_

<details><summary>↩ Tool result · `toolu_01BeaTmhVYFAfYRHy2pcbyr8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/global/registry.yaml
registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "10f784d4-3017-4596-9a9b-e7d317f39394",
  "tool_use_result": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/global/registry.yaml",
      "registry.yaml"
    ],
    "durationMs": 47,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jzf4aZAyBWU5Sd4vSnGEaT`</summary>

```json
{
  "command": "grep -A 20 \"eval-random-selection-object-seed42:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "description": "Find random-selection-object-seed42 command in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "45459b30-946d-4870-b537-015b7b0c2569",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvbX5j3GW4QZsmNsKidoYU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 298,
      "cache_read_input_tokens": 54338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 298
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

### Tool result

_source line 48 · 2026-05-28T04:41:46.331Z_

<details><summary>↩ Tool result · `toolu_01Jzf4aZAyBWU5Sd4vSnGEaT`</summary>

```text
  eval-random-selection-object-seed42:
    status: DONE
    retry_count: 1
    created_at: '2026-05-17T13:32:30.506Z'
    updated_at: '2026-05-20T09:26:47.119Z'
    hypothesis: Random selection baseline (K=10 随机选一个 action) on LIBERO-Object seed42.
      Ablation 验证 CRM uncertainty-guided selection 的价值。
    completed_at: '2026-05-18T12:20:08.756Z'
    extra:
      previous_failure:
        conclusion: success
        metrics:
          success_rate: 0.13
          n_tasks: 10
          n_rollouts: 10
          total_rollouts: 100
          per_task_sr:
          - 0
          - 0.1
          - 0.1
          - 0.4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "1faa0c90-1b32-469d-b0d9-2f31e1ea2bf3",
  "tool_use_result": {
    "stdout": "  eval-random-selection-object-seed42:\n    status: DONE\n    retry_count: 1\n    created_at: '2026-05-17T13:32:30.506Z'\n    updated_at: '2026-05-20T09:26:47.119Z'\n    hypothesis: Random selection baseline (K=10 随机选一个 action) on LIBERO-Object seed42.\n      Ablation 验证 CRM uncertainty-guided selection 的价值。\n    completed_at: '2026-05-18T12:20:08.756Z'\n    extra:\n      previous_failure:\n        conclusion: success\n        metrics:\n          success_rate: 0.13\n          n_tasks: 10\n          n_rollouts: 10\n          total_rollouts: 100\n          per_task_sr:\n          - 0\n          - 0.1\n          - 0.1\n          - 0.4",
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

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01NLDSAvJpLKgS19teppL5Yw`</summary>

```json
{
  "command": "grep -A 20 \"eval-ksweep-k20-obs-object-s43:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "description": "Find ksweep-k20 command in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "4000b30b-0ca4-46c0-9197-52d586b81101",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvbX5j3GW4QZsmNsKidoYU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 298,
      "cache_read_input_tokens": 54338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 298
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

### Tool result

_source line 50 · 2026-05-28T04:41:46.912Z_

<details><summary>↩ Tool result · `toolu_01NLDSAvJpLKgS19teppL5Yw`</summary>

```text
  eval-ksweep-k20-obs-object-s43:
    status: DONE
    retry_count: 0
    created_at: '2026-05-27T06:39:17.001Z'
    updated_at: '2026-05-27T10:00:17.626Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
        --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --crm_checkpoint
        /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark
        object --seed 43 --n_rollouts 20 --output_file logs/eval_object_obs_only_k20_norm02_s43.json"
      server: bjb1-18228
      gpu:
      - cuda:3
      pid: '616215'
      log_path: ~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s43.log
      submitted_at: '2026-05-27T06:39:14.276Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      data_count: 200
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "0b0a3467-4df0-4868-85b5-7696ae32de01",
  "tool_use_result": {
    "stdout": "  eval-ksweep-k20-obs-object-s43:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-27T06:39:17.001Z'\n    updated_at: '2026-05-27T10:00:17.626Z'\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py\n        --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --crm_checkpoint\n        /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark\n        object --seed 43 --n_rollouts 20 --output_file logs/eval_object_obs_only_k20_norm02_s43.json\"\n      server: bjb1-18228\n      gpu:\n      - cuda:3\n      pid: '616215'\n      log_path: ~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s43.log\n      submitted_at: '2026-05-27T06:39:14.276Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      data_count: 200",
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

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Got the ksweep command. Now let me also get the random-selection command with spec. Let me look for more details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "5647f8f9-af17-497b-a160-58e744c17643",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxWZth5fKVevLFBgLLdh9p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 922,
      "cache_read_input_tokens": 54636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 922
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01NXgJWNt9SH13zrzJxMLcx8`</summary>

```json
{
  "command": "grep -A 40 \"eval-random-selection-object-seed44:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "description": "Find random-selection-object-seed44 command in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "7ac5539a-27a5-4f86-aa8b-0a8695f55b28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxWZth5fKVevLFBgLLdh9p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 922,
      "cache_read_input_tokens": 54636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 922
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 53 · 2026-05-28T04:41:51.557Z_

<details><summary>↩ Tool result · `toolu_01NXgJWNt9SH13zrzJxMLcx8`</summary>

```text
  eval-random-selection-object-seed44:
    status: DONE
    retry_count: 1
    created_at: '2026-05-18T02:25:56.030Z'
    updated_at: '2026-05-21T04:34:43.303Z'
    hypothesis: Random Selection (K=10, uniform pick) on LIBERO-Object seed44. Third
      seed for Random Selection Object baseline.
    completed_at: '2026-05-18T19:54:45.658Z'
    extra:
      previous_failure:
        conclusion: success
        metrics:
          success_rate: 0.13
          n_tasks: 10
          n_rollouts: 10
          total_rollouts: 100
      hook_events:
      - event: on_complete
        action: agent
        ts: '2026-05-20T08:44:57.080310+00:00'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
        --mode random_selection --benchmark object --K 10 --seed 44 --n_rollouts 10
        --output_file logs/eval_random_selection_object_seed44.json 2>&1 | tee logs/eval-random-selection-object-seed44.log"
      server: bjb1-32546
      gpu:
      - cuda:3
      pid: '853229'
      log_path: ~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed44.log
      submitted_at: '2026-05-21T04:34:41.887Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
    notes: 'Random selection baseline seed44 完成。SR=0.11, 10 tasks × 10 rollouts =
      100 total。三个 seed 汇总: seed43=0.09, seed44=0.11, seed45=0.10, 均值≈0.10。与 VLA-only
      baseline 相当，确认 random selection 无法有效利用 K=10 candidates。'
    reproduce:
      finished_at: '2026-05-20T08:44:41.731Z'
    metrics:
      overall_success_rate: 0.11
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "ddbd0177-2e27-4e9a-bcbb-293084428d26",
  "tool_use_result": {
    "stdout": "  eval-random-selection-object-seed44:\n    status: DONE\n    retry_count: 1\n    created_at: '2026-05-18T02:25:56.030Z'\n    updated_at: '2026-05-21T04:34:43.303Z'\n    hypothesis: Random Selection (K=10, uniform pick) on LIBERO-Object seed44. Third\n      seed for Random Selection Object baseline.\n    completed_at: '2026-05-18T19:54:45.658Z'\n    extra:\n      previous_failure:\n        conclusion: success\n        metrics:\n          success_rate: 0.13\n          n_tasks: 10\n          n_rollouts: 10\n          total_rollouts: 100\n      hook_events:\n      - event: on_complete\n        action: agent\n        ts: '2026-05-20T08:44:57.080310+00:00'\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py\n        --mode random_selection --benchmark object --K 10 --seed 44 --n_rollouts 10\n        --output_file logs/eval_random_selection_object_seed44.json 2>&1 | tee logs/eval-random-selection-object-seed44.log\"\n      server: bjb1-32546\n      gpu:\n      - cuda:3\n      pid: '853229'\n      log_path: ~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed44.log\n      submitted_at: '2026-05-21T04:34:41.887Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n    notes: 'Random selection baseline seed44 完成。SR=0.11, 10 tasks × 10 rollouts =\n      100 total。三个 seed 汇总: seed43=0.09, seed44=0.11, seed45=0.10, 均值≈0.10。与 VLA-only\n      baseline 相当，确认 random selection 无法有效利用 K=10 candidates。'\n    reproduce:\n      finished_at: '2026-05-20T08:44:41.731Z'\n    metrics:\n      overall_success_rate: 0.11",
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

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01K4tCPqweaozsgbfRL3FTpx`</summary>

```json
{
  "command": "grep -A 40 \"eval-random-selection-object-seed43:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "description": "Find random-selection-object-seed43 command in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "09e123cc-47d1-47ce-abdd-7f5c44bc1b55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxWZth5fKVevLFBgLLdh9p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 922,
      "cache_read_input_tokens": 54636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 922
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 55 · 2026-05-28T04:41:52.214Z_

<details><summary>↩ Tool result · `toolu_01K4tCPqweaozsgbfRL3FTpx`</summary>

```text
  eval-random-selection-object-seed43:
    status: DONE
    retry_count: 0
    created_at: '2026-05-17T23:10:52.130Z'
    updated_at: '2026-05-21T04:34:38.177Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
        --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 10
        --output_file logs/eval_random_selection_object_seed43.json 2>&1 | tee logs/eval-random-selection-object-seed43.log"
      server: bjb1-32546
      gpu:
      - cuda:1
      pid: '852632'
      log_path: ~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43.log
      submitted_at: '2026-05-21T04:34:36.549Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
    hypothesis: Random Selection (K=10, uniform pick) on LIBERO-Object seed43. Second
      seed for Random Selection Object baseline.
    reproduce:
      finished_at: '2026-05-18T15:47:26.699Z'
    extra:
      hook_events:
      - event: on_complete
        action: agent
        ts: '2026-05-18T15:47:36.829906+00:00'
    metrics:
      success_rate: 0.09
      n_tasks: 10
      n_rollouts: 10
      total_rollouts: 100
      per_task_sr:
      - 0
      - 0
      - 0.1
      - 0.1
      - 0
      - 0.1
      - 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "9238e588-c5e2-4f3e-a90b-f2ed2a989c33",
  "tool_use_result": {
    "stdout": "  eval-random-selection-object-seed43:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-17T23:10:52.130Z'\n    updated_at: '2026-05-21T04:34:38.177Z'\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py\n        --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 10\n        --output_file logs/eval_random_selection_object_seed43.json 2>&1 | tee logs/eval-random-selection-object-seed43.log\"\n      server: bjb1-32546\n      gpu:\n      - cuda:1\n      pid: '852632'\n      log_path: ~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43.log\n      submitted_at: '2026-05-21T04:34:36.549Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n    hypothesis: Random Selection (K=10, uniform pick) on LIBERO-Object seed43. Second\n      seed for Random Selection Object baseline.\n    reproduce:\n      finished_at: '2026-05-18T15:47:26.699Z'\n    extra:\n      hook_events:\n      - event: on_complete\n        action: agent\n        ts: '2026-05-18T15:47:36.829906+00:00'\n    metrics:\n      success_rate: 0.09\n      n_tasks: 10\n      n_rollouts: 10\n      total_rollouts: 100\n      per_task_sr:\n      - 0\n      - 0\n      - 0.1\n      - 0.1\n      - 0\n      - 0.1\n      - 0",
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

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
Now I have the reference commands. Let me also check what Pi05 experiments are running or still needed for bjb2-28827 cuda:4/5.

Let me first deploy the two experiments on bjb1-32546 cuda:3 and cuda:4. 

For cuda:3 - random selection seed43:
The seed43 experiment already exists and is DONE! `eval-random-selection-object-seed43` is already done with SR=0.09. The user wants `eval-random-selection-object-seed43-v2` though.

Wait, looking again at the task - the user wants me to deploy:


I see that `eval-random-selection-object-seed43-v2` already exists as DONE with metrics, but I should follow the user's instructions and deploy it anyway. The key difference is the user's template specifies `--n_rollouts 20` whereas the old seed43 used `--n_rollouts 10`, so I'll use the updated value. I also need to check if the seed44 version includes `--model smolvla` explicitly since the old random-selection commands don't have it.

Looking at the seed44 reference command, it doesn't include the `--model smolvla` flag either, but the user specifically requested SmolVLA (not OpenVLA), so I should add that to match their template. For the cuda:4 ksweep with K=20 seed44, I'm examining the reference command structure...

Actually, I need to check what experiments are currently running on the Pi05 instances to determine what should be deployed on bjb2-28827 cuda:4/5.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "b23f7eae-bd52-4890-9fc5-31fddab22b00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhV18qZrsZ9CXTUbtquaP1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1480,
      "cache_read_input_tokens": 55558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1480
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 57_

找到参考命令。现在查 Pi05 运行中的实验以决定 bjb2-28827 部署方案。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "7ae4b0c8-0b0e-4998-8fdb-5b1c01b02be2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhV18qZrsZ9CXTUbtquaP1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1480,
      "cache_read_input_tokens": 55558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1480
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LLLNkN9F58w1eQwYthjawu`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "RUNNING"
  },
  "fields": [
    "exp_id",
    "status",
    "spec"
  ],
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "6007a260-13f2-40f7-8ac5-8680b2af29bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhV18qZrsZ9CXTUbtquaP1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1480,
      "cache_read_input_tokens": 55558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1480
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 59 · 2026-05-28T04:42:16.662Z_

<details><summary>↩ Tool result · `toolu_01LLLNkN9F58w1eQwYthjawu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"pi05-crm-always-on-long-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"pid\": \"156008\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log\", \"submitted_at\": \"2026-05-27T21:56:10.320Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval-only)\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO long benchmark\", \"data_count\": 200}}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.2925}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "6b49f596-2d6b-4da0-8797-feac10c2d81c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"pi05-crm-always-on-long-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"156008\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T21:56:10.320Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO long benchmark\\\", \\\"data_count\\\": 200}}}, \\\"count\\\": 1, \\\"total\\\": 1, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.2925}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"pi05-crm-always-on-long-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"pid\": \"156008\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log\", \"submitted_at\": \"2026-05-27T21:56:10.320Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval-only)\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO long benchmark\", \"data_count\": 200}}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.2925}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
Only 1 RUNNING experiment: `pi05-crm-always-on-long-s42` on cqa1. Let me check what Pi05 CRM always-on experiments exist and their status to figure out what's missing.

According to the user:
- Object: s42 (90.5%), s43 (92.0%) — 缺 s44（正在 bjb1-32546 跑）
- Spatial: s42 (96.0%) — s43/s44 正在 bjb1-18228 跑  


- Goal: s42 (81.5%) — s43/s44 正在 bjb1-32546 跑
- Long: s42 运行中 (cqa1) — s43/s44 正在 bjb1-18228 跑

The user mentioned s43/s44 are running for various tasks, but the registry only shows one active experiment. These could be the ghost processes we just terminated. Let me search through the pi05-crm-always-on experiments to see which ones are actually completed versus which were those phantom processes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "633b14a3-cc58-4ffd-8d7b-5d20f7e19a8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLoWTgNLMrRrZyqpeFJ6LL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1253,
      "cache_read_input_tokens": 57038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1253
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01EkvpQiJAHtDxPi2jrmh3C6`</summary>

```json
{
  "command": "grep -B1 \"pi05-crm-always-on\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | grep -E \"(pi05-crm-always-on|status)\"",
  "description": "Check all pi05-crm-always-on experiments status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "e7484713-b970-42bd-8e6b-a5f71dbe37d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLoWTgNLMrRrZyqpeFJ6LL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1253,
      "cache_read_input_tokens": 57038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1253
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 62 · 2026-05-28T04:42:27.991Z_

<details><summary>↩ Tool result · `toolu_01EkvpQiJAHtDxPi2jrmh3C6`</summary>

```text
  pi05-crm-always-on-object-s42:
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log
    log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log
  pi05-crm-always-on-spatial-s42:
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s42.log
    log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s42.log
  pi05-crm-always-on-goal-s42:
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s42.log
    log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s42.log
  pi05-crm-always-on-long-s42:
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log
  pi05-crm-always-on-object-s43:
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s43.log
  pi05-crm-always-on-long-s43:
    parent: pi05-crm-always-on-long-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s43.log
  pi05-crm-always-on-spatial-s43:
    parent: pi05-crm-always-on-spatial-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s43.log
  pi05-crm-always-on-goal-s43:
    parent: pi05-crm-always-on-goal-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log
  pi05-crm-always-on-long-s44:
    parent: pi05-crm-always-on-long-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s44.log
  pi05-crm-always-on-goal-s44:
    parent: pi05-crm-always-on-goal-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log
  pi05-crm-always-on-spatial-s44:
    parent: pi05-crm-always-on-spatial-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s44.log
  pi05-crm-always-on-object-s44:
    parent: pi05-crm-always-on-object-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "092393b6-1023-41ab-9cf0-66e7fac529fd",
  "tool_use_result": {
    "stdout": "  pi05-crm-always-on-object-s42:\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log\n    log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log\n  pi05-crm-always-on-spatial-s42:\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s42.log\n    log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s42.log\n  pi05-crm-always-on-goal-s42:\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s42.log\n    log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s42.log\n  pi05-crm-always-on-long-s42:\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log\n  pi05-crm-always-on-object-s43:\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s43.log\n  pi05-crm-always-on-long-s43:\n    parent: pi05-crm-always-on-long-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s43.log\n  pi05-crm-always-on-spatial-s43:\n    parent: pi05-crm-always-on-spatial-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s43.log\n  pi05-crm-always-on-goal-s43:\n    parent: pi05-crm-always-on-goal-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log\n  pi05-crm-always-on-long-s44:\n    parent: pi05-crm-always-on-long-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s44.log\n  pi05-crm-always-on-goal-s44:\n    parent: pi05-crm-always-on-goal-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log\n  pi05-crm-always-on-spatial-s44:\n    parent: pi05-crm-always-on-spatial-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s44.log\n  pi05-crm-always-on-object-s44:\n    parent: pi05-crm-always-on-object-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log",
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

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_01WtTFHepWAuR3eZE3yihgQK`</summary>

```json
{
  "command": "grep -A 2 \"pi05-crm-always-on-\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | grep -E \"(pi05-crm-always-on|status:)\"",
  "description": "Get status of all pi05-crm-always-on experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "3cfd46fc-e398-4321-a51f-87c2bebedda3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rbbstdbyV6R48xxyX6Y9F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1343,
      "cache_read_input_tokens": 58291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1343
      },
      "output_tokens": 47,
      "service_tier": "standard",
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

_source line 64 · 2026-05-28T04:42:32.664Z_

<details><summary>↩ Tool result · `toolu_01WtTFHepWAuR3eZE3yihgQK`</summary>

```text
  pi05-crm-always-on-object-s42:
    status: DONE
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log
    log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log
  pi05-crm-always-on-spatial-s42:
    status: DONE
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s42.log
    log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s42.log
  pi05-crm-always-on-goal-s42:
    status: DONE
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s42.log
    log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s42.log
  pi05-crm-always-on-long-s42:
    status: RUNNING
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log
  pi05-crm-always-on-object-s43:
    status: DONE
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s43.log
  pi05-crm-always-on-long-s43:
    status: PREPARING
    parent: pi05-crm-always-on-long-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s43.log
  pi05-crm-always-on-spatial-s43:
    status: PREPARING
    parent: pi05-crm-always-on-spatial-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s43.log
  pi05-crm-always-on-goal-s43:
    status: PREPARING
    parent: pi05-crm-always-on-goal-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log
  pi05-crm-always-on-long-s44:
    status: PREPARING
    parent: pi05-crm-always-on-long-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s44.log
  pi05-crm-always-on-goal-s44:
    status: PREPARING
    parent: pi05-crm-always-on-goal-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log
  pi05-crm-always-on-spatial-s44:
    status: PREPARING
    parent: pi05-crm-always-on-spatial-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s44.log
  pi05-crm-always-on-object-s44:
    status: PREPARING
    parent: pi05-crm-always-on-object-s42
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "469f27a7-ab3a-4d00-ac43-b6a1cd974211",
  "tool_use_result": {
    "stdout": "  pi05-crm-always-on-object-s42:\n    status: DONE\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log\n    log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log\n  pi05-crm-always-on-spatial-s42:\n    status: DONE\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s42.log\n    log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s42.log\n  pi05-crm-always-on-goal-s42:\n    status: DONE\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s42.log\n    log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s42.log\n  pi05-crm-always-on-long-s42:\n    status: RUNNING\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log\n  pi05-crm-always-on-object-s43:\n    status: DONE\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s43.log\n  pi05-crm-always-on-long-s43:\n    status: PREPARING\n    parent: pi05-crm-always-on-long-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s43.log\n  pi05-crm-always-on-spatial-s43:\n    status: PREPARING\n    parent: pi05-crm-always-on-spatial-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s43.log\n  pi05-crm-always-on-goal-s43:\n    status: PREPARING\n    parent: pi05-crm-always-on-goal-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log\n  pi05-crm-always-on-long-s44:\n    status: PREPARING\n    parent: pi05-crm-always-on-long-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s44.log\n  pi05-crm-always-on-goal-s44:\n    status: PREPARING\n    parent: pi05-crm-always-on-goal-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log\n  pi05-crm-always-on-spatial-s44:\n    status: PREPARING\n    parent: pi05-crm-always-on-spatial-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s44.log\n  pi05-crm-always-on-object-s44:\n    status: PREPARING\n    parent: pi05-crm-always-on-object-s42\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log",
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

_source line 65_

<details><summary>Logged reasoning block</summary>

```text
Now I see:
- Pi05 CRM always-on DONE: object-s42, spatial-s42, goal-s42, object-s43
- Pi05 CRM always-on RUNNING: long-s42 (on cqa1)
- Pi05 CRM always-on PREPARING: long-s43, spatial-s43, goal-s43, long-s44, goal-s44, spatial-s44, object-s44

So the user was wrong about some being "正在跑" — they're actually in PREPARING status, meaning the ghost processes may have been running them but now they're killed.


I need to deploy the PREPARING experiments to bjb2-28827 cuda:4/5, prioritizing object-s44 (which the user mentioned was running on bjb1-32546) and the spatial and goal variants for s43 and s44. Since the user said to deploy SmolVLA tau-sweep once all Pi05 seeds are deployed, I should grab the deployment command for these Pi05 CRM always-on experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "eba8676b-0ad4-4a53-b23f-5325c9807c4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BCT36sV5rCvnC8GTQMHrYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 59634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1122
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 66_

Pi05 CRM always-on 有多个还在 PREPARING 状态。获取参考命令并开始部署。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "e6ebeed2-7ab2-46b7-9d82-7cac70a00304",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BCT36sV5rCvnC8GTQMHrYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 59634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1122
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 67_

<details open><summary>🔧 Tool call — Bash · `toolu_01U8hpemRVSLsCZ7syML8dxs`</summary>

```json
{
  "command": "grep -A 30 \"pi05-crm-always-on-object-s43:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -35",
  "description": "Get pi05-crm-always-on-object-s43 command"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "b390b671-67f6-4829-8898-9a82389ed8fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BCT36sV5rCvnC8GTQMHrYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 59634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1122
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 68 · 2026-05-28T04:42:47.115Z_

<details><summary>↩ Tool result · `toolu_01U8hpemRVSLsCZ7syML8dxs`</summary>

```text
  pi05-crm-always-on-object-s43:
    status: DONE
    retry_count: 0
    created_at: '2026-05-27T23:15:13.105Z'
    updated_at: '2026-05-28T03:03:14.655Z'
    hypothesis: 'Pi05 CRM always-on (τ=0.001) on Object suite s43. Ablation: CRM correction
      applied every step (trigger_rate=100%) to measure CRM-only contribution without
      conformal gating. Table 1 data for Pi05 model, second seed.'
    spec:
      command: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
        && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model
        pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold
        0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt
        --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts
        20 --output_file logs/eval_object_crm_always_on_pi05_k2_norm0.2_seed43.json
      server: cqa1-32758
      gpu:
      - cuda:0
      pid: 190565
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s43.log
      account: root
      data_path: LIBERO-Object (built-in)
      data_count: '200'
      model_name: pi05
      seed: 43
      checkpoint_source: /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt
      eval_data: LIBERO-Object
    reproduce:
      finished_at: '2026-05-28T02:59:26.584Z'
    extra:
      hook_events:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "8bb6e770-3e74-4668-93f6-0ba914e4f9b0",
  "tool_use_result": {
    "stdout": "  pi05-crm-always-on-object-s43:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-27T23:15:13.105Z'\n    updated_at: '2026-05-28T03:03:14.655Z'\n    hypothesis: 'Pi05 CRM always-on (τ=0.001) on Object suite s43. Ablation: CRM correction\n      applied every step (trigger_rate=100%) to measure CRM-only contribution without\n      conformal gating. Table 1 data for Pi05 model, second seed.'\n    spec:\n      command: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n        && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model\n        pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold\n        0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\n        --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts\n        20 --output_file logs/eval_object_crm_always_on_pi05_k2_norm0.2_seed43.json\n      server: cqa1-32758\n      gpu:\n      - cuda:0\n      pid: 190565\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s43.log\n      account: root\n      data_path: LIBERO-Object (built-in)\n      data_count: '200'\n      model_name: pi05\n      seed: 43\n      checkpoint_source: /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\n      eval_data: LIBERO-Object\n    reproduce:\n      finished_at: '2026-05-28T02:59:26.584Z'\n    extra:\n      hook_events:",
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

_source line 69_

<details open><summary>🔧 Tool call — Bash · `toolu_014zmuCDrJdvR1FeqYQW7x5a`</summary>

```json
{
  "command": "grep -A 30 \"pi05-crm-always-on-spatial-s43:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -35",
  "description": "Get pi05-crm-always-on-spatial-s43 spec"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "d6adbeba-10be-41fa-b2ee-f256d78bafcb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BCT36sV5rCvnC8GTQMHrYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 59634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1122
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 70 · 2026-05-28T04:42:47.828Z_

<details><summary>↩ Tool result · `toolu_014zmuCDrJdvR1FeqYQW7x5a`</summary>

```text
  pi05-crm-always-on-spatial-s43:
    status: PREPARING
    retry_count: 0
    created_at: '2026-05-28T03:09:36.681Z'
    updated_at: '2026-05-28T03:11:25.661Z'
    hypothesis: Pi05 CRM always-on (τ=0.001) on Spatial suite s43. Second seed for
      Table 2 Spatial row.
    parent: pi05-crm-always-on-spatial-s42
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
        --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2
        --conformal_threshold 0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt
        --obs_dim 2048 --unified_obs_dim 2088 --benchmark spatial --seed 43 --n_rollouts
        20 --output_file logs/eval_spatial_crm_always_on_pi05_k2_norm0.2_seed43.json"
      server: bjb1-18228
      gpu:
      - cuda:1
      pid: '982668'
      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s43.log
      submitted_at: '2026-05-28T03:11:17.581Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
  pi05-crm-always-on-goal-s43:
    status: PREPARING
    retry_count: 0
    created_at: '2026-05-28T03:09:46.268Z'
    updated_at: '2026-05-28T03:11:36.225Z'
    hypothesis: Pi05 CRM always-on (τ=0.001) on Goal suite s43. Second seed for Table
      2 Goal row, measuring CRM-only degradation without conformal gating on Pi05.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "977df2fa-54c9-4a45-b1eb-c180b1e8b376",
  "tool_use_result": {
    "stdout": "  pi05-crm-always-on-spatial-s43:\n    status: PREPARING\n    retry_count: 0\n    created_at: '2026-05-28T03:09:36.681Z'\n    updated_at: '2026-05-28T03:11:25.661Z'\n    hypothesis: Pi05 CRM always-on (τ=0.001) on Spatial suite s43. Second seed for\n      Table 2 Spatial row.\n    parent: pi05-crm-always-on-spatial-s42\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py\n        --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2\n        --conformal_threshold 0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\n        --obs_dim 2048 --unified_obs_dim 2088 --benchmark spatial --seed 43 --n_rollouts\n        20 --output_file logs/eval_spatial_crm_always_on_pi05_k2_norm0.2_seed43.json\"\n      server: bjb1-18228\n      gpu:\n      - cuda:1\n      pid: '982668'\n      log_path: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-spatial-s43.log\n      submitted_at: '2026-05-28T03:11:17.581Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n  pi05-crm-always-on-goal-s43:\n    status: PREPARING\n    retry_count: 0\n    created_at: '2026-05-28T03:09:46.268Z'\n    updated_at: '2026-05-28T03:11:36.225Z'\n    hypothesis: Pi05 CRM always-on (τ=0.001) on Goal suite s43. Second seed for Table\n      2 Goal row, measuring CRM-only degradation without conformal gating on Pi05.",
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

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
Now I have all reference commands. Let me check if the PREPARING experiments were the ghost processes that we just killed. The spatial-s43 was submitted to bjb1-18228 not bjb2-28827 or bjb1-32546. The ghost processes we killed were on bjb2-28827 and bjb1-32546.

Let me check what was running on those specific servers before.

Actually, the task says:
1. bjb1-32546 cuda:3 → random selection seed43 (plan_600)


2. bjb1-32546 cuda:4 → K-sweep K=20 seed44 (plan_601)
3. bjb2-28827 cuda:4/5 → Pi05 or SmolVLA

For bjb2-28827, I need to figure out which Pi05 experiments to deploy. Two of them are already running on bjb1-18228, but I have two PREPARING experiments that need servers: the long and spatial variants with seed44.

Looking at the remaining PREPARING experiments, there are several more variants with seed44 that haven't been submitted yet. I should check which ones are actually missing submissions versus which ones might still be running on bjb1-18228 that we didn't terminate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "b3090f19-8bc4-44c0-ae1d-3ff39d612f98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5zkpCZWrJkrK59uVQRhLy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1928,
      "cache_read_input_tokens": 60756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1928
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_012u2kHRcKgWZEFya5g6ubMi`</summary>

```json
{
  "command": "for exp in pi05-crm-always-on-long-s43 pi05-crm-always-on-long-s44 pi05-crm-always-on-goal-s43 pi05-crm-always-on-goal-s44 pi05-crm-always-on-spatial-s43 pi05-crm-always-on-spatial-s44 pi05-crm-always-on-object-s44; do echo \"=== $exp ===\"; grep -A 25 \"$exp:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | grep -E \"(status|server|gpu|pid)\" | head -4; done",
  "description": "Check PREPARING experiments' server assignments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "cf7654f2-c85f-4e66-a7a4-37e5a207bf3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5zkpCZWrJkrK59uVQRhLy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1928,
      "cache_read_input_tokens": 60756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1928
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 73 · 2026-05-28T04:43:08.411Z_

<details><summary>↩ Tool result · `toolu_012u2kHRcKgWZEFya5g6ubMi`</summary>

```text
=== pi05-crm-always-on-long-s43 ===
    status: PREPARING
      server: bjb1-18228
      gpu:
      pid: '982384'
=== pi05-crm-always-on-long-s44 ===
    status: PREPARING
      server: bjb1-18228
      gpu:
      pid: '983101'
=== pi05-crm-always-on-goal-s43 ===
    status: PREPARING
      server: bjb1-32546
      gpu:
      pid: '510334'
=== pi05-crm-always-on-goal-s44 ===
    status: PREPARING
      server: bjb1-32546
      gpu:
      pid: '510700'
=== pi05-crm-always-on-spatial-s43 ===
    status: PREPARING
      server: bjb1-18228
      gpu:
      pid: '982668'
=== pi05-crm-always-on-spatial-s44 ===
    status: PREPARING
      server: bjb1-18228
      gpu:
      pid: '983391'
=== pi05-crm-always-on-object-s44 ===
    status: PREPARING
      server: bjb1-32546
      gpu:
      pid: '510990'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "4e9f47c0-3d9f-431c-bb31-674b7881f602",
  "tool_use_result": {
    "stdout": "=== pi05-crm-always-on-long-s43 ===\n    status: PREPARING\n      server: bjb1-18228\n      gpu:\n      pid: '982384'\n=== pi05-crm-always-on-long-s44 ===\n    status: PREPARING\n      server: bjb1-18228\n      gpu:\n      pid: '983101'\n=== pi05-crm-always-on-goal-s43 ===\n    status: PREPARING\n      server: bjb1-32546\n      gpu:\n      pid: '510334'\n=== pi05-crm-always-on-goal-s44 ===\n    status: PREPARING\n      server: bjb1-32546\n      gpu:\n      pid: '510700'\n=== pi05-crm-always-on-spatial-s43 ===\n    status: PREPARING\n      server: bjb1-18228\n      gpu:\n      pid: '982668'\n=== pi05-crm-always-on-spatial-s44 ===\n    status: PREPARING\n      server: bjb1-18228\n      gpu:\n      pid: '983391'\n=== pi05-crm-always-on-object-s44 ===\n    status: PREPARING\n      server: bjb1-32546\n      gpu:\n      pid: '510990'",
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

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
Now I see the picture:

PREPARING experiments and their servers:
- **bjb1-18228**: long-s43 (pid 982384), long-s44 (pid 983101), spatial-s43 (pid 982668), spatial-s44 (pid 983391)
- **bjb1-32546**: goal-s43 (pid 510334), goal-s44 (pid 510700), object-s44 (pid 510990)

The ghost processes we killed on bjb1-32546 were PIDs 515230 and 515586 — different PIDs from the ones in registry (510334, 510700, 510990). 

The PREPARING experiments on bjb1-18228 might still be running, while the ones on bjb1-32546 likely had their processes die or get replaced. Since bjb2-28827 has no Pi05 experiments assigned, all 6 GPUs there are available for the missing deployments. The PREPARING experiments on bjb1-32546 are likely already dead since the PIDs we killed (515230, 515586) don't match the ones listed for those jobs (510334, 510700, 510990), suggesting they were ghost processes from an earlier cleanup attempt.

Now I need to focus on deploying the three critical Pi05 experiments to bjb2-28827, which has 6 free GPUs available—specifically the object-s44, goal-s43, and goal-s44 variants that were previously assigned to bjb1-32546. I need to verify that bjb2-28827 has the Pi05 checkpoint available and check whether those experiments are still running on bjb1-32546 before proceeding with the deployment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "f566c17f-da73-456a-b49c-90041fbefc2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DRe6Hsfk42TMmxvXfcUSs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 62684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 75_

需要确认 bjb1-32546 上的 PREPARING 实验是否还活着，以及 bjb2-28827 是否有 Pi05 checkpoint。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "ee21be1e-f0d9-4fe6-86bc-96619214361a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DRe6Hsfk42TMmxvXfcUSs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 62684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 76_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01H5ddBhZE6rNJtwxu4kzesx`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps -p 510334,510700,510990 -o pid,stat,cmd --no-headers",
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "a8872a51-1c31-4c69-b457-005dc440f154",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DRe6Hsfk42TMmxvXfcUSs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 62684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 77 · 2026-05-28T04:43:37.662Z_

<details><summary>↩ Tool result · `toolu_01H5ddBhZE6rNJtwxu4kzesx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"510334 Ss+  bash -c rm -f /tmp/agent-ml-exit/pi05-crm-always-on-goal-s43.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/pi05-crm-always-on-goal-s43.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --output_file logs/eval_goal_crm_always_on_pi05_k2_norm0.2_seed43.json\\\"'; } > ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log 2>&1\\n510700 Ss+  bash -c rm -f /tmp/agent-ml-exit/pi05-crm-always-on-goal-s44.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/pi05-crm-always-on-goal-s44.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 44 --n_rollouts 20 --output_file logs/eval_goal_crm_always_on_pi05_k2_norm0.2_seed44.json\\\"'; } > ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log 2>&1\\n510990 Ss+  bash -c rm -f /tmp/agent-ml-exit/pi05-crm-always-on-object-s44.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/pi05-crm-always-on-object-s44.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_crm_always_on_pi05_k2_norm0.2_seed44.json\\\"'; } > ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log 2>&1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "d6741e69-700f-4a57-835b-ca152570442f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"510334 Ss+  bash -c rm -f /tmp/agent-ml-exit/pi05-crm-always-on-goal-s43.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/pi05-crm-always-on-goal-s43.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --output_file logs/eval_goal_crm_always_on_pi05_k2_norm0.2_seed43.json\\\\\\\"'; } > ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log 2>&1\\\\n510700 Ss+  bash -c rm -f /tmp/agent-ml-exit/pi05-crm-always-on-goal-s44.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/pi05-crm-always-on-goal-s44.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 44 --n_rollouts 20 --output_file logs/eval_goal_crm_always_on_pi05_k2_norm0.2_seed44.json\\\\\\\"'; } > ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log 2>&1\\\\n510990 Ss+  bash -c rm -f /tmp/agent-ml-exit/pi05-crm-always-on-object-s44.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/pi05-crm-always-on-object-s44.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_crm_always_on_pi05_k2_norm0.2_seed44.json\\\\\\\"'; } > ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log 2>&1\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"510334 Ss+  bash -c rm -f /tmp/agent-ml-exit/pi05-crm-always-on-goal-s43.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/pi05-crm-always-on-goal-s43.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --output_file logs/eval_goal_crm_always_on_pi05_k2_norm0.2_seed43.json\\\"'; } > ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log 2>&1\\n510700 Ss+  bash -c rm -f /tmp/agent-ml-exit/pi05-crm-always-on-goal-s44.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/pi05-crm-always-on-goal-s44.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 44 --n_rollouts 20 --output_file logs/eval_goal_crm_always_on_pi05_k2_norm0.2_seed44.json\\\"'; } > ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log 2>&1\\n510990 Ss+  bash -c rm -f /tmp/agent-ml-exit/pi05-crm-always-on-object-s44.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/pi05-crm-always-on-object-s44.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_crm_always_on_pi05_k2_norm0.2_seed44.json\\\"'; } > ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log 2>&1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SZ4vHFyGY57RoMGGPyBAZJ`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt",
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "58460d3f-8d28-4271-b8b3-a0fc9c531318",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DRe6Hsfk42TMmxvXfcUSs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 62684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 79 · 2026-05-28T04:43:38.886Z_

<details><summary>↩ Tool result · `toolu_01SZ4vHFyGY57RoMGGPyBAZJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "7068d906-dd09-406f-9dd5-c841e7b1c262",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 80_

<details><summary>Logged reasoning block</summary>

```text
Important findings:

1. **bjb1-32546**: The Pi05 PREPARING experiments are STILL ALIVE:
   - pid 510334 (goal-s43): Running on **CUDA_VISIBLE_DEVICES=0** 
   - pid 510700 (goal-s44): Running on **CUDA_VISIBLE_DEVICES=1**
   - pid 510990 (object-s44): Running on **CUDA_VISIBLE_DEVICES=2**

   These are on cuda:0, cuda:1, cuda:2 — which matches the nvidia-smi showing 12612/12612/12693 MiB on those GPUs. 

2. **bjb2-28827**: Pi05 checkpoint exists at `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt` ✓

So the three active Pi05 experiments are occupying cuda:0/1/2 on bjb1-32546, leaving cuda:3/4 available for new deployments. The ghost processes we killed earlier were unrelated to these.

For bjb2-28827, I'm verifying that all Pi05 seeds across the different task types are accounted for—Object, Spatial, Goal, and Long variants are either done or actively preparing across the cluster. Since Pi05 is fully deployed, I should move forward with launching the SmolVLA tau-sweep experiments on bjb2-28827's cuda:4/5, and I'm checking what tau-sweep configurations still need to be run.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "788fc3ab-6d5c-4bfd-9817-b3a8aaad7a8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFEQNnYfid4sHYUWAWBd8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3355,
      "cache_read_input_tokens": 63797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3355
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

_source line 81_

bjb1-32546 上的 Pi05 goal-s43/s44 和 object-s44 仍在 cuda:0/1/2 正常运行。所有 Pi05 seed 已铺开。

bjb2-28827 将部署 SmolVLA 补充实验。查缺口。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "20cc5735-08c4-49eb-9ab0-f89fc3492ec9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFEQNnYfid4sHYUWAWBd8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3355,
      "cache_read_input_tokens": 63797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3355
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

_source line 82_

<details open><summary>🔧 Tool call — Bash · `toolu_01L16UYvcg9MTMGZ3mYxcnSx`</summary>

```json
{
  "command": "grep -E \"smolvla-tau[0-9]+-long\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | grep -oP \"smolvla-tau[0-9]+-long-\\S+\" | sort -u",
  "description": "List all SmolVLA tau-sweep long experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "97987e90-1926-4a8f-82ff-bef0f7bee119",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFEQNnYfid4sHYUWAWBd8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3355,
      "cache_read_input_tokens": 63797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3355
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

_source line 83 · 2026-05-28T04:44:02.968Z_

<details><summary>↩ Tool result · `toolu_01L16UYvcg9MTMGZ3mYxcnSx`</summary>

```text
smolvla-tau005-long-s42.log
smolvla-tau005-long-s42:
smolvla-tau010-long-s42.log
smolvla-tau010-long-s42:
smolvla-tau015-long-s42.log
smolvla-tau015-long-s42:
smolvla-tau015-long-s43.log
smolvla-tau015-long-s43:
smolvla-tau020-long-s42
smolvla-tau020-long-s42-r2.log
smolvla-tau020-long-s42-r2:
smolvla-tau020-long-s42.log
smolvla-tau020-long-s42:
smolvla-tau020-long-s43-r2.log
smolvla-tau020-long-s43-r2:
smolvla-tau020-long-s43:
smolvla-tau025-long-s42:
smolvla-tau025-long-s43.log
smolvla-tau025-long-s43:
smolvla-tau030-long-s42-r2.log
smolvla-tau030-long-s42-r2:
smolvla-tau030-long-s42.log
smolvla-tau030-long-s42:
smolvla-tau030-long-s43-r2.log
smolvla-tau030-long-s43-r2:
smolvla-tau030-long-s43:
smolvla-tau035-long-s42.log
smolvla-tau035-long-s42:
smolvla-tau035-long-s43:
smolvla-tau040-long-s42.log
smolvla-tau040-long-s42:
smolvla-tau045-long-s42.log
smolvla-tau045-long-s42:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "27e3c650-a78f-4383-a94c-10599b899d85",
  "tool_use_result": {
    "stdout": "smolvla-tau005-long-s42.log\nsmolvla-tau005-long-s42:\nsmolvla-tau010-long-s42.log\nsmolvla-tau010-long-s42:\nsmolvla-tau015-long-s42.log\nsmolvla-tau015-long-s42:\nsmolvla-tau015-long-s43.log\nsmolvla-tau015-long-s43:\nsmolvla-tau020-long-s42\nsmolvla-tau020-long-s42-r2.log\nsmolvla-tau020-long-s42-r2:\nsmolvla-tau020-long-s42.log\nsmolvla-tau020-long-s42:\nsmolvla-tau020-long-s43-r2.log\nsmolvla-tau020-long-s43-r2:\nsmolvla-tau020-long-s43:\nsmolvla-tau025-long-s42:\nsmolvla-tau025-long-s43.log\nsmolvla-tau025-long-s43:\nsmolvla-tau030-long-s42-r2.log\nsmolvla-tau030-long-s42-r2:\nsmolvla-tau030-long-s42.log\nsmolvla-tau030-long-s42:\nsmolvla-tau030-long-s43-r2.log\nsmolvla-tau030-long-s43-r2:\nsmolvla-tau030-long-s43:\nsmolvla-tau035-long-s42.log\nsmolvla-tau035-long-s42:\nsmolvla-tau035-long-s43:\nsmolvla-tau040-long-s42.log\nsmolvla-tau040-long-s42:\nsmolvla-tau045-long-s42.log\nsmolvla-tau045-long-s42:",
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

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_01FYAqqdCouJPu4h1NqjcxiJ`</summary>

```json
{
  "command": "grep -E \"(smolvla-tau|eval-.*tau)\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | grep -i \"PREPARING\\|RUNNING\" | head -20",
  "description": "Check any running/preparing tau-sweep experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "3960f0c3-b8d1-4ecb-b37b-f069ebc8cb8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFEQNnYfid4sHYUWAWBd8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3355,
      "cache_read_input_tokens": 63797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3355
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

_source line 85 · 2026-05-28T04:44:04.080Z_

<details><summary>↩ Tool result · `toolu_01FYAqqdCouJPu4h1NqjcxiJ`</summary>

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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "7d371555-c3c6-420e-acc5-b8293184edd3",
  "tool_use_result": {
    "stdout": "",
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

_source line 86_

<details><summary>Logged reasoning block</summary>

```text
No SmolVLA tau-sweep experiments are currently RUNNING or PREPARING. Let me check what gaps exist in the tau-sweep matrix.

Looking at the long-horizon tau-sweep:
- s42: tau005, tau010, tau015, tau020, tau025, tau030, tau035, tau040, tau045 — complete set
- s43: tau015, tau020, tau025, tau030, tau035 — missing tau005, tau010, tau040, tau045

For other benchmarks let me check what exists:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "f6a25d23-3ef3-453f-b45e-59a2ce521c37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTL63gL3pc4xhDNwbxW9vt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 67152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1477
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_01JFdkvmdGojS6a3EyZH4BEQ`</summary>

```json
{
  "command": "echo \"=== OBJECT ===\" && grep -oP \"smolvla-tau\\d+-object-s\\d+[^:]*:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | sort -u && echo \"=== SPATIAL ===\" && grep -oP \"smolvla-tau\\d+-spatial-s\\d+[^:]*:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | sort -u && echo \"=== GOAL ===\" && grep -oP \"smolvla-tau\\d+-goal-s\\d+[^:]*:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | sort -u && echo \"=== LONG ===\" && grep -oP \"smolvla-tau\\d+-long-s\\d+[^:]*:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | sort -u",
  "description": "Map all SmolVLA tau-sweep experiments across benchmarks and seeds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "fa99c751-54f5-4a38-a333-2a6c04f63e2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTL63gL3pc4xhDNwbxW9vt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 67152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1477
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

_source line 88 · 2026-05-28T04:44:13.036Z_

<details><summary>↩ Tool result · `toolu_01JFdkvmdGojS6a3EyZH4BEQ`</summary>

```text
=== OBJECT ===
smolvla-tau005-object-s42:
smolvla-tau010-object-s42:
smolvla-tau015-object-s42:
smolvla-tau015-object-s43-bjb1:
smolvla-tau015-object-s43:
smolvla-tau020-object-s42:
smolvla-tau025-object-s42-r2:
smolvla-tau025-object-s42-r3:
smolvla-tau025-object-s42:
smolvla-tau025-object-s43-bjb1:
smolvla-tau025-object-s43-r3:
smolvla-tau025-object-s43:
smolvla-tau030-object-s42:
smolvla-tau035-object-s42-r2:
smolvla-tau035-object-s42-r3:
smolvla-tau035-object-s42:
smolvla-tau035-object-s43-bjb1:
smolvla-tau035-object-s43-r3:
smolvla-tau035-object-s43:
smolvla-tau040-object-s42:
smolvla-tau045-object-s42:
=== SPATIAL ===
smolvla-tau015-spatial-s42-bjb1:
smolvla-tau015-spatial-s42-fix:
smolvla-tau015-spatial-s42:
smolvla-tau015-spatial-s43:
smolvla-tau025-spatial-s43:
smolvla-tau035-spatial-s42-bjb1:
smolvla-tau035-spatial-s43:
smolvla-tau045-spatial-s42:
=== GOAL ===
smolvla-tau015-goal-s42:
smolvla-tau015-goal-s43-bjb1:
smolvla-tau015-goal-s43:
smolvla-tau025-goal-s42:
smolvla-tau025-goal-s43-bjb1:
smolvla-tau025-goal-s43:
smolvla-tau035-goal-s42:
smolvla-tau035-goal-s43-bjb1:
smolvla-tau035-goal-s43:
=== LONG ===
smolvla-tau005-long-s42:
smolvla-tau010-long-s42:
smolvla-tau015-long-s42:
smolvla-tau015-long-s43:
smolvla-tau020-long-s42-r2:
smolvla-tau020-long-s42:
smolvla-tau020-long-s43-r2:
smolvla-tau020-long-s43:
smolvla-tau025-long-s42:
smolvla-tau025-long-s43:
smolvla-tau030-long-s42-r2:
smolvla-tau030-long-s42:
smolvla-tau030-long-s43-r2:
smolvla-tau030-long-s43:
smolvla-tau035-long-s42:
smolvla-tau035-long-s43:
smolvla-tau040-long-s42:
smolvla-tau045-long-s42:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "1d39dea1-0a64-495e-8fc2-63848700d98e",
  "tool_use_result": {
    "stdout": "=== OBJECT ===\nsmolvla-tau005-object-s42:\nsmolvla-tau010-object-s42:\nsmolvla-tau015-object-s42:\nsmolvla-tau015-object-s43-bjb1:\nsmolvla-tau015-object-s43:\nsmolvla-tau020-object-s42:\nsmolvla-tau025-object-s42-r2:\nsmolvla-tau025-object-s42-r3:\nsmolvla-tau025-object-s42:\nsmolvla-tau025-object-s43-bjb1:\nsmolvla-tau025-object-s43-r3:\nsmolvla-tau025-object-s43:\nsmolvla-tau030-object-s42:\nsmolvla-tau035-object-s42-r2:\nsmolvla-tau035-object-s42-r3:\nsmolvla-tau035-object-s42:\nsmolvla-tau035-object-s43-bjb1:\nsmolvla-tau035-object-s43-r3:\nsmolvla-tau035-object-s43:\nsmolvla-tau040-object-s42:\nsmolvla-tau045-object-s42:\n=== SPATIAL ===\nsmolvla-tau015-spatial-s42-bjb1:\nsmolvla-tau015-spatial-s42-fix:\nsmolvla-tau015-spatial-s42:\nsmolvla-tau015-spatial-s43:\nsmolvla-tau025-spatial-s43:\nsmolvla-tau035-spatial-s42-bjb1:\nsmolvla-tau035-spatial-s43:\nsmolvla-tau045-spatial-s42:\n=== GOAL ===\nsmolvla-tau015-goal-s42:\nsmolvla-tau015-goal-s43-bjb1:\nsmolvla-tau015-goal-s43:\nsmolvla-tau025-goal-s42:\nsmolvla-tau025-goal-s43-bjb1:\nsmolvla-tau025-goal-s43:\nsmolvla-tau035-goal-s42:\nsmolvla-tau035-goal-s43-bjb1:\nsmolvla-tau035-goal-s43:\n=== LONG ===\nsmolvla-tau005-long-s42:\nsmolvla-tau010-long-s42:\nsmolvla-tau015-long-s42:\nsmolvla-tau015-long-s43:\nsmolvla-tau020-long-s42-r2:\nsmolvla-tau020-long-s42:\nsmolvla-tau020-long-s43-r2:\nsmolvla-tau020-long-s43:\nsmolvla-tau025-long-s42:\nsmolvla-tau025-long-s43:\nsmolvla-tau030-long-s42-r2:\nsmolvla-tau030-long-s42:\nsmolvla-tau030-long-s43-r2:\nsmolvla-tau030-long-s43:\nsmolvla-tau035-long-s42:\nsmolvla-tau035-long-s43:\nsmolvla-tau040-long-s42:\nsmolvla-tau045-long-s42:",
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

_source line 89_

<details><summary>Logged reasoning block</summary>

```text
Now I can see the gaps. The user mentioned "tau020-long 或其他缺口".

Looking at the tau-sweep data:

**Long benchmark gaps:**
- s42: tau005-045 (all 9 values) — fairly complete
- s43: tau015, tau020, tau025, tau030, tau035 — missing tau005, tau010, tau040, tau045

**Spatial benchmark is very sparse:**
- s42: tau015, tau035, tau045 (only 3!)
- s43: tau015, tau025, tau035


- **Goal benchmark:** s42 and s43 both have tau015, tau025, tau035
- **Object benchmark:** s42 has the full range while s43 only has tau015, tau025, tau035

For bjb2-28827 cuda:4/5, the spatial and goal benchmarks are the bottlenecks with fewer tau values covered. The user specifically called out tau020-long, so I should prioritize filling that gap along with expanding spatial coverage to match what's available for object and long benchmarks.

Since all Pi05 seeds are already deployed, I need to identify which SmolVLA tau-sweep experiments would be most valuable. The user wants me to fill in the missing tau values—I should look for what's not yet covered and pick the experiments that would give the most complete tau-sweep analysis across all benchmark types.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "1cacaca4-ab40-42d0-a6d0-8b94719aa962",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B34MnkQWjrsohwLPe41qX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1345,
      "cache_read_input_tokens": 68629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1345
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

所有 Pi05 seed 已铺开。SmolVLA tau-sweep 中 spatial 和 goal 缺口最大。确认 bjb2-28827 环境。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "6225fca2-9874-45eb-83ea-683a434a78c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B34MnkQWjrsohwLPe41qX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1345,
      "cache_read_input_tokens": 68629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1345
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01A8kmYvQyWFkqnhwAj1Cvt9`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "f44e13c4-1f6a-4a59-9f35-8e24930181a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B34MnkQWjrsohwLPe41qX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1345,
      "cache_read_input_tokens": 68629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1345
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 92 · 2026-05-28T04:44:34.271Z_

<details><summary>↩ Tool result · `toolu_01A8kmYvQyWFkqnhwAj1Cvt9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "08afd5ca-cebb-4dd5-9f80-e5e67d734cae",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01WqrFXdnsBNxH5dxeuq65a7`</summary>

```json
{
  "command": "grep -A 20 \"smolvla-tau025-spatial-s43:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -25",
  "description": "Get SmolVLA tau-sweep spatial reference command"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "58972ac5-27c7-4c10-9f2f-0cd263e87288",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B34MnkQWjrsohwLPe41qX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1345,
      "cache_read_input_tokens": 68629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1345
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 94 · 2026-05-28T04:44:35.063Z_

<details><summary>↩ Tool result · `toolu_01WqrFXdnsBNxH5dxeuq65a7`</summary>

```text
  smolvla-tau025-spatial-s43:
    status: DONE
    retry_count: 0
    created_at: '2026-05-27T00:55:08.702Z'
    updated_at: '2026-05-27T02:44:08.075Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
        --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm
        0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt
        --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_spatial_adaptive_tau025_s43.json"
      server: westd-49937
      gpu:
      - cuda:1
      pid: '782029'
      log_path: /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_tau025_s43.json
      submitted_at: '2026-05-27T00:55:03.849Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      data_path: LIBERO-Spatial
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "90fec216-cea7-4e78-a685-73cd246b0227",
  "tool_use_result": {
    "stdout": "  smolvla-tau025-spatial-s43:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-27T00:55:08.702Z'\n    updated_at: '2026-05-27T02:44:08.075Z'\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py\n        --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm\n        0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\n        --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_spatial_adaptive_tau025_s43.json\"\n      server: westd-49937\n      gpu:\n      - cuda:1\n      pid: '782029'\n      log_path: /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_tau025_s43.json\n      submitted_at: '2026-05-27T00:55:03.849Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      data_path: LIBERO-Spatial",
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

_source line 95_

<details><summary>Logged reasoning block</summary>

```text
SmolVLA checkpoint exists on bjb2-28827. I have the reference command format.

Now let me choose 2 SmolVLA tau-sweep experiments for bjb2-28827 cuda:4/5. The biggest gaps are:

**Spatial** (only has tau015, tau035, tau045 for s42; tau015, tau025, tau035 for s43):
- Missing for s42: tau005, tau010, tau020, tau025, tau030
- Missing for s43: tau005, tau010, tau020, tau030, tau040, tau045


**Goal** (only has tau015, tau025, tau035):
- Missing for s42: tau005, tau010, tau020, tau030, tau040, tau045
- Missing for s43: same
**Long** s43 missing: tau005, tau010, tau040, tau045

For the paper, I need consistent tau-sweep coverage across all benchmarks. Looking at what's actually available, I'm trying to identify which experiments would fill the biggest holes. Let me verify what's already been completed before deciding on the next two runs. I'm noticing that tau025 is missing from the spatial s42 experiments, which is a critical gap since that's often the optimal threshold value. For spatial s43, I have better coverage with tau015, tau025, and tau035. I should prioritize filling the tau025-spatial-s42 slot on one GPU, and then decide between tau020-spatial-s42 or exploring goal suite gaps for the second GPU.

Now I'm constructing the evaluation commands that will run the conformal refinement model with specific threshold and benchmark parameters.

For the tau025 variant, I need to adjust the seed to 42 and update the output filename to reflect those changes. For tau020, I'll modify the conformal threshold to 0.20 and adjust the output path accordingly.

I'm ready to submit all four jobs in parallel across the two machines — the random selection and K-sweep experiments on bjb1, and the two spatial refinement variants on bjb2.

Looking back at the random-selection command, I notice it didn't explicitly specify the model, but since the user wants SmolVLA specifically, I should add `--model smolvla` to be explicit. The template also uses `--n_rollouts 20` rather than the previous 10, so I'll follow that specification.

Now I'm ready to submit all four experiments using the submit_training_job function, and I can register artifacts later if needed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "3c214950-4e4c-452b-9391-df18dbd7dbfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rZU6YMGonSiirZ41QQ7mw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1486,
      "cache_read_input_tokens": 69974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1486
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 96_

SmolVLA checkpoint 存在于 bjb2-28827。Spatial s42 缺 tau025/tau020，这是最关键的缺口。

现在提交全部 4 个实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "5ec19509-3b20-41e5-87fa-e90d2d0ae92c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rZU6YMGonSiirZ41QQ7mw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1486,
      "cache_read_input_tokens": 69974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1486
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 97_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job · `toolu_01GcKqzJg4GmS7nzCrYQf3nT`</summary>

```json
{
  "server": "bjb1-32546",
  "gpu_ids": [
    "cuda:3"
  ],
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20 --output_file logs/eval_random_selection_object_seed43_v2.json\"",
  "exp_id": "eval-random-selection-object-seed43-v2",
  "account": "root",
  "project": "acr-vla-conformal-refinement",
  "plan_id": "plan_600"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "20e2c207-7cab-4479-95d6-382cfe6e4b47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rZU6YMGonSiirZ41QQ7mw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1486,
      "cache_read_input_tokens": 69974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1486
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job · `toolu_0113mjpMDmunTQfFScoYPXBS`</summary>

```json
{
  "server": "bjb1-32546",
  "gpu_ids": [
    "cuda:4"
  ],
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_obs_only_k20_norm02_s44.json\"",
  "exp_id": "eval-ksweep-k20-obs-object-s44",
  "account": "root",
  "project": "acr-vla-conformal-refinement",
  "plan_id": "plan_601"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "a1040b94-ca00-4b80-a347-66c41da38a45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rZU6YMGonSiirZ41QQ7mw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1486,
      "cache_read_input_tokens": 69974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1486
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 99_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job · `toolu_01Wdk6u2eU7a5Yq9UdKQZESp`</summary>

```json
{
  "server": "bjb2-28827",
  "gpu_ids": [
    "cuda:4"
  ],
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_adaptive_tau025_s42.json\"",
  "exp_id": "smolvla-tau025-spatial-s42",
  "account": "root",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "f365f8de-b150-4542-b2cd-a1ecdd1cd82e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rZU6YMGonSiirZ41QQ7mw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1486,
      "cache_read_input_tokens": 69974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1486
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 100_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job · `toolu_01HiH9SMScorSvA7ocXJ2ipX`</summary>

```json
{
  "server": "bjb2-28827",
  "gpu_ids": [
    "cuda:5"
  ],
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_adaptive_tau020_s42.json\"",
  "exp_id": "smolvla-tau020-spatial-s42",
  "account": "root",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "fe96f5a9-884d-47d4-be6d-456bee3ea52a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rZU6YMGonSiirZ41QQ7mw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1486,
      "cache_read_input_tokens": 69974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1486
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 101 · 2026-05-28T04:45:18.596Z_

<details><summary>↩ Tool result · `toolu_01GcKqzJg4GmS7nzCrYQf3nT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"pid\": \"550552\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\", \"gpu_ids\": [\"cuda:3\"], \"server\": \"bjb1-32546\", \"account\": \"root\", \"cuda_visible_devices\": \"3\", \"backend\": \"tmux\", \"tmux_session\": \"eval-random-selection-object-seed43-v2\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.69}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "8d820e82-05c4-450e-bc75-3c596683ed54",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"pid\\\": \\\"550552\\\", \\\"log_file\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\\\", \\\"gpu_ids\\\": [\\\"cuda:3\\\"], \\\"server\\\": \\\"bjb1-32546\\\", \\\"account\\\": \\\"root\\\", \\\"cuda_visible_devices\\\": \\\"3\\\", \\\"backend\\\": \\\"tmux\\\", \\\"tmux_session\\\": \\\"eval-random-selection-object-seed43-v2\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.69}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"pid\": \"550552\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\", \"gpu_ids\": [\"cuda:3\"], \"server\": \"bjb1-32546\", \"account\": \"root\", \"cuda_visible_devices\": \"3\", \"backend\": \"tmux\", \"tmux_session\": \"eval-random-selection-object-seed43-v2\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.69}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-28T04:45:28.265Z_

<details><summary>↩ Tool result · `toolu_0113mjpMDmunTQfFScoYPXBS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"pid\": \"550832\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\", \"gpu_ids\": [\"cuda:4\"], \"server\": \"bjb1-32546\", \"account\": \"root\", \"cuda_visible_devices\": \"4\", \"backend\": \"tmux\", \"tmux_session\": \"eval-ksweep-k20-obs-object-s44\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.66}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "6f87b6d8-a65b-4018-999b-cfb82731bf62",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"pid\\\": \\\"550832\\\", \\\"log_file\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:4\\\"], \\\"server\\\": \\\"bjb1-32546\\\", \\\"account\\\": \\\"root\\\", \\\"cuda_visible_devices\\\": \\\"4\\\", \\\"backend\\\": \\\"tmux\\\", \\\"tmux_session\\\": \\\"eval-ksweep-k20-obs-object-s44\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.66}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"pid\": \"550832\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\", \"gpu_ids\": [\"cuda:4\"], \"server\": \"bjb1-32546\", \"account\": \"root\", \"cuda_visible_devices\": \"4\", \"backend\": \"tmux\", \"tmux_session\": \"eval-ksweep-k20-obs-object-s44\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.66}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-28T04:45:36.892Z_

<details><summary>↩ Tool result · `toolu_01Wdk6u2eU7a5Yq9UdKQZESp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"pid\": \"112960\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau025-spatial-s42.log\", \"gpu_ids\": [\"cuda:4\"], \"server\": \"bjb2-28827\", \"account\": \"root\", \"cuda_visible_devices\": \"4\", \"backend\": \"tmux\", \"tmux_session\": \"smolvla-tau025-spatial-s42\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.61}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "7e55b41f-a92e-4ddf-887c-01609482003a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"pid\\\": \\\"112960\\\", \\\"log_file\\\": \\\"~/runs/acr-vla-conformal-refinement/smolvla-tau025-spatial-s42.log\\\", \\\"gpu_ids\\\": [\\\"cuda:4\\\"], \\\"server\\\": \\\"bjb2-28827\\\", \\\"account\\\": \\\"root\\\", \\\"cuda_visible_devices\\\": \\\"4\\\", \\\"backend\\\": \\\"tmux\\\", \\\"tmux_session\\\": \\\"smolvla-tau025-spatial-s42\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.61}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"pid\": \"112960\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau025-spatial-s42.log\", \"gpu_ids\": [\"cuda:4\"], \"server\": \"bjb2-28827\", \"account\": \"root\", \"cuda_visible_devices\": \"4\", \"backend\": \"tmux\", \"tmux_session\": \"smolvla-tau025-spatial-s42\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.61}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-28T04:45:45.411Z_

<details><summary>↩ Tool result · `toolu_01HiH9SMScorSvA7ocXJ2ipX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"pid\": \"113242\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau020-spatial-s42.log\", \"gpu_ids\": [\"cuda:5\"], \"server\": \"bjb2-28827\", \"account\": \"root\", \"cuda_visible_devices\": \"5\", \"backend\": \"tmux\", \"tmux_session\": \"smolvla-tau020-spatial-s42\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "940bca07-da3c-41b4-a902-a4cf1fc3010c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"pid\\\": \\\"113242\\\", \\\"log_file\\\": \\\"~/runs/acr-vla-conformal-refinement/smolvla-tau020-spatial-s42.log\\\", \\\"gpu_ids\\\": [\\\"cuda:5\\\"], \\\"server\\\": \\\"bjb2-28827\\\", \\\"account\\\": \\\"root\\\", \\\"cuda_visible_devices\\\": \\\"5\\\", \\\"backend\\\": \\\"tmux\\\", \\\"tmux_session\\\": \\\"smolvla-tau020-spatial-s42\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.5}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"pid\": \"113242\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau020-spatial-s42.log\", \"gpu_ids\": [\"cuda:5\"], \"server\": \"bjb2-28827\", \"account\": \"root\", \"cuda_visible_devices\": \"5\", \"backend\": \"tmux\", \"tmux_session\": \"smolvla-tau020-spatial-s42\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.5}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 105_

<details><summary>Logged reasoning block</summary>

```text
All 4 experiments submitted successfully. Now let me load update_registry to update the hypotheses for the bjb2 experiments.

Actually, submit_training_job should have already registered them. Let me also update the registry with hypotheses for the bjb2 experiments. Let me load the update_registry tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "5b6f16aa-274c-4065-9cf9-4c4075c65db6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3eyMDeaBTeUzvvaH8Btvq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3706,
      "cache_read_input_tokens": 71460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3706
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

全部 4 个实验提交成功。更新 registry 补充 hypothesis。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "272d5809-bcb8-4db2-b023-b9d6d523a41c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3eyMDeaBTeUzvvaH8Btvq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3706,
      "cache_read_input_tokens": 71460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3706
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Vq5p5ttQTQExGp2k75AgEg`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "8d683cb3-901d-4e76-bd1d-7296862fae07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3eyMDeaBTeUzvvaH8Btvq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3706,
      "cache_read_input_tokens": 71460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3706
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 108 · 2026-05-28T04:45:52.464Z_

<details><summary>↩ Tool result · `toolu_01Vq5p5ttQTQExGp2k75AgEg`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
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
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "2bea867b-a6fe-4fe7-956e-7ba3cf285089",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 27
  }
}
```

</details>

---

### Tool call

_source line 109_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01SeZyaUfvfz2MejuwPtcApj`</summary>

```json
{
  "exp_id": "eval-random-selection-object-seed43-v2",
  "field": "hypothesis",
  "value": "Random selection baseline (K=10, uniform random pick) on Object seed43. Ablation isolating conformal ranking contribution — if random pick ≈ VLA-only, conformal scoring is the key ingredient.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "85bba67f-6873-4bb6-8f5f-6af1fcc4edce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxrMZd6yTWhm5kD3Cdrybe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 75166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 698
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

### Tool call

_source line 110_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Y4r1agMTwunE8YSCUKwbXw`</summary>

```json
{
  "exp_id": "eval-random-selection-object-seed43-v2",
  "field": "parent",
  "value": "eval-random-selection-object-seed44",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "09d38fc6-4827-45e4-a5e5-93a5d761916d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxrMZd6yTWhm5kD3Cdrybe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 75166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 698
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

### Tool call

_source line 111_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_012YEhhs482GcgRQ9AhGT4gD`</summary>

```json
{
  "exp_id": "eval-ksweep-k20-obs-object-s44",
  "field": "hypothesis",
  "value": "K=20 obs_only CRM on Object seed44. Third seed for K-sweep analysis justifying K=10 design choice.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "6ddc558b-7ce1-4c72-b2bd-894a6aef8b45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxrMZd6yTWhm5kD3Cdrybe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 75166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 698
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

### Tool call

_source line 112_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01WnyEM1jf6sqZwPCcudnVZu`</summary>

```json
{
  "exp_id": "eval-ksweep-k20-obs-object-s44",
  "field": "parent",
  "value": "eval-ksweep-k20-obs-object-s43",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "61a2dd05-e0d6-4afd-8074-30459fed6cab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxrMZd6yTWhm5kD3Cdrybe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 75166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 698
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

_source line 113 · 2026-05-28T04:46:03.942Z_

<details><summary>↩ Tool result · `toolu_01SeZyaUfvfz2MejuwPtcApj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-object-seed43-v2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:16.507Z\", \"updated_at\": \"2026-05-28T04:46:01.915Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20 --output_file logs/eval_random_selection_object_seed43_v2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"550552\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\", \"submitted_at\": \"2026-05-28T04:45:13.541Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Random selection baseline (K=10, uniform random pick) on Object seed43. Ablation isolating conformal ranking contribution — if random pick ≈ VLA-only, conformal scoring is the key ingredient.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.1064}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "fc986288-5c9d-4414-aadc-26812235fc62",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-random-selection-object-seed43-v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T04:45:16.507Z\\\", \\\"updated_at\\\": \\\"2026-05-28T04:46:01.915Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20 --output_file logs/eval_random_selection_object_seed43_v2.json\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"550552\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:13.541Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"hypothesis\\\": \\\"Random selection baseline (K=10, uniform random pick) on Object seed43. Ablation isolating conformal ranking contribution — if random pick ≈ VLA-only, conformal scoring is the key ingredient.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.1064}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-object-seed43-v2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:16.507Z\", \"updated_at\": \"2026-05-28T04:46:01.915Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20 --output_file logs/eval_random_selection_object_seed43_v2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"550552\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\", \"submitted_at\": \"2026-05-28T04:45:13.541Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Random selection baseline (K=10, uniform random pick) on Object seed43. Ablation isolating conformal ranking contribution — if random pick ≈ VLA-only, conformal scoring is the key ingredient.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.1064}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 114_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01HYosLV6qTBRmdwFpYKM7nf`</summary>

```json
{
  "exp_id": "smolvla-tau025-spatial-s42",
  "field": "hypothesis",
  "value": "SmolVLA adaptive conformal CRM τ=0.25 on Spatial s42. Fills critical tau-sweep gap — spatial s42 missing tau025 data point for sweep curve.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "256a7934-d3d7-4f3b-ad55-728ca20714f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxrMZd6yTWhm5kD3Cdrybe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 75166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 698
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

### Tool call

_source line 115_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01DYo9CWUqQ7Xq8WBoMMwn5i`</summary>

```json
{
  "exp_id": "smolvla-tau020-spatial-s42",
  "field": "hypothesis",
  "value": "SmolVLA adaptive conformal CRM τ=0.20 on Spatial s42. Second spatial tau-sweep gap fill for denser sweep curve around optimal range.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "9c1470a0-5b36-4635-884d-4e5336e4fcfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxrMZd6yTWhm5kD3Cdrybe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 75166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 698
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

_source line 116 · 2026-05-28T04:46:09.132Z_

<details><summary>↩ Tool result · `toolu_01Y4r1agMTwunE8YSCUKwbXw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-object-seed43-v2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:16.507Z\", \"updated_at\": \"2026-05-28T04:46:07.074Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20 --output_file logs/eval_random_selection_object_seed43_v2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"550552\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\", \"submitted_at\": \"2026-05-28T04:45:13.541Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Random selection baseline (K=10, uniform random pick) on Object seed43. Ablation isolating conformal ranking contribution — if random pick ≈ VLA-only, conformal scoring is the key ingredient.\", \"parent\": \"eval-random-selection-object-seed44\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.1757}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "724bbc14-c778-4e11-a709-146bcf3bb4ae",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-random-selection-object-seed43-v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T04:45:16.507Z\\\", \\\"updated_at\\\": \\\"2026-05-28T04:46:07.074Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20 --output_file logs/eval_random_selection_object_seed43_v2.json\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"550552\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:13.541Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"hypothesis\\\": \\\"Random selection baseline (K=10, uniform random pick) on Object seed43. Ablation isolating conformal ranking contribution — if random pick ≈ VLA-only, conformal scoring is the key ingredient.\\\", \\\"parent\\\": \\\"eval-random-selection-object-seed44\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.1757}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-object-seed43-v2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:16.507Z\", \"updated_at\": \"2026-05-28T04:46:07.074Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20 --output_file logs/eval_random_selection_object_seed43_v2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"550552\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\", \"submitted_at\": \"2026-05-28T04:45:13.541Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Random selection baseline (K=10, uniform random pick) on Object seed43. Ablation isolating conformal ranking contribution — if random pick ≈ VLA-only, conformal scoring is the key ingredient.\", \"parent\": \"eval-random-selection-object-seed44\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.1757}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-28T04:46:14.126Z_

<details><summary>↩ Tool result · `toolu_012YEhhs482GcgRQ9AhGT4gD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-ksweep-k20-obs-object-s44\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:26.027Z\", \"updated_at\": \"2026-05-28T04:46:12.120Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_obs_only_k20_norm02_s44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"550832\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\", \"submitted_at\": \"2026-05-28T04:45:22.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"K=20 obs_only CRM on Object seed44. Third seed for K-sweep analysis justifying K=10 design choice.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9777}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "33472896-23d1-4f61-9118-5ef41cadbc83",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-ksweep-k20-obs-object-s44\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T04:45:26.027Z\\\", \\\"updated_at\\\": \\\"2026-05-28T04:46:12.120Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_obs_only_k20_norm02_s44.json\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"550832\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:22.258Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"hypothesis\\\": \\\"K=20 obs_only CRM on Object seed44. Third seed for K-sweep analysis justifying K=10 design choice.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.9777}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-ksweep-k20-obs-object-s44\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:26.027Z\", \"updated_at\": \"2026-05-28T04:46:12.120Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_obs_only_k20_norm02_s44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"550832\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\", \"submitted_at\": \"2026-05-28T04:45:22.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"K=20 obs_only CRM on Object seed44. Third seed for K-sweep analysis justifying K=10 design choice.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9777}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-28T04:46:19.060Z_

<details><summary>↩ Tool result · `toolu_01WnyEM1jf6sqZwPCcudnVZu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-ksweep-k20-obs-object-s44\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:26.027Z\", \"updated_at\": \"2026-05-28T04:46:17.067Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_obs_only_k20_norm02_s44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"550832\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\", \"submitted_at\": \"2026-05-28T04:45:22.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"K=20 obs_only CRM on Object seed44. Third seed for K-sweep analysis justifying K=10 design choice.\", \"parent\": \"eval-ksweep-k20-obs-object-s43\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9208}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "c974e332-b931-4448-9fb7-08b8b22a9a04",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-ksweep-k20-obs-object-s44\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T04:45:26.027Z\\\", \\\"updated_at\\\": \\\"2026-05-28T04:46:17.067Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_obs_only_k20_norm02_s44.json\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"550832\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:22.258Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"hypothesis\\\": \\\"K=20 obs_only CRM on Object seed44. Third seed for K-sweep analysis justifying K=10 design choice.\\\", \\\"parent\\\": \\\"eval-ksweep-k20-obs-object-s43\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.9208}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-ksweep-k20-obs-object-s44\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:26.027Z\", \"updated_at\": \"2026-05-28T04:46:17.067Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_obs_only_k20_norm02_s44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"550832\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\", \"submitted_at\": \"2026-05-28T04:45:22.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"K=20 obs_only CRM on Object seed44. Third seed for K-sweep analysis justifying K=10 design choice.\", \"parent\": \"eval-ksweep-k20-obs-object-s43\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9208}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-28T04:46:26.450Z_

<details><summary>↩ Tool result · `toolu_01HYosLV6qTBRmdwFpYKM7nf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau025-spatial-s42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:34.861Z\", \"updated_at\": \"2026-05-28T04:46:22.570Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_adaptive_tau025_s42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"112960\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau025-spatial-s42.log\", \"submitted_at\": \"2026-05-28T04:45:31.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"SmolVLA adaptive conformal CRM τ=0.25 on Spatial s42. Fills critical tau-sweep gap — spatial s42 missing tau025 data point for sweep curve.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.3736}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "a5d2d96c-31a6-434d-b8d1-9f462b7953a2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-tau025-spatial-s42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T04:45:34.861Z\\\", \\\"updated_at\\\": \\\"2026-05-28T04:46:22.570Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_adaptive_tau025_s42.json\\\\\\\"\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"112960\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/smolvla-tau025-spatial-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:31.846Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"hypothesis\\\": \\\"SmolVLA adaptive conformal CRM τ=0.25 on Spatial s42. Fills critical tau-sweep gap — spatial s42 missing tau025 data point for sweep curve.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 7.3736}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau025-spatial-s42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:34.861Z\", \"updated_at\": \"2026-05-28T04:46:22.570Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_adaptive_tau025_s42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"112960\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau025-spatial-s42.log\", \"submitted_at\": \"2026-05-28T04:45:31.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"SmolVLA adaptive conformal CRM τ=0.25 on Spatial s42. Fills critical tau-sweep gap — spatial s42 missing tau025 data point for sweep curve.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.3736}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-28T04:46:34.855Z_

<details><summary>↩ Tool result · `toolu_01DYo9CWUqQ7Xq8WBoMMwn5i`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau020-spatial-s42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:43.384Z\", \"updated_at\": \"2026-05-28T04:46:31.435Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_adaptive_tau020_s42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"113242\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau020-spatial-s42.log\", \"submitted_at\": \"2026-05-28T04:45:40.430Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"SmolVLA adaptive conformal CRM τ=0.20 on Spatial s42. Second spatial tau-sweep gap fill for denser sweep curve around optimal range.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.3906}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "d5ddb96c-a610-45a3-9072-35fbdb6e647e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-tau020-spatial-s42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T04:45:43.384Z\\\", \\\"updated_at\\\": \\\"2026-05-28T04:46:31.435Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_adaptive_tau020_s42.json\\\\\\\"\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"113242\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/smolvla-tau020-spatial-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:40.430Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"hypothesis\\\": \\\"SmolVLA adaptive conformal CRM τ=0.20 on Spatial s42. Second spatial tau-sweep gap fill for denser sweep curve around optimal range.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.3906}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau020-spatial-s42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:43.384Z\", \"updated_at\": \"2026-05-28T04:46:31.435Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_adaptive_tau020_s42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"113242\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau020-spatial-s42.log\", \"submitted_at\": \"2026-05-28T04:45:40.430Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"SmolVLA adaptive conformal CRM τ=0.20 on Spatial s42. Second spatial tau-sweep gap fill for denser sweep curve around optimal range.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.3906}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 121_

全部完成。

## 1. Kill 结果

| 服务器 | 操作 | GPU 释放确认 |
|--------|------|-------------|
| bjb2-28827 | kill -9 95782 97560 | cuda:0-5 全部 0 MiB ✓ |
| bjb1-32546 | kill -9 515230 515586 | cuda:3 = 2 MiB, cuda:4 = 2 MiB ✓ (cuda:0/1/2 有 Pi05 goal-s43/s44, object-s44 正常运行) |

## 2. bjb1-32546 部署

| GPU | exp_id | PID | 说明 |
|-----|--------|-----|------|
| cuda:3 | `eval-random-selection-object-seed43-v2` | 550552 | Random selection K=10, n_rollouts=20, plan_600 |
| cuda:4 | `eval-ksweep-k20-obs-object-s44` | 550832 | K=20 obs_only CRM, n_rollouts=20, plan_601 |

## 3. bjb2-28827 部署

所有 Pi05 CRM always-on seed 已铺开（object-s44/goal-s43/goal-s44 在 bjb1-32546 cuda:0/1/2；spatial-s43/s44/long-s43/s44 在 bjb1-18228；long-s42 在 cqa1）。改为填补 SmolVLA tau-sweep spatial s42 缺口：

| GPU | exp_id | PID | 说明 |
|-----|--------|-----|------|
| cuda:4 | `smolvla-tau025-spatial-s42` | 112960 | τ=0.25 spatial s42, 最关键缺口 |
| cuda:5 | `smolvla-tau020-spatial-s42` | 113242 | τ=0.20 spatial s42, 密化 sweep 曲线 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "uuid": "1b1dbac4-85d7-4847-89eb-d6d74bfb882c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DGsLNScjC4Tz6rBq3pk5U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4047,
      "cache_read_input_tokens": 75864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4047
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

_source line 122_

全部完成。

## 1. Kill 结果

| 服务器 | 操作 | GPU 释放确认 |
|--------|------|-------------|
| bjb2-28827 | kill -9 95782 97560 | cuda:0-5 全部 0 MiB ✓ |
| bjb1-32546 | kill -9 515230 515586 | cuda:3 = 2 MiB, cuda:4 = 2 MiB ✓ (cuda:0/1/2 有 Pi05 goal-s43/s44, object-s44 正常运行) |

## 2. bjb1-32546 部署

| GPU | exp_id | PID | 说明 |
|-----|--------|-----|------|
| cuda:3 | `eval-random-selection-object-seed43-v2` | 550552 | Random selection K=10, n_rollouts=20, plan_600 |
| cuda:4 | `eval-ksweep-k20-obs-object-s44` | 550832 | K=20 obs_only CRM, n_rollouts=20, plan_601 |

## 3. bjb2-28827 部署

所有 Pi05 CRM always-on seed 已铺开（object-s44/goal-s43/goal-s44 在 bjb1-32546 cuda:0/1/2；spatial-s43/s44/long-s43/s44 在 bjb1-18228；long-s42 在 cqa1）。改为填补 SmolVLA tau-sweep spatial s42 缺口：

| GPU | exp_id | PID | 说明 |
|-----|--------|-----|------|
| cuda:4 | `smolvla-tau025-spatial-s42` | 112960 | τ=0.25 spatial s42, 最关键缺口 |
| cuda:5 | `smolvla-tau020-spatial-s42` | 113242 | τ=0.20 spatial s42, 密化 sweep 曲线 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 392814,
  "duration_api_ms": 307476,
  "num_turns": 44,
  "stop_reason": "end_turn",
  "session_id": "4fe136af-402a-4a92-a7c2-4bd6e773f3d4",
  "total_cost_usd": 1.388454,
  "usage": {
    "input_tokens": 28,
    "cache_creation_input_tokens": 68460,
    "cache_read_input_tokens": 1181622,
    "output_tokens": 14693,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 68460,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 548,
        "cache_read_input_tokens": 75864,
        "cache_creation_input_tokens": 4047,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4047
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2228,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002303,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 28,
      "outputTokens": 14693,
      "cacheReadInputTokens": 1181622,
      "cacheCreationInputTokens": 68460,
      "webSearchRequests": 0,
      "costUSD": 1.3861510000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8d1093bc-78a7-4949-91e0-0bd5d7756bef"
}
```

</details>

---
