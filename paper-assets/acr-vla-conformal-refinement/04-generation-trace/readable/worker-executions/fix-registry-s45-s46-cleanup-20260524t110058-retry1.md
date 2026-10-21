# fix registry s45 s46 cleanup 20260524T110058 retry1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/workers/worker_fix_registry-s45-s46-cleanup_20260524T110058_retry1.log`
- **Structured JSON:** [`83c44c30daa0dcf96671.json`](../../sessions/83/83c44c30daa0dcf96671.json)

## Before a recorded user message

60 recorded events

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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
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
  "uuid": "4a4a301c-6de7-4344-b492-86d07367022d",
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
    "resetsAt": 1779628200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d56c4cdc-4921-4fa3-a481-95b2f020f066",
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad"
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "9ee6288a-2683-430e-b77a-339d6d7e3f0c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AzodFAz5J45fRxJG2671K3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14729,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14729
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FGwWpTbjuqrqz3dRaLwrVV`</summary>

```json
{
  "query": "select:read_registry,update_registry,ssh_read_only,ssh_execute,detect_image",
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "371ceb1e-9b22-4ded-a01f-c123c78c59c2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AzodFAz5J45fRxJG2671K3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14729,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14729
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

_source line 6 · 2026-05-24T11:01:18.567Z_

<details><summary>↩ Tool result · `toolu_01FGwWpTbjuqrqz3dRaLwrVV`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "b1b53a66-17f9-4440-9827-ff084ad4969d",
  "tool_use_result": {
    "matches": [],
    "query": "select:read_registry,update_registry,ssh_read_only,ssh_execute,detect_image",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UjCrhbTJEzuuwEJgAfZ8DT`</summary>

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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "03887171-948e-41ac-b6ce-243409068a03",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011zeLM5txCoztWTBf8bmQ2c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 195,
      "cache_read_input_tokens": 30970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 195
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 8 · 2026-05-24T11:01:22.290Z_

<details><summary>↩ Tool result · `toolu_01UjCrhbTJEzuuwEJgAfZ8DT`</summary>

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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "e8351e63-b194-47a8-a073-a24f46082a36",
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

### Assistant

_source line 9_

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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "76edae38-73a1-45d3-8c40-9b86adbd11eb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Tna8oyfDRxRGtt41qV2Nq4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16937,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16937
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28878
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Bb22EpUk8BnFWBJpqYLA3g`</summary>

```json
{
  "filters": {
    "exp_id": "eval-supp-spatial-reconvla-s46"
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "82ed7827-26ac-4254-8841-37e7278d4adf",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Tna8oyfDRxRGtt41qV2Nq4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16937,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16937
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28878
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01K6cTurYuyFEY7eihGXEhdy`</summary>

```json
{
  "filters": {
    "exp_id": "eval-supp-spatial-k2mean-s46"
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "37c90f7a-49d0-4eac-84db-cdfec8f3d5b9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Tna8oyfDRxRGtt41qV2Nq4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16937,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16937
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28878
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T11:01:33.588Z_

<details><summary>↩ Tool result · `toolu_01Bb22EpUk8BnFWBJpqYLA3g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0314}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "59389101-b637-4649-bc9e-6d3070fdadae",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.0314}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0314}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01DZAK5ob3GHNHBLCb18YehD`</summary>

```json
{
  "filters": {
    "exp_id": "eval-supp-spatial-adapt-tau025-s45-r3"
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "77a75f4e-84be-4e7c-bb45-eecf6ba808fe",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Tna8oyfDRxRGtt41qV2Nq4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16937,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16937
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28878
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01B1roXJ3N4ggGAyE7FR3KD2`</summary>

```json
{
  "filters": {
    "exp_id": "eval-supp-reconvla-obj-s45"
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "61245284-06eb-45e5-b97d-4e7fac4da622",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Tna8oyfDRxRGtt41qV2Nq4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16937,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16937
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28878
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-24T11:01:35.546Z_

<details><summary>↩ Tool result · `toolu_01K6cTurYuyFEY7eihGXEhdy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9461}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "5507990a-5b48-414b-93aa-26fac731006c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.9461}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9461}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BV2KjSfJdSyfBcE4Si4rja`</summary>

```json
{
  "filters": {
    "exp_id": "eval-smolvla-lerobot-goal-seed43-v3"
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "f5bccf5f-4819-49a0-a0a3-d7c2b2cd7b76",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Tna8oyfDRxRGtt41qV2Nq4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16937,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16937
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28878
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T11:01:37.599Z_

<details><summary>↩ Tool result · `toolu_01DZAK5ob3GHNHBLCb18YehD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0401}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "3473585d-560e-4c9b-a740-0361456c08a0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.0401}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0401}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_013yyJci2VcaTkHwqVxMFk4b`</summary>

```json
{
  "filters": {
    "exp_id": "eval-smolvla-lerobot-spatial-seed43-v3"
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "d14705ca-6531-4d2b-85b7-854b02630b54",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Tna8oyfDRxRGtt41qV2Nq4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16937,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16937
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28878
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011K2qj5s9h6VCMnLhxyXxNh`</summary>

```json
{
  "filters": {
    "exp_id": "eval-supp-spatial-crm-norm005-s47"
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "39a89847-a725-4bbd-9f14-7eccca89d09b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Tna8oyfDRxRGtt41qV2Nq4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16937,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16937
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28878
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T11:01:39.628Z_

<details><summary>↩ Tool result · `toolu_01B1roXJ3N4ggGAyE7FR3KD2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0169}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "f0789dc8-9696-43ea-b20a-b827363dda81",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.0169}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0169}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-24T11:01:41.787Z_

<details><summary>↩ Tool result · `toolu_01BV2KjSfJdSyfBcE4Si4rja`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1435}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "6cb17d82-7933-4c91-a69b-4b48c24b780f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.1435}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1435}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T11:01:43.707Z_

<details><summary>↩ Tool result · `toolu_013yyJci2VcaTkHwqVxMFk4b`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9059}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "90eb414b-991c-4b2c-b882-c8b3385ce6a4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.9059}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9059}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T11:01:46.259Z_

<details><summary>↩ Tool result · `toolu_011K2qj5s9h6VCMnLhxyXxNh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5246}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "754824f6-6a73-4543-b2a7-6062b842e2a0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.5246}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5246}}"
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "a5a2eaea-5093-49ca-8e7e-254cb8db4d4d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01CvYnpzxsFrQi946fd3WfiQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1992,
      "cache_read_input_tokens": 33271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1992
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_014cMzfNycYtGN527nxat1ra`</summary>

```json
{
  "filters": {
    "status": "RUNNING"
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "6f2cb01a-b6c7-4e42-bd00-c7f45ab03f5a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01CvYnpzxsFrQi946fd3WfiQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1992,
      "cache_read_input_tokens": 33271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1992
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

_source line 26 · 2026-05-24T11:01:53.256Z_

<details><summary>↩ Tool result · `toolu_014cMzfNycYtGN527nxat1ra`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-spatial-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:58:57.165Z\", \"updated_at\": \"2026-05-24T11:00:32.832Z\", \"hypothesis\": \"ReconVLA reconstruction-based baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the reconvla baseline.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb2-40593\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"gpu\": \"cuda:0\", \"pid\": 261844, \"tmux_session\": \"spatial-reconvla-s47\", \"log_path\": \"/tmp/eval_spatial_reconvla_s47.log\"}}, \"eval-supp-spatial-k2mean-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:58:53.820Z\", \"updated_at\": \"2026-05-24T11:00:26.172Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"gpu\": \"cuda:3\", \"pid\": 845121, \"tmux_session\": \"spatial-k2mean-s47\", \"log_path\": \"/tmp/eval_spatial_k2mean_s47.log\"}}, \"eval-supp-spatial-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:58:50.342Z\", \"updated_at\": \"2026-05-24T11:00:19.541Z\", \"hypothesis\": \"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --adaptive_threshold 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"gpu\": \"cuda:2\", \"pid\": 844595, \"tmux_session\": \"spatial-adapt-s47\", \"log_path\": \"/tmp/eval_spatial_adapt_s47.log\"}}, \"eval-supp-spatial-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:58:43.441Z\", \"updated_at\": \"2026-05-24T11:00:12.802Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial at seed 47 for seed-extension coverage. Extends 3-seed mean to 4th seed.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 2\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"gpu\": \"cuda:0\", \"pid\": 844299, \"tmux_session\": \"spatial-vla-s47\", \"log_path\": \"/tmp/eval_spatial_vla_s47.log\"}}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T10:58:46.991Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"train-crm-pi05-unified-3suite-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:38:31.224Z\", \"updated_at\": \"2026-05-24T10:39:56.094Z\", \"hypothesis\": \"π0.5 unified 3-suite (Spatial+Goal+Object) CRM training retry with batch_size=256 (was 32). D135: Long dropped due to DDL. obs_dim=2048, ~194K samples, 50 epochs. Parent killed due to 55h ETA; bs256 targets ~7-8h.\", \"parent\": \"train-crm-pi05-unified-3suite\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark object spatial goal --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ --obs_dim 2048 --epochs 50 --batch_size 256 --lr 1e-3 --output_dir /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/\", \"server\": \"bjb1-18228\", \"gpu\": 0, \"pid\": 326310, \"model_name\": \"pi05\", \"obs_dim\": 2048, \"data_count\": 194485, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/\", \"data_breakdown\": {\"object\": 72507, \"spatial\": 60250, \"goal\": 61728}, \"seed\": 42, \"batch_size\": 256, \"epochs\": 50, \"lr\": 0.001, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-pi05-unified-3suite-r2.log\", \"tmux_session\": \"train-crm-pi05-unified-3suite-r2\", \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training job, not eval)\"}}, \"eval-supp-long-k2mean-s47-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:52:10.417Z\", \"updated_at\": \"2026-05-24T09:53:45.939Z\", \"hypothesis\": \"Long s47 K=2 mean baseline for seed extension (r2 on bjb2-28827). Sixth seed to tighten CI for Long suite K2mean method.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\", \"tmux_session\": \"long-k2mean-s47\", \"log_path\": \"/tmp/eval_long_k2mean_s47.log\", \"gpu\": 5, \"pid\": 205647}}, \"eval-supp-obj-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:52:06.114Z\", \"updated_at\": \"2026-05-24T09:53:35.694Z\", \"hypothesis\": \"Object s47 Reconvla baseline, only missing Object s47 method. Completes Object suite seed extension coverage.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark object --mode reconvla --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-reconvla\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"tmux_session\": \"obj-reconvla-s47\", \"log_path\": \"/tmp/eval_obj_reconvla_s47.log\", \"gpu\": 4, \"pid\": 200690}}, \"eval-supp-goal-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:52:02.749Z\", \"updated_at\": \"2026-05-24T09:53:29.313Z\", \"hypothesis\": \"Goal s47 Reconvla baseline for seed extension. Sixth seed to tighten CI for Goal suite Reconvla method.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-reconvla\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-reconvla-s47\", \"log_path\": \"/tmp/eval_goal_reconvla_s47.log\", \"gpu\": 3, \"pid\": 200418}}, \"eval-supp-goal-k2mean-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:51:59.402Z\", \"updated_at\": \"2026-05-24T09:53:22.862Z\", \"hypothesis\": \"Goal s47 K=2 mean baseline for seed extension. Sixth seed to tighten CI for Goal suite K2mean method.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-k2mean-s47\", \"log_path\": \"/tmp/eval_goal_k2mean_s47.log\", \"gpu\": 2, \"pid\": 205380}}, \"eval-supp-goal-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:51:56.065Z\", \"updated_at\": \"2026-05-24T09:53:16.020Z\", \"hypothesis\": \"Goal s47 CRM obs-only (norm=0.05) eval for seed extension. Sixth seed to tighten CI for Goal suite CRM method.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-crm-s47\", \"log_path\": \"/tmp/eval_goal_crm_s47.log\", \"gpu\": 1, \"pid\": 199883}}, \"eval-supp-goal-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:51:52.528Z\", \"updated_at\": \"2026-05-24T09:53:08.583Z\", \"hypothesis\": \"Goal s47 Adaptive gating (tau=0.25) eval for seed extension. Sixth seed to tighten CI for Goal suite Adaptive method.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --adaptive_threshold 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-adapt-s47\", \"log_path\": \"/tmp/eval_goal_adapt_s47.log\", \"gpu\": 0, \"pid\": 205107}}, \"eval-supp-goal-vla-only-s47-r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:31:15.967Z\", \"updated_at\": \"2026-05-24T09:32:36.215Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline, second re-run after r2 was killed for CRM training priority. Fills Goal s47 seed extension for variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s47-r2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO goal benchmark\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"pretrained SmolVLA /root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO goal, 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-vla-s47\", \"log_path\": \"/tmp/eval_goal_vla_s47.log\", \"gpu\": 2, \"pid\": 307664}}, \"eval-supp-long-vla-only-s47-r4\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:31:12.366Z\", \"updated_at\": \"2026-05-24T09:32:29.415Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline, third re-run after r2/r3 were killed for CRM training priority. Fills Long s47 seed extension for variance analysis.\", \"parent\": \"eval-supp-long-vla-only-s47-r3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO long benchmark\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"pretrained SmolVLA /root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO long, 10 tasks x 20 rollouts\", \"tmux_session\": \"long-vla-s47\", \"log_path\": \"/tmp/eval_long_vla_s47.log\", \"gpu\": 1, \"pid\": 307463}}, \"eval-supp-obj-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T08:38:16.262Z\", \"updated_at\": \"2026-05-24T08:40:20.644Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object suite seed47. Sixth seed extending Object Adaptive coverage for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"obj-adapt-s47\", \"log_path\": \"/tmp/eval_obj_adapt_s47.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA+Adaptive CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-supp-obj-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T08:38:10.740Z\", \"updated_at\": \"2026-05-24T08:40:14.365Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Object suite seed47. Sixth seed extending Object CRM coverage for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"obj-crm-s47\", \"log_path\": \"/tmp/eval_obj_crm_norm005_s47.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-supp-obj-k2mean-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T08:38:07.452Z\", \"updated_at\": \"2026-05-24T08:40:07.860Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed47. Sixth seed extending Object K2mean coverage for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"obj-k2mean-s47\", \"log_path\": \"/tmp/eval_obj_k2mean_s47.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-obj-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T08:38:03.765Z\", \"updated_at\": \"2026-05-24T08:39:52.861Z\", \"hypothesis\": \"VLA-only (K=1) baseline on Object suite seed47. Sixth seed extending Object VLA-only coverage for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"obj-vla-s47\", \"log_path\": \"/tmp/eval_obj_vla_only_s47.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-long-k2mean-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:23.532Z\", \"updated_at\": \"2026-05-24T08:27:00.000Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed47. Renamed from eval-supp-long-vla-only-s47 (was misnamed at creation — actual command uses --baseline_mode mean --K 2). Paired with Adapt-s47 for matched-seed comparison.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-vla-s47\", \"log_path\": \"logs/eval-supp-long-vla-only-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:55.833Z\", \"updated_at\": \"2026-05-24T07:18:30.230Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"spatial-k2mean-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:47.910Z\", \"updated_at\": \"2026-05-24T07:18:23.847Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"spatial-reconvla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Reconvla\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:43.884Z\", \"updated_at\": \"2026-05-24T07:18:17.441Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80.5%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"spatial-adapt-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Adaptive CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:40.347Z\", \"updated_at\": \"2026-05-24T07:18:10.979Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~78.7%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"spatial-vla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:08.968Z\", \"updated_at\": \"2026-05-24T06:53:16.695Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-crm-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:05.630Z\", \"updated_at\": \"2026-05-24T06:53:02.593Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-reconvla-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:20.287Z\", \"updated_at\": \"2026-05-24T06:38:39.651Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-adapt-s47\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46-r2\"}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:31.140Z\", \"updated_at\": \"2026-05-24T06:23:39.262Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}}, \"count\": 27, \"total\": 27, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8995}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "1b693d83-fa90-49db-88f1-4fb351392bf1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-spatial-reconvla-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T10:58:57.165Z\\\", \\\"updated_at\\\": \\\"2026-05-24T11:00:32.832Z\\\", \\\"hypothesis\\\": \\\"ReconVLA reconstruction-based baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the reconvla baseline.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 261844, \\\"tmux_session\\\": \\\"spatial-reconvla-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_reconvla_s47.log\\\"}}, \\\"eval-supp-spatial-k2mean-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T10:58:53.820Z\\\", \\\"updated_at\\\": \\\"2026-05-24T11:00:26.172Z\\\", \\\"hypothesis\\\": \\\"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 845121, \\\"tmux_session\\\": \\\"spatial-k2mean-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_k2mean_s47.log\\\"}}, \\\"eval-supp-spatial-adapt-tau025-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T10:58:50.342Z\\\", \\\"updated_at\\\": \\\"2026-05-24T11:00:19.541Z\\\", \\\"hypothesis\\\": \\\"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --adaptive_threshold 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 844595, \\\"tmux_session\\\": \\\"spatial-adapt-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_adapt_s47.log\\\"}}, \\\"eval-supp-spatial-vla-only-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T10:58:43.441Z\\\", \\\"updated_at\\\": \\\"2026-05-24T11:00:12.802Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Spatial at seed 47 for seed-extension coverage. Extends 3-seed mean to 4th seed.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 2\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 844299, \\\"tmux_session\\\": \\\"spatial-vla-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_vla_s47.log\\\"}}, \\\"eval-supp-spatial-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:49:40.206Z\\\", \\\"updated_at\\\": \\\"2026-05-24T10:58:46.991Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\\\", \\\"parent\\\": \\\"eval-supp-spatial-crm-norm005-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"235730\\\", \\\"tmux_session\\\": \\\"eval-spatial-crm-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"submitted_at\\\": \\\"2026-05-24T06:50:07Z\\\", \\\"submitted_via\\\": \\\"ssh_execute_tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"train-crm-pi05-unified-3suite-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T10:38:31.224Z\\\", \\\"updated_at\\\": \\\"2026-05-24T10:39:56.094Z\\\", \\\"hypothesis\\\": \\\"π0.5 unified 3-suite (Spatial+Goal+Object) CRM training retry with batch_size=256 (was 32). D135: Long dropped due to DDL. obs_dim=2048, ~194K samples, 50 epochs. Parent killed due to 55h ETA; bs256 targets ~7-8h.\\\", \\\"parent\\\": \\\"train-crm-pi05-unified-3suite\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/train_crm.py --benchmark object spatial goal --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ --obs_dim 2048 --epochs 50 --batch_size 256 --lr 1e-3 --output_dir /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": 0, \\\"pid\\\": 326310, \\\"model_name\\\": \\\"pi05\\\", \\\"obs_dim\\\": 2048, \\\"data_count\\\": 194485, \\\"data_path\\\": \\\"/root/autodl-tmp/crm_cache_pi05_2048/\\\", \\\"data_breakdown\\\": {\\\"object\\\": 72507, \\\"spatial\\\": 60250, \\\"goal\\\": 61728}, \\\"seed\\\": 42, \\\"batch_size\\\": 256, \\\"epochs\\\": 50, \\\"lr\\\": 0.001, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/train-crm-pi05-unified-3suite-r2.log\\\", \\\"tmux_session\\\": \\\"train-crm-pi05-unified-3suite-r2\\\", \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"N/A (training job, not eval)\\\"}}, \\\"eval-supp-long-k2mean-s47-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T09:52:10.417Z\\\", \\\"updated_at\\\": \\\"2026-05-24T09:53:45.939Z\\\", \\\"hypothesis\\\": \\\"Long s47 K=2 mean baseline for seed extension (r2 on bjb2-28827). Sixth seed to tighten CI for Long suite K2mean method.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"eval_data\\\": \\\"LIBERO-Long 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"long-k2mean-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_long_k2mean_s47.log\\\", \\\"gpu\\\": 5, \\\"pid\\\": 205647}}, \\\"eval-supp-obj-reconvla-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T09:52:06.114Z\\\", \\\"updated_at\\\": \\\"2026-05-24T09:53:35.694Z\\\", \\\"hypothesis\\\": \\\"Object s47 Reconvla baseline, only missing Object s47 method. Completes Object suite seed extension coverage.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark object --mode reconvla --seed 47 --n_rollouts 20 --K 2\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\", \\\"eval_data\\\": \\\"LIBERO-Object 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"obj-reconvla-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_obj_reconvla_s47.log\\\", \\\"gpu\\\": 4, \\\"pid\\\": 200690}}, \\\"eval-supp-goal-reconvla-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T09:52:02.749Z\\\", \\\"updated_at\\\": \\\"2026-05-24T09:53:29.313Z\\\", \\\"hypothesis\\\": \\\"Goal s47 Reconvla baseline for seed extension. Sixth seed to tighten CI for Goal suite Reconvla method.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 47 --n_rollouts 20 --K 2\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\", \\\"eval_data\\\": \\\"LIBERO-Goal 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"goal-reconvla-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_goal_reconvla_s47.log\\\", \\\"gpu\\\": 3, \\\"pid\\\": 200418}}, \\\"eval-supp-goal-k2mean-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T09:51:59.402Z\\\", \\\"updated_at\\\": \\\"2026-05-24T09:53:22.862Z\\\", \\\"hypothesis\\\": \\\"Goal s47 K=2 mean baseline for seed extension. Sixth seed to tighten CI for Goal suite K2mean method.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"eval_data\\\": \\\"LIBERO-Goal 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"goal-k2mean-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_goal_k2mean_s47.log\\\", \\\"gpu\\\": 2, \\\"pid\\\": 205380}}, \\\"eval-supp-goal-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T09:51:56.065Z\\\", \\\"updated_at\\\": \\\"2026-05-24T09:53:16.020Z\\\", \\\"hypothesis\\\": \\\"Goal s47 CRM obs-only (norm=0.05) eval for seed extension. Sixth seed to tighten CI for Goal suite CRM method.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Goal 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"goal-crm-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_goal_crm_s47.log\\\", \\\"gpu\\\": 1, \\\"pid\\\": 199883}}, \\\"eval-supp-goal-adapt-tau025-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T09:51:52.528Z\\\", \\\"updated_at\\\": \\\"2026-05-24T09:53:08.583Z\\\", \\\"hypothesis\\\": \\\"Goal s47 Adaptive gating (tau=0.25) eval for seed extension. Sixth seed to tighten CI for Goal suite Adaptive method.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --adaptive_threshold 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Goal 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"goal-adapt-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_goal_adapt_s47.log\\\", \\\"gpu\\\": 0, \\\"pid\\\": 205107}}, \\\"eval-supp-goal-vla-only-s47-r3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T09:31:15.967Z\\\", \\\"updated_at\\\": \\\"2026-05-24T09:32:36.215Z\\\", \\\"hypothesis\\\": \\\"Goal s47 VLA-only (K=1) baseline, second re-run after r2 was killed for CRM training priority. Fills Goal s47 seed extension for variance analysis.\\\", \\\"parent\\\": \\\"eval-supp-goal-vla-only-s47-r2\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO goal benchmark\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"pretrained SmolVLA /root/autodl-tmp/models/smolvla_libero/\\\", \\\"eval_data\\\": \\\"LIBERO goal, 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"goal-vla-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_goal_vla_s47.log\\\", \\\"gpu\\\": 2, \\\"pid\\\": 307664}}, \\\"eval-supp-long-vla-only-s47-r4\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T09:31:12.366Z\\\", \\\"updated_at\\\": \\\"2026-05-24T09:32:29.415Z\\\", \\\"hypothesis\\\": \\\"Long s47 VLA-only (K=1) baseline, third re-run after r2/r3 were killed for CRM training priority. Fills Long s47 seed extension for variance analysis.\\\", \\\"parent\\\": \\\"eval-supp-long-vla-only-s47-r3\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO long benchmark\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"checkpoint_source\\\": \\\"pretrained SmolVLA /root/autodl-tmp/models/smolvla_libero/\\\", \\\"eval_data\\\": \\\"LIBERO long, 10 tasks x 20 rollouts\\\", \\\"tmux_session\\\": \\\"long-vla-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_long_vla_s47.log\\\", \\\"gpu\\\": 1, \\\"pid\\\": 307463}}, \\\"eval-supp-obj-adapt-tau025-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T08:38:16.262Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:40:20.644Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Object suite seed47. Sixth seed extending Object Adaptive coverage for variance analysis.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"tmux_session\\\": \\\"obj-adapt-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_obj_adapt_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+Adaptive CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Object 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}}, \\\"eval-supp-obj-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T08:38:10.740Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:40:14.365Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only norm=0.05 on Object suite seed47. Sixth seed extending Object CRM coverage for variance analysis.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"tmux_session\\\": \\\"obj-crm-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_obj_crm_norm005_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Object 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}}, \\\"eval-supp-obj-k2mean-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T08:38:07.452Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:40:07.860Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Object suite seed47. Sixth seed extending Object K2mean coverage for variance analysis.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"tmux_session\\\": \\\"obj-k2mean-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_obj_k2mean_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Object 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}}, \\\"eval-supp-obj-vla-only-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T08:38:03.765Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:39:52.861Z\\\", \\\"hypothesis\\\": \\\"VLA-only (K=1) baseline on Object suite seed47. Sixth seed extending Object VLA-only coverage for variance analysis.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"tmux_session\\\": \\\"obj-vla-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_obj_vla_only_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Object 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}}, \\\"eval-supp-long-k2mean-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:34:23.532Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:27:00.000Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Long suite seed47. Renamed from eval-supp-long-vla-only-s47 (was misnamed at creation — actual command uses --baseline_mode mean --K 2). Paired with Adapt-s47 for matched-seed comparison.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"tmux_session\\\": \\\"long-vla-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-vla-only-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"parent\\\": \\\"eval-supp-long-vla-only-s46\\\"}}, \\\"eval-supp-k2mean-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:55.833Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:30.230Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"tmux_session\\\": \\\"spatial-k2mean-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}}, \\\"eval-supp-reconvla-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:47.910Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:23.847Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"tmux_session\\\": \\\"spatial-reconvla-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+Reconvla\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\"}}, \\\"eval-supp-adapt-tau025-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:43.884Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:17.441Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80.5%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"tmux_session\\\": \\\"spatial-adapt-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+Adaptive CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}}, \\\"eval-supp-vla-only-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:40.347Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:10.979Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~78.7%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"tmux_session\\\": \\\"spatial-vla-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}}, \\\"eval-supp-long-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:52:08.968Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:53:16.695Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"tmux_session\\\": \\\"long-crm-s47\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}}, \\\"eval-supp-long-reconvla-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:52:05.630Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:53:02.593Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"tmux_session\\\": \\\"long-reconvla-s47\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\"}}, \\\"eval-supp-long-adapt-tau025-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:34:20.287Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:38:39.651Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"tmux_session\\\": \\\"long-adapt-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-adapt-tau025-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"parent\\\": \\\"eval-supp-long-adapt-tau025-s46-r2\\\"}}, \\\"precompute-pi05-long-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:18:31.140Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:23:39.262Z\\\", \\\"hypothesis\\\": \\\"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": 114507, \\\"data_path\\\": \\\"/root/autodl-tmp/crm_cache_pi05_2048/long/\\\", \\\"data_count\\\": 136090, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\\\"}}}, \\\"count\\\": 27, \\\"total\\\": 27, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.8995}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-spatial-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:58:57.165Z\", \"updated_at\": \"2026-05-24T11:00:32.832Z\", \"hypothesis\": \"ReconVLA reconstruction-based baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the reconvla baseline.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb2-40593\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"gpu\": \"cuda:0\", \"pid\": 261844, \"tmux_session\": \"spatial-reconvla-s47\", \"log_path\": \"/tmp/eval_spatial_reconvla_s47.log\"}}, \"eval-supp-spatial-k2mean-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:58:53.820Z\", \"updated_at\": \"2026-05-24T11:00:26.172Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"gpu\": \"cuda:3\", \"pid\": 845121, \"tmux_session\": \"spatial-k2mean-s47\", \"log_path\": \"/tmp/eval_spatial_k2mean_s47.log\"}}, \"eval-supp-spatial-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:58:50.342Z\", \"updated_at\": \"2026-05-24T11:00:19.541Z\", \"hypothesis\": \"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --adaptive_threshold 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"gpu\": \"cuda:2\", \"pid\": 844595, \"tmux_session\": \"spatial-adapt-s47\", \"log_path\": \"/tmp/eval_spatial_adapt_s47.log\"}}, \"eval-supp-spatial-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:58:43.441Z\", \"updated_at\": \"2026-05-24T11:00:12.802Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial at seed 47 for seed-extension coverage. Extends 3-seed mean to 4th seed.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 2\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"gpu\": \"cuda:0\", \"pid\": 844299, \"tmux_session\": \"spatial-vla-s47\", \"log_path\": \"/tmp/eval_spatial_vla_s47.log\"}}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T10:58:46.991Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"train-crm-pi05-unified-3suite-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:38:31.224Z\", \"updated_at\": \"2026-05-24T10:39:56.094Z\", \"hypothesis\": \"π0.5 unified 3-suite (Spatial+Goal+Object) CRM training retry with batch_size=256 (was 32). D135: Long dropped due to DDL. obs_dim=2048, ~194K samples, 50 epochs. Parent killed due to 55h ETA; bs256 targets ~7-8h.\", \"parent\": \"train-crm-pi05-unified-3suite\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark object spatial goal --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ --obs_dim 2048 --epochs 50 --batch_size 256 --lr 1e-3 --output_dir /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/\", \"server\": \"bjb1-18228\", \"gpu\": 0, \"pid\": 326310, \"model_name\": \"pi05\", \"obs_dim\": 2048, \"data_count\": 194485, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/\", \"data_breakdown\": {\"object\": 72507, \"spatial\": 60250, \"goal\": 61728}, \"seed\": 42, \"batch_size\": 256, \"epochs\": 50, \"lr\": 0.001, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-pi05-unified-3suite-r2.log\", \"tmux_session\": \"train-crm-pi05-unified-3suite-r2\", \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training job, not eval)\"}}, \"eval-supp-long-k2mean-s47-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:52:10.417Z\", \"updated_at\": \"2026-05-24T09:53:45.939Z\", \"hypothesis\": \"Long s47 K=2 mean baseline for seed extension (r2 on bjb2-28827). Sixth seed to tighten CI for Long suite K2mean method.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Long 10 tasks x 20 rollouts\", \"tmux_session\": \"long-k2mean-s47\", \"log_path\": \"/tmp/eval_long_k2mean_s47.log\", \"gpu\": 5, \"pid\": 205647}}, \"eval-supp-obj-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:52:06.114Z\", \"updated_at\": \"2026-05-24T09:53:35.694Z\", \"hypothesis\": \"Object s47 Reconvla baseline, only missing Object s47 method. Completes Object suite seed extension coverage.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark object --mode reconvla --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-reconvla\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"tmux_session\": \"obj-reconvla-s47\", \"log_path\": \"/tmp/eval_obj_reconvla_s47.log\", \"gpu\": 4, \"pid\": 200690}}, \"eval-supp-goal-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:52:02.749Z\", \"updated_at\": \"2026-05-24T09:53:29.313Z\", \"hypothesis\": \"Goal s47 Reconvla baseline for seed extension. Sixth seed to tighten CI for Goal suite Reconvla method.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-reconvla\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-reconvla-s47\", \"log_path\": \"/tmp/eval_goal_reconvla_s47.log\", \"gpu\": 3, \"pid\": 200418}}, \"eval-supp-goal-k2mean-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:51:59.402Z\", \"updated_at\": \"2026-05-24T09:53:22.862Z\", \"hypothesis\": \"Goal s47 K=2 mean baseline for seed extension. Sixth seed to tighten CI for Goal suite K2mean method.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"n/a-baseline\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-k2mean-s47\", \"log_path\": \"/tmp/eval_goal_k2mean_s47.log\", \"gpu\": 2, \"pid\": 205380}}, \"eval-supp-goal-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:51:56.065Z\", \"updated_at\": \"2026-05-24T09:53:16.020Z\", \"hypothesis\": \"Goal s47 CRM obs-only (norm=0.05) eval for seed extension. Sixth seed to tighten CI for Goal suite CRM method.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-crm-s47\", \"log_path\": \"/tmp/eval_goal_crm_s47.log\", \"gpu\": 1, \"pid\": 199883}}, \"eval-supp-goal-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:51:52.528Z\", \"updated_at\": \"2026-05-24T09:53:08.583Z\", \"hypothesis\": \"Goal s47 Adaptive gating (tau=0.25) eval for seed extension. Sixth seed to tighten CI for Goal suite Adaptive method.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --adaptive_threshold 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-adapt-s47\", \"log_path\": \"/tmp/eval_goal_adapt_s47.log\", \"gpu\": 0, \"pid\": 205107}}, \"eval-supp-goal-vla-only-s47-r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:31:15.967Z\", \"updated_at\": \"2026-05-24T09:32:36.215Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline, second re-run after r2 was killed for CRM training priority. Fills Goal s47 seed extension for variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s47-r2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO goal benchmark\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"pretrained SmolVLA /root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO goal, 10 tasks x 20 rollouts\", \"tmux_session\": \"goal-vla-s47\", \"log_path\": \"/tmp/eval_goal_vla_s47.log\", \"gpu\": 2, \"pid\": 307664}}, \"eval-supp-long-vla-only-s47-r4\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:31:12.366Z\", \"updated_at\": \"2026-05-24T09:32:29.415Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline, third re-run after r2/r3 were killed for CRM training priority. Fills Long s47 seed extension for variance analysis.\", \"parent\": \"eval-supp-long-vla-only-s47-r3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO long benchmark\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 47, \"checkpoint_source\": \"pretrained SmolVLA /root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO long, 10 tasks x 20 rollouts\", \"tmux_session\": \"long-vla-s47\", \"log_path\": \"/tmp/eval_long_vla_s47.log\", \"gpu\": 1, \"pid\": 307463}}, \"eval-supp-obj-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T08:38:16.262Z\", \"updated_at\": \"2026-05-24T08:40:20.644Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object suite seed47. Sixth seed extending Object Adaptive coverage for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"obj-adapt-s47\", \"log_path\": \"/tmp/eval_obj_adapt_s47.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA+Adaptive CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-supp-obj-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T08:38:10.740Z\", \"updated_at\": \"2026-05-24T08:40:14.365Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Object suite seed47. Sixth seed extending Object CRM coverage for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"obj-crm-s47\", \"log_path\": \"/tmp/eval_obj_crm_norm005_s47.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-supp-obj-k2mean-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T08:38:07.452Z\", \"updated_at\": \"2026-05-24T08:40:07.860Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed47. Sixth seed extending Object K2mean coverage for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"obj-k2mean-s47\", \"log_path\": \"/tmp/eval_obj_k2mean_s47.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-obj-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T08:38:03.765Z\", \"updated_at\": \"2026-05-24T08:39:52.861Z\", \"hypothesis\": \"VLA-only (K=1) baseline on Object suite seed47. Sixth seed extending Object VLA-only coverage for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"obj-vla-s47\", \"log_path\": \"/tmp/eval_obj_vla_only_s47.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-long-k2mean-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:23.532Z\", \"updated_at\": \"2026-05-24T08:27:00.000Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed47. Renamed from eval-supp-long-vla-only-s47 (was misnamed at creation — actual command uses --baseline_mode mean --K 2). Paired with Adapt-s47 for matched-seed comparison.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-vla-s47\", \"log_path\": \"logs/eval-supp-long-vla-only-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:55.833Z\", \"updated_at\": \"2026-05-24T07:18:30.230Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"spatial-k2mean-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:47.910Z\", \"updated_at\": \"2026-05-24T07:18:23.847Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"spatial-reconvla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Reconvla\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:43.884Z\", \"updated_at\": \"2026-05-24T07:18:17.441Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80.5%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"spatial-adapt-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Adaptive CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:40.347Z\", \"updated_at\": \"2026-05-24T07:18:10.979Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~78.7%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"spatial-vla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:08.968Z\", \"updated_at\": \"2026-05-24T06:53:16.695Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-crm-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:05.630Z\", \"updated_at\": \"2026-05-24T06:53:02.593Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-reconvla-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:20.287Z\", \"updated_at\": \"2026-05-24T06:38:39.651Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-adapt-s47\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46-r2\"}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:31.140Z\", \"updated_at\": \"2026-05-24T06:23:39.262Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}}, \"count\": 27, \"total\": 27, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8995}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "e198102d-04ac-47b6-8cd9-19beb2675c13",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HydovAb9s8P3M94cFwJnk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14263,
      "cache_read_input_tokens": 35263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14263
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

### Assistant

_source line 28_

Most of the s45/s46 experiments aren't in the current RUNNING list. Let me search for them by status filter or get the full list to find them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "8ae6589c-3cc4-44ed-8fa4-77d96aa2b10b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HydovAb9s8P3M94cFwJnk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14263,
      "cache_read_input_tokens": 35263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14263
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

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01GhcURbsnCLUtu43LLXD8zT`</summary>

```json
{
  "filters": {
    "status": "DONE"
  },
  "project": "acr-vla-conformal-refinement",
  "limit": 200,
  "fields": [
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "ff475e21-a6b0-49db-a789-ca4dafd24408",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HydovAb9s8P3M94cFwJnk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14263,
      "cache_read_input_tokens": 35263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14263
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

### Tool result

_source line 30 · 2026-05-24T11:02:09.404Z_

<details><summary>↩ Tool result · `toolu_01GhcURbsnCLUtu43LLXD8zT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-unified-3suite\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-spatial-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-goal-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-goal-bjb1-32546\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-pi05-spatial-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-crm-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-k2mean-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-k2mean-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-crm-norm005-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-adapt-tau025-s45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-ablation-tau040-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-ablation-tau015-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-ablation-tau010-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-crm-norm005-obj-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-goal-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-goal-reconvla-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-k2mean-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r6\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-goal-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-crm-norm005-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-k2-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-adapt-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-object-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-crm005-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm02-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed55\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-features-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-adapt-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau035-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r5-resumed\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau035-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-3dir-adaptive-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-3dir-norm03-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-3dir-reconvla-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-3dir-norm01-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-3dir-norm005-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-goal-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-spatial-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-object-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-object-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r5\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-long-2048\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-lerobot-goal-seed44-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-smolvla-3suite-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-goal-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-object-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}}, \"count\": 200, \"total\": 780, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9449}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "aed73dcc-b035-4e2f-8396-23ceb9a7db99",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-long-crm-norm005-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train-crm-pi05-unified-3suite\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-pi05-object-2048-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-openvla-object-vla-only-seed42-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-vla-only-spatial-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-vla-only-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-spatial-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train-crm-pi05-spatial-k1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train-crm-pi05-goal-k1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-vla-only-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-vla-only-s47-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-vla-only-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-goal-vla-only-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-reconvla-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-k2mean-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-spatial-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-adapt-tau025-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"crm-train-openvla-k1-multiscale-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-k2mean-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-reconvla-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-crm-norm005-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-adapt-tau025-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-obj-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-obj-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-pi05-goal-2048-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-vla-only-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-pi05-spatial-2048-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-smolvla-goal-bjb1-32546\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-goal-vla-only-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-reconvla-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"crm-train-pi05-spatial-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-norm003-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-adaptive-k-spatial-p90-seed44-bjb2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-vla-only-wrapper-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-reconvla-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-k2mean-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-long-seed42-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-reconvla-obj-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-k2mean-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-k2mean-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-adapt-tau025-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-crm-norm005-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-adapt-tau025-s45-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-k2mean-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-vla-only-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-reconvla-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-adapt-tau025-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-crm-norm005-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-reconvla-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-k2mean-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-adapt-tau025-obj-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-k2mean-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-crm-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-k2mean-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-long-reconvla-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-reconvla-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-obj-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-reconvla-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-crm-norm005-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-adapt-tau025-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-k2mean-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-obj-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-vla-only-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-k2mean-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-obj-vla-only-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-vla-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-k2mean-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-long-reconvla-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-long-crm-norm005-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-long-adapt-tau025-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-obj-adapt-tau025-s45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-crm-norm005-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-long-adapt-tau025-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-reconvla-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-ablation-tau040-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-ablation-tau015-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-object-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-ablation-tau010-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-obj-reconvla-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-vla-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-vla-only-wrapper-s44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-spatial-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-vla-only-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-goal-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-adapt-tau025-obj-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-crm-norm005-obj-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-goal-vla-only-wrapper-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-vla-only-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-reconvla-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-obj-reconvla-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-goal-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-object-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-goal-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-goal-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-obj-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-adapt-tau025-goal-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-goal-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-adapt-tau025-obj-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-goal-reconvla-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-k2mean-spatial-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-reconvla-spatial-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-reconvla-spatial-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-goal-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-object-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-adapt-tau025-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-crm005-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-reconvla-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"train-crm-unified-4suite-r6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-goal-vla-only-wrapper-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-adapt-tau025-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-crm-norm005-spatial-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-spatial-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-reconvla-k2-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-spatial-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-spatial-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-obj-adapt-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-object-vla-only-wrapper-s44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-object-vla-only-wrapper-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-object-vla-only-wrapper-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-reconvla-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-crm005-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau035-spatial-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau015-spatial-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm02-spatial-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-spatial-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-openvla-object-baseline-seed42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm02-seed55\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-pi05-features-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-smolvla-goal-shard2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-smolvla-goal-shard1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-smolvla-goal-shard0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-long-seed2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-long-seed1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-long-seed0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-crm-spatial-seed42-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-crm-spatial-seed43-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-crm-spatial-seed44-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-crm-goal-seed42-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-crm-goal-seed43-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-crm-goal-seed44-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-obj-adapt-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-crm-norm02-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-adaptive-tau015-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-adaptive-tau025-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-adaptive-tau035-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"train-crm-unified-4suite-r5-resumed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-object-vla-only-wrapper-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-object-vla-only-wrapper-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-object-vla-only-wrapper-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-obj-crm005-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-adapt-tau035-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-adapt-tau025-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-adapt-tau015-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-crm-norm02-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-3dir-adaptive-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-3dir-norm03-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-3dir-reconvla-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-3dir-norm01-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-3dir-norm005-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-pi05-goal-2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"precompute-pi05-spatial-2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"precompute-pi05-object-2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-smolvla-crm-object-seed43-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-smolvla-crm-object-seed42-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-smolvla-crm-object-seed44-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"train-crm-unified-4suite-r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-crm-goal-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-crm-goal-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-crm-spatial-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-crm-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-crm-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-pi05-long-2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-lerobot-goal-seed44-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-smolvla-lerobot-goal-seed43-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-smolvla-lerobot-spatial-seed43-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train-crm-smolvla-3suite-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-smolvla-lerobot-goal-seed43-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-smolvla-lerobot-spatial-seed43-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-smolvla-lerobot-object-seed44-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-smolvla-lerobot-object-seed43-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 200, \\\"total\\\": 780, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.9449}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-unified-3suite\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-spatial-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-pi05-goal-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-goal-bjb1-32546\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-pi05-spatial-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-crm-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-k2mean-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-k2mean-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-crm-norm005-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-adapt-tau025-s45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-ablation-tau040-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-ablation-tau015-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-ablation-tau010-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-crm-norm005-obj-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-goal-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-goal-reconvla-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-k2mean-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r6\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-goal-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-crm-norm005-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-k2-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-adapt-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-object-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-crm005-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm02-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed55\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-features-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-adapt-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau035-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r5-resumed\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau035-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-3dir-adaptive-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-3dir-norm03-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-3dir-reconvla-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-3dir-norm01-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-3dir-norm005-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-goal-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-spatial-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-object-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-object-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r5\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-long-2048\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-lerobot-goal-seed44-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-smolvla-3suite-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-goal-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-object-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}}, \"count\": 200, \"total\": 780, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9449}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 31_

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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "7a13d684-fb9d-47f1-853b-e6a289dc966e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Sp2MqqtWci5q1kNhQm7GkA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10931,
      "cache_read_input_tokens": 49526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10931
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

_source line 32_

6 of the 7 listed experiments are already marked DONE/success in registry. Only `eval-supp-spatial-crm-norm005-s47` is still RUNNING. Let me verify on bjb2-40593.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "346c768c-3700-4a41-ae36-47107d53fdf2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Sp2MqqtWci5q1kNhQm7GkA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10931,
      "cache_read_input_tokens": 49526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10931
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

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DeC29GbPPDNnFPfBFbdYcQ`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "tmux has-session -t eval-spatial-crm-s47",
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "f180e082-49b0-43c9-8e94-d034b84b7d9e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Sp2MqqtWci5q1kNhQm7GkA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10931,
      "cache_read_input_tokens": 49526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10931
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

_source line 34 · 2026-05-24T11:02:21.097Z_

<details><summary>↩ Tool result · `toolu_01DeC29GbPPDNnFPfBFbdYcQ`</summary>

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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "b15282db-673e-4028-ad76-7b5704987649",
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

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019U9XEi5b19wQ4nbmHm8Mfo`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls -la /tmp/eval_spatial_crm_s47.log",
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "9e406366-3bf4-414c-ad83-ea1a488a3efc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Sp2MqqtWci5q1kNhQm7GkA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10931,
      "cache_read_input_tokens": 49526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10931
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

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JuBTCuKDV4UFDxeUmEa9Sw`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed47.json",
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "0d64c3a9-69c0-4b15-a5ed-e386c9fbb37f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Sp2MqqtWci5q1kNhQm7GkA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10931,
      "cache_read_input_tokens": 49526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10931
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

_source line 37 · 2026-05-24T11:02:23.232Z_

<details><summary>↩ Tool result · `toolu_019U9XEi5b19wQ4nbmHm8Mfo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 7563 May 24 18:15 /tmp/eval_spatial_crm_s47.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.09}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "0381688a-4189-417c-ada9-24b2c1f171cf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 7563 May 24 18:15 /tmp/eval_spatial_crm_s47.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.09}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 7563 May 24 18:15 /tmp/eval_spatial_crm_s47.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.09}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-24T11:02:23.618Z_

<details><summary>↩ Tool result · `toolu_01JuBTCuKDV4UFDxeUmEa9Sw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1709 May 24 18:15 /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "d0e24446-c22a-4543-a946-c5bca57d6dc7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 1709 May 24 18:15 /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1709 May 24 18:15 /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01A9oRMpABDkQXhuVGjD82Wd`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "tmux has-session -t eval-spatial-crm-s47 2>&1; echo \"exit=$?\"",
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "93c45385-5f40-4bb4-9cdf-545afb5b1381",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UQcyYYquNCpuK3Aq2A9gFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1488,
      "cache_read_input_tokens": 60457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1488
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 40 · 2026-05-24T11:02:30.439Z_

<details><summary>↩ Tool result · `toolu_01A9oRMpABDkQXhuVGjD82Wd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"can't find session: eval-spatial-crm-s47\\nexit=1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "7c52c244-dd6e-4ab1-b9ff-9d691ff5a010",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"can't find session: eval-spatial-crm-s47\\\\nexit=1\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"can't find session: eval-spatial-crm-s47\\nexit=1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01T8LvhWbz3tcMUzzNgUBvWk`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed47.json",
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "5404ff64-9bb4-409c-a344-192c2aff2703",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UQcyYYquNCpuK3Aq2A9gFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1488,
      "cache_read_input_tokens": 60457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1488
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 42 · 2026-05-24T11:02:31.020Z_

<details><summary>↩ Tool result · `toolu_01T8LvhWbz3tcMUzzNgUBvWk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.805,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "064dc590-e1d1-4134-a53c-08b0bc852737",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"crm_obs_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"spatial\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.805,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.805,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017eiXjwizemLJi23BXEV7Nt`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "tail -30 /tmp/eval_spatial_crm_s47.log",
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "e45417f3-6c38-4a6b-a282-6be58f55bc8b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UQcyYYquNCpuK3Aq2A9gFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1488,
      "cache_read_input_tokens": 60457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1488
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 44 · 2026-05-24T11:02:31.744Z_

<details><summary>↩ Tool result · `toolu_017eiXjwizemLJi23BXEV7Nt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 0/10\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 0/15\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 10/20, success so far: 8/10\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 15/20, success so far: 12/15\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 20/20, success so far: 17/20\\n[pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate] success rate: 85.0% (17/20)\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 5/20, success so far: 2/5\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 10/20, success so far: 7/10\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 15/20, success so far: 11/15\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 20/20, success so far: 14/20\\n[pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 15/20, success so far: 13/15\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 20/20, success so far: 18/20\\n[pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 90.0% (18/20)\\n\\n============================================================\\nOverall success rate (crm_obs_only): 80.5% (161/200)\\n============================================================\\n[eval] Results saved to logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "0b523c72-ef7e-4023-b1e8-af8468c0a506",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 0/10\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 0/15\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 0/20\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 10/20, success so far: 8/10\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 15/20, success so far: 12/15\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 20/20, success so far: 17/20\\\\n[pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate] success rate: 85.0% (17/20)\\\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 5/20, success so far: 2/5\\\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 10/20, success so far: 7/10\\\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 15/20, success so far: 11/15\\\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 20/20, success so far: 14/20\\\\n[pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 15/20, success so far: 13/15\\\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 20/20, success so far: 18/20\\\\n[pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 90.0% (18/20)\\\\n\\\\n============================================================\\\\nOverall success rate (crm_obs_only): 80.5% (161/200)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 0/10\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 0/15\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 10/20, success so far: 8/10\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 15/20, success so far: 12/15\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 20/20, success so far: 17/20\\n[pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate] success rate: 85.0% (17/20)\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 5/20, success so far: 2/5\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 10/20, success so far: 7/10\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 15/20, success so far: 11/15\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 20/20, success so far: 14/20\\n[pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 15/20, success so far: 13/15\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 20/20, success so far: 18/20\\n[pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 90.0% (18/20)\\n\\n============================================================\\nOverall success rate (crm_obs_only): 80.5% (161/200)\\n============================================================\\n[eval] Results saved to logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 45_

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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "c434ae4c-84fe-48c5-928c-31a887e6d5d8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KYD2Z9io1wNZTcRW576b26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 61945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3578
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 46_

Confirmed complete: 80.5% (161/200). Let me update the registry for this experiment, plus set metrics and conclusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "52a6628b-d705-4576-9072-25fe7bedce4b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KYD2Z9io1wNZTcRW576b26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 61945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3578
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_0176jwqcFWiyiL2qny5u3cTU`</summary>

```json
{
  "exp_id": "eval-supp-spatial-crm-norm005-s47",
  "field": "checkpoint_path",
  "value": "n/a-eval-only",
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "d238bb3f-8929-4860-b660-f6dccbb1bf46",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KYD2Z9io1wNZTcRW576b26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 61945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3578
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01S4Cme5mtvfgp5Ky49DQPdL`</summary>

```json
{
  "exp_id": "eval-supp-spatial-crm-norm005-s47",
  "field": "log_path",
  "value": "/tmp/eval_spatial_crm_s47.log",
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "59901a8d-a13f-4aea-b71a-f5055820f958",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KYD2Z9io1wNZTcRW576b26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 61945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3578
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01975Uiig3ZV1FchqxRt5kj7`</summary>

```json
{
  "exp_id": "eval-supp-spatial-crm-norm005-s47",
  "field": "metrics",
  "value": {
    "overall_success_rate": 0.805,
    "successes": 161,
    "total": 200,
    "n_tasks": 10,
    "n_rollouts_per_task": 20,
    "output_file": "logs/eval_spatial_crm_obs_only_norm0.05_seed47.json"
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "4b912293-c72a-4065-8874-55d682eb12bd",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KYD2Z9io1wNZTcRW576b26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 61945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3578
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 50 · 2026-05-24T11:02:45.744Z_

<details><summary>↩ Tool result · `toolu_0176jwqcFWiyiL2qny5u3cTU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-crm-norm005-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T11:02:43.731Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}, \"checkpoint_path\": \"n/a-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.4616}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "7a680a6f-2061-4fcd-a871-9e0cc4b921da",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-crm-norm005-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:49:40.206Z\\\", \\\"updated_at\\\": \\\"2026-05-24T11:02:43.731Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\\\", \\\"parent\\\": \\\"eval-supp-spatial-crm-norm005-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"235730\\\", \\\"tmux_session\\\": \\\"eval-spatial-crm-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"submitted_at\\\": \\\"2026-05-24T06:50:07Z\\\", \\\"submitted_via\\\": \\\"ssh_execute_tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.4616}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-crm-norm005-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T11:02:43.731Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}, \"checkpoint_path\": \"n/a-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.4616}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-24T11:02:51.912Z_

<details><summary>↩ Tool result · `toolu_01S4Cme5mtvfgp5Ky49DQPdL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-crm-norm005-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T11:02:49.418Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.1484}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "5c38ba2e-1d76-4ff9-a9a4-c858be674fea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-crm-norm005-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:49:40.206Z\\\", \\\"updated_at\\\": \\\"2026-05-24T11:02:49.418Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\\\", \\\"parent\\\": \\\"eval-supp-spatial-crm-norm005-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"235730\\\", \\\"tmux_session\\\": \\\"eval-spatial-crm-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"submitted_at\\\": \\\"2026-05-24T06:50:07Z\\\", \\\"submitted_via\\\": \\\"ssh_execute_tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.1484}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-crm-norm005-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T11:02:49.418Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.1484}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-24T11:02:57.537Z_

<details><summary>↩ Tool result · `toolu_01975Uiig3ZV1FchqxRt5kj7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-crm-norm005-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T11:02:54.931Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"metrics\": {\"overall_success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.6085}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "dda211f0-09d9-4d6c-932f-4629b7e0cc79",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-crm-norm005-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:49:40.206Z\\\", \\\"updated_at\\\": \\\"2026-05-24T11:02:54.931Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\\\", \\\"parent\\\": \\\"eval-supp-spatial-crm-norm005-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"235730\\\", \\\"tmux_session\\\": \\\"eval-spatial-crm-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"submitted_at\\\": \\\"2026-05-24T06:50:07Z\\\", \\\"submitted_via\\\": \\\"ssh_execute_tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.805, \\\"successes\\\": 161, \\\"total\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20, \\\"output_file\\\": \\\"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.6085}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-crm-norm005-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T11:02:54.931Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"metrics\": {\"overall_success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.6085}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01YGPhujwhGEA2NRXVnvL9dC`</summary>

```json
{
  "exp_id": "eval-supp-spatial-crm-norm005-s47",
  "field": "status",
  "value": "DONE",
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "63a88930-b062-445a-9170-c7993147e25d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011zqtcHyXoSvysaTZGeaR3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3681,
      "cache_read_input_tokens": 65523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3681
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

_source line 54 · 2026-05-24T11:03:05.422Z_

<details><summary>↩ Tool result · `toolu_01YGPhujwhGEA2NRXVnvL9dC`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 1.9653}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "77682bd8-ae9b-4be6-b1a4-8ab4ab2506c9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.9653}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 1.9653}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_011LfwAf7Kr6fLgGfRH3YbHp`</summary>

```json
{
  "exp_id": "eval-supp-spatial-crm-norm005-s47",
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "0298192b-9c50-47e5-b7b4-c9649c6403c8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EGg38VCCX4mXqsoM6HVsCN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 274,
      "cache_read_input_tokens": 69204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 274
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

_source line 56 · 2026-05-24T11:03:12.625Z_

<details><summary>↩ Tool result · `toolu_011LfwAf7Kr6fLgGfRH3YbHp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-crm-norm005-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T11:03:11.288Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"metrics\": {\"overall_success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.2934}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "abdfd48a-6fc2-42a5-8ac0-d6442fce9d45",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-crm-norm005-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:49:40.206Z\\\", \\\"updated_at\\\": \\\"2026-05-24T11:03:11.288Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\\\", \\\"parent\\\": \\\"eval-supp-spatial-crm-norm005-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"235730\\\", \\\"tmux_session\\\": \\\"eval-spatial-crm-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"submitted_at\\\": \\\"2026-05-24T06:50:07Z\\\", \\\"submitted_via\\\": \\\"ssh_execute_tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.805, \\\"successes\\\": 161, \\\"total\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20, \\\"output_file\\\": \\\"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\"}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.2934}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-crm-norm005-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T11:03:11.288Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"metrics\": {\"overall_success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.2934}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01RFt1fmjXH8X21h9mz3yYSn`</summary>

```json
{
  "exp_id": "eval-supp-spatial-crm-norm005-s47",
  "field": "status",
  "value": "DONE",
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
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "b14e6f1f-ad87-49f9-b73f-1725e04daec5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01R5Es1g4YnHt8s9BRex5ti7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 69478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1154
      },
      "output_tokens": 78,
      "service_tier": "standard",
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

_source line 58 · 2026-05-24T11:03:26.342Z_

<details><summary>↩ Tool result · `toolu_01RFt1fmjXH8X21h9mz3yYSn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-crm-norm005-s47\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T11:03:21.940Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 15194.9, \"gpu_hours\": 4.22}, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"metrics\": {\"overall_success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T11:03:21.940Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.3822}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "a874bd9d-e93e-44eb-965d-9b2e52735676",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-crm-norm005-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:49:40.206Z\\\", \\\"updated_at\\\": \\\"2026-05-24T11:03:21.940Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\\\", \\\"parent\\\": \\\"eval-supp-spatial-crm-norm005-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"235730\\\", \\\"tmux_session\\\": \\\"eval-spatial-crm-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"submitted_at\\\": \\\"2026-05-24T06:50:07Z\\\", \\\"submitted_via\\\": \\\"ssh_execute_tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 15194.9, \\\"gpu_hours\\\": 4.22}, \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.805, \\\"successes\\\": 161, \\\"total\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20, \\\"output_file\\\": \\\"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-24T11:03:21.940Z\\\"}, \\\"hint\\\": \\\"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.3822}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-crm-norm005-s47\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T11:03:21.940Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 15194.9, \"gpu_hours\": 4.22}, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"metrics\": {\"overall_success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T11:03:21.940Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.3822}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

所有 7 个实验状态确认完毕：

| Exp ID | 当前状态 | 结论 | 操作 |
|---|---|---|---|
| eval-supp-spatial-reconvla-s46 | DONE | success | 已是 DONE，无需操作 |
| eval-supp-spatial-k2mean-s46 | DONE | success | 已是 DONE，无需操作 |
| eval-supp-spatial-adapt-tau025-s45-r3 | DONE | success | 已是 DONE，无需操作 |
| eval-supp-reconvla-obj-s45 | DONE | success | 已是 DONE，无需操作 |
| eval-smolvla-lerobot-goal-seed43-v3 | DONE | success | 已是 DONE，无需操作 |
| eval-smolvla-lerobot-spatial-seed43-v3 | DONE | success | 已是 DONE，无需操作 |
| **eval-supp-spatial-crm-norm005-s47** | **DONE (新)** | **success** | tmux 已消失，JSON 完整，**success_rate=0.805 (161/200)**。已更新 metrics + log_path + checkpoint_path + conclusion + status |

实际只有 1 个 RUNNING→DONE 的 registry 更新（eval-supp-spatial-crm-norm005-s47）。其余 6 个 registry 早已标记 DONE/success，无需处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "uuid": "fce8709a-3b6b-47ba-8c8b-a07acf47fdac",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PmRbdg34rJ1cFg3iCMezoP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 70632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1251
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

_source line 60_

所有 7 个实验状态确认完毕：

| Exp ID | 当前状态 | 结论 | 操作 |
|---|---|---|---|
| eval-supp-spatial-reconvla-s46 | DONE | success | 已是 DONE，无需操作 |
| eval-supp-spatial-k2mean-s46 | DONE | success | 已是 DONE，无需操作 |
| eval-supp-spatial-adapt-tau025-s45-r3 | DONE | success | 已是 DONE，无需操作 |
| eval-supp-reconvla-obj-s45 | DONE | success | 已是 DONE，无需操作 |
| eval-smolvla-lerobot-goal-seed43-v3 | DONE | success | 已是 DONE，无需操作 |
| eval-smolvla-lerobot-spatial-seed43-v3 | DONE | success | 已是 DONE，无需操作 |
| **eval-supp-spatial-crm-norm005-s47** | **DONE (新)** | **success** | tmux 已消失，JSON 完整，**success_rate=0.805 (161/200)**。已更新 metrics + log_path + checkpoint_path + conclusion + status |

实际只有 1 个 RUNNING→DONE 的 registry 更新（eval-supp-spatial-crm-norm005-s47）。其余 6 个 registry 早已标记 DONE/success，无需处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 141869,
  "duration_api_ms": 105736,
  "num_turns": 24,
  "stop_reason": "end_turn",
  "session_id": "1c6c9d52-cd13-4a27-8df9-af480a81e3ad",
  "total_cost_usd": 0.87266225,
  "usage": {
    "input_tokens": 22,
    "cache_creation_input_tokens": 70473,
    "cache_read_input_tokens": 578844,
    "output_tokens": 5649,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 70473,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 488,
        "cache_read_input_tokens": 70632,
        "cache_creation_input_tokens": 1251,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1251
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1339,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001449,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 22,
      "outputTokens": 5649,
      "cacheReadInputTokens": 578844,
      "cacheCreationInputTokens": 70473,
      "webSearchRequests": 0,
      "costUSD": 0.8712132499999999,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "79b822da-6243-4210-9c42-ee5f4653a082"
}
```

</details>

---
