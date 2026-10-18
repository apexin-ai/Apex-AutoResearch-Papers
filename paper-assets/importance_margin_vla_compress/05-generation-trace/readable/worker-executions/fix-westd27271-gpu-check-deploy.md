# fix westd27271 gpu check deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 84
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_fix_westd27271_gpu_check_deploy_20260527T061429.log`
- **Structured JSON:** [`918ba03f141defd2c67d.json`](../../sessions/91/918ba03f141defd2c67d.json)

## Before a recorded user message

37 recorded events

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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
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
  "uuid": "a66f7643-353c-4008-9f70-930ad5c76e3a",
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
    "resetsAt": 1779877200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "cd9e74eb-78fa-417f-9706-7d2a9e2ae2ce",
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me check the GPU status on the server immediately.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "a8d8717a-036c-49e7-95e0-ad98db88327a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01219qz8XQfFd3xxWGLfkct6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12278,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12278
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

### Assistant

_source line 5_

检查 westd-27271 GPU 和实验状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "3c1502bc-e665-4a90-87e8-c7f444e99982",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01219qz8XQfFd3xxWGLfkct6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12278,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12278
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CTCA65e3q5uzKbN22WNaaF`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "a1d686b4-d7c8-488c-b3b9-7d41efc98a61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01219qz8XQfFd3xxWGLfkct6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12278,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12278
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

_source line 7 · 2026-05-27T06:14:43.684Z_

<details><summary>↩ Tool result · `toolu_01CTCA65e3q5uzKbN22WNaaF`</summary>

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
  "tool_name": "mcp__agent-ml-research__submit_training_job"
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "951393ff-7cbc-4046-b6d8-e3a5d00de201",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 27
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Let me run the GPU status checks in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "7c6bb7f3-5752-4a1b-842d-85f9110e1f96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMS7fRVSxgDJs1fQRtnXs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2530,
      "cache_read_input_tokens": 24123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2530
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015kQWvoc4UoSAvrYBM4ZQGp`</summary>

```json
{
  "server": "westd-27271",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "17ac76b1-922e-4ca1-a6bb-c7f93b06577d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMS7fRVSxgDJs1fQRtnXs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2530,
      "cache_read_input_tokens": 24123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2530
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019g3jYBE6qGqtoz1pFiD52A`</summary>

```json
{
  "server": "westd-27271",
  "command": "ps aux | grep -E \"eval_openvla|eval_pi05\" | grep -v grep",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "4cce5f1c-7502-4455-81f6-d4816ac4f11e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMS7fRVSxgDJs1fQRtnXs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2530,
      "cache_read_input_tokens": 24123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2530
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

_source line 11 · 2026-05-27T06:14:49.235Z_

<details><summary>↩ Tool result · `toolu_015kQWvoc4UoSAvrYBM4ZQGp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 15964 MiB, 97887 MiB, 91 %\\n1, 1 MiB, 97887 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.24}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "ce20e72f-ecaa-4cfd-9a62-c82ded664d1d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 15964 MiB, 97887 MiB, 91 %\\\\n1, 1 MiB, 97887 MiB, 0 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.24}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 15964 MiB, 97887 MiB, 91 %\\n1, 1 MiB, 97887 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.24}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RfVcsDZXifqi9yzX5MGRDa`</summary>

```json
{
  "server": "westd-27271",
  "command": "tmux list-sessions",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "34f35b75-c22e-4c80-8c9c-f9c8477cbd39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMS7fRVSxgDJs1fQRtnXs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2530,
      "cache_read_input_tokens": 24123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2530
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

_source line 13 · 2026-05-27T06:14:49.250Z_

<details><summary>↩ Tool result · `toolu_019g3jYBE6qGqtoz1pFiD52A`</summary>

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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "8dfb872f-8262-4689-8293-607a2bb505df",
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

_source line 14 · 2026-05-27T06:14:49.263Z_

<details><summary>↩ Tool result · `toolu_01RfVcsDZXifqi9yzX5MGRDa`</summary>

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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "23c56c8d-dcec-4ae8-8fc0-ae7903a1d206",
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

### Assistant

_source line 15_

GPU0: 15964 MiB 使用中, 91% 利用率 — 在跑。GPU1: 1 MiB, 0% — 空闲。

检查 GPU0 日志和 GPU1 之前的实验状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "facc250c-7b72-4db7-8008-9b7620eab657",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TztjrTSrVJDYaH7qGnuhB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 26653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 745
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

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CN6eU69ujZXwpTFQXveWk8`</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -30 /root/runs/importance_margin_vla_compress/eval_openvla_attn_k095_goal_seed42_v3.log",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "481f4fa8-2504-4c44-bd8b-7404ee5d4fa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TztjrTSrVJDYaH7qGnuhB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 26653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 745
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

### Tool result

_source line 17 · 2026-05-27T06:14:54.611Z_

<details><summary>↩ Tool result · `toolu_01CN6eU69ujZXwpTFQXveWk8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-7b-finetuned-libero-goal\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  7.58it/s]\\rLoading checkpoint shards:  50%|█████     | 2/4 [00:00<00:00,  8.47it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 11.75it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 10.77it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] Attention pruning: k=0.95\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[*] libero_goal: 10 tasks x 50 episodes = 500 total\\n\\n[Task 1/10] open the middle drawer of the cabinet\\n[Attn Pruning] 256 -> 243 vision tokens (k=0.95), importance range=[0.7313, 1.6883]\\n  Ep 10/50 task_sr=8/10 (2.6 eps/min)\\n  Ep 20/50 task_sr=14/20 (2.3 eps/min)\\n  Ep 30/50 task_sr=20/30 (2.2 eps/min)\\n  Ep 40/50 task_sr=27/40 (2.2 eps/min)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "9ec86d7f-8d3d-4ff0-9889-da46a004a51a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-7b-finetuned-libero-goal\\\\n\\\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  7.58it/s]\\\\rLoading checkpoint shards:  50%|█████     | 2/4 [00:00<00:00,  8.47it/s]\\\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 11.75it/s]\\\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 10.77it/s]\\\\n[*] Model loaded, GPU: 15.1 GB\\\\n[*] Vision tokens: 256, dim: 4096\\\\n[*] Attention pruning: k=0.95\\\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n[*] libero_goal: 10 tasks x 50 episodes = 500 total\\\\n\\\\n[Task 1/10] open the middle drawer of the cabinet\\\\n[Attn Pruning] 256 -> 243 vision tokens (k=0.95), importance range=[0.7313, 1.6883]\\\\n  Ep 10/50 task_sr=8/10 (2.6 eps/min)\\\\n  Ep 20/50 task_sr=14/20 (2.3 eps/min)\\\\n  Ep 30/50 task_sr=20/30 (2.2 eps/min)\\\\n  Ep 40/50 task_sr=27/40 (2.2 eps/min)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-7b-finetuned-libero-goal\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  7.58it/s]\\rLoading checkpoint shards:  50%|█████     | 2/4 [00:00<00:00,  8.47it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 11.75it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 10.77it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] Attention pruning: k=0.95\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[*] libero_goal: 10 tasks x 50 episodes = 500 total\\n\\n[Task 1/10] open the middle drawer of the cabinet\\n[Attn Pruning] 256 -> 243 vision tokens (k=0.95), importance range=[0.7313, 1.6883]\\n  Ep 10/50 task_sr=8/10 (2.6 eps/min)\\n  Ep 20/50 task_sr=14/20 (2.3 eps/min)\\n  Ep 30/50 task_sr=20/30 (2.2 eps/min)\\n  Ep 40/50 task_sr=27/40 (2.2 eps/min)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BGM9mibdt4mMjaccsidqoN`</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -50 /root/runs/importance_margin_vla_compress/eval_openvla_attn_k095_object_seed42.log",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "65cae379-d3d0-41da-a1c9-b20150773127",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TztjrTSrVJDYaH7qGnuhB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 26653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 745
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

### Tool result

_source line 19 · 2026-05-27T06:14:55.635Z_

<details><summary>↩ Tool result · `toolu_01BGM9mibdt4mMjaccsidqoN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Ep 40/50 task_sr=33/40 (2.0 eps/min)\\n  Ep 50/50 task_sr=43/50 (2.1 eps/min)\\n  => Task SR: 0.860 (43/50)\\n\\n[Task 6/10] pick up the tomato sauce and place it in the basket\\n  Ep 10/50 task_sr=8/10 (2.1 eps/min)\\n  Ep 20/50 task_sr=15/20 (2.1 eps/min)\\n  Ep 30/50 task_sr=22/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=28/40 (2.0 eps/min)\\n  Ep 50/50 task_sr=38/50 (2.1 eps/min)\\n  => Task SR: 0.760 (38/50)\\n\\n[Task 7/10] pick up the butter and place it in the basket\\n  Ep 10/50 task_sr=7/10 (2.1 eps/min)\\n  Ep 20/50 task_sr=12/20 (2.1 eps/min)\\n  Ep 30/50 task_sr=19/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=24/40 (2.1 eps/min)\\n  Ep 50/50 task_sr=31/50 (2.1 eps/min)\\n  => Task SR: 0.620 (31/50)\\n\\n[Task 8/10] pick up the milk and place it in the basket\\n  Ep 10/50 task_sr=6/10 (2.1 eps/min)\\n  Ep 20/50 task_sr=11/20 (2.1 eps/min)\\n  Ep 30/50 task_sr=16/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=25/40 (2.1 eps/min)\\n  Ep 50/50 task_sr=31/50 (2.1 eps/min)\\n  => Task SR: 0.620 (31/50)\\n\\n[Task 9/10] pick up the chocolate pudding and place it in the basket\\n  Ep 10/50 task_sr=8/10 (2.1 eps/min)\\n  Ep 20/50 task_sr=15/20 (2.1 eps/min)\\n  Ep 30/50 task_sr=20/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=26/40 (2.1 eps/min)\\n  Ep 50/50 task_sr=33/50 (2.1 eps/min)\\n  => Task SR: 0.660 (33/50)\\n\\n[Task 10/10] pick up the orange juice and place it in the basket\\n  Ep 10/50 task_sr=9/10 (2.1 eps/min)\\n  Ep 20/50 task_sr=19/20 (2.1 eps/min)\\n  Ep 30/50 task_sr=27/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=36/40 (2.1 eps/min)\\n  Ep 50/50 task_sr=46/50 (2.1 eps/min)\\n  => Task SR: 0.920 (46/50)\\n\\n============================================================\\nOverall SR: 0.7120 (356/500)\\nTime: 238.2 min\\n============================================================\\n[*] Saved: /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attention_prune_k095_object_seed42.json\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "b433a057-d051-471a-88e1-5c8353c67dea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  Ep 40/50 task_sr=33/40 (2.0 eps/min)\\\\n  Ep 50/50 task_sr=43/50 (2.1 eps/min)\\\\n  => Task SR: 0.860 (43/50)\\\\n\\\\n[Task 6/10] pick up the tomato sauce and place it in the basket\\\\n  Ep 10/50 task_sr=8/10 (2.1 eps/min)\\\\n  Ep 20/50 task_sr=15/20 (2.1 eps/min)\\\\n  Ep 30/50 task_sr=22/30 (2.1 eps/min)\\\\n  Ep 40/50 task_sr=28/40 (2.0 eps/min)\\\\n  Ep 50/50 task_sr=38/50 (2.1 eps/min)\\\\n  => Task SR: 0.760 (38/50)\\\\n\\\\n[Task 7/10] pick up the butter and place it in the basket\\\\n  Ep 10/50 task_sr=7/10 (2.1 eps/min)\\\\n  Ep 20/50 task_sr=12/20 (2.1 eps/min)\\\\n  Ep 30/50 task_sr=19/30 (2.1 eps/min)\\\\n  Ep 40/50 task_sr=24/40 (2.1 eps/min)\\\\n  Ep 50/50 task_sr=31/50 (2.1 eps/min)\\\\n  => Task SR: 0.620 (31/50)\\\\n\\\\n[Task 8/10] pick up the milk and place it in the basket\\\\n  Ep 10/50 task_sr=6/10 (2.1 eps/min)\\\\n  Ep 20/50 task_sr=11/20 (2.1 eps/min)\\\\n  Ep 30/50 task_sr=16/30 (2.1 eps/min)\\\\n  Ep 40/50 task_sr=25/40 (2.1 eps/min)\\\\n  Ep 50/50 task_sr=31/50 (2.1 eps/min)\\\\n  => Task SR: 0.620 (31/50)\\\\n\\\\n[Task 9/10] pick up the chocolate pudding and place it in the basket\\\\n  Ep 10/50 task_sr=8/10 (2.1 eps/min)\\\\n  Ep 20/50 task_sr=15/20 (2.1 eps/min)\\\\n  Ep 30/50 task_sr=20/30 (2.1 eps/min)\\\\n  Ep 40/50 task_sr=26/40 (2.1 eps/min)\\\\n  Ep 50/50 task_sr=33/50 (2.1 eps/min)\\\\n  => Task SR: 0.660 (33/50)\\\\n\\\\n[Task 10/10] pick up the orange juice and place it in the basket\\\\n  Ep 10/50 task_sr=9/10 (2.1 eps/min)\\\\n  Ep 20/50 task_sr=19/20 (2.1 eps/min)\\\\n  Ep 30/50 task_sr=27/30 (2.1 eps/min)\\\\n  Ep 40/50 task_sr=36/40 (2.1 eps/min)\\\\n  Ep 50/50 task_sr=46/50 (2.1 eps/min)\\\\n  => Task SR: 0.920 (46/50)\\\\n\\\\n============================================================\\\\nOverall SR: 0.7120 (356/500)\\\\nTime: 238.2 min\\\\n============================================================\\\\n[*] Saved: /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attention_prune_k095_object_seed42.json\\\\nEXIT_CODE=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  Ep 40/50 task_sr=33/40 (2.0 eps/min)\\n  Ep 50/50 task_sr=43/50 (2.1 eps/min)\\n  => Task SR: 0.860 (43/50)\\n\\n[Task 6/10] pick up the tomato sauce and place it in the basket\\n  Ep 10/50 task_sr=8/10 (2.1 eps/min)\\n  Ep 20/50 task_sr=15/20 (2.1 eps/min)\\n  Ep 30/50 task_sr=22/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=28/40 (2.0 eps/min)\\n  Ep 50/50 task_sr=38/50 (2.1 eps/min)\\n  => Task SR: 0.760 (38/50)\\n\\n[Task 7/10] pick up the butter and place it in the basket\\n  Ep 10/50 task_sr=7/10 (2.1 eps/min)\\n  Ep 20/50 task_sr=12/20 (2.1 eps/min)\\n  Ep 30/50 task_sr=19/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=24/40 (2.1 eps/min)\\n  Ep 50/50 task_sr=31/50 (2.1 eps/min)\\n  => Task SR: 0.620 (31/50)\\n\\n[Task 8/10] pick up the milk and place it in the basket\\n  Ep 10/50 task_sr=6/10 (2.1 eps/min)\\n  Ep 20/50 task_sr=11/20 (2.1 eps/min)\\n  Ep 30/50 task_sr=16/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=25/40 (2.1 eps/min)\\n  Ep 50/50 task_sr=31/50 (2.1 eps/min)\\n  => Task SR: 0.620 (31/50)\\n\\n[Task 9/10] pick up the chocolate pudding and place it in the basket\\n  Ep 10/50 task_sr=8/10 (2.1 eps/min)\\n  Ep 20/50 task_sr=15/20 (2.1 eps/min)\\n  Ep 30/50 task_sr=20/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=26/40 (2.1 eps/min)\\n  Ep 50/50 task_sr=33/50 (2.1 eps/min)\\n  => Task SR: 0.660 (33/50)\\n\\n[Task 10/10] pick up the orange juice and place it in the basket\\n  Ep 10/50 task_sr=9/10 (2.1 eps/min)\\n  Ep 20/50 task_sr=19/20 (2.1 eps/min)\\n  Ep 30/50 task_sr=27/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=36/40 (2.1 eps/min)\\n  Ep 50/50 task_sr=46/50 (2.1 eps/min)\\n  => Task SR: 0.920 (46/50)\\n\\n============================================================\\nOverall SR: 0.7120 (356/500)\\nTime: 238.2 min\\n============================================================\\n[*] Saved: /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attention_prune_k095_object_seed42.json\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01VuEpc7qtFdA5KDCGmHLR5c`</summary>

```json
{
  "server": "westd-27271",
  "command": "ps -p 638225 -o pid= 2>/dev/null && echo \"RUNNING\" || echo \"DONE\"",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "b2b3a710-2673-443c-8519-1ce03d24b14d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TztjrTSrVJDYaH7qGnuhB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 26653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 745
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

### Tool result

_source line 21 · 2026-05-27T06:14:56.495Z_

<details><summary>↩ Tool result · `toolu_01VuEpc7qtFdA5KDCGmHLR5c`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "2a87e205-3a1d-4efd-8d09-af8ab56ef34a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_0194piRE4cKtyU416RA1yhYR`</summary>

```json
{
  "server": "westd-27271",
  "command": "tmux list-sessions 2>/dev/null || echo \"NO_TMUX_SESSIONS\"",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "bd927349-dc86-440a-adea-e7e81b8d63c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TztjrTSrVJDYaH7qGnuhB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 26653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 745
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

### Tool result

_source line 23 · 2026-05-27T06:14:57.176Z_

<details><summary>↩ Tool result · `toolu_0194piRE4cKtyU416RA1yhYR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_openvla_attn_k095_goal_seed42_v3: 1 windows (created Wed May 27 13:55:53 2026)\\npi05_attn_k075_long: 1 windows (created Wed May 27 06:58:13 2026)\\npi05_attn_k07_long_rerun: 1 windows (created Wed May 27 06:58:01 2026)\\npi05_l2norm_k07_long_rerun: 1 windows (created Wed May 27 06:57:47 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "2a57ad5d-e047-4177-ab77-80bb98a7cee8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_openvla_attn_k095_goal_seed42_v3: 1 windows (created Wed May 27 13:55:53 2026)\\\\npi05_attn_k075_long: 1 windows (created Wed May 27 06:58:13 2026)\\\\npi05_attn_k07_long_rerun: 1 windows (created Wed May 27 06:58:01 2026)\\\\npi05_l2norm_k07_long_rerun: 1 windows (created Wed May 27 06:57:47 2026)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_openvla_attn_k095_goal_seed42_v3: 1 windows (created Wed May 27 13:55:53 2026)\\npi05_attn_k075_long: 1 windows (created Wed May 27 06:58:13 2026)\\npi05_attn_k07_long_rerun: 1 windows (created Wed May 27 06:58:01 2026)\\npi05_l2norm_k07_long_rerun: 1 windows (created Wed May 27 06:57:47 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
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
Let me summarize the findings:

**GPU0**: Running `eval_openvla_attn_k095_goal_seed42_v3` - currently on Task 1/10, Ep 40/50. Working fine.

**GPU1**: PID 638225 is DONE. The Object experiment completed:
- Overall SR: 0.7120 (356/500)
- Time: 238.2 min
- EXIT_CODE=0

GPU1 is now idle. I need to:
1. Register the Object result
2. Check what models are available to deploy next on GPU1


3. Look at the ROADMAP to see which experiment should run next on the freed GPU.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "1ad95961-7b7c-4e9b-9f2e-96f2ae8680d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZhUtmTrqFTHGnoLnfnWcy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 27398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2828
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

状态汇总：
- **GPU0**: OV Attn k=0.95 Goal v3 运行中，Task 1/10 Ep 40/50，正常
- **GPU1**: OV Attn k=0.95 Object **已完成** — Overall SR: **0.7120** (356/500)

注册 Object 结果，同时检查可用模型和 ROADMAP 缺口。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "7e8bb056-c2b8-496c-b641-fca0f611ba1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZhUtmTrqFTHGnoLnfnWcy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 27398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2828
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01WkFZNYcPXmUBv3SUNHt4D5`</summary>

```json
{
  "exp_id": "eval_openvla_attn_k095_object_seed42",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress",
  "spec": {
    "conclusion": "success",
    "metrics": {
      "overall_sr": 0.712
    }
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "8713ea3c-452a-4799-9647-df184fa97484",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZhUtmTrqFTHGnoLnfnWcy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 27398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2828
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_017S5P2bW5rMEBsMifhs54DF`</summary>

```json
{
  "server": "westd-27271",
  "command": "ls /root/autodl-tmp/openvla-libero-goal/ 2>/dev/null && echo \"GOAL_MODEL_OK\" || echo \"NO_GOAL\"; ls /root/autodl-tmp/openvla-libero-object/ 2>/dev/null && echo \"OBJECT_MODEL_OK\" || echo \"NO_OBJECT\"; ls /root/autodl-tmp/models/openvla-7b-finetuned-libero-10/ 2>/dev/null && echo \"LONG_MODEL_OK\" || echo \"NO_LONG\"",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "b0fec90f-0984-4099-902d-07360f181302",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZhUtmTrqFTHGnoLnfnWcy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 27398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2828
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

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_016yR5XNZpg7CX2fgnCu1EPK`</summary>

```json
{
  "project": "importance_margin_vla_compress",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "111bbdeb-ace0-4e0a-bba5-c7f2054dece0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZhUtmTrqFTHGnoLnfnWcy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 27398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2828
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

_source line 29 · 2026-05-27T06:15:20.032Z_

<details><summary>↩ Tool result · `toolu_01WkFZNYcPXmUBv3SUNHt4D5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k095_object_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T23:49:31.309Z\", \"updated_at\": \"2026-05-27T06:15:13.243Z\", \"hypothesis\": \"OpenVLA Attention k=0.95 Object seed42 — Object Attn cliff curve 顶端缺口。Attn k=0.9=61.4%, k=0.85=55.0%, k=0.75=53.2%。k=0.95 补全曲线起始段，与 L2norm k=0.95=70.6% 和 Baseline=74.0% 形成对比\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 1\", \"server\": \"westd-27271\", \"gpu_id\": 1, \"pid\": 638220, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_object_seed42.log\", \"data_path\": \"libero_object\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.712}}, \"metrics\": {\"overall_sr\": 71.2, \"per_task\": {\"T9_chocolate_pudding\": 66, \"T10_orange_juice\": 92}, \"time_min\": 238.2}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T06:12:33.664Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.4469}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "da7e8a2e-723e-495d-ba03-4397b7a7d947",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_openvla_attn_k095_object_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T23:49:31.309Z\\\", \\\"updated_at\\\": \\\"2026-05-27T06:15:13.243Z\\\", \\\"hypothesis\\\": \\\"OpenVLA Attention k=0.95 Object seed42 — Object Attn cliff curve 顶端缺口。Attn k=0.9=61.4%, k=0.85=55.0%, k=0.75=53.2%。k=0.95 补全曲线起始段，与 L2norm k=0.95=70.6% 和 Baseline=74.0% 形成对比\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 1\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu_id\\\": 1, \\\"pid\\\": 638220, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_object_seed42.log\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": \\\"10 tasks x 50 episodes\\\", \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-object\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"eval_data\\\": \\\"libero_object\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.712}}, \\\"metrics\\\": {\\\"overall_sr\\\": 71.2, \\\"per_task\\\": {\\\"T9_chocolate_pudding\\\": 66, \\\"T10_orange_juice\\\": 92}, \\\"time_min\\\": 238.2}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-27T06:12:33.664Z\\\"}, \\\"hint\\\": \\\"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 11.4469}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k095_object_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T23:49:31.309Z\", \"updated_at\": \"2026-05-27T06:15:13.243Z\", \"hypothesis\": \"OpenVLA Attention k=0.95 Object seed42 — Object Attn cliff curve 顶端缺口。Attn k=0.9=61.4%, k=0.85=55.0%, k=0.75=53.2%。k=0.95 补全曲线起始段，与 L2norm k=0.95=70.6% 和 Baseline=74.0% 形成对比\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 1\", \"server\": \"westd-27271\", \"gpu_id\": 1, \"pid\": 638220, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_object_seed42.log\", \"data_path\": \"libero_object\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.712}}, \"metrics\": {\"overall_sr\": 71.2, \"per_task\": {\"T9_chocolate_pudding\": 66, \"T10_orange_juice\": 92}, \"time_min\": 238.2}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T06:12:33.664Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.4469}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-27T06:15:20.486Z_

<details><summary>↩ Tool result · `toolu_017S5P2bW5rMEBsMifhs54DF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"NO_GOAL\\nREADME.md\\nadded_tokens.json\\nconfig.json\\nconfiguration_prismatic.py\\ndataset_statistics.json\\ngeneration_config.json\\nmodel-00001-of-00004.safetensors\\nmodel-00002-of-00004.safetensors\\nmodel-00003-of-00004.safetensors\\nmodel-00004-of-00004.safetensors\\nmodel.safetensors.index.json\\nmodeling_prismatic.py\\npreprocessor_config.json\\nprocessing_prismatic.py\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer.model\\ntokenizer_config.json\\nOBJECT_MODEL_OK\\nNO_LONG\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "4dc91f9e-c887-40bb-ba5f-b8b92c62a149",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"NO_GOAL\\\\nREADME.md\\\\nadded_tokens.json\\\\nconfig.json\\\\nconfiguration_prismatic.py\\\\ndataset_statistics.json\\\\ngeneration_config.json\\\\nmodel-00001-of-00004.safetensors\\\\nmodel-00002-of-00004.safetensors\\\\nmodel-00003-of-00004.safetensors\\\\nmodel-00004-of-00004.safetensors\\\\nmodel.safetensors.index.json\\\\nmodeling_prismatic.py\\\\npreprocessor_config.json\\\\nprocessing_prismatic.py\\\\nspecial_tokens_map.json\\\\ntokenizer.json\\\\ntokenizer.model\\\\ntokenizer_config.json\\\\nOBJECT_MODEL_OK\\\\nNO_LONG\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"NO_GOAL\\nREADME.md\\nadded_tokens.json\\nconfig.json\\nconfiguration_prismatic.py\\ndataset_statistics.json\\ngeneration_config.json\\nmodel-00001-of-00004.safetensors\\nmodel-00002-of-00004.safetensors\\nmodel-00003-of-00004.safetensors\\nmodel-00004-of-00004.safetensors\\nmodel.safetensors.index.json\\nmodeling_prismatic.py\\npreprocessor_config.json\\nprocessing_prismatic.py\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer.model\\ntokenizer_config.json\\nOBJECT_MODEL_OK\\nNO_LONG\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-27T06:15:22.793Z_

<details><summary>↩ Tool result · `toolu_016yR5XNZpg7CX2fgnCu1EPK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_pi05_random_k075_long_seed42_strict\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T05:15:32.754Z\", \"updated_at\": \"2026-05-27T06:10:47.435Z\", \"hypothesis\": \"π0.5 Random k=0.75 Long strict — cqa1 宽松条件值 62.4% 可能被污染。strict 重跑获取真实值。验证 V-shape 现象是否在 strict 条件下依然存在。\", \"parent\": \"eval_pi05_random_k085_long_seed42_strict\"}, \"eval_openvla_attn_k095_goal_seed42_v2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T05:36:10.021Z\", \"updated_at\": \"2026-05-27T06:09:58.573Z\", \"hypothesis\": \"OpenVLA Attention k=0.95 Goal seed42 v2 — v1 被误杀停在 Task 4/10。Goal Attn curve 顶端缺口。Attn k=0.9=73.2%, k=0.85=74.6%。k=0.95 补全曲线起始段\", \"parent\": \"eval_openvla_attn_k095_goal_seed42\"}, \"eval_pi05_baseline_goal_seed42_strict\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T04:55:16.633Z\", \"updated_at\": \"2026-05-27T05:48:56.329Z\", \"hypothesis\": \"Pi0.5 baseline (no pruning, k=1.0) on libero_goal with strict done-only success condition will produce a lower SR than the contaminated lenient baseline (96.4%), providing a fair reference for pruning method comparisons.\"}, \"eval_pi05_attn_k095_long_seed42_strict\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T03:41:34.647Z\", \"updated_at\": \"2026-05-27T03:54:59.429Z\", \"hypothesis\": \"π0.5 Attn k=0.95 Long strict 条件重跑 — cqa1 原版使用宽松条件(done|reward>0.5)导致 SR=77.0% 被污染。此实验使用修正后的 strict 代码(if done: only)获取真实 SR。k=0.95 是最接近 baseline 的点，修正后最有参考价值。\"}, \"eval_pi05_attn_k085_long_seed42_strict\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T03:42:25.358Z\", \"updated_at\": \"2026-05-27T03:45:27.037Z\", \"hypothesis\": \"π0.5 Attn k=0.85 Long strict — cqa1 污染值 SR=51.6% 与 reward>0.5 阈值吻合，极度可疑。strict 重跑获取真实值。L2norm k=0.85=77.8%(strict confirmed)，Attn 真实值决定 k=0.85 处方法差异\", \"parent\": \"eval_pi05_attention_k085_long_seed42_v2\"}, \"eval_pi05_attn_k09_long_seed42_strict\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T03:42:22.012Z\", \"updated_at\": \"2026-05-27T03:45:17.116Z\", \"hypothesis\": \"π0.5 Attn k=0.9 Long strict — cqa1 污染值 SR=63.8%(宽松条件)。k=0.9 是 cliff curve 关键拐点(L2norm k=0.9=81.0%)，Attn 真实值对 curve 形状至关重要。westd strict code (if done: only)\", \"parent\": \"eval_pi05_attention_k09_long_seed42\"}, \"eval_openvla_random_k095_goal_seed42_v2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T02:20:14.455Z\", \"updated_at\": \"2026-05-27T02:30:16.088Z\", \"hypothesis\": \"OpenVLA Random k=0.95 Goal seed42 v2 — v1 因 cqa1 代码版本错误(transformers 5.5.3)无效。Goal Random cliff curve 顶端：k=0.9=79.6%, k=0.85=78.6%\", \"parent\": \"eval_openvla_random_k095_goal_seed42\"}, \"eval_openvla_attn_k05_goal_seed42_v3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T02:22:31.036Z\", \"updated_at\": \"2026-05-27T02:29:42.882Z\"}, \"eval_openvla_l2norm_k095_object_seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T07:52:39.419Z\", \"updated_at\": \"2026-05-27T02:29:36.799Z\", \"hypothesis\": \"OpenVLA L2norm k=0.95 Object seed42 — Object L2norm cliff curve 顶端确认。L2norm k=0.9=70.6%。k=0.95 应接近 baseline(74.0%)\", \"parent\": \"eval_openvla_l2norm_k09_object_seed42\"}, \"eval_openvla_l2norm_k075_long_seed42_v2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T01:39:50.975Z\", \"updated_at\": \"2026-05-27T01:41:49.724Z\", \"hypothesis\": \"OpenVLA L2norm k=0.75 Long seed42 v2 — v1 因 8h 超时失败(EXIT_CODE=124, 8/10 tasks 完成)。增加 timeout 到 12h 重跑。Long suite L2norm cliff curve 关键中间点：k=0.85=38.8%, k=0.7=31.2%\", \"parent\": \"eval_openvla_l2norm_k075_long_seed42\"}, \"eval_openvla_attn_k095_long_seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T01:11:13.957Z\", \"updated_at\": \"2026-05-27T01:15:25.146Z\", \"hypothesis\": \"OpenVLA Attention k=0.95 Long seed42 — Long Attn curve 顶端缺口。Attn k=0.9=44.0%, k=0.85=45.8%。k=0.95 补全曲线起始段\"}, \"eval_openvla_l2norm_k095_long_seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T01:11:10.791Z\", \"updated_at\": \"2026-05-27T01:15:18.441Z\", \"hypothesis\": \"OpenVLA L2norm k=0.95 Long seed42 — Long L2norm curve 顶端缺口。L2norm k=0.9=43.6%, k=0.85=38.8%。k=0.95 补全曲线起始段\"}, \"eval_openvla_random_k095_long_seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T00:29:13.098Z\", \"updated_at\": \"2026-05-27T00:31:38.873Z\", \"hypothesis\": \"OpenVLA Random k=0.95 Long seed42 — Long curve 顶端三方法都缺。Random k=0.9=46.8%。k=0.95 补全 Long cliff curve 起始段\"}}, \"count\": 13, \"total\": 13, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.287}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "2f069fd2-8bff-4d7f-b070-09b22095538d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_pi05_random_k075_long_seed42_strict\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-27T05:15:32.754Z\\\", \\\"updated_at\\\": \\\"2026-05-27T06:10:47.435Z\\\", \\\"hypothesis\\\": \\\"π0.5 Random k=0.75 Long strict — cqa1 宽松条件值 62.4% 可能被污染。strict 重跑获取真实值。验证 V-shape 现象是否在 strict 条件下依然存在。\\\", \\\"parent\\\": \\\"eval_pi05_random_k085_long_seed42_strict\\\"}, \\\"eval_openvla_attn_k095_goal_seed42_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-27T05:36:10.021Z\\\", \\\"updated_at\\\": \\\"2026-05-27T06:09:58.573Z\\\", \\\"hypothesis\\\": \\\"OpenVLA Attention k=0.95 Goal seed42 v2 — v1 被误杀停在 Task 4/10。Goal Attn curve 顶端缺口。Attn k=0.9=73.2%, k=0.85=74.6%。k=0.95 补全曲线起始段\\\", \\\"parent\\\": \\\"eval_openvla_attn_k095_goal_seed42\\\"}, \\\"eval_pi05_baseline_goal_seed42_strict\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-27T04:55:16.633Z\\\", \\\"updated_at\\\": \\\"2026-05-27T05:48:56.329Z\\\", \\\"hypothesis\\\": \\\"Pi0.5 baseline (no pruning, k=1.0) on libero_goal with strict done-only success condition will produce a lower SR than the contaminated lenient baseline (96.4%), providing a fair reference for pruning method comparisons.\\\"}, \\\"eval_pi05_attn_k095_long_seed42_strict\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-27T03:41:34.647Z\\\", \\\"updated_at\\\": \\\"2026-05-27T03:54:59.429Z\\\", \\\"hypothesis\\\": \\\"π0.5 Attn k=0.95 Long strict 条件重跑 — cqa1 原版使用宽松条件(done|reward>0.5)导致 SR=77.0% 被污染。此实验使用修正后的 strict 代码(if done: only)获取真实 SR。k=0.95 是最接近 baseline 的点，修正后最有参考价值。\\\"}, \\\"eval_pi05_attn_k085_long_seed42_strict\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-27T03:42:25.358Z\\\", \\\"updated_at\\\": \\\"2026-05-27T03:45:27.037Z\\\", \\\"hypothesis\\\": \\\"π0.5 Attn k=0.85 Long strict — cqa1 污染值 SR=51.6% 与 reward>0.5 阈值吻合，极度可疑。strict 重跑获取真实值。L2norm k=0.85=77.8%(strict confirmed)，Attn 真实值决定 k=0.85 处方法差异\\\", \\\"parent\\\": \\\"eval_pi05_attention_k085_long_seed42_v2\\\"}, \\\"eval_pi05_attn_k09_long_seed42_strict\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-27T03:42:22.012Z\\\", \\\"updated_at\\\": \\\"2026-05-27T03:45:17.116Z\\\", \\\"hypothesis\\\": \\\"π0.5 Attn k=0.9 Long strict — cqa1 污染值 SR=63.8%(宽松条件)。k=0.9 是 cliff curve 关键拐点(L2norm k=0.9=81.0%)，Attn 真实值对 curve 形状至关重要。westd strict code (if done: only)\\\", \\\"parent\\\": \\\"eval_pi05_attention_k09_long_seed42\\\"}, \\\"eval_openvla_random_k095_goal_seed42_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-27T02:20:14.455Z\\\", \\\"updated_at\\\": \\\"2026-05-27T02:30:16.088Z\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.95 Goal seed42 v2 — v1 因 cqa1 代码版本错误(transformers 5.5.3)无效。Goal Random cliff curve 顶端：k=0.9=79.6%, k=0.85=78.6%\\\", \\\"parent\\\": \\\"eval_openvla_random_k095_goal_seed42\\\"}, \\\"eval_openvla_attn_k05_goal_seed42_v3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-27T02:22:31.036Z\\\", \\\"updated_at\\\": \\\"2026-05-27T02:29:42.882Z\\\"}, \\\"eval_openvla_l2norm_k095_object_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T07:52:39.419Z\\\", \\\"updated_at\\\": \\\"2026-05-27T02:29:36.799Z\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.95 Object seed42 — Object L2norm cliff curve 顶端确认。L2norm k=0.9=70.6%。k=0.95 应接近 baseline(74.0%)\\\", \\\"parent\\\": \\\"eval_openvla_l2norm_k09_object_seed42\\\"}, \\\"eval_openvla_l2norm_k075_long_seed42_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-27T01:39:50.975Z\\\", \\\"updated_at\\\": \\\"2026-05-27T01:41:49.724Z\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.75 Long seed42 v2 — v1 因 8h 超时失败(EXIT_CODE=124, 8/10 tasks 完成)。增加 timeout 到 12h 重跑。Long suite L2norm cliff curve 关键中间点：k=0.85=38.8%, k=0.7=31.2%\\\", \\\"parent\\\": \\\"eval_openvla_l2norm_k075_long_seed42\\\"}, \\\"eval_openvla_attn_k095_long_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-27T01:11:13.957Z\\\", \\\"updated_at\\\": \\\"2026-05-27T01:15:25.146Z\\\", \\\"hypothesis\\\": \\\"OpenVLA Attention k=0.95 Long seed42 — Long Attn curve 顶端缺口。Attn k=0.9=44.0%, k=0.85=45.8%。k=0.95 补全曲线起始段\\\"}, \\\"eval_openvla_l2norm_k095_long_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-27T01:11:10.791Z\\\", \\\"updated_at\\\": \\\"2026-05-27T01:15:18.441Z\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.95 Long seed42 — Long L2norm curve 顶端缺口。L2norm k=0.9=43.6%, k=0.85=38.8%。k=0.95 补全曲线起始段\\\"}, \\\"eval_openvla_random_k095_long_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-27T00:29:13.098Z\\\", \\\"updated_at\\\": \\\"2026-05-27T00:31:38.873Z\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.95 Long seed42 — Long curve 顶端三方法都缺。Random k=0.9=46.8%。k=0.95 补全 Long cliff curve 起始段\\\"}}, \\\"count\\\": 13, \\\"total\\\": 13, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.287}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_pi05_random_k075_long_seed42_strict\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T05:15:32.754Z\", \"updated_at\": \"2026-05-27T06:10:47.435Z\", \"hypothesis\": \"π0.5 Random k=0.75 Long strict — cqa1 宽松条件值 62.4% 可能被污染。strict 重跑获取真实值。验证 V-shape 现象是否在 strict 条件下依然存在。\", \"parent\": \"eval_pi05_random_k085_long_seed42_strict\"}, \"eval_openvla_attn_k095_goal_seed42_v2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T05:36:10.021Z\", \"updated_at\": \"2026-05-27T06:09:58.573Z\", \"hypothesis\": \"OpenVLA Attention k=0.95 Goal seed42 v2 — v1 被误杀停在 Task 4/10。Goal Attn curve 顶端缺口。Attn k=0.9=73.2%, k=0.85=74.6%。k=0.95 补全曲线起始段\", \"parent\": \"eval_openvla_attn_k095_goal_seed42\"}, \"eval_pi05_baseline_goal_seed42_strict\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T04:55:16.633Z\", \"updated_at\": \"2026-05-27T05:48:56.329Z\", \"hypothesis\": \"Pi0.5 baseline (no pruning, k=1.0) on libero_goal with strict done-only success condition will produce a lower SR than the contaminated lenient baseline (96.4%), providing a fair reference for pruning method comparisons.\"}, \"eval_pi05_attn_k095_long_seed42_strict\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T03:41:34.647Z\", \"updated_at\": \"2026-05-27T03:54:59.429Z\", \"hypothesis\": \"π0.5 Attn k=0.95 Long strict 条件重跑 — cqa1 原版使用宽松条件(done|reward>0.5)导致 SR=77.0% 被污染。此实验使用修正后的 strict 代码(if done: only)获取真实 SR。k=0.95 是最接近 baseline 的点，修正后最有参考价值。\"}, \"eval_pi05_attn_k085_long_seed42_strict\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T03:42:25.358Z\", \"updated_at\": \"2026-05-27T03:45:27.037Z\", \"hypothesis\": \"π0.5 Attn k=0.85 Long strict — cqa1 污染值 SR=51.6% 与 reward>0.5 阈值吻合，极度可疑。strict 重跑获取真实值。L2norm k=0.85=77.8%(strict confirmed)，Attn 真实值决定 k=0.85 处方法差异\", \"parent\": \"eval_pi05_attention_k085_long_seed42_v2\"}, \"eval_pi05_attn_k09_long_seed42_strict\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T03:42:22.012Z\", \"updated_at\": \"2026-05-27T03:45:17.116Z\", \"hypothesis\": \"π0.5 Attn k=0.9 Long strict — cqa1 污染值 SR=63.8%(宽松条件)。k=0.9 是 cliff curve 关键拐点(L2norm k=0.9=81.0%)，Attn 真实值对 curve 形状至关重要。westd strict code (if done: only)\", \"parent\": \"eval_pi05_attention_k09_long_seed42\"}, \"eval_openvla_random_k095_goal_seed42_v2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T02:20:14.455Z\", \"updated_at\": \"2026-05-27T02:30:16.088Z\", \"hypothesis\": \"OpenVLA Random k=0.95 Goal seed42 v2 — v1 因 cqa1 代码版本错误(transformers 5.5.3)无效。Goal Random cliff curve 顶端：k=0.9=79.6%, k=0.85=78.6%\", \"parent\": \"eval_openvla_random_k095_goal_seed42\"}, \"eval_openvla_attn_k05_goal_seed42_v3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T02:22:31.036Z\", \"updated_at\": \"2026-05-27T02:29:42.882Z\"}, \"eval_openvla_l2norm_k095_object_seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T07:52:39.419Z\", \"updated_at\": \"2026-05-27T02:29:36.799Z\", \"hypothesis\": \"OpenVLA L2norm k=0.95 Object seed42 — Object L2norm cliff curve 顶端确认。L2norm k=0.9=70.6%。k=0.95 应接近 baseline(74.0%)\", \"parent\": \"eval_openvla_l2norm_k09_object_seed42\"}, \"eval_openvla_l2norm_k075_long_seed42_v2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T01:39:50.975Z\", \"updated_at\": \"2026-05-27T01:41:49.724Z\", \"hypothesis\": \"OpenVLA L2norm k=0.75 Long seed42 v2 — v1 因 8h 超时失败(EXIT_CODE=124, 8/10 tasks 完成)。增加 timeout 到 12h 重跑。Long suite L2norm cliff curve 关键中间点：k=0.85=38.8%, k=0.7=31.2%\", \"parent\": \"eval_openvla_l2norm_k075_long_seed42\"}, \"eval_openvla_attn_k095_long_seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T01:11:13.957Z\", \"updated_at\": \"2026-05-27T01:15:25.146Z\", \"hypothesis\": \"OpenVLA Attention k=0.95 Long seed42 — Long Attn curve 顶端缺口。Attn k=0.9=44.0%, k=0.85=45.8%。k=0.95 补全曲线起始段\"}, \"eval_openvla_l2norm_k095_long_seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T01:11:10.791Z\", \"updated_at\": \"2026-05-27T01:15:18.441Z\", \"hypothesis\": \"OpenVLA L2norm k=0.95 Long seed42 — Long L2norm curve 顶端缺口。L2norm k=0.9=43.6%, k=0.85=38.8%。k=0.95 补全曲线起始段\"}, \"eval_openvla_random_k095_long_seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-27T00:29:13.098Z\", \"updated_at\": \"2026-05-27T00:31:38.873Z\", \"hypothesis\": \"OpenVLA Random k=0.95 Long seed42 — Long curve 顶端三方法都缺。Random k=0.9=46.8%。k=0.95 补全 Long cliff curve 起始段\"}}, \"count\": 13, \"total\": 13, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.287}}"
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
OK, let me analyze:

1. **GPU0**: OV Attn k=0.95 Goal v3 running, on Task 1/10 Ep 40/50. Good.
2. **GPU1**: IDLE. Object experiment done with SR=71.2%.

Available models on westd:
- **NO** Goal model (`/root/autodl-tmp/openvla-libero-goal/` doesn't exist — wait, the first result says "NO_GOAL")
- **YES** Object model (`/root/autodl-tmp/openvla-libero-object/`)


- **NO** Long model

Actually, GPU0 is running the Goal v3 experiment from `/root/autodl-tmp/openvla-7b-finetuned-libero-goal`, so that's where the Goal model actually lives. Let me verify which models are truly available and check the roadmap to see what I should be working on next.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "57dcaad2-dad9-4e9b-97e2-3af6fd1a0b54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014J27thDZXamKuycXQwuynx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4087,
      "cache_read_input_tokens": 30226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4087
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

_source line 33_

Object 结果已注册 (SR=71.2%)。Goal 模型路径不同，确认可用模型并检查 ROADMAP。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "a0061a96-a5ca-4d17-ad26-eec37f39fb90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014J27thDZXamKuycXQwuynx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4087,
      "cache_read_input_tokens": 30226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4087
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

_source line 34_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01SdviL4JZoj8jqsxzMHJqXn`</summary>

```json
{
  "server": "westd-27271",
  "command": "ls -d /root/autodl-tmp/openvla-7b-finetuned-libero-goal/ 2>/dev/null && echo \"GOAL_MODEL_OK\" || echo \"NO_GOAL\"; ls -d /root/autodl-tmp/openvla-7b-finetuned-libero-10/ 2>/dev/null && echo \"LONG_MODEL_OK\" || echo \"NO_LONG\"; ls /root/autodl-tmp/ | grep -i openvla",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "a99f6547-da39-47a9-b28d-09f5c82514b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014J27thDZXamKuycXQwuynx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4087,
      "cache_read_input_tokens": 30226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4087
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

_source line 35 · 2026-05-27T06:15:37.560Z_

<details><summary>↩ Tool result · `toolu_01SdviL4JZoj8jqsxzMHJqXn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-goal/\\nGOAL_MODEL_OK\\n/root/autodl-tmp/openvla-7b-finetuned-libero-10/\\nLONG_MODEL_OK\\ndownload_openvla.sh\\nopenvla-7b\\nopenvla-7b-finetuned-libero-10\\nopenvla-7b-finetuned-libero-goal\\nopenvla-7b-finetuned-libero-spatial\\nopenvla-7b-git\\nopenvla-7b-hf\\nopenvla-7b-meta\\nopenvla-libero-object\\nopenvla-repo\\nopenvla_deps\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "e9d5686e-c26b-4b24-a188-72c3d84cb638",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/openvla-7b-finetuned-libero-goal/\\\\nGOAL_MODEL_OK\\\\n/root/autodl-tmp/openvla-7b-finetuned-libero-10/\\\\nLONG_MODEL_OK\\\\ndownload_openvla.sh\\\\nopenvla-7b\\\\nopenvla-7b-finetuned-libero-10\\\\nopenvla-7b-finetuned-libero-goal\\\\nopenvla-7b-finetuned-libero-spatial\\\\nopenvla-7b-git\\\\nopenvla-7b-hf\\\\nopenvla-7b-meta\\\\nopenvla-libero-object\\\\nopenvla-repo\\\\nopenvla_deps\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-goal/\\nGOAL_MODEL_OK\\n/root/autodl-tmp/openvla-7b-finetuned-libero-10/\\nLONG_MODEL_OK\\ndownload_openvla.sh\\nopenvla-7b\\nopenvla-7b-finetuned-libero-10\\nopenvla-7b-finetuned-libero-goal\\nopenvla-7b-finetuned-libero-spatial\\nopenvla-7b-git\\nopenvla-7b-hf\\nopenvla-7b-meta\\nopenvla-libero-object\\nopenvla-repo\\nopenvla_deps\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Agent · `toolu_01CSKSyPjwU1ArVKVao6zCww`</summary>

```json
{
  "description": "Read ROADMAP for gaps",
  "subagent_type": "Explore",
  "prompt": "Read the ROADMAP.md file in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ and summarize the experiment gaps / high-priority tasks that are still TODO. I need to know what OpenVLA experiments are missing so I can deploy one on an idle GPU that has the Object model available. Report in under 300 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "f3a01b8d-342b-4968-8b40-561555d9a672",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014J27thDZXamKuycXQwuynx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4087,
      "cache_read_input_tokens": 30226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4087
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

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a1aea833ad9194404",
  "tool_use_id": "toolu_01CSKSyPjwU1ArVKVao6zCww",
  "description": "Read ROADMAP for gaps",
  "task_type": "local_agent",
  "prompt": "Read the ROADMAP.md file in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ and summarize the experiment gaps / high-priority tasks that are still TODO. I need to know what OpenVLA experiments are missing so I can deploy one on an idle GPU that has the Object model available. Report in under 300 words.",
  "uuid": "d06af2d7-8f89-4627-9d02-b6ba8485f7df",
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77"
}
```

---

## Round 1

47 recorded events

### User

_source line 38 · 2026-05-27T06:15:41.211Z_

Read the ROADMAP.md file in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ and summarize the experiment gaps / high-priority tasks that are still TODO. I need to know what OpenVLA experiments are missing so I can deploy one on an idle GPU that has the Object model available. Report in under 300 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CSKSyPjwU1ArVKVao6zCww",
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "b477176a-559c-4969-8fc9-e9b2afe42e46"
}
```

</details>

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1aea833ad9194404",
  "tool_use_id": "toolu_01CSKSyPjwU1ArVKVao6zCww",
  "description": "Reading ROADMAP.md",
  "usage": {
    "total_tokens": 17849,
    "tool_uses": 1,
    "duration_ms": 2318
  },
  "last_tool_name": "Read",
  "uuid": "ee49d05c-4c51-4438-aed4-f5b0b5d127f3",
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_012rkFTQMd2ATKF5TCf5maub`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CSKSyPjwU1ArVKVao6zCww",
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "54037e3b-84cf-4ed4-a55d-d4f48140fb4c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SbMAGPh2ieXMc5kWoRZb9Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17830,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17830,
        "ephemeral_1h_input_tokens": 0
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

_source line 41 · 2026-05-27T06:15:43.547Z_

<details><summary>↩ Tool result · `toolu_012rkFTQMd2ATKF5TCf5maub`</summary>

```text
1	# importance_margin_vla_compress — Research Dashboard
2	
3	> 最后更新: 2026-05-27 05:30 UTC | 更新原因: L2norm k=0.95 Goal = 75.2% 确认; 诊断 Worker 确认实际 GPU 状态中
4	
5	> 详见 paper_framing.md。
6	
7	## 核心方向
8	VLA vision token compressibility: **scoring method × connector × task 三维交互**。5+ 模型 × 4 LIBERO suites。
9	
10	## 当前阶段
11	✅ **Crossover table 16/16 完成**
12	✅ **Position encoding sensitivity 确认 (D237)**
13	✅ **Abstract 已提交** (May 26)
14	✅ **全部 k=0.95 缺口实验已部署**
15	📝 **Paper Agent**: Provenance 83/83
16	✅ **cqa1 代码已修复** — transformers 4.40.1, eval 脚本 425 行同步完成
17	⚠️ **π0.5 全 cqa1 数据污染 (D248)** — cqa1 用 `done|reward>0.5` (宽松), westd 用 `done` (严格)。影响: Goal 全列 + Long k≤0.85。Object/Spatial 不受影响(全 westd)。Claim 5 核心证据(Object)安全
18	
19	## Deadlines
20	- **实验硬截止**: May 28 20:00 BJT (C002)
21	- **CoRL 2026 Paper**: May 29
22	
23	## OpenVLA Object Cliff Curve
24	| k | L2norm | Attn | Random | Baseline |
25	|---|--------|------|--------|----------|
26	| 0.95 | 70.6% | 🏃 westd-27271 | 67.4% | 74.0% |
27	| 0.9 | 70.6% | 61.4% | 62.8% | — |
28	| 0.85 | 55.2% | 55.0% | 60.4% | — |
29	| 0.75 | 57.4%† | 53.2% | 50.4% | — |
30	| 0.7 | 49.8% | 43.8% | 44.4% | — |
31	| 0.5 | 39.2% | 40.6% | 35.8% | — |
32	
33	## OpenVLA Goal Cliff Curve
34	| k | L2norm | Attn | Random | Baseline |
35	|---|--------|------|--------|----------|
36	| 0.95 | **75.2%** ✓ | 🏃 cqa1 | 🏃 cqa1 | 74.8% |
37	| 0.9 | 74.8% | 73.2% | 79.6% | — |
38	| 0.85 | 75.4% | 74.6% | 78.6% | — |
39	| 0.75 | 70.2% | 67.4% | 72.0% | — |
40	| 0.7 | 68.4% | 66.4% | 68.4% | — |
41	| 0.5 | 43.4% | 🏃 cqa1 | 52.2% | — |
42	
43	## OpenVLA Long Cliff Curve
44	| k | L2norm | Attn | Random | Baseline |
45	|---|--------|------|--------|----------|
46	| 0.95 | 🏃 westd-38929 | 🏃 westd-38929 | 🏃 westd-41074 | 52.8% |
47	| 0.9 | 43.6% | 44.0% | 46.8% | — |
48	| 0.85 | 38.8% | 45.8% | 45.0% | — |
49	| 0.75 | 🏃 westd-38929 (~12h) | 39.8%† | **43.0%** ✓ | — |
50	| 0.7 | 31.2% | 24.0% | 38.8% | — |
51	| 0.5 | 16.4% | 14.6% | 18.6% | — |
52	
53	## π0.5 Long Cliff Curve
54	| k | L2norm | Attn | Random |
55	|---|--------|------|--------|
56	| 0.95 | 87.0% | 77.0% | 63.2% |
57	| 0.9 | 81.0% | 63.8% | ~32% |
58	| 0.85 | 77.8% | 51.6% | **45.2%** strict ✓ |
59	| 0.75 | 73.4% | 51.8% | 62.4%⚠️ → 🏃 strict westd-41074 (~4h) |
60	| 0.7 | 63.2% | 50.8% | 62.4%⚠️ |
61	| 0.5 | 50.0% | 49.8% | 50.2%⚠️ |
62	⚠️ cqa1 宽松条件污染。strict 重跑进展: Random k=0.85=45.2%✓; Random k=0.75 🏃; Attn k=0.9/0.85/0.95 Long strict 部署中
63	
64	## 运行中实验
65	- westd-27271: Attn k=0.95 Object + L2norm k=0.95 Goal + GPU0 新任务
66	- westd-38929: L2norm k=0.95 Long + Attn k=0.95 Long + L2norm k=0.75 Long v2
67	- westd-41074: Random k=0.95 Long (GPU0) + π0.5 Random k=0.75 strict (GPU1) + GPU2/3 π0.5 Attn strict 部署中
68	- cqa1: Random k=0.95 Goal + Attn k=0.95 Goal + Attn k=0.5 Goal + GPU2 π0.5 strict
69	- **14/14 GPU running**
70	
71	## 近期任务
72	- [x] OpenVLA Random k=0.75 Long = 43.0% ✓
73	- [x] π0.5 Random k=0.85 Long strict = 45.2% ✓
74	- [ ] π0.5 Random k=0.75 Long strict (~4h, 验证 V-shape)
75	- [ ] 全部 k=0.95 endpoints 收齐
76	- [ ] OpenVLA Long L2norm k=0.75 v2 (~12h)
77	- [ ] π0.5 Attn strict reruns (k=0.9/0.85/0.95)
78	- [ ] 全部结果收齐 → Paper Agent 更新 figures
79	- [ ] May 28 20:00 实验截止 → May 29 论文提交
80	
81	## GPU 预算
82	14 张 GPU (4 servers), 14/14 running。
83	
84	## 关键决策日志
85	
86	| ID | 日期 | 摘要 | 关联实验 |
87	|----|------|------|----------|
88	| D249 | 2026-05-27 | Crossover table 最终呈现：主表保留 OpenVLA 全部 + π0.5 Object | — |
89	| D248 | 2026-05-27 | π0.5 污染范围扩大至全部 cqa1 实验（Object/Goal/Spatial/Long），但 | crossover_table, eval_pi05_random_k085_long_strict |
90	| D247 | 2026-05-27 | π0.5 Long k≤0.85 数据因 success 条件不一致被判定为污染，论文仅使用 k≥0 | eval_pi05_random_k085_long, eval_pi05_random_k09_long |
91	| D246 | 2026-05-26 | OpenVLA L2norm k=0.7 Goal SR=68.4%: Goal k=0.7 L2n | eval_openvla_l2norm_k07_goal_seed42 |
92	| D245 | 2026-05-26 | π0.5 Attn k=0.85 Long SR=51.6%: k=0.9→0.85 断崖 -12. | eval_pi05_attention_k085_long_seed42_v2 |
93	| D244 | 2026-05-26 | Attn k=0.5 Goal SR=44.2%: Goal k=0.5 三方法完成 — Rando | eval_openvla_attn_k05_goal_seed42 |
94	| D243 | 2026-05-26 | Random k=0.5 Object SR=35.8%: Object k=0.5 三方法收敛 ( | eval_openvla_random_k05_object_seed42_v3 |
95	| D242 | 2026-05-26 | OpenVLA Attn k=0.7 Object SR=43.8%: k=0.7 Object 三 | eval_openvla_attn_k07_object_seed42_v3 |
96	| D241 | 2026-05-26 | OpenVLA Random k=0.5 Long SR=18.6%: Long suite 极端压 | eval_openvla_random_k05_long_seed42_v2 |
97	| D240 | 2026-05-26 | 实验硬截止 5/28 20:00 BJT：只补论文 figure 必需的 cliff curve 数 | — |
98	
99	
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CSKSyPjwU1ArVKVao6zCww",
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "9e7f0b1d-1410-4a59-be49-f284063505ea"
}
```

</details>

---

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a1aea833ad9194404",
  "tool_use_id": "toolu_01CSKSyPjwU1ArVKVao6zCww",
  "status": "completed",
  "output_file": "",
  "summary": "Read ROADMAP for gaps",
  "usage": {
    "total_tokens": 21567,
    "tool_uses": 1,
    "duration_ms": 9664
  },
  "uuid": "c52dcde1-fabc-4d20-a751-88996c10c970",
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77"
}
```

---

### Tool result

_source line 43 · 2026-05-27T06:15:50.880Z_

<details><summary>↩ Tool result · `toolu_01CSKSyPjwU1ArVKVao6zCww`</summary>

```text
Based on the ROADMAP.md, here are the critical OpenVLA experiment gaps and high-priority TODO tasks:

## OpenVLA Missing Experiments (Ready for Deployment)

**Object Model - IMMEDIATE GAPS:**
1. **Attn k=0.95 Object** - Currently running (westd-27271) but results needed
2. **Random k=0.95 Object** - Missing entirely; required for full k=0.95 Object cliff curve

**Goal Model - NEAR COMPLETE:**
- Random k=0.95 Goal and Attn k=0.95 Goal actively running (cqa1), but need results collection
- Most k values are complete; waiting on k=0.95 endpoints

**Long Task - CRITICAL GAPS:**
1. **L2norm k=0.95 Long** - Running (westd-38929) but needs completion
2. **Attn k=0.95 Long** - Running but needs completion
3. **L2norm k=0.75 Long v2** - Running (~12h remaining) for validation

## High-Priority Tasks (Before 2026-05-28 20:00 BJT Deadline)

1. **Collect all k=0.95 Object, Goal, Long endpoints** - These are critical for cliff curve figures
2. **Complete Long L2norm k=0.75 v2 rerun** (~12h) - Validates proposed model improvements
3. **Finalize π0.5 Attn strict reruns** (k=0.9/0.85/0.95) - Currently deploying
4. **Aggregate all results** → Update paper figures before May 29 submission

## Current GPU Status
14/14 GPUs fully running across 4 servers. **Object model is available** on westd-27271 (Attn k=0.95 running) and westd-41074. If you have idle Object-enabled GPUs, the highest-priority missing experiment is **OpenVLA Random k=0.95 Object** (completes the k=0.95 cliff curve for Object task).

All experiments align with hard deadline of May 28 20:00 BJT for CoRL 2026 paper submission.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "0c6d5218-fc65-4052-b451-df5274e14077",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the ROADMAP.md file in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ and summarize the experiment gaps / high-priority tasks that are still TODO. I need to know what OpenVLA experiments are missing so I can deploy one on an idle GPU that has the Object model available. Report in under 300 words.",
    "agentId": "a1aea833ad9194404",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on the ROADMAP.md, here are the critical OpenVLA experiment gaps and high-priority TODO tasks:\n\n## OpenVLA Missing Experiments (Ready for Deployment)\n\n**Object Model - IMMEDIATE GAPS:**\n1. **Attn k=0.95 Object** - Currently running (westd-27271) but results needed\n2. **Random k=0.95 Object** - Missing entirely; required for full k=0.95 Object cliff curve\n\n**Goal Model - NEAR COMPLETE:**\n- Random k=0.95 Goal and Attn k=0.95 Goal actively running (cqa1), but need results collection\n- Most k values are complete; waiting on k=0.95 endpoints\n\n**Long Task - CRITICAL GAPS:**\n1. **L2norm k=0.95 Long** - Running (westd-38929) but needs completion\n2. **Attn k=0.95 Long** - Running but needs completion\n3. **L2norm k=0.75 Long v2** - Running (~12h remaining) for validation\n\n## High-Priority Tasks (Before 2026-05-28 20:00 BJT Deadline)\n\n1. **Collect all k=0.95 Object, Goal, Long endpoints** - These are critical for cliff curve figures\n2. **Complete Long L2norm k=0.75 v2 rerun** (~12h) - Validates proposed model improvements\n3. **Finalize π0.5 Attn strict reruns** (k=0.9/0.85/0.95) - Currently deploying\n4. **Aggregate all results** → Update paper figures before May 29 submission\n\n## Current GPU Status\n14/14 GPUs fully running across 4 servers. **Object model is available** on westd-27271 (Attn k=0.95 running) and westd-41074. If you have idle Object-enabled GPUs, the highest-priority missing experiment is **OpenVLA Random k=0.95 Object** (completes the k=0.95 cliff curve for Object task).\n\nAll experiments align with hard deadline of May 28 20:00 BJT for CoRL 2026 paper submission."
      }
    ],
    "totalDurationMs": 9668,
    "totalTokens": 22068,
    "totalToolUseCount": 1,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3715,
      "cache_read_input_tokens": 17830,
      "output_tokens": 518,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3715
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 518,
          "cache_read_input_tokens": 17830,
          "cache_creation_input_tokens": 3715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3715,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
So the available models on westd-27271:
- Goal model: `/root/autodl-tmp/openvla-7b-finetuned-libero-goal/` ✅
- Object model: `/root/autodl-tmp/openvla-libero-object/` ✅
- Long model: `/root/autodl-tmp/openvla-7b-finetuned-libero-10/` ✅
- Spatial model: `/root/autodl-tmp/openvla-7b-finetuned-libero-spatial/` ✅


The critical gap is the Random k=0.95 Object experiment, which would complete the k=0.95 curve for that task. I'm checking what's currently running and already completed to confirm it's not already in progress.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "9b26d05e-a851-4d39-ae83-5b548fc3c5af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsyY7R3VzUXkFCyx5MDepP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1749,
      "cache_read_input_tokens": 34313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1749
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

_source line 45_

所有模型都在 westd 上（Goal、Object、Long、Spatial）。最高优先级缺口: **OpenVLA Random k=0.95 Object**。

确认该实验不存在/未完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "05965550-b5b0-4b1f-a754-77a515f807a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsyY7R3VzUXkFCyx5MDepP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1749,
      "cache_read_input_tokens": 34313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1749
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

_source line 46_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01TN8xxZ79nKWG2Ftoz6AvgA`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "status",
    "metrics",
    "hypothesis"
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "f7b87479-0157-4f13-8996-f47be44cd1b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsyY7R3VzUXkFCyx5MDepP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1749,
      "cache_read_input_tokens": 34313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1749
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

_source line 47 · 2026-05-27T06:16:07.659Z_

<details><summary>↩ Tool result · `toolu_01TN8xxZ79nKWG2Ftoz6AvgA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_openvla_attn_k095_object_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.95 Object seed42 — Object Attn cliff curve 顶端缺口。Attn k=0.9=61.4%, k=0.85=55.0%, k=0.75=53.2%。k=0.95 补全曲线起始段，与 L2norm k=0.95=70.6% 和 Baseline=74.0% 形成对比\", \"metrics\": {\"overall_sr\": 71.2, \"per_task\": {\"T9_chocolate_pudding\": 66, \"T10_orange_juice\": 92}, \"time_min\": 238.2}}, \"eval_openvla_random_k095_object_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.95 Object seed42 — Object curve 顶端 Random 方法缺口。Random k=0.9=57.4%。k=0.95 补全 Object Random cliff curve 起始段，与 L2norm k=0.95=70.6% 形成对比\", \"metrics\": {\"overall_sr\": 67.4, \"per_task\": {\"T1_alphabet_soup\": 76, \"T2_cream_cheese\": 44, \"T3_salad_dressing\": 74, \"T4_bbq_sauce\": 48, \"T5_ketchup\": 78, \"T6_tomato_sauce\": 78, \"T7_butter\": 48, \"T8_milk\": 66, \"T9_chocolate_pudding\": 74, \"T10_orange_juice\": 88}, \"time_min\": 282.6}}, \"eval_openvla_random_k075_object_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.75 Object seed42 — Object cliff curve 中间点。Random k=0.85=61.4%(v2), k=0.7=44.4%。k=0.75 填补两者之间的下降斜率，与 Attn k=0.75(running) 对比三方法在 25% 压缩下的差异\", \"metrics\": {\"overall_sr\": 50.4, \"per_task\": {\"T1_alphabet_soup\": 40, \"T2_cream_cheese\": 40, \"T3_salad_dressing\": 64, \"T4_bbq_sauce\": 42, \"T5_ketchup\": 58, \"T6_tomato_sauce\": 52, \"T7_butter\": 38, \"T8_milk\": 56, \"T9_chocolate_pudding\": 46, \"T10_orange_juice\": 70}, \"time_min\": 297.3}}, \"eval_openvla_random_k075_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\", \"metrics\": {\"overall_sr\": 72, \"per_task\": {\"T1_open_middle_drawer\": 70, \"T2_bowl_on_stove\": 86, \"T3_wine_on_cabinet\": 70, \"T4_bowl_in_drawer\": 36, \"T5_bowl_on_cabinet\": 92, \"T6_plate_to_front\": 76, \"T7_cream_cheese_in_bowl\": 60, \"T8_turn_on_stove\": 100, \"T9_bowl_on_plate\": 74, \"T10_wine_on_rack\": 56}, \"time_min\": 228.8}}, \"eval_openvla_attn_k095_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.95 Goal seed42 — Goal Attn curve 顶端缺口。Attn k=0.9=73.2%, k=0.85=74.6%。k=0.95 补全曲线起始段\"}, \"eval_openvla_random_k075_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Random pruning at k=0.75 on OpenVLA Long suite serves as a baseline to quantify the importance margin of structured pruning methods over random token removal.\"}, \"eval_openvla_l2norm_k095_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.95 Goal seed42 — Goal curve 顶端三方法都缺。L2n k=0.9=74.8%。k=0.95 预期接近 baseline，补全 Goal cliff curve 起始段\", \"metrics\": {\"overall_sr\": 75.2, \"per_task\": {\"T1\": 96, \"T2\": 94, \"T3\": 82, \"T4\": 60, \"T5\": 88, \"T6\": 66, \"T7\": 54, \"T8\": 96, \"T9\": 82, \"T10\": 54}}}, \"eval_pi05_random_k085_long_seed42_strict_v2\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Random k=0.85 Long strict v2 — v1 因缺少 HF_HUB_OFFLINE=1 在 westd-41074 上失败(网络不可达)。本次添加离线模式环境变量。strict 条件(if done: only)重跑，修正 cqa1 宽松条件(done|reward>0.5)导致的数据污染。cqa1 SR=44.4%(宽松)\"}, \"eval_openvla_attn_k075_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Attention-based pruning at k=0.75 on OpenVLA (LIBERO-Long/10 tasks) maintains competitive success rate by retaining the most important 75% of vision tokens based on attention scores\", \"metrics\": {\"overall_sr\": 37.4, \"overall_sr_completed_tasks\": 39.8, \"completed_episodes\": 430, \"total_planned\": 500, \"total_success\": 161, \"per_task_sr\": {\"T1_alphabet_soup_tomato_sauce\": 38, \"T2_cream_cheese_butter\": 52, \"T3_stove_moka_pot\": 48, \"T4_bowl_in_drawer\": 34, \"T5_mugs_on_plates\": 18, \"T6_book_in_caddy\": 54, \"T7_mug_pudding\": 24, \"T8_soup_cream_cheese\": 50, \"T9_moka_pots_stove_PARTIAL\": 6.7}, \"per_task_success\": {\"T1\": \"19/50\", \"T2\": \"26/50\", \"T3\": \"24/50\", \"T4\": \"17/50\", \"T5\": \"9/50\", \"T6\": \"27/50\", \"T7\": \"12/50\", \"T8\": \"25/50\", \"T9\": \"2/30 (partial)\", \"T10\": \"not started\"}}}, \"eval_pi05_random_k085_long_seed42_strict\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Random k=0.85 Long seed42 严格条件重跑 — 使用 westd-41074 V-B 代码(426行, `if done:` strict)。修正 cqa1 V-C 宽松条件(done|reward>0.5)导致的数据污染。cqa1 SR=44.4%(宽松), 此实验为严格条件下的真实值\"}, \"eval_pi05_random_k07_long_seed42\": {\"hypothesis\": \"Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估\", \"status\": \"DONE\", \"metrics\": {\"overall_sr\": 62.4, \"suite\": \"libero_10\", \"prune_method\": \"random\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_l2norm_k085_long_seed42\": {\"hypothesis\": \"π0.5 L2norm k=0.85 on LIBERO-Long (libero_10): 15% token removal on 520-step horizon tasks. Object k=0.85=98.0%. Testing if Long suite shows similar resilience or begins to degrade.\", \"metrics\": {\"elapsed_min\": 133.4, \"keep_ratio\": 0.85, \"num_episodes\": 500, \"num_success\": 390, \"prune_mode\": \"l2norm\", \"seed\": 42, \"success_rate\": 0.78, \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_openvla_attn_k075_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Attention-based pruning at k=0.75 on OpenVLA Goal suite will retain task performance by preserving the most important attention heads for goal-conditioned manipulation tasks.\", \"metrics\": {\"overall_sr\": 67.4, \"suite\": \"libero_goal\", \"prune_method\": \"attention\", \"keep_ratio\": 0.75, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_l2norm_k05_long_seed42_v4\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 L2norm k=0.5 Long seed42 v4 — 重跑。L2norm k=0.5 在 libero_10 上的 50% 压缩性能评估\", \"metrics\": {\"overall_sr\": 50, \"total_successes\": 250, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 66, \"T1_cream_cheese_butter\": 52, \"T2_stove_moka_pot\": 74, \"T3_black_bowl_drawer\": 38, \"T4_white_mug_left_plate\": 30, \"T5_book_back_shelf\": 50, \"T6_white_mug_plate\": 32, \"T7_alphabet_soup_cream\": 60, \"T8_moka_pots_stove\": 16, \"T9_yellow_mug_microwave\": 82}, \"elapsed_minutes\": 249.4, \"seed\": 42}}, \"eval_pi05_l2norm_k085_long_seed42_v4\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 L2norm k=0.85 Long seed42 — L2norm Long curve 唯一缺口。L2norm k=0.9=81.0%, k=0.75=73.4%。k=0.85 补全 L2norm 完美单调曲线(D237)\", \"metrics\": {\"overall_sr\": 77.8, \"suite\": \"libero_10\", \"prune_method\": \"l2norm\", \"keep_ratio\": 0.85, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_attention_k07_long_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Attention k=0.7 Long seed42 v2 — Attn Long cliff curve 中间点。Attn k=0.75=51.8%, k=0.5=49.4%。k=0.7 补全 Attn Long curve\", \"metrics\": {\"overall_sr\": 50.8, \"per_task\": {\"T0_alphabet_soup_tomato\": 72, \"T1_cream_cheese_butter\": 70, \"T2_stove_moka_pot\": 58, \"T3_black_bowl_drawer\": 46, \"T4_white_mug_plate\": 36, \"T5_book_back\": 32, \"T6_mug_plate_yellow\": 58, \"T7_alphabet_soup_cream\": 48, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 82}, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_attention_k075_long_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Attention k=0.75 Long seed42 v2 — cliff curve k=0.75 三方法对比。Attn k=0.9=63.8%。重跑：v1 因缺 offline flags 崩溃\", \"metrics\": {\"overall_sr\": 52.4, \"task_sr\": {\"T0_alphabet_soup_tomato\": 68, \"T1_cream_cheese_butter\": 78, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 48, \"T4_white_mug_left_plate\": 26, \"T5_book_back_compartment\": 50, \"T6_white_mug_plate\": 76, \"T7_alphabet_soup_cream\": 30, \"T8_both_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 78}}}, \"eval_pi05_attention_k05_long_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Attention k=0.5 Long seed42 v2 — 重跑。Attn Long cliff curve 极端压缩点。Attn k=0.9=63.8%, k=0.75=51.8%。v1 被误判 failed 但有 SR=49.4%，本次重新验证\", \"metrics\": {\"overall_sr\": 49.8, \"task_sr\": {\"T0_alphabet_soup_tomato\": 74, \"T1_cream_cheese_butter\": 46, \"T2_stove_moka_pot\": 60, \"T3_black_bowl_drawer\": 70, \"T4_white_mug_left_plate\": 46, \"T5_book_back_shelf\": 52, \"T6_white_mug_plate\": 10, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 18, \"T9_yellow_white_mug_microwave\": 68}}}, \"eval_pi05_attention_k085_long_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Attention k=0.85 Long seed42 — Attn Long cliff curve 中间点。Attn k=0.9=63.8%, k=0.75=51.8%。k=0.85 填补两者之间数据缺口（v1 进程静默死亡，v2 改用绝对路径 python 重试）\", \"metrics\": {\"overall_sr\": 51.6, \"total_episodes\": 500, \"per_task\": {\"T0_alphabet_soup_tomato\": 20, \"T1_cream_cheese_butter\": 54, \"T2_stove_moka_pot\": 32, \"T3_black_bowl_drawer\": 60, \"T4_white_mug_left_plate\": 48, \"T5_book_back_shelf\": 90, \"T6_white_mug_plate\": 68, \"T7_alphabet_soup_cream\": 46, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 92}}}, \"eval_pi05_random_k05_long_seed42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Random k=0.5 Long seed42 v3 — 重跑。Random k=0.5 在 libero_10 上的 50% 压缩性能评估\", \"metrics\": {\"overall_sr\": 50.2, \"total_successes\": 251, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 84, \"T1_cream_cheese_butter\": 32, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 72, \"T4_white_mug_left_plate\": 74, \"T5_book_back_shelf\": 38, \"T6_white_mug_plate\": 30, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 4, \"T9_yellow_mug_microwave\": 50}, \"elapsed_minutes\": 252.3, \"seed\": 42}}, \"eval_pi05_random_k075_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 62.4, \"suite\": \"libero_10\", \"tasks_completed\": 10, \"total_episodes\": 500}, \"hypothesis\": \"π0.5 Random k=0.75 Long seed42 v2 — cliff curve 补充点。Random k=0.9=63.8%。k=0.75 测试 Random 在 25% 压缩下 libero_10 的性能衰退速度\"}, \"eval_pi05_random_k085_long_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Random k=0.85 Long seed42 v2 — 重跑验证。v1 结果 SR=44.4%（negative），与 L2norm k=0.75=73.4% 差距过大，需确认是否正确\", \"metrics\": {\"overall_sr\": 44.4, \"total_success\": 222, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 52, \"T1_cream_cheese_butter\": 46, \"T2_stove_moka_pot\": 58, \"T3_black_bowl_drawer\": 74, \"T4_white_mug_left_plate\": 12, \"T5_book_back_shelf\": 32, \"T6_white_mug_plate\": 42, \"T7_alphabet_soup_cream\": 44, \"T8_moka_pots_stove\": 10, \"T9_yellow_white_mug_microwave\": 74}, \"runtime_min\": 267.8}}, \"eval_openvla_random_k095_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.95 Goal seed42 — Goal Random curve 顶端缺口。Random k=0.9=79.6%, k=0.85=78.6%。k=0.95 补全曲线起始段\"}, \"eval_openvla_attn_k075_goal_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attn k=0.75 Goal seed42 重跑 — v1 process dead 失败。Goal Attn cliff curve: k=0.9=73.2%, k=0.85=74.6%, k=0.7=66.4%。k=0.75 精确定位 cliff 下降起点\"}, \"eval_openvla_attn_k05_goal_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.5 Goal seed42 — Goal Attn cliff curve 极端压缩端点。测试 50% 压缩下 Attention pruning 在 Goal suite 的性能下限\"}, \"eval_openvla_random_k05_object_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.5 Object seed42 — Random pruning 极端压缩在 LIBERO-Object 上的性能下限\"}, \"eval_openvla_l2norm_k075_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.75 Long seed42 — L2norm pruning k=0.75 在 LIBERO-10 上的性能，Long cliff curve 数据点\"}, \"eval_openvla_attn_k07_long_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.7 Long seed42 — Attention pruning k=0.7 在 LIBERO-10 上的性能，Long cliff curve 中间点\", \"metrics\": {\"success_rate\": 24, \"total_successes\": 120, \"total_episodes\": 500}}, \"eval_openvla_attn_k05_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.5 Long seed42 — Attention pruning 极端压缩(保留50% tokens)在 LIBERO-10 上的性能下限，测试 attention cliff curve 最低点\", \"metrics\": {\"overall_sr\": 14.6, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.5, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_openvla_l2norm_k05_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.5 Long seed42 — Long L2norm cliff curve 极端压缩点。L2norm k=0.9=43.6%, k=0.85=38.8%, k=0.7=31.2%。k=0.5 测试 50% 压缩下的性能下限\"}, \"eval_openvla_random_k085_long_seed42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.85 Long — cliff curve 中间点。Random k=0.9=46.8%, k=0.7=38.8%。k=0.85 精确定位 Long suite cliff 位置\", \"metrics\": {\"overall_sr\": 0.45, \"n_episodes\": 500, \"task_sr\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0.6, \"put_both_cream_cheese_and_butter_in_basket\": 0.64, \"turn_on_stove_put_moka_pot\": 0.6, \"put_black_bowl_in_bottom_drawer\": 0.32, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.2, \"pick_up_book_place_in_caddy\": 0.76, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.3, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0.6, \"put_both_moka_pots_on_stove\": 0.32, \"put_yellow_white_mug_in_microwave\": 0.16}}}, \"eval_openvla_random_k05_goal_seed42\": {\"hypothesis\": \"OpenVLA Random k=0.5 Goal seed42 — Goal Random cliff curve 底端缺口。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.5 测试 50% 极端压缩下 Goal suite 性能下限\", \"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.522, \"total_successes\": 261, \"total_episodes\": 500}}, \"eval_pi05_attn_k095_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Attention k=0.95 Long seed42 — Attn Long cliff curve 顶端点。Attn k=0.9=63.8%, k=0.85=51.6%（cliff 在 0.85-0.9 间）。k=0.95 补全 Attn 曲线起始段，与 L2norm k=0.95=87% 和 Random k=0.95=63.2% 形成三方法对比\", \"metrics\": {\"overall_sr\": 77, \"n_episodes\": 500, \"task_sr\": {\"T0\": null, \"T1\": null, \"T2\": null, \"T3\": null, \"T4\": null, \"T5\": null, \"T6\": 14, \"T7\": 80, \"T8\": 30, \"T9\": 98}}}, \"eval_openvla_l2norm_k075_goal_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.75 Goal seed42 v2 — Goal cliff curve 加密点（v1 因 python not found 失败，改用 /root/miniconda3/bin/python）。L2norm k=0.9=74.8%, k=0.85=75.4%, k=0.7=68.4%。k=0.75 填补 k=0.85→0.7 下降斜率\", \"metrics\": {\"overall_sr\": 70.2, \"task_srs\": [54, 80, 86, 22, 88, 70, 68, 98, 82, 54], \"episodes\": 500, \"tasks\": 10, \"time_min\": 198, \"tokens_256_to_192\": true}}, \"eval_openvla_attn_k085_long_seed42_v5\": {\"status\": \"DONE\", \"hypothesis\": \"Attention-based pruning at k=0.85 on Long suite will show whether attention scoring preserves task-critical tokens for long-horizon manipulation, establishing the Attn cliff curve point between k=0.9 (known) and k=0.75 (TBD)\", \"metrics\": {\"overall_sr\": 45.8, \"task_srs\": [60, 58, 56, 34, 38, 66, 34, 66, 24, 22], \"episodes\": 500, \"tasks\": 10, \"time_min\": 548.6, \"tokens_256_to_217\": true}}, \"eval_openvla_attn_k075_object_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.75 Object seed42 — Object Attn cliff curve 中间点。Attn k=0.9=61.4%, k=0.85=55.0%, k=0.7=43.8%。k=0.75 精确定位 Attention pruning 在 Object suite 上的 cliff 位置，区分平缓退化还是断崖式下降\", \"metrics\": {\"overall_sr\": 53.2, \"total_success\": 266, \"total_episodes\": 500, \"per_task_sr\": {\"alphabet_soup\": 56, \"cream_cheese\": 28, \"salad_dressing\": 70, \"bbq_sauce\": 34, \"ketchup\": 76, \"tomato_sauce\": 30, \"butter\": 28, \"milk\": 54, \"chocolate_pudding\": 86, \"orange_juice\": 70}, \"eval_time_min\": 272}}, \"eval_pi05_l2norm_k075_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 L2norm k=0.75 Long seed42 — cliff curve k=0.75 三方法对比。L2norm k=0.9=81%, k=0.5 在跑。重跑：之前因缺 offline flags 崩溃\", \"metrics\": {\"overall_sr\": 73.4, \"per_task\": {\"T0_soup_tomato\": 96, \"T1_cream_butter\": 94, \"T2_stove_moka\": 82, \"T3_bowl_drawer\": 70, \"T4_mug_plate\": 68, \"T5_book_back\": 84, \"T6_mug_plate_tomato\": 52, \"T7_soup_cream\": 76, \"T8_moka_pots\": 28, \"T9_mug_microwave\": 84}}}, \"eval_pi05_l2norm_k05_spatial_seed42_postfix\": {\"hypothesis\": \"π0.5 L2norm k=0.5 Spatial seed42 post-fix — L2norm Spatial 曲线缺口。L2norm k=0.85 Spatial=88.4%。验证 L2norm importance scoring 在 50% keep ratio 下的 Spatial 表现\", \"metrics\": {\"elapsed_min\": 149.18, \"overall_sr\": 0.574, \"per_task_sr\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.8, \"pick_up_black_bowl_from_table_center\": 0.9, \"pick_up_black_bowl_in_top_drawer\": 0.32, \"pick_up_black_bowl_next_to_cookie_box\": 0.28, \"pick_up_black_bowl_next_to_plate\": 0.74, \"pick_up_black_bowl_next_to_ramekin\": 0.9, \"pick_up_black_bowl_on_cookie_box\": 0.26, \"pick_up_black_bowl_on_ramekin\": 0.34, \"pick_up_black_bowl_on_stove\": 0.76, \"pick_up_black_bowl_on_wooden_cabinet\": 0.44}, \"total_episodes\": 500, \"total_successes\": 287}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed43_postfix\": {\"hypothesis\": \"π0.5 Random k=0.85 Long seed43 postfix — dual-seed Random Long cliff zone 验证。k=0.85 是 Object suite 上 Random disruption peak。验证 Long suite 是否同样存在 cliff\", \"metrics\": {\"overall_sr\": 0.418, \"total_episodes\": 500, \"total_successes\": 209}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed42_postfix\": {\"hypothesis\": \"π0.5 L2norm k=0.3 Long post-fix — L2norm Long curve extreme pruning endpoint。Pre-fix k=0.3 Long 已有数据。Random k=0.3 Long postfix 正在跑。补全 L2norm Long disruption curve 的极端端，与 Random k=0.3 对比验证 importance margin 在极端 pruning 下是否仍存在\", \"metrics\": {\"overall_sr\": 0.366, \"total_episodes\": 500, \"total_successes\": 183}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_long_seed43_postfix\": {\"hypothesis\": \"π0.5 Random k=0.9 Long seed43 postfix — dual-seed Random Long curve near-full retention。seed42 k=0.9 已有结果。验证 90% retention 下 random pruning 的 seed 稳定性\", \"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.356, \"total_episodes\": 500, \"total_successes\": 178}}, \"eval_openvla_random_k085_object_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.85 Object seed42 — Object cliff curve 中间点。Random k=0.9=62.8%, k=0.7=44.4%。k=0.85 与 L2norm(55.2%) 和 Attn(55.0%) 在 k=0.85 处三方法对比\"}, \"eval_pi05_l2norm_k085_long_seed42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 L2norm k=0.85 Long seed42 — L2norm Long 单调曲线缺失点。k=0.9=81%, k=0.75=73.4%。k=0.85 确认下降斜率，验证 D237 position encoding sensitivity 假设中 L2norm 的平滑退化特性\", \"metrics\": {\"overall_sr\": 78.8, \"total_episodes\": 500, \"total_successes\": 394, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 98, \"T1_cream_cheese_butter\": 94, \"T2_stove_moka_pot\": 88, \"T3_black_bowl_drawer\": 98, \"T4_white_mug_left_plate\": 72, \"T5_book_back\": 98, \"T6_white_mug_plate\": 6, \"T7_alphabet_soup_cream\": 86, \"T8_moka_pots_stove\": 54, \"T9_yellow_white_mug_microwave\": 94}}}, \"eval_openvla_l2norm_k075_object_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.75 Object seed42 — Object L2norm cliff curve 中间点。L2norm k=0.95=70.6%, k=0.9=70.6%, k=0.85=?。k=0.75 测试更深压缩下 Object 的降级模式\", \"metrics\": {\"overall_sr\": 0.574, \"total_episodes\": 500, \"successful_episodes\": 287, \"task_sr\": {\"alphabet_soup\": 0.78, \"cream_cheese\": 0.28, \"salad_dressing\": 0.68, \"bbq_sauce\": 0.46, \"ketchup\": 0.86, \"tomato_sauce\": 0.66, \"butter\": 0.4, \"milk\": 0.48, \"chocolate_pudding\": 0.46, \"orange_juice\": 0.68}, \"time_min\": 289.4}}, \"eval_openvla_attn_k07_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attn k=0.7 Goal seed42 — Goal Attn cliff curve 进一步压缩。Attn k=0.9=73.2%, k=0.85=74.6%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"metrics\": {\"overall_sr\": 0.664, \"total_episodes\": 500, \"total_successes\": 332}}, \"eval_openvla_l2norm_k075_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.75 Goal seed42 — Goal cliff curve 加密点。L2norm k=0.9=74.8%, k=0.85=75.4%, k=0.7=68.4%, k=0.5=43.4%。k=0.75 填补 k=0.85→0.7 之间的下降斜率（75.4%→68.4%=-7pp），判断是平滑退化还是存在 cliff\"}, \"eval_openvla_l2norm_k07_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.7 Goal seed42 — Goal cliff curve 进一步压缩。L2norm k=0.9=75.2%, k=0.85=75.4%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"metrics\": {\"overall_sr\": 0.684, \"total_episodes\": 500, \"per_task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_bowl_on_the_stove\": 0.86, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.74, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.16, \"put_the_bowl_on_top_of_the_cabinet\": 0.84, \"push_the_plate_to_the_front_of_the_stove\": 0.66, \"put_the_cream_cheese_in_the_bowl\": 0.74, \"turn_on_the_stove\": 0.98, \"put_the_bowl_on_the_plate\": 0.7, \"put_the_wine_bottle_on_the_rack\": 0.56}}}, \"eval_openvla_attn_k05_goal_seed42\": {\"hypothesis\": \"OpenVLA Attention k=0.5 Goal — cliff curve extreme endpoint. Attn k=0.9 Goal=73.2%, k=0.85=74.6%. k=0.5 tests 50% compression limit for attention pruning on Goal suite\", \"status\": \"DONE\", \"metrics\": {\"overall_sr\": 44.2, \"total_episodes\": 500, \"total_successes\": 221, \"source\": \"result file found on westd-27271 by audit worker, needs verification\"}}, \"eval_openvla_attn_k07_object_seed42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.7 Object v3 — v2进程PID 542010仍在运行（已过Task 7崩溃点）。带stderr捕获继续跑完。Attn Object cliff curve: k=0.9=61.4%, k=0.85=55.0%, k=0.7=?\", \"metrics\": {\"overall_sr\": 43.8, \"total_episodes\": 500, \"total_successes\": 219}}, \"eval_openvla_random_k05_object_seed42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.5 Object — cliff curve extreme endpoint. Random k=0.9=62.8%, k=0.7=44.4%. k=0.5 tests 50% compression limit for random pruning on Object suite\", \"metrics\": {\"overall_sr\": 35.8, \"total_episodes\": 500, \"total_successes\": 179, \"per_task\": {\"alphabet_soup\": 56, \"bbq_sauce\": 58, \"butter\": 0, \"chocolate_pudding\": 30, \"cream_cheese\": 2, \"ketchup\": 60, \"milk\": 12, \"orange_juice\": 74, \"salad_dressing\": 40, \"tomato_sauce\": 26}}}}, \"count\": 50, \"total\": 750, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8604}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "e74acd90-27d3-45c2-b9dc-a48119d5795d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_openvla_attn_k095_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Attention k=0.95 Object seed42 — Object Attn cliff curve 顶端缺口。Attn k=0.9=61.4%, k=0.85=55.0%, k=0.75=53.2%。k=0.95 补全曲线起始段，与 L2norm k=0.95=70.6% 和 Baseline=74.0% 形成对比\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 71.2, \\\"per_task\\\": {\\\"T9_chocolate_pudding\\\": 66, \\\"T10_orange_juice\\\": 92}, \\\"time_min\\\": 238.2}}, \\\"eval_openvla_random_k095_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.95 Object seed42 — Object curve 顶端 Random 方法缺口。Random k=0.9=57.4%。k=0.95 补全 Object Random cliff curve 起始段，与 L2norm k=0.95=70.6% 形成对比\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 67.4, \\\"per_task\\\": {\\\"T1_alphabet_soup\\\": 76, \\\"T2_cream_cheese\\\": 44, \\\"T3_salad_dressing\\\": 74, \\\"T4_bbq_sauce\\\": 48, \\\"T5_ketchup\\\": 78, \\\"T6_tomato_sauce\\\": 78, \\\"T7_butter\\\": 48, \\\"T8_milk\\\": 66, \\\"T9_chocolate_pudding\\\": 74, \\\"T10_orange_juice\\\": 88}, \\\"time_min\\\": 282.6}}, \\\"eval_openvla_random_k075_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.75 Object seed42 — Object cliff curve 中间点。Random k=0.85=61.4%(v2), k=0.7=44.4%。k=0.75 填补两者之间的下降斜率，与 Attn k=0.75(running) 对比三方法在 25% 压缩下的差异\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 50.4, \\\"per_task\\\": {\\\"T1_alphabet_soup\\\": 40, \\\"T2_cream_cheese\\\": 40, \\\"T3_salad_dressing\\\": 64, \\\"T4_bbq_sauce\\\": 42, \\\"T5_ketchup\\\": 58, \\\"T6_tomato_sauce\\\": 52, \\\"T7_butter\\\": 38, \\\"T8_milk\\\": 56, \\\"T9_chocolate_pudding\\\": 46, \\\"T10_orange_juice\\\": 70}, \\\"time_min\\\": 297.3}}, \\\"eval_openvla_random_k075_goal_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 72, \\\"per_task\\\": {\\\"T1_open_middle_drawer\\\": 70, \\\"T2_bowl_on_stove\\\": 86, \\\"T3_wine_on_cabinet\\\": 70, \\\"T4_bowl_in_drawer\\\": 36, \\\"T5_bowl_on_cabinet\\\": 92, \\\"T6_plate_to_front\\\": 76, \\\"T7_cream_cheese_in_bowl\\\": 60, \\\"T8_turn_on_stove\\\": 100, \\\"T9_bowl_on_plate\\\": 74, \\\"T10_wine_on_rack\\\": 56}, \\\"time_min\\\": 228.8}}, \\\"eval_openvla_attn_k095_goal_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Attention k=0.95 Goal seed42 — Goal Attn curve 顶端缺口。Attn k=0.9=73.2%, k=0.85=74.6%。k=0.95 补全曲线起始段\\\"}, \\\"eval_openvla_random_k075_long_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Random pruning at k=0.75 on OpenVLA Long suite serves as a baseline to quantify the importance margin of structured pruning methods over random token removal.\\\"}, \\\"eval_openvla_l2norm_k095_goal_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.95 Goal seed42 — Goal curve 顶端三方法都缺。L2n k=0.9=74.8%。k=0.95 预期接近 baseline，补全 Goal cliff curve 起始段\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 75.2, \\\"per_task\\\": {\\\"T1\\\": 96, \\\"T2\\\": 94, \\\"T3\\\": 82, \\\"T4\\\": 60, \\\"T5\\\": 88, \\\"T6\\\": 66, \\\"T7\\\": 54, \\\"T8\\\": 96, \\\"T9\\\": 82, \\\"T10\\\": 54}}}, \\\"eval_pi05_random_k085_long_seed42_strict_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 Random k=0.85 Long strict v2 — v1 因缺少 HF_HUB_OFFLINE=1 在 westd-41074 上失败(网络不可达)。本次添加离线模式环境变量。strict 条件(if done: only)重跑，修正 cqa1 宽松条件(done|reward>0.5)导致的数据污染。cqa1 SR=44.4%(宽松)\\\"}, \\\"eval_openvla_attn_k075_long_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Attention-based pruning at k=0.75 on OpenVLA (LIBERO-Long/10 tasks) maintains competitive success rate by retaining the most important 75% of vision tokens based on attention scores\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 37.4, \\\"overall_sr_completed_tasks\\\": 39.8, \\\"completed_episodes\\\": 430, \\\"total_planned\\\": 500, \\\"total_success\\\": 161, \\\"per_task_sr\\\": {\\\"T1_alphabet_soup_tomato_sauce\\\": 38, \\\"T2_cream_cheese_butter\\\": 52, \\\"T3_stove_moka_pot\\\": 48, \\\"T4_bowl_in_drawer\\\": 34, \\\"T5_mugs_on_plates\\\": 18, \\\"T6_book_in_caddy\\\": 54, \\\"T7_mug_pudding\\\": 24, \\\"T8_soup_cream_cheese\\\": 50, \\\"T9_moka_pots_stove_PARTIAL\\\": 6.7}, \\\"per_task_success\\\": {\\\"T1\\\": \\\"19/50\\\", \\\"T2\\\": \\\"26/50\\\", \\\"T3\\\": \\\"24/50\\\", \\\"T4\\\": \\\"17/50\\\", \\\"T5\\\": \\\"9/50\\\", \\\"T6\\\": \\\"27/50\\\", \\\"T7\\\": \\\"12/50\\\", \\\"T8\\\": \\\"25/50\\\", \\\"T9\\\": \\\"2/30 (partial)\\\", \\\"T10\\\": \\\"not started\\\"}}}, \\\"eval_pi05_random_k085_long_seed42_strict\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 Random k=0.85 Long seed42 严格条件重跑 — 使用 westd-41074 V-B 代码(426行, `if done:` strict)。修正 cqa1 V-C 宽松条件(done|reward>0.5)导致的数据污染。cqa1 SR=44.4%(宽松), 此实验为严格条件下的真实值\\\"}, \\\"eval_pi05_random_k07_long_seed42\\\": {\\\"hypothesis\\\": \\\"Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估\\\", \\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 62.4, \\\"suite\\\": \\\"libero_10\\\", \\\"prune_method\\\": \\\"random\\\", \\\"keep_ratio\\\": 0.7, \\\"seed\\\": 42, \\\"episodes_per_task\\\": 50}}, \\\"eval_pi05_l2norm_k085_long_seed42\\\": {\\\"hypothesis\\\": \\\"π0.5 L2norm k=0.85 on LIBERO-Long (libero_10): 15% token removal on 520-step horizon tasks. Object k=0.85=98.0%. Testing if Long suite shows similar resilience or begins to degrade.\\\", \\\"metrics\\\": {\\\"elapsed_min\\\": 133.4, \\\"keep_ratio\\\": 0.85, \\\"num_episodes\\\": 500, \\\"num_success\\\": 390, \\\"prune_mode\\\": \\\"l2norm\\\", \\\"seed\\\": 42, \\\"success_rate\\\": 0.78, \\\"suite\\\": \\\"libero_10\\\"}, \\\"status\\\": \\\"DONE\\\"}, \\\"eval_openvla_attn_k075_goal_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Attention-based pruning at k=0.75 on OpenVLA Goal suite will retain task performance by preserving the most important attention heads for goal-conditioned manipulation tasks.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 67.4, \\\"suite\\\": \\\"libero_goal\\\", \\\"prune_method\\\": \\\"attention\\\", \\\"keep_ratio\\\": 0.75, \\\"seed\\\": 42, \\\"episodes_per_task\\\": 50}}, \\\"eval_pi05_l2norm_k05_long_seed42_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 L2norm k=0.5 Long seed42 v4 — 重跑。L2norm k=0.5 在 libero_10 上的 50% 压缩性能评估\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 50, \\\"total_successes\\\": 250, \\\"total_episodes\\\": 500, \\\"per_task_sr\\\": {\\\"T0_alphabet_soup_tomato\\\": 66, \\\"T1_cream_cheese_butter\\\": 52, \\\"T2_stove_moka_pot\\\": 74, \\\"T3_black_bowl_drawer\\\": 38, \\\"T4_white_mug_left_plate\\\": 30, \\\"T5_book_back_shelf\\\": 50, \\\"T6_white_mug_plate\\\": 32, \\\"T7_alphabet_soup_cream\\\": 60, \\\"T8_moka_pots_stove\\\": 16, \\\"T9_yellow_mug_microwave\\\": 82}, \\\"elapsed_minutes\\\": 249.4, \\\"seed\\\": 42}}, \\\"eval_pi05_l2norm_k085_long_seed42_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 L2norm k=0.85 Long seed42 — L2norm Long curve 唯一缺口。L2norm k=0.9=81.0%, k=0.75=73.4%。k=0.85 补全 L2norm 完美单调曲线(D237)\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 77.8, \\\"suite\\\": \\\"libero_10\\\", \\\"prune_method\\\": \\\"l2norm\\\", \\\"keep_ratio\\\": 0.85, \\\"seed\\\": 42, \\\"episodes_per_task\\\": 50}}, \\\"eval_pi05_attention_k07_long_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 Attention k=0.7 Long seed42 v2 — Attn Long cliff curve 中间点。Attn k=0.75=51.8%, k=0.5=49.4%。k=0.7 补全 Attn Long curve\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 50.8, \\\"per_task\\\": {\\\"T0_alphabet_soup_tomato\\\": 72, \\\"T1_cream_cheese_butter\\\": 70, \\\"T2_stove_moka_pot\\\": 58, \\\"T3_black_bowl_drawer\\\": 46, \\\"T4_white_mug_plate\\\": 36, \\\"T5_book_back\\\": 32, \\\"T6_mug_plate_yellow\\\": 58, \\\"T7_alphabet_soup_cream\\\": 48, \\\"T8_moka_pots_stove\\\": 6, \\\"T9_yellow_white_mug_microwave\\\": 82}, \\\"suite\\\": \\\"libero_10\\\", \\\"prune_method\\\": \\\"attention\\\", \\\"keep_ratio\\\": 0.7, \\\"seed\\\": 42, \\\"episodes_per_task\\\": 50}}, \\\"eval_pi05_attention_k075_long_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 Attention k=0.75 Long seed42 v2 — cliff curve k=0.75 三方法对比。Attn k=0.9=63.8%。重跑：v1 因缺 offline flags 崩溃\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 52.4, \\\"task_sr\\\": {\\\"T0_alphabet_soup_tomato\\\": 68, \\\"T1_cream_cheese_butter\\\": 78, \\\"T2_stove_moka_pot\\\": 64, \\\"T3_black_bowl_drawer\\\": 48, \\\"T4_white_mug_left_plate\\\": 26, \\\"T5_book_back_compartment\\\": 50, \\\"T6_white_mug_plate\\\": 76, \\\"T7_alphabet_soup_cream\\\": 30, \\\"T8_both_moka_pots_stove\\\": 6, \\\"T9_yellow_white_mug_microwave\\\": 78}}}, \\\"eval_pi05_attention_k05_long_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 Attention k=0.5 Long seed42 v2 — 重跑。Attn Long cliff curve 极端压缩点。Attn k=0.9=63.8%, k=0.75=51.8%。v1 被误判 failed 但有 SR=49.4%，本次重新验证\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 49.8, \\\"task_sr\\\": {\\\"T0_alphabet_soup_tomato\\\": 74, \\\"T1_cream_cheese_butter\\\": 46, \\\"T2_stove_moka_pot\\\": 60, \\\"T3_black_bowl_drawer\\\": 70, \\\"T4_white_mug_left_plate\\\": 46, \\\"T5_book_back_shelf\\\": 52, \\\"T6_white_mug_plate\\\": 10, \\\"T7_alphabet_soup_cream\\\": 54, \\\"T8_moka_pots_stove\\\": 18, \\\"T9_yellow_white_mug_microwave\\\": 68}}}, \\\"eval_pi05_attention_k085_long_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 Attention k=0.85 Long seed42 — Attn Long cliff curve 中间点。Attn k=0.9=63.8%, k=0.75=51.8%。k=0.85 填补两者之间数据缺口（v1 进程静默死亡，v2 改用绝对路径 python 重试）\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 51.6, \\\"total_episodes\\\": 500, \\\"per_task\\\": {\\\"T0_alphabet_soup_tomato\\\": 20, \\\"T1_cream_cheese_butter\\\": 54, \\\"T2_stove_moka_pot\\\": 32, \\\"T3_black_bowl_drawer\\\": 60, \\\"T4_white_mug_left_plate\\\": 48, \\\"T5_book_back_shelf\\\": 90, \\\"T6_white_mug_plate\\\": 68, \\\"T7_alphabet_soup_cream\\\": 46, \\\"T8_moka_pots_stove\\\": 6, \\\"T9_yellow_white_mug_microwave\\\": 92}}}, \\\"eval_pi05_random_k05_long_seed42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 Random k=0.5 Long seed42 v3 — 重跑。Random k=0.5 在 libero_10 上的 50% 压缩性能评估\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 50.2, \\\"total_successes\\\": 251, \\\"total_episodes\\\": 500, \\\"per_task_sr\\\": {\\\"T0_alphabet_soup_tomato\\\": 84, \\\"T1_cream_cheese_butter\\\": 32, \\\"T2_stove_moka_pot\\\": 64, \\\"T3_black_bowl_drawer\\\": 72, \\\"T4_white_mug_left_plate\\\": 74, \\\"T5_book_back_shelf\\\": 38, \\\"T6_white_mug_plate\\\": 30, \\\"T7_alphabet_soup_cream\\\": 54, \\\"T8_moka_pots_stove\\\": 4, \\\"T9_yellow_mug_microwave\\\": 50}, \\\"elapsed_minutes\\\": 252.3, \\\"seed\\\": 42}}, \\\"eval_pi05_random_k075_long_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"success_rate\\\": 62.4, \\\"suite\\\": \\\"libero_10\\\", \\\"tasks_completed\\\": 10, \\\"total_episodes\\\": 500}, \\\"hypothesis\\\": \\\"π0.5 Random k=0.75 Long seed42 v2 — cliff curve 补充点。Random k=0.9=63.8%。k=0.75 测试 Random 在 25% 压缩下 libero_10 的性能衰退速度\\\"}, \\\"eval_pi05_random_k085_long_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 Random k=0.85 Long seed42 v2 — 重跑验证。v1 结果 SR=44.4%（negative），与 L2norm k=0.75=73.4% 差距过大，需确认是否正确\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 44.4, \\\"total_success\\\": 222, \\\"total_episodes\\\": 500, \\\"per_task_sr\\\": {\\\"T0_alphabet_soup_tomato\\\": 52, \\\"T1_cream_cheese_butter\\\": 46, \\\"T2_stove_moka_pot\\\": 58, \\\"T3_black_bowl_drawer\\\": 74, \\\"T4_white_mug_left_plate\\\": 12, \\\"T5_book_back_shelf\\\": 32, \\\"T6_white_mug_plate\\\": 42, \\\"T7_alphabet_soup_cream\\\": 44, \\\"T8_moka_pots_stove\\\": 10, \\\"T9_yellow_white_mug_microwave\\\": 74}, \\\"runtime_min\\\": 267.8}}, \\\"eval_openvla_random_k095_goal_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.95 Goal seed42 — Goal Random curve 顶端缺口。Random k=0.9=79.6%, k=0.85=78.6%。k=0.95 补全曲线起始段\\\"}, \\\"eval_openvla_attn_k075_goal_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Attn k=0.75 Goal seed42 重跑 — v1 process dead 失败。Goal Attn cliff curve: k=0.9=73.2%, k=0.85=74.6%, k=0.7=66.4%。k=0.75 精确定位 cliff 下降起点\\\"}, \\\"eval_openvla_attn_k05_goal_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Attention k=0.5 Goal seed42 — Goal Attn cliff curve 极端压缩端点。测试 50% 压缩下 Attention pruning 在 Goal suite 的性能下限\\\"}, \\\"eval_openvla_random_k05_object_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.5 Object seed42 — Random pruning 极端压缩在 LIBERO-Object 上的性能下限\\\"}, \\\"eval_openvla_l2norm_k075_long_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.75 Long seed42 — L2norm pruning k=0.75 在 LIBERO-10 上的性能，Long cliff curve 数据点\\\"}, \\\"eval_openvla_attn_k07_long_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Attention k=0.7 Long seed42 — Attention pruning k=0.7 在 LIBERO-10 上的性能，Long cliff curve 中间点\\\", \\\"metrics\\\": {\\\"success_rate\\\": 24, \\\"total_successes\\\": 120, \\\"total_episodes\\\": 500}}, \\\"eval_openvla_attn_k05_long_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Attention k=0.5 Long seed42 — Attention pruning 极端压缩(保留50% tokens)在 LIBERO-10 上的性能下限，测试 attention cliff curve 最低点\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 14.6, \\\"suite\\\": \\\"libero_10\\\", \\\"prune_method\\\": \\\"attention\\\", \\\"keep_ratio\\\": 0.5, \\\"seed\\\": 42, \\\"episodes_per_task\\\": 50}}, \\\"eval_openvla_l2norm_k05_long_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.5 Long seed42 — Long L2norm cliff curve 极端压缩点。L2norm k=0.9=43.6%, k=0.85=38.8%, k=0.7=31.2%。k=0.5 测试 50% 压缩下的性能下限\\\"}, \\\"eval_openvla_random_k085_long_seed42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.85 Long — cliff curve 中间点。Random k=0.9=46.8%, k=0.7=38.8%。k=0.85 精确定位 Long suite cliff 位置\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.45, \\\"n_episodes\\\": 500, \\\"task_sr\\\": {\\\"put_both_alphabet_soup_and_tomato_sauce_in_basket\\\": 0.6, \\\"put_both_cream_cheese_and_butter_in_basket\\\": 0.64, \\\"turn_on_stove_put_moka_pot\\\": 0.6, \\\"put_black_bowl_in_bottom_drawer\\\": 0.32, \\\"put_white_mug_left_plate_yellow_mug_right_plate\\\": 0.2, \\\"pick_up_book_place_in_caddy\\\": 0.76, \\\"put_white_mug_on_plate_chocolate_pudding_right\\\": 0.3, \\\"put_both_alphabet_soup_and_cream_cheese_in_basket\\\": 0.6, \\\"put_both_moka_pots_on_stove\\\": 0.32, \\\"put_yellow_white_mug_in_microwave\\\": 0.16}}}, \\\"eval_openvla_random_k05_goal_seed42\\\": {\\\"hypothesis\\\": \\\"OpenVLA Random k=0.5 Goal seed42 — Goal Random cliff curve 底端缺口。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.5 测试 50% 极端压缩下 Goal suite 性能下限\\\", \\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.522, \\\"total_successes\\\": 261, \\\"total_episodes\\\": 500}}, \\\"eval_pi05_attn_k095_long_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 Attention k=0.95 Long seed42 — Attn Long cliff curve 顶端点。Attn k=0.9=63.8%, k=0.85=51.6%（cliff 在 0.85-0.9 间）。k=0.95 补全 Attn 曲线起始段，与 L2norm k=0.95=87% 和 Random k=0.95=63.2% 形成三方法对比\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 77, \\\"n_episodes\\\": 500, \\\"task_sr\\\": {\\\"T0\\\": null, \\\"T1\\\": null, \\\"T2\\\": null, \\\"T3\\\": null, \\\"T4\\\": null, \\\"T5\\\": null, \\\"T6\\\": 14, \\\"T7\\\": 80, \\\"T8\\\": 30, \\\"T9\\\": 98}}}, \\\"eval_openvla_l2norm_k075_goal_seed42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.75 Goal seed42 v2 — Goal cliff curve 加密点（v1 因 python not found 失败，改用 /root/miniconda3/bin/python）。L2norm k=0.9=74.8%, k=0.85=75.4%, k=0.7=68.4%。k=0.75 填补 k=0.85→0.7 下降斜率\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 70.2, \\\"task_srs\\\": [54, 80, 86, 22, 88, 70, 68, 98, 82, 54], \\\"episodes\\\": 500, \\\"tasks\\\": 10, \\\"time_min\\\": 198, \\\"tokens_256_to_192\\\": true}}, \\\"eval_openvla_attn_k085_long_seed42_v5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Attention-based pruning at k=0.85 on Long suite will show whether attention scoring preserves task-critical tokens for long-horizon manipulation, establishing the Attn cliff curve point between k=0.9 (known) and k=0.75 (TBD)\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 45.8, \\\"task_srs\\\": [60, 58, 56, 34, 38, 66, 34, 66, 24, 22], \\\"episodes\\\": 500, \\\"tasks\\\": 10, \\\"time_min\\\": 548.6, \\\"tokens_256_to_217\\\": true}}, \\\"eval_openvla_attn_k075_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Attention k=0.75 Object seed42 — Object Attn cliff curve 中间点。Attn k=0.9=61.4%, k=0.85=55.0%, k=0.7=43.8%。k=0.75 精确定位 Attention pruning 在 Object suite 上的 cliff 位置，区分平缓退化还是断崖式下降\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 53.2, \\\"total_success\\\": 266, \\\"total_episodes\\\": 500, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 56, \\\"cream_cheese\\\": 28, \\\"salad_dressing\\\": 70, \\\"bbq_sauce\\\": 34, \\\"ketchup\\\": 76, \\\"tomato_sauce\\\": 30, \\\"butter\\\": 28, \\\"milk\\\": 54, \\\"chocolate_pudding\\\": 86, \\\"orange_juice\\\": 70}, \\\"eval_time_min\\\": 272}}, \\\"eval_pi05_l2norm_k075_long_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 L2norm k=0.75 Long seed42 — cliff curve k=0.75 三方法对比。L2norm k=0.9=81%, k=0.5 在跑。重跑：之前因缺 offline flags 崩溃\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 73.4, \\\"per_task\\\": {\\\"T0_soup_tomato\\\": 96, \\\"T1_cream_butter\\\": 94, \\\"T2_stove_moka\\\": 82, \\\"T3_bowl_drawer\\\": 70, \\\"T4_mug_plate\\\": 68, \\\"T5_book_back\\\": 84, \\\"T6_mug_plate_tomato\\\": 52, \\\"T7_soup_cream\\\": 76, \\\"T8_moka_pots\\\": 28, \\\"T9_mug_microwave\\\": 84}}}, \\\"eval_pi05_l2norm_k05_spatial_seed42_postfix\\\": {\\\"hypothesis\\\": \\\"π0.5 L2norm k=0.5 Spatial seed42 post-fix — L2norm Spatial 曲线缺口。L2norm k=0.85 Spatial=88.4%。验证 L2norm importance scoring 在 50% keep ratio 下的 Spatial 表现\\\", \\\"metrics\\\": {\\\"elapsed_min\\\": 149.18, \\\"overall_sr\\\": 0.574, \\\"per_task_sr\\\": {\\\"pick_up_black_bowl_between_plate_and_ramekin\\\": 0.8, \\\"pick_up_black_bowl_from_table_center\\\": 0.9, \\\"pick_up_black_bowl_in_top_drawer\\\": 0.32, \\\"pick_up_black_bowl_next_to_cookie_box\\\": 0.28, \\\"pick_up_black_bowl_next_to_plate\\\": 0.74, \\\"pick_up_black_bowl_next_to_ramekin\\\": 0.9, \\\"pick_up_black_bowl_on_cookie_box\\\": 0.26, \\\"pick_up_black_bowl_on_ramekin\\\": 0.34, \\\"pick_up_black_bowl_on_stove\\\": 0.76, \\\"pick_up_black_bowl_on_wooden_cabinet\\\": 0.44}, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 287}, \\\"status\\\": \\\"DONE\\\"}, \\\"eval_pi05_random_k085_long_seed43_postfix\\\": {\\\"hypothesis\\\": \\\"π0.5 Random k=0.85 Long seed43 postfix — dual-seed Random Long cliff zone 验证。k=0.85 是 Object suite 上 Random disruption peak。验证 Long suite 是否同样存在 cliff\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.418, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 209}, \\\"status\\\": \\\"DONE\\\"}, \\\"eval_pi05_l2norm_k03_long_seed42_postfix\\\": {\\\"hypothesis\\\": \\\"π0.5 L2norm k=0.3 Long post-fix — L2norm Long curve extreme pruning endpoint。Pre-fix k=0.3 Long 已有数据。Random k=0.3 Long postfix 正在跑。补全 L2norm Long disruption curve 的极端端，与 Random k=0.3 对比验证 importance margin 在极端 pruning 下是否仍存在\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.366, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 183}, \\\"status\\\": \\\"DONE\\\"}, \\\"eval_pi05_random_k09_long_seed43_postfix\\\": {\\\"hypothesis\\\": \\\"π0.5 Random k=0.9 Long seed43 postfix — dual-seed Random Long curve near-full retention。seed42 k=0.9 已有结果。验证 90% retention 下 random pruning 的 seed 稳定性\\\", \\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.356, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 178}}, \\\"eval_openvla_random_k085_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.85 Object seed42 — Object cliff curve 中间点。Random k=0.9=62.8%, k=0.7=44.4%。k=0.85 与 L2norm(55.2%) 和 Attn(55.0%) 在 k=0.85 处三方法对比\\\"}, \\\"eval_pi05_l2norm_k085_long_seed42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"π0.5 L2norm k=0.85 Long seed42 — L2norm Long 单调曲线缺失点。k=0.9=81%, k=0.75=73.4%。k=0.85 确认下降斜率，验证 D237 position encoding sensitivity 假设中 L2norm 的平滑退化特性\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 78.8, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 394, \\\"per_task_sr\\\": {\\\"T0_alphabet_soup_tomato\\\": 98, \\\"T1_cream_cheese_butter\\\": 94, \\\"T2_stove_moka_pot\\\": 88, \\\"T3_black_bowl_drawer\\\": 98, \\\"T4_white_mug_left_plate\\\": 72, \\\"T5_book_back\\\": 98, \\\"T6_white_mug_plate\\\": 6, \\\"T7_alphabet_soup_cream\\\": 86, \\\"T8_moka_pots_stove\\\": 54, \\\"T9_yellow_white_mug_microwave\\\": 94}}}, \\\"eval_openvla_l2norm_k075_object_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.75 Object seed42 — Object L2norm cliff curve 中间点。L2norm k=0.95=70.6%, k=0.9=70.6%, k=0.85=?。k=0.75 测试更深压缩下 Object 的降级模式\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.574, \\\"total_episodes\\\": 500, \\\"successful_episodes\\\": 287, \\\"task_sr\\\": {\\\"alphabet_soup\\\": 0.78, \\\"cream_cheese\\\": 0.28, \\\"salad_dressing\\\": 0.68, \\\"bbq_sauce\\\": 0.46, \\\"ketchup\\\": 0.86, \\\"tomato_sauce\\\": 0.66, \\\"butter\\\": 0.4, \\\"milk\\\": 0.48, \\\"chocolate_pudding\\\": 0.46, \\\"orange_juice\\\": 0.68}, \\\"time_min\\\": 289.4}}, \\\"eval_openvla_attn_k07_goal_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Attn k=0.7 Goal seed42 — Goal Attn cliff curve 进一步压缩。Attn k=0.9=73.2%, k=0.85=74.6%（平稳）。k=0.7 测试 cliff 是否开始下降\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.664, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 332}}, \\\"eval_openvla_l2norm_k075_goal_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.75 Goal seed42 — Goal cliff curve 加密点。L2norm k=0.9=74.8%, k=0.85=75.4%, k=0.7=68.4%, k=0.5=43.4%。k=0.75 填补 k=0.85→0.7 之间的下降斜率（75.4%→68.4%=-7pp），判断是平滑退化还是存在 cliff\\\"}, \\\"eval_openvla_l2norm_k07_goal_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.7 Goal seed42 — Goal cliff curve 进一步压缩。L2norm k=0.9=75.2%, k=0.85=75.4%（平稳）。k=0.7 测试 cliff 是否开始下降\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.684, \\\"total_episodes\\\": 500, \\\"per_task_sr\\\": {\\\"open_the_middle_drawer_of_the_cabinet\\\": 0.6, \\\"put_the_bowl_on_the_stove\\\": 0.86, \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": 0.74, \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.16, \\\"put_the_bowl_on_top_of_the_cabinet\\\": 0.84, \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.66, \\\"put_the_cream_cheese_in_the_bowl\\\": 0.74, \\\"turn_on_the_stove\\\": 0.98, \\\"put_the_bowl_on_the_plate\\\": 0.7, \\\"put_the_wine_bottle_on_the_rack\\\": 0.56}}}, \\\"eval_openvla_attn_k05_goal_seed42\\\": {\\\"hypothesis\\\": \\\"OpenVLA Attention k=0.5 Goal — cliff curve extreme endpoint. Attn k=0.9 Goal=73.2%, k=0.85=74.6%. k=0.5 tests 50% compression limit for attention pruning on Goal suite\\\", \\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 44.2, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 221, \\\"source\\\": \\\"result file found on westd-27271 by audit worker, needs verification\\\"}}, \\\"eval_openvla_attn_k07_object_seed42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Attention k=0.7 Object v3 — v2进程PID 542010仍在运行（已过Task 7崩溃点）。带stderr捕获继续跑完。Attn Object cliff curve: k=0.9=61.4%, k=0.85=55.0%, k=0.7=?\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 43.8, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 219}}, \\\"eval_openvla_random_k05_object_seed42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.5 Object — cliff curve extreme endpoint. Random k=0.9=62.8%, k=0.7=44.4%. k=0.5 tests 50% compression limit for random pruning on Object suite\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 35.8, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 179, \\\"per_task\\\": {\\\"alphabet_soup\\\": 56, \\\"bbq_sauce\\\": 58, \\\"butter\\\": 0, \\\"chocolate_pudding\\\": 30, \\\"cream_cheese\\\": 2, \\\"ketchup\\\": 60, \\\"milk\\\": 12, \\\"orange_juice\\\": 74, \\\"salad_dressing\\\": 40, \\\"tomato_sauce\\\": 26}}}}, \\\"count\\\": 50, \\\"total\\\": 750, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.8604}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_openvla_attn_k095_object_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.95 Object seed42 — Object Attn cliff curve 顶端缺口。Attn k=0.9=61.4%, k=0.85=55.0%, k=0.75=53.2%。k=0.95 补全曲线起始段，与 L2norm k=0.95=70.6% 和 Baseline=74.0% 形成对比\", \"metrics\": {\"overall_sr\": 71.2, \"per_task\": {\"T9_chocolate_pudding\": 66, \"T10_orange_juice\": 92}, \"time_min\": 238.2}}, \"eval_openvla_random_k095_object_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.95 Object seed42 — Object curve 顶端 Random 方法缺口。Random k=0.9=57.4%。k=0.95 补全 Object Random cliff curve 起始段，与 L2norm k=0.95=70.6% 形成对比\", \"metrics\": {\"overall_sr\": 67.4, \"per_task\": {\"T1_alphabet_soup\": 76, \"T2_cream_cheese\": 44, \"T3_salad_dressing\": 74, \"T4_bbq_sauce\": 48, \"T5_ketchup\": 78, \"T6_tomato_sauce\": 78, \"T7_butter\": 48, \"T8_milk\": 66, \"T9_chocolate_pudding\": 74, \"T10_orange_juice\": 88}, \"time_min\": 282.6}}, \"eval_openvla_random_k075_object_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.75 Object seed42 — Object cliff curve 中间点。Random k=0.85=61.4%(v2), k=0.7=44.4%。k=0.75 填补两者之间的下降斜率，与 Attn k=0.75(running) 对比三方法在 25% 压缩下的差异\", \"metrics\": {\"overall_sr\": 50.4, \"per_task\": {\"T1_alphabet_soup\": 40, \"T2_cream_cheese\": 40, \"T3_salad_dressing\": 64, \"T4_bbq_sauce\": 42, \"T5_ketchup\": 58, \"T6_tomato_sauce\": 52, \"T7_butter\": 38, \"T8_milk\": 56, \"T9_chocolate_pudding\": 46, \"T10_orange_juice\": 70}, \"time_min\": 297.3}}, \"eval_openvla_random_k075_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\", \"metrics\": {\"overall_sr\": 72, \"per_task\": {\"T1_open_middle_drawer\": 70, \"T2_bowl_on_stove\": 86, \"T3_wine_on_cabinet\": 70, \"T4_bowl_in_drawer\": 36, \"T5_bowl_on_cabinet\": 92, \"T6_plate_to_front\": 76, \"T7_cream_cheese_in_bowl\": 60, \"T8_turn_on_stove\": 100, \"T9_bowl_on_plate\": 74, \"T10_wine_on_rack\": 56}, \"time_min\": 228.8}}, \"eval_openvla_attn_k095_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.95 Goal seed42 — Goal Attn curve 顶端缺口。Attn k=0.9=73.2%, k=0.85=74.6%。k=0.95 补全曲线起始段\"}, \"eval_openvla_random_k075_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Random pruning at k=0.75 on OpenVLA Long suite serves as a baseline to quantify the importance margin of structured pruning methods over random token removal.\"}, \"eval_openvla_l2norm_k095_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.95 Goal seed42 — Goal curve 顶端三方法都缺。L2n k=0.9=74.8%。k=0.95 预期接近 baseline，补全 Goal cliff curve 起始段\", \"metrics\": {\"overall_sr\": 75.2, \"per_task\": {\"T1\": 96, \"T2\": 94, \"T3\": 82, \"T4\": 60, \"T5\": 88, \"T6\": 66, \"T7\": 54, \"T8\": 96, \"T9\": 82, \"T10\": 54}}}, \"eval_pi05_random_k085_long_seed42_strict_v2\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Random k=0.85 Long strict v2 — v1 因缺少 HF_HUB_OFFLINE=1 在 westd-41074 上失败(网络不可达)。本次添加离线模式环境变量。strict 条件(if done: only)重跑，修正 cqa1 宽松条件(done|reward>0.5)导致的数据污染。cqa1 SR=44.4%(宽松)\"}, \"eval_openvla_attn_k075_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Attention-based pruning at k=0.75 on OpenVLA (LIBERO-Long/10 tasks) maintains competitive success rate by retaining the most important 75% of vision tokens based on attention scores\", \"metrics\": {\"overall_sr\": 37.4, \"overall_sr_completed_tasks\": 39.8, \"completed_episodes\": 430, \"total_planned\": 500, \"total_success\": 161, \"per_task_sr\": {\"T1_alphabet_soup_tomato_sauce\": 38, \"T2_cream_cheese_butter\": 52, \"T3_stove_moka_pot\": 48, \"T4_bowl_in_drawer\": 34, \"T5_mugs_on_plates\": 18, \"T6_book_in_caddy\": 54, \"T7_mug_pudding\": 24, \"T8_soup_cream_cheese\": 50, \"T9_moka_pots_stove_PARTIAL\": 6.7}, \"per_task_success\": {\"T1\": \"19/50\", \"T2\": \"26/50\", \"T3\": \"24/50\", \"T4\": \"17/50\", \"T5\": \"9/50\", \"T6\": \"27/50\", \"T7\": \"12/50\", \"T8\": \"25/50\", \"T9\": \"2/30 (partial)\", \"T10\": \"not started\"}}}, \"eval_pi05_random_k085_long_seed42_strict\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Random k=0.85 Long seed42 严格条件重跑 — 使用 westd-41074 V-B 代码(426行, `if done:` strict)。修正 cqa1 V-C 宽松条件(done|reward>0.5)导致的数据污染。cqa1 SR=44.4%(宽松), 此实验为严格条件下的真实值\"}, \"eval_pi05_random_k07_long_seed42\": {\"hypothesis\": \"Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估\", \"status\": \"DONE\", \"metrics\": {\"overall_sr\": 62.4, \"suite\": \"libero_10\", \"prune_method\": \"random\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_l2norm_k085_long_seed42\": {\"hypothesis\": \"π0.5 L2norm k=0.85 on LIBERO-Long (libero_10): 15% token removal on 520-step horizon tasks. Object k=0.85=98.0%. Testing if Long suite shows similar resilience or begins to degrade.\", \"metrics\": {\"elapsed_min\": 133.4, \"keep_ratio\": 0.85, \"num_episodes\": 500, \"num_success\": 390, \"prune_mode\": \"l2norm\", \"seed\": 42, \"success_rate\": 0.78, \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_openvla_attn_k075_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Attention-based pruning at k=0.75 on OpenVLA Goal suite will retain task performance by preserving the most important attention heads for goal-conditioned manipulation tasks.\", \"metrics\": {\"overall_sr\": 67.4, \"suite\": \"libero_goal\", \"prune_method\": \"attention\", \"keep_ratio\": 0.75, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_l2norm_k05_long_seed42_v4\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 L2norm k=0.5 Long seed42 v4 — 重跑。L2norm k=0.5 在 libero_10 上的 50% 压缩性能评估\", \"metrics\": {\"overall_sr\": 50, \"total_successes\": 250, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 66, \"T1_cream_cheese_butter\": 52, \"T2_stove_moka_pot\": 74, \"T3_black_bowl_drawer\": 38, \"T4_white_mug_left_plate\": 30, \"T5_book_back_shelf\": 50, \"T6_white_mug_plate\": 32, \"T7_alphabet_soup_cream\": 60, \"T8_moka_pots_stove\": 16, \"T9_yellow_mug_microwave\": 82}, \"elapsed_minutes\": 249.4, \"seed\": 42}}, \"eval_pi05_l2norm_k085_long_seed42_v4\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 L2norm k=0.85 Long seed42 — L2norm Long curve 唯一缺口。L2norm k=0.9=81.0%, k=0.75=73.4%。k=0.85 补全 L2norm 完美单调曲线(D237)\", \"metrics\": {\"overall_sr\": 77.8, \"suite\": \"libero_10\", \"prune_method\": \"l2norm\", \"keep_ratio\": 0.85, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_attention_k07_long_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Attention k=0.7 Long seed42 v2 — Attn Long cliff curve 中间点。Attn k=0.75=51.8%, k=0.5=49.4%。k=0.7 补全 Attn Long curve\", \"metrics\": {\"overall_sr\": 50.8, \"per_task\": {\"T0_alphabet_soup_tomato\": 72, \"T1_cream_cheese_butter\": 70, \"T2_stove_moka_pot\": 58, \"T3_black_bowl_drawer\": 46, \"T4_white_mug_plate\": 36, \"T5_book_back\": 32, \"T6_mug_plate_yellow\": 58, \"T7_alphabet_soup_cream\": 48, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 82}, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_attention_k075_long_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Attention k=0.75 Long seed42 v2 — cliff curve k=0.75 三方法对比。Attn k=0.9=63.8%。重跑：v1 因缺 offline flags 崩溃\", \"metrics\": {\"overall_sr\": 52.4, \"task_sr\": {\"T0_alphabet_soup_tomato\": 68, \"T1_cream_cheese_butter\": 78, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 48, \"T4_white_mug_left_plate\": 26, \"T5_book_back_compartment\": 50, \"T6_white_mug_plate\": 76, \"T7_alphabet_soup_cream\": 30, \"T8_both_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 78}}}, \"eval_pi05_attention_k05_long_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Attention k=0.5 Long seed42 v2 — 重跑。Attn Long cliff curve 极端压缩点。Attn k=0.9=63.8%, k=0.75=51.8%。v1 被误判 failed 但有 SR=49.4%，本次重新验证\", \"metrics\": {\"overall_sr\": 49.8, \"task_sr\": {\"T0_alphabet_soup_tomato\": 74, \"T1_cream_cheese_butter\": 46, \"T2_stove_moka_pot\": 60, \"T3_black_bowl_drawer\": 70, \"T4_white_mug_left_plate\": 46, \"T5_book_back_shelf\": 52, \"T6_white_mug_plate\": 10, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 18, \"T9_yellow_white_mug_microwave\": 68}}}, \"eval_pi05_attention_k085_long_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Attention k=0.85 Long seed42 — Attn Long cliff curve 中间点。Attn k=0.9=63.8%, k=0.75=51.8%。k=0.85 填补两者之间数据缺口（v1 进程静默死亡，v2 改用绝对路径 python 重试）\", \"metrics\": {\"overall_sr\": 51.6, \"total_episodes\": 500, \"per_task\": {\"T0_alphabet_soup_tomato\": 20, \"T1_cream_cheese_butter\": 54, \"T2_stove_moka_pot\": 32, \"T3_black_bowl_drawer\": 60, \"T4_white_mug_left_plate\": 48, \"T5_book_back_shelf\": 90, \"T6_white_mug_plate\": 68, \"T7_alphabet_soup_cream\": 46, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 92}}}, \"eval_pi05_random_k05_long_seed42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Random k=0.5 Long seed42 v3 — 重跑。Random k=0.5 在 libero_10 上的 50% 压缩性能评估\", \"metrics\": {\"overall_sr\": 50.2, \"total_successes\": 251, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 84, \"T1_cream_cheese_butter\": 32, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 72, \"T4_white_mug_left_plate\": 74, \"T5_book_back_shelf\": 38, \"T6_white_mug_plate\": 30, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 4, \"T9_yellow_mug_microwave\": 50}, \"elapsed_minutes\": 252.3, \"seed\": 42}}, \"eval_pi05_random_k075_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 62.4, \"suite\": \"libero_10\", \"tasks_completed\": 10, \"total_episodes\": 500}, \"hypothesis\": \"π0.5 Random k=0.75 Long seed42 v2 — cliff curve 补充点。Random k=0.9=63.8%。k=0.75 测试 Random 在 25% 压缩下 libero_10 的性能衰退速度\"}, \"eval_pi05_random_k085_long_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Random k=0.85 Long seed42 v2 — 重跑验证。v1 结果 SR=44.4%（negative），与 L2norm k=0.75=73.4% 差距过大，需确认是否正确\", \"metrics\": {\"overall_sr\": 44.4, \"total_success\": 222, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 52, \"T1_cream_cheese_butter\": 46, \"T2_stove_moka_pot\": 58, \"T3_black_bowl_drawer\": 74, \"T4_white_mug_left_plate\": 12, \"T5_book_back_shelf\": 32, \"T6_white_mug_plate\": 42, \"T7_alphabet_soup_cream\": 44, \"T8_moka_pots_stove\": 10, \"T9_yellow_white_mug_microwave\": 74}, \"runtime_min\": 267.8}}, \"eval_openvla_random_k095_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.95 Goal seed42 — Goal Random curve 顶端缺口。Random k=0.9=79.6%, k=0.85=78.6%。k=0.95 补全曲线起始段\"}, \"eval_openvla_attn_k075_goal_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attn k=0.75 Goal seed42 重跑 — v1 process dead 失败。Goal Attn cliff curve: k=0.9=73.2%, k=0.85=74.6%, k=0.7=66.4%。k=0.75 精确定位 cliff 下降起点\"}, \"eval_openvla_attn_k05_goal_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.5 Goal seed42 — Goal Attn cliff curve 极端压缩端点。测试 50% 压缩下 Attention pruning 在 Goal suite 的性能下限\"}, \"eval_openvla_random_k05_object_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.5 Object seed42 — Random pruning 极端压缩在 LIBERO-Object 上的性能下限\"}, \"eval_openvla_l2norm_k075_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.75 Long seed42 — L2norm pruning k=0.75 在 LIBERO-10 上的性能，Long cliff curve 数据点\"}, \"eval_openvla_attn_k07_long_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.7 Long seed42 — Attention pruning k=0.7 在 LIBERO-10 上的性能，Long cliff curve 中间点\", \"metrics\": {\"success_rate\": 24, \"total_successes\": 120, \"total_episodes\": 500}}, \"eval_openvla_attn_k05_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.5 Long seed42 — Attention pruning 极端压缩(保留50% tokens)在 LIBERO-10 上的性能下限，测试 attention cliff curve 最低点\", \"metrics\": {\"overall_sr\": 14.6, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.5, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_openvla_l2norm_k05_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.5 Long seed42 — Long L2norm cliff curve 极端压缩点。L2norm k=0.9=43.6%, k=0.85=38.8%, k=0.7=31.2%。k=0.5 测试 50% 压缩下的性能下限\"}, \"eval_openvla_random_k085_long_seed42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.85 Long — cliff curve 中间点。Random k=0.9=46.8%, k=0.7=38.8%。k=0.85 精确定位 Long suite cliff 位置\", \"metrics\": {\"overall_sr\": 0.45, \"n_episodes\": 500, \"task_sr\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0.6, \"put_both_cream_cheese_and_butter_in_basket\": 0.64, \"turn_on_stove_put_moka_pot\": 0.6, \"put_black_bowl_in_bottom_drawer\": 0.32, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.2, \"pick_up_book_place_in_caddy\": 0.76, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.3, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0.6, \"put_both_moka_pots_on_stove\": 0.32, \"put_yellow_white_mug_in_microwave\": 0.16}}}, \"eval_openvla_random_k05_goal_seed42\": {\"hypothesis\": \"OpenVLA Random k=0.5 Goal seed42 — Goal Random cliff curve 底端缺口。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.5 测试 50% 极端压缩下 Goal suite 性能下限\", \"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.522, \"total_successes\": 261, \"total_episodes\": 500}}, \"eval_pi05_attn_k095_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 Attention k=0.95 Long seed42 — Attn Long cliff curve 顶端点。Attn k=0.9=63.8%, k=0.85=51.6%（cliff 在 0.85-0.9 间）。k=0.95 补全 Attn 曲线起始段，与 L2norm k=0.95=87% 和 Random k=0.95=63.2% 形成三方法对比\", \"metrics\": {\"overall_sr\": 77, \"n_episodes\": 500, \"task_sr\": {\"T0\": null, \"T1\": null, \"T2\": null, \"T3\": null, \"T4\": null, \"T5\": null, \"T6\": 14, \"T7\": 80, \"T8\": 30, \"T9\": 98}}}, \"eval_openvla_l2norm_k075_goal_seed42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.75 Goal seed42 v2 — Goal cliff curve 加密点（v1 因 python not found 失败，改用 /root/miniconda3/bin/python）。L2norm k=0.9=74.8%, k=0.85=75.4%, k=0.7=68.4%。k=0.75 填补 k=0.85→0.7 下降斜率\", \"metrics\": {\"overall_sr\": 70.2, \"task_srs\": [54, 80, 86, 22, 88, 70, 68, 98, 82, 54], \"episodes\": 500, \"tasks\": 10, \"time_min\": 198, \"tokens_256_to_192\": true}}, \"eval_openvla_attn_k085_long_seed42_v5\": {\"status\": \"DONE\", \"hypothesis\": \"Attention-based pruning at k=0.85 on Long suite will show whether attention scoring preserves task-critical tokens for long-horizon manipulation, establishing the Attn cliff curve point between k=0.9 (known) and k=0.75 (TBD)\", \"metrics\": {\"overall_sr\": 45.8, \"task_srs\": [60, 58, 56, 34, 38, 66, 34, 66, 24, 22], \"episodes\": 500, \"tasks\": 10, \"time_min\": 548.6, \"tokens_256_to_217\": true}}, \"eval_openvla_attn_k075_object_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.75 Object seed42 — Object Attn cliff curve 中间点。Attn k=0.9=61.4%, k=0.85=55.0%, k=0.7=43.8%。k=0.75 精确定位 Attention pruning 在 Object suite 上的 cliff 位置，区分平缓退化还是断崖式下降\", \"metrics\": {\"overall_sr\": 53.2, \"total_success\": 266, \"total_episodes\": 500, \"per_task_sr\": {\"alphabet_soup\": 56, \"cream_cheese\": 28, \"salad_dressing\": 70, \"bbq_sauce\": 34, \"ketchup\": 76, \"tomato_sauce\": 30, \"butter\": 28, \"milk\": 54, \"chocolate_pudding\": 86, \"orange_juice\": 70}, \"eval_time_min\": 272}}, \"eval_pi05_l2norm_k075_long_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 L2norm k=0.75 Long seed42 — cliff curve k=0.75 三方法对比。L2norm k=0.9=81%, k=0.5 在跑。重跑：之前因缺 offline flags 崩溃\", \"metrics\": {\"overall_sr\": 73.4, \"per_task\": {\"T0_soup_tomato\": 96, \"T1_cream_butter\": 94, \"T2_stove_moka\": 82, \"T3_bowl_drawer\": 70, \"T4_mug_plate\": 68, \"T5_book_back\": 84, \"T6_mug_plate_tomato\": 52, \"T7_soup_cream\": 76, \"T8_moka_pots\": 28, \"T9_mug_microwave\": 84}}}, \"eval_pi05_l2norm_k05_spatial_seed42_postfix\": {\"hypothesis\": \"π0.5 L2norm k=0.5 Spatial seed42 post-fix — L2norm Spatial 曲线缺口。L2norm k=0.85 Spatial=88.4%。验证 L2norm importance scoring 在 50% keep ratio 下的 Spatial 表现\", \"metrics\": {\"elapsed_min\": 149.18, \"overall_sr\": 0.574, \"per_task_sr\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.8, \"pick_up_black_bowl_from_table_center\": 0.9, \"pick_up_black_bowl_in_top_drawer\": 0.32, \"pick_up_black_bowl_next_to_cookie_box\": 0.28, \"pick_up_black_bowl_next_to_plate\": 0.74, \"pick_up_black_bowl_next_to_ramekin\": 0.9, \"pick_up_black_bowl_on_cookie_box\": 0.26, \"pick_up_black_bowl_on_ramekin\": 0.34, \"pick_up_black_bowl_on_stove\": 0.76, \"pick_up_black_bowl_on_wooden_cabinet\": 0.44}, \"total_episodes\": 500, \"total_successes\": 287}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed43_postfix\": {\"hypothesis\": \"π0.5 Random k=0.85 Long seed43 postfix — dual-seed Random Long cliff zone 验证。k=0.85 是 Object suite 上 Random disruption peak。验证 Long suite 是否同样存在 cliff\", \"metrics\": {\"overall_sr\": 0.418, \"total_episodes\": 500, \"total_successes\": 209}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed42_postfix\": {\"hypothesis\": \"π0.5 L2norm k=0.3 Long post-fix — L2norm Long curve extreme pruning endpoint。Pre-fix k=0.3 Long 已有数据。Random k=0.3 Long postfix 正在跑。补全 L2norm Long disruption curve 的极端端，与 Random k=0.3 对比验证 importance margin 在极端 pruning 下是否仍存在\", \"metrics\": {\"overall_sr\": 0.366, \"total_episodes\": 500, \"total_successes\": 183}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_long_seed43_postfix\": {\"hypothesis\": \"π0.5 Random k=0.9 Long seed43 postfix — dual-seed Random Long curve near-full retention。seed42 k=0.9 已有结果。验证 90% retention 下 random pruning 的 seed 稳定性\", \"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.356, \"total_episodes\": 500, \"total_successes\": 178}}, \"eval_openvla_random_k085_object_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.85 Object seed42 — Object cliff curve 中间点。Random k=0.9=62.8%, k=0.7=44.4%。k=0.85 与 L2norm(55.2%) 和 Attn(55.0%) 在 k=0.85 处三方法对比\"}, \"eval_pi05_l2norm_k085_long_seed42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 L2norm k=0.85 Long seed42 — L2norm Long 单调曲线缺失点。k=0.9=81%, k=0.75=73.4%。k=0.85 确认下降斜率，验证 D237 position encoding sensitivity 假设中 L2norm 的平滑退化特性\", \"metrics\": {\"overall_sr\": 78.8, \"total_episodes\": 500, \"total_successes\": 394, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 98, \"T1_cream_cheese_butter\": 94, \"T2_stove_moka_pot\": 88, \"T3_black_bowl_drawer\": 98, \"T4_white_mug_left_plate\": 72, \"T5_book_back\": 98, \"T6_white_mug_plate\": 6, \"T7_alphabet_soup_cream\": 86, \"T8_moka_pots_stove\": 54, \"T9_yellow_white_mug_microwave\": 94}}}, \"eval_openvla_l2norm_k075_object_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.75 Object seed42 — Object L2norm cliff curve 中间点。L2norm k=0.95=70.6%, k=0.9=70.6%, k=0.85=?。k=0.75 测试更深压缩下 Object 的降级模式\", \"metrics\": {\"overall_sr\": 0.574, \"total_episodes\": 500, \"successful_episodes\": 287, \"task_sr\": {\"alphabet_soup\": 0.78, \"cream_cheese\": 0.28, \"salad_dressing\": 0.68, \"bbq_sauce\": 0.46, \"ketchup\": 0.86, \"tomato_sauce\": 0.66, \"butter\": 0.4, \"milk\": 0.48, \"chocolate_pudding\": 0.46, \"orange_juice\": 0.68}, \"time_min\": 289.4}}, \"eval_openvla_attn_k07_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attn k=0.7 Goal seed42 — Goal Attn cliff curve 进一步压缩。Attn k=0.9=73.2%, k=0.85=74.6%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"metrics\": {\"overall_sr\": 0.664, \"total_episodes\": 500, \"total_successes\": 332}}, \"eval_openvla_l2norm_k075_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.75 Goal seed42 — Goal cliff curve 加密点。L2norm k=0.9=74.8%, k=0.85=75.4%, k=0.7=68.4%, k=0.5=43.4%。k=0.75 填补 k=0.85→0.7 之间的下降斜率（75.4%→68.4%=-7pp），判断是平滑退化还是存在 cliff\"}, \"eval_openvla_l2norm_k07_goal_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA L2norm k=0.7 Goal seed42 — Goal cliff curve 进一步压缩。L2norm k=0.9=75.2%, k=0.85=75.4%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"metrics\": {\"overall_sr\": 0.684, \"total_episodes\": 500, \"per_task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_bowl_on_the_stove\": 0.86, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.74, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.16, \"put_the_bowl_on_top_of_the_cabinet\": 0.84, \"push_the_plate_to_the_front_of_the_stove\": 0.66, \"put_the_cream_cheese_in_the_bowl\": 0.74, \"turn_on_the_stove\": 0.98, \"put_the_bowl_on_the_plate\": 0.7, \"put_the_wine_bottle_on_the_rack\": 0.56}}}, \"eval_openvla_attn_k05_goal_seed42\": {\"hypothesis\": \"OpenVLA Attention k=0.5 Goal — cliff curve extreme endpoint. Attn k=0.9 Goal=73.2%, k=0.85=74.6%. k=0.5 tests 50% compression limit for attention pruning on Goal suite\", \"status\": \"DONE\", \"metrics\": {\"overall_sr\": 44.2, \"total_episodes\": 500, \"total_successes\": 221, \"source\": \"result file found on westd-27271 by audit worker, needs verification\"}}, \"eval_openvla_attn_k07_object_seed42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Attention k=0.7 Object v3 — v2进程PID 542010仍在运行（已过Task 7崩溃点）。带stderr捕获继续跑完。Attn Object cliff curve: k=0.9=61.4%, k=0.85=55.0%, k=0.7=?\", \"metrics\": {\"overall_sr\": 43.8, \"total_episodes\": 500, \"total_successes\": 219}}, \"eval_openvla_random_k05_object_seed42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"OpenVLA Random k=0.5 Object — cliff curve extreme endpoint. Random k=0.9=62.8%, k=0.7=44.4%. k=0.5 tests 50% compression limit for random pruning on Object suite\", \"metrics\": {\"overall_sr\": 35.8, \"total_episodes\": 500, \"total_successes\": 179, \"per_task\": {\"alphabet_soup\": 56, \"bbq_sauce\": 58, \"butter\": 0, \"chocolate_pudding\": 30, \"cream_cheese\": 2, \"ketchup\": 60, \"milk\": 12, \"orange_juice\": 74, \"salad_dressing\": 40, \"tomato_sauce\": 26}}}}, \"count\": 50, \"total\": 750, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8604}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
OK, I see that `eval_openvla_random_k095_object_seed42` is already DONE with SR=67.4%. So that's already completed.

Let me think about what experiments are still missing that I could run on GPU1 with the available models (Goal, Object, Long, Spatial all available).

Let me look at what's in the RUNNING state and see if there are key gaps. Let me also check the ROADMAP more carefully.

Looking at RUNNING experiments:
1. eval_pi05_random_k075_long_seed42_strict - Pi0.5, different model


2. eval_openvla_attn_k095_goal_seed42_v2 - Running on another server probably
3. eval_pi05_baseline_goal_seed42_strict - Pi0.5
4. eval_pi05_attn_k095_long_seed42_strict - Pi0.5
5. eval_pi05_attn_k085_long_seed42_strict - Pi0.5
6. eval_pi05_attn_k09_long_seed42_strict - Pi0.5
7. eval_openvla_random_k095_goal_seed42_v2 - Running
8. eval_openvla_at...

I'm scanning through the running experiments to identify which ones are Pi0.5 variants and which are OpenVLA, and noting which are still in progress versus completed.

Looking at the completed OpenVLA Object experiments, I see attention with k=0.95 achieved 71.2%, and I'm checking what other configurations have finished to avoid duplicating work on GPU1. I'm cross-referencing the results to identify which experiments are actually missing. Looking at the OpenVLA Object data, L2norm k=0.85 appears to be a gap, and I need to verify whether some of the Random k values are complete or still running. Looking at the Object eval runtime of 4-5 hours and checking the actual deadline—it's tomorrow at 12:00 UTC, giving me about 30 hours, not 4. So I have enough time to run the missing experiments like L2norm k=0.85 Object, L2norm k=0.5 Object, and Attn k=0.5 Object before the hard deadline. Looking at the missing data points for the Object suite, the k=0.85 L2norm result would be most valuable since it fills a critical gap in the curve between existing points, whereas the extreme endpoints at k=0.5 are less important for the overall shape. I need to verify what's actually in the ROADMAP to see which experiment I should prioritize running next.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "c77686d6-c72c-4f6e-bf9f-be7a0bd0aa2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9nMiW8FFz4uooHdKyGaqS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11184,
      "cache_read_input_tokens": 36062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11184
      },
      "output_tokens": 31,
      "service_tier": "standard",
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

_source line 49_

Random k=0.95 Object 已完成 (67.4%)。需要找其他缺口。检查 L2norm k=0.85 Object 是否缺失。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "5a51bced-18f7-45ce-b147-ff4fc4653ad0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9nMiW8FFz4uooHdKyGaqS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11184,
      "cache_read_input_tokens": 36062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11184
      },
      "output_tokens": 31,
      "service_tier": "standard",
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

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_014i2UYK4dYEhdkDE16qymLp`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "fields": [
    "status",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "640cbe57-8d6e-4e3a-ba3c-83946ecbf81a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9nMiW8FFz4uooHdKyGaqS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11184,
      "cache_read_input_tokens": 36062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11184
      },
      "output_tokens": 31,
      "service_tier": "standard",
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

_source line 51 · 2026-05-27T06:16:53.596Z_

<details><summary>↩ Tool result · `toolu_014i2UYK4dYEhdkDE16qymLp`</summary>

```text
Error: result (198,998 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/77f0b2fb-f038-4bff-bd48-3bed171e3c77/tool-results/mcp-agent-ml-research-read_registry-1779862613590.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/77f0b2fb-f038-4bff-bd48-3bed171e3c77/tool-results/mcp-agent-ml-research-read_registry-1779862613590.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "b97fe566-64e6-4c9c-b886-a8a301ae25d8",
  "tool_use_result": {
    "content": "Error: result (198,998 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/77f0b2fb-f038-4bff-bd48-3bed171e3c77/tool-results/mcp-agent-ml-research-read_registry-1779862613590.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/77f0b2fb-f038-4bff-bd48-3bed171e3c77/tool-results/mcp-agent-ml-research-read_registry-1779862613590.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_openvla_attn_k095_object_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 71.2, \"per_task\": {\"T9_chocolate_pudding\": 66, \"T10_orange_juice\": 92}, \"time_min\": 238.2}}, \"eval_openvla_random_k095_object_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 67.4, \"per_task\": {\"T1_alphabet_soup\": 76, \"T2_cream_cheese\": 44, \"T3_salad_dressing\": 74, \"T4_bbq_sauce\": 48, \"T5_ketchup\": 78, \"T6_tomato_sauce\": 78, \"T7_butter\": 48, \"T8_milk\": 66, \"T9_chocolate_pudding\": 74, \"T10_orange_juice\": 88}, \"time_min\": 282.6}}, \"eval_openvla_random_k075_object_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 50.4, \"per_task\": {\"T1_alphabet_soup\": 40, \"T2_cream_cheese\": 40, \"T3_salad_dressing\": 64, \"T4_bbq_sauce\": 42, \"T5_ketchup\": 58, \"T6_tomato_sauce\": 52, \"T7_butter\": 38, \"T8_milk\": 56, \"T9_chocolate_pudding\": 46, \"T10_orange_juice\": 70}, \"time_min\": 297.3}}, \"eval_openvla_random_k075_goal_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 72, \"per_task\": {\"T1_open_middle_drawer\": 70, \"T2_bowl_on_stove\": 86, \"T3_wine_on_cabinet\": 70, \"T4_bowl_in_drawer\": 36, \"T5_bowl_on_cabinet\": 92, \"T6_plate_to_front\": 76, \"T7_cream_cheese_in_bowl\": 60, \"T8_turn_on_stove\": 100, \"T9_bowl_on_plate\": 74, \"T10_wine_on_rack\": 56}, \"time_min\": 228.8}}, \"eval_pi05_random_k075_long_seed42_strict\": {\"status\": \"RUNNING\"}, \"eval_openvla_attn_k095_goal_seed42_v2\": {\"status\": \"RUNNING\"}, \"eval_openvla_attn_k095_goal_seed42_v3\": {\"status\": \"PREPARING\"}, \"eval_pi05_baseline_goal_seed42_strict\": {\"status\": \"RUNNING\"}, \"eval_openvla_attn_k095_goal_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_random_k075_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_l2norm_k095_goal_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 75.2, \"per_task\": {\"T1\": 96, \"T2\": 94, \"T3\": 82, \"T4\": 60, \"T5\": 88, \"T6\": 66, \"T7\": 54, \"T8\": 96, \"T9\": 82, \"T10\": 54}}}, \"eval_pi05_random_k085_long_seed42_strict_v2\": {\"status\": \"DONE\"}, \"eval_pi05_attn_k095_long_seed42_strict\": {\"status\": \"RUNNING\"}, \"eval_pi05_attn_k085_long_seed42_strict\": {\"status\": \"RUNNING\"}, \"eval_pi05_attn_k09_long_seed42_strict\": {\"status\": \"RUNNING\"}, \"eval_openvla_attn_k075_long_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 37.4, \"overall_sr_completed_tasks\": 39.8, \"completed_episodes\": 430, \"total_planned\": 500, \"total_success\": 161, \"per_task_sr\": {\"T1_alphabet_soup_tomato_sauce\": 38, \"T2_cream_cheese_butter\": 52, \"T3_stove_moka_pot\": 48, \"T4_bowl_in_drawer\": 34, \"T5_mugs_on_plates\": 18, \"T6_book_in_caddy\": 54, \"T7_mug_pudding\": 24, \"T8_soup_cream_cheese\": 50, \"T9_moka_pots_stove_PARTIAL\": 6.7}, \"per_task_success\": {\"T1\": \"19/50\", \"T2\": \"26/50\", \"T3\": \"24/50\", \"T4\": \"17/50\", \"T5\": \"9/50\", \"T6\": \"27/50\", \"T7\": \"12/50\", \"T8\": \"25/50\", \"T9\": \"2/30 (partial)\", \"T10\": \"not started\"}}}, \"eval_pi05_random_k085_long_seed42_strict\": {\"status\": \"DONE\"}, \"eval_pi05_random_k07_long_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 62.4, \"suite\": \"libero_10\", \"prune_method\": \"random\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_l2norm_k085_long_seed42\": {\"metrics\": {\"elapsed_min\": 133.4, \"keep_ratio\": 0.85, \"num_episodes\": 500, \"num_success\": 390, \"prune_mode\": \"l2norm\", \"seed\": 42, \"success_rate\": 0.78, \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_openvla_attn_k075_goal_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 67.4, \"suite\": \"libero_goal\", \"prune_method\": \"attention\", \"keep_ratio\": 0.75, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_l2norm_k05_long_seed42_v4\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 50, \"total_successes\": 250, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 66, \"T1_cream_cheese_butter\": 52, \"T2_stove_moka_pot\": 74, \"T3_black_bowl_drawer\": 38, \"T4_white_mug_left_plate\": 30, \"T5_book_back_shelf\": 50, \"T6_white_mug_plate\": 32, \"T7_alphabet_soup_cream\": 60, \"T8_moka_pots_stove\": 16, \"T9_yellow_mug_microwave\": 82}, \"elapsed_minutes\": 249.4, \"seed\": 42}}, \"eval_pi05_l2norm_k07_long_seed42\": {\"metrics\": {\"overall_sr\": 63.2, \"suite\": \"libero_10\", \"prune_method\": \"l2norm\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}, \"status\": \"DEPLOYED\"}, \"eval_pi05_l2norm_k085_long_seed42_v4\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 77.8, \"suite\": \"libero_10\", \"prune_method\": \"l2norm\", \"keep_ratio\": 0.85, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_attention_k07_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 50.8, \"per_task\": {\"T0_alphabet_soup_tomato\": 72, \"T1_cream_cheese_butter\": 70, \"T2_stove_moka_pot\": 58, \"T3_black_bowl_drawer\": 46, \"T4_white_mug_plate\": 36, \"T5_book_back\": 32, \"T6_mug_plate_yellow\": 58, \"T7_alphabet_soup_cream\": 48, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 82}, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_attention_k075_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 52.4, \"task_sr\": {\"T0_alphabet_soup_tomato\": 68, \"T1_cream_cheese_butter\": 78, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 48, \"T4_white_mug_left_plate\": 26, \"T5_book_back_compartment\": 50, \"T6_white_mug_plate\": 76, \"T7_alphabet_soup_cream\": 30, \"T8_both_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 78}}}, \"eval_pi05_attention_k05_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 49.8, \"task_sr\": {\"T0_alphabet_soup_tomato\": 74, \"T1_cream_cheese_butter\": 46, \"T2_stove_moka_pot\": 60, \"T3_black_bowl_drawer\": 70, \"T4_white_mug_left_plate\": 46, \"T5_book_back_shelf\": 52, \"T6_white_mug_plate\": 10, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 18, \"T9_yellow_white_mug_microwave\": 68}}}, \"eval_pi05_attention_k085_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 51.6, \"total_episodes\": 500, \"per_task\": {\"T0_alphabet_soup_tomato\": 20, \"T1_cream_cheese_butter\": 54, \"T2_stove_moka_pot\": 32, \"T3_black_bowl_drawer\": 60, \"T4_white_mug_left_plate\": 48, \"T5_book_back_shelf\": 90, \"T6_white_mug_plate\": 68, \"T7_alphabet_soup_cream\": 46, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 92}}}, \"eval_pi05_random_k05_long_seed42_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 50.2, \"total_successes\": 251, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 84, \"T1_cream_cheese_butter\": 32, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 72, \"T4_white_mug_left_plate\": 74, \"T5_book_back_shelf\": 38, \"T6_white_mug_plate\": 30, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 4, \"T9_yellow_mug_microwave\": 50}, \"elapsed_minutes\": 252.3, \"seed\": 42}}, \"eval_pi05_random_k075_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 62.4, \"suite\": \"libero_10\", \"tasks_completed\": 10, \"total_episodes\": 500}}, \"eval_pi05_random_k085_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 44.4, \"total_success\": 222, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 52, \"T1_cream_cheese_butter\": 46, \"T2_stove_moka_pot\": 58, \"T3_black_bowl_drawer\": 74, \"T4_white_mug_left_plate\": 12, \"T5_book_back_shelf\": 32, \"T6_white_mug_plate\": 42, \"T7_alphabet_soup_cream\": 44, \"T8_moka_pots_stove\": 10, \"T9_yellow_white_mug_microwave\": 74}, \"runtime_min\": 267.8}}, \"eval_openvla_random_k095_goal_seed42_v2\": {\"status\": \"RUNNING\"}, \"eval_openvla_attn_k05_goal_seed42_v3\": {\"status\": \"RUNNING\"}, \"eval_openvla_l2norm_k095_object_seed42\": {\"status\": \"RUNNING\"}, \"eval_openvla_random_k095_goal_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_random_k095_long_seed42_v2\": {\"status\": \"PREPARING\"}, \"eval_openvla_attn_k075_goal_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k05_goal_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_l2norm_k075_long_seed42_v2\": {\"status\": \"RUNNING\"}, \"eval_openvla_random_k05_object_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_l2norm_k075_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k07_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 24, \"total_successes\": 120, \"total_episodes\": 500}}, \"eval_openvla_attn_k05_long_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 14.6, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.5, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_openvla_attn_k095_long_seed42\": {\"status\": \"RUNNING\"}, \"eval_openvla_l2norm_k095_long_seed42\": {\"status\": \"RUNNING\"}, \"eval_openvla_l2norm_k05_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_random_k085_long_seed42_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.45, \"n_episodes\": 500, \"task_sr\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0.6, \"put_both_cream_cheese_and_butter_in_basket\": 0.64, \"turn_on_stove_put_moka_pot\": 0.6, \"put_black_bowl_in_bottom_drawer\": 0.32, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.2, \"pick_up_book_place_in_caddy\": 0.76, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.3, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0.6, \"put_both_moka_pots_on_stove\": 0.32, \"put_yellow_white_mug_in_microwave\": 0.16}}}, \"eval_openvla_random_k095_long_seed42\": {\"status\": \"RUNNING\"}, \"eval_openvla_random_k05_goal_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.522, \"total_successes\": 261, \"total_episodes\": 500}}, \"eval_pi05_attn_k095_long_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 77, \"n_episodes\": 500, \"task_sr\": {\"T0\": null, \"T1\": null, \"T2\": null, \"T3\": null, \"T4\": null, \"T5\": null, \"T6\": 14, \"T7\": 80, \"T8\": 30, \"T9\": 98}}}, \"eval_openvla_l2norm_k075_goal_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 70.2, \"task_srs\": [54, 80, 86, 22, 88, 70, 68, 98, 82, 54], \"episodes\": 500, \"tasks\": 10, \"time_min\": 198, \"tokens_256_to_192\": true}}, \"eval_openvla_attn_k085_long_seed42_v5\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 45.8, \"task_srs\": [60, 58, 56, 34, 38, 66, 34, 66, 24, 22], \"episodes\": 500, \"tasks\": 10, \"time_min\": 548.6, \"tokens_256_to_217\": true}}, \"eval_openvla_attn_k075_object_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 53.2, \"total_success\": 266, \"total_episodes\": 500, \"per_task_sr\": {\"alphabet_soup\": 56, \"cream_cheese\": 28, \"salad_dressing\": 70, \"bbq_sauce\": 34, \"ketchup\": 76, \"tomato_sauce\": 30, \"butter\": 28, \"milk\": 54, \"chocolate_pudding\": 86, \"orange_juice\": 70}, \"eval_time_min\": 272}}, \"eval_openvla_random_k085_object_seed42_v2\": {\"status\": \"PREPARING\"}, \"eval_openvla_l2norm_k085_object_seed42\": {\"status\": \"PREPARING\"}, \"eval_pi05_l2norm_k075_long_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 73.4, \"per_task\": {\"T0_soup_tomato\": 96, \"T1_cream_butter\": 94, \"T2_stove_moka\": 82, \"T3_bowl_drawer\": 70, \"T4_mug_plate\": 68, \"T5_book_back\": 84, \"T6_mug_plate_tomato\": 52, \"T7_soup_cream\": 76, \"T8_moka_pots\": 28, \"T9_mug_microwave\": 84}}}, \"eval_pi05_l2norm_k05_spatial_seed42_postfix\": {\"metrics\": {\"elapsed_min\": 149.18, \"overall_sr\": 0.574, \"per_task_sr\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.8, \"pick_up_black_bowl_from_table_center\": 0.9, \"pick_up_black_bowl_in_top_drawer\": 0.32, \"pick_up_black_bowl_next_to_cookie_box\": 0.28, \"pick_up_black_bowl_next_to_plate\": 0.74, \"pick_up_black_bowl_next_to_ramekin\": 0.9, \"pick_up_black_bowl_on_cookie_box\": 0.26, \"pick_up_black_bowl_on_ramekin\": 0.34, \"pick_up_black_bowl_on_stove\": 0.76, \"pick_up_black_bowl_on_wooden_cabinet\": 0.44}, \"total_episodes\": 500, \"total_successes\": 287}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed43_postfix\": {\"metrics\": {\"overall_sr\": 0.418, \"total_episodes\": 500, \"total_successes\": 209}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed42_postfix\": {\"metrics\": {\"overall_sr\": 0.366, \"total_episodes\": 500, \"total_successes\": 183}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_long_seed43_postfix\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.356, \"total_episodes\": 500, \"total_successes\": 178}}, \"eval_pi05_attention_k05_long_seed42_v3\": {\"status\": \"PREPARING\"}, \"eval_openvla_random_k085_object_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed42_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 78.8, \"total_episodes\": 500, \"total_successes\": 394, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 98, \"T1_cream_cheese_butter\": 94, \"T2_stove_moka_pot\": 88, \"T3_black_bowl_drawer\": 98, \"T4_white_mug_left_plate\": 72, \"T5_book_back\": 98, \"T6_white_mug_plate\": 6, \"T7_alphabet_soup_cream\": 86, \"T8_moka_pots_stove\": 54, \"T9_yellow_white_mug_microwave\": 94}}}, \"eval_openvla_l2norm_k075_object_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.574, \"total_episodes\": 500, \"successful_episodes\": 287, \"task_sr\": {\"alphabet_soup\": 0.78, \"cream_cheese\": 0.28, \"salad_dressing\": 0.68, \"bbq_sauce\": 0.46, \"ketchup\": 0.86, \"tomato_sauce\": 0.66, \"butter\": 0.4, \"milk\": 0.48, \"chocolate_pudding\": 0.46, \"orange_juice\": 0.68}, \"time_min\": 289.4}}, \"eval_openvla_attn_k07_goal_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.664, \"total_episodes\": 500, \"total_successes\": 332}}, \"eval_openvla_l2norm_k075_goal_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_l2norm_k07_goal_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.684, \"total_episodes\": 500, \"per_task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_bowl_on_the_stove\": 0.86, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.74, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.16, \"put_the_bowl_on_top_of_the_cabinet\": 0.84, \"push_the_plate_to_the_front_of_the_stove\": 0.66, \"put_the_cream_cheese_in_the_bowl\": 0.74, \"turn_on_the_stove\": 0.98, \"put_the_bowl_on_the_plate\": 0.7, \"put_the_wine_bottle_on_the_rack\": 0.56}}}, \"eval_openvla_attn_k05_goal_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 44.2, \"total_episodes\": 500, \"total_successes\": 221, \"source\": \"result file found on westd-27271 by audit worker, needs verification\"}}, \"eval_openvla_attn_k07_object_seed42_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 43.8, \"total_episodes\": 500, \"total_successes\": 219}}, \"eval_openvla_random_k05_object_seed42_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 35.8, \"total_episodes\": 500, \"total_successes\": 179, \"per_task\": {\"alphabet_soup\": 56, \"bbq_sauce\": 58, \"butter\": 0, \"chocolate_pudding\": 30, \"cream_cheese\": 2, \"ketchup\": 60, \"milk\": 12, \"orange_juice\": 74, \"salad_dressing\": 40, \"tomato_sauce\": 26}}}, \"eval_openvla_random_k05_object_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_random_k05_goal_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.522, \"total_successes\": 261, \"total_episodes\": 500, \"per_task_sr\": {\"open_middle_drawer\": 0.44, \"bowl_on_stove\": 0.64, \"wine_bottle_on_cabinet\": 0.64, \"open_drawer_put_bowl\": 0.1, \"bowl_on_cabinet\": 0.74, \"push_plate_stove\": 0.54, \"cream_cheese_in_bowl\": 0.48, \"turn_on_stove\": 0.94, \"bowl_on_plate\": 0.46, \"wine_bottle_on_rack\": 0.24}, \"source\": \"v1 results (v2 process died early)\", \"elapsed_minutes\": 230.08}}, \"eval_openvla_random_k05_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 18.6, \"n_episodes\": 500}}, \"eval_openvla_l2norm_k05_goal_seed42\": {\"metrics\": {\"overall_sr\": 0.434, \"total_successes\": 217, \"total_episodes\": 500, \"elapsed_min\": 386.1}, \"status\": \"DONE\"}, \"eval_openvla_random_k07_goal_seed42_v4\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 68.4}}, \"eval_openvla_attn_k05_object_seed42\": {\"status\": \"DEPLOYED\"}, \"eval_openvla_random_k085_goal_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 78.6, \"task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 70, \"put_the_bowl_on_the_stove\": 92, \"put_the_wine_bottle_on_top_of_the_cabinet\": 84, \"open_the_top_drawer_and_put_the_bowl_inside\": 30, \"put_the_bowl_on_top_of_the_cabinet\": 98, \"push_the_plate_to_the_front_of_the_stove\": 88, \"put_the_cream_cheese_in_the_bowl\": 70, \"turn_on_the_stove\": 98, \"put_the_bowl_on_the_plate\": 86, \"put_the_wine_bottle_on_the_rack\": 70}}}, \"eval_openvla_attn_k07_object_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"status\": \"CRASHED at Task 7/10 ep 10/50\", \"completed_tasks\": 6, \"total_tasks\": 10, \"partial_per_task_sr\": {\"task1_alphabet_soup\": 0.38, \"task2_cream_cheese\": 0.12, \"task3_salad_dressing\": 0.66, \"task4_bbq_sauce\": 0.3, \"task5_ketchup\": 0.62, \"task6_tomato_sauce\": 0.32}, \"partial_avg_sr\": 0.4, \"note\": \"Process silently died during Task 7 (no error/traceback in log). Likely OOM or external kill. v2 was already a re-run of v1 which also crashed at Task 6.\"}}, \"eval_pi05_random_k085_long_seed42\": {\"metrics\": {\"overall_SR\": 0.444, \"total_episodes\": 500, \"total_successes\": 222}, \"status\": \"DONE\"}, \"eval_openvla_attn_k085_goal_seed42_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 74.6, \"per_task\": {\"T1_open_drawer\": 52, \"T2_bowl_stove\": 88, \"T3_wine_cabinet\": 76, \"T4_drawer_bowl\": 44, \"T5_bowl_cabinet\": 98, \"T6_plate_stove\": 84, \"T7_cream_bowl\": 74, \"T8_stove_on\": 94, \"T9_bowl_plate\": 78, \"T10_wine_rack\": 58}}}, \"eval_openvla_l2norm_k085_goal_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 75.4, \"per_task\": {\"T1_open_drawer\": 66, \"T2_bowl_stove\": 96, \"T3_wine_cabinet\": 74, \"T4_drawer_bowl\": 30, \"T5_bowl_cabinet\": 96, \"T6_plate_stove\": 78, \"T7_cream_bowl\": 74, \"T8_stove_on\": 94, \"T9_bowl_plate\": 84, \"T10_wine_rack\": 62}}}, \"eval_pi05_attention_k085_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_random_k07_goal_seed42_v3\": {\"status\": \"PREPARING\"}, \"eval_openvla_random_k07_goal_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k085_long_seed42_v3\": {\"metrics\": {\"k_ratio\": 0.85, \"mode\": \"attention_prune\", \"note\": \"result file misnamed as openvla_l2norm_prune_k085_10.json, actual mode is attention_prune\", \"overall_sr\": 45.8, \"seed\": 42, \"suite\": \"libero_10\", \"total_episodes\": 500, \"total_successes\": 229}, \"status\": \"DONE\"}, \"eval_openvla_random_k07_goal_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k085_long_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k085_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k09_goal_seed43_v4\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 73.2, \"total_successes\": 366, \"total_episodes\": 500, \"per_task_sr\": {\"T0_open_middle_drawer\": 50, \"T1_put_bowl_on_stove\": 86, \"T2_put_wine_bottle_on_cabinet\": 88, \"T3_open_drawer_put_bowl\": 40, \"T4_put_bowl_on_cabinet\": 94, \"T5_push_plate_to_stove\": 84, \"T6_put_cream_cheese_in_bowl\": 66, \"T7_turn_on_stove\": 98, \"T8_put_bowl_on_plate\": 78, \"T9_put_wine_bottle_on_rack\": 48}, \"elapsed_minutes\": 205.3, \"seed\": 43}}, \"eval_pi05_attention_k05_long_seed42\": {\"metrics\": {\"episodes\": 500, \"result_sr\": 49.4}, \"status\": \"DEPLOYED\"}, \"eval_openvla_attn_k085_object_seed42\": {\"metrics\": {\"elapsed_minutes\": 259.3, \"per_task\": {\"alphabet_soup\": 0.66, \"bbq_sauce\": 0.36, \"butter\": 0.36, \"chocolate_pudding\": 0.88, \"cream_cheese\": 0.36, \"ketchup\": 0.74, \"milk\": 0.52, \"orange_juice\": 0.74, \"salad_dressing\": 0.52, \"tomato_sauce\": 0.36}, \"success_rate\": 0.55, \"total_episodes\": 500, \"total_successes\": 275}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k09_goal_seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 75.2, \"total_successes\": 376, \"total_episodes\": 500, \"per_task_sr\": {\"T0_open_middle_drawer\": 66, \"T1_put_bowl_on_stove\": 92, \"T2_put_wine_bottle_on_cabinet\": 82, \"T3_open_drawer_put_bowl\": 38, \"T4_put_bowl_on_cabinet\": 94, \"T5_push_plate_to_stove\": 72, \"T6_put_cream_cheese_in_bowl\": 74, \"T7_turn_on_stove\": 94, \"T8_put_bowl_on_plate\": 80, \"T9_put_wine_bottle_on_rack\": 60}, \"elapsed_minutes\": 185.7, \"seed\": 43}}, \"eval_openvla_random_k09_goal_seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 80.4, \"total_successes\": 402, \"total_episodes\": 500, \"per_task_sr\": {\"T0_open_middle_drawer\": 70, \"T1_put_bowl_on_stove\": 98, \"T2_put_wine_bottle_on_cabinet\": 92, \"T3_open_drawer_put_bowl\": 42, \"T4_put_bowl_on_cabinet\": 94, \"T5_push_plate_to_stove\": 78, \"T6_put_cream_cheese_in_bowl\": 82, \"T7_turn_on_stove\": 100, \"T8_put_bowl_on_plate\": 74, \"T9_put_wine_bottle_on_rack\": 74}, \"elapsed_minutes\": 175.5, \"seed\": 43}}, \"eval_openvla_l2norm_k09_goal_seed43_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.752, \"total_successes\": 376, \"total_episodes\": 500, \"per_task_sr\": {\"T0_open_middle_drawer\": 0.66, \"T1_put_bowl_on_stove\": 0.92, \"T2_put_wine_bottle_on_cabinet\": 0.82, \"T3_open_drawer_put_bowl\": 0.38, \"T4_put_bowl_on_cabinet\": 0.94, \"T5_push_plate_to_stove\": 0.72, \"T6_put_cream_cheese_in_bowl\": 0.74, \"T7_turn_on_stove\": 0.94, \"T8_put_bowl_on_plate\": 0.8, \"T9_put_wine_bottle_on_rack\": 0.6}, \"elapsed_minutes\": 210.5, \"seed\": 43}}, \"eval_openvla_attn_k07_object_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_attention_k075_long_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 51.8, \"total_successes\": 259, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 68, \"T1_cream_cheese_butter\": 78, \"T2_stove_moka_pot\": 56, \"T3_black_bowl_drawer\": 42, \"T4_white_mug_plate\": 36, \"T5_book_back\": 44, \"T6_white_mug_plate_2\": 80, \"T7_alphabet_soup_cream\": 30, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 78}}}, \"eval_openvla_l2norm_k09_goal_seed43_v2\": {\"status\": \"DONE\"}, \"eval_openvla_baseline_spatial_seed42_v4\": {\"status\": \"DONE\"}, \"eval_openvla_l2norm_k07_object_seed42_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.498, \"total_episodes\": 500, \"total_successes\": 249, \"task_srs\": {\"task1\": 0.46, \"task2\": 0.66, \"task3\": 0.48, \"task4\": 0.32, \"task5\": 0.76, \"task6\": 0.62, \"task7\": 0.28, \"task8\": 0.56, \"task9\": 0.46, \"task10\": 0.68}}}, \"eval_openvla_l2norm_k07_object_seed42\": {\"metrics\": {\"failure_reason\": \"AutoDL container restart at 14:50:19 UTC killed process. Was at Task 4/10 (~40%). GPU count dropped from 4 to 1 after restart.\"}, \"status\": \"DEPLOYED\"}, \"eval_smolvla_official_l2norm_k070_object_seed42\": {\"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_pi05_zeromask_random_k09_object_seed42_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.98, \"total_successes\": 490, \"total_episodes\": 500, \"elapsed_min\": 83.05, \"per_task_sr\": {\"T0_alphabet_soup\": 0.96, \"T1_cream_cheese\": 0.96, \"T2_salad_dressing\": 1, \"T3_bbq_sauce\": 0.94, \"T4_ketchup\": 0.98, \"T5_tomato_sauce\": 1, \"T6_butter\": 1, \"T7_milk\": 0.98, \"T8_chocolate_pudding\": 1, \"T9_orange_juice\": 0.98}}}, \"eval_pi05_random_k05_long_seed42\": {\"metrics\": {\"elapsed_min\": 157.7, \"overall_sr\": 0.502, \"total_episodes\": 500, \"total_successes\": 251}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_long_seed42\": {\"metrics\": {\"elapsed_min\": 158, \"success_rate\": 0.502, \"total_episodes\": 500, \"total_successes\": 251}, \"status\": \"DONE\"}, \"eval_openvla_random_k05_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k09_goal_seed43_v3\": {\"status\": \"PREPARING\"}, \"eval_openvla_attn_k09_goal_seed43_v2\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_goal_seed42_postfix\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.518, \"total_successes\": 259, \"total_episodes\": 500, \"n_tasks\": 10, \"seed\": 42}}, \"l2norm_k05_object_s42\": {\"metrics\": {\"elapsed_minutes\": 264.6, \"k_ratio\": 0.5, \"overall_success_rate\": 0.392, \"per_task\": {\"alphabet_soup\": 0.56, \"bbq_sauce\": 0.32, \"butter\": 0.12, \"chocolate_pudding\": 0.44, \"cream_cheese\": 0.14, \"ketchup\": 0.7, \"milk\": 0.5, \"orange_juice\": 0.44, \"salad_dressing\": 0.38, \"tomato_sauce\": 0.32}, \"seed\": 42, \"total_episodes\": 500, \"total_successes\": 196, \"vision_tokens\": \"256->128\"}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_spatial_seed43\": {\"metrics\": {\"overall_sr\": 0.726, \"total_episodes\": 500, \"total_successes\": 363, \"wilson_ci_95\": [0.685, 0.763], \"elapsed_min\": 64.3}, \"status\": \"DONE\"}, \"eval_openvla_baseline_goal_seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.776, \"total_successes\": 388, \"total_episodes\": 500, \"elapsed_minutes\": 193, \"seed\": 43, \"per_task_sr\": {\"T1_open_middle_drawer\": 0.58, \"T2_put_bowl_on_stove\": 0.96, \"T3_put_wine_bottle_on_cabinet\": 0.82, \"T4_open_top_drawer_put_bowl\": 0.58, \"T5_put_bowl_on_cabinet\": 0.98, \"T6_push_plate_front_stove\": 0.8, \"T7_put_cream_cheese_in_bowl\": 0.66, \"T8_turn_on_stove\": 0.98, \"T9_put_bowl_on_plate\": 0.86, \"T10_put_wine_bottle_on_rack\": 0.54}}}, \"eval_openvla_l2norm_k07_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.312, \"task_srs\": [0.42, 0.34, 0.36, 0.16, 0.2, 0.58, 0.42, 0.4, 0.08, 0.16], \"n_episodes\": 500, \"n_tasks\": 10, \"time_min\": 563}}, \"eval_openvla_random_k07_object_seed42_v3\": {\"status\": \"DONE\"}, \"eval_pi05_attention_k0925_long_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k075_long_seed42_v2\": {\"status\": \"DONE\"}, \"eval_pi05_zeromask_random_k09_object_seed42_v2\": {\"status\": \"DONE\"}, \"eval_pi05_random_k075_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_l2norm_k085_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.388, \"total_episodes\": 500, \"total_successes\": 194, \"elapsed_minutes\": 521.4, \"seed\": 42, \"k_ratio\": 0.85, \"suite\": \"libero_10_long\", \"per_task_sr\": {\"task1_alphabet_soup_tomato_sauce_basket\": 0.62, \"task2_cream_cheese_butter_basket\": 0.48, \"task3_stove_moka_pot\": 0.44, \"task4_black_bowl_drawer_close\": 0.28, \"task5_white_mug_left_yellow_mug_right\": 0.18, \"task6_book_caddy\": 0.84, \"task7_white_mug_plate_chocolate_pudding\": 0.3, \"task8_alphabet_soup_cream_cheese_basket\": 0.38, \"task9_both_moka_pots_stove\": 0.2, \"task10_yellow_mug_microwave_close\": 0.16}}}, \"eval_openvla_random_k07_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.388, \"total_successes\": 194, \"total_episodes\": 500, \"elapsed_minutes\": 516.7, \"seed\": 42, \"per_task_sr\": {\"put both the alphabet soup and the tomato sauce in the basket\": 0.48, \"put both the cream cheese box and the butter in the basket\": 0.46, \"turn on the stove and put the moka pot on it\": 0.58, \"put the black bowl in the bottom drawer of the cabinet and close it\": 0.34, \"put the white mug on the left plate and put the yellow and white mug on the right plate\": 0.14, \"pick up the book and place it in the back compartment of the caddy\": 0.68, \"put the white mug on the plate and put the chocolate pudding to the right of the plate\": 0.42, \"put both the alphabet soup and the cream cheese box in the basket\": 0.34, \"put both moka pots on the stove\": 0.24, \"put the yellow and white mug in the microwave and close it\": 0.2}}}, \"eval_pi05_l2norm_k075_long_seed42_v3\": {\"status\": \"DEPLOYED\"}, \"eval_openvla_attn_k085_long_seed42_v4\": {\"status\": \"DONE\"}, \"eval_openvla_random_k085_long_seed42_v2\": {\"status\": \"PREPARING\"}, \"eval_openvla_random_k07_object_seed42_v2\": {\"metrics\": {\"elapsed_minutes\": 274.4, \"overall_sr\": 0.444, \"per_task\": {\"alphabet_soup\": 0.72, \"bbq_sauce\": 0.38, \"butter\": 0.2, \"chocolate_pudding\": 0.34, \"cream_cheese\": 0.2, \"ketchup\": 0.64, \"milk\": 0.24, \"orange_juice\": 0.64, \"salad_dressing\": 0.56, \"tomato_sauce\": 0.52}, \"total_episodes\": 500, \"total_successes\": 222}, \"status\": \"DONE\"}, \"eval_openvla_random_k085_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k09_goal_seed43\": {\"status\": \"DONE\"}, \"profiling_pi05_latency_westd41074\": {\"status\": \"DONE\", \"metrics\": {\"k1.0_median_ms\": 209.88, \"k1.0_p5_ms\": 197.76, \"k1.0_p95_ms\": 221.67, \"k0.9_median_ms\": 206.36, \"k0.9_p5_ms\": 171.43, \"k0.9_p95_ms\": 225.03, \"k0.5_median_ms\": 201.87, \"k0.5_p5_ms\": 189.21, \"k0.5_p95_ms\": 211.31, \"k0.9_speedup_pct\": 1.7, \"k0.5_speedup_pct\": 4}}, \"eval_openvla_zeromask_l2norm_k09_object_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_SR\": 0.688, \"per_task_SR\": {\"alphabet_soup\": 0.84, \"cream_cheese\": 0.62, \"salad_dressing\": 0.88, \"bbq_sauce\": 0.26, \"ketchup\": 0.82, \"tomato_sauce\": 0.54, \"butter\": 0.62, \"milk\": 0.82, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.88}, \"total_episodes\": 500, \"total_successes\": 344}}, \"eval_pi05_l2norm_k0925_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_object_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_zeromask_random_k09_object_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.718, \"per_task\": {\"alphabet_soup\": 0.9, \"cream_cheese\": 0.54, \"salad_dressing\": 0.78, \"bbq_sauce\": 0.62, \"ketchup\": 0.8, \"tomato_sauce\": 0.68, \"butter\": 0.5, \"milk\": 0.74, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.92}, \"elapsed_minutes\": 246.4}}, \"eval_pi05_zeromask_l2norm_k09_object_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.994, \"total_successes\": 497, \"total_episodes\": 500, \"elapsed_min\": 97.4}}, \"eval_pi05_zeromask_random_k09_object_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.832, \"total_episodes\": 500, \"elapsed_min\": 168.6, \"per_task_sr\": [0.92, 0.92, 0.68, 0.98, 0.9, 0.94, 0.92, 0.44, 0.98, 0.64]}}, \"profiling_pi05_latency_westd41074_v2\": {\"status\": \"DONE\"}, \"profiling_pi05_latency_cqa1\": {\"status\": \"DONE\", \"metrics\": {\"k_1.0_mean_ms\": 200.06, \"k_1.0_std_ms\": 26.33, \"k_0.9_mean_ms\": 206.66, \"k_0.9_std_ms\": 42.1, \"k_0.5_mean_ms\": 185.95, \"k_0.5_std_ms\": 20.01, \"speedup_k09\": 0.968, \"speedup_k05\": 1.076}}, \"eval_pi05_l2norm_k05_long_seed43_postfix_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.53, \"total_successes\": 265, \"total_episodes\": 500, \"elapsed_min\": 214.5, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 0.64, \"T1_cream_cheese_butter\": 0.64, \"T2_stove_moka_pot\": 0.72, \"T3_black_bowl_drawer\": 0.46, \"T4_white_mug_yellow_mug\": 0.4, \"T5_book_caddy\": 0.5, \"T6_white_mug_chocolate\": 0.38, \"T7_alphabet_soup_cream_cheese\": 0.58, \"T8_both_moka_pots\": 0.1, \"T9_yellow_mug_microwave\": 0.88}}}, \"eval_pi05_random_k0925_long_seed42_postfix\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 38.6, \"total_episodes\": 500, \"total_success\": 193, \"per_task_sr\": [22, 66, 42, 44, 22, 52, 4, 50, 4, 80], \"runtime_min\": 257.9}}, \"eval_openvla_random_k07_long_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_attention_k09_long_seed42_postfix\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.638, \"total_successes\": 319, \"total_episodes\": 500}}, \"eval_openvla_l2norm_k085_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_l2norm_k07_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_random_k05_spatial_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.5, \"total_episodes\": 500, \"total_success\": 250, \"wall_time_min\": 248.8}}, \"eval_openvla_attn_k07_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_spatial_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k09_object_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_random_k07_long_seed43_postfix\": {\"metrics\": {\"elapsed_min\": 222.9, \"overall_sr\": 0.686, \"per_task_sr\": {\"T0\": 0.92, \"T1\": 0.74, \"T2\": 0.76, \"T3\": 0.7, \"T4\": 0.86, \"T5\": 0.52, \"T6\": 0.7, \"T7\": 0.72, \"T8\": 0.08, \"T9\": 0.86}, \"total_episodes\": 500, \"total_successes\": 343}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_long_seed43_v4\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.272, \"total_successes\": 136, \"total_episodes\": 500, \"elapsed_min\": 284.7}}, \"eval_pi05_l2norm_k07_long_seed43_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.65, \"total_successes\": 325, \"total_episodes\": 500, \"elapsed_min\": 228.5}}, \"eval_openvla_l2norm_k09_long_seed42_v3\": {\"metrics\": {\"k_ratio\": 0.9, \"mode\": \"l2norm_prune\", \"overall_sr\": 43.6, \"seed\": 42, \"suite\": \"libero_10\", \"total_episodes\": 500, \"total_successes\": 218}, \"status\": \"DONE\"}, \"eval_openvla_attn_k09_long_seed42_v3\": {\"metrics\": {\"k_ratio\": 0.9, \"mode\": \"attention_prune\", \"note\": \"result file misnamed openvla_l2norm_prune_k09_10.json; backed up to openvla_attn_prune_k09_long_seed42.json\", \"overall_sr\": 44.0, \"seed\": 42, \"suite\": \"libero_10\", \"total_episodes\": 500, \"total_successes\": 220}, \"status\": \"DONE\"}, \"eval_openvla_random_k09_long_seed42_v3\": {\"metrics\": {\"k_ratio\": 0.9, \"mode\": \"random_prune\", \"note\": \"result file generic name openvla_random_prune_k09_10.json, needs rename\", \"overall_sr\": 46.8, \"seed\": 42, \"suite\": \"libero_10\", \"total_episodes\": 500, \"total_successes\": 234}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43_v3\": {\"metrics\": {\"per_task\": {\"T0_put_both_alphabet_soup_and_tomato\": 96, \"T1_put_both_cream_cheese_and_butter\": 92, \"T2_turn_on_stove_put_moka_pot\": 86, \"T3_put_black_bowl_in_bottom_drawer\": 100, \"T4_put_white_mug_on_left_plate\": 78, \"T5_pick_up_book_place_in_back\": 98, \"T6_put_white_mug_on_plate_and_put\": 14, \"T7_put_both_alphabet_soup_and_cream\": 90, \"T8_put_both_moka_pots_on_stove\": 52, \"T9_put_yellow_white_mug_in_microwave\": 94}, \"success_rate\": 80, \"total_episodes\": 500, \"total_successes\": 400}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_long_seed43_postfix\": {\"metrics\": {\"elapsed_min\": 194.3, \"overall_sr\": 0.808, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 0.92, \"T1_cream_cheese_butter\": 0.96, \"T2_stove_moka\": 0.92, \"T3_black_bowl_drawer\": 1, \"T4_white_mug_plates\": 0.88, \"T5_book_caddy\": 0.96, \"T6_mug_plate_pudding\": 0.14, \"T7_soup_cream_cheese_basket\": 0.82, \"T8_two_moka_stove\": 0.58, \"T9_mug_microwave\": 0.9}, \"total_episodes\": 500, \"total_successes\": 404}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k03_seed42\": {\"metrics\": {\"elapsed_minutes\": 374.64, \"k_ratio\": 0.3, \"overall_success_rate\": 0.206, \"seed\": 42, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 103}, \"status\": \"DONE\"}, \"random_k07_seed43_object\": {\"metrics\": {\"elapsed_minutes\": 270.07, \"k_ratio\": 0.7, \"overall_success_rate\": 0.512, \"per_task\": {\"alphabet_soup\": {\"ep\": 50, \"sr\": 0.74, \"succ\": 37}, \"bbq_sauce\": {\"ep\": 50, \"sr\": 0.56, \"succ\": 28}, \"butter\": {\"ep\": 50, \"sr\": 0.2, \"succ\": 10}, \"chocolate_pudding\": {\"ep\": 50, \"sr\": 0.42, \"succ\": 21}, \"cream_cheese\": {\"ep\": 50, \"sr\": 0.14, \"succ\": 7}, \"ketchup\": {\"ep\": 50, \"sr\": 0.72, \"succ\": 36}, \"milk\": {\"ep\": 50, \"sr\": 0.3, \"succ\": 15}, \"orange_juice\": {\"ep\": 50, \"sr\": 0.84, \"succ\": 42}, \"salad_dressing\": {\"ep\": 50, \"sr\": 0.58, \"succ\": 29}, \"tomato_sauce\": {\"ep\": 50, \"sr\": 0.62, \"succ\": 31}}, \"seed\": 43, \"total_episodes\": 500, \"total_successes\": 256, \"vision_tokens\": 179}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_goal_seed42_postfix\": {\"metrics\": {\"baseline_sr\": 96.4, \"delta_vs_baseline\": -6.6, \"success_rate\": 89.8, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_object_seed42_v4\": {\"metrics\": {\"baseline_sr\": 0.74, \"delta_from_baseline\": -0.348, \"elapsed_minutes\": 346.85, \"k_ratio\": 0.5, \"per_task_rates\": {\"alphabet_soup\": 0.56, \"bbq_sauce\": 0.32, \"butter\": 0.12, \"chocolate_pudding\": 0.44, \"cream_cheese\": 0.14, \"ketchup\": 0.7, \"milk\": 0.5, \"orange_juice\": 0.44, \"salad_dressing\": 0.38, \"tomato_sauce\": 0.32}, \"success_rate\": 0.392, \"total_episodes\": 500, \"total_successes\": 196, \"vision_tokens_kept\": 128, \"vision_tokens_total\": 256}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed42_postfix_v3\": {\"metrics\": {\"per_task_sr\": {\"T0_alphabet_soup_tomato\": 52, \"T1_cream_cheese_butter\": 46, \"T2_stove_moka_pot\": 66, \"T3_black_bowl_drawer\": 74, \"T4_white_mug_left_plate\": 24, \"T5_book_back_shelf\": 44, \"T6_white_mug_plate\": 52, \"T7_alphabet_soup_cream\": 52, \"T8_both_moka_pots_stove\": 12, \"T9_yellow_white_mug_microwave\": 72}, \"success_rate\": 49.4, \"total_episodes\": 500, \"total_successes\": 247}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed42_postfix_v3\": {\"metrics\": {\"per_task\": {\"T0_alphabet_soup_tomato\": 0.98, \"T1_cream_cheese_butter\": 0.94, \"T2_stove_moka\": 0.82, \"T3_black_bowl_drawer\": 1, \"T4_white_mug_yellow_mug\": 0.72, \"T5_book_caddy\": 0.96, \"T6_white_mug_chocolate\": 0.08, \"T7_alphabet_soup_cream_cheese\": 0.8, \"T8_both_moka_pots\": 0.56, \"T9_yellow_white_mug_microwave\": 0.94}, \"success_rate\": 0.78, \"total_episodes\": 500, \"total_successes\": 390}, \"status\": \"DONE\"}, \"eval_openvla_random_k09_spatial_seed42\": {\"metrics\": {\"elapsed_min\": 252.4, \"overall_sr\": 79.8, \"total_episodes\": 500, \"total_successes\": 399}, \"status\": \"DONE\"}, \"eval_openvla_random_k09_goal_seed42\": {\"metrics\": {\"elapsed_min\": 246.2, \"overall_sr\": 79.6, \"per_task\": {\"T0_open_middle_drawer_cabinet\": {\"episodes\": 50, \"sr\": 74, \"successes\": 37}, \"T1_put_bowl_on_stove\": {\"episodes\": 50, \"sr\": 96, \"successes\": 48}, \"T2_put_wine_bottle_top_cabinet\": {\"episodes\": 50, \"sr\": 84, \"successes\": 42}, \"T3_open_top_drawer_put_bowl_in\": {\"episodes\": 50, \"sr\": 38, \"successes\": 19}, \"T4_put_bowl_top_cabinet\": {\"episodes\": 50, \"sr\": 94, \"successes\": 47}, \"T5_push_plate_front_stove\": {\"episodes\": 50, \"sr\": 72, \"successes\": 36}, \"T6_put_cream_cheese_in_bowl\": {\"episodes\": 50, \"sr\": 78, \"successes\": 39}, \"T7_turn_on_stove\": {\"episodes\": 50, \"sr\": 100, \"successes\": 50}, \"T8_put_bowl_on_plate\": {\"episodes\": 50, \"sr\": 86, \"successes\": 43}, \"T9_put_wine_bottle_on_rack\": {\"episodes\": 50, \"sr\": 74, \"successes\": 37}}, \"total_episodes\": 500, \"total_successes\": 398}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed42_postfix_v3\": {\"metrics\": {\"elapsed_min\": 139.3, \"overall_sr\": 53, \"per_task\": {\"T0_open_middle_drawer_cabinet\": {\"episodes\": 50, \"sr\": 84, \"successes\": 42}, \"T1_put_bowl_on_stove\": {\"episodes\": 50, \"sr\": 2, \"successes\": 1}, \"T2_put_wine_bottle_top_cabinet\": {\"episodes\": 50, \"sr\": 18, \"successes\": 9}, \"T3_open_top_drawer_put_bowl_in\": {\"episodes\": 50, \"sr\": 34, \"successes\": 17}, \"T4_put_bowl_top_cabinet\": {\"episodes\": 50, \"sr\": 54, \"successes\": 27}, \"T5_push_plate_front_stove\": {\"episodes\": 50, \"sr\": 76, \"successes\": 38}, \"T6_put_cream_cheese_in_bowl\": {\"episodes\": 50, \"sr\": 82, \"successes\": 41}, \"T7_turn_on_stove\": {\"episodes\": 50, \"sr\": 88, \"successes\": 44}, \"T8_put_bowl_on_plate\": {\"episodes\": 50, \"sr\": 84, \"successes\": 42}, \"T9_put_wine_bottle_on_rack\": {\"episodes\": 50, \"sr\": 8, \"successes\": 4}}, \"total_episodes\": 500, \"total_successes\": 265}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed42_postfix_v2\": {\"metrics\": {\"success_rate\": 98.4, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_random_k09_object_seed42\": {\"metrics\": {\"elapsed_minutes\": 246.3, \"overall_success_rate\": 0.628, \"total_episodes\": 500, \"total_successes\": 314}, \"status\": \"DONE\"}, \"eval_openvla_baseline_object_seed42_v2\": {\"metrics\": {\"overall_sr\": 0.74, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed42_postfix_v2\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed42_postfix\": {\"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed42_postfix_v2\": {\"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed42_postfix_v2\": {\"status\": \"DONE\"}, \"eval_openvla_l2norm_k09_long_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_random_k09_long_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k09_long_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_random_k09_long_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43_postfix_v2\": {\"status\": \"DONE\"}, \"eval_openvla_l2norm_k09_long_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed42_postfix\": {\"metrics\": {\"per_task_sr\": {\"T0_alphabet_soup\": 6, \"T1_cream_cheese\": 2, \"T2_salad_dressing\": 2, \"T3_bbq_sauce\": 2, \"T4_ketchup\": 12, \"T5_tomato_sauce\": 8, \"T6_butter\": 4, \"T7_milk\": 8, \"T8_chocolate_pudding\": 4, \"T9_orange_juice\": 8}, \"success_rate\": 5.6, \"total_episodes\": 500, \"total_successes\": 28}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_goal_seed42_postfix\": {\"metrics\": {\"T0_open_drawer\": 90, \"T1_bowl_stove\": 92, \"T2_wine_cabinet\": 98, \"T3_drawer_bowl\": 84, \"T4_bowl_cabinet\": 100, \"T5_push_plate\": 94, \"T6_cream_bowl\": 88, \"T7_turn_stove\": 100, \"T8_bowl_plate\": 84, \"T9_wine_rack\": 44, \"overall_sr\": 87.4, \"total_episodes\": 500, \"total_successes\": 437}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_goal_seed43_postfix\": {\"metrics\": {\"success_rate\": 87, \"total_episodes\": 500, \"total_successes\": 435}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed43_v2\": {\"metrics\": {\"success_rate\": 42, \"total_episodes\": 500, \"total_successes\": 210}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed43_postfix\": {\"metrics\": {\"success_rate\": 59.2, \"total_episodes\": 500, \"total_successes\": 296}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed43_postfix\": {\"metrics\": {\"success_rate\": 99, \"total_episodes\": 500, \"total_successes\": 495}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k09_spatial_seed42\": {\"metrics\": {\"overall_sr\": 0.75, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k09_goal_seed42\": {\"metrics\": {\"overall_sr\": 0.748, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_baseline_spatial\": {\"metrics\": {\"elapsed_minutes\": 209.9, \"model\": \"openvla-7b-finetuned-libero-spatial\", \"seed\": 42, \"success_rate\": 0.8, \"suite\": \"libero_spatial\", \"total_episodes\": 500, \"total_successes\": 400}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed43_postfix\": {\"metrics\": {\"overall_sr\": 0.534, \"total_episodes\": 500, \"total_successes\": 267}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_spatial_seed43_postfix\": {\"metrics\": {\"overall_sr\": 0.882, \"total_episodes\": 500, \"total_successes\": 441}, \"status\": \"DONE\"}, \"eval_openvla_attn_k09_long_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_random_k09_spatial_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_random_k09_goal_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k085_spatial_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k085_goal_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k085_spatial_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_attn_k085_goal_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed43_postfix\": {\"metrics\": {\"elapsed_min\": 164.83, \"overall_sr\": 0.048, \"total_episodes\": 500, \"total_successes\": 24}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43_postfix\": {\"metrics\": {\"overall_sr\": 78.6, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"pi05_baseline_long_seed42\": {\"metrics\": {\"overall_sr\": 92.8, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_baseline_spatial_seed42\": {\"metrics\": {\"overall_sr\": 97.2, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_baseline_long_seed42\": {\"metrics\": {\"note\": \"Result from westd-38929 run (2026-05-22). Original cqa1-33015 run was stale. Second cqa1-33015 run=91.6%.\", \"overall_sr\": 92.8, \"per_task\": {\"alphabet_soup_cream_cheese_basket\": 0.9, \"alphabet_soup_tomato_basket\": 0.96, \"book_in_caddy\": 0.98, \"bowl_bottom_drawer\": 1, \"cream_cheese_butter_basket\": 0.96, \"moka_pots_stove\": 0.64, \"mug_microwave\": 0.98, \"mug_plate_chocolate\": 0.88, \"mugs_on_plates\": 1, \"stove_moka_pot\": 0.98}, \"source_file\": \"westd-38929:/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_baseline_libero_10_seed42.json\", \"total_episodes\": 500, \"total_successes\": 464}, \"status\": \"DONE\"}, \"eval_pi05_baseline_object_seed42\": {\"metrics\": {\"overall_sr\": 98.2, \"per_task\": {\"alphabet_soup\": 0.96, \"bbq_sauce\": 1, \"butter\": 1, \"chocolate_pudding\": 1, \"cream_cheese\": 0.98, \"ketchup\": 0.94, \"milk\": 0.98, \"orange_juice\": 0.98, \"salad_dressing\": 0.98, \"tomato_sauce\": 1}, \"source_file\": \"westd-41074:/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_baseline_libero_object.json\", \"total_episodes\": 500, \"total_successes\": 491}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_spatial_seed43_postfix_v2\": {\"metrics\": {\"elapsed_min\": 94.1, \"overall_sr\": 54, \"per_task_sr\": {\"T0\": 92, \"T1\": 44, \"T2\": 76, \"T3\": 10, \"T4\": 28, \"T5\": 58, \"T6\": 56, \"T7\": 72, \"T8\": 76, \"T9\": 28}, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_long_seed43_postfix\": {\"metrics\": {\"elapsed_min\": 250.5, \"overall_sr\": 46.8, \"per_task_sr\": {\"T0\": 72, \"T1\": 34, \"T2\": 64, \"T3\": 68, \"T4\": 58, \"T5\": 26, \"T6\": 36, \"T7\": 64, \"T8\": 6, \"T9\": 40}, \"result_json\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.50_libero_10_seed43.json\", \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_attn_k09_goal_seed42\": {\"metrics\": {\"elapsed_min\": 198.3, \"overall_sr\": 0.732, \"per_task_sr\": [0.62, 0.86, 0.8, 0.3, 0.96, 0.8, 0.7, 0.98, 0.82, 0.48], \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_attn_k09_spatial_seed42\": {\"metrics\": {\"elapsed_min\": 190.8, \"overall_sr\": 0.804, \"per_task_sr\": [0.88, 0.9, 0.9, 0.94, 0.74, 0.24, 0.96, 0.9, 0.78, 0.8], \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_attn_k09_object_seed42_v3\": {\"metrics\": {\"elapsed_minutes\": 260.6, \"k_ratio\": 0.9, \"overall_success_rate\": 0.614, \"per_task_sr\": {\"alphabet_soup\": 0.74, \"bbq_sauce\": 0.38, \"butter\": 0.28, \"chocolate_pudding\": 0.74, \"cream_cheese\": 0.46, \"ketchup\": 0.76, \"milk\": 0.52, \"orange_juice\": 0.76, \"salad_dressing\": 0.76, \"tomato_sauce\": 0.74}, \"total_episodes\": 500, \"total_successes\": 307, \"vision_tokens_kept\": 230, \"vision_tokens_original\": 256}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_long_seed43_postfix\": {\"metrics\": {\"elapsed_min\": 236.8, \"overall_sr\": 0.584, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 0.5, \"T1_cream_cheese_butter\": 0.88, \"T2_stove_moka\": 0.62, \"T3_black_bowl_drawer\": 0.8, \"T4_white_mug_plates\": 0.42, \"T5_book_caddy\": 0.9, \"T6_mug_plate_pudding\": 0.06, \"T7_alphabet_soup_cream_cheese\": 0.58, \"T8_moka_pots_stove\": 0.18, \"T9_mug_microwave\": 0.9}, \"total_episodes\": 500, \"total_successes\": 292}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_object_seed43_postfix\": {\"metrics\": {\"elapsed_min\": 113.8, \"per_task_sr\": {\"alphabet_soup\": 4, \"bbq_sauce\": 6, \"butter\": 4, \"chocolate_pudding\": 4, \"cream_cheese\": 16, \"ketchup\": 2, \"milk\": 4, \"orange_juice\": 12, \"salad_dressing\": 4, \"tomato_sauce\": 18}, \"success_rate\": 7.4, \"total_episodes\": 500, \"total_successes\": 37}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_goal_seed43_postfix\": {\"metrics\": {\"per_task_sr\": [74, 30, 38, 48, 92, 92, 82, 86, 64, 6], \"success_rate\": 61.2}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_spatial_seed43_postfix\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed43_postfix_v2\": {\"metrics\": {\"success_rate\": 39.2, \"total_episodes\": 500, \"total_success\": 196}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_object_seed43_postfix\": {\"metrics\": {\"success_rate\": 98.4, \"task_sr\": {\"T0\": 100, \"T1\": 100, \"T2\": 96, \"T3\": 100, \"T4\": 98, \"T5\": 96, \"T6\": 96, \"T7\": 98, \"T8\": 100, \"T9\": 100}}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_goal_seed43_postfix\": {\"metrics\": {\"success_rate\": 91}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_spatial_seed43_postfix\": {\"metrics\": {\"per_task\": [100, 100, 98, 100, 84, 92, 100, 98, 100, 90], \"success_rate\": 96.2}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_long_seed43_postfix\": {\"metrics\": {\"SR\": 0.526, \"per_task_SR\": {\"T0_alphabet_soup_tomato\": 0.66, \"T1_cream_cheese_butter\": 0.54, \"T2_stove_moka_pot\": 0.82, \"T3_black_bowl_drawer\": 0.38, \"T4_white_mug_left_plate\": 0.32, \"T5_book_back\": 0.62, \"T6_white_mug_plate\": 0.24, \"T7_alphabet_soup_cream\": 0.56, \"T8_moka_pots_stove\": 0.22, \"T9_yellow_white_mug_microwave\": 0.9}, \"total_episodes\": 500, \"total_successes\": 263}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_long_seed42_postfix\": {\"metrics\": {\"SR\": 0.502, \"total_episodes\": 500, \"total_successes\": 251}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed42_postfix_v2\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_long_seed42_postfix\": {\"metrics\": {\"overall_sr\": 62.6}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_long_seed42_postfix\": {\"metrics\": {\"overall_sr\": 29.6}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_long_seed43_postfix\": {\"status\": \"DONE\"}, \"eval_openvla_simplerenv_l2norm_k09\": {\"metrics\": {\"PutCarrotOnPlate_SR\": 0, \"PutEggplantInBasket_SR\": 0, \"PutSpoonOnTableCloth_SR\": 0, \"StackGreenCubeOnYellowCube_SR\": 0, \"avg_SR\": 0, \"episodes_per_task\": 50}, \"status\": \"DONE\"}, \"eval_openvla_simplerenv_baseline\": {\"metrics\": {\"PutCarrotOnPlate_SR\": 0, \"PutEggplantInBasket_SR\": 0, \"PutSpoonOnTableCloth_SR\": 0, \"StackGreenCubeOnYellowCube_SR\": 0, \"avg_SR\": 0, \"episodes_per_task\": 50}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_long_seed42_postfix_v2\": {\"metrics\": {\"overall_sr\": 80}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_long_seed43_postfix\": {\"metrics\": {\"n_episodes\": 50, \"overall_sr\": 87.4, \"per_task\": [98, 98, 94, 98, 96, 96, 52, 94, 54, 94], \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_smolvla_metaworld_l2norm_sweep\": {\"metrics\": {\"baseline_sr\": 26.4, \"k0.5_sr\": 0.8, \"k0.85_sr\": 2.4, \"k0.95_sr\": 7.2, \"k0.9_sr\": 10}, \"status\": \"DONE\"}, \"eval_smolvla_metaworld_random_sweep\": {\"metrics\": {\"baseline_sr\": 26.4, \"k0.5_sr\": 9.6, \"k0.85_sr\": 4.4, \"k0.95_sr\": 6.4, \"k0.9_sr\": 5.6}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_long_seed43_postfix_v2\": {\"metrics\": {\"overall_sr\": 80}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed43_postfix\": {\"status\": \"DONE\"}, \"eval_smolvla_metaworld_baseline\": {\"metrics\": {\"assembly_v3\": 20, \"drawer_open_v3\": 52, \"num_episodes_per_task\": 25, \"overall_sr\": 26.4, \"pick_place_v3\": 8, \"push_v3\": 24, \"reach_v3\": 28, \"wilson_ci_95\": [19.5, 34.7]}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_long_seed42_postfix\": {\"metrics\": {\"success_rate\": 32, \"task_sr\": {\"T0\": 10, \"T1\": 46, \"T2\": 38, \"T3\": 44, \"T4\": 16, \"T5\": 26, \"T6\": 10, \"T7\": 38, \"T8\": 10, \"T9\": 82}}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_spatial_seed42_postfix_v2\": {\"metrics\": {\"T1\": 60, \"T2\": 52, \"T3\": 8, \"T4\": 34, \"T5\": 22, \"T6\": 24, \"T7\": 62, \"T8\": 74, \"T9\": 40, \"overall_sr\": 43.4}, \"status\": \"DONE\"}, \"diag_openvla_unnorm_key\": {\"metrics\": {\"details\": {\"action_required\": \"Script needs --model_path and --unnorm_key args added to support non-object suites\", \"argparse_args\": [\"--mode\", \"--k_ratio\", \"--suite\", \"--num_episodes\", \"--seed\", \"--output\", \"--center_crop\", \"--num_steps_wait\"], \"line_31\": \"CHECKPOINT_PATH = /root/autodl-tmp/openvla-libero-object (hardcoded)\", \"line_32\": \"UNNORM_KEY = libero_object (hardcoded)\", \"missing_args\": [\"--model_path\", \"--unnorm_key\", \"--gpu\"], \"supported_suites\": {\"libero_10\": 520, \"libero_goal\": 300, \"libero_object\": 280, \"libero_spatial\": 280}, \"unnorm_key_usage\": [\"line 111: predict_action(unnorm_key=UNNORM_KEY)\", \"line 257: predict_action(unnorm_key=UNNORM_KEY)\"]}, \"finding\": \"UNNORM_KEY and CHECKPOINT_PATH are hardcoded, no CLI overrides\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_long_seed42_postfix\": {\"metrics\": {\"keep_ratio\": 0.95, \"n_episodes\": 50, \"overall_sr\": 87, \"prune_mode\": \"l2norm\", \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_long_seed42_postfix\": {\"metrics\": {\"keep_ratio\": 0.5, \"n_episodes\": 50, \"overall_sr\": 46.8, \"prune_mode\": \"random\", \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_long_seed42_postfix\": {\"metrics\": {\"keep_ratio\": 0.7, \"n_episodes\": 50, \"overall_sr\": 65.8, \"prune_mode\": \"random\", \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed42_postfix\": {\"metrics\": {\"keep_ratio\": 0.85, \"n_episodes\": 50, \"overall_sr\": 45.2, \"prune_mode\": \"random\", \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_long_seed42_postfix\": {\"metrics\": {\"keep_ratio\": 0.95, \"n_episodes\": 50, \"overall_sr\": 63.2, \"prune_mode\": \"random\", \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_spatial_seed42_postfix\": {\"metrics\": {\"keep_ratio\": 0.3, \"n_episodes\": 50, \"overall_sr\": 52.8, \"prune_mode\": \"l2norm\", \"suite\": \"libero_spatial\", \"task_0_sr\": 48, \"task_1_sr\": 80, \"task_2_sr\": 74, \"task_3_sr\": 22, \"task_4_sr\": 28, \"task_5_sr\": 22, \"task_6_sr\": 78, \"task_7_sr\": 84, \"task_8_sr\": 58, \"task_9_sr\": 34}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_long_seed42_postfix\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed42_postfix\": {\"metrics\": {\"overall_sr\": 78.4, \"per_task\": {\"task0_alphabet_soup_tomato_sauce_basket\": 96, \"task1_cream_cheese_butter_basket\": 92, \"task2_stove_moka_pot\": 86, \"task3_black_bowl_drawer_close\": 100, \"task4_white_mug_left_yellow_mug_right\": 76, \"task5_book_caddy_back\": 96, \"task6_white_mug_plate_chocolate_pudding\": 12, \"task7_alphabet_soup_cream_cheese_basket\": 84, \"task8_both_moka_pots_stove\": 50, \"task9_yellow_white_mug_microwave_close\": 92}, \"total_episodes\": 500, \"total_successes\": 392}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_goal_seed42_postfix\": {\"metrics\": {\"T0_open_middle_drawer\": 84, \"T1_put_bowl_on_stove\": 98, \"T2_put_wine_bottle_on_cabinet\": 90, \"T3_open_top_drawer_put_bowl\": 94, \"T4_put_bowl_on_cabinet\": 100, \"T5_push_plate_front_stove\": 100, \"T6_put_cream_cheese_in_bowl\": 92, \"T7_turn_on_stove\": 100, \"T8_put_bowl_on_plate\": 100, \"T9_put_wine_bottle_on_rack\": 50, \"overall_sr\": 90.8, \"total_episodes\": 500, \"total_successes\": 454}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_spatial_seed42_postfix\": {\"metrics\": {\"SR_overall\": 68.2, \"eval_time_min\": 143.9, \"server\": \"cqa1-33015\", \"tasks\": {\"T0\": 86, \"T1\": 92, \"T2\": 88, \"T3\": 44, \"T4\": 48, \"T5\": 56, \"T6\": 82, \"T7\": 52, \"T8\": 86, \"T9\": 48}, \"total_episodes\": 500, \"total_success\": 341}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_object_seed42_postfix\": {\"metrics\": {\"overall_sr\": 56.4, \"total_episodes\": 500, \"total_successes\": 282}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_spatial_seed42_postfix_v2\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_spatial_seed42_postfix\": {\"metrics\": {\"overall_sr\": 96, \"total_episodes\": 500, \"total_successes\": 480}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_goal_seed42_postfix\": {\"metrics\": {\"T0_open_middle_drawer\": 88, \"T1_put_bowl_on_stove\": 6, \"T2_put_wine_bottle_on_cabinet\": 72, \"T3_open_top_drawer_put_bowl\": 40, \"T4_put_bowl_on_cabinet\": 70, \"T5_push_plate_front_stove\": 30, \"T6_put_cream_cheese_in_bowl\": 32, \"T7_turn_on_stove\": 100, \"T8_put_bowl_on_plate\": 68, \"T9_put_wine_bottle_on_rack\": 22, \"overall_sr\": 52.8, \"total_episodes\": 500, \"total_success\": 264}, \"status\": \"DONE\"}, \"eval_openvla_attn_k05_object_seed42_v2\": {\"status\": \"DONE\"}, \"eval_pi05_random_k03_spatial_seed42_postfix\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_goal_seed42_postfix\": {\"metrics\": {\"T0_open_middle_drawer\": 43, \"T1_put_bowl_on_stove\": 49, \"T2_put_wine_bottle_on_cabinet\": 47, \"T3_open_top_drawer_put_bowl\": 44, \"T4_put_bowl_on_cabinet\": 50, \"T5_push_plate_front_stove\": 49, \"T6_put_cream_cheese_in_bowl\": 45, \"T7_turn_on_stove\": 50, \"T8_put_bowl_on_plate\": 47, \"T9_put_wine_bottle_on_rack\": 19, \"overall_sr\": 88.6, \"total_episodes\": 500, \"total_success\": 443}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_goal_seed42_postfix\": {\"metrics\": {\"T0_open_middle_drawer\": 37, \"T1_put_bowl_on_stove\": 41, \"T2_put_wine_bottle_on_cabinet\": 35, \"T3_open_top_drawer_put_bowl\": 24, \"T4_put_bowl_on_cabinet\": 46, \"T5_push_plate_front_stove\": 35, \"T6_put_cream_cheese_in_bowl\": 31, \"T7_turn_on_stove\": 50, \"T8_put_bowl_on_plate\": 30, \"T9_put_wine_bottle_on_rack\": 22, \"overall_sr\": 70.2, \"total_episodes\": 500, \"total_success\": 351}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_goal_seed42_postfix\": {\"metrics\": {\"T0_open_middle_drawer\": 32, \"T1_put_bowl_on_stove\": 1, \"T2_put_wine_bottle_on_cabinet\": 46, \"T3_open_top_drawer_put_bowl\": 33, \"T4_put_bowl_on_cabinet\": 37, \"T5_push_plate_front_stove\": 31, \"T6_put_cream_cheese_in_bowl\": 17, \"T7_turn_on_stove\": 50, \"T8_put_bowl_on_plate\": 28, \"T9_put_wine_bottle_on_rack\": 24, \"overall_sr\": 59.8, \"total_episodes\": 500, \"total_success\": 299}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_goal_seed42_postfix\": {\"metrics\": {\"T0_open_middle_drawer\": 86, \"T1_put_bowl_on_stove\": 94, \"T2_put_wine_bottle_on_cabinet\": 84, \"T3_open_top_drawer_put_bowl\": 78, \"T4_put_bowl_on_cabinet\": 98, \"T5_push_plate_front_stove\": 92, \"T6_put_cream_cheese_in_bowl\": 88, \"T7_turn_on_stove\": 100, \"T8_put_bowl_on_plate\": 96, \"T9_put_wine_bottle_on_rack\": 10, \"overall_sr\": 82.6, \"total_episodes\": 500, \"total_success\": 413}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_goal_seed42_postfix\": {\"metrics\": {\"overall_sr\": 73.6, \"per_task_sr\": {\"T0_open_middle_drawer_cabinet\": 78, \"T1_put_bowl_on_stove\": 44, \"T2_put_wine_bottle_on_cabinet\": 86, \"T3_open_top_drawer_put_bowl_in\": 76, \"T4_put_bowl_on_cabinet\": 92, \"T5_push_plate_front_stove\": 70, \"T6_put_cream_cheese_in_bowl\": 62, \"T7_turn_on_stove\": 100, \"T8_put_bowl_on_plate\": 86, \"T9_put_wine_bottle_on_rack\": 42}, \"runtime_min\": 100.8, \"total_episodes\": 500, \"total_success\": 368}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_goal_seed42_v5\": {\"metrics\": {\"domain_id\": 3, \"elapsed_min\": 84, \"overall_sr\": 0.37, \"per_task_sr\": {\"task0_open_drawer\": 0.42, \"task1_bowl_on_stove\": 0.92, \"task2_wine_on_cabinet\": 0.2, \"task3_drawer_bowl\": 0.24, \"task4_bowl_on_cabinet\": 0.98, \"task5_push_plate\": 0, \"task6_cream_cheese\": 0.02, \"task7_turn_stove\": 0.16, \"task8_bowl_on_plate\": 0.76, \"task9_wine_on_rack\": 0}, \"seed\": 42, \"total_episodes\": 500, \"total_success\": 185, \"vision_tokens_kept\": 15, \"vision_tokens_original\": 50, \"wilson_ci_95\": [0.3288, 0.4132]}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_long_seed43_v2\": {\"metrics\": {\"overall_sr\": 28, \"total_episodes\": 500, \"total_success\": 140}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed42_postfix\": {\"metrics\": {\"T0_open_drawer\": 68, \"T1_bowl_stove\": 4, \"T2_wine_cabinet\": 20, \"T3_drawer_bowl\": 30, \"T4_bowl_cabinet\": 66, \"T5_push_plate\": 80, \"T6_cream_bowl\": 86, \"T7_turn_stove\": 90, \"T8_bowl_plate\": 78, \"T9_wine_rack\": 6, \"overall_sr\": 52.8, \"total_episodes\": 500, \"total_successes\": 264}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_goal_seed42_postfix\": {\"metrics\": {\"T0_open_drawer\": 76, \"T1_bowl_stove\": 32, \"T2_wine_cabinet\": 38, \"T3_drawer_bowl\": 38, \"T4_bowl_cabinet\": 90, \"T5_push_plate\": 88, \"T6_cream_bowl\": 80, \"T7_turn_stove\": 88, \"T8_bowl_plate\": 74, \"T9_wine_rack\": 14, \"overall_sr\": 61.8, \"total_episodes\": 500, \"total_successes\": 309}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_goal_seed42_postfix\": {\"metrics\": {\"T0_open_drawer\": 90, \"T1_bowl_stove\": 48, \"T2_wine_cabinet\": 82, \"T3_drawer_bowl\": 74, \"T4_bowl_cabinet\": 96, \"T5_push_plate\": 72, \"T6_cream_bowl\": 62, \"T7_turn_stove\": 100, \"T8_bowl_plate\": 82, \"T9_wine_rack\": 50, \"overall_sr\": 75.6, \"total_episodes\": 500, \"total_successes\": 378}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed42_postfix_v2\": {\"metrics\": {\"T0_plate_ramekin\": 100, \"T1_next_ramekin\": 86, \"T2_table_center\": 88, \"T3_cookie_box\": 64, \"T4_top_drawer\": 50, \"T5_on_ramekin\": 80, \"T6_next_cookie\": 92, \"T7_on_stove\": 76, \"T8_next_plate\": 94, \"T9_wooden_cabinet\": 38, \"overall_sr\": 76.8, \"total_episodes\": 500, \"total_successes\": 384}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_goal_seed42_v3\": {\"metrics\": {\"T0_open_drawer\": 68, \"T1_bowl_stove\": 52, \"T2_wine_cabinet\": 58, \"T3_drawer_bowl\": 64, \"T4_bowl_cabinet\": 94, \"T5_push_plate\": 88, \"T6_cream_bowl\": 88, \"T7_turn_stove\": 96, \"T8_bowl_plate\": 86, \"T9_wine_rack\": 6, \"overall_sr\": 70, \"total_episodes\": 500, \"total_successes\": 350}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_object_seed42_postfix\": {\"metrics\": {\"T0_alphabet_soup\": 30, \"T1_cream_cheese\": 36, \"T2_salad_dressing\": 22, \"T3_bbq_sauce\": 28, \"T4_ketchup\": 8, \"T5_tomato_sauce\": 44, \"T6_butter\": 48, \"T7_milk\": 20, \"T8_chocolate_pudding\": 16, \"T9_orange_juice\": 20, \"overall_sr\": 27.2, \"total_episodes\": 500, \"total_successes\": 136}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_spatial_seed42_postfix\": {\"metrics\": {\"overall_sr\": 73.8, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_long_seed42\": {\"status\": \"DONE\"}, \"eval_xvla_random_k03_long_seed42\": {\"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_long_seed42_v4\": {\"metrics\": {\"elapsed_min\": 94.6, \"overall_sr\": 44.6, \"per_task_sr\": {\"T0_alphabet_soup_tomato_basket\": 26, \"T1_cream_cheese_butter_basket\": 0, \"T2_stove_moka_pot\": 48, \"T3_black_bowl_drawer\": 84, \"T4_mugs_on_plates\": 36, \"T5_book_caddy\": 88, \"T6_mug_plate_pudding\": 48, \"T7_alphabet_soup_cream_cheese_basket\": 78, \"T8_moka_pots_stove\": 34, \"T9_mug_microwave\": 4}, \"total_episodes\": 500, \"total_success\": 223}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_spatial_seed42_v3\": {\"metrics\": {\"elapsed_min\": 63.1, \"overall_sr\": 88.4, \"per_task_sr\": {\"T0_between_plate_ramekin\": 98, \"T1_next_to_ramekin\": 92, \"T2_table_center\": 94, \"T3_on_cookie_box\": 84, \"T4_top_drawer\": 76, \"T5_on_ramekin\": 82, \"T6_next_to_cookie_box\": 98, \"T7_on_stove\": 86, \"T8_next_to_plate\": 98, \"T9_wooden_cabinet\": 76}, \"total_episodes\": 500, \"total_success\": 442}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed42_v3\": {\"metrics\": {\"elapsed_min\": 86.9, \"overall_sr\": 60.2, \"per_task_sr\": {\"T0_between_plate_ramekin\": 78, \"T1_next_to_ramekin\": 62, \"T2_table_center\": 92, \"T3_on_cookie_box\": 14, \"T4_top_drawer\": 60, \"T5_on_ramekin\": 36, \"T6_next_to_cookie_box\": 44, \"T7_on_stove\": 82, \"T8_next_to_plate\": 86, \"T9_wooden_cabinet\": 48}, \"total_episodes\": 500, \"total_success\": 301}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_goal_seed42_v3\": {\"metrics\": {\"elapsed_min\": 56.3, \"overall_sr\": 89.8, \"per_task_sr\": {\"bowl_on_cabinet\": 98, \"bowl_on_plate\": 96, \"bowl_on_stove\": 96, \"cream_cheese_in_bowl\": 88, \"open_drawer_put_bowl\": 90, \"open_middle_drawer\": 86, \"push_plate_front_stove\": 98, \"turn_on_stove\": 100, \"wine_bottle_on_cabinet\": 100, \"wine_bottle_on_rack\": 46}, \"total_episodes\": 500, \"total_success\": 449}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_spatial_seed42\": {\"metrics\": {\"overall_sr\": 90.4}, \"status\": \"DEPLOYED\"}, \"eval_xvla_l2norm_k03_goal_seed42\": {\"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_spatial_seed42_v2\": {\"metrics\": {\"overall_sr\": 72.8, \"per_task_sr\": {\"task_0\": 98, \"task_1\": 42, \"task_2\": 96, \"task_3\": 94, \"task_4\": 82, \"task_5\": 0, \"task_6\": 98, \"task_7\": 34, \"task_8\": 94, \"task_9\": 90}, \"total_episodes\": 500, \"total_success\": 364}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_spatial_seed42_postfix_v3\": {\"metrics\": {\"overall_sr\": 0.718, \"per_task_sr\": {\"T0\": 0.88, \"T1\": 0.88, \"T2\": 0.88, \"T3\": 0.48, \"T4\": 0.4, \"T5\": 0.32, \"T6\": 0.92, \"T7\": 0.86, \"T8\": 0.84, \"T9\": 0.72}, \"total_episodes\": 500, \"total_success\": 359, \"wall_time_min\": 139.2}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_spatial_seed43_v2\": {\"metrics\": {\"overall_sr\": 0.554, \"per_task_sr\": {\"T0_between_plate\": 0.76, \"T1_next_to_ramekin\": 0.84, \"T2_table_center\": 0.84, \"T3_on_cookie_box\": 0.14, \"T4_top_drawer\": 0.42, \"T5_on_ramekin\": 0.48, \"T6_next_to_cookie\": 0.28, \"T7_on_stove\": 0.74, \"T8_next_to_plate\": 0.68, \"T9_wooden_cabinet\": 0.36}, \"total_episodes\": 500, \"total_success\": 277, \"wall_time_min\": 90.3}, \"status\": \"DONE\"}, \"eval_xvla_random_k085_long_seed42\": {\"metrics\": {\"cross_suite_k085\": {\"goal\": 60.4, \"long\": 35, \"object\": 65, \"spatial\": 68.2}, \"elapsed_min\": 106.7, \"keep_ratio\": 0.85, \"model\": \"X-VLA\", \"overall_sr\": 35, \"per_task_sr\": {\"T0_alphabet_soup_tomato_sauce_basket\": 54, \"T1_cream_cheese_butter_basket\": 10, \"T2_stove_moka_pot\": 16, \"T3_black_bowl_drawer\": 88, \"T4_white_mug_left_yellow_mug_right\": 2, \"T5_book_caddy\": 98, \"T6_white_mug_chocolate_pudding\": 0, \"T7_alphabet_soup_cream_cheese_basket\": 48, \"T8_both_moka_pots_stove\": 16, \"T9_mug_microwave\": 18}, \"prune_mode\": \"random\", \"seed\": 42, \"suite\": \"libero_10\", \"total_episodes\": 500, \"total_success\": 175, \"vs_k05_long\": {\"delta_pp\": -26.6, \"k05_sr\": 61.6, \"k085_sr\": 35, \"non_monotonic\": true}, \"wilson_ci_95\": [30.9, 39.3]}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_spatial_seed42_postfix_v2\": {\"metrics\": {\"baseline_spatial_k1\": 78, \"delta_vs_baseline\": -24.6, \"overall_sr\": 53.4, \"per_task_sr\": {\"T0_between_plate\": 90, \"T1_next_to_ramekin\": 52, \"T2_table_center\": 80, \"T3_on_cookie_box\": 24, \"T4_top_drawer\": 18, \"T5_on_ramekin\": 40, \"T6_next_to_cookie\": 58, \"T7_on_stove\": 54, \"T8_next_to_plate\": 90, \"T9_wooden_cabinet\": 28}, \"total_episodes\": 500, \"total_success\": 267, \"wall_time_min\": 171.9}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed42_postfix_v2\": {\"metrics\": {\"baseline_spatial_k1\": 78, \"delta_vs_baseline\": -17.2, \"overall_sr\": 60.8, \"per_task_sr\": {\"T0\": 84, \"T1\": 68, \"T2\": 92, \"T3\": 16, \"T4\": 66, \"T5\": 28, \"T6\": 44, \"T7\": 76, \"T8\": 82, \"T9\": 52}, \"total_episodes\": 500, \"total_success\": 304}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_goal_seed43_v2\": {\"metrics\": {\"T0_open_drawer\": 80, \"T1_bowl_stove\": 12, \"T2_wine_cabinet\": 76, \"T3_drawer_bowl\": 52, \"T4_bowl_cabinet\": 60, \"T5_push_plate\": 32, \"T6_cream_bowl\": 26, \"T7_turn_stove\": 100, \"T8_bowl_plate\": 70, \"T9_wine_rack\": 28, \"cv_mean\": 52.1, \"cv_seed42\": 50.6, \"cv_seed43\": 53.6, \"cv_std\": 2.1, \"elapsed_min\": 127.4, \"overall_sr\": 53.6, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_goal_seed42_v2\": {\"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_goal_seed42_v3\": {\"metrics\": {\"success_rate\": 0.376, \"task_sr\": {\"task0_open_drawer\": 0.42, \"task1_bowl_on_stove\": 0.94, \"task2_wine_on_cabinet\": 0.16, \"task3_drawer_bowl_inside\": 0.24, \"task4_bowl_on_cabinet\": 0.98, \"task5_push_plate\": 0, \"task6_cream_in_bowl\": 0.02, \"task7_turn_on_stove\": 0.2, \"task8_bowl_on_plate\": 0.8, \"task9_wine_on_rack\": 0}, \"total_episodes\": 500, \"total_successes\": 188}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_long_seed42_v3\": {\"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_spatial_seed42_v2\": {\"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_spatial_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 360, \"seed\": 42, \"success_rate\": 0.72, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_goal_seed42_v2\": {\"metrics\": {\"keep_ratio\": 0.5, \"model\": \"X-VLA\", \"per_task_sr\": {\"T0_open_middle_drawer\": 80, \"T1_put_bowl_on_stove\": 92, \"T2_put_wine_bottle_on_cabinet\": 98, \"T3_open_top_drawer_put_bowl\": 34, \"T4_put_bowl_on_cabinet\": 100, \"T5_push_plate_to_stove\": 0, \"T6_put_cream_cheese_in_bowl\": 24, \"T7_turn_on_stove\": 72, \"T8_put_bowl_on_plate\": 90, \"T9_put_wine_bottle_on_rack\": 0}, \"prune_mode\": \"l2_norm\", \"seed\": 42, \"success_rate\": 0.59, \"suite\": \"libero_goal\", \"total_episodes\": 500, \"total_successes\": 295}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_spatial_seed43\": {\"metrics\": {\"overall_SR\": 0.582, \"total_episodes\": 500, \"total_successes\": 291}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed43\": {\"metrics\": {\"keep_ratio\": 0.85, \"model\": \"pi0.5\", \"note\": \"completed via direct tmux May24 10:24\", \"per_task_sr\": {\"T0_open_middle_drawer\": 80, \"T1_put_bowl_on_stove\": 4, \"T2_put_wine_bottle_on_cabinet\": 20, \"T3_open_top_drawer_put_bowl\": 46, \"T4_put_bowl_on_cabinet\": 58, \"T5_push_plate_to_stove\": 82, \"T6_put_cream_cheese_in_bowl\": 74, \"T7_turn_on_stove\": 90, \"T8_put_bowl_on_plate\": 58, \"T9_put_wine_bottle_on_rack\": 10}, \"prune_mode\": \"random\", \"seed\": 43, \"success_rate\": 0.522, \"suite\": \"libero_goal\", \"total_episodes\": 500, \"total_successes\": 261}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_goal_seed43\": {\"metrics\": {\"keep_ratio\": 0.95, \"model\": \"pi0.5\", \"note\": \"re-run with HF_HUB_OFFLINE=1, result file May24 10:54\", \"per_task_sr\": {\"T0_open_middle_drawer\": 86, \"T1_put_bowl_on_stove\": 94, \"T2_put_wine_bottle_on_cabinet\": 74, \"T3_open_top_drawer_put_bowl\": 80, \"T4_put_bowl_on_cabinet\": 100, \"T5_push_plate_to_stove\": 96, \"T6_put_cream_cheese_in_bowl\": 90, \"T7_turn_on_stove\": 100, \"T8_put_bowl_on_plate\": 96, \"T9_put_wine_bottle_on_rack\": 18}, \"prune_mode\": \"random\", \"seed\": 43, \"success_rate\": 0.834, \"suite\": \"libero_goal\", \"total_episodes\": 500, \"total_successes\": 417}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_goal_seed43\": {\"metrics\": {\"overall_SR\": 0.602, \"per_task_SR\": [0.84, 1, 0.98, 0.3, 1, 0, 0.22, 0.74, 0.9, 0.04], \"seed\": 43, \"total_episodes\": 500, \"total_successes\": 301, \"wilson_ci_95\": [0.5585, 0.644]}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_goal_seed42_v2\": {\"metrics\": {\"duration_min\": 109.7, \"overall_SR\": 73.6, \"per_task_SR\": {\"T0_open_drawer\": 78, \"T1_bowl_stove\": 44, \"T2_wine_cabinet\": 86, \"T3_bowl_drawer\": 76, \"T4_bowl_cabinet\": 92, \"T5_plate_stove\": 70, \"T6_cream_bowl\": 62, \"T7_turn_stove\": 100, \"T8_bowl_plate\": 86, \"T9_wine_rack\": 42}, \"total_episodes\": 500, \"total_successes\": 368}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_goal_seed43_v2\": {\"metrics\": {\"duration_min\": 71.3, \"overall_SR\": 72.2, \"per_task_SR\": {\"T0_open_middle_drawer\": 78, \"T1_put_bowl_on_stove\": 76, \"T2_wine_bottle_on_cabinet\": 68, \"T3_open_drawer_put_bowl\": 48, \"T4_bowl_on_cabinet\": 90, \"T5_push_plate_front_stove\": 80, \"T6_cream_cheese_in_bowl\": 66, \"T7_turn_on_stove\": 98, \"T8_bowl_on_plate\": 68, \"T9_wine_bottle_on_rack\": 50}, \"total_episodes\": 500, \"total_successes\": 361}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_goal_seed42_v2\": {\"status\": \"DEPLOYED\"}, \"eval_pi05_l2norm_k085_goal_seed43\": {\"metrics\": {\"elapsed_min\": 86.5, \"overall_SR\": 87, \"per_task\": {\"open the middle drawer of the cabinet\": 88, \"open the top drawer and put the bowl inside\": 80, \"push the plate to the front of the stove\": 94, \"put the bowl on the plate\": 94, \"put the bowl on the stove\": 94, \"put the bowl on top of the cabinet\": 96, \"put the cream cheese in the bowl\": 86, \"put the wine bottle on the rack\": 46, \"put the wine bottle on top of the cabinet\": 96, \"turn on the stove\": 96}, \"total_episodes\": 500, \"total_successes\": 435}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed42_postfix\": {\"status\": \"DONE\"}, \"eval_xvla_random_k085_object_seed42\": {\"metrics\": {\"elapsed_seconds\": 3572.9, \"overall_SR\": 0.65, \"per_task_sr\": [0.98, 0.14, 1, 0.88, 0.36, 0.96, 0, 0.94, 0.24, 1], \"total_episodes\": 500, \"total_successes\": 325, \"wilson_ci_95\": [0.6072, 0.6905]}, \"status\": \"DONE\"}, \"eval_xvla_random_k085_spatial_seed42\": {\"metrics\": {\"overall_SR\": 0.682, \"per_task\": {\"0\": 1, \"1\": 0.06, \"2\": 0.98, \"3\": 0.98, \"4\": 0.82, \"5\": 0.06, \"6\": 1, \"7\": 0.04, \"8\": 0.92, \"9\": 0.96}, \"total_episodes\": 500, \"wilson_ci_95\": [0.6399, 0.7213]}, \"status\": \"DONE\"}, \"eval_xvla_random_k085_goal_seed42\": {\"metrics\": {\"overall_SR\": 0.604, \"per_task\": {\"0\": 1, \"1\": 0.42, \"2\": 0.7, \"3\": 0.78, \"4\": 0.98, \"5\": 0, \"6\": 0.02, \"7\": 0.88, \"8\": 0.98, \"9\": 0.28}, \"total_episodes\": 500, \"wilson_ci_95\": [0.5605, 0.6459]}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_object_seed42_v2\": {\"metrics\": {\"duration_min\": 119.6, \"num_episodes\": 500, \"per_task\": [0.82, 0.86, 0.66, 0.68, 0.64, 0.74, 0.76, 0.56, 0.86, 0.82], \"success_rate\": 74}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_object_seed42_v4\": {\"metrics\": {\"duration_min\": 120.7, \"num_episodes\": 500, \"per_task\": [0.86, 0.86, 0.7, 0.76, 0.72, 0.3, 0.88, 0.76, 0.88, 0.68], \"success_rate\": 74}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_goal_seed42_v2\": {\"status\": \"DONE\"}, \"eval_pi05_random_k09_object_seed42_v2\": {\"metrics\": {\"overall_SR\": 0.09, \"per_task_sr\": {\"T0\": 14, \"T1\": 20, \"T2\": 4, \"T3\": 6, \"T4\": 2, \"T5\": 20, \"T6\": 6, \"T7\": 2, \"T8\": 6, \"T9\": 10}, \"postfix_confirmed\": true, \"postfix_sr\": 9, \"prefix_v2_sr\": 9, \"result_json\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.90_libero_object_seed42.json\", \"seed\": 42, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_object_seed42_v2\": {\"metrics\": {\"overall_SR\": 0.682, \"seed\": 42, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_object_seed42_v3\": {\"metrics\": {\"overall_SR\": 0.74, \"seed\": 42, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_long_seed43\": {\"metrics\": {\"elapsed_min\": 94, \"overall_SR\": 43.8, \"per_task_sr\": {\"T0\": 26, \"T1\": 0, \"T2\": 52, \"T3\": 78, \"T4\": 38, \"T5\": 86, \"T6\": 56, \"T7\": 76, \"T8\": 24, \"T9\": 2}, \"result_json\": \"eval_results/xvla_prune_k0.5_libero_10.json\", \"total_episodes\": 500, \"total_successes\": 219, \"wilson_ci_95\": [39.5, 48.2]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_long_seed43\": {\"metrics\": {\"sr\": 0.54, \"total_episodes\": 500, \"total_successes\": 270}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_goal_seed43\": {\"status\": \"DONE\"}, \"eval_pi05_random_k05_spatial_seed42_postfix_v2\": {\"status\": \"DONE\"}, \"eval_pi05_random_k09_spatial_seed42_postfix\": {\"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_long_seed42\": {\"metrics\": {\"elapsed_min\": 94.6, \"episodes\": 500, \"overall_sr\": 45, \"per_task_sr\": {\"task_0_alphabet_soup_tomato_sauce\": 26, \"task_1_cream_cheese_butter\": 0, \"task_2_stove_moka_pot\": 46, \"task_3_black_bowl_drawer\": 82, \"task_4_white_mug_yellow_mug\": 42, \"task_5_book_caddy\": 92, \"task_6_white_mug_chocolate_pudding\": 54, \"task_7_alphabet_soup_cream_cheese\": 70, \"task_8_both_moka_pots\": 34, \"task_9_mug_microwave\": 4}, \"wilson_ci_95\": [40.7, 49.4]}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_object_seed42\": {\"metrics\": {\"duration_min\": 76.0, \"num_episodes\": 500, \"per_task\": [0.96, 0.46, 0.98, 0.8, 1.0, 0.76, 0.02, 0.82, 0.26, 1.0], \"success_rate\": 70.6, \"wilson_ci_95\": [0.665, 0.744]}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_object_seed43\": {\"metrics\": {\"elapsed_min\": 119.5, \"overall_sr\": 0.096, \"per_task_sr\": {\"T0_alphabet_soup\": 0.16, \"T1_cream_cheese\": 0.16, \"T2_salad_dressing\": 0.1, \"T3_bbq_sauce\": 0.02, \"T4_ketchup\": 0.06, \"T5_tomato_sauce\": 0.14, \"T6_butter\": 0.14, \"T7_milk\": 0.02, \"T8_chocolate_pudding\": 0.08, \"T9_orange_juice\": 0.08}, \"total_episodes\": 500, \"total_successes\": 48}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_spatial_seed42\": {\"metrics\": {\"duration_min\": 92.1, \"num_episodes\": 500, \"per_task\": [0.98, 0.26, 0.98, 0.9, 0.86, 0, 0.92, 0.66, 0.92, 0.66], \"success_rate\": 71.4, \"suite\": \"libero_spatial\", \"wilson_ci_95\": [0.673, 0.752]}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_long_seed42\": {\"metrics\": {\"keep_ratio\": 0.5, \"per_task_sr\": [68, 0, 64, 94, 70, 90, 84, 86, 46, 14], \"prune_method\": \"random\", \"seed\": 42, \"success_rate\": 61.6, \"suite\": \"libero_10\", \"tokens_kept\": \"25/50\", \"total_episodes\": 500, \"total_successes\": 308, \"wall_time_min\": 82.6, \"wilson_ci_95\": [57.3, 65.8]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_object_seed42\": {\"metrics\": {\"success_rate\": 0.434, \"total_episodes\": 500, \"total_successes\": 217}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_spatial_seed43\": {\"metrics\": {\"elapsed_min\": 79.1, \"per_task_SR\": {\"T0_bowl_between_plate_ramekin\": 98, \"T1_bowl_next_ramekin\": 20, \"T2_bowl_from_table_center\": 92, \"T3_bowl_on_cookie_box\": 72, \"T4_bowl_in_top_drawer\": 76, \"T5_bowl_on_ramekin\": 0, \"T6_bowl_next_cookie_box\": 76, \"T7_bowl_on_stove\": 38, \"T8_bowl_next_plate\": 66, \"T9_bowl_on_wooden_cabinet\": 52}, \"seed\": 43, \"success_rate\": 59, \"total_episodes\": 500, \"total_successes\": 295, \"vs_l2norm_spatial_seed42\": {\"diff_pp\": 0.2, \"mean\": 58.9, \"seed42_sr\": 58.8, \"seed43_sr\": 59}, \"vs_random_k05_spatial_seed43\": {\"delta_pp\": -13.6, \"l2norm_sr\": 59, \"random_sr\": 72.6, \"verdict\": \"L2norm worse than random on Spatial\"}, \"wilson_ci_95\": [54.6, 63.2]}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_goal_seed43_v4\": {\"metrics\": {\"cv_with_seed42\": {\"diff_pp\": 1.4, \"mean\": 67.9, \"seed42\": 67.2, \"seed43\": 68.6}, \"elapsed_min\": 56.1, \"per_task_sr\": {\"T0_open_middle_drawer\": 100, \"T1_bowl_on_stove\": 94, \"T2_wine_on_cabinet\": 96, \"T3_open_drawer_bowl_inside\": 68, \"T4_bowl_on_cabinet\": 98, \"T5_push_plate\": 0, \"T6_cream_cheese_in_bowl\": 38, \"T7_turn_on_stove\": 96, \"T8_bowl_on_plate\": 96, \"T9_wine_on_rack\": 0}, \"success_rate\": 68.6, \"total_episodes\": 500, \"total_successes\": 343, \"wilson_ci_95\": [64.4, 72.5]}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_spatial_seed42_postfix\": {\"status\": \"DONE\"}, \"eval_openvla_baseline_long_seed42\": {\"metrics\": {\"overall_sr\": 0.528, \"task_sr\": {\"task01_alphabet_soup_tomato_sauce_basket\": 0.62, \"task02_cream_cheese_butter_basket\": 0.7, \"task03_stove_moka_pot\": 0.5, \"task04_black_bowl_drawer\": 0.48, \"task05_white_mug_left_yellow_mug_right\": 0.4, \"task06_book_caddy\": 0.7, \"task07_white_mug_plate_chocolate_pudding\": 0.5, \"task08_alphabet_soup_cream_cheese_basket\": 0.6, \"task09_both_moka_pots_stove\": 0.24, \"task10_yellow_white_mug_microwave\": 0.54}, \"time_min\": 483.3, \"total_episodes\": 500, \"total_success\": 264}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_goal_seed42\": {\"metrics\": {\"overall_SR\": 0.51, \"per_task\": {\"T0_open_drawer\": 0.82, \"T1_bowl_stove\": 0.22, \"T2_wine_cabinet\": 0.76, \"T3_drawer_bowl\": 0.34, \"T4_bowl_cabinet\": 0.64, \"T5_plate_stove\": 0.26, \"T6_cream_cheese_bowl\": 0.26, \"T7_turn_stove\": 1, \"T8_bowl_plate\": 0.54, \"T9_wine_rack\": 0.26}, \"total_episodes\": 500, \"total_successes\": 255}, \"status\": \"DONE\"}, \"eval_pi05_attention_k05_object_seed42\": {\"metrics\": {\"overall_SR\": 0.378, \"per_task\": {\"T0_alphabet_soup\": 0.94, \"T1_cream_cheese\": 0.26, \"T2_salad_dressing\": 0.32, \"T3_bbq_sauce\": 0.18, \"T4_ketchup\": 0.4, \"T5_tomato_sauce\": 0.12, \"T6_butter\": 0.38, \"T7_milk\": 0.6, \"T8_chocolate_pudding\": 0.36, \"T9_orange_juice\": 0.22}, \"total_episodes\": 500, \"total_successes\": 189}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_goal_seed42_v3\": {\"metrics\": {\"eval_time_min\": 247.8, \"overall_sr\": 0.434, \"task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 0.28, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.06, \"push_the_plate_to_the_front_of_the_stove\": 0.2, \"put_the_bowl_on_the_plate\": 0.3, \"put_the_bowl_on_the_stove\": 0.38, \"put_the_bowl_on_top_of_the_cabinet\": 0.66, \"put_the_cream_cheese_in_the_bowl\": 0.22, \"put_the_wine_bottle_on_the_rack\": 0.44, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.82, \"turn_on_the_stove\": 0.98}, \"total_episodes\": 500, \"total_successes\": 217}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_long_seed43\": {\"metrics\": {\"elapsed_min\": 83.6, \"overall_SR\": 0.582, \"per_task_SR\": [0.62, 0, 0.68, 0.94, 0.6, 0.86, 0.82, 0.84, 0.4, 0.06], \"seed\": 43, \"total_episodes\": 500, \"total_successes\": 291, \"wilson_ci_95\": [0.5383, 0.6244]}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed42_postfix\": {\"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_object_seed43\": {\"metrics\": {\"elapsed_min\": 76.3, \"overall_SR\": 0.43, \"per_task_SR\": {\"T0_alphabet_soup\": 0.52, \"T1_cream_cheese\": 0.06, \"T2_salad_dressing\": 0.76, \"T3_bbq_sauce\": 0.7, \"T4_ketchup\": 0.52, \"T5_tomato_sauce\": 0.56, \"T6_butter\": 0.02, \"T7_milk\": 0.38, \"T8_chocolate_pudding\": 0.16, \"T9_orange_juice\": 0.62}, \"seed\": 43, \"total_episodes\": 500, \"total_successes\": 215, \"vs_random_k05_object_seed43\": {\"delta_pp\": -28, \"l2norm_sr\": 0.43, \"random_sr\": 0.71, \"verdict\": \"L2norm catastrophically worse than random on Object suite\"}, \"wilson_ci_95\": [0.387, 0.474]}, \"status\": \"DONE\"}, \"eval_pi05_attention_k05_spatial_seed42\": {\"metrics\": {\"elapsed_min\": 74.3, \"overall_sr\": 0.726, \"per_task\": {\"T0_bowl_between_plate_ramekin\": 0.72, \"T1_bowl_next_to_ramekin\": 0.92, \"T2_bowl_from_table_center\": 0.96, \"T3_bowl_on_cookie_box\": 0.68, \"T4_bowl_in_top_drawer\": 0.28, \"T5_bowl_on_ramekin\": 0.32, \"T6_bowl_next_to_cookie_box\": 0.86, \"T7_bowl_on_stove\": 0.88, \"T8_bowl_next_to_plate\": 0.76, \"T9_bowl_on_wooden_cabinet\": 0.88}, \"total_episodes\": 500, \"total_successes\": 363, \"vs_random_k05_spatial\": {\"attention_sr\": 0.726, \"delta_pp\": 1, \"random_sr\": 0.716, \"verdict\": \"noise-level, attention provides no benefit over random\"}}, \"status\": \"DONE\"}, \"eval_pi05_attention_k05_goal_seed43\": {\"metrics\": {\"elapsed_min\": 70.6, \"overall_sr\": 0.722, \"per_task\": {\"bowl_in_drawer\": 0.72, \"bowl_on_cabinet\": 1, \"bowl_on_plate\": 0.9, \"bowl_on_stove\": 0.32, \"cream_cheese_in_bowl\": 0.62, \"open_middle_drawer\": 0.76, \"plate_to_front\": 0.64, \"turn_on_stove\": 1, \"wine_on_cabinet\": 0.84, \"wine_on_rack\": 0.42}, \"total_episodes\": 500, \"total_successes\": 361}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_object_seed42_v2\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_goal_seed42\": {\"metrics\": {\"elapsed_min\": 90.4, \"overall_sr\": 0.908, \"per_task\": {\"open the middle drawer of the cabinet\": 0.84, \"open the top drawer and put the bowl inside\": 0.96, \"push the plate to the front of the stove\": 1, \"put the bowl on the plate\": 0.98, \"put the bowl on the stove\": 0.98, \"put the bowl on top of the cabinet\": 1, \"put the cream cheese in the bowl\": 0.92, \"put the wine bottle on the rack\": 0.46, \"put the wine bottle on top of the cabinet\": 0.94, \"turn on the stove\": 1}, \"total_episodes\": 500, \"total_successes\": 454}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_goal_seed42\": {\"metrics\": {\"elapsed_min\": 118.7, \"keep_ratio\": 0.3, \"note\": \"Two runs: v2=50.6%, latest=54.2%. vs Random k=0.3 Goal=51.8%, delta=+2.4pp (negligible)\", \"overall_SR\": 0.542, \"per_task\": {\"open the middle drawer of the cabinet\": 0.7, \"open the top drawer and put the bowl inside\": 0.4, \"push the plate to the front of the stove\": 0.48, \"put the bowl on the plate\": 0.72, \"put the bowl on the stove\": 0.2, \"put the bowl on top of the cabinet\": 0.6, \"put the cream cheese in the bowl\": 0.26, \"put the wine bottle on the rack\": 0.28, \"put the wine bottle on top of the cabinet\": 0.82, \"turn on the stove\": 0.96}, \"prune_mode\": \"l2norm\", \"seed\": 42, \"suite\": \"libero_goal\", \"total_episodes\": 500, \"total_successes\": 271, \"v2_run_SR\": 0.506}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_goal_seed43_v3\": {\"status\": \"DONE\"}, \"eval_xvla_random_k05_goal_seed43_v2\": {\"status\": \"DONE\"}, \"eval_pi05_random_k05_spatial_seed42\": {\"metrics\": {\"per_task\": {\"T0_bowl_between_plate_ramekin\": 88, \"T1_bowl_next_to_ramekin\": 82, \"T2_bowl_from_table_center\": 88, \"T3_bowl_on_cookie_box\": 52, \"T4_bowl_in_top_drawer\": 44, \"T5_bowl_on_ramekin\": 38, \"T6_bowl_next_to_cookie_box\": 84, \"T7_bowl_on_stove\": 84, \"T8_bowl_next_to_plate\": 80, \"T9_bowl_on_wooden_cabinet\": 76}, \"success_rate\": 71.6, \"total_episodes\": 500, \"total_successes\": 358}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_goal_seed43\": {\"metrics\": {\"elapsed_min\": 58.2, \"note\": \"log=eval_xvla_random_k05_goal_seed42_v2.log; JSON overwritten by l2_norm run (known bug)\", \"overall_sr\": 0.672, \"per_task\": {\"task_0_open_middle_drawer\": {\"sr\": 0.98, \"succ\": 49, \"total\": 50}, \"task_1_bowl_on_stove\": {\"sr\": 0.98, \"succ\": 49, \"total\": 50}, \"task_2_wine_on_cabinet\": {\"sr\": 0.9, \"succ\": 45, \"total\": 50}, \"task_3_open_drawer_bowl_inside\": {\"sr\": 0.6, \"succ\": 30, \"total\": 50}, \"task_4_bowl_on_cabinet\": {\"sr\": 0.98, \"succ\": 49, \"total\": 50}, \"task_5_push_plate\": {\"sr\": 0, \"succ\": 0, \"total\": 50}, \"task_6_cream_cheese_in_bowl\": {\"sr\": 0.4, \"succ\": 20, \"total\": 50}, \"task_7_turn_on_stove\": {\"sr\": 0.98, \"succ\": 49, \"total\": 50}, \"task_8_bowl_on_plate\": {\"sr\": 0.86, \"succ\": 43, \"total\": 50}, \"task_9_wine_on_rack\": {\"sr\": 0.04, \"succ\": 2, \"total\": 50}}, \"total_episodes\": 500, \"total_successes\": 336, \"wilson_ci_95\": [0.63, 0.712]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_long_seed42_v3\": {\"metrics\": {\"elapsed_min\": 154.8, \"success_rate\": 51.4, \"total_episodes\": 500, \"total_successes\": 257}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_spatial_seed42_unreg\": {\"metrics\": {\"success_rate\": 58.2, \"total_episodes\": 500, \"total_successes\": 291}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_long_seed42_v2\": {\"metrics\": {\"cpu_rng_fixed\": true, \"elapsed_min\": 160, \"importance_margin_vs_l2norm\": {\"l2norm_k05_long_sr\": 50.2, \"margin_pp\": 3.4, \"random_k05_long_sr\": 46.8}, \"keep_ratio\": 0.5, \"model\": \"pi05\", \"per_task\": {\"T0_alphabet_soup_tomato_basket\": 0.7, \"T1_cream_cheese_butter_basket\": 0.4, \"T2_stove_moka_pot\": 0.72, \"T3_bowl_bottom_drawer\": 0.72, \"T4_white_mug_left_yellow_right\": 0.52, \"T5_book_caddy\": 0.2, \"T6_white_mug_plate_chocolate\": 0.26, \"T7_alphabet_soup_cream_cheese_basket\": 0.56, \"T8_both_moka_pots_stove\": 0.04, \"T9_yellow_mug_microwave\": 0.56}, \"prune_mode\": \"random\", \"seed\": 42, \"success_rate\": 46.8, \"suite\": \"libero_10\", \"total_episodes\": 500, \"total_successes\": 234, \"v1_comparison\": {\"delta_pp\": -3.4, \"note\": \"CPU RNG fix caused -3.4pp drop\", \"v1_sr\": 50.2, \"v2_sr\": 46.8}}, \"status\": \"DONE\"}, \"eval_pi05_attention_k05_goal_seed42\": {\"metrics\": {\"elapsed_min\": 84.9, \"per_task\": {\"T0_open_middle_drawer\": 0.76, \"T1_put_bowl_stove\": 0.4, \"T2_wine_bottle_cabinet\": 0.76, \"T3_open_drawer_bowl\": 0.68, \"T4_bowl_top_cabinet\": 0.94, \"T5_push_plate_front\": 0.7, \"T6_cream_cheese_bowl\": 0.54, \"T7_turn_on_stove\": 1, \"T8_bowl_on_plate\": 0.86, \"T9_wine_bottle_rack\": 0.38}, \"success_rate\": 70.2, \"total_episodes\": 500, \"total_successes\": 351}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_goal_seed42_v4\": {\"metrics\": {\"success_rate\": 37.6, \"total_episodes\": 500, \"total_successes\": 188}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_goal_seed42_v2\": {\"metrics\": {\"success_rate\": 67.2, \"total_episodes\": 500, \"total_successes\": 336}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_object_seed43\": {\"metrics\": {\"success_rate\": 0.71, \"total_episodes\": 500, \"total_successes\": 355, \"wilson_ci_95\": [0.6687, 0.7481]}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed42_v4\": {\"metrics\": {\"success_rate\": 52.4, \"total_episodes\": 500, \"total_successes\": 262}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_spatial_seed42\": {\"metrics\": {\"elapsed_seconds\": 6754.6, \"n_vision_tokens_kept\": 15, \"n_vision_tokens_original\": 50, \"per_task\": {\"task_0\": {\"desc\": \"pick up the black bowl between the plate and the ramekin and place it on the plate\", \"sr\": 0.74}, \"task_1\": {\"desc\": \"pick up the black bowl next to the ramekin and place it on the plate\", \"sr\": 0.06}, \"task_2\": {\"desc\": \"pick up the black bowl from table center and place it on the plate\", \"sr\": 0.82}, \"task_3\": {\"desc\": \"pick up the black bowl on the cookie box and place it on the plate\", \"sr\": 0.34}, \"task_4\": {\"desc\": \"pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate\", \"sr\": 0.66}, \"task_5\": {\"desc\": \"pick up the black bowl on the ramekin and place it on the plate\", \"sr\": 0}, \"task_6\": {\"desc\": \"pick up the black bowl next to the cookie box and place it on the plate\", \"sr\": 0.04}, \"task_7\": {\"desc\": \"pick up the black bowl on the stove and place it on the plate\", \"sr\": 0.08}, \"task_8\": {\"desc\": \"pick up the black bowl next to the plate and place it on the plate\", \"sr\": 0.34}, \"task_9\": {\"desc\": \"pick up the black bowl on the wooden cabinet and place it on the plate\", \"sr\": 0.04}}, \"success_rate\": 0.312, \"total_episodes\": 500, \"total_successes\": 156, \"wilson_ci_95\": [0.273, 0.354]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_goal_seed42_v3\": {\"metrics\": {\"elapsed_min\": 65.8, \"per_task\": {\"T0_open_middle_drawer\": 0.8, \"T1_put_bowl_stove\": 0.92, \"T2_wine_bottle_cabinet\": 0.98, \"T3_open_drawer_bowl\": 0.34, \"T4_bowl_top_cabinet\": 1, \"T5_push_plate_front\": 0, \"T6_cream_cheese_bowl\": 0.24, \"T7_turn_on_stove\": 0.72, \"T8_bowl_on_plate\": 0.9, \"T9_wine_bottle_rack\": 0}, \"success_rate\": 59, \"total_episodes\": 500, \"total_successes\": 295}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_spatial_seed42_v3\": {\"metrics\": {\"elapsed_min\": 82, \"per_task_sr\": [92, 22, 88, 72, 84, 0, 82, 32, 72, 44], \"success_rate\": 58.8, \"total_episodes\": 500, \"wilson_ci_95\": [54.4, 63]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_goal_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 267, \"seed\": 42, \"success_rate\": 0.534, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_goal_seed42_w38\": {\"status\": \"DONE\"}, \"eval_e5_xvla_attn_last_goal_k03\": {\"status\": \"DONE\"}, \"eval_pi05_random_k07_goal_seed42_v2\": {\"metrics\": {\"source\": \"westd-41074 diag harvested, CPU RNG fixed\", \"success_rate\": 78.2, \"total_episodes\": 500, \"total_successes\": 391}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_goal_seed42_v2\": {\"metrics\": {\"source\": \"westd-41074 diag harvested, CPU RNG fixed\", \"success_rate\": 83.8, \"total_episodes\": 500, \"total_successes\": 419}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_goal_seed42_v2\": {\"metrics\": {\"source\": \"westd-41074 GPU diag harvested, CPU RNG fixed\", \"success_rate\": 62.2, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_goal_seed43\": {\"metrics\": {\"comparison_seed42_sr\": 89, \"per_task\": {\"T0_open_middle_drawer_of_cabinet\": 92, \"T1_put_bowl_on_stove\": 98, \"T2_put_wine_bottle_on_top_of_cabinet\": 100, \"T3_open_top_drawer_put_bowl_inside\": 92, \"T4_put_bowl_on_top_of_cabinet\": 98, \"T5_push_plate_to_front_of_stove\": 100, \"T6_put_cream_cheese_in_bowl\": 92, \"T7_turn_on_stove\": 98, \"T8_put_bowl_on_plate\": 96, \"T9_put_wine_bottle_on_rack\": 42}, \"seed\": 43, \"seed_delta_pp\": 1.8, \"success_rate\": 90.8, \"total_episodes\": 500, \"total_successes\": 454}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed42_v2\": {\"metrics\": {\"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 56.6, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_goal_seed42_w38\": {\"status\": \"DONE\"}, \"eval_e5_xvla_attn_mean_goal_k03\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_goal_seed42\": {\"metrics\": {\"keep_ratio\": 0.85, \"prune_mode\": \"l2norm\", \"seed\": 42, \"success_rate\": 88, \"successes\": 440, \"suite\": \"libero_goal\", \"total\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_spatial_seed42\": {\"metrics\": {\"success_rate_mean\": 60.4}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_goal_seed42_v2\": {\"metrics\": {\"per_task\": {\"T0\": 86, \"T1\": 96, \"T2\": 100, \"T3\": 90, \"T4\": 98, \"T5\": 98, \"T6\": 88, \"T7\": 100, \"T8\": 94, \"T9\": 40}, \"success_rate\": 89, \"total_episodes\": 500, \"total_successes\": 445}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_goal_seed42_v2\": {\"metrics\": {\"elapsed_min\": 74.8, \"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 71.2, \"total_episodes\": 500, \"total_successes\": 356}, \"status\": \"DONE\"}, \"eval_openvla_baseline_goal_seed42_v3\": {\"metrics\": {\"elapsed_min\": 242.4, \"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 74.8, \"total_episodes\": 500, \"total_successes\": 374}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_spatial_seed42_v2\": {\"metrics\": {\"elapsed_min\": 67.3, \"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 88.6, \"total_episodes\": 500, \"total_successes\": 443}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_long_seed42_v2\": {\"status\": \"PREPARING\"}, \"eval_pi05_l2norm_k03_goal_seed42_v2\": {\"metrics\": {\"per_task\": {\"T0\": 66, \"T1\": 22, \"T2\": 76, \"T3\": 32, \"T4\": 62, \"T5\": 30, \"T6\": 20, \"T7\": 96, \"T8\": 78, \"T9\": 24}, \"success_rate\": 50.6, \"total_episodes\": 500, \"total_successes\": 253}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_goal_seed42\": {\"metrics\": {\"elapsed_min\": 158.9, \"episodes\": 500, \"per_task_sr\": {\"task0_open_middle_drawer\": 0, \"task1_bowl_on_stove\": 0, \"task2_wine_on_cabinet\": 0, \"task3_open_drawer_bowl_inside\": 0, \"task4_bowl_on_cabinet\": 0, \"task5_push_plate_front_stove\": 0, \"task6_cream_cheese_in_bowl\": 0, \"task7_turn_on_stove\": 0, \"task8_bowl_on_plate\": 0, \"task9_wine_on_rack\": 0}, \"success_rate\": 0, \"tasks\": 10, \"wilson_ci_95\": [0, 0.8]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_goal_seed42_v2\": {\"metrics\": {\"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 73.6, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_goal_seed42_v2\": {\"metrics\": {\"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 90.6, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_goal_seed42_v2\": {\"metrics\": {\"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 89.4, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_rollout_goal_k05_v2\": {\"metrics\": {\"elapsed_min\": 31.1, \"success_rate\": 96.8, \"total_episodes\": 500, \"total_successes\": 484, \"wilson_ci_95\": [94.9, 98]}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_mean_goal_k05_v2\": {\"metrics\": {\"elapsed_min\": 30.2, \"success_rate\": 97.4, \"total_episodes\": 500, \"total_successes\": 487, \"wilson_ci_95\": [95.6, 98.5]}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_last_goal_k05_v2\": {\"metrics\": {\"elapsed_min\": 30, \"success_rate\": 98.2, \"total_episodes\": 500, \"total_successes\": 491, \"wilson_ci_95\": [96.6, 99.1]}, \"status\": \"DONE\"}, \"eval_e5_xvla_random_goal_k05_v2\": {\"metrics\": {\"elapsed_min\": 58.2, \"success_rate\": 67.2, \"total_episodes\": 500, \"total_successes\": 336, \"wilson_ci_95\": [63, 71.2]}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_goal_seed42_v2\": {\"metrics\": {\"source\": \"westd-41074 diag harvested, CPU RNG fixed\", \"success_rate\": 50.6, \"total_episodes\": 500, \"total_successes\": 253}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_last_obj_k03\": {\"metrics\": {\"elapsed_min\": 45.2, \"source\": \"Worker harvested from westd-27271\", \"success_rate\": 84.2, \"total_episodes\": 500, \"total_successes\": 421, \"wilson_ci_95\": [80.7, 87.1]}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_rollout_obj_k03\": {\"metrics\": {\"source\": \"Director harvested from westd-38929\", \"success_rate\": 92, \"total_episodes\": 500, \"total_successes\": 460}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_mean_spatial_k03\": {\"metrics\": {\"source\": \"Director harvested from westd-38929\", \"success_rate\": 90.4, \"total_episodes\": 500, \"total_successes\": 452}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_last_spatial_k03\": {\"metrics\": {\"source\": \"Director harvested from westd-38929\", \"success_rate\": 85.6, \"total_episodes\": 500, \"total_successes\": 428}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_mean_obj_k03\": {\"metrics\": {\"source\": \"Director harvested from westd-38929\", \"success_rate\": 96, \"total_episodes\": 500, \"total_successes\": 480}, \"status\": \"DONE\"}, \"eval_openvla_baseline_goal_seed42_v2\": {\"status\": \"PREPARING\"}, \"diag_find_pi05_path\": {\"status\": \"PREPARING\"}, \"diag_openvla_script_model_path\": {\"status\": \"PREPARING\"}, \"eval_pi05_l2norm_k0925_spatial_seed42\": {\"metrics\": {\"overall_SR\": 0.97, \"per_task\": {\"T0\": 1, \"T1\": 0.98, \"T2\": 0.98, \"T3\": 0.94, \"T4\": 0.92, \"T5\": 0.94, \"T6\": 1, \"T7\": 0.98, \"T8\": 1, \"T9\": 0.96}, \"total_episodes\": 500, \"total_successes\": 485}, \"status\": \"DONE\"}, \"eval_openvla_baseline_goal_seed42\": {\"status\": \"PREPARING\"}, \"eval_pi05_random_k085_spatial_seed42\": {\"metrics\": {\"seed\": 42, \"success_rate\": 0.584, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_goal_seed42\": {\"status\": \"PREPARING\"}, \"eval_pi05_random_k0925_goal_seed42\": {\"status\": \"PREPARING\"}, \"diag_openvla_script_args\": {\"status\": \"PREPARING\"}, \"diag_openvla_shards_check\": {\"status\": \"PREPARING\"}, \"diag_openvla_status_v3\": {\"status\": \"PREPARING\"}, \"eval_pi05_random_k09_goal_seed42_cqa1\": {\"metrics\": {\"keep_ratio\": 0.9, \"prune_mode\": \"random\", \"seed\": 42, \"success_rate\": 84, \"successes\": 420, \"suite\": \"libero_goal\", \"total\": 500}, \"status\": \"PREPARING\"}, \"eval_pi05_random_k085_goal_seed42\": {\"metrics\": {\"keep_ratio\": 0.85, \"prune_mode\": \"random\", \"seed\": 42, \"success_rate\": 51.6, \"successes\": 258, \"suite\": \"libero_goal\", \"total\": 500}, \"status\": \"PREPARING\"}, \"eval_pi05_random_k05_goal_seed42\": {\"metrics\": {\"keep_ratio\": 0.5, \"prune_mode\": \"random\", \"seed\": 42, \"success_rate\": 73.6, \"successes\": 368, \"suite\": \"libero_goal\", \"total\": 500}, \"status\": \"PREPARING\"}, \"diag_read_long_seed43\": {\"status\": \"PREPARING\"}, \"diag_read_goal_v2\": {\"status\": \"PREPARING\"}, \"diag_read_cqa1_goal_results\": {\"status\": \"PREPARING\"}, \"diag_read_goal_results\": {\"status\": \"PREPARING\"}, \"eval_pi05_l2norm_k085_object_cqa1\": {\"metrics\": {\"keep_ratio\": 0.85, \"prune_mode\": \"l2norm\", \"seed\": 43, \"success_rate\": 99, \"successes\": 495, \"suite\": \"libero_object\", \"total\": 500}, \"status\": \"PREPARING\"}, \"eval_pi05_l2norm_k03_object_cqa1\": {\"metrics\": {\"keep_ratio\": 0.3, \"prune_mode\": \"l2norm\", \"seed\": 43, \"success_rate\": 59, \"successes\": 295, \"suite\": \"libero_object\", \"total\": 500}, \"status\": \"PREPARING\"}, \"eval_pi05_random_k03_object_cqa1\": {\"metrics\": {\"keep_ratio\": 0.3, \"prune_mode\": \"random\", \"seed\": 43, \"success_rate\": 32.2, \"successes\": 161, \"suite\": \"libero_object\", \"total\": 500}, \"status\": \"PREPARING\"}, \"eval_pi05_random_k085_object_cqa1\": {\"metrics\": {\"keep_ratio\": 0.85, \"prune_mode\": \"random\", \"seed\": 43, \"success_rate\": 3.6, \"successes\": 18, \"suite\": \"libero_object\", \"total\": 500}, \"status\": \"PREPARING\"}, \"diag_cqa1_find_goal_k09\": {\"status\": \"PREPARING\"}, \"diag_westd41074_find_goal_logs\": {\"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_rollout_spatial_k07\": {\"metrics\": {\"ci_95\": [90.4, 94.9], \"success_rate\": 93, \"successes\": 465, \"total\": 500}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_mean_long_k05_seed43\": {\"metrics\": {\"ci_95\": [92.3, 96.3], \"success_rate\": 94.6, \"successes\": 473, \"total\": 500}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_last_long_k05_seed43\": {\"metrics\": {\"ci_95\": [87.5, 92.7], \"success_rate\": 90.4, \"successes\": 452, \"total\": 500}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_rollout_long_k05_w38\": {\"metrics\": {\"ci_95\": [92.5, 96.4], \"success_rate\": 94.8, \"successes\": 474, \"total\": 500}, \"status\": \"PREPARING\"}, \"diag_openvla_download_check\": {\"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_rollout_obj_k07_w27\": {\"metrics\": {\"elapsed_min\": 32.2, \"episodes\": 500, \"per_task_sr\": {\"T0\": 100, \"T1\": 100, \"T2\": 96, \"T3\": 96, \"T4\": 100, \"T5\": 98, \"T6\": 100, \"T7\": 94, \"T8\": 100, \"T9\": 100}, \"success_rate\": 98.4, \"successes\": 492, \"wilson_ci_95\": [96.9, 99.2]}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_rollout_goal_k05\": {\"metrics\": {\"episodes\": 500, \"success_rate\": 0, \"successes\": 0}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_mean_goal_k05\": {\"metrics\": {\"episodes\": 500, \"success_rate\": 0, \"successes\": 0}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_rollout_long_k05_w27\": {\"status\": \"PREPARING\"}, \"eval_pi05_random_k03_long_seed43_v5\": {\"metrics\": {\"source\": \"westd-41074 tmux log\", \"success_rate\": 28.2, \"total_episodes\": 500}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_mean_long_k05\": {\"metrics\": {\"episodes\": 500, \"success_rate\": 94, \"successes\": 470}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_last_goal_k05\": {\"metrics\": {\"episodes\": 500, \"success_rate\": 0, \"successes\": 0}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_mean_spatial_k05\": {\"metrics\": {\"episodes\": 500, \"success_rate\": 91.6, \"successes\": 458, \"wilson_ci_95\": [88.8, 93.7]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_goal_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 450, \"seed\": 42, \"success_rate\": 0.9, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_goal_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 403, \"seed\": 42, \"success_rate\": 0.806, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_goal_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 296, \"seed\": 42, \"success_rate\": 0.592, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43_v4\": {\"metrics\": {\"elapsed_min\": 140.4, \"overall_sr\": 0.77, \"total_episodes\": 500, \"total_successes\": 385}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed43_v3\": {\"metrics\": {\"elapsed_min\": 170.8, \"overall_sr\": 0.424, \"total_episodes\": 500, \"total_successes\": 212}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_long_seed43_v4\": {\"metrics\": {\"elapsed_min\": 148, \"overall_sr\": 0.654, \"total_episodes\": 500, \"total_successes\": 327}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_rollout_spatial_k05\": {\"metrics\": {\"elapsed_min\": 42.8, \"episodes\": 500, \"overall_sr\": 92.8, \"per_task_sr\": {\"T0_bowl_between_plate_ramekin\": 100, \"T1_bowl_next_ramekin\": 100, \"T2_bowl_table_center\": 100, \"T3_bowl_on_cookie_box\": 100, \"T4_bowl_top_drawer_cabinet\": 90, \"T5_bowl_on_ramekin\": 46, \"T6_bowl_next_cookie_box\": 100, \"T7_bowl_on_stove\": 94, \"T8_bowl_next_plate\": 98, \"T9_bowl_on_cabinet\": 100}, \"tasks\": 10, \"wilson_ci_95\": [90.2, 94.8]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed43\": {\"metrics\": {\"source\": \"westd-41074 pi05_l2norm_k0.30_libero_10_seed43.json\", \"success_rate\": 35.2, \"total_episodes\": 500, \"total_successes\": 176}, \"status\": \"PREPARING\"}, \"eval_pi05_random_k05_long_seed43\": {\"metrics\": {\"source\": \"westd-41074 pi05_random_k0.50_libero_10_seed43.json\", \"success_rate\": 51.2, \"total_episodes\": 500}, \"status\": \"PREPARING\"}, \"eval_pi05_random_k05_object_cqa1\": {\"metrics\": {\"elapsed_min\": 135.3, \"episodes\": 500, \"per_task_sr\": {\"T8\": 64, \"T9\": 62}, \"source\": \"cqa1-33015 /tmp/pi05_random_k050_object.log\", \"success_rate\": 66.2, \"successes\": 331}, \"status\": \"PREPARING\"}, \"eval_pi05_l2norm_k07_object_cqa1\": {\"metrics\": {\"elapsed_min\": 135.6, \"episodes\": 500, \"source\": \"cqa1-33015 /tmp/pi05_l2norm_k070_object.log\", \"success_rate\": 56.8, \"successes\": 284}, \"status\": \"PREPARING\"}, \"eval_pi05_l2norm_k05_object_cqa1\": {\"metrics\": {\"elapsed_min\": 150.2, \"episodes\": 500, \"source\": \"cqa1-33015 /tmp/pi05_l2norm_k050_object.log\", \"success_rate\": 32, \"successes\": 160}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_last_spatial_k05\": {\"metrics\": {\"elapsed_min\": 47.2, \"episodes\": 500, \"per_task_sr\": {\"T0\": 98, \"T1\": 100, \"T2\": 100, \"T3\": 98, \"T4\": 86, \"T5\": 22, \"T6\": 98, \"T7\": 88, \"T8\": 98, \"T9\": 100}, \"success_rate\": 88.8, \"successes\": 444, \"wilson_ci_95\": [85.7, 91.3]}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_last_long_k05\": {\"metrics\": {\"elapsed_min\": 59.1, \"episodes\": 500, \"per_task_sr\": {\"T0\": 96, \"T1\": 66, \"T2\": 100, \"T3\": 98, \"T4\": 90, \"T5\": 94, \"T6\": 94, \"T7\": 70, \"T8\": 96, \"T9\": 98}, \"success_rate\": 90.2, \"successes\": 451, \"wilson_ci_95\": [87.3, 92.5]}, \"status\": \"PREPARING\"}, \"eval_pi05_random_k07_object_cqa1\": {\"metrics\": {\"elapsed_min\": 123, \"episodes\": 500, \"per_task_sr\": {\"T4\": 86, \"T5\": 48, \"T6\": 88, \"T7\": 70, \"T8\": 86, \"T9\": 80}, \"success_rate\": 78.6, \"successes\": 393}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_last_obj_k07\": {\"metrics\": {\"elapsed_min\": 31.5, \"episodes\": 500, \"per_task_sr\": {\"T0\": 96, \"T1\": 100, \"T2\": 100, \"T3\": 96, \"T4\": 100, \"T5\": 100, \"T6\": 100, \"T7\": 100, \"T8\": 100, \"T9\": 100}, \"success_rate\": 99.2, \"successes\": 496, \"wilson_ci_95\": [98, 99.7]}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_rollout_obj_k05\": {\"metrics\": {\"elapsed_min\": 34.1, \"episodes\": 500, \"per_task_sr\": {\"T0\": 100, \"T1\": 100, \"T2\": 96, \"T3\": 96, \"T4\": 98, \"T5\": 96, \"T6\": 100, \"T7\": 88, \"T8\": 100, \"T9\": 100}, \"success_rate\": 97.4, \"successes\": 487, \"wilson_ci_95\": [95.6, 98.5]}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_mean_obj_k05\": {\"metrics\": {\"elapsed_min\": 33.3, \"episodes\": 500, \"per_task_sr\": {\"T0\": 100, \"T1\": 98, \"T2\": 96, \"T3\": 96, \"T4\": 100, \"T5\": 98, \"T6\": 100, \"T7\": 96, \"T8\": 100, \"T9\": 100}, \"success_rate\": 98.4, \"successes\": 492, \"wilson_ci_95\": [96.9, 99.2]}, \"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_last_obj_k05\": {\"metrics\": {\"elapsed_min\": 32.1, \"episodes\": 500, \"per_task_sr\": {\"T0\": 98, \"T1\": 100, \"T2\": 100, \"T3\": 100, \"T4\": 100, \"T5\": 98, \"T6\": 100, \"T7\": 96, \"T8\": 100, \"T9\": 100}, \"success_rate\": 99.2, \"successes\": 496, \"wilson_ci_95\": [98, 99.7]}, \"status\": \"PREPARING\"}, \"eval_pi05_l2norm_k07_goal_seed42\": {\"metrics\": {\"overall_SR\": 0.712, \"source\": \"westd-41074 log harvested by worker\", \"total_episodes\": 500, \"total_successes\": 356}, \"status\": \"DEPLOYED\"}, \"eval_pi05_random_k09_goal_seed42\": {\"metrics\": {\"overall_SR\": 0.58, \"source\": \"westd-41074 log harvested by worker\", \"total_episodes\": 500, \"total_successes\": 290}, \"status\": \"DEPLOYED\"}, \"diag_cqa1_logs\": {\"status\": \"PREPARING\"}, \"eval_e5_xvla_attn_mean_obj_k05_w27\": {\"status\": \"PREPARING\"}, \"eval_xvla_l2norm_k07_long_seed42_v2\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43_v3_r\": {\"status\": \"PREPARING\"}, \"eval_pi05_random_k085_long_seed43_v2_r\": {\"status\": \"PREPARING\"}, \"eval_pi05_l2norm_k07_long_seed43_v3_r\": {\"status\": \"PREPARING\"}, \"eval_pi05_random_k03_long_seed43_v4_r\": {\"status\": \"PREPARING\"}, \"diag_find_e5_westd27271\": {\"status\": \"PREPARING\"}, \"diag_transfer_e5_v2\": {\"status\": \"PREPARING\"}, \"diag_transfer_e5_script\": {\"status\": \"PREPARING\"}, \"diag_westd38929_e5_check\": {\"status\": \"PREPARING\"}, \"diag_find_pi05_script\": {\"status\": \"PREPARING\"}, \"eval_xvla_l2norm_k07_long_seed42\": {\"metrics\": {\"overall_SR\": 0.494, \"per_task_SR\": {\"T0_alphabet_soup_tomato\": 0.12, \"T1_cream_cheese_butter\": 0.04, \"T2_stove_moka\": 0.56, \"T3_bowl_drawer\": 0.98, \"T4_mugs_plates\": 0.68, \"T5_book_caddy\": 0.94, \"T6_mug_pudding\": 0.78, \"T7_soup_cream_cheese\": 0.76, \"T8_two_moka_pots\": 0, \"T9_mug_microwave\": 0.08}, \"total_episodes\": 500, \"total_successes\": 247}, \"status\": \"DONE\"}, \"eval_xvla_random_k09_long_seed42\": {\"metrics\": {\"elapsed_min\": 104.4, \"episodes\": 500, \"overall_sr\": 29.6, \"per_task_sr\": {\"task_0_alphabet_soup_tomato_sauce\": 0, \"task_1_cream_cheese_butter\": 16, \"task_2_stove_moka_pot\": 0, \"task_3_black_bowl_drawer\": 96, \"task_4_white_mug_yellow_mug\": 36, \"task_5_book_caddy\": 98, \"task_6_white_mug_chocolate_pudding\": 0, \"task_7_alphabet_soup_cream_cheese\": 0, \"task_8_both_moka_pots\": 0, \"task_9_mug_microwave\": 50}, \"wilson_ci_95\": [25.8, 33.7]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_object_seed42_v3\": {\"status\": \"PREPARING\"}, \"eval_xvla_random_k07_long_seed42\": {\"metrics\": {\"keep_ratio\": 0.7, \"per_task_sr\": [10, 8, 66, 98, 82, 100, 82, 70, 4, 10], \"prune_method\": \"random\", \"seed\": 42, \"success_rate\": 53, \"suite\": \"libero_10\", \"tokens_kept\": \"35/50\", \"total_episodes\": 500, \"total_successes\": 265, \"wall_time_min\": 87, \"wilson_ci_95\": [48.6, 57.3]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_object_seed42_v2\": {\"metrics\": {\"per_task_sr\": [96, 98, 96, 96, 96, 100, 100, 100, 100, 100], \"success_rate\": 98.2, \"tokens_kept\": 243, \"tokens_total\": 256, \"total_episodes\": 500, \"total_successes\": 491, \"wall_time_min\": 63.2}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_object_seed43_v4\": {\"metrics\": {\"keep_ratio\": 0.9, \"per_task_sr\": [16, 16, 10, 2, 6, 14, 14, 2, 8, 8], \"prune_method\": \"random\", \"seed\": 43, \"success_rate\": 9.6, \"suite\": \"libero_object\", \"tokens_kept\": 230, \"tokens_total\": 256, \"total_episodes\": 500, \"total_successes\": 48, \"wall_time_min\": 119.5}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_spatial_seed42\": {\"metrics\": {\"overall_SR\": 0.766, \"total_episodes\": 500, \"total_successes\": 383}, \"status\": \"DONE\"}, \"eval_xvla_random_k095_long_seed42\": {\"metrics\": {\"eval_episodes_per_task\": 50, \"keep_ratio\": 0.95, \"per_task_sr\": [0, 46, 72, 90, 54, 98, 18, 10, 92, 2], \"prune_method\": \"random\", \"seed\": 42, \"success_rate\": 48.2, \"suite\": \"libero_10\", \"tokens_kept\": \"47/50\", \"total_episodes\": 500, \"total_success\": 241, \"wall_time_min\": 91.2, \"wilson_ci_95\": [43.9, 52.6]}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_object_seed43_v3\": {\"metrics\": {\"note\": \"Harvested from eval_results/pi05_random_k0.90_libero_object_seed43.json on westd-27271. Reviewer-confirmed.\", \"seed\": 43, \"success_rate\": 9.6, \"total_episodes\": 500, \"total_successes\": 48}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_long_seed43_v3\": {\"status\": \"PREPARING\"}, \"eval_pi05_random_k05_long_seed43_v2\": {\"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.5, \"prune_method\": \"random\", \"success_rate\": 51.2, \"total_episodes\": 500, \"total_success\": 256}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed43\": {\"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.85, \"prune_method\": \"random\", \"success_rate\": 41.8, \"total_episodes\": 500, \"total_success\": 209}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_long_seed43_v2\": {\"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.7, \"prune_method\": \"l2norm\", \"success_rate\": 65.8, \"total_episodes\": 500, \"total_success\": 329}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_long_seed43_v3\": {\"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.3, \"prune_method\": \"random\", \"success_rate\": 28.4, \"total_episodes\": 500, \"total_success\": 142}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43_v2\": {\"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.85, \"per_task_sr\": {\"T2\": 88, \"T3\": 96, \"T4\": 70, \"T5\": 98, \"T6\": 12, \"T7\": 80, \"T8\": 64, \"T9\": 88}, \"prune_method\": \"l2norm\", \"success_rate\": 79, \"total_episodes\": 500, \"total_success\": 395}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_spatial_seed43_v2\": {\"metrics\": {\"elapsed_min\": 80.6, \"per_task_sr\": {\"T0_between_plate_ramekin\": 88, \"T1_next_to_ramekin\": 88, \"T2_table_center\": 88, \"T3_on_cookie_box\": 56, \"T4_top_drawer\": 38, \"T5_on_ramekin\": 32, \"T6_next_to_cookie_box\": 86, \"T7_on_stove\": 92, \"T8_next_to_plate\": 72, \"T9_on_wooden_cabinet\": 84}, \"success_rate\": 72.4, \"total_episodes\": 500, \"total_successes\": 362}, \"status\": \"DONE\"}, \"eval_xvla_baseline_spatial_seed42\": {\"metrics\": {\"note\": \"Corrected from 0.916 to 0.930 per Reviewer SSH verification of xvla_prune_k1.0_libero_spatial.json (465/500)\", \"num_episodes\": 500, \"success_rate\": 0.93, \"total_successes\": 465, \"wilson_ci_95\": [0.904, 0.95]}, \"status\": \"DONE\"}, \"eval_xvla_baseline_goal_seed42\": {\"metrics\": {\"note\": \"Corrected from 0.98 to 0.984 per Reviewer SSH verification (492/500)\", \"num_episodes\": 500, \"success_rate\": 0.984, \"total_successes\": 492, \"wilson_ci_95\": [0.969, 0.992]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k09_seed42\": {\"metrics\": {\"note\": \"Reconstructed entry. SR=99.2% (seed42). Cross-seed range 97.6%–99.2% (seed43=97.6%, seed44=98.2%). Original JSON may exist on cqa1-33015.\", \"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.992}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_long_seed43\": {\"metrics\": {\"sr\": 0.308, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_spatial_seed43\": {\"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed43\": {\"metrics\": {\"overall_SR\": 0.576, \"per_task\": {\"T0\": 0.82, \"T1\": 0.62, \"T2\": 0.9, \"T3\": 0.08, \"T4\": 0.48, \"T5\": 0.38, \"T6\": 0.38, \"T7\": 0.74, \"T8\": 0.92, \"T9\": 0.44}, \"total_episodes\": 500, \"total_successes\": 288}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_spatial_seed43\": {\"metrics\": {\"overall_SR\": 0.88, \"per_task\": {\"T0\": 1, \"T1\": 0.92, \"T2\": 1, \"T3\": 0.78, \"T4\": 0.62, \"T5\": 0.84, \"T6\": 0.96, \"T7\": 0.9, \"T8\": 0.96, \"T9\": 0.82}, \"total_episodes\": 500, \"total_successes\": 440}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_spatial_seed43\": {\"metrics\": {\"overall_SR\": 0.98, \"total_episodes\": 500, \"total_successes\": 490}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_long_seed43\": {\"status\": \"DONE\"}, \"eval_pi05_random_k03_long_seed43\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43\": {\"status\": \"DONE\"}, \"eval_pi05_random_k095_goal_seed42\": {\"metrics\": {\"sr\": 0.84, \"total_episodes\": 500, \"total_successes\": 420}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed42\": {\"metrics\": {\"sr\": 0.39, \"total_episodes\": 500, \"total_successes\": 195}, \"status\": \"DONE\"}, \"eval_xvla_random_k095_object_seed42_v2\": {\"metrics\": {\"elapsed_seconds\": 2068.5, \"success_rate\": 0.988, \"total_episodes\": 500, \"total_successes\": 494}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_long_seed42\": {\"metrics\": {\"elapsed_min\": 171, \"success_rate\": 0.29, \"total_episodes\": 500, \"total_successes\": 145}, \"status\": \"DONE\"}, \"eval_xvla_random_k095_object_seed42\": {\"status\": \"PREPARING\"}, \"eval_pi05_attention_k07_object_seed42\": {\"metrics\": {\"elapsed_min\": 117.26, \"keep_ratio\": 0.7, \"prune_mode\": \"attention\", \"seed\": 42, \"success_rate\": 0.006, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 3}, \"status\": \"DONE\"}, \"eval_smolvla_baseline_spatial_seed42_cqa1\": {\"status\": \"DONE\"}, \"eval_xvla_random_k07_goal_seed42\": {\"metrics\": {\"overall_SR\": 0.572, \"total_episodes\": 500, \"total_successes\": 286}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_long_seed42\": {\"metrics\": {\"overall_SR\": 0.318, \"total_episodes\": 500, \"total_successes\": 159}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_long_seed42\": {\"metrics\": {\"overall_SR\": 0.81, \"total_episodes\": 500, \"total_successes\": 405}, \"status\": \"DONE\"}, \"eval_xvla_random_k09_spatial_seed42\": {\"metrics\": {\"overall_SR\": 0.778, \"total_episodes\": 500, \"total_successes\": 389}, \"status\": \"DONE\"}, \"eval_xvla_random_k09_goal_seed42\": {\"metrics\": {\"overall_SR\": 0.706, \"total_episodes\": 500, \"total_successes\": 353}, \"status\": \"DONE\"}, \"eval_xvla_random_k095_spatial_seed42\": {\"metrics\": {\"overall_SR\": 0.702, \"total_episodes\": 500, \"total_successes\": 351}, \"status\": \"DONE\"}, \"eval_xvla_random_k095_goal_seed42\": {\"metrics\": {\"overall_SR\": 0.54, \"total_episodes\": 500, \"total_successes\": 270}, \"status\": \"DONE\"}, \"eval_openvla_baseline_spatial_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_spatial_seed42\": {\"metrics\": {\"seed\": 42, \"success_rate\": 0.978, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_object_seed43\": {\"metrics\": {\"seed\": 43, \"success_rate\": 0.3, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_smolvla_random_k09_spatial_seed42_cqa1\": {\"status\": \"PREPARING\"}, \"eval_smolvla_l2norm_k09_spatial_seed42_cqa1\": {\"status\": \"PREPARING\"}, \"eval_smolvla_baseline_spatial_seed42\": {\"metrics\": {\"failure_reason\": \"Ghost process: no GPU assigned, PID 224849 likely dead after westd-38929 GPUs reassigned to OpenVLA experiments\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_long_seed42\": {\"metrics\": {\"elapsed_min\": 157.6, \"keep_ratio\": 0.95, \"num_episodes\": 500, \"num_success\": 306, \"prune_mode\": \"random\", \"seed\": 42, \"success_rate\": 0.612, \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed42_v3\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 262, \"seed\": 42, \"success_rate\": 0.524, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_spatial_seed43\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_object_seed43\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_object_seed43_v2\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_object_seed43_v2\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_long_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_goal_seed42_w38929\": {\"status\": \"DONE\"}, \"random_k095_goal_seed42\": {\"status\": \"DONE\"}, \"pi05_l2norm_k09_goal_s42\": {\"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed42_v2\": {\"status\": \"DONE\"}, \"l2norm_k095_goal_seed42\": {\"status\": \"DONE\"}, \"random_k095_long_seed42\": {\"status\": \"DONE\"}, \"pi05_l2norm_k095_long_s42\": {\"status\": \"DONE\"}, \"pi05_random_k09_goal_s42\": {\"status\": \"DONE\"}, \"pi05_l2norm_k085_goal_s42\": {\"status\": \"DONE\"}, \"train_openvla_sc_m96_seed42_v3\": {\"status\": \"DONE\"}, \"train_openvla_sc_m64_seed42_v6\": {\"status\": \"DONE\"}, \"eval_pi05_attention_k085_object_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 461, \"seed\": 42, \"success_rate\": 0.922, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_pi05_attention_k09_object_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 486, \"seed\": 42, \"success_rate\": 0.972, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"smolvla_random_k095_long_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 0, \"seed\": 42, \"success_rate\": 0, \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"smolvla_l2norm_k095_long_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 0, \"seed\": 42, \"success_rate\": 0, \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"smolvla_random_k095_goal_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 21, \"seed\": 42, \"success_rate\": 0.042, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"smolvla_l2norm_k095_goal_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 17, \"seed\": 42, \"success_rate\": 0.034, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"smolvla_random_k095_spatial_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 21, \"seed\": 42, \"success_rate\": 0.042, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"smolvla_l2norm_k095_spatial_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 33, \"seed\": 42, \"success_rate\": 0.066, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"smolvla_baseline_long_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 183, \"seed\": 42, \"success_rate\": 0.366, \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k09_spatial_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 394, \"seed\": 42, \"success_rate\": 0.788, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k09_goal_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 351, \"seed\": 42, \"success_rate\": 0.702, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k095_goal_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 269, \"seed\": 42, \"success_rate\": 0.538, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k095_spatial_seed42\": {\"metrics\": {\"num_episodes\": 500, \"num_success\": 358, \"seed\": 42, \"success_rate\": 0.716, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"eval_pi05_attention_k095_object_seed42\": {\"metrics\": {\"keep_tokens\": 690, \"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.984, \"suite\": \"libero_object\", \"total_tokens\": 768, \"wilson_ci_95\": [0.969, 0.992]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k09_long_seed42\": {\"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.275, \"suite\": \"libero_10\", \"wilson_ci_95\": [0.218, 0.341]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k095_long_seed42\": {\"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.47, \"suite\": \"libero_10\", \"wilson_ci_95\": [0.402, 0.539]}, \"status\": \"DONE\"}, \"eval_xvla_baseline_long_seed42\": {\"metrics\": {\"num_episodes\": 500, \"per_task\": [0.96, 0.68, 1.0, 0.98, 0.94, 0.96, 0.94, 0.96, 1.0, 0.98], \"seed\": 42, \"success_rate\": 0.94, \"suite\": \"libero_10\", \"wilson_ci_95\": [0.916, 0.958]}, \"status\": \"DONE\"}, \"pi05_random_k085_goal_s42\": {\"status\": \"DONE\"}, \"smolvla_official_goal_baseline_s42\": {\"metrics\": {\"success_rate\": 0.608, \"total_episodes\": 500, \"total_successes\": 304, \"wilson_ci_95\": [0.5645, 0.6498]}, \"status\": \"DONE\"}, \"smolvla_official_object_l2norm_k095_s42\": {\"metrics\": {\"success_rate\": 0.002, \"total_episodes\": 500, \"total_successes\": 1, \"wilson_ci_95\": [0.0004, 0.0112]}, \"status\": \"DONE\"}, \"smolvla_official_spatial_baseline_s42\": {\"metrics\": {\"success_rate\": 0.446, \"total_episodes\": 500, \"total_successes\": 223, \"wilson_ci_95\": [0.403, 0.4898]}, \"status\": \"DONE\"}, \"eval_pi05_baseline_goal_seed42\": {\"metrics\": {\"elapsed_min\": 49.7, \"overall_sr\": 0.964, \"per_task\": {\"bowl_on_cabinet\": 1, \"bowl_on_plate\": 1, \"bowl_on_stove\": 1, \"cream_cheese_in_bowl\": 0.96, \"open_middle_drawer\": 0.9, \"open_top_drawer_bowl_inside\": 0.9, \"push_plate_front_stove\": 1, \"turn_on_stove\": 1, \"wine_bottle_on_cabinet\": 0.98, \"wine_bottle_on_rack\": 0.9}, \"total_episodes\": 500, \"total_successes\": 482}, \"status\": \"DONE\"}, \"eval_smolvla_zeromask_l2norm_k095_object_seed42\": {\"metrics\": {\"per_task\": {\"task0_alphabet_soup\": 0, \"task1_cream_cheese\": 0, \"task2_salad_dressing\": 0, \"task3_bbq_sauce\": 0, \"task4_ketchup\": 0, \"task5_tomato_sauce\": 0, \"task6_butter\": 0, \"task7_milk\": 0, \"task8_chocolate_pudding\": 0, \"task9_orange_juice\": 0}, \"success_rate\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_zeromask_random_k095_object_seed42\": {\"metrics\": {\"per_task\": {\"task0_alphabet_soup\": 0, \"task1_cream_cheese\": 0, \"task2_salad_dressing\": 0, \"task3_bbq_sauce\": 0, \"task4_ketchup\": 0, \"task5_tomato_sauce\": 0.02, \"task6_butter\": 0, \"task7_milk\": 0, \"task8_chocolate_pudding\": 0, \"task9_orange_juice\": 0}, \"success_rate\": 0.002, \"total_episodes\": 500, \"total_successes\": 1, \"wilson_ci_95\": [0.0004, 0.0112]}, \"status\": \"DONE\"}, \"train_openvla_sc_m96_seed42\": {\"metrics\": {\"final_eval_loss\": 2.6575, \"final_train_loss\": 2.4509, \"steps_completed\": 99999, \"steps_total\": 100000}, \"status\": \"DONE\"}, \"eval_smolvla_official_l2norm_k090_object_seed42\": {\"metrics\": {\"SR\": 0, \"episodes\": 500, \"note\": \"all 10 tasks 0% SR, mean_steps=280 (max)\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_object_seed43_v4\": {\"metrics\": {\"overall_SR\": 0.322, \"total_episodes\": 500, \"total_successes\": 161}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed43\": {\"metrics\": {\"overall_SR\": 0.038, \"total_episodes\": 500, \"total_successes\": 19}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_spatial_seed43\": {\"metrics\": {\"overall_SR\": 0.52, \"total_episodes\": 500, \"total_successes\": 260}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_spatial_seed43\": {\"metrics\": {\"overall_SR\": 0.512, \"total_episodes\": 500, \"total_successes\": 256}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_object_seed43\": {\"metrics\": {\"overall_SR\": 0.984, \"total_episodes\": 500, \"total_successes\": 492}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_object_seed43\": {\"metrics\": {\"overall_SR\": 0.984, \"total_episodes\": 500, \"total_successes\": 492}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_spatial_seed43\": {\"metrics\": {\"overall_SR\": 0.684, \"total_episodes\": 500, \"total_successes\": 342}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_spatial_seed43\": {\"metrics\": {\"overall_SR\": 0.738, \"total_episodes\": 500, \"total_successes\": 369}, \"status\": \"DONE\"}, \"eval_smart_compress_m32_official\": {\"metrics\": {\"CI_95_wilson\": \"49.0-57.7\", \"SR\": 53.4, \"episodes\": 500, \"per_task_SR\": [64, 48, 56, 46, 46, 28, 78, 42, 66, 60]}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_object_seed43\": {\"metrics\": {\"elapsed_min\": 82.3, \"success_rate\": 68.4, \"total_episodes\": 500, \"total_successes\": 342}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_object_seed43\": {\"metrics\": {\"elapsed_min\": 86.9, \"success_rate\": 73.8, \"total_episodes\": 500, \"total_successes\": 369}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed43\": {\"metrics\": {\"overall_SR\": 0.984, \"per_task\": {\"T0\": 1, \"T1\": 1, \"T2\": 1, \"T3\": 0.98, \"T4\": 1, \"T5\": 0.96, \"T6\": 0.98, \"T7\": 0.92, \"T8\": 1, \"T9\": 1}, \"total_episodes\": 500, \"total_successes\": 492}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_spatial_seed43\": {\"metrics\": {\"overall_SR\": 0.956, \"total_episodes\": 500, \"total_successes\": 478}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_spatial_seed43\": {\"metrics\": {\"overall_SR\": 0.536, \"total_episodes\": 500, \"total_successes\": 268}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_spatial_seed43\": {\"metrics\": {\"overall_SR\": 0.578, \"total_episodes\": 500, \"total_successes\": 289}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_object_seed42_v5\": {\"metrics\": {\"overall_SR\": 0.392, \"per_task\": {\"T0\": 0.56, \"T1\": 0.14, \"T2\": 0.38, \"T3\": 0.32, \"T4\": 0.7, \"T5\": 0.32, \"T6\": 0.12, \"T7\": 0.5, \"T8\": 0.44, \"T9\": 0.44}, \"total_episodes\": 500, \"total_successes\": 196}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed43\": {\"metrics\": {\"overall_SR\": 0.768, \"per_task\": {\"T0\": 1, \"T1\": 0.94, \"T2\": 1, \"T3\": 0.6, \"T4\": 0.36, \"T5\": 0.76, \"T6\": 0.9, \"T7\": 0.74, \"T8\": 1, \"T9\": 0.38}, \"total_episodes\": 500, \"total_successes\": 384}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_object_seed43_v2\": {\"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed43_v2\": {\"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed42_v2\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_object_seed43_v3\": {\"metrics\": {\"success_rate_mean\": 57.2}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed42_v4\": {\"metrics\": {\"success_rate_mean\": 76.4}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_object_seed43\": {\"metrics\": {\"elapsed_min\": 85.5, \"per_task_sr\": {\"T0_alphabet_soup\": 0.7, \"T1_cream_cheese\": 0.9, \"T2_salad_dressing\": 0.78, \"T3_bbq_sauce\": 0.66, \"T4_ketchup\": 0.54, \"T5_tomato_sauce\": 0.8, \"T6_butter\": 0.82, \"T7_milk\": 0.66, \"T8_chocolate_pudding\": 0.78, \"T9_orange_juice\": 0.64}, \"success_rate\": 0.728, \"total_episodes\": 500, \"total_successes\": 364}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed43_v3\": {\"metrics\": {\"success_rate_mean\": 3.8}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_object_seed43_v3\": {\"status\": \"PREPARING\"}, \"eval_pi05_l2norm_k0925_object_seed42\": {\"metrics\": {\"n_episodes\": 500, \"per_task\": {\"T0_alphabet_soup\": 98, \"T1_cream_cheese\": 98, \"T2_salad_dressing\": 96, \"T3_bbq_sauce\": 100, \"T4_ketchup\": 100, \"T5_tomato_sauce\": 100, \"T6_butter\": 100, \"T7_milk\": 100, \"T8_chocolate_pudding\": 100, \"T9_orange_juice\": 100}, \"success_rate\": 99.2, \"successes\": 496}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed42_v3\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_spatial_seed42_v2\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_spatial_seed42\": {\"metrics\": {\"duration_min\": 98.8, \"episodes\": 500, \"per_task_sr\": \"10 tasks completed, overall 335/500\", \"success_rate\": 67, \"tasks\": 10}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_spatial_seed42\": {\"metrics\": {\"episodes_per_task\": 50, \"keep_ratio\": 0.9, \"prune_mode\": \"l2norm\", \"seed\": 42, \"success_rate_mean\": 0.95, \"suite\": \"libero_spatial\", \"tasks_evaluated\": 10, \"total_episodes\": 500, \"total_success\": 475}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_spatial_seed42\": {\"metrics\": {\"episodes_per_task\": 50, \"keep_ratio\": 0.9, \"prune_mode\": \"random\", \"seed\": 42, \"success_rate_mean\": 0.546, \"suite\": \"libero_spatial\", \"tasks_evaluated\": 10, \"total_episodes\": 500, \"total_success\": 273}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_spatial_seed42_v2\": {\"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed42_v4\": {\"metrics\": {\"elapsed_min\": 64.35, \"overall_sr\": 0.98, \"per_task_sr\": {\"T0_alphabet_soup\": 1, \"T1_cream_cheese\": 1, \"T2_salad_dressing\": 0.98, \"T3_bbq_sauce\": 0.98, \"T4_ketchup\": 0.98, \"T5_tomato_sauce\": 0.98, \"T6_butter\": 1, \"T7_milk\": 0.88, \"T8_chocolate_pudding\": 1, \"T9_orange_juice\": 1}, \"total_episodes\": 500, \"total_successes\": 490}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_baseline_spatial_seed42_v3\": {\"status\": \"DONE\"}, \"train_openvla_sc_m32_vtconly_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_object_seed42\": {\"status\": \"PREPARING\"}, \"eval_pi05_l2norm_k085_object_seed42_v3\": {\"status\": \"PREPARING\"}, \"eval_pi05_random_k0925_object_seed42\": {\"metrics\": {\"elapsed_min\": 108.9, \"overall_sr\": 0.276, \"per_task_sr\": [0.34, 0.42, 0.24, 0.14, 0.08, 0.42, 0.4, 0.12, 0.34, 0.26], \"total_episodes\": 500, \"total_successes\": 138}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_object_seed43\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed42_v2\": {\"metrics\": {\"duration_min\": 108.5, \"episodes\": 500, \"per_task_sr\": \"10 tasks completed, overall 25/500\", \"success_rate\": 5, \"tasks\": 10}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_spatial_seed42\": {\"metrics\": {\"per_task_sr\": {\"T0_between_plate\": 66, \"T1_next_to_ramekin\": 80, \"T2_from_table_center\": 62, \"T3_on_cookie_box\": 14, \"T4_in_top_drawer\": 30, \"T5_on_ramekin\": 28, \"T6_next_to_cookie\": 32, \"T7_on_stove\": 64, \"T8_next_to_plate\": 82, \"T9_on_wooden_cab\": 38}, \"success_rate\": 49.6, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_fixedmask_object_seed42_v2\": {\"metrics\": {\"per_task_sr\": [0.12, 0.26, 0.16, 0.14, 0.12, 0.24, 0.18, 0.14, 0.24, 0.1], \"success_rate\": 0.17, \"successes\": 85, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"train_smart_compress_m16_seed44_v3\": {\"metrics\": {\"eval_action_loss\": 0.0495, \"total_steps\": 99999, \"train_action_loss\": 0.0677, \"train_grad_norm\": 1.88821}, \"status\": \"DONE\"}, \"train_smart_compress_m16_seed43\": {\"metrics\": {\"eval_action_loss\": 0.06236, \"total_steps\": 99999, \"train_action_loss\": 0.07652, \"train_grad_norm\": 0.97135}, \"status\": \"DONE\"}, \"train_smart_compress_m128_seed43\": {\"metrics\": {\"eval_action_loss\": 0.06125, \"total_steps\": 99999, \"train_action_loss\": 0.05584, \"train_grad_norm\": 0.95519}, \"status\": \"DONE\"}, \"train_smart_compress_m96_seed44\": {\"metrics\": {\"eval_action_loss\": 0.05259, \"total_steps\": 99999, \"train_action_loss\": 0.04668, \"train_grad_norm\": 0.97222}, \"status\": \"DONE\"}, \"train_smart_compress_m32_seed44\": {\"metrics\": {\"eval_action_loss\": 0.0635, \"total_steps\": 99999, \"train_action_loss\": 0.04146, \"train_grad_norm\": 0.57272}, \"status\": \"DONE\"}, \"train_smart_compress_m64_seed44\": {\"metrics\": {\"eval_action_loss\": 0.06994, \"total_steps\": 99999, \"train_action_loss\": 0.031, \"train_grad_norm\": 1.08378}, \"status\": \"DONE\"}, \"train_smart_compress_m128_resume\": {\"metrics\": {\"eval_action_loss\": 0.05743, \"resumed_from_step\": 32001, \"total_steps\": 99999, \"train_action_loss\": 0.05412, \"train_grad_norm\": 0.92663}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_spatial_seed42\": {\"metrics\": {\"per_task_sr\": {\"T0_between_plate\": 90, \"T1_next_to_ramekin\": 96, \"T2_table_center\": 94, \"T3_on_cookie_box\": 52, \"T4_in_top_drawer\": 60, \"T5_on_ramekin\": 42, \"T6_next_to_cookie\": 58, \"T7_on_stove\": 76, \"T8_next_to_plate\": 80, \"T9_on_wooden_cab\": 96}, \"success_rate\": 74.4, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_object_seed43\": {\"metrics\": {\"SR\": 0.554, \"elapsed_min\": 85.15, \"per_task\": {\"alphabet_soup\": 0.16, \"bbq_sauce\": 0.54, \"butter\": 0.52, \"chocolate_pudding\": 0.92, \"cream_cheese\": 0.56, \"ketchup\": 0.4, \"milk\": 0.14, \"orange_juice\": 0.54, \"salad_dressing\": 0.9, \"tomato_sauce\": 0.86}, \"total_episodes\": 500, \"total_successes\": 277}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k09_object_seed42\": {\"metrics\": {\"elapsed_minutes\": 228.5, \"overall_sr\": 0.706, \"per_task_sr\": {\"alphabet_soup\": 0.66, \"bbq_sauce\": 0.48, \"butter\": 0.74, \"chocolate_pudding\": 0.78, \"cream_cheese\": 0.58, \"ketchup\": 0.9, \"milk\": 0.74, \"orange_juice\": 0.88, \"salad_dressing\": 0.66, \"tomato_sauce\": 0.64}, \"total_episodes\": 500, \"total_successes\": 353}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_object_seed43\": {\"metrics\": {\"overall_sr\": 0.336, \"per_task_sr\": {\"alphabet_soup\": 0.44, \"bbq_sauce\": 0.04, \"butter\": 0.32, \"chocolate_pudding\": 0.46, \"cream_cheese\": 0.08, \"ketchup\": 0.6, \"milk\": 0.52, \"orange_juice\": 0.52, \"salad_dressing\": 0, \"tomato_sauce\": 0.38}, \"total_episodes\": 500, \"total_successes\": 168}, \"status\": \"DONE\"}, \"eval_smolvla_official_random_k050_object_seed42\": {\"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_official_random_k090_object_seed42\": {\"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_official_l2norm_k030_object_seed42\": {\"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_official_random_k070_object_seed42\": {\"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_official_random_k030_object_seed42\": {\"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_official_l2norm_k050_object_seed42\": {\"metrics\": {\"seed\": 42, \"success_rate\": 0, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_spatial_seed42\": {\"metrics\": {\"comparison\": {\"vs_baseline_spatial\": \"55.6 vs 97.2 (-41.6pp)\", \"vs_l2norm_k05_object\": \"55.6 vs 33.4 (+22.2pp)\", \"vs_random_k05_spatial\": \"55.6 vs 71.6 (-16.0pp)\"}, \"elapsed_min\": 108.9, \"overall_sr\": 55.6, \"per_task_sr\": {\"T0_pick_up_black_bowl_between_plate\": 74, \"T1_pick_up_black_bowl_next_to_ramekin\": 82, \"T2_pick_up_black_bowl_on_plate\": 78, \"T3_pick_up_black_bowl_on_cookie_box\": 28, \"T4_pick_up_black_bowl_in_top_drawer\": 38, \"T5_pick_up_black_bowl_on_ramekin\": 44, \"T6_pick_up_black_bowl_next_to_cookie\": 32, \"T7_pick_up_black_bowl_on_stove\": 74, \"T8_pick_up_black_bowl_next_to_plate\": 62, \"T9_pick_up_black_bowl_on_wooden_cab\": 44}, \"total_episodes\": 500, \"total_successes\": 278}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_spatial_seed42\": {\"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"elapsed_min\": 108.4, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k03_spatial_seed42.log\", \"overall_sr\": 57.2, \"per_task_sr\": {\"T0_bowl_between_plate\": 62, \"T1_bowl_next_to_ramekin\": 72, \"T2_bowl_from_table_center\": 78, \"T3_bowl_on_cookie_box\": 24, \"T4_bowl_in_top_drawer\": 34, \"T5_bowl_on_ramekin\": 26, \"T6_bowl_next_to_cookie\": 74, \"T7_bowl_on_stove\": 90, \"T8_bowl_next_to_plate\": 66, \"T9_bowl_on_wooden_cabinet\": 46}, \"result_json\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.30_libero_spatial_seed42.json\", \"seed\": 42, \"total_episodes\": 500, \"total_successes\": 286}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_random_k09_fixedmask_object_seed42\": {\"metrics\": {\"error\": \"Network unreachable - AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224') failed because AutoDL network was not enabled (source /etc/network_turbo not run). No episodes executed.\", \"overall_sr\": null, \"total_episodes\": 0}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_object_seed42\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k01_object_seed42\": {\"metrics\": {\"elapsed_min\": 117.55, \"overall_sr\": 0.026, \"per_task_sr\": {\"T0_alphabet_soup\": 0.02, \"T1_cream_cheese\": 0.06, \"T2_salad_dressing\": 0.04, \"T3_bbq_sauce\": 0.02, \"T4_ketchup\": 0.04, \"T5_tomato_sauce\": 0.02, \"T6_butter\": 0, \"T7_milk\": 0, \"T8_chocolate_pudding\": 0.02, \"T9_orange_juice\": 0.04}, \"total_episodes\": 500, \"total_successes\": 13}, \"status\": \"DONE\"}, \"eval_smolvla_official_random_k050_object_seed43\": {\"status\": \"DONE\"}, \"eval_smolvla_official_l2norm_k095_object_seed43\": {\"status\": \"DONE\"}, \"eval_smolvla_official_random_k095_object_seed43\": {\"status\": \"DONE\"}, \"eval_smolvla_official_baseline_object_seed43\": {\"status\": \"DONE\"}, \"eval_smolvla_official_l2norm_k095_object_seed42\": {\"metrics\": {\"seed\": 42, \"success_rate\": 0.4, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_smolvla_official_random_k095_object_seed42\": {\"metrics\": {\"seed\": 42, \"success_rate\": 0, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_smolvla_official_baseline_object_seed42\": {\"metrics\": {\"note\": \"Official checkpoint, paper reports ~87% - significant gap\", \"seed\": 42, \"success_rate\": 57.2, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_object_seed43\": {\"metrics\": {\"seed\": 43, \"success_rate\": 39.2, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"train_openvla_sc_m64_seed42_v5\": {\"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_object_seed42_v2\": {\"metrics\": {\"seed\": 42, \"success_rate\": 98.2, \"total_episodes\": 500, \"total_successes\": 491}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k03_object_seed43\": {\"metrics\": {\"num_episodes\": 500, \"per_task\": {\"alphabet_soup\": 42, \"bbq_sauce\": 10, \"butter\": 8, \"chocolate_pudding\": 28, \"cream_cheese\": 6, \"ketchup\": 66, \"milk\": 36, \"orange_juice\": 26, \"salad_dressing\": 28, \"tomato_sauce\": 0}, \"success_rate\": 25}, \"status\": \"DONE\"}, \"eval_openvla_random_k07_object_seed43\": {\"metrics\": {\"elapsed_min\": 272.6, \"overall_sr\": 0.526, \"per_task\": {\"alphabet_soup\": 0.84, \"bbq_sauce\": 0.42, \"butter\": 0.1, \"chocolate_pudding\": 0.36, \"cream_cheese\": 0.2, \"ketchup\": 0.7, \"milk\": 0.6, \"orange_juice\": 0.84, \"salad_dressing\": 0.66, \"tomato_sauce\": 0.54}, \"total_episodes\": 500, \"total_successes\": 263}, \"status\": \"DONE\"}, \"eval_openvla_baseline_object_seed42\": {\"metrics\": {\"num_episodes\": 500, \"source\": \"log extraction - full eval completed but results/ dir missing caused save failure\", \"success_rate\": 74}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_object_seed44\": {\"metrics\": {}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_object_seed42_v2\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 65.2}, \"status\": \"DONE\"}, \"eval_xvla_random_k085_object_seed43\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 63.2}, \"status\": \"DONE\"}, \"eval_xvla_random_k085_object_seed42_v2\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 63.6}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_object_seed43\": {\"metrics\": {\"elapsed_min\": 100.3, \"success_rate\": 56.4, \"total_episodes\": 500, \"total_successes\": 282}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_object_seed42\": {\"metrics\": {\"elapsed_min\": 91.7, \"success_rate\": 55, \"total_episodes\": 500, \"total_successes\": 275}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_object_seed42_v2\": {\"status\": \"DONE\"}, \"eval_xvla_l2norm_k085_object_seed43\": {\"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_object_seed43\": {\"metrics\": {\"SR\": 0.21}, \"status\": \"DONE\"}, \"eval_xvla_random_k03_object_seed43\": {\"metrics\": {\"SR\": 0.662}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_object_seed44\": {\"metrics\": {\"SR\": 0.65}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_object_seed43\": {\"metrics\": {\"SR\": 0.59}, \"status\": \"DONE\"}, \"eval_xvla_random_k03_object_seed44\": {\"metrics\": {\"SR\": 0.63, \"per_task\": [0.74, 0.42, 0.96, 0.8, 0.88, 0.84, 0, 0.74, 0, 0.92]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_object_seed44\": {\"metrics\": {\"SR\": 0.564, \"per_task\": [0.96, 0, 1, 0.8, 0.26, 0.9, 0.12, 0.7, 0.02, 0.88]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_object_seed43_v2\": {\"metrics\": {\"SR\": 0.578, \"elapsed_min\": 91.34, \"per_task\": {\"alphabet_soup\": 0.46, \"bbq_sauce\": 0.8, \"butter\": 0.3, \"chocolate_pudding\": 0.7, \"cream_cheese\": 0.96, \"ketchup\": 0.26, \"milk\": 0.04, \"orange_juice\": 0.46, \"salad_dressing\": 0.8, \"tomato_sauce\": 1}, \"total_episodes\": 500, \"total_successes\": 289}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k03_object_seed42_rerun\": {\"metrics\": {\"SR\": 0.25, \"elapsed_minutes\": 299.2, \"per_task\": {\"alphabet_soup\": 0.42, \"bbq_sauce\": 0.1, \"butter\": 0.08, \"chocolate_pudding\": 0.28, \"cream_cheese\": 0.06, \"ketchup\": 0.66, \"milk\": 0.36, \"orange_juice\": 0.26, \"salad_dressing\": 0.28, \"tomato_sauce\": 0}, \"total_episodes\": 500, \"total_successes\": 125, \"vision_tokens\": \"256->76\"}, \"status\": \"DONE\"}, \"eval_openvla_random_k03_object_seed42_v2\": {\"metrics\": {\"elapsed_min\": 304.1, \"overall_SR\": 0.214, \"per_task\": {\"alphabet_soup\": 0.14, \"bbq_sauce\": 0.3, \"butter\": 0.02, \"chocolate_pudding\": 0.16, \"cream_cheese\": 0, \"ketchup\": 0.26, \"milk\": 0.14, \"orange_juice\": 0.56, \"salad_dressing\": 0.56, \"tomato_sauce\": 0}, \"seed\": 42}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_object_seed42_v3\": {\"status\": \"DONE\"}, \"eval_openvla_l2norm_k07_object_seed42_v2\": {\"metrics\": {\"overall_sr\": 0.498, \"total_episodes\": 500, \"total_successes\": 249}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_object_seed42\": {\"metrics\": {\"elapsed_min\": 83.1, \"overall_sr\": 0.772, \"total_episodes\": 500, \"total_successes\": 386}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_object_seed42\": {\"metrics\": {\"notes\": \"3 tasks at 0% SR (catastrophic). vs random k=0.3=62.8% → gap +40.6pp confirms D132.\", \"per_task\": [26, 0, 32, 40, 18, 46, 0, 24, 0, 36], \"success_rate\": 0.222, \"total_episodes\": 500, \"total_successes\": 111, \"wilson_ci_95\": [0.188, 0.26]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_object_seed42\": {\"metrics\": {\"notes\": \"D140: L2norm reversal at k=0.3 - L2norm > random for pi0.5\", \"success_rate\": 0.51, \"total_episodes\": 500, \"total_successes\": 255}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_object_seed42\": {\"metrics\": {\"success_rate\": 0.364, \"total_episodes\": 500, \"total_successes\": 182}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_object_seed44\": {\"metrics\": {\"notes\": \"3rd seed confirms D132: random k=0.5 seed42=70.6%, seed43=71.0%, seed44=69.2%\", \"success_rate\": 0.692, \"total_episodes\": 500, \"total_successes\": 346}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_object_seed42\": {\"metrics\": {\"comparison\": {\"baseline_sr\": 0.982, \"l2norm_k05_sr\": 0.334, \"random_vs_l2norm_gap\": \"+36.0pp\", \"retention_rate\": \"70.7%\"}, \"elapsed_min\": 94.9, \"overall_sr\": 0.694, \"per_task_sr\": {\"alphabet_soup\": 0.92, \"bbq_sauce\": 0.6, \"butter\": 0.88, \"chocolate_pudding\": 0.78, \"cream_cheese\": 0.78, \"ketchup\": 0.6, \"milk\": 0.54, \"orange_juice\": 0.58, \"salad_dressing\": 0.68, \"tomato_sauce\": 0.58}, \"total_episodes\": 500, \"total_successes\": 347}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_object_seed42_v2\": {\"metrics\": {\"notes\": \"Reviewer confirmed. westd-38929=56.2% vs cqa1=58.2%, 2pp diff acceptable.\", \"per_task\": [96, 2, 100, 78, 34, 90, 18, 0, 70, 94], \"success_rate\": 0.582, \"total_episodes\": 500, \"total_successes\": 291}, \"status\": \"DONE\"}, \"train_openvla_sc_m64_seed42_v4\": {\"metrics\": {\"note\": \"Previous run crashed at 50K. Current run restarted from 0.\", \"steps_completed\": \"from_step_0_restart\", \"steps_total\": 100000}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_object_seed43_v2\": {\"metrics\": {\"success_rate\": 0.65, \"total_episodes\": 500, \"total_successes\": 325, \"wilson_ci_95\": [0.6072, 0.6905]}, \"status\": \"DONE\"}, \"eval_openvla_sc_m128_object_seed42_v2\": {\"metrics\": {\"failure_reason\": \"7/7 episodes FAIL (280-step timeout), model output invalid after LoRA merge. Killed by Director.\"}, \"status\": \"DONE\"}, \"eval_openvla_random_k07_object_seed42\": {\"metrics\": {\"failure_reason\": \"Process never started — empty log, command failure on westd-38929\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_object_seed42\": {\"metrics\": {\"elapsed_minutes\": 95.6, \"keep_ratio\": 0.5, \"num_episodes\": 500, \"per_task\": {\"alphabet_soup\": 0.5, \"bbq_sauce\": 0.0, \"butter\": 0.28, \"chocolate_pudding\": 0.38, \"cream_cheese\": 0.14, \"ketchup\": 0.54, \"milk\": 0.64, \"orange_juice\": 0.48, \"salad_dressing\": 0.0, \"tomato_sauce\": 0.38}, \"seed\": 42, \"success_rate\": 33.4, \"total_successes\": 167}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_object_seed43\": {\"metrics\": {}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k03_object_seed42\": {\"metrics\": {\"failure_reason\": \"AutoDL container restart at 14:50:19 UTC killed process. Was at Task 4/10 (~40%). GPU count dropped from 4 to 1 after restart.\", \"k_ratio\": 0.3, \"note\": \"Prior complete result found on disk after container crash. Current run crashed at Task 4/10.\", \"success_rate\": 25.0}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_object_seed42\": {\"metrics\": {\"failure_reason\": \"AutoDL container restart at 14:50:19 UTC killed process. Was at Task 4/10 (~40%). GPU count dropped from 4 to 1 after restart.\", \"k_ratio\": 0.5, \"note\": \"Prior complete result found on disk after container crash. Current run crashed at Task 4/10.\", \"success_rate\": 39.2}, \"status\": \"DONE\"}, \"eval_openvla_random_k03_object_seed42\": {\"metrics\": {\"failure_reason\": \"AutoDL container restart at 14:50:19 UTC killed process. Was at Task 4/10 (~40%). GPU count dropped from 4 to 1 after restart.\"}, \"status\": \"DONE\"}, \"eval_xvla_random_k03_object_seed42\": {\"metrics\": {\"keep_ratio\": 0.3, \"success_rate\": 62.8}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_object_seed42\": {\"metrics\": {\"duration_min\": 77.3, \"num_episodes\": 500, \"per_task\": [0.98, 0.0, 1.0, 0.94, 0.62, 0.96, 0.1, 0.92, 0.0, 1.0], \"success_rate\": 65.2, \"wilson_ci_95\": [0.609, 0.692]}, \"status\": \"DONE\"}, \"eval_openvla_sc_m128_object_seed42\": {\"metrics\": {\"all_fail\": true, \"num_episodes_completed\": 16, \"success_rate\": 0.0}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k05_seed42\": {\"metrics\": {\"duration_min\": 291, \"num_episodes\": 500, \"per_task\": [0.56, 0.02, 0.4, 0.58, 0.6, 0.26, 0.0, 0.12, 0.3, 0.74], \"seed\": 42, \"success_rate\": 35.8, \"wilson_ci_95\": [0.317, 0.401]}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k07_seed42_v2\": {\"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 44.4}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k095_seed42_v2\": {\"metrics\": {\"num_episodes\": 500, \"per_task\": [0.8, 0.42, 0.7, 0.42, 0.88, 0.84, 0.6, 0.68, 0.66, 0.92], \"seed\": 42, \"success_rate\": 69.2, \"wilson_ci_95\": [0.65, 0.731]}, \"status\": \"DONE\"}, \"eval_smolvla_baseline_spatial_westd38929_seed42\": {\"metrics\": {\"note\": \"OffScreenRenderEnv - not comparable with LiberoEnv results\", \"num_episodes\": 500, \"per_task\": [0.24, 0.08, 0.04, 0.24, 0.0, 0.02, 0.02, 0.02, 0.14, 0.0], \"success_rate\": 8.0, \"wilson_ci_95\": [0.059, 0.107]}, \"status\": \"DONE\"}, \"eval_xvla_random_k08_object_seed42\": {\"metrics\": {\"num_episodes\": 500, \"per_task\": [0.96, 0.88, 1.0, 0.92, 0.94, 0.96, 0.5, 0.94, 0.84, 1.0], \"success_rate\": 89.4, \"wilson_ci_95\": [0.864, 0.918]}, \"status\": \"DONE\"}, \"eval_xvla_random_k09_object_seed42\": {\"metrics\": {\"duration_min\": 50.4, \"num_episodes\": 500, \"per_task\": [0.96, 1.0, 1.0, 0.94, 1.0, 0.94, 1.0, 0.98, 0.96, 1.0], \"success_rate\": 97.8, \"wilson_ci_95\": [0.961, 0.988]}, \"status\": \"DONE\"}, \"eval_oft_baseline_goal_seed42\": {\"status\": \"PREPARING\"}, \"eval_oft_object_std_v3\": {\"status\": \"PREPARING\"}, \"eval_oft_object_nolora_v2\": {\"status\": \"PREPARING\"}, \"eval_xvla_spatial_k085_seed42\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 66.6}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k07_seed43_v2\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 49.8, \"wilson_ci_95\": [0.455, 0.541]}, \"status\": \"DONE\"}, \"eval_oft_baseline_object_seed42\": {\"status\": \"DONE\"}, \"train_openvla_sc_m64_seed42_v3\": {\"status\": \"DONE\"}, \"eval_openvla_sc_m64_50k_seed42\": {\"status\": \"PREPARING\"}, \"openvla-spatial-maxsteps600-quick\": {\"status\": \"PREPARING\"}, \"openvla-spatial-maxsteps600-test\": {\"status\": \"PREPARING\"}, \"eval_openvla_baseline_spatial_seed42_v2\": {\"status\": \"DONE\"}, \"eval_xvla_goal_k05_seed42\": {\"metrics\": {\"num_episodes\": 500, \"per_task\": [0.82, 0.98, 1.0, 0.4, 1.0, 0.0, 0.24, 0.74, 0.92, 0.0], \"seed\": 42, \"success_rate\": 0.61, \"suite\": \"libero_goal\", \"wilson_ci_95\": [0.567, 0.652]}, \"status\": \"DONE\"}, \"eval_xvla_goal_k09_seed42\": {\"metrics\": {\"num_episodes\": 500, \"per_task\": [1.0, 0.82, 0.96, 0.06, 0.96, 0.0, 0.78, 1.0, 0.46, 0.98], \"seed\": 42, \"success_rate\": 0.702, \"suite\": \"libero_goal\", \"wilson_ci_95\": [0.66, 0.74]}, \"status\": \"DONE\"}, \"eval_xvla_spatial_k09_seed42\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.79, \"wilson_ci_95\": [0.752, 0.823]}, \"status\": \"DONE\"}, \"eval_openvla_sc_m128_spatial_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_prune_random_k03_seed43\": {\"status\": \"DONE\"}, \"eval_openvla_prune_random_k07_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_prune_random_k095_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k09_seed43\": {\"status\": \"DONE\"}, \"eval_xvla_spatial_k05_seed42\": {\"metrics\": {\"num_episodes\": 500, \"per_task\": [0.94, 0.22, 0.9, 0.74, 0.88, 0.0, 0.78, 0.3, 0.74, 0.38], \"success_rate\": 0.588, \"wilson_ci_95\": [0.544, 0.63]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k085_seed44\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.682, \"wilson_ci_95\": [0.64, 0.721]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k08_seed44\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.898, \"total_successes\": 449, \"wilson_ci_95\": [0.868, 0.922]}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k095_seed43\": {\"metrics\": {\"elapsed_minutes\": 249.43, \"k_ratio\": 0.95, \"mode\": \"random_prune\", \"num_episodes\": 500, \"seed\": 43, \"success_rate\": 0.668, \"total_successes\": 334, \"wilson_ci_95\": [0.626, 0.708]}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k07_seed43\": {\"metrics\": {\"elapsed_minutes\": 237.8, \"num_episodes\": 500, \"per_task\": {\"alphabet_soup\": 0.78, \"bbq_sauce\": 0.46, \"butter\": 0.58, \"chocolate_pudding\": 0.68, \"cream_cheese\": 0.8, \"ketchup\": 0.96, \"milk\": 0.72, \"orange_juice\": 0.82, \"salad_dressing\": 0.82, \"tomato_sauce\": 0.78}, \"seed\": 43, \"success_rate\": 0.74, \"total_successes\": 370, \"wilson_ci_95\": [0.7, 0.777]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k08_seed42\": {\"metrics\": {\"keep_ratio\": 0.8, \"n_vision_tokens_kept\": 40, \"n_vision_tokens_original\": 50, \"num_episodes\": 500, \"success_rate\": 0.888, \"wilson_ci_95\": [0.8573, 0.9127]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k085_seed43\": {\"metrics\": {\"keep_ratio\": 0.85, \"n_vision_tokens_kept\": 42, \"n_vision_tokens_original\": 50, \"num_episodes\": 500, \"success_rate\": 0.676, \"wilson_ci_95\": [0.6338, 0.7155]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k085_seed42\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.68, \"wilson_ci_95\": [0.638, 0.719]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k08_seed43\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.884, \"wilson_ci_95\": [0.853, 0.909]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k01_seed42\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0, \"wilson_ci_95\": [0, 0.008]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k095_seed43\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.99, \"wilson_ci_95\": [0.9768, 0.9957]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k095_seed44\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.994, \"wilson_ci_95\": [0.983, 0.998]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k095_seed42\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.99, \"wilson_ci_95\": [0.977, 0.996]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k01_seed44\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0, \"wilson_ci_95\": [0, 0.008]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k01_seed43\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k09_seed42\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.646, \"total_successes\": 323, \"wilson_ci_95\": [0.604, 0.686]}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k09_seed43\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.622}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k05_seed43_v2\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.356}, \"status\": \"DONE\"}, \"eval_xvla_prune_k02_seed44\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.04}, \"status\": \"DONE\"}, \"eval_xvla_prune_k02_seed43\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.048}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k09\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.706}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k07_seed43_v2\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.526}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k095\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.706}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k03\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.25}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k05\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.392}, \"status\": \"DONE\"}, \"eval_xvla_prune_k03_seed43\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.21}, \"status\": \"DONE\"}, \"eval_xvla_prune_k03_seed44\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.228}, \"status\": \"DONE\"}, \"eval_xvla_prune_k05_seed44\": {\"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.444}, \"status\": \"DONE\"}, \"eval_xvla_prune_k07_seed44\": {\"metrics\": {\"episodes\": 500, \"success_rate\": 0.564}, \"status\": \"DONE\"}, \"eval_xvla_prune_k09_seed44\": {\"metrics\": {\"episodes\": 500, \"success_rate\": 0.982}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k05_seed43\": {\"status\": \"DONE\"}, \"eval_openvla_prune_random_k07_seed43\": {\"status\": \"DONE\"}, \"eval_openvla_prune_seed43_sweep\": {\"status\": \"PREPARING\"}, \"eval_oft_baseline_k10\": {\"status\": \"DONE\"}, \"eval_openvla_sc_m128_20k_seed42\": {\"metrics\": {\"episodes_completed\": 44, \"episodes_total\": 50, \"note\": \"0/44 episodes succeeded on Task 0. All episodes timeout at 280 steps. Overfitting confirmed.\", \"seed\": 42, \"suite\": \"libero_object\", \"task_0_sr\": 0}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_sweep\": {\"status\": \"PREPARING\"}, \"eval_smart_compress_m16_seed44\": {\"metrics\": {\"n_episodes\": 500, \"n_queries\": 16, \"overall_sr\": 0.565, \"per_task_sr\": {\"task_0_alphabet_soup\": 0.38, \"task_1_cream_cheese\": 0.7, \"task_2_salad_dressing\": 0.55, \"task_3_bbq_sauce\": 0.42, \"task_4_ketchup\": 0.65, \"task_5_tomato_sauce\": 0.33, \"task_6_butter\": 0.73, \"task_7_milk\": 0.64, \"task_8_chocolate_pudding\": 0.87, \"task_9_orange_juice\": 0.38}, \"seed\": 44, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"analysis_smolvla_importance_cv\": {\"metrics\": {\"entropy_ratio\": 0.952, \"importance_cv\": 0.314, \"importance_cv_std\": 0.015, \"importance_gini\": 0.156}, \"status\": \"PREPARING\"}, \"eval_smart_compress_m16_seed43\": {\"metrics\": {\"n_queries\": 16, \"overall_sr\": 0.584, \"per_task_sr\": {\"task_0_alphabet_soup\": 0.428, \"task_1_cream_cheese\": 0.474, \"task_2_salad_dressing\": 0.662, \"task_3_bbq_sauce\": 0.484, \"task_4_ketchup\": 0.742, \"task_5_tomato_sauce\": 0.4, \"task_6_butter\": 0.792, \"task_7_milk\": 0.698, \"task_8_chocolate_pudding\": 0.766, \"task_9_orange_juice\": 0.394}, \"seed\": 43, \"suite\": \"libero_object\", \"wilson_ci_95\": [0.5703, 0.5976]}, \"status\": \"DONE\"}, \"eval_smart_compress_m128_seed43\": {\"metrics\": {\"n_queries\": 128, \"overall_sr\": 0.54, \"per_task_sr\": {\"task_0_alphabet_soup\": 0.646, \"task_1_cream_cheese\": 0.322, \"task_2_salad_dressing\": 0.614, \"task_3_bbq_sauce\": 0.432, \"task_4_ketchup\": 0.348, \"task_5_tomato_sauce\": 0.442, \"task_6_butter\": 0.716, \"task_7_milk\": 0.604, \"task_8_chocolate_pudding\": 0.818, \"task_9_orange_juice\": 0.458}, \"seed\": 43, \"suite\": \"libero_object\", \"wilson_ci_95\": [0.5262, 0.5538]}, \"status\": \"DONE\"}, \"train_openvla_sc_m128_vtconly_seed42\": {\"status\": \"DONE\"}, \"eval_openvla_sc_m128_vtconly_20k_seed42\": {\"status\": \"DONE\"}, \"analysis_pi0_token_importance\": {\"metrics\": {\"entropy_ratio\": 0.9999, \"importance_cv\": 0.038, \"importance_gini\": 0.009, \"k01_norm_loss\": 0.976, \"k05_norm_loss\": 0.983, \"k09_norm_loss\": 0.993, \"suffix_vis_entropy_mean\": 0.959}, \"status\": \"PREPARING\"}, \"train_openvla_sc_m128_seed42_v2\": {\"status\": \"DONE\"}, \"train_openvla_sc_m64_seed42\": {\"status\": \"PREPARING\"}, \"analysis_xvla_token_importance\": {\"status\": \"DONE\"}, \"train_openvla_sc_m96_vtconly_seed42\": {\"status\": \"DONE\"}, \"train_openvla_sc_m64_vtconly_seed42\": {\"status\": \"DONE\"}, \"train_c5_roboflamingo_v2\": {\"status\": \"DONE\"}, \"train_c5_roboflamingo_libero_object\": {\"status\": \"DONE\"}, \"train_openvla_sc_m128_lora_seed42\": {\"status\": \"DONE\"}, \"eval_smart_compress_m32_seed44\": {\"metrics\": {\"ci_95_lower\": 55.2, \"ci_95_upper\": 63.8, \"n_episodes\": 500, \"seed\": 44, \"success_rate\": 59.6}, \"status\": \"DONE\"}, \"eval_smart_compress_m96_seed44\": {\"metrics\": {\"ci_95_lower\": 48.4, \"ci_95_upper\": 57.1, \"n_episodes\": 500, \"seed\": 44, \"success_rate\": 52.8}, \"status\": \"DONE\"}, \"eval_smart_compress_m64_seed44\": {\"metrics\": {\"ci_95_lower\": 60.1, \"ci_95_upper\": 68.5, \"n_episodes\": 500, \"seed\": 44, \"success_rate\": 64.4}, \"status\": \"DONE\"}, \"eval_openvla_random_pruning_sweep\": {\"metrics\": {\"k0.30_sr\": 20.6, \"k0.50_sr\": 37.4, \"k0.70_sr\": 49, \"k0.90_sr\": 62, \"k0.95_sr\": 69.4, \"k1.0_sr\": 74, \"n_episodes\": 500, \"seed\": 7, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"c5_roboflamingo_libero_object\": {\"status\": \"PREPARING\"}, \"c5-roboflamingo-libero-baseline\": {\"status\": \"PREPARING\"}, \"train_openvla_sc_m128_seed42\": {\"status\": \"DONE\"}, \"train_smart_compress_m16_seed44_v2\": {\"metrics\": {\"failure_reason\": \"Disk full on /root/autodl-tmp/ (250G/250G, 100% used, 4MB free). Training ran normally to step=1000 (loss 5.0→0.2), but torch.save() failed at first checkpoint save with PytorchStreamWriter write error. Checkpoints dir already 112GB from prior experiments — needs cleanup before retry. Partial checkpoint.pt (228MB) likely corrupted.\", \"last_loss\": 0.207, \"last_step\": 1000, \"steps_per_second\": 3.8}, \"status\": \"DONE\"}, \"eval_official_smolvla_prune_k05_spatial_v2\": {\"metrics\": {\"note\": \"cliff-edge confirmed on Spatial suite, 0.6% SR with k=0.5 random pruning\", \"overall_success_rate\": 0.006, \"total_episodes\": 500, \"total_successes\": 3}, \"status\": \"DONE\"}, \"eval_smart_compress_m96_seed44_v2\": {\"metrics\": {\"overall_success_rate\": 0.528, \"total_episodes\": 500, \"total_successes\": 264, \"wilson_ci_95\": [0.4842, 0.5714]}, \"status\": \"DONE\"}, \"eval_smart_compress_m64_seed44_v2\": {\"metrics\": {\"overall_success_rate\": 0.644, \"total_episodes\": 500, \"total_successes\": 322, \"wilson_ci_95\": [0.6011, 0.6847]}, \"status\": \"DONE\"}, \"eval_smart_compress_m32_seed44_v2\": {\"metrics\": {\"overall_success_rate\": 0.596, \"total_episodes\": 500, \"total_successes\": 298, \"wilson_ci_95\": [0.5524, 0.6381]}, \"status\": \"DONE\"}, \"eval_mlp_adapter_seed44\": {\"metrics\": {\"overall_success_rate\": 0.604, \"per_task_sr\": {\"0_alphabet_soup\": 0.54, \"1_cream_cheese\": 0.68, \"2_salad_dressing\": 0.58, \"3_bbq_sauce\": 0.5, \"4_ketchup\": 0.8, \"5_tomato_sauce\": 0.58, \"6_butter\": 0.82, \"7_milk\": 0.58, \"8_chocolate_pudding\": 0.54, \"9_orange_juice\": 0.42}, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 302, \"wilson_ci_95\": [0.5605, 0.6459]}, \"status\": \"DONE\"}, \"eval_official_smolvla_prune_k05_spatial\": {\"status\": \"DONE\"}, \"eval_smolvla_official_baseline_spatial_v2\": {\"metrics\": {\"overall_success_rate\": 0.438, \"per_task_sr\": {\"task_0\": 0.54, \"task_1\": 0.48, \"task_2\": 0.08, \"task_3\": 0.76, \"task_4\": 0.38, \"task_5\": 0.2, \"task_6\": 0.34, \"task_7\": 0.78, \"task_8\": 0.48, \"task_9\": 0.34}, \"total_episodes\": 500, \"total_successes\": 219, \"wilson_ci_95\": [0.3951, 0.4818]}, \"status\": \"DONE\"}, \"eval_mlp_adapter_seed43\": {\"metrics\": {\"overall_success_rate\": 0.646, \"per_task_sr\": {\"task0_alphabet_soup\": 0.74, \"task1_cream_cheese\": 0.74, \"task2_salad_dressing\": 0.66, \"task3_bbq_sauce\": 0.44, \"task4_ketchup\": 0.56, \"task5_tomato_sauce\": 0.64, \"task6_butter\": 0.86, \"task7_milk\": 0.58, \"task8_chocolate_pudding\": 0.72, \"task9_orange_juice\": 0.52}, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 323, \"wilson_ci_95\": [0.603, 0.687]}, \"status\": \"DONE\"}, \"eval_mlp_adapter_control\": {\"metrics\": {\"overall_success_rate\": 0.652, \"per_task_sr\": {\"task0_alphabet_soup\": 0.58, \"task1_cream_cheese\": 0.74, \"task2_salad_dressing\": 0.72, \"task3_bbq_sauce\": 0.56, \"task4_ketchup\": 0.76, \"task5_tomato_sauce\": 0.68, \"task6_butter\": 0.8, \"task7_milk\": 0.62, \"task8_chocolate_pudding\": 0.52, \"task9_orange_juice\": 0.54}, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 326, \"wilson_ci_95\": [0.6092, 0.6925]}, \"status\": \"DONE\"}, \"eval_smolvla_prune_k05_spatial_v2\": {\"metrics\": {\"episodes_per_task\": 50, \"k_ratio\": 0.5, \"num_tasks\": 10, \"overall_success_rate\": 0, \"per_task_sr\": {\"T0\": 0, \"T1\": 0, \"T2\": 0, \"T3\": 0, \"T4\": 0, \"T5\": 0, \"T6\": 0, \"T7\": 0, \"T8\": 0, \"T9\": 0}, \"pruning_method\": \"true_removal\", \"tokens_kept\": 64, \"tokens_removed\": 64, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_baseline_spatial\": {\"metrics\": {\"overall_success_rate\": 0.062, \"total_episodes\": 500, \"total_successes\": 31}, \"status\": \"DONE\"}, \"eval_smolvla_official_baseline_spatial\": {\"status\": \"DONE\"}, \"eval_smolvla_prune_k05_spatial\": {\"status\": \"DONE\"}, \"train_smart_compress_m16_seed44\": {\"status\": \"DONE\"}, \"train_mlp_adapter_control\": {\"status\": \"DONE\"}, \"eval_smart_compress_m32_spatial\": {\"status\": \"DONE\"}, \"eval_smart_compress_m128_seed44\": {\"metrics\": {\"overall_success_rate\": 0.602, \"per_task_sr\": {\"alphabet_soup\": 0.54, \"bbq_sauce\": 0.5, \"butter\": 0.66, \"chocolate_pudding\": 0.88, \"cream_cheese\": 0.3, \"ketchup\": 0.86, \"milk\": 0.72, \"orange_juice\": 0.54, \"salad_dressing\": 0.62, \"tomato_sauce\": 0.4}, \"total_episodes\": 500, \"total_successes\": 301, \"wilson_ci_95\": [0.5585, 0.644]}, \"status\": \"DONE\"}, \"train_smart_compress_m32_official\": {\"status\": \"DONE\"}, \"train_smart_compress_m128_seed44\": {\"status\": \"DONE\"}, \"eval_openvla_prune_k095\": {\"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [76, 38, 84, 54, 84, 82, 46, 74, 64, 92], \"success_rate\": 69.4, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_openvla_prune_k09\": {\"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [70, 28, 76, 56, 78, 70, 42, 60, 54, 86], \"success_rate\": 62, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_smart_compress_m32_seed43\": {\"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [72, 38, 68, 36, 68, 48, 86, 44, 96, 36], \"success_rate\": 59.2, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_smart_compress_m32_libero_spatial\": {\"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [58, 62, 52, 82, 28, 18, 82, 70, 56, 24], \"success_rate\": 53.2, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"eval_smart_compress_m64_seed43\": {\"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [58, 56, 46, 50, 48, 58, 80, 60, 86, 58], \"success_rate\": 60, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_smart_compress_m32_libero_goal\": {\"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [60, 94, 62, 52, 32, 28, 28, 100, 78, 30], \"success_rate\": 56.4, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_baseline_control_prune_k05\": {\"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"success_rate\": 0, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"train_smart_compress_m64_seed43\": {\"status\": \"DONE\"}, \"train_smart_compress_m32_seed43\": {\"status\": \"DONE\"}, \"eval_smart_compress_m96_seed43_v2\": {\"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [72, 66, 54, 48, 52, 40, 88, 60, 86, 16], \"success_rate\": 58.2, \"suite\": \"libero_object\", \"wilson_ci_95\": [53.8, 62.4]}, \"status\": \"DONE\"}, \"eval_smart_compress_m96_seed43\": {\"metrics\": {\"note\": \"INVALID — used wrong eval script (eval_success_rate_libero.py --mode baseline, no compressor loaded). Re-eval as eval_smart_compress_m96_seed43_v2.\", \"num_episodes\": 500, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"success_rate\": 0, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"train_smart_compress_m96_seed43\": {\"status\": \"DONE\"}, \"train_baseline_control_100k_v2\": {\"status\": \"DONE\"}, \"eval_baseline_control_100k_v2\": {\"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [0, 50, 74, 64, 68, 8, 58, 38, 52, 38], \"success_rate\": 45, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_official_smolvla_prune_k095\": {\"metrics\": {\"note\": \"Official SmolVLA checkpoint k=0.95 random pruning (true_removal, remove 5% = 7 tokens) = 0% SR. All 500 episodes timeout at 280 steps.\", \"overall_sr\": 0, \"per_task_sr\": {\"all_10_tasks\": \"0%\"}, \"total_episodes\": 500, \"total_successes\": 0}, \"status\": \"DONE\"}, \"eval_official_smolvla_prune_k09\": {\"metrics\": {\"note\": \"Official SmolVLA checkpoint k=0.9 random pruning (true_removal, remove 10% tokens) = 0% SR. All 500 episodes timeout at 280 steps.\", \"overall_sr\": 0, \"per_task_sr\": {\"all_10_tasks\": \"0%\"}, \"total_episodes\": 500, \"total_successes\": 0}, \"status\": \"DONE\"}, \"eval_acis_k05_supplement_v2\": {\"metrics\": {\"note\": \"Fixed eval script with offset-based ACIS hook confirms 0% SR. Previous 47.5% was due to pruning hook bug (never applied pruning).\", \"overall_SR\": \"0.0% (0/200)\", \"task6_SR\": \"0% (0/50)\", \"task7_SR\": \"0% (0/50)\", \"task8_SR\": \"0% (0/50)\", \"task9_SR\": \"0% (0/50)\", \"wilson_ci_95\": \"[0.0%, 1.9%]\"}, \"status\": \"DONE\"}, \"eval_acis_k05_supplement_200eps\": {\"metrics\": {\"overall_SR\": \"47.5% (95/200)\", \"task6_SR\": \"48% (24/50)\", \"task7_SR\": \"40% (20/50)\", \"task8_SR\": \"64% (32/50)\", \"task9_SR\": \"38% (19/50)\", \"wilson_ci_95\": \"[40.7%, 54.4%]\"}, \"status\": \"DONE\"}, \"eval_official_smolvla_prune_k05_v2\": {\"metrics\": {\"note\": \"Official SmolVLA checkpoint with k=0.5 random pruning = 0% SR, confirming cliff-edge on official checkpoint (59.2% baseline → 0%)\", \"overall_sr\": 0, \"per_task_sr\": {\"all_tasks\": \"0%\"}, \"total_episodes\": 500, \"total_successes\": 0}, \"status\": \"DONE\"}, \"eval_official_smolvla_baseline\": {\"metrics\": {\"overall_sr\": 59.2, \"per_task_sr\": {\"task_0_alphabet_soup\": 64, \"task_1_cream_cheese\": 40, \"task_2_salad_dressing\": 44, \"task_3_bbq_sauce\": 38, \"task_4_ketchup\": 60, \"task_5_tomato_sauce\": 46, \"task_6_butter\": 78, \"task_7_milk\": 52, \"task_8_chocolate_pudding\": 90, \"task_9_orange_juice\": 80}, \"total_episodes\": 500, \"total_successes\": 296, \"wilson_ci_95\": [54.8, 63.4]}, \"status\": \"DONE\"}, \"eval_smolvla_random_prune_k095\": {\"metrics\": {\"k_ratio\": 0.95, \"overall_SR\": 0, \"per_task_SR\": {\"T0_alphabet_soup\": 0, \"T1_cream_cheese\": 0, \"T2_salad_dressing\": 0, \"T3_bbq_sauce\": 0, \"T4_ketchup\": 0, \"T5_tomato_sauce\": 0, \"T6_butter\": 0, \"T7_milk\": 0, \"T8_chocolate_pudding\": 0, \"T9_orange_juice\": 0}, \"tokens_kept\": 121, \"tokens_removed\": 7, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_official_smolvla_pruning\": {\"status\": \"DONE\"}, \"debug_obs_official\": {\"status\": \"PREPARING\"}, \"eval_official_smolvla_prune_k05\": {\"status\": \"PREPARING\"}, \"train_baseline_control_100k\": {\"status\": \"DONE\"}, \"eval_smart_compress_m128\": {\"metrics\": {\"libero_object_sr\": 0.598, \"libero_object_sr_ci95\": [0.554, 0.64], \"per_task_sr\": {\"alphabet_soup\": 0.62, \"bbq_sauce\": 0.34, \"butter\": 0.82, \"chocolate_pudding\": 0.82, \"cream_cheese\": 0.58, \"ketchup\": 0.62, \"milk\": 0.56, \"orange_juice\": 0.58, \"salad_dressing\": 0.54, \"tomato_sauce\": 0.5}, \"total_episodes\": 500, \"total_successes\": 299}, \"status\": \"DONE\"}, \"eval_openvla_pruning_k03_restart\": {\"metrics\": {\"elapsed_minutes\": 288.6, \"overall_sr\": 0.206, \"per_task_sr\": {\"alphabet_soup\": 0.14, \"bbq_sauce\": 0.3, \"butter\": 0, \"chocolate_pudding\": 0.1, \"cream_cheese\": 0, \"ketchup\": 0.3, \"milk\": 0.08, \"orange_juice\": 0.42, \"salad_dressing\": 0.64, \"tomato_sauce\": 0.08}, \"total_episodes\": 500, \"total_successes\": 103, \"wilson_ci_95\": [0.173, 0.244]}, \"status\": \"DONE\"}, \"smolvla_entropy_perlayer\": {\"metrics\": {\"dataset\": \"LIBERO-Object (task 20-29)\", \"entropy_range\": [0.9311, 0.9826], \"entropy_range_width\": 0.05, \"n_images\": 260, \"n_layers\": 16, \"n_tasks\": 10, \"note\": \"Fixed: previous run sampled task 0-8 (LIBERO-90), not LIBERO-Object. Difference: 0.952 vs 0.944, conclusion unchanged.\", \"openvla_comparison\": {\"overall\": 0.639, \"range_width\": 0.5}, \"overall_entropy_ratio\": 0.9521, \"overall_entropy_std\": 0.02, \"per_layer\": {\"L0\": 0.9826, \"L1\": 0.9561, \"L10\": 0.9455, \"L11\": 0.951, \"L12\": 0.9485, \"L13\": 0.9311, \"L14\": 0.9482, \"L15\": 0.9566, \"L2\": 0.9597, \"L3\": 0.9434, \"L4\": 0.9408, \"L5\": 0.9406, \"L6\": 0.9474, \"L7\": 0.9628, \"L8\": 0.9614, \"L9\": 0.9572}}, \"status\": \"DONE\"}, \"inference_latency_comparison\": {\"metrics\": {\"baseline_128_mean_ms\": 164.33, \"baseline_params\": 450046176, \"compressor_m32_params\": 22179840, \"m32_mean_ms\": 154.78, \"m64_mean_ms\": 156.16, \"speedup_m32\": 1.0617, \"speedup_m64\": 1.0523}, \"status\": \"DONE\"}, \"eval_openvla_pruning_k03\": {\"status\": \"DONE\"}, \"openvla_entropy_real\": {\"metrics\": {\"deep_layers_27_30\": [0.542, 0.53, 0.477, 0.524], \"max_entropy_layer\": {\"layer\": 0, \"ratio\": 0.979}, \"min_entropy_layer\": {\"layer\": 29, \"ratio\": 0.4774}, \"n_images\": 250, \"n_tasks\": 10, \"overall_entropy_ratio\": 0.6393, \"overall_entropy_std\": 0.1334, \"overall_vision_attn_frac\": 0.1211, \"previous_random_N20\": 0.617, \"shallow_layers_0_1\": [0.979, 0.952], \"smolvla_reference\": 0.98}, \"status\": \"DONE\"}, \"train_smart_compress_m128\": {\"status\": \"DONE\"}, \"eval_smart_compress_m96\": {\"metrics\": {\"overall_sr\": 52.6, \"per_task_sr\": {\"task_0_alphabet_soup\": 40, \"task_1_cream_cheese\": 52, \"task_2_salad_dressing\": 56, \"task_3_bbq_sauce\": 40, \"task_4_ketchup\": 26, \"task_5_tomato_sauce\": 50, \"task_6_butter\": 72, \"task_7_milk\": 62, \"task_8_chocolate_pudding\": 86, \"task_9_orange_juice\": 42}, \"total_episodes\": 500, \"total_successes\": 263, \"wilson_ci_95\": [48.2, 56.9]}, \"status\": \"DONE\"}, \"eval_smart_compress_m16\": {\"metrics\": {\"overall_sr\": 55.8, \"overall_sr_ci95\": [51.4, 60.1], \"per_task_sr\": {\"task_0_alphabet_soup\": 56, \"task_1_cream_cheese\": 44, \"task_2_salad_dressing\": 72, \"task_3_bbq_sauce\": 56, \"task_4_ketchup\": 62, \"task_5_tomato_sauce\": 40, \"task_6_butter\": 78, \"task_7_milk\": 54, \"task_8_chocolate_pudding\": 76, \"task_9_orange_juice\": 20}, \"runtime_minutes\": 55, \"total_episodes\": 500, \"total_successes\": 279}, \"status\": \"DONE\"}, \"eval_openvla_pruning_k07\": {\"metrics\": {\"elapsed_minutes\": 260.7, \"overall_sr\": 0.49, \"per_task_sr\": {\"alphabet_soup\": 0.74, \"bbq_sauce\": 0.46, \"butter\": 0.1, \"chocolate_pudding\": 0.32, \"cream_cheese\": 0.18, \"ketchup\": 0.68, \"milk\": 0.4, \"orange_juice\": 0.76, \"salad_dressing\": 0.64, \"tomato_sauce\": 0.62}, \"total_episodes\": 500, \"total_successes\": 245}, \"status\": \"DONE\"}, \"train_smart_compress_m96\": {\"metrics\": {\"eval_action_loss\": 0.064, \"total_steps\": 100000, \"train_action_loss\": 0.055}, \"status\": \"DONE\"}, \"smart_compress_m16\": {\"metrics\": {\"eval_action_loss\": 0.069, \"total_steps\": 100000, \"train_action_loss\": 0.058}, \"status\": \"DONE\"}, \"eval_smart_compress_m64\": {\"metrics\": {\"overall_sr\": 0.616, \"per_task_sr\": {\"alphabet_soup\": 0.74, \"bbq_sauce\": 0.56, \"butter\": 0.84, \"chocolate_pudding\": 0.74, \"cream_cheese\": 0.38, \"ketchup\": 0.64, \"milk\": 0.62, \"orange_juice\": 0.46, \"salad_dressing\": 0.64, \"tomato_sauce\": 0.54}, \"total_episodes\": 500, \"total_successes\": 308, \"wilson_ci_95\": [0.573, 0.658]}, \"status\": \"DONE\"}, \"eval_smart_compress_m32\": {\"metrics\": {\"overall_sr\": 0.616, \"per_task_sr\": {\"alphabet_soup\": 0.68, \"bbq_sauce\": 0.46, \"butter\": 0.82, \"chocolate_pudding\": 0.9, \"cream_cheese\": 0.64, \"ketchup\": 0.66, \"milk\": 0.76, \"orange_juice\": 0.28, \"salad_dressing\": 0.6, \"tomato_sauce\": 0.36}, \"total_episodes\": 500, \"total_successes\": 308, \"wilson_ci_95\": [0.573, 0.658]}, \"status\": \"DONE\"}, \"train_smart_compress_m32\": {\"metrics\": {\"checkpoint\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"checkpoint_size_gb\": 1.5, \"eval_action_loss\": 0.052, \"speed_sps\": 4.1, \"total_steps\": 100000, \"train_action_loss\": 0.11, \"training_duration_h\": 6.5}, \"status\": \"DONE\"}, \"train_smart_compress_m64\": {\"metrics\": {\"checkpoint\": \"checkpoints/smart_compress_m64/checkpoint.pt\", \"checkpoint_size_gb\": 1.5, \"eval_action_loss\": 0.062, \"speed_sps\": 4.1, \"total_steps\": 100000, \"train_action_loss\": 0.045, \"training_duration_h\": 6.5}, \"status\": \"DONE\"}, \"libero_full_ft_baseline\": {\"metrics\": {\"diversity_10k\": {\"noise_diversity_std\": 0.1987, \"pass\": true, \"per_obs\": [0.193, 0.192, 0.203, 0.193, 0.213], \"threshold\": 0.05}, \"sr_100k_goal\": {\"n_episodes\": 100, \"overall\": 0.63, \"per_task\": [0.5, 0.9, 0.7, 0.3, 1, 0.4, 0.4, 1, 0.8, 0.3], \"suite\": \"libero_goal\"}, \"sr_100k_object\": {\"n_episodes\": 100, \"overall\": 0.36, \"per_task\": [0, 0.3, 0.4, 0.6, 0.5, 0.1, 0.3, 0.5, 0.4, 0.5], \"suite\": \"libero_object\"}, \"sr_100k_overall\": 0.49, \"sr_100k_spatial\": {\"n_episodes\": 100, \"overall\": 0.48, \"per_task\": [0.8, 0.5, 0.4, 0.4, 0.3, 0.3, 0.6, 0.2, 0.9, 0.4], \"suite\": \"libero_spatial\"}, \"sr_50k\": {\"n_episodes\": 100, \"overall\": 0.33, \"per_task\": [0.1, 0.7, 0.5, 0.1, 0.3, 0.1, 0.5, 0.1, 0.4, 0.5], \"suite\": \"libero_object\", \"wilson_ci_95\": [0.246, 0.427]}, \"sr_50k_goal\": {\"n_episodes\": 100, \"overall\": 0.42, \"per_task\": [0.2, 0.7, 0.5, 0.1, 0.6, 0.5, 0.2, 0.8, 0.5, 0.1], \"suite\": \"libero_goal\", \"wilson_ci_95\": [0.328, 0.518]}, \"sr_50k_spatial\": {\"n_episodes\": 100, \"overall\": 0.34, \"per_task\": [0.8, 0.1, 0.3, 0.2, 0.2, 0.4, 0.3, 0.2, 0.6, 0.3], \"suite\": \"libero_spatial\", \"wilson_ci_95\": [0.255, 0.437]}}, \"status\": \"DONE\"}, \"train_acis_stage1only_k03\": {\"status\": \"DONE\"}, \"eval_openvla_pruning_k05\": {\"status\": \"DONE\"}, \"geometric_prior_k05_eval\": {\"status\": \"DONE\"}, \"eval_openvla_crossmodel_pruning\": {\"status\": \"DONE\"}, \"eval_geometric_prior_k09\": {\"status\": \"DONE\"}, \"eval_geometric_prior_k07\": {\"status\": \"DONE\"}, \"eval_geometric_prior_k05\": {\"status\": \"DONE\"}, \"libero_fullft_batch64_v2\": {\"status\": \"DONE\"}, \"baseline_bypass_object\": {\"metrics\": {\"checkpoint_matches_object_eval\": true, \"k_ratio\": 1, \"mode\": \"bypass\", \"overall_sr\": 0.448, \"per_task_sr\": [0.22, 0.6, 0.42, 0.38, 0.58, 0.26, 0.62, 0.38, 0.5, 0.52], \"total_episodes\": 500, \"total_successes\": 224, \"wilson_ci_95\": [0.405, 0.492]}, \"status\": \"DONE\"}, \"action_divergence_v2_clean\": {\"metrics\": {\"action_l2_mean\": 1.117, \"action_l2_median\": 0.85, \"bypass_early_terminations\": \"multiple\", \"divergence_onset_step\": 0, \"eef_position_l2_mean_m\": 0.214, \"eef_position_l2_median_m\": 0.214, \"first_10_steps_action_l2\": 1.262, \"first_10_steps_eef_l2_m\": 0.041, \"last_10_steps_action_l2\": 0.759, \"last_10_steps_eef_l2_m\": 0.198, \"max_steps\": 300, \"n_episodes_per_task\": 10, \"n_tasks\": 3, \"pattern\": \"immediate_onset_monotonic_growth\", \"pruned_early_terminations\": 0}, \"status\": \"DONE\"}, \"eval_goal_prune_k05\": {\"metrics\": {\"all_tasks_zero\": true, \"baseline_sr\": 0.63, \"k_ratio\": 0.5, \"mode\": \"acis_prune\", \"overall_sr\": 0, \"pruning_method\": \"true_removal\", \"sr_drop\": -0.63, \"suite\": \"libero_goal\", \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"offline_singlestep_action_error\": {\"metrics\": {\"bypass_vs_gt_l2_mean\": 0.414, \"bypass_vs_pruned_l2_mean\": 1.284, \"conclusion_type\": \"large_per_step_error\", \"interpretation\": \"Pruning directly destroys action prediction at each step. Not a compounding issue.\", \"n_steps\": 200, \"per_dim_gripper\": 1.02, \"per_dim_position_xyz\": [0.2, 0.25, 0.3], \"per_dim_rotation_xyz\": [0.01, 0.02, 0.01], \"pruned_vs_gt_l2_mean\": 1.391, \"relative_error_pct\": 111.5}, \"status\": \"DONE\"}, \"offline_singlestep_error_k05\": {\"status\": \"DONE\"}, \"eval_spatial_prune_k05\": {\"metrics\": {\"all_tasks_zero\": true, \"baseline_sr\": 0.518, \"mode\": \"acis_prune\", \"overall_sr\": 0, \"pruning_method\": \"true_removal\", \"sr_drop\": -0.518, \"suite\": \"libero_spatial\", \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_merge_k05\": {\"metrics\": {\"episodes\": 500, \"k_ratio\": 0.5, \"libero_object_sr\": 0, \"merge_alpha\": 1, \"pruning_method\": \"merge\", \"pruning_type\": \"acis\", \"wilson_ci_95\": \"[0.0%, 0.76%]\"}, \"status\": \"DONE\"}, \"eval_k07_zero_mask\": {\"metrics\": {\"episodes\": 500, \"k_ratio\": 0.7, \"libero_object_sr\": 0, \"pruning_method\": \"zero_mask\", \"pruning_type\": \"acis\", \"wilson_ci_95\": \"[0.0%, 0.76%]\"}, \"status\": \"DONE\"}, \"eval_true_removal_k05\": {\"metrics\": {\"episodes\": 500, \"k_ratio\": 0.5, \"libero_object_sr\": 0, \"pruning_method\": \"true_removal\", \"pruning_type\": \"acis\", \"wilson_ci_95\": \"[0.0%, 0.8%]\"}, \"status\": \"DONE\"}, \"eval_stage1only_k09\": {\"metrics\": {\"episodes\": 500, \"k_ratio\": 0.9, \"libero_object_sr\": 0, \"pruning_method\": \"zero_mask\", \"pruning_type\": \"acis\"}, \"status\": \"DONE\"}, \"eval_random_prune_k05\": {\"metrics\": {\"episodes\": 500, \"k_ratio\": 0.5, \"libero_object_sr\": 0, \"pruning_method\": \"zero_mask\", \"pruning_type\": \"random\"}, \"status\": \"DONE\"}, \"train_acis_stage1only_k07\": {\"status\": \"DONE\"}, \"eval_stage1only_object_v2_fixed\": {\"metrics\": {\"k_ratio\": 0.5, \"mode\": \"acis_prune\", \"note\": \"Fixed pruning (offset-tracking). Pruning actually executed this time. 0% SR confirms ACIS importance scoring is ineffective for closed-loop control after Stage1-only training.\", \"overall_success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0], \"total_episodes\": 300, \"total_successes\": 0}, \"status\": \"DONE\"}, \"eval_stage1only_spatial\": {\"status\": \"DONE\"}, \"eval_stage1_only\": {\"metrics\": {\"k_ratio\": 0.5, \"mode\": \"acis_prune\", \"overall_success_rate\": 0.448, \"per_task_sr\": [0.22, 0.6, 0.42, 0.38, 0.58, 0.26, 0.62, 0.38, 0.5, 0.52], \"total_episodes\": 500, \"total_successes\": 224, \"wilson_ci_95\": [0.405, 0.4918]}, \"status\": \"DONE\"}, \"sanity_acis_prune\": {\"status\": \"PREPARING\"}, \"libero_fullft_seed1\": {\"metrics\": {\"eval_action_loss\": 0.05404, \"total_steps\": 100000, \"train_action_loss\": 0.04282, \"train_grad_norm\": 1.17539}, \"status\": \"DONE\"}, \"libero_fullft_batch64\": {\"status\": \"DONE\"}, \"eval_random_prune_baseline\": {\"status\": \"PREPARING\"}, \"eval_imm100k_bypass\": {\"metrics\": {\"mode\": \"baseline_bypass\", \"note\": \"Stage2 completely destroyed expert weights\", \"overall_success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_k07_bypass_v3\": {\"metrics\": {\"mode\": \"baseline_bypass\", \"note\": \"Stage2 k=0.7 also completely destroyed expert weights\", \"overall_success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_k07_bypass_v2\": {\"status\": \"DONE\"}, \"eval_k07_bypass\": {\"status\": \"PREPARING\"}, \"eval_imm_k07_object\": {\"metrics\": {\"overall_success_rate\": 0.048, \"per_task_sr\": [0, 0, 0.06, 0.02, 0.32, 0.06, 0.02, 0, 0, 0], \"total_episodes\": 500, \"total_successes\": 24, \"wilson_ci_95\": [0.0325, 0.0704]}, \"status\": \"DONE\"}, \"mvp_imm_anchor_v7_2\": {\"metrics\": {\"bypass_acis\": {\"clean_action_loss\": 0.0078, \"conclusion\": \"weights_damaged\", \"g3_ratio\": 1.91}, \"eval_500batch_soft\": {\"clean_action_loss\": 0.013, \"clean_margin_median\": 0.6627, \"clean_preservation\": 1, \"eps001_led_median\": 0.162, \"eps001_preservation\": 0.9253, \"eps002_led_median\": 0.3232, \"eps002_preservation\": 0.8482, \"eps005_led_median\": 0.7656, \"eps005_preservation\": 0.6597, \"lipschitz_empirical\": 0.3393, \"lipschitz_spectral\": 1.0672}, \"gate_v7_2\": {\"G1_margin_ratio\": 64.25, \"G1_pass\": true, \"G2_pass\": true, \"G2_preservation_diff_pp\": 47.46, \"G3_action_loss_ratio\": 3.19, \"G3_pass\": false, \"G4_led_median\": 0.323, \"G4_pass\": true, \"overall\": \"FAIL\"}, \"source\": \"eval_results/eval_imm_v7_2_final.json + eval_results/eval_imm_v7_2_bypass_acis.json\"}, \"status\": \"DONE\"}, \"mvp_imm_anchor_v7\": {\"metrics\": {\"eval_500batch\": {\"clean_action_loss\": 0.0134, \"clean_margin_median\": 0.5743, \"clean_preservation\": 1, \"eps001_led_median\": 0.1341, \"eps001_preservation\": 0.9124, \"eps002_led_median\": 0.2726, \"eps002_preservation\": 0.8172, \"eps005_led_median\": 0.69, \"eps005_preservation\": 0.6079, \"lipschitz_empirical\": 0.2493, \"lipschitz_spectral\": 1.0672}, \"source\": \"eval_results/eval_imm_v7_final.json\"}, \"status\": \"DONE\"}, \"libero_fullft_seed0\": {\"status\": \"DONE\"}, \"libero_imm_fullft_k07\": {\"status\": \"DONE\"}, \"libero_imm_fullft_seed0\": {\"status\": \"DONE\"}, \"libero_imm_fullft_100k\": {\"status\": \"DONE\"}, \"libero_imm_fullft_v2\": {\"metrics\": {\"sr_object\": {\"n_episodes\": 100, \"note\": \"IMM two-stage on 50K FT checkpoint, Object suite eval. 15.4% vs baseline 44.8% (-66% relative)\", \"overall\": 0.154, \"source\": \"imm_v2_fullft_libero_object.json\", \"suite\": \"libero_object\"}}, \"status\": \"DONE\"}, \"libero_lora_seed0\": {\"status\": \"DONE\"}, \"libero_lora_baseline\": {\"metrics\": {\"diversity_10k\": {\"noise_diversity_std\": 0.1736, \"pass\": true, \"per_obs\": [0.166, 0.177, 0.154, 0.198, 0.174], \"threshold\": 0.05}, \"sr_100k\": {\"all_episodes_hit_max_steps\": true, \"eval_running\": true, \"max_steps\": 400, \"n_episodes_completed\": 10, \"n_episodes_total\": 100, \"note\": \"task_0 complete 0/10, remaining tasks 1-9 still evaluating but pattern is conclusive\", \"overall\": 0, \"suite\": \"libero_object\", \"task_0_episodes\": 10, \"task_0_sr\": 0}, \"sr_50k\": {\"lora_keys_loaded\": 74, \"missing_keys\": 0, \"n_episodes\": 50, \"overall\": 0, \"per_task\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"suite\": \"libero_object\", \"unexpected_keys\": 0, \"verdict\": \"CORRECT_LOAD_confirmed_0pct_SR\", \"verified\": true}, \"training_100k\": {\"checkpoint_size_mb\": 883, \"completed_normally\": true, \"final_eval_loss\": 0.08041, \"final_grad_norm\": 0.415, \"final_lr\": 2.5e-06, \"final_step\": 99999, \"final_train_loss\": 0.0648}}, \"status\": \"DONE\"}, \"libero_imm_twostage_v1\": {\"status\": \"DONE\"}, \"plan_009_token_importance\": {\"metrics\": {\"action_loss_mean\": 0.0195, \"gradient_ratio_retained_over_pruned\": 1.7027, \"n_samples\": 100, \"n_vis_tokens\": 64, \"pruned_grad_mean\": 0.000183, \"retained_grad_mean\": 0.000311, \"spearman_corr_mean\": 0.4069, \"spearman_corr_median\": 0.4065, \"spearman_corr_std\": 0.1022}, \"status\": \"DONE\"}, \"plan_011_acis_overhead\": {\"metrics\": {\"flops_acis_increment_M\": 409.75, \"flops_baseline_G\": 169.87, \"flops_overhead_pct\": 0.24, \"latency_acis_increment_ms\": 0.32, \"latency_baseline_ms\": 51.16, \"latency_overhead_pct\": 0.63, \"n_trials\": 100, \"params_acis_increment_M\": 3.46, \"params_baseline_M\": 451.53, \"params_overhead_pct\": 0.77, \"source\": \"results/acis_overhead.json\"}, \"status\": \"DONE\"}, \"plan_008_pruning_sweep_v2\": {\"metrics\": {\"G3_best\": 0.237, \"G3_best_k\": 0.6, \"G3_k05\": 0.24, \"improvement_pct\": 76.2, \"source\": \"eval_results/pruning_sweep_v2.json\", \"sweet_spot\": \"k=0.5-0.6\"}, \"status\": \"DONE\"}, \"plan_005_formal_bound_v2\": {\"metrics\": {\"L_empirical\": 0.193, \"L_spectral\": 1.067, \"margin_median\": 0.96, \"source\": \"results/formal_bound_plan005.json\", \"stability_eps01\": 0.976, \"tightness_spectral_max\": 1.125, \"tightness_spectral_min\": 1.005}, \"status\": \"DONE\"}, \"plan_008_pruning_sweep\": {\"status\": \"DONE\"}, \"plan_005_formal_bound\": {\"status\": \"PREPARING\"}, \"baseline_v6_alpha16\": {\"metrics\": {\"mode_collapse_test\": {\"checkpoint\": \"checkpoints/baseline_v6_alpha16/step_029999/checkpoint.pt\", \"comparison_alpha64\": \"alpha64 std=0.006, alpha16 std=0.007 — no meaningful improvement\", \"cross_obs_std\": 0.096329, \"noise_diversity_std\": 0.007352, \"pretrained_noise_std\": null, \"threshold_fail\": 0.01, \"threshold_pass\": 0.05, \"verdict\": \"FAIL\"}}, \"status\": \"DONE\"}, \"mvp_imm_v8c_annealing\": {\"metrics\": {\"G1_margin_ratio\": 108.15, \"G2_preservation_diff\": 60.92, \"G3_deploy\": 2.04, \"G4_LED\": 0.1046, \"action_loss_acis_prune\": null, \"action_loss_baseline\": null, \"final_action_loss\": 0.0023, \"final_margin_loss\": 0.0938, \"final_train_loss\": 0.0492}, \"status\": \"DONE\"}, \"eval_sim_success_rate\": {\"status\": \"PREPARING\"}, \"mvp_imm_v8b_twostage\": {\"metrics\": {\"sim_success_rate\": {\"acis_prune\": 0, \"acis_prune_mean_reward\": 0, \"baseline\": 0, \"baseline_mean_reward\": 0.16, \"bypass\": 0, \"bypass_mean_reward\": 0, \"n_episodes\": 50, \"wilson_ci_95_upper\": 0.0714}}, \"status\": \"DONE\"}, \"mvp_imm_anchor_v8_1\": {\"status\": \"DONE\"}, \"imm_two_stage_v9\": {\"status\": \"PREPARING\"}, \"mvp_imm_anchor_v8\": {\"metrics\": {\"baseline_v5_fixed\": {\"clean_action_loss\": 0.004063, \"eps001_preservation\": 0.3352, \"margin_median\": 0.010022, \"source\": \"eval_results/eval_baseline_v5_fixed.json\"}, \"checkpoint_trajectory\": {\"step_2000\": {\"acis_advantage\": 0.0068, \"acis_prune\": 0.0357, \"bypass\": 0.05842, \"random_prune\": 0.0425, \"standard\": 0.03787}, \"step_29999\": {\"acis_advantage\": 0.01246, \"acis_prune\": 0.0033, \"bypass\": 0.0323, \"random_prune\": 0.01576, \"standard\": 0.00659}}, \"eval_500batch_bypass_fixed\": {\"bypass_clean_action_loss\": 0.028948, \"bypass_pruned_action_loss\": 0.017215, \"eps001_action_loss_noprune\": 0.027873, \"eps001_action_loss_prune\": 0.016572, \"eps005_action_loss_noprune\": 0.039901, \"eps005_action_loss_prune\": 0.02627, \"source\": \"eval_results/eval_imm_v8_bypass_fixed.json\"}, \"eval_500batch_fixed\": {\"bypass_clean_action_loss\": 0.028948, \"eps001_kendall_tau\": 0.8393, \"eps001_led_median\": 0.0852, \"eps001_preservation\": 0.923, \"eps002_led_median\": 0.1714, \"eps002_preservation\": 0.8367, \"eps005_led_median\": 0.4429, \"eps005_preservation\": 0.6613, \"eval_tag\": \"D028_fix_reeval\", \"lipschitz_empirical\": 0.1364, \"lipschitz_spectral\": 1.0672, \"margin_mean\": 0.7696, \"margin_median\": 0.5034, \"margin_std\": 0.8133, \"pruneFalse_clean_action_loss\": 0.029996, \"pruneTrue_clean_action_loss\": 0.005462, \"source\": \"eval_results/eval_imm_v8_fixed.json\", \"standard_clean_action_loss\": 0.005462}, \"gate_analysis_fixed\": {\"G1_margin_ratio\": 50.2, \"G1_pass\": true, \"G2_pass\": true, \"G2_preservation_diff_pp\": 58.78, \"G3_clean_loss_ratio\": 1.344, \"G3_deploy_pass\": false, \"G3_deploy_ratio\": 1.344, \"G3_pass\": false, \"G3_target\": 1.1, \"G4_led_median\": 0.0865, \"G4_pass\": true, \"bypass_backbone_ratio\": 7.12, \"eval_tag\": \"D028_fix_reeval\", \"notes\": \"Fixed eval (5 bugs: eps0 pruning flag, hard binary mask, per-condition RNG, eval mode, preloaded batches). Results consistent with old buggy eval within ~5%. G3 still fails at 1.344x.\", \"overall_pass\": false}}, \"status\": \"DONE\"}, \"mvp_baseline_v5\": {\"metrics\": {\"eval_500batch\": {\"clean_action_loss\": 0.004077, \"clean_margin_median\": 0.010022, \"eps001_preservation\": 0.3352, \"eps002_preservation\": 0.3362, \"eps005_preservation\": 0.3381}, \"mid_checkpoints\": {\"step005000\": {\"clean_action_loss\": 0.01891, \"clean_margin_mean\": 0.01608, \"clean_margin_median\": 0.01002, \"clean_pruned_action_loss\": 0.08304, \"eps001_action_loss\": 0.02234, \"eps001_kendall_tau\": -0.2315, \"eps001_preservation\": 0.3359, \"eps001_pruned_action_loss\": 0.08645, \"eps002_action_loss\": 0.02057, \"eps002_preservation\": 0.3369, \"eps002_pruned_action_loss\": 0.0882, \"eps005_action_loss\": 0.03377, \"eps005_preservation\": 0.34, \"eps005_pruned_action_loss\": 0.0912, \"lipschitz_empirical\": 0, \"lipschitz_spectral\": 0, \"source\": \"eval_results/eval_baseline_v5_step5000.json\"}, \"step010000\": {\"clean_action_loss\": 0.00974, \"clean_margin_mean\": 0.01608, \"clean_margin_median\": 0.01002, \"clean_pruned_action_loss\": 0.09434, \"eps001_action_loss\": 0.01243, \"eps001_kendall_tau\": -0.2315, \"eps001_preservation\": 0.3359, \"eps001_pruned_action_loss\": 0.09473, \"eps002_action_loss\": 0.01092, \"eps002_preservation\": 0.3369, \"eps002_pruned_action_loss\": 0.10085, \"eps005_action_loss\": 0.02565, \"eps005_preservation\": 0.34, \"eps005_pruned_action_loss\": 0.10132, \"lipschitz_empirical\": 0, \"lipschitz_spectral\": 0, \"source\": \"eval_results/eval_baseline_v5_step10000.json\"}}, \"source\": \"eval_results/eval_baseline_v5_final.json\"}, \"status\": \"DONE\"}, \"mvp_imm_anchor_v7_1\": {\"status\": \"DONE\"}, \"mvp_imm_anchor_v6\": {\"status\": \"DONE\"}, \"mvp_imm_anchor_v5\": {\"status\": \"DONE\"}, \"mvp_baseline_v4\": {\"status\": \"DONE\"}, \"mvp_imm_anchor_v4\": {\"status\": \"DONE\"}, \"mvp_baseline_v3\": {\"status\": \"DONE\"}, \"mvp_imm_anchor_v2\": {\"status\": \"DONE\"}, \"mvp_baseline_v2\": {\"status\": \"DONE\"}, \"mvp_imm_anchor\": {\"status\": \"DONE\"}, \"mvp_baseline\": {\"status\": \"DONE\"}, \"eval_oft_baseline_object_seed42_v2\": {\"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k03_seed42\": {\"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.25, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k05_seed42\": {\"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.392, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k095_seed42\": {\"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.706, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k09_seed42\": {\"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.706, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}}, \"count\": 867, \"total\": 867, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.5077}}"
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
The registry is too large. Let me search for specific experiments instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "3eb212dc-9e66-48c0-9f5e-ed14e0e3bc09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018aeoMiY171TA7FFRL5V8dT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2574,
      "cache_read_input_tokens": 47246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2574
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

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01TKe9iRFZK6jxzN8BTYc6Lq`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/77f0b2fb-f038-4bff-bd48-3bed171e3c77/tool-results/mcp-agent-ml-research-read_registry-1779862613590.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find all OpenVLA Object experiments\nobject_exps = {k: v for k, v in exps.items() if 'object' in k.lower() and 'openvla' in k.lower()}\nfor k, v in sorted(object_exps.items()):\n    sr = v.get('metrics', {}).get('overall_sr', '?')\n    print(f'{v[\\\"status\\\"]:8s} SR={sr!s:>6s}  {k}')\nprint()\n# Find all OpenVLA Long experiments  \nlong_exps = {k: v for k, v in exps.items() if 'long' in k.lower() and 'openvla' in k.lower()}\nfor k, v in sorted(long_exps.items()):\n    sr = v.get('metrics', {}).get('overall_sr', '?')\n    print(f'{v[\\\"status\\\"]:8s} SR={sr!s:>6s}  {k}')\nprint()\n# Find all OpenVLA Goal experiments\ngoal_exps = {k: v for k, v in exps.items() if 'goal' in k.lower() and 'openvla' in k.lower()}\nfor k, v in sorted(goal_exps.items()):\n    sr = v.get('metrics', {}).get('overall_sr', '?')\n    print(f'{v[\\\"status\\\"]:8s} SR={sr!s:>6s}  {k}')\n\"\n",
  "description": "Parse registry for OpenVLA experiment gaps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "f4b8371a-5a38-457e-b4d5-dbccadce27c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018aeoMiY171TA7FFRL5V8dT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2574,
      "cache_read_input_tokens": 47246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2574
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

_source line 54 · 2026-05-27T06:17:02.448Z_

<details><summary>↩ Tool result · `toolu_01TKe9iRFZK6jxzN8BTYc6Lq`</summary>

```text
DEPLOYED SR=     ?  eval_openvla_attn_k05_object_seed42
DONE     SR=     ?  eval_openvla_attn_k05_object_seed42_v2
DONE     SR=  53.2  eval_openvla_attn_k075_object_seed42
DONE     SR=     ?  eval_openvla_attn_k07_object_seed42
DONE     SR=     ?  eval_openvla_attn_k07_object_seed42_v2
DONE     SR=  43.8  eval_openvla_attn_k07_object_seed42_v3
DONE     SR=     ?  eval_openvla_attn_k085_object_seed42
DONE     SR=  71.2  eval_openvla_attn_k095_object_seed42
DONE     SR=     ?  eval_openvla_attn_k09_object_seed42
DONE     SR=     ?  eval_openvla_attn_k09_object_seed42_v3
DONE     SR=     ?  eval_openvla_baseline_object_seed42
DONE     SR=  0.74  eval_openvla_baseline_object_seed42_v2
DONE     SR=     ?  eval_openvla_l2norm_k03_object_seed42
DONE     SR=     ?  eval_openvla_l2norm_k03_object_seed42_rerun
DONE     SR=     ?  eval_openvla_l2norm_k03_object_seed43
DONE     SR=     ?  eval_openvla_l2norm_k05_object_seed42
DONE     SR=     ?  eval_openvla_l2norm_k05_object_seed42_v2
DONE     SR=     ?  eval_openvla_l2norm_k05_object_seed42_v3
DONE     SR=     ?  eval_openvla_l2norm_k05_object_seed42_v4
DONE     SR=     ?  eval_openvla_l2norm_k05_object_seed42_v5
DONE     SR=     ?  eval_openvla_l2norm_k05_object_seed43
DONE     SR= 0.574  eval_openvla_l2norm_k075_object_seed42
DEPLOYED SR=     ?  eval_openvla_l2norm_k07_object_seed42
DONE     SR= 0.498  eval_openvla_l2norm_k07_object_seed42_v2
DONE     SR= 0.498  eval_openvla_l2norm_k07_object_seed42_v3
PREPARING SR=     ?  eval_openvla_l2norm_k085_object_seed42
RUNNING  SR=     ?  eval_openvla_l2norm_k095_object_seed42
DONE     SR= 0.706  eval_openvla_l2norm_k09_object_seed42
DONE     SR=     ?  eval_openvla_random_k03_object_seed42
DONE     SR=     ?  eval_openvla_random_k03_object_seed42_v2
DONE     SR=     ?  eval_openvla_random_k05_object_seed42
DONE     SR=     ?  eval_openvla_random_k05_object_seed42_v2
DONE     SR=  35.8  eval_openvla_random_k05_object_seed42_v3
DONE     SR=  50.4  eval_openvla_random_k075_object_seed42
DONE     SR=     ?  eval_openvla_random_k07_object_seed42
DONE     SR= 0.444  eval_openvla_random_k07_object_seed42_v2
DONE     SR=     ?  eval_openvla_random_k07_object_seed42_v3
DONE     SR= 0.526  eval_openvla_random_k07_object_seed43
DONE     SR=     ?  eval_openvla_random_k085_object_seed42
PREPARING SR=     ?  eval_openvla_random_k085_object_seed42_v2
DONE     SR=  67.4  eval_openvla_random_k095_object_seed42
DONE     SR=     ?  eval_openvla_random_k09_object_seed42
DONE     SR=     ?  eval_openvla_sc_m128_object_seed42
DONE     SR=     ?  eval_openvla_sc_m128_object_seed42_v2
DONE     SR=     ?  eval_openvla_zeromask_l2norm_k09_object_seed42
DONE     SR= 0.718  eval_openvla_zeromask_random_k09_object_seed42

DONE     SR=  14.6  eval_openvla_attn_k05_long_seed42
DONE     SR=  37.4  eval_openvla_attn_k075_long_seed42
DONE     SR=     ?  eval_openvla_attn_k07_long_seed42
DONE     SR=     ?  eval_openvla_attn_k07_long_seed42_v2
DONE     SR=     ?  eval_openvla_attn_k085_long_seed42
DONE     SR=     ?  eval_openvla_attn_k085_long_seed42_v2
DONE     SR=  45.8  eval_openvla_attn_k085_long_seed42_v3
DONE     SR=     ?  eval_openvla_attn_k085_long_seed42_v4
DONE     SR=  45.8  eval_openvla_attn_k085_long_seed42_v5
RUNNING  SR=     ?  eval_openvla_attn_k095_long_seed42
DONE     SR=     ?  eval_openvla_attn_k09_long_seed42
DONE     SR=     ?  eval_openvla_attn_k09_long_seed42_v2
DONE     SR=  44.0  eval_openvla_attn_k09_long_seed42_v3
DONE     SR= 0.528  eval_openvla_baseline_long_seed42
DONE     SR=     ?  eval_openvla_l2norm_k05_long_seed42
DONE     SR=     ?  eval_openvla_l2norm_k075_long_seed42
RUNNING  SR=     ?  eval_openvla_l2norm_k075_long_seed42_v2
DONE     SR=     ?  eval_openvla_l2norm_k07_long_seed42
DONE     SR= 0.312  eval_openvla_l2norm_k07_long_seed42_v2
DONE     SR=     ?  eval_openvla_l2norm_k085_long_seed42
DONE     SR= 0.388  eval_openvla_l2norm_k085_long_seed42_v2
RUNNING  SR=     ?  eval_openvla_l2norm_k095_long_seed42
DONE     SR=     ?  eval_openvla_l2norm_k09_long_seed42
DONE     SR=     ?  eval_openvla_l2norm_k09_long_seed42_v2
DONE     SR=  43.6  eval_openvla_l2norm_k09_long_seed42_v3
DONE     SR=     ?  eval_openvla_random_k05_long_seed42
DONE     SR=  18.6  eval_openvla_random_k05_long_seed42_v2
DONE     SR=     ?  eval_openvla_random_k075_long_seed42
DONE     SR=     ?  eval_openvla_random_k07_long_seed42
DONE     SR= 0.388  eval_openvla_random_k07_long_seed42_v2
DONE     SR=     ?  eval_openvla_random_k085_long_seed42
PREPARING SR=     ?  eval_openvla_random_k085_long_seed42_v2
DONE     SR=  0.45  eval_openvla_random_k085_long_seed42_v3
RUNNING  SR=     ?  eval_openvla_random_k095_long_seed42
PREPARING SR=     ?  eval_openvla_random_k095_long_seed42_v2
DONE     SR=     ?  eval_openvla_random_k09_long_seed42
DONE     SR=     ?  eval_openvla_random_k09_long_seed42_v2
DONE     SR=  46.8  eval_openvla_random_k09_long_seed42_v3

DONE     SR=  44.2  eval_openvla_attn_k05_goal_seed42
DONE     SR=     ?  eval_openvla_attn_k05_goal_seed42_v2
RUNNING  SR=     ?  eval_openvla_attn_k05_goal_seed42_v3
DONE     SR=  67.4  eval_openvla_attn_k075_goal_seed42
DONE     SR=     ?  eval_openvla_attn_k075_goal_seed42_v2
DONE     SR= 0.664  eval_openvla_attn_k07_goal_seed42
DONE     SR=     ?  eval_openvla_attn_k085_goal_seed42
DONE     SR=     ?  eval_openvla_attn_k085_goal_seed42_v2
DONE     SR=  74.6  eval_openvla_attn_k085_goal_seed42_v3
DONE     SR=     ?  eval_openvla_attn_k095_goal_seed42
RUNNING  SR=     ?  eval_openvla_attn_k095_goal_seed42_v2
PREPARING SR=     ?  eval_openvla_attn_k095_goal_seed42_v3
DONE     SR= 0.732  eval_openvla_attn_k09_goal_seed42
DONE     SR=     ?  eval_openvla_attn_k09_goal_seed43
DONE     SR=     ?  eval_openvla_attn_k09_goal_seed43_v2
PREPARING SR=     ?  eval_openvla_attn_k09_goal_seed43_v3
DONE     SR=  73.2  eval_openvla_attn_k09_goal_seed43_v4
PREPARING SR=     ?  eval_openvla_baseline_goal_seed42
PREPARING SR=     ?  eval_openvla_baseline_goal_seed42_v2
DONE     SR=     ?  eval_openvla_baseline_goal_seed42_v3
DONE     SR= 0.776  eval_openvla_baseline_goal_seed43
DONE     SR= 0.434  eval_openvla_l2norm_k05_goal_seed42
DONE     SR=     ?  eval_openvla_l2norm_k05_goal_seed42_v2
DONE     SR= 0.434  eval_openvla_l2norm_k05_goal_seed42_v3
DONE     SR=     ?  eval_openvla_l2norm_k075_goal_seed42
DONE     SR=  70.2  eval_openvla_l2norm_k075_goal_seed42_v2
DONE     SR= 0.684  eval_openvla_l2norm_k07_goal_seed42
DONE     SR=  75.4  eval_openvla_l2norm_k085_goal_seed42
DONE     SR=  75.2  eval_openvla_l2norm_k095_goal_seed42
DONE     SR= 0.748  eval_openvla_l2norm_k09_goal_seed42
DONE     SR=  75.2  eval_openvla_l2norm_k09_goal_seed43
DONE     SR=     ?  eval_openvla_l2norm_k09_goal_seed43_v2
DONE     SR= 0.752  eval_openvla_l2norm_k09_goal_seed43_v3
DONE     SR= 0.522  eval_openvla_random_k05_goal_seed42
DONE     SR= 0.522  eval_openvla_random_k05_goal_seed42_v2
DONE     SR=    72  eval_openvla_random_k075_goal_seed42
DONE     SR=     ?  eval_openvla_random_k07_goal_seed42
DONE     SR=     ?  eval_openvla_random_k07_goal_seed42_v2
PREPARING SR=     ?  eval_openvla_random_k07_goal_seed42_v3
DONE     SR=  68.4  eval_openvla_random_k07_goal_seed42_v4
DONE     SR=  78.6  eval_openvla_random_k085_goal_seed42
DONE     SR=     ?  eval_openvla_random_k095_goal_seed42
RUNNING  SR=     ?  eval_openvla_random_k095_goal_seed42_v2
DONE     SR=  79.6  eval_openvla_random_k09_goal_seed42
DONE     SR=     ?  eval_openvla_random_k09_goal_seed42_v2
DONE     SR=  80.4  eval_openvla_random_k09_goal_seed43
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "4c18d4d1-605d-4ed5-9c9f-b6c9b98dae78",
  "tool_use_result": {
    "stdout": "DEPLOYED SR=     ?  eval_openvla_attn_k05_object_seed42\nDONE     SR=     ?  eval_openvla_attn_k05_object_seed42_v2\nDONE     SR=  53.2  eval_openvla_attn_k075_object_seed42\nDONE     SR=     ?  eval_openvla_attn_k07_object_seed42\nDONE     SR=     ?  eval_openvla_attn_k07_object_seed42_v2\nDONE     SR=  43.8  eval_openvla_attn_k07_object_seed42_v3\nDONE     SR=     ?  eval_openvla_attn_k085_object_seed42\nDONE     SR=  71.2  eval_openvla_attn_k095_object_seed42\nDONE     SR=     ?  eval_openvla_attn_k09_object_seed42\nDONE     SR=     ?  eval_openvla_attn_k09_object_seed42_v3\nDONE     SR=     ?  eval_openvla_baseline_object_seed42\nDONE     SR=  0.74  eval_openvla_baseline_object_seed42_v2\nDONE     SR=     ?  eval_openvla_l2norm_k03_object_seed42\nDONE     SR=     ?  eval_openvla_l2norm_k03_object_seed42_rerun\nDONE     SR=     ?  eval_openvla_l2norm_k03_object_seed43\nDONE     SR=     ?  eval_openvla_l2norm_k05_object_seed42\nDONE     SR=     ?  eval_openvla_l2norm_k05_object_seed42_v2\nDONE     SR=     ?  eval_openvla_l2norm_k05_object_seed42_v3\nDONE     SR=     ?  eval_openvla_l2norm_k05_object_seed42_v4\nDONE     SR=     ?  eval_openvla_l2norm_k05_object_seed42_v5\nDONE     SR=     ?  eval_openvla_l2norm_k05_object_seed43\nDONE     SR= 0.574  eval_openvla_l2norm_k075_object_seed42\nDEPLOYED SR=     ?  eval_openvla_l2norm_k07_object_seed42\nDONE     SR= 0.498  eval_openvla_l2norm_k07_object_seed42_v2\nDONE     SR= 0.498  eval_openvla_l2norm_k07_object_seed42_v3\nPREPARING SR=     ?  eval_openvla_l2norm_k085_object_seed42\nRUNNING  SR=     ?  eval_openvla_l2norm_k095_object_seed42\nDONE     SR= 0.706  eval_openvla_l2norm_k09_object_seed42\nDONE     SR=     ?  eval_openvla_random_k03_object_seed42\nDONE     SR=     ?  eval_openvla_random_k03_object_seed42_v2\nDONE     SR=     ?  eval_openvla_random_k05_object_seed42\nDONE     SR=     ?  eval_openvla_random_k05_object_seed42_v2\nDONE     SR=  35.8  eval_openvla_random_k05_object_seed42_v3\nDONE     SR=  50.4  eval_openvla_random_k075_object_seed42\nDONE     SR=     ?  eval_openvla_random_k07_object_seed42\nDONE     SR= 0.444  eval_openvla_random_k07_object_seed42_v2\nDONE     SR=     ?  eval_openvla_random_k07_object_seed42_v3\nDONE     SR= 0.526  eval_openvla_random_k07_object_seed43\nDONE     SR=     ?  eval_openvla_random_k085_object_seed42\nPREPARING SR=     ?  eval_openvla_random_k085_object_seed42_v2\nDONE     SR=  67.4  eval_openvla_random_k095_object_seed42\nDONE     SR=     ?  eval_openvla_random_k09_object_seed42\nDONE     SR=     ?  eval_openvla_sc_m128_object_seed42\nDONE     SR=     ?  eval_openvla_sc_m128_object_seed42_v2\nDONE     SR=     ?  eval_openvla_zeromask_l2norm_k09_object_seed42\nDONE     SR= 0.718  eval_openvla_zeromask_random_k09_object_seed42\n\nDONE     SR=  14.6  eval_openvla_attn_k05_long_seed42\nDONE     SR=  37.4  eval_openvla_attn_k075_long_seed42\nDONE     SR=     ?  eval_openvla_attn_k07_long_seed42\nDONE     SR=     ?  eval_openvla_attn_k07_long_seed42_v2\nDONE     SR=     ?  eval_openvla_attn_k085_long_seed42\nDONE     SR=     ?  eval_openvla_attn_k085_long_seed42_v2\nDONE     SR=  45.8  eval_openvla_attn_k085_long_seed42_v3\nDONE     SR=     ?  eval_openvla_attn_k085_long_seed42_v4\nDONE     SR=  45.8  eval_openvla_attn_k085_long_seed42_v5\nRUNNING  SR=     ?  eval_openvla_attn_k095_long_seed42\nDONE     SR=     ?  eval_openvla_attn_k09_long_seed42\nDONE     SR=     ?  eval_openvla_attn_k09_long_seed42_v2\nDONE     SR=  44.0  eval_openvla_attn_k09_long_seed42_v3\nDONE     SR= 0.528  eval_openvla_baseline_long_seed42\nDONE     SR=     ?  eval_openvla_l2norm_k05_long_seed42\nDONE     SR=     ?  eval_openvla_l2norm_k075_long_seed42\nRUNNING  SR=     ?  eval_openvla_l2norm_k075_long_seed42_v2\nDONE     SR=     ?  eval_openvla_l2norm_k07_long_seed42\nDONE     SR= 0.312  eval_openvla_l2norm_k07_long_seed42_v2\nDONE     SR=     ?  eval_openvla_l2norm_k085_long_seed42\nDONE     SR= 0.388  eval_openvla_l2norm_k085_long_seed42_v2\nRUNNING  SR=     ?  eval_openvla_l2norm_k095_long_seed42\nDONE     SR=     ?  eval_openvla_l2norm_k09_long_seed42\nDONE     SR=     ?  eval_openvla_l2norm_k09_long_seed42_v2\nDONE     SR=  43.6  eval_openvla_l2norm_k09_long_seed42_v3\nDONE     SR=     ?  eval_openvla_random_k05_long_seed42\nDONE     SR=  18.6  eval_openvla_random_k05_long_seed42_v2\nDONE     SR=     ?  eval_openvla_random_k075_long_seed42\nDONE     SR=     ?  eval_openvla_random_k07_long_seed42\nDONE     SR= 0.388  eval_openvla_random_k07_long_seed42_v2\nDONE     SR=     ?  eval_openvla_random_k085_long_seed42\nPREPARING SR=     ?  eval_openvla_random_k085_long_seed42_v2\nDONE     SR=  0.45  eval_openvla_random_k085_long_seed42_v3\nRUNNING  SR=     ?  eval_openvla_random_k095_long_seed42\nPREPARING SR=     ?  eval_openvla_random_k095_long_seed42_v2\nDONE     SR=     ?  eval_openvla_random_k09_long_seed42\nDONE     SR=     ?  eval_openvla_random_k09_long_seed42_v2\nDONE     SR=  46.8  eval_openvla_random_k09_long_seed42_v3\n\nDONE     SR=  44.2  eval_openvla_attn_k05_goal_seed42\nDONE     SR=     ?  eval_openvla_attn_k05_goal_seed42_v2\nRUNNING  SR=     ?  eval_openvla_attn_k05_goal_seed42_v3\nDONE     SR=  67.4  eval_openvla_attn_k075_goal_seed42\nDONE     SR=     ?  eval_openvla_attn_k075_goal_seed42_v2\nDONE     SR= 0.664  eval_openvla_attn_k07_goal_seed42\nDONE     SR=     ?  eval_openvla_attn_k085_goal_seed42\nDONE     SR=     ?  eval_openvla_attn_k085_goal_seed42_v2\nDONE     SR=  74.6  eval_openvla_attn_k085_goal_seed42_v3\nDONE     SR=     ?  eval_openvla_attn_k095_goal_seed42\nRUNNING  SR=     ?  eval_openvla_attn_k095_goal_seed42_v2\nPREPARING SR=     ?  eval_openvla_attn_k095_goal_seed42_v3\nDONE     SR= 0.732  eval_openvla_attn_k09_goal_seed42\nDONE     SR=     ?  eval_openvla_attn_k09_goal_seed43\nDONE     SR=     ?  eval_openvla_attn_k09_goal_seed43_v2\nPREPARING SR=     ?  eval_openvla_attn_k09_goal_seed43_v3\nDONE     SR=  73.2  eval_openvla_attn_k09_goal_seed43_v4\nPREPARING SR=     ?  eval_openvla_baseline_goal_seed42\nPREPARING SR=     ?  eval_openvla_baseline_goal_seed42_v2\nDONE     SR=     ?  eval_openvla_baseline_goal_seed42_v3\nDONE     SR= 0.776  eval_openvla_baseline_goal_seed43\nDONE     SR= 0.434  eval_openvla_l2norm_k05_goal_seed42\nDONE     SR=     ?  eval_openvla_l2norm_k05_goal_seed42_v2\nDONE     SR= 0.434  eval_openvla_l2norm_k05_goal_seed42_v3\nDONE     SR=     ?  eval_openvla_l2norm_k075_goal_seed42\nDONE     SR=  70.2  eval_openvla_l2norm_k075_goal_seed42_v2\nDONE     SR= 0.684  eval_openvla_l2norm_k07_goal_seed42\nDONE     SR=  75.4  eval_openvla_l2norm_k085_goal_seed42\nDONE     SR=  75.2  eval_openvla_l2norm_k095_goal_seed42\nDONE     SR= 0.748  eval_openvla_l2norm_k09_goal_seed42\nDONE     SR=  75.2  eval_openvla_l2norm_k09_goal_seed43\nDONE     SR=     ?  eval_openvla_l2norm_k09_goal_seed43_v2\nDONE     SR= 0.752  eval_openvla_l2norm_k09_goal_seed43_v3\nDONE     SR= 0.522  eval_openvla_random_k05_goal_seed42\nDONE     SR= 0.522  eval_openvla_random_k05_goal_seed42_v2\nDONE     SR=    72  eval_openvla_random_k075_goal_seed42\nDONE     SR=     ?  eval_openvla_random_k07_goal_seed42\nDONE     SR=     ?  eval_openvla_random_k07_goal_seed42_v2\nPREPARING SR=     ?  eval_openvla_random_k07_goal_seed42_v3\nDONE     SR=  68.4  eval_openvla_random_k07_goal_seed42_v4\nDONE     SR=  78.6  eval_openvla_random_k085_goal_seed42\nDONE     SR=     ?  eval_openvla_random_k095_goal_seed42\nRUNNING  SR=     ?  eval_openvla_random_k095_goal_seed42_v2\nDONE     SR=  79.6  eval_openvla_random_k09_goal_seed42\nDONE     SR=     ?  eval_openvla_random_k09_goal_seed42_v2\nDONE     SR=  80.4  eval_openvla_random_k09_goal_seed43",
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

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
Now I can see the gaps clearly:

**Object missing:**
- `eval_openvla_l2norm_k085_object_seed42` — PREPARING (never ran!)
- `eval_openvla_l2norm_k095_object_seed42` — RUNNING (on another server)
- `eval_openvla_random_k085_object_seed42_v2` — PREPARING

**Long running/missing:**
- Several RUNNING experiments on other servers

The key gap is **L2norm k=0.85 Object** — it's in PREPARING state, meaning it was never actually deployed. 

The L2norm k=0.85 Object eval would fill the gap between k=0.9 at 70.6% and k=0.75 at 57.4%, but Object evals typically run 240-290 minutes, which is cutting it close against the <4 hour deadline. It's worth attempting since it's the most critical missing data point. I also notice the random k=0.85 Object v2 is still PREPARING, likely because v1 didn't report success rates properly.

I'm setting up the eval command for L2norm k=0.85 Object, adapting the parameters from the attention pruning experiment to use l2norm mode instead with the same k_ratio of 0.85. I need to account for how CUDA_VISIBLE_DEVICES remaps the GPU indices, so when I set CUDA_VISIBLE_DEVICES=1, the --gpu flag should be 0 to target that remapped device. Let me finalize and run this command.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "d054d918-217d-414c-bcab-5afc61fd46c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyqREq6ubKxj8BMFJ7a7Mq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4113,
      "cache_read_input_tokens": 49820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4113
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

_source line 56_

关键发现：**L2norm k=0.85 Object** 停在 PREPARING 状态，从未实际运行。这是 Object L2norm 曲线的关键缺口 (k=0.9=70.6%, k=0.75=57.4%)。

在 GPU1 上部署。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "b899d14b-b384-49a0-b3ec-cae68813c182",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyqREq6ubKxj8BMFJ7a7Mq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4113,
      "cache_read_input_tokens": 49820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4113
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

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job · `toolu_01CumYy7iDPq97Dztc39XoWM`</summary>

```json
{
  "server": "westd-27271",
  "gpu_ids": [
    "cuda:1"
  ],
  "exp_id": "eval_openvla_l2norm_k085_object_seed42",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm --k_ratio 0.85 --suite libero_object --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\"",
  "project": "importance_margin_vla_compress",
  "account": "root",
  "timeout_hours": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "25a776bb-1dc8-4fca-89bd-c39773cf1f0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyqREq6ubKxj8BMFJ7a7Mq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4113,
      "cache_read_input_tokens": 49820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4113
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

_source line 58 · 2026-05-27T06:17:48.223Z_

<details><summary>↩ Tool result · `toolu_01CumYy7iDPq97Dztc39XoWM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"pid\": \"734991\", \"log_file\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log\", \"gpu_ids\": [\"cuda:1\"], \"server\": \"westd-27271\", \"account\": \"root\", \"cuda_visible_devices\": \"1\", \"backend\": \"tmux\", \"tmux_session\": \"eval_openvla_l2norm_k085_object_seed42\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 18.03}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "aa65edf0-cf16-4de2-8f9f-5a1f42b4c577",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"pid\\\": \\\"734991\\\", \\\"log_file\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log\\\", \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"server\\\": \\\"westd-27271\\\", \\\"account\\\": \\\"root\\\", \\\"cuda_visible_devices\\\": \\\"1\\\", \\\"backend\\\": \\\"tmux\\\", \\\"tmux_session\\\": \\\"eval_openvla_l2norm_k085_object_seed42\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 18.03}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"pid\": \"734991\", \"log_file\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log\", \"gpu_ids\": [\"cuda:1\"], \"server\": \"westd-27271\", \"account\": \"root\", \"cuda_visible_devices\": \"1\", \"backend\": \"tmux\", \"tmux_session\": \"eval_openvla_l2norm_k085_object_seed42\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 18.03}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
Job submitted. Let me update the registry and then verify both GPUs are running.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "377e5df7-9beb-4e68-89b0-f491248e230e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ve74ASL4Z7UsBU2B7R5FWQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1467,
      "cache_read_input_tokens": 53933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1467
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

_source line 60_

已提交。更新 registry 并等待验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "1e06abe9-5b36-4dc5-8256-fe69e9bbc5d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ve74ASL4Z7UsBU2B7R5FWQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1467,
      "cache_read_input_tokens": 53933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1467
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01N2xZ3FoqfRBXheKWWkFBoD`</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k085_object_seed42",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": {
    "command": "python -u eval_openvla_l2norm_libero.py --mode l2norm --k_ratio 0.85 --suite libero_object --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object",
    "server": "westd-27271",
    "gpu_id": 1,
    "pid": 734991,
    "log_path": "~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log",
    "data_path": "libero_object",
    "data_count": "10 tasks x 50 episodes",
    "model_name": "openvla-7b-finetuned-libero-object",
    "seed": 42,
    "checkpoint_path": "N/A (eval only)",
    "checkpoint_source": "/root/autodl-tmp/openvla-libero-object",
    "eval_data": "libero_object"
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "fc01044b-578f-435e-9dbe-78bee4808e34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ve74ASL4Z7UsBU2B7R5FWQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1467,
      "cache_read_input_tokens": 53933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1467
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

_source line 62 · 2026-05-27T06:18:00.058Z_

<details><summary>↩ Tool result · `toolu_01N2xZ3FoqfRBXheKWWkFBoD`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.0569}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "18d08e8c-b2d2-4240-8492-38c7d6f0ddab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.0569}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.0569}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01XofRUtrqRyvNLy3kFckToZ`</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k085_object_seed42",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "38d7290f-fe5a-40e7-95cb-eeb99b245981",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FuhPGa8Mr1CyUshKxv4Hrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 55400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 64 · 2026-05-27T06:18:15.475Z_

<details><summary>↩ Tool result · `toolu_01XofRUtrqRyvNLy3kFckToZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k085_object_seed42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T07:52:33.834Z\", \"updated_at\": \"2026-05-27T06:18:08.713Z\", \"hypothesis\": \"OpenVLA L2norm k=0.85 Object seed42 重跑 — 验证前次 SR=55.2%（k=0.75=57.4% 非单调可疑）。Object L2norm cliff curve: k=0.95=70.6%, k=0.9=70.6%, k=0.85=55.2%?, k=0.75=57.4%, k=0.7=49.8%\", \"parent\": \"eval_openvla_l2norm_k09_object_seed42\", \"completed_at\": \"2026-05-26T13:26:44.353Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 55.2, \"task_sr\": {\"ketchup\": 92, \"alphabet_soup\": 60, \"salad_dressing\": 60, \"milk\": 58, \"orange_juice\": 54, \"chocolate_pudding\": 52, \"butter\": 50, \"bbq_sauce\": 44, \"tomato_sauce\": 42, \"cream_cheese\": 40}, \"n_episodes\": 500, \"duration_min\": 330.9}}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm --k_ratio 0.85 --suite libero_object --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"734991\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log\", \"submitted_at\": \"2026-05-27T06:17:36.138Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.5547}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "711113d2-1fb0-4e17-af2b-2a0c89a24363",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_openvla_l2norm_k085_object_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T07:52:33.834Z\\\", \\\"updated_at\\\": \\\"2026-05-27T06:18:08.713Z\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.85 Object seed42 重跑 — 验证前次 SR=55.2%（k=0.75=57.4% 非单调可疑）。Object L2norm cliff curve: k=0.95=70.6%, k=0.9=70.6%, k=0.85=55.2%?, k=0.75=57.4%, k=0.7=49.8%\\\", \\\"parent\\\": \\\"eval_openvla_l2norm_k09_object_seed42\\\", \\\"completed_at\\\": \\\"2026-05-26T13:26:44.353Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 55.2, \\\"task_sr\\\": {\\\"ketchup\\\": 92, \\\"alphabet_soup\\\": 60, \\\"salad_dressing\\\": 60, \\\"milk\\\": 58, \\\"orange_juice\\\": 54, \\\"chocolate_pudding\\\": 52, \\\"butter\\\": 50, \\\"bbq_sauce\\\": 44, \\\"tomato_sauce\\\": 42, \\\"cream_cheese\\\": 40}, \\\"n_episodes\\\": 500, \\\"duration_min\\\": 330.9}}}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm --k_ratio 0.85 --suite libero_object --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\\\\\\\"\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"734991\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T06:17:36.138Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 11.5547}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k085_object_seed42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T07:52:33.834Z\", \"updated_at\": \"2026-05-27T06:18:08.713Z\", \"hypothesis\": \"OpenVLA L2norm k=0.85 Object seed42 重跑 — 验证前次 SR=55.2%（k=0.75=57.4% 非单调可疑）。Object L2norm cliff curve: k=0.95=70.6%, k=0.9=70.6%, k=0.85=55.2%?, k=0.75=57.4%, k=0.7=49.8%\", \"parent\": \"eval_openvla_l2norm_k09_object_seed42\", \"completed_at\": \"2026-05-26T13:26:44.353Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 55.2, \"task_sr\": {\"ketchup\": 92, \"alphabet_soup\": 60, \"salad_dressing\": 60, \"milk\": 58, \"orange_juice\": 54, \"chocolate_pudding\": 52, \"butter\": 50, \"bbq_sauce\": 44, \"tomato_sauce\": 42, \"cream_cheese\": 40}, \"n_episodes\": 500, \"duration_min\": 330.9}}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm --k_ratio 0.85 --suite libero_object --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"734991\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log\", \"submitted_at\": \"2026-05-27T06:17:36.138Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.5547}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_016BV1necDfs1bMLX5aTBVgB`</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k085_object_seed42",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": {
    "command": "python -u eval_openvla_l2norm_libero.py --mode l2norm --k_ratio 0.85 --suite libero_object --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object",
    "server": "westd-27271",
    "gpu_id": 1,
    "pid": 734991,
    "log_path": "~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log",
    "data_path": "libero_object",
    "data_count": "10 tasks x 50 episodes",
    "model_name": "openvla-7b-finetuned-libero-object",
    "seed": 42,
    "checkpoint_path": "N/A (eval only)",
    "checkpoint_source": "/root/autodl-tmp/openvla-libero-object",
    "eval_data": "libero_object"
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "d4fd0af3-2ca8-4504-b9b2-2697b9f512a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeRVUpAMyjbnFRNA8ibyY7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 55923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 895
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

_source line 66 · 2026-05-27T06:18:32.477Z_

<details><summary>↩ Tool result · `toolu_016BV1necDfs1bMLX5aTBVgB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k085_object_seed42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T07:52:33.834Z\", \"updated_at\": \"2026-05-27T06:18:28.383Z\", \"hypothesis\": \"OpenVLA L2norm k=0.85 Object seed42 重跑 — 验证前次 SR=55.2%（k=0.75=57.4% 非单调可疑）。Object L2norm cliff curve: k=0.95=70.6%, k=0.9=70.6%, k=0.85=55.2%?, k=0.75=57.4%, k=0.7=49.8%\", \"parent\": \"eval_openvla_l2norm_k09_object_seed42\", \"completed_at\": \"2026-05-26T13:26:44.353Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 55.2, \"task_sr\": {\"ketchup\": 92, \"alphabet_soup\": 60, \"salad_dressing\": 60, \"milk\": 58, \"orange_juice\": 54, \"chocolate_pudding\": 52, \"butter\": 50, \"bbq_sauce\": 44, \"tomato_sauce\": 42, \"cream_cheese\": 40}, \"n_episodes\": 500, \"duration_min\": 330.9}}}, \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode l2norm --k_ratio 0.85 --suite libero_object --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": 734991, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log\", \"submitted_at\": \"2026-05-27T06:17:36.138Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": 1, \"data_path\": \"libero_object\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.9883}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "026069ae-9890-4396-be4f-2fb755d14254",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_openvla_l2norm_k085_object_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T07:52:33.834Z\\\", \\\"updated_at\\\": \\\"2026-05-27T06:18:28.383Z\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.85 Object seed42 重跑 — 验证前次 SR=55.2%（k=0.75=57.4% 非单调可疑）。Object L2norm cliff curve: k=0.95=70.6%, k=0.9=70.6%, k=0.85=55.2%?, k=0.75=57.4%, k=0.7=49.8%\\\", \\\"parent\\\": \\\"eval_openvla_l2norm_k09_object_seed42\\\", \\\"completed_at\\\": \\\"2026-05-26T13:26:44.353Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 55.2, \\\"task_sr\\\": {\\\"ketchup\\\": 92, \\\"alphabet_soup\\\": 60, \\\"salad_dressing\\\": 60, \\\"milk\\\": 58, \\\"orange_juice\\\": 54, \\\"chocolate_pudding\\\": 52, \\\"butter\\\": 50, \\\"bbq_sauce\\\": 44, \\\"tomato_sauce\\\": 42, \\\"cream_cheese\\\": 40}, \\\"n_episodes\\\": 500, \\\"duration_min\\\": 330.9}}}, \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode l2norm --k_ratio 0.85 --suite libero_object --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 734991, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T06:17:36.138Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"gpu_id\\\": 1, \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": \\\"10 tasks x 50 episodes\\\", \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-object\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"eval_data\\\": \\\"libero_object\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.9883}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k085_object_seed42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T07:52:33.834Z\", \"updated_at\": \"2026-05-27T06:18:28.383Z\", \"hypothesis\": \"OpenVLA L2norm k=0.85 Object seed42 重跑 — 验证前次 SR=55.2%（k=0.75=57.4% 非单调可疑）。Object L2norm cliff curve: k=0.95=70.6%, k=0.9=70.6%, k=0.85=55.2%?, k=0.75=57.4%, k=0.7=49.8%\", \"parent\": \"eval_openvla_l2norm_k09_object_seed42\", \"completed_at\": \"2026-05-26T13:26:44.353Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 55.2, \"task_sr\": {\"ketchup\": 92, \"alphabet_soup\": 60, \"salad_dressing\": 60, \"milk\": 58, \"orange_juice\": 54, \"chocolate_pudding\": 52, \"butter\": 50, \"bbq_sauce\": 44, \"tomato_sauce\": 42, \"cream_cheese\": 40}, \"n_episodes\": 500, \"duration_min\": 330.9}}}, \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode l2norm --k_ratio 0.85 --suite libero_object --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": 734991, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log\", \"submitted_at\": \"2026-05-27T06:17:36.138Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": 1, \"data_path\": \"libero_object\", \"data_count\": \"10 tasks x 50 episodes\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.9883}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 67_

验证两张 GPU 都在工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "5a6f48ba-9fdd-45b2-8572-246abee5ef8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DnswjKRpE4x6pTrHuJyrk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 56818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1208
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

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017fRmjLKCins9s6KcoGyKz5`</summary>

```json
{
  "server": "westd-27271",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "67b15ddc-fabb-4fa4-ab68-81ace80f0a1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DnswjKRpE4x6pTrHuJyrk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 56818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1208
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

### Tool result

_source line 69 · 2026-05-27T06:18:36.835Z_

<details><summary>↩ Tool result · `toolu_017fRmjLKCins9s6KcoGyKz5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 15964 MiB, 97887 MiB, 91 %\\n1, 1 MiB, 97887 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "4918465e-4606-40cf-937d-967d48fa5e1d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 15964 MiB, 97887 MiB, 91 %\\\\n1, 1 MiB, 97887 MiB, 0 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 15964 MiB, 97887 MiB, 91 %\\n1, 1 MiB, 97887 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
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
GPU1 still showing 1 MiB — the model hasn't loaded yet. Let me check the log to see if the process started correctly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "573ce38c-fc40-4a81-aaaa-fd0eb778a349",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jjzSo8XZAgeBc7nypiWrd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 58026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 71_

GPU1 还没开始加载模型，检查日志确认启动状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "c25df2d5-9b36-49e0-b574-7e4e78561f7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jjzSo8XZAgeBc7nypiWrd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 58026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BZ5urTaT1Zsyo58TtpCwAb`</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -20 /root/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "aaa50c74-124f-4e2a-9182-fd60316a39b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jjzSo8XZAgeBc7nypiWrd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 58026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 73 · 2026-05-27T06:18:41.707Z_

<details><summary>↩ Tool result · `toolu_01BZ5urTaT1Zsyo58TtpCwAb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: eval_openvla_l2norm_libero.py [-h]\\n                                     [--mode {baseline,random_prune,l2norm_prune,attention_prune}]\\n                                     [--k_ratio K_RATIO] [--suite SUITE]\\n                                     [--num_episodes NUM_EPISODES]\\n                                     [--seed SEED] [--output OUTPUT]\\n                                     [--center_crop]\\n                                     [--num_steps_wait NUM_STEPS_WAIT]\\n                                     [--model_path MODEL_PATH]\\n                                     [--unnorm_key UNNORM_KEY] [--gpu GPU]\\neval_openvla_l2norm_libero.py: error: argument --mode: invalid choice: 'l2norm' (choose from 'baseline', 'random_prune', 'l2norm_prune', 'attention_prune')\\nEXIT_CODE=2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "9685976a-54b8-446b-a840-ff26ee6be4bb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"usage: eval_openvla_l2norm_libero.py [-h]\\\\n                                     [--mode {baseline,random_prune,l2norm_prune,attention_prune}]\\\\n                                     [--k_ratio K_RATIO] [--suite SUITE]\\\\n                                     [--num_episodes NUM_EPISODES]\\\\n                                     [--seed SEED] [--output OUTPUT]\\\\n                                     [--center_crop]\\\\n                                     [--num_steps_wait NUM_STEPS_WAIT]\\\\n                                     [--model_path MODEL_PATH]\\\\n                                     [--unnorm_key UNNORM_KEY] [--gpu GPU]\\\\neval_openvla_l2norm_libero.py: error: argument --mode: invalid choice: 'l2norm' (choose from 'baseline', 'random_prune', 'l2norm_prune', 'attention_prune')\\\\nEXIT_CODE=2\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"usage: eval_openvla_l2norm_libero.py [-h]\\n                                     [--mode {baseline,random_prune,l2norm_prune,attention_prune}]\\n                                     [--k_ratio K_RATIO] [--suite SUITE]\\n                                     [--num_episodes NUM_EPISODES]\\n                                     [--seed SEED] [--output OUTPUT]\\n                                     [--center_crop]\\n                                     [--num_steps_wait NUM_STEPS_WAIT]\\n                                     [--model_path MODEL_PATH]\\n                                     [--unnorm_key UNNORM_KEY] [--gpu GPU]\\neval_openvla_l2norm_libero.py: error: argument --mode: invalid choice: 'l2norm' (choose from 'baseline', 'random_prune', 'l2norm_prune', 'attention_prune')\\nEXIT_CODE=2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
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
Ah, the mode should be `l2norm_prune`, not `l2norm`. Let me resubmit with the correct mode.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "7ed9bdc7-43ef-410f-aca1-bc3bb96ddd83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xgfE3VuZhua7TaREhjb1Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 58291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 625
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

### Assistant

_source line 75_

模式名错误，应为 `l2norm_prune`。重新提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "b5b1b613-268e-4aa7-8a9c-54c050a0cd72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xgfE3VuZhua7TaREhjb1Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 58291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 625
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

_source line 76_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job · `toolu_01SjHAat2o6ySvw7MamPBtjj`</summary>

```json
{
  "server": "westd-27271",
  "gpu_ids": [
    "cuda:1"
  ],
  "exp_id": "eval_openvla_l2norm_k085_object_seed42",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.85 --suite libero_object --seed 42 --gpu 0 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\"",
  "project": "importance_margin_vla_compress",
  "account": "root",
  "timeout_hours": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "1e69e7c2-0380-443a-b79f-117d099a3b7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xgfE3VuZhua7TaREhjb1Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 58291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 625
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

_source line 77 · 2026-05-27T06:18:54.359Z_

<details><summary>↩ Tool result · `toolu_01SjHAat2o6ySvw7MamPBtjj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"pid\": \"735723\", \"log_file\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log\", \"gpu_ids\": [\"cuda:1\"], \"server\": \"westd-27271\", \"account\": \"root\", \"cuda_visible_devices\": \"1\", \"backend\": \"tmux\", \"tmux_session\": \"eval_openvla_l2norm_k085_object_seed42\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.13}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "f527d167-90a6-4db1-8e6a-49a9ae95ceee",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"pid\\\": \\\"735723\\\", \\\"log_file\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log\\\", \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"server\\\": \\\"westd-27271\\\", \\\"account\\\": \\\"root\\\", \\\"cuda_visible_devices\\\": \\\"1\\\", \\\"backend\\\": \\\"tmux\\\", \\\"tmux_session\\\": \\\"eval_openvla_l2norm_k085_object_seed42\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 7.13}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"pid\": \"735723\", \"log_file\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log\", \"gpu_ids\": [\"cuda:1\"], \"server\": \"westd-27271\", \"account\": \"root\", \"cuda_visible_devices\": \"1\", \"backend\": \"tmux\", \"tmux_session\": \"eval_openvla_l2norm_k085_object_seed42\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.13}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 78_

等待模型加载后验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "7c5976dd-9e06-4c00-9e61-3b89aa7c8aa0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AD434CV4KSD1pBtfJiKyqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 598,
      "cache_read_input_tokens": 58916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 598
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

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KK6xnJSgbhnvd1mJQZt8Vp`</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -10 /root/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_object_seed42.log",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "2e12aafd-329b-43c3-b62f-ca51a3aec06a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AD434CV4KSD1pBtfJiKyqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 598,
      "cache_read_input_tokens": 58916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 598
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

### Tool result

_source line 80 · 2026-05-27T06:18:58.661Z_

<details><summary>↩ Tool result · `toolu_01KK6xnJSgbhnvd1mJQZt8Vp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-libero-object\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  9.19it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00, 12.35it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 12.72it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] L2 norm pruning: k=0.85\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[*] libero_object: 10 tasks x 50 episodes = 500 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "348f73b5-70f4-4d54-a28b-3f28b37bb032",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-libero-object\\\\n\\\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  9.19it/s]\\\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00, 12.35it/s]\\\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 12.72it/s]\\\\n[*] Model loaded, GPU: 15.1 GB\\\\n[*] Vision tokens: 256, dim: 4096\\\\n[*] L2 norm pruning: k=0.85\\\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n[*] libero_object: 10 tasks x 50 episodes = 500 total\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-libero-object\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  9.19it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00, 12.35it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 12.72it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] L2 norm pruning: k=0.85\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[*] libero_object: 10 tasks x 50 episodes = 500 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 81_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VzXeRnUqAoDR3kdyEBrHuT`</summary>

```json
{
  "server": "westd-27271",
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
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "3160afad-11b9-4991-8a9c-eda29cd7575c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTywyqTTBju7BzCEkCcoXg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 59514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 609
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

_source line 82 · 2026-05-27T06:19:02.934Z_

<details><summary>↩ Tool result · `toolu_01VzXeRnUqAoDR3kdyEBrHuT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 15964 MiB, 97887 MiB, 66 %\\n1, 15980 MiB, 97887 MiB, 76 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "bcd68d64-d3d1-4a95-8efd-3789b4a6e17d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 15964 MiB, 97887 MiB, 66 %\\\\n1, 15980 MiB, 97887 MiB, 76 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 15964 MiB, 97887 MiB, 66 %\\n1, 15980 MiB, 97887 MiB, 76 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 83_

两张 GPU 均已确认在跑：

| GPU | 显存 | 利用率 | 实验 |
|-----|------|--------|------|
| GPU0 | 15964 MiB | 66% | OV Attn k=0.95 Goal v3 (Task 1/10 进行中) |
| GPU1 | 15980 MiB | 76% | OV L2norm k=0.85 Object (刚启动，模型已加载) |

完成的结果：**OV Attn k=0.95 Object = 71.2%** (已注册)。

新部署：**OV L2norm k=0.85 Object** — 填补 Object L2norm 曲线关键缺口 (k=0.9=70.6% → k=0.85=? → k=0.75=57.4%)，验证前次可疑值 55.2%。预计 ~4.5h 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "uuid": "2363c398-aa1a-465c-a2eb-88c3a6f968ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012C6Ph85fKSssCokcrv8U1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 60123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 253
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

_source line 84_

两张 GPU 均已确认在跑：

| GPU | 显存 | 利用率 | 实验 |
|-----|------|--------|------|
| GPU0 | 15964 MiB | 66% | OV Attn k=0.95 Goal v3 (Task 1/10 进行中) |
| GPU1 | 15980 MiB | 76% | OV L2norm k=0.85 Object (刚启动，模型已加载) |

完成的结果：**OV Attn k=0.95 Object = 71.2%** (已注册)。

新部署：**OV L2norm k=0.85 Object** — 填补 Object L2norm 曲线关键缺口 (k=0.9=70.6% → k=0.85=? → k=0.75=57.4%)，验证前次可疑值 55.2%。预计 ~4.5h 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 271785,
  "duration_api_ms": 208361,
  "num_turns": 26,
  "stop_reason": "end_turn",
  "session_id": "77f0b2fb-f038-4bff-bd48-3bed171e3c77",
  "total_cost_usd": 0.9786440000000001,
  "usage": {
    "input_tokens": 22,
    "cache_creation_input_tokens": 48531,
    "cache_read_input_tokens": 804630,
    "output_tokens": 9558,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 48531,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 262,
        "cache_read_input_tokens": 60123,
        "cache_creation_input_tokens": 253,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 253
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1976,
      "outputTokens": 652,
      "cacheReadInputTokens": 17830,
      "cacheCreationInputTokens": 21545,
      "webSearchRequests": 0,
      "costUSD": 0.033950249999999994,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 22,
      "outputTokens": 9558,
      "cacheReadInputTokens": 804630,
      "cacheCreationInputTokens": 48531,
      "webSearchRequests": 0,
      "costUSD": 0.9446937500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "89ad14b4-2830-4893-8c12-fc821e208621"
}
```

</details>

---
