# deploy bjb1 32546 backfill urgent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-backfill-urgent_20260528T082124.log`
- **Structured JSON:** [`e9da913dee0ee9a5acf8.json`](../../sessions/e9/e9da913dee0ee9a5acf8.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
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
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
    "mcp__agent-ml-research__submit_training_job"
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
  "uuid": "c522eef8-c357-4585-8651-55a80da94cac",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779974400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "85664ad8-69f8-4578-b63e-1a1b1d636ee1",
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this down:

1. First, I need to load the MCP tools for SSH and registry operations
2. Check GPU status on bjb1-32546
3. Check registry for existing experiments
4. Deploy 6 experiments

Let me start by loading the necessary tools.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "2d2c05b8-fd94-4d4f-b632-2d586ff7ec06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxNt4PVPxVAt9g4J7oDr3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12729,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12729
      },
      "output_tokens": 30,
      "service_tier": "standard",
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

先加载工具并检查 GPU 状态和 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "3f609288-b67c-499d-8018-0f0fdc417488",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxNt4PVPxVAt9g4J7oDr3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12729,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12729
      },
      "output_tokens": 30,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WJ1eNxq5CPwts5wbHrqtBt`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__detect_image",
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
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "97e41246-6b87-496b-a94d-b8dd5b1fde29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxNt4PVPxVAt9g4J7oDr3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12729,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12729
      },
      "output_tokens": 30,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-28T08:21:39.954Z_

<details><summary>↩ Tool result · `toolu_01WJ1eNxq5CPwts5wbHrqtBt`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "5736f8a1-e5c9-497d-906b-c2dc82224a8c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me check GPU status on bjb1-32546 and read the registry for the experiment IDs in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "04da6662-f342-4b7b-9a4a-1d189bc6e085",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ez9qeXvTypBXcybNWo8Rzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2089,
      "cache_read_input_tokens": 24574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2089
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

### Assistant

_source line 9_

并行检查 GPU 状态、tmux 残留、文件存在性和 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "1a995ba8-84f6-4735-9a88-a540b5814f5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ez9qeXvTypBXcybNWo8Rzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2089,
      "cache_read_input_tokens": 24574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2089
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01V7BmM4AZx32RUQzAehVDYE`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv,noheader",
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
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "9c1619a6-b1bc-457e-99f6-315ca5b50362",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ez9qeXvTypBXcybNWo8Rzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2089,
      "cache_read_input_tokens": 24574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2089
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

_source line 11 · 2026-05-28T08:21:47.075Z_

<details><summary>↩ Tool result · `toolu_01V7BmM4AZx32RUQzAehVDYE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 1 MiB, 0 %\\n1, 1 MiB, 0 %\\n2, 1 MiB, 0 %\\n3, 1 MiB, 0 %\\n4, 1 MiB, 0 %\\n5, 1 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.29}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "480e1355-bffe-44e1-8a68-e8ac1a87c0ea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 1 MiB, 0 %\\\\n1, 1 MiB, 0 %\\\\n2, 1 MiB, 0 %\\\\n3, 1 MiB, 0 %\\\\n4, 1 MiB, 0 %\\\\n5, 1 MiB, 0 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.29}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 1 MiB, 0 %\\n1, 1 MiB, 0 %\\n2, 1 MiB, 0 %\\n3, 1 MiB, 0 %\\n4, 1 MiB, 0 %\\n5, 1 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.29}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_019UJYZuVL4gzzDxpWPRbbbq`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux ls 2>/dev/null || echo \"NO_TMUX_SESSIONS\"",
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
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "8b3440d5-b1a0-4594-bdff-6ecd905fb904",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ez9qeXvTypBXcybNWo8Rzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2089,
      "cache_read_input_tokens": 24574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2089
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

_source line 13 · 2026-05-28T08:21:47.592Z_

<details><summary>↩ Tool result · `toolu_019UJYZuVL4gzzDxpWPRbbbq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"NO_TMUX_SESSIONS\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "03d92573-8607-4374-b42b-3c4a0b332628",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"NO_TMUX_SESSIONS\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"NO_TMUX_SESSIONS\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011bFvfvU7KtXLXFukM1qK9f`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/src/evaluate.py /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
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
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "eb5d58fc-fdf4-433b-905a-1fa31642d49e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ez9qeXvTypBXcybNWo8Rzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2089,
      "cache_read_input_tokens": 24574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2089
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

_source line 15 · 2026-05-28T08:21:48.608Z_

<details><summary>↩ Tool result · `toolu_011bFvfvU7KtXLXFukM1qK9f`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root   36365 May 26 08:27 /root/acr-vla-conformal-refinement/src/evaluate.py\\n-rw-r--r-- 1 root root 1320219 May 23 07:23 /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "4c5e206b-ded1-42af-b552-c8745e9b5e90",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root   36365 May 26 08:27 /root/acr-vla-conformal-refinement/src/evaluate.py\\\\n-rw-r--r-- 1 root root 1320219 May 23 07:23 /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root   36365 May 26 08:27 /root/acr-vla-conformal-refinement/src/evaluate.py\\n-rw-r--r-- 1 root root 1320219 May 23 07:23 /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01SeCuB1wkGVCdiSrtqAbf6E`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "DONE"
  },
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
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "aaf0a78d-41f2-4471-ad1d-6de212cce26b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ez9qeXvTypBXcybNWo8Rzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2089,
      "cache_read_input_tokens": 24574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2089
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

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Ukn4f6vwVugyQHeLbmGQM4`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "RUNNING"
  },
  "limit": 0,
  "fields": [
    "exp_id",
    "status",
    "server"
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
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "6982e51a-a474-43f9-a476-f81981420dc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ez9qeXvTypBXcybNWo8Rzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2089,
      "cache_read_input_tokens": 24574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2089
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

_source line 18 · 2026-05-28T08:21:52.647Z_

<details><summary>↩ Tool result · `toolu_01SeCuB1wkGVCdiSrtqAbf6E`</summary>

```text
Error: result (107,431 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/ea13e2a6-0063-4484-9dd5-6afd670f7933/tool-results/mcp-agent-ml-research-read_registry-1779956512632.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/ea13e2a6-0063-4484-9dd5-6afd670f7933/tool-results/mcp-agent-ml-research-read_registry-1779956512632.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "b9617ecb-ed72-4d8e-a71e-13169ef41b0b",
  "tool_use_result": {
    "content": "Error: result (107,431 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/ea13e2a6-0063-4484-9dd5-6afd670f7933/tool-results/mcp-agent-ml-research-read_registry-1779956512632.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/ea13e2a6-0063-4484-9dd5-6afd670f7933/tool-results/mcp-agent-ml-research-read_registry-1779956512632.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-spatial-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"pi05-crm-always-on-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-crm-always-on-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau020-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau015-spatial-s42-fix\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-long-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-always-on-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau045-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau040-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-always-on-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau020-long-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-tau005-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-always-on-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-tau040-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-tau045-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-object-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau005-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"crm-always-on-object-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau010-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-tau-sweep-goal-tau070-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-tau-sweep-goal-tau050-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-goal-tau035-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-long-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-goal-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-goal-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-goal-tau025-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-tau-sweep-goal-tau050-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-goal-tau015-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau035-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau030-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"smolvla-tau015-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau045-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau040-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau030-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-long-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau025-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-long-tau015-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-k2mean-spatial-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-k2mean-long-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-k2mean-object-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau035-object-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau025-object-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau020-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau010-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau005-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau030-long-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau030-long-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"tau-sweep-goal-tau035-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"tau-sweep-long-tau015-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"tau-sweep-long-tau035-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau020-long-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"tau-sweep-goal-tau015-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"tau-sweep-spatial-tau035-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"tau-sweep-spatial-tau015-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau035-object-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau035-object-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau025-object-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-object-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-always-on-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm003-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-object-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-object-norm003-s46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-k2mean-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-k2mean-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-k2mean-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-vla-only-spatial-s42-4090\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-vla-only-goal-s42-4090\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-k2mean-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-vla-only-spatial-s42-4090-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-vla-only-object-s42-4090-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-vla-only-goal-s42-4090-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-tau010-015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-tau010-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed42-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-vla-only-object-s42-4090\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-vla-only-long-s42-4090\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"smolvla-tau020-long-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"smolvla-tau030-long-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-object-s43-r5\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-s44-westd\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-s44-westd\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm005-s45-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm005-s44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm003-s44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm005-s43-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm003-s43-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-s43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-s43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-vla-only-goal-s44-4090\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-vla-only-object-s43-4090\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-vla-only-long-s44-4090\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-vla-only-long-s43-4090\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-vla-only-long-s42-4090-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-ksweep-k5-obs-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm005-s44-westd\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau035-spatial-s42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm005-s43-westd\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm003-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm005-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm003-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-ksweep-k20-obs-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-ksweep-k20-obs-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau025-spatial-s42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm003-s43-westd\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm003-s44-westd\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-object-norm005-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-ksweep-k5-obs-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-vla-only-long-n20-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-vla-only-long-n20-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-object-adaptive-s44-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-object-adaptive-s43-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-object-adaptive-s42-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-object-s42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s43-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s43-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau025-long-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau015-long-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau025-object-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau035-long-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-goal-tau015-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"smolvla-tau035-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau025-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau015-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-goal-tau035-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"pi05-goal-tau025-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"pi05-adaptive-long-s43-cqa1-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-spatial-tau015-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-spatial-tau035-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-spatial-tau025-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-object-tau035-s42-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"E_smolvla_crm_norm005_spatial_s42_d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-object-tau015-s42-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"E_smolvla_adaptive_tau045_spatial_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"E_smolvla_adaptive_tau035_spatial_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"E_smolvla_adaptive_tau015_spatial_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-object-s42-tau045-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau035-spatial-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau015-spatial-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-crm-norm005-spatial-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau045-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-long-s44-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-long-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-crm-norm005-k10-object-s44-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau015-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau025-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"smolvla-tau035-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau025-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau015-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau015-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"smolvla-tau035-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-adaptive-long-s42-tau035-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"smolvla-tau015-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau025-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau035-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-long-s42-tau015-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau035-object-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau025-object-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau015-object-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau035-goal-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau025-goal-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau015-goal-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-goal-s42-tau035-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-adaptive-object-s44-paired\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"westd-pi05-adaptive-object-s43-paired\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"westd-pi05-adaptive-object-s42-paired\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"westd-pi05-crm-k2-object-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"westd-pi05-crm-k2-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"westd-pi05-crm-k2-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-crm-goal-s43-d149-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-s43-d149-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-s42-d149-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-spatial-s48-d149-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-long-s44-cqa1-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-object-s44-cqa1-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-object-s43-cqa1-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-goal-s42-tau015-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-spatial-s42-tau015-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-spatial-s42-tau035-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-spatial-s48-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-long-s43-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-goal-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-long-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-long-s44-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-goal-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-k2-long-s44-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-k2-object-s42-bjb1-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-k2-object-s43-bjb1-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-k2-object-s44-bjb1-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-goal-s44-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"pi05-adaptive-spatial-s44-bjb2-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-spatial-s43-bjb2-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-spatial-s42-bjb2-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-k2-spatial-s44-bjb2-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-k2-spatial-s43-bjb2-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-k2-spatial-s42-bjb2-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-k2-goal-s44-bjb1-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-k2-goal-s43-bjb1-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-k2-goal-s42-bjb1-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-vla-only-long-s44-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-k2-long-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"pi05-crm-k2-long-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"westd-pi05-vla-only-long-s43-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-crm-k2-long-s43-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"westd-pi05-vla-only-spatial-s43-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-vla-only-spatial-s42-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-vla-only-spatial-s44-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-vla-only-long-s42-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-vla-only-object-s44-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-vla-only-object-s43-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-vla-only-object-s42-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-vla-only-goal-s44-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-vla-only-goal-s43-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-vla-only-goal-s42-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-object-s42-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-long-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-object-s43-bjb2-24035\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-long-s44-cqa1-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-adaptive-long-s43-cqa1-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-adaptive-goal-s42-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-crm-k2-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-adaptive-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-adaptive-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-adaptive-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-object-s44-cqa1-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-adaptive-goal-s43-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-adaptive-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-spatial-s44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-spatial-s43-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-spatial-s42-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-spatial-s44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-spatial-s43-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-spatial-s42-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-object-s44-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-object-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-object-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-goal-s44-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-goal-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-goal-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-spatial-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-spatial-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-goal-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-goal-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-object-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-object-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-spatial-k1-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-vla-only-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-adaptive-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"tau_sweep_goal_tau090_s42_cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"tau_sweep_goal_tau070_s42_cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"tau_sweep_goal_tau050_s42_cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"tau_sweep_spatial_tau025_s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"tau_sweep_goal_tau025_s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"tau_sweep_goal_tau040_s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"tau_sweep_goal_tau045_s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"goal_vla_only_s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"goal_adapt_s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"westd-pi05-k2mean-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-goal-vla-only-s49-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-goal-adapt-tau025-s49-paired\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-spatial-vla-only-s48-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-spatial-vla-only-s46-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-spatial-adapt-tau025-s48-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-spatial-adapt-tau025-s46-paired\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"pi05-adaptive-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-object-s42-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-k2mean-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-long-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-goal-vla-only-s49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-mechanism-goal-adapt-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-crm-k2-long-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-crm-k2-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-k2-tau030-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau020-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-object-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-goal-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-spatial-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-spatial-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-goal-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-goal-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-long-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-long-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-adaptive-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-crm-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-bjb1-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-bjb1-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-long-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-long-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s44-paired-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s43-paired-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s42-paired-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-s47-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-object-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-crm-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-pi05-adaptive-goal-s42-dryrun\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-spatial-s47-bjb1-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-spatial-s47-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-goal-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-adaptive-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-k2-tau010-spatial-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau0075-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau015-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-goal-vla-only-s46-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-goal-vla-only-s45-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-goal-adapt-s47-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-goal-adapt-s46-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-goal-vla-only-s47-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-goal-adapt-s45-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-bjb1-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-adaptive-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-adaptive-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-adaptive-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-adaptive-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-adaptive-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-cqa1-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-cqa1-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-cqa1-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-adaptive-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-s42-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s42-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-long-adaptive-k10-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau010-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-norm005-goal-s49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-norm005-object-s48\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-long-vla-only-s48\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s50\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-spatial-vla-only-smolvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train-crm-pi05-unified-3suite-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-vla-only-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-obj-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-obj-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-goal-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-spatial-s42-sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-a1-baseline-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-vla-only-s47-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-adapt-tau025-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-crm-norm005-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s47-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-unified-3suite\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-spatial-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-goal-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-goal-bjb1-32546\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-pi05-spatial-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-crm-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-k2mean-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-crm-norm005-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-adapt-tau025-s45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-ablation-tau040-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-ablation-tau015-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-ablation-tau010-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-goal-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-goal-reconvla-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-k2mean-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r6\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-goal-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-crm-norm005-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-k2-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-adapt-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-object-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-crm005-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm02-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed55\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-features-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-adapt-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau035-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r5-resumed\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau035-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-3dir-adaptive-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-3dir-norm03-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-3dir-reconvla-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-3dir-norm01-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-3dir-norm005-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-goal-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-spatial-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-object-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-object-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r5\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-long-2048\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-lerobot-goal-seed44-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-smolvla-3suite-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-goal-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-object-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-long-wrapper-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-unified-4suite-r4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-long-seed42-r4-rerun\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-crm-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed43-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed44-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed42-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed44-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed43-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-long-k2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-bjb2-28827\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-long-bjb2-28827\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-long-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-oft-official-object\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-object-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-official-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-unified-4suite\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-smolvla-long-bjb1-32546-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-long-bjb1-32546\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-loss-perdof-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-loss-combined-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-loss-conformal-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-loss-mse-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-openvla-oft-object-baseline-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"precompute-smolvla-long-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-loss-combined\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"crm-loss-conformal\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"precompute-smolvla-goal-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-loss-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-loss-mse-baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-acr-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-long-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-long-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-acr-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-acr-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-train-pi05-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-pi05-object-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-pi05-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-pi05-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-spatial-obs-only-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed75\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed51-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed52-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed61\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed64-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed63\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed62\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed52-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed55-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-openvla-crm-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed54\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-openvla-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"openvla-precompute-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed42-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed44-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed44-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-k1-object-seed43-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-k1-object-seed42-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-latency-profiling-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-adaptive-k-spatial-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-k-spatial-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"latency-profile-n1000\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"calibrate-crm-correction-signal\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"fmvd-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-k5\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-k5\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}}, \"count\": 1214, \"total\": 1214, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.2136}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T08:21:55.763Z_

<details><summary>↩ Tool result · `toolu_01Ukn4f6vwVugyQHeLbmGQM4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-spatial-k2mean-s47\": {\"status\": \"RUNNING\"}, \"eval-supp-spatial-adapt-tau025-s47\": {\"status\": \"RUNNING\"}, \"smolvla-adapt-tau015-object-s44-cqa1\": {\"status\": \"RUNNING\"}, \"smolvla-adapt-tau015-object-s43-cqa1\": {\"status\": \"RUNNING\"}, \"smolvla-adapt-tau015-object-s42-cqa1\": {\"status\": \"RUNNING\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"RUNNING\"}, \"eval-supp-long-vla-only-s42\": {\"status\": \"RUNNING\"}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-k2-tau045-spatial-s42-bjb2\": {\"status\": \"RUNNING\"}, \"eval-random-selection-object-seed43-v2\": {\"status\": \"RUNNING\"}, \"eval-supp-long-vla-only-s46\": {\"status\": \"RUNNING\"}, \"smolvla-tau020-spatial-s42\": {\"status\": \"RUNNING\"}, \"smolvla-tau025-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-ksweep-k20-obs-obj-s43\": {\"status\": \"RUNNING\"}, \"eval-ksweep-k20-obs-object-s44\": {\"status\": \"RUNNING\"}, \"pi05-crm-always-on-object-s44\": {\"status\": \"RUNNING\"}, \"pi05-crm-always-on-goal-s44\": {\"status\": \"RUNNING\"}, \"pi05-crm-always-on-goal-s43\": {\"status\": \"RUNNING\"}, \"pi05-crm-always-on-long-s44\": {\"status\": \"RUNNING\"}, \"pi05-crm-always-on-long-s43\": {\"status\": \"RUNNING\"}}, \"count\": 20, \"total\": 20, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0971}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "222123e7-0289-4d17-982f-ae88f12cdde7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-spatial-k2mean-s47\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-spatial-adapt-tau025-s47\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"smolvla-adapt-tau015-object-s44-cqa1\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"smolvla-adapt-tau015-object-s43-cqa1\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"smolvla-adapt-tau015-object-s42-cqa1\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-long-vla-only-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-long-vla-only-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-adapt-tau025-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-tau045-spatial-s42-bjb2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-random-selection-object-seed43-v2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-long-vla-only-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"smolvla-tau020-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"smolvla-tau025-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-ksweep-k20-obs-obj-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-ksweep-k20-obs-object-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"pi05-crm-always-on-object-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"pi05-crm-always-on-goal-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"pi05-crm-always-on-goal-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"pi05-crm-always-on-long-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"pi05-crm-always-on-long-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}}, \\\"count\\\": 20, \\\"total\\\": 20, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.0971}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-spatial-k2mean-s47\": {\"status\": \"RUNNING\"}, \"eval-supp-spatial-adapt-tau025-s47\": {\"status\": \"RUNNING\"}, \"smolvla-adapt-tau015-object-s44-cqa1\": {\"status\": \"RUNNING\"}, \"smolvla-adapt-tau015-object-s43-cqa1\": {\"status\": \"RUNNING\"}, \"smolvla-adapt-tau015-object-s42-cqa1\": {\"status\": \"RUNNING\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"RUNNING\"}, \"eval-supp-long-vla-only-s42\": {\"status\": \"RUNNING\"}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-k2-tau045-spatial-s42-bjb2\": {\"status\": \"RUNNING\"}, \"eval-random-selection-object-seed43-v2\": {\"status\": \"RUNNING\"}, \"eval-supp-long-vla-only-s46\": {\"status\": \"RUNNING\"}, \"smolvla-tau020-spatial-s42\": {\"status\": \"RUNNING\"}, \"smolvla-tau025-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-ksweep-k20-obs-obj-s43\": {\"status\": \"RUNNING\"}, \"eval-ksweep-k20-obs-object-s44\": {\"status\": \"RUNNING\"}, \"pi05-crm-always-on-object-s44\": {\"status\": \"RUNNING\"}, \"pi05-crm-always-on-goal-s44\": {\"status\": \"RUNNING\"}, \"pi05-crm-always-on-goal-s43\": {\"status\": \"RUNNING\"}, \"pi05-crm-always-on-long-s44\": {\"status\": \"RUNNING\"}, \"pi05-crm-always-on-long-s43\": {\"status\": \"RUNNING\"}}, \"count\": 20, \"total\": 20, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0971}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Let me check the status:

1. **GPU status**: All 6 GPUs (0-5) are idle (1 MiB used, 0% utilization) ✓
2. **tmux**: No sessions ✓
3. **Files**: Both evaluate.py and crm_best.pt exist ✓
4. **Registry RUNNING**: I need to check if any of the 6 planned exp_ids are already RUNNING or DONE.

From RUNNING experiments:
- `eval-supp-spatial-k2mean-s47` — **RUNNING** → This is one of our planned experiments (cuda:4)!


- `eval-supp-adapt-tau025-spatial-s46` — **RUNNING** → This is planned for cuda:2!

The other four experiments aren't currently running, so they're clear to launch.

Now I need to cross-reference against the DONE registry to make sure none of these have already completed. The DONE file is quite large, so I'll search for each specific experiment ID to check their status.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "7e960bc5-c8a4-4a75-b02d-bec5e45702c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbEtndjprB2JZ59cTBApjj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 26663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

_source line 21_

GPU 全部空闲，无 tmux 残留，文件就绪。发现 2 个计划实验已在 RUNNING：
- `eval-supp-spatial-k2mean-s47` (cuda:4)
- `eval-supp-adapt-tau025-spatial-s46` (cuda:2)

需要检查 DONE registry 中是否有其他计划实验，以及确认需要替换哪些。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "023579b7-f01e-4418-8667-81d6eb22523c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbEtndjprB2JZ59cTBApjj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 26663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01HTPSReMPVAkvRyTgHyERdw`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/ea13e2a6-0063-4484-9dd5-6afd670f7933/tool-results/mcp-agent-ml-research-read_registry-1779956512632.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\ntargets = [\n    'smolvla-crm-norm005-spatial-s42-d149',\n    'smolvla-crm-norm005-k10-object-s44-cqa1', \n    'eval-supp-adapt-tau025-spatial-s46',\n    'eval-supp-long-adapt-tau025-s47-r2',\n    'eval-supp-spatial-k2mean-s47',\n    'eval-obs-only-object-norm005-seed75',\n    'eval-obs-only-object-norm01-seed74',\n    'eval-obs-only-object-norm003-seed73',\n    'eval-obs-only-object-norm005-seed64',\n    'smolvla-adapt-tau015-object-s42-cqa1',\n]\nfor t in targets:\n    if t in exps:\n        e = exps[t]\n        print(f'{t}: status={e.get(\\\"status\\\")}, conclusion={e.get(\\\"conclusion\\\",\\\"N/A\\\")}')\n    else:\n        print(f'{t}: NOT_FOUND')\n\"\n",
  "description": "Search DONE registry for planned experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "bfd761c0-0faf-4096-9df0-f9553de1f5bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbEtndjprB2JZ59cTBApjj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 26663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

_source line 23 · 2026-05-28T08:22:15.130Z_

<details><summary>↩ Tool result · `toolu_01HTPSReMPVAkvRyTgHyERdw`</summary>

```text
smolvla-crm-norm005-spatial-s42-d149: status=DONE, conclusion=success
smolvla-crm-norm005-k10-object-s44-cqa1: status=DONE, conclusion=success
eval-supp-adapt-tau025-spatial-s46: NOT_FOUND
eval-supp-long-adapt-tau025-s47-r2: status=DONE, conclusion=negative
eval-supp-spatial-k2mean-s47: NOT_FOUND
eval-obs-only-object-norm005-seed75: status=DONE, conclusion=success
eval-obs-only-object-norm01-seed74: status=DONE, conclusion=success
eval-obs-only-object-norm003-seed73: status=DONE, conclusion=success
eval-obs-only-object-norm005-seed64: status=DONE, conclusion=success
smolvla-adapt-tau015-object-s42-cqa1: NOT_FOUND
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "fa1f1c8a-71e2-4530-8162-3564b6870367",
  "tool_use_result": {
    "stdout": "smolvla-crm-norm005-spatial-s42-d149: status=DONE, conclusion=success\nsmolvla-crm-norm005-k10-object-s44-cqa1: status=DONE, conclusion=success\neval-supp-adapt-tau025-spatial-s46: NOT_FOUND\neval-supp-long-adapt-tau025-s47-r2: status=DONE, conclusion=negative\neval-supp-spatial-k2mean-s47: NOT_FOUND\neval-obs-only-object-norm005-seed75: status=DONE, conclusion=success\neval-obs-only-object-norm01-seed74: status=DONE, conclusion=success\neval-obs-only-object-norm003-seed73: status=DONE, conclusion=success\neval-obs-only-object-norm005-seed64: status=DONE, conclusion=success\nsmolvla-adapt-tau015-object-s42-cqa1: NOT_FOUND",
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

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture:

**Planned experiments that need replacement:**

| GPU | Original exp_id | Status | Action |
|-----|-----------------|--------|--------|
| cuda:0 | smolvla-crm-norm005-spatial-s42-d149 | DONE (success) | Need replacement |
| cuda:1 | smolvla-crm-norm005-k10-object-s44-cqa1 | DONE (success) | Need replacement |
| cuda:2 | eval-supp-adapt-tau025-spatial-s46 | RUNNING (elsewhere) | Need replacement |


| cuda:3 | eval-supp-long-adapt-tau025-s47-r2 | DONE (negative) | Need replacement |
| cuda:4 | eval-supp-spatial-k2mean-s47 | RUNNING (elsewhere) | Need replacement |
| cuda:5 | eval-obs-only-object-norm005-seed75 | DONE (success) | Need replacement |

All six planned experiments are either completed or running elsewhere, so I need to find replacements for every single one. Looking at my backup candidates, I have several completed eval-obs-only-object runs with different norm and seed values that could work as substitutes.

But checking the backup list more carefully, I'm realizing that the experiments I thought were available are actually already done or running on other machines. I need to reconcile what I'm seeing in the DONE registry versus the RUNNING registry—some experiments appear in one but not the other, which suggests my search results might be incomplete or there's overlap I'm not accounting for properly. Looking at the rest of the experiment statuses, cuda:5 is also done, and all the backup experiments are either completed or running. Since all 10 slots are accounted for with no available GPUs, I need to let the user know there's nothing to deploy right now and ask how they'd like to proceed with the free capacity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "6187360c-5658-4c44-a23c-670695e6b3a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JktvF3rjk1BYW49tNCWybk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 28917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1583
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

_source line 25_

所有 6 个计划实验和 4 个备选都已完成或在运行中：

| GPU | 计划 exp_id | 状态 |
|-----|------------|------|
| cuda:0 | smolvla-crm-norm005-spatial-s42-d149 | **DONE** (success) |
| cuda:1 | smolvla-crm-norm005-k10-object-s44-cqa1 | **DONE** (success) |
| cuda:2 | eval-supp-adapt-tau025-spatial-s46 | **RUNNING** (其他服务器) |
| cuda:3 | eval-supp-long-adapt-tau025-s47-r2 | **DONE** (negative) |
| cuda:4 | eval-supp-spatial-k2mean-s47 | **RUNNING** (其他服务器) |
| cuda:5 | eval-obs-only-object-norm005-seed75 | **DONE** (success) |

**备选列表同样全部已完成或运行中：**
- eval-obs-only-object-norm01-seed74 → DONE
- eval-obs-only-object-norm003-seed73 → DONE
- eval-obs-only-object-norm005-seed64 → DONE
- smolvla-adapt-tau015-object-s42-cqa1 → RUNNING

bjb1-32546 的 6 张 GPU 全部空闲可用，但已无可部署的实验。需要你提供新的实验列表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "uuid": "82c940b7-f9dd-4efb-87a1-f005af7e4ba9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JktvF3rjk1BYW49tNCWybk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 28917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1583
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

### Task result

_source line 26_

所有 6 个计划实验和 4 个备选都已完成或在运行中：

| GPU | 计划 exp_id | 状态 |
|-----|------------|------|
| cuda:0 | smolvla-crm-norm005-spatial-s42-d149 | **DONE** (success) |
| cuda:1 | smolvla-crm-norm005-k10-object-s44-cqa1 | **DONE** (success) |
| cuda:2 | eval-supp-adapt-tau025-spatial-s46 | **RUNNING** (其他服务器) |
| cuda:3 | eval-supp-long-adapt-tau025-s47-r2 | **DONE** (negative) |
| cuda:4 | eval-supp-spatial-k2mean-s47 | **RUNNING** (其他服务器) |
| cuda:5 | eval-obs-only-object-norm005-seed75 | **DONE** (success) |

**备选列表同样全部已完成或运行中：**
- eval-obs-only-object-norm01-seed74 → DONE
- eval-obs-only-object-norm003-seed73 → DONE
- eval-obs-only-object-norm005-seed64 → DONE
- smolvla-adapt-tau015-object-s42-cqa1 → RUNNING

bjb1-32546 的 6 张 GPU 全部空闲可用，但已无可部署的实验。需要你提供新的实验列表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 58722,
  "duration_api_ms": 54765,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "ea13e2a6-0063-4484-9dd5-6afd670f7933",
  "total_cost_usd": 0.25317025000000004,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 18655,
    "cache_read_input_tokens": 91999,
    "output_tokens": 3520,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 18655,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1352,
        "cache_read_input_tokens": 28917,
        "cache_creation_input_tokens": 1583,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1583
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2437,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002542,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 3520,
      "cacheReadInputTokens": 91999,
      "cacheCreationInputTokens": 18655,
      "webSearchRequests": 0,
      "costUSD": 0.25062825,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bf49670b-b863-4a4f-8e11-0ad15ae427d9"
}
```

</details>

---
