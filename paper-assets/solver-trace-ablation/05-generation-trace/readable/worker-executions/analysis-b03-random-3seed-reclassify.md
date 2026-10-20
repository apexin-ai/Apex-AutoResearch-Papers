# analysis b03 random 3seed reclassify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_analysis_b03-random-3seed-reclassify_20260515T182051.log`
- **Structured JSON:** [`03e9279e8c6630414646.json`](../../sessions/03/03e9279e8c6630414646.json)

## Before a recorded user message

55 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
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
  "uuid": "e7069e07-989c-46df-a392-a3f19655dace",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
Let me start by connecting to the server and doing the initial exploration steps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "a4e05e01-1209-4016-bb81-3d40a706bf9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMRVGJUhdtk21qrxxCrJTZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13509,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13509
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

_source line 4_

开始执行 β=0.3 Random 三 seed 的 classify_h7 重分类。先连接服务器探测环境。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "a58b4d4f-82fe-46c3-8a8f-30cfebc3f064",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMRVGJUhdtk21qrxxCrJTZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13509,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13509
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

### Runtime record

_source line 5_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778885400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9598b32f-fa71-4f22-8c84-e34fb8a4f251",
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5"
}
```

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QvAX4C7U94gbrRYEhndfJd`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry",
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "29046680-a0fe-4ff4-be47-76b167958ace",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMRVGJUhdtk21qrxxCrJTZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13509,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13509
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

_source line 7 · 2026-05-15T18:21:06.159Z_

<details><summary>↩ Tool result · `toolu_01QvAX4C7U94gbrRYEhndfJd`</summary>

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
  "tool_name": "mcp__agent-ml-research__detect_image"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "2c534bb6-dc1c-4c78-abe1-89bd8d42a021",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AH9EtTERgpFTYYhEEKH7tz`</summary>

```json
{
  "server": "westd-39279",
  "command": "nvidia-smi",
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "e4337586-c04d-4ae1-b908-31ff37cad0db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSKQBD8U7K6xJh7PMB2acs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1697,
      "cache_read_input_tokens": 25350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1697
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

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011bCjsdmRbYE6iZy6CgzMWe`</summary>

```json
{
  "server": "westd-39279",
  "command": "ls /root/autodl-tmp/outputs/ | grep -iE \"plan017|b03|random\"",
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "1846cb3f-f1c4-46ce-a00e-3a4912f7fa09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSKQBD8U7K6xJh7PMB2acs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1697,
      "cache_read_input_tokens": 25350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1697
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

_source line 10 · 2026-05-15T18:21:10.836Z_

<details><summary>↩ Tool result · `toolu_01AH9EtTERgpFTYYhEEKH7tz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Sat May 16 02:21:10 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |\\n| N/A   29C    P8             35W /  600W |       0MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   62C    P0            296W /  600W |   82683MiB /  97887MiB |     90%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    1   N/A  N/A          533420      C   python3                               82674MiB |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.28}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "bb648a33-79ad-45ab-873c-0f3da34d73f9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Sat May 16 02:21:10 2026       \\\\n+-----------------------------------------------------------------------------------------+\\\\n| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\\\n|                                         |                        |               MIG M. |\\\\n|=========================================+========================+======================|\\\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |\\\\n| N/A   29C    P8             35W /  600W |       0MiB /  97887MiB |      0%      Default |\\\\n|                                         |                        |             Disabled |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\\\n| N/A   62C    P0            296W /  600W |   82683MiB /  97887MiB |     90%      Default |\\\\n|                                         |                        |             Disabled |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n\\\\n+-----------------------------------------------------------------------------------------+\\\\n| Processes:                                                                              |\\\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\\\n|        ID   ID                                                               Usage      |\\\\n|=========================================================================================|\\\\n|    1   N/A  N/A          533420      C   python3                               82674MiB |\\\\n+-----------------------------------------------------------------------------------------+\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.28}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Sat May 16 02:21:10 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |\\n| N/A   29C    P8             35W /  600W |       0MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   62C    P0            296W /  600W |   82683MiB /  97887MiB |     90%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    1   N/A  N/A          533420      C   python3                               82674MiB |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.28}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T18:21:10.849Z_

<details><summary>↩ Tool result · `toolu_011bCjsdmRbYE6iZy6CgzMWe`</summary>

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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "37b3ca9d-32c4-4b8a-a8d7-951d2772c786",
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AENymjYqZeaptFujyEMVv5`</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": {
    "exp_id": "plan017-additive-random-s42"
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "9f5036ee-72b9-4240-9eea-21383aafb966",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSKQBD8U7K6xJh7PMB2acs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1697,
      "cache_read_input_tokens": 25350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1697
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

_source line 13 · 2026-05-15T18:21:11.321Z_

<details><summary>↩ Tool result · `toolu_01AENymjYqZeaptFujyEMVv5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3084}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "dab1772f-898e-4278-a88e-e420fafc0720",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3084}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3084}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01JbgukLMyjH3n3jHA1jrQpX`</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": {
    "exp_id": "exp1-random-b03-s43-r4"
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "c7982259-a908-4529-982d-66209058a0e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSKQBD8U7K6xJh7PMB2acs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1697,
      "cache_read_input_tokens": 25350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1697
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

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01DAHGadxSVv2P9GU3W56Aqk`</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": {
    "exp_id": "exp1-random-b03-s44-r2"
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "dc0869f7-26a0-458d-aeaa-6d3ebb581674",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSKQBD8U7K6xJh7PMB2acs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1697,
      "cache_read_input_tokens": 25350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1697
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

_source line 16 · 2026-05-15T18:21:12.884Z_

<details><summary>↩ Tool result · `toolu_01JbgukLMyjH3n3jHA1jrQpX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.485}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "4a35b31d-bb54-4081-932c-a4341856abe7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.485}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.485}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T18:21:13.292Z_

<details><summary>↩ Tool result · `toolu_01DAHGadxSVv2P9GU3W56Aqk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3951}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "57ecb7df-b75f-473b-8c59-bf41d2aee363",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3951}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3951}}"
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
GPU 0 is free, GPU 1 is busy with a training job. Good, I'll use GPU 0.

The registry filter by exp_id returned empty - the filter might not work that way. Let me search differently. Also need to list the outputs directory without pipe.

Let me do two things:
1. List the outputs directory
2. Search registry for these experiments differently
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "ea122f99-cff4-4057-b58d-b6f9054a7b10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGqmJCvsLKRaUoyaLfWuiu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1522,
      "cache_read_input_tokens": 27047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1522
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

GPU 0 空闲，可用。Registry 的 exp_id 过滤没匹配到，换方式搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "bbf9b668-062c-4a76-bd30-3080bef5465a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGqmJCvsLKRaUoyaLfWuiu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1522,
      "cache_read_input_tokens": 27047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1522
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016aTd74g5o5VHnGjSJrsT7w`</summary>

```json
{
  "server": "westd-39279",
  "command": "ls /root/autodl-tmp/outputs/",
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "408590a2-8332-4d84-ba78-84d4d29eeae2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGqmJCvsLKRaUoyaLfWuiu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1522,
      "cache_read_input_tokens": 27047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1522
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

_source line 21 · 2026-05-15T18:21:19.922Z_

<details><summary>↩ Tool result · `toolu_016aTd74g5o5VHnGjSJrsT7w`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"bootstrap_ci_results.json\\nd086_missed_classify_h7.json\\neval_sta_exp1_isr_b03_s43.json\\neval_sta_exp1_isr_b03_s43_r3\\neval_sta_exp1_isr_b03_s43_r3.json\\neval_sta_exp1_isr_b03_s44_r2_correct.json\\neval_sta_exp1_random_b03_s43.json\\neval_sta_exp1_random_b03_s43_r4.json\\neval_sta_exp1_random_b03_s44_r2.json\\neval_sta_plan001_exec_only_s44.json\\neval_sta_plan001_r2.json\\neval_sta_plan002.log\\neval_sta_plan004_fast_isr_s42.json\\neval_sta_plan006_prolog_exec_s42.json\\neval_sta_plan009_sft_s43.json\\neval_sta_plan009_sft_s44.json\\neval_sta_plan013_r4.json\\neval_sta_plan017_additive_random_s42.json\\neval_sta_plan018_additive_random_b01_s42.json\\neval_sta_run.log\\nexp1_isr_b03_s42_1000\\nexp1_isr_b03_s43_eval\\nexp1_isr_b03_s44_r2\\nexp1_isr_b03_s44_r2_eval\\nexp1_random_b03_s43_r2\\nexp1_random_b03_s43_r4\\nexp1_random_b03_s44\\nexp1_random_b03_s44_r2\\nexp4_100step_h1h7_classification.json\\nh7_classification\\nh8_retroactive_audit.json\\nh8_retroactive_audit.txt\\nisr_s44_fn_evidence.json\\nplan001_exec_only_s43_1000_r2\\nplan001_exec_only_s44_1000_r2\\nplan001_s44_eval_sta.json\\nplan002_additive_b01_s42_1000\\nplan002_additive_b01_s42_1000_taxonomy_unified.json\\nplan002_additive_b01_s42_taxonomy_unified.json\\nplan002_additive_b01_s43_r2\\nplan003_eval_exec_only_r5.json\\nplan004_fast_isr_s42\\nplan009_sft_baseline_s42_1000\\nplan009_sft_baseline_s43\\nplan009_sft_baseline_s43_1000\\nplan009_sft_baseline_s44\\nplan009_sft_baseline_s44_1000\\nplan014_downstream_nli.json\\nplan018_additive_random_b01_s42_1000\\nplan018_additive_random_b01_s42_1000_r3\\nplan018_additive_random_b01_s43_r3\\nplan018_additive_random_b01_s44_r2\\nplan018_random_s42_taxonomy_verification.json\\nsft_1000_taxonomy_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "f35acb61-cb58-4ddc-b856-0fe7c7b71725",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"bootstrap_ci_results.json\\\\nd086_missed_classify_h7.json\\\\neval_sta_exp1_isr_b03_s43.json\\\\neval_sta_exp1_isr_b03_s43_r3\\\\neval_sta_exp1_isr_b03_s43_r3.json\\\\neval_sta_exp1_isr_b03_s44_r2_correct.json\\\\neval_sta_exp1_random_b03_s43.json\\\\neval_sta_exp1_random_b03_s43_r4.json\\\\neval_sta_exp1_random_b03_s44_r2.json\\\\neval_sta_plan001_exec_only_s44.json\\\\neval_sta_plan001_r2.json\\\\neval_sta_plan002.log\\\\neval_sta_plan004_fast_isr_s42.json\\\\neval_sta_plan006_prolog_exec_s42.json\\\\neval_sta_plan009_sft_s43.json\\\\neval_sta_plan009_sft_s44.json\\\\neval_sta_plan013_r4.json\\\\neval_sta_plan017_additive_random_s42.json\\\\neval_sta_plan018_additive_random_b01_s42.json\\\\neval_sta_run.log\\\\nexp1_isr_b03_s42_1000\\\\nexp1_isr_b03_s43_eval\\\\nexp1_isr_b03_s44_r2\\\\nexp1_isr_b03_s44_r2_eval\\\\nexp1_random_b03_s43_r2\\\\nexp1_random_b03_s43_r4\\\\nexp1_random_b03_s44\\\\nexp1_random_b03_s44_r2\\\\nexp4_100step_h1h7_classification.json\\\\nh7_classification\\\\nh8_retroactive_audit.json\\\\nh8_retroactive_audit.txt\\\\nisr_s44_fn_evidence.json\\\\nplan001_exec_only_s43_1000_r2\\\\nplan001_exec_only_s44_1000_r2\\\\nplan001_s44_eval_sta.json\\\\nplan002_additive_b01_s42_1000\\\\nplan002_additive_b01_s42_1000_taxonomy_unified.json\\\\nplan002_additive_b01_s42_taxonomy_unified.json\\\\nplan002_additive_b01_s43_r2\\\\nplan003_eval_exec_only_r5.json\\\\nplan004_fast_isr_s42\\\\nplan009_sft_baseline_s42_1000\\\\nplan009_sft_baseline_s43\\\\nplan009_sft_baseline_s43_1000\\\\nplan009_sft_baseline_s44\\\\nplan009_sft_baseline_s44_1000\\\\nplan014_downstream_nli.json\\\\nplan018_additive_random_b01_s42_1000\\\\nplan018_additive_random_b01_s42_1000_r3\\\\nplan018_additive_random_b01_s43_r3\\\\nplan018_additive_random_b01_s44_r2\\\\nplan018_random_s42_taxonomy_verification.json\\\\nsft_1000_taxonomy_summary.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"bootstrap_ci_results.json\\nd086_missed_classify_h7.json\\neval_sta_exp1_isr_b03_s43.json\\neval_sta_exp1_isr_b03_s43_r3\\neval_sta_exp1_isr_b03_s43_r3.json\\neval_sta_exp1_isr_b03_s44_r2_correct.json\\neval_sta_exp1_random_b03_s43.json\\neval_sta_exp1_random_b03_s43_r4.json\\neval_sta_exp1_random_b03_s44_r2.json\\neval_sta_plan001_exec_only_s44.json\\neval_sta_plan001_r2.json\\neval_sta_plan002.log\\neval_sta_plan004_fast_isr_s42.json\\neval_sta_plan006_prolog_exec_s42.json\\neval_sta_plan009_sft_s43.json\\neval_sta_plan009_sft_s44.json\\neval_sta_plan013_r4.json\\neval_sta_plan017_additive_random_s42.json\\neval_sta_plan018_additive_random_b01_s42.json\\neval_sta_run.log\\nexp1_isr_b03_s42_1000\\nexp1_isr_b03_s43_eval\\nexp1_isr_b03_s44_r2\\nexp1_isr_b03_s44_r2_eval\\nexp1_random_b03_s43_r2\\nexp1_random_b03_s43_r4\\nexp1_random_b03_s44\\nexp1_random_b03_s44_r2\\nexp4_100step_h1h7_classification.json\\nh7_classification\\nh8_retroactive_audit.json\\nh8_retroactive_audit.txt\\nisr_s44_fn_evidence.json\\nplan001_exec_only_s43_1000_r2\\nplan001_exec_only_s44_1000_r2\\nplan001_s44_eval_sta.json\\nplan002_additive_b01_s42_1000\\nplan002_additive_b01_s42_1000_taxonomy_unified.json\\nplan002_additive_b01_s42_taxonomy_unified.json\\nplan002_additive_b01_s43_r2\\nplan003_eval_exec_only_r5.json\\nplan004_fast_isr_s42\\nplan009_sft_baseline_s42_1000\\nplan009_sft_baseline_s43\\nplan009_sft_baseline_s43_1000\\nplan009_sft_baseline_s44\\nplan009_sft_baseline_s44_1000\\nplan014_downstream_nli.json\\nplan018_additive_random_b01_s42_1000\\nplan018_additive_random_b01_s42_1000_r3\\nplan018_additive_random_b01_s43_r3\\nplan018_additive_random_b01_s44_r2\\nplan018_random_s42_taxonomy_verification.json\\nsft_1000_taxonomy_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_015f8H5yBtd1jqshjrWWDEW8`</summary>

```json
{
  "project": "solver-trace-ablation",
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "85493452-4e3d-4b10-83e5-4f238aed6560",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGqmJCvsLKRaUoyaLfWuiu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1522,
      "cache_read_input_tokens": 27047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1522
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

_source line 23 · 2026-05-15T18:21:20.291Z_

<details><summary>↩ Tool result · `toolu_015f8H5yBtd1jqshjrWWDEW8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan018-additive-random-b01-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.79, \"eval_mean_isr\": 0.1038, \"eval_isr_std\": 0.1369, \"eval_median_isr\": 0.0357, \"eval_proved_only_isr\": 0.1314, \"eval_n_proved\": 79, \"eval_n_problems\": 100, \"tautological_collapse\": false, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 58, \"h1_rate\": 0.7342, \"h8_count\": 4, \"h8_rate\": 0.0506, \"genuine_count\": 18, \"genuine_rate\": 0.2278, \"taxonomy_tool\": \"classify_h7.py standard (2026-05-15)\", \"taxonomy_note\": \"Re-classified with current classify_h7.py. Old values: genuine_strict=12 (H1_exact=56, H1_near=8, H8=3). New standard: H1=58 (2 former H1-near now H1), H8=4, genuine=18. Standard definition: proved - H7 - H1 - H8.\"}}, \"plan018-additive-random-b01-s43-r3\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.94, \"n_proved\": 94, \"n_problems\": 100, \"mean_isr\": 0.1406, \"isr_std\": null, \"proved_only_isr\": 0.1495, \"h7_count\": 36, \"h7_rate\": 0.383, \"h7a_count\": 36, \"h7b_count\": 0, \"h1_count\": 56, \"h1_rate\": 0.596, \"h8_count\": 1, \"h8_rate\": 0.011, \"genuine_count\": 1, \"genuine_rate\": 0.0106, \"train_prove_rate\": 0.5825, \"train_mean_isr\": 0.1266}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s44-r2\": {\"status\": \"RUNNING\"}, \"plan002-additive-b01-s43-r2\": {\"status\": \"DONE\", \"metrics\": {\"eval_n_problems\": 100, \"eval_n_proved\": 61, \"eval_prove_rate\": 0.61, \"eval_mean_isr\": 0.5063, \"eval_isr_std\": 0.4518, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.8301, \"h7a_count\": 59, \"h7b_count\": 2, \"h7_count\": 61, \"h7_rate\": 1, \"h1_count\": 0, \"h1_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"proved_single_premise_ratio\": 1, \"content_independent_predicates\": 5, \"isr_eq_1_count\": 40, \"isr_eq_1_rate_of_proved\": 0.656, \"train_prove_rate\": 0.68775, \"train_mean_isr\": 0.5039}, \"conclusion\": \"negative\"}, \"plan001-exec-only-s43-1000-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.9, \"n_proved\": 90, \"n_problems\": 100, \"mean_isr\": 0.531, \"isr_std\": 0.15, \"isr_corrected\": 0.465, \"isr_artifact_note\": \"n_components=3 quantifier decomposition artifact (+0.066) + $T solver bug 5 samples (+0.025). Corrected ISR=0.465, but both values entirely from H7a tautological necessity, no reasoning quality signal.\", \"h7_count\": 90, \"h7_rate\": 1, \"h7a_count\": 90, \"h7b_count\": 0, \"h1_count\": 0, \"h1_rate\": 0, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0}}, \"plan016-extended-1000-s42\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.96, \"n_proved\": 96, \"n_problems\": 100, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 96, \"h1_rate\": 1, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"genuine_h1_near\": 0, \"genuine_strict\": 0, \"content_independent_rate\": 1, \"single_premise_rate\": 0, \"taxonomy_audit\": \"2026-05-15\", \"taxonomy_tool\": \"classify_h7.py current version (with H8 detection)\", \"taxonomy_note\": \"Re-run with current classify_h7.py. Old value genuine=7 was incorrect (old version lacked H8 and had weaker H1 detection). All 96 proved are H1 (conclusion embedded in premises). 0 H7, 0 H8.\"}, \"conclusion\": \"success\"}, \"plan001-exec-only-s44-1000-r2\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 1, \"n_proved\": 100, \"n_problems\": 100, \"mean_isr\": 0.002, \"isr_std\": 0.0146, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 85, \"h1_rate\": 0.85, \"h8_count\": 15, \"h8_rate\": 0.15, \"genuine_count\": 0, \"genuine_rate\": 0, \"genuine_note\": \"D091: 3 samples escape text-match classifiers but are functionally degenerate (ISR=0, disjunctive/commuted bypasses)\"}, \"conclusion\": \"success\"}, \"plan018-additive-random-b01-s42-1000-r3\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.97, \"eval_mean_isr\": 0.6892, \"eval_isr_std\": 0.2037, \"eval_median_isr\": 0.75, \"eval_proved_only_isr\": 0.7105, \"eval_n_proved\": 97, \"eval_n_problems\": 100, \"genuine_count\": 0, \"genuine_rate\": 0, \"h1_count\": 0, \"h1_rate\": 0, \"h7_count\": 97, \"h7_rate\": 1, \"tautological_collapse\": true, \"train_final_prove_rate\": 0.827, \"train_final_mean_isr\": 0.5213, \"train_loss\": 0.00671, \"train_final_entropy\": 0.003, \"train_runtime_seconds\": 5783, \"train_steps\": 1000, \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 25, \"prove_rate\": 1, \"mean_isr\": 0.7533}, \"unknown\": {\"count\": 41, \"proved\": 39, \"prove_rate\": 0.951, \"mean_isr\": 0.6565}, \"true\": {\"count\": 34, \"proved\": 33, \"prove_rate\": 0.971, \"mean_isr\": 0.6814}}, \"n_premise_distribution\": {\"1\": 97}, \"pattern_description\": \"All 97 proved: 1 premise identical to conclusion (P therefore P). D088 correction: h7=97 h1=0 (was h1=97 h7=0 pre-D086 bugfix).\"}, \"conclusion\": \"negative\"}, \"plan009-sft-baseline-s44-1000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.15, \"n_proved\": 15, \"n_problems\": 100, \"mean_isr\": 0.0884, \"isr_std\": 0.2268, \"median_isr\": 0, \"proved_only_mean_isr\": 0.5892, \"max_isr\": 0.8571, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.4412}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0}}, \"genuine_count\": 14, \"genuine_rate\": 0.9333, \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0667, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0667, \"content_independent_count\": 0, \"content_independent_rate\": 0, \"isr_1_count\": 0, \"isr_1_rate\": 0, \"train_final_loss\": 0.0171, \"train_avg_loss\": 0.1544, \"train_token_accuracy\": 0.995, \"train_runtime_s\": 1580.97, \"eval_elapsed_s\": 391.8}}, \"plan009-sft-baseline-s43-1000\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.11, \"n_proved\": 11, \"n_problems\": 100, \"mean_isr\": 0.0699, \"isr_std\": 0.2155, \"median_isr\": 0, \"proved_only_mean_isr\": 0.6352, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 11, \"prove_rate\": 0.3235}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0}}, \"genuine_count\": 10, \"genuine_rate\": 0.9091, \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0909, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0909, \"content_independent_count\": 0, \"content_independent_rate\": 0, \"isr_1_count\": 1, \"isr_1_rate\": 0.0909, \"train_final_loss\": 0.0167, \"train_avg_loss\": 0.1551, \"train_token_accuracy\": 0.9954, \"train_runtime_s\": 1584.79, \"eval_elapsed_s\": 326.1}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s42-1000\": {\"status\": \"DONE\", \"metrics\": {\"train_final_loss\": 0.0168, \"train_last_step_loss\": 0.0168, \"train_token_accuracy\": 0.9955, \"train_epochs\": 15.88, \"train_runtime_sec\": 1415, \"train_steps\": 1000, \"eval_prove_rate\": 0.13, \"eval_n_proved\": 13, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0738, \"eval_isr_std\": 0.2077, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5677, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"eval_output_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json\", \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0769, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 12, \"genuine_rate\": 0.9231, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0769, \"isr_1_count\": 0, \"content_independent_count\": 0, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 12, \"prove_rate\": 0.353, \"mean_isr\": 0.209}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.011}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}}}, \"conclusion\": \"success\"}, \"exp1-random-b03-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.79, \"mean_isr\": 0.1745, \"isr_std\": 0.1628, \"median_isr\": 0.1667, \"proved_only_mean_isr\": 0.2209, \"hacking_rate_strict_h7\": 0, \"hacking_rate_functional\": 0.1013, \"genuine_rate\": 0.8987, \"genuine_count\": 71, \"n_proved\": 79, \"n_problems\": 100, \"h1_conclusion_in_premise\": 0.759, \"eval_data\": \"test_100.jsonl\", \"eval_output\": \"/root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43.json\"}}, \"exp1-random-b03-s43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_step\": 500, \"prove_rate\": 0.5505, \"mean_isr\": 0.1358, \"parse_rate\": 1, \"train_loss\": 0.01365, \"train_runtime_sec\": 6161.1, \"epoch\": 2, \"eval_prove_rate\": 0.92, \"eval_mean_isr\": 0.1659, \"eval_isr_std\": 0.1147, \"eval_median_isr\": 0.1429, \"eval_proved_only_mean_isr\": 0.1803, \"eval_min_isr\": 0, \"eval_max_isr\": 0.5, \"eval_n_proved\": 92, \"eval_n_problems\": 100, \"eval_h7_strict_rate\": 0.076, \"eval_h7_strict_count\": 7, \"eval_h1_strict_rate\": 0.891, \"eval_h1_strict_count\": 82, \"eval_genuine_rate\": 0.0326, \"eval_genuine_count\": 3, \"eval_isr0_count\": 6, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 23, \"prove_rate\": 0.92, \"mean_isr\": 0.156}, \"unknown\": {\"count\": 41, \"proved\": 37, \"prove_rate\": 0.902, \"mean_isr\": 0.184}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.151}}, \"D086_correction\": \"H1 90→82, genuine 2→3 per D086 clean batch run\"}}, \"plan002-additive-b01-s42-1000\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.9, \"eval_mean_isr\": 0.7892, \"eval_isr_std\": 0.3424, \"eval_proved_only_isr\": 0.8769, \"eval_median_isr\": 1, \"eval_n_proved\": 90, \"eval_n_problems\": 100, \"eval_component_count_mean\": 2.889, \"tautological_collapse\": true, \"train_final_prove_rate\": 0.855, \"train_final_mean_isr\": 0.532, \"h7_count\": 87, \"h7_rate\": 0.9667, \"h1_count\": 0, \"h1_rate\": 0, \"h1_near_count\": 1, \"h1_near_rate\": 0.0111, \"h8_conjunction_collapse_count\": 1, \"h8_conjunction_collapse_rate\": 0.0111, \"genuine_count\": 2, \"genuine_rate\": 0.0222, \"taxonomy_standard\": \"D086 clean run = ground truth. D084 residual removed.\"}}, \"plan002-additive-b01-s44\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.89, \"eval_mean_isr\": 0.803, \"eval_isr_std\": null, \"eval_proved_only_isr\": 0.902, \"eval_n_proved\": 89, \"eval_n_problems\": 100, \"h7_count\": 89, \"h7_rate\": 1, \"h1_count\": 0, \"h1_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"component_mean\": 4.33, \"comp_2_ratio\": 0.022, \"h7_fn_correction\": \"12 former genuine reclassified as H7: all n_prem=1 false negatives (normalization mismatch prevented conclusion matching)\"}, \"conclusion\": \"negative\"}, \"plan013-random-reward-s42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 1, \"eval_mean_isr\": 0.535, \"eval_isr_std\": 0.1282, \"eval_proved_only_isr\": 0.535, \"eval_median_isr\": 0.5, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"}}, \"plan001-exec-only-s43-r4\": {\"status\": \"DONE\", \"metrics\": {\"eval_sampling_prove_rate\": 0.14, \"eval_sampling_mean_isr\": 0, \"eval_sampling_n_proved\": 14, \"eval_sampling_temperature\": 0.7, \"eval_sampling_method\": \"do_sample=True, temperature=0.7\", \"eval_sampling_by_answer\": {\"true\": {\"count\": 34, \"proved\": 6, \"prove_rate\": 0.176}, \"false\": {\"count\": 25, \"proved\": 2, \"prove_rate\": 0.08}, \"unknown\": {\"count\": 41, \"proved\": 6, \"prove_rate\": 0.146}}, \"eval_greedy_prove_rate\": 0.13, \"eval_greedy_mean_isr\": 0, \"eval_greedy_proved_only_isr\": 0, \"eval_greedy_n_proved\": 13, \"eval_greedy_method\": \"eval_sta.py default (do_sample=False)\", \"eval_greedy_by_answer\": {\"true\": {\"count\": 34, \"proved\": 4, \"prove_rate\": 0.118}, \"false\": {\"count\": 25, \"proved\": 5, \"prove_rate\": 0.2}, \"unknown\": {\"count\": 41, \"proved\": 4, \"prove_rate\": 0.0976}}, \"eval_greedy_h7_count\": 0, \"eval_greedy_h7_rate\": 0, \"eval_greedy_h1_count\": 13, \"eval_greedy_h1_rate\": 1, \"eval_greedy_genuine_rate\": 0, \"eval_greedy_n_premises_proved_mean\": 17.92, \"eval_greedy_mean_components_proved\": 18.92, \"eval_greedy_n_premises_all_mean\": 32.67, \"eval_sampling_h1_rate\": 1, \"eval_sampling_h7_rate\": 0, \"eval_sampling_genuine_rate\": 0, \"eval_sampling_mean_components_proved\": 18.5, \"eval_greedy_vs_sampling_delta_pr\": -0.01, \"eval_method_note\": \"Greedy and sampling agree on failure profile (ISR*=0, H1=100%, components~18.5-18.9). s43 collapse is decoding-invariant.\"}, \"conclusion\": \"negative\"}, \"plan001-exec-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan017-additive-random-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"tautological_collapse\": false, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 1, \"h1_count\": 48, \"genuine_rate\": 0, \"genuine_count\": 0}}, \"plan002-additive-b01-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.81, \"eval_mean_isr\": 0.3365, \"eval_isr_std\": 0.3227, \"eval_proved_only_isr\": 0.4154, \"eval_median_isr\": 0.2, \"eval_n_proved\": 81, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 5.58, \"h7_rate\": 0.16, \"h7_count\": 13, \"h1_rate\": 0.519, \"h1_count\": 42, \"h8_conjunction_collapse_count\": 12, \"h8_conjunction_collapse_rate\": 0.148, \"genuine_rate\": 0.173, \"genuine_count\": 14, \"tautological_collapse\": false, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse audit completed. 12/81 proved samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json\"}}, \"plan002-additive-b01-s43\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.61, \"eval_n_proved\": 61, \"eval_n_problems\": 100, \"eval_proved_only_isr\": 0.83, \"h7_count\": 59, \"h7_rate\": 0.9672, \"h1_count\": 0, \"h1_rate\": 0, \"h1_near_count\": 0, \"h1_near_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 2, \"genuine_rate\": 0.0328, \"proved_single_premise_ratio\": 1, \"taxonomy_note\": \"structurally determined: proved_single_premise_ratio=1.0, all taxonomy categories except H7 are zero by construction. eval file lost but classification derivable from structure.\"}, \"conclusion\": \"negative\"}, \"exp1-isr-b03-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.91, \"mean_isr\": 0.2575, \"isr_std\": 0.2363, \"median_isr\": 0.3333, \"proved_only_mean_isr\": 0.283, \"hacking_rate_strict_h7\": 0.022, \"hacking_rate_functional\": 0.3297, \"genuine_rate\": 0.6703, \"genuine_count\": 61, \"n_proved\": 91, \"n_problems\": 100, \"h1_conclusion_in_premise\": 0.747, \"eval_data\": \"test_100.jsonl\", \"eval_output\": \"/root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s43.json\"}}, \"plan009-sft-baseline-s44-1000-r3\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.15, \"eval_n_proved\": 15, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0884, \"eval_isr_std\": 0.2268, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5892, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 1, \"h1_rate\": 0.0667, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 14, \"genuine_rate\": 0.9333, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.441, \"mean_isr\": 0.26}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}}}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s44\": {\"status\": \"DONE\", \"metrics\": {\"train_final_loss\": 0.2397, \"train_last_step_loss\": 0.0328, \"train_token_accuracy\": 0.9928, \"train_epochs\": 7.94, \"train_runtime_sec\": 729.05, \"train_steps\": 500, \"eval_prove_rate\": 0.17, \"eval_n_proved\": 17, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0974, \"eval_isr_std\": 0.2409, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5729, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"eval_output_path\": \"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s44.json\", \"eval_tautological_collapse\": false, \"eval_h7_count\": 0, \"eval_h7_rate\": 0, \"eval_h1_count\": 2, \"eval_h1_rate\": 0.118, \"eval_genuine_count\": 15, \"eval_genuine_rate\": 0.882, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.441, \"mean_isr\": 0.257}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.027}, \"unknown\": {\"count\": 41, \"proved\": 1, \"prove_rate\": 0.024, \"mean_isr\": 0.008}}, \"eval_correction_note\": \"Corrected 2026-05-15: previous eval used test_100.jsonl (50/44/6 distribution), re-evaled with proofwriter_fol_100.jsonl (34/25/41)\"}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s43\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.2391, \"train_token_accuracy\": 0.9938, \"train_epochs\": 7.94, \"train_runtime_sec\": 677.14, \"train_steps\": 500, \"eval_prove_rate\": 0.15, \"eval_mean_isr\": 0.0895, \"eval_isr_std\": 0.2338, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5967, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 1, \"h1_rate\": 0.067, \"genuine_count\": 14, \"genuine_rate\": 0.933, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"prove_rate\": 0.382, \"mean_isr\": 0.234}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.027}, \"unknown\": {\"count\": 41, \"proved\": 1, \"prove_rate\": 0.024, \"mean_isr\": 0.008}}, \"eval_data_path\": \"data/proofwriter_fol_100.jsonl\", \"eval_output_path\": \"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s43.json\"}, \"conclusion\": \"success\"}, \"plan001-exec-only-s44-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan009-sft-baseline-s44-1000-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan002-additive-b03-s42\": {\"status\": \"DONE\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"last100_prove_rate\": 0.5525, \"eval_prove_rate\": 0.18, \"eval_mean_isr\": 0.0257, \"eval_isr_std\": 0.0742, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.1427, \"eval_n_proved\": 18, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.778, \"h1_count\": 14, \"h8_conjunction_collapse_count\": 3, \"h8_conjunction_collapse_rate\": 0.1667, \"genuine_rate\": 0.0556, \"genuine_count\": 1, \"eval_by_type_false_pr\": 0.12, \"eval_by_type_false_isr\": 0.0102, \"eval_by_type_unknown_pr\": 0.195, \"eval_by_type_unknown_isr\": 0.0422, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.0172, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine 4→1.\"}, \"conclusion\": \"negative\"}, \"plan001-exec-only-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.93, \"eval_mean_isr\": 0.1232, \"eval_isr_std\": 0.1887, \"eval_proved_only_isr\": 0.1324, \"eval_median_isr\": 0, \"eval_n_proved\": 93, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.871, \"h1_count\": 81, \"h8_conjunction_collapse_count\": 6, \"h8_conjunction_collapse_rate\": 0.0645, \"genuine_rate\": 0.0753, \"genuine_count\": 7, \"genuine_mean_isr\": 0.3141, \"h1_mean_isr\": 0.1055, \"conclusion_embedding_total\": 0.871, \"content_independent_predicates_count\": 1, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine 12→7.\"}}, \"plan004-o1-ablation-s42\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.63, \"mean_isr\": 0.0072, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 63, \"h1_rate\": 1, \"h8_conjunction_collapse_count\": 2, \"h8_conjunction_collapse_rate\": 0.0317, \"genuine_count\": 0, \"genuine_rate\": 0, \"content_independent_predicates_count\": 3, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine unchanged (0).\"}, \"conclusion\": \"negative\"}, \"exp1-isr-b03-s42-1000-r2\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.95, \"eval_mean_isr\": 0.734, \"eval_isr_std\": 0.2575, \"eval_median_isr\": 0.6, \"eval_proved_only_isr\": 0.7726, \"eval_n_proved\": 95, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 25, \"prove_rate\": 1, \"mean_isr\": 0.824}, \"unknown\": {\"count\": 41, \"proved\": 38, \"prove_rate\": 0.927, \"mean_isr\": 0.673}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.741}}, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 54, \"h1_rate\": 0.568, \"genuine_count\": 0, \"genuine_rate\": 0, \"tautological_collapse\": true, \"isr_1_count\": 41, \"isr_1_rate\": 0.432, \"single_premise_count\": 0, \"train_final_prove_rate\": 0.829, \"train_final_mean_isr\": 0.727, \"train_loss\": 0.0041, \"train_runtime_seconds\": 6280, \"train_final_entropy\": 9e-06, \"completions_mean_length\": 47, \"h8_conjunction_collapse_count\": 41, \"h8_conjunction_collapse_rate\": 0.432, \"content_independent_predicates\": true}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s42-1000-r2\": {\"status\": \"DONE\", \"metrics\": {\"train_final_prove_rate\": 0.989, \"train_final_mean_isr\": 0.353, \"train_final_reward\": 1.062, \"train_steps\": 1000, \"train_runtime_seconds\": 2957, \"eval_prove_rate\": 1, \"eval_mean_isr\": 0.3333, \"eval_isr_std\": 0, \"eval_median_isr\": 0.3333, \"eval_proved_only_isr\": 0.3333, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_component_count_mean\": 3, \"genuine_rate\": 0, \"genuine_count\": 0, \"tautological_collapse\": true, \"h7_rate\": null, \"h7_count\": null, \"h1_rate\": null, \"h1_count\": null}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s42-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp1-isr-b03-s42-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s44\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.98, \"eval_mean_isr\": 0.57, \"eval_isr_std\": 0.2013, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.5816, \"eval_n_proved\": 98, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 2.04, \"eval_component_count_2\": 94, \"eval_component_count_3\": 4, \"tautological_collapse\": true, \"h7_rate\": 1, \"h7_count\": 97, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"conclusion_embedding_total\": 1}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s43-r2\": {\"status\": \"DONE\", \"metrics\": {\"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 93.2, \"h1_count\": 82, \"genuine_rate\": 6.8, \"genuine_count\": 6, \"eval_prove_rate\": 0.88, \"eval_mean_isr\": 0.058}, \"conclusion\": \"negative\"}, \"exp1-random-b03-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.23, \"eval_proved_only_mean_isr\": 0, \"eval_mean_isr\": 0, \"eval_isr_std\": 0, \"eval_median_isr\": 0, \"eval_n_proved\": 23, \"eval_n_problems\": 100, \"eval_h7_strict_rate\": 0, \"eval_h7_strict_count\": 0, \"eval_h1_strict_rate\": 1, \"eval_h1_strict_count\": 23, \"eval_genuine_rate\": 0, \"eval_genuine_count\": 0, \"eval_data\": \"proofwriter_fol_100.jsonl\"}}, \"exp1-isr-b03-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_step\": 500, \"prove_rate\": 0.56125, \"mean_isr\": 0.1515, \"parse_rate\": 1, \"train_loss\": 0.0176, \"train_runtime_sec\": 4153.6, \"epoch\": 2, \"eval_prove_rate\": 0.86, \"eval_mean_isr\": 0.2535, \"eval_isr_std\": 0.2406, \"eval_median_isr\": 0.3333, \"eval_proved_only_mean_isr\": 0.2948, \"eval_min_isr\": 0, \"eval_max_isr\": 0.75, \"eval_n_proved\": 86, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_h7_strict_rate\": 0.047, \"eval_h7_strict_count\": 4, \"eval_h1_strict_rate\": 0.686, \"eval_h1_strict_count\": 59, \"eval_conclusion_in_premise_rate\": 0.733, \"eval_conclusion_in_premise_count\": 63, \"eval_genuine_rate\": 0.267, \"eval_genuine_count\": 23, \"eval_single_premise_rate\": 0.058, \"eval_single_premise_count\": 5, \"eval_isr_1_count\": 0, \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 23, \"prove_rate\": 0.92, \"mean_isr\": 0.334}, \"unknown\": {\"count\": 41, \"proved\": 35, \"prove_rate\": 0.854, \"mean_isr\": 0.199}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.26}}}}, \"exp1-random-b03-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan015-linear-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp1-isr-b03-s43-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp1-random-b03-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp1-isr-b03-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.95, \"mean_isr\": 0.705, \"isr_std\": 0.172, \"proved_only_isr\": 0.7421, \"n_proved\": 95, \"n_problems\": 100, \"h7_rate\": 1, \"h7_count\": 95, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"single_premise_rate\": 1, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"Re-eval with correct test set (D062). Previous test_100.jsonl results invalidated.\"}}, \"exp1-random-b03-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp1-isr-b03-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp1-isr-b03-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp2-exec-s43-greedy\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp4-100step-h1h7\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan006-prolog-sta-s44\": {\"status\": \"DONE\", \"metrics\": {\"pass_rate\": 0.97, \"isr_mean\": 0.885, \"isr_n_cl_ge3\": \"N/A (0 samples)\", \"n_clauses_dist\": \"78/100 single-clause, 22/100 two-clause\", \"h7_functional_rate\": 0.979, \"genuine_rate\": 0, \"premise_count_analysis\": \"100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs\", \"failure_mode\": \"query-as-fact gaming (total H7 collapse)\"}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s43\": {\"status\": \"DONE\", \"metrics\": {\"train\": {\"final_prove_rate\": 0.769, \"final_mean_isr\": 0.129, \"final_loss\": 0.0155, \"final_entropy\": 0.09, \"final_reward\": 0.573, \"completion_length_mean\": 143, \"train_runtime_seconds\": 5095, \"train_runtime_minutes\": 84.9}, \"eval\": {\"n_problems\": 100, \"n_proved\": 38, \"prove_rate\": 0.38, \"mean_isr\": 0.0704, \"isr_std\": 0.1263, \"median_isr\": 0, \"proved_only_mean_isr\": 0.1853, \"min_isr\": 0, \"max_isr\": 1, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 11, \"prove_rate\": 0.44, \"mean_isr\": 0.1003}, \"unknown\": {\"count\": 41, \"proved\": 11, \"prove_rate\": 0.268, \"mean_isr\": 0.0394}, \"true\": {\"count\": 34, \"proved\": 16, \"prove_rate\": 0.471, \"mean_isr\": 0.0859}}}, \"h7_classification\": {\"h7_strict\": 0, \"h7_rate\": 0, \"h1_strict\": 37, \"h1_rate\": 0.974, \"conclusion_in_premise_total\": 37, \"conclusion_in_premise_rate\": 0.974, \"genuine_count\": 0, \"genuine_rate\": 0, \"isr_1_count\": 1, \"note\": \"1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause; all 38/38 proved samples are tautological\"}}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"cumulative_prove_rate\": 0.848, \"cumulative_mean_isr\": 0.787, \"final_prove_rate\": 1, \"final_isr\": 1, \"final_reward\": 1, \"saturation_onset_step\": 100, \"train_loss\": 0.00716, \"training_hours\": 0.78, \"final_entropy\": 0.01, \"final_completion_length\": 27, \"initial_completion_length\": 120, \"steps_at_perfect_reward\": 400, \"train_runtime_sec\": 2791, \"eval_prove_rate\": 0.5, \"eval_mean_isr\": 0.5, \"eval_proved_only_isr\": 1, \"eval_h7_rate\": 1, \"eval_h7_count\": 50, \"eval_proved_count\": 50, \"eval_total_count\": 100, \"eval_n_clauses_mean\": 1, \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"}}, \"plan006-prolog-exec-s44\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.21, \"eval_mean_isr\": 0.0812, \"eval_isr_std\": 0.2343, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.3866, \"eval_min_isr\": 0, \"eval_max_isr\": 1, \"eval_n_proved\": 21, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 683.9, \"eval_by_type_false_pr\": 0.04, \"eval_by_type_false_isr\": 0.04, \"eval_by_type_unknown_pr\": 0.317, \"eval_by_type_unknown_isr\": 0.099, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.09, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\"}, \"plan009-sft-baseline-s42-r4\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.14, \"eval_mean_isr\": 0.08, \"eval_isr_std\": 0.214, \"eval_median_isr\": 0, \"eval_max_isr\": 0.833, \"eval_proved_only_isr\": 0.571, \"eval_n_proved\": 14, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"train_final_loss\": 0.0287, \"train_token_accuracy\": 0.9935, \"train_epochs\": 7.94, \"train_runtime_sec\": 789.6, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"pr\": 0.382, \"isr\": 0.226}, \"unknown\": {\"count\": 41, \"proved\": 1, \"pr\": 0.024, \"isr\": 0.008}, \"false\": {\"count\": 25, \"proved\": 0, \"pr\": 0, \"isr\": 0}}, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.071, \"h1_count\": 1, \"genuine_rate\": 0.929, \"genuine_count\": 13, \"hacking_patterns\": \"near-zero (1/14 H1, 0 H7, 92.9% genuine)\", \"tautological_collapse\": false}, \"conclusion\": \"success\"}, \"plan006-prolog-exec-s43-r3\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.56, \"eval_mean_isr\": 0.0084, \"eval_isr_std\": 0.0221, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.015, \"eval_min_isr\": 0, \"eval_max_isr\": 0.1, \"eval_n_proved\": 56, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 868.2, \"eval_by_type_false_pr\": 0.48, \"eval_by_type_false_isr\": 0.0043, \"eval_by_type_unknown_pr\": 0.6585, \"eval_by_type_unknown_isr\": 0.0114, \"eval_by_type_true_pr\": 0.5, \"eval_by_type_true_isr\": 0.0078, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s44\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.89, \"mean_isr\": 0.0619, \"isr_std\": 0.1756, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0695, \"n_proved\": 89, \"n_problems\": 100, \"max_isr\": 1, \"min_isr\": 0, \"isr_pr_ratio\": 0.0695, \"isr_zero_count\": 72, \"isr_one_count\": 2, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 21, \"prove_rate\": 0.84, \"mean_isr\": 0.0533}, \"unknown\": {\"count\": 41, \"proved\": 40, \"prove_rate\": 0.976, \"mean_isr\": 0.0892}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.0353}}, \"elapsed_seconds\": 1012.7, \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan006-prolog-exec-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan006-prolog-exec-s42\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.83, \"eval_mean_isr\": 0.031, \"eval_proved_only_isr\": 0.037, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2, \"eval_isr_std\": 0.0534, \"h7_rate\": 0, \"h1_rate\": 0, \"isr_1_rate\": 0, \"single_premise_rate\": 0, \"by_answer_type\": {\"true\": {\"proved\": 37, \"count\": 40, \"pr\": 0.925, \"isr\": 0.037}, \"false\": {\"proved\": 21, \"count\": 29, \"pr\": 0.724, \"isr\": 0.038}, \"unknown\": {\"proved\": 25, \"count\": 31, \"pr\": 0.806, \"isr\": 0.016}}}, \"conclusion\": \"negative\"}, \"plan006-prolog-exec-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan009-sft-baseline-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan009-sft-baseline-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan018-additive-random-b01-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan012-hacking-taxonomy\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"isr_b01_genuine_rate\": 0.259, \"random_b01_genuine_rate\": 0.177, \"genuine_rate_delta_pp\": 8.2, \"isr_b01_conclusion_embedding_rate\": 0.728, \"random_b01_conclusion_embedding_rate\": 0.785, \"isr_b01_genuine_mean_isr\": 0.6723, \"random_b01_genuine_mean_isr\": 0.3427, \"isr_b01_complexity_wo_utility_rate\": 0, \"random_b01_complexity_wo_utility_rate\": 0.038, \"isr_b01_hacking_rate\": 0.741, \"random_b01_hacking_rate\": 0.823}}, \"plan005-sta-low-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 71, \"parse_rate\": 1, \"overall_prove_rate\": 0.5657, \"overall_isr\": 0.1682, \"last50_prove_rate\": 0.77, \"last50_isr\": 0.2559, \"last100_prove_rate\": 0.7725, \"last100_isr\": 0.2299, \"last100_loss\": 0.022752, \"overall_loss\": 0.017296, \"last100_isr_pr_ratio\": 0.298, \"last100_isr_lt_pr_count\": \"99/100\", \"first_rolling10_pr_ge_0.8\": 178, \"first_rolling10_pr_ge_0.9\": 439, \"max_rolling10_pr\": 0.9375, \"max_rolling10_isr\": 0.3282, \"windowed\": {\"1-50\": {\"pr\": 0.1775, \"isr\": 0.0906}, \"51-100\": {\"pr\": 0.1775, \"isr\": 0.0835}, \"101-200\": {\"pr\": 0.5062, \"isr\": 0.1463}, \"201-300\": {\"pr\": 0.6713, \"isr\": 0.1791}, \"301-400\": {\"pr\": 0.7013, \"isr\": 0.1984}, \"401-500\": {\"pr\": 0.7725, \"isr\": 0.2299}}}}, \"plan014-downstream-nli-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_accuracy\": 0.341, \"proved_rate\": 0.915, \"proved_count\": 732, \"total_generations\": 800, \"parse_errors\": 0, \"accuracy_by_label\": {\"true\": 0.912, \"false\": 0, \"unknown\": 0.076}, \"spearman_rho\": -0.049, \"spearman_p\": 0.187, \"mann_whitney_U\": 17202, \"mann_whitney_p\": 0.288, \"bon_isr_accuracy\": 0.35, \"bon_random_accuracy\": 0.341, \"bon_oracle_accuracy\": 0.44, \"bon_prove_first_accuracy\": 0.35, \"isr_bucket_high_acc\": 0.75, \"isr_bucket_mid_acc\": 0.377, \"isr_bucket_low_acc\": 0.327, \"runtime_inference_s\": 408.8, \"runtime_eval_s\": 13.6}}, \"plan001-exec-only-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan003-eval-exec-only-r5\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.32, \"mean_isr\": 0.2055, \"isr_std\": 0.3194, \"proved_only_isr\": 0.6423, \"isr_by_type\": {\"true\": 0.3598, \"false\": 0.1723, \"unknown\": 0.0979}, \"total_samples\": 100, \"proved_count\": 32, \"runtime_s\": 251.7}, \"conclusion\": \"success\"}, \"plan001-exec-only-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r5\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1, \"mean_isr\": 0.04347, \"last20_prove_rate\": 0.15, \"last20_isr_mean\": 0.04956, \"first20_prove_rate\": 0.08125, \"first20_isr_mean\": 0.05182, \"overall_reward_mean\": 0.07174, \"last20_reward_mean\": 0.09978, \"training_steps\": 100, \"training_minutes\": 16.9, \"step_time_s\": 10.13, \"isr_pr_ratio_overall\": 0.43, \"isr_pr_ratio_last20\": 0.33, \"K\": 8}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r5\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_prove_rate\": 0.11875, \"first20_isr_mean\": 0.11875, \"overall_reward_mean\": 0.15125, \"last20_reward_mean\": 0.2, \"training_steps\": 100, \"training_minutes\": 15.7, \"step_time_s\": 9.44, \"isr_pr_ratio_last20\": 1, \"K\": 8}, \"conclusion\": \"success\"}, \"sta-phase1-exec-sta-r4\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1575, \"mean_isr\": 0.1525, \"last20_prove_rate\": 0.2125, \"last20_isr_mean\": 0.2125, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r4\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-only\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-gt-isr-baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gt_prove_rate\": 0.18, \"gt_mean_isr\": 0.5588, \"gt_isr_std\": 0.2582, \"gt_isr_median\": 0.6125, \"solver_execution_rate\": 1, \"true_prove_rate\": 0.5, \"true_mean_isr\": 0.5833}}, \"sta-phase0-baseline\": {\"status\": \"DONE\", \"metrics\": {\"mean_isr\": 0.0641, \"isr_std\": 0.1983, \"median_isr\": 0, \"isr_range\": [0, 0.889], \"prove_rate\": 0.12, \"proved_count\": 12, \"total_samples\": 100, \"xor_affected_samples\": 34, \"effective_prove_rate_no_xor\": 0.182, \"avg_time_per_sample_s\": 3.4, \"total_runtime_s\": 336, \"isr_by_answer\": {\"true\": {\"n\": 34, \"proved\": 9, \"prove_rate\": 0.265, \"mean_isr\": 0.1345}, \"false\": {\"n\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.024}, \"unknown\": {\"n\": 41, \"proved\": 2, \"prove_rate\": 0.049, \"mean_isr\": 0.0302}}}, \"conclusion\": \"success\"}}, \"count\": 86, \"total\": 86, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3376}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "e7a3f98c-3003-4061-a1d5-5db42004e897",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"plan018-additive-random-b01-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.79, \\\"eval_mean_isr\\\": 0.1038, \\\"eval_isr_std\\\": 0.1369, \\\"eval_median_isr\\\": 0.0357, \\\"eval_proved_only_isr\\\": 0.1314, \\\"eval_n_proved\\\": 79, \\\"eval_n_problems\\\": 100, \\\"tautological_collapse\\\": false, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h7a_count\\\": 0, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 58, \\\"h1_rate\\\": 0.7342, \\\"h8_count\\\": 4, \\\"h8_rate\\\": 0.0506, \\\"genuine_count\\\": 18, \\\"genuine_rate\\\": 0.2278, \\\"taxonomy_tool\\\": \\\"classify_h7.py standard (2026-05-15)\\\", \\\"taxonomy_note\\\": \\\"Re-classified with current classify_h7.py. Old values: genuine_strict=12 (H1_exact=56, H1_near=8, H8=3). New standard: H1=58 (2 former H1-near now H1), H8=4, genuine=18. Standard definition: proved - H7 - H1 - H8.\\\"}}, \\\"plan018-additive-random-b01-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.94, \\\"n_proved\\\": 94, \\\"n_problems\\\": 100, \\\"mean_isr\\\": 0.1406, \\\"isr_std\\\": null, \\\"proved_only_isr\\\": 0.1495, \\\"h7_count\\\": 36, \\\"h7_rate\\\": 0.383, \\\"h7a_count\\\": 36, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 56, \\\"h1_rate\\\": 0.596, \\\"h8_count\\\": 1, \\\"h8_rate\\\": 0.011, \\\"genuine_count\\\": 1, \\\"genuine_rate\\\": 0.0106, \\\"train_prove_rate\\\": 0.5825, \\\"train_mean_isr\\\": 0.1266}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan018-additive-random-b01-s44-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"plan002-additive-b01-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_n_problems\\\": 100, \\\"eval_n_proved\\\": 61, \\\"eval_prove_rate\\\": 0.61, \\\"eval_mean_isr\\\": 0.5063, \\\"eval_isr_std\\\": 0.4518, \\\"eval_median_isr\\\": 0.5, \\\"eval_proved_only_isr\\\": 0.8301, \\\"h7a_count\\\": 59, \\\"h7b_count\\\": 2, \\\"h7_count\\\": 61, \\\"h7_rate\\\": 1, \\\"h1_count\\\": 0, \\\"h1_rate\\\": 0, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"proved_single_premise_ratio\\\": 1, \\\"content_independent_predicates\\\": 5, \\\"isr_eq_1_count\\\": 40, \\\"isr_eq_1_rate_of_proved\\\": 0.656, \\\"train_prove_rate\\\": 0.68775, \\\"train_mean_isr\\\": 0.5039}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan001-exec-only-s43-1000-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.9, \\\"n_proved\\\": 90, \\\"n_problems\\\": 100, \\\"mean_isr\\\": 0.531, \\\"isr_std\\\": 0.15, \\\"isr_corrected\\\": 0.465, \\\"isr_artifact_note\\\": \\\"n_components=3 quantifier decomposition artifact (+0.066) + $T solver bug 5 samples (+0.025). Corrected ISR=0.465, but both values entirely from H7a tautological necessity, no reasoning quality signal.\\\", \\\"h7_count\\\": 90, \\\"h7_rate\\\": 1, \\\"h7a_count\\\": 90, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 0, \\\"h1_rate\\\": 0, \\\"h8_count\\\": 0, \\\"h8_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0}}, \\\"plan016-extended-1000-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.96, \\\"n_proved\\\": 96, \\\"n_problems\\\": 100, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h7a_count\\\": 0, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 96, \\\"h1_rate\\\": 1, \\\"h8_count\\\": 0, \\\"h8_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"genuine_h1_near\\\": 0, \\\"genuine_strict\\\": 0, \\\"content_independent_rate\\\": 1, \\\"single_premise_rate\\\": 0, \\\"taxonomy_audit\\\": \\\"2026-05-15\\\", \\\"taxonomy_tool\\\": \\\"classify_h7.py current version (with H8 detection)\\\", \\\"taxonomy_note\\\": \\\"Re-run with current classify_h7.py. Old value genuine=7 was incorrect (old version lacked H8 and had weaker H1 detection). All 96 proved are H1 (conclusion embedded in premises). 0 H7, 0 H8.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan001-exec-only-s44-1000-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 1, \\\"n_proved\\\": 100, \\\"n_problems\\\": 100, \\\"mean_isr\\\": 0.002, \\\"isr_std\\\": 0.0146, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h7a_count\\\": 0, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 85, \\\"h1_rate\\\": 0.85, \\\"h8_count\\\": 15, \\\"h8_rate\\\": 0.15, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"genuine_note\\\": \\\"D091: 3 samples escape text-match classifiers but are functionally degenerate (ISR=0, disjunctive/commuted bypasses)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan018-additive-random-b01-s42-1000-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.97, \\\"eval_mean_isr\\\": 0.6892, \\\"eval_isr_std\\\": 0.2037, \\\"eval_median_isr\\\": 0.75, \\\"eval_proved_only_isr\\\": 0.7105, \\\"eval_n_proved\\\": 97, \\\"eval_n_problems\\\": 100, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"h1_count\\\": 0, \\\"h1_rate\\\": 0, \\\"h7_count\\\": 97, \\\"h7_rate\\\": 1, \\\"tautological_collapse\\\": true, \\\"train_final_prove_rate\\\": 0.827, \\\"train_final_mean_isr\\\": 0.5213, \\\"train_loss\\\": 0.00671, \\\"train_final_entropy\\\": 0.003, \\\"train_runtime_seconds\\\": 5783, \\\"train_steps\\\": 1000, \\\"eval_by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 25, \\\"prove_rate\\\": 1, \\\"mean_isr\\\": 0.7533}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 39, \\\"prove_rate\\\": 0.951, \\\"mean_isr\\\": 0.6565}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 33, \\\"prove_rate\\\": 0.971, \\\"mean_isr\\\": 0.6814}}, \\\"n_premise_distribution\\\": {\\\"1\\\": 97}, \\\"pattern_description\\\": \\\"All 97 proved: 1 premise identical to conclusion (P therefore P). D088 correction: h7=97 h1=0 (was h1=97 h7=0 pre-D086 bugfix).\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan009-sft-baseline-s44-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.15, \\\"n_proved\\\": 15, \\\"n_problems\\\": 100, \\\"mean_isr\\\": 0.0884, \\\"isr_std\\\": 0.2268, \\\"median_isr\\\": 0, \\\"proved_only_mean_isr\\\": 0.5892, \\\"max_isr\\\": 0.8571, \\\"by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 15, \\\"prove_rate\\\": 0.4412}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 0, \\\"prove_rate\\\": 0}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 0, \\\"prove_rate\\\": 0}}, \\\"genuine_count\\\": 14, \\\"genuine_rate\\\": 0.9333, \\\"h7_strict_count\\\": 0, \\\"h7_strict_rate\\\": 0, \\\"h1_strict_count\\\": 1, \\\"h1_strict_rate\\\": 0.0667, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"conclusion_in_premise_count\\\": 1, \\\"conclusion_in_premise_rate\\\": 0.0667, \\\"content_independent_count\\\": 0, \\\"content_independent_rate\\\": 0, \\\"isr_1_count\\\": 0, \\\"isr_1_rate\\\": 0, \\\"train_final_loss\\\": 0.0171, \\\"train_avg_loss\\\": 0.1544, \\\"train_token_accuracy\\\": 0.995, \\\"train_runtime_s\\\": 1580.97, \\\"eval_elapsed_s\\\": 391.8}}, \\\"plan009-sft-baseline-s43-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.11, \\\"n_proved\\\": 11, \\\"n_problems\\\": 100, \\\"mean_isr\\\": 0.0699, \\\"isr_std\\\": 0.2155, \\\"median_isr\\\": 0, \\\"proved_only_mean_isr\\\": 0.6352, \\\"by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 11, \\\"prove_rate\\\": 0.3235}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 0, \\\"prove_rate\\\": 0}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 0, \\\"prove_rate\\\": 0}}, \\\"genuine_count\\\": 10, \\\"genuine_rate\\\": 0.9091, \\\"h7_strict_count\\\": 0, \\\"h7_strict_rate\\\": 0, \\\"h1_strict_count\\\": 1, \\\"h1_strict_rate\\\": 0.0909, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"conclusion_in_premise_count\\\": 1, \\\"conclusion_in_premise_rate\\\": 0.0909, \\\"content_independent_count\\\": 0, \\\"content_independent_rate\\\": 0, \\\"isr_1_count\\\": 1, \\\"isr_1_rate\\\": 0.0909, \\\"train_final_loss\\\": 0.0167, \\\"train_avg_loss\\\": 0.1551, \\\"train_token_accuracy\\\": 0.9954, \\\"train_runtime_s\\\": 1584.79, \\\"eval_elapsed_s\\\": 326.1}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan009-sft-baseline-s42-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_final_loss\\\": 0.0168, \\\"train_last_step_loss\\\": 0.0168, \\\"train_token_accuracy\\\": 0.9955, \\\"train_epochs\\\": 15.88, \\\"train_runtime_sec\\\": 1415, \\\"train_steps\\\": 1000, \\\"eval_prove_rate\\\": 0.13, \\\"eval_n_proved\\\": 13, \\\"eval_n_problems\\\": 100, \\\"eval_mean_isr\\\": 0.0738, \\\"eval_isr_std\\\": 0.2077, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.5677, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_output_path\\\": \\\"/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json\\\", \\\"h7_strict_count\\\": 0, \\\"h7_strict_rate\\\": 0, \\\"h1_strict_count\\\": 1, \\\"h1_strict_rate\\\": 0.0769, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"genuine_count\\\": 12, \\\"genuine_rate\\\": 0.9231, \\\"conclusion_in_premise_count\\\": 1, \\\"conclusion_in_premise_rate\\\": 0.0769, \\\"isr_1_count\\\": 0, \\\"content_independent_count\\\": 0, \\\"eval_by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 12, \\\"prove_rate\\\": 0.353, \\\"mean_isr\\\": 0.209}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.04, \\\"mean_isr\\\": 0.011}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 0, \\\"prove_rate\\\": 0, \\\"mean_isr\\\": 0}}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp1-random-b03-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.79, \\\"mean_isr\\\": 0.1745, \\\"isr_std\\\": 0.1628, \\\"median_isr\\\": 0.1667, \\\"proved_only_mean_isr\\\": 0.2209, \\\"hacking_rate_strict_h7\\\": 0, \\\"hacking_rate_functional\\\": 0.1013, \\\"genuine_rate\\\": 0.8987, \\\"genuine_count\\\": 71, \\\"n_proved\\\": 79, \\\"n_problems\\\": 100, \\\"h1_conclusion_in_premise\\\": 0.759, \\\"eval_data\\\": \\\"test_100.jsonl\\\", \\\"eval_output\\\": \\\"/root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43.json\\\"}}, \\\"exp1-random-b03-s43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_step\\\": 500, \\\"prove_rate\\\": 0.5505, \\\"mean_isr\\\": 0.1358, \\\"parse_rate\\\": 1, \\\"train_loss\\\": 0.01365, \\\"train_runtime_sec\\\": 6161.1, \\\"epoch\\\": 2, \\\"eval_prove_rate\\\": 0.92, \\\"eval_mean_isr\\\": 0.1659, \\\"eval_isr_std\\\": 0.1147, \\\"eval_median_isr\\\": 0.1429, \\\"eval_proved_only_mean_isr\\\": 0.1803, \\\"eval_min_isr\\\": 0, \\\"eval_max_isr\\\": 0.5, \\\"eval_n_proved\\\": 92, \\\"eval_n_problems\\\": 100, \\\"eval_h7_strict_rate\\\": 0.076, \\\"eval_h7_strict_count\\\": 7, \\\"eval_h1_strict_rate\\\": 0.891, \\\"eval_h1_strict_count\\\": 82, \\\"eval_genuine_rate\\\": 0.0326, \\\"eval_genuine_count\\\": 3, \\\"eval_isr0_count\\\": 6, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 23, \\\"prove_rate\\\": 0.92, \\\"mean_isr\\\": 0.156}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 37, \\\"prove_rate\\\": 0.902, \\\"mean_isr\\\": 0.184}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 32, \\\"prove_rate\\\": 0.941, \\\"mean_isr\\\": 0.151}}, \\\"D086_correction\\\": \\\"H1 90→82, genuine 2→3 per D086 clean batch run\\\"}}, \\\"plan002-additive-b01-s42-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.9, \\\"eval_mean_isr\\\": 0.7892, \\\"eval_isr_std\\\": 0.3424, \\\"eval_proved_only_isr\\\": 0.8769, \\\"eval_median_isr\\\": 1, \\\"eval_n_proved\\\": 90, \\\"eval_n_problems\\\": 100, \\\"eval_component_count_mean\\\": 2.889, \\\"tautological_collapse\\\": true, \\\"train_final_prove_rate\\\": 0.855, \\\"train_final_mean_isr\\\": 0.532, \\\"h7_count\\\": 87, \\\"h7_rate\\\": 0.9667, \\\"h1_count\\\": 0, \\\"h1_rate\\\": 0, \\\"h1_near_count\\\": 1, \\\"h1_near_rate\\\": 0.0111, \\\"h8_conjunction_collapse_count\\\": 1, \\\"h8_conjunction_collapse_rate\\\": 0.0111, \\\"genuine_count\\\": 2, \\\"genuine_rate\\\": 0.0222, \\\"taxonomy_standard\\\": \\\"D086 clean run = ground truth. D084 residual removed.\\\"}}, \\\"plan002-additive-b01-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.89, \\\"eval_mean_isr\\\": 0.803, \\\"eval_isr_std\\\": null, \\\"eval_proved_only_isr\\\": 0.902, \\\"eval_n_proved\\\": 89, \\\"eval_n_problems\\\": 100, \\\"h7_count\\\": 89, \\\"h7_rate\\\": 1, \\\"h1_count\\\": 0, \\\"h1_rate\\\": 0, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"component_mean\\\": 4.33, \\\"comp_2_ratio\\\": 0.022, \\\"h7_fn_correction\\\": \\\"12 former genuine reclassified as H7: all n_prem=1 false negatives (normalization mismatch prevented conclusion matching)\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan013-random-reward-s42-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 1, \\\"eval_mean_isr\\\": 0.535, \\\"eval_isr_std\\\": 0.1282, \\\"eval_proved_only_isr\\\": 0.535, \\\"eval_median_isr\\\": 0.5, \\\"eval_n_proved\\\": 100, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_note\\\": \\\"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\\\"}}, \\\"plan001-exec-only-s43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_sampling_prove_rate\\\": 0.14, \\\"eval_sampling_mean_isr\\\": 0, \\\"eval_sampling_n_proved\\\": 14, \\\"eval_sampling_temperature\\\": 0.7, \\\"eval_sampling_method\\\": \\\"do_sample=True, temperature=0.7\\\", \\\"eval_sampling_by_answer\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 6, \\\"prove_rate\\\": 0.176}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 2, \\\"prove_rate\\\": 0.08}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 6, \\\"prove_rate\\\": 0.146}}, \\\"eval_greedy_prove_rate\\\": 0.13, \\\"eval_greedy_mean_isr\\\": 0, \\\"eval_greedy_proved_only_isr\\\": 0, \\\"eval_greedy_n_proved\\\": 13, \\\"eval_greedy_method\\\": \\\"eval_sta.py default (do_sample=False)\\\", \\\"eval_greedy_by_answer\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 4, \\\"prove_rate\\\": 0.118}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 5, \\\"prove_rate\\\": 0.2}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 4, \\\"prove_rate\\\": 0.0976}}, \\\"eval_greedy_h7_count\\\": 0, \\\"eval_greedy_h7_rate\\\": 0, \\\"eval_greedy_h1_count\\\": 13, \\\"eval_greedy_h1_rate\\\": 1, \\\"eval_greedy_genuine_rate\\\": 0, \\\"eval_greedy_n_premises_proved_mean\\\": 17.92, \\\"eval_greedy_mean_components_proved\\\": 18.92, \\\"eval_greedy_n_premises_all_mean\\\": 32.67, \\\"eval_sampling_h1_rate\\\": 1, \\\"eval_sampling_h7_rate\\\": 0, \\\"eval_sampling_genuine_rate\\\": 0, \\\"eval_sampling_mean_components_proved\\\": 18.5, \\\"eval_greedy_vs_sampling_delta_pr\\\": -0.01, \\\"eval_method_note\\\": \\\"Greedy and sampling agree on failure profile (ISR*=0, H1=100%, components~18.5-18.9). s43 collapse is decoding-invariant.\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan001-exec-only-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan017-additive-random-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.48, \\\"eval_mean_isr\\\": 0.0453, \\\"eval_isr_std\\\": 0.0759, \\\"eval_median_isr\\\": 0, \\\"eval_max_isr\\\": 0.2857, \\\"eval_proved_only_isr\\\": 0.0943, \\\"eval_n_proved\\\": 48, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_component_count_mean\\\": 9.6, \\\"eval_component_count_2_ratio\\\": 0, \\\"tautological_collapse\\\": false, \\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 1, \\\"h1_count\\\": 48, \\\"genuine_rate\\\": 0, \\\"genuine_count\\\": 0}}, \\\"plan002-additive-b01-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.81, \\\"eval_mean_isr\\\": 0.3365, \\\"eval_isr_std\\\": 0.3227, \\\"eval_proved_only_isr\\\": 0.4154, \\\"eval_median_isr\\\": 0.2, \\\"eval_n_proved\\\": 81, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_component_count_mean\\\": 5.58, \\\"h7_rate\\\": 0.16, \\\"h7_count\\\": 13, \\\"h1_rate\\\": 0.519, \\\"h1_count\\\": 42, \\\"h8_conjunction_collapse_count\\\": 12, \\\"h8_conjunction_collapse_rate\\\": 0.148, \\\"genuine_rate\\\": 0.173, \\\"genuine_count\\\": 14, \\\"tautological_collapse\\\": false, \\\"h8_audit_note\\\": \\\"2026-05-15: H8 conjunction collapse audit completed. 12/81 proved samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json\\\"}}, \\\"plan002-additive-b01-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.61, \\\"eval_n_proved\\\": 61, \\\"eval_n_problems\\\": 100, \\\"eval_proved_only_isr\\\": 0.83, \\\"h7_count\\\": 59, \\\"h7_rate\\\": 0.9672, \\\"h1_count\\\": 0, \\\"h1_rate\\\": 0, \\\"h1_near_count\\\": 0, \\\"h1_near_rate\\\": 0, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"genuine_count\\\": 2, \\\"genuine_rate\\\": 0.0328, \\\"proved_single_premise_ratio\\\": 1, \\\"taxonomy_note\\\": \\\"structurally determined: proved_single_premise_ratio=1.0, all taxonomy categories except H7 are zero by construction. eval file lost but classification derivable from structure.\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp1-isr-b03-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.91, \\\"mean_isr\\\": 0.2575, \\\"isr_std\\\": 0.2363, \\\"median_isr\\\": 0.3333, \\\"proved_only_mean_isr\\\": 0.283, \\\"hacking_rate_strict_h7\\\": 0.022, \\\"hacking_rate_functional\\\": 0.3297, \\\"genuine_rate\\\": 0.6703, \\\"genuine_count\\\": 61, \\\"n_proved\\\": 91, \\\"n_problems\\\": 100, \\\"h1_conclusion_in_premise\\\": 0.747, \\\"eval_data\\\": \\\"test_100.jsonl\\\", \\\"eval_output\\\": \\\"/root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s43.json\\\"}}, \\\"plan009-sft-baseline-s44-1000-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.15, \\\"eval_n_proved\\\": 15, \\\"eval_n_problems\\\": 100, \\\"eval_mean_isr\\\": 0.0884, \\\"eval_isr_std\\\": 0.2268, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.5892, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h1_count\\\": 1, \\\"h1_rate\\\": 0.0667, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"genuine_count\\\": 14, \\\"genuine_rate\\\": 0.9333, \\\"eval_by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 15, \\\"prove_rate\\\": 0.441, \\\"mean_isr\\\": 0.26}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 0, \\\"prove_rate\\\": 0, \\\"mean_isr\\\": 0}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 0, \\\"prove_rate\\\": 0, \\\"mean_isr\\\": 0}}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan009-sft-baseline-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_final_loss\\\": 0.2397, \\\"train_last_step_loss\\\": 0.0328, \\\"train_token_accuracy\\\": 0.9928, \\\"train_epochs\\\": 7.94, \\\"train_runtime_sec\\\": 729.05, \\\"train_steps\\\": 500, \\\"eval_prove_rate\\\": 0.17, \\\"eval_n_proved\\\": 17, \\\"eval_n_problems\\\": 100, \\\"eval_mean_isr\\\": 0.0974, \\\"eval_isr_std\\\": 0.2409, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.5729, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_output_path\\\": \\\"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s44.json\\\", \\\"eval_tautological_collapse\\\": false, \\\"eval_h7_count\\\": 0, \\\"eval_h7_rate\\\": 0, \\\"eval_h1_count\\\": 2, \\\"eval_h1_rate\\\": 0.118, \\\"eval_genuine_count\\\": 15, \\\"eval_genuine_rate\\\": 0.882, \\\"eval_by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 15, \\\"prove_rate\\\": 0.441, \\\"mean_isr\\\": 0.257}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.04, \\\"mean_isr\\\": 0.027}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.024, \\\"mean_isr\\\": 0.008}}, \\\"eval_correction_note\\\": \\\"Corrected 2026-05-15: previous eval used test_100.jsonl (50/44/6 distribution), re-evaled with proofwriter_fol_100.jsonl (34/25/41)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan009-sft-baseline-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.2391, \\\"train_token_accuracy\\\": 0.9938, \\\"train_epochs\\\": 7.94, \\\"train_runtime_sec\\\": 677.14, \\\"train_steps\\\": 500, \\\"eval_prove_rate\\\": 0.15, \\\"eval_mean_isr\\\": 0.0895, \\\"eval_isr_std\\\": 0.2338, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.5967, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h1_count\\\": 1, \\\"h1_rate\\\": 0.067, \\\"genuine_count\\\": 14, \\\"genuine_rate\\\": 0.933, \\\"by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 13, \\\"prove_rate\\\": 0.382, \\\"mean_isr\\\": 0.234}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.04, \\\"mean_isr\\\": 0.027}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.024, \\\"mean_isr\\\": 0.008}}, \\\"eval_data_path\\\": \\\"data/proofwriter_fol_100.jsonl\\\", \\\"eval_output_path\\\": \\\"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s43.json\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan001-exec-only-s44-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan001-exec-only-s43-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan009-sft-baseline-s44-1000-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan002-additive-b03-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_steps\\\": 500, \\\"duration_min\\\": 56.7, \\\"overall_prove_rate\\\": 0.34025, \\\"overall_isr\\\": 0.11527, \\\"last100_prove_rate\\\": 0.5525, \\\"eval_prove_rate\\\": 0.18, \\\"eval_mean_isr\\\": 0.0257, \\\"eval_isr_std\\\": 0.0742, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.1427, \\\"eval_n_proved\\\": 18, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 0.778, \\\"h1_count\\\": 14, \\\"h8_conjunction_collapse_count\\\": 3, \\\"h8_conjunction_collapse_rate\\\": 0.1667, \\\"genuine_rate\\\": 0.0556, \\\"genuine_count\\\": 1, \\\"eval_by_type_false_pr\\\": 0.12, \\\"eval_by_type_false_isr\\\": 0.0102, \\\"eval_by_type_unknown_pr\\\": 0.195, \\\"eval_by_type_unknown_isr\\\": 0.0422, \\\"eval_by_type_true_pr\\\": 0.206, \\\"eval_by_type_true_isr\\\": 0.0172, \\\"h8_audit_note\\\": \\\"2026-05-15: H8 conjunction collapse added. genuine 4→1.\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan001-exec-only-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.93, \\\"eval_mean_isr\\\": 0.1232, \\\"eval_isr_std\\\": 0.1887, \\\"eval_proved_only_isr\\\": 0.1324, \\\"eval_median_isr\\\": 0, \\\"eval_n_proved\\\": 93, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 0.871, \\\"h1_count\\\": 81, \\\"h8_conjunction_collapse_count\\\": 6, \\\"h8_conjunction_collapse_rate\\\": 0.0645, \\\"genuine_rate\\\": 0.0753, \\\"genuine_count\\\": 7, \\\"genuine_mean_isr\\\": 0.3141, \\\"h1_mean_isr\\\": 0.1055, \\\"conclusion_embedding_total\\\": 0.871, \\\"content_independent_predicates_count\\\": 1, \\\"h8_audit_note\\\": \\\"2026-05-15: H8 conjunction collapse added. genuine 12→7.\\\"}}, \\\"plan004-o1-ablation-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.63, \\\"mean_isr\\\": 0.0072, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h1_count\\\": 63, \\\"h1_rate\\\": 1, \\\"h8_conjunction_collapse_count\\\": 2, \\\"h8_conjunction_collapse_rate\\\": 0.0317, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"content_independent_predicates_count\\\": 3, \\\"h8_audit_note\\\": \\\"2026-05-15: H8 conjunction collapse added. genuine unchanged (0).\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp1-isr-b03-s42-1000-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.95, \\\"eval_mean_isr\\\": 0.734, \\\"eval_isr_std\\\": 0.2575, \\\"eval_median_isr\\\": 0.6, \\\"eval_proved_only_isr\\\": 0.7726, \\\"eval_n_proved\\\": 95, \\\"eval_n_problems\\\": 100, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 25, \\\"prove_rate\\\": 1, \\\"mean_isr\\\": 0.824}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 38, \\\"prove_rate\\\": 0.927, \\\"mean_isr\\\": 0.673}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 32, \\\"prove_rate\\\": 0.941, \\\"mean_isr\\\": 0.741}}, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h1_count\\\": 54, \\\"h1_rate\\\": 0.568, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"tautological_collapse\\\": true, \\\"isr_1_count\\\": 41, \\\"isr_1_rate\\\": 0.432, \\\"single_premise_count\\\": 0, \\\"train_final_prove_rate\\\": 0.829, \\\"train_final_mean_isr\\\": 0.727, \\\"train_loss\\\": 0.0041, \\\"train_runtime_seconds\\\": 6280, \\\"train_final_entropy\\\": 9e-06, \\\"completions_mean_length\\\": 47, \\\"h8_conjunction_collapse_count\\\": 41, \\\"h8_conjunction_collapse_rate\\\": 0.432, \\\"content_independent_predicates\\\": true}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan018-additive-random-b01-s42-1000-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_final_prove_rate\\\": 0.989, \\\"train_final_mean_isr\\\": 0.353, \\\"train_final_reward\\\": 1.062, \\\"train_steps\\\": 1000, \\\"train_runtime_seconds\\\": 2957, \\\"eval_prove_rate\\\": 1, \\\"eval_mean_isr\\\": 0.3333, \\\"eval_isr_std\\\": 0, \\\"eval_median_isr\\\": 0.3333, \\\"eval_proved_only_isr\\\": 0.3333, \\\"eval_n_proved\\\": 100, \\\"eval_n_problems\\\": 100, \\\"eval_component_count_mean\\\": 3, \\\"genuine_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"tautological_collapse\\\": true, \\\"h7_rate\\\": null, \\\"h7_count\\\": null, \\\"h1_rate\\\": null, \\\"h1_count\\\": null}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan018-additive-random-b01-s42-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp1-isr-b03-s42-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan001-exec-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.98, \\\"eval_mean_isr\\\": 0.57, \\\"eval_isr_std\\\": 0.2013, \\\"eval_median_isr\\\": 0.5, \\\"eval_proved_only_isr\\\": 0.5816, \\\"eval_n_proved\\\": 98, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_component_count_mean\\\": 2.04, \\\"eval_component_count_2\\\": 94, \\\"eval_component_count_3\\\": 4, \\\"tautological_collapse\\\": true, \\\"h7_rate\\\": 1, \\\"h7_count\\\": 97, \\\"h1_rate\\\": 0, \\\"h1_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"conclusion_embedding_total\\\": 1}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan018-additive-random-b01-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 93.2, \\\"h1_count\\\": 82, \\\"genuine_rate\\\": 6.8, \\\"genuine_count\\\": 6, \\\"eval_prove_rate\\\": 0.88, \\\"eval_mean_isr\\\": 0.058}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp1-random-b03-s44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.23, \\\"eval_proved_only_mean_isr\\\": 0, \\\"eval_mean_isr\\\": 0, \\\"eval_isr_std\\\": 0, \\\"eval_median_isr\\\": 0, \\\"eval_n_proved\\\": 23, \\\"eval_n_problems\\\": 100, \\\"eval_h7_strict_rate\\\": 0, \\\"eval_h7_strict_count\\\": 0, \\\"eval_h1_strict_rate\\\": 1, \\\"eval_h1_strict_count\\\": 23, \\\"eval_genuine_rate\\\": 0, \\\"eval_genuine_count\\\": 0, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\"}}, \\\"exp1-isr-b03-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_step\\\": 500, \\\"prove_rate\\\": 0.56125, \\\"mean_isr\\\": 0.1515, \\\"parse_rate\\\": 1, \\\"train_loss\\\": 0.0176, \\\"train_runtime_sec\\\": 4153.6, \\\"epoch\\\": 2, \\\"eval_prove_rate\\\": 0.86, \\\"eval_mean_isr\\\": 0.2535, \\\"eval_isr_std\\\": 0.2406, \\\"eval_median_isr\\\": 0.3333, \\\"eval_proved_only_mean_isr\\\": 0.2948, \\\"eval_min_isr\\\": 0, \\\"eval_max_isr\\\": 0.75, \\\"eval_n_proved\\\": 86, \\\"eval_n_problems\\\": 100, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_h7_strict_rate\\\": 0.047, \\\"eval_h7_strict_count\\\": 4, \\\"eval_h1_strict_rate\\\": 0.686, \\\"eval_h1_strict_count\\\": 59, \\\"eval_conclusion_in_premise_rate\\\": 0.733, \\\"eval_conclusion_in_premise_count\\\": 63, \\\"eval_genuine_rate\\\": 0.267, \\\"eval_genuine_count\\\": 23, \\\"eval_single_premise_rate\\\": 0.058, \\\"eval_single_premise_count\\\": 5, \\\"eval_isr_1_count\\\": 0, \\\"eval_by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 23, \\\"prove_rate\\\": 0.92, \\\"mean_isr\\\": 0.334}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 35, \\\"prove_rate\\\": 0.854, \\\"mean_isr\\\": 0.199}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 28, \\\"prove_rate\\\": 0.824, \\\"mean_isr\\\": 0.26}}}}, \\\"exp1-random-b03-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan015-linear-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp1-isr-b03-s43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp1-random-b03-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp1-isr-b03-s44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.95, \\\"mean_isr\\\": 0.705, \\\"isr_std\\\": 0.172, \\\"proved_only_isr\\\": 0.7421, \\\"n_proved\\\": 95, \\\"n_problems\\\": 100, \\\"h7_rate\\\": 1, \\\"h7_count\\\": 95, \\\"h1_rate\\\": 0, \\\"h1_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"single_premise_rate\\\": 1, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_note\\\": \\\"Re-eval with correct test set (D062). Previous test_100.jsonl results invalidated.\\\"}}, \\\"exp1-random-b03-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp1-isr-b03-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp1-isr-b03-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp2-exec-s43-greedy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp4-100step-h1h7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan006-prolog-sta-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"pass_rate\\\": 0.97, \\\"isr_mean\\\": 0.885, \\\"isr_n_cl_ge3\\\": \\\"N/A (0 samples)\\\", \\\"n_clauses_dist\\\": \\\"78/100 single-clause, 22/100 two-clause\\\", \\\"h7_functional_rate\\\": 0.979, \\\"genuine_rate\\\": 0, \\\"premise_count_analysis\\\": \\\"100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs\\\", \\\"failure_mode\\\": \\\"query-as-fact gaming (total H7 collapse)\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan006-prolog-sta-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train\\\": {\\\"final_prove_rate\\\": 0.769, \\\"final_mean_isr\\\": 0.129, \\\"final_loss\\\": 0.0155, \\\"final_entropy\\\": 0.09, \\\"final_reward\\\": 0.573, \\\"completion_length_mean\\\": 143, \\\"train_runtime_seconds\\\": 5095, \\\"train_runtime_minutes\\\": 84.9}, \\\"eval\\\": {\\\"n_problems\\\": 100, \\\"n_proved\\\": 38, \\\"prove_rate\\\": 0.38, \\\"mean_isr\\\": 0.0704, \\\"isr_std\\\": 0.1263, \\\"median_isr\\\": 0, \\\"proved_only_mean_isr\\\": 0.1853, \\\"min_isr\\\": 0, \\\"max_isr\\\": 1, \\\"by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 11, \\\"prove_rate\\\": 0.44, \\\"mean_isr\\\": 0.1003}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 11, \\\"prove_rate\\\": 0.268, \\\"mean_isr\\\": 0.0394}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 16, \\\"prove_rate\\\": 0.471, \\\"mean_isr\\\": 0.0859}}}, \\\"h7_classification\\\": {\\\"h7_strict\\\": 0, \\\"h7_rate\\\": 0, \\\"h1_strict\\\": 37, \\\"h1_rate\\\": 0.974, \\\"conclusion_in_premise_total\\\": 37, \\\"conclusion_in_premise_rate\\\": 0.974, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"isr_1_count\\\": 1, \\\"note\\\": \\\"1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause; all 38/38 proved samples are tautological\\\"}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan006-prolog-sta-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"cumulative_prove_rate\\\": 0.848, \\\"cumulative_mean_isr\\\": 0.787, \\\"final_prove_rate\\\": 1, \\\"final_isr\\\": 1, \\\"final_reward\\\": 1, \\\"saturation_onset_step\\\": 100, \\\"train_loss\\\": 0.00716, \\\"training_hours\\\": 0.78, \\\"final_entropy\\\": 0.01, \\\"final_completion_length\\\": 27, \\\"initial_completion_length\\\": 120, \\\"steps_at_perfect_reward\\\": 400, \\\"train_runtime_sec\\\": 2791, \\\"eval_prove_rate\\\": 0.5, \\\"eval_mean_isr\\\": 0.5, \\\"eval_proved_only_isr\\\": 1, \\\"eval_h7_rate\\\": 1, \\\"eval_h7_count\\\": 50, \\\"eval_proved_count\\\": 50, \\\"eval_total_count\\\": 100, \\\"eval_n_clauses_mean\\\": 1, \\\"eval_isr_distribution\\\": \\\"binary: 50x0 + 50x1\\\"}}, \\\"plan006-prolog-exec-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.21, \\\"eval_mean_isr\\\": 0.0812, \\\"eval_isr_std\\\": 0.2343, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.3866, \\\"eval_min_isr\\\": 0, \\\"eval_max_isr\\\": 1, \\\"eval_n_proved\\\": 21, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_elapsed_seconds\\\": 683.9, \\\"eval_by_type_false_pr\\\": 0.04, \\\"eval_by_type_false_isr\\\": 0.04, \\\"eval_by_type_unknown_pr\\\": 0.317, \\\"eval_by_type_unknown_isr\\\": 0.099, \\\"eval_by_type_true_pr\\\": 0.206, \\\"eval_by_type_true_isr\\\": 0.09, \\\"solver\\\": \\\"PrologSolver\\\", \\\"logic_type\\\": \\\"prolog\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan009-sft-baseline-s42-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.14, \\\"eval_mean_isr\\\": 0.08, \\\"eval_isr_std\\\": 0.214, \\\"eval_median_isr\\\": 0, \\\"eval_max_isr\\\": 0.833, \\\"eval_proved_only_isr\\\": 0.571, \\\"eval_n_proved\\\": 14, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"train_final_loss\\\": 0.0287, \\\"train_token_accuracy\\\": 0.9935, \\\"train_epochs\\\": 7.94, \\\"train_runtime_sec\\\": 789.6, \\\"by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 13, \\\"pr\\\": 0.382, \\\"isr\\\": 0.226}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 1, \\\"pr\\\": 0.024, \\\"isr\\\": 0.008}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 0, \\\"pr\\\": 0, \\\"isr\\\": 0}}, \\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 0.071, \\\"h1_count\\\": 1, \\\"genuine_rate\\\": 0.929, \\\"genuine_count\\\": 13, \\\"hacking_patterns\\\": \\\"near-zero (1/14 H1, 0 H7, 92.9% genuine)\\\", \\\"tautological_collapse\\\": false}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan006-prolog-exec-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.56, \\\"eval_mean_isr\\\": 0.0084, \\\"eval_isr_std\\\": 0.0221, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.015, \\\"eval_min_isr\\\": 0, \\\"eval_max_isr\\\": 0.1, \\\"eval_n_proved\\\": 56, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_elapsed_seconds\\\": 868.2, \\\"eval_by_type_false_pr\\\": 0.48, \\\"eval_by_type_false_isr\\\": 0.0043, \\\"eval_by_type_unknown_pr\\\": 0.6585, \\\"eval_by_type_unknown_isr\\\": 0.0114, \\\"eval_by_type_true_pr\\\": 0.5, \\\"eval_by_type_true_isr\\\": 0.0078, \\\"solver\\\": \\\"PrologSolver\\\", \\\"logic_type\\\": \\\"prolog\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan018-additive-random-b01-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.89, \\\"mean_isr\\\": 0.0619, \\\"isr_std\\\": 0.1756, \\\"median_isr\\\": 0, \\\"proved_only_mean_isr\\\": 0.0695, \\\"n_proved\\\": 89, \\\"n_problems\\\": 100, \\\"max_isr\\\": 1, \\\"min_isr\\\": 0, \\\"isr_pr_ratio\\\": 0.0695, \\\"isr_zero_count\\\": 72, \\\"isr_one_count\\\": 2, \\\"by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 21, \\\"prove_rate\\\": 0.84, \\\"mean_isr\\\": 0.0533}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 40, \\\"prove_rate\\\": 0.976, \\\"mean_isr\\\": 0.0892}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 28, \\\"prove_rate\\\": 0.824, \\\"mean_isr\\\": 0.0353}}, \\\"elapsed_seconds\\\": 1012.7, \\\"eval_method\\\": \\\"eval_sta.py with Prover9Solver, FOL\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan009-sft-baseline-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"plan006-prolog-exec-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan006-prolog-exec-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.83, \\\"eval_mean_isr\\\": 0.031, \\\"eval_proved_only_isr\\\": 0.037, \\\"eval_median_isr\\\": 0, \\\"eval_max_isr\\\": 0.2, \\\"eval_isr_std\\\": 0.0534, \\\"h7_rate\\\": 0, \\\"h1_rate\\\": 0, \\\"isr_1_rate\\\": 0, \\\"single_premise_rate\\\": 0, \\\"by_answer_type\\\": {\\\"true\\\": {\\\"proved\\\": 37, \\\"count\\\": 40, \\\"pr\\\": 0.925, \\\"isr\\\": 0.037}, \\\"false\\\": {\\\"proved\\\": 21, \\\"count\\\": 29, \\\"pr\\\": 0.724, \\\"isr\\\": 0.038}, \\\"unknown\\\": {\\\"proved\\\": 25, \\\"count\\\": 31, \\\"pr\\\": 0.806, \\\"isr\\\": 0.016}}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan006-prolog-exec-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"plan009-sft-baseline-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan009-sft-baseline-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan018-additive-random-b01-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan012-hacking-taxonomy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"isr_b01_genuine_rate\\\": 0.259, \\\"random_b01_genuine_rate\\\": 0.177, \\\"genuine_rate_delta_pp\\\": 8.2, \\\"isr_b01_conclusion_embedding_rate\\\": 0.728, \\\"random_b01_conclusion_embedding_rate\\\": 0.785, \\\"isr_b01_genuine_mean_isr\\\": 0.6723, \\\"random_b01_genuine_mean_isr\\\": 0.3427, \\\"isr_b01_complexity_wo_utility_rate\\\": 0, \\\"random_b01_complexity_wo_utility_rate\\\": 0.038, \\\"isr_b01_hacking_rate\\\": 0.741, \\\"random_b01_hacking_rate\\\": 0.823}}, \\\"plan005-sta-low-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"total_steps\\\": 500, \\\"duration_min\\\": 71, \\\"parse_rate\\\": 1, \\\"overall_prove_rate\\\": 0.5657, \\\"overall_isr\\\": 0.1682, \\\"last50_prove_rate\\\": 0.77, \\\"last50_isr\\\": 0.2559, \\\"last100_prove_rate\\\": 0.7725, \\\"last100_isr\\\": 0.2299, \\\"last100_loss\\\": 0.022752, \\\"overall_loss\\\": 0.017296, \\\"last100_isr_pr_ratio\\\": 0.298, \\\"last100_isr_lt_pr_count\\\": \\\"99/100\\\", \\\"first_rolling10_pr_ge_0.8\\\": 178, \\\"first_rolling10_pr_ge_0.9\\\": 439, \\\"max_rolling10_pr\\\": 0.9375, \\\"max_rolling10_isr\\\": 0.3282, \\\"windowed\\\": {\\\"1-50\\\": {\\\"pr\\\": 0.1775, \\\"isr\\\": 0.0906}, \\\"51-100\\\": {\\\"pr\\\": 0.1775, \\\"isr\\\": 0.0835}, \\\"101-200\\\": {\\\"pr\\\": 0.5062, \\\"isr\\\": 0.1463}, \\\"201-300\\\": {\\\"pr\\\": 0.6713, \\\"isr\\\": 0.1791}, \\\"301-400\\\": {\\\"pr\\\": 0.7013, \\\"isr\\\": 0.1984}, \\\"401-500\\\": {\\\"pr\\\": 0.7725, \\\"isr\\\": 0.2299}}}}, \\\"plan014-downstream-nli-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"overall_accuracy\\\": 0.341, \\\"proved_rate\\\": 0.915, \\\"proved_count\\\": 732, \\\"total_generations\\\": 800, \\\"parse_errors\\\": 0, \\\"accuracy_by_label\\\": {\\\"true\\\": 0.912, \\\"false\\\": 0, \\\"unknown\\\": 0.076}, \\\"spearman_rho\\\": -0.049, \\\"spearman_p\\\": 0.187, \\\"mann_whitney_U\\\": 17202, \\\"mann_whitney_p\\\": 0.288, \\\"bon_isr_accuracy\\\": 0.35, \\\"bon_random_accuracy\\\": 0.341, \\\"bon_oracle_accuracy\\\": 0.44, \\\"bon_prove_first_accuracy\\\": 0.35, \\\"isr_bucket_high_acc\\\": 0.75, \\\"isr_bucket_mid_acc\\\": 0.377, \\\"isr_bucket_low_acc\\\": 0.327, \\\"runtime_inference_s\\\": 408.8, \\\"runtime_eval_s\\\": 13.6}}, \\\"plan001-exec-only-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan013-random-reward-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan001-exec-only-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan013-random-reward-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan013-random-reward-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan001-exec-only-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan003-eval-exec-only-r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.32, \\\"mean_isr\\\": 0.2055, \\\"isr_std\\\": 0.3194, \\\"proved_only_isr\\\": 0.6423, \\\"isr_by_type\\\": {\\\"true\\\": 0.3598, \\\"false\\\": 0.1723, \\\"unknown\\\": 0.0979}, \\\"total_samples\\\": 100, \\\"proved_count\\\": 32, \\\"runtime_s\\\": 251.7}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan001-exec-only-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-sta-r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.1, \\\"mean_isr\\\": 0.04347, \\\"last20_prove_rate\\\": 0.15, \\\"last20_isr_mean\\\": 0.04956, \\\"first20_prove_rate\\\": 0.08125, \\\"first20_isr_mean\\\": 0.05182, \\\"overall_reward_mean\\\": 0.07174, \\\"last20_reward_mean\\\": 0.09978, \\\"training_steps\\\": 100, \\\"training_minutes\\\": 16.9, \\\"step_time_s\\\": 10.13, \\\"isr_pr_ratio_overall\\\": 0.43, \\\"isr_pr_ratio_last20\\\": 0.33, \\\"K\\\": 8}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"sta-phase1-exec-only-r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.15125, \\\"mean_isr\\\": 0.1475, \\\"last20_prove_rate\\\": 0.2, \\\"last20_isr_mean\\\": 0.2, \\\"first20_prove_rate\\\": 0.11875, \\\"first20_isr_mean\\\": 0.11875, \\\"overall_reward_mean\\\": 0.15125, \\\"last20_reward_mean\\\": 0.2, \\\"training_steps\\\": 100, \\\"training_minutes\\\": 15.7, \\\"step_time_s\\\": 9.44, \\\"isr_pr_ratio_last20\\\": 1, \\\"K\\\": 8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sta-phase1-exec-sta-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.1575, \\\"mean_isr\\\": 0.1525, \\\"last20_prove_rate\\\": 0.2125, \\\"last20_isr_mean\\\": 0.2125, \\\"first20_reward_mean\\\": 0.119, \\\"training_steps\\\": 100, \\\"training_minutes\\\": 15}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"sta-phase1-exec-only-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.15125, \\\"mean_isr\\\": 0.1475, \\\"last20_prove_rate\\\": 0.2, \\\"last20_isr_mean\\\": 0.2, \\\"first20_reward_mean\\\": 0.119, \\\"training_steps\\\": 100, \\\"training_minutes\\\": 15}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"sta-phase1-exec-only-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-sta-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-sta-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-only-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-sta\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-gt-isr-baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gt_prove_rate\\\": 0.18, \\\"gt_mean_isr\\\": 0.5588, \\\"gt_isr_std\\\": 0.2582, \\\"gt_isr_median\\\": 0.6125, \\\"solver_execution_rate\\\": 1, \\\"true_prove_rate\\\": 0.5, \\\"true_mean_isr\\\": 0.5833}}, \\\"sta-phase0-baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"mean_isr\\\": 0.0641, \\\"isr_std\\\": 0.1983, \\\"median_isr\\\": 0, \\\"isr_range\\\": [0, 0.889], \\\"prove_rate\\\": 0.12, \\\"proved_count\\\": 12, \\\"total_samples\\\": 100, \\\"xor_affected_samples\\\": 34, \\\"effective_prove_rate_no_xor\\\": 0.182, \\\"avg_time_per_sample_s\\\": 3.4, \\\"total_runtime_s\\\": 336, \\\"isr_by_answer\\\": {\\\"true\\\": {\\\"n\\\": 34, \\\"proved\\\": 9, \\\"prove_rate\\\": 0.265, \\\"mean_isr\\\": 0.1345}, \\\"false\\\": {\\\"n\\\": 25, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.04, \\\"mean_isr\\\": 0.024}, \\\"unknown\\\": {\\\"n\\\": 41, \\\"proved\\\": 2, \\\"prove_rate\\\": 0.049, \\\"mean_isr\\\": 0.0302}}}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 86, \\\"total\\\": 86, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3376}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan018-additive-random-b01-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.79, \"eval_mean_isr\": 0.1038, \"eval_isr_std\": 0.1369, \"eval_median_isr\": 0.0357, \"eval_proved_only_isr\": 0.1314, \"eval_n_proved\": 79, \"eval_n_problems\": 100, \"tautological_collapse\": false, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 58, \"h1_rate\": 0.7342, \"h8_count\": 4, \"h8_rate\": 0.0506, \"genuine_count\": 18, \"genuine_rate\": 0.2278, \"taxonomy_tool\": \"classify_h7.py standard (2026-05-15)\", \"taxonomy_note\": \"Re-classified with current classify_h7.py. Old values: genuine_strict=12 (H1_exact=56, H1_near=8, H8=3). New standard: H1=58 (2 former H1-near now H1), H8=4, genuine=18. Standard definition: proved - H7 - H1 - H8.\"}}, \"plan018-additive-random-b01-s43-r3\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.94, \"n_proved\": 94, \"n_problems\": 100, \"mean_isr\": 0.1406, \"isr_std\": null, \"proved_only_isr\": 0.1495, \"h7_count\": 36, \"h7_rate\": 0.383, \"h7a_count\": 36, \"h7b_count\": 0, \"h1_count\": 56, \"h1_rate\": 0.596, \"h8_count\": 1, \"h8_rate\": 0.011, \"genuine_count\": 1, \"genuine_rate\": 0.0106, \"train_prove_rate\": 0.5825, \"train_mean_isr\": 0.1266}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s44-r2\": {\"status\": \"RUNNING\"}, \"plan002-additive-b01-s43-r2\": {\"status\": \"DONE\", \"metrics\": {\"eval_n_problems\": 100, \"eval_n_proved\": 61, \"eval_prove_rate\": 0.61, \"eval_mean_isr\": 0.5063, \"eval_isr_std\": 0.4518, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.8301, \"h7a_count\": 59, \"h7b_count\": 2, \"h7_count\": 61, \"h7_rate\": 1, \"h1_count\": 0, \"h1_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"proved_single_premise_ratio\": 1, \"content_independent_predicates\": 5, \"isr_eq_1_count\": 40, \"isr_eq_1_rate_of_proved\": 0.656, \"train_prove_rate\": 0.68775, \"train_mean_isr\": 0.5039}, \"conclusion\": \"negative\"}, \"plan001-exec-only-s43-1000-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.9, \"n_proved\": 90, \"n_problems\": 100, \"mean_isr\": 0.531, \"isr_std\": 0.15, \"isr_corrected\": 0.465, \"isr_artifact_note\": \"n_components=3 quantifier decomposition artifact (+0.066) + $T solver bug 5 samples (+0.025). Corrected ISR=0.465, but both values entirely from H7a tautological necessity, no reasoning quality signal.\", \"h7_count\": 90, \"h7_rate\": 1, \"h7a_count\": 90, \"h7b_count\": 0, \"h1_count\": 0, \"h1_rate\": 0, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0}}, \"plan016-extended-1000-s42\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.96, \"n_proved\": 96, \"n_problems\": 100, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 96, \"h1_rate\": 1, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"genuine_h1_near\": 0, \"genuine_strict\": 0, \"content_independent_rate\": 1, \"single_premise_rate\": 0, \"taxonomy_audit\": \"2026-05-15\", \"taxonomy_tool\": \"classify_h7.py current version (with H8 detection)\", \"taxonomy_note\": \"Re-run with current classify_h7.py. Old value genuine=7 was incorrect (old version lacked H8 and had weaker H1 detection). All 96 proved are H1 (conclusion embedded in premises). 0 H7, 0 H8.\"}, \"conclusion\": \"success\"}, \"plan001-exec-only-s44-1000-r2\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 1, \"n_proved\": 100, \"n_problems\": 100, \"mean_isr\": 0.002, \"isr_std\": 0.0146, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 85, \"h1_rate\": 0.85, \"h8_count\": 15, \"h8_rate\": 0.15, \"genuine_count\": 0, \"genuine_rate\": 0, \"genuine_note\": \"D091: 3 samples escape text-match classifiers but are functionally degenerate (ISR=0, disjunctive/commuted bypasses)\"}, \"conclusion\": \"success\"}, \"plan018-additive-random-b01-s42-1000-r3\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.97, \"eval_mean_isr\": 0.6892, \"eval_isr_std\": 0.2037, \"eval_median_isr\": 0.75, \"eval_proved_only_isr\": 0.7105, \"eval_n_proved\": 97, \"eval_n_problems\": 100, \"genuine_count\": 0, \"genuine_rate\": 0, \"h1_count\": 0, \"h1_rate\": 0, \"h7_count\": 97, \"h7_rate\": 1, \"tautological_collapse\": true, \"train_final_prove_rate\": 0.827, \"train_final_mean_isr\": 0.5213, \"train_loss\": 0.00671, \"train_final_entropy\": 0.003, \"train_runtime_seconds\": 5783, \"train_steps\": 1000, \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 25, \"prove_rate\": 1, \"mean_isr\": 0.7533}, \"unknown\": {\"count\": 41, \"proved\": 39, \"prove_rate\": 0.951, \"mean_isr\": 0.6565}, \"true\": {\"count\": 34, \"proved\": 33, \"prove_rate\": 0.971, \"mean_isr\": 0.6814}}, \"n_premise_distribution\": {\"1\": 97}, \"pattern_description\": \"All 97 proved: 1 premise identical to conclusion (P therefore P). D088 correction: h7=97 h1=0 (was h1=97 h7=0 pre-D086 bugfix).\"}, \"conclusion\": \"negative\"}, \"plan009-sft-baseline-s44-1000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.15, \"n_proved\": 15, \"n_problems\": 100, \"mean_isr\": 0.0884, \"isr_std\": 0.2268, \"median_isr\": 0, \"proved_only_mean_isr\": 0.5892, \"max_isr\": 0.8571, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.4412}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0}}, \"genuine_count\": 14, \"genuine_rate\": 0.9333, \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0667, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0667, \"content_independent_count\": 0, \"content_independent_rate\": 0, \"isr_1_count\": 0, \"isr_1_rate\": 0, \"train_final_loss\": 0.0171, \"train_avg_loss\": 0.1544, \"train_token_accuracy\": 0.995, \"train_runtime_s\": 1580.97, \"eval_elapsed_s\": 391.8}}, \"plan009-sft-baseline-s43-1000\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.11, \"n_proved\": 11, \"n_problems\": 100, \"mean_isr\": 0.0699, \"isr_std\": 0.2155, \"median_isr\": 0, \"proved_only_mean_isr\": 0.6352, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 11, \"prove_rate\": 0.3235}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0}}, \"genuine_count\": 10, \"genuine_rate\": 0.9091, \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0909, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0909, \"content_independent_count\": 0, \"content_independent_rate\": 0, \"isr_1_count\": 1, \"isr_1_rate\": 0.0909, \"train_final_loss\": 0.0167, \"train_avg_loss\": 0.1551, \"train_token_accuracy\": 0.9954, \"train_runtime_s\": 1584.79, \"eval_elapsed_s\": 326.1}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s42-1000\": {\"status\": \"DONE\", \"metrics\": {\"train_final_loss\": 0.0168, \"train_last_step_loss\": 0.0168, \"train_token_accuracy\": 0.9955, \"train_epochs\": 15.88, \"train_runtime_sec\": 1415, \"train_steps\": 1000, \"eval_prove_rate\": 0.13, \"eval_n_proved\": 13, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0738, \"eval_isr_std\": 0.2077, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5677, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"eval_output_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json\", \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0769, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 12, \"genuine_rate\": 0.9231, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0769, \"isr_1_count\": 0, \"content_independent_count\": 0, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 12, \"prove_rate\": 0.353, \"mean_isr\": 0.209}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.011}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}}}, \"conclusion\": \"success\"}, \"exp1-random-b03-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.79, \"mean_isr\": 0.1745, \"isr_std\": 0.1628, \"median_isr\": 0.1667, \"proved_only_mean_isr\": 0.2209, \"hacking_rate_strict_h7\": 0, \"hacking_rate_functional\": 0.1013, \"genuine_rate\": 0.8987, \"genuine_count\": 71, \"n_proved\": 79, \"n_problems\": 100, \"h1_conclusion_in_premise\": 0.759, \"eval_data\": \"test_100.jsonl\", \"eval_output\": \"/root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43.json\"}}, \"exp1-random-b03-s43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_step\": 500, \"prove_rate\": 0.5505, \"mean_isr\": 0.1358, \"parse_rate\": 1, \"train_loss\": 0.01365, \"train_runtime_sec\": 6161.1, \"epoch\": 2, \"eval_prove_rate\": 0.92, \"eval_mean_isr\": 0.1659, \"eval_isr_std\": 0.1147, \"eval_median_isr\": 0.1429, \"eval_proved_only_mean_isr\": 0.1803, \"eval_min_isr\": 0, \"eval_max_isr\": 0.5, \"eval_n_proved\": 92, \"eval_n_problems\": 100, \"eval_h7_strict_rate\": 0.076, \"eval_h7_strict_count\": 7, \"eval_h1_strict_rate\": 0.891, \"eval_h1_strict_count\": 82, \"eval_genuine_rate\": 0.0326, \"eval_genuine_count\": 3, \"eval_isr0_count\": 6, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 23, \"prove_rate\": 0.92, \"mean_isr\": 0.156}, \"unknown\": {\"count\": 41, \"proved\": 37, \"prove_rate\": 0.902, \"mean_isr\": 0.184}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.151}}, \"D086_correction\": \"H1 90→82, genuine 2→3 per D086 clean batch run\"}}, \"plan002-additive-b01-s42-1000\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.9, \"eval_mean_isr\": 0.7892, \"eval_isr_std\": 0.3424, \"eval_proved_only_isr\": 0.8769, \"eval_median_isr\": 1, \"eval_n_proved\": 90, \"eval_n_problems\": 100, \"eval_component_count_mean\": 2.889, \"tautological_collapse\": true, \"train_final_prove_rate\": 0.855, \"train_final_mean_isr\": 0.532, \"h7_count\": 87, \"h7_rate\": 0.9667, \"h1_count\": 0, \"h1_rate\": 0, \"h1_near_count\": 1, \"h1_near_rate\": 0.0111, \"h8_conjunction_collapse_count\": 1, \"h8_conjunction_collapse_rate\": 0.0111, \"genuine_count\": 2, \"genuine_rate\": 0.0222, \"taxonomy_standard\": \"D086 clean run = ground truth. D084 residual removed.\"}}, \"plan002-additive-b01-s44\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.89, \"eval_mean_isr\": 0.803, \"eval_isr_std\": null, \"eval_proved_only_isr\": 0.902, \"eval_n_proved\": 89, \"eval_n_problems\": 100, \"h7_count\": 89, \"h7_rate\": 1, \"h1_count\": 0, \"h1_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"component_mean\": 4.33, \"comp_2_ratio\": 0.022, \"h7_fn_correction\": \"12 former genuine reclassified as H7: all n_prem=1 false negatives (normalization mismatch prevented conclusion matching)\"}, \"conclusion\": \"negative\"}, \"plan013-random-reward-s42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 1, \"eval_mean_isr\": 0.535, \"eval_isr_std\": 0.1282, \"eval_proved_only_isr\": 0.535, \"eval_median_isr\": 0.5, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"}}, \"plan001-exec-only-s43-r4\": {\"status\": \"DONE\", \"metrics\": {\"eval_sampling_prove_rate\": 0.14, \"eval_sampling_mean_isr\": 0, \"eval_sampling_n_proved\": 14, \"eval_sampling_temperature\": 0.7, \"eval_sampling_method\": \"do_sample=True, temperature=0.7\", \"eval_sampling_by_answer\": {\"true\": {\"count\": 34, \"proved\": 6, \"prove_rate\": 0.176}, \"false\": {\"count\": 25, \"proved\": 2, \"prove_rate\": 0.08}, \"unknown\": {\"count\": 41, \"proved\": 6, \"prove_rate\": 0.146}}, \"eval_greedy_prove_rate\": 0.13, \"eval_greedy_mean_isr\": 0, \"eval_greedy_proved_only_isr\": 0, \"eval_greedy_n_proved\": 13, \"eval_greedy_method\": \"eval_sta.py default (do_sample=False)\", \"eval_greedy_by_answer\": {\"true\": {\"count\": 34, \"proved\": 4, \"prove_rate\": 0.118}, \"false\": {\"count\": 25, \"proved\": 5, \"prove_rate\": 0.2}, \"unknown\": {\"count\": 41, \"proved\": 4, \"prove_rate\": 0.0976}}, \"eval_greedy_h7_count\": 0, \"eval_greedy_h7_rate\": 0, \"eval_greedy_h1_count\": 13, \"eval_greedy_h1_rate\": 1, \"eval_greedy_genuine_rate\": 0, \"eval_greedy_n_premises_proved_mean\": 17.92, \"eval_greedy_mean_components_proved\": 18.92, \"eval_greedy_n_premises_all_mean\": 32.67, \"eval_sampling_h1_rate\": 1, \"eval_sampling_h7_rate\": 0, \"eval_sampling_genuine_rate\": 0, \"eval_sampling_mean_components_proved\": 18.5, \"eval_greedy_vs_sampling_delta_pr\": -0.01, \"eval_method_note\": \"Greedy and sampling agree on failure profile (ISR*=0, H1=100%, components~18.5-18.9). s43 collapse is decoding-invariant.\"}, \"conclusion\": \"negative\"}, \"plan001-exec-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan017-additive-random-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"tautological_collapse\": false, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 1, \"h1_count\": 48, \"genuine_rate\": 0, \"genuine_count\": 0}}, \"plan002-additive-b01-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.81, \"eval_mean_isr\": 0.3365, \"eval_isr_std\": 0.3227, \"eval_proved_only_isr\": 0.4154, \"eval_median_isr\": 0.2, \"eval_n_proved\": 81, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 5.58, \"h7_rate\": 0.16, \"h7_count\": 13, \"h1_rate\": 0.519, \"h1_count\": 42, \"h8_conjunction_collapse_count\": 12, \"h8_conjunction_collapse_rate\": 0.148, \"genuine_rate\": 0.173, \"genuine_count\": 14, \"tautological_collapse\": false, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse audit completed. 12/81 proved samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json\"}}, \"plan002-additive-b01-s43\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.61, \"eval_n_proved\": 61, \"eval_n_problems\": 100, \"eval_proved_only_isr\": 0.83, \"h7_count\": 59, \"h7_rate\": 0.9672, \"h1_count\": 0, \"h1_rate\": 0, \"h1_near_count\": 0, \"h1_near_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 2, \"genuine_rate\": 0.0328, \"proved_single_premise_ratio\": 1, \"taxonomy_note\": \"structurally determined: proved_single_premise_ratio=1.0, all taxonomy categories except H7 are zero by construction. eval file lost but classification derivable from structure.\"}, \"conclusion\": \"negative\"}, \"exp1-isr-b03-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.91, \"mean_isr\": 0.2575, \"isr_std\": 0.2363, \"median_isr\": 0.3333, \"proved_only_mean_isr\": 0.283, \"hacking_rate_strict_h7\": 0.022, \"hacking_rate_functional\": 0.3297, \"genuine_rate\": 0.6703, \"genuine_count\": 61, \"n_proved\": 91, \"n_problems\": 100, \"h1_conclusion_in_premise\": 0.747, \"eval_data\": \"test_100.jsonl\", \"eval_output\": \"/root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s43.json\"}}, \"plan009-sft-baseline-s44-1000-r3\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.15, \"eval_n_proved\": 15, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0884, \"eval_isr_std\": 0.2268, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5892, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 1, \"h1_rate\": 0.0667, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 14, \"genuine_rate\": 0.9333, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.441, \"mean_isr\": 0.26}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}}}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s44\": {\"status\": \"DONE\", \"metrics\": {\"train_final_loss\": 0.2397, \"train_last_step_loss\": 0.0328, \"train_token_accuracy\": 0.9928, \"train_epochs\": 7.94, \"train_runtime_sec\": 729.05, \"train_steps\": 500, \"eval_prove_rate\": 0.17, \"eval_n_proved\": 17, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0974, \"eval_isr_std\": 0.2409, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5729, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"eval_output_path\": \"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s44.json\", \"eval_tautological_collapse\": false, \"eval_h7_count\": 0, \"eval_h7_rate\": 0, \"eval_h1_count\": 2, \"eval_h1_rate\": 0.118, \"eval_genuine_count\": 15, \"eval_genuine_rate\": 0.882, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.441, \"mean_isr\": 0.257}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.027}, \"unknown\": {\"count\": 41, \"proved\": 1, \"prove_rate\": 0.024, \"mean_isr\": 0.008}}, \"eval_correction_note\": \"Corrected 2026-05-15: previous eval used test_100.jsonl (50/44/6 distribution), re-evaled with proofwriter_fol_100.jsonl (34/25/41)\"}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s43\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.2391, \"train_token_accuracy\": 0.9938, \"train_epochs\": 7.94, \"train_runtime_sec\": 677.14, \"train_steps\": 500, \"eval_prove_rate\": 0.15, \"eval_mean_isr\": 0.0895, \"eval_isr_std\": 0.2338, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5967, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 1, \"h1_rate\": 0.067, \"genuine_count\": 14, \"genuine_rate\": 0.933, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"prove_rate\": 0.382, \"mean_isr\": 0.234}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.027}, \"unknown\": {\"count\": 41, \"proved\": 1, \"prove_rate\": 0.024, \"mean_isr\": 0.008}}, \"eval_data_path\": \"data/proofwriter_fol_100.jsonl\", \"eval_output_path\": \"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s43.json\"}, \"conclusion\": \"success\"}, \"plan001-exec-only-s44-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan009-sft-baseline-s44-1000-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan002-additive-b03-s42\": {\"status\": \"DONE\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"last100_prove_rate\": 0.5525, \"eval_prove_rate\": 0.18, \"eval_mean_isr\": 0.0257, \"eval_isr_std\": 0.0742, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.1427, \"eval_n_proved\": 18, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.778, \"h1_count\": 14, \"h8_conjunction_collapse_count\": 3, \"h8_conjunction_collapse_rate\": 0.1667, \"genuine_rate\": 0.0556, \"genuine_count\": 1, \"eval_by_type_false_pr\": 0.12, \"eval_by_type_false_isr\": 0.0102, \"eval_by_type_unknown_pr\": 0.195, \"eval_by_type_unknown_isr\": 0.0422, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.0172, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine 4→1.\"}, \"conclusion\": \"negative\"}, \"plan001-exec-only-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.93, \"eval_mean_isr\": 0.1232, \"eval_isr_std\": 0.1887, \"eval_proved_only_isr\": 0.1324, \"eval_median_isr\": 0, \"eval_n_proved\": 93, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.871, \"h1_count\": 81, \"h8_conjunction_collapse_count\": 6, \"h8_conjunction_collapse_rate\": 0.0645, \"genuine_rate\": 0.0753, \"genuine_count\": 7, \"genuine_mean_isr\": 0.3141, \"h1_mean_isr\": 0.1055, \"conclusion_embedding_total\": 0.871, \"content_independent_predicates_count\": 1, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine 12→7.\"}}, \"plan004-o1-ablation-s42\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.63, \"mean_isr\": 0.0072, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 63, \"h1_rate\": 1, \"h8_conjunction_collapse_count\": 2, \"h8_conjunction_collapse_rate\": 0.0317, \"genuine_count\": 0, \"genuine_rate\": 0, \"content_independent_predicates_count\": 3, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine unchanged (0).\"}, \"conclusion\": \"negative\"}, \"exp1-isr-b03-s42-1000-r2\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.95, \"eval_mean_isr\": 0.734, \"eval_isr_std\": 0.2575, \"eval_median_isr\": 0.6, \"eval_proved_only_isr\": 0.7726, \"eval_n_proved\": 95, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 25, \"prove_rate\": 1, \"mean_isr\": 0.824}, \"unknown\": {\"count\": 41, \"proved\": 38, \"prove_rate\": 0.927, \"mean_isr\": 0.673}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.741}}, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 54, \"h1_rate\": 0.568, \"genuine_count\": 0, \"genuine_rate\": 0, \"tautological_collapse\": true, \"isr_1_count\": 41, \"isr_1_rate\": 0.432, \"single_premise_count\": 0, \"train_final_prove_rate\": 0.829, \"train_final_mean_isr\": 0.727, \"train_loss\": 0.0041, \"train_runtime_seconds\": 6280, \"train_final_entropy\": 9e-06, \"completions_mean_length\": 47, \"h8_conjunction_collapse_count\": 41, \"h8_conjunction_collapse_rate\": 0.432, \"content_independent_predicates\": true}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s42-1000-r2\": {\"status\": \"DONE\", \"metrics\": {\"train_final_prove_rate\": 0.989, \"train_final_mean_isr\": 0.353, \"train_final_reward\": 1.062, \"train_steps\": 1000, \"train_runtime_seconds\": 2957, \"eval_prove_rate\": 1, \"eval_mean_isr\": 0.3333, \"eval_isr_std\": 0, \"eval_median_isr\": 0.3333, \"eval_proved_only_isr\": 0.3333, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_component_count_mean\": 3, \"genuine_rate\": 0, \"genuine_count\": 0, \"tautological_collapse\": true, \"h7_rate\": null, \"h7_count\": null, \"h1_rate\": null, \"h1_count\": null}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s42-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp1-isr-b03-s42-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s44\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.98, \"eval_mean_isr\": 0.57, \"eval_isr_std\": 0.2013, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.5816, \"eval_n_proved\": 98, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 2.04, \"eval_component_count_2\": 94, \"eval_component_count_3\": 4, \"tautological_collapse\": true, \"h7_rate\": 1, \"h7_count\": 97, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"conclusion_embedding_total\": 1}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s43-r2\": {\"status\": \"DONE\", \"metrics\": {\"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 93.2, \"h1_count\": 82, \"genuine_rate\": 6.8, \"genuine_count\": 6, \"eval_prove_rate\": 0.88, \"eval_mean_isr\": 0.058}, \"conclusion\": \"negative\"}, \"exp1-random-b03-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.23, \"eval_proved_only_mean_isr\": 0, \"eval_mean_isr\": 0, \"eval_isr_std\": 0, \"eval_median_isr\": 0, \"eval_n_proved\": 23, \"eval_n_problems\": 100, \"eval_h7_strict_rate\": 0, \"eval_h7_strict_count\": 0, \"eval_h1_strict_rate\": 1, \"eval_h1_strict_count\": 23, \"eval_genuine_rate\": 0, \"eval_genuine_count\": 0, \"eval_data\": \"proofwriter_fol_100.jsonl\"}}, \"exp1-isr-b03-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_step\": 500, \"prove_rate\": 0.56125, \"mean_isr\": 0.1515, \"parse_rate\": 1, \"train_loss\": 0.0176, \"train_runtime_sec\": 4153.6, \"epoch\": 2, \"eval_prove_rate\": 0.86, \"eval_mean_isr\": 0.2535, \"eval_isr_std\": 0.2406, \"eval_median_isr\": 0.3333, \"eval_proved_only_mean_isr\": 0.2948, \"eval_min_isr\": 0, \"eval_max_isr\": 0.75, \"eval_n_proved\": 86, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_h7_strict_rate\": 0.047, \"eval_h7_strict_count\": 4, \"eval_h1_strict_rate\": 0.686, \"eval_h1_strict_count\": 59, \"eval_conclusion_in_premise_rate\": 0.733, \"eval_conclusion_in_premise_count\": 63, \"eval_genuine_rate\": 0.267, \"eval_genuine_count\": 23, \"eval_single_premise_rate\": 0.058, \"eval_single_premise_count\": 5, \"eval_isr_1_count\": 0, \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 23, \"prove_rate\": 0.92, \"mean_isr\": 0.334}, \"unknown\": {\"count\": 41, \"proved\": 35, \"prove_rate\": 0.854, \"mean_isr\": 0.199}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.26}}}}, \"exp1-random-b03-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan015-linear-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp1-isr-b03-s43-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp1-random-b03-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp1-isr-b03-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.95, \"mean_isr\": 0.705, \"isr_std\": 0.172, \"proved_only_isr\": 0.7421, \"n_proved\": 95, \"n_problems\": 100, \"h7_rate\": 1, \"h7_count\": 95, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"single_premise_rate\": 1, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"Re-eval with correct test set (D062). Previous test_100.jsonl results invalidated.\"}}, \"exp1-random-b03-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp1-isr-b03-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp1-isr-b03-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp2-exec-s43-greedy\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp4-100step-h1h7\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan006-prolog-sta-s44\": {\"status\": \"DONE\", \"metrics\": {\"pass_rate\": 0.97, \"isr_mean\": 0.885, \"isr_n_cl_ge3\": \"N/A (0 samples)\", \"n_clauses_dist\": \"78/100 single-clause, 22/100 two-clause\", \"h7_functional_rate\": 0.979, \"genuine_rate\": 0, \"premise_count_analysis\": \"100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs\", \"failure_mode\": \"query-as-fact gaming (total H7 collapse)\"}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s43\": {\"status\": \"DONE\", \"metrics\": {\"train\": {\"final_prove_rate\": 0.769, \"final_mean_isr\": 0.129, \"final_loss\": 0.0155, \"final_entropy\": 0.09, \"final_reward\": 0.573, \"completion_length_mean\": 143, \"train_runtime_seconds\": 5095, \"train_runtime_minutes\": 84.9}, \"eval\": {\"n_problems\": 100, \"n_proved\": 38, \"prove_rate\": 0.38, \"mean_isr\": 0.0704, \"isr_std\": 0.1263, \"median_isr\": 0, \"proved_only_mean_isr\": 0.1853, \"min_isr\": 0, \"max_isr\": 1, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 11, \"prove_rate\": 0.44, \"mean_isr\": 0.1003}, \"unknown\": {\"count\": 41, \"proved\": 11, \"prove_rate\": 0.268, \"mean_isr\": 0.0394}, \"true\": {\"count\": 34, \"proved\": 16, \"prove_rate\": 0.471, \"mean_isr\": 0.0859}}}, \"h7_classification\": {\"h7_strict\": 0, \"h7_rate\": 0, \"h1_strict\": 37, \"h1_rate\": 0.974, \"conclusion_in_premise_total\": 37, \"conclusion_in_premise_rate\": 0.974, \"genuine_count\": 0, \"genuine_rate\": 0, \"isr_1_count\": 1, \"note\": \"1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause; all 38/38 proved samples are tautological\"}}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"cumulative_prove_rate\": 0.848, \"cumulative_mean_isr\": 0.787, \"final_prove_rate\": 1, \"final_isr\": 1, \"final_reward\": 1, \"saturation_onset_step\": 100, \"train_loss\": 0.00716, \"training_hours\": 0.78, \"final_entropy\": 0.01, \"final_completion_length\": 27, \"initial_completion_length\": 120, \"steps_at_perfect_reward\": 400, \"train_runtime_sec\": 2791, \"eval_prove_rate\": 0.5, \"eval_mean_isr\": 0.5, \"eval_proved_only_isr\": 1, \"eval_h7_rate\": 1, \"eval_h7_count\": 50, \"eval_proved_count\": 50, \"eval_total_count\": 100, \"eval_n_clauses_mean\": 1, \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"}}, \"plan006-prolog-exec-s44\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.21, \"eval_mean_isr\": 0.0812, \"eval_isr_std\": 0.2343, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.3866, \"eval_min_isr\": 0, \"eval_max_isr\": 1, \"eval_n_proved\": 21, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 683.9, \"eval_by_type_false_pr\": 0.04, \"eval_by_type_false_isr\": 0.04, \"eval_by_type_unknown_pr\": 0.317, \"eval_by_type_unknown_isr\": 0.099, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.09, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\"}, \"plan009-sft-baseline-s42-r4\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.14, \"eval_mean_isr\": 0.08, \"eval_isr_std\": 0.214, \"eval_median_isr\": 0, \"eval_max_isr\": 0.833, \"eval_proved_only_isr\": 0.571, \"eval_n_proved\": 14, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"train_final_loss\": 0.0287, \"train_token_accuracy\": 0.9935, \"train_epochs\": 7.94, \"train_runtime_sec\": 789.6, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"pr\": 0.382, \"isr\": 0.226}, \"unknown\": {\"count\": 41, \"proved\": 1, \"pr\": 0.024, \"isr\": 0.008}, \"false\": {\"count\": 25, \"proved\": 0, \"pr\": 0, \"isr\": 0}}, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.071, \"h1_count\": 1, \"genuine_rate\": 0.929, \"genuine_count\": 13, \"hacking_patterns\": \"near-zero (1/14 H1, 0 H7, 92.9% genuine)\", \"tautological_collapse\": false}, \"conclusion\": \"success\"}, \"plan006-prolog-exec-s43-r3\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.56, \"eval_mean_isr\": 0.0084, \"eval_isr_std\": 0.0221, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.015, \"eval_min_isr\": 0, \"eval_max_isr\": 0.1, \"eval_n_proved\": 56, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 868.2, \"eval_by_type_false_pr\": 0.48, \"eval_by_type_false_isr\": 0.0043, \"eval_by_type_unknown_pr\": 0.6585, \"eval_by_type_unknown_isr\": 0.0114, \"eval_by_type_true_pr\": 0.5, \"eval_by_type_true_isr\": 0.0078, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s44\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.89, \"mean_isr\": 0.0619, \"isr_std\": 0.1756, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0695, \"n_proved\": 89, \"n_problems\": 100, \"max_isr\": 1, \"min_isr\": 0, \"isr_pr_ratio\": 0.0695, \"isr_zero_count\": 72, \"isr_one_count\": 2, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 21, \"prove_rate\": 0.84, \"mean_isr\": 0.0533}, \"unknown\": {\"count\": 41, \"proved\": 40, \"prove_rate\": 0.976, \"mean_isr\": 0.0892}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.0353}}, \"elapsed_seconds\": 1012.7, \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan006-prolog-exec-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan006-prolog-exec-s42\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.83, \"eval_mean_isr\": 0.031, \"eval_proved_only_isr\": 0.037, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2, \"eval_isr_std\": 0.0534, \"h7_rate\": 0, \"h1_rate\": 0, \"isr_1_rate\": 0, \"single_premise_rate\": 0, \"by_answer_type\": {\"true\": {\"proved\": 37, \"count\": 40, \"pr\": 0.925, \"isr\": 0.037}, \"false\": {\"proved\": 21, \"count\": 29, \"pr\": 0.724, \"isr\": 0.038}, \"unknown\": {\"proved\": 25, \"count\": 31, \"pr\": 0.806, \"isr\": 0.016}}}, \"conclusion\": \"negative\"}, \"plan006-prolog-exec-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan009-sft-baseline-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan009-sft-baseline-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan018-additive-random-b01-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan012-hacking-taxonomy\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"isr_b01_genuine_rate\": 0.259, \"random_b01_genuine_rate\": 0.177, \"genuine_rate_delta_pp\": 8.2, \"isr_b01_conclusion_embedding_rate\": 0.728, \"random_b01_conclusion_embedding_rate\": 0.785, \"isr_b01_genuine_mean_isr\": 0.6723, \"random_b01_genuine_mean_isr\": 0.3427, \"isr_b01_complexity_wo_utility_rate\": 0, \"random_b01_complexity_wo_utility_rate\": 0.038, \"isr_b01_hacking_rate\": 0.741, \"random_b01_hacking_rate\": 0.823}}, \"plan005-sta-low-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 71, \"parse_rate\": 1, \"overall_prove_rate\": 0.5657, \"overall_isr\": 0.1682, \"last50_prove_rate\": 0.77, \"last50_isr\": 0.2559, \"last100_prove_rate\": 0.7725, \"last100_isr\": 0.2299, \"last100_loss\": 0.022752, \"overall_loss\": 0.017296, \"last100_isr_pr_ratio\": 0.298, \"last100_isr_lt_pr_count\": \"99/100\", \"first_rolling10_pr_ge_0.8\": 178, \"first_rolling10_pr_ge_0.9\": 439, \"max_rolling10_pr\": 0.9375, \"max_rolling10_isr\": 0.3282, \"windowed\": {\"1-50\": {\"pr\": 0.1775, \"isr\": 0.0906}, \"51-100\": {\"pr\": 0.1775, \"isr\": 0.0835}, \"101-200\": {\"pr\": 0.5062, \"isr\": 0.1463}, \"201-300\": {\"pr\": 0.6713, \"isr\": 0.1791}, \"301-400\": {\"pr\": 0.7013, \"isr\": 0.1984}, \"401-500\": {\"pr\": 0.7725, \"isr\": 0.2299}}}}, \"plan014-downstream-nli-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_accuracy\": 0.341, \"proved_rate\": 0.915, \"proved_count\": 732, \"total_generations\": 800, \"parse_errors\": 0, \"accuracy_by_label\": {\"true\": 0.912, \"false\": 0, \"unknown\": 0.076}, \"spearman_rho\": -0.049, \"spearman_p\": 0.187, \"mann_whitney_U\": 17202, \"mann_whitney_p\": 0.288, \"bon_isr_accuracy\": 0.35, \"bon_random_accuracy\": 0.341, \"bon_oracle_accuracy\": 0.44, \"bon_prove_first_accuracy\": 0.35, \"isr_bucket_high_acc\": 0.75, \"isr_bucket_mid_acc\": 0.377, \"isr_bucket_low_acc\": 0.327, \"runtime_inference_s\": 408.8, \"runtime_eval_s\": 13.6}}, \"plan001-exec-only-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan003-eval-exec-only-r5\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.32, \"mean_isr\": 0.2055, \"isr_std\": 0.3194, \"proved_only_isr\": 0.6423, \"isr_by_type\": {\"true\": 0.3598, \"false\": 0.1723, \"unknown\": 0.0979}, \"total_samples\": 100, \"proved_count\": 32, \"runtime_s\": 251.7}, \"conclusion\": \"success\"}, \"plan001-exec-only-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r5\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1, \"mean_isr\": 0.04347, \"last20_prove_rate\": 0.15, \"last20_isr_mean\": 0.04956, \"first20_prove_rate\": 0.08125, \"first20_isr_mean\": 0.05182, \"overall_reward_mean\": 0.07174, \"last20_reward_mean\": 0.09978, \"training_steps\": 100, \"training_minutes\": 16.9, \"step_time_s\": 10.13, \"isr_pr_ratio_overall\": 0.43, \"isr_pr_ratio_last20\": 0.33, \"K\": 8}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r5\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_prove_rate\": 0.11875, \"first20_isr_mean\": 0.11875, \"overall_reward_mean\": 0.15125, \"last20_reward_mean\": 0.2, \"training_steps\": 100, \"training_minutes\": 15.7, \"step_time_s\": 9.44, \"isr_pr_ratio_last20\": 1, \"K\": 8}, \"conclusion\": \"success\"}, \"sta-phase1-exec-sta-r4\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1575, \"mean_isr\": 0.1525, \"last20_prove_rate\": 0.2125, \"last20_isr_mean\": 0.2125, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r4\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-only\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-gt-isr-baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gt_prove_rate\": 0.18, \"gt_mean_isr\": 0.5588, \"gt_isr_std\": 0.2582, \"gt_isr_median\": 0.6125, \"solver_execution_rate\": 1, \"true_prove_rate\": 0.5, \"true_mean_isr\": 0.5833}}, \"sta-phase0-baseline\": {\"status\": \"DONE\", \"metrics\": {\"mean_isr\": 0.0641, \"isr_std\": 0.1983, \"median_isr\": 0, \"isr_range\": [0, 0.889], \"prove_rate\": 0.12, \"proved_count\": 12, \"total_samples\": 100, \"xor_affected_samples\": 34, \"effective_prove_rate_no_xor\": 0.182, \"avg_time_per_sample_s\": 3.4, \"total_runtime_s\": 336, \"isr_by_answer\": {\"true\": {\"n\": 34, \"proved\": 9, \"prove_rate\": 0.265, \"mean_isr\": 0.1345}, \"false\": {\"n\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.024}, \"unknown\": {\"n\": 41, \"proved\": 2, \"prove_rate\": 0.049, \"mean_isr\": 0.0302}}}, \"conclusion\": \"success\"}}, \"count\": 86, \"total\": 86, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3376}}"
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
Good. I found the three experiments in the registry:

1. **plan017-additive-random-s42**: metrics show h7_count=0, h1_count=48, genuine_count=0. Status: DONE, conclusion: negative
2. **exp1-random-b03-s43-r4**: metrics show eval_h7_strict_count=7, eval_h1_strict_count=82, eval_genuine_count=3. Status: DONE, conclusion: success


3. **exp1-random-b03-s44-r2**: metrics show eval_h7_strict_count=0, eval_h1_strict_count=23, eval_genuine_count=0. Status: DONE, conclusion: success

Now I'm locating the eval output directories. I can see the first experiment has a JSON file while the other two have corresponding directories. Let me check what classify_h7.py expects as arguments.

I need to examine the script to understand what input format it requires and verify that the eval directories have the right structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "29b1c0a5-3f1f-4efa-9765-f8dd67e75b5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTtRxpsFU4TYL1vn4cDoX4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19618,
      "cache_read_input_tokens": 28569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19618
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

找到三个实验的 registry 数据和输出目录。现在检查 classify_h7.py 参数和 eval 数据位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "6c61d713-231c-4682-85fe-e7c3b2602067",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTtRxpsFU4TYL1vn4cDoX4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19618,
      "cache_read_input_tokens": 28569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19618
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VEe7c7Vx69DrLCUbKbZiAj`</summary>

```json
{
  "server": "westd-39279",
  "command": "head -80 /root/solver-trace-ablation/scripts/classify_h7.py",
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "87b8a7aa-0781-4d34-902a-c76f485d0059",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTtRxpsFU4TYL1vn4cDoX4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19618,
      "cache_read_input_tokens": 28569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19618
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

_source line 27 · 2026-05-15T18:21:33.112Z_

<details><summary>↩ Tool result · `toolu_01VEe7c7Vx69DrLCUbKbZiAj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nClassify hacking patterns in eval results.\\n\\nH7a: standard tautology — single premise text-matches conclusion\\n     (whitespace/case normalized)\\nH7b: obfuscated tautology — single premise, logically equivalent but\\n     textually different (vacuous quantifier wrapping, variable renaming)\\n     Detection: strip vacuous quantifiers + alpha-normalize, then fallback\\n     to quantifier-count + predicate-overlap heuristic\\nH1:  multi-premise, at least one premise == conclusion (conclusion embedding)\\nH8:  conclusion is top-level conjunction of premises (conjunction collapse)\\n\\nUsage:\\n    python scripts/classify_h7.py --eval_path /path/to/eval_results.json\\n    python scripts/classify_h7.py --batch f1.json f2.json ... --out /path/to/output.txt\\n    python scripts/classify_h7.py --batch f1.json f2.json ... --json_out /path/to/audit.json\\n\\\"\\\"\\\"\\nimport json\\nimport argparse\\nimport re\\nimport sys\\nimport os\\nimport hashlib\\n\\n\\ndef normalize_fol(s):\\n    s = s.strip()\\n    s = re.sub(r'\\\\s+', ' ', s)\\n    return s\\n\\n\\ndef strip_outer_parens(s):\\n    \\\"\\\"\\\"Strip matching outer parentheses if present.\\\"\\\"\\\"\\n    s = s.strip()\\n    if not (s.startswith('(') and s.endswith(')')):\\n        return s\\n    depth = 0\\n    for i, c in enumerate(s):\\n        if c == '(':\\n            depth += 1\\n        elif c == ')':\\n            depth -= 1\\n        if depth == 0 and i < len(s) - 1:\\n            return s\\n    return s[1:-1].strip()\\n\\n\\ndef strip_outer_parens_recursive(s):\\n    \\\"\\\"\\\"Recursively strip ALL layers of matching outer parentheses.\\n    D086-P1 fix: D084 re-audit used deeper paren normalization.\\n    Won't strip non-matching outer parens like (A) ∧ (B).\\n    \\\"\\\"\\\"\\n    s = s.strip()\\n    while s.startswith('(') and s.endswith(')'):\\n        depth = 0\\n        is_matching = True\\n        for i, c in enumerate(s):\\n            if c == '(':\\n                depth += 1\\n            elif c == ')':\\n                depth -= 1\\n            if depth == 0 and i < len(s) - 1:\\n                is_matching = False\\n                break\\n        if not is_matching:\\n            break\\n        s = s[1:-1].strip()\\n    return s\\n\\n\\ndef normalize_for_match(s):\\n    \\\"\\\"\\\"Normalize for matching: whitespace + recursive outer paren strip.\\n    D086-P1 fix: upgraded from single-layer to recursive paren strip.\\n    \\\"\\\"\\\"\\n    s = normalize_fol(s)\\n    s = strip_outer_parens_recursive(s)\\n    s = re.sub(r'\\\\s+', ' ', s)\\n    return s\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "9085213a-3e8e-4ffc-9ab6-86cb35bd7643",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nClassify hacking patterns in eval results.\\\\n\\\\nH7a: standard tautology — single premise text-matches conclusion\\\\n     (whitespace/case normalized)\\\\nH7b: obfuscated tautology — single premise, logically equivalent but\\\\n     textually different (vacuous quantifier wrapping, variable renaming)\\\\n     Detection: strip vacuous quantifiers + alpha-normalize, then fallback\\\\n     to quantifier-count + predicate-overlap heuristic\\\\nH1:  multi-premise, at least one premise == conclusion (conclusion embedding)\\\\nH8:  conclusion is top-level conjunction of premises (conjunction collapse)\\\\n\\\\nUsage:\\\\n    python scripts/classify_h7.py --eval_path /path/to/eval_results.json\\\\n    python scripts/classify_h7.py --batch f1.json f2.json ... --out /path/to/output.txt\\\\n    python scripts/classify_h7.py --batch f1.json f2.json ... --json_out /path/to/audit.json\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport json\\\\nimport argparse\\\\nimport re\\\\nimport sys\\\\nimport os\\\\nimport hashlib\\\\n\\\\n\\\\ndef normalize_fol(s):\\\\n    s = s.strip()\\\\n    s = re.sub(r'\\\\\\\\s+', ' ', s)\\\\n    return s\\\\n\\\\n\\\\ndef strip_outer_parens(s):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Strip matching outer parentheses if present.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    s = s.strip()\\\\n    if not (s.startswith('(') and s.endswith(')')):\\\\n        return s\\\\n    depth = 0\\\\n    for i, c in enumerate(s):\\\\n        if c == '(':\\\\n            depth += 1\\\\n        elif c == ')':\\\\n            depth -= 1\\\\n        if depth == 0 and i < len(s) - 1:\\\\n            return s\\\\n    return s[1:-1].strip()\\\\n\\\\n\\\\ndef strip_outer_parens_recursive(s):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Recursively strip ALL layers of matching outer parentheses.\\\\n    D086-P1 fix: D084 re-audit used deeper paren normalization.\\\\n    Won't strip non-matching outer parens like (A) ∧ (B).\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    s = s.strip()\\\\n    while s.startswith('(') and s.endswith(')'):\\\\n        depth = 0\\\\n        is_matching = True\\\\n        for i, c in enumerate(s):\\\\n            if c == '(':\\\\n                depth += 1\\\\n            elif c == ')':\\\\n                depth -= 1\\\\n            if depth == 0 and i < len(s) - 1:\\\\n                is_matching = False\\\\n                break\\\\n        if not is_matching:\\\\n            break\\\\n        s = s[1:-1].strip()\\\\n    return s\\\\n\\\\n\\\\ndef normalize_for_match(s):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Normalize for matching: whitespace + recursive outer paren strip.\\\\n    D086-P1 fix: upgraded from single-layer to recursive paren strip.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    s = normalize_fol(s)\\\\n    s = strip_outer_parens_recursive(s)\\\\n    s = re.sub(r'\\\\\\\\s+', ' ', s)\\\\n    return s\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nClassify hacking patterns in eval results.\\n\\nH7a: standard tautology — single premise text-matches conclusion\\n     (whitespace/case normalized)\\nH7b: obfuscated tautology — single premise, logically equivalent but\\n     textually different (vacuous quantifier wrapping, variable renaming)\\n     Detection: strip vacuous quantifiers + alpha-normalize, then fallback\\n     to quantifier-count + predicate-overlap heuristic\\nH1:  multi-premise, at least one premise == conclusion (conclusion embedding)\\nH8:  conclusion is top-level conjunction of premises (conjunction collapse)\\n\\nUsage:\\n    python scripts/classify_h7.py --eval_path /path/to/eval_results.json\\n    python scripts/classify_h7.py --batch f1.json f2.json ... --out /path/to/output.txt\\n    python scripts/classify_h7.py --batch f1.json f2.json ... --json_out /path/to/audit.json\\n\\\"\\\"\\\"\\nimport json\\nimport argparse\\nimport re\\nimport sys\\nimport os\\nimport hashlib\\n\\n\\ndef normalize_fol(s):\\n    s = s.strip()\\n    s = re.sub(r'\\\\s+', ' ', s)\\n    return s\\n\\n\\ndef strip_outer_parens(s):\\n    \\\"\\\"\\\"Strip matching outer parentheses if present.\\\"\\\"\\\"\\n    s = s.strip()\\n    if not (s.startswith('(') and s.endswith(')')):\\n        return s\\n    depth = 0\\n    for i, c in enumerate(s):\\n        if c == '(':\\n            depth += 1\\n        elif c == ')':\\n            depth -= 1\\n        if depth == 0 and i < len(s) - 1:\\n            return s\\n    return s[1:-1].strip()\\n\\n\\ndef strip_outer_parens_recursive(s):\\n    \\\"\\\"\\\"Recursively strip ALL layers of matching outer parentheses.\\n    D086-P1 fix: D084 re-audit used deeper paren normalization.\\n    Won't strip non-matching outer parens like (A) ∧ (B).\\n    \\\"\\\"\\\"\\n    s = s.strip()\\n    while s.startswith('(') and s.endswith(')'):\\n        depth = 0\\n        is_matching = True\\n        for i, c in enumerate(s):\\n            if c == '(':\\n                depth += 1\\n            elif c == ')':\\n                depth -= 1\\n            if depth == 0 and i < len(s) - 1:\\n                is_matching = False\\n                break\\n        if not is_matching:\\n            break\\n        s = s[1:-1].strip()\\n    return s\\n\\n\\ndef normalize_for_match(s):\\n    \\\"\\\"\\\"Normalize for matching: whitespace + recursive outer paren strip.\\n    D086-P1 fix: upgraded from single-layer to recursive paren strip.\\n    \\\"\\\"\\\"\\n    s = normalize_fol(s)\\n    s = strip_outer_parens_recursive(s)\\n    s = re.sub(r'\\\\s+', ' ', s)\\n    return s\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HBUoPTkMFg7vLvMj6xqGeJ`</summary>

```json
{
  "server": "westd-39279",
  "command": "ls /root/autodl-tmp/outputs/exp1_random_b03_s43_r4/",
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "aee23938-4bf4-47e7-9e8a-1c5f309e4a12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTtRxpsFU4TYL1vn4cDoX4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19618,
      "cache_read_input_tokens": 28569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19618
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

_source line 29 · 2026-05-15T18:21:34.062Z_

<details><summary>↩ Tool result · `toolu_01HBUoPTkMFg7vLvMj6xqGeJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadded_tokens.json\\nchat_template.jinja\\nconfig.json\\ngeneration_config.json\\nmerges.txt\\nmodel.safetensors.index.json\\nreward_log.jsonl\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntraining_args.bin\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "07089b45-2e28-43c2-ba12-465209f7dfdd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"README.md\\\\nadded_tokens.json\\\\nchat_template.jinja\\\\nconfig.json\\\\ngeneration_config.json\\\\nmerges.txt\\\\nmodel.safetensors.index.json\\\\nreward_log.jsonl\\\\nspecial_tokens_map.json\\\\ntokenizer.json\\\\ntokenizer_config.json\\\\ntraining_args.bin\\\\nvocab.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadded_tokens.json\\nchat_template.jinja\\nconfig.json\\ngeneration_config.json\\nmerges.txt\\nmodel.safetensors.index.json\\nreward_log.jsonl\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntraining_args.bin\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01A7Qoi4cvh87BgcZo47mD8u`</summary>

```json
{
  "server": "westd-39279",
  "command": "ls /root/autodl-tmp/outputs/exp1_random_b03_s44_r2/",
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "d82cf767-9deb-4135-9626-6a49116f7fa1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTtRxpsFU4TYL1vn4cDoX4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19618,
      "cache_read_input_tokens": 28569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19618
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

_source line 31 · 2026-05-15T18:21:34.685Z_

<details><summary>↩ Tool result · `toolu_01A7Qoi4cvh87BgcZo47mD8u`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadded_tokens.json\\nchat_template.jinja\\nconfig.json\\ngeneration_config.json\\nmerges.txt\\nmodel.safetensors.index.json\\nreward_log.jsonl\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntraining_args.bin\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "67a3611d-cd7a-417f-b8d5-2450203d9e75",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"README.md\\\\nadded_tokens.json\\\\nchat_template.jinja\\\\nconfig.json\\\\ngeneration_config.json\\\\nmerges.txt\\\\nmodel.safetensors.index.json\\\\nreward_log.jsonl\\\\nspecial_tokens_map.json\\\\ntokenizer.json\\\\ntokenizer_config.json\\\\ntraining_args.bin\\\\nvocab.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadded_tokens.json\\nchat_template.jinja\\nconfig.json\\ngeneration_config.json\\nmerges.txt\\nmodel.safetensors.index.json\\nreward_log.jsonl\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntraining_args.bin\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
The classify_h7.py script uses `--eval_path` not `--eval_dir`. It takes a JSON file path.

The directories `exp1_random_b03_s43_r4` and `exp1_random_b03_s44_r2` are checkpoint directories (model files), not eval output directories.

The eval results are JSON files:
- `eval_sta_plan017_additive_random_s42.json`


- `eval_sta_exp1_random_b03_s43_r4.json`
- `eval_sta_exp1_random_b03_s44_r2.json`

I should check the rest of classify_h7.py to understand all the arguments and verify those JSON files actually exist.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "39cb0290-2005-41c5-84b5-d2bd30897a49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KPoxzS8rgqosEVvxRbcC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2119,
      "cache_read_input_tokens": 48187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2119
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

_source line 33_

classify_h7.py 用 `--eval_path` 不是 `--eval_dir`。eval 结果是 JSON 文件。让我确认参数和 JSON 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "5da72378-ba49-4499-87c2-9098e6c09bd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KPoxzS8rgqosEVvxRbcC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2119,
      "cache_read_input_tokens": 48187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2119
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

_source line 34_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Pchkp6Yvz6KdoJmocUCZaS`</summary>

```json
{
  "server": "westd-39279",
  "command": "grep -n \"add_argument\\|argparse\" /root/solver-trace-ablation/scripts/classify_h7.py",
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "6b263fb4-aae0-40bb-8b3e-d7cc3643e0e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KPoxzS8rgqosEVvxRbcC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2119,
      "cache_read_input_tokens": 48187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2119
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

_source line 35 · 2026-05-15T18:21:41.108Z_

<details><summary>↩ Tool result · `toolu_01Pchkp6Yvz6KdoJmocUCZaS`</summary>

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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "eafb5e41-2866-4ec3-a756-249ef86d4729",
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

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CGv7eX3sfmvAcP6L9nPhdd`</summary>

```json
{
  "server": "westd-39279",
  "command": "ls -la /root/autodl-tmp/outputs/eval_sta_plan017_additive_random_s42.json /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43_r4.json /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s44_r2.json",
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "920ba045-47cb-41c8-8320-501621877e9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KPoxzS8rgqosEVvxRbcC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2119,
      "cache_read_input_tokens": 48187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2119
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

_source line 37 · 2026-05-15T18:21:42.386Z_

<details><summary>↩ Tool result · `toolu_01CGv7eX3sfmvAcP6L9nPhdd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 338462 May 15 12:42 /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43_r4.json\\n-rw-r--r-- 1 root root 431141 May 15 11:03 /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s44_r2.json\\n-rw-r--r-- 1 root root 290570 May 14 13:39 /root/autodl-tmp/outputs/eval_sta_plan017_additive_random_s42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "31e3de96-ccd6-43d6-b3af-b521c092006c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 338462 May 15 12:42 /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43_r4.json\\\\n-rw-r--r-- 1 root root 431141 May 15 11:03 /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s44_r2.json\\\\n-rw-r--r-- 1 root root 290570 May 14 13:39 /root/autodl-tmp/outputs/eval_sta_plan017_additive_random_s42.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 338462 May 15 12:42 /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43_r4.json\\n-rw-r--r-- 1 root root 431141 May 15 11:03 /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s44_r2.json\\n-rw-r--r-- 1 root root 290570 May 14 13:39 /root/autodl-tmp/outputs/eval_sta_plan017_additive_random_s42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
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
All three JSON files exist. Now let me check the argparse arguments of classify_h7.py more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "f14b7713-5777-4e41-868e-2de2d9e45b56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9h3e8xeky1aVivWw7XzEP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 935,
      "cache_read_input_tokens": 50306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 935
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

_source line 39_

三个 JSON 文件都在。查看 classify_h7.py 的完整参数定义。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "a0757df4-3e7b-4a9d-8a27-6d377da98545",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9h3e8xeky1aVivWw7XzEP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 935,
      "cache_read_input_tokens": 50306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 935
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QnSh9YQTEvVLuFsdRVL95b`</summary>

```json
{
  "server": "westd-39279",
  "command": "grep -n \"add_argument\" /root/solver-trace-ablation/scripts/classify_h7.py",
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "daeade30-4ec9-4bf3-9697-a9a14c3b11b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9h3e8xeky1aVivWw7XzEP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 935,
      "cache_read_input_tokens": 50306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 935
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

_source line 41 · 2026-05-15T18:21:46.774Z_

<details><summary>↩ Tool result · `toolu_01QnSh9YQTEvVLuFsdRVL95b`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"519:    parser.add_argument('--eval_path', help='Single eval file')\\n520:    parser.add_argument('--batch', nargs='+', help='Multiple eval files')\\n521:    parser.add_argument('--out', help='Output text file path')\\n522:    parser.add_argument('--json_out', help='Output JSON file path')\\n523:    parser.add_argument('--scan', action='store_true',\\n525:    parser.add_argument('--scan_dirs', nargs='+',\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "7df0009a-f1ba-49a0-97a2-4eb83d1ffffb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"519:    parser.add_argument('--eval_path', help='Single eval file')\\\\n520:    parser.add_argument('--batch', nargs='+', help='Multiple eval files')\\\\n521:    parser.add_argument('--out', help='Output text file path')\\\\n522:    parser.add_argument('--json_out', help='Output JSON file path')\\\\n523:    parser.add_argument('--scan', action='store_true',\\\\n525:    parser.add_argument('--scan_dirs', nargs='+',\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"519:    parser.add_argument('--eval_path', help='Single eval file')\\n520:    parser.add_argument('--batch', nargs='+', help='Multiple eval files')\\n521:    parser.add_argument('--out', help='Output text file path')\\n522:    parser.add_argument('--json_out', help='Output JSON file path')\\n523:    parser.add_argument('--scan', action='store_true',\\n525:    parser.add_argument('--scan_dirs', nargs='+',\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Now I know the interface. I'll use `--batch` with all three files and `--json_out` to get structured output. Let me run classify_h7.py with `--batch` for all three files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "789ec196-aa46-4c7f-94f9-c55c69016581",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNVFeipFAytEV3ieoW2U4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 51241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 400
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

_source line 43_

参数确认完毕。用 `--batch` 一次性运行三个文件，输出 JSON。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "84f9267c-75e8-4dc2-94dc-84b2893f41a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNVFeipFAytEV3ieoW2U4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 51241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 400
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

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_019MYdYBkFMT9Vdeay9Z6Bxk`</summary>

```json
{
  "server": "westd-39279",
  "command": "export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/classify_h7.py --batch /root/autodl-tmp/outputs/eval_sta_plan017_additive_random_s42.json /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43_r4.json /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s44_r2.json --json_out /root/autodl-tmp/outputs/h7_classification/random_b03_3seed_classify.json",
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
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "ff8d3626-7a2e-411a-b383-7dedb492ebaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNVFeipFAytEV3ieoW2U4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 51241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 400
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

_source line 45 · 2026-05-15T18:21:53.839Z_

<details><summary>↩ Tool result · `toolu_019MYdYBkFMT9Vdeay9Z6Bxk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n  plan017_additive_random_s42\\n============================================================\\nTotal samples: 100, Proved: 48\\nH7a (text-match tautology):                 4/48 = 8.3%\\nH7b (obfuscated tautology):                 0/48 = 0.0%\\nH7 total (H7a + H7b):                       4/48 = 8.3%\\nH1 strict  (multi-prem, concl in premises): 44/48 = 91.7%\\nH8 conj-collapse (concl = P1∧P2∧...):      0/48 = 0.0%\\nAny conclusion-in-premise (H7a+H1):         48/48 = 100.0%\\nContent-independent predicates:              6/48 = 12.5%\\nGenuine (proved - H7 - H1 - H8):           0/48 = 0.0%\\n---\\nH7 relaxed (single_premise + ISR>=0.5):     0/48 = 0.0%\\nSingle premise: 0/48 = 0.0%\\nISR = 1.0:      0/48 = 0.0%\\n\\n  H7a examples (first 3):\\n    folio_1051: 10 premises, isr=0.0\\n    folio_1381: 10 premises, isr=0.0\\n    folio_715: 5 premises, isr=0.0\\n\\n  H1 examples (first 3):\\n    folio_765: 7 premises, isr=0.1111111111111111\\n    folio_592: 7 premises, isr=0.1111111111111111\\n    folio_556: 5 premises, isr=0.2857142857142857\\n\\n============================================================\\n  exp1_random_b03_s43_r4\\n============================================================\\nTotal samples: 100, Proved: 92\\nH7a (text-match tautology):                 7/92 = 7.6%\\nH7b (obfuscated tautology):                 0/92 = 0.0%\\nH7 total (H7a + H7b):                       7/92 = 7.6%\\nH1 strict  (multi-prem, concl in premises): 82/92 = 89.1%\\nH8 conj-collapse (concl = P1∧P2∧...):      0/92 = 0.0%\\nAny conclusion-in-premise (H7a+H1):         89/92 = 96.7%\\nContent-independent predicates:              4/92 = 4.3%\\nGenuine (proved - H7 - H1 - H8):           3/92 = 3.3%\\n---\\nH7 relaxed (single_premise + ISR>=0.5):     0/92 = 0.0%\\nSingle premise: 0/92 = 0.0%\\nISR = 1.0:      0/92 = 0.0%\\n\\n  H7a examples (first 3):\\n    folio_233: 7 premises, isr=0.1111111111111111\\n    folio_711: 3 premises, isr=0.3333333333333333\\n    folio_394: 5 premises, isr=0.14285714285714285\\n\\n  H1 examples (first 3):\\n    folio_765: 7 premises, isr=0.2\\n    folio_1179: 7 premises, isr=0.3\\n    folio_1378: 9 premises, isr=0.25\\n\\n============================================================\\n  exp1_random_b03_s44_r2\\n============================================================\\nTotal samples: 100, Proved: 23\\nH7a (text-match tautology):                 0/23 = 0.0%\\nH7b (obfuscated tautology):                 0/23 = 0.0%\\nH7 total (H7a + H7b):                       0/23 = 0.0%\\nH1 strict  (multi-prem, concl in premises): 23/23 = 100.0%\\nH8 conj-collapse (concl = P1∧P2∧...):      0/23 = 0.0%\\nAny conclusion-in-premise (H7a+H1):         23/23 = 100.0%\\nContent-independent predicates:              0/23 = 0.0%\\nGenuine (proved - H7 - H1 - H8):           0/23 = 0.0%\\n---\\nH7 relaxed (single_premise + ISR>=0.5):     0/23 = 0.0%\\nSingle premise: 0/23 = 0.0%\\nISR = 1.0:      0/23 = 0.0%\\n\\n  H1 examples (first 3):\\n    folio_71: 20 premises, isr=0.0\\n    folio_160: 15 premises, isr=0.0\\n    folio_192: 16 premises, isr=0.0\\n\\n\\n===================================================================================================================\\n  SUMMARY TABLE\\n===================================================================================================================\\nRun                                      Proved    H7a    H7b     H7     H1     H8  Genuine    Gen% CntIndep\\n-------------------------------------------------------------------------------------------------------------------\\nplan017_additive_random_s42                  48      4      0      4     44      0        0    0.0%        6\\nexp1_random_b03_s43_r4                       92      7      0      7     82      0        3    3.3%        4\\nexp1_random_b03_s44_r2                       23      0      0      0     23      0        0    0.0%        0\\n-------------------------------------------------------------------------------------------------------------------\\n\\nJSON saved to /root/autodl-tmp/outputs/h7_classification/random_b03_3seed_classify.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "53ac96ca-9b5a-409d-8d4f-d20f3cf3545d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\n============================================================\\\\n  plan017_additive_random_s42\\\\n============================================================\\\\nTotal samples: 100, Proved: 48\\\\nH7a (text-match tautology):                 4/48 = 8.3%\\\\nH7b (obfuscated tautology):                 0/48 = 0.0%\\\\nH7 total (H7a + H7b):                       4/48 = 8.3%\\\\nH1 strict  (multi-prem, concl in premises): 44/48 = 91.7%\\\\nH8 conj-collapse (concl = P1∧P2∧...):      0/48 = 0.0%\\\\nAny conclusion-in-premise (H7a+H1):         48/48 = 100.0%\\\\nContent-independent predicates:              6/48 = 12.5%\\\\nGenuine (proved - H7 - H1 - H8):           0/48 = 0.0%\\\\n---\\\\nH7 relaxed (single_premise + ISR>=0.5):     0/48 = 0.0%\\\\nSingle premise: 0/48 = 0.0%\\\\nISR = 1.0:      0/48 = 0.0%\\\\n\\\\n  H7a examples (first 3):\\\\n    folio_1051: 10 premises, isr=0.0\\\\n    folio_1381: 10 premises, isr=0.0\\\\n    folio_715: 5 premises, isr=0.0\\\\n\\\\n  H1 examples (first 3):\\\\n    folio_765: 7 premises, isr=0.1111111111111111\\\\n    folio_592: 7 premises, isr=0.1111111111111111\\\\n    folio_556: 5 premises, isr=0.2857142857142857\\\\n\\\\n============================================================\\\\n  exp1_random_b03_s43_r4\\\\n============================================================\\\\nTotal samples: 100, Proved: 92\\\\nH7a (text-match tautology):                 7/92 = 7.6%\\\\nH7b (obfuscated tautology):                 0/92 = 0.0%\\\\nH7 total (H7a + H7b):                       7/92 = 7.6%\\\\nH1 strict  (multi-prem, concl in premises): 82/92 = 89.1%\\\\nH8 conj-collapse (concl = P1∧P2∧...):      0/92 = 0.0%\\\\nAny conclusion-in-premise (H7a+H1):         89/92 = 96.7%\\\\nContent-independent predicates:              4/92 = 4.3%\\\\nGenuine (proved - H7 - H1 - H8):           3/92 = 3.3%\\\\n---\\\\nH7 relaxed (single_premise + ISR>=0.5):     0/92 = 0.0%\\\\nSingle premise: 0/92 = 0.0%\\\\nISR = 1.0:      0/92 = 0.0%\\\\n\\\\n  H7a examples (first 3):\\\\n    folio_233: 7 premises, isr=0.1111111111111111\\\\n    folio_711: 3 premises, isr=0.3333333333333333\\\\n    folio_394: 5 premises, isr=0.14285714285714285\\\\n\\\\n  H1 examples (first 3):\\\\n    folio_765: 7 premises, isr=0.2\\\\n    folio_1179: 7 premises, isr=0.3\\\\n    folio_1378: 9 premises, isr=0.25\\\\n\\\\n============================================================\\\\n  exp1_random_b03_s44_r2\\\\n============================================================\\\\nTotal samples: 100, Proved: 23\\\\nH7a (text-match tautology):                 0/23 = 0.0%\\\\nH7b (obfuscated tautology):                 0/23 = 0.0%\\\\nH7 total (H7a + H7b):                       0/23 = 0.0%\\\\nH1 strict  (multi-prem, concl in premises): 23/23 = 100.0%\\\\nH8 conj-collapse (concl = P1∧P2∧...):      0/23 = 0.0%\\\\nAny conclusion-in-premise (H7a+H1):         23/23 = 100.0%\\\\nContent-independent predicates:              0/23 = 0.0%\\\\nGenuine (proved - H7 - H1 - H8):           0/23 = 0.0%\\\\n---\\\\nH7 relaxed (single_premise + ISR>=0.5):     0/23 = 0.0%\\\\nSingle premise: 0/23 = 0.0%\\\\nISR = 1.0:      0/23 = 0.0%\\\\n\\\\n  H1 examples (first 3):\\\\n    folio_71: 20 premises, isr=0.0\\\\n    folio_160: 15 premises, isr=0.0\\\\n    folio_192: 16 premises, isr=0.0\\\\n\\\\n\\\\n===================================================================================================================\\\\n  SUMMARY TABLE\\\\n===================================================================================================================\\\\nRun                                      Proved    H7a    H7b     H7     H1     H8  Genuine    Gen% CntIndep\\\\n-------------------------------------------------------------------------------------------------------------------\\\\nplan017_additive_random_s42                  48      4      0      4     44      0        0    0.0%        6\\\\nexp1_random_b03_s43_r4                       92      7      0      7     82      0        3    3.3%        4\\\\nexp1_random_b03_s44_r2                       23      0      0      0     23      0        0    0.0%        0\\\\n-------------------------------------------------------------------------------------------------------------------\\\\n\\\\nJSON saved to /root/autodl-tmp/outputs/h7_classification/random_b03_3seed_classify.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.64}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n  plan017_additive_random_s42\\n============================================================\\nTotal samples: 100, Proved: 48\\nH7a (text-match tautology):                 4/48 = 8.3%\\nH7b (obfuscated tautology):                 0/48 = 0.0%\\nH7 total (H7a + H7b):                       4/48 = 8.3%\\nH1 strict  (multi-prem, concl in premises): 44/48 = 91.7%\\nH8 conj-collapse (concl = P1∧P2∧...):      0/48 = 0.0%\\nAny conclusion-in-premise (H7a+H1):         48/48 = 100.0%\\nContent-independent predicates:              6/48 = 12.5%\\nGenuine (proved - H7 - H1 - H8):           0/48 = 0.0%\\n---\\nH7 relaxed (single_premise + ISR>=0.5):     0/48 = 0.0%\\nSingle premise: 0/48 = 0.0%\\nISR = 1.0:      0/48 = 0.0%\\n\\n  H7a examples (first 3):\\n    folio_1051: 10 premises, isr=0.0\\n    folio_1381: 10 premises, isr=0.0\\n    folio_715: 5 premises, isr=0.0\\n\\n  H1 examples (first 3):\\n    folio_765: 7 premises, isr=0.1111111111111111\\n    folio_592: 7 premises, isr=0.1111111111111111\\n    folio_556: 5 premises, isr=0.2857142857142857\\n\\n============================================================\\n  exp1_random_b03_s43_r4\\n============================================================\\nTotal samples: 100, Proved: 92\\nH7a (text-match tautology):                 7/92 = 7.6%\\nH7b (obfuscated tautology):                 0/92 = 0.0%\\nH7 total (H7a + H7b):                       7/92 = 7.6%\\nH1 strict  (multi-prem, concl in premises): 82/92 = 89.1%\\nH8 conj-collapse (concl = P1∧P2∧...):      0/92 = 0.0%\\nAny conclusion-in-premise (H7a+H1):         89/92 = 96.7%\\nContent-independent predicates:              4/92 = 4.3%\\nGenuine (proved - H7 - H1 - H8):           3/92 = 3.3%\\n---\\nH7 relaxed (single_premise + ISR>=0.5):     0/92 = 0.0%\\nSingle premise: 0/92 = 0.0%\\nISR = 1.0:      0/92 = 0.0%\\n\\n  H7a examples (first 3):\\n    folio_233: 7 premises, isr=0.1111111111111111\\n    folio_711: 3 premises, isr=0.3333333333333333\\n    folio_394: 5 premises, isr=0.14285714285714285\\n\\n  H1 examples (first 3):\\n    folio_765: 7 premises, isr=0.2\\n    folio_1179: 7 premises, isr=0.3\\n    folio_1378: 9 premises, isr=0.25\\n\\n============================================================\\n  exp1_random_b03_s44_r2\\n============================================================\\nTotal samples: 100, Proved: 23\\nH7a (text-match tautology):                 0/23 = 0.0%\\nH7b (obfuscated tautology):                 0/23 = 0.0%\\nH7 total (H7a + H7b):                       0/23 = 0.0%\\nH1 strict  (multi-prem, concl in premises): 23/23 = 100.0%\\nH8 conj-collapse (concl = P1∧P2∧...):      0/23 = 0.0%\\nAny conclusion-in-premise (H7a+H1):         23/23 = 100.0%\\nContent-independent predicates:              0/23 = 0.0%\\nGenuine (proved - H7 - H1 - H8):           0/23 = 0.0%\\n---\\nH7 relaxed (single_premise + ISR>=0.5):     0/23 = 0.0%\\nSingle premise: 0/23 = 0.0%\\nISR = 1.0:      0/23 = 0.0%\\n\\n  H1 examples (first 3):\\n    folio_71: 20 premises, isr=0.0\\n    folio_160: 15 premises, isr=0.0\\n    folio_192: 16 premises, isr=0.0\\n\\n\\n===================================================================================================================\\n  SUMMARY TABLE\\n===================================================================================================================\\nRun                                      Proved    H7a    H7b     H7     H1     H8  Genuine    Gen% CntIndep\\n-------------------------------------------------------------------------------------------------------------------\\nplan017_additive_random_s42                  48      4      0      4     44      0        0    0.0%        6\\nexp1_random_b03_s43_r4                       92      7      0      7     82      0        3    3.3%        4\\nexp1_random_b03_s44_r2                       23      0      0      0     23      0        0    0.0%        0\\n-------------------------------------------------------------------------------------------------------------------\\n\\nJSON saved to /root/autodl-tmp/outputs/h7_classification/random_b03_3seed_classify.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
The classify_h7 results are ready. Now let me read the JSON output for detailed data, then update the registry for all three experiments.

Results summary:

| Experiment | Proved | H7 | H1 | H8 | Genuine | Gen% |
|---|---|---|---|---|---|---|
| plan017-additive-random-s42 (s42) | 48 | 4 | 44 | 0 | 0 | 0.0% |
| exp1-random-b03-s43-r4 (s43) | 92 | 7 | 82 | 0 | 3 | 3.3% |


| exp1-random-b03-s44-r2 (s44) | 23 | 0 | 23 | 0 | 0 | 0.0% |

Now I'm comparing these results against the old data to see what's changed. For s42, the H7 count increased from 0 to 4, which means 4 of the H1 results shifted to H7 classification.  S43 stayed consistent with the current standard, and s44 also shows no changes with H8 confirmed at 0. The main update needed is for s42 since that's where the reclassification occurred.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "fb7690e9-6beb-44de-bd9a-e17e6741762b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiQonb3yCfmPo3ZHsQSRy8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2120,
      "cache_read_input_tokens": 51641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2120
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

_source line 47_

分类完成。现在更新三个实验的 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "9cfb778a-ed29-46dd-bde7-700fe1ae8c10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiQonb3yCfmPo3ZHsQSRy8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2120,
      "cache_read_input_tokens": 51641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2120
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

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_017W1CwuyTc3CG5ro77qDLDq`</summary>

```json
{
  "exp_id": "plan017-additive-random-s42",
  "field": "metrics",
  "value": {
    "eval_prove_rate": 0.48,
    "eval_mean_isr": 0.0453,
    "eval_isr_std": 0.0759,
    "eval_median_isr": 0,
    "eval_max_isr": 0.2857,
    "eval_proved_only_isr": 0.0943,
    "eval_n_proved": 48,
    "eval_n_problems": 100,
    "eval_method": "eval_sta.py full STA",
    "eval_data": "proofwriter_fol_100.jsonl",
    "eval_component_count_mean": 9.6,
    "eval_component_count_2_ratio": 0,
    "tautological_collapse": false,
    "h7_count": 4,
    "h7_rate": 0.0833,
    "h7a_count": 4,
    "h7b_count": 0,
    "h1_count": 44,
    "h1_rate": 0.9167,
    "h8_count": 0,
    "h8_rate": 0,
    "genuine_count": 0,
    "genuine_rate": 0,
    "taxonomy_tool": "classify_h7.py standard (2026-05-15)",
    "taxonomy_note": "Re-classified with current classify_h7.py. Old values: H7=0, H1=48, genuine=0. New: H7=4 (4 H7a text-match tautologies reclassified from H1), H1=44, H8=0, genuine=0."
  },
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "865b07d6-9e0e-41c2-846d-5568f9006b76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiQonb3yCfmPo3ZHsQSRy8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2120,
      "cache_read_input_tokens": 51641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2120
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

_source line 49 · 2026-05-15T18:22:14.760Z_

<details><summary>↩ Tool result · `toolu_017W1CwuyTc3CG5ro77qDLDq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan017-additive-random-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:11:14.694Z\", \"updated_at\": \"2026-05-15T18:22:14.528Z\", \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\", \"parent\": \"plan013-random-reward-s42-r4\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random)\", \"plan_id\": \"plan017\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"beta\": 0.3}, \"pid\": \"207116\", \"log_path\": \"~/runs/solver-trace-ablation/plan017-additive-random-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"finished_at\": \"2026-05-14T05:17:13.920Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:17:18.376399+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan017_additive_random_s42\", \"notes\": \"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"tautological_collapse\": false, \"h7_count\": 4, \"h7_rate\": 0.0833, \"h7a_count\": 4, \"h7b_count\": 0, \"h1_count\": 44, \"h1_rate\": 0.9167, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"taxonomy_tool\": \"classify_h7.py standard (2026-05-15)\", \"taxonomy_note\": \"Re-classified with current classify_h7.py. Old values: H7=0, H1=48, genuine=0. New: H7=4 (4 H7a text-match tautologies reclassified from H1), H1=44, H8=0, genuine=0.\"}, \"completed_at\": \"2026-05-14T05:30:46.783Z\", \"h7a_count\": 4, \"h1_count\": 44, \"taxonomy_note\": \"D086 clean run: H7a=4 (new, deeper normalization), H7b=0, H1=44, H8=0, genuine=0. β=0.3 Random also produces H7 under higher reward pressure.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5213}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "62c5e5ea-acaf-41fb-b6ff-dcb0d2fcd43f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"plan017-additive-random-s42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T03:11:14.694Z\\\", \\\"updated_at\\\": \\\"2026-05-15T18:22:14.528Z\\\", \\\"hypothesis\\\": \\\"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\\\", \\\"parent\\\": \\\"plan013-random-reward-s42-r4\\\", \\\"server\\\": \\\"westd-39279\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"account\\\": \\\"root\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\\\\\"\\\", \\\"server\\\": \\\"westd-39279\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"data_path\\\": \\\"/root/solver-trace-ablation/data/train_500_seed42.jsonl\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"Qwen3-4B\\\", \\\"seed\\\": 42, \\\"hypothesis\\\": \\\"Additive random control: r = r_exec·(1+0.3·random)\\\", \\\"plan_id\\\": \\\"plan017\\\", \\\"reward_formula\\\": \\\"r = r_exec * (1 + 0.3 * random[0,1])\\\", \\\"beta\\\": 0.3}, \\\"pid\\\": \\\"207116\\\", \\\"log_path\\\": \\\"~/runs/solver-trace-ablation/plan017-additive-random-s42.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-14T05:17:13.920Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T05:17:18.376399+00:00\\\"}]}, \\\"conclusion\\\": \\\"negative\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/outputs/plan017_additive_random_s42\\\", \\\"notes\\\": \\\"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.48, \\\"eval_mean_isr\\\": 0.0453, \\\"eval_isr_std\\\": 0.0759, \\\"eval_median_isr\\\": 0, \\\"eval_max_isr\\\": 0.2857, \\\"eval_proved_only_isr\\\": 0.0943, \\\"eval_n_proved\\\": 48, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_component_count_mean\\\": 9.6, \\\"eval_component_count_2_ratio\\\": 0, \\\"tautological_collapse\\\": false, \\\"h7_count\\\": 4, \\\"h7_rate\\\": 0.0833, \\\"h7a_count\\\": 4, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 44, \\\"h1_rate\\\": 0.9167, \\\"h8_count\\\": 0, \\\"h8_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"taxonomy_tool\\\": \\\"classify_h7.py standard (2026-05-15)\\\", \\\"taxonomy_note\\\": \\\"Re-classified with current classify_h7.py. Old values: H7=0, H1=48, genuine=0. New: H7=4 (4 H7a text-match tautologies reclassified from H1), H1=44, H8=0, genuine=0.\\\"}, \\\"completed_at\\\": \\\"2026-05-14T05:30:46.783Z\\\", \\\"h7a_count\\\": 4, \\\"h1_count\\\": 44, \\\"taxonomy_note\\\": \\\"D086 clean run: H7a=4 (new, deeper normalization), H7b=0, H1=44, H8=0, genuine=0. β=0.3 Random also produces H7 under higher reward pressure.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5213}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"plan017-additive-random-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:11:14.694Z\", \"updated_at\": \"2026-05-15T18:22:14.528Z\", \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\", \"parent\": \"plan013-random-reward-s42-r4\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random)\", \"plan_id\": \"plan017\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"beta\": 0.3}, \"pid\": \"207116\", \"log_path\": \"~/runs/solver-trace-ablation/plan017-additive-random-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"finished_at\": \"2026-05-14T05:17:13.920Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:17:18.376399+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan017_additive_random_s42\", \"notes\": \"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"tautological_collapse\": false, \"h7_count\": 4, \"h7_rate\": 0.0833, \"h7a_count\": 4, \"h7b_count\": 0, \"h1_count\": 44, \"h1_rate\": 0.9167, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"taxonomy_tool\": \"classify_h7.py standard (2026-05-15)\", \"taxonomy_note\": \"Re-classified with current classify_h7.py. Old values: H7=0, H1=48, genuine=0. New: H7=4 (4 H7a text-match tautologies reclassified from H1), H1=44, H8=0, genuine=0.\"}, \"completed_at\": \"2026-05-14T05:30:46.783Z\", \"h7a_count\": 4, \"h1_count\": 44, \"taxonomy_note\": \"D086 clean run: H7a=4 (new, deeper normalization), H7b=0, H1=44, H8=0, genuine=0. β=0.3 Random also produces H7 under higher reward pressure.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5213}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01M7d8q68jiUBJTcN4XrCto3`</summary>

```json
{
  "exp_id": "exp1-random-b03-s43-r4",
  "field": "metrics",
  "value": {
    "final_step": 500,
    "prove_rate": 0.5505,
    "mean_isr": 0.1358,
    "parse_rate": 1,
    "train_loss": 0.01365,
    "train_runtime_sec": 6161.1,
    "epoch": 2,
    "eval_prove_rate": 0.92,
    "eval_mean_isr": 0.1659,
    "eval_isr_std": 0.1147,
    "eval_median_isr": 0.1429,
    "eval_proved_only_mean_isr": 0.1803,
    "eval_min_isr": 0,
    "eval_max_isr": 0.5,
    "eval_n_proved": 92,
    "eval_n_problems": 100,
    "eval_data": "proofwriter_fol_100.jsonl",
    "eval_by_answer_type": {
      "false": {
        "count": 25,
        "proved": 23,
        "prove_rate": 0.92,
        "mean_isr": 0.156
      },
      "unknown": {
        "count": 41,
        "proved": 37,
        "prove_rate": 0.902,
        "mean_isr": 0.184
      },
      "true": {
        "count": 34,
        "proved": 32,
        "prove_rate": 0.941,
        "mean_isr": 0.151
      }
    },
    "h7_count": 7,
    "h7_rate": 0.076,
    "h7a_count": 7,
    "h7b_count": 0,
    "h1_count": 82,
    "h1_rate": 0.891,
    "h8_count": 0,
    "h8_rate": 0,
    "genuine_count": 3,
    "genuine_rate": 0.0326,
    "taxonomy_tool": "classify_h7.py standard (2026-05-15)",
    "taxonomy_note": "Re-classified with current classify_h7.py. Matches previous strict values: H7=7, H1=82, H8=0, genuine=3. No change."
  },
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "756bf38d-a4f3-4aa0-9ea6-4f2b67407da2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiQonb3yCfmPo3ZHsQSRy8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2120,
      "cache_read_input_tokens": 51641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2120
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

_source line 51 · 2026-05-15T18:22:22.085Z_

<details><summary>↩ Tool result · `toolu_01M7d8q68jiUBJTcN4XrCto3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp1-random-b03-s43-r4\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:44:48.792Z\", \"updated_at\": \"2026-05-15T18:22:21.716Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.3 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/exp1_random_b03_s43_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"117566\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-random-b03-s43-r4.log\", \"submitted_at\": \"2026-05-15T02:44:48.579Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"Random beta=0.3 s43 retry #4: previous r2 killed, r3 OOM. Clean GPU now.\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"plan_id\": \"EXP-1\", \"output_dir\": \"/root/autodl-tmp/outputs/exp1_random_b03_s43_r4\", \"wall_clock_seconds\": 6738.6, \"gpu_hours\": 1.87}, \"reproduce\": {\"finished_at\": \"2026-05-15T04:29:26.819Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:29:29.426423+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_step\": 500, \"prove_rate\": 0.5505, \"mean_isr\": 0.1358, \"parse_rate\": 1, \"train_loss\": 0.01365, \"train_runtime_sec\": 6161.1, \"epoch\": 2, \"eval_prove_rate\": 0.92, \"eval_mean_isr\": 0.1659, \"eval_isr_std\": 0.1147, \"eval_median_isr\": 0.1429, \"eval_proved_only_mean_isr\": 0.1803, \"eval_min_isr\": 0, \"eval_max_isr\": 0.5, \"eval_n_proved\": 92, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 23, \"prove_rate\": 0.92, \"mean_isr\": 0.156}, \"unknown\": {\"count\": 41, \"proved\": 37, \"prove_rate\": 0.902, \"mean_isr\": 0.184}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.151}}, \"h7_count\": 7, \"h7_rate\": 0.076, \"h7a_count\": 7, \"h7b_count\": 0, \"h1_count\": 82, \"h1_rate\": 0.891, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 3, \"genuine_rate\": 0.0326, \"taxonomy_tool\": \"classify_h7.py standard (2026-05-15)\", \"taxonomy_note\": \"Re-classified with current classify_h7.py. Matches previous strict values: H7=7, H1=82, H8=0, genuine=3. No change.\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s43_r4/checkpoint-500\", \"completed_at\": \"2026-05-15T04:37:07.139Z\", \"notes\": \"Training 500/500 steps, 1h42m. Final train: prove_rate=0.5505, mean_isr=0.1358, loss=0.01365. EVAL (proofwriter_fol_100.jsonl): PR=0.92, ISR=0.1659, H7=7/92(7.6%), H1=90/92(97.8%), genuine=2/92(2.2%). ANOMALY: massive seed variance vs s44-r2 (PR=0.23, ISR=0, H1=100%, genuine=0%). s43 learned high-PR hacking strategy with conclusion-in-premise; s44 barely proved anything. Both are random baseline — this variance weakens cross-seed claims.\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-random-b03-s43-r4.log\", \"eval_h7_strict_count\": 0, \"eval_h1_strict_count\": 89, \"eval_genuine_count\": 3, \"h7a_count\": 7, \"h1_count\": 82, \"taxonomy_note\": \"D086 clean run: H7a=7, H1=82, genuine=3. metrics 字段已从旧值 (H1=90, genuine=2) 同步修正.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.138}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "c3198d87-05cd-449c-a182-3411eaca4dcf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp1-random-b03-s43-r4\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T02:44:48.792Z\\\", \\\"updated_at\\\": \\\"2026-05-15T18:22:21.716Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.3 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/exp1_random_b03_s43_r4\\\\\\\"\\\", \\\"server\\\": \\\"westd-39279\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"117566\\\", \\\"log_path\\\": \\\"~/runs/solver-trace-ablation/exp1-random-b03-s43-r4.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T02:44:48.579Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/train_500_seed42.jsonl\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"Qwen3-4B\\\", \\\"seed\\\": 43, \\\"hypothesis\\\": \\\"Random beta=0.3 s43 retry #4: previous r2 killed, r3 OOM. Clean GPU now.\\\", \\\"reward_formula\\\": \\\"r = r_exec * (1 + 0.3 * random[0,1])\\\", \\\"plan_id\\\": \\\"EXP-1\\\", \\\"output_dir\\\": \\\"/root/autodl-tmp/outputs/exp1_random_b03_s43_r4\\\", \\\"wall_clock_seconds\\\": 6738.6, \\\"gpu_hours\\\": 1.87}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-15T04:29:26.819Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T04:29:29.426423+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_step\\\": 500, \\\"prove_rate\\\": 0.5505, \\\"mean_isr\\\": 0.1358, \\\"parse_rate\\\": 1, \\\"train_loss\\\": 0.01365, \\\"train_runtime_sec\\\": 6161.1, \\\"epoch\\\": 2, \\\"eval_prove_rate\\\": 0.92, \\\"eval_mean_isr\\\": 0.1659, \\\"eval_isr_std\\\": 0.1147, \\\"eval_median_isr\\\": 0.1429, \\\"eval_proved_only_mean_isr\\\": 0.1803, \\\"eval_min_isr\\\": 0, \\\"eval_max_isr\\\": 0.5, \\\"eval_n_proved\\\": 92, \\\"eval_n_problems\\\": 100, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 23, \\\"prove_rate\\\": 0.92, \\\"mean_isr\\\": 0.156}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 37, \\\"prove_rate\\\": 0.902, \\\"mean_isr\\\": 0.184}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 32, \\\"prove_rate\\\": 0.941, \\\"mean_isr\\\": 0.151}}, \\\"h7_count\\\": 7, \\\"h7_rate\\\": 0.076, \\\"h7a_count\\\": 7, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 82, \\\"h1_rate\\\": 0.891, \\\"h8_count\\\": 0, \\\"h8_rate\\\": 0, \\\"genuine_count\\\": 3, \\\"genuine_rate\\\": 0.0326, \\\"taxonomy_tool\\\": \\\"classify_h7.py standard (2026-05-15)\\\", \\\"taxonomy_note\\\": \\\"Re-classified with current classify_h7.py. Matches previous strict values: H7=7, H1=82, H8=0, genuine=3. No change.\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/outputs/exp1_random_b03_s43_r4/checkpoint-500\\\", \\\"completed_at\\\": \\\"2026-05-15T04:37:07.139Z\\\", \\\"notes\\\": \\\"Training 500/500 steps, 1h42m. Final train: prove_rate=0.5505, mean_isr=0.1358, loss=0.01365. EVAL (proofwriter_fol_100.jsonl): PR=0.92, ISR=0.1659, H7=7/92(7.6%), H1=90/92(97.8%), genuine=2/92(2.2%). ANOMALY: massive seed variance vs s44-r2 (PR=0.23, ISR=0, H1=100%, genuine=0%). s43 learned high-PR hacking strategy with conclusion-in-premise; s44 barely proved anything. Both are random baseline — this variance weakens cross-seed claims.\\\", \\\"log_path\\\": \\\"~/runs/solver-trace-ablation/exp1-random-b03-s43-r4.log\\\", \\\"eval_h7_strict_count\\\": 0, \\\"eval_h1_strict_count\\\": 89, \\\"eval_genuine_count\\\": 3, \\\"h7a_count\\\": 7, \\\"h1_count\\\": 82, \\\"taxonomy_note\\\": \\\"D086 clean run: H7a=7, H1=82, genuine=3. metrics 字段已从旧值 (H1=90, genuine=2) 同步修正.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.138}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp1-random-b03-s43-r4\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:44:48.792Z\", \"updated_at\": \"2026-05-15T18:22:21.716Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.3 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/exp1_random_b03_s43_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"117566\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-random-b03-s43-r4.log\", \"submitted_at\": \"2026-05-15T02:44:48.579Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"Random beta=0.3 s43 retry #4: previous r2 killed, r3 OOM. Clean GPU now.\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"plan_id\": \"EXP-1\", \"output_dir\": \"/root/autodl-tmp/outputs/exp1_random_b03_s43_r4\", \"wall_clock_seconds\": 6738.6, \"gpu_hours\": 1.87}, \"reproduce\": {\"finished_at\": \"2026-05-15T04:29:26.819Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:29:29.426423+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_step\": 500, \"prove_rate\": 0.5505, \"mean_isr\": 0.1358, \"parse_rate\": 1, \"train_loss\": 0.01365, \"train_runtime_sec\": 6161.1, \"epoch\": 2, \"eval_prove_rate\": 0.92, \"eval_mean_isr\": 0.1659, \"eval_isr_std\": 0.1147, \"eval_median_isr\": 0.1429, \"eval_proved_only_mean_isr\": 0.1803, \"eval_min_isr\": 0, \"eval_max_isr\": 0.5, \"eval_n_proved\": 92, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 23, \"prove_rate\": 0.92, \"mean_isr\": 0.156}, \"unknown\": {\"count\": 41, \"proved\": 37, \"prove_rate\": 0.902, \"mean_isr\": 0.184}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.151}}, \"h7_count\": 7, \"h7_rate\": 0.076, \"h7a_count\": 7, \"h7b_count\": 0, \"h1_count\": 82, \"h1_rate\": 0.891, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 3, \"genuine_rate\": 0.0326, \"taxonomy_tool\": \"classify_h7.py standard (2026-05-15)\", \"taxonomy_note\": \"Re-classified with current classify_h7.py. Matches previous strict values: H7=7, H1=82, H8=0, genuine=3. No change.\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s43_r4/checkpoint-500\", \"completed_at\": \"2026-05-15T04:37:07.139Z\", \"notes\": \"Training 500/500 steps, 1h42m. Final train: prove_rate=0.5505, mean_isr=0.1358, loss=0.01365. EVAL (proofwriter_fol_100.jsonl): PR=0.92, ISR=0.1659, H7=7/92(7.6%), H1=90/92(97.8%), genuine=2/92(2.2%). ANOMALY: massive seed variance vs s44-r2 (PR=0.23, ISR=0, H1=100%, genuine=0%). s43 learned high-PR hacking strategy with conclusion-in-premise; s44 barely proved anything. Both are random baseline — this variance weakens cross-seed claims.\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-random-b03-s43-r4.log\", \"eval_h7_strict_count\": 0, \"eval_h1_strict_count\": 89, \"eval_genuine_count\": 3, \"h7a_count\": 7, \"h1_count\": 82, \"taxonomy_note\": \"D086 clean run: H7a=7, H1=82, genuine=3. metrics 字段已从旧值 (H1=90, genuine=2) 同步修正.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.138}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01DpMQkhWEwdQZ2VCejWPsFg`</summary>

```json
{
  "exp_id": "exp1-random-b03-s44-r2",
  "field": "metrics",
  "value": {
    "eval_prove_rate": 0.23,
    "eval_proved_only_mean_isr": 0,
    "eval_mean_isr": 0,
    "eval_isr_std": 0,
    "eval_median_isr": 0,
    "eval_n_proved": 23,
    "eval_n_problems": 100,
    "eval_data": "proofwriter_fol_100.jsonl",
    "h7_count": 0,
    "h7_rate": 0,
    "h7a_count": 0,
    "h7b_count": 0,
    "h1_count": 23,
    "h1_rate": 1,
    "h8_count": 0,
    "h8_rate": 0,
    "genuine_count": 0,
    "genuine_rate": 0,
    "taxonomy_tool": "classify_h7.py standard (2026-05-15)",
    "taxonomy_note": "Re-classified with current classify_h7.py. Matches previous values: H7=0, H1=23, H8=0, genuine=0. No change."
  },
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "6dae5ac2-3c31-4223-a617-cd45d0153e71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiQonb3yCfmPo3ZHsQSRy8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2120,
      "cache_read_input_tokens": 51641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2120
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

_source line 53 · 2026-05-15T18:22:24.320Z_

<details><summary>↩ Tool result · `toolu_01DpMQkhWEwdQZ2VCejWPsFg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp1-random-b03-s44-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:42:02.173Z\", \"updated_at\": \"2026-05-15T18:22:24.072Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.3 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/exp1_random_b03_s44_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": 51297, \"log_path\": \"/root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s44_r2.json\", \"submitted_at\": \"2026-05-15T00:42:39.447Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"hypothesis\": \"Random beta=0.3 s44: 3-seed random control for Claim 2\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"plan_id\": \"EXP-1\", \"parent\": \"exp1-random-b03-s44\", \"output_dir\": \"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2\", \"wall_clock_seconds\": 8595.6, \"gpu_hours\": 2.39}, \"reproduce\": {\"finished_at\": \"2026-05-15T02:26:26.919Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T02:26:39.221668+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.23, \"eval_proved_only_mean_isr\": 0, \"eval_mean_isr\": 0, \"eval_isr_std\": 0, \"eval_median_isr\": 0, \"eval_n_proved\": 23, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 23, \"h1_rate\": 1, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"taxonomy_tool\": \"classify_h7.py standard (2026-05-15)\", \"taxonomy_note\": \"Re-classified with current classify_h7.py. Matches previous values: H7=0, H1=23, H8=0, genuine=0. No change.\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2/reward_log.jsonl\", \"completed_at\": \"2026-05-15T03:05:55.070Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5747}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "0b04d84b-4482-4e70-af27-dc943735c489",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp1-random-b03-s44-r2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T00:42:02.173Z\\\", \\\"updated_at\\\": \\\"2026-05-15T18:22:24.072Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.3 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/exp1_random_b03_s44_r2\\\\\\\"\\\", \\\"server\\\": \\\"westd-39279\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 51297, \\\"log_path\\\": \\\"/root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s44_r2.json\\\", \\\"submitted_at\\\": \\\"2026-05-15T00:42:39.447Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/train_500_seed42.jsonl\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"Qwen3-4B\\\", \\\"seed\\\": 44, \\\"hypothesis\\\": \\\"Random beta=0.3 s44: 3-seed random control for Claim 2\\\", \\\"reward_formula\\\": \\\"r = r_exec * (1 + 0.3 * random[0,1])\\\", \\\"plan_id\\\": \\\"EXP-1\\\", \\\"parent\\\": \\\"exp1-random-b03-s44\\\", \\\"output_dir\\\": \\\"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2\\\", \\\"wall_clock_seconds\\\": 8595.6, \\\"gpu_hours\\\": 2.39}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-15T02:26:26.919Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T02:26:39.221668+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.23, \\\"eval_proved_only_mean_isr\\\": 0, \\\"eval_mean_isr\\\": 0, \\\"eval_isr_std\\\": 0, \\\"eval_median_isr\\\": 0, \\\"eval_n_proved\\\": 23, \\\"eval_n_problems\\\": 100, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h7a_count\\\": 0, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 23, \\\"h1_rate\\\": 1, \\\"h8_count\\\": 0, \\\"h8_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"taxonomy_tool\\\": \\\"classify_h7.py standard (2026-05-15)\\\", \\\"taxonomy_note\\\": \\\"Re-classified with current classify_h7.py. Matches previous values: H7=0, H1=23, H8=0, genuine=0. No change.\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2/checkpoint-500\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2/reward_log.jsonl\\\", \\\"completed_at\\\": \\\"2026-05-15T03:05:55.070Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5747}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp1-random-b03-s44-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:42:02.173Z\", \"updated_at\": \"2026-05-15T18:22:24.072Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.3 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/exp1_random_b03_s44_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": 51297, \"log_path\": \"/root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s44_r2.json\", \"submitted_at\": \"2026-05-15T00:42:39.447Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"hypothesis\": \"Random beta=0.3 s44: 3-seed random control for Claim 2\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"plan_id\": \"EXP-1\", \"parent\": \"exp1-random-b03-s44\", \"output_dir\": \"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2\", \"wall_clock_seconds\": 8595.6, \"gpu_hours\": 2.39}, \"reproduce\": {\"finished_at\": \"2026-05-15T02:26:26.919Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T02:26:39.221668+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.23, \"eval_proved_only_mean_isr\": 0, \"eval_mean_isr\": 0, \"eval_isr_std\": 0, \"eval_median_isr\": 0, \"eval_n_proved\": 23, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 23, \"h1_rate\": 1, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"taxonomy_tool\": \"classify_h7.py standard (2026-05-15)\", \"taxonomy_note\": \"Re-classified with current classify_h7.py. Matches previous values: H7=0, H1=23, H8=0, genuine=0. No change.\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/exp1_random_b03_s44_r2/reward_log.jsonl\", \"completed_at\": \"2026-05-15T03:05:55.070Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5747}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 54_

三个 registry 全部更新完成。

## 结果汇总

### β=0.3 Random 三 seed 标准 classify_h7 taxonomy

| Seed | Proved | H7 | H1 | H8 | Genuine | Gen% |
|------|--------|-----|-----|-----|---------|------|
| s42 (plan017) | 48 | 4 | 44 | 0 | 0 | 0.0% |
| s43 (exp1-r4) | 92 | 7 | 82 | 0 | 3 | 3.3% |
| s44 (exp1-r2) | 23 | 0 | 23 | 0 | 0 | 0.0% |

### 新旧对比

| Experiment | Field | Old | New | Change |
|---|---|---|---|---|
| plan017-s42 | H7 | 0 | **4** | +4 (H7a 从 H1 拆出) |
| plan017-s42 | H1 | 48 | **44** | -4 |
| plan017-s42 | genuine | 0 | 0 | — |
| exp1-s43-r4 | H7 | 7 | 7 | — |
| exp1-s43-r4 | H1 | 82 | 82 | — |
| exp1-s43-r4 | genuine | 3 | 3 | — |
| exp1-s44-r2 | H7 | 0 | 0 | — |
| exp1-s44-r2 | H1 | 23 | 23 | — |
| exp1-s44-r2 | genuine | 0 | 0 | — |

唯一变化：plan017-s42 有 4 个样本从 H1 重分类为 H7a（多前提中有单前提文本匹配结论的情况，之前旧版本未检测到）。s43 和 s44 的结果与之前完全一致。三个实验均 H8=0。JSON 审计文件已保存至 `/root/autodl-tmp/outputs/h7_classification/random_b03_3seed_classify.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "uuid": "17c44005-077e-420a-aa08-3da723841ff6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013TiQaAdpjEcPbsAd3mW8co",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6474,
      "cache_read_input_tokens": 53761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6474
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

_source line 55_

三个 registry 全部更新完成。

## 结果汇总

### β=0.3 Random 三 seed 标准 classify_h7 taxonomy

| Seed | Proved | H7 | H1 | H8 | Genuine | Gen% |
|------|--------|-----|-----|-----|---------|------|
| s42 (plan017) | 48 | 4 | 44 | 0 | 0 | 0.0% |
| s43 (exp1-r4) | 92 | 7 | 82 | 0 | 3 | 3.3% |
| s44 (exp1-r2) | 23 | 0 | 23 | 0 | 0 | 0.0% |

### 新旧对比

| Experiment | Field | Old | New | Change |
|---|---|---|---|---|
| plan017-s42 | H7 | 0 | **4** | +4 (H7a 从 H1 拆出) |
| plan017-s42 | H1 | 48 | **44** | -4 |
| plan017-s42 | genuine | 0 | 0 | — |
| exp1-s43-r4 | H7 | 7 | 7 | — |
| exp1-s43-r4 | H1 | 82 | 82 | — |
| exp1-s43-r4 | genuine | 3 | 3 | — |
| exp1-s44-r2 | H7 | 0 | 0 | — |
| exp1-s44-r2 | H1 | 23 | 23 | — |
| exp1-s44-r2 | genuine | 0 | 0 | — |

唯一变化：plan017-s42 有 4 个样本从 H1 重分类为 H7a（多前提中有单前提文本匹配结论的情况，之前旧版本未检测到）。s43 和 s44 的结果与之前完全一致。三个实验均 H8=0。JSON 审计文件已保存至 `/root/autodl-tmp/outputs/h7_classification/random_b03_3seed_classify.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 96022,
  "duration_api_ms": 96278,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "c73ca316-b6e6-4c17-b8da-f82769cd2ff5",
  "total_cost_usd": 0.619912,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 48394,
    "cache_read_input_tokens": 347943,
    "output_tokens": 5598,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 48394,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 601,
        "cache_read_input_tokens": 53761,
        "cache_creation_input_tokens": 6474,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6474
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3328,
      "outputTokens": 27,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003463,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 5598,
      "cacheReadInputTokens": 347943,
      "cacheCreationInputTokens": 48394,
      "webSearchRequests": 0,
      "costUSD": 0.616449,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2c07c072-3c0a-4017-b80e-d58e433a172e"
}
```

</details>

---
