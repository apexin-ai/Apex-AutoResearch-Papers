# ssh d3 instance failure analysis

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_ssh_d3-instance-failure-analysis_20260520T092219.log`
- **Structured JSON:** [`d1d4237fe7e4c253226b.json`](../../sessions/d1/d1d4237fe7e4c253226b.json)

## Before a recorded user message

16 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
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
  "uuid": "d32f40b0-e8e3-4fab-a0c0-8a938bff33c7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1779282600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e3ba36a1-f3df-43ad-996e-40b7e781e25b",
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down this task:

1. Connect to autodl-5090 server, verify hostname
2. Find samples.jsonl files in the output directory
3. Analyze entity construction failures across multiple dimensions
4. Write analysis results to local artifacts

Let me start by connecting to the server and exploring the data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "265ceaf9-b985-4819-984d-5a55e6dbe599",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KjN6qzEa1Qx66LBXkgnNRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12195,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12195
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

### Assistant

_source line 5_

先连接服务器探测数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "78587dd2-038c-4bca-b25b-0f87268aace5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KjN6qzEa1Qx66LBXkgnNRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12195,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12195
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

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ENBZ7CGJ4uiMYyFFtWHCs4`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
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
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "91e94849-dfe9-453c-a5cd-b778631390c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KjN6qzEa1Qx66LBXkgnNRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12195,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12195
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

_source line 7 · 2026-05-20T09:22:35.092Z_

<details><summary>↩ Tool result · `toolu_01ENBZ7CGJ4uiMYyFFtWHCs4`</summary>

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
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "7ff59c10-7b15-4414-a3af-2e32edeaa012",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
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
Let me start by connecting to the server to verify hostname and find the samples.jsonl files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "ce83ad16-b133-4b4d-b37a-57a7327c407a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7wgsU5YZu3SdAu3GnwyU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2178,
      "cache_read_input_tokens": 23896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2178
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EVYFZ1gG1rSxr9Kccg458M`</summary>

```json
{
  "server": "autodl-5090",
  "command": "hostname",
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
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "e6639229-c50a-4632-8339-e6b1d6949ef2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7wgsU5YZu3SdAu3GnwyU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2178,
      "cache_read_input_tokens": 23896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2178
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

_source line 10 · 2026-05-20T09:22:39.145Z_

<details><summary>↩ Tool result · `toolu_01EVYFZ1gG1rSxr9Kccg458M`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'hostname' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "1381858d-0cea-4dae-a700-4dad675e5e93",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'hostname' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'hostname' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0116rd5S4ZWzM52WWk5W7Bzu`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"samples.jsonl\" -exec sh -c 'echo \"$(dirname \"$1\"): $(wc -l < \"$1\") instances\"' _ {} \\;",
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
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "0342a284-d5bf-4d04-8ad0-18d7889e5878",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7wgsU5YZu3SdAu3GnwyU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2178,
      "cache_read_input_tokens": 23896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2178
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

_source line 12 · 2026-05-20T09:22:39.956Z_

<details><summary>↩ Tool result · `toolu_0116rd5S4ZWzM52WWk5W7Bzu`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "5ca1fcd8-cf0b-4277-a3b2-d2aeaecd437b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01SQ41Thi3TtYExmejzcQs58`</summary>

```json
{
  "server": "autodl-5090",
  "command": "hostname",
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
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "7c9d2247-3476-43fc-bde9-c38923afac82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mqt34cJceaMT1rFcZrALeE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 526,
      "cache_read_input_tokens": 26074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 526
      },
      "output_tokens": 67,
      "service_tier": "standard",
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01HXQuwxGvEJc1fh4CZMMZiV`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"samples.jsonl\" | while read f; do lines=$(wc -l < \"$f\"); dir=$(dirname \"$f\"); echo \"$dir: $lines instances\"; done",
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
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "1b3acc32-388c-48e7-8912-abe6343a3ff7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mqt34cJceaMT1rFcZrALeE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 526,
      "cache_read_input_tokens": 26074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 526
      },
      "output_tokens": 67,
      "service_tier": "standard",
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

_source line 15 · 2026-05-20T09:22:43.952Z_

<details><summary>↩ Tool result · `toolu_01SQ41Thi3TtYExmejzcQs58`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"autodl-container-31eb41bf76-61568de9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "0014f1b7-54e2-4ad0-8d20-c97b85880765",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"autodl-container-31eb41bf76-61568de9\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.1}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"autodl-container-31eb41bf76-61568de9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T09:22:47.200Z_

<details><summary>↩ Tool result · `toolu_01HXQuwxGvEJc1fh4CZMMZiV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/gate0_ft002v2: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/gate0_ft002v2_ckpt400: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2_r1024: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42_200only_backup: 200 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_200only: 200 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed456_200only: 200 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16_200only: 200 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_seed456_t10_full: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_seed123_t10_full: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16_t10_full: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_pilot: 1287 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_dryrun: 3 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval: 1287 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_dryrun: 3 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2_ner: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_003_wnut17_v2_infer: 1287 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123_r1024: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456_r1024: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16_r1024: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_018_qwen_scierc_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_018_qwen_scierc_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/ou\\n\\n... [截断: 输出过长，省略 2279 字符] ...\\n\\nference: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_020_pilot: 200 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/shard_0: 9412 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/shard_2: 9412 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/shard_1: 9412 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/shard_3: 9412 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/shard_0: 1250 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/shard_1: 1250 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/shard_2: 1250 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/shard_3: 1250 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16: 5000 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_T05: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_T08: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_T12: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_028_fewnerd_5epoch: 5000 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_029a_scierc_3epoch: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_029b_scierc_10epoch: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n8_seed456: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n8_seed123: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_030_conll_t12: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_031_fewnerd_t12: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_scierc_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed789_shard0: 12549 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed789_shard1: 12549 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed789_shard2: 12550 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_fewnerd_s123: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_fewnerd_s42: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_fewnerd_s456: 37648 instances\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.23}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d0fab042-1d58-46d2-97a9-896c695d2f14",
  "uuid": "499f2098-6a66-4025-8b24-78d2581e7a93",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/gate0_ft002v2: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/gate0_ft002v2_ckpt400: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2_r1024: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42_200only_backup: 200 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_200only: 200 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed456_200only: 200 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16_200only: 200 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed456: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_seed456_t10_full: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_seed123_t10_full: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16_t10_full: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_pilot: 1287 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_dryrun: 3 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval: 1287 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_dryrun: 3 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_seed123: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2_ner: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_003_wnut17_v2_infer: 1287 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123_r1024: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456_r1024: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16_r1024: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_018_qwen_scierc_seed456: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed456: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_018_qwen_scierc_seed123: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/ou\\\\n\\\\n... [截断: 输出过长，省略 2279 字符] ...\\\\n\\\\nference: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_020_pilot: 200 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/shard_0: 9412 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/shard_2: 9412 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/shard_1: 9412 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/shard_3: 9412 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference: 37648 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/shard_0: 1250 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/shard_1: 1250 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/shard_2: 1250 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/shard_3: 1250 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16: 5000 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_T05: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_T08: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_T12: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_028_fewnerd_5epoch: 5000 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_029a_scierc_3epoch: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_029b_scierc_10epoch: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123: 37648 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456: 37648 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n8_seed456: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n8_seed123: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_030_conll_t12: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_031_fewnerd_t12: 37648 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_scierc_seed123: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456: 3453 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed123: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed123: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed123: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed456: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed456: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed456: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed123: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed456: 551 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed789_shard0: 12549 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed789_shard1: 12549 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed789_shard2: 12550 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged: 37648 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_fewnerd_s123: 37648 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_fewnerd_s42: 37648 instances\\\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_fewnerd_s456: 37648 instances\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.23}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/gate0_ft002v2: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/gate0_ft002v2_ckpt400: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2_r1024: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42_200only_backup: 200 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_200only: 200 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed456_200only: 200 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16_200only: 200 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_seed456_t10_full: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_seed123_t10_full: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16_t10_full: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_pilot: 1287 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_dryrun: 3 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval: 1287 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_dryrun: 3 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2_ner: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_003_wnut17_v2_infer: 1287 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123_r1024: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456_r1024: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16_r1024: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_018_qwen_scierc_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_018_qwen_scierc_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/ou\\n\\n... [截断: 输出过长，省略 2279 字符] ...\\n\\nference: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_020_pilot: 200 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/shard_0: 9412 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/shard_2: 9412 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/shard_1: 9412 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/shard_3: 9412 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/shard_0: 1250 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/shard_1: 1250 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/shard_2: 1250 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/shard_3: 1250 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16: 5000 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_T05: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_T08: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_T12: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_028_fewnerd_5epoch: 5000 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_029a_scierc_3epoch: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_029b_scierc_10epoch: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n8_seed456: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n8_seed123: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_030_conll_t12: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_031_fewnerd_t12: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_scierc_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456: 3453 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed123: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed456: 551 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed789_shard0: 12549 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed789_shard1: 12549 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed789_shard2: 12550 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_fewnerd_s123: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_fewnerd_s42: 37648 instances\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_fewnerd_s456: 37648 instances\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.23}}"
    }
  }
}
```

</details>

---
