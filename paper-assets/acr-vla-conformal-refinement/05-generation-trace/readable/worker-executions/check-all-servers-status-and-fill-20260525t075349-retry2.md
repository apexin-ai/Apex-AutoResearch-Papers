# check all servers status and fill 20260525T075349 retry2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/workers/worker_check_all-servers-status-and-fill_20260525T075349_retry2.log`
- **Structured JSON:** [`dfbb2ee49a7e6e0e19e3.json`](../../sessions/df/dfbb2ee49a7e6e0e19e3.json)

## Before a recorded user message

65 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
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
  "uuid": "8ac1aad2-0c6a-46f5-bb16-dab2854582d2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 2_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779700200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a8a698a0-b8f6-4bac-894b-355955791ba5",
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to:
1. Check GPU status on 4 servers
2. Verify if certain RUNNING experiments are actually still running
3. Report per-server status
4. Check if τ=0.075 experiment on bjb2-40593 is complete

Let me start by loading the necessary MCP tools and then run SSH commands on all 4 servers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "6571fa79-ce48-41d2-9bf2-a4046e786099",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxB8wF22wcdy14eZ6e7XRF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11778,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11778
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

_source line 4_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Sb6HLsoLyxph4yknUF4gpo`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "86252f12-fb9a-4607-a3d2-4bba304bdd8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxB8wF22wcdy14eZ6e7XRF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11778,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11778
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

_source line 5 · 2026-05-25T07:58:07.945Z_

<details><summary>↩ Tool result · `toolu_01Sb6HLsoLyxph4yknUF4gpo`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "5422bed2-4274-4bc1-a39c-05054b9ade45",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 6_

先查 registry RUNNING 实验和所有服务器 GPU 状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "cf9babf0-8807-4c19-b733-4ecf69bfdb5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EJdxzEwYG2A6sqaFddSAA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 23619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 874
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

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01VF318EhirHB9uc24QoaaPH`</summary>

```json
{
  "filters": {
    "status": "RUNNING"
  },
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "name",
    "status",
    "server",
    "gpu",
    "pid"
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "8284988b-5643-4777-9e91-ea59d5799d77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EJdxzEwYG2A6sqaFddSAA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 23619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 874
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017ihacqPotXSSzeZ92whWdJ`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "fb7119e4-0fd5-4663-9cd4-598e1a53debb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EJdxzEwYG2A6sqaFddSAA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 23619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 874
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AAHJLCGJcxqs1yPsyXdaHL`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "b24e91d5-d9c6-4087-b56c-fff66cdd7a8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EJdxzEwYG2A6sqaFddSAA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 23619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 874
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012RizVV5CzYYwZxdms4dXwJ`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "7a551635-36de-4ae9-a9d0-bdac606c978c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EJdxzEwYG2A6sqaFddSAA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 23619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 874
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

_source line 11 · 2026-05-25T07:58:14.690Z_

<details><summary>↩ Tool result · `toolu_01VF318EhirHB9uc24QoaaPH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-s43-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-object-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-adaptive-spatial-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-goal-s42-paired\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-spatial-s42-paired\": {\"status\": \"RUNNING\"}, \"eval-pi05-adaptive-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s47-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s47-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s46-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s46-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s45-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s45-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s44-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s43-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s42-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-tau0075-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s44\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s43\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s48\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s42\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s44\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s43\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"RUNNING\"}, \"eval-long-adaptive-k10-s44\": {\"status\": \"RUNNING\"}, \"eval-long-adaptive-k10-s43\": {\"status\": \"RUNNING\"}, \"eval-long-adaptive-k10-s42\": {\"status\": \"RUNNING\"}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"RUNNING\"}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s46\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s48\": {\"status\": \"RUNNING\"}, \"eval-k2-tau010-spatial-s42-r3\": {\"status\": \"RUNNING\"}, \"eval-k2-tau015-spatial-s42-r2\": {\"status\": \"RUNNING\"}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\"}}, \"count\": 45, \"total\": 45, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.429}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "1db9176f-58c1-429f-8361-a3da85de0419",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-pi05-vla-only-spatial-s43-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-vla-only-object-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-adaptive-spatial-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-vla-only-goal-s42-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-vla-only-spatial-s42-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-adaptive-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-vla-only-s47-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-adapt-s47-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-vla-only-s46-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-adapt-s46-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-vla-only-s45-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-adapt-s45-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-vla-only-s44-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-adapt-s44-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-vla-only-s43-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-adapt-s43-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-vla-only-s42-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-adapt-s42-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-tau0075-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-cqa1-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s49\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-cqa1-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s48\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-cqa1-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k10-tau025-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s49\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s48\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-long-adaptive-k10-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-long-adaptive-k10-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-long-adaptive-k10-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k10-tau025-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k10-tau025-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-bjb1-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-bjb1-s49\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-bjb1-s48\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-tau010-spatial-s42-r3\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-tau015-spatial-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"precompute-pi05-long-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}}, \\\"count\\\": 45, \\\"total\\\": 45, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.429}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-s43-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-object-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-adaptive-spatial-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-goal-s42-paired\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-spatial-s42-paired\": {\"status\": \"RUNNING\"}, \"eval-pi05-adaptive-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s47-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s47-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s46-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s46-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s45-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s45-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s44-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s43-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s42-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-tau0075-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s44\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s43\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s48\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s42\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s44\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s43\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"RUNNING\"}, \"eval-long-adaptive-k10-s44\": {\"status\": \"RUNNING\"}, \"eval-long-adaptive-k10-s43\": {\"status\": \"RUNNING\"}, \"eval-long-adaptive-k10-s42\": {\"status\": \"RUNNING\"}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"RUNNING\"}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s46\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s48\": {\"status\": \"RUNNING\"}, \"eval-k2-tau010-spatial-s42-r3\": {\"status\": \"RUNNING\"}, \"eval-k2-tau015-spatial-s42-r2\": {\"status\": \"RUNNING\"}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\"}}, \"count\": 45, \"total\": 45, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.429}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YF892ArGdbkxfWtujnmfRV`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "63ec63bf-0047-4d38-afdf-f76fa336c953",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EJdxzEwYG2A6sqaFddSAA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 23619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 874
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

_source line 13 · 2026-05-25T07:58:15.762Z_

<details><summary>↩ Tool result · `toolu_017ihacqPotXSSzeZ92whWdJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 14135 MiB, 24564 MiB, 23 %\\n1, 10365 MiB, 24564 MiB, 24 %\\n2, 10429 MiB, 24564 MiB, 14 %\\n3, 9883 MiB, 24564 MiB, 23 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "b3928e99-0e9e-4006-8901-22fb137314a2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 14135 MiB, 24564 MiB, 23 %\\\\n1, 10365 MiB, 24564 MiB, 24 %\\\\n2, 10429 MiB, 24564 MiB, 14 %\\\\n3, 9883 MiB, 24564 MiB, 23 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.06}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 14135 MiB, 24564 MiB, 23 %\\n1, 10365 MiB, 24564 MiB, 24 %\\n2, 10429 MiB, 24564 MiB, 14 %\\n3, 9883 MiB, 24564 MiB, 23 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T07:58:16.537Z_

<details><summary>↩ Tool result · `toolu_01AAHJLCGJcxqs1yPsyXdaHL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 2353 MiB, 24564 MiB, 20 %\\n1, 2347 MiB, 24564 MiB, 18 %\\n2, 2353 MiB, 24564 MiB, 18 %\\n3, 1895 MiB, 24564 MiB, 18 %\\n4, 2353 MiB, 24564 MiB, 18 %\\n5, 1894 MiB, 24564 MiB, 16 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "32ae4994-16d7-4ff0-a724-16c80e0a1e35",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 2353 MiB, 24564 MiB, 20 %\\\\n1, 2347 MiB, 24564 MiB, 18 %\\\\n2, 2353 MiB, 24564 MiB, 18 %\\\\n3, 1895 MiB, 24564 MiB, 18 %\\\\n4, 2353 MiB, 24564 MiB, 18 %\\\\n5, 1894 MiB, 24564 MiB, 16 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.76}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 2353 MiB, 24564 MiB, 20 %\\n1, 2347 MiB, 24564 MiB, 18 %\\n2, 2353 MiB, 24564 MiB, 18 %\\n3, 1895 MiB, 24564 MiB, 18 %\\n4, 2353 MiB, 24564 MiB, 18 %\\n5, 1894 MiB, 24564 MiB, 16 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T07:58:17.557Z_

<details><summary>↩ Tool result · `toolu_012RizVV5CzYYwZxdms4dXwJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 1978 MiB, 24564 MiB, 23 %\\n1, 1972 MiB, 24564 MiB, 20 %\\n2, 1978 MiB, 24564 MiB, 22 %\\n3, 2 MiB, 24564 MiB, 0 %\\n4, 1978 MiB, 24564 MiB, 20 %\\n5, 1972 MiB, 24564 MiB, 21 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.01}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "fc93d130-a39e-41e9-a021-76b72e08a461",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 1978 MiB, 24564 MiB, 23 %\\\\n1, 1972 MiB, 24564 MiB, 20 %\\\\n2, 1978 MiB, 24564 MiB, 22 %\\\\n3, 2 MiB, 24564 MiB, 0 %\\\\n4, 1978 MiB, 24564 MiB, 20 %\\\\n5, 1972 MiB, 24564 MiB, 21 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.01}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 1978 MiB, 24564 MiB, 23 %\\n1, 1972 MiB, 24564 MiB, 20 %\\n2, 1978 MiB, 24564 MiB, 22 %\\n3, 2 MiB, 24564 MiB, 0 %\\n4, 1978 MiB, 24564 MiB, 20 %\\n5, 1972 MiB, 24564 MiB, 21 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.01}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T07:58:18.318Z_

<details><summary>↩ Tool result · `toolu_01YF892ArGdbkxfWtujnmfRV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 2239 MiB, 24564 MiB, 12 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "cdbc7c40-5a05-41e9-9f6f-962d8c0269ac",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 2239 MiB, 24564 MiB, 12 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.75}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 2239 MiB, 24564 MiB, 12 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now I need to check the processes on each server and verify PIDs. Let me also check the registry for the specific old experiments mentioned by the user. The registry didn't return pid/server/gpu fields - let me get those. Also need to check processes on each server.

Let me now:
1. Get full registry details for the experiments mentioned
2. Check processes on each server
3. Check τ=0.075 on bjb2-40593
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "7cad680c-a6cb-4309-99b0-58079185d214",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDeZHpLenh18Ugsp2qhQq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 24493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2753
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

_source line 18_

Registry 没返回 pid/server/gpu 字段，重新查一下。同时查各服务器进程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "d541fe5b-6168-4424-ae2b-2b6293c52dbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDeZHpLenh18Ugsp2qhQq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 24493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2753
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AGfxv5L6s7G3fMTCQitDkM`</summary>

```json
{
  "filters": {
    "status": "RUNNING"
  },
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "*"
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "8882f74e-1655-4e2d-9b39-c498bd3e8074",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDeZHpLenh18Ugsp2qhQq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 24493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2753
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VDogpc8gDcJtegqt98BoGE`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ps aux --no-headers -o pid,user,%cpu,%mem,start,command --sort=-%mem",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "d544b504-4cad-462b-a3af-aa6949480d7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDeZHpLenh18Ugsp2qhQq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 24493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2753
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

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AnwT7s2SUtKNFysnyj1toA`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps aux --no-headers -o pid,user,%cpu,%mem,start,command --sort=-%mem",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "f74d4039-5fa3-4d65-a239-621ca5b24a20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDeZHpLenh18Ugsp2qhQq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 24493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2753
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

_source line 22 · 2026-05-25T07:58:26.590Z_

<details><summary>↩ Tool result · `toolu_01AGfxv5L6s7G3fMTCQitDkM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-s43-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:34:11.243Z\", \"updated_at\": \"2026-05-25T07:34:51.098Z\", \"hypothesis\": \"π0.5 VLA-only baseline rerun on LIBERO-Spatial s43 (bjb1-18228 cuda:2). Redundant replication on a different server to fill idle GPU; prior run (-s43) reached 0.96 success rate on bjb1-32546.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_pi05_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"485043\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"backend\": \"nohup\", \"account\": \"root\"}}, \"eval-pi05-vla-only-object-s42-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:34:04.734Z\", \"updated_at\": \"2026-05-25T07:34:43.804Z\", \"hypothesis\": \"π0.5 VLA-only baseline rerun on LIBERO-Object s42 (bjb1-18228 cuda:1). Redundant replication on a different server to fill idle GPU; prior run (-s42) reached 0.965 success rate on bjb1-32546.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"484670\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\", \"backend\": \"nohup\", \"account\": \"root\"}}, \"eval-pi05-adaptive-spatial-s42-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:32:29.311Z\", \"updated_at\": \"2026-05-25T07:33:45.816Z\", \"hypothesis\": \"π0.5 Adaptive CRM (K=2, τ=0.25) on LIBERO-Spatial s42. Retry of failed s42 run: CRM checkpoint trained with unified_obs_dim=2088 (2048D PI05 features padded by 40); previous run used default obs_dim=960 causing input_mean shape mismatch [2118] vs [990]. Now passing --obs_dim 2048 --unified_obs_dim 2088 to match training-time CRM input.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --output_file logs/eval_spatial_adaptive_pi05_seed42_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"484286\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_pi05_seed42_r2.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"backend\": \"nohup\", \"account\": \"root\"}}, \"eval-pi05-vla-only-goal-s42-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T04:30:16.021Z\", \"updated_at\": \"2026-05-25T07:25:21.880Z\", \"hypothesis\": \"π0.5 VLA-only baseline Goal s42 on bjb1-18228. 跨模型验证的 baseline。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_pi05_seed42_paired.json\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:2\"], \"pid\": 446717, \"log_path\": \"/tmp/eval-pi05-vla-only-goal-s42-paired.log\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"timeout\": 18000, \"account\": \"root\", \"gpu\": \"cuda:2\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200, \"mode\": \"vla_only\", \"benchmark\": \"goal\", \"seed\": 42, \"model\": \"pi05\"}}, \"eval-pi05-vla-only-spatial-s42-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T04:30:12.187Z\", \"updated_at\": \"2026-05-25T07:25:18.287Z\", \"hypothesis\": \"π0.5 VLA-only baseline Spatial s42 on bjb1-18228. 跨模型验证的 baseline，与后续 π0.5 Adaptive 同服务器配对。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_pi05_seed42_paired.json\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 446358, \"log_path\": \"/tmp/eval-pi05-vla-only-spatial-s42-paired.log\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"timeout\": 18000, \"account\": \"root\", \"gpu\": \"cuda:1\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200, \"mode\": \"vla_only\", \"benchmark\": \"spatial\", \"seed\": 42, \"model\": \"pi05\"}}, \"eval-pi05-adaptive-spatial-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:23:29.843Z\", \"updated_at\": \"2026-05-25T07:25:06.005Z\", \"hypothesis\": \"π0.5 Adaptive CRM (K=2, τ=0.25) on Spatial s42. 跨模型验证：π0.5 是否也能从 uncertainty gating 获益。Spatial trigger rate 最高，最可能看到效应。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --output_file logs/eval_spatial_adaptive_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"spatial\", \"gpu\": \"cuda:0\"}, \"conclusion\": \"failed\"}, \"eval-k2-goal-vla-only-s47-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:08:33.713Z\", \"updated_at\": \"2026-05-25T06:10:13.903Z\", \"hypothesis\": \"VLA-only baseline on Goal s47, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 47 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed47_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"smolvla_libero (no CRM)\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_vla_only_seed47_paired.log\"}}, \"eval-k2-goal-adapt-s47-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:08:28.049Z\", \"updated_at\": \"2026-05-25T06:10:06.863Z\", \"hypothesis\": \"K=2 Adaptive CRM (tau=0.25) on Goal s47, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test and trigger rate correlation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed47_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_adaptive_k2_tau025_seed47_paired.log\"}}, \"eval-k2-goal-vla-only-s46-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:08:23.483Z\", \"updated_at\": \"2026-05-25T06:09:59.793Z\", \"hypothesis\": \"VLA-only baseline on Goal s46, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 46 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed46_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"smolvla_libero (no CRM)\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_vla_only_seed46_paired.log\"}}, \"eval-k2-goal-adapt-s46-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:08:19.812Z\", \"updated_at\": \"2026-05-25T06:09:52.461Z\", \"hypothesis\": \"K=2 Adaptive CRM (tau=0.25) on Goal s46, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test and trigger rate correlation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed46_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_adaptive_k2_tau025_seed46_paired.log\"}}, \"eval-k2-goal-vla-only-s45-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:08:15.041Z\", \"updated_at\": \"2026-05-25T06:09:45.415Z\", \"hypothesis\": \"VLA-only baseline on Goal s45, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 45 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed45_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"smolvla_libero (no CRM)\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_vla_only_seed45_paired.log\"}}, \"eval-k2-goal-adapt-s45-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:08:05.643Z\", \"updated_at\": \"2026-05-25T06:09:37.026Z\", \"hypothesis\": \"K=2 Adaptive CRM (tau=0.25) on Goal s45, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test and trigger rate correlation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 45 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed45_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_adaptive_k2_tau025_seed45_paired.log\"}}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:39.553Z\", \"updated_at\": \"2026-05-25T06:08:09.387Z\", \"hypothesis\": \"VLA-only baseline on Spatial s44, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed44_paired_r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-k2-spatial-adapt-s44-paired-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:33.724Z\", \"updated_at\": \"2026-05-25T06:07:58.295Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s44, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:27.742Z\", \"updated_at\": \"2026-05-25T06:07:48.981Z\", \"hypothesis\": \"VLA-only baseline on Spatial s43, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed43_paired_r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-k2-spatial-adapt-s43-paired-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:21.430Z\", \"updated_at\": \"2026-05-25T06:07:39.847Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s43, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:14.262Z\", \"updated_at\": \"2026-05-25T06:07:27.518Z\", \"hypothesis\": \"VLA-only baseline on Spatial s42, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed42_paired_r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-k2-spatial-adapt-s42-paired-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:08.065Z\", \"updated_at\": \"2026-05-25T06:07:15.816Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s42, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-k2-tau0075-spatial-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T04:09:13.381Z\", \"updated_at\": \"2026-05-25T04:10:58.696Z\", \"hypothesis\": \"K=2 τ-sweep 补点: τ=0.075 Adaptive Conformal on Spatial s42。τ-sweep 图中该点是 SR 峰值(81.0%)，supplementary figure 需要。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.075 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-40593\", \"data_path\": \"libero/spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-tau0075-spatial-s42.log\", \"pid\": 349399}}, \"eval-vla-only-spatial-cqa1-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:41.130Z\", \"updated_at\": \"2026-05-25T02:57:12.230Z\", \"hypothesis\": \"VLA-only baseline Spatial s44 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s44\"}}, \"eval-k2-adaptive-spatial-s49\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:04.109Z\", \"updated_at\": \"2026-05-25T02:57:05.394Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是 Adaptive 方法设计的正确采样数（两次前向推理算 L2 距离做 gating）。配对 bjb1-32546 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial (20 rollouts)\", \"gpu\": \"cuda:3\", \"tmux_session\": \"eval-k2-adaptive-spatial-s49\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s49.log\"}}, \"eval-vla-only-spatial-cqa1-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:33.714Z\", \"updated_at\": \"2026-05-25T02:56:58.821Z\", \"hypothesis\": \"VLA-only baseline Spatial s43 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s43\"}}, \"eval-k2-adaptive-spatial-s48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:52:50.570Z\", \"updated_at\": \"2026-05-25T02:56:52.010Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是 Adaptive 方法设计的正确采样数（两次前向推理算 L2 距离做 gating）。配对 bjb1-32546 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial (20 rollouts)\", \"gpu\": \"cuda:2\", \"tmux_session\": \"eval-k2-adaptive-spatial-s48\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s48.log\"}}, \"eval-vla-only-spatial-cqa1-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:26.220Z\", \"updated_at\": \"2026-05-25T02:56:45.258Z\", \"hypothesis\": \"VLA-only baseline Spatial s42 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s42\"}}, \"eval-k2-adaptive-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:52:46.638Z\", \"updated_at\": \"2026-05-25T02:56:38.633Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是 Adaptive 方法设计的正确采样数（两次前向推理算 L2 距离做 gating）。配对 bjb1-32546 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 46 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial (20 rollouts)\", \"gpu\": \"cuda:0\", \"tmux_session\": \"eval-k2-adaptive-spatial-s46\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s46.log\"}}, \"eval-k2-adaptive-spatial-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:18.842Z\", \"updated_at\": \"2026-05-25T02:56:32.450Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s44\"}}, \"eval-k2-adaptive-spatial-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:11.261Z\", \"updated_at\": \"2026-05-25T02:56:24.240Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s43\"}}, \"eval-k2-adaptive-spatial-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:52:57.415Z\", \"updated_at\": \"2026-05-25T02:56:08.049Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s42\"}}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:03:58.063Z\", \"updated_at\": \"2026-05-25T02:50:55.056Z\", \"hypothesis\": \"Re-run s46 Adaptive Conformal with K=10 (τ=0.25) on Spatial on cqa1-32758 for same-server pairing. Audit confirmed s46 used K=2. Ensures uniform K=10 across all 8 seeds for valid paired t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 46 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k10-tau025-spatial-s46.log\", \"tmux_session\": \"eval-k10-tau025-spatial-s46\"}, \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T23:05:04.837Z\", \"updated_at\": \"2026-05-25T02:50:51.380Z\", \"hypothesis\": \"Canonical K=10 Adaptive Conformal (τ=0.25) on Spatial s49. Same-server data for paired t-test. Resubmit after timeout failure on cqa1.\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s49 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s49.log'\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"211568\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s49.log\", \"submitted_at\": \"2026-05-24T23:07:38.344Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s49\", \"timeout_seconds\": 18000}, \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T23:05:01.412Z\", \"updated_at\": \"2026-05-25T02:50:46.676Z\", \"hypothesis\": \"Canonical K=10 Adaptive Conformal (τ=0.25) on Spatial s48. Same-server data for paired t-test. Resubmit after timeout failure on cqa1.\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s48 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s48.log'\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"210816\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s48.log\", \"submitted_at\": \"2026-05-24T23:07:31.869Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s48\", \"timeout_seconds\": 18000}, \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T23:04:57.826Z\", \"updated_at\": \"2026-05-25T02:50:42.958Z\", \"hypothesis\": \"Canonical K=10 Adaptive Conformal (τ=0.25) on Spatial s44. Same-server data for paired t-test. Resubmit after timeout failure on cqa1.\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s44 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=5 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s44.log'\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"210458\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s44.log\", \"submitted_at\": \"2026-05-24T23:07:25.453Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s44\", \"timeout_seconds\": 18000}, \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T23:04:54.331Z\", \"updated_at\": \"2026-05-25T02:50:39.342Z\", \"hypothesis\": \"Canonical K=10 Adaptive Conformal (τ=0.25) on Spatial s43. Same-server data for paired t-test. Resubmit after timeout failure on cqa1.\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s43 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=4 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s43.log'\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"210181\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s43.log\", \"submitted_at\": \"2026-05-24T23:07:19.023Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s43\", \"timeout_seconds\": 18000}, \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:38:19.450Z\", \"updated_at\": \"2026-05-25T02:50:33.644Z\", \"hypothesis\": \"Long Adaptive K=10 (τ=0.25) 补跑。原 Long 实验使用 K=2 与 Spatial/Goal/Object (K=10) 不一致。补跑确保 Table 1 全 suite 统一 K=10 方法。Long Δ≈0 是预期的。\", \"parent\": \"eval-supp-long-adapt-tau025-s44\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 10\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_long\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_long\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s44.log\", \"gpu\": \"cuda:5\", \"tmux_session\": \"eval-long-adaptive-k10-s44\"}, \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:38:15.859Z\", \"updated_at\": \"2026-05-25T02:50:29.100Z\", \"hypothesis\": \"Long Adaptive K=10 (τ=0.25) 补跑。原 Long 实验使用 K=2 与 Spatial/Goal/Object (K=10) 不一致。补跑确保 Table 1 全 suite 统一 K=10 方法。Long Δ≈0 是预期的。\", \"parent\": \"eval-supp-long-adapt-tau025-s43\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 10\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_long\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_long\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s43.log\", \"gpu\": \"cuda:4\", \"tmux_session\": \"eval-long-adaptive-k10-s43\"}, \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:38:11.212Z\", \"updated_at\": \"2026-05-25T02:50:25.359Z\", \"hypothesis\": \"Long Adaptive K=10 (τ=0.25) 补跑。原 Long 实验使用 K=2 与 Spatial/Goal/Object (K=10) 不一致。补跑确保 Table 1 全 suite 统一 K=10 方法。Long Δ≈0 是预期的。\", \"parent\": \"eval-supp-long-adapt-tau025-s42\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --K 10\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_long\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_long\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s42.log\", \"gpu\": \"cuda:3\", \"tmux_session\": \"eval-long-adaptive-k10-s42\"}, \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:24:29.423Z\", \"updated_at\": \"2026-05-25T02:50:21.717Z\", \"hypothesis\": \"Re-run s47 Adaptive Conformal with K=10 (τ=0.25) on Spatial on cqa1-32758 for same-server pairing. Ensures uniform K=10 + same-server across all 8 seeds for valid paired t-test.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\"}, \"notes\": \"2026-05-25 09:18: Killed first attempt (timeout=7200s, would have timed out). Resubmitted with timeout=18000s on cqa1-32758 cuda:1 in tmux eval-k10-tau025-spatial-s47.\", \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:24:16.535Z\", \"updated_at\": \"2026-05-25T02:50:17.943Z\", \"hypothesis\": \"Re-run s45 Adaptive Conformal with K=10 (τ=0.25) on Spatial on cqa1-32758 for same-server pairing. Previous s45 data likely from K=2 run. Ensures uniform K=10 across all 8 seeds for valid paired t-test.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 45 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\"}, \"notes\": \"2026-05-25 09:18: Killed first attempt (timeout=7200s, would have timed out). Resubmitted with timeout=18000s on cqa1-32758 cuda:0 in tmux eval-k10-tau025-spatial-s45.\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T23:04:50.613Z\", \"updated_at\": \"2026-05-25T02:50:14.144Z\", \"hypothesis\": \"Canonical same-server Adaptive K=10 on cqa1-32758 Spatial s42. Eliminates cross-server confound — paired with cqa1 VLA-only baseline for clean paired t-test.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"pid\": \"209904\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-canonical-adaptive-k10-spatial-s42.log\", \"submitted_at\": \"2026-05-24T23:07:09.098Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s42\", \"timeout_s\": 18000}, \"notes\": \"2026-05-25 09:22: Resubmitted after timeout=7200s failure. Now timeout=18000s on cqa1-32758 cuda:2 in tmux eval-canonical-adaptive-k10-spatial-s42.\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-bjb1-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:36:53.772Z\", \"updated_at\": \"2026-05-25T01:37:21.767Z\", \"hypothesis\": \"VLA-only baseline on Spatial s46 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 46 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 46}}, \"eval-vla-only-spatial-bjb1-s49\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:32:07.247Z\", \"updated_at\": \"2026-05-25T01:32:46.520Z\", \"hypothesis\": \"VLA-only baseline on Spatial s49 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 49}}, \"eval-vla-only-spatial-bjb1-s48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:32:03.658Z\", \"updated_at\": \"2026-05-25T01:32:39.435Z\", \"hypothesis\": \"VLA-only baseline on Spatial s48 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 48}}, \"eval-k2-tau010-spatial-s42-r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:52:49.412Z\", \"updated_at\": \"2026-05-25T00:54:58.601Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.10 Adaptive Conformal on Spatial s42. Retry #3 on bjb2-28827 with 14400s timeout. Prior attempts timed out due to insufficient timeout and GPU contention on bjb2-40593.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.10 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau010-spatial-s42-r3.log\", \"tmux_session\": \"eval-k2-tau010-spatial-s42-r3\", \"timeout\": 14400}}, \"eval-k2-tau015-spatial-s42-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:52:41.760Z\", \"updated_at\": \"2026-05-25T00:54:51.278Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.15 Adaptive Conformal on Spatial s42. Retry on bjb2-28827 with 14400s timeout after first attempt timed out on bjb2-40593 (7200s, completed only 4/10 tasks).\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.15 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau015-spatial-s42-r2.log\", \"tmux_session\": \"eval-k2-tau015-spatial-s42-r2\", \"timeout\": 14400}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:31.140Z\", \"updated_at\": \"2026-05-24T06:23:39.262Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}}, \"count\": 45, \"total\": 45, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2149}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "7eb4d67a-30ff-4535-8041-58f3eb69771b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-pi05-vla-only-spatial-s43-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T07:34:11.243Z\\\", \\\"updated_at\\\": \\\"2026-05-25T07:34:51.098Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline rerun on LIBERO-Spatial s43 (bjb1-18228 cuda:2). Redundant replication on a different server to fill idle GPU; prior run (-s43) reached 0.96 success rate on bjb1-32546.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_pi05_seed43.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"485043\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/pi05_libero_finetuned/\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\", \\\"backend\\\": \\\"nohup\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval-pi05-vla-only-object-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T07:34:04.734Z\\\", \\\"updated_at\\\": \\\"2026-05-25T07:34:43.804Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline rerun on LIBERO-Object s42 (bjb1-18228 cuda:1). Redundant replication on a different server to fill idle GPU; prior run (-s42) reached 0.965 success rate on bjb1-32546.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"484670\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.log\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/pi05_libero_finetuned/\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 20 rollouts)\\\", \\\"backend\\\": \\\"nohup\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval-pi05-adaptive-spatial-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T07:32:29.311Z\\\", \\\"updated_at\\\": \\\"2026-05-25T07:33:45.816Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive CRM (K=2, τ=0.25) on LIBERO-Spatial s42. Retry of failed s42 run: CRM checkpoint trained with unified_obs_dim=2088 (2048D PI05 features padded by 40); previous run used default obs_dim=960 causing input_mean shape mismatch [2118] vs [990]. Now passing --obs_dim 2048 --unified_obs_dim 2088 to match training-time CRM input.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --output_file logs/eval_spatial_adaptive_pi05_seed42_r2.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"484286\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_pi05_seed42_r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\", \\\"backend\\\": \\\"nohup\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval-pi05-vla-only-goal-s42-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T04:30:16.021Z\\\", \\\"updated_at\\\": \\\"2026-05-25T07:25:21.880Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline Goal s42 on bjb1-18228. 跨模型验证的 baseline。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_pi05_seed42_paired.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu_ids\\\": [\\\"cuda:2\\\"], \\\"pid\\\": 446717, \\\"log_path\\\": \\\"/tmp/eval-pi05-vla-only-goal-s42-paired.log\\\", \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"timeout\\\": 18000, \\\"account\\\": \\\"root\\\", \\\"gpu\\\": \\\"cuda:2\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.98, \\\"successes\\\": 196, \\\"total\\\": 200, \\\"mode\\\": \\\"vla_only\\\", \\\"benchmark\\\": \\\"goal\\\", \\\"seed\\\": 42, \\\"model\\\": \\\"pi05\\\"}}, \\\"eval-pi05-vla-only-spatial-s42-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T04:30:12.187Z\\\", \\\"updated_at\\\": \\\"2026-05-25T07:25:18.287Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline Spatial s42 on bjb1-18228. 跨模型验证的 baseline，与后续 π0.5 Adaptive 同服务器配对。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_pi05_seed42_paired.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 446358, \\\"log_path\\\": \\\"/tmp/eval-pi05-vla-only-spatial-s42-paired.log\\\", \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"timeout\\\": 18000, \\\"account\\\": \\\"root\\\", \\\"gpu\\\": \\\"cuda:1\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.98, \\\"successes\\\": 196, \\\"total\\\": 200, \\\"mode\\\": \\\"vla_only\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"seed\\\": 42, \\\"model\\\": \\\"pi05\\\"}}, \\\"eval-pi05-adaptive-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T05:23:29.843Z\\\", \\\"updated_at\\\": \\\"2026-05-25T07:25:06.005Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive CRM (K=2, τ=0.25) on Spatial s42. 跨模型验证：π0.5 是否也能从 uncertainty gating 获益。Spatial trigger rate 最高，最可能看到效应。\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --output_file logs/eval_spatial_adaptive_pi05_seed42.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\\", \\\"eval_data\\\": \\\"spatial\\\", \\\"gpu\\\": \\\"cuda:0\\\"}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-k2-goal-vla-only-s47-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:08:33.713Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:10:13.903Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Goal s47, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 47 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed47_paired.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"smolvla_libero (no CRM)\\\", \\\"eval_data\\\": \\\"LIBERO-goal 10 tasks x 20 rollouts\\\", \\\"log_path\\\": \\\"logs/eval_goal_vla_only_seed47_paired.log\\\"}}, \\\"eval-k2-goal-adapt-s47-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:08:28.049Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:10:06.863Z\\\", \\\"hypothesis\\\": \\\"K=2 Adaptive CRM (tau=0.25) on Goal s47, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test and trigger rate correlation.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed47_paired.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-goal 10 tasks x 20 rollouts\\\", \\\"log_path\\\": \\\"logs/eval_goal_adaptive_k2_tau025_seed47_paired.log\\\"}}, \\\"eval-k2-goal-vla-only-s46-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:08:23.483Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:09:59.793Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Goal s46, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 46 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed46_paired.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"smolvla_libero (no CRM)\\\", \\\"eval_data\\\": \\\"LIBERO-goal 10 tasks x 20 rollouts\\\", \\\"log_path\\\": \\\"logs/eval_goal_vla_only_seed46_paired.log\\\"}}, \\\"eval-k2-goal-adapt-s46-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:08:19.812Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:09:52.461Z\\\", \\\"hypothesis\\\": \\\"K=2 Adaptive CRM (tau=0.25) on Goal s46, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test and trigger rate correlation.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed46_paired.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-goal 10 tasks x 20 rollouts\\\", \\\"log_path\\\": \\\"logs/eval_goal_adaptive_k2_tau025_seed46_paired.log\\\"}}, \\\"eval-k2-goal-vla-only-s45-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:08:15.041Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:09:45.415Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Goal s45, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 45 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed45_paired.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"smolvla_libero (no CRM)\\\", \\\"eval_data\\\": \\\"LIBERO-goal 10 tasks x 20 rollouts\\\", \\\"log_path\\\": \\\"logs/eval_goal_vla_only_seed45_paired.log\\\"}}, \\\"eval-k2-goal-adapt-s45-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:08:05.643Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:09:37.026Z\\\", \\\"hypothesis\\\": \\\"K=2 Adaptive CRM (tau=0.25) on Goal s45, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test and trigger rate correlation.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 45 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed45_paired.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-goal 10 tasks x 20 rollouts\\\", \\\"log_path\\\": \\\"logs/eval_goal_adaptive_k2_tau025_seed45_paired.log\\\"}}, \\\"eval-k2-spatial-vla-only-s44-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:05:39.553Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:08:09.387Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial s44, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 44, \\\"model_name\\\": \\\"smolvla\\\", \\\"data_path\\\": \\\"LIBERO spatial (10 tasks)\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO spatial\\\", \\\"log_path\\\": \\\"logs/eval_spatial_vla_only_seed44_paired_r2.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}}, \\\"eval-k2-spatial-adapt-s44-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:05:33.724Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:07:58.295Z\\\", \\\"hypothesis\\\": \\\"K=2 Adaptive CRM (τ=0.25) on Spatial s44, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 44, \\\"model_name\\\": \\\"smolvla\\\", \\\"data_path\\\": \\\"LIBERO spatial (10 tasks)\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO spatial\\\", \\\"log_path\\\": \\\"logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}}, \\\"eval-k2-spatial-vla-only-s43-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:05:27.742Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:07:48.981Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial s43, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 43, \\\"model_name\\\": \\\"smolvla\\\", \\\"data_path\\\": \\\"LIBERO spatial (10 tasks)\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO spatial\\\", \\\"log_path\\\": \\\"logs/eval_spatial_vla_only_seed43_paired_r2.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}}, \\\"eval-k2-spatial-adapt-s43-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:05:21.430Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:07:39.847Z\\\", \\\"hypothesis\\\": \\\"K=2 Adaptive CRM (τ=0.25) on Spatial s43, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 43, \\\"model_name\\\": \\\"smolvla\\\", \\\"data_path\\\": \\\"LIBERO spatial (10 tasks)\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO spatial\\\", \\\"log_path\\\": \\\"logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}}, \\\"eval-k2-spatial-vla-only-s42-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:05:14.262Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:07:27.518Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial s42, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 42, \\\"model_name\\\": \\\"smolvla\\\", \\\"data_path\\\": \\\"LIBERO spatial (10 tasks)\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO spatial\\\", \\\"log_path\\\": \\\"logs/eval_spatial_vla_only_seed42_paired_r2.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}}, \\\"eval-k2-spatial-adapt-s42-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:05:08.065Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:07:15.816Z\\\", \\\"hypothesis\\\": \\\"K=2 Adaptive CRM (τ=0.25) on Spatial s42, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 42, \\\"model_name\\\": \\\"smolvla\\\", \\\"data_path\\\": \\\"LIBERO spatial (10 tasks)\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO spatial\\\", \\\"log_path\\\": \\\"logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}}, \\\"eval-k2-tau0075-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T04:09:13.381Z\\\", \\\"updated_at\\\": \\\"2026-05-25T04:10:58.696Z\\\", \\\"hypothesis\\\": \\\"K=2 τ-sweep 补点: τ=0.075 Adaptive Conformal on Spatial s42。τ-sweep 图中该点是 SR 峰值(81.0%)，supplementary figure 需要。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.075 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"data_path\\\": \\\"libero/spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-k2-tau0075-spatial-s42.log\\\", \\\"pid\\\": 349399}}, \\\"eval-vla-only-spatial-cqa1-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T02:53:41.130Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:57:12.230Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline Spatial s44 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"smolvla_base\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log\\\", \\\"tmux_session\\\": \\\"eval-vla-only-spatial-cqa1-s44\\\"}}, \\\"eval-k2-adaptive-spatial-s49\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T02:53:04.109Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:57:05.394Z\\\", \\\"hypothesis\\\": \\\"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是 Adaptive 方法设计的正确采样数（两次前向推理算 L2 距离做 gating）。配对 bjb1-32546 VLA-only baseline 用于 paired t-test。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial (20 rollouts)\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"tmux_session\\\": \\\"eval-k2-adaptive-spatial-s49\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s49.log\\\"}}, \\\"eval-vla-only-spatial-cqa1-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T02:53:33.714Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:56:58.821Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline Spatial s43 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"smolvla_base\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log\\\", \\\"tmux_session\\\": \\\"eval-vla-only-spatial-cqa1-s43\\\"}}, \\\"eval-k2-adaptive-spatial-s48\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T02:52:50.570Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:56:52.010Z\\\", \\\"hypothesis\\\": \\\"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是 Adaptive 方法设计的正确采样数（两次前向推理算 L2 距离做 gating）。配对 bjb1-32546 VLA-only baseline 用于 paired t-test。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 48, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial (20 rollouts)\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"tmux_session\\\": \\\"eval-k2-adaptive-spatial-s48\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s48.log\\\"}}, \\\"eval-vla-only-spatial-cqa1-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T02:53:26.220Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:56:45.258Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline Spatial s42 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"smolvla_base\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log\\\", \\\"tmux_session\\\": \\\"eval-vla-only-spatial-cqa1-s42\\\"}}, \\\"eval-k2-adaptive-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T02:52:46.638Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:56:38.633Z\\\", \\\"hypothesis\\\": \\\"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是 Adaptive 方法设计的正确采样数（两次前向推理算 L2 距离做 gating）。配对 bjb1-32546 VLA-only baseline 用于 paired t-test。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 46 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial (20 rollouts)\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"tmux_session\\\": \\\"eval-k2-adaptive-spatial-s46\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s46.log\\\"}}, \\\"eval-k2-adaptive-spatial-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T02:53:18.842Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:56:32.450Z\\\", \\\"hypothesis\\\": \\\"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log\\\", \\\"tmux_session\\\": \\\"eval-k2-adaptive-spatial-s44\\\"}}, \\\"eval-k2-adaptive-spatial-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T02:53:11.261Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:56:24.240Z\\\", \\\"hypothesis\\\": \\\"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log\\\", \\\"tmux_session\\\": \\\"eval-k2-adaptive-spatial-s43\\\"}}, \\\"eval-k2-adaptive-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T02:52:57.415Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:56:08.049Z\\\", \\\"hypothesis\\\": \\\"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log\\\", \\\"tmux_session\\\": \\\"eval-k2-adaptive-spatial-s42\\\"}}, \\\"eval-k10-tau025-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T00:03:58.063Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:50:55.056Z\\\", \\\"hypothesis\\\": \\\"Re-run s46 Adaptive Conformal with K=10 (τ=0.25) on Spatial on cqa1-32758 for same-server pairing. Audit confirmed s46 used K=2. Ensures uniform K=10 across all 8 seeds for valid paired t-test.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 46 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"/root/acr-vla-conformal-refinement\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-k10-tau025-spatial-s46.log\\\", \\\"tmux_session\\\": \\\"eval-k10-tau025-spatial-s46\\\"}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s49\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T23:05:04.837Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:50:51.380Z\\\", \\\"hypothesis\\\": \\\"Canonical K=10 Adaptive Conformal (τ=0.25) on Spatial s49. Same-server data for paired t-test. Resubmit after timeout failure on cqa1.\\\", \\\"spec\\\": {\\\"command\\\": \\\"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s49 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s49.log'\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"211568\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s49.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T23:07:38.344Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"eval-canonical-adaptive-k10-spatial-s49\\\", \\\"timeout_seconds\\\": 18000}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s48\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T23:05:01.412Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:50:46.676Z\\\", \\\"hypothesis\\\": \\\"Canonical K=10 Adaptive Conformal (τ=0.25) on Spatial s48. Same-server data for paired t-test. Resubmit after timeout failure on cqa1.\\\", \\\"spec\\\": {\\\"command\\\": \\\"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s48 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s48.log'\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"210816\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s48.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T23:07:31.869Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 48, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"eval-canonical-adaptive-k10-spatial-s48\\\", \\\"timeout_seconds\\\": 18000}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T23:04:57.826Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:50:42.958Z\\\", \\\"hypothesis\\\": \\\"Canonical K=10 Adaptive Conformal (τ=0.25) on Spatial s44. Same-server data for paired t-test. Resubmit after timeout failure on cqa1.\\\", \\\"spec\\\": {\\\"command\\\": \\\"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s44 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=5 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s44.log'\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"210458\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s44.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T23:07:25.453Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"eval-canonical-adaptive-k10-spatial-s44\\\", \\\"timeout_seconds\\\": 18000}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T23:04:54.331Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:50:39.342Z\\\", \\\"hypothesis\\\": \\\"Canonical K=10 Adaptive Conformal (τ=0.25) on Spatial s43. Same-server data for paired t-test. Resubmit after timeout failure on cqa1.\\\", \\\"spec\\\": {\\\"command\\\": \\\"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s43 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=4 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s43.log'\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"210181\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T23:07:19.023Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"eval-canonical-adaptive-k10-spatial-s43\\\", \\\"timeout_seconds\\\": 18000}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-long-adaptive-k10-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T02:38:19.450Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:50:33.644Z\\\", \\\"hypothesis\\\": \\\"Long Adaptive K=10 (τ=0.25) 补跑。原 Long 实验使用 K=2 与 Spatial/Goal/Object (K=10) 不一致。补跑确保 Table 1 全 suite 统一 K=10 方法。Long Δ≈0 是预期的。\\\", \\\"parent\\\": \\\"eval-supp-long-adapt-tau025-s44\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 10\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_long\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_long\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s44.log\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"tmux_session\\\": \\\"eval-long-adaptive-k10-s44\\\"}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-long-adaptive-k10-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T02:38:15.859Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:50:29.100Z\\\", \\\"hypothesis\\\": \\\"Long Adaptive K=10 (τ=0.25) 补跑。原 Long 实验使用 K=2 与 Spatial/Goal/Object (K=10) 不一致。补跑确保 Table 1 全 suite 统一 K=10 方法。Long Δ≈0 是预期的。\\\", \\\"parent\\\": \\\"eval-supp-long-adapt-tau025-s43\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 10\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_long\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_long\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s43.log\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"tmux_session\\\": \\\"eval-long-adaptive-k10-s43\\\"}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-long-adaptive-k10-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T02:38:11.212Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:50:25.359Z\\\", \\\"hypothesis\\\": \\\"Long Adaptive K=10 (τ=0.25) 补跑。原 Long 实验使用 K=2 与 Spatial/Goal/Object (K=10) 不一致。补跑确保 Table 1 全 suite 统一 K=10 方法。Long Δ≈0 是预期的。\\\", \\\"parent\\\": \\\"eval-supp-long-adapt-tau025-s42\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --K 10\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_long\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_long\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s42.log\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"tmux_session\\\": \\\"eval-long-adaptive-k10-s42\\\"}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-k10-tau025-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T00:24:29.423Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:50:21.717Z\\\", \\\"hypothesis\\\": \\\"Re-run s47 Adaptive Conformal with K=10 (τ=0.25) on Spatial on cqa1-32758 for same-server pairing. Ensures uniform K=10 + same-server across all 8 seeds for valid paired t-test.\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\"}, \\\"notes\\\": \\\"2026-05-25 09:18: Killed first attempt (timeout=7200s, would have timed out). Resubmitted with timeout=18000s on cqa1-32758 cuda:1 in tmux eval-k10-tau025-spatial-s47.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-k10-tau025-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T00:24:16.535Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:50:17.943Z\\\", \\\"hypothesis\\\": \\\"Re-run s45 Adaptive Conformal with K=10 (τ=0.25) on Spatial on cqa1-32758 for same-server pairing. Previous s45 data likely from K=2 run. Ensures uniform K=10 across all 8 seeds for valid paired t-test.\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 45 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\"}, \\\"notes\\\": \\\"2026-05-25 09:18: Killed first attempt (timeout=7200s, would have timed out). Resubmitted with timeout=18000s on cqa1-32758 cuda:0 in tmux eval-k10-tau025-spatial-s45.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T23:04:50.613Z\\\", \\\"updated_at\\\": \\\"2026-05-25T02:50:14.144Z\\\", \\\"hypothesis\\\": \\\"Canonical same-server Adaptive K=10 on cqa1-32758 Spatial s42. Eliminates cross-server confound — paired with cqa1 VLA-only baseline for clean paired t-test.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"209904\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-canonical-adaptive-k10-spatial-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T23:07:09.098Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\", \\\"tmux_session\\\": \\\"eval-canonical-adaptive-k10-spatial-s42\\\", \\\"timeout_s\\\": 18000}, \\\"notes\\\": \\\"2026-05-25 09:22: Resubmitted after timeout=7200s failure. Now timeout=18000s on cqa1-32758 cuda:2 in tmux eval-canonical-adaptive-k10-spatial-s42.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-vla-only-spatial-bjb1-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T01:36:53.772Z\\\", \\\"updated_at\\\": \\\"2026-05-25T01:37:21.767Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial s46 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 46 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"model_name\\\": \\\"SmolVLA\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 46}}, \\\"eval-vla-only-spatial-bjb1-s49\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T01:32:07.247Z\\\", \\\"updated_at\\\": \\\"2026-05-25T01:32:46.520Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial s49 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"model_name\\\": \\\"SmolVLA\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 49}}, \\\"eval-vla-only-spatial-bjb1-s48\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T01:32:03.658Z\\\", \\\"updated_at\\\": \\\"2026-05-25T01:32:39.435Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial s48 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"model_name\\\": \\\"SmolVLA\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 48}}, \\\"eval-k2-tau010-spatial-s42-r3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T00:52:49.412Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:54:58.601Z\\\", \\\"hypothesis\\\": \\\"K=2 τ-sweep: τ=0.10 Adaptive Conformal on Spatial s42. Retry #3 on bjb2-28827 with 14400s timeout. Prior attempts timed out due to insufficient timeout and GPU contention on bjb2-40593.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.10 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 42, \\\"log_path\\\": \\\"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau010-spatial-s42-r3.log\\\", \\\"tmux_session\\\": \\\"eval-k2-tau010-spatial-s42-r3\\\", \\\"timeout\\\": 14400}}, \\\"eval-k2-tau015-spatial-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T00:52:41.760Z\\\", \\\"updated_at\\\": \\\"2026-05-25T00:54:51.278Z\\\", \\\"hypothesis\\\": \\\"K=2 τ-sweep: τ=0.15 Adaptive Conformal on Spatial s42. Retry on bjb2-28827 with 14400s timeout after first attempt timed out on bjb2-40593 (7200s, completed only 4/10 tasks).\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.15 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 42, \\\"log_path\\\": \\\"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau015-spatial-s42-r2.log\\\", \\\"tmux_session\\\": \\\"eval-k2-tau015-spatial-s42-r2\\\", \\\"timeout\\\": 14400}}, \\\"precompute-pi05-long-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:18:31.140Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:23:39.262Z\\\", \\\"hypothesis\\\": \\\"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": 114507, \\\"data_path\\\": \\\"/root/autodl-tmp/crm_cache_pi05_2048/long/\\\", \\\"data_count\\\": 136090, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\\\"}}}, \\\"count\\\": 45, \\\"total\\\": 45, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.2149}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-s43-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:34:11.243Z\", \"updated_at\": \"2026-05-25T07:34:51.098Z\", \"hypothesis\": \"π0.5 VLA-only baseline rerun on LIBERO-Spatial s43 (bjb1-18228 cuda:2). Redundant replication on a different server to fill idle GPU; prior run (-s43) reached 0.96 success rate on bjb1-32546.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_pi05_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"485043\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"backend\": \"nohup\", \"account\": \"root\"}}, \"eval-pi05-vla-only-object-s42-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:34:04.734Z\", \"updated_at\": \"2026-05-25T07:34:43.804Z\", \"hypothesis\": \"π0.5 VLA-only baseline rerun on LIBERO-Object s42 (bjb1-18228 cuda:1). Redundant replication on a different server to fill idle GPU; prior run (-s42) reached 0.965 success rate on bjb1-32546.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"484670\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\", \"backend\": \"nohup\", \"account\": \"root\"}}, \"eval-pi05-adaptive-spatial-s42-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:32:29.311Z\", \"updated_at\": \"2026-05-25T07:33:45.816Z\", \"hypothesis\": \"π0.5 Adaptive CRM (K=2, τ=0.25) on LIBERO-Spatial s42. Retry of failed s42 run: CRM checkpoint trained with unified_obs_dim=2088 (2048D PI05 features padded by 40); previous run used default obs_dim=960 causing input_mean shape mismatch [2118] vs [990]. Now passing --obs_dim 2048 --unified_obs_dim 2088 to match training-time CRM input.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --output_file logs/eval_spatial_adaptive_pi05_seed42_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"484286\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_pi05_seed42_r2.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"backend\": \"nohup\", \"account\": \"root\"}}, \"eval-pi05-vla-only-goal-s42-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T04:30:16.021Z\", \"updated_at\": \"2026-05-25T07:25:21.880Z\", \"hypothesis\": \"π0.5 VLA-only baseline Goal s42 on bjb1-18228. 跨模型验证的 baseline。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_pi05_seed42_paired.json\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:2\"], \"pid\": 446717, \"log_path\": \"/tmp/eval-pi05-vla-only-goal-s42-paired.log\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"timeout\": 18000, \"account\": \"root\", \"gpu\": \"cuda:2\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200, \"mode\": \"vla_only\", \"benchmark\": \"goal\", \"seed\": 42, \"model\": \"pi05\"}}, \"eval-pi05-vla-only-spatial-s42-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T04:30:12.187Z\", \"updated_at\": \"2026-05-25T07:25:18.287Z\", \"hypothesis\": \"π0.5 VLA-only baseline Spatial s42 on bjb1-18228. 跨模型验证的 baseline，与后续 π0.5 Adaptive 同服务器配对。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_pi05_seed42_paired.json\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 446358, \"log_path\": \"/tmp/eval-pi05-vla-only-spatial-s42-paired.log\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"timeout\": 18000, \"account\": \"root\", \"gpu\": \"cuda:1\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200, \"mode\": \"vla_only\", \"benchmark\": \"spatial\", \"seed\": 42, \"model\": \"pi05\"}}, \"eval-pi05-adaptive-spatial-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:23:29.843Z\", \"updated_at\": \"2026-05-25T07:25:06.005Z\", \"hypothesis\": \"π0.5 Adaptive CRM (K=2, τ=0.25) on Spatial s42. 跨模型验证：π0.5 是否也能从 uncertainty gating 获益。Spatial trigger rate 最高，最可能看到效应。\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --output_file logs/eval_spatial_adaptive_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"spatial\", \"gpu\": \"cuda:0\"}, \"conclusion\": \"failed\"}, \"eval-k2-goal-vla-only-s47-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:08:33.713Z\", \"updated_at\": \"2026-05-25T06:10:13.903Z\", \"hypothesis\": \"VLA-only baseline on Goal s47, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 47 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed47_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"smolvla_libero (no CRM)\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_vla_only_seed47_paired.log\"}}, \"eval-k2-goal-adapt-s47-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:08:28.049Z\", \"updated_at\": \"2026-05-25T06:10:06.863Z\", \"hypothesis\": \"K=2 Adaptive CRM (tau=0.25) on Goal s47, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test and trigger rate correlation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed47_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_adaptive_k2_tau025_seed47_paired.log\"}}, \"eval-k2-goal-vla-only-s46-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:08:23.483Z\", \"updated_at\": \"2026-05-25T06:09:59.793Z\", \"hypothesis\": \"VLA-only baseline on Goal s46, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 46 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed46_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"smolvla_libero (no CRM)\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_vla_only_seed46_paired.log\"}}, \"eval-k2-goal-adapt-s46-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:08:19.812Z\", \"updated_at\": \"2026-05-25T06:09:52.461Z\", \"hypothesis\": \"K=2 Adaptive CRM (tau=0.25) on Goal s46, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test and trigger rate correlation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed46_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_adaptive_k2_tau025_seed46_paired.log\"}}, \"eval-k2-goal-vla-only-s45-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:08:15.041Z\", \"updated_at\": \"2026-05-25T06:09:45.415Z\", \"hypothesis\": \"VLA-only baseline on Goal s45, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 45 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed45_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"smolvla_libero (no CRM)\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_vla_only_seed45_paired.log\"}}, \"eval-k2-goal-adapt-s45-paired\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:08:05.643Z\", \"updated_at\": \"2026-05-25T06:09:37.026Z\", \"hypothesis\": \"K=2 Adaptive CRM (tau=0.25) on Goal s45, same-server paired on bjb2-28827. Extends Goal seed coverage for paired t-test and trigger rate correlation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 45 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed45_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_adaptive_k2_tau025_seed45_paired.log\"}}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:39.553Z\", \"updated_at\": \"2026-05-25T06:08:09.387Z\", \"hypothesis\": \"VLA-only baseline on Spatial s44, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed44_paired_r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-k2-spatial-adapt-s44-paired-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:33.724Z\", \"updated_at\": \"2026-05-25T06:07:58.295Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s44, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:27.742Z\", \"updated_at\": \"2026-05-25T06:07:48.981Z\", \"hypothesis\": \"VLA-only baseline on Spatial s43, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed43_paired_r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-k2-spatial-adapt-s43-paired-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:21.430Z\", \"updated_at\": \"2026-05-25T06:07:39.847Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s43, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:14.262Z\", \"updated_at\": \"2026-05-25T06:07:27.518Z\", \"hypothesis\": \"VLA-only baseline on Spatial s42, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed42_paired_r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-k2-spatial-adapt-s42-paired-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:08.065Z\", \"updated_at\": \"2026-05-25T06:07:15.816Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s42, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-k2-tau0075-spatial-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T04:09:13.381Z\", \"updated_at\": \"2026-05-25T04:10:58.696Z\", \"hypothesis\": \"K=2 τ-sweep 补点: τ=0.075 Adaptive Conformal on Spatial s42。τ-sweep 图中该点是 SR 峰值(81.0%)，supplementary figure 需要。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.075 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-40593\", \"data_path\": \"libero/spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-tau0075-spatial-s42.log\", \"pid\": 349399}}, \"eval-vla-only-spatial-cqa1-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:41.130Z\", \"updated_at\": \"2026-05-25T02:57:12.230Z\", \"hypothesis\": \"VLA-only baseline Spatial s44 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s44\"}}, \"eval-k2-adaptive-spatial-s49\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:04.109Z\", \"updated_at\": \"2026-05-25T02:57:05.394Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是 Adaptive 方法设计的正确采样数（两次前向推理算 L2 距离做 gating）。配对 bjb1-32546 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial (20 rollouts)\", \"gpu\": \"cuda:3\", \"tmux_session\": \"eval-k2-adaptive-spatial-s49\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s49.log\"}}, \"eval-vla-only-spatial-cqa1-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:33.714Z\", \"updated_at\": \"2026-05-25T02:56:58.821Z\", \"hypothesis\": \"VLA-only baseline Spatial s43 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s43\"}}, \"eval-k2-adaptive-spatial-s48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:52:50.570Z\", \"updated_at\": \"2026-05-25T02:56:52.010Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是 Adaptive 方法设计的正确采样数（两次前向推理算 L2 距离做 gating）。配对 bjb1-32546 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial (20 rollouts)\", \"gpu\": \"cuda:2\", \"tmux_session\": \"eval-k2-adaptive-spatial-s48\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s48.log\"}}, \"eval-vla-only-spatial-cqa1-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:26.220Z\", \"updated_at\": \"2026-05-25T02:56:45.258Z\", \"hypothesis\": \"VLA-only baseline Spatial s42 on cqa1-32758. 同服务器配对数据用于 K=2 Adaptive paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s42\"}}, \"eval-k2-adaptive-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:52:46.638Z\", \"updated_at\": \"2026-05-25T02:56:38.633Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是 Adaptive 方法设计的正确采样数（两次前向推理算 L2 距离做 gating）。配对 bjb1-32546 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 46 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial (20 rollouts)\", \"gpu\": \"cuda:0\", \"tmux_session\": \"eval-k2-adaptive-spatial-s46\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s46.log\"}}, \"eval-k2-adaptive-spatial-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:18.842Z\", \"updated_at\": \"2026-05-25T02:56:32.450Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s44\"}}, \"eval-k2-adaptive-spatial-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:53:11.261Z\", \"updated_at\": \"2026-05-25T02:56:24.240Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s43\"}}, \"eval-k2-adaptive-spatial-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:52:57.415Z\", \"updated_at\": \"2026-05-25T02:56:08.049Z\", \"hypothesis\": \"K=2 Adaptive Spatial (τ=0.25) 同服务器配对。K=2 是正确采样数（两次前向推理算 L2 距离做 gating）。配对 cqa1-32758 VLA-only baseline 用于 paired t-test。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s42\"}}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:03:58.063Z\", \"updated_at\": \"2026-05-25T02:50:55.056Z\", \"hypothesis\": \"Re-run s46 Adaptive Conformal with K=10 (τ=0.25) on Spatial on cqa1-32758 for same-server pairing. Audit confirmed s46 used K=2. Ensures uniform K=10 across all 8 seeds for valid paired t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 46 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k10-tau025-spatial-s46.log\", \"tmux_session\": \"eval-k10-tau025-spatial-s46\"}, \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T23:05:04.837Z\", \"updated_at\": \"2026-05-25T02:50:51.380Z\", \"hypothesis\": \"Canonical K=10 Adaptive Conformal (τ=0.25) on Spatial s49. Same-server data for paired t-test. Resubmit after timeout failure on cqa1.\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s49 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s49.log'\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"211568\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s49.log\", \"submitted_at\": \"2026-05-24T23:07:38.344Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s49\", \"timeout_seconds\": 18000}, \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T23:05:01.412Z\", \"updated_at\": \"2026-05-25T02:50:46.676Z\", \"hypothesis\": \"Canonical K=10 Adaptive Conformal (τ=0.25) on Spatial s48. Same-server data for paired t-test. Resubmit after timeout failure on cqa1.\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s48 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s48.log'\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"210816\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s48.log\", \"submitted_at\": \"2026-05-24T23:07:31.869Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s48\", \"timeout_seconds\": 18000}, \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T23:04:57.826Z\", \"updated_at\": \"2026-05-25T02:50:42.958Z\", \"hypothesis\": \"Canonical K=10 Adaptive Conformal (τ=0.25) on Spatial s44. Same-server data for paired t-test. Resubmit after timeout failure on cqa1.\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s44 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=5 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s44.log'\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"210458\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s44.log\", \"submitted_at\": \"2026-05-24T23:07:25.453Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s44\", \"timeout_seconds\": 18000}, \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T23:04:54.331Z\", \"updated_at\": \"2026-05-25T02:50:39.342Z\", \"hypothesis\": \"Canonical K=10 Adaptive Conformal (τ=0.25) on Spatial s43. Same-server data for paired t-test. Resubmit after timeout failure on cqa1.\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s43 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=4 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s43.log'\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"210181\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s43.log\", \"submitted_at\": \"2026-05-24T23:07:19.023Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s43\", \"timeout_seconds\": 18000}, \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:38:19.450Z\", \"updated_at\": \"2026-05-25T02:50:33.644Z\", \"hypothesis\": \"Long Adaptive K=10 (τ=0.25) 补跑。原 Long 实验使用 K=2 与 Spatial/Goal/Object (K=10) 不一致。补跑确保 Table 1 全 suite 统一 K=10 方法。Long Δ≈0 是预期的。\", \"parent\": \"eval-supp-long-adapt-tau025-s44\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 10\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_long\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_long\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s44.log\", \"gpu\": \"cuda:5\", \"tmux_session\": \"eval-long-adaptive-k10-s44\"}, \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:38:15.859Z\", \"updated_at\": \"2026-05-25T02:50:29.100Z\", \"hypothesis\": \"Long Adaptive K=10 (τ=0.25) 补跑。原 Long 实验使用 K=2 与 Spatial/Goal/Object (K=10) 不一致。补跑确保 Table 1 全 suite 统一 K=10 方法。Long Δ≈0 是预期的。\", \"parent\": \"eval-supp-long-adapt-tau025-s43\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 10\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_long\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_long\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s43.log\", \"gpu\": \"cuda:4\", \"tmux_session\": \"eval-long-adaptive-k10-s43\"}, \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:38:11.212Z\", \"updated_at\": \"2026-05-25T02:50:25.359Z\", \"hypothesis\": \"Long Adaptive K=10 (τ=0.25) 补跑。原 Long 实验使用 K=2 与 Spatial/Goal/Object (K=10) 不一致。补跑确保 Table 1 全 suite 统一 K=10 方法。Long Δ≈0 是预期的。\", \"parent\": \"eval-supp-long-adapt-tau025-s42\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --K 10\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_long\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_long\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s42.log\", \"gpu\": \"cuda:3\", \"tmux_session\": \"eval-long-adaptive-k10-s42\"}, \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:24:29.423Z\", \"updated_at\": \"2026-05-25T02:50:21.717Z\", \"hypothesis\": \"Re-run s47 Adaptive Conformal with K=10 (τ=0.25) on Spatial on cqa1-32758 for same-server pairing. Ensures uniform K=10 + same-server across all 8 seeds for valid paired t-test.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\"}, \"notes\": \"2026-05-25 09:18: Killed first attempt (timeout=7200s, would have timed out). Resubmitted with timeout=18000s on cqa1-32758 cuda:1 in tmux eval-k10-tau025-spatial-s47.\", \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:24:16.535Z\", \"updated_at\": \"2026-05-25T02:50:17.943Z\", \"hypothesis\": \"Re-run s45 Adaptive Conformal with K=10 (τ=0.25) on Spatial on cqa1-32758 for same-server pairing. Previous s45 data likely from K=2 run. Ensures uniform K=10 across all 8 seeds for valid paired t-test.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 45 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\"}, \"notes\": \"2026-05-25 09:18: Killed first attempt (timeout=7200s, would have timed out). Resubmitted with timeout=18000s on cqa1-32758 cuda:0 in tmux eval-k10-tau025-spatial-s45.\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T23:04:50.613Z\", \"updated_at\": \"2026-05-25T02:50:14.144Z\", \"hypothesis\": \"Canonical same-server Adaptive K=10 on cqa1-32758 Spatial s42. Eliminates cross-server confound — paired with cqa1 VLA-only baseline for clean paired t-test.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"pid\": \"209904\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-canonical-adaptive-k10-spatial-s42.log\", \"submitted_at\": \"2026-05-24T23:07:09.098Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s42\", \"timeout_s\": 18000}, \"notes\": \"2026-05-25 09:22: Resubmitted after timeout=7200s failure. Now timeout=18000s on cqa1-32758 cuda:2 in tmux eval-canonical-adaptive-k10-spatial-s42.\", \"conclusion\": \"killed\"}, \"eval-vla-only-spatial-bjb1-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:36:53.772Z\", \"updated_at\": \"2026-05-25T01:37:21.767Z\", \"hypothesis\": \"VLA-only baseline on Spatial s46 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 46 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 46}}, \"eval-vla-only-spatial-bjb1-s49\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:32:07.247Z\", \"updated_at\": \"2026-05-25T01:32:46.520Z\", \"hypothesis\": \"VLA-only baseline on Spatial s49 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 49}}, \"eval-vla-only-spatial-bjb1-s48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:32:03.658Z\", \"updated_at\": \"2026-05-25T01:32:39.435Z\", \"hypothesis\": \"VLA-only baseline on Spatial s48 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 48}}, \"eval-k2-tau010-spatial-s42-r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:52:49.412Z\", \"updated_at\": \"2026-05-25T00:54:58.601Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.10 Adaptive Conformal on Spatial s42. Retry #3 on bjb2-28827 with 14400s timeout. Prior attempts timed out due to insufficient timeout and GPU contention on bjb2-40593.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.10 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau010-spatial-s42-r3.log\", \"tmux_session\": \"eval-k2-tau010-spatial-s42-r3\", \"timeout\": 14400}}, \"eval-k2-tau015-spatial-s42-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:52:41.760Z\", \"updated_at\": \"2026-05-25T00:54:51.278Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.15 Adaptive Conformal on Spatial s42. Retry on bjb2-28827 with 14400s timeout after first attempt timed out on bjb2-40593 (7200s, completed only 4/10 tasks).\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.15 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau015-spatial-s42-r2.log\", \"tmux_session\": \"eval-k2-tau015-spatial-s42-r2\", \"timeout\": 14400}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:31.140Z\", \"updated_at\": \"2026-05-24T06:23:39.262Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}}, \"count\": 45, \"total\": 45, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2149}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-25T07:58:26.960Z_

<details><summary>↩ Tool result · `toolu_01VDogpc8gDcJtegqt98BoGE`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "0268e868-f085-48a2-a5c3-88a4d1d9a165",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"error: conflicting format options\\\\n\\\\nUsage:\\\\n ps [options]\\\\n\\\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\\\n for additional help text.\\\\n\\\\nFor more details see ps(1).\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T07:58:27.278Z_

<details><summary>↩ Tool result · `toolu_01AnwT7s2SUtKNFysnyj1toA`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "77a45434-1861-4e43-8bf1-da36684b4789",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"error: conflicting format options\\\\n\\\\nUsage:\\\\n ps [options]\\\\n\\\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\\\n for additional help text.\\\\n\\\\nFor more details see ps(1).\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01K6TEmVaMSUfXjnhMUvPafx`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps aux --no-headers -o pid,user,%cpu,%mem,start,command --sort=-%mem",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "979a0e49-0745-404e-93dc-4146d35f96f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDeZHpLenh18Ugsp2qhQq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 24493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2753
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

_source line 26 · 2026-05-25T07:58:27.691Z_

<details><summary>↩ Tool result · `toolu_01K6TEmVaMSUfXjnhMUvPafx`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "39592810-d224-4e97-9320-4b5803e649a4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"error: conflicting format options\\\\n\\\\nUsage:\\\\n ps [options]\\\\n\\\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\\\n for additional help text.\\\\n\\\\nFor more details see ps(1).\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XgPnMNRq184BYsZYDvkXsC`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ps aux --no-headers -o pid,user,%cpu,%mem,start,command --sort=-%mem",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "1e4442bb-a9f8-4d0f-a705-946fc5f1cfd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDeZHpLenh18Ugsp2qhQq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 24493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2753
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

_source line 28 · 2026-05-25T07:58:28.078Z_

<details><summary>↩ Tool result · `toolu_01XgPnMNRq184BYsZYDvkXsC`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "c8e93c4e-b2e3-453f-84fc-f40bf8435e9a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"error: conflicting format options\\\\n\\\\nUsage:\\\\n ps [options]\\\\n\\\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\\\n for additional help text.\\\\n\\\\nFor more details see ps(1).\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
The ps command format is wrong. Let me use a simpler grep approach to check for python processes. Also need to check specific PIDs from the registry. Let me also check the τ=0.075 experiment on bjb2-40593.

Let me now:
1. Check python processes on each server with a simpler command
2. Check specific PIDs for the old experiments
3. Check τ=0.075 result on bjb2-40593

From the registry, I have the following info about the specific old experiments the user asked about:

**bjb2-28827 old experiments** - These are NOT in the current RUNNING registry. 

Looking at what the user is asking about, those five experiments they mentioned aren't showing up in the current registry either. The registry for bjb2-28827 shows different experiments running instead - eval-k2-goal-vla-only-s47-paired and eval-k2-goal-adapt-s are what's actually there.

Now I'm checking the older bjb1-32546 experiments the user is asking about - eval-supp-spatial-k2mean-s46, eval-supp-reconvla-obj-s45, and eval-smolvla-lerobot-goal-seed43 - and these also don't appear to be in the current running list.

Looking at what's actually in the registry for bjb1-32546, I see a different set of experiments running across the GPUs: several k2-spatial variants with paired configurations at different seeds (s44, s43, s42) in both vla-only and adapt versions, plus an eval-k10-tau025-spatial-s46 job. Looking at the registry for bjb1-18228, I see several evaluation jobs currently running across different GPUs, with a few that have failed or are still in progress, and one precompute job that appears to be cut off.

The old supplementary experiments the user asked about aren't showing up in the current RUNNING registry list of 45 experiments, so they've likely already completed or moved to a different status rather than still actively running.

Now I need to check the actual processes running on each server using a simpler ps command, and also verify the τ=0.075 parameter on bjb2-40593.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "9924d11d-4e5a-4dc1-ae10-6610bbf4a5f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UB6uRrWzWfykFGQn2gRvR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20975,
      "cache_read_input_tokens": 27246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20975
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

_source line 30_

ps 格式报错，换 grep 方式查进程。同时查 τ=0.075 和旧实验状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "93adcb25-acbb-41b5-9f9b-cf7e2be35d34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UB6uRrWzWfykFGQn2gRvR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20975,
      "cache_read_input_tokens": 27246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20975
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01U14ycZ1AyfjzdU48JCDUjs`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ps aux",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "b8474bf5-b1b3-41b7-aaca-757794d57f45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UB6uRrWzWfykFGQn2gRvR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20975,
      "cache_read_input_tokens": 27246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20975
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

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EG1Bz9UGoFM5x57MzNp243`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps aux",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "f5a6344c-e462-4c6b-8764-a1c3cae3ed90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UB6uRrWzWfykFGQn2gRvR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20975,
      "cache_read_input_tokens": 27246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20975
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

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NdHNjkX7nFthSWGVLFSb1h`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps aux",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "8a094c0e-34a7-4248-acca-78c47c6ccdbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UB6uRrWzWfykFGQn2gRvR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20975,
      "cache_read_input_tokens": 27246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20975
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

_source line 34 · 2026-05-25T07:58:57.929Z_

<details><summary>↩ Tool result · `toolu_01U14ycZ1AyfjzdU48JCDUjs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  1968 ?        Ss   May13   0:02 bash /init/boot/boot.sh\\nroot        794  1.4  0.0 724128 19992 ?        Sl   May13 261:22 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        808  0.0  0.0  15444  8380 ?        S    May13   0:58 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\nroot        809  0.0  0.0 4147492 77540 ?       Sl   May13   7:46 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        814  0.0  0.0 191536 103272 ?       S    May13   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        817  0.2  0.0 5196664 99836 ?       Sl   May13  44:04 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        818  0.0  0.0 3535912 18248 ?       Sl   May13   6:08 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        819  0.1  0.0 3609132 21604 ?       Sl   May13  20:32 proxy -c /init/proxy/proxy.ini\\nroot        925  0.0  0.0 17524960 8888 ?       Sl   May13   6:36 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_vbt2aa5n/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_vbt2aa5n/startup_error\\nroot     114507  131  1.6 70675684 17065224 ?   Rl   May23 4705:18 python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\\nroot     433927  0.0  0.0  16692 10464 ?        Ss   07:58   0:04 sshd: root@notty\\nroot     484286  0.0  0.0   4364  2012 ?        S    15:29   0:00 bash -c cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 nohup python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --output_file logs/eval_spatial_adaptive_pi05_seed42_r2.json > logs/eval_spatial_adaptive_pi05_seed42_r2.log 2>&1 & echo \\\"PID=$!\\\"\\nroot     484291  240  1.2 79904208 13137712 ?   Rl   15:29  69:42 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --output_file logs/eval_spatial_adaptive_pi05_seed42_r2.json\\nroot     484670  0.0  0.0   4364  1988 ?        S    15:30   0:00 bash -c cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 nohup python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42.json > logs/eval_object_vla_only_pi05_seed42.log 2>&1 & echo \\\"PID=$!\\\"\\nroot     484675  229  0.9 65270544 10062156 ?   Rl   15:30  65:33 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42.json\\nroot     516560  0.0  0.0  16692 10508 ?        Ss   15:58   0:00 sshd: root@notty\\nroot     517259  1.0  0.0  16432  9992 ?        Ss   15:58   0:00 sshd: unknown [priv]\\nsshd     517260  0.0  0.0  15444  5476 ?        S    15:58   0:00 sshd: unknown [net]\\nroot     517262  0.0  0.0   7064  1608 ?        Rs   15:58   0:00 ps aux\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "77ca9d68-e189-4d4a-99fd-8e48a9747a89",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\\\nroot          1  0.0  0.0   4476  1968 ?        Ss   May13   0:02 bash /init/boot/boot.sh\\\\nroot        794  1.4  0.0 724128 19992 ?        Sl   May13 261:22 /bin/supervisord -c /init/supervisor/supervisor.ini\\\\nroot        808  0.0  0.0  15444  8380 ?        S    May13   0:58 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\\\nroot        809  0.0  0.0 4147492 77540 ?       Sl   May13   7:46 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\\\nroot        814  0.0  0.0 191536 103272 ?       S    May13   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\\\nroot        817  0.2  0.0 5196664 99836 ?       Sl   May13  44:04 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\\\nroot        818  0.0  0.0 3535912 18248 ?       Sl   May13   6:08 proxy -c /init/proxy/proxy-hot-backup.ini\\\\nroot        819  0.1  0.0 3609132 21604 ?       Sl   May13  20:32 proxy -c /init/proxy/proxy.ini\\\\nroot        925  0.0  0.0 17524960 8888 ?       Sl   May13   6:36 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_vbt2aa5n/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_vbt2aa5n/startup_error\\\\nroot     114507  131  1.6 70675684 17065224 ?   Rl   May23 4705:18 python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\\\\nroot     433927  0.0  0.0  16692 10464 ?        Ss   07:58   0:04 sshd: root@notty\\\\nroot     484286  0.0  0.0   4364  2012 ?        S    15:29   0:00 bash -c cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 nohup python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --output_file logs/eval_spatial_adaptive_pi05_seed42_r2.json > logs/eval_spatial_adaptive_pi05_seed42_r2.log 2>&1 & echo \\\\\\\"PID=$!\\\\\\\"\\\\nroot     484291  240  1.2 79904208 13137712 ?   Rl   15:29  69:42 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --output_file logs/eval_spatial_adaptive_pi05_seed42_r2.json\\\\nroot     484670  0.0  0.0   4364  1988 ?        S    15:30   0:00 bash -c cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 nohup python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42.json > logs/eval_object_vla_only_pi05_seed42.log 2>&1 & echo \\\\\\\"PID=$!\\\\\\\"\\\\nroot     484675  229  0.9 65270544 10062156 ?   Rl   15:30  65:33 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42.json\\\\nroot     516560  0.0  0.0  16692 10508 ?        Ss   15:58   0:00 sshd: root@notty\\\\nroot     517259  1.0  0.0  16432  9992 ?        Ss   15:58   0:00 sshd: unknown [priv]\\\\nsshd     517260  0.0  0.0  15444  5476 ?        S    15:58   0:00 sshd: unknown [net]\\\\nroot     517262  0.0  0.0   7064  1608 ?        Rs   15:58   0:00 ps aux\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  1968 ?        Ss   May13   0:02 bash /init/boot/boot.sh\\nroot        794  1.4  0.0 724128 19992 ?        Sl   May13 261:22 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        808  0.0  0.0  15444  8380 ?        S    May13   0:58 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\nroot        809  0.0  0.0 4147492 77540 ?       Sl   May13   7:46 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        814  0.0  0.0 191536 103272 ?       S    May13   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        817  0.2  0.0 5196664 99836 ?       Sl   May13  44:04 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        818  0.0  0.0 3535912 18248 ?       Sl   May13   6:08 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        819  0.1  0.0 3609132 21604 ?       Sl   May13  20:32 proxy -c /init/proxy/proxy.ini\\nroot        925  0.0  0.0 17524960 8888 ?       Sl   May13   6:36 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_vbt2aa5n/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_vbt2aa5n/startup_error\\nroot     114507  131  1.6 70675684 17065224 ?   Rl   May23 4705:18 python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\\nroot     433927  0.0  0.0  16692 10464 ?        Ss   07:58   0:04 sshd: root@notty\\nroot     484286  0.0  0.0   4364  2012 ?        S    15:29   0:00 bash -c cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 nohup python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --output_file logs/eval_spatial_adaptive_pi05_seed42_r2.json > logs/eval_spatial_adaptive_pi05_seed42_r2.log 2>&1 & echo \\\"PID=$!\\\"\\nroot     484291  240  1.2 79904208 13137712 ?   Rl   15:29  69:42 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --output_file logs/eval_spatial_adaptive_pi05_seed42_r2.json\\nroot     484670  0.0  0.0   4364  1988 ?        S    15:30   0:00 bash -c cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 nohup python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42.json > logs/eval_object_vla_only_pi05_seed42.log 2>&1 & echo \\\"PID=$!\\\"\\nroot     484675  229  0.9 65270544 10062156 ?   Rl   15:30  65:33 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42.json\\nroot     516560  0.0  0.0  16692 10508 ?        Ss   15:58   0:00 sshd: root@notty\\nroot     517259  1.0  0.0  16432  9992 ?        Ss   15:58   0:00 sshd: unknown [priv]\\nsshd     517260  0.0  0.0  15444  5476 ?        S    15:58   0:00 sshd: unknown [net]\\nroot     517262  0.0  0.0   7064  1608 ?        Rs   15:58   0:00 ps aux\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YLM4FirF9DL6U94g4PimpH`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ps aux",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "e938a6ec-b3fb-4f72-ab37-e32de7d9eba2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UB6uRrWzWfykFGQn2gRvR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20975,
      "cache_read_input_tokens": 27246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20975
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

_source line 36 · 2026-05-25T07:58:58.256Z_

<details><summary>↩ Tool result · `toolu_01EG1Bz9UGoFM5x57MzNp243`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476   316 ?        Ss   May15   0:01 bash /init/boot/boot.sh\\nroot        941  1.6  0.0 723872 23832 ?        Sl   May15 247:00 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        960  0.0  0.0 4147492 60244 ?       Sl   May15   5:56 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        963  0.0  0.0  15444  4276 ?        S    May15   0:40 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        964  0.0  0.0 190528 88376 ?        S    May15   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        965  0.3  0.0 5344128 101348 ?      Sl   May15  49:23 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        966  0.1  0.0 3536104 20080 ?       Sl   May15  28:20 proxy -c /init/proxy/proxy.ini\\nroot        967  0.0  0.0 3535144 17692 ?       Sl   May15   4:41 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1082  0.0  0.0 17524960 4608 ?       Sl   May15   5:26 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_edewh761/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_edewh761/startup_error\\nroot     510623  0.0  0.0  16692 11004 ?        Ss   07:58   0:03 sshd: root@notty\\nroot     639146  0.0  0.0   4496  3216 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=0; export MUJOCO_EGL_DEVICE_ID=0; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 45 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed45_paired.json 2>&1 | tee logs/eval_goal_adaptive_k2_tau025_seed45_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-adapt-s45-paired.sentinel\\nroot     639147  0.0  0.0   4496  3196 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=1; export MUJOCO_EGL_DEVICE_ID=1; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 45 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed45_paired.json 2>&1 | tee logs/eval_goal_vla_only_seed45_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-vla-only-s45-paired.sentinel\\nroot     639148  0.0  0.0   4496  3248 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=2; export MUJOCO_EGL_DEVICE_ID=2; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed46_paired.json 2>&1 | tee logs/eval_goal_adaptive_k2_tau025_seed46_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-adapt-s46-paired.sentinel\\nroot     639149  0.0  0.0   4496  3296 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=3; export MUJOCO_EGL_DEVICE_ID=3; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 46 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed46_paired.json 2>&1 | tee logs/eval_goal_vla_only_seed46_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-vla-only-s46-paired.sentinel\\nroot     639150  0.0  0.0   4496  3156 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=4; export MUJOCO_EGL_DEVICE_ID=4; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed47_paired.json 2>&1 | tee logs/eval_goal_adaptive_k2_tau025_seed47_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-adapt-s47-paired.sentinel\\nroot     639151  0.0  0.0   4496  3384 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=5; export MUJOCO_EGL_DEVICE_ID=5; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 47 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed47_paired.json 2>&1 | tee logs/eval_goal_vla_only_seed47_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-vla-only-s47-paired.sentinel\\nroot     639189  552  0.7 57709580 8206040 ?    Rl   14:06 623:49 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 45 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed45_paired.json\\nroot     639190  557  0.7 57754116 8189320 ?    Rl   14:06 629:26 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed46_paired.json\\nroot     639191  0.0  0.0   2796  1036 ?        S    14:06   0:00 tee logs/eval_goal_vla_only_seed45_paired.log\\nroot     639192  578  0.7 56042044 7957880 ?    Rl   14:06 652:54 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 45 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed45_paired.json\\nroot     639193  552  0.7 57737348 8322052 ?    Rl   14:06 622:55 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed47_paired.json\\nroot     639194  565  0.7 56100596 8065252 ?    Rl   14:06 638:25 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 47 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed47_paired.json\\nroot     639195  0.0  0.0   2796   992 ?        S    14:06   0:00 tee logs/eval_goal_adaptive_k2_tau025_seed46_paired.log\\nroot     639196  0.0  0.0   2796  1040 ?        S    14:06   0:00 tee logs/eval_goal_adaptive_k2_tau025_seed45_paired.log\\nroot     639197  0.0  0.0   2796  1076 ?        S    14:06   0:00 tee logs/eval_goal_adaptive_k2_tau025_seed47_paired.log\\nroot     639198  0.0  0.0   2796  1044 ?        S    14:06   0:00 tee logs/eval_goal_vla_only_seed47_paired.log\\nroot     639199  574  0.7 56025384 7804008 ?    Rl   14:06 648:46 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 46 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed46_paired.json\\nroot     639200  0.0  0.0   2796  1008 ?        S    14:06   0:00 tee logs/eval_goal_vla_only_seed46_paired.log\\nroot     711432  0.0  0.0  16692 10820 ?        Ss   15:58   0:00 sshd: root@notty\\nroot     712168  0.0  0.0   7064  1536 ?        Rs   15:58   0:00 ps aux\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "3fabe7d3-c8d6-47c2-83f8-c48f8005f6fa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\\\nroot          1  0.0  0.0   4476   316 ?        Ss   May15   0:01 bash /init/boot/boot.sh\\\\nroot        941  1.6  0.0 723872 23832 ?        Sl   May15 247:00 /bin/supervisord -c /init/supervisor/supervisor.ini\\\\nroot        960  0.0  0.0 4147492 60244 ?       Sl   May15   5:56 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\\\nroot        963  0.0  0.0  15444  4276 ?        S    May15   0:40 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\\\nroot        964  0.0  0.0 190528 88376 ?        S    May15   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\\\nroot        965  0.3  0.0 5344128 101348 ?      Sl   May15  49:23 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\\\nroot        966  0.1  0.0 3536104 20080 ?       Sl   May15  28:20 proxy -c /init/proxy/proxy.ini\\\\nroot        967  0.0  0.0 3535144 17692 ?       Sl   May15   4:41 proxy -c /init/proxy/proxy-hot-backup.ini\\\\nroot       1082  0.0  0.0 17524960 4608 ?       Sl   May15   5:26 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_edewh761/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_edewh761/startup_error\\\\nroot     510623  0.0  0.0  16692 11004 ?        Ss   07:58   0:03 sshd: root@notty\\\\nroot     639146  0.0  0.0   4496  3216 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=0; export MUJOCO_EGL_DEVICE_ID=0; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 45 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed45_paired.json 2>&1 | tee logs/eval_goal_adaptive_k2_tau025_seed45_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-adapt-s45-paired.sentinel\\\\nroot     639147  0.0  0.0   4496  3196 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=1; export MUJOCO_EGL_DEVICE_ID=1; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 45 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed45_paired.json 2>&1 | tee logs/eval_goal_vla_only_seed45_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-vla-only-s45-paired.sentinel\\\\nroot     639148  0.0  0.0   4496  3248 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=2; export MUJOCO_EGL_DEVICE_ID=2; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed46_paired.json 2>&1 | tee logs/eval_goal_adaptive_k2_tau025_seed46_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-adapt-s46-paired.sentinel\\\\nroot     639149  0.0  0.0   4496  3296 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=3; export MUJOCO_EGL_DEVICE_ID=3; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 46 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed46_paired.json 2>&1 | tee logs/eval_goal_vla_only_seed46_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-vla-only-s46-paired.sentinel\\\\nroot     639150  0.0  0.0   4496  3156 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=4; export MUJOCO_EGL_DEVICE_ID=4; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed47_paired.json 2>&1 | tee logs/eval_goal_adaptive_k2_tau025_seed47_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-adapt-s47-paired.sentinel\\\\nroot     639151  0.0  0.0   4496  3384 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=5; export MUJOCO_EGL_DEVICE_ID=5; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 47 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed47_paired.json 2>&1 | tee logs/eval_goal_vla_only_seed47_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-vla-only-s47-paired.sentinel\\\\nroot     639189  552  0.7 57709580 8206040 ?    Rl   14:06 623:49 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 45 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed45_paired.json\\\\nroot     639190  557  0.7 57754116 8189320 ?    Rl   14:06 629:26 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed46_paired.json\\\\nroot     639191  0.0  0.0   2796  1036 ?        S    14:06   0:00 tee logs/eval_goal_vla_only_seed45_paired.log\\\\nroot     639192  578  0.7 56042044 7957880 ?    Rl   14:06 652:54 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 45 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed45_paired.json\\\\nroot     639193  552  0.7 57737348 8322052 ?    Rl   14:06 622:55 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed47_paired.json\\\\nroot     639194  565  0.7 56100596 8065252 ?    Rl   14:06 638:25 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 47 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed47_paired.json\\\\nroot     639195  0.0  0.0   2796   992 ?        S    14:06   0:00 tee logs/eval_goal_adaptive_k2_tau025_seed46_paired.log\\\\nroot     639196  0.0  0.0   2796  1040 ?        S    14:06   0:00 tee logs/eval_goal_adaptive_k2_tau025_seed45_paired.log\\\\nroot     639197  0.0  0.0   2796  1076 ?        S    14:06   0:00 tee logs/eval_goal_adaptive_k2_tau025_seed47_paired.log\\\\nroot     639198  0.0  0.0   2796  1044 ?        S    14:06   0:00 tee logs/eval_goal_vla_only_seed47_paired.log\\\\nroot     639199  574  0.7 56025384 7804008 ?    Rl   14:06 648:46 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 46 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed46_paired.json\\\\nroot     639200  0.0  0.0   2796  1008 ?        S    14:06   0:00 tee logs/eval_goal_vla_only_seed46_paired.log\\\\nroot     711432  0.0  0.0  16692 10820 ?        Ss   15:58   0:00 sshd: root@notty\\\\nroot     712168  0.0  0.0   7064  1536 ?        Rs   15:58   0:00 ps aux\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476   316 ?        Ss   May15   0:01 bash /init/boot/boot.sh\\nroot        941  1.6  0.0 723872 23832 ?        Sl   May15 247:00 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        960  0.0  0.0 4147492 60244 ?       Sl   May15   5:56 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        963  0.0  0.0  15444  4276 ?        S    May15   0:40 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        964  0.0  0.0 190528 88376 ?        S    May15   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        965  0.3  0.0 5344128 101348 ?      Sl   May15  49:23 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        966  0.1  0.0 3536104 20080 ?       Sl   May15  28:20 proxy -c /init/proxy/proxy.ini\\nroot        967  0.0  0.0 3535144 17692 ?       Sl   May15   4:41 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1082  0.0  0.0 17524960 4608 ?       Sl   May15   5:26 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_edewh761/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_edewh761/startup_error\\nroot     510623  0.0  0.0  16692 11004 ?        Ss   07:58   0:03 sshd: root@notty\\nroot     639146  0.0  0.0   4496  3216 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=0; export MUJOCO_EGL_DEVICE_ID=0; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 45 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed45_paired.json 2>&1 | tee logs/eval_goal_adaptive_k2_tau025_seed45_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-adapt-s45-paired.sentinel\\nroot     639147  0.0  0.0   4496  3196 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=1; export MUJOCO_EGL_DEVICE_ID=1; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 45 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed45_paired.json 2>&1 | tee logs/eval_goal_vla_only_seed45_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-vla-only-s45-paired.sentinel\\nroot     639148  0.0  0.0   4496  3248 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=2; export MUJOCO_EGL_DEVICE_ID=2; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed46_paired.json 2>&1 | tee logs/eval_goal_adaptive_k2_tau025_seed46_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-adapt-s46-paired.sentinel\\nroot     639149  0.0  0.0   4496  3296 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=3; export MUJOCO_EGL_DEVICE_ID=3; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 46 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed46_paired.json 2>&1 | tee logs/eval_goal_vla_only_seed46_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-vla-only-s46-paired.sentinel\\nroot     639150  0.0  0.0   4496  3156 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=4; export MUJOCO_EGL_DEVICE_ID=4; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed47_paired.json 2>&1 | tee logs/eval_goal_adaptive_k2_tau025_seed47_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-adapt-s47-paired.sentinel\\nroot     639151  0.0  0.0   4496  3384 ?        S    14:06   0:00 bash -lc export CUDA_VISIBLE_DEVICES=5; export MUJOCO_EGL_DEVICE_ID=5; source /root/miniconda3/etc/profile.d/conda.sh; conda activate base; cd /root/acr-vla-conformal-refinement; python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 47 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed47_paired.json 2>&1 | tee logs/eval_goal_vla_only_seed47_paired.log; echo EXIT=${PIPESTATUS[0]} >> /tmp/goal_k2_launch/eval-k2-goal-vla-only-s47-paired.sentinel\\nroot     639189  552  0.7 57709580 8206040 ?    Rl   14:06 623:49 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 45 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed45_paired.json\\nroot     639190  557  0.7 57754116 8189320 ?    Rl   14:06 629:26 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed46_paired.json\\nroot     639191  0.0  0.0   2796  1036 ?        S    14:06   0:00 tee logs/eval_goal_vla_only_seed45_paired.log\\nroot     639192  578  0.7 56042044 7957880 ?    Rl   14:06 652:54 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 45 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed45_paired.json\\nroot     639193  552  0.7 57737348 8322052 ?    Rl   14:06 622:55 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed47_paired.json\\nroot     639194  565  0.7 56100596 8065252 ?    Rl   14:06 638:25 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 47 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed47_paired.json\\nroot     639195  0.0  0.0   2796   992 ?        S    14:06   0:00 tee logs/eval_goal_adaptive_k2_tau025_seed46_paired.log\\nroot     639196  0.0  0.0   2796  1040 ?        S    14:06   0:00 tee logs/eval_goal_adaptive_k2_tau025_seed45_paired.log\\nroot     639197  0.0  0.0   2796  1076 ?        S    14:06   0:00 tee logs/eval_goal_adaptive_k2_tau025_seed47_paired.log\\nroot     639198  0.0  0.0   2796  1044 ?        S    14:06   0:00 tee logs/eval_goal_vla_only_seed47_paired.log\\nroot     639199  574  0.7 56025384 7804008 ?    Rl   14:06 648:46 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 46 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed46_paired.json\\nroot     639200  0.0  0.0   2796  1008 ?        S    14:06   0:00 tee logs/eval_goal_vla_only_seed46_paired.log\\nroot     711432  0.0  0.0  16692 10820 ?        Ss   15:58   0:00 sshd: root@notty\\nroot     712168  0.0  0.0   7064  1536 ?        Rs   15:58   0:00 ps aux\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-25T07:58:58.619Z_

<details><summary>↩ Tool result · `toolu_01NdHNjkX7nFthSWGVLFSb1h`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  3364 ?        Ss   May15   0:01 bash /init/boot/boot.sh\\nroot        940  1.4  0.0 723360 20752 ?        Sl   May15 217:40 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        955  0.0  0.0 191548 105804 ?       S    May15   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        961  0.0  0.0 4147608 81420 ?       Sl   May15   6:18 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        962  0.0  0.0  15444  9420 ?        S    May15   0:46 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\nroot        964  0.1  0.0 3609324 22060 ?       Sl   May15  21:59 proxy -c /init/proxy/proxy.ini\\nroot        965  0.2  0.0 5342848 100176 ?      Sl   May15  38:03 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        966  0.0  0.0 3756340 18448 ?       Sl   May15   6:19 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1079  0.0  0.0 17524960 9964 ?       Sl   May15   5:26 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_q6bmzxvy/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_q6bmzxvy/startup_error\\nroot      68939  0.0  0.0  16692 10592 ?        Ss   15:58   0:00 sshd: root@notty\\nroot      69188  0.3  0.0  16432  9924 ?        Ss   15:58   0:00 sshd: unknown [priv]\\nsshd      69189  0.0  0.0  15444  5568 ?        S    15:58   0:00 sshd: unknown [net]\\nroot      69255  0.0  0.0   7064  1572 ?        Rs   15:58   0:00 ps aux\\nroot     831215  0.0  0.0  16692 10576 ?        Ss   07:53   0:02 sshd: root@notty\\nroot     978837  0.0  0.0   4496  2080 ?        S    14:00   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\\ CUDA_VISIBLE_DEVICES=0 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log 2>&1 & \\\\ CUDA_VISIBLE_DEVICES=1 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42_paired_r2.json > logs/eval_spatial_vla_only_seed42_paired_r2.log 2>&1 & \\\\ CUDA_VISIBLE_DEVICES=2 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log 2>&1 & \\\\ CUDA_VISIBLE_DEVICES=3 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed43_paired_r2.json > logs/eval_spatial_vla_only_seed43_paired_r2.log 2>&1 & \\\\ CUDA_VISIBLE_DEVICES=4 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log 2>&1 & \\\\ CUDA_VISIBLE_DEVICES=5 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed44_paired_r2.json > logs/eval_spatial_vla_only_seed44_paired_r2.log 2>&1 & \\\\ sleep 3 && echo \\\"All 6 launched\\\"\\nroot     978848  365  0.7 59324704 8317324 ?    Rl   14:00 431:38 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.json\\nroot     980366  0.0  0.0   4364  2016 ?        S    14:01   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42_paired_r2.json > logs/eval_spatial_vla_only_seed42_paired_r2.log 2>&1 &\\nroot     980371  358  0.7 59311480 8343392 ?    Rl   14:01 419:34 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42_paired_r2.json\\nroot     981558  0.0  0.0   4364  2116 ?        S    14:02   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log 2>&1 &\\nroot     981563  367  0.7 59339220 8241436 ?    Rl   14:02 427:45 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json\\nroot     984721  0.0  0.0   4364  2024 ?        S    14:03   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log 2>&1 &\\nroot     984726  361  0.7 59371628 8428672 ?    Rl   14:03 417:10 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json\\nroot     986458  0.0  0.0   4364  2092 ?        S    14:03   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed44_paired_r2.json > logs/eval_spatial_vla_only_seed44_paired_r2.log 2>&1 &\\nroot     986463  367  0.7 59293744 8271280 ?    Rl   14:03 422:28 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed44_paired_r2.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "c30c8a99-6f29-46b3-9f81-2f61d062e488",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\\\nroot          1  0.0  0.0   4476  3364 ?        Ss   May15   0:01 bash /init/boot/boot.sh\\\\nroot        940  1.4  0.0 723360 20752 ?        Sl   May15 217:40 /bin/supervisord -c /init/supervisor/supervisor.ini\\\\nroot        955  0.0  0.0 191548 105804 ?       S    May15   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\\\nroot        961  0.0  0.0 4147608 81420 ?       Sl   May15   6:18 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\\\nroot        962  0.0  0.0  15444  9420 ?        S    May15   0:46 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\\\nroot        964  0.1  0.0 3609324 22060 ?       Sl   May15  21:59 proxy -c /init/proxy/proxy.ini\\\\nroot        965  0.2  0.0 5342848 100176 ?      Sl   May15  38:03 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\\\nroot        966  0.0  0.0 3756340 18448 ?       Sl   May15   6:19 proxy -c /init/proxy/proxy-hot-backup.ini\\\\nroot       1079  0.0  0.0 17524960 9964 ?       Sl   May15   5:26 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_q6bmzxvy/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_q6bmzxvy/startup_error\\\\nroot      68939  0.0  0.0  16692 10592 ?        Ss   15:58   0:00 sshd: root@notty\\\\nroot      69188  0.3  0.0  16432  9924 ?        Ss   15:58   0:00 sshd: unknown [priv]\\\\nsshd      69189  0.0  0.0  15444  5568 ?        S    15:58   0:00 sshd: unknown [net]\\\\nroot      69255  0.0  0.0   7064  1572 ?        Rs   15:58   0:00 ps aux\\\\nroot     831215  0.0  0.0  16692 10576 ?        Ss   07:53   0:02 sshd: root@notty\\\\nroot     978837  0.0  0.0   4496  2080 ?        S    14:00   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\\\\\\ CUDA_VISIBLE_DEVICES=0 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log 2>&1 & \\\\\\\\ CUDA_VISIBLE_DEVICES=1 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42_paired_r2.json > logs/eval_spatial_vla_only_seed42_paired_r2.log 2>&1 & \\\\\\\\ CUDA_VISIBLE_DEVICES=2 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log 2>&1 & \\\\\\\\ CUDA_VISIBLE_DEVICES=3 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed43_paired_r2.json > logs/eval_spatial_vla_only_seed43_paired_r2.log 2>&1 & \\\\\\\\ CUDA_VISIBLE_DEVICES=4 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log 2>&1 & \\\\\\\\ CUDA_VISIBLE_DEVICES=5 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed44_paired_r2.json > logs/eval_spatial_vla_only_seed44_paired_r2.log 2>&1 & \\\\\\\\ sleep 3 && echo \\\\\\\"All 6 launched\\\\\\\"\\\\nroot     978848  365  0.7 59324704 8317324 ?    Rl   14:00 431:38 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.json\\\\nroot     980366  0.0  0.0   4364  2016 ?        S    14:01   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42_paired_r2.json > logs/eval_spatial_vla_only_seed42_paired_r2.log 2>&1 &\\\\nroot     980371  358  0.7 59311480 8343392 ?    Rl   14:01 419:34 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42_paired_r2.json\\\\nroot     981558  0.0  0.0   4364  2116 ?        S    14:02   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log 2>&1 &\\\\nroot     981563  367  0.7 59339220 8241436 ?    Rl   14:02 427:45 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json\\\\nroot     984721  0.0  0.0   4364  2024 ?        S    14:03   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log 2>&1 &\\\\nroot     984726  361  0.7 59371628 8428672 ?    Rl   14:03 417:10 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json\\\\nroot     986458  0.0  0.0   4364  2092 ?        S    14:03   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed44_paired_r2.json > logs/eval_spatial_vla_only_seed44_paired_r2.log 2>&1 &\\\\nroot     986463  367  0.7 59293744 8271280 ?    Rl   14:03 422:28 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed44_paired_r2.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  3364 ?        Ss   May15   0:01 bash /init/boot/boot.sh\\nroot        940  1.4  0.0 723360 20752 ?        Sl   May15 217:40 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        955  0.0  0.0 191548 105804 ?       S    May15   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        961  0.0  0.0 4147608 81420 ?       Sl   May15   6:18 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        962  0.0  0.0  15444  9420 ?        S    May15   0:46 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\nroot        964  0.1  0.0 3609324 22060 ?       Sl   May15  21:59 proxy -c /init/proxy/proxy.ini\\nroot        965  0.2  0.0 5342848 100176 ?      Sl   May15  38:03 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        966  0.0  0.0 3756340 18448 ?       Sl   May15   6:19 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1079  0.0  0.0 17524960 9964 ?       Sl   May15   5:26 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_q6bmzxvy/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_q6bmzxvy/startup_error\\nroot      68939  0.0  0.0  16692 10592 ?        Ss   15:58   0:00 sshd: root@notty\\nroot      69188  0.3  0.0  16432  9924 ?        Ss   15:58   0:00 sshd: unknown [priv]\\nsshd      69189  0.0  0.0  15444  5568 ?        S    15:58   0:00 sshd: unknown [net]\\nroot      69255  0.0  0.0   7064  1572 ?        Rs   15:58   0:00 ps aux\\nroot     831215  0.0  0.0  16692 10576 ?        Ss   07:53   0:02 sshd: root@notty\\nroot     978837  0.0  0.0   4496  2080 ?        S    14:00   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && \\\\ CUDA_VISIBLE_DEVICES=0 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log 2>&1 & \\\\ CUDA_VISIBLE_DEVICES=1 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42_paired_r2.json > logs/eval_spatial_vla_only_seed42_paired_r2.log 2>&1 & \\\\ CUDA_VISIBLE_DEVICES=2 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log 2>&1 & \\\\ CUDA_VISIBLE_DEVICES=3 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed43_paired_r2.json > logs/eval_spatial_vla_only_seed43_paired_r2.log 2>&1 & \\\\ CUDA_VISIBLE_DEVICES=4 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log 2>&1 & \\\\ CUDA_VISIBLE_DEVICES=5 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed44_paired_r2.json > logs/eval_spatial_vla_only_seed44_paired_r2.log 2>&1 & \\\\ sleep 3 && echo \\\"All 6 launched\\\"\\nroot     978848  365  0.7 59324704 8317324 ?    Rl   14:00 431:38 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.json\\nroot     980366  0.0  0.0   4364  2016 ?        S    14:01   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42_paired_r2.json > logs/eval_spatial_vla_only_seed42_paired_r2.log 2>&1 &\\nroot     980371  358  0.7 59311480 8343392 ?    Rl   14:01 419:34 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42_paired_r2.json\\nroot     981558  0.0  0.0   4364  2116 ?        S    14:02   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log 2>&1 &\\nroot     981563  367  0.7 59339220 8241436 ?    Rl   14:02 427:45 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json\\nroot     984721  0.0  0.0   4364  2024 ?        S    14:03   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 nohup python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json > logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log 2>&1 &\\nroot     984726  361  0.7 59371628 8428672 ?    Rl   14:03 417:10 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json\\nroot     986458  0.0  0.0   4364  2092 ?        S    14:03   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 nohup python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed44_paired_r2.json > logs/eval_spatial_vla_only_seed44_paired_r2.log 2>&1 &\\nroot     986463  367  0.7 59293744 8271280 ?    Rl   14:03 422:28 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed44_paired_r2.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-25T07:58:58.936Z_

<details><summary>↩ Tool result · `toolu_01YLM4FirF9DL6U94g4PimpH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476   316 ?        Ss   May13   0:02 bash /init/boot/boot.sh\\nroot        881  1.6  0.0 725152 21284 ?        Sl   May13 293:56 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        900  0.0  0.0  15444  4188 ?        S    May13   1:03 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        902  0.2  0.0 5343360 99292 ?       Sl   May13  50:56 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        904  0.0  0.0 2181320 53704 ?       Sl   May13   7:47 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        905  0.0  0.0 191540 88620 ?        S    May13   0:03 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        906  0.1  0.0 3831096 17776 ?       Sl   May13  29:05 proxy -c /init/proxy/proxy.ini\\nroot        907  0.0  0.0 3608876 17204 ?       Sl   May13   6:40 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        974  0.0  0.0 17524960 4608 ?       Sl   May13   6:35 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_cg0t3xd4/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_cg0t3xd4/startup_error\\nroot     308485  0.0  0.0   4364  2008 ?        S    04:22   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup python -m http.server 19876 --directory /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/ > /dev/null 2>&1 & echo \\\"PID: $!\\\"\\nroot     308490  0.0  0.0  25560 19460 ?        S    04:22   0:04 python -m http.server 19876 --directory /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/\\nroot     333037  0.0  0.0  16692 10952 ?        Ss   07:58   0:03 sshd: root@notty\\nroot     349399  0.0  0.0   4364  1752 ?        S    12:09   0:00 bash -c cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.075 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2' > /root/autodl-tmp/logs/eval-k2-tau0075-spatial-s42.log 2>&1 & echo \\\"PID=$!\\\" sleep 2 ps -p $! -o pid=,cmd= 2>/dev/null | head -3\\nroot     349401  418  1.4 34476416 7500388 ?    Rl   12:09 960:31 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.075 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\nroot     370483  0.0  0.0  16692 10700 ?        Ss   15:58   0:00 sshd: root@notty\\nroot     370579  0.0  0.0   7064  1612 ?        Rs   15:58   0:00 ps aux\\nroot     643113  0.0  0.0  25560 15736 ?        S    May20   0:41 python3 -m http.server 18888\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "3159d0f2-ad53-4afa-9b9d-8176b449d188",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\\\nroot          1  0.0  0.0   4476   316 ?        Ss   May13   0:02 bash /init/boot/boot.sh\\\\nroot        881  1.6  0.0 725152 21284 ?        Sl   May13 293:56 /bin/supervisord -c /init/supervisor/supervisor.ini\\\\nroot        900  0.0  0.0  15444  4188 ?        S    May13   1:03 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\\\nroot        902  0.2  0.0 5343360 99292 ?       Sl   May13  50:56 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\\\nroot        904  0.0  0.0 2181320 53704 ?       Sl   May13   7:47 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\\\nroot        905  0.0  0.0 191540 88620 ?        S    May13   0:03 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\\\nroot        906  0.1  0.0 3831096 17776 ?       Sl   May13  29:05 proxy -c /init/proxy/proxy.ini\\\\nroot        907  0.0  0.0 3608876 17204 ?       Sl   May13   6:40 proxy -c /init/proxy/proxy-hot-backup.ini\\\\nroot        974  0.0  0.0 17524960 4608 ?       Sl   May13   6:35 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_cg0t3xd4/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_cg0t3xd4/startup_error\\\\nroot     308485  0.0  0.0   4364  2008 ?        S    04:22   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup python -m http.server 19876 --directory /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/ > /dev/null 2>&1 & echo \\\\\\\"PID: $!\\\\\\\"\\\\nroot     308490  0.0  0.0  25560 19460 ?        S    04:22   0:04 python -m http.server 19876 --directory /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/\\\\nroot     333037  0.0  0.0  16692 10952 ?        Ss   07:58   0:03 sshd: root@notty\\\\nroot     349399  0.0  0.0   4364  1752 ?        S    12:09   0:00 bash -c cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.075 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2' > /root/autodl-tmp/logs/eval-k2-tau0075-spatial-s42.log 2>&1 & echo \\\\\\\"PID=$!\\\\\\\" sleep 2 ps -p $! -o pid=,cmd= 2>/dev/null | head -3\\\\nroot     349401  418  1.4 34476416 7500388 ?    Rl   12:09 960:31 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.075 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\\\nroot     370483  0.0  0.0  16692 10700 ?        Ss   15:58   0:00 sshd: root@notty\\\\nroot     370579  0.0  0.0   7064  1612 ?        Rs   15:58   0:00 ps aux\\\\nroot     643113  0.0  0.0  25560 15736 ?        S    May20   0:41 python3 -m http.server 18888\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476   316 ?        Ss   May13   0:02 bash /init/boot/boot.sh\\nroot        881  1.6  0.0 725152 21284 ?        Sl   May13 293:56 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        900  0.0  0.0  15444  4188 ?        S    May13   1:03 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        902  0.2  0.0 5343360 99292 ?       Sl   May13  50:56 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        904  0.0  0.0 2181320 53704 ?       Sl   May13   7:47 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        905  0.0  0.0 191540 88620 ?        S    May13   0:03 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        906  0.1  0.0 3831096 17776 ?       Sl   May13  29:05 proxy -c /init/proxy/proxy.ini\\nroot        907  0.0  0.0 3608876 17204 ?       Sl   May13   6:40 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        974  0.0  0.0 17524960 4608 ?       Sl   May13   6:35 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_cg0t3xd4/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_cg0t3xd4/startup_error\\nroot     308485  0.0  0.0   4364  2008 ?        S    04:22   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup python -m http.server 19876 --directory /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/ > /dev/null 2>&1 & echo \\\"PID: $!\\\"\\nroot     308490  0.0  0.0  25560 19460 ?        S    04:22   0:04 python -m http.server 19876 --directory /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/\\nroot     333037  0.0  0.0  16692 10952 ?        Ss   07:58   0:03 sshd: root@notty\\nroot     349399  0.0  0.0   4364  1752 ?        S    12:09   0:00 bash -c cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.075 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2' > /root/autodl-tmp/logs/eval-k2-tau0075-spatial-s42.log 2>&1 & echo \\\"PID=$!\\\" sleep 2 ps -p $! -o pid=,cmd= 2>/dev/null | head -3\\nroot     349401  418  1.4 34476416 7500388 ?    Rl   12:09 960:31 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.075 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\nroot     370483  0.0  0.0  16692 10700 ?        Ss   15:58   0:00 sshd: root@notty\\nroot     370579  0.0  0.0   7064  1612 ?        Rs   15:58   0:00 ps aux\\nroot     643113  0.0  0.0  25560 15736 ?        S    May20   0:41 python3 -m http.server 18888\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011t9Q5qkiyNUUytwkxREgEM`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "python3 -c \"\nimport json, glob\nfor f in glob.glob('/root/acr-vla-conformal-refinement/logs/eval_spatial_*tau*0.075*.json') + glob.glob('/root/acr-vla-conformal-refinement/logs/eval_spatial_*tau0075*.json'):\n    d = json.load(open(f))\n    print(f'file={f}')\n    print(f'SR={d.get(\\\"success_rate\\\")}, trigger_rate={d.get(\\\"trigger_rate\\\")}, mean_unc={d.get(\\\"mean_unc\\\")}')\n\"\n",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "19890bdc-f2e2-4ecf-bb4b-b336dc46d375",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UB6uRrWzWfykFGQn2gRvR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20975,
      "cache_read_input_tokens": 27246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20975
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

_source line 40 · 2026-05-25T07:59:00.807Z_

<details><summary>↩ Tool result · `toolu_011t9Q5qkiyNUUytwkxREgEM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "c0b7aa63-ad59-46ff-966a-62b1330c16c0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_014NXmKX1AkabgeskB7VTDuk`</summary>

```json
{
  "filters": {
    "status": "RUNNING"
  },
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "name",
    "status",
    "server",
    "gpu",
    "pid",
    "spec"
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "5649aca8-95a7-4db7-85b5-f28fc34607b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UB6uRrWzWfykFGQn2gRvR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20975,
      "cache_read_input_tokens": 27246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20975
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

_source line 42 · 2026-05-25T07:59:03.861Z_

<details><summary>↩ Tool result · `toolu_014NXmKX1AkabgeskB7VTDuk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-s43-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_pi05_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"485043\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"backend\": \"nohup\", \"account\": \"root\"}}, \"eval-pi05-vla-only-object-s42-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"484670\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\", \"backend\": \"nohup\", \"account\": \"root\"}}, \"eval-pi05-adaptive-spatial-s42-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --output_file logs/eval_spatial_adaptive_pi05_seed42_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"484286\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_pi05_seed42_r2.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"backend\": \"nohup\", \"account\": \"root\"}}, \"eval-pi05-vla-only-goal-s42-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_pi05_seed42_paired.json\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:2\"], \"pid\": 446717, \"log_path\": \"/tmp/eval-pi05-vla-only-goal-s42-paired.log\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"timeout\": 18000, \"account\": \"root\", \"gpu\": \"cuda:2\"}}, \"eval-pi05-vla-only-spatial-s42-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_pi05_seed42_paired.json\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 446358, \"log_path\": \"/tmp/eval-pi05-vla-only-spatial-s42-paired.log\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"timeout\": 18000, \"account\": \"root\", \"gpu\": \"cuda:1\"}}, \"eval-pi05-adaptive-spatial-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --output_file logs/eval_spatial_adaptive_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"spatial\", \"gpu\": \"cuda:0\"}}, \"eval-k2-goal-vla-only-s47-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 47 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed47_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"smolvla_libero (no CRM)\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_vla_only_seed47_paired.log\"}}, \"eval-k2-goal-adapt-s47-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed47_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_adaptive_k2_tau025_seed47_paired.log\"}}, \"eval-k2-goal-vla-only-s46-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 46 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed46_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"smolvla_libero (no CRM)\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_vla_only_seed46_paired.log\"}}, \"eval-k2-goal-adapt-s46-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed46_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_adaptive_k2_tau025_seed46_paired.log\"}}, \"eval-k2-goal-vla-only-s45-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 45 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed45_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"smolvla_libero (no CRM)\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_vla_only_seed45_paired.log\"}}, \"eval-k2-goal-adapt-s45-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 45 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed45_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_adaptive_k2_tau025_seed45_paired.log\"}}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed44_paired_r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-k2-spatial-adapt-s44-paired-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed43_paired_r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-k2-spatial-adapt-s43-paired-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed42_paired_r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-k2-spatial-adapt-s42-paired-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-k2-tau0075-spatial-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.075 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-40593\", \"data_path\": \"libero/spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-tau0075-spatial-s42.log\", \"pid\": 349399}}, \"eval-vla-only-spatial-cqa1-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s44\"}}, \"eval-k2-adaptive-spatial-s49\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial (20 rollouts)\", \"gpu\": \"cuda:3\", \"tmux_session\": \"eval-k2-adaptive-spatial-s49\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s49.log\"}}, \"eval-vla-only-spatial-cqa1-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s43\"}}, \"eval-k2-adaptive-spatial-s48\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial (20 rollouts)\", \"gpu\": \"cuda:2\", \"tmux_session\": \"eval-k2-adaptive-spatial-s48\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s48.log\"}}, \"eval-vla-only-spatial-cqa1-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s42\"}}, \"eval-k2-adaptive-spatial-s46\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 46 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial (20 rollouts)\", \"gpu\": \"cuda:0\", \"tmux_session\": \"eval-k2-adaptive-spatial-s46\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s46.log\"}}, \"eval-k2-adaptive-spatial-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s44\"}}, \"eval-k2-adaptive-spatial-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s43\"}}, \"eval-k2-adaptive-spatial-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s42\"}}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 46 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k10-tau025-spatial-s46.log\", \"tmux_session\": \"eval-k10-tau025-spatial-s46\"}}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s49 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s49.log'\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"211568\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s49.log\", \"submitted_at\": \"2026-05-24T23:07:38.344Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s49\", \"timeout_seconds\": 18000}}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s48 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s48.log'\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"210816\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s48.log\", \"submitted_at\": \"2026-05-24T23:07:31.869Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s48\", \"timeout_seconds\": 18000}}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s44 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=5 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s44.log'\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"210458\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s44.log\", \"submitted_at\": \"2026-05-24T23:07:25.453Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s44\", \"timeout_seconds\": 18000}}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s43 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=4 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s43.log'\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"210181\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s43.log\", \"submitted_at\": \"2026-05-24T23:07:19.023Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s43\", \"timeout_seconds\": 18000}}, \"eval-long-adaptive-k10-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 10\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_long\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_long\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s44.log\", \"gpu\": \"cuda:5\", \"tmux_session\": \"eval-long-adaptive-k10-s44\"}}, \"eval-long-adaptive-k10-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 10\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_long\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_long\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s43.log\", \"gpu\": \"cuda:4\", \"tmux_session\": \"eval-long-adaptive-k10-s43\"}}, \"eval-long-adaptive-k10-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --K 10\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_long\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_long\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s42.log\", \"gpu\": \"cuda:3\", \"tmux_session\": \"eval-long-adaptive-k10-s42\"}}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\"}}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 45 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\"}}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"pid\": \"209904\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-canonical-adaptive-k10-spatial-s42.log\", \"submitted_at\": \"2026-05-24T23:07:09.098Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s42\", \"timeout_s\": 18000}}, \"eval-vla-only-spatial-bjb1-s46\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 46 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 46}}, \"eval-vla-only-spatial-bjb1-s49\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 49}}, \"eval-vla-only-spatial-bjb1-s48\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 48}}, \"eval-k2-tau010-spatial-s42-r3\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.10 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau010-spatial-s42-r3.log\", \"tmux_session\": \"eval-k2-tau010-spatial-s42-r3\", \"timeout\": 14400}}, \"eval-k2-tau015-spatial-s42-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.15 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau015-spatial-s42-r2.log\", \"tmux_session\": \"eval-k2-tau015-spatial-s42-r2\", \"timeout\": 14400}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}}, \"count\": 45, \"total\": 45, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1631}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "e18f373a-fc13-4b2c-8af6-38413d69daf8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-pi05-vla-only-spatial-s43-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_pi05_seed43.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"485043\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/pi05_libero_finetuned/\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\", \\\"backend\\\": \\\"nohup\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval-pi05-vla-only-object-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"484670\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.log\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/pi05_libero_finetuned/\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 20 rollouts)\\\", \\\"backend\\\": \\\"nohup\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval-pi05-adaptive-spatial-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --output_file logs/eval_spatial_adaptive_pi05_seed42_r2.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"484286\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_pi05_seed42_r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\", \\\"backend\\\": \\\"nohup\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval-pi05-vla-only-goal-s42-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_pi05_seed42_paired.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu_ids\\\": [\\\"cuda:2\\\"], \\\"pid\\\": 446717, \\\"log_path\\\": \\\"/tmp/eval-pi05-vla-only-goal-s42-paired.log\\\", \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"timeout\\\": 18000, \\\"account\\\": \\\"root\\\", \\\"gpu\\\": \\\"cuda:2\\\"}}, \\\"eval-pi05-vla-only-spatial-s42-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_pi05_seed42_paired.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 446358, \\\"log_path\\\": \\\"/tmp/eval-pi05-vla-only-spatial-s42-paired.log\\\", \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"timeout\\\": 18000, \\\"account\\\": \\\"root\\\", \\\"gpu\\\": \\\"cuda:1\\\"}}, \\\"eval-pi05-adaptive-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --output_file logs/eval_spatial_adaptive_pi05_seed42.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\\", \\\"eval_data\\\": \\\"spatial\\\", \\\"gpu\\\": \\\"cuda:0\\\"}}, \\\"eval-k2-goal-vla-only-s47-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 47 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed47_paired.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"smolvla_libero (no CRM)\\\", \\\"eval_data\\\": \\\"LIBERO-goal 10 tasks x 20 rollouts\\\", \\\"log_path\\\": \\\"logs/eval_goal_vla_only_seed47_paired.log\\\"}}, \\\"eval-k2-goal-adapt-s47-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed47_paired.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-goal 10 tasks x 20 rollouts\\\", \\\"log_path\\\": \\\"logs/eval_goal_adaptive_k2_tau025_seed47_paired.log\\\"}}, \\\"eval-k2-goal-vla-only-s46-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 46 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed46_paired.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"smolvla_libero (no CRM)\\\", \\\"eval_data\\\": \\\"LIBERO-goal 10 tasks x 20 rollouts\\\", \\\"log_path\\\": \\\"logs/eval_goal_vla_only_seed46_paired.log\\\"}}, \\\"eval-k2-goal-adapt-s46-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed46_paired.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-goal 10 tasks x 20 rollouts\\\", \\\"log_path\\\": \\\"logs/eval_goal_adaptive_k2_tau025_seed46_paired.log\\\"}}, \\\"eval-k2-goal-vla-only-s45-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 45 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed45_paired.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"smolvla_libero (no CRM)\\\", \\\"eval_data\\\": \\\"LIBERO-goal 10 tasks x 20 rollouts\\\", \\\"log_path\\\": \\\"logs/eval_goal_vla_only_seed45_paired.log\\\"}}, \\\"eval-k2-goal-adapt-s45-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 45 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed45_paired.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-goal 10 tasks x 20 rollouts\\\", \\\"log_path\\\": \\\"logs/eval_goal_adaptive_k2_tau025_seed45_paired.log\\\"}}, \\\"eval-k2-spatial-vla-only-s44-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 44, \\\"model_name\\\": \\\"smolvla\\\", \\\"data_path\\\": \\\"LIBERO spatial (10 tasks)\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO spatial\\\", \\\"log_path\\\": \\\"logs/eval_spatial_vla_only_seed44_paired_r2.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}}, \\\"eval-k2-spatial-adapt-s44-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 44, \\\"model_name\\\": \\\"smolvla\\\", \\\"data_path\\\": \\\"LIBERO spatial (10 tasks)\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO spatial\\\", \\\"log_path\\\": \\\"logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}}, \\\"eval-k2-spatial-vla-only-s43-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 43, \\\"model_name\\\": \\\"smolvla\\\", \\\"data_path\\\": \\\"LIBERO spatial (10 tasks)\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO spatial\\\", \\\"log_path\\\": \\\"logs/eval_spatial_vla_only_seed43_paired_r2.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}}, \\\"eval-k2-spatial-adapt-s43-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 43, \\\"model_name\\\": \\\"smolvla\\\", \\\"data_path\\\": \\\"LIBERO spatial (10 tasks)\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO spatial\\\", \\\"log_path\\\": \\\"logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}}, \\\"eval-k2-spatial-vla-only-s42-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 42, \\\"model_name\\\": \\\"smolvla\\\", \\\"data_path\\\": \\\"LIBERO spatial (10 tasks)\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO spatial\\\", \\\"log_path\\\": \\\"logs/eval_spatial_vla_only_seed42_paired_r2.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}}, \\\"eval-k2-spatial-adapt-s42-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 42, \\\"model_name\\\": \\\"smolvla\\\", \\\"data_path\\\": \\\"LIBERO spatial (10 tasks)\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO spatial\\\", \\\"log_path\\\": \\\"logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}}, \\\"eval-k2-tau0075-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.075 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"data_path\\\": \\\"libero/spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-k2-tau0075-spatial-s42.log\\\", \\\"pid\\\": 349399}}, \\\"eval-vla-only-spatial-cqa1-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"smolvla_base\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log\\\", \\\"tmux_session\\\": \\\"eval-vla-only-spatial-cqa1-s44\\\"}}, \\\"eval-k2-adaptive-spatial-s49\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial (20 rollouts)\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"tmux_session\\\": \\\"eval-k2-adaptive-spatial-s49\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s49.log\\\"}}, \\\"eval-vla-only-spatial-cqa1-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"smolvla_base\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log\\\", \\\"tmux_session\\\": \\\"eval-vla-only-spatial-cqa1-s43\\\"}}, \\\"eval-k2-adaptive-spatial-s48\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 48, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial (20 rollouts)\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"tmux_session\\\": \\\"eval-k2-adaptive-spatial-s48\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s48.log\\\"}}, \\\"eval-vla-only-spatial-cqa1-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"smolvla_base\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log\\\", \\\"tmux_session\\\": \\\"eval-vla-only-spatial-cqa1-s42\\\"}}, \\\"eval-k2-adaptive-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 46 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial (20 rollouts)\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"tmux_session\\\": \\\"eval-k2-adaptive-spatial-s46\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s46.log\\\"}}, \\\"eval-k2-adaptive-spatial-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log\\\", \\\"tmux_session\\\": \\\"eval-k2-adaptive-spatial-s44\\\"}}, \\\"eval-k2-adaptive-spatial-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log\\\", \\\"tmux_session\\\": \\\"eval-k2-adaptive-spatial-s43\\\"}}, \\\"eval-k2-adaptive-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log\\\", \\\"tmux_session\\\": \\\"eval-k2-adaptive-spatial-s42\\\"}}, \\\"eval-k10-tau025-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 46 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"/root/acr-vla-conformal-refinement\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-k10-tau025-spatial-s46.log\\\", \\\"tmux_session\\\": \\\"eval-k10-tau025-spatial-s46\\\"}}, \\\"eval-canonical-adaptive-k10-spatial-s49\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s49 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s49.log'\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"211568\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s49.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T23:07:38.344Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"eval-canonical-adaptive-k10-spatial-s49\\\", \\\"timeout_seconds\\\": 18000}}, \\\"eval-canonical-adaptive-k10-spatial-s48\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s48 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s48.log'\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"210816\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s48.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T23:07:31.869Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 48, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"eval-canonical-adaptive-k10-spatial-s48\\\", \\\"timeout_seconds\\\": 18000}}, \\\"eval-canonical-adaptive-k10-spatial-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s44 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=5 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s44.log'\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"210458\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s44.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T23:07:25.453Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"eval-canonical-adaptive-k10-spatial-s44\\\", \\\"timeout_seconds\\\": 18000}}, \\\"eval-canonical-adaptive-k10-spatial-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s43 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=4 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s43.log'\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"210181\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T23:07:19.023Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"eval-canonical-adaptive-k10-spatial-s43\\\", \\\"timeout_seconds\\\": 18000}}, \\\"eval-long-adaptive-k10-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 10\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_long\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_long\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s44.log\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"tmux_session\\\": \\\"eval-long-adaptive-k10-s44\\\"}}, \\\"eval-long-adaptive-k10-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 10\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_long\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_long\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s43.log\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"tmux_session\\\": \\\"eval-long-adaptive-k10-s43\\\"}}, \\\"eval-long-adaptive-k10-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --K 10\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"libero_long\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"libero_long\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s42.log\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"tmux_session\\\": \\\"eval-long-adaptive-k10-s42\\\"}}, \\\"eval-k10-tau025-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\"}}, \\\"eval-k10-tau025-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 45 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\"}}, \\\"eval-canonical-adaptive-k10-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"209904\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-canonical-adaptive-k10-spatial-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T23:07:09.098Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 20 rollouts)\\\", \\\"tmux_session\\\": \\\"eval-canonical-adaptive-k10-spatial-s42\\\", \\\"timeout_s\\\": 18000}}, \\\"eval-vla-only-spatial-bjb1-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 46 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"model_name\\\": \\\"SmolVLA\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 46}}, \\\"eval-vla-only-spatial-bjb1-s49\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"model_name\\\": \\\"SmolVLA\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 49}}, \\\"eval-vla-only-spatial-bjb1-s48\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"model_name\\\": \\\"SmolVLA\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"seed\\\": 48}}, \\\"eval-k2-tau010-spatial-s42-r3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.10 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 42, \\\"log_path\\\": \\\"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau010-spatial-s42-r3.log\\\", \\\"tmux_session\\\": \\\"eval-k2-tau010-spatial-s42-r3\\\", \\\"timeout\\\": 14400}}, \\\"eval-k2-tau015-spatial-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.15 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 42, \\\"log_path\\\": \\\"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau015-spatial-s42-r2.log\\\", \\\"tmux_session\\\": \\\"eval-k2-tau015-spatial-s42-r2\\\", \\\"timeout\\\": 14400}}, \\\"precompute-pi05-long-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": 114507, \\\"data_path\\\": \\\"/root/autodl-tmp/crm_cache_pi05_2048/long/\\\", \\\"data_count\\\": 136090, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\\\"}}}, \\\"count\\\": 45, \\\"total\\\": 45, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.1631}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-s43-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_pi05_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"485043\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"backend\": \"nohup\", \"account\": \"root\"}}, \"eval-pi05-vla-only-object-s42-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"484670\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\", \"backend\": \"nohup\", \"account\": \"root\"}}, \"eval-pi05-adaptive-spatial-s42-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --output_file logs/eval_spatial_adaptive_pi05_seed42_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"484286\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_pi05_seed42_r2.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"backend\": \"nohup\", \"account\": \"root\"}}, \"eval-pi05-vla-only-goal-s42-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_pi05_seed42_paired.json\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:2\"], \"pid\": 446717, \"log_path\": \"/tmp/eval-pi05-vla-only-goal-s42-paired.log\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"timeout\": 18000, \"account\": \"root\", \"gpu\": \"cuda:2\"}}, \"eval-pi05-vla-only-spatial-s42-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_pi05_seed42_paired.json\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 446358, \"log_path\": \"/tmp/eval-pi05-vla-only-spatial-s42-paired.log\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"timeout\": 18000, \"account\": \"root\", \"gpu\": \"cuda:1\"}}, \"eval-pi05-adaptive-spatial-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --output_file logs/eval_spatial_adaptive_pi05_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"spatial\", \"gpu\": \"cuda:0\"}}, \"eval-k2-goal-vla-only-s47-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 47 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed47_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"smolvla_libero (no CRM)\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_vla_only_seed47_paired.log\"}}, \"eval-k2-goal-adapt-s47-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed47_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_adaptive_k2_tau025_seed47_paired.log\"}}, \"eval-k2-goal-vla-only-s46-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 46 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed46_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"smolvla_libero (no CRM)\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_vla_only_seed46_paired.log\"}}, \"eval-k2-goal-adapt-s46-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed46_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_adaptive_k2_tau025_seed46_paired.log\"}}, \"eval-k2-goal-vla-only-s45-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --benchmark goal --seed 45 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed45_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"smolvla_libero (no CRM)\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_vla_only_seed45_paired.log\"}}, \"eval-k2-goal-adapt-s45-paired\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark goal --seed 45 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_k2_tau025_seed45_paired.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"log_path\": \"logs/eval_goal_adaptive_k2_tau025_seed45_paired.log\"}}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed44_paired_r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-k2-spatial-adapt-s44-paired-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed43_paired_r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-k2-spatial-adapt-s43-paired-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed42_paired_r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-k2-spatial-adapt-s42-paired-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-k2-tau0075-spatial-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.075 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-40593\", \"data_path\": \"libero/spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-tau0075-spatial-s42.log\", \"pid\": 349399}}, \"eval-vla-only-spatial-cqa1-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s44.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s44\"}}, \"eval-k2-adaptive-spatial-s49\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial (20 rollouts)\", \"gpu\": \"cuda:3\", \"tmux_session\": \"eval-k2-adaptive-spatial-s49\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s49.log\"}}, \"eval-vla-only-spatial-cqa1-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s43.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s43\"}}, \"eval-k2-adaptive-spatial-s48\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial (20 rollouts)\", \"gpu\": \"cuda:2\", \"tmux_session\": \"eval-k2-adaptive-spatial-s48\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s48.log\"}}, \"eval-vla-only-spatial-cqa1-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"smolvla_base\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-vla-only-spatial-cqa1-s42.log\", \"tmux_session\": \"eval-vla-only-spatial-cqa1-s42\"}}, \"eval-k2-adaptive-spatial-s46\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 46 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial (20 rollouts)\", \"gpu\": \"cuda:0\", \"tmux_session\": \"eval-k2-adaptive-spatial-s46\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s46.log\"}}, \"eval-k2-adaptive-spatial-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s44.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s44\"}}, \"eval-k2-adaptive-spatial-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s43.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s43\"}}, \"eval-k2-adaptive-spatial-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_spatial\", \"data_count\": 20, \"model_name\": \"smolvla+crm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/logs/eval-k2-adaptive-spatial-s42.log\", \"tmux_session\": \"eval-k2-adaptive-spatial-s42\"}}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 46 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k10-tau025-spatial-s46.log\", \"tmux_session\": \"eval-k10-tau025-spatial-s46\"}}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s49 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s49.log'\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"211568\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s49.log\", \"submitted_at\": \"2026-05-24T23:07:38.344Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s49\", \"timeout_seconds\": 18000}}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s48 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s48.log'\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"210816\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s48.log\", \"submitted_at\": \"2026-05-24T23:07:31.869Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s48\", \"timeout_seconds\": 18000}}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s44 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=5 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s44.log'\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"210458\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s44.log\", \"submitted_at\": \"2026-05-24T23:07:25.453Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s44\", \"timeout_seconds\": 18000}}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"tmux new-session -d -s eval-canonical-adaptive-k10-spatial-s43 'cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=4 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-canonical-adaptive-k10-spatial-s43.log'\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"210181\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-canonical-adaptive-k10-spatial-s43.log\", \"submitted_at\": \"2026-05-24T23:07:19.023Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s43\", \"timeout_seconds\": 18000}}, \"eval-long-adaptive-k10-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 10\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_long\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_long\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s44.log\", \"gpu\": \"cuda:5\", \"tmux_session\": \"eval-long-adaptive-k10-s44\"}}, \"eval-long-adaptive-k10-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 10\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_long\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_long\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s43.log\", \"gpu\": \"cuda:4\", \"tmux_session\": \"eval-long-adaptive-k10-s43\"}}, \"eval-long-adaptive-k10-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --K 10\", \"server\": \"cqa1-32758\", \"data_path\": \"libero_long\", \"data_count\": 20, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_long\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-long-adaptive-k10-s42.log\", \"gpu\": \"cuda:3\", \"tmux_session\": \"eval-long-adaptive-k10-s42\"}}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\"}}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 45 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\"}}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 timeout 18000 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --K 10 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"pid\": \"209904\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-canonical-adaptive-k10-spatial-s42.log\", \"submitted_at\": \"2026-05-24T23:07:09.098Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"tmux_session\": \"eval-canonical-adaptive-k10-spatial-s42\", \"timeout_s\": 18000}}, \"eval-vla-only-spatial-bjb1-s46\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 46 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 46}}, \"eval-vla-only-spatial-bjb1-s49\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 49}}, \"eval-vla-only-spatial-bjb1-s48\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 48}}, \"eval-k2-tau010-spatial-s42-r3\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.10 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau010-spatial-s42-r3.log\", \"tmux_session\": \"eval-k2-tau010-spatial-s42-r3\", \"timeout\": 14400}}, \"eval-k2-tau015-spatial-s42-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.15 --K 2 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval-k2-tau015-spatial-s42-r2.log\", \"tmux_session\": \"eval-k2-tau015-spatial-s42-r2\", \"timeout\": 14400}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}}, \"count\": 45, \"total\": 45, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1631}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Now I need to check bjb1-32546 more carefully - the ps output didn't show the vla-only s46/s48/s49 or the k2-adaptive experiments. Let me check for those specific processes. Also need to check bjb2-28827 for the tau010 and tau015 tmux sessions.

Wait, looking at bjb1-32546 ps output more carefully:
- I see 6 python processes running for K=2 spatial paired r2 (s42, s43, s44 - both adapt and vla_only) on GPUs 0-5


- But several expected processes are missing: the k2-adaptive runs for s46/s48/s49, the vla-only variants for those same seeds, and the k10-tau025 experiment that should be on cuda:0.

Looking at the process list more carefully, it seems the K=2 spatial paired r2 experiments have taken over all six GPUs on this machine, which means those older experiments must have been killed and replaced. Let me check the actual running processes again to see what's currently active. Looking at the process list more carefully, I can see five python processes running with their CPU usage, but the vla_only s43 process on CUDA:3 appears to be missing—there's a bash wrapper for it but no actual python child process spawned. GPU 3 is indeed idle with just 2 MiB of VRAM, so vla_only s43 must have crashed or finished running. Now I need to check the τ=0.075 log on bjb2-40593 using cat since ssh_read_only is blocking the python open() call, and also verify whether the tau010/tau015 tmux sessions exist on bjb2-28827 since I only see the 6 Goal K=2 paired experiments running there.

Looking more closely at the process list on bjb2-28827, I see 6 bash processes and 6 corresponding python processes for the Goal K=2 paired experiments across GPUs 0-5, each using about 2.3 GB of VRAM, but the registry shows eval-k2-tau010-spatial-s42-r3 and eval-k2-tau015-spatial-s42-r2 should be running there—they've clearly been overwritten. The supplementary experiments the user mentioned are likely already gone too, replaced by these newer deployments.

Now I need to check the τ=0.075 logs on bjb2-40593, verify what's happening with GPU 3 on bjb1-32546, inspect the tmux sessions on bjb2-28827 to confirm the tau010/tau015 processes are truly gone, and search the registry for those old supplementary experiments to see if they're still tracked anywhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "ab569aa9-9d2b-494c-9c03-d7dd645af0ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dpvh7Lxi7PtiGMKj1Vza6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 48221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25590
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

_source line 44_

需要用 cat 读 τ=0.075 日志，同时检查各服务器 tmux 和 PID 验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "4f3c7664-33e9-4857-93d8-5c36a2a4cb47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dpvh7Lxi7PtiGMKj1Vza6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 48221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25590
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

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AGa7LUVHQnKJC1RtPvgjgu`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "tail -30 /root/autodl-tmp/logs/eval-k2-tau0075-spatial-s42.log",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "3e752b7f-a363-400e-9600-68fb301e9711",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dpvh7Lxi7PtiGMKj1Vza6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 48221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25590
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

_source line 46 · 2026-05-25T07:59:40.685Z_

<details><summary>↩ Tool result · `toolu_01AGa7LUVHQnKJC1RtPvgjgu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 13/15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 18/20\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 90.0% (18/20)\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 15/20, success so far: 12/15\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 20/20, success so far: 15/20\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 75.0% (15/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 0/10\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 0/15\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 14/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 15/20, success so far: 14/15\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 5/20, success so far: 3/5\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 10/20, success so far: 8/10\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 15/20, success so far: 13/15\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 20/20, success so far: 17/20\\n[pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate] success rate: 85.0% (17/20)\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 7/10\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "c972b599-9350-4f21-aabb-cf56eb975094",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 13/15\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 18/20\\\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 90.0% (18/20)\\\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 15/20, success so far: 12/15\\\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 20/20, success so far: 15/20\\\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 75.0% (15/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 0/5\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 0/10\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 0/15\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 0/20\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 14/15\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 15/20, success so far: 14/15\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\\\n[pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 5/20, success so far: 3/5\\\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 10/20, success so far: 8/10\\\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 15/20, success so far: 13/15\\\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 20/20, success so far: 17/20\\\\n[pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate] success rate: 85.0% (17/20)\\\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 7/10\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 13/15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 18/20\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 90.0% (18/20)\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 15/20, success so far: 12/15\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 20/20, success so far: 15/20\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 75.0% (15/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 0/10\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 0/15\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 14/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 15/20, success so far: 14/15\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 5/20, success so far: 3/5\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 10/20, success so far: 8/10\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 15/20, success so far: 13/15\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 20/20, success so far: 17/20\\n[pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate] success rate: 85.0% (17/20)\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 7/10\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HzMMGh2ipVnwD7JvgEF6mD`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_spatial_*tau*0.075* /root/acr-vla-conformal-refinement/logs/eval_spatial_*tau0075* /root/acr-vla-conformal-refinement/logs/*tau0075*.json 2>/dev/null",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "b880bb32-c9a8-40c3-868f-9572da0eff93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dpvh7Lxi7PtiGMKj1Vza6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 48221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25590
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

_source line 48 · 2026-05-25T07:59:42.212Z_

<details><summary>↩ Tool result · `toolu_01HzMMGh2ipVnwD7JvgEF6mD`</summary>

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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "8336b9ea-ac69-4d06-ac15-1b07f3ad4ace",
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

_source line 49_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018szm8wtV2tan5M2zEex7d7`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "16d367e2-cca2-4ac4-9694-46ff8c4c1e42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dpvh7Lxi7PtiGMKj1Vza6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 48221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25590
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

_source line 50 · 2026-05-25T07:59:43.856Z_

<details><summary>↩ Tool result · `toolu_018szm8wtV2tan5M2zEex7d7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"978848, GPU-220671b6-4e9c-db2d-1361-6ed090a1f3af, 1959 MiB\\n980371, GPU-ade291cb-7e13-f292-1714-09ef80919436, 1953 MiB\\n984726, GPU-563702d3-df96-d375-0303-c9b9f202bdd2, 1959 MiB\\n986463, GPU-6d1331f1-8f19-df6c-71d5-e8ca2f3e2178, 1953 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "4234a413-abad-458d-9f3f-9875020d704f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"978848, GPU-220671b6-4e9c-db2d-1361-6ed090a1f3af, 1959 MiB\\\\n980371, GPU-ade291cb-7e13-f292-1714-09ef80919436, 1953 MiB\\\\n984726, GPU-563702d3-df96-d375-0303-c9b9f202bdd2, 1959 MiB\\\\n986463, GPU-6d1331f1-8f19-df6c-71d5-e8ca2f3e2178, 1953 MiB\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.69}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"978848, GPU-220671b6-4e9c-db2d-1361-6ed090a1f3af, 1959 MiB\\n980371, GPU-ade291cb-7e13-f292-1714-09ef80919436, 1953 MiB\\n984726, GPU-563702d3-df96-d375-0303-c9b9f202bdd2, 1959 MiB\\n986463, GPU-6d1331f1-8f19-df6c-71d5-e8ca2f3e2178, 1953 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WqyaSQCC66WtCFDg3nZBma`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "c0f1e903-5689-454c-8782-faf755fd188b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dpvh7Lxi7PtiGMKj1Vza6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 48221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25590
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

_source line 52 · 2026-05-25T07:59:44.536Z_

<details><summary>↩ Tool result · `toolu_01WqyaSQCC66WtCFDg3nZBma`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"639192, GPU-d7423c53-447e-0c0f-dd10-076e4989d991, 1882 MiB\\n639189, GPU-3ca0dfcc-ade3-2eb8-0f77-59f6aae6ac44, 2329 MiB\\n639190, GPU-cd6008a7-b242-51e0-5f10-49dfd6d5651d, 2335 MiB\\n639199, GPU-a0d22891-1964-0f75-4962-81994416abaf, 1876 MiB\\n639193, GPU-54175474-0aa4-3553-ee7c-968cb4b0f9ad, 2335 MiB\\n639194, GPU-e78bc8c3-4047-7933-7882-9f404fae347f, 1876 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "644247fb-043b-420e-af5c-4a0296fb0411",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"639192, GPU-d7423c53-447e-0c0f-dd10-076e4989d991, 1882 MiB\\\\n639189, GPU-3ca0dfcc-ade3-2eb8-0f77-59f6aae6ac44, 2329 MiB\\\\n639190, GPU-cd6008a7-b242-51e0-5f10-49dfd6d5651d, 2335 MiB\\\\n639199, GPU-a0d22891-1964-0f75-4962-81994416abaf, 1876 MiB\\\\n639193, GPU-54175474-0aa4-3553-ee7c-968cb4b0f9ad, 2335 MiB\\\\n639194, GPU-e78bc8c3-4047-7933-7882-9f404fae347f, 1876 MiB\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"639192, GPU-d7423c53-447e-0c0f-dd10-076e4989d991, 1882 MiB\\n639189, GPU-3ca0dfcc-ade3-2eb8-0f77-59f6aae6ac44, 2329 MiB\\n639190, GPU-cd6008a7-b242-51e0-5f10-49dfd6d5651d, 2335 MiB\\n639199, GPU-a0d22891-1964-0f75-4962-81994416abaf, 1876 MiB\\n639193, GPU-54175474-0aa4-3553-ee7c-968cb4b0f9ad, 2335 MiB\\n639194, GPU-e78bc8c3-4047-7933-7882-9f404fae347f, 1876 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019GqgVH3sR6qTybRJk8D1Ai`</summary>

```json
{
  "filters": {
    "status": "RUNNING"
  },
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "name",
    "status",
    "server"
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "21239125-597f-4f1c-a207-0d8b0d88ce5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dpvh7Lxi7PtiGMKj1Vza6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 48221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25590
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

_source line 54 · 2026-05-25T07:59:47.276Z_

<details><summary>↩ Tool result · `toolu_019GqgVH3sR6qTybRJk8D1Ai`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-s43-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-object-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-adaptive-spatial-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-goal-s42-paired\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-spatial-s42-paired\": {\"status\": \"RUNNING\"}, \"eval-pi05-adaptive-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s47-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s47-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s46-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s46-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s45-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s45-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s44-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s43-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s42-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-tau0075-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s44\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s43\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s48\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s42\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s44\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s43\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"RUNNING\"}, \"eval-long-adaptive-k10-s44\": {\"status\": \"RUNNING\"}, \"eval-long-adaptive-k10-s43\": {\"status\": \"RUNNING\"}, \"eval-long-adaptive-k10-s42\": {\"status\": \"RUNNING\"}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"RUNNING\"}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s46\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s48\": {\"status\": \"RUNNING\"}, \"eval-k2-tau010-spatial-s42-r3\": {\"status\": \"RUNNING\"}, \"eval-k2-tau015-spatial-s42-r2\": {\"status\": \"RUNNING\"}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\"}}, \"count\": 45, \"total\": 45, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1728}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "68e4260f-a69d-40dd-8768-57a9f071a791",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-pi05-vla-only-spatial-s43-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-vla-only-object-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-adaptive-spatial-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-vla-only-goal-s42-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-vla-only-spatial-s42-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-adaptive-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-vla-only-s47-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-adapt-s47-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-vla-only-s46-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-adapt-s46-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-vla-only-s45-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-adapt-s45-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-vla-only-s44-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-adapt-s44-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-vla-only-s43-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-adapt-s43-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-vla-only-s42-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-adapt-s42-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-tau0075-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-cqa1-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s49\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-cqa1-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s48\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-cqa1-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k10-tau025-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s49\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s48\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-long-adaptive-k10-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-long-adaptive-k10-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-long-adaptive-k10-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k10-tau025-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k10-tau025-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-bjb1-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-bjb1-s49\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-bjb1-s48\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-tau010-spatial-s42-r3\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-tau015-spatial-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"precompute-pi05-long-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}}, \\\"count\\\": 45, \\\"total\\\": 45, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.1728}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-s43-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-object-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-adaptive-spatial-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-goal-s42-paired\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-spatial-s42-paired\": {\"status\": \"RUNNING\"}, \"eval-pi05-adaptive-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s47-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s47-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s46-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s46-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s45-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s45-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s44-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s43-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s42-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-tau0075-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s44\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s43\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s48\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s42\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s44\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s43\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"RUNNING\"}, \"eval-long-adaptive-k10-s44\": {\"status\": \"RUNNING\"}, \"eval-long-adaptive-k10-s43\": {\"status\": \"RUNNING\"}, \"eval-long-adaptive-k10-s42\": {\"status\": \"RUNNING\"}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"RUNNING\"}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"RUNNING\"}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s46\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s48\": {\"status\": \"RUNNING\"}, \"eval-k2-tau010-spatial-s42-r3\": {\"status\": \"RUNNING\"}, \"eval-k2-tau015-spatial-s42-r2\": {\"status\": \"RUNNING\"}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\"}}, \"count\": 45, \"total\": 45, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1728}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
Now let me also verify what's on bjb1-32546 more carefully. I see only 4 compute apps (not 5 or 6). Let me map them:
- PID 978848 on GPU-220671b6... → adapt s42 on cuda:0
- PID 980371 on GPU-ade291cb... → vla_only s42 on cuda:1
- PID 984726 on GPU-563702d3... → adapt s44 on cuda:4


- PID 986463 on GPU-6d1331f1... → vla_only s44 on cuda:5

But there's a discrepancy here. The ps aux output showed PID 981563 running at 367% CPU, which should be adapt s43 on cuda:2, yet it's not showing up in nvidia-smi's compute apps list. And vla_only s43 on cuda:3 is completely missing from both outputs. Let me double-check what ps aux actually reported.

Looking at the raw process data, PID 981563 is definitely running the adaptive_conformal_crm evaluation with seed 43, consuming significant CPU. But nvidia-smi --query-compute-apps only lists 4 PIDs total on this machine, and 981563 isn't among them. That's strange—GPU 2 shows 1978 MiB allocated, but there's no corresponding compute process listed. Either the process released GPU memory despite still running, or there's a timing mismatch between when ps and nvidia-smi captured their snapshots. Looking at GPU 2's memory usage and utilization rate, it seems PID 981563 is actively running there even though the compute apps query didn't capture it. GPU 3 appears to be idle now. Checking the user's list of old experiments from bjb2-28827, none of them show up in the current RUNNING registry, so they've already been completed or marked as finished. I'm noticing a discrepancy between what the registry claims is running and what actually shows up in the process list. Several PIDs that should be active—485043 for the spatial s43 process and 446717 for the goal s42 process—aren't appearing in the ps output at all, which suggests they either crashed or were never properly started despite being registered. Looking at the nvidia-smi output more carefully, all four GPUs are actually in use with significant memory allocated—GPU 2 isn't free as I initially thought, and GPU 3 is being used by the precompute process, so there's no available GPU capacity on this machine. Looking at the registry entry for that spatial experiment, it shows PID 485043 registered at 07:34 today, but ps doesn't list it anywhere—the GPU memory is likely orphaned from a crashed process that didn't release its CUDA allocation. Now I need to check whether any of the user's old supplementary experiments are actually running in the current batch of 45 experiments.

Let me pull together the full status report. On bjb1-18228, I'm seeing four GPUs with mixed results: GPU 0 and 1 are running the adaptive and vla_only spatial experiments as expected, GPU 3 is running the precompute job, but GPU 2 has orphaned memory from the spatial s43 r2 process that crashed without freeing its allocation. Looking at the remaining zombie processes, a few have no PID found, and one experiment already shows a failed conclusion. The bjb2-28827 machine has 6 GPUs with varying memory usage, mostly running goal-based experiments with different spatial and VLA configurations across paired seeds. The last experiment on GPU 5 just finished, so all six Goal K=2 paired runs across checkpoints s45-s47 are now complete. I'm also noting there are some zombie processes still registered but actually dead—older spatial and canonical experiments that got overwritten or already killed. All GPUs are currently occupied, and there are a few supplementary experiments from s47 that the user mentioned earlier. Looking at the GPU allocation across the remaining slots—GPU 3 freed up after the vla_only experiment on s43 crashed, leaving five K2 spatial paired experiments actively running across the other GPUs with consistent memory usage around 2GB each and CPU utilization tracking normally. Looking at the remaining zombie processes that were already killed, and noting that cuda:3 is now free. The old experiments the user mentioned aren't in the registry anymore since they completed earlier. On the bjb2 server, GPU 0 is running the K2 tau0075 spatial experiment with moderate memory usage.

The tau=0.075 run is still active and progressing through its tasks, currently around task 8 or 9 of 10. Since those older experiments aren't showing up in the current registry, they've likely already finished or been terminated, which aligns with what the user suspected about them being overwritten or cleared out.

There's also a cluster of zombie processes on cqa1-32758 that are still marked as running despite the user saying that machine is disabled — these include several spatial and adaptive variants that should probably be cleaned up.

Now I'm checking bjb1-32546 more carefully to see if that adapt s43 process on GPU 2 is actually still running, since the nvidia-smi output shows some PIDs with GPU memory allocated but I need to verify the exact mapping between those processes and their GPU assignments. So there are 5 processes running across GPUs 0, 1, 2, 4, and 5 with about 2GB each. Checking on the vla_only s43 process on GPU 3—I can see the bash wrapper was launched but there's no corresponding Python process in the output, and GPU 3 shows minimal memory and no utilization, so that job must have already finished. Now I'll compile the full GPU mapping report with all the process details. Now I need to figure out whether that vla_only s43 job actually finished or crashed, and check if it left any output on disk. On bjb1-18228, GPU 2 is stuck with 10.4 GB of leaked memory from a crashed experiment — the GPU won't free up unless I reset it, which would kill everything else running there. Let me search the registry by experiment name to see what actually happened to those older eval-supp jobs the user mentioned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "0df5cb89-63f5-4d06-9d6e-4fdd04caa649",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SP52THgthTksHVWfgbAjc5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6128,
      "cache_read_input_tokens": 73811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6128
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

_source line 56_

最后确认几个关键点：bjb1-32546 的 vla_only s43 日志，以及旧 supplementary 实验的 registry 状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "d289cc84-0d90-4d99-9d4b-c4e3f49d1a14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SP52THgthTksHVWfgbAjc5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6128,
      "cache_read_input_tokens": 73811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6128
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

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RmqSFshjQAiiP6yMDKZHeg`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43_paired_r2.log",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "51ba2e81-013a-4ec6-8dba-bb8d9ac9d9d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SP52THgthTksHVWfgbAjc5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6128,
      "cache_read_input_tokens": 73811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6128
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

_source line 58 · 2026-05-25T08:01:22.264Z_

<details><summary>↩ Tool result · `toolu_01RmqSFshjQAiiP6yMDKZHeg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nOverall success rate (vla_only): 79.5% (159/200)\\n============================================================\\n[eval] Results saved to logs/eval_spatial_vla_only_seed43_paired_r2.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "76f9482b-4db1-4c2d-b9e6-6fd00b9dd2f6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"============================================================\\\\nOverall success rate (vla_only): 79.5% (159/200)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_spatial_vla_only_seed43_paired_r2.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.64}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nOverall success rate (vla_only): 79.5% (159/200)\\n============================================================\\n[eval] Results saved to logs/eval_spatial_vla_only_seed43_paired_r2.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0169NNk4yFSJE4TE3fqSXib2`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.log",
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
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "396ad179-9ce1-4d47-bc7c-245692c4f68e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SP52THgthTksHVWfgbAjc5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6128,
      "cache_read_input_tokens": 73811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6128
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

_source line 60 · 2026-05-25T08:01:22.886Z_

<details><summary>↩ Tool result · `toolu_0169NNk4yFSJE4TE3fqSXib2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nOverall success rate (vla_only): 97.5% (195/200)\\n============================================================\\n[eval] Results saved to logs/eval_spatial_vla_only_pi05_seed43.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "ed260d6c-6568-4c6a-9214-d113b32b6855",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"============================================================\\\\nOverall success rate (vla_only): 97.5% (195/200)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_spatial_vla_only_pi05_seed43.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nOverall success rate (vla_only): 97.5% (195/200)\\n============================================================\\n[eval] Results saved to logs/eval_spatial_vla_only_pi05_seed43.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01QQo6Gj7kVZ2yNnkwWgUgxq`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "name",
    "status",
    "server",
    "conclusion"
  ],
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "00a7603e-4558-48da-9801-f6ba3854e7ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SP52THgthTksHVWfgbAjc5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6128,
      "cache_read_input_tokens": 73811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6128
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

_source line 62 · 2026-05-25T08:01:25.474Z_

<details><summary>↩ Tool result · `toolu_01QQo6Gj7kVZ2yNnkwWgUgxq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-s43-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-object-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-adaptive-spatial-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s42-paired\": {\"status\": \"RUNNING\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s42-paired\": {\"status\": \"RUNNING\", \"conclusion\": \"success\"}, \"eval-pi05-adaptive-spatial-s42\": {\"status\": \"RUNNING\", \"conclusion\": \"failed\"}, \"eval-k2-goal-vla-only-s47-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s47-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s46-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s46-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s45-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s45-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s44-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s43-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s42-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s47-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s47-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-vla-only-s45-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s45-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-vla-only-s49-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-vla-only-s48-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-vla-only-s46-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s49-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s48-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s46-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-tau0075-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s44\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s43\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s48\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s42\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s44\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s43\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb2-s47\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-bjb2-s45\": {\"status\": \"PREPARING\"}, \"eval-k2-adaptive-spatial-s47\": {\"status\": \"PREPARING\"}, \"eval-k2-adaptive-spatial-s45\": {\"status\": \"PREPARING\"}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s44\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s43\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s42\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-bjb1-s46\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s48\": {\"status\": \"RUNNING\"}, \"eval-k2-tau035-spatial-s42\": {\"status\": \"QUEUED\"}, \"eval-k2-tau025-spatial-s42\": {\"status\": \"QUEUED\"}, \"eval-k2-tau020-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau010-spatial-s42-r3\": {\"status\": \"RUNNING\"}, \"eval-k2-tau015-spatial-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-tau030-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau010-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-norm005-goal-s49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-norm005-object-s48\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-long-vla-only-s48\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s50\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-spatial-vla-only-smolvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-object-s43-v2\": {\"status\": \"QUEUED\"}, \"eval-pi05-vla-only-object-s42-v2\": {\"status\": \"QUEUED\"}, \"eval-pi05-vla-only-goal-s43-v2\": {\"status\": \"QUEUED\"}, \"eval-pi05-vla-only-goal-s42-v2\": {\"status\": \"QUEUED\"}, \"eval-pi05-vla-only-spatial-s43-v2\": {\"status\": \"QUEUED\"}, \"eval-pi05-vla-only-spatial-s42-v2\": {\"status\": \"QUEUED\"}, \"eval-k2-tau010-015-spatial-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"eval-k2-tau010-spatial-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"train-crm-pi05-unified-3suite-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-vla-only-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-obj-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-obj-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-goal-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-reconvla-spatial-s42\": {\"status\": \"PREPARING\"}, \"eval-canonical-vla-only-spatial-s44\": {\"status\": \"PREPARING\"}, \"eval-adaptive-spatial-k1-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-spatial-s42-sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-tau045-spatial-s42\": {\"status\": \"PREPARING\"}, \"eval-tau040-spatial-s42\": {\"status\": \"PREPARING\"}, \"eval-tau005-spatial-s42\": {\"status\": \"PREPARING\"}, \"eval-spatial-vla-only-s42-verify\": {\"status\": \"PREPARING\"}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-s50\": {\"status\": \"PREPARING\"}, \"eval-pi05-reconvla-spatial-s42-bf16\": {\"status\": \"PREPARING\"}, \"eval-supp-object-vla-only-s50\": {\"status\": \"QUEUED\", \"conclusion\": \"killed\"}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s49\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-pi05-reconvla-object-s42\": {\"status\": \"PREPARING\"}, \"eval-pi05-reconvla-goal-s42\": {\"status\": \"PREPARING\"}, \"eval-supp-adapt-tau025-goal-s49\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-goal-s48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s49\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-adaptive-k1-spatial-tau025-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-crm-obj-s47-reeval\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-tau-sweep-spatial-tau030-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-tau-sweep-spatial-tau020-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-tau-sweep-spatial-tau010-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s50\": {\"status\": \"PREPARING\"}, \"eval-supp-long-adapt-tau025-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-k5-spatial-tau025-s42\": {\"status\": \"PREPARING\"}, \"eval-supp-long-k2mean-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-a1-baseline-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-vla-only-s47-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-adapt-tau025-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-crm-norm005-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s47-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-unified-3suite\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-spatial-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-goal-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}}, \"count\": 200, \"total\": 1047, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2973}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "fedcf764-4c22-4475-9b0b-2de955443d56",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-spatial-adapt-tau025-s45-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-spatial-reconvla-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-pi05-vla-only-spatial-s43-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-vla-only-object-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-adaptive-spatial-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-pi05-vla-only-spatial-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-object-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-goal-s42-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-spatial-s42-paired\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-adaptive-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-k2-goal-vla-only-s47-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-adapt-s47-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-vla-only-s46-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-adapt-s46-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-vla-only-s45-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-goal-adapt-s45-paired\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-vla-only-s44-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-adapt-s44-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-vla-only-s43-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-adapt-s43-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-vla-only-s42-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-adapt-s42-paired-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-spatial-vla-only-s47-paired\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-spatial-adapt-s47-paired\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-spatial-vla-only-s45-paired\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-spatial-adapt-s45-paired\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-spatial-vla-only-s49-paired\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-spatial-vla-only-s48-paired\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-spatial-vla-only-s46-paired\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-spatial-adapt-s49-paired\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-spatial-adapt-s48-paired\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-spatial-adapt-s46-paired\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-tau0075-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-cqa1-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s49\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-cqa1-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s48\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-cqa1-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s44\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s43\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-adaptive-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-bjb2-s47\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-bjb2-s45\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-k2-adaptive-spatial-s47\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-k2-adaptive-spatial-s45\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-k10-tau025-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s49\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s48\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-long-adaptive-k10-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-long-adaptive-k10-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-long-adaptive-k10-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-k10-tau025-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-k10-tau025-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-canonical-adaptive-k10-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-vla-only-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-adapt-tau025-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-spatial-bjb1-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-bjb1-s49\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-vla-only-spatial-bjb1-s48\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-tau035-spatial-s42\\\": {\\\"status\\\": \\\"QUEUED\\\"}, \\\"eval-k2-tau025-spatial-s42\\\": {\\\"status\\\": \\\"QUEUED\\\"}, \\\"eval-k2-tau020-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-tau010-spatial-s42-r3\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-tau015-spatial-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-k2-tau030-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-tau010-spatial-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-pi05-vla-only-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-object-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-object-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k2-tau015-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-pi05-vla-only-goal-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-goal-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-spatial-s49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-spatial-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-vla-only-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-goal-vla-only-s42-bjb1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"crm-norm005-goal-s49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-obj-vla-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"crm-norm005-object-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-obj-vla-only-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-obj-vla-only-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-long-vla-only-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-goal-vla-only-s50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-goal-vla-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-spatial-vla-only-smolvla-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-goal-vla-only-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-goal-vla-only-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-pi05-vla-only-object-s43-v2\\\": {\\\"status\\\": \\\"QUEUED\\\"}, \\\"eval-pi05-vla-only-object-s42-v2\\\": {\\\"status\\\": \\\"QUEUED\\\"}, \\\"eval-pi05-vla-only-goal-s43-v2\\\": {\\\"status\\\": \\\"QUEUED\\\"}, \\\"eval-pi05-vla-only-goal-s42-v2\\\": {\\\"status\\\": \\\"QUEUED\\\"}, \\\"eval-pi05-vla-only-spatial-s43-v2\\\": {\\\"status\\\": \\\"QUEUED\\\"}, \\\"eval-pi05-vla-only-spatial-s42-v2\\\": {\\\"status\\\": \\\"QUEUED\\\"}, \\\"eval-k2-tau010-015-spatial-s42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-k2-tau010-spatial-s42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"train-crm-pi05-unified-3suite-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-vla-only-spatial-s49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-vla-only-spatial-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-vla-only-obj-s49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-vla-only-obj-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-vla-only-goal-s49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-vla-only-goal-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-reconvla-spatial-s42\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-canonical-vla-only-spatial-s44\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-adaptive-spatial-k1-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k5-spatial-s42-sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-tau045-spatial-s42\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-tau040-spatial-s42\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-tau005-spatial-s42\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-spatial-vla-only-s42-verify\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-supp-long-vla-only-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-object-vla-only-s50\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-pi05-reconvla-spatial-s42-bf16\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-supp-object-vla-only-s50\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-goal-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-vla-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-vla-only-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-object-seed43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-vla-only-s50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-obj-s49\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-obj-s48\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-reconvla-object-s42\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-pi05-reconvla-goal-s42\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-supp-adapt-tau025-goal-s49\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-goal-s48\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-spatial-s49\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-spatial-s48\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k1-spatial-tau025-s42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-obj-s47-reeval\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-tau-sweep-spatial-tau030-s42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-tau-sweep-spatial-tau020-s42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-tau-sweep-spatial-tau010-s42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-obj-s50\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-supp-long-adapt-tau025-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-adaptive-k5-spatial-tau025-s42\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-supp-long-k2mean-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-reconvla-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-a1-baseline-object-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-long-vla-only-s47-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-k2mean-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-obj-adapt-tau025-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-crm-norm005-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-vla-only-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-spatial-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-vla-only-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-adapt-tau025-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-adapt-tau025-spatial-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-k2mean-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-reconvla-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-k2mean-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-adapt-tau025-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-crm-norm005-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-reconvla-spatial-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-vla-only-spatial-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-reconvla-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-crm-norm005-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-reconvla-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-k2mean-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-crm-norm005-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-adapt-tau025-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-vla-only-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-vla-only-s47-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-k2mean-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-long-adapt-tau025-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-spatial-crm-norm005-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-crm-norm005-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train-crm-pi05-unified-3suite\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-pi05-object-2048-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-openvla-object-vla-only-seed42-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-vla-only-spatial-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-vla-only-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-spatial-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train-crm-pi05-spatial-k1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train-crm-pi05-goal-k1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-vla-only-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-vla-only-s47-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-vla-only-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-goal-vla-only-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-reconvla-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-k2mean-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-spatial-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-adapt-tau025-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"crm-train-openvla-k1-multiscale-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-k2mean-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-reconvla-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-crm-norm005-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-adapt-tau025-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-obj-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-obj-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 200, \\\"total\\\": 1047, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.2973}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-s43-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-object-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-adaptive-spatial-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-pi05-vla-only-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s42-paired\": {\"status\": \"RUNNING\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s42-paired\": {\"status\": \"RUNNING\", \"conclusion\": \"success\"}, \"eval-pi05-adaptive-spatial-s42\": {\"status\": \"RUNNING\", \"conclusion\": \"failed\"}, \"eval-k2-goal-vla-only-s47-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s47-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s46-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s46-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-vla-only-s45-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-goal-adapt-s45-paired\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s44-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s44-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s43-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s43-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s42-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-adapt-s42-paired-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-spatial-vla-only-s47-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s47-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-vla-only-s45-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s45-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-vla-only-s49-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-vla-only-s48-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-vla-only-s46-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s49-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s48-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-spatial-adapt-s46-paired\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-k2-tau0075-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s44\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s43\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s48\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-cqa1-s42\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s44\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s43\": {\"status\": \"RUNNING\"}, \"eval-k2-adaptive-spatial-s42\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb2-s47\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-bjb2-s45\": {\"status\": \"PREPARING\"}, \"eval-k2-adaptive-spatial-s47\": {\"status\": \"PREPARING\"}, \"eval-k2-adaptive-spatial-s45\": {\"status\": \"PREPARING\"}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s44\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s43\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-long-adaptive-k10-s42\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"RUNNING\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-bjb1-s46\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-spatial-bjb1-s48\": {\"status\": \"RUNNING\"}, \"eval-k2-tau035-spatial-s42\": {\"status\": \"QUEUED\"}, \"eval-k2-tau025-spatial-s42\": {\"status\": \"QUEUED\"}, \"eval-k2-tau020-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau010-spatial-s42-r3\": {\"status\": \"RUNNING\"}, \"eval-k2-tau015-spatial-s42-r2\": {\"status\": \"RUNNING\"}, \"eval-k2-tau030-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau010-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k2-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s42-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-norm005-goal-s49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-norm005-object-s48\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-long-vla-only-s48\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s50\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-spatial-vla-only-smolvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-object-s43-v2\": {\"status\": \"QUEUED\"}, \"eval-pi05-vla-only-object-s42-v2\": {\"status\": \"QUEUED\"}, \"eval-pi05-vla-only-goal-s43-v2\": {\"status\": \"QUEUED\"}, \"eval-pi05-vla-only-goal-s42-v2\": {\"status\": \"QUEUED\"}, \"eval-pi05-vla-only-spatial-s43-v2\": {\"status\": \"QUEUED\"}, \"eval-pi05-vla-only-spatial-s42-v2\": {\"status\": \"QUEUED\"}, \"eval-k2-tau010-015-spatial-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"eval-k2-tau010-spatial-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"train-crm-pi05-unified-3suite-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-vla-only-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-obj-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-obj-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-goal-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-reconvla-spatial-s42\": {\"status\": \"PREPARING\"}, \"eval-canonical-vla-only-spatial-s44\": {\"status\": \"PREPARING\"}, \"eval-adaptive-spatial-k1-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-spatial-s42-sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-tau045-spatial-s42\": {\"status\": \"PREPARING\"}, \"eval-tau040-spatial-s42\": {\"status\": \"PREPARING\"}, \"eval-tau005-spatial-s42\": {\"status\": \"PREPARING\"}, \"eval-spatial-vla-only-s42-verify\": {\"status\": \"PREPARING\"}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-s50\": {\"status\": \"PREPARING\"}, \"eval-pi05-reconvla-spatial-s42-bf16\": {\"status\": \"PREPARING\"}, \"eval-supp-object-vla-only-s50\": {\"status\": \"QUEUED\", \"conclusion\": \"killed\"}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s49\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-pi05-reconvla-object-s42\": {\"status\": \"PREPARING\"}, \"eval-pi05-reconvla-goal-s42\": {\"status\": \"PREPARING\"}, \"eval-supp-adapt-tau025-goal-s49\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-goal-s48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s49\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-adaptive-k1-spatial-tau025-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-crm-obj-s47-reeval\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-tau-sweep-spatial-tau030-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-tau-sweep-spatial-tau020-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-tau-sweep-spatial-tau010-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s50\": {\"status\": \"PREPARING\"}, \"eval-supp-long-adapt-tau025-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-k5-spatial-tau025-s42\": {\"status\": \"PREPARING\"}, \"eval-supp-long-k2mean-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-a1-baseline-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-vla-only-s47-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-adapt-tau025-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-crm-norm005-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s47-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-unified-3suite\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-spatial-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-goal-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}}, \"count\": 200, \"total\": 1047, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2973}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me compile the report.

Key findings:

1. **bjb1-32546 eval-k2-spatial-vla-only-s43-paired-r2**: The log shows it **completed successfully** with 79.5% SR (159/200). GPU 3 is now free.

2. **bjb1-18228 eval-pi05-vla-only-spatial-s43-r2**: The log shows it **completed** with 97.5% SR (195/200). But PID 485043 is dead and GPU 2 has leaked memory (10.4 GB).
   
3. **Old supplementary experiments**: All the supplementary experiments are already marked as done in the registry—the object and goal reconstruction variants, the k2mean and CRM experiments, and the adaptive tau variant all completed successfully, along with the precompute task for pi05 objects.

Now I'm checking through the bjb1-32546 batch to see which experiments are actually present. Some of the spatial variants I'm looking for don't match the exact names in the results—there's eval-supp-spatial-vla-only-s46 which succeeded, but eval-supp-crm-norm005-spatial-s46 isn't showing up in the top results. For the object experiments, I'm finding similar naming mismatches where the s45 versions have different prefixes than expected, though some did complete successfully while others failed.

The key insight is that all the user's original experiments have already transitioned out of RUNNING status—they're in DONE or other states now, so they're not actually zombie processes that need cleanup.

The cqa1-32758 batch is the real problem: these are all marked as RUNNING in the registry but cqa1 is disabled, making them true zombies that need to be addressed. The list includes several spatial variants across different seeds and the k2-adaptive experiments that were running on cqa1.

I'm seeing additional cqa1 experiments that were killed—various k10 adaptive and tau variants across multiple seeds—and now I need to compile all this into a clear report for the user, focusing on what actually needs action versus what's already been resolved. Looking at bjb2-28827, I see several processes that were overwritten or already marked as killed. On bjb1-32546, the K=2 spatial evaluation completed with 79.5% success rate, but it overwrote three other adaptive spatial runs that were in progress on different GPUs. Looking at the job status across these experiment runs, I'm seeing that most have either been overwritten or killed, but there's one eval still actively running on bjb2-40593 with the tau=0.075 parameter — it's progressed to task 8 out of 10 and is currently processing the pick_up_the_black_bowl task.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "db2ed292-d84d-413e-89a1-a34f431a28e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhQQX8zkVoC7n1EvkPEXne",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13114,
      "cache_read_input_tokens": 79939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13114
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

_source line 64_

数据收集完毕。以下是完整报告。

---

## bjb1-18228 (4x GPU)

**实际在跑的实验:**
| GPU | 实验 | PID | 显存 |
|-----|------|-----|------|
| cuda:0 | eval-pi05-adaptive-spatial-s42-r2 | 484291 | 14135 MiB |
| cuda:1 | eval-pi05-vla-only-object-s42-r2 | 484675 | 10365 MiB |
| cuda:3 | precompute-pi05-long-2048-r2 | 114507 | 9883 MiB |

**空闲 GPU:** cuda:2（但有 10429 MiB 泄漏显存，需 GPU reset 回收）

**Zombie 实验（registry RUNNING 但实际已死）:**
- `eval-pi05-vla-only-spatial-s43-r2` (pid 485043, cuda:2) — **已完成** SR=97.5%，进程已退出但显存未释放
- `eval-pi05-vla-only-goal-s42-paired` (pid 446717) — **已完成** SR=98.0%，进程已退出
- `eval-pi05-vla-only-spatial-s42-paired` (pid 446358) — **已完成** SR=98.0%，进程已退出
- `eval-pi05-adaptive-spatial-s42` — conclusion=failed，已死

**用户指定的旧实验:**
- `precompute-pi05-object-2048-r2` — registry 已是 DONE/success，不在 RUNNING 列表

---

## bjb2-28827 (6x GPU)

**实际在跑的实验:**
| GPU | 实验 | PID |
|-----|------|-----|
| cuda:0 | eval-k2-goal-adapt-s45-paired | 639192 |
| cuda:1 | eval-k2-goal-vla-only-s45-paired | 639189 |
| cuda:2 | eval-k2-goal-adapt-s46-paired | 639190 |
| cuda:3 | eval-k2-goal-vla-only-s46-paired | 639199 |
| cuda:4 | eval-k2-goal-adapt-s47-paired | 639193 |
| cuda:5 | eval-k2-goal-vla-only-s47-paired | 639194 |

**空闲 GPU:** 无（6/6 全满）

**Zombie 实验（registry RUNNING 但实际已死）:**
- `eval-k2-tau010-spatial-s42-r3` (cuda:2) — 被 Goal K=2 配对覆盖
- `eval-k2-tau015-spatial-s42-r2` (cuda:0) — 被 Goal K=2 配对覆盖
- `eval-canonical-adaptive-k10-spatial-s44` (conclusion=killed)
- `eval-canonical-adaptive-k10-spatial-s43` (conclusion=killed)

**用户指定的旧实验:**
- eval-supp-obj-reconvla-s47, eval-supp-goal-reconvla-s47, eval-supp-goal-k2mean-s47, eval-supp-goal-crm-norm005-s47, eval-supp-goal-adapt-tau025-s47 — **全部已是 DONE/success**，不在 RUNNING 列表

---

## bjb1-32546 (6x GPU)

**实际在跑的实验:**
| GPU | 实验 | PID |
|-----|------|-----|
| cuda:0 | eval-k2-spatial-adapt-s42-paired-r2 | 978848 |
| cuda:1 | eval-k2-spatial-vla-only-s42-paired-r2 | 980371 |
| cuda:2 | eval-k2-spatial-adapt-s43-paired-r2 | 981563 |
| cuda:4 | eval-k2-spatial-adapt-s44-paired-r2 | 984726 |
| cuda:5 | eval-k2-spatial-vla-only-s44-paired-r2 | 986463 |

**空闲 GPU:** cuda:3

**Zombie 实验（registry RUNNING 但实际已死）:**
- `eval-k2-spatial-vla-only-s43-paired-r2` (cuda:3) — **已完成** SR=79.5%，GPU 3 已释放
- `eval-k2-adaptive-spatial-s49` (cuda:3) — 被 K=2 spatial r2 覆盖
- `eval-k2-adaptive-spatial-s48` (cuda:2) — 被覆盖
- `eval-k2-adaptive-spatial-s46` (cuda:0) — 被覆盖
- `eval-vla-only-spatial-bjb1-s46` — 被覆盖
- `eval-vla-only-spatial-bjb1-s49` (cuda:4) — 被覆盖
- `eval-vla-only-spatial-bjb1-s48` (cuda:1) — 被覆盖
- `eval-k10-tau025-spatial-s46` (killed)
- `eval-canonical-adaptive-k10-spatial-s49` (killed)
- `eval-canonical-adaptive-k10-spatial-s48` (killed)

**用户指定的旧实验:**
- eval-supp-spatial-k2mean-s46, eval-supp-reconvla-obj-s45, eval-smolvla-lerobot-goal-seed43-v3, eval-smolvla-lerobot-spatial-seed43-v3 — **不在 RUNNING registry**（已完成或已终止）

---

## bjb2-40593 (1x GPU)

**实际在跑的实验:**
| GPU | 实验 | PID |
|-----|------|-----|
| cuda:0 | eval-k2-tau0075-spatial-s42 | 349401 |

**空闲 GPU:** 无

**τ=0.075 状态:** 仍在运行，正在跑最后一个 task（task 10/10，rollout 10/20）。预计很快完成。JSON 文件尚未生成。

---

## cqa1-32758 补充（已禁用但 registry 仍标 RUNNING）

以下 12 个实验挂在 cqa1 上，全是 zombie：
- eval-vla-only-spatial-cqa1-s44/s43/s42
- eval-k2-adaptive-spatial-s44/s43/s42
- eval-canonical-adaptive-k10-spatial-s42 (killed)
- eval-k10-tau025-spatial-s47/s45 (killed)
- eval-long-adaptive-k10-s44/s43/s42 (killed)

---

## 总结

| 服务器 | 在跑 | 空闲GPU | Zombie数 |
|--------|------|---------|----------|
| bjb1-18228 | 3 | 1 (cuda:2, 显存泄漏) | 4 |
| bjb2-28827 | 6 | 0 | 4 |
| bjb1-32546 | 5 | 1 (cuda:3) | 10 |
| bjb2-40593 | 1 | 0 | 0 |
| cqa1-32758 | 0 | — | 12 |

Registry 共 45 个 RUNNING，实际只有 **15 个真正在跑**。**30 个 zombie** 需要清理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "uuid": "cd952c53-6ccf-463d-ab50-695393535139",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhQQX8zkVoC7n1EvkPEXne",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13114,
      "cache_read_input_tokens": 79939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13114
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

_source line 65_

数据收集完毕。以下是完整报告。

---

## bjb1-18228 (4x GPU)

**实际在跑的实验:**
| GPU | 实验 | PID | 显存 |
|-----|------|-----|------|
| cuda:0 | eval-pi05-adaptive-spatial-s42-r2 | 484291 | 14135 MiB |
| cuda:1 | eval-pi05-vla-only-object-s42-r2 | 484675 | 10365 MiB |
| cuda:3 | precompute-pi05-long-2048-r2 | 114507 | 9883 MiB |

**空闲 GPU:** cuda:2（但有 10429 MiB 泄漏显存，需 GPU reset 回收）

**Zombie 实验（registry RUNNING 但实际已死）:**
- `eval-pi05-vla-only-spatial-s43-r2` (pid 485043, cuda:2) — **已完成** SR=97.5%，进程已退出但显存未释放
- `eval-pi05-vla-only-goal-s42-paired` (pid 446717) — **已完成** SR=98.0%，进程已退出
- `eval-pi05-vla-only-spatial-s42-paired` (pid 446358) — **已完成** SR=98.0%，进程已退出
- `eval-pi05-adaptive-spatial-s42` — conclusion=failed，已死

**用户指定的旧实验:**
- `precompute-pi05-object-2048-r2` — registry 已是 DONE/success，不在 RUNNING 列表

---

## bjb2-28827 (6x GPU)

**实际在跑的实验:**
| GPU | 实验 | PID |
|-----|------|-----|
| cuda:0 | eval-k2-goal-adapt-s45-paired | 639192 |
| cuda:1 | eval-k2-goal-vla-only-s45-paired | 639189 |
| cuda:2 | eval-k2-goal-adapt-s46-paired | 639190 |
| cuda:3 | eval-k2-goal-vla-only-s46-paired | 639199 |
| cuda:4 | eval-k2-goal-adapt-s47-paired | 639193 |
| cuda:5 | eval-k2-goal-vla-only-s47-paired | 639194 |

**空闲 GPU:** 无（6/6 全满）

**Zombie 实验（registry RUNNING 但实际已死）:**
- `eval-k2-tau010-spatial-s42-r3` (cuda:2) — 被 Goal K=2 配对覆盖
- `eval-k2-tau015-spatial-s42-r2` (cuda:0) — 被 Goal K=2 配对覆盖
- `eval-canonical-adaptive-k10-spatial-s44` (conclusion=killed)
- `eval-canonical-adaptive-k10-spatial-s43` (conclusion=killed)

**用户指定的旧实验:**
- eval-supp-obj-reconvla-s47, eval-supp-goal-reconvla-s47, eval-supp-goal-k2mean-s47, eval-supp-goal-crm-norm005-s47, eval-supp-goal-adapt-tau025-s47 — **全部已是 DONE/success**，不在 RUNNING 列表

---

## bjb1-32546 (6x GPU)

**实际在跑的实验:**
| GPU | 实验 | PID |
|-----|------|-----|
| cuda:0 | eval-k2-spatial-adapt-s42-paired-r2 | 978848 |
| cuda:1 | eval-k2-spatial-vla-only-s42-paired-r2 | 980371 |
| cuda:2 | eval-k2-spatial-adapt-s43-paired-r2 | 981563 |
| cuda:4 | eval-k2-spatial-adapt-s44-paired-r2 | 984726 |
| cuda:5 | eval-k2-spatial-vla-only-s44-paired-r2 | 986463 |

**空闲 GPU:** cuda:3

**Zombie 实验（registry RUNNING 但实际已死）:**
- `eval-k2-spatial-vla-only-s43-paired-r2` (cuda:3) — **已完成** SR=79.5%，GPU 3 已释放
- `eval-k2-adaptive-spatial-s49` (cuda:3) — 被 K=2 spatial r2 覆盖
- `eval-k2-adaptive-spatial-s48` (cuda:2) — 被覆盖
- `eval-k2-adaptive-spatial-s46` (cuda:0) — 被覆盖
- `eval-vla-only-spatial-bjb1-s46` — 被覆盖
- `eval-vla-only-spatial-bjb1-s49` (cuda:4) — 被覆盖
- `eval-vla-only-spatial-bjb1-s48` (cuda:1) — 被覆盖
- `eval-k10-tau025-spatial-s46` (killed)
- `eval-canonical-adaptive-k10-spatial-s49` (killed)
- `eval-canonical-adaptive-k10-spatial-s48` (killed)

**用户指定的旧实验:**
- eval-supp-spatial-k2mean-s46, eval-supp-reconvla-obj-s45, eval-smolvla-lerobot-goal-seed43-v3, eval-smolvla-lerobot-spatial-seed43-v3 — **不在 RUNNING registry**（已完成或已终止）

---

## bjb2-40593 (1x GPU)

**实际在跑的实验:**
| GPU | 实验 | PID |
|-----|------|-----|
| cuda:0 | eval-k2-tau0075-spatial-s42 | 349401 |

**空闲 GPU:** 无

**τ=0.075 状态:** 仍在运行，正在跑最后一个 task（task 10/10，rollout 10/20）。预计很快完成。JSON 文件尚未生成。

---

## cqa1-32758 补充（已禁用但 registry 仍标 RUNNING）

以下 12 个实验挂在 cqa1 上，全是 zombie：
- eval-vla-only-spatial-cqa1-s44/s43/s42
- eval-k2-adaptive-spatial-s44/s43/s42
- eval-canonical-adaptive-k10-spatial-s42 (killed)
- eval-k10-tau025-spatial-s47/s45 (killed)
- eval-long-adaptive-k10-s44/s43/s42 (killed)

---

## 总结

| 服务器 | 在跑 | 空闲GPU | Zombie数 |
|--------|------|---------|----------|
| bjb1-18228 | 3 | 1 (cuda:2, 显存泄漏) | 4 |
| bjb2-28827 | 6 | 0 | 4 |
| bjb1-32546 | 5 | 1 (cuda:3) | 10 |
| bjb2-40593 | 1 | 0 | 0 |
| cqa1-32758 | 0 | — | 12 |

Registry 共 45 个 RUNNING，实际只有 **15 个真正在跑**。**30 个 zombie** 需要清理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 263438,
  "duration_api_ms": 254597,
  "num_turns": 26,
  "stop_reason": "end_turn",
  "session_id": "c79219db-3b3a-40b4-8a6d-753b2be27bab",
  "total_cost_usd": 1.062155,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 81212,
    "cache_read_input_tokens": 289170,
    "output_tokens": 16336,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 81212,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 4044,
        "cache_read_input_tokens": 79939,
        "cache_creation_input_tokens": 13114,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 13114
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1470,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001545,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 16336,
      "cacheReadInputTokens": 289170,
      "cacheCreationInputTokens": 81212,
      "webSearchRequests": 0,
      "costUSD": 1.06061,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "81e9ddc2-cf57-423d-8048-46820f2058d3"
}
```

</details>

---
