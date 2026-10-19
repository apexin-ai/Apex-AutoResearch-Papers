# audit deploy bjb1 32546 full audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 0
- **Tool calls:** 34
- **Original source:** `logs/workers/worker_audit-deploy_bjb1-32546-full-audit_20260523T101221.log`
- **Structured JSON:** [`a20bfdba68ecf2031ce3.json`](../../sessions/a2/a20bfdba68ecf2031ce3.json)

## Before a recorded user message

89 recorded events

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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
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
  "uuid": "d352af49-d634-4653-b149-7386c450698b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779634800,
    "rateLimitType": "seven_day",
    "utilization": 0.84,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "4fec738e-0a72-4564-be03-add33cffefbf",
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by auditing the GPU state on bjb1-32546. I'll use ssh_read_only to check the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "42396036-f5fd-40ef-abc6-ea4cc2db42d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToUY2fZaNiAY7E6SvFqN11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12953,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12953
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

### Assistant

_source line 5_

开始审计 bjb1-32546 GPU 状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "c7e3b994-96ef-4f7e-b9ec-434ed15d2861",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToUY2fZaNiAY7E6SvFqN11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12953,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12953
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0191HnoGaWXvPgFThkxf8nnx`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "2419eea4-f10c-4912-9b85-919e39a96de6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToUY2fZaNiAY7E6SvFqN11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12953,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12953
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

_source line 7 · 2026-05-23T10:12:35.350Z_

<details><summary>↩ Tool result · `toolu_0191HnoGaWXvPgFThkxf8nnx`</summary>

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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "f5fa8c98-c3f1-4308-b9f9-4ca29eef772f",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 27
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KoisupeQxnLUEA1JVjiUHp`</summary>

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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "e1f3027f-afcb-42b7-a969-cb23743b0742",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8cPcEENWotRCJGWDppPEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 24794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1037
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

_source line 9 · 2026-05-23T10:12:42.226Z_

<details><summary>↩ Tool result · `toolu_01KoisupeQxnLUEA1JVjiUHp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 21 %, 2848 MiB, 24564 MiB\\n1, 29 %, 2448 MiB, 24564 MiB\\n2, 22 %, 2354 MiB, 24564 MiB\\n3, 24 %, 5607 MiB, 24564 MiB\\n4, 37 %, 2942 MiB, 24564 MiB\\n5, 20 %, 3257 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "a10feff9-20ae-4aa4-8364-d983a68f4db3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 21 %, 2848 MiB, 24564 MiB\\\\n1, 29 %, 2448 MiB, 24564 MiB\\\\n2, 22 %, 2354 MiB, 24564 MiB\\\\n3, 24 %, 5607 MiB, 24564 MiB\\\\n4, 37 %, 2942 MiB, 24564 MiB\\\\n5, 20 %, 3257 MiB, 24564 MiB\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 21 %, 2848 MiB, 24564 MiB\\n1, 29 %, 2448 MiB, 24564 MiB\\n2, 22 %, 2354 MiB, 24564 MiB\\n3, 24 %, 5607 MiB, 24564 MiB\\n4, 37 %, 2942 MiB, 24564 MiB\\n5, 20 %, 3257 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.34}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01H44MRUdtWXwcFS3T6Qk6sb`</summary>

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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "6c3986e3-63ba-44ba-83e0-ca2e2ee23f32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8cPcEENWotRCJGWDppPEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 24794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1037
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

_source line 11 · 2026-05-23T10:12:42.799Z_

<details><summary>↩ Tool result · `toolu_01H44MRUdtWXwcFS3T6Qk6sb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"818121, GPU-220671b6-4e9c-db2d-1361-6ed090a1f3af, 2828 MiB\\n818386, GPU-ade291cb-7e13-f292-1714-09ef80919436, 2429 MiB\\n818658, GPU-4f00bf04-f4ff-96b6-3f56-723337f44abf, 2335 MiB\\n848576, GPU-00ae24f3-53b1-cd05-f561-fe7adbb64e72, 5587 MiB\\n818928, GPU-563702d3-df96-d375-0303-c9b9f202bdd2, 2922 MiB\\n835200, GPU-6d1331f1-8f19-df6c-71d5-e8ca2f3e2178, 3238 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "34e34b73-cf4c-4448-8b0b-43762a4f1cc8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"818121, GPU-220671b6-4e9c-db2d-1361-6ed090a1f3af, 2828 MiB\\\\n818386, GPU-ade291cb-7e13-f292-1714-09ef80919436, 2429 MiB\\\\n818658, GPU-4f00bf04-f4ff-96b6-3f56-723337f44abf, 2335 MiB\\\\n848576, GPU-00ae24f3-53b1-cd05-f561-fe7adbb64e72, 5587 MiB\\\\n818928, GPU-563702d3-df96-d375-0303-c9b9f202bdd2, 2922 MiB\\\\n835200, GPU-6d1331f1-8f19-df6c-71d5-e8ca2f3e2178, 3238 MiB\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"818121, GPU-220671b6-4e9c-db2d-1361-6ed090a1f3af, 2828 MiB\\n818386, GPU-ade291cb-7e13-f292-1714-09ef80919436, 2429 MiB\\n818658, GPU-4f00bf04-f4ff-96b6-3f56-723337f44abf, 2335 MiB\\n848576, GPU-00ae24f3-53b1-cd05-f561-fe7adbb64e72, 5587 MiB\\n818928, GPU-563702d3-df96-d375-0303-c9b9f202bdd2, 2922 MiB\\n835200, GPU-6d1331f1-8f19-df6c-71d5-e8ca2f3e2178, 3238 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E3UR57rLe3ct2M43t8Sybw`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps aux --no-headers -o pid,cmd --sort=-start_time",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "373d6b14-4e38-49cb-861e-bc64f89361c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8cPcEENWotRCJGWDppPEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 24794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1037
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

_source line 13 · 2026-05-23T10:12:43.573Z_

<details><summary>↩ Tool result · `toolu_01E3UR57rLe3ct2M43t8Sybw`</summary>

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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "a34cf1bd-42c8-4a05-b2c0-67a88d26908b",
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_018thsu1rNLRTF72av4vs62h`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "server": "bjb1-32546"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "8e0bc880-b07f-48a2-a6af-dc092cd58577",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8cPcEENWotRCJGWDppPEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 24794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1037
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

_source line 15 · 2026-05-23T10:12:47.195Z_

<details><summary>↩ Tool result · `toolu_018thsu1rNLRTF72av4vs62h`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T04:50:15.572Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": 805840, \"seed\": 67, \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:2\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T04:43:57.464Z\"}, \"failure_reason\": \"null - completed successfully, SR=10.0%\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:44:08.410Z\", \"metrics\": {\"overall_success_rate\": 0.1}, \"notes\": \"监控误报为 failed。实际正常完成 SR=10.0% (10/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.05_seed67.json (bjb1-32546，注意保存在 /root/logs/ 而非项目 logs/)。日志: /root/autodl-tmp/logs/norm005_seed67.log。\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T15:16:07.852Z\", \"updated_at\": \"2026-05-21T03:28:51.768Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 最薄数据点：obs_only ε=0.03 当前 n=1，seed43/44 已在跑。第 4 个 seed 确保极低 norm 端有可靠 error bars。\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-18T15:16:41.398Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed45.json\", \"finished_at\": \"2026-05-18T21:19:01.662Z\", \"training_hours\": 6.04}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"completed_at\": \"2026-05-18T21:19:07.176Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:19:22.371450+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: timeout (EXIT_CODE=124), 运行 ~6h 后在 task 5/10 rollout 5/10 处被杀。实验正常运行无报错，timeout_hours 设置过低（需 ~12-14h 完成全部 10 tasks × 10 rollouts）。部分结果: task1=0%, task2=0%, task3=20%, task4=30%（4个task完成）。建议: 重提交并将 timeout_hours 提高至 15h+\"}}, \"notes\": \"失败原因: timeout (EXIT_CODE=124), 运行 ~6h 后在 task 5/10 rollout 5/10 处被杀。实验正常运行无报错，timeout_hours 设置过低（需 ~12-14h 完成全部 10 tasks × 10 rollouts）。部分结果: task1=0%, task2=0%, task3=20%, task4=30%（4个task完成）。建议: 重提交并将 timeout_hours 提高至 15h+\", \"spec\": {\"command\": \"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.03 --n_rollouts 10 --seed 45 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb2-28827\", \"seed\": 45, \"model_name\": \"crm_obs_only\", \"data_path\": \"object_benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm003_seed45.log\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-18T15:15:11.377Z\", \"updated_at\": \"2026-05-21T03:28:46.427Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T15:16:33.436Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed44.json\", \"finished_at\": \"2026-05-20T19:25:22.704Z\", \"training_hours\": 52.15}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-18T21:18:43.893Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:18:53.264334+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T10:50:07.963621+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:25:48.137312+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 30, \"bbq_sauce\": 20, \"ketchup\": 0, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 30}}, \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\"}}, \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_norm003\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:34:52.011Z\", \"updated_at\": \"2026-05-20T11:29:58.029Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-20T06:37:44.903Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u evaluate.py --mode adaptive_k --threshold 0.074855 --benchmark spatial --seed 43 --K 10 --max_correction_norm 0.2\\\"\", \"finished_at\": \"2026-05-20T06:38:02.731Z\", \"training_hours\": 0.0}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u evaluate.py --mode adaptive_k --threshold 0.074855 --benchmark spatial --seed 43 --K 10 --max_correction_norm 0.2\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"293536\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43.log\", \"submitted_at\": \"2026-05-20T06:37:48.547Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 24.8, \"gpu_hours\": 0.01}, \"pid\": \"293536\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43.log\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T06:38:13.345Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T06:38:22.128132+00:00\"}]}, \"notes\": \"审计修正：JSON 完整（10 tasks × 10 rollouts），实验已成功完成。EXIT_CODE=2 为提交命令路径错误（evaluate.py vs src/evaluate.py），但实际运行的进程已正常完成并写出结果。\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:42:06.832Z\", \"updated_at\": \"2026-05-20T09:26:09.877Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"parent\": \"eval-adaptive-k-spatial-p50-seed43\", \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log\"}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-20T07:07:47.040Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p50_seed43.json\\\"\", \"finished_at\": \"2026-05-20T09:14:06.027Z\", \"training_hours\": 2.11}, \"pid\": \"303834\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T09:14:15.835758+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.4, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"mean_l2_distance\": 0.0903, \"total_steps\": 23414, \"fast_steps\": 10728, \"full_steps\": 12686, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:26:09.877Z\"}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:24:47.682Z\", \"updated_at\": \"2026-05-19T16:06:09.222Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed45. Spatial benchmark 第四个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\", \"spec\": {\"checkpoint_path\": \"N/A (vla_only baseline)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\"}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"pid\": \"932535\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 45 --output_file logs/eval_spatial_vla_only_seed45.json\", \"finished_at\": \"2026-05-19T15:17:27.081Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T15:17:34.738444+00:00\"}]}, \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (vla_only baseline)\", \"completed_at\": \"2026-05-19T15:47:20.192Z\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:15:14.634Z\", \"updated_at\": \"2026-05-19T11:28:09.358Z\", \"hypothesis\": \"perdof CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 薄数据点：perdof ε=0.03 当前 n=1 (seed42=14%)，seed43/44 已在跑。验证 per-DOF correction 在极低 norm 下表现。\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-18T15:16:48.731Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed45.json\"}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"652406\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-18T15:16:51.497Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"notes\": \"bjb1-32546 GPU process dead, no JSON output\", \"wall_clock_seconds\": 72677.9, \"gpu_hours\": 20.19}, \"pid\": \"652406\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed45.log\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T11:28:09.358Z\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:05:55.304Z\", \"updated_at\": \"2026-05-19T03:28:52.476Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed43 on LIBERO-Object。magnitude curve 低 ε 端当前只有 seed42 (14%, n=1)，第二个 seed 增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"640615\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed43.log\", \"submitted_at\": \"2026-05-18T13:25:05.368Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A-eval\", \"wall_clock_seconds\": 50627.1, \"gpu_hours\": 14.06}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": \"640615\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed43.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed43.json\", \"finished_at\": \"2026-05-19T03:25:56.586Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:26:06.809444+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:28:52.476Z\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:27:51.549Z\", \"updated_at\": \"2026-05-19T02:56:00.676Z\", \"hypothesis\": \"perdof CRM ε=0.05 seed43 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.05 当前只有 seed42 (14%, n=1)，第二个 seed 增强统计可靠性。\", \"parent\": \"eval-mag-perdof-norm005-object\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"642296\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed43.log\", \"submitted_at\": \"2026-05-18T13:28:51.027Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"max_correction_norm\": 0.05, \"seed\": 43, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"wall_clock_seconds\": 48429.6, \"gpu_hours\": 13.45}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"pid\": \"642296\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed43.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed43.json\", \"finished_at\": \"2026-05-19T02:35:05.529Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T02:35:13.418956+00:00\"}]}, \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T02:56:00.676Z\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:05:51.470Z\", \"updated_at\": \"2026-05-16T19:37:12.898Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed magnitude curve coverage. seed42 norm=0.3 object still running on bjb2-28827. Pairs with seed44 norm=0.2 for norm sensitivity across seeds.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T06:06:08.369Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed44.json\\\"\", \"finished_at\": \"2026-05-16T19:34:37.134Z\", \"training_hours\": 13.47}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"220777\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:34:40.416412+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T19:37:12.898Z\"}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:58:30.713Z\", \"updated_at\": \"2026-05-16T18:36:08.965Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:58:47.863Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:33:19.875Z\", \"training_hours\": 13.58}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"submitted_at\": \"2026-05-16T04:58:50.101Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 49038.9, \"gpu_hours\": 13.62}, \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:33:23.084588+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\", \"completed_at\": \"2026-05-16T18:36:08.965Z\"}}, \"count\": 11, \"total\": 11, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.982}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "46ba4d6c-d259-4111-a9bf-c14e7eb2927c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-obs-only-object-norm005-seed67\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:35:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:50:15.572Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 805840, \\\"seed\\\": 67, \\\"spec\\\": {\\\"command\\\": \\\"detected on GPU, submitted by prior Worker but not registered\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/acr-vla-conformal-refinement/\\\", \\\"data_count\\\": \\\"100 rollouts\\\", \\\"model_name\\\": \\\"crm_v3_norm/obs_only\\\", \\\"seed\\\": 67, \\\"gpu\\\": \\\"cuda:2\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T04:43:57.464Z\\\"}, \\\"failure_reason\\\": \\\"null - completed successfully, SR=10.0%\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-21T04:44:08.410Z\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.1}, \\\"notes\\\": \\\"监控误报为 failed。实际正常完成 SR=10.0% (10/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.05_seed67.json (bjb1-32546，注意保存在 /root/logs/ 而非项目 logs/)。日志: /root/autodl-tmp/logs/norm005_seed67.log。\\\"}, \\\"eval-obs-only-object-norm003-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-18T15:16:07.852Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:28:51.768Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 最薄数据点：obs_only ε=0.03 当前 n=1，seed43/44 已在跑。第 4 个 seed 确保极低 norm 端有可靠 error bars。\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"started_at\\\": \\\"2026-05-18T15:16:41.398Z\\\", \\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed45.json\\\", \\\"finished_at\\\": \\\"2026-05-18T21:19:01.662Z\\\", \\\"training_hours\\\": 6.04}, \\\"failure_reason\\\": \\\"EXIT_CODE=124 (timeout — exceeded timeout_hours)\\\", \\\"completed_at\\\": \\\"2026-05-18T21:19:07.176Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-18T21:19:22.371450+00:00\\\"}], \\\"previous_failure\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: timeout (EXIT_CODE=124), 运行 ~6h 后在 task 5/10 rollout 5/10 处被杀。实验正常运行无报错，timeout_hours 设置过低（需 ~12-14h 完成全部 10 tasks × 10 rollouts）。部分结果: task1=0%, task2=0%, task3=20%, task4=30%（4个task完成）。建议: 重提交并将 timeout_hours 提高至 15h+\\\"}}, \\\"notes\\\": \\\"失败原因: timeout (EXIT_CODE=124), 运行 ~6h 后在 task 5/10 rollout 5/10 处被杀。实验正常运行无报错，timeout_hours 设置过低（需 ~12-14h 完成全部 10 tasks × 10 rollouts）。部分结果: task1=0%, task2=0%, task3=20%, task4=30%（4个task完成）。建议: 重提交并将 timeout_hours 提高至 15h+\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.03 --n_rollouts 10 --seed 45 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"seed\\\": 45, \\\"model_name\\\": \\\"crm_obs_only\\\", \\\"data_path\\\": \\\"object_benchmark\\\", \\\"data_count\\\": 10, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"object\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm003_seed45.log\\\"}, \\\"eval-obs-only-object-norm003-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 2, \\\"created_at\\\": \\\"2026-05-18T15:15:11.377Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:28:46.427Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-18T15:16:33.436Z\\\", \\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed44.json\\\", \\\"finished_at\\\": \\\"2026-05-20T19:25:22.704Z\\\", \\\"training_hours\\\": 52.15}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"completed_at\\\": \\\"2026-05-18T21:18:43.893Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-18T21:18:53.264334+00:00\\\"}, {\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T10:50:07.963621+00:00\\\"}, {\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T19:25:48.137312+00:00\\\"}], \\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 15, \\\"total_rollouts\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 30, \\\"bbq_sauce\\\": 20, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 10, \\\"butter\\\": 10, \\\"milk\\\": 20, \\\"chocolate_pudding\\\": 30, \\\"orange_juice\\\": 30}}, \\\"notes\\\": \\\"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\\\"}}, \\\"notes\\\": \\\"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed44.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only_norm003\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}}, \\\"eval-adaptive-k-spatial-p50-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T06:34:52.011Z\\\", \\\"updated_at\\\": \\\"2026-05-20T11:29:58.029Z\\\", \\\"hypothesis\\\": \\\"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"started_at\\\": \\\"2026-05-20T06:37:44.903Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u evaluate.py --mode adaptive_k --threshold 0.074855 --benchmark spatial --seed 43 --K 10 --max_correction_norm 0.2\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-20T06:38:02.731Z\\\", \\\"training_hours\\\": 0.0}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u evaluate.py --mode adaptive_k --threshold 0.074855 --benchmark spatial --seed 43 --K 10 --max_correction_norm 0.2\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"293536\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T06:37:48.547Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 24.8, \\\"gpu_hours\\\": 0.01}, \\\"pid\\\": \\\"293536\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43.log\\\", \\\"failure_reason\\\": \\\"\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T06:38:13.345Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T06:38:22.128132+00:00\\\"}]}, \\\"notes\\\": \\\"审计修正：JSON 完整（10 tasks × 10 rollouts），实验已成功完成。EXIT_CODE=2 为提交命令路径错误（evaluate.py vs src/evaluate.py），但实际运行的进程已正常完成并写出结果。\\\", \\\"metrics\\\": {\\\"sr\\\": 0.33, \\\"avg_K\\\": 6.33, \\\"fast_path_ratio\\\": 0.458, \\\"adaptive_trigger_rate\\\": 0.542, \\\"threshold\\\": 0.074855}}, \\\"eval-adaptive-k-spatial-p50-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T06:42:06.832Z\\\", \\\"updated_at\\\": \\\"2026-05-20T09:26:09.877Z\\\", \\\"hypothesis\\\": \\\"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\\\", \\\"parent\\\": \\\"eval-adaptive-k-spatial-p50-seed43\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log\\\"}, \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-20T07:07:47.040Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p50_seed43.json\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-20T09:14:06.027Z\\\", \\\"training_hours\\\": 2.11}, \\\"pid\\\": \\\"303834\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T09:14:15.835758+00:00\\\"}]}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.33, \\\"per_task_sr\\\": {\\\"between_plate_and_ramekin\\\": 0.8, \\\"next_to_ramekin\\\": 1, \\\"from_table_center\\\": 0, \\\"on_cookie_box\\\": 0.4, \\\"in_top_drawer\\\": 0.1, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 0.9, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0.1, \\\"on_wooden_cabinet\\\": 0}, \\\"avg_k\\\": 6.33, \\\"fast_path_ratio\\\": 0.458, \\\"adaptive_trigger_rate\\\": 0.542, \\\"mean_l2_distance\\\": 0.0903, \\\"total_steps\\\": 23414, \\\"fast_steps\\\": 10728, \\\"full_steps\\\": 12686, \\\"threshold\\\": 0.074855, \\\"total_rollouts\\\": 100}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T09:26:09.877Z\\\"}, \\\"eval-vla-only-spatial-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T13:24:47.682Z\\\", \\\"updated_at\\\": \\\"2026-05-19T16:06:09.222Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Spatial seed45. Spatial benchmark 第四个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A (vla_only baseline)\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\\"}, \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"932535\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 45 --output_file logs/eval_spatial_vla_only_seed45.json\\\", \\\"finished_at\\\": \\\"2026-05-19T15:17:27.081Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-19T15:17:34.738444+00:00\\\"}]}, \\\"metrics\\\": {\\\"success_rate\\\": 0.27, \\\"per_task\\\": {\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": 0.7, \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": 0.9, \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": 0, \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": 0.2, \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0, \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": 0, \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": 0.9, \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": 0, \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": 0, \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": 0}, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"N/A (vla_only baseline)\\\", \\\"completed_at\\\": \\\"2026-05-19T15:47:20.192Z\\\"}, \\\"eval-perdof-object-norm003-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T15:15:14.634Z\\\", \\\"updated_at\\\": \\\"2026-05-19T11:28:09.358Z\\\", \\\"hypothesis\\\": \\\"perdof CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 薄数据点：perdof ε=0.03 当前 n=1 (seed42=14%)，seed43/44 已在跑。验证 per-DOF correction 在极低 norm 下表现。\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"started_at\\\": \\\"2026-05-18T15:16:48.731Z\\\", \\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed45.json\\\"}, \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed45.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"652406\\\", \\\"log_path\\\": \\\"N/A\\\", \\\"submitted_at\\\": \\\"2026-05-18T15:16:51.497Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"notes\\\": \\\"bjb1-32546 GPU process dead, no JSON output\\\", \\\"wall_clock_seconds\\\": 72677.9, \\\"gpu_hours\\\": 20.19}, \\\"pid\\\": \\\"652406\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed45.log\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-19T11:28:09.358Z\\\"}, \\\"eval-perdof-object-norm003-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T13:05:55.304Z\\\", \\\"updated_at\\\": \\\"2026-05-19T03:28:52.476Z\\\", \\\"hypothesis\\\": \\\"perdof CRM ε=0.03 seed43 on LIBERO-Object。magnitude curve 低 ε 端当前只有 seed42 (14%, n=1)，第二个 seed 增强统计。\\\", \\\"parent\\\": \\\"eval-mag-perdof-norm003-object\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed43.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"640615\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed43.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T13:25:05.368Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"N/A-eval\\\", \\\"wall_clock_seconds\\\": 50627.1, \\\"gpu_hours\\\": 14.06}, \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": \\\"640615\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed43.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed43.json\\\", \\\"finished_at\\\": \\\"2026-05-19T03:25:56.586Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-19T03:26:06.809444+00:00\\\"}]}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.13, \\\"total_rollouts\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.3}}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T03:28:52.476Z\\\"}, \\\"eval-perdof-object-norm005-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T13:27:51.549Z\\\", \\\"updated_at\\\": \\\"2026-05-19T02:56:00.676Z\\\", \\\"hypothesis\\\": \\\"perdof CRM ε=0.05 seed43 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.05 当前只有 seed42 (14%, n=1)，第二个 seed 增强统计可靠性。\\\", \\\"parent\\\": \\\"eval-mag-perdof-norm005-object\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed43.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"642296\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed43.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T13:28:51.027Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"max_correction_norm\\\": 0.05, \\\"seed\\\": 43, \\\"benchmark\\\": \\\"object\\\", \\\"mode\\\": \\\"crm_perdof\\\", \\\"wall_clock_seconds\\\": 48429.6, \\\"gpu_hours\\\": 13.45}, \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"642296\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed43.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed43.json\\\", \\\"finished_at\\\": \\\"2026-05-19T02:35:05.529Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-19T02:35:13.418956+00:00\\\"}]}, \\\"metrics\\\": {\\\"success_rate\\\": 0.13, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.3, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0.1, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.3}}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T02:56:00.676Z\\\"}, \\\"eval-obs-only-object-norm03-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T06:05:51.470Z\\\", \\\"updated_at\\\": \\\"2026-05-16T19:37:12.898Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed magnitude curve coverage. seed42 norm=0.3 object still running on bjb2-28827. Pairs with seed44 norm=0.2 for norm sensitivity across seeds.\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"started_at\\\": \\\"2026-05-16T06:06:08.369Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed44.json\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-16T19:34:37.134Z\\\", \\\"training_hours\\\": 13.47}, \\\"spec\\\": {\\\"data_path\\\": \\\"LIBERO object benchmark\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_obs_only (327198 params)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO object 10 tasks x 10 rollouts\\\"}, \\\"pid\\\": \\\"220777\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed44.log\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-16T19:34:40.416412+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.18, \\\"total_rollouts\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0.1, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0.1, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.3}}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"completed_at\\\": \\\"2026-05-16T19:37:12.898Z\\\"}, \\\"eval-vla-mean-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T04:58:30.713Z\\\", \\\"updated_at\\\": \\\"2026-05-16T18:36:08.965Z\\\", \\\"hypothesis\\\": \\\"VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"started_at\\\": \\\"2026-05-16T04:58:47.863Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-16T18:33:19.875Z\\\", \\\"training_hours\\\": 13.58}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"212655\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\\\", \\\"submitted_at\\\": \\\"2026-05-16T04:58:50.101Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 49038.9, \\\"gpu_hours\\\": 13.62}, \\\"pid\\\": \\\"212655\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-16T18:33:23.084588+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.1, \\\"per_task_sr\\\": {\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": 0.3, \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": 0.2, \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": 0.2}}, \\\"checkpoint_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\\\", \\\"completed_at\\\": \\\"2026-05-16T18:36:08.965Z\\\"}}, \\\"count\\\": 11, \\\"total\\\": 11, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.982}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T04:50:15.572Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": 805840, \"seed\": 67, \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:2\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T04:43:57.464Z\"}, \"failure_reason\": \"null - completed successfully, SR=10.0%\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:44:08.410Z\", \"metrics\": {\"overall_success_rate\": 0.1}, \"notes\": \"监控误报为 failed。实际正常完成 SR=10.0% (10/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.05_seed67.json (bjb1-32546，注意保存在 /root/logs/ 而非项目 logs/)。日志: /root/autodl-tmp/logs/norm005_seed67.log。\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T15:16:07.852Z\", \"updated_at\": \"2026-05-21T03:28:51.768Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 最薄数据点：obs_only ε=0.03 当前 n=1，seed43/44 已在跑。第 4 个 seed 确保极低 norm 端有可靠 error bars。\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-18T15:16:41.398Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed45.json\", \"finished_at\": \"2026-05-18T21:19:01.662Z\", \"training_hours\": 6.04}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"completed_at\": \"2026-05-18T21:19:07.176Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:19:22.371450+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: timeout (EXIT_CODE=124), 运行 ~6h 后在 task 5/10 rollout 5/10 处被杀。实验正常运行无报错，timeout_hours 设置过低（需 ~12-14h 完成全部 10 tasks × 10 rollouts）。部分结果: task1=0%, task2=0%, task3=20%, task4=30%（4个task完成）。建议: 重提交并将 timeout_hours 提高至 15h+\"}}, \"notes\": \"失败原因: timeout (EXIT_CODE=124), 运行 ~6h 后在 task 5/10 rollout 5/10 处被杀。实验正常运行无报错，timeout_hours 设置过低（需 ~12-14h 完成全部 10 tasks × 10 rollouts）。部分结果: task1=0%, task2=0%, task3=20%, task4=30%（4个task完成）。建议: 重提交并将 timeout_hours 提高至 15h+\", \"spec\": {\"command\": \"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.03 --n_rollouts 10 --seed 45 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb2-28827\", \"seed\": 45, \"model_name\": \"crm_obs_only\", \"data_path\": \"object_benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm003_seed45.log\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-18T15:15:11.377Z\", \"updated_at\": \"2026-05-21T03:28:46.427Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T15:16:33.436Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed44.json\", \"finished_at\": \"2026-05-20T19:25:22.704Z\", \"training_hours\": 52.15}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-18T21:18:43.893Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:18:53.264334+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T10:50:07.963621+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:25:48.137312+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 30, \"bbq_sauce\": 20, \"ketchup\": 0, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 30}}, \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\"}}, \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_norm003\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:34:52.011Z\", \"updated_at\": \"2026-05-20T11:29:58.029Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-20T06:37:44.903Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u evaluate.py --mode adaptive_k --threshold 0.074855 --benchmark spatial --seed 43 --K 10 --max_correction_norm 0.2\\\"\", \"finished_at\": \"2026-05-20T06:38:02.731Z\", \"training_hours\": 0.0}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u evaluate.py --mode adaptive_k --threshold 0.074855 --benchmark spatial --seed 43 --K 10 --max_correction_norm 0.2\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"293536\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43.log\", \"submitted_at\": \"2026-05-20T06:37:48.547Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 24.8, \"gpu_hours\": 0.01}, \"pid\": \"293536\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43.log\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T06:38:13.345Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T06:38:22.128132+00:00\"}]}, \"notes\": \"审计修正：JSON 完整（10 tasks × 10 rollouts），实验已成功完成。EXIT_CODE=2 为提交命令路径错误（evaluate.py vs src/evaluate.py），但实际运行的进程已正常完成并写出结果。\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:42:06.832Z\", \"updated_at\": \"2026-05-20T09:26:09.877Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"parent\": \"eval-adaptive-k-spatial-p50-seed43\", \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log\"}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-20T07:07:47.040Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p50_seed43.json\\\"\", \"finished_at\": \"2026-05-20T09:14:06.027Z\", \"training_hours\": 2.11}, \"pid\": \"303834\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T09:14:15.835758+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.4, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"mean_l2_distance\": 0.0903, \"total_steps\": 23414, \"fast_steps\": 10728, \"full_steps\": 12686, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:26:09.877Z\"}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:24:47.682Z\", \"updated_at\": \"2026-05-19T16:06:09.222Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed45. Spatial benchmark 第四个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\", \"spec\": {\"checkpoint_path\": \"N/A (vla_only baseline)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\"}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"pid\": \"932535\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 45 --output_file logs/eval_spatial_vla_only_seed45.json\", \"finished_at\": \"2026-05-19T15:17:27.081Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T15:17:34.738444+00:00\"}]}, \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (vla_only baseline)\", \"completed_at\": \"2026-05-19T15:47:20.192Z\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:15:14.634Z\", \"updated_at\": \"2026-05-19T11:28:09.358Z\", \"hypothesis\": \"perdof CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 薄数据点：perdof ε=0.03 当前 n=1 (seed42=14%)，seed43/44 已在跑。验证 per-DOF correction 在极低 norm 下表现。\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-18T15:16:48.731Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed45.json\"}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"652406\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-18T15:16:51.497Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"notes\": \"bjb1-32546 GPU process dead, no JSON output\", \"wall_clock_seconds\": 72677.9, \"gpu_hours\": 20.19}, \"pid\": \"652406\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed45.log\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T11:28:09.358Z\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:05:55.304Z\", \"updated_at\": \"2026-05-19T03:28:52.476Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed43 on LIBERO-Object。magnitude curve 低 ε 端当前只有 seed42 (14%, n=1)，第二个 seed 增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"640615\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed43.log\", \"submitted_at\": \"2026-05-18T13:25:05.368Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A-eval\", \"wall_clock_seconds\": 50627.1, \"gpu_hours\": 14.06}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": \"640615\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed43.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed43.json\", \"finished_at\": \"2026-05-19T03:25:56.586Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:26:06.809444+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:28:52.476Z\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:27:51.549Z\", \"updated_at\": \"2026-05-19T02:56:00.676Z\", \"hypothesis\": \"perdof CRM ε=0.05 seed43 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.05 当前只有 seed42 (14%, n=1)，第二个 seed 增强统计可靠性。\", \"parent\": \"eval-mag-perdof-norm005-object\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"642296\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed43.log\", \"submitted_at\": \"2026-05-18T13:28:51.027Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"max_correction_norm\": 0.05, \"seed\": 43, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"wall_clock_seconds\": 48429.6, \"gpu_hours\": 13.45}, \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"pid\": \"642296\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed43.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed43.json\", \"finished_at\": \"2026-05-19T02:35:05.529Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T02:35:13.418956+00:00\"}]}, \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T02:56:00.676Z\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:05:51.470Z\", \"updated_at\": \"2026-05-16T19:37:12.898Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed magnitude curve coverage. seed42 norm=0.3 object still running on bjb2-28827. Pairs with seed44 norm=0.2 for norm sensitivity across seeds.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T06:06:08.369Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed44.json\\\"\", \"finished_at\": \"2026-05-16T19:34:37.134Z\", \"training_hours\": 13.47}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"220777\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:34:40.416412+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T19:37:12.898Z\"}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:58:30.713Z\", \"updated_at\": \"2026-05-16T18:36:08.965Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:58:47.863Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:33:19.875Z\", \"training_hours\": 13.58}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"submitted_at\": \"2026-05-16T04:58:50.101Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 49038.9, \"gpu_hours\": 13.62}, \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:33:23.084588+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\", \"completed_at\": \"2026-05-16T18:36:08.965Z\"}}, \"count\": 11, \"total\": 11, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.982}}"
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
Let me analyze the GPU state:

GPU 0: 21% util, 2848 MiB used, PID 818121
GPU 1: 29% util, 2448 MiB used, PID 818386
GPU 2: 22% util, 2354 MiB used, PID 818658
GPU 3: 24% util, 5607 MiB used, PID 848576
GPU 4: 37% util, 2942 MiB used, PID 818928
GPU 5: 20% util, 3257 MiB used, PID 835200


I can see that cuda:3 and cuda:5 have registered jobs running, but the processes on GPUs 0, 1, 2, and 4 aren't showing up in the registry as active. Let me check what those PIDs are actually doing by looking at the tmux sessions and process details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "4139ca1d-5e10-4589-b0f5-08ff7f6a4d2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQCcHwJmKEZwHo84bBdxzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11610,
      "cache_read_input_tokens": 25831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11610
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

_source line 17_

6 个 GPU 都有进程在跑。需要进一步确认 cuda:0/1/2/4 上的进程是什么。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "5c5b4836-2a1b-4041-8391-a4c0e2f60ab7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQCcHwJmKEZwHo84bBdxzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11610,
      "cache_read_input_tokens": 25831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11610
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

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017jDpsWbedNbXp6uowWASjV`</summary>

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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "b84f2562-be34-4104-b353-049d393c4fdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQCcHwJmKEZwHo84bBdxzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11610,
      "cache_read_input_tokens": 25831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11610
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

_source line 19 · 2026-05-23T10:12:58.011Z_

<details><summary>↩ Tool result · `toolu_017jDpsWbedNbXp6uowWASjV`</summary>

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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "223ffbe7-32e6-4a79-b2e4-eb4dd6d4d91b",
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

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PvmsiqyG5LutKydsc751cv`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps -p 818121,818386,818658,818928,848576,835200 -o pid,etimes,cmd --no-headers",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "14058f62-50d2-48e8-a109-79b53a17cd48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQCcHwJmKEZwHo84bBdxzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11610,
      "cache_read_input_tokens": 25831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11610
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

_source line 21 · 2026-05-23T10:12:59.210Z_

<details><summary>↩ Tool result · `toolu_01PvmsiqyG5LutKydsc751cv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"818121    5577 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\n818386    5574 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05\\n818658    5571 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\n818928    5569 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05\\n835200    4094 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\n848576    2865 python -u src/evaluate.py --mode vla_only --benchmark long --seed 42 --n_rollouts 20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "3cc8fc83-063a-4004-871d-47cd75ccab57",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"818121    5577 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\\\n818386    5574 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05\\\\n818658    5571 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\\\n818928    5569 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05\\\\n835200    4094 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\\\n848576    2865 python -u src/evaluate.py --mode vla_only --benchmark long --seed 42 --n_rollouts 20\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"818121    5577 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\n818386    5574 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05\\n818658    5571 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\n818928    5569 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05\\n835200    4094 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\n848576    2865 python -u src/evaluate.py --mode vla_only --benchmark long --seed 42 --n_rollouts 20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. All 6 GPUs are actively running experiments:

| GPU | PID | Elapsed (s) | Experiment |
|-----|-----|-------------|------------|
| cuda:0 | 818121 | 5577 (~1.5h) | Object Adaptive tau=0.25 s43 |
| cuda:1 | 818386 | 5574 (~1.5h) | Goal CRM norm=0.05 s43 |


| cuda:2 | 818658 | 5571 (~1.5h) | Goal Adaptive tau=0.25 s43 |
| cuda:3 | 848576 | 2865 (~48min) | Long VLA-only s42 |
| cuda:4 | 818928 | 5569 (~1.5h) | Object CRM norm=0.05 s43 |
| cuda:5 | 835200 | 4094 (~1.1h) | Goal Adaptive tau=0.25 s44 |

Every GPU is currently occupied with experiments, with most running for about an hour and a half, except for cuda:3 which started more recently at around 48 minutes elapsed.

Looking at the registry for running experiments on this server, I can confirm cuda:3 and cuda:5 match the expected tasks, but the other four GPUs are running variations of Goal Adaptive and Object CRM experiments that I need to verify against what was actually supposed to be deployed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "d3c0bc3f-632d-4ecb-93af-479381d1862c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yCnxyTRKpwZhbN8cupzeU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 37441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1329
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

_source line 23_

全部 6 个 GPU 都有实验在跑，运行时长 ~48min 到 ~1.5h。让我确认这些实验的 registry 状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "2c7aff6c-0913-4c15-b7c3-2791f01db4ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yCnxyTRKpwZhbN8cupzeU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 37441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1329
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

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01DTm3TJAnZdpBt4ygW8hT5K`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "RUNNING"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "5272a02a-bddd-4c2c-8a29-bdea0913431c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yCnxyTRKpwZhbN8cupzeU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 37441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1329
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

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01PstMLydzfkNaiHzt8wtS4w`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "PREPARING"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "76306475-50af-461f-9049-16727e8bc247",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yCnxyTRKpwZhbN8cupzeU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 37441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1329
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

_source line 26 · 2026-05-23T10:13:21.183Z_

<details><summary>↩ Tool result · `toolu_01DTm3TJAnZdpBt4ygW8hT5K`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-k2mean-goal-s42-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:33:20.623Z\", \"updated_at\": \"2026-05-23T10:10:52.074Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --n_rollouts 20 --seed 42\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"eval-supp-k2mean-goal-s42\", \"eval_data\": \"goal\"}, \"hypothesis\": \"K=2 mean baseline on Goal seed42 (retry). Goal VLA-only baseline = 83.5%. Isolates multi-sample averaging effect on Goal tasks.\"}, \"eval-supp-k2mean-goal-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:38:57.518Z\", \"updated_at\": \"2026-05-23T10:10:46.253Z\", \"hypothesis\": \"K=2 mean baseline on Goal seed43. Goal VLA-only baseline = 83.5%. Isolates multi-sample averaging effect on Goal tasks. Second seed for 3-seed mean±std.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite goal --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Goal\", \"gpu\": \"cuda:4\", \"pid\": 16445}}, \"eval-supp-goal-reconvla-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:19:47.656Z\", \"updated_at\": \"2026-05-23T10:10:40.768Z\", \"hypothesis\": \"Reconvla K=10 argmin on Goal seed43. Goal VLA-only baseline = 83.5%. s42=81.0% (-2.5pp negative). Second seed for Goal reconvla multi-seed validation.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python src/evaluate.py --mode reconvla --K 10 --suite goal --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Goal\", \"gpu\": \"cuda:5\", \"pid\": 34385}}, \"eval-supp-adapt-tau025-goal-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:05:16.443Z\", \"updated_at\": \"2026-05-23T10:10:34.864Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed44. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Third seed for 3-seed mean±std on Goal Adaptive performance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla+crm_adaptive_tau025\", \"data_path\": \"goal_benchmark\", \"data_count\": 20, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"goal\"}}, \"eval-supp-long-vla-only-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:25:38.707Z\", \"updated_at\": \"2026-05-23T09:26:16.634Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark long --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:3\"], \"seed\": 42, \"model_name\": \"SmolVLA\", \"tmux_session\": \"eval-supp-long-vla-only-s42\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200}}, \"eval-supp-obj-reconvla-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:59:10.206Z\", \"updated_at\": \"2026-05-23T08:59:57.778Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object seed43. Multi-seed validation (s42=79.0%). Tests cross-seed consistency of reconvla selection on Object suite.\", \"parent\": \"eval-supp-obj-reconvla-s42\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --K 10 --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu_ids\": [\"cuda:2\"], \"seed\": 43, \"data_path\": \"LIBERO/object\", \"data_count\": 200, \"model_name\": \"smolvla-reconvla\", \"checkpoint_source\": \"smolvla_libero\", \"eval_data\": \"LIBERO-object-10tasks-20rollouts\"}}, \"eval-supp-reconvla-spatial-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:03:44.347Z\", \"updated_at\": \"2026-05-23T08:20:46.950Z\", \"hypothesis\": \"Reconvla K=10 argmin on Spatial seed44. Multi-seed validation (with s42=79%, s43). Third seed for 3-seed mean±std statistical claim on reconvla.\", \"parent\": \"eval-supp-reconvla-k2-spatial-s42\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python src/evaluate.py --mode reconvla --K 10 --suite spatial --n_rollouts 20 --seed 44\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:3\", \"pid\": 34383}}, \"eval-supp-reconvla-spatial-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:03:39.046Z\", \"updated_at\": \"2026-05-23T08:20:41.363Z\", \"hypothesis\": \"Reconvla K=10 argmin on Spatial seed43. Multi-seed validation (with s42=79%, s44). Tests cross-seed consistency of reconvla selection strategy.\", \"parent\": \"eval-supp-reconvla-k2-spatial-s42\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python src/evaluate.py --mode reconvla --K 10 --suite spatial --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:1\", \"pid\": 34387}}, \"eval-supp-k2mean-object-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:38:54.570Z\", \"updated_at\": \"2026-05-23T08:19:19.844Z\", \"hypothesis\": \"K=2 mean baseline multi-seed on Object seed43. Isolates multi-sample averaging effect from CRM correction. Second seed for 3-seed mean±std on K=2 mean baseline.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite object --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"cuda:2\", \"pid\": 16441}}, \"eval-supp-k2mean-spatial-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:38:51.694Z\", \"updated_at\": \"2026-05-23T08:19:14.264Z\", \"hypothesis\": \"K=2 mean baseline multi-seed on Spatial seed43. Isolates multi-sample averaging effect from CRM correction. Second seed for 3-seed mean±std on K=2 mean baseline.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite spatial --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:0\", \"pid\": 16439}}}, \"count\": 10, \"total\": 10, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.5815}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "4615297f-e4f8-4115-8c4d-06a03fea940f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-k2mean-goal-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T08:33:20.623Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:10:52.074Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --n_rollouts 20 --seed 42\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"data_path\\\": \\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\", \\\"data_count\\\": 20, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"eval-supp-k2mean-goal-s42\\\", \\\"eval_data\\\": \\\"goal\\\"}, \\\"hypothesis\\\": \\\"K=2 mean baseline on Goal seed42 (retry). Goal VLA-only baseline = 83.5%. Isolates multi-sample averaging effect on Goal tasks.\\\"}, \\\"eval-supp-k2mean-goal-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T07:38:57.518Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:10:46.253Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Goal seed43. Goal VLA-only baseline = 83.5%. Isolates multi-sample averaging effect on Goal tasks. Second seed for 3-seed mean±std.\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite goal --n_rollouts 20 --seed 43\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"/root/acr-vla-conformal-refinement\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"n/a\\\", \\\"eval_data\\\": \\\"LIBERO-Goal\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"pid\\\": 16445}}, \\\"eval-supp-goal-reconvla-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T08:19:47.656Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:10:40.768Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on Goal seed43. Goal VLA-only baseline = 83.5%. s42=81.0% (-2.5pp negative). Second seed for Goal reconvla multi-seed validation.\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python src/evaluate.py --mode reconvla --K 10 --suite goal --n_rollouts 20 --seed 43\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"/root/acr-vla-conformal-refinement\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"n/a\\\", \\\"eval_data\\\": \\\"LIBERO-Goal\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": 34385}}, \\\"eval-supp-adapt-tau025-goal-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T09:05:16.443Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:10:34.864Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Goal seed44. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Third seed for 3-seed mean±std on Goal Adaptive performance.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 44, \\\"model_name\\\": \\\"smolvla+crm_adaptive_tau025\\\", \\\"data_path\\\": \\\"goal_benchmark\\\", \\\"data_count\\\": 20, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"goal\\\"}}, \\\"eval-supp-long-vla-only-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T09:25:38.707Z\\\", \\\"updated_at\\\": \\\"2026-05-23T09:26:16.634Z\\\", \\\"hypothesis\\\": \\\"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode vla_only --benchmark long --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu_ids\\\": [\\\"cuda:3\\\"], \\\"seed\\\": 42, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"tmux_session\\\": \\\"eval-supp-long-vla-only-s42\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200}}, \\\"eval-supp-obj-reconvla-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T08:59:10.206Z\\\", \\\"updated_at\\\": \\\"2026-05-23T08:59:57.778Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on Object seed43. Multi-seed validation (s42=79.0%). Tests cross-seed consistency of reconvla selection on Object suite.\\\", \\\"parent\\\": \\\"eval-supp-obj-reconvla-s42\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode reconvla --K 10 --benchmark object --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu_ids\\\": [\\\"cuda:2\\\"], \\\"seed\\\": 43, \\\"data_path\\\": \\\"LIBERO/object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla-reconvla\\\", \\\"checkpoint_source\\\": \\\"smolvla_libero\\\", \\\"eval_data\\\": \\\"LIBERO-object-10tasks-20rollouts\\\"}}, \\\"eval-supp-reconvla-spatial-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T07:03:44.347Z\\\", \\\"updated_at\\\": \\\"2026-05-23T08:20:46.950Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on Spatial seed44. Multi-seed validation (with s42=79%, s43). Third seed for 3-seed mean±std statistical claim on reconvla.\\\", \\\"parent\\\": \\\"eval-supp-reconvla-k2-spatial-s42\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python src/evaluate.py --mode reconvla --K 10 --suite spatial --n_rollouts 20 --seed 44\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"/root/acr-vla-conformal-refinement\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"n/a\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 34383}}, \\\"eval-supp-reconvla-spatial-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T07:03:39.046Z\\\", \\\"updated_at\\\": \\\"2026-05-23T08:20:41.363Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on Spatial seed43. Multi-seed validation (with s42=79%, s44). Tests cross-seed consistency of reconvla selection strategy.\\\", \\\"parent\\\": \\\"eval-supp-reconvla-k2-spatial-s42\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python src/evaluate.py --mode reconvla --K 10 --suite spatial --n_rollouts 20 --seed 43\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"/root/acr-vla-conformal-refinement\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"n/a\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 34387}}, \\\"eval-supp-k2mean-object-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T07:38:54.570Z\\\", \\\"updated_at\\\": \\\"2026-05-23T08:19:19.844Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline multi-seed on Object seed43. Isolates multi-sample averaging effect from CRM correction. Second seed for 3-seed mean±std on K=2 mean baseline.\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite object --n_rollouts 20 --seed 43\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"/root/acr-vla-conformal-refinement\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"n/a\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 16441}}, \\\"eval-supp-k2mean-spatial-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T07:38:51.694Z\\\", \\\"updated_at\\\": \\\"2026-05-23T08:19:14.264Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline multi-seed on Spatial seed43. Isolates multi-sample averaging effect from CRM correction. Second seed for 3-seed mean±std on K=2 mean baseline.\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite spatial --n_rollouts 20 --seed 43\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"data_path\\\": \\\"/root/acr-vla-conformal-refinement\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"n/a\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 16439}}}, \\\"count\\\": 10, \\\"total\\\": 10, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.5815}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-k2mean-goal-s42-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:33:20.623Z\", \"updated_at\": \"2026-05-23T10:10:52.074Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --n_rollouts 20 --seed 42\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"eval-supp-k2mean-goal-s42\", \"eval_data\": \"goal\"}, \"hypothesis\": \"K=2 mean baseline on Goal seed42 (retry). Goal VLA-only baseline = 83.5%. Isolates multi-sample averaging effect on Goal tasks.\"}, \"eval-supp-k2mean-goal-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:38:57.518Z\", \"updated_at\": \"2026-05-23T10:10:46.253Z\", \"hypothesis\": \"K=2 mean baseline on Goal seed43. Goal VLA-only baseline = 83.5%. Isolates multi-sample averaging effect on Goal tasks. Second seed for 3-seed mean±std.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite goal --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Goal\", \"gpu\": \"cuda:4\", \"pid\": 16445}}, \"eval-supp-goal-reconvla-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:19:47.656Z\", \"updated_at\": \"2026-05-23T10:10:40.768Z\", \"hypothesis\": \"Reconvla K=10 argmin on Goal seed43. Goal VLA-only baseline = 83.5%. s42=81.0% (-2.5pp negative). Second seed for Goal reconvla multi-seed validation.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python src/evaluate.py --mode reconvla --K 10 --suite goal --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Goal\", \"gpu\": \"cuda:5\", \"pid\": 34385}}, \"eval-supp-adapt-tau025-goal-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:05:16.443Z\", \"updated_at\": \"2026-05-23T10:10:34.864Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed44. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Third seed for 3-seed mean±std on Goal Adaptive performance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla+crm_adaptive_tau025\", \"data_path\": \"goal_benchmark\", \"data_count\": 20, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"goal\"}}, \"eval-supp-long-vla-only-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:25:38.707Z\", \"updated_at\": \"2026-05-23T09:26:16.634Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark long --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:3\"], \"seed\": 42, \"model_name\": \"SmolVLA\", \"tmux_session\": \"eval-supp-long-vla-only-s42\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200}}, \"eval-supp-obj-reconvla-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:59:10.206Z\", \"updated_at\": \"2026-05-23T08:59:57.778Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object seed43. Multi-seed validation (s42=79.0%). Tests cross-seed consistency of reconvla selection on Object suite.\", \"parent\": \"eval-supp-obj-reconvla-s42\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --K 10 --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu_ids\": [\"cuda:2\"], \"seed\": 43, \"data_path\": \"LIBERO/object\", \"data_count\": 200, \"model_name\": \"smolvla-reconvla\", \"checkpoint_source\": \"smolvla_libero\", \"eval_data\": \"LIBERO-object-10tasks-20rollouts\"}}, \"eval-supp-reconvla-spatial-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:03:44.347Z\", \"updated_at\": \"2026-05-23T08:20:46.950Z\", \"hypothesis\": \"Reconvla K=10 argmin on Spatial seed44. Multi-seed validation (with s42=79%, s43). Third seed for 3-seed mean±std statistical claim on reconvla.\", \"parent\": \"eval-supp-reconvla-k2-spatial-s42\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python src/evaluate.py --mode reconvla --K 10 --suite spatial --n_rollouts 20 --seed 44\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:3\", \"pid\": 34383}}, \"eval-supp-reconvla-spatial-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:03:39.046Z\", \"updated_at\": \"2026-05-23T08:20:41.363Z\", \"hypothesis\": \"Reconvla K=10 argmin on Spatial seed43. Multi-seed validation (with s42=79%, s44). Tests cross-seed consistency of reconvla selection strategy.\", \"parent\": \"eval-supp-reconvla-k2-spatial-s42\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python src/evaluate.py --mode reconvla --K 10 --suite spatial --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:1\", \"pid\": 34387}}, \"eval-supp-k2mean-object-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:38:54.570Z\", \"updated_at\": \"2026-05-23T08:19:19.844Z\", \"hypothesis\": \"K=2 mean baseline multi-seed on Object seed43. Isolates multi-sample averaging effect from CRM correction. Second seed for 3-seed mean±std on K=2 mean baseline.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite object --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"cuda:2\", \"pid\": 16441}}, \"eval-supp-k2mean-spatial-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:38:51.694Z\", \"updated_at\": \"2026-05-23T08:19:14.264Z\", \"hypothesis\": \"K=2 mean baseline multi-seed on Spatial seed43. Isolates multi-sample averaging effect from CRM correction. Second seed for 3-seed mean±std on K=2 mean baseline.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite spatial --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:0\", \"pid\": 16439}}}, \"count\": 10, \"total\": 10, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.5815}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-23T10:13:26.149Z_

<details><summary>↩ Tool result · `toolu_01PstMLydzfkNaiHzt8wtS4w`</summary>

```text
Error: result (92,054 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4294b235-1b87-40b4-afe2-9e7ed46ec777/tool-results/mcp-agent-ml-research-read_registry-1779531206092.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4294b235-1b87-40b4-afe2-9e7ed46ec777/tool-results/mcp-agent-ml-research-read_registry-1779531206092.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4294b235-1b87-40b4-afe2-9e7ed46ec777/tool-results/mcp-agent-ml-research-read_registry-1779531206092.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "dbaaf43d-6519-49ff-8219-fe5c2014482b",
  "tool_use_result": {
    "content": "Error: result (92,054 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4294b235-1b87-40b4-afe2-9e7ed46ec777/tool-results/mcp-agent-ml-research-read_registry-1779531206092.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4294b235-1b87-40b4-afe2-9e7ed46ec777/tool-results/mcp-agent-ml-research-read_registry-1779531206092.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4294b235-1b87-40b4-afe2-9e7ed46ec777/tool-results/mcp-agent-ml-research-read_registry-1779531206092.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-crm-norm005-goal-s44\": {\"status\": \"PREPARING\", \"retry_count\": 1, \"created_at\": \"2026-05-23T09:24:35.031Z\", \"updated_at\": \"2026-05-23T10:13:09.671Z\", \"hypothesis\": \"CRM norm=0.05 on Goal seed44. Goal VLA-only = 97.5-98%. s42=85.5% (-12pp). Third seed for 3-seed mean±std on Goal CRM degradation magnitude.\", \"completed_at\": \"2026-05-23T09:54:59.067Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:56:44.431Z\", \"updated_at\": \"2026-05-23T09:57:37.568Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt --benchmark long --seed 42 --n_rollouts 20 --max_correction_norm 0.05\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"712369\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s42.log\", \"submitted_at\": \"2026-05-23T09:57:35.905Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"CRM always-on norm=0.05 on LIBERO-Long seed42 using 4-suite CRM checkpoint. CRM improved Spatial (79.8% vs 78.5% VLA-only) but hurt Goal (-12pp). Tests CRM effect on challenging long-horizon tasks.\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:56:38.730Z\", \"updated_at\": \"2026-05-23T09:57:30.694Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"711761\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-adapt-tau025-s42.log\", \"submitted_at\": \"2026-05-23T09:57:28.057Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Adaptive conformal CRM tau=0.25 on LIBERO-Long seed42 using 4-suite CRM checkpoint. Adaptive method achieved best Spatial results (82.0% vs 78.5% VLA-only). Tests if selective CRM application benefits long-horizon tasks.\"}, \"eval-supp-long-reconvla-s42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:56:33.117Z\", \"updated_at\": \"2026-05-23T09:57:21.640Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --K 10 --benchmark long --seed 42 --n_rollouts 20\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"711470\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s42.log\", \"submitted_at\": \"2026-05-23T09:57:18.522Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Reconvla K=10 argmin on LIBERO-Long seed42. Tests if reconstruction-based action selection benefits long-horizon tasks. Reconvla achieved 80% on Spatial (vs 78.5% VLA-only) and 79% on Object (vs 77.8% VLA-only).\"}, \"eval-pi05-vla-only-long-seed42-r4-std\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:13:45.727Z\", \"updated_at\": \"2026-05-22T16:17:13.985Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-22T16:13:48.238Z\"}, \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:14:08.464410+00:00\"}]}, \"notes\": \"Phantom experiment entry — never submitted (status was PREPARING, no spec/server/command). Cron false alarm. Real experiment is eval-pi05-vla-only-long-seed42-r4 (RUNNING on bjb2-40593).\"}, \"precompute-smolvla-goal-k10\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:48:27.660Z\", \"updated_at\": \"2026-05-22T15:48:27.660Z\", \"spec\": {\"command\": \"bash -c \\\"while kill -0 249393 2>/dev/null; do sleep 10; done; sleep 5; cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/lerobot_precompute.py --benchmark goal --K 10 --cache_dir /root/autodl-tmp/crm_cache_smolvla_k10/ 2>&1 | tee /root/runs/acr-vla-conformal-refinement/precompute-smolvla-goal.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"299301\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-smolvla-goal-k10.log\", \"submitted_at\": \"2026-05-22T15:48:21.784Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-smolvla-spatial-k10\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:48:13.209Z\", \"updated_at\": \"2026-05-22T15:48:13.210Z\", \"spec\": {\"command\": \"bash -c \\\"while kill -0 249256 2>/dev/null; do sleep 10; done; sleep 5; cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/lerobot_precompute.py --benchmark spatial --K 10 --cache_dir /root/autodl-tmp/crm_cache_smolvla_k10/ 2>&1 | tee /root/runs/acr-vla-conformal-refinement/precompute-smolvla-spatial.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"299065\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-smolvla-spatial-k10.log\", \"submitted_at\": \"2026-05-22T15:48:02.014Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-smolvla-object-k10\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:47:41.690Z\", \"updated_at\": \"2026-05-22T15:47:41.690Z\", \"spec\": {\"command\": \"bash -c \\\"while kill -0 249181 2>/dev/null; do sleep 10; done; sleep 5; cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/lerobot_precompute.py --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_smolvla_k10/ 2>&1 | tee /root/runs/acr-vla-conformal-refinement/precompute-smolvla-object.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"298669\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-smolvla-object-k10.log\", \"submitted_at\": \"2026-05-22T15:47:29.485Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-long-seed2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:19:49.215Z\", \"updated_at\": \"2026-05-22T14:19:49.215Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python src/evaluate.py --mode vla_only --benchmark long --seed 2 --n_rollouts 10 --output_file logs/eval_long_vla_only_seed2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"233564\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-long-seed2.log\", \"submitted_at\": \"2026-05-22T14:19:47.701Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-long-seed1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:19:43.184Z\", \"updated_at\": \"2026-05-22T14:19:43.184Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python src/evaluate.py --mode vla_only --benchmark long --seed 1 --n_rollouts 10 --output_file logs/eval_long_vla_only_seed1.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"232884\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-long-seed1.log\", \"submitted_at\": \"2026-05-22T14:19:41.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-long-seed0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:19:38.265Z\", \"updated_at\": \"2026-05-22T14:19:38.265Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python src/evaluate.py --mode vla_only --benchmark long --seed 0 --n_rollouts 10 --output_file logs/eval_long_vla_only_seed0.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"232609\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-long-seed0.log\", \"submitted_at\": \"2026-05-22T14:19:36.630Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-long-bjb1-18228\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:00:18.250Z\", \"updated_at\": \"2026-05-22T09:00:18.250Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python src/train_crm.py --precompute --benchmark long --K 10 --model pi05 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --shard_id 0 --num_shards 1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"883206\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-long-bjb1-18228.log\", \"submitted_at\": \"2026-05-22T09:00:16.701Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-goal-bjb2-28827-s2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:03:27.743Z\", \"updated_at\": \"2026-05-22T08:03:27.743Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python src/train_crm.py --precompute --benchmark goal --K 10 --model pi05 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --shard_id 2 --num_shards 3\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"206549\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-goal-bjb2-28827-s2.log\", \"submitted_at\": \"2026-05-22T08:03:26.321Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-goal-bjb2-28827-s1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:03:23.271Z\", \"updated_at\": \"2026-05-22T08:03:23.271Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python src/train_crm.py --precompute --benchmark goal --K 10 --model pi05 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --shard_id 1 --num_shards 3\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"206270\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-goal-bjb2-28827-s1.log\", \"submitted_at\": \"2026-05-22T08:03:21.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-goal-bjb2-28827-s0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:03:18.740Z\", \"updated_at\": \"2026-05-22T08:03:18.741Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python src/train_crm.py --precompute --benchmark goal --K 10 --model pi05 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --shard_id 0 --num_shards 3\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"206123\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-goal-bjb2-28827-s0.log\", \"submitted_at\": \"2026-05-22T08:03:17.284Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-smolvla-crm-long-seed44\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:10:41.746Z\", \"updated_at\": \"2026-05-22T05:10:41.746Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py --mode acr_vla --benchmark long --n_rollouts 20 --seed 44 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"170200\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-smolvla-crm-long-seed44.log\", \"submitted_at\": \"2026-05-22T05:10:40.364Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-smolvla-crm-long-seed43\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:10:32.722Z\", \"updated_at\": \"2026-05-22T05:10:32.722Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py --mode acr_vla --benchmark long --n_rollouts 20 --seed 43 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"169645\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-smolvla-crm-long-seed43.log\", \"submitted_at\": \"2026-05-22T05:10:31.278Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"crm-pipeline-auto\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T16:37:34.472Z\", \"updated_at\": \"2026-05-21T16:37:34.472Z\", \"spec\": {\"command\": \"bash -c \\\"\\nset -e\\n\\necho '[pipeline] Starting auto CRM pipeline monitor at $(date)'\\necho '[pipeline] Will poll precompute progress every 5 min, then auto-execute merge + training'\\n\\n# === PHASE 1: Wait for all precompute to finish ===\\necho '[pipeline] Phase 1: Monitoring precompute completion...'\\n\\nwhile true; do\\n    # Check bjb1-32546 (Object s1-s9)\\n    OBJ_PROCS=\\\\$(ssh bjb1-32546 'ps aux | grep train_crm | grep precompute | grep -v grep | wc -l' 2>/dev/null || echo 0)\\n    # Check bjb2-40593 (Object s0)  \\n    OBJ0_PROCS=\\\\$(ssh bjb2-40593 'ps aux | grep train_crm | grep precompute | grep -v grep | wc -l' 2>/dev/null || echo 0)\\n    # Check bjb2-28827 (Spatial s0-s5)\\n    SPA_PROCS=\\\\$(ssh bjb2-28827 'ps aux | grep train_crm | grep precompute | grep -v grep | wc -l' 2>/dev/null || echo 0)\\n    # Check local (Spatial s6)\\n    SPA6_PROCS=\\\\$(ps aux | grep train_crm | grep precompute | grep -v grep | wc -l)\\n    \\n    TOTAL=\\\\$((OBJ_PROCS + OBJ0_PROCS + SPA_PROCS + SPA6_PROCS))\\n    echo \\\\\\\"[pipeline] \\\\$(date): precompute processes remaining: bjb1-32546=\\\\${OBJ_PROCS} bjb2-40593=\\\\${OBJ0_PROCS} bjb2-28827=\\\\${SPA_PROCS} local=\\\\${SPA6_PROCS} total=\\\\${TOTAL}\\\\\\\"\\n    \\n    if [ \\\\\\\"\\\\$TOTAL\\\\\\\" -eq 0 ]; then\\n        echo '[pipeline] All precompute processes finished!'\\n        break\\n    fi\\n    \\n    sleep 300\\ndone\\n\\n# === PHASE 2: Clean old partials on bjb1-18228 ===\\necho '[pipeline] Phase 2: Cleaning old object partials on bjb1-18228...'\\nrm -f /root/autodl-tmp/crm_cache_pi05/object/partial_s*.pt\\nrm -f /root/autodl-tmp/crm_cache_pi05/object/obs_features.pt /root/autodl-tmp/crm_cache_pi05/object/k_samples.pt /root/autodl-tmp/crm_cache_pi05/object/expert_actions.pt /root/autodl-tmp/crm_cache_pi05/object/manifest.json\\necho '[pipeline] Old partials cleaned'\\n\\n# === PHASE 3: rsync all shard caches to bjb1-18228 ===\\necho '[pipeline] Phase 3: Rsyncing all shard caches...'\\n\\n# Object shard 0 from bjb2-40593\\necho '[pipeline] rsync Object s0 from bjb2-40593...'\\nrsync -av bjb2-40593:/root/autodl-tmp/crm_cache_pi05/object/partial_s0_*.pt /root/autodl-tmp/crm_cache_pi05/object/\\necho '[pipeline] Object s0 done'\\n\\n# Object shards 1-9 from bjb1-32546\\necho '[pipeline] rsync Object s1-9 from bjb1-32546...'\\nrsync -av bjb1-32546:/root/autodl-tmp/crm_cache_pi05/object/partial_s*.pt /root/autodl-tmp/crm_cache_pi05/object/\\necho '[pipeline] Object s1-9 done'\\n\\n# Spatial shards 0-5 from bjb2-28827\\necho '[pipeline] rsync Spatial s0-5 from bjb2-28827...'\\nrsync -av bjb2-28827:/root/autodl-tmp/crm_cache_pi05/spatial/partial_s*.pt /root/autodl-tmp/crm_cache_pi05/spatial/\\necho '[pipeline] Spatial s0-5 done'\\n# Spatial s6 already local\\n\\necho '[pipeline] rsync complete. File counts:'\\nls /root/autodl-tmp/crm_cache_pi05/object/partial_s*.pt 2>/dev/null | wc -l\\nls /root/autodl-tmp/crm_cache_pi05/spatial/partial_s*.pt 2>/dev/null | wc -l\\n\\n# === PHASE 4: Merge ===\\necho '[pipeline] Phase 4: Merge...'\\ncd /root/acr-vla-conformal-refinement\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\n\\n# Dry-run first\\necho '[pipeline] Object merge dry-run...'\\npython scripts/merge_precompute_cache.py --cache_dir /root/autodl-tmp/crm_cache_pi05/object --num_shards 10 --dry_run\\n\\necho '[pipeline] Spatial merge dry-run...'\\npython scripts/merge_precompute_cache.py --cache_dir /root/autodl-tmp/crm_cache_pi05/spatial --num_shards 7 --dry_run\\n\\n# Actual merge\\necho '[pipeline] Object merge...'\\npython scripts/merge_precompute_cache.py --cache_dir /root/autodl-tmp/crm_cache_pi05/object --num_shards 10\\n\\necho '[pipeline] Spatial merge...'\\npython scripts/merge_precompute_cache.py --cache_dir /root/autodl-tmp/crm_cache_pi05/spatial --num_shards 7\\n\\n# Verify merge output\\necho '[pipeline] Merge verification:'\\nls -la /root/autodl-tmp/crm_cache_pi05/object/{obs_features.pt,k_samples.pt,expert_actions.pt,manifest.json}\\nls -la /root/autodl-tmp/crm_cache_pi05/spatial/{obs_features.pt,k_samples.pt,expert_actions.pt,manifest.json}\\npython -c \\\\\\\"import torch; o=torch.load('/root/autodl-tmp/crm_cache_pi05/object/obs_features.pt',weights_only=True); print('Object obs:', o.shape)\\\\\\\"\\npython -c \\\\\\\"import torch; s=torch.load('/root/autodl-tmp/crm_cache_pi05/spatial/obs_features.pt',weights_only=True); print('Spatial obs:', s.shape)\\\\\\\"\\n\\necho '[pipeline] Phase 4 complete!'\\necho '[pipeline] CRM training will be started by separate jobs on cuda:0 and cuda:1'\\necho '[pipeline] DONE at $(date)'\\n\\\"\\n\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"790737\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-pipeline-auto.log\", \"submitted_at\": \"2026-05-21T16:37:33.143Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s6-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T15:04:33.582Z\", \"updated_at\": \"2026-05-21T15:04:33.582Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 6 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"182283\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s6-r2.log\", \"submitted_at\": \"2026-05-21T15:04:31.010Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s9-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:19:39.622Z\", \"updated_at\": \"2026-05-21T14:19:39.622Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 9 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"783655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s9-r2.log\", \"submitted_at\": \"2026-05-21T14:19:38.235Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s8-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:19:35.288Z\", \"updated_at\": \"2026-05-21T14:19:35.288Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 8 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"783507\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s8-r2.log\", \"submitted_at\": \"2026-05-21T14:19:33.986Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s7-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:19:30.950Z\", \"updated_at\": \"2026-05-21T14:19:30.950Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 7 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"783362\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s7-r2.log\", \"submitted_at\": \"2026-05-21T14:19:29.613Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s0-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:19:26.580Z\", \"updated_at\": \"2026-05-21T14:19:26.580Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 0 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"878484\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s0-r2.log\", \"submitted_at\": \"2026-05-21T14:19:25.216Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s5-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:19:22.348Z\", \"updated_at\": \"2026-05-21T14:19:22.348Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 5 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"179280\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s5-r2.log\", \"submitted_at\": \"2026-05-21T14:19:20.929Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s4-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:19:17.949Z\", \"updated_at\": \"2026-05-21T14:19:17.949Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 4 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"178931\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s4-r2.log\", \"submitted_at\": \"2026-05-21T14:19:16.602Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s3-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:19:13.168Z\", \"updated_at\": \"2026-05-21T14:19:13.169Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 3 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"178652\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s3-r2.log\", \"submitted_at\": \"2026-05-21T14:19:11.761Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s2-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:19:08.830Z\", \"updated_at\": \"2026-05-21T14:19:08.830Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 2 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"178505\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s2-r2.log\", \"submitted_at\": \"2026-05-21T14:19:07.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s1-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:19:04.514Z\", \"updated_at\": \"2026-05-21T14:19:04.514Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 1 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"178356\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s1-r2.log\", \"submitted_at\": \"2026-05-21T14:19:03.162Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s9-fix\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:05:27.170Z\", \"updated_at\": \"2026-05-21T14:05:27.170Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 9 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --save_every 100\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"176442\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s9-fix.log\", \"submitted_at\": \"2026-05-21T14:05:25.745Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s8-fix\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:05:22.511Z\", \"updated_at\": \"2026-05-21T14:05:22.511Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 8 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --save_every 100\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"176097\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s8-fix.log\", \"submitted_at\": \"2026-05-21T14:05:20.949Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s7-fix\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:05:17.907Z\", \"updated_at\": \"2026-05-21T14:05:17.907Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 7 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --save_every 100\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"175818\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s7-fix.log\", \"submitted_at\": \"2026-05-21T14:05:16.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s6-fix\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:05:13.392Z\", \"updated_at\": \"2026-05-21T14:05:13.392Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 6 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --save_every 100\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"175671\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s6-fix.log\", \"submitted_at\": \"2026-05-21T14:05:11.879Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-s5-fix\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:05:08.790Z\", \"updated_at\": \"2026-05-21T14:05:08.790Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 5 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/ --save_every 100\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"175522\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-s5-fix.log\", \"submitted_at\": \"2026-05-21T14:05:07.337Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-shard9\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:50:29.762Z\", \"updated_at\": \"2026-05-21T13:50:29.762Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 9 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"173849\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-shard9.log\", \"submitted_at\": \"2026-05-21T13:50:28.123Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-shard8\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:50:25.069Z\", \"updated_at\": \"2026-05-21T13:50:25.069Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 8 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"173507\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-shard8.log\", \"submitted_at\": \"2026-05-21T13:50:23.574Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-shard7\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:50:20.551Z\", \"updated_at\": \"2026-05-21T13:50:20.551Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 7 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"173224\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-shard7.log\", \"submitted_at\": \"2026-05-21T13:50:19.119Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-shard6\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:50:15.986Z\", \"updated_at\": \"2026-05-21T13:50:15.986Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 6 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"173077\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-shard6.log\", \"submitted_at\": \"2026-05-21T13:50:14.476Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-obj-shard5\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:50:11.352Z\", \"updated_at\": \"2026-05-21T13:50:11.353Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 5 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"172930\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-obj-shard5.log\", \"submitted_at\": \"2026-05-21T13:50:09.940Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard6\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:46:14.580Z\", \"updated_at\": \"2026-05-21T13:46:14.580Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 6 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"781275\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard6.log\", \"submitted_at\": \"2026-05-21T13:46:12.692Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard5\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:46:08.912Z\", \"updated_at\": \"2026-05-21T13:46:08.912Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 5 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"101845\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard5.log\", \"submitted_at\": \"2026-05-21T13:46:07.228Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:46:03.897Z\", \"updated_at\": \"2026-05-21T13:46:03.897Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 4 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"101566\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard4.log\", \"submitted_at\": \"2026-05-21T13:46:02.116Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:45:58.808Z\", \"updated_at\": \"2026-05-21T13:45:58.808Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 3 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"101227\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard3.log\", \"submitted_at\": \"2026-05-21T13:45:55.961Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:45:51.058Z\", \"updated_at\": \"2026-05-21T13:45:51.058Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 2 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"100880\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard2.log\", \"submitted_at\": \"2026-05-21T13:45:49.296Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:45:45.565Z\", \"updated_at\": \"2026-05-21T13:45:45.566Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 1 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"100538\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard1.log\", \"submitted_at\": \"2026-05-21T13:45:43.800Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-spatial-shard0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:45:40.280Z\", \"updated_at\": \"2026-05-21T13:45:40.280Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark spatial --shard_id 0 --num_shards 7 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"100391\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard0.log\", \"submitted_at\": \"2026-05-21T13:45:37.963Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:13:53.765Z\", \"updated_at\": \"2026-05-21T13:44:35.499Z\", \"hypothesis\": \"π0.5 CRM feature precompute (shard 0/6). Extract 2048D obs features + K=10 action samples from frozen π0.5 on LIBERO Object+Spatial demos for CRM training.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 0 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"876712\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard0.log\", \"submitted_at\": \"2026-05-21T13:44:33.853Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard9\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:19:30.227Z\", \"updated_at\": \"2026-05-21T13:42:56.355Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 9 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"780274\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard9.log\", \"submitted_at\": \"2026-05-21T13:42:54.650Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 CRM feature precompute (shard 9/10). Extract 2048D obs features + K=10 action samples from frozen π0.5 on LIBERO Object+Spatial demos for CRM training.\"}, \"precompute-pi05-shard8\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:19:22.125Z\", \"updated_at\": \"2026-05-21T13:42:50.972Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 8 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"779995\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard8.log\", \"submitted_at\": \"2026-05-21T13:42:49.363Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 CRM feature precompute (shard 8/10). Extract 2048D obs features + K=10 action samples from frozen π0.5 on LIBERO Object+Spatial demos for CRM training.\"}, \"precompute-pi05-shard7\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:19:03.096Z\", \"updated_at\": \"2026-05-21T13:42:45.877Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 7 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"779846\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard7.log\", \"submitted_at\": \"2026-05-21T13:42:44.324Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 CRM feature precompute (shard 7/10). Extract 2048D obs features + K=10 action samples from frozen π0.5 on LIBERO Object+Spatial demos for CRM training.\"}, \"precompute-pi05-shard6\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:18:56.927Z\", \"updated_at\": \"2026-05-21T13:42:40.538Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 6 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"171752\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard6.log\", \"submitted_at\": \"2026-05-21T13:42:38.931Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 CRM feature precompute (shard 6/10). Extract 2048D obs features + K=10 action samples from frozen π0.5 on LIBERO Object+Spatial demos for CRM training.\"}, \"precompute-pi05-shard5\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:15:49.135Z\", \"updated_at\": \"2026-05-21T13:42:35.528Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 5 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"171537\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard5.log\", \"submitted_at\": \"2026-05-21T13:42:33.909Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:15:32.187Z\", \"updated_at\": \"2026-05-21T13:42:30.590Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 4 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"171195\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard4.log\", \"submitted_at\": \"2026-05-21T13:42:28.892Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:15:13.099Z\", \"updated_at\": \"2026-05-21T13:42:24.367Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 3 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"170840\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard3.log\", \"submitted_at\": \"2026-05-21T13:42:22.597Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:14:59.128Z\", \"updated_at\": \"2026-05-21T13:42:18.667Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 2 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"170561\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard2.log\", \"submitted_at\": \"2026-05-21T13:42:16.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"precompute-pi05-shard1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:14:44.417Z\", \"updated_at\": \"2026-05-21T13:42:13.102Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCHDYNAMO_DISABLE=1 python -u src/train_crm.py --model pi05 --precompute --benchmark object --shard_id 1 --num_shards 10 --cache_dir /root/autodl-tmp/crm_cache_pi05/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"170414\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-pi05-shard1.log\", \"submitted_at\": \"2026-05-21T13:42:11.409Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:30:28.663Z\", \"updated_at\": \"2026-05-21T08:02:33.602Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→MEAN_STD normalization mismatch that caused 0% SR in r1.\", \"parent\": \"eval-pi05-baseline-object-seed42\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python3 -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --K 10 --output_file logs/eval_pi05_baseline_object_seed42_r2.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"811001\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-baseline-object-seed42-r2.log\", \"submitted_at\": \"2026-05-21T03:30:45.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"KILLED (旧策略 action[0] only). 后续修复历程: (1) action queue fix → bbq_sauce 0/5 (2) vision tower 确认正确加载 (3) 图像 180° 翻转修复 (torch.flip dims=[2,3]) → **Quick verify SR=72%** 修复成功！根因: 官方 lerobot 对图像做 NCHW 180° 旋转，我们的 wrapper 缺失此步骤。\", \"reproduce\": {\"finished_at\": \"2026-05-21T04:53:21.758Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T04:53:36.626571+00:00\"}]}, \"conclusion\": \"killed\"}, \"eval-random-selection-object-seed42-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:34:04.735Z\", \"updated_at\": \"2026-05-21T04:34:32.245Z\", \"hypothesis\": \"Random Selection (K=10, uniform pick) on LIBERO-Object seed42. Isolates conformal ranking contribution: if Random ≈ VLA-only, then CRM's advantage comes from learned correction not just sampling diversity.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode random_selection --benchmark object --K 10 --seed 42 --n_rollouts 10 --output_file logs/eval_random_selection_object_seed42.json 2>&1 | tee logs/eval-random-selection-object-seed42.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"852344\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed42-r3.log\", \"submitted_at\": \"2026-05-21T04:34:30.827Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T01:18:47.309Z\", \"updated_at\": \"2026-05-21T04:32:53.123Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed50. 补齐 Spatial baseline 样本量，与 CRM Spatial 配对统计检验。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 50 --n_rollouts 10 --output_file logs/eval_vla_only_spatial_seed50.json 2>&1 | tee logs/eval-vla-only-spatial-seed50.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"850105\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed50.log\", \"submitted_at\": \"2026-05-21T04:32:49.401Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:42:58.271Z\", \"updated_at\": \"2026-05-21T04:32:42.275Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark spatial --K 10 --seed 50 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed50.json 2>&1 | tee logs/eval-crm-spatial-k10-seed50.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"849760\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-spatial-k10-seed50.log\", \"submitted_at\": \"2026-05-21T04:32:38.353Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed50. 补齐 Spatial CRM 样本量 (n→7+)，增强 ID suite 上 CRM correction 效果的统计可靠性。\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:42:47.989Z\", \"updated_at\": \"2026-05-21T04:32:32.158Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark spatial --K 10 --seed 49 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed49.json 2>&1 | tee logs/eval-crm-spatial-k10-seed49.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"11357\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-spatial-k10-seed49.log\", \"submitted_at\": \"2026-05-21T04:32:28.560Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed49. 补齐 Spatial CRM 样本量 (n→6+)，增强 ID suite 上 CRM correction 效果的统计可靠性。\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:27:30.715Z\", \"updated_at\": \"2026-05-21T04:32:24.008Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed44. K=20 第三个 seed，n=3 可报告 error bars，确认 K-value diminishing returns。\", \"conclusion\": \"killed\", \"failure_reason\": \"Director DROP 决策: K=20 代码/参数不支持。从未部署。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed44.json 2>&1 | tee logs/eval-obs-only-object-norm02-k20-seed44.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"11078\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed44.log\", \"submitted_at\": \"2026-05-21T04:32:21.220Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:27:28.230Z\", \"updated_at\": \"2026-05-21T04:32:17.159Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed43. K=20 第二个 seed，与 K=10 seed43 配对，增强 K-value curve K=20 端的统计可靠性。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed43.json 2>&1 | tee logs/eval-obs-only-object-norm02-k20-seed43.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"10781\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed43.log\", \"submitted_at\": \"2026-05-21T04:32:14.520Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\", \"failure_reason\": \"Director DROP 决策: K=20 代码/参数不支持，三次部署失败。K-value curve 已有 K=1/5/10 三点。\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"PREPARING\", \"retry_count\": 2, \"created_at\": \"2026-05-17T13:34:42.612Z\", \"updated_at\": \"2026-05-21T04:32:11.044Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed42. 扩展 K-value curve 到 K=20，验证收益曲线在 K=10→K=20 段是否趋平（预期 ≤+1pp over K=10 的 17.6%）。用 K=10 训练的 CRM 模型，eval 时生成 20 个 VLA 样本。\", \"reproduce\": {\"finished_at\": \"2026-05-17T18:33:08.015Z\"}, \"failure_reason\": \"Director DROP 决策: K=20 代码/参数不支持，三次部署失败。K-value curve 已有 K=1/5/10 三点，收益递减模式清晰。DDL 10天不值得 debug。\", \"completed_at\": \"2026-05-17T18:33:10.102Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:33:36.294183+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 42 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed42.json 2>&1 | tee logs/eval-obs-only-object-norm02-k20-seed42.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"10438\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed42.log\", \"submitted_at\": \"2026-05-21T04:32:09.740Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed76\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:57:48.001Z\", \"updated_at\": \"2026-05-21T03:33:43.610Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.03 has fewest seeds, expanding coverage for statistical confidence.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 76 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed76.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"825126\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed76.log\", \"submitted_at\": \"2026-05-21T03:33:41.212Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm01-seed77\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:15:13.220Z\", \"updated_at\": \"2026-05-21T03:17:06.237Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.1 补种.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 77 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed77.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"815988\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed77.log\", \"submitted_at\": \"2026-05-21T03:17:04.908Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm01-seed76\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:15:10.875Z\", \"updated_at\": \"2026-05-21T03:17:01.964Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.1 补种.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 76 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_object_norm01_seed76.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"815198\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed76.log\", \"submitted_at\": \"2026-05-21T03:16:59.361Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm005-seed77\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:57:21.662Z\", \"updated_at\": \"2026-05-21T03:16:58.507Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.05 outlier verification.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 77 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed77.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"982671\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed77.log\", \"submitted_at\": \"2026-05-21T03:16:55.416Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm003-seed63-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:15:08.600Z\", \"updated_at\": \"2026-05-21T03:16:54.862Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed63 r3. Redo of killed seed63-r2 (M036 dual process). Norm sweep ε=0.03 seed balance.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 63 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed63_r3.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"814859\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed63-r3.log\", \"submitted_at\": \"2026-05-21T03:16:50.645Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm005-seed76\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:14:58.578Z\", \"updated_at\": \"2026-05-21T03:16:49.849Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.05 has outlier seeds, expanding for variance verification.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 76 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed76.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"981080\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed76.log\", \"submitted_at\": \"2026-05-21T03:16:43.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm003-seed62-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:15:06.396Z\", \"updated_at\": \"2026-05-21T03:16:44.624Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed62 r3. Redo of killed seed62-r2 (M036 dual process). Norm sweep ε=0.03 seed balance.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 62 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed62_r3.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"814262\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed62-r3.log\", \"submitted_at\": \"2026-05-21T03:16:40.387Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm003-seed78\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:14:54.184Z\", \"updated_at\": \"2026-05-21T03:16:34.818Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed78. Norm sweep: ε=0.03 has fewest seeds, expanding coverage.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 78 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed78.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"980035\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed78.log\", \"submitted_at\": \"2026-05-21T03:16:31.286Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-object-norm003-seed77\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:14:50.541Z\", \"updated_at\": \"2026-05-21T03:16:26.327Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.03 has fewest seeds, expanding coverage.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 77 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed77.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"979376\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed77.log\", \"submitted_at\": \"2026-05-21T03:16:22.477Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-obs-only-goal-norm02-seed53\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:07:47.325Z\", \"updated_at\": \"2026-05-20T13:08:32.542Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Goal seed53. Additional OOD Goal seed for multi-seed robustness.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 53 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_goal_norm02_seed53.json 2>&1 | tee logs/eval-obs-only-goal-norm02-seed53.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"424172\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-goal-norm02-seed53.log\", \"submitted_at\": \"2026-05-20T13:08:31.497Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-long-seed54\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:16:25.982Z\", \"updated_at\": \"2026-05-20T05:59:13.545Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed54. 补齐 Long baseline 样本量。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark long --seed 54 --n_rollouts 10 --K 1 --output_file logs/eval_long_vla_only_seed54.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"281225\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-long-seed54.log\", \"submitted_at\": \"2026-05-20T05:59:11.992Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-crm-long-seed54\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:39:32.457Z\", \"updated_at\": \"2026-05-20T05:39:32.457Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark long --seed 54 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --n_rollouts 10 --output_file logs/eval_long_obs_only_norm02_seed54.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"266970\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-long-seed54.log\", \"submitted_at\": \"2026-05-20T05:39:31.530Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-spatial-seed54\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:39:29.096Z\", \"updated_at\": \"2026-05-20T05:39:29.096Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 54 --n_rollouts 10 --K 1 --output_file logs/eval_spatial_vla_only_seed54.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"266698\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed54.log\", \"submitted_at\": \"2026-05-20T05:39:28.178Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-crm-long-seed53\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:39:25.536Z\", \"updated_at\": \"2026-05-20T05:39:25.536Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark long --seed 53 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --n_rollouts 10 --output_file logs/eval_long_obs_only_norm02_seed53.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"272966\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-long-seed53.log\", \"submitted_at\": \"2026-05-20T05:39:24.453Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-spatial-seed53\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:39:21.611Z\", \"updated_at\": \"2026-05-20T05:39:21.611Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 53 --n_rollouts 10 --K 1 --output_file logs/eval_spatial_vla_only_seed53.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"272634\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed53.log\", \"submitted_at\": \"2026-05-20T05:39:20.683Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-spatial-seed52\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:39:11.774Z\", \"updated_at\": \"2026-05-20T05:39:11.774Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 52 --n_rollouts 10 --K 1 --output_file logs/eval_spatial_vla_only_seed52.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"272102\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed52.log\", \"submitted_at\": \"2026-05-20T05:39:10.829Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-crm-goal-seed50\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:39:07.990Z\", \"updated_at\": \"2026-05-20T05:39:07.990Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 50 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --n_rollouts 10 --output_file logs/eval_goal_obs_only_norm02_seed50.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"205462\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-goal-seed50.log\", \"submitted_at\": \"2026-05-20T05:39:07.010Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-crm-goal-seed49\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:39:04.130Z\", \"updated_at\": \"2026-05-20T05:39:04.130Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 49 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --n_rollouts 10 --output_file logs/eval_goal_obs_only_norm02_seed49.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"205187\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-goal-seed49.log\", \"submitted_at\": \"2026-05-20T05:39:03.140Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-crm-long-seed52\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:39:00.913Z\", \"updated_at\": \"2026-05-20T05:39:00.914Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark long --seed 52 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --n_rollouts 10 --output_file logs/eval_long_obs_only_norm02_seed52.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"204912\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-long-seed52.log\", \"submitted_at\": \"2026-05-20T05:38:59.719Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-goal-seed52\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:16:27.646Z\", \"updated_at\": \"2026-05-20T05:17:00.091Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed52. 补齐 Goal baseline 样本量 (n→9)。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark goal --seed 52 --n_rollouts 10 --K 1 --output_file logs/eval_goal_vla_only_seed52.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"255472\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-goal-seed52.log\", \"submitted_at\": \"2026-05-20T05:16:59.102Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-long-seed53\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:16:24.338Z\", \"updated_at\": \"2026-05-20T05:16:52.571Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed53. 补齐 Long baseline 样本量，与 CRM-Long 配对。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark long --seed 53 --n_rollouts 10 --K 1 --output_file logs/eval_long_vla_only_seed53.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"254717\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-long-seed53.log\", \"submitted_at\": \"2026-05-20T05:16:51.670Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-crm-long-seed51\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:16:22.723Z\", \"updated_at\": \"2026-05-20T05:16:49.496Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Long seed51. 补齐 Long CRM OOD 样本量 (n→10)，增强 +3pp 效果的统计显著性。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark long --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_long_obs_only_norm02_seed51.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"254508\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-long-seed51.log\", \"submitted_at\": \"2026-05-20T05:16:48.525Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-goal-seed50\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:16:19.471Z\", \"updated_at\": \"2026-05-20T05:16:42.496Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed50. 补齐 Goal baseline 样本量 (n→7)，与 CRM-Goal (n=7) 配对。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark goal --seed 50 --n_rollouts 10 --K 1 --output_file logs/eval_goal_vla_only_seed50.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"197007\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-goal-seed50.log\", \"submitted_at\": \"2026-05-20T05:16:40.861Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-crm-long-seed49\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:43:08.930Z\", \"updated_at\": \"2026-05-20T05:15:52.486Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark long --n_rollouts 10 --seed 49 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_long_obs_only_norm02_seed49.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"201115\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-long-seed49.log\", \"submitted_at\": \"2026-05-20T02:43:07.765Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Long seed49. 补齐 Long CRM OOD 样本量 (n→8)，验证 CRM 在 OOD Long 上的效果稳定性。\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-crm-long-seed48\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:43:05.584Z\", \"updated_at\": \"2026-05-20T05:15:50.831Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark long --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_long_obs_only_norm02_seed48.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"200523\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-long-seed48.log\", \"submitted_at\": \"2026-05-20T02:43:04.664Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Long seed48. 补齐 Long CRM OOD 样本量 (n→7)，验证 CRM 在 OOD Long 上的 +5.3pp 效果是否稳定或集中于单 task。\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-crm-goal-seed48\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:57:44.184Z\", \"updated_at\": \"2026-05-20T05:15:47.607Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_goal_obs_only_norm02_seed48.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"145395\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-goal-seed48.log\", \"submitted_at\": \"2026-05-20T02:57:43.269Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Goal seed48. Goal OOD 补样本量 (n→6)，验证 CRM 在 cross-suite OOD 上的效果。seed46=72% 推高均值，看是否一致。\", \"metrics\": {\"success_rate\": 0.68, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-crm-goal-seed47\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:54:07.709Z\", \"updated_at\": \"2026-05-20T04:33:38.995Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark goal --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_goal_obs_only_norm02_seed47.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"137169\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-goal-seed47.log\", \"submitted_at\": \"2026-05-20T02:54:06.768Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Goal seed47. Goal OOD 补样本量 (n→6)，增强 cross-suite OOD 统计可靠性。\", \"metrics\": {\"success_rate\": 0.69, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-crm-spatial-seed48\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T01:20:10.184Z\", \"updated_at\": \"2026-05-20T04:13:53.186Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 48 --K 10 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --n_rollouts 10 --output_file logs/eval_spatial_obs_only_norm02_seed48.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"171138\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-spatial-seed48.log\", \"submitted_at\": \"2026-05-20T01:20:07.619Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed51\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:12:22.300Z\", \"updated_at\": \"2026-05-20T03:12:40.851Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 51 --output_file logs/eval_spatial_vla_only_seed51.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"216392\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed51.log\", \"submitted_at\": \"2026-05-20T03:12:21.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed51. 补齐 Spatial baseline 样本量，与 CRM-Spatial 配对检验。\"}, \"eval-vla-only-object-seed51\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:43:01.821Z\", \"updated_at\": \"2026-05-20T02:43:30.806Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 51 --output_file logs/eval_object_vla_only_seed51.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"200247\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed51.log\", \"submitted_at\": \"2026-05-20T02:43:00.488Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed51. 补齐 Object VLA-only 样本量 (n→8+)，增强主 ID benchmark baseline 统计可靠性。\"}, \"eval-vla-only-long-seed49\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:42:51.266Z\", \"updated_at\": \"2026-05-20T02:43:21.463Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark long --n_rollouts 10 --seed 49 --output_file logs/eval_long_vla_only_seed49.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"129691\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-long-seed49.log\", \"submitted_at\": \"2026-05-20T02:42:50.344Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed49. 补齐 Long VLA-only 样本量 (n→8)，增强 OOD baseline 统计可靠性，与 CRM-Long 配对检验。\"}, \"eval-adaptive-k-p25-seed44\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T22:53:09.016Z\", \"updated_at\": \"2026-05-20T02:36:09.821Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed44. ~75% steps trigger K=10+CRM. P25 sweep 第三个 seed。\", \"spec\": {\"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"647875\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.054959 --k_full 10 --benchmark object --seed 44 --n_rollouts 10 --output_file logs/eval_adaptive_k_p25_seed44.json\\\"\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only (adaptive_k)\", \"seed\": 44, \"adaptive_threshold\": 0.054959, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"mode\": \"adaptive_k\"}}, \"eval-crm-spatial-seed47\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T01:18:50.143Z\", \"updated_at\": \"2026-05-20T01:19:10.476Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Spatial seed47. 补齐 CRM-Spatial 第 6 个 seed（当前 n=5, seeds 42-46），增强 in-distribution 效果的统计显著性。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 47 --K 10 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --n_rollouts 10 --output_file logs/eval_spatial_obs_only_norm02_seed47.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"201260\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-spatial-seed47.log\", \"submitted_at\": \"2026-05-20T01:19:09.529Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-object-seed49-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T01:19:03.093Z\", \"updated_at\": \"2026-05-20T01:19:03.093Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --seed 49 --n_rollouts 10 --K 1 --output_file logs/eval_object_vla_only_seed49.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"200692\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed49-r2.log\", \"submitted_at\": \"2026-05-20T01:19:02.012Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-vla-only-spatial-seed49-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T22:12:47.550Z\", \"updated_at\": \"2026-05-19T22:12:58.379Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode acr_vla --benchmark spatial --seed 49 --K 1 --n_rollouts 10 --output_file logs/eval_vla_only_spatial_seed49_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"37308\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed49-r2.log\", \"submitted_at\": \"2026-05-19T22:12:46.685Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed49. 补齐 Spatial VLA-only 样本量 (n→7)。重跑（前次进程死亡）。\"}}, \"count\": 98, \"total\": 98, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.5978}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Let me understand the situation:

**bjb1-32546 GPU State (all 6 GPUs occupied):**

| GPU | PID | Elapsed | Experiment | Registry Status |
|-----|-----|---------|------------|----------------|
| cuda:0 | 818121 | ~1.5h | Object Adaptive tau=0.25 s43 | NOT registered |
| cuda:1 | 818386 | ~1.5h | Goal CRM norm=0.05 s43 | NOT registered |


| cuda:2 | 818658 | ~1.5h | Goal Adaptive tau=0.25 s43 | NOT registered |
| cuda:3 | 848576 | ~48min | Long VLA-only s42 | RUNNING (eval-supp-long-vla-only-s42) |
| cuda:4 | 818928 | ~1.5h | Object CRM norm=0.05 s43 | NOT registered |
| cuda:5 | 835200 | ~1.1h | Goal Adaptive tau=0.25 s44 | RUNNING (eval-supp-adapt-tau025-goal) |

Most of the experiments have been running for about 1.5 hours and aren't registered in the system yet, while two are actively running with registered status. The cuda:3 job is the newest at 48 minutes elapsed.

Looking at the P1 deployment options, I can see that two of the four required experiments are already running—the Goal CRM norm=0.05 on cuda:1 and the Goal Adaptive tau=0.25 on cuda:2—but they're not registered. I need to register these four unregistered experiments and note that all GPUs are currently occupied.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "fddb0c2d-e5bf-4442-898a-9e71036144ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTmqJioWdREq6QQLts1DAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4927,
      "cache_read_input_tokens": 38770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4927
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

_source line 29_

全部 6 个 GPU 都在跑实验，无空闲 GPU。

**当前 bjb1-32546 GPU 状态：**

| GPU | PID | 运行时长 | 实验 | Registry |
|-----|-----|---------|------|----------|
| cuda:0 | 818121 | ~1.5h | Object Adaptive tau=0.25 s43 | 未注册 |
| cuda:1 | 818386 | ~1.5h | Goal CRM norm=0.05 s43 | 未注册 |
| cuda:2 | 818658 | ~1.5h | Goal Adaptive tau=0.25 s43 | 未注册 |
| cuda:3 | 848576 | ~48min | Long VLA-only s42 | RUNNING |
| cuda:4 | 818928 | ~1.5h | Object CRM norm=0.05 s43 | 未注册 |
| cuda:5 | 835200 | ~1.1h | Goal Adaptive tau=0.25 s44 | RUNNING |

**关键发现：**
- P1 部署选项 #2 (Goal CRM norm=0.05 s43) 已在 cuda:1 运行
- P1 部署选项 #3 (Goal Adaptive tau=0.25 s43) 已在 cuda:2 运行
- 无空闲 GPU，无法部署新实验

现在为 4 个未注册的实验补注册 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "8599cd2f-5169-42a0-85fa-e1c390bad36d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTmqJioWdREq6QQLts1DAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4927,
      "cache_read_input_tokens": 38770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4927
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

_source line 30_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JYe2JANJXMe1ifEbrUT7hB`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "74860752-754c-4369-b88f-7cefdb844ec1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTmqJioWdREq6QQLts1DAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4927,
      "cache_read_input_tokens": 38770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4927
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

_source line 31 · 2026-05-23T10:13:44.866Z_

<details><summary>↩ Tool result · `toolu_01JYe2JANJXMe1ifEbrUT7hB`</summary>

````text
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "8bfb8aba-4e1b-4a7d-bfef-9f6ede910482",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 27
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Let me register the 4 unregistered experiments. I need to create registry entries for them with status RUNNING and proper specs.

For each experiment:

1. cuda:0 (PID 818121): Object Adaptive tau=0.25 s43
   - exp_id: eval-supp-adapt-tau025-obj-s43
   - command: python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2


2. cuda:1 (PID 818386): Goal CRM norm=0.05 s43
   - exp_id: eval-supp-crm-norm005-goal-s43
   - command: python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05
3. cuda:2 (PID 818658): Goal Adaptive tau=0.25 s43
   - exp_id: eval-supp-adapt-tau025-goal-s43
   - command: python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2
4. cuda:4 (PID 818928): Object CRM norm=0.05 s43
   - exp_id: eval-supp-crm-norm005-obj-s43
   - command: python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05

I'm noticing a potential naming conflict with the adaptive tau experiment ID that might need attention.

Looking back at the task requirements, I see cuda:5 is already running with eval-supp-adapt-tau025-goal-s44. For the unregistered experiments, I should assign distinct IDs: eval-supp-adapt-tau025-obj-s43 for the object adaptive run, eval-supp-crm-norm005-goal-s43 for the goal CRM variant, eval-supp-adapt-tau025-goal-s43 for the goal adaptive run, and eval-supp-crm-norm005-obj-s43 for the object CRM run. Now I need to register these using the update_registry tool.

Registering all four experiments in parallel...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "dfc536f3-2995-4906-bac5-73cebd22c0f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018khwYiFwgcF35vWE3vxrPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1537,
      "cache_read_input_tokens": 43697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1537
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

### Assistant

_source line 33_

为 4 个未注册实验补注册 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "4c707240-0300-4992-ad8f-5aeab67b95cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018khwYiFwgcF35vWE3vxrPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1537,
      "cache_read_input_tokens": 43697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1537
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

_source line 34_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_015idohQyZ2rYrSGeRFmU1mQ`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:0"
    ],
    "pid": 818121,
    "seed": 43,
    "model_name": "smolvla+crm_adaptive_tau025",
    "data_path": "LIBERO-Object",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Object"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "1a2d35e0-0dab-4b0d-8436-708c5d434f56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018khwYiFwgcF35vWE3vxrPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1537,
      "cache_read_input_tokens": 43697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1537
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

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_015qSo3KdAat6s7GJsaZrU4q`</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:1"
    ],
    "pid": 818386,
    "seed": 43,
    "model_name": "smolvla+crm_obs_only_norm005",
    "data_path": "LIBERO-Goal",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Goal"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "b74eb216-5f26-4f4c-ac97-03d83603a80a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018khwYiFwgcF35vWE3vxrPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1537,
      "cache_read_input_tokens": 43697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1537
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

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01TPS7pYteQ5ncU9gNDzmjVC`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:2"
    ],
    "pid": 818658,
    "seed": 43,
    "model_name": "smolvla+crm_adaptive_tau025",
    "data_path": "LIBERO-Goal",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Goal"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "85f0dd1e-6f10-4e68-80bf-ae184ed4075e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018khwYiFwgcF35vWE3vxrPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1537,
      "cache_read_input_tokens": 43697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1537
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

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_015PZoa2gc4GHoyPiiu4HuZP`</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:4"
    ],
    "pid": 818928,
    "seed": 43,
    "model_name": "smolvla+crm_obs_only_norm005",
    "data_path": "LIBERO-Object",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Object"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "21d0d840-0e02-4af2-b05d-7d86a789ca81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018khwYiFwgcF35vWE3vxrPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1537,
      "cache_read_input_tokens": 43697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1537
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

_source line 38 · 2026-05-23T10:14:16.226Z_

<details><summary>↩ Tool result · `toolu_015idohQyZ2rYrSGeRFmU1mQ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 11.3965}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "009fa2e8-6304-4f52-a99c-e7e8e908d882",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 11.3965}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 11.3965}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-23T10:14:19.597Z_

<details><summary>↩ Tool result · `toolu_015qSo3KdAat6s7GJsaZrU4q`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.3328}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "a124397f-3e5b-4b75-b8b1-1e1db5bfe5e5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.3328}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.3328}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T10:14:29.743Z_

<details><summary>↩ Tool result · `toolu_01TPS7pYteQ5ncU9gNDzmjVC`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 10.1165}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "8703c9ac-72e3-4cfd-950f-2083e41f5bb2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 10.1165}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 10.1165}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-23T10:14:32.831Z_

<details><summary>↩ Tool result · `toolu_015PZoa2gc4GHoyPiiu4HuZP`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.0729}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "5decedd2-023b-48cb-b48a-2a284ce7f350",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.0729}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.0729}}"
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
The experiments were already created in PREPARING status (probably from the PREPARING registry query that was too large to load). I need to transition them from PREPARING → PENDING → RUNNING, or maybe just update the needed fields. Let me check what transitions are allowed.

The error says: "Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']"

So I need to go PREPARING → PENDING first, then PENDING → RUNNING (or maybe PREPARING → QUEUED → RUNNING).

Let me try setting them to PENDING first.

Actually wait, let me also add hypotheses first since the task says "先 update_registry 创建 PREPARING 条目（含 hypothesis），再 submit_training_job"


Since they're already in PREPARING status, I'll just transition them to PENDING and move forward.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "092a9a75-32cb-48fe-8194-4c997d1f6393",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RenAdpi9B1CHkyCBGvLe2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2697,
      "cache_read_input_tokens": 45234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2697
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

_source line 43_

实验已存在（PREPARING 状态）。需要先转到 PENDING 再到 RUNNING。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "73bb2606-afe1-4c36-aaa4-f8dbcebad9b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RenAdpi9B1CHkyCBGvLe2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2697,
      "cache_read_input_tokens": 45234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2697
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

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01U1DXUKVoLBBuxJLCpjBQ4R`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s43",
  "field": "status",
  "value": "PENDING",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "69a0827d-f1be-4fbb-8663-23531b620bea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RenAdpi9B1CHkyCBGvLe2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2697,
      "cache_read_input_tokens": 45234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2697
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01EBavxJmbDW8BwKUmAkJ5gb`</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s43",
  "field": "status",
  "value": "PENDING",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "62f55610-eb92-424b-85d9-a7b0b1149d1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RenAdpi9B1CHkyCBGvLe2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2697,
      "cache_read_input_tokens": 45234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2697
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

_source line 46_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01JgTc35sYFBzQeLs7Lp9Dx5`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-goal-s43",
  "field": "status",
  "value": "PENDING",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "ae4a5e02-69fa-4d14-867e-433ef4ea9487",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RenAdpi9B1CHkyCBGvLe2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2697,
      "cache_read_input_tokens": 45234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2697
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

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01GmSn698YRwqLhU7szpjtt1`</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s43",
  "field": "status",
  "value": "PENDING",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "2a13c6ae-e482-4797-a68c-f6c71cd797f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RenAdpi9B1CHkyCBGvLe2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2697,
      "cache_read_input_tokens": 45234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2697
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

_source line 48 · 2026-05-23T10:15:02.138Z_

<details><summary>↩ Tool result · `toolu_01U1DXUKVoLBBuxJLCpjBQ4R`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T10:14:52.970Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.5166}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "7ff93f8a-ef42-403d-8a83-aabf618656cf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-adapt-tau025-obj-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:14:52.970Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:14:52.970Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 12.5166}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T10:14:52.970Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.5166}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-23T10:15:18.692Z_

<details><summary>↩ Tool result · `toolu_01EBavxJmbDW8BwKUmAkJ5gb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T10:15:08.681Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 16.5291}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "bf158345-c774-4ef7-ab5b-fc004db5d9a9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-crm-norm005-goal-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:15:08.681Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:15:08.681Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 16.5291}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T10:15:08.681Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 16.5291}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T10:15:28.613Z_

<details><summary>↩ Tool result · `toolu_01JgTc35sYFBzQeLs7Lp9Dx5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T10:15:23.340Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.9069}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "44f55c15-67ce-44da-b615-ed454ee3340f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-adapt-tau025-goal-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:15:23.340Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:15:23.340Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.9069}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T10:15:23.340Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.9069}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-23T10:15:37.118Z_

<details><summary>↩ Tool result · `toolu_01GmSn698YRwqLhU7szpjtt1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T10:15:30.412Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.4853}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "723423de-aa71-433d-b9aa-593c8e4744a4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-crm-norm005-obj-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:15:30.412Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:15:30.412Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.4853}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T10:15:30.412Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.4853}}"
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
Good. Now I need to set hypotheses and transition to RUNNING with specs. Let me add hypotheses first, then transition to RUNNING.

Actually, looking at it more carefully - these experiments were newly created (the created_at timestamps are now). The old PREPARING ones must have had different exp_ids. Let me just set hypotheses and transition to RUNNING.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "4daab8fb-6448-4d1f-9191-5dbe3e0a2cdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Fu6vzzfhmr23LKAGjoU5b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 47931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1525
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

现在添加 hypothesis 并转为 RUNNING。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "03e04936-942a-4cc7-a78f-6c23b61ff47f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Fu6vzzfhmr23LKAGjoU5b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 47931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1525
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01DyhCxkZbgMppFE1jn83Bqd`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s43",
  "field": "hypothesis",
  "value": "Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "7b6a3113-2972-4b9f-bf67-f4c48225949b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Fu6vzzfhmr23LKAGjoU5b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 47931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1525
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

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Hx9zWnyBLyhd4NTVEYEcuC`</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s43",
  "field": "hypothesis",
  "value": "CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "aad52870-db08-47d2-9435-4e232a7158e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Fu6vzzfhmr23LKAGjoU5b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 47931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1525
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

_source line 56 · 2026-05-23T10:15:48.702Z_

<details><summary>↩ Tool result · `toolu_01DyhCxkZbgMppFE1jn83Bqd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T10:15:47.533Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7604}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "9931a8c1-a937-4b48-96fa-182fdf49754d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-adapt-tau025-obj-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:14:52.970Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:15:47.533Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.7604}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T10:15:47.533Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7604}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_0128EjuT6wmEzp7uXkoE4HsG`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-goal-s43",
  "field": "hypothesis",
  "value": "Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "05d508ee-dead-4848-a8bc-a0e7821c6dc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Fu6vzzfhmr23LKAGjoU5b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 47931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1525
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

_source line 58 · 2026-05-23T10:15:51.625Z_

<details><summary>↩ Tool result · `toolu_01Hx9zWnyBLyhd4NTVEYEcuC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T10:15:50.398Z\", \"hypothesis\": \"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9133}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "30530715-5755-4d15-87ef-b75737c407a8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-crm-norm005-goal-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:15:08.681Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:15:50.398Z\\\", \\\"hypothesis\\\": \\\"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.9133}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T10:15:50.398Z\", \"hypothesis\": \"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9133}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01JN5cuifNeX41WxdL55AvCy`</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s43",
  "field": "hypothesis",
  "value": "CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "f8238d56-785d-4a44-ba6e-b5ca9b90e4ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Fu6vzzfhmr23LKAGjoU5b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 47931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1525
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

_source line 60 · 2026-05-23T10:15:54.627Z_

<details><summary>↩ Tool result · `toolu_0128EjuT6wmEzp7uXkoE4HsG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T10:15:53.458Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9901}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "d3cd8574-6004-4648-82b8-6ffac36f0462",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-adapt-tau025-goal-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:15:23.340Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:15:53.458Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.9901}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T10:15:53.458Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9901}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-23T10:15:57.542Z_

<details><summary>↩ Tool result · `toolu_01JN5cuifNeX41WxdL55AvCy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T10:15:56.371Z\", \"hypothesis\": \"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8979}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "e59d711d-2504-44f4-a8f9-26c5f6efd61e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-crm-norm005-obj-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:15:30.412Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:15:56.371Z\\\", \\\"hypothesis\\\": \\\"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.8979}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T10:15:56.371Z\", \"hypothesis\": \"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8979}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01FSXXKFHBQL89zrxwDQzEZL`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:0"
    ],
    "pid": 818121,
    "seed": 43,
    "model_name": "smolvla+crm_adaptive_tau025",
    "data_path": "LIBERO-Object",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Object"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "e16e7c5b-557e-411a-b8e0-998765b204b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3PAhpNtcLDUDM2MZabnDw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 49456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1666
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

_source line 63 · 2026-05-23T10:16:07.621Z_

<details><summary>↩ Tool result · `toolu_01FSXXKFHBQL89zrxwDQzEZL`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.7213}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "7858e8ef-4813-4ca6-b50b-5c88406b9652",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.7213}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.7213}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01LtiarNpTKKef96bfwAGWPR`</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:1"
    ],
    "pid": 818386,
    "seed": 43,
    "model_name": "smolvla+crm_obs_only_norm005",
    "data_path": "LIBERO-Goal",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Goal"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "2c396f74-17ef-44fd-9233-063c689b1248",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3PAhpNtcLDUDM2MZabnDw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 49456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1666
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

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01DPNBcKHihondd6CXSe2ub2`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:2"
    ],
    "pid": 818658,
    "seed": 43,
    "model_name": "smolvla+crm_adaptive_tau025",
    "data_path": "LIBERO-Goal",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Goal"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "dad1d2b5-766c-4869-a680-252b83861efe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3PAhpNtcLDUDM2MZabnDw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 49456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1666
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

_source line 66 · 2026-05-23T10:16:12.030Z_

<details><summary>↩ Tool result · `toolu_01LtiarNpTKKef96bfwAGWPR`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.2765}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "47555b7e-d4fa-4c21-8cbd-bf4b33322cde",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.2765}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.2765}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01VhSjWftU2qr1hLJ9FGUCpN`</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:4"
    ],
    "pid": 818928,
    "seed": 43,
    "model_name": "smolvla+crm_obs_only_norm005",
    "data_path": "LIBERO-Object",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Object"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "3cbc2db6-cb69-44b1-93fe-4c696cb9694e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3PAhpNtcLDUDM2MZabnDw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 49456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1666
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

_source line 68 · 2026-05-23T10:16:15.108Z_

<details><summary>↩ Tool result · `toolu_01DPNBcKHihondd6CXSe2ub2`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.066}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "1e33bdc0-efa3-48b4-b377-b7a1e6b3b055",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.066}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.066}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-23T10:16:18.398Z_

<details><summary>↩ Tool result · `toolu_01VhSjWftU2qr1hLJ9FGUCpN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.2754}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "f487a984-db88-4fa2-bb36-c85f0c3534a5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.2754}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.2754}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 70_

<details><summary>Logged reasoning block</summary>

```text
PENDING → RUNNING not allowed. Allowed transitions from PENDING are DONE and QUEUED. Let me try PENDING → QUEUED → RUNNING.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "8050c3d5-9ab4-4640-97c9-19b901270e4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuwHAbQ8dxxwoipAZJFj1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1815,
      "cache_read_input_tokens": 51122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1815
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 71_

需要 PENDING → QUEUED → RUNNING。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "1a5db82f-0c44-4d49-9b03-bdaa407a34a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuwHAbQ8dxxwoipAZJFj1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1815,
      "cache_read_input_tokens": 51122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1815
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Au1g5xSNZhce4YczcmKRMR`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s43",
  "field": "status",
  "value": "QUEUED",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "ea05353b-3586-47b1-8960-793b8a067468",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuwHAbQ8dxxwoipAZJFj1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1815,
      "cache_read_input_tokens": 51122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1815
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 73_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01KsRVtjBvbdtk5eDehuBtV6`</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s43",
  "field": "status",
  "value": "QUEUED",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "e9f12b14-7f01-4e95-ab3f-4fc2e35af346",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuwHAbQ8dxxwoipAZJFj1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1815,
      "cache_read_input_tokens": 51122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1815
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 74_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01UvNMzivphbzHcowxyGCPTs`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-goal-s43",
  "field": "status",
  "value": "QUEUED",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "4e507465-1478-4788-b2f8-3015278f6abe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuwHAbQ8dxxwoipAZJFj1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1815,
      "cache_read_input_tokens": 51122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1815
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 75_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01DdoSnWWHYD3rLZQD4mfZSp`</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s43",
  "field": "status",
  "value": "QUEUED",
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "54fe5562-68da-41a9-b8d4-79f811d691e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuwHAbQ8dxxwoipAZJFj1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1815,
      "cache_read_input_tokens": 51122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1815
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 76 · 2026-05-23T10:16:32.144Z_

<details><summary>↩ Tool result · `toolu_01Au1g5xSNZhce4YczcmKRMR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T10:16:25.410Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.9933}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "03ac825d-9b1c-4610-9bd8-2a58e5d7fd6e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-adapt-tau025-obj-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:14:52.970Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:16:25.410Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.9933}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T10:16:25.410Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.9933}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-23T10:16:41.143Z_

<details><summary>↩ Tool result · `toolu_01KsRVtjBvbdtk5eDehuBtV6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T10:16:34.711Z\", \"hypothesis\": \"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.9783}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "bcb97fa8-3014-44da-8c2e-4eef5bc52647",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-crm-norm005-goal-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:15:08.681Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:16:34.711Z\\\", \\\"hypothesis\\\": \\\"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.9783}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T10:16:34.711Z\", \"hypothesis\": \"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.9783}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-23T10:16:46.786Z_

<details><summary>↩ Tool result · `toolu_01UvNMzivphbzHcowxyGCPTs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T10:16:42.856Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.63}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "7e9de45e-69b8-4c57-8353-e9477337d5b5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-adapt-tau025-goal-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:15:23.340Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:16:42.856Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.63}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T10:16:42.856Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.63}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-23T10:16:52.366Z_

<details><summary>↩ Tool result · `toolu_01DdoSnWWHYD3rLZQD4mfZSp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T10:16:48.441Z\", \"hypothesis\": \"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.5698}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "bc438d05-52f6-4199-9b8d-051a35af90be",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-crm-norm005-obj-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:15:30.412Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:16:48.441Z\\\", \\\"hypothesis\\\": \\\"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.5698}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T10:16:48.441Z\", \"hypothesis\": \"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.5698}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01EVq27h7U7j3pXaWAUwFiUd`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:0"
    ],
    "pid": 818121,
    "seed": 43,
    "model_name": "smolvla+crm_adaptive_tau025",
    "data_path": "LIBERO-Object",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Object"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "a8b87049-4dfa-4242-9670-30d65eaae959",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTX9gMtMc5DaK5gq8EgtRR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 52937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1568
      },
      "output_tokens": 68,
      "service_tier": "standard",
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

_source line 81_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Qmh6gGz6WD5vpc5xDBca5h`</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:1"
    ],
    "pid": 818386,
    "seed": 43,
    "model_name": "smolvla+crm_obs_only_norm005",
    "data_path": "LIBERO-Goal",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Goal"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "26908418-192b-4a77-9c8d-c3ac54bb48d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTX9gMtMc5DaK5gq8EgtRR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 52937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1568
      },
      "output_tokens": 68,
      "service_tier": "standard",
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

_source line 82_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_016PcRjE845tYPvc6Y6tuWQS`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:2"
    ],
    "pid": 818658,
    "seed": 43,
    "model_name": "smolvla+crm_adaptive_tau025",
    "data_path": "LIBERO-Goal",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Goal"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "f6d1d35c-fa77-466f-acf3-aeb42dac508f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTX9gMtMc5DaK5gq8EgtRR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 52937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1568
      },
      "output_tokens": 68,
      "service_tier": "standard",
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

_source line 83_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01P4hAvmYGJmARmC3AtG9h8r`</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:4"
    ],
    "pid": 818928,
    "seed": 43,
    "model_name": "smolvla+crm_obs_only_norm005",
    "data_path": "LIBERO-Object",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Object"
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
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "65eb39d5-8761-42cb-b3ae-44aa1baf4827",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTX9gMtMc5DaK5gq8EgtRR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 52937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1568
      },
      "output_tokens": 68,
      "service_tier": "standard",
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

_source line 84 · 2026-05-23T10:17:11.041Z_

<details><summary>↩ Tool result · `toolu_01EVq27h7U7j3pXaWAUwFiUd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T10:17:04.537Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:0\"], \"pid\": 818121, \"seed\": 43, \"model_name\": \"smolvla+crm_adaptive_tau025\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.7019}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "8a335d8c-60d6-44ff-924a-7365aab336d8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-adapt-tau025-obj-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:14:52.970Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:17:04.537Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu_ids\\\": [\\\"cuda:0\\\"], \\\"pid\\\": 818121, \\\"seed\\\": 43, \\\"model_name\\\": \\\"smolvla+crm_adaptive_tau025\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.7019}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T10:17:04.537Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:0\"], \"pid\": 818121, \"seed\": 43, \"model_name\": \"smolvla+crm_adaptive_tau025\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.7019}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-23T10:17:16.642Z_

<details><summary>↩ Tool result · `toolu_01Qmh6gGz6WD5vpc5xDBca5h`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T10:17:12.777Z\", \"hypothesis\": \"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 818386, \"seed\": 43, \"model_name\": \"smolvla+crm_obs_only_norm005\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.587}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "08bb8d34-05ed-4a0d-88e9-766ddef21ed5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-crm-norm005-goal-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:15:08.681Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:17:12.777Z\\\", \\\"hypothesis\\\": \\\"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 818386, \\\"seed\\\": 43, \\\"model_name\\\": \\\"smolvla+crm_obs_only_norm005\\\", \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Goal\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.587}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T10:17:12.777Z\", \"hypothesis\": \"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 818386, \"seed\": 43, \"model_name\": \"smolvla+crm_obs_only_norm005\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.587}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-23T10:17:22.289Z_

<details><summary>↩ Tool result · `toolu_016PcRjE845tYPvc6Y6tuWQS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T10:17:18.363Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:2\"], \"pid\": 818658, \"seed\": 43, \"model_name\": \"smolvla+crm_adaptive_tau025\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.6357}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "c962cf8a-5cf2-4ac0-824e-4de4d06053e8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-adapt-tau025-goal-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:15:23.340Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:17:18.363Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu_ids\\\": [\\\"cuda:2\\\"], \\\"pid\\\": 818658, \\\"seed\\\": 43, \\\"model_name\\\": \\\"smolvla+crm_adaptive_tau025\\\", \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Goal\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.6357}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T10:17:18.363Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:2\"], \"pid\": 818658, \"seed\": 43, \"model_name\": \"smolvla+crm_adaptive_tau025\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.6357}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-23T10:17:27.916Z_

<details><summary>↩ Tool result · `toolu_01P4hAvmYGJmARmC3AtG9h8r`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T10:17:24.007Z\", \"hypothesis\": \"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:4\"], \"pid\": 818928, \"seed\": 43, \"model_name\": \"smolvla+crm_obs_only_norm005\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.6149}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "f0d7aa48-d121-4b05-83ea-a3e01bb71a4a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-crm-norm005-obj-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T10:15:30.412Z\\\", \\\"updated_at\\\": \\\"2026-05-23T10:17:24.007Z\\\", \\\"hypothesis\\\": \\\"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu_ids\\\": [\\\"cuda:4\\\"], \\\"pid\\\": 818928, \\\"seed\\\": 43, \\\"model_name\\\": \\\"smolvla+crm_obs_only_norm005\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.6149}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T10:17:24.007Z\", \"hypothesis\": \"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:4\"], \"pid\": 818928, \"seed\": 43, \"model_name\": \"smolvla+crm_obs_only_norm005\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.6149}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 88_

4 个实验已全部注册为 RUNNING。

## 审计结果汇总

**bjb1-32546 全部 6 GPU 占满，无空闲 GPU 可部署新实验。**

| GPU | exp_id | 实验 | 状态 | 运行时长 |
|-----|--------|------|------|---------|
| cuda:0 | eval-supp-adapt-tau025-obj-s43 | Object Adaptive tau=0.25 s43 | RUNNING (新注册) | ~1.5h |
| cuda:1 | eval-supp-crm-norm005-goal-s43 | Goal CRM norm=0.05 s43 | RUNNING (新注册) | ~1.5h |
| cuda:2 | eval-supp-adapt-tau025-goal-s43 | Goal Adaptive tau=0.25 s43 | RUNNING (新注册) | ~1.5h |
| cuda:3 | eval-supp-long-vla-only-s42 | Long VLA-only s42 | RUNNING (已注册) | ~48min |
| cuda:4 | eval-supp-crm-norm005-obj-s43 | Object CRM norm=0.05 s43 | RUNNING (新注册) | ~1.5h |
| cuda:5 | eval-supp-adapt-tau025-goal-s44 | Goal Adaptive tau=0.25 s44 | RUNNING (已注册) | ~1.1h |

**P1 部署选项对照：**
- #1 Long K=2 mean s42 — **无空闲 GPU，无法部署**
- #2 Goal CRM norm=0.05 s43 — **已在 cuda:1 运行**（由之前 Worker 启动）
- #3 Goal Adaptive tau=0.25 s43 — **已在 cuda:2 运行**（由之前 Worker 启动）
- #4 Goal Reconvla s44 — **无空闲 GPU，无法部署**

已为 cuda:0/1/2/4 上的 4 个未注册实验补建了 registry 条目（RUNNING）。这些实验预计还需 ~10-12h 完成（20 rollouts × 10 tasks 的 eval 通常需 12-14h）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "uuid": "8eed6b7f-6dcf-416a-854c-5d2f1703f65b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgmSmpor1qDxmvAVDuYXqE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3241,
      "cache_read_input_tokens": 54505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3241
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

_source line 89_

4 个实验已全部注册为 RUNNING。

## 审计结果汇总

**bjb1-32546 全部 6 GPU 占满，无空闲 GPU 可部署新实验。**

| GPU | exp_id | 实验 | 状态 | 运行时长 |
|-----|--------|------|------|---------|
| cuda:0 | eval-supp-adapt-tau025-obj-s43 | Object Adaptive tau=0.25 s43 | RUNNING (新注册) | ~1.5h |
| cuda:1 | eval-supp-crm-norm005-goal-s43 | Goal CRM norm=0.05 s43 | RUNNING (新注册) | ~1.5h |
| cuda:2 | eval-supp-adapt-tau025-goal-s43 | Goal Adaptive tau=0.25 s43 | RUNNING (新注册) | ~1.5h |
| cuda:3 | eval-supp-long-vla-only-s42 | Long VLA-only s42 | RUNNING (已注册) | ~48min |
| cuda:4 | eval-supp-crm-norm005-obj-s43 | Object CRM norm=0.05 s43 | RUNNING (新注册) | ~1.5h |
| cuda:5 | eval-supp-adapt-tau025-goal-s44 | Goal Adaptive tau=0.25 s44 | RUNNING (已注册) | ~1.1h |

**P1 部署选项对照：**
- #1 Long K=2 mean s42 — **无空闲 GPU，无法部署**
- #2 Goal CRM norm=0.05 s43 — **已在 cuda:1 运行**（由之前 Worker 启动）
- #3 Goal Adaptive tau=0.25 s43 — **已在 cuda:2 运行**（由之前 Worker 启动）
- #4 Goal Reconvla s44 — **无空闲 GPU，无法部署**

已为 cuda:0/1/2/4 上的 4 个未注册实验补建了 registry 条目（RUNNING）。这些实验预计还需 ~10-12h 完成（20 rollouts × 10 tasks 的 eval 通常需 12-14h）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 309241,
  "duration_api_ms": 174063,
  "num_turns": 35,
  "stop_reason": "end_turn",
  "session_id": "4294b235-1b87-40b4-afe2-9e7ed46ec777",
  "total_cost_usd": 0.80505075,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 45905,
    "cache_read_input_tokens": 483559,
    "output_tokens": 10942,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 45905,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 621,
        "cache_read_input_tokens": 54505,
        "cache_creation_input_tokens": 3241,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3241
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2620,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00273,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 10942,
      "cacheReadInputTokens": 483559,
      "cacheCreationInputTokens": 45905,
      "webSearchRequests": 0,
      "costUSD": 0.80232075,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "295515bf-0000-47ef-a7e7-a278ebc26da2"
}
```

</details>

---
