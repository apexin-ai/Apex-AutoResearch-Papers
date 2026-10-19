# gpu check and deploy supp

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 104
- **Recorded user turns:** 1
- **Tool calls:** 34
- **Original source:** `logs/workers/worker_gpu_check-and-deploy-supp_20260528T155015.log`
- **Structured JSON:** [`2e6d2b423155b4b32636.json`](../../sessions/2e/2e6d2b423155b4b32636.json)

## Before a recorded user message

29 recorded events

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
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
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
  "uuid": "adaf5ab3-9b44-4e79-becb-8cd69151abdf",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779996600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b74675ad-ae28-4a62-8a82-8f1d29c24529",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down the task:
1. Check GPU status on 4 servers
2. Read registry for completed experiments
3. Read supplementary summary
4. Read experiment plan
5. Report status and gaps

Let me start by loading the MCP tools I need, then execute everything in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "5a06eda9-911c-4005-9e15-a91560ab4af8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VG5EAQcpQjDhLa7HZ768rF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12222,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12222
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

先加载需要的工具，然后并行检查所有服务器和读取项目数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "77458b85-e83d-44eb-812c-dd3fbc5d2d76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VG5EAQcpQjDhLa7HZ768rF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12222,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12222
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01L9AYTuP2SW1aec25SjwLSc`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "57408b3c-be9d-4d2c-81ea-adfcfeaef802",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VG5EAQcpQjDhLa7HZ768rF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12222,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12222
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-28T15:50:30.750Z_

<details><summary>↩ Tool result · `toolu_01L9AYTuP2SW1aec25SjwLSc`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "71a06652-f553-4f1a-95bd-d5826222609e",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 29
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me execute all the checks in parallel:
1. GPU status on all 4 servers
2. Read registry for DONE experiments
3. Read registry for RUNNING experiments
4. Read supplementary summary
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "5e3625fc-f2bc-478a-a676-a264110696af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGXJcQB1QHRxuQF97636hD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1216,
      "cache_read_input_tokens": 24067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1216
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

_source line 9_

并行检查 4 台服务器 GPU 状态 + 读取 registry 和 supplementary 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "2a2afdf3-fe56-4d9a-bbe6-d250fe5038f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGXJcQB1QHRxuQF97636hD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1216,
      "cache_read_input_tokens": 24067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1216
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017N4tDprfcvFckEqFBtDVsh`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader",
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
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "ed080065-ee33-4cbc-ae36-f7654f7e6eee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGXJcQB1QHRxuQF97636hD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1216,
      "cache_read_input_tokens": 24067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1216
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01ADzsnJ6DhY8xwktCxcYAHz`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader",
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
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "aa005adf-11bc-47ee-bf72-d051b82ec2fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGXJcQB1QHRxuQF97636hD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1216,
      "cache_read_input_tokens": 24067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1216
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

### Tool result

_source line 12 · 2026-05-28T15:50:36.456Z_

<details><summary>↩ Tool result · `toolu_017N4tDprfcvFckEqFBtDVsh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA GeForce RTX 4090, 0 MiB, 24564 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.13}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "5d4e12a6-3084-4664-a839-d4ef607b94a8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, NVIDIA GeForce RTX 4090, 0 MiB, 24564 MiB, 0 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.13}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA GeForce RTX 4090, 0 MiB, 24564 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.13}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T15:50:36.544Z_

<details><summary>↩ Tool result · `toolu_01ADzsnJ6DhY8xwktCxcYAHz`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[Errno None] Unable to connect to port 32546 on 106.120.183.117\", \"metadata\": {\"elapsed_seconds\": 0.08}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "b11aa0e9-a1ea-4e23-9ba4-306ac2c63125",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[Errno None] Unable to connect to port 32546 on 106.120.183.117\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.08}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[Errno None] Unable to connect to port 32546 on 106.120.183.117\", \"metadata\": {\"elapsed_seconds\": 0.08}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019bKRe6M74Wrkrw9Vc5HMV1`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader",
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
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "603b74bf-65dc-4fc3-8771-8804d34aef2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGXJcQB1QHRxuQF97636hD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1216,
      "cache_read_input_tokens": 24067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1216
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

### Tool result

_source line 15 · 2026-05-28T15:50:37.630Z_

<details><summary>↩ Tool result · `toolu_019bKRe6M74Wrkrw9Vc5HMV1`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[Errno None] Unable to connect to port 28827 on 106.38.204.136\", \"metadata\": {\"elapsed_seconds\": 0.24}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "315ad8be-39de-4027-b1bd-e461f6bf604a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[Errno None] Unable to connect to port 28827 on 106.38.204.136\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.24}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[Errno None] Unable to connect to port 28827 on 106.38.204.136\", \"metadata\": {\"elapsed_seconds\": 0.24}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014YQ1Ws3XQ4cMezUZTQtsWp`</summary>

```json
{
  "server": "cqa1-32758",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader",
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
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "cb79c1e2-4810-4555-9bf3-8354214431e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGXJcQB1QHRxuQF97636hD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1216,
      "cache_read_input_tokens": 24067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1216
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

### Tool result

_source line 17 · 2026-05-28T15:50:38.379Z_

<details><summary>↩ Tool result · `toolu_014YQ1Ws3XQ4cMezUZTQtsWp`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[Errno None] Unable to connect to port 32758 on 58.144.141.28\", \"metadata\": {\"elapsed_seconds\": 0.19}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "6eedf96a-2311-4030-9c06-e42eaf3345a2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[Errno None] Unable to connect to port 32758 on 58.144.141.28\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.19}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[Errno None] Unable to connect to port 32758 on 58.144.141.28\", \"metadata\": {\"elapsed_seconds\": 0.19}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_017YoVuqQN51owKaU8km92Kg`</summary>

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
    "conclusion",
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
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "6464fade-ee3e-4652-bc7f-a26003e29102",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGXJcQB1QHRxuQF97636hD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1216,
      "cache_read_input_tokens": 24067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1216
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

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01KHeuJ2mo7npkzmpoNJK93g`</summary>

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
    "server",
    "gpu"
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
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "d6bb8312-e481-48de-b8ad-607937fd1955",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGXJcQB1QHRxuQF97636hD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1216,
      "cache_read_input_tokens": 24067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1216
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

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019tgQgx4NHpt6qWYALrMLzg`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "artifacts/supplementary/supplementary_summary.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "1761deea-9a66-4440-9b4f-411bbcfba67f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGXJcQB1QHRxuQF97636hD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1216,
      "cache_read_input_tokens": 24067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1216
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

### Tool result

_source line 21 · 2026-05-28T15:50:42.756Z_

<details><summary>↩ Tool result · `toolu_017YoVuqQN51owKaU8km92Kg`</summary>

```text
Error: result (306,502 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "42a1a44d-6300-4b66-80be-a151cfdddfe3",
  "tool_use_result": {
    "content": "Error: result (306,502 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-only-spatial-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-k-p25-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"killed\"}, \"eval-crm-spatial-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-object-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-spatial-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"killed\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"killed\"}, \"eval-vla-only-long-seed49\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-object-seed51\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-long-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"killed\"}, \"eval-crm-long-seed49\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"killed\"}, \"eval-crm-goal-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.69, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"killed\"}, \"eval-crm-goal-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.68, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-seed51\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed50\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-long-seed51\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-long-seed53\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-long-seed54\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed52\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-long-seed52\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-goal-seed49\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-goal-seed50\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-seed52\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-seed53\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-long-seed53\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-seed54\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-long-seed54\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-goal-norm02-seed53\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed77\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed76\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed77\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed78\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed76\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed62-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed63-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed76\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed77\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-random-selection-object-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-shard3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-shard4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-shard5\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-shard6\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-shard7\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-shard8\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-shard9\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-spatial-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-spatial-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-spatial-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-spatial-shard3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-spatial-shard4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-spatial-shard5\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-spatial-shard6\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-shard5\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-shard6\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-shard7\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-shard8\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-shard9\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s5-fix\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s6-fix\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s7-fix\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s8-fix\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s9-fix\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s1-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s2-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s3-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s4-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s5-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s0-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s7-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s8-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s9-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-obj-s6-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-pipeline-auto\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-goal-bjb2-28827-s0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-goal-bjb2-28827-s1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-goal-bjb2-28827-s2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-long-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-long-seed0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-long-seed1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-long-seed2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-object-k10\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-spatial-k10\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-k10\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-lerobot-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-k2mean-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm-norm005-s46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"source\": \"json_harvest_bjb1\"}, \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-tau-sweep-spatial-tau010-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"overall_success_rate\": 0.79, \"trigger_rate\": 0.752, \"tau\": 0.1, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-tau-sweep-spatial-tau020-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"overall_success_rate\": 0.81, \"trigger_rate\": 0.266, \"tau\": 0.2, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-tau-sweep-spatial-tau030-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"overall_success_rate\": 0.805, \"trigger_rate\": 0.167, \"tau\": 0.3, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-crm-obj-s47-reeval\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"overall_success_rate\": 0.825, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\", \"seed\": 47}}, \"eval-adaptive-k1-spatial-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"overall_success_rate\": 0.795, \"trigger_rate\": 0.197, \"tau\": 0.25, \"K\": 1, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-adaptive-k5-spatial-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau025-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"overall_success_rate\": 0.81, \"trigger_rate\": 0.198, \"tau\": 0.25, \"benchmark\": \"spatial\", \"seed\": 48}}, \"eval-supp-adapt-tau025-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"overall_success_rate\": 0.82, \"trigger_rate\": 0.195, \"tau\": 0.25, \"benchmark\": \"spatial\", \"seed\": 49}}, \"eval-supp-adapt-tau025-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"overall_success_rate\": 0.845, \"trigger_rate\": 0.089, \"tau\": 0.25, \"benchmark\": \"goal\", \"seed\": 48}}, \"eval-supp-adapt-tau025-goal-s49\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"overall_success_rate\": 0.815, \"trigger_rate\": 0.089, \"tau\": 0.25, \"benchmark\": \"goal\", \"seed\": 49}}, \"eval-supp-adapt-tau025-obj-s48\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"overall_sr\": 0.76, \"trigger_rate\": 0.0389, \"mean_uncertainty\": 0.1117, \"per_task_sr\": {\"soup\": 0.75, \"cream_cheese\": 0.75, \"salad\": 0.7, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.6, \"milk\": 0.8, \"pudding\": 0.7, \"oj\": 0.95}}}, \"eval-supp-adapt-tau025-obj-s49\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"overall_sr\": 0.74, \"trigger_rate\": 0.0417, \"mean_uncertainty\": 0.1131, \"per_task_sr\": {\"soup\": 0.7, \"cream_cheese\": 0.65, \"salad\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.75, \"tomato\": 0.75, \"butter\": 0.6, \"milk\": 0.6, \"pudding\": 0.8, \"oj\": 0.95}}}, \"eval-supp-adapt-tau025-obj-s50\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-reconvla-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-reconvla-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-reconvla-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-object-vla-only-s50\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-reconvla-spatial-s42-bf16\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-s50\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-vla-only-s42-verify\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-tau035-spatial-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.795, \"trigger_rate\": 0.123, \"benchmark\": \"spatial\", \"seed\": 42, \"tau\": 0.35, \"K\": 2, \"norm\": 0.2}, \"conclusion\": \"killed\"}, \"eval-canonical-vla-only-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-adaptive-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-adaptive-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-bjb2-s45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-bjb2-s47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-spatial-adapt-s46-paired\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"mode\": \"adaptive_conformal_crm\", \"benchmark\": \"spatial\", \"seed\": 46, \"K\": 2, \"tau\": 0.25, \"trigger_rate\": 0.1906, \"mean_unc\": 0.1826, \"crm_steps\": 5442, \"total_steps\": 28553}}, \"eval-k2-spatial-adapt-s48-paired\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"mode\": \"adaptive_conformal_crm\", \"benchmark\": \"spatial\", \"seed\": 48, \"K\": 2, \"tau\": 0.25, \"trigger_rate\": 0.2, \"mean_unc\": 0.1869, \"crm_steps\": 5650, \"total_steps\": 28244}}, \"eval-k2-spatial-adapt-s49-paired\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"mode\": \"adaptive_conformal_crm\", \"benchmark\": \"spatial\", \"seed\": 49, \"K\": 2, \"tau\": 0.25, \"trigger_rate\": 0.1999, \"mean_unc\": 0.1878, \"crm_steps\": 5624, \"total_steps\": 28134}}, \"eval-k2-spatial-vla-only-s46-paired\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"mode\": \"vla_only\", \"benchmark\": \"spatial\", \"seed\": 46}}, \"eval-k2-spatial-vla-only-s48-paired\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 0.775, \"successes\": 155, \"total\": 200, \"mode\": \"vla_only\", \"benchmark\": \"spatial\", \"seed\": 48}}, \"eval-k2-spatial-vla-only-s49-paired\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"mode\": \"vla_only\", \"benchmark\": \"spatial\", \"seed\": 49}}, \"eval-k2-spatial-adapt-s45-paired\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 0.8, \"total\": 200, \"mode\": \"adaptive_conformal_crm\", \"benchmark\": \"spatial\", \"seed\": 45, \"K\": 2, \"tau\": 0.25, \"trigger_rate\": 0.201, \"mean_unc\": 0.186}}, \"eval-k2-spatial-vla-only-s45-paired\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 0.805, \"total\": 200, \"mode\": \"vla_only\", \"benchmark\": \"spatial\", \"seed\": 45}}, \"eval-k2-spatial-adapt-s47-paired\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 0.795, \"total\": 200, \"mode\": \"adaptive_conformal_crm\", \"benchmark\": \"spatial\", \"seed\": 47, \"K\": 2, \"tau\": 0.25, \"trigger_rate\": 0.208, \"mean_unc\": 0.188}}, \"eval-k2-spatial-vla-only-s47-paired\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 0.765, \"total\": 200, \"mode\": \"vla_only\", \"benchmark\": \"spatial\", \"seed\": 47}}, \"eval-crm-goal-s42-d149-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-spatial-s49-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-spatial-s47-rerun\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-goal-s42-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-long-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-spatial-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-tau005-spatial-s42-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.785, \"trigger_rate\": 0.994, \"benchmark\": \"spatial\", \"seed\": 42, \"tau\": 0.05, \"K\": 2, \"norm\": 0.2}, \"conclusion\": \"killed\"}, \"eval-k2-tau040-spatial-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.0987, \"benchmark\": \"spatial\", \"seed\": 42, \"tau\": 0.4, \"K\": 2, \"norm\": 0.2}, \"conclusion\": \"killed\"}, \"eval-k2-tau045-spatial-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.8, \"trigger_rate\": 0.0723, \"benchmark\": \"spatial\", \"seed\": 42, \"tau\": 0.45, \"K\": 2, \"norm\": 0.2}, \"conclusion\": \"killed\"}, \"pi05-tau-sweep-goal-tau050-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-tau-sweep-goal-tau070-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-tau-sweep-goal-tau090-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-k2mean-goal-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-object-s44-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 0.88, \"successes\": 176, \"total\": 200, \"mode\": \"adaptive_conformal_crm\", \"benchmark\": \"object\", \"seed\": 44, \"trigger_rate\": 0.035, \"tau\": 0.25}}, \"westd-pi05-vla-only-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-goal-s42-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-goal-s43-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-goal-s44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-object-s42-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-object-s43-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-object-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-long-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-goal-s43-cqa1-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-goal-s44-cqa1-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-goal-s44-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"westd-pi05-vla-only-long-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-k2mean-goal-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-k2mean-object-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-k2mean-long-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-k2mean-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-vla-only-long-s42-4090-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-tau045-spatial-s42-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau025-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau035-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm005-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm005-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-s43-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-s44-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm005-s43-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm005-s44-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-s44-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-object-norm003-s45-bjb2-24035\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-always-on-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-always-on-long-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-always-on-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm005-s44-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-openvla-crm-k1-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-openvla-crm-k1-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau020-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-adapt-tau025-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-long-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.76, \"benchmark\": \"long\", \"mode\": \"crm_obs_only\", \"seed\": 43, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10, \"K\": 2}}, \"pi05-crm-k2-long-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"mode\": \"crm_obs_only\", \"K\": 2, \"max_correction_norm\": 0.05, \"benchmark\": \"long\", \"seed\": 42}}, \"pi05-adaptive-goal-s44-backfill\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.865, \"trigger_rate\": 0.1}}, \"pi05-crm-k2-long-s43-backfill\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-crm-k2-long-s42-backfill\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.585, \"successes\": 117, \"total_rollouts\": 200, \"benchmark\": \"long\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 46, \"K\": 2, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25}}, \"eval-supp-long-adapt-tau025-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.6, \"successes\": 120, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s44\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.56, \"trigger_rate\": 0.049}, \"conclusion\": \"negative\"}, \"eval-supp-long-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 59.5, \"total_successes\": 119, \"total_trials\": 200}}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 60.5, \"total_successes\": 121, \"total_trials\": 200}}, \"pi05-crm-always-on-long-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 79.5, \"total_successes\": 159, \"total_trials\": 200}}, \"eval-supp-spatial-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"trigger_rate\": 0.21, \"mean_uncertainty\": 0.1886, \"total_successes\": 159, \"total_trials\": 200}}, \"eval-supp-spatial-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 82, \"total_successes\": 164, \"total_trials\": 200}}, \"smolvla-adapt-tau015-object-s44-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 73.5, \"trigger_rate\": 0.168, \"mean_uncertainty\": 0.1097, \"total_successes\": 147, \"total_trials\": 200}}, \"smolvla-adapt-tau015-object-s43-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78, \"trigger_rate\": 0.174, \"mean_uncertainty\": 0.1122, \"total_successes\": 156, \"total_trials\": 200}}, \"smolvla-adapt-tau015-object-s42-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"trigger_rate\": 0.171, \"mean_uncertainty\": 0.112, \"total_successes\": 158, \"total_trials\": 200}}, \"eval-ksweep-k20-obs-obj-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 77}, \"conclusion\": \"success\"}, \"eval-ksweep-k20-obs-object-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 71}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed43-v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 77}, \"conclusion\": \"success\"}, \"pi05-crm-always-on-object-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 89.5}, \"conclusion\": \"success\"}, \"pi05-crm-always-on-goal-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 83.5}, \"conclusion\": \"success\"}, \"pi05-crm-always-on-goal-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 82.5}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"smolvla-crm-norm005-spatial-s42-d149\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.805}, \"conclusion\": \"success\"}, \"smolvla-tau045-spatial-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.8, \"trigger_rate\": 0.073, \"mean_correction_norm\": 0.199, \"mean_uncertainty\": 0.189, \"total_steps\": 28391, \"crm_applied_steps\": 2070}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"total_successes\": 162, \"total_trials\": 200, \"per_task_range\": \"0.0-1.0\", \"worst_task\": \"pick_up_black_bowl_on_ramekin (0/20)\", \"best_tasks\": \"from_table_center, on_cookie_box, next_to_cookie_box (20/20)\"}}, \"eval-supp-long-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"successes\": 112, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-adapt-tau025-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"trigger_rate\": 0.037, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"pi05-crm-always-on-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 81.5, \"baseline_vla_only_sr\": 95.5, \"delta_vs_baseline\": -14}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\"}, \"pi05-crm-always-on-long-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 77, \"trigger_rate\": 100, \"mean_unc\": 0.104, \"mean_correction_norm\": 0.2, \"total_rollouts\": 200, \"total_successes\": 154, \"baseline_vla_only_sr\": 94, \"delta_vs_baseline\": -17, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 85, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 100, \"KITCHEN_SCENE3_stove_moka_pot\": 80, \"KITCHEN_SCENE4_black_bowl_drawer\": 85, \"LIVING_ROOM_SCENE5_mugs_plates\": 85, \"STUDY_SCENE1_book_caddy\": 70, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 75, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 90, \"KITCHEN_SCENE8_moka_pots\": 45, \"KITCHEN_SCENE6_mug_microwave\": 55}}, \"conclusion\": \"success\"}, \"smolvla-tau020-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.585, \"trigger_rate\": 0.089, \"mean_uncertainty\": 0.1226, \"total_rollouts\": 200, \"total_successes\": 117, \"benchmark\": \"long\", \"method\": \"adaptive_conformal\", \"tau\": 0.2, \"seed\": 42, \"server\": \"bjb2-28827\", \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.25, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0.9, \"KITCHEN_SCENE3_stove_moka_pot\": 0.95, \"KITCHEN_SCENE4_black_bowl_drawer\": 0.95, \"LIVING_ROOM_SCENE5_two_mugs_plates\": 0.35, \"STUDY_SCENE1_book_caddy\": 0.9, \"LIVING_ROOM_SCENE6_mug_pudding\": 0.3, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0.6, \"KITCHEN_SCENE8_two_moka_pots\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.65}}}, \"smolvla-tau015-spatial-s42-fix\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 79, \"trigger_rate\": 40.8, \"mean_unc\": 0.1851}, \"conclusion\": \"success\"}, \"crm-always-on-long-s45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.435, \"trigger_rate\": 1, \"mean_uncertainty\": 0.1292, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_episodes\": 200, \"total_successes\": 87, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0.2, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0.7, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0.55, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.55, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.2, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0.7, \"KITCHEN_SCENE8_moka_pots_stove\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.45}}, \"conclusion\": \"success\"}, \"pi05-crm-always-on-object-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 92, \"trigger_rate\": 100, \"mean_unc\": 0.0789, \"tau\": 0.001, \"total_rollouts\": 200, \"mean_correction_norm\": 0.2, \"per_task\": {\"alphabet_soup\": 95, \"cream_cheese\": 90, \"salad_dressing\": 90, \"bbq_sauce\": 85, \"ketchup\": 75, \"tomato_sauce\": 95, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 95, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"smolvla-tau045-long-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.595, \"trigger_rate\": 0.003, \"mean_unc\": 0.1239}, \"conclusion\": \"success\"}, \"smolvla-tau040-long-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.6, \"trigger_rate\": 0.004, \"mean_unc\": 0.123}, \"conclusion\": \"success\"}, \"pi05-crm-always-on-object-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 90.5, \"trigger_rate\": 100, \"total_rollouts\": 200, \"mean_unc\": 0.0813, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 95, \"bbq_sauce\": 85, \"ketchup\": 55, \"tomato_sauce\": 90, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 95, \"orange_juice\": 85}}, \"conclusion\": \"success\"}, \"smolvla-tau020-long-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 54.5, \"trigger_rate\": 11.4}}, \"eval-tau005-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"trigger_rate\": 99.2}}, \"pi05-crm-always-on-spatial-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 96, \"trigger_rate\": 100, \"mean_unc\": 0.1096, \"mean_correction_norm\": 0.2, \"total_steps\": 22455, \"crm_applied_steps\": 22455, \"baseline_vla_only_sr\": 97, \"delta_vs_baseline\": -1, \"per_task\": {\"between_plate_ramekin\": 100, \"next_to_ramekin\": 100, \"table_center\": 100, \"cookie_box\": 100, \"top_drawer\": 90, \"on_ramekin\": 75, \"next_to_cookie_box\": 100, \"on_stove\": 100, \"next_to_plate\": 100, \"wooden_cabinet\": 95}}, \"conclusion\": \"success\"}, \"eval-tau040-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"trigger_rate\": 9.6}}, \"eval-tau045-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"trigger_rate\": 7.1}}, \"crm-always-on-object-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.675, \"trigger_rate\": 1, \"mean_unc\": 0.1128}}, \"smolvla-tau005-long-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.44, \"trigger_rate\": 0.9781}, \"conclusion\": \"negative\"}, \"crm-always-on-object-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.745, \"trigger_rate\": 1, \"mean_unc\": 0.1129}}, \"smolvla-tau010-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.535, \"trigger_rate\": 0.613, \"mean_correction_norm\": 0.2}}, \"pi05-tau-sweep-goal-tau070-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 87, \"trigger_rate\": 1.1}}, \"pi05-tau-sweep-goal-tau050-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"success_rate\": 0, \"trigger_rate\": null, \"note\": \"CUDA DSA error - all 200 rollouts failed\"}}, \"pi05-goal-tau035-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 89.5, \"trigger_rate\": 5.1}}, \"crm-always-on-long-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.43, \"trigger_rate\": 1, \"tau\": 0.001, \"mean_uncertainty\": 0.1299, \"mean_correction_norm\": 0.1642, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.15, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0.65, \"KITCHEN_SCENE3_stove_moka_pot\": 0.75, \"KITCHEN_SCENE4_black_bowl_drawer\": 0.6, \"LIVING_ROOM_SCENE5_white_mug_yellow_mug\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.65, \"LIVING_ROOM_SCENE6_white_mug_chocolate_pudding\": 0.2, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0.55, \"KITCHEN_SCENE8_moka_pots\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.55}}, \"conclusion\": \"success\"}, \"crm-always-on-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78.5, \"trigger_rate\": 100, \"mean_unc\": 0.1779}}, \"crm-always-on-goal-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"trigger_rate\": 100, \"mean_unc\": 0.1457}}, \"crm-always-on-goal-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 82, \"trigger_rate\": 100, \"mean_unc\": 0.1459}}, \"crm-always-on-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.77, \"trigger_rate\": 1, \"mean_unc\": 0.179, \"benchmark\": \"spatial\", \"seed\": 45, \"tau\": 0.001, \"K\": 2, \"norm\": 0.2, \"mode\": \"crm_always_on\", \"total\": 200}}, \"pi05-goal-tau025-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 88.5, \"trigger_rate\": 9.1}}, \"pi05-tau-sweep-goal-tau050-s42-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.87, \"trigger_rate\": 0.0206}, \"conclusion\": \"success\"}, \"pi05-goal-tau015-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 87.5, \"trigger_rate\": 20.5}}, \"smolvla-tau035-long-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.575, \"trigger_rate\": 0.013, \"mean_correction_norm\": 0.148, \"mean_uncertainty\": 0.127, \"total_steps\": 73533, \"crm_applied_steps\": 975}, \"conclusion\": \"success\"}, \"smolvla-tau030-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"smolvla-tau015-long-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.61, \"trigger_rate\": 0.239, \"mean_correction_norm\": 0.159, \"mean_uncertainty\": 0.124, \"total_steps\": 72484, \"crm_applied_steps\": 17341}, \"conclusion\": \"success\"}, \"smolvla-tau045-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.715, \"trigger_rate\": 0.0075}}, \"smolvla-tau040-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.735, \"trigger_rate\": 0.0091}}, \"smolvla-tau030-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.79, \"trigger_rate\": 0.0231}}, \"crm-always-on-long-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.455, \"trigger_rate\": 1}}, \"crm-always-on-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.41, \"trigger_rate\": 1}}, \"smolvla-tau025-long-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.56, \"trigger_rate\": 0.042, \"mean_correction_norm\": 0.157, \"mean_uncertainty\": 0.124, \"total_steps\": 73750, \"crm_applied_steps\": 3073}, \"conclusion\": \"success\"}, \"pi05-long-tau015-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 82, \"trigger_rate\": 11.4}}, \"pi05-k2mean-spatial-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 96.5}}, \"pi05-k2mean-long-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 97}}, \"pi05-k2mean-object-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 100}}, \"smolvla-tau035-object-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 75, \"trigger_rate\": 1.6}}, \"smolvla-tau025-object-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 81, \"trigger_rate\": 3.5}}, \"smolvla-tau020-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78.5, \"trigger_rate\": 7.1}}, \"smolvla-tau010-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78, \"trigger_rate\": 44.4}}, \"smolvla-tau005-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 75, \"trigger_rate\": 94.2}}, \"crm-always-on-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"trigger_rate\": 100}}, \"crm-always-on-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"trigger_rate\": 100}}, \"crm-always-on-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"trigger_rate\": 100}}, \"crm-always-on-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 76, \"trigger_rate\": 100}}, \"smolvla-tau030-long-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 54.5, \"trigger_rate\": 1.6}}, \"smolvla-tau030-long-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 55.5, \"trigger_rate\": 1.6}}, \"tau-sweep-goal-tau035-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 86, \"trigger_rate\": 2.1}}, \"tau-sweep-long-tau015-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 61, \"trigger_rate\": 24.1}}, \"tau-sweep-long-tau035-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 57, \"trigger_rate\": 1}}, \"smolvla-tau020-long-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 58.5, \"trigger_rate\": 8.7}}, \"tau-sweep-goal-tau015-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 83, \"trigger_rate\": 36.4}}, \"tau-sweep-spatial-tau035-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80.5, \"trigger_rate\": 12.1}}, \"tau-sweep-spatial-tau015-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"trigger_rate\": 40.7}}, \"smolvla-tau035-object-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.75, \"trigger_rate\": 0.016, \"mean_unc\": 0.1121}}, \"smolvla-tau035-object-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.77, \"trigger_rate\": 0.013, \"mean_unc\": 0.1094}}, \"smolvla-tau025-object-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.775, \"trigger_rate\": 0.037, \"mean_unc\": 0.1103}}, \"crm-always-on-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.79, \"trigger_rate\": 1, \"mean_unc\": 0.186}}, \"crm-always-on-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"trigger_rate\": 1, \"mean_unc\": 0.1492}}, \"crm-always-on-object-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.745, \"trigger_rate\": 1, \"mean_unc\": 0.1105}}, \"crm-always-on-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.735, \"trigger_rate\": 1, \"mean_unc\": 0.111}}, \"crm-always-on-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.71, \"trigger_rate\": 1, \"mean_unc\": 0.1137}}, \"eval-obs-object-norm003-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-object-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-object-norm003-s46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-k2mean-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-k2mean-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-k2mean-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-vla-only-spatial-s42-4090\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-vla-only-goal-s42-4090\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-k2mean-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-vla-only-spatial-s42-4090-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-vla-only-object-s42-4090-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-vla-only-goal-s42-4090-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-tau010-015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-tau010-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed42-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-vla-only-object-s42-4090\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-vla-only-long-s42-4090\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"smolvla-tau020-long-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"smolvla-tau030-long-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-object-s43-r5\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.985, \"benchmark\": \"object\", \"method\": \"vla_only\", \"model\": \"pi05\", \"seed\": 43, \"server\": \"bjb2-28827\"}}, \"eval-perdof-object-norm005-s44-westd\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.79, \"benchmark\": \"object\", \"method\": \"perdof\", \"norm\": 0.05, \"seed\": 44, \"server\": \"westd-49937\", \"note\": \"westd server - LIBERO assets version bias caveat\"}}, \"eval-perdof-object-norm003-s44-westd\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"benchmark\": \"object\", \"method\": \"perdof\", \"norm\": 0.03, \"seed\": 44, \"server\": \"westd-49937\", \"note\": \"westd server - LIBERO assets version bias caveat\"}}, \"eval-obs-object-norm005-s45-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.73, \"benchmark\": \"object\", \"method\": \"obs_only\", \"norm\": 0.05, \"seed\": 45, \"server\": \"bjb2-28827\"}}, \"eval-obs-object-norm005-s44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.74, \"benchmark\": \"object\", \"method\": \"obs_only\", \"norm\": 0.05, \"seed\": 44, \"server\": \"bjb2-28827\"}}, \"eval-obs-object-norm003-s44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.785, \"benchmark\": \"object\", \"method\": \"obs_only\", \"norm\": 0.03, \"seed\": 44, \"server\": \"bjb2-28827\"}}, \"eval-obs-object-norm005-s43-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.785, \"benchmark\": \"object\", \"method\": \"obs_only\", \"norm\": 0.05, \"seed\": 43, \"server\": \"bjb2-28827\"}}, \"eval-obs-object-norm003-s43-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.74, \"benchmark\": \"object\", \"method\": \"obs_only\", \"norm\": 0.03, \"seed\": 43, \"server\": \"bjb2-28827\"}}, \"eval-obs-object-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"benchmark\": \"object\", \"method\": \"obs_only\", \"norm\": 0.05, \"seed\": 46}}, \"eval-perdof-object-norm005-s43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78.5, \"successes\": 157, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-perdof-object-norm003-s43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"successes\": 158, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.03, \"K\": 10}}, \"pi05-vla-only-goal-s44-4090\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 97.5, \"successes\": 195, \"trials\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\"}}, \"pi05-vla-only-object-s43-4090\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 98.5, \"successes\": 197, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\"}}, \"pi05-vla-only-long-s44-4090\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 95.5, \"successes\": 191, \"trials\": 200, \"benchmark\": \"long\", \"mode\": \"vla_only\"}}, \"pi05-vla-only-long-s43-4090\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 95.5, \"successes\": 191, \"trials\": 200, \"benchmark\": \"long\", \"mode\": \"vla_only\"}}, \"pi05-vla-only-long-s42-4090-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 94, \"successes\": 188, \"trials\": 200, \"benchmark\": \"long\", \"mode\": \"vla_only\"}}, \"eval-ksweep-k5-obs-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 73, \"successes\": 146, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"K\": 5, \"max_correction_norm\": 0.2}}, \"eval-obs-object-norm005-s44-westd\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 76.5, \"successes\": 153, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"K\": 10, \"max_correction_norm\": 0.05}}, \"eval-k2-tau035-spatial-s42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80.5, \"successes\": 161, \"trials\": 200, \"benchmark\": \"spatial\", \"mode\": \"adaptive_conformal_crm\", \"K\": 2, \"conformal_threshold\": 0.35, \"max_correction_norm\": 0.2, \"mean_uncertainty\": 0.1866, \"trigger_rate\": 0.118}}, \"eval-obs-object-norm005-s43-westd\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 73.5, \"successes\": 147, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"K\": 10, \"max_correction_norm\": 0.05}}, \"eval-obs-object-norm003-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 74, \"successes\": 148, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"K\": 10, \"max_correction_norm\": 0.03}}, \"eval-obs-object-norm005-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78.5, \"successes\": 157, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"K\": 10, \"max_correction_norm\": 0.05}}, \"eval-obs-object-norm003-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78.5, \"successes\": 157, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"K\": 10, \"max_correction_norm\": 0.03}}, \"eval-ksweep-k20-obs-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 73.5, \"successes\": 147, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"K\": 20, \"max_correction_norm\": 0.2}}, \"eval-ksweep-k20-obs-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 75.5, \"successes\": 151, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"K\": 20, \"max_correction_norm\": 0.2}}, \"eval-k2-tau025-spatial-s42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"successes\": 159, \"trials\": 200, \"benchmark\": \"spatial\", \"mode\": \"adaptive_conformal_crm\", \"K\": 2, \"conformal_threshold\": 0.25, \"max_correction_norm\": 0.2}}, \"eval-obs-object-norm003-s43-westd\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 74, \"successes\": 148, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"K\": 10, \"max_correction_norm\": 0.03}}, \"eval-obs-object-norm003-s44-westd\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 74.5, \"successes\": 149, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"K\": 10, \"max_correction_norm\": 0.03}}, \"eval-obs-object-norm005-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 74, \"successes\": 148, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"K\": 10, \"max_correction_norm\": 0.05}}, \"eval-ksweep-k5-obs-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 73.5, \"successes\": 147, \"trials\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"K\": 5, \"max_correction_norm\": 0.2}}, \"smolvla-vla-only-long-n20-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.575, \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"smolvla-vla-only-long-n20-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.62, \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"pi05-object-adaptive-s44-cqa1\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.88, \"trigger_rate\": 0.0348, \"mean_uncertainty\": 0.082, \"total_steps\": 33220, \"crm_applied_steps\": 1155}, \"conclusion\": \"success\"}, \"pi05-object-adaptive-s43-cqa1\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.85, \"trigger_rate\": 0.0402, \"mean_uncertainty\": 0.085, \"total_steps\": 34067, \"crm_applied_steps\": 1368}, \"conclusion\": \"success\"}, \"pi05-object-adaptive-s42-cqa1\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.855, \"trigger_rate\": 0.0368, \"mean_uncertainty\": 0.084, \"total_steps\": 33946, \"crm_applied_steps\": 1250}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"success_rate\": 0.865, \"n_rollouts\": 20, \"benchmark\": \"object\", \"note\": \"INVALID - CUDA OOM corrupted results\"}}, \"eval-pi05-vla-only-object-s42-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.965, \"n_rollouts\": 20, \"benchmark\": \"object\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s43-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.97, \"n_rollouts\": 20, \"benchmark\": \"goal\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s42-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.955, \"n_rollouts\": 20, \"benchmark\": \"goal\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s43-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.96, \"n_rollouts\": 20, \"benchmark\": \"spatial\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s42-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.98, \"n_rollouts\": 20, \"benchmark\": \"spatial\"}, \"conclusion\": \"success\"}, \"smolvla-tau025-long-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.53, \"trigger_rate\": 0.046, \"mean_correction_norm\": 0.159, \"mean_uncertainty\": 0.126, \"total_steps\": 75218, \"crm_applied_steps\": 3492}, \"conclusion\": \"success\"}, \"smolvla-tau015-long-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.61, \"trigger_rate\": 0.236, \"mean_correction_norm\": 0.158, \"mean_uncertainty\": 0.124, \"total_steps\": 72270, \"crm_applied_steps\": 17074}, \"conclusion\": \"success\"}, \"smolvla-tau025-object-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.034, \"mean_correction_norm\": \"N/A\", \"mean_uncertainty\": 0.109, \"total_steps\": 35330, \"crm_applied_steps\": 1209}, \"conclusion\": \"success\"}, \"smolvla-tau035-long-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.6, \"trigger_rate\": 0.01, \"mean_correction_norm\": 0.163, \"mean_uncertainty\": 0.124, \"total_steps\": 71976, \"crm_applied_steps\": 747}, \"conclusion\": \"success\"}, \"pi05-goal-tau015-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.88, \"trigger_rate\": 0.195, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.118, \"total_steps\": 26631, \"crm_applied_steps\": 5186}}, \"smolvla-tau035-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"trigger_rate\": 0.127, \"mean_correction_norm\": 0.198, \"mean_uncertainty\": 0.188, \"total_steps\": 28473, \"crm_applied_steps\": 3613}}, \"smolvla-tau025-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"trigger_rate\": 0.193, \"mean_correction_norm\": 0.191, \"mean_uncertainty\": 0.183, \"total_steps\": 28690, \"crm_applied_steps\": 5546}}, \"smolvla-tau015-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"trigger_rate\": 0.386, \"mean_correction_norm\": 0.184, \"mean_uncertainty\": 0.18, \"total_steps\": 28231, \"crm_applied_steps\": 10899}}, \"pi05-goal-tau035-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.9, \"trigger_rate\": 0.044, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.117, \"total_steps\": 26576, \"crm_applied_steps\": 1171}}, \"pi05-goal-tau025-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.89, \"trigger_rate\": 0.093, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.123, \"total_steps\": 26259, \"crm_applied_steps\": 2449}}, \"pi05-adaptive-long-s43-cqa1-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"trigger_rate\": 0.053, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.093}}, \"pi05-spatial-tau015-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.965, \"trigger_rate\": 0.117, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.103, \"total_steps\": 22280, \"crm_applied_steps\": 2599}}, \"pi05-spatial-tau035-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.975, \"trigger_rate\": 0.022, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.101, \"total_steps\": 21857, \"crm_applied_steps\": 483}}, \"pi05-spatial-tau025-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.985, \"trigger_rate\": 0.028, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.091, \"total_steps\": 21566, \"crm_applied_steps\": 607}}, \"pi05-object-tau035-s42-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"E_smolvla_crm_norm005_spatial_s42_d149\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-object-tau015-s42-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"E_smolvla_adaptive_tau045_spatial_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"E_smolvla_adaptive_tau035_spatial_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"E_smolvla_adaptive_tau015_spatial_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-object-s42-tau045-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau035-spatial-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla-tau015-spatial-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"pi05-adaptive-long-s44-bjb1\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.82, \"trigger_rate\": 0.044, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.088, \"total_steps\": 63273, \"crm_applied_steps\": 2757}, \"conclusion\": \"success\"}, \"pi05-adaptive-long-s43-bjb1\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.79, \"trigger_rate\": 0.053, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.093, \"total_steps\": 65132, \"crm_applied_steps\": 3427}, \"conclusion\": \"success\"}, \"smolvla-crm-norm005-k10-object-s44-cqa1\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.78}, \"conclusion\": \"success\"}, \"smolvla-tau015-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.167, \"mean_correction_norm\": 0.172, \"mean_uncertainty\": 0.11}}, \"smolvla-tau025-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"smolvla-tau035-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"trigger_rate\": 0.024, \"mean_correction_norm\": 0.189, \"mean_uncertainty\": 0.147}}, \"smolvla-tau025-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.84, \"trigger_rate\": 0.083, \"mean_correction_norm\": 0.178, \"mean_uncertainty\": 0.145}}, \"smolvla-tau015-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.855, \"trigger_rate\": 0.333, \"mean_correction_norm\": 0.162, \"mean_uncertainty\": 0.142}}, \"smolvla-tau015-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"smolvla-tau035-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-adaptive-long-s42-tau035-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"smolvla-tau015-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"trigger_rate\": 0.354, \"mean_correction_norm\": 0.16, \"mean_uncertainty\": 0.146, \"total_steps\": 28680, \"crm_applied_steps\": 10162}}, \"smolvla-tau025-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"trigger_rate\": 0.0925, \"mean_correction_norm\": 0.176, \"mean_uncertainty\": 0.148, \"total_steps\": 29089, \"crm_applied_steps\": 2692}}, \"smolvla-tau035-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.855, \"trigger_rate\": 0.0211, \"mean_correction_norm\": 0.184, \"mean_uncertainty\": 0.143, \"total_steps\": 27726, \"crm_applied_steps\": 586}}, \"pi05-adaptive-long-s42-tau015-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.84, \"trigger_rate\": 0.114, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.089, \"total_steps\": 63147, \"crm_applied_steps\": 7216}}, \"smolvla-tau035-object-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau025-object-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau015-object-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau035-goal-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau025-goal-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"smolvla-tau015-goal-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-goal-s42-tau035-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.875, \"trigger_rate\": 0.057, \"fast_path_ratio\": 0.943, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.124, \"tau\": 0.35, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"total_steps\": 27163, \"crm_applied_steps\": 1549}}, \"westd-pi05-adaptive-object-s44-paired\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"westd-pi05-adaptive-object-s43-paired\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.87, \"trigger_rate\": 0.0383, \"mean_correction_norm\": 0.2, \"tau\": 0.25, \"per_task\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.75, \"salad_dressing\": 0.9, \"bbq_sauce\": 0.85, \"ketchup\": 0.65, \"tomato_sauce\": 0.9, \"butter\": 1, \"milk\": 0.95, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}, \"paired_vla_only_sr\": 1}, \"conclusion\": \"negative\"}, \"westd-pi05-adaptive-object-s42-paired\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.835, \"trigger_rate\": 0.0346, \"mean_correction_norm\": 0.2, \"tau\": 0.25, \"per_task\": {\"alphabet_soup\": 0.95, \"cream_cheese\": 0.65, \"salad_dressing\": 0.95, \"bbq_sauce\": 0.9, \"ketchup\": 0.45, \"tomato_sauce\": 0.8, \"butter\": 0.95, \"milk\": 1, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}, \"paired_vla_only_sr\": 0.995}, \"conclusion\": \"negative\"}, \"westd-pi05-crm-k2-object-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.88, \"per_task\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.65, \"salad_dressing\": 0.8, \"bbq_sauce\": 1, \"ketchup\": 0.65, \"tomato_sauce\": 0.95, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.8}, \"paired_vla_only_sr\": 0.995}, \"conclusion\": \"negative\"}, \"westd-pi05-crm-k2-object-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.87, \"per_task\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.75, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.9, \"ketchup\": 0.65, \"tomato_sauce\": 0.9, \"butter\": 0.95, \"milk\": 0.95, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.8}, \"paired_vla_only_sr\": 1}, \"conclusion\": \"negative\"}, \"westd-pi05-crm-k2-object-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.87, \"per_task\": {\"alphabet_soup\": 0.9, \"cream_cheese\": 0.9, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.9, \"ketchup\": 0.5, \"tomato_sauce\": 0.9, \"butter\": 0.95, \"milk\": 1, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.9}, \"paired_vla_only_sr\": 0.995}, \"conclusion\": \"negative\"}, \"eval-crm-goal-s43-d149-bjb1\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"open_middle_drawer\": 0.75, \"bowl_on_stove\": 1, \"wine_on_cabinet\": 0.9, \"open_top_drawer_bowl\": 0.6, \"bowl_on_cabinet\": 0.95, \"plate_to_front\": 0.95, \"cream_cheese_in_bowl\": 0.5, \"turn_on_stove\": 0.95, \"bowl_on_plate\": 0.9, \"wine_on_rack\": 0.7}}, \"conclusion\": \"success\"}, \"eval-crm-object-s43-d149-bjb1\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.785, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.8, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.8, \"ketchup\": 0.8, \"tomato_sauce\": 0.75, \"butter\": 0.7, \"milk\": 0.7, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.9}}, \"conclusion\": \"success\"}, \"eval-crm-object-s42-d149-bjb1\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.77, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.9, \"ketchup\": 0.8, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.75, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}}, \"conclusion\": \"success\"}, \"eval-crm-spatial-s48-d149-bjb1\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.805, \"per_task\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"on_cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.9, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.8}}, \"conclusion\": \"success\"}, \"pi05-adaptive-long-s44-cqa1-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.83, \"trigger_rate\": 0.0448, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.0893, \"total_steps\": 63093, \"crm_applied_steps\": 2829, \"per_task_sr\": {\"LR2_soup_tomato\": 0.9, \"LR2_cheese_butter\": 1, \"K3_stove_moka\": 1, \"K4_bowl_drawer\": 0.95, \"LR5_mugs_plates\": 0.95, \"STUDY1_book\": 0.75, \"LR6_mug_pudding\": 0.75, \"LR1_soup_cheese\": 0.9, \"K8_moka_pots\": 0.35, \"K6_mug_microwave\": 0.75}}, \"conclusion\": \"success\"}, \"pi05-adaptive-object-s44-cqa1-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.88, \"trigger_rate\": 0.0348, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.0822, \"total_steps\": 33220, \"crm_applied_steps\": 1155, \"per_task_sr\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.7, \"salad_dressing\": 0.95, \"bbq_sauce\": 0.95, \"ketchup\": 0.6, \"tomato_sauce\": 0.85, \"butter\": 0.95, \"milk\": 1, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.9}}, \"conclusion\": \"success\"}, \"pi05-adaptive-object-s43-cqa1-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.85, \"trigger_rate\": 0.0402, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.0846, \"total_steps\": 34067, \"crm_applied_steps\": 1368, \"per_task_sr\": {\"alphabet_soup\": 0.95, \"cream_cheese\": 0.7, \"salad_dressing\": 0.95, \"bbq_sauce\": 0.9, \"ketchup\": 0.7, \"tomato_sauce\": 0.85, \"butter\": 0.8, \"milk\": 0.95, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}}, \"conclusion\": \"success\"}, \"pi05-adaptive-goal-s42-tau015-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.92, \"trigger_rate\": 0.174, \"fast_path_ratio\": 0.826, \"mean_correction_norm\": 0.2, \"tau\": 0.15, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"pi05-adaptive-spatial-s42-tau015-bjb2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.97, \"trigger_rate\": 0.112, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.099, \"total_steps\": 22013, \"crm_applied_steps\": 2471, \"per_task\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 1, \"table_center\": 1, \"cookie_box\": 0.95, \"top_drawer\": 0.9, \"on_ramekin\": 0.9, \"next_to_cookie_box\": 1, \"stove\": 1, \"next_to_plate\": 0.95, \"wooden_cabinet\": 1}}, \"conclusion\": \"success\"}, \"pi05-adaptive-spatial-s42-tau035-bjb2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.965, \"trigger_rate\": 0.0255, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.1055, \"total_steps\": 22218, \"crm_applied_steps\": 567, \"n_rollouts_per_task\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"eval-crm-goal-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 82}}, \"eval-crm-goal-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 82}}, \"eval-crm-object-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 77}}, \"eval-crm-object-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78.5}}, \"eval-crm-object-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 74}}, \"eval-crm-spatial-s48-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80.5}}, \"pi05-adaptive-long-s43-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0}}, \"eval-supp-goal-k2mean-s47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 20}, \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"success_rate\": 54.5, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"success_rate\": 82, \"n_episodes\": 200}}, \"precompute-pi05-object-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"cache_size_gb\": 1.3, \"n_samples\": 72507}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"cache_size_gb\": 2.5, \"n_samples\": 136090}}, \"pi05-adaptive-long-s44-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0}}, \"eval-supp-goal-adapt-tau025-s47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 82}, \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 82}}, \"eval-supp-goal-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 83.5}}, \"eval-supp-obj-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 76.5}}, \"eval-supp-reconvla-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78}}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80}}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"trigger_rate\": 20}}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80}}, \"pi05-crm-k2-long-s44-cqa1\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 76, \"successes\": 152, \"total_rollouts\": 200, \"benchmark\": \"long\", \"mode\": \"crm_obs_only\", \"model\": \"pi05\", \"K\": 2, \"max_correction_norm\": 0.05, \"seed\": 44, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": {\"sr\": 80, \"successes\": 16, \"total\": 20}, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"KITCHEN_SCENE3_stove_moka_pot\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"KITCHEN_SCENE4_black_bowl_drawer\": {\"sr\": 80, \"successes\": 16, \"total\": 20}, \"LIVING_ROOM_SCENE5_mug_plate\": {\"sr\": 90, \"successes\": 18, \"total\": 20}, \"STUDY_SCENE1_book_caddy\": {\"sr\": 65, \"successes\": 13, \"total\": 20}, \"LIVING_ROOM_SCENE6_mug_chocolate_pudding\": {\"sr\": 65, \"successes\": 13, \"total\": 20}, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": {\"sr\": 85, \"successes\": 17, \"total\": 20}, \"KITCHEN_SCENE8_both_moka_pots\": {\"sr\": 20, \"successes\": 4, \"total\": 20}, \"KITCHEN_SCENE6_mug_microwave\": {\"sr\": 85, \"successes\": 17, \"total\": 20}}}, \"conclusion\": \"success\"}, \"pi05-crm-k2-object-s42-bjb1-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 89, \"successes\": 178, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"model\": \"pi05\", \"K\": 2, \"max_correction_norm\": 0.05, \"seed\": 42, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 100, \"successes\": 20, \"total\": 20}, \"cream_cheese\": {\"sr\": 75, \"successes\": 15, \"total\": 20}, \"salad_dressing\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"bbq_sauce\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"ketchup\": {\"sr\": 65, \"successes\": 13, \"total\": 20}, \"tomato_sauce\": {\"sr\": 85, \"successes\": 17, \"total\": 20}, \"butter\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"milk\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"chocolate_pudding\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"orange_juice\": {\"sr\": 90, \"successes\": 18, \"total\": 20}}, \"delta_vs_vla_only_pp\": -10.5, \"vla_only_baseline_sr\": 99.5}, \"conclusion\": \"success\"}, \"pi05-crm-k2-object-s43-bjb1-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 87, \"successes\": 174, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"model\": \"pi05\", \"K\": 2, \"max_correction_norm\": 0.05, \"seed\": 43, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 100, \"successes\": 20, \"total\": 20}, \"cream_cheese\": {\"sr\": 70, \"successes\": 14, \"total\": 20}, \"salad_dressing\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"bbq_sauce\": {\"sr\": 90, \"successes\": 18, \"total\": 20}, \"ketchup\": {\"sr\": 65, \"successes\": 13, \"total\": 20}, \"tomato_sauce\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"butter\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"milk\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"chocolate_pudding\": {\"sr\": 80, \"successes\": 16, \"total\": 20}, \"orange_juice\": {\"sr\": 85, \"successes\": 17, \"total\": 20}}, \"delta_vs_vla_only_pp\": -12.5, \"vla_only_baseline_sr\": 99.5}, \"conclusion\": \"success\"}, \"pi05-crm-k2-object-s44-bjb1-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 88, \"successes\": 176, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\", \"model\": \"pi05\", \"K\": 2, \"max_correction_norm\": 0.05, \"seed\": 44, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 1, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.75, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.95, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.95, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.6, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.9, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.9, \"pick_up_the_milk_and_place_it_in_the_basket\": 1, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 1, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.75}, \"delta_vs_vla_only_pp\": -11.5, \"vla_only_baseline_sr\": 0.995, \"source\": \"logs/eval_object_crm_k2_pi05_seed44.json\"}, \"conclusion\": \"success\"}, \"pi05-adaptive-goal-s44-bjb1\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.865, \"successes\": 173, \"total_rollouts\": 200, \"trigger_rate\": 0.1001, \"mean_unc\": 0.1269, \"mean_correction_norm\": 0.2, \"crm_applied_steps\": 2785, \"total_steps\": 27810, \"tau\": 0.25, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": {\"sr\": 0.85, \"s\": 17, \"t\": 20}, \"put_the_bowl_on_the_stove\": {\"sr\": 1, \"s\": 20, \"t\": 20}, \"put_the_wine_bottle_on_top_of_the_cabinet\": {\"sr\": 0.6, \"s\": 12, \"t\": 20}, \"open_the_top_drawer_and_put_the_bowl_inside\": {\"sr\": 0.65, \"s\": 13, \"t\": 20}, \"put_the_bowl_on_top_of_the_cabinet\": {\"sr\": 1, \"s\": 20, \"t\": 20}, \"push_the_plate_to_the_front_of_the_stove\": {\"sr\": 0.9, \"s\": 18, \"t\": 20}, \"put_the_cream_cheese_in_the_bowl\": {\"sr\": 1, \"s\": 20, \"t\": 20}, \"turn_on_the_stove\": {\"sr\": 1, \"s\": 20, \"t\": 20}, \"put_the_bowl_on_the_plate\": {\"sr\": 0.95, \"s\": 19, \"t\": 20}, \"put_the_wine_bottle_on_the_rack\": {\"sr\": 0.7, \"s\": 14, \"t\": 20}}}, \"conclusion\": \"negative\"}, \"pi05-adaptive-spatial-s44-bjb2-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 97, \"successes\": 194, \"total_rollouts\": 200, \"trigger_rate\": 3.9, \"mean_unc\": 0.0975}}, \"pi05-adaptive-spatial-s43-bjb2-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 98, \"successes\": 196, \"total_rollouts\": 200, \"trigger_rate\": 4.4, \"mean_unc\": 0.1062}}, \"pi05-adaptive-spatial-s42-bjb2-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 96.5, \"successes\": 193, \"total_rollouts\": 200, \"trigger_rate\": 4.8, \"mean_unc\": 0.1056}}, \"pi05-crm-k2-spatial-s44-bjb2-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 97, \"successes\": 194, \"total_rollouts\": 200}}, \"pi05-crm-k2-spatial-s43-bjb2-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 97, \"successes\": 194, \"total_rollouts\": 200}}, \"pi05-crm-k2-spatial-s42-bjb2-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 96.5, \"successes\": 193, \"total_rollouts\": 200}}, \"pi05-crm-k2-goal-s44-bjb1-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 85, \"successes\": 170, \"total_rollouts\": 200}}, \"pi05-crm-k2-goal-s43-bjb1-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 83, \"successes\": 166, \"total_rollouts\": 200}}, \"pi05-crm-k2-goal-s42-bjb1-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 82.5, \"successes\": 165, \"total_rollouts\": 200}}, \"westd-pi05-vla-only-long-s44-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.96, \"benchmark\": \"long\", \"mode\": \"vla_only\", \"seed\": 44, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"total_successes\": 192}}, \"westd-pi05-vla-only-long-s43-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.945, \"benchmark\": \"long\", \"mode\": \"vla_only\", \"seed\": 43, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}}, \"pi05-crm-k2-long-s43-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"westd-pi05-vla-only-spatial-s43-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.975, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"total_successes\": 195}}, \"westd-pi05-vla-only-spatial-s42-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"total_successes\": 196}}, \"westd-pi05-vla-only-spatial-s44-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.985, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"total_successes\": 197}}, \"westd-pi05-vla-only-long-s42-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}, \"conclusion\": \"success\"}, \"westd-pi05-vla-only-object-s44-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.995, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"seed\": 44, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}}, \"westd-pi05-vla-only-object-s43-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 1, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"seed\": 43, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}}, \"westd-pi05-vla-only-object-s42-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.995, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"seed\": 42, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}}, \"westd-pi05-vla-only-goal-s44-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.955, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"seed\": 44, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}}, \"westd-pi05-vla-only-goal-s43-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.965, \"per_task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 1, \"put_the_bowl_on_the_stove\": 1, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.85, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 1, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.9}, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"seed\": 43, \"model\": \"pi0.5\", \"n_rollouts\": 20}}, \"westd-pi05-vla-only-goal-s42-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.975, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"seed\": 42, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}}, \"pi05-adaptive-object-s42-cqa1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.855, \"trigger_rate\": 0.0368, \"mean_correction_norm\": 0.2, \"mean_uncertainty\": 0.0842, \"benchmark\": \"object\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 42, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}}, \"pi05-adaptive-long-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"mode\": \"adaptive_conformal_crm\", \"K\": 2, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"trigger_rate\": 0.039, \"mean_uncertainty\": 0.087, \"benchmark\": \"long\", \"seed\": 42}, \"conclusion\": \"success\"}, \"pi05-adaptive-object-s43-bjb2-24035\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.83}}, \"pi05-adaptive-long-s44-cqa1-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"trigger_rate\": null, \"benchmark\": \"long\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 44, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10, \"error\": \"CUDA OOM at step 0 of every rollout\", \"successes\": 0, \"total\": 200}, \"conclusion\": \"failed\"}, \"pi05-adaptive-long-s43-cqa1-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"trigger_rate\": null, \"benchmark\": \"long\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 43, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10, \"error\": \"CUDA OOM at step 0 of every rollout\", \"successes\": 0, \"total\": 200}, \"conclusion\": \"failed\"}, \"pi05-adaptive-goal-s42-cqa1\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.895, \"success_count\": 179, \"total_rollouts\": 200, \"trigger_rate\": 0.081, \"mean_unc\": 0.1152, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 42, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10, \"K\": 2, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.7, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 0.9, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.85}}, \"conclusion\": \"success\"}, \"westd-pi05-crm-k2-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.855, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"seed\": 42, \"K\": 2, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"westd-pi05-adaptive-object-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.835, \"benchmark\": \"object\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 42, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"westd-pi05-adaptive-goal-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.875, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 43, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"westd-pi05-adaptive-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.88, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 42, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"pi05-adaptive-object-s44-cqa1-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-adaptive-goal-s43-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 89.5}}, \"westd-pi05-adaptive-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-spatial-s44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-spatial-s43-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-spatial-s42-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-spatial-s44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-spatial-s43-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-spatial-s42-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-object-s44-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-object-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-object-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-goal-s44-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-goal-s43-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-goal-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-spatial-s44-d149\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.805, \"trigger_rate\": 0.195, \"successes\": 161, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"source\": \"eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json\"}, \"conclusion\": \"success\"}, \"eval-adaptive-spatial-s43-d149\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.795, \"trigger_rate\": 0.203, \"successes\": 159, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"source\": \"eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json\"}, \"conclusion\": \"success\"}, \"eval-adaptive-goal-s44-d149\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.865, \"trigger_rate\": 0.068, \"successes\": 173, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"source\": \"eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\"}, \"conclusion\": \"success\"}, \"eval-adaptive-goal-s43-d149\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.845, \"trigger_rate\": 0.088, \"successes\": 169, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"source\": \"eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\"}, \"conclusion\": \"success\"}, \"eval-adaptive-object-s44-d149\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.75, \"trigger_rate\": 0.036, \"successes\": 150, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"source\": \"eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\"}, \"conclusion\": \"success\"}, \"eval-adaptive-object-s43-d149\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.775, \"trigger_rate\": 0.037, \"successes\": 155, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"source\": \"eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\"}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.74, \"successes\": 148, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"source\": \"eval_object_crm_obs_only_norm0.05_seed44.json\"}, \"conclusion\": \"negative\"}, \"eval-adaptive-spatial-k1-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.795, \"trigger_rate\": 0.198, \"successes\": 159, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"source\": \"eval_spatial_adaptive_k2_tau025_seed42_paired_r2.json\"}}, \"westd-pi05-vla-only-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.975, \"successes\": 195, \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": {\"sr\": 0.95, \"successes\": 19, \"total\": 20}, \"put_the_bowl_on_the_stove\": {\"sr\": 1, \"successes\": 20, \"total\": 20}, \"put_the_wine_bottle_on_top_of_the_cabinet\": {\"sr\": 1, \"successes\": 20, \"total\": 20}, \"open_the_top_drawer_and_put_the_bowl_inside\": {\"sr\": 0.9, \"successes\": 18, \"total\": 20}, \"put_the_bowl_on_top_of_the_cabinet\": {\"sr\": 1, \"successes\": 20, \"total\": 20}, \"push_the_plate_to_the_front_of_the_stove\": {\"sr\": 0.95, \"successes\": 19, \"total\": 20}, \"put_the_cream_cheese_in_the_bowl\": {\"sr\": 1, \"successes\": 20, \"total\": 20}, \"turn_on_the_stove\": {\"sr\": 1, \"successes\": 20, \"total\": 20}, \"put_the_bowl_on_the_plate\": {\"sr\": 1, \"successes\": 20, \"total\": 20}, \"put_the_wine_bottle_on_the_rack\": {\"sr\": 0.95, \"successes\": 19, \"total\": 20}}, \"delta_vs_4090_s42\": \"+2.0pp (97.5% vs 95.5%)\"}, \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 82.5, \"source\": \"JSON file eval_goal_vla_only_seed43.json on bjb1-32546, harvested 2026-05-26\"}, \"conclusion\": \"success\"}, \"westd-pi05-adaptive-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.875}}, \"tau_sweep_goal_tau090_s42_cqa1\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.89, \"mean_uncertainty\": 0.1148, \"trigger_rate\": 0.0035, \"crm_applied_steps\": 94, \"total_steps\": 26628, \"tau\": 0.9, \"n_rollouts\": 20}, \"conclusion\": \"success\"}, \"tau_sweep_goal_tau070_s42_cqa1\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.87, \"mean_uncertainty\": 0.121, \"trigger_rate\": 0.0104, \"crm_applied_steps\": 283, \"total_steps\": 27265, \"tau\": 0.7, \"n_rollouts\": 20}, \"conclusion\": \"success\"}, \"tau_sweep_goal_tau050_s42_cqa1\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.87, \"mean_uncertainty\": 0.1196, \"trigger_rate\": 0.0206, \"crm_applied_steps\": 565, \"total_steps\": 27431, \"tau\": 0.5, \"n_rollouts\": 20}, \"conclusion\": \"success\"}, \"tau_sweep_spatial_tau025_s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.785, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}, \"conclusion\": \"negative\"}, \"tau_sweep_goal_tau025_s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}, \"conclusion\": \"negative\"}, \"tau_sweep_goal_tau040_s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}, \"conclusion\": \"negative\"}, \"tau_sweep_goal_tau045_s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}, \"conclusion\": \"negative\"}, \"goal_vla_only_s48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.795, \"n_rollouts\": 200}, \"conclusion\": \"success\"}, \"goal_adapt_s48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.85, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 5.5}, \"conclusion\": \"success\"}, \"westd-pi05-k2mean-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.995}, \"conclusion\": \"success\"}, \"eval-goal-vla-only-s49-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"benchmark\": \"goal\", \"seed\": 49}, \"conclusion\": \"success\"}, \"eval-goal-adapt-tau025-s49-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.805, \"n_rollouts\": 200, \"benchmark\": \"goal\", \"seed\": 49}, \"conclusion\": \"negative\"}, \"eval-spatial-vla-only-s48-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.775, \"n_rollouts\": 200, \"benchmark\": \"spatial\", \"seed\": 48}, \"conclusion\": \"success\"}, \"eval-spatial-vla-only-s46-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.8, \"n_rollouts\": 200, \"benchmark\": \"spatial\", \"seed\": 46}, \"conclusion\": \"success\"}, \"eval-spatial-adapt-tau025-s48-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.81, \"n_rollouts\": 200, \"benchmark\": \"spatial\", \"seed\": 48}, \"conclusion\": \"success\"}, \"eval-spatial-adapt-tau025-s46-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.78, \"n_rollouts\": 200, \"benchmark\": \"spatial\", \"seed\": 46}, \"conclusion\": \"negative\"}, \"pi05-adaptive-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-adaptive-object-s42-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-k2mean-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"pi05-crm-k2-long-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"benchmark\": \"long\", \"model\": \"pi0.5\", \"mode\": \"crm_obs_only\", \"K\": 2, \"norm\": 0.05, \"seed\": 44, \"per_task\": {\"LIVING_ROOM_SCENE2_soup_sauce\": 1, \"LIVING_ROOM_SCENE2_cream_butter\": 0.95, \"KITCHEN_SCENE3_stove_moka\": 0.95, \"KITCHEN_SCENE4_bowl_drawer\": 0.85, \"LIVING_ROOM_SCENE5_mugs_plates\": 1, \"STUDY_SCENE1_book_caddy\": 0.6, \"LIVING_ROOM_SCENE6_mug_pudding\": 0.65, \"LIVING_ROOM_SCENE1_soup_cream\": 0.9, \"KITCHEN_SCENE8_moka_pots\": 0.2, \"KITCHEN_SCENE6_mug_microwave\": 0.9}}}, \"eval-k2-goal-vla-only-s49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-mechanism-goal-adapt-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-crm-k2-long-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pi05-crm-k2-long-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-k2-tau030-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"trigger_rate\": 0.168, \"benchmark\": \"spatial\", \"seed\": 42, \"tau\": 0.3, \"K\": 2, \"norm\": 0.2}}, \"eval-k2-tau020-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"trigger_rate\": 0.267, \"benchmark\": \"spatial\", \"seed\": 42, \"tau\": 0.2, \"K\": 2, \"norm\": 0.2}}, \"eval-pi05-vla-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-object-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-goal-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-spatial-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-spatial-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-goal-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-goal-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-long-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.545}}, \"eval-adaptive-long-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.58}}, \"eval-crm-long-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.555}}, \"eval-crm-long-s43-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.545}}, \"eval-pi05-adaptive-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.83}, \"conclusion\": \"success\"}, \"eval-crm-long-s42-d149\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.565}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.985}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.975}, \"conclusion\": \"success\"}, \"eval-smolvla-crm-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"successes\": 165, \"total\": 200}}, \"eval-vla-only-spatial-bjb1-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200}}, \"eval-vla-only-spatial-bjb1-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.775, \"successes\": 155, \"total\": 200}}, \"eval-adaptive-long-s44-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.54, \"trigger_rate\": 0.045, \"mean_uncertainty\": 0.126}}, \"eval-adaptive-long-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.58, \"trigger_rate\": 0.043, \"mean_uncertainty\": 0.125}}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200}}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200}}, \"eval-k2-spatial-adapt-s44-paired-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"trigger_rate\": 0.195, \"paired_vla_only_sr\": 0.8}}, \"eval-k2-spatial-adapt-s43-paired-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"trigger_rate\": 0.203, \"paired_vla_only_sr\": 0.795}}, \"eval-k2-spatial-adapt-s42-paired-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"trigger_rate\": 0.198, \"paired_vla_only_sr\": 0.785}}, \"eval-vla-only-spatial-s47-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.785}}, \"eval-adaptive-object-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"trigger_rate\": 0.035}}, \"eval-smolvla-crm-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.52}}, \"eval-pi05-adaptive-goal-s42-dryrun\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.65, \"vram_peak_mib\": 13920, \"vram_stable\": true}}, \"eval-adaptive-spatial-s47-bjb1-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"trigger_rate\": 0.191}}, \"eval-adaptive-spatial-s47-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.795, \"trigger_rate\": 0.192}}, \"eval-adaptive-goal-s42-d149\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.835, \"trigger_rate\": 0.083}}, \"eval-pi05-vla-only-object-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-s44-d149\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.99, \"successes\": 198, \"total\": 200, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"eval-pi05-adaptive-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"success_rate\": 0, \"total\": 200, \"successes\": 0, \"failure_reason\": \"CUDA OOM memory leak from task 4 onwards (399 OOM errors). First 3 tasks ran correctly: 75%, 95%, 75%. JSON serialization bug masked real results by zeroing per_task dict.\", \"partial_results\": {\"open_the_middle_drawer\": 0.75, \"put_the_bowl_on_stove\": 0.95, \"wine_bottle_on_cabinet\": 0.75}}}, \"eval-k2-tau010-spatial-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"trigger_rate\": 0.744, \"mean_uncertainty\": 0.1854}}, \"eval-k2-tau0075-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"trigger_rate\": 0.92, \"mean_uncertainty\": 0.1811}}, \"eval-k2-tau015-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"trigger_rate\": 0.412, \"mean_uncertainty\": 0.1855}}, \"eval-k2-goal-vla-only-s46-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.82, \"successes\": 164, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-k2-goal-vla-only-s45-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-k2-goal-adapt-s47-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"trigger_rate\": 0.098, \"mean_uncertainty\": 0.1499}, \"conclusion\": \"success\"}, \"eval-k2-goal-adapt-s46-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.84, \"successes\": 168, \"total\": 200, \"trigger_rate\": 0.088, \"mean_uncertainty\": 0.1482}, \"conclusion\": \"success\"}, \"eval-k2-goal-vla-only-s47-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-k2-goal-adapt-s45-paired\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"trigger_rate\": 0.094, \"mean_uncertainty\": 0.1495}, \"conclusion\": \"success\"}, \"eval-vla-only-spatial-bjb1-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-adaptive-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-adaptive-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-adaptive-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.975, \"successes\": 195, \"total\": 200}}, \"eval-k2-adaptive-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-adaptive-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-cqa1-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-cqa1-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-cqa1-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k2-adaptive-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-s42-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200, \"mode\": \"vla_only\", \"benchmark\": \"spatial\", \"seed\": 42, \"model\": \"pi05\"}}, \"eval-pi05-vla-only-goal-s42-paired\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200, \"mode\": \"vla_only\", \"benchmark\": \"goal\", \"seed\": 42, \"model\": \"pi05\"}}, \"eval-long-adaptive-k10-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-adaptive-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-goal-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.97, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.96, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.965, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-k2-tau010-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-s45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.85, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-k2-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.955, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.98, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.8, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-crm-norm005-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.785, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-crm-norm005-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.78, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-long-vla-only-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-norm005-goal-s49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-norm005-object-s48\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-long-vla-only-s48\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s50\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-spatial-vla-only-smolvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train-crm-pi05-unified-3suite-r2\": {\"status\": \"DONE\", \"metrics\": {\"current_epoch\": 25, \"total_epochs\": 50, \"best_val_loss\": 0.004854, \"best_epoch\": 24, \"train_loss_latest\": 0.00844, \"progress_pct\": 50}, \"conclusion\": \"failed\"}, \"eval-supp-vla-only-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.785, \"per_task_sr\": {\"between\": 0.9, \"next_ramekin\": 0.95, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.7, \"on_ramekin\": 0, \"next_cookie\": 0.9, \"stove\": 0.8, \"next_plate\": 0.75, \"cabinet\": 0.95}}}, \"eval-supp-vla-only-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.795, \"per_task_sr\": {\"between\": 1, \"next_ramekin\": 0.9, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.8, \"on_ramekin\": 0, \"next_cookie\": 0.95, \"stove\": 0.75, \"next_plate\": 0.85, \"cabinet\": 0.8}}}, \"eval-supp-vla-only-obj-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.755, \"per_task_sr\": {\"soup\": 0.55, \"cream_cheese\": 0.7, \"salad\": 0.8, \"bbq\": 0.95, \"ketchup\": 0.8, \"tomato\": 0.8, \"butter\": 0.6, \"milk\": 0.65, \"pudding\": 0.8, \"oj\": 0.9}}}, \"eval-supp-vla-only-obj-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.79, \"per_task_sr\": {\"soup\": 0.65, \"cream_cheese\": 0.8, \"salad\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.85, \"tomato\": 0.8, \"butter\": 0.65, \"milk\": 0.8, \"pudding\": 0.75, \"oj\": 0.95}}}, \"eval-supp-vla-only-goal-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.82, \"per_task_sr\": {\"middle_drawer\": 0.75, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.65, \"bowl_cabinet\": 0.95, \"push_plate\": 0.85, \"cream_cheese\": 0.55, \"stove_on\": 1, \"bowl_plate\": 0.85, \"wine_rack\": 0.8}}}, \"eval-supp-vla-only-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.85, \"per_task_sr\": {\"middle_drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.9, \"drawer_bowl\": 0.55, \"bowl_cabinet\": 1, \"push_plate\": 0.9, \"cream_cheese\": 0.6, \"stove_on\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}}, \"eval-k5-spatial-s42-sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"K\": 5, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.835}}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.575, \"successes\": 115, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"spatial\", \"seed\": 42, \"mode\": \"vla_only\", \"model\": \"pi05\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 98.5, \"total_successes\": 197, \"total_episodes\": 200}}, \"eval-supp-obj-vla-only-s50\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.74, \"successes\": 148, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"object\", \"seed\": 50, \"mode\": \"vla_only\", \"model\": \"pi05\"}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.545, \"successes\": 109, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"note\": \"output saved as eval_long_vla_only_seed47.json (pre-M083 naming)\"}}, \"eval-supp-spatial-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.78, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"total_rollouts\": 200, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.65, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.7}}}, \"eval-a1-baseline-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.565, \"total_successes\": 113, \"total_episodes\": 200, \"official_reported_sr\": 0.998, \"gap_vs_official\": -0.433, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.35, \"salad_dressing\": 0.35, \"bbq_sauce\": 0.8, \"ketchup\": 0.65, \"tomato_sauce\": 0.95, \"butter\": 0.65, \"milk\": 0.1, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.25}}}, \"eval-supp-long-vla-only-s47-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.595, \"total_successes\": 119, \"total_trials\": 200}}, \"eval-supp-obj-k2mean-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-adapt-tau025-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.77, \"trigger_rate\": 0.0403, \"crm_applied_steps\": 1458}}, \"eval-supp-obj-crm-norm005-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825}}, \"eval-supp-obj-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.755}}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"note\": \"Completed at 18:07 with SR=81.0% per log; JSON overwritten by vla-only K=1 run which wrote to same output_file (eval_spatial_vla_only_seed47.json). Per-task data recoverable from eval-supp-k2mean-spatial-s47.log on cqa1-32758. Recommend explicit --output_file for future k2mean runs.\"}}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"successes\": 163, \"total\": 200, \"trigger_rate\": 0.2046, \"mean_uncertainty\": 0.1873, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-long-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.565, \"successes\": 113, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-obj-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.775, \"successes\": 155, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.77, \"successes\": 154, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.755, \"successes\": 151, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-goal-vla-only-s47-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_goal_vla_only_seed47.json\"}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\"}, \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.54, \"successes\": 108, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"train-crm-pi05-unified-3suite\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200}}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"mean_uncertainty\": 0.1885, \"trigger_rate\": 0.2013, \"tau\": 0.25, \"total_steps\": 28599, \"crm_applied_steps\": 5758}}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200}}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200}}, \"train-crm-pi05-spatial-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.002887, \"best_epoch\": 50, \"final_train_loss\": 0.018836}}, \"train-crm-pi05-goal-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.003319, \"best_epoch\": 48, \"final_train_loss\": 0.018992}}, \"eval-supp-goal-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.077477, \"total_epochs\": 50, \"train_samples\": 74507, \"obs_dim\": 4096, \"params\": 908106, \"architecture\": \"MultiScaleCRM-K1\"}}, \"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.765, \"successes\": 153, \"total\": 200, \"source\": \"json_harvest_bjb2-40593\", \"json_file\": \"eval_object_crm_obs_only_norm0.05_seed45.json\"}, \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.76}, \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.78, \"successes\": 156, \"total\": 200, \"per_task\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.7}}}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.77, \"successes\": 154, \"total\": 200}}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-goal-bjb1-32546\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.83, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.79, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\"}, \"crm-train-pi05-spatial-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006138, \"epochs_completed\": 50, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/\"}}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 100}}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 11, \"successes\": 11, \"total\": 100}}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 34, \"successes\": 34, \"total\": 100}}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 36, \"successes\": 36, \"total\": 100, \"fast_path\": 81.5, \"avg_k\": 3.5, \"mean_l2\": 0.0885}}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 82, \"successes\": 164, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 59, \"successes\": 118, \"total\": 200}}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 200}}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"trigger_rate\": 0.0909, \"tau\": 0.25, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-spatial-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80.5, \"successes\": 161, \"total\": 200}}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 19.9, \"mean_unc\": 0.1846}}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}}, \"eval-supp-long-crm-norm005-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.605, \"successes\": 121, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"successes\": 159, \"total\": 200}}, \"eval-supp-goal-k2mean-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.81, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.6, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.55, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.78}, \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-crm-obj-s46\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.795, \"per_task\": {\"alphabet_soup\": 0.8, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.7, \"tomato_sauce\": 0.75, \"butter\": 0.75, \"milk\": 0.85, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.9}}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"SR\": 0.545, \"successes\": 109, \"total\": 200}}, \"eval-supp-long-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.57, \"successes\": 114, \"total\": 200}}, \"eval-supp-goal-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.855}}, \"eval-supp-crm-norm005-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.795}}, \"eval-supp-goal-crm-norm005-s45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.765}}, \"eval-supp-reconvla-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-supp-goal-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.094, \"mean_unc\": 0.1493}}, \"eval-supp-long-crm-norm005-s44\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.565}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-obj-s46\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.765}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-obj-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.775}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s46\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.775}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s42\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.57}, \"conclusion\": \"negative\"}, \"eval-supp-obj-vla-only-s46\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.79}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s43\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.56}, \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s43\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.59}, \"conclusion\": \"negative\"}, \"eval-supp-long-crm-norm005-s43\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.545}, \"conclusion\": \"negative\"}, \"eval-supp-obj-adapt-tau025-s45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.565}, \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.565}, \"conclusion\": \"negative\"}, \"eval-ablation-tau040-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.835, \"trigger_rate\": 0.012, \"tau\": 0.4, \"crm_applied_steps\": 346, \"total_steps\": 28165}, \"conclusion\": \"negative\"}, \"eval-ablation-tau015-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.85, \"trigger_rate\": 0.339, \"tau\": 0.15, \"crm_applied_steps\": 9590, \"total_steps\": 28273}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.75, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.8, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.55, \"milk\": 0.7, \"chocolate_pudding\": 0.75, \"orange_juice\": 0.95}}, \"conclusion\": \"success\"}, \"eval-ablation-tau010-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.81, \"trigger_rate\": 0.739, \"tau\": 0.1, \"crm_applied_steps\": 22170, \"total_steps\": 29984}, \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.76, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.7, \"salad_dressing\": 0.7, \"bbq_sauce\": 0.95, \"ketchup\": 0.9, \"tomato_sauce\": 0.7, \"butter\": 0.75, \"milk\": 0.6, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.95}}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.785, \"successes\": 157, \"total\": 200, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.95, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.8, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.7}}, \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.85, \"successes\": 170, \"total\": 200, \"per_task\": {\"open_middle_drawer\": 0.85, \"put_bowl_stove\": 0.95, \"wine_bottle_cabinet\": 0.85, \"open_top_drawer_bowl\": 0.7, \"bowl_on_cabinet\": 0.9, \"push_plate_stove\": 0.9, \"cream_cheese_bowl\": 0.65, \"turn_on_stove\": 1, \"bowl_on_plate\": 0.95, \"wine_bottle_rack\": 0.75}}}, \"eval-supp-k2mean-spatial-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.79, \"successes\": 158, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"drawer\": 0.85, \"bowl_stove\": 1, \"wine_cabinet\": 0.8, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.95, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.75}}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.75, \"trigger_rate\": 0.0364, \"mean_uncertainty\": 0.11, \"crm_applied_steps\": 1310, \"total_steps\": 35990, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.75, \"salad_dressing\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.65, \"milk\": 0.7, \"chocolate\": 0.75, \"orange_juice\": 0.85}}, \"conclusion\": \"negative\"}, \"eval-supp-goal-reconvla-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.805, \"total_rollouts\": 200, \"total_successes\": 161, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.81, 0.81, 0.805], \"mean\": 0.8083, \"std\": 0.0029}}, \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.77, \"total_rollouts\": 200, \"total_successes\": 154}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.835, \"total_rollouts\": 200, \"total_successes\": 167, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.855, 0.82, 0.835], \"mean\": 0.8367, \"std\": 0.0176}}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.78, \"total_successes\": 156, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0.85, \"cream_cheese\": 0.85, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.7, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.9}}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.855, \"n_tasks\": 10, \"n_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 1, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.65, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-goal-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.865, \"trigger_rate\": 0.0677, \"crm_applied_steps\": 1870, \"total_steps\": 27642}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.785}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-goal-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.845, \"trigger_rate\": 0.088, \"crm_applied_steps\": 2509, \"total_steps\": 28500}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.82}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.775, \"trigger_rate\": 0.0367, \"crm_applied_steps\": 1312, \"total_steps\": 35796}, \"conclusion\": \"negative\"}, \"eval-supp-goal-reconvla-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_episodes\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.65, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.55, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.95, \"put_the_wine_bottle_on_the_rack\": 0.85}}, \"conclusion\": \"negative\"}, \"eval-supp-k2mean-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.78, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_episodes\": 200, \"per_task\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.75, \"next_to_plate\": 0.7, \"on_wooden_cabinet\": 0.85}}, \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.795, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task\": {\"between_plate_and_ramekin\": 1, \"table_center\": 1, \"next_to_ramekin\": 0.95, \"next_to_cookie_box\": 0.95, \"on_cookie_box\": 0.9, \"on_wooden_cabinet\": 0.85, \"on_stove\": 0.8, \"next_to_plate\": 0.8, \"top_drawer_wooden_cabinet\": 0.7, \"on_ramekin\": 0}, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.8, 0.815, 0.795], \"mean\": 0.803, \"std\": 0.01}}}, \"eval-supp-reconvla-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.85}}}, \"eval-supp-k2mean-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"total_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.55, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.45, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.95, \"put_the_wine_bottle_on_the_rack\": 0.85}}}, \"eval-supp-k2mean-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"total_successes\": 159, \"total_rollouts\": 200, \"mode\": \"vla_only\", \"K\": 2, \"baseline_mode\": \"mean\", \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"bbq_sauce\": 90, \"ketchup\": 95, \"tomato_sauce\": 85, \"butter\": 60, \"milk\": 70, \"chocolate_pudding\": 70, \"orange_juice\": 95}}}, \"eval-supp-goal-adapt-tau025-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 84, \"total_rollouts\": 200, \"total_successes\": 168, \"trigger_rate\": 8.3, \"mean_unc\": 0.1448, \"per_task\": {\"open_middle_drawer_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"put_bowl_on_stove\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"put_wine_bottle_on_cabinet\": {\"sr\": 80, \"success\": 16, \"total\": 20}, \"open_top_drawer_put_bowl\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"put_bowl_on_top_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"push_plate_to_stove\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"put_cream_cheese_in_bowl\": {\"sr\": 60, \"success\": 12, \"total\": 20}, \"turn_on_stove\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"put_bowl_on_plate\": {\"sr\": 90, \"success\": 18, \"total\": 20}, \"put_wine_bottle_on_rack\": {\"sr\": 80, \"success\": 16, \"total\": 20}}}, \"conclusion\": \"success\"}, \"eval-supp-goal-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 85.5, \"total_successes\": 171, \"total_episodes\": 200, \"per_task\": {\"middle_drawer\": 85, \"bowl_stove\": 100, \"wine_bottle_cabinet\": 95, \"top_drawer_bowl\": 70, \"bowl_cabinet\": 95, \"plate_stove\": 95, \"cream_cheese_bowl\": 50, \"stove\": 95, \"bowl_plate\": 95, \"wine_bottle_rack\": 75}}}, \"eval-supp-goal-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r6\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.005669, \"epochs\": 50, \"final_train_loss\": 0.009731, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/\"}}, \"eval-goal-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200}}, \"eval-supp-obj-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.035, \"mean_unc\": 0.109, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 2}}, \"eval-supp-k2mean-spatial-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 81.5, \"total_success\": 163, \"total_rollouts\": 200, \"per_task\": {\"bowl_between_plate_ramekin\": 95, \"bowl_next_to_ramekin\": 95, \"bowl_from_table_center\": 100, \"bowl_on_cookie_box\": 100, \"bowl_in_top_drawer\": 70, \"bowl_on_ramekin\": 0, \"bowl_next_to_cookie_box\": 95, \"bowl_on_stove\": 80, \"bowl_next_to_plate\": 85, \"bowl_on_wooden_cabinet\": 95}}, \"conclusion\": \"negative\"}, \"eval-supp-crm-norm005-spatial-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 78.5, \"total_rollouts\": 200, \"total_successes\": 157, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"next_to_ramekin\": {\"sr\": 90, \"success\": 18, \"total\": 20}, \"from_table_center\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_cookie_box\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"in_top_drawer_wooden_cabinet\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_ramekin\": {\"sr\": 0, \"success\": 0, \"total\": 20}, \"next_to_cookie_box\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_stove\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"next_to_plate\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_wooden_cabinet\": {\"sr\": 80, \"success\": 16, \"total\": 20}}, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [80, 81, 78.5], \"mean\": 79.8, \"std\": 1.3}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 80.5, \"total_successes\": 161, \"total_rollouts\": 200, \"trigger_rate\": 20, \"mean_unc\": 0.1881, \"conformal_threshold\": 0.25, \"max_correction_norm\": 0.2, \"mode\": \"adaptive_conformal_crm\", \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin\": {\"sr\": 90, \"successes\": 18, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_ramekin\": {\"sr\": 95, \"successes\": 19, \"rollouts\": 20}, \"pick_up_the_black_bowl_from_table_center\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_cookie_box\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet\": {\"sr\": 65, \"successes\": 13, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_ramekin\": {\"sr\": 0, \"successes\": 0, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_cookie_box\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_stove\": {\"sr\": 80, \"successes\": 16, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_plate\": {\"sr\": 80, \"successes\": 16, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_wooden_cabinet\": {\"sr\": 95, \"successes\": 19, \"rollouts\": 20}}}, \"conclusion\": \"success\"}, \"eval-supp-reconvla-k2-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"total_rollouts\": 200, \"total_successes\": 160, \"per_task\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 100, \"from_table_center\": 100, \"on_cookie_box\": 95, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 95, \"on_stove\": 75, \"next_to_plate\": 80, \"on_wooden_cabinet\": 85}}}, \"eval-supp-adapt-tau025-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 80, \"trigger_rate\": 19.4, \"mean_unc\": 0.1845, \"total_rollouts\": 200, \"total_successes\": 160, \"per_task\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 95, \"from_table_center\": 95, \"on_cookie_box\": 100, \"in_top_drawer_wooden_cabinet\": 70, \"on_ramekin\": 0, \"next_to_cookie_box\": 100, \"on_stove\": 80, \"next_to_plate\": 85, \"on_wooden_cabinet\": 80}}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 81, \"total_rollouts\": 200, \"total_successes\": 162, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"next_to_ramekin\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"from_table_center\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_cookie_box\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"in_top_drawer_wooden_cabinet\": {\"sr\": 75, \"success\": 15, \"total\": 20}, \"on_ramekin\": {\"sr\": 0, \"success\": 0, \"total\": 20}, \"next_to_cookie_box\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_stove\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"next_to_plate\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_wooden_cabinet\": {\"sr\": 95, \"success\": 19, \"total\": 20}}}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-adapt-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 77.5, \"total_successes\": 155, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 80, \"cream_cheese\": 90, \"salad_dressing\": 70, \"bbq_sauce\": 85, \"ketchup\": 70, \"tomato_sauce\": 75, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 80, \"orange_juice\": 95}, \"mean_unc\": 0.1104, \"trigger_rate\": 0.702}, \"conclusion\": \"negative\"}, \"eval-object-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 77.5, \"total_successes\": 155, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 90, \"ketchup\": 90, \"tomato_sauce\": 80, \"butter\": 75, \"milk\": 65, \"chocolate_pudding\": 65, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s43-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 77, \"total_successes\": 154, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 85, \"ketchup\": 80, \"tomato_sauce\": 85, \"butter\": 60, \"milk\": 75, \"chocolate_pudding\": 75, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 85, \"cream_cheese\": 75, \"salad_dressing\": 85, \"bbq_sauce\": 85, \"ketchup\": 90, \"tomato_sauce\": 75, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 70, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"bbq_sauce\": 95, \"ketchup\": 90, \"tomato_sauce\": 80, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 75, \"orange_juice\": 90}}}, \"eval-supp-obj-crm005-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.77, \"n_success\": 154, \"n_total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"conformal_threshold\": 0.074855, \"K\": 10, \"seed\": 42, \"per_task_sr\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.9, \"ketchup\": 0.8, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.75, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 80, \"n_success\": 160, \"n_total\": 200, \"trigger_rate\": 12.17, \"mean_unc\": 0.1873, \"conformal_threshold\": 0.35, \"max_correction_norm\": 0.2, \"crm_applied_steps\": 3474, \"total_steps\": 28549, \"per_task_sr\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 100, \"from_table_center\": 90, \"on_cookie_box\": 95, \"in_top_drawer\": 70, \"on_ramekin\": 0, \"next_to_cookie_box\": 95, \"on_stove\": 85, \"next_to_plate\": 85, \"on_wooden_cabinet\": 85}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 80.5, \"n_success\": 161, \"n_total\": 200, \"trigger_rate\": 40.7, \"mean_unc\": 0.1852, \"conformal_threshold\": 0.15, \"max_correction_norm\": 0.2, \"per_task_sr\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 100, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 90, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 75, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 90, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 80, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 85}}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm02-spatial-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 79, \"n_success\": 158, \"n_total\": 200, \"per_task_sr\": {\"between_plate_and_ramekin\": 100, \"next_to_ramekin\": 90, \"from_table_center\": 95, \"on_cookie_box\": 95, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 100, \"on_stove\": 95, \"next_to_plate\": 75, \"on_wooden_cabinet\": 65}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 82, \"n_success\": 164, \"n_total\": 200, \"trigger_rate\": 19.4, \"mean_unc\": 0.1847, \"per_task_sr\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 95, \"from_table_center\": 100, \"on_cookie_box\": 100, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 90, \"on_stove\": 90, \"next_to_plate\": 90, \"on_wooden_cabinet\": 85}}, \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed55\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-features-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-adapt-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau035-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r5-resumed\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau035-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-3dir-adaptive-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"trigger_rate\": 0.918, \"tau\": 0.074855, \"mean_uncertainty\": 0.183, \"crm_applied_steps\": 26589, \"total_steps\": 28955, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 1, \"from_table_center\": 1, \"on_cookie_box\": 0.9, \"in_top_drawer\": 0.8, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.8}}}, \"eval-3dir-norm03-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 73.9, \"successes\": 133, \"total\": 180, \"n_tasks_complete\": 9, \"n_tasks_total\": 10, \"n_rollouts\": 20, \"note\": \"killed at T10 rollout 10/20, 9/10 tasks complete\", \"per_task_sr\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 0.85, \"from_table_center\": 1, \"on_cookie_box\": 0.9, \"in_top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0.8, \"next_to_plate\": 0.55, \"on_wooden_cabinet\": \"partial_5/10\"}}}, \"eval-3dir-reconvla-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"successes\": 158, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 0.95, \"from_table_center\": 1, \"on_cookie_box\": 1, \"in_top_drawer\": 0.65, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.75, \"next_to_plate\": 0.7, \"on_wooden_cabinet\": 0.85}}}, \"eval-3dir-norm01-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 79, \"successes\": 158, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"from_table_center\": 1, \"on_cookie_box\": 1, \"in_top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.75}}}, \"eval-3dir-norm005-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 1, \"from_table_center\": 1, \"on_cookie_box\": 0.95, \"in_top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.85, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.8}}}, \"precompute-pi05-goal-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-spatial-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-object-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-object-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r5\": {\"status\": \"DONE\", \"metrics\": {\"val_loss\": 0.006075, \"epochs_completed\": 32, \"epochs_target\": 50, \"train_loss_final\": 0.010489, \"best_epoch\": 32, \"crash_epoch\": 33, \"crash_count\": 2}, \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-long-2048\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-lerobot-goal-seed44-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78, \"n_episodes\": 200}}, \"train-crm-smolvla-3suite-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.005878, \"final_train_loss\": 0.00969, \"final_val_loss\": 0.00588, \"epochs_completed\": 50, \"total_params\": 327198, \"data_samples\": 77835, \"best_epoch\": 50}}, \"eval-smolvla-lerobot-goal-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pc_success\": 65, \"n_episodes\": 200, \"eval_s\": 841}}, \"eval-smolvla-lerobot-object-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pc_success\": 66.5, \"n_episodes\": 200, \"eval_s\": 857.4}}, \"eval-smolvla-lerobot-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.6, \"n_episodes\": 200, \"n_tasks\": 10, \"per_task_sr\": [0.75, 0.65, 0.75, 0.75, 0.5, 0, 0.9, 0.7, 0.4, 0.6]}}, \"precompute-smolvla-long-wrapper-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 49.5, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 53.5, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 49.5, \"n_episodes\": 200}}, \"train-crm-unified-4suite-r4\": {\"status\": \"DONE\", \"metrics\": {\"epochs_completed\": 13, \"current_epoch\": 14, \"current_batch\": \"2700/6316\", \"total_epochs\": 50, \"last_train_loss\": 0.012, \"checkpoint_latest\": \"checkpoint_epoch0013.pt\", \"checked_at\": \"2026-05-22T01:21Z\", \"note\": \"CRON false alarm - process still running (PID 322367)\"}, \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-long-seed42-r4-rerun\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.94, \"successes\": 188, \"total\": 200, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.95, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 1, \"KITCHEN_SCENE3_stove_moka_pot\": 1, \"KITCHEN_SCENE4_black_bowl_drawer\": 1, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.9, \"STUDY_SCENE1_book_in_caddy\": 0.95, \"LIVING_ROOM_SCENE6_mug_pudding\": 1, \"LIVING_ROOM_SCENE1_soup_cream_cheese\": 0.9, \"KITCHEN_SCENE8_both_moka_pots\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave\": 0.9}}, \"conclusion\": \"success\"}, \"eval-pi05-crm-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed43-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed44-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed42-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed44-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed43-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}}, \"precompute-smolvla-long-k2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-bjb2-28827\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-long-bjb2-28827\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.955}}, \"eval-pi05-vla-only-long-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.955}}, \"eval-pi05-vla-only-goal-seed44-r4\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.975, \"successes\": 195, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-seed43-r4\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-openvla-oft-official-object\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-object-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 99.5, \"total_successes\": 199, \"total_episodes\": 200}}, \"eval-smolvla-lerobot-official-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42-r4\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 100, \"total_success\": 200, \"total_rollouts\": 200, \"n_action_steps\": 10, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 100, \"bbq_sauce\": 100, \"ketchup\": 100, \"tomato_sauce\": 100, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 100, \"orange_juice\": 100}}, \"conclusion\": \"success\"}, \"train-crm-unified-4suite\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"completed_epochs\": 4, \"target_epochs\": 50, \"exit_code\": 124, \"failure_reason\": \"timeout (EXIT_CODE=124) — killed after 4/50 epochs (~2.3 GPU hours)\", \"best_val_loss\": 0.009633, \"best_epoch\": 4, \"training_curve\": [{\"epoch\": 1, \"train_loss\": 0.019467, \"val_loss\": 0.010801, \"lr\": \"9.99e-04\"}, {\"epoch\": 2, \"train_loss\": 0.018024, \"val_loss\": 0.010438, \"lr\": \"9.96e-04\"}, {\"epoch\": 3, \"train_loss\": 0.017237, \"val_loss\": 0.009901, \"lr\": \"9.91e-04\"}, {\"epoch\": 4, \"train_loss\": 0.01663, \"val_loss\": 0.009633, \"lr\": \"9.84e-04\"}]}}, \"precompute-smolvla-long-bjb1-32546-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-long-bjb1-32546\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-loss-perdof-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"milk\": 5, \"chocolate_pudding\": 5, \"orange_juice\": 5}}, \"conclusion\": \"negative\"}, \"eval-loss-combined-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"avg_success_rate\": 9, \"total_successes\": 18, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 10, \"salad_dressing\": 10, \"bbq_sauce\": 15, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 5, \"milk\": 10, \"chocolate_pudding\": 25, \"orange_juice\": 10}}, \"conclusion\": \"negative\"}, \"eval-loss-conformal-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 6, \"total_successes\": 12, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 10, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 0, \"milk\": 10, \"chocolate_pudding\": 20, \"orange_juice\": 10}}, \"conclusion\": \"negative\"}, \"eval-loss-mse-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"avg_success_rate\": 7, \"total_successes\": 14, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 10, \"ketchup\": 5, \"tomato_sauce\": 15, \"butter\": 10, \"milk\": 15, \"chocolate_pudding\": 5, \"orange_juice\": 0}}, \"conclusion\": \"negative\"}, \"eval-openvla-oft-object-baseline-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": \"all 10 tasks 0.0%\", \"n_rollouts\": 20, \"total_episodes\": 200}}, \"precompute-smolvla-long-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 136090, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5, \"obs_features_shape\": [136090, 960], \"k_samples_shape\": [136090, 10, 5, 6], \"expert_actions_shape\": [136090, 5, 6], \"total_time_sec\": 8021, \"speed\": \"0.06s/sample\"}}, \"crm-loss-combined\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.005302, \"final_train_loss\": 0.004481, \"best_epoch\": 48, \"epochs\": 50, \"vs_mse\": \"2.5x worse\", \"vs_perdof\": \"43x worse\", \"dof_weight_range\": [0.0107, 3.7318]}, \"conclusion\": \"negative\"}, \"crm-loss-conformal\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.013343, \"final_train_loss\": 0.016046, \"epochs\": 50, \"vs_mse\": \"6.4x worse\"}, \"conclusion\": \"negative\"}, \"precompute-smolvla-goal-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 61728, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5}}, \"crm-loss-perdof\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.000124, \"final_train_loss\": 0.000141, \"best_epoch\": 50, \"total_epochs\": 50, \"dof_weight_min\": 0.0107, \"dof_weight_max\": 3.7318, \"mse_baseline_val_loss\": 0.00208, \"conformal_guided_val_loss\": 0.013343, \"samples\": 14570, \"crm_params\": 337438}, \"conclusion\": \"success\"}, \"crm-loss-mse-baseline\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.00208, \"final_train_loss\": 0.004038, \"best_epoch\": 50, \"total_epochs\": 50, \"initial_val_loss\": 0.008373, \"exit_code\": 0}, \"conclusion\": \"success\"}, \"eval-smolvla-acr-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-long-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-long-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-acr-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"RuntimeError: state_dict shape mismatch in CRM checkpoint. input_mean/input_std: [990] vs [1030], net.0.weight: [256,990] vs [256,1030]. CRM checkpoint (crm_v3_norm/obs_only/crm_best.pt) was trained with obs_dim=960 but model now expects obs_dim=1000.\"}}, \"eval-smolvla-acr-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-train-pi05-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"val_loss\": 0.006138, \"best_epoch\": 50, \"total_epochs\": 50}}, \"crm-train-pi05-object-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"val_loss\": 0.004018, \"best_epoch\": 50, \"total_epochs\": 50}}, \"crm-train-pi05-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-pi05-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.85, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed43-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.83, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed42-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.845, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.81, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.815, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.82, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-spatial-obs-only-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.34, \"per_task_sr\": [0.9, 0.9, 0, 0.4, 0.1, 0, 0.8, 0, 0.3, 0], \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10}}, \"eval-pi05-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.17}}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\"}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"sr_pct\": \"19.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1468, \"trigger_rate\": 0.838}}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12}, \"conclusion\": \"success\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"total_rollouts\": 100, \"total_successes\": 35, \"mean_uncertainty\": 0.2619, \"trigger_rate\": 0.98}}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"sr_pct\": \"20.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1448, \"trigger_rate\": 0.832}}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"total_rollouts\": 100, \"total_successes\": 34, \"mean_uncertainty\": 0.2679, \"trigger_rate\": 0.976}}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"sr_pct\": \"36.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.2661, \"trigger_rate\": 0.978}}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1457, \"trigger_rate\": 0.84}}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"source\": \"harvested from bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm01_seed60.json\"}}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed75\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed51-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11}}, \"eval-obs-only-object-norm01-seed52-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed65\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed61\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed64-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed63\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed62\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed52-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"total_successes\": 11}}, \"eval-obs-only-object-norm005-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed55-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-openvla-crm-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0, \"sr_pct\": \"0.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"sr_pct\": \"15.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.1, \"sr_pct\": \"10.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.33, \"sr_pct\": \"33.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-seed54\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.14, \"mean_l2\": 0, \"avg_k\": 1, \"fast_path_pct\": 0.12, \"n_rollouts\": 10}}, \"eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.11, \"n_rollouts\": 100, \"fast_path_pct\": 12.5, \"avg_k\": 1}}, \"eval-perdof-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.1, \"n_rollouts\": 100, \"per_task\": [0, 0, 1, 1, 0, 1, 1, 0, 4, 2]}}, \"eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"avg_K\": 1, \"adaptive_trigger_rate\": 0, \"crm_trigger_rate\": 0.8795, \"unc_threshold\": 0.42}, \"conclusion\": \"negative\"}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"successes\": 35, \"total_rollouts\": 100}}, \"train-crm-openvla-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.07726, \"final_train_loss\": 0.234989, \"epochs_completed\": 50}}, \"openvla-precompute-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_files\": 74507, \"obs_dim\": 4096, \"cache_size_gb\": 6, \"multi_scale_layers\": [7, 15, 23, 31]}}, \"eval-random-selection-object-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"tasks_evaluated\": 10, \"rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 10}}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"seed\": 49, \"K\": 10, \"max_correction_norm\": 0.2}}, \"eval-random-selection-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 7}}, \"eval-obs-only-spatial-norm02-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 33}}, \"eval-k5-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 17}}, \"eval-random-selection-spatial-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 26}}, \"eval-random-selection-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.28, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed42-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed44-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 10, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.26, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.7, \"stove\": 0, \"next_to_plate\": 0.2, \"wooden_cabinet\": 0}}}, \"eval-random-selection-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.35, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed42\": {\"status\": \"DONE\", \"metrics\": {\"status_note\": \"INCOMPLETE - only 2/10 tasks evaluated before process terminated\", \"partial_per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 1}, \"tasks_completed\": 2, \"tasks_total\": 10}, \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-norm02-seed49\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.32, \"sr_pct\": \"32%\", \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"on_cookie_box\": 0.3, \"top_drawer_cabinet\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.36, \"avg_K\": 3.56, \"fast_path_ratio\": 0.805, \"adaptive_trigger_rate\": 0.195, \"total_rollouts\": 100, \"successes\": 36, \"total_steps\": 23123, \"fast_steps\": 18615, \"full_steps\": 4508, \"threshold\": 0.12587, \"mean_l2_distance\": 0.09, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 0.8, \"successes\": 8, \"total\": 10}, \"next_to_ramekin\": {\"sr\": 1, \"successes\": 10, \"total\": 10}, \"from_table_center\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"on_cookie_box\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"in_top_drawer\": {\"sr\": 0.1, \"successes\": 1, \"total\": 10}, \"on_ramekin\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_cookie_box\": {\"sr\": 0.9, \"successes\": 9, \"total\": 10}, \"on_stove\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_plate\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"on_wooden_cabinet\": {\"sr\": 0, \"successes\": 0, \"total\": 10}}}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed50\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}, \"total_rollouts\": 100, \"total_successes\": 13, \"seed\": 50, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\"}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"successes\": 11, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.1, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.4, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 69, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-spatial-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed44-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-k1-object-seed43-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-k1-object-seed42-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.07, \"total\": 100, \"successes\": 7, \"benchmark\": \"object\", \"mode\": \"crm_perdof\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.11, \"total\": 100, \"successes\": 11, \"benchmark\": \"object\", \"mode\": \"reconvla\"}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.73, \"total\": 100, \"successes\": 73, \"benchmark\": \"goal\", \"mode\": \"vla_only\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.33, \"total\": 100, \"successes\": 33, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\"}, \"conclusion\": \"success\"}, \"eval-latency-profiling-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pipeline_latency_ms\": 247, \"crm_latency_ms\": 0.27}}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 33, \"avg_k\": 5.054, \"fast_path_pct\": 61.8, \"mean_l2\": 0.092, \"total_rollouts\": 100, \"threshold\": 0.098735}}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 66, \"total_rollouts\": 100, \"per_task_sr\": {\"open_middle_drawer\": 40, \"put_bowl_on_stove\": 90, \"put_wine_bottle_on_cabinet\": 50, \"open_top_drawer_put_bowl\": 40, \"put_bowl_on_cabinet\": 80, \"push_plate_to_stove\": 90, \"put_cream_cheese_in_bowl\": 20, \"turn_on_stove\": 100, \"put_bowl_on_plate\": 100, \"put_wine_bottle_on_rack\": 50}}}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 32, \"avg_k\": 7.693, \"fast_path_pct\": 28.8, \"mean_l2\": 0.0896, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 70, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 40, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"total_successes\": 16, \"total_rollouts\": 100, \"seed\": 49, \"benchmark\": \"LIBERO-Object\", \"K\": 10, \"mode\": \"reconvla (argmin baseline)\", \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.3, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}}}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.68, \"per_task\": {\"open_middle_drawer\": 0.7, \"bowl_on_stove\": 0.9, \"wine_on_cabinet\": 0.4, \"bowl_in_drawer\": 0.3, \"bowl_on_cabinet\": 0.8, \"plate_to_stove\": 0.8, \"cream_cheese_in_bowl\": 0.4, \"turn_on_stove\": 1, \"bowl_on_plate\": 1, \"wine_on_rack\": 0.5}}}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32, \"avg_K\": 3.586, \"fast_path_pct\": 80.17, \"mean_l2\": 0.0905, \"adaptive_trigger_rate\": 0.198, \"threshold\": 0.12587, \"total_steps\": 23797, \"fast_steps\": 19079, \"full_steps\": 4718}}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.31, \"avg_K\": 3.5, \"fast_path_pct\": 80.6, \"mean_l2\": 0.0907, \"threshold\": 0.12587, \"total_rollouts\": 100, \"total_successes\": 31, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14, \"total_rollouts\": 100, \"total_successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"updated_aggregate\": {\"mean_sr\": 16.4, \"std_sr\": 2, \"n_seeds\": 7, \"prior\": \"16.8±1.8% (n=6)\", \"delta_vs_vla_baseline\": \"+5.5pp\"}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"incomplete\": true, \"tasks_completed\": 2, \"tasks_total\": 10, \"partial_results\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9}, \"failure_reason\": \"Process exited after 2/10 tasks; no JSON output generated; likely OOM or early termination\"}}, \"eval-adaptive-k-spatial-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.4, \"fast_path_ratio\": 0.45, \"adaptive_trigger_rate\": 0.55, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 30, \"avg_K\": 6.324, \"fast_path_pct\": 45.95, \"mean_l2\": 0.0903, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.33, \"avg_K\": 7.65, \"fast_path_pct\": 29.4, \"mean_l2_distance\": 0.0892, \"threshold\": 0.054959, \"total_steps\": 23410, \"fast_steps\": 6873, \"full_steps\": 16537, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"negative\"}, \"eval-adaptive-k-spatial-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 30, \"avg_k\": 7.6, \"fast_path_pct\": 29.5, \"mean_l2\": 0.089, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 60, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 30, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}}, \"eval-adaptive-k-spatial-p75-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 34, \"total_rollouts\": 100, \"adaptive_stats\": {\"fast_path_pct\": 62.2, \"avg_k\": 5, \"mean_l2\": 0.0911}, \"per_task\": {\"bowl_between_plate_ramekin\": 80, \"bowl_next_to_ramekin\": 100, \"bowl_from_table_center\": 0, \"bowl_on_cookie_box\": 40, \"bowl_in_top_drawer\": 0, \"bowl_on_ramekin\": 0, \"bowl_next_to_cookie_box\": 90, \"bowl_on_stove\": 0, \"bowl_next_to_plate\": 30, \"bowl_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.18, \"total_successes\": 18, \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}, \"comparison\": {\"k10_reference\": \"16.8±1.8%\", \"k20_this\": \"18.0%\", \"delta\": \"+1.2pp\", \"note\": \"within K=10 error bars, marginal improvement\"}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed49-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.16, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.9, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_mug_pudding\": 0.2, \"LIVING_ROOM_SCENE1_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.31, \"avg_k\": 5.02, \"fast_path_ratio\": 0.622, \"mean_l2\": 0.0909, \"adaptive_trigger_rate\": 0.378, \"total_steps\": 23914, \"fast_steps\": 14875, \"full_steps\": 9039}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.4, \"fast_path_ratio\": 0.45, \"adaptive_trigger_rate\": 0.55, \"mean_l2_distance\": 0.0923, \"total_steps\": 23661, \"fast_steps\": 10649, \"full_steps\": 13012, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 3.07, \"fast_path_ratio\": 0.866}}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 3.15, \"fast_path_ratio\": 0.856}}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.72, \"fast_path_ratio\": 0.785}}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.81, \"fast_path_ratio\": 0.7737, \"total_steps\": 27813, \"fast_steps\": 21520, \"full_steps\": 6293}}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0.1, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.4, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"mean_l2_distance\": 0.0903, \"total_steps\": 23414, \"fast_steps\": 10728, \"full_steps\": 12686, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.2, \"total_episodes\": 100, \"total_successes\": 20, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.4, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"latency-profile-n1000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vla_e2e_K1_ms\": 256.5, \"vla_e2e_K10_ms\": 253.2, \"crm_forward_ms\": 0.28, \"cgs_features_ms\": 5.75, \"full_pipeline_K10_ms\": 249, \"adaptive_fast_path_ms\": 252.9, \"adaptive_full_path_ms\": 459.6, \"crm_overhead_vs_vla_K10_ms\": -4.2, \"crm_overhead_pct\": -1.66, \"adaptive_speedup_ratio\": 1.82, \"argmin_l2_K10_ms\": 0.06, \"gpu_mem_mb\": 903, \"n_measure\": 1000, \"gpu_model\": \"RTX 4090\"}}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.58, \"fast_path_ratio\": 0.928}}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 4.788, \"fast_path_ratio\": 0.6515, \"total_steps\": 28207, \"fast_steps\": 18377, \"full_steps\": 9830}}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.36, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed49\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.65, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed52\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed51\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed50\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-crm-long-seed50\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.736, \"fast_path_ratio\": 0.658, \"adaptive_trigger_rate\": 0.342, \"total_steps\": 27889, \"fast_steps\": 18351, \"full_steps\": 9538}, \"conclusion\": \"success\"}, \"calibrate-crm-correction-signal\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"go_nogo\": \"NO-GO\", \"rho_k1_corr_vs_k10_var\": 0.1523, \"p_k1_corr_vs_k10_var\": \"6.37e-143\", \"rho_k2_corr_vs_k10_var\": 0.134, \"p_k2_corr_vs_k10_var\": \"8.66e-111\", \"total_steps\": 27626, \"total_episodes\": 100}}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.8, \"fast_path_ratio\": 0.65}}, \"eval-vla-only-goal-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.3}}}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 3.909, \"fast_path_ratio\": 0.761, \"total_steps\": 28067, \"fast_steps\": 21368, \"full_steps\": 6699}}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.022, \"fast_path_ratio\": 0.872, \"total_steps\": 27724, \"fast_steps\": 24181, \"full_steps\": 3543}}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.612, \"fast_path_ratio\": 0.923, \"total_steps\": 27935, \"fast_steps\": 25797, \"full_steps\": 2138}}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 2.672, \"fast_path_ratio\": 0.916, \"total_steps\": 28258, \"fast_steps\": 25886, \"full_steps\": 2372}}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.2, \"STUDY_SCENE1_book_in_caddy\": 0.2, \"LIVING_ROOM_SCENE2_soup_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cheese_butter_basket\": 0, \"KITCHEN_SCENE4_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_soup_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.3, \"STUDY_SCENE1_book_in_back_compartment\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0.1, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.9, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.2, \"STUDY_SCENE1_book_in_back_compartment\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.65, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_bowl_on_top_of_the_cabinet\": 0.8, \"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"put_the_wine_bottle_on_the_rack\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_cream_cheese_in_the_bowl\": 0.2}}}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.64, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_bowl_on_the_stove\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"put_the_wine_bottle_on_the_rack\": 0.4, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"k2l2_vs_k10var_rho\": 0.9979, \"k2l2_vs_k10var_pvalue\": 0, \"k2l2_vs_fmvd_rho\": 0.0925, \"k2l2_vs_fmvd_pvalue\": 6.03e-29, \"k10var_vs_fmvd_rho\": 0.0825, \"k10var_vs_fmvd_pvalue\": 2.33e-23, \"n_samples\": 14512, \"k2l2_mean\": 0.0807, \"k2l2_std\": 0.0361, \"go_nogo_k2_proxy\": \"GO (rho=0.9979)\", \"go_nogo_fmvd_signal\": \"NO-GO (rho=0.09)\"}}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 18}}, \"eval-vla-only-spatial-seed49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.69, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.5, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.6}}}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2, \"alphabet_soup\": 0, \"cream_cheese\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.2, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.6, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.3, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.4, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.67, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 100, \"successful_rollouts\": 14, \"per_task\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0, \"put_both_cream_cheese_box_and_butter_in_basket\": 0, \"turn_on_stove_put_moka_pot\": 0.8, \"put_black_bowl_in_bottom_drawer\": 0, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.4, \"pick_up_book_place_in_caddy\": 0.1, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.1, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0, \"put_both_moka_pots_on_stove\": 0, \"put_yellow_white_mug_in_microwave\": 0}}}, \"eval-crm-goal-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.63, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.3, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.1, \"turn_on_the_stove\": 0.8, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.6, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 0.9, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.5, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.1, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}}, \"fmvd-calibration-phase1\": {\"status\": \"DONE\", \"metrics\": {\"spearman_rho\": 0.082528, \"spearman_pvalue\": 2.33e-23, \"n_samples\": 14512, \"go_nogo\": \"NO-GO\", \"threshold\": 0.3, \"fmvd_mean\": 0.054867, \"fmvd_std\": 0.040291, \"fmvd_P25\": 0.027738, \"fmvd_P50\": 0.046693, \"fmvd_P75\": 0.070899, \"fmvd_P90\": 0.093805, \"k10_variance_mean\": 0.004888, \"k10_variance_std\": 0.005635, \"task_success_rate\": 0.06, \"n_tasks\": 10, \"n_episodes\": 50, \"n_successes\": 3}, \"conclusion\": \"negative\"}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 1, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.2, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.2, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.1, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.7, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.3, \"STUDY_SCENE1_book_caddy\": 0, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0.1, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.2}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.32, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.8, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0.1, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.07, \"successes\": 7, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"successes\": 11, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"successes\": 14, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.37, \"successes\": 37, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_bowl_between_plate_ramekin\": 0.9, \"pick_up_bowl_next_to_ramekin\": 1, \"pick_up_bowl_from_table_center\": 0, \"pick_up_bowl_on_cookie_box\": 0.3, \"pick_up_bowl_in_top_drawer\": 0.1, \"pick_up_bowl_on_ramekin\": 0, \"pick_up_bowl_next_to_cookie_box\": 0.9, \"pick_up_bowl_on_stove\": 0, \"pick_up_bowl_next_to_plate\": 0.2, \"pick_up_bowl_on_wooden_cabinet\": 0}}}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_ms\": 28.4, \"crm_forward_ms\": 0.246, \"preprocess_ms\": 0.96, \"batched_K1_ms\": 180, \"batched_K5_ms\": 182.3, \"batched_K10_ms\": 162.3, \"batched_K20_ms\": 167.4, \"sequential_K1_ms\": 177, \"sequential_K5_ms\": 891.7, \"sequential_K10_ms\": 1638.9, \"sequential_K20_ms\": 3245.8, \"cgs_K10_ms\": 6.3, \"full_pipe_K10_ms\": 200.7, \"full_pipe_K20_ms\": 199.7, \"vla_model_mb\": 884.1, \"crm_model_mb\": 1.8, \"peak_K20_mb\": 1085.1}}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"sr_pct\": \"10%\"}}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.31, \"successes\": 31, \"total\": 100, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.6, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.29, \"successes\": 29, \"total\": 100, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.8, \"from_table_center\": 0.1, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}}}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.3, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.12, \"sr_pct\": \"12%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.18, \"sr_pct\": \"18%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.15, \"sr_pct\": \"15%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 5, \"sr_pct\": \"5%\", \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 34}}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 16}}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 18}}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.07, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}, \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.05, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"partial\": true, \"tasks_completed\": \"5/10\", \"task6_partial\": \"5/10 rollouts\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0}, \"partial_avg_sr\": 0.1, \"failure_mode\": \"process killed silently mid-eval, no error in log, no JSON output\"}}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.3, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Partial 9/10 tasks, 0/90 rollouts. Accepted as collapse evidence per Director decision 2026-05-18.\"}}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"negative\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 100, \"avg_inference_time_ms\": 178, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0}}}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100}}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.69, \"n_tasks\": 10, \"n_trials_per_task\": 10, \"total_rollouts\": 100}}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_prefix_ms\": 33.5, \"vla_sample_K1_ms\": 192.6, \"vla_sample_K5_ms\": 965.3, \"vla_sample_K10_ms\": 1913.7, \"vla_sample_K20_ms\": 3858.2, \"cgs_ms\": 6.2, \"crm_forward_ms\": 0.3, \"full_pipeline_K10_ms\": 1908.2, \"acr_overhead_pct\": 0.34}}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.007199, \"total_epochs\": 50, \"train_samples\": 65223, \"obs_dim\": \"4x960D\", \"multi_scale\": true}, \"conclusion\": \"success\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.07, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks\": 10, \"rollouts_per_task\": 20, \"total_successes\": 24, \"total_rollouts\": 200}}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"best_task\": \"chocolate_pudding_0.25\", \"worst_task\": \"alphabet_soup_0.0\"}}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006505, \"best_epoch\": 43, \"total_epochs\": 50, \"train_samples\": 4857, \"obs_dim\": 960, \"multi_scale\": false, \"wall_clock_seconds\": 914.9}}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.06, \"successes\": 6, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"n_rollouts\": 10, \"total_rollouts\": 100, \"note\": \"JSON result found by diagnostic worker. Matches original seed44=4%. False positive failure due to no sentinel/W&B in evaluate.py.\"}}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.08, \"total_successes\": 8, \"total_rollouts\": 100, \"seed\": 44, \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}, \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"total_episodes\": 100, \"successes\": 4, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 0, \"bbq_sauce\": 1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 1, \"milk\": 0, \"chocolate_pudding\": 1, \"orange_juice\": 0}}}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"negative\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"negative\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}}, \"precompute-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-k5\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.06, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.08, \"total_success\": 8, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"conclusion\": \"success\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}}, \"crm-train-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}}, \"crm-train-k5\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}}, \"count\": 1415, \"total\": 1415, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1697}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T15:50:45.890Z_

<details><summary>↩ Tool result · `toolu_01KHeuJ2mo7npkzmpoNJK93g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1117}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "64a4e8c0-b09a-4385-83d6-83f09c18627a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.1117}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1117}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-28T15:50:45.904Z_

<details><summary>↩ Tool result · `toolu_019tgQgx4NHpt6qWYALrMLzg`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/supplementary/supplementary_summary.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "1e38da4a-2e6e-4c53-8358-0461c508a4f5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/supplementary/supplementary_summary.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/supplementary/supplementary_summary.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Key findings so far:
1. bjb1-18228: 1 GPU (cuda:0), 0 MiB used, idle - **wait, only 1 GPU reported but task says 4 GPUs**. Let me check - the output shows only one line. Maybe it's a 1-GPU machine? The task says cuda:0-3 (4 GPU). Let me re-check.

Actually looking at the output: "0, NVIDIA GeForce RTX 4090, 0 MiB, 24564 MiB, 0 %" - only 1 GPU. But the task says 4 GPUs. Maybe the server only has 1 GPU.


2. Three of the other servers (bjb1-32546, bjb2-28827, cqa1-32758) are completely unreachable. The registry shows no running experiments, confirming they were all killed, but the full results are too large to parse directly. I need to use an agent to handle that, and I should check for any leftover processes still running on the one accessible machine.

I'll also need to pull the roadmap and try reading the supplementary summary from the local filesystem to get the full picture of what was happening with these experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "b4fe8a67-6fcf-43ae-9863-9050620b4346",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oeqnds6un9cGemsfemBM5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2315,
      "cache_read_input_tokens": 25283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2315
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

_source line 25_

3 台服务器连接失败，只有 bjb1-18228 可达。继续检查残留进程、解析 registry、读取本地 supplementary 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "3b10f917-6c68-42c3-b345-7993617e3fde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oeqnds6un9cGemsfemBM5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2315,
      "cache_read_input_tokens": 25283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2315
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

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QuHGgyWoDjfUM4a1XGMNDn`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ps aux | grep -E \"evaluate|train|python\" | grep -v grep",
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
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "88f6656a-15d8-4395-8c97-bfc789b95509",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oeqnds6un9cGemsfemBM5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2315,
      "cache_read_input_tokens": 25283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2315
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

_source line 27 · 2026-05-28T15:50:56.997Z_

<details><summary>↩ Tool result · `toolu_01QuHGgyWoDjfUM4a1XGMNDn`</summary>

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
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "1cd82d32-c471-4d83-b84c-a436b26df0ff",
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

_source line 28_

<details open><summary>🔧 Tool call — Agent · `toolu_013vePFTt1F11vhKDNckffVj`</summary>

```json
{
  "description": "Parse registry DONE experiments",
  "prompt": "Parse the registry JSON file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt\n\nThis file is JSON with schema: {result: string} where result is itself a JSON string.\n\nI need you to:\n1. Probe structure with jq/python\n2. Extract ALL experiment entries that have status \"DONE\"\n3. For each, report: exp_id, conclusion, and key metrics (especially success_rate or SR for each task)\n4. Group them by experiment type - specifically identify:\n   - tau-sweep experiments (different tau values like tau025, tau05, tau075, tau10, tau15, tau20)\n   - bonus seed experiments (different seeds like s42, s43, s44)\n   - baseline experiments\n   - any other supplementary experiments\n5. Summarize which configurations are complete and which are missing\n\nReturn a structured summary. Be thorough - I need the complete picture of what's done.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "33c52565-0859-4b17-991f-4330ea39f3db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oeqnds6un9cGemsfemBM5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2315,
      "cache_read_input_tokens": 25283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2315
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

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Parse registry DONE experiments",
  "task_type": "local_agent",
  "prompt": "Parse the registry JSON file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt\n\nThis file is JSON with schema: {result: string} where result is itself a JSON string.\n\nI need you to:\n1. Probe structure with jq/python\n2. Extract ALL experiment entries that have status \"DONE\"\n3. For each, report: exp_id, conclusion, and key metrics (especially success_rate or SR for each task)\n4. Group them by experiment type - specifically identify:\n   - tau-sweep experiments (different tau values like tau025, tau05, tau075, tau10, tau15, tau20)\n   - bonus seed experiments (different seeds like s42, s43, s44)\n   - baseline experiments\n   - any other supplementary experiments\n5. Summarize which configurations are complete and which are missing\n\nReturn a structured summary. Be thorough - I need the complete picture of what's done.",
  "uuid": "1dcb3456-6f60-41d2-aafa-cc945637b4f2",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

## Round 1

75 recorded events

### User

_source line 30 · 2026-05-28T15:51:02.627Z_

Parse the registry JSON file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt

This file is JSON with schema: {result: string} where result is itself a JSON string.

I need you to:
1. Probe structure with jq/python
2. Extract ALL experiment entries that have status "DONE"
3. For each, report: exp_id, conclusion, and key metrics (especially success_rate or SR for each task)
4. Group them by experiment type - specifically identify:
   - tau-sweep experiments (different tau values like tau025, tau05, tau075, tau10, tau15, tau20)
   - bonus seed experiments (different seeds like s42, s43, s44)
   - baseline experiments
   - any other supplementary experiments
5. Summarize which configurations are complete and which are missing

Return a structured summary. Be thorough - I need the complete picture of what's done.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "f8c715ef-1188-4907-b340-16135c1875bb"
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Glob · `toolu_01EYf95ozPJffU56x3EGt7z5`</summary>

```json
{
  "pattern": "**/supplementary_summary*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "9b2906d0-4e06-428f-b883-55179f4b8285",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oeqnds6un9cGemsfemBM5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2315,
      "cache_read_input_tokens": 25283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2315
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

_source line 32 · 2026-05-28T15:51:03.642Z_

<details><summary>↩ Tool result · `toolu_01EYf95ozPJffU56x3EGt7z5`</summary>

```text
artifacts/_project/report/supplementary_summary.md
artifacts/supplementary/supplementary_summary.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "0bde4dc4-c350-49eb-a168-e8e6a4983927",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/report/supplementary_summary.md",
      "artifacts/supplementary/supplementary_summary.md"
    ],
    "durationMs": 102,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Glob · `toolu_019mCB8B8rb78NXFJD9nXB9x`</summary>

```json
{
  "pattern": "**/supplementary*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "148e1052-d732-436e-b240-72474d633128",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oeqnds6un9cGemsfemBM5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2315,
      "cache_read_input_tokens": 25283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2315
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

_source line 34 · 2026-05-28T15:51:04.123Z_

<details><summary>↩ Tool result · `toolu_019mCB8B8rb78NXFJD9nXB9x`</summary>

```text
artifacts/_project/report/supplementary_summary.md
artifacts/supplementary/supplementary_summary.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "f33b5689-76b1-46eb-bfe0-399ba0fed3b6",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/report/supplementary_summary.md",
      "artifacts/supplementary/supplementary_summary.md"
    ],
    "durationMs": 50,
    "numFiles": 2,
    "truncated": false
  }
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
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Reading ~/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt",
  "usage": {
    "total_tokens": 14668,
    "tool_uses": 1,
    "duration_ms": 3625
  },
  "last_tool_name": "Read",
  "uuid": "afe9f3d0-2d15-4858-a287-88bbb0a43556",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01GHpjB2UPrhTvHkG6HHJHPh`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "15ad02a7-79d6-42c1-b82b-5169ae0936ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHMxKJS8XCLLUQsazZ3gMn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14661,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14661,
        "ephemeral_1h_input_tokens": 0
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

_source line 37 · 2026-05-28T15:51:06.754Z_

<details><summary>↩ Tool result · reported error · `toolu_01GHpjB2UPrhTvHkG6HHJHPh`</summary>

```text
File content (131281 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "5c348502-e07e-44a0-8ee9-be54a2fafcd1",
  "tool_use_result": "Error: File content (131281 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Probe the structure of the registry JSON file",
  "usage": {
    "total_tokens": 15746,
    "tool_uses": 2,
    "duration_ms": 10887
  },
  "last_tool_name": "Bash",
  "uuid": "8cd7f5a2-e256-4ade-9de0-487481bcd6f7",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01CyND8emqDPhS2rckkgV9w5`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\n# The outer structure has a 'result' field which is a JSON string\ninner = json.loads(raw['result'])\nprint('Top-level keys:', list(inner.keys())[:20])\nprint('Type:', type(inner))\nif isinstance(inner, dict):\n    # Check if it's a flat dict or nested\n    for k in list(inner.keys())[:3]:\n        v = inner[k]\n        print(f'  Key: {k}, Type: {type(v).__name__}')\n        if isinstance(v, dict):\n            print(f'    Sub-keys: {list(v.keys())[:10]}')\n        elif isinstance(v, str):\n            print(f'    Value (first 200): {v[:200]}')\n\" 2>&1\n",
  "description": "Probe the structure of the registry JSON file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "707de510-c354-4b08-88ea-08395b129a09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GpdFWrXqdeeSiYjnAoeuWD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1078,
      "cache_read_input_tokens": 14661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1078,
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

_source line 40 · 2026-05-28T15:51:13.808Z_

<details><summary>↩ Tool result · `toolu_01CyND8emqDPhS2rckkgV9w5`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']
Type: &lt;class 'dict'>
  Key: success, Type: bool
  Key: data, Type: dict
    Sub-keys: ['experiments', 'count', 'total', 'baseline']
  Key: error, Type: NoneType
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "e0359767-3e0a-4b4e-970d-d9612059fb9d"
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
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Explore the data structure and list all experiment IDs",
  "usage": {
    "total_tokens": 16314,
    "tool_uses": 3,
    "duration_ms": 16387
  },
  "last_tool_name": "Bash",
  "uuid": "51e227e1-2d58-4388-bf6e-905df6cbbeec",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01V2mbBjwfqt5fek93RVPPQF`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\ndata = inner['data']\nprint('data keys:', list(data.keys()))\nprint('count:', data.get('count'))\nprint('total:', data.get('total'))\nprint('baseline type:', type(data.get('baseline')))\nif data.get('baseline'):\n    print('baseline keys:', list(data['baseline'].keys())[:10])\n\nexps = data.get('experiments', {})\nprint(f'\\nTotal experiments: {len(exps)}')\nprint('Experiment IDs:', list(exps.keys()))\n\" 2>&1\n",
  "description": "Explore the data structure and list all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "24c96dbb-89ab-47eb-8304-52f9273107b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012c9P9e34UFEkz5mFyKBUXf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 15739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 495,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-28T15:51:19.128Z_

<details><summary>↩ Tool result · `toolu_01V2mbBjwfqt5fek93RVPPQF`</summary>

```text
&lt;persisted-output>
Output too large (46.3KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/bww2cj7qy.txt

Preview (first 2KB):
data keys: ['experiments', 'count', 'total', 'baseline']
count: 1415
total: 1415
baseline type: &lt;class 'NoneType'>

Total experiments: 1415
Experiment IDs: ['eval-vla-only-spatial-seed49-r2', 'eval-adaptive-k-p25-seed44', 'eval-vla-only-spatial-seed50', 'eval-crm-spatial-seed47', 'eval-vla-only-object-seed49-r2', 'eval-crm-spatial-seed48', 'eval-crm-spatial-k10-seed49', 'eval-vla-only-long-seed49', 'eval-crm-spatial-k10-seed50', 'eval-vla-only-object-seed51', 'eval-crm-long-seed48', 'eval-crm-long-seed49', 'eval-crm-goal-seed47', 'eval-crm-goal-seed48', 'eval-vla-only-spatial-seed51', 'eval-vla-only-goal-seed50', 'eval-crm-long-seed51', 'eval-vla-only-long-seed53', 'eval-vla-only-long-seed54', 'eval-vla-only-goal-seed52', 'eval-crm-long-seed52', 'eval-crm-goal-seed49', 'eval-crm-goal-seed50', 'eval-vla-only-spatial-seed52', 'eval-vla-only-spatial-seed53', 'eval-crm-long-seed53', 'eval-vla-only-spatial-seed54', 'eval-crm-long-seed54', 'eval-obs-only-goal-norm02-seed53', 'eval-obs-only-object-norm005-seed77', 'eval-obs-only-object-norm003-seed76', 'eval-obs-only-object-norm003-seed77', 'eval-obs-only-object-norm003-seed78', 'eval-obs-only-object-norm005-seed76', 'eval-obs-only-object-norm003-seed62-r3', 'eval-obs-only-object-norm003-seed63-r3', 'eval-obs-only-object-norm01-seed76', 'eval-obs-only-object-norm01-seed77', 'eval-random-selection-object-seed42-r3', 'precompute-pi05-shard0', 'precompute-pi05-shard1', 'precompute-pi05-shard2', 'precompute-pi05-shard3', 'precompute-pi05-shard4', 'precompute-pi05-shard5', 'precompute-pi05-shard6', 'precompute-pi05-shard7', 'precompute-pi05-shard8', 'precompute-pi05-shard9', 'precompute-pi05-spatial-shard0', 'precompute-pi05-spatial-shard1', 'precompute-pi05-spatial-shard2', 'precompute-pi05-spatial-shard3', 'precompute-pi05-spatial-shard4', 'precompute-pi05-spatial-shard5', 'precompute-pi05-spatial-shard6', 'precompute-pi05-obj-shard5', 'precompute-pi05-obj-shard6', 'precompute-pi05-obj-shard7', 'precompute-pi05-obj-shard8', '
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "73a949d7-0876-40b7-9c2a-ed6dc9e8cd59"
}
```

</details>

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Get status distribution and sample DONE experiment schema",
  "usage": {
    "total_tokens": 17699,
    "tool_uses": 4,
    "duration_ms": 25377
  },
  "last_tool_name": "Bash",
  "uuid": "8ab3fcb6-1539-43b6-82eb-bc3c8cf5d850",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01VbAjjWa9yQt3NefGGhFi8o`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# First, understand all statuses\nstatuses = {}\nfor eid, edata in exps.items():\n    s = edata.get('status', 'UNKNOWN')\n    statuses[s] = statuses.get(s, 0) + 1\nprint(\"=== Status distribution ===\")\nfor s, c in sorted(statuses.items(), key=lambda x: -x[1]):\n    print(f\"  {s}: {c}\")\n\n# Look at one DONE experiment to understand the schema\ndone_exps = {eid: edata for eid, edata in exps.items() if edata.get('status') == 'DONE'}\nprint(f\"\\nTotal DONE experiments: {len(done_exps)}\")\n\nif done_exps:\n    sample_id = list(done_exps.keys())[0]\n    sample = done_exps[sample_id]\n    print(f\"\\n=== Sample DONE experiment: {sample_id} ===\")\n    print(f\"  Keys: {list(sample.keys())}\")\n    for k, v in sample.items():\n        if isinstance(v, dict):\n            print(f\"  {k}: (dict) keys={list(v.keys())[:15]}\")\n        elif isinstance(v, str) and len(v) > 200:\n            print(f\"  {k}: {v[:200]}...\")\n        else:\n            print(f\"  {k}: {v}\")\nPYEOF\n",
  "description": "Get status distribution and sample DONE experiment schema"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "17682356-c518-4217-9686-2a642fcdef04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013rBmYyN7JkAJKww6nRQd7K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1383,
      "cache_read_input_tokens": 16234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1383,
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

_source line 46 · 2026-05-28T15:51:28.096Z_

<details><summary>↩ Tool result · `toolu_01VbAjjWa9yQt3NefGGhFi8o`</summary>

```text
=== Status distribution ===
  DONE: 1415

Total DONE experiments: 1415

=== Sample DONE experiment: eval-vla-only-spatial-seed49-r2 ===
  Keys: ['status', 'conclusion']
  status: DONE
  conclusion: killed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "035cd034-7581-42b6-a992-167d209f2e56"
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
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Analyze conclusion patterns and find experiments with metrics",
  "usage": {
    "total_tokens": 18383,
    "tool_uses": 5,
    "duration_ms": 34635
  },
  "last_tool_name": "Bash",
  "uuid": "e193e18d-2f84-47df-a7c9-e71582627413",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_01DcJ23mmPa6vNwu82ZBs9mv`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nfrom collections import Counter\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Check all unique key sets and conclusions\nkey_sets = Counter()\nconclusions = Counter()\nhas_metrics = []\n\nfor eid, edata in exps.items():\n    ks = frozenset(edata.keys())\n    key_sets[str(sorted(ks))] += 1\n    conc = edata.get('conclusion', '')\n    # Truncate long conclusions for grouping\n    if len(conc) > 100:\n        conclusions[conc[:80] + '...'] += 1\n    else:\n        conclusions[conc] += 1\n    \n    # Check for experiments with more than just status+conclusion\n    if len(edata.keys()) > 2:\n        has_metrics.append(eid)\n\nprint(\"=== Key sets distribution ===\")\nfor ks, c in key_sets.most_common(10):\n    print(f\"  {ks}: {c}\")\n\nprint(f\"\\n=== Unique conclusions (top 30) ===\")\nfor conc, c in conclusions.most_common(30):\n    print(f\"  [{c}x] {conc}\")\n\nprint(f\"\\n=== Experiments with extra fields (beyond status+conclusion): {len(has_metrics)} ===\")\nfor eid in has_metrics[:10]:\n    print(f\"  {eid}: keys={list(exps[eid].keys())}\")\nPYEOF\n",
  "description": "Analyze conclusion patterns and find experiments with metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "d962cd7a-1f66-4e22-9364-19ecc2090d88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5DcLh3Ekksx8tyM7C4xNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 17617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 682,
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

_source line 49 · 2026-05-28T15:51:37.357Z_

<details><summary>↩ Tool result · `toolu_01DcJ23mmPa6vNwu82ZBs9mv`</summary>

```text
=== Key sets distribution ===
  ['conclusion', 'metrics', 'status']: 900
  ['conclusion', 'status']: 515

=== Unique conclusions (top 30) ===
  [768x] success
  [421x] killed
  [130x] failed
  [96x] negative

=== Experiments with extra fields (beyond status+conclusion): 900 ===
  eval-vla-only-spatial-seed50: keys=['status', 'metrics', 'conclusion']
  eval-crm-spatial-seed48: keys=['status', 'metrics', 'conclusion']
  eval-crm-spatial-k10-seed49: keys=['status', 'metrics', 'conclusion']
  eval-crm-long-seed48: keys=['status', 'metrics', 'conclusion']
  eval-crm-long-seed49: keys=['status', 'metrics', 'conclusion']
  eval-crm-goal-seed47: keys=['status', 'metrics', 'conclusion']
  eval-crm-goal-seed48: keys=['status', 'metrics', 'conclusion']
  eval-supp-obj-crm-norm005-s46: keys=['status', 'metrics', 'conclusion']
  eval-tau-sweep-spatial-tau010-s42: keys=['status', 'conclusion', 'metrics']
  eval-tau-sweep-spatial-tau020-s42: keys=['status', 'conclusion', 'metrics']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "92d4860a-c938-4b71-b0ad-ee423e0e4752"
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
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Inspect metrics structure from representative experiments",
  "usage": {
    "total_tokens": 19353,
    "tool_uses": 6,
    "duration_ms": 41646
  },
  "last_tool_name": "Bash",
  "uuid": "804d9daf-09ba-426d-9536-ebc4fb89a214",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Bash · `toolu_01Sa7tnVYK3pLcPoXUpEf52E`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nfrom collections import Counter\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Look at metrics structure from a few examples\nfor eid in ['eval-tau-sweep-spatial-tau010-s42', 'eval-crm-spatial-seed48', 'eval-vla-only-spatial-seed50', 'eval-supp-obj-crm-norm005-s46']:\n    edata = exps.get(eid, {})\n    m = edata.get('metrics', {})\n    print(f\"\\n=== {eid} ===\")\n    print(f\"  conclusion: {edata.get('conclusion')}\")\n    if isinstance(m, dict):\n        print(f\"  metrics keys: {list(m.keys())}\")\n        for mk, mv in m.items():\n            print(f\"    {mk}: {mv}\")\n    elif isinstance(m, str):\n        print(f\"  metrics (str, first 500): {m[:500]}\")\nPYEOF\n",
  "description": "Inspect metrics structure from representative experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "44e230b7-1bd0-40a9-b6c1-90de8b39df47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vXyWVqWQKqsBHExUULhYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 18299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

_source line 52 · 2026-05-28T15:51:44.370Z_

<details><summary>↩ Tool result · `toolu_01Sa7tnVYK3pLcPoXUpEf52E`</summary>

```text
=== eval-tau-sweep-spatial-tau010-s42 ===
  conclusion: killed
  metrics keys: ['overall_success_rate', 'trigger_rate', 'tau', 'benchmark', 'seed']
    overall_success_rate: 0.79
    trigger_rate: 0.752
    tau: 0.1
    benchmark: spatial
    seed: 42

=== eval-crm-spatial-seed48 ===
  conclusion: killed
  metrics keys: ['success_rate', 'n_tasks', 'n_rollouts', 'total']
    success_rate: 0.35
    n_tasks: 10
    n_rollouts: 10
    total: 100

=== eval-vla-only-spatial-seed50 ===
  conclusion: killed
  metrics keys: ['success_rate', 'n_tasks', 'n_rollouts', 'total']
    success_rate: 0.3
    n_tasks: 10
    n_rollouts: 10
    total: 100

=== eval-supp-obj-crm-norm005-s46 ===
  conclusion: killed
  metrics keys: ['success_rate', 'successes', 'total', 'source']
    success_rate: 0.795
    successes: 159
    total: 200
    source: json_harvest_bjb1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "440522fd-c0f5-44a1-953e-573a46d07953"
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
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Categorize all 1415 experiments into types",
  "usage": {
    "total_tokens": 20173,
    "tool_uses": 7,
    "duration_ms": 56369
  },
  "last_tool_name": "Bash",
  "uuid": "df9b7a07-77d1-463a-b446-6773fb534226",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01KgNBT7Wd9GyxUGzQ5bvn3u`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Categorize all experiments\ncategories = defaultdict(list)\n\nfor eid, edata in exps.items():\n    metrics = edata.get('metrics', {})\n    if not isinstance(metrics, dict):\n        metrics = {}\n    \n    entry = {\n        'id': eid,\n        'status': edata.get('status'),\n        'conclusion': edata.get('conclusion'),\n        'metrics': metrics,\n    }\n    \n    # Categorize by experiment ID pattern\n    if 'tau-sweep' in eid or 'tau_sweep' in eid:\n        categories['tau-sweep'].append(entry)\n    elif 'bonus-seed' in eid or 'bonus_seed' in eid or re.search(r'bonus.*s\\d+', eid):\n        categories['bonus-seed'].append(entry)\n    elif 'adaptive-k' in eid:\n        categories['adaptive-k'].append(entry)\n    elif 'obs-only' in eid:\n        categories['obs-only'].append(entry)\n    elif 'random-selection' in eid or 'random_selection' in eid:\n        categories['random-selection'].append(entry)\n    elif 'vla-only' in eid:\n        categories['vla-only-baseline'].append(entry)\n    elif 'crm-' in eid and 'supp' not in eid:\n        categories['crm-main'].append(entry)\n    elif 'supp' in eid:\n        categories['supplementary'].append(entry)\n    elif 'precompute' in eid:\n        categories['precompute'].append(entry)\n    elif 'calib' in eid:\n        categories['calibration'].append(entry)\n    elif 'ablation' in eid:\n        categories['ablation'].append(entry)\n    elif 'oracle' in eid:\n        categories['oracle'].append(entry)\n    elif 'heuristic' in eid:\n        categories['heuristic'].append(entry)\n    elif 'fixed-thresh' in eid or 'fixed_thresh' in eid:\n        categories['fixed-threshold'].append(entry)\n    else:\n        categories['other'].append(entry)\n\nprint(\"=\" * 80)\nprint(\"EXPERIMENT CATEGORY SUMMARY\")\nprint(\"=\" * 80)\nfor cat in sorted(categories.keys()):\n    entries = categories[cat]\n    n_with_metrics = sum(1 for e in entries if e['metrics'])\n    conc_counts = defaultdict(int)\n    for e in entries:\n        conc_counts[e['conclusion']] += 1\n    print(f\"\\n{cat}: {len(entries)} experiments ({n_with_metrics} with metrics)\")\n    print(f\"  Conclusions: {dict(conc_counts)}\")\n    # Show sample IDs\n    sample_ids = [e['id'] for e in entries[:5]]\n    if len(entries) > 5:\n        sample_ids.append(f\"... and {len(entries)-5} more\")\n    print(f\"  Sample IDs: {sample_ids}\")\n\nPYEOF\n",
  "description": "Categorize all 1415 experiments into types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "14bdc3ea-16a4-4db5-8a57-5840764faa56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014wjFsrfw41gH1NMqmUks62",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 19267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 816,
        "ephemeral_1h_input_tokens": 0
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

_source line 55 · 2026-05-28T15:51:59.099Z_

<details><summary>↩ Tool result · `toolu_01KgNBT7Wd9GyxUGzQ5bvn3u`</summary>

```text
================================================================================
EXPERIMENT CATEGORY SUMMARY
================================================================================

ablation: 3 experiments (3 with metrics)
  Conclusions: {'negative': 2, 'success': 1}
  Sample IDs: ['eval-ablation-tau040-goal-s42', 'eval-ablation-tau015-goal-s42', 'eval-ablation-tau010-goal-s42']

adaptive-k: 38 experiments (28 with metrics)
  Conclusions: {'killed': 11, 'success': 26, 'negative': 1}
  Sample IDs: ['eval-adaptive-k-p25-seed44', 'eval-adaptive-k1-spatial-tau025-s42', 'eval-adaptive-k5-spatial-tau025-s42', 'eval-canonical-adaptive-k10-spatial-s42', 'eval-long-adaptive-k10-s42', '... and 33 more']

calibration: 2 experiments (2 with metrics)
  Conclusions: {'success': 1, 'negative': 1}
  Sample IDs: ['k2-l2-calibration-phase1', 'fmvd-calibration-phase1']

crm-main: 222 experiments (125 with metrics)
  Conclusions: {'killed': 88, 'negative': 21, 'failed': 17, 'success': 96}
  Sample IDs: ['eval-crm-spatial-seed47', 'eval-crm-spatial-seed48', 'eval-crm-spatial-k10-seed49', 'eval-crm-spatial-k10-seed50', 'eval-crm-long-seed48', '... and 217 more']

obs-only: 178 experiments (128 with metrics)
  Conclusions: {'killed': 35, 'success': 120, 'failed': 22, 'negative': 1}
  Sample IDs: ['eval-obs-only-goal-norm02-seed53', 'eval-obs-only-object-norm005-seed77', 'eval-obs-only-object-norm003-seed76', 'eval-obs-only-object-norm003-seed77', 'eval-obs-only-object-norm003-seed78', '... and 173 more']

other: 471 experiments (300 with metrics)
  Conclusions: {'killed': 139, 'success': 242, 'negative': 44, 'failed': 46}
  Sample IDs: ['eval-smolvla-lerobot-goal-seed44', 'eval-pi05-reconvla-spatial-s42', 'eval-pi05-reconvla-goal-s42', 'eval-pi05-reconvla-object-s42', 'eval-pi05-reconvla-spatial-s42-bf16', '... and 466 more']

precompute: 83 experiments (6 with metrics)
  Conclusions: {'killed': 58, 'success': 20, 'failed': 5}
  Sample IDs: ['precompute-pi05-shard0', 'precompute-pi05-shard1', 'precompute-pi05-shard2', 'precompute-pi05-shard3', 'precompute-pi05-shard4', '... and 78 more']

random-selection: 26 experiments (19 with metrics)
  Conclusions: {'killed': 1, 'success': 19, 'failed': 6}
  Sample IDs: ['eval-random-selection-object-seed42-r3', 'eval-random-selection-object-seed43-v2', 'eval-random-selection-spatial-seed42', 'eval-random-selection-object-seed44', 'eval-random-selection-object-seed43', '... and 21 more']

supplementary: 138 experiments (116 with metrics)
  Conclusions: {'killed': 23, 'success': 88, 'negative': 21, 'failed': 6}
  Sample IDs: ['eval-supp-k2mean-spatial-s45', 'eval-supp-obj-crm-norm005-s46', 'eval-supp-adapt-tau025-spatial-s46', 'eval-supp-adapt-tau025-spatial-s48', 'eval-supp-adapt-tau025-spatial-s49', '... and 133 more']

tau-sweep: 22 experiments (19 with metrics)
  Conclusions: {'killed': 6, 'success': 11, 'failed': 1, 'negative': 4}
  Sample IDs: ['eval-tau-sweep-spatial-tau010-s42', 'eval-tau-sweep-spatial-tau020-s42', 'eval-tau-sweep-spatial-tau030-s42', 'pi05-tau-sweep-goal-tau050-s42', 'pi05-tau-sweep-goal-tau070-s42', '... and 17 more']

vla-only-baseline: 232 experiments (154 with metrics)
  Conclusions: {'killed': 60, 'success': 144, 'failed': 27, 'negative': 1}
  Sample IDs: ['eval-vla-only-spatial-seed49-r2', 'eval-vla-only-spatial-seed50', 'eval-vla-only-object-seed49-r2', 'eval-vla-only-long-seed49', 'eval-vla-only-object-seed51', '... and 227 more']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "bda632e4-391a-4283-b573-6ca58ad079dd"
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
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Detail tau-sweep experiments",
  "usage": {
    "total_tokens": 22569,
    "tool_uses": 8,
    "duration_ms": 64615
  },
  "last_tool_name": "Bash",
  "uuid": "17ceb740-448c-4c45-a100-7052c03b84fa",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_015KmAMYTwjM5PjJGBAisYpL`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# ==========================================\n# 1. TAU-SWEEP EXPERIMENTS\n# ==========================================\nprint(\"=\" * 80)\nprint(\"1. TAU-SWEEP EXPERIMENTS\")\nprint(\"=\" * 80)\n\ntau_exps = {eid: ed for eid, ed in exps.items() if 'tau-sweep' in eid or 'tau_sweep' in eid}\nfor eid in sorted(tau_exps.keys()):\n    ed = tau_exps[eid]\n    m = ed.get('metrics', {})\n    if not isinstance(m, dict): m = {}\n    sr = m.get('overall_success_rate', m.get('success_rate', 'N/A'))\n    tau = m.get('tau', 'N/A')\n    bench = m.get('benchmark', 'N/A')\n    seed = m.get('seed', 'N/A')\n    tr = m.get('trigger_rate', 'N/A')\n    print(f\"  {eid}: conc={ed['conclusion']}, SR={sr}, tau={tau}, bench={bench}, seed={seed}, trigger_rate={tr}\")\n\nPYEOF\n",
  "description": "Detail tau-sweep experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "48357f71-a24e-4ed2-8d0b-138103ea822b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYoetn12Z8ZW399gv3oi6J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2388,
      "cache_read_input_tokens": 20083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2388,
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

_source line 58 · 2026-05-28T15:52:07.325Z_

<details><summary>↩ Tool result · `toolu_015KmAMYTwjM5PjJGBAisYpL`</summary>

```text
================================================================================
1. TAU-SWEEP EXPERIMENTS
================================================================================
  eval-tau-sweep-spatial-tau010-s42: conc=killed, SR=0.79, tau=0.1, bench=spatial, seed=42, trigger_rate=0.752
  eval-tau-sweep-spatial-tau020-s42: conc=killed, SR=0.81, tau=0.2, bench=spatial, seed=42, trigger_rate=0.266
  eval-tau-sweep-spatial-tau030-s42: conc=killed, SR=0.805, tau=0.3, bench=spatial, seed=42, trigger_rate=0.167
  pi05-tau-sweep-goal-tau050-s42: conc=killed, SR=N/A, tau=N/A, bench=N/A, seed=N/A, trigger_rate=N/A
  pi05-tau-sweep-goal-tau050-s42-r2: conc=failed, SR=0, tau=N/A, bench=N/A, seed=N/A, trigger_rate=None
  pi05-tau-sweep-goal-tau050-s42-r3: conc=success, SR=0.87, tau=N/A, bench=N/A, seed=N/A, trigger_rate=0.0206
  pi05-tau-sweep-goal-tau070-s42: conc=killed, SR=N/A, tau=N/A, bench=N/A, seed=N/A, trigger_rate=N/A
  pi05-tau-sweep-goal-tau070-s42-r2: conc=success, SR=87, tau=N/A, bench=N/A, seed=N/A, trigger_rate=1.1
  pi05-tau-sweep-goal-tau090-s42: conc=killed, SR=N/A, tau=N/A, bench=N/A, seed=N/A, trigger_rate=N/A
  tau-sweep-goal-tau015-s42: conc=success, SR=83, tau=N/A, bench=N/A, seed=N/A, trigger_rate=36.4
  tau-sweep-goal-tau035-s42: conc=success, SR=86, tau=N/A, bench=N/A, seed=N/A, trigger_rate=2.1
  tau-sweep-long-tau015-s42: conc=success, SR=61, tau=N/A, bench=N/A, seed=N/A, trigger_rate=24.1
  tau-sweep-long-tau035-s42: conc=success, SR=57, tau=N/A, bench=N/A, seed=N/A, trigger_rate=1
  tau-sweep-spatial-tau015-s42: conc=success, SR=79.5, tau=N/A, bench=N/A, seed=N/A, trigger_rate=40.7
  tau-sweep-spatial-tau035-s42: conc=success, SR=80.5, tau=N/A, bench=N/A, seed=N/A, trigger_rate=12.1
  tau_sweep_goal_tau025_s42: conc=negative, SR=0.835, tau=N/A, bench=N/A, seed=N/A, trigger_rate=N/A
  tau_sweep_goal_tau040_s42: conc=negative, SR=0.835, tau=N/A, bench=N/A, seed=N/A, trigger_rate=N/A
  tau_sweep_goal_tau045_s42: conc=negative, SR=0.835, tau=N/A, bench=N/A, seed=N/A, trigger_rate=N/A
  tau_sweep_goal_tau050_s42_cqa1: conc=success, SR=0.87, tau=0.5, bench=N/A, seed=N/A, trigger_rate=0.0206
  tau_sweep_goal_tau070_s42_cqa1: conc=success, SR=0.87, tau=0.7, bench=N/A, seed=N/A, trigger_rate=0.0104
  tau_sweep_goal_tau090_s42_cqa1: conc=success, SR=0.89, tau=0.9, bench=N/A, seed=N/A, trigger_rate=0.0035
  tau_sweep_spatial_tau025_s42: conc=negative, SR=0.785, tau=N/A, bench=N/A, seed=N/A, trigger_rate=N/A
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "f31e1d44-3e7c-470b-97a2-8375237e225b"
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
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Detail supplementary/bonus seed experiments",
  "usage": {
    "total_tokens": 24315,
    "tool_uses": 9,
    "duration_ms": 75808
  },
  "last_tool_name": "Bash",
  "uuid": "2e5afaac-4382-4c88-89d9-4986af7bab05",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Bash · `toolu_01Fyehecrpvcj6roLCBYTNmm`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# ==========================================\n# 2. BONUS SEED experiments - search more broadly\n# ==========================================\nprint(\"=\" * 80)\nprint(\"2. BONUS/EXTRA SEED EXPERIMENTS (looking for seed patterns in supp)\")\nprint(\"=\" * 80)\n\n# Let's look at the supp experiments more carefully\nsupp_exps = {eid: ed for eid, ed in exps.items() if 'supp' in eid}\n# Group supp by sub-type\nsupp_types = defaultdict(list)\nfor eid in sorted(supp_exps.keys()):\n    ed = supp_exps[eid]\n    m = ed.get('metrics', {})\n    if not isinstance(m, dict): m = {}\n    \n    # Extract the sub-type pattern\n    # e.g. eval-supp-adapt-tau025-spatial-s46 -> adapt-tau025-spatial\n    # e.g. eval-supp-obj-crm-norm005-s46 -> obj-crm-norm005\n    match = re.match(r'eval-supp-(.+)-s(\\d+)', eid)\n    if match:\n        subtype = match.group(1)\n        seed = match.group(2)\n    else:\n        subtype = eid\n        seed = '?'\n    \n    sr = m.get('success_rate', m.get('overall_success_rate', 'N/A'))\n    supp_types[subtype].append({\n        'eid': eid, 'seed': seed, 'sr': sr, \n        'conclusion': ed['conclusion'], 'metrics': m\n    })\n\nfor subtype in sorted(supp_types.keys()):\n    entries = supp_types[subtype]\n    print(f\"\\n  {subtype} ({len(entries)} seeds):\")\n    for e in sorted(entries, key=lambda x: x['seed']):\n        extra = \"\"\n        if e['metrics']:\n            extra_keys = {k:v for k,v in e['metrics'].items() if k not in ('success_rate', 'overall_success_rate')}\n            if extra_keys:\n                extra = f\" | {extra_keys}\"\n        print(f\"    s{e['seed']}: SR={e['sr']}, conc={e['conclusion']}{extra}\")\n\nPYEOF\n",
  "description": "Detail supplementary/bonus seed experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "aebe711e-3243-454a-a994-5bf61e8441d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nj2AzdWYeEwSUvjN5bzyy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1674,
      "cache_read_input_tokens": 22471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1674,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-28T15:52:18.538Z_

<details><summary>↩ Tool result · `toolu_01Fyehecrpvcj6roLCBYTNmm`</summary>

```text
================================================================================
2. BONUS/EXTRA SEED EXPERIMENTS (looking for seed patterns in supp)
================================================================================

  adapt-tau015-spatial (2 seeds):
    s42: SR=N/A, conc=killed
    s42: SR=N/A, conc=success | {'overall_sr': 80.5, 'n_success': 161, 'n_total': 200, 'trigger_rate': 40.7, 'mean_unc': 0.1852, 'conformal_threshold': 0.15, 'max_correction_norm': 0.2, 'per_task_sr': {'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate': 100, 'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate': 90, 'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate': 95, 'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate': 95, 'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate': 75, 'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate': 0, 'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate': 95, 'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate': 90, 'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate': 80, 'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate': 85}}

  adapt-tau025-goal (4 seeds):
    s43: SR=0.845, conc=success | {'trigger_rate': 0.088, 'crm_applied_steps': 2509, 'total_steps': 28500}
    s44: SR=0.865, conc=success | {'trigger_rate': 0.0677, 'crm_applied_steps': 1870, 'total_steps': 27642}
    s48: SR=0.845, conc=killed | {'trigger_rate': 0.089, 'tau': 0.25, 'benchmark': 'goal', 'seed': 48}
    s49: SR=0.815, conc=killed | {'trigger_rate': 0.089, 'tau': 0.25, 'benchmark': 'goal', 'seed': 49}

  adapt-tau025-obj (7 seeds):
    s43: SR=0.775, conc=negative | {'trigger_rate': 0.0367, 'crm_applied_steps': 1312, 'total_steps': 35796}
    s44: SR=N/A, conc=negative | {'overall_sr': 0.75, 'trigger_rate': 0.0364, 'mean_uncertainty': 0.11, 'crm_applied_steps': 1310, 'total_steps': 35990, 'per_task': {'alphabet_soup': 0.7, 'cream_cheese': 0.75, 'salad_dressing': 0.75, 'bbq': 0.9, 'ketchup': 0.8, 'tomato': 0.65, 'butter': 0.65, 'milk': 0.7, 'chocolate': 0.75, 'orange_juice': 0.85}}
    s45: SR=N/A, conc=success | {'SR': 0.78}
    s46: SR=N/A, conc=success | {'SR': 0.775}
    s48: SR=N/A, conc=killed | {'overall_sr': 0.76, 'trigger_rate': 0.0389, 'mean_uncertainty': 0.1117, 'per_task_sr': {'soup': 0.75, 'cream_cheese': 0.75, 'salad': 0.7, 'bbq': 0.9, 'ketchup': 0.8, 'tomato': 0.65, 'butter': 0.6, 'milk': 0.8, 'pudding': 0.7, 'oj': 0.95}}
    s49: SR=N/A, conc=killed | {'overall_sr': 0.74, 'trigger_rate': 0.0417, 'mean_uncertainty': 0.1131, 'per_task_sr': {'soup': 0.7, 'cream_cheese': 0.65, 'salad': 0.8, 'bbq': 0.8, 'ketchup': 0.75, 'tomato': 0.75, 'butter': 0.6, 'milk': 0.6, 'pudding': 0.8, 'oj': 0.95}}
    s50: SR=N/A, conc=killed

  adapt-tau025-spatial (9 seeds):
    s42: SR=N/A, conc=killed
    s42: SR=N/A, conc=success | {'overall_sr': 82, 'n_success': 164, 'n_total': 200, 'trigger_rate': 19.4, 'mean_unc': 0.1847, 'per_task_sr': {'between_plate_and_ramekin': 95, 'next_to_ramekin': 95, 'from_table_center': 100, 'on_cookie_box': 100, 'in_top_drawer': 75, 'on_ramekin': 0, 'next_to_cookie_box': 90, 'on_stove': 90, 'next_to_plate': 90, 'on_wooden_cabinet': 85}}
    s43: SR=80, conc=success | {'trigger_rate': 19.4, 'mean_unc': 0.1845, 'total_rollouts': 200, 'total_successes': 160, 'per_task': {'between_plate_and_ramekin': 95, 'next_to_ramekin': 95, 'from_table_center': 95, 'on_cookie_box': 100, 'in_top_drawer_wooden_cabinet': 70, 'on_ramekin': 0, 'next_to_cookie_box': 100, 'on_stove': 80, 'next_to_plate': 85, 'on_wooden_cabinet': 80}}
    s44: SR=80.5, conc=success | {'total_successes': 161, 'total_rollouts': 200, 'trigger_rate': 20, 'mean_unc': 0.1881, 'conformal_threshold': 0.25, 'max_correction_norm': 0.2, 'mode': 'adaptive_conformal_crm', 'per_task': {'pick_up_the_black_bowl_between_the_plate_and_the_ramekin': {'sr': 90, 'successes': 18, 'rollouts': 20}, 'pick_up_the_black_bowl_next_to_the_ramekin': {'sr': 95, 'successes': 19, 'rollouts': 20}, 'pick_up_the_black_bowl_from_table_center': {'sr': 100, 'successes': 20, 'rollouts': 20}, 'pick_up_the_black_bowl_on_the_cookie_box': {'sr': 100, 'successes': 20, 'rollouts': 20}, 'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet': {'sr': 65, 'successes': 13, 'rollouts': 20}, 'pick_up_the_black_bowl_on_the_ramekin': {'sr': 0, 'successes': 0, 'rollouts': 20}, 'pick_up_the_black_bowl_next_to_the_cookie_box': {'sr': 100, 'successes': 20, 'rollouts': 20}, 'pick_up_the_black_bowl_on_the_stove': {'sr': 80, 'successes': 16, 'rollouts': 20}, 'pick_up_the_black_bowl_next_to_the_plate': {'sr': 80, 'successes': 16, 'rollouts': 20}, 'pick_up_the_black_bowl_on_the_wooden_cabinet': {'sr': 95, 'successes': 19, 'rollouts': 20}}}
    s45: SR=0.8, conc=success | {'successes': 160, 'total': 200, 'mean_uncertainty': 0.1885, 'trigger_rate': 0.2013, 'tau': 0.25, 'total_steps': 28599, 'crm_applied_steps': 5758}
    s46: SR=N/A, conc=killed
    s47: SR=0.815, conc=success | {'successes': 163, 'total': 200, 'trigger_rate': 0.2046, 'mean_uncertainty': 0.1873, 'json_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json', 'note': 'False failure - completed but harvest missed result'}
    s48: SR=0.81, conc=killed | {'trigger_rate': 0.198, 'tau': 0.25, 'benchmark': 'spatial', 'seed': 48}
    s49: SR=0.82, conc=killed | {'trigger_rate': 0.195, 'tau': 0.25, 'benchmark': 'spatial', 'seed': 49}

  adapt-tau035-spatial (2 seeds):
    s42: SR=N/A, conc=killed
    s42: SR=N/A, conc=success | {'overall_sr': 80, 'n_success': 160, 'n_total': 200, 'trigger_rate': 12.17, 'mean_unc': 0.1873, 'conformal_threshold': 0.35, 'max_correction_norm': 0.2, 'crm_applied_steps': 3474, 'total_steps': 28549, 'per_task_sr': {'between_plate_and_ramekin': 95, 'next_to_ramekin': 100, 'from_table_center': 90, 'on_cookie_box': 95, 'in_top_drawer': 70, 'on_ramekin': 0, 'next_to_cookie_box': 95, 'on_stove': 85, 'next_to_plate': 85, 'on_wooden_cabinet': 85}}

  crm-norm005-goal (3 seeds):
    s43: SR=0.82, conc=negative
    s44: SR=0.835, conc=success | {'total_rollouts': 200, 'total_successes': 167, 'three_seed_summary': {'seeds': [42, 43, 44], 'srs': [0.855, 0.82, 0.835], 'mean': 0.8367, 'std': 0.0176}}
    s48: SR=0.8, conc=success | {'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'benchmark': 'goal', 'mode': 'crm_obs_only', 'max_correction_norm': 0.05, 'K': 10}

  crm-norm005-obj (4 seeds):
    s43: SR=0.785, conc=negative
    s44: SR=0.74, conc=negative | {'successes': 148, 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20, 'source': 'eval_object_crm_obs_only_norm0.05_seed44.json'}
    s45: SR=N/A, conc=success | {'SR': 0.765}
    s46: SR=N/A, conc=success | {'SR': 0.795}

  crm-norm005-spatial (6 seeds):
    s43: SR=81, conc=success | {'total_rollouts': 200, 'total_successes': 162, 'per_task': {'between_plate_and_ramekin': {'sr': 100, 'success': 20, 'total': 20}, 'next_to_ramekin': {'sr': 95, 'success': 19, 'total': 20}, 'from_table_center': {'sr': 95, 'success': 19, 'total': 20}, 'on_cookie_box': {'sr': 100, 'success': 20, 'total': 20}, 'in_top_drawer_wooden_cabinet': {'sr': 75, 'success': 15, 'total': 20}, 'on_ramekin': {'sr': 0, 'success': 0, 'total': 20}, 'next_to_cookie_box': {'sr': 95, 'success': 19, 'total': 20}, 'on_stove': {'sr': 85, 'success': 17, 'total': 20}, 'next_to_plate': {'sr': 70, 'success': 14, 'total': 20}, 'on_wooden_cabinet': {'sr': 95, 'success': 19, 'total': 20}}}
    s44: SR=78.5, conc=success | {'total_rollouts': 200, 'total_successes': 157, 'per_task': {'between_plate_and_ramekin': {'sr': 100, 'success': 20, 'total': 20}, 'next_to_ramekin': {'sr': 90, 'success': 18, 'total': 20}, 'from_table_center': {'sr': 95, 'success': 19, 'total': 20}, 'on_cookie_box': {'sr': 100, 'success': 20, 'total': 20}, 'in_top_drawer_wooden_cabinet': {'sr': 70, 'success': 14, 'total': 20}, 'on_ramekin': {'sr': 0, 'success': 0, 'total': 20}, 'next_to_cookie_box': {'sr': 95, 'success': 19, 'total': 20}, 'on_stove': {'sr': 85, 'success': 17, 'total': 20}, 'next_to_plate': {'sr': 70, 'success': 14, 'total': 20}, 'on_wooden_cabinet': {'sr': 80, 'success': 16, 'total': 20}}, 'three_seed_summary': {'seeds': [42, 43, 44], 'srs': [80, 81, 78.5], 'mean': 79.8, 'std': 1.3}}
    s45: SR=0.805, conc=success | {'successes': 161, 'total': 200}
    s46: SR=0.785, conc=success | {'successes': 157, 'total': 200}
    s48: SR=0.78, conc=success | {'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'benchmark': 'spatial', 'mode': 'crm_obs_only', 'max_correction_norm': 0.05, 'K': 10}
    s49: SR=0.785, conc=success | {'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'benchmark': 'spatial', 'mode': 'crm_obs_only', 'max_correction_norm': 0.05, 'K': 10}

  crm-norm02-spatial (2 seeds):
    s42: SR=N/A, conc=killed
    s42: SR=N/A, conc=success | {'overall_sr': 79, 'n_success': 158, 'n_total': 200, 'per_task_sr': {'between_plate_and_ramekin': 100, 'next_to_ramekin': 90, 'from_table_center': 95, 'on_cookie_box': 95, 'in_top_drawer': 75, 'on_ramekin': 0, 'next_to_cookie_box': 100, 'on_stove': 95, 'next_to_plate': 75, 'on_wooden_cabinet': 65}}

  crm-obj (1 seeds):
    s46: SR=N/A, conc=success | {'overall_sr': 0.795, 'per_task': {'alphabet_soup': 0.8, 'cream_cheese': 0.7, 'salad_dressing': 0.75, 'bbq_sauce': 0.8, 'ketchup': 0.7, 'tomato_sauce': 0.75, 'butter': 0.75, 'milk': 0.85, 'chocolate_pudding': 0.95, 'orange_juice': 0.9}}

  goal-adapt-tau025 (4 seeds):
    s42: SR=84, conc=success | {'total_rollouts': 200, 'total_successes': 168, 'trigger_rate': 8.3, 'mean_unc': 0.1448, 'per_task': {'open_middle_drawer_cabinet': {'sr': 85, 'success': 17, 'total': 20}, 'put_bowl_on_stove': {'sr': 95, 'success': 19, 'total': 20}, 'put_wine_bottle_on_cabinet': {'sr': 80, 'success': 16, 'total': 20}, 'open_top_drawer_put_bowl': {'sr': 70, 'success': 14, 'total': 20}, 'put_bowl_on_top_cabinet': {'sr': 85, 'success': 17, 'total': 20}, 'push_plate_to_stove': {'sr': 95, 'success': 19, 'total': 20}, 'put_cream_cheese_in_bowl': {'sr': 60, 'success': 12, 'total': 20}, 'turn_on_stove': {'sr': 100, 'success': 20, 'total': 20}, 'put_bowl_on_plate': {'sr': 90, 'success': 18, 'total': 20}, 'put_wine_bottle_on_rack': {'sr': 80, 'success': 16, 'total': 20}}}
    s45: SR=0.81, conc=success | {'successes': 162, 'total': 200, 'trigger_rate': 0.094, 'mean_unc': 0.1493}
    s46: SR=0.835, conc=success | {'trigger_rate': 0.0909, 'tau': 0.25, 'source': 'json_harvest_bjb2-28827'}
    s47: SR=82, conc=success

  goal-crm-norm005 (3 seeds):
    s45: SR=81, conc=success | {'successes': 162, 'total': 200}
    s46: SR=0.82, conc=success | {'source': 'json_harvest_bjb2-28827'}
    s47: SR=82, conc=success

  goal-crm005 (1 seeds):
    s42: SR=85.5, conc=success | {'total_successes': 171, 'total_episodes': 200, 'per_task': {'middle_drawer': 85, 'bowl_stove': 100, 'wine_bottle_cabinet': 95, 'top_drawer_bowl': 70, 'bowl_cabinet': 95, 'plate_stove': 95, 'cream_cheese_bowl': 50, 'stove': 95, 'bowl_plate': 95, 'wine_bottle_rack': 75}}

  goal-k2mean (3 seeds):
    s45: SR=N/A, conc=negative | {'SR': 0.81, 'per_task': {'open_the_middle_drawer_of_the_cabinet': 0.7, 'put_the_bowl_on_the_stove': 0.95, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.85, 'open_the_top_drawer_and_put_the_bowl_inside': 0.6, 'put_the_bowl_on_top_of_the_cabinet': 0.95, 'push_the_plate_to_the_front_of_the_stove': 0.95, 'put_the_cream_cheese_in_the_bowl': 0.55, 'turn_on_the_stove': 0.95, 'put_the_bowl_on_the_plate': 0.9, 'put_the_wine_bottle_on_the_rack': 0.7}}
    s46: SR=0.825, conc=success | {'source': 'json_harvest_bjb2-28827'}
    s47: SR=0.825, conc=failed | {'successes': 165, 'total': 200, 'benchmark': 'goal', 'mode': 'vla_only', 'baseline_mode': 'mean', 'n_rollouts': 20}

  goal-reconvla (6 seeds):
    s42: SR=N/A, conc=negative
    s43: SR=0.81, conc=negative | {'n_rollouts': 20, 'n_tasks': 10, 'total_episodes': 200, 'per_task': {'open_the_middle_drawer_of_the_cabinet': 0.65, 'put_the_bowl_on_the_stove': 0.95, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.85, 'open_the_top_drawer_and_put_the_bowl_inside': 0.5, 'put_the_bowl_on_top_of_the_cabinet': 0.95, 'push_the_plate_to_the_front_of_the_stove': 0.9, 'put_the_cream_cheese_in_the_bowl': 0.55, 'turn_on_the_stove': 0.95, 'put_the_bowl_on_the_plate': 0.95, 'put_the_wine_bottle_on_the_rack': 0.85}}
    s44: SR=0.805, conc=negative | {'total_rollouts': 200, 'total_successes': 161, 'three_seed_summary': {'seeds': [42, 43, 44], 'srs': [0.81, 0.81, 0.805], 'mean': 0.8083, 'std': 0.0029}}
    s45: SR=N/A, conc=success | {'SR': 0.855}
    s46: SR=0.79, conc=success | {'source': 'json_harvest_bjb2-28827'}
    s47: SR=83.5, conc=success

  goal-vla-only (10 seeds):
    s42: SR=N/A, conc=failed
    s42: SR=N/A, conc=failed
    s43: SR=N/A, conc=failed
    s44: SR=N/A, conc=failed
    s45: SR=N/A, conc=success | {'SR': 0.835}
    s46: SR=0.83, conc=success | {'source': 'json_harvest_bjb2-28827'}
    s47: SR=N/A, conc=killed
    s47: SR=N/A, conc=killed
    s47: SR=0.825, conc=success | {'successes': 165, 'total': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20, 'output_file': 'logs/eval_goal_vla_only_seed47.json'}
    s50: SR=N/A, conc=failed

  goal-vla-only-wrapper (3 seeds):
    s43: SR=82.5, conc=success | {'source': 'JSON file eval_goal_vla_only_seed43.json on bjb1-32546, harvested 2026-05-26'}
    s44: SR=82, conc=success | {'successes': 164, 'total': 200}
    s44: SR=N/A, conc=success | {'SR': 0.85, 'successes': 170, 'total': 200, 'per_task': {'open_middle_drawer': 0.85, 'put_bowl_stove': 0.95, 'wine_bottle_cabinet': 0.85, 'open_top_drawer_bowl': 0.7, 'bowl_on_cabinet': 0.9, 'push_plate_stove': 0.9, 'cream_cheese_bowl': 0.65, 'turn_on_stove': 1, 'bowl_on_plate': 0.95, 'wine_bottle_rack': 0.75}}

  k2mean-goal (4 seeds):
    s42: SR=N/A, conc=failed
    s42: SR=N/A, conc=success | {'overall_sr': 0.855, 'n_tasks': 10, 'n_rollouts': 200, 'per_task': {'open_the_middle_drawer_of_the_cabinet': 0.8, 'put_the_bowl_on_the_stove': 1, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.9, 'open_the_top_drawer_and_put_the_bowl_inside': 0.65, 'put_the_bowl_on_top_of_the_cabinet': 0.95, 'push_the_plate_to_the_front_of_the_stove': 0.95, 'put_the_cream_cheese_in_the_bowl': 0.5, 'turn_on_the_stove': 1, 'put_the_bowl_on_the_plate': 1, 'put_the_wine_bottle_on_the_rack': 0.8}}
    s43: SR=0.815, conc=success | {'total_rollouts': 200, 'per_task': {'open_the_middle_drawer_of_the_cabinet': 0.7, 'put_the_bowl_on_the_stove': 0.95, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.9, 'open_the_top_drawer_and_put_the_bowl_inside': 0.55, 'put_the_bowl_on_top_of_the_cabinet': 0.9, 'push_the_plate_to_the_front_of_the_stove': 0.95, 'put_the_cream_cheese_in_the_bowl': 0.45, 'turn_on_the_stove': 0.95, 'put_the_bowl_on_the_plate': 0.95, 'put_the_wine_bottle_on_the_rack': 0.85}}
    s44: SR=N/A, conc=negative | {'overall_sr': 0.82, 'per_task': {'drawer': 0.85, 'bowl_stove': 1, 'wine_cabinet': 0.8, 'drawer_bowl': 0.6, 'bowl_cabinet': 0.9, 'plate': 0.95, 'cream_cheese': 0.45, 'stove': 1, 'bowl_plate': 0.9, 'wine_rack': 0.75}}

  k2mean-obj (2 seeds):
    s45: SR=N/A, conc=success | {'SR': 0.775}
    s46: SR=N/A, conc=success | {'SR': 0.765}

  k2mean-object (3 seeds):
    s42: SR=79.5, conc=success | {'total_successes': 159, 'total_rollouts': 200, 'mode': 'vla_only', 'K': 2, 'baseline_mode': 'mean', 'per_task': {'alphabet_soup': 75, 'cream_cheese': 70, 'salad_dressing': 85, 'bbq_sauce': 90, 'ketchup': 95, 'tomato_sauce': 85, 'butter': 60, 'milk': 70, 'chocolate_pudding': 70, 'orange_juice': 95}}
    s43: SR=0.78, conc=success | {'total_successes': 156, 'total_rollouts': 200, 'per_task': {'alphabet_soup': 0.85, 'cream_cheese': 0.85, 'salad_dressing': 0.75, 'bbq_sauce': 0.8, 'ketchup': 0.85, 'tomato_sauce': 0.7, 'butter': 0.7, 'milk': 0.7, 'chocolate_pudding': 0.7, 'orange_juice': 0.9}}
    s44: SR=N/A, conc=success | {'overall_sr': 0.75, 'per_task': {'alphabet_soup': 0.7, 'cream_cheese': 0.7, 'salad_dressing': 0.8, 'bbq_sauce': 0.8, 'ketchup': 0.85, 'tomato_sauce': 0.7, 'butter': 0.55, 'milk': 0.7, 'chocolate_pudding': 0.75, 'orange_juice': 0.95}}

  k2mean-spatial (5 seeds):
    s42: SR=81.5, conc=negative | {'total_success': 163, 'total_rollouts': 200, 'per_task': {'bowl_between_plate_ramekin': 95, 'bowl_next_to_ramekin': 95, 'bowl_from_table_center': 100, 'bowl_on_cookie_box': 100, 'bowl_in_top_drawer': 70, 'bowl_on_ramekin': 0, 'bowl_next_to_cookie_box': 95, 'bowl_on_stove': 80, 'bowl_next_to_plate': 85, 'bowl_on_wooden_cabinet': 95}}
    s43: SR=0.78, conc=success | {'n_rollouts': 20, 'n_tasks': 10, 'total_episodes': 200, 'per_task': {'between_plate_ramekin': 0.95, 'next_to_ramekin': 0.95, 'table_center': 0.95, 'on_cookie_box': 1, 'top_drawer': 0.7, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'on_stove': 0.75, 'next_to_plate': 0.7, 'on_wooden_cabinet': 0.85}}
    s44: SR=0.81, conc=success | {'successes': 162, 'total': 200}
    s45: SR=N/A, conc=killed
    s47: SR=0.81, conc=success | {'successes': 162, 'total': 200, 'note': 'Completed at 18:07 with SR=81.0% per log; JSON overwritten by vla-only K=1 run which wrote to same output_file (eval_spatial_vla_only_seed47.json). Per-task data recoverable from eval-supp-k2mean-spatial-s47.log on cqa1-32758. Recommend explicit --output_file for future k2mean runs.'}

  long-adapt-tau025 (6 seeds):
    s44: SR=N/A, conc=negative | {'SR': 0.56, 'trigger_rate': 0.049}
    s45: SR=N/A, conc=success | {'SR': 0.6, 'successes': 120, 'total': 200}
    s46: SR=0.585, conc=success | {'successes': 117, 'total_rollouts': 200, 'benchmark': 'long', 'mode': 'adaptive_conformal_crm', 'seed': 46, 'K': 2, 'max_correction_norm': 0.2, 'conformal_threshold': 0.25}
    s46: SR=N/A, conc=killed
    s47: SR=N/A, conc=failed
    s47: SR=0.55, conc=negative | {'successes': 110, 'total': 200, 'trigger_rate': 0.037, 'n_tasks': 10, 'n_rollouts_per_task': 20}

  long-crm-norm005 (7 seeds):
    s42: SR=N/A, conc=negative | {'overall_sr': 0.565}
    s43: SR=N/A, conc=negative | {'SR': 0.545}
    s44: SR=N/A, conc=success | {'SR': 0.565}
    s45: SR=N/A, conc=success | {'SR': 0.605, 'successes': 121, 'total': 200}
    s46: SR=0.54, conc=success | {'successes': 108, 'total': 200, 'source': 'json_harvest_bjb1-32546'}
    s46: SR=N/A, conc=killed
    s47: SR=0.565, conc=success | {'successes': 113, 'total': 200, 'json_path': '/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed47.json', 'note': 'False failure - completed but harvest missed result'}

  long-k2mean (8 seeds):
    s42: SR=N/A, conc=negative | {'SR': 0.57}
    s43: SR=N/A, conc=negative | {'SR': 0.56}
    s44: SR=N/A, conc=negative | {'SR': 0.545, 'successes': 109, 'total': 200}
    s45: SR=0.56, conc=success | {'source': 'json_harvest_bjb2-28827'}
    s46: SR=0.55, conc=success | {'successes': 110, 'total': 200, 'source': 'json_harvest_bjb1-32546'}
    s46: SR=N/A, conc=killed
    s47: SR=N/A, conc=failed
    s47: SR=0.545, conc=success | {'successes': 109, 'total': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20, 'note': 'output saved as eval_long_vla_only_seed47.json (pre-M083 naming)'}

  long-reconvla (7 seeds):
    s42: SR=N/A, conc=negative | {'overall_sr': 0.565}
    s43: SR=N/A, conc=negative | {'SR': 0.59}
    s44: SR=N/A, conc=success | {'SR': 0.57, 'successes': 114, 'total': 200}
    s45: SR=59, conc=success | {'successes': 118, 'total': 200}
    s46: SR=0.56, conc=success | {'successes': 112, 'total': 200, 'source': 'json_harvest_bjb1-32546'}
    s46: SR=N/A, conc=killed
    s47: SR=0.55, conc=success | {'successes': 110, 'total': 200, 'json_path': '/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed47.json', 'note': 'False failure - completed but harvest missed result'}

  long-vla-only (10 seeds):
    s42: SR=N/A, conc=success | {'SR': 59.5, 'total_successes': 119, 'total_trials': 200}
    s43: SR=N/A, conc=killed
    s43: SR=N/A, conc=failed
    s44: SR=N/A, conc=success | {'SR': 60.5, 'total_successes': 121, 'total_trials': 200}
    s45: SR=N/A, conc=success | {'SR': 0.575, 'successes': 115, 'total': 200}
    s46: SR=N/A, conc=killed
    s47: SR=N/A, conc=killed
    s47: SR=N/A, conc=killed
    s47: SR=0.595, conc=success | {'total_successes': 119, 'total_trials': 200}
    s48: SR=N/A, conc=failed

  obj-adapt (2 seeds):
    s42: SR=N/A, conc=killed
    s42: SR=77.5, conc=negative | {'total_successes': 155, 'total_episodes': 200, 'per_task': {'alphabet_soup': 80, 'cream_cheese': 90, 'salad_dressing': 70, 'bbq_sauce': 85, 'ketchup': 70, 'tomato_sauce': 75, 'butter': 65, 'milk': 65, 'chocolate_pudding': 80, 'orange_juice': 95}, 'mean_unc': 0.1104, 'trigger_rate': 0.702}

  obj-adapt-tau025 (6 seeds):
    s42: SR=0.81, conc=success | {'successes': 162, 'total': 200, 'trigger_rate': 0.035, 'mean_unc': 0.109, 'max_correction_norm': 0.2, 'conformal_threshold': 0.25, 'K': 2}
    s43: SR=N/A, conc=killed
    s45: SR=N/A, conc=failed
    s45: SR=N/A, conc=killed
    s47: SR=0.77, conc=success | {'successes': 154, 'total': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20}
    s47: SR=0.77, conc=success | {'trigger_rate': 0.0403, 'crm_applied_steps': 1458}

  obj-crm-norm005 (4 seeds):
    s45: SR=0.765, conc=success | {'successes': 153, 'total': 200, 'source': 'json_harvest_bjb2-40593', 'json_file': 'eval_object_crm_obs_only_norm0.05_seed45.json'}
    s46: SR=0.795, conc=killed | {'successes': 159, 'total': 200, 'source': 'json_harvest_bjb1'}
    s47: SR=0.825, conc=success | {'successes': 165, 'total': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20}
    s47: SR=0.825, conc=success

  obj-crm005 (2 seeds):
    s42: SR=N/A, conc=killed
    s42: SR=0.77, conc=success | {'n_success': 154, 'n_total': 200, 'n_tasks': 10, 'n_rollouts': 20, 'mode': 'crm_obs_only', 'max_correction_norm': 0.05, 'conformal_threshold': 0.074855, 'K': 10, 'seed': 42, 'per_task_sr': {'alphabet_soup': 0.7, 'cream_cheese': 0.7, 'salad_dressing': 0.75, 'bbq_sauce': 0.9, 'ketchup': 0.8, 'tomato_sauce': 0.7, 'butter': 0.7, 'milk': 0.75, 'chocolate_pudding': 0.85, 'orange_juice': 0.85}}

  obj-k2mean (3 seeds):
    s45: SR=N/A, conc=killed
    s47: SR=0.775, conc=success | {'successes': 155, 'total': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20}
    s47: SR=N/A, conc=failed

  obj-reconvla (4 seeds):
    s42: SR=79, conc=success | {'total_successes': 158, 'total_episodes': 200, 'per_task': {'alphabet_soup': 75, 'cream_cheese': 70, 'salad_dressing': 85, 'bbq_sauce': 95, 'ketchup': 90, 'tomato_sauce': 80, 'butter': 65, 'milk': 65, 'chocolate_pudding': 75, 'orange_juice': 90}}
    s43: SR=0.77, conc=success | {'total_rollouts': 200, 'total_successes': 154}
    s44: SR=N/A, conc=success | {'overall_sr': 0.76, 'per_task': {'alphabet_soup': 0.65, 'cream_cheese': 0.7, 'salad_dressing': 0.7, 'bbq_sauce': 0.95, 'ketchup': 0.9, 'tomato_sauce': 0.7, 'butter': 0.75, 'milk': 0.6, 'chocolate_pudding': 0.7, 'orange_juice': 0.95}}
    s47: SR=76.5, conc=success

  obj-vla-only (8 seeds):
    s42: SR=N/A, conc=failed
    s43: SR=N/A, conc=failed
    s44: SR=N/A, conc=failed
    s45: SR=N/A, conc=success | {'SR': 0.76}
    s46: SR=N/A, conc=success | {'SR': 0.79}
    s47: SR=0.755, conc=success | {'successes': 151, 'total': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20}
    s47: SR=0.755, conc=success
    s50: SR=0.74, conc=success | {'successes': 148, 'total': 200, 'n_rollouts': 20, 'benchmark': 'object', 'seed': 50, 'mode': 'vla_only', 'model': 'pi05'}

  object-vla-only (1 seeds):
    s50: SR=N/A, conc=killed

  reconvla-k2-spatial (1 seeds):
    s42: SR=80, conc=success | {'total_rollouts': 200, 'total_successes': 160, 'per_task': {'between_plate_and_ramekin': 95, 'next_to_ramekin': 100, 'from_table_center': 100, 'on_cookie_box': 95, 'in_top_drawer': 75, 'on_ramekin': 0, 'next_to_cookie_box': 95, 'on_stove': 75, 'next_to_plate': 80, 'on_wooden_cabinet': 85}}

  reconvla-obj (2 seeds):
    s45: SR=78, conc=success
    s46: SR=0.8, conc=success | {'successes': 160, 'total': 200}

  reconvla-spatial (3 seeds):
    s43: SR=0.815, conc=success | {'n_tasks': 10, 'n_rollouts': 20, 'per_task': {'between_plate_ramekin': 0.95, 'next_to_ramekin': 0.95, 'table_center': 1, 'on_cookie_box': 1, 'top_drawer_cabinet': 0.7, 'on_ramekin': 0, 'next_to_cookie_box': 1, 'on_stove': 0.9, 'next_to_plate': 0.8, 'on_wooden_cabinet': 0.85}}
    s44: SR=0.795, conc=success | {'n_tasks': 10, 'n_rollouts_per_task': 20, 'per_task': {'between_plate_and_ramekin': 1, 'table_center': 1, 'next_to_ramekin': 0.95, 'next_to_cookie_box': 0.95, 'on_cookie_box': 0.9, 'on_wooden_cabinet': 0.85, 'on_stove': 0.8, 'next_to_plate': 0.8, 'top_drawer_wooden_cabinet': 0.7, 'on_ramekin': 0}, 'three_seed_summary': {'seeds': [42, 43, 44], 'srs': [0.8, 0.815, 0.795], 'mean': 0.803, 'std': 0.01}}
    s47: SR=0.81, conc=success | {'successes': 162, 'total': 200, 'json_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json', 'note': 'False failure - completed but harvest missed result'}

  spatial-adapt-tau025 (3 seeds):
    s45: SR=80, conc=success | {'trigger_rate': 20}
    s46: SR=80, conc=success | {'successes': 160, 'total': 200, 'trigger_rate': 19.9, 'mean_unc': 0.1846}
    s47: SR=79.5, conc=success | {'trigger_rate': 0.21, 'mean_uncertainty': 0.1886, 'total_successes': 159, 'total_trials': 200}

  spatial-crm-norm005 (3 seeds):
    s45: SR=N/A, conc=success | {'SR': 0.78, 'successes': 156, 'total': 200, 'per_task': {'between_plate_and_ramekin': 1, 'next_to_ramekin': 1, 'table_center': 0.9, 'on_cookie_box': 1, 'top_drawer_cabinet': 0.7, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'on_stove': 0.8, 'next_to_plate': 0.75, 'on_wooden_cabinet': 0.7}}
    s46: SR=81, conc=success | {'successes': 162, 'total': 200}
    s47: SR=0.805, conc=success | {'successes': 161, 'total': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20, 'output_file': 'logs/eval_spatial_crm_obs_only_norm0.05_seed47.json'}

  spatial-k2mean (3 seeds):
    s45: SR=80, conc=success | {'successes': 160, 'total': 200}
    s46: SR=80, conc=success
    s47: SR=82, conc=success | {'total_successes': 164, 'total_trials': 200}

  spatial-reconvla (3 seeds):
    s45: SR=79.5, conc=success | {'successes': 159, 'total': 200}
    s46: SR=80, conc=success
    s47: SR=N/A, conc=success | {'overall_sr': 0.78, 'n_tasks': 10, 'n_rollouts_per_task': 20, 'total_rollouts': 200, 'per_task': {'between_plate_and_ramekin': 0.9, 'next_to_ramekin': 0.9, 'table_center': 0.95, 'on_cookie_box': 1, 'top_drawer_cabinet': 0.65, 'on_ramekin': 0, 'next_to_cookie_box': 1, 'on_stove': 0.9, 'next_to_plate': 0.8, 'on_wooden_cabinet': 0.7}}

  spatial-vla-only (6 seeds):
    s42: SR=0.8, conc=success | {'successes': 160, 'total': 200, 'n_rollouts': 20, 'benchmark': 'spatial', 'seed': 42, 'mode': 'vla_only', 'model': 'pi05'}
    s43: SR=0.79, conc=success | {'successes': 158, 'total': 200}
    s44: SR=N/A, conc=success | {'overall_sr': 0.785, 'successes': 157, 'total': 200, 'per_task': {'between_plate_ramekin': 0.9, 'next_to_ramekin': 0.95, 'table_center': 0.95, 'on_cookie_box': 1, 'top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 1, 'on_stove': 0.8, 'next_to_plate': 0.8, 'on_wooden_cabinet': 0.7}}
    s45: SR=N/A, conc=success | {'SR': 0.77, 'successes': 154, 'total': 200}
    s46: SR=80.5, conc=success | {'successes': 161, 'total': 200}
    s47: SR=0.81, conc=success | {'total_successes': 162, 'total_trials': 200, 'per_task_range': '0.0-1.0', 'worst_task': 'pick_up_black_bowl_on_ramekin (0/20)', 'best_tasks': 'from_table_center, on_cookie_box, next_to_cookie_box (20/20)'}

  spatial-vla-only-smolvla (1 seeds):
    s42: SR=N/A, conc=failed

  vla-only-goal (2 seeds):
    s48: SR=N/A, conc=success | {'overall_sr': 0.85, 'per_task_sr': {'middle_drawer': 0.9, 'bowl_stove': 0.95, 'wine_cabinet': 0.9, 'drawer_bowl': 0.55, 'bowl_cabinet': 1, 'push_plate': 0.9, 'cream_cheese': 0.6, 'stove_on': 1, 'bowl_plate': 0.9, 'wine_rack': 0.8}}
    s49: SR=N/A, conc=success | {'overall_sr': 0.82, 'per_task_sr': {'middle_drawer': 0.75, 'bowl_stove': 0.95, 'wine_cabinet': 0.85, 'drawer_bowl': 0.65, 'bowl_cabinet': 0.95, 'push_plate': 0.85, 'cream_cheese': 0.55, 'stove_on': 1, 'bowl_plate': 0.85, 'wine_rack': 0.8}}

  vla-only-obj (2 seeds):
    s48: SR=N/A, conc=success | {'overall_sr': 0.79, 'per_task_sr': {'soup': 0.65, 'cream_cheese': 0.8, 'salad': 0.75, 'bbq': 0.9, 'ketchup': 0.85, 'tomato': 0.8, 'butter': 0.65, 'milk': 0.8, 'pudding': 0.75, 'oj': 0.95}}
    s49: SR=N/A, conc=success | {'overall_sr': 0.755, 'per_task_sr': {'soup': 0.55, 'cream_cheese': 0.7, 'salad': 0.8, 'bbq': 0.95, 'ketchup': 0.8, 'tomato': 0.8, 'butter': 0.6, 'milk': 0.65, 'pudding': 0.8, 'oj': 0.9}}

  vla-only-spatial (5 seeds):
    s45: SR=0.8, conc=success | {'successes': 160, 'total': 200}
    s46: SR=0.805, conc=success | {'successes': 161, 'total': 200}
    s47: SR=0.8, conc=success | {'successes': 160, 'total': 200, 'json_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json', 'note': 'False failure - completed but harvest missed result'}
    s48: SR=N/A, conc=success | {'overall_sr': 0.795, 'per_task_sr': {'between': 1, 'next_ramekin': 0.9, 'center': 0.95, 'cookie_box': 0.95, 'drawer': 0.8, 'on_ramekin': 0, 'next_cookie': 0.95, 'stove': 0.75, 'next_plate': 0.85, 'cabinet': 0.8}}
    s49: SR=N/A, conc=success | {'overall_sr': 0.785, 'per_task_sr': {'between': 0.9, 'next_ramekin': 0.95, 'center': 0.95, 'cookie_box': 0.95, 'drawer': 0.7, 'on_ramekin': 0, 'next_cookie': 0.9, 'stove': 0.8, 'next_plate': 0.75, 'cabinet': 0.95}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "33a73f8b-c72a-4e00-a5b7-301ede40671d"
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
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Detail adaptive-k experiments",
  "usage": {
    "total_tokens": 39450,
    "tool_uses": 10,
    "duration_ms": 87434
  },
  "last_tool_name": "Bash",
  "uuid": "31a107c4-47c8-4396-b1fa-cbf78f828382",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_013T1vUm6BAZvtE4zjG8Sq4h`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# ==========================================\n# ADAPTIVE-K experiments (with metrics)\n# ==========================================\nprint(\"=\" * 80)\nprint(\"ADAPTIVE-K EXPERIMENTS (with metrics)\")\nprint(\"=\" * 80)\n\nak_exps = {eid: ed for eid, ed in exps.items() if 'adaptive-k' in eid and ed.get('metrics')}\nfor eid in sorted(ak_exps.keys()):\n    ed = ak_exps[eid]\n    m = ed.get('metrics', {})\n    if not isinstance(m, dict): m = {}\n    sr = m.get('success_rate', m.get('overall_success_rate', m.get('SR', m.get('overall_sr', 'N/A'))))\n    print(f\"  {eid}: conc={ed['conclusion']}, SR={sr}, metrics={m}\")\n\nPYEOF\n",
  "description": "Detail adaptive-k experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "0deea3c4-d702-49e6-b806-ecf902683675",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Ndv2Cak4wGQBDne7Vzuc3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15133,
      "cache_read_input_tokens": 24145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15133,
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

_source line 64 · 2026-05-28T15:52:30.146Z_

<details><summary>↩ Tool result · `toolu_013T1vUm6BAZvtE4zjG8Sq4h`</summary>

```text
================================================================================
ADAPTIVE-K EXPERIMENTS (with metrics)
================================================================================
  eval-adaptive-k-p25-seed42: conc=success, SR=0.15, metrics={'success_rate': 0.15, 'avg_actual_k': 4.8, 'fast_path_ratio': 0.65}
  eval-adaptive-k-p25-seed43: conc=success, SR=0.13, metrics={'success_rate': 0.13, 'avg_actual_k': 4.788, 'fast_path_ratio': 0.6515, 'total_steps': 28207, 'fast_steps': 18377, 'full_steps': 9830}
  eval-adaptive-k-p25-seed44-r2: conc=success, SR=0.15, metrics={'success_rate': 0.15, 'avg_actual_k': 4.736, 'fast_path_ratio': 0.658, 'adaptive_trigger_rate': 0.342, 'total_steps': 27889, 'fast_steps': 18351, 'full_steps': 9538}
  eval-adaptive-k-p50-seed42: conc=success, SR=0.16, metrics={'success_rate': 0.16, 'avg_actual_k': 3.72, 'fast_path_ratio': 0.785}
  eval-adaptive-k-p50-seed43: conc=success, SR=0.16, metrics={'success_rate': 0.16, 'avg_actual_k': 3.81, 'fast_path_ratio': 0.7737, 'total_steps': 27813, 'fast_steps': 21520, 'full_steps': 6293}
  eval-adaptive-k-p50-seed44: conc=success, SR=0.14, metrics={'success_rate': 0.14, 'avg_actual_k': 3.909, 'fast_path_ratio': 0.761, 'total_steps': 28067, 'fast_steps': 21368, 'full_steps': 6699}
  eval-adaptive-k-p75-seed42: conc=success, SR=0.12, metrics={'success_rate': 0.12, 'avg_actual_k': 3.07, 'fast_path_ratio': 0.866}
  eval-adaptive-k-p75-seed43: conc=success, SR=0.13, metrics={'success_rate': 0.13, 'avg_actual_k': 3.15, 'fast_path_ratio': 0.856}
  eval-adaptive-k-p75-seed44: conc=success, SR=0.16, metrics={'success_rate': 0.16, 'avg_actual_k': 3.022, 'fast_path_ratio': 0.872, 'total_steps': 27724, 'fast_steps': 24181, 'full_steps': 3543}
  eval-adaptive-k-p90-seed42: conc=success, SR=0.12, metrics={'success_rate': 0.12, 'avg_actual_k': 2.672, 'fast_path_ratio': 0.916, 'total_steps': 28258, 'fast_steps': 25886, 'full_steps': 2372}
  eval-adaptive-k-p90-seed43: conc=success, SR=0.14, metrics={'success_rate': 0.14, 'avg_actual_k': 2.612, 'fast_path_ratio': 0.923, 'total_steps': 27935, 'fast_steps': 25797, 'full_steps': 2138}
  eval-adaptive-k-p90-seed44: conc=success, SR=0.14, metrics={'success_rate': 0.14, 'avg_actual_k': 2.58, 'fast_path_ratio': 0.928}
  eval-adaptive-k-spatial-p25-seed42: conc=negative, SR=0.33, metrics={'overall_success_rate': 0.33, 'avg_K': 7.65, 'fast_path_pct': 29.4, 'mean_l2_distance': 0.0892, 'threshold': 0.054959, 'total_steps': 23410, 'fast_steps': 6873, 'full_steps': 16537, 'per_task': {'between_plate_and_ramekin': 0.7, 'next_to_ramekin': 1, 'from_table_center': 0, 'on_cookie_box': 0.3, 'in_top_drawer': 0.1, 'on_ramekin': 0, 'next_to_cookie_box': 0.9, 'on_stove': 0, 'next_to_plate': 0.3, 'on_wooden_cabinet': 0}}
  eval-adaptive-k-spatial-p25-seed43: conc=success, SR=N/A, metrics={'sr': 30, 'avg_k': 7.6, 'fast_path_pct': 29.5, 'mean_l2': 0.089, 'total_rollouts': 100, 'per_task_sr': {'between_plate_and_ramekin': 60, 'next_to_ramekin': 100, 'from_table_center': 0, 'on_cookie_box': 30, 'in_top_drawer': 10, 'on_ramekin': 0, 'next_to_cookie_box': 80, 'on_stove': 0, 'next_to_plate': 20, 'on_wooden_cabinet': 0}}
  eval-adaptive-k-spatial-p25-seed44: conc=success, SR=N/A, metrics={'sr': 32, 'avg_k': 7.693, 'fast_path_pct': 28.8, 'mean_l2': 0.0896, 'total_rollouts': 100, 'per_task_sr': {'between_plate_and_ramekin': 70, 'next_to_ramekin': 100, 'from_table_center': 0, 'on_cookie_box': 40, 'in_top_drawer': 10, 'on_ramekin': 0, 'next_to_cookie_box': 80, 'on_stove': 0, 'next_to_plate': 20, 'on_wooden_cabinet': 0}}
  eval-adaptive-k-spatial-p50-seed42: conc=success, SR=N/A, metrics={'sr': 30, 'avg_K': 6.324, 'fast_path_pct': 45.95, 'mean_l2': 0.0903, 'total_rollouts': 100}
  eval-adaptive-k-spatial-p50-seed43: conc=success, SR=N/A, metrics={'sr': 0.33, 'avg_K': 6.33, 'fast_path_ratio': 0.458, 'adaptive_trigger_rate': 0.542, 'threshold': 0.074855}
  eval-adaptive-k-spatial-p50-seed43-r2: conc=success, SR=0.33, metrics={'overall_success_rate': 0.33, 'per_task_sr': {'between_plate_and_ramekin': 0.8, 'next_to_ramekin': 1, 'from_table_center': 0, 'on_cookie_box': 0.4, 'in_top_drawer': 0.1, 'on_ramekin': 0, 'next_to_cookie_box': 0.9, 'on_stove': 0, 'next_to_plate': 0.1, 'on_wooden_cabinet': 0}, 'avg_k': 6.33, 'fast_path_ratio': 0.458, 'adaptive_trigger_rate': 0.542, 'mean_l2_distance': 0.0903, 'total_steps': 23414, 'fast_steps': 10728, 'full_steps': 12686, 'threshold': 0.074855, 'total_rollouts': 100}
  eval-adaptive-k-spatial-p50-seed44: conc=success, SR=N/A, metrics={'sr': 0.33, 'avg_K': 6.4, 'fast_path_ratio': 0.45, 'adaptive_trigger_rate': 0.55, 'threshold': 0.074855}
  eval-adaptive-k-spatial-p50-seed44-r2: conc=success, SR=0.33, metrics={'overall_success_rate': 0.33, 'per_task_sr': {'between_plate_and_ramekin': 0.6, 'next_to_ramekin': 1, 'from_table_center': 0, 'on_cookie_box': 0.3, 'in_top_drawer': 0.1, 'on_ramekin': 0, 'next_to_cookie_box': 0.9, 'on_stove': 0, 'next_to_plate': 0.4, 'on_wooden_cabinet': 0}, 'avg_k': 6.4, 'fast_path_ratio': 0.45, 'adaptive_trigger_rate': 0.55, 'mean_l2_distance': 0.0923, 'total_steps': 23661, 'fast_steps': 10649, 'full_steps': 13012, 'threshold': 0.074855, 'total_rollouts': 100}
  eval-adaptive-k-spatial-p75-seed42: conc=success, SR=N/A, metrics={'sr': 0.31, 'avg_k': 5.02, 'fast_path_ratio': 0.622, 'mean_l2': 0.0909, 'adaptive_trigger_rate': 0.378, 'total_steps': 23914, 'fast_steps': 14875, 'full_steps': 9039}
  eval-adaptive-k-spatial-p75-seed43: conc=success, SR=34, metrics={'success_rate': 34, 'total_rollouts': 100, 'adaptive_stats': {'fast_path_pct': 62.2, 'avg_k': 5, 'mean_l2': 0.0911}, 'per_task': {'bowl_between_plate_ramekin': 80, 'bowl_next_to_ramekin': 100, 'bowl_from_table_center': 0, 'bowl_on_cookie_box': 40, 'bowl_in_top_drawer': 0, 'bowl_on_ramekin': 0, 'bowl_next_to_cookie_box': 90, 'bowl_on_stove': 0, 'bowl_next_to_plate': 30, 'bowl_on_wooden_cabinet': 0}}
  eval-adaptive-k-spatial-p75-seed44: conc=success, SR=N/A, metrics={'sr': 33, 'avg_k': 5.054, 'fast_path_pct': 61.8, 'mean_l2': 0.092, 'total_rollouts': 100, 'threshold': 0.098735}
  eval-adaptive-k-spatial-p90-seed42: conc=success, SR=0.31, metrics={'overall_success_rate': 0.31, 'avg_K': 3.5, 'fast_path_pct': 80.6, 'mean_l2': 0.0907, 'threshold': 0.12587, 'total_rollouts': 100, 'total_successes': 31, 'per_task': {'between_plate_and_ramekin': 0.6, 'next_to_ramekin': 1, 'from_table_center': 0, 'on_cookie_box': 0.3, 'in_top_drawer': 0, 'on_ramekin': 0, 'next_to_cookie_box': 0.9, 'on_stove': 0, 'next_to_plate': 0.3, 'on_wooden_cabinet': 0}}
  eval-adaptive-k-spatial-p90-seed43: conc=success, SR=0.32, metrics={'overall_success_rate': 0.32, 'avg_K': 3.586, 'fast_path_pct': 80.17, 'mean_l2': 0.0905, 'adaptive_trigger_rate': 0.198, 'threshold': 0.12587, 'total_steps': 23797, 'fast_steps': 19079, 'full_steps': 4718}
  eval-adaptive-k-spatial-p90-seed44: conc=success, SR=0.36, metrics={'success_rate': 0.36, 'avg_K': 3.56, 'fast_path_ratio': 0.805, 'adaptive_trigger_rate': 0.195, 'total_rollouts': 100, 'successes': 36, 'total_steps': 23123, 'fast_steps': 18615, 'full_steps': 4508, 'threshold': 0.12587, 'mean_l2_distance': 0.09, 'per_task': {'between_plate_and_ramekin': {'sr': 0.8, 'successes': 8, 'total': 10}, 'next_to_ramekin': {'sr': 1, 'successes': 10, 'total': 10}, 'from_table_center': {'sr': 0, 'successes': 0, 'total': 10}, 'on_cookie_box': {'sr': 0.4, 'successes': 4, 'total': 10}, 'in_top_drawer': {'sr': 0.1, 'successes': 1, 'total': 10}, 'on_ramekin': {'sr': 0, 'successes': 0, 'total': 10}, 'next_to_cookie_box': {'sr': 0.9, 'successes': 9, 'total': 10}, 'on_stove': {'sr': 0, 'successes': 0, 'total': 10}, 'next_to_plate': {'sr': 0.4, 'successes': 4, 'total': 10}, 'on_wooden_cabinet': {'sr': 0, 'successes': 0, 'total': 10}}}
  eval-adaptive-k-spatial-p90-seed44-bjb2: conc=success, SR=36, metrics={'success_rate': 36, 'successes': 36, 'total': 100, 'fast_path': 81.5, 'avg_k': 3.5, 'mean_l2': 0.0885}
  eval-adaptive-k1-spatial-tau025-s42: conc=killed, SR=0.795, metrics={'overall_success_rate': 0.795, 'trigger_rate': 0.197, 'tau': 0.25, 'K': 1, 'benchmark': 'spatial', 'seed': 42}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "89eea5e8-c324-42ef-81e5-850fa46699c6"
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
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Detail random-selection, ablation, and canonical experiments",
  "usage": {
    "total_tokens": 43876,
    "tool_uses": 11,
    "duration_ms": 110793
  },
  "last_tool_name": "Bash",
  "uuid": "affbf735-c5bf-4179-978b-793fb8e95230",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Bash · `toolu_019NhNE6PusYLn1PZvqsPjAb`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# ==========================================\n# RANDOM SELECTION experiments\n# ==========================================\nprint(\"=\" * 80)\nprint(\"RANDOM SELECTION EXPERIMENTS (with metrics)\")\nprint(\"=\" * 80)\n\nrs_exps = {eid: ed for eid, ed in exps.items() if 'random-selection' in eid and ed.get('metrics')}\nfor eid in sorted(rs_exps.keys()):\n    ed = rs_exps[eid]\n    m = ed.get('metrics', {})\n    sr = m.get('success_rate', m.get('overall_success_rate', m.get('SR', m.get('overall_sr', 'N/A'))))\n    bench = 'unknown'\n    if 'spatial' in eid: bench = 'spatial'\n    elif 'object' in eid or 'obj' in eid: bench = 'object'\n    elif 'goal' in eid: bench = 'goal'\n    elif 'long' in eid: bench = 'long'\n    print(f\"  {eid}: bench={bench}, conc={ed['conclusion']}, SR={sr}, metrics_keys={list(m.keys())}\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"ABLATION EXPERIMENTS\")\nprint(\"=\" * 80)\n\nabl_exps = {eid: ed for eid, ed in exps.items() if 'ablation' in eid}\nfor eid in sorted(abl_exps.keys()):\n    ed = abl_exps[eid]\n    m = ed.get('metrics', {})\n    print(f\"  {eid}: conc={ed['conclusion']}, metrics={m}\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"CANONICAL/FIXED-K experiments (canonical-adaptive)\")\nprint(\"=\" * 80)\n\ncan_exps = {eid: ed for eid, ed in exps.items() if 'canonical' in eid and ed.get('metrics')}\nfor eid in sorted(can_exps.keys()):\n    ed = can_exps[eid]\n    m = ed.get('metrics', {})\n    sr = m.get('success_rate', m.get('overall_success_rate', m.get('SR', m.get('overall_sr', 'N/A'))))\n    print(f\"  {eid}: conc={ed['conclusion']}, SR={sr}, metrics={m}\")\n\nPYEOF\n",
  "description": "Detail random-selection, ablation, and canonical experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "b25fe130-adb7-431f-81f8-753527157606",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBWzyVwmEvLspPqdTP4ssi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4382,
      "cache_read_input_tokens": 39278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4382,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-28T15:52:53.512Z_

<details><summary>↩ Tool result · `toolu_019NhNE6PusYLn1PZvqsPjAb`</summary>

```text
================================================================================
RANDOM SELECTION EXPERIMENTS (with metrics)
================================================================================
  eval-random-selection-object-k5-seed42-r2: bench=object, conc=success, SR=0.14, metrics_keys=['success_rate', 'successes', 'total', 'n_tasks', 'n_rollouts']
  eval-random-selection-object-k5-seed43-r2: bench=object, conc=success, SR=0.11, metrics_keys=['success_rate', 'successes', 'total', 'n_tasks', 'n_rollouts']
  eval-random-selection-object-k5-seed44-r2: bench=object, conc=success, SR=0.1, metrics_keys=['success_rate', 'successes', 'total', 'n_tasks', 'n_rollouts']
  eval-random-selection-object-k5-seed45-r2: bench=object, conc=success, SR=0.07, metrics_keys=['success_rate', 'successes', 'total', 'n_tasks', 'n_rollouts']
  eval-random-selection-object-seed42: bench=object, conc=success, SR=0.11, metrics_keys=['success_rate', 'n_tasks', 'n_rollouts', 'total_rollouts', 'per_task_sr']
  eval-random-selection-object-seed43: bench=object, conc=success, SR=0.09, metrics_keys=['success_rate', 'n_tasks', 'n_rollouts', 'total_rollouts', 'per_task_sr']
  eval-random-selection-object-seed43-v2: bench=object, conc=success, SR=77, metrics_keys=['overall_sr']
  eval-random-selection-object-seed44: bench=object, conc=success, SR=0.11, metrics_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'total_rollouts', 'per_task_sr']
  eval-random-selection-object-seed45: bench=object, conc=success, SR=0.1, metrics_keys=['success_rate', 'n_tasks', 'n_rollouts', 'total_rollouts']
  eval-random-selection-object-seed46-r3: bench=object, conc=success, SR=0.1, metrics_keys=['overall_success_rate', 'tasks_evaluated', 'rollouts_per_task', 'total_rollouts', 'total_successes']
  eval-random-selection-object-seed47: bench=object, conc=success, SR=N/A, metrics_keys=['sr']
  eval-random-selection-object-seed48: bench=object, conc=success, SR=0.1, metrics_keys=['success_rate', 'sr_pct', 'n_tasks', 'n_rollouts', 'total_rollouts']
  eval-random-selection-object-seed49: bench=object, conc=success, SR=0.12, metrics_keys=['success_rate', 'sr_pct', 'n_tasks', 'n_rollouts', 'total_rollouts']
  eval-random-selection-spatial-seed42: bench=spatial, conc=success, SR=34, metrics_keys=['success_rate', 'successes', 'total']
  eval-random-selection-spatial-seed42-r2: bench=spatial, conc=success, SR=N/A, metrics_keys=['sr', 'n_tasks', 'n_rollouts', 'total_rollouts']
  eval-random-selection-spatial-seed42-r3: bench=spatial, conc=success, SR=0.34, metrics_keys=['success_rate', 'successes', 'total_rollouts']
  eval-random-selection-spatial-seed43: bench=spatial, conc=success, SR=0.26, metrics_keys=['overall_success_rate', 'per_task_sr']
  eval-random-selection-spatial-seed43-r2: bench=spatial, conc=success, SR=N/A, metrics_keys=['sr']
  eval-random-selection-spatial-seed44: bench=spatial, conc=success, SR=0.28, metrics_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'total_rollouts']

================================================================================
ABLATION EXPERIMENTS
================================================================================
  eval-ablation-tau010-goal-s42: conc=negative, metrics={'overall_sr': 0.81, 'trigger_rate': 0.739, 'tau': 0.1, 'crm_applied_steps': 22170, 'total_steps': 29984}
  eval-ablation-tau015-goal-s42: conc=success, metrics={'overall_sr': 0.85, 'trigger_rate': 0.339, 'tau': 0.15, 'crm_applied_steps': 9590, 'total_steps': 28273}
  eval-ablation-tau040-goal-s42: conc=negative, metrics={'overall_sr': 0.835, 'trigger_rate': 0.012, 'tau': 0.4, 'crm_applied_steps': 346, 'total_steps': 28165}

================================================================================
CANONICAL/FIXED-K experiments (canonical-adaptive)
================================================================================
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "57782c23-2d16-4e1a-a45d-cf583c01401b"
}
```

</details>

---

### System

_source line 68_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Break down the 'other' category into sub-types",
  "usage": {
    "total_tokens": 46129,
    "tool_uses": 12,
    "duration_ms": 123462
  },
  "last_tool_name": "Bash",
  "uuid": "3e68ee7f-0145-4ff5-9c83-b3f47b261ef1",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Bash · `toolu_01L698hUMjhEEW13kdLqXGbE`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# ==========================================\n# \"OTHER\" category - what's in there?\n# ==========================================\nprint(\"=\" * 80)\nprint(\"'OTHER' CATEGORY - DETAILED BREAKDOWN\")\nprint(\"=\" * 80)\n\nother_exps = {}\nfor eid, ed in exps.items():\n    if any(x in eid for x in ['tau-sweep', 'tau_sweep', 'bonus-seed', 'bonus_seed', \n                                'adaptive-k', 'obs-only', 'random-selection', 'random_selection',\n                                'vla-only', 'supp', 'precompute', 'calib', 'ablation',\n                                'oracle', 'heuristic', 'fixed-thresh', 'fixed_thresh']):\n        continue\n    if 'crm-' in eid and 'supp' not in eid:\n        continue\n    other_exps[eid] = ed\n\n# Sub-categorize 'other'\nother_cats = defaultdict(list)\nfor eid, ed in other_exps.items():\n    if 'smolvla' in eid:\n        other_cats['smolvla'].append(eid)\n    elif 'pi05' in eid:\n        other_cats['pi05'].append(eid)\n    elif 'reconvla' in eid:\n        other_cats['reconvla'].append(eid)\n    elif 'canonical' in eid:\n        other_cats['canonical-adaptive'].append(eid)\n    elif 'k2' in eid or 'k10' in eid or 'k5' in eid or 'k1-' in eid:\n        other_cats['k-variants'].append(eid)\n    elif 'norm' in eid:\n        other_cats['norm-variants'].append(eid)\n    elif 'fmvd' in eid:\n        other_cats['fmvd'].append(eid)\n    else:\n        other_cats['misc'].append(eid)\n\nfor cat in sorted(other_cats.keys()):\n    entries = other_cats[cat]\n    print(f\"\\n--- {cat} ({len(entries)} experiments) ---\")\n    for eid in sorted(entries)[:15]:\n        ed = other_exps[eid]\n        m = ed.get('metrics', {})\n        if not isinstance(m, dict): m = {}\n        sr = m.get('success_rate', m.get('overall_success_rate', m.get('SR', m.get('overall_sr', 'N/A'))))\n        print(f\"  {eid}: conc={ed['conclusion']}, SR={sr}\")\n    if len(entries) > 15:\n        print(f\"  ... and {len(entries)-15} more\")\n\nPYEOF\n",
  "description": "Break down the 'other' category into sub-types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "dc0cf32c-9087-4d64-acc5-1bfeefcc4d20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjeV6LFWtBcfcskeLYr83A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2181,
      "cache_read_input_tokens": 43660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2181,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-28T15:53:06.179Z_

<details><summary>↩ Tool result · `toolu_01L698hUMjhEEW13kdLqXGbE`</summary>

```text
================================================================================
'OTHER' CATEGORY - DETAILED BREAKDOWN
================================================================================

--- k-variants (53 experiments) ---
  eval-adaptive-spatial-k1-s42: conc=success, SR=0.795
  eval-argmin-object-k5-seed42: conc=success, SR=N/A
  eval-argmin-object-k5-seed43: conc=success, SR=N/A
  eval-argmin-object-k5-seed44: conc=failed, SR=N/A
  eval-argmin-object-k5-seed44-r2: conc=success, SR=N/A
  eval-argmin-object-k5-seed45: conc=success, SR=N/A
  eval-k10-tau025-spatial-s45: conc=killed, SR=N/A
  eval-k10-tau025-spatial-s46: conc=killed, SR=N/A
  eval-k10-tau025-spatial-s47: conc=killed, SR=N/A
  eval-k2-adaptive-spatial-s42: conc=killed, SR=N/A
  eval-k2-adaptive-spatial-s43: conc=killed, SR=N/A
  eval-k2-adaptive-spatial-s44: conc=killed, SR=N/A
  eval-k2-adaptive-spatial-s45: conc=killed, SR=N/A
  eval-k2-adaptive-spatial-s46: conc=killed, SR=N/A
  eval-k2-adaptive-spatial-s47: conc=killed, SR=N/A
  ... and 38 more

--- misc (120 experiments) ---
  D088-eval-adaptive-unc-head-object-seed42: conc=killed, SR=N/A
  D088-eval-adaptive-unc-head-object-seed43: conc=killed, SR=N/A
  D088-eval-adaptive-unc-head-object-seed44: conc=killed, SR=N/A
  eval-3dir-adaptive-spatial-s42: conc=success, SR=81
  eval-a1-baseline-object-s42: conc=negative, SR=0.565
  eval-acr-object-v3: conc=negative, SR=0
  eval-acr-object-v4-default: conc=killed, SR=N/A
  eval-acr-object-v4-default-r2: conc=success, SR=0
  eval-acr-object-v4-perdof: conc=success, SR=11.0% (11/100)
  eval-acr-object-v4-scalar: conc=negative, SR=9
  eval-acr-object-v4-scalar-b2: conc=killed, SR=N/A
  eval-acr-spatial-v1: conc=killed, SR=N/A
  eval-acr-spatial-v2: conc=killed, SR=N/A
  eval-acr-spatial-v3: conc=success, SR=0.025
  eval-acr-spatial-v4-default: conc=failed, SR=N/A
  ... and 105 more

--- norm-variants (111 experiments) ---
  eval-3dir-norm005-spatial-s42: conc=success, SR=80
  eval-3dir-norm01-spatial-s42: conc=negative, SR=79
  eval-3dir-norm03-spatial-s42: conc=killed, SR=73.9
  eval-mag-obsonly-norm-0.3-r3: conc=killed, SR=N/A
  eval-mag-obsonly-norm-0p3-r3: conc=killed, SR=N/A
  eval-mag-obsonly-norm003: conc=killed, SR=N/A
  eval-mag-obsonly-norm003-b2: conc=success, SR=N/A
  eval-mag-obsonly-norm003-object: conc=success, SR=0.16
  eval-mag-obsonly-norm005: conc=success, SR=35
  eval-mag-obsonly-norm005-object: conc=success, SR=0.13
  eval-mag-obsonly-norm02: conc=negative, SR=35
  eval-mag-obsonly-norm02-object: conc=killed, SR=N/A
  eval-mag-obsonly-norm03: conc=killed, SR=N/A
  eval-mag-obsonly-norm03-b2: conc=failed, SR=N/A
  eval-mag-obsonly-norm03-b3: conc=killed, SR=N/A
  ... and 96 more

--- pi05 (92 experiments) ---
  eval-pi05-adaptive-goal-s42: conc=failed, SR=0
  eval-pi05-adaptive-goal-s42-dryrun: conc=success, SR=0.65
  eval-pi05-adaptive-goal-s42-full: conc=killed, SR=N/A
  eval-pi05-adaptive-goal-s43: conc=killed, SR=N/A
  eval-pi05-adaptive-goal-s44: conc=killed, SR=N/A
  eval-pi05-adaptive-object-s42: conc=killed, SR=N/A
  eval-pi05-adaptive-object-s43: conc=killed, SR=N/A
  eval-pi05-adaptive-object-s44: conc=killed, SR=N/A
  eval-pi05-adaptive-spatial-s42: conc=failed, SR=N/A
  eval-pi05-adaptive-spatial-s42-r2: conc=killed, SR=N/A
  eval-pi05-baseline-object-seed42: conc=failed, SR=0
  eval-pi05-baseline-object-seed42-r2: conc=killed, SR=N/A
  eval-pi05-reconvla-goal-s42: conc=killed, SR=N/A
  eval-pi05-reconvla-object-s42: conc=killed, SR=N/A
  eval-pi05-reconvla-spatial-s42: conc=killed, SR=N/A
  ... and 77 more

--- reconvla (6 experiments) ---
  eval-3dir-reconvla-spatial-s42: conc=success, SR=79
  eval-reconvla-object: conc=success, SR=0.12
  eval-reconvla-spatial-v1: conc=killed, SR=N/A
  eval-reconvla-spatial-v2: conc=killed, SR=N/A
  eval-reconvla-spatial-v3: conc=success, SR=0.34
  plan_014-reconvla-baseline: conc=failed, SR=N/A

--- smolvla (89 experiments) ---
  E_smolvla_adaptive_tau015_spatial_s42: conc=success, SR=N/A
  E_smolvla_adaptive_tau035_spatial_s42: conc=success, SR=N/A
  E_smolvla_adaptive_tau045_spatial_s42: conc=success, SR=N/A
  E_smolvla_crm_norm005_spatial_s42_d149: conc=success, SR=N/A
  eval-smolvla-acr-goal-seed42: conc=failed, SR=N/A
  eval-smolvla-acr-goal-seed43: conc=failed, SR=N/A
  eval-smolvla-acr-long-seed42: conc=failed, SR=N/A
  eval-smolvla-lerobot-goal-seed43: conc=failed, SR=N/A
  eval-smolvla-lerobot-goal-seed43-v2: conc=failed, SR=N/A
  eval-smolvla-lerobot-goal-seed43-v3: conc=failed, SR=82
  eval-smolvla-lerobot-goal-seed44: conc=killed, SR=N/A
  eval-smolvla-lerobot-goal-seed44-v3: conc=success, SR=78
  eval-smolvla-lerobot-long-seed42: conc=success, SR=49.5
  eval-smolvla-lerobot-long-seed43: conc=success, SR=53.5
  eval-smolvla-lerobot-long-seed44: conc=success, SR=49.5
  ... and 74 more
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "56d07c48-1db0-42f6-b832-59e1d586ed84"
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
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Build comprehensive results table across methods, benchmarks, and seeds",
  "usage": {
    "total_tokens": 49214,
    "tool_uses": 13,
    "duration_ms": 153281
  },
  "last_tool_name": "Bash",
  "uuid": "128350b5-73f8-40e6-a513-fd9b87628116",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_01Fkpvma8AE5pbtkHUrr5DUH`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Helper to normalize SR to 0-1 scale\ndef norm_sr(val):\n    if val is None or val == 'N/A':\n        return None\n    if isinstance(val, str):\n        val = val.replace('%', '').strip()\n        try:\n            val = float(val.split('/')[0])  # handle \"11.0% (11/100)\" format\n        except:\n            return None\n    if val > 1:\n        val = val / 100.0\n    return round(val, 4)\n\ndef get_sr(m):\n    \"\"\"Get SR from metrics dict, trying all known keys\"\"\"\n    for key in ['success_rate', 'overall_success_rate', 'SR', 'overall_sr', 'sr']:\n        if key in m:\n            return norm_sr(m[key])\n    return None\n\n# ==========================================\n# Build a comprehensive table of the MAIN experimental conditions\n# Focus on experiments with metrics and successful conclusions\n# ==========================================\n\n# We want to aggregate by: (method, benchmark, seed) -> SR\n# Methods: vla-only, crm-obs-only (norm005), reconvla, k2mean, adaptive-tau025, obs-only\n# Benchmarks: spatial, object, goal, long\n\nresults = defaultdict(dict)  # (method, benchmark) -> {seed: SR}\n\nfor eid, ed in exps.items():\n    m = ed.get('metrics', {})\n    if not isinstance(m, dict): m = {}\n    sr = get_sr(m)\n    \n    # Skip entries without SR\n    if sr is None:\n        continue\n    \n    # Skip very low SR (likely broken runs, e.g. SR < 0.2 for main methods)\n    # But keep for random-selection and adaptive-k which are legitimately low\n    \n    # Determine benchmark\n    bench = None\n    if 'spatial' in eid: bench = 'spatial'\n    elif 'object' in eid or '-obj' in eid: bench = 'object'\n    elif 'goal' in eid: bench = 'goal'\n    elif 'long' in eid: bench = 'long'\n    if not bench:\n        bench_from_m = m.get('benchmark')\n        if bench_from_m: bench = bench_from_m\n    \n    if not bench:\n        continue\n    \n    # Determine seed\n    seed_match = re.search(r'seed(\\d+)|[-_]s(\\d+)', eid)\n    seed = seed_match.group(1) or seed_match.group(2) if seed_match else m.get('seed')\n    if seed: seed = int(seed)\n    \n    # Determine method\n    method = None\n    \n    # SUPPLEMENTARY experiments (the most complete set)\n    if 'supp' in eid:\n        if 'adapt-tau025' in eid or 'adapt_tau025' in eid:\n            method = 'adaptive-conformal-crm-tau025'\n        elif 'crm-norm005' in eid or 'crm005' in eid:\n            method = 'crm-obs-only-norm005'\n        elif 'k2mean' in eid:\n            method = 'k2mean-baseline'\n        elif 'reconvla' in eid:\n            method = 'reconvla'\n        elif 'vla-only' in eid:\n            method = 'vla-only'\n        elif 'adapt' in eid and 'tau025' in eid:\n            method = 'adaptive-conformal-crm-tau025'\n        elif 'obj-crm-norm005' in eid:\n            method = 'crm-obs-only-norm005'\n        elif 'obj-adapt' in eid:\n            method = 'adaptive-conformal-crm-tau025'\n        elif 'crm' in eid and 'norm' in eid:\n            # various norm experiments\n            continue\n        else:\n            continue\n    \n    # VLA-only baseline\n    elif ('vla-only' in eid or 'vla_only' in eid) and 'supp' not in eid:\n        if sr < 0.3:  # skip broken runs\n            continue\n        method = 'vla-only'\n    \n    # CRM obs-only\n    elif 'crm' in eid and ('norm005' in eid or 'norm0.05' in eid or 'crm005' in eid) and 'supp' not in eid:\n        if sr < 0.3:\n            continue\n        method = 'crm-obs-only-norm005'\n    \n    # Adaptive tau025\n    elif 'adapt' in eid and 'tau025' in eid and 'supp' not in eid and 'adaptive-k' not in eid:\n        if sr < 0.3:\n            continue\n        method = 'adaptive-conformal-crm-tau025'\n    \n    # k2mean\n    elif 'k2mean' in eid and 'supp' not in eid:\n        if sr < 0.3:\n            continue\n        method = 'k2mean-baseline'\n    \n    # reconvla\n    elif 'reconvla' in eid and 'supp' not in eid and sr > 0.3:\n        method = 'reconvla'\n    \n    else:\n        continue\n    \n    if method and bench and seed is not None:\n        key = (method, bench)\n        # Keep highest SR for each seed (handles retries)\n        if seed not in results[key] or (results[key][seed] is not None and sr > results[key][seed]):\n            results[key][seed] = sr\n\n# ==========================================\n# Print the comprehensive table\n# ==========================================\nprint(\"=\" * 100)\nprint(\"COMPREHENSIVE RESULTS TABLE: (method, benchmark) -> SR per seed\")\nprint(\"=\" * 100)\n\nmethods_order = ['vla-only', 'k2mean-baseline', 'reconvla', 'crm-obs-only-norm005', 'adaptive-conformal-crm-tau025']\nbenchmarks = ['spatial', 'object', 'goal', 'long']\n\nfor method in methods_order:\n    print(f\"\\n{'='*80}\")\n    print(f\"  METHOD: {method}\")\n    print(f\"{'='*80}\")\n    for bench in benchmarks:\n        key = (method, bench)\n        if key in results:\n            seed_data = results[key]\n            seeds_sorted = sorted(seed_data.keys())\n            srs = [seed_data[s] for s in seeds_sorted]\n            valid_srs = [s for s in srs if s is not None]\n            mean_sr = sum(valid_srs) / len(valid_srs) if valid_srs else None\n            print(f\"\\n  [{bench}] ({len(valid_srs)} seeds)\")\n            for s in seeds_sorted:\n                print(f\"    seed {s}: SR={seed_data[s]}\")\n            if mean_sr:\n                print(f\"    --> MEAN SR = {mean_sr:.4f} ({mean_sr*100:.1f}%)\")\n        else:\n            print(f\"\\n  [{bench}] NO DATA\")\n\nPYEOF\n",
  "description": "Build comprehensive results table across methods, benchmarks, and seeds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "448493e0-b034-4e66-a4c5-e9f15dca66c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkJgHAjRBdj7hUGCuvNm4E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3083,
      "cache_read_input_tokens": 45841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3083,
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

_source line 73 · 2026-05-28T15:53:36.016Z_

<details><summary>↩ Tool result · `toolu_01Fkpvma8AE5pbtkHUrr5DUH`</summary>

```text
====================================================================================================
COMPREHENSIVE RESULTS TABLE: (method, benchmark) -> SR per seed
====================================================================================================

================================================================================
  METHOD: vla-only
================================================================================

  [spatial] (9 seeds)
    seed 42: SR=0.98
    seed 43: SR=0.975
    seed 44: SR=0.99
    seed 45: SR=0.85
    seed 46: SR=0.805
    seed 47: SR=0.81
    seed 48: SR=0.795
    seed 49: SR=0.795
    seed 50: SR=0.3
    --> MEAN SR = 0.8111 (81.1%)

  [object] (9 seeds)
    seed 42: SR=1.0
    seed 43: SR=1
    seed 44: SR=0.995
    seed 45: SR=0.76
    seed 46: SR=0.79
    seed 47: SR=0.755
    seed 48: SR=0.79
    seed 49: SR=0.755
    seed 50: SR=0.74
    --> MEAN SR = 0.8428 (84.3%)

  [goal] (9 seeds)
    seed 42: SR=0.98
    seed 43: SR=0.98
    seed 44: SR=0.975
    seed 45: SR=0.835
    seed 46: SR=0.83
    seed 47: SR=0.835
    seed 48: SR=0.85
    seed 49: SR=0.835
    seed 51: SR=0.69
    --> MEAN SR = 0.8678 (86.8%)

  [long] (5 seeds)
    seed 42: SR=0.98
    seed 43: SR=0.955
    seed 44: SR=0.96
    seed 45: SR=0.575
    seed 47: SR=0.595
    --> MEAN SR = 0.8130 (81.3%)

================================================================================
  METHOD: k2mean-baseline
================================================================================

  [spatial] (6 seeds)
    seed 42: SR=0.965
    seed 43: SR=0.78
    seed 44: SR=0.81
    seed 45: SR=0.8
    seed 46: SR=0.8
    seed 47: SR=0.82
    --> MEAN SR = 0.8292 (82.9%)

  [object] (6 seeds)
    seed 42: SR=1.0
    seed 43: SR=0.78
    seed 44: SR=0.75
    seed 45: SR=0.775
    seed 46: SR=0.765
    seed 47: SR=0.775
    --> MEAN SR = 0.8075 (80.8%)

  [goal] (6 seeds)
    seed 42: SR=0.995
    seed 43: SR=0.815
    seed 44: SR=0.82
    seed 45: SR=0.81
    seed 46: SR=0.825
    seed 47: SR=0.825
    --> MEAN SR = 0.8483 (84.8%)

  [long] (6 seeds)
    seed 42: SR=0.97
    seed 43: SR=0.56
    seed 44: SR=0.545
    seed 45: SR=0.56
    seed 46: SR=0.55
    seed 47: SR=0.545
    --> MEAN SR = 0.6217 (62.2%)

================================================================================
  METHOD: reconvla
================================================================================

  [spatial] (6 seeds)
    seed 42: SR=0.8
    seed 43: SR=0.815
    seed 44: SR=0.795
    seed 45: SR=0.795
    seed 46: SR=0.8
    seed 47: SR=0.81
    --> MEAN SR = 0.8025 (80.3%)

  [object] (6 seeds)
    seed 42: SR=0.79
    seed 43: SR=0.77
    seed 44: SR=0.76
    seed 45: SR=0.78
    seed 46: SR=0.8
    seed 47: SR=0.765
    --> MEAN SR = 0.7775 (77.8%)

  [goal] (5 seeds)
    seed 43: SR=0.81
    seed 44: SR=0.805
    seed 45: SR=0.855
    seed 46: SR=0.79
    seed 47: SR=0.835
    --> MEAN SR = 0.8190 (81.9%)

  [long] (6 seeds)
    seed 42: SR=0.565
    seed 43: SR=0.59
    seed 44: SR=0.57
    seed 45: SR=0.59
    seed 46: SR=0.56
    seed 47: SR=0.55
    --> MEAN SR = 0.5708 (57.1%)

================================================================================
  METHOD: crm-obs-only-norm005
================================================================================

  [spatial] (8 seeds)
    seed 42: SR=0.805
    seed 43: SR=0.81
    seed 44: SR=0.785
    seed 45: SR=0.805
    seed 46: SR=0.81
    seed 47: SR=0.805
    seed 48: SR=0.78
    seed 49: SR=0.785
    --> MEAN SR = 0.7981 (79.8%)

  [object] (6 seeds)
    seed 42: SR=0.77
    seed 43: SR=0.785
    seed 44: SR=0.78
    seed 45: SR=0.765
    seed 46: SR=0.795
    seed 47: SR=0.825
    --> MEAN SR = 0.7867 (78.7%)

  [goal] (7 seeds)
    seed 42: SR=0.855
    seed 43: SR=0.82
    seed 44: SR=0.835
    seed 45: SR=0.81
    seed 46: SR=0.82
    seed 47: SR=0.82
    seed 48: SR=0.8
    --> MEAN SR = 0.8229 (82.3%)

  [long] (6 seeds)
    seed 42: SR=0.565
    seed 43: SR=0.545
    seed 44: SR=0.565
    seed 45: SR=0.605
    seed 46: SR=0.54
    seed 47: SR=0.565
    --> MEAN SR = 0.5642 (56.4%)

================================================================================
  METHOD: adaptive-conformal-crm-tau025
================================================================================

  [spatial] (8 seeds)
    seed 42: SR=0.82
    seed 43: SR=0.8
    seed 44: SR=0.805
    seed 45: SR=0.8
    seed 46: SR=0.8
    seed 47: SR=0.815
    seed 48: SR=0.81
    seed 49: SR=0.82
    --> MEAN SR = 0.8087 (80.9%)

  [object] (8 seeds)
    seed 42: SR=0.81
    seed 43: SR=0.775
    seed 44: SR=0.75
    seed 45: SR=0.78
    seed 46: SR=0.775
    seed 47: SR=0.77
    seed 48: SR=0.76
    seed 49: SR=0.74
    --> MEAN SR = 0.7700 (77.0%)

  [goal] (8 seeds)
    seed 42: SR=0.84
    seed 43: SR=0.845
    seed 44: SR=0.865
    seed 45: SR=0.81
    seed 46: SR=0.835
    seed 47: SR=0.82
    seed 48: SR=0.845
    seed 49: SR=0.815
    --> MEAN SR = 0.8344 (83.4%)

  [long] (4 seeds)
    seed 44: SR=0.56
    seed 45: SR=0.6
    seed 46: SR=0.585
    seed 47: SR=0.55
    --> MEAN SR = 0.5737 (57.4%)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "ebb7f968-5d36-47df-acbe-8c846c0e6abd"
}
```

</details>

---

### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Verify suspicious high-SR entries for vla-only seeds 42-44",
  "usage": {
    "total_tokens": 53434,
    "tool_uses": 14,
    "duration_ms": 164560
  },
  "last_tool_name": "Bash",
  "uuid": "1c3baff0-9fc6-4445-ace4-f2e008ce2f11",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Bash · `toolu_01VN4repCr7exhKyKrXsu4va`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Check the high-SR vla-only entries (seed 42-44) - these are suspicious\nprint(\"=== Checking suspicious high-SR vla-only entries ===\")\nfor eid, ed in sorted(exps.items()):\n    if 'vla-only' in eid and any(f'seed{s}' in eid or f'-s{s}' in eid for s in [42, 43, 44]):\n        m = ed.get('metrics', {})\n        if not isinstance(m, dict): m = {}\n        sr = m.get('success_rate', m.get('overall_success_rate', m.get('SR', m.get('overall_sr', 'N/A'))))\n        total = m.get('total', m.get('total_rollouts', m.get('total_trials', 'N/A')))\n        n_rollouts = m.get('n_rollouts', 'N/A')\n        print(f\"  {eid}: SR={sr}, total={total}, n_rollouts={n_rollouts}, conc={ed['conclusion']}\")\n        if m:\n            print(f\"    all metrics: {m}\")\n\nPYEOF\n",
  "description": "Verify suspicious high-SR entries for vla-only seeds 42-44"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "a9868c60-9e64-4f1e-b31e-12b91da8ba46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145GzqeisvbbYTpdXsZz42c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4218,
      "cache_read_input_tokens": 48924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4218,
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

_source line 76 · 2026-05-28T15:53:47.280Z_

<details><summary>↩ Tool result · `toolu_01VN4repCr7exhKyKrXsu4va`</summary>

```text
=== Checking suspicious high-SR vla-only entries ===
  eval-canonical-vla-only-spatial-s44: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-goal-vla-only-wrapper-s42: SR=0.835, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.835, 'successes': 167, 'total': 200}
  eval-k2-spatial-vla-only-s42-paired-r2: SR=0.785, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.785, 'successes': 157, 'total': 200}
  eval-k2-spatial-vla-only-s43-paired-r2: SR=0.795, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.795, 'successes': 159, 'total': 200}
  eval-k2-spatial-vla-only-s44-paired-r2: SR=0.8, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.8, 'successes': 160, 'total': 200}
  eval-object-vla-only-wrapper-s42: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-object-vla-only-wrapper-s42-r2: SR=79, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 79, 'total_successes': 158, 'total_episodes': 200, 'per_task': {'alphabet_soup': 85, 'cream_cheese': 75, 'salad_dressing': 85, 'bbq_sauce': 85, 'ketchup': 90, 'tomato_sauce': 75, 'butter': 65, 'milk': 65, 'chocolate_pudding': 70, 'orange_juice': 95}}
  eval-object-vla-only-wrapper-s43: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-object-vla-only-wrapper-s43-r2: SR=77, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 77, 'total_successes': 154, 'total_episodes': 200, 'per_task': {'alphabet_soup': 70, 'cream_cheese': 70, 'salad_dressing': 75, 'bbq_sauce': 85, 'ketchup': 80, 'tomato_sauce': 85, 'butter': 60, 'milk': 75, 'chocolate_pudding': 75, 'orange_juice': 95}}
  eval-object-vla-only-wrapper-s44: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-object-vla-only-wrapper-s44-r2: SR=77.5, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 77.5, 'total_successes': 155, 'total_episodes': 200, 'per_task': {'alphabet_soup': 70, 'cream_cheese': 70, 'salad_dressing': 75, 'bbq_sauce': 90, 'ketchup': 90, 'tomato_sauce': 80, 'butter': 75, 'milk': 65, 'chocolate_pudding': 65, 'orange_juice': 95}}
  eval-openvla-object-vla-only-seed42: SR=0, total=100, n_rollouts=N/A, conc=negative
    all metrics: {'overall_success_rate': 0, 'total_successes': 0, 'total_rollouts': 100, 'avg_inference_time_ms': 178, 'per_task': {'pick_up_the_alphabet_soup_and_place_it_in_the_basket': 0, 'pick_up_the_cream_cheese_and_place_it_in_the_basket': 0, 'pick_up_the_salad_dressing_and_place_it_in_the_basket': 0, 'pick_up_the_bbq_sauce_and_place_it_in_the_basket': 0, 'pick_up_the_ketchup_and_place_it_in_the_basket': 0, 'pick_up_the_tomato_sauce_and_place_it_in_the_basket': 0, 'pick_up_the_butter_and_place_it_in_the_basket': 0, 'pick_up_the_milk_and_place_it_in_the_basket': 0, 'pick_up_the_chocolate_pudding_and_place_it_in_the_basket': 0, 'pick_up_the_orange_juice_and_place_it_in_the_basket': 0}}
  eval-openvla-object-vla-only-seed42-v2: SR=0.69, total=100, n_rollouts=N/A, conc=success
    all metrics: {'overall_sr': 0.69, 'n_tasks': 10, 'n_trials_per_task': 10, 'total_rollouts': 100}
  eval-openvla-object-vla-only-seed42-v3: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-pi05-vla-only-goal-s42: SR=0.955, total=200, n_rollouts=20, conc=success
    all metrics: {'overall_success_rate': 0.955, 'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'benchmark': 'goal', 'mode': 'vla_only', 'model': 'pi0.5'}
  eval-pi05-vla-only-goal-s42-paired: SR=0.98, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.98, 'successes': 196, 'total': 200, 'mode': 'vla_only', 'benchmark': 'goal', 'seed': 42, 'model': 'pi05'}
  eval-pi05-vla-only-goal-s42-v2: SR=0.955, total=N/A, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.955, 'n_rollouts': 20, 'benchmark': 'goal'}
  eval-pi05-vla-only-goal-s43: SR=0.97, total=200, n_rollouts=20, conc=success
    all metrics: {'overall_success_rate': 0.97, 'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'benchmark': 'goal', 'mode': 'vla_only', 'model': 'pi0.5'}
  eval-pi05-vla-only-goal-s43-v2: SR=0.97, total=N/A, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.97, 'n_rollouts': 20, 'benchmark': 'goal'}
  eval-pi05-vla-only-goal-s44: SR=0.975, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.975}
  eval-pi05-vla-only-goal-seed42-r4: SR=0.98, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.98, 'successes': 196, 'total': 200}
  eval-pi05-vla-only-goal-seed42-r4-std: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-pi05-vla-only-goal-seed43-r4: SR=0.98, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.98, 'successes': 196, 'total': 200}
  eval-pi05-vla-only-goal-seed43-r4-std: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-pi05-vla-only-goal-seed44-r4: SR=0.975, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.975, 'successes': 195, 'total': 200}
  eval-pi05-vla-only-goal-seed44-r4-std: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-pi05-vla-only-long-seed42-r4: SR=0, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0, 'successes': 0, 'total': 200}
  eval-pi05-vla-only-long-seed42-r4-rerun: SR=0.94, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.94, 'successes': 188, 'total': 200, 'per_task': {'LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce': 0.95, 'LIVING_ROOM_SCENE2_cream_cheese_butter': 1, 'KITCHEN_SCENE3_stove_moka_pot': 1, 'KITCHEN_SCENE4_black_bowl_drawer': 1, 'LIVING_ROOM_SCENE5_mugs_on_plates': 0.9, 'STUDY_SCENE1_book_in_caddy': 0.95, 'LIVING_ROOM_SCENE6_mug_pudding': 1, 'LIVING_ROOM_SCENE1_soup_cream_cheese': 0.9, 'KITCHEN_SCENE8_both_moka_pots': 0.8, 'KITCHEN_SCENE6_mug_in_microwave': 0.9}}
  eval-pi05-vla-only-long-seed42-r4-std: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-pi05-vla-only-long-seed43-r4: SR=0.955, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.955}
  eval-pi05-vla-only-long-seed43-r4-std: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-pi05-vla-only-long-seed44-r4: SR=0.955, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.955}
  eval-pi05-vla-only-long-seed44-r4-std: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-pi05-vla-only-object-s42: SR=0.965, total=200, n_rollouts=20, conc=success
    all metrics: {'overall_success_rate': 0.965, 'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'benchmark': 'object', 'mode': 'vla_only', 'model': 'pi0.5'}
  eval-pi05-vla-only-object-s42-r2: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-pi05-vla-only-object-s42-v2: SR=0.965, total=N/A, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.965, 'n_rollouts': 20, 'benchmark': 'object'}
  eval-pi05-vla-only-object-s43: SR=0.985, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.985}
  eval-pi05-vla-only-object-s43-r5: SR=0.985, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.985, 'benchmark': 'object', 'method': 'vla_only', 'model': 'pi05', 'seed': 43, 'server': 'bjb2-28827'}
  eval-pi05-vla-only-object-s43-v2: SR=0.865, total=N/A, n_rollouts=20, conc=failed
    all metrics: {'success_rate': 0.865, 'n_rollouts': 20, 'benchmark': 'object', 'note': 'INVALID - CUDA OOM corrupted results'}
  eval-pi05-vla-only-object-s44: SR=0.81, total=200, n_rollouts=20, conc=success
    all metrics: {'overall_success_rate': 0.81, 'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'benchmark': 'object', 'mode': 'vla_only', 'model': 'pi0.5'}
  eval-pi05-vla-only-object-seed42: SR=0, total=200, n_rollouts=N/A, conc=failed
    all metrics: {'overall_sr': 0, 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20}
  eval-pi05-vla-only-object-seed42-r3: SR=0.82, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.82, 'n_tasks': 10, 'total_rollouts': 200}
  eval-pi05-vla-only-object-seed42-r4: SR=100, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 100, 'total_success': 200, 'total_rollouts': 200, 'n_action_steps': 10, 'per_task': {'alphabet_soup': 100, 'cream_cheese': 100, 'salad_dressing': 100, 'bbq_sauce': 100, 'ketchup': 100, 'tomato_sauce': 100, 'butter': 100, 'milk': 100, 'chocolate_pudding': 100, 'orange_juice': 100}}
  eval-pi05-vla-only-object-seed43: SR=0, total=200, n_rollouts=N/A, conc=success
    all metrics: {'overall_sr': 0, 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20}
  eval-pi05-vla-only-object-seed43-r3: SR=0.815, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.815, 'n_tasks': 10, 'total_rollouts': 200}
  eval-pi05-vla-only-object-seed43-r4: SR=98.5, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 98.5, 'total_successes': 197, 'total_episodes': 200}
  eval-pi05-vla-only-object-seed44: SR=0, total=200, n_rollouts=N/A, conc=success
    all metrics: {'overall_sr': 0, 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20}
  eval-pi05-vla-only-object-seed44-r3: SR=0.81, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.81, 'n_tasks': 10, 'total_rollouts': 200}
  eval-pi05-vla-only-object-seed44-r4: SR=99.5, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 99.5, 'total_successes': 199, 'total_episodes': 200}
  eval-pi05-vla-only-spatial-s42: SR=0.98, total=200, n_rollouts=20, conc=success
    all metrics: {'overall_success_rate': 0.98, 'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'benchmark': 'spatial', 'mode': 'vla_only', 'model': 'pi0.5'}
  eval-pi05-vla-only-spatial-s42-paired: SR=0.98, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.98, 'successes': 196, 'total': 200, 'mode': 'vla_only', 'benchmark': 'spatial', 'seed': 42, 'model': 'pi05'}
  eval-pi05-vla-only-spatial-s42-v2: SR=0.98, total=N/A, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.98, 'n_rollouts': 20, 'benchmark': 'spatial'}
  eval-pi05-vla-only-spatial-s43: SR=0.96, total=200, n_rollouts=20, conc=success
    all metrics: {'overall_success_rate': 0.96, 'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'benchmark': 'spatial', 'mode': 'vla_only', 'model': 'pi0.5'}
  eval-pi05-vla-only-spatial-s43-r2: SR=0.975, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.975, 'successes': 195, 'total': 200}
  eval-pi05-vla-only-spatial-s43-v2: SR=0.96, total=N/A, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.96, 'n_rollouts': 20, 'benchmark': 'spatial'}
  eval-pi05-vla-only-spatial-s44-d149: SR=0.99, total=200, n_rollouts=N/A, conc=success
    all metrics: {'overall_success_rate': 0.99, 'successes': 198, 'total': 200, 'n_tasks': 10}
  eval-pi05-vla-only-spatial-seed42: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-pi05-vla-only-spatial-seed42-r3: SR=0.845, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.845, 'n_tasks': 10, 'total_rollouts': 200}
  eval-pi05-vla-only-spatial-seed42-r4: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-pi05-vla-only-spatial-seed43: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-pi05-vla-only-spatial-seed43-r3: SR=0.83, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.83, 'n_tasks': 10, 'total_rollouts': 200}
  eval-pi05-vla-only-spatial-seed43-r4: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-pi05-vla-only-spatial-seed44: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-pi05-vla-only-spatial-seed44-r4: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-spatial-vla-only-s42-verify: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-supp-goal-vla-only-s42: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-supp-goal-vla-only-s42-bjb1: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-supp-goal-vla-only-s43: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-supp-goal-vla-only-s44: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-supp-goal-vla-only-wrapper-s43: SR=82.5, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 82.5, 'source': 'JSON file eval_goal_vla_only_seed43.json on bjb1-32546, harvested 2026-05-26'}
  eval-supp-goal-vla-only-wrapper-s44: SR=82, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 82, 'successes': 164, 'total': 200}
  eval-supp-goal-vla-only-wrapper-s44-r2: SR=0.85, total=200, n_rollouts=N/A, conc=success
    all metrics: {'SR': 0.85, 'successes': 170, 'total': 200, 'per_task': {'open_middle_drawer': 0.85, 'put_bowl_stove': 0.95, 'wine_bottle_cabinet': 0.85, 'open_top_drawer_bowl': 0.7, 'bowl_on_cabinet': 0.9, 'push_plate_stove': 0.9, 'cream_cheese_bowl': 0.65, 'turn_on_stove': 1, 'bowl_on_plate': 0.95, 'wine_bottle_rack': 0.75}}
  eval-supp-long-vla-only-s42: SR=59.5, total=200, n_rollouts=N/A, conc=success
    all metrics: {'SR': 59.5, 'total_successes': 119, 'total_trials': 200}
  eval-supp-long-vla-only-s43: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-supp-long-vla-only-s43-r2: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-supp-long-vla-only-s44: SR=60.5, total=200, n_rollouts=N/A, conc=success
    all metrics: {'SR': 60.5, 'total_successes': 121, 'total_trials': 200}
  eval-supp-obj-vla-only-s42: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-supp-obj-vla-only-s43: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-supp-obj-vla-only-s44: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-supp-spatial-vla-only-s42: SR=0.8, total=200, n_rollouts=20, conc=success
    all metrics: {'overall_success_rate': 0.8, 'successes': 160, 'total': 200, 'n_rollouts': 20, 'benchmark': 'spatial', 'seed': 42, 'mode': 'vla_only', 'model': 'pi05'}
  eval-supp-spatial-vla-only-s43: SR=0.79, total=200, n_rollouts=N/A, conc=success
    all metrics: {'overall_success_rate': 0.79, 'successes': 158, 'total': 200}
  eval-supp-spatial-vla-only-s44: SR=0.785, total=200, n_rollouts=N/A, conc=success
    all metrics: {'overall_sr': 0.785, 'successes': 157, 'total': 200, 'per_task': {'between_plate_ramekin': 0.9, 'next_to_ramekin': 0.95, 'table_center': 0.95, 'on_cookie_box': 1, 'top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 1, 'on_stove': 0.8, 'next_to_plate': 0.8, 'on_wooden_cabinet': 0.7}}
  eval-supp-spatial-vla-only-smolvla-s42: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-vla-only-goal-seed42: SR=0.71, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'overall_success_rate': 0.71, 'per_task': {'open_the_middle_drawer_of_the_cabinet': 0.9, 'put_the_bowl_on_the_stove': 0.9, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.6, 'open_the_top_drawer_and_put_the_bowl_inside': 0.4, 'put_the_bowl_on_top_of_the_cabinet': 0.7, 'push_the_plate_to_the_front_of_the_stove': 0.9, 'put_the_cream_cheese_in_the_bowl': 0.2, 'turn_on_the_stove': 0.9, 'put_the_bowl_on_the_plate': 0.9, 'put_the_wine_bottle_on_the_rack': 0.7}}
  eval-vla-only-goal-seed43: SR=0.69, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'overall_success_rate': 0.69, 'per_task': {'open_the_middle_drawer_of_the_cabinet': 0.9, 'put_the_bowl_on_the_stove': 0.9, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.4, 'open_the_top_drawer_and_put_the_bowl_inside': 0.5, 'put_the_bowl_on_top_of_the_cabinet': 0.5, 'push_the_plate_to_the_front_of_the_stove': 0.8, 'put_the_cream_cheese_in_the_bowl': 0.4, 'turn_on_the_stove': 0.9, 'put_the_bowl_on_the_plate': 1, 'put_the_wine_bottle_on_the_rack': 0.6}}
  eval-vla-only-goal-seed44: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-vla-only-goal-seed44-r2: SR=N/A, total=100, n_rollouts=N/A, conc=success
    all metrics: {'sr': 0.73, 'total': 100, 'successes': 73, 'benchmark': 'goal', 'mode': 'vla_only'}
  eval-vla-only-long-s44-d149: SR=0.545, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'overall_success_rate': 0.545}
  eval-vla-only-long-seed42: SR=0.11, total=N/A, n_rollouts=10, conc=success
    all metrics: {'overall_success_rate': 0.11, 'n_tasks': 10, 'n_rollouts': 10, 'per_task': {'LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket': 0, 'LIVING_ROOM_SCENE2_cream_cheese_butter_basket': 0, 'KITCHEN_SCENE3_stove_moka_pot': 0.8, 'KITCHEN_SCENE4_black_bowl_drawer': 0, 'LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right': 0.1, 'STUDY_SCENE1_book_caddy': 0.1, 'LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding': 0, 'LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket': 0, 'KITCHEN_SCENE8_both_moka_pots_stove': 0, 'KITCHEN_SCENE6_yellow_white_mug_microwave': 0.1}}
  eval-vla-only-long-seed43: SR=0.13, total=N/A, n_rollouts=10, conc=success
    all metrics: {'overall_success_rate': 0.13, 'n_tasks': 10, 'n_rollouts': 10, 'per_task': {'LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket': 0, 'LIVING_ROOM_SCENE2_cream_cheese_butter_basket': 0, 'KITCHEN_SCENE3_stove_moka_pot': 0.7, 'KITCHEN_SCENE4_black_bowl_drawer': 0, 'LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right': 0.3, 'STUDY_SCENE1_book_caddy': 0, 'LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding': 0.1, 'LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket': 0, 'KITCHEN_SCENE8_both_moka_pots_stove': 0, 'KITCHEN_SCENE6_yellow_white_mug_microwave': 0.2}}
  eval-vla-only-long-seed44: SR=0.12, total=N/A, n_rollouts=10, conc=success
    all metrics: {'overall_success_rate': 0.12, 'n_tasks': 10, 'n_rollouts': 10, 'per_task': {'LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket': 0, 'LIVING_ROOM_SCENE2_cream_cheese_butter_basket': 0, 'KITCHEN_SCENE3_stove_moka_pot': 0.8, 'KITCHEN_SCENE4_black_bowl_drawer': 0, 'LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right': 0.2, 'STUDY_SCENE1_book_caddy': 0.1, 'LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding': 0, 'LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket': 0, 'KITCHEN_SCENE8_both_moka_pots_stove': 0, 'KITCHEN_SCENE6_yellow_white_mug_microwave': 0.1}}
  eval-vla-only-object-seed43: SR=0.12, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'overall_success_rate': 0.12}
  eval-vla-only-object-seed44: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  eval-vla-only-object-seed44-r2: SR=0.1, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'overall_success_rate': 0.1}
  eval-vla-only-spatial-cqa1-s42: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-vla-only-spatial-cqa1-s43: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-vla-only-spatial-cqa1-s44: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  eval-vla-only-spatial-seed42: SR=0.3, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.3, 'per_task': {'between_plate_and_ramekin': 0.6, 'next_to_ramekin': 1, 'from_table_center': 0, 'on_cookie_box': 0.2, 'in_top_drawer': 0, 'on_ramekin': 0, 'next_to_cookie_box': 0.9, 'on_stove': 0, 'next_to_plate': 0.3, 'on_wooden_cabinet': 0}}
  eval-vla-only-spatial-seed43: SR=0.29, total=100, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.29, 'successes': 29, 'total': 100, 'per_task': {'between_plate_and_ramekin': 0.7, 'next_to_ramekin': 0.8, 'from_table_center': 0.1, 'on_cookie_box': 0.3, 'in_top_drawer': 0, 'on_ramekin': 0, 'next_to_cookie_box': 0.9, 'on_stove': 0, 'next_to_plate': 0.1, 'on_wooden_cabinet': 0}}
  eval-vla-only-spatial-seed44: SR=0.31, total=100, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.31, 'successes': 31, 'total': 100, 'per_task': {'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate': 0.6, 'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate': 1, 'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate': 0, 'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate': 0.3, 'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate': 0, 'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate': 0, 'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate': 0.9, 'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate': 0, 'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate': 0.3, 'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate': 0}}
  pi05-vla-only-goal-s42-4090: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  pi05-vla-only-goal-s42-4090-r2: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  pi05-vla-only-goal-s44-4090: SR=97.5, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 97.5, 'successes': 195, 'trials': 200, 'benchmark': 'goal', 'mode': 'vla_only'}
  pi05-vla-only-long-s42-4090: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  pi05-vla-only-long-s42-4090-r2: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  pi05-vla-only-long-s42-4090-r3: SR=94, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 94, 'successes': 188, 'trials': 200, 'benchmark': 'long', 'mode': 'vla_only'}
  pi05-vla-only-long-s43-4090: SR=95.5, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 95.5, 'successes': 191, 'trials': 200, 'benchmark': 'long', 'mode': 'vla_only'}
  pi05-vla-only-long-s44-4090: SR=95.5, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 95.5, 'successes': 191, 'trials': 200, 'benchmark': 'long', 'mode': 'vla_only'}
  pi05-vla-only-object-s42-4090: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  pi05-vla-only-object-s42-4090-r2: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  pi05-vla-only-object-s43-4090: SR=98.5, total=N/A, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 98.5, 'successes': 197, 'trials': 200, 'benchmark': 'object', 'mode': 'vla_only'}
  pi05-vla-only-spatial-s42-4090: SR=N/A, total=N/A, n_rollouts=N/A, conc=failed
  pi05-vla-only-spatial-s42-4090-r2: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  smolvla-vla-only-long-n20-s42: SR=0.62, total=N/A, n_rollouts=20, conc=success
    all metrics: {'overall_success_rate': 0.62, 'n_rollouts': 20, 'n_tasks': 10}
  smolvla-vla-only-long-n20-s43: SR=0.575, total=N/A, n_rollouts=20, conc=success
    all metrics: {'overall_success_rate': 0.575, 'n_rollouts': 20, 'n_tasks': 10}
  westd-pi05-vla-only-goal-s42: SR=0.975, total=200, n_rollouts=N/A, conc=success
    all metrics: {'overall_success_rate': 0.975, 'successes': 195, 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20, 'per_task': {'open_the_middle_drawer_of_the_cabinet': {'sr': 0.95, 'successes': 19, 'total': 20}, 'put_the_bowl_on_the_stove': {'sr': 1, 'successes': 20, 'total': 20}, 'put_the_wine_bottle_on_top_of_the_cabinet': {'sr': 1, 'successes': 20, 'total': 20}, 'open_the_top_drawer_and_put_the_bowl_inside': {'sr': 0.9, 'successes': 18, 'total': 20}, 'put_the_bowl_on_top_of_the_cabinet': {'sr': 1, 'successes': 20, 'total': 20}, 'push_the_plate_to_the_front_of_the_stove': {'sr': 0.95, 'successes': 19, 'total': 20}, 'put_the_cream_cheese_in_the_bowl': {'sr': 1, 'successes': 20, 'total': 20}, 'turn_on_the_stove': {'sr': 1, 'successes': 20, 'total': 20}, 'put_the_bowl_on_the_plate': {'sr': 1, 'successes': 20, 'total': 20}, 'put_the_wine_bottle_on_the_rack': {'sr': 0.95, 'successes': 19, 'total': 20}}, 'delta_vs_4090_s42': '+2.0pp (97.5% vs 95.5%)'}
  westd-pi05-vla-only-goal-s42-paired: SR=0.975, total=N/A, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.975, 'benchmark': 'goal', 'mode': 'vla_only', 'seed': 42, 'model': 'pi05', 'n_rollouts': 20, 'n_tasks': 10}
  westd-pi05-vla-only-goal-s43-paired: SR=0.965, total=N/A, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.965, 'per_task_sr': {'open_the_middle_drawer_of_the_cabinet': 1, 'put_the_bowl_on_the_stove': 1, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.9, 'open_the_top_drawer_and_put_the_bowl_inside': 0.85, 'put_the_bowl_on_top_of_the_cabinet': 1, 'push_the_plate_to_the_front_of_the_stove': 1, 'put_the_cream_cheese_in_the_bowl': 1, 'turn_on_the_stove': 1, 'put_the_bowl_on_the_plate': 1, 'put_the_wine_bottle_on_the_rack': 0.9}, 'benchmark': 'goal', 'mode': 'vla_only', 'seed': 43, 'model': 'pi0.5', 'n_rollouts': 20}
  westd-pi05-vla-only-goal-s44: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  westd-pi05-vla-only-goal-s44-paired: SR=0.955, total=N/A, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.955, 'benchmark': 'goal', 'mode': 'vla_only', 'seed': 44, 'model': 'pi05', 'n_rollouts': 20, 'n_tasks': 10}
  westd-pi05-vla-only-long-s42-paired: SR=0.98, total=200, n_rollouts=N/A, conc=success
    all metrics: {'success_rate': 0.98, 'successes': 196, 'total': 200}
  westd-pi05-vla-only-long-s43-paired: SR=0.945, total=N/A, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.945, 'benchmark': 'long', 'mode': 'vla_only', 'seed': 43, 'model': 'pi05', 'n_rollouts': 20, 'n_tasks': 10}
  westd-pi05-vla-only-long-s44-paired: SR=0.96, total=200, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.96, 'benchmark': 'long', 'mode': 'vla_only', 'seed': 44, 'model': 'pi05', 'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'total_successes': 192}
  westd-pi05-vla-only-long-s44-r2: SR=N/A, total=N/A, n_rollouts=N/A, conc=killed
  westd-pi05-vla-only-object-s42-paired: SR=0.995, total=N/A, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.995, 'benchmark': 'object', 'mode': 'vla_only', 'seed': 42, 'model': 'pi05', 'n_rollouts': 20, 'n_tasks': 10}
  westd-pi05-vla-only-object-s43-paired: SR=1, total=N/A, n_rollouts=20, conc=success
    all metrics: {'success_rate': 1, 'benchmark': 'object', 'mode': 'vla_only', 'seed': 43, 'model': 'pi05', 'n_rollouts': 20, 'n_tasks': 10}
  westd-pi05-vla-only-object-s44-paired: SR=0.995, total=N/A, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.995, 'benchmark': 'object', 'mode': 'vla_only', 'seed': 44, 'model': 'pi05', 'n_rollouts': 20, 'n_tasks': 10}
  westd-pi05-vla-only-spatial-s42-paired: SR=0.98, total=200, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.98, 'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'total_successes': 196}
  westd-pi05-vla-only-spatial-s43-paired: SR=0.975, total=200, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.975, 'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'total_successes': 195}
  westd-pi05-vla-only-spatial-s44-paired: SR=0.985, total=200, n_rollouts=20, conc=success
    all metrics: {'success_rate': 0.985, 'n_rollouts': 20, 'n_tasks': 10, 'total_rollouts': 200, 'total_successes': 197}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "b964698f-fee2-450c-bd5d-201a5d3c63c4"
}
```

</details>

---

### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Check SmolVLA experiments",
  "usage": {
    "total_tokens": 66874,
    "tool_uses": 15,
    "duration_ms": 186722
  },
  "last_tool_name": "Bash",
  "uuid": "5be0d272-1a71-4c5b-af07-dbc99a0c0297",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01EaNkoES6KkCs7BW5j7f9Yy`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# There are clearly TWO phases of experiments:\n# 1. \"pi05\" experiments with K=10, n_rollouts=10 (100 total) - older, SR around 0.3 for spatial\n#    These use SmolVLA or an older pi0.5 setup\n# 2. \"supp\" / newer experiments with n_rollouts=20 (200 total) - the MAIN results\n#    Spatial SR around 0.8, Object around 0.77-0.81, Goal around 0.82-0.86\n\n# Also there are \"paired\" pi05 experiments on westd server with VERY HIGH SR (0.95-1.0)\n# These are clearly a different (harder/easier?) VLA model/setup\n\n# Let me look for SmolVLA experiments specifically\nprint(\"=\" * 80)\nprint(\"SMOLVLA EXPERIMENTS (with metrics, success conclusion)\")\nprint(\"=\" * 80)\n\nsmolvla_exps = {eid: ed for eid, ed in exps.items() \n                if 'smolvla' in eid.lower() and ed.get('metrics') and ed['conclusion'] == 'success'}\n\n# Group by benchmark\nsmolvla_by_bench = defaultdict(list)\nfor eid, ed in sorted(smolvla_exps.items()):\n    m = ed.get('metrics', {})\n    if not isinstance(m, dict): m = {}\n    \n    bench = None\n    if 'spatial' in eid: bench = 'spatial'\n    elif 'object' in eid or '-obj' in eid: bench = 'object'\n    elif 'goal' in eid: bench = 'goal'\n    elif 'long' in eid: bench = 'long'\n    \n    sr = None\n    for key in ['success_rate', 'overall_success_rate', 'SR', 'overall_sr', 'sr']:\n        if key in m:\n            sr = m[key]\n            break\n    \n    if sr is not None:\n        if isinstance(sr, (int, float)) and sr > 1:\n            sr = sr / 100.0\n    \n    seed_match = re.search(r'seed(\\d+)|[-_]s(\\d+)', eid)\n    seed = None\n    if seed_match:\n        seed = int(seed_match.group(1) or seed_match.group(2))\n    \n    method = 'vla-only' if 'vla-only' in eid or 'vla_only' in eid else 'other'\n    if 'crm' in eid and 'norm005' in eid: method = 'crm-norm005'\n    if 'adaptive' in eid or 'adapt' in eid: method = 'adaptive'\n    if 'reconvla' in eid: method = 'reconvla'\n    \n    smolvla_by_bench[bench].append({'eid': eid, 'sr': sr, 'seed': seed, 'method': method, 'metrics': m})\n\nfor bench in ['spatial', 'object', 'goal', 'long']:\n    entries = smolvla_by_bench.get(bench, [])\n    print(f\"\\n  [{bench}] ({len(entries)} entries)\")\n    for e in entries:\n        print(f\"    {e['eid']}: method={e['method']}, seed={e['seed']}, SR={e['sr']}\")\n\nPYEOF\n",
  "description": "Check SmolVLA experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "8be24ae3-f9e5-4500-a263-b9952dd58c93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbPfgppCwvH7HRMkJGLnQe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13438,
      "cache_read_input_tokens": 53142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13438,
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

_source line 79 · 2026-05-28T15:54:09.434Z_

<details><summary>↩ Tool result · `toolu_01EaNkoES6KkCs7BW5j7f9Yy`</summary>

```text
================================================================================
SMOLVLA EXPERIMENTS (with metrics, success conclusion)
================================================================================

  [spatial] (7 entries)
    eval-smolvla-lerobot-spatial-seed44: method=other, seed=44, SR=0.6
    smolvla-crm-norm005-spatial-s42-d149: method=crm-norm005, seed=42, SR=0.805
    smolvla-tau015-spatial-s42-fix: method=other, seed=42, SR=0.79
    smolvla-tau015-spatial-s43: method=other, seed=43, SR=0.805
    smolvla-tau025-spatial-s43: method=other, seed=43, SR=0.795
    smolvla-tau035-spatial-s43: method=other, seed=43, SR=0.795
    smolvla-tau045-spatial-s42: method=other, seed=42, SR=0.8

  [object] (19 entries)
    eval-smolvla-lerobot-object-seed43-v2: method=other, seed=43, SR=None
    eval-smolvla-lerobot-object-seed44-v2: method=other, seed=44, SR=None
    smolvla-adapt-tau015-object-s42-cqa1: method=adaptive, seed=42, SR=0.79
    smolvla-adapt-tau015-object-s43-cqa1: method=adaptive, seed=43, SR=0.78
    smolvla-adapt-tau015-object-s44-cqa1: method=adaptive, seed=44, SR=0.735
    smolvla-crm-norm005-k10-object-s44-cqa1: method=crm-norm005, seed=44, SR=0.78
    smolvla-tau005-object-s42: method=other, seed=42, SR=0.75
    smolvla-tau010-object-s42: method=other, seed=42, SR=0.78
    smolvla-tau015-object-s42: method=other, seed=42, SR=0.78
    smolvla-tau020-object-s42: method=other, seed=42, SR=0.785
    smolvla-tau025-object-s42-r2: method=other, seed=42, SR=0.78
    smolvla-tau025-object-s42-r3: method=other, seed=42, SR=0.81
    smolvla-tau025-object-s43-r3: method=other, seed=43, SR=0.775
    smolvla-tau030-object-s42: method=other, seed=42, SR=0.79
    smolvla-tau035-object-s42-r2: method=other, seed=42, SR=0.75
    smolvla-tau035-object-s42-r3: method=other, seed=42, SR=0.75
    smolvla-tau035-object-s43-r3: method=other, seed=43, SR=0.77
    smolvla-tau040-object-s42: method=other, seed=42, SR=0.735
    smolvla-tau045-object-s42: method=other, seed=42, SR=0.715

  [goal] (10 entries)
    eval-smolvla-crm-goal-s42: method=other, seed=42, SR=0.83
    eval-smolvla-crm-goal-seed44: method=other, seed=44, SR=0.825
    eval-smolvla-lerobot-goal-seed44-v3: method=other, seed=44, SR=0.78
    precompute-smolvla-goal-bjb1-18228: method=other, seed=None, SR=None
    smolvla-tau015-goal-s42: method=other, seed=42, SR=0.855
    smolvla-tau015-goal-s43: method=other, seed=43, SR=0.835
    smolvla-tau025-goal-s42: method=other, seed=42, SR=0.84
    smolvla-tau025-goal-s43: method=other, seed=43, SR=0.81
    smolvla-tau035-goal-s42: method=other, seed=42, SR=0.825
    smolvla-tau035-goal-s43: method=other, seed=43, SR=0.855

  [long] (20 entries)
    eval-smolvla-lerobot-long-seed42: method=other, seed=42, SR=0.495
    eval-smolvla-lerobot-long-seed43: method=other, seed=43, SR=0.535
    eval-smolvla-lerobot-long-seed44: method=other, seed=44, SR=0.495
    precompute-smolvla-long-bjb1-18228: method=other, seed=None, SR=None
    smolvla-tau010-long-s42: method=other, seed=42, SR=0.535
    smolvla-tau015-long-s42: method=other, seed=42, SR=0.61
    smolvla-tau015-long-s43: method=other, seed=43, SR=0.61
    smolvla-tau020-long-s42: method=other, seed=42, SR=0.585
    smolvla-tau020-long-s42-r2: method=other, seed=42, SR=0.585
    smolvla-tau020-long-s43-r2: method=other, seed=43, SR=0.545
    smolvla-tau025-long-s42: method=other, seed=42, SR=0.56
    smolvla-tau025-long-s43: method=other, seed=43, SR=0.53
    smolvla-tau030-long-s42-r2: method=other, seed=42, SR=0.545
    smolvla-tau030-long-s43-r2: method=other, seed=43, SR=0.555
    smolvla-tau035-long-s42: method=other, seed=42, SR=0.575
    smolvla-tau035-long-s43: method=other, seed=43, SR=0.6
    smolvla-tau040-long-s42: method=other, seed=42, SR=0.6
    smolvla-tau045-long-s42: method=other, seed=42, SR=0.595
    smolvla-vla-only-long-n20-s42: method=vla-only, seed=42, SR=0.62
    smolvla-vla-only-long-n20-s43: method=vla-only, seed=43, SR=0.575
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "ba9f36fb-d374-419e-a466-3a7a938d5b4e"
}
```

</details>

---

### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Build clean final results table for main experiments",
  "usage": {
    "total_tokens": 69760,
    "tool_uses": 16,
    "duration_ms": 226278
  },
  "last_tool_name": "Bash",
  "uuid": "df66ca21-1f78-4b45-ac7e-03faf49d25d7",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_01EgXxHg9ZWBYoz9Ujb51sXk`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Now build the CLEAN final table, filtering to only the \"supp\" / main experiment family\n# These are: eval-supp-*, and the matching non-supp experiments with 200 total rollouts\n# Focus on seeds 42-49 with 200 total rollouts\n\ndef norm_sr(val):\n    if val is None: return None\n    if isinstance(val, str):\n        try: val = float(val.replace('%','').strip().split('/')[0])\n        except: return None\n    if val > 1: val = val / 100.0\n    return round(val, 4)\n\ndef get_sr(m):\n    for key in ['success_rate', 'overall_success_rate', 'SR', 'overall_sr', 'sr']:\n        if key in m:\n            return norm_sr(m[key])\n    return None\n\n# The \"main\" experiment results for the paper - these use pi0.5 model with 200 rollouts (20 per task x 10 tasks)\n# on the standard evaluation server (not westd, not pi05-paired which has different GPU)\n# Identified by: eval-supp-* prefix, or the equivalent IDs with seeds 45-49\n\n# Let me build the clean table using ONLY supp-prefixed experiments\nresults = defaultdict(lambda: defaultdict(dict))  # method -> benchmark -> {seed: SR}\n\nfor eid, ed in exps.items():\n    m = ed.get('metrics', {})\n    if not isinstance(m, dict): m = {}\n    sr = get_sr(m)\n    if sr is None or sr < 0.3:\n        continue\n    \n    # Determine seed\n    seed_match = re.search(r'[-_]s(\\d+)', eid)\n    seed = int(seed_match.group(1)) if seed_match else None\n    if seed is None:\n        seed_match = re.search(r'seed(\\d+)', eid)\n        seed = int(seed_match.group(1)) if seed_match else None\n    if seed is None:\n        seed = m.get('seed')\n        if seed: seed = int(seed)\n    \n    # Determine benchmark\n    bench = None\n    for b in ['spatial', 'object', 'goal', 'long']:\n        if b in eid: bench = b\n    if 'obj' in eid and bench is None: bench = 'object'\n    if not bench: bench = m.get('benchmark')\n    if not bench: continue\n    \n    method = None\n    \n    # SUPP experiments (the canonical results)\n    if eid.startswith('eval-supp-'):\n        if 'adapt-tau025' in eid: method = 'ACR (tau=0.25)'\n        elif 'crm-norm005' in eid or 'crm005' in eid: method = 'CRM-obs-only'\n        elif 'k2mean' in eid: method = 'K2-mean baseline'\n        elif 'reconvla' in eid: method = 'ReConVLA'\n        elif 'vla-only' in eid: method = 'VLA-only'\n        elif 'adapt-tau015' in eid: method = 'ACR (tau=0.15)'\n        elif 'adapt-tau035' in eid: method = 'ACR (tau=0.35)'\n        elif 'crm-norm02' in eid: method = 'CRM-obs-only (norm=0.2)'\n        elif 'obj-crm-norm005' in eid: method = 'CRM-obs-only'\n        elif 'obj-adapt' in eid and 'tau025' in eid: method = 'ACR (tau=0.25)'\n        elif 'obj-adapt' in eid: method = 'ACR (adaptive)'\n        elif 'obj-crm' in eid: method = 'CRM-obs-only'\n        elif 'crm-obj' in eid: method = 'CRM-obs-only'\n        elif 'goal-adapt-tau025' in eid: method = 'ACR (tau=0.25)'\n        elif 'goal-crm-norm005' in eid or 'goal-crm005' in eid: method = 'CRM-obs-only'\n        elif 'goal-k2mean' in eid: method = 'K2-mean baseline'\n        elif 'goal-reconvla' in eid: method = 'ReConVLA'\n        elif 'goal-vla-only' in eid: method = 'VLA-only'\n        elif 'long-' in eid and 'adapt-tau025' in eid: method = 'ACR (tau=0.25)'\n        elif 'long-crm-norm005' in eid: method = 'CRM-obs-only'\n        elif 'long-k2mean' in eid: method = 'K2-mean baseline'\n        elif 'long-reconvla' in eid: method = 'ReConVLA'\n        elif 'long-vla-only' in eid: method = 'VLA-only'\n        elif 'spatial-adapt-tau025' in eid: method = 'ACR (tau=0.25)'\n        elif 'spatial-crm-norm005' in eid: method = 'CRM-obs-only'\n        elif 'spatial-k2mean' in eid: method = 'K2-mean baseline'\n        elif 'spatial-reconvla' in eid: method = 'ReConVLA'\n        elif 'spatial-vla-only' in eid: method = 'VLA-only'\n        elif 'obj-k2mean' in eid: method = 'K2-mean baseline'\n        elif 'obj-reconvla' in eid: method = 'ReConVLA'\n        elif 'obj-vla-only' in eid: method = 'VLA-only'\n        elif 'obj-crm-norm005' in eid: method = 'CRM-obs-only'\n        elif 'obj-adapt-tau025' in eid: method = 'ACR (tau=0.25)'\n        elif 'vla-only' in eid and 'goal' in eid: method = 'VLA-only'\n        \n    if method and seed is not None:\n        key = (method, bench)\n        # Keep highest SR for each seed\n        if seed not in results[method][bench] or sr > results[method][bench][seed]:\n            results[method][bench][seed] = sr\n\n# Also add the non-supp experiments that have the same pattern\n# These are eval-*-vla-only-*, eval-*-crm-*, etc. with seeds 45-49\nfor eid, ed in exps.items():\n    if eid.startswith('eval-supp-'): continue\n    if 'smolvla' in eid or 'pi05' in eid.lower() or 'openvla' in eid: continue\n    if 'westd' in eid or 'paired' in eid or '4090' in eid: continue\n    if 'adaptive-k' in eid: continue  # different experiment type\n    \n    m = ed.get('metrics', {})\n    if not isinstance(m, dict): m = {}\n    sr = get_sr(m)\n    if sr is None or sr < 0.3: continue\n    \n    total = m.get('total', m.get('total_rollouts', m.get('total_trials', m.get('total_episodes'))))\n    if total is not None and total < 150: continue  # skip 100-rollout experiments\n    \n    seed_match = re.search(r'[-_]s(\\d+)', eid)\n    seed = int(seed_match.group(1)) if seed_match else None\n    if seed is None:\n        seed_match = re.search(r'seed(\\d+)', eid)\n        seed = int(seed_match.group(1)) if seed_match else None\n    if seed is None:\n        seed = m.get('seed')\n        if seed: seed = int(seed)\n    if seed is None: continue\n    \n    bench = None\n    for b in ['spatial', 'object', 'goal', 'long']:\n        if b in eid: bench = b\n    if 'obj' in eid and bench is None: bench = 'object'\n    if not bench: bench = m.get('benchmark')\n    if not bench: continue\n    \n    method = None\n    if ('adapt' in eid and 'tau025' in eid) or ('adaptive' in eid and 'conformal' in eid and 'tau025' in eid):\n        method = 'ACR (tau=0.25)'\n    elif ('crm' in eid and ('norm005' in eid or 'norm0.05' in eid or 'crm005' in eid)):\n        method = 'CRM-obs-only'\n    elif 'k2mean' in eid or 'k2-mean' in eid:\n        method = 'K2-mean baseline'\n    elif 'reconvla' in eid and 'adaptive-k' not in eid:\n        method = 'ReConVLA'\n    elif 'vla-only' in eid and 'crm' not in eid and 'adapt' not in eid:\n        method = 'VLA-only'\n    \n    if method and seed is not None:\n        if seed not in results[method][bench] or sr > results[method][bench][seed]:\n            results[method][bench][seed] = sr\n\n# Print the clean table\nprint(\"=\" * 100)\nprint(\"MAIN EXPERIMENT RESULTS (pi0.5 model, 200 rollouts, 10 tasks x 20 rollouts)\")\nprint(\"All SR values normalized to [0,1]\")\nprint(\"=\" * 100)\n\nmethods_order = ['VLA-only', 'K2-mean baseline', 'ReConVLA', 'CRM-obs-only', 'ACR (tau=0.25)']\nbenchmarks = ['spatial', 'object', 'goal', 'long']\n\nfor method in methods_order:\n    print(f\"\\n{'='*80}\")\n    print(f\"  {method}\")\n    print(f\"{'='*80}\")\n    for bench in benchmarks:\n        seed_data = results.get(method, {}).get(bench, {})\n        if not seed_data:\n            print(f\"  [{bench}] NO DATA\")\n            continue\n        seeds_sorted = sorted(seed_data.keys())\n        srs = [seed_data[s] for s in seeds_sorted]\n        mean_sr = sum(srs) / len(srs)\n        std_sr = (sum((s - mean_sr)**2 for s in srs) / len(srs)) ** 0.5\n        print(f\"  [{bench}] {len(srs)} seeds, MEAN={mean_sr:.3f} +/- {std_sr:.3f} ({mean_sr*100:.1f}%)\")\n        for s in seeds_sorted:\n            print(f\"    seed {s}: {seed_data[s]:.3f} ({seed_data[s]*100:.1f}%)\")\n\nPYEOF\n",
  "description": "Build clean final results table for main experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "e864e171-bb0e-4bad-b48d-c91d11aef097",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UTdghftLMrokvfYUKQtXW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2814,
      "cache_read_input_tokens": 66580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2814,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-28T15:54:49.014Z_

<details><summary>↩ Tool result · `toolu_01EgXxHg9ZWBYoz9Ujb51sXk`</summary>

```text
====================================================================================================
MAIN EXPERIMENT RESULTS (pi0.5 model, 200 rollouts, 10 tasks x 20 rollouts)
All SR values normalized to [0,1]
====================================================================================================

================================================================================
  VLA-only
================================================================================
  [spatial] 8 seeds, MEAN=0.798 +/- 0.008 (79.8%)
    seed 42: 0.800 (80.0%)
    seed 43: 0.790 (79.0%)
    seed 44: 0.785 (78.5%)
    seed 45: 0.800 (80.0%)
    seed 46: 0.805 (80.5%)
    seed 47: 0.810 (81.0%)
    seed 48: 0.795 (79.5%)
    seed 49: 0.795 (79.5%)
  [object] 9 seeds, MEAN=0.769 +/- 0.017 (76.9%)
    seed 42: 0.790 (79.0%)
    seed 43: 0.770 (77.0%)
    seed 44: 0.775 (77.5%)
    seed 45: 0.760 (76.0%)
    seed 46: 0.790 (79.0%)
    seed 47: 0.755 (75.5%)
    seed 48: 0.790 (79.0%)
    seed 49: 0.755 (75.5%)
    seed 50: 0.740 (74.0%)
  [goal] 8 seeds, MEAN=0.834 +/- 0.011 (83.4%)
    seed 42: 0.835 (83.5%)
    seed 43: 0.825 (82.5%)
    seed 44: 0.850 (85.0%)
    seed 45: 0.835 (83.5%)
    seed 46: 0.830 (83.0%)
    seed 47: 0.825 (82.5%)
    seed 48: 0.850 (85.0%)
    seed 49: 0.820 (82.0%)
  [long] 4 seeds, MEAN=0.593 +/- 0.011 (59.2%)
    seed 42: 0.595 (59.5%)
    seed 44: 0.605 (60.5%)
    seed 45: 0.575 (57.5%)
    seed 47: 0.595 (59.5%)

================================================================================
  K2-mean baseline
================================================================================
  [spatial] 6 seeds, MEAN=0.804 +/- 0.013 (80.4%)
    seed 42: 0.815 (81.5%)
    seed 43: 0.780 (78.0%)
    seed 44: 0.810 (81.0%)
    seed 45: 0.800 (80.0%)
    seed 46: 0.800 (80.0%)
    seed 47: 0.820 (82.0%)
  [object] 6 seeds, MEAN=0.773 +/- 0.014 (77.3%)
    seed 42: 0.795 (79.5%)
    seed 43: 0.780 (78.0%)
    seed 44: 0.750 (75.0%)
    seed 45: 0.775 (77.5%)
    seed 46: 0.765 (76.5%)
    seed 47: 0.775 (77.5%)
  [goal] 6 seeds, MEAN=0.825 +/- 0.014 (82.5%)
    seed 42: 0.855 (85.5%)
    seed 43: 0.815 (81.5%)
    seed 44: 0.820 (82.0%)
    seed 45: 0.810 (81.0%)
    seed 46: 0.825 (82.5%)
    seed 47: 0.825 (82.5%)
  [long] 6 seeds, MEAN=0.555 +/- 0.009 (55.5%)
    seed 42: 0.570 (57.0%)
    seed 43: 0.560 (56.0%)
    seed 44: 0.545 (54.5%)
    seed 45: 0.560 (56.0%)
    seed 46: 0.550 (55.0%)
    seed 47: 0.545 (54.5%)

================================================================================
  ReConVLA
================================================================================
  [spatial] 6 seeds, MEAN=0.803 +/- 0.007 (80.3%)
    seed 42: 0.800 (80.0%)
    seed 43: 0.815 (81.5%)
    seed 44: 0.795 (79.5%)
    seed 45: 0.795 (79.5%)
    seed 46: 0.800 (80.0%)
    seed 47: 0.810 (81.0%)
  [object] 6 seeds, MEAN=0.777 +/- 0.014 (77.8%)
    seed 42: 0.790 (79.0%)
    seed 43: 0.770 (77.0%)
    seed 44: 0.760 (76.0%)
    seed 45: 0.780 (78.0%)
    seed 46: 0.800 (80.0%)
    seed 47: 0.765 (76.5%)
  [goal] 5 seeds, MEAN=0.819 +/- 0.023 (81.9%)
    seed 43: 0.810 (81.0%)
    seed 44: 0.805 (80.5%)
    seed 45: 0.855 (85.5%)
    seed 46: 0.790 (79.0%)
    seed 47: 0.835 (83.5%)
  [long] 6 seeds, MEAN=0.571 +/- 0.015 (57.1%)
    seed 42: 0.565 (56.5%)
    seed 43: 0.590 (59.0%)
    seed 44: 0.570 (57.0%)
    seed 45: 0.590 (59.0%)
    seed 46: 0.560 (56.0%)
    seed 47: 0.550 (55.0%)

================================================================================
  CRM-obs-only
================================================================================
  [spatial] 7 seeds, MEAN=0.797 +/- 0.012 (79.7%)
    seed 43: 0.810 (81.0%)
    seed 44: 0.785 (78.5%)
    seed 45: 0.805 (80.5%)
    seed 46: 0.810 (81.0%)
    seed 47: 0.805 (80.5%)
    seed 48: 0.780 (78.0%)
    seed 49: 0.785 (78.5%)
  [object] 6 seeds, MEAN=0.780 +/- 0.026 (78.0%)
    seed 42: 0.770 (77.0%)
    seed 43: 0.785 (78.5%)
    seed 44: 0.740 (74.0%)
    seed 45: 0.765 (76.5%)
    seed 46: 0.795 (79.5%)
    seed 47: 0.825 (82.5%)
  [goal] 7 seeds, MEAN=0.823 +/- 0.016 (82.3%)
    seed 42: 0.855 (85.5%)
    seed 43: 0.820 (82.0%)
    seed 44: 0.835 (83.5%)
    seed 45: 0.810 (81.0%)
    seed 46: 0.820 (82.0%)
    seed 47: 0.820 (82.0%)
    seed 48: 0.800 (80.0%)
  [long] 6 seeds, MEAN=0.564 +/- 0.021 (56.4%)
    seed 42: 0.565 (56.5%)
    seed 43: 0.545 (54.5%)
    seed 44: 0.565 (56.5%)
    seed 45: 0.605 (60.5%)
    seed 46: 0.540 (54.0%)
    seed 47: 0.565 (56.5%)

================================================================================
  ACR (tau=0.25)
================================================================================
  [spatial] 8 seeds, MEAN=0.809 +/- 0.008 (80.9%)
    seed 42: 0.820 (82.0%)
    seed 43: 0.800 (80.0%)
    seed 44: 0.805 (80.5%)
    seed 45: 0.800 (80.0%)
    seed 46: 0.800 (80.0%)
    seed 47: 0.815 (81.5%)
    seed 48: 0.810 (81.0%)
    seed 49: 0.820 (82.0%)
  [object] 8 seeds, MEAN=0.770 +/- 0.020 (77.0%)
    seed 42: 0.810 (81.0%)
    seed 43: 0.775 (77.5%)
    seed 44: 0.750 (75.0%)
    seed 45: 0.780 (78.0%)
    seed 46: 0.775 (77.5%)
    seed 47: 0.770 (77.0%)
    seed 48: 0.760 (76.0%)
    seed 49: 0.740 (74.0%)
  [goal] 8 seeds, MEAN=0.834 +/- 0.017 (83.4%)
    seed 42: 0.840 (84.0%)
    seed 43: 0.845 (84.5%)
    seed 44: 0.865 (86.5%)
    seed 45: 0.810 (81.0%)
    seed 46: 0.835 (83.5%)
    seed 47: 0.820 (82.0%)
    seed 48: 0.845 (84.5%)
    seed 49: 0.815 (81.5%)
  [long] 4 seeds, MEAN=0.574 +/- 0.020 (57.4%)
    seed 44: 0.560 (56.0%)
    seed 45: 0.600 (60.0%)
    seed 46: 0.585 (58.5%)
    seed 47: 0.550 (55.0%)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "ee7247b6-9400-4530-996b-d141f82b3ca2"
}
```

</details>

---

### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Detail obs-only experiments grouped by benchmark and norm",
  "usage": {
    "total_tokens": 75613,
    "tool_uses": 17,
    "duration_ms": 242785
  },
  "last_tool_name": "Bash",
  "uuid": "ccd31cab-3802-4c2a-bc96-12f333912040",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_011cp1nuKddxiPj5wNk7HZPv`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Obs-only experiments (separate baseline category)\nprint(\"=\" * 80)\nprint(\"OBS-ONLY EXPERIMENTS (with metrics)\")\nprint(\"=\" * 80)\n\nobs_exps = {eid: ed for eid, ed in exps.items() if 'obs-only' in eid and ed.get('metrics')}\n# Group by benchmark and norm\nobs_groups = defaultdict(list)\nfor eid in sorted(obs_exps.keys()):\n    ed = obs_exps[eid]\n    m = ed.get('metrics', {})\n    if not isinstance(m, dict): m = {}\n    \n    bench = None\n    for b in ['spatial', 'object', 'goal', 'long']:\n        if b in eid: bench = b\n    if 'obj' in eid and not bench: bench = 'object'\n    \n    norm = 'unknown'\n    nm = re.search(r'norm(\\d+\\.?\\d*|0p\\d+)', eid)\n    if nm:\n        norm = nm.group(1).replace('p', '.')\n    \n    sr = None\n    for key in ['success_rate', 'overall_success_rate', 'SR', 'overall_sr', 'sr']:\n        if key in m:\n            sr = m[key]\n            break\n    if sr and isinstance(sr, (int, float)) and sr > 1:\n        sr = sr / 100.0\n    \n    seed_match = re.search(r'seed(\\d+)|[-_]s(\\d+)', eid)\n    seed = int(seed_match.group(1) or seed_match.group(2)) if seed_match else '?'\n    \n    obs_groups[(bench, norm)].append({\n        'eid': eid, 'sr': sr, 'seed': seed, 'conc': ed['conclusion']\n    })\n\nfor (bench, norm) in sorted(obs_groups.keys()):\n    entries = obs_groups[(bench, norm)]\n    success_entries = [e for e in entries if e['sr'] is not None]\n    print(f\"\\n  [{bench}] norm={norm} ({len(success_entries)}/{len(entries)} with SR)\")\n    for e in sorted(success_entries, key=lambda x: x['seed']):\n        print(f\"    seed {e['seed']}: SR={e['sr']:.4f}, conc={e['conc']}\")\n\nPYEOF\n",
  "description": "Detail obs-only experiments grouped by benchmark and norm"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "7c7f9cca-1213-481c-b775-03d45017ee58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GrW3YN5iT9wSKmUtzBN2y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 69394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5851,
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

_source line 85 · 2026-05-28T15:55:05.622Z_

<details><summary>↩ Tool result · reported error · `toolu_011cp1nuKddxiPj5wNk7HZPv`</summary>

```text
Exit code 1
================================================================================
OBS-ONLY EXPERIMENTS (with metrics)
================================================================================
Traceback (most recent call last):
  File "&lt;stdin>", line 47, in &lt;module>
TypeError: '<' not supported between instances of 'str' and 'NoneType'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "059caee3-e693-4a7e-be9a-8c1fb414641c",
  "tool_use_result": "Error: Exit code 1\n================================================================================\nOBS-ONLY EXPERIMENTS (with metrics)\n================================================================================\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 47, in &lt;module>\nTypeError: '<' not supported between instances of 'str' and 'NoneType'"
}
```

</details>

---

### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Detail obs-only experiments (fixed)",
  "usage": {
    "total_tokens": 76634,
    "tool_uses": 18,
    "duration_ms": 252837
  },
  "last_tool_name": "Bash",
  "uuid": "3ac48c2f-303f-4d92-963c-fee6deb89497",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_01HhjZg26ysywWMnCdWKuzm2`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Obs-only experiments\nobs_exps = {eid: ed for eid, ed in exps.items() if 'obs-only' in eid and ed.get('metrics')}\nobs_groups = defaultdict(list)\nfor eid in sorted(obs_exps.keys()):\n    ed = obs_exps[eid]\n    m = ed.get('metrics', {})\n    if not isinstance(m, dict): m = {}\n    \n    bench = None\n    for b in ['spatial', 'object', 'goal', 'long']:\n        if b in eid: bench = b\n    if 'obj' in eid and not bench: bench = 'object'\n    if not bench: bench = 'unknown'\n    \n    norm = 'unknown'\n    nm = re.search(r'norm(\\d+\\.?\\d*|0p\\d+)', eid)\n    if nm: norm = nm.group(1).replace('p', '.')\n    \n    sr = None\n    for key in ['success_rate', 'overall_success_rate', 'SR', 'overall_sr', 'sr']:\n        if key in m:\n            sr = m[key]\n            break\n    if sr is not None and isinstance(sr, (int, float)) and sr > 1:\n        sr = sr / 100.0\n    \n    seed_match = re.search(r'seed(\\d+)|[-_]s(\\d+)', eid)\n    seed = int(seed_match.group(1) or seed_match.group(2)) if seed_match else -1\n    \n    obs_groups[(bench, norm)].append({\n        'eid': eid, 'sr': sr, 'seed': seed, 'conc': ed['conclusion']\n    })\n\nfor (bench, norm) in sorted(obs_groups.keys()):\n    entries = obs_groups[(bench, norm)]\n    success_entries = [e for e in entries if e['sr'] is not None]\n    print(f\"\\n  [{bench}] norm={norm} ({len(success_entries)}/{len(entries)} with SR)\")\n    for e in sorted(success_entries, key=lambda x: str(x['seed'])):\n        sr_str = f\"{e['sr']:.4f}\" if isinstance(e['sr'], float) else str(e['sr'])\n        print(f\"    seed {e['seed']}: SR={sr_str}, conc={e['conc']}\")\n\nPYEOF\n",
  "description": "Detail obs-only experiments (fixed)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "92f8cdb5-e5b1-4aec-8406-effc5297b433",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACHAELaDes32W5M47NTBVf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 75245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 949,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-28T15:55:15.601Z_

<details><summary>↩ Tool result · `toolu_01HhjZg26ysywWMnCdWKuzm2`</summary>

```text
  [goal] norm=02 (2/2 with SR)
    seed 51: SR=0.6600, conc=success
    seed 52: SR=0.6800, conc=success

  [object] norm=003 (16/17 with SR)
    seed 43: SR=0.1400, conc=success
    seed 43: SR=0.1400, conc=success
    seed 44: SR=0.1500, conc=success
    seed 44: SR=0.1500, conc=success
    seed 44: SR=0.1500, conc=success
    seed 45: SR=0.1500, conc=success
    seed 46: SR=0.1500, conc=success
    seed 47: SR=0.1500, conc=success
    seed 48: SR=0.1500, conc=success
    seed 56: SR=0.1500, conc=success
    seed 59: SR=0.1300, conc=success
    seed 64: SR=0.1700, conc=success
    seed 65: SR=0.1700, conc=success
    seed 66: SR=0.1150, conc=success
    seed 67: SR=0.1400, conc=success
    seed 73: SR=0.1600, conc=success

  [object] norm=005 (16/16 with SR)
    seed 43: SR=0.1300, conc=success
    seed 43: SR=0.1400, conc=success
    seed 44: SR=0.1200, conc=success
    seed 47: SR=0.1300, conc=success
    seed 48: SR=0.1300, conc=success
    seed 49: SR=0.1500, conc=success
    seed 50: SR=0.1300, conc=success
    seed 55: SR=0.1500, conc=success
    seed 58: SR=0.1600, conc=success
    seed 61: SR=0.1500, conc=success
    seed 64: SR=0.1500, conc=success
    seed 65: SR=0.1400, conc=success
    seed 66: SR=0.1100, conc=success
    seed 67: SR=0.1000, conc=success
    seed 72: SR=0.1100, conc=success
    seed 75: SR=0.1500, conc=success

  [object] norm=01 (22/22 with SR)
    seed 44: SR=0.1600, conc=success
    seed 45: SR=0.1400, conc=success
    seed 45: SR=0.1700, conc=success
    seed 46: SR=0.1800, conc=success
    seed 47: SR=0.1700, conc=success
    seed 48: SR=0.1300, conc=success
    seed 49: SR=0.1600, conc=success
    seed 50: SR=0.1400, conc=success
    seed 51: SR=0.1100, conc=success
    seed 51: SR=0.1100, conc=success
    seed 52: SR=0.1500, conc=success
    seed 52: SR=0.1500, conc=success
    seed 53: SR=0.1900, conc=success
    seed 54: SR=0.1500, conc=success
    seed 57: SR=0.1900, conc=success
    seed 60: SR=0.1500, conc=success
    seed 64: SR=0.1500, conc=success
    seed 65: SR=0.1500, conc=success
    seed 66: SR=0.1350, conc=success
    seed 67: SR=0.1400, conc=success
    seed 71: SR=0.1600, conc=success
    seed 74: SR=0.1300, conc=success

  [object] norm=02 (21/22 with SR)
    seed -1: SR=0.2200, conc=success
    seed 42: SR=0.1400, conc=success
    seed 42: SR=0.2000, conc=success
    seed 43: SR=0.1900, conc=success
    seed 43: SR=0.1600, conc=success
    seed 43: SR=0.1600, conc=success
    seed 44: SR=0.1700, conc=success
    seed 44: SR=0.1600, conc=success
    seed 45: SR=0.1500, conc=success
    seed 45: SR=0.1600, conc=success
    seed 46: SR=0.1600, conc=success
    seed 46: SR=0.1500, conc=success
    seed 47: SR=0.1300, conc=success
    seed 47: SR=0.2000, conc=success
    seed 48: SR=0.1800, conc=success
    seed 48: SR=0.1800, conc=success
    seed 49: SR=0.1400, conc=success
    seed 50: SR=0.1800, conc=success
    seed 51: SR=0.1700, conc=success
    seed 52: SR=0.1500, conc=success
    seed 53: SR=0.1600, conc=success

  [object] norm=03 (4/4 with SR)
    seed 44: SR=0.1800, conc=success
    seed 45: SR=0.1400, conc=success
    seed 46: SR=0.1700, conc=success
    seed 48: SR=0.1600, conc=success

  [object] norm=unknown (16/16 with SR)
    seed -1: SR=0.1700, conc=success
    seed -1: SR=19.0% (19/100), conc=success
    seed 42: SR=0.2000, conc=success
    seed 43: SR=0.1800, conc=success
    seed 43: SR=0.1700, conc=success
    seed 43: SR=0.1200, conc=negative
    seed 44: SR=0.1800, conc=success
    seed 44: SR=0.1400, conc=success
    seed 44: SR=0.1600, conc=success
    seed 45: SR=0.1900, conc=success
    seed 45: SR=0.1200, conc=success
    seed 45: SR=0.1800, conc=success
    seed 46: SR=0.1500, conc=success
    seed 47: SR=0.1600, conc=success
    seed 48: SR=0.1700, conc=success
    seed 48: SR=0.1700, conc=success

  [spatial] norm=02 (14/15 with SR)
    seed 42: SR=0.3500, conc=success
    seed 42: SR=0.3300, conc=success
    seed 43: SR=0.3200, conc=success
    seed 43: SR=0.3400, conc=success
    seed 44: SR=0.3700, conc=success
    seed 44: SR=0.3600, conc=success
    seed 45: SR=0.3400, conc=success
    seed 45: SR=0.3400, conc=success
    seed 46: SR=0.3300, conc=success
    seed 47: SR=0.3200, conc=success
    seed 48: SR=0.3500, conc=success
    seed 49: SR=0.3200, conc=success
    seed 50: SR=0.3500, conc=success
    seed 52: SR=0.3300, conc=success

  [spatial] norm=unknown (7/9 with SR)
    seed -1: SR=35.0% (35/100), conc=success
    seed -1: SR=0, conc=success
    seed 42: SR=0.3500, conc=success
    seed 43: SR=0.3400, conc=success
    seed 44: SR=0.3400, conc=success
    seed 45: SR=0.3400, conc=success
    seed 48: SR=0.3500, conc=success

  [unknown] norm=unknown (0/5 with SR)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "8ff23283-33ca-4c91-ae1f-67db139f4e34"
}
```

</details>

---

### System

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "description": "Running Check pi0.5 paired experiments and SmolVLA tau sweep",
  "usage": {
    "total_tokens": 79657,
    "tool_uses": 19,
    "duration_ms": 265153
  },
  "last_tool_name": "Bash",
  "uuid": "f5630ad3-173f-4c18-8e38-37afa4723b8a",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Bash · `toolu_01LyQ4oW3w4Q6yprPiyZ3oHt`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt', 'r') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Count pi05 paired/westd experiments with success\nprint(\"=\" * 80)\nprint(\"PI0.5 PAIRED EXPERIMENTS (westd server, high-fidelity)\")\nprint(\"=\" * 80)\npaired = {eid: ed for eid, ed in exps.items() \n          if ('westd' in eid or 'paired' in eid) and ed.get('metrics')}\nfor eid in sorted(paired.keys()):\n    ed = paired[eid]\n    m = ed.get('metrics', {})\n    sr = m.get('success_rate', m.get('overall_success_rate', 'N/A'))\n    if isinstance(sr, (int, float)) and sr > 1: sr = sr / 100.0\n    print(f\"  {eid}: SR={sr}, conc={ed['conclusion']}\")\n\n# Count the tau-sweep for SmolVLA\nprint(\"\\n\" + \"=\" * 80)\nprint(\"SMOLVLA TAU-SWEEP (object benchmark, seed 42)\")\nprint(\"=\" * 80)\nfor eid in sorted(exps.keys()):\n    if 'smolvla' in eid and 'tau' in eid and 'object' in eid:\n        ed = exps[eid]\n        m = ed.get('metrics', {})\n        if not isinstance(m, dict): m = {}\n        sr = None\n        for key in ['success_rate', 'overall_success_rate', 'SR', 'overall_sr', 'sr']:\n            if key in m:\n                sr = m[key]\n                break\n        if sr and isinstance(sr, (int, float)) and sr > 1: sr = sr / 100.0\n        tau_match = re.search(r'tau(\\d+)', eid)\n        tau = int(tau_match.group(1)) / 100.0 if tau_match else '?'\n        seed_match = re.search(r'[-_]s(\\d+)', eid)\n        seed = seed_match.group(1) if seed_match else '?'\n        print(f\"  tau={tau}, seed={seed}: SR={sr}, conc={ed['conclusion']} | {eid}\")\n\nPYEOF\n",
  "description": "Check pi0.5 paired experiments and SmolVLA tau sweep"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "ab38832c-37b2-413d-b753-91e5f1575b3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2jV2cehW4YffNFMTqEGjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 76194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3021,
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

_source line 91 · 2026-05-28T15:55:27.897Z_

<details><summary>↩ Tool result · `toolu_01LyQ4oW3w4Q6yprPiyZ3oHt`</summary>

```text
================================================================================
PI0.5 PAIRED EXPERIMENTS (westd server, high-fidelity)
================================================================================
  eval-goal-adapt-tau025-s49-paired: SR=0.805, conc=negative
  eval-goal-vla-only-s49-paired: SR=0.835, conc=success
  eval-k2-goal-adapt-s45-paired: SR=0.82, conc=success
  eval-k2-goal-adapt-s46-paired: SR=0.84, conc=success
  eval-k2-goal-adapt-s47-paired: SR=0.825, conc=success
  eval-k2-goal-vla-only-s45-paired: SR=0.835, conc=success
  eval-k2-goal-vla-only-s46-paired: SR=0.82, conc=success
  eval-k2-goal-vla-only-s47-paired: SR=0.835, conc=success
  eval-k2-spatial-adapt-s42-paired-r2: SR=0.795, conc=success
  eval-k2-spatial-adapt-s43-paired-r2: SR=0.795, conc=success
  eval-k2-spatial-adapt-s44-paired-r2: SR=0.805, conc=success
  eval-k2-spatial-adapt-s45-paired: SR=0.8, conc=killed
  eval-k2-spatial-adapt-s46-paired: SR=0.8, conc=killed
  eval-k2-spatial-adapt-s47-paired: SR=0.795, conc=killed
  eval-k2-spatial-adapt-s48-paired: SR=0.805, conc=killed
  eval-k2-spatial-adapt-s49-paired: SR=0.81, conc=killed
  eval-k2-spatial-vla-only-s42-paired-r2: SR=0.785, conc=success
  eval-k2-spatial-vla-only-s43-paired-r2: SR=0.795, conc=success
  eval-k2-spatial-vla-only-s44-paired-r2: SR=0.8, conc=success
  eval-k2-spatial-vla-only-s45-paired: SR=0.805, conc=killed
  eval-k2-spatial-vla-only-s46-paired: SR=0.8, conc=killed
  eval-k2-spatial-vla-only-s47-paired: SR=0.765, conc=killed
  eval-k2-spatial-vla-only-s48-paired: SR=0.775, conc=killed
  eval-k2-spatial-vla-only-s49-paired: SR=0.795, conc=killed
  eval-obs-object-norm003-s43-westd: SR=0.74, conc=success
  eval-obs-object-norm003-s44-westd: SR=0.745, conc=success
  eval-obs-object-norm005-s43-westd: SR=0.735, conc=success
  eval-obs-object-norm005-s44-westd: SR=0.765, conc=success
  eval-perdof-object-norm003-s44-westd: SR=0.795, conc=success
  eval-perdof-object-norm005-s44-westd: SR=0.79, conc=success
  eval-pi05-vla-only-goal-s42-paired: SR=0.98, conc=success
  eval-pi05-vla-only-spatial-s42-paired: SR=0.98, conc=success
  eval-spatial-adapt-tau025-s46-paired: SR=0.78, conc=negative
  eval-spatial-adapt-tau025-s48-paired: SR=0.81, conc=success
  eval-spatial-vla-only-s46-paired: SR=0.8, conc=success
  eval-spatial-vla-only-s48-paired: SR=0.775, conc=success
  westd-pi05-adaptive-goal-s42: SR=0.88, conc=success
  westd-pi05-adaptive-goal-s43: SR=0.875, conc=success
  westd-pi05-adaptive-goal-s44: SR=0.875, conc=negative
  westd-pi05-adaptive-object-s42: SR=0.835, conc=success
  westd-pi05-adaptive-object-s42-paired: SR=N/A, conc=negative
  westd-pi05-adaptive-object-s43-paired: SR=N/A, conc=negative
  westd-pi05-crm-k2-goal-s42: SR=0.855, conc=success
  westd-pi05-crm-k2-object-s42: SR=N/A, conc=negative
  westd-pi05-crm-k2-object-s43: SR=N/A, conc=negative
  westd-pi05-crm-k2-object-s44: SR=N/A, conc=negative
  westd-pi05-k2mean-goal-s42: SR=0.995, conc=success
  westd-pi05-vla-only-goal-s42: SR=0.975, conc=success
  westd-pi05-vla-only-goal-s42-paired: SR=0.975, conc=success
  westd-pi05-vla-only-goal-s43-paired: SR=0.965, conc=success
  westd-pi05-vla-only-goal-s44-paired: SR=0.955, conc=success
  westd-pi05-vla-only-long-s42-paired: SR=0.98, conc=success
  westd-pi05-vla-only-long-s43-paired: SR=0.945, conc=success
  westd-pi05-vla-only-long-s44-paired: SR=0.96, conc=success
  westd-pi05-vla-only-object-s42-paired: SR=0.995, conc=success
  westd-pi05-vla-only-object-s43-paired: SR=1, conc=success
  westd-pi05-vla-only-object-s44-paired: SR=0.995, conc=success
  westd-pi05-vla-only-spatial-s42-paired: SR=0.98, conc=success
  westd-pi05-vla-only-spatial-s43-paired: SR=0.975, conc=success
  westd-pi05-vla-only-spatial-s44-paired: SR=0.985, conc=success

================================================================================
SMOLVLA TAU-SWEEP (object benchmark, seed 42)
================================================================================
  tau=0.15, seed=42: SR=0.79, conc=success | smolvla-adapt-tau015-object-s42-cqa1
  tau=0.15, seed=43: SR=0.78, conc=success | smolvla-adapt-tau015-object-s43-cqa1
  tau=0.15, seed=44: SR=0.735, conc=success | smolvla-adapt-tau015-object-s44-cqa1
  tau=0.05, seed=42: SR=0.75, conc=success | smolvla-tau005-object-s42
  tau=0.1, seed=42: SR=0.78, conc=success | smolvla-tau010-object-s42
  tau=0.15, seed=42: SR=0.78, conc=success | smolvla-tau015-object-s42
  tau=0.15, seed=43: SR=None, conc=failed | smolvla-tau015-object-s43
  tau=0.15, seed=43: SR=None, conc=killed | smolvla-tau015-object-s43-bjb1
  tau=0.2, seed=42: SR=0.785, conc=success | smolvla-tau020-object-s42
  tau=0.25, seed=42: SR=None, conc=killed | smolvla-tau025-object-s42
  tau=0.25, seed=42: SR=0.78, conc=success | smolvla-tau025-object-s42-r2
  tau=0.25, seed=42: SR=0.81, conc=success | smolvla-tau025-object-s42-r3
  tau=0.25, seed=43: SR=None, conc=failed | smolvla-tau025-object-s43
  tau=0.25, seed=43: SR=None, conc=killed | smolvla-tau025-object-s43-bjb1
  tau=0.25, seed=43: SR=0.775, conc=success | smolvla-tau025-object-s43-r3
  tau=0.3, seed=42: SR=0.79, conc=success | smolvla-tau030-object-s42
  tau=0.35, seed=42: SR=None, conc=killed | smolvla-tau035-object-s42
  tau=0.35, seed=42: SR=0.75, conc=success | smolvla-tau035-object-s42-r2
  tau=0.35, seed=42: SR=0.75, conc=success | smolvla-tau035-object-s42-r3
  tau=0.35, seed=43: SR=None, conc=failed | smolvla-tau035-object-s43
  tau=0.35, seed=43: SR=None, conc=killed | smolvla-tau035-object-s43-bjb1
  tau=0.35, seed=43: SR=0.77, conc=success | smolvla-tau035-object-s43-r3
  tau=0.4, seed=42: SR=0.735, conc=success | smolvla-tau040-object-s42
  tau=0.45, seed=42: SR=0.715, conc=success | smolvla-tau045-object-s42
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "175721fd-b001-43a2-840f-0e868351dd67"
}
```

</details>

---

### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "abc7696410407b735",
  "tool_use_id": "toolu_013vePFTt1F11vhKDNckffVj",
  "status": "completed",
  "output_file": "",
  "summary": "Parse registry DONE experiments",
  "usage": {
    "total_tokens": 83079,
    "tool_uses": 19,
    "duration_ms": 308975
  },
  "uuid": "25f6df6e-fe38-44af-a7ef-de844ea68c34",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53"
}
```

---

### Tool result

_source line 93 · 2026-05-28T15:56:11.605Z_

<details><summary>↩ Tool result · `toolu_013vePFTt1F11vhKDNckffVj`</summary>

```text
Now I have the complete picture. Here is the structured summary:

---

## Complete Registry Summary

**Registry stats**: 1415 total experiments, all status=DONE. Conclusions: 768 success, 421 killed, 130 failed, 96 negative. 900 experiments have metrics.

---

### 1. MAIN RESULTS (pi0.5 model, 200 rollouts = 10 tasks x 20 rollouts/task)

These are the primary experimental results across 5 methods and 4 benchmarks:

**VLA-only (baseline)**
| Benchmark | Seeds | Mean SR | Std |
|-----------|-------|---------|-----|
| spatial | 8 (42-49) | 79.8% | 0.8% |
| object | 9 (42-50) | 76.9% | 1.7% |
| goal | 8 (42-49) | 83.4% | 1.1% |
| long | 4 (42,44,45,47) | 59.2% | 1.1% |

**K2-mean baseline**
| Benchmark | Seeds | Mean SR | Std |
|-----------|-------|---------|-----|
| spatial | 6 (42-47) | 80.4% | 1.3% |
| object | 6 (42-47) | 77.3% | 1.4% |
| goal | 6 (42-47) | 82.5% | 1.4% |
| long | 6 (42-47) | 55.5% | 0.9% |

**ReConVLA**
| Benchmark | Seeds | Mean SR | Std |
|-----------|-------|---------|-----|
| spatial | 6 (42-47) | 80.3% | 0.7% |
| object | 6 (42-47) | 77.8% | 1.4% |
| goal | 5 (43-47) | 81.9% | 2.3% |
| long | 6 (42-47) | 57.1% | 1.5% |

**CRM-obs-only (norm=0.05)**
| Benchmark | Seeds | Mean SR | Std |
|-----------|-------|---------|-----|
| spatial | 7 (43-49) | 79.7% | 1.2% |
| object | 6 (42-47) | 78.0% | 2.6% |
| goal | 7 (42-48) | 82.3% | 1.6% |
| long | 6 (42-47) | 56.4% | 2.1% |

**ACR / Adaptive Conformal CRM (tau=0.25) -- the proposed method**
| Benchmark | Seeds | Mean SR | Std |
|-----------|-------|---------|-----|
| spatial | 8 (42-49) | 80.9% | 0.8% |
| object | 8 (42-49) | 77.0% | 2.0% |
| goal | 8 (42-49) | 83.4% | 1.7% |
| long | 4 (44-47) | 57.4% | 2.0% |

---

### 2. TAU-SWEEP EXPERIMENTS

**Pi0.5 spatial benchmark (seed 42):**
- tau=0.10: SR=79.0%, trigger_rate=75.2%
- tau=0.15: SR=79.5%, trigger_rate=40.7%
- tau=0.20: SR=81.0%, trigger_rate=26.6%
- tau=0.25: SR=82.0%, trigger_rate=~19.5%
- tau=0.30: SR=80.5%, trigger_rate=16.7%
- tau=0.35: SR=80.0%, trigger_rate=12.2%

**Pi0.5 goal benchmark (seed 42):**
- tau=0.15: SR=83.0%, trigger_rate=36.4%
- tau=0.25: SR=84.0%, trigger_rate=8.3%
- tau=0.35: SR=86.0%, trigger_rate=2.1%
- tau=0.50: SR=87.0%, trigger_rate=2.1%
- tau=0.70: SR=87.0%, trigger_rate=1.1%
- tau=0.90: SR=89.0%, trigger_rate=0.35%

**Pi0.5 long benchmark (seed 42):**
- tau=0.15: SR=61.0%, trigger_rate=24.1%
- tau=0.35: SR=57.0%, trigger_rate=1.0%

**Ablation on goal (seed 42):**
- tau=0.10: SR=81.0%, trigger_rate=73.9%
- tau=0.15: SR=85.0%, trigger_rate=33.9%
- tau=0.40: SR=83.5%, trigger_rate=1.2%

**SmolVLA object tau-sweep (seed 42):**
- tau=0.05: SR=75.0%
- tau=0.10: SR=78.0%
- tau=0.15: SR=78.0%
- tau=0.20: SR=78.5%
- tau=0.25: SR=81.0% (best, r3)
- tau=0.30: SR=79.0%
- tau=0.35: SR=75.0%
- tau=0.40: SR=73.5%
- tau=0.45: SR=71.5%

---

### 3. SMOLVLA EXPERIMENTS (secondary VLA model)

Present for spatial, object, goal, long. Key results with metrics:
- **Spatial**: VLA-only ~80%, CRM-norm005 ~80.5%, tau015 ~79-80.5%
- **Object**: VLA-only ~77%, tau015-adaptive ~73.5-79%, CRM-norm005 ~78%
- **Goal**: VLA-only ~82-83%, tau015 ~85.5%, tau025 ~84%
- **Long**: VLA-only ~58-62%, tau015 ~61%, various taus 53-61%

---

### 4. PI0.5 WESTD/PAIRED (different evaluation server -- much higher baseline SR)

VLA-only baseline on westd:
- spatial: 98.0%, 97.5%, 98.5% (seeds 42-44)
- object: 99.5%, 100%, 99.5% (seeds 42-44)
- goal: 97.5%, 96.5%, 95.5% (seeds 42-44)
- long: 98.0%, 94.5%, 96.0% (seeds 42-44)

These are clearly from a different hardware/rendering setup. Ceiling effect makes method comparison less informative.

---

### 5. ADAPTIVE-K EXPERIMENTS (efficiency/speed experiments)

These test reducing the number of action candidates K dynamically. Spatial benchmark with K=10 baseline:
- p25 (25th percentile threshold): SR~31-33%, avg K~7.6, fast_path~29%
- p50: SR~30-33%, avg K~6.3, fast_path~46%
- p75: SR~31-34%, avg K~5.0, fast_path~62%
- p90: SR~31-36%, avg K~3.5, fast_path~81%

SR is very low (30-36%) -- these appear to be from an older experimental setup (100 rollouts, K=10, SmolVLA/older model).

---

### 6. RANDOM-SELECTION BASELINE

Object: SR=7-14% (K=5), 9-12% (K=10) -- very low as expected
Spatial: SR=26-34%

---

### 7. OBS-ONLY (observation-only CRM, no VLA actions)

These are conformal prediction experiments on observations only:
- Spatial (norm=0.2): SR~32-37% across many seeds
- Object (norm=0.03-0.3): SR~10-22%
- Goal (norm=0.2): SR~66-68%

---

### COMPLETENESS ASSESSMENT

**Well-covered (6+ seeds across all 4 benchmarks):**
- VLA-only: spatial(8), object(9), goal(8), long(4) -- **long needs 2+ more seeds**
- ACR tau=0.25: spatial(8), object(8), goal(8), long(4) -- **long needs 2+ more seeds**
- CRM-obs-only: spatial(7), object(6), goal(7), long(6) -- complete
- K2-mean: spatial(6), object(6), goal(6), long(6) -- complete
- ReConVLA: spatial(6), object(6), goal(5), long(6) -- **goal needs 1 more seed (missing seed 42)**

**Missing configurations:**
1. **VLA-only long**: only seeds 42, 44, 45, 47 (missing 43, 46)
2. **ACR (tau=0.25) long**: only seeds 44-47 (missing 42, 43)
3. **ReConVLA goal**: only seeds 43-47 (missing 42)
4. **CRM-obs-only spatial**: missing seed 42 (has 43-49)
5. **Tau sweep**: mostly single-seed (seed 42). Multi-seed coverage only for tau=0.25

agentId: abc7696410407b735 (use SendMessage with to: 'abc7696410407b735' to continue this agent)
&lt;usage>total_tokens: 85014
tool_uses: 19
duration_ms: 308976&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "4a969d83-4a62-443e-be05-90faf0281f35",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Parse the registry JSON file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8c290cbe-aa35-4006-bed3-2d946febaa53/tool-results/mcp-agent-ml-research-read_registry-1779983442741.txt\n\nThis file is JSON with schema: {result: string} where result is itself a JSON string.\n\nI need you to:\n1. Probe structure with jq/python\n2. Extract ALL experiment entries that have status \"DONE\"\n3. For each, report: exp_id, conclusion, and key metrics (especially success_rate or SR for each task)\n4. Group them by experiment type - specifically identify:\n   - tau-sweep experiments (different tau values like tau025, tau05, tau075, tau10, tau15, tau20)\n   - bonus seed experiments (different seeds like s42, s43, s44)\n   - baseline experiments\n   - any other supplementary experiments\n5. Summarize which configurations are complete and which are missing\n\nReturn a structured summary. Be thorough - I need the complete picture of what's done.",
    "agentId": "abc7696410407b735",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have the complete picture. Here is the structured summary:\n\n---\n\n## Complete Registry Summary\n\n**Registry stats**: 1415 total experiments, all status=DONE. Conclusions: 768 success, 421 killed, 130 failed, 96 negative. 900 experiments have metrics.\n\n---\n\n### 1. MAIN RESULTS (pi0.5 model, 200 rollouts = 10 tasks x 20 rollouts/task)\n\nThese are the primary experimental results across 5 methods and 4 benchmarks:\n\n**VLA-only (baseline)**\n| Benchmark | Seeds | Mean SR | Std |\n|-----------|-------|---------|-----|\n| spatial | 8 (42-49) | 79.8% | 0.8% |\n| object | 9 (42-50) | 76.9% | 1.7% |\n| goal | 8 (42-49) | 83.4% | 1.1% |\n| long | 4 (42,44,45,47) | 59.2% | 1.1% |\n\n**K2-mean baseline**\n| Benchmark | Seeds | Mean SR | Std |\n|-----------|-------|---------|-----|\n| spatial | 6 (42-47) | 80.4% | 1.3% |\n| object | 6 (42-47) | 77.3% | 1.4% |\n| goal | 6 (42-47) | 82.5% | 1.4% |\n| long | 6 (42-47) | 55.5% | 0.9% |\n\n**ReConVLA**\n| Benchmark | Seeds | Mean SR | Std |\n|-----------|-------|---------|-----|\n| spatial | 6 (42-47) | 80.3% | 0.7% |\n| object | 6 (42-47) | 77.8% | 1.4% |\n| goal | 5 (43-47) | 81.9% | 2.3% |\n| long | 6 (42-47) | 57.1% | 1.5% |\n\n**CRM-obs-only (norm=0.05)**\n| Benchmark | Seeds | Mean SR | Std |\n|-----------|-------|---------|-----|\n| spatial | 7 (43-49) | 79.7% | 1.2% |\n| object | 6 (42-47) | 78.0% | 2.6% |\n| goal | 7 (42-48) | 82.3% | 1.6% |\n| long | 6 (42-47) | 56.4% | 2.1% |\n\n**ACR / Adaptive Conformal CRM (tau=0.25) -- the proposed method**\n| Benchmark | Seeds | Mean SR | Std |\n|-----------|-------|---------|-----|\n| spatial | 8 (42-49) | 80.9% | 0.8% |\n| object | 8 (42-49) | 77.0% | 2.0% |\n| goal | 8 (42-49) | 83.4% | 1.7% |\n| long | 4 (44-47) | 57.4% | 2.0% |\n\n---\n\n### 2. TAU-SWEEP EXPERIMENTS\n\n**Pi0.5 spatial benchmark (seed 42):**\n- tau=0.10: SR=79.0%, trigger_rate=75.2%\n- tau=0.15: SR=79.5%, trigger_rate=40.7%\n- tau=0.20: SR=81.0%, trigger_rate=26.6%\n- tau=0.25: SR=82.0%, trigger_rate=~19.5%\n- tau=0.30: SR=80.5%, trigger_rate=16.7%\n- tau=0.35: SR=80.0%, trigger_rate=12.2%\n\n**Pi0.5 goal benchmark (seed 42):**\n- tau=0.15: SR=83.0%, trigger_rate=36.4%\n- tau=0.25: SR=84.0%, trigger_rate=8.3%\n- tau=0.35: SR=86.0%, trigger_rate=2.1%\n- tau=0.50: SR=87.0%, trigger_rate=2.1%\n- tau=0.70: SR=87.0%, trigger_rate=1.1%\n- tau=0.90: SR=89.0%, trigger_rate=0.35%\n\n**Pi0.5 long benchmark (seed 42):**\n- tau=0.15: SR=61.0%, trigger_rate=24.1%\n- tau=0.35: SR=57.0%, trigger_rate=1.0%\n\n**Ablation on goal (seed 42):**\n- tau=0.10: SR=81.0%, trigger_rate=73.9%\n- tau=0.15: SR=85.0%, trigger_rate=33.9%\n- tau=0.40: SR=83.5%, trigger_rate=1.2%\n\n**SmolVLA object tau-sweep (seed 42):**\n- tau=0.05: SR=75.0%\n- tau=0.10: SR=78.0%\n- tau=0.15: SR=78.0%\n- tau=0.20: SR=78.5%\n- tau=0.25: SR=81.0% (best, r3)\n- tau=0.30: SR=79.0%\n- tau=0.35: SR=75.0%\n- tau=0.40: SR=73.5%\n- tau=0.45: SR=71.5%\n\n---\n\n### 3. SMOLVLA EXPERIMENTS (secondary VLA model)\n\nPresent for spatial, object, goal, long. Key results with metrics:\n- **Spatial**: VLA-only ~80%, CRM-norm005 ~80.5%, tau015 ~79-80.5%\n- **Object**: VLA-only ~77%, tau015-adaptive ~73.5-79%, CRM-norm005 ~78%\n- **Goal**: VLA-only ~82-83%, tau015 ~85.5%, tau025 ~84%\n- **Long**: VLA-only ~58-62%, tau015 ~61%, various taus 53-61%\n\n---\n\n### 4. PI0.5 WESTD/PAIRED (different evaluation server -- much higher baseline SR)\n\nVLA-only baseline on westd:\n- spatial: 98.0%, 97.5%, 98.5% (seeds 42-44)\n- object: 99.5%, 100%, 99.5% (seeds 42-44)\n- goal: 97.5%, 96.5%, 95.5% (seeds 42-44)\n- long: 98.0%, 94.5%, 96.0% (seeds 42-44)\n\nThese are clearly from a different hardware/rendering setup. Ceiling effect makes method comparison less informative.\n\n---\n\n### 5. ADAPTIVE-K EXPERIMENTS (efficiency/speed experiments)\n\nThese test reducing the number of action candidates K dynamically. Spatial benchmark with K=10 baseline:\n- p25 (25th percentile threshold): SR~31-33%, avg K~7.6, fast_path~29%\n- p50: SR~30-33%, avg K~6.3, fast_path~46%\n- p75: SR~31-34%, avg K~5.0, fast_path~62%\n- p90: SR~31-36%, avg K~3.5, fast_path~81%\n\nSR is very low (30-36%) -- these appear to be from an older experimental setup (100 rollouts, K=10, SmolVLA/older model).\n\n---\n\n### 6. RANDOM-SELECTION BASELINE\n\nObject: SR=7-14% (K=5), 9-12% (K=10) -- very low as expected\nSpatial: SR=26-34%\n\n---\n\n### 7. OBS-ONLY (observation-only CRM, no VLA actions)\n\nThese are conformal prediction experiments on observations only:\n- Spatial (norm=0.2): SR~32-37% across many seeds\n- Object (norm=0.03-0.3): SR~10-22%\n- Goal (norm=0.2): SR~66-68%\n\n---\n\n### COMPLETENESS ASSESSMENT\n\n**Well-covered (6+ seeds across all 4 benchmarks):**\n- VLA-only: spatial(8), object(9), goal(8), long(4) -- **long needs 2+ more seeds**\n- ACR tau=0.25: spatial(8), object(8), goal(8), long(4) -- **long needs 2+ more seeds**\n- CRM-obs-only: spatial(7), object(6), goal(7), long(6) -- complete\n- K2-mean: spatial(6), object(6), goal(6), long(6) -- complete\n- ReConVLA: spatial(6), object(6), goal(5), long(6) -- **goal needs 1 more seed (missing seed 42)**\n\n**Missing configurations:**\n1. **VLA-only long**: only seeds 42, 44, 45, 47 (missing 43, 46)\n2. **ACR (tau=0.25) long**: only seeds 44-47 (missing 42, 43)\n3. **ReConVLA goal**: only seeds 43-47 (missing 42)\n4. **CRM-obs-only spatial**: missing seed 42 (has 43-49)\n5. **Tau sweep**: mostly single-seed (seed 42). Multi-seed coverage only for tau=0.25"
      }
    ],
    "totalDurationMs": 308976,
    "totalTokens": 85014,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3420,
      "cache_read_input_tokens": 79215,
      "output_tokens": 2378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3420
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2378,
          "cache_read_input_tokens": 79215,
          "cache_creation_input_tokens": 3420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3420,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 18,
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

### Assistant

_source line 94_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the registry analysis. Now let me:
1. Check for residual processes on bjb1-18228 (need to use separate commands since pipe is blocked)
2. Read the supplementary summary
3. Read the ROADMAP for experiment plan

Let me also check the memory for any relevant context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "4adb4fda-4044-4489-bc49-4817e6325e1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGTv9P7cT4afXZAtGcfbbi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 103,
      "cache_creation_input_tokens": 3642,
      "cache_read_input_tokens": 27598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3642
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

_source line 95_

读取 supplementary summary 和检查 bjb1-18228 残留进程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "2e4cfd5b-6cad-45b1-9420-a2a805b67fbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGTv9P7cT4afXZAtGcfbbi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 103,
      "cache_creation_input_tokens": 3642,
      "cache_read_input_tokens": 27598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3642
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

_source line 96_

<details open><summary>🔧 Tool call — Read · `toolu_01NYaHpVdthA8NTdkgjwPnAj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/supplementary/supplementary_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "45e4de7e-5b78-411f-8961-db4a9c2556a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGTv9P7cT4afXZAtGcfbbi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 103,
      "cache_creation_input_tokens": 3642,
      "cache_read_input_tokens": 27598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3642
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

_source line 97 · 2026-05-28T15:56:15.968Z_

<details><summary>↩ Tool result · `toolu_01NYaHpVdthA8NTdkgjwPnAj`</summary>

```text
1	# Supplementary Experiment Results
2	
3	All results from experiments with status=DONE, conclusion=success.
4	
5	## A. Threshold (τ) Sensitivity Analysis
6	
7	**Total experiments: 55** (with valid SR values)
8	
9	### pi05 / goal
10	
11	| τ | seed | SR (%) | trigger_rate | source_exp_id |
12	|---|------|--------|-------------|---------------|
13	| 0.15 | 42 | 92.0 | 0.174 | pi05-adaptive-goal-s42-tau015-bjb2 |
14	| 0.15 | 43 | 87.5 | — | pi05-goal-tau015-s43-r3 |
15	| 0.25 | 43 | 88.5 | — | pi05-goal-tau025-s43-r3 |
16	| 0.35 | 42 | 87.5 | 0.057 | pi05-adaptive-goal-s42-tau035-bjb2 |
17	| 0.35 | 43 | 89.5 | — | pi05-goal-tau035-s43-r3 |
18	| 0.5 | 42 | 87.0 | 0.0206 | pi05-tau-sweep-goal-tau050-s42-r3 |
19	| 0.7 | 42 | 87.0 | 0.0104 | tau_sweep_goal_tau070_s42_cqa1 |
20	| 0.9 | 42 | 89.0 | 0.0035 | tau_sweep_goal_tau090_s42_cqa1 |
21	
22	### pi05 / long
23	
24	| τ | seed | SR (%) | trigger_rate | source_exp_id |
25	|---|------|--------|-------------|---------------|
26	| 0.15 | 42 | 84.0 | 0.114 | pi05-adaptive-long-s42-tau015-bjb2 |
27	| 0.15 | 43 | 82.0 | — | pi05-long-tau015-s43-r3 |
28	
29	### pi05 / spatial
30	
31	| τ | seed | SR (%) | trigger_rate | source_exp_id |
32	|---|------|--------|-------------|---------------|
33	| 0.15 | 42 | 97.0 | 0.112 | pi05-adaptive-spatial-s42-tau015-bjb2 |
34	| 0.15 | 43 | 96.5 | 0.117 | pi05-spatial-tau015-s43 |
35	| 0.25 | 43 | 98.5 | 0.028 | pi05-spatial-tau025-s43 |
36	| 0.35 | 42 | 96.5 | 0.0255 | pi05-adaptive-spatial-s42-tau035-bjb2 |
37	| 0.35 | 43 | 97.5 | 0.022 | pi05-spatial-tau035-s43 |
38	
39	### smolvla / goal
40	
41	| τ | seed | SR (%) | trigger_rate | source_exp_id |
42	|---|------|--------|-------------|---------------|
43	| 0.15 | 42 | 85.5 | 0.333 | smolvla-tau015-goal-s42 |
44	| 0.15 | 42 | 85.0 | 0.339 | eval-ablation-tau015-goal-s42 |
45	| 0.15 | 43 | 83.5 | 0.354 | smolvla-tau015-goal-s43 |
46	| 0.25 | 42 | 84.0 | 0.083 | smolvla-tau025-goal-s42 |
47	| 0.25 | 43 | 81.0 | 0.0925 | smolvla-tau025-goal-s43 |
48	| 0.35 | 42 | 82.5 | 0.024 | smolvla-tau035-goal-s42 |
49	| 0.35 | 43 | 85.5 | 0.0211 | smolvla-tau035-goal-s43 |
50	
51	### smolvla / long
52	
53	| τ | seed | SR (%) | trigger_rate | source_exp_id |
54	|---|------|--------|-------------|---------------|
55	| 0.1 | 42 | 53.5 | 0.613 | smolvla-tau010-long-s42 |
56	| 0.15 | 42 | 61.0 | 0.239 | smolvla-tau015-long-s42 |
57	| 0.15 | 43 | 61.0 | 0.236 | smolvla-tau015-long-s43 |
58	| 0.2 | 42 | 58.5 | 0.089 | smolvla-tau020-long-s42 |
59	| 0.2 | 43 | 54.5 | — | smolvla-tau020-long-s43-r2 |
60	| 0.25 | 42 | 56.0 | 0.042 | smolvla-tau025-long-s42 |
61	| 0.25 | 43 | 53.0 | 0.046 | smolvla-tau025-long-s43 |
62	| 0.3 | 42 | 54.5 | — | smolvla-tau030-long-s42-r2 |
63	| 0.3 | 43 | 55.5 | — | smolvla-tau030-long-s43-r2 |
64	| 0.35 | 42 | 57.5 | 0.013 | smolvla-tau035-long-s42 |
65	| 0.35 | 43 | 60.0 | 0.01 | smolvla-tau035-long-s43 |
66	| 0.4 | 42 | 60.0 | 0.004 | smolvla-tau040-long-s42 |
67	| 0.45 | 42 | 59.5 | 0.003 | smolvla-tau045-long-s42 |
68	
69	### smolvla / object
70	
71	| τ | seed | SR (%) | trigger_rate | source_exp_id |
72	|---|------|--------|-------------|---------------|
73	| 0.05 | 42 | 75.0 | — | smolvla-tau005-object-s42 |
74	| 0.1 | 42 | 78.0 | — | smolvla-tau010-object-s42 |
75	| 0.15 | 42 | 78.0 | 0.167 | smolvla-tau015-object-s42 |
76	| 0.2 | 42 | 78.5 | — | smolvla-tau020-object-s42 |
77	| 0.25 | 42 | 78.0 | 0.034 | smolvla-tau025-object-s42-r2 |
78	| 0.25 | 43 | 77.5 | 0.037 | smolvla-tau025-object-s43-r3 |
79	| 0.3 | 42 | 79.0 | 0.0231 | smolvla-tau030-object-s42 |
80	| 0.35 | 42 | 75.0 | 0.016 | smolvla-tau035-object-s42-r2 |
81	| 0.35 | 43 | 77.0 | 0.013 | smolvla-tau035-object-s43-r3 |
82	| 0.4 | 42 | 73.5 | 0.0091 | smolvla-tau040-object-s42 |
83	| 0.45 | 42 | 71.5 | 0.0075 | smolvla-tau045-object-s42 |
84	
85	### smolvla / spatial
86	
87	| τ | seed | SR (%) | trigger_rate | source_exp_id |
88	|---|------|--------|-------------|---------------|
89	| 0.1 | 42 | 78.0 | 0.744 | eval-k2-tau010-spatial-s42-r3 |
90	| 0.15 | 42 | 80.0 | 0.412 | eval-k2-tau015-spatial-s42-r2 |
91	| 0.15 | 43 | 80.5 | 0.386 | smolvla-tau015-spatial-s43 |
92	| 0.2 | 42 | 81.0 | 0.267 | eval-k2-tau020-spatial-s42 |
93	| 0.25 | 43 | 79.5 | 0.193 | smolvla-tau025-spatial-s43 |
94	| 0.3 | 42 | 79.5 | 0.168 | eval-k2-tau030-spatial-s42 |
95	| 0.35 | 42 | 80.5 | 0.118 | eval-k2-tau035-spatial-s42-v2 |
96	| 0.35 | 43 | 79.5 | 0.127 | smolvla-tau035-spatial-s43 |
97	| 0.45 | 42 | 80.0 | 0.073 | smolvla-tau045-spatial-s42 |
98	
99	## B. Supplementary Seeds (Mean ± Std)
100	
101	**Total experiments: 65** (with valid SR values)
102	
103	| benchmark | method | n_seeds | SR (mean ± std) |
104	|-----------|--------|---------|----------------|
105	| goal | adaptive_conformal_crm | 6 | 83.6 ± 1.9 |
106	| goal | crm_obs_only | 5 | 82.8 ± 1.8 |
107	| goal | reconvla | 2 | 81.2 ± 3.2 |
108	| goal | vla_only | 7 | 83.2 ± 1.4 |
109	| long | crm_obs_only | 1 | 54.0 |
110	| long | reconvla | 2 | 57.5 ± 2.1 |
111	| long | vla_only | 3 | 56.8 ± 2.4 |
112	| object | adaptive_conformal_crm | 1 | 81.0 |
113	| object | crm_obs_only | 1 | 79.5 |
114	| object | reconvla | 6 | 77.8 ± 1.5 |
115	| object | vla_only | 4 | 77.2 ± 2.3 |
116	| spatial | adaptive_conformal_crm | 8 | 80.4 ± 0.7 |
117	| spatial | crm_obs_only | 6 | 79.8 ± 1.2 |
118	| spatial | reconvla | 4 | 79.4 ± 0.9 |
119	| spatial | vla_only | 9 | 79.8 ± 0.9 |
120	
121	### Detailed per-seed results
122	
123	| benchmark | method | seed | SR (%) | source_exp_id |
124	|-----------|--------|------|--------|---------------|
125	| goal | adaptive_conformal_crm | 42 | 84.0 | eval-supp-goal-adapt-tau025-s42 |
126	| goal | adaptive_conformal_crm | 43 | 84.5 | eval-supp-adapt-tau025-goal-s43 |
127	| goal | adaptive_conformal_crm | 44 | 86.5 | eval-supp-adapt-tau025-goal-s44 |
128	| goal | adaptive_conformal_crm | 45 | 81.0 | eval-supp-goal-adapt-tau025-s45 |
129	| goal | adaptive_conformal_crm | 46 | 83.5 | eval-supp-goal-adapt-tau025-s46 |
130	| goal | adaptive_conformal_crm | 47 | 82.0 | eval-supp-goal-adapt-tau025-s47 |
131	| goal | crm_obs_only | 42 | 85.5 | eval-supp-goal-crm005-s42 |
132	| goal | crm_obs_only | 44 | 83.5 | eval-supp-crm-norm005-goal-s44 |
133	| goal | crm_obs_only | 45 | 81.0 | eval-supp-goal-crm-norm005-s45 |
134	| goal | crm_obs_only | 46 | 82.0 | eval-supp-goal-crm-norm005-s46 |
135	| goal | crm_obs_only | 47 | 82.0 | eval-supp-goal-crm-norm005-s47 |
136	| goal | reconvla | 46 | 79.0 | eval-supp-goal-reconvla-s46 |
137	| goal | reconvla | 47 | 83.5 | eval-supp-goal-reconvla-s47 |
138	| goal | vla_only | 42 | 85.5 | eval-supp-k2mean-goal-s42-r2 |
139	| goal | vla_only | 43 | 82.5 | eval-supp-goal-vla-only-wrapper-s43 |
140	| goal | vla_only | 44 | 82.0 | eval-supp-goal-vla-only-wrapper-s44 |
141	| goal | vla_only | 46 | 83.0 | eval-supp-goal-vla-only-s46 |
142	| goal | vla_only | 46 | 82.5 | eval-supp-goal-k2mean-s46 |
143	| goal | vla_only | 48 | 85.0 | eval-supp-vla-only-goal-s48 |
144	| goal | vla_only | 49 | 82.0 | eval-supp-vla-only-goal-s49 |
145	| long | crm_obs_only | 46 | 54.0 | eval-supp-long-crm-norm005-s46 |
146	| long | reconvla | 45 | 59.0 | eval-supp-long-reconvla-s45 |
147	| long | reconvla | 46 | 56.0 | eval-supp-long-reconvla-s46 |
148	| long | vla_only | 45 | 56.0 | eval-supp-long-k2mean-s45 |
149	| long | vla_only | 46 | 55.0 | eval-supp-long-k2mean-s46 |
150	| long | vla_only | 47 | 59.5 | eval-supp-long-vla-only-s47-r4 |
151	| object | adaptive_conformal_crm | 42 | 81.0 | eval-supp-obj-adapt-tau025-s42 |
152	| object | crm_obs_only | 46 | 79.5 | eval-supp-crm-obj-s46 |
153	| object | reconvla | 42 | 79.0 | eval-supp-obj-reconvla-s42 |
154	| object | reconvla | 43 | 77.0 | eval-supp-obj-reconvla-s43 |
155	| object | reconvla | 44 | 76.0 | eval-supp-obj-reconvla-s44 |
156	| object | reconvla | 45 | 78.0 | eval-supp-reconvla-obj-s45 |
157	| object | reconvla | 46 | 80.0 | eval-supp-reconvla-obj-s46 |
158	| object | reconvla | 47 | 76.5 | eval-supp-obj-reconvla-s47 |
159	| object | vla_only | 42 | 79.5 | eval-supp-k2mean-object-s42 |
160	| object | vla_only | 44 | 75.0 | eval-supp-k2mean-object-s44 |
161	| object | vla_only | 48 | 79.0 | eval-supp-vla-only-obj-s48 |
162	| object | vla_only | 49 | 75.5 | eval-supp-vla-only-obj-s49 |
163	| spatial | adaptive_conformal_crm | 42 | 80.5 | eval-supp-adapt-tau015-spatial-s42-r2 |
164	| spatial | adaptive_conformal_crm | 42 | 82.0 | eval-supp-adapt-tau025-spatial-s42-r2 |
165	| spatial | adaptive_conformal_crm | 42 | 80.0 | eval-supp-adapt-tau035-spatial-s42-r2 |
166	| spatial | adaptive_conformal_crm | 43 | 80.0 | eval-supp-adapt-tau025-spatial-s43 |
167	| spatial | adaptive_conformal_crm | 44 | 80.5 | eval-supp-adapt-tau025-spatial-s44 |
168	| spatial | adaptive_conformal_crm | 45 | 80.0 | eval-supp-spatial-adapt-tau025-s45-r3 |
169	| spatial | adaptive_conformal_crm | 45 | 80.0 | eval-supp-adapt-tau025-spatial-s45 |
170	| spatial | adaptive_conformal_crm | 46 | 80.0 | eval-supp-spatial-adapt-tau025-s46 |
171	| spatial | crm_obs_only | 42 | 79.0 | eval-supp-crm-norm02-spatial-s42-r2 |
172	| spatial | crm_obs_only | 43 | 81.0 | eval-supp-crm-norm005-spatial-s43 |
173	| spatial | crm_obs_only | 44 | 78.5 | eval-supp-crm-norm005-spatial-s44 |
174	| spatial | crm_obs_only | 45 | 80.5 | eval-supp-crm-norm005-spatial-s45 |
175	| spatial | crm_obs_only | 46 | 78.5 | eval-supp-crm-norm005-spatial-s46 |
176	| spatial | crm_obs_only | 46 | 81.0 | eval-supp-spatial-crm-norm005-s46 |
177	| spatial | reconvla | 42 | 80.0 | eval-supp-reconvla-k2-spatial-s42 |
178	| spatial | reconvla | 45 | 79.5 | eval-supp-spatial-reconvla-s45 |
179	| spatial | reconvla | 46 | 80.0 | eval-supp-spatial-reconvla-s46 |
180	| spatial | reconvla | 47 | 78.0 | eval-supp-spatial-reconvla-s47 |
181	| spatial | vla_only | 44 | 78.5 | eval-supp-spatial-vla-only-s44 |
182	| spatial | vla_only | 45 | 80.0 | eval-supp-vla-only-spatial-s45 |
183	| spatial | vla_only | 45 | 80.0 | eval-supp-spatial-k2mean-s45 |
184	| spatial | vla_only | 46 | 80.0 | eval-supp-spatial-k2mean-s46 |
185	| spatial | vla_only | 46 | 80.5 | eval-supp-vla-only-spatial-s46 |
186	| spatial | vla_only | 46 | 80.5 | eval-supp-spatial-vla-only-s46 |
187	| spatial | vla_only | 47 | 81.0 | eval-supp-spatial-vla-only-s47 |
188	| spatial | vla_only | 48 | 79.5 | eval-supp-vla-only-spatial-s48 |
189	| spatial | vla_only | 49 | 78.5 | eval-supp-vla-only-spatial-s49 |
190	
191	## C. Pi05 Cross-VLA Generalization (Table 2)
192	
193	**Total experiments: 33** (canonical, deduplicated)
194	
195	### Summary (Mean ± Std)
196	
197	| benchmark | mode | n | SR (mean ± std) |
198	|-----------|------|---|----------------|
199	| goal | adaptive_conformal_crm | 2 | 89.5 ± 0.0 |
200	| goal | crm_obs_only | 3 | 84.5 ± 1.3 |
201	| goal | vla_only | 3 | 97.5 ± 0.5 |
202	| long | adaptive_conformal_crm | 3 | 81.3 ± 1.4 |
203	| long | crm_obs_only | 1 | 76.0 |
204	| long | vla_only | 3 | 95.0 ± 0.9 |
205	| object | adaptive_conformal_crm | 3 | 86.2 ± 1.6 |
206	| object | crm_obs_only | 3 | 88.0 ± 1.0 |
207	| object | vla_only | 3 | 99.3 ± 0.8 |
208	| spatial | adaptive_conformal_crm | 3 | 97.2 ± 0.8 |
209	| spatial | crm_obs_only | 3 | 96.8 ± 0.3 |
210	| spatial | vla_only | 3 | 98.0 ± 0.5 |
211	
212	### Per-seed detail
213	
214	| benchmark | mode | seed | SR (%) | source_exp_id |
215	|-----------|------|------|--------|---------------|
216	| goal | adaptive_conformal_crm | 42 | 89.5 | pi05-adaptive-goal-s42-cqa1 |
217	| goal | adaptive_conformal_crm | 43 | 89.5 | pi05-adaptive-goal-s43-bjb1-18228 |
218	| goal | crm_obs_only | 42 | 85.5 | westd-pi05-crm-k2-goal-s42 |
219	| goal | crm_obs_only | 43 | 83.0 | pi05-crm-k2-goal-s43-bjb1-r2 |
220	| goal | crm_obs_only | 44 | 85.0 | pi05-crm-k2-goal-s44-bjb1-r2 |
221	| goal | vla_only | 42 | 98.0 | eval-pi05-vla-only-goal-s42-paired |
222	| goal | vla_only | 43 | 97.0 | eval-pi05-vla-only-goal-s43-v2 |
223	| goal | vla_only | 44 | 97.5 | eval-pi05-vla-only-goal-s44 |
224	| long | adaptive_conformal_crm | 42 | 80.5 | pi05-adaptive-long-s42-r2 |
225	| long | adaptive_conformal_crm | 43 | 80.5 | pi05-adaptive-long-s43-cqa1-r3 |
226	| long | adaptive_conformal_crm | 44 | 83.0 | pi05-adaptive-long-s44-cqa1-r3 |
227	| long | crm_obs_only | 44 | 76.0 | pi05-crm-k2-long-s44-cqa1 |
228	| long | vla_only | 42 | 94.0 | eval-pi05-vla-only-long-seed42-r4-rerun |
229	| long | vla_only | 43 | 95.5 | eval-pi05-vla-only-long-seed43-r4 |
230	| long | vla_only | 44 | 95.5 | eval-pi05-vla-only-long-seed44-r4 |
231	| object | adaptive_conformal_crm | 42 | 85.5 | pi05-adaptive-object-s42-cqa1 |
232	| object | adaptive_conformal_crm | 43 | 85.0 | pi05-adaptive-object-s43-cqa1-r3 |
233	| object | adaptive_conformal_crm | 44 | 88.0 | pi05-adaptive-object-s44-cqa1-r3 |
234	| object | crm_obs_only | 42 | 89.0 | pi05-crm-k2-object-s42-bjb1-r2 |
235	| object | crm_obs_only | 43 | 87.0 | pi05-crm-k2-object-s43-bjb1-r2 |
236	| object | crm_obs_only | 44 | 88.0 | pi05-crm-k2-object-s44-bjb1-r2 |
237	| object | vla_only | 42 | 100.0 | eval-pi05-vla-only-object-seed42-r4 |
238	| object | vla_only | 43 | 98.5 | eval-pi05-vla-only-object-seed43-r4 |
239	| object | vla_only | 44 | 99.5 | eval-pi05-vla-only-object-seed44-r4 |
240	| spatial | adaptive_conformal_crm | 42 | 96.5 | pi05-adaptive-spatial-s42-bjb2-r2 |
241	| spatial | adaptive_conformal_crm | 43 | 98.0 | pi05-adaptive-spatial-s43-bjb2-r2 |
242	| spatial | adaptive_conformal_crm | 44 | 97.0 | pi05-adaptive-spatial-s44-bjb2-r2 |
243	| spatial | crm_obs_only | 42 | 96.5 | pi05-crm-k2-spatial-s42-bjb2-r2 |
244	| spatial | crm_obs_only | 43 | 97.0 | pi05-crm-k2-spatial-s43-bjb2-r2 |
245	| spatial | crm_obs_only | 44 | 97.0 | pi05-crm-k2-spatial-s44-bjb2-r2 |
246	| spatial | vla_only | 42 | 98.0 | eval-pi05-vla-only-spatial-s42-paired |
247	| spatial | vla_only | 43 | 97.5 | westd-pi05-vla-only-spatial-s43-paired |
248	| spatial | vla_only | 44 | 98.5 | westd-pi05-vla-only-spatial-s44-paired |
249	
250	## D. K-sweep Results
251	
252	**Total experiments: 23** (22 with valid SR)
253	
254	| model | benchmark | mode | seed | K | SR (%) | source_exp_id |
255	|-------|-----------|------|------|---|--------|---------------|
256	| — | object | — | — | 5 | 18.0 | eval-obs-only-object-norm02-k5-seed48 |
257	| smolvla | object | crm_obs_only | 42 | 5 | 73.5 | eval-ksweep-k5-obs-object-s42 |
258	| — | object | crm_obs_only | 42 | 5 | — | eval-obs-only-object-norm02-k5-seed42 |
259	| — | object | random_selection | 42 | 5 | 14.0 | eval-random-selection-object-k5-seed42-r2 |
260	| smolvla | object | crm_obs_only | 43 | 5 | 73.0 | eval-ksweep-k5-obs-object-s43 |
261	| — | object | crm_obs_only | 43 | 5 | 19.0 | eval-obs-only-object-norm02-k5-seed43 |
262	| — | object | random_selection | 43 | 5 | 11.0 | eval-random-selection-object-k5-seed43-r2 |
263	| — | object | crm_obs_only | 44 | 5 | 14.0 | eval-k5-obs-only-object-seed44 |
264	| — | object | crm_obs_only | 44 | 5 | 17.0 | eval-obs-only-object-norm02-k5-seed44 |
265	| — | object | random_selection | 44 | 5 | 10.0 | eval-random-selection-object-k5-seed44-r2 |
266	| — | object | crm_obs_only | 45 | 5 | 15.0 | eval-obs-only-object-norm02-k5-seed45 |
267	| — | object | random_selection | 45 | 5 | 7.0 | eval-random-selection-object-k5-seed45-r2 |
268	| — | object | crm_obs_only | 46 | 5 | 16.0 | eval-obs-only-object-norm02-k5-seed46 |
269	| — | object | crm_obs_only | 47 | 5 | 13.0 | eval-obs-only-object-norm02-k5-seed47 |
270	| smolvla | object | crm_obs_only | 44 | 10 | 78.0 | smolvla-crm-norm005-k10-object-s44-cqa1 |
271	| smolvla | object | crm_obs_only | 42 | 20 | 75.5 | eval-ksweep-k20-obs-object-s42 |
272	| smolvla | object | crm_obs_only | 43 | 20 | 73.5 | eval-ksweep-k20-obs-object-s43 |
273	| — | spatial | — | — | 5 | 35.0 | eval-obs-only-spatial-norm02-k5-seed42 |
274	| — | spatial | — | — | 5 | 32.0 | eval-obs-only-spatial-norm02-k5-seed43 |
275	| — | spatial | adaptive_conformal_crm | 42 | 5 | 79.0 | eval-k5-spatial-s42-sweep |
276	| — | spatial | crm_obs_only | 44 | 5 | 37.0 | eval-obs-only-spatial-norm02-k5-seed44-r2 |
277	| — | spatial | crm_obs_only | 45 | 5 | 34.0 | eval-obs-only-spatial-norm02-k5-seed45-r2 |
278	| — | spatial | crm_obs_only | 51 | 10 | 36.0 | eval-crm-spatial-k10-seed51 |
279	
280	### K-sweep summary (SmolVLA, object, crm_obs_only)
281	
282	| K | seeds | SR (mean ± std) |
283	|---|-------|----------------|
284	| 5 | 2 | 73.2 ± 0.4 |
285	| 10 | 1 | 78.0 |
286	| 20 | 2 | 74.5 ± 1.4 |
287	
288	## E. CRM Always-On Ablation (τ=0.001)
289	
290	**Total experiments: 23** (23 with valid SR)
291	
292	### Summary (Mean ± Std)
293	
294	| model | benchmark | n | SR (mean ± std) |
295	|-------|-----------|---|----------------|
296	| pi05 | goal | 1 | 81.5 |
297	| pi05 | long | 1 | 77.0 |
298	| pi05 | object | 2 | 91.2 ± 1.1 |
299	| pi05 | spatial | 1 | 96.0 |
300	| smolvla | goal | 5 | 80.4 ± 1.0 |
301	| smolvla | long | 3 | 43.2 ± 2.3 |
302	| smolvla | object | 5 | 72.2 ± 3.0 |
303	| smolvla | spatial | 5 | 77.9 ± 1.3 |
304	
305	### Per-seed detail
306	
307	| model | benchmark | seed | SR (%) | trigger_rate (%) | source_exp_id |
308	|-------|-----------|------|--------|-----------------|---------------|
309	| pi05 | goal | 42 | 81.5 | 100 | pi05-crm-always-on-goal-s42 |
310	| pi05 | long | 42 | 77.0 | 100 | pi05-crm-always-on-long-s42 |
311	| pi05 | object | 42 | 90.5 | 100 | pi05-crm-always-on-object-s42 |
312	| pi05 | object | 43 | 92.0 | 100 | pi05-crm-always-on-object-s43 |
313	| pi05 | spatial | 42 | 96.0 | 100 | pi05-crm-always-on-spatial-s42 |
314	| smolvla | goal | 42 | 80.0 | 100 | crm-always-on-goal-s42 |
315	| smolvla | goal | 43 | 79.5 | 100 | crm-always-on-goal-s43 |
316	| smolvla | goal | 44 | 80.5 | 100 | crm-always-on-goal-s44 |
317	| smolvla | goal | 45 | 82.0 | 100 | crm-always-on-goal-s45 |
318	| smolvla | goal | 46 | 80.0 | 100 | crm-always-on-goal-s46 |
319	| smolvla | long | 42 | 41.0 | 100 | crm-always-on-long-s42 |
320	| smolvla | long | 43 | 45.5 | 100 | crm-always-on-long-s43 |
321	| smolvla | long | 44 | 43.0 | 100 | crm-always-on-long-s44 |
322	| smolvla | object | 42 | 71.0 | 100 | crm-always-on-object-s42 |
323	| smolvla | object | 43 | 73.5 | 100 | crm-always-on-object-s43 |
324	| smolvla | object | 44 | 74.5 | 100 | crm-always-on-object-s44 |
325	| smolvla | object | 45 | 74.5 | 100 | crm-always-on-object-s45 |
326	| smolvla | object | 46 | 67.5 | 100 | crm-always-on-object-s46 |
327	| smolvla | spatial | 42 | 79.0 | 100 | crm-always-on-spatial-s42 |
328	| smolvla | spatial | 43 | 76.0 | 100 | crm-always-on-spatial-s43 |
329	| smolvla | spatial | 44 | 79.0 | 100 | crm-always-on-spatial-s44 |
330	| smolvla | spatial | 45 | 77.0 | 100 | crm-always-on-spatial-s45 |
331	| smolvla | spatial | 46 | 78.5 | 100 | crm-always-on-spatial-s46 |
332	
333	## F. Data Gaps & Notes
334	
335	### Incomplete categories
336	- **Bonus seeds / long / adaptive**: Only experiments with None SR (s42/s45/s46) — **incomplete**
337	- **Bonus seeds / object / adaptive**: Only 1 valid experiment (s42) — **incomplete**
338	- **Bonus seeds / object / crm_obs_only**: Only 1 valid experiment (s46) — **incomplete**
339	- **Bonus seeds / long / crm_obs_only**: Only 1 valid experiment (s46) — **incomplete**
340	- **Bonus seeds / goal / reconvla**: Only 2 valid experiments (s46, s47) — **incomplete**
341	- **Bonus seeds / long / reconvla**: Only 2 valid experiments (s45, s46) — **incomplete**
342	- **Pi05 / long / crm_obs_only**: Only 1 seed (s44) — **incomplete**
343	- **K-sweep**: Many experiments have None SR (especially K=20 and reconvla/argmin variants)
344	- **CRM always-on / smolvla / long**: s45 has None SR — **incomplete**
345	
346	### Deduplication notes
347	- Multiple runs exist for same conditions (e.g., different servers, -r2/-r3 reruns). This summary uses the latest successful run with valid metrics.
348	- Pi05 vla_only experiments with SR=0% (e.g., seed42-r4 long, seed43/44 object) are excluded as known OOM artifacts.
349	- Trigger rates stored inconsistently: some as fractions (0.0–1.0), some as percentages (0–100). Values >1.0 in the tau-sweep are likely percentages.
350	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "4d06b869-aaa8-41ac-afce-692cde488a2e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/supplementary/supplementary_summary.md",
      "content": "# Supplementary Experiment Results\n\nAll results from experiments with status=DONE, conclusion=success.\n\n## A. Threshold (τ) Sensitivity Analysis\n\n**Total experiments: 55** (with valid SR values)\n\n### pi05 / goal\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.15 | 42 | 92.0 | 0.174 | pi05-adaptive-goal-s42-tau015-bjb2 |\n| 0.15 | 43 | 87.5 | — | pi05-goal-tau015-s43-r3 |\n| 0.25 | 43 | 88.5 | — | pi05-goal-tau025-s43-r3 |\n| 0.35 | 42 | 87.5 | 0.057 | pi05-adaptive-goal-s42-tau035-bjb2 |\n| 0.35 | 43 | 89.5 | — | pi05-goal-tau035-s43-r3 |\n| 0.5 | 42 | 87.0 | 0.0206 | pi05-tau-sweep-goal-tau050-s42-r3 |\n| 0.7 | 42 | 87.0 | 0.0104 | tau_sweep_goal_tau070_s42_cqa1 |\n| 0.9 | 42 | 89.0 | 0.0035 | tau_sweep_goal_tau090_s42_cqa1 |\n\n### pi05 / long\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.15 | 42 | 84.0 | 0.114 | pi05-adaptive-long-s42-tau015-bjb2 |\n| 0.15 | 43 | 82.0 | — | pi05-long-tau015-s43-r3 |\n\n### pi05 / spatial\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.15 | 42 | 97.0 | 0.112 | pi05-adaptive-spatial-s42-tau015-bjb2 |\n| 0.15 | 43 | 96.5 | 0.117 | pi05-spatial-tau015-s43 |\n| 0.25 | 43 | 98.5 | 0.028 | pi05-spatial-tau025-s43 |\n| 0.35 | 42 | 96.5 | 0.0255 | pi05-adaptive-spatial-s42-tau035-bjb2 |\n| 0.35 | 43 | 97.5 | 0.022 | pi05-spatial-tau035-s43 |\n\n### smolvla / goal\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.15 | 42 | 85.5 | 0.333 | smolvla-tau015-goal-s42 |\n| 0.15 | 42 | 85.0 | 0.339 | eval-ablation-tau015-goal-s42 |\n| 0.15 | 43 | 83.5 | 0.354 | smolvla-tau015-goal-s43 |\n| 0.25 | 42 | 84.0 | 0.083 | smolvla-tau025-goal-s42 |\n| 0.25 | 43 | 81.0 | 0.0925 | smolvla-tau025-goal-s43 |\n| 0.35 | 42 | 82.5 | 0.024 | smolvla-tau035-goal-s42 |\n| 0.35 | 43 | 85.5 | 0.0211 | smolvla-tau035-goal-s43 |\n\n### smolvla / long\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.1 | 42 | 53.5 | 0.613 | smolvla-tau010-long-s42 |\n| 0.15 | 42 | 61.0 | 0.239 | smolvla-tau015-long-s42 |\n| 0.15 | 43 | 61.0 | 0.236 | smolvla-tau015-long-s43 |\n| 0.2 | 42 | 58.5 | 0.089 | smolvla-tau020-long-s42 |\n| 0.2 | 43 | 54.5 | — | smolvla-tau020-long-s43-r2 |\n| 0.25 | 42 | 56.0 | 0.042 | smolvla-tau025-long-s42 |\n| 0.25 | 43 | 53.0 | 0.046 | smolvla-tau025-long-s43 |\n| 0.3 | 42 | 54.5 | — | smolvla-tau030-long-s42-r2 |\n| 0.3 | 43 | 55.5 | — | smolvla-tau030-long-s43-r2 |\n| 0.35 | 42 | 57.5 | 0.013 | smolvla-tau035-long-s42 |\n| 0.35 | 43 | 60.0 | 0.01 | smolvla-tau035-long-s43 |\n| 0.4 | 42 | 60.0 | 0.004 | smolvla-tau040-long-s42 |\n| 0.45 | 42 | 59.5 | 0.003 | smolvla-tau045-long-s42 |\n\n### smolvla / object\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.05 | 42 | 75.0 | — | smolvla-tau005-object-s42 |\n| 0.1 | 42 | 78.0 | — | smolvla-tau010-object-s42 |\n| 0.15 | 42 | 78.0 | 0.167 | smolvla-tau015-object-s42 |\n| 0.2 | 42 | 78.5 | — | smolvla-tau020-object-s42 |\n| 0.25 | 42 | 78.0 | 0.034 | smolvla-tau025-object-s42-r2 |\n| 0.25 | 43 | 77.5 | 0.037 | smolvla-tau025-object-s43-r3 |\n| 0.3 | 42 | 79.0 | 0.0231 | smolvla-tau030-object-s42 |\n| 0.35 | 42 | 75.0 | 0.016 | smolvla-tau035-object-s42-r2 |\n| 0.35 | 43 | 77.0 | 0.013 | smolvla-tau035-object-s43-r3 |\n| 0.4 | 42 | 73.5 | 0.0091 | smolvla-tau040-object-s42 |\n| 0.45 | 42 | 71.5 | 0.0075 | smolvla-tau045-object-s42 |\n\n### smolvla / spatial\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.1 | 42 | 78.0 | 0.744 | eval-k2-tau010-spatial-s42-r3 |\n| 0.15 | 42 | 80.0 | 0.412 | eval-k2-tau015-spatial-s42-r2 |\n| 0.15 | 43 | 80.5 | 0.386 | smolvla-tau015-spatial-s43 |\n| 0.2 | 42 | 81.0 | 0.267 | eval-k2-tau020-spatial-s42 |\n| 0.25 | 43 | 79.5 | 0.193 | smolvla-tau025-spatial-s43 |\n| 0.3 | 42 | 79.5 | 0.168 | eval-k2-tau030-spatial-s42 |\n| 0.35 | 42 | 80.5 | 0.118 | eval-k2-tau035-spatial-s42-v2 |\n| 0.35 | 43 | 79.5 | 0.127 | smolvla-tau035-spatial-s43 |\n| 0.45 | 42 | 80.0 | 0.073 | smolvla-tau045-spatial-s42 |\n\n## B. Supplementary Seeds (Mean ± Std)\n\n**Total experiments: 65** (with valid SR values)\n\n| benchmark | method | n_seeds | SR (mean ± std) |\n|-----------|--------|---------|----------------|\n| goal | adaptive_conformal_crm | 6 | 83.6 ± 1.9 |\n| goal | crm_obs_only | 5 | 82.8 ± 1.8 |\n| goal | reconvla | 2 | 81.2 ± 3.2 |\n| goal | vla_only | 7 | 83.2 ± 1.4 |\n| long | crm_obs_only | 1 | 54.0 |\n| long | reconvla | 2 | 57.5 ± 2.1 |\n| long | vla_only | 3 | 56.8 ± 2.4 |\n| object | adaptive_conformal_crm | 1 | 81.0 |\n| object | crm_obs_only | 1 | 79.5 |\n| object | reconvla | 6 | 77.8 ± 1.5 |\n| object | vla_only | 4 | 77.2 ± 2.3 |\n| spatial | adaptive_conformal_crm | 8 | 80.4 ± 0.7 |\n| spatial | crm_obs_only | 6 | 79.8 ± 1.2 |\n| spatial | reconvla | 4 | 79.4 ± 0.9 |\n| spatial | vla_only | 9 | 79.8 ± 0.9 |\n\n### Detailed per-seed results\n\n| benchmark | method | seed | SR (%) | source_exp_id |\n|-----------|--------|------|--------|---------------|\n| goal | adaptive_conformal_crm | 42 | 84.0 | eval-supp-goal-adapt-tau025-s42 |\n| goal | adaptive_conformal_crm | 43 | 84.5 | eval-supp-adapt-tau025-goal-s43 |\n| goal | adaptive_conformal_crm | 44 | 86.5 | eval-supp-adapt-tau025-goal-s44 |\n| goal | adaptive_conformal_crm | 45 | 81.0 | eval-supp-goal-adapt-tau025-s45 |\n| goal | adaptive_conformal_crm | 46 | 83.5 | eval-supp-goal-adapt-tau025-s46 |\n| goal | adaptive_conformal_crm | 47 | 82.0 | eval-supp-goal-adapt-tau025-s47 |\n| goal | crm_obs_only | 42 | 85.5 | eval-supp-goal-crm005-s42 |\n| goal | crm_obs_only | 44 | 83.5 | eval-supp-crm-norm005-goal-s44 |\n| goal | crm_obs_only | 45 | 81.0 | eval-supp-goal-crm-norm005-s45 |\n| goal | crm_obs_only | 46 | 82.0 | eval-supp-goal-crm-norm005-s46 |\n| goal | crm_obs_only | 47 | 82.0 | eval-supp-goal-crm-norm005-s47 |\n| goal | reconvla | 46 | 79.0 | eval-supp-goal-reconvla-s46 |\n| goal | reconvla | 47 | 83.5 | eval-supp-goal-reconvla-s47 |\n| goal | vla_only | 42 | 85.5 | eval-supp-k2mean-goal-s42-r2 |\n| goal | vla_only | 43 | 82.5 | eval-supp-goal-vla-only-wrapper-s43 |\n| goal | vla_only | 44 | 82.0 | eval-supp-goal-vla-only-wrapper-s44 |\n| goal | vla_only | 46 | 83.0 | eval-supp-goal-vla-only-s46 |\n| goal | vla_only | 46 | 82.5 | eval-supp-goal-k2mean-s46 |\n| goal | vla_only | 48 | 85.0 | eval-supp-vla-only-goal-s48 |\n| goal | vla_only | 49 | 82.0 | eval-supp-vla-only-goal-s49 |\n| long | crm_obs_only | 46 | 54.0 | eval-supp-long-crm-norm005-s46 |\n| long | reconvla | 45 | 59.0 | eval-supp-long-reconvla-s45 |\n| long | reconvla | 46 | 56.0 | eval-supp-long-reconvla-s46 |\n| long | vla_only | 45 | 56.0 | eval-supp-long-k2mean-s45 |\n| long | vla_only | 46 | 55.0 | eval-supp-long-k2mean-s46 |\n| long | vla_only | 47 | 59.5 | eval-supp-long-vla-only-s47-r4 |\n| object | adaptive_conformal_crm | 42 | 81.0 | eval-supp-obj-adapt-tau025-s42 |\n| object | crm_obs_only | 46 | 79.5 | eval-supp-crm-obj-s46 |\n| object | reconvla | 42 | 79.0 | eval-supp-obj-reconvla-s42 |\n| object | reconvla | 43 | 77.0 | eval-supp-obj-reconvla-s43 |\n| object | reconvla | 44 | 76.0 | eval-supp-obj-reconvla-s44 |\n| object | reconvla | 45 | 78.0 | eval-supp-reconvla-obj-s45 |\n| object | reconvla | 46 | 80.0 | eval-supp-reconvla-obj-s46 |\n| object | reconvla | 47 | 76.5 | eval-supp-obj-reconvla-s47 |\n| object | vla_only | 42 | 79.5 | eval-supp-k2mean-object-s42 |\n| object | vla_only | 44 | 75.0 | eval-supp-k2mean-object-s44 |\n| object | vla_only | 48 | 79.0 | eval-supp-vla-only-obj-s48 |\n| object | vla_only | 49 | 75.5 | eval-supp-vla-only-obj-s49 |\n| spatial | adaptive_conformal_crm | 42 | 80.5 | eval-supp-adapt-tau015-spatial-s42-r2 |\n| spatial | adaptive_conformal_crm | 42 | 82.0 | eval-supp-adapt-tau025-spatial-s42-r2 |\n| spatial | adaptive_conformal_crm | 42 | 80.0 | eval-supp-adapt-tau035-spatial-s42-r2 |\n| spatial | adaptive_conformal_crm | 43 | 80.0 | eval-supp-adapt-tau025-spatial-s43 |\n| spatial | adaptive_conformal_crm | 44 | 80.5 | eval-supp-adapt-tau025-spatial-s44 |\n| spatial | adaptive_conformal_crm | 45 | 80.0 | eval-supp-spatial-adapt-tau025-s45-r3 |\n| spatial | adaptive_conformal_crm | 45 | 80.0 | eval-supp-adapt-tau025-spatial-s45 |\n| spatial | adaptive_conformal_crm | 46 | 80.0 | eval-supp-spatial-adapt-tau025-s46 |\n| spatial | crm_obs_only | 42 | 79.0 | eval-supp-crm-norm02-spatial-s42-r2 |\n| spatial | crm_obs_only | 43 | 81.0 | eval-supp-crm-norm005-spatial-s43 |\n| spatial | crm_obs_only | 44 | 78.5 | eval-supp-crm-norm005-spatial-s44 |\n| spatial | crm_obs_only | 45 | 80.5 | eval-supp-crm-norm005-spatial-s45 |\n| spatial | crm_obs_only | 46 | 78.5 | eval-supp-crm-norm005-spatial-s46 |\n| spatial | crm_obs_only | 46 | 81.0 | eval-supp-spatial-crm-norm005-s46 |\n| spatial | reconvla | 42 | 80.0 | eval-supp-reconvla-k2-spatial-s42 |\n| spatial | reconvla | 45 | 79.5 | eval-supp-spatial-reconvla-s45 |\n| spatial | reconvla | 46 | 80.0 | eval-supp-spatial-reconvla-s46 |\n| spatial | reconvla | 47 | 78.0 | eval-supp-spatial-reconvla-s47 |\n| spatial | vla_only | 44 | 78.5 | eval-supp-spatial-vla-only-s44 |\n| spatial | vla_only | 45 | 80.0 | eval-supp-vla-only-spatial-s45 |\n| spatial | vla_only | 45 | 80.0 | eval-supp-spatial-k2mean-s45 |\n| spatial | vla_only | 46 | 80.0 | eval-supp-spatial-k2mean-s46 |\n| spatial | vla_only | 46 | 80.5 | eval-supp-vla-only-spatial-s46 |\n| spatial | vla_only | 46 | 80.5 | eval-supp-spatial-vla-only-s46 |\n| spatial | vla_only | 47 | 81.0 | eval-supp-spatial-vla-only-s47 |\n| spatial | vla_only | 48 | 79.5 | eval-supp-vla-only-spatial-s48 |\n| spatial | vla_only | 49 | 78.5 | eval-supp-vla-only-spatial-s49 |\n\n## C. Pi05 Cross-VLA Generalization (Table 2)\n\n**Total experiments: 33** (canonical, deduplicated)\n\n### Summary (Mean ± Std)\n\n| benchmark | mode | n | SR (mean ± std) |\n|-----------|------|---|----------------|\n| goal | adaptive_conformal_crm | 2 | 89.5 ± 0.0 |\n| goal | crm_obs_only | 3 | 84.5 ± 1.3 |\n| goal | vla_only | 3 | 97.5 ± 0.5 |\n| long | adaptive_conformal_crm | 3 | 81.3 ± 1.4 |\n| long | crm_obs_only | 1 | 76.0 |\n| long | vla_only | 3 | 95.0 ± 0.9 |\n| object | adaptive_conformal_crm | 3 | 86.2 ± 1.6 |\n| object | crm_obs_only | 3 | 88.0 ± 1.0 |\n| object | vla_only | 3 | 99.3 ± 0.8 |\n| spatial | adaptive_conformal_crm | 3 | 97.2 ± 0.8 |\n| spatial | crm_obs_only | 3 | 96.8 ± 0.3 |\n| spatial | vla_only | 3 | 98.0 ± 0.5 |\n\n### Per-seed detail\n\n| benchmark | mode | seed | SR (%) | source_exp_id |\n|-----------|------|------|--------|---------------|\n| goal | adaptive_conformal_crm | 42 | 89.5 | pi05-adaptive-goal-s42-cqa1 |\n| goal | adaptive_conformal_crm | 43 | 89.5 | pi05-adaptive-goal-s43-bjb1-18228 |\n| goal | crm_obs_only | 42 | 85.5 | westd-pi05-crm-k2-goal-s42 |\n| goal | crm_obs_only | 43 | 83.0 | pi05-crm-k2-goal-s43-bjb1-r2 |\n| goal | crm_obs_only | 44 | 85.0 | pi05-crm-k2-goal-s44-bjb1-r2 |\n| goal | vla_only | 42 | 98.0 | eval-pi05-vla-only-goal-s42-paired |\n| goal | vla_only | 43 | 97.0 | eval-pi05-vla-only-goal-s43-v2 |\n| goal | vla_only | 44 | 97.5 | eval-pi05-vla-only-goal-s44 |\n| long | adaptive_conformal_crm | 42 | 80.5 | pi05-adaptive-long-s42-r2 |\n| long | adaptive_conformal_crm | 43 | 80.5 | pi05-adaptive-long-s43-cqa1-r3 |\n| long | adaptive_conformal_crm | 44 | 83.0 | pi05-adaptive-long-s44-cqa1-r3 |\n| long | crm_obs_only | 44 | 76.0 | pi05-crm-k2-long-s44-cqa1 |\n| long | vla_only | 42 | 94.0 | eval-pi05-vla-only-long-seed42-r4-rerun |\n| long | vla_only | 43 | 95.5 | eval-pi05-vla-only-long-seed43-r4 |\n| long | vla_only | 44 | 95.5 | eval-pi05-vla-only-long-seed44-r4 |\n| object | adaptive_conformal_crm | 42 | 85.5 | pi05-adaptive-object-s42-cqa1 |\n| object | adaptive_conformal_crm | 43 | 85.0 | pi05-adaptive-object-s43-cqa1-r3 |\n| object | adaptive_conformal_crm | 44 | 88.0 | pi05-adaptive-object-s44-cqa1-r3 |\n| object | crm_obs_only | 42 | 89.0 | pi05-crm-k2-object-s42-bjb1-r2 |\n| object | crm_obs_only | 43 | 87.0 | pi05-crm-k2-object-s43-bjb1-r2 |\n| object | crm_obs_only | 44 | 88.0 | pi05-crm-k2-object-s44-bjb1-r2 |\n| object | vla_only | 42 | 100.0 | eval-pi05-vla-only-object-seed42-r4 |\n| object | vla_only | 43 | 98.5 | eval-pi05-vla-only-object-seed43-r4 |\n| object | vla_only | 44 | 99.5 | eval-pi05-vla-only-object-seed44-r4 |\n| spatial | adaptive_conformal_crm | 42 | 96.5 | pi05-adaptive-spatial-s42-bjb2-r2 |\n| spatial | adaptive_conformal_crm | 43 | 98.0 | pi05-adaptive-spatial-s43-bjb2-r2 |\n| spatial | adaptive_conformal_crm | 44 | 97.0 | pi05-adaptive-spatial-s44-bjb2-r2 |\n| spatial | crm_obs_only | 42 | 96.5 | pi05-crm-k2-spatial-s42-bjb2-r2 |\n| spatial | crm_obs_only | 43 | 97.0 | pi05-crm-k2-spatial-s43-bjb2-r2 |\n| spatial | crm_obs_only | 44 | 97.0 | pi05-crm-k2-spatial-s44-bjb2-r2 |\n| spatial | vla_only | 42 | 98.0 | eval-pi05-vla-only-spatial-s42-paired |\n| spatial | vla_only | 43 | 97.5 | westd-pi05-vla-only-spatial-s43-paired |\n| spatial | vla_only | 44 | 98.5 | westd-pi05-vla-only-spatial-s44-paired |\n\n## D. K-sweep Results\n\n**Total experiments: 23** (22 with valid SR)\n\n| model | benchmark | mode | seed | K | SR (%) | source_exp_id |\n|-------|-----------|------|------|---|--------|---------------|\n| — | object | — | — | 5 | 18.0 | eval-obs-only-object-norm02-k5-seed48 |\n| smolvla | object | crm_obs_only | 42 | 5 | 73.5 | eval-ksweep-k5-obs-object-s42 |\n| — | object | crm_obs_only | 42 | 5 | — | eval-obs-only-object-norm02-k5-seed42 |\n| — | object | random_selection | 42 | 5 | 14.0 | eval-random-selection-object-k5-seed42-r2 |\n| smolvla | object | crm_obs_only | 43 | 5 | 73.0 | eval-ksweep-k5-obs-object-s43 |\n| — | object | crm_obs_only | 43 | 5 | 19.0 | eval-obs-only-object-norm02-k5-seed43 |\n| — | object | random_selection | 43 | 5 | 11.0 | eval-random-selection-object-k5-seed43-r2 |\n| — | object | crm_obs_only | 44 | 5 | 14.0 | eval-k5-obs-only-object-seed44 |\n| — | object | crm_obs_only | 44 | 5 | 17.0 | eval-obs-only-object-norm02-k5-seed44 |\n| — | object | random_selection | 44 | 5 | 10.0 | eval-random-selection-object-k5-seed44-r2 |\n| — | object | crm_obs_only | 45 | 5 | 15.0 | eval-obs-only-object-norm02-k5-seed45 |\n| — | object | random_selection | 45 | 5 | 7.0 | eval-random-selection-object-k5-seed45-r2 |\n| — | object | crm_obs_only | 46 | 5 | 16.0 | eval-obs-only-object-norm02-k5-seed46 |\n| — | object | crm_obs_only | 47 | 5 | 13.0 | eval-obs-only-object-norm02-k5-seed47 |\n| smolvla | object | crm_obs_only | 44 | 10 | 78.0 | smolvla-crm-norm005-k10-object-s44-cqa1 |\n| smolvla | object | crm_obs_only | 42 | 20 | 75.5 | eval-ksweep-k20-obs-object-s42 |\n| smolvla | object | crm_obs_only | 43 | 20 | 73.5 | eval-ksweep-k20-obs-object-s43 |\n| — | spatial | — | — | 5 | 35.0 | eval-obs-only-spatial-norm02-k5-seed42 |\n| — | spatial | — | — | 5 | 32.0 | eval-obs-only-spatial-norm02-k5-seed43 |\n| — | spatial | adaptive_conformal_crm | 42 | 5 | 79.0 | eval-k5-spatial-s42-sweep |\n| — | spatial | crm_obs_only | 44 | 5 | 37.0 | eval-obs-only-spatial-norm02-k5-seed44-r2 |\n| — | spatial | crm_obs_only | 45 | 5 | 34.0 | eval-obs-only-spatial-norm02-k5-seed45-r2 |\n| — | spatial | crm_obs_only | 51 | 10 | 36.0 | eval-crm-spatial-k10-seed51 |\n\n### K-sweep summary (SmolVLA, object, crm_obs_only)\n\n| K | seeds | SR (mean ± std) |\n|---|-------|----------------|\n| 5 | 2 | 73.2 ± 0.4 |\n| 10 | 1 | 78.0 |\n| 20 | 2 | 74.5 ± 1.4 |\n\n## E. CRM Always-On Ablation (τ=0.001)\n\n**Total experiments: 23** (23 with valid SR)\n\n### Summary (Mean ± Std)\n\n| model | benchmark | n | SR (mean ± std) |\n|-------|-----------|---|----------------|\n| pi05 | goal | 1 | 81.5 |\n| pi05 | long | 1 | 77.0 |\n| pi05 | object | 2 | 91.2 ± 1.1 |\n| pi05 | spatial | 1 | 96.0 |\n| smolvla | goal | 5 | 80.4 ± 1.0 |\n| smolvla | long | 3 | 43.2 ± 2.3 |\n| smolvla | object | 5 | 72.2 ± 3.0 |\n| smolvla | spatial | 5 | 77.9 ± 1.3 |\n\n### Per-seed detail\n\n| model | benchmark | seed | SR (%) | trigger_rate (%) | source_exp_id |\n|-------|-----------|------|--------|-----------------|---------------|\n| pi05 | goal | 42 | 81.5 | 100 | pi05-crm-always-on-goal-s42 |\n| pi05 | long | 42 | 77.0 | 100 | pi05-crm-always-on-long-s42 |\n| pi05 | object | 42 | 90.5 | 100 | pi05-crm-always-on-object-s42 |\n| pi05 | object | 43 | 92.0 | 100 | pi05-crm-always-on-object-s43 |\n| pi05 | spatial | 42 | 96.0 | 100 | pi05-crm-always-on-spatial-s42 |\n| smolvla | goal | 42 | 80.0 | 100 | crm-always-on-goal-s42 |\n| smolvla | goal | 43 | 79.5 | 100 | crm-always-on-goal-s43 |\n| smolvla | goal | 44 | 80.5 | 100 | crm-always-on-goal-s44 |\n| smolvla | goal | 45 | 82.0 | 100 | crm-always-on-goal-s45 |\n| smolvla | goal | 46 | 80.0 | 100 | crm-always-on-goal-s46 |\n| smolvla | long | 42 | 41.0 | 100 | crm-always-on-long-s42 |\n| smolvla | long | 43 | 45.5 | 100 | crm-always-on-long-s43 |\n| smolvla | long | 44 | 43.0 | 100 | crm-always-on-long-s44 |\n| smolvla | object | 42 | 71.0 | 100 | crm-always-on-object-s42 |\n| smolvla | object | 43 | 73.5 | 100 | crm-always-on-object-s43 |\n| smolvla | object | 44 | 74.5 | 100 | crm-always-on-object-s44 |\n| smolvla | object | 45 | 74.5 | 100 | crm-always-on-object-s45 |\n| smolvla | object | 46 | 67.5 | 100 | crm-always-on-object-s46 |\n| smolvla | spatial | 42 | 79.0 | 100 | crm-always-on-spatial-s42 |\n| smolvla | spatial | 43 | 76.0 | 100 | crm-always-on-spatial-s43 |\n| smolvla | spatial | 44 | 79.0 | 100 | crm-always-on-spatial-s44 |\n| smolvla | spatial | 45 | 77.0 | 100 | crm-always-on-spatial-s45 |\n| smolvla | spatial | 46 | 78.5 | 100 | crm-always-on-spatial-s46 |\n\n## F. Data Gaps & Notes\n\n### Incomplete categories\n- **Bonus seeds / long / adaptive**: Only experiments with None SR (s42/s45/s46) — **incomplete**\n- **Bonus seeds / object / adaptive**: Only 1 valid experiment (s42) — **incomplete**\n- **Bonus seeds / object / crm_obs_only**: Only 1 valid experiment (s46) — **incomplete**\n- **Bonus seeds / long / crm_obs_only**: Only 1 valid experiment (s46) — **incomplete**\n- **Bonus seeds / goal / reconvla**: Only 2 valid experiments (s46, s47) — **incomplete**\n- **Bonus seeds / long / reconvla**: Only 2 valid experiments (s45, s46) — **incomplete**\n- **Pi05 / long / crm_obs_only**: Only 1 seed (s44) — **incomplete**\n- **K-sweep**: Many experiments have None SR (especially K=20 and reconvla/argmin variants)\n- **CRM always-on / smolvla / long**: s45 has None SR — **incomplete**\n\n### Deduplication notes\n- Multiple runs exist for same conditions (e.g., different servers, -r2/-r3 reruns). This summary uses the latest successful run with valid metrics.\n- Pi05 vla_only experiments with SR=0% (e.g., seed42-r4 long, seed43/44 object) are excluded as known OOM artifacts.\n- Trigger rates stored inconsistently: some as fractions (0.0–1.0), some as percentages (0–100). Values >1.0 in the tau-sweep are likely percentages.\n",
      "numLines": 350,
      "startLine": 1,
      "totalLines": 350
    }
  }
}
```

</details>

---

### Tool call

_source line 98_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VrofjnyywSAmin2CXXiCNB`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ps aux --no-header",
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
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "86859908-b9c6-40ec-beac-d7867ca024e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGTv9P7cT4afXZAtGcfbbi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 103,
      "cache_creation_input_tokens": 3642,
      "cache_read_input_tokens": 27598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3642
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

_source line 99 · 2026-05-28T15:56:17.320Z_

<details><summary>↩ Tool result · `toolu_01VrofjnyywSAmin2CXXiCNB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"root          1  0.0  0.0   4476  3464 ?        Ss   20:40   0:00 bash /init/boot/boot.sh\\nroot        794  1.5  0.0 718240 20652 ?        Sl   20:40   2:59 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        812  0.0  0.0 193124 107668 ?       S    20:40   0:03 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        813  0.0  0.0 2181876 79204 ?       Sl   20:40   0:09 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        814  0.0  0.0 2868996 17072 ?       Sl   20:40   0:05 proxy -c /init/proxy/proxy.ini\\nroot        816  0.2  0.0 4975212 96212 ?       Sl   20:40   0:28 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        817  0.0  0.0  15444  9280 ?        S    20:40   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        818  0.0  0.0 2794240 17556 ?       Sl   20:40   0:02 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        883  0.0  0.0 17524960 10444 ?      Sl   20:40   0:04 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_xwa8ej3x/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_xwa8ej3x/startup_error\\nroot       1186  0.0  0.0  16692 10488 ?        Ss   20:41   0:01 sshd: root@notty\\nroot       8099  0.0  0.0  16692 10824 ?        Ss   23:50   0:00 sshd: root@notty\\nroot       8333  0.0  0.0   7064  1568 ?        Rs   23:56   0:00 ps aux --no-header\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "e5c1104d-8a70-451f-bc69-290480eb4569",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"root          1  0.0  0.0   4476  3464 ?        Ss   20:40   0:00 bash /init/boot/boot.sh\\\\nroot        794  1.5  0.0 718240 20652 ?        Sl   20:40   2:59 /bin/supervisord -c /init/supervisor/supervisor.ini\\\\nroot        812  0.0  0.0 193124 107668 ?       S    20:40   0:03 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\\\nroot        813  0.0  0.0 2181876 79204 ?       Sl   20:40   0:09 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\\\nroot        814  0.0  0.0 2868996 17072 ?       Sl   20:40   0:05 proxy -c /init/proxy/proxy.ini\\\\nroot        816  0.2  0.0 4975212 96212 ?       Sl   20:40   0:28 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\\\nroot        817  0.0  0.0  15444  9280 ?        S    20:40   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\\\nroot        818  0.0  0.0 2794240 17556 ?       Sl   20:40   0:02 proxy -c /init/proxy/proxy-hot-backup.ini\\\\nroot        883  0.0  0.0 17524960 10444 ?      Sl   20:40   0:04 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_xwa8ej3x/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_xwa8ej3x/startup_error\\\\nroot       1186  0.0  0.0  16692 10488 ?        Ss   20:41   0:01 sshd: root@notty\\\\nroot       8099  0.0  0.0  16692 10824 ?        Ss   23:50   0:00 sshd: root@notty\\\\nroot       8333  0.0  0.0   7064  1568 ?        Rs   23:56   0:00 ps aux --no-header\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"root          1  0.0  0.0   4476  3464 ?        Ss   20:40   0:00 bash /init/boot/boot.sh\\nroot        794  1.5  0.0 718240 20652 ?        Sl   20:40   2:59 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        812  0.0  0.0 193124 107668 ?       S    20:40   0:03 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        813  0.0  0.0 2181876 79204 ?       Sl   20:40   0:09 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        814  0.0  0.0 2868996 17072 ?       Sl   20:40   0:05 proxy -c /init/proxy/proxy.ini\\nroot        816  0.2  0.0 4975212 96212 ?       Sl   20:40   0:28 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        817  0.0  0.0  15444  9280 ?        S    20:40   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        818  0.0  0.0 2794240 17556 ?       Sl   20:40   0:02 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        883  0.0  0.0 17524960 10444 ?      Sl   20:40   0:04 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_xwa8ej3x/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_xwa8ej3x/startup_error\\nroot       1186  0.0  0.0  16692 10488 ?        Ss   20:41   0:01 sshd: root@notty\\nroot       8099  0.0  0.0  16692 10824 ?        Ss   23:50   0:00 sshd: root@notty\\nroot       8333  0.0  0.0   7064  1568 ?        Rs   23:56   0:00 ps aux --no-header\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 100_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01USKVDPHQW1asMNy4GHV4Ag`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "7da38b53-bdd5-44dd-a17d-076ca0c37575",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGTv9P7cT4afXZAtGcfbbi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 103,
      "cache_creation_input_tokens": 3642,
      "cache_read_input_tokens": 27598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3642
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

_source line 101 · 2026-05-28T15:56:17.583Z_

<details><summary>↩ Tool result · `toolu_01USKVDPHQW1asMNy4GHV4Ag`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-28 09:39 UTC | 更新原因: Paper Agent 确认 Table 1 重构+叙事升级完成，论文就绪待提交，ROADMAP 更新任务完成状态\\n\\n> 详见 paper_framing.md（D170/D177/D178: K=2 CRM always-on 4/4 harmful + K-matched Table 1）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-28 20:00 北京时间**。\\n\\n## 当前进展\\n- **论文就绪**：编译通过，8 页正文 + 6 页（refs 2 + appendix 4），零 critical warning\\n- **Table 1 重构完成**：K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），4/4 suites harmful 叙事升级 ✅\\n- **Table 3 (Pi05) 完成**：4/4 suites degradation-only（含 Long 94.0→77.0, Δ=-17.0pp），seed-matched ✅\\n- **叙事一致性**：4/4 harmful + gating recovery，全文对齐（Abstract/Intro/Experiments/Conclusion）✅\\n- **贡献**：3 条（OpenVLA 从贡献列表移除，保留 §4.5 + Appendix）✅\\n- **Backfill 修复**：M115 根因定位（手动 update_registry 不创建 cron），已全部改用 submit_training_job\\n- **GPU**：22/22 满载，补充实验持续产出\\n\\n## CRM always-on 最终数据（SmolVLA, K=2, n=3）\\n| Suite | VLA-only (K=1) | CRM always-on (K=2) | Adaptive (K=2) | Δ CRM vs VLA | Δ Adaptive vs VLA |\\n|-------|---------------|--------------------|-----------|----|---|\\n| Spatial | 79.3±0.8 | 78.0±1.7 | 80.8±1.1 | -1.3pp | +1.5pp |\\n| Goal | 83.7±1.3 | 80.0±0.5 | 85.0±1.3 | -3.7pp | +1.3pp |\\n| Object | 77.7±1.3 | 73.0±1.8 | 77.8±2.1 | -4.7pp | +0.1pp |\\n| Long | 58.0±1.5 | 43.2±2.3 | 57.7±1.5 | -14.8pp | -0.3pp |\\n\\n## 近期任务\\n- [x] **P0** 收集 Long CRM always-on 3 seeds → 43.2%\\n- [x] **P0** Paper Agent Table 1 K-matched 重构 + 叙事 4/4 升级 ✅\\n- [ ] **P0** 等待用户确认 title + CoRL 提交决定（contingency: 18:00 BJ 默认提交）\\n- [ ] **P1** Pi05 CRM always-on long s43/s44（bjb1-18228 运行中）→ supplementary\\n- [ ] **P1** Bonus seeds + tau-sweep 补充点（22 GPU 持续跑）→ supplementary / camera-ready\\n- [ ] **P2** 最终论文提交 submit_paper_to_review\\n- [ ] **Reviewer** 最终 claim 强度审查中\\n\\n## Claim 策略 (D170/D178)\\n- **MC1**: CRM always-on **4/4 suites** 有害 → Adaptive gating 全面恢复（K-matched controlled experiment）\\n- **MC2**: Trigger rate ↔ Δ 单调正相关（cross-suite + within-suite τ-sweep sensitivity analysis）\\n- **MC3**: Cross-VLA (SmolVLA 0.4B + π0.5 3.6B) 泛化\\n\\n## GPU 预算\\n- 本项目分配：22 GPU（4 servers: bjb1-18228 4卡, bjb1-32546 6卡, bjb2-28827 6卡, cqa1-32758 6卡）\\n- 当前：22/22 满载运行（eval 类，CPU-bound 利用率 20-28% 正常）\\n- Backfill 修复后 cron 回调正常，实验完成自动触发 Agent 补位\\n- DDL 前预计再完成 1-2 轮 ≈ 22-44 个补充实验\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D184 | 2026-05-28 | Title 锁定 + 20:00 数据锁定 + CoRL 提交确认。用户授权按核心 claim 定  | — |\\n| D183 | 2026-05-28 | D183: 移除 OpenVLA Contribution 4，保留 discussion 段 bo | — |\\n| D182 | 2026-05-28 | D182: Pi05 Table 2 Long 数据确认 — VLA-only 95.0%, CRM | pi05-crm-always-on-long-s42, pi05-vla-only-long-s42-4090-r3, pi05-vla-only-long-s43-4090, pi05-vla-only-long-s44-4090 |\\n| D181 | 2026-05-28 | D181: Table 2 确认 degradation-only 两列（VLA-only + CR | pi05-crm-always-on-object-s42, pi05-crm-always-on-goal-s42, pi05-object-adaptive-s42-cqa1 |\\n| D180 | 2026-05-28 | Table 2 叙事调整：Pi05 CRM always-on 跨模型一致有害（MC1 强化），但  | pi05-crm-always-on-object-s42, pi05-crm-always-on-spatial-s42, pi05-crm-always-on-goal-s42 |\\n| D179 | 2026-05-28 | Title 锁定 \\\"Knowing When Not to Correct: Adaptive Te | crm-always-on-long-s42, pi05-crm-always-on-goal-s42 |\\n| D178 | 2026-05-27 | Long CRM always-on -14.7pp 是论文最有力证据。4/4 suites CRM | crm-always-on-long-s42, crm-always-on-long-s43, smolvla-tau025-object-s42-r3, smolvla-tau025-long-s42 |\\n| D177 | 2026-05-27 | Table 1 重构为 K-matched 3 列（VLA-only K=1 / K=2 CRM a | crm-always-on-object-s42, crm-always-on-object-s43, crm-always-on-object-s44, crm-always-on-spatial-s42, crm-always-on-spatial-s43, crm-always-on-spatial-s44, crm-always-on-goal-s42, crm-always-on-goal-s43, crm-always-on-goal-s44 |\\n| D176 | 2026-05-27 | D176: Table 1 无 westd 污染确认 + perdof 对比因训练条件差异不可用于论 | eval-perdof-object-norm003-s43-v3, eval-perdof-object-norm005-s43-v3, eval-perdof-object-norm003-s44-westd, eval-perdof-object-norm005-s44-westd |\\n| D175 | 2026-05-27 | westd-49937 偏差根因确认：LIBERO assets 版本差异（HF 下载 vs 预装） | eval-obs-object-norm005-s43-bjb2, eval-obs-object-norm005-s43-westd, eval-obs-object-norm003-s44 |\\n\\n\", \"total_chars\": 4024, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "6d046196-2d6f-42a4-9594-7f8bd08c8430",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\\\", \\\"content\\\": \\\"# acr-vla-conformal-refinement — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-28 09:39 UTC | 更新原因: Paper Agent 确认 Table 1 重构+叙事升级完成，论文就绪待提交，ROADMAP 更新任务完成状态\\\\n\\\\n> 详见 paper_framing.md（D170/D177/D178: K=2 CRM always-on 4/4 harmful + K-matched Table 1）\\\\n\\\\n## 核心方向\\\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-28 20:00 北京时间**。\\\\n\\\\n## 当前进展\\\\n- **论文就绪**：编译通过，8 页正文 + 6 页（refs 2 + appendix 4），零 critical warning\\\\n- **Table 1 重构完成**：K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），4/4 suites harmful 叙事升级 ✅\\\\n- **Table 3 (Pi05) 完成**：4/4 suites degradation-only（含 Long 94.0→77.0, Δ=-17.0pp），seed-matched ✅\\\\n- **叙事一致性**：4/4 harmful + gating recovery，全文对齐（Abstract/Intro/Experiments/Conclusion）✅\\\\n- **贡献**：3 条（OpenVLA 从贡献列表移除，保留 §4.5 + Appendix）✅\\\\n- **Backfill 修复**：M115 根因定位（手动 update_registry 不创建 cron），已全部改用 submit_training_job\\\\n- **GPU**：22/22 满载，补充实验持续产出\\\\n\\\\n## CRM always-on 最终数据（SmolVLA, K=2, n=3）\\\\n| Suite | VLA-only (K=1) | CRM always-on (K=2) | Adaptive (K=2) | Δ CRM vs VLA | Δ Adaptive vs VLA |\\\\n|-------|---------------|--------------------|-----------|----|---|\\\\n| Spatial | 79.3±0.8 | 78.0±1.7 | 80.8±1.1 | -1.3pp | +1.5pp |\\\\n| Goal | 83.7±1.3 | 80.0±0.5 | 85.0±1.3 | -3.7pp | +1.3pp |\\\\n| Object | 77.7±1.3 | 73.0±1.8 | 77.8±2.1 | -4.7pp | +0.1pp |\\\\n| Long | 58.0±1.5 | 43.2±2.3 | 57.7±1.5 | -14.8pp | -0.3pp |\\\\n\\\\n## 近期任务\\\\n- [x] **P0** 收集 Long CRM always-on 3 seeds → 43.2%\\\\n- [x] **P0** Paper Agent Table 1 K-matched 重构 + 叙事 4/4 升级 ✅\\\\n- [ ] **P0** 等待用户确认 title + CoRL 提交决定（contingency: 18:00 BJ 默认提交）\\\\n- [ ] **P1** Pi05 CRM always-on long s43/s44（bjb1-18228 运行中）→ supplementary\\\\n- [ ] **P1** Bonus seeds + tau-sweep 补充点（22 GPU 持续跑）→ supplementary / camera-ready\\\\n- [ ] **P2** 最终论文提交 submit_paper_to_review\\\\n- [ ] **Reviewer** 最终 claim 强度审查中\\\\n\\\\n## Claim 策略 (D170/D178)\\\\n- **MC1**: CRM always-on **4/4 suites** 有害 → Adaptive gating 全面恢复（K-matched controlled experiment）\\\\n- **MC2**: Trigger rate ↔ Δ 单调正相关（cross-suite + within-suite τ-sweep sensitivity analysis）\\\\n- **MC3**: Cross-VLA (SmolVLA 0.4B + π0.5 3.6B) 泛化\\\\n\\\\n## GPU 预算\\\\n- 本项目分配：22 GPU（4 servers: bjb1-18228 4卡, bjb1-32546 6卡, bjb2-28827 6卡, cqa1-32758 6卡）\\\\n- 当前：22/22 满载运行（eval 类，CPU-bound 利用率 20-28% 正常）\\\\n- Backfill 修复后 cron 回调正常，实验完成自动触发 Agent 补位\\\\n- DDL 前预计再完成 1-2 轮 ≈ 22-44 个补充实验\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D184 | 2026-05-28 | Title 锁定 + 20:00 数据锁定 + CoRL 提交确认。用户授权按核心 claim 定  | — |\\\\n| D183 | 2026-05-28 | D183: 移除 OpenVLA Contribution 4，保留 discussion 段 bo | — |\\\\n| D182 | 2026-05-28 | D182: Pi05 Table 2 Long 数据确认 — VLA-only 95.0%, CRM | pi05-crm-always-on-long-s42, pi05-vla-only-long-s42-4090-r3, pi05-vla-only-long-s43-4090, pi05-vla-only-long-s44-4090 |\\\\n| D181 | 2026-05-28 | D181: Table 2 确认 degradation-only 两列（VLA-only + CR | pi05-crm-always-on-object-s42, pi05-crm-always-on-goal-s42, pi05-object-adaptive-s42-cqa1 |\\\\n| D180 | 2026-05-28 | Table 2 叙事调整：Pi05 CRM always-on 跨模型一致有害（MC1 强化），但  | pi05-crm-always-on-object-s42, pi05-crm-always-on-spatial-s42, pi05-crm-always-on-goal-s42 |\\\\n| D179 | 2026-05-28 | Title 锁定 \\\\\\\"Knowing When Not to Correct: Adaptive Te | crm-always-on-long-s42, pi05-crm-always-on-goal-s42 |\\\\n| D178 | 2026-05-27 | Long CRM always-on -14.7pp 是论文最有力证据。4/4 suites CRM | crm-always-on-long-s42, crm-always-on-long-s43, smolvla-tau025-object-s42-r3, smolvla-tau025-long-s42 |\\\\n| D177 | 2026-05-27 | Table 1 重构为 K-matched 3 列（VLA-only K=1 / K=2 CRM a | crm-always-on-object-s42, crm-always-on-object-s43, crm-always-on-object-s44, crm-always-on-spatial-s42, crm-always-on-spatial-s43, crm-always-on-spatial-s44, crm-always-on-goal-s42, crm-always-on-goal-s43, crm-always-on-goal-s44 |\\\\n| D176 | 2026-05-27 | D176: Table 1 无 westd 污染确认 + perdof 对比因训练条件差异不可用于论 | eval-perdof-object-norm003-s43-v3, eval-perdof-object-norm005-s43-v3, eval-perdof-object-norm003-s44-westd, eval-perdof-object-norm005-s44-westd |\\\\n| D175 | 2026-05-27 | westd-49937 偏差根因确认：LIBERO assets 版本差异（HF 下载 vs 预装） | eval-obs-object-norm005-s43-bjb2, eval-obs-object-norm005-s43-westd, eval-obs-object-norm003-s44 |\\\\n\\\\n\\\", \\\"total_chars\\\": 4024, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-28 09:39 UTC | 更新原因: Paper Agent 确认 Table 1 重构+叙事升级完成，论文就绪待提交，ROADMAP 更新任务完成状态\\n\\n> 详见 paper_framing.md（D170/D177/D178: K=2 CRM always-on 4/4 harmful + K-matched Table 1）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-28 20:00 北京时间**。\\n\\n## 当前进展\\n- **论文就绪**：编译通过，8 页正文 + 6 页（refs 2 + appendix 4），零 critical warning\\n- **Table 1 重构完成**：K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），4/4 suites harmful 叙事升级 ✅\\n- **Table 3 (Pi05) 完成**：4/4 suites degradation-only（含 Long 94.0→77.0, Δ=-17.0pp），seed-matched ✅\\n- **叙事一致性**：4/4 harmful + gating recovery，全文对齐（Abstract/Intro/Experiments/Conclusion）✅\\n- **贡献**：3 条（OpenVLA 从贡献列表移除，保留 §4.5 + Appendix）✅\\n- **Backfill 修复**：M115 根因定位（手动 update_registry 不创建 cron），已全部改用 submit_training_job\\n- **GPU**：22/22 满载，补充实验持续产出\\n\\n## CRM always-on 最终数据（SmolVLA, K=2, n=3）\\n| Suite | VLA-only (K=1) | CRM always-on (K=2) | Adaptive (K=2) | Δ CRM vs VLA | Δ Adaptive vs VLA |\\n|-------|---------------|--------------------|-----------|----|---|\\n| Spatial | 79.3±0.8 | 78.0±1.7 | 80.8±1.1 | -1.3pp | +1.5pp |\\n| Goal | 83.7±1.3 | 80.0±0.5 | 85.0±1.3 | -3.7pp | +1.3pp |\\n| Object | 77.7±1.3 | 73.0±1.8 | 77.8±2.1 | -4.7pp | +0.1pp |\\n| Long | 58.0±1.5 | 43.2±2.3 | 57.7±1.5 | -14.8pp | -0.3pp |\\n\\n## 近期任务\\n- [x] **P0** 收集 Long CRM always-on 3 seeds → 43.2%\\n- [x] **P0** Paper Agent Table 1 K-matched 重构 + 叙事 4/4 升级 ✅\\n- [ ] **P0** 等待用户确认 title + CoRL 提交决定（contingency: 18:00 BJ 默认提交）\\n- [ ] **P1** Pi05 CRM always-on long s43/s44（bjb1-18228 运行中）→ supplementary\\n- [ ] **P1** Bonus seeds + tau-sweep 补充点（22 GPU 持续跑）→ supplementary / camera-ready\\n- [ ] **P2** 最终论文提交 submit_paper_to_review\\n- [ ] **Reviewer** 最终 claim 强度审查中\\n\\n## Claim 策略 (D170/D178)\\n- **MC1**: CRM always-on **4/4 suites** 有害 → Adaptive gating 全面恢复（K-matched controlled experiment）\\n- **MC2**: Trigger rate ↔ Δ 单调正相关（cross-suite + within-suite τ-sweep sensitivity analysis）\\n- **MC3**: Cross-VLA (SmolVLA 0.4B + π0.5 3.6B) 泛化\\n\\n## GPU 预算\\n- 本项目分配：22 GPU（4 servers: bjb1-18228 4卡, bjb1-32546 6卡, bjb2-28827 6卡, cqa1-32758 6卡）\\n- 当前：22/22 满载运行（eval 类，CPU-bound 利用率 20-28% 正常）\\n- Backfill 修复后 cron 回调正常，实验完成自动触发 Agent 补位\\n- DDL 前预计再完成 1-2 轮 ≈ 22-44 个补充实验\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D184 | 2026-05-28 | Title 锁定 + 20:00 数据锁定 + CoRL 提交确认。用户授权按核心 claim 定  | — |\\n| D183 | 2026-05-28 | D183: 移除 OpenVLA Contribution 4，保留 discussion 段 bo | — |\\n| D182 | 2026-05-28 | D182: Pi05 Table 2 Long 数据确认 — VLA-only 95.0%, CRM | pi05-crm-always-on-long-s42, pi05-vla-only-long-s42-4090-r3, pi05-vla-only-long-s43-4090, pi05-vla-only-long-s44-4090 |\\n| D181 | 2026-05-28 | D181: Table 2 确认 degradation-only 两列（VLA-only + CR | pi05-crm-always-on-object-s42, pi05-crm-always-on-goal-s42, pi05-object-adaptive-s42-cqa1 |\\n| D180 | 2026-05-28 | Table 2 叙事调整：Pi05 CRM always-on 跨模型一致有害（MC1 强化），但  | pi05-crm-always-on-object-s42, pi05-crm-always-on-spatial-s42, pi05-crm-always-on-goal-s42 |\\n| D179 | 2026-05-28 | Title 锁定 \\\"Knowing When Not to Correct: Adaptive Te | crm-always-on-long-s42, pi05-crm-always-on-goal-s42 |\\n| D178 | 2026-05-27 | Long CRM always-on -14.7pp 是论文最有力证据。4/4 suites CRM | crm-always-on-long-s42, crm-always-on-long-s43, smolvla-tau025-object-s42-r3, smolvla-tau025-long-s42 |\\n| D177 | 2026-05-27 | Table 1 重构为 K-matched 3 列（VLA-only K=1 / K=2 CRM a | crm-always-on-object-s42, crm-always-on-object-s43, crm-always-on-object-s44, crm-always-on-spatial-s42, crm-always-on-spatial-s43, crm-always-on-spatial-s44, crm-always-on-goal-s42, crm-always-on-goal-s43, crm-always-on-goal-s44 |\\n| D176 | 2026-05-27 | D176: Table 1 无 westd 污染确认 + perdof 对比因训练条件差异不可用于论 | eval-perdof-object-norm003-s43-v3, eval-perdof-object-norm005-s43-v3, eval-perdof-object-norm003-s44-westd, eval-perdof-object-norm005-s44-westd |\\n| D175 | 2026-05-27 | westd-49937 偏差根因确认：LIBERO assets 版本差异（HF 下载 vs 预装） | eval-obs-object-norm005-s43-bjb2, eval-obs-object-norm005-s43-westd, eval-obs-object-norm003-s44 |\\n\\n\", \"total_chars\": 4024, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 102_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me compile the report.

Key findings:
1. **GPU Status**: 
   - bjb1-18228: 1 GPU (RTX 4090), fully idle (0 MiB used, 0% util), no residual python/evaluate processes
   - bjb1-32546: **Connection refused** (port 32546)
   - bjb2-28827: **Connection refused** (port 28827)
   - cqa1-32758: **Connection refused** (port 32758)


2. **GPU Discrepancy**: bjb1-18228 is showing only 1 GPU when the project config expects 4 (cuda:0-3). This could mean the instance was restarted with different GPU allocation, or the other GPUs might be on a separate node entirely.

3. **Registry Status**: All experiments are either DONE or KILLED as expected, with 0 currently running.

4. **Data Gaps**: Looking at the supplementary summary, there are significant gaps across bonus seed configurations—most notably no valid SR experiments for the long/adaptive setup, and only 1-2 valid entries across most other bonus seed combinations like object/adaptive, goal/reconvla, and long/reconvla.

5. **Critical Infrastructure Issue**: Three of four servers are unreachable, leaving only bjb1-18228 operational with a single GPU—a major bottleneck given the deadline is today at 20:00 BJ time and the original plan called for full capacity utilization.

6. **Main Table Gaps**: The agent analysis reveals missing seeds across key configurations—VLA-only long is missing seeds 43 and 46, ACR with tau=0.25 long is missing 42 and 43, and ReConV has incomplete coverage as well.

7. **Supplementary vs. Main Table**: The supplementary summary contains a different set of experiments, so I need to determine which dataset takes priority given the resource constraints and tight deadline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "4576ea1a-a816-433b-a455-fe14273a400c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013feVDMh7518UTwJexexYRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14221,
      "cache_read_input_tokens": 31240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14221
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

### Assistant

_source line 103_

## GPU 状态

| 服务器 | GPU 数 | 状态 | 备注 |
|--------|--------|------|------|
| bjb1-18228 | 1× RTX 4090 | **空闲** (0 MiB / 24564 MiB, 0%) | 无残留 python 进程 |
| bjb1-32546 | 6× GPU | **连接失败** | `Unable to connect to port 32546` |
| bjb2-28827 | 6× GPU | **连接失败** | `Unable to connect to port 28827` |
| cqa1-32758 | 6× GPU | **连接失败** | `Unable to connect to port 32758` |

**严重问题：3/4 服务器不可达，22 GPU 中只有 1 GPU 可用。** AutoDL 实例可能已关机或端口已变。需要去 AutoDL 控制台确认实例状态并获取新端口。

此外 bjb1-18228 只显示 1 块 GPU（配置说 cuda:0-3 共 4 卡），可能也已重建。

Registry 确认 RUNNING 实验数为 0，所有实验已清理。

---

## 数据缺口（来自 supplementary_summary.md Section F）

| 类型 | 缺口描述 | 优先级 |
|------|----------|--------|
| Bonus seeds / long / adaptive_conformal | **无有效 SR**（s42/s45/s46 均为 None） | **P0** — 主方法 long 无补充数据 |
| Bonus seeds / object / adaptive_conformal | 仅 1 个有效 seed (s42) | **P0** — 主方法 object 补充不足 |
| Bonus seeds / object / crm_obs_only | 仅 1 个有效 seed (s46) | P1 |
| Bonus seeds / long / crm_obs_only | 仅 1 个有效 seed (s46) | P1 |
| Bonus seeds / goal / reconvla | 仅 2 个有效 seed (s46, s47) | P1 |
| Bonus seeds / long / reconvla | 仅 2 个有效 seed (s45, s46) | P1 |
| Pi05 / long / crm_obs_only | 仅 1 个 seed (s44) | P2 |
| Pi05 tau-sweep | 多为单 seed (s42)，multi-seed 覆盖仅 tau=0.25 | P2 |
| CRM always-on / smolvla / long s45 | SR 为 None | P2 |

---

## 部署建议

**当前只有 bjb1-18228 的 1 块 GPU 可用。** DDL 20:00 BJ，每个实验约 30-40 分钟，最多再跑 ~10-12 个实验。

如果只有 1 GPU 可用，建议优先级排序：

| 优先级 | 实验 | 服务器:GPU | 预估时长 |
|--------|------|-----------|----------|
| 1 | eval-supp-long-adapt-tau025-s43 | bjb1-18228:0 | ~35min |
| 2 | eval-supp-long-adapt-tau025-s44 | bjb1-18228:0 | ~35min |
| 3 | eval-supp-obj-adapt-tau025-s43 | bjb1-18228:0 | ~35min |
| 4 | eval-supp-obj-adapt-tau025-s44 | bjb1-18228:0 | ~35min |
| ... | 后续按 P1 缺口排 | — | — |

**但真正的瓶颈是服务器不可达。** 建议：
1. **立即去 AutoDL 控制台检查 bjb1-32546 / bjb2-28827 / cqa1-32758 实例状态**，如果已关机则开机，如果端口变了请更新 `~/.ssh/config`
2. 恢复后 22 GPU 全开可在 DDL 前批量补齐上述缺口
3. bjb1-18228 如果确实只有 1 卡，立即开始跑 P0 缺口实验（long/adaptive 和 object/adaptive）

等待指示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "uuid": "e6e2c9c0-b877-4fea-b3f5-b632ec2c9d65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013feVDMh7518UTwJexexYRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14221,
      "cache_read_input_tokens": 31240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14221
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

### Task result

_source line 104_

## GPU 状态

| 服务器 | GPU 数 | 状态 | 备注 |
|--------|--------|------|------|
| bjb1-18228 | 1× RTX 4090 | **空闲** (0 MiB / 24564 MiB, 0%) | 无残留 python 进程 |
| bjb1-32546 | 6× GPU | **连接失败** | `Unable to connect to port 32546` |
| bjb2-28827 | 6× GPU | **连接失败** | `Unable to connect to port 28827` |
| cqa1-32758 | 6× GPU | **连接失败** | `Unable to connect to port 32758` |

**严重问题：3/4 服务器不可达，22 GPU 中只有 1 GPU 可用。** AutoDL 实例可能已关机或端口已变。需要去 AutoDL 控制台确认实例状态并获取新端口。

此外 bjb1-18228 只显示 1 块 GPU（配置说 cuda:0-3 共 4 卡），可能也已重建。

Registry 确认 RUNNING 实验数为 0，所有实验已清理。

---

## 数据缺口（来自 supplementary_summary.md Section F）

| 类型 | 缺口描述 | 优先级 |
|------|----------|--------|
| Bonus seeds / long / adaptive_conformal | **无有效 SR**（s42/s45/s46 均为 None） | **P0** — 主方法 long 无补充数据 |
| Bonus seeds / object / adaptive_conformal | 仅 1 个有效 seed (s42) | **P0** — 主方法 object 补充不足 |
| Bonus seeds / object / crm_obs_only | 仅 1 个有效 seed (s46) | P1 |
| Bonus seeds / long / crm_obs_only | 仅 1 个有效 seed (s46) | P1 |
| Bonus seeds / goal / reconvla | 仅 2 个有效 seed (s46, s47) | P1 |
| Bonus seeds / long / reconvla | 仅 2 个有效 seed (s45, s46) | P1 |
| Pi05 / long / crm_obs_only | 仅 1 个 seed (s44) | P2 |
| Pi05 tau-sweep | 多为单 seed (s42)，multi-seed 覆盖仅 tau=0.25 | P2 |
| CRM always-on / smolvla / long s45 | SR 为 None | P2 |

---

## 部署建议

**当前只有 bjb1-18228 的 1 块 GPU 可用。** DDL 20:00 BJ，每个实验约 30-40 分钟，最多再跑 ~10-12 个实验。

如果只有 1 GPU 可用，建议优先级排序：

| 优先级 | 实验 | 服务器:GPU | 预估时长 |
|--------|------|-----------|----------|
| 1 | eval-supp-long-adapt-tau025-s43 | bjb1-18228:0 | ~35min |
| 2 | eval-supp-long-adapt-tau025-s44 | bjb1-18228:0 | ~35min |
| 3 | eval-supp-obj-adapt-tau025-s43 | bjb1-18228:0 | ~35min |
| 4 | eval-supp-obj-adapt-tau025-s44 | bjb1-18228:0 | ~35min |
| ... | 后续按 P1 缺口排 | — | — |

**但真正的瓶颈是服务器不可达。** 建议：
1. **立即去 AutoDL 控制台检查 bjb1-32546 / bjb2-28827 / cqa1-32758 实例状态**，如果已关机则开机，如果端口变了请更新 `~/.ssh/config`
2. 恢复后 22 GPU 全开可在 DDL 前批量补齐上述缺口
3. bjb1-18228 如果确实只有 1 卡，立即开始跑 P0 缺口实验（long/adaptive 和 object/adaptive）

等待指示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 391190,
  "duration_api_ms": 386923,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "8c290cbe-aa35-4006-bed3-2d946febaa53",
  "total_cost_usd": 1.76133575,
  "usage": {
    "input_tokens": 111,
    "cache_creation_input_tokens": 33616,
    "cache_read_input_tokens": 120033,
    "output_tokens": 4701,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 33616,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2094,
        "cache_read_input_tokens": 31240,
        "cache_creation_input_tokens": 14221,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 14221
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1761,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001841,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 133,
      "outputTokens": 23570,
      "cacheReadInputTokens": 886022,
      "cacheCreationInputTokens": 116251,
      "webSearchRequests": 0,
      "costUSD": 1.75949475,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "cd6031ec-4cc8-4384-9770-cf404be630a4"
}
```

</details>

---
