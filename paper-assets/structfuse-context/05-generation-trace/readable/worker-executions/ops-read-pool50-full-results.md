# ops read pool50 full results

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_ops_read_pool50_full_results_20260516T051426.log`
- **Structured JSON:** [`24c5761775712847af94.json`](../../sessions/24/24c5761775712847af94.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
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
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "bcad0fbc-dea8-484a-8ee4-57e0d8682b3e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
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
    "resetsAt": 1778919600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4272abce-01b9-4786-9b9d-cd7c16bf5195",
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to read evaluation results from a remote server via SSH. Let me fetch the necessary tool schemas first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "9fc7920f-81c9-4390-8c95-66e58233867a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AT6wHK1MWXhES6nTxGCX6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12026,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12026
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017CAEBnoaHmpEG2jNJZ253A`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "9c4a0a0b-299f-4b0a-94fa-e444ed964024",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AT6wHK1MWXhES6nTxGCX6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12026,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12026
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

_source line 6 · 2026-05-16T05:14:39.138Z_

<details><summary>↩ Tool result · `toolu_017CAEBnoaHmpEG2jNJZ253A`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "750c0816-5994-4fa3-b085-c52792d00f03",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SKjb4mYiiXxdqEqWXaqzXB`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "python3 -c \"\nimport json\nwith open('/root/autodl-tmp/structfuse/results/pool50_eval_qwen_all.json') as f:\n    data = json.load(f)\nif isinstance(data, dict):\n    print('Keys:', list(data.keys())[:20])\n    for k in list(data.keys())[:3]:\n        print(f'{k}: {json.dumps(data[k], indent=2)[:400]}')\nelif isinstance(data, list):\n    print(f'List of {len(data)} items')\n    print(json.dumps(data[0], indent=2)[:500])\n\"\n",
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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "755dbf34-0d51-4f20-b76d-12d33d8a0b0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FoEqq95eydsGre2uRtP2Vi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 23473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 465
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

_source line 8 · 2026-05-16T05:14:43.718Z_

<details><summary>↩ Tool result · `toolu_01SKjb4mYiiXxdqEqWXaqzXB`</summary>

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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "99c5bcf4-980a-4b3c-96f3-a3dc6a521682",
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AmUNag8DDP7dCeTaBtX4KT`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ps -p 142966 -o pid,etime 2>/dev/null",
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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "4f2699bb-c2aa-4db7-90cf-34164b7e249d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FoEqq95eydsGre2uRtP2Vi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 23473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 465
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

_source line 10 · 2026-05-16T05:14:44.638Z_

<details><summary>↩ Tool result · `toolu_01AmUNag8DDP7dCeTaBtX4KT`</summary>

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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "c0eb1ba5-b33c-4031-9467-60a43e9d1cf5",
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012wdE5yUuJQs5hfXzWKNv65`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -20 /tmp/pool50_eval_starcoder.log 2>/dev/null",
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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "1581a63c-8456-4ca6-a2e8-6536f8ab0c34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FoEqq95eydsGre2uRtP2Vi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 23473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 465
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

_source line 12 · 2026-05-16T05:14:44.987Z_

<details><summary>↩ Tool result · `toolu_012wdE5yUuJQs5hfXzWKNv65`</summary>

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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "d6da16c7-d73b-40db-a989-d265e13c45d8",
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

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
The read-only tool is quite restrictive. Let me try with simpler commands - cat for the JSON file, and simpler ps/tail commands.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "53ea8304-af47-4640-bf11-c0863ce91df7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHrVBHj2i4NLmRfbSKHkL6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 23938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 834
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

_source line 14_

读取命令受限，换用基础命令重试。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "435f8504-6f03-4f0b-bbca-681bd9d3770b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHrVBHj2i4NLmRfbSKHkL6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 23938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 834
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

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RQDiNbqDeKxGRcR2Nagu9b`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/autodl-tmp/structfuse/results/pool50_eval_qwen_all.json",
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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "2286d8ce-971b-402f-ad62-4a8352ad3292",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHrVBHj2i4NLmRfbSKHkL6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 23938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 834
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01J46stR4TyLm8XVjSftXr6A`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -20 /tmp/pool50_eval_starcoder.log",
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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "2fa3cd9b-a799-4f79-a9d7-28e3c3ac8dfa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHrVBHj2i4NLmRfbSKHkL6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 23938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 834
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

_source line 17 · 2026-05-16T05:14:50.444Z_

<details><summary>↩ Tool result · `toolu_01RQDiNbqDeKxGRcR2Nagu9b`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.3659731543624162,\\n      \\\"recall@1_std\\\": 0.005421722262716973,\\n      \\\"recall@5_mean\\\": 0.8930872483221476,\\n      \\\"recall@5_std\\\": 0.002731139590520259\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.375503355704698,\\n        \\\"recall@5\\\": 0.8922818791946309\\n      },\\n      {\\n        \\\"recall@1\\\": 0.36140939597315436,\\n        \\\"recall@5\\\": 0.8882550335570469\\n      },\\n      {\\n        \\\"recall@1\\\": 0.36006711409395975,\\n        \\\"recall@5\\\": 0.8963087248322148\\n      },\\n      {\\n        \\\"recall@1\\\": 0.36644295302013424,\\n        \\\"recall@5\\\": 0.8942953020134228\\n      },\\n      {\\n        \\\"recall@1\\\": 0.36644295302013424,\\n        \\\"recall@5\\\": 0.8942953020134228\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.38973154362416107,\\n      \\\"recall@1_std\\\": 0.004842457451690605,\\n      \\\"recall@5_mean\\\": 0.9259060402684565,\\n      \\\"recall@5_std\\\": 0.0009347911595425639\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.3912751677852349,\\n        \\\"recall@5\\\": 0.926510067114094\\n      },\\n      {\\n        \\\"recall@1\\\": 0.39362416107382553,\\n        \\\"recall@5\\\": 0.9248322147651007\\n      },\\n      {\\n        \\\"recall@1\\\": 0.39362416107382553,\\n        \\\"recall@5\\\": 0.9271812080536913\\n      },\\n      {\\n        \\\"recall@1\\\": 0.38053691275167784,\\n        \\\"recall@5\\\": 0.9248322147651007\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3895973154362416,\\n        \\\"recall@5\\\": 0.9261744966442953\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_recall_at_1\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.31711409395973156,\\n      \\\"recall@1_std\\\": 0.005128851858937662,\\n      \\\"recall@5_mean\\\": 0.8473154362416107,\\n      \\\"recall@5_std\\\": 0.0034614220022087566\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.32550335570469796,\\n        \\\"recall@5\\\": 0.8419463087248322\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3181208053691275,\\n        \\\"recall@5\\\": 0.8523489932885906\\n      },\\n      {\\n        \\\"recall@1\\\": 0.31476510067114094,\\n        \\\"recall@5\\\": 0.8456375838926175\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3174496644295302,\\n        \\\"recall@5\\\": 0.8489932885906041\\n      },\\n      {\\n        \\\"recall@1\\\": 0.30973154362416105,\\n        \\\"recall@5\\\": 0.8476510067114094\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.27302013422818794,\\n      \\\"recall@1_std\\\": 0.004902545602080458,\\n      \\\"recall@5_mean\\\": 0.7681208053691275,\\n      \\\"recall@5_std\\\": 0.0045121439769051285\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.2802013422818792,\\n        \\\"recall@5\\\": 0.7597315436241611\\n      },\\n      {\\n        \\\"recall@1\\\": 0.2664429530201342,\\n        \\\"recall@5\\\": 0.771476510067114\\n      },\\n      {\\n        \\\"recall@1\\\": 0.2687919463087248,\\n        \\\"recall@5\\\": 0.7671140939597315\\n      },\\n      {\\n        \\\"recall@1\\\": 0.27550335570469797,\\n        \\\"recall@5\\\": 0.7704697986577181\\n      },\\n      {\\n        \\\"recall@1\\\": 0.27416107382550337,\\n        \\\"recall@5\\\": 0.7718120805369127\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models\\n\\n... [截断: 输出过长，省略 3479 字符] ...\\n\\n     \\\"recall@1\\\": 0.33624161073825504,\\n        \\\"recall@5\\\": 0.8573825503355704\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3359060402684564,\\n        \\\"recall@5\\\": 0.8674496644295302\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_val_loss\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.3693959731543624,\\n      \\\"recall@1_std\\\": 0.0056686583661150845,\\n      \\\"recall@5_mean\\\": 0.9030872483221476,\\n      \\\"recall@5_std\\\": 0.0015215817515107097\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.3781879194630873,\\n        \\\"recall@5\\\": 0.9003355704697986\\n      },\\n      {\\n        \\\"recall@1\\\": 0.36308724832214767,\\n        \\\"recall@5\\\": 0.9036912751677852\\n      },\\n      {\\n        \\\"recall@1\\\": 0.363758389261745,\\n        \\\"recall@5\\\": 0.9046979865771813\\n      },\\n      {\\n        \\\"recall@1\\\": 0.37281879194630874,\\n        \\\"recall@5\\\": 0.9026845637583892\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3691275167785235,\\n        \\\"recall@5\\\": 0.9040268456375838\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.27302013422818794,\\n      \\\"recall@1_std\\\": 0.004902545602080458,\\n      \\\"recall@5_mean\\\": 0.7681208053691275,\\n      \\\"recall@5_std\\\": 0.0045121439769051285\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.2802013422818792,\\n        \\\"recall@5\\\": 0.7597315436241611\\n      },\\n      {\\n        \\\"recall@1\\\": 0.2664429530201342,\\n        \\\"recall@5\\\": 0.771476510067114\\n      },\\n      {\\n        \\\"recall@1\\\": 0.2687919463087248,\\n        \\\"recall@5\\\": 0.7671140939597315\\n      },\\n      {\\n        \\\"recall@1\\\": 0.27550335570469797,\\n        \\\"recall@5\\\": 0.7704697986577181\\n      },\\n      {\\n        \\\"recall@1\\\": 0.27416107382550337,\\n        \\\"recall@5\\\": 0.7718120805369127\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.3138255033557047,\\n      \\\"recall@1_std\\\": 0.006379017222660111,\\n      \\\"recall@5_mean\\\": 0.826510067114094,\\n      \\\"recall@5_std\\\": 0.004180513155006014\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.3197986577181208,\\n        \\\"recall@5\\\": 0.8281879194630872\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3124161073825503,\\n        \\\"recall@5\\\": 0.8288590604026845\\n      },\\n      {\\n        \\\"recall@1\\\": 0.30201342281879195,\\n        \\\"recall@5\\\": 0.8258389261744966\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3174496644295302,\\n        \\\"recall@5\\\": 0.8187919463087249\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3174496644295302,\\n        \\\"recall@5\\\": 0.8308724832214766\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.3181208053691275,\\n      \\\"recall@1_std\\\": 0.005013382388451839,\\n      \\\"recall@5_mean\\\": 0.8253020134228187,\\n      \\\"recall@5_std\\\": 0.004383531756458478\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.3261744966442953,\\n        \\\"recall@5\\\": 0.8224832214765101\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3110738255033557,\\n        \\\"recall@5\\\": 0.825503355704698\\n      },\\n      {\\n        \\\"recall@1\\\": 0.32046979865771813,\\n        \\\"recall@5\\\": 0.8265100671140939\\n      },\\n      {\\n        \\\"recall@1\\\": 0.31644295302013425,\\n        \\\"recall@5\\\": 0.8194630872483222\\n      },\\n      {\\n        \\\"recall@1\\\": 0.31644295302013425,\\n        \\\"recall@5\\\": 0.8325503355704698\\n      }\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "59a93349-8ae2-4bfe-9a14-dad4dc9e1910",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1\\\\\\\": {\\\\n    \\\\\\\"config_model_name\\\\\\\": \\\\\\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\\\\\",\\\\n    \\\\\\\"pool_size\\\\\\\": 50,\\\\n    \\\\\\\"num_samples\\\\\\\": 5,\\\\n    \\\\\\\"num_queries\\\\\\\": 2980,\\\\n    \\\\\\\"metrics\\\\\\\": {\\\\n      \\\\\\\"recall@1_mean\\\\\\\": 0.3659731543624162,\\\\n      \\\\\\\"recall@1_std\\\\\\\": 0.005421722262716973,\\\\n      \\\\\\\"recall@5_mean\\\\\\\": 0.8930872483221476,\\\\n      \\\\\\\"recall@5_std\\\\\\\": 0.002731139590520259\\\\n    },\\\\n    \\\\\\\"per_trial\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.375503355704698,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8922818791946309\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.36140939597315436,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8882550335570469\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.36006711409395975,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8963087248322148\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.36644295302013424,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8942953020134228\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.36644295302013424,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8942953020134228\\\\n      }\\\\n    ]\\\\n  },\\\\n  \\\\\\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1\\\\\\\": {\\\\n    \\\\\\\"config_model_name\\\\\\\": \\\\\\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\\\\\",\\\\n    \\\\\\\"pool_size\\\\\\\": 50,\\\\n    \\\\\\\"num_samples\\\\\\\": 5,\\\\n    \\\\\\\"num_queries\\\\\\\": 2980,\\\\n    \\\\\\\"metrics\\\\\\\": {\\\\n      \\\\\\\"recall@1_mean\\\\\\\": 0.38973154362416107,\\\\n      \\\\\\\"recall@1_std\\\\\\\": 0.004842457451690605,\\\\n      \\\\\\\"recall@5_mean\\\\\\\": 0.9259060402684565,\\\\n      \\\\\\\"recall@5_std\\\\\\\": 0.0009347911595425639\\\\n    },\\\\n    \\\\\\\"per_trial\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3912751677852349,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.926510067114094\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.39362416107382553,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.9248322147651007\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.39362416107382553,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.9271812080536913\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.38053691275167784,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.9248322147651007\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3895973154362416,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.9261744966442953\\\\n      }\\\\n    ]\\\\n  },\\\\n  \\\\\\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_recall_at_1\\\\\\\": {\\\\n    \\\\\\\"config_model_name\\\\\\\": \\\\\\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\\\\\",\\\\n    \\\\\\\"pool_size\\\\\\\": 50,\\\\n    \\\\\\\"num_samples\\\\\\\": 5,\\\\n    \\\\\\\"num_queries\\\\\\\": 2980,\\\\n    \\\\\\\"metrics\\\\\\\": {\\\\n      \\\\\\\"recall@1_mean\\\\\\\": 0.31711409395973156,\\\\n      \\\\\\\"recall@1_std\\\\\\\": 0.005128851858937662,\\\\n      \\\\\\\"recall@5_mean\\\\\\\": 0.8473154362416107,\\\\n      \\\\\\\"recall@5_std\\\\\\\": 0.0034614220022087566\\\\n    },\\\\n    \\\\\\\"per_trial\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.32550335570469796,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8419463087248322\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3181208053691275,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8523489932885906\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.31476510067114094,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8456375838926175\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3174496644295302,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8489932885906041\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.30973154362416105,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8476510067114094\\\\n      }\\\\n    ]\\\\n  },\\\\n  \\\\\\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\\\\\\": {\\\\n    \\\\\\\"config_model_name\\\\\\\": \\\\\\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\\\\\",\\\\n    \\\\\\\"pool_size\\\\\\\": 50,\\\\n    \\\\\\\"num_samples\\\\\\\": 5,\\\\n    \\\\\\\"num_queries\\\\\\\": 2980,\\\\n    \\\\\\\"metrics\\\\\\\": {\\\\n      \\\\\\\"recall@1_mean\\\\\\\": 0.27302013422818794,\\\\n      \\\\\\\"recall@1_std\\\\\\\": 0.004902545602080458,\\\\n      \\\\\\\"recall@5_mean\\\\\\\": 0.7681208053691275,\\\\n      \\\\\\\"recall@5_std\\\\\\\": 0.0045121439769051285\\\\n    },\\\\n    \\\\\\\"per_trial\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.2802013422818792,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.7597315436241611\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.2664429530201342,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.771476510067114\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.2687919463087248,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.7671140939597315\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.27550335570469797,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.7704697986577181\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.27416107382550337,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.7718120805369127\\\\n      }\\\\n    ]\\\\n  },\\\\n  \\\\\\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\\\\\\": {\\\\n    \\\\\\\"config_model_name\\\\\\\": \\\\\\\"/root/autodl-tmp/structfuse/models\\\\n\\\\n... [截断: 输出过长，省略 3479 字符] ...\\\\n\\\\n     \\\\\\\"recall@1\\\\\\\": 0.33624161073825504,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8573825503355704\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3359060402684564,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8674496644295302\\\\n      }\\\\n    ]\\\\n  },\\\\n  \\\\\\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_val_loss\\\\\\\": {\\\\n    \\\\\\\"config_model_name\\\\\\\": \\\\\\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\\\\\",\\\\n    \\\\\\\"pool_size\\\\\\\": 50,\\\\n    \\\\\\\"num_samples\\\\\\\": 5,\\\\n    \\\\\\\"num_queries\\\\\\\": 2980,\\\\n    \\\\\\\"metrics\\\\\\\": {\\\\n      \\\\\\\"recall@1_mean\\\\\\\": 0.3693959731543624,\\\\n      \\\\\\\"recall@1_std\\\\\\\": 0.0056686583661150845,\\\\n      \\\\\\\"recall@5_mean\\\\\\\": 0.9030872483221476,\\\\n      \\\\\\\"recall@5_std\\\\\\\": 0.0015215817515107097\\\\n    },\\\\n    \\\\\\\"per_trial\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3781879194630873,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.9003355704697986\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.36308724832214767,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.9036912751677852\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.363758389261745,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.9046979865771813\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.37281879194630874,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.9026845637583892\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3691275167785235,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.9040268456375838\\\\n      }\\\\n    ]\\\\n  },\\\\n  \\\\\\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss\\\\\\\": {\\\\n    \\\\\\\"config_model_name\\\\\\\": \\\\\\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\\\\\",\\\\n    \\\\\\\"pool_size\\\\\\\": 50,\\\\n    \\\\\\\"num_samples\\\\\\\": 5,\\\\n    \\\\\\\"num_queries\\\\\\\": 2980,\\\\n    \\\\\\\"metrics\\\\\\\": {\\\\n      \\\\\\\"recall@1_mean\\\\\\\": 0.27302013422818794,\\\\n      \\\\\\\"recall@1_std\\\\\\\": 0.004902545602080458,\\\\n      \\\\\\\"recall@5_mean\\\\\\\": 0.7681208053691275,\\\\n      \\\\\\\"recall@5_std\\\\\\\": 0.0045121439769051285\\\\n    },\\\\n    \\\\\\\"per_trial\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.2802013422818792,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.7597315436241611\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.2664429530201342,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.771476510067114\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.2687919463087248,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.7671140939597315\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.27550335570469797,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.7704697986577181\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.27416107382550337,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.7718120805369127\\\\n      }\\\\n    ]\\\\n  },\\\\n  \\\\\\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss\\\\\\\": {\\\\n    \\\\\\\"config_model_name\\\\\\\": \\\\\\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\\\\\",\\\\n    \\\\\\\"pool_size\\\\\\\": 50,\\\\n    \\\\\\\"num_samples\\\\\\\": 5,\\\\n    \\\\\\\"num_queries\\\\\\\": 2980,\\\\n    \\\\\\\"metrics\\\\\\\": {\\\\n      \\\\\\\"recall@1_mean\\\\\\\": 0.3138255033557047,\\\\n      \\\\\\\"recall@1_std\\\\\\\": 0.006379017222660111,\\\\n      \\\\\\\"recall@5_mean\\\\\\\": 0.826510067114094,\\\\n      \\\\\\\"recall@5_std\\\\\\\": 0.004180513155006014\\\\n    },\\\\n    \\\\\\\"per_trial\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3197986577181208,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8281879194630872\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3124161073825503,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8288590604026845\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.30201342281879195,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8258389261744966\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3174496644295302,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8187919463087249\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3174496644295302,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8308724832214766\\\\n      }\\\\n    ]\\\\n  },\\\\n  \\\\\\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss\\\\\\\": {\\\\n    \\\\\\\"config_model_name\\\\\\\": \\\\\\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\\\\\",\\\\n    \\\\\\\"pool_size\\\\\\\": 50,\\\\n    \\\\\\\"num_samples\\\\\\\": 5,\\\\n    \\\\\\\"num_queries\\\\\\\": 2980,\\\\n    \\\\\\\"metrics\\\\\\\": {\\\\n      \\\\\\\"recall@1_mean\\\\\\\": 0.3181208053691275,\\\\n      \\\\\\\"recall@1_std\\\\\\\": 0.005013382388451839,\\\\n      \\\\\\\"recall@5_mean\\\\\\\": 0.8253020134228187,\\\\n      \\\\\\\"recall@5_std\\\\\\\": 0.004383531756458478\\\\n    },\\\\n    \\\\\\\"per_trial\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3261744966442953,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8224832214765101\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.3110738255033557,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.825503355704698\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.32046979865771813,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8265100671140939\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.31644295302013425,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8194630872483222\\\\n      },\\\\n      {\\\\n        \\\\\\\"recall@1\\\\\\\": 0.31644295302013425,\\\\n        \\\\\\\"recall@5\\\\\\\": 0.8325503355704698\\\\n      }\\\\n    ]\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.17}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.3659731543624162,\\n      \\\"recall@1_std\\\": 0.005421722262716973,\\n      \\\"recall@5_mean\\\": 0.8930872483221476,\\n      \\\"recall@5_std\\\": 0.002731139590520259\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.375503355704698,\\n        \\\"recall@5\\\": 0.8922818791946309\\n      },\\n      {\\n        \\\"recall@1\\\": 0.36140939597315436,\\n        \\\"recall@5\\\": 0.8882550335570469\\n      },\\n      {\\n        \\\"recall@1\\\": 0.36006711409395975,\\n        \\\"recall@5\\\": 0.8963087248322148\\n      },\\n      {\\n        \\\"recall@1\\\": 0.36644295302013424,\\n        \\\"recall@5\\\": 0.8942953020134228\\n      },\\n      {\\n        \\\"recall@1\\\": 0.36644295302013424,\\n        \\\"recall@5\\\": 0.8942953020134228\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.38973154362416107,\\n      \\\"recall@1_std\\\": 0.004842457451690605,\\n      \\\"recall@5_mean\\\": 0.9259060402684565,\\n      \\\"recall@5_std\\\": 0.0009347911595425639\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.3912751677852349,\\n        \\\"recall@5\\\": 0.926510067114094\\n      },\\n      {\\n        \\\"recall@1\\\": 0.39362416107382553,\\n        \\\"recall@5\\\": 0.9248322147651007\\n      },\\n      {\\n        \\\"recall@1\\\": 0.39362416107382553,\\n        \\\"recall@5\\\": 0.9271812080536913\\n      },\\n      {\\n        \\\"recall@1\\\": 0.38053691275167784,\\n        \\\"recall@5\\\": 0.9248322147651007\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3895973154362416,\\n        \\\"recall@5\\\": 0.9261744966442953\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_recall_at_1\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.31711409395973156,\\n      \\\"recall@1_std\\\": 0.005128851858937662,\\n      \\\"recall@5_mean\\\": 0.8473154362416107,\\n      \\\"recall@5_std\\\": 0.0034614220022087566\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.32550335570469796,\\n        \\\"recall@5\\\": 0.8419463087248322\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3181208053691275,\\n        \\\"recall@5\\\": 0.8523489932885906\\n      },\\n      {\\n        \\\"recall@1\\\": 0.31476510067114094,\\n        \\\"recall@5\\\": 0.8456375838926175\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3174496644295302,\\n        \\\"recall@5\\\": 0.8489932885906041\\n      },\\n      {\\n        \\\"recall@1\\\": 0.30973154362416105,\\n        \\\"recall@5\\\": 0.8476510067114094\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.27302013422818794,\\n      \\\"recall@1_std\\\": 0.004902545602080458,\\n      \\\"recall@5_mean\\\": 0.7681208053691275,\\n      \\\"recall@5_std\\\": 0.0045121439769051285\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.2802013422818792,\\n        \\\"recall@5\\\": 0.7597315436241611\\n      },\\n      {\\n        \\\"recall@1\\\": 0.2664429530201342,\\n        \\\"recall@5\\\": 0.771476510067114\\n      },\\n      {\\n        \\\"recall@1\\\": 0.2687919463087248,\\n        \\\"recall@5\\\": 0.7671140939597315\\n      },\\n      {\\n        \\\"recall@1\\\": 0.27550335570469797,\\n        \\\"recall@5\\\": 0.7704697986577181\\n      },\\n      {\\n        \\\"recall@1\\\": 0.27416107382550337,\\n        \\\"recall@5\\\": 0.7718120805369127\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models\\n\\n... [截断: 输出过长，省略 3479 字符] ...\\n\\n     \\\"recall@1\\\": 0.33624161073825504,\\n        \\\"recall@5\\\": 0.8573825503355704\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3359060402684564,\\n        \\\"recall@5\\\": 0.8674496644295302\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_val_loss\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.3693959731543624,\\n      \\\"recall@1_std\\\": 0.0056686583661150845,\\n      \\\"recall@5_mean\\\": 0.9030872483221476,\\n      \\\"recall@5_std\\\": 0.0015215817515107097\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.3781879194630873,\\n        \\\"recall@5\\\": 0.9003355704697986\\n      },\\n      {\\n        \\\"recall@1\\\": 0.36308724832214767,\\n        \\\"recall@5\\\": 0.9036912751677852\\n      },\\n      {\\n        \\\"recall@1\\\": 0.363758389261745,\\n        \\\"recall@5\\\": 0.9046979865771813\\n      },\\n      {\\n        \\\"recall@1\\\": 0.37281879194630874,\\n        \\\"recall@5\\\": 0.9026845637583892\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3691275167785235,\\n        \\\"recall@5\\\": 0.9040268456375838\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.27302013422818794,\\n      \\\"recall@1_std\\\": 0.004902545602080458,\\n      \\\"recall@5_mean\\\": 0.7681208053691275,\\n      \\\"recall@5_std\\\": 0.0045121439769051285\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.2802013422818792,\\n        \\\"recall@5\\\": 0.7597315436241611\\n      },\\n      {\\n        \\\"recall@1\\\": 0.2664429530201342,\\n        \\\"recall@5\\\": 0.771476510067114\\n      },\\n      {\\n        \\\"recall@1\\\": 0.2687919463087248,\\n        \\\"recall@5\\\": 0.7671140939597315\\n      },\\n      {\\n        \\\"recall@1\\\": 0.27550335570469797,\\n        \\\"recall@5\\\": 0.7704697986577181\\n      },\\n      {\\n        \\\"recall@1\\\": 0.27416107382550337,\\n        \\\"recall@5\\\": 0.7718120805369127\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.3138255033557047,\\n      \\\"recall@1_std\\\": 0.006379017222660111,\\n      \\\"recall@5_mean\\\": 0.826510067114094,\\n      \\\"recall@5_std\\\": 0.004180513155006014\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.3197986577181208,\\n        \\\"recall@5\\\": 0.8281879194630872\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3124161073825503,\\n        \\\"recall@5\\\": 0.8288590604026845\\n      },\\n      {\\n        \\\"recall@1\\\": 0.30201342281879195,\\n        \\\"recall@5\\\": 0.8258389261744966\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3174496644295302,\\n        \\\"recall@5\\\": 0.8187919463087249\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3174496644295302,\\n        \\\"recall@5\\\": 0.8308724832214766\\n      }\\n    ]\\n  },\\n  \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss\\\": {\\n    \\\"config_model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n    \\\"pool_size\\\": 50,\\n    \\\"num_samples\\\": 5,\\n    \\\"num_queries\\\": 2980,\\n    \\\"metrics\\\": {\\n      \\\"recall@1_mean\\\": 0.3181208053691275,\\n      \\\"recall@1_std\\\": 0.005013382388451839,\\n      \\\"recall@5_mean\\\": 0.8253020134228187,\\n      \\\"recall@5_std\\\": 0.004383531756458478\\n    },\\n    \\\"per_trial\\\": [\\n      {\\n        \\\"recall@1\\\": 0.3261744966442953,\\n        \\\"recall@5\\\": 0.8224832214765101\\n      },\\n      {\\n        \\\"recall@1\\\": 0.3110738255033557,\\n        \\\"recall@5\\\": 0.825503355704698\\n      },\\n      {\\n        \\\"recall@1\\\": 0.32046979865771813,\\n        \\\"recall@5\\\": 0.8265100671140939\\n      },\\n      {\\n        \\\"recall@1\\\": 0.31644295302013425,\\n        \\\"recall@5\\\": 0.8194630872483222\\n      },\\n      {\\n        \\\"recall@1\\\": 0.31644295302013425,\\n        \\\"recall@5\\\": 0.8325503355704698\\n      }\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SbwoZwvsQQVBQBycwoWFWV`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ps -p 142966 -o pid,etime",
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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "b5377fbb-b768-452b-aea0-a27418e121f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHrVBHj2i4NLmRfbSKHkL6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 23938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 834
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

_source line 19 · 2026-05-16T05:14:51.144Z_

<details><summary>↩ Tool result · `toolu_01J46stR4TyLm8XVjSftXr6A`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Encoding queries...\\n\\rEncoding:   0%|          | 0/94 [00:00<?, ?it/s]\\rEncoding:   1%|          | 1/94 [00:06<10:10,  6.56s/it]\\rEncoding:   2%|▏         | 2/94 [00:14<11:06,  7.25s/it]\\rEncoding:   3%|▎         | 3/94 [00:19<09:55,  6.54s/it]\\rEncoding:   4%|▍         | 4/94 [00:26<09:29,  6.33s/it]\\rEncoding:   5%|▌         | 5/94 [00:31<08:54,  6.00s/it]\\rEncoding:   6%|▋         | 6/94 [00:37<08:48,  6.00s/it]\\rEncoding:   7%|▋         | 7/94 [00:43<08:55,  6.16s/it]\\rEncoding:   9%|▊         | 8/94 [00:49<08:39,  6.04s/it]\\rEncoding:  10%|▉         | 9/94 [00:53<07:36,  5.37s/it]\\rEncoding:  11%|█         | 10/94 [00:57<06:59,  5.00s/it]\\rEncoding:  12%|█▏        | 11/94 [01:02<06:50,  4.94s/it]\\rEncoding:  13%|█▎        | 12/94 [01:06<06:18,  4.61s/it]\\rEncoding:  14%|█▍        | 13/94 [01:10<05:53,  4.37s/it]\\rEncoding:  15%|█▍        | 14/94 [01:13<05:31,  4.14s/it]\\rEncoding:  16%|█▌        | 15/94 [01:17<05:21,  4.06s/it]\\rEncoding:  17%|█▋        | 16/94 [01:21<05:10,  3.98s/it]\\rEncoding:  18%|█▊        | 17/94 [01:25<04:56,  3.85s/it]\\rEncoding:  19%|█▉        | 18/94 [01:27<04:23,  3.47s/it]\\rEncoding:  20%|██        | 19/94 [01:31<04:22,  3.50s/it]\\rEncoding:  21%|██▏       | 20/94 [01:34<04:22,  3.54s/it]\\rEncoding:  22%|██▏       | 21/94 [01:38<04:17,  3.53s/it]\\rEncoding:  23%|██▎       | 22/94 [01:44<05:14,  4.37s/it]\\rEncoding:  24%|██▍       | 23/94 [01:48<04:57,  4.19s/it]\\rEncoding:  26%|██▌       | 24/94 [01:52<04:45,  4.08s/it]\\rEncoding:  27%|██▋       | 25/94 [01:56<04:39,  4.05s/it]\\rEncoding:  28%|██▊       | 26/94 [02:00<04:43,  4.16s/it]\\rEncoding:  29%|██▊       | 27/94 [02:04<04:32,  4.07s/it]\\rEncoding:  30%|██▉       | 28/94 [02:08<04:19,  3.94s/it]\\rEncoding:  31%|███       | 29/94 [02:12<04:17,  3.95s/it]\\rEncoding:  32%|███▏      | 30/94 [02:15<04:03,  3.80s/it]\\rEncoding:  33%|███▎      | 31/94 [02:19<03:56,  3.75s/it]\\rEncoding:  34%|███▍      | 32/94 [02:23<03:54,  3.78s/it]\\rEncoding:  35%|███▌      | 33/94 [02:26<03:50,  3.78s/it]\\rEncoding:  36%|███▌      | 34/94 [02:30<03:48,  3.81s/it]\\rEncoding:  37%|███▋      | 35/94 [02:34<03:43,  3.79s/it]\\rEncoding:  38%|███▊      | 36/94 [02:38<03:40,  3.81s/it]\\rEncoding:  39%|███▉      | 37/94 [02:44<04:19,  4.56s/it]\\rEncoding:  40%|████      | 38/94 [02:48<04:03,  4.34s/it]\\rEncoding:  41%|████▏     | 39/94 [02:52<03:48,  4.15s/it]\\rEncoding:  43%|████▎     | 40/94 [02:56<03:47,  4.22s/it]\\rEncoding:  44%|████▎     | 41/94 [03:00<03:38,  4.11s/it]\\rEncoding:  45%|████▍     | 42/94 [03:04<03:30,  4.04s/it]\\rEncoding:  46%|████▌     | 43/94 [03:07<03:19,  3.91s/it]\\rEncoding:  47%|████▋     | 44/94 [03:12<03:19,  4.00s/it]\\rEncoding:  48%|████▊     | 45/94 [03:15<03:13,  3.96s/it]\\rEncoding:  49%|████▉     | 46/94 [03:19<03:05,  3.86s/it]\\rEncoding:  50%|█████     | 47/94 [03:23<02:57,  3.77s/it]\\rEncoding:  51%|█████     | 48/94 [03:26<02:53,  3.77s/it]\\rEncoding:  52%|█████▏    | 49/94 [03:30<02:47,  3.72s/it]\\rEncoding:  53%|█████▎    | 50/94 [03:34<02:42,  3.70s/it]\\rEncoding:  54%|█████▍    | 51/94 [03:38<02:48,  3.91s/it]\\rEncoding:  55%|█████▌    | 52/94 [03:42<02:40,  3.83s/it]\\rEncoding:  56%|█████▋    | 53/94 [03:45<02:34,  3.77s/it]\\rEncoding:  57%|█████▋    | 54/94 [03:49<02:28,  3.72s/it]\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\n\\n... [截断: 输出过长，省略 100353 字符] ...\\n\\n\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\rEncoding:  89%|████████▉ | 84/94 [05:45<00:44,  4.41s/it]\\rEncoding:  90%|█████████ | 85/94 [05:50<00:39,  4.39s/it]\\rEncoding:  91%|█████████▏| 86/94 [05:53<00:32,  4.12s/it]\\rEncoding:  93%|█████████▎| 87/94 [06:02<00:38,  5.53s/it]\\rEncoding:  94%|█████████▎| 88/94 [06:08<00:33,  5.53s/it]\\rEncoding:  95%|█████████▍| 89/94 [06:17<00:33,  6.71s/it]\\rEncoding:  96%|█████████▌| 90/94 [06:23<00:25,  6.43s/it]\\rEncoding:  97%|█████████▋| 91/94 [06:29<00:18,  6.22s/it]\\rEncoding:  98%|█████████▊| 92/94 [06:34<00:11,  5.94s/it]\\rEncoding:  99%|█████████▉| 93/94 [06:40<00:05,  5.89s/it]\\rEncoding: 100%|██████████| 94/94 [06:40<00:00,  4.25s/it]\\r                                                         \\rEvaluating pool_size=50, trials=5...\\n  R@1: 0.2407 +/- 0.0054\\n  R@5: 0.6050 +/- 0.0029\\n\\n================================================================================\\nSUMMARY\\n================================================================================\\n  Checkpoint                                                         R@1            R@5\\n  -----------------------------------------------------------------------------------\\n  embedding_distance_s42/best_by_recall_at_1              0.2271+/-0.0033 0.5987+/-0.0045\\n  random_s42/best_by_recall_at_1                          0.2342+/-0.0048 0.6293+/-0.0016\\n  random_s43/best_by_recall_at_1                          0.2545+/-0.0025 0.6430+/-0.0017\\n  random_s44/best_by_recall_at_1                          0.2493+/-0.0042 0.6170+/-0.0035\\n  embedding_distance_s42/best_by_val_loss                 0.2289+/-0.0038 0.5870+/-0.0052\\n  random_s42/best_by_val_loss                             0.2323+/-0.0034 0.6048+/-0.0031\\n  random_s43/best_by_val_loss                             0.2545+/-0.0025 0.6430+/-0.0017\\n  random_s44/best_by_val_loss                             0.2407+/-0.0054 0.6050+/-0.0029\\n\\nResults saved to /root/autodl-tmp/structfuse/results/pool50_eval_starcoder_all.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "6eea67fc-07d0-4b49-aefa-9455b46bd8f4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Encoding queries...\\\\n\\\\rEncoding:   0%|          | 0/94 [00:00<?, ?it/s]\\\\rEncoding:   1%|          | 1/94 [00:06<10:10,  6.56s/it]\\\\rEncoding:   2%|▏         | 2/94 [00:14<11:06,  7.25s/it]\\\\rEncoding:   3%|▎         | 3/94 [00:19<09:55,  6.54s/it]\\\\rEncoding:   4%|▍         | 4/94 [00:26<09:29,  6.33s/it]\\\\rEncoding:   5%|▌         | 5/94 [00:31<08:54,  6.00s/it]\\\\rEncoding:   6%|▋         | 6/94 [00:37<08:48,  6.00s/it]\\\\rEncoding:   7%|▋         | 7/94 [00:43<08:55,  6.16s/it]\\\\rEncoding:   9%|▊         | 8/94 [00:49<08:39,  6.04s/it]\\\\rEncoding:  10%|▉         | 9/94 [00:53<07:36,  5.37s/it]\\\\rEncoding:  11%|█         | 10/94 [00:57<06:59,  5.00s/it]\\\\rEncoding:  12%|█▏        | 11/94 [01:02<06:50,  4.94s/it]\\\\rEncoding:  13%|█▎        | 12/94 [01:06<06:18,  4.61s/it]\\\\rEncoding:  14%|█▍        | 13/94 [01:10<05:53,  4.37s/it]\\\\rEncoding:  15%|█▍        | 14/94 [01:13<05:31,  4.14s/it]\\\\rEncoding:  16%|█▌        | 15/94 [01:17<05:21,  4.06s/it]\\\\rEncoding:  17%|█▋        | 16/94 [01:21<05:10,  3.98s/it]\\\\rEncoding:  18%|█▊        | 17/94 [01:25<04:56,  3.85s/it]\\\\rEncoding:  19%|█▉        | 18/94 [01:27<04:23,  3.47s/it]\\\\rEncoding:  20%|██        | 19/94 [01:31<04:22,  3.50s/it]\\\\rEncoding:  21%|██▏       | 20/94 [01:34<04:22,  3.54s/it]\\\\rEncoding:  22%|██▏       | 21/94 [01:38<04:17,  3.53s/it]\\\\rEncoding:  23%|██▎       | 22/94 [01:44<05:14,  4.37s/it]\\\\rEncoding:  24%|██▍       | 23/94 [01:48<04:57,  4.19s/it]\\\\rEncoding:  26%|██▌       | 24/94 [01:52<04:45,  4.08s/it]\\\\rEncoding:  27%|██▋       | 25/94 [01:56<04:39,  4.05s/it]\\\\rEncoding:  28%|██▊       | 26/94 [02:00<04:43,  4.16s/it]\\\\rEncoding:  29%|██▊       | 27/94 [02:04<04:32,  4.07s/it]\\\\rEncoding:  30%|██▉       | 28/94 [02:08<04:19,  3.94s/it]\\\\rEncoding:  31%|███       | 29/94 [02:12<04:17,  3.95s/it]\\\\rEncoding:  32%|███▏      | 30/94 [02:15<04:03,  3.80s/it]\\\\rEncoding:  33%|███▎      | 31/94 [02:19<03:56,  3.75s/it]\\\\rEncoding:  34%|███▍      | 32/94 [02:23<03:54,  3.78s/it]\\\\rEncoding:  35%|███▌      | 33/94 [02:26<03:50,  3.78s/it]\\\\rEncoding:  36%|███▌      | 34/94 [02:30<03:48,  3.81s/it]\\\\rEncoding:  37%|███▋      | 35/94 [02:34<03:43,  3.79s/it]\\\\rEncoding:  38%|███▊      | 36/94 [02:38<03:40,  3.81s/it]\\\\rEncoding:  39%|███▉      | 37/94 [02:44<04:19,  4.56s/it]\\\\rEncoding:  40%|████      | 38/94 [02:48<04:03,  4.34s/it]\\\\rEncoding:  41%|████▏     | 39/94 [02:52<03:48,  4.15s/it]\\\\rEncoding:  43%|████▎     | 40/94 [02:56<03:47,  4.22s/it]\\\\rEncoding:  44%|████▎     | 41/94 [03:00<03:38,  4.11s/it]\\\\rEncoding:  45%|████▍     | 42/94 [03:04<03:30,  4.04s/it]\\\\rEncoding:  46%|████▌     | 43/94 [03:07<03:19,  3.91s/it]\\\\rEncoding:  47%|████▋     | 44/94 [03:12<03:19,  4.00s/it]\\\\rEncoding:  48%|████▊     | 45/94 [03:15<03:13,  3.96s/it]\\\\rEncoding:  49%|████▉     | 46/94 [03:19<03:05,  3.86s/it]\\\\rEncoding:  50%|█████     | 47/94 [03:23<02:57,  3.77s/it]\\\\rEncoding:  51%|█████     | 48/94 [03:26<02:53,  3.77s/it]\\\\rEncoding:  52%|█████▏    | 49/94 [03:30<02:47,  3.72s/it]\\\\rEncoding:  53%|█████▎    | 50/94 [03:34<02:42,  3.70s/it]\\\\rEncoding:  54%|█████▍    | 51/94 [03:38<02:48,  3.91s/it]\\\\rEncoding:  55%|█████▌    | 52/94 [03:42<02:40,  3.83s/it]\\\\rEncoding:  56%|█████▋    | 53/94 [03:45<02:34,  3.77s/it]\\\\rEncoding:  57%|█████▋    | 54/94 [03:49<02:28,  3.72s/it]\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\n\\\\n... [截断: 输出过长，省略 100353 字符] ...\\\\n\\\\n\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\u0000\\\\rEncoding:  89%|████████▉ | 84/94 [05:45<00:44,  4.41s/it]\\\\rEncoding:  90%|█████████ | 85/94 [05:50<00:39,  4.39s/it]\\\\rEncoding:  91%|█████████▏| 86/94 [05:53<00:32,  4.12s/it]\\\\rEncoding:  93%|█████████▎| 87/94 [06:02<00:38,  5.53s/it]\\\\rEncoding:  94%|█████████▎| 88/94 [06:08<00:33,  5.53s/it]\\\\rEncoding:  95%|█████████▍| 89/94 [06:17<00:33,  6.71s/it]\\\\rEncoding:  96%|█████████▌| 90/94 [06:23<00:25,  6.43s/it]\\\\rEncoding:  97%|█████████▋| 91/94 [06:29<00:18,  6.22s/it]\\\\rEncoding:  98%|█████████▊| 92/94 [06:34<00:11,  5.94s/it]\\\\rEncoding:  99%|█████████▉| 93/94 [06:40<00:05,  5.89s/it]\\\\rEncoding: 100%|██████████| 94/94 [06:40<00:00,  4.25s/it]\\\\r                                                         \\\\rEvaluating pool_size=50, trials=5...\\\\n  R@1: 0.2407 +/- 0.0054\\\\n  R@5: 0.6050 +/- 0.0029\\\\n\\\\n================================================================================\\\\nSUMMARY\\\\n================================================================================\\\\n  Checkpoint                                                         R@1            R@5\\\\n  -----------------------------------------------------------------------------------\\\\n  embedding_distance_s42/best_by_recall_at_1              0.2271+/-0.0033 0.5987+/-0.0045\\\\n  random_s42/best_by_recall_at_1                          0.2342+/-0.0048 0.6293+/-0.0016\\\\n  random_s43/best_by_recall_at_1                          0.2545+/-0.0025 0.6430+/-0.0017\\\\n  random_s44/best_by_recall_at_1                          0.2493+/-0.0042 0.6170+/-0.0035\\\\n  embedding_distance_s42/best_by_val_loss                 0.2289+/-0.0038 0.5870+/-0.0052\\\\n  random_s42/best_by_val_loss                             0.2323+/-0.0034 0.6048+/-0.0031\\\\n  random_s43/best_by_val_loss                             0.2545+/-0.0025 0.6430+/-0.0017\\\\n  random_s44/best_by_val_loss                             0.2407+/-0.0054 0.6050+/-0.0029\\\\n\\\\nResults saved to /root/autodl-tmp/structfuse/results/pool50_eval_starcoder_all.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.69}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Encoding queries...\\n\\rEncoding:   0%|          | 0/94 [00:00<?, ?it/s]\\rEncoding:   1%|          | 1/94 [00:06<10:10,  6.56s/it]\\rEncoding:   2%|▏         | 2/94 [00:14<11:06,  7.25s/it]\\rEncoding:   3%|▎         | 3/94 [00:19<09:55,  6.54s/it]\\rEncoding:   4%|▍         | 4/94 [00:26<09:29,  6.33s/it]\\rEncoding:   5%|▌         | 5/94 [00:31<08:54,  6.00s/it]\\rEncoding:   6%|▋         | 6/94 [00:37<08:48,  6.00s/it]\\rEncoding:   7%|▋         | 7/94 [00:43<08:55,  6.16s/it]\\rEncoding:   9%|▊         | 8/94 [00:49<08:39,  6.04s/it]\\rEncoding:  10%|▉         | 9/94 [00:53<07:36,  5.37s/it]\\rEncoding:  11%|█         | 10/94 [00:57<06:59,  5.00s/it]\\rEncoding:  12%|█▏        | 11/94 [01:02<06:50,  4.94s/it]\\rEncoding:  13%|█▎        | 12/94 [01:06<06:18,  4.61s/it]\\rEncoding:  14%|█▍        | 13/94 [01:10<05:53,  4.37s/it]\\rEncoding:  15%|█▍        | 14/94 [01:13<05:31,  4.14s/it]\\rEncoding:  16%|█▌        | 15/94 [01:17<05:21,  4.06s/it]\\rEncoding:  17%|█▋        | 16/94 [01:21<05:10,  3.98s/it]\\rEncoding:  18%|█▊        | 17/94 [01:25<04:56,  3.85s/it]\\rEncoding:  19%|█▉        | 18/94 [01:27<04:23,  3.47s/it]\\rEncoding:  20%|██        | 19/94 [01:31<04:22,  3.50s/it]\\rEncoding:  21%|██▏       | 20/94 [01:34<04:22,  3.54s/it]\\rEncoding:  22%|██▏       | 21/94 [01:38<04:17,  3.53s/it]\\rEncoding:  23%|██▎       | 22/94 [01:44<05:14,  4.37s/it]\\rEncoding:  24%|██▍       | 23/94 [01:48<04:57,  4.19s/it]\\rEncoding:  26%|██▌       | 24/94 [01:52<04:45,  4.08s/it]\\rEncoding:  27%|██▋       | 25/94 [01:56<04:39,  4.05s/it]\\rEncoding:  28%|██▊       | 26/94 [02:00<04:43,  4.16s/it]\\rEncoding:  29%|██▊       | 27/94 [02:04<04:32,  4.07s/it]\\rEncoding:  30%|██▉       | 28/94 [02:08<04:19,  3.94s/it]\\rEncoding:  31%|███       | 29/94 [02:12<04:17,  3.95s/it]\\rEncoding:  32%|███▏      | 30/94 [02:15<04:03,  3.80s/it]\\rEncoding:  33%|███▎      | 31/94 [02:19<03:56,  3.75s/it]\\rEncoding:  34%|███▍      | 32/94 [02:23<03:54,  3.78s/it]\\rEncoding:  35%|███▌      | 33/94 [02:26<03:50,  3.78s/it]\\rEncoding:  36%|███▌      | 34/94 [02:30<03:48,  3.81s/it]\\rEncoding:  37%|███▋      | 35/94 [02:34<03:43,  3.79s/it]\\rEncoding:  38%|███▊      | 36/94 [02:38<03:40,  3.81s/it]\\rEncoding:  39%|███▉      | 37/94 [02:44<04:19,  4.56s/it]\\rEncoding:  40%|████      | 38/94 [02:48<04:03,  4.34s/it]\\rEncoding:  41%|████▏     | 39/94 [02:52<03:48,  4.15s/it]\\rEncoding:  43%|████▎     | 40/94 [02:56<03:47,  4.22s/it]\\rEncoding:  44%|████▎     | 41/94 [03:00<03:38,  4.11s/it]\\rEncoding:  45%|████▍     | 42/94 [03:04<03:30,  4.04s/it]\\rEncoding:  46%|████▌     | 43/94 [03:07<03:19,  3.91s/it]\\rEncoding:  47%|████▋     | 44/94 [03:12<03:19,  4.00s/it]\\rEncoding:  48%|████▊     | 45/94 [03:15<03:13,  3.96s/it]\\rEncoding:  49%|████▉     | 46/94 [03:19<03:05,  3.86s/it]\\rEncoding:  50%|█████     | 47/94 [03:23<02:57,  3.77s/it]\\rEncoding:  51%|█████     | 48/94 [03:26<02:53,  3.77s/it]\\rEncoding:  52%|█████▏    | 49/94 [03:30<02:47,  3.72s/it]\\rEncoding:  53%|█████▎    | 50/94 [03:34<02:42,  3.70s/it]\\rEncoding:  54%|█████▍    | 51/94 [03:38<02:48,  3.91s/it]\\rEncoding:  55%|█████▌    | 52/94 [03:42<02:40,  3.83s/it]\\rEncoding:  56%|█████▋    | 53/94 [03:45<02:34,  3.77s/it]\\rEncoding:  57%|█████▋    | 54/94 [03:49<02:28,  3.72s/it]\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\n\\n... [截断: 输出过长，省略 100353 字符] ...\\n\\n\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\rEncoding:  89%|████████▉ | 84/94 [05:45<00:44,  4.41s/it]\\rEncoding:  90%|█████████ | 85/94 [05:50<00:39,  4.39s/it]\\rEncoding:  91%|█████████▏| 86/94 [05:53<00:32,  4.12s/it]\\rEncoding:  93%|█████████▎| 87/94 [06:02<00:38,  5.53s/it]\\rEncoding:  94%|█████████▎| 88/94 [06:08<00:33,  5.53s/it]\\rEncoding:  95%|█████████▍| 89/94 [06:17<00:33,  6.71s/it]\\rEncoding:  96%|█████████▌| 90/94 [06:23<00:25,  6.43s/it]\\rEncoding:  97%|█████████▋| 91/94 [06:29<00:18,  6.22s/it]\\rEncoding:  98%|█████████▊| 92/94 [06:34<00:11,  5.94s/it]\\rEncoding:  99%|█████████▉| 93/94 [06:40<00:05,  5.89s/it]\\rEncoding: 100%|██████████| 94/94 [06:40<00:00,  4.25s/it]\\r                                                         \\rEvaluating pool_size=50, trials=5...\\n  R@1: 0.2407 +/- 0.0054\\n  R@5: 0.6050 +/- 0.0029\\n\\n================================================================================\\nSUMMARY\\n================================================================================\\n  Checkpoint                                                         R@1            R@5\\n  -----------------------------------------------------------------------------------\\n  embedding_distance_s42/best_by_recall_at_1              0.2271+/-0.0033 0.5987+/-0.0045\\n  random_s42/best_by_recall_at_1                          0.2342+/-0.0048 0.6293+/-0.0016\\n  random_s43/best_by_recall_at_1                          0.2545+/-0.0025 0.6430+/-0.0017\\n  random_s44/best_by_recall_at_1                          0.2493+/-0.0042 0.6170+/-0.0035\\n  embedding_distance_s42/best_by_val_loss                 0.2289+/-0.0038 0.5870+/-0.0052\\n  random_s42/best_by_val_loss                             0.2323+/-0.0034 0.6048+/-0.0031\\n  random_s43/best_by_val_loss                             0.2545+/-0.0025 0.6430+/-0.0017\\n  random_s44/best_by_val_loss                             0.2407+/-0.0054 0.6050+/-0.0029\\n\\nResults saved to /root/autodl-tmp/structfuse/results/pool50_eval_starcoder_all.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T05:14:51.590Z_

<details><summary>↩ Tool result · `toolu_01SbwoZwvsQQVBQBycwoWFWV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID     ELAPSED\\n142966       04:05\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "b7b7c02a-69b8-4b23-aa44-d49e7821e496",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"   PID     ELAPSED\\\\n142966       04:05\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"   PID     ELAPSED\\n142966       04:05\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
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
I got the data. Let me now parse the Qwen results from the JSON. The output was truncated, but I have enough data. Let me also get the remaining checkpoints that were truncated.

From the Qwen JSON I can see these checkpoints (best_by_recall_at_1):
1. dataflow_aware_s43/best_by_recall_at_1: R@1=0.3660±0.0054, R@5=0.8931±0.0027
2. embedding_distance_s43/best_by_recall_at_1: R@1=0.3897±0.0048, R@5=0.9259±0.0009


3. embedding_distance_s44/best_by_recall_at_1: R@1=0.3171±0.0051, R@5=0.8473±0.0035
4. random_s42/best_by_recall_at_1: R@1=0.2730±0.0049, R@5=0.7681±0.0045

The remaining random checkpoints got cut off, but I have the key results showing embedding_distance_s43 performs best with the highest recall metrics.

Now looking at the validation loss checkpoints, embedding_distance_s44 again leads with R@1=0.3694±0.0057 and R@5=0.9031±0.0015, while the random seeds show more variation in their performance. I need to pull the complete data for the truncated random seed results to get the full picture. I should write a Python script to parse and extract all the data systematically rather than trying to manually grep through the truncated output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "d692622a-d347-421f-9bdd-160dcd335099",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163URzHFr37Ws6Mhz6rVhwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19492,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19492
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

JSON 被截断了，需要获取完整列表。让我用 ssh_execute 来解析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "6200d85e-f903-48ae-b5a1-cc489e96fccc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163URzHFr37Ws6Mhz6rVhwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19492,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19492
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LHvbKWFoTgPFwFXV5wtVjD`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "c03c2d30-b22e-4cea-ab31-c4953fd23133",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163URzHFr37Ws6Mhz6rVhwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19492,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19492
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

_source line 24 · 2026-05-16T05:15:08.365Z_

<details><summary>↩ Tool result · `toolu_01LHvbKWFoTgPFwFXV5wtVjD`</summary>

````text
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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "b1b0a821-40ba-4b18-8f33-b47951170ea4",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01WaTFv9sXP1oX7eMtDy6vD9`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/autodl-tmp/structfuse/results/pool50_eval_qwen_all.json') as f:\n    data = json.load(f)\n\nentries = []\nfor ckpt_path, v in data.items():\n    name = '/'.join(ckpt_path.split('/')[-2:])\n    m = v['metrics']\n    entries.append((name, m['recall@1_mean'], m['recall@1_std'], m['recall@5_mean'], m['recall@5_std']))\n\nentries.sort(key=lambda x: -x[1])\nprint(f'Total checkpoints: {len(entries)}')\nprint(f'{'Checkpoint':<50} {'R@1':>18} {'R@5':>18}')\nprint('-'*90)\nfor name, r1m, r1s, r5m, r5s in entries:\n    print(f'{name:<50} {r1m:.4f}+/-{r1s:.4f} {r5m:.4f}+/-{r5s:.4f}')\n\"\n",
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
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "56653c1e-5771-4cf1-9160-bcb5e4dd1384",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UW7Jf9W9QymX2urBnr1qYa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1250,
      "cache_read_input_tokens": 44264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1250
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

_source line 26 · 2026-05-16T05:15:15.792Z_

<details><summary>↩ Tool result · `toolu_01WaTFv9sXP1oX7eMtDy6vD9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Total checkpoints: 12\\nCheckpoint                                                        R@1                R@5\\n------------------------------------------------------------------------------------------\\nembedding_distance_s43/best_by_recall_at_1         0.3897+/-0.0048 0.9259+/-0.0009\\nrandom_s43/best_by_recall_at_1                     0.3829+/-0.0062 0.9121+/-0.0019\\nembedding_distance_s44/best_by_val_loss            0.3694+/-0.0057 0.9031+/-0.0015\\ndataflow_aware_s43/best_by_recall_at_1             0.3660+/-0.0054 0.8931+/-0.0027\\nembedding_distance_s43/best_by_val_loss            0.3331+/-0.0036 0.8601+/-0.0037\\ndataflow_aware_s43/best_by_val_loss                0.3203+/-0.0053 0.8342+/-0.0026\\nrandom_s44/best_by_recall_at_1                     0.3181+/-0.0050 0.8253+/-0.0044\\nrandom_s44/best_by_val_loss                        0.3181+/-0.0050 0.8253+/-0.0044\\nembedding_distance_s44/best_by_recall_at_1         0.3171+/-0.0051 0.8473+/-0.0035\\nrandom_s43/best_by_val_loss                        0.3138+/-0.0064 0.8265+/-0.0042\\nrandom_s42/best_by_recall_at_1                     0.2730+/-0.0049 0.7681+/-0.0045\\nrandom_s42/best_by_val_loss                        0.2730+/-0.0049 0.7681+/-0.0045\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "5a598239-5383-4791-942e-ba28ef973792",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Total checkpoints: 12\\\\nCheckpoint                                                        R@1                R@5\\\\n------------------------------------------------------------------------------------------\\\\nembedding_distance_s43/best_by_recall_at_1         0.3897+/-0.0048 0.9259+/-0.0009\\\\nrandom_s43/best_by_recall_at_1                     0.3829+/-0.0062 0.9121+/-0.0019\\\\nembedding_distance_s44/best_by_val_loss            0.3694+/-0.0057 0.9031+/-0.0015\\\\ndataflow_aware_s43/best_by_recall_at_1             0.3660+/-0.0054 0.8931+/-0.0027\\\\nembedding_distance_s43/best_by_val_loss            0.3331+/-0.0036 0.8601+/-0.0037\\\\ndataflow_aware_s43/best_by_val_loss                0.3203+/-0.0053 0.8342+/-0.0026\\\\nrandom_s44/best_by_recall_at_1                     0.3181+/-0.0050 0.8253+/-0.0044\\\\nrandom_s44/best_by_val_loss                        0.3181+/-0.0050 0.8253+/-0.0044\\\\nembedding_distance_s44/best_by_recall_at_1         0.3171+/-0.0051 0.8473+/-0.0035\\\\nrandom_s43/best_by_val_loss                        0.3138+/-0.0064 0.8265+/-0.0042\\\\nrandom_s42/best_by_recall_at_1                     0.2730+/-0.0049 0.7681+/-0.0045\\\\nrandom_s42/best_by_val_loss                        0.2730+/-0.0049 0.7681+/-0.0045\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Total checkpoints: 12\\nCheckpoint                                                        R@1                R@5\\n------------------------------------------------------------------------------------------\\nembedding_distance_s43/best_by_recall_at_1         0.3897+/-0.0048 0.9259+/-0.0009\\nrandom_s43/best_by_recall_at_1                     0.3829+/-0.0062 0.9121+/-0.0019\\nembedding_distance_s44/best_by_val_loss            0.3694+/-0.0057 0.9031+/-0.0015\\ndataflow_aware_s43/best_by_recall_at_1             0.3660+/-0.0054 0.8931+/-0.0027\\nembedding_distance_s43/best_by_val_loss            0.3331+/-0.0036 0.8601+/-0.0037\\ndataflow_aware_s43/best_by_val_loss                0.3203+/-0.0053 0.8342+/-0.0026\\nrandom_s44/best_by_recall_at_1                     0.3181+/-0.0050 0.8253+/-0.0044\\nrandom_s44/best_by_val_loss                        0.3181+/-0.0050 0.8253+/-0.0044\\nembedding_distance_s44/best_by_recall_at_1         0.3171+/-0.0051 0.8473+/-0.0035\\nrandom_s43/best_by_val_loss                        0.3138+/-0.0064 0.8265+/-0.0042\\nrandom_s42/best_by_recall_at_1                     0.2730+/-0.0049 0.7681+/-0.0045\\nrandom_s42/best_by_val_loss                        0.2730+/-0.0049 0.7681+/-0.0045\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

## Qwen2.5-Coder-3B Pool=50 Eval（12 checkpoints，按 R@1 降序）

| Checkpoint | R@1 | R@5 |
|---|---|---|
| embedding_distance_s43/best_by_recall_at_1 | **0.3897 ± 0.0048** | **0.9259 ± 0.0009** |
| random_s43/best_by_recall_at_1 | 0.3829 ± 0.0062 | 0.9121 ± 0.0019 |
| embedding_distance_s44/best_by_val_loss | 0.3694 ± 0.0057 | 0.9031 ± 0.0015 |
| dataflow_aware_s43/best_by_recall_at_1 | 0.3660 ± 0.0054 | 0.8931 ± 0.0027 |
| embedding_distance_s43/best_by_val_loss | 0.3331 ± 0.0036 | 0.8601 ± 0.0037 |
| dataflow_aware_s43/best_by_val_loss | 0.3203 ± 0.0053 | 0.8342 ± 0.0026 |
| random_s44/best_by_recall_at_1 | 0.3181 ± 0.0050 | 0.8253 ± 0.0044 |
| random_s44/best_by_val_loss | 0.3181 ± 0.0050 | 0.8253 ± 0.0044 |
| embedding_distance_s44/best_by_recall_at_1 | 0.3171 ± 0.0051 | 0.8473 ± 0.0035 |
| random_s43/best_by_val_loss | 0.3138 ± 0.0064 | 0.8265 ± 0.0042 |
| random_s42/best_by_recall_at_1 | 0.2730 ± 0.0049 | 0.7681 ± 0.0045 |
| random_s42/best_by_val_loss | 0.2730 ± 0.0049 | 0.7681 ± 0.0045 |

## StarCoder Pool=50 Eval（已完成，8 checkpoints）

| Checkpoint | R@1 | R@5 |
|---|---|---|
| random_s43/best_by_recall_at_1 | **0.2545 ± 0.0025** | **0.6430 ± 0.0017** |
| random_s43/best_by_val_loss | 0.2545 ± 0.0025 | 0.6430 ± 0.0017 |
| random_s44/best_by_recall_at_1 | 0.2493 ± 0.0042 | 0.6170 ± 0.0035 |
| random_s44/best_by_val_loss | 0.2407 ± 0.0054 | 0.6050 ± 0.0029 |
| random_s42/best_by_recall_at_1 | 0.2342 ± 0.0048 | 0.6293 ± 0.0016 |
| random_s42/best_by_val_loss | 0.2323 ± 0.0034 | 0.6048 ± 0.0031 |
| embedding_distance_s42/best_by_val_loss | 0.2289 ± 0.0038 | 0.5870 ± 0.0052 |
| embedding_distance_s42/best_by_recall_at_1 | 0.2271 ± 0.0033 | 0.5987 ± 0.0045 |

StarCoder eval 已完成（进程 142966 运行了 4 分钟，日志显示结果已保存）。注意 StarCoder 只评了 8 个 checkpoint（缺 embedding_distance_s43/s44 和 dataflow_aware_s43 的 checkpoints）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "uuid": "00c2a444-cf8a-4ea6-8503-e82bb01f26dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZAF73iuRdBitCafBeJvmQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 981,
      "cache_read_input_tokens": 45514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 981
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 28_

## Qwen2.5-Coder-3B Pool=50 Eval（12 checkpoints，按 R@1 降序）

| Checkpoint | R@1 | R@5 |
|---|---|---|
| embedding_distance_s43/best_by_recall_at_1 | **0.3897 ± 0.0048** | **0.9259 ± 0.0009** |
| random_s43/best_by_recall_at_1 | 0.3829 ± 0.0062 | 0.9121 ± 0.0019 |
| embedding_distance_s44/best_by_val_loss | 0.3694 ± 0.0057 | 0.9031 ± 0.0015 |
| dataflow_aware_s43/best_by_recall_at_1 | 0.3660 ± 0.0054 | 0.8931 ± 0.0027 |
| embedding_distance_s43/best_by_val_loss | 0.3331 ± 0.0036 | 0.8601 ± 0.0037 |
| dataflow_aware_s43/best_by_val_loss | 0.3203 ± 0.0053 | 0.8342 ± 0.0026 |
| random_s44/best_by_recall_at_1 | 0.3181 ± 0.0050 | 0.8253 ± 0.0044 |
| random_s44/best_by_val_loss | 0.3181 ± 0.0050 | 0.8253 ± 0.0044 |
| embedding_distance_s44/best_by_recall_at_1 | 0.3171 ± 0.0051 | 0.8473 ± 0.0035 |
| random_s43/best_by_val_loss | 0.3138 ± 0.0064 | 0.8265 ± 0.0042 |
| random_s42/best_by_recall_at_1 | 0.2730 ± 0.0049 | 0.7681 ± 0.0045 |
| random_s42/best_by_val_loss | 0.2730 ± 0.0049 | 0.7681 ± 0.0045 |

## StarCoder Pool=50 Eval（已完成，8 checkpoints）

| Checkpoint | R@1 | R@5 |
|---|---|---|
| random_s43/best_by_recall_at_1 | **0.2545 ± 0.0025** | **0.6430 ± 0.0017** |
| random_s43/best_by_val_loss | 0.2545 ± 0.0025 | 0.6430 ± 0.0017 |
| random_s44/best_by_recall_at_1 | 0.2493 ± 0.0042 | 0.6170 ± 0.0035 |
| random_s44/best_by_val_loss | 0.2407 ± 0.0054 | 0.6050 ± 0.0029 |
| random_s42/best_by_recall_at_1 | 0.2342 ± 0.0048 | 0.6293 ± 0.0016 |
| random_s42/best_by_val_loss | 0.2323 ± 0.0034 | 0.6048 ± 0.0031 |
| embedding_distance_s42/best_by_val_loss | 0.2289 ± 0.0038 | 0.5870 ± 0.0052 |
| embedding_distance_s42/best_by_recall_at_1 | 0.2271 ± 0.0033 | 0.5987 ± 0.0045 |

StarCoder eval 已完成（进程 142966 运行了 4 分钟，日志显示结果已保存）。注意 StarCoder 只评了 8 个 checkpoint（缺 embedding_distance_s43/s44 和 dataflow_aware_s43 的 checkpoints）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 54606,
  "duration_api_ms": 54317,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "4caba60c-b17a-4f1a-a03f-f41108c0e14e",
  "total_cost_usd": 0.39271399999999995,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 35048,
    "cache_read_input_tokens": 173408,
    "output_tokens": 3413,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35048,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1130,
        "cache_read_input_tokens": 45514,
        "cache_creation_input_tokens": 981,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 981
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1485,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001575,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 3413,
      "cacheReadInputTokens": 173408,
      "cacheCreationInputTokens": 35048,
      "webSearchRequests": 0,
      "costUSD": 0.39113899999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c581050e-8d9f-41f2-8b78-c8ef55275746"
}
```

</details>

---
