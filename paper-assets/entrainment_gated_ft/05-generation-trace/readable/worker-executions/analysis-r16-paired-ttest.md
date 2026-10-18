# analysis r16 paired ttest

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_analysis_r16-paired-ttest_20260523T170538.log`
- **Structured JSON:** [`a5fe665cbc38158e3482.json`](../../sessions/a5/a5fe665cbc38158e3482.json)

## Before a recorded user message

46 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
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
  "uuid": "627d04f8-c21e-4a9d-8b64-2b8f64d86018",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/memory/"
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
    "resetsAt": 1779565800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "fd1f53ab-e8ca-409a-a8bd-82af253dd142",
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me search for routing-related data on the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "1b17efab-e3bf-4b5a-a99b-7a9624c4e039",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMrRZyEYCa8VQ6wkroj1DC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12324,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12324
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GpxVr6mCLSRjbWcGgXk1ap`</summary>

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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "6b0c964e-5601-40bf-a204-13bce64505d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMrRZyEYCa8VQ6wkroj1DC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12324,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12324
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 6 · 2026-05-23T17:05:50.565Z_

<details><summary>↩ Tool result · `toolu_01GpxVr6mCLSRjbWcGgXk1ap`</summary>

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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "d7c4d035-c200-4d37-84ec-770e75fc5595",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WR4eJrZRFsjLX2WRMaAZki`</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/results/ -name \"*routing*\" -o -name \"*rescue*\" -o -name \"*threshold*\"",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "2d72c7b2-24cf-4280-bf7b-397f1731b6ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJDAJVU5dtr5Y7i1M3BP8V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 453,
      "cache_read_input_tokens": 24165,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 453
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FQ4Dux3txRMTFVdtaLWRgM`</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/results/ -name \"*split*\"",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "b12a3d98-aaa4-4c77-8855-8d66576670b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJDAJVU5dtr5Y7i1M3BP8V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 453,
      "cache_read_input_tokens": 24165,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 453
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WDhPmYR2J29dzYx7uBuTum`</summary>

```json
{
  "server": "westb-48145",
  "command": "ls -la /root/entrainment_gated_ft/results/",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "12c66e76-244d-4c27-ab17-dcb60d8e0aae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJDAJVU5dtr5Y7i1M3BP8V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 453,
      "cache_read_input_tokens": 24165,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 453
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

_source line 10 · 2026-05-23T17:05:58.931Z_

<details><summary>↩ Tool result · `toolu_01WR4eJrZRFsjLX2WRMaAZki`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.8}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "2d221162-9424-444b-b72c-cbcafcb7c4c9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.8}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.8}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T17:06:01.369Z_

<details><summary>↩ Tool result · `toolu_01FQ4Dux3txRMTFVdtaLWRgM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "8b2b7b5c-e045-4fc6-a115-0b34a0cbd061",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.42}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T17:06:02.282Z_

<details><summary>↩ Tool result · `toolu_01WDhPmYR2J29dzYx7uBuTum`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 136\\ndrwxr-xr-x 13 root root  4096 May 23 05:04 .\\ndrwxr-xr-x 12 root root  4096 May 24 00:46 ..\\ndrwxr-xr-x  2 root root  4096 May 22 16:03 a1_cross_benchmark_jaccard\\ndrwxr-xr-x  2 root root    95 May 22 16:23 a2_prediction_framework\\ndrwxr-xr-x  2 root root  4096 May 22 16:24 a3_complementarity\\n-rw-r--r--  1 root root  5640 May 22 17:59 e1_confidence_selection.json\\n-rw-r--r--  1 root root  8375 May 22 17:59 e2_continuous_jaccard.json\\n-rw-r--r--  1 root root 12556 May 22 18:01 e3_calibration.json\\ndrwxr-xr-x 11 root root  4096 May 22 20:31 e4_pythia_seed\\ndrwxr-xr-x 19 root root  4096 May 23 10:33 exp005_zoo_expansion\\ndrwxr-xr-x  2 root root  4096 May 23 10:38 figures\\ndrwxr-xr-x  3 root root    30 May 18 14:20 func_comp\\ndrwxr-xr-x  3 root root  8192 May 18 15:20 mvp_direct\\ndrwxr-xr-x  2 root root  8192 May 18 15:36 mvp_logprob\\n-rw-r--r--  1 root root 35275 May 18 15:36 mvp_logprob_run.log\\ndrwxr-xr-x  2 root root   110 May 18 15:28 test_logprob\\n-rw-r--r--  1 root root  2397 May 18 15:28 test_logprob_dryrun.log\\ndrwxr-xr-x  3 root root  4096 May 18 14:29 test_run\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.88}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "e8dd5745-bfb9-4816-a084-b6e258b638d1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 136\\\\ndrwxr-xr-x 13 root root  4096 May 23 05:04 .\\\\ndrwxr-xr-x 12 root root  4096 May 24 00:46 ..\\\\ndrwxr-xr-x  2 root root  4096 May 22 16:03 a1_cross_benchmark_jaccard\\\\ndrwxr-xr-x  2 root root    95 May 22 16:23 a2_prediction_framework\\\\ndrwxr-xr-x  2 root root  4096 May 22 16:24 a3_complementarity\\\\n-rw-r--r--  1 root root  5640 May 22 17:59 e1_confidence_selection.json\\\\n-rw-r--r--  1 root root  8375 May 22 17:59 e2_continuous_jaccard.json\\\\n-rw-r--r--  1 root root 12556 May 22 18:01 e3_calibration.json\\\\ndrwxr-xr-x 11 root root  4096 May 22 20:31 e4_pythia_seed\\\\ndrwxr-xr-x 19 root root  4096 May 23 10:33 exp005_zoo_expansion\\\\ndrwxr-xr-x  2 root root  4096 May 23 10:38 figures\\\\ndrwxr-xr-x  3 root root    30 May 18 14:20 func_comp\\\\ndrwxr-xr-x  3 root root  8192 May 18 15:20 mvp_direct\\\\ndrwxr-xr-x  2 root root  8192 May 18 15:36 mvp_logprob\\\\n-rw-r--r--  1 root root 35275 May 18 15:36 mvp_logprob_run.log\\\\ndrwxr-xr-x  2 root root   110 May 18 15:28 test_logprob\\\\n-rw-r--r--  1 root root  2397 May 18 15:28 test_logprob_dryrun.log\\\\ndrwxr-xr-x  3 root root  4096 May 18 14:29 test_run\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.88}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 136\\ndrwxr-xr-x 13 root root  4096 May 23 05:04 .\\ndrwxr-xr-x 12 root root  4096 May 24 00:46 ..\\ndrwxr-xr-x  2 root root  4096 May 22 16:03 a1_cross_benchmark_jaccard\\ndrwxr-xr-x  2 root root    95 May 22 16:23 a2_prediction_framework\\ndrwxr-xr-x  2 root root  4096 May 22 16:24 a3_complementarity\\n-rw-r--r--  1 root root  5640 May 22 17:59 e1_confidence_selection.json\\n-rw-r--r--  1 root root  8375 May 22 17:59 e2_continuous_jaccard.json\\n-rw-r--r--  1 root root 12556 May 22 18:01 e3_calibration.json\\ndrwxr-xr-x 11 root root  4096 May 22 20:31 e4_pythia_seed\\ndrwxr-xr-x 19 root root  4096 May 23 10:33 exp005_zoo_expansion\\ndrwxr-xr-x  2 root root  4096 May 23 10:38 figures\\ndrwxr-xr-x  3 root root    30 May 18 14:20 func_comp\\ndrwxr-xr-x  3 root root  8192 May 18 15:20 mvp_direct\\ndrwxr-xr-x  2 root root  8192 May 18 15:36 mvp_logprob\\n-rw-r--r--  1 root root 35275 May 18 15:36 mvp_logprob_run.log\\ndrwxr-xr-x  2 root root   110 May 18 15:28 test_logprob\\n-rw-r--r--  1 root root  2397 May 18 15:28 test_logprob_dryrun.log\\ndrwxr-xr-x  3 root root  4096 May 18 14:29 test_run\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.88}}"
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
No files matching "routing", "rescue", "threshold", or "split" were found. Let me look more broadly at the results directory structure and check if routing data might be inside the exp005 or other directories, or in the main project code.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "478448eb-bfa8-485d-a231-8ccadc5d4fb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6EiQ99UpVaEEXjaTXpxod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1254,
      "cache_read_input_tokens": 24618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1254
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

没有直接匹配的文件。让我深入查看可能包含 routing 数据的目录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "1747e9cc-0809-4570-a213-9002998bb3c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6EiQ99UpVaEEXjaTXpxod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1254,
      "cache_read_input_tokens": 24618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1254
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RXT5SM2WUdx4kott4j28xN`</summary>

```json
{
  "server": "westb-48145",
  "command": "ls -la /root/entrainment_gated_ft/results/exp005_zoo_expansion/",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "c4f9e600-f268-4f6d-b65b-405bc7bea145",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6EiQ99UpVaEEXjaTXpxod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1254,
      "cache_read_input_tokens": 24618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1254
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HtT6h7Rx3Kk43nDVuCcDHu`</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/results/e1_confidence_selection.json",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "bea89b4d-62ef-4972-878c-901f48b45787",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6EiQ99UpVaEEXjaTXpxod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1254,
      "cache_read_input_tokens": 24618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1254
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

_source line 17 · 2026-05-23T17:06:08.811Z_

<details><summary>↩ Tool result · `toolu_01RXT5SM2WUdx4kott4j28xN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1680\\ndrwxr-xr-x 19 root root   4096 May 23 10:33 .\\ndrwxr-xr-x 13 root root   4096 May 23 05:04 ..\\ndrwxr-xr-x  3 root root     88 May 23 10:26 DeltaNet_h31_hswag_piqa\\ndrwxr-xr-x  3 root root     88 May 23 00:09 DeltaNet_hybrid-3-1\\ndrwxr-xr-x  3 root root     82 May 23 01:13 DeltaNet_pure_baseline\\ndrwxr-xr-x  3 root root     82 May 23 10:32 DeltaNet_pure_hswag_piqa\\ndrwxr-xr-x  3 root root     93 May 23 00:57 GDN_h3-1_lambada\\ndrwxr-xr-x  3 root root     96 May 23 00:55 GDN_pure_lambada\\ndrwxr-xr-x  3 root root     83 May 23 10:16 GLA_h31_hswag_piqa\\ndrwxr-xr-x  3 root root    107 May 23 00:21 GLA_hybrid-3-1\\ndrwxr-xr-x  3 root root     86 May 23 00:41 GLA_pure\\ndrwxr-xr-x  3 root root     86 May 23 00:59 GLA_pure_baseline\\ndrwxr-xr-x  3 root root     86 May 23 10:21 GLA_pure_hswag_piqa\\ndrwxr-xr-x  3 root root     85 May 23 01:07 HGRN2_h3-1_lambada\\ndrwxr-xr-x  3 root root     88 May 23 01:05 HGRN2_pure_lambada\\ndrwxr-xr-x  3 root root     84 May 23 01:47 HGRN_hybrid-3-1\\ndrwxr-xr-x  3 root root     87 May 23 02:05 HGRN_pure_baseline\\ndrwxr-xr-x  3 root root     86 May 23 01:02 RetNet_h3-1_lambada\\ndrwxr-xr-x  3 root root     80 May 23 01:00 RetNet_pure_lambada\\n-rw-r--r--  1 root root  13128 May 23 10:33 analysis_extended.log\\n-rw-r--r--  1 root root  10364 May 23 01:08 analyze_4arch_jaccard.py\\n-rw-r--r--  1 root root  12061 May 23 01:22 analyze_5arch.py\\n-rw-r--r--  1 root root  14264 May 23 10:13 analyze_5arch_extended.py\\n-rw-r--r--  1 root root   8654 May 22 20:39 analyze_6arch.py\\n-rw-r--r--  1 root root  11452 May 23 01:49 analyze_6arch_jaccard.py\\n-rw-r--r--  1 root root   1749 May 23 00:54 bg_downloads.log\\n-rwxr-xr-x  1 root root    902 May 22 23:49 eval_deltanet_hardcode.sh\\n-rw-r--r--  1 root root   9617 May 23 00:47 eval_download.log\\n-rw-r--r--  1 root root   1660 May 23 00:17 eval_fla.py\\n-rwxr-xr-x  1 root root    877 May 22 23:44 eval_gla_hardcode.sh\\n-rwxr-xr-x  1 root root    882 May 22 23:49 eval_hgrn_hardcode.sh\\n-rw-r--r--  1 root root  38528 May 23 00:22 eval_p1.log\\n-rw-r--r--  1 root root   4220 May 22 23:38 gla_eval.log\\n-rw-r--r--  1 root root 365221 May 23 10:32 hellaswag_piqa_eval.log\\n-rw-r--r--  1 root root   3724 May 23 00:32 hgrn_chain.log\\n-rw-r--r--  1 root root  19335 May 23 03:07 hgrn_eval.log\\n-rw-r--r--  1 root root   9995 May 23 01:09 jaccard_4arch.json\\n-rw-r--r--  1 root root  15386 May 23 01:23 jaccard_5arch.json\\n-rw-r--r--  1 root root  31707 May 23 10:33 jaccard_5arch_extended.json\\n-rw-r--r--  1 root root  23651 May 23 02:05 jaccard_6arch.json\\n-rw-r--r--  1 root root    663 May 22 20:48 priority1.log\\n-rw-r--r--  1 root root   3605 May 22 22:15 priority1_v2.log\\n-rw-r--r--  1 root root 291307 May 22 22:48 priority1_v3.log\\n-rw-r--r--  1 root root   6256 May 22 23:17 priority1_v4.log\\n-rw-r--r--  1 root root   6796 May 23 00:13 pure_download_eval.log\\n-rw-r--r--  1 root root   6322 May 23 01:08 pure_v3.log\\n-rw-r--r--  1 root root    354 May 23 00:35 pure_v4.log\\n-rw-r--r--  1 root root   2327 May 23 00:51 pure_v5.log\\n-rw-r--r--  1 root root   5067 May 23 01:00 pure_wget_eval.log\\n-rw-r--r--  1 root root    230 May 22 22:22 run_all.log\\n-rwxr-xr-x  1 root root   2671 May 22 23:58 run_download_eval_pure.sh\\n-rwxr-xr-x  1 root root   4822 May 23 00:30 run_eval_download.sh\\n-rwxr-xr-x  1 root root   2063 May 23 00:16 run_eval_p1.sh\\n-rwxr-xr-x  1 root root   1075 May 23 10:11 run_hellaswag_piqa.sh\\n-rwxr-xr-x  1 root root   2129 May 23 00:27 run_hgrn_chain.sh\\n-rwxr-xr-x  1 root root   1360 May 23 03:03 run_hgrn_eval.sh\\n-rwxr-xr-x  1 root root   3016 May 22 22:49 run_p1_v4.sh\\n-rwxr-xr-x  1 root root   2160 May 22 20:30 run_priority1.sh\\n-rwxr-xr-x  1 root root   2314 May 22 20:46 run_priority1_v2.sh\\n-rwxr-xr-x  1 root root   2548 May 22 20:51 run_priority1_v3.sh\\n-rw-r--r--  1 root root 268144 May 23 02:25 run_pure_v10.log\\n-rwxr-xr-x  1 root root   3307 May 23 01:08 run_pure_v10.sh\\n-rwxr-xr-x  1 root root   3010 May 23 00:32 run_pure_v3.sh\\n-rwxr-xr-x  1 root root   3156 May 23 00:34 run_pure_v4.sh\\n-rwxr-xr-x  1 root root   4189 May 23 00:37 run_pure_v5.sh\\n-rw-r--r--  1 root root    402 May 23 00:55 run_pure_v6.log\\n-rwxr-xr-x  1 root root   1653 May 23 00:55 run_pure_v6.sh\\n-rw-r--r--  1 root root   3709 May 23 00:56 run_pure_v7.log\\n-rwxr-xr-x  1 root root   1649 May 23 00:55 run_pure_v7.sh\\n-rw-r--r--  1 root root  41899 May 23 01:00 run_pure_v8.log\\n-rwxr-xr-x  1 root root   2240 May 23 00:57 run_pure_v8.sh\\n-rw-r--r--  1 root root 303266 May 23 03:00 run_pure_v9.log\\n-rwxr-xr-x  1 root root   3361 May 23 01:03 run_pure_v9.sh\\n-rwxr-xr-x  1 root root   2552 May 23 00:01 run_wget_eval_pure.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.55}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "b35c532b-4b24-4924-86f0-295eca233428",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 1680\\\\ndrwxr-xr-x 19 root root   4096 May 23 10:33 .\\\\ndrwxr-xr-x 13 root root   4096 May 23 05:04 ..\\\\ndrwxr-xr-x  3 root root     88 May 23 10:26 DeltaNet_h31_hswag_piqa\\\\ndrwxr-xr-x  3 root root     88 May 23 00:09 DeltaNet_hybrid-3-1\\\\ndrwxr-xr-x  3 root root     82 May 23 01:13 DeltaNet_pure_baseline\\\\ndrwxr-xr-x  3 root root     82 May 23 10:32 DeltaNet_pure_hswag_piqa\\\\ndrwxr-xr-x  3 root root     93 May 23 00:57 GDN_h3-1_lambada\\\\ndrwxr-xr-x  3 root root     96 May 23 00:55 GDN_pure_lambada\\\\ndrwxr-xr-x  3 root root     83 May 23 10:16 GLA_h31_hswag_piqa\\\\ndrwxr-xr-x  3 root root    107 May 23 00:21 GLA_hybrid-3-1\\\\ndrwxr-xr-x  3 root root     86 May 23 00:41 GLA_pure\\\\ndrwxr-xr-x  3 root root     86 May 23 00:59 GLA_pure_baseline\\\\ndrwxr-xr-x  3 root root     86 May 23 10:21 GLA_pure_hswag_piqa\\\\ndrwxr-xr-x  3 root root     85 May 23 01:07 HGRN2_h3-1_lambada\\\\ndrwxr-xr-x  3 root root     88 May 23 01:05 HGRN2_pure_lambada\\\\ndrwxr-xr-x  3 root root     84 May 23 01:47 HGRN_hybrid-3-1\\\\ndrwxr-xr-x  3 root root     87 May 23 02:05 HGRN_pure_baseline\\\\ndrwxr-xr-x  3 root root     86 May 23 01:02 RetNet_h3-1_lambada\\\\ndrwxr-xr-x  3 root root     80 May 23 01:00 RetNet_pure_lambada\\\\n-rw-r--r--  1 root root  13128 May 23 10:33 analysis_extended.log\\\\n-rw-r--r--  1 root root  10364 May 23 01:08 analyze_4arch_jaccard.py\\\\n-rw-r--r--  1 root root  12061 May 23 01:22 analyze_5arch.py\\\\n-rw-r--r--  1 root root  14264 May 23 10:13 analyze_5arch_extended.py\\\\n-rw-r--r--  1 root root   8654 May 22 20:39 analyze_6arch.py\\\\n-rw-r--r--  1 root root  11452 May 23 01:49 analyze_6arch_jaccard.py\\\\n-rw-r--r--  1 root root   1749 May 23 00:54 bg_downloads.log\\\\n-rwxr-xr-x  1 root root    902 May 22 23:49 eval_deltanet_hardcode.sh\\\\n-rw-r--r--  1 root root   9617 May 23 00:47 eval_download.log\\\\n-rw-r--r--  1 root root   1660 May 23 00:17 eval_fla.py\\\\n-rwxr-xr-x  1 root root    877 May 22 23:44 eval_gla_hardcode.sh\\\\n-rwxr-xr-x  1 root root    882 May 22 23:49 eval_hgrn_hardcode.sh\\\\n-rw-r--r--  1 root root  38528 May 23 00:22 eval_p1.log\\\\n-rw-r--r--  1 root root   4220 May 22 23:38 gla_eval.log\\\\n-rw-r--r--  1 root root 365221 May 23 10:32 hellaswag_piqa_eval.log\\\\n-rw-r--r--  1 root root   3724 May 23 00:32 hgrn_chain.log\\\\n-rw-r--r--  1 root root  19335 May 23 03:07 hgrn_eval.log\\\\n-rw-r--r--  1 root root   9995 May 23 01:09 jaccard_4arch.json\\\\n-rw-r--r--  1 root root  15386 May 23 01:23 jaccard_5arch.json\\\\n-rw-r--r--  1 root root  31707 May 23 10:33 jaccard_5arch_extended.json\\\\n-rw-r--r--  1 root root  23651 May 23 02:05 jaccard_6arch.json\\\\n-rw-r--r--  1 root root    663 May 22 20:48 priority1.log\\\\n-rw-r--r--  1 root root   3605 May 22 22:15 priority1_v2.log\\\\n-rw-r--r--  1 root root 291307 May 22 22:48 priority1_v3.log\\\\n-rw-r--r--  1 root root   6256 May 22 23:17 priority1_v4.log\\\\n-rw-r--r--  1 root root   6796 May 23 00:13 pure_download_eval.log\\\\n-rw-r--r--  1 root root   6322 May 23 01:08 pure_v3.log\\\\n-rw-r--r--  1 root root    354 May 23 00:35 pure_v4.log\\\\n-rw-r--r--  1 root root   2327 May 23 00:51 pure_v5.log\\\\n-rw-r--r--  1 root root   5067 May 23 01:00 pure_wget_eval.log\\\\n-rw-r--r--  1 root root    230 May 22 22:22 run_all.log\\\\n-rwxr-xr-x  1 root root   2671 May 22 23:58 run_download_eval_pure.sh\\\\n-rwxr-xr-x  1 root root   4822 May 23 00:30 run_eval_download.sh\\\\n-rwxr-xr-x  1 root root   2063 May 23 00:16 run_eval_p1.sh\\\\n-rwxr-xr-x  1 root root   1075 May 23 10:11 run_hellaswag_piqa.sh\\\\n-rwxr-xr-x  1 root root   2129 May 23 00:27 run_hgrn_chain.sh\\\\n-rwxr-xr-x  1 root root   1360 May 23 03:03 run_hgrn_eval.sh\\\\n-rwxr-xr-x  1 root root   3016 May 22 22:49 run_p1_v4.sh\\\\n-rwxr-xr-x  1 root root   2160 May 22 20:30 run_priority1.sh\\\\n-rwxr-xr-x  1 root root   2314 May 22 20:46 run_priority1_v2.sh\\\\n-rwxr-xr-x  1 root root   2548 May 22 20:51 run_priority1_v3.sh\\\\n-rw-r--r--  1 root root 268144 May 23 02:25 run_pure_v10.log\\\\n-rwxr-xr-x  1 root root   3307 May 23 01:08 run_pure_v10.sh\\\\n-rwxr-xr-x  1 root root   3010 May 23 00:32 run_pure_v3.sh\\\\n-rwxr-xr-x  1 root root   3156 May 23 00:34 run_pure_v4.sh\\\\n-rwxr-xr-x  1 root root   4189 May 23 00:37 run_pure_v5.sh\\\\n-rw-r--r--  1 root root    402 May 23 00:55 run_pure_v6.log\\\\n-rwxr-xr-x  1 root root   1653 May 23 00:55 run_pure_v6.sh\\\\n-rw-r--r--  1 root root   3709 May 23 00:56 run_pure_v7.log\\\\n-rwxr-xr-x  1 root root   1649 May 23 00:55 run_pure_v7.sh\\\\n-rw-r--r--  1 root root  41899 May 23 01:00 run_pure_v8.log\\\\n-rwxr-xr-x  1 root root   2240 May 23 00:57 run_pure_v8.sh\\\\n-rw-r--r--  1 root root 303266 May 23 03:00 run_pure_v9.log\\\\n-rwxr-xr-x  1 root root   3361 May 23 01:03 run_pure_v9.sh\\\\n-rwxr-xr-x  1 root root   2552 May 23 00:01 run_wget_eval_pure.sh\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.55}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 1680\\ndrwxr-xr-x 19 root root   4096 May 23 10:33 .\\ndrwxr-xr-x 13 root root   4096 May 23 05:04 ..\\ndrwxr-xr-x  3 root root     88 May 23 10:26 DeltaNet_h31_hswag_piqa\\ndrwxr-xr-x  3 root root     88 May 23 00:09 DeltaNet_hybrid-3-1\\ndrwxr-xr-x  3 root root     82 May 23 01:13 DeltaNet_pure_baseline\\ndrwxr-xr-x  3 root root     82 May 23 10:32 DeltaNet_pure_hswag_piqa\\ndrwxr-xr-x  3 root root     93 May 23 00:57 GDN_h3-1_lambada\\ndrwxr-xr-x  3 root root     96 May 23 00:55 GDN_pure_lambada\\ndrwxr-xr-x  3 root root     83 May 23 10:16 GLA_h31_hswag_piqa\\ndrwxr-xr-x  3 root root    107 May 23 00:21 GLA_hybrid-3-1\\ndrwxr-xr-x  3 root root     86 May 23 00:41 GLA_pure\\ndrwxr-xr-x  3 root root     86 May 23 00:59 GLA_pure_baseline\\ndrwxr-xr-x  3 root root     86 May 23 10:21 GLA_pure_hswag_piqa\\ndrwxr-xr-x  3 root root     85 May 23 01:07 HGRN2_h3-1_lambada\\ndrwxr-xr-x  3 root root     88 May 23 01:05 HGRN2_pure_lambada\\ndrwxr-xr-x  3 root root     84 May 23 01:47 HGRN_hybrid-3-1\\ndrwxr-xr-x  3 root root     87 May 23 02:05 HGRN_pure_baseline\\ndrwxr-xr-x  3 root root     86 May 23 01:02 RetNet_h3-1_lambada\\ndrwxr-xr-x  3 root root     80 May 23 01:00 RetNet_pure_lambada\\n-rw-r--r--  1 root root  13128 May 23 10:33 analysis_extended.log\\n-rw-r--r--  1 root root  10364 May 23 01:08 analyze_4arch_jaccard.py\\n-rw-r--r--  1 root root  12061 May 23 01:22 analyze_5arch.py\\n-rw-r--r--  1 root root  14264 May 23 10:13 analyze_5arch_extended.py\\n-rw-r--r--  1 root root   8654 May 22 20:39 analyze_6arch.py\\n-rw-r--r--  1 root root  11452 May 23 01:49 analyze_6arch_jaccard.py\\n-rw-r--r--  1 root root   1749 May 23 00:54 bg_downloads.log\\n-rwxr-xr-x  1 root root    902 May 22 23:49 eval_deltanet_hardcode.sh\\n-rw-r--r--  1 root root   9617 May 23 00:47 eval_download.log\\n-rw-r--r--  1 root root   1660 May 23 00:17 eval_fla.py\\n-rwxr-xr-x  1 root root    877 May 22 23:44 eval_gla_hardcode.sh\\n-rwxr-xr-x  1 root root    882 May 22 23:49 eval_hgrn_hardcode.sh\\n-rw-r--r--  1 root root  38528 May 23 00:22 eval_p1.log\\n-rw-r--r--  1 root root   4220 May 22 23:38 gla_eval.log\\n-rw-r--r--  1 root root 365221 May 23 10:32 hellaswag_piqa_eval.log\\n-rw-r--r--  1 root root   3724 May 23 00:32 hgrn_chain.log\\n-rw-r--r--  1 root root  19335 May 23 03:07 hgrn_eval.log\\n-rw-r--r--  1 root root   9995 May 23 01:09 jaccard_4arch.json\\n-rw-r--r--  1 root root  15386 May 23 01:23 jaccard_5arch.json\\n-rw-r--r--  1 root root  31707 May 23 10:33 jaccard_5arch_extended.json\\n-rw-r--r--  1 root root  23651 May 23 02:05 jaccard_6arch.json\\n-rw-r--r--  1 root root    663 May 22 20:48 priority1.log\\n-rw-r--r--  1 root root   3605 May 22 22:15 priority1_v2.log\\n-rw-r--r--  1 root root 291307 May 22 22:48 priority1_v3.log\\n-rw-r--r--  1 root root   6256 May 22 23:17 priority1_v4.log\\n-rw-r--r--  1 root root   6796 May 23 00:13 pure_download_eval.log\\n-rw-r--r--  1 root root   6322 May 23 01:08 pure_v3.log\\n-rw-r--r--  1 root root    354 May 23 00:35 pure_v4.log\\n-rw-r--r--  1 root root   2327 May 23 00:51 pure_v5.log\\n-rw-r--r--  1 root root   5067 May 23 01:00 pure_wget_eval.log\\n-rw-r--r--  1 root root    230 May 22 22:22 run_all.log\\n-rwxr-xr-x  1 root root   2671 May 22 23:58 run_download_eval_pure.sh\\n-rwxr-xr-x  1 root root   4822 May 23 00:30 run_eval_download.sh\\n-rwxr-xr-x  1 root root   2063 May 23 00:16 run_eval_p1.sh\\n-rwxr-xr-x  1 root root   1075 May 23 10:11 run_hellaswag_piqa.sh\\n-rwxr-xr-x  1 root root   2129 May 23 00:27 run_hgrn_chain.sh\\n-rwxr-xr-x  1 root root   1360 May 23 03:03 run_hgrn_eval.sh\\n-rwxr-xr-x  1 root root   3016 May 22 22:49 run_p1_v4.sh\\n-rwxr-xr-x  1 root root   2160 May 22 20:30 run_priority1.sh\\n-rwxr-xr-x  1 root root   2314 May 22 20:46 run_priority1_v2.sh\\n-rwxr-xr-x  1 root root   2548 May 22 20:51 run_priority1_v3.sh\\n-rw-r--r--  1 root root 268144 May 23 02:25 run_pure_v10.log\\n-rwxr-xr-x  1 root root   3307 May 23 01:08 run_pure_v10.sh\\n-rwxr-xr-x  1 root root   3010 May 23 00:32 run_pure_v3.sh\\n-rwxr-xr-x  1 root root   3156 May 23 00:34 run_pure_v4.sh\\n-rwxr-xr-x  1 root root   4189 May 23 00:37 run_pure_v5.sh\\n-rw-r--r--  1 root root    402 May 23 00:55 run_pure_v6.log\\n-rwxr-xr-x  1 root root   1653 May 23 00:55 run_pure_v6.sh\\n-rw-r--r--  1 root root   3709 May 23 00:56 run_pure_v7.log\\n-rwxr-xr-x  1 root root   1649 May 23 00:55 run_pure_v7.sh\\n-rw-r--r--  1 root root  41899 May 23 01:00 run_pure_v8.log\\n-rwxr-xr-x  1 root root   2240 May 23 00:57 run_pure_v8.sh\\n-rw-r--r--  1 root root 303266 May 23 03:00 run_pure_v9.log\\n-rwxr-xr-x  1 root root   3361 May 23 01:03 run_pure_v9.sh\\n-rwxr-xr-x  1 root root   2552 May 23 00:01 run_wget_eval_pure.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.55}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WYNcEBi6xHMgGtuHSNFJym`</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/ -name \"*.json\" -path \"*/results/*\" -type f",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "8f38220f-3ff0-4c65-ac27-733b692f9133",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6EiQ99UpVaEEXjaTXpxod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1254,
      "cache_read_input_tokens": 24618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1254
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

_source line 19 · 2026-05-23T17:06:11.593Z_

<details><summary>↩ Tool result · `toolu_01HtT6h7Rx3Kk43nDVuCcDHu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"analysis\\\": \\\"e1_confidence_selection\\\",\\n  \\\"date\\\": \\\"2026-05-22\\\",\\n  \\\"method\\\": {\\n    \\\"attention_ratio\\\": \\\"h3-1 (25%)\\\",\\n    \\\"architectures\\\": [\\n      \\\"GDN\\\",\\n      \\\"RetNet\\\",\\n      \\\"HGRN2\\\"\\n    ],\\n    \\\"cv\\\": \\\"50/50 random split x 10 repeats\\\",\\n    \\\"confidence_measure\\\": {\\n      \\\"lambada\\\": \\\"target word loglikelihood\\\",\\n      \\\"hellaswag\\\": \\\"max char-length-normalized loglikelihood\\\",\\n      \\\"piqa\\\": \\\"max raw loglikelihood across choices\\\",\\n      \\\"arc_easy\\\": \\\"max raw loglikelihood across choices\\\"\\n    }\\n  },\\n  \\\"results\\\": {\\n    \\\"lambada\\\": {\\n      \\\"strategies\\\": {\\n        \\\"max_confidence\\\": {\\n          \\\"mean_acc\\\": 0.525378,\\n          \\\"std_acc\\\": 0.006802,\\n          \\\"vs_mv_pp\\\": 1.634,\\n          \\\"vs_best_single_pp\\\": 1.649\\n        },\\n        \\\"rescue_threshold\\\": {\\n          \\\"mean_acc\\\": 0.562321,\\n          \\\"std_acc\\\": 0.005296,\\n          \\\"vs_mv_pp\\\": 5.328,\\n          \\\"vs_best_single_pp\\\": 5.343,\\n          \\\"mean_threshold\\\": 1.7244,\\n          \\\"std_threshold\\\": 0.1688\\n        },\\n        \\\"confidence_weighted\\\": {\\n          \\\"mean_acc\\\": 0.527163,\\n          \\\"std_acc\\\": 0.006393,\\n          \\\"vs_mv_pp\\\": 1.812,\\n          \\\"vs_best_single_pp\\\": 1.828\\n        }\\n      },\\n      \\\"baselines\\\": {\\n        \\\"majority_vote_acc\\\": 0.509042,\\n        \\\"majority_vote_std\\\": 0.005642,\\n        \\\"best_single_acc\\\": 0.508886,\\n        \\\"best_single_std\\\": 0.005018,\\n        \\\"oracle_acc\\\": 0.654637,\\n        \\\"oracle_std\\\": 0.005371,\\n        \\\"random_acc\\\": 0.50683,\\n        \\\"random_std\\\": 0.008304\\n      },\\n      \\\"per_arch\\\": {\\n        \\\"GDN\\\": {\\n          \\\"pure_acc\\\": 0.543373,\\n          \\\"hybrid_acc\\\": 0.513293\\n        },\\n        \\\"RetNet\\\": {\\n          \\\"pure_acc\\\": 0.517369,\\n          \\\"hybrid_acc\\\": 0.502426\\n        },\\n        \\\"HGRN2\\\": {\\n          \\\"pure_acc\\\": 0.48399,\\n          \\\"hybrid_acc\\\": 0.514264\\n        }\\n      },\\n      \\\"n_samples\\\": 5153\\n    },\\n    \\\"hellaswag\\\": {\\n      \\\"strategies\\\": {\\n        \\\"max_confidence\\\": {\\n          \\\"mean_acc\\\": 0.596415,\\n          \\\"std_acc\\\": 0.004721,\\n          \\\"vs_mv_pp\\\": 0.118,\\n          \\\"vs_best_single_pp\\\": -0.44\\n        },\\n        \\\"rescue_threshold\\\": {\\n          \\\"mean_acc\\\": 0.595041,\\n          \\\"std_acc\\\": 0.004511,\\n          \\\"vs_mv_pp\\\": -0.02,\\n          \\\"vs_best_single_pp\\\": -0.578,\\n          \\\"mean_threshold\\\": 0.5435,\\n          \\\"std_threshold\\\": 0.0805\\n        },\\n        \\\"confidence_weighted\\\": {\\n          \\\"mean_acc\\\": 0.59524,\\n          \\\"std_acc\\\": 0.005038,\\n          \\\"vs_mv_pp\\\": 0.0,\\n          \\\"vs_best_single_pp\\\": -0.558\\n        }\\n      },\\n      \\\"baselines\\\": {\\n        \\\"majority_vote_acc\\\": 0.59524,\\n        \\\"majority_vote_std\\\": 0.005038,\\n        \\\"best_single_acc\\\": 0.600817,\\n        \\\"best_single_std\\\": 0.004614,\\n        \\\"oracle_acc\\\": 0.668552,\\n        \\\"oracle_std\\\": 0.005935,\\n        \\\"random_acc\\\": 0.593169,\\n        \\\"random_std\\\": 0.004782\\n      },\\n      \\\"per_arch\\\": {\\n        \\\"GDN\\\": {\\n          \\\"pure_acc\\\": 0.607648,\\n          \\\"hybrid_acc\\\": 0.603167\\n        },\\n        \\\"RetNet\\\": {\\n          \\\"pure_acc\\\": 0.579765,\\n          \\\"hybrid_acc\\\": 0.577674\\n        },\\n        \\\"HGRN2\\\": {\\n          \\\"pure_acc\\\": 0.598984,\\n          \\\"hybrid_acc\\\": 0.603963\\n        }\\n      },\\n      \\\"n_samples\\\": 10042\\n    },\\n    \\\"piqa\\\": {\\n      \\\"strategies\\\": {\\n        \\\"max_confidence\\\": {\\n          \\\"mean_acc\\\": 0.728945,\\n          \\\"std_acc\\\": 0.009303,\\n          \\\"vs_mv_pp\\\": -1.121,\\n          \\\"vs_best_single_pp\\\": -0.272\\n        },\\n        \\\"rescue_threshold\\\": {\\n          \\\"mean_acc\\\": 0.734059,\\n          \\\"std_acc\\\": 0.010268,\\n          \\\"vs_mv_pp\\\": -0.609,\\n          \\\"vs_best_single_pp\\\": 0.239,\\n          \\\"mean_threshold\\\": 70.8392,\\n          \\\"std_threshold\\\": 62.5899\\n        },\\n        \\\"confidence_weighted\\\": {\\n          \\\"mean_acc\\\": 0.730686,\\n          \\\"std_acc\\\": 0.009662,\\n          \\\"vs_mv_pp\\\": -0.947,\\n          \\\"vs_best_single_pp\\\": -0.098\\n        }\\n      },\\n      \\\"baselines\\\": {\\n        \\\"majority_vote_acc\\\": 0.740152,\\n        \\\"majority_vote_std\\\": 0.010581,\\n        \\\"best_single_acc\\\": 0.731665,\\n        \\\"best_single_std\\\": 0.011772,\\n        \\\"oracle_acc\\\": 0.795647,\\n        \\\"oracle_std\\\": 0.01089,\\n        \\\"random_acc\\\": 0.728618,\\n        \\\"random_std\\\": 0.008949\\n      },\\n      \\\"per_arch\\\": {\\n        \\\"GDN\\\": {\\n          \\\"pure_acc\\\": 0.723613,\\n          \\\"hybrid_acc\\\": 0.737758\\n        },\\n        \\\"RetNet\\\": {\\n          \\\"pure_acc\\\": 0.726333,\\n          \\\"hybrid_acc\\\": 0.729053\\n        },\\n        \\\"HGRN2\\\": {\\n          \\\"pure_acc\\\": 0.734494,\\n          \\\"hybrid_acc\\\": 0.730141\\n        }\\n      },\\n      \\\"n_samples\\\": 1838\\n    },\\n    \\\"arc_easy\\\": {\\n      \\\"strategies\\\": {\\n        \\\"max_confidence\\\": {\\n          \\\"mean_acc\\\": 0.710943,\\n          \\\"std_acc\\\": 0.008495,\\n          \\\"vs_mv_pp\\\": 0.471,\\n          \\\"vs_best_single_pp\\\": -0.236\\n        },\\n        \\\"rescue_threshold\\\": {\\n          \\\"mean_acc\\\": 0.716414,\\n          \\\"std_acc\\\": 0.007323,\\n          \\\"vs_mv_pp\\\": 1.019,\\n          \\\"vs_best_single_pp\\\": 0.311,\\n          \\\"mean_threshold\\\": 19.8566,\\n          \\\"std_threshold\\\": 6.608\\n        },\\n        \\\"confidence_weighted\\\": {\\n          \\\"mean_acc\\\": 0.714141,\\n          \\\"std_acc\\\": 0.007671,\\n          \\\"vs_mv_pp\\\": 0.791,\\n          \\\"vs_best_single_pp\\\": 0.084\\n        }\\n      },\\n      \\\"baselines\\\": {\\n        \\\"majority_vote_acc\\\": 0.706229,\\n        \\\"majority_vote_std\\\": 0.005494,\\n        \\\"best_single_acc\\\": 0.7133,\\n        \\\"best_single_std\\\": 0.009897,\\n        \\\"oracle_acc\\\": 0.808418,\\n        \\\"oracle_std\\\": 0.005883,\\n        \\\"random_acc\\\": 0.707407,\\n        \\\"random_std\\\": 0.008846\\n      },\\n      \\\"per_arch\\\": {\\n        \\\"GDN\\\": {\\n          \\\"pure_acc\\\": 0.712121,\\n          \\\"hybrid_acc\\\": 0.708333\\n        },\\n        \\\"RetNet\\\": {\\n          \\\"pure_acc\\\": 0.712963,\\n          \\\"hybrid_acc\\\": 0.696128\\n        },\\n        \\\"HGRN2\\\": {\\n          \\\"pure_acc\\\": 0.712963,\\n          \\\"hybrid_acc\\\": 0.720539\\n        }\\n      },\\n      \\\"n_samples\\\": 2376\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "de3b5fb4-181d-4df3-8ffc-95a604c4544e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"analysis\\\\\\\": \\\\\\\"e1_confidence_selection\\\\\\\",\\\\n  \\\\\\\"date\\\\\\\": \\\\\\\"2026-05-22\\\\\\\",\\\\n  \\\\\\\"method\\\\\\\": {\\\\n    \\\\\\\"attention_ratio\\\\\\\": \\\\\\\"h3-1 (25%)\\\\\\\",\\\\n    \\\\\\\"architectures\\\\\\\": [\\\\n      \\\\\\\"GDN\\\\\\\",\\\\n      \\\\\\\"RetNet\\\\\\\",\\\\n      \\\\\\\"HGRN2\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"cv\\\\\\\": \\\\\\\"50/50 random split x 10 repeats\\\\\\\",\\\\n    \\\\\\\"confidence_measure\\\\\\\": {\\\\n      \\\\\\\"lambada\\\\\\\": \\\\\\\"target word loglikelihood\\\\\\\",\\\\n      \\\\\\\"hellaswag\\\\\\\": \\\\\\\"max char-length-normalized loglikelihood\\\\\\\",\\\\n      \\\\\\\"piqa\\\\\\\": \\\\\\\"max raw loglikelihood across choices\\\\\\\",\\\\n      \\\\\\\"arc_easy\\\\\\\": \\\\\\\"max raw loglikelihood across choices\\\\\\\"\\\\n    }\\\\n  },\\\\n  \\\\\\\"results\\\\\\\": {\\\\n    \\\\\\\"lambada\\\\\\\": {\\\\n      \\\\\\\"strategies\\\\\\\": {\\\\n        \\\\\\\"max_confidence\\\\\\\": {\\\\n          \\\\\\\"mean_acc\\\\\\\": 0.525378,\\\\n          \\\\\\\"std_acc\\\\\\\": 0.006802,\\\\n          \\\\\\\"vs_mv_pp\\\\\\\": 1.634,\\\\n          \\\\\\\"vs_best_single_pp\\\\\\\": 1.649\\\\n        },\\\\n        \\\\\\\"rescue_threshold\\\\\\\": {\\\\n          \\\\\\\"mean_acc\\\\\\\": 0.562321,\\\\n          \\\\\\\"std_acc\\\\\\\": 0.005296,\\\\n          \\\\\\\"vs_mv_pp\\\\\\\": 5.328,\\\\n          \\\\\\\"vs_best_single_pp\\\\\\\": 5.343,\\\\n          \\\\\\\"mean_threshold\\\\\\\": 1.7244,\\\\n          \\\\\\\"std_threshold\\\\\\\": 0.1688\\\\n        },\\\\n        \\\\\\\"confidence_weighted\\\\\\\": {\\\\n          \\\\\\\"mean_acc\\\\\\\": 0.527163,\\\\n          \\\\\\\"std_acc\\\\\\\": 0.006393,\\\\n          \\\\\\\"vs_mv_pp\\\\\\\": 1.812,\\\\n          \\\\\\\"vs_best_single_pp\\\\\\\": 1.828\\\\n        }\\\\n      },\\\\n      \\\\\\\"baselines\\\\\\\": {\\\\n        \\\\\\\"majority_vote_acc\\\\\\\": 0.509042,\\\\n        \\\\\\\"majority_vote_std\\\\\\\": 0.005642,\\\\n        \\\\\\\"best_single_acc\\\\\\\": 0.508886,\\\\n        \\\\\\\"best_single_std\\\\\\\": 0.005018,\\\\n        \\\\\\\"oracle_acc\\\\\\\": 0.654637,\\\\n        \\\\\\\"oracle_std\\\\\\\": 0.005371,\\\\n        \\\\\\\"random_acc\\\\\\\": 0.50683,\\\\n        \\\\\\\"random_std\\\\\\\": 0.008304\\\\n      },\\\\n      \\\\\\\"per_arch\\\\\\\": {\\\\n        \\\\\\\"GDN\\\\\\\": {\\\\n          \\\\\\\"pure_acc\\\\\\\": 0.543373,\\\\n          \\\\\\\"hybrid_acc\\\\\\\": 0.513293\\\\n        },\\\\n        \\\\\\\"RetNet\\\\\\\": {\\\\n          \\\\\\\"pure_acc\\\\\\\": 0.517369,\\\\n          \\\\\\\"hybrid_acc\\\\\\\": 0.502426\\\\n        },\\\\n        \\\\\\\"HGRN2\\\\\\\": {\\\\n          \\\\\\\"pure_acc\\\\\\\": 0.48399,\\\\n          \\\\\\\"hybrid_acc\\\\\\\": 0.514264\\\\n        }\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 5153\\\\n    },\\\\n    \\\\\\\"hellaswag\\\\\\\": {\\\\n      \\\\\\\"strategies\\\\\\\": {\\\\n        \\\\\\\"max_confidence\\\\\\\": {\\\\n          \\\\\\\"mean_acc\\\\\\\": 0.596415,\\\\n          \\\\\\\"std_acc\\\\\\\": 0.004721,\\\\n          \\\\\\\"vs_mv_pp\\\\\\\": 0.118,\\\\n          \\\\\\\"vs_best_single_pp\\\\\\\": -0.44\\\\n        },\\\\n        \\\\\\\"rescue_threshold\\\\\\\": {\\\\n          \\\\\\\"mean_acc\\\\\\\": 0.595041,\\\\n          \\\\\\\"std_acc\\\\\\\": 0.004511,\\\\n          \\\\\\\"vs_mv_pp\\\\\\\": -0.02,\\\\n          \\\\\\\"vs_best_single_pp\\\\\\\": -0.578,\\\\n          \\\\\\\"mean_threshold\\\\\\\": 0.5435,\\\\n          \\\\\\\"std_threshold\\\\\\\": 0.0805\\\\n        },\\\\n        \\\\\\\"confidence_weighted\\\\\\\": {\\\\n          \\\\\\\"mean_acc\\\\\\\": 0.59524,\\\\n          \\\\\\\"std_acc\\\\\\\": 0.005038,\\\\n          \\\\\\\"vs_mv_pp\\\\\\\": 0.0,\\\\n          \\\\\\\"vs_best_single_pp\\\\\\\": -0.558\\\\n        }\\\\n      },\\\\n      \\\\\\\"baselines\\\\\\\": {\\\\n        \\\\\\\"majority_vote_acc\\\\\\\": 0.59524,\\\\n        \\\\\\\"majority_vote_std\\\\\\\": 0.005038,\\\\n        \\\\\\\"best_single_acc\\\\\\\": 0.600817,\\\\n        \\\\\\\"best_single_std\\\\\\\": 0.004614,\\\\n        \\\\\\\"oracle_acc\\\\\\\": 0.668552,\\\\n        \\\\\\\"oracle_std\\\\\\\": 0.005935,\\\\n        \\\\\\\"random_acc\\\\\\\": 0.593169,\\\\n        \\\\\\\"random_std\\\\\\\": 0.004782\\\\n      },\\\\n      \\\\\\\"per_arch\\\\\\\": {\\\\n        \\\\\\\"GDN\\\\\\\": {\\\\n          \\\\\\\"pure_acc\\\\\\\": 0.607648,\\\\n          \\\\\\\"hybrid_acc\\\\\\\": 0.603167\\\\n        },\\\\n        \\\\\\\"RetNet\\\\\\\": {\\\\n          \\\\\\\"pure_acc\\\\\\\": 0.579765,\\\\n          \\\\\\\"hybrid_acc\\\\\\\": 0.577674\\\\n        },\\\\n        \\\\\\\"HGRN2\\\\\\\": {\\\\n          \\\\\\\"pure_acc\\\\\\\": 0.598984,\\\\n          \\\\\\\"hybrid_acc\\\\\\\": 0.603963\\\\n        }\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 10042\\\\n    },\\\\n    \\\\\\\"piqa\\\\\\\": {\\\\n      \\\\\\\"strategies\\\\\\\": {\\\\n        \\\\\\\"max_confidence\\\\\\\": {\\\\n          \\\\\\\"mean_acc\\\\\\\": 0.728945,\\\\n          \\\\\\\"std_acc\\\\\\\": 0.009303,\\\\n          \\\\\\\"vs_mv_pp\\\\\\\": -1.121,\\\\n          \\\\\\\"vs_best_single_pp\\\\\\\": -0.272\\\\n        },\\\\n        \\\\\\\"rescue_threshold\\\\\\\": {\\\\n          \\\\\\\"mean_acc\\\\\\\": 0.734059,\\\\n          \\\\\\\"std_acc\\\\\\\": 0.010268,\\\\n          \\\\\\\"vs_mv_pp\\\\\\\": -0.609,\\\\n          \\\\\\\"vs_best_single_pp\\\\\\\": 0.239,\\\\n          \\\\\\\"mean_threshold\\\\\\\": 70.8392,\\\\n          \\\\\\\"std_threshold\\\\\\\": 62.5899\\\\n        },\\\\n        \\\\\\\"confidence_weighted\\\\\\\": {\\\\n          \\\\\\\"mean_acc\\\\\\\": 0.730686,\\\\n          \\\\\\\"std_acc\\\\\\\": 0.009662,\\\\n          \\\\\\\"vs_mv_pp\\\\\\\": -0.947,\\\\n          \\\\\\\"vs_best_single_pp\\\\\\\": -0.098\\\\n        }\\\\n      },\\\\n      \\\\\\\"baselines\\\\\\\": {\\\\n        \\\\\\\"majority_vote_acc\\\\\\\": 0.740152,\\\\n        \\\\\\\"majority_vote_std\\\\\\\": 0.010581,\\\\n        \\\\\\\"best_single_acc\\\\\\\": 0.731665,\\\\n        \\\\\\\"best_single_std\\\\\\\": 0.011772,\\\\n        \\\\\\\"oracle_acc\\\\\\\": 0.795647,\\\\n        \\\\\\\"oracle_std\\\\\\\": 0.01089,\\\\n        \\\\\\\"random_acc\\\\\\\": 0.728618,\\\\n        \\\\\\\"random_std\\\\\\\": 0.008949\\\\n      },\\\\n      \\\\\\\"per_arch\\\\\\\": {\\\\n        \\\\\\\"GDN\\\\\\\": {\\\\n          \\\\\\\"pure_acc\\\\\\\": 0.723613,\\\\n          \\\\\\\"hybrid_acc\\\\\\\": 0.737758\\\\n        },\\\\n        \\\\\\\"RetNet\\\\\\\": {\\\\n          \\\\\\\"pure_acc\\\\\\\": 0.726333,\\\\n          \\\\\\\"hybrid_acc\\\\\\\": 0.729053\\\\n        },\\\\n        \\\\\\\"HGRN2\\\\\\\": {\\\\n          \\\\\\\"pure_acc\\\\\\\": 0.734494,\\\\n          \\\\\\\"hybrid_acc\\\\\\\": 0.730141\\\\n        }\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 1838\\\\n    },\\\\n    \\\\\\\"arc_easy\\\\\\\": {\\\\n      \\\\\\\"strategies\\\\\\\": {\\\\n        \\\\\\\"max_confidence\\\\\\\": {\\\\n          \\\\\\\"mean_acc\\\\\\\": 0.710943,\\\\n          \\\\\\\"std_acc\\\\\\\": 0.008495,\\\\n          \\\\\\\"vs_mv_pp\\\\\\\": 0.471,\\\\n          \\\\\\\"vs_best_single_pp\\\\\\\": -0.236\\\\n        },\\\\n        \\\\\\\"rescue_threshold\\\\\\\": {\\\\n          \\\\\\\"mean_acc\\\\\\\": 0.716414,\\\\n          \\\\\\\"std_acc\\\\\\\": 0.007323,\\\\n          \\\\\\\"vs_mv_pp\\\\\\\": 1.019,\\\\n          \\\\\\\"vs_best_single_pp\\\\\\\": 0.311,\\\\n          \\\\\\\"mean_threshold\\\\\\\": 19.8566,\\\\n          \\\\\\\"std_threshold\\\\\\\": 6.608\\\\n        },\\\\n        \\\\\\\"confidence_weighted\\\\\\\": {\\\\n          \\\\\\\"mean_acc\\\\\\\": 0.714141,\\\\n          \\\\\\\"std_acc\\\\\\\": 0.007671,\\\\n          \\\\\\\"vs_mv_pp\\\\\\\": 0.791,\\\\n          \\\\\\\"vs_best_single_pp\\\\\\\": 0.084\\\\n        }\\\\n      },\\\\n      \\\\\\\"baselines\\\\\\\": {\\\\n        \\\\\\\"majority_vote_acc\\\\\\\": 0.706229,\\\\n        \\\\\\\"majority_vote_std\\\\\\\": 0.005494,\\\\n        \\\\\\\"best_single_acc\\\\\\\": 0.7133,\\\\n        \\\\\\\"best_single_std\\\\\\\": 0.009897,\\\\n        \\\\\\\"oracle_acc\\\\\\\": 0.808418,\\\\n        \\\\\\\"oracle_std\\\\\\\": 0.005883,\\\\n        \\\\\\\"random_acc\\\\\\\": 0.707407,\\\\n        \\\\\\\"random_std\\\\\\\": 0.008846\\\\n      },\\\\n      \\\\\\\"per_arch\\\\\\\": {\\\\n        \\\\\\\"GDN\\\\\\\": {\\\\n          \\\\\\\"pure_acc\\\\\\\": 0.712121,\\\\n          \\\\\\\"hybrid_acc\\\\\\\": 0.708333\\\\n        },\\\\n        \\\\\\\"RetNet\\\\\\\": {\\\\n          \\\\\\\"pure_acc\\\\\\\": 0.712963,\\\\n          \\\\\\\"hybrid_acc\\\\\\\": 0.696128\\\\n        },\\\\n        \\\\\\\"HGRN2\\\\\\\": {\\\\n          \\\\\\\"pure_acc\\\\\\\": 0.712963,\\\\n          \\\\\\\"hybrid_acc\\\\\\\": 0.720539\\\\n        }\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 2376\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"analysis\\\": \\\"e1_confidence_selection\\\",\\n  \\\"date\\\": \\\"2026-05-22\\\",\\n  \\\"method\\\": {\\n    \\\"attention_ratio\\\": \\\"h3-1 (25%)\\\",\\n    \\\"architectures\\\": [\\n      \\\"GDN\\\",\\n      \\\"RetNet\\\",\\n      \\\"HGRN2\\\"\\n    ],\\n    \\\"cv\\\": \\\"50/50 random split x 10 repeats\\\",\\n    \\\"confidence_measure\\\": {\\n      \\\"lambada\\\": \\\"target word loglikelihood\\\",\\n      \\\"hellaswag\\\": \\\"max char-length-normalized loglikelihood\\\",\\n      \\\"piqa\\\": \\\"max raw loglikelihood across choices\\\",\\n      \\\"arc_easy\\\": \\\"max raw loglikelihood across choices\\\"\\n    }\\n  },\\n  \\\"results\\\": {\\n    \\\"lambada\\\": {\\n      \\\"strategies\\\": {\\n        \\\"max_confidence\\\": {\\n          \\\"mean_acc\\\": 0.525378,\\n          \\\"std_acc\\\": 0.006802,\\n          \\\"vs_mv_pp\\\": 1.634,\\n          \\\"vs_best_single_pp\\\": 1.649\\n        },\\n        \\\"rescue_threshold\\\": {\\n          \\\"mean_acc\\\": 0.562321,\\n          \\\"std_acc\\\": 0.005296,\\n          \\\"vs_mv_pp\\\": 5.328,\\n          \\\"vs_best_single_pp\\\": 5.343,\\n          \\\"mean_threshold\\\": 1.7244,\\n          \\\"std_threshold\\\": 0.1688\\n        },\\n        \\\"confidence_weighted\\\": {\\n          \\\"mean_acc\\\": 0.527163,\\n          \\\"std_acc\\\": 0.006393,\\n          \\\"vs_mv_pp\\\": 1.812,\\n          \\\"vs_best_single_pp\\\": 1.828\\n        }\\n      },\\n      \\\"baselines\\\": {\\n        \\\"majority_vote_acc\\\": 0.509042,\\n        \\\"majority_vote_std\\\": 0.005642,\\n        \\\"best_single_acc\\\": 0.508886,\\n        \\\"best_single_std\\\": 0.005018,\\n        \\\"oracle_acc\\\": 0.654637,\\n        \\\"oracle_std\\\": 0.005371,\\n        \\\"random_acc\\\": 0.50683,\\n        \\\"random_std\\\": 0.008304\\n      },\\n      \\\"per_arch\\\": {\\n        \\\"GDN\\\": {\\n          \\\"pure_acc\\\": 0.543373,\\n          \\\"hybrid_acc\\\": 0.513293\\n        },\\n        \\\"RetNet\\\": {\\n          \\\"pure_acc\\\": 0.517369,\\n          \\\"hybrid_acc\\\": 0.502426\\n        },\\n        \\\"HGRN2\\\": {\\n          \\\"pure_acc\\\": 0.48399,\\n          \\\"hybrid_acc\\\": 0.514264\\n        }\\n      },\\n      \\\"n_samples\\\": 5153\\n    },\\n    \\\"hellaswag\\\": {\\n      \\\"strategies\\\": {\\n        \\\"max_confidence\\\": {\\n          \\\"mean_acc\\\": 0.596415,\\n          \\\"std_acc\\\": 0.004721,\\n          \\\"vs_mv_pp\\\": 0.118,\\n          \\\"vs_best_single_pp\\\": -0.44\\n        },\\n        \\\"rescue_threshold\\\": {\\n          \\\"mean_acc\\\": 0.595041,\\n          \\\"std_acc\\\": 0.004511,\\n          \\\"vs_mv_pp\\\": -0.02,\\n          \\\"vs_best_single_pp\\\": -0.578,\\n          \\\"mean_threshold\\\": 0.5435,\\n          \\\"std_threshold\\\": 0.0805\\n        },\\n        \\\"confidence_weighted\\\": {\\n          \\\"mean_acc\\\": 0.59524,\\n          \\\"std_acc\\\": 0.005038,\\n          \\\"vs_mv_pp\\\": 0.0,\\n          \\\"vs_best_single_pp\\\": -0.558\\n        }\\n      },\\n      \\\"baselines\\\": {\\n        \\\"majority_vote_acc\\\": 0.59524,\\n        \\\"majority_vote_std\\\": 0.005038,\\n        \\\"best_single_acc\\\": 0.600817,\\n        \\\"best_single_std\\\": 0.004614,\\n        \\\"oracle_acc\\\": 0.668552,\\n        \\\"oracle_std\\\": 0.005935,\\n        \\\"random_acc\\\": 0.593169,\\n        \\\"random_std\\\": 0.004782\\n      },\\n      \\\"per_arch\\\": {\\n        \\\"GDN\\\": {\\n          \\\"pure_acc\\\": 0.607648,\\n          \\\"hybrid_acc\\\": 0.603167\\n        },\\n        \\\"RetNet\\\": {\\n          \\\"pure_acc\\\": 0.579765,\\n          \\\"hybrid_acc\\\": 0.577674\\n        },\\n        \\\"HGRN2\\\": {\\n          \\\"pure_acc\\\": 0.598984,\\n          \\\"hybrid_acc\\\": 0.603963\\n        }\\n      },\\n      \\\"n_samples\\\": 10042\\n    },\\n    \\\"piqa\\\": {\\n      \\\"strategies\\\": {\\n        \\\"max_confidence\\\": {\\n          \\\"mean_acc\\\": 0.728945,\\n          \\\"std_acc\\\": 0.009303,\\n          \\\"vs_mv_pp\\\": -1.121,\\n          \\\"vs_best_single_pp\\\": -0.272\\n        },\\n        \\\"rescue_threshold\\\": {\\n          \\\"mean_acc\\\": 0.734059,\\n          \\\"std_acc\\\": 0.010268,\\n          \\\"vs_mv_pp\\\": -0.609,\\n          \\\"vs_best_single_pp\\\": 0.239,\\n          \\\"mean_threshold\\\": 70.8392,\\n          \\\"std_threshold\\\": 62.5899\\n        },\\n        \\\"confidence_weighted\\\": {\\n          \\\"mean_acc\\\": 0.730686,\\n          \\\"std_acc\\\": 0.009662,\\n          \\\"vs_mv_pp\\\": -0.947,\\n          \\\"vs_best_single_pp\\\": -0.098\\n        }\\n      },\\n      \\\"baselines\\\": {\\n        \\\"majority_vote_acc\\\": 0.740152,\\n        \\\"majority_vote_std\\\": 0.010581,\\n        \\\"best_single_acc\\\": 0.731665,\\n        \\\"best_single_std\\\": 0.011772,\\n        \\\"oracle_acc\\\": 0.795647,\\n        \\\"oracle_std\\\": 0.01089,\\n        \\\"random_acc\\\": 0.728618,\\n        \\\"random_std\\\": 0.008949\\n      },\\n      \\\"per_arch\\\": {\\n        \\\"GDN\\\": {\\n          \\\"pure_acc\\\": 0.723613,\\n          \\\"hybrid_acc\\\": 0.737758\\n        },\\n        \\\"RetNet\\\": {\\n          \\\"pure_acc\\\": 0.726333,\\n          \\\"hybrid_acc\\\": 0.729053\\n        },\\n        \\\"HGRN2\\\": {\\n          \\\"pure_acc\\\": 0.734494,\\n          \\\"hybrid_acc\\\": 0.730141\\n        }\\n      },\\n      \\\"n_samples\\\": 1838\\n    },\\n    \\\"arc_easy\\\": {\\n      \\\"strategies\\\": {\\n        \\\"max_confidence\\\": {\\n          \\\"mean_acc\\\": 0.710943,\\n          \\\"std_acc\\\": 0.008495,\\n          \\\"vs_mv_pp\\\": 0.471,\\n          \\\"vs_best_single_pp\\\": -0.236\\n        },\\n        \\\"rescue_threshold\\\": {\\n          \\\"mean_acc\\\": 0.716414,\\n          \\\"std_acc\\\": 0.007323,\\n          \\\"vs_mv_pp\\\": 1.019,\\n          \\\"vs_best_single_pp\\\": 0.311,\\n          \\\"mean_threshold\\\": 19.8566,\\n          \\\"std_threshold\\\": 6.608\\n        },\\n        \\\"confidence_weighted\\\": {\\n          \\\"mean_acc\\\": 0.714141,\\n          \\\"std_acc\\\": 0.007671,\\n          \\\"vs_mv_pp\\\": 0.791,\\n          \\\"vs_best_single_pp\\\": 0.084\\n        }\\n      },\\n      \\\"baselines\\\": {\\n        \\\"majority_vote_acc\\\": 0.706229,\\n        \\\"majority_vote_std\\\": 0.005494,\\n        \\\"best_single_acc\\\": 0.7133,\\n        \\\"best_single_std\\\": 0.009897,\\n        \\\"oracle_acc\\\": 0.808418,\\n        \\\"oracle_std\\\": 0.005883,\\n        \\\"random_acc\\\": 0.707407,\\n        \\\"random_std\\\": 0.008846\\n      },\\n      \\\"per_arch\\\": {\\n        \\\"GDN\\\": {\\n          \\\"pure_acc\\\": 0.712121,\\n          \\\"hybrid_acc\\\": 0.708333\\n        },\\n        \\\"RetNet\\\": {\\n          \\\"pure_acc\\\": 0.712963,\\n          \\\"hybrid_acc\\\": 0.696128\\n        },\\n        \\\"HGRN2\\\": {\\n          \\\"pure_acc\\\": 0.712963,\\n          \\\"hybrid_acc\\\": 0.720539\\n        }\\n      },\\n      \\\"n_samples\\\": 2376\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.77}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T17:06:13.378Z_

<details><summary>↩ Tool result · `toolu_01WYNcEBi6xHMgGtuHSNFJym`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/results/func_comp/datasets/depth_1_direct_n10.json\\n/root/entrainment_gated_ft/results/func_comp/datasets/depth_2_direct_n10.json\\n/root/entrainment_gated_ft/results/func_comp/datasets/depth_3_direct_n10.json\\n/root/entrainment_gated_ft/results/func_comp/datasets/depth_4_direct_n10.json\\n/root/entrainment_gated_ft/results/func_comp/datasets/depth_5_direct_n10.json\\n/root/entrainment_gated_ft/results/test_run/datasets/depth_1_direct_n5.json\\n/root/entrainment_gated_ft/results/test_run/datasets/depth_2_direct_n5.json\\n/root/entrainment_gated_ft/results/test_run/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth1_direct.json\\n/root/entrainment_gated_ft/results/test_run/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth2_direct.json\\n/root/entrainment_gated_ft/results/test_run/summary_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_1_direct_n500.json\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_2_direct_n500.json\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_3_direct_n500.json\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_4_direct_n500.json\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_5_direct_n500.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth1_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth2_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth3_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth4_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth5_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth1_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth2_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth3_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth4_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth5_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth1_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth2_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth3_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth4_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth5_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth1_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth2_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth3_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth4_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth5_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-3-1_depth1_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-3-1_depth2_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-3-1_depth3_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-3-1_depth4_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340\\n\\n... [截断: 输出过长，省略 15212 字符] ...\\n\\nroot__autodl-tmp__pythia_weights_70m__seed7/results_2026-05-22T19-36-59.412802.json\\n/root/entrainment_gated_ft/results/e4_pythia_seed/seed8/__root__autodl-tmp__pythia_weights_70m__seed8/results_2026-05-22T22-05-45.863267.json\\n/root/entrainment_gated_ft/results/e4_pythia_seed/seed9/__root__autodl-tmp__pythia_weights_70m__seed9/results_2026-05-22T22-06-48.390425.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-GLA-hybrid-3-1/results_2026-05-22T23-51-08.119053.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_hybrid-3-1/results.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-hybrid-3-1/results_2026-05-23T00-09-47.452122.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-HGRN-hybrid-3-1/results_2026-05-23T01-47-55.682781.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/results_2026-05-23T00-41-14.537211.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_4arch.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GDN_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-GatedDeltaNet-pure-baseline/results_2026-05-23T00-55-12.446919.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/results_2026-05-23T01-04-47.578552.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GDN_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-GatedDeltaNet-hybrid-3-1/results_2026-05-23T00-57-27.658457.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-pure/results_2026-05-23T01-13-35.906959.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/RetNet_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-RetNet-pure/results_2026-05-23T01-00-10.816890.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/RetNet_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-RetNet-hybrid-3-1/results_2026-05-23T01-02-18.914553.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN2_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-HGRN2-pure-baseline/results_2026-05-23T01-05-14.495517.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN2_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-HGRN2-hybrid-3-1/results_2026-05-23T01-07-22.356663.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_5arch.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-HGRN-pure-baseline/results_2026-05-23T02-05-21.242421.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-HGRN-pure-baseline/results_2026-05-23T03-07-41.643648.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_6arch.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_h31_hswag_piqa/__root__entrainment_gated_ft__models__340M-20B-GLA-hybrid-3-1/results_2026-05-23T10-16-50.014884.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure_hswag_piqa/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/results_2026-05-23T10-21-27.935861.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_h31_hswag_piqa/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-hybrid-3-1/results_2026-05-23T10-26-41.172537.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_pure_hswag_piqa/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-pure/results_2026-05-23T10-32-03.537865.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_5arch_extended.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "d90f1925-72b1-48ff-b6df-e88ee56b361f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/entrainment_gated_ft/results/func_comp/datasets/depth_1_direct_n10.json\\\\n/root/entrainment_gated_ft/results/func_comp/datasets/depth_2_direct_n10.json\\\\n/root/entrainment_gated_ft/results/func_comp/datasets/depth_3_direct_n10.json\\\\n/root/entrainment_gated_ft/results/func_comp/datasets/depth_4_direct_n10.json\\\\n/root/entrainment_gated_ft/results/func_comp/datasets/depth_5_direct_n10.json\\\\n/root/entrainment_gated_ft/results/test_run/datasets/depth_1_direct_n5.json\\\\n/root/entrainment_gated_ft/results/test_run/datasets/depth_2_direct_n5.json\\\\n/root/entrainment_gated_ft/results/test_run/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth1_direct.json\\\\n/root/entrainment_gated_ft/results/test_run/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth2_direct.json\\\\n/root/entrainment_gated_ft/results/test_run/summary_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_1_direct_n500.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_2_direct_n500.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_3_direct_n500.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_4_direct_n500.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_5_direct_n500.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth1_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth2_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth3_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth4_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth5_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth1_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth2_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth3_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth4_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth5_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth1_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth2_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth3_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth4_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth5_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth1_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth2_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth3_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth4_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth5_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-3-1_depth1_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-3-1_depth2_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-3-1_depth3_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-3-1_depth4_direct.json\\\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340\\\\n\\\\n... [截断: 输出过长，省略 15212 字符] ...\\\\n\\\\nroot__autodl-tmp__pythia_weights_70m__seed7/results_2026-05-22T19-36-59.412802.json\\\\n/root/entrainment_gated_ft/results/e4_pythia_seed/seed8/__root__autodl-tmp__pythia_weights_70m__seed8/results_2026-05-22T22-05-45.863267.json\\\\n/root/entrainment_gated_ft/results/e4_pythia_seed/seed9/__root__autodl-tmp__pythia_weights_70m__seed9/results_2026-05-22T22-06-48.390425.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-GLA-hybrid-3-1/results_2026-05-22T23-51-08.119053.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_hybrid-3-1/results.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-hybrid-3-1/results_2026-05-23T00-09-47.452122.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-HGRN-hybrid-3-1/results_2026-05-23T01-47-55.682781.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/results_2026-05-23T00-41-14.537211.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_4arch.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GDN_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-GatedDeltaNet-pure-baseline/results_2026-05-23T00-55-12.446919.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/results_2026-05-23T01-04-47.578552.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GDN_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-GatedDeltaNet-hybrid-3-1/results_2026-05-23T00-57-27.658457.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-pure/results_2026-05-23T01-13-35.906959.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/RetNet_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-RetNet-pure/results_2026-05-23T01-00-10.816890.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/RetNet_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-RetNet-hybrid-3-1/results_2026-05-23T01-02-18.914553.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN2_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-HGRN2-pure-baseline/results_2026-05-23T01-05-14.495517.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN2_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-HGRN2-hybrid-3-1/results_2026-05-23T01-07-22.356663.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_5arch.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-HGRN-pure-baseline/results_2026-05-23T02-05-21.242421.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-HGRN-pure-baseline/results_2026-05-23T03-07-41.643648.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_6arch.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_h31_hswag_piqa/__root__entrainment_gated_ft__models__340M-20B-GLA-hybrid-3-1/results_2026-05-23T10-16-50.014884.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure_hswag_piqa/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/results_2026-05-23T10-21-27.935861.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_h31_hswag_piqa/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-hybrid-3-1/results_2026-05-23T10-26-41.172537.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_pure_hswag_piqa/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-pure/results_2026-05-23T10-32-03.537865.json\\\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_5arch_extended.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/results/func_comp/datasets/depth_1_direct_n10.json\\n/root/entrainment_gated_ft/results/func_comp/datasets/depth_2_direct_n10.json\\n/root/entrainment_gated_ft/results/func_comp/datasets/depth_3_direct_n10.json\\n/root/entrainment_gated_ft/results/func_comp/datasets/depth_4_direct_n10.json\\n/root/entrainment_gated_ft/results/func_comp/datasets/depth_5_direct_n10.json\\n/root/entrainment_gated_ft/results/test_run/datasets/depth_1_direct_n5.json\\n/root/entrainment_gated_ft/results/test_run/datasets/depth_2_direct_n5.json\\n/root/entrainment_gated_ft/results/test_run/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth1_direct.json\\n/root/entrainment_gated_ft/results/test_run/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth2_direct.json\\n/root/entrainment_gated_ft/results/test_run/summary_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_1_direct_n500.json\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_2_direct_n500.json\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_3_direct_n500.json\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_4_direct_n500.json\\n/root/entrainment_gated_ft/results/mvp_direct/datasets/depth_5_direct_n500.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth1_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth2_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth3_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth4_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-pure-baseline_depth5_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth1_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth2_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth3_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth4_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-New-hybrid-24-1_depth5_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth1_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth2_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth3_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth4_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-12-1_depth5_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth1_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth2_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth3_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth4_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-6-1_depth5_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-3-1_depth1_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-3-1_depth2_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-3-1_depth3_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340M-20B-GatedDeltaNet-hybrid-3-1_depth4_direct.json\\n/root/entrainment_gated_ft/results/mvp_direct/predictions_340\\n\\n... [截断: 输出过长，省略 15212 字符] ...\\n\\nroot__autodl-tmp__pythia_weights_70m__seed7/results_2026-05-22T19-36-59.412802.json\\n/root/entrainment_gated_ft/results/e4_pythia_seed/seed8/__root__autodl-tmp__pythia_weights_70m__seed8/results_2026-05-22T22-05-45.863267.json\\n/root/entrainment_gated_ft/results/e4_pythia_seed/seed9/__root__autodl-tmp__pythia_weights_70m__seed9/results_2026-05-22T22-06-48.390425.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-GLA-hybrid-3-1/results_2026-05-22T23-51-08.119053.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_hybrid-3-1/results.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-hybrid-3-1/results_2026-05-23T00-09-47.452122.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-HGRN-hybrid-3-1/results_2026-05-23T01-47-55.682781.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/results_2026-05-23T00-41-14.537211.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_4arch.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GDN_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-GatedDeltaNet-pure-baseline/results_2026-05-23T00-55-12.446919.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/results_2026-05-23T01-04-47.578552.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GDN_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-GatedDeltaNet-hybrid-3-1/results_2026-05-23T00-57-27.658457.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-pure/results_2026-05-23T01-13-35.906959.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/RetNet_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-RetNet-pure/results_2026-05-23T01-00-10.816890.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/RetNet_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-RetNet-hybrid-3-1/results_2026-05-23T01-02-18.914553.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN2_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-HGRN2-pure-baseline/results_2026-05-23T01-05-14.495517.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN2_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-HGRN2-hybrid-3-1/results_2026-05-23T01-07-22.356663.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_5arch.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-HGRN-pure-baseline/results_2026-05-23T02-05-21.242421.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/HGRN_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-HGRN-pure-baseline/results_2026-05-23T03-07-41.643648.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_6arch.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_h31_hswag_piqa/__root__entrainment_gated_ft__models__340M-20B-GLA-hybrid-3-1/results_2026-05-23T10-16-50.014884.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure_hswag_piqa/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/results_2026-05-23T10-21-27.935861.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_h31_hswag_piqa/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-hybrid-3-1/results_2026-05-23T10-26-41.172537.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_pure_hswag_piqa/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-pure/results_2026-05-23T10-32-03.537865.json\\n/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_5arch_extended.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.77}}"
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
The e1_confidence_selection.json has only aggregate results (mean_acc, std_acc) across the 10 repeats — no per-split data. Let me check if there's a script that generated this data, which might save per-split results, or look for the analysis scripts that produced this.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "ffb10f66-5779-4ef7-8c08-c7709cad47d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLN5EyvLqWd1kXfJVmEGQs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9926,
      "cache_read_input_tokens": 25872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9926
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

e1_confidence_selection.json 只有聚合统计（mean/std），没有逐 split 数据。让我找生成脚本和可能的 per-split 输出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "8f7aa1a2-78c5-42da-8883-446fae07faa5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLN5EyvLqWd1kXfJVmEGQs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9926,
      "cache_read_input_tokens": 25872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9926
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019ysjgwWmnMkSk8CxhWPV8Y`</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/ -name \"*confidence*\" -o -name \"*e1_*\" -type f",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "fe74ffcc-5a72-4acb-8c06-e6138ad3b369",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLN5EyvLqWd1kXfJVmEGQs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9926,
      "cache_read_input_tokens": 25872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9926
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GbaKe9qEQLtkVTRbSzFxBC`</summary>

```json
{
  "server": "westb-48145",
  "command": "ls -la /root/entrainment_gated_ft/results/a2_prediction_framework/",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "8d30ce9c-aee4-42f3-a57d-afb3106a0a41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLN5EyvLqWd1kXfJVmEGQs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9926,
      "cache_read_input_tokens": 25872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9926
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

_source line 25 · 2026-05-23T17:06:23.069Z_

<details><summary>↩ Tool result · `toolu_019ysjgwWmnMkSk8CxhWPV8Y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/results/a2_prediction_framework/confidence_margin_prediction.json\\n/root/entrainment_gated_ft/results/e1_confidence_selection.json\\n/root/entrainment_gated_ft/analysis/paper_data/table1_task_specificity.csv\\n/root/entrainment_gated_ft/analysis/confidence_margin_analysis.py\\n/root/entrainment_gated_ft/analysis/confidence_margin_analysis.json\\n/root/entrainment_gated_ft/analysis/confidence_margin_within_category.py\\n/root/entrainment_gated_ft/analysis/confidence_margin_within_category.json\\n/root/entrainment_gated_ft/analysis/e1_confidence_selection.py\\n/root/entrainment_gated_ft/analysis_output/cross_benchmark_confidence_margin.json\\n/root/entrainment_gated_ft/analysis_output/boolq_confidence_margin.json\\n/root/entrainment_gated_ft/analyze_confidence_margin_mc.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.18}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "1033cd61-241c-4cab-86f8-307a4ab5a267",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/entrainment_gated_ft/results/a2_prediction_framework/confidence_margin_prediction.json\\\\n/root/entrainment_gated_ft/results/e1_confidence_selection.json\\\\n/root/entrainment_gated_ft/analysis/paper_data/table1_task_specificity.csv\\\\n/root/entrainment_gated_ft/analysis/confidence_margin_analysis.py\\\\n/root/entrainment_gated_ft/analysis/confidence_margin_analysis.json\\\\n/root/entrainment_gated_ft/analysis/confidence_margin_within_category.py\\\\n/root/entrainment_gated_ft/analysis/confidence_margin_within_category.json\\\\n/root/entrainment_gated_ft/analysis/e1_confidence_selection.py\\\\n/root/entrainment_gated_ft/analysis_output/cross_benchmark_confidence_margin.json\\\\n/root/entrainment_gated_ft/analysis_output/boolq_confidence_margin.json\\\\n/root/entrainment_gated_ft/analyze_confidence_margin_mc.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.18}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/results/a2_prediction_framework/confidence_margin_prediction.json\\n/root/entrainment_gated_ft/results/e1_confidence_selection.json\\n/root/entrainment_gated_ft/analysis/paper_data/table1_task_specificity.csv\\n/root/entrainment_gated_ft/analysis/confidence_margin_analysis.py\\n/root/entrainment_gated_ft/analysis/confidence_margin_analysis.json\\n/root/entrainment_gated_ft/analysis/confidence_margin_within_category.py\\n/root/entrainment_gated_ft/analysis/confidence_margin_within_category.json\\n/root/entrainment_gated_ft/analysis/e1_confidence_selection.py\\n/root/entrainment_gated_ft/analysis_output/cross_benchmark_confidence_margin.json\\n/root/entrainment_gated_ft/analysis_output/boolq_confidence_margin.json\\n/root/entrainment_gated_ft/analyze_confidence_margin_mc.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.18}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T17:06:24.366Z_

<details><summary>↩ Tool result · `toolu_01GbaKe9qEQLtkVTRbSzFxBC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16\\ndrwxr-xr-x  2 root root   95 May 22 16:23 .\\ndrwxr-xr-x 13 root root 4096 May 23 05:04 ..\\n-rw-r--r--  1 root root 7800 May 22 16:23 confidence_margin_prediction.json\\n-rw-r--r--  1 root root 1200 May 22 16:23 prediction_summary_table.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.29}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "f7bff873-30d9-44b6-96e6-ebb176cfcfbb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 16\\\\ndrwxr-xr-x  2 root root   95 May 22 16:23 .\\\\ndrwxr-xr-x 13 root root 4096 May 23 05:04 ..\\\\n-rw-r--r--  1 root root 7800 May 22 16:23 confidence_margin_prediction.json\\\\n-rw-r--r--  1 root root 1200 May 22 16:23 prediction_summary_table.tex\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.29}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 16\\ndrwxr-xr-x  2 root root   95 May 22 16:23 .\\ndrwxr-xr-x 13 root root 4096 May 23 05:04 ..\\n-rw-r--r--  1 root root 7800 May 22 16:23 confidence_margin_prediction.json\\n-rw-r--r--  1 root root 1200 May 22 16:23 prediction_summary_table.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.29}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KsBTw37SH1GkLA9fZNw62m`</summary>

```json
{
  "server": "westb-48145",
  "command": "head -80 /root/entrainment_gated_ft/analysis/e1_confidence_selection.py",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "cf8b8ef0-09b9-4a66-b1f5-4ce5e47cb436",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSWwm9n9tE5KMuanjmkuWz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 35798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1095
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

_source line 28 · 2026-05-23T17:06:29.101Z_

<details><summary>↩ Tool result · `toolu_01KsBTw37SH1GkLA9fZNw62m`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"E1: Confidence-based Architecture Selection\\\"\\\"\\\"\\nimport json\\nimport numpy as np\\nfrom pathlib import Path\\n\\nBASE = Path(\\\"/root/entrainment_gated_ft\\\")\\nLM = BASE / \\\"lm_eval_clean\\\"\\nARCHS = [\\\"GDN\\\", \\\"RetNet\\\", \\\"HGRN2\\\"]\\nFULL_NAMES = {\\\"GDN\\\": \\\"GatedDeltaNet\\\", \\\"RetNet\\\": \\\"RetNet\\\", \\\"HGRN2\\\": \\\"HGRN2\\\"}\\n\\nBENCHMARKS = {\\n    \\\"lambada\\\": {\\n        \\\"metric\\\": \\\"acc\\\",\\n        \\\"pure\\\": {\\n            \\\"GDN\\\":    LM / \\\"exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\\\",\\n            \\\"RetNet\\\": LM / \\\"exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\\\",\\n            \\\"HGRN2\\\":  LM / \\\"exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\\\",\\n        },\\n        \\\"hybrid\\\": {\\n            \\\"GDN\\\":    LM / \\\"1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\\\",\\n            \\\"RetNet\\\": LM / \\\"exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\\\",\\n            \\\"HGRN2\\\":  LM / \\\"exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\\\",\\n        },\\n    },\\n    \\\"hellaswag\\\": {\\n        \\\"metric\\\": \\\"acc_norm\\\",\\n        \\\"pure\\\":   {a: LM / f\\\"hellaswag/1.3B-100B-{FULL_NAMES[a]}-pure/samples/hellaswag.jsonl\\\" for a in ARCHS},\\n        \\\"hybrid\\\": {a: LM / f\\\"hellaswag/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/hellaswag.jsonl\\\" for a in ARCHS},\\n    },\\n    \\\"piqa\\\": {\\n        \\\"metric\\\": \\\"acc\\\",\\n        \\\"pure\\\":   {a: LM / f\\\"piqa/1.3B-100B-{FULL_NAMES[a]}-pure/samples/piqa.jsonl\\\" for a in ARCHS},\\n        \\\"hybrid\\\": {a: LM / f\\\"piqa/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/piqa.jsonl\\\" for a in ARCHS},\\n    },\\n    \\\"arc_easy\\\": {\\n        \\\"metric\\\": \\\"acc\\\",\\n        \\\"pure\\\":   {a: LM / f\\\"arc_easy/1.3B-100B-{FULL_NAMES[a]}-pure/samples/arc_easy.jsonl\\\" for a in ARCHS},\\n        \\\"hybrid\\\": {a: LM / f\\\"arc_easy/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/arc_easy.jsonl\\\" for a in ARCHS},\\n    },\\n}\\n\\n\\ndef load_jsonl(path):\\n    with open(path) as f:\\n        data = [json.loads(line) for line in f]\\n    data.sort(key=lambda x: x[\\\"doc_id\\\"])\\n    return data\\n\\n\\ndef get_confidence(sample, metric, benchmark):\\n    if benchmark == \\\"lambada\\\":\\n        return sample[\\\"resps\\\"][0][0][0]\\n    resps = [r[0][0] for r in sample[\\\"resps\\\"]]\\n    if metric == \\\"acc_norm\\\":\\n        endings = sample[\\\"doc\\\"][\\\"endings\\\"]\\n        return max(r / max(len(e), 1) for r, e in zip(resps, endings))\\n    return max(resps)\\n\\n\\ndef load_data(benchmark):\\n    cfg = BENCHMARKS[benchmark]\\n    metric = cfg[\\\"metric\\\"]\\n    data = {\\\"pure_conf\\\": {}, \\\"pure_acc\\\": {}, \\\"hybrid_acc\\\": {}}\\n\\n    for arch in ARCHS:\\n        pp, hp = str(cfg[\\\"pure\\\"][arch]), str(cfg[\\\"hybrid\\\"][arch])\\n        if not Path(pp).exists() or not Path(hp).exists():\\n            print(f\\\"  MISSING: {pp} or {hp}\\\")\\n            return None\\n\\n        ps = load_jsonl(pp)\\n        hs = load_jsonl(hp)\\n        assert [s[\\\"doc_id\\\"] for s in ps] == [s[\\\"doc_id\\\"] for s in hs], \\\\\\n            f\\\"doc_id mismatch {benchmark}/{arch}\\\"\\n\\n        data[\\\"pure_conf\\\"][arch] = np.array([get_confidence(s, metric, benchmark) for s in ps])\\n        data[\\\"pure_acc\\\"][arch]  = np.array([int(s[metric]) for s in ps])\\n        data[\\\"hybrid_acc\\\"][arch] = np.array([int(s[metric]) for s in hs])\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "e315c66f-a292-496f-af22-de2e80a4dcc0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"E1: Confidence-based Architecture Selection\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport json\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\n\\\\nBASE = Path(\\\\\\\"/root/entrainment_gated_ft\\\\\\\")\\\\nLM = BASE / \\\\\\\"lm_eval_clean\\\\\\\"\\\\nARCHS = [\\\\\\\"GDN\\\\\\\", \\\\\\\"RetNet\\\\\\\", \\\\\\\"HGRN2\\\\\\\"]\\\\nFULL_NAMES = {\\\\\\\"GDN\\\\\\\": \\\\\\\"GatedDeltaNet\\\\\\\", \\\\\\\"RetNet\\\\\\\": \\\\\\\"RetNet\\\\\\\", \\\\\\\"HGRN2\\\\\\\": \\\\\\\"HGRN2\\\\\\\"}\\\\n\\\\nBENCHMARKS = {\\\\n    \\\\\\\"lambada\\\\\\\": {\\\\n        \\\\\\\"metric\\\\\\\": \\\\\\\"acc\\\\\\\",\\\\n        \\\\\\\"pure\\\\\\\": {\\\\n            \\\\\\\"GDN\\\\\\\":    LM / \\\\\\\"exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\\\\\\\",\\\\n            \\\\\\\"RetNet\\\\\\\": LM / \\\\\\\"exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\\\\\\\",\\\\n            \\\\\\\"HGRN2\\\\\\\":  LM / \\\\\\\"exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\\\\\\\",\\\\n        },\\\\n        \\\\\\\"hybrid\\\\\\\": {\\\\n            \\\\\\\"GDN\\\\\\\":    LM / \\\\\\\"1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\\\\\\\",\\\\n            \\\\\\\"RetNet\\\\\\\": LM / \\\\\\\"exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\\\\\\\",\\\\n            \\\\\\\"HGRN2\\\\\\\":  LM / \\\\\\\"exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\\\\\\\",\\\\n        },\\\\n    },\\\\n    \\\\\\\"hellaswag\\\\\\\": {\\\\n        \\\\\\\"metric\\\\\\\": \\\\\\\"acc_norm\\\\\\\",\\\\n        \\\\\\\"pure\\\\\\\":   {a: LM / f\\\\\\\"hellaswag/1.3B-100B-{FULL_NAMES[a]}-pure/samples/hellaswag.jsonl\\\\\\\" for a in ARCHS},\\\\n        \\\\\\\"hybrid\\\\\\\": {a: LM / f\\\\\\\"hellaswag/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/hellaswag.jsonl\\\\\\\" for a in ARCHS},\\\\n    },\\\\n    \\\\\\\"piqa\\\\\\\": {\\\\n        \\\\\\\"metric\\\\\\\": \\\\\\\"acc\\\\\\\",\\\\n        \\\\\\\"pure\\\\\\\":   {a: LM / f\\\\\\\"piqa/1.3B-100B-{FULL_NAMES[a]}-pure/samples/piqa.jsonl\\\\\\\" for a in ARCHS},\\\\n        \\\\\\\"hybrid\\\\\\\": {a: LM / f\\\\\\\"piqa/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/piqa.jsonl\\\\\\\" for a in ARCHS},\\\\n    },\\\\n    \\\\\\\"arc_easy\\\\\\\": {\\\\n        \\\\\\\"metric\\\\\\\": \\\\\\\"acc\\\\\\\",\\\\n        \\\\\\\"pure\\\\\\\":   {a: LM / f\\\\\\\"arc_easy/1.3B-100B-{FULL_NAMES[a]}-pure/samples/arc_easy.jsonl\\\\\\\" for a in ARCHS},\\\\n        \\\\\\\"hybrid\\\\\\\": {a: LM / f\\\\\\\"arc_easy/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/arc_easy.jsonl\\\\\\\" for a in ARCHS},\\\\n    },\\\\n}\\\\n\\\\n\\\\ndef load_jsonl(path):\\\\n    with open(path) as f:\\\\n        data = [json.loads(line) for line in f]\\\\n    data.sort(key=lambda x: x[\\\\\\\"doc_id\\\\\\\"])\\\\n    return data\\\\n\\\\n\\\\ndef get_confidence(sample, metric, benchmark):\\\\n    if benchmark == \\\\\\\"lambada\\\\\\\":\\\\n        return sample[\\\\\\\"resps\\\\\\\"][0][0][0]\\\\n    resps = [r[0][0] for r in sample[\\\\\\\"resps\\\\\\\"]]\\\\n    if metric == \\\\\\\"acc_norm\\\\\\\":\\\\n        endings = sample[\\\\\\\"doc\\\\\\\"][\\\\\\\"endings\\\\\\\"]\\\\n        return max(r / max(len(e), 1) for r, e in zip(resps, endings))\\\\n    return max(resps)\\\\n\\\\n\\\\ndef load_data(benchmark):\\\\n    cfg = BENCHMARKS[benchmark]\\\\n    metric = cfg[\\\\\\\"metric\\\\\\\"]\\\\n    data = {\\\\\\\"pure_conf\\\\\\\": {}, \\\\\\\"pure_acc\\\\\\\": {}, \\\\\\\"hybrid_acc\\\\\\\": {}}\\\\n\\\\n    for arch in ARCHS:\\\\n        pp, hp = str(cfg[\\\\\\\"pure\\\\\\\"][arch]), str(cfg[\\\\\\\"hybrid\\\\\\\"][arch])\\\\n        if not Path(pp).exists() or not Path(hp).exists():\\\\n            print(f\\\\\\\"  MISSING: {pp} or {hp}\\\\\\\")\\\\n            return None\\\\n\\\\n        ps = load_jsonl(pp)\\\\n        hs = load_jsonl(hp)\\\\n        assert [s[\\\\\\\"doc_id\\\\\\\"] for s in ps] == [s[\\\\\\\"doc_id\\\\\\\"] for s in hs], \\\\\\\\\\\\n            f\\\\\\\"doc_id mismatch {benchmark}/{arch}\\\\\\\"\\\\n\\\\n        data[\\\\\\\"pure_conf\\\\\\\"][arch] = np.array([get_confidence(s, metric, benchmark) for s in ps])\\\\n        data[\\\\\\\"pure_acc\\\\\\\"][arch]  = np.array([int(s[metric]) for s in ps])\\\\n        data[\\\\\\\"hybrid_acc\\\\\\\"][arch] = np.array([int(s[metric]) for s in hs])\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.12}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"E1: Confidence-based Architecture Selection\\\"\\\"\\\"\\nimport json\\nimport numpy as np\\nfrom pathlib import Path\\n\\nBASE = Path(\\\"/root/entrainment_gated_ft\\\")\\nLM = BASE / \\\"lm_eval_clean\\\"\\nARCHS = [\\\"GDN\\\", \\\"RetNet\\\", \\\"HGRN2\\\"]\\nFULL_NAMES = {\\\"GDN\\\": \\\"GatedDeltaNet\\\", \\\"RetNet\\\": \\\"RetNet\\\", \\\"HGRN2\\\": \\\"HGRN2\\\"}\\n\\nBENCHMARKS = {\\n    \\\"lambada\\\": {\\n        \\\"metric\\\": \\\"acc\\\",\\n        \\\"pure\\\": {\\n            \\\"GDN\\\":    LM / \\\"exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\\\",\\n            \\\"RetNet\\\": LM / \\\"exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\\\",\\n            \\\"HGRN2\\\":  LM / \\\"exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\\\",\\n        },\\n        \\\"hybrid\\\": {\\n            \\\"GDN\\\":    LM / \\\"1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\\\",\\n            \\\"RetNet\\\": LM / \\\"exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\\\",\\n            \\\"HGRN2\\\":  LM / \\\"exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\\\",\\n        },\\n    },\\n    \\\"hellaswag\\\": {\\n        \\\"metric\\\": \\\"acc_norm\\\",\\n        \\\"pure\\\":   {a: LM / f\\\"hellaswag/1.3B-100B-{FULL_NAMES[a]}-pure/samples/hellaswag.jsonl\\\" for a in ARCHS},\\n        \\\"hybrid\\\": {a: LM / f\\\"hellaswag/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/hellaswag.jsonl\\\" for a in ARCHS},\\n    },\\n    \\\"piqa\\\": {\\n        \\\"metric\\\": \\\"acc\\\",\\n        \\\"pure\\\":   {a: LM / f\\\"piqa/1.3B-100B-{FULL_NAMES[a]}-pure/samples/piqa.jsonl\\\" for a in ARCHS},\\n        \\\"hybrid\\\": {a: LM / f\\\"piqa/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/piqa.jsonl\\\" for a in ARCHS},\\n    },\\n    \\\"arc_easy\\\": {\\n        \\\"metric\\\": \\\"acc\\\",\\n        \\\"pure\\\":   {a: LM / f\\\"arc_easy/1.3B-100B-{FULL_NAMES[a]}-pure/samples/arc_easy.jsonl\\\" for a in ARCHS},\\n        \\\"hybrid\\\": {a: LM / f\\\"arc_easy/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/arc_easy.jsonl\\\" for a in ARCHS},\\n    },\\n}\\n\\n\\ndef load_jsonl(path):\\n    with open(path) as f:\\n        data = [json.loads(line) for line in f]\\n    data.sort(key=lambda x: x[\\\"doc_id\\\"])\\n    return data\\n\\n\\ndef get_confidence(sample, metric, benchmark):\\n    if benchmark == \\\"lambada\\\":\\n        return sample[\\\"resps\\\"][0][0][0]\\n    resps = [r[0][0] for r in sample[\\\"resps\\\"]]\\n    if metric == \\\"acc_norm\\\":\\n        endings = sample[\\\"doc\\\"][\\\"endings\\\"]\\n        return max(r / max(len(e), 1) for r, e in zip(resps, endings))\\n    return max(resps)\\n\\n\\ndef load_data(benchmark):\\n    cfg = BENCHMARKS[benchmark]\\n    metric = cfg[\\\"metric\\\"]\\n    data = {\\\"pure_conf\\\": {}, \\\"pure_acc\\\": {}, \\\"hybrid_acc\\\": {}}\\n\\n    for arch in ARCHS:\\n        pp, hp = str(cfg[\\\"pure\\\"][arch]), str(cfg[\\\"hybrid\\\"][arch])\\n        if not Path(pp).exists() or not Path(hp).exists():\\n            print(f\\\"  MISSING: {pp} or {hp}\\\")\\n            return None\\n\\n        ps = load_jsonl(pp)\\n        hs = load_jsonl(hp)\\n        assert [s[\\\"doc_id\\\"] for s in ps] == [s[\\\"doc_id\\\"] for s in hs], \\\\\\n            f\\\"doc_id mismatch {benchmark}/{arch}\\\"\\n\\n        data[\\\"pure_conf\\\"][arch] = np.array([get_confidence(s, metric, benchmark) for s in ps])\\n        data[\\\"pure_acc\\\"][arch]  = np.array([int(s[metric]) for s in ps])\\n        data[\\\"hybrid_acc\\\"][arch] = np.array([int(s[metric]) for s in hs])\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013mLdncNjvh8kh8C4XCu8i5`</summary>

```json
{
  "server": "westb-48145",
  "command": "tail -n +80 /root/entrainment_gated_ft/analysis/e1_confidence_selection.py",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "76b93ca1-08a8-491a-bff5-ee867da22f1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DdPy2weAnnhxdF3bDC9J6C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 36893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1801
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

_source line 30 · 2026-05-23T17:06:37.421Z_

<details><summary>↩ Tool result · `toolu_013mLdncNjvh8kh8C4XCu8i5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n    ref = [s[\\\"doc_id\\\"] for s in load_jsonl(str(cfg[\\\"pure\\\"][\\\"GDN\\\"]))]\\n    for arch in [\\\"RetNet\\\", \\\"HGRN2\\\"]:\\n        other = [s[\\\"doc_id\\\"] for s in load_jsonl(str(cfg[\\\"pure\\\"][arch]))]\\n        assert ref == other, f\\\"Cross-arch mismatch {benchmark}: GDN vs {arch}\\\"\\n\\n    data[\\\"n\\\"] = len(ref)\\n    return data\\n\\n\\n# ── Strategies ──\\n\\ndef strat_max_confidence(data, train, test):\\n    conf  = np.column_stack([data[\\\"pure_conf\\\"][a] for a in ARCHS])\\n    hyb   = np.column_stack([data[\\\"hybrid_acc\\\"][a] for a in ARCHS])\\n    best  = np.argmax(conf[test], axis=1)\\n    return float(np.mean(hyb[test][np.arange(len(test)), best]))\\n\\n\\ndef strat_rescue_threshold(data, train, test):\\n    conf  = np.column_stack([data[\\\"pure_conf\\\"][a] for a in ARCHS])\\n    pure  = np.column_stack([data[\\\"pure_acc\\\"][a]  for a in ARCHS])\\n    hyb   = np.column_stack([data[\\\"hybrid_acc\\\"][a] for a in ARCHS])\\n    absconf = np.abs(conf)\\n\\n    tr_abs = absconf[train]\\n    thresholds = np.linspace(np.percentile(tr_abs, 2), np.percentile(tr_abs, 98), 100)\\n\\n    best_t, best_a = thresholds[0], -1\\n    for t in thresholds:\\n        dec = np.where(tr_abs > t, hyb[train], pure[train])\\n        a = np.mean(np.sum(dec, axis=1) >= 2)\\n        if a > best_a:\\n            best_a, best_t = a, t\\n\\n    te_abs = absconf[test]\\n    dec = np.where(te_abs > best_t, hyb[test], pure[test])\\n    return float(np.mean(np.sum(dec, axis=1) >= 2)), float(best_t)\\n\\n\\ndef strat_confidence_weighted(data, train, test):\\n    conf = np.column_stack([data[\\\"pure_conf\\\"][a] for a in ARCHS])\\n    hyb  = np.column_stack([data[\\\"hybrid_acc\\\"][a] for a in ARCHS])\\n    tc   = conf[test]\\n    th   = hyb[test]\\n    shifted = tc - np.max(tc, axis=1, keepdims=True)\\n    w = np.exp(shifted)\\n    w /= np.sum(w, axis=1, keepdims=True)\\n    return float(np.mean(np.sum(w * th, axis=1) >= 0.5))\\n\\n\\n# ── Baselines ──\\n\\ndef bl_mv(data, test):\\n    hyb = np.column_stack([data[\\\"hybrid_acc\\\"][a] for a in ARCHS])\\n    return float(np.mean(np.sum(hyb[test], axis=1) >= 2))\\n\\ndef bl_best_single(data, train, test):\\n    best = max(ARCHS, key=lambda a: np.mean(data[\\\"hybrid_acc\\\"][a][train]))\\n    return float(np.mean(data[\\\"hybrid_acc\\\"][best][test])), best\\n\\ndef bl_oracle(data, test):\\n    hyb = np.column_stack([data[\\\"hybrid_acc\\\"][a] for a in ARCHS])\\n    return float(np.mean(np.max(hyb[test], axis=1)))\\n\\ndef bl_random(data, test, rng):\\n    hyb = np.column_stack([data[\\\"hybrid_acc\\\"][a] for a in ARCHS])\\n    n = len(test)\\n    c = rng.integers(0, 3, size=n)\\n    return float(np.mean(hyb[test][np.arange(n), c]))\\n\\n\\n# ── Cross-validation ──\\n\\ndef run_cv(data, n_splits=10, seed=42):\\n    n = data[\\\"n\\\"]\\n    rng = np.random.default_rng(seed)\\n    idx = np.arange(n)\\n\\n    res = {k: [] for k in [\\n        \\\"max_confidence\\\", \\\"rescue_threshold\\\", \\\"confidence_weighted\\\",\\n        \\\"majority_vote\\\", \\\"best_single\\\", \\\"oracle\\\", \\\"random\\\"\\n    ]}\\n    threshs = []\\n\\n    for _ in range(n_splits):\\n        perm = rng.permutation(idx)\\n        h = n // 2\\n        tr, te = perm[:h], perm[h:]\\n\\n        res[\\\"max_confidence\\\"].append(strat_max_confidence(data, tr, te))\\n\\n        ra, rt = strat_rescue_threshold(data, tr, te)\\n        res[\\\"rescue_threshold\\\"].append(ra)\\n        threshs.append(rt)\\n\\n        res[\\\"confidence_weighted\\\"].append(strat_confidence_weighted(data, tr, te))\\n        res[\\\"majority_vote\\\"].append(bl_mv(data, te))\\n\\n        ba, _ = bl_best_single(data, tr, te)\\n        res[\\\"best_single\\\"].append(ba)\\n        res[\\\"oracle\\\"].append(bl_oracle(data, te))\\n        res[\\\"random\\\"].append(bl_random(data, te, rng))\\n\\n    return res, threshs\\n\\n\\ndef main():\\n    out = {\\n        \\\"analysis\\\": \\\"e1_confidence_selection\\\",\\n        \\\"date\\\": \\\"2026-05-22\\\",\\n        \\\"method\\\": {\\n            \\\"attention_ratio\\\": \\\"h3-1 (25%)\\\",\\n            \\\"architectures\\\": ARCHS,\\n            \\\"cv\\\": \\\"50/50 random split x 10 repeats\\\",\\n            \\\"confidence_measure\\\": {\\n                \\\"lambada\\\": \\\"target word loglikelihood\\\",\\n                \\\"hellaswag\\\": \\\"max char-length-normalized loglikelihood\\\",\\n                \\\"piqa\\\": \\\"max raw loglikelihood across choices\\\",\\n                \\\"arc_easy\\\": \\\"max raw loglikelihood across choices\\\",\\n            },\\n        },\\n        \\\"results\\\": {},\\n    }\\n\\n    for bm in BENCHMARKS:\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"Benchmark: {bm}\\\")\\n        print(f\\\"{'='*60}\\\")\\n\\n        data = load_data(bm)\\n        if data is None:\\n            print(\\\"  SKIPPED\\\")\\n            continue\\n\\n        print(f\\\"  N = {data['n']}\\\")\\n        for a in ARCHS:\\n            p = np.mean(data[\\\"pure_acc\\\"][a])\\n            h = np.mean(data[\\\"hybrid_acc\\\"][a])\\n            print(f\\\"  {a:8s}: pure={p:.4f}  h3-1={h:.4f}  delta={h-p:+.4f}\\\")\\n\\n        cv, threshs = run_cv(data)\\n\\n        mv_m = np.mean(cv[\\\"majority_vote\\\"])\\n        bs_m = np.mean(cv[\\\"best_single\\\"])\\n\\n        strats = {}\\n        for s in [\\\"max_confidence\\\", \\\"rescue_threshold\\\", \\\"confidence_weighted\\\"]:\\n            m, sd = np.mean(cv[s]), np.std(cv[s])\\n            strats[s] = {\\n                \\\"mean_acc\\\": round(m, 6),\\n                \\\"std_acc\\\": round(sd, 6),\\n                \\\"vs_mv_pp\\\": round((m - mv_m) * 100, 3),\\n                \\\"vs_best_single_pp\\\": round((m - bs_m) * 100, 3),\\n            }\\n            print(f\\\"  {s:25s}: {m:.4f} +/- {sd:.4f}  (vs MV: {(m-mv_m)*100:+.2f}pp)\\\")\\n\\n        if threshs:\\n            strats[\\\"rescue_threshold\\\"][\\\"mean_threshold\\\"] = round(float(np.mean(threshs)), 4)\\n            strats[\\\"rescue_threshold\\\"][\\\"std_threshold\\\"] = round(float(np.std(threshs)), 4)\\n            print(f\\\"  rescue threshold: {np.mean(threshs):.3f} +/- {np.std(threshs):.3f}\\\")\\n\\n        baselines = {}\\n        for b in [\\\"majority_vote\\\", \\\"best_single\\\", \\\"oracle\\\", \\\"random\\\"]:\\n            m, sd = np.mean(cv[b]), np.std(cv[b])\\n            baselines[f\\\"{b}_acc\\\"] = round(m, 6)\\n            baselines[f\\\"{b}_std\\\"] = round(sd, 6)\\n            print(f\\\"  {b:15s}: {m:.4f} +/- {sd:.4f}\\\")\\n\\n        per_arch = {}\\n        for a in ARCHS:\\n            per_arch[a] = {\\n                \\\"pure_acc\\\":   round(float(np.mean(data[\\\"pure_acc\\\"][a])), 6),\\n                \\\"hybrid_acc\\\": round(float(np.mean(data[\\\"hybrid_acc\\\"][a])), 6),\\n            }\\n\\n        out[\\\"results\\\"][bm] = {\\n            \\\"strategies\\\": strats,\\n            \\\"baselines\\\": baselines,\\n            \\\"per_arch\\\": per_arch,\\n            \\\"n_samples\\\": data[\\\"n\\\"],\\n        }\\n\\n    # Summary\\n    print(f\\\"\\\\n{'='*95}\\\")\\n    print(\\\"SUMMARY\\\")\\n    print(f\\\"{'='*95}\\\")\\n    hdr = f\\\"{'Benchmark':<12} {'MV':<8} {'BestSgl':<8} {'MaxConf':<15} {'Rescue':<15} {'CW-Vote':<15} {'Oracle':<8}\\\"\\n    print(hdr)\\n    print(\\\"-\\\" * 95)\\n    for bm, r in out[\\\"results\\\"].items():\\n        s, b = r[\\\"strategies\\\"], r[\\\"baselines\\\"]\\n        print(f\\\"{bm:<12} {b['majority_vote_acc']:.4f}  {b['best_single_acc']:.4f}  \\\"\\n              f\\\"{s['max_confidence']['mean_acc']:.4f}({s['max_confidence']['vs_mv_pp']:+.1f})  \\\"\\n              f\\\"{s['rescue_threshold']['mean_acc']:.4f}({s['rescue_threshold']['vs_mv_pp']:+.1f})  \\\"\\n              f\\\"{s['confidence_weighted']['mean_acc']:.4f}({s['confidence_weighted']['vs_mv_pp']:+.1f})  \\\"\\n              f\\\"{b['oracle_acc']:.4f}\\\")\\n\\n    out_path = BASE / \\\"results/e1_confidence_selection.json\\\"\\n    out_path.parent.mkdir(parents=True, exist_ok=True)\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(out, f, indent=2)\\n    print(f\\\"\\\\nSaved: {out_path}\\\")\\n\\n    return out\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.28}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "8909ccfc-7ce8-441f-92e0-8082e02baaee",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\n    ref = [s[\\\\\\\"doc_id\\\\\\\"] for s in load_jsonl(str(cfg[\\\\\\\"pure\\\\\\\"][\\\\\\\"GDN\\\\\\\"]))]\\\\n    for arch in [\\\\\\\"RetNet\\\\\\\", \\\\\\\"HGRN2\\\\\\\"]:\\\\n        other = [s[\\\\\\\"doc_id\\\\\\\"] for s in load_jsonl(str(cfg[\\\\\\\"pure\\\\\\\"][arch]))]\\\\n        assert ref == other, f\\\\\\\"Cross-arch mismatch {benchmark}: GDN vs {arch}\\\\\\\"\\\\n\\\\n    data[\\\\\\\"n\\\\\\\"] = len(ref)\\\\n    return data\\\\n\\\\n\\\\n# ── Strategies ──\\\\n\\\\ndef strat_max_confidence(data, train, test):\\\\n    conf  = np.column_stack([data[\\\\\\\"pure_conf\\\\\\\"][a] for a in ARCHS])\\\\n    hyb   = np.column_stack([data[\\\\\\\"hybrid_acc\\\\\\\"][a] for a in ARCHS])\\\\n    best  = np.argmax(conf[test], axis=1)\\\\n    return float(np.mean(hyb[test][np.arange(len(test)), best]))\\\\n\\\\n\\\\ndef strat_rescue_threshold(data, train, test):\\\\n    conf  = np.column_stack([data[\\\\\\\"pure_conf\\\\\\\"][a] for a in ARCHS])\\\\n    pure  = np.column_stack([data[\\\\\\\"pure_acc\\\\\\\"][a]  for a in ARCHS])\\\\n    hyb   = np.column_stack([data[\\\\\\\"hybrid_acc\\\\\\\"][a] for a in ARCHS])\\\\n    absconf = np.abs(conf)\\\\n\\\\n    tr_abs = absconf[train]\\\\n    thresholds = np.linspace(np.percentile(tr_abs, 2), np.percentile(tr_abs, 98), 100)\\\\n\\\\n    best_t, best_a = thresholds[0], -1\\\\n    for t in thresholds:\\\\n        dec = np.where(tr_abs > t, hyb[train], pure[train])\\\\n        a = np.mean(np.sum(dec, axis=1) >= 2)\\\\n        if a > best_a:\\\\n            best_a, best_t = a, t\\\\n\\\\n    te_abs = absconf[test]\\\\n    dec = np.where(te_abs > best_t, hyb[test], pure[test])\\\\n    return float(np.mean(np.sum(dec, axis=1) >= 2)), float(best_t)\\\\n\\\\n\\\\ndef strat_confidence_weighted(data, train, test):\\\\n    conf = np.column_stack([data[\\\\\\\"pure_conf\\\\\\\"][a] for a in ARCHS])\\\\n    hyb  = np.column_stack([data[\\\\\\\"hybrid_acc\\\\\\\"][a] for a in ARCHS])\\\\n    tc   = conf[test]\\\\n    th   = hyb[test]\\\\n    shifted = tc - np.max(tc, axis=1, keepdims=True)\\\\n    w = np.exp(shifted)\\\\n    w /= np.sum(w, axis=1, keepdims=True)\\\\n    return float(np.mean(np.sum(w * th, axis=1) >= 0.5))\\\\n\\\\n\\\\n# ── Baselines ──\\\\n\\\\ndef bl_mv(data, test):\\\\n    hyb = np.column_stack([data[\\\\\\\"hybrid_acc\\\\\\\"][a] for a in ARCHS])\\\\n    return float(np.mean(np.sum(hyb[test], axis=1) >= 2))\\\\n\\\\ndef bl_best_single(data, train, test):\\\\n    best = max(ARCHS, key=lambda a: np.mean(data[\\\\\\\"hybrid_acc\\\\\\\"][a][train]))\\\\n    return float(np.mean(data[\\\\\\\"hybrid_acc\\\\\\\"][best][test])), best\\\\n\\\\ndef bl_oracle(data, test):\\\\n    hyb = np.column_stack([data[\\\\\\\"hybrid_acc\\\\\\\"][a] for a in ARCHS])\\\\n    return float(np.mean(np.max(hyb[test], axis=1)))\\\\n\\\\ndef bl_random(data, test, rng):\\\\n    hyb = np.column_stack([data[\\\\\\\"hybrid_acc\\\\\\\"][a] for a in ARCHS])\\\\n    n = len(test)\\\\n    c = rng.integers(0, 3, size=n)\\\\n    return float(np.mean(hyb[test][np.arange(n), c]))\\\\n\\\\n\\\\n# ── Cross-validation ──\\\\n\\\\ndef run_cv(data, n_splits=10, seed=42):\\\\n    n = data[\\\\\\\"n\\\\\\\"]\\\\n    rng = np.random.default_rng(seed)\\\\n    idx = np.arange(n)\\\\n\\\\n    res = {k: [] for k in [\\\\n        \\\\\\\"max_confidence\\\\\\\", \\\\\\\"rescue_threshold\\\\\\\", \\\\\\\"confidence_weighted\\\\\\\",\\\\n        \\\\\\\"majority_vote\\\\\\\", \\\\\\\"best_single\\\\\\\", \\\\\\\"oracle\\\\\\\", \\\\\\\"random\\\\\\\"\\\\n    ]}\\\\n    threshs = []\\\\n\\\\n    for _ in range(n_splits):\\\\n        perm = rng.permutation(idx)\\\\n        h = n // 2\\\\n        tr, te = perm[:h], perm[h:]\\\\n\\\\n        res[\\\\\\\"max_confidence\\\\\\\"].append(strat_max_confidence(data, tr, te))\\\\n\\\\n        ra, rt = strat_rescue_threshold(data, tr, te)\\\\n        res[\\\\\\\"rescue_threshold\\\\\\\"].append(ra)\\\\n        threshs.append(rt)\\\\n\\\\n        res[\\\\\\\"confidence_weighted\\\\\\\"].append(strat_confidence_weighted(data, tr, te))\\\\n        res[\\\\\\\"majority_vote\\\\\\\"].append(bl_mv(data, te))\\\\n\\\\n        ba, _ = bl_best_single(data, tr, te)\\\\n        res[\\\\\\\"best_single\\\\\\\"].append(ba)\\\\n        res[\\\\\\\"oracle\\\\\\\"].append(bl_oracle(data, te))\\\\n        res[\\\\\\\"random\\\\\\\"].append(bl_random(data, te, rng))\\\\n\\\\n    return res, threshs\\\\n\\\\n\\\\ndef main():\\\\n    out = {\\\\n        \\\\\\\"analysis\\\\\\\": \\\\\\\"e1_confidence_selection\\\\\\\",\\\\n        \\\\\\\"date\\\\\\\": \\\\\\\"2026-05-22\\\\\\\",\\\\n        \\\\\\\"method\\\\\\\": {\\\\n            \\\\\\\"attention_ratio\\\\\\\": \\\\\\\"h3-1 (25%)\\\\\\\",\\\\n            \\\\\\\"architectures\\\\\\\": ARCHS,\\\\n            \\\\\\\"cv\\\\\\\": \\\\\\\"50/50 random split x 10 repeats\\\\\\\",\\\\n            \\\\\\\"confidence_measure\\\\\\\": {\\\\n                \\\\\\\"lambada\\\\\\\": \\\\\\\"target word loglikelihood\\\\\\\",\\\\n                \\\\\\\"hellaswag\\\\\\\": \\\\\\\"max char-length-normalized loglikelihood\\\\\\\",\\\\n                \\\\\\\"piqa\\\\\\\": \\\\\\\"max raw loglikelihood across choices\\\\\\\",\\\\n                \\\\\\\"arc_easy\\\\\\\": \\\\\\\"max raw loglikelihood across choices\\\\\\\",\\\\n            },\\\\n        },\\\\n        \\\\\\\"results\\\\\\\": {},\\\\n    }\\\\n\\\\n    for bm in BENCHMARKS:\\\\n        print(f\\\\\\\"\\\\\\\\n{'='*60}\\\\\\\")\\\\n        print(f\\\\\\\"Benchmark: {bm}\\\\\\\")\\\\n        print(f\\\\\\\"{'='*60}\\\\\\\")\\\\n\\\\n        data = load_data(bm)\\\\n        if data is None:\\\\n            print(\\\\\\\"  SKIPPED\\\\\\\")\\\\n            continue\\\\n\\\\n        print(f\\\\\\\"  N = {data['n']}\\\\\\\")\\\\n        for a in ARCHS:\\\\n            p = np.mean(data[\\\\\\\"pure_acc\\\\\\\"][a])\\\\n            h = np.mean(data[\\\\\\\"hybrid_acc\\\\\\\"][a])\\\\n            print(f\\\\\\\"  {a:8s}: pure={p:.4f}  h3-1={h:.4f}  delta={h-p:+.4f}\\\\\\\")\\\\n\\\\n        cv, threshs = run_cv(data)\\\\n\\\\n        mv_m = np.mean(cv[\\\\\\\"majority_vote\\\\\\\"])\\\\n        bs_m = np.mean(cv[\\\\\\\"best_single\\\\\\\"])\\\\n\\\\n        strats = {}\\\\n        for s in [\\\\\\\"max_confidence\\\\\\\", \\\\\\\"rescue_threshold\\\\\\\", \\\\\\\"confidence_weighted\\\\\\\"]:\\\\n            m, sd = np.mean(cv[s]), np.std(cv[s])\\\\n            strats[s] = {\\\\n                \\\\\\\"mean_acc\\\\\\\": round(m, 6),\\\\n                \\\\\\\"std_acc\\\\\\\": round(sd, 6),\\\\n                \\\\\\\"vs_mv_pp\\\\\\\": round((m - mv_m) * 100, 3),\\\\n                \\\\\\\"vs_best_single_pp\\\\\\\": round((m - bs_m) * 100, 3),\\\\n            }\\\\n            print(f\\\\\\\"  {s:25s}: {m:.4f} +/- {sd:.4f}  (vs MV: {(m-mv_m)*100:+.2f}pp)\\\\\\\")\\\\n\\\\n        if threshs:\\\\n            strats[\\\\\\\"rescue_threshold\\\\\\\"][\\\\\\\"mean_threshold\\\\\\\"] = round(float(np.mean(threshs)), 4)\\\\n            strats[\\\\\\\"rescue_threshold\\\\\\\"][\\\\\\\"std_threshold\\\\\\\"] = round(float(np.std(threshs)), 4)\\\\n            print(f\\\\\\\"  rescue threshold: {np.mean(threshs):.3f} +/- {np.std(threshs):.3f}\\\\\\\")\\\\n\\\\n        baselines = {}\\\\n        for b in [\\\\\\\"majority_vote\\\\\\\", \\\\\\\"best_single\\\\\\\", \\\\\\\"oracle\\\\\\\", \\\\\\\"random\\\\\\\"]:\\\\n            m, sd = np.mean(cv[b]), np.std(cv[b])\\\\n            baselines[f\\\\\\\"{b}_acc\\\\\\\"] = round(m, 6)\\\\n            baselines[f\\\\\\\"{b}_std\\\\\\\"] = round(sd, 6)\\\\n            print(f\\\\\\\"  {b:15s}: {m:.4f} +/- {sd:.4f}\\\\\\\")\\\\n\\\\n        per_arch = {}\\\\n        for a in ARCHS:\\\\n            per_arch[a] = {\\\\n                \\\\\\\"pure_acc\\\\\\\":   round(float(np.mean(data[\\\\\\\"pure_acc\\\\\\\"][a])), 6),\\\\n                \\\\\\\"hybrid_acc\\\\\\\": round(float(np.mean(data[\\\\\\\"hybrid_acc\\\\\\\"][a])), 6),\\\\n            }\\\\n\\\\n        out[\\\\\\\"results\\\\\\\"][bm] = {\\\\n            \\\\\\\"strategies\\\\\\\": strats,\\\\n            \\\\\\\"baselines\\\\\\\": baselines,\\\\n            \\\\\\\"per_arch\\\\\\\": per_arch,\\\\n            \\\\\\\"n_samples\\\\\\\": data[\\\\\\\"n\\\\\\\"],\\\\n        }\\\\n\\\\n    # Summary\\\\n    print(f\\\\\\\"\\\\\\\\n{'='*95}\\\\\\\")\\\\n    print(\\\\\\\"SUMMARY\\\\\\\")\\\\n    print(f\\\\\\\"{'='*95}\\\\\\\")\\\\n    hdr = f\\\\\\\"{'Benchmark':<12} {'MV':<8} {'BestSgl':<8} {'MaxConf':<15} {'Rescue':<15} {'CW-Vote':<15} {'Oracle':<8}\\\\\\\"\\\\n    print(hdr)\\\\n    print(\\\\\\\"-\\\\\\\" * 95)\\\\n    for bm, r in out[\\\\\\\"results\\\\\\\"].items():\\\\n        s, b = r[\\\\\\\"strategies\\\\\\\"], r[\\\\\\\"baselines\\\\\\\"]\\\\n        print(f\\\\\\\"{bm:<12} {b['majority_vote_acc']:.4f}  {b['best_single_acc']:.4f}  \\\\\\\"\\\\n              f\\\\\\\"{s['max_confidence']['mean_acc']:.4f}({s['max_confidence']['vs_mv_pp']:+.1f})  \\\\\\\"\\\\n              f\\\\\\\"{s['rescue_threshold']['mean_acc']:.4f}({s['rescue_threshold']['vs_mv_pp']:+.1f})  \\\\\\\"\\\\n              f\\\\\\\"{s['confidence_weighted']['mean_acc']:.4f}({s['confidence_weighted']['vs_mv_pp']:+.1f})  \\\\\\\"\\\\n              f\\\\\\\"{b['oracle_acc']:.4f}\\\\\\\")\\\\n\\\\n    out_path = BASE / \\\\\\\"results/e1_confidence_selection.json\\\\\\\"\\\\n    out_path.parent.mkdir(parents=True, exist_ok=True)\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(out, f, indent=2)\\\\n    print(f\\\\\\\"\\\\\\\\nSaved: {out_path}\\\\\\\")\\\\n\\\\n    return out\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.28}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\n    ref = [s[\\\"doc_id\\\"] for s in load_jsonl(str(cfg[\\\"pure\\\"][\\\"GDN\\\"]))]\\n    for arch in [\\\"RetNet\\\", \\\"HGRN2\\\"]:\\n        other = [s[\\\"doc_id\\\"] for s in load_jsonl(str(cfg[\\\"pure\\\"][arch]))]\\n        assert ref == other, f\\\"Cross-arch mismatch {benchmark}: GDN vs {arch}\\\"\\n\\n    data[\\\"n\\\"] = len(ref)\\n    return data\\n\\n\\n# ── Strategies ──\\n\\ndef strat_max_confidence(data, train, test):\\n    conf  = np.column_stack([data[\\\"pure_conf\\\"][a] for a in ARCHS])\\n    hyb   = np.column_stack([data[\\\"hybrid_acc\\\"][a] for a in ARCHS])\\n    best  = np.argmax(conf[test], axis=1)\\n    return float(np.mean(hyb[test][np.arange(len(test)), best]))\\n\\n\\ndef strat_rescue_threshold(data, train, test):\\n    conf  = np.column_stack([data[\\\"pure_conf\\\"][a] for a in ARCHS])\\n    pure  = np.column_stack([data[\\\"pure_acc\\\"][a]  for a in ARCHS])\\n    hyb   = np.column_stack([data[\\\"hybrid_acc\\\"][a] for a in ARCHS])\\n    absconf = np.abs(conf)\\n\\n    tr_abs = absconf[train]\\n    thresholds = np.linspace(np.percentile(tr_abs, 2), np.percentile(tr_abs, 98), 100)\\n\\n    best_t, best_a = thresholds[0], -1\\n    for t in thresholds:\\n        dec = np.where(tr_abs > t, hyb[train], pure[train])\\n        a = np.mean(np.sum(dec, axis=1) >= 2)\\n        if a > best_a:\\n            best_a, best_t = a, t\\n\\n    te_abs = absconf[test]\\n    dec = np.where(te_abs > best_t, hyb[test], pure[test])\\n    return float(np.mean(np.sum(dec, axis=1) >= 2)), float(best_t)\\n\\n\\ndef strat_confidence_weighted(data, train, test):\\n    conf = np.column_stack([data[\\\"pure_conf\\\"][a] for a in ARCHS])\\n    hyb  = np.column_stack([data[\\\"hybrid_acc\\\"][a] for a in ARCHS])\\n    tc   = conf[test]\\n    th   = hyb[test]\\n    shifted = tc - np.max(tc, axis=1, keepdims=True)\\n    w = np.exp(shifted)\\n    w /= np.sum(w, axis=1, keepdims=True)\\n    return float(np.mean(np.sum(w * th, axis=1) >= 0.5))\\n\\n\\n# ── Baselines ──\\n\\ndef bl_mv(data, test):\\n    hyb = np.column_stack([data[\\\"hybrid_acc\\\"][a] for a in ARCHS])\\n    return float(np.mean(np.sum(hyb[test], axis=1) >= 2))\\n\\ndef bl_best_single(data, train, test):\\n    best = max(ARCHS, key=lambda a: np.mean(data[\\\"hybrid_acc\\\"][a][train]))\\n    return float(np.mean(data[\\\"hybrid_acc\\\"][best][test])), best\\n\\ndef bl_oracle(data, test):\\n    hyb = np.column_stack([data[\\\"hybrid_acc\\\"][a] for a in ARCHS])\\n    return float(np.mean(np.max(hyb[test], axis=1)))\\n\\ndef bl_random(data, test, rng):\\n    hyb = np.column_stack([data[\\\"hybrid_acc\\\"][a] for a in ARCHS])\\n    n = len(test)\\n    c = rng.integers(0, 3, size=n)\\n    return float(np.mean(hyb[test][np.arange(n), c]))\\n\\n\\n# ── Cross-validation ──\\n\\ndef run_cv(data, n_splits=10, seed=42):\\n    n = data[\\\"n\\\"]\\n    rng = np.random.default_rng(seed)\\n    idx = np.arange(n)\\n\\n    res = {k: [] for k in [\\n        \\\"max_confidence\\\", \\\"rescue_threshold\\\", \\\"confidence_weighted\\\",\\n        \\\"majority_vote\\\", \\\"best_single\\\", \\\"oracle\\\", \\\"random\\\"\\n    ]}\\n    threshs = []\\n\\n    for _ in range(n_splits):\\n        perm = rng.permutation(idx)\\n        h = n // 2\\n        tr, te = perm[:h], perm[h:]\\n\\n        res[\\\"max_confidence\\\"].append(strat_max_confidence(data, tr, te))\\n\\n        ra, rt = strat_rescue_threshold(data, tr, te)\\n        res[\\\"rescue_threshold\\\"].append(ra)\\n        threshs.append(rt)\\n\\n        res[\\\"confidence_weighted\\\"].append(strat_confidence_weighted(data, tr, te))\\n        res[\\\"majority_vote\\\"].append(bl_mv(data, te))\\n\\n        ba, _ = bl_best_single(data, tr, te)\\n        res[\\\"best_single\\\"].append(ba)\\n        res[\\\"oracle\\\"].append(bl_oracle(data, te))\\n        res[\\\"random\\\"].append(bl_random(data, te, rng))\\n\\n    return res, threshs\\n\\n\\ndef main():\\n    out = {\\n        \\\"analysis\\\": \\\"e1_confidence_selection\\\",\\n        \\\"date\\\": \\\"2026-05-22\\\",\\n        \\\"method\\\": {\\n            \\\"attention_ratio\\\": \\\"h3-1 (25%)\\\",\\n            \\\"architectures\\\": ARCHS,\\n            \\\"cv\\\": \\\"50/50 random split x 10 repeats\\\",\\n            \\\"confidence_measure\\\": {\\n                \\\"lambada\\\": \\\"target word loglikelihood\\\",\\n                \\\"hellaswag\\\": \\\"max char-length-normalized loglikelihood\\\",\\n                \\\"piqa\\\": \\\"max raw loglikelihood across choices\\\",\\n                \\\"arc_easy\\\": \\\"max raw loglikelihood across choices\\\",\\n            },\\n        },\\n        \\\"results\\\": {},\\n    }\\n\\n    for bm in BENCHMARKS:\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"Benchmark: {bm}\\\")\\n        print(f\\\"{'='*60}\\\")\\n\\n        data = load_data(bm)\\n        if data is None:\\n            print(\\\"  SKIPPED\\\")\\n            continue\\n\\n        print(f\\\"  N = {data['n']}\\\")\\n        for a in ARCHS:\\n            p = np.mean(data[\\\"pure_acc\\\"][a])\\n            h = np.mean(data[\\\"hybrid_acc\\\"][a])\\n            print(f\\\"  {a:8s}: pure={p:.4f}  h3-1={h:.4f}  delta={h-p:+.4f}\\\")\\n\\n        cv, threshs = run_cv(data)\\n\\n        mv_m = np.mean(cv[\\\"majority_vote\\\"])\\n        bs_m = np.mean(cv[\\\"best_single\\\"])\\n\\n        strats = {}\\n        for s in [\\\"max_confidence\\\", \\\"rescue_threshold\\\", \\\"confidence_weighted\\\"]:\\n            m, sd = np.mean(cv[s]), np.std(cv[s])\\n            strats[s] = {\\n                \\\"mean_acc\\\": round(m, 6),\\n                \\\"std_acc\\\": round(sd, 6),\\n                \\\"vs_mv_pp\\\": round((m - mv_m) * 100, 3),\\n                \\\"vs_best_single_pp\\\": round((m - bs_m) * 100, 3),\\n            }\\n            print(f\\\"  {s:25s}: {m:.4f} +/- {sd:.4f}  (vs MV: {(m-mv_m)*100:+.2f}pp)\\\")\\n\\n        if threshs:\\n            strats[\\\"rescue_threshold\\\"][\\\"mean_threshold\\\"] = round(float(np.mean(threshs)), 4)\\n            strats[\\\"rescue_threshold\\\"][\\\"std_threshold\\\"] = round(float(np.std(threshs)), 4)\\n            print(f\\\"  rescue threshold: {np.mean(threshs):.3f} +/- {np.std(threshs):.3f}\\\")\\n\\n        baselines = {}\\n        for b in [\\\"majority_vote\\\", \\\"best_single\\\", \\\"oracle\\\", \\\"random\\\"]:\\n            m, sd = np.mean(cv[b]), np.std(cv[b])\\n            baselines[f\\\"{b}_acc\\\"] = round(m, 6)\\n            baselines[f\\\"{b}_std\\\"] = round(sd, 6)\\n            print(f\\\"  {b:15s}: {m:.4f} +/- {sd:.4f}\\\")\\n\\n        per_arch = {}\\n        for a in ARCHS:\\n            per_arch[a] = {\\n                \\\"pure_acc\\\":   round(float(np.mean(data[\\\"pure_acc\\\"][a])), 6),\\n                \\\"hybrid_acc\\\": round(float(np.mean(data[\\\"hybrid_acc\\\"][a])), 6),\\n            }\\n\\n        out[\\\"results\\\"][bm] = {\\n            \\\"strategies\\\": strats,\\n            \\\"baselines\\\": baselines,\\n            \\\"per_arch\\\": per_arch,\\n            \\\"n_samples\\\": data[\\\"n\\\"],\\n        }\\n\\n    # Summary\\n    print(f\\\"\\\\n{'='*95}\\\")\\n    print(\\\"SUMMARY\\\")\\n    print(f\\\"{'='*95}\\\")\\n    hdr = f\\\"{'Benchmark':<12} {'MV':<8} {'BestSgl':<8} {'MaxConf':<15} {'Rescue':<15} {'CW-Vote':<15} {'Oracle':<8}\\\"\\n    print(hdr)\\n    print(\\\"-\\\" * 95)\\n    for bm, r in out[\\\"results\\\"].items():\\n        s, b = r[\\\"strategies\\\"], r[\\\"baselines\\\"]\\n        print(f\\\"{bm:<12} {b['majority_vote_acc']:.4f}  {b['best_single_acc']:.4f}  \\\"\\n              f\\\"{s['max_confidence']['mean_acc']:.4f}({s['max_confidence']['vs_mv_pp']:+.1f})  \\\"\\n              f\\\"{s['rescue_threshold']['mean_acc']:.4f}({s['rescue_threshold']['vs_mv_pp']:+.1f})  \\\"\\n              f\\\"{s['confidence_weighted']['mean_acc']:.4f}({s['confidence_weighted']['vs_mv_pp']:+.1f})  \\\"\\n              f\\\"{b['oracle_acc']:.4f}\\\")\\n\\n    out_path = BASE / \\\"results/e1_confidence_selection.json\\\"\\n    out_path.parent.mkdir(parents=True, exist_ok=True)\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(out, f, indent=2)\\n    print(f\\\"\\\\nSaved: {out_path}\\\")\\n\\n    return out\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.28}}"
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
Now I can see the full script. The key observation is:

1. `run_cv` generates per-split data (`cv` dict with lists of per-split accuracies for each strategy), but the script only saves aggregated mean/std to the output JSON.
2. The raw per-split data is never saved.

However, the analysis script is deterministic (seed=42), operates on sample-level JSONL files that exist on the server, and can be re-run. So I can modify the script to output per-split data, or write a new inline script to compute the paired t-test.


I'll write a Python script that loads the same JSONL data, runs the identical 50/50 random split cross-validation with 10 repeats, collects the per-split accuracies for both routing strategies, and performs a paired t-test to determine if the difference is statistically significant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "3e0ea32d-3e1b-4e0e-b9ef-ffd9deea4e04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1JjD23V4BrFAgpYh47iHM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3577,
      "cache_read_input_tokens": 38694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3577
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

找到了。`e1_confidence_selection.py` 的 `run_cv` 函数生成了逐 split 数据但只保存了 mean/std。脚本是确定性的（seed=42），可以重跑提取 per-split 数据做 paired t-test。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "35809c58-41ac-4552-96be-5a5eeea97188",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1JjD23V4BrFAgpYh47iHM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3577,
      "cache_read_input_tokens": 38694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3577
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015aCTJYVi1p8ddaMXy3vFz6`</summary>

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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "ac2472ae-c57d-4743-8f29-dd068e46767f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1JjD23V4BrFAgpYh47iHM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3577,
      "cache_read_input_tokens": 38694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3577
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 34 · 2026-05-23T17:06:51.153Z_

<details><summary>↩ Tool result · `toolu_015aCTJYVi1p8ddaMXy3vFz6`</summary>

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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "9c1db01b-bdf3-41b1-bd1b-45391d118390",
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

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01CnahctTgMtXBvHRajm9J8w`</summary>

```json
{
  "server": "westb-48145",
  "command": "cd /root/entrainment_gated_ft && python3 -c \"\nimport json, numpy as np\nfrom pathlib import Path\nfrom scipy import stats\n\nBASE = Path('/root/entrainment_gated_ft')\nLM = BASE / 'lm_eval_clean'\nARCHS = ['GDN', 'RetNet', 'HGRN2']\nFULL_NAMES = {'GDN': 'GatedDeltaNet', 'RetNet': 'RetNet', 'HGRN2': 'HGRN2'}\n\nBENCHMARKS = {\n    'lambada': {\n        'metric': 'acc',\n        'pure': {\n            'GDN':    LM / 'exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl',\n            'RetNet': LM / 'exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl',\n            'HGRN2':  LM / 'exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl',\n        },\n        'hybrid': {\n            'GDN':    LM / '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl',\n            'RetNet': LM / 'exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl',\n            'HGRN2':  LM / 'exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl',\n        },\n    },\n    'hellaswag': {\n        'metric': 'acc_norm',\n        'pure':   {a: LM / f'hellaswag/1.3B-100B-{FULL_NAMES[a]}-pure/samples/hellaswag.jsonl' for a in ARCHS},\n        'hybrid': {a: LM / f'hellaswag/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/hellaswag.jsonl' for a in ARCHS},\n    },\n    'piqa': {\n        'metric': 'acc',\n        'pure':   {a: LM / f'piqa/1.3B-100B-{FULL_NAMES[a]}-pure/samples/piqa.jsonl' for a in ARCHS},\n        'hybrid': {a: LM / f'piqa/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/piqa.jsonl' for a in ARCHS},\n    },\n    'arc_easy': {\n        'metric': 'acc',\n        'pure':   {a: LM / f'arc_easy/1.3B-100B-{FULL_NAMES[a]}-pure/samples/arc_easy.jsonl' for a in ARCHS},\n        'hybrid': {a: LM / f'arc_easy/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/arc_easy.jsonl' for a in ARCHS},\n    },\n}\n\ndef load_jsonl(path):\n    with open(path) as f:\n        data = [json.loads(line) for line in f]\n    data.sort(key=lambda x: x['doc_id'])\n    return data\n\ndef get_confidence(sample, metric, benchmark):\n    if benchmark == 'lambada':\n        return sample['resps'][0][0][0]\n    resps = [r[0][0] for r in sample['resps']]\n    if metric == 'acc_norm':\n        endings = sample['doc']['endings']\n        return max(r / max(len(e), 1) for r, e in zip(resps, endings))\n    return max(resps)\n\ndef load_data(benchmark):\n    cfg = BENCHMARKS[benchmark]\n    metric = cfg['metric']\n    data = {'pure_conf': {}, 'pure_acc': {}, 'hybrid_acc': {}}\n    for arch in ARCHS:\n        pp, hp = str(cfg['pure'][arch]), str(cfg['hybrid'][arch])\n        if not Path(pp).exists() or not Path(hp).exists():\n            return None\n        ps = load_jsonl(pp)\n        hs = load_jsonl(hp)\n        data['pure_conf'][arch] = np.array([get_confidence(s, metric, benchmark) for s in ps])\n        data['pure_acc'][arch]  = np.array([int(s[metric]) for s in ps])\n        data['hybrid_acc'][arch] = np.array([int(s[metric]) for s in hs])\n    data['n'] = len(load_jsonl(str(cfg['pure']['GDN'])))\n    return data\n\ndef strat_rescue_threshold(data, train, test):\n    conf  = np.column_stack([data['pure_conf'][a] for a in ARCHS])\n    pure  = np.column_stack([data['pure_acc'][a]  for a in ARCHS])\n    hyb   = np.column_stack([data['hybrid_acc'][a] for a in ARCHS])\n    absconf = np.abs(conf)\n    tr_abs = absconf[train]\n    thresholds = np.linspace(np.percentile(tr_abs, 2), np.percentile(tr_abs, 98), 100)\n    best_t, best_a = thresholds[0], -1\n    for t in thresholds:\n        dec = np.where(tr_abs > t, hyb[train], pure[train])\n        a = np.mean(np.sum(dec, axis=1) >= 2)\n        if a > best_a:\n            best_a, best_t = a, t\n    te_abs = absconf[test]\n    dec = np.where(te_abs > best_t, hyb[test], pure[test])\n    return float(np.mean(np.sum(dec, axis=1) >= 2))\n\ndef bl_mv(data, test):\n    hyb = np.column_stack([data['hybrid_acc'][a] for a in ARCHS])\n    return float(np.mean(np.sum(hyb[test], axis=1) >= 2))\n\nprint('='*80)\nprint('PAIRED T-TEST: rescue_threshold vs majority_vote (per-split)')\nprint('='*80)\n\nall_results = {}\n\nfor bm in BENCHMARKS:\n    data = load_data(bm)\n    if data is None:\n        print(f'{bm}: SKIPPED (missing data)')\n        continue\n\n    n = data['n']\n    rng = np.random.default_rng(42)\n    idx = np.arange(n)\n    n_splits = 10\n\n    routing_accs = []\n    mv_accs = []\n\n    for i in range(n_splits):\n        perm = rng.permutation(idx)\n        h = n // 2\n        tr, te = perm[:h], perm[h:]\n        routing_accs.append(strat_rescue_threshold(data, tr, te))\n        mv_accs.append(bl_mv(data, te))\n\n    routing_accs = np.array(routing_accs)\n    mv_accs = np.array(mv_accs)\n    diffs = routing_accs - mv_accs\n\n    t_stat, p_val = stats.ttest_rel(routing_accs, mv_accs)\n    se = stats.sem(diffs)\n    ci = stats.t.interval(0.95, len(diffs)-1, loc=np.mean(diffs), scale=se)\n\n    print(f'\\n{bm} (n_splits={n_splits}, n_samples={n})')\n    print(f'  Per-split routing:  {routing_accs}')\n    print(f'  Per-split MV:       {mv_accs}')\n    print(f'  Per-split diff:     {diffs}')\n    print(f'  mean_diff = {np.mean(diffs):.6f} ({np.mean(diffs)*100:+.3f} pp)')\n    print(f'  t = {t_stat:.4f}, p = {p_val:.6f}')\n    print(f'  95% CI: [{ci[0]:.6f}, {ci[1]:.6f}] = [{ci[0]*100:.3f}, {ci[1]*100:.3f}] pp')\n    sig = 'YES' if p_val < 0.05 else 'NO'\n    print(f'  Significant (p<0.05): {sig}')\n\n    all_results[bm] = {\n        'routing_accs': routing_accs.tolist(),\n        'mv_accs': mv_accs.tolist(),\n        'diffs': diffs.tolist(),\n        'mean_diff': float(np.mean(diffs)),\n        'mean_diff_pp': float(np.mean(diffs)*100),\n        't_stat': float(t_stat),\n        'p_value': float(p_val),\n        'ci_95_low': float(ci[0]),\n        'ci_95_high': float(ci[1]),\n        'n_splits': n_splits,\n        'n_samples': n,\n    }\n\nprint('\\n' + '='*80)\nprint('SUMMARY TABLE')\nprint('='*80)\nprint(f'{\\\"Benchmark\\\":<12} {\\\"mean_diff(pp)\\\":>14} {\\\"t\\\":>8} {\\\"p\\\":>10} {\\\"95% CI (pp)\\\":>22} {\\\"sig?\\\":>6}')\nprint('-'*75)\nfor bm, r in all_results.items():\n    sig = '*' if r['p_value'] < 0.05 else ''\n    if r['p_value'] < 0.01: sig = '**'\n    if r['p_value'] < 0.001: sig = '***'\n    print(f'{bm:<12} {r[\\\"mean_diff_pp\\\"]:>+13.3f} {r[\\\"t_stat\\\"]:>8.3f} {r[\\\"p_value\\\"]:>10.6f} [{r[\\\"ci_95_low\\\"]*100:>+7.3f}, {r[\\\"ci_95_high\\\"]*100:>+7.3f}] {sig:>6}')\n\n# Save\nout_path = BASE / 'results/e1_paired_ttest.json'\nwith open(out_path, 'w') as f:\n    json.dump(all_results, f, indent=2)\nprint(f'\\nSaved: {out_path}')\n\"\n",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "77438952-eb66-4286-a9d8-7e341817935f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PB3SeGT1beU3wKjAdPQ5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 42271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 689
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

_source line 36 · 2026-05-23T17:07:33.605Z_

<details><summary>↩ Tool result · `toolu_01CnahctTgMtXBvHRajm9J8w`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/entrainment_gated_ft && python3 -c \\\"\\\\nimport json, numpy as np\\\\nfrom pathlib import Path\\\\nfrom scipy import stats\\\\n\\\\nBASE = Path(\\\\'/root/entrainment_gated_ft\\\\')\\\\nLM = BASE / \\\\'lm_eval_clean\\\\'\\\\nARCHS = [\\\\'GDN\\\\', \\\\'RetNet\\\\', \\\\'HGRN2\\\\']\\\\nFULL_NAMES = {\\\\'GDN\\\\': \\\\'GatedDeltaNet\\\\', \\\\'RetNet\\\\': \\\\'RetNet\\\\', \\\\'HGRN2\\\\': \\\\'HGRN2\\\\'}\\\\n\\\\nBENCHMARKS = {\\\\n    \\\\'lambada\\\\': {\\\\n        \\\\'metric\\\\': \\\\'acc\\\\',\\\\n        \\\\'pure\\\\': {\\\\n            \\\\'GDN\\\\':    LM / \\\\'exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\\\\',\\\\n            \\\\'RetNet\\\\': LM / \\\\'exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\\\\',\\\\n            \\\\'HGRN2\\\\':  LM / \\\\'exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\\\\',\\\\n        },\\\\n        \\\\'hybrid\\\\': {\\\\n            \\\\'GDN\\\\':    LM / \\\\'1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\\\\',\\\\n            \\\\'RetNet\\\\': LM / \\\\'exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\\\\',\\\\n            \\\\'HGRN2\\\\':  LM / \\\\'exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\\\\',\\\\n        },\\\\n    },\\\\n    \\\\'hellaswag\\\\': {\\\\n        \\\\'metric\\\\': \\\\'acc_norm\\\\',\\\\n        \\\\'pure\\\\':   {a: LM / f\\\\'hellaswag/1.3B-100B-{FULL_NAMES[a]}-pure/samples/hellaswag.jsonl\\\\' for a in ARCHS},\\\\n        \\\\'hybrid\\\\': {a: LM / f\\\\'hellaswag/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/hellaswag.jsonl\\\\' for a in ARCHS},\\\\n    },\\\\n    \\\\'piqa\\\\': {\\\\n        \\\\'metric\\\\': \\\\'acc\\\\',\\\\n        \\\\'pure\\\\':   {a: LM / f\\\\'piqa/1.3B-100B-{FULL_NAMES[a]}-pure/samples/piqa.jsonl\\\\' for a in ARCHS},\\\\n        \\\\'hybrid\\\\': {a: LM / f\\\\'piqa/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/piqa.jsonl\\\\' for a in ARCHS},\\\\n    },\\\\n    \\\\'arc_easy\\\\': {\\\\n        \\\\'metric\\\\': \\\\'acc\\\\',\\\\n        \\\\'pure\\\\':   {a: LM / f\\\\'arc_easy/1.3B-100B-{FULL_NAMES[a]}-pure/samples/arc_easy.jsonl\\\\' for a in ARCHS},\\\\n        \\\\'hybrid\\\\': {a: LM / f\\\\'arc_easy/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/arc_easy.jsonl\\\\' for a in ARCHS},\\\\n    },\\\\n}\\\\n\\\\ndef load_jsonl(path):\\\\n    with open(path) as f:\\\\n        data = [json.loads(line) for line in f]\\\\n    data.sort(key=lambda x: x[\\\\'doc_id\\\\'])\\\\n    return data\\\\n\\\\ndef get_confidence(sample, metric, benchmark):\\\\n    if benchmark == \\\\'lambada\\\\':\\\\n        return sample[\\\\'resps\\\\'][0][0][0]\\\\n    resps = [r[0][0] for r in sample[\\\\'resps\\\\']]\\\\n    if metric == \\\\'acc_norm\\\\':\\\\n        endings = sample[\\\\'doc\\\\'][\\\\'endings\\\\']\\\\n        return max(r / max(len(e), 1) for r, e in zip(resps, endings))\\\\n    return max(resps)\\\\n\\\\ndef load_data(benchmark):\\\\n    cfg = BENCHMARKS[benchmark]\\\\n    metric = cfg[\\\\'metric\\\\']\\\\n    data = {\\\\'pure_conf\\\\': {}, \\\\'pure_acc\\\\': {}, \\\\'hybrid_acc\\\\': {}}\\\\n    for arch in ARCHS:\\\\n        pp, hp = str(cfg[\\\\'pure\\\\'][arch]), str(cfg[\\\\'hybrid\\\\'][arch])\\\\n        if not Path(pp).exists() or not Path(hp).exists():\\\\n            return None\\\\n        ps = load_jsonl(pp)\\\\n        hs = load_jsonl(hp)\\\\n        data[\\\\'pure_conf\\\\'][arch] = np.array([get_confidence(s, metric, benchmark) for s in ps])\\\\n        data[\\\\'pure_acc\\\\'][arch]  = np.array([int(s[metric]) for s in ps])\\\\n        data[\\\\'hybrid_acc\\\\'][arch] = np.array([int(s[metric]) for s in hs])\\\\n    data[\\\\'n\\\\'] = len(load_jsonl(str(cfg[\\\\'pure\\\\'][\\\\'GDN\\\\'])))\\\\n    return data\\\\n\\\\ndef strat_rescue_threshold(data, train, test):\\\\n    conf  = np.column_stack([data[\\\\'pure_conf\\\\'][a] for a in ARCHS])\\\\n    pure  = np.column_stack([data[\\\\'pure_acc\\\\'][a]  for a in ARCHS])\\\\n    hyb   = np.column_stack([data[\\\\'hybrid_acc\\\\'][a] for a in ARCHS])\\\\n    absconf = np.abs(conf)\\\\n    tr_abs = absconf[train]\\\\n    thresholds = np.linspace(np.percentile(tr_abs, 2), np.percentile(tr_abs, 98), 100)\\\\n    best_t, best_a = thresholds[0], -1\\\\n    for t in thresholds:\\\\n        dec = np.where(tr_abs > t, hyb[train], pure[train])\\\\n        a = np.mean(np.sum(dec, axis=1) >= 2)\\\\n        if a > best_a:\\\\n            best_a, best_t = a, t\\\\n    te_abs = absconf[test]\\\\n    dec = np.where(te_abs > best_t, hyb[test], pure[test])\\\\n    return float(np.mean(np.sum(dec, axis=1) >= 2))\\\\n\\\\ndef bl_mv(data, test):\\\\n    hyb = np.column_stack([data[\\\\'hybrid_acc\\\\'][a] for a in ARCHS])\\\\n    return float(np.mean(np.sum(hyb[test], axis=1) >= 2))\\\\n\\\\nprint(\\\\'=\\\\'*80)\\\\nprint(\\\\'PAIRED T-TEST: rescue_threshold vs majority_vote (per-split)\\\\')\\\\nprint(\\\\'=\\\\'*80)\\\\n\\\\nall_results = {}\\\\n\\\\nfor bm in BENCHMARKS:\\\\n    data = load_data(bm)\\\\n    if data is None:\\\\n        print(f\\\\'{bm}: SKIPPED (missing data)\\\\')\\\\n        continue\\\\n\\\\n    n = data[\\\\'n\\\\']\\\\n    rng = np.random.default_rng(42)\\\\n    idx = np.arange(n)\\\\n    n_splits = 10\\\\n\\\\n    routing_accs = []\\\\n    mv_accs = []\\\\n\\\\n    for i in range(n_splits):\\\\n        perm = rng.permutation(idx)\\\\n        h = n // 2\\\\n        tr, te = perm[:h], perm[h:]\\\\n        routing_accs.append(strat_rescue_threshold(data, tr, te))\\\\n        mv_accs.append(bl_mv(data, te))\\\\n\\\\n    routing_accs = np.array(routing_accs)\\\\n    mv_accs = np.array(mv_accs)\\\\n    diffs = routing_accs - mv_accs\\\\n\\\\n    t_stat, p_val = stats.ttest_rel(routing_accs, mv_accs)\\\\n    se = stats.sem(diffs)\\\\n    ci = stats.t.interval(0.95, len(diffs)-1, loc=np.mean(diffs), scale=se)\\\\n\\\\n    print(f\\\\'\\\\\\\\n{bm} (n_splits={n_splits}, n_samples={n})\\\\')\\\\n    print(f\\\\'  Per-split routing:  {routing_accs}\\\\')\\\\n    print(f\\\\'  Per-split MV:       {mv_accs}\\\\')\\\\n    print(f\\\\'  Per-split diff:     {diffs}\\\\')\\\\n    print(f\\\\'  mean_diff = {np.mean(diffs):.6f} ({np.mean(diffs)*100:+.3f} pp)\\\\')\\\\n    print(f\\\\'  t = {t_stat:.4f}, p = {p_val:.6f}\\\\')\\\\n    print(f\\\\'  95% CI: [{ci[0]:.6f}, {ci[1]:.6f}] = [{ci[0]*100:.3f}, {ci[1]*100:.3f}] pp\\\\')\\\\n    sig = \\\\'YES\\\\' if p_val < 0.05 else \\\\'NO\\\\'\\\\n    print(f\\\\'  Significant (p<0.05): {sig}\\\\')\\\\n\\\\n    all_results[bm] = {\\\\n        \\\\'routing_accs\\\\': routing_accs.tolist(),\\\\n        \\\\'mv_accs\\\\': mv_accs.tolist(),\\\\n        \\\\'diffs\\\\': diffs.tolist(),\\\\n        \\\\'mean_diff\\\\': float(np.mean(diffs)),\\\\n        \\\\'mean_diff_pp\\\\': float(np.mean(diffs)*100),\\\\n        \\\\'t_stat\\\\': float(t_stat),\\\\n        \\\\'p_value\\\\': float(p_val),\\\\n        \\\\'ci_95_low\\\\': float(ci[0]),\\\\n        \\\\'ci_95_high\\\\': float(ci[1]),\\\\n        \\\\'n_splits\\\\': n_splits,\\\\n        \\\\'n_samples\\\\': n,\\\\n    }\\\\n\\\\nprint(\\\\'\\\\\\\\n\\\\' + \\\\'=\\\\'*80)\\\\nprint(\\\\'SUMMARY TABLE\\\\')\\\\nprint(\\\\'=\\\\'*80)\\\\nprint(f\\\\'{\\\\\\\\\\\"Benchmark\\\\\\\\\\\":<12} {\\\\\\\\\\\"mean_diff(pp)\\\\\\\\\\\":>14} {\\\\\\\\\\\"t\\\\\\\\\\\":>8} {\\\\\\\\\\\"p\\\\\\\\\\\":>10} {\\\\\\\\\\\"95% CI (pp)\\\\\\\\\\\":>22} {\\\\\\\\\\\"sig?\\\\\\\\\\\":>6}\\\\')\\\\nprint(\\\\'-\\\\'*75)\\\\nfor bm, r in all_results.items():\\\\n    sig = \\\\'*\\\\' if r[\\\\'p_value\\\\'] < 0.05 else \\\\'\\\\'\\\\n    if r[\\\\'p_value\\\\'] < 0.01: sig = \\\\'**\\\\'\\\\n    if r[\\\\'p_value\\\\'] < 0.001: sig = \\\\'***\\\\'\\\\n    print(f\\\\'{bm:<12} {r[\\\\\\\\\\\"mean_diff_pp\\\\\\\\\\\"]:>+13.3f} {r[\\\\\\\\\\\"t_stat\\\\\\\\\\\"]:>8.3f} {r[\\\\\\\\\\\"p_value\\\\\\\\\\\"]:>10.6f} [{r[\\\\\\\\\\\"ci_95_low\\\\\\\\\\\"]*100:>+7.3f}, {r[\\\\\\\\\\\"ci_95_high\\\\\\\\\\\"]*100:>+7.3f}] {sig:>6}\\\\')\\\\n\\\\n# Save\\\\nout_path = BASE / \\\\'results/e1_paired_ttest.json\\\\'\\\\nwith open(out_path, \\\\'w\\\\') as f:\\\\n    json.dump(all_results, f, indent=2)\\\\nprint(f\\\\'\\\\\\\\nSaved: {out_path}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "6024ee5b-70c4-41a5-b855-b1e384f590d6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'cd /root/entrainment_gated_ft && python3 -c \\\\\\\"\\\\\\\\nimport json, numpy as np\\\\\\\\nfrom pathlib import Path\\\\\\\\nfrom scipy import stats\\\\\\\\n\\\\\\\\nBASE = Path(\\\\\\\\'/root/entrainment_gated_ft\\\\\\\\')\\\\\\\\nLM = BASE / \\\\\\\\'lm_eval_clean\\\\\\\\'\\\\\\\\nARCHS = [\\\\\\\\'GDN\\\\\\\\', \\\\\\\\'RetNet\\\\\\\\', \\\\\\\\'HGRN2\\\\\\\\']\\\\\\\\nFULL_NAMES = {\\\\\\\\'GDN\\\\\\\\': \\\\\\\\'GatedDeltaNet\\\\\\\\', \\\\\\\\'RetNet\\\\\\\\': \\\\\\\\'RetNet\\\\\\\\', \\\\\\\\'HGRN2\\\\\\\\': \\\\\\\\'HGRN2\\\\\\\\'}\\\\\\\\n\\\\\\\\nBENCHMARKS = {\\\\\\\\n    \\\\\\\\'lambada\\\\\\\\': {\\\\\\\\n        \\\\\\\\'metric\\\\\\\\': \\\\\\\\'acc\\\\\\\\',\\\\\\\\n        \\\\\\\\'pure\\\\\\\\': {\\\\\\\\n            \\\\\\\\'GDN\\\\\\\\':    LM / \\\\\\\\'exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\\\\\\\\',\\\\\\\\n            \\\\\\\\'RetNet\\\\\\\\': LM / \\\\\\\\'exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\\\\\\\\',\\\\\\\\n            \\\\\\\\'HGRN2\\\\\\\\':  LM / \\\\\\\\'exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\\\\\\\\',\\\\\\\\n        },\\\\\\\\n        \\\\\\\\'hybrid\\\\\\\\': {\\\\\\\\n            \\\\\\\\'GDN\\\\\\\\':    LM / \\\\\\\\'1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\\\\\\\\',\\\\\\\\n            \\\\\\\\'RetNet\\\\\\\\': LM / \\\\\\\\'exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\\\\\\\\',\\\\\\\\n            \\\\\\\\'HGRN2\\\\\\\\':  LM / \\\\\\\\'exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\\\\\\\\',\\\\\\\\n        },\\\\\\\\n    },\\\\\\\\n    \\\\\\\\'hellaswag\\\\\\\\': {\\\\\\\\n        \\\\\\\\'metric\\\\\\\\': \\\\\\\\'acc_norm\\\\\\\\',\\\\\\\\n        \\\\\\\\'pure\\\\\\\\':   {a: LM / f\\\\\\\\'hellaswag/1.3B-100B-{FULL_NAMES[a]}-pure/samples/hellaswag.jsonl\\\\\\\\' for a in ARCHS},\\\\\\\\n        \\\\\\\\'hybrid\\\\\\\\': {a: LM / f\\\\\\\\'hellaswag/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/hellaswag.jsonl\\\\\\\\' for a in ARCHS},\\\\\\\\n    },\\\\\\\\n    \\\\\\\\'piqa\\\\\\\\': {\\\\\\\\n        \\\\\\\\'metric\\\\\\\\': \\\\\\\\'acc\\\\\\\\',\\\\\\\\n        \\\\\\\\'pure\\\\\\\\':   {a: LM / f\\\\\\\\'piqa/1.3B-100B-{FULL_NAMES[a]}-pure/samples/piqa.jsonl\\\\\\\\' for a in ARCHS},\\\\\\\\n        \\\\\\\\'hybrid\\\\\\\\': {a: LM / f\\\\\\\\'piqa/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/piqa.jsonl\\\\\\\\' for a in ARCHS},\\\\\\\\n    },\\\\\\\\n    \\\\\\\\'arc_easy\\\\\\\\': {\\\\\\\\n        \\\\\\\\'metric\\\\\\\\': \\\\\\\\'acc\\\\\\\\',\\\\\\\\n        \\\\\\\\'pure\\\\\\\\':   {a: LM / f\\\\\\\\'arc_easy/1.3B-100B-{FULL_NAMES[a]}-pure/samples/arc_easy.jsonl\\\\\\\\' for a in ARCHS},\\\\\\\\n        \\\\\\\\'hybrid\\\\\\\\': {a: LM / f\\\\\\\\'arc_easy/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/arc_easy.jsonl\\\\\\\\' for a in ARCHS},\\\\\\\\n    },\\\\\\\\n}\\\\\\\\n\\\\\\\\ndef load_jsonl(path):\\\\\\\\n    with open(path) as f:\\\\\\\\n        data = [json.loads(line) for line in f]\\\\\\\\n    data.sort(key=lambda x: x[\\\\\\\\'doc_id\\\\\\\\'])\\\\\\\\n    return data\\\\\\\\n\\\\\\\\ndef get_confidence(sample, metric, benchmark):\\\\\\\\n    if benchmark == \\\\\\\\'lambada\\\\\\\\':\\\\\\\\n        return sample[\\\\\\\\'resps\\\\\\\\'][0][0][0]\\\\\\\\n    resps = [r[0][0] for r in sample[\\\\\\\\'resps\\\\\\\\']]\\\\\\\\n    if metric == \\\\\\\\'acc_norm\\\\\\\\':\\\\\\\\n        endings = sample[\\\\\\\\'doc\\\\\\\\'][\\\\\\\\'endings\\\\\\\\']\\\\\\\\n        return max(r / max(len(e), 1) for r, e in zip(resps, endings))\\\\\\\\n    return max(resps)\\\\\\\\n\\\\\\\\ndef load_data(benchmark):\\\\\\\\n    cfg = BENCHMARKS[benchmark]\\\\\\\\n    metric = cfg[\\\\\\\\'metric\\\\\\\\']\\\\\\\\n    data = {\\\\\\\\'pure_conf\\\\\\\\': {}, \\\\\\\\'pure_acc\\\\\\\\': {}, \\\\\\\\'hybrid_acc\\\\\\\\': {}}\\\\\\\\n    for arch in ARCHS:\\\\\\\\n        pp, hp = str(cfg[\\\\\\\\'pure\\\\\\\\'][arch]), str(cfg[\\\\\\\\'hybrid\\\\\\\\'][arch])\\\\\\\\n        if not Path(pp).exists() or not Path(hp).exists():\\\\\\\\n            return None\\\\\\\\n        ps = load_jsonl(pp)\\\\\\\\n        hs = load_jsonl(hp)\\\\\\\\n        data[\\\\\\\\'pure_conf\\\\\\\\'][arch] = np.array([get_confidence(s, metric, benchmark) for s in ps])\\\\\\\\n        data[\\\\\\\\'pure_acc\\\\\\\\'][arch]  = np.array([int(s[metric]) for s in ps])\\\\\\\\n        data[\\\\\\\\'hybrid_acc\\\\\\\\'][arch] = np.array([int(s[metric]) for s in hs])\\\\\\\\n    data[\\\\\\\\'n\\\\\\\\'] = len(load_jsonl(str(cfg[\\\\\\\\'pure\\\\\\\\'][\\\\\\\\'GDN\\\\\\\\'])))\\\\\\\\n    return data\\\\\\\\n\\\\\\\\ndef strat_rescue_threshold(data, train, test):\\\\\\\\n    conf  = np.column_stack([data[\\\\\\\\'pure_conf\\\\\\\\'][a] for a in ARCHS])\\\\\\\\n    pure  = np.column_stack([data[\\\\\\\\'pure_acc\\\\\\\\'][a]  for a in ARCHS])\\\\\\\\n    hyb   = np.column_stack([data[\\\\\\\\'hybrid_acc\\\\\\\\'][a] for a in ARCHS])\\\\\\\\n    absconf = np.abs(conf)\\\\\\\\n    tr_abs = absconf[train]\\\\\\\\n    thresholds = np.linspace(np.percentile(tr_abs, 2), np.percentile(tr_abs, 98), 100)\\\\\\\\n    best_t, best_a = thresholds[0], -1\\\\\\\\n    for t in thresholds:\\\\\\\\n        dec = np.where(tr_abs > t, hyb[train], pure[train])\\\\\\\\n        a = np.mean(np.sum(dec, axis=1) >= 2)\\\\\\\\n        if a > best_a:\\\\\\\\n            best_a, best_t = a, t\\\\\\\\n    te_abs = absconf[test]\\\\\\\\n    dec = np.where(te_abs > best_t, hyb[test], pure[test])\\\\\\\\n    return float(np.mean(np.sum(dec, axis=1) >= 2))\\\\\\\\n\\\\\\\\ndef bl_mv(data, test):\\\\\\\\n    hyb = np.column_stack([data[\\\\\\\\'hybrid_acc\\\\\\\\'][a] for a in ARCHS])\\\\\\\\n    return float(np.mean(np.sum(hyb[test], axis=1) >= 2))\\\\\\\\n\\\\\\\\nprint(\\\\\\\\'=\\\\\\\\'*80)\\\\\\\\nprint(\\\\\\\\'PAIRED T-TEST: rescue_threshold vs majority_vote (per-split)\\\\\\\\')\\\\\\\\nprint(\\\\\\\\'=\\\\\\\\'*80)\\\\\\\\n\\\\\\\\nall_results = {}\\\\\\\\n\\\\\\\\nfor bm in BENCHMARKS:\\\\\\\\n    data = load_data(bm)\\\\\\\\n    if data is None:\\\\\\\\n        print(f\\\\\\\\'{bm}: SKIPPED (missing data)\\\\\\\\')\\\\\\\\n        continue\\\\\\\\n\\\\\\\\n    n = data[\\\\\\\\'n\\\\\\\\']\\\\\\\\n    rng = np.random.default_rng(42)\\\\\\\\n    idx = np.arange(n)\\\\\\\\n    n_splits = 10\\\\\\\\n\\\\\\\\n    routing_accs = []\\\\\\\\n    mv_accs = []\\\\\\\\n\\\\\\\\n    for i in range(n_splits):\\\\\\\\n        perm = rng.permutation(idx)\\\\\\\\n        h = n // 2\\\\\\\\n        tr, te = perm[:h], perm[h:]\\\\\\\\n        routing_accs.append(strat_rescue_threshold(data, tr, te))\\\\\\\\n        mv_accs.append(bl_mv(data, te))\\\\\\\\n\\\\\\\\n    routing_accs = np.array(routing_accs)\\\\\\\\n    mv_accs = np.array(mv_accs)\\\\\\\\n    diffs = routing_accs - mv_accs\\\\\\\\n\\\\\\\\n    t_stat, p_val = stats.ttest_rel(routing_accs, mv_accs)\\\\\\\\n    se = stats.sem(diffs)\\\\\\\\n    ci = stats.t.interval(0.95, len(diffs)-1, loc=np.mean(diffs), scale=se)\\\\\\\\n\\\\\\\\n    print(f\\\\\\\\'\\\\\\\\\\\\\\\\n{bm} (n_splits={n_splits}, n_samples={n})\\\\\\\\')\\\\\\\\n    print(f\\\\\\\\'  Per-split routing:  {routing_accs}\\\\\\\\')\\\\\\\\n    print(f\\\\\\\\'  Per-split MV:       {mv_accs}\\\\\\\\')\\\\\\\\n    print(f\\\\\\\\'  Per-split diff:     {diffs}\\\\\\\\')\\\\\\\\n    print(f\\\\\\\\'  mean_diff = {np.mean(diffs):.6f} ({np.mean(diffs)*100:+.3f} pp)\\\\\\\\')\\\\\\\\n    print(f\\\\\\\\'  t = {t_stat:.4f}, p = {p_val:.6f}\\\\\\\\')\\\\\\\\n    print(f\\\\\\\\'  95% CI: [{ci[0]:.6f}, {ci[1]:.6f}] = [{ci[0]*100:.3f}, {ci[1]*100:.3f}] pp\\\\\\\\')\\\\\\\\n    sig = \\\\\\\\'YES\\\\\\\\' if p_val < 0.05 else \\\\\\\\'NO\\\\\\\\'\\\\\\\\n    print(f\\\\\\\\'  Significant (p<0.05): {sig}\\\\\\\\')\\\\\\\\n\\\\\\\\n    all_results[bm] = {\\\\\\\\n        \\\\\\\\'routing_accs\\\\\\\\': routing_accs.tolist(),\\\\\\\\n        \\\\\\\\'mv_accs\\\\\\\\': mv_accs.tolist(),\\\\\\\\n        \\\\\\\\'diffs\\\\\\\\': diffs.tolist(),\\\\\\\\n        \\\\\\\\'mean_diff\\\\\\\\': float(np.mean(diffs)),\\\\\\\\n        \\\\\\\\'mean_diff_pp\\\\\\\\': float(np.mean(diffs)*100),\\\\\\\\n        \\\\\\\\'t_stat\\\\\\\\': float(t_stat),\\\\\\\\n        \\\\\\\\'p_value\\\\\\\\': float(p_val),\\\\\\\\n        \\\\\\\\'ci_95_low\\\\\\\\': float(ci[0]),\\\\\\\\n        \\\\\\\\'ci_95_high\\\\\\\\': float(ci[1]),\\\\\\\\n        \\\\\\\\'n_splits\\\\\\\\': n_splits,\\\\\\\\n        \\\\\\\\'n_samples\\\\\\\\': n,\\\\\\\\n    }\\\\\\\\n\\\\\\\\nprint(\\\\\\\\'\\\\\\\\\\\\\\\\n\\\\\\\\' + \\\\\\\\'=\\\\\\\\'*80)\\\\\\\\nprint(\\\\\\\\'SUMMARY TABLE\\\\\\\\')\\\\\\\\nprint(\\\\\\\\'=\\\\\\\\'*80)\\\\\\\\nprint(f\\\\\\\\'{\\\\\\\\\\\\\\\\\\\\\\\"Benchmark\\\\\\\\\\\\\\\\\\\\\\\":<12} {\\\\\\\\\\\\\\\\\\\\\\\"mean_diff(pp)\\\\\\\\\\\\\\\\\\\\\\\":>14} {\\\\\\\\\\\\\\\\\\\\\\\"t\\\\\\\\\\\\\\\\\\\\\\\":>8} {\\\\\\\\\\\\\\\\\\\\\\\"p\\\\\\\\\\\\\\\\\\\\\\\":>10} {\\\\\\\\\\\\\\\\\\\\\\\"95% CI (pp)\\\\\\\\\\\\\\\\\\\\\\\":>22} {\\\\\\\\\\\\\\\\\\\\\\\"sig?\\\\\\\\\\\\\\\\\\\\\\\":>6}\\\\\\\\')\\\\\\\\nprint(\\\\\\\\'-\\\\\\\\'*75)\\\\\\\\nfor bm, r in all_results.items():\\\\\\\\n    sig = \\\\\\\\'*\\\\\\\\' if r[\\\\\\\\'p_value\\\\\\\\'] < 0.05 else \\\\\\\\'\\\\\\\\'\\\\\\\\n    if r[\\\\\\\\'p_value\\\\\\\\'] < 0.01: sig = \\\\\\\\'**\\\\\\\\'\\\\\\\\n    if r[\\\\\\\\'p_value\\\\\\\\'] < 0.001: sig = \\\\\\\\'***\\\\\\\\'\\\\\\\\n    print(f\\\\\\\\'{bm:<12} {r[\\\\\\\\\\\\\\\\\\\\\\\"mean_diff_pp\\\\\\\\\\\\\\\\\\\\\\\"]:>+13.3f} {r[\\\\\\\\\\\\\\\\\\\\\\\"t_stat\\\\\\\\\\\\\\\\\\\\\\\"]:>8.3f} {r[\\\\\\\\\\\\\\\\\\\\\\\"p_value\\\\\\\\\\\\\\\\\\\\\\\"]:>10.6f} [{r[\\\\\\\\\\\\\\\\\\\\\\\"ci_95_low\\\\\\\\\\\\\\\\\\\\\\\"]*100:>+7.3f}, {r[\\\\\\\\\\\\\\\\\\\\\\\"ci_95_high\\\\\\\\\\\\\\\\\\\\\\\"]*100:>+7.3f}] {sig:>6}\\\\\\\\')\\\\\\\\n\\\\\\\\n# Save\\\\\\\\nout_path = BASE / \\\\\\\\'results/e1_paired_ttest.json\\\\\\\\'\\\\\\\\nwith open(out_path, \\\\\\\\'w\\\\\\\\') as f:\\\\\\\\n    json.dump(all_results, f, indent=2)\\\\\\\\nprint(f\\\\\\\\'\\\\\\\\\\\\\\\\nSaved: {out_path}\\\\\\\\')\\\\\\\\n\\\\\\\"\\\\\\\\n'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nbash: line 1: python3: command not found\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/entrainment_gated_ft && python3 -c \\\"\\\\nimport json, numpy as np\\\\nfrom pathlib import Path\\\\nfrom scipy import stats\\\\n\\\\nBASE = Path(\\\\'/root/entrainment_gated_ft\\\\')\\\\nLM = BASE / \\\\'lm_eval_clean\\\\'\\\\nARCHS = [\\\\'GDN\\\\', \\\\'RetNet\\\\', \\\\'HGRN2\\\\']\\\\nFULL_NAMES = {\\\\'GDN\\\\': \\\\'GatedDeltaNet\\\\', \\\\'RetNet\\\\': \\\\'RetNet\\\\', \\\\'HGRN2\\\\': \\\\'HGRN2\\\\'}\\\\n\\\\nBENCHMARKS = {\\\\n    \\\\'lambada\\\\': {\\\\n        \\\\'metric\\\\': \\\\'acc\\\\',\\\\n        \\\\'pure\\\\': {\\\\n            \\\\'GDN\\\\':    LM / \\\\'exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\\\\',\\\\n            \\\\'RetNet\\\\': LM / \\\\'exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\\\\',\\\\n            \\\\'HGRN2\\\\':  LM / \\\\'exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\\\\',\\\\n        },\\\\n        \\\\'hybrid\\\\': {\\\\n            \\\\'GDN\\\\':    LM / \\\\'1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\\\\',\\\\n            \\\\'RetNet\\\\': LM / \\\\'exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\\\\',\\\\n            \\\\'HGRN2\\\\':  LM / \\\\'exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\\\\',\\\\n        },\\\\n    },\\\\n    \\\\'hellaswag\\\\': {\\\\n        \\\\'metric\\\\': \\\\'acc_norm\\\\',\\\\n        \\\\'pure\\\\':   {a: LM / f\\\\'hellaswag/1.3B-100B-{FULL_NAMES[a]}-pure/samples/hellaswag.jsonl\\\\' for a in ARCHS},\\\\n        \\\\'hybrid\\\\': {a: LM / f\\\\'hellaswag/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/hellaswag.jsonl\\\\' for a in ARCHS},\\\\n    },\\\\n    \\\\'piqa\\\\': {\\\\n        \\\\'metric\\\\': \\\\'acc\\\\',\\\\n        \\\\'pure\\\\':   {a: LM / f\\\\'piqa/1.3B-100B-{FULL_NAMES[a]}-pure/samples/piqa.jsonl\\\\' for a in ARCHS},\\\\n        \\\\'hybrid\\\\': {a: LM / f\\\\'piqa/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/piqa.jsonl\\\\' for a in ARCHS},\\\\n    },\\\\n    \\\\'arc_easy\\\\': {\\\\n        \\\\'metric\\\\': \\\\'acc\\\\',\\\\n        \\\\'pure\\\\':   {a: LM / f\\\\'arc_easy/1.3B-100B-{FULL_NAMES[a]}-pure/samples/arc_easy.jsonl\\\\' for a in ARCHS},\\\\n        \\\\'hybrid\\\\': {a: LM / f\\\\'arc_easy/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/arc_easy.jsonl\\\\' for a in ARCHS},\\\\n    },\\\\n}\\\\n\\\\ndef load_jsonl(path):\\\\n    with open(path) as f:\\\\n        data = [json.loads(line) for line in f]\\\\n    data.sort(key=lambda x: x[\\\\'doc_id\\\\'])\\\\n    return data\\\\n\\\\ndef get_confidence(sample, metric, benchmark):\\\\n    if benchmark == \\\\'lambada\\\\':\\\\n        return sample[\\\\'resps\\\\'][0][0][0]\\\\n    resps = [r[0][0] for r in sample[\\\\'resps\\\\']]\\\\n    if metric == \\\\'acc_norm\\\\':\\\\n        endings = sample[\\\\'doc\\\\'][\\\\'endings\\\\']\\\\n        return max(r / max(len(e), 1) for r, e in zip(resps, endings))\\\\n    return max(resps)\\\\n\\\\ndef load_data(benchmark):\\\\n    cfg = BENCHMARKS[benchmark]\\\\n    metric = cfg[\\\\'metric\\\\']\\\\n    data = {\\\\'pure_conf\\\\': {}, \\\\'pure_acc\\\\': {}, \\\\'hybrid_acc\\\\': {}}\\\\n    for arch in ARCHS:\\\\n        pp, hp = str(cfg[\\\\'pure\\\\'][arch]), str(cfg[\\\\'hybrid\\\\'][arch])\\\\n        if not Path(pp).exists() or not Path(hp).exists():\\\\n            return None\\\\n        ps = load_jsonl(pp)\\\\n        hs = load_jsonl(hp)\\\\n        data[\\\\'pure_conf\\\\'][arch] = np.array([get_confidence(s, metric, benchmark) for s in ps])\\\\n        data[\\\\'pure_acc\\\\'][arch]  = np.array([int(s[metric]) for s in ps])\\\\n        data[\\\\'hybrid_acc\\\\'][arch] = np.array([int(s[metric]) for s in hs])\\\\n    data[\\\\'n\\\\'] = len(load_jsonl(str(cfg[\\\\'pure\\\\'][\\\\'GDN\\\\'])))\\\\n    return data\\\\n\\\\ndef strat_rescue_threshold(data, train, test):\\\\n    conf  = np.column_stack([data[\\\\'pure_conf\\\\'][a] for a in ARCHS])\\\\n    pure  = np.column_stack([data[\\\\'pure_acc\\\\'][a]  for a in ARCHS])\\\\n    hyb   = np.column_stack([data[\\\\'hybrid_acc\\\\'][a] for a in ARCHS])\\\\n    absconf = np.abs(conf)\\\\n    tr_abs = absconf[train]\\\\n    thresholds = np.linspace(np.percentile(tr_abs, 2), np.percentile(tr_abs, 98), 100)\\\\n    best_t, best_a = thresholds[0], -1\\\\n    for t in thresholds:\\\\n        dec = np.where(tr_abs > t, hyb[train], pure[train])\\\\n        a = np.mean(np.sum(dec, axis=1) >= 2)\\\\n        if a > best_a:\\\\n            best_a, best_t = a, t\\\\n    te_abs = absconf[test]\\\\n    dec = np.where(te_abs > best_t, hyb[test], pure[test])\\\\n    return float(np.mean(np.sum(dec, axis=1) >= 2))\\\\n\\\\ndef bl_mv(data, test):\\\\n    hyb = np.column_stack([data[\\\\'hybrid_acc\\\\'][a] for a in ARCHS])\\\\n    return float(np.mean(np.sum(hyb[test], axis=1) >= 2))\\\\n\\\\nprint(\\\\'=\\\\'*80)\\\\nprint(\\\\'PAIRED T-TEST: rescue_threshold vs majority_vote (per-split)\\\\')\\\\nprint(\\\\'=\\\\'*80)\\\\n\\\\nall_results = {}\\\\n\\\\nfor bm in BENCHMARKS:\\\\n    data = load_data(bm)\\\\n    if data is None:\\\\n        print(f\\\\'{bm}: SKIPPED (missing data)\\\\')\\\\n        continue\\\\n\\\\n    n = data[\\\\'n\\\\']\\\\n    rng = np.random.default_rng(42)\\\\n    idx = np.arange(n)\\\\n    n_splits = 10\\\\n\\\\n    routing_accs = []\\\\n    mv_accs = []\\\\n\\\\n    for i in range(n_splits):\\\\n        perm = rng.permutation(idx)\\\\n        h = n // 2\\\\n        tr, te = perm[:h], perm[h:]\\\\n        routing_accs.append(strat_rescue_threshold(data, tr, te))\\\\n        mv_accs.append(bl_mv(data, te))\\\\n\\\\n    routing_accs = np.array(routing_accs)\\\\n    mv_accs = np.array(mv_accs)\\\\n    diffs = routing_accs - mv_accs\\\\n\\\\n    t_stat, p_val = stats.ttest_rel(routing_accs, mv_accs)\\\\n    se = stats.sem(diffs)\\\\n    ci = stats.t.interval(0.95, len(diffs)-1, loc=np.mean(diffs), scale=se)\\\\n\\\\n    print(f\\\\'\\\\\\\\n{bm} (n_splits={n_splits}, n_samples={n})\\\\')\\\\n    print(f\\\\'  Per-split routing:  {routing_accs}\\\\')\\\\n    print(f\\\\'  Per-split MV:       {mv_accs}\\\\')\\\\n    print(f\\\\'  Per-split diff:     {diffs}\\\\')\\\\n    print(f\\\\'  mean_diff = {np.mean(diffs):.6f} ({np.mean(diffs)*100:+.3f} pp)\\\\')\\\\n    print(f\\\\'  t = {t_stat:.4f}, p = {p_val:.6f}\\\\')\\\\n    print(f\\\\'  95% CI: [{ci[0]:.6f}, {ci[1]:.6f}] = [{ci[0]*100:.3f}, {ci[1]*100:.3f}] pp\\\\')\\\\n    sig = \\\\'YES\\\\' if p_val < 0.05 else \\\\'NO\\\\'\\\\n    print(f\\\\'  Significant (p<0.05): {sig}\\\\')\\\\n\\\\n    all_results[bm] = {\\\\n        \\\\'routing_accs\\\\': routing_accs.tolist(),\\\\n        \\\\'mv_accs\\\\': mv_accs.tolist(),\\\\n        \\\\'diffs\\\\': diffs.tolist(),\\\\n        \\\\'mean_diff\\\\': float(np.mean(diffs)),\\\\n        \\\\'mean_diff_pp\\\\': float(np.mean(diffs)*100),\\\\n        \\\\'t_stat\\\\': float(t_stat),\\\\n        \\\\'p_value\\\\': float(p_val),\\\\n        \\\\'ci_95_low\\\\': float(ci[0]),\\\\n        \\\\'ci_95_high\\\\': float(ci[1]),\\\\n        \\\\'n_splits\\\\': n_splits,\\\\n        \\\\'n_samples\\\\': n,\\\\n    }\\\\n\\\\nprint(\\\\'\\\\\\\\n\\\\' + \\\\'=\\\\'*80)\\\\nprint(\\\\'SUMMARY TABLE\\\\')\\\\nprint(\\\\'=\\\\'*80)\\\\nprint(f\\\\'{\\\\\\\\\\\"Benchmark\\\\\\\\\\\":<12} {\\\\\\\\\\\"mean_diff(pp)\\\\\\\\\\\":>14} {\\\\\\\\\\\"t\\\\\\\\\\\":>8} {\\\\\\\\\\\"p\\\\\\\\\\\":>10} {\\\\\\\\\\\"95% CI (pp)\\\\\\\\\\\":>22} {\\\\\\\\\\\"sig?\\\\\\\\\\\":>6}\\\\')\\\\nprint(\\\\'-\\\\'*75)\\\\nfor bm, r in all_results.items():\\\\n    sig = \\\\'*\\\\' if r[\\\\'p_value\\\\'] < 0.05 else \\\\'\\\\'\\\\n    if r[\\\\'p_value\\\\'] < 0.01: sig = \\\\'**\\\\'\\\\n    if r[\\\\'p_value\\\\'] < 0.001: sig = \\\\'***\\\\'\\\\n    print(f\\\\'{bm:<12} {r[\\\\\\\\\\\"mean_diff_pp\\\\\\\\\\\"]:>+13.3f} {r[\\\\\\\\\\\"t_stat\\\\\\\\\\\"]:>8.3f} {r[\\\\\\\\\\\"p_value\\\\\\\\\\\"]:>10.6f} [{r[\\\\\\\\\\\"ci_95_low\\\\\\\\\\\"]*100:>+7.3f}, {r[\\\\\\\\\\\"ci_95_high\\\\\\\\\\\"]*100:>+7.3f}] {sig:>6}\\\\')\\\\n\\\\n# Save\\\\nout_path = BASE / \\\\'results/e1_paired_ttest.json\\\\'\\\\nwith open(out_path, \\\\'w\\\\') as f:\\\\n    json.dump(all_results, f, indent=2)\\\\nprint(f\\\\'\\\\\\\\nSaved: {out_path}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.42}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Python3 not found - this might be a conda environment. Let me check the environment setup.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "75cf2681-9f11-4544-b390-06b6d44c6a39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9n3fmsyQSJqLMQPTjkbcT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6586,
      "cache_read_input_tokens": 42960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6586
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

_source line 38_

Conda 环境需要激活。让我先写脚本文件再执行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "466aeb47-a3d7-46ce-8e4b-4bfbedb782bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9n3fmsyQSJqLMQPTjkbcT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6586,
      "cache_read_input_tokens": 42960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6586
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

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BYoH9rQk9JMmz4C7bReufR`</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/miniconda3/bin/python3",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "1caf325f-13f7-4fac-b502-7d1cd011b3c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9n3fmsyQSJqLMQPTjkbcT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6586,
      "cache_read_input_tokens": 42960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6586
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

_source line 40 · 2026-05-23T17:07:40.575Z_

<details><summary>↩ Tool result · `toolu_01BYoH9rQk9JMmz4C7bReufR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.91}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "3cdde003-af85-4431-9416-d2ede8136a64",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/miniconda3/bin/python3\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.91}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.91}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_019rZg36m9jpk62GghDkdtEg`</summary>

```json
{
  "server": "westb-48145",
  "command": "cat > /tmp/paired_ttest.py << 'PYEOF'\nimport json, numpy as np\nfrom pathlib import Path\nfrom scipy import stats\n\nBASE = Path('/root/entrainment_gated_ft')\nLM = BASE / 'lm_eval_clean'\nARCHS = ['GDN', 'RetNet', 'HGRN2']\nFULL_NAMES = {'GDN': 'GatedDeltaNet', 'RetNet': 'RetNet', 'HGRN2': 'HGRN2'}\n\nBENCHMARKS = {\n    'lambada': {\n        'metric': 'acc',\n        'pure': {\n            'GDN':    LM / 'exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl',\n            'RetNet': LM / 'exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl',\n            'HGRN2':  LM / 'exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl',\n        },\n        'hybrid': {\n            'GDN':    LM / '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl',\n            'RetNet': LM / 'exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl',\n            'HGRN2':  LM / 'exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl',\n        },\n    },\n    'hellaswag': {\n        'metric': 'acc_norm',\n        'pure':   {a: LM / f'hellaswag/1.3B-100B-{FULL_NAMES[a]}-pure/samples/hellaswag.jsonl' for a in ARCHS},\n        'hybrid': {a: LM / f'hellaswag/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/hellaswag.jsonl' for a in ARCHS},\n    },\n    'piqa': {\n        'metric': 'acc',\n        'pure':   {a: LM / f'piqa/1.3B-100B-{FULL_NAMES[a]}-pure/samples/piqa.jsonl' for a in ARCHS},\n        'hybrid': {a: LM / f'piqa/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/piqa.jsonl' for a in ARCHS},\n    },\n    'arc_easy': {\n        'metric': 'acc',\n        'pure':   {a: LM / f'arc_easy/1.3B-100B-{FULL_NAMES[a]}-pure/samples/arc_easy.jsonl' for a in ARCHS},\n        'hybrid': {a: LM / f'arc_easy/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/arc_easy.jsonl' for a in ARCHS},\n    },\n}\n\ndef load_jsonl(path):\n    with open(path) as f:\n        data = [json.loads(line) for line in f]\n    data.sort(key=lambda x: x['doc_id'])\n    return data\n\ndef get_confidence(sample, metric, benchmark):\n    if benchmark == 'lambada':\n        return sample['resps'][0][0][0]\n    resps = [r[0][0] for r in sample['resps']]\n    if metric == 'acc_norm':\n        endings = sample['doc']['endings']\n        return max(r / max(len(e), 1) for r, e in zip(resps, endings))\n    return max(resps)\n\ndef load_data(benchmark):\n    cfg = BENCHMARKS[benchmark]\n    metric = cfg['metric']\n    data = {'pure_conf': {}, 'pure_acc': {}, 'hybrid_acc': {}}\n    for arch in ARCHS:\n        pp, hp = str(cfg['pure'][arch]), str(cfg['hybrid'][arch])\n        if not Path(pp).exists() or not Path(hp).exists():\n            print(f\"  MISSING: {pp} or {hp}\")\n            return None\n        ps = load_jsonl(pp)\n        hs = load_jsonl(hp)\n        data['pure_conf'][arch] = np.array([get_confidence(s, metric, benchmark) for s in ps])\n        data['pure_acc'][arch]  = np.array([int(s[metric]) for s in ps])\n        data['hybrid_acc'][arch] = np.array([int(s[metric]) for s in hs])\n    data['n'] = len(load_jsonl(str(cfg['pure']['GDN'])))\n    return data\n\ndef strat_rescue_threshold(data, train, test):\n    conf  = np.column_stack([data['pure_conf'][a] for a in ARCHS])\n    pure  = np.column_stack([data['pure_acc'][a]  for a in ARCHS])\n    hyb   = np.column_stack([data['hybrid_acc'][a] for a in ARCHS])\n    absconf = np.abs(conf)\n    tr_abs = absconf[train]\n    thresholds = np.linspace(np.percentile(tr_abs, 2), np.percentile(tr_abs, 98), 100)\n    best_t, best_a = thresholds[0], -1\n    for t in thresholds:\n        dec = np.where(tr_abs > t, hyb[train], pure[train])\n        a = np.mean(np.sum(dec, axis=1) >= 2)\n        if a > best_a:\n            best_a, best_t = a, t\n    te_abs = absconf[test]\n    dec = np.where(te_abs > best_t, hyb[test], pure[test])\n    return float(np.mean(np.sum(dec, axis=1) >= 2))\n\ndef bl_mv(data, test):\n    hyb = np.column_stack([data['hybrid_acc'][a] for a in ARCHS])\n    return float(np.mean(np.sum(hyb[test], axis=1) >= 2))\n\nprint('='*80)\nprint('PAIRED T-TEST: rescue_threshold vs majority_vote (per-split)')\nprint('='*80)\n\nall_results = {}\n\nfor bm in BENCHMARKS:\n    data = load_data(bm)\n    if data is None:\n        print(f'{bm}: SKIPPED (missing data)')\n        continue\n\n    n = data['n']\n    rng = np.random.default_rng(42)\n    idx = np.arange(n)\n    n_splits = 10\n\n    routing_accs = []\n    mv_accs = []\n\n    for i in range(n_splits):\n        perm = rng.permutation(idx)\n        h = n // 2\n        tr, te = perm[:h], perm[h:]\n        routing_accs.append(strat_rescue_threshold(data, tr, te))\n        mv_accs.append(bl_mv(data, te))\n\n    routing_accs = np.array(routing_accs)\n    mv_accs = np.array(mv_accs)\n    diffs = routing_accs - mv_accs\n\n    t_stat, p_val = stats.ttest_rel(routing_accs, mv_accs)\n    se = stats.sem(diffs)\n    ci = stats.t.interval(0.95, len(diffs)-1, loc=np.mean(diffs), scale=se)\n\n    print(f'\\n{bm} (n_splits={n_splits}, n_samples={n})')\n    print(f'  Per-split routing:  {np.round(routing_accs, 6)}')\n    print(f'  Per-split MV:       {np.round(mv_accs, 6)}')\n    print(f'  Per-split diff:     {np.round(diffs, 6)}')\n    print(f'  mean_diff = {np.mean(diffs):.6f} ({np.mean(diffs)*100:+.3f} pp)')\n    print(f'  t = {t_stat:.4f}, p = {p_val:.6f}')\n    print(f'  95% CI: [{ci[0]:.6f}, {ci[1]:.6f}] = [{ci[0]*100:.3f}, {ci[1]*100:.3f}] pp')\n    sig = 'YES' if p_val < 0.05 else 'NO'\n    print(f'  Significant (p<0.05): {sig}')\n\n    all_results[bm] = {\n        'routing_accs': routing_accs.tolist(),\n        'mv_accs': mv_accs.tolist(),\n        'diffs': diffs.tolist(),\n        'mean_diff': float(np.mean(diffs)),\n        'mean_diff_pp': float(np.mean(diffs)*100),\n        't_stat': float(t_stat),\n        'p_value': float(p_val),\n        'ci_95_low': float(ci[0]),\n        'ci_95_high': float(ci[1]),\n        'n_splits': n_splits,\n        'n_samples': n,\n    }\n\nprint('\\n' + '='*80)\nprint('SUMMARY TABLE')\nprint('='*80)\nhdr = f'{\"Benchmark\":<12} {\"mean_diff(pp)\":>14} {\"t\":>8} {\"p\":>10} {\"95% CI (pp)\":>22} {\"sig?\":>6}'\nprint(hdr)\nprint('-'*75)\nfor bm, r in all_results.items():\n    sig = '' \n    if r['p_value'] < 0.05: sig = '*'\n    if r['p_value'] < 0.01: sig = '**'\n    if r['p_value'] < 0.001: sig = '***'\n    print(f'{bm:<12} {r[\"mean_diff_pp\"]:>+13.3f} {r[\"t_stat\"]:>8.3f} {r[\"p_value\"]:>10.6f} [{r[\"ci_95_low\"]*100:>+7.3f}, {r[\"ci_95_high\"]*100:>+7.3f}] {sig:>6}')\n\nout_path = BASE / 'results/e1_paired_ttest.json'\nwith open(out_path, 'w') as f:\n    json.dump(all_results, f, indent=2)\nprint(f'\\nSaved: {out_path}')\nPYEOF\n",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "7bff8247-b710-410b-83fc-c7d50601d68a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EEQVRSnKvqP38BjEkxuFYk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 260,
      "cache_read_input_tokens": 49546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 260
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

_source line 42 · 2026-05-23T17:08:19.629Z_

<details><summary>↩ Tool result · `toolu_019rZg36m9jpk62GghDkdtEg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.73}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "443f26bc-66ce-4c43-9519-e9fa907ef716",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.73}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.73}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01322PqWzs7uyPy8kqKiyqVx`</summary>

```json
{
  "server": "westb-48145",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/paired_ttest.py",
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
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "557b67a5-f359-496b-9be6-0c02d85f50f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W71Z7NGJRZRPkFqCECKeN2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 49806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2923
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

_source line 44 · 2026-05-23T17:08:28.735Z_

<details><summary>↩ Tool result · `toolu_01322PqWzs7uyPy8kqKiyqVx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"================================================================================\\nPAIRED T-TEST: rescue_threshold vs majority_vote (per-split)\\n================================================================================\\n\\nlambada (n_splits=10, n_samples=5153)\\n  Per-split routing:  [0.557625 0.56655  0.572371 0.563058 0.56655  0.561894 0.569267 0.56461\\n 0.567326 0.558401]\\n  Per-split MV:       [0.50097  0.510671 0.51688  0.515716 0.509895 0.510671 0.522701 0.512224\\n 0.520761 0.511835]\\n  Per-split diff:     [0.056655 0.055879 0.055491 0.047342 0.056655 0.051222 0.046566 0.052386\\n 0.046566 0.046566]\\n  mean_diff = 0.051533 (+5.153 pp)\\n  t = 36.4967, p = 0.000000\\n  95% CI: [0.048339, 0.054727] = [4.834, 5.473] pp\\n  Significant (p<0.05): YES\\n\\nhellaswag (n_splits=10, n_samples=10042)\\n  Per-split routing:  [0.60227  0.606254 0.590918 0.598885 0.601872 0.601673 0.592312 0.594503\\n 0.598686 0.589325]\\n  Per-split MV:       [0.60705  0.603864 0.590321 0.599084 0.60227  0.604461 0.591914 0.593109\\n 0.599084 0.591914]\\n  Per-split diff:     [-0.00478   0.00239   0.000597 -0.000199 -0.000398 -0.002788  0.000398\\n  0.001394 -0.000398 -0.002589]\\n  mean_diff = -0.000637 (-0.064 pp)\\n  t = -0.9353, p = 0.374067\\n  95% CI: [-0.002179, 0.000904] = [-0.218, 0.090] pp\\n  Significant (p<0.05): NO\\n\\npiqa (n_splits=10, n_samples=1838)\\n  Per-split routing:  [0.73123  0.742111 0.73123  0.733406 0.726877 0.729053 0.715996 0.708379\\n 0.751904 0.732318]\\n  Per-split MV:       [0.737758 0.750816 0.733406 0.739935 0.727965 0.738847 0.715996 0.708379\\n 0.754081 0.744287]\\n  Per-split diff:     [-0.006529 -0.008705 -0.002176 -0.006529 -0.001088 -0.009793  0.\\n  0.       -0.002176 -0.01197 ]\\n  mean_diff = -0.004897 (-0.490 pp)\\n  t = -3.5514, p = 0.006202\\n  95% CI: [-0.008016, -0.001778] = [-0.802, -0.178] pp\\n  Significant (p<0.05): YES\\n\\narc_easy (n_splits=10, n_samples=2376)\\n  Per-split routing:  [0.72138  0.728956 0.742424 0.709596 0.732323 0.723064 0.734007 0.717172\\n 0.718013 0.739899]\\n  Per-split MV:       [0.709596 0.723906 0.728114 0.700337 0.724747 0.709596 0.725589 0.710438\\n 0.701178 0.718013]\\n  Per-split diff:     [0.011785 0.005051 0.01431  0.009259 0.007576 0.013468 0.008418 0.006734\\n 0.016835 0.021886]\\n  mean_diff = 0.011532 (+1.153 pp)\\n  t = 7.0269, p = 0.000061\\n  95% CI: [0.007820, 0.015244] = [0.782, 1.524] pp\\n  Significant (p<0.05): YES\\n\\n================================================================================\\nSUMMARY TABLE\\n================================================================================\\nBenchmark     mean_diff(pp)        t          p            95% CI (pp)   sig?\\n---------------------------------------------------------------------------\\nlambada             +5.153   36.497   0.000000 [ +4.834,  +5.473]    ***\\nhellaswag           -0.064   -0.935   0.374067 [ -0.218,  +0.090]       \\npiqa                -0.490   -3.551   0.006202 [ -0.802,  -0.178]     **\\narc_easy            +1.153    7.027   0.000061 [ +0.782,  +1.524]    ***\\n\\nSaved: /root/entrainment_gated_ft/results/e1_paired_ttest.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "2b96cbe4-2988-43a7-aeb9-c9a472b56630",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"================================================================================\\\\nPAIRED T-TEST: rescue_threshold vs majority_vote (per-split)\\\\n================================================================================\\\\n\\\\nlambada (n_splits=10, n_samples=5153)\\\\n  Per-split routing:  [0.557625 0.56655  0.572371 0.563058 0.56655  0.561894 0.569267 0.56461\\\\n 0.567326 0.558401]\\\\n  Per-split MV:       [0.50097  0.510671 0.51688  0.515716 0.509895 0.510671 0.522701 0.512224\\\\n 0.520761 0.511835]\\\\n  Per-split diff:     [0.056655 0.055879 0.055491 0.047342 0.056655 0.051222 0.046566 0.052386\\\\n 0.046566 0.046566]\\\\n  mean_diff = 0.051533 (+5.153 pp)\\\\n  t = 36.4967, p = 0.000000\\\\n  95% CI: [0.048339, 0.054727] = [4.834, 5.473] pp\\\\n  Significant (p<0.05): YES\\\\n\\\\nhellaswag (n_splits=10, n_samples=10042)\\\\n  Per-split routing:  [0.60227  0.606254 0.590918 0.598885 0.601872 0.601673 0.592312 0.594503\\\\n 0.598686 0.589325]\\\\n  Per-split MV:       [0.60705  0.603864 0.590321 0.599084 0.60227  0.604461 0.591914 0.593109\\\\n 0.599084 0.591914]\\\\n  Per-split diff:     [-0.00478   0.00239   0.000597 -0.000199 -0.000398 -0.002788  0.000398\\\\n  0.001394 -0.000398 -0.002589]\\\\n  mean_diff = -0.000637 (-0.064 pp)\\\\n  t = -0.9353, p = 0.374067\\\\n  95% CI: [-0.002179, 0.000904] = [-0.218, 0.090] pp\\\\n  Significant (p<0.05): NO\\\\n\\\\npiqa (n_splits=10, n_samples=1838)\\\\n  Per-split routing:  [0.73123  0.742111 0.73123  0.733406 0.726877 0.729053 0.715996 0.708379\\\\n 0.751904 0.732318]\\\\n  Per-split MV:       [0.737758 0.750816 0.733406 0.739935 0.727965 0.738847 0.715996 0.708379\\\\n 0.754081 0.744287]\\\\n  Per-split diff:     [-0.006529 -0.008705 -0.002176 -0.006529 -0.001088 -0.009793  0.\\\\n  0.       -0.002176 -0.01197 ]\\\\n  mean_diff = -0.004897 (-0.490 pp)\\\\n  t = -3.5514, p = 0.006202\\\\n  95% CI: [-0.008016, -0.001778] = [-0.802, -0.178] pp\\\\n  Significant (p<0.05): YES\\\\n\\\\narc_easy (n_splits=10, n_samples=2376)\\\\n  Per-split routing:  [0.72138  0.728956 0.742424 0.709596 0.732323 0.723064 0.734007 0.717172\\\\n 0.718013 0.739899]\\\\n  Per-split MV:       [0.709596 0.723906 0.728114 0.700337 0.724747 0.709596 0.725589 0.710438\\\\n 0.701178 0.718013]\\\\n  Per-split diff:     [0.011785 0.005051 0.01431  0.009259 0.007576 0.013468 0.008418 0.006734\\\\n 0.016835 0.021886]\\\\n  mean_diff = 0.011532 (+1.153 pp)\\\\n  t = 7.0269, p = 0.000061\\\\n  95% CI: [0.007820, 0.015244] = [0.782, 1.524] pp\\\\n  Significant (p<0.05): YES\\\\n\\\\n================================================================================\\\\nSUMMARY TABLE\\\\n================================================================================\\\\nBenchmark     mean_diff(pp)        t          p            95% CI (pp)   sig?\\\\n---------------------------------------------------------------------------\\\\nlambada             +5.153   36.497   0.000000 [ +4.834,  +5.473]    ***\\\\nhellaswag           -0.064   -0.935   0.374067 [ -0.218,  +0.090]       \\\\npiqa                -0.490   -3.551   0.006202 [ -0.802,  -0.178]     **\\\\narc_easy            +1.153    7.027   0.000061 [ +0.782,  +1.524]    ***\\\\n\\\\nSaved: /root/entrainment_gated_ft/results/e1_paired_ttest.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"================================================================================\\nPAIRED T-TEST: rescue_threshold vs majority_vote (per-split)\\n================================================================================\\n\\nlambada (n_splits=10, n_samples=5153)\\n  Per-split routing:  [0.557625 0.56655  0.572371 0.563058 0.56655  0.561894 0.569267 0.56461\\n 0.567326 0.558401]\\n  Per-split MV:       [0.50097  0.510671 0.51688  0.515716 0.509895 0.510671 0.522701 0.512224\\n 0.520761 0.511835]\\n  Per-split diff:     [0.056655 0.055879 0.055491 0.047342 0.056655 0.051222 0.046566 0.052386\\n 0.046566 0.046566]\\n  mean_diff = 0.051533 (+5.153 pp)\\n  t = 36.4967, p = 0.000000\\n  95% CI: [0.048339, 0.054727] = [4.834, 5.473] pp\\n  Significant (p<0.05): YES\\n\\nhellaswag (n_splits=10, n_samples=10042)\\n  Per-split routing:  [0.60227  0.606254 0.590918 0.598885 0.601872 0.601673 0.592312 0.594503\\n 0.598686 0.589325]\\n  Per-split MV:       [0.60705  0.603864 0.590321 0.599084 0.60227  0.604461 0.591914 0.593109\\n 0.599084 0.591914]\\n  Per-split diff:     [-0.00478   0.00239   0.000597 -0.000199 -0.000398 -0.002788  0.000398\\n  0.001394 -0.000398 -0.002589]\\n  mean_diff = -0.000637 (-0.064 pp)\\n  t = -0.9353, p = 0.374067\\n  95% CI: [-0.002179, 0.000904] = [-0.218, 0.090] pp\\n  Significant (p<0.05): NO\\n\\npiqa (n_splits=10, n_samples=1838)\\n  Per-split routing:  [0.73123  0.742111 0.73123  0.733406 0.726877 0.729053 0.715996 0.708379\\n 0.751904 0.732318]\\n  Per-split MV:       [0.737758 0.750816 0.733406 0.739935 0.727965 0.738847 0.715996 0.708379\\n 0.754081 0.744287]\\n  Per-split diff:     [-0.006529 -0.008705 -0.002176 -0.006529 -0.001088 -0.009793  0.\\n  0.       -0.002176 -0.01197 ]\\n  mean_diff = -0.004897 (-0.490 pp)\\n  t = -3.5514, p = 0.006202\\n  95% CI: [-0.008016, -0.001778] = [-0.802, -0.178] pp\\n  Significant (p<0.05): YES\\n\\narc_easy (n_splits=10, n_samples=2376)\\n  Per-split routing:  [0.72138  0.728956 0.742424 0.709596 0.732323 0.723064 0.734007 0.717172\\n 0.718013 0.739899]\\n  Per-split MV:       [0.709596 0.723906 0.728114 0.700337 0.724747 0.709596 0.725589 0.710438\\n 0.701178 0.718013]\\n  Per-split diff:     [0.011785 0.005051 0.01431  0.009259 0.007576 0.013468 0.008418 0.006734\\n 0.016835 0.021886]\\n  mean_diff = 0.011532 (+1.153 pp)\\n  t = 7.0269, p = 0.000061\\n  95% CI: [0.007820, 0.015244] = [0.782, 1.524] pp\\n  Significant (p<0.05): YES\\n\\n================================================================================\\nSUMMARY TABLE\\n================================================================================\\nBenchmark     mean_diff(pp)        t          p            95% CI (pp)   sig?\\n---------------------------------------------------------------------------\\nlambada             +5.153   36.497   0.000000 [ +4.834,  +5.473]    ***\\nhellaswag           -0.064   -0.935   0.374067 [ -0.218,  +0.090]       \\npiqa                -0.490   -3.551   0.006202 [ -0.802,  -0.178]     **\\narc_easy            +1.153    7.027   0.000061 [ +0.782,  +1.524]    ***\\n\\nSaved: /root/entrainment_gated_ft/results/e1_paired_ttest.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.31}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 45_

Per-split 数据可用，paired t-test 完成。结果保存至 `/root/entrainment_gated_ft/results/e1_paired_ttest.json`。

## Paired t-test 结果（rescue_threshold routing vs majority vote, 10 splits）

| Benchmark | mean diff (pp) | t | p | 95% CI (pp) | sig |
|-----------|------:|------:|------:|------|:---:|
| **LAMBADA** | **+5.153** | 36.497 | <0.000001 | [+4.834, +5.473] | *** |
| HellaSwag | -0.064 | -0.935 | 0.374 | [-0.218, +0.090] | |
| PIQA | **-0.490** | -3.551 | 0.006 | [-0.802, -0.178] | ** |
| **ARC-Easy** | **+1.153** | 7.027 | 0.000061 | [+0.782, +1.524] | *** |

要点：
- **LAMBADA**：routing 显著优于 MV（+5.15pp, p<10⁻⁶），CI 极窄
- **ARC-Easy**：routing 显著优于 MV（+1.15pp, p=6×10⁻⁵）
- **HellaSwag**：无显著差异（p=0.37），routing 和 MV 基本持平
- **PIQA**：routing 显著**劣于** MV（-0.49pp, p=0.006），方向相反

和之前 unpaired Welch t-test 方向一致，但 paired 检验 power 更高——PIQA 的负向差异现在达到 p<0.01 显著水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "uuid": "772fbf30-a6f0-4146-af66-15bd77ac0221",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPTPcGAmzf8ki2VX82cBLX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1622,
      "cache_read_input_tokens": 52729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1622
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

_source line 46_

Per-split 数据可用，paired t-test 完成。结果保存至 `/root/entrainment_gated_ft/results/e1_paired_ttest.json`。

## Paired t-test 结果（rescue_threshold routing vs majority vote, 10 splits）

| Benchmark | mean diff (pp) | t | p | 95% CI (pp) | sig |
|-----------|------:|------:|------:|------|:---:|
| **LAMBADA** | **+5.153** | 36.497 | <0.000001 | [+4.834, +5.473] | *** |
| HellaSwag | -0.064 | -0.935 | 0.374 | [-0.218, +0.090] | |
| PIQA | **-0.490** | -3.551 | 0.006 | [-0.802, -0.178] | ** |
| **ARC-Easy** | **+1.153** | 7.027 | 0.000061 | [+0.782, +1.524] | *** |

要点：
- **LAMBADA**：routing 显著优于 MV（+5.15pp, p<10⁻⁶），CI 极窄
- **ARC-Easy**：routing 显著优于 MV（+1.15pp, p=6×10⁻⁵）
- **HellaSwag**：无显著差异（p=0.37），routing 和 MV 基本持平
- **PIQA**：routing 显著**劣于** MV（-0.49pp, p=0.006），方向相反

和之前 unpaired Welch t-test 方向一致，但 paired 检验 power 更高——PIQA 的负向差异现在达到 p<0.01 显著水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 172356,
  "duration_api_ms": 148649,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "3a23b384-a0e3-46e0-a75c-4b162c774424",
  "total_cost_usd": 0.695529,
  "usage": {
    "input_tokens": 18,
    "cache_creation_input_tokens": 42510,
    "cache_read_input_tokens": 435193,
    "output_tokens": 8421,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 42510,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 483,
        "cache_read_input_tokens": 52729,
        "cache_creation_input_tokens": 1622,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1622
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1530,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00163,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 18,
      "outputTokens": 8421,
      "cacheReadInputTokens": 435193,
      "cacheCreationInputTokens": 42510,
      "webSearchRequests": 0,
      "costUSD": 0.6938989999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7c27fc09-cc3e-4854-a135-d35c7a1d989b"
}
```

</details>

---
