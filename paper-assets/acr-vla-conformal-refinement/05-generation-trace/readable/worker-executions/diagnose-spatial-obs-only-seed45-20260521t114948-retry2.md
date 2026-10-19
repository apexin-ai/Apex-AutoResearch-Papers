# diagnose spatial obs only seed45 20260521T114948 retry2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_diagnose_spatial-obs-only-seed45_20260521T114948_retry2.log`
- **Structured JSON:** [`b7ea533e7ede1948f4ab.json`](../../sessions/b7/b7ea533e7ede1948f4ab.json)

## Before a recorded user message

31 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
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
  "uuid": "e14ca97e-b59d-407c-ace5-9d633535932f",
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
    "status": "allowed_warning",
    "resetsAt": 1779584400,
    "rateLimitType": "seven_day",
    "utilization": 0.87,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "8a8036d6-6de6-43db-9eab-16ceef67f005",
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58"
}
```

---

### Assistant

_source line 3_

Looking at the task, I need to check the status of the eval-spatial-obs-only-seed45 experiment on server bjb2-28827. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "acc94500-5663-4aa9-a4b1-9129248426de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTMCJbgHr8ZtEDpbPK8J5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11555,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11555
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

_source line 4_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UvtPEv4KWoQy6xs8e5rXk6`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "21ecb603-543c-4eaa-8bda-7d9107e43933",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTMCJbgHr8ZtEDpbPK8J5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11555,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11555
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

_source line 5 · 2026-05-21T11:50:11.687Z_

<details><summary>↩ Tool result · `toolu_01UvtPEv4KWoQy6xs8e5rXk6`</summary>

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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "1ef2916a-4949-4ba2-aa3a-d985112b99cd",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 6_

<details><summary>Logged reasoning block</summary>

```text
Let me first check the registry entry and SSH into the server to check the experiment status in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "790bcf94-e4c6-468d-b687-3b5bc582cd5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhYXtYv2CkSutFypzhaZNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
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

_source line 7_

Checking registry and server status in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "be65d9f2-e256-425f-a102-c566b534c1f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhYXtYv2CkSutFypzhaZNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01UrAQcm2JVYKJXbhNywZrgp`</summary>

```json
{
  "filters": {
    "exp_id": "eval-spatial-obs-only-seed45"
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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "33fdd16f-a1db-446d-b8d3-e1beaf92df97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhYXtYv2CkSutFypzhaZNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LgseSTmSQWjGgvLv4Ap4CR`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps aux | grep evaluate | grep -v grep",
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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "fc7eb870-d694-4e76-898d-77d744d4c2fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhYXtYv2CkSutFypzhaZNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UYELvkKUvxL9aSLbkt16xW`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45*",
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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "93f11c5b-5e34-4a8c-89a9-6686af96fa50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhYXtYv2CkSutFypzhaZNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015ZUimu1mSm3yL7ds39aqup`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/runs/acr-vla-conformal-refinement/eval-spatial-obs-only-seed45*",
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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "e239c148-5e0f-4b0e-bb53-5e460d8fb866",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhYXtYv2CkSutFypzhaZNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
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

_source line 12 · 2026-05-21T11:50:20.424Z_

<details><summary>↩ Tool result · `toolu_01UrAQcm2JVYKJXbhNywZrgp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.3025}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "f66eb59f-0fd0-4b4f-b5c1-7275ef70250f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.3025}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.3025}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T11:50:20.444Z_

<details><summary>↩ Tool result · `toolu_01LgseSTmSQWjGgvLv4Ap4CR`</summary>

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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "c83f1ed0-bbaa-42e9-96d9-accb20d7c300",
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

_source line 14 · 2026-05-21T11:50:21.255Z_

<details><summary>↩ Tool result · `toolu_01UYELvkKUvxL9aSLbkt16xW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1696 May 21 16:48 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json\\n-rw-r--r-- 1 root root 4937 May 21 16:48 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "07ea0403-f884-46f8-a9d0-0b8b3f0f3f27",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 1696 May 21 16:48 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json\\\\n-rw-r--r-- 1 root root 4937 May 21 16:48 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.79}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1696 May 21 16:48 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json\\n-rw-r--r-- 1 root root 4937 May 21 16:48 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T11:50:21.637Z_

<details><summary>↩ Tool result · `toolu_015ZUimu1mSm3yL7ds39aqup`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/runs/acr-vla-conformal-refinement/eval-spatial-obs-only-seed45*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "ba7d0339-7661-43b6-a48e-78803353d128",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/runs/acr-vla-conformal-refinement/eval-spatial-obs-only-seed45*': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/runs/acr-vla-conformal-refinement/eval-spatial-obs-only-seed45*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.37}}"
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
OK so:
1. Registry filter by exp_id returned 0 results - maybe the filter syntax is wrong. Let me try without filter or with a different approach.
2. The pipe command was blocked - need to use grep directly without pipe.
3. Log files exist at `/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json` and `.log` — both dated May 21 16:48, so recent.
4. No files at ~/runs/ path.

Let me check the log content and JSON results, and also check for the process differently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "99e8cdc3-3b28-439d-97e5-f97fe8296bd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SATi51JW1Z54fUTQj3gDf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1078,
      "cache_read_input_tokens": 24705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1078
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

Log files exist (dated today 16:48). Let me check their contents and the process status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "8a4952df-410c-48e4-95a7-0964c5975dab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SATi51JW1Z54fUTQj3gDf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1078,
      "cache_read_input_tokens": 24705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1078
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TPS8NxJCwpDxkN5cxyiUq9`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -50 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log",
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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "5bdadf4f-003d-4dd8-b358-964a1f532ea5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SATi51JW1Z54fUTQj3gDf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1078,
      "cache_read_input_tokens": 24705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1078
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

_source line 19 · 2026-05-21T11:50:28.588Z_

<details><summary>↩ Tool result · `toolu_01TPS8NxJCwpDxkN5cxyiUq9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 45, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_spatial_obs_only_seed45.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: crm_obs_only, benchmark: spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  44%|████▍     | 214/489 [00:00<00:00, 2136.82it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 2472.31it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 4/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 9/10\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 90.0% (9/10)\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 9/10\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 90.0% (9/10)\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10/10, success so far: 0/10\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 0.0% (0/10)\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/10, success so far: 2/5\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10/10, success so far: 4/10\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 40.0% (4/10)\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/10, success so far: 1/10\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 10.0% (1/10)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 0/10\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/10)\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 5/10, success so far: 4/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 10/10, success so far: 8/10\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 80.0% (8/10)\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 10/10, success so far: 0/10\\n[pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate] success rate: 0.0% (0/10)\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 5/10, success so far: 1/5\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 10/10, success so far: 3/10\\n[pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate] success rate: 30.0% (3/10)\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/10, success so far: 0/10\\n[pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 0.0% (0/10)\\n\\n============================================================\\nOverall success rate (crm_obs_only): 34.0% (34/100)\\n============================================================\\n[eval] Results saved to logs/eval_spatial_obs_only_seed45.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "5d64af40-35a7-433f-b6c3-4a559c1db577",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 45, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_spatial_obs_only_seed45.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\\\n[eval] Mode: crm_obs_only, benchmark: spatial\\\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\\\n\\\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\\\rLoading weights:  44%|████▍     | 214/489 [00:00<00:00, 2136.82it/s]\\\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 2472.31it/s]\\\\nReducing the number of VLM layers to 16 ...\\\\nLoading weights from local directory\\\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)\\\\n[eval] Override max_correction_norm = 0.2\\\\n[eval] Loading LIBERO spatial environments...\\\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n[eval] 10 tasks loaded.\\\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 4/5\\\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 9/10\\\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 90.0% (9/10)\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 5/5\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 9/10\\\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 90.0% (9/10)\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10/10, success so far: 0/10\\\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 0.0% (0/10)\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/10, success so far: 2/5\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10/10, success so far: 4/10\\\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 40.0% (4/10)\\\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/10, success so far: 1/10\\\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 10.0% (1/10)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 0/10\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/10)\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 5/10, success so far: 4/5\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 10/10, success so far: 8/10\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 80.0% (8/10)\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 10/10, success so far: 0/10\\\\n[pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate] success rate: 0.0% (0/10)\\\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 5/10, success so far: 1/5\\\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 10/10, success so far: 3/10\\\\n[pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate] success rate: 30.0% (3/10)\\\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/10, success so far: 0/10\\\\n[pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 0.0% (0/10)\\\\n\\\\n============================================================\\\\nOverall success rate (crm_obs_only): 34.0% (34/100)\\\\n============================================================\\\\n[eval] Results saved to logs/eval_spatial_obs_only_seed45.json\\\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.33}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 45, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_spatial_obs_only_seed45.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: crm_obs_only, benchmark: spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  44%|████▍     | 214/489 [00:00<00:00, 2136.82it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 2472.31it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 4/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 9/10\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 90.0% (9/10)\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 9/10\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 90.0% (9/10)\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10/10, success so far: 0/10\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 0.0% (0/10)\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/10, success so far: 2/5\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10/10, success so far: 4/10\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 40.0% (4/10)\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/10, success so far: 1/10\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 10.0% (1/10)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 0/10\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/10)\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 5/10, success so far: 4/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 10/10, success so far: 8/10\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 80.0% (8/10)\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 10/10, success so far: 0/10\\n[pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate] success rate: 0.0% (0/10)\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 5/10, success so far: 1/5\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 10/10, success so far: 3/10\\n[pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate] success rate: 30.0% (3/10)\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/10, success so far: 0/5\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/10, success so far: 0/10\\n[pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 0.0% (0/10)\\n\\n============================================================\\nOverall success rate (crm_obs_only): 34.0% (34/100)\\n============================================================\\n[eval] Results saved to logs/eval_spatial_obs_only_seed45.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015wsQ9q6tjzD9ASptL3asYF`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json",
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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "361fc7b5-542e-4c0b-9a7d-38dabd10602e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SATi51JW1Z54fUTQj3gDf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1078,
      "cache_read_input_tokens": 24705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1078
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

_source line 21 · 2026-05-21T11:50:29.529Z_

<details><summary>↩ Tool result · `toolu_015wsQ9q6tjzD9ASptL3asYF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.34,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "e12f6205-8e1e-48df-a439-886ebbee39c4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"crm_obs_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"spatial\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.34,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 9,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 9,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.4,\\\\n      \\\\\\\"successes\\\\\\\": 4,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n      \\\\\\\"successes\\\\\\\": 1,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 8,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n      \\\\\\\"successes\\\\\\\": 3,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.33}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.34,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E9koJ3ji4ZADg4M6fCo1vn`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -r evaluate /proc/*/cmdline 2>/dev/null",
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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "fe03a7ce-d413-4c07-b392-1f28c750a3b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SATi51JW1Z54fUTQj3gDf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1078,
      "cache_read_input_tokens": 24705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1078
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

_source line 23 · 2026-05-21T11:50:30.105Z_

<details><summary>↩ Tool result · `toolu_01E9koJ3ji4ZADg4M6fCo1vn`</summary>

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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "23eb3596-40fd-4840-86ed-63e827641048",
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

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_018sHM8om3PE1RY4cBmkhWxt`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": 20,
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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "fdb8e3d6-0a47-4c94-b1ea-d2e7485a5ef9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SATi51JW1Z54fUTQj3gDf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1078,
      "cache_read_input_tokens": 24705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1078
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

_source line 25 · 2026-05-21T11:50:33.064Z_

<details><summary>↩ Tool result · `toolu_018sHM8om3PE1RY4cBmkhWxt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-spatial-obs-only-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:09:30.589Z\", \"updated_at\": \"2026-05-21T11:50:24.015Z\", \"hypothesis\": \"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_seed45.json\", \"server\": \"bjb2-28827\", \"seed\": 45, \"model_name\": \"crm_obs_only\", \"data_path\": \"spatial\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\"}, \"notes\": \"Cron false-positive: marked failed but actually completed successfully. Overall SR 34.0% (34/100) on LIBERO-Spatial with crm_obs_only mode (K=10, max_correction_norm=0.2). Output: /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json. Per-task: between_plate_ramekin=90%, next_to_ramekin=90%, table_center=0%, on_cookie_box=40%, in_top_drawer=10%, on_ramekin=0%, next_to_cookie_box=80%, on_stove=0%, next_to_plate=30%, on_wooden_cabinet=0%.\", \"reproduce\": {\"finished_at\": \"2026-05-21T11:48:53.463Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:49:04.204Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:49:25.607190+00:00\"}]}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"metrics\": {\"overall_sr\": 0.34, \"per_task_sr\": [0.9, 0.9, 0, 0.4, 0.1, 0, 0.8, 0, 0.3, 0], \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10}}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:19.985Z\", \"updated_at\": \"2026-05-21T11:50:10.568Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 44 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"983472\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44.log\", \"submitted_at\": \"2026-05-21T10:18:46.979Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5204.2, \"gpu_hours\": 1.45}, \"reproduce\": {\"finished_at\": \"2026-05-21T11:40:10.658Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:40:31.815288+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44.log\", \"checkpoint_path\": \"N/A (eval only)\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:45:31.175Z\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:17.435Z\", \"updated_at\": \"2026-05-21T11:49:59.821Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 43 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"983128\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43.log\", \"submitted_at\": \"2026-05-21T10:18:36.208Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5206.7, \"gpu_hours\": 1.45}, \"reproduce\": {\"finished_at\": \"2026-05-21T11:39:39.042Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:39:59.242083+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43.log\", \"checkpoint_path\": \"N/A (eval only)\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:45:22.888Z\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:14.823Z\", \"updated_at\": \"2026-05-21T11:49:55.157Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 42 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"982849\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42.log\", \"submitted_at\": \"2026-05-21T10:18:26.307Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5205.3, \"gpu_hours\": 1.45}, \"reproduce\": {\"finished_at\": \"2026-05-21T11:38:56.784Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:39:24.095528+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42.log\", \"checkpoint_path\": \"N/A (eval only)\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:45:11.623Z\", \"notes\": \"ANOMALY: 0% SR (0/200) across all 10 tasks. Prior quick verify on bjb2-40593 showed 72% (50 rollouts) with identical code/model/deps. Code, model weights (7.47GB), normalizer files, torch 2.10.0+cu128, lerobot 0.5.2, transformers 5.8.0 all verified identical between servers. SmolVLA works fine on bjb1-32546 (12% vla_only). Root cause unknown — possible GPU arch bfloat16 difference or hidden env issue. NEEDS RE-RUN ON bjb2-40593.\"}, \"eval-pi05-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:27.768Z\", \"updated_at\": \"2026-05-21T11:46:53.337Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed44, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 44 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"984515\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed44.log\", \"submitted_at\": \"2026-05-21T10:19:17.220Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5220.7, \"gpu_hours\": 1.45}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:46:17.927Z\", \"notes\": \"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}, \"eval-pi05-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:25.180Z\", \"updated_at\": \"2026-05-21T11:46:50.878Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed43, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 43 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"984171\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed43.log\", \"submitted_at\": \"2026-05-21T10:19:07.725Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5214.7, \"gpu_hours\": 1.45}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:46:02.380Z\", \"notes\": \"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}, \"eval-pi05-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:22.540Z\", \"updated_at\": \"2026-05-21T11:46:42.183Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed42, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 42 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"983816\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed42.log\", \"submitted_at\": \"2026-05-21T10:18:57.361Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5212.1, \"gpu_hours\": 1.45}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:45:49.413Z\", \"notes\": \"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Stdout buffering may hide further progress. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:30:28.663Z\", \"updated_at\": \"2026-05-21T08:02:33.602Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→MEAN_STD normalization mismatch that caused 0% SR in r1.\", \"parent\": \"eval-pi05-baseline-object-seed42\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python3 -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --K 10 --output_file logs/eval_pi05_baseline_object_seed42_r2.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"811001\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-baseline-object-seed42-r2.log\", \"submitted_at\": \"2026-05-21T03:30:45.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"KILLED (旧策略 action[0] only). 后续修复历程: (1) action queue fix → bbq_sauce 0/5 (2) vision tower 确认正确加载 (3) 图像 180° 翻转修复 (torch.flip dims=[2,3]) → **Quick verify SR=72%** 修复成功！根因: 官方 lerobot 对图像做 NCHW 180° 旋转，我们的 wrapper 缺失此步骤。\", \"reproduce\": {\"finished_at\": \"2026-05-21T04:53:21.758Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T04:53:36.626571+00:00\"}]}, \"conclusion\": \"killed\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:50.702Z\", \"updated_at\": \"2026-05-21T07:30:47.255Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 707148, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-21T07:30:47.255Z\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:46.321Z\", \"updated_at\": \"2026-05-21T07:30:42.676Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 706941, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-21T07:30:42.676Z\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:41.832Z\", \"updated_at\": \"2026-05-21T07:30:37.114Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": 873171, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-21T07:30:37.114Z\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:55.095Z\", \"updated_at\": \"2026-05-21T07:30:32.202Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 45 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_object_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 23401, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-21T07:30:32.202Z\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:50:21.016Z\", \"updated_at\": \"2026-05-21T05:22:58.984Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": 975409, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-adaptive-k-spatial-p90-seed44-bjb2.log\", \"submitted_at\": \"2026-05-20T13:50:48.545Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"model_name\": \"CRM_obs_only_adaptive_k\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 55922.2, \"gpu_hours\": 15.53}, \"reproduce\": {\"finished_at\": \"2026-05-21T05:22:43.825Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T05:22:50.761Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:23:07.915783+00:00\"}]}}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:14:31.173Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 642428, \"seed\": 66, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.03 --seed 66 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_obs_only_v3_norm\", \"seed\": 66, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (eval only)\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/autodl-tmp/logs/norm003_seed66.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T05:14:21.920Z\", \"metrics\": {\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}, \"notes\": \"[2026-05-21] 成功完成全部 10 task × 20 rollouts = 200。SR=11.5% (23/200)。Log: /root/autodl-tmp/logs/norm003_seed66.log (bjb1-18228, PID 642428, cuda:0)\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:14:00.886Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 642775, \"seed\": 66, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.1 --seed 66 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_obs_only_v3_norm\", \"seed\": 66, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (eval only)\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/autodl-tmp/logs/norm01_seed66.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T05:13:24.858Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T05:13:35.464Z\", \"metrics\": {\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:14:12.689293+00:00\"}]}}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:13:12.047Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 642506, \"seed\": 66, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.05 --seed 66 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"SmolVLA-base\", \"seed\": 66}, \"notes\": \"[2026-05-21 修正] 之前的\\\"task 9/10 异常退出\\\"判断错误。实际进程跑完了全部 10 个 task (20 rollouts each, 共 200)，JSON 已生成: logs/eval_object_crm_obs_only_norm0.05_seed66.json。SR=11.0% (22/200)。原 conclusion=failed 已修正为 success。Log: /root/autodl-tmp/logs/norm005_seed66.log (bjb1-18228)。\", \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-21T05:10:14.887Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-21T05:10:23.876Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:10:47.214816+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T05:10:29.526Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 969788, \"seed\": 67, \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:5\"}, \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\", \"log_path\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"reproduce\": {\"finished_at\": \"2026-05-21T04:59:55.277Z\"}, \"completed_at\": \"2026-05-21T04:59:59.475Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:00:37.585302+00:00\"}]}}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-21T05:07:12.893Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json\", \"completed_at\": \"2026-05-20T22:04:43.969Z\"}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:31:55.966Z\", \"updated_at\": \"2026-05-21T05:07:10.342Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"484257\", \"log_path\": \"logs/eval-k20-obs-only-object-seed43.log\", \"submitted_at\": \"2026-05-20T15:32:00Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA + CRM obs_only (K=20, norm02)\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 6686.0, \"gpu_hours\": 1.86}, \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed43. K sweep for plan_601: tests whether more candidates improve CRM selection quality.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed43.log\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-20T17:23:26.043Z\"}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:33:50.688Z\", \"updated_at\": \"2026-05-21T05:07:08.046Z\", \"hypothesis\": \"K=20 sweep for obs_only CRM on LIBERO-Object seed42 (plan_601). Testing whether doubling K from 10 to 20 further improves correction quality.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"421434\", \"log_path\": \"logs/eval_k20_obs_only_object_seed42.json\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_K20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"status\": \"DONE\", \"metrics\": {\"sr\": 0.2}, \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed42.log\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-20T17:24:50.263Z\"}}, \"count\": 20, \"total\": 567, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3647}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "b9bc2598-b1b6-439a-9bbf-60f9430a723b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-spatial-obs-only-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T07:09:30.589Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:50:24.015Z\\\", \\\"hypothesis\\\": \\\"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_seed45.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"seed\\\": 45, \\\"model_name\\\": \\\"crm_obs_only\\\", \\\"data_path\\\": \\\"spatial\\\", \\\"data_count\\\": 10, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"spatial\\\"}, \\\"notes\\\": \\\"Cron false-positive: marked failed but actually completed successfully. Overall SR 34.0% (34/100) on LIBERO-Spatial with crm_obs_only mode (K=10, max_correction_norm=0.2). Output: /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json. Per-task: between_plate_ramekin=90%, next_to_ramekin=90%, table_center=0%, on_cookie_box=40%, in_top_drawer=10%, on_ramekin=0%, next_to_cookie_box=80%, on_stove=0%, next_to_plate=30%, on_wooden_cabinet=0%.\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T11:48:53.463Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-21T11:49:04.204Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T11:49:25.607190+00:00\\\"}]}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.34, \\\"per_task_sr\\\": [0.9, 0.9, 0, 0.4, 0.1, 0, 0.8, 0, 0.3, 0], \\\"total_rollouts\\\": 100, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 10}}, \\\"eval-pi05-vla-only-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T08:22:19.985Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:50:10.568Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 44 --K 10\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"983472\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44.log\\\", \\\"submitted_at\\\": \\\"2026-05-21T10:18:46.979Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 5204.2, \\\"gpu_hours\\\": 1.45}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T11:40:10.658Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T11:40:31.815288+00:00\\\"}]}, \\\"log_path\\\": \\\"/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"per_task_sr\\\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \\\"total_rollouts\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-21T11:45:31.175Z\\\", \\\"notes\\\": \\\"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\\\"}, \\\"eval-pi05-vla-only-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T08:22:17.435Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:49:59.821Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 43 --K 10\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"983128\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43.log\\\", \\\"submitted_at\\\": \\\"2026-05-21T10:18:36.208Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 5206.7, \\\"gpu_hours\\\": 1.45}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T11:39:39.042Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T11:39:59.242083+00:00\\\"}]}, \\\"log_path\\\": \\\"/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"per_task_sr\\\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \\\"total_rollouts\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-21T11:45:22.888Z\\\", \\\"notes\\\": \\\"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\\\"}, \\\"eval-pi05-vla-only-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T08:22:14.823Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:49:55.157Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 42 --K 10\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"982849\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-21T10:18:26.307Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 5205.3, \\\"gpu_hours\\\": 1.45}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T11:38:56.784Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T11:39:24.095528+00:00\\\"}]}, \\\"log_path\\\": \\\"/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"per_task_sr\\\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \\\"total_rollouts\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-21T11:45:11.623Z\\\", \\\"notes\\\": \\\"ANOMALY: 0% SR (0/200) across all 10 tasks. Prior quick verify on bjb2-40593 showed 72% (50 rollouts) with identical code/model/deps. Code, model weights (7.47GB), normalizer files, torch 2.10.0+cu128, lerobot 0.5.2, transformers 5.8.0 all verified identical between servers. SmolVLA works fine on bjb1-32546 (12% vla_only). Root cause unknown — possible GPU arch bfloat16 difference or hidden env issue. NEEDS RE-RUN ON bjb2-40593.\\\"}, \\\"eval-pi05-vla-only-spatial-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T08:22:27.768Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:46:53.337Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Spatial seed44, cross-VLA validation of CRM\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 44 --K 10\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"984515\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed44.log\\\", \\\"submitted_at\\\": \\\"2026-05-21T10:19:17.220Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 5220.7, \\\"gpu_hours\\\": 1.45}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-21T11:46:17.927Z\\\", \\\"notes\\\": \\\"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\\\"}, \\\"eval-pi05-vla-only-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T08:22:25.180Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:46:50.878Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Spatial seed43, cross-VLA validation of CRM\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 43 --K 10\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"984171\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed43.log\\\", \\\"submitted_at\\\": \\\"2026-05-21T10:19:07.725Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 5214.7, \\\"gpu_hours\\\": 1.45}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-21T11:46:02.380Z\\\", \\\"notes\\\": \\\"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\\\"}, \\\"eval-pi05-vla-only-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T08:22:22.540Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:46:42.183Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Spatial seed42, cross-VLA validation of CRM\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 42 --K 10\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"983816\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-21T10:18:57.361Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 5212.1, \\\"gpu_hours\\\": 1.45}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-21T11:45:49.413Z\\\", \\\"notes\\\": \\\"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Stdout buffering may hide further progress. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\\\"}, \\\"eval-pi05-baseline-object-seed42-r2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T03:30:28.663Z\\\", \\\"updated_at\\\": \\\"2026-05-21T08:02:33.602Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→MEAN_STD normalization mismatch that caused 0% SR in r1.\\\", \\\"parent\\\": \\\"eval-pi05-baseline-object-seed42\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python3 -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --K 10 --output_file logs/eval_pi05_baseline_object_seed42_r2.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"811001\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-pi05-baseline-object-seed42-r2.log\\\", \\\"submitted_at\\\": \\\"2026-05-21T03:30:45.775Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"notes\\\": \\\"KILLED (旧策略 action[0] only). 后续修复历程: (1) action queue fix → bbq_sauce 0/5 (2) vision tower 确认正确加载 (3) 图像 180° 翻转修复 (torch.flip dims=[2,3]) → **Quick verify SR=72%** 修复成功！根因: 官方 lerobot 对图像做 NCHW 180° 旋转，我们的 wrapper 缺失此步骤。\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T04:53:21.758Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T04:53:36.626571+00:00\\\"}]}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-k20-obs-only-spatial-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T06:11:50.702Z\\\", \\\"updated_at\\\": \\\"2026-05-21T07:30:47.255Z\\\", \\\"hypothesis\\\": \\\"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed44.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 707148, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.log\\\", \\\"output_json\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"pi0.5+CRM-obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"K\\\": 20, \\\"max_correction_norm\\\": 0.2, \\\"started_at\\\": \\\"2026-05-21T13:07Z\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.34, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"checkpoint_path\\\": \\\"obs_only_K10_eps02_default\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"completed_at\\\": \\\"2026-05-21T07:30:47.255Z\\\"}, \\\"eval-k20-obs-only-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T06:11:46.321Z\\\", \\\"updated_at\\\": \\\"2026-05-21T07:30:42.676Z\\\", \\\"hypothesis\\\": \\\"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed43.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 706941, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.log\\\", \\\"output_json\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"pi0.5+CRM-obs_only\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"K\\\": 20, \\\"max_correction_norm\\\": 0.2, \\\"started_at\\\": \\\"2026-05-21T13:07Z\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.34, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"checkpoint_path\\\": \\\"obs_only_K10_eps02_default\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"completed_at\\\": \\\"2026-05-21T07:30:42.676Z\\\"}, \\\"eval-k20-obs-only-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T06:11:41.832Z\\\", \\\"updated_at\\\": \\\"2026-05-21T07:30:37.114Z\\\", \\\"hypothesis\\\": \\\"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed42.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 873171, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.log\\\", \\\"output_json\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"pi0.5+CRM-obs_only\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"K\\\": 20, \\\"max_correction_norm\\\": 0.2, \\\"started_at\\\": \\\"2026-05-21T13:07Z\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.35, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"checkpoint_path\\\": \\\"obs_only_K10_eps02_default\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"completed_at\\\": \\\"2026-05-21T07:30:37.114Z\\\"}, \\\"eval-k20-obs-only-object-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T06:11:55.095Z\\\", \\\"updated_at\\\": \\\"2026-05-21T07:30:32.202Z\\\", \\\"hypothesis\\\": \\\"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 45 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_object_seed45.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": 23401, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.log\\\", \\\"output_json\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"pi0.5+CRM-obs_only\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"K\\\": 20, \\\"max_correction_norm\\\": 0.2, \\\"started_at\\\": \\\"2026-05-21T13:07Z\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.19, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"checkpoint_path\\\": \\\"obs_only_K10_eps02_default\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"completed_at\\\": \\\"2026-05-21T07:30:32.202Z\\\"}, \\\"eval-adaptive-k-spatial-p90-seed44-bjb2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T13:50:21.016Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:22:58.984Z\\\", \\\"hypothesis\\\": \\\"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed44.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 975409, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-adaptive-k-spatial-p90-seed44-bjb2.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T13:50:48.545Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"seed\\\": 44, \\\"model_name\\\": \\\"CRM_obs_only_adaptive_k\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"wall_clock_seconds\\\": 55922.2, \\\"gpu_hours\\\": 15.53}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T05:22:43.825Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-21T05:22:50.761Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T05:23:07.915783+00:00\\\"}]}}, \\\"eval-obs-only-object-norm003-seed66\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:30:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:14:31.173Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 642428, \\\"seed\\\": 66, \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.03 --seed 66 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"CRM_obs_only_v3_norm\\\", \\\"seed\\\": 66, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/norm003_seed66.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-21T05:14:21.920Z\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.115, \\\"total_successes\\\": 23, \\\"total_rollouts\\\": 200, \\\"n_rollouts_per_task\\\": 20, \\\"n_tasks\\\": 10, \\\"output_json\\\": \\\"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\\\"}, \\\"notes\\\": \\\"[2026-05-21] 成功完成全部 10 task × 20 rollouts = 200。SR=11.5% (23/200)。Log: /root/autodl-tmp/logs/norm003_seed66.log (bjb1-18228, PID 642428, cuda:0)\\\"}, \\\"eval-obs-only-object-norm01-seed66\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:30:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:14:00.886Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.1 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 642775, \\\"seed\\\": 66, \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.1 --seed 66 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"CRM_obs_only_v3_norm\\\", \\\"seed\\\": 66, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/logs/norm01_seed66.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T05:13:24.858Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-21T05:13:35.464Z\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.135, \\\"total_successes\\\": 27, \\\"total_rollouts\\\": 200, \\\"n_rollouts_per_task\\\": 20, \\\"n_tasks\\\": 10, \\\"output_json\\\": \\\"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T05:14:12.689293+00:00\\\"}]}}, \\\"eval-obs-only-object-norm005-seed66\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:30:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:13:12.047Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 642506, \\\"seed\\\": 66, \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.05 --seed 66 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 10, \\\"model_name\\\": \\\"SmolVLA-base\\\", \\\"seed\\\": 66}, \\\"notes\\\": \\\"[2026-05-21 修正] 之前的\\\\\\\"task 9/10 异常退出\\\\\\\"判断错误。实际进程跑完了全部 10 个 task (20 rollouts each, 共 200)，JSON 已生成: logs/eval_object_crm_obs_only_norm0.05_seed66.json。SR=11.0% (22/200)。原 conclusion=failed 已修正为 success。Log: /root/autodl-tmp/logs/norm005_seed66.log (bjb1-18228)。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T05:10:14.887Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"completed_at\\\": \\\"2026-05-21T05:10:23.876Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T05:10:47.214816+00:00\\\"}]}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.11, \\\"total_successes\\\": 22, \\\"total_rollouts\\\": 200, \\\"n_rollouts_per_task\\\": 20, \\\"n_tasks\\\": 10, \\\"output_json\\\": \\\"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\\\"}}, \\\"eval-obs-only-object-norm003-seed67\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:35:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:10:29.526Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": 969788, \\\"seed\\\": 67, \\\"spec\\\": {\\\"command\\\": \\\"detected on GPU, submitted by prior Worker but not registered\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/acr-vla-conformal-refinement/\\\", \\\"data_count\\\": \\\"100 rollouts\\\", \\\"model_name\\\": \\\"crm_v3_norm/obs_only\\\", \\\"seed\\\": 67, \\\"gpu\\\": \\\"cuda:5\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.14}, \\\"conclusion\\\": \\\"success\\\", \\\"log_path\\\": \\\"/root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T04:59:55.277Z\\\"}, \\\"completed_at\\\": \\\"2026-05-21T04:59:59.475Z\\\", \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T05:00:37.585302+00:00\\\"}]}}, \\\"eval-k20-obs-only-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T17:19:11.419Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:07:12.893Z\\\", \\\"hypothesis\\\": \\\"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed44.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.18}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"log_path\\\": \\\"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json\\\", \\\"completed_at\\\": \\\"2026-05-20T22:04:43.969Z\\\"}, \\\"eval-k20-obs-only-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T15:31:55.966Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:07:10.342Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed43.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"484257\\\", \\\"log_path\\\": \\\"logs/eval-k20-obs-only-object-seed43.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T15:32:00Z\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA + CRM obs_only (K=20, norm02)\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"wall_clock_seconds\\\": 6686.0, \\\"gpu_hours\\\": 1.86}, \\\"hypothesis\\\": \\\"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed43. K sweep for plan_601: tests whether more candidates improve CRM selection quality.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.18}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed43.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"completed_at\\\": \\\"2026-05-20T17:23:26.043Z\\\"}, \\\"eval-k20-obs-only-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T15:33:50.688Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:07:08.046Z\\\", \\\"hypothesis\\\": \\\"K=20 sweep for obs_only CRM on LIBERO-Object seed42 (plan_601). Testing whether doubling K from 10 to 20 further improves correction quality.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed42.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"421434\\\", \\\"log_path\\\": \\\"logs/eval_k20_obs_only_object_seed42.json\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only_K20\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sr\\\": 0.2}, \\\"checkpoint_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.2}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed42.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"completed_at\\\": \\\"2026-05-20T17:24:50.263Z\\\"}}, \\\"count\\\": 20, \\\"total\\\": 567, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.3647}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-spatial-obs-only-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:09:30.589Z\", \"updated_at\": \"2026-05-21T11:50:24.015Z\", \"hypothesis\": \"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_seed45.json\", \"server\": \"bjb2-28827\", \"seed\": 45, \"model_name\": \"crm_obs_only\", \"data_path\": \"spatial\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\"}, \"notes\": \"Cron false-positive: marked failed but actually completed successfully. Overall SR 34.0% (34/100) on LIBERO-Spatial with crm_obs_only mode (K=10, max_correction_norm=0.2). Output: /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json. Per-task: between_plate_ramekin=90%, next_to_ramekin=90%, table_center=0%, on_cookie_box=40%, in_top_drawer=10%, on_ramekin=0%, next_to_cookie_box=80%, on_stove=0%, next_to_plate=30%, on_wooden_cabinet=0%.\", \"reproduce\": {\"finished_at\": \"2026-05-21T11:48:53.463Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:49:04.204Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:49:25.607190+00:00\"}]}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"metrics\": {\"overall_sr\": 0.34, \"per_task_sr\": [0.9, 0.9, 0, 0.4, 0.1, 0, 0.8, 0, 0.3, 0], \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10}}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:19.985Z\", \"updated_at\": \"2026-05-21T11:50:10.568Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 44 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"983472\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44.log\", \"submitted_at\": \"2026-05-21T10:18:46.979Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5204.2, \"gpu_hours\": 1.45}, \"reproduce\": {\"finished_at\": \"2026-05-21T11:40:10.658Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:40:31.815288+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44.log\", \"checkpoint_path\": \"N/A (eval only)\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:45:31.175Z\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:17.435Z\", \"updated_at\": \"2026-05-21T11:49:59.821Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 43 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"983128\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43.log\", \"submitted_at\": \"2026-05-21T10:18:36.208Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5206.7, \"gpu_hours\": 1.45}, \"reproduce\": {\"finished_at\": \"2026-05-21T11:39:39.042Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:39:59.242083+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43.log\", \"checkpoint_path\": \"N/A (eval only)\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:45:22.888Z\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:14.823Z\", \"updated_at\": \"2026-05-21T11:49:55.157Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 42 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"982849\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42.log\", \"submitted_at\": \"2026-05-21T10:18:26.307Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5205.3, \"gpu_hours\": 1.45}, \"reproduce\": {\"finished_at\": \"2026-05-21T11:38:56.784Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:39:24.095528+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42.log\", \"checkpoint_path\": \"N/A (eval only)\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:45:11.623Z\", \"notes\": \"ANOMALY: 0% SR (0/200) across all 10 tasks. Prior quick verify on bjb2-40593 showed 72% (50 rollouts) with identical code/model/deps. Code, model weights (7.47GB), normalizer files, torch 2.10.0+cu128, lerobot 0.5.2, transformers 5.8.0 all verified identical between servers. SmolVLA works fine on bjb1-32546 (12% vla_only). Root cause unknown — possible GPU arch bfloat16 difference or hidden env issue. NEEDS RE-RUN ON bjb2-40593.\"}, \"eval-pi05-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:27.768Z\", \"updated_at\": \"2026-05-21T11:46:53.337Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed44, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 44 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"984515\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed44.log\", \"submitted_at\": \"2026-05-21T10:19:17.220Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5220.7, \"gpu_hours\": 1.45}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:46:17.927Z\", \"notes\": \"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}, \"eval-pi05-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:25.180Z\", \"updated_at\": \"2026-05-21T11:46:50.878Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed43, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 43 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"984171\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed43.log\", \"submitted_at\": \"2026-05-21T10:19:07.725Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5214.7, \"gpu_hours\": 1.45}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:46:02.380Z\", \"notes\": \"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}, \"eval-pi05-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:22.540Z\", \"updated_at\": \"2026-05-21T11:46:42.183Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed42, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark spatial --n_rollouts 20 --seed 42 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"983816\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-spatial-seed42.log\", \"submitted_at\": \"2026-05-21T10:18:57.361Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5212.1, \"gpu_hours\": 1.45}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T11:45:49.413Z\", \"notes\": \"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Stdout buffering may hide further progress. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:30:28.663Z\", \"updated_at\": \"2026-05-21T08:02:33.602Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→MEAN_STD normalization mismatch that caused 0% SR in r1.\", \"parent\": \"eval-pi05-baseline-object-seed42\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python3 -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --K 10 --output_file logs/eval_pi05_baseline_object_seed42_r2.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"811001\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-baseline-object-seed42-r2.log\", \"submitted_at\": \"2026-05-21T03:30:45.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"KILLED (旧策略 action[0] only). 后续修复历程: (1) action queue fix → bbq_sauce 0/5 (2) vision tower 确认正确加载 (3) 图像 180° 翻转修复 (torch.flip dims=[2,3]) → **Quick verify SR=72%** 修复成功！根因: 官方 lerobot 对图像做 NCHW 180° 旋转，我们的 wrapper 缺失此步骤。\", \"reproduce\": {\"finished_at\": \"2026-05-21T04:53:21.758Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T04:53:36.626571+00:00\"}]}, \"conclusion\": \"killed\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:50.702Z\", \"updated_at\": \"2026-05-21T07:30:47.255Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 707148, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-21T07:30:47.255Z\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:46.321Z\", \"updated_at\": \"2026-05-21T07:30:42.676Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 706941, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-21T07:30:42.676Z\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:41.832Z\", \"updated_at\": \"2026-05-21T07:30:37.114Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": 873171, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-21T07:30:37.114Z\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:55.095Z\", \"updated_at\": \"2026-05-21T07:30:32.202Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 45 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_object_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 23401, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-21T07:30:32.202Z\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:50:21.016Z\", \"updated_at\": \"2026-05-21T05:22:58.984Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": 975409, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-adaptive-k-spatial-p90-seed44-bjb2.log\", \"submitted_at\": \"2026-05-20T13:50:48.545Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"model_name\": \"CRM_obs_only_adaptive_k\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 55922.2, \"gpu_hours\": 15.53}, \"reproduce\": {\"finished_at\": \"2026-05-21T05:22:43.825Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T05:22:50.761Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:23:07.915783+00:00\"}]}}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:14:31.173Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 642428, \"seed\": 66, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.03 --seed 66 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_obs_only_v3_norm\", \"seed\": 66, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (eval only)\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/autodl-tmp/logs/norm003_seed66.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T05:14:21.920Z\", \"metrics\": {\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}, \"notes\": \"[2026-05-21] 成功完成全部 10 task × 20 rollouts = 200。SR=11.5% (23/200)。Log: /root/autodl-tmp/logs/norm003_seed66.log (bjb1-18228, PID 642428, cuda:0)\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:14:00.886Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 642775, \"seed\": 66, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.1 --seed 66 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_obs_only_v3_norm\", \"seed\": 66, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (eval only)\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/autodl-tmp/logs/norm01_seed66.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T05:13:24.858Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T05:13:35.464Z\", \"metrics\": {\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:14:12.689293+00:00\"}]}}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:13:12.047Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 642506, \"seed\": 66, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.05 --seed 66 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"SmolVLA-base\", \"seed\": 66}, \"notes\": \"[2026-05-21 修正] 之前的\\\"task 9/10 异常退出\\\"判断错误。实际进程跑完了全部 10 个 task (20 rollouts each, 共 200)，JSON 已生成: logs/eval_object_crm_obs_only_norm0.05_seed66.json。SR=11.0% (22/200)。原 conclusion=failed 已修正为 success。Log: /root/autodl-tmp/logs/norm005_seed66.log (bjb1-18228)。\", \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-21T05:10:14.887Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-21T05:10:23.876Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:10:47.214816+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T05:10:29.526Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 969788, \"seed\": 67, \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:5\"}, \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\", \"log_path\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed67.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"reproduce\": {\"finished_at\": \"2026-05-21T04:59:55.277Z\"}, \"completed_at\": \"2026-05-21T04:59:59.475Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:00:37.585302+00:00\"}]}}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-21T05:07:12.893Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json\", \"completed_at\": \"2026-05-20T22:04:43.969Z\"}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:31:55.966Z\", \"updated_at\": \"2026-05-21T05:07:10.342Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"484257\", \"log_path\": \"logs/eval-k20-obs-only-object-seed43.log\", \"submitted_at\": \"2026-05-20T15:32:00Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA + CRM obs_only (K=20, norm02)\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 6686.0, \"gpu_hours\": 1.86}, \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed43. K sweep for plan_601: tests whether more candidates improve CRM selection quality.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed43.log\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-20T17:23:26.043Z\"}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:33:50.688Z\", \"updated_at\": \"2026-05-21T05:07:08.046Z\", \"hypothesis\": \"K=20 sweep for obs_only CRM on LIBERO-Object seed42 (plan_601). Testing whether doubling K from 10 to 20 further improves correction quality.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"421434\", \"log_path\": \"logs/eval_k20_obs_only_object_seed42.json\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_K20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"status\": \"DONE\", \"metrics\": {\"sr\": 0.2}, \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed42.log\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-20T17:24:50.263Z\"}}, \"count\": 20, \"total\": 567, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3647}}"
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
The registry already shows the experiment has been resolved. Let me check the current state:

1. Registry status: **DONE**, conclusion: **failed** — but the notes say "Cron false-positive: marked failed but actually completed successfully"
2. The log shows the experiment completed successfully with **Overall SR: 34.0% (34/100)**
3. JSON results file exists with full per-task breakdown
4. Metrics are already populated in the registry
5. Log path and checkpoint path are already set

So it looks like someone already resolved this — the registry already has:
- conclusion: "failed" 


- But notes indicate it was a cron false positive and actually completed successfully
- Metrics are filled in: overall_sr=0.34
- log_path and checkpoint_path are set

The real issue here is that the conclusion is marked "failed" when it should reflect the actual outcome. Looking at the crm_obs_only experiment on LIBERO-Spatial seed45, the 34% success rate is consistent with other K=10 Spatial obs_only results, so this is a legitimate result, not a failure.

The registry shows the experiment is DONE with all the data populated, but the conclusion field is wrong. Since the hypothesis was about adding a seed for statistical robustness and the experiment ran to completion with valid metrics, I should update the conclusion to "success" to accurately reflect that it produced the intended results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "6926de4d-c5d3-40b2-99c6-1219a82113e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dytugVq5kd9Dmk1kg1cSu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17356,
      "cache_read_input_tokens": 25783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17356
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

_source line 27_

实验已完成。日志确认全部 10 tasks × 10 rollouts 跑完，**Overall SR = 34.0% (34/100)**。进程正常退出，JSON 结果已生成。Registry 当前 conclusion="failed" 是 cron 误判，需修正。

更新 registry conclusion 为 success：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "11194b3b-7a59-447a-8ce4-2e733405add3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dytugVq5kd9Dmk1kg1cSu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17356,
      "cache_read_input_tokens": 25783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17356
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01PKG2MUkmpJvqDoqJqo8oud`</summary>

```json
{
  "exp_id": "eval-spatial-obs-only-seed45",
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
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "d31c19eb-7bbd-4777-93c4-650be44e1607",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dytugVq5kd9Dmk1kg1cSu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17356,
      "cache_read_input_tokens": 25783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17356
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

_source line 29 · 2026-05-21T11:50:53.121Z_

<details><summary>↩ Tool result · `toolu_01PKG2MUkmpJvqDoqJqo8oud`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-spatial-obs-only-seed45\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:09:30.589Z\", \"updated_at\": \"2026-05-21T11:50:52.186Z\", \"hypothesis\": \"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_seed45.json\", \"server\": \"bjb2-28827\", \"seed\": 45, \"model_name\": \"crm_obs_only\", \"data_path\": \"spatial\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\"}, \"notes\": \"Cron false-positive: marked failed but actually completed successfully. Overall SR 34.0% (34/100) on LIBERO-Spatial with crm_obs_only mode (K=10, max_correction_norm=0.2). Output: /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json. Per-task: between_plate_ramekin=90%, next_to_ramekin=90%, table_center=0%, on_cookie_box=40%, in_top_drawer=10%, on_ramekin=0%, next_to_cookie_box=80%, on_stove=0%, next_to_plate=30%, on_wooden_cabinet=0%.\", \"reproduce\": {\"finished_at\": \"2026-05-21T11:48:53.463Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T11:49:04.204Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:49:25.607190+00:00\"}]}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"metrics\": {\"overall_sr\": 0.34, \"per_task_sr\": [0.9, 0.9, 0, 0.4, 0.1, 0, 0.8, 0, 0.3, 0], \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4441}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "35ee0206-eec0-43cf-93cd-b769a32ec30c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-spatial-obs-only-seed45\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T07:09:30.589Z\\\", \\\"updated_at\\\": \\\"2026-05-21T11:50:52.186Z\\\", \\\"hypothesis\\\": \\\"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_seed45.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"seed\\\": 45, \\\"model_name\\\": \\\"crm_obs_only\\\", \\\"data_path\\\": \\\"spatial\\\", \\\"data_count\\\": 10, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"spatial\\\"}, \\\"notes\\\": \\\"Cron false-positive: marked failed but actually completed successfully. Overall SR 34.0% (34/100) on LIBERO-Spatial with crm_obs_only mode (K=10, max_correction_norm=0.2). Output: /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json. Per-task: between_plate_ramekin=90%, next_to_ramekin=90%, table_center=0%, on_cookie_box=40%, in_top_drawer=10%, on_ramekin=0%, next_to_cookie_box=80%, on_stove=0%, next_to_plate=30%, on_wooden_cabinet=0%.\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T11:48:53.463Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-21T11:49:04.204Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T11:49:25.607190+00:00\\\"}]}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.34, \\\"per_task_sr\\\": [0.9, 0.9, 0, 0.4, 0.1, 0, 0.8, 0, 0.3, 0], \\\"total_rollouts\\\": 100, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 10}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.4441}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-spatial-obs-only-seed45\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:09:30.589Z\", \"updated_at\": \"2026-05-21T11:50:52.186Z\", \"hypothesis\": \"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_seed45.json\", \"server\": \"bjb2-28827\", \"seed\": 45, \"model_name\": \"crm_obs_only\", \"data_path\": \"spatial\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\"}, \"notes\": \"Cron false-positive: marked failed but actually completed successfully. Overall SR 34.0% (34/100) on LIBERO-Spatial with crm_obs_only mode (K=10, max_correction_norm=0.2). Output: /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json. Per-task: between_plate_ramekin=90%, next_to_ramekin=90%, table_center=0%, on_cookie_box=40%, in_top_drawer=10%, on_ramekin=0%, next_to_cookie_box=80%, on_stove=0%, next_to_plate=30%, on_wooden_cabinet=0%.\", \"reproduce\": {\"finished_at\": \"2026-05-21T11:48:53.463Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T11:49:04.204Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:49:25.607190+00:00\"}]}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"metrics\": {\"overall_sr\": 0.34, \"per_task_sr\": [0.9, 0.9, 0, 0.4, 0.1, 0, 0.8, 0, 0.3, 0], \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4441}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

Registry 已修正。总结：

- **状态**：实验正常完成，cron 误判（eval 脚本不写 sentinel/W&B，进程退出后 cron 无法确认）
- **结果**：LIBERO-Spatial crm_obs_only seed45, **SR = 34.0%** (34/100)
- **Per-task**：between_plate_ramekin 90%, next_to_ramekin 90%, next_to_cookie_box 80%, on_cookie_box 40%, next_to_plate 30%, in_top_drawer 10%, table_center/on_ramekin/on_stove/on_wooden_cabinet 均 0%
- **Registry**：conclusion 从 "failed" 修正为 "success"，metrics/log_path/checkpoint_path 此前已正确设置

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "uuid": "9dccd448-8711-4e33-9785-e64269c0465c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155Fto7NhMC2f268ZSnfFpC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 43139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1585
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

_source line 31_

Registry 已修正。总结：

- **状态**：实验正常完成，cron 误判（eval 脚本不写 sentinel/W&B，进程退出后 cron 无法确认）
- **结果**：LIBERO-Spatial crm_obs_only seed45, **SR = 34.0%** (34/100)
- **Per-task**：between_plate_ramekin 90%, next_to_ramekin 90%, next_to_cookie_box 80%, on_cookie_box 40%, next_to_plate 30%, in_top_drawer 10%, table_center/on_ramekin/on_stove/on_wooden_cabinet 均 0%
- **Registry**：conclusion 从 "failed" 修正为 "success"，metrics/log_path/checkpoint_path 此前已正确设置

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 53093,
  "duration_api_ms": 47173,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "07a91267-7f67-4ef2-b0a2-2e50d4db4d58",
  "total_cost_usd": 0.32591475000000003,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 32883,
    "cache_read_input_tokens": 128864,
    "output_tokens": 2183,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32883,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 222,
        "cache_read_input_tokens": 43139,
        "cache_creation_input_tokens": 1585,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1585
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1234,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0013440000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 2183,
      "cacheReadInputTokens": 128864,
      "cacheCreationInputTokens": 32883,
      "webSearchRequests": 0,
      "costUSD": 0.32457075,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bc38c9dd-769b-4847-a1cb-3c3ba42004b3"
}
```

</details>

---
