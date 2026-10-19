# investigate pi05 object s43 conflict 20260524T192714 retry1 — Part 1 of 2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[Transcript overview](../investigate-pi05-object-s43-conflict-20260524t192714-retry1.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/3f/3f8f8b09be4c2cdccc27.json)

## Before a recorded user message

## Before a recorded user message

130 recorded events


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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
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
  "uuid": "4b2b612b-f9a5-4f57-adbb-7bee64b36974",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779664200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4c54797f-96dd-40d6-a920-5bc5567128c5",
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d"
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "ef803a98-a961-4833-b680-9a9fc7b35493",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01P3DwfFZ9TLHoYs3kCCj9rn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15519,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15519
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VVsQtsS7GCmf6PSYFn8iaW`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__save_project_file",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "5535f04a-8137-4152-b600-ef2828ca6051",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01P3DwfFZ9TLHoYs3kCCj9rn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15519,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15519
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

_source line 6 · 2026-05-24T19:27:35.374Z_

<details><summary>↩ Tool result · `toolu_01VVsQtsS7GCmf6PSYFn8iaW`</summary>

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
  "tool_name": "mcp__agent-ml-research__register_artifact"
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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "fc953ce2-6e5e-4cff-99bb-087ddc0f0e0c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 29
  }
}
```

</details>

---


### Assistant

_source line 7_

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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "7248f159-6698-4d3b-9930-4994de809dc2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016BTbbpD9VebXLbKYPfQ4GC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 19040,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19040
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29180
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_016G7DNog5fR1rd6ZmPmt7q6`</summary>

```json
{
  "filters": {
    "exp_id": "eval-pi05-vla-only-object-seed43-r4"
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "2de25ab7-7ed5-48f2-bf08-4d62b7c0a2bc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016BTbbpD9VebXLbKYPfQ4GC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 19040,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19040
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29180
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01WWZBu6PXa978XCawSXRWpe`</summary>

```json
{
  "filters": {
    "exp_id": "eval-pi05-vla-only-object-seed43-r3"
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "8091c69d-a6f0-4216-99b0-d772bdb08141",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016BTbbpD9VebXLbKYPfQ4GC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 19040,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19040
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29180
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 10 · 2026-05-24T19:27:43.689Z_

<details><summary>↩ Tool result · `toolu_016G7DNog5fR1rd6ZmPmt7q6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4276}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "14717e72-4812-46ce-a94d-af9ac5ed9912",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4276}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4276}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-24T19:27:44.071Z_

<details><summary>↩ Tool result · `toolu_01WWZBu6PXa978XCawSXRWpe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.365}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "6eb8c8a8-0736-4445-a4ca-3d8603304095",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.365}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.365}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01E4zXSLS12vkh6rHo37g8Sw`</summary>

```json
{
  "filters": {
    "project": "acr-vla-conformal-refinement"
  },
  "fields": [
    "exp_id",
    "status",
    "metrics",
    "server"
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "2fdcbc5d-dcc7-4f26-9261-ca02769633c6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DEFtgoasVJYRo7qmrzeNfr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 35374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
      },
      "output_tokens": 56,
      "service_tier": "standard",
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

_source line 13 · 2026-05-24T19:27:47.443Z_

<details><summary>↩ Tool result · `toolu_01E4zXSLS12vkh6rHo37g8Sw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2286}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "f020b1a4-a78b-41c1-af8d-5ca0dd5b8ff6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2286}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2286}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_014Q6TAoMZpCW7FNmxhWxF8J`</summary>

```json
{
  "filters": {},
  "fields": [
    "exp_id"
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "262248cc-23c9-47ac-8dd6-350dbf4aa0c0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01D3y77XuiPwqKnBNQPQ3fLd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 260,
      "cache_read_input_tokens": 36110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 260
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 15 · 2026-05-24T19:27:50.819Z_

<details><summary>↩ Tool result · `toolu_014Q6TAoMZpCW7FNmxhWxF8J`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-adapt-tau025-s47-r2\": {}, \"eval-supp-long-k2mean-s47-r2\": {}, \"eval-supp-spatial-vla-only-s47\": {}, \"eval-supp-spatial-adapt-tau025-s47\": {}, \"eval-supp-adapt-tau025-spatial-s47\": {}, \"eval-a1-baseline-object-s42\": {}, \"eval-supp-spatial-k2mean-s47\": {}, \"eval-supp-obj-reconvla-s47\": {}, \"eval-supp-goal-reconvla-s47\": {}, \"eval-supp-goal-k2mean-s47\": {}, \"eval-supp-goal-crm-norm005-s47\": {}, \"eval-supp-goal-adapt-tau025-s47\": {}, \"eval-supp-adapt-tau025-spatial-s46\": {}, \"eval-supp-long-k2mean-s46\": {}, \"eval-supp-long-reconvla-s46\": {}, \"precompute-pi05-goal-2048-r2\": {}, \"precompute-pi05-spatial-2048-r2\": {}, \"eval-supp-spatial-reconvla-s46\": {}, \"eval-supp-spatial-reconvla-s45\": {}, \"eval-supp-spatial-k2mean-s46\": {}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {}, \"eval-supp-reconvla-obj-s45\": {}, \"eval-supp-long-vla-only-s43\": {}, \"eval-supp-long-k2mean-s42\": {}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {}, \"eval-supp-crm-norm02-spatial-s42-r2\": {}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {}, \"precompute-pi05-long-2048-r2\": {}, \"precompute-pi05-object-2048-r2\": {}, \"eval-smolvla-lerobot-goal-seed43-v3\": {}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {}, \"eval-smolvla-lerobot-object-seed44-v2\": {}, \"eval-smolvla-lerobot-object-seed43-v2\": {}, \"eval-pi05-vla-only-long-seed42-r4-std\": {}, \"eval-pi05-vla-only-spatial-seed44-r4\": {}, \"eval-pi05-vla-only-spatial-seed43-r4\": {}, \"eval-pi05-vla-only-spatial-seed42-r4\": {}, \"eval-pi05-crm-spatial-seed44\": {}, \"eval-pi05-crm-spatial-seed43\": {}, \"eval-pi05-crm-spatial-seed42\": {}, \"eval-openvla-oft-official-object\": {}, \"eval-perdof-object-norm02-seed45-r3\": {}, \"eval-obs-only-object-norm005-seed43\": {}, \"eval-perdof-object-norm02-seed48\": {}, \"eval-openvla-object-baseline-seed42\": {}, \"eval-argmin-object-k5-seed44-r2\": {}, \"eval-vla-only-goal-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-seed46-r2\": {}, \"eval-adaptive-k-spatial-p75-seed44\": {}, \"eval-adaptive-k-spatial-p25-seed44\": {}, \"eval-adaptive-k-spatial-p90-seed42\": {}, \"eval-random-selection-spatial-seed42\": {}, \"eval-random-selection-spatial-seed44\": {}, \"eval-obs-only-object-norm02-seed49\": {}, \"eval-argmin-object-seed48\": {}, \"eval-pi05-vla-only-object-seed44-r3\": {}, \"eval-pi05-vla-only-object-seed43-r3\": {}, \"eval-pi05-vla-only-object-seed42-r3\": {}, \"eval-pi05-vla-only-object-seed44\": {}, \"eval-pi05-vla-only-object-seed43\": {}, \"eval-pi05-vla-only-object-seed42\": {}, \"eval-vla-only-long-seed49\": {}, \"eval-crm-long-seed52\": {}, \"eval-crm-goal-seed49\": {}, \"eval-crm-goal-seed50\": {}, \"eval-crm-goal-seed47\": {}, \"eval-crm-goal-seed48\": {}, \"eval-crm-spatial-k10-seed49\": {}, \"eval-vla-only-object-seed49-r2\": {}, \"eval-crm-spatial-seed47\": {}, \"eval-vla-only-spatial-seed50\": {}, \"eval-vla-only-spatial-seed52\": {}, \"eval-vla-only-spatial-seed53\": {}, \"eval-crm-long-seed53\": {}, \"eval-vla-only-long-seed54\": {}, \"eval-obs-only-goal-norm02-seed53\": {}, \"eval-crm-spatial-seed48\": {}, \"eval-vla-only-object-seed51\": {}, \"eval-vla-only-spatial-seed51\": {}, \"eval-crm-long-seed51\": {}, \"eval-vla-only-goal-seed52\": {}, \"eval-vla-only-long-seed53\": {}, \"eval-crm-spatial-k10-seed50\": {}, \"eval-crm-long-seed48\": {}, \"eval-crm-long-seed49\": {}, \"eval-crm-long-seed54\": {}, \"eval-vla-only-spatial-seed54\": {}, \"eval-obs-only-object-norm005-seed75\": {}, \"eval-obs-only-object-norm01-seed74\": {}, \"eval-obs-only-object-norm01-seed64\": {}, \"eval-obs-only-object-norm003-seed73\": {}, \"eval-obs-only-object-norm005-seed64\": {}, \"eval-obs-only-object-norm003-seed65\": {}, \"eval-obs-only-object-norm003-seed64\": {}, \"eval-obs-only-object-norm003-seed63-r2\": {}, \"eval-obs-only-object-norm003-seed62-r2\": {}, \"eval-obs-only-object-norm005-seed65\": {}, \"eval-obs-only-object-norm005-seed61\": {}, \"eval-obs-only-object-norm01-seed60\": {}, \"eval-obs-only-object-norm003-seed56\": {}, \"eval-obs-only-object-norm01-seed66\": {}, \"eval-obs-only-object-norm005-seed66\": {}, \"eval-obs-only-object-norm003-seed66\": {}, \"eval-obs-only-object-norm003-seed59\": {}, \"eval-obs-only-object-norm005-seed58\": {}, \"eval-obs-only-object-norm01-seed57\": {}, \"eval-obs-only-object-norm005-seed63\": {}, \"eval-obs-only-object-norm005-seed62\": {}, \"eval-perdof-object-norm02-seed49\": {}, \"eval-obs-only-object-norm02-seed43-r3\": {}, \"openvla-precompute-k1\": {}, \"eval-obs-only-goal-norm02-seed52\": {}, \"eval-argmin-object-seed49\": {}, \"eval-random-selection-spatial-seed43\": {}, \"eval-adaptive-k-spatial-p90-seed43\": {}, \"eval-adaptive-k-object-p90-seed44\": {}, \"eval-adaptive-k-object-p90-seed43\": {}, \"eval-adaptive-k-spatial-p50-seed42\": {}, \"eval-obs-only-object-norm003-seed44\": {}, \"eval-random-selection-object-seed46-r2\": {}, \"eval-obs-only-spatial-norm02-seed47\": {}, \"eval-vla-only-spatial-seed45\": {}, \"eval-obs-only-spatial-norm02-seed44\": {}, \"eval-obs-only-object-norm003-seed43-r2\": {}, \"eval-obs-only-object-norm03-seed48\": {}, \"eval-obs-only-object-norm01-seed48\": {}, \"eval-obs-only-object-norm02-k5-seed42\": {}, \"eval-perdof-object-norm01-seed46\": {}, \"eval-perdof-object-default-seed46\": {}, \"eval-obs-only-object-default-seed46\": {}, \"eval-obs-only-object-norm01-seed46\": {}, \"eval-k1-crm-multiscale-object-seed43\": {}, \"eval-k1-crm-multiscale-object-seed42\": {}, \"eval-k1-crm-multiscale-object-seed44-r2\": {}, \"eval-mag-perdof-norm03-object-r3\": {}, \"eval-mag-perdof-norm005-object\": {}, \"eval-mag-obsonly-norm03-object\": {}}, \"count\": 138, \"total\": 138, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2893}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "12e2c0a9-0419-43b8-a0f5-37f448aede69",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-long-adapt-tau025-s47-r2\\\": {}, \\\"eval-supp-long-k2mean-s47-r2\\\": {}, \\\"eval-supp-spatial-vla-only-s47\\\": {}, \\\"eval-supp-spatial-adapt-tau025-s47\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s47\\\": {}, \\\"eval-a1-baseline-object-s42\\\": {}, \\\"eval-supp-spatial-k2mean-s47\\\": {}, \\\"eval-supp-obj-reconvla-s47\\\": {}, \\\"eval-supp-goal-reconvla-s47\\\": {}, \\\"eval-supp-goal-k2mean-s47\\\": {}, \\\"eval-supp-goal-crm-norm005-s47\\\": {}, \\\"eval-supp-goal-adapt-tau025-s47\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s46\\\": {}, \\\"eval-supp-long-k2mean-s46\\\": {}, \\\"eval-supp-long-reconvla-s46\\\": {}, \\\"precompute-pi05-goal-2048-r2\\\": {}, \\\"precompute-pi05-spatial-2048-r2\\\": {}, \\\"eval-supp-spatial-reconvla-s46\\\": {}, \\\"eval-supp-spatial-reconvla-s45\\\": {}, \\\"eval-supp-spatial-k2mean-s46\\\": {}, \\\"eval-supp-spatial-adapt-tau025-s45-r3\\\": {}, \\\"eval-supp-reconvla-obj-s45\\\": {}, \\\"eval-supp-long-vla-only-s43\\\": {}, \\\"eval-supp-long-k2mean-s42\\\": {}, \\\"eval-supp-adapt-tau035-spatial-s42-r2\\\": {}, \\\"eval-supp-adapt-tau015-spatial-s42-r2\\\": {}, \\\"eval-supp-crm-norm02-spatial-s42-r2\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s42-r2\\\": {}, \\\"precompute-pi05-long-2048-r2\\\": {}, \\\"precompute-pi05-object-2048-r2\\\": {}, \\\"eval-smolvla-lerobot-goal-seed43-v3\\\": {}, \\\"eval-smolvla-lerobot-spatial-seed43-v3\\\": {}, \\\"eval-smolvla-lerobot-object-seed44-v2\\\": {}, \\\"eval-smolvla-lerobot-object-seed43-v2\\\": {}, \\\"eval-pi05-vla-only-long-seed42-r4-std\\\": {}, \\\"eval-pi05-vla-only-spatial-seed44-r4\\\": {}, \\\"eval-pi05-vla-only-spatial-seed43-r4\\\": {}, \\\"eval-pi05-vla-only-spatial-seed42-r4\\\": {}, \\\"eval-pi05-crm-spatial-seed44\\\": {}, \\\"eval-pi05-crm-spatial-seed43\\\": {}, \\\"eval-pi05-crm-spatial-seed42\\\": {}, \\\"eval-openvla-oft-official-object\\\": {}, \\\"eval-perdof-object-norm02-seed45-r3\\\": {}, \\\"eval-obs-only-object-norm005-seed43\\\": {}, \\\"eval-perdof-object-norm02-seed48\\\": {}, \\\"eval-openvla-object-baseline-seed42\\\": {}, \\\"eval-argmin-object-k5-seed44-r2\\\": {}, \\\"eval-vla-only-goal-seed44-r2\\\": {}, \\\"eval-obs-only-spatial-norm02-seed46-r2\\\": {}, \\\"eval-adaptive-k-spatial-p75-seed44\\\": {}, \\\"eval-adaptive-k-spatial-p25-seed44\\\": {}, \\\"eval-adaptive-k-spatial-p90-seed42\\\": {}, \\\"eval-random-selection-spatial-seed42\\\": {}, \\\"eval-random-selection-spatial-seed44\\\": {}, \\\"eval-obs-only-object-norm02-seed49\\\": {}, \\\"eval-argmin-object-seed48\\\": {}, \\\"eval-pi05-vla-only-object-seed44-r3\\\": {}, \\\"eval-pi05-vla-only-object-seed43-r3\\\": {}, \\\"eval-pi05-vla-only-object-seed42-r3\\\": {}, \\\"eval-pi05-vla-only-object-seed44\\\": {}, \\\"eval-pi05-vla-only-object-seed43\\\": {}, \\\"eval-pi05-vla-only-object-seed42\\\": {}, \\\"eval-vla-only-long-seed49\\\": {}, \\\"eval-crm-long-seed52\\\": {}, \\\"eval-crm-goal-seed49\\\": {}, \\\"eval-crm-goal-seed50\\\": {}, \\\"eval-crm-goal-seed47\\\": {}, \\\"eval-crm-goal-seed48\\\": {}, \\\"eval-crm-spatial-k10-seed49\\\": {}, \\\"eval-vla-only-object-seed49-r2\\\": {}, \\\"eval-crm-spatial-seed47\\\": {}, \\\"eval-vla-only-spatial-seed50\\\": {}, \\\"eval-vla-only-spatial-seed52\\\": {}, \\\"eval-vla-only-spatial-seed53\\\": {}, \\\"eval-crm-long-seed53\\\": {}, \\\"eval-vla-only-long-seed54\\\": {}, \\\"eval-obs-only-goal-norm02-seed53\\\": {}, \\\"eval-crm-spatial-seed48\\\": {}, \\\"eval-vla-only-object-seed51\\\": {}, \\\"eval-vla-only-spatial-seed51\\\": {}, \\\"eval-crm-long-seed51\\\": {}, \\\"eval-vla-only-goal-seed52\\\": {}, \\\"eval-vla-only-long-seed53\\\": {}, \\\"eval-crm-spatial-k10-seed50\\\": {}, \\\"eval-crm-long-seed48\\\": {}, \\\"eval-crm-long-seed49\\\": {}, \\\"eval-crm-long-seed54\\\": {}, \\\"eval-vla-only-spatial-seed54\\\": {}, \\\"eval-obs-only-object-norm005-seed75\\\": {}, \\\"eval-obs-only-object-norm01-seed74\\\": {}, \\\"eval-obs-only-object-norm01-seed64\\\": {}, \\\"eval-obs-only-object-norm003-seed73\\\": {}, \\\"eval-obs-only-object-norm005-seed64\\\": {}, \\\"eval-obs-only-object-norm003-seed65\\\": {}, \\\"eval-obs-only-object-norm003-seed64\\\": {}, \\\"eval-obs-only-object-norm003-seed63-r2\\\": {}, \\\"eval-obs-only-object-norm003-seed62-r2\\\": {}, \\\"eval-obs-only-object-norm005-seed65\\\": {}, \\\"eval-obs-only-object-norm005-seed61\\\": {}, \\\"eval-obs-only-object-norm01-seed60\\\": {}, \\\"eval-obs-only-object-norm003-seed56\\\": {}, \\\"eval-obs-only-object-norm01-seed66\\\": {}, \\\"eval-obs-only-object-norm005-seed66\\\": {}, \\\"eval-obs-only-object-norm003-seed66\\\": {}, \\\"eval-obs-only-object-norm003-seed59\\\": {}, \\\"eval-obs-only-object-norm005-seed58\\\": {}, \\\"eval-obs-only-object-norm01-seed57\\\": {}, \\\"eval-obs-only-object-norm005-seed63\\\": {}, \\\"eval-obs-only-object-norm005-seed62\\\": {}, \\\"eval-perdof-object-norm02-seed49\\\": {}, \\\"eval-obs-only-object-norm02-seed43-r3\\\": {}, \\\"openvla-precompute-k1\\\": {}, \\\"eval-obs-only-goal-norm02-seed52\\\": {}, \\\"eval-argmin-object-seed49\\\": {}, \\\"eval-random-selection-spatial-seed43\\\": {}, \\\"eval-adaptive-k-spatial-p90-seed43\\\": {}, \\\"eval-adaptive-k-object-p90-seed44\\\": {}, \\\"eval-adaptive-k-object-p90-seed43\\\": {}, \\\"eval-adaptive-k-spatial-p50-seed42\\\": {}, \\\"eval-obs-only-object-norm003-seed44\\\": {}, \\\"eval-random-selection-object-seed46-r2\\\": {}, \\\"eval-obs-only-spatial-norm02-seed47\\\": {}, \\\"eval-vla-only-spatial-seed45\\\": {}, \\\"eval-obs-only-spatial-norm02-seed44\\\": {}, \\\"eval-obs-only-object-norm003-seed43-r2\\\": {}, \\\"eval-obs-only-object-norm03-seed48\\\": {}, \\\"eval-obs-only-object-norm01-seed48\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed42\\\": {}, \\\"eval-perdof-object-norm01-seed46\\\": {}, \\\"eval-perdof-object-default-seed46\\\": {}, \\\"eval-obs-only-object-default-seed46\\\": {}, \\\"eval-obs-only-object-norm01-seed46\\\": {}, \\\"eval-k1-crm-multiscale-object-seed43\\\": {}, \\\"eval-k1-crm-multiscale-object-seed42\\\": {}, \\\"eval-k1-crm-multiscale-object-seed44-r2\\\": {}, \\\"eval-mag-perdof-norm03-object-r3\\\": {}, \\\"eval-mag-perdof-norm005-object\\\": {}, \\\"eval-mag-obsonly-norm03-object\\\": {}}, \\\"count\\\": 138, \\\"total\\\": 138, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2893}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-adapt-tau025-s47-r2\": {}, \"eval-supp-long-k2mean-s47-r2\": {}, \"eval-supp-spatial-vla-only-s47\": {}, \"eval-supp-spatial-adapt-tau025-s47\": {}, \"eval-supp-adapt-tau025-spatial-s47\": {}, \"eval-a1-baseline-object-s42\": {}, \"eval-supp-spatial-k2mean-s47\": {}, \"eval-supp-obj-reconvla-s47\": {}, \"eval-supp-goal-reconvla-s47\": {}, \"eval-supp-goal-k2mean-s47\": {}, \"eval-supp-goal-crm-norm005-s47\": {}, \"eval-supp-goal-adapt-tau025-s47\": {}, \"eval-supp-adapt-tau025-spatial-s46\": {}, \"eval-supp-long-k2mean-s46\": {}, \"eval-supp-long-reconvla-s46\": {}, \"precompute-pi05-goal-2048-r2\": {}, \"precompute-pi05-spatial-2048-r2\": {}, \"eval-supp-spatial-reconvla-s46\": {}, \"eval-supp-spatial-reconvla-s45\": {}, \"eval-supp-spatial-k2mean-s46\": {}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {}, \"eval-supp-reconvla-obj-s45\": {}, \"eval-supp-long-vla-only-s43\": {}, \"eval-supp-long-k2mean-s42\": {}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {}, \"eval-supp-crm-norm02-spatial-s42-r2\": {}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {}, \"precompute-pi05-long-2048-r2\": {}, \"precompute-pi05-object-2048-r2\": {}, \"eval-smolvla-lerobot-goal-seed43-v3\": {}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {}, \"eval-smolvla-lerobot-object-seed44-v2\": {}, \"eval-smolvla-lerobot-object-seed43-v2\": {}, \"eval-pi05-vla-only-long-seed42-r4-std\": {}, \"eval-pi05-vla-only-spatial-seed44-r4\": {}, \"eval-pi05-vla-only-spatial-seed43-r4\": {}, \"eval-pi05-vla-only-spatial-seed42-r4\": {}, \"eval-pi05-crm-spatial-seed44\": {}, \"eval-pi05-crm-spatial-seed43\": {}, \"eval-pi05-crm-spatial-seed42\": {}, \"eval-openvla-oft-official-object\": {}, \"eval-perdof-object-norm02-seed45-r3\": {}, \"eval-obs-only-object-norm005-seed43\": {}, \"eval-perdof-object-norm02-seed48\": {}, \"eval-openvla-object-baseline-seed42\": {}, \"eval-argmin-object-k5-seed44-r2\": {}, \"eval-vla-only-goal-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-seed46-r2\": {}, \"eval-adaptive-k-spatial-p75-seed44\": {}, \"eval-adaptive-k-spatial-p25-seed44\": {}, \"eval-adaptive-k-spatial-p90-seed42\": {}, \"eval-random-selection-spatial-seed42\": {}, \"eval-random-selection-spatial-seed44\": {}, \"eval-obs-only-object-norm02-seed49\": {}, \"eval-argmin-object-seed48\": {}, \"eval-pi05-vla-only-object-seed44-r3\": {}, \"eval-pi05-vla-only-object-seed43-r3\": {}, \"eval-pi05-vla-only-object-seed42-r3\": {}, \"eval-pi05-vla-only-object-seed44\": {}, \"eval-pi05-vla-only-object-seed43\": {}, \"eval-pi05-vla-only-object-seed42\": {}, \"eval-vla-only-long-seed49\": {}, \"eval-crm-long-seed52\": {}, \"eval-crm-goal-seed49\": {}, \"eval-crm-goal-seed50\": {}, \"eval-crm-goal-seed47\": {}, \"eval-crm-goal-seed48\": {}, \"eval-crm-spatial-k10-seed49\": {}, \"eval-vla-only-object-seed49-r2\": {}, \"eval-crm-spatial-seed47\": {}, \"eval-vla-only-spatial-seed50\": {}, \"eval-vla-only-spatial-seed52\": {}, \"eval-vla-only-spatial-seed53\": {}, \"eval-crm-long-seed53\": {}, \"eval-vla-only-long-seed54\": {}, \"eval-obs-only-goal-norm02-seed53\": {}, \"eval-crm-spatial-seed48\": {}, \"eval-vla-only-object-seed51\": {}, \"eval-vla-only-spatial-seed51\": {}, \"eval-crm-long-seed51\": {}, \"eval-vla-only-goal-seed52\": {}, \"eval-vla-only-long-seed53\": {}, \"eval-crm-spatial-k10-seed50\": {}, \"eval-crm-long-seed48\": {}, \"eval-crm-long-seed49\": {}, \"eval-crm-long-seed54\": {}, \"eval-vla-only-spatial-seed54\": {}, \"eval-obs-only-object-norm005-seed75\": {}, \"eval-obs-only-object-norm01-seed74\": {}, \"eval-obs-only-object-norm01-seed64\": {}, \"eval-obs-only-object-norm003-seed73\": {}, \"eval-obs-only-object-norm005-seed64\": {}, \"eval-obs-only-object-norm003-seed65\": {}, \"eval-obs-only-object-norm003-seed64\": {}, \"eval-obs-only-object-norm003-seed63-r2\": {}, \"eval-obs-only-object-norm003-seed62-r2\": {}, \"eval-obs-only-object-norm005-seed65\": {}, \"eval-obs-only-object-norm005-seed61\": {}, \"eval-obs-only-object-norm01-seed60\": {}, \"eval-obs-only-object-norm003-seed56\": {}, \"eval-obs-only-object-norm01-seed66\": {}, \"eval-obs-only-object-norm005-seed66\": {}, \"eval-obs-only-object-norm003-seed66\": {}, \"eval-obs-only-object-norm003-seed59\": {}, \"eval-obs-only-object-norm005-seed58\": {}, \"eval-obs-only-object-norm01-seed57\": {}, \"eval-obs-only-object-norm005-seed63\": {}, \"eval-obs-only-object-norm005-seed62\": {}, \"eval-perdof-object-norm02-seed49\": {}, \"eval-obs-only-object-norm02-seed43-r3\": {}, \"openvla-precompute-k1\": {}, \"eval-obs-only-goal-norm02-seed52\": {}, \"eval-argmin-object-seed49\": {}, \"eval-random-selection-spatial-seed43\": {}, \"eval-adaptive-k-spatial-p90-seed43\": {}, \"eval-adaptive-k-object-p90-seed44\": {}, \"eval-adaptive-k-object-p90-seed43\": {}, \"eval-adaptive-k-spatial-p50-seed42\": {}, \"eval-obs-only-object-norm003-seed44\": {}, \"eval-random-selection-object-seed46-r2\": {}, \"eval-obs-only-spatial-norm02-seed47\": {}, \"eval-vla-only-spatial-seed45\": {}, \"eval-obs-only-spatial-norm02-seed44\": {}, \"eval-obs-only-object-norm003-seed43-r2\": {}, \"eval-obs-only-object-norm03-seed48\": {}, \"eval-obs-only-object-norm01-seed48\": {}, \"eval-obs-only-object-norm02-k5-seed42\": {}, \"eval-perdof-object-norm01-seed46\": {}, \"eval-perdof-object-default-seed46\": {}, \"eval-obs-only-object-default-seed46\": {}, \"eval-obs-only-object-norm01-seed46\": {}, \"eval-k1-crm-multiscale-object-seed43\": {}, \"eval-k1-crm-multiscale-object-seed42\": {}, \"eval-k1-crm-multiscale-object-seed44-r2\": {}, \"eval-mag-perdof-norm03-object-r3\": {}, \"eval-mag-perdof-norm005-object\": {}, \"eval-mag-obsonly-norm03-object\": {}}, \"count\": 138, \"total\": 138, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2893}}"
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "8c3a12cf-6a7d-4667-a526-c90c38aadbe7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EdonAfLNrMWCZkyoeA1Hgk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3534,
      "cache_read_input_tokens": 36370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3534
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Jq5oKHAWEJXQW8oVR5uXEi`</summary>

```json
{
  "filters": {
    "exp_id": "eval-pi05-vla-only-object-seed43-r4"
  },
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "27b6c1be-6f0e-42a2-a66a-48b5bc101687",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EdonAfLNrMWCZkyoeA1Hgk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3534,
      "cache_read_input_tokens": 36370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3534
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01DFs3ZTbVRREEAdKDWP3bzy`</summary>

```json
{
  "filters": {
    "exp_id": "eval-pi05-vla-only-object-seed43-r3"
  },
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "6578de6b-9be9-492c-83e7-657d1df518be",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EdonAfLNrMWCZkyoeA1Hgk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3534,
      "cache_read_input_tokens": 36370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3534
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Q9CTgj2fY67529dshj4XJv`</summary>

```json
{
  "filters": {
    "exp_id": "eval-pi05-vla-only-object-seed43"
  },
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "0056738f-5d7c-4149-b1e7-9ed1a88f694a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EdonAfLNrMWCZkyoeA1Hgk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3534,
      "cache_read_input_tokens": 36370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3534
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

_source line 20 · 2026-05-24T19:27:58.726Z_

<details><summary>↩ Tool result · `toolu_01Jq5oKHAWEJXQW8oVR5uXEi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8799}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "69932106-c4f6-44a2-ba7a-53811931a284",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.8799}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8799}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-24T19:28:00.963Z_

<details><summary>↩ Tool result · `toolu_01DFs3ZTbVRREEAdKDWP3bzy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2199}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "76a683bc-1461-49bc-b2b1-3fae006ec5ed",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.2199}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2199}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-24T19:28:03.129Z_

<details><summary>↩ Tool result · `toolu_01Q9CTgj2fY67529dshj4XJv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1486}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "94260a01-8aaa-402e-a035-3b145f73d9e9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.1486}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1486}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 23_

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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "4ce11ef6-5f51-4383-9f6e-e432910d3158",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WtFD3uBDjF8uTzYehG4Kzd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 39904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
      },
      "output_tokens": 53,
      "service_tier": "standard",
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

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01QGEeSD4HWA3VTZ36Tjthrf`</summary>

```json
{
  "filters": {
    "id": "eval-pi05-vla-only-object-seed43-r4"
  },
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "893034df-6cb7-4e07-83e9-853235e9b5ea",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WtFD3uBDjF8uTzYehG4Kzd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 39904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
      },
      "output_tokens": 53,
      "service_tier": "standard",
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

_source line 25 · 2026-05-24T19:28:09.179Z_

<details><summary>↩ Tool result · `toolu_01QGEeSD4HWA3VTZ36Tjthrf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2476}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "1a58f1f0-a3b9-48b4-8a7d-406dbcd4d1de",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.2476}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2476}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01S7Qt7eVwPSjjAKqHU3sbeq`</summary>

```json
{
  "filters": {},
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "exp_id",
    "status",
    "metrics",
    "server",
    "log_path"
  ],
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "fbc1fc01-3142-496c-9724-39ae8826488e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AhFFLn3FxxmQh39FVo5HFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 327,
      "cache_read_input_tokens": 40809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 327
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

_source line 27 · 2026-05-24T19:28:14.799Z_

<details><summary>↩ Tool result · `toolu_01S7Qt7eVwPSjjAKqHU3sbeq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-obj-vla-only-s50\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.74, \"successes\": 148, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"object\", \"seed\": 50, \"mode\": \"vla_only\", \"model\": \"pi05\"}}, \"eval-supp-spatial-vla-only-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"spatial\", \"seed\": 42, \"mode\": \"vla_only\", \"model\": \"pi05\"}}, \"eval-supp-adapt-tau025-obj-s49\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.74, \"trigger_rate\": 0.0417, \"mean_uncertainty\": 0.1131, \"per_task_sr\": {\"soup\": 0.7, \"cream_cheese\": 0.65, \"salad\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.75, \"tomato\": 0.75, \"butter\": 0.6, \"milk\": 0.6, \"pudding\": 0.8, \"oj\": 0.95}}}, \"eval-supp-adapt-tau025-obj-s48\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.76, \"trigger_rate\": 0.0389, \"mean_uncertainty\": 0.1117, \"per_task_sr\": {\"soup\": 0.75, \"cream_cheese\": 0.75, \"salad\": 0.7, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.6, \"milk\": 0.8, \"pudding\": 0.7, \"oj\": 0.95}}}, \"eval-supp-vla-only-obj-s49\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.755, \"per_task_sr\": {\"soup\": 0.55, \"cream_cheese\": 0.7, \"salad\": 0.8, \"bbq\": 0.95, \"ketchup\": 0.8, \"tomato\": 0.8, \"butter\": 0.6, \"milk\": 0.65, \"pudding\": 0.8, \"oj\": 0.9}}}, \"eval-supp-vla-only-obj-s48\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.79, \"per_task_sr\": {\"soup\": 0.65, \"cream_cheese\": 0.8, \"salad\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.85, \"tomato\": 0.8, \"butter\": 0.65, \"milk\": 0.8, \"pudding\": 0.75, \"oj\": 0.95}}}, \"eval-supp-vla-only-goal-s49\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.82, \"per_task_sr\": {\"middle_drawer\": 0.75, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.65, \"bowl_cabinet\": 0.95, \"push_plate\": 0.85, \"cream_cheese\": 0.55, \"stove_on\": 1, \"bowl_plate\": 0.85, \"wine_rack\": 0.8}}}, \"eval-supp-vla-only-goal-s48\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.85, \"per_task_sr\": {\"middle_drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.9, \"drawer_bowl\": 0.55, \"bowl_cabinet\": 1, \"push_plate\": 0.9, \"cream_cheese\": 0.6, \"stove_on\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}}, \"eval-supp-vla-only-spatial-s49\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.785, \"per_task_sr\": {\"between\": 0.9, \"next_ramekin\": 0.95, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.7, \"on_ramekin\": 0, \"next_cookie\": 0.9, \"stove\": 0.8, \"next_plate\": 0.75, \"cabinet\": 0.95}}}, \"eval-supp-vla-only-spatial-s48\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.795, \"per_task_sr\": {\"between\": 1, \"next_ramekin\": 0.9, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.8, \"on_ramekin\": 0, \"next_cookie\": 0.95, \"stove\": 0.75, \"next_plate\": 0.85, \"cabinet\": 0.8}}}}, \"count\": 10, \"total\": 953, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.313}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "f187d337-4636-4983-bc03-79c8fad8cb56",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-obj-vla-only-s50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.74, \\\"successes\\\": 148, \\\"total\\\": 200, \\\"n_rollouts\\\": 20, \\\"benchmark\\\": \\\"object\\\", \\\"seed\\\": 50, \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi05\\\"}}, \\\"eval-supp-spatial-vla-only-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.8, \\\"successes\\\": 160, \\\"total\\\": 200, \\\"n_rollouts\\\": 20, \\\"benchmark\\\": \\\"spatial\\\", \\\"seed\\\": 42, \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi05\\\"}}, \\\"eval-supp-adapt-tau025-obj-s49\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.74, \\\"trigger_rate\\\": 0.0417, \\\"mean_uncertainty\\\": 0.1131, \\\"per_task_sr\\\": {\\\"soup\\\": 0.7, \\\"cream_cheese\\\": 0.65, \\\"salad\\\": 0.8, \\\"bbq\\\": 0.8, \\\"ketchup\\\": 0.75, \\\"tomato\\\": 0.75, \\\"butter\\\": 0.6, \\\"milk\\\": 0.6, \\\"pudding\\\": 0.8, \\\"oj\\\": 0.95}}}, \\\"eval-supp-adapt-tau025-obj-s48\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.76, \\\"trigger_rate\\\": 0.0389, \\\"mean_uncertainty\\\": 0.1117, \\\"per_task_sr\\\": {\\\"soup\\\": 0.75, \\\"cream_cheese\\\": 0.75, \\\"salad\\\": 0.7, \\\"bbq\\\": 0.9, \\\"ketchup\\\": 0.8, \\\"tomato\\\": 0.65, \\\"butter\\\": 0.6, \\\"milk\\\": 0.8, \\\"pudding\\\": 0.7, \\\"oj\\\": 0.95}}}, \\\"eval-supp-vla-only-obj-s49\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.755, \\\"per_task_sr\\\": {\\\"soup\\\": 0.55, \\\"cream_cheese\\\": 0.7, \\\"salad\\\": 0.8, \\\"bbq\\\": 0.95, \\\"ketchup\\\": 0.8, \\\"tomato\\\": 0.8, \\\"butter\\\": 0.6, \\\"milk\\\": 0.65, \\\"pudding\\\": 0.8, \\\"oj\\\": 0.9}}}, \\\"eval-supp-vla-only-obj-s48\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.79, \\\"per_task_sr\\\": {\\\"soup\\\": 0.65, \\\"cream_cheese\\\": 0.8, \\\"salad\\\": 0.75, \\\"bbq\\\": 0.9, \\\"ketchup\\\": 0.85, \\\"tomato\\\": 0.8, \\\"butter\\\": 0.65, \\\"milk\\\": 0.8, \\\"pudding\\\": 0.75, \\\"oj\\\": 0.95}}}, \\\"eval-supp-vla-only-goal-s49\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.82, \\\"per_task_sr\\\": {\\\"middle_drawer\\\": 0.75, \\\"bowl_stove\\\": 0.95, \\\"wine_cabinet\\\": 0.85, \\\"drawer_bowl\\\": 0.65, \\\"bowl_cabinet\\\": 0.95, \\\"push_plate\\\": 0.85, \\\"cream_cheese\\\": 0.55, \\\"stove_on\\\": 1, \\\"bowl_plate\\\": 0.85, \\\"wine_rack\\\": 0.8}}}, \\\"eval-supp-vla-only-goal-s48\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.85, \\\"per_task_sr\\\": {\\\"middle_drawer\\\": 0.9, \\\"bowl_stove\\\": 0.95, \\\"wine_cabinet\\\": 0.9, \\\"drawer_bowl\\\": 0.55, \\\"bowl_cabinet\\\": 1, \\\"push_plate\\\": 0.9, \\\"cream_cheese\\\": 0.6, \\\"stove_on\\\": 1, \\\"bowl_plate\\\": 0.9, \\\"wine_rack\\\": 0.8}}}, \\\"eval-supp-vla-only-spatial-s49\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.785, \\\"per_task_sr\\\": {\\\"between\\\": 0.9, \\\"next_ramekin\\\": 0.95, \\\"center\\\": 0.95, \\\"cookie_box\\\": 0.95, \\\"drawer\\\": 0.7, \\\"on_ramekin\\\": 0, \\\"next_cookie\\\": 0.9, \\\"stove\\\": 0.8, \\\"next_plate\\\": 0.75, \\\"cabinet\\\": 0.95}}}, \\\"eval-supp-vla-only-spatial-s48\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.795, \\\"per_task_sr\\\": {\\\"between\\\": 1, \\\"next_ramekin\\\": 0.9, \\\"center\\\": 0.95, \\\"cookie_box\\\": 0.95, \\\"drawer\\\": 0.8, \\\"on_ramekin\\\": 0, \\\"next_cookie\\\": 0.95, \\\"stove\\\": 0.75, \\\"next_plate\\\": 0.85, \\\"cabinet\\\": 0.8}}}}, \\\"count\\\": 10, \\\"total\\\": 953, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.313}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-obj-vla-only-s50\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.74, \"successes\": 148, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"object\", \"seed\": 50, \"mode\": \"vla_only\", \"model\": \"pi05\"}}, \"eval-supp-spatial-vla-only-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"spatial\", \"seed\": 42, \"mode\": \"vla_only\", \"model\": \"pi05\"}}, \"eval-supp-adapt-tau025-obj-s49\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.74, \"trigger_rate\": 0.0417, \"mean_uncertainty\": 0.1131, \"per_task_sr\": {\"soup\": 0.7, \"cream_cheese\": 0.65, \"salad\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.75, \"tomato\": 0.75, \"butter\": 0.6, \"milk\": 0.6, \"pudding\": 0.8, \"oj\": 0.95}}}, \"eval-supp-adapt-tau025-obj-s48\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.76, \"trigger_rate\": 0.0389, \"mean_uncertainty\": 0.1117, \"per_task_sr\": {\"soup\": 0.75, \"cream_cheese\": 0.75, \"salad\": 0.7, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.6, \"milk\": 0.8, \"pudding\": 0.7, \"oj\": 0.95}}}, \"eval-supp-vla-only-obj-s49\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.755, \"per_task_sr\": {\"soup\": 0.55, \"cream_cheese\": 0.7, \"salad\": 0.8, \"bbq\": 0.95, \"ketchup\": 0.8, \"tomato\": 0.8, \"butter\": 0.6, \"milk\": 0.65, \"pudding\": 0.8, \"oj\": 0.9}}}, \"eval-supp-vla-only-obj-s48\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.79, \"per_task_sr\": {\"soup\": 0.65, \"cream_cheese\": 0.8, \"salad\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.85, \"tomato\": 0.8, \"butter\": 0.65, \"milk\": 0.8, \"pudding\": 0.75, \"oj\": 0.95}}}, \"eval-supp-vla-only-goal-s49\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.82, \"per_task_sr\": {\"middle_drawer\": 0.75, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.65, \"bowl_cabinet\": 0.95, \"push_plate\": 0.85, \"cream_cheese\": 0.55, \"stove_on\": 1, \"bowl_plate\": 0.85, \"wine_rack\": 0.8}}}, \"eval-supp-vla-only-goal-s48\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.85, \"per_task_sr\": {\"middle_drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.9, \"drawer_bowl\": 0.55, \"bowl_cabinet\": 1, \"push_plate\": 0.9, \"cream_cheese\": 0.6, \"stove_on\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}}, \"eval-supp-vla-only-spatial-s49\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.785, \"per_task_sr\": {\"between\": 0.9, \"next_ramekin\": 0.95, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.7, \"on_ramekin\": 0, \"next_cookie\": 0.9, \"stove\": 0.8, \"next_plate\": 0.75, \"cabinet\": 0.95}}}, \"eval-supp-vla-only-spatial-s48\": {\"status\": \"PREPARING\", \"metrics\": {\"overall_sr\": 0.795, \"per_task_sr\": {\"between\": 1, \"next_ramekin\": 0.9, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.8, \"on_ramekin\": 0, \"next_cookie\": 0.95, \"stove\": 0.75, \"next_plate\": 0.85, \"cabinet\": 0.8}}}}, \"count\": 10, \"total\": 953, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.313}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HktpTeGujtRMYzdML4QBJ9`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "f8661e67-292a-42a2-aed4-b82d3a3c1ed4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01GNRDFJ3ZQeRZnwUsuFs1Ys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2372,
      "cache_read_input_tokens": 41136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2372
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

_source line 29 · 2026-05-24T19:28:17.559Z_

<details><summary>↩ Tool result · `toolu_01HktpTeGujtRMYzdML4QBJ9`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "5fee15af-a34b-46c0-a767-a90d36962089",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 29
  }
}
```

</details>

---


### Tool call

_source line 30_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01RQ1LrMFcttiHqpUeJo8d5B`</summary>

```json
{
  "todos": [
    {
      "content": "Check bjb2-28827 for s43 logs",
      "activeForm": "Checking bjb2-28827 for s43 logs",
      "status": "in_progress"
    },
    {
      "content": "Check bjb1-18228 for r4 log",
      "activeForm": "Checking bjb1-18228 for r4 log",
      "status": "pending"
    },
    {
      "content": "Check bjb1-32546 for r3 log",
      "activeForm": "Checking bjb1-32546 for r3 log",
      "status": "pending"
    },
    {
      "content": "Compare v1/v2/r3 results and analyze",
      "activeForm": "Comparing v1/v2/r3 results",
      "status": "pending"
    },
    {
      "content": "Write investigation report and update registry",
      "activeForm": "Writing investigation report",
      "status": "pending"
    }
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "51a4cefa-61f8-4d2a-9cde-d7fff06e626e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Kubpq61DLgd7VurJvPds2Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3512,
      "cache_read_input_tokens": 43508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3512
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


### Tool result

_source line 31 · 2026-05-24T19:28:23.401Z_

<details><summary>↩ Tool result · `toolu_01RQ1LrMFcttiHqpUeJo8d5B`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "5e249bbf-5ffc-4653-88fa-36695baab218",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Check bjb2-28827 for s43 logs",
        "status": "in_progress",
        "activeForm": "Checking bjb2-28827 for s43 logs"
      },
      {
        "content": "Check bjb1-18228 for r4 log",
        "status": "pending",
        "activeForm": "Checking bjb1-18228 for r4 log"
      },
      {
        "content": "Check bjb1-32546 for r3 log",
        "status": "pending",
        "activeForm": "Checking bjb1-32546 for r3 log"
      },
      {
        "content": "Compare v1/v2/r3 results and analyze",
        "status": "pending",
        "activeForm": "Comparing v1/v2/r3 results"
      },
      {
        "content": "Write investigation report and update registry",
        "status": "pending",
        "activeForm": "Writing investigation report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BEUjVAjWV8PLQQWfuM47ho`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs /tmp /root/runs -maxdepth 5 -name \"*pi05*object*s43*\" -o -name \"*pi05*object*seed43*\" -o -name \"*pi05*seed43*object*\"",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "4b702b3b-c7b4-45ee-99f5-bea3d9847518",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011Mtk3QTiUK5bnAyh13STmq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 391,
      "cache_read_input_tokens": 47020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 391
      },
      "output_tokens": 79,
      "service_tier": "standard",
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

_source line 33 · 2026-05-24T19:28:30.880Z_

<details><summary>↩ Tool result · `toolu_01BEUjVAjWV8PLQQWfuM47ho`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s43.log\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s43-v2.log\\n/tmp/agent-ml-exit/eval-pi05-vla-only-object-s43.exit\\n/tmp/agent-ml-exit/eval-pi05-vla-only-object-s43-v2.exit\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s43.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s43-v2.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "c086a5a9-31db-4690-b544-6b33dccdb020",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s43.log\\\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s43-v2.log\\\\n/tmp/agent-ml-exit/eval-pi05-vla-only-object-s43.exit\\\\n/tmp/agent-ml-exit/eval-pi05-vla-only-object-s43-v2.exit\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s43.log\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s43-v2.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.0}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s43.log\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s43-v2.log\\n/tmp/agent-ml-exit/eval-pi05-vla-only-object-s43.exit\\n/tmp/agent-ml-exit/eval-pi05-vla-only-object-s43-v2.exit\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s43.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s43-v2.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SmxzzUQC7Bw6noT141E6bt`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs /tmp /root/runs -maxdepth 5 -name \"*pi05*object*s43*\" -o -name \"*pi05*object*seed43*\" -o -name \"*pi05*seed43*object*\"",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "d658ba30-6ef5-4b64-b6cd-a419c31379d8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011Mtk3QTiUK5bnAyh13STmq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 391,
      "cache_read_input_tokens": 47020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 391
      },
      "output_tokens": 79,
      "service_tier": "standard",
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

_source line 35 · 2026-05-24T19:28:32.331Z_

<details><summary>↩ Tool result · `toolu_01SmxzzUQC7Bw6noT141E6bt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-acr-object-seed43.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "94dce8f0-900b-4a2b-9272-06484343aace",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/runs/acr-vla-conformal-refinement/eval-pi05-acr-object-seed43.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.92}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-acr-object-seed43.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QUjv7qsE8YT72yVY9Kydf7`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs /tmp /root/runs -maxdepth 5 -name \"*pi05*object*s43*\" -o -name \"*pi05*object*seed43*\" -o -name \"*pi05*seed43*object*\"",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "71e61f84-3276-4fdd-96f0-cc6497f89c4d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011Mtk3QTiUK5bnAyh13STmq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 391,
      "cache_read_input_tokens": 47020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 391
      },
      "output_tokens": 79,
      "service_tier": "standard",
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

_source line 37 · 2026-05-24T19:28:33.481Z_

<details><summary>↩ Tool result · `toolu_01QUjv7qsE8YT72yVY9Kydf7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed43.log\\n/tmp/agent-ml-exit/eval-pi05-vla-only-object-seed43.exit\\n/tmp/agent-ml-exit/eval-pi05-vla-only-object-seed43-r3.exit\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43-r3.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed43.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "f8d03519-133b-4fdb-9dc6-4426b4a639bf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed43.log\\\\n/tmp/agent-ml-exit/eval-pi05-vla-only-object-seed43.exit\\\\n/tmp/agent-ml-exit/eval-pi05-vla-only-object-seed43-r3.exit\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43.log\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43-r3.log\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed43.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.89}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed43.log\\n/tmp/agent-ml-exit/eval-pi05-vla-only-object-seed43.exit\\n/tmp/agent-ml-exit/eval-pi05-vla-only-object-seed43-r3.exit\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43-r3.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed43.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "3f4adf93-82c1-4432-ba29-81e079352082",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018JvZ18SrMW46xPJfV1rqQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1526,
      "cache_read_input_tokens": 47411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1526
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


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015qzccPpzrboPDZsyf2A9VD`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -60 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s43.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "5d4a6053-bc6d-4a1e-9253-01946f6c3dbb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018JvZ18SrMW46xPJfV1rqQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1526,
      "cache_read_input_tokens": 47411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1526
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

_source line 40 · 2026-05-24T19:28:45.815Z_

<details><summary>↩ Tool result · `toolu_015qzccPpzrboPDZsyf2A9VD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 13/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 18/20\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 90.0% (18/20)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n\\n============================================================\\nOverall success rate (vla_only): 98.5% (197/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "ee0881bc-c3c1-4324-8cc7-64dec532a05b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\\\n[eval] Loading LIBERO object environments...\\\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n[eval] 10 tasks loaded.\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 13/15\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 18/20\\\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 90.0% (18/20)\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\\\n\\\\n============================================================\\\\nOverall success rate (vla_only): 98.5% (197/200)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 13/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 18/20\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 90.0% (18/20)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n\\n============================================================\\nOverall success rate (vla_only): 98.5% (197/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014KVrZaWp4fvAdWfRWYfQM7`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -60 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s43-v2.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "be755e39-09ed-406a-9b2d-3bb229896701",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018JvZ18SrMW46xPJfV1rqQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1526,
      "cache_read_input_tokens": 47411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1526
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

_source line 42 · 2026-05-24T19:28:46.841Z_

<details><summary>↩ Tool result · `toolu_014KVrZaWp4fvAdWfRWYfQM7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py\\\", line 1787, in _call_impl\\n    return forward_call(*args, **kwargs)\\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/lerobot/policies/pi_gemma.py\\\", line 117, in forward\\n    normed = self._norm(x)\\n             ^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/lerobot/policies/pi_gemma.py\\\", line 106, in _norm\\n    var = torch.mean(torch.square(x.float()), dim=-1, keepdim=True)\\n                                  ^^^^^^^^^\\ntorch.OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 21.75 MiB is free. Process 388316 has 12.44 GiB memory in use. Including non-PyTorch memory, this process has 11.02 GiB memory in use. Of the allocated memory 8.74 GiB is allocated by PyTorch, and 225.04 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/20, success so far: 4/10\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 9/15\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 14/20\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n\\n============================================================\\nOverall success rate (vla_only): 86.5% (173/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "9a47cbb0-dec1-47b7-ab47-1edea04cb5e9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  File \\\\\\\"/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py\\\\\\\", line 1787, in _call_impl\\\\n    return forward_call(*args, **kwargs)\\\\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\\\n  File \\\\\\\"/root/miniconda3/lib/python3.12/site-packages/lerobot/policies/pi_gemma.py\\\\\\\", line 117, in forward\\\\n    normed = self._norm(x)\\\\n             ^^^^^^^^^^^^^\\\\n  File \\\\\\\"/root/miniconda3/lib/python3.12/site-packages/lerobot/policies/pi_gemma.py\\\\\\\", line 106, in _norm\\\\n    var = torch.mean(torch.square(x.float()), dim=-1, keepdim=True)\\\\n                                  ^^^^^^^^^\\\\ntorch.OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 21.75 MiB is free. Process 388316 has 12.44 GiB memory in use. Including non-PyTorch memory, this process has 11.02 GiB memory in use. Of the allocated memory 8.74 GiB is allocated by PyTorch, and 225.04 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/20, success so far: 4/10\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 9/15\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 14/20\\\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n\\\\n============================================================\\\\nOverall success rate (vla_only): 86.5% (173/200)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py\\\", line 1787, in _call_impl\\n    return forward_call(*args, **kwargs)\\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/lerobot/policies/pi_gemma.py\\\", line 117, in forward\\n    normed = self._norm(x)\\n             ^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/lerobot/policies/pi_gemma.py\\\", line 106, in _norm\\n    var = torch.mean(torch.square(x.float()), dim=-1, keepdim=True)\\n                                  ^^^^^^^^^\\ntorch.OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 21.75 MiB is free. Process 388316 has 12.44 GiB memory in use. Including non-PyTorch memory, this process has 11.02 GiB memory in use. Of the allocated memory 8.74 GiB is allocated by PyTorch, and 225.04 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/20, success so far: 4/10\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 9/15\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 14/20\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n\\n============================================================\\nOverall success rate (vla_only): 86.5% (173/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SuikhrUNnsk9i88uLuHDUi`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "head -30 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s43.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "cc2fe4fa-7431-493a-9121-34edaa02785d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018JvZ18SrMW46xPJfV1rqQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1526,
      "cache_read_input_tokens": 47411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1526
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

_source line 44 · 2026-05-24T19:28:48.439Z_

<details><summary>↩ Tool result · `toolu_01SuikhrUNnsk9i88uLuHDUi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 13/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 18/20\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 90.0% (18/20)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "7137d0d4-3986-4448-8bfb-30160d8e0573",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\\\n[eval] Mode: vla_only, benchmark: object\\\\n[eval] max_steps set to 280 for benchmark object\\\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\\\nThe PI05 model is a direct port of the OpenPI implementation. \\\\nThis implementation follows the original OpenPI structure for compatibility. \\\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\\\n✓ Loaded state dict from model.safetensors\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\\\nAll keys loaded successfully!\\\\n[pi05] Fixed 437 vision tower keys\\\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\\\n[eval] Loading LIBERO object environments...\\\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n[eval] 10 tasks loaded.\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 13/15\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 18/20\\\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 90.0% (18/20)\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 13/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 18/20\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 90.0% (18/20)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MdnmSrfxhSpDgAeXggEVNj`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "head -30 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s43-v2.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "08bc711c-7133-438f-af20-0f9280893ff9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018JvZ18SrMW46xPJfV1rqQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1526,
      "cache_read_input_tokens": 47411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1526
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

_source line 46 · 2026-05-24T19:28:49.050Z_

<details><summary>↩ Tool result · `toolu_01MdnmSrfxhSpDgAeXggEVNj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n[rollout] Exception at step 0: CUDA out of memory. Tried to allocate 2.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 10.69 MiB is free. Process 388316 has 12.45 GiB memory in use. Including non-PyTorch memory, this process has 11.02 GiB memory in use. Of the allocated memory 8.71 GiB is allocated by PyTorch, and 226.65 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)\\nTraceback (most recent call last):\\n  File \\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\", line 510, in rollout_single\\n    action_7d = action_fn(obs)\\n                ^^^^^^^^^^^^^^\\n  File \\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\", line 679, in &lt;lambda>\\n    action_fn = lambda obs: select_action_vla_only(\\n                            ^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\", line 183, in select_action_vla_only\\n    return wrapper.predict_action(\\n           ^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/utils/_contextlib.py\\\", line 124, in decorate_context\\n    return func(*args, **kwargs)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "5efaeb72-5227-4475-bd56-b94f9ef8502d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\\\n[eval] Mode: vla_only, benchmark: object\\\\n[eval] max_steps set to 280 for benchmark object\\\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\\\nThe PI05 model is a direct port of the OpenPI implementation. \\\\nThis implementation follows the original OpenPI structure for compatibility. \\\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\\\n✓ Loaded state dict from model.safetensors\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\\\nAll keys loaded successfully!\\\\n[pi05] Fixed 437 vision tower keys\\\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\\\n[eval] Loading LIBERO object environments...\\\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n[eval] 10 tasks loaded.\\\\n[rollout] Exception at step 0: CUDA out of memory. Tried to allocate 2.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 10.69 MiB is free. Process 388316 has 12.45 GiB memory in use. Including non-PyTorch memory, this process has 11.02 GiB memory in use. Of the allocated memory 8.71 GiB is allocated by PyTorch, and 226.65 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)\\\\nTraceback (most recent call last):\\\\n  File \\\\\\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\\\\\", line 510, in rollout_single\\\\n    action_7d = action_fn(obs)\\\\n                ^^^^^^^^^^^^^^\\\\n  File \\\\\\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\\\\\", line 679, in &lt;lambda>\\\\n    action_fn = lambda obs: select_action_vla_only(\\\\n                            ^^^^^^^^^^^^^^^^^^^^^^^\\\\n  File \\\\\\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\\\\\", line 183, in select_action_vla_only\\\\n    return wrapper.predict_action(\\\\n           ^^^^^^^^^^^^^^^^^^^^^^^\\\\n  File \\\\\\\"/root/miniconda3/lib/python3.12/site-packages/torch/utils/_contextlib.py\\\\\\\", line 124, in decorate_context\\\\n    return func(*args, **kwargs)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n[rollout] Exception at step 0: CUDA out of memory. Tried to allocate 2.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 10.69 MiB is free. Process 388316 has 12.45 GiB memory in use. Including non-PyTorch memory, this process has 11.02 GiB memory in use. Of the allocated memory 8.71 GiB is allocated by PyTorch, and 226.65 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)\\nTraceback (most recent call last):\\n  File \\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\", line 510, in rollout_single\\n    action_7d = action_fn(obs)\\n                ^^^^^^^^^^^^^^\\n  File \\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\", line 679, in &lt;lambda>\\n    action_fn = lambda obs: select_action_vla_only(\\n                            ^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\", line 183, in select_action_vla_only\\n    return wrapper.predict_action(\\n           ^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/utils/_contextlib.py\\\", line 124, in decorate_context\\n    return func(*args, **kwargs)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 47_

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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "5ed11d79-c7ab-4105-92dd-5bffdc6b2b56",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011Qw8Xw9eN7E8k3JRk1xZbS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10065,
      "cache_read_input_tokens": 48937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10065
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


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01P7Doi5TtoiuFrvnG6w7Z9b`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -60 /root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43-r3.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "7593c01a-917c-4602-81d0-7dfda29619c2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011Qw8Xw9eN7E8k3JRk1xZbS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10065,
      "cache_read_input_tokens": 48937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10065
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

_source line 49 · 2026-05-24T19:29:25.113Z_

<details><summary>↩ Tool result · `toolu_01P7Doi5TtoiuFrvnG6w7Z9b`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 12/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 6/10\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 10/15\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 14/20\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 13/15\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 17/20\\n[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 85.0% (17/20)\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 15/20, success so far: 11/15\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\n[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 3/5\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 6/10\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 8/15\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 12/20\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 60.0% (12/20)\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/20, success so far: 3/5\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 7/10\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 11/15\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 3/5\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 15/20, success so far: 10/15\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 14/20\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\n\\n============================================================\\nOverall success rate (vla_only): 81.5% (163/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "a34e992d-735a-40db-9697-979fcce420cb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[eval] Loading LIBERO object environments...\\\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n[eval] 10 tasks loaded.\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 12/15\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 6/10\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 10/15\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 14/20\\\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 13/15\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 17/20\\\\n[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 85.0% (17/20)\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 15/20, success so far: 11/15\\\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\\\n[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 3/5\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 6/10\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 8/15\\\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 12/20\\\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 60.0% (12/20)\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/20, success so far: 3/5\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 7/10\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 11/15\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 3/5\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 15/20, success so far: 10/15\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 14/20\\\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\\\n\\\\n============================================================\\\\nOverall success rate (vla_only): 81.5% (163/200)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\nEXIT_CODE=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 12/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 6/10\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 10/15\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 14/20\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 13/15\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 17/20\\n[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 85.0% (17/20)\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 15/20, success so far: 11/15\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\n[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 3/5\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 6/10\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 8/15\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 12/20\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 60.0% (12/20)\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/20, success so far: 3/5\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 7/10\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 11/15\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 3/5\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 15/20, success so far: 10/15\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 14/20\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\n\\n============================================================\\nOverall success rate (vla_only): 81.5% (163/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012viVPxLK58zoVpqWrhGurM`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -20 /root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43-r3.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "bd52e506-e005-4ac1-80cc-97614ac1d031",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011Qw8Xw9eN7E8k3JRk1xZbS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10065,
      "cache_read_input_tokens": 48937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10065
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

_source line 51 · 2026-05-24T19:29:26.137Z_

<details><summary>↩ Tool result · `toolu_012viVPxLK58zoVpqWrhGurM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 12/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "aedcec3b-a3f0-4c7d-b87a-10a7561d1996",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\\\n[eval] Mode: vla_only, benchmark: object\\\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\\\nThe PI05 model is a direct port of the OpenPI implementation. \\\\nThis implementation follows the original OpenPI structure for compatibility. \\\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\\\n✓ Loaded state dict from model.safetensors\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\\\nAll keys loaded successfully!\\\\n[pi05] Fixed 437 vision tower keys\\\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\\\n[eval] Loading LIBERO object environments...\\\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n[eval] 10 tasks loaded.\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 12/15\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 12/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MLqkWKUNphoE4JfjGFfEYK`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -60 /root/runs/acr-vla-conformal-refinement/eval-pi05-acr-object-seed43.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "7d060757-fb56-48f9-8205-ed065bcea33f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011Qw8Xw9eN7E8k3JRk1xZbS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10065,
      "cache_read_input_tokens": 48937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10065
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

_source line 53 · 2026-05-24T19:29:27.222Z_

<details><summary>↩ Tool result · `toolu_01MLqkWKUNphoE4JfjGFfEYK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_pi05_full/object/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 10, 'mode': 'acr_vla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 2048, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_acr_vla_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: acr_vla, benchmark: object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_pi05_full/object/crm_best.pt (615,966 params)\\n[eval] PI05 features (2048D) passed directly to CRM (no projection)\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "ca39f1d4-4871-4887-a616-dbcce2cc7928",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[robosuite WARNING] No private macro file found! (__init__.py:7)\\\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\\\n[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_pi05_full/object/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 10, 'mode': 'acr_vla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 2048, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_acr_vla_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\\\n[eval] Mode: acr_vla, benchmark: object\\\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\\\nThe PI05 model is a direct port of the OpenPI implementation. \\\\nThis implementation follows the original OpenPI structure for compatibility. \\\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\\\n✓ Loaded state dict from model.safetensors\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\\\nAll keys loaded successfully!\\\\n[pi05] Fixed 437 vision tower keys\\\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_pi05_full/object/crm_best.pt (615,966 params)\\\\n[eval] PI05 features (2048D) passed directly to CRM (no projection)\\\\n[eval] Loading LIBERO object environments...\\\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n[eval] 10 tasks loaded.\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_pi05_full/object/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 10, 'mode': 'acr_vla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 2048, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_acr_vla_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: acr_vla, benchmark: object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_pi05_full/object/crm_best.pt (615,966 params)\\n[eval] PI05 features (2048D) passed directly to CRM (no projection)\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018NqnhqkC4gm5xxttF2Zvjg`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /tmp -name \"*pi05*seed43*\" -o -name \"*pi05_seed43*\"",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "7698944a-60ba-43fb-a12a-8b3cd35f52be",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011Qw8Xw9eN7E8k3JRk1xZbS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10065,
      "cache_read_input_tokens": 48937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10065
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

_source line 55 · 2026-05-24T19:29:28.268Z_

<details><summary>↩ Tool result · `toolu_018NqnhqkC4gm5xxttF2Zvjg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/tmp/agent-ml-exit/eval-pi05-vla-only-long-seed43-r4.exit\\n/tmp/eval_pi05_seed43_r4.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "3307f743-726a-438e-9947-416cb2e96350",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/tmp/agent-ml-exit/eval-pi05-vla-only-long-seed43-r4.exit\\\\n/tmp/eval_pi05_seed43_r4.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/tmp/agent-ml-exit/eval-pi05-vla-only-long-seed43-r4.exit\\n/tmp/eval_pi05_seed43_r4.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 56_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01UvHozMZsJGE5goeznEW9VG`</summary>

```json
{
  "todos": [
    {
      "content": "Check bjb2-28827 for s43 logs",
      "activeForm": "Checking bjb2-28827 for s43 logs",
      "status": "completed"
    },
    {
      "content": "Check bjb1-18228 for r4 log",
      "activeForm": "Checking bjb1-18228 for r4 log",
      "status": "in_progress"
    },
    {
      "content": "Check bjb1-32546 for r3 log",
      "activeForm": "Checking bjb1-32546 for r3 log",
      "status": "completed"
    },
    {
      "content": "Compare v1/v2/r3 results and analyze",
      "activeForm": "Comparing v1/v2/r3 results",
      "status": "pending"
    },
    {
      "content": "Write investigation report and update registry",
      "activeForm": "Writing investigation report",
      "status": "pending"
    }
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "c5691149-93f9-44a5-9e2a-091b2420ea75",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0191rXggPUp2ruW33sSPojG7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8285,
      "cache_read_input_tokens": 59002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8285
      },
      "output_tokens": 64,
      "service_tier": "standard",
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

_source line 57 · 2026-05-24T19:29:33.561Z_

<details><summary>↩ Tool result · `toolu_01UvHozMZsJGE5goeznEW9VG`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "2b2febb6-b364-4114-84f8-b9956b926ad9",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Check bjb2-28827 for s43 logs",
        "status": "in_progress",
        "activeForm": "Checking bjb2-28827 for s43 logs"
      },
      {
        "content": "Check bjb1-18228 for r4 log",
        "status": "pending",
        "activeForm": "Checking bjb1-18228 for r4 log"
      },
      {
        "content": "Check bjb1-32546 for r3 log",
        "status": "pending",
        "activeForm": "Checking bjb1-32546 for r3 log"
      },
      {
        "content": "Compare v1/v2/r3 results and analyze",
        "status": "pending",
        "activeForm": "Comparing v1/v2/r3 results"
      },
      {
        "content": "Write investigation report and update registry",
        "status": "pending",
        "activeForm": "Writing investigation report"
      }
    ],
    "newTodos": [
      {
        "content": "Check bjb2-28827 for s43 logs",
        "status": "completed",
        "activeForm": "Checking bjb2-28827 for s43 logs"
      },
      {
        "content": "Check bjb1-18228 for r4 log",
        "status": "in_progress",
        "activeForm": "Checking bjb1-18228 for r4 log"
      },
      {
        "content": "Check bjb1-32546 for r3 log",
        "status": "completed",
        "activeForm": "Checking bjb1-32546 for r3 log"
      },
      {
        "content": "Compare v1/v2/r3 results and analyze",
        "status": "pending",
        "activeForm": "Comparing v1/v2/r3 results"
      },
      {
        "content": "Write investigation report and update registry",
        "status": "pending",
        "activeForm": "Writing investigation report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 58_

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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "2641628c-c27e-40d3-9615-5a9323795c5d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Jwis8RREZxLd8LkaUdU3D8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 67287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
      },
      "output_tokens": 74,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013oZ5iYzMKCAgzXwsGur7CJ`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "head -20 /tmp/eval_pi05_seed43_r4.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "4d9b0d14-1731-46b8-afef-9f26d92f739f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Jwis8RREZxLd8LkaUdU3D8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 67287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
      },
      "output_tokens": 74,
      "service_tier": "standard",
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

_source line 60 · 2026-05-24T19:29:56.495Z_

<details><summary>↩ Tool result · `toolu_013oZ5iYzMKCAgzXwsGur7CJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "488435ab-6f36-41f6-ade5-537564670f28",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[robosuite WARNING] No private macro file found! (__init__.py:7)\\\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\\\n[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\\\n[eval] Mode: vla_only, benchmark: object\\\\n[eval] max_steps set to 280 for benchmark object\\\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\\\nThe PI05 model is a direct port of the OpenPI implementation. \\\\nThis implementation follows the original OpenPI structure for compatibility. \\\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\\\n✓ Loaded state dict from model.safetensors\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\\\nAll keys loaded successfully!\\\\n[pi05] Fixed 437 vision tower keys\\\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\\\n[eval] Loading LIBERO object environments...\\\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n[eval] 10 tasks loaded.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed43.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 61_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CMRcYBPuuyxmwbm3HnFFkb`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -20 /tmp/eval_pi05_seed43_r4.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "dc8ebbc1-fb9d-4068-8871-d08c315fbe02",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Jwis8RREZxLd8LkaUdU3D8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 67287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
      },
      "output_tokens": 74,
      "service_tier": "standard",
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

_source line 62 · 2026-05-24T19:29:57.554Z_

<details><summary>↩ Tool result · `toolu_01CMRcYBPuuyxmwbm3HnFFkb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n\\n============================================================\\nOverall success rate (vla_only): 98.5% (197/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "d24c2421-8191-4988-9ebb-2ed0d25e26e0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\\\n\\\\n============================================================\\\\nOverall success rate (vla_only): 98.5% (197/200)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 15/15\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/20, success so far: 9/10\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n\\n============================================================\\nOverall success rate (vla_only): 98.5% (197/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VxMKyQWUosjFbdJEhGBGQ5`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*pi05*vla*object*42*\" -o -name \"*pi05*vla*object*44*\" -o -name \"*pi05*object*seed42*\" -o -name \"*pi05*object*seed44*\"",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "05c00732-60d2-4334-b940-0de6cb1ea8d5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Jwis8RREZxLd8LkaUdU3D8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 67287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
      },
      "output_tokens": 74,
      "service_tier": "standard",
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

_source line 64 · 2026-05-24T19:29:59.115Z_

<details><summary>↩ Tool result · `toolu_01VxMKyQWUosjFbdJEhGBGQ5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-pi05-reconvla-object-s42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "90adec84-2fb0-460a-9a96-ee78c008ccb4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-pi05-reconvla-object-s42.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-pi05-reconvla-object-s42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AWNBamGUXYKj9VC63kCaTx`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs /root/runs -maxdepth 4 -name \"*pi05*vla*object*42*\" -o -name \"*pi05*vla*object*44*\" -o -name \"*pi05*object*seed42*\" -o -name \"*pi05*object*seed44*\"",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "dc7a26fa-2629-4052-ad7e-e1d5d588dcc9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Jwis8RREZxLd8LkaUdU3D8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 67287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
      },
      "output_tokens": 74,
      "service_tier": "standard",
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

_source line 66 · 2026-05-24T19:30:00.598Z_

<details><summary>↩ Tool result · `toolu_01AWNBamGUXYKj9VC63kCaTx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s42.log\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s42-v2.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42-r3.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44-r3.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-acr-object-seed44.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed42.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed44.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s42.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s42-v2.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "6b8712bd-9f0a-4e4d-87d9-25fbedb81821",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed42.log\\\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed44.log\\\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s42.log\\\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s42-v2.log\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42.log\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44.log\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42-r3.log\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44-r3.log\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-acr-object-seed44.log\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed42.log\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed44.log\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s42.log\\\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s42-v2.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s42.log\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s42-v2.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42-r3.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44-r3.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-acr-object-seed44.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed42.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed44.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s42.log\\n/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s42-v2.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 67_

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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "f1ae8d1a-082f-4887-8ba8-4d90d9ad012c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018xWPV8mGMKSvJsvr11UCCV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5117,
      "cache_read_input_tokens": 67672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5117
      },
      "output_tokens": 74,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01B1D13tCVPWeyKsvAtcqz5K`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -10 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed42.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "217c04b2-8f5a-4605-8f77-def31268119d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018xWPV8mGMKSvJsvr11UCCV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5117,
      "cache_read_input_tokens": 67672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5117
      },
      "output_tokens": 74,
      "service_tier": "standard",
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

_source line 69 · 2026-05-24T19:30:10.955Z_

<details><summary>↩ Tool result · `toolu_01B1D13tCVPWeyKsvAtcqz5K`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_pi05_vla_only_object_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "c5ebb992-8c35-4169-bd6f-b2a5b020257e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_pi05_vla_only_object_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\\\n[eval] Mode: vla_only, benchmark: object\\\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\\\nThe PI05 model is a direct port of the OpenPI implementation. \\\\nThis implementation follows the original OpenPI structure for compatibility. \\\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\\\n✓ Loaded state dict from model.safetensors\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_pi05_vla_only_object_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SUGYD1ZX4UL7c9pAxx5ijy`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed42.log /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed44.log /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s42.log /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s42-v2.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "48ab7bee-b994-4d74-9cd4-58c7e4063797",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018xWPV8mGMKSvJsvr11UCCV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5117,
      "cache_read_input_tokens": 67672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5117
      },
      "output_tokens": 74,
      "service_tier": "standard",
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

_source line 71 · 2026-05-24T19:30:13.357Z_

<details><summary>↩ Tool result · `toolu_01SUGYD1ZX4UL7c9pAxx5ijy`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"tail: option used in invalid context -- 5\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "fe34637d-f4bd-40da-b5c0-ac513d8ec141",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"tail: option used in invalid context -- 5\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"tail: option used in invalid context -- 5\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E17yjBmqtp9s8T5DFzXWXo`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -10 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s42.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "5f13282a-9298-4680-a95b-f112dbe9768c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018xWPV8mGMKSvJsvr11UCCV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5117,
      "cache_read_input_tokens": 67672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5117
      },
      "output_tokens": 74,
      "service_tier": "standard",
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

_source line 73 · 2026-05-24T19:30:14.471Z_

<details><summary>↩ Tool result · `toolu_01E17yjBmqtp9s8T5DFzXWXo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "ab6a93bb-454d-4fd5-86b5-7bddcb1987dd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\\\n[eval] Mode: vla_only, benchmark: object\\\\n[eval] max_steps set to 280 for benchmark object\\\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\\\nThe PI05 model is a direct port of the OpenPI implementation. \\\\nThis implementation follows the original OpenPI structure for compatibility. \\\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\\\n✓ Loaded state dict from model.safetensors\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 74_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PgRs2M9Yr5gLFqgUifoBiy`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -10 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s42-v2.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "b75f6bce-dc50-4d65-8a7f-4708093c0aca",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018xWPV8mGMKSvJsvr11UCCV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5117,
      "cache_read_input_tokens": 67672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5117
      },
      "output_tokens": 74,
      "service_tier": "standard",
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

_source line 75 · 2026-05-24T19:30:16.401Z_

<details><summary>↩ Tool result · `toolu_01PgRs2M9Yr5gLFqgUifoBiy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "e244beca-35c7-444b-8762-d34a1454fdf9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\\\n[eval] Mode: vla_only, benchmark: object\\\\n[eval] max_steps set to 280 for benchmark object\\\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\\\nThe PI05 model is a direct port of the OpenPI implementation. \\\\nThis implementation follows the original OpenPI structure for compatibility. \\\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\\\n✓ Loaded state dict from model.safetensors\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017ko8AKamHLfhwSkdvrkeZh`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -8 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed42.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "0c6a2770-0afc-445e-a374-a3a97c5cad07",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MnczZfGfF8d7gQw3doAe9J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3786,
      "cache_read_input_tokens": 72789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3786
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 77 · 2026-05-24T19:30:24.589Z_

<details><summary>↩ Tool result · `toolu_017ko8AKamHLfhwSkdvrkeZh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 0.0% (0/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 0/15\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 0/20\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 0.0% (0/20)\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "65cf835e-6fba-419d-abad-21fd0f37250e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 0.0% (0/20)\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 0/15\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 0/20\\\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 0.0% (0/20)\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 0.0% (0/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 0/15\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 0/20\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 0.0% (0/20)\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 78_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HSc5NSLUYAQXJGESEyvrLx`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -8 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed44.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "ce7ceea9-cb1a-4b80-9764-e2294f9ce1f4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MnczZfGfF8d7gQw3doAe9J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3786,
      "cache_read_input_tokens": 72789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3786
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 79_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DFroWvkinnT8FU41tdJXpK`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -8 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s42.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "47e1bb39-aa67-4e60-a923-653960527c90",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MnczZfGfF8d7gQw3doAe9J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3786,
      "cache_read_input_tokens": 72789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3786
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 80 · 2026-05-24T19:30:26.145Z_

<details><summary>↩ Tool result · `toolu_01HSc5NSLUYAQXJGESEyvrLx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 0.0% (0/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 0/15\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 0/20\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 0.0% (0/20)\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "bab78c53-249d-41f4-8201-40613736a2cf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 0.0% (0/20)\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 0/15\\\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 0/20\\\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 0.0% (0/20)\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 0.0% (0/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 15/20, success so far: 0/15\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 20/20, success so far: 0/20\\n[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 0.0% (0/20)\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_bbq_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-24T19:30:26.561Z_

<details><summary>↩ Tool result · `toolu_01DFroWvkinnT8FU41tdJXpK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n\\n============================================================\\nOverall success rate (vla_only): 100.0% (200/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed42.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "d930e30f-5f25-44e6-9422-27671c3f29b6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\\\n\\\\n============================================================\\\\nOverall success rate (vla_only): 100.0% (200/200)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed42.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 20/20\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 100.0% (20/20)\\n\\n============================================================\\nOverall success rate (vla_only): 100.0% (200/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed42.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 82_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011eJjN8b7XTxifyogf49Sj3`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -8 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s42-v2.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "fd6f9c1e-c39e-49f7-9aad-9cd5512942dd",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MnczZfGfF8d7gQw3doAe9J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3786,
      "cache_read_input_tokens": 72789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3786
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 83 · 2026-05-24T19:30:27.448Z_

<details><summary>↩ Tool result · `toolu_011eJjN8b7XTxifyogf49Sj3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n\\n============================================================\\nOverall success rate (vla_only): 96.5% (193/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed42.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "795c481d-256c-4f7d-be70-9b1db2f3808f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\\\n\\\\n============================================================\\\\nOverall success rate (vla_only): 96.5% (193/200)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed42.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n\\n============================================================\\nOverall success rate (vla_only): 96.5% (193/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed42.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 84_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VewHCT9WettWVR8rfKi4eq`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -10 /root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-seed44.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "a2c34cb5-f322-4397-9bfe-7ba3cc2adb78",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MnczZfGfF8d7gQw3doAe9J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3786,
      "cache_read_input_tokens": 72789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3786
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 85 · 2026-05-24T19:30:29.767Z_

<details><summary>↩ Tool result · `toolu_01VewHCT9WettWVR8rfKi4eq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 44, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_pi05_vla_only_object_seed44.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "e928864c-4199-4074-92bc-c4609b1e297d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 44, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_pi05_vla_only_object_seed44.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\\\n[eval] Mode: vla_only, benchmark: object\\\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\\\nThe PI05 model is a direct port of the OpenPI implementation. \\\\nThis implementation follows the original OpenPI structure for compatibility. \\\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\\\n✓ Loaded state dict from model.safetensors\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 44, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_pi05_vla_only_object_seed44.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 86_

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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "ea2000a2-711a-4e02-b951-799d08378827",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01B58WJAry6Ry7BVGXCsgygV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3537,
      "cache_read_input_tokens": 76575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3537
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01VrMyPLRMnyAGE7PPoRnj82`</summary>

```json
{
  "todos": [
    {
      "content": "Check bjb2-28827 for s43 logs",
      "activeForm": "Checking bjb2-28827 for s43 logs",
      "status": "completed"
    },
    {
      "content": "Check bjb1-18228 for r4 log",
      "activeForm": "Checking bjb1-18228 for r4 log",
      "status": "completed"
    },
    {
      "content": "Check bjb1-32546 for r3 log",
      "activeForm": "Checking bjb1-32546 for r3 log",
      "status": "completed"
    },
    {
      "content": "Cross-check s42/s44 to determine which eval setup is canonical",
      "activeForm": "Cross-checking s42/s44 baselines",
      "status": "in_progress"
    },
    {
      "content": "Write investigation report and update registry",
      "activeForm": "Writing investigation report",
      "status": "pending"
    }
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "9607528d-74ab-4d4e-8071-7643dd6039b3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01B58WJAry6Ry7BVGXCsgygV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3537,
      "cache_read_input_tokens": 76575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3537
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 88 · 2026-05-24T19:30:45.619Z_

<details><summary>↩ Tool result · `toolu_01VrMyPLRMnyAGE7PPoRnj82`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "93380f27-b60d-41a5-a9ef-ed2d2df06bb0",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Check bjb2-28827 for s43 logs",
        "status": "completed",
        "activeForm": "Checking bjb2-28827 for s43 logs"
      },
      {
        "content": "Check bjb1-18228 for r4 log",
        "status": "in_progress",
        "activeForm": "Checking bjb1-18228 for r4 log"
      },
      {
        "content": "Check bjb1-32546 for r3 log",
        "status": "completed",
        "activeForm": "Checking bjb1-32546 for r3 log"
      },
      {
        "content": "Compare v1/v2/r3 results and analyze",
        "status": "pending",
        "activeForm": "Comparing v1/v2/r3 results"
      },
      {
        "content": "Write investigation report and update registry",
        "status": "pending",
        "activeForm": "Writing investigation report"
      }
    ],
    "newTodos": [
      {
        "content": "Check bjb2-28827 for s43 logs",
        "status": "completed",
        "activeForm": "Checking bjb2-28827 for s43 logs"
      },
      {
        "content": "Check bjb1-18228 for r4 log",
        "status": "completed",
        "activeForm": "Checking bjb1-18228 for r4 log"
      },
      {
        "content": "Check bjb1-32546 for r3 log",
        "status": "completed",
        "activeForm": "Checking bjb1-32546 for r3 log"
      },
      {
        "content": "Cross-check s42/s44 to determine which eval setup is canonical",
        "status": "in_progress",
        "activeForm": "Cross-checking s42/s44 baselines"
      },
      {
        "content": "Write investigation report and update registry",
        "status": "pending",
        "activeForm": "Writing investigation report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Tool call

_source line 89_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WtDTDPND6YzT5iMSHRGrTA`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -8 /root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42-r3.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "f514fb56-cbab-42f7-b8d4-f1ff4f50ba84",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EUYcm21P5n5nEWyiotvg8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 80112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 852
      },
      "output_tokens": 66,
      "service_tier": "standard",
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

_source line 90 · 2026-05-24T19:30:51.233Z_

<details><summary>↩ Tool result · `toolu_01WtDTDPND6YzT5iMSHRGrTA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\n\\n============================================================\\nOverall success rate (vla_only): 82.0% (164/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed42.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "26c3cdfb-0fc9-4f6c-8bc1-d583fd839563",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\\\n\\\\n============================================================\\\\nOverall success rate (vla_only): 82.0% (164/200)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed42.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\nEXIT_CODE=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\n\\n============================================================\\nOverall success rate (vla_only): 82.0% (164/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed42.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 91_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DPF8UMEkGrbnLzzbCUri1i`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -10 /root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42-r3.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "10ab7b07-c417-47b9-9bd3-2df0f5bcded9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EUYcm21P5n5nEWyiotvg8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 80112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 852
      },
      "output_tokens": 66,
      "service_tier": "standard",
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

_source line 92 · 2026-05-24T19:30:52.836Z_

<details><summary>↩ Tool result · `toolu_01DPF8UMEkGrbnLzzbCUri1i`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "b0ee9f6c-8801-4caa-8863-684d6cc022fa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\\\n[eval] Mode: vla_only, benchmark: object\\\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\\\nThe PI05 model is a direct port of the OpenPI implementation. \\\\nThis implementation follows the original OpenPI structure for compatibility. \\\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\\\n✓ Loaded state dict from model.safetensors\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 93_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01P2KbTC4U5u98K9eJ5sAyWs`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -8 /root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44-r3.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "03407f26-d550-4f3f-b21a-901a480ca80f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EUYcm21P5n5nEWyiotvg8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 80112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 852
      },
      "output_tokens": 66,
      "service_tier": "standard",
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

_source line 94 · 2026-05-24T19:30:53.834Z_

<details><summary>↩ Tool result · `toolu_01P2KbTC4U5u98K9eJ5sAyWs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\n\\n============================================================\\nOverall success rate (vla_only): 81.0% (162/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed44.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "4fe0bae5-2c19-4d71-b5a4-3da9331ec14b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\\\n\\\\n============================================================\\\\nOverall success rate (vla_only): 81.0% (162/200)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed44.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\nEXIT_CODE=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\n\\n============================================================\\nOverall success rate (vla_only): 81.0% (162/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed44.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 95_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019pDLFR5fdBVpsteJxAqrvy`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -10 /root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44-r3.log",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "8e3110ae-0651-49ac-9c9f-604d9268178a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EUYcm21P5n5nEWyiotvg8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 80112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 852
      },
      "output_tokens": 66,
      "service_tier": "standard",
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

_source line 96 · 2026-05-24T19:30:54.789Z_

<details><summary>↩ Tool result · `toolu_019pDLFR5fdBVpsteJxAqrvy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 44, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed44.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "d563fbf6-5ca1-4cbf-a3ca-80f2569f91dc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 44, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed44.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\\\n[eval] Mode: vla_only, benchmark: object\\\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\\\nThe PI05 model is a direct port of the OpenPI implementation. \\\\nThis implementation follows the original OpenPI structure for compatibility. \\\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\\\n✓ Loaded state dict from model.safetensors\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 44, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_vla_only_pi05_seed44.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: vla_only, benchmark: object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 97_

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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "150b86af-73bd-4878-8760-24dcfdb9dd80",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DcKsG66XRBJyRNuLuVK2cH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2866,
      "cache_read_input_tokens": 80964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2866
      },
      "output_tokens": 56,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01WZprHvq9MoXqvhg5eT8uou`</summary>

```json
{
  "filters": {
    "model": "pi05",
    "benchmark": "object",
    "mode": "vla_only"
  },
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "*"
  ],
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "b28fc10b-8e01-4541-a41c-b7f00081f9bc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DcKsG66XRBJyRNuLuVK2cH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2866,
      "cache_read_input_tokens": 80964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2866
      },
      "output_tokens": 56,
      "service_tier": "standard",
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

_source line 99 · 2026-05-24T19:31:25.990Z_

<details><summary>↩ Tool result · `toolu_01WZprHvq9MoXqvhg5eT8uou`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8442}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "9bd16cde-eca5-4301-bd9c-63502e5eee77",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.8442}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8442}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 100_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01ThQ83RSnFCfhhYJWbaD1rm`</summary>

```json
{
  "filters": {},
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "exp_id",
    "metrics",
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
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "36409882-8f8c-42ed-a26d-c0c149425b00",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018T9jvokfx4QCiw8xqrubtj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1852,
      "cache_read_input_tokens": 83830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1852
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Large event (continued)

````text
### Tool result

_source line 101 · 2026-05-24T19:31:34.761Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01ThQ83RSnFCfhhYJWbaD1rm`&lt;/summary>

```text
Error: result (803,234 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/a712f88f-e229-4c2a-912b-78963520492d/tool-results/mcp-agent-ml-research-read_registry-1779651094744.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/a712f88f-e229-4c2a-912b-78963520492d/tool-results/mcp-agent-ml-research-read_registry-1779651094744.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a712f88f-e229-4c2a-912b-78963520492d",
  "uuid": "c3ec62b3-657c-4ac6-9cdd-a1474cd9697b",
  "tool_use_result": {
    "content": "Error: result (803,234 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/a712f88f-e229-4c2a-912b-78963520492d/tool-results/mcp-agent-ml-research-read_registry-1779651094744.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/a712f88f-e229-4c2a-912b-78963520492d/tool-results/mcp-agent-ml-research-read_registry-1779651094744.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"train-crm-pi05-unified-3suite-r2\": {\"spec\": {\"command\": \"python -u src/train_crm.py --benchmark object spatial goal --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ --obs_dim 2048 --epochs 50 --batch_size 256 --lr 1e-3 --output_dir /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/\", \"server\": \"bjb1-18228\", \"gpu\": 0, \"pid\": 326310, \"model_name\": \"crm_pi05_unified_3suite\", \"obs_dim\": 2048, \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/\", \"data_breakdown\": {\"object\": 72507, \"spatial\": 60250, \"goal\": 61728}, \"seed\": 0, \"batch_size\": 256, \"epochs\": 50, \"lr\": 0.001, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-pi05-unified-3suite-r2.log\", \"tmux_session\": \"train-crm-pi05-unified-3suite-r2\", \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training job, not eval)\"}, \"metrics\": {\"current_epoch\": 25, \"total_epochs\": 50, \"best_val_loss\": 0.004854, \"best_epoch\": 24, \"train_loss_latest\": 0.00844, \"progress_pct\": 50}}, \"eval-supp-obj-vla-only-s50\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --seed 50 --n_rollouts 20 2>&1 | tee logs/eval-supp-obj-vla-only-s50.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"356733\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-obj-vla-only-s50.log\", \"submitted_at\": \"2026-05-24T16:18:58.101Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (10 tasks × 20 rollouts)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 50, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"wall_clock_seconds\": 11298.0, \"gpu_hours\": 3.14}, \"metrics\": {\"overall_success_rate\": 0.74, \"successes\": 148, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"object\", \"seed\": 50, \"mode\": \"vla_only\", \"model\": \"pi05\"}}, \"eval-supp-spatial-vla-only-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-supp-spatial-vla-only-s42.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"356458\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-spatial-vla-only-s42.log\", \"submitted_at\": \"2026-05-24T16:18:52.189Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial (10 tasks × 20 rollouts)\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_path\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"wall_clock_seconds\": 11293.8, \"gpu_hours\": 3.14}, \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"spatial\", \"seed\": 42, \"mode\": \"vla_only\", \"model\": \"pi05\"}}, \"eval-supp-adapt-tau025-obj-s49\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 49 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-adapt-tau025-obj-s49.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"304327\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s49.log\", \"submitted_at\": \"2026-05-24T15:36:49.163Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_sr\": 0.74, \"trigger_rate\": 0.0417, \"mean_uncertainty\": 0.1131, \"per_task_sr\": {\"soup\": 0.7, \"cream_cheese\": 0.65, \"salad\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.75, \"tomato\": 0.75, \"butter\": 0.6, \"milk\": 0.6, \"pudding\": 0.8, \"oj\": 0.95}}}, \"eval-supp-adapt-tau025-obj-s48\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 48 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-adapt-tau025-obj-s48.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"302994\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s48.log\", \"submitted_at\": \"2026-05-24T15:36:42.973Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_sr\": 0.76, \"trigger_rate\": 0.0389, \"mean_uncertainty\": 0.1117, \"per_task_sr\": {\"soup\": 0.75, \"cream_cheese\": 0.75, \"salad\": 0.7, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.6, \"milk\": 0.8, \"pudding\": 0.7, \"oj\": 0.95}}}, \"eval-supp-vla-only-obj-s49\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --seed 49 --n_rollouts 20 2>&1 | tee logs/eval-supp-vla-only-obj-s49.log\\\"\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"pid\": \"942933\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-vla-only-obj-s49.log\", \"submitted_at\": \"2026-05-24T15:38:56.078Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_sr\": 0.755, \"per_task_sr\": {\"soup\": 0.55, \"cream_cheese\": 0.7, \"salad\": 0.8, \"bbq\": 0.95, \"ketchup\": 0.8, \"tomato\": 0.8, \"butter\": 0.6, \"milk\": 0.65, \"pudding\": 0.8, \"oj\": 0.9}}}, \"eval-supp-vla-only-obj-s48\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --seed 48 --n_rollouts 20 2>&1 | tee logs/eval-supp-vla-only-obj-s48.log\\\"\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"pid\": \"942179\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-vla-only-obj-s48.log\", \"submitted_at\": \"2026-05-24T15:38:50.023Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_sr\": 0.79, \"per_task_sr\": {\"soup\": 0.65, \"cream_cheese\": 0.8, \"salad\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.85, \"tomato\": 0.8, \"butter\": 0.65, \"milk\": 0.8, \"pudding\": 0.75, \"oj\": 0.95}}}, \"eval-supp-vla-only-goal-s49\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark goal --seed 49 --n_rollouts 20 2>&1 | tee logs/eval-supp-vla-only-goal-s49.log\\\"\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"pid\": \"941522\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-vla-only-goal-s49.log\", \"submitted_at\": \"2026-05-24T15:38:44.019Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_sr\": 0.82, \"per_task_sr\": {\"middle_drawer\": 0.75, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.65, \"bowl_cabinet\": 0.95, \"push_plate\": 0.85, \"cream_cheese\": 0.55, \"stove_on\": 1, \"bowl_plate\": 0.85, \"wine_rack\": 0.8}}}, \"eval-supp-vla-only-goal-s48\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark goal --seed 48 --n_rollouts 20 2>&1 | tee logs/eval-supp-vla-only-goal-s48.log\\\"\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"pid\": \"941247\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-vla-only-goal-s48.log\", \"submitted_at\": \"2026-05-24T15:38:38.015Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_sr\": 0.85, \"per_task_sr\": {\"middle_drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.9, \"drawer_bowl\": 0.55, \"bowl_cabinet\": 1, \"push_plate\": 0.9, \"cream_cheese\": 0.6, \"stove_on\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}}, \"eval-supp-vla-only-spatial-s49\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20 2>&1 | tee logs/eval-supp-vla-only-spatial-s49.log\\\"\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"pid\": \"940972\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-vla-only-spatial-s49.log\", \"submitted_at\": \"2026-05-24T15:38:31.390Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_sr\": 0.785, \"per_task_sr\": {\"between\": 0.9, \"next_ramekin\": 0.95, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.7, \"on_ramekin\": 0, \"next_cookie\": 0.9, \"stove\": 0.8, \"next_plate\": 0.75, \"cabinet\": 0.95}}}, \"eval-supp-vla-only-spatial-s48\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20 2>&1 | tee logs/eval-supp-vla-only-spatial-s48.log\\\"\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"940684\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-vla-only-spatial-s48.log\", \"submitted_at\": \"2026-05-24T15:38:24.960Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_sr\": 0.795, \"per_task_sr\": {\"between\": 1, \"next_ramekin\": 0.9, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.8, \"on_ramekin\": 0, \"next_cookie\": 0.95, \"stove\": 0.75, \"next_plate\": 0.85, \"cabinet\": 0.8}}}, \"eval-pi05-reconvla-spatial-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode reconvla --benchmark spatial --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-pi05-reconvla-spatial-s42.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"395002\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-reconvla-spatial-s42.log\", \"submitted_at\": \"2026-05-24T18:25:02.706Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-reconvla-object-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode reconvla --benchmark object --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-pi05-reconvla-object-s42.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"394188\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-reconvla-object-s42.log\", \"submitted_at\": \"2026-05-24T18:24:31.210Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-reconvla-goal-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode reconvla --benchmark goal --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-pi05-reconvla-goal-s42.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"393784\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-reconvla-goal-s42.log\", \"submitted_at\": \"2026-05-24T18:24:24.145Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-object-s43-v2\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 2>&1 | tee logs/eval-pi05-vla-only-object-s43-v2.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"393309\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s43-v2.log\", \"submitted_at\": \"2026-05-24T18:24:15.755Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-object-s42-v2\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-pi05-vla-only-object-s42-v2.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"583769\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s42-v2.log\", \"submitted_at\": \"2026-05-24T18:22:06.993Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-goal-s43-v2\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 43 --n_rollouts 20 2>&1 | tee logs/eval-pi05-vla-only-goal-s43-v2.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"583098\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-s43-v2.log\", \"submitted_at\": \"2026-05-24T18:22:00.922Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-goal-s42-v2\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-pi05-vla-only-goal-s42-v2.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"582430\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-s42-v2.log\", \"submitted_at\": \"2026-05-24T18:21:54.737Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-spatial-s43-v2\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 2>&1 | tee logs/eval-pi05-vla-only-spatial-s43-v2.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"581958\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-s43-v2.log\", \"submitted_at\": \"2026-05-24T18:21:48.585Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-spatial-s42-v2\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-pi05-vla-only-spatial-s42-v2.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"581363\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-s42-v2.log\", \"submitted_at\": \"2026-05-24T18:21:42.352Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-object-s43\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 2>&1 | tee logs/eval-pi05-vla-only-object-s43.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"388306\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s43.log\", \"submitted_at\": \"2026-05-24T18:18:30.109Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-object-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-pi05-vla-only-object-s42.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"574940\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s42.log\", \"submitted_at\": \"2026-05-24T18:18:23.857Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-goal-s43\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 43 --n_rollouts 20 2>&1 | tee logs/eval-pi05-vla-only-goal-s43.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"574597\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-s43.log\", \"submitted_at\": \"2026-05-24T18:18:17.275Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-goal-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-pi05-vla-only-goal-s42.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"574188\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-s42.log\", \"submitted_at\": \"2026-05-24T18:18:09.640Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-spatial-s43\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 2>&1 | tee logs/eval-pi05-vla-only-spatial-s43.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"573908\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-s43.log\", \"submitted_at\": \"2026-05-24T18:18:00.844Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-spatial-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-pi05-vla-only-spatial-s42.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"573629\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-s42.log\", \"submitted_at\": \"2026-05-24T18:17:54.298Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-supp-adapt-tau025-goal-s49\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 49 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-adapt-tau025-goal-s49.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"301553\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-goal-s49.log\", \"submitted_at\": \"2026-05-24T15:36:34.065Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_success_rate\": 0.815, \"trigger_rate\": 0.089, \"tau\": 0.25, \"benchmark\": \"goal\", \"seed\": 49}}, \"eval-supp-adapt-tau025-goal-s48\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 48 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-adapt-tau025-goal-s48.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"300823\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-goal-s48.log\", \"submitted_at\": \"2026-05-24T15:36:27.474Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_success_rate\": 0.845, \"trigger_rate\": 0.089, \"tau\": 0.25, \"benchmark\": \"goal\", \"seed\": 48}}, \"eval-supp-adapt-tau025-spatial-s49\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark spatial --seed 49 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-adapt-tau025-spatial-s49.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"300212\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s49.log\", \"submitted_at\": \"2026-05-24T15:36:20.989Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_success_rate\": 0.82, \"trigger_rate\": 0.195, \"tau\": 0.25, \"benchmark\": \"spatial\", \"seed\": 49}}, \"eval-supp-adapt-tau025-spatial-s48\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark spatial --seed 48 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-adapt-tau025-spatial-s48.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"299935\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s48.log\", \"submitted_at\": \"2026-05-24T15:36:14.829Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_success_rate\": 0.81, \"trigger_rate\": 0.198, \"tau\": 0.25, \"benchmark\": \"spatial\", \"seed\": 48}}, \"eval-adaptive-k1-spatial-tau025-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --K 1 2>&1 | tee logs/eval-adaptive-k1-spatial-s42.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"488687\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k1-spatial-tau025-s42.log\", \"submitted_at\": \"2026-05-24T15:12:15.838Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_success_rate\": 0.795, \"trigger_rate\": 0.197, \"tau\": 0.25, \"K\": 1, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-crm-obj-s47-reeval\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt 2>&1 | tee logs/eval-crm-obj-s47-reeval.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"487954\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-obj-s47-reeval.log\", \"submitted_at\": \"2026-05-24T15:12:09.757Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_success_rate\": 0.825, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\", \"seed\": 47}}, \"eval-tau-sweep-spatial-tau030-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.30 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-tau030-spatial-s42.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"487354\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-tau-sweep-spatial-tau030-s42.log\", \"submitted_at\": \"2026-05-24T15:12:03.869Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_success_rate\": 0.805, \"trigger_rate\": 0.167, \"tau\": 0.3, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-tau-sweep-spatial-tau020-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.20 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-tau020-spatial-s42.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"487074\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-tau-sweep-spatial-tau020-s42.log\", \"submitted_at\": \"2026-05-24T15:11:57.916Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_success_rate\": 0.81, \"trigger_rate\": 0.266, \"tau\": 0.2, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-tau-sweep-spatial-tau010-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.10 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-tau010-spatial-s42.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"486799\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-tau-sweep-spatial-tau010-s42.log\", \"submitted_at\": \"2026-05-24T15:11:50.901Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_success_rate\": 0.79, \"trigger_rate\": 0.752, \"tau\": 0.1, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-supp-adapt-tau025-obj-s50\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 50 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-adapt-tau025-obj-s50.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"567056\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s50.log\", \"submitted_at\": \"2026-05-24T17:33:56.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-supp-long-adapt-tau025-s47-r2\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --adaptive_threshold 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO long benchmark\", \"data_count\": 200, \"model_name\": \"smolvla+crm_unified_4suite_r4\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO long n_rollouts=20\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-long-adapt-tau025-s47-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"tmux_session\": \"eval-supp-long-adapt-tau025-s47-r2\", \"pid\": 433348, \"gpu\": \"cuda:1\"}, \"metrics\": {\"overall_success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"trigger_rate\": 0.037, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-adaptive-k5-spatial-tau025-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --K 5 2>&1 | tee logs/eval-adaptive-k5-spatial-s42.log\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k5-spatial-tau025-s42.log\", \"submitted_at\": \"2026-05-24T16:55:41.165Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-supp-long-k2mean-s47-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\", \"tmux_session\": \"long-k2mean-s47\", \"log_path\": \"/tmp/eval_long_k2mean_s47.log\", \"gpu\": 5, \"pid\": 205647}, \"metrics\": {\"overall_success_rate\": 0.545, \"successes\": 109, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"note\": \"output saved as eval_long_vla_only_seed47.json (pre-M083 naming)\"}}, \"eval-supp-spatial-reconvla-s47\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb2-40593\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"gpu\": \"cuda:0\", \"pid\": 261844, \"tmux_session\": \"spatial-reconvla-s47\", \"log_path\": \"/tmp/eval_spatial_reconvla_s47.log\", \"checkpoint_path\": \"n/a-baseline\", \"result_json\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json\"}, \"metrics\": {\"overall_sr\": 0.78, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"total_rollouts\": 200, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.65, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.7}}}, \"eval-a1-baseline-object-s42\": {\"spec\": {\"command\": \"python eval_a1_baseline.py --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"a1-libero\", \"seed\": 42, \"checkpoint_source\": \"a1-official\", \"eval_data\": \"LIBERO-Object-10tasks-20trials\", \"checkpoint_path\": \"/root/autodl-tmp/A1/checkpoints/\", \"log_path\": \"/tmp/a1_eval.log\"}, \"metrics\": {\"overall_success_rate\": 0.565, \"total_successes\": 113, \"total_episodes\": 200, \"official_reported_sr\": 0.998, \"gap_vs_official\": -0.433, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.35, \"salad_dressing\": 0.35, \"bbq_sauce\": 0.8, \"ketchup\": 0.65, \"tomato_sauce\": 0.95, \"butter\": 0.65, \"milk\": 0.1, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.25}}}, \"eval-supp-long-vla-only-s47-r4\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO long benchmark\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"pretrained SmolVLA /root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO long, 10 tasks x 20 rollouts\", \"tmux_session\": \"long-vla-s47\", \"log_path\": \"/tmp/eval_long_vla_s47.log\", \"gpu\": 1, \"pid\": 307463}, \"metrics\": {\"success_rate\": 0.595, \"total_successes\": 119, \"total_trials\": 200}}, \"eval-supp-obj-k2mean-s47-r2\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb1-32546\", \"model_name\": \"SmolVLA\", \"seed\": 47, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"n/a-process-crashed-no-output\"}}, \"eval-supp-obj-adapt-tau025-s47-r2\": {\"spec\": {\"model_name\": \"SmolVLA\", \"command\": \"python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --adaptive_threshold 0.2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 47, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\"}, \"metrics\": {\"overall_success_rate\": 0.77, \"trigger_rate\": 0.0403, \"crm_applied_steps\": 1458}}, \"eval-supp-obj-crm-norm005-s47-r2\": {\"spec\": {\"model_name\": \"SmolVLA\", \"command\": \"python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"seed\": 47, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed47.json\"}, \"metrics\": {\"overall_success_rate\": 0.825}}, \"eval-supp-obj-vla-only-s47-r2\": {\"spec\": {\"model_name\": \"SmolVLA\", \"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --seed 47 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 47, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\"}, \"metrics\": {\"overall_success_rate\": 0.755}}, \"eval-supp-k2mean-spatial-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"spatial-k2mean-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}, \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"note\": \"Completed at 18:07 with SR=81.0% per log; JSON overwritten by vla-only K=1 run which wrote to same output_file (eval_spatial_vla_only_seed47.json). Per-task data recoverable from eval-supp-k2mean-spatial-s47.log on cqa1-32758. Recommend explicit --output_file for future k2mean runs.\"}}, \"eval-supp-spatial-vla-only-s47\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 2\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"gpu\": \"cuda:0\", \"pid\": 844299, \"tmux_session\": \"spatial-vla-s47\", \"log_path\": \"/tmp/eval_spatial_vla_s47.log\"}, \"metrics\": {\"success_rate\": 0.81, \"total_successes\": 162, \"total_trials\": 200, \"per_task_range\": \"0.0-1.0\", \"worst_task\": \"pick_up_black_bowl_on_ramekin (0/20)\", \"best_tasks\": \"from_table_center, on_cookie_box, next_to_cookie_box (20/20)\"}}, \"eval-supp-spatial-adapt-tau025-s47\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --adaptive_threshold 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"gpu\": \"cuda:2\", \"pid\": 844595, \"tmux_session\": \"spatial-adapt-s47\", \"log_path\": \"/tmp/eval_spatial_adapt_s47.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"metrics\": {\"success_rate\": 0.79, \"total_successes\": 158, \"total_trials\": 200, \"mean_uncertainty\": 0.1835, \"trigger_rate\": 0.188, \"tau\": 0.25, \"total_steps\": 28642, \"crm_applied_steps\": 5381}}, \"eval-supp-adapt-tau025-spatial-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"spatial-adapt-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Adaptive CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.815, \"successes\": 163, \"total\": 200, \"trigger_rate\": 0.2046, \"mean_uncertainty\": 0.1873, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-spatial-k2mean-s47\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"gpu\": \"cuda:3\", \"pid\": 845121, \"tmux_session\": \"spatial-k2mean-s47\", \"log_path\": \"/tmp/eval_spatial_k2mean_s47.log\"}, \"metrics\": {\"success_rate\": 0.82, \"total_successes\": 164, \"total_trials\": 200, \"note\": \"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\"}}, \"eval-supp-obj-reconvla-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark object --mode reconvla --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-reconvla\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"tmux_session\": \"obj-reconvla-s47\", \"log_path\": \"/tmp/eval_obj_reconvla_s47.log\", \"gpu\": 4, \"pid\": 200690, \"checkpoint_path\": \"n/a-reconvla\", \"result_json\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\"}, \"metrics\": {\"success_rate\": 0.765, \"total_successes\": 153, \"total_trials\": 200, \"per_task\": {\"alphabet_soup\": 0.75, \"cream_cheese\": 0.95, \"salad_dressing\": 0.7, \"bbq_sauce\": 0.95, \"ketchup\": 0.75, \"tomato_sauce\": 0.65, \"butter\": 0.5, \"milk\": 0.7, \"chocolate_pudding\": 0.75, \"orange_juice\": 0.95}}}, \"eval-supp-goal-k2mean-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-k2mean-s47\", \"log_path\": \"/tmp/eval_goal_k2mean_s47.log\", \"gpu\": 2, \"pid\": 205380}, \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 20}}, \"eval-supp-goal-adapt-tau025-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --adaptive_threshold 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-adapt-s47\", \"log_path\": \"/tmp/eval_goal_adapt_s47.log\", \"gpu\": 0, \"pid\": 205107}, \"metrics\": {\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"tau\": 0.25, \"trigger_rate\": 0.0887, \"mean_uncertainty\": 0.1476, \"total_steps\": 29241, \"crm_applied_steps\": 2594, \"n_rollouts\": 20}}, \"eval-supp-goal-crm-norm005-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-crm-s47\", \"log_path\": \"/tmp/eval_goal_crm_s47.log\", \"gpu\": 1, \"pid\": 199883}, \"metrics\": {\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"n_rollouts\": 20}}, \"eval-supp-reconvla-spatial-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"spatial-reconvla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Reconvla\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-reconvla\"}, \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-vla-only-spatial-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"spatial-vla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}, \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-long-reconvla-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-reconvla-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\"}, \"metrics\": {\"overall_success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-long-crm-norm005-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-crm-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.565, \"successes\": 113, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-goal-reconvla-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-reconvla\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-reconvla-s47\", \"log_path\": \"/tmp/eval_goal_reconvla_s47.log\", \"gpu\": 3, \"pid\": 200418}, \"metrics\": {\"overall_success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-k2mean-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"obj-k2mean-s47\", \"log_path\": \"/tmp/eval_obj_k2mean_s47.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}, \"metrics\": {\"overall_success_rate\": 0.775, \"successes\": 155, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-crm-norm005-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"obj-crm-s47\", \"log_path\": \"/tmp/eval_obj_crm_norm005_s47.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-adapt-tau025-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"obj-adapt-s47\", \"log_path\": \"/tmp/eval_obj_adapt_s47.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA+Adaptive CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.77, \"successes\": 154, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-vla-only-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"obj-vla-s47\", \"log_path\": \"/tmp/eval_obj_vla_only_s47.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}, \"metrics\": {\"overall_success_rate\": 0.755, \"successes\": 151, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-goal-vla-only-s47-r3\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO goal benchmark\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"pretrained SmolVLA /root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO goal, 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-vla-s47\", \"log_path\": \"/tmp/eval_goal_vla_s47.log\", \"gpu\": 2, \"pid\": 307664}, \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_goal_vla_only_seed47.json\"}}, \"eval-supp-long-k2mean-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-vla-s47\", \"log_path\": \"logs/eval-supp-long-vla-only-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"eval-supp-long-adapt-tau025-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-adapt-s47\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46-r2\"}}, \"eval-supp-spatial-crm-norm005-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 15194.9, \"gpu_hours\": 4.22}, \"metrics\": {\"overall_success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\"}}, \"eval-supp-long-crm-norm005-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 262247, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\", \"submitted_at\": \"2026-05-24T03:23:09.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"metrics\": {\"success_rate\": 0.54, \"successes\": 108, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"train-crm-pi05-unified-3suite\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark object spatial goal --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ --obs_dim 2048 --epochs 50 --batch_size 32 --lr 1e-3 --output_dir /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/\", \"server\": \"bjb1-18228\", \"gpu\": 0, \"pid\": 319672, \"model_name\": \"pi05\", \"obs_dim\": 2048, \"data_count\": 194485, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/{object,spatial,goal}/\", \"data_breakdown\": {\"object\": 72507, \"spatial\": 60250, \"goal\": 61728}, \"seed\": 42, \"script\": \"src/train_crm.py\", \"tmux_session\": \"crm-pi05-unified\", \"log_path\": \"/tmp/train_crm_pi05_unified_3suite.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/\", \"cache_dir\": \"/root/autodl-tmp/crm_cache_pi05_2048/\", \"epochs\": 50, \"batch_size\": 32, \"lr\": 0.001}}, \"precompute-pi05-object-2048-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 113456, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/object/\", \"data_count\": 72507, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_object_2048.log\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/object/\"}, \"metrics\": {\"n_samples\": 72507, \"K\": 10, \"obs_dim\": 2048, \"action_dim\": 6, \"h_eff\": 5}}, \"eval-openvla-object-vla-only-seed42-v3\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u src/openvla_eval.py --benchmark object --model_path /root/autodl-tmp/models/openvla-libero-object --mode vla_only --seed 42 --n_rollouts 20 --gpu 0 --output_file logs/eval_openvla_object_vla_only_seed42_v3.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object\", \"data_count\": 200, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts = 200 episodes)\", \"pid\": \"114984\", \"log_path\": \"/tmp/eval_openvla_vla_only_seed42_v3.log\", \"checkpoint_path\": \"/root/autodl-tmp/models/openvla-libero-object\"}}, \"eval-supp-vla-only-spatial-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s46\", \"gpu\": 5, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-vla-only-spatial-s46.log\", \"result_json\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json\"}, \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200}}, \"eval-supp-adapt-tau025-spatial-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm-adaptive\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"adaptive_conformal_crm\", \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 10, \"tmux_session\": \"eval-supp-adapt-tau025-spatial-s45\", \"gpu\": 4, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-spatial-s45.log\", \"result_json\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\"}, \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"mean_uncertainty\": 0.1885, \"trigger_rate\": 0.2013, \"tau\": 0.25, \"total_steps\": 28599, \"crm_applied_steps\": 5758}}, \"eval-supp-crm-norm005-spatial-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10, \"tmux_session\": \"eval-supp-crm-norm005-spatial-s45\", \"gpu\": 3, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm005-spatial-s45.log\", \"result_json\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed45.json\"}, \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200}}, \"eval-supp-vla-only-spatial-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s45\", \"gpu\": 2, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-vla-only-spatial-s45.log\", \"result_json\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\"}, \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-supp-crm-norm005-spatial-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 20 rollouts\", \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm005-spatial-s46.log\", \"result_json\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed46.json\"}, \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200}}, \"train-crm-pi05-spatial-k1\": {\"metrics\": {\"best_val_loss\": 0.002887, \"best_epoch\": 50, \"final_train_loss\": 0.018836}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_crm_k1.py --benchmark spatial --reuse_merged_cache --merged_cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ --obs_dim 2048 --output_dir /root/autodl-tmp/checkpoints/crm_pi05_k1_multiscale/spatial/ --epochs 50 --lr 1e-3 --batch_size 256 --no_wandb\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/spatial/\", \"data_count\": 60250, \"model_name\": \"pi05-MultiScaleCRM-k1\", \"seed\": 42, \"tmux_session\": \"crm-pi05-spatial\", \"log_path\": \"/tmp/train_crm_pi05_spatial.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_k1_multiscale/spatial/\", \"gpu\": 1, \"obs_dim\": 2048, \"action_dim\": 6, \"h_eff\": 5, \"batch_size\": 256, \"epochs\": 50}}, \"train-crm-pi05-goal-k1\": {\"metrics\": {\"best_val_loss\": 0.003319, \"best_epoch\": 48, \"final_train_loss\": 0.018992}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/train_crm_k1.py --benchmark goal --reuse_merged_cache --merged_cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ --obs_dim 2048 --output_dir /root/autodl-tmp/checkpoints/crm_pi05_k1_multiscale/goal/ --epochs 50 --lr 1e-3 --batch_size 256 --no_wandb\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/goal/\", \"data_count\": 61728, \"model_name\": \"pi05-MultiScaleCRM-k1\", \"seed\": 42, \"tmux_session\": \"crm-pi05-goal\", \"log_path\": \"/tmp/train_crm_pi05_goal.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_k1_multiscale/goal/\", \"gpu\": 2, \"obs_dim\": 2048, \"action_dim\": 6, \"h_eff\": 5, \"batch_size\": 256, \"epochs\": 50}}, \"eval-supp-goal-vla-only-s47-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO goal benchmark\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"pretrained SmolVLA /root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO goal, 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-vla-s47-r2\", \"log_path\": \"/tmp/eval_goal_vla_only_s47_r2.log\", \"gpu\": 2}}, \"eval-supp-long-vla-only-s47-r3\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO long benchmark\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"pretrained SmolVLA /root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO long, 10 tasks x 20 rollouts\", \"tmux_session\": \"long-vla-s47-r3\", \"log_path\": \"/tmp/eval_long_vla_only_s47_r3.log\", \"gpu\": 1}}, \"eval-supp-long-vla-only-s47-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 278846, \"tmux_session\": \"long-vla-s47-r2\", \"log_path\": \"logs/eval-supp-long-vla-only-s47-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-goal-vla-only-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 279117, \"tmux_session\": \"goal-vla-s47\", \"log_path\": \"logs/eval-supp-goal-vla-only-s47.log\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-long-reconvla-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": 262529, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s46.log\", \"submitted_at\": \"2026-05-24T03:23:15.265Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"metrics\": {\"success_rate\": 0.56, \"successes\": 112, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-k2mean-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 263191, \"log_path\": \"logs/eval_long_k2mean_seed46.json\", \"submitted_at\": \"2026-05-24T03:23:22.142Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\"}, \"metrics\": {\"success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-adapt-tau025-spatial-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial suite\", \"data_count\": 200, \"model_name\": \"SmolVLA + Adaptive CRM (crm_smolvla_3suite_v1)\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 20 rollouts\"}}, \"eval-supp-long-adapt-tau025-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 261974, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-adapt-tau025-s46.log\", \"submitted_at\": \"2026-05-24T03:23:03.745Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"wall_clock_seconds\": 16917.4, \"gpu_hours\": 4.7}, \"metrics\": {\"overall_success_rate\": 0.585, \"successes\": 117, \"total_rollouts\": 200, \"benchmark\": \"long\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 46, \"K\": 2, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25}}, \"crm-train-openvla-k1-multiscale-object\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm_k1.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_k1_openvla --obs_dim 4096 --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --output_dir /root/autodl-tmp/checkpoints/crm_openvla_k1_multiscale/object --wandb_run_name crm-openvla-k1-multiscale-object --loss_mode multi\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/crm_cache_k1_openvla/object\", \"data_count\": 74507, \"model_name\": \"MultiScaleCRM-OpenVLA-K1\", \"seed\": 42}, \"metrics\": {\"best_val_loss\": 0.077477, \"total_epochs\": 50, \"train_samples\": 74507, \"obs_dim\": 4096, \"params\": 908106, \"architecture\": \"MultiScaleCRM-K1\"}}, \"eval-supp-long-k2mean-s46-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"long-k2mean-s46-r2\", \"log_path\": \"logs/eval-supp-long-k2mean-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-k2mean-s46\"}}, \"eval-supp-long-reconvla-s46-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"long-reconvla-s46-r2\", \"log_path\": \"logs/eval-supp-long-reconvla-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\", \"parent\": \"eval-supp-long-reconvla-s46\"}}, \"eval-supp-long-crm-norm005-s46-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"long-crm-s46-r2\", \"log_path\": \"logs/eval-supp-long-crm-norm005-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-crm-norm005-s46\"}}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"long-adapt-s46-r2\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46\"}}, \"eval-supp-obj-crm-norm005-s45\": {\"metrics\": {\"success_rate\": 0.765, \"successes\": 153, \"total\": 200, \"source\": \"json_harvest_bjb2-40593\", \"json_file\": \"eval_object_crm_obs_only_norm0.05_seed45.json\"}, \"spec\": {\"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"eval_object_crm_obs_only_norm0.05_seed45.json\", \"command\": \"duplicate entry fix\", \"server\": \"bjb2-40593\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 45, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-supp-obj-adapt-tau025-s45\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"eval-obj-adapt-s45\", \"log_path\": \"/tmp/eval_obj_adapt_s45.log\", \"seed\": 45, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-supp-obj-vla-only-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark object --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": 849667, \"tmux_session\": \"eval-supp-obj-vla-only-s45\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-obj-vla-only-s45.log\", \"seed\": 45, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA\"}, \"metrics\": {\"SR\": 0.76}}, \"eval-supp-spatial-crm-norm005-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:3\", \"seed\": 45, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_spatial_crm_s45.log\"}, \"metrics\": {\"SR\": 0.78, \"successes\": 156, \"total\": 200, \"per_task\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.7}}}, \"eval-supp-spatial-vla-only-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:1\", \"seed\": 45, \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"log_path\": \"/tmp/eval_spatial_vla_s45.log\"}, \"metrics\": {\"SR\": 0.77, \"successes\": 154, \"total\": 200}}, \"precompute-pi05-long-2048-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}, \"precompute-pi05-goal-2048-r2\": {\"spec\": {\"command\": \"python -u src/train_crm.py --precompute --model pi05 --benchmark goal --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/goal/\", \"data_count\": 61728, \"model_name\": \"pi0.5\", \"seed\": 0}}, \"eval-supp-long-vla-only-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:3\", \"seed\": 46, \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"log_path\": \"/tmp/eval_long_vla_s46.log\", \"pid\": 601530, \"tmux_session\": \"eval-long-vla-s46\", \"checkpoint_path\": \"n/a-eval-only\"}, \"metrics\": {\"success_rate\": 60.5, \"successes\": 121, \"total\": 200, \"source\": \"reviewer_manual_check\"}}, \"precompute-pi05-spatial-2048-r2\": {\"spec\": {\"command\": \"python precompute_cache.py --model pi05 --suite spatial --K 2048\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/spatial/\", \"data_count\": 60250, \"model_name\": \"pi0.5\", \"seed\": 0}}, \"precompute-smolvla-goal-bjb1-32546\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python src/train_crm.py --precompute --benchmark goal --K 10 --cache_dir /root/autodl-tmp/crm_cache_v5/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"260139\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-smolvla-goal-bjb1-32546.log\", \"submitted_at\": \"2026-05-22T06:36:52.793Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 169630.6, \"gpu_hours\": 47.12}}, \"eval-supp-goal-vla-only-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": \"991460\", \"log_path\": \"/tmp/eval_goal_vla_s46.log\", \"submitted_at\": \"2026-05-23T23:03:11.586Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 46, \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"tmux_session\": \"eval-supp-goal-vla-only-s46\", \"checkpoint_source\": \"n/a\", \"checkpoint_path\": \"n/a-eval-only\", \"wall_clock_seconds\": 24021.1, \"gpu_hours\": 6.67}, \"metrics\": {\"success_rate\": 0.83, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-reconvla-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": \"992062\", \"log_path\": \"/tmp/eval_goal_reconvla_s46.log\", \"submitted_at\": \"2026-05-23T23:03:22.963Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 46, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"tmux_session\": \"eval-supp-goal-reconvla-s46\", \"checkpoint_path\": \"n/a-eval-only\", \"wall_clock_seconds\": 24003.5, \"gpu_hours\": 6.67}, \"metrics\": {\"success_rate\": 0.79, \"source\": \"json_harvest_bjb2-28827\"}}, \"crm-train-pi05-spatial-full\": {\"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_pi05/ --output_dir /root/autodl-tmp/checkpoints/crm_pi05_full/spatial/ --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 2048\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_pi05/spatial/\", \"data_count\": 60250, \"model_name\": \"CRM-spatial\", \"seed\": 42, \"gpu\": \"cuda:1\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-pi05-spatial-full.log\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/\"}, \"metrics\": {\"best_val_loss\": 0.006138, \"epochs_completed\": 50, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/\"}}, \"eval-obs-only-spatial-v2\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"203968\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v2.log\", \"submitted_at\": \"2026-05-14T12:43:42.188Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features tests whether per-DOF conformal intervals are necessary for effective correction\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"parent\": \"crm-train-v2-obs-only\", \"failure_reason\": \"Bug: evaluate.py line 266 CRM load condition missing crm_obs_only, CRM was None throughout eval, all rollouts 0%. Replaced by eval-obs-only-spatial-v3.\", \"wall_clock_seconds\": 185.5, \"gpu_hours\": 0.05}, \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 100}}, \"eval-perdof-object-norm003-seed44\": {\"spec\": {\"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"853859\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed44.log\", \"submitted_at\": \"2026-05-18T13:31:56.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"success_rate\": 11, \"successes\": 11, \"total\": 100}}, \"eval-random-selection-spatial-seed42\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 42 --n_rollouts 10 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"346791\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed42.log\", \"submitted_at\": \"2026-05-20T10:51:06.018Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"random_selection_baseline\", \"seed\": 42, \"wall_clock_seconds\": 3442.7, \"gpu_hours\": 0.96}, \"metrics\": {\"success_rate\": 34, \"successes\": 34, \"total\": 100}}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": 975409, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-adaptive-k-spatial-p90-seed44-bjb2.log\", \"submitted_at\": \"2026-05-20T13:50:48.545Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"model_name\": \"CRM_obs_only_adaptive_k\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 55922.2, \"gpu_hours\": 15.53}, \"metrics\": {\"success_rate\": 36, \"successes\": 36, \"total\": 100, \"fast_path\": 81.5, \"avg_k\": 3.5, \"mean_l2\": 0.0885}}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"906142\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s44.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"wall_clock_seconds\": 10078.6, \"gpu_hours\": 2.8}, \"metrics\": {\"success_rate\": 82, \"successes\": 164, \"total\": 200}}, \"eval-supp-long-reconvla-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"seed\": 45, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"crm_unified_4suite_r4/crm_best.pt\", \"log_path\": \"/tmp/eval_long_reconvla_s45.log\"}, \"metrics\": {\"success_rate\": 59, \"successes\": 118, \"total\": 200}}, \"eval-supp-spatial-k2mean-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_spatial_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"seed\": 46, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"log_path\": \"/tmp/eval_spatial_k2mean_s46.log\", \"checkpoint_source\": \"n/a\", \"checkpoint_path\": \"n/a-eval-only\"}, \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-obj-crm-norm005-s46\": {\"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}, \"eval-pi05-vla-only-long-seed42-r4\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode vla_only --model pi05 --benchmark long --seed 42 --n_rollouts 20 --K 10 --n_action_steps 10 --max_steps 520 --output_file logs/eval_long_vla_only_seed42_r4.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"67669\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-long-seed42-r4.log\", \"submitted_at\": \"2026-05-22T15:52:57.803Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4052.5, \"gpu_hours\": 1.13}, \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 200}}, \"eval-supp-reconvla-obj-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"seed\": 45, \"model_name\": \"smolvla+crm\", \"data_path\": \"libero_object\", \"data_count\": 20, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"logs/eval-reconvla-obj-s45.log\", \"checkpoint_path\": \"n/a-eval-only\", \"eval_data\": \"libero_object\"}, \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}, \"eval-pi05-vla-only-object-seed42\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 42 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"982849\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42.log\", \"submitted_at\": \"2026-05-21T10:18:26.307Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5205.3, \"gpu_hours\": 1.45}, \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-pi05-vla-only-object-seed43\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 43 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"983128\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43.log\", \"submitted_at\": \"2026-05-21T10:18:36.208Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5206.7, \"gpu_hours\": 1.45}, \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-pi05-vla-only-object-seed44\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 44 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"983472\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44.log\", \"submitted_at\": \"2026-05-21T10:18:46.979Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5204.2, \"gpu_hours\": 1.45}, \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-long-k2mean-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 45 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:4\", \"seed\": 45, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"log_path\": \"/tmp/eval_long_k2mean_s45.log\", \"pid\": 924226}, \"metrics\": {\"success_rate\": 0.56, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-k2mean-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_goal_k2mean_seed46.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:1\", \"seed\": 46, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"log_path\": \"/tmp/eval_goal_k2mean_s46.log\", \"tmux_session\": \"eval-goal-k2mean-s46\", \"checkpoint_source\": \"n/a\", \"checkpoint_path\": \"n/a-eval-only\"}, \"metrics\": {\"success_rate\": 0.825, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-adapt-tau025-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": \"unknown\", \"log_path\": \"/tmp/eval_goal_adapt_s46.log\", \"submitted_at\": \"2026-05-23T23:03:32.801Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 46, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"tmux_session\": \"eval-goal-adapt-s46\", \"checkpoint_path\": \"n/a-eval-only\", \"wall_clock_seconds\": 9126.9, \"gpu_hours\": 2.54}, \"metrics\": {\"success_rate\": 0.835, \"trigger_rate\": 0.0909, \"tau\": 0.25, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-crm-norm005-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_goal_crm_s46.log\", \"tmux_session\": \"eval-goal-crm-s46\", \"checkpoint_path\": \"n/a-eval-only\"}, \"metrics\": {\"success_rate\": 0.82, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:4\", \"seed\": 45, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log\", \"pid\": \"502821\", \"tmux_session\": \"eval-supp-spatial-adapt-tau025-s45\"}, \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 20, \"mean_unc\": 0.1863}}, \"eval-supp-spatial-k2mean-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 45 --n_rollouts 20 --output_file logs/eval_spatial_k2mean_seed45.json\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"seed\": 45, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"log_path\": \"/tmp/eval_spatial_k2mean_s45.log\", \"pid\": \"204339\", \"tmux_session\": \"eval-spatial-k2mean-s45\"}, \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-vla-only-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:1\", \"seed\": 46, \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"log_path\": \"/tmp/eval_spatial_vla_s46.log\", \"pid\": 604290, \"tmux_session\": \"eval-spatial-vla-s46\", \"checkpoint_path\": \"n/a-eval-only\"}, \"metrics\": {\"success_rate\": 80.5, \"successes\": 161, \"total\": 200}}, \"eval-supp-spatial-reconvla-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:5\", \"seed\": 46, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_spatial_reconvla_s46.log\", \"pid\": 588065, \"tmux_session\": \"eval-spatial-reconvla-s46\", \"checkpoint_path\": \"n/a-eval-only\"}, \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-adapt-tau025-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:2\", \"seed\": 46, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_spatial_adapt_s46.log\", \"pid\": \"560487\", \"tmux_session\": \"eval-spatial-adapt-s46\", \"checkpoint_path\": \"n/a-eval-only\"}, \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 19.9, \"mean_unc\": 0.1846}}, \"eval-supp-spatial-crm-norm005-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_spatial_crm_s46.log\", \"pid\": \"590633\", \"tmux_session\": \"eval-spatial-crm-s46\", \"checkpoint_path\": \"n/a-eval-only\"}, \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}}, \"eval-supp-long-crm-norm005-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 45 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"seed\": 45, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"crm_unified_4suite_r4/crm_best.pt\", \"log_path\": \"/tmp/eval_long_crm_s45.log\"}, \"metrics\": {\"SR\": 0.605, \"successes\": 121, \"total\": 200}}, \"eval-supp-long-adapt-tau025-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"seed\": 45, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"crm_unified_4suite_r4/crm_best.pt\", \"log_path\": \"/tmp/eval_long_adapt_s45.log\"}, \"metrics\": {\"SR\": 0.6, \"successes\": 120, \"total\": 200}}, \"eval-supp-long-vla-only-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"seed\": 45, \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"log_path\": \"/tmp/eval_long_vla_s45.log\"}, \"metrics\": {\"SR\": 0.575, \"successes\": 115, \"total\": 200}}, \"eval-supp-spatial-reconvla-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:5\", \"seed\": 45, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_spatial_reconvla_s45.log\"}, \"metrics\": {\"success_rate\": 79.5, \"successes\": 159, \"total\": 200}}, \"eval-supp-goal-k2mean-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --K 2 --seed 45 --n_rollouts 20 --output_file logs/eval_goal_k2mean_seed45.json\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"seed\": 45, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"log_path\": \"/tmp/eval_goal_k2mean_s45.log\", \"checkpoint_path\": \"n/a-eval-only\"}, \"metrics\": {\"SR\": 0.81, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.6, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.55, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-supp-adapt-tau025-obj-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 849131, \"tmux_session\": \"eval-supp-adapt-tau025-obj-s45\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s45.log\", \"seed\": 45, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"metrics\": {\"SR\": 0.78}}, \"eval-supp-obj-k2mean-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --seed 45 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:2\", \"seed\": 45, \"model_name\": \"smolvla\", \"data_path\": \"libero_object\", \"data_count\": 20, \"log_path\": \"logs/eval-obj-k2mean-s45.log\", \"checkpoint_path\": \"n/a-eval-only\", \"eval_data\": \"libero_object\"}}, \"eval-supp-crm-obj-s46\": {\"metrics\": {\"overall_sr\": 0.795, \"per_task\": {\"alphabet_soup\": 0.8, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.7, \"tomato_sauce\": 0.75, \"butter\": 0.75, \"milk\": 0.85, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.9}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_crm_obj_s46.log\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-spatial-adapt-tau025-s45\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:4\", \"seed\": 45, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log\", \"pid\": \"502821\", \"tmux_session\": \"eval-supp-spatial-adapt-tau025-s45\"}}, \"eval-supp-long-k2mean-s44\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --seed 44 --n_rollouts 20 --K 2 --baseline_mode mean\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": 850410, \"tmux_session\": \"eval-supp-long-k2mean-s44\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-k2mean-s44.log\", \"seed\": 44, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA-K2mean\"}, \"metrics\": {\"SR\": 0.545, \"successes\": 109, \"total\": 200}}, \"eval-supp-long-reconvla-s44\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode reconvla --seed 44 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": 849677, \"tmux_session\": \"eval-supp-long-reconvla-s44\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s44.log\", \"seed\": 44, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla-reconvla-k10\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO Long benchmark\"}, \"metrics\": {\"SR\": 0.57, \"successes\": 114, \"total\": 200}}, \"eval-supp-k2mean-spatial-s45\": {}, \"eval-supp-goal-reconvla-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"seed\": 45, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_goal_reconvla_s45.log\"}, \"metrics\": {\"SR\": 0.855}}, \"eval-supp-goal-vla-only-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"seed\": 45, \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"log_path\": \"/tmp/eval_goal_vla_s45.log\"}, \"metrics\": {\"SR\": 0.835}}, \"eval-supp-crm-norm005-obj-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_crm_obj_s46.log\"}, \"metrics\": {\"SR\": 0.795}}, \"eval-supp-goal-crm-norm005-s45\": {\"spec\": {\"checkpoint_path\": \"logs/eval_goal_crm_obs_only_norm0.05_seed45.json\", \"log_path\": \"/tmp/eval_goal_crm_s45.log\"}, \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}}, \"eval-supp-crm-norm005-obj-s45\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 45 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"seed\": 45, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_crm_obj_s45.log\"}, \"metrics\": {\"SR\": 0.765}}, \"eval-supp-reconvla-obj-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:2\", \"seed\": 46, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_reconvla_obj_s46.log\"}, \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-supp-goal-adapt-tau025-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"seed\": 45, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_goal_adapt_s45.log\"}, \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.094, \"mean_unc\": 0.1493}}, \"eval-supp-long-crm-norm005-s44\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 44 --n_rollouts 20 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt --K 10\", \"server\": \"cqa1-32758\", \"gpu\": 5, \"pid\": 291523, \"tmux_session\": \"eval-supp-long-crm-norm005-s44\", \"seed\": 44, \"model_name\": \"smolvla+crm_unified_4suite_r4\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO long suite\", \"data_path\": \"LIBERO long suite (10 tasks)\", \"data_count\": 200}, \"metrics\": {\"SR\": 0.565}}, \"eval-supp-long-adapt-tau025-s44\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": 1, \"pid\": 291315, \"tmux_session\": \"eval-supp-long-adapt-tau025-s44\", \"seed\": 44, \"model_name\": \"smolvla+crm_unified_4suite_r4\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO long suite\", \"data_path\": \"LIBERO long suite (10 tasks)\", \"data_count\": 200}, \"metrics\": {\"SR\": 0.56, \"trigger_rate\": 0.049}}, \"eval-supp-k2mean-obj-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:3\", \"seed\": 46, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/tmp/eval_k2mean_obj_s46.log\"}, \"metrics\": {\"SR\": 0.765}}, \"eval-supp-k2mean-obj-s45\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --seed 45 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"seed\": 45, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/tmp/eval_k2mean_obj_s45.log\"}, \"metrics\": {\"SR\": 0.775}}, \"eval-supp-adapt-tau025-obj-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": 849395, \"tmux_session\": \"eval-supp-adapt-tau025-obj-s46\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s46.log\", \"seed\": 46, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"metrics\": {\"SR\": 0.775}}, \"eval-supp-long-vla-only-s43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode vla_only --seed 43 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": 849946, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-vla-only-s43.log\", \"submitted_at\": \"2026-05-23T11:56:02.350Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"tmux_session\": \"eval-supp-long-vla-only-s43\", \"seed\": 43, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"wall_clock_seconds\": 30301.7, \"gpu_hours\": 8.42}}, \"eval-supp-long-k2mean-s42\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark long --n_rollouts 20 --seed 42\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"pid\": \"172246\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-k2mean-s42.log\", \"submitted_at\": \"2026-05-23T11:23:16.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"hypothesis\": \"K=2 mean baseline on LIBERO-Long seed42. Isolates multi-sample averaging effect on long-horizon tasks. Long VLA-only s42 running on bjb1-32546 provides baseline comparison.\", \"wall_clock_seconds\": 31794.0, \"gpu_hours\": 8.83}, \"metrics\": {\"SR\": 0.57}}, \"eval-supp-obj-vla-only-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --benchmark object --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"smolvla\", \"gpu\": \"cuda:0\", \"tmux_session\": \"eval-supp-obj-vla-only-s46\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-obj-vla-only-s46.log\", \"data_path\": \"LIBERO-object\", \"data_count\": 200}, \"metrics\": {\"SR\": 0.79}}, \"eval-supp-long-vla-only-s44\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python src/evaluate.py --benchmark long --mode vla_only --seed 44 --n_rollouts 20 --K 1\", \"server\": \"bjb1-32546\", \"seed\": 44, \"pid\": 997776, \"log_path\": \"/tmp/eval_long_vla_only_s44.log\", \"model_name\": \"SmolVLA\", \"data_path\": \"long_suite\", \"data_count\": 20}, \"metrics\": {\"SR\": 0.565}}, \"eval-supp-long-k2mean-s43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --benchmark long --mode vla_only --seed 43 --n_rollouts 20 --K 2 --baseline_mode mean\", \"server\": \"bjb1-32546\", \"seed\": 43, \"pid\": 996158, \"log_path\": \"/tmp/eval_long_k2mean_s43.log\", \"model_name\": \"SmolVLA\", \"data_path\": \"long_suite\", \"data_count\": 20}, \"metrics\": {\"SR\": 0.56}}, \"eval-supp-long-reconvla-s43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/evaluate.py --benchmark long --mode reconvla --seed 43 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"seed\": 43, \"pid\": 994675, \"log_path\": \"/tmp/eval_long_reconvla_s43.log\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"long_suite\", \"data_count\": 20}, \"metrics\": {\"SR\": 0.59}}, \"eval-supp-long-crm-norm005-s43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python src/evaluate.py --benchmark long --mode crm_obs_only --seed 43 --n_rollouts 20 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt --K 10\", \"server\": \"bjb1-32546\", \"seed\": 43, \"pid\": 993249, \"log_path\": \"/tmp/eval_long_crm_norm005_s43.log\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"long_suite\", \"data_count\": 20}, \"metrics\": {\"SR\": 0.545}}, \"eval-supp-long-adapt-tau025-s43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"seed\": 43, \"pid\": 991960, \"log_path\": \"/tmp/eval_long_adapt_tau025_s43.log\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"long_suite\", \"data_count\": 20}, \"metrics\": {\"SR\": 0.58, \"trigger_rate\": 0.045}}, \"eval-supp-obj-adapt-tau025-s45-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"seed\": 45, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/tmp/eval_obj_adapt_s45_r2.log\"}}, \"eval-supp-long-crm-norm005-s42\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt --benchmark long --seed 42 --n_rollouts 20 --max_correction_norm 0.05\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"712378\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s42.log\", \"submitted_at\": \"2026-05-23T09:57:35.905Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla-crm-norm005\", \"seed\": 42, \"wall_clock_seconds\": 26891.8, \"gpu_hours\": 7.47}, \"metrics\": {\"overall_sr\": 0.565}}, \"eval-supp-long-adapt-tau025-s42\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"711770\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-adapt-tau025-s42.log\", \"submitted_at\": \"2026-05-23T09:57:28.057Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla-adaptive-crm-tau025\", \"seed\": 42, \"wall_clock_seconds\": 26893.5, \"gpu_hours\": 7.47}, \"metrics\": {\"overall_sr\": 0.59, \"trigger_rate\": 0.039, \"tau\": 0.25, \"crm_applied_steps\": 2785, \"total_steps\": 71980}}, \"eval-supp-long-reconvla-s42\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --K 10 --benchmark long --seed 42 --n_rollouts 20\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"711479\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s42.log\", \"submitted_at\": \"2026-05-23T09:57:18.522Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla-reconvla-k10\", \"seed\": 42, \"wall_clock_seconds\": 26894.0, \"gpu_hours\": 7.47}, \"metrics\": {\"overall_sr\": 0.565}}, \"eval-ablation-tau040-goal-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.40 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO goal suite\", \"data_count\": 20, \"model_name\": \"smolvla + CRM 3suite v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO goal benchmark\"}, \"metrics\": {\"overall_sr\": 0.835, \"trigger_rate\": 0.012, \"tau\": 0.4, \"crm_applied_steps\": 346, \"total_steps\": 28165}}, \"eval-ablation-tau015-goal-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.15 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO goal suite\", \"data_count\": 20, \"model_name\": \"smolvla + CRM 3suite v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO goal benchmark\"}, \"metrics\": {\"overall_sr\": 0.85, \"trigger_rate\": 0.339, \"tau\": 0.15, \"crm_applied_steps\": 9590, \"total_steps\": 28273}}, \"eval-supp-k2mean-object-s44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"pid\": \"177864\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-k2mean-object-s44.log\", \"submitted_at\": \"2026-05-23T11:27:59.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA-K2mean\", \"wall_clock_seconds\": 21427.5, \"gpu_hours\": 5.95}, \"metrics\": {\"overall_sr\": 0.75, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.8, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.55, \"milk\": 0.7, \"chocolate_pudding\": 0.75, \"orange_juice\": 0.95}}}, \"eval-ablation-tau010-goal-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.10 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO goal suite\", \"data_count\": 20, \"model_name\": \"smolvla + CRM 3suite v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO goal benchmark\"}, \"metrics\": {\"overall_sr\": 0.81, \"trigger_rate\": 0.739, \"tau\": 0.1, \"crm_applied_steps\": 22170, \"total_steps\": 29984}}, \"eval-supp-obj-reconvla-s44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --K 10 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"180869\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-obj-reconvla-s44.log\", \"submitted_at\": \"2026-05-23T11:31:37.684Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"smolvla-reconvla\", \"wall_clock_seconds\": 21190.8, \"gpu_hours\": 5.89}, \"metrics\": {\"overall_sr\": 0.76, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.7, \"salad_dressing\": 0.7, \"bbq_sauce\": 0.95, \"ketchup\": 0.9, \"tomato_sauce\": 0.7, \"butter\": 0.75, \"milk\": 0.6, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.95}}}, \"eval-supp-spatial-vla-only-s44\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"148584\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-spatial-vla-only-s44.log\", \"submitted_at\": \"2026-05-23T11:51:28.980Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial_benchmark\", \"data_count\": 20, \"model_name\": \"vla_only\", \"seed\": 44, \"checkpoint_source\": \"n/a\", \"eval_data\": \"spatial\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 19841.6, \"gpu_hours\": 5.51}, \"metrics\": {\"overall_sr\": 0.785, \"successes\": 157, \"total\": 200, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.95, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.8, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.7}}}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --benchmark goal --mode vla_only --seed 44 --n_rollouts 20 --K 1\", \"server\": \"bjb1-32546\", \"seed\": 44, \"pid\": 990832, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\", \"model_name\": \"SmolVLA\", \"data_path\": \"goal_suite\", \"data_count\": 20, \"checkpoint_path\": \"n/a\"}, \"metrics\": {\"SR\": 0.85, \"successes\": 170, \"total\": 200, \"per_task\": {\"open_middle_drawer\": 0.85, \"put_bowl_stove\": 0.95, \"wine_bottle_cabinet\": 0.85, \"open_top_drawer_bowl\": 0.7, \"bowl_on_cabinet\": 0.9, \"push_plate_stove\": 0.9, \"cream_cheese_bowl\": 0.65, \"turn_on_stove\": 1, \"bowl_on_plate\": 0.95, \"wine_bottle_rack\": 0.75}}}, \"eval-supp-k2mean-spatial-s44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark spatial --n_rollouts 20 --seed 44\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"pid\": \"174444\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-k2mean-spatial-s44.log\", \"submitted_at\": \"2026-05-23T11:24:26.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"wall_clock_seconds\": 11842.7, \"gpu_hours\": 3.29}, \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200}}, \"eval-supp-spatial-vla-only-s43\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"pid\": \"181173\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-spatial-vla-only-s43.log\", \"submitted_at\": \"2026-05-23T11:31:46.804Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"wall_clock_seconds\": 11396.2, \"gpu_hours\": 3.17}, \"metrics\": {\"overall_success_rate\": 0.79, \"successes\": 158, \"total\": 200}}, \"eval-supp-k2mean-goal-s44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"910373\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-k2mean-goal-s44.log\", \"submitted_at\": \"2026-05-23T11:39:08.809Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-goal\", \"data_count\": 20, \"model_name\": \"SmolVLA-K2mean\", \"wall_clock_seconds\": 9769.1, \"gpu_hours\": 2.71}, \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"drawer\": 0.85, \"bowl_stove\": 1, \"wine_cabinet\": 0.8, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.95, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.75}}}, \"eval-supp-adapt-tau025-obj-s44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"910029\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s44.log\", \"submitted_at\": \"2026-05-23T11:39:03.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-object\", \"data_count\": 20, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"wall_clock_seconds\": 9768.3, \"gpu_hours\": 2.71}, \"metrics\": {\"overall_sr\": 0.75, \"trigger_rate\": 0.0364, \"mean_uncertainty\": 0.11, \"crm_applied_steps\": 1310, \"total_steps\": 35990, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.75, \"salad_dressing\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.65, \"milk\": 0.7, \"chocolate\": 0.75, \"orange_juice\": 0.85}}}, \"eval-supp-crm-norm005-obj-s44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"909754\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm005-obj-s44.log\", \"submitted_at\": \"2026-05-23T11:38:57.336Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-object\", \"data_count\": 20, \"model_name\": \"SmolVLA+CRM\", \"wall_clock_seconds\": 9768.9, \"gpu_hours\": 2.71}, \"metrics\": {\"overall_sr\": 0.74, \"per_task\": {\"alphabet_soup\": 0.6, \"cream_cheese\": 0.6, \"salad_dressing\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.8, \"tomato\": 0.7, \"butter\": 0.65, \"milk\": 0.6, \"chocolate\": 0.9, \"orange_juice\": 0.95}}}, \"eval-supp-goal-vla-only-wrapper-s43\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"905856\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s43.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"wall_clock_seconds\": 10020.5, \"gpu_hours\": 2.78}, \"metrics\": {\"overall_sr\": 0.825, \"per_task\": {\"drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.9, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}}, \"eval-supp-long-vla-only-s42\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark long --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:3\"], \"seed\": 42, \"model_name\": \"SmolVLA\", \"tmux_session\": \"eval-supp-long-vla-only-s42\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-long-vla-only-s42.log\"}, \"metrics\": {\"overall_sr\": 0.58, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.25, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0.65, \"KITCHEN_SCENE3_stove_moka_pot\": 1, \"KITCHEN_SCENE4_black_bowl_drawer\": 1, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.4, \"STUDY_SCENE1_book_caddy\": 0.9, \"LIVING_ROOM_SCENE6_mug_pudding\": 0.3, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0.55, \"KITCHEN_SCENE8_moka_pots_stove\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.75}}}, \"eval-supp-goal-reconvla-s44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --K 10 --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"719848\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-reconvla-s44.log\", \"submitted_at\": \"2026-05-23T10:14:17.183Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"wall_clock_seconds\": 11487.9, \"gpu_hours\": 3.19}, \"metrics\": {\"success_rate\": 0.805, \"total_rollouts\": 200, \"total_successes\": 161, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.81, 0.81, 0.805], \"mean\": 0.8083, \"std\": 0.0029}}}, \"eval-supp-obj-reconvla-s43\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --K 10 --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu_ids\": [\"cuda:2\"], \"seed\": 43, \"data_path\": \"LIBERO/object\", \"data_count\": 200, \"model_name\": \"smolvla-reconvla\", \"checkpoint_source\": \"smolvla_libero\", \"eval_data\": \"LIBERO-object-10tasks-20rollouts\"}, \"metrics\": {\"success_rate\": 0.77, \"total_rollouts\": 200, \"total_successes\": 154}}, \"eval-supp-crm-norm005-goal-s44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 44 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"719244\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm005-goal-s44.log\", \"submitted_at\": \"2026-05-23T10:14:04.000Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla+crm_obs_only_norm005\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"wall_clock_seconds\": 11489.4, \"gpu_hours\": 3.19}, \"metrics\": {\"success_rate\": 0.835, \"total_rollouts\": 200, \"total_successes\": 167, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.855, 0.82, 0.835], \"mean\": 0.8367, \"std\": 0.0176}}}, \"eval-supp-k2mean-object-s43\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite object --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"cuda:2\", \"pid\": 16441}, \"metrics\": {\"overall_success_rate\": 0.78, \"total_successes\": 156, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0.85, \"cream_cheese\": 0.85, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.7, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.9}}}, \"eval-supp-k2mean-goal-s42-r2\": {\"spec\": {\"command\": \"python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --n_rollouts 20 --seed 42\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"eval-supp-k2mean-goal-s42\", \"eval_data\": \"goal\"}, \"metrics\": {\"overall_sr\": 0.855, \"n_tasks\": 10, \"n_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 1, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.65, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.8}}}, \"eval-supp-adapt-tau025-goal-s44\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla+crm_adaptive_tau025\", \"data_path\": \"goal_benchmark\", \"data_count\": 20, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"goal\"}, \"metrics\": {\"success_rate\": 0.865, \"trigger_rate\": 0.0677, \"crm_applied_steps\": 1870, \"total_steps\": 27642}}, \"eval-supp-crm-norm005-obj-s43\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:4\"], \"pid\": 818928, \"seed\": 43, \"model_name\": \"smolvla+crm_obs_only_norm005\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"metrics\": {\"success_rate\": 0.785}}, \"eval-supp-adapt-tau025-goal-s43\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:2\"], \"pid\": 818658, \"seed\": 43, \"model_name\": \"smolvla+crm_adaptive_tau025\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}, \"metrics\": {\"success_rate\": 0.845, \"trigger_rate\": 0.088, \"crm_applied_steps\": 2509, \"total_steps\": 28500}}, \"eval-supp-crm-norm005-goal-s43\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 818386, \"seed\": 43, \"model_name\": \"smolvla+crm_obs_only_norm005\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}, \"metrics\": {\"success_rate\": 0.82}}, \"eval-supp-adapt-tau025-obj-s43\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:0\"], \"pid\": 818121, \"seed\": 43, \"model_name\": \"smolvla+crm_adaptive_tau025\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"metrics\": {\"success_rate\": 0.775, \"trigger_rate\": 0.0367, \"crm_applied_steps\": 1312, \"total_steps\": 35796}}, \"eval-supp-goal-reconvla-s43\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python src/evaluate.py --mode reconvla --K 10 --suite goal --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Goal\", \"gpu\": \"cuda:5\", \"pid\": 34385}, \"metrics\": {\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_episodes\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.65, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.55, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.95, \"put_the_wine_bottle_on_the_rack\": 0.85}}}, \"eval-supp-k2mean-spatial-s43\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite spatial --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:0\", \"pid\": 16439}, \"metrics\": {\"overall_success_rate\": 0.78, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_episodes\": 200, \"per_task\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.75, \"next_to_plate\": 0.7, \"on_wooden_cabinet\": 0.85}}}, \"eval-supp-reconvla-spatial-s44\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python src/evaluate.py --mode reconvla --K 10 --suite spatial --n_rollouts 20 --seed 44\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:3\", \"pid\": 34383}, \"metrics\": {\"overall_success_rate\": 0.795, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task\": {\"between_plate_and_ramekin\": 1, \"table_center\": 1, \"next_to_ramekin\": 0.95, \"next_to_cookie_box\": 0.95, \"on_cookie_box\": 0.9, \"on_wooden_cabinet\": 0.85, \"on_stove\": 0.8, \"next_to_plate\": 0.8, \"top_drawer_wooden_cabinet\": 0.7, \"on_ramekin\": 0}, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.8, 0.815, 0.795], \"mean\": 0.803, \"std\": 0.01}}}, \"eval-supp-reconvla-spatial-s43\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python src/evaluate.py --mode reconvla --K 10 --suite spatial --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:1\", \"pid\": 34387}, \"metrics\": {\"overall_success_rate\": 0.815, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.85}}}, \"eval-supp-k2mean-goal-s43\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite goal --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Goal\", \"gpu\": \"cuda:4\", \"pid\": 16445}, \"metrics\": {\"overall_success_rate\": 0.815, \"total_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.55, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.45, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.95, \"put_the_wine_bottle_on_the_rack\": 0.85}}}, \"eval-supp-k2mean-object-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark object --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-supp-k2mean-object-s42.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"618917\", \"log_path\": \"logs/eval-supp-k2mean-object-s42.log\", \"submitted_at\": \"2026-05-23T07:13:58.001Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"n/a (vla_only mode)\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"n/a (eval-only)\", \"wall_clock_seconds\": 10540.4, \"gpu_hours\": 2.93}, \"metrics\": {\"success_rate\": 79.5, \"total_successes\": 159, \"total_rollouts\": 200, \"mode\": \"vla_only\", \"K\": 2, \"baseline_mode\": \"mean\", \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"bbq_sauce\": 90, \"ketchup\": 95, \"tomato_sauce\": 85, \"butter\": 60, \"milk\": 70, \"chocolate_pudding\": 70, \"orange_juice\": 95}}}, \"eval-supp-goal-adapt-tau025-s42\": {\"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-goal-adapt-tau025-s42.log\"}, \"metrics\": {\"success_rate\": 84, \"total_rollouts\": 200, \"total_successes\": 168, \"trigger_rate\": 8.3, \"mean_unc\": 0.1448, \"per_task\": {\"open_middle_drawer_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"put_bowl_on_stove\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"put_wine_bottle_on_cabinet\": {\"sr\": 80, \"success\": 16, \"total\": 20}, \"open_top_drawer_put_bowl\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"put_bowl_on_top_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"push_plate_to_stove\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"put_cream_cheese_in_bowl\": {\"sr\": 60, \"success\": 12, \"total\": 20}, \"turn_on_stove\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"put_bowl_on_plate\": {\"sr\": 90, \"success\": 18, \"total\": 20}, \"put_wine_bottle_on_rack\": {\"sr\": 80, \"success\": 16, \"total\": 20}}}}, \"eval-supp-goal-crm005-s42\": {\"spec\": {\"command\": \"evaluate.py --mode crm_obs_only --max_correction_norm 0.05 --benchmark goal\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": 524322, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-crm005-s42.log\", \"submitted_at\": \"2026-05-23T04:12:27.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\", \"wall_clock_seconds\": 10324.7, \"gpu_hours\": 2.87}, \"metrics\": {\"success_rate\": 85.5, \"total_successes\": 171, \"total_episodes\": 200, \"per_task\": {\"middle_drawer\": 85, \"bowl_stove\": 100, \"wine_bottle_cabinet\": 95, \"top_drawer_bowl\": 70, \"bowl_cabinet\": 95, \"plate_stove\": 95, \"cream_cheese_bowl\": 50, \"stove\": 95, \"bowl_plate\": 95, \"wine_bottle_rack\": 75}}}, \"eval-supp-goal-reconvla-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20 --K 10 2>&1 | tee logs/eval-supp-goal-reconvla-s42.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"620817\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-reconvla-s42.log\", \"submitted_at\": \"2026-05-23T07:16:25.113Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\", \"wall_clock_seconds\": 10491.5, \"gpu_hours\": 2.91}}, \"train-crm-unified-4suite-r6\": {\"spec\": {\"command\": \"train_crm.py --benchmark all --epochs 50 --resume_from checkpoint_epoch0038.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"pid\": 668372, \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-unified-4suite-r6.log\", \"submitted_at\": \"2026-05-23T04:12:01.547Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5\", \"data_count\": 0, \"model_name\": \"crm_obs_only_4suite\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/\", \"wall_clock_seconds\": 21468.6, \"gpu_hours\": 5.96}, \"metrics\": {\"best_val_loss\": 0.005669, \"epochs\": 50, \"final_train_loss\": 0.009731, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/\"}}, \"eval-goal-vla-only-wrapper-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark goal --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-goal-vla-only-wrapper-s42.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"621698\", \"log_path\": \"logs/eval-goal-vla-only-wrapper-s42.log\", \"submitted_at\": \"2026-05-23T07:16:35.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"n/a (vla_only mode)\", \"eval_data\": \"LIBERO-Goal\", \"checkpoint_path\": \"n/a (eval-only)\", \"wall_clock_seconds\": 10388.9, \"gpu_hours\": 2.89}, \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200}}, \"eval-supp-obj-adapt-tau025-s42\": {\"spec\": {\"log_path\": \"logs/eval-supp-obj-adapt-tau025-s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"result_file\": \"logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\"}, \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.035, \"mean_unc\": 0.109, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 2}}, \"eval-supp-k2mean-spatial-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark spatial --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-supp-k2mean-spatial-s42.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"621415\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-k2mean-spatial-s42.log\", \"submitted_at\": \"2026-05-23T07:16:30.364Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"n/a (vla_only mode)\", \"eval_data\": \"LIBERO-Spatial\", \"wall_clock_seconds\": 8626.1, \"gpu_hours\": 2.4}, \"metrics\": {\"success_rate\": 81.5, \"total_success\": 163, \"total_rollouts\": 200, \"per_task\": {\"bowl_between_plate_ramekin\": 95, \"bowl_next_to_ramekin\": 95, \"bowl_from_table_center\": 100, \"bowl_on_cookie_box\": 100, \"bowl_in_top_drawer\": 70, \"bowl_on_ramekin\": 0, \"bowl_next_to_cookie_box\": 95, \"bowl_on_stove\": 80, \"bowl_next_to_plate\": 85, \"bowl_on_wooden_cabinet\": 95}}}, \"eval-supp-crm-norm005-spatial-s44\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.05 --max_steps 280 2>&1 | tee logs/eval-supp-crm-norm005-spatial-s44.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"759205\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm005-spatial-s44.log\", \"submitted_at\": \"2026-05-23T06:52:10.651Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 7454.9, \"gpu_hours\": 2.07}, \"metrics\": {\"success_rate\": 78.5, \"total_rollouts\": 200, \"total_successes\": 157, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"next_to_ramekin\": {\"sr\": 90, \"success\": 18, \"total\": 20}, \"from_table_center\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_cookie_box\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"in_top_drawer_wooden_cabinet\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_ramekin\": {\"sr\": 0, \"success\": 0, \"total\": 20}, \"next_to_cookie_box\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_stove\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"next_to_plate\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_wooden_cabinet\": {\"sr\": 80, \"success\": 16, \"total\": 20}}, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [80, 81, 78.5], \"mean\": 79.8, \"std\": 1.3}}}, \"eval-supp-adapt-tau025-spatial-s44\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-adapt-tau025-spatial-s44.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"742219\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s44.log\", \"submitted_at\": \"2026-05-23T06:33:10.257Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 200, \"data_path\": \"/root/acr-vla-conformal-refinement\", \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"wall_clock_seconds\": 7861.7, \"gpu_hours\": 2.18}, \"metrics\": {\"success_rate\": 80.5, \"total_successes\": 161, \"total_rollouts\": 200, \"trigger_rate\": 20, \"mean_unc\": 0.1881, \"conformal_threshold\": 0.25, \"max_correction_norm\": 0.2, \"mode\": \"adaptive_conformal_crm\", \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin\": {\"sr\": 90, \"successes\": 18, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_ramekin\": {\"sr\": 95, \"successes\": 19, \"rollouts\": 20}, \"pick_up_the_black_bowl_from_table_center\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_cookie_box\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet\": {\"sr\": 65, \"successes\": 13, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_ramekin\": {\"sr\": 0, \"successes\": 0, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_cookie_box\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_stove\": {\"sr\": 80, \"successes\": 16, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_plate\": {\"sr\": 80, \"successes\": 16, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_wooden_cabinet\": {\"sr\": 95, \"successes\": 19, \"rollouts\": 20}}}}, \"eval-supp-reconvla-k2-spatial-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 2 --benchmark spatial --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-supp-reconvla-k2-spatial-s42.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"742499\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-reconvla-k2-spatial-s42.log\", \"submitted_at\": \"2026-05-23T06:33:15.223Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 200, \"data_path\": \"/root/acr-vla-conformal-refinement\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"wall_clock_seconds\": 7403.0, \"gpu_hours\": 2.06}, \"metrics\": {\"success_rate\": 80, \"total_rollouts\": 200, \"total_successes\": 160, \"per_task\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 100, \"from_table_center\": 100, \"on_cookie_box\": 95, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 95, \"on_stove\": 75, \"next_to_plate\": 80, \"on_wooden_cabinet\": 85}}}, \"eval-supp-adapt-tau025-spatial-s43\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-adapt-tau025-spatial-s43.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"741944\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s43.log\", \"submitted_at\": \"2026-05-23T06:33:05.214Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 200, \"data_path\": \"/root/acr-vla-conformal-refinement\", \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"wall_clock_seconds\": 7376.4, \"gpu_hours\": 2.05}, \"metrics\": {\"success_rate\": 80, \"trigger_rate\": 19.4, \"mean_unc\": 0.1845, \"total_rollouts\": 200, \"total_successes\": 160, \"per_task\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 95, \"from_table_center\": 95, \"on_cookie_box\": 100, \"in_top_drawer_wooden_cabinet\": 70, \"on_ramekin\": 0, \"next_to_cookie_box\": 100, \"on_stove\": 80, \"next_to_plate\": 85, \"on_wooden_cabinet\": 80}}}, \"eval-supp-crm-norm005-spatial-s43\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 43 --n_rollouts 20 --max_correction_norm 0.05 2>&1 | tee logs/eval-supp-crm-norm005-spatial-s43.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"743110\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm005-spatial-s43.log\", \"submitted_at\": \"2026-05-23T06:33:20.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 200, \"data_path\": \"/root/acr-vla-conformal-refinement\", \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"wall_clock_seconds\": 7304.2, \"gpu_hours\": 2.03}, \"metrics\": {\"success_rate\": 81, \"total_rollouts\": 200, \"total_successes\": 162, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"next_to_ramekin\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"from_table_center\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_cookie_box\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"in_top_drawer_wooden_cabinet\": {\"sr\": 75, \"success\": 15, \"total\": 20}, \"on_ramekin\": {\"sr\": 0, \"success\": 0, \"total\": 20}, \"next_to_cookie_box\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_stove\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"next_to_plate\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_wooden_cabinet\": {\"sr\": 95, \"success\": 19, \"total\": 20}}}}, \"eval-supp-k2mean-goal-s42\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-supp-k2mean-goal-s42.log\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"n/a\", \"submitted_at\": \"2026-05-23T06:56:53.932Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"n/a (vla_only mode)\", \"eval_data\": \"LIBERO-Goal\", \"checkpoint_path\": \"n/a\", \"failure_reason\": \"exit code 127 (command not found) on bjb2-40593 — likely environment not set up for K=2 mean evaluate.py\", \"wall_clock_seconds\": 5578.1, \"gpu_hours\": 1.55}}, \"eval-supp-obj-adapt-s42-r2\": {\"spec\": {\"command\": \"evaluate.py --mode adaptive_conformal_crm --conformal_threshold 0.074855 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": 522259, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-obj-adapt-s42-r2.log\", \"submitted_at\": \"2026-05-23T04:12:14.719Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 10570.2, \"gpu_hours\": 2.94}, \"metrics\": {\"success_rate\": 77.5, \"total_successes\": 155, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 80, \"cream_cheese\": 90, \"salad_dressing\": 70, \"bbq_sauce\": 85, \"ketchup\": 70, \"tomato_sauce\": 75, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 80, \"orange_juice\": 95}, \"mean_unc\": 0.1104, \"trigger_rate\": 0.702}}, \"eval-object-vla-only-wrapper-s44-r2\": {\"spec\": {\"command\": \"evaluate.py --mode vla_only --benchmark object --seed 44\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 521785, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-object-vla-only-wrapper-s44-r2.log\", \"submitted_at\": \"2026-05-23T04:12:06.236Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 10539.3, \"gpu_hours\": 2.93}, \"metrics\": {\"success_rate\": 77.5, \"total_successes\": 155, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 90, \"ketchup\": 90, \"tomato_sauce\": 80, \"butter\": 75, \"milk\": 65, \"chocolate_pudding\": 65, \"orange_juice\": 95}}}, \"eval-object-vla-only-wrapper-s43-r2\": {\"spec\": {\"command\": \"evaluate.py --mode vla_only --benchmark object --seed 43\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:4\", \"pid\": 520493, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-object-vla-only-wrapper-s43-r2.log\", \"submitted_at\": \"2026-05-23T04:11:55.548Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 10532.1, \"gpu_hours\": 2.93}, \"metrics\": {\"success_rate\": 77, \"total_successes\": 154, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 85, \"ketchup\": 80, \"tomato_sauce\": 85, \"butter\": 60, \"milk\": 75, \"chocolate_pudding\": 75, \"orange_juice\": 95}}}, \"eval-object-vla-only-wrapper-s42-r2\": {\"spec\": {\"command\": \"evaluate.py --mode vla_only --benchmark object --seed 42\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"pid\": 519749, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-object-vla-only-wrapper-s42-r2.log\", \"submitted_at\": \"2026-05-23T04:11:36.448Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 10532.1, \"gpu_hours\": 2.93}, \"metrics\": {\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 85, \"cream_cheese\": 75, \"salad_dressing\": 85, \"bbq_sauce\": 85, \"ketchup\": 90, \"tomato_sauce\": 75, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 70, \"orange_juice\": 95}}}, \"eval-supp-obj-reconvla-s42\": {\"spec\": {\"command\": \"evaluate.py --mode reconvla --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:1\", \"pid\": 523238, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-obj-reconvla-s42.log\", \"submitted_at\": \"2026-05-23T04:12:20.187Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 10114.4, \"gpu_hours\": 2.81}, \"metrics\": {\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"bbq_sauce\": 95, \"ketchup\": 90, \"tomato_sauce\": 80, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 75, \"orange_juice\": 90}}}, \"eval-supp-obj-crm005-s42-r2\": {\"spec\": {\"command\": \"evaluate.py --mode crm_obs_only --max_correction_norm 0.05 --benchmark object\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"pid\": 669419, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-obj-crm005-s42-r2.log\", \"submitted_at\": \"2026-05-23T04:12:10.537Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 8872.7, \"gpu_hours\": 2.46}, \"metrics\": {\"overall_success_rate\": 0.77, \"n_success\": 154, \"n_total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"conformal_threshold\": 0.074855, \"K\": 10, \"seed\": 42, \"per_task_sr\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.9, \"ketchup\": 0.8, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.75, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}}}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {\"spec\": {\"command\": \"evaluate.py --mode adaptive_conformal_crm --conformal_threshold 0.35\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 667018, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau035-spatial-s42-r2.log\", \"submitted_at\": \"2026-05-23T04:11:49.182Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"wall_clock_seconds\": 7722.1, \"gpu_hours\": 2.15}, \"metrics\": {\"overall_sr\": 80, \"n_success\": 160, \"n_total\": 200, \"trigger_rate\": 12.17, \"mean_unc\": 0.1873, \"conformal_threshold\": 0.35, \"max_correction_norm\": 0.2, \"crm_applied_steps\": 3474, \"total_steps\": 28549, \"per_task_sr\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 100, \"from_table_center\": 90, \"on_cookie_box\": 95, \"in_top_drawer\": 70, \"on_ramekin\": 0, \"next_to_cookie_box\": 95, \"on_stove\": 85, \"next_to_plate\": 85, \"on_wooden_cabinet\": 85}}}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {\"spec\": {\"command\": \"evaluate.py --mode adaptive_conformal_crm --conformal_threshold 0.15\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"pid\": 664686, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau015-spatial-s42-r2.log\", \"submitted_at\": \"2026-05-23T04:11:21.579Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"wall_clock_seconds\": 7509.2, \"gpu_hours\": 2.09}, \"metrics\": {\"overall_sr\": 80.5, \"n_success\": 161, \"n_total\": 200, \"trigger_rate\": 40.7, \"mean_unc\": 0.1852, \"conformal_threshold\": 0.15, \"max_correction_norm\": 0.2, \"per_task_sr\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 100, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 90, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 75, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 90, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 80, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 85}}}, \"eval-supp-crm-norm02-spatial-s42-r2\": {\"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-crm-norm02-spatial-s42-r2.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"pid\": 664402, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm02-spatial-s42-r2.log\", \"submitted_at\": \"2026-05-23T04:11:09.306Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"wall_clock_seconds\": 7293.9, \"gpu_hours\": 2.03}, \"metrics\": {\"overall_sr\": 79, \"n_success\": 158, \"n_total\": 200, \"per_task_sr\": {\"between_plate_and_ramekin\": 100, \"next_to_ramekin\": 90, \"from_table_center\": 95, \"on_cookie_box\": 95, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 100, \"on_stove\": 95, \"next_to_plate\": 75, \"on_wooden_cabinet\": 65}}}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {\"spec\": {\"command\": \"evaluate.py --mode adaptive_conformal_crm --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": 665520, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s42-r2.log\", \"submitted_at\": \"2026-05-23T04:11:35.167Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"wall_clock_seconds\": 7232.0, \"gpu_hours\": 2.01}, \"metrics\": {\"overall_sr\": 82, \"n_success\": 164, \"n_total\": 200, \"trigger_rate\": 19.4, \"mean_unc\": 0.1847, \"per_task_sr\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 95, \"from_table_center\": 100, \"on_cookie_box\": 100, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 90, \"on_stove\": 90, \"next_to_plate\": 90, \"on_wooden_cabinet\": 85}}}, \"eval-openvla-object-baseline-seed42-r2\": {\"spec\": {\"command\": \"n/a\", \"server\": \"n/a\", \"data_path\": \"n/a\", \"data_count\": 0, \"model_name\": \"openvla\", \"seed\": 42}}, \"eval-obs-only-object-norm02-seed55\": {}, \"precompute-pi05-features-object\": {}, \"precompute-smolvla-goal-shard2\": {}, \"precompute-smolvla-goal-shard1\": {}, \"precompute-smolvla-goal-shard0\": {}, \"eval-smolvla-long-seed2\": {}, \"eval-smolvla-long-seed1\": {}, \"eval-smolvla-long-seed0\": {}, \"eval-smolvla-crm-spatial-seed42-v1\": {}, \"eval-smolvla-crm-spatial-seed43-v1\": {}, \"eval-smolvla-crm-spatial-seed44-v1\": {}, \"eval-smolvla-crm-goal-seed42-v1\": {}, \"eval-smolvla-crm-goal-seed43-v1\": {}, \"eval-smolvla-crm-goal-seed44-v1\": {}, \"eval-supp-obj-adapt-s42\": {}, \"eval-crm-norm02-spatial-s42\": {}, \"eval-adaptive-tau015-spatial-s42\": {}, \"eval-adaptive-tau025-spatial-s42\": {}, \"eval-adaptive-tau035-spatial-s42\": {}, \"train-crm-unified-4suite-r5-resumed\": {\"spec\": {\"command\": \"python -u src/train_crm.py --input_mode obs_only --benchmark all --epochs 50 --resume /root/autodl-tmp/checkpoints/crm_smolvla_4suite_r5/checkpoint_epoch0032.pt\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5\", \"data_count\": 0, \"model_name\": \"crm_obs_only_4suite\", \"seed\": 42, \"gpu\": \"cuda:3\", \"pid\": 548658, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_4suite_r5/checkpoint_epoch0032.pt\", \"eval_data\": \"N/A (training, not eval)\"}}, \"eval-object-vla-only-wrapper-s44\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode vla_only --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"N/A (VLA-only, no CRM)\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"cuda:5\", \"pid\": 455618}}, \"eval-object-vla-only-wrapper-s43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode vla_only --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"N/A (VLA-only, no CRM)\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"cuda:4\", \"pid\": 455415}}, \"eval-object-vla-only-wrapper-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"N/A (VLA-only, no CRM)\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"cuda:3\", \"pid\": 455214}}, \"eval-supp-obj-crm005-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"cuda:5\", \"pid\": 626812}}, \"eval-supp-adapt-tau035-spatial-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:4\", \"pid\": 626543}}, \"eval-supp-adapt-tau025-spatial-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:2\", \"pid\": 626274}}, \"eval-supp-adapt-tau015-spatial-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:1\", \"pid\": 626005}}, \"eval-supp-crm-norm02-spatial-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:0\", \"pid\": 625804}}, \"eval-3dir-adaptive-spatial-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/dirB_adaptive_spatial_s42.log\"}, \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"trigger_rate\": 0.918, \"tau\": 0.074855, \"mean_uncertainty\": 0.183, \"crm_applied_steps\": 26589, \"total_steps\": 28955, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 1, \"from_table_center\": 1, \"on_cookie_box\": 0.9, \"in_top_drawer\": 0.8, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.8}}}, \"eval-3dir-norm03-spatial-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.3\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:0\", \"pid\": 548888, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/dirA_norm03_spatial_s42.log\", \"metrics\": {\"success_rate\": 73.9, \"n_tasks\": 9, \"n_rollouts\": 20, \"note\": \"killed at T10 rollout 10/20, 9/10 tasks complete\"}}, \"metrics\": {\"success_rate\": 73.9, \"successes\": 133, \"total\": 180, \"n_tasks_complete\": 9, \"n_tasks_total\": 10, \"n_rollouts\": 20, \"note\": \"killed at T10 rollout 10/20, 9/10 tasks complete\", \"per_task_sr\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 0.85, \"from_table_center\": 1, \"on_cookie_box\": 0.9, \"in_top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0.8, \"next_to_plate\": 0.55, \"on_wooden_cabinet\": \"partial_5/10\"}}}, \"eval-3dir-reconvla-spatial-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode reconvla --benchmark spatial --seed 42 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"N/A (reconvla uses no CRM)\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:5\", \"pid\": 550634, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/dirC_reconvla_spatial_s42.log\", \"metrics\": {\"success_rate\": 79, \"n_tasks\": 10, \"n_rollouts\": 20}}, \"metrics\": {\"success_rate\": 79, \"successes\": 158, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 0.95, \"from_table_center\": 1, \"on_cookie_box\": 1, \"in_top_drawer\": 0.65, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.75, \"next_to_plate\": 0.7, \"on_wooden_cabinet\": 0.85}}}, \"eval-3dir-norm01-spatial-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:1\", \"pid\": 549157, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/dirA_norm01_spatial_s42.log\", \"metrics\": {\"success_rate\": 79, \"n_tasks\": 10, \"n_rollouts\": 20}}, \"metrics\": {\"success_rate\": 79, \"successes\": 158, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"from_table_center\": 1, \"on_cookie_box\": 1, \"in_top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.75}}}, \"eval-3dir-norm005-spatial-s42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:2\", \"pid\": 549426, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/dirA_norm005_spatial_s42.log\", \"metrics\": {\"success_rate\": 80, \"n_tasks\": 10, \"n_rollouts\": 20}}, \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 1, \"from_table_center\": 1, \"on_cookie_box\": 0.95, \"in_top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.85, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.8}}}, \"precompute-pi05-goal-2048\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/train_crm.py --precompute --model pi05 --benchmark goal --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_goal/\", \"data_count\": 0, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_goal_2048.log\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/goal/\"}}, \"precompute-pi05-spatial-2048\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --precompute --model pi05 --benchmark spatial --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_spatial/\", \"data_count\": 0, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_spatial_2048.log\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/spatial/\"}}, \"precompute-pi05-object-2048\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 0, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_object_2048.log\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/object/\"}}, \"eval-smolvla-crm-object-seed43-v1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --K 10 --obs_dim 960 --n_action_steps 50 --max_steps 280\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed43.log\", \"metrics\": {\"success_rate\": 53.5, \"n_tasks\": 10, \"n_rollouts\": 20}}}, \"eval-smolvla-crm-object-seed42-v1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --K 10 --obs_dim 960 --n_action_steps 50 --max_steps 280\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed42.log\", \"metrics\": {\"success_rate\": 50.5, \"n_tasks\": 10, \"n_rollouts\": 20}}}, \"eval-smolvla-crm-object-seed44-v1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --K 10 --obs_dim 960 --n_action_steps 50 --max_steps 280\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed44.log\", \"metrics\": {\"success_rate\": 51.5, \"n_tasks\": 10, \"n_rollouts\": 20}}}, \"train-crm-unified-4suite-r5\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark object spatial goal long --obs_dim 960 --epochs 50 --batch_size 32 --lr 1e-3 --input_mode obs_only --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"322367\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 224555, \"model_name\": \"CRM-unified-4suite-obs_only\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/train.log\", \"checkpoint_source\": \"from_scratch (continuation of r4)\", \"eval_data\": \"N/A - training run\"}, \"metrics\": {\"val_loss\": 0.006075, \"epochs_completed\": 32, \"epochs_target\": 50, \"train_loss_final\": 0.010489, \"best_epoch\": 32, \"crash_epoch\": 33, \"crash_count\": 2}}, \"eval-smolvla-crm-goal-seed43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --K 10 --obs_dim 960 --n_action_steps 50 --max_steps 300\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}}, \"eval-smolvla-crm-goal-seed42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20 --K 10 --obs_dim 960 --n_action_steps 50 --max_steps 300\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}}, \"eval-smolvla-crm-spatial-seed44\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 44 --n_rollouts 20 --K 10 --obs_dim 960 --n_action_steps 50 --max_steps 280\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-smolvla-crm-spatial-seed43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 43 --n_rollouts 20 --K 10 --obs_dim 960 --n_action_steps 50 --max_steps 280\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-smolvla-crm-spatial-seed42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --K 10 --obs_dim 960 --n_action_steps 50 --max_steps 280\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-smolvla-crm-goal-seed44\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py --mode acr_vla --benchmark goal --n_rollouts 20 --seed 44 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"169920\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-smolvla-crm-goal-seed44.log\", \"submitted_at\": \"2026-05-22T05:10:35.845Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-long-2048\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_10/\", \"data_count\": 0, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\"}}, \"eval-smolvla-lerobot-goal-seed44-v3\": {\"spec\": {\"command\": \"lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.task=libero_goal --eval.n_episodes=20 --seed=44 --env.episode_length=300 --output_dir=/root/outputs/eval/smolvla_goal_seed44_v3\", \"server\": \"bjb1-32546\", \"pid\": 205154, \"data_path\": \"libero_goal\", \"data_count\": 20, \"model_name\": \"smolvla_libero\", \"seed\": 44, \"checkpoint_path\": \"/root/outputs/eval/smolvla_goal_seed44_v3\", \"log_path\": \"/tmp/eval_smolvla_goal_seed44_v3.log\"}, \"metrics\": {\"success_rate\": 78, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-goal-seed43-v3\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -m lerobot.scripts.eval --policy.path=lerobot/smolvla_libero --env.type=libero --env.task=libero_goal --eval.n_episodes=20 --seed=43 --output_dir=/root/outputs/eval/smolvla_goal_seed43_v3\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO-Goal (10 tasks x 20 rollouts)\", \"checkpoint_path\": \"/root/outputs/eval/smolvla_goal_seed43_v3\", \"log_path\": \"/tmp/eval_smolvla_goal_seed43_v3.log\"}, \"metrics\": {\"success_rate\": 82, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m lerobot.scripts.eval --policy.path=lerobot/smolvla_libero --env.type=libero --env.task=libero_spatial --eval.n_episodes=20 --seed=43 --output_dir=/root/outputs/eval/smolvla_spatial_seed43_v3\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"checkpoint_path\": \"/root/outputs/eval/smolvla_spatial_seed43_v3\", \"log_path\": \"/tmp/eval_smolvla_spatial_seed43_v3.log\"}, \"metrics\": {\"success_rate\": 54.5, \"n_episodes\": 200}}, \"train-crm-smolvla-3suite-v1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --cache_dir /root/autodl-tmp/crm_cache_smolvla_k10/ --benchmark object spatial goal --obs_dim 960 --input_mode obs_only --epochs 50 --batch_size 32 --lr 1e-3 --output_dir /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"344463\", \"data_path\": \"/root/autodl-tmp/crm_cache_smolvla_k10/\", \"data_count\": 77835, \"model_name\": \"CRM-SmolVLA-3suite-obs_only\", \"seed\": 42, \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-smolvla-3suite-v1.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/\"}, \"metrics\": {\"best_val_loss\": 0.005878, \"final_train_loss\": 0.00969, \"final_val_loss\": 0.00588, \"epochs_completed\": 50, \"total_params\": 327198, \"data_samples\": 77835, \"best_epoch\": 50}}, \"eval-smolvla-lerobot-goal-seed43-v2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.task=libero_goal --eval.n_episodes=20 --seed=43 --env.episode_length=300 --rename_map --output_dir=/root/outputs/eval/smolvla_goal_seed43_v2\", \"server\": \"bjb1-18228\", \"seed\": 43, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO-Goal (10 tasks x 20 rollouts)\", \"checkpoint_path\": \"N/A-killed\", \"log_path\": \"killed-on-bjb1-18228\"}}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.task=libero_spatial --eval.n_episodes=20 --seed=43 --env.episode_length=280 --rename_map --output_dir=/root/outputs/eval/smolvla_spatial_seed43_v2\", \"server\": \"bjb1-18228\", \"seed\": 43, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"checkpoint_path\": \"N/A-killed\", \"log_path\": \"killed-on-bjb1-18228\"}}, \"eval-smolvla-lerobot-object-seed44-v2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.task=libero_object --eval.n_episodes=20 --seed=44 --env.episode_length=280 --rename_map --output_dir=/root/outputs/eval/smolvla_object_seed44_v2\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\", \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/tmp/eval_smolvla_object_seed44_v2.log\"}, \"metrics\": {\"pc_success\": 65, \"n_episodes\": 200, \"eval_s\": 841}}, \"eval-smolvla-lerobot-object-seed43-v2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.task=libero_object --eval.n_episodes=20 --seed=43 --env.episode_length=280 --rename_map --output_dir=/root/outputs/eval/smolvla_object_seed43_v2\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\", \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/tmp/eval_smolvla_object_seed43_v2.log\"}, \"metrics\": {\"pc_success\": 66.5, \"n_episodes\": 200, \"eval_s\": 857.4}}, \"eval-smolvla-lerobot-goal-seed43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.task=libero_goal --eval.n_episodes=20 --seed=43 --env.episode_length=300 --output_dir=/root/outputs/eval/smolvla_goal_seed43\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO-Goal (10 tasks x 20 rollouts)\", \"checkpoint_path\": \"/root/outputs/eval/smolvla_goal_seed43\", \"log_path\": \"/root/outputs/eval/smolvla_goal_seed43/eval.log\"}}, \"eval-smolvla-lerobot-spatial-seed43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.task=libero_spatial --eval.n_episodes=20 --seed=43 --env.episode_length=280 --output_dir=/root/outputs/eval/smolvla_spatial_seed43\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"checkpoint_path\": \"/root/outputs/eval/smolvla_spatial_seed43\", \"log_path\": \"/root/outputs/eval/smolvla_spatial_seed43/eval.log\"}}, \"eval-smolvla-lerobot-object-seed44\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.task=libero_object --eval.n_episodes=20 --seed=44 --env.episode_length=280 --output_dir=/root/outputs/eval/smolvla_object_seed44\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\", \"checkpoint_path\": \"/root/outputs/eval/smolvla_object_seed44\", \"log_path\": \"/root/outputs/eval/smolvla_object_seed44/eval.log\"}}, \"eval-smolvla-lerobot-object-seed43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.task=libero_object --eval.n_episodes=20 --seed=43 --env.episode_length=280 --output_dir=/root/outputs/eval/smolvla_object_seed43\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\", \"checkpoint_path\": \"/root/outputs/eval/smolvla_object_seed43\", \"log_path\": \"/root/outputs/eval/smolvla_object_seed43/eval.log\"}}, \"eval-smolvla-lerobot-spatial-seed44\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 lerobot-eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.task=libero_spatial --eval.n_episodes=20 --seed=44 --env.episode_length=280 --output_dir=/root/outputs/eval/smolvla_spatial_seed44\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"checkpoint_path\": \"/root/outputs/eval/smolvla_spatial_seed44\", \"log_path\": \"/root/outputs/eval/smolvla_spatial_seed44/eval.log\"}, \"metrics\": {\"success_rate\": 0.6, \"n_episodes\": 200, \"n_tasks\": 10, \"per_task_sr\": [0.75, 0.65, 0.75, 0.75, 0.5, 0, 0.9, 0.7, 0.4, 0.6]}}, \"precompute-smolvla-long-wrapper-bjb1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/lerobot_precompute.py --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_smolvla_k10/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_10/\", \"data_count\": 10, \"model_name\": \"smolvla_libero\", \"seed\": 42}}, \"eval-smolvla-lerobot-goal-seed44\": {}, \"eval-smolvla-lerobot-long-seed44\": {\"spec\": {\"command\": \"lerobot-eval --policy.path=smolvla_libero --env.task=libero_10 --eval.n_episodes=20 --seed=44\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla_libero\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_10/\", \"data_count\": 200}, \"metrics\": {\"success_rate\": 49.5, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-long-seed43\": {\"spec\": {\"command\": \"lerobot-eval --policy.path=smolvla_libero --env.task=libero_10 --eval.n_episodes=20 --seed=43\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla_libero\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_10/\", \"data_count\": 200}, \"metrics\": {\"success_rate\": 53.5, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-long-seed42\": {\"spec\": {\"command\": \"lerobot-eval --policy.path=smolvla_libero --env.task=libero_10 --eval.n_episodes=20 --seed=42\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla_libero\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_10/\", \"data_count\": 200}, \"metrics\": {\"success_rate\": 49.5, \"n_episodes\": 200}}, \"train-crm-unified-4suite-r4\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark object spatial goal long --obs_dim 960 --epochs 50 --batch_size 32 --lr 1e-3 --input_mode obs_only --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"model_name\": \"crm_unified_4suite_obs_only\", \"seed\": 42, \"data_count\": 0, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - training run\"}, \"metrics\": {\"epochs_completed\": 13, \"current_epoch\": 14, \"current_batch\": \"2700/6316\", \"total_epochs\": 50, \"last_train_loss\": 0.012, \"checkpoint_latest\": \"checkpoint_epoch0013.pt\", \"checked_at\": \"2026-05-22T01:21Z\", \"note\": \"CRON false alarm - process still running (PID 322367)\"}}, \"eval-pi05-vla-only-long-seed42-r4-rerun\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --model pi05 --benchmark long --seed 42 --n_rollouts 20 --K 10 --n_action_steps 10 --max_steps 520 --output_file logs/eval_long_vla_only_seed42_r4_rerun.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Long\", \"data_count\": 20, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"pi05-pretrained\", \"eval_data\": \"LIBERO-Long\"}, \"metrics\": {\"success_rate\": 0.94, \"successes\": 188, \"total\": 200, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.95, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 1, \"KITCHEN_SCENE3_stove_moka_pot\": 1, \"KITCHEN_SCENE4_black_bowl_drawer\": 1, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.9, \"STUDY_SCENE1_book_in_caddy\": 0.95, \"LIVING_ROOM_SCENE6_mug_pudding\": 1, \"LIVING_ROOM_SCENE1_soup_cream_cheese\": 0.9, \"KITCHEN_SCENE8_both_moka_pots\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave\": 0.9}}}, \"eval-pi05-crm-object-seed44\": {\"spec\": {\"command\": \"TORCHDYNAMO_DISABLE=1 python src/evaluate.py --model pi05 --mode acr_vla --crm_checkpoint crm_best.pt --benchmark object --seed 44 --obs_dim 2048\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": 218700, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed44.log\", \"submitted_at\": \"2026-05-22T01:05:48.729Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"crm-train-pi05-object-full\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05+crm-object\", \"seed\": 44, \"wall_clock_seconds\": 58497.3, \"gpu_hours\": 16.25}}, \"eval-pi05-crm-object-seed43\": {\"spec\": {\"command\": \"TORCHDYNAMO_DISABLE=1 python src/evaluate.py --model pi05 --mode acr_vla --crm_checkpoint crm_best.pt --benchmark object --seed 43 --obs_dim 2048\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"pid\": 218420, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed43.log\", \"submitted_at\": \"2026-05-22T01:05:44.257Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"crm-train-pi05-object-full\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05+crm-object\", \"seed\": 43, \"wall_clock_seconds\": 58491.0, \"gpu_hours\": 16.25}}, \"eval-pi05-crm-object-seed42\": {\"spec\": {\"command\": \"TORCHDYNAMO_DISABLE=1 python src/evaluate.py --model pi05 --mode acr_vla --crm_checkpoint crm_best.pt --benchmark object --seed 42 --obs_dim 2048\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"pid\": 218131, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed42.log\", \"submitted_at\": \"2026-05-22T01:05:39.094Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"crm-train-pi05-object-full\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05+crm-object\", \"seed\": 42, \"wall_clock_seconds\": 58485.8, \"gpu_hours\": 16.25}}, \"eval-pi05-vla-only-long-seed43-r4-std\": {\"spec\": {\"command\": \"N/A - phantom entry\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 43, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}}, \"eval-pi05-vla-only-goal-seed44-r4-std\": {\"spec\": {\"command\": \"N/A - phantom entry\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 44, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}}, \"eval-pi05-vla-only-goal-seed42-r4-std\": {\"spec\": {\"command\": \"N/A - phantom entry\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}}, \"eval-pi05-vla-only-long-seed44-r4-std\": {\"spec\": {\"command\": \"N/A - phantom entry\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 44, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}}, \"eval-pi05-vla-only-goal-seed43-r4-std\": {\"spec\": {\"command\": \"N/A - phantom entry\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 43, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}}, \"eval-pi05-vla-only-goal-seed42-r4\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode vla_only --model pi05 --benchmark goal --seed 42 --n_rollouts 20 --K 10 --n_action_steps 10 --max_steps 300 --output_file logs/eval_goal_vla_only_seed42_r4.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"42259\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-seed42-r4.log\", \"submitted_at\": \"2026-05-22T15:52:45.940Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4167.5, \"gpu_hours\": 1.16}, \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}}, \"precompute-smolvla-long-k2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES={3,4,5} python src/train_crm.py --precompute --benchmark long --K 2 --cache_dir /root/autodl-tmp/crm_cache_v5/ --model smolvla --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --obs_dim 960 --shard_id {0,1,2} --num_shards 3 --precompute_batch_size 4 --save_every 500\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_10/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"SmolVLA-0.4B (smolvla_libero)\", \"seed\": 42, \"cache_output\": \"/root/autodl-tmp/crm_cache_v5/long/\", \"log_path\": \"/tmp/precompute_long_s{0,1,2}.log\", \"gpus\": \"cuda:3, cuda:4, cuda:5\", \"shards\": 3}}, \"train-crm-unified-4suite-r3\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark object spatial goal long --obs_dim 960 --epochs 50 --batch_size 32 --lr 1e-3 --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_unified_4suite/ --input_mode obs_only\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 224555, \"model_name\": \"CRM-unified-obs_only\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite/train.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite/\", \"gpu\": \"cuda:3\", \"tmux_session\": \"train-crm-unified-r3\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"crm_cache_v5 (4 suites: object/spatial/goal/long, K=10)\"}}, \"train-crm-unified-4suite-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark object spatial goal long --obs_dim 960 --epochs 50 --batch_size 32 --lr 1e-3 --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_unified_4suite/\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 224555, \"model_name\": \"CRM (hidden_dim=256, input_mode=full, obs_dim=960)\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training, not eval)\"}}, \"precompute-smolvla-goal-bjb2-28827\": {\"spec\": {\"command\": \"python src/train_crm.py --precompute --benchmark goal --K 10 --cache_dir /root/autodl-tmp/crm_cache_k10/\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:4\", \"pid\": 204643, \"data_path\": \"/root/autodl-tmp/libero_data/libero_goal/\", \"data_count\": \"61728 samples\", \"model_name\": \"smolvla\", \"seed\": 42}}, \"precompute-smolvla-long-bjb2-28827\": {\"spec\": {\"command\": \"python src/train_crm.py --precompute --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_k10/\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"pid\": 203764, \"data_path\": \"/root/autodl-tmp/libero_data/libero_10/\", \"data_count\": \"136090 samples\", \"model_name\": \"smolvla\", \"seed\": 42}}, \"eval-pi05-vla-only-spatial-seed44-r4\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20 --K 10 --n_action_steps 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-pi05-vla-only-spatial-seed43-r4\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20 --K 10 --n_action_steps 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-pi05-vla-only-spatial-seed42-r4\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20 --K 10 --n_action_steps 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-pi05-vla-only-long-seed44-r4\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=2 python evaluate.py --mode vla_only --model pi05 --benchmark long --seed 44 --n_action_steps 10 --max_steps 520 --n_rollouts 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"41914\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-long-seed44-r4.log\", \"submitted_at\": \"2026-05-22T15:52:31.653Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": \"10 tasks × 50 trials\", \"model_name\": \"pi0.5\", \"seed\": 44, \"wall_clock_seconds\": 3034.2, \"gpu_hours\": 0.84}, \"metrics\": {\"success_rate\": 0.955}}, \"eval-pi05-vla-only-long-seed43-r4\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode vla_only --model pi05 --benchmark long --seed 43 --n_rollouts 20 --K 10 --n_action_steps 10 --max_steps 520 --output_file logs/eval_long_vla_only_seed43_r4.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"41632\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-long-seed43-r4.log\", \"submitted_at\": \"2026-05-22T15:52:18.929Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3030.8, \"gpu_hours\": 0.84}, \"metrics\": {\"success_rate\": 0.955}}, \"eval-pi05-vla-only-goal-seed44-r4\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=5 python evaluate.py --mode vla_only --model pi05 --benchmark goal --seed 44 --n_action_steps 10 --max_steps 300 --n_rollouts 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"466238\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-seed44-r4.log\", \"submitted_at\": \"2026-05-22T15:52:03.322Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": \"10 tasks × 50 trials\", \"model_name\": \"pi0.5\", \"seed\": 44, \"wall_clock_seconds\": 1906.7, \"gpu_hours\": 0.53}, \"metrics\": {\"success_rate\": 0.975, \"successes\": 195, \"total\": 200}}, \"eval-pi05-vla-only-goal-seed43-r4\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=4 python evaluate.py --mode vla_only --model pi05 --benchmark goal --seed 43 --n_action_steps 10 --max_steps 300 --n_rollouts 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"465874\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-goal-seed43-r4.log\", \"submitted_at\": \"2026-05-22T15:51:50.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": \"10 tasks × 50 trials\", \"model_name\": \"pi0.5\", \"seed\": 43, \"wall_clock_seconds\": 1911.3, \"gpu_hours\": 0.53}, \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}}, \"eval-pi05-vla-only-long-seed42-r4-std\": {}, \"precompute-smolvla-goal-k10\": {\"spec\": {\"command\": \"bash -c \\\"while kill -0 249393 2>/dev/null; do sleep 10; done; sleep 5; cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/lerobot_precompute.py --benchmark goal --K 10 --cache_dir /root/autodl-tmp/crm_cache_smolvla_k10/ 2>&1 | tee /root/runs/acr-vla-conformal-refinement/precompute-smolvla-goal.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"299301\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-smolvla-goal-k10.log\", \"submitted_at\": \"2026-05-22T15:48:21.784Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-smolvla-spatial-k10\": {\"spec\": {\"command\": \"bash -c \\\"while kill -0 249256 2>/dev/null; do sleep 10; done; sleep 5; cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/lerobot_precompute.py --benchmark spatial --K 10 --cache_dir /root/autodl-tmp/crm_cache_smolvla_k10/ 2>&1 | tee /root/runs/acr-vla-conformal-refinement/precompute-smolvla-spatial.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"299065\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-smolvla-spatial-k10.log\", \"submitted_at\": \"2026-05-22T15:48:02.014Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-smolvla-object-k10\": {\"spec\": {\"command\": \"bash -c \\\"while kill -0 249181 2>/dev/null; do sleep 10; done; sleep 5; cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/lerobot_precompute.py --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_smolvla_k10/ 2>&1 | tee /root/runs/acr-vla-conformal-refinement/precompute-smolvla-object.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"298669\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-smolvla-object-k10.log\", \"submitted_at\": \"2026-05-22T15:47:29.485Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-long-seed2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python src/evaluate.py --mode vla_only --benchmark long --seed 2 --n_rollouts 10 --output_file logs/eval_long_vla_only_seed2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"233564\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-long-seed2.log\", \"submitted_at\": \"2026-05-22T14:19:47.701Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-long-seed1\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python src/evaluate.py --mode vla_only --benchmark long --seed 1 --n_rollouts 10 --output_file logs/eval_long_vla_only_seed1.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"232884\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-long-seed1.log\", \"submitted_at\": \"2026-05-22T14:19:41.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-long-seed0\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python src/evaluate.py --mode vla_only --benchmark long --seed 0 --n_rollouts 10 --output_file logs/eval_long_vla_only_seed0.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"232609\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-long-seed0.log\", \"submitted_at\": \"2026-05-22T14:19:36.630Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-openvla-oft-official-object\": {\"spec\": {\"command\": \"conda activate /root/autodl-tmp/envs/openvla-oft && python experiments/robot/libero/run_libero_eval.py --model_family openvla-oft --pretrained_checkpoint /root/autodl-tmp/models/openvla-oft/object/ --task_suite_name libero_object --num_trials_per_task 50 --seed 7\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/eval_results/openvla-oft-official/eval_output.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 500, \"model_name\": \"openvla-7b-oft-finetuned-libero-object\", \"seed\": 7}}, \"eval-pi05-crm-spatial-seed44\": {\"spec\": {\"command\": \"TORCHDYNAMO_DISABLE=1 python src/evaluate.py --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_full/spatial/crm_best.pt --benchmark spatial --seed 44 --obs_dim 2048\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"149307\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-spatial-seed44.log\", \"submitted_at\": \"2026-05-22T01:17:33.445Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:2\"], \"tmux_session\": \"eval-pi05-crm-spatial-seed44\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"crm-train-pi05-spatial-v2\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"wall_clock_seconds\": 43345.0, \"gpu_hours\": 12.04}}, \"eval-pi05-crm-spatial-seed43\": {\"spec\": {\"command\": \"TORCHDYNAMO_DISABLE=1 python src/evaluate.py --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_full/spatial/crm_best.pt --benchmark spatial --seed 43 --obs_dim 2048\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"149025\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-spatial-seed43.log\", \"submitted_at\": \"2026-05-22T01:17:28.916Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:1\"], \"tmux_session\": \"eval-pi05-crm-spatial-seed43\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"crm-train-pi05-spatial-v2\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"wall_clock_seconds\": 43309.0, \"gpu_hours\": 12.03}}, \"eval-pi05-crm-spatial-seed42\": {\"spec\": {\"command\": \"TORCHDYNAMO_DISABLE=1 python src/evaluate.py --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_full/spatial/crm_best.pt --benchmark spatial --seed 42 --obs_dim 2048\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"148748\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-spatial-seed42.log\", \"submitted_at\": \"2026-05-22T01:17:24.505Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:0\"], \"tmux_session\": \"eval-pi05-crm-spatial-seed42\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"crm-train-pi05-spatial-v2\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"wall_clock_seconds\": 43270.5, \"gpu_hours\": 12.02}}, \"eval-pi05-vla-only-object-seed43-r4\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --K 10 --n_action_steps 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_pi05_seed43_r4.log\", \"pid\": 905874, \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"success_rate\": 98.5, \"total_successes\": 197, \"total_episodes\": 200}}, \"eval-pi05-vla-only-object-seed44-r4\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --K 10 --n_action_steps 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_pi05_seed44_r4.log\", \"pid\": 906424, \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"success_rate\": 99.5, \"total_successes\": 199, \"total_episodes\": 200}}, \"eval-smolvla-lerobot-official-object\": {\"spec\": {\"command\": \"python -m lerobot.scripts.lerobot_eval --policy.path=/root/autodl-tmp/models/smolvla_libero --env.type=libero --env.task=libero_object --eval.n_episodes=20 --eval.batch_size=1 --policy.device=cuda\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla_libero\", \"data_path\": \"libero_object\", \"data_count\": 20, \"seed\": 1000, \"checkpoint_path\": \"/root/autodl-tmp/models/smolvla_libero\", \"log_path\": \"/tmp/lerobot_eval_object2.log\"}}, \"eval-pi05-vla-only-object-seed42-r4\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --K 10 --n_action_steps 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_pi05_seed42_r4.log\", \"pid\": 905242, \"checkpoint_path\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\"}, \"metrics\": {\"success_rate\": 100, \"total_success\": 200, \"total_rollouts\": 200, \"n_action_steps\": 10, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 100, \"bbq_sauce\": 100, \"ketchup\": 100, \"tomato_sauce\": 100, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 100, \"orange_juice\": 100}}}, \"train-crm-unified-4suite\": {\"spec\": {\"command\": \"python src/train_crm.py --benchmark object spatial goal long --obs_dim 960 --epochs 50 --batch_size 32 --lr 1e-3 --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_unified_4suite/\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 882598, \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-unified-4suite.log\", \"submitted_at\": \"2026-05-22T08:57:47.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/{object,spatial,goal,long}/\", \"data_count\": \"224555 samples (4 suites merged)\", \"model_name\": \"CRM-unified-4suite (input_mode=full, obs_dim=960, hidden_dim=256)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite/crm_best.pt\"}, \"metrics\": {\"completed_epochs\": 4, \"target_epochs\": 50, \"exit_code\": 124, \"failure_reason\": \"timeout (EXIT_CODE=124) — killed after 4/50 epochs (~2.3 GPU hours)\", \"best_val_loss\": 0.009633, \"best_epoch\": 4, \"training_curve\": [{\"epoch\": 1, \"train_loss\": 0.019467, \"val_loss\": 0.010801, \"lr\": \"9.99e-04\"}, {\"epoch\": 2, \"train_loss\": 0.018024, \"val_loss\": 0.010438, \"lr\": \"9.96e-04\"}, {\"epoch\": 3, \"train_loss\": 0.017237, \"val_loss\": 0.009901, \"lr\": \"9.91e-04\"}, {\"epoch\": 4, \"train_loss\": 0.01663, \"val_loss\": 0.009633, \"lr\": \"9.84e-04\"}]}}, \"precompute-smolvla-long-bjb1-32546-r2\": {\"spec\": {\"command\": \"python -u src/train_crm.py --precompute --benchmark long --K 2 --cache_dir /root/autodl-tmp/crm_cache_v5/ --model smolvla --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --obs_dim 960 --precompute_batch_size 4 --save_every 500\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/long\", \"data_count\": 136090, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"long\"}}, \"precompute-smolvla-long-bjb1-32546\": {\"spec\": {\"command\": \"python src/train_crm.py --precompute --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_k10/\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"pid\": 278590, \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-smolvla-long-bjb1-32546.log\", \"submitted_at\": \"2026-05-22T06:37:03.834Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_10/\", \"data_count\": \"136090 samples\", \"model_name\": \"smolvla\", \"seed\": 42, \"conclusion\": \"failed\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 16474.1, \"gpu_hours\": 4.58}}, \"eval-loss-perdof-object-seed42\": {\"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"857640\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-perdof-object-seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt\", \"submitted_at\": \"2026-05-22T06:45:31.934Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-perdof\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 14028.6, \"gpu_hours\": 3.9}, \"metrics\": {\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"milk\": 5, \"chocolate_pudding\": 5, \"orange_juice\": 5}}}, \"eval-loss-combined-object-seed42\": {\"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"265357\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log\", \"submitted_at\": \"2026-05-22T06:45:41.486Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_combined\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-combined\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 14139.1, \"gpu_hours\": 3.93}, \"metrics\": {\"avg_success_rate\": 9, \"total_successes\": 18, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 10, \"salad_dressing\": 10, \"bbq_sauce\": 15, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 5, \"milk\": 10, \"chocolate_pudding\": 25, \"orange_juice\": 10}}}, \"eval-loss-conformal-object-seed42\": {\"spec\": {\"command\": \"python evaluate.py --benchmark object --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log\", \"checkpoint_source\": \"train-loss-conformal\", \"eval_data\": \"LIBERO-object\", \"seed\": 42, \"model_name\": \"smolvla+conformal_crm\", \"data_path\": \"LIBERO-object\"}, \"metrics\": {\"success_rate\": 6, \"total_successes\": 12, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 10, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 0, \"milk\": 10, \"chocolate_pudding\": 20, \"orange_juice\": 10}}}, \"eval-loss-mse-object-seed42\": {\"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/mse/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"857356\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-mse-object-seed42.log\", \"submitted_at\": \"2026-05-22T06:45:27.218Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_mse\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-mse-baseline\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/mse/crm_best.pt\", \"wall_clock_seconds\": 13241.2, \"gpu_hours\": 3.68}, \"metrics\": {\"avg_success_rate\": 7, \"total_successes\": 14, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 10, \"ketchup\": 5, \"tomato_sauce\": 15, \"butter\": 10, \"milk\": 15, \"chocolate_pudding\": 5, \"orange_juice\": 0}}}, \"eval-openvla-oft-object-baseline-seed42\": {\"spec\": {\"command\": \"python src/evaluate.py --model openvla_oft --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --obs_dim 4096\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"pid\": 925107, \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": \"10 tasks x 20 rollouts = 200 episodes\", \"model_name\": \"openvla-oft-7b\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-openvla-oft-object-seed42.log\"}, \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": \"all 10 tasks 0.0%\", \"n_rollouts\": 20, \"total_episodes\": 200}}, \"precompute-pi05-long-bjb1-18228\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python src/train_crm.py --precompute --benchmark long --K 10 --model pi05 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --shard_id 0 --num_shards 1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"883206\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-long-bjb1-18228.log\", \"submitted_at\": \"2026-05-22T09:00:16.701Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-smolvla-long-bjb1-18228\": {\"spec\": {\"command\": \"python src/train_crm.py --precompute --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_v5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"855753\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-smolvla-long-bjb1-18228.log\", \"submitted_at\": \"2026-05-22T06:37:26.905Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/long\", \"data_count\": 136090, \"model_name\": \"SmolVLA\", \"seed\": 42, \"wall_clock_seconds\": 8365.9, \"gpu_hours\": 2.32}, \"metrics\": {\"n_samples\": 136090, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5, \"obs_features_shape\": [136090, 960], \"k_samples_shape\": [136090, 10, 5, 6], \"expert_actions_shape\": [136090, 5, 6], \"total_time_sec\": 8021, \"speed\": \"0.06s/sample\"}}, \"precompute-pi05-goal-bjb2-28827-s2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python src/train_crm.py --precompute --benchmark goal --K 10 --model pi05 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --shard_id 2 --num_shards 3\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"206549\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-goal-bjb2-28827-s2.log\", \"submitted_at\": \"2026-05-22T08:03:26.321Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-goal-bjb2-28827-s1\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python src/train_crm.py --precompute --benchmark goal --K 10 --model pi05 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --shard_id 1 --num_shards 3\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"206270\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-goal-bjb2-28827-s1.log\", \"submitted_at\": \"2026-05-22T08:03:21.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-goal-bjb2-28827-s0\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python src/train_crm.py --precompute --benchmark goal --K 10 --model pi05 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --shard_id 0 --num_shards 3\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"206123\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-goal-bjb2-28827-s0.log\", \"submitted_at\": \"2026-05-22T08:03:17.284Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"crm-loss-combined\": {\"spec\": {\"command\": \"python src/train_crm.py --benchmark object --loss_type combined --lambda_conf 0.1 --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 960\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"845729\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-loss-combined.log\", \"submitted_at\": \"2026-05-22T05:03:04.572Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 14570, \"model_name\": \"CRM_combined\", \"seed\": 42, \"wall_clock_seconds\": 6739.4, \"gpu_hours\": 1.87}, \"metrics\": {\"best_val_loss\": 0.005302, \"final_train_loss\": 0.004481, \"best_epoch\": 48, \"epochs\": 50, \"vs_mse\": \"2.5x worse\", \"vs_perdof\": \"43x worse\", \"dof_weight_range\": [0.0107, 3.7318]}}, \"crm-loss-conformal\": {\"spec\": {\"command\": \"python src/train_crm.py --benchmark object --loss_type conformal_guided --lambda_conf 0.1 --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 960\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"845499\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-loss-conformal.log\", \"submitted_at\": \"2026-05-22T05:02:54.937Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 14570, \"model_name\": \"CRM_conformal_guided\", \"seed\": 42, \"wall_clock_seconds\": 5342.6, \"gpu_hours\": 1.48}, \"metrics\": {\"best_val_loss\": 0.013343, \"final_train_loss\": 0.016046, \"epochs\": 50, \"vs_mse\": \"6.4x worse\"}}, \"precompute-smolvla-goal-bjb1-18228\": {\"spec\": {\"command\": \"python src/train_crm.py --precompute --benchmark goal --K 10 --cache_dir /root/autodl-tmp/crm_cache_v5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"855590\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-smolvla-goal-bjb1-18228.log\", \"submitted_at\": \"2026-05-22T06:37:16.505Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_goal\", \"data_count\": 61728, \"model_name\": \"SmolVLA\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/goal/\", \"wall_clock_seconds\": 3370.1, \"gpu_hours\": 0.94}, \"metrics\": {\"n_samples\": 61728, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5}}, \"crm-loss-perdof\": {\"spec\": {\"command\": \"python src/train_crm.py --benchmark object --loss_type perdof_weighted --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 960\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"845281\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-loss-perdof.log\", \"submitted_at\": \"2026-05-22T05:02:50.428Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 14570, \"model_name\": \"CRM_perdof_weighted\", \"seed\": 42, \"wall_clock_seconds\": 5575.7, \"gpu_hours\": 1.55}, \"metrics\": {\"best_val_loss\": 0.000124, \"final_train_loss\": 0.000141, \"best_epoch\": 50, \"total_epochs\": 50, \"dof_weight_min\": 0.0107, \"dof_weight_max\": 3.7318, \"mse_baseline_val_loss\": 0.00208, \"conformal_guided_val_loss\": 0.013343, \"samples\": 14570, \"crm_params\": 337438}}, \"crm-loss-mse-baseline\": {\"spec\": {\"command\": \"python src/train_crm.py --benchmark object --loss_type mse --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 960\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"845069\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-loss-mse-baseline.log\", \"submitted_at\": \"2026-05-22T05:02:45.750Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 14570, \"model_name\": \"CRM_MSE_baseline\", \"seed\": 42, \"wall_clock_seconds\": 5341.6, \"gpu_hours\": 1.48}, \"metrics\": {\"best_val_loss\": 0.00208, \"final_train_loss\": 0.004038, \"best_epoch\": 50, \"total_epochs\": 50, \"initial_val_loss\": 0.008373, \"exit_code\": 0}}, \"eval-smolvla-acr-goal-seed43\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark goal --n_rollouts 20 --seed 43 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_goal_acr_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"pid\": 243748, \"data_path\": \"LIBERO-Goal (libero pkg)\", \"data_count\": \"10 tasks x 20 rollouts\", \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-smolvla-acr-goal-seed43.log\", \"output_file\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_acr_seed43.json\"}}, \"eval-smolvla-crm-long-seed44-v2\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark long --n_rollouts 20 --seed 44 --K 2 --crm_checkpoint crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"172552\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-smolvla-crm-long-seed44-v2.log\", \"submitted_at\": \"2026-05-22T05:12:34.263Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM_acr_vla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO-Long (10 tasks x 20 rollouts)\", \"wall_clock_seconds\": 2562.8, \"gpu_hours\": 0.71}}, \"eval-smolvla-crm-goal-seed44-v2\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark goal --n_rollouts 20 --seed 44 --K 2 --crm_checkpoint crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"171949\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-smolvla-crm-goal-seed44-v2.log\", \"submitted_at\": \"2026-05-22T05:12:26.468Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM_acr_vla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 20 rollouts)\", \"wall_clock_seconds\": 2564.1, \"gpu_hours\": 0.71}}, \"eval-smolvla-crm-long-seed43-v2\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark long --n_rollouts 20 --seed 43 --K 2 --crm_checkpoint crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"171674\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-smolvla-crm-long-seed43-v2.log\", \"submitted_at\": \"2026-05-22T05:12:20.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM_acr_vla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO-Long (10 tasks x 20 rollouts)\", \"wall_clock_seconds\": 2563.7, \"gpu_hours\": 0.71}}, \"eval-smolvla-acr-long-seed42\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark long --n_rollouts 20 --seed 42 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_long_acr_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 243677, \"data_path\": \"LIBERO-Long (libero pkg)\", \"data_count\": \"10 tasks x 20 rollouts\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"libero_10 (Long)\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-smolvla-acr-long-seed42.log\", \"output_file\": \"/root/acr-vla-conformal-refinement/logs/eval_long_acr_seed42.json\"}, \"metrics\": {\"failure_reason\": \"RuntimeError: state_dict shape mismatch in CRM checkpoint. input_mean/input_std: [990] vs [1030], net.0.weight: [256,990] vs [256,1030]. CRM checkpoint (crm_v3_norm/obs_only/crm_best.pt) was trained with obs_dim=960 but model now expects obs_dim=1000.\"}}, \"eval-smolvla-acr-goal-seed42\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark goal --n_rollouts 20 --seed 42 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_goal_acr_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"pid\": 243608, \"data_path\": \"LIBERO-Goal (libero pkg)\", \"data_count\": \"10 tasks x 20 rollouts\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-smolvla-acr-goal-seed42.log\", \"output_file\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_acr_seed42.json\"}}, \"eval-smolvla-crm-long-seed44\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py --mode acr_vla --benchmark long --n_rollouts 20 --seed 44 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"170200\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-smolvla-crm-long-seed44.log\", \"submitted_at\": \"2026-05-22T05:10:40.364Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-smolvla-crm-long-seed43\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py --mode acr_vla --benchmark long --n_rollouts 20 --seed 43 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"169645\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-smolvla-crm-long-seed43.log\", \"submitted_at\": \"2026-05-22T05:10:31.278Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"crm-train-pi05-spatial-v2\": {\"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_pi05/spatial --output_dir /root/autodl-tmp/checkpoints/crm_pi05_full/spatial --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 2048\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 805017, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05/spatial/\", \"data_count\": 60250, \"model_name\": \"crm-pi05-spatial-full\", \"seed\": 42, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-pi05-spatial-v2.log\"}, \"metrics\": {\"val_loss\": 0.006138, \"best_epoch\": 50, \"total_epochs\": 50}}, \"crm-train-pi05-object-full\": {\"spec\": {\"command\": \"nohup env CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_pi05/ --output_dir /root/autodl-tmp/checkpoints/crm_pi05_full/object/ --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 2048\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 800111, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05/object/\", \"data_count\": 69303, \"model_name\": \"crm-pi05-object-full\", \"seed\": 42, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-pi05-object-full.log\"}, \"metrics\": {\"val_loss\": 0.004018, \"best_epoch\": 50, \"total_epochs\": 50}}, \"crm-train-pi05-spatial\": {\"spec\": {\"command\": \"nohup python src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_pi05/ --output_dir /root/autodl-tmp/checkpoints/crm_pi05/spatial/ --epochs 50 --batch_size 32 --obs_dim 2048\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 795051, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05/spatial/\", \"data_count\": 38500, \"model_name\": \"crm-pi05-spatial\", \"seed\": 42, \"checkpoint_path\": \"N/A - incomplete data, pipeline validation only\", \"log_path\": \"N/A\"}}, \"crm-train-pi05-object\": {\"spec\": {\"command\": \"nohup python src/train_crm.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_pi05/ --output_dir /root/autodl-tmp/checkpoints/crm_pi05/object/ --epochs 50 --batch_size 32 --obs_dim 2048\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 795874, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05/object/\", \"data_count\": 49700, \"model_name\": \"crm-pi05-object\", \"seed\": 42, \"checkpoint_path\": \"N/A - incomplete data, pipeline validation only\", \"log_path\": \"N/A\"}}, \"crm-pipeline-auto\": {\"spec\": {\"command\": \"bash -c \\\"\\nset -e\\n\\necho '[pipeline] Starting auto CRM pipeline monitor at $(date)'\\necho '[pipeline] Will poll precompute progress every 5 min, then auto-execute merge + training'\\n\\n# === PHASE 1: Wait for all precompute to finish ===\\necho '[pipeline] Phase 1: Monitoring precompute completion...'\\n\\nwhile true; do\\n    # Check bjb1-32546 (Object s1-s9)\\n    OBJ_PROCS=\\\\$(ssh bjb1-32546 'ps aux | grep train_crm | grep precompute | grep -v grep | wc -l' 2>/dev/null || echo 0)\\n    # Check bjb2-40593 (Object s0)  \\n    OBJ0_PROCS=\\\\$(ssh bjb2-40593 'ps aux | grep train_crm | grep precompute | grep -v grep | wc -l' 2>/dev/null || echo 0)\\n    # Check bjb2-28827 (Spatial s0-s5)\\n    SPA_PROCS=\\\\$(ssh bjb2-28827 'ps aux | grep train_crm | grep precompute | grep -v grep | wc -l' 2>/dev/null || echo 0)\\n    # Check local (Spatial s6)\\n    SPA6_PROCS=\\\\$(ps aux | grep train_crm | grep precompute | grep -v grep | wc -l)\\n    \\n    TOTAL=\\\\$((OBJ_PROCS + OBJ0_PROCS + SPA_PROCS + SPA6_PROCS))\\n    echo \\\\\\\"[pipeline] \\\\$(date): precompute processes remaining: bjb1-32546=\\\\${OBJ_PROCS} bjb2-40593=\\\\${OBJ0_PROCS} bjb2-28827=\\\\${SPA_PROCS} local=\\\\${SPA6_PROCS} total=\\\\${TOTAL}\\\\\\\"\\n    \\n    if [ \\\\\\\"\\\\$TOTAL\\\\\\\" -eq 0 ]; then\\n        echo '[pipeline] All precompute processes finished!'\\n        break\\n    fi\\n    \\n    sleep 300\\ndone\\n\\n# === PHASE 2: Clean old partials on bjb1-18228 ===\\necho '[pipeline] Phase 2: Cleaning old object partials on bjb1-18228...'\\nrm -f /root/autodl-tmp/crm_cache_pi05/object/partial_s*.pt\\nrm -f /root/autodl-tmp/crm_cache_pi05/object/obs_features.pt /root/autodl-tmp/crm_cache_pi05/object/k_samples.pt /root/autodl-tmp/crm_cache_pi05/object/expert_actions.pt /root/autodl-tmp/crm_cache_pi05/object/manifest.json\\necho '[pipeline] Old partials cleaned'\\n\\n# === PHASE 3: rsync all shard caches to bjb1-18228 ===\\necho '[pipeline] Phase 3: Rsyncing all shard caches...'\\n\\n# Object shard 0 from bjb2-40593\\necho '[pipeline] rsync Object s0 from bjb2-40593...'\\nrsync -av bjb2-40593:/root/autodl-tmp/crm_cache_pi05/object/partial_s0_*.pt /root/autodl-tmp/crm_cache_pi05/object/\\necho '[pipeline] Object s0 done'\\n\\n# Object shards 1-9 from bjb1-32546\\necho '[pipeline] rsync Object s1-9 from bjb1-32546...'\\nrsync -av bjb1-32546:/root/autodl-tmp/crm_cache_pi05/object/partial_s*.pt /root/autodl-tmp/crm_cache_pi05/object/\\necho '[pipeline] Object s1-9 done'\\n\\n# Spatial shards 0-5 from bjb2-28827\\necho '[pipeline] rsync Spatial s0-5 from bjb2-28827...'\\nrsync -av bjb2-28827:/root/autodl-tmp/crm_cache_pi05/spatial/partial_s*.pt /root/autodl-tmp/crm_cache_pi05/spatial/\\necho '[pipeline] Spatial s0-5 done'\\n# Spatial s6 already local\\n\\necho '[pipeline] rsync complete. File counts:'\\nls /root/autodl-tmp/crm_cache_pi05/object/partial_s*.pt 2>/dev/null | wc -l\\nls /root/autodl-tmp/crm_cache_pi05/spatial/partial_s*.pt 2>/dev/null | wc -l\\n\\n# === PHASE 4: Merge ===\\necho '[pipeline] Phase 4: Merge...'\\ncd /root/acr-vla-conformal-refinement\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\n\\n# Dry-run first\\necho '[pipeline] Object merge dry-run...'\\npython scripts/merge_precompute_cache.py --cache_dir /root/autodl-tmp/crm_cache_pi05/object --num_shards 10 --dry_run\\n\\necho '[pipeline] Spatial merge dry-run...'\\npython scripts/merge_precompute_cache.py --cache_dir /root/autodl-tmp/crm_cache_pi05/spatial --num_shards 7 --dry_run\\n\\n# Actual merge\\necho '[pipeline] Object merge...'\\npython scripts/merge_precompute_cache.py --cache_dir /root/autodl-tmp/crm_cache_pi05/object --num_shards 10\\n\\necho '[pipeline] Spatial merge...'\\npython scripts/merge_precompute_cache.py --cache_dir /root/autodl-tmp/crm_cache_pi05/spatial --num_shards 7\\n\\n# Verify merge output\\necho '[pipeline] Merge verification:'\\nls -la /root/autodl-tmp/crm_cache_pi05/object/{obs_features.pt,k_samples.pt,expert_actions.pt,manifest.json}\\nls -la /root/autodl-tmp/crm_cache_pi05/spatial/{obs_features.pt,k_samples.pt,expert_actions.pt,manifest.json}\\npython -c \\\\\\\"import torch; o=torch.load('/root/autodl-tmp/crm_cache_pi05/object/obs_features.pt',weights_only=True); print('Object obs:', o.shape)\\\\\\\"\\npython -c \\\\\\\"import torch; s=torch.load('/root/autodl-tmp/crm_cache_pi05/spatial/obs_features.pt',weights_only=True); print('Spatial obs:', s.shape)\\\\\\\"\\n\\necho '[pipeline] Phase 4 complete!'\\necho '[pipeline] CRM training will be started by separate jobs on cuda:0 and cuda:1'\\necho '[pipeline] DONE at $(date)'\\n\\\"\\n\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"790737\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-pipeline-auto.log\", \"submitted_at\": \"2026-05-21T16:37:33.143Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s6-r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 6 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"182283\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s6-r2.log\", \"submitted_at\": \"2026-05-21T15:04:31.010Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s9-r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 9 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"783655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s9-r2.log\", \"submitted_at\": \"2026-05-21T14:19:38.235Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s8-r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 8 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"783507\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s8-r2.log\", \"submitted_at\": \"2026-05-21T14:19:33.986Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s7-r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 7 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"783362\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s7-r2.log\", \"submitted_at\": \"2026-05-21T14:19:29.613Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s0-r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 0 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"878484\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s0-r2.log\", \"submitted_at\": \"2026-05-21T14:19:25.216Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s5-r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 5 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"179280\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s5-r2.log\", \"submitted_at\": \"2026-05-21T14:19:20.929Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s4-r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 4 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"178931\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s4-r2.log\", \"submitted_at\": \"2026-05-21T14:19:16.602Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s3-r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 3 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"178652\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s3-r2.log\", \"submitted_at\": \"2026-05-21T14:19:11.761Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s2-r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 2 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"178505\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s2-r2.log\", \"submitted_at\": \"2026-05-21T14:19:07.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s1-r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 1 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"178356\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s1-r2.log\", \"submitted_at\": \"2026-05-21T14:19:03.162Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s9-fix\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 9 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --save_every 100\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"176442\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s9-fix.log\", \"submitted_at\": \"2026-05-21T14:05:25.745Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s8-fix\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 8 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --save_every 100\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"176097\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s8-fix.log\", \"submitted_at\": \"2026-05-21T14:05:20.949Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s7-fix\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 7 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --save_every 100\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"175818\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s7-fix.log\", \"submitted_at\": \"2026-05-21T14:05:16.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s6-fix\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 6 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --save_every 100\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"175671\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s6-fix.log\", \"submitted_at\": \"2026-05-21T14:05:11.879Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s5-fix\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 5 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --save_every 100\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"175522\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s5-fix.log\", \"submitted_at\": \"2026-05-21T14:05:07.337Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-shard9\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 9 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"173849\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-shard9.log\", \"submitted_at\": \"2026-05-21T13:50:28.123Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-shard8\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 8 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"173507\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-shard8.log\", \"submitted_at\": \"2026-05-21T13:50:23.574Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-shard7\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 7 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"173224\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-shard7.log\", \"submitted_at\": \"2026-05-21T13:50:19.119Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-shard6\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 6 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"173077\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-shard6.log\", \"submitted_at\": \"2026-05-21T13:50:14.476Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-shard5\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 5 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"172930\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-shard5.log\", \"submitted_at\": \"2026-05-21T13:50:09.940Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard6\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 6 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"781275\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard6.log\", \"submitted_at\": \"2026-05-21T13:46:12.692Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard5\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 5 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"101845\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard5.log\", \"submitted_at\": \"2026-05-21T13:46:07.228Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard4\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 4 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"101566\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard4.log\", \"submitted_at\": \"2026-05-21T13:46:02.116Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard3\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 3 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"101227\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard3.log\", \"submitted_at\": \"2026-05-21T13:45:55.961Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 2 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"100880\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard2.log\", \"submitted_at\": \"2026-05-21T13:45:49.296Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard1\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 1 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"100538\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard1.log\", \"submitted_at\": \"2026-05-21T13:45:43.800Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard0\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 0 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"100391\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard0.log\", \"submitted_at\": \"2026-05-21T13:45:37.963Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard0\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 0 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"876712\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard0.log\", \"submitted_at\": \"2026-05-21T13:44:33.853Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard9\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 9 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"780274\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard9.log\", \"submitted_at\": \"2026-05-21T13:42:54.650Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard8\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 8 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"779995\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard8.log\", \"submitted_at\": \"2026-05-21T13:42:49.363Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard7\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 7 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"779846\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard7.log\", \"submitted_at\": \"2026-05-21T13:42:44.324Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard6\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 6 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"171752\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard6.log\", \"submitted_at\": \"2026-05-21T13:42:38.931Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard5\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 5 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"171537\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard5.log\", \"submitted_at\": \"2026-05-21T13:42:33.909Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard4\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 4 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"171195\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard4.log\", \"submitted_at\": \"2026-05-21T13:42:28.892Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard3\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 3 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"170840\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard3.log\", \"submitted_at\": \"2026-05-21T13:42:22.597Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 2 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"170561\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard2.log\", \"submitted_at\": \"2026-05-21T13:42:16.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard1\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 1 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"170414\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard1.log\", \"submitted_at\": \"2026-05-21T13:42:11.409Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-vla-only-spatial-seed45\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 45 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"78040\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed45.log\", \"submitted_at\": \"2026-05-21T11:52:40.865Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"200 (10x20)\", \"model_name\": \"pi0.5\", \"seed\": 45, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 1812.4, \"gpu_hours\": 0.5}, \"metrics\": {\"success_rate\": 0.85, \"n_tasks\": 10, \"total_rollouts\": 200}}, \"eval-pi05-vla-only-spatial-seed43-r3\": {\"spec\": {\"command\": \"bash -c \\\"...pi05 vla_only spatial seed43...\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"77759\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed43-r3.log\", \"submitted_at\": \"2026-05-21T11:52:35.481Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"200 (10x20)\", \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 1810.6, \"gpu_hours\": 0.5}, \"metrics\": {\"success_rate\": 0.83, \"n_tasks\": 10, \"total_rollouts\": 200}}, \"eval-pi05-vla-only-spatial-seed42-r3\": {\"spec\": {\"command\": \"bash -c \\\"...pi05 vla_only spatial seed42...\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"77420\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed42-r3.log\", \"submitted_at\": \"2026-05-21T11:52:31.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"200 (10x20)\", \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 1803.6, \"gpu_hours\": 0.5}, \"metrics\": {\"success_rate\": 0.845, \"n_tasks\": 10, \"total_rollouts\": 200}}, \"eval-pi05-vla-only-object-seed44-r3\": {\"spec\": {\"command\": \"bash -c \\\"...pi05 vla_only object seed44...\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"77064\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44-r3.log\", \"submitted_at\": \"2026-05-21T11:52:26.133Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"200 (10x20)\", \"model_name\": \"pi0.5\", \"seed\": 44, \"checkpoint_path\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"wall_clock_seconds\": 1793.3, \"gpu_hours\": 0.5}, \"metrics\": {\"success_rate\": 0.81, \"n_tasks\": 10, \"total_rollouts\": 200}}, \"eval-pi05-vla-only-object-seed43-r3\": {\"spec\": {\"command\": \"bash -c \\\"...pi05 vla_only object seed43...\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"76780\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43-r3.log\", \"submitted_at\": \"2026-05-21T11:52:19.812Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"200 (10x20)\", \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_path\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"wall_clock_seconds\": 1788.5, \"gpu_hours\": 0.5}, \"metrics\": {\"success_rate\": 0.815, \"n_tasks\": 10, \"total_rollouts\": 200}}, \"eval-pi05-vla-only-object-seed42-r3\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 42 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"76502\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42-r3.log\", \"submitted_at\": \"2026-05-21T11:52:15.488Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"200 (10x20)\", \"model_name\": \"pi0.5\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"wall_clock_seconds\": 1778.1, \"gpu_hours\": 0.49}, \"metrics\": {\"success_rate\": 0.82, \"n_tasks\": 10, \"total_rollouts\": 200}}, \"eval-spatial-obs-only-seed45\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_seed45.json\", \"server\": \"bjb2-28827\", \"seed\": 45, \"model_name\": \"crm_obs_only\", \"data_path\": \"spatial\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\"}, \"metrics\": {\"overall_sr\": 0.34, \"per_task_sr\": [0.9, 0.9, 0, 0.4, 0.1, 0, 0.8, 0, 0.3, 0], \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10}}, \"eval-pi05-vla-only-spatial-seed44\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 44 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"984515\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed44.log\", \"submitted_at\": \"2026-05-21T10:19:17.220Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5220.7, \"gpu_hours\": 1.45}}, \"eval-pi05-vla-only-spatial-seed43\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 43 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"984171\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed43.log\", \"submitted_at\": \"2026-05-21T10:19:07.725Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5214.7, \"gpu_hours\": 1.45}}, \"eval-pi05-vla-only-spatial-seed42\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 42 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"983816\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed42.log\", \"submitted_at\": \"2026-05-21T10:18:57.361Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5212.1, \"gpu_hours\": 1.45}}, \"eval-pi05-baseline-object-seed42-r2\": {\"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python3 -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --K 10 --output_file logs/eval_pi05_baseline_object_seed42_r2.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"811001\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-baseline-object-seed42-r2.log\", \"submitted_at\": \"2026-05-21T03:30:45.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-k20-obs-only-spatial-seed44\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 707148, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}}, \"eval-k20-obs-only-spatial-seed43\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 706941, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}}, \"eval-k20-obs-only-spatial-seed42\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": 873171, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}}, \"eval-k20-obs-only-object-seed45\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 45 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_object_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 23401, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}}, \"eval-obs-only-object-norm003-seed66\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.03 --seed 66 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_obs_only_v3_norm\", \"seed\": 66, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (eval only)\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/autodl-tmp/logs/norm003_seed66.log\"}, \"metrics\": {\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}}, \"eval-obs-only-object-norm01-seed66\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.1 --seed 66 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_obs_only_v3_norm\", \"seed\": 66, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (eval only)\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/autodl-tmp/logs/norm01_seed66.log\"}, \"metrics\": {\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}}, \"eval-obs-only-object-norm005-seed66\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.05 --seed 66 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"SmolVLA-base\", \"seed\": 66}, \"metrics\": {\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}}, \"eval-obs-only-object-norm003-seed67\": {\"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:5\"}, \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-k20-obs-only-object-seed44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed43\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"484257\", \"log_path\": \"logs/eval-k20-obs-only-object-seed43.log\", \"submitted_at\": \"2026-05-20T15:32:00Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA + CRM obs_only (K=20, norm02)\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 6686.0, \"gpu_hours\": 1.86}, \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed42\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"421434\", \"log_path\": \"logs/eval_k20_obs_only_object_seed42.json\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_K20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"status\": \"DONE\", \"metrics\": {\"sr\": 0.2}, \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-crm-object-k20-seed44\": {\"spec\": {\"command\": \"bash -c \\\"... python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --max_correction_norm 0.2 ...\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"278078\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-object-k20-seed44.log\", \"submitted_at\": \"2026-05-20T08:49:02.579Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only K=20\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 7329.3, \"gpu_hours\": 2.04}, \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-crm-object-k20-seed42\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_K20_seed42.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"309205\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-object-k20-seed42.log\", \"submitted_at\": \"2026-05-20T08:03:32.825Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only K=20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 9021.6, \"gpu_hours\": 2.51}, \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed53\": {\"spec\": {\"command\": \"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.2 --n_rollouts 10 --seed 53 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb2-28827\", \"seed\": 53, \"model_name\": \"crm_obs_only\", \"data_path\": \"object_benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed52\": {\"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.2 --n_rollouts 10 --seed 52 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm02_seed52.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"613001\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm02_seed52.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 52, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed51\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_seed51.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"CRM_obs_only\", \"seed\": 51, \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-obs-only-object-norm02-seed51.log\"}, \"metrics\": {\"overall_success_rate\": 0.17}}, \"eval-obs-only-object-norm02-seed50\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 50 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_seed50.json 2>&1 | tee logs/eval-obs-only-object-norm02-seed50.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"423273\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed50.log\", \"submitted_at\": \"2026-05-20T13:08:20.924Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6643.6, \"gpu_hours\": 1.85}, \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed48-r2\": {\"spec\": {\"command\": \"crm_obs_only --seed 48 --K 10 --max_correction_norm 0.2\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"796900\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed47\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed47.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"319128\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed47.log\", \"submitted_at\": \"2026-05-16T21:33:49.282Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 47, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\", \"wall_clock_seconds\": 48714.4, \"gpu_hours\": 13.53}, \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed46\": {\"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed46.json 2>&1 | tee logs/eval_object_obs_only_norm02_seed46.log\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 510896, \"seed\": 46, \"model_name\": \"crm_obs_only_norm02\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"hypothesis\": \"obs_only CRM v3-norm norm=0.2 seed=46 on LIBERO object. 5th seed for Fisher test statistical power.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"log_path\": \"logs/eval_object_obs_only_norm02_seed46.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed45\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"pid\": \"233544\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed45.log\", \"submitted_at\": \"2026-05-16T07:44:18.928Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 45, \"model_name\": \"crm_v3_norm_obs_only\", \"hypothesis\": \"obs_only CRM v3-norm norm=0.2 seed=45 on LIBERO object. 4th seed pre-deployed for statistical power.\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"wall_clock_seconds\": 49759.8, \"gpu_hours\": 13.82}, \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed44-r2\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"428406\", \"seed\": 44, \"model_name\": \"crm_obs_only_norm02\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}, \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed43-r3\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_seed43_r3.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"CRM_obs_only\", \"seed\": 43, \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-obs-only-object-norm02-seed43-r3.log\"}, \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed43-r2\": {\"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed43-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm005-seed67\": {\"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:2\"}, \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed67\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.1 --seed 67 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"SmolVLA-base\", \"seed\": 67}, \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-vla-only-object-seed50\": {\"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode vla_only --n_rollouts 10 --seed 50 --output_file logs/eval_vla_only_object_seed50.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"610053\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/vla_only_object_seed50.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 50}, \"metrics\": {\"overall_success_rate\": 0.09}}, \"eval-vla-only-object-seed49\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark object --seed 49 --n_rollouts 10 --K 1 --output_file logs/eval_vla_only_object_seed49.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 49, \"checkpoint_source\": \"N/A\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-vla-only-object-seed49.log\"}, \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-vla-only-object-seed48\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 48 --K 1 --output_file logs/eval_object_vla_only_seed48.json\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": 10, \"model_name\": \"smolvla_libero\", \"seed\": 48, \"checkpoint_source\": \"N/A (vla_only mode)\", \"eval_data\": \"LIBERO object benchmark\"}, \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-vla-only-object-seed46\": {\"spec\": {\"command\": \"vla_only --benchmark object --seed 46 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"vla_only\", \"seed\": 46, \"eval_data\": \"LIBERO-Object\"}, \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-vla-only-object-seed45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --benchmark object --mode vla_only --K 1 --seed 45 --output_file logs/eval_object_vla_only_seed45.json\", \"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:4\", \"pid\": 221407, \"seed\": 45, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO object\", \"data_count\": 10, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"VLA-only baseline K=1 seed=45 on LIBERO object. Reference for seed45 statistical comparison. seed42=12%, seed43=12%, seed44=10%.\"}, \"metrics\": {\"overall_success_rate\": 0.09}}, \"eval-vla-only-object-seed44-r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"286989\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44-r2.log\", \"submitted_at\": \"2026-05-16T01:33:46.467Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20383.4, \"gpu_hours\": 5.66}, \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-plan-a-object-seed42\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --benchmark object --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.074855\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"559831\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only(adaptive_conformal_crm)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/plan_a_object_seed42.log\"}, \"metrics\": {\"success_rate\": 0.19, \"sr_pct\": \"19.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1468, \"trigger_rate\": 0.838}}, \"eval-vla-only-object-seed43\": {\"spec\": {\"hypothesis\": \"D031: VLA-only baseline (K=1, single sample, no CRM) seed=43 on LIBERO object benchmark. Completes 7-way seed=43 comparison table. VLA-only seed=42 = 12% = argmin.\", \"parent\": \"eval-vla-only-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 43 --K 1 --output_file logs/eval_object_vla_only_seed43.json\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"vla_only\", \"seed\": 43, \"eval_data\": \"object\"}, \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-vla-only-object\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --n_rollouts 10 --K 1 --output_file logs/eval_object_vla_only.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA (VLA-only baseline)\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\"}, \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-plan-a-spatial-seed43\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.074855 --output_file logs/eval_plan_a_spatial_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"664544\", \"seed\": 43, \"model_name\": \"SmolVLA+CRM_obs_only_adaptive\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/plan_a_spatial_seed43.log\"}, \"metrics\": {\"success_rate\": 0.35, \"total_rollouts\": 100, \"total_successes\": 35, \"mean_uncertainty\": 0.2619, \"trigger_rate\": 0.98}}, \"eval-plan-a-object-seed44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --benchmark object --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.074855\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"563761\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only(adaptive_conformal_crm)\", \"seed\": 44, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/plan_a_object_seed44.log\"}, \"metrics\": {\"success_rate\": 0.2, \"sr_pct\": \"20.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1448, \"trigger_rate\": 0.832}}, \"eval-plan-a-spatial-seed42\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.074855 --output_file logs/eval_plan_a_spatial_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"664543\", \"seed\": 42, \"model_name\": \"SmolVLA+CRM_obs_only_adaptive\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/plan_a_spatial_seed42.log\"}, \"metrics\": {\"success_rate\": 0.34, \"total_rollouts\": 100, \"total_successes\": 34, \"mean_uncertainty\": 0.2679, \"trigger_rate\": 0.976}}, \"eval-plan-a-spatial-seed44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.074855 --output_file logs/eval_plan_a_spatial_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"664545\", \"seed\": 44, \"model_name\": \"SmolVLA+CRM_obs_only_adaptive\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/plan_a_spatial_seed44.log\"}, \"metrics\": {\"success_rate\": 0.36, \"sr_pct\": \"36.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.2661, \"trigger_rate\": 0.978}}, \"eval-plan-a-object-seed43\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.074855\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"560444\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only(adaptive_conformal_crm)\", \"seed\": 43, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/plan_a_object_seed43.log\"}, \"metrics\": {\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1457, \"trigger_rate\": 0.84}}, \"eval-random-selection-object-seed44\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode random_selection --benchmark object --K 10 --seed 44 --n_rollouts 10 --output_file logs/eval_random_selection_object_seed44.json 2>&1 | tee logs/eval-random-selection-object-seed44.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"853229\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed44.log\", \"submitted_at\": \"2026-05-21T04:34:41.887Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-random-selection-object-seed43\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 10 --output_file logs/eval_random_selection_object_seed43.json 2>&1 | tee logs/eval-random-selection-object-seed43.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"852632\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43.log\", \"submitted_at\": \"2026-05-21T04:34:36.549Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}}, \"eval-random-selection-object-seed42-r3\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode random_selection --benchmark object --K 10 --seed 42 --n_rollouts 10 --output_file logs/eval_random_selection_object_seed42.json 2>&1 | tee logs/eval-random-selection-object-seed42.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"852344\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed42-r3.log\", \"submitted_at\": \"2026-05-21T04:34:30.827Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-spatial-seed50\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 50 --n_rollouts 10 --output_file logs/eval_vla_only_spatial_seed50.json 2>&1 | tee logs/eval-vla-only-spatial-seed50.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"850105\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed50.log\", \"submitted_at\": \"2026-05-21T04:32:49.401Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-crm-spatial-k10-seed50\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark spatial --K 10 --seed 50 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed50.json 2>&1 | tee logs/eval-crm-spatial-k10-seed50.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"849760\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-spatial-k10-seed50.log\", \"submitted_at\": \"2026-05-21T04:32:38.353Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-crm-spatial-k10-seed49\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark spatial --K 10 --seed 49 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed49.json 2>&1 | tee logs/eval-crm-spatial-k10-seed49.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"11357\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-spatial-k10-seed49.log\", \"submitted_at\": \"2026-05-21T04:32:28.560Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-obs-only-object-norm02-k20-seed44\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed44.json 2>&1 | tee logs/eval-obs-only-object-norm02-k20-seed44.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"11078\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed44.log\", \"submitted_at\": \"2026-05-21T04:32:21.220Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm02-k20-seed43\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed43.json 2>&1 | tee logs/eval-obs-only-object-norm02-k20-seed43.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"10781\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed43.log\", \"submitted_at\": \"2026-05-21T04:32:14.520Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm02-k20-seed42\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 42 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed42.json 2>&1 | tee logs/eval-obs-only-object-norm02-k20-seed42.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"10438\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed42.log\", \"submitted_at\": \"2026-05-21T04:32:09.740Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm01-seed60\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 60 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/norm01_seed60.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"914909\", \"seed\": 60, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/norm01_seed60.log\"}, \"metrics\": {\"overall_success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"source\": \"harvested from bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm01_seed60.json\"}}, \"eval-pi05-baseline-object-seed42\": {\"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python3 -u src/evaluate.py --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --K 10 --output_file logs/eval_pi05_baseline_object_seed42_r2.json\", \"server\": \"bjb2-40593\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42}, \"metrics\": {\"overall_success_rate\": 0}}, \"eval-obs-only-object-norm003-seed76\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 76 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed76.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"825126\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed76.log\", \"submitted_at\": \"2026-05-21T03:33:41.212Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm01-seed54\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 54 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed54.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"855445\", \"seed\": 54, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm01_seed54.log\"}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed53\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 53 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed53.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"855444\", \"seed\": 53, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm01_seed53.log\"}, \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm01-seed52\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 52 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed52.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"664547\", \"seed\": 52, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm01_seed52.log\"}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed50\": {\"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.1 --n_rollouts 10 --seed 50 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"seed\": 50, \"model_name\": \"SmolVLM2-500M-Video-Instruct\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"gpu\": [\"cuda:2\"], \"pid\": \"526048\"}, \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed49\": {\"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.1 --n_rollouts 10 --seed 49 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm01_seed49.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"615795\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm01_seed49.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 49, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm01-seed48\": {\"spec\": {\"command\": \"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.1 --n_rollouts 10 --seed 48 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb2-28827\", \"seed\": 48, \"model_name\": \"crm_obs_only\", \"data_path\": \"object_benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\", \"gpu\": [\"cuda:1\"]}, \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm01-seed47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"logs/eval_object_obs_only_norm01_seed47.log\"}, \"metrics\": {\"overall_success_rate\": 0.17}}, \"eval-obs-only-object-norm01-seed45-r2\": {\"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed45_r2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"578936\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed45-r2.log\", \"submitted_at\": \"2026-05-18T13:24:52.633Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 56230.4, \"gpu_hours\": 15.62}, \"metrics\": {\"overall_success_rate\": 0.17}}, \"eval-obs-only-object-norm01-seed44\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"227086\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed44.log\", \"submitted_at\": \"2026-05-16T07:12:01.614Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 45205.2, \"gpu_hours\": 12.56}, \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm005-seed55\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 55 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed55.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"578254\", \"seed\": 55, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm005_seed55.log\"}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed50\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 50 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed50.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"855446\", \"seed\": 50, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm005_seed50.log\"}, \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed49\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 49 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed49.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"664548\", \"seed\": 49, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm005_seed49.log\"}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed48\": {\"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.05 --n_rollouts 10 --seed 48 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm005_seed48.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"617583\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm005_seed48.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed47\": {\"spec\": {\"command\": \"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.05 --n_rollouts 10 --seed 47 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb2-28827\", \"seed\": 47, \"model_name\": \"crm_obs_only\", \"data_path\": \"object_benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_norm005\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-obs-only-object-norm005-seed43-r2\": {\"spec\": {\"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"433500\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005_seed43_r2.json\", \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 43, \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm005-seed43\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"484651\", \"log_path\": \"logs/eval-obs-only-object-norm005-seed43.log\", \"submitted_at\": \"2026-05-20T15:32:00Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA + CRM obs_only (K=10, ε=0.05)\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 6721.6, \"gpu_hours\": 1.87}, \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed48\": {\"spec\": {\"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed48.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"67819\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed48.log\", \"submitted_at\": \"2026-05-19T11:59:23.808Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"crm_obs_only (max_correction_norm=0.03)\", \"seed\": 48, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 6434.5, \"gpu_hours\": 1.79}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed47-r2\": {\"spec\": {\"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed47.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"894890\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed47-r2.log\", \"submitted_at\": \"2026-05-19T11:59:21.264Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"crm_obs_only (max_correction_norm=0.03)\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 8431.2, \"gpu_hours\": 2.34}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 46 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed46.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"855447\", \"seed\": 46, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm003_seed46.log\"}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed45\": {\"spec\": {\"command\": \"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.03 --n_rollouts 10 --seed 45 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb2-28827\", \"seed\": 45, \"model_name\": \"crm_obs_only\", \"data_path\": \"object_benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"spec\": {\"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed44.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 44, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"submitted_at\": \"2026-05-18T21:09:00Z\", \"wall_clock_seconds\": 56135.2, \"gpu_hours\": 15.59}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_norm003\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed43-r2\": {\"spec\": {\"command\": \"bash -c \\\"... python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --max_correction_norm 0.03 ...\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"314884\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed43-r2.log\", \"submitted_at\": \"2026-05-20T08:21:20.349Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only ε=0.03\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 8051.5, \"gpu_hours\": 2.24}, \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm003-seed43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"CRM_obs_only\", \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt\", \"seed\": 43, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-obs-only-object-norm003-seed43.log\"}, \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed57\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 57 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed57.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"594635\", \"seed\": 57, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm01_seed57.log\"}, \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm005-seed65\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 65 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed65.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"622479\", \"seed\": 65, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm005_seed65.log\"}, \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm005-seed61\": {\"metrics\": {\"overall_success_rate\": 0.15}, \"spec\": {\"command\": \"python src/evaluate.py --mode crm_obs_only --benchmark object --K 10 --n_rollouts 10 --seed 61 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object (10 tasks)\", \"data_count\": 100, \"model_name\": \"SmolVLA + CRM v3 obs_only\", \"seed\": 61, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-obs-only-object-norm005-seed58\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 58 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed58.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"596867\", \"seed\": 58, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm005_seed58.log\"}, \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm003-seed59\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 59 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed59.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"599925\", \"seed\": 59, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm003_seed59.log\"}, \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed56\": {\"metrics\": {\"overall_success_rate\": 0.15}, \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 56 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed56.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"865274\", \"seed\": 56, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm003_seed56.log\"}}, \"eval-obs-only-object-norm01-seed77\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 77 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed77.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"815988\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed77.log\", \"submitted_at\": \"2026-05-21T03:17:04.908Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm01-seed76\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 76 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed76.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"815198\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed76.log\", \"submitted_at\": \"2026-05-21T03:16:59.361Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm005-seed77\": {\"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 77 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed77.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"982671\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed77.log\", \"submitted_at\": \"2026-05-21T03:16:55.416Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm003-seed63-r3\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 63 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed63_r3.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"814859\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed63-r3.log\", \"submitted_at\": \"2026-05-21T03:16:50.645Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm005-seed76\": {\"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 76 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed76.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"981080\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed76.log\", \"submitted_at\": \"2026-05-21T03:16:43.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm003-seed62-r3\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 62 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed62_r3.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"814262\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed62-r3.log\", \"submitted_at\": \"2026-05-21T03:16:40.387Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm003-seed78\": {\"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 78 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed78.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"980035\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed78.log\", \"submitted_at\": \"2026-05-21T03:16:31.286Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm003-seed77\": {\"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 77 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed77.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"979376\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed77.log\", \"submitted_at\": \"2026-05-21T03:16:22.477Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm005-seed75\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 75 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/norm005_seed75.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"923398\", \"seed\": 75, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/norm005_seed75.log\"}, \"metrics\": {\"overall_success_rate\": 0.15, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed74\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 74 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/norm01_seed74.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"923256\", \"seed\": 74, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/norm01_seed74.log\"}, \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed72\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 72 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/norm005_seed72.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"922712\", \"seed\": 72, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/norm005_seed72.log\"}, \"metrics\": {\"overall_success_rate\": 0.11, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed63-r2\": {\"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 63 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed63_r2.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"seed\": 63, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_source\": \"crm_v3_norm_obs_only\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm003_seed63_r2.log\", \"pid\": 735998}}, \"eval-obs-only-object-norm01-seed71\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 71 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/norm01_seed71.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"922504\", \"seed\": 71, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/norm01_seed71.log\"}, \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed62-r2\": {\"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 62 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed62_r2.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"seed\": 62, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_source\": \"crm_v3_norm_obs_only\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm003_seed62_r2.log\", \"pid\": 734631}}, \"eval-obs-only-object-norm003-seed73\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 73 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/norm003_seed73.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"922982\", \"seed\": 73, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/norm003_seed73.log\"}, \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed51-r3\": {\"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed51_r3.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"seed\": 51, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_source\": \"crm_v3_norm_obs_only\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm01_seed51_r3.log\", \"pid\": 731912}, \"metrics\": {\"overall_success_rate\": 0.11}}, \"eval-obs-only-object-norm01-seed52-r3\": {\"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 52 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed52_r3.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"seed\": 52, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_source\": \"crm_v3_norm_obs_only\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm01_seed52_r3.log\", \"pid\": 733203}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed65\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 65 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed65.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"728057\", \"seed\": 65, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm01_seed65.log\"}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed64\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 64 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed64.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"726800\", \"seed\": 64, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm01_seed64.log\"}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed64\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 64 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed64.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"729873\", \"seed\": 64, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm005_seed64.log\"}, \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed65\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 65 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed65.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"725722\", \"seed\": 65, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm003_seed65.log\"}, \"metrics\": {\"overall_success_rate\": 0.17}}, \"eval-obs-only-object-norm003-seed64\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 64 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed64.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"723784\", \"seed\": 64, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm003_seed64.log\"}, \"metrics\": {\"overall_success_rate\": 0.17}}, \"eval-obs-only-object-norm005-seed62\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 62 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/norm005_seed62.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"915391\", \"seed\": 62, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/norm005_seed62.log\"}}, \"eval-obs-only-object-norm005-seed63\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 63 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/norm005_seed63.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"915981\", \"seed\": 63, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/norm005_seed63.log\"}}, \"eval-obs-only-object-norm01-seed61\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 61 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/norm01_seed61.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"915187\", \"seed\": 61, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/norm01_seed61.log\"}}, \"eval-obs-only-object-norm003-seed64-bjb2\": {\"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 64 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/norm003_seed64.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"916316\", \"seed\": 64, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/norm003_seed64.log\"}}, \"eval-obs-only-object-norm003-seed63\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 63 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed63.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"720054\", \"seed\": 63, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm003_seed63.log\"}}, \"eval-obs-only-object-norm003-seed62\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 62 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed62.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"720053\", \"seed\": 62, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm003_seed62.log\"}}, \"eval-obs-only-object-norm01-seed51-r2\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed51_r2.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"720055\", \"seed\": 51, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm01_seed51_r2.log\"}}, \"eval-obs-only-object-norm01-seed52-r2\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 52 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed52_r2.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"720056\", \"seed\": 52, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm01_seed52_r2.log\"}}, \"eval-obs-only-object-norm01-seed51\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed51.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"664546\", \"seed\": 51, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm01_seed51.log\"}, \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"total_successes\": 11}}, \"eval-obs-only-object-norm005-seed49-r2\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 49 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed49_r2.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"720058\", \"seed\": 49, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm005_seed49_r2.log\"}}, \"eval-obs-only-object-norm005-seed55-r2\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 55 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed55_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"617168\", \"seed\": 55, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm005_seed55_r2.log\"}}, \"eval-openvla-crm-object-seed42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --openvla --mode crm_obs_only --benchmark object --seed 42 --n_rollouts 10 --K 10 --obs_dim 4096 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_openvla_obs_only/crm_best.pt --max_correction_norm 0.2 --output_file /root/autodl-tmp/logs/openvla_crm_eval_seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": 842052, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"OpenVLA-7B+CRM_obs_only\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_openvla_obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/openvla_crm_eval_seed42.log\"}, \"metrics\": {\"success_rate\": 0, \"sr_pct\": \"0.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed44-r2\": {\"metrics\": {\"success_rate\": 0.15, \"sr_pct\": \"15.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"spec\": {\"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"seed\": 44, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100}}, \"eval-random-selection-object-seed49\": {\"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode random_selection --K 10 --n_rollouts 10 --seed 49 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_object_seed49.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"611575\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/random_sel_object_seed49.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+RandomSelection\", \"seed\": 49, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"metrics\": {\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed48\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark object --seed 48 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"CRM_obs_only\", \"seed\": 48}, \"metrics\": {\"success_rate\": 0.1, \"sr_pct\": \"10.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-k5-obs-only-object-seed44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k5_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"metrics\": {\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-seed52\": {\"spec\": {\"command\": \"python src/evaluate.py --benchmark spatial --mode crm_obs_only --K 10 --max_correction_norm 0.2 --n_rollouts 10 --seed 52 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_spatial_norm02_seed52.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"614298\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_spatial_norm02_seed52.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 52, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"metrics\": {\"success_rate\": 0.33, \"sr_pct\": \"33.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-seed54\": {\"spec\": {\"command\": \"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.2 --n_rollouts 10 --seed 54 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb2-28827\", \"seed\": 54, \"model_name\": \"crm_obs_only\", \"data_path\": \"object_benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}}, \"D088-eval-adaptive-unc-head-object-seed44\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 44, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed44.log\"}}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 43, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed43.log\"}}, \"D088-eval-adaptive-unc-head-object-seed42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 42, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed42.log\"}}, \"eval-obs-only-object-norm005-seed45\": {\"spec\": {\"command\": \"crm_obs_only --seed 45 --K 10 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"565173\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-adaptive-unc-head-object-seed42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"UncHead_tau0.42_K1_CRM\", \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt + uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 42, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed42.log\"}, \"metrics\": {\"success_rate\": 0.14, \"mean_l2\": 0, \"avg_k\": 1, \"fast_path_pct\": 0.12, \"n_rollouts\": 10}}, \"eval-adaptive-unc-head-object-seed43\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"UncHead_tau0.42_K1_CRM\", \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt + uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 43, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed43.log\"}, \"metrics\": {\"success_rate\": 0.11, \"n_rollouts\": 100, \"fast_path_pct\": 12.5, \"avg_k\": 1}}, \"eval-perdof-object-norm02-seed50\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 50 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_perdof_object_norm02_seed50.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"CRM_perdof\", \"seed\": 50, \"checkpoint_source\": \"crm_v3_norm/perdof/crm_best.pt\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-perdof-object-norm02-seed50.log\"}, \"metrics\": {\"success_rate\": 0.1, \"n_rollouts\": 100, \"per_task\": [0, 0, 1, 1, 0, 1, 1, 0, 4, 2]}}, \"eval-adaptive-unc-head-object-seed44\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 10 --K 1 --crm_checkpoint crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"seed\": 44, \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"pid\": 728278, \"log_path\": \"logs/eval-adaptive-unc-head-object-seed44.log\", \"checkpoint_path\": \"N/A (eval-only)\", \"account\": \"root\"}, \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"avg_K\": 1, \"adaptive_trigger_rate\": 0, \"crm_trigger_rate\": 0.8795, \"unc_threshold\": 0.42}}, \"eval-random-selection-spatial-seed42-r3\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed42_r3.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-seed50\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 50 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed50.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"CRM_obs_only\", \"seed\": 50, \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-obs-only-spatial-norm02-seed50.log\"}, \"metrics\": {\"success_rate\": 0.35, \"successes\": 35, \"total_rollouts\": 100}}, \"train-crm-openvla-obs-only\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_k1_openvla --K 1 --obs_dim 4096 --input_mode obs_only --epochs 50 --batch_size 32 --lr 1e-3 --seed 42 --output_dir /root/autodl-tmp/checkpoints/crm_openvla_obs_only/\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"data_path\": \"/root/autodl-tmp/crm_cache_k1_openvla/object\", \"data_count\": 74507, \"model_name\": \"CRM_obs_only_openvla\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training run)\"}, \"metrics\": {\"best_val_loss\": 0.07726, \"final_train_loss\": 0.234989, \"epochs_completed\": 50}}, \"openvla-precompute-k1\": {\"spec\": {\"command\": \"python precompute_openvla.py --device cuda:0 --max_demos_per_task 50 --cache_dir /root/autodl-tmp/crm_cache_k1_openvla/\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"365142\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/openvla-precompute-k1.log\", \"submitted_at\": \"2026-05-20T13:49:29.016Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 74507, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"wall_clock_seconds\": 17125.6, \"gpu_hours\": 4.76}, \"metrics\": {\"total_files\": 74507, \"obs_dim\": 4096, \"cache_size_gb\": 6, \"multi_scale_layers\": [7, 15, 23, 31]}}, \"eval-random-selection-object-seed46-r3\": {\"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark object --seed 46 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_object_seed46.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"421636\", \"log_path\": \"logs/eval-random-selection-object-seed46.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"/root/auto
```

---
