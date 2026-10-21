# ops westd27271 cleanup deploy v1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_ops_westd27271_cleanup_deploy_v1_20260522T091519.log`
- **Structured JSON:** [`089a23514c62d0d36f1e.json`](../../sessions/08/089a23514c62d0d36f1e.json)

## Before a recorded user message

28 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
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
  "uuid": "93651322-3af3-4a02-88d9-f84357503134",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1779459000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "351fb5f7-b6ed-4724-8083-aa62919c523e",
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down the task:

1. Kill duplicate process PID 213482 on GPU 1
2. Check for duplicate experiments on other servers
3. Check registry for experiment status
4. Deploy 3 new experiments to GPUs 0, 2, 3
5. Verify and report

Let me start by loading the necessary tools and doing the initial checks in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "ed4bf365-8f0f-4533-8c77-2518f2129507",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JvqLCfZN4SVhntKYDDipbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12464,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12464
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

先加载工具，同时做去重检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "09a12e4d-1ecc-45e9-a8bf-3cebfaef500b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JvqLCfZN4SVhntKYDDipbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12464,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12464
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KPetbTLwN9CfxDU4x9zk6g`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__kill_job,mcp__agent-ml-research__detect_image",
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
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "63b87bc0-b9a3-48b4-b548-ba0065849b56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JvqLCfZN4SVhntKYDDipbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12464,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12464
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 7 · 2026-05-22T09:15:31.900Z_

<details><summary>↩ Tool result · `toolu_01KPetbTLwN9CfxDU4x9zk6g`</summary>

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
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "cef93de7-2876-42d9-ad5e-b327dcaca864",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__kill_job,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me do the initial checks in parallel:
1. Kill the duplicate process on westd-27271
2. Check registry for the 3 experiment IDs
3. Check westd-38929 for duplicate experiments
4. Check cqa1 for duplicate experiments
5. Check current state on westd-27271
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "d90ea882-4d00-4730-b10d-dcd2c3521562",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PAzRWHigCTUTVLUTJVchg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1570,
      "cache_read_input_tokens": 24305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1570
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

_source line 9_

开始并行执行：kill 重复进程 + 去重检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "5e10ea5b-e66a-4a12-8717-41b71f7301ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PAzRWHigCTUTVLUTJVchg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1570,
      "cache_read_input_tokens": 24305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1570
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__kill_job · `toolu_01434X6MRzR96iS1WV9ovsKb`</summary>

```json
{
  "server": "westd-27271",
  "pid": "213482",
  "reason": "Duplicate process for l2norm_k095_object_seed43, keeping PID 212585",
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
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "40a8a6a5-6ac3-41b1-ab6a-9310b6f4efbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PAzRWHigCTUTVLUTJVchg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1570,
      "cache_read_input_tokens": 24305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1570
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_013NBQcCo44CZyTmgxeiZa2t`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "status",
    "conclusion"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "2da67e42-b2ed-4e93-b192-cf2ec9c115f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PAzRWHigCTUTVLUTJVchg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1570,
      "cache_read_input_tokens": 24305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1570
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KBNsinKqg2kshRWQT5Wd9x`</summary>

```json
{
  "server": "westd-27271",
  "command": "ps aux | grep eval_pi05 | grep -v grep",
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
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "e445e8b9-be76-440d-b318-6a79b8541f11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PAzRWHigCTUTVLUTJVchg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1570,
      "cache_read_input_tokens": 24305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1570
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

_source line 13 · 2026-05-22T09:15:42.453Z_

<details><summary>↩ Tool result · `toolu_01434X6MRzR96iS1WV9ovsKb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"pid\": \"213482\", \"reason\": \"Duplicate process for l2norm_k095_object_seed43, keeping PID 212585\", \"force_killed\": true}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.22}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "f4f9cda0-9832-4e4b-b45b-76a3c289eed1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"pid\\\": \\\"213482\\\", \\\"reason\\\": \\\"Duplicate process for l2norm_k095_object_seed43, keeping PID 212585\\\", \\\"force_killed\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.22}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"pid\": \"213482\", \"reason\": \"Duplicate process for l2norm_k095_object_seed43, keeping PID 212585\", \"force_killed\": true}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.22}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01N98H21UjQ7fEN76veu178L`</summary>

```json
{
  "server": "westd-38929",
  "command": "ps aux | grep eval_pi05 | grep -v grep",
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
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "4a8285be-0d85-440c-9c61-1f96c31c16d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PAzRWHigCTUTVLUTJVchg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1570,
      "cache_read_input_tokens": 24305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1570
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

_source line 15 · 2026-05-22T09:15:43.357Z_

<details><summary>↩ Tool result · `toolu_013NBQcCo44CZyTmgxeiZa2t`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_pi05_l2norm_k07_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k07_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32_official\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_smolvla_official_l2norm_k090_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_random_k085_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k05_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k07_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k085_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k0925_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k09_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k09_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k095_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k0925_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k05_object_seed42_v5\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k085_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k095_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k03_object_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_random_k085_object_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_random_k095_spatial_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_l2norm_k07_object_seed43_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k095_spatial_seed42_v4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k0925_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k095_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k085_object_seed43_v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_pi05_l2norm_k0925_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k095_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k095_spatial_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_l2norm_k095_spatial_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_l2norm_k085_spatial_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_l2norm_k07_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k085_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k09_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k09_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k0925_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k085_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k07_spatial_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k095_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_l2norm_k085_object_seed42_v4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k095_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k085_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_baseline_spatial_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_openvla_sc_m32_vtconly_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k0925_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_pi05_random_k03_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_l2norm_k085_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k085_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k085_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_pi05_random_k03_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k09_fixedmask_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train_smart_compress_m16_seed44_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m16_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m128_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m96_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m32_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m64_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m128_resume\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k07_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_k07_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_k09_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_l2norm_k03_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k09_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k05_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k095_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k050_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k090_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_l2norm_k070_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_l2norm_k030_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k070_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k030_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_l2norm_k050_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k05_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k03_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_pi05_random_k05_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k085_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k09_fixedmask_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_baseline_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k095_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k09_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k09_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k01_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k050_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_l2norm_k095_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k095_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_baseline_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_l2norm_k095_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k095_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_baseline_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k05_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_openvla_sc_m64_seed42_v5\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_l2norm_k09_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k03_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_k07_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_baseline_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k03_object_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k07_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k085_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k085_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k07_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k07_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k03_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_xvla_l2norm_k085_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_xvla_random_k085_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k03_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k03_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k07_object_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k07_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k03_object_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k07_object_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k07_object_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k03_object_seed42_rerun\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_k03_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k05_object_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_l2norm_k05_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k07_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k07_object_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_random_k07_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k03_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k07_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_random_k03_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k03_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k05_object_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k07_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_openvla_sc_m64_seed42_v4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_xvla_random_k07_object_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k05_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_sc_m128_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_random_k07_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_l2norm_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_xvla_random_k05_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k07_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_l2norm_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k03_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_k03_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_l2norm_k07_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_xvla_random_k03_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_baseline_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_baseline_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k07_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_sc_m128_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_prune_random_k05_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k085_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k07_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k095_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_baseline_spatial_westd38929_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k08_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k09_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_spatial_k085_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k07_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_oft_baseline_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_openvla_sc_m64_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_baseline_spatial_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_xvla_goal_k05_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_baseline_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_goal_k09_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_baseline_goal_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_baseline_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_spatial_k09_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_sc_m128_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_prune_random_k03_seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_prune_random_k07_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_prune_random_k095_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_prune_l2norm_k09_seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_xvla_spatial_k05_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k085_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k08_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k095_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k07_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_xvla_prune_k08_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k085_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k085_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k08_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k01_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k095_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k095_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k095_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k01_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k01_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k09_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k09_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k05_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k02_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k02_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k09\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k07_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k095\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k03\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k05\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k03_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k03_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k05_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k07_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k09_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k05_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_prune_random_k07_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_oft_baseline_k10\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_sc_m128_20k_seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_smart_compress_m16_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m16_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m128_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_openvla_sc_m128_vtconly_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_sc_m128_vtconly_20k_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_openvla_sc_m128_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"analysis_xvla_token_importance\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_openvla_sc_m96_vtconly_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_openvla_sc_m64_vtconly_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_c5_roboflamingo_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_c5_roboflamingo_libero_object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_openvla_sc_m128_lora_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_smart_compress_m32_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m96_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m64_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_pruning_sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_openvla_sc_m128_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_baseline_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m16_seed44_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_official_smolvla_prune_k05_spatial_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m96_seed44_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m64_seed44_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32_seed44_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_mlp_adapter_seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_official_smolvla_prune_k05_spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_smolvla_official_baseline_spatial_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_mlp_adapter_seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_mlp_adapter_control\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_smolvla_prune_k05_spatial_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_baseline_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_baseline_spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_smolvla_prune_k05_spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_smart_compress_m16_seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_mlp_adapter_control\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m128_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m32_official\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m128_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_k095\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_k09\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32_libero_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m64_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32_libero_goal\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_baseline_control_prune_k05\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m64_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m32_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m96_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m96_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_smart_compress_m96_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_baseline_control_100k_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_baseline_control_100k_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_official_smolvla_prune_k095\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_official_smolvla_prune_k09\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_acis_k05_supplement_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_acis_k05_supplement_200eps\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_official_smolvla_prune_k05_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_official_smolvla_baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_random_prune_k095\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_official_smolvla_pruning\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_baseline_control_100k\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_smart_compress_m128\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_pruning_k03_restart\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla_entropy_perlayer\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"inference_latency_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_pruning_k03\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"openvla_entropy_real\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m128\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_smart_compress_m96\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m16\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_pruning_k07\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m96\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smart_compress_m16\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m32\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_full_ft_baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_acis_stage1only_k03\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_pruning_k05\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"geometric_prior_k05_eval\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_openvla_crossmodel_pruning\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_geometric_prior_k09\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_geometric_prior_k07\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_geometric_prior_k05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"libero_fullft_batch64_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"baseline_bypass_object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"action_divergence_v2_clean\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_goal_prune_k05\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"offline_singlestep_action_error\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"offline_singlestep_error_k05\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_spatial_prune_k05\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_merge_k05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_k07_zero_mask\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_true_removal_k05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_stage1only_k09\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_random_prune_k05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train_acis_stage1only_k07\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_stage1only_object_v2_fixed\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_stage1only_spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_stage1_only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_fullft_seed1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_fullft_batch64\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_imm100k_bypass\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_k07_bypass_v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_k07_bypass_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_imm_k07_object\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_imm_anchor_v7_2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_imm_anchor_v7\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"libero_fullft_seed0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_imm_fullft_k07\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_imm_fullft_seed0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_imm_fullft_100k\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_imm_fullft_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"libero_lora_seed0\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"libero_lora_baseline\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"libero_imm_twostage_v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan_009_token_importance\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_011_acis_overhead\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_008_pruning_sweep_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_005_formal_bound_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_008_pruning_sweep\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"baseline_v6_alpha16\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_imm_v8c_annealing\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_imm_v8b_twostage\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp_imm_anchor_v8_1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_imm_anchor_v8\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_baseline_v5\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp_imm_anchor_v7_1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_imm_anchor_v6\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_imm_anchor_v5\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_baseline_v4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mvp_imm_anchor_v4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_baseline_v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_imm_anchor_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_baseline_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_imm_anchor\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_baseline\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_prune_l2norm_k095_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k09_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k05_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k03_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_oft_baseline_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}}, \"count\": 343, \"total\": 343, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8909}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "101f5fad-a13c-4384-8056-d6215189593a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_pi05_l2norm_k07_spatial_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k07_spatial_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m32_official\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_smolvla_official_l2norm_k090_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_random_k085_spatial_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k05_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k07_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k085_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k0925_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k09_spatial_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k09_spatial_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k095_spatial_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k0925_spatial_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_l2norm_k05_object_seed42_v5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k085_spatial_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k095_spatial_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k03_object_seed43_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_random_k085_object_seed43_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_random_k095_spatial_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_l2norm_k07_object_seed43_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k095_spatial_seed42_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k0925_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k095_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k085_object_seed43_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_pi05_l2norm_k0925_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k095_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k095_spatial_seed42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_l2norm_k095_spatial_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_l2norm_k085_spatial_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_l2norm_k07_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k085_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k09_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k09_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k0925_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k085_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k07_spatial_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_random_k095_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_l2norm_k085_object_seed42_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k095_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k085_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_openvla_baseline_spatial_seed42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"train_openvla_sc_m32_vtconly_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_random_k0925_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_pi05_random_k03_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_l2norm_k085_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_random_k085_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_random_k085_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_pi05_random_k03_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k09_fixedmask_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"train_smart_compress_m16_seed44_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m16_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m128_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m96_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m32_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m64_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m128_resume\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k07_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_random_k05_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_random_k07_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_random_k09_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_l2norm_k03_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_l2norm_k09_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k05_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k095_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_random_k050_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_random_k090_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_l2norm_k070_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_l2norm_k030_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_random_k070_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_random_k030_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_l2norm_k050_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k05_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k03_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_pi05_random_k05_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k085_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_random_k09_fixedmask_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_baseline_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k095_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_random_k09_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k09_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k01_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_random_k050_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_l2norm_k095_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_random_k095_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_baseline_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_l2norm_k095_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_random_k095_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_baseline_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_l2norm_k05_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_openvla_sc_m64_seed42_v5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_l2norm_k09_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_l2norm_k03_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_random_k07_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_baseline_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_l2norm_k03_object_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k07_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k085_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k085_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k07_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k07_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_l2norm_k03_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_xvla_l2norm_k085_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_xvla_random_k085_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_l2norm_k03_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k03_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k07_object_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_l2norm_k07_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k03_object_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_l2norm_k07_object_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k07_object_seed43_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_l2norm_k03_object_seed42_rerun\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_random_k03_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_l2norm_k05_object_seed42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_openvla_l2norm_k05_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_l2norm_k07_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k07_object_seed42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_random_k07_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_l2norm_k03_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k07_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_random_k03_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_l2norm_k05_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_l2norm_k03_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k05_object_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_random_k05_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_l2norm_k07_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_openvla_sc_m64_seed42_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_xvla_random_k07_object_seed43_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k05_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_sc_m128_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_openvla_random_k07_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_l2norm_k05_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_xvla_random_k05_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k07_object_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_openvla_l2norm_k05_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_l2norm_k03_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_random_k03_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_openvla_l2norm_k07_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_xvla_random_k03_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_baseline_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_baseline_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k05_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k07_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_sc_m128_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_openvla_prune_random_k05_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k085_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_random_k07_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_random_k095_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_baseline_spatial_westd38929_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k08_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_random_k09_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_spatial_k085_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_l2norm_k07_seed43_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_oft_baseline_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"train_openvla_sc_m64_seed42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_openvla_baseline_spatial_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_xvla_goal_k05_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_baseline_long_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_goal_k09_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_baseline_goal_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_baseline_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_spatial_k09_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_sc_m128_spatial_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_openvla_prune_random_k03_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_openvla_prune_random_k07_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_openvla_prune_random_k095_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_openvla_prune_l2norm_k09_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_xvla_spatial_k05_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k085_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k08_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_random_k095_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_l2norm_k07_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_xvla_prune_k08_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k085_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k085_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k08_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k01_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k095_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k095_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k095_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k01_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k01_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_random_k09_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_random_k09_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_random_k05_seed43_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k02_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k02_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_l2norm_k09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_random_k07_seed43_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_l2norm_k095\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_l2norm_k03\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_l2norm_k05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k03_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k03_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k05_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k07_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_xvla_prune_k09_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_random_k05_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_openvla_prune_random_k07_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_oft_baseline_k10\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_openvla_sc_m128_20k_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_smart_compress_m16_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m16_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m128_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_openvla_sc_m128_vtconly_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_openvla_sc_m128_vtconly_20k_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"train_openvla_sc_m128_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"analysis_xvla_token_importance\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_openvla_sc_m96_vtconly_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"train_openvla_sc_m64_vtconly_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"train_c5_roboflamingo_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"train_c5_roboflamingo_libero_object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"train_openvla_sc_m128_lora_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_smart_compress_m32_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m96_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m64_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_random_pruning_sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_openvla_sc_m128_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_openvla_baseline_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m16_seed44_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_official_smolvla_prune_k05_spatial_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m96_seed44_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m64_seed44_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m32_seed44_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_mlp_adapter_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_official_smolvla_prune_k05_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_smolvla_official_baseline_spatial_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_mlp_adapter_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_mlp_adapter_control\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_smolvla_prune_k05_spatial_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_baseline_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_official_baseline_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_smolvla_prune_k05_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"train_smart_compress_m16_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"train_mlp_adapter_control\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m32_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m128_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m32_official\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m128_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_k095\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_k09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m32_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m32_libero_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m64_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m32_libero_goal\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_baseline_control_prune_k05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m64_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m32_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m96_seed43_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m96_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"train_smart_compress_m96_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_baseline_control_100k_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_baseline_control_100k_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_official_smolvla_prune_k095\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_official_smolvla_prune_k09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_acis_k05_supplement_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_acis_k05_supplement_200eps\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_official_smolvla_prune_k05_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_official_smolvla_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smolvla_random_prune_k095\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_official_smolvla_pruning\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"train_baseline_control_100k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_smart_compress_m128\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_pruning_k03_restart\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"smolvla_entropy_perlayer\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"inference_latency_comparison\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_pruning_k03\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"openvla_entropy_real\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m128\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_smart_compress_m96\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m16\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_pruning_k07\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m96\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"smart_compress_m16\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m64\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m32\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m64\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"libero_full_ft_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_acis_stage1only_k03\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_openvla_pruning_k05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"geometric_prior_k05_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_openvla_crossmodel_pruning\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_geometric_prior_k09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_geometric_prior_k07\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_geometric_prior_k05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"libero_fullft_batch64_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"baseline_bypass_object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"action_divergence_v2_clean\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_goal_prune_k05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"offline_singlestep_action_error\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"offline_singlestep_error_k05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_spatial_prune_k05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_merge_k05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_k07_zero_mask\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_true_removal_k05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_stage1only_k09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_random_prune_k05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"train_acis_stage1only_k07\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_stage1only_object_v2_fixed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_stage1only_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_stage1_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"libero_fullft_seed1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"libero_fullft_batch64\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_imm100k_bypass\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_k07_bypass_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_k07_bypass_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_imm_k07_object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"mvp_imm_anchor_v7_2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"mvp_imm_anchor_v7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"libero_fullft_seed0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"libero_imm_fullft_k07\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"libero_imm_fullft_seed0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"libero_imm_fullft_100k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"libero_imm_fullft_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"libero_lora_seed0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"libero_lora_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"libero_imm_twostage_v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"plan_009_token_importance\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_011_acis_overhead\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_008_pruning_sweep_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_005_formal_bound_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_008_pruning_sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"baseline_v6_alpha16\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"mvp_imm_v8c_annealing\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"mvp_imm_v8b_twostage\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp_imm_anchor_v8_1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"mvp_imm_anchor_v8\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"mvp_baseline_v5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp_imm_anchor_v7_1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mvp_imm_anchor_v6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mvp_imm_anchor_v5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mvp_baseline_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mvp_imm_anchor_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mvp_baseline_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mvp_imm_anchor_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mvp_baseline_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mvp_imm_anchor\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mvp_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_openvla_prune_l2norm_k095_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_l2norm_k09_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_l2norm_k05_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_l2norm_k03_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_oft_baseline_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}}, \\\"count\\\": 343, \\\"total\\\": 343, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8909}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_pi05_l2norm_k07_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k07_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32_official\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_smolvla_official_l2norm_k090_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_random_k085_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k05_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k07_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k085_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k0925_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k09_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k09_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k095_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k0925_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k05_object_seed42_v5\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k085_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k095_spatial_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k03_object_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_random_k085_object_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_random_k095_spatial_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_l2norm_k07_object_seed43_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k095_spatial_seed42_v4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k0925_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k095_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k085_object_seed43_v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_pi05_l2norm_k0925_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k095_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k095_spatial_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_l2norm_k095_spatial_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_l2norm_k085_spatial_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_l2norm_k07_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k085_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k09_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k09_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k0925_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k085_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k07_spatial_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k095_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_l2norm_k085_object_seed42_v4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k095_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k085_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_baseline_spatial_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_openvla_sc_m32_vtconly_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k0925_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_pi05_random_k03_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_l2norm_k085_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k085_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k085_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_pi05_random_k03_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k09_fixedmask_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train_smart_compress_m16_seed44_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m16_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m128_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m96_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m32_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m64_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m128_resume\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k07_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_k07_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_k09_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_l2norm_k03_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k09_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k05_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k095_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k050_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k090_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_l2norm_k070_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_l2norm_k030_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k070_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k030_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_l2norm_k050_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k05_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k03_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_pi05_random_k05_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k085_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k09_fixedmask_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_baseline_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k095_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k09_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k09_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k01_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k050_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_l2norm_k095_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k095_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_baseline_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_l2norm_k095_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_random_k095_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_baseline_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k05_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_openvla_sc_m64_seed42_v5\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_l2norm_k09_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k03_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_k07_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_baseline_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k03_object_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k07_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k085_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k085_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k07_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k07_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k03_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_xvla_l2norm_k085_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_xvla_random_k085_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k03_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k03_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k07_object_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k07_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k03_object_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k07_object_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k07_object_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k03_object_seed42_rerun\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_k03_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k05_object_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_l2norm_k05_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k07_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k07_object_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_random_k07_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k03_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k07_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_random_k03_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k03_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k05_object_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_pi05_random_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_l2norm_k07_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_openvla_sc_m64_seed42_v4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_xvla_random_k07_object_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k05_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_sc_m128_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_random_k07_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_l2norm_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_xvla_random_k05_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k07_object_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_l2norm_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k03_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_k03_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_l2norm_k07_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_xvla_random_k03_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_baseline_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_baseline_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k07_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_sc_m128_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_prune_random_k05_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k085_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k07_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k095_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_baseline_spatial_westd38929_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k08_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_random_k09_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_spatial_k085_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k07_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_oft_baseline_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_openvla_sc_m64_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_baseline_spatial_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_xvla_goal_k05_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_baseline_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_goal_k09_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_baseline_goal_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_baseline_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_spatial_k09_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_sc_m128_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_prune_random_k03_seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_prune_random_k07_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_prune_random_k095_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_prune_l2norm_k09_seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_xvla_spatial_k05_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k085_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k08_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k095_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k07_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_xvla_prune_k08_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k085_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k085_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k08_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k01_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k095_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k095_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k095_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k01_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k01_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k09_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k09_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k05_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k02_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k02_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k09\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k07_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k095\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k03\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k05\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k03_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k03_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k05_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k07_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_xvla_prune_k09_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_random_k05_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_prune_random_k07_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_oft_baseline_k10\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_sc_m128_20k_seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_smart_compress_m16_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m16_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m128_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_openvla_sc_m128_vtconly_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_sc_m128_vtconly_20k_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_openvla_sc_m128_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"analysis_xvla_token_importance\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_openvla_sc_m96_vtconly_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_openvla_sc_m64_vtconly_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_c5_roboflamingo_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_c5_roboflamingo_libero_object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_openvla_sc_m128_lora_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_smart_compress_m32_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m96_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m64_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_random_pruning_sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_openvla_sc_m128_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_baseline_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m16_seed44_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_official_smolvla_prune_k05_spatial_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m96_seed44_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m64_seed44_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32_seed44_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_mlp_adapter_seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_official_smolvla_prune_k05_spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_smolvla_official_baseline_spatial_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_mlp_adapter_seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_mlp_adapter_control\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_smolvla_prune_k05_spatial_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_baseline_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_official_baseline_spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_smolvla_prune_k05_spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_smart_compress_m16_seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_mlp_adapter_control\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m128_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m32_official\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m128_seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_k095\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_k09\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32_libero_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m64_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32_libero_goal\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_baseline_control_prune_k05\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m64_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m32_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m96_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m96_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_smart_compress_m96_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_baseline_control_100k_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_baseline_control_100k_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_official_smolvla_prune_k095\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_official_smolvla_prune_k09\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_acis_k05_supplement_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_acis_k05_supplement_200eps\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_official_smolvla_prune_k05_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_official_smolvla_baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smolvla_random_prune_k095\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_official_smolvla_pruning\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_baseline_control_100k\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_smart_compress_m128\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_pruning_k03_restart\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smolvla_entropy_perlayer\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"inference_latency_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_pruning_k03\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"openvla_entropy_real\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m128\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_smart_compress_m96\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m16\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_pruning_k07\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m96\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smart_compress_m16\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_smart_compress_m32\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m32\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_smart_compress_m64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_full_ft_baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_acis_stage1only_k03\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_pruning_k05\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"geometric_prior_k05_eval\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_openvla_crossmodel_pruning\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_geometric_prior_k09\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_geometric_prior_k07\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_geometric_prior_k05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"libero_fullft_batch64_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"baseline_bypass_object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"action_divergence_v2_clean\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_goal_prune_k05\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"offline_singlestep_action_error\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"offline_singlestep_error_k05\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_spatial_prune_k05\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_merge_k05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_k07_zero_mask\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_true_removal_k05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_stage1only_k09\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_random_prune_k05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train_acis_stage1only_k07\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_stage1only_object_v2_fixed\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_stage1only_spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_stage1_only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_fullft_seed1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_fullft_batch64\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_imm100k_bypass\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_k07_bypass_v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval_k07_bypass_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_imm_k07_object\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_imm_anchor_v7_2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_imm_anchor_v7\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"libero_fullft_seed0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_imm_fullft_k07\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_imm_fullft_seed0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_imm_fullft_100k\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"libero_imm_fullft_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"libero_lora_seed0\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"libero_lora_baseline\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"libero_imm_twostage_v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan_009_token_importance\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_011_acis_overhead\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_008_pruning_sweep_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_005_formal_bound_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_008_pruning_sweep\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"baseline_v6_alpha16\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_imm_v8c_annealing\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_imm_v8b_twostage\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp_imm_anchor_v8_1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_imm_anchor_v8\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_baseline_v5\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp_imm_anchor_v7_1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_imm_anchor_v6\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_imm_anchor_v5\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_baseline_v4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mvp_imm_anchor_v4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_baseline_v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_imm_anchor_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_baseline_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_imm_anchor\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_baseline\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_prune_l2norm_k095_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k09_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k05_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_openvla_prune_l2norm_k03_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_oft_baseline_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}}, \"count\": 343, \"total\": 343, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8909}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T09:15:43.368Z_

<details><summary>↩ Tool result · `toolu_01KBNsinKqg2kshRWQT5Wd9x`</summary>

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
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "3fde323b-8ed3-449b-8bf0-9f76f708c8cf",
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

### Tool result

_source line 17 · 2026-05-22T09:15:43.379Z_

<details><summary>↩ Tool result · `toolu_01N98H21UjQ7fEN76veu178L`</summary>

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
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "69910109-498c-4e39-ace8-dcf31585540f",
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

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
The ssh_read_only blocks pipe characters. Let me use ssh_execute with warn=true for the read-only checks on other servers instead. Also, I need to check the registry results.

From the registry, let me check the three experiments I need to deploy:
1. `eval_pi05_l2norm_k07_object_seed43` - I see `eval_pi05_l2norm_k07_object_seed43` is DONE with conclusion "success", and also `eval_pi05_l2norm_k07_object_seed43_v2` and `eval_pi05_l2norm_k07_object_seed43_v3` are DONE. So this experiment is already DONE!


2. `eval_pi05_l2norm_k05_object_seed43` - Also marked DONE with success.
3. `eval_pi05_random_k09_object_seed43` - Also marked DONE with success.

All three experiments are already completed successfully in the registry, so there's nothing to deploy. I should alert the user to this discrepancy since they asked me to deploy experiments that are already finished.

Let me look for what's actually incomplete. The user mentioned some gaps with object seed 43, and I need to check the alternatives like `eval_pi05_l2norm_k0925_object_seed43` and `eval_pi05_random_k0925_object_seed43` to see their status. I should also scan for any RUNNING experiments in the registry and verify the kill operation worked properly across all servers. I should check what experiments are currently running to get a complete picture before flagging this discrepancy to the user.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "e445f7da-cbbe-4929-8ff5-b422a80709c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiEmKPsibVTiAMJXdYPnnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12884,
      "cache_read_input_tokens": 25875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12884
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

Kill 成功。Registry 检查发现问题——三个目标实验全部已是 DONE/success 状态：

- `eval_pi05_l2norm_k07_object_seed43` → DONE (v3 也 DONE)
- `eval_pi05_l2norm_k05_object_seed43` → DONE  
- `eval_pi05_random_k09_object_seed43` → DONE

备选也已完成：
- `eval_pi05_l2norm_k03_object_seed43` → DONE
- `eval_pi05_random_k0925_object_seed43` → DONE

ssh_read_only 不支持管道，改用 ssh_execute 做去重检查，同时查 RUNNING 状态实验和验证 kill 结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "842ad104-4bf1-48e2-8fa2-67ec8ec4e284",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiEmKPsibVTiAMJXdYPnnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12884,
      "cache_read_input_tokens": 25875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12884
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AkG6sWg21Udjq3VPUBfvdp`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": {
    "status": "RUNNING"
  },
  "fields": [
    "exp_id",
    "status",
    "server",
    "conclusion"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "784dc353-1c04-4d53-abc9-6f6d535edeb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiEmKPsibVTiAMJXdYPnnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12884,
      "cache_read_input_tokens": 25875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12884
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

_source line 21 · 2026-05-22T09:16:08.453Z_

<details><summary>↩ Tool result · `toolu_01AkG6sWg21Udjq3VPUBfvdp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_pi05_random_k03_object_seed43_v4\": {\"status\": \"RUNNING\"}, \"eval_pi05_l2norm_k09_object_seed43\": {\"status\": \"RUNNING\"}, \"eval_pi05_l2norm_k095_object_seed43\": {\"status\": \"RUNNING\"}, \"eval_pi05_random_k05_spatial_seed43\": {\"status\": \"RUNNING\"}, \"eval_pi05_l2norm_k0925_spatial_seed43\": {\"status\": \"RUNNING\"}, \"train_openvla_sc_m64_seed42_v6\": {\"status\": \"RUNNING\"}, \"train_openvla_sc_m96_seed42_v3\": {\"status\": \"RUNNING\"}}, \"count\": 7, \"total\": 7, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9825}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "8ac4df70-3e17-4af0-a4d1-5ba663e2d354",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_pi05_random_k03_object_seed43_v4\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval_pi05_l2norm_k09_object_seed43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval_pi05_l2norm_k095_object_seed43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval_pi05_random_k05_spatial_seed43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval_pi05_l2norm_k0925_spatial_seed43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"train_openvla_sc_m64_seed42_v6\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"train_openvla_sc_m96_seed42_v3\\\": {\\\"status\\\": \\\"RUNNING\\\"}}, \\\"count\\\": 7, \\\"total\\\": 7, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9825}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_pi05_random_k03_object_seed43_v4\": {\"status\": \"RUNNING\"}, \"eval_pi05_l2norm_k09_object_seed43\": {\"status\": \"RUNNING\"}, \"eval_pi05_l2norm_k095_object_seed43\": {\"status\": \"RUNNING\"}, \"eval_pi05_random_k05_spatial_seed43\": {\"status\": \"RUNNING\"}, \"eval_pi05_l2norm_k0925_spatial_seed43\": {\"status\": \"RUNNING\"}, \"train_openvla_sc_m64_seed42_v6\": {\"status\": \"RUNNING\"}, \"train_openvla_sc_m96_seed42_v3\": {\"status\": \"RUNNING\"}}, \"count\": 7, \"total\": 7, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9825}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01LQCgD2GJiVtQByZ2asuWky`</summary>

```json
{
  "server": "westd-27271",
  "command": "ps -p 212585 -o pid,etime,rss,args 2>/dev/null; echo \"---\"; nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader; echo \"---\"; ps aux | grep eval_pi05 | grep -v grep",
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
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "b6749625-c3d0-41af-a7d8-1b0a50ff7cf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiEmKPsibVTiAMJXdYPnnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12884,
      "cache_read_input_tokens": 25875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12884
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

_source line 23 · 2026-05-22T09:16:09.799Z_

<details><summary>↩ Tool result · `toolu_01LQCgD2GJiVtQByZ2asuWky`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID     ELAPSED   RSS COMMAND\\n212585    01:08:31 12254932 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\\n---\\n0, 1 MiB, 97887 MiB, 0 %\\n1, 10564 MiB, 97887 MiB, 32 %\\n---\\nroot     212580  0.0  0.0   4364  2112 ?        S    16:07   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && nohup bash -c 'HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 43 --gpu 0' > /root/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_object_seed43.log 2>&1 & echo PID=\\nroot     212585  383  1.1 78164292 12254932 ?   Rl   16:07 262:39 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "9419a648-dd94-4498-9b0d-7bc9bcde2431",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"   PID     ELAPSED   RSS COMMAND\\\\n212585    01:08:31 12254932 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\\\\n---\\\\n0, 1 MiB, 97887 MiB, 0 %\\\\n1, 10564 MiB, 97887 MiB, 32 %\\\\n---\\\\nroot     212580  0.0  0.0   4364  2112 ?        S    16:07   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && nohup bash -c 'HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 43 --gpu 0' > /root/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_object_seed43.log 2>&1 & echo PID=\\\\nroot     212585  383  1.1 78164292 12254932 ?   Rl   16:07 262:39 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"   PID     ELAPSED   RSS COMMAND\\n212585    01:08:31 12254932 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\\n---\\n0, 1 MiB, 97887 MiB, 0 %\\n1, 10564 MiB, 97887 MiB, 32 %\\n---\\nroot     212580  0.0  0.0   4364  2112 ?        S    16:07   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && nohup bash -c 'HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 43 --gpu 0' > /root/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_object_seed43.log 2>&1 & echo PID=\\nroot     212585  383  1.1 78164292 12254932 ?   Rl   16:07 262:39 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01AaY8rz19JJQZcgM3rnHpYf`</summary>

```json
{
  "server": "westd-38929",
  "command": "ps aux | grep eval_pi05 | grep -v grep",
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
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "e58533c2-a8b0-46c2-b466-d05971e64ed9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiEmKPsibVTiAMJXdYPnnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12884,
      "cache_read_input_tokens": 25875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12884
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

_source line 25 · 2026-05-22T09:16:10.978Z_

<details><summary>↩ Tool result · `toolu_01AaY8rz19JJQZcgM3rnHpYf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"root     708992  378  1.0 64610352 11494112 ?   Rl   15:42 355:01 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0\\nroot     709233  396  1.1 64773916 11741088 ?   Rl   15:42 370:56 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0\\nroot     709369  400  1.0 64326932 11115828 ?   Rl   15:42 374:24 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.3 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0\\nroot     808099  449  1.2 64693072 12842492 ?   Rl   16:40 160:03 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "bd4a52b8-0b6d-4a0d-a294-37a3b2dd1c92",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"root     708992  378  1.0 64610352 11494112 ?   Rl   15:42 355:01 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0\\\\nroot     709233  396  1.1 64773916 11741088 ?   Rl   15:42 370:56 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0\\\\nroot     709369  400  1.0 64326932 11115828 ?   Rl   15:42 374:24 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.3 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0\\\\nroot     808099  449  1.2 64693072 12842492 ?   Rl   16:40 160:03 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.93}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"root     708992  378  1.0 64610352 11494112 ?   Rl   15:42 355:01 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0\\nroot     709233  396  1.1 64773916 11741088 ?   Rl   15:42 370:56 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0\\nroot     709369  400  1.0 64326932 11115828 ?   Rl   15:42 374:24 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.3 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0\\nroot     808099  449  1.2 64693072 12842492 ?   Rl   16:40 160:03 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"
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
Let me summarize the current state:

**westd-27271:**
- GPU 0: 0% util, 1 MiB used → **空闲**
- GPU 1: 32% util, 10564 MiB → PID 212585 running l2norm k095 object seed43 (the one we kept)
- GPU 2 & 3: not shown in nvidia-smi separately but only 2 GPUs listed... Wait, it shows 2 entries (index 0 and 1). But the task says 4 GPUs. Let me re-read.


Actually, looking at the nvidia-smi output more carefully, I'm only seeing indices 0 and 1 listed, which suggests the server might only have 2 GPUs despite the task mentioning 4. Each GPU has about 96GB of memory, so this could be a 2-GPU setup. Looking at the registry, there are seven experiments currently running across the system—four on westd-38929 involving various combinations of l2norm and random methods with different k values and seeds, plus three additional training jobs in the registry including OpenVLA experiments with different configurations.

The three experiments the user wants to deploy are already marked as done in the registry, which means deploying them again doesn't align with the current state. Additionally, westd-38929 only has 2 GPUs available, so I can only run one experiment at a time on GPU 0, not the four that are currently listed. Looking at what's actually missing for object seed43 experiments, I see that random_k05_object_seed43 and random_k07_object_seed43 are already complete, so I need to identify which object seed43 variants still need to be run. Looking at the remaining evaluations, I see several are still running and need to identify what's missing from the full sweep across all ratio and method combinations for object seed43. I'm noticing that `l2norm_k0925_object_seed43` doesn't appear in either the DONE or RUNNING lists, which suggests it might be a genuine gap in the job queue. The user checked the registry about ten minutes ago, so there's a possibility it's been updated since then, or they might have a different view of the current state. The main takeaway is that the machine only has 2 GPUs available with just one currently free, and the three target experiments are already completed—I should report these findings and ask what they'd like to do next.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "b90582e6-1109-4c61-8799-287838bb816e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKT485Fod4nXq8KKZQL7mG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2840,
      "cache_read_input_tokens": 38759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2840
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

发现两个关键问题，暂停部署：

**问题 1：westd-27271 只有 2 个 GPU，不是 4 个**

nvidia-smi 输出：
```
GPU 0: 1 MiB / 97887 MiB, 0% → 空闲
GPU 1: 10564 MiB / 97887 MiB, 32% → PID 212585 (l2norm_k095_object_seed43)
```

只能部署 1 个实验到 GPU 0。

**问题 2：目标实验全部已 DONE/success**

| 实验 | Registry 状态 |
|------|--------------|
| l2norm_k07_object_seed43 | DONE (success) — v2, v3 也 DONE |
| l2norm_k05_object_seed43 | DONE (success) |
| random_k09_object_seed43 | DONE (success) |

备选同样已完成：
- l2norm_k03_object_seed43 → DONE
- random_k0925_object_seed43 → DONE

**当前 RUNNING 实验（registry）：**
- eval_pi05_l2norm_k095_object_seed43（westd-27271 GPU 1）
- eval_pi05_l2norm_k09_object_seed43
- eval_pi05_random_k03_object_seed43_v4
- eval_pi05_random_k05_spatial_seed43
- eval_pi05_l2norm_k0925_spatial_seed43
- 2 个 training jobs

**westd-38929 在跑 4 个实验（无冲突）：**
- l2norm_k05_spatial_seed43
- random_k03_spatial_seed43
- l2norm_k03_spatial_seed43
- random_k03_object_seed43 (v4)

**可能的真实缺口：** `l2norm_k0925_object_seed43` 不在 DONE 也不在 RUNNING 中。需要确认是否需要跑这个？

请指示：GPU 0 应该部署什么实验？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "uuid": "45b62d2e-1690-4b17-b0fb-60f83659cd77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKT485Fod4nXq8KKZQL7mG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2840,
      "cache_read_input_tokens": 38759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2840
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

### Task result

_source line 28_

发现两个关键问题，暂停部署：

**问题 1：westd-27271 只有 2 个 GPU，不是 4 个**

nvidia-smi 输出：
```
GPU 0: 1 MiB / 97887 MiB, 0% → 空闲
GPU 1: 10564 MiB / 97887 MiB, 32% → PID 212585 (l2norm_k095_object_seed43)
```

只能部署 1 个实验到 GPU 0。

**问题 2：目标实验全部已 DONE/success**

| 实验 | Registry 状态 |
|------|--------------|
| l2norm_k07_object_seed43 | DONE (success) — v2, v3 也 DONE |
| l2norm_k05_object_seed43 | DONE (success) |
| random_k09_object_seed43 | DONE (success) |

备选同样已完成：
- l2norm_k03_object_seed43 → DONE
- random_k0925_object_seed43 → DONE

**当前 RUNNING 实验（registry）：**
- eval_pi05_l2norm_k095_object_seed43（westd-27271 GPU 1）
- eval_pi05_l2norm_k09_object_seed43
- eval_pi05_random_k03_object_seed43_v4
- eval_pi05_random_k05_spatial_seed43
- eval_pi05_l2norm_k0925_spatial_seed43
- 2 个 training jobs

**westd-38929 在跑 4 个实验（无冲突）：**
- l2norm_k05_spatial_seed43
- random_k03_spatial_seed43
- l2norm_k03_spatial_seed43
- random_k03_object_seed43 (v4)

**可能的真实缺口：** `l2norm_k0925_object_seed43` 不在 DONE 也不在 RUNNING 中。需要确认是否需要跑这个？

请指示：GPU 0 应该部署什么实验？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 85423,
  "duration_api_ms": 85569,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "f0cad418-0a05-4d0d-a52f-4d0f4a162064",
  "total_cost_usd": 0.35704149999999996,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 29758,
    "cache_read_input_tokens": 100780,
    "output_tokens": 4736,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29758,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2491,
        "cache_read_input_tokens": 38759,
        "cache_creation_input_tokens": 2840,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2840
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2154,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002229,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 4736,
      "cacheReadInputTokens": 100780,
      "cacheCreationInputTokens": 29758,
      "webSearchRequests": 0,
      "costUSD": 0.3548125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a91ca4ab-745a-4e7f-aadd-0f7c8d69a42c"
}
```

</details>

---
