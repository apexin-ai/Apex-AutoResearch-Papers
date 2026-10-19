# harvest bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 76
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/workers/worker_harvest_bjb1-32546_20260524T032326.log`
- **Structured JSON:** [`6cf3741ffaf50238a736.json`](../../sessions/6c/6cf3741ffaf50238a736.json)

## Before a recorded user message

76 recorded events

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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
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
  "uuid": "9f26fb86-9759-4e99-a810-1cf4cd44472c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779610200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f5a5852a-fa1f-4675-9328-7103b8a292c9",
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by loading the necessary MCP tools, then execute the steps as outlined.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "931498e7-124d-4180-995f-cd05f0770bd7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYRysQNxbwHy6yeHe1G8zk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12080,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12080
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

_source line 5_

先加载需要的工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "07ddfb78-74c2-4cde-bf64-47e44a74b3cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYRysQNxbwHy6yeHe1G8zk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12080,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12080
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UrTcQE2ho76rCYZQPdFYzG`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "efe9b89d-1a6c-492b-a0ec-4afe7b0a6cc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYRysQNxbwHy6yeHe1G8zk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12080,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12080
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

_source line 7 · 2026-05-24T03:23:42.213Z_

<details><summary>↩ Tool result · `toolu_01UrTcQE2ho76rCYZQPdFYzG`</summary>

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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "2b4c7b82-2bc5-4d7e-902f-93a06d6876f9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
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
Now let me execute steps 1, 2, and 6 in parallel (GPU scan, find JSON files, disk check), plus read the registry to understand current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "97ade9c4-d002-47aa-8cfd-27a22e34a5ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms7mwyw1JwPnC2BvM8AKPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1754,
      "cache_read_input_tokens": 23921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1754
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

开始并行扫描 GPU 状态、查找 JSON 文件、检查磁盘、读取 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "f8a3a1ee-e3cc-4d88-9522-24c88cdaadfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms7mwyw1JwPnC2BvM8AKPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1754,
      "cache_read_input_tokens": 23921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1754
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Jqg7dW5Aikc1G581RX1Ah4`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "b51a2374-9a4c-4a12-81a9-789665ef1ebf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms7mwyw1JwPnC2BvM8AKPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1754,
      "cache_read_input_tokens": 23921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1754
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

_source line 11 · 2026-05-24T03:23:48.931Z_

<details><summary>↩ Tool result · `toolu_01Jqg7dW5Aikc1G581RX1Ah4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 22 %, 6289 MiB, 24564 MiB\\n1, 33 %, 9012 MiB, 24564 MiB\\n2, 46 %, 8360 MiB, 24564 MiB\\n3, 24 %, 5844 MiB, 24564 MiB\\n4, 0 %, 2 MiB, 24564 MiB\\n5, 0 %, 2 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "2750257a-549c-4ed1-a9b2-b261da1ce05d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 22 %, 6289 MiB, 24564 MiB\\\\n1, 33 %, 9012 MiB, 24564 MiB\\\\n2, 46 %, 8360 MiB, 24564 MiB\\\\n3, 24 %, 5844 MiB, 24564 MiB\\\\n4, 0 %, 2 MiB, 24564 MiB\\\\n5, 0 %, 2 MiB, 24564 MiB\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.17}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 22 %, 6289 MiB, 24564 MiB\\n1, 33 %, 9012 MiB, 24564 MiB\\n2, 46 %, 8360 MiB, 24564 MiB\\n3, 24 %, 5844 MiB, 24564 MiB\\n4, 0 %, 2 MiB, 24564 MiB\\n5, 0 %, 2 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JN7C4vLTZtSQCxUTWLP72z`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name '*.json' -mtime -5",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "a5db69c3-9224-4e38-86d3-4649e11e5753",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms7mwyw1JwPnC2BvM8AKPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1754,
      "cache_read_input_tokens": 23921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1754
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

_source line 13 · 2026-05-24T03:23:49.686Z_

<details><summary>↩ Tool result · `toolu_01JN7C4vLTZtSQCxUTWLP72z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\\n/root/acr-vla-conformal-refine\\n\\n... [截断: 输出过长，省略 4610 字符] ...\\n\\nrefinement/logs/eval_obs_only_object_norm01_seed77.json\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm003_seed63_r3.json\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm003_seed76.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_acr_vla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.1_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_tau0.074855_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.2_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.35_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed46.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "bbf9bf6e-dd3a-4707-989e-0412e66de8fd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed50.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\\\\n/root/acr-vla-conformal-refine\\\\n\\\\n... [截断: 输出过长，省略 4610 字符] ...\\\\n\\\\nrefinement/logs/eval_obs_only_object_norm01_seed77.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm003_seed63_r3.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm003_seed76.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_acr_vla_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.1_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_tau0.074855_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.2_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.35_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed46.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\\n/root/acr-vla-conformal-refine\\n\\n... [截断: 输出过长，省略 4610 字符] ...\\n\\nrefinement/logs/eval_obs_only_object_norm01_seed77.json\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm003_seed63_r3.json\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm003_seed76.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_acr_vla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.1_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_tau0.074855_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.2_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.35_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed46.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PaYKhwuZVGoTMhWo52XAHh`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "df -h / /root/autodl-tmp",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "6217b2cf-cc93-4a7f-bcc3-5c286b75fc6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms7mwyw1JwPnC2BvM8AKPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1754,
      "cache_read_input_tokens": 23921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1754
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

_source line 15 · 2026-05-24T03:23:50.498Z_

<details><summary>↩ Tool result · `toolu_01PaYKhwuZVGoTMhWo52XAHh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\noverlay          30G   10G   21G  34% /\\n/dev/md0        250G   68G  183G  28% /root/autodl-tmp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "6b303ded-6cac-4057-bcf4-5346a0fba53e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Filesystem      Size  Used Avail Use% Mounted on\\\\noverlay          30G   10G   21G  34% /\\\\n/dev/md0        250G   68G  183G  28% /root/autodl-tmp\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\noverlay          30G   10G   21G  34% /\\n/dev/md0        250G   68G  183G  28% /root/autodl-tmp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01B2R5emoX1gztkWpaSabfnn`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux ls",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "0031fc17-22ef-40ea-bd39-06a2435052fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms7mwyw1JwPnC2BvM8AKPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1754,
      "cache_read_input_tokens": 23921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1754
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

_source line 17 · 2026-05-24T03:23:50.608Z_

<details><summary>↩ Tool result · `toolu_01B2R5emoX1gztkWpaSabfnn`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "bfb9e297-2746-421a-903e-520664d78a3f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015CrzEa9ELQHSZfF32ekrCB`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps aux --no-headers -o pid,pcpu,pmem,etime,args --sort=-pcpu",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "6d5c8e46-2754-4c9d-8ce0-a12831ff5f4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms7mwyw1JwPnC2BvM8AKPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1754,
      "cache_read_input_tokens": 23921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1754
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

_source line 19 · 2026-05-24T03:23:52.442Z_

<details><summary>↩ Tool result · `toolu_015CrzEa9ELQHSZfF32ekrCB`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "4b39d40f-a1be-4916-ac80-e3fc5d855eb9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"error: conflicting format options\\\\n\\\\nUsage:\\\\n ps [options]\\\\n\\\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\\\n for additional help text.\\\\n\\\\nFor more details see ps(1).\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01L8tYkdUorRPnP5MajcRVBN`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "RUNNING"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "ab4ac5c0-e2af-4ffe-b665-1b0b941b4057",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms7mwyw1JwPnC2BvM8AKPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1754,
      "cache_read_input_tokens": 23921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1754
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

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WK5phqzbtb7Vy5BM2bFTst`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /tmp/eval_*.log",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "98acc2c9-5117-4157-a25e-945c511b87ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms7mwyw1JwPnC2BvM8AKPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1754,
      "cache_read_input_tokens": 23921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1754
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

_source line 22 · 2026-05-24T03:23:55.733Z_

<details><summary>↩ Tool result · `toolu_01L8tYkdUorRPnP5MajcRVBN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-vla-only-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:32:53.028Z\", \"updated_at\": \"2026-05-24T00:33:27.913Z\", \"hypothesis\": \"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5851}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "59e17ce0-c404-4761-9223-ad77519caa4e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-long-vla-only-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T00:32:53.028Z\\\", \\\"updated_at\\\": \\\"2026-05-24T00:33:27.913Z\\\", \\\"hypothesis\\\": \\\"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\\\"}}, \\\"count\\\": 1, \\\"total\\\": 1, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.5851}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-vla-only-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:32:53.028Z\", \"updated_at\": \"2026-05-24T00:33:27.913Z\", \"hypothesis\": \"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5851}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T03:23:56.094Z_

<details><summary>↩ Tool result · `toolu_01WK5phqzbtb7Vy5BM2bFTst`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root     1281 May 23 07:23 /tmp/eval_crm_goal_seed42.log\\n-rw-r--r-- 1 root root     1281 May 23 07:23 /tmp/eval_crm_goal_seed43.log\\n-rw-r--r-- 1 root root     1281 May 23 07:23 /tmp/eval_crm_goal_seed44.log\\n-rw-r--r-- 1 root root     6377 May 24 06:30 /tmp/eval_crm_obj_s46.log\\n-rw-r--r-- 1 root root      821 May 22 06:33 /tmp/eval_dryrun.log\\n-rw-r--r-- 1 root root     1035 May 22 06:35 /tmp/eval_dryrun2.log\\n-rw-r--r-- 1 root root     5631 May 24 06:06 /tmp/eval_goal_adapt_s45.log\\n-rw-r--r-- 1 root root     5265 May 24 00:34 /tmp/eval_goal_wrapper_s44_r2.log\\n-rw-r--r-- 1 root root     7951 May 24 08:46 /tmp/eval_long_adapt_s45.log\\n-rw-r--r-- 1 root root     5002 May 24 11:20 /tmp/eval_long_adapt_s46.log\\n-rw-r--r-- 1 root root     7950 May 24 03:38 /tmp/eval_long_adapt_tau025_s43.log\\n-rw-r--r-- 1 root root     7826 May 24 03:32 /tmp/eval_long_crm_norm005_s43.log\\n-rw-r--r-- 1 root root     7832 May 24 08:51 /tmp/eval_long_crm_s45.log\\n-rw-r--r-- 1 root root     4972 May 24 11:21 /tmp/eval_long_crm_s46.log\\n-rw-r--r-- 1 root root     7579 May 24 03:32 /tmp/eval_long_k2mean_s43.log\\n-rw-r--r-- 1 root root     7645 May 24 03:14 /tmp/eval_long_reconvla_s43.log\\n-rw-r--r-- 1 root root     7726 May 24 08:55 /tmp/eval_long_reconvla_s45.log\\n-rw-r--r-- 1 root root     5116 May 24 11:23 /tmp/eval_long_reconvla_s46.log\\n-rw-r--r-- 1 root root     7584 May 24 03:20 /tmp/eval_long_vla_only_s44.log\\n-rw-r--r-- 1 root root     7584 May 24 08:43 /tmp/eval_long_vla_s45.log\\n-rw-r--r-- 1 root root  5203936 May 22 21:24 /tmp/eval_smolvla_goal.log\\n-rw-r--r-- 1 root root   632348 May 23 05:12 /tmp/eval_smolvla_goal_seed43_v3.log\\n-rw-r--r-- 1 root root   663158 May 23 05:17 /tmp/eval_smolvla_goal_seed44_v3.log\\n-rw-r--r-- 1 root root 12940332 May 22 21:48 /tmp/eval_smolvla_long.log\\n-rw-r--r-- 1 root root  1966232 May 23 02:11 /tmp/eval_smolvla_long_seed42.log\\n-rw-r--r-- 1 root root  1967352 May 23 02:12 /tmp/eval_smolvla_long_seed43.log\\n-rw-r--r-- 1 root root  1922488 May 23 02:12 /tmp/eval_smolvla_long_seed44.log\\n-rw-r--r-- 1 root root   618349 May 23 04:35 /tmp/eval_smolvla_object_seed43_v2.log\\n-rw-r--r-- 1 root root   617033 May 23 04:35 /tmp/eval_smolvla_object_seed44_v2.log\\n-rw-r--r-- 1 root root  6334951 May 22 21:32 /tmp/eval_smolvla_spatial.log\\n-rw-r--r-- 1 root root   627385 May 23 05:11 /tmp/eval_smolvla_spatial_seed43_v3.log\\n-rw-r--r-- 1 root root     7159 May 24 09:22 /tmp/eval_spatial_k2mean_s46.log\\n-rw-r--r-- 1 root root     1492 May 23 07:27 /tmp/eval_vla_goal_seed42.log\\n-rw-r--r-- 1 root root     1653 May 23 07:30 /tmp/eval_vla_goal_seed43.log\\n-rw-r--r-- 1 root root     1569 May 23 07:30 /tmp/eval_vla_goal_seed44.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "b270b69c-07d2-4daa-8f32-976c5107e1c8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root     1281 May 23 07:23 /tmp/eval_crm_goal_seed42.log\\\\n-rw-r--r-- 1 root root     1281 May 23 07:23 /tmp/eval_crm_goal_seed43.log\\\\n-rw-r--r-- 1 root root     1281 May 23 07:23 /tmp/eval_crm_goal_seed44.log\\\\n-rw-r--r-- 1 root root     6377 May 24 06:30 /tmp/eval_crm_obj_s46.log\\\\n-rw-r--r-- 1 root root      821 May 22 06:33 /tmp/eval_dryrun.log\\\\n-rw-r--r-- 1 root root     1035 May 22 06:35 /tmp/eval_dryrun2.log\\\\n-rw-r--r-- 1 root root     5631 May 24 06:06 /tmp/eval_goal_adapt_s45.log\\\\n-rw-r--r-- 1 root root     5265 May 24 00:34 /tmp/eval_goal_wrapper_s44_r2.log\\\\n-rw-r--r-- 1 root root     7951 May 24 08:46 /tmp/eval_long_adapt_s45.log\\\\n-rw-r--r-- 1 root root     5002 May 24 11:20 /tmp/eval_long_adapt_s46.log\\\\n-rw-r--r-- 1 root root     7950 May 24 03:38 /tmp/eval_long_adapt_tau025_s43.log\\\\n-rw-r--r-- 1 root root     7826 May 24 03:32 /tmp/eval_long_crm_norm005_s43.log\\\\n-rw-r--r-- 1 root root     7832 May 24 08:51 /tmp/eval_long_crm_s45.log\\\\n-rw-r--r-- 1 root root     4972 May 24 11:21 /tmp/eval_long_crm_s46.log\\\\n-rw-r--r-- 1 root root     7579 May 24 03:32 /tmp/eval_long_k2mean_s43.log\\\\n-rw-r--r-- 1 root root     7645 May 24 03:14 /tmp/eval_long_reconvla_s43.log\\\\n-rw-r--r-- 1 root root     7726 May 24 08:55 /tmp/eval_long_reconvla_s45.log\\\\n-rw-r--r-- 1 root root     5116 May 24 11:23 /tmp/eval_long_reconvla_s46.log\\\\n-rw-r--r-- 1 root root     7584 May 24 03:20 /tmp/eval_long_vla_only_s44.log\\\\n-rw-r--r-- 1 root root     7584 May 24 08:43 /tmp/eval_long_vla_s45.log\\\\n-rw-r--r-- 1 root root  5203936 May 22 21:24 /tmp/eval_smolvla_goal.log\\\\n-rw-r--r-- 1 root root   632348 May 23 05:12 /tmp/eval_smolvla_goal_seed43_v3.log\\\\n-rw-r--r-- 1 root root   663158 May 23 05:17 /tmp/eval_smolvla_goal_seed44_v3.log\\\\n-rw-r--r-- 1 root root 12940332 May 22 21:48 /tmp/eval_smolvla_long.log\\\\n-rw-r--r-- 1 root root  1966232 May 23 02:11 /tmp/eval_smolvla_long_seed42.log\\\\n-rw-r--r-- 1 root root  1967352 May 23 02:12 /tmp/eval_smolvla_long_seed43.log\\\\n-rw-r--r-- 1 root root  1922488 May 23 02:12 /tmp/eval_smolvla_long_seed44.log\\\\n-rw-r--r-- 1 root root   618349 May 23 04:35 /tmp/eval_smolvla_object_seed43_v2.log\\\\n-rw-r--r-- 1 root root   617033 May 23 04:35 /tmp/eval_smolvla_object_seed44_v2.log\\\\n-rw-r--r-- 1 root root  6334951 May 22 21:32 /tmp/eval_smolvla_spatial.log\\\\n-rw-r--r-- 1 root root   627385 May 23 05:11 /tmp/eval_smolvla_spatial_seed43_v3.log\\\\n-rw-r--r-- 1 root root     7159 May 24 09:22 /tmp/eval_spatial_k2mean_s46.log\\\\n-rw-r--r-- 1 root root     1492 May 23 07:27 /tmp/eval_vla_goal_seed42.log\\\\n-rw-r--r-- 1 root root     1653 May 23 07:30 /tmp/eval_vla_goal_seed43.log\\\\n-rw-r--r-- 1 root root     1569 May 23 07:30 /tmp/eval_vla_goal_seed44.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root     1281 May 23 07:23 /tmp/eval_crm_goal_seed42.log\\n-rw-r--r-- 1 root root     1281 May 23 07:23 /tmp/eval_crm_goal_seed43.log\\n-rw-r--r-- 1 root root     1281 May 23 07:23 /tmp/eval_crm_goal_seed44.log\\n-rw-r--r-- 1 root root     6377 May 24 06:30 /tmp/eval_crm_obj_s46.log\\n-rw-r--r-- 1 root root      821 May 22 06:33 /tmp/eval_dryrun.log\\n-rw-r--r-- 1 root root     1035 May 22 06:35 /tmp/eval_dryrun2.log\\n-rw-r--r-- 1 root root     5631 May 24 06:06 /tmp/eval_goal_adapt_s45.log\\n-rw-r--r-- 1 root root     5265 May 24 00:34 /tmp/eval_goal_wrapper_s44_r2.log\\n-rw-r--r-- 1 root root     7951 May 24 08:46 /tmp/eval_long_adapt_s45.log\\n-rw-r--r-- 1 root root     5002 May 24 11:20 /tmp/eval_long_adapt_s46.log\\n-rw-r--r-- 1 root root     7950 May 24 03:38 /tmp/eval_long_adapt_tau025_s43.log\\n-rw-r--r-- 1 root root     7826 May 24 03:32 /tmp/eval_long_crm_norm005_s43.log\\n-rw-r--r-- 1 root root     7832 May 24 08:51 /tmp/eval_long_crm_s45.log\\n-rw-r--r-- 1 root root     4972 May 24 11:21 /tmp/eval_long_crm_s46.log\\n-rw-r--r-- 1 root root     7579 May 24 03:32 /tmp/eval_long_k2mean_s43.log\\n-rw-r--r-- 1 root root     7645 May 24 03:14 /tmp/eval_long_reconvla_s43.log\\n-rw-r--r-- 1 root root     7726 May 24 08:55 /tmp/eval_long_reconvla_s45.log\\n-rw-r--r-- 1 root root     5116 May 24 11:23 /tmp/eval_long_reconvla_s46.log\\n-rw-r--r-- 1 root root     7584 May 24 03:20 /tmp/eval_long_vla_only_s44.log\\n-rw-r--r-- 1 root root     7584 May 24 08:43 /tmp/eval_long_vla_s45.log\\n-rw-r--r-- 1 root root  5203936 May 22 21:24 /tmp/eval_smolvla_goal.log\\n-rw-r--r-- 1 root root   632348 May 23 05:12 /tmp/eval_smolvla_goal_seed43_v3.log\\n-rw-r--r-- 1 root root   663158 May 23 05:17 /tmp/eval_smolvla_goal_seed44_v3.log\\n-rw-r--r-- 1 root root 12940332 May 22 21:48 /tmp/eval_smolvla_long.log\\n-rw-r--r-- 1 root root  1966232 May 23 02:11 /tmp/eval_smolvla_long_seed42.log\\n-rw-r--r-- 1 root root  1967352 May 23 02:12 /tmp/eval_smolvla_long_seed43.log\\n-rw-r--r-- 1 root root  1922488 May 23 02:12 /tmp/eval_smolvla_long_seed44.log\\n-rw-r--r-- 1 root root   618349 May 23 04:35 /tmp/eval_smolvla_object_seed43_v2.log\\n-rw-r--r-- 1 root root   617033 May 23 04:35 /tmp/eval_smolvla_object_seed44_v2.log\\n-rw-r--r-- 1 root root  6334951 May 22 21:32 /tmp/eval_smolvla_spatial.log\\n-rw-r--r-- 1 root root   627385 May 23 05:11 /tmp/eval_smolvla_spatial_seed43_v3.log\\n-rw-r--r-- 1 root root     7159 May 24 09:22 /tmp/eval_spatial_k2mean_s46.log\\n-rw-r--r-- 1 root root     1492 May 23 07:27 /tmp/eval_vla_goal_seed42.log\\n-rw-r--r-- 1 root root     1653 May 23 07:30 /tmp/eval_vla_goal_seed43.log\\n-rw-r--r-- 1 root root     1569 May 23 07:30 /tmp/eval_vla_goal_seed44.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
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
Good. I found the key JSON files. Let me now focus on the specific ones mentioned in the task:

From the find output, I can see these target files exist:
1. `eval_spatial_k2mean_seed46.json` → eval-supp-spatial-k2mean-s46
2. `eval_object_reconvla_seed45.json` → eval-supp-reconvla-obj-s45
3. `eval_long_reconvla_seed45.json` → eval-supp-long-reconvla-s45


4. `eval_long_vla_only_seed45.json` → eval-supp-long-vla-only-s45
5. `eval_long_crm_obs_only_norm0.05_seed45.json` → eval-supp-long-crm-norm005-s45
6. `eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json` → eval-supp-long-adapt-tau025-s45

I also spotted `eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json` in the results.

Now I'm seeing additional files with different seeds and configurations—object variants with seed46, goal variants with seed44, and several others. I'm noticing that `eval_long_k2mean_seed45.json` isn't showing up in the logs directory even though there's a log file for it, so I need to investigate that more carefully. Let me also check what processes are currently running and then start reading all the target JSON files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "97d9a088-e431-4e5f-b133-72288b9aac94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGELyLpfWUactdPNPs1kRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7022,
      "cache_read_input_tokens": 25675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7022
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

找到大量 JSON 文件。GPU 0-3 在用，4-5 空闲。现在读取任务重点关注的 JSON 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "82745694-8262-49aa-a919-80e384094171",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGELyLpfWUactdPNPs1kRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7022,
      "cache_read_input_tokens": 25675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7022
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MZFpNvfq1y6NNmRW5CcJdN`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed46.json",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "a771d769-0842-4a37-b5b8-7e8bfb2a01c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGELyLpfWUactdPNPs1kRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7022,
      "cache_read_input_tokens": 25675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7022
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

_source line 27 · 2026-05-24T03:24:17.161Z_

<details><summary>↩ Tool result · `toolu_01MZFpNvfq1y6NNmRW5CcJdN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"mean\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.8,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "8f914d74-6589-4678-a2a7-e2774be666a7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"mean\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"spatial\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.8,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"mean\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.8,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KiQBv2DzLQ3Mptj4SWa6jK`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "cb9e05ad-357e-4813-b208-cd9c3c58d1f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGELyLpfWUactdPNPs1kRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7022,
      "cache_read_input_tokens": 25675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7022
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

_source line 29 · 2026-05-24T03:24:18.110Z_

<details><summary>↩ Tool result · `toolu_01KiQBv2DzLQ3Mptj4SWa6jK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"reconvla\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.78,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "704ddb73-6d89-4bc6-a495-c95683e076f9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"reconvla\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.78,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.65,\\\\n      \\\\\\\"successes\\\\\\\": 13,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"reconvla\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.78,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018x24wkzfCFuxeuU2ogP9Jn`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed45.json",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "1cf903c8-5c1b-41d1-937c-64e8ab2d27c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGELyLpfWUactdPNPs1kRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7022,
      "cache_read_input_tokens": 25675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7022
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

_source line 31 · 2026-05-24T03:24:18.611Z_

<details><summary>↩ Tool result · `toolu_018x24wkzfCFuxeuU2ogP9Jn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"reconvla\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.59,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.25,\\n      \\\"successes\\\": 5,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.35,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.35,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.15,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "1a2d6d13-600b-47ef-b17d-cddea852e0c9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"reconvla\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"long\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.59,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.25,\\\\n      \\\\\\\"successes\\\\\\\": 5,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.35,\\\\n      \\\\\\\"successes\\\\\\\": 7,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.35,\\\\n      \\\\\\\"successes\\\\\\\": 7,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.6,\\\\n      \\\\\\\"successes\\\\\\\": 12,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.15,\\\\n      \\\\\\\"successes\\\\\\\": 3,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"reconvla\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.59,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.25,\\n      \\\"successes\\\": 5,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.35,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.35,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.15,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PgrcLEEu81Ci67MunJGhv2`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "2d4f0a2e-6a17-4723-a1f3-a3afc39198b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGELyLpfWUactdPNPs1kRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7022,
      "cache_read_input_tokens": 25675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7022
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

_source line 33 · 2026-05-24T03:24:19.591Z_

<details><summary>↩ Tool result · `toolu_01PgrcLEEu81Ci67MunJGhv2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.575,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.35,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.35,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.05,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "9fa3d467-83a2-45f0-9b38-2ee0bc8012a8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"long\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.575,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n      \\\\\\\"successes\\\\\\\": 4,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.65,\\\\n      \\\\\\\"successes\\\\\\\": 13,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.35,\\\\n      \\\\\\\"successes\\\\\\\": 7,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.35,\\\\n      \\\\\\\"successes\\\\\\\": 7,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.6,\\\\n      \\\\\\\"successes\\\\\\\": 12,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.05,\\\\n      \\\\\\\"successes\\\\\\\": 1,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.575,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.35,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.35,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.05,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VVZycGuZADPnqAR1A8dpYJ`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed45.json",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "fc3f9931-6b9a-4df1-8202-d9715c2f1a67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGELyLpfWUactdPNPs1kRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7022,
      "cache_read_input_tokens": 25675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7022
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

_source line 35 · 2026-05-24T03:24:20.442Z_

<details><summary>↩ Tool result · `toolu_01VVZycGuZADPnqAR1A8dpYJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.605,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.55,\\n      \\\"successes\\\": 11,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 6,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "04a6f0ee-33f9-4e77-83cb-68dd8e7946a6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"crm_obs_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"long\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.605,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n      \\\\\\\"successes\\\\\\\": 4,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.55,\\\\n      \\\\\\\"successes\\\\\\\": 11,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n      \\\\\\\"successes\\\\\\\": 6,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.6,\\\\n      \\\\\\\"successes\\\\\\\": 12,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n      \\\\\\\"successes\\\\\\\": 2,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.5,\\\\n      \\\\\\\"successes\\\\\\\": 10,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.605,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.55,\\n      \\\"successes\\\": 11,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 6,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016CeJH49PwgdUxt4DqDNt3n`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "a48ddf0d-f01d-4910-be60-34c2c7ec5047",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGELyLpfWUactdPNPs1kRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7022,
      "cache_read_input_tokens": 25675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7022
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

_source line 37 · 2026-05-24T03:24:21.379Z_

<details><summary>↩ Tool result · `toolu_016CeJH49PwgdUxt4DqDNt3n`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.6,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.15,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.45,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.35,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.05,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_stats\\\": {\\n    \\\"mean_uncertainty\\\": 0.12093888436455003,\\n    \\\"trigger_rate\\\": 0.03358183054988686,\\n    \\\"tau\\\": 0.25,\\n    \\\"total_steps\\\": 72033,\\n    \\\"crm_applied_steps\\\": 2419\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "c0ef7007-890b-4ee2-a59f-918f76aea95a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"adaptive_conformal_crm\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"long\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.6,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.15,\\\\n      \\\\\\\"successes\\\\\\\": 3,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.45,\\\\n      \\\\\\\"successes\\\\\\\": 9,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.35,\\\\n      \\\\\\\"successes\\\\\\\": 7,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.6,\\\\n      \\\\\\\"successes\\\\\\\": 12,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.05,\\\\n      \\\\\\\"successes\\\\\\\": 1,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  },\\\\n  \\\\\\\"adaptive_stats\\\\\\\": {\\\\n    \\\\\\\"mean_uncertainty\\\\\\\": 0.12093888436455003,\\\\n    \\\\\\\"trigger_rate\\\\\\\": 0.03358183054988686,\\\\n    \\\\\\\"tau\\\\\\\": 0.25,\\\\n    \\\\\\\"total_steps\\\\\\\": 72033,\\\\n    \\\\\\\"crm_applied_steps\\\\\\\": 2419\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.6,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.15,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.45,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.35,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.05,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_stats\\\": {\\n    \\\"mean_uncertainty\\\": 0.12093888436455003,\\n    \\\"trigger_rate\\\": 0.03358183054988686,\\n    \\\"tau\\\": 0.25,\\n    \\\"total_steps\\\": 72033,\\n    \\\"crm_applied_steps\\\": 2419\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013J4kq7Gw12ekrWT2ACYai6`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name '*k2mean*seed45*'",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "94ea95cb-cd94-40d2-9006-23249956ea37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGELyLpfWUactdPNPs1kRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7022,
      "cache_read_input_tokens": 25675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7022
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

_source line 39 · 2026-05-24T03:24:22.427Z_

<details><summary>↩ Tool result · `toolu_013J4kq7Gw12ekrWT2ACYai6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "dd337862-3bb6-4ed7-a80b-5db92d553cf3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AXXDaQTjcJtHueWAPGDtNh`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "e9cedb64-8da3-4742-99d4-f9d0b313a106",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGELyLpfWUactdPNPs1kRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7022,
      "cache_read_input_tokens": 25675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7022
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

_source line 41 · 2026-05-24T03:24:23.321Z_

<details><summary>↩ Tool result · `toolu_01AXXDaQTjcJtHueWAPGDtNh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.81,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_stats\\\": {\\n    \\\"mean_uncertainty\\\": 0.14933589608835302,\\n    \\\"trigger_rate\\\": 0.09386823000102253,\\n    \\\"tau\\\": 0.25,\\n    \\\"total_steps\\\": 29339,\\n    \\\"crm_applied_steps\\\": 2754\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "208c4d8d-e2b9-42cf-94a3-7726622d92dc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"adaptive_conformal_crm\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"goal\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.81,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_wine_bottle_on_top_of_the_cabinet\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_top_of_the_cabinet\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_cream_cheese_in_the_bowl\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.5,\\\\n      \\\\\\\"successes\\\\\\\": 10,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"turn_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_wine_bottle_on_the_rack\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  },\\\\n  \\\\\\\"adaptive_stats\\\\\\\": {\\\\n    \\\\\\\"mean_uncertainty\\\\\\\": 0.14933589608835302,\\\\n    \\\\\\\"trigger_rate\\\\\\\": 0.09386823000102253,\\\\n    \\\\\\\"tau\\\\\\\": 0.25,\\\\n    \\\\\\\"total_steps\\\\\\\": 29339,\\\\n    \\\\\\\"crm_applied_steps\\\\\\\": 2754\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.81,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_stats\\\": {\\n    \\\"mean_uncertainty\\\": 0.14933589608835302,\\n    \\\"trigger_rate\\\": 0.09386823000102253,\\n    \\\"tau\\\": 0.25,\\n    \\\"total_steps\\\": 29339,\\n    \\\"crm_applied_steps\\\": 2754\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01W6L4LvjecSNnGT4R4foxq7`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed46.json",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "4db6cd57-b401-415c-83e2-39f757ca0092",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGELyLpfWUactdPNPs1kRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7022,
      "cache_read_input_tokens": 25675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7022
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

_source line 43 · 2026-05-24T03:24:24.305Z_

<details><summary>↩ Tool result · `toolu_01W6L4LvjecSNnGT4R4foxq7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.795,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "d623db9c-67c5-4d1a-9814-ad37f3ae0809",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"crm_obs_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.795,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.795,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016rj255fGCeLdNtCuLgC1pt`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "687acbbc-2b9f-4121-9458-c61d04da9cd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGELyLpfWUactdPNPs1kRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7022,
      "cache_read_input_tokens": 25675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7022
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

_source line 45 · 2026-05-24T03:24:24.994Z_

<details><summary>↩ Tool result · `toolu_016rj255fGCeLdNtCuLgC1pt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.79,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.55,\\n      \\\"successes\\\": 11,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "a1b006ed-cae8-4e91-9bbc-d18bc4e88f59",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.79,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.55,\\\\n      \\\\\\\"successes\\\\\\\": 11,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.79,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.55,\\n      \\\"successes\\\": 11,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
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
I've collected the key JSON files. Let me also check for some additional files that were mentioned in the task, and also check for any running processes. Let me also look for additional recent JSONs that might be from the supplementary experiments. Let me also read some more recent ones.

Let me also check for:
- long_k2mean_seed45 - not found (find returned empty)
- Also check for additional new JSONs from the latest batch

Let me also check for new JSONs from the latest round of experiments. Looking at the /tmp logs, I can see active evaluations happening for seed46 variants (long_adapt_s46, long_crm_s46, long_reconvla_s46). Let me check those.


Now I need to verify the current registry state for these experiments to understand what needs to be updated, then locate the additional result files from the recent batches including the CRM variants with different normalization and conformal prediction parameters across seeds 43 and 44. I'm checking the s45 seed results across the long evaluation variants—VLA-only, CRM, Adaptive all have their JSONs, but k2mean_seed45 is missing. Let me scan through the other recent JSON files to see what else might be available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "46dc56b7-4c0a-4b2a-8a44-5dc27eeb78d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Qew1X9rdMfwHq6HTPx2TQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11792,
      "cache_read_input_tokens": 32697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11792
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

所有关键 JSON 都已读取。k2mean_seed45 不存在。现在检查 registry 中这些实验的当前状态，再进行更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "50b63d88-8220-4317-b6dc-7d8450400b3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Qew1X9rdMfwHq6HTPx2TQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11792,
      "cache_read_input_tokens": 32697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11792
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01HnUVHLQrrKq9zdZa9nTAkM`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "status",
    "conclusion",
    "metrics"
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "50451256-a5ce-4a98-bf6d-57242253b212",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Qew1X9rdMfwHq6HTPx2TQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11792,
      "cache_read_input_tokens": 32697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11792
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01SBrcCnViV3W92L9Su7tPkm`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "FAILED"
  },
  "fields": [
    "status",
    "conclusion",
    "metrics",
    "hypothesis"
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "55cd1bc6-e8fb-4f31-aa98-0314a6339cda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Qew1X9rdMfwHq6HTPx2TQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11792,
      "cache_read_input_tokens": 32697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11792
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

_source line 50 · 2026-05-24T03:24:56.668Z_

<details><summary>↩ Tool result · `toolu_01HnUVHLQrrKq9zdZa9nTAkM`</summary>

```text
Error: result (187,243 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/602e10fd-b61b-43df-9ff5-2ac62d7d0b87/tool-results/mcp-agent-ml-research-read_registry-1779593096635.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/602e10fd-b61b-43df-9ff5-2ac62d7d0b87/tool-results/mcp-agent-ml-research-read_registry-1779593096635.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/602e10fd-b61b-43df-9ff5-2ac62d7d0b87/tool-results/mcp-agent-ml-research-read_registry-1779593096635.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "3973fec6-736f-461b-8bf5-9ce73cb4ee27",
  "tool_use_result": {
    "content": "Error: result (187,243 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/602e10fd-b61b-43df-9ff5-2ac62d7d0b87/tool-results/mcp-agent-ml-research-read_registry-1779593096635.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/602e10fd-b61b-43df-9ff5-2ac62d7d0b87/tool-results/mcp-agent-ml-research-read_registry-1779593096635.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/602e10fd-b61b-43df-9ff5-2ac62d7d0b87/tool-results/mcp-agent-ml-research-read_registry-1779593096635.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"trigger_rate\": 0.0909, \"tau\": 0.25, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 20, \"mean_unc\": 0.1863}}, \"eval-supp-spatial-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80.5, \"successes\": 161, \"total\": 200}}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 19.9, \"mean_unc\": 0.1846}}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-reconvla-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-long-crm-norm005-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.605, \"successes\": 121, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.6, \"successes\": 120, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.575, \"successes\": 115, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.77, \"successes\": 154, \"total\": 200}}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.78, \"successes\": 156, \"total\": 200, \"per_task\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.7}}}, \"eval-supp-spatial-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"successes\": 159, \"total\": 200}}, \"eval-supp-goal-k2mean-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.81, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.6, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.55, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.78}, \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-crm-obj-s46\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.795, \"per_task\": {\"alphabet_soup\": 0.8, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.7, \"tomato_sauce\": 0.75, \"butter\": 0.75, \"milk\": 0.85, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.9}}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"SR\": 0.545, \"successes\": 109, \"total\": 200}}, \"eval-supp-long-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.57, \"successes\": 114, \"total\": 200}}, \"eval-supp-goal-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.855}}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.835}}, \"eval-supp-crm-norm005-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.795}}, \"eval-supp-goal-crm-norm005-s45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.765}}, \"eval-supp-reconvla-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-supp-goal-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.094, \"mean_unc\": 0.1493}}, \"eval-supp-long-crm-norm005-s44\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.565}, \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s44\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.56, \"trigger_rate\": 0.049}, \"conclusion\": \"negative\"}, \"eval-supp-k2mean-obj-s46\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.765}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-obj-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.775}, \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.76}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s46\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.775}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-k2mean-s42\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.57}, \"conclusion\": \"negative\"}, \"eval-supp-obj-vla-only-s46\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.79}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.565}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s43\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.56}, \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s43\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.59}, \"conclusion\": \"negative\"}, \"eval-supp-long-crm-norm005-s43\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.545}, \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s43\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.58, \"trigger_rate\": 0.045}, \"conclusion\": \"negative\"}, \"eval-supp-obj-adapt-tau025-s45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.565}, \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.59, \"trigger_rate\": 0.039, \"tau\": 0.25, \"crm_applied_steps\": 2785, \"total_steps\": 71980}, \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.565}, \"conclusion\": \"negative\"}, \"eval-ablation-tau040-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.835, \"trigger_rate\": 0.012, \"tau\": 0.4, \"crm_applied_steps\": 346, \"total_steps\": 28165}, \"conclusion\": \"negative\"}, \"eval-ablation-tau015-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.85, \"trigger_rate\": 0.339, \"tau\": 0.15, \"crm_applied_steps\": 9590, \"total_steps\": 28273}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.75, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.8, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.55, \"milk\": 0.7, \"chocolate_pudding\": 0.75, \"orange_juice\": 0.95}}, \"conclusion\": \"success\"}, \"eval-ablation-tau010-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.81, \"trigger_rate\": 0.739, \"tau\": 0.1, \"crm_applied_steps\": 22170, \"total_steps\": 29984}, \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.76, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.7, \"salad_dressing\": 0.7, \"bbq_sauce\": 0.95, \"ketchup\": 0.9, \"tomato_sauce\": 0.7, \"butter\": 0.75, \"milk\": 0.6, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.95}}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.785, \"successes\": 157, \"total\": 200, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.95, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.8, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.7}}, \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.85, \"successes\": 170, \"total\": 200, \"per_task\": {\"open_middle_drawer\": 0.85, \"put_bowl_stove\": 0.95, \"wine_bottle_cabinet\": 0.85, \"open_top_drawer_bowl\": 0.7, \"bowl_on_cabinet\": 0.9, \"push_plate_stove\": 0.9, \"cream_cheese_bowl\": 0.65, \"turn_on_stove\": 1, \"bowl_on_plate\": 0.95, \"wine_bottle_rack\": 0.75}}}, \"eval-supp-k2mean-spatial-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.79, \"successes\": 158, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"LOST - JSON overwritten by k2mean-goal-s44 (same output filename). Experiment completed exit_code=0 at 2026-05-23T13:35:37Z but result file was overwritten 3min later.\"}, \"conclusion\": \"failed\"}, \"eval-supp-k2mean-goal-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"drawer\": 0.85, \"bowl_stove\": 1, \"wine_cabinet\": 0.8, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.95, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.75}}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.75, \"trigger_rate\": 0.0364, \"mean_uncertainty\": 0.11, \"crm_applied_steps\": 1310, \"total_steps\": 35990, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.75, \"salad_dressing\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.65, \"milk\": 0.7, \"chocolate\": 0.75, \"orange_juice\": 0.85}}, \"conclusion\": \"negative\"}, \"eval-supp-crm-norm005-obj-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.74, \"per_task\": {\"alphabet_soup\": 0.6, \"cream_cheese\": 0.6, \"salad_dressing\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.8, \"tomato\": 0.7, \"butter\": 0.65, \"milk\": 0.6, \"chocolate\": 0.9, \"orange_juice\": 0.95}}, \"conclusion\": \"negative\"}, \"eval-supp-goal-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.825, \"per_task\": {\"drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.9, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.58, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.25, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0.65, \"KITCHEN_SCENE3_stove_moka_pot\": 1, \"KITCHEN_SCENE4_black_bowl_drawer\": 1, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.4, \"STUDY_SCENE1_book_caddy\": 0.9, \"LIVING_ROOM_SCENE6_mug_pudding\": 0.3, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0.55, \"KITCHEN_SCENE8_moka_pots_stove\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.75}}, \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.805, \"total_rollouts\": 200, \"total_successes\": 161, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.81, 0.81, 0.805], \"mean\": 0.8083, \"std\": 0.0029}}, \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.77, \"total_rollouts\": 200, \"total_successes\": 154}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.835, \"total_rollouts\": 200, \"total_successes\": 167, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.855, 0.82, 0.835], \"mean\": 0.8367, \"std\": 0.0176}}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.78, \"total_successes\": 156, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0.85, \"cream_cheese\": 0.85, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.7, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.9}}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.855, \"n_tasks\": 10, \"n_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 1, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.65, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-goal-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.865, \"trigger_rate\": 0.0677, \"crm_applied_steps\": 1870, \"total_steps\": 27642}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.785}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-goal-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.845, \"trigger_rate\": 0.088, \"crm_applied_steps\": 2509, \"total_steps\": 28500}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.82}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.775, \"trigger_rate\": 0.0367, \"crm_applied_steps\": 1312, \"total_steps\": 35796}, \"conclusion\": \"negative\"}, \"eval-supp-goal-reconvla-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_episodes\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.65, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.55, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.95, \"put_the_wine_bottle_on_the_rack\": 0.85}}, \"conclusion\": \"negative\"}, \"eval-supp-k2mean-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.78, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_episodes\": 200, \"per_task\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.75, \"next_to_plate\": 0.7, \"on_wooden_cabinet\": 0.85}}, \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.795, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task\": {\"between_plate_and_ramekin\": 1, \"table_center\": 1, \"next_to_ramekin\": 0.95, \"next_to_cookie_box\": 0.95, \"on_cookie_box\": 0.9, \"on_wooden_cabinet\": 0.85, \"on_stove\": 0.8, \"next_to_plate\": 0.8, \"top_drawer_wooden_cabinet\": 0.7, \"on_ramekin\": 0}, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.8, 0.815, 0.795], \"mean\": 0.803, \"std\": 0.01}}}, \"eval-supp-reconvla-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.85}}}, \"eval-supp-k2mean-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"total_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.55, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.45, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.95, \"put_the_wine_bottle_on_the_rack\": 0.85}}}, \"eval-supp-k2mean-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"total_successes\": 159, \"total_rollouts\": 200, \"mode\": \"vla_only\", \"K\": 2, \"baseline_mode\": \"mean\", \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"bbq_sauce\": 90, \"ketchup\": 95, \"tomato_sauce\": 85, \"butter\": 60, \"milk\": 70, \"chocolate_pudding\": 70, \"orange_juice\": 95}}}, \"eval-supp-goal-adapt-tau025-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 84, \"total_rollouts\": 200, \"total_successes\": 168, \"trigger_rate\": 8.3, \"mean_unc\": 0.1448, \"per_task\": {\"open_middle_drawer_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"put_bowl_on_stove\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"put_wine_bottle_on_cabinet\": {\"sr\": 80, \"success\": 16, \"total\": 20}, \"open_top_drawer_put_bowl\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"put_bowl_on_top_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"push_plate_to_stove\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"put_cream_cheese_in_bowl\": {\"sr\": 60, \"success\": 12, \"total\": 20}, \"turn_on_stove\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"put_bowl_on_plate\": {\"sr\": 90, \"success\": 18, \"total\": 20}, \"put_wine_bottle_on_rack\": {\"sr\": 80, \"success\": 16, \"total\": 20}}}, \"conclusion\": \"success\"}, \"eval-supp-goal-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 85.5, \"total_successes\": 171, \"total_episodes\": 200, \"per_task\": {\"middle_drawer\": 85, \"bowl_stove\": 100, \"wine_bottle_cabinet\": 95, \"top_drawer_bowl\": 70, \"bowl_cabinet\": 95, \"plate_stove\": 95, \"cream_cheese_bowl\": 50, \"stove\": 95, \"bowl_plate\": 95, \"wine_bottle_rack\": 75}}}, \"eval-supp-goal-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r6\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.005669, \"epochs\": 50, \"final_train_loss\": 0.009731, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/\"}}, \"eval-goal-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200}}, \"eval-supp-obj-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.035, \"mean_unc\": 0.109, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 2}}, \"eval-supp-k2mean-spatial-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 81.5, \"total_success\": 163, \"total_rollouts\": 200, \"per_task\": {\"bowl_between_plate_ramekin\": 95, \"bowl_next_to_ramekin\": 95, \"bowl_from_table_center\": 100, \"bowl_on_cookie_box\": 100, \"bowl_in_top_drawer\": 70, \"bowl_on_ramekin\": 0, \"bowl_next_to_cookie_box\": 95, \"bowl_on_stove\": 80, \"bowl_next_to_plate\": 85, \"bowl_on_wooden_cabinet\": 95}}, \"conclusion\": \"negative\"}, \"eval-supp-crm-norm005-spatial-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 78.5, \"total_rollouts\": 200, \"total_successes\": 157, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"next_to_ramekin\": {\"sr\": 90, \"success\": 18, \"total\": 20}, \"from_table_center\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_cookie_box\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"in_top_drawer_wooden_cabinet\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_ramekin\": {\"sr\": 0, \"success\": 0, \"total\": 20}, \"next_to_cookie_box\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_stove\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"next_to_plate\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_wooden_cabinet\": {\"sr\": 80, \"success\": 16, \"total\": 20}}, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [80, 81, 78.5], \"mean\": 79.8, \"std\": 1.3}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 80.5, \"total_successes\": 161, \"total_rollouts\": 200, \"trigger_rate\": 20, \"mean_unc\": 0.1881, \"conformal_threshold\": 0.25, \"max_correction_norm\": 0.2, \"mode\": \"adaptive_conformal_crm\", \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin\": {\"sr\": 90, \"successes\": 18, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_ramekin\": {\"sr\": 95, \"successes\": 19, \"rollouts\": 20}, \"pick_up_the_black_bowl_from_table_center\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_cookie_box\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet\": {\"sr\": 65, \"successes\": 13, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_ramekin\": {\"sr\": 0, \"successes\": 0, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_cookie_box\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_stove\": {\"sr\": 80, \"successes\": 16, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_plate\": {\"sr\": 80, \"successes\": 16, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_wooden_cabinet\": {\"sr\": 95, \"successes\": 19, \"rollouts\": 20}}}, \"conclusion\": \"success\"}, \"eval-supp-reconvla-k2-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"total_rollouts\": 200, \"total_successes\": 160, \"per_task\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 100, \"from_table_center\": 100, \"on_cookie_box\": 95, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 95, \"on_stove\": 75, \"next_to_plate\": 80, \"on_wooden_cabinet\": 85}}}, \"eval-supp-adapt-tau025-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 80, \"trigger_rate\": 19.4, \"mean_unc\": 0.1845, \"total_rollouts\": 200, \"total_successes\": 160, \"per_task\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 95, \"from_table_center\": 95, \"on_cookie_box\": 100, \"in_top_drawer_wooden_cabinet\": 70, \"on_ramekin\": 0, \"next_to_cookie_box\": 100, \"on_stove\": 80, \"next_to_plate\": 85, \"on_wooden_cabinet\": 80}}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 81, \"total_rollouts\": 200, \"total_successes\": 162, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"next_to_ramekin\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"from_table_center\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_cookie_box\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"in_top_drawer_wooden_cabinet\": {\"sr\": 75, \"success\": 15, \"total\": 20}, \"on_ramekin\": {\"sr\": 0, \"success\": 0, \"total\": 20}, \"next_to_cookie_box\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_stove\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"next_to_plate\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_wooden_cabinet\": {\"sr\": 95, \"success\": 19, \"total\": 20}}}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-adapt-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 77.5, \"total_successes\": 155, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 80, \"cream_cheese\": 90, \"salad_dressing\": 70, \"bbq_sauce\": 85, \"ketchup\": 70, \"tomato_sauce\": 75, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 80, \"orange_juice\": 95}, \"mean_unc\": 0.1104, \"trigger_rate\": 0.702}, \"conclusion\": \"negative\"}, \"eval-object-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 77.5, \"total_successes\": 155, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 90, \"ketchup\": 90, \"tomato_sauce\": 80, \"butter\": 75, \"milk\": 65, \"chocolate_pudding\": 65, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s43-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 77, \"total_successes\": 154, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 85, \"ketchup\": 80, \"tomato_sauce\": 85, \"butter\": 60, \"milk\": 75, \"chocolate_pudding\": 75, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 85, \"cream_cheese\": 75, \"salad_dressing\": 85, \"bbq_sauce\": 85, \"ketchup\": 90, \"tomato_sauce\": 75, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 70, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"bbq_sauce\": 95, \"ketchup\": 90, \"tomato_sauce\": 80, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 75, \"orange_juice\": 90}}}, \"eval-supp-obj-crm005-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.77, \"n_success\": 154, \"n_total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"conformal_threshold\": 0.074855, \"K\": 10, \"seed\": 42, \"per_task_sr\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.9, \"ketchup\": 0.8, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.75, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 80, \"n_success\": 160, \"n_total\": 200, \"trigger_rate\": 12.17, \"mean_unc\": 0.1873, \"conformal_threshold\": 0.35, \"max_correction_norm\": 0.2, \"crm_applied_steps\": 3474, \"total_steps\": 28549, \"per_task_sr\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 100, \"from_table_center\": 90, \"on_cookie_box\": 95, \"in_top_drawer\": 70, \"on_ramekin\": 0, \"next_to_cookie_box\": 95, \"on_stove\": 85, \"next_to_plate\": 85, \"on_wooden_cabinet\": 85}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 80.5, \"n_success\": 161, \"n_total\": 200, \"trigger_rate\": 40.7, \"mean_unc\": 0.1852, \"conformal_threshold\": 0.15, \"max_correction_norm\": 0.2, \"per_task_sr\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 100, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 90, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 75, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 90, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 80, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 85}}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm02-spatial-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 79, \"n_success\": 158, \"n_total\": 200, \"per_task_sr\": {\"between_plate_and_ramekin\": 100, \"next_to_ramekin\": 90, \"from_table_center\": 95, \"on_cookie_box\": 95, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 100, \"on_stove\": 95, \"next_to_plate\": 75, \"on_wooden_cabinet\": 65}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 82, \"n_success\": 164, \"n_total\": 200, \"trigger_rate\": 19.4, \"mean_unc\": 0.1847, \"per_task_sr\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 95, \"from_table_center\": 100, \"on_cookie_box\": 100, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 90, \"on_stove\": 90, \"next_to_plate\": 90, \"on_wooden_cabinet\": 85}}, \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed55\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-features-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-adapt-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau035-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r5-resumed\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau035-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-3dir-adaptive-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"trigger_rate\": 0.918, \"tau\": 0.074855, \"mean_uncertainty\": 0.183, \"crm_applied_steps\": 26589, \"total_steps\": 28955, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 1, \"from_table_center\": 1, \"on_cookie_box\": 0.9, \"in_top_drawer\": 0.8, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.8}}}, \"eval-3dir-norm03-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 73.9, \"successes\": 133, \"total\": 180, \"n_tasks_complete\": 9, \"n_tasks_total\": 10, \"n_rollouts\": 20, \"note\": \"killed at T10 rollout 10/20, 9/10 tasks complete\", \"per_task_sr\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 0.85, \"from_table_center\": 1, \"on_cookie_box\": 0.9, \"in_top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0.8, \"next_to_plate\": 0.55, \"on_wooden_cabinet\": \"partial_5/10\"}}}, \"eval-3dir-reconvla-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"successes\": 158, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 0.95, \"from_table_center\": 1, \"on_cookie_box\": 1, \"in_top_drawer\": 0.65, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.75, \"next_to_plate\": 0.7, \"on_wooden_cabinet\": 0.85}}}, \"eval-3dir-norm01-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 79, \"successes\": 158, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"from_table_center\": 1, \"on_cookie_box\": 1, \"in_top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.75}}}, \"eval-3dir-norm005-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 1, \"from_table_center\": 1, \"on_cookie_box\": 0.95, \"in_top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.85, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.8}}}, \"precompute-pi05-goal-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-spatial-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-object-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-object-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r5\": {\"status\": \"DONE\", \"metrics\": {\"val_loss\": 0.006075, \"epochs_completed\": 32, \"epochs_target\": 50, \"train_loss_final\": 0.010489, \"best_epoch\": 32, \"crash_epoch\": 33, \"crash_count\": 2}, \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-long-2048\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-lerobot-goal-seed44-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 82, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 54.5, \"n_episodes\": 200}}, \"train-crm-smolvla-3suite-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.005878, \"final_train_loss\": 0.00969, \"final_val_loss\": 0.00588, \"epochs_completed\": 50, \"total_params\": 327198, \"data_samples\": 77835, \"best_epoch\": 50}}, \"eval-smolvla-lerobot-goal-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pc_success\": 65, \"n_episodes\": 200, \"eval_s\": 841}}, \"eval-smolvla-lerobot-object-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pc_success\": 66.5, \"n_episodes\": 200, \"eval_s\": 857.4}}, \"eval-smolvla-lerobot-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.6, \"n_episodes\": 200, \"n_tasks\": 10, \"per_task_sr\": [0.75, 0.65, 0.75, 0.75, 0.5, 0, 0.9, 0.7, 0.4, 0.6]}}, \"precompute-smolvla-long-wrapper-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 49.5, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 53.5, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 49.5, \"n_episodes\": 200}}, \"train-crm-unified-4suite-r4\": {\"status\": \"DONE\", \"metrics\": {\"epochs_completed\": 13, \"current_epoch\": 14, \"current_batch\": \"2700/6316\", \"total_epochs\": 50, \"last_train_loss\": 0.012, \"checkpoint_latest\": \"checkpoint_epoch0013.pt\", \"checked_at\": \"2026-05-22T01:21Z\", \"note\": \"CRON false alarm - process still running (PID 322367)\"}, \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-long-seed42-r4-rerun\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.94, \"successes\": 188, \"total\": 200, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.95, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 1, \"KITCHEN_SCENE3_stove_moka_pot\": 1, \"KITCHEN_SCENE4_black_bowl_drawer\": 1, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.9, \"STUDY_SCENE1_book_in_caddy\": 0.95, \"LIVING_ROOM_SCENE6_mug_pudding\": 1, \"LIVING_ROOM_SCENE1_soup_cream_cheese\": 0.9, \"KITCHEN_SCENE8_both_moka_pots\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave\": 0.9}}, \"conclusion\": \"success\"}, \"eval-pi05-crm-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed43-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed44-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed42-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed44-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed43-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}}, \"precompute-smolvla-long-k2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train-crm-unified-4suite-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-bjb2-28827\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-long-bjb2-28827\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.955}}, \"eval-pi05-vla-only-long-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.955}}, \"eval-pi05-vla-only-goal-seed44-r4\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.975, \"successes\": 195, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-seed43-r4\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-openvla-oft-official-object\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-object-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 98.5, \"total_successes\": 197, \"total_episodes\": 200}}, \"eval-pi05-vla-only-object-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 99.5, \"total_successes\": 199, \"total_episodes\": 200}}, \"eval-smolvla-lerobot-official-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42-r4\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 100, \"total_success\": 200, \"total_rollouts\": 200, \"n_action_steps\": 10, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 100, \"bbq_sauce\": 100, \"ketchup\": 100, \"tomato_sauce\": 100, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 100, \"orange_juice\": 100}}, \"conclusion\": \"success\"}, \"train-crm-unified-4suite\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"completed_epochs\": 4, \"target_epochs\": 50, \"exit_code\": 124, \"failure_reason\": \"timeout (EXIT_CODE=124) — killed after 4/50 epochs (~2.3 GPU hours)\", \"best_val_loss\": 0.009633, \"best_epoch\": 4, \"training_curve\": [{\"epoch\": 1, \"train_loss\": 0.019467, \"val_loss\": 0.010801, \"lr\": \"9.99e-04\"}, {\"epoch\": 2, \"train_loss\": 0.018024, \"val_loss\": 0.010438, \"lr\": \"9.96e-04\"}, {\"epoch\": 3, \"train_loss\": 0.017237, \"val_loss\": 0.009901, \"lr\": \"9.91e-04\"}, {\"epoch\": 4, \"train_loss\": 0.01663, \"val_loss\": 0.009633, \"lr\": \"9.84e-04\"}]}}, \"precompute-smolvla-long-bjb1-32546-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-long-bjb1-32546\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-loss-perdof-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"milk\": 5, \"chocolate_pudding\": 5, \"orange_juice\": 5}}, \"conclusion\": \"negative\"}, \"eval-loss-combined-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"avg_success_rate\": 9, \"total_successes\": 18, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 10, \"salad_dressing\": 10, \"bbq_sauce\": 15, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 5, \"milk\": 10, \"chocolate_pudding\": 25, \"orange_juice\": 10}}, \"conclusion\": \"negative\"}, \"eval-loss-conformal-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 6, \"total_successes\": 12, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 10, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 0, \"milk\": 10, \"chocolate_pudding\": 20, \"orange_juice\": 10}}, \"conclusion\": \"negative\"}, \"eval-loss-mse-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"avg_success_rate\": 7, \"total_successes\": 14, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 10, \"ketchup\": 5, \"tomato_sauce\": 15, \"butter\": 10, \"milk\": 15, \"chocolate_pudding\": 5, \"orange_juice\": 0}}, \"conclusion\": \"negative\"}, \"eval-openvla-oft-object-baseline-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": \"all 10 tasks 0.0%\", \"n_rollouts\": 20, \"total_episodes\": 200}}, \"precompute-smolvla-long-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 136090, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5, \"obs_features_shape\": [136090, 960], \"k_samples_shape\": [136090, 10, 5, 6], \"expert_actions_shape\": [136090, 5, 6], \"total_time_sec\": 8021, \"speed\": \"0.06s/sample\"}}, \"crm-loss-combined\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.005302, \"final_train_loss\": 0.004481, \"best_epoch\": 48, \"epochs\": 50, \"vs_mse\": \"2.5x worse\", \"vs_perdof\": \"43x worse\", \"dof_weight_range\": [0.0107, 3.7318]}, \"conclusion\": \"negative\"}, \"crm-loss-conformal\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.013343, \"final_train_loss\": 0.016046, \"epochs\": 50, \"vs_mse\": \"6.4x worse\"}, \"conclusion\": \"negative\"}, \"precompute-smolvla-goal-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 61728, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5}}, \"crm-loss-perdof\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.000124, \"final_train_loss\": 0.000141, \"best_epoch\": 50, \"total_epochs\": 50, \"dof_weight_min\": 0.0107, \"dof_weight_max\": 3.7318, \"mse_baseline_val_loss\": 0.00208, \"conformal_guided_val_loss\": 0.013343, \"samples\": 14570, \"crm_params\": 337438}, \"conclusion\": \"success\"}, \"crm-loss-mse-baseline\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.00208, \"final_train_loss\": 0.004038, \"best_epoch\": 50, \"total_epochs\": 50, \"initial_val_loss\": 0.008373, \"exit_code\": 0}, \"conclusion\": \"success\"}, \"eval-smolvla-acr-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-long-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-long-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-acr-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"RuntimeError: state_dict shape mismatch in CRM checkpoint. input_mean/input_std: [990] vs [1030], net.0.weight: [256,990] vs [256,1030]. CRM checkpoint (crm_v3_norm/obs_only/crm_best.pt) was trained with obs_dim=960 but model now expects obs_dim=1000.\"}}, \"eval-smolvla-acr-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-train-pi05-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"val_loss\": 0.006138, \"best_epoch\": 50, \"total_epochs\": 50}}, \"crm-train-pi05-object-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"val_loss\": 0.004018, \"best_epoch\": 50, \"total_epochs\": 50}}, \"crm-train-pi05-spatial-full\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-train-pi05-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-pi05-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.85, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed43-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.83, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed42-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.845, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.81, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.815, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.82, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-spatial-obs-only-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.34, \"per_task_sr\": [0.9, 0.9, 0, 0.4, 0.1, 0, 0.8, 0, 0.3, 0], \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10}}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.17}}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\"}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"sr_pct\": \"19.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1468, \"trigger_rate\": 0.838}}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12}, \"conclusion\": \"success\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"total_rollouts\": 100, \"total_successes\": 35, \"mean_uncertainty\": 0.2619, \"trigger_rate\": 0.98}}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"sr_pct\": \"20.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1448, \"trigger_rate\": 0.832}}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"total_rollouts\": 100, \"total_successes\": 34, \"mean_uncertainty\": 0.2679, \"trigger_rate\": 0.976}}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"sr_pct\": \"36.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.2661, \"trigger_rate\": 0.978}}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1457, \"trigger_rate\": 0.84}}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"source\": \"harvested from bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm01_seed60.json\"}}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed75\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed51-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11}}, \"eval-obs-only-object-norm01-seed52-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed65\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed61\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed64-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed63\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed62\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed52-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"total_successes\": 11}}, \"eval-obs-only-object-norm005-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed55-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-openvla-crm-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0, \"sr_pct\": \"0.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"sr_pct\": \"15.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.1, \"sr_pct\": \"10.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.33, \"sr_pct\": \"33.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-seed54\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.14, \"mean_l2\": 0, \"avg_k\": 1, \"fast_path_pct\": 0.12, \"n_rollouts\": 10}}, \"eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.11, \"n_rollouts\": 100, \"fast_path_pct\": 12.5, \"avg_k\": 1}}, \"eval-perdof-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.1, \"n_rollouts\": 100, \"per_task\": [0, 0, 1, 1, 0, 1, 1, 0, 4, 2]}}, \"eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"avg_K\": 1, \"adaptive_trigger_rate\": 0, \"crm_trigger_rate\": 0.8795, \"unc_threshold\": 0.42}, \"conclusion\": \"negative\"}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"successes\": 35, \"total_rollouts\": 100}}, \"train-crm-openvla-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.07726, \"final_train_loss\": 0.234989, \"epochs_completed\": 50}}, \"openvla-precompute-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_files\": 74507, \"obs_dim\": 4096, \"cache_size_gb\": 6, \"multi_scale_layers\": [7, 15, 23, 31]}}, \"eval-random-selection-object-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"tasks_evaluated\": 10, \"rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 10}}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"seed\": 49, \"K\": 10, \"max_correction_norm\": 0.2}}, \"eval-random-selection-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 7}}, \"eval-obs-only-spatial-norm02-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 33}}, \"eval-k5-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 17}}, \"eval-random-selection-spatial-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 26}}, \"eval-random-selection-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.28, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed42-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed44-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 10, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.26, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.7, \"stove\": 0, \"next_to_plate\": 0.2, \"wooden_cabinet\": 0}}}, \"eval-random-selection-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.35, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed42\": {\"status\": \"DONE\", \"metrics\": {\"status_note\": \"INCOMPLETE - only 2/10 tasks evaluated before process terminated\", \"partial_per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 1}, \"tasks_completed\": 2, \"tasks_total\": 10}, \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-norm02-seed49\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.32, \"sr_pct\": \"32%\", \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"on_cookie_box\": 0.3, \"top_drawer_cabinet\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.36, \"avg_K\": 3.56, \"fast_path_ratio\": 0.805, \"adaptive_trigger_rate\": 0.195, \"total_rollouts\": 100, \"successes\": 36, \"total_steps\": 23123, \"fast_steps\": 18615, \"full_steps\": 4508, \"threshold\": 0.12587, \"mean_l2_distance\": 0.09, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 0.8, \"successes\": 8, \"total\": 10}, \"next_to_ramekin\": {\"sr\": 1, \"successes\": 10, \"total\": 10}, \"from_table_center\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"on_cookie_box\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"in_top_drawer\": {\"sr\": 0.1, \"successes\": 1, \"total\": 10}, \"on_ramekin\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_cookie_box\": {\"sr\": 0.9, \"successes\": 9, \"total\": 10}, \"on_stove\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_plate\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"on_wooden_cabinet\": {\"sr\": 0, \"successes\": 0, \"total\": 10}}}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed50\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}, \"total_rollouts\": 100, \"total_successes\": 13, \"seed\": 50, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\"}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"successes\": 11, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.1, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.4, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 69, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-spatial-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed44-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-k1-object-seed43-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-k1-object-seed42-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.07, \"total\": 100, \"successes\": 7, \"benchmark\": \"object\", \"mode\": \"crm_perdof\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.11, \"total\": 100, \"successes\": 11, \"benchmark\": \"object\", \"mode\": \"reconvla\"}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.73, \"total\": 100, \"successes\": 73, \"benchmark\": \"goal\", \"mode\": \"vla_only\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.33, \"total\": 100, \"successes\": 33, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\"}, \"conclusion\": \"success\"}, \"eval-latency-profiling-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pipeline_latency_ms\": 247, \"crm_latency_ms\": 0.27}}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 33, \"avg_k\": 5.054, \"fast_path_pct\": 61.8, \"mean_l2\": 0.092, \"total_rollouts\": 100, \"threshold\": 0.098735}}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 66, \"total_rollouts\": 100, \"per_task_sr\": {\"open_middle_drawer\": 40, \"put_bowl_on_stove\": 90, \"put_wine_bottle_on_cabinet\": 50, \"open_top_drawer_put_bowl\": 40, \"put_bowl_on_cabinet\": 80, \"push_plate_to_stove\": 90, \"put_cream_cheese_in_bowl\": 20, \"turn_on_stove\": 100, \"put_bowl_on_plate\": 100, \"put_wine_bottle_on_rack\": 50}}}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 32, \"avg_k\": 7.693, \"fast_path_pct\": 28.8, \"mean_l2\": 0.0896, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 70, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 40, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"total_successes\": 16, \"total_rollouts\": 100, \"seed\": 49, \"benchmark\": \"LIBERO-Object\", \"K\": 10, \"mode\": \"reconvla (argmin baseline)\", \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.3, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}}}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.68, \"per_task\": {\"open_middle_drawer\": 0.7, \"bowl_on_stove\": 0.9, \"wine_on_cabinet\": 0.4, \"bowl_in_drawer\": 0.3, \"bowl_on_cabinet\": 0.8, \"plate_to_stove\": 0.8, \"cream_cheese_in_bowl\": 0.4, \"turn_on_stove\": 1, \"bowl_on_plate\": 1, \"wine_on_rack\": 0.5}}}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32, \"avg_K\": 3.586, \"fast_path_pct\": 80.17, \"mean_l2\": 0.0905, \"adaptive_trigger_rate\": 0.198, \"threshold\": 0.12587, \"total_steps\": 23797, \"fast_steps\": 19079, \"full_steps\": 4718}}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.31, \"avg_K\": 3.5, \"fast_path_pct\": 80.6, \"mean_l2\": 0.0907, \"threshold\": 0.12587, \"total_rollouts\": 100, \"total_successes\": 31, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14, \"total_rollouts\": 100, \"total_successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"updated_aggregate\": {\"mean_sr\": 16.4, \"std_sr\": 2, \"n_seeds\": 7, \"prior\": \"16.8±1.8% (n=6)\", \"delta_vs_vla_baseline\": \"+5.5pp\"}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"incomplete\": true, \"tasks_completed\": 2, \"tasks_total\": 10, \"partial_results\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9}, \"failure_reason\": \"Process exited after 2/10 tasks; no JSON output generated; likely OOM or early termination\"}}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-adaptive-k-spatial-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.4, \"fast_path_ratio\": 0.45, \"adaptive_trigger_rate\": 0.55, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 30, \"avg_K\": 6.324, \"fast_path_pct\": 45.95, \"mean_l2\": 0.0903, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.33, \"avg_K\": 7.65, \"fast_path_pct\": 29.4, \"mean_l2_distance\": 0.0892, \"threshold\": 0.054959, \"total_steps\": 23410, \"fast_steps\": 6873, \"full_steps\": 16537, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"negative\"}, \"eval-adaptive-k-spatial-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 30, \"avg_k\": 7.6, \"fast_path_pct\": 29.5, \"mean_l2\": 0.089, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 60, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 30, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}}, \"eval-adaptive-k-spatial-p75-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 34, \"total_rollouts\": 100, \"adaptive_stats\": {\"fast_path_pct\": 62.2, \"avg_k\": 5, \"mean_l2\": 0.0911}, \"per_task\": {\"bowl_between_plate_ramekin\": 80, \"bowl_next_to_ramekin\": 100, \"bowl_from_table_center\": 0, \"bowl_on_cookie_box\": 40, \"bowl_in_top_drawer\": 0, \"bowl_on_ramekin\": 0, \"bowl_next_to_cookie_box\": 90, \"bowl_on_stove\": 0, \"bowl_next_to_plate\": 30, \"bowl_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.18, \"total_successes\": 18, \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}, \"comparison\": {\"k10_reference\": \"16.8±1.8%\", \"k20_this\": \"18.0%\", \"delta\": \"+1.2pp\", \"note\": \"within K=10 error bars, marginal improvement\"}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed49-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.16, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.9, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_mug_pudding\": 0.2, \"LIVING_ROOM_SCENE1_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.31, \"avg_k\": 5.02, \"fast_path_ratio\": 0.622, \"mean_l2\": 0.0909, \"adaptive_trigger_rate\": 0.378, \"total_steps\": 23914, \"fast_steps\": 14875, \"full_steps\": 9039}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.4, \"fast_path_ratio\": 0.45, \"adaptive_trigger_rate\": 0.55, \"mean_l2_distance\": 0.0923, \"total_steps\": 23661, \"fast_steps\": 10649, \"full_steps\": 13012, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 3.07, \"fast_path_ratio\": 0.866}}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 3.15, \"fast_path_ratio\": 0.856}}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.72, \"fast_path_ratio\": 0.785}}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.81, \"fast_path_ratio\": 0.7737, \"total_steps\": 27813, \"fast_steps\": 21520, \"full_steps\": 6293}}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0.1, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.4, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"mean_l2_distance\": 0.0903, \"total_steps\": 23414, \"fast_steps\": 10728, \"full_steps\": 12686, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.2, \"total_episodes\": 100, \"total_successes\": 20, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.4, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"latency-profile-n1000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vla_e2e_K1_ms\": 256.5, \"vla_e2e_K10_ms\": 253.2, \"crm_forward_ms\": 0.28, \"cgs_features_ms\": 5.75, \"full_pipeline_K10_ms\": 249, \"adaptive_fast_path_ms\": 252.9, \"adaptive_full_path_ms\": 459.6, \"crm_overhead_vs_vla_K10_ms\": -4.2, \"crm_overhead_pct\": -1.66, \"adaptive_speedup_ratio\": 1.82, \"argmin_l2_K10_ms\": 0.06, \"gpu_mem_mb\": 903, \"n_measure\": 1000, \"gpu_model\": \"RTX 4090\"}}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.58, \"fast_path_ratio\": 0.928}}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 4.788, \"fast_path_ratio\": 0.6515, \"total_steps\": 28207, \"fast_steps\": 18377, \"full_steps\": 9830}}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.36, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed49\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.65, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed52\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed51\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed50\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-crm-long-seed50\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.736, \"fast_path_ratio\": 0.658, \"adaptive_trigger_rate\": 0.342, \"total_steps\": 27889, \"fast_steps\": 18351, \"full_steps\": 9538}, \"conclusion\": \"success\"}, \"calibrate-crm-correction-signal\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"go_nogo\": \"NO-GO\", \"rho_k1_corr_vs_k10_var\": 0.1523, \"p_k1_corr_vs_k10_var\": \"6.37e-143\", \"rho_k2_corr_vs_k10_var\": 0.134, \"p_k2_corr_vs_k10_var\": \"8.66e-111\", \"total_steps\": 27626, \"total_episodes\": 100}}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.8, \"fast_path_ratio\": 0.65}}, \"eval-vla-only-goal-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.3}}}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 3.909, \"fast_path_ratio\": 0.761, \"total_steps\": 28067, \"fast_steps\": 21368, \"full_steps\": 6699}}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.022, \"fast_path_ratio\": 0.872, \"total_steps\": 27724, \"fast_steps\": 24181, \"full_steps\": 3543}}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.612, \"fast_path_ratio\": 0.923, \"total_steps\": 27935, \"fast_steps\": 25797, \"full_steps\": 2138}}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 2.672, \"fast_path_ratio\": 0.916, \"total_steps\": 28258, \"fast_steps\": 25886, \"full_steps\": 2372}}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.2, \"STUDY_SCENE1_book_in_caddy\": 0.2, \"LIVING_ROOM_SCENE2_soup_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cheese_butter_basket\": 0, \"KITCHEN_SCENE4_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_soup_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.3, \"STUDY_SCENE1_book_in_back_compartment\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0.1, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.9, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.2, \"STUDY_SCENE1_book_in_back_compartment\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.65, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_bowl_on_top_of_the_cabinet\": 0.8, \"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"put_the_wine_bottle_on_the_rack\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_cream_cheese_in_the_bowl\": 0.2}}}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.64, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_bowl_on_the_stove\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"put_the_wine_bottle_on_the_rack\": 0.4, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"k2l2_vs_k10var_rho\": 0.9979, \"k2l2_vs_k10var_pvalue\": 0, \"k2l2_vs_fmvd_rho\": 0.0925, \"k2l2_vs_fmvd_pvalue\": 6.03e-29, \"k10var_vs_fmvd_rho\": 0.0825, \"k10var_vs_fmvd_pvalue\": 2.33e-23, \"n_samples\": 14512, \"k2l2_mean\": 0.0807, \"k2l2_std\": 0.0361, \"go_nogo_k2_proxy\": \"GO (rho=0.9979)\", \"go_nogo_fmvd_signal\": \"NO-GO (rho=0.09)\"}}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 18}}, \"eval-vla-only-spatial-seed49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.69, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.5, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.6}}}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2, \"alphabet_soup\": 0, \"cream_cheese\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.2, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.6, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.3, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.4, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.67, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 100, \"successful_rollouts\": 14, \"per_task\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0, \"put_both_cream_cheese_box_and_butter_in_basket\": 0, \"turn_on_stove_put_moka_pot\": 0.8, \"put_black_bowl_in_bottom_drawer\": 0, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.4, \"pick_up_book_place_in_caddy\": 0.1, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.1, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0, \"put_both_moka_pots_on_stove\": 0, \"put_yellow_white_mug_in_microwave\": 0}}}, \"eval-crm-goal-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.63, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.3, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.1, \"turn_on_the_stove\": 0.8, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.6, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 0.9, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.5, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.1, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}}, \"fmvd-calibration-phase1\": {\"status\": \"DONE\", \"metrics\": {\"spearman_rho\": 0.082528, \"spearman_pvalue\": 2.33e-23, \"n_samples\": 14512, \"go_nogo\": \"NO-GO\", \"threshold\": 0.3, \"fmvd_mean\": 0.054867, \"fmvd_std\": 0.040291, \"fmvd_P25\": 0.027738, \"fmvd_P50\": 0.046693, \"fmvd_P75\": 0.070899, \"fmvd_P90\": 0.093805, \"k10_variance_mean\": 0.004888, \"k10_variance_std\": 0.005635, \"task_success_rate\": 0.06, \"n_tasks\": 10, \"n_episodes\": 50, \"n_successes\": 3}, \"conclusion\": \"negative\"}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 1, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.2, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.2, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.1, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.7, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.3, \"STUDY_SCENE1_book_caddy\": 0, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0.1, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.2}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.32, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.8, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0.1, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.07, \"successes\": 7, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"successes\": 11, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"successes\": 14, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.37, \"successes\": 37, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_bowl_between_plate_ramekin\": 0.9, \"pick_up_bowl_next_to_ramekin\": 1, \"pick_up_bowl_from_table_center\": 0, \"pick_up_bowl_on_cookie_box\": 0.3, \"pick_up_bowl_in_top_drawer\": 0.1, \"pick_up_bowl_on_ramekin\": 0, \"pick_up_bowl_next_to_cookie_box\": 0.9, \"pick_up_bowl_on_stove\": 0, \"pick_up_bowl_next_to_plate\": 0.2, \"pick_up_bowl_on_wooden_cabinet\": 0}}}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_ms\": 28.4, \"crm_forward_ms\": 0.246, \"preprocess_ms\": 0.96, \"batched_K1_ms\": 180, \"batched_K5_ms\": 182.3, \"batched_K10_ms\": 162.3, \"batched_K20_ms\": 167.4, \"sequential_K1_ms\": 177, \"sequential_K5_ms\": 891.7, \"sequential_K10_ms\": 1638.9, \"sequential_K20_ms\": 3245.8, \"cgs_K10_ms\": 6.3, \"full_pipe_K10_ms\": 200.7, \"full_pipe_K20_ms\": 199.7, \"vla_model_mb\": 884.1, \"crm_model_mb\": 1.8, \"peak_K20_mb\": 1085.1}}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"sr_pct\": \"10%\"}}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.31, \"successes\": 31, \"total\": 100, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.6, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.29, \"successes\": 29, \"total\": 100, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.8, \"from_table_center\": 0.1, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}}}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.3, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.12, \"sr_pct\": \"12%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.18, \"sr_pct\": \"18%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.15, \"sr_pct\": \"15%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 5, \"sr_pct\": \"5%\", \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 34}}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 16}}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 18}}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.07, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}, \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.05, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"partial\": true, \"tasks_completed\": \"5/10\", \"task6_partial\": \"5/10 rollouts\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0}, \"partial_avg_sr\": 0.1, \"failure_mode\": \"process killed silently mid-eval, no error in log, no JSON output\"}}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.3, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Partial 9/10 tasks, 0/90 rollouts. Accepted as collapse evidence per Director decision 2026-05-18.\"}}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"negative\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 100, \"avg_inference_time_ms\": 178, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0}}}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100}}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.69, \"n_tasks\": 10, \"n_trials_per_task\": 10, \"total_rollouts\": 100}}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_prefix_ms\": 33.5, \"vla_sample_K1_ms\": 192.6, \"vla_sample_K5_ms\": 965.3, \"vla_sample_K10_ms\": 1913.7, \"vla_sample_K20_ms\": 3858.2, \"cgs_ms\": 6.2, \"crm_forward_ms\": 0.3, \"full_pipeline_K10_ms\": 1908.2, \"acr_overhead_pct\": 0.34}}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.007199, \"total_epochs\": 50, \"train_samples\": 65223, \"obs_dim\": \"4x960D\", \"multi_scale\": true}, \"conclusion\": \"success\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.07, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks\": 10, \"rollouts_per_task\": 20, \"total_successes\": 24, \"total_rollouts\": 200}}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"best_task\": \"chocolate_pudding_0.25\", \"worst_task\": \"alphabet_soup_0.0\"}}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006505, \"best_epoch\": 43, \"total_epochs\": 50, \"train_samples\": 4857, \"obs_dim\": 960, \"multi_scale\": false, \"wall_clock_seconds\": 914.9}}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.06, \"successes\": 6, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"n_rollouts\": 10, \"total_rollouts\": 100, \"note\": \"JSON result found by diagnostic worker. Matches original seed44=4%. False positive failure due to no sentinel/W&B in evaluate.py.\"}}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.08, \"total_successes\": 8, \"total_rollouts\": 100, \"seed\": 44, \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}, \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"total_episodes\": 100, \"successes\": 4, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 0, \"bbq_sauce\": 1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 1, \"milk\": 0, \"chocolate_pudding\": 1, \"orange_juice\": 0}}}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"negative\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"negative\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}}, \"precompute-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-k5\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.06, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.08, \"total_success\": 8, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"conclusion\": \"success\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}}, \"crm-train-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}}, \"crm-train-k5\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}}, \"count\": 749, \"total\": 749, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.2655}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-24T03:25:00.371Z_

<details><summary>↩ Tool result · `toolu_01SBrcCnViV3W92L9Su7tPkm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6711}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "9eefc271-4a00-4a51-aa7d-edc6fb8db868",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.6711}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6711}}"
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
Good - no FAILED experiments. The DONE list is too large to read directly. Let me search specifically for the exp_ids I need to update.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "a74122e5-f1dc-44b3-b789-251ec2227764",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qefRexR4BdDdbucbEdpo9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 44489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1900
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

没有 FAILED 状态的实验。让我直接查找需要更新的特定 exp_id。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "0d6b79fe-757d-489d-bad2-5cef889a78e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qefRexR4BdDdbucbEdpo9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 44489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1900
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

<details open><summary>🔧 Tool call — Bash · `toolu_015YsJycRABYGkcVepaYa6wV`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/602e10fd-b61b-43df-9ff5-2ac62d7d0b87/tool-results/mcp-agent-ml-research-read_registry-1779593096635.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\ntargets = [\n    'eval-supp-spatial-k2mean-s46',\n    'eval-supp-reconvla-obj-s45',\n    'eval-supp-long-reconvla-s45',\n    'eval-supp-long-vla-only-s45',\n    'eval-supp-long-crm-norm005-s45',\n    'eval-supp-long-adapt-tau025-s45',\n    'eval-supp-long-k2mean-s45',\n    'eval-supp-goal-adapt-tau025-s45',\n    'eval-supp-obj-crm-norm005-s46',\n    'eval-supp-obj-vla-only-s46',\n]\nfor t in targets:\n    if t in exps:\n        e = exps[t]\n        print(f'{t}: status={e.get(\\\"status\\\")}, conclusion={e.get(\\\"conclusion\\\")}, metrics={e.get(\\\"metrics\\\")}')\n    else:\n        print(f'{t}: NOT IN REGISTRY')\n\"\n",
  "description": "Check registry status for target experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "6b45ecb4-fbc4-4639-9010-39fbf776206f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qefRexR4BdDdbucbEdpo9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 44489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1900
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

_source line 55 · 2026-05-24T03:25:09.945Z_

<details><summary>↩ Tool result · `toolu_015YsJycRABYGkcVepaYa6wV`</summary>

```text
eval-supp-spatial-k2mean-s46: status=DONE, conclusion=failed, metrics=None
eval-supp-reconvla-obj-s45: status=DONE, conclusion=failed, metrics=None
eval-supp-long-reconvla-s45: status=DONE, conclusion=failed, metrics=None
eval-supp-long-vla-only-s45: status=DONE, conclusion=success, metrics={'SR': 0.575, 'successes': 115, 'total': 200}
eval-supp-long-crm-norm005-s45: status=DONE, conclusion=success, metrics={'SR': 0.605, 'successes': 121, 'total': 200}
eval-supp-long-adapt-tau025-s45: status=DONE, conclusion=success, metrics={'SR': 0.6, 'successes': 120, 'total': 200}
eval-supp-long-k2mean-s45: status=DONE, conclusion=success, metrics={'success_rate': 0.56, 'source': 'json_harvest_bjb2-28827'}
eval-supp-goal-adapt-tau025-s45: status=DONE, conclusion=success, metrics={'success_rate': 0.81, 'successes': 162, 'total': 200, 'trigger_rate': 0.094, 'mean_unc': 0.1493}
eval-supp-obj-crm-norm005-s46: NOT IN REGISTRY
eval-supp-obj-vla-only-s46: status=DONE, conclusion=success, metrics={'SR': 0.79}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "8d402ac4-9066-4f8c-b573-17d2531b59dc",
  "tool_use_result": {
    "stdout": "eval-supp-spatial-k2mean-s46: status=DONE, conclusion=failed, metrics=None\neval-supp-reconvla-obj-s45: status=DONE, conclusion=failed, metrics=None\neval-supp-long-reconvla-s45: status=DONE, conclusion=failed, metrics=None\neval-supp-long-vla-only-s45: status=DONE, conclusion=success, metrics={'SR': 0.575, 'successes': 115, 'total': 200}\neval-supp-long-crm-norm005-s45: status=DONE, conclusion=success, metrics={'SR': 0.605, 'successes': 121, 'total': 200}\neval-supp-long-adapt-tau025-s45: status=DONE, conclusion=success, metrics={'SR': 0.6, 'successes': 120, 'total': 200}\neval-supp-long-k2mean-s45: status=DONE, conclusion=success, metrics={'success_rate': 0.56, 'source': 'json_harvest_bjb2-28827'}\neval-supp-goal-adapt-tau025-s45: status=DONE, conclusion=success, metrics={'success_rate': 0.81, 'successes': 162, 'total': 200, 'trigger_rate': 0.094, 'mean_unc': 0.1493}\neval-supp-obj-crm-norm005-s46: NOT IN REGISTRY\neval-supp-obj-vla-only-s46: status=DONE, conclusion=success, metrics={'SR': 0.79}",
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
Now I can see:
- eval-supp-spatial-k2mean-s46: DONE, conclusion=failed, metrics=None → needs update to success with metrics
- eval-supp-reconvla-obj-s45: DONE, conclusion=failed, metrics=None → needs update to success with metrics
- eval-supp-long-reconvla-s45: DONE, conclusion=failed, metrics=None → needs update to success with metrics
- eval-supp-long-vla-only-s45: already success with correct metrics
- eval-supp-long-crm-norm005-s45: already success with correct metrics


- eval-supp-long-adapt-tau025-s45: already success with correct metrics
- eval-supp-long-k2mean-s45: already success (0.56)
- eval-supp-goal-adapt-tau025-s45: already success with correct metrics
- eval-supp-obj-crm-norm005-s46: NOT IN REGISTRY → needs creation
- eval-supp-obj-vla-only-s46: already success

So I need to update three entries with failed conclusions to success and add their metrics, plus create the missing registry entry for eval-supp-obj-crm-norm005-s46.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "92cbbbbc-6f03-4ddc-b249-071252a1d90e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UMduSNDEpkxkZPrxn9cB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 981,
      "cache_read_input_tokens": 46389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 981
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

_source line 57_

发现 3 个被误标 failed 的实验有有效 JSON，1 个不在 registry。现在更新 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "a9c64f63-930c-407a-89fd-4440b4636ea6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UMduSNDEpkxkZPrxn9cB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 981,
      "cache_read_input_tokens": 46389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 981
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

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_017DLhwGaWU3y8xqZ1rAEZC4`</summary>

```json
{
  "exp_id": "eval-supp-spatial-k2mean-s46",
  "field": "metrics",
  "value": {
    "success_rate": 0.8,
    "successes": 160,
    "total": 200,
    "source": "json_harvest_bjb1"
  },
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "06011b86-ae70-40c5-8334-2b127307ed36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UMduSNDEpkxkZPrxn9cB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 981,
      "cache_read_input_tokens": 46389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 981
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

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_013p4iRg67764MypnEovbjUM`</summary>

```json
{
  "exp_id": "eval-supp-reconvla-obj-s45",
  "field": "metrics",
  "value": {
    "success_rate": 0.78,
    "successes": 156,
    "total": 200,
    "source": "json_harvest_bjb1"
  },
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "2008e112-5dd7-46b1-b628-fcc3d435316f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UMduSNDEpkxkZPrxn9cB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 981,
      "cache_read_input_tokens": 46389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 981
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

_source line 60_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01FvCNvNs91ZT19X7xHapaC6`</summary>

```json
{
  "exp_id": "eval-supp-long-reconvla-s45",
  "field": "metrics",
  "value": {
    "success_rate": 0.59,
    "successes": 118,
    "total": 200,
    "source": "json_harvest_bjb1"
  },
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "8c61caac-ab6c-4d6c-99c4-6e88c75b8632",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UMduSNDEpkxkZPrxn9cB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 981,
      "cache_read_input_tokens": 46389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 981
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_015SgusVgy7NXfbKYMWTa9q6`</summary>

```json
{
  "exp_id": "eval-supp-obj-crm-norm005-s46",
  "field": "hypothesis",
  "value": "Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "4e8be26e-4b7c-4f8f-9ce4-323d0d152758",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UMduSNDEpkxkZPrxn9cB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 981,
      "cache_read_input_tokens": 46389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 981
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

_source line 62 · 2026-05-24T03:25:31.284Z_

<details><summary>↩ Tool result · `toolu_017DLhwGaWU3y8xqZ1rAEZC4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s46\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:41:52.628Z\", \"updated_at\": \"2026-05-24T03:25:29.861Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed46. Fifth seed extending Spatial K2mean coverage for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_spatial_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"seed\": 46, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"log_path\": \"/tmp/eval_spatial_k2mean_s46.log\", \"checkpoint_source\": \"n/a\", \"checkpoint_path\": \"n/a-eval-only\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:40:09.136Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:40:06.099Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:40:29.611202+00:00\"}]}, \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.1685}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "b5decfbd-a8a8-4db2-a3b7-8a307f43ed54",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-k2mean-s46\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T23:41:52.628Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:25:29.861Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Spatial suite seed46. Fifth seed extending Spatial K2mean coverage for variance analysis.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_spatial_k2mean_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"seed\\\": 46, \\\"model_name\\\": \\\"SmolVLA-K2mean\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_k2mean_s46.log\\\", \\\"checkpoint_source\\\": \\\"n/a\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-24T01:40:09.136Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-24T01:40:06.099Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-24T01:40:29.611202+00:00\\\"}]}, \\\"metrics\\\": {\\\"success_rate\\\": 0.8, \\\"successes\\\": 160, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.1685}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s46\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:41:52.628Z\", \"updated_at\": \"2026-05-24T03:25:29.861Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed46. Fifth seed extending Spatial K2mean coverage for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_spatial_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"seed\": 46, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"log_path\": \"/tmp/eval_spatial_k2mean_s46.log\", \"checkpoint_source\": \"n/a\", \"checkpoint_path\": \"n/a-eval-only\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:40:09.136Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:40:06.099Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:40:29.611202+00:00\"}]}, \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.1685}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-24T03:25:44.154Z_

<details><summary>↩ Tool result · `toolu_013p4iRg67764MypnEovbjUM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-reconvla-obj-s45\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:37:18.110Z\", \"updated_at\": \"2026-05-24T03:25:42.811Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed45. Extends Object Reconvla coverage, s46 already 80.0%. Fourth seed for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"seed\": 45, \"model_name\": \"smolvla+crm\", \"data_path\": \"libero_object\", \"data_count\": 20, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"logs/eval-reconvla-obj-s45.log\", \"checkpoint_path\": \"n/a-eval-only\", \"eval_data\": \"libero_object\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:14:37.557Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T01:14:46.869Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:14:59.634087+00:00\"}]}, \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.8454}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "2385cc4f-2eb7-487b-8c6e-bfa646d43312",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-reconvla-obj-s45\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T22:37:18.110Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:25:42.811Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on Object suite seed45. Extends Object Reconvla coverage, s46 already 80.0%. Fourth seed for variance analysis.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"seed\\\": 45, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 20, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"log_path\\\": \\\"logs/eval-reconvla-obj-s45.log\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"eval_data\\\": \\\"libero_object\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-24T01:14:37.557Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-24T01:14:46.869Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-24T01:14:59.634087+00:00\\\"}]}, \\\"metrics\\\": {\\\"success_rate\\\": 0.78, \\\"successes\\\": 156, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 12.8454}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-reconvla-obj-s45\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:37:18.110Z\", \"updated_at\": \"2026-05-24T03:25:42.811Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed45. Extends Object Reconvla coverage, s46 already 80.0%. Fourth seed for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"seed\": 45, \"model_name\": \"smolvla+crm\", \"data_path\": \"libero_object\", \"data_count\": 20, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"logs/eval-reconvla-obj-s45.log\", \"checkpoint_path\": \"n/a-eval-only\", \"eval_data\": \"libero_object\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:14:37.557Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T01:14:46.869Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:14:59.634087+00:00\"}]}, \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.8454}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-24T03:25:50.929Z_

<details><summary>↩ Tool result · `toolu_01FvCNvNs91ZT19X7xHapaC6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-reconvla-s45\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T20:12:57.615Z\", \"updated_at\": \"2026-05-24T03:25:49.550Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed45. Fourth seed for Long Reconvla validation.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"seed\": 45, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"crm_unified_4suite_r4/crm_best.pt\", \"log_path\": \"/tmp/eval_long_reconvla_s45.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:10:03.694Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:10:13.119Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:10:25.577523+00:00\"}]}, \"metrics\": {\"success_rate\": 0.59, \"successes\": 118, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.7557}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "4eca27bb-7cf5-4b79-98e9-6fc748b74475",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-reconvla-s45\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T20:12:57.615Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:25:49.550Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Long suite seed45. Fourth seed for Long Reconvla validation.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"seed\\\": 45, \\\"model_name\\\": \\\"SmolVLA-Reconvla\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"crm_unified_4suite_r4/crm_best.pt\\\", \\\"log_path\\\": \\\"/tmp/eval_long_reconvla_s45.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-24T01:10:03.694Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-24T01:10:13.119Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-24T01:10:25.577523+00:00\\\"}]}, \\\"metrics\\\": {\\\"success_rate\\\": 0.59, \\\"successes\\\": 118, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.7557}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-reconvla-s45\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T20:12:57.615Z\", \"updated_at\": \"2026-05-24T03:25:49.550Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed45. Fourth seed for Long Reconvla validation.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"seed\": 45, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"crm_unified_4suite_r4/crm_best.pt\", \"log_path\": \"/tmp/eval_long_reconvla_s45.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:10:03.694Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:10:13.119Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:10:25.577523+00:00\"}]}, \"metrics\": {\"success_rate\": 0.59, \"successes\": 118, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.7557}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-24T03:25:57.680Z_

<details><summary>↩ Tool result · `toolu_015SgusVgy7NXfbKYMWTa9q6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-crm-norm005-s46\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:25:56.315Z\", \"updated_at\": \"2026-05-24T03:25:56.316Z\", \"hypothesis\": \"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.7252}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "74555163-0883-4ad3-b7dd-70635f0ab712",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-obj-crm-norm005-s46\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T03:25:56.315Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:25:56.316Z\\\", \\\"hypothesis\\\": \\\"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.7252}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-crm-norm005-s46\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:25:56.315Z\", \"updated_at\": \"2026-05-24T03:25:56.316Z\", \"hypothesis\": \"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.7252}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 66_

<details><summary>Logged reasoning block</summary>

```text
Now I need to:
1. Update the conclusion for eval-supp-reconvla-obj-s45 (it's still "failed" - the metrics update didn't change conclusion)
2. Update conclusion for eval-supp-long-reconvla-s45 (already updated to "success" based on the response)
3. Update eval-supp-obj-crm-norm005-s46 with metrics and conclusion

Wait, looking at the responses:
- eval-supp-spatial-k2mean-s46: conclusion already "success" - just metrics updated ✓


- eval-supp-reconvla-obj-s45: conclusion still "failed" even though metrics were added → need to update conclusion
- eval-supp-long-reconvla-s45: conclusion shows "success" → already good ✓
- eval-supp-obj-crm-norm005-s46: status PREPARING → needs metrics and conclusion

Let me update the conclusions and the new entry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "3af95232-3fbf-4129-a8e4-ec98ebd06509",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WqQEssyyrUFudYcgbtzEKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3287,
      "cache_read_input_tokens": 47370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3287
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 67_

eval-supp-reconvla-obj-s45 的 conclusion 还是 failed，需要修正。同时完成新创建实验的 metrics 和 conclusion。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "2d325725-79c9-4f0f-a522-9f25f9483736",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WqQEssyyrUFudYcgbtzEKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3287,
      "cache_read_input_tokens": 47370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3287
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 68_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01RXcnzREjoAcZUsjWtPsrFm`</summary>

```json
{
  "exp_id": "eval-supp-reconvla-obj-s45",
  "field": "conclusion",
  "value": "success",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "8b7c5b1e-eab1-47ba-a0ed-ddc4e90ce9d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WqQEssyyrUFudYcgbtzEKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3287,
      "cache_read_input_tokens": 47370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3287
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01LPwFSDtLRHZLYSMbXb6voc`</summary>

```json
{
  "exp_id": "eval-supp-obj-crm-norm005-s46",
  "field": "metrics",
  "value": {
    "success_rate": 0.795,
    "successes": 159,
    "total": 200,
    "source": "json_harvest_bjb1"
  },
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "2f6d56bb-e53e-4fb8-b663-0e9bea49a4fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WqQEssyyrUFudYcgbtzEKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3287,
      "cache_read_input_tokens": 47370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3287
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 70 · 2026-05-24T03:26:18.013Z_

<details><summary>↩ Tool result · `toolu_01RXcnzREjoAcZUsjWtPsrFm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-reconvla-obj-s45\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:37:18.110Z\", \"updated_at\": \"2026-05-24T03:26:15.872Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed45. Extends Object Reconvla coverage, s46 already 80.0%. Fourth seed for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"seed\": 45, \"model_name\": \"smolvla+crm\", \"data_path\": \"libero_object\", \"data_count\": 20, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"logs/eval-reconvla-obj-s45.log\", \"checkpoint_path\": \"n/a-eval-only\", \"eval_data\": \"libero_object\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:14:37.557Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:14:46.869Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:14:59.634087+00:00\"}]}, \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}, \"impact_analysis\": {\"change_type\": \"experiment\", \"change_id\": \"eval-supp-reconvla-obj-s45\", \"affected_decisions\": [], \"cascade_decisions\": [], \"affected_claims\": [], \"affected_figures\": [], \"recommendations\": [\"No downstream impact detected\"]}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.4669}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "35c2c5b7-3e33-4677-bca2-82446017f832",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-reconvla-obj-s45\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T22:37:18.110Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:15.872Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on Object suite seed45. Extends Object Reconvla coverage, s46 already 80.0%. Fourth seed for variance analysis.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"seed\\\": 45, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 20, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"log_path\\\": \\\"logs/eval-reconvla-obj-s45.log\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"eval_data\\\": \\\"libero_object\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-24T01:14:37.557Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-24T01:14:46.869Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-24T01:14:59.634087+00:00\\\"}]}, \\\"metrics\\\": {\\\"success_rate\\\": 0.78, \\\"successes\\\": 156, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1\\\"}}, \\\"impact_analysis\\\": {\\\"change_type\\\": \\\"experiment\\\", \\\"change_id\\\": \\\"eval-supp-reconvla-obj-s45\\\", \\\"affected_decisions\\\": [], \\\"cascade_decisions\\\": [], \\\"affected_claims\\\": [], \\\"affected_figures\\\": [], \\\"recommendations\\\": [\\\"No downstream impact detected\\\"]}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 11.4669}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-reconvla-obj-s45\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:37:18.110Z\", \"updated_at\": \"2026-05-24T03:26:15.872Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed45. Extends Object Reconvla coverage, s46 already 80.0%. Fourth seed for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"seed\": 45, \"model_name\": \"smolvla+crm\", \"data_path\": \"libero_object\", \"data_count\": 20, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"logs/eval-reconvla-obj-s45.log\", \"checkpoint_path\": \"n/a-eval-only\", \"eval_data\": \"libero_object\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:14:37.557Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:14:46.869Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:14:59.634087+00:00\"}]}, \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}, \"impact_analysis\": {\"change_type\": \"experiment\", \"change_id\": \"eval-supp-reconvla-obj-s45\", \"affected_decisions\": [], \"cascade_decisions\": [], \"affected_claims\": [], \"affected_figures\": [], \"recommendations\": [\"No downstream impact detected\"]}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.4669}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-24T03:26:24.323Z_

<details><summary>↩ Tool result · `toolu_01LPwFSDtLRHZLYSMbXb6voc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-crm-norm005-s46\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:25:56.315Z\", \"updated_at\": \"2026-05-24T03:26:21.517Z\", \"hypothesis\": \"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.2876}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "9ae88a8b-4515-491c-834a-93e06297862c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-obj-crm-norm005-s46\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T03:25:56.315Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:21.517Z\\\", \\\"hypothesis\\\": \\\"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.795, \\\"successes\\\": 159, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.2876}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-crm-norm005-s46\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:25:56.315Z\", \"updated_at\": \"2026-05-24T03:26:21.517Z\", \"hypothesis\": \"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.2876}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01K5aPSsR5gAkg3nda15B9Sn`</summary>

```json
{
  "exp_id": "eval-supp-obj-crm-norm005-s46",
  "field": "conclusion",
  "value": "success",
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
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "6bd8cf18-fa5b-448e-952b-f6c663ee3a18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpGHHVKMMr7zTCciQ4D7U3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1575,
      "cache_read_input_tokens": 50657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1575
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 73 · 2026-05-24T03:26:36.274Z_

<details><summary>↩ Tool result · `toolu_01K5aPSsR5gAkg3nda15B9Sn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-crm-norm005-s46\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:25:56.315Z\", \"updated_at\": \"2026-05-24T03:26:33.701Z\", \"hypothesis\": \"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"source\": \"json_harvest_bjb1\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.4724}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "a2bf43a1-3b9a-4869-af09-f74238a0e5b4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-obj-crm-norm005-s46\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T03:25:56.315Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:33.701Z\\\", \\\"hypothesis\\\": \\\"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.795, \\\"successes\\\": 159, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1\\\"}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.4724}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-crm-norm005-s46\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:25:56.315Z\", \"updated_at\": \"2026-05-24T03:26:33.701Z\", \"hypothesis\": \"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"source\": \"json_harvest_bjb1\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.4724}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
All registry updates are done. Let me also check if there are any additional recent JSON files from the latest round that should be harvested. Let me check the /tmp logs that seem to be from active processes on seed46.

Actually looking at the /tmp logs timestamps:
- eval_long_adapt_s46.log: May 24 11:20
- eval_long_crm_s46.log: May 24 11:21
- eval_long_reconvla_s46.log: May 24 11:23
- eval_crm_obj_s46.log: May 24 06:30


These processes appear to still be running based on the GPU activity I'm seeing on GPUs 0-3. I should also pull in those seed43 variants I spotted in the find output—eval_long_crm_obs_only_norm0.05_seed43.json, eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json, and eval_long_reconvla_seed43.json—since they're part of the experiments I need to summarize.

There are seed43 and seed44 results for the spatial, goal, and object benchmarks too, but those seem to be from an earlier iteration and weren't specifically called out in the task. Now I'll put together the summary report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "c3f6a334-e5ee-4193-8059-fe067ff71f50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQb2TMBUgvYyFKsUiB42Gr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 52232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 371
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

_source line 75_

全部 registry 更新完成。汇总报告如下：

---

## 汇总报告

### GPU 状态 (bjb1-32546)

| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| 0 | 22% | 6289/24564 MiB | 运行中 |
| 1 | 33% | 9012/24564 MiB | 运行中 |
| 2 | 46% | 8360/24564 MiB | 运行中 |
| 3 | 24% | 5844/24564 MiB | 运行中 |
| 4 | 0% | 2/24564 MiB | 空闲 |
| 5 | 0% | 2/24564 MiB | 空闲 |

### 磁盘状态

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 10G | 21G | 34% |
| /root/autodl-tmp | 250G | 68G | 183G | 28% |

### 收割的 JSON 结果

| 文件名 | success_rate | exp_id | Registry 操作 |
|--------|-------------|--------|---------------|
| eval_spatial_k2mean_seed46.json | **0.80** | eval-supp-spatial-k2mean-s46 | metrics 更新 (原 conclusion=failed→已是 success，补 metrics) |
| eval_object_reconvla_seed45.json | **0.78** | eval-supp-reconvla-obj-s45 | metrics 更新 + conclusion failed→**success** |
| eval_long_reconvla_seed45.json | **0.59** | eval-supp-long-reconvla-s45 | metrics 更新 (conclusion 已自动修正为 success) |
| eval_long_vla_only_seed45.json | **0.575** | eval-supp-long-vla-only-s45 | 已有正确数据，无需更新 |
| eval_long_crm_obs_only_norm0.05_seed45.json | **0.605** | eval-supp-long-crm-norm005-s45 | 已有正确数据，无需更新 |
| eval_long_adaptive_...tau0.25_seed45.json | **0.60** | eval-supp-long-adapt-tau025-s45 | 已有正确数据，无需更新 |
| eval_object_crm_obs_only_norm0.05_seed46.json | **0.795** | eval-supp-obj-crm-norm005-s46 | **新建** + metrics + conclusion=success |
| eval_object_vla_only_seed46.json | **0.79** | eval-supp-obj-vla-only-s46 | 已有正确数据，无需更新 |
| eval_goal_adaptive_...tau0.25_seed45.json | **0.81** | eval-supp-goal-adapt-tau025-s45 | 已有正确数据，无需更新 |

### 未找到的 JSON
- `eval_long_k2mean_seed45.json` — 不存在于 logs/ 目录（registry 中已有来自 bjb2 的数据 SR=0.56）

### 被 cron 误标 failed 已修正：3 个
1. **eval-supp-spatial-k2mean-s46** — SR=0.80，metrics 已补录
2. **eval-supp-reconvla-obj-s45** — SR=0.78，conclusion 已修正为 success
3. **eval-supp-long-reconvla-s45** — SR=0.59，metrics 已补录

### 当前运行中
- Registry 中 RUNNING 状态仅剩 **eval-supp-long-vla-only-s46**
- /tmp 日志显示 GPU 0-3 上有 seed46 系列 Long 评估在跑（adapt/crm/reconvla s46，时间戳 ~11:20 今天）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "uuid": "38d82cf0-9082-4929-993a-ce0a5f7aae7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQb2TMBUgvYyFKsUiB42Gr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 52232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 371
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

_source line 76_

全部 registry 更新完成。汇总报告如下：

---

## 汇总报告

### GPU 状态 (bjb1-32546)

| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| 0 | 22% | 6289/24564 MiB | 运行中 |
| 1 | 33% | 9012/24564 MiB | 运行中 |
| 2 | 46% | 8360/24564 MiB | 运行中 |
| 3 | 24% | 5844/24564 MiB | 运行中 |
| 4 | 0% | 2/24564 MiB | 空闲 |
| 5 | 0% | 2/24564 MiB | 空闲 |

### 磁盘状态

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 10G | 21G | 34% |
| /root/autodl-tmp | 250G | 68G | 183G | 28% |

### 收割的 JSON 结果

| 文件名 | success_rate | exp_id | Registry 操作 |
|--------|-------------|--------|---------------|
| eval_spatial_k2mean_seed46.json | **0.80** | eval-supp-spatial-k2mean-s46 | metrics 更新 (原 conclusion=failed→已是 success，补 metrics) |
| eval_object_reconvla_seed45.json | **0.78** | eval-supp-reconvla-obj-s45 | metrics 更新 + conclusion failed→**success** |
| eval_long_reconvla_seed45.json | **0.59** | eval-supp-long-reconvla-s45 | metrics 更新 (conclusion 已自动修正为 success) |
| eval_long_vla_only_seed45.json | **0.575** | eval-supp-long-vla-only-s45 | 已有正确数据，无需更新 |
| eval_long_crm_obs_only_norm0.05_seed45.json | **0.605** | eval-supp-long-crm-norm005-s45 | 已有正确数据，无需更新 |
| eval_long_adaptive_...tau0.25_seed45.json | **0.60** | eval-supp-long-adapt-tau025-s45 | 已有正确数据，无需更新 |
| eval_object_crm_obs_only_norm0.05_seed46.json | **0.795** | eval-supp-obj-crm-norm005-s46 | **新建** + metrics + conclusion=success |
| eval_object_vla_only_seed46.json | **0.79** | eval-supp-obj-vla-only-s46 | 已有正确数据，无需更新 |
| eval_goal_adaptive_...tau0.25_seed45.json | **0.81** | eval-supp-goal-adapt-tau025-s45 | 已有正确数据，无需更新 |

### 未找到的 JSON
- `eval_long_k2mean_seed45.json` — 不存在于 logs/ 目录（registry 中已有来自 bjb2 的数据 SR=0.56）

### 被 cron 误标 failed 已修正：3 个
1. **eval-supp-spatial-k2mean-s46** — SR=0.80，metrics 已补录
2. **eval-supp-reconvla-obj-s45** — SR=0.78，conclusion 已修正为 success
3. **eval-supp-long-reconvla-s45** — SR=0.59，metrics 已补录

### 当前运行中
- Registry 中 RUNNING 状态仅剩 **eval-supp-long-vla-only-s46**
- /tmp 日志显示 GPU 0-3 上有 seed46 系列 Long 评估在跑（adapt/crm/reconvla s46，时间戳 ~11:20 今天）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 209595,
  "duration_api_ms": 144222,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "602e10fd-b61b-43df-9ff5-2ac62d7d0b87",
  "total_cost_usd": 0.6237379999999999,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 40762,
    "cache_read_input_tokens": 335271,
    "output_tokens": 7976,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40762,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1510,
        "cache_read_input_tokens": 52232,
        "cache_creation_input_tokens": 371,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 371
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1760,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0018750000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 7976,
      "cacheReadInputTokens": 335271,
      "cacheCreationInputTokens": 40762,
      "webSearchRequests": 0,
      "costUSD": 0.621863,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5287d017-3f2b-4e94-93e8-a58a47871436"
}
```

</details>

---
