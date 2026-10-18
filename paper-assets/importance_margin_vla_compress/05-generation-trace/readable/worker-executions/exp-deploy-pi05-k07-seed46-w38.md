# exp deploy pi05 k07 seed46 w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_exp_deploy_pi05_k07_seed46_w38_20260528T161831.log`
- **Structured JSON:** [`4f00fef66c1a35ff6d18.json`](../../sessions/4f/4f00fef66c1a35ff6d18.json)

## Before a recorded user message

36 recorded events

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
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
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
    "mcp__agent-ml-research__submit_training_job",
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
  "uuid": "d02e5fe7-40a2-4bde-a3a8-bf2ea9d7f959",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1780001400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4a75054e-1e13-493c-b9c9-e983bc5e8211",
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by checking GPU availability on westd-38929, then look up the v1 experiment in the registry for parameters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "af140f26-ac76-449b-a985-34303c2a6171",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HozZzwFBFn19xWtTD5fzhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12645,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12645
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014LMKNPm3eXBq3Eg4wiqnP6`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__update_registry",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "4d0fd0fd-77c8-4bae-9d7e-c7b5c22d87c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HozZzwFBFn19xWtTD5fzhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12645,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12645
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 6 · 2026-05-28T16:18:42.775Z_

<details><summary>↩ Tool result · `toolu_014LMKNPm3eXBq3Eg4wiqnP6`</summary>

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
  "tool_name": "mcp__agent-ml-research__submit_training_job"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
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
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "96f45c2d-f4fd-43e2-8d4a-106792967958",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 27
  }
}
```

</details>

---

### Assistant

_source line 7_

检查 GPU 状态和查询 v1 实验参数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "7fb211e2-9f13-4562-af3f-bb437723646a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URuQHkEP2qMoHWG53NuGEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2083,
      "cache_read_input_tokens": 24490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2083
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018Gj2SrHkR35NRZ83CkeP19`</summary>

```json
{
  "server": "westd-38929",
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
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "77242d8c-cd4d-4c49-b40c-48eb44db1906",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URuQHkEP2qMoHWG53NuGEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2083,
      "cache_read_input_tokens": 24490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2083
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HebTSavvkqQJuUMKoxUVPR`</summary>

```json
{
  "server": "westd-38929",
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
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "6b4ffc62-66b3-4496-9b35-58b3e613163e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URuQHkEP2qMoHWG53NuGEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2083,
      "cache_read_input_tokens": 24490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2083
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

_source line 10 · 2026-05-28T16:18:48.110Z_

<details><summary>↩ Tool result · `toolu_018Gj2SrHkR35NRZ83CkeP19`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 MiB, 97887 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "36509859-64e8-4a5d-94d5-221464835b29",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 0 MiB, 97887 MiB, 0 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.17}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 0 MiB, 97887 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_015LnsYDPsTEomRTHVumRzUb`</summary>

```json
{
  "filters": {
    "exp_id": "eval_pi05_l2norm_k07_long_seed46_strict_w38"
  },
  "project": "importance_margin_vla_compress",
  "fields": [
    "*"
  ],
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "0a0071c2-080a-4af1-87c8-a1f35296da7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URuQHkEP2qMoHWG53NuGEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2083,
      "cache_read_input_tokens": 24490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2083
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

_source line 12 · 2026-05-28T16:18:48.704Z_

<details><summary>↩ Tool result · `toolu_01HebTSavvkqQJuUMKoxUVPR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "3c8b430a-02e4-44b4-b305-26c20b9f5fc7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.59}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T16:18:51.233Z_

<details><summary>↩ Tool result · `toolu_015LnsYDPsTEomRTHVumRzUb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5094}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "4477edfe-931e-4581-9293-889acca4b12b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.5094}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5094}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
GPU 0 is completely free (0 MiB used, no processes). Let me search for the v1 experiment with a broader filter.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "42b047f2-b14a-4323-8a50-b63e9940cafc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzhfUCefbUudFJDXJXz34e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 26573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 728
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

_source line 15_

GPU 0 完全空闲（0 MiB / 97887 MiB，无进程）。v1 实验名精确匹配未找到，扩大搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "f9d134bf-1038-45db-88f7-628d574579cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzhfUCefbUudFJDXJXz34e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 26573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 728
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

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0174YXTJDjnR51kNoNndcQqi`</summary>

```json
{
  "filters": {
    "status": "FAILED"
  },
  "project": "importance_margin_vla_compress",
  "fields": [
    "exp_id",
    "status",
    "spec",
    "conclusion"
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
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "3428ed58-f1c6-4be1-93d8-e3fc09098bfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzhfUCefbUudFJDXJXz34e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 26573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 728
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

_source line 17 · 2026-05-28T16:18:58.399Z_

<details><summary>↩ Tool result · `toolu_0174YXTJDjnR51kNoNndcQqi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5403}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "a07ccc4e-a23d-416a-abec-0f993749e8be",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.5403}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5403}}"
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
No failed experiments found. Let me search more broadly for any pi05 l2norm k07 long experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "56542741-b4e2-4716-af41-bc656d8d22b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018akwLhmYYzvkeVohK5rYvt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 27301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 315
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_016q3cM8yAUDJahdmtEVuVqJ`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "fields": [
    "exp_id",
    "status",
    "spec"
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
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "eb61778a-b636-4d2d-a0cc-87852a175f11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018akwLhmYYzvkeVohK5rYvt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 27301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 315
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

_source line 20 · 2026-05-28T16:19:04.450Z_

<details><summary>↩ Tool result · `toolu_016q3cM8yAUDJahdmtEVuVqJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_pi05_l2norm_k05_long_seed47_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 47 --gpu 0\", \"server\": \"westd-38929\", \"gpu\": \"cuda:1\", \"pid\": 589899, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k05_long_seed47_w38.log\", \"model_name\": \"pi0.5\", \"seed\": 47, \"data_path\": \"libero_long\", \"data_count\": 500}}, \"eval_pi05_random_k085_long_seed47_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 47 --gpu 0\", \"server\": \"westd-38929\", \"gpu\": \"cuda:0\", \"pid\": 589824, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed47_w38.log\", \"model_name\": \"pi0.5\", \"seed\": 47, \"data_path\": \"libero_long\", \"data_count\": 500}}, \"eval_pi05_attn_k05_long_seed47_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 47 --gpu 0\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"pid\": 590036, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k05_long_seed47_w38.log\", \"model_name\": \"pi0.5\", \"seed\": 47, \"data_path\": \"libero_long\", \"data_count\": 500}}, \"eval_pi05_l2norm_k07_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"923767\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k07_long_seed46_strict_w41.log\", \"model_name\": \"pi0.5\", \"seed\": 46, \"data_path\": \"libero_10\", \"data_count\": 500, \"note\": \"Config confirmed correct: --keep_ratio 0.7. The k0.75 seed46 file is from a separate earlier experiment.\", \"checkpoint_path\": \"N/A\"}}, \"eval_openvla_l2norm_k095_long_seed43_w27\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 43 --gpu 0 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"545112\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed43_w27.log\", \"submitted_at\": \"2026-05-28T05:57:09.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21742.3, \"gpu_hours\": 6.04}}, \"eval_pi05_random_k05_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": \"cuda:2\", \"pid\": 899098, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed46_strict_w41.log\", \"submitted_at\": \"2026-05-28T08:54:56.681Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi0.5\", \"seed\": 46, \"data_path\": \"libero_long\", \"data_count\": 500, \"wall_clock_seconds\": 10436.4, \"gpu_hours\": 2.9}}, \"eval_pi05_random_k095_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 46\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:0\"], \"pid\": \"898746\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k095_long_seed46_strict_w41.log\", \"submitted_at\": \"2026-05-28T08:54:49.370Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi0.5\", \"seed\": 46, \"data_path\": \"libero_10\", \"data_count\": 500, \"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"wall_clock_seconds\": 9921.1, \"gpu_hours\": 2.76}}, \"eval_pi05_attn_k095_long_seed46_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": \"cuda:3\", \"pid\": 457257, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k095_long_seed46_strict_w38.log\", \"submitted_at\": \"2026-05-28T08:55:07.572Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi0.5\", \"seed\": 46, \"data_path\": \"libero_long\", \"data_count\": 500, \"wall_clock_seconds\": 8550.9, \"gpu_hours\": 2.38}}, \"eval_pi05_l2norm_k05_long_seed46_strict\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:0\"], \"pid\": \"168016\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k05_long_seed46_strict.log\", \"submitted_at\": \"2026-05-28T06:33:19.594Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"wall_clock_seconds\": 16984.9, \"gpu_hours\": 4.72}}, \"eval_openvla_random_k095_goal_seed42_v4\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_goal --num_episodes 50 --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-goal --unnorm_key libero_goal\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:2\"], \"pid\": \"147681\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_goal_seed42_v4.log\", \"submitted_at\": \"2026-05-28T05:47:11.255Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 19678.8, \"gpu_hours\": 5.47}}, \"eval_pi05_attn_k07_long_seed46_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:3\"], \"pid\": \"163384\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k07_long_seed46_strict_cqa1.log\", \"submitted_at\": \"2026-05-28T06:26:19.770Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 16528.8, \"gpu_hours\": 4.59}}, \"eval_pi05_l2norm_k095_long_seed46_strict_w27\": {\"status\": \"DONE\", \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 46\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"616102\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_long_seed46_strict_w27.log\", \"submitted_at\": \"2026-05-28T08:54:39.968Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi0.5\", \"seed\": 46, \"data_path\": \"libero_10\", \"data_count\": 500, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 7600.6, \"gpu_hours\": 2.11}}, \"eval_pi05_attn_k09_long_seed46_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"163026\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k09_long_seed46_strict_cqa1.log\", \"submitted_at\": \"2026-05-28T06:25:49.031Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval)\", \"wall_clock_seconds\": 16321.7, \"gpu_hours\": 4.53}}, \"eval_pi05_l2norm_k085_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:3\"], \"pid\": \"859388\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k085_long_seed46_strict_w41.log\", \"submitted_at\": \"2026-05-28T08:12:47.837Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval)\", \"wall_clock_seconds\": 9849.9, \"gpu_hours\": 2.74}}, \"eval_pi05_attn_k075_long_seed46_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"363743\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed46_strict_w38.log\", \"submitted_at\": \"2026-05-28T07:47:39.761Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"wall_clock_seconds\": 10653.9, \"gpu_hours\": 2.96}}, \"eval_pi05_random_k075_long_seed46_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:0\"], \"pid\": \"363188\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed46_strict_w38.log\", \"submitted_at\": \"2026-05-28T07:47:27.897Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"wall_clock_seconds\": 9567.8, \"gpu_hours\": 2.66}}, \"eval_pi05_random_k09_long_seed46_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_long_seed46_strict_w38.log\"}}, \"eval_pi05_attn_k05_long_seed46_strict\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:1\"], \"pid\": \"261876\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k05_long_seed46_strict.log\", \"submitted_at\": \"2026-05-28T06:34:24.685Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"wall_clock_seconds\": 11665.4, \"gpu_hours\": 3.24}}, \"eval_pi05_random_k07_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"744875\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_long_seed46_strict_w41.log\", \"submitted_at\": \"2026-05-28T06:37:42.521Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.70_libero_10_seed46.json\", \"wall_clock_seconds\": 9428.4, \"gpu_hours\": 2.62}}, \"eval_pi05_attn_k085_long_seed46_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:3\"], \"pid\": \"218239\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k085_long_seed46_strict_w38.log\", \"submitted_at\": \"2026-05-28T05:54:16.144Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10658.5, \"gpu_hours\": 2.96, \"checkpoint_path\": \"N/A (eval only)\"}}, \"eval_pi05_random_k085_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:0\"], \"pid\": \"697206\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed46_strict_w41.log\", \"submitted_at\": \"2026-05-28T05:53:31.834Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10694.6, \"gpu_hours\": 2.97, \"checkpoint_path\": \"N/A (eval only)\"}}, \"eval_pi05_l2norm_k09_long_seed46_strict_w27\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"549654\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k09_long_seed46_strict_w27.log\", \"submitted_at\": \"2026-05-28T06:25:16.159Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"wall_clock_seconds\": 8764.6, \"gpu_hours\": 2.43}}, \"eval_pi05_l2norm_k075_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:2\"], \"pid\": \"697663\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k075_long_seed46_strict_w41.log\", \"submitted_at\": \"2026-05-28T05:53:56.633Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8956.0, \"gpu_hours\": 2.49}}, \"eval_pi05_l2norm_k07_long_seed46_strict_w38_v2\": {\"status\": \"PREPARING\"}, \"eval_pi05_attn_k07_long_seed45_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:3\"], \"pid\": \"684035\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k07_long_seed45_strict_w41.log\", \"submitted_at\": \"2026-05-28T05:18:00.559Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9879.3, \"gpu_hours\": 2.74}}, \"eval_pi05_random_k07_long_seed45_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"156371\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_long_seed45_strict_w38.log\", \"submitted_at\": \"2026-05-28T04:58:10.440Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9832.3, \"gpu_hours\": 2.73}}, \"eval_pi05_random_k095_long_seed45_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:0\"], \"pid\": \"155733\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k095_long_seed45_strict_w38.log\", \"submitted_at\": \"2026-05-28T04:57:51.765Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9833.6, \"gpu_hours\": 2.73}}, \"eval_pi05_l2norm_k05_long_seed45_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:0\"], \"pid\": \"981950\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k05_long_seed45_strict_cqa1.log\", \"submitted_at\": \"2026-05-28T02:21:15.841Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"pi0.5\", \"seed\": 45, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 15628.8, \"gpu_hours\": 4.34}}, \"eval_pi05_attn_k07_long_seed44_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 44 --gpu 0\", \"server\": \"westd-41074\", \"gpu\": \"cuda:1\", \"pid\": 374814, \"data_path\": \"libero_10\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"pi0.5\", \"seed\": 44, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (stale duplicate)\", \"log_path\": \"N/A (never deployed)\"}}, \"eval_pi05_random_k09_long_seed46_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:0\"], \"pid\": \"191022\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_long_seed46_strict_cqa1.log\", \"submitted_at\": \"2026-05-28T07:02:30.044Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"kill_reason\": \"重复部署，w38 版本领先 43min\", \"wall_clock_seconds\": 1065.1, \"gpu_hours\": 0.3}}, \"eval_pi05_attn_k09_long_seed44_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 44 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:2\"], \"pid\": \"695388\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k09_long_seed44_strict_w38.log\", \"submitted_at\": \"2026-05-27T20:29:38.138Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 35998.2, \"gpu_hours\": 10.0}}, \"eval_pi05_l2norm_k07_long_seed46_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:1\"], \"pid\": \"267270\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38.log\", \"submitted_at\": \"2026-05-28T06:38:27.889Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1432.5, \"gpu_hours\": 0.4}}, \"eval_openvla_random_k095_long_seed43_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 43 --gpu 0 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"700644\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_long_seed43_w41.log\", \"submitted_at\": \"2026-05-28T05:56:48.639Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2617.8, \"gpu_hours\": 0.73}}, \"eval_openvla_attn_k075_long_seed42_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"server\": \"westd-38929\", \"gpu\": 1, \"pid\": 266221, \"tmux_session\": \"ov_attn_k075_long\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_attn_k075_long_seed42_v3.log\", \"fix_note\": \"v3: added conda activation (v2 failed with 'python: command not found'), removed invalid --gpu param\"}}, \"eval_pi05_random_k085_long_seed44_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 44 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:0\"], \"pid\": \"178679\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed44_strict_w41.log\", \"submitted_at\": \"2026-05-27T20:51:16.193Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 34731.3, \"gpu_hours\": 9.65}}, \"eval_pi05_l2norm_k095_long_seed45_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:1\"], \"pid\": \"106960\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_long_seed45_strict_w38.log\", \"submitted_at\": \"2026-05-28T03:59:26.117Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9075.4, \"gpu_hours\": 2.52}}, \"eval_openvla_attn_k075_goal_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-27271\", \"gpu_ids\": [0], \"pid\": 499267, \"data_path\": \"libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_attn_k075_goal_seed42.log\"}}, \"eval_openvla_attn_k075_long_seed42\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-41074\", \"gpu\": \"cuda:3\", \"command\": \"MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"pid\": 824210, \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_long_seed42.log\"}}, \"mvp_imm_v8b_twostage\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/imm_two_stage/\", \"checkpoint_source\": \"checkpoints/baseline_v5/ (mvp_baseline_v5 final checkpoint)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python train_twostage.py --config configs/imm_anchor_v8b_twostage.yaml'\", \"config_path\": \"configs/imm_anchor_v8b_twostage.yaml\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"eval_data\": \"N/A (training experiment, not eval)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.79, \"log_path\": \"~/runs/importance_margin_vla_compress/mvp_imm_v8b_twostage.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32 + ACIS two-stage (stage1: ACIS-only lambda=1.0, stage2: LoRA+ACIS lambda=0.5)\", \"pid\": \"136367\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-16T04:18:10.534Z\", \"submitted_via\": \"submit_training_job\", \"tmux_session\": \"v8b_twostage\", \"wall_clock_seconds\": 10051.6}, \"status\": \"DONE\"}, \"train_smart_compress_m32_official\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/checkpoint.pt\", \"checkpoint_source\": \"/root/checkpoints/smart_compress_m32_official/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_official.yaml --wandb_run smart_compress_m32_official --seed 42 --gpu 0\", \"data_count\": \"full LIBERO dataset\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m32_official.log\", \"model_name\": \"smart_compress_m32\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\"}, \"eval_openvla_random_k075_goal_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-38929\", \"gpu_id\": 3, \"data_path\": \"libero_goal\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k075_goal_seed42.log\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}}, \"eval_pi05_random_k07_long_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 732826, \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log\", \"checkpoint_source\": \"pi0.5-base\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"eval_openvla_random_k095_object_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\", \"server\": \"westd-41074\", \"gpu_id\": 2, \"data_path\": \"libero_object\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"seed\": 42, \"log_path\": \"N/A\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\"}}, \"eval_pi05_l2norm_k085_long_seed42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_long_seed43_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"pid\": \"315686\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k095_long_seed43_strict_w38.log\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"eval_pi05_l2norm_k09_long_seed43_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": \"386864\", \"data_path\": \"libero_10\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.90_libero_10_seed43.json\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k09_long_seed43_strict_cqa1.log\", \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}}, \"eval_pi05_random_k07_long_seed44_strict_w27\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.70_libero_10_seed44.json\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_long_seed44_strict_w27.log\"}}, \"eval_pi05_attn_k095_long_seed45_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_attention_k0.95_libero_10_seed45.json\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k095_long_seed45_strict_cqa1.log\"}}, \"eval_openvla_random_k095_goal_seed42_v3\": {\"status\": \"PREPARING\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-goal --unnorm_key libero_goal\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:2\"], \"pid\": \"260085\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_goal_seed42_v3.log\", \"submitted_at\": \"2026-05-27T07:28:01.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_pi05_random_k05_long_seed45_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"570796\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed45_strict_w41.log\", \"submitted_at\": \"2026-05-28T02:30:37.265Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"pi0.5\", \"seed\": 45, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 11515.3, \"gpu_hours\": 3.2}}}, \"count\": 50, \"total\": 996, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4643}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "be673ae9-3689-4be2-8f51-2adaea130e5f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_pi05_l2norm_k05_long_seed47_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 47 --gpu 0\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 589899, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k05_long_seed47_w38.log\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 47, \\\"data_path\\\": \\\"libero_long\\\", \\\"data_count\\\": 500}}, \\\"eval_pi05_random_k085_long_seed47_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 47 --gpu 0\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 589824, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed47_w38.log\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 47, \\\"data_path\\\": \\\"libero_long\\\", \\\"data_count\\\": 500}}, \\\"eval_pi05_attn_k05_long_seed47_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 47 --gpu 0\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 590036, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_attn_k05_long_seed47_w38.log\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 47, \\\"data_path\\\": \\\"libero_long\\\", \\\"data_count\\\": 500}}, \\\"eval_pi05_l2norm_k07_long_seed46_strict_w41\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"923767\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k07_long_seed46_strict_w41.log\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 46, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"note\\\": \\\"Config confirmed correct: --keep_ratio 0.7. The k0.75 seed46 file is from a separate earlier experiment.\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}}, \\\"eval_openvla_l2norm_k095_long_seed43_w27\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 43 --gpu 0 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\\\\\"\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"545112\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed43_w27.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T05:57:09.091Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 21742.3, \\\"gpu_hours\\\": 6.04}}, \\\"eval_pi05_random_k05_long_seed46_strict_w41\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 899098, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed46_strict_w41.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T08:54:56.681Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 46, \\\"data_path\\\": \\\"libero_long\\\", \\\"data_count\\\": 500, \\\"wall_clock_seconds\\\": 10436.4, \\\"gpu_hours\\\": 2.9}}, \\\"eval_pi05_random_k095_long_seed46_strict_w41\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 46\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"898746\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k095_long_seed46_strict_w41.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T08:54:49.370Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 46, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/pi05_libero_finetuned\\\", \\\"wall_clock_seconds\\\": 9921.1, \\\"gpu_hours\\\": 2.76}}, \\\"eval_pi05_attn_k095_long_seed46_strict_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 457257, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_attn_k095_long_seed46_strict_w38.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T08:55:07.572Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 46, \\\"data_path\\\": \\\"libero_long\\\", \\\"data_count\\\": 500, \\\"wall_clock_seconds\\\": 8550.9, \\\"gpu_hours\\\": 2.38}}, \\\"eval_pi05_l2norm_k05_long_seed46_strict\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"168016\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k05_long_seed46_strict.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T06:33:19.594Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 46, \\\"wall_clock_seconds\\\": 16984.9, \\\"gpu_hours\\\": 4.72}}, \\\"eval_openvla_random_k095_goal_seed42_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_goal --num_episodes 50 --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-goal --unnorm_key libero_goal\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"147681\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_goal_seed42_v4.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T05:47:11.255Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 19678.8, \\\"gpu_hours\\\": 5.47}}, \\\"eval_pi05_attn_k07_long_seed46_strict_cqa1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"163384\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_attn_k07_long_seed46_strict_cqa1.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T06:26:19.770Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"pi05_libero_finetuned\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"wall_clock_seconds\\\": 16528.8, \\\"gpu_hours\\\": 4.59}}, \\\"eval_pi05_l2norm_k095_long_seed46_strict_w27\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 46\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"616102\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_long_seed46_strict_w27.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T08:54:39.968Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 46, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"wall_clock_seconds\\\": 7600.6, \\\"gpu_hours\\\": 2.11}}, \\\"eval_pi05_attn_k09_long_seed46_strict_cqa1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"163026\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_attn_k09_long_seed46_strict_cqa1.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T06:25:49.031Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"pi05_libero_finetuned\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"checkpoint_path\\\": \\\"N/A (eval)\\\", \\\"wall_clock_seconds\\\": 16321.7, \\\"gpu_hours\\\": 4.53}}, \\\"eval_pi05_l2norm_k085_long_seed46_strict_w41\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"859388\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k085_long_seed46_strict_w41.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T08:12:47.837Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"pi05_libero_finetuned\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"checkpoint_path\\\": \\\"N/A (eval)\\\", \\\"wall_clock_seconds\\\": 9849.9, \\\"gpu_hours\\\": 2.74}}, \\\"eval_pi05_attn_k075_long_seed46_strict_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"363743\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed46_strict_w38.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T07:47:39.761Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"pi05_libero_finetuned\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"wall_clock_seconds\\\": 10653.9, \\\"gpu_hours\\\": 2.96}}, \\\"eval_pi05_random_k075_long_seed46_strict_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"363188\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed46_strict_w38.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T07:47:27.897Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"pi05_libero_finetuned\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"wall_clock_seconds\\\": 9567.8, \\\"gpu_hours\\\": 2.66}}, \\\"eval_pi05_random_k09_long_seed46_strict_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_long_seed46_strict_w38.log\\\"}}, \\\"eval_pi05_attn_k05_long_seed46_strict\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"261876\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_attn_k05_long_seed46_strict.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T06:34:24.685Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 46, \\\"wall_clock_seconds\\\": 11665.4, \\\"gpu_hours\\\": 3.24}}, \\\"eval_pi05_random_k07_long_seed46_strict_w41\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"744875\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_long_seed46_strict_w41.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T06:37:42.521Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.70_libero_10_seed46.json\\\", \\\"wall_clock_seconds\\\": 9428.4, \\\"gpu_hours\\\": 2.62}}, \\\"eval_pi05_attn_k085_long_seed46_strict_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"218239\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_attn_k085_long_seed46_strict_w38.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T05:54:16.144Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 10658.5, \\\"gpu_hours\\\": 2.96, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}}, \\\"eval_pi05_random_k085_long_seed46_strict_w41\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"697206\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed46_strict_w41.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T05:53:31.834Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 10694.6, \\\"gpu_hours\\\": 2.97, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}}, \\\"eval_pi05_l2norm_k09_long_seed46_strict_w27\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"549654\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k09_long_seed46_strict_w27.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T06:25:16.159Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"pi05_libero_finetuned\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"wall_clock_seconds\\\": 8764.6, \\\"gpu_hours\\\": 2.43}}, \\\"eval_pi05_l2norm_k075_long_seed46_strict_w41\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"697663\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k075_long_seed46_strict_w41.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T05:53:56.633Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 8956.0, \\\"gpu_hours\\\": 2.49}}, \\\"eval_pi05_l2norm_k07_long_seed46_strict_w38_v2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval_pi05_attn_k07_long_seed45_strict_w41\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"684035\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_attn_k07_long_seed45_strict_w41.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T05:18:00.559Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 9879.3, \\\"gpu_hours\\\": 2.74}}, \\\"eval_pi05_random_k07_long_seed45_strict_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"156371\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_long_seed45_strict_w38.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:58:10.440Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 9832.3, \\\"gpu_hours\\\": 2.73}}, \\\"eval_pi05_random_k095_long_seed45_strict_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"155733\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k095_long_seed45_strict_w38.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:57:51.765Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 9833.6, \\\"gpu_hours\\\": 2.73}}, \\\"eval_pi05_l2norm_k05_long_seed45_strict_cqa1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"981950\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k05_long_seed45_strict_cqa1.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T02:21:15.841Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": \\\"10 tasks x 50 episodes\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"pi0.5 pretrained\\\", \\\"eval_data\\\": \\\"libero_10 (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"wall_clock_seconds\\\": 15628.8, \\\"gpu_hours\\\": 4.34}}, \\\"eval_pi05_attn_k07_long_seed44_strict_cqa1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 44 --gpu 0\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 374814, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": \\\"10 tasks x 50 episodes\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"pi0.5 pretrained\\\", \\\"eval_data\\\": \\\"libero_10 (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (stale duplicate)\\\", \\\"log_path\\\": \\\"N/A (never deployed)\\\"}}, \\\"eval_pi05_random_k09_long_seed46_strict_cqa1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"191022\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_long_seed46_strict_cqa1.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T07:02:30.044Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"kill_reason\\\": \\\"重复部署，w38 版本领先 43min\\\", \\\"wall_clock_seconds\\\": 1065.1, \\\"gpu_hours\\\": 0.3}}, \\\"eval_pi05_attn_k09_long_seed44_strict_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 44 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"695388\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_attn_k09_long_seed44_strict_w38.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T20:29:38.138Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 35998.2, \\\"gpu_hours\\\": 10.0}}, \\\"eval_pi05_l2norm_k07_long_seed46_strict_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"267270\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T06:38:27.889Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 1432.5, \\\"gpu_hours\\\": 0.4}}, \\\"eval_openvla_random_k095_long_seed43_w41\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 43 --gpu 0 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\\\\\"\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"700644\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_long_seed43_w41.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T05:56:48.639Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 2617.8, \\\"gpu_hours\\\": 0.73}}, \\\"eval_openvla_attn_k075_long_seed42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": 1, \\\"pid\\\": 266221, \\\"tmux_session\\\": \\\"ov_attn_k075_long\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_attn_k075_long_seed42_v3.log\\\", \\\"fix_note\\\": \\\"v3: added conda activation (v2 failed with 'python: command not found'), removed invalid --gpu param\\\"}}, \\\"eval_pi05_random_k085_long_seed44_strict_w41\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 44 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"178679\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed44_strict_w41.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T20:51:16.193Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 34731.3, \\\"gpu_hours\\\": 9.65}}, \\\"eval_pi05_l2norm_k095_long_seed45_strict_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"106960\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_long_seed45_strict_w38.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T03:59:26.117Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 9075.4, \\\"gpu_hours\\\": 2.52}}, \\\"eval_openvla_attn_k075_goal_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 499267, \\\"data_path\\\": \\\"libero_goal\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-goal\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-7b-finetuned-libero-goal\\\", \\\"eval_data\\\": \\\"libero_goal\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_attn_k075_goal_seed42.log\\\"}}, \\\"eval_openvla_attn_k075_long_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"command\\\": \\\"MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\", \\\"pid\\\": 824210, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-10\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-7b-finetuned-libero-10\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_long_seed42.log\\\"}}, \\\"mvp_imm_v8b_twostage\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"checkpoint_path\\\": \\\"checkpoints/imm_two_stage/\\\", \\\"checkpoint_source\\\": \\\"checkpoints/baseline_v5/ (mvp_baseline_v5 final checkpoint)\\\", \\\"command\\\": \\\"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python train_twostage.py --config configs/imm_anchor_v8b_twostage.yaml'\\\", \\\"config_path\\\": \\\"configs/imm_anchor_v8b_twostage.yaml\\\", \\\"data_count\\\": 20000, \\\"data_path\\\": \\\"lerobot/aloha_sim_insertion_scripted_image\\\", \\\"eval_data\\\": \\\"N/A (training experiment, not eval)\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"gpu_hours\\\": 2.79, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/mvp_imm_v8b_twostage.log\\\", \\\"model_name\\\": \\\"lerobot/smolvla_base + LoRA r=32 + ACIS two-stage (stage1: ACIS-only lambda=1.0, stage2: LoRA+ACIS lambda=0.5)\\\", \\\"pid\\\": \\\"136367\\\", \\\"seed\\\": 42, \\\"server\\\": \\\"westd-27271\\\", \\\"submitted_at\\\": \\\"2026-05-16T04:18:10.534Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"tmux_session\\\": \\\"v8b_twostage\\\", \\\"wall_clock_seconds\\\": 10051.6}, \\\"status\\\": \\\"DONE\\\"}, \\\"train_smart_compress_m32_official\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/checkpoint.pt\\\", \\\"checkpoint_source\\\": \\\"/root/checkpoints/smart_compress_m32_official/checkpoint.pt\\\", \\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_official.yaml --wandb_run smart_compress_m32_official --seed 42 --gpu 0\\\", \\\"data_count\\\": \\\"full LIBERO dataset\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m32_official.log\\\", \\\"model_name\\\": \\\"smart_compress_m32\\\", \\\"seed\\\": 42, \\\"server\\\": \\\"cqa1-33015\\\"}, \\\"status\\\": \\\"DONE\\\"}, \\\"eval_openvla_random_k075_goal_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu_id\\\": 3, \\\"data_path\\\": \\\"libero_goal\\\", \\\"data_count\\\": \\\"10 tasks x 50 episodes\\\", \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-goal\\\", \\\"seed\\\": 42, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_random_k075_goal_seed42.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/openvla-7b-finetuned-libero-goal\\\", \\\"eval_data\\\": \\\"libero_goal\\\"}}, \\\"eval_pi05_random_k07_long_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 732826, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log\\\", \\\"checkpoint_source\\\": \\\"pi0.5-base\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}}, \\\"eval_openvla_random_k095_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu_id\\\": 2, \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": \\\"10 tasks x 50 episodes\\\", \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-object\\\", \\\"seed\\\": 42, \\\"log_path\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"eval_data\\\": \\\"libero_object\\\"}}, \\\"eval_pi05_l2norm_k085_long_seed42\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\", \\\"data_count\\\": 500, \\\"data_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"server\\\": \\\"westd-38929\\\"}, \\\"status\\\": \\\"DONE\\\"}, \\\"eval_pi05_l2norm_k095_long_seed43_strict_w38\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": \\\"315686\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k095_long_seed43_strict_w38.log\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"pi0.5 pretrained\\\", \\\"eval_data\\\": \\\"libero_10 (Long)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}}, \\\"eval_pi05_l2norm_k09_long_seed43_strict_cqa1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": \\\"386864\\\", \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": \\\"10 tasks x 50 episodes\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 43, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.90_libero_10_seed43.json\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k09_long_seed43_strict_cqa1.log\\\", \\\"checkpoint_source\\\": \\\"pi0.5 pretrained\\\", \\\"eval_data\\\": \\\"libero_10 (Long)\\\"}}, \\\"eval_pi05_random_k07_long_seed44_strict_w27\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.70_libero_10_seed44.json\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_long_seed44_strict_w27.log\\\"}}, \\\"eval_pi05_attn_k095_long_seed45_strict_cqa1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_attention_k0.95_libero_10_seed45.json\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_attn_k095_long_seed45_strict_cqa1.log\\\"}}, \\\"eval_openvla_random_k095_goal_seed42_v3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-goal --unnorm_key libero_goal\\\\\\\"\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"260085\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_goal_seed42_v3.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T07:28:01.091Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval_pi05_random_k05_long_seed45_strict_w41\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"570796\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed45_strict_w41.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T02:30:37.265Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": \\\"10 tasks x 50 episodes\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"pi0.5 pretrained\\\", \\\"eval_data\\\": \\\"libero_10 (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"wall_clock_seconds\\\": 11515.3, \\\"gpu_hours\\\": 3.2}}}, \\\"count\\\": 50, \\\"total\\\": 996, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.4643}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_pi05_l2norm_k05_long_seed47_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 47 --gpu 0\", \"server\": \"westd-38929\", \"gpu\": \"cuda:1\", \"pid\": 589899, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k05_long_seed47_w38.log\", \"model_name\": \"pi0.5\", \"seed\": 47, \"data_path\": \"libero_long\", \"data_count\": 500}}, \"eval_pi05_random_k085_long_seed47_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 47 --gpu 0\", \"server\": \"westd-38929\", \"gpu\": \"cuda:0\", \"pid\": 589824, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed47_w38.log\", \"model_name\": \"pi0.5\", \"seed\": 47, \"data_path\": \"libero_long\", \"data_count\": 500}}, \"eval_pi05_attn_k05_long_seed47_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 47 --gpu 0\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"pid\": 590036, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k05_long_seed47_w38.log\", \"model_name\": \"pi0.5\", \"seed\": 47, \"data_path\": \"libero_long\", \"data_count\": 500}}, \"eval_pi05_l2norm_k07_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"923767\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k07_long_seed46_strict_w41.log\", \"model_name\": \"pi0.5\", \"seed\": 46, \"data_path\": \"libero_10\", \"data_count\": 500, \"note\": \"Config confirmed correct: --keep_ratio 0.7. The k0.75 seed46 file is from a separate earlier experiment.\", \"checkpoint_path\": \"N/A\"}}, \"eval_openvla_l2norm_k095_long_seed43_w27\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 43 --gpu 0 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"545112\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed43_w27.log\", \"submitted_at\": \"2026-05-28T05:57:09.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21742.3, \"gpu_hours\": 6.04}}, \"eval_pi05_random_k05_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": \"cuda:2\", \"pid\": 899098, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed46_strict_w41.log\", \"submitted_at\": \"2026-05-28T08:54:56.681Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi0.5\", \"seed\": 46, \"data_path\": \"libero_long\", \"data_count\": 500, \"wall_clock_seconds\": 10436.4, \"gpu_hours\": 2.9}}, \"eval_pi05_random_k095_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 46\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:0\"], \"pid\": \"898746\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k095_long_seed46_strict_w41.log\", \"submitted_at\": \"2026-05-28T08:54:49.370Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi0.5\", \"seed\": 46, \"data_path\": \"libero_10\", \"data_count\": 500, \"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"wall_clock_seconds\": 9921.1, \"gpu_hours\": 2.76}}, \"eval_pi05_attn_k095_long_seed46_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": \"cuda:3\", \"pid\": 457257, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k095_long_seed46_strict_w38.log\", \"submitted_at\": \"2026-05-28T08:55:07.572Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi0.5\", \"seed\": 46, \"data_path\": \"libero_long\", \"data_count\": 500, \"wall_clock_seconds\": 8550.9, \"gpu_hours\": 2.38}}, \"eval_pi05_l2norm_k05_long_seed46_strict\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:0\"], \"pid\": \"168016\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k05_long_seed46_strict.log\", \"submitted_at\": \"2026-05-28T06:33:19.594Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"wall_clock_seconds\": 16984.9, \"gpu_hours\": 4.72}}, \"eval_openvla_random_k095_goal_seed42_v4\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_goal --num_episodes 50 --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-goal --unnorm_key libero_goal\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:2\"], \"pid\": \"147681\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_goal_seed42_v4.log\", \"submitted_at\": \"2026-05-28T05:47:11.255Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 19678.8, \"gpu_hours\": 5.47}}, \"eval_pi05_attn_k07_long_seed46_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:3\"], \"pid\": \"163384\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k07_long_seed46_strict_cqa1.log\", \"submitted_at\": \"2026-05-28T06:26:19.770Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 16528.8, \"gpu_hours\": 4.59}}, \"eval_pi05_l2norm_k095_long_seed46_strict_w27\": {\"status\": \"DONE\", \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 46\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"616102\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_long_seed46_strict_w27.log\", \"submitted_at\": \"2026-05-28T08:54:39.968Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi0.5\", \"seed\": 46, \"data_path\": \"libero_10\", \"data_count\": 500, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 7600.6, \"gpu_hours\": 2.11}}, \"eval_pi05_attn_k09_long_seed46_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"163026\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k09_long_seed46_strict_cqa1.log\", \"submitted_at\": \"2026-05-28T06:25:49.031Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval)\", \"wall_clock_seconds\": 16321.7, \"gpu_hours\": 4.53}}, \"eval_pi05_l2norm_k085_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:3\"], \"pid\": \"859388\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k085_long_seed46_strict_w41.log\", \"submitted_at\": \"2026-05-28T08:12:47.837Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval)\", \"wall_clock_seconds\": 9849.9, \"gpu_hours\": 2.74}}, \"eval_pi05_attn_k075_long_seed46_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"363743\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed46_strict_w38.log\", \"submitted_at\": \"2026-05-28T07:47:39.761Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"wall_clock_seconds\": 10653.9, \"gpu_hours\": 2.96}}, \"eval_pi05_random_k075_long_seed46_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:0\"], \"pid\": \"363188\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k075_long_seed46_strict_w38.log\", \"submitted_at\": \"2026-05-28T07:47:27.897Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"wall_clock_seconds\": 9567.8, \"gpu_hours\": 2.66}}, \"eval_pi05_random_k09_long_seed46_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_long_seed46_strict_w38.log\"}}, \"eval_pi05_attn_k05_long_seed46_strict\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:1\"], \"pid\": \"261876\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k05_long_seed46_strict.log\", \"submitted_at\": \"2026-05-28T06:34:24.685Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"wall_clock_seconds\": 11665.4, \"gpu_hours\": 3.24}}, \"eval_pi05_random_k07_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"744875\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_long_seed46_strict_w41.log\", \"submitted_at\": \"2026-05-28T06:37:42.521Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.70_libero_10_seed46.json\", \"wall_clock_seconds\": 9428.4, \"gpu_hours\": 2.62}}, \"eval_pi05_attn_k085_long_seed46_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:3\"], \"pid\": \"218239\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k085_long_seed46_strict_w38.log\", \"submitted_at\": \"2026-05-28T05:54:16.144Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10658.5, \"gpu_hours\": 2.96, \"checkpoint_path\": \"N/A (eval only)\"}}, \"eval_pi05_random_k085_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:0\"], \"pid\": \"697206\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed46_strict_w41.log\", \"submitted_at\": \"2026-05-28T05:53:31.834Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10694.6, \"gpu_hours\": 2.97, \"checkpoint_path\": \"N/A (eval only)\"}}, \"eval_pi05_l2norm_k09_long_seed46_strict_w27\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"549654\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k09_long_seed46_strict_w27.log\", \"submitted_at\": \"2026-05-28T06:25:16.159Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"pi05\", \"seed\": 46, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"wall_clock_seconds\": 8764.6, \"gpu_hours\": 2.43}}, \"eval_pi05_l2norm_k075_long_seed46_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:2\"], \"pid\": \"697663\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k075_long_seed46_strict_w41.log\", \"submitted_at\": \"2026-05-28T05:53:56.633Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8956.0, \"gpu_hours\": 2.49}}, \"eval_pi05_l2norm_k07_long_seed46_strict_w38_v2\": {\"status\": \"PREPARING\"}, \"eval_pi05_attn_k07_long_seed45_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:3\"], \"pid\": \"684035\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k07_long_seed45_strict_w41.log\", \"submitted_at\": \"2026-05-28T05:18:00.559Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9879.3, \"gpu_hours\": 2.74}}, \"eval_pi05_random_k07_long_seed45_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"156371\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_long_seed45_strict_w38.log\", \"submitted_at\": \"2026-05-28T04:58:10.440Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9832.3, \"gpu_hours\": 2.73}}, \"eval_pi05_random_k095_long_seed45_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:0\"], \"pid\": \"155733\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k095_long_seed45_strict_w38.log\", \"submitted_at\": \"2026-05-28T04:57:51.765Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9833.6, \"gpu_hours\": 2.73}}, \"eval_pi05_l2norm_k05_long_seed45_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:0\"], \"pid\": \"981950\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k05_long_seed45_strict_cqa1.log\", \"submitted_at\": \"2026-05-28T02:21:15.841Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"pi0.5\", \"seed\": 45, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 15628.8, \"gpu_hours\": 4.34}}, \"eval_pi05_attn_k07_long_seed44_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 44 --gpu 0\", \"server\": \"westd-41074\", \"gpu\": \"cuda:1\", \"pid\": 374814, \"data_path\": \"libero_10\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"pi0.5\", \"seed\": 44, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (stale duplicate)\", \"log_path\": \"N/A (never deployed)\"}}, \"eval_pi05_random_k09_long_seed46_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:0\"], \"pid\": \"191022\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_long_seed46_strict_cqa1.log\", \"submitted_at\": \"2026-05-28T07:02:30.044Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"kill_reason\": \"重复部署，w38 版本领先 43min\", \"wall_clock_seconds\": 1065.1, \"gpu_hours\": 0.3}}, \"eval_pi05_attn_k09_long_seed44_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 44 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:2\"], \"pid\": \"695388\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k09_long_seed44_strict_w38.log\", \"submitted_at\": \"2026-05-27T20:29:38.138Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 35998.2, \"gpu_hours\": 10.0}}, \"eval_pi05_l2norm_k07_long_seed46_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:1\"], \"pid\": \"267270\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38.log\", \"submitted_at\": \"2026-05-28T06:38:27.889Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1432.5, \"gpu_hours\": 0.4}}, \"eval_openvla_random_k095_long_seed43_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 43 --gpu 0 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"700644\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_long_seed43_w41.log\", \"submitted_at\": \"2026-05-28T05:56:48.639Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2617.8, \"gpu_hours\": 0.73}}, \"eval_openvla_attn_k075_long_seed42_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"server\": \"westd-38929\", \"gpu\": 1, \"pid\": 266221, \"tmux_session\": \"ov_attn_k075_long\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_attn_k075_long_seed42_v3.log\", \"fix_note\": \"v3: added conda activation (v2 failed with 'python: command not found'), removed invalid --gpu param\"}}, \"eval_pi05_random_k085_long_seed44_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 44 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:0\"], \"pid\": \"178679\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed44_strict_w41.log\", \"submitted_at\": \"2026-05-27T20:51:16.193Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 34731.3, \"gpu_hours\": 9.65}}, \"eval_pi05_l2norm_k095_long_seed45_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:1\"], \"pid\": \"106960\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_long_seed45_strict_w38.log\", \"submitted_at\": \"2026-05-28T03:59:26.117Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9075.4, \"gpu_hours\": 2.52}}, \"eval_openvla_attn_k075_goal_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-27271\", \"gpu_ids\": [0], \"pid\": 499267, \"data_path\": \"libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_attn_k075_goal_seed42.log\"}}, \"eval_openvla_attn_k075_long_seed42\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-41074\", \"gpu\": \"cuda:3\", \"command\": \"MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"pid\": 824210, \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_long_seed42.log\"}}, \"mvp_imm_v8b_twostage\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/imm_two_stage/\", \"checkpoint_source\": \"checkpoints/baseline_v5/ (mvp_baseline_v5 final checkpoint)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python train_twostage.py --config configs/imm_anchor_v8b_twostage.yaml'\", \"config_path\": \"configs/imm_anchor_v8b_twostage.yaml\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"eval_data\": \"N/A (training experiment, not eval)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.79, \"log_path\": \"~/runs/importance_margin_vla_compress/mvp_imm_v8b_twostage.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32 + ACIS two-stage (stage1: ACIS-only lambda=1.0, stage2: LoRA+ACIS lambda=0.5)\", \"pid\": \"136367\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-16T04:18:10.534Z\", \"submitted_via\": \"submit_training_job\", \"tmux_session\": \"v8b_twostage\", \"wall_clock_seconds\": 10051.6}, \"status\": \"DONE\"}, \"train_smart_compress_m32_official\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/checkpoint.pt\", \"checkpoint_source\": \"/root/checkpoints/smart_compress_m32_official/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_official.yaml --wandb_run smart_compress_m32_official --seed 42 --gpu 0\", \"data_count\": \"full LIBERO dataset\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m32_official.log\", \"model_name\": \"smart_compress_m32\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\"}, \"eval_openvla_random_k075_goal_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-38929\", \"gpu_id\": 3, \"data_path\": \"libero_goal\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k075_goal_seed42.log\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}}, \"eval_pi05_random_k07_long_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 732826, \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log\", \"checkpoint_source\": \"pi0.5-base\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"eval_openvla_random_k095_object_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\", \"server\": \"westd-41074\", \"gpu_id\": 2, \"data_path\": \"libero_object\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"seed\": 42, \"log_path\": \"N/A\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\"}}, \"eval_pi05_l2norm_k085_long_seed42\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_long_seed43_strict_w38\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"pid\": \"315686\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k095_long_seed43_strict_w38.log\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": 500, \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"eval_pi05_l2norm_k09_long_seed43_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": \"386864\", \"data_path\": \"libero_10\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"pi0.5\", \"seed\": 43, \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.90_libero_10_seed43.json\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k09_long_seed43_strict_cqa1.log\", \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (Long)\"}}, \"eval_pi05_random_k07_long_seed44_strict_w27\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.70_libero_10_seed44.json\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_long_seed44_strict_w27.log\"}}, \"eval_pi05_attn_k095_long_seed45_strict_cqa1\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_attention_k0.95_libero_10_seed45.json\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_attn_k095_long_seed45_strict_cqa1.log\"}}, \"eval_openvla_random_k095_goal_seed42_v3\": {\"status\": \"PREPARING\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-goal --unnorm_key libero_goal\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:2\"], \"pid\": \"260085\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_goal_seed42_v3.log\", \"submitted_at\": \"2026-05-27T07:28:01.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_pi05_random_k05_long_seed45_strict_w41\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 45 --gpu 0\\\"\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": \"570796\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_long_seed45_strict_w41.log\", \"submitted_at\": \"2026-05-28T02:30:37.265Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"pi0.5\", \"seed\": 45, \"checkpoint_source\": \"pi0.5 pretrained\", \"eval_data\": \"libero_10 (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 11515.3, \"gpu_hours\": 3.2}}}, \"count\": 50, \"total\": 996, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4643}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

````text
Found the v1 experiment: `eval_pi05_l2norm_k07_long_seed46_strict_w38` with command:
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0"


```

The v1 run hit an out-of-memory error on GPU 1 after about 24 minutes. Since GPU 0 is now available on w38, I'm switching to that device for v2, which is already queued up and ready to go.

Constructing the command...

GPU 0 appears to be the only GPU on this machine based on the nvidia-smi output showing just one line, though I should verify if there are actually multiple GPUs since other experiments suggest there might be more.

```
0, 0 MiB, 97887 MiB, 0 %
```

That's roughly 96GB of memory, which could indicate an H100, but the discrepancy with previous experiments using cuda:0 through cuda:3 is puzzling. Either the machine configuration has changed, or the query format isn't capturing all available GPUs for some reason.

Looking at the compute apps output, there are no processes running, so GPU 0 is completely free. If w38 only has one GPU now, setting CUDA_VISIBLE_DEVICES=0 should work fine.

Now I need to verify the eval script exists. The user's template references `eval_pi05_pruning_libero_cqa1.py`, but looking back at the v1 experiment, the actual script used was `eval_pi05_pruning_libero.py` without the `_cqa1` suffix. I should use the v1 naming convention to be consistent.

I also notice the argument names differ between the user's template and v1's actual command—the template uses `--mode l2norm_prune --k_ratio 0.7` while v1 uses `--prune_mode l2norm --keep_ratio 0.7`. Since v1's command is what actually worked, I'll stick with those argument names instead.

GPU 0 has 97887 MiB available, which is more than enough for pi0.5, so I'm ready to submit the job.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "f4b9db25-6b9d-484f-b191-be6647c746e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JpyeRKHbqQtzj122RaC36",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16800,
      "cache_read_input_tokens": 27616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16800
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

_source line 22_

找到 v1 实验 `eval_pi05_l2norm_k07_long_seed46_strict_w38`，它用了 cuda:1（OOM 失败，仅运行 24 分钟）。w38 当前只有 GPU 0（97887 MiB H100），完全空闲无进程。提交 v2 到 cuda:0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "e69bef18-d866-4713-a24b-c47239eebdc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JpyeRKHbqQtzj122RaC36",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16800,
      "cache_read_input_tokens": 27616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16800
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

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job · `toolu_01DWoDJS43hf4UseFykBBvip`</summary>

```json
{
  "server": "westd-38929",
  "gpu_ids": [
    "cuda:0"
  ],
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\"",
  "exp_id": "eval_pi05_l2norm_k07_long_seed46_strict_w38_v2",
  "timeout_hours": 6,
  "account": "root",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "bc41f034-45ed-40d8-aeed-30c1c6a27083",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JpyeRKHbqQtzj122RaC36",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16800,
      "cache_read_input_tokens": 27616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16800
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

_source line 24 · 2026-05-28T16:19:39.133Z_

<details><summary>↩ Tool result · `toolu_01DWoDJS43hf4UseFykBBvip`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"pid\": \"16710\", \"log_file\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log\", \"gpu_ids\": [\"cuda:0\"], \"server\": \"westd-38929\", \"account\": \"root\", \"cuda_visible_devices\": \"0\", \"backend\": \"tmux\", \"tmux_session\": \"eval_pi05_l2norm_k07_long_seed46_strict_w38_v2\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.22}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "7bf1b58c-7243-4074-a1a9-21ccd3f49e3c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"pid\\\": \\\"16710\\\", \\\"log_file\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log\\\", \\\"gpu_ids\\\": [\\\"cuda:0\\\"], \\\"server\\\": \\\"westd-38929\\\", \\\"account\\\": \\\"root\\\", \\\"cuda_visible_devices\\\": \\\"0\\\", \\\"backend\\\": \\\"tmux\\\", \\\"tmux_session\\\": \\\"eval_pi05_l2norm_k07_long_seed46_strict_w38_v2\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 7.22}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"pid\": \"16710\", \"log_file\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log\", \"gpu_ids\": [\"cuda:0\"], \"server\": \"westd-38929\", \"account\": \"root\", \"cuda_visible_devices\": \"0\", \"backend\": \"tmux\", \"tmux_session\": \"eval_pi05_l2norm_k07_long_seed46_strict_w38_v2\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.22}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Job submitted successfully. Now update registry to RUNNING with spec.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "995d1c6f-6c87-4e5d-9751-69c876df26fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173bMBrjB59SThHzLZcYHbk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1881,
      "cache_read_input_tokens": 44416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1881
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

_source line 26_

已提交，PID=16710。更新 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "df7a1ffa-1a2e-4561-a77a-be345205972e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173bMBrjB59SThHzLZcYHbk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1881,
      "cache_read_input_tokens": 44416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1881
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

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01C9z7UzUkzKAePVYCtLXs6g`</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k07_long_seed46_strict_w38_v2",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\"",
    "server": "westd-38929",
    "gpu": [
      "cuda:0"
    ],
    "pid": "16710",
    "log_path": "~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log",
    "model_name": "pi0.5",
    "seed": 46,
    "data_path": "libero_long",
    "data_count": 500,
    "note": "v2: v1 OOM on cuda:1 (shared GPU). This run uses dedicated GPU 0 (H100 97GB)."
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
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "d8cdee74-3168-4aca-bbc3-2f8cf306d18d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173bMBrjB59SThHzLZcYHbk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1881,
      "cache_read_input_tokens": 44416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1881
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

_source line 28 · 2026-05-28T16:19:48.859Z_

<details><summary>↩ Tool result · `toolu_01C9z7UzUkzKAePVYCtLXs6g`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.3494}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "020f8f1a-8cd3-45df-a7a3-486d2e8f405d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.3494}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.3494}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01JbLCs3PgctwpeT5Rx2ZGVz`</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k07_long_seed46_strict_w38_v2",
  "field": "status",
  "value": "QUEUED",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "cd49aaea-c19f-4deb-ad7e-3bf434d7004a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WJuUyYF6ycfVpUrnAktiJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 587,
      "cache_read_input_tokens": 46297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 587
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

_source line 30 · 2026-05-28T16:20:00.250Z_

<details><summary>↩ Tool result · `toolu_01JbLCs3PgctwpeT5Rx2ZGVz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_l2norm_k07_long_seed46_strict_w38_v2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-28T07:46:24.306Z\", \"updated_at\": \"2026-05-28T16:19:54.482Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 Long strict seed46 — v1 被 GPU OOM kill (w38:cuda:1 三进程共享)。重试部署到独占 GPU。5th seed for crossover point, 4-seed mean=63.5±1.57pp\", \"parent\": \"eval_pi05_l2norm_k07_long_seed46_strict_w38\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:0\"], \"pid\": \"16710\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log\", \"submitted_at\": \"2026-05-28T16:19:35.184Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.0386}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "38d68fd3-7c0e-44ff-9dc5-66b5f46e29ba",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_pi05_l2norm_k07_long_seed46_strict_w38_v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T07:46:24.306Z\\\", \\\"updated_at\\\": \\\"2026-05-28T16:19:54.482Z\\\", \\\"hypothesis\\\": \\\"π0.5 L2norm k=0.7 Long strict seed46 — v1 被 GPU OOM kill (w38:cuda:1 三进程共享)。重试部署到独占 GPU。5th seed for crossover point, 4-seed mean=63.5±1.57pp\\\", \\\"parent\\\": \\\"eval_pi05_l2norm_k07_long_seed46_strict_w38\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"16710\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T16:19:35.184Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.0386}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_l2norm_k07_long_seed46_strict_w38_v2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-28T07:46:24.306Z\", \"updated_at\": \"2026-05-28T16:19:54.482Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 Long strict seed46 — v1 被 GPU OOM kill (w38:cuda:1 三进程共享)。重试部署到独占 GPU。5th seed for crossover point, 4-seed mean=63.5±1.57pp\", \"parent\": \"eval_pi05_l2norm_k07_long_seed46_strict_w38\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:0\"], \"pid\": \"16710\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log\", \"submitted_at\": \"2026-05-28T16:19:35.184Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.0386}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_017YGYKVKui5BYbq18neFiMN`</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k07_long_seed46_strict_w38_v2",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\"",
    "server": "westd-38929",
    "gpu": [
      "cuda:0"
    ],
    "pid": "16710",
    "log_path": "~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log",
    "model_name": "pi0.5",
    "seed": 46,
    "data_path": "libero_long",
    "data_count": 500,
    "note": "v2: v1 OOM on cuda:1 (shared GPU). This run uses dedicated GPU 0 (H100 97GB)."
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
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "6668a227-03d7-45aa-a31b-b155bde8b78c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLpoDQcodS4nTZ5MdQ3n2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 46884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 730
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

_source line 32 · 2026-05-28T16:20:08.306Z_

<details><summary>↩ Tool result · `toolu_017YGYKVKui5BYbq18neFiMN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Eval experiment requires additional spec fields: ['checkpoint_source', 'eval_data']. Eval spec must include: ['checkpoint_source', 'eval_data']\", \"metadata\": {\"elapsed_seconds\": 2.2846}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "710279bf-4465-4dfb-8c71-6941150293c8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Eval experiment requires additional spec fields: ['checkpoint_source', 'eval_data']. Eval spec must include: ['checkpoint_source', 'eval_data']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.2846}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Eval experiment requires additional spec fields: ['checkpoint_source', 'eval_data']. Eval spec must include: ['checkpoint_source', 'eval_data']\", \"metadata\": {\"elapsed_seconds\": 2.2846}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_014BAw3rUwiZjCaNEQ3bL4XD`</summary>

```json
{
  "exp_id": "eval_pi05_l2norm_k07_long_seed46_strict_w38_v2",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\"",
    "server": "westd-38929",
    "gpu": [
      "cuda:0"
    ],
    "pid": "16710",
    "log_path": "~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log",
    "model_name": "pi0.5",
    "seed": 46,
    "data_path": "libero_long",
    "data_count": 500,
    "checkpoint_source": "pi05_libero_finetuned",
    "eval_data": "libero_10",
    "checkpoint_path": "N/A (eval only)",
    "note": "v2: v1 OOM on cuda:1 (shared GPU). This run uses dedicated GPU 0 (H100 97GB)."
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
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "fcc1c14d-bea3-4b0c-8d39-8e57c6558cc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5RqWVazn9EfWYCfY9CFXk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 558,
      "cache_read_input_tokens": 47614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 558
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

_source line 34 · 2026-05-28T16:20:21.268Z_

<details><summary>↩ Tool result · `toolu_014BAw3rUwiZjCaNEQ3bL4XD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_l2norm_k07_long_seed46_strict_w38_v2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T07:46:24.306Z\", \"updated_at\": \"2026-05-28T16:20:16.463Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 Long strict seed46 — v1 被 GPU OOM kill (w38:cuda:1 三进程共享)。重试部署到独占 GPU。5th seed for crossover point, 4-seed mean=63.5±1.57pp\", \"parent\": \"eval_pi05_l2norm_k07_long_seed46_strict_w38\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:0\"], \"pid\": \"16710\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log\", \"submitted_at\": \"2026-05-28T16:19:35.184Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi0.5\", \"seed\": 46, \"data_path\": \"libero_long\", \"data_count\": 500, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval only)\", \"note\": \"v2: v1 OOM on cuda:1 (shared GPU). This run uses dedicated GPU 0 (H100 97GB).\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.0428}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "8f3da53c-67a5-4085-b424-bb8aca301491",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_pi05_l2norm_k07_long_seed46_strict_w38_v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T07:46:24.306Z\\\", \\\"updated_at\\\": \\\"2026-05-28T16:20:16.463Z\\\", \\\"hypothesis\\\": \\\"π0.5 L2norm k=0.7 Long strict seed46 — v1 被 GPU OOM kill (w38:cuda:1 三进程共享)。重试部署到独占 GPU。5th seed for crossover point, 4-seed mean=63.5±1.57pp\\\", \\\"parent\\\": \\\"eval_pi05_l2norm_k07_long_seed46_strict_w38\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"16710\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T16:19:35.184Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 46, \\\"data_path\\\": \\\"libero_long\\\", \\\"data_count\\\": 500, \\\"checkpoint_source\\\": \\\"pi05_libero_finetuned\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"note\\\": \\\"v2: v1 OOM on cuda:1 (shared GPU). This run uses dedicated GPU 0 (H100 97GB).\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 7.0428}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_l2norm_k07_long_seed46_strict_w38_v2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T07:46:24.306Z\", \"updated_at\": \"2026-05-28T16:20:16.463Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 Long strict seed46 — v1 被 GPU OOM kill (w38:cuda:1 三进程共享)。重试部署到独占 GPU。5th seed for crossover point, 4-seed mean=63.5±1.57pp\", \"parent\": \"eval_pi05_l2norm_k07_long_seed46_strict_w38\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:0\"], \"pid\": \"16710\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log\", \"submitted_at\": \"2026-05-28T16:19:35.184Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi0.5\", \"seed\": 46, \"data_path\": \"libero_long\", \"data_count\": 500, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval only)\", \"note\": \"v2: v1 OOM on cuda:1 (shared GPU). This run uses dedicated GPU 0 (H100 97GB).\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.0428}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

已部署完成：

- **实验**: `eval_pi05_l2norm_k07_long_seed46_strict_w38_v2`
- **服务器**: westd-38929, GPU 0 (H100 97GB, 独占)
- **PID**: 16710
- **状态**: RUNNING
- **日志**: `~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log`
- **预估时长**: ~3h（参考同类实验）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "uuid": "591dcd37-d738-4562-b53b-9562aae91b8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UbCa9ZDmmC26DwPLZ1Ze4T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1219,
      "cache_read_input_tokens": 48172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1219
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

_source line 36_

已部署完成：

- **实验**: `eval_pi05_l2norm_k07_long_seed46_strict_w38_v2`
- **服务器**: westd-38929, GPU 0 (H100 97GB, 独占)
- **PID**: 16710
- **状态**: RUNNING
- **日志**: `~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed46_strict_w38_v2.log`
- **预估时长**: ~3h（参考同类实验）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 107635,
  "duration_api_ms": 80371,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "80c21e0a-e1ff-4315-a663-688cdd437079",
  "total_cost_usd": 0.5209484999999999,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 37546,
    "cache_read_input_tokens": 351208,
    "output_tokens": 4330,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37546,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 151,
        "cache_read_input_tokens": 48172,
        "cache_creation_input_tokens": 1219,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1219
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2222,
      "outputTokens": 28,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002362,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 4330,
      "cacheReadInputTokens": 351208,
      "cacheCreationInputTokens": 37546,
      "webSearchRequests": 0,
      "costUSD": 0.5185865,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d6e674ba-1fed-49e9-b37f-44ec247b7686"
}
```

</details>

---
