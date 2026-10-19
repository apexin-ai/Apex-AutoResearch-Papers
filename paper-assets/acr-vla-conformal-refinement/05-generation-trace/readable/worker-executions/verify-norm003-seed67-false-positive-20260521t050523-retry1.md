# verify norm003 seed67 false positive 20260521T050523 retry1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_verify_norm003-seed67-false-positive_20260521T050523_retry1.log`
- **Structured JSON:** [`9ec7808d40e406ab1835.json`](../../sessions/9e/9ec7808d40e406ab1835.json)

## Before a recorded user message

40 recorded events

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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
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
  "model": "claude-opus-4-7[1m]",
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
  "uuid": "ad8c63c4-37cd-4014-acf4-f2a0f2999457",
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
    "resetsAt": 1779343800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6cf32bc2-9a2f-4746-8663-d0f0d68c9cc9",
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "6e8de9ec-f982-4c98-8df6-bbcf71be3195",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NRvXtJuSrDMrHscm976Li7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14704,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14704
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017gs9CP27RMCUjw2jGWJsh5`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "b38b5090-9fa9-4839-a56f-6a7301182392",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NRvXtJuSrDMrHscm976Li7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14704,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14704
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

_source line 6 · 2026-05-21T05:05:45.048Z_

<details><summary>↩ Tool result · `toolu_017gs9CP27RMCUjw2jGWJsh5`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "cf345c10-f6e5-4508-a5c7-10d76e19bd72",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_017TgghztVuMeTh8fAiVQk9F`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "eval-obs-only-object-norm003-seed67"
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "0cb3be24-9a8f-4db1-ab18-09e946e5c1cd",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NxqUS9M77hjaLBgsp2KiDU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16764,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16764
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28772
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T05:05:52.503Z_

<details><summary>↩ Tool result · `toolu_017TgghztVuMeTh8fAiVQk9F`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6332}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "55b197d9-a0a3-4ddb-8335-ddcb838d5f09",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.6332}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6332}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_015LnMd5ZabxCvKZUQPjy8tX`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "id": "eval-obs-only-object-norm003-seed67"
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "dbebb02d-d9bb-40e9-806c-d42734ac8656",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01YPuhGRX9HgbGv55oUVFsHz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 33098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 270
      },
      "output_tokens": 69,
      "service_tier": "standard",
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

_source line 10 · 2026-05-21T05:06:00.092Z_

<details><summary>↩ Tool result · `toolu_015LnMd5ZabxCvKZUQPjy8tX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3953}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "4afa906a-d8b1-4679-93fa-9ec86aa27106",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.3953}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3953}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011qJrT9xxmVdYqLDxvpsP1K`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "name": "eval-obs-only-object-norm003-seed67"
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "1d25e23e-975b-4e5c-a317-93b42d2c5646",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Q3j8BoGt1RJLt1sUCxWJh3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 33368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 261
      },
      "output_tokens": 69,
      "service_tier": "standard",
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

_source line 12 · 2026-05-21T05:06:04.849Z_

<details><summary>↩ Tool result · `toolu_011qJrT9xxmVdYqLDxvpsP1K`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3503}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "efb69a5f-9808-4cc6-89c9-a962f626d81e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.3503}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3503}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "1db0c8d1-0e5f-406f-b6ae-80e79c461801",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012qqLTnqGJdqukHzuaKqUx8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 33629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 261
      },
      "output_tokens": 42,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01HSABKj6mNZw5ScMyD38QLJ`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": 0,
  "fields": [
    "server",
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "7ad5631f-ccd6-4108-a791-1b8baf3248b7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012qqLTnqGJdqukHzuaKqUx8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 33629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 261
      },
      "output_tokens": 42,
      "service_tier": "standard",
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

_source line 15 · 2026-05-21T05:06:10.154Z_

<details><summary>↩ Tool result · `toolu_01HSABKj6mNZw5ScMyD38QLJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"RUNNING\", \"server\": \"bjb1-18228\", \"conclusion\": \"failed\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb2-40593\", \"conclusion\": \"success\"}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed42-r3\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"DONE\", \"server\": \"bjb2-40593\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed76\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed77\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed76\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed77\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed63-r3\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed76\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed62-r3\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed78\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed77\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed75\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed51-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed52-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"RUNNING\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"RUNNING\", \"server\": \"bjb1-18228\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"RUNNING\", \"server\": \"bjb1-18228\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed61\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed64-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed63\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed62\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed52-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed55-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-openvla-crm-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed55\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-seed54\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed45\": {\"status\": \"DEPLOYED\", \"conclusion\": \"success\"}, \"eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-openvla-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"openvla-precompute-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed42-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed44-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed44-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-k1-object-seed43-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-k1-object-seed42-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-latency-profiling-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-goal-norm02-seed53\": {\"status\": \"PREPARING\"}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-adaptive-k-spatial-p50-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-k-spatial-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"latency-profile-n1000\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed54\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"calibrate-crm-correction-signal\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-crm-long-seed54\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed54\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed53\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed53\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed52\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed49\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed52\": {\"status\": \"PREPARING\"}, \"eval-vla-only-goal-seed52\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed53\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed51\": {\"status\": \"PREPARING\"}, \"eval-vla-only-goal-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed49\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed48\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed48\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed47\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-seed48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed51\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed51\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed49\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed44\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-spatial-seed47\": {\"status\": \"PREPARING\"}, \"eval-vla-only-object-seed49-r2\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42-r2\": {\"status\": \"PREPARING\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed49-r2\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"fmvd-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed46-r2\": {\"status\": \"DEPLOYED\", \"conclusion\": \"killed\"}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-k5\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-40593\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-40593\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object\": {\"status\": \"DEPLOYED\", \"server\": \"bjb2-28827\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-k5\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}}, \"count\": 556, \"total\": 556, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.567}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "df87fe0b-921a-4f66-b6a2-d8a8e00a6a7d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-k20-obs-only-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k20-obs-only-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k20-obs-only-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-object-k20-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-object-k20-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed67\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm02-seed53\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed52\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed51\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed48-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-baseline-object-seed42-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm005-seed67\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed67\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed66\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-vla-only-object-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-plan-a-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-plan-a-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-plan-a-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-plan-a-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-plan-a-spatial-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-plan-a-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed42-r3\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-seed50\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-spatial-k10-seed50\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-spatial-k10-seed49\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm02-k20-seed44\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm02-k20-seed43\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm02-k20-seed42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm01-seed60\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-baseline-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm003-seed76\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm01-seed54\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed53\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed52\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed55\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed44-bjb2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed57\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed65\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed61\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed58\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed59\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed56\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed77\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm01-seed76\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm005-seed77\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm003-seed63-r3\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm005-seed76\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm003-seed62-r3\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm003-seed78\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm003-seed77\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm005-seed75\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed74\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed72\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed63-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm01-seed71\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed62-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm003-seed73\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed51-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed52-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed65\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed64\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed64\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed65\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed64\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p90-seed44-bjb2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-obs-only-object-norm003-seed66\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"server\\\": \\\"bjb1-18228\\\"}, \\\"eval-obs-only-object-norm01-seed66\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"server\\\": \\\"bjb1-18228\\\"}, \\\"eval-obs-only-object-norm005-seed62\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm005-seed63\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm01-seed61\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm003-seed64-bjb2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm003-seed63\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm003-seed62\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm01-seed51-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm01-seed52-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm01-seed51\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed49-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm005-seed55-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-openvla-crm-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-obs-only-object-norm003-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k5-obs-only-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-seed52\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed55\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm02-seed54\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"D088-eval-adaptive-unc-head-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"D088-eval-adaptive-unc-head-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"D088-eval-adaptive-unc-head-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm005-seed45\\\": {\\\"status\\\": \\\"DEPLOYED\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-unc-head-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-adaptive-unc-head-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-perdof-object-norm02-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-adaptive-unc-head-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-random-selection-spatial-seed42-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train-crm-openvla-obs-only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"openvla-precompute-k1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed46-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm02-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-seed42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k5-obs-only-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-spatial-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-spatial-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-k1-object-seed43-plan702\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-k1-object-seed42-plan702\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-k1-object-seed44-plan702\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-random-selection-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-spatial-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-spatial-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-spatial-norm02-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p90-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-argmin-object-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed48-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-goal-seed51\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-spatial-seed42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-k1-object-seed44-plan702-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-crm-k1-object-seed43-plan702-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-crm-k1-object-seed42-plan702-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-perdof-object-norm02-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-argmin-object-k5-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-goal-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-seed46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-latency-profiling-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p75-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-goal-norm02-seed51\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p25-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-openvla-object-baseline-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-argmin-object-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-goal-norm02-seed53\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-argmin-object-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-goal-norm02-seed52\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p90-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm02-seed45-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p90-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-goal-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-random-selection-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-adaptive-k-spatial-p50-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p50-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p50-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p25-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-adaptive-k-spatial-p25-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p75-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-object-k20-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-long-seed49-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p75-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p50-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-p75-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-p75-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-p50-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-p50-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p50-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"latency-profile-n1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-p90-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-long-seed54\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-adaptive-k-p25-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-spatial-k10-seed51\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-goal-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-long-seed52\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-long-seed51\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-long-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-long-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-p25-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"calibrate-crm-correction-signal\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-crm-long-seed54\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-seed54\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-long-seed53\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-seed53\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-seed52\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-goal-seed50\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-goal-seed49\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-long-seed52\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-goal-seed52\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-long-seed53\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-long-seed51\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-goal-seed50\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-long-seed49\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-long-seed48\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-goal-seed48\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-goal-seed47\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-spatial-seed48\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-spatial-seed51\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-adaptive-k-p25-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-goal-seed48-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-vla-only-goal-seed47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-crm-goal-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed51\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-long-seed49\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-adaptive-k-p50-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-p75-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-p90-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-p90-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-p25-seed44\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-spatial-seed47\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-object-seed49-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-long-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-long-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-long-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-goal-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-goal-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-openvla-object-baseline-seed42-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"k2-l2-calibration-phase1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-long-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-spatial-seed49-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-vla-only-goal-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-vla-only-goal-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-goal-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-long-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-long-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-long-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-goal-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-goal-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-spatial-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-long-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-goal-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-crm-goal-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-vla-only-goal-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-goal-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-long-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"fmvd-calibration-phase1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-vla-only-long-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm003-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm005-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-long-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-long-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-long-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-spatial-norm02-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-argmin-object-k5-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-vla-only-goal-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-random-selection-object-k5-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-k5-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-k5-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-k5-seed42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-k5-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-k5-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_602-latency-profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-spatial-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm005-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-spatial-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-default-seed48-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-k5-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-spatial-norm02-k5-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-random-selection-object-k5-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-random-selection-object-k5-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-random-selection-object-k5-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-random-selection-object-k5-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-spatial-norm02-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm01-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-default-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-argmin-object-k5-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-argmin-object-k5-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-argmin-object-k5-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm03-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train-crm-k1-accg-object-seed42-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_701-precompute-k1-spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_701-crm-k1-train\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_obs_only_norm03_seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_obs_only_norm01_seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-lto-splitA-vla-only-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-lto-splitA-vla-only-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-lto-splitA-heldout-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"crm-lto-splitA-train\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm003-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-scalar-object-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-obs-only-spatial-norm02-k5-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-k5-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-norm02-k5-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-k5-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-lto-splitA-vla-only-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-lto-splitA-heldout-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-perdof-object-default-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-perdof-object-norm03-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-default-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm003-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm005-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm003-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm02-k5-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm01-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-default-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm03-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm03-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-scalar-object-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-lto-splitA-vla-only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-lto-splitA-heldout\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm005-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-perdof-object-norm03-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm003-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"crm-lto-splitA-train-fixed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-perdof-object-norm003-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm005-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-default-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-default-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-k5-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm005-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm02-k5-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm003-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-perdof-object-norm01-seed42\\\": {\\\"status\\\": \\\"DEPLOYED\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed42\\\": {\\\"status\\\": \\\"DEPLOYED\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed46-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm005-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm003-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm03-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-k5-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm01-seed42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm01-seed42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-perdof-object-norm02-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm01-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-obs-only-object-norm01-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-k5-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-default-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-perdof-object-default-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-mag-perdof-norm02\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-spatial-v4-scalar\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-spatial-v4-small\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-spatial-v4-obs-only-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-argmin-only-spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-spatial-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-object-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-openvla-object-vla-only-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-perdof-object-norm02-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-default-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm02-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm01-seed46-r2\\\": {\\\"status\\\": \\\"DEPLOYED\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mag_obs_only_norm01_seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mag_obs_only_norm01_seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-perdof-object-norm02-seed43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mag_perdof_norm02_seed43_r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-perdof-object-norm01-seed47-bjb1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-openvla-object-vla-only-seed42-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k1-crm-multiscale-object-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-k1-crm-multiscale-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-k1-crm-multiscale-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-k1-crm-multiscale-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-perdof-object-norm01-seed46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k1-crm-multiscale-object-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-perdof-object-norm02-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm005-seed43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"plan_602-latency-profile\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train-crm-k1-accg-object-seed42-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k1-crm-accg-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-k1-crm-accg-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-k1-crm-accg-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-obs-only-object-default-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-scalar-object-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm02-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm02-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train-crm-k1-accg-object-seed42-fallback\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train-crm-k1-accg-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-perdof-object-norm02-seed45-deploy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm01-seed47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-perdof-object-norm03-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-perdof-object-norm03-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-obs-only-object-norm03-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-perdof-object-norm03-seed46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-perdof-object-norm01-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-obs-only-object-norm01-seed47-bjb2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm01-seed46-bjb2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-argmin-object-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm01-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm01-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-argmin-object-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm03-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-mean-object-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-argmin-object-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-direct-correction-object-seed42-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm03-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-mag-perdof-norm02-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-acr-object-v4-scalar\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-mag-obsonly-norm02\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-mag-perdof-norm03\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-mag-perdof-norm005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-mag-perdof-norm003\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-vla-mean-spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-object-obs-only-norm02\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-spatial-v7-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-object-v8-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-v5-shard2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-v5-shard1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-v5-shard0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-v4-shard2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-v4-shard1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-v4-shard0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-mean-spatial-t10\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-reconvla-spatial-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"crm-train-v2-scalar-unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"crm-train-v2-perdof\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"crm-train-v2-obs-only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-shard2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-shard1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-shard0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-k5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_014-reconvla-baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan_001-crm-smolvla\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mvp-point-reaching\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-smolvla-libero-spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-default-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm005-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm02-seed43-object-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm03-object-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm003-b2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm03-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm005-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-direct-correction-object-seed42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-direct-correction-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-scalar-object-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-perdof-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-obs-only-object-norm03-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-mean-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed44-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-argmin-object-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm03-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-acr-object-v4-default-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm003-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-object-obs-only-default\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-scalar-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm003-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-scalar-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm02-seed44-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-argmin-object-seed44-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-vla-mean-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm02-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-argmin-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-mag-obsonly-norm03-b2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-argmin-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm02-seed43-object-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-obsonly-norm03\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-obsonly-norm02-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-obsonly-norm03-b4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-obsonly-norm03-b3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-perdof-norm02-seed43-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-perdof-norm03-object-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-object-v4-scalar-b2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-object-v4-obs-only-b2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-spatial-v4-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-reconvla-spatial-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-object-v6-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-v3-shard2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-v3-shard1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-v3-shard0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-v2-shard2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-v2-shard1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-v2-shard0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-perdof-norm0p3-object-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-perdof-norm0p3-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm02-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-acr-object-v4-default\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-perdof-norm03-object\\\": {\\\"status\\\": \\\"DEPLOYED\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-obsonly-norm03-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-mean-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-reconvla-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-object-v4-obs-only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-object-v4-perdof\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-spatial-v4-scalar-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-spatial-v4-obs-only-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-acr-spatial-v4-small-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm-0.3-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-obsonly-norm-0p3-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-argmin-only-spatial-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm003\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-vla-only-object-k1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-acr-spatial-v4-default-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-tiny-correction-spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-spatial-v4-default-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-spatial-v4-obs-only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-acr-spatial-v4-default\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"crm-train-v3-norm-scalar-unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"crm-train-v3-norm-obs-only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"crm-train-v3-norm\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"crm-train-v3-scalar-unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"crm-train-v3-obs-only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"crm-train-v3-perdof\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-spatial-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-scalar-unc-spatial-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"crm-train-a4-scalar-unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"crm-train-a3-obs-only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"crm-train-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"crm-train-k5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-scalar-unc-spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-spatial-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-k5-spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-object-v7-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-spatial-v6-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-object-v5-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-vla-spatial-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-spatial-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-reconvla-spatial-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-object-v4-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-spatial-v5-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-spatial-v3-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-spatial-reeval-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}}, \\\"count\\\": 556, \\\"total\\\": 556, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.567}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"RUNNING\", \"server\": \"bjb1-18228\", \"conclusion\": \"failed\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb2-40593\", \"conclusion\": \"success\"}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed42-r3\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"DONE\", \"server\": \"bjb2-40593\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed76\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed77\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed76\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed77\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed63-r3\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed76\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed62-r3\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed78\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed77\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed75\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed51-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed52-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"RUNNING\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"RUNNING\", \"server\": \"bjb1-18228\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"RUNNING\", \"server\": \"bjb1-18228\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed61\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed64-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed63\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed62\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed52-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed55-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-openvla-crm-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed55\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-seed54\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed45\": {\"status\": \"DEPLOYED\", \"conclusion\": \"success\"}, \"eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-openvla-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"openvla-precompute-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed42-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed44-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed44-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-k1-object-seed43-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-k1-object-seed42-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-latency-profiling-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-goal-norm02-seed53\": {\"status\": \"PREPARING\"}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-adaptive-k-spatial-p50-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-k-spatial-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"latency-profile-n1000\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed54\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"calibrate-crm-correction-signal\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-crm-long-seed54\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed54\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed53\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed53\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed52\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed49\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed52\": {\"status\": \"PREPARING\"}, \"eval-vla-only-goal-seed52\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed53\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed51\": {\"status\": \"PREPARING\"}, \"eval-vla-only-goal-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed49\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed48\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed48\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed47\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-seed48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed51\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed51\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed49\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed44\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-spatial-seed47\": {\"status\": \"PREPARING\"}, \"eval-vla-only-object-seed49-r2\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42-r2\": {\"status\": \"PREPARING\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed49-r2\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"fmvd-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed46-r2\": {\"status\": \"DEPLOYED\", \"conclusion\": \"killed\"}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-k5\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-40593\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-40593\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object\": {\"status\": \"DEPLOYED\", \"server\": \"bjb2-28827\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-k5\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}}, \"count\": 556, \"total\": 556, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.567}}"
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "5318fe32-b3d3-448b-bc6a-082f173a314d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011EaecfQR6sukVj6VJFupSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27199,
      "cache_read_input_tokens": 33890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27199
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01RCcL3J5G1CrfzPVtPbZgjb`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "eval-obs-only-object-norm003-seed67"
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "208f69c6-81e5-4bf3-a93f-60d32314a095",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011EaecfQR6sukVj6VJFupSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27199,
      "cache_read_input_tokens": 33890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27199
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 18 · 2026-05-21T05:06:19.626Z_

<details><summary>↩ Tool result · `toolu_01RCcL3J5G1CrfzPVtPbZgjb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.3114}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "fa50f9cc-6094-4cdf-9034-b798d4197950",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.3114}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.3114}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01E66dXrmZ3NQmWrrEvojAi9`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "server": "bjb2-28827",
    "conclusion": "failed"
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "162ef354-d1f1-4529-9b4b-841de4cc09b1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RdAJ2PkxFsUEiktKuqXreg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 332,
      "cache_read_input_tokens": 61089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 332
      },
      "output_tokens": 69,
      "service_tier": "standard",
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

_source line 20 · 2026-05-21T05:06:26.374Z_

<details><summary>↩ Tool result · `toolu_01E66dXrmZ3NQmWrrEvojAi9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T05:00:11.340Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 969788, \"seed\": 67, \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:5\"}, \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"failed\", \"log_path\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"reproduce\": {\"finished_at\": \"2026-05-21T04:59:55.277Z\"}, \"completed_at\": \"2026-05-21T04:59:59.475Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:00:37.585302+00:00\"}]}}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:50:46.149Z\", \"updated_at\": \"2026-05-18T21:55:07.741Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve：perdof ε=0.05 当前 n=2 (seed42=14%, seed44=9%), seed43 在跑。第 4 个 seed 强化低 ε 端 error bars。\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T15:51:08.830Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed45.json\", \"finished_at\": \"2026-05-18T21:53:11.259Z\", \"training_hours\": 6.03}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"598900\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed45.log\", \"submitted_at\": \"2026-05-18T15:51:11.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21723.3, \"gpu_hours\": 6.03}, \"pid\": \"598900\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed45.log\", \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T21:53:14.790Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:53:20.362616+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=124 timeout (wall_clock=6.03h, timeout_hours 过低) | 已知失败模式: LIBERO-Object 全量 eval 需 12-14h，6h timeout 不够 | 建议: 重提交 timeout_hours=16\"}}, \"count\": 2, \"total\": 2, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0139}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "81cd6568-d64a-4220-9fa2-3a989343ae64",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-obs-only-object-norm003-seed67\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:35:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:00:11.340Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": 969788, \\\"seed\\\": 67, \\\"spec\\\": {\\\"command\\\": \\\"detected on GPU, submitted by prior Worker but not registered\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/acr-vla-conformal-refinement/\\\", \\\"data_count\\\": \\\"100 rollouts\\\", \\\"model_name\\\": \\\"crm_v3_norm/obs_only\\\", \\\"seed\\\": 67, \\\"gpu\\\": \\\"cuda:5\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.14}, \\\"conclusion\\\": \\\"failed\\\", \\\"log_path\\\": \\\"/root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T04:59:55.277Z\\\"}, \\\"completed_at\\\": \\\"2026-05-21T04:59:59.475Z\\\", \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T05:00:37.585302+00:00\\\"}]}}, \\\"eval-perdof-object-norm005-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T15:50:46.149Z\\\", \\\"updated_at\\\": \\\"2026-05-18T21:55:07.741Z\\\", \\\"hypothesis\\\": \\\"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve：perdof ε=0.05 当前 n=2 (seed42=14%, seed44=9%), seed43 在跑。第 4 个 seed 强化低 ε 端 error bars。\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-18T15:51:08.830Z\\\", \\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed45.json\\\", \\\"finished_at\\\": \\\"2026-05-18T21:53:11.259Z\\\", \\\"training_hours\\\": 6.03}, \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed45.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"598900\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed45.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T15:51:11.483Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 21723.3, \\\"gpu_hours\\\": 6.03}, \\\"pid\\\": \\\"598900\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed45.log\\\", \\\"failure_reason\\\": \\\"EXIT_CODE=124 (timeout — exceeded timeout_hours)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-18T21:53:14.790Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-18T21:53:20.362616+00:00\\\"}]}, \\\"notes\\\": \\\"失败原因: EXIT_CODE=124 timeout (wall_clock=6.03h, timeout_hours 过低) | 已知失败模式: LIBERO-Object 全量 eval 需 12-14h，6h timeout 不够 | 建议: 重提交 timeout_hours=16\\\"}}, \\\"count\\\": 2, \\\"total\\\": 2, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.0139}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T05:00:11.340Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 969788, \"seed\": 67, \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:5\"}, \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"failed\", \"log_path\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"reproduce\": {\"finished_at\": \"2026-05-21T04:59:55.277Z\"}, \"completed_at\": \"2026-05-21T04:59:59.475Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:00:37.585302+00:00\"}]}}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:50:46.149Z\", \"updated_at\": \"2026-05-18T21:55:07.741Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve：perdof ε=0.05 当前 n=2 (seed42=14%, seed44=9%), seed43 在跑。第 4 个 seed 强化低 ε 端 error bars。\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T15:51:08.830Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed45.json\", \"finished_at\": \"2026-05-18T21:53:11.259Z\", \"training_hours\": 6.03}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"598900\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed45.log\", \"submitted_at\": \"2026-05-18T15:51:11.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21723.3, \"gpu_hours\": 6.03}, \"pid\": \"598900\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed45.log\", \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T21:53:14.790Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:53:20.362616+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=124 timeout (wall_clock=6.03h, timeout_hours 过低) | 已知失败模式: LIBERO-Object 全量 eval 需 12-14h，6h timeout 不够 | 建议: 重提交 timeout_hours=16\"}}, \"count\": 2, \"total\": 2, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0139}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "ac93a14a-e518-4d34-849b-6d4f6700ab3a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014vFoXp8pKEU6vnpnwfmF1Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2151,
      "cache_read_input_tokens": 61421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2151
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0137hRtJ8dqsCq4abbmewdP9`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.03_seed67.json /root/logs/eval_object_crm_obs_only_norm0.03_seed67.json /root/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed67.log",
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "13c00f05-91ec-4004-aa20-3f84b1ce7fb4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014vFoXp8pKEU6vnpnwfmF1Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2151,
      "cache_read_input_tokens": 61421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2151
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 23 · 2026-05-21T05:06:35.523Z_

<details><summary>↩ Tool result · `toolu_0137hRtJ8dqsCq4abbmewdP9`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1490 May 21 12:51 /root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\\n\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.03_seed67.json': No such file or directory\\nls: cannot access '/root/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed67.log': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.84}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "7f0a5953-6fac-49f7-bf06-26be2f2c2b22",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 1490 May 21 12:51 /root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\\\\n\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.03_seed67.json': No such file or directory\\\\nls: cannot access '/root/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed67.log': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.84}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1490 May 21 12:51 /root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\\n\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.03_seed67.json': No such file or directory\\nls: cannot access '/root/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed67.log': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.84}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WFGe7Enq43W7x1yXMbaWc3`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/logs/eval_object_crm_obs_only_norm0.03_seed67.json",
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "e752c07c-e7be-485b-a15b-ea4ace2cc8f1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016xar3Kr3wjEi82x1Jw67fE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 63572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 869
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

_source line 25 · 2026-05-21T05:06:38.571Z_

<details><summary>↩ Tool result · `toolu_01WFGe7Enq43W7x1yXMbaWc3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.14,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "824eb08c-184f-473d-a082-a7df10b28681",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"crm_obs_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n      \\\\\\\"successes\\\\\\\": 1,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n      \\\\\\\"successes\\\\\\\": 1,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n      \\\\\\\"successes\\\\\\\": 3,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n      \\\\\\\"successes\\\\\\\": 1,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n      \\\\\\\"successes\\\\\\\": 2,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n      \\\\\\\"successes\\\\\\\": 3,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n      \\\\\\\"successes\\\\\\\": 3,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.14,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "0ae78fd4-6f1e-4c92-b76e-874469cfe338",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018d2TJRdFAk1Gce4S2dpaSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1373,
      "cache_read_input_tokens": 64441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1373
      },
      "output_tokens": 48,
      "service_tier": "standard",
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

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01V6zi2LfhHcWhXaJA6oBixE`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/runs /root/logs ~/runs -name \"*seed67*\" -o -name \"*norm0.03*seed67*\" -o -name \"*norm003*seed67*\" 2>/dev/null",
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "f8698ff8-b777-482f-bb4a-9af0dff7fdd9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018d2TJRdFAk1Gce4S2dpaSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1373,
      "cache_read_input_tokens": 64441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1373
      },
      "output_tokens": 48,
      "service_tier": "standard",
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

_source line 28 · 2026-05-21T05:06:44.022Z_

<details><summary>↩ Tool result · `toolu_01V6zi2LfhHcWhXaJA6oBixE`</summary>

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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "9453956a-be70-40cb-9754-ab9d5de9f103",
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

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MEBQRnnMoogUavgefd5cZb`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/runs -name \"*seed67*\"",
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "2d407374-b016-4143-8424-d1632ac6e183",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01QYAZUdbfHBCdBkiyVjfs4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 65814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
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

_source line 30 · 2026-05-21T05:06:48.352Z_

<details><summary>↩ Tool result · `toolu_01MEBQRnnMoogUavgefd5cZb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "7f41541b-57fe-41eb-bb28-16a2ebd7d8b1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RziVYizXJkHhsunyf4Ve2u`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root -maxdepth 5 -name \"*norm003*seed67*\" -o -name \"*norm0.03*seed67*\"",
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "8e5c1a06-d3c1-4ce7-b266-46eee40d87fa",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01QjHBqvQCu3Hexv3VusFcGJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 66394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 240
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

_source line 32 · 2026-05-21T05:06:51.864Z_

<details><summary>↩ Tool result · `toolu_01RziVYizXJkHhsunyf4Ve2u`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/logs/norm003_seed67.log\\n/root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "1f60fdb8-f11a-437d-9924-e5f3fe219356",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/logs/norm003_seed67.log\\\\n/root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/logs/norm003_seed67.log\\n/root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JRHTHY4q3mVCsGGiEksGCV`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -30 /root/autodl-tmp/logs/norm003_seed67.log",
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
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "f6b4de78-11f7-437e-afc8-d52f6234799e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WNGrimiHwVRH9k8GkS2wGS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 66634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 326
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

_source line 34 · 2026-05-21T05:10:11.508Z_

<details><summary>↩ Tool result · `toolu_01JRHTHY4q3mVCsGGiEksGCV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/10, success so far: 1/10\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 10.0% (1/10)\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/10, success so far: 3/10\\n[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 30.0% (3/10)\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\n[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/10, success so far: 1/10\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 10.0% (1/10)\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/10, success so far: 2/5\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/10, success so far: 2/10\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 20.0% (2/10)\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/10, success so far: 3/10\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 30.0% (3/10)\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/10, success so far: 2/5\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/10, success so far: 3/10\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 30.0% (3/10)\\n\\n============================================================\\nOverall success rate (crm_obs_only): 14.0% (14/100)\\n============================================================\\n[eval] Results saved to logs/eval_object_crm_obs_only_norm0.03_seed67.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "cddbaa96-1e7a-40d8-a8cd-6c1df35a1dbd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/10, success so far: 1/10\\\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 10.0% (1/10)\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/10, success so far: 3/10\\\\n[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 30.0% (3/10)\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\\\n[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/10, success so far: 1/10\\\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 10.0% (1/10)\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/10, success so far: 2/5\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/10, success so far: 2/10\\\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 20.0% (2/10)\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/10, success so far: 3/10\\\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 30.0% (3/10)\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/10, success so far: 2/5\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/10, success so far: 3/10\\\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 30.0% (3/10)\\\\n\\\\n============================================================\\\\nOverall success rate (crm_obs_only): 14.0% (14/100)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_object_crm_obs_only_norm0.03_seed67.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/10, success so far: 1/10\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 10.0% (1/10)\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/10, success so far: 3/10\\n[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 30.0% (3/10)\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\n[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/10, success so far: 1/10\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 10.0% (1/10)\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/10, success so far: 2/5\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/10, success so far: 2/10\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 20.0% (2/10)\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/10, success so far: 3/10\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 30.0% (3/10)\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/10, success so far: 2/5\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/10, success so far: 3/10\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 30.0% (3/10)\\n\\n============================================================\\nOverall success rate (crm_obs_only): 14.0% (14/100)\\n============================================================\\n[eval] Results saved to logs/eval_object_crm_obs_only_norm0.03_seed67.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "45719fdb-19d1-41a5-8e49-f435508a8f01",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HDsHVaDJGa5bszm8ERy8rq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 66960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1464
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

### Assistant

_source line 36_

确认 false positive。日志显示正常完成：`Overall success rate (crm_obs_only): 14.0% (14/100)` + `[eval] Results saved to logs/eval_object_crm_obs_only_norm0.03_seed67.json`。100 rollouts 全跑完，metrics 已经在 registry 里（SR=0.14）。修正 conclusion。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "bf687dfb-0129-4ee0-9441-9c062e5f5fd2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HDsHVaDJGa5bszm8ERy8rq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 66960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1464
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

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01DkFd7d5paD8Tc5YbRXhrDN`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "exp_id": "eval-obs-only-object-norm003-seed67",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "13416b85-9c2e-4c3e-b443-079de8f64e04",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HDsHVaDJGa5bszm8ERy8rq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 66960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1464
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

_source line 38 · 2026-05-21T05:10:32.301Z_

<details><summary>↩ Tool result · `toolu_01DkFd7d5paD8Tc5YbRXhrDN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm003-seed67\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T05:10:29.526Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 969788, \"seed\": 67, \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:5\"}, \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\", \"log_path\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"reproduce\": {\"finished_at\": \"2026-05-21T04:59:55.277Z\"}, \"completed_at\": \"2026-05-21T04:59:59.475Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:00:37.585302+00:00\"}]}}, \"impact_analysis\": {\"change_type\": \"experiment\", \"change_id\": \"eval-obs-only-object-norm003-seed67\", \"affected_decisions\": [], \"cascade_decisions\": [], \"affected_claims\": [], \"affected_figures\": [], \"recommendations\": [\"No downstream impact detected\"]}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.1364}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "6e2a9b9d-64af-4b16-ad80-5a8863372dca",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-obs-only-object-norm003-seed67\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:35:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:10:29.526Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": 969788, \\\"seed\\\": 67, \\\"spec\\\": {\\\"command\\\": \\\"detected on GPU, submitted by prior Worker but not registered\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/acr-vla-conformal-refinement/\\\", \\\"data_count\\\": \\\"100 rollouts\\\", \\\"model_name\\\": \\\"crm_v3_norm/obs_only\\\", \\\"seed\\\": 67, \\\"gpu\\\": \\\"cuda:5\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.14}, \\\"conclusion\\\": \\\"success\\\", \\\"log_path\\\": \\\"/root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T04:59:55.277Z\\\"}, \\\"completed_at\\\": \\\"2026-05-21T04:59:59.475Z\\\", \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T05:00:37.585302+00:00\\\"}]}}, \\\"impact_analysis\\\": {\\\"change_type\\\": \\\"experiment\\\", \\\"change_id\\\": \\\"eval-obs-only-object-norm003-seed67\\\", \\\"affected_decisions\\\": [], \\\"cascade_decisions\\\": [], \\\"affected_claims\\\": [], \\\"affected_figures\\\": [], \\\"recommendations\\\": [\\\"No downstream impact detected\\\"]}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 12.1364}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm003-seed67\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T05:10:29.526Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 969788, \"seed\": 67, \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:5\"}, \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\", \"log_path\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"reproduce\": {\"finished_at\": \"2026-05-21T04:59:55.277Z\"}, \"completed_at\": \"2026-05-21T04:59:59.475Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:00:37.585302+00:00\"}]}}, \"impact_analysis\": {\"change_type\": \"experiment\", \"change_id\": \"eval-obs-only-object-norm003-seed67\", \"affected_decisions\": [], \"cascade_decisions\": [], \"affected_claims\": [], \"affected_figures\": [], \"recommendations\": [\"No downstream impact detected\"]}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.1364}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 39_

## 总结

**是否 false positive**: 是。Cron 误判（项目脚本不写 sentinel/W&B 的已知问题）。

**证据**：
- Log `/root/autodl-tmp/logs/norm003_seed67.log` 末尾显示：
  - `Overall success rate (crm_obs_only): 14.0% (14/100)`
  - `[eval] Results saved to logs/eval_object_crm_obs_only_norm0.03_seed67.json`
- Output JSON 完整：10 task × 10 rollouts = 100 全跑完

**SR 值**: overall_success_rate = **0.14** (14/100)

**Registry 修正**: ✅ conclusion: failed → success（metrics 已存在，无需补录）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "uuid": "b820bac4-a949-4bb0-afb7-5f6d4de3f032",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TWiUi8W3gBDXj4Z2wuedWP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1365,
      "cache_read_input_tokens": 68424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1365
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

_source line 40_

## 总结

**是否 false positive**: 是。Cron 误判（项目脚本不写 sentinel/W&B 的已知问题）。

**证据**：
- Log `/root/autodl-tmp/logs/norm003_seed67.log` 末尾显示：
  - `Overall success rate (crm_obs_only): 14.0% (14/100)`
  - `[eval] Results saved to logs/eval_object_crm_obs_only_norm0.03_seed67.json`
- Output JSON 完整：10 task × 10 rollouts = 100 全跑完

**SR 值**: overall_success_rate = **0.14** (14/100)

**Registry 修正**: ✅ conclusion: failed → success（metrics 已存在，无需补录）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 297930,
  "duration_api_ms": 269217,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "76ee10a5-de55-4637-81fb-92e47739b714",
  "total_cost_usd": 0.89094025,
  "usage": {
    "input_tokens": 25,
    "cache_creation_input_tokens": 68159,
    "cache_read_input_tokens": 751309,
    "output_tokens": 3509,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 68159,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 258,
        "cache_read_input_tokens": 68424,
        "cache_creation_input_tokens": 1365,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1365
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1312,
      "outputTokens": 26,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001442,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 25,
      "outputTokens": 3509,
      "cacheReadInputTokens": 751309,
      "cacheCreationInputTokens": 68159,
      "webSearchRequests": 0,
      "costUSD": 0.88949825,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "50872b45-b0ca-4679-af8f-868c0b00ef79"
}
```

</details>

---
