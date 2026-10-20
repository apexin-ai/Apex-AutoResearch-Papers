# fix mlp correlation extend

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 68
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/workers/worker_fix_mlp-correlation-extend_20260514T052804.log`
- **Structured JSON:** [`ca9c2d6b52d2ee8e2b06.json`](../../sessions/ca/ca9c2d6b52d2ee8e2b06.json)

## Before a recorded user message

68 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
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
  "uuid": "be1c2b93-1096-4846-a1d3-55c64011d29c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1778744400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d16d7114-fdd6-452b-ba32-610fc009c5ac",
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down this task:

1. First, I need to wait for files to stabilize (another worker is modifying them)
2. Then check/modify cka_overlap.py for MLP pairwise CKA matrix
3. Extend correlation_analysis.py with MLP-level recoverability analysis
4. Confirm pruning_mask format in prune.py
5. Verify with --help

Let me start by checking file stability on the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "1501307e-f0d7-41b7-9ffd-9a4a4ec6cbb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbCid2m7PDunqdRsdRcCML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13281,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13281
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

### Assistant

_source line 5_

先检查文件稳定性，确认另一个 Worker 是否还在修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "3f25fefd-9f23-4185-9cb1-71fa80111c5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbCid2m7PDunqdRsdRcCML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13281,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13281
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

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LwrkgF27mvFastsXpKd4WN`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "d91a5fa9-206d-4715-80b8-76d35eb66f79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbCid2m7PDunqdRsdRcCML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13281,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13281
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

_source line 7 · 2026-05-14T05:28:17.572Z_

<details><summary>↩ Tool result · `toolu_01LwrkgF27mvFastsXpKd4WN`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "2b91797d-eeee-4d31-a2ce-3e9e30000c8d",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Jo47KmKjvBqHb9SFyqPQg9`</summary>

```json
{
  "server": "westb-23072",
  "command": "stat -c '%Y %n' /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/correlation_analysis.py /root/recovery_aware_struct_prune/src/prune.py /root/recovery_aware_struct_prune/src/importance_score.py 2>&1",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "9601ef4d-3ad7-4c6b-b5fb-c9e5d24a7ff3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8PfBsJE1RFMPNCfJ22ZTC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1017,
      "cache_read_input_tokens": 25122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1017
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

_source line 9 · 2026-05-14T05:28:22.146Z_

<details><summary>↩ Tool result · `toolu_01Jo47KmKjvBqHb9SFyqPQg9`</summary>

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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "fbffac8a-e1f6-4a94-b426-768c95ff8a26",
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01ViXuZ1dc8uxxyBBFP3qqfT`</summary>

```json
{
  "server": "westb-23072",
  "command": "stat -c '%Y %n' /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/correlation_analysis.py /root/recovery_aware_struct_prune/src/prune.py /root/recovery_aware_struct_prune/src/importance_score.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "91c2c742-b733-46e6-a275-02aa31d96d00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JyFCUXNqC8uFthZCLBkDrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 26139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 284
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

_source line 11 · 2026-05-14T05:28:27.403Z_

<details><summary>↩ Tool result · `toolu_01ViXuZ1dc8uxxyBBFP3qqfT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"1778735926 /root/recovery_aware_struct_prune/src/cka_overlap.py\\n1778731373 /root/recovery_aware_struct_prune/src/correlation_analysis.py\\n1778728609 /root/recovery_aware_struct_prune/src/prune.py\\n1778736119 /root/recovery_aware_struct_prune/src/importance_score.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "62715a56-cec4-4a70-af8c-07b6b46fccb7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"1778735926 /root/recovery_aware_struct_prune/src/cka_overlap.py\\\\n1778731373 /root/recovery_aware_struct_prune/src/correlation_analysis.py\\\\n1778728609 /root/recovery_aware_struct_prune/src/prune.py\\\\n1778736119 /root/recovery_aware_struct_prune/src/importance_score.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"1778735926 /root/recovery_aware_struct_prune/src/cka_overlap.py\\n1778731373 /root/recovery_aware_struct_prune/src/correlation_analysis.py\\n1778728609 /root/recovery_aware_struct_prune/src/prune.py\\n1778736119 /root/recovery_aware_struct_prune/src/importance_score.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.77}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

第一次 mtime 记录完成。等 30 秒后再检查一次。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "eab38644-0007-48f6-94f1-bf798d60bea5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGExtsHP9PrVoXEEGLm6vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 26423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
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

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_019Rtgu3Ps76vGYw9FuvQyZ4`</summary>

```json
{
  "command": "sleep 30 && echo \"done\"",
  "description": "Wait 30 seconds before second mtime check"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "07599831-468b-4b05-924e-5bb4e2a50e6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGExtsHP9PrVoXEEGLm6vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 26423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
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

_source line 14 · 2026-05-14T05:28:30.736Z_

<details><summary>↩ Tool result · reported error · `toolu_019Rtgu3Ps76vGYw9FuvQyZ4`</summary>

```text
&lt;tool_use_error>Blocked: sleep 30 followed by: echo "done". To wait for a condition, use Monitor with an until-loop (e.g. `until &lt;check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "7b9fa987-54d7-48a3-ac93-214e7a5d31e9",
  "tool_use_result": "Error: Blocked: sleep 30 followed by: echo \"done\". To wait for a condition, use Monitor with an until-loop (e.g. `until &lt;check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block."
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_01TTqENnPyTLgBB1ics6QCzV`</summary>

```json
{
  "command": "until [ $(($(date +%s) - 1747220000)) -gt 30 ]; do sleep 2; done && echo \"done\"",
  "description": "Wait ~30 seconds for file stability check",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "1621d805-5030-43d7-88d9-e374f9a2c467",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhkVBunnEwb8UVWZfTFYAw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 26785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 218
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

_source line 16 · 2026-05-14T05:28:34.113Z_

<details><summary>↩ Tool result · `toolu_01TTqENnPyTLgBB1ics6QCzV`</summary>

```text
done
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "ebf0f246-36e8-460a-aeec-50926e9b29fb",
  "tool_use_result": {
    "stdout": "done",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014HVChp9WHENCFys4VUztrw`</summary>

```json
{
  "server": "westb-23072",
  "command": "stat -c '%Y %n' /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/correlation_analysis.py /root/recovery_aware_struct_prune/src/prune.py /root/recovery_aware_struct_prune/src/importance_score.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "c5058bf7-46dc-4189-bc88-66c339b40cf0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W4BfEtvSThFMpDaAZPcLWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 142,
      "cache_read_input_tokens": 27003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 142
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

_source line 18 · 2026-05-14T05:28:38.015Z_

<details><summary>↩ Tool result · `toolu_014HVChp9WHENCFys4VUztrw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"1778735926 /root/recovery_aware_struct_prune/src/cka_overlap.py\\n1778731373 /root/recovery_aware_struct_prune/src/correlation_analysis.py\\n1778728609 /root/recovery_aware_struct_prune/src/prune.py\\n1778736119 /root/recovery_aware_struct_prune/src/importance_score.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "514a06c0-317a-4d35-9596-808a4b8d2a39",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"1778735926 /root/recovery_aware_struct_prune/src/cka_overlap.py\\\\n1778731373 /root/recovery_aware_struct_prune/src/correlation_analysis.py\\\\n1778728609 /root/recovery_aware_struct_prune/src/prune.py\\\\n1778736119 /root/recovery_aware_struct_prune/src/importance_score.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"1778735926 /root/recovery_aware_struct_prune/src/cka_overlap.py\\n1778731373 /root/recovery_aware_struct_prune/src/correlation_analysis.py\\n1778728609 /root/recovery_aware_struct_prune/src/prune.py\\n1778736119 /root/recovery_aware_struct_prune/src/importance_score.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
mtime values are identical between the two checks:
- cka_overlap.py: 1778735926
- correlation_analysis.py: 1778731373
- prune.py: 1778728609
- importance_score.py: 1778736119

Files are stable. Now I need to read all four files to understand the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "4df66652-0f25-4634-8e54-04e8ef1f3ca2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Y4WJhVJ6fzWqNyMtejG2S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 27145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
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

_source line 20_

文件 mtime 两次检查完全一致，文件已稳定。现在读取所有四个文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "6b2c0a70-bfa9-4a7b-96c6-e7c5c6914a54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Y4WJhVJ6fzWqNyMtejG2S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 27145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
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

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SJEzTEHajgbvhmA57QCFME`</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/recovery_aware_struct_prune/src/cka_overlap.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "a297c874-d04a-4f61-a441-a7b31c625e46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Y4WJhVJ6fzWqNyMtejG2S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 27145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
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

_source line 22 · 2026-05-14T05:28:43.011Z_

<details><summary>↩ Tool result · `toolu_01SJEzTEHajgbvhmA57QCFME`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCKA Overlap Computation for RASP.\\n\\nComputes intra-layer functional overlap F(g) for each GQA group and MLP channel group\\nusing linear CKA (Centered Kernel Alignment via HSIC).\\n\\nGQA group: each group contains heads_per_kv Q heads + 1 KV head.\\nActivations are the concatenation of Q head outputs within the group.\\n\\nInput:  model + calibration data (GSM8K train subset)\\nOutput: per-structure F(g) scores saved as dict in .pt file\\n        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_kv_heads]]),\\n              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport logging\\nimport math\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:\\n    \\\"\\\"\\\"Linear CKA between two activation matrices.\\n    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].\\n    \\\"\\\"\\\"\\n    X = X - X.mean(0)\\n    Y = Y - Y.mean(0)\\n    hsic_xy = torch.norm(X.T @ Y, \\\"fro\\\") ** 2\\n    hsic_xx = torch.norm(X.T @ X, \\\"fro\\\") ** 2\\n    hsic_yy = torch.norm(Y.T @ Y, \\\"fro\\\") ** 2\\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    \\\"\\\"\\\"Load GSM8K train questions as calibration prompts.\\\"\\\"\\\"\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef collect_head_activations(model, tokenizer, calibration_data, device):\\n    \\\"\\\"\\\"Collect per-GQA-group activations by concatenating Q heads within each group.\\n\\n    Returns dict[layer_idx] -> tensor[n_samples, n_kv_heads, heads_per_kv * head_dim]\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_layers = config.num_hidden_layers\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n\\n    q_proj_outputs = {i: [] for i in range(n_layers)}\\n\\n    def make_q_hook(layer_idx):\\n        def hook_fn(module, input, output):\\n            q_proj_outputs[layer_idx].append(output.detach())\\n        return hook_fn\\n\\n    hooks = []\\n    for i in range(n_layers):\\n        layer = model.model.layers[i]\\n        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))\\n        hooks.append(h)\\n\\n    model.eval()\\n    with torch.no_grad():\\n        for batch_idx, enc in enumerate(calibration_data):\\n            input_ids = enc[\\\"input_ids\\\"].to(device)\\n            attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\n            if (batch_idx + 1) % 50 == 0:\\n                logger.info(f\\\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\\\")\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    layer_activations = {}\\n    for layer_idx in range(n_layers):\\n        tensors = q_proj_outputs[layer_idx]\\n        per_group_list = []\\n        for t in tensors:\\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\\n            t = t.view(t.shape[0], n_kv_heads, heads_per_kv, head_dim)\\n            t = t.reshape(t.shape[0], n_kv_heads, heads_per_kv * head_dim)\\n            t = t.mean(dim=0)  # [n_kv_heads, heads_per_kv * head_dim]\\n            per_group_list.append(t)\\n        layer_act\\n\\n... [截断: 输出过长，省略 2186 字符] ...\\n\\ntrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA\\n    \\\"\\\"\\\"\\n    overlap_scores = {}\\n    cka_matrices = {}\\n    for layer_idx, acts in activations_dict.items():\\n        n_samples, n_structs, dim = acts.shape\\n        matrix = torch.zeros(n_structs, n_structs)\\n        for i in range(n_structs):\\n            matrix[i, i] = 1.0\\n            for j in range(i + 1, n_structs):\\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\\n                matrix[i, j] = val\\n                matrix[j, i] = val\\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\\n        overlap_scores[layer_idx] = scores\\n        cka_matrices[layer_idx] = matrix\\n        logger.info(\\n            f\\\"  Layer {layer_idx} {structure_name}: F(g) range [{scores.min():.4f}, {scores.max():.4f}], \\\"\\n            f\\\"mean={scores.mean():.4f}\\\"\\n        )\\n    return overlap_scores, cka_matrices\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Compute CKA-based functional overlap scores for RASP\\\")\\n    parser.add_argument(\\\"--model_path\\\", type=str, required=True, help=\\\"Path to pretrained model\\\")\\n    parser.add_argument(\\\"--output_path\\\", type=str, required=True, help=\\\"Output .pt file for overlap scores\\\")\\n    parser.add_argument(\\\"--n_samples\\\", type=int, default=512, help=\\\"Number of calibration samples\\\")\\n    parser.add_argument(\\\"--max_length\\\", type=int, default=512, help=\\\"Max token length for calibration inputs\\\")\\n    parser.add_argument(\\\"--mlp_groups\\\", type=int, default=28, help=\\\"Number of MLP channel groups per layer\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--dtype\\\", type=str, default=\\\"bfloat16\\\", choices=[\\\"float16\\\", \\\"bfloat16\\\", \\\"float32\\\"])\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(\\\"cuda\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    dtype_map = {\\\"float16\\\": torch.float16, \\\"bfloat16\\\": torch.bfloat16, \\\"float32\\\": torch.float32}\\n    torch_dtype = dtype_map[args.dtype]\\n\\n    logger.info(f\\\"Loading model from {args.model_path}\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        args.model_path,\\n        torch_dtype=torch_dtype,\\n        device_map=device,\\n        trust_remote_code=True,\\n    )\\n\\n    n_kv_heads = model.config.num_key_value_heads\\n    heads_per_kv = model.config.num_attention_heads // n_kv_heads\\n    logger.info(f\\\"GQA config: {n_kv_heads} KV heads, {heads_per_kv} Q heads per group\\\")\\n\\n    logger.info(f\\\"Loading {args.n_samples} calibration samples from GSM8K train\\\")\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\\n\\n    logger.info(\\\"Collecting GQA group activations...\\\")\\n    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)\\n\\n    logger.info(\\\"Computing GQA group overlap F(g)...\\\")\\n    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, \\\"gqa_groups\\\")\\n    del head_acts\\n    torch.cuda.empty_cache()\\n\\n    logger.info(\\\"Collecting MLP activations...\\\")\\n    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)\\n\\n    logger.info(\\\"Computing MLP group overlap F(g)...\\\")\\n    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, \\\"mlp_groups\\\")\\n    del mlp_acts\\n    torch.cuda.empty_cache()\\n\\n    os.makedirs(os.path.dirname(args.output_path) or \\\".\\\", exist_ok=True)\\n    result = {\\n        \\\"attn_overlap\\\": attn_overlap,\\n        \\\"mlp_overlap\\\": mlp_overlap,\\n        \\\"attn_cka_matrix\\\": attn_cka_matrix,\\n        \\\"mlp_cka_matrix\\\": mlp_cka_matrix,\\n    }\\n    torch.save(result, args.output_path)\\n    logger.info(f\\\"Saved CKA overlap scores to {args.output_path}\\\")\\n\\n    for layer_idx in sorted(attn_overlap.keys()):\\n        a = attn_overlap[layer_idx]\\n        logger.info(f\\\"  Layer {layer_idx}: attn GQA groups shape={a.shape}, \\\"\\n                     f\\\"range=[{a.min():.4f}, {a.max():.4f}]\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "75858038-92ae-4548-9d96-8aa8876bacb2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nCKA Overlap Computation for RASP.\\\\n\\\\nComputes intra-layer functional overlap F(g) for each GQA group and MLP channel group\\\\nusing linear CKA (Centered Kernel Alignment via HSIC).\\\\n\\\\nGQA group: each group contains heads_per_kv Q heads + 1 KV head.\\\\nActivations are the concatenation of Q head outputs within the group.\\\\n\\\\nInput:  model + calibration data (GSM8K train subset)\\\\nOutput: per-structure F(g) scores saved as dict in .pt file\\\\n        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_kv_heads]]),\\\\n              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport logging\\\\nimport math\\\\nimport os\\\\nimport random\\\\n\\\\nimport numpy as np\\\\nimport torch\\\\nfrom datasets import load_dataset\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n)\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n\\\\ndef set_seed(seed: int):\\\\n    random.seed(seed)\\\\n    np.random.seed(seed)\\\\n    torch.manual_seed(seed)\\\\n    torch.cuda.manual_seed_all(seed)\\\\n\\\\n\\\\ndef linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Linear CKA between two activation matrices.\\\\n    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    X = X - X.mean(0)\\\\n    Y = Y - Y.mean(0)\\\\n    hsic_xy = torch.norm(X.T @ Y, \\\\\\\"fro\\\\\\\") ** 2\\\\n    hsic_xx = torch.norm(X.T @ X, \\\\\\\"fro\\\\\\\") ** 2\\\\n    hsic_yy = torch.norm(Y.T @ Y, \\\\\\\"fro\\\\\\\") ** 2\\\\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\\\\n\\\\n\\\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load GSM8K train questions as calibration prompts.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    ds = load_dataset(\\\\\\\"openai/gsm8k\\\\\\\", \\\\\\\"main\\\\\\\", split=\\\\\\\"train\\\\\\\")\\\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\\\n\\\\n    encodings = []\\\\n    for example in ds:\\\\n        prompt = f\\\\\\\"Question: {example['question']}\\\\\\\\nAnswer: Let me think step by step.\\\\\\\\n\\\\\\\"\\\\n        ids = tokenizer(prompt, return_tensors=\\\\\\\"pt\\\\\\\", truncation=True, max_length=max_length)\\\\n        encodings.append(ids)\\\\n    return encodings\\\\n\\\\n\\\\ndef collect_head_activations(model, tokenizer, calibration_data, device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Collect per-GQA-group activations by concatenating Q heads within each group.\\\\n\\\\n    Returns dict[layer_idx] -> tensor[n_samples, n_kv_heads, heads_per_kv * head_dim]\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    config = model.config\\\\n    n_layers = config.num_hidden_layers\\\\n    n_heads = config.num_attention_heads\\\\n    n_kv_heads = config.num_key_value_heads\\\\n    head_dim = config.hidden_size // n_heads\\\\n    heads_per_kv = n_heads // n_kv_heads\\\\n\\\\n    q_proj_outputs = {i: [] for i in range(n_layers)}\\\\n\\\\n    def make_q_hook(layer_idx):\\\\n        def hook_fn(module, input, output):\\\\n            q_proj_outputs[layer_idx].append(output.detach())\\\\n        return hook_fn\\\\n\\\\n    hooks = []\\\\n    for i in range(n_layers):\\\\n        layer = model.model.layers[i]\\\\n        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))\\\\n        hooks.append(h)\\\\n\\\\n    model.eval()\\\\n    with torch.no_grad():\\\\n        for batch_idx, enc in enumerate(calibration_data):\\\\n            input_ids = enc[\\\\\\\"input_ids\\\\\\\"].to(device)\\\\n            attention_mask = enc[\\\\\\\"attention_mask\\\\\\\"].to(device)\\\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\\\n            if (batch_idx + 1) % 50 == 0:\\\\n                logger.info(f\\\\\\\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\\\\\\\")\\\\n\\\\n    for h in hooks:\\\\n        h.remove()\\\\n\\\\n    layer_activations = {}\\\\n    for layer_idx in range(n_layers):\\\\n        tensors = q_proj_outputs[layer_idx]\\\\n        per_group_list = []\\\\n        for t in tensors:\\\\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\\\\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\\\\n            t = t.view(t.shape[0], n_kv_heads, heads_per_kv, head_dim)\\\\n            t = t.reshape(t.shape[0], n_kv_heads, heads_per_kv * head_dim)\\\\n            t = t.mean(dim=0)  # [n_kv_heads, heads_per_kv * head_dim]\\\\n            per_group_list.append(t)\\\\n        layer_act\\\\n\\\\n... [截断: 输出过长，省略 2186 字符] ...\\\\n\\\\ntrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    overlap_scores = {}\\\\n    cka_matrices = {}\\\\n    for layer_idx, acts in activations_dict.items():\\\\n        n_samples, n_structs, dim = acts.shape\\\\n        matrix = torch.zeros(n_structs, n_structs)\\\\n        for i in range(n_structs):\\\\n            matrix[i, i] = 1.0\\\\n            for j in range(i + 1, n_structs):\\\\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\\\\n                matrix[i, j] = val\\\\n                matrix[j, i] = val\\\\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\\\\n        overlap_scores[layer_idx] = scores\\\\n        cka_matrices[layer_idx] = matrix\\\\n        logger.info(\\\\n            f\\\\\\\"  Layer {layer_idx} {structure_name}: F(g) range [{scores.min():.4f}, {scores.max():.4f}], \\\\\\\"\\\\n            f\\\\\\\"mean={scores.mean():.4f}\\\\\\\"\\\\n        )\\\\n    return overlap_scores, cka_matrices\\\\n\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(description=\\\\\\\"Compute CKA-based functional overlap scores for RASP\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--model_path\\\\\\\", type=str, required=True, help=\\\\\\\"Path to pretrained model\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output_path\\\\\\\", type=str, required=True, help=\\\\\\\"Output .pt file for overlap scores\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--n_samples\\\\\\\", type=int, default=512, help=\\\\\\\"Number of calibration samples\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--max_length\\\\\\\", type=int, default=512, help=\\\\\\\"Max token length for calibration inputs\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--mlp_groups\\\\\\\", type=int, default=28, help=\\\\\\\"Number of MLP channel groups per layer\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42, help=\\\\\\\"Random seed\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--dtype\\\\\\\", type=str, default=\\\\\\\"bfloat16\\\\\\\", choices=[\\\\\\\"float16\\\\\\\", \\\\\\\"bfloat16\\\\\\\", \\\\\\\"float32\\\\\\\"])\\\\n    args = parser.parse_args()\\\\n\\\\n    set_seed(args.seed)\\\\n    device = torch.device(\\\\\\\"cuda\\\\\\\" if torch.cuda.is_available() else \\\\\\\"cpu\\\\\\\")\\\\n    dtype_map = {\\\\\\\"float16\\\\\\\": torch.float16, \\\\\\\"bfloat16\\\\\\\": torch.bfloat16, \\\\\\\"float32\\\\\\\": torch.float32}\\\\n    torch_dtype = dtype_map[args.dtype]\\\\n\\\\n    logger.info(f\\\\\\\"Loading model from {args.model_path}\\\\\\\")\\\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\\\n    model = AutoModelForCausalLM.from_pretrained(\\\\n        args.model_path,\\\\n        torch_dtype=torch_dtype,\\\\n        device_map=device,\\\\n        trust_remote_code=True,\\\\n    )\\\\n\\\\n    n_kv_heads = model.config.num_key_value_heads\\\\n    heads_per_kv = model.config.num_attention_heads // n_kv_heads\\\\n    logger.info(f\\\\\\\"GQA config: {n_kv_heads} KV heads, {heads_per_kv} Q heads per group\\\\\\\")\\\\n\\\\n    logger.info(f\\\\\\\"Loading {args.n_samples} calibration samples from GSM8K train\\\\\\\")\\\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\\\\n\\\\n    logger.info(\\\\\\\"Collecting GQA group activations...\\\\\\\")\\\\n    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)\\\\n\\\\n    logger.info(\\\\\\\"Computing GQA group overlap F(g)...\\\\\\\")\\\\n    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, \\\\\\\"gqa_groups\\\\\\\")\\\\n    del head_acts\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    logger.info(\\\\\\\"Collecting MLP activations...\\\\\\\")\\\\n    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)\\\\n\\\\n    logger.info(\\\\\\\"Computing MLP group overlap F(g)...\\\\\\\")\\\\n    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, \\\\\\\"mlp_groups\\\\\\\")\\\\n    del mlp_acts\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    os.makedirs(os.path.dirname(args.output_path) or \\\\\\\".\\\\\\\", exist_ok=True)\\\\n    result = {\\\\n        \\\\\\\"attn_overlap\\\\\\\": attn_overlap,\\\\n        \\\\\\\"mlp_overlap\\\\\\\": mlp_overlap,\\\\n        \\\\\\\"attn_cka_matrix\\\\\\\": attn_cka_matrix,\\\\n        \\\\\\\"mlp_cka_matrix\\\\\\\": mlp_cka_matrix,\\\\n    }\\\\n    torch.save(result, args.output_path)\\\\n    logger.info(f\\\\\\\"Saved CKA overlap scores to {args.output_path}\\\\\\\")\\\\n\\\\n    for layer_idx in sorted(attn_overlap.keys()):\\\\n        a = attn_overlap[layer_idx]\\\\n        logger.info(f\\\\\\\"  Layer {layer_idx}: attn GQA groups shape={a.shape}, \\\\\\\"\\\\n                     f\\\\\\\"range=[{a.min():.4f}, {a.max():.4f}]\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCKA Overlap Computation for RASP.\\n\\nComputes intra-layer functional overlap F(g) for each GQA group and MLP channel group\\nusing linear CKA (Centered Kernel Alignment via HSIC).\\n\\nGQA group: each group contains heads_per_kv Q heads + 1 KV head.\\nActivations are the concatenation of Q head outputs within the group.\\n\\nInput:  model + calibration data (GSM8K train subset)\\nOutput: per-structure F(g) scores saved as dict in .pt file\\n        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_kv_heads]]),\\n              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport logging\\nimport math\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:\\n    \\\"\\\"\\\"Linear CKA between two activation matrices.\\n    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].\\n    \\\"\\\"\\\"\\n    X = X - X.mean(0)\\n    Y = Y - Y.mean(0)\\n    hsic_xy = torch.norm(X.T @ Y, \\\"fro\\\") ** 2\\n    hsic_xx = torch.norm(X.T @ X, \\\"fro\\\") ** 2\\n    hsic_yy = torch.norm(Y.T @ Y, \\\"fro\\\") ** 2\\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    \\\"\\\"\\\"Load GSM8K train questions as calibration prompts.\\\"\\\"\\\"\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef collect_head_activations(model, tokenizer, calibration_data, device):\\n    \\\"\\\"\\\"Collect per-GQA-group activations by concatenating Q heads within each group.\\n\\n    Returns dict[layer_idx] -> tensor[n_samples, n_kv_heads, heads_per_kv * head_dim]\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_layers = config.num_hidden_layers\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n\\n    q_proj_outputs = {i: [] for i in range(n_layers)}\\n\\n    def make_q_hook(layer_idx):\\n        def hook_fn(module, input, output):\\n            q_proj_outputs[layer_idx].append(output.detach())\\n        return hook_fn\\n\\n    hooks = []\\n    for i in range(n_layers):\\n        layer = model.model.layers[i]\\n        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))\\n        hooks.append(h)\\n\\n    model.eval()\\n    with torch.no_grad():\\n        for batch_idx, enc in enumerate(calibration_data):\\n            input_ids = enc[\\\"input_ids\\\"].to(device)\\n            attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\n            if (batch_idx + 1) % 50 == 0:\\n                logger.info(f\\\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\\\")\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    layer_activations = {}\\n    for layer_idx in range(n_layers):\\n        tensors = q_proj_outputs[layer_idx]\\n        per_group_list = []\\n        for t in tensors:\\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\\n            t = t.view(t.shape[0], n_kv_heads, heads_per_kv, head_dim)\\n            t = t.reshape(t.shape[0], n_kv_heads, heads_per_kv * head_dim)\\n            t = t.mean(dim=0)  # [n_kv_heads, heads_per_kv * head_dim]\\n            per_group_list.append(t)\\n        layer_act\\n\\n... [截断: 输出过长，省略 2186 字符] ...\\n\\ntrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA\\n    \\\"\\\"\\\"\\n    overlap_scores = {}\\n    cka_matrices = {}\\n    for layer_idx, acts in activations_dict.items():\\n        n_samples, n_structs, dim = acts.shape\\n        matrix = torch.zeros(n_structs, n_structs)\\n        for i in range(n_structs):\\n            matrix[i, i] = 1.0\\n            for j in range(i + 1, n_structs):\\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\\n                matrix[i, j] = val\\n                matrix[j, i] = val\\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\\n        overlap_scores[layer_idx] = scores\\n        cka_matrices[layer_idx] = matrix\\n        logger.info(\\n            f\\\"  Layer {layer_idx} {structure_name}: F(g) range [{scores.min():.4f}, {scores.max():.4f}], \\\"\\n            f\\\"mean={scores.mean():.4f}\\\"\\n        )\\n    return overlap_scores, cka_matrices\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Compute CKA-based functional overlap scores for RASP\\\")\\n    parser.add_argument(\\\"--model_path\\\", type=str, required=True, help=\\\"Path to pretrained model\\\")\\n    parser.add_argument(\\\"--output_path\\\", type=str, required=True, help=\\\"Output .pt file for overlap scores\\\")\\n    parser.add_argument(\\\"--n_samples\\\", type=int, default=512, help=\\\"Number of calibration samples\\\")\\n    parser.add_argument(\\\"--max_length\\\", type=int, default=512, help=\\\"Max token length for calibration inputs\\\")\\n    parser.add_argument(\\\"--mlp_groups\\\", type=int, default=28, help=\\\"Number of MLP channel groups per layer\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--dtype\\\", type=str, default=\\\"bfloat16\\\", choices=[\\\"float16\\\", \\\"bfloat16\\\", \\\"float32\\\"])\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(\\\"cuda\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    dtype_map = {\\\"float16\\\": torch.float16, \\\"bfloat16\\\": torch.bfloat16, \\\"float32\\\": torch.float32}\\n    torch_dtype = dtype_map[args.dtype]\\n\\n    logger.info(f\\\"Loading model from {args.model_path}\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        args.model_path,\\n        torch_dtype=torch_dtype,\\n        device_map=device,\\n        trust_remote_code=True,\\n    )\\n\\n    n_kv_heads = model.config.num_key_value_heads\\n    heads_per_kv = model.config.num_attention_heads // n_kv_heads\\n    logger.info(f\\\"GQA config: {n_kv_heads} KV heads, {heads_per_kv} Q heads per group\\\")\\n\\n    logger.info(f\\\"Loading {args.n_samples} calibration samples from GSM8K train\\\")\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\\n\\n    logger.info(\\\"Collecting GQA group activations...\\\")\\n    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)\\n\\n    logger.info(\\\"Computing GQA group overlap F(g)...\\\")\\n    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, \\\"gqa_groups\\\")\\n    del head_acts\\n    torch.cuda.empty_cache()\\n\\n    logger.info(\\\"Collecting MLP activations...\\\")\\n    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)\\n\\n    logger.info(\\\"Computing MLP group overlap F(g)...\\\")\\n    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, \\\"mlp_groups\\\")\\n    del mlp_acts\\n    torch.cuda.empty_cache()\\n\\n    os.makedirs(os.path.dirname(args.output_path) or \\\".\\\", exist_ok=True)\\n    result = {\\n        \\\"attn_overlap\\\": attn_overlap,\\n        \\\"mlp_overlap\\\": mlp_overlap,\\n        \\\"attn_cka_matrix\\\": attn_cka_matrix,\\n        \\\"mlp_cka_matrix\\\": mlp_cka_matrix,\\n    }\\n    torch.save(result, args.output_path)\\n    logger.info(f\\\"Saved CKA overlap scores to {args.output_path}\\\")\\n\\n    for layer_idx in sorted(attn_overlap.keys()):\\n        a = attn_overlap[layer_idx]\\n        logger.info(f\\\"  Layer {layer_idx}: attn GQA groups shape={a.shape}, \\\"\\n                     f\\\"range=[{a.min():.4f}, {a.max():.4f}]\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"
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
Good. cka_overlap.py already has `mlp_cka_matrix` in the output. Let me note the key structure:
- Output includes: `attn_overlap`, `mlp_overlap`, `attn_cka_matrix`, `mlp_cka_matrix`
- `compute_overlap` returns both overlap scores and CKA matrices
- MLP activations collected via `collect_mlp_activations` with `n_groups` param (default 28)

Now let me read the other files. The output was truncated - I need to see the `collect_mlp_activations` function. 

Let me check the other files to understand the full picture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "00b38226-d352-41ad-af62-c634cdc9a98e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfU4vMexQQTkSyGGg9trsX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3706,
      "cache_read_input_tokens": 27507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3706
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

_source line 24_

cka_overlap.py 已包含 `mlp_cka_matrix`。输出被截断，需要看 `collect_mlp_activations` 函数。同时读取其他文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "0aaedcd0-3b8b-440b-ae2b-6d351aa3d38f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfU4vMexQQTkSyGGg9trsX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3706,
      "cache_read_input_tokens": 27507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3706
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

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YXNoBZ2hNNsZfcTzRvNQup`</summary>

```json
{
  "server": "westb-23072",
  "command": "wc -l /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/correlation_analysis.py /root/recovery_aware_struct_prune/src/prune.py /root/recovery_aware_struct_prune/src/importance_score.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "d936df43-165a-4ad2-80e3-1733d12d50e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfU4vMexQQTkSyGGg9trsX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3706,
      "cache_read_input_tokens": 27507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3706
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

_source line 26 · 2026-05-14T05:28:50.690Z_

<details><summary>↩ Tool result · `toolu_01YXNoBZ2hNNsZfcTzRvNQup`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  263 /root/recovery_aware_struct_prune/src/cka_overlap.py\\n  335 /root/recovery_aware_struct_prune/src/correlation_analysis.py\\n  411 /root/recovery_aware_struct_prune/src/prune.py\\n  219 /root/recovery_aware_struct_prune/src/importance_score.py\\n 1228 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "5450cc4c-0b5b-4e7e-be02-3e66555f3bba",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  263 /root/recovery_aware_struct_prune/src/cka_overlap.py\\\\n  335 /root/recovery_aware_struct_prune/src/correlation_analysis.py\\\\n  411 /root/recovery_aware_struct_prune/src/prune.py\\\\n  219 /root/recovery_aware_struct_prune/src/importance_score.py\\\\n 1228 total\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  263 /root/recovery_aware_struct_prune/src/cka_overlap.py\\n  335 /root/recovery_aware_struct_prune/src/correlation_analysis.py\\n  411 /root/recovery_aware_struct_prune/src/prune.py\\n  219 /root/recovery_aware_struct_prune/src/importance_score.py\\n 1228 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011V5RFwaRzpnQWXHjF2RZC7`</summary>

```json
{
  "server": "westb-23072",
  "command": "head -160 /root/recovery_aware_struct_prune/src/cka_overlap.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "bd86e3c0-8480-4a86-af21-9431ccdbda8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEsZ1y8EWVHiRaUQ7FtKuC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 575,
      "cache_read_input_tokens": 31213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 575
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

_source line 28 · 2026-05-14T05:28:56.427Z_

<details><summary>↩ Tool result · `toolu_011V5RFwaRzpnQWXHjF2RZC7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCKA Overlap Computation for RASP.\\n\\nComputes intra-layer functional overlap F(g) for each GQA group and MLP channel group\\nusing linear CKA (Centered Kernel Alignment via HSIC).\\n\\nGQA group: each group contains heads_per_kv Q heads + 1 KV head.\\nActivations are the concatenation of Q head outputs within the group.\\n\\nInput:  model + calibration data (GSM8K train subset)\\nOutput: per-structure F(g) scores saved as dict in .pt file\\n        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_kv_heads]]),\\n              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport logging\\nimport math\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:\\n    \\\"\\\"\\\"Linear CKA between two activation matrices.\\n    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].\\n    \\\"\\\"\\\"\\n    X = X - X.mean(0)\\n    Y = Y - Y.mean(0)\\n    hsic_xy = torch.norm(X.T @ Y, \\\"fro\\\") ** 2\\n    hsic_xx = torch.norm(X.T @ X, \\\"fro\\\") ** 2\\n    hsic_yy = torch.norm(Y.T @ Y, \\\"fro\\\") ** 2\\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    \\\"\\\"\\\"Load GSM8K train questions as calibration prompts.\\\"\\\"\\\"\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef collect_head_activations(model, tokenizer, calibration_data, device):\\n    \\\"\\\"\\\"Collect per-GQA-group activations by concatenating Q heads within each group.\\n\\n    Returns dict[layer_idx] -> tensor[n_samples, n_kv_heads, heads_per_kv * head_dim]\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_layers = config.num_hidden_layers\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n\\n    q_proj_outputs = {i: [] for i in range(n_layers)}\\n\\n    def make_q_hook(layer_idx):\\n        def hook_fn(module, input, output):\\n            q_proj_outputs[layer_idx].append(output.detach())\\n        return hook_fn\\n\\n    hooks = []\\n    for i in range(n_layers):\\n        layer = model.model.layers[i]\\n        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))\\n        hooks.append(h)\\n\\n    model.eval()\\n    with torch.no_grad():\\n        for batch_idx, enc in enumerate(calibration_data):\\n            input_ids = enc[\\\"input_ids\\\"].to(device)\\n            attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\n            if (batch_idx + 1) % 50 == 0:\\n                logger.info(f\\\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\\\")\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    layer_activations = {}\\n    for layer_idx in range(n_layers):\\n        tensors = q_proj_outputs[layer_idx]\\n        per_group_list = []\\n        for t in tensors:\\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\\n            t = t.view(t.shape[0], n_kv_heads, heads_per_kv, head_dim)\\n            t = t.reshape(t.shape[0], n_kv_heads, heads_per_kv * head_dim)\\n            t = t.mean(dim=0)  # [n_kv_heads, heads_per_kv * head_dim]\\n            per_group_list.append(t)\\n        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)\\n        q_proj_outputs[layer_idx] = None\\n\\n    return layer_activations\\n\\n\\ndef collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups: int = 28):\\n    \\\"\\\"\\\"Collect MLP intermediate activations grouped into channel groups.\\n\\n    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim]\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_layers = config.num_hidden_layers\\n    intermediate_size = config.intermediate_size\\n    group_size = intermediate_size // n_groups\\n\\n    gate_outputs = {i: [] for i in range(n_layers)}\\n    hooks = []\\n\\n    def make_gate_hook(layer_idx):\\n        def hook_fn(module, input, output):\\n            gate_outputs[layer_idx].append(output.detach())\\n        return hook_fn\\n\\n    for i in range(n_layers):\\n        layer = model.model.layers[i]\\n        h = layer.mlp.gate_proj.register_forward_hook(make_gate_hook(i))\\n        hooks.append(h)\\n\\n    model.eval()\\n    with torch.no_grad():\\n        for enc in calibration_data:\\n            input_ids = enc[\\\"input_ids\\\"].to(device)\\n            attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    layer_activations = {}\\n    for layer_idx in range(n_layers):\\n        tensors = gate_outputs[layer_idx]\\n        per_group_list = []\\n        for t in tensors:\\n            t = t.squeeze(0)  # [seq, intermediate_size]\\n            t = t.mean(dim=0)  # [intermediate_size]\\n            usable = n_groups * group_size\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "4202b3ec-4c89-4e73-84c0-b255fb8d3e9d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nCKA Overlap Computation for RASP.\\\\n\\\\nComputes intra-layer functional overlap F(g) for each GQA group and MLP channel group\\\\nusing linear CKA (Centered Kernel Alignment via HSIC).\\\\n\\\\nGQA group: each group contains heads_per_kv Q heads + 1 KV head.\\\\nActivations are the concatenation of Q head outputs within the group.\\\\n\\\\nInput:  model + calibration data (GSM8K train subset)\\\\nOutput: per-structure F(g) scores saved as dict in .pt file\\\\n        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_kv_heads]]),\\\\n              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport logging\\\\nimport math\\\\nimport os\\\\nimport random\\\\n\\\\nimport numpy as np\\\\nimport torch\\\\nfrom datasets import load_dataset\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n)\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n\\\\ndef set_seed(seed: int):\\\\n    random.seed(seed)\\\\n    np.random.seed(seed)\\\\n    torch.manual_seed(seed)\\\\n    torch.cuda.manual_seed_all(seed)\\\\n\\\\n\\\\ndef linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Linear CKA between two activation matrices.\\\\n    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    X = X - X.mean(0)\\\\n    Y = Y - Y.mean(0)\\\\n    hsic_xy = torch.norm(X.T @ Y, \\\\\\\"fro\\\\\\\") ** 2\\\\n    hsic_xx = torch.norm(X.T @ X, \\\\\\\"fro\\\\\\\") ** 2\\\\n    hsic_yy = torch.norm(Y.T @ Y, \\\\\\\"fro\\\\\\\") ** 2\\\\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\\\\n\\\\n\\\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load GSM8K train questions as calibration prompts.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    ds = load_dataset(\\\\\\\"openai/gsm8k\\\\\\\", \\\\\\\"main\\\\\\\", split=\\\\\\\"train\\\\\\\")\\\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\\\n\\\\n    encodings = []\\\\n    for example in ds:\\\\n        prompt = f\\\\\\\"Question: {example['question']}\\\\\\\\nAnswer: Let me think step by step.\\\\\\\\n\\\\\\\"\\\\n        ids = tokenizer(prompt, return_tensors=\\\\\\\"pt\\\\\\\", truncation=True, max_length=max_length)\\\\n        encodings.append(ids)\\\\n    return encodings\\\\n\\\\n\\\\ndef collect_head_activations(model, tokenizer, calibration_data, device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Collect per-GQA-group activations by concatenating Q heads within each group.\\\\n\\\\n    Returns dict[layer_idx] -> tensor[n_samples, n_kv_heads, heads_per_kv * head_dim]\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    config = model.config\\\\n    n_layers = config.num_hidden_layers\\\\n    n_heads = config.num_attention_heads\\\\n    n_kv_heads = config.num_key_value_heads\\\\n    head_dim = config.hidden_size // n_heads\\\\n    heads_per_kv = n_heads // n_kv_heads\\\\n\\\\n    q_proj_outputs = {i: [] for i in range(n_layers)}\\\\n\\\\n    def make_q_hook(layer_idx):\\\\n        def hook_fn(module, input, output):\\\\n            q_proj_outputs[layer_idx].append(output.detach())\\\\n        return hook_fn\\\\n\\\\n    hooks = []\\\\n    for i in range(n_layers):\\\\n        layer = model.model.layers[i]\\\\n        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))\\\\n        hooks.append(h)\\\\n\\\\n    model.eval()\\\\n    with torch.no_grad():\\\\n        for batch_idx, enc in enumerate(calibration_data):\\\\n            input_ids = enc[\\\\\\\"input_ids\\\\\\\"].to(device)\\\\n            attention_mask = enc[\\\\\\\"attention_mask\\\\\\\"].to(device)\\\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\\\n            if (batch_idx + 1) % 50 == 0:\\\\n                logger.info(f\\\\\\\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\\\\\\\")\\\\n\\\\n    for h in hooks:\\\\n        h.remove()\\\\n\\\\n    layer_activations = {}\\\\n    for layer_idx in range(n_layers):\\\\n        tensors = q_proj_outputs[layer_idx]\\\\n        per_group_list = []\\\\n        for t in tensors:\\\\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\\\\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\\\\n            t = t.view(t.shape[0], n_kv_heads, heads_per_kv, head_dim)\\\\n            t = t.reshape(t.shape[0], n_kv_heads, heads_per_kv * head_dim)\\\\n            t = t.mean(dim=0)  # [n_kv_heads, heads_per_kv * head_dim]\\\\n            per_group_list.append(t)\\\\n        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)\\\\n        q_proj_outputs[layer_idx] = None\\\\n\\\\n    return layer_activations\\\\n\\\\n\\\\ndef collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups: int = 28):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Collect MLP intermediate activations grouped into channel groups.\\\\n\\\\n    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim]\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    config = model.config\\\\n    n_layers = config.num_hidden_layers\\\\n    intermediate_size = config.intermediate_size\\\\n    group_size = intermediate_size // n_groups\\\\n\\\\n    gate_outputs = {i: [] for i in range(n_layers)}\\\\n    hooks = []\\\\n\\\\n    def make_gate_hook(layer_idx):\\\\n        def hook_fn(module, input, output):\\\\n            gate_outputs[layer_idx].append(output.detach())\\\\n        return hook_fn\\\\n\\\\n    for i in range(n_layers):\\\\n        layer = model.model.layers[i]\\\\n        h = layer.mlp.gate_proj.register_forward_hook(make_gate_hook(i))\\\\n        hooks.append(h)\\\\n\\\\n    model.eval()\\\\n    with torch.no_grad():\\\\n        for enc in calibration_data:\\\\n            input_ids = enc[\\\\\\\"input_ids\\\\\\\"].to(device)\\\\n            attention_mask = enc[\\\\\\\"attention_mask\\\\\\\"].to(device)\\\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\\\n\\\\n    for h in hooks:\\\\n        h.remove()\\\\n\\\\n    layer_activations = {}\\\\n    for layer_idx in range(n_layers):\\\\n        tensors = gate_outputs[layer_idx]\\\\n        per_group_list = []\\\\n        for t in tensors:\\\\n            t = t.squeeze(0)  # [seq, intermediate_size]\\\\n            t = t.mean(dim=0)  # [intermediate_size]\\\\n            usable = n_groups * group_size\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCKA Overlap Computation for RASP.\\n\\nComputes intra-layer functional overlap F(g) for each GQA group and MLP channel group\\nusing linear CKA (Centered Kernel Alignment via HSIC).\\n\\nGQA group: each group contains heads_per_kv Q heads + 1 KV head.\\nActivations are the concatenation of Q head outputs within the group.\\n\\nInput:  model + calibration data (GSM8K train subset)\\nOutput: per-structure F(g) scores saved as dict in .pt file\\n        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_kv_heads]]),\\n              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport logging\\nimport math\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:\\n    \\\"\\\"\\\"Linear CKA between two activation matrices.\\n    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].\\n    \\\"\\\"\\\"\\n    X = X - X.mean(0)\\n    Y = Y - Y.mean(0)\\n    hsic_xy = torch.norm(X.T @ Y, \\\"fro\\\") ** 2\\n    hsic_xx = torch.norm(X.T @ X, \\\"fro\\\") ** 2\\n    hsic_yy = torch.norm(Y.T @ Y, \\\"fro\\\") ** 2\\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    \\\"\\\"\\\"Load GSM8K train questions as calibration prompts.\\\"\\\"\\\"\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef collect_head_activations(model, tokenizer, calibration_data, device):\\n    \\\"\\\"\\\"Collect per-GQA-group activations by concatenating Q heads within each group.\\n\\n    Returns dict[layer_idx] -> tensor[n_samples, n_kv_heads, heads_per_kv * head_dim]\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_layers = config.num_hidden_layers\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n\\n    q_proj_outputs = {i: [] for i in range(n_layers)}\\n\\n    def make_q_hook(layer_idx):\\n        def hook_fn(module, input, output):\\n            q_proj_outputs[layer_idx].append(output.detach())\\n        return hook_fn\\n\\n    hooks = []\\n    for i in range(n_layers):\\n        layer = model.model.layers[i]\\n        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))\\n        hooks.append(h)\\n\\n    model.eval()\\n    with torch.no_grad():\\n        for batch_idx, enc in enumerate(calibration_data):\\n            input_ids = enc[\\\"input_ids\\\"].to(device)\\n            attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\n            if (batch_idx + 1) % 50 == 0:\\n                logger.info(f\\\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\\\")\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    layer_activations = {}\\n    for layer_idx in range(n_layers):\\n        tensors = q_proj_outputs[layer_idx]\\n        per_group_list = []\\n        for t in tensors:\\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\\n            t = t.view(t.shape[0], n_kv_heads, heads_per_kv, head_dim)\\n            t = t.reshape(t.shape[0], n_kv_heads, heads_per_kv * head_dim)\\n            t = t.mean(dim=0)  # [n_kv_heads, heads_per_kv * head_dim]\\n            per_group_list.append(t)\\n        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)\\n        q_proj_outputs[layer_idx] = None\\n\\n    return layer_activations\\n\\n\\ndef collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups: int = 28):\\n    \\\"\\\"\\\"Collect MLP intermediate activations grouped into channel groups.\\n\\n    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim]\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_layers = config.num_hidden_layers\\n    intermediate_size = config.intermediate_size\\n    group_size = intermediate_size // n_groups\\n\\n    gate_outputs = {i: [] for i in range(n_layers)}\\n    hooks = []\\n\\n    def make_gate_hook(layer_idx):\\n        def hook_fn(module, input, output):\\n            gate_outputs[layer_idx].append(output.detach())\\n        return hook_fn\\n\\n    for i in range(n_layers):\\n        layer = model.model.layers[i]\\n        h = layer.mlp.gate_proj.register_forward_hook(make_gate_hook(i))\\n        hooks.append(h)\\n\\n    model.eval()\\n    with torch.no_grad():\\n        for enc in calibration_data:\\n            input_ids = enc[\\\"input_ids\\\"].to(device)\\n            attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    layer_activations = {}\\n    for layer_idx in range(n_layers):\\n        tensors = gate_outputs[layer_idx]\\n        per_group_list = []\\n        for t in tensors:\\n            t = t.squeeze(0)  # [seq, intermediate_size]\\n            t = t.mean(dim=0)  # [intermediate_size]\\n            usable = n_groups * group_size\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Nem3VdJFM5vRZCZznKTm9H`</summary>

```json
{
  "server": "westb-23072",
  "command": "tail -110 /root/recovery_aware_struct_prune/src/cka_overlap.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "b5cc2e20-a628-4725-aef6-862015c5b482",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016X5vF2q2pRwVh3CQCeEoyT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2378,
      "cache_read_input_tokens": 31788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2378
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

_source line 30 · 2026-05-14T05:28:59.985Z_

<details><summary>↩ Tool result · `toolu_01Nem3VdJFM5vRZCZznKTm9H`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    for layer_idx in range(n_layers):\\n        tensors = gate_outputs[layer_idx]\\n        per_group_list = []\\n        for t in tensors:\\n            t = t.squeeze(0)  # [seq, intermediate_size]\\n            t = t.mean(dim=0)  # [intermediate_size]\\n            usable = n_groups * group_size\\n            t = t[:usable].view(n_groups, group_size)\\n            per_group_list.append(t)\\n        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)\\n        gate_outputs[layer_idx] = None\\n\\n    return layer_activations\\n\\n\\ndef compute_overlap(activations_dict: dict, structure_name: str) -> tuple:\\n    \\\"\\\"\\\"Compute F(g) = mean CKA similarity and pairwise CKA matrix per layer.\\n\\n    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]\\n    Returns: (overlap_scores, cka_matrices)\\n        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(g) in [0, 1]\\n        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA\\n    \\\"\\\"\\\"\\n    overlap_scores = {}\\n    cka_matrices = {}\\n    for layer_idx, acts in activations_dict.items():\\n        n_samples, n_structs, dim = acts.shape\\n        matrix = torch.zeros(n_structs, n_structs)\\n        for i in range(n_structs):\\n            matrix[i, i] = 1.0\\n            for j in range(i + 1, n_structs):\\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\\n                matrix[i, j] = val\\n                matrix[j, i] = val\\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\\n        overlap_scores[layer_idx] = scores\\n        cka_matrices[layer_idx] = matrix\\n        logger.info(\\n            f\\\"  Layer {layer_idx} {structure_name}: F(g) range [{scores.min():.4f}, {scores.max():.4f}], \\\"\\n            f\\\"mean={scores.mean():.4f}\\\"\\n        )\\n    return overlap_scores, cka_matrices\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Compute CKA-based functional overlap scores for RASP\\\")\\n    parser.add_argument(\\\"--model_path\\\", type=str, required=True, help=\\\"Path to pretrained model\\\")\\n    parser.add_argument(\\\"--output_path\\\", type=str, required=True, help=\\\"Output .pt file for overlap scores\\\")\\n    parser.add_argument(\\\"--n_samples\\\", type=int, default=512, help=\\\"Number of calibration samples\\\")\\n    parser.add_argument(\\\"--max_length\\\", type=int, default=512, help=\\\"Max token length for calibration inputs\\\")\\n    parser.add_argument(\\\"--mlp_groups\\\", type=int, default=28, help=\\\"Number of MLP channel groups per layer\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--dtype\\\", type=str, default=\\\"bfloat16\\\", choices=[\\\"float16\\\", \\\"bfloat16\\\", \\\"float32\\\"])\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(\\\"cuda\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    dtype_map = {\\\"float16\\\": torch.float16, \\\"bfloat16\\\": torch.bfloat16, \\\"float32\\\": torch.float32}\\n    torch_dtype = dtype_map[args.dtype]\\n\\n    logger.info(f\\\"Loading model from {args.model_path}\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        args.model_path,\\n        torch_dtype=torch_dtype,\\n        device_map=device,\\n        trust_remote_code=True,\\n    )\\n\\n    n_kv_heads = model.config.num_key_value_heads\\n    heads_per_kv = model.config.num_attention_heads // n_kv_heads\\n    logger.info(f\\\"GQA config: {n_kv_heads} KV heads, {heads_per_kv} Q heads per group\\\")\\n\\n    logger.info(f\\\"Loading {args.n_samples} calibration samples from GSM8K train\\\")\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\\n\\n    logger.info(\\\"Collecting GQA group activations...\\\")\\n    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)\\n\\n    logger.info(\\\"Computing GQA group overlap F(g)...\\\")\\n    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, \\\"gqa_groups\\\")\\n    del head_acts\\n    torch.cuda.empty_cache()\\n\\n    logger.info(\\\"Collecting MLP activations...\\\")\\n    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)\\n\\n    logger.info(\\\"Computing MLP group overlap F(g)...\\\")\\n    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, \\\"mlp_groups\\\")\\n    del mlp_acts\\n    torch.cuda.empty_cache()\\n\\n    os.makedirs(os.path.dirname(args.output_path) or \\\".\\\", exist_ok=True)\\n    result = {\\n        \\\"attn_overlap\\\": attn_overlap,\\n        \\\"mlp_overlap\\\": mlp_overlap,\\n        \\\"attn_cka_matrix\\\": attn_cka_matrix,\\n        \\\"mlp_cka_matrix\\\": mlp_cka_matrix,\\n    }\\n    torch.save(result, args.output_path)\\n    logger.info(f\\\"Saved CKA overlap scores to {args.output_path}\\\")\\n\\n    for layer_idx in sorted(attn_overlap.keys()):\\n        a = attn_overlap[layer_idx]\\n        logger.info(f\\\"  Layer {layer_idx}: attn GQA groups shape={a.shape}, \\\"\\n                     f\\\"range=[{a.min():.4f}, {a.max():.4f}]\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "ba0b6cf4-294b-4e9c-8627-f8282ba6d9c2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    for layer_idx in range(n_layers):\\\\n        tensors = gate_outputs[layer_idx]\\\\n        per_group_list = []\\\\n        for t in tensors:\\\\n            t = t.squeeze(0)  # [seq, intermediate_size]\\\\n            t = t.mean(dim=0)  # [intermediate_size]\\\\n            usable = n_groups * group_size\\\\n            t = t[:usable].view(n_groups, group_size)\\\\n            per_group_list.append(t)\\\\n        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)\\\\n        gate_outputs[layer_idx] = None\\\\n\\\\n    return layer_activations\\\\n\\\\n\\\\ndef compute_overlap(activations_dict: dict, structure_name: str) -> tuple:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute F(g) = mean CKA similarity and pairwise CKA matrix per layer.\\\\n\\\\n    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]\\\\n    Returns: (overlap_scores, cka_matrices)\\\\n        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(g) in [0, 1]\\\\n        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    overlap_scores = {}\\\\n    cka_matrices = {}\\\\n    for layer_idx, acts in activations_dict.items():\\\\n        n_samples, n_structs, dim = acts.shape\\\\n        matrix = torch.zeros(n_structs, n_structs)\\\\n        for i in range(n_structs):\\\\n            matrix[i, i] = 1.0\\\\n            for j in range(i + 1, n_structs):\\\\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\\\\n                matrix[i, j] = val\\\\n                matrix[j, i] = val\\\\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\\\\n        overlap_scores[layer_idx] = scores\\\\n        cka_matrices[layer_idx] = matrix\\\\n        logger.info(\\\\n            f\\\\\\\"  Layer {layer_idx} {structure_name}: F(g) range [{scores.min():.4f}, {scores.max():.4f}], \\\\\\\"\\\\n            f\\\\\\\"mean={scores.mean():.4f}\\\\\\\"\\\\n        )\\\\n    return overlap_scores, cka_matrices\\\\n\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(description=\\\\\\\"Compute CKA-based functional overlap scores for RASP\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--model_path\\\\\\\", type=str, required=True, help=\\\\\\\"Path to pretrained model\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output_path\\\\\\\", type=str, required=True, help=\\\\\\\"Output .pt file for overlap scores\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--n_samples\\\\\\\", type=int, default=512, help=\\\\\\\"Number of calibration samples\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--max_length\\\\\\\", type=int, default=512, help=\\\\\\\"Max token length for calibration inputs\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--mlp_groups\\\\\\\", type=int, default=28, help=\\\\\\\"Number of MLP channel groups per layer\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42, help=\\\\\\\"Random seed\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--dtype\\\\\\\", type=str, default=\\\\\\\"bfloat16\\\\\\\", choices=[\\\\\\\"float16\\\\\\\", \\\\\\\"bfloat16\\\\\\\", \\\\\\\"float32\\\\\\\"])\\\\n    args = parser.parse_args()\\\\n\\\\n    set_seed(args.seed)\\\\n    device = torch.device(\\\\\\\"cuda\\\\\\\" if torch.cuda.is_available() else \\\\\\\"cpu\\\\\\\")\\\\n    dtype_map = {\\\\\\\"float16\\\\\\\": torch.float16, \\\\\\\"bfloat16\\\\\\\": torch.bfloat16, \\\\\\\"float32\\\\\\\": torch.float32}\\\\n    torch_dtype = dtype_map[args.dtype]\\\\n\\\\n    logger.info(f\\\\\\\"Loading model from {args.model_path}\\\\\\\")\\\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\\\n    model = AutoModelForCausalLM.from_pretrained(\\\\n        args.model_path,\\\\n        torch_dtype=torch_dtype,\\\\n        device_map=device,\\\\n        trust_remote_code=True,\\\\n    )\\\\n\\\\n    n_kv_heads = model.config.num_key_value_heads\\\\n    heads_per_kv = model.config.num_attention_heads // n_kv_heads\\\\n    logger.info(f\\\\\\\"GQA config: {n_kv_heads} KV heads, {heads_per_kv} Q heads per group\\\\\\\")\\\\n\\\\n    logger.info(f\\\\\\\"Loading {args.n_samples} calibration samples from GSM8K train\\\\\\\")\\\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\\\\n\\\\n    logger.info(\\\\\\\"Collecting GQA group activations...\\\\\\\")\\\\n    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)\\\\n\\\\n    logger.info(\\\\\\\"Computing GQA group overlap F(g)...\\\\\\\")\\\\n    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, \\\\\\\"gqa_groups\\\\\\\")\\\\n    del head_acts\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    logger.info(\\\\\\\"Collecting MLP activations...\\\\\\\")\\\\n    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)\\\\n\\\\n    logger.info(\\\\\\\"Computing MLP group overlap F(g)...\\\\\\\")\\\\n    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, \\\\\\\"mlp_groups\\\\\\\")\\\\n    del mlp_acts\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    os.makedirs(os.path.dirname(args.output_path) or \\\\\\\".\\\\\\\", exist_ok=True)\\\\n    result = {\\\\n        \\\\\\\"attn_overlap\\\\\\\": attn_overlap,\\\\n        \\\\\\\"mlp_overlap\\\\\\\": mlp_overlap,\\\\n        \\\\\\\"attn_cka_matrix\\\\\\\": attn_cka_matrix,\\\\n        \\\\\\\"mlp_cka_matrix\\\\\\\": mlp_cka_matrix,\\\\n    }\\\\n    torch.save(result, args.output_path)\\\\n    logger.info(f\\\\\\\"Saved CKA overlap scores to {args.output_path}\\\\\\\")\\\\n\\\\n    for layer_idx in sorted(attn_overlap.keys()):\\\\n        a = attn_overlap[layer_idx]\\\\n        logger.info(f\\\\\\\"  Layer {layer_idx}: attn GQA groups shape={a.shape}, \\\\\\\"\\\\n                     f\\\\\\\"range=[{a.min():.4f}, {a.max():.4f}]\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    for layer_idx in range(n_layers):\\n        tensors = gate_outputs[layer_idx]\\n        per_group_list = []\\n        for t in tensors:\\n            t = t.squeeze(0)  # [seq, intermediate_size]\\n            t = t.mean(dim=0)  # [intermediate_size]\\n            usable = n_groups * group_size\\n            t = t[:usable].view(n_groups, group_size)\\n            per_group_list.append(t)\\n        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)\\n        gate_outputs[layer_idx] = None\\n\\n    return layer_activations\\n\\n\\ndef compute_overlap(activations_dict: dict, structure_name: str) -> tuple:\\n    \\\"\\\"\\\"Compute F(g) = mean CKA similarity and pairwise CKA matrix per layer.\\n\\n    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]\\n    Returns: (overlap_scores, cka_matrices)\\n        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(g) in [0, 1]\\n        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA\\n    \\\"\\\"\\\"\\n    overlap_scores = {}\\n    cka_matrices = {}\\n    for layer_idx, acts in activations_dict.items():\\n        n_samples, n_structs, dim = acts.shape\\n        matrix = torch.zeros(n_structs, n_structs)\\n        for i in range(n_structs):\\n            matrix[i, i] = 1.0\\n            for j in range(i + 1, n_structs):\\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\\n                matrix[i, j] = val\\n                matrix[j, i] = val\\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\\n        overlap_scores[layer_idx] = scores\\n        cka_matrices[layer_idx] = matrix\\n        logger.info(\\n            f\\\"  Layer {layer_idx} {structure_name}: F(g) range [{scores.min():.4f}, {scores.max():.4f}], \\\"\\n            f\\\"mean={scores.mean():.4f}\\\"\\n        )\\n    return overlap_scores, cka_matrices\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Compute CKA-based functional overlap scores for RASP\\\")\\n    parser.add_argument(\\\"--model_path\\\", type=str, required=True, help=\\\"Path to pretrained model\\\")\\n    parser.add_argument(\\\"--output_path\\\", type=str, required=True, help=\\\"Output .pt file for overlap scores\\\")\\n    parser.add_argument(\\\"--n_samples\\\", type=int, default=512, help=\\\"Number of calibration samples\\\")\\n    parser.add_argument(\\\"--max_length\\\", type=int, default=512, help=\\\"Max token length for calibration inputs\\\")\\n    parser.add_argument(\\\"--mlp_groups\\\", type=int, default=28, help=\\\"Number of MLP channel groups per layer\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--dtype\\\", type=str, default=\\\"bfloat16\\\", choices=[\\\"float16\\\", \\\"bfloat16\\\", \\\"float32\\\"])\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(\\\"cuda\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    dtype_map = {\\\"float16\\\": torch.float16, \\\"bfloat16\\\": torch.bfloat16, \\\"float32\\\": torch.float32}\\n    torch_dtype = dtype_map[args.dtype]\\n\\n    logger.info(f\\\"Loading model from {args.model_path}\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        args.model_path,\\n        torch_dtype=torch_dtype,\\n        device_map=device,\\n        trust_remote_code=True,\\n    )\\n\\n    n_kv_heads = model.config.num_key_value_heads\\n    heads_per_kv = model.config.num_attention_heads // n_kv_heads\\n    logger.info(f\\\"GQA config: {n_kv_heads} KV heads, {heads_per_kv} Q heads per group\\\")\\n\\n    logger.info(f\\\"Loading {args.n_samples} calibration samples from GSM8K train\\\")\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\\n\\n    logger.info(\\\"Collecting GQA group activations...\\\")\\n    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)\\n\\n    logger.info(\\\"Computing GQA group overlap F(g)...\\\")\\n    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, \\\"gqa_groups\\\")\\n    del head_acts\\n    torch.cuda.empty_cache()\\n\\n    logger.info(\\\"Collecting MLP activations...\\\")\\n    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)\\n\\n    logger.info(\\\"Computing MLP group overlap F(g)...\\\")\\n    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, \\\"mlp_groups\\\")\\n    del mlp_acts\\n    torch.cuda.empty_cache()\\n\\n    os.makedirs(os.path.dirname(args.output_path) or \\\".\\\", exist_ok=True)\\n    result = {\\n        \\\"attn_overlap\\\": attn_overlap,\\n        \\\"mlp_overlap\\\": mlp_overlap,\\n        \\\"attn_cka_matrix\\\": attn_cka_matrix,\\n        \\\"mlp_cka_matrix\\\": mlp_cka_matrix,\\n    }\\n    torch.save(result, args.output_path)\\n    logger.info(f\\\"Saved CKA overlap scores to {args.output_path}\\\")\\n\\n    for layer_idx in sorted(attn_overlap.keys()):\\n        a = attn_overlap[layer_idx]\\n        logger.info(f\\\"  Layer {layer_idx}: attn GQA groups shape={a.shape}, \\\"\\n                     f\\\"range=[{a.min():.4f}, {a.max():.4f}]\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"
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
Good. cka_overlap.py is complete. Key findings:
- `mlp_cka_matrix` already exists in output
- MLP groups use `gate_proj` activation, grouped by `group_size = intermediate_size // n_groups` (default 28 groups)
- Output format: `{'attn_overlap': ..., 'mlp_overlap': ..., 'attn_cka_matrix': ..., 'mlp_cka_matrix': ...}`

Now let me read correlation_analysis.py and prune.py.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "156bb7e4-8ab9-4922-bff6-513f3dcaf208",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MfqtcVcrejybEJBXft86L4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2150,
      "cache_read_input_tokens": 34166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2150
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

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TmqiekDPxDkt3zCwsNNNY8`</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/recovery_aware_struct_prune/src/correlation_analysis.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "f745ee53-d6b7-46eb-b12a-07676c7fddf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MfqtcVcrejybEJBXft86L4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2150,
      "cache_read_input_tokens": 34166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2150
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

_source line 33 · 2026-05-14T05:29:05.972Z_

<details><summary>↩ Tool result · `toolu_01TmqiekDPxDkt3zCwsNNNY8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\\n\\nTests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more\\neffectively compensated by RLVR through their most similar retained head.\\n\\nMetric: for each pruned head h_p, find the most CKA-similar retained head h_r,\\nthen measure h_r's activation shift between pruned model and RLVR-recovered model.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport scipy.stats as stats\\nimport torch\\nimport torch.nn.functional as F\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\\n    \\\"\\\"\\\"Load a structurally pruned model by reconstructing from base model + saved weights.\\\"\\\"\\\"\\n    logging.getLogger(\\\"prune\\\").setLevel(logging.WARNING)\\n    from prune import prune_attention_heads, prune_mlp_channels\\n\\n    model = AutoModelForCausalLM.from_pretrained(\\n        base_model_path, torch_dtype=torch_dtype, device_map=\\\"cpu\\\", trust_remote_code=True\\n    )\\n    prune_attention_heads(model, pruning_meta[\\\"attn_keep_masks\\\"])\\n    prune_mlp_channels(model, pruning_meta[\\\"mlp_keep_masks\\\"])\\n\\n    safetensor_files = sorted(\\n        [f for f in os.listdir(saved_model_path) if f.endswith(\\\".safetensors\\\")]\\n    )\\n    if safetensor_files:\\n        from safetensors.torch import load_file\\n        state_dict = {}\\n        for f in safetensor_files:\\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\\n    else:\\n        state_dict = torch.load(\\n            os.path.join(saved_model_path, \\\"pytorch_model.bin\\\"),\\n            map_location=\\\"cpu\\\", weights_only=True,\\n        )\\n\\n    model.load_state_dict(state_dict)\\n    model.to(device)\\n    return model\\n\\n\\ndef collect_retained_head_activations(model, calibration_data, keep_masks, device):\\n    \\\"\\\"\\\"Collect per-head q_proj activations (mean-pooled over seq_len).\\n\\n    Returns dict[layer_idx] -> tensor[n_samples, n_retained_heads, head_dim]\\n    \\\"\\\"\\\"\\n    n_layers = model.config.num_hidden_layers\\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\\n\\n    q_outputs = {i: [] for i in range(n_layers)}\\n    hooks = []\\n\\n    def make_hook(layer_idx):\\n        def fn(module, inp, out):\\n            q_outputs[layer_idx].append(out.detach().cpu())\\n        return fn\\n\\n    for i in range(n_layers):\\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\\n        hooks.append(h)\\n\\n    model.eval()\\n    with torch.no_grad():\\n        for idx, enc in enumerate(calibration_data):\\n            input_ids = enc[\\\"input_ids\\\"].to(device)\\n            attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\n            if (idx + 1) % 50 == 0:\\n                logger.info(f\\\"  Processed {idx + 1}/{len(calibration_data)} samples\\\")\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    activations = {}\\n    for layer_idx in range(n_layers):\\n        n_retained = len(keep_masks[layer_idx])\\n        per_head = []\\n        for t in q_outputs[layer_idx]:\\n            t = t.squeeze(0)  # [seq, n_retained * head_dim]\\n            t = t\\n\\n... [截断: 输出过长，省略 4617 字符] ...\\n\\n of calibration samples\\\")\\n    parser.add_argument(\\\"--output_dir\\\", default=\\\"results/analysis/\\\",\\n                        help=\\\"Output directory\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42)\\n    parser.add_argument(\\\"--dtype\\\", type=str, default=\\\"bfloat16\\\",\\n                        choices=[\\\"float16\\\", \\\"bfloat16\\\", \\\"float32\\\"])\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(\\\"cuda\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    torch_dtype = {\\\"float16\\\": torch.float16, \\\"bfloat16\\\": torch.bfloat16,\\n                   \\\"float32\\\": torch.float32}[args.dtype]\\n\\n    logger.info(\\\"Loading CKA scores...\\\")\\n    cka_data = torch.load(args.cka_scores_path, map_location=\\\"cpu\\\", weights_only=True)\\n    if \\\"attn_cka_matrix\\\" not in cka_data:\\n        raise ValueError(\\n            \\\"CKA scores missing 'attn_cka_matrix'. \\\"\\n            \\\"Re-run cka_overlap.py to generate pairwise CKA matrices.\\\"\\n        )\\n\\n    logger.info(\\\"Loading pruning metadata...\\\")\\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\\\"cpu\\\",\\n                              weights_only=True)\\n    keep_masks = pruning_meta[\\\"attn_keep_masks\\\"]\\n\\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\\n    logger.info(f\\\"Loaded {len(calibration_data)} calibration samples\\\")\\n\\n    logger.info(f\\\"Loading pruned model from {args.pruned_model_path}\\\")\\n    pruned_model = load_pruned_model(\\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\\n    )\\n    logger.info(\\\"Collecting activations from pruned model...\\\")\\n    pruned_acts = collect_retained_head_activations(\\n        pruned_model, calibration_data, keep_masks, device\\n    )\\n    del pruned_model\\n    torch.cuda.empty_cache()\\n\\n    logger.info(f\\\"Loading recovered model from {args.recovered_model_path}\\\")\\n    recovered_model = load_pruned_model(\\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\\n    )\\n    logger.info(\\\"Collecting activations from recovered model...\\\")\\n    recovered_acts = collect_retained_head_activations(\\n        recovered_model, calibration_data, keep_masks, device\\n    )\\n    del recovered_model\\n    torch.cuda.empty_cache()\\n\\n    logger.info(\\\"Computing recoverability scores...\\\")\\n    n_heads = 28\\n    results = compute_recoverability(\\n        pruned_acts, recovered_acts, cka_data, keep_masks, n_heads\\n    )\\n    del pruned_acts, recovered_acts\\n    logger.info(f\\\"Computed recoverability for {len(results)} pruned heads\\\")\\n\\n    fh = [r[\\\"cka_overlap\\\"] for r in results]\\n    rec = [r[\\\"recoverability\\\"] for r in results]\\n    rho, p_value = stats.spearmanr(fh, rec)\\n    ci = bootstrap_spearman(fh, rec, seed=args.seed)\\n    perm_p = permutation_test(fh, rec, seed=args.seed)\\n\\n    verdict = \\\"PASS\\\" if rho >= 0.4 else (\\\"WARNING\\\" if rho >= 0.3 else \\\"FAIL\\\")\\n\\n    os.makedirs(args.output_dir, exist_ok=True)\\n    output = {\\n        \\\"spearman_rho\\\": rho,\\n        \\\"p_value\\\": p_value,\\n        \\\"bootstrap_ci_95\\\": ci,\\n        \\\"permutation_p_value\\\": perm_p,\\n        \\\"n_pruned_heads\\\": len(results),\\n        \\\"mvp_verdict\\\": verdict,\\n        \\\"per_head_data\\\": results,\\n    }\\n    json_path = os.path.join(args.output_dir, \\\"correlation_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2)\\n    logger.info(f\\\"Results saved to {json_path}\\\")\\n\\n    plot_path = os.path.join(args.output_dir, \\\"fh_vs_recoverability.png\\\")\\n    make_scatter_plot(results, rho, p_value, ci, perm_p, plot_path)\\n\\n    print(f\\\"\\\\n{'='*50}\\\")\\n    print(\\\"MVP Correlation Analysis Results\\\")\\n    print(f\\\"{'='*50}\\\")\\n    print(f\\\"Spearman rho:      {rho:.4f}\\\")\\n    print(f\\\"p-value:           {p_value:.2e}\\\")\\n    print(f\\\"95% CI:            [{ci[0]:.4f}, {ci[1]:.4f}]\\\")\\n    print(f\\\"Permutation p:     {perm_p:.4f}\\\")\\n    print(f\\\"N pruned heads:    {len(results)}\\\")\\n    print(f\\\"MVP Verdict:       {verdict}\\\")\\n    print(f\\\"{'='*50}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "638f5379-a4e0-45bc-906c-acbf09e894ee",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\\\\n\\\\nTests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more\\\\neffectively compensated by RLVR through their most similar retained head.\\\\n\\\\nMetric: for each pruned head h_p, find the most CKA-similar retained head h_r,\\\\nthen measure h_r's activation shift between pruned model and RLVR-recovered model.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport random\\\\n\\\\nimport numpy as np\\\\nimport scipy.stats as stats\\\\nimport torch\\\\nimport torch.nn.functional as F\\\\nfrom datasets import load_dataset\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n)\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n\\\\ndef set_seed(seed: int):\\\\n    random.seed(seed)\\\\n    np.random.seed(seed)\\\\n    torch.manual_seed(seed)\\\\n    torch.cuda.manual_seed_all(seed)\\\\n\\\\n\\\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\\\n    ds = load_dataset(\\\\\\\"openai/gsm8k\\\\\\\", \\\\\\\"main\\\\\\\", split=\\\\\\\"train\\\\\\\")\\\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\\\n    encodings = []\\\\n    for example in ds:\\\\n        prompt = f\\\\\\\"Question: {example['question']}\\\\\\\\nAnswer: Let me think step by step.\\\\\\\\n\\\\\\\"\\\\n        ids = tokenizer(prompt, return_tensors=\\\\\\\"pt\\\\\\\", truncation=True, max_length=max_length)\\\\n        encodings.append(ids)\\\\n    return encodings\\\\n\\\\n\\\\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load a structurally pruned model by reconstructing from base model + saved weights.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    logging.getLogger(\\\\\\\"prune\\\\\\\").setLevel(logging.WARNING)\\\\n    from prune import prune_attention_heads, prune_mlp_channels\\\\n\\\\n    model = AutoModelForCausalLM.from_pretrained(\\\\n        base_model_path, torch_dtype=torch_dtype, device_map=\\\\\\\"cpu\\\\\\\", trust_remote_code=True\\\\n    )\\\\n    prune_attention_heads(model, pruning_meta[\\\\\\\"attn_keep_masks\\\\\\\"])\\\\n    prune_mlp_channels(model, pruning_meta[\\\\\\\"mlp_keep_masks\\\\\\\"])\\\\n\\\\n    safetensor_files = sorted(\\\\n        [f for f in os.listdir(saved_model_path) if f.endswith(\\\\\\\".safetensors\\\\\\\")]\\\\n    )\\\\n    if safetensor_files:\\\\n        from safetensors.torch import load_file\\\\n        state_dict = {}\\\\n        for f in safetensor_files:\\\\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\\\\n    else:\\\\n        state_dict = torch.load(\\\\n            os.path.join(saved_model_path, \\\\\\\"pytorch_model.bin\\\\\\\"),\\\\n            map_location=\\\\\\\"cpu\\\\\\\", weights_only=True,\\\\n        )\\\\n\\\\n    model.load_state_dict(state_dict)\\\\n    model.to(device)\\\\n    return model\\\\n\\\\n\\\\ndef collect_retained_head_activations(model, calibration_data, keep_masks, device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Collect per-head q_proj activations (mean-pooled over seq_len).\\\\n\\\\n    Returns dict[layer_idx] -> tensor[n_samples, n_retained_heads, head_dim]\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    n_layers = model.config.num_hidden_layers\\\\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\\\\n\\\\n    q_outputs = {i: [] for i in range(n_layers)}\\\\n    hooks = []\\\\n\\\\n    def make_hook(layer_idx):\\\\n        def fn(module, inp, out):\\\\n            q_outputs[layer_idx].append(out.detach().cpu())\\\\n        return fn\\\\n\\\\n    for i in range(n_layers):\\\\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\\\\n        hooks.append(h)\\\\n\\\\n    model.eval()\\\\n    with torch.no_grad():\\\\n        for idx, enc in enumerate(calibration_data):\\\\n            input_ids = enc[\\\\\\\"input_ids\\\\\\\"].to(device)\\\\n            attention_mask = enc[\\\\\\\"attention_mask\\\\\\\"].to(device)\\\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\\\n            if (idx + 1) % 50 == 0:\\\\n                logger.info(f\\\\\\\"  Processed {idx + 1}/{len(calibration_data)} samples\\\\\\\")\\\\n\\\\n    for h in hooks:\\\\n        h.remove()\\\\n\\\\n    activations = {}\\\\n    for layer_idx in range(n_layers):\\\\n        n_retained = len(keep_masks[layer_idx])\\\\n        per_head = []\\\\n        for t in q_outputs[layer_idx]:\\\\n            t = t.squeeze(0)  # [seq, n_retained * head_dim]\\\\n            t = t\\\\n\\\\n... [截断: 输出过长，省略 4617 字符] ...\\\\n\\\\n of calibration samples\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output_dir\\\\\\\", default=\\\\\\\"results/analysis/\\\\\\\",\\\\n                        help=\\\\\\\"Output directory\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    parser.add_argument(\\\\\\\"--dtype\\\\\\\", type=str, default=\\\\\\\"bfloat16\\\\\\\",\\\\n                        choices=[\\\\\\\"float16\\\\\\\", \\\\\\\"bfloat16\\\\\\\", \\\\\\\"float32\\\\\\\"])\\\\n    args = parser.parse_args()\\\\n\\\\n    set_seed(args.seed)\\\\n    device = torch.device(\\\\\\\"cuda\\\\\\\" if torch.cuda.is_available() else \\\\\\\"cpu\\\\\\\")\\\\n    torch_dtype = {\\\\\\\"float16\\\\\\\": torch.float16, \\\\\\\"bfloat16\\\\\\\": torch.bfloat16,\\\\n                   \\\\\\\"float32\\\\\\\": torch.float32}[args.dtype]\\\\n\\\\n    logger.info(\\\\\\\"Loading CKA scores...\\\\\\\")\\\\n    cka_data = torch.load(args.cka_scores_path, map_location=\\\\\\\"cpu\\\\\\\", weights_only=True)\\\\n    if \\\\\\\"attn_cka_matrix\\\\\\\" not in cka_data:\\\\n        raise ValueError(\\\\n            \\\\\\\"CKA scores missing 'attn_cka_matrix'. \\\\\\\"\\\\n            \\\\\\\"Re-run cka_overlap.py to generate pairwise CKA matrices.\\\\\\\"\\\\n        )\\\\n\\\\n    logger.info(\\\\\\\"Loading pruning metadata...\\\\\\\")\\\\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\\\\\\\"cpu\\\\\\\",\\\\n                              weights_only=True)\\\\n    keep_masks = pruning_meta[\\\\\\\"attn_keep_masks\\\\\\\"]\\\\n\\\\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\\\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\\\\n    logger.info(f\\\\\\\"Loaded {len(calibration_data)} calibration samples\\\\\\\")\\\\n\\\\n    logger.info(f\\\\\\\"Loading pruned model from {args.pruned_model_path}\\\\\\\")\\\\n    pruned_model = load_pruned_model(\\\\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\\\\n    )\\\\n    logger.info(\\\\\\\"Collecting activations from pruned model...\\\\\\\")\\\\n    pruned_acts = collect_retained_head_activations(\\\\n        pruned_model, calibration_data, keep_masks, device\\\\n    )\\\\n    del pruned_model\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    logger.info(f\\\\\\\"Loading recovered model from {args.recovered_model_path}\\\\\\\")\\\\n    recovered_model = load_pruned_model(\\\\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\\\\n    )\\\\n    logger.info(\\\\\\\"Collecting activations from recovered model...\\\\\\\")\\\\n    recovered_acts = collect_retained_head_activations(\\\\n        recovered_model, calibration_data, keep_masks, device\\\\n    )\\\\n    del recovered_model\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    logger.info(\\\\\\\"Computing recoverability scores...\\\\\\\")\\\\n    n_heads = 28\\\\n    results = compute_recoverability(\\\\n        pruned_acts, recovered_acts, cka_data, keep_masks, n_heads\\\\n    )\\\\n    del pruned_acts, recovered_acts\\\\n    logger.info(f\\\\\\\"Computed recoverability for {len(results)} pruned heads\\\\\\\")\\\\n\\\\n    fh = [r[\\\\\\\"cka_overlap\\\\\\\"] for r in results]\\\\n    rec = [r[\\\\\\\"recoverability\\\\\\\"] for r in results]\\\\n    rho, p_value = stats.spearmanr(fh, rec)\\\\n    ci = bootstrap_spearman(fh, rec, seed=args.seed)\\\\n    perm_p = permutation_test(fh, rec, seed=args.seed)\\\\n\\\\n    verdict = \\\\\\\"PASS\\\\\\\" if rho >= 0.4 else (\\\\\\\"WARNING\\\\\\\" if rho >= 0.3 else \\\\\\\"FAIL\\\\\\\")\\\\n\\\\n    os.makedirs(args.output_dir, exist_ok=True)\\\\n    output = {\\\\n        \\\\\\\"spearman_rho\\\\\\\": rho,\\\\n        \\\\\\\"p_value\\\\\\\": p_value,\\\\n        \\\\\\\"bootstrap_ci_95\\\\\\\": ci,\\\\n        \\\\\\\"permutation_p_value\\\\\\\": perm_p,\\\\n        \\\\\\\"n_pruned_heads\\\\\\\": len(results),\\\\n        \\\\\\\"mvp_verdict\\\\\\\": verdict,\\\\n        \\\\\\\"per_head_data\\\\\\\": results,\\\\n    }\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"correlation_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(output, f, indent=2)\\\\n    logger.info(f\\\\\\\"Results saved to {json_path}\\\\\\\")\\\\n\\\\n    plot_path = os.path.join(args.output_dir, \\\\\\\"fh_vs_recoverability.png\\\\\\\")\\\\n    make_scatter_plot(results, rho, p_value, ci, perm_p, plot_path)\\\\n\\\\n    print(f\\\\\\\"\\\\\\\\n{'='*50}\\\\\\\")\\\\n    print(\\\\\\\"MVP Correlation Analysis Results\\\\\\\")\\\\n    print(f\\\\\\\"{'='*50}\\\\\\\")\\\\n    print(f\\\\\\\"Spearman rho:      {rho:.4f}\\\\\\\")\\\\n    print(f\\\\\\\"p-value:           {p_value:.2e}\\\\\\\")\\\\n    print(f\\\\\\\"95% CI:            [{ci[0]:.4f}, {ci[1]:.4f}]\\\\\\\")\\\\n    print(f\\\\\\\"Permutation p:     {perm_p:.4f}\\\\\\\")\\\\n    print(f\\\\\\\"N pruned heads:    {len(results)}\\\\\\\")\\\\n    print(f\\\\\\\"MVP Verdict:       {verdict}\\\\\\\")\\\\n    print(f\\\\\\\"{'='*50}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\\n\\nTests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more\\neffectively compensated by RLVR through their most similar retained head.\\n\\nMetric: for each pruned head h_p, find the most CKA-similar retained head h_r,\\nthen measure h_r's activation shift between pruned model and RLVR-recovered model.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport scipy.stats as stats\\nimport torch\\nimport torch.nn.functional as F\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\\n    \\\"\\\"\\\"Load a structurally pruned model by reconstructing from base model + saved weights.\\\"\\\"\\\"\\n    logging.getLogger(\\\"prune\\\").setLevel(logging.WARNING)\\n    from prune import prune_attention_heads, prune_mlp_channels\\n\\n    model = AutoModelForCausalLM.from_pretrained(\\n        base_model_path, torch_dtype=torch_dtype, device_map=\\\"cpu\\\", trust_remote_code=True\\n    )\\n    prune_attention_heads(model, pruning_meta[\\\"attn_keep_masks\\\"])\\n    prune_mlp_channels(model, pruning_meta[\\\"mlp_keep_masks\\\"])\\n\\n    safetensor_files = sorted(\\n        [f for f in os.listdir(saved_model_path) if f.endswith(\\\".safetensors\\\")]\\n    )\\n    if safetensor_files:\\n        from safetensors.torch import load_file\\n        state_dict = {}\\n        for f in safetensor_files:\\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\\n    else:\\n        state_dict = torch.load(\\n            os.path.join(saved_model_path, \\\"pytorch_model.bin\\\"),\\n            map_location=\\\"cpu\\\", weights_only=True,\\n        )\\n\\n    model.load_state_dict(state_dict)\\n    model.to(device)\\n    return model\\n\\n\\ndef collect_retained_head_activations(model, calibration_data, keep_masks, device):\\n    \\\"\\\"\\\"Collect per-head q_proj activations (mean-pooled over seq_len).\\n\\n    Returns dict[layer_idx] -> tensor[n_samples, n_retained_heads, head_dim]\\n    \\\"\\\"\\\"\\n    n_layers = model.config.num_hidden_layers\\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\\n\\n    q_outputs = {i: [] for i in range(n_layers)}\\n    hooks = []\\n\\n    def make_hook(layer_idx):\\n        def fn(module, inp, out):\\n            q_outputs[layer_idx].append(out.detach().cpu())\\n        return fn\\n\\n    for i in range(n_layers):\\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\\n        hooks.append(h)\\n\\n    model.eval()\\n    with torch.no_grad():\\n        for idx, enc in enumerate(calibration_data):\\n            input_ids = enc[\\\"input_ids\\\"].to(device)\\n            attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\n            if (idx + 1) % 50 == 0:\\n                logger.info(f\\\"  Processed {idx + 1}/{len(calibration_data)} samples\\\")\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    activations = {}\\n    for layer_idx in range(n_layers):\\n        n_retained = len(keep_masks[layer_idx])\\n        per_head = []\\n        for t in q_outputs[layer_idx]:\\n            t = t.squeeze(0)  # [seq, n_retained * head_dim]\\n            t = t\\n\\n... [截断: 输出过长，省略 4617 字符] ...\\n\\n of calibration samples\\\")\\n    parser.add_argument(\\\"--output_dir\\\", default=\\\"results/analysis/\\\",\\n                        help=\\\"Output directory\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42)\\n    parser.add_argument(\\\"--dtype\\\", type=str, default=\\\"bfloat16\\\",\\n                        choices=[\\\"float16\\\", \\\"bfloat16\\\", \\\"float32\\\"])\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(\\\"cuda\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    torch_dtype = {\\\"float16\\\": torch.float16, \\\"bfloat16\\\": torch.bfloat16,\\n                   \\\"float32\\\": torch.float32}[args.dtype]\\n\\n    logger.info(\\\"Loading CKA scores...\\\")\\n    cka_data = torch.load(args.cka_scores_path, map_location=\\\"cpu\\\", weights_only=True)\\n    if \\\"attn_cka_matrix\\\" not in cka_data:\\n        raise ValueError(\\n            \\\"CKA scores missing 'attn_cka_matrix'. \\\"\\n            \\\"Re-run cka_overlap.py to generate pairwise CKA matrices.\\\"\\n        )\\n\\n    logger.info(\\\"Loading pruning metadata...\\\")\\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\\\"cpu\\\",\\n                              weights_only=True)\\n    keep_masks = pruning_meta[\\\"attn_keep_masks\\\"]\\n\\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\\n    logger.info(f\\\"Loaded {len(calibration_data)} calibration samples\\\")\\n\\n    logger.info(f\\\"Loading pruned model from {args.pruned_model_path}\\\")\\n    pruned_model = load_pruned_model(\\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\\n    )\\n    logger.info(\\\"Collecting activations from pruned model...\\\")\\n    pruned_acts = collect_retained_head_activations(\\n        pruned_model, calibration_data, keep_masks, device\\n    )\\n    del pruned_model\\n    torch.cuda.empty_cache()\\n\\n    logger.info(f\\\"Loading recovered model from {args.recovered_model_path}\\\")\\n    recovered_model = load_pruned_model(\\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\\n    )\\n    logger.info(\\\"Collecting activations from recovered model...\\\")\\n    recovered_acts = collect_retained_head_activations(\\n        recovered_model, calibration_data, keep_masks, device\\n    )\\n    del recovered_model\\n    torch.cuda.empty_cache()\\n\\n    logger.info(\\\"Computing recoverability scores...\\\")\\n    n_heads = 28\\n    results = compute_recoverability(\\n        pruned_acts, recovered_acts, cka_data, keep_masks, n_heads\\n    )\\n    del pruned_acts, recovered_acts\\n    logger.info(f\\\"Computed recoverability for {len(results)} pruned heads\\\")\\n\\n    fh = [r[\\\"cka_overlap\\\"] for r in results]\\n    rec = [r[\\\"recoverability\\\"] for r in results]\\n    rho, p_value = stats.spearmanr(fh, rec)\\n    ci = bootstrap_spearman(fh, rec, seed=args.seed)\\n    perm_p = permutation_test(fh, rec, seed=args.seed)\\n\\n    verdict = \\\"PASS\\\" if rho >= 0.4 else (\\\"WARNING\\\" if rho >= 0.3 else \\\"FAIL\\\")\\n\\n    os.makedirs(args.output_dir, exist_ok=True)\\n    output = {\\n        \\\"spearman_rho\\\": rho,\\n        \\\"p_value\\\": p_value,\\n        \\\"bootstrap_ci_95\\\": ci,\\n        \\\"permutation_p_value\\\": perm_p,\\n        \\\"n_pruned_heads\\\": len(results),\\n        \\\"mvp_verdict\\\": verdict,\\n        \\\"per_head_data\\\": results,\\n    }\\n    json_path = os.path.join(args.output_dir, \\\"correlation_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2)\\n    logger.info(f\\\"Results saved to {json_path}\\\")\\n\\n    plot_path = os.path.join(args.output_dir, \\\"fh_vs_recoverability.png\\\")\\n    make_scatter_plot(results, rho, p_value, ci, perm_p, plot_path)\\n\\n    print(f\\\"\\\\n{'='*50}\\\")\\n    print(\\\"MVP Correlation Analysis Results\\\")\\n    print(f\\\"{'='*50}\\\")\\n    print(f\\\"Spearman rho:      {rho:.4f}\\\")\\n    print(f\\\"p-value:           {p_value:.2e}\\\")\\n    print(f\\\"95% CI:            [{ci[0]:.4f}, {ci[1]:.4f}]\\\")\\n    print(f\\\"Permutation p:     {perm_p:.4f}\\\")\\n    print(f\\\"N pruned heads:    {len(results)}\\\")\\n    print(f\\\"MVP Verdict:       {verdict}\\\")\\n    print(f\\\"{'='*50}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
The output was truncated. I need to see the middle portion of correlation_analysis.py. Let me also read prune.py. Let me get the parts I'm missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "965bce76-f85c-4841-a0f9-4f0111cd1eae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNY8K8wKoawPu5pnTdyLwF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3558,
      "cache_read_input_tokens": 36316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3558
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

_source line 35_

需要看 correlation_analysis.py 被截断的中间部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "c94c7eb3-c78e-47a6-ad83-6126c5f3e38a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNY8K8wKoawPu5pnTdyLwF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3558,
      "cache_read_input_tokens": 36316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3558
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

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017DwXMEDmvNoUZnJwysP2Ui`</summary>

```json
{
  "server": "westb-23072",
  "command": "head -230 /root/recovery_aware_struct_prune/src/correlation_analysis.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "27bd396a-53fe-4aaf-abfd-c21b12355a41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNY8K8wKoawPu5pnTdyLwF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3558,
      "cache_read_input_tokens": 36316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3558
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

_source line 37 · 2026-05-14T05:29:11.657Z_

<details><summary>↩ Tool result · `toolu_017DwXMEDmvNoUZnJwysP2Ui`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\\n\\nTests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more\\neffectively compensated by RLVR through their most similar retained head.\\n\\nMetric: for each pruned head h_p, find the most CKA-similar retained head h_r,\\nthen measure h_r's activation shift between pruned model and RLVR-recovered model.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport scipy.stats as stats\\nimport torch\\nimport torch.nn.functional as F\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\\n    \\\"\\\"\\\"Load a structurally pruned model by reconstructing from base model + saved weights.\\\"\\\"\\\"\\n    logging.getLogger(\\\"prune\\\").setLevel(logging.WARNING)\\n    from prune import prune_attention_heads, prune_mlp_channels\\n\\n    model = AutoModelForCausalLM.from_pretrained(\\n        base_model_path, torch_dtype=torch_dtype, device_map=\\\"cpu\\\", trust_remote_code=True\\n    )\\n    prune_attention_heads(model, pruning_meta[\\\"attn_keep_masks\\\"])\\n    prune_mlp_channels(model, pruning_meta[\\\"mlp_keep_masks\\\"])\\n\\n    safetensor_files = sorted(\\n        [f for f in os.listdir(saved_model_path) if f.endswith(\\\".safetensors\\\")]\\n    )\\n    if safetensor_files:\\n        from safetensors.torch import load_file\\n        state_dict = {}\\n        for f in safetensor_files:\\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\\n    else:\\n        state_dict = torch.load(\\n            os.path.join(saved_model_path, \\\"pytorch_model.bin\\\"),\\n            map_location=\\\"cpu\\\", weights_only=True,\\n        )\\n\\n    model.load_state_dict(state_dict)\\n    model.to(device)\\n    return model\\n\\n\\ndef collect_retained_head_activations(model, calibration_data, keep_masks, device):\\n    \\\"\\\"\\\"Collect per-head q_proj activations (mean-pooled over seq_len).\\n\\n    Returns dict[layer_idx] -> tensor[n_samples, n_retained_heads, head_dim]\\n    \\\"\\\"\\\"\\n    n_layers = model.config.num_hidden_layers\\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\\n\\n    q_outputs = {i: [] for i in range(n_layers)}\\n    hooks = []\\n\\n    def make_hook(layer_idx):\\n        def fn(module, inp, out):\\n            q_outputs[layer_idx].append(out.detach().cpu())\\n        return fn\\n\\n    for i in range(n_layers):\\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\\n        hooks.append(h)\\n\\n    model.eval()\\n    with torch.no_grad():\\n        for idx, enc in enumerate(calibration_data):\\n            input_ids = enc[\\\"input_ids\\\"].to(device)\\n            attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\n            if (idx + 1) % 50 == 0:\\n                logger.info(f\\\"  Processed {idx + 1}/{len(calibration_data)} samples\\\")\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    activations = {}\\n    for layer_idx in range(n_layers):\\n        n_retained = len(keep_masks[layer_idx])\\n        per_head = []\\n        for t in q_outputs[layer_idx]:\\n            t = t.squeeze(0)  # [seq, n_retained * head_dim]\\n            t = t\\n\\n... [截断: 输出过长，省略 208 字符] ...\\n\\nead, dim=0).float()\\n        q_outputs[layer_idx] = None\\n\\n    return activations\\n\\n\\ndef compute_recoverability(pruned_acts, recovered_acts, cka_data, keep_masks,\\n                           n_heads_original=28):\\n    \\\"\\\"\\\"Compute per-pruned-head recoverability as activation shift of best retained head.\\\"\\\"\\\"\\n    attn_overlap = cka_data[\\\"attn_overlap\\\"]\\n    attn_cka_matrix = cka_data[\\\"attn_cka_matrix\\\"]\\n    results = []\\n\\n    for layer_idx in range(len(keep_masks)):\\n        retained = keep_masks[layer_idx]\\n        pruned_heads = sorted(set(range(n_heads_original)) - set(retained))\\n        if not pruned_heads:\\n            continue\\n\\n        cka_matrix = attn_cka_matrix[layer_idx]\\n\\n        for h_p in pruned_heads:\\n            sims = torch.tensor([cka_matrix[h_p, h_r].item() for h_r in retained])\\n            best_idx = sims.argmax().item()\\n            h_r = retained[best_idx]\\n            h_r_local = retained.index(h_r)\\n\\n            act_p = pruned_acts[layer_idx][:, h_r_local, :]\\n            act_r = recovered_acts[layer_idx][:, h_r_local, :]\\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\\n            activation_shift = 1.0 - cos_sim.mean().item()\\n\\n            results.append({\\n                \\\"layer\\\": layer_idx,\\n                \\\"pruned_head\\\": h_p,\\n                \\\"best_retained_head\\\": h_r,\\n                \\\"cka_overlap\\\": attn_overlap[layer_idx][h_p].item(),\\n                \\\"recoverability\\\": activation_shift,\\n                \\\"cka_similarity_to_retained\\\": sims[best_idx].item(),\\n            })\\n\\n    return results\\n\\n\\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    x, y = np.array(x), np.array(y)\\n    n = len(x)\\n    rhos = []\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        r, _ = stats.spearmanr(x[idx], y[idx])\\n        if not np.isnan(r):\\n            rhos.append(r)\\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\\n\\n\\ndef permutation_test(x, y, n_perm=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    x, y = np.array(x), np.array(y)\\n    observed, _ = stats.spearmanr(x, y)\\n    count = 0\\n    for _ in range(n_perm):\\n        r, _ = stats.spearmanr(x, rng.permutation(y))\\n        if abs(r) >= abs(observed):\\n            count += 1\\n    return count / n_perm\\n\\n\\ndef make_scatter_plot(results, rho, p_value, ci, perm_p, output_path):\\n    try:\\n        import matplotlib\\n        matplotlib.use(\\\"Agg\\\")\\n        import matplotlib.pyplot as plt\\n    except ImportError:\\n        logger.warning(\\\"matplotlib not available, skipping scatter plot\\\")\\n        return\\n\\n    fh = [r[\\\"cka_overlap\\\"] for r in results]\\n    rec = [r[\\\"recoverability\\\"] for r in results]\\n    layers = [r[\\\"layer\\\"] for r in results]\\n\\n    fig, ax = plt.subplots(figsize=(8, 6))\\n    sc = ax.scatter(fh, rec, c=layers, cmap=\\\"viridis\\\", alpha=0.7,\\n                    edgecolors=\\\"k\\\", linewidths=0.3, s=30)\\n    plt.colorbar(sc, ax=ax, label=\\\"Layer index\\\")\\n    ax.set_xlabel(\\\"F(h_p) — CKA overlap of pruned head\\\")\\n    ax.set_ylabel(\\\"Recoverability — activation shift of best retained head\\\")\\n\\n    verdict = \\\"PASS\\\" if rho >= 0.4 else (\\\"WARNING\\\" if rho >= 0.3 else \\\"FAIL\\\")\\n    ax.set_title(\\n        f\\\"CKA Overlap vs RLVR Recoverability\\\\n\\\"\\n        f\\\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \\\"\\n        f\\\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\\\"\\n    )\\n    plt.tight_layout()\\n    plt.savefig(output_path, dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n    logger.info(f\\\"Scatter plot saved to {output_path}\\\")\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Correlation analysis: rho(CKA overlap, RLVR recoverability)\\\"\\n    )\\n    parser.add_argument(\\\"--base_model_path\\\", required=True,\\n                        help=\\\"Path to original unpruned model\\\")\\n    parser.add_argument(\\\"--pruned_model_path\\\", required=True,\\n                        help=\\\"Path to pruned model (before RLVR)\\\")\\n    parser.add_argument(\\\"--recovered_model_path\\\", required=True,\\n                        help=\\\"Path to RLVR-recovered model\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "b33188be-8458-481d-aa7c-45d5ed9c094e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\\\\n\\\\nTests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more\\\\neffectively compensated by RLVR through their most similar retained head.\\\\n\\\\nMetric: for each pruned head h_p, find the most CKA-similar retained head h_r,\\\\nthen measure h_r's activation shift between pruned model and RLVR-recovered model.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport random\\\\n\\\\nimport numpy as np\\\\nimport scipy.stats as stats\\\\nimport torch\\\\nimport torch.nn.functional as F\\\\nfrom datasets import load_dataset\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n)\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n\\\\ndef set_seed(seed: int):\\\\n    random.seed(seed)\\\\n    np.random.seed(seed)\\\\n    torch.manual_seed(seed)\\\\n    torch.cuda.manual_seed_all(seed)\\\\n\\\\n\\\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\\\n    ds = load_dataset(\\\\\\\"openai/gsm8k\\\\\\\", \\\\\\\"main\\\\\\\", split=\\\\\\\"train\\\\\\\")\\\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\\\n    encodings = []\\\\n    for example in ds:\\\\n        prompt = f\\\\\\\"Question: {example['question']}\\\\\\\\nAnswer: Let me think step by step.\\\\\\\\n\\\\\\\"\\\\n        ids = tokenizer(prompt, return_tensors=\\\\\\\"pt\\\\\\\", truncation=True, max_length=max_length)\\\\n        encodings.append(ids)\\\\n    return encodings\\\\n\\\\n\\\\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load a structurally pruned model by reconstructing from base model + saved weights.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    logging.getLogger(\\\\\\\"prune\\\\\\\").setLevel(logging.WARNING)\\\\n    from prune import prune_attention_heads, prune_mlp_channels\\\\n\\\\n    model = AutoModelForCausalLM.from_pretrained(\\\\n        base_model_path, torch_dtype=torch_dtype, device_map=\\\\\\\"cpu\\\\\\\", trust_remote_code=True\\\\n    )\\\\n    prune_attention_heads(model, pruning_meta[\\\\\\\"attn_keep_masks\\\\\\\"])\\\\n    prune_mlp_channels(model, pruning_meta[\\\\\\\"mlp_keep_masks\\\\\\\"])\\\\n\\\\n    safetensor_files = sorted(\\\\n        [f for f in os.listdir(saved_model_path) if f.endswith(\\\\\\\".safetensors\\\\\\\")]\\\\n    )\\\\n    if safetensor_files:\\\\n        from safetensors.torch import load_file\\\\n        state_dict = {}\\\\n        for f in safetensor_files:\\\\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\\\\n    else:\\\\n        state_dict = torch.load(\\\\n            os.path.join(saved_model_path, \\\\\\\"pytorch_model.bin\\\\\\\"),\\\\n            map_location=\\\\\\\"cpu\\\\\\\", weights_only=True,\\\\n        )\\\\n\\\\n    model.load_state_dict(state_dict)\\\\n    model.to(device)\\\\n    return model\\\\n\\\\n\\\\ndef collect_retained_head_activations(model, calibration_data, keep_masks, device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Collect per-head q_proj activations (mean-pooled over seq_len).\\\\n\\\\n    Returns dict[layer_idx] -> tensor[n_samples, n_retained_heads, head_dim]\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    n_layers = model.config.num_hidden_layers\\\\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\\\\n\\\\n    q_outputs = {i: [] for i in range(n_layers)}\\\\n    hooks = []\\\\n\\\\n    def make_hook(layer_idx):\\\\n        def fn(module, inp, out):\\\\n            q_outputs[layer_idx].append(out.detach().cpu())\\\\n        return fn\\\\n\\\\n    for i in range(n_layers):\\\\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\\\\n        hooks.append(h)\\\\n\\\\n    model.eval()\\\\n    with torch.no_grad():\\\\n        for idx, enc in enumerate(calibration_data):\\\\n            input_ids = enc[\\\\\\\"input_ids\\\\\\\"].to(device)\\\\n            attention_mask = enc[\\\\\\\"attention_mask\\\\\\\"].to(device)\\\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\\\n            if (idx + 1) % 50 == 0:\\\\n                logger.info(f\\\\\\\"  Processed {idx + 1}/{len(calibration_data)} samples\\\\\\\")\\\\n\\\\n    for h in hooks:\\\\n        h.remove()\\\\n\\\\n    activations = {}\\\\n    for layer_idx in range(n_layers):\\\\n        n_retained = len(keep_masks[layer_idx])\\\\n        per_head = []\\\\n        for t in q_outputs[layer_idx]:\\\\n            t = t.squeeze(0)  # [seq, n_retained * head_dim]\\\\n            t = t\\\\n\\\\n... [截断: 输出过长，省略 208 字符] ...\\\\n\\\\nead, dim=0).float()\\\\n        q_outputs[layer_idx] = None\\\\n\\\\n    return activations\\\\n\\\\n\\\\ndef compute_recoverability(pruned_acts, recovered_acts, cka_data, keep_masks,\\\\n                           n_heads_original=28):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute per-pruned-head recoverability as activation shift of best retained head.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    attn_overlap = cka_data[\\\\\\\"attn_overlap\\\\\\\"]\\\\n    attn_cka_matrix = cka_data[\\\\\\\"attn_cka_matrix\\\\\\\"]\\\\n    results = []\\\\n\\\\n    for layer_idx in range(len(keep_masks)):\\\\n        retained = keep_masks[layer_idx]\\\\n        pruned_heads = sorted(set(range(n_heads_original)) - set(retained))\\\\n        if not pruned_heads:\\\\n            continue\\\\n\\\\n        cka_matrix = attn_cka_matrix[layer_idx]\\\\n\\\\n        for h_p in pruned_heads:\\\\n            sims = torch.tensor([cka_matrix[h_p, h_r].item() for h_r in retained])\\\\n            best_idx = sims.argmax().item()\\\\n            h_r = retained[best_idx]\\\\n            h_r_local = retained.index(h_r)\\\\n\\\\n            act_p = pruned_acts[layer_idx][:, h_r_local, :]\\\\n            act_r = recovered_acts[layer_idx][:, h_r_local, :]\\\\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\\\\n            activation_shift = 1.0 - cos_sim.mean().item()\\\\n\\\\n            results.append({\\\\n                \\\\\\\"layer\\\\\\\": layer_idx,\\\\n                \\\\\\\"pruned_head\\\\\\\": h_p,\\\\n                \\\\\\\"best_retained_head\\\\\\\": h_r,\\\\n                \\\\\\\"cka_overlap\\\\\\\": attn_overlap[layer_idx][h_p].item(),\\\\n                \\\\\\\"recoverability\\\\\\\": activation_shift,\\\\n                \\\\\\\"cka_similarity_to_retained\\\\\\\": sims[best_idx].item(),\\\\n            })\\\\n\\\\n    return results\\\\n\\\\n\\\\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\\\\n    rng = np.random.RandomState(seed)\\\\n    x, y = np.array(x), np.array(y)\\\\n    n = len(x)\\\\n    rhos = []\\\\n    for _ in range(n_bootstrap):\\\\n        idx = rng.choice(n, n, replace=True)\\\\n        r, _ = stats.spearmanr(x[idx], y[idx])\\\\n        if not np.isnan(r):\\\\n            rhos.append(r)\\\\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\\\\n\\\\n\\\\ndef permutation_test(x, y, n_perm=10000, seed=42):\\\\n    rng = np.random.RandomState(seed)\\\\n    x, y = np.array(x), np.array(y)\\\\n    observed, _ = stats.spearmanr(x, y)\\\\n    count = 0\\\\n    for _ in range(n_perm):\\\\n        r, _ = stats.spearmanr(x, rng.permutation(y))\\\\n        if abs(r) >= abs(observed):\\\\n            count += 1\\\\n    return count / n_perm\\\\n\\\\n\\\\ndef make_scatter_plot(results, rho, p_value, ci, perm_p, output_path):\\\\n    try:\\\\n        import matplotlib\\\\n        matplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\n        import matplotlib.pyplot as plt\\\\n    except ImportError:\\\\n        logger.warning(\\\\\\\"matplotlib not available, skipping scatter plot\\\\\\\")\\\\n        return\\\\n\\\\n    fh = [r[\\\\\\\"cka_overlap\\\\\\\"] for r in results]\\\\n    rec = [r[\\\\\\\"recoverability\\\\\\\"] for r in results]\\\\n    layers = [r[\\\\\\\"layer\\\\\\\"] for r in results]\\\\n\\\\n    fig, ax = plt.subplots(figsize=(8, 6))\\\\n    sc = ax.scatter(fh, rec, c=layers, cmap=\\\\\\\"viridis\\\\\\\", alpha=0.7,\\\\n                    edgecolors=\\\\\\\"k\\\\\\\", linewidths=0.3, s=30)\\\\n    plt.colorbar(sc, ax=ax, label=\\\\\\\"Layer index\\\\\\\")\\\\n    ax.set_xlabel(\\\\\\\"F(h_p) — CKA overlap of pruned head\\\\\\\")\\\\n    ax.set_ylabel(\\\\\\\"Recoverability — activation shift of best retained head\\\\\\\")\\\\n\\\\n    verdict = \\\\\\\"PASS\\\\\\\" if rho >= 0.4 else (\\\\\\\"WARNING\\\\\\\" if rho >= 0.3 else \\\\\\\"FAIL\\\\\\\")\\\\n    ax.set_title(\\\\n        f\\\\\\\"CKA Overlap vs RLVR Recoverability\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \\\\\\\"\\\\n        f\\\\\\\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\\\\\\\"\\\\n    )\\\\n    plt.tight_layout()\\\\n    plt.savefig(output_path, dpi=150, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.close()\\\\n    logger.info(f\\\\\\\"Scatter plot saved to {output_path}\\\\\\\")\\\\n\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(\\\\n        description=\\\\\\\"Correlation analysis: rho(CKA overlap, RLVR recoverability)\\\\\\\"\\\\n    )\\\\n    parser.add_argument(\\\\\\\"--base_model_path\\\\\\\", required=True,\\\\n                        help=\\\\\\\"Path to original unpruned model\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--pruned_model_path\\\\\\\", required=True,\\\\n                        help=\\\\\\\"Path to pruned model (before RLVR)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--recovered_model_path\\\\\\\", required=True,\\\\n                        help=\\\\\\\"Path to RLVR-recovered model\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\\n\\nTests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more\\neffectively compensated by RLVR through their most similar retained head.\\n\\nMetric: for each pruned head h_p, find the most CKA-similar retained head h_r,\\nthen measure h_r's activation shift between pruned model and RLVR-recovered model.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport scipy.stats as stats\\nimport torch\\nimport torch.nn.functional as F\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\\n    \\\"\\\"\\\"Load a structurally pruned model by reconstructing from base model + saved weights.\\\"\\\"\\\"\\n    logging.getLogger(\\\"prune\\\").setLevel(logging.WARNING)\\n    from prune import prune_attention_heads, prune_mlp_channels\\n\\n    model = AutoModelForCausalLM.from_pretrained(\\n        base_model_path, torch_dtype=torch_dtype, device_map=\\\"cpu\\\", trust_remote_code=True\\n    )\\n    prune_attention_heads(model, pruning_meta[\\\"attn_keep_masks\\\"])\\n    prune_mlp_channels(model, pruning_meta[\\\"mlp_keep_masks\\\"])\\n\\n    safetensor_files = sorted(\\n        [f for f in os.listdir(saved_model_path) if f.endswith(\\\".safetensors\\\")]\\n    )\\n    if safetensor_files:\\n        from safetensors.torch import load_file\\n        state_dict = {}\\n        for f in safetensor_files:\\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\\n    else:\\n        state_dict = torch.load(\\n            os.path.join(saved_model_path, \\\"pytorch_model.bin\\\"),\\n            map_location=\\\"cpu\\\", weights_only=True,\\n        )\\n\\n    model.load_state_dict(state_dict)\\n    model.to(device)\\n    return model\\n\\n\\ndef collect_retained_head_activations(model, calibration_data, keep_masks, device):\\n    \\\"\\\"\\\"Collect per-head q_proj activations (mean-pooled over seq_len).\\n\\n    Returns dict[layer_idx] -> tensor[n_samples, n_retained_heads, head_dim]\\n    \\\"\\\"\\\"\\n    n_layers = model.config.num_hidden_layers\\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\\n\\n    q_outputs = {i: [] for i in range(n_layers)}\\n    hooks = []\\n\\n    def make_hook(layer_idx):\\n        def fn(module, inp, out):\\n            q_outputs[layer_idx].append(out.detach().cpu())\\n        return fn\\n\\n    for i in range(n_layers):\\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\\n        hooks.append(h)\\n\\n    model.eval()\\n    with torch.no_grad():\\n        for idx, enc in enumerate(calibration_data):\\n            input_ids = enc[\\\"input_ids\\\"].to(device)\\n            attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\n            if (idx + 1) % 50 == 0:\\n                logger.info(f\\\"  Processed {idx + 1}/{len(calibration_data)} samples\\\")\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    activations = {}\\n    for layer_idx in range(n_layers):\\n        n_retained = len(keep_masks[layer_idx])\\n        per_head = []\\n        for t in q_outputs[layer_idx]:\\n            t = t.squeeze(0)  # [seq, n_retained * head_dim]\\n            t = t\\n\\n... [截断: 输出过长，省略 208 字符] ...\\n\\nead, dim=0).float()\\n        q_outputs[layer_idx] = None\\n\\n    return activations\\n\\n\\ndef compute_recoverability(pruned_acts, recovered_acts, cka_data, keep_masks,\\n                           n_heads_original=28):\\n    \\\"\\\"\\\"Compute per-pruned-head recoverability as activation shift of best retained head.\\\"\\\"\\\"\\n    attn_overlap = cka_data[\\\"attn_overlap\\\"]\\n    attn_cka_matrix = cka_data[\\\"attn_cka_matrix\\\"]\\n    results = []\\n\\n    for layer_idx in range(len(keep_masks)):\\n        retained = keep_masks[layer_idx]\\n        pruned_heads = sorted(set(range(n_heads_original)) - set(retained))\\n        if not pruned_heads:\\n            continue\\n\\n        cka_matrix = attn_cka_matrix[layer_idx]\\n\\n        for h_p in pruned_heads:\\n            sims = torch.tensor([cka_matrix[h_p, h_r].item() for h_r in retained])\\n            best_idx = sims.argmax().item()\\n            h_r = retained[best_idx]\\n            h_r_local = retained.index(h_r)\\n\\n            act_p = pruned_acts[layer_idx][:, h_r_local, :]\\n            act_r = recovered_acts[layer_idx][:, h_r_local, :]\\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\\n            activation_shift = 1.0 - cos_sim.mean().item()\\n\\n            results.append({\\n                \\\"layer\\\": layer_idx,\\n                \\\"pruned_head\\\": h_p,\\n                \\\"best_retained_head\\\": h_r,\\n                \\\"cka_overlap\\\": attn_overlap[layer_idx][h_p].item(),\\n                \\\"recoverability\\\": activation_shift,\\n                \\\"cka_similarity_to_retained\\\": sims[best_idx].item(),\\n            })\\n\\n    return results\\n\\n\\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    x, y = np.array(x), np.array(y)\\n    n = len(x)\\n    rhos = []\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        r, _ = stats.spearmanr(x[idx], y[idx])\\n        if not np.isnan(r):\\n            rhos.append(r)\\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\\n\\n\\ndef permutation_test(x, y, n_perm=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    x, y = np.array(x), np.array(y)\\n    observed, _ = stats.spearmanr(x, y)\\n    count = 0\\n    for _ in range(n_perm):\\n        r, _ = stats.spearmanr(x, rng.permutation(y))\\n        if abs(r) >= abs(observed):\\n            count += 1\\n    return count / n_perm\\n\\n\\ndef make_scatter_plot(results, rho, p_value, ci, perm_p, output_path):\\n    try:\\n        import matplotlib\\n        matplotlib.use(\\\"Agg\\\")\\n        import matplotlib.pyplot as plt\\n    except ImportError:\\n        logger.warning(\\\"matplotlib not available, skipping scatter plot\\\")\\n        return\\n\\n    fh = [r[\\\"cka_overlap\\\"] for r in results]\\n    rec = [r[\\\"recoverability\\\"] for r in results]\\n    layers = [r[\\\"layer\\\"] for r in results]\\n\\n    fig, ax = plt.subplots(figsize=(8, 6))\\n    sc = ax.scatter(fh, rec, c=layers, cmap=\\\"viridis\\\", alpha=0.7,\\n                    edgecolors=\\\"k\\\", linewidths=0.3, s=30)\\n    plt.colorbar(sc, ax=ax, label=\\\"Layer index\\\")\\n    ax.set_xlabel(\\\"F(h_p) — CKA overlap of pruned head\\\")\\n    ax.set_ylabel(\\\"Recoverability — activation shift of best retained head\\\")\\n\\n    verdict = \\\"PASS\\\" if rho >= 0.4 else (\\\"WARNING\\\" if rho >= 0.3 else \\\"FAIL\\\")\\n    ax.set_title(\\n        f\\\"CKA Overlap vs RLVR Recoverability\\\\n\\\"\\n        f\\\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \\\"\\n        f\\\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\\\"\\n    )\\n    plt.tight_layout()\\n    plt.savefig(output_path, dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n    logger.info(f\\\"Scatter plot saved to {output_path}\\\")\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Correlation analysis: rho(CKA overlap, RLVR recoverability)\\\"\\n    )\\n    parser.add_argument(\\\"--base_model_path\\\", required=True,\\n                        help=\\\"Path to original unpruned model\\\")\\n    parser.add_argument(\\\"--pruned_model_path\\\", required=True,\\n                        help=\\\"Path to pruned model (before RLVR)\\\")\\n    parser.add_argument(\\\"--recovered_model_path\\\", required=True,\\n                        help=\\\"Path to RLVR-recovered model\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XJWigH4pLUgqGwn131iAwt`</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/recovery_aware_struct_prune/src/prune.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "07097259-fe23-4ba7-852f-3ca5b87d590c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APKVjCk21GxdQ1pqtZX4vS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3470,
      "cache_read_input_tokens": 39874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3470
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

_source line 39 · 2026-05-14T05:29:15.485Z_

<details><summary>↩ Tool result · `toolu_01XJWigH4pLUgqGwn131iAwt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nStructured Pruning for Qwen2.5 architecture (GQA-group granularity).\\n\\nRemoves GQA groups (7 Q heads + 1 KV head each) and MLP channel groups\\nbased on RASP or standard importance scores.\\n\\nInput:  pretrained model + pruning scores\\nOutput: pruned model saved to disk\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport copy\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef prune_attention_heads(model, attn_keep_masks: dict):\\n    \\\"\\\"\\\"Prune GQA groups from the model by slicing weight matrices in-place.\\n\\n    attn_keep_masks: dict[layer_idx -> list of GQA group indices to KEEP]\\n    Each GQA group = heads_per_kv Q heads + 1 KV head.\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n\\n    total_pruned_groups = 0\\n\\n    for layer_idx, keep_groups in attn_keep_masks.items():\\n        layer = model.model.layers[layer_idx]\\n        attn = layer.self_attn\\n        n_keep_groups = len(keep_groups)\\n        pruned_groups = n_kv_heads - n_keep_groups\\n\\n        # Expand GQA group indices to Q head weight indices\\n        q_indices = []\\n        for g in keep_groups:\\n            for qh in range(heads_per_kv):\\n                h = g * heads_per_kv + qh\\n                start = h * head_dim\\n                q_indices.extend(range(start, start + head_dim))\\n        q_indices = torch.tensor(q_indices, dtype=torch.long)\\n\\n        # KV head weight indices (1 per group)\\n        kv_indices = []\\n        for g in keep_groups:\\n            start = g * head_dim\\n            kv_indices.extend(range(start, start + head_dim))\\n        kv_indices = torch.tensor(kv_indices, dtype=torch.long)\\n\\n        # Slice q_proj: [n_heads*head_dim, hidden] -> [n_keep_q*head_dim, hidden]\\n        attn.q_proj.weight = torch.nn.Parameter(attn.q_proj.weight.data[q_indices])\\n        if attn.q_proj.bias is not None:\\n            attn.q_proj.bias = torch.nn.Parameter(attn.q_proj.bias.data[q_indices])\\n\\n        # Slice k_proj, v_proj: [n_kv*head_dim, hidden] -> [n_keep_kv*head_dim, hidden]\\n        attn.k_proj.weight = torch.nn.Parameter(attn.k_proj.weight.data[kv_indices])\\n        if attn.k_proj.bias is not None:\\n            attn.k_proj.bias = torch.nn.Parameter(attn.k_proj.bias.data[kv_indices])\\n\\n        attn.v_proj.weight = torch.nn.Parameter(attn.v_proj.weight.data[kv_indices])\\n        if attn.v_proj.bias is not None:\\n            attn.v_proj.bias = torch.nn.Parameter(attn.v_proj.bias.data[kv_indices])\\n\\n        # Slice o_proj: [hidden, n_heads*head_dim] -> [hidden, n_keep_q*head_dim]\\n        attn.o_proj.weight = torch.nn.Parameter(attn.o_proj.weight.data[:, q_indices])\\n\\n        # Update layer config\\n        n_keep_q = n_keep_groups * heads_per_kv\\n        attn.num_heads = n_keep_q\\n        attn.num_key_value_heads = n_keep_groups\\n        attn.head_dim = head_dim\\n\\n        total_pruned_groups += pruned_groups\\n\\n        if pruned_groups > 0:\\n            logger.info(\\n                f\\\"  Layer {layer_idx}: pruned {pruned_groups}/{n_kv_heads} GQA groups \\\"\\n                f\\\"({pruned_groups * heads_per_kv} Q heads, {pruned_groups} KV heads)\\\"\\n            )\\n\\n    logger.info(f\\\"Total attention pruning: {total_pruned_groups} GQA groups removed\\\")\\n\\n\\ndef prune_mlp_channels(model, mlp_keep_masks: dict, n_mlp_groups: int = 28):\\n    \\\"\\\"\\\"Prune MLP channel groups by slicing gate_proj, up_proj, and down_proj.\\\"\\\"\\\"\\n    config = model.config\\n    intermediate_size = config.intermediate_size\\n    group_size = intermediate_size // n_mlp_groups\\n\\n    total_pruned = 0\\n\\n    for layer_idx, keep_groups in mlp_keep_masks.items():\\n        layer = model.m\\n\\n... [截断: 输出过长，省略 7975 字符] ...\\n\\n   f\\\"(actual sparsity: {actual_sparsity:.2%})\\\"\\n    )\\n\\n    # --- Update model config ---\\n    per_layer_q_heads = []\\n    per_layer_kv_heads = []\\n    for li in range(n_layers):\\n        layer_i = model.model.layers[li]\\n        per_layer_q_heads.append(layer_i.self_attn.num_heads)\\n        per_layer_kv_heads.append(layer_i.self_attn.num_key_value_heads)\\n\\n    unique_q = set(per_layer_q_heads)\\n    unique_kv = set(per_layer_kv_heads)\\n\\n    if len(unique_q) == 1 and len(unique_kv) == 1:\\n        model.config.num_attention_heads = per_layer_q_heads[0]\\n        model.config.num_key_value_heads = per_layer_kv_heads[0]\\n        logger.info(f\\\"Uniform pruning: config num_attention_heads={per_layer_q_heads[0]}, \\\"\\n                    f\\\"num_key_value_heads={per_layer_kv_heads[0]}\\\")\\n    else:\\n        model.config.num_attention_heads = min(per_layer_q_heads)\\n        model.config.num_key_value_heads = min(per_layer_kv_heads)\\n        model.config.per_layer_num_attention_heads = per_layer_q_heads\\n        model.config.per_layer_num_key_value_heads = per_layer_kv_heads\\n        logger.warning(\\n            f\\\"Non-uniform pruning: per-layer Q heads range \\\"\\n            f\\\"[{min(per_layer_q_heads)}, {max(per_layer_q_heads)}], \\\"\\n            f\\\"KV heads range [{min(per_layer_kv_heads)}, {max(per_layer_kv_heads)}]. \\\"\\n            f\\\"Per-layer counts stored in config.\\\"\\n        )\\n\\n    # Update intermediate_size for MLP pruning\\n    per_layer_intermediate = []\\n    for li in range(n_layers):\\n        new_intermediate = model.model.layers[li].mlp.gate_proj.weight.shape[0]\\n        per_layer_intermediate.append(new_intermediate)\\n\\n    unique_intermediate = set(per_layer_intermediate)\\n    if len(unique_intermediate) == 1:\\n        model.config.intermediate_size = per_layer_intermediate[0]\\n        logger.info(f\\\"Updated config intermediate_size={per_layer_intermediate[0]}\\\")\\n    else:\\n        model.config.intermediate_size = min(per_layer_intermediate)\\n        model.config.per_layer_intermediate_size = per_layer_intermediate\\n        logger.warning(f\\\"Non-uniform MLP: intermediate_size range \\\"\\n                       f\\\"[{min(per_layer_intermediate)}, {max(per_layer_intermediate)}]\\\")\\n\\n    # Forward pass validation\\n    embed_device = model.model.embed_tokens.weight.device\\n    with torch.no_grad():\\n        dummy_input = torch.randint(0, 1000, (1, 32)).to(embed_device)\\n        try:\\n            output = model(dummy_input)\\n            logger.info(f\\\"Forward pass validation OK, output shape: {output.logits.shape}\\\")\\n        except Exception as e:\\n            logger.error(f\\\"Forward pass FAILED after pruning: {e}\\\")\\n            raise RuntimeError(f\\\"Pruned model forward pass failed: {e}\\\")\\n\\n    # Print pruning statistics\\n    logger.info(\\\"=\\\" * 50)\\n    logger.info(\\\"PRUNING STATISTICS\\\")\\n    logger.info(f\\\"  Mode: {args.mode}\\\")\\n    logger.info(f\\\"  Attn GQA groups pruned: {len(attn_prune_set)} / {n_layers * n_gqa_groups}\\\")\\n    logger.info(f\\\"  MLP groups pruned: {len(mlp_prune_set)} / {n_layers * n_mlp_groups}\\\")\\n    logger.info(f\\\"  Target sparsity: {args.sparsity:.2%}\\\")\\n    logger.info(f\\\"  Actual sparsity: {actual_sparsity:.2%}\\\")\\n    logger.info(\\\"=\\\" * 50)\\n\\n    # Save\\n    logger.info(f\\\"Saving pruned model to {args.output_path}\\\")\\n    os.makedirs(args.output_path, exist_ok=True)\\n    model.save_pretrained(args.output_path)\\n    tokenizer.save_pretrained(args.output_path)\\n\\n    # Save pruning metadata\\n    metadata = {\\n        \\\"mode\\\": args.mode,\\n        \\\"sparsity_target\\\": args.sparsity,\\n        \\\"sparsity_actual\\\": actual_sparsity,\\n        \\\"alpha\\\": args.alpha if args.mode == \\\"rasp\\\" else None,\\n        \\\"original_params\\\": original_params,\\n        \\\"pruned_params\\\": pruned_params_actual,\\n        \\\"attn_keep_masks\\\": attn_keep_masks,\\n        \\\"mlp_keep_masks\\\": mlp_keep_masks,\\n        \\\"n_attn_groups_pruned\\\": len(attn_prune_set),\\n        \\\"n_mlp_groups_pruned\\\": len(mlp_prune_set),\\n    }\\n    torch.save(metadata, os.path.join(args.output_path, \\\"pruning_metadata.pt\\\"))\\n    logger.info(\\\"Done.\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "89afa6c3-2bc9-44ed-bc3f-41fc9255c916",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nStructured Pruning for Qwen2.5 architecture (GQA-group granularity).\\\\n\\\\nRemoves GQA groups (7 Q heads + 1 KV head each) and MLP channel groups\\\\nbased on RASP or standard importance scores.\\\\n\\\\nInput:  pretrained model + pruning scores\\\\nOutput: pruned model saved to disk\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport copy\\\\nimport logging\\\\nimport os\\\\nimport random\\\\n\\\\nimport numpy as np\\\\nimport torch\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n)\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n\\\\ndef set_seed(seed: int):\\\\n    random.seed(seed)\\\\n    np.random.seed(seed)\\\\n    torch.manual_seed(seed)\\\\n    torch.cuda.manual_seed_all(seed)\\\\n\\\\n\\\\ndef prune_attention_heads(model, attn_keep_masks: dict):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Prune GQA groups from the model by slicing weight matrices in-place.\\\\n\\\\n    attn_keep_masks: dict[layer_idx -> list of GQA group indices to KEEP]\\\\n    Each GQA group = heads_per_kv Q heads + 1 KV head.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    config = model.config\\\\n    n_heads = config.num_attention_heads\\\\n    n_kv_heads = config.num_key_value_heads\\\\n    head_dim = config.hidden_size // n_heads\\\\n    heads_per_kv = n_heads // n_kv_heads\\\\n\\\\n    total_pruned_groups = 0\\\\n\\\\n    for layer_idx, keep_groups in attn_keep_masks.items():\\\\n        layer = model.model.layers[layer_idx]\\\\n        attn = layer.self_attn\\\\n        n_keep_groups = len(keep_groups)\\\\n        pruned_groups = n_kv_heads - n_keep_groups\\\\n\\\\n        # Expand GQA group indices to Q head weight indices\\\\n        q_indices = []\\\\n        for g in keep_groups:\\\\n            for qh in range(heads_per_kv):\\\\n                h = g * heads_per_kv + qh\\\\n                start = h * head_dim\\\\n                q_indices.extend(range(start, start + head_dim))\\\\n        q_indices = torch.tensor(q_indices, dtype=torch.long)\\\\n\\\\n        # KV head weight indices (1 per group)\\\\n        kv_indices = []\\\\n        for g in keep_groups:\\\\n            start = g * head_dim\\\\n            kv_indices.extend(range(start, start + head_dim))\\\\n        kv_indices = torch.tensor(kv_indices, dtype=torch.long)\\\\n\\\\n        # Slice q_proj: [n_heads*head_dim, hidden] -> [n_keep_q*head_dim, hidden]\\\\n        attn.q_proj.weight = torch.nn.Parameter(attn.q_proj.weight.data[q_indices])\\\\n        if attn.q_proj.bias is not None:\\\\n            attn.q_proj.bias = torch.nn.Parameter(attn.q_proj.bias.data[q_indices])\\\\n\\\\n        # Slice k_proj, v_proj: [n_kv*head_dim, hidden] -> [n_keep_kv*head_dim, hidden]\\\\n        attn.k_proj.weight = torch.nn.Parameter(attn.k_proj.weight.data[kv_indices])\\\\n        if attn.k_proj.bias is not None:\\\\n            attn.k_proj.bias = torch.nn.Parameter(attn.k_proj.bias.data[kv_indices])\\\\n\\\\n        attn.v_proj.weight = torch.nn.Parameter(attn.v_proj.weight.data[kv_indices])\\\\n        if attn.v_proj.bias is not None:\\\\n            attn.v_proj.bias = torch.nn.Parameter(attn.v_proj.bias.data[kv_indices])\\\\n\\\\n        # Slice o_proj: [hidden, n_heads*head_dim] -> [hidden, n_keep_q*head_dim]\\\\n        attn.o_proj.weight = torch.nn.Parameter(attn.o_proj.weight.data[:, q_indices])\\\\n\\\\n        # Update layer config\\\\n        n_keep_q = n_keep_groups * heads_per_kv\\\\n        attn.num_heads = n_keep_q\\\\n        attn.num_key_value_heads = n_keep_groups\\\\n        attn.head_dim = head_dim\\\\n\\\\n        total_pruned_groups += pruned_groups\\\\n\\\\n        if pruned_groups > 0:\\\\n            logger.info(\\\\n                f\\\\\\\"  Layer {layer_idx}: pruned {pruned_groups}/{n_kv_heads} GQA groups \\\\\\\"\\\\n                f\\\\\\\"({pruned_groups * heads_per_kv} Q heads, {pruned_groups} KV heads)\\\\\\\"\\\\n            )\\\\n\\\\n    logger.info(f\\\\\\\"Total attention pruning: {total_pruned_groups} GQA groups removed\\\\\\\")\\\\n\\\\n\\\\ndef prune_mlp_channels(model, mlp_keep_masks: dict, n_mlp_groups: int = 28):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Prune MLP channel groups by slicing gate_proj, up_proj, and down_proj.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    config = model.config\\\\n    intermediate_size = config.intermediate_size\\\\n    group_size = intermediate_size // n_mlp_groups\\\\n\\\\n    total_pruned = 0\\\\n\\\\n    for layer_idx, keep_groups in mlp_keep_masks.items():\\\\n        layer = model.m\\\\n\\\\n... [截断: 输出过长，省略 7975 字符] ...\\\\n\\\\n   f\\\\\\\"(actual sparsity: {actual_sparsity:.2%})\\\\\\\"\\\\n    )\\\\n\\\\n    # --- Update model config ---\\\\n    per_layer_q_heads = []\\\\n    per_layer_kv_heads = []\\\\n    for li in range(n_layers):\\\\n        layer_i = model.model.layers[li]\\\\n        per_layer_q_heads.append(layer_i.self_attn.num_heads)\\\\n        per_layer_kv_heads.append(layer_i.self_attn.num_key_value_heads)\\\\n\\\\n    unique_q = set(per_layer_q_heads)\\\\n    unique_kv = set(per_layer_kv_heads)\\\\n\\\\n    if len(unique_q) == 1 and len(unique_kv) == 1:\\\\n        model.config.num_attention_heads = per_layer_q_heads[0]\\\\n        model.config.num_key_value_heads = per_layer_kv_heads[0]\\\\n        logger.info(f\\\\\\\"Uniform pruning: config num_attention_heads={per_layer_q_heads[0]}, \\\\\\\"\\\\n                    f\\\\\\\"num_key_value_heads={per_layer_kv_heads[0]}\\\\\\\")\\\\n    else:\\\\n        model.config.num_attention_heads = min(per_layer_q_heads)\\\\n        model.config.num_key_value_heads = min(per_layer_kv_heads)\\\\n        model.config.per_layer_num_attention_heads = per_layer_q_heads\\\\n        model.config.per_layer_num_key_value_heads = per_layer_kv_heads\\\\n        logger.warning(\\\\n            f\\\\\\\"Non-uniform pruning: per-layer Q heads range \\\\\\\"\\\\n            f\\\\\\\"[{min(per_layer_q_heads)}, {max(per_layer_q_heads)}], \\\\\\\"\\\\n            f\\\\\\\"KV heads range [{min(per_layer_kv_heads)}, {max(per_layer_kv_heads)}]. \\\\\\\"\\\\n            f\\\\\\\"Per-layer counts stored in config.\\\\\\\"\\\\n        )\\\\n\\\\n    # Update intermediate_size for MLP pruning\\\\n    per_layer_intermediate = []\\\\n    for li in range(n_layers):\\\\n        new_intermediate = model.model.layers[li].mlp.gate_proj.weight.shape[0]\\\\n        per_layer_intermediate.append(new_intermediate)\\\\n\\\\n    unique_intermediate = set(per_layer_intermediate)\\\\n    if len(unique_intermediate) == 1:\\\\n        model.config.intermediate_size = per_layer_intermediate[0]\\\\n        logger.info(f\\\\\\\"Updated config intermediate_size={per_layer_intermediate[0]}\\\\\\\")\\\\n    else:\\\\n        model.config.intermediate_size = min(per_layer_intermediate)\\\\n        model.config.per_layer_intermediate_size = per_layer_intermediate\\\\n        logger.warning(f\\\\\\\"Non-uniform MLP: intermediate_size range \\\\\\\"\\\\n                       f\\\\\\\"[{min(per_layer_intermediate)}, {max(per_layer_intermediate)}]\\\\\\\")\\\\n\\\\n    # Forward pass validation\\\\n    embed_device = model.model.embed_tokens.weight.device\\\\n    with torch.no_grad():\\\\n        dummy_input = torch.randint(0, 1000, (1, 32)).to(embed_device)\\\\n        try:\\\\n            output = model(dummy_input)\\\\n            logger.info(f\\\\\\\"Forward pass validation OK, output shape: {output.logits.shape}\\\\\\\")\\\\n        except Exception as e:\\\\n            logger.error(f\\\\\\\"Forward pass FAILED after pruning: {e}\\\\\\\")\\\\n            raise RuntimeError(f\\\\\\\"Pruned model forward pass failed: {e}\\\\\\\")\\\\n\\\\n    # Print pruning statistics\\\\n    logger.info(\\\\\\\"=\\\\\\\" * 50)\\\\n    logger.info(\\\\\\\"PRUNING STATISTICS\\\\\\\")\\\\n    logger.info(f\\\\\\\"  Mode: {args.mode}\\\\\\\")\\\\n    logger.info(f\\\\\\\"  Attn GQA groups pruned: {len(attn_prune_set)} / {n_layers * n_gqa_groups}\\\\\\\")\\\\n    logger.info(f\\\\\\\"  MLP groups pruned: {len(mlp_prune_set)} / {n_layers * n_mlp_groups}\\\\\\\")\\\\n    logger.info(f\\\\\\\"  Target sparsity: {args.sparsity:.2%}\\\\\\\")\\\\n    logger.info(f\\\\\\\"  Actual sparsity: {actual_sparsity:.2%}\\\\\\\")\\\\n    logger.info(\\\\\\\"=\\\\\\\" * 50)\\\\n\\\\n    # Save\\\\n    logger.info(f\\\\\\\"Saving pruned model to {args.output_path}\\\\\\\")\\\\n    os.makedirs(args.output_path, exist_ok=True)\\\\n    model.save_pretrained(args.output_path)\\\\n    tokenizer.save_pretrained(args.output_path)\\\\n\\\\n    # Save pruning metadata\\\\n    metadata = {\\\\n        \\\\\\\"mode\\\\\\\": args.mode,\\\\n        \\\\\\\"sparsity_target\\\\\\\": args.sparsity,\\\\n        \\\\\\\"sparsity_actual\\\\\\\": actual_sparsity,\\\\n        \\\\\\\"alpha\\\\\\\": args.alpha if args.mode == \\\\\\\"rasp\\\\\\\" else None,\\\\n        \\\\\\\"original_params\\\\\\\": original_params,\\\\n        \\\\\\\"pruned_params\\\\\\\": pruned_params_actual,\\\\n        \\\\\\\"attn_keep_masks\\\\\\\": attn_keep_masks,\\\\n        \\\\\\\"mlp_keep_masks\\\\\\\": mlp_keep_masks,\\\\n        \\\\\\\"n_attn_groups_pruned\\\\\\\": len(attn_prune_set),\\\\n        \\\\\\\"n_mlp_groups_pruned\\\\\\\": len(mlp_prune_set),\\\\n    }\\\\n    torch.save(metadata, os.path.join(args.output_path, \\\\\\\"pruning_metadata.pt\\\\\\\"))\\\\n    logger.info(\\\\\\\"Done.\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.84}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nStructured Pruning for Qwen2.5 architecture (GQA-group granularity).\\n\\nRemoves GQA groups (7 Q heads + 1 KV head each) and MLP channel groups\\nbased on RASP or standard importance scores.\\n\\nInput:  pretrained model + pruning scores\\nOutput: pruned model saved to disk\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport copy\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef prune_attention_heads(model, attn_keep_masks: dict):\\n    \\\"\\\"\\\"Prune GQA groups from the model by slicing weight matrices in-place.\\n\\n    attn_keep_masks: dict[layer_idx -> list of GQA group indices to KEEP]\\n    Each GQA group = heads_per_kv Q heads + 1 KV head.\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n\\n    total_pruned_groups = 0\\n\\n    for layer_idx, keep_groups in attn_keep_masks.items():\\n        layer = model.model.layers[layer_idx]\\n        attn = layer.self_attn\\n        n_keep_groups = len(keep_groups)\\n        pruned_groups = n_kv_heads - n_keep_groups\\n\\n        # Expand GQA group indices to Q head weight indices\\n        q_indices = []\\n        for g in keep_groups:\\n            for qh in range(heads_per_kv):\\n                h = g * heads_per_kv + qh\\n                start = h * head_dim\\n                q_indices.extend(range(start, start + head_dim))\\n        q_indices = torch.tensor(q_indices, dtype=torch.long)\\n\\n        # KV head weight indices (1 per group)\\n        kv_indices = []\\n        for g in keep_groups:\\n            start = g * head_dim\\n            kv_indices.extend(range(start, start + head_dim))\\n        kv_indices = torch.tensor(kv_indices, dtype=torch.long)\\n\\n        # Slice q_proj: [n_heads*head_dim, hidden] -> [n_keep_q*head_dim, hidden]\\n        attn.q_proj.weight = torch.nn.Parameter(attn.q_proj.weight.data[q_indices])\\n        if attn.q_proj.bias is not None:\\n            attn.q_proj.bias = torch.nn.Parameter(attn.q_proj.bias.data[q_indices])\\n\\n        # Slice k_proj, v_proj: [n_kv*head_dim, hidden] -> [n_keep_kv*head_dim, hidden]\\n        attn.k_proj.weight = torch.nn.Parameter(attn.k_proj.weight.data[kv_indices])\\n        if attn.k_proj.bias is not None:\\n            attn.k_proj.bias = torch.nn.Parameter(attn.k_proj.bias.data[kv_indices])\\n\\n        attn.v_proj.weight = torch.nn.Parameter(attn.v_proj.weight.data[kv_indices])\\n        if attn.v_proj.bias is not None:\\n            attn.v_proj.bias = torch.nn.Parameter(attn.v_proj.bias.data[kv_indices])\\n\\n        # Slice o_proj: [hidden, n_heads*head_dim] -> [hidden, n_keep_q*head_dim]\\n        attn.o_proj.weight = torch.nn.Parameter(attn.o_proj.weight.data[:, q_indices])\\n\\n        # Update layer config\\n        n_keep_q = n_keep_groups * heads_per_kv\\n        attn.num_heads = n_keep_q\\n        attn.num_key_value_heads = n_keep_groups\\n        attn.head_dim = head_dim\\n\\n        total_pruned_groups += pruned_groups\\n\\n        if pruned_groups > 0:\\n            logger.info(\\n                f\\\"  Layer {layer_idx}: pruned {pruned_groups}/{n_kv_heads} GQA groups \\\"\\n                f\\\"({pruned_groups * heads_per_kv} Q heads, {pruned_groups} KV heads)\\\"\\n            )\\n\\n    logger.info(f\\\"Total attention pruning: {total_pruned_groups} GQA groups removed\\\")\\n\\n\\ndef prune_mlp_channels(model, mlp_keep_masks: dict, n_mlp_groups: int = 28):\\n    \\\"\\\"\\\"Prune MLP channel groups by slicing gate_proj, up_proj, and down_proj.\\\"\\\"\\\"\\n    config = model.config\\n    intermediate_size = config.intermediate_size\\n    group_size = intermediate_size // n_mlp_groups\\n\\n    total_pruned = 0\\n\\n    for layer_idx, keep_groups in mlp_keep_masks.items():\\n        layer = model.m\\n\\n... [截断: 输出过长，省略 7975 字符] ...\\n\\n   f\\\"(actual sparsity: {actual_sparsity:.2%})\\\"\\n    )\\n\\n    # --- Update model config ---\\n    per_layer_q_heads = []\\n    per_layer_kv_heads = []\\n    for li in range(n_layers):\\n        layer_i = model.model.layers[li]\\n        per_layer_q_heads.append(layer_i.self_attn.num_heads)\\n        per_layer_kv_heads.append(layer_i.self_attn.num_key_value_heads)\\n\\n    unique_q = set(per_layer_q_heads)\\n    unique_kv = set(per_layer_kv_heads)\\n\\n    if len(unique_q) == 1 and len(unique_kv) == 1:\\n        model.config.num_attention_heads = per_layer_q_heads[0]\\n        model.config.num_key_value_heads = per_layer_kv_heads[0]\\n        logger.info(f\\\"Uniform pruning: config num_attention_heads={per_layer_q_heads[0]}, \\\"\\n                    f\\\"num_key_value_heads={per_layer_kv_heads[0]}\\\")\\n    else:\\n        model.config.num_attention_heads = min(per_layer_q_heads)\\n        model.config.num_key_value_heads = min(per_layer_kv_heads)\\n        model.config.per_layer_num_attention_heads = per_layer_q_heads\\n        model.config.per_layer_num_key_value_heads = per_layer_kv_heads\\n        logger.warning(\\n            f\\\"Non-uniform pruning: per-layer Q heads range \\\"\\n            f\\\"[{min(per_layer_q_heads)}, {max(per_layer_q_heads)}], \\\"\\n            f\\\"KV heads range [{min(per_layer_kv_heads)}, {max(per_layer_kv_heads)}]. \\\"\\n            f\\\"Per-layer counts stored in config.\\\"\\n        )\\n\\n    # Update intermediate_size for MLP pruning\\n    per_layer_intermediate = []\\n    for li in range(n_layers):\\n        new_intermediate = model.model.layers[li].mlp.gate_proj.weight.shape[0]\\n        per_layer_intermediate.append(new_intermediate)\\n\\n    unique_intermediate = set(per_layer_intermediate)\\n    if len(unique_intermediate) == 1:\\n        model.config.intermediate_size = per_layer_intermediate[0]\\n        logger.info(f\\\"Updated config intermediate_size={per_layer_intermediate[0]}\\\")\\n    else:\\n        model.config.intermediate_size = min(per_layer_intermediate)\\n        model.config.per_layer_intermediate_size = per_layer_intermediate\\n        logger.warning(f\\\"Non-uniform MLP: intermediate_size range \\\"\\n                       f\\\"[{min(per_layer_intermediate)}, {max(per_layer_intermediate)}]\\\")\\n\\n    # Forward pass validation\\n    embed_device = model.model.embed_tokens.weight.device\\n    with torch.no_grad():\\n        dummy_input = torch.randint(0, 1000, (1, 32)).to(embed_device)\\n        try:\\n            output = model(dummy_input)\\n            logger.info(f\\\"Forward pass validation OK, output shape: {output.logits.shape}\\\")\\n        except Exception as e:\\n            logger.error(f\\\"Forward pass FAILED after pruning: {e}\\\")\\n            raise RuntimeError(f\\\"Pruned model forward pass failed: {e}\\\")\\n\\n    # Print pruning statistics\\n    logger.info(\\\"=\\\" * 50)\\n    logger.info(\\\"PRUNING STATISTICS\\\")\\n    logger.info(f\\\"  Mode: {args.mode}\\\")\\n    logger.info(f\\\"  Attn GQA groups pruned: {len(attn_prune_set)} / {n_layers * n_gqa_groups}\\\")\\n    logger.info(f\\\"  MLP groups pruned: {len(mlp_prune_set)} / {n_layers * n_mlp_groups}\\\")\\n    logger.info(f\\\"  Target sparsity: {args.sparsity:.2%}\\\")\\n    logger.info(f\\\"  Actual sparsity: {actual_sparsity:.2%}\\\")\\n    logger.info(\\\"=\\\" * 50)\\n\\n    # Save\\n    logger.info(f\\\"Saving pruned model to {args.output_path}\\\")\\n    os.makedirs(args.output_path, exist_ok=True)\\n    model.save_pretrained(args.output_path)\\n    tokenizer.save_pretrained(args.output_path)\\n\\n    # Save pruning metadata\\n    metadata = {\\n        \\\"mode\\\": args.mode,\\n        \\\"sparsity_target\\\": args.sparsity,\\n        \\\"sparsity_actual\\\": actual_sparsity,\\n        \\\"alpha\\\": args.alpha if args.mode == \\\"rasp\\\" else None,\\n        \\\"original_params\\\": original_params,\\n        \\\"pruned_params\\\": pruned_params_actual,\\n        \\\"attn_keep_masks\\\": attn_keep_masks,\\n        \\\"mlp_keep_masks\\\": mlp_keep_masks,\\n        \\\"n_attn_groups_pruned\\\": len(attn_prune_set),\\n        \\\"n_mlp_groups_pruned\\\": len(mlp_prune_set),\\n    }\\n    torch.save(metadata, os.path.join(args.output_path, \\\"pruning_metadata.pt\\\"))\\n    logger.info(\\\"Done.\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture. Let me also read the truncated middle of prune.py to understand the unified ranking and group parameter logic.

Actually, I can see from the tail of prune.py that:
1. `attn_keep_masks` and `mlp_keep_masks` are already saved in `pruning_metadata.pt` ✓
2. The metadata includes both attn and mlp info ✓

Now let me read the truncated portion of correlation_analysis.py and the importance_score.py to understand MLP group structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "bcd9634f-f56b-4b8b-8d35-18db4f9e7148",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUHKk9oW9xC4YbgWspwwU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3363,
      "cache_read_input_tokens": 43344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3363
      },
      "output_tokens": 12,
      "service_tier": "standard",
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

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UdxGHShVfRiWEZxRc6H4ZG`</summary>

```json
{
  "server": "westb-23072",
  "command": "head -115 /root/recovery_aware_struct_prune/src/correlation_analysis.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "0b7fc03e-cddb-4f25-884e-fca36f32e0b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUHKk9oW9xC4YbgWspwwU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3363,
      "cache_read_input_tokens": 43344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3363
      },
      "output_tokens": 12,
      "service_tier": "standard",
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

_source line 42 · 2026-05-14T05:29:22.031Z_

<details><summary>↩ Tool result · `toolu_01UdxGHShVfRiWEZxRc6H4ZG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\\n\\nTests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more\\neffectively compensated by RLVR through their most similar retained head.\\n\\nMetric: for each pruned head h_p, find the most CKA-similar retained head h_r,\\nthen measure h_r's activation shift between pruned model and RLVR-recovered model.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport scipy.stats as stats\\nimport torch\\nimport torch.nn.functional as F\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\\n    \\\"\\\"\\\"Load a structurally pruned model by reconstructing from base model + saved weights.\\\"\\\"\\\"\\n    logging.getLogger(\\\"prune\\\").setLevel(logging.WARNING)\\n    from prune import prune_attention_heads, prune_mlp_channels\\n\\n    model = AutoModelForCausalLM.from_pretrained(\\n        base_model_path, torch_dtype=torch_dtype, device_map=\\\"cpu\\\", trust_remote_code=True\\n    )\\n    prune_attention_heads(model, pruning_meta[\\\"attn_keep_masks\\\"])\\n    prune_mlp_channels(model, pruning_meta[\\\"mlp_keep_masks\\\"])\\n\\n    safetensor_files = sorted(\\n        [f for f in os.listdir(saved_model_path) if f.endswith(\\\".safetensors\\\")]\\n    )\\n    if safetensor_files:\\n        from safetensors.torch import load_file\\n        state_dict = {}\\n        for f in safetensor_files:\\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\\n    else:\\n        state_dict = torch.load(\\n            os.path.join(saved_model_path, \\\"pytorch_model.bin\\\"),\\n            map_location=\\\"cpu\\\", weights_only=True,\\n        )\\n\\n    model.load_state_dict(state_dict)\\n    model.to(device)\\n    return model\\n\\n\\ndef collect_retained_head_activations(model, calibration_data, keep_masks, device):\\n    \\\"\\\"\\\"Collect per-head q_proj activations (mean-pooled over seq_len).\\n\\n    Returns dict[layer_idx] -> tensor[n_samples, n_retained_heads, head_dim]\\n    \\\"\\\"\\\"\\n    n_layers = model.config.num_hidden_layers\\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\\n\\n    q_outputs = {i: [] for i in range(n_layers)}\\n    hooks = []\\n\\n    def make_hook(layer_idx):\\n        def fn(module, inp, out):\\n            q_outputs[layer_idx].append(out.detach().cpu())\\n        return fn\\n\\n    for i in range(n_layers):\\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\\n        hooks.append(h)\\n\\n    model.eval()\\n    with torch.no_grad():\\n        for idx, enc in enumerate(calibration_data):\\n            input_ids = enc[\\\"input_ids\\\"].to(device)\\n            attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\n            if (idx + 1) % 50 == 0:\\n                logger.info(f\\\"  Processed {idx + 1}/{len(calibration_data)} samples\\\")\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    activations = {}\\n    for layer_idx in range(n_layers):\\n        n_retained = len(keep_masks[layer_idx])\\n        per_head = []\\n        for t in q_outputs[layer_idx]:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "95eeb415-9adb-424d-bbfe-217c39b963f9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\\\\n\\\\nTests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more\\\\neffectively compensated by RLVR through their most similar retained head.\\\\n\\\\nMetric: for each pruned head h_p, find the most CKA-similar retained head h_r,\\\\nthen measure h_r's activation shift between pruned model and RLVR-recovered model.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport random\\\\n\\\\nimport numpy as np\\\\nimport scipy.stats as stats\\\\nimport torch\\\\nimport torch.nn.functional as F\\\\nfrom datasets import load_dataset\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n)\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n\\\\ndef set_seed(seed: int):\\\\n    random.seed(seed)\\\\n    np.random.seed(seed)\\\\n    torch.manual_seed(seed)\\\\n    torch.cuda.manual_seed_all(seed)\\\\n\\\\n\\\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\\\n    ds = load_dataset(\\\\\\\"openai/gsm8k\\\\\\\", \\\\\\\"main\\\\\\\", split=\\\\\\\"train\\\\\\\")\\\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\\\n    encodings = []\\\\n    for example in ds:\\\\n        prompt = f\\\\\\\"Question: {example['question']}\\\\\\\\nAnswer: Let me think step by step.\\\\\\\\n\\\\\\\"\\\\n        ids = tokenizer(prompt, return_tensors=\\\\\\\"pt\\\\\\\", truncation=True, max_length=max_length)\\\\n        encodings.append(ids)\\\\n    return encodings\\\\n\\\\n\\\\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load a structurally pruned model by reconstructing from base model + saved weights.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    logging.getLogger(\\\\\\\"prune\\\\\\\").setLevel(logging.WARNING)\\\\n    from prune import prune_attention_heads, prune_mlp_channels\\\\n\\\\n    model = AutoModelForCausalLM.from_pretrained(\\\\n        base_model_path, torch_dtype=torch_dtype, device_map=\\\\\\\"cpu\\\\\\\", trust_remote_code=True\\\\n    )\\\\n    prune_attention_heads(model, pruning_meta[\\\\\\\"attn_keep_masks\\\\\\\"])\\\\n    prune_mlp_channels(model, pruning_meta[\\\\\\\"mlp_keep_masks\\\\\\\"])\\\\n\\\\n    safetensor_files = sorted(\\\\n        [f for f in os.listdir(saved_model_path) if f.endswith(\\\\\\\".safetensors\\\\\\\")]\\\\n    )\\\\n    if safetensor_files:\\\\n        from safetensors.torch import load_file\\\\n        state_dict = {}\\\\n        for f in safetensor_files:\\\\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\\\\n    else:\\\\n        state_dict = torch.load(\\\\n            os.path.join(saved_model_path, \\\\\\\"pytorch_model.bin\\\\\\\"),\\\\n            map_location=\\\\\\\"cpu\\\\\\\", weights_only=True,\\\\n        )\\\\n\\\\n    model.load_state_dict(state_dict)\\\\n    model.to(device)\\\\n    return model\\\\n\\\\n\\\\ndef collect_retained_head_activations(model, calibration_data, keep_masks, device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Collect per-head q_proj activations (mean-pooled over seq_len).\\\\n\\\\n    Returns dict[layer_idx] -> tensor[n_samples, n_retained_heads, head_dim]\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    n_layers = model.config.num_hidden_layers\\\\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\\\\n\\\\n    q_outputs = {i: [] for i in range(n_layers)}\\\\n    hooks = []\\\\n\\\\n    def make_hook(layer_idx):\\\\n        def fn(module, inp, out):\\\\n            q_outputs[layer_idx].append(out.detach().cpu())\\\\n        return fn\\\\n\\\\n    for i in range(n_layers):\\\\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\\\\n        hooks.append(h)\\\\n\\\\n    model.eval()\\\\n    with torch.no_grad():\\\\n        for idx, enc in enumerate(calibration_data):\\\\n            input_ids = enc[\\\\\\\"input_ids\\\\\\\"].to(device)\\\\n            attention_mask = enc[\\\\\\\"attention_mask\\\\\\\"].to(device)\\\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\\\n            if (idx + 1) % 50 == 0:\\\\n                logger.info(f\\\\\\\"  Processed {idx + 1}/{len(calibration_data)} samples\\\\\\\")\\\\n\\\\n    for h in hooks:\\\\n        h.remove()\\\\n\\\\n    activations = {}\\\\n    for layer_idx in range(n_layers):\\\\n        n_retained = len(keep_masks[layer_idx])\\\\n        per_head = []\\\\n        for t in q_outputs[layer_idx]:\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\\n\\nTests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more\\neffectively compensated by RLVR through their most similar retained head.\\n\\nMetric: for each pruned head h_p, find the most CKA-similar retained head h_r,\\nthen measure h_r's activation shift between pruned model and RLVR-recovered model.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport scipy.stats as stats\\nimport torch\\nimport torch.nn.functional as F\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\\n    \\\"\\\"\\\"Load a structurally pruned model by reconstructing from base model + saved weights.\\\"\\\"\\\"\\n    logging.getLogger(\\\"prune\\\").setLevel(logging.WARNING)\\n    from prune import prune_attention_heads, prune_mlp_channels\\n\\n    model = AutoModelForCausalLM.from_pretrained(\\n        base_model_path, torch_dtype=torch_dtype, device_map=\\\"cpu\\\", trust_remote_code=True\\n    )\\n    prune_attention_heads(model, pruning_meta[\\\"attn_keep_masks\\\"])\\n    prune_mlp_channels(model, pruning_meta[\\\"mlp_keep_masks\\\"])\\n\\n    safetensor_files = sorted(\\n        [f for f in os.listdir(saved_model_path) if f.endswith(\\\".safetensors\\\")]\\n    )\\n    if safetensor_files:\\n        from safetensors.torch import load_file\\n        state_dict = {}\\n        for f in safetensor_files:\\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\\n    else:\\n        state_dict = torch.load(\\n            os.path.join(saved_model_path, \\\"pytorch_model.bin\\\"),\\n            map_location=\\\"cpu\\\", weights_only=True,\\n        )\\n\\n    model.load_state_dict(state_dict)\\n    model.to(device)\\n    return model\\n\\n\\ndef collect_retained_head_activations(model, calibration_data, keep_masks, device):\\n    \\\"\\\"\\\"Collect per-head q_proj activations (mean-pooled over seq_len).\\n\\n    Returns dict[layer_idx] -> tensor[n_samples, n_retained_heads, head_dim]\\n    \\\"\\\"\\\"\\n    n_layers = model.config.num_hidden_layers\\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\\n\\n    q_outputs = {i: [] for i in range(n_layers)}\\n    hooks = []\\n\\n    def make_hook(layer_idx):\\n        def fn(module, inp, out):\\n            q_outputs[layer_idx].append(out.detach().cpu())\\n        return fn\\n\\n    for i in range(n_layers):\\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\\n        hooks.append(h)\\n\\n    model.eval()\\n    with torch.no_grad():\\n        for idx, enc in enumerate(calibration_data):\\n            input_ids = enc[\\\"input_ids\\\"].to(device)\\n            attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\\n            if (idx + 1) % 50 == 0:\\n                logger.info(f\\\"  Processed {idx + 1}/{len(calibration_data)} samples\\\")\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    activations = {}\\n    for layer_idx in range(n_layers):\\n        n_retained = len(keep_masks[layer_idx])\\n        per_head = []\\n        for t in q_outputs[layer_idx]:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YDcYvZmFbvRkQCigP9Qads`</summary>

```json
{
  "server": "westb-23072",
  "command": "tail -n +112 /root/recovery_aware_struct_prune/src/correlation_analysis.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "9bd55377-0f8d-4c15-9bce-f27ddcf90d5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2ENsBFZzS9bUjVLaRbxzf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 46707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1823
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

_source line 44 · 2026-05-14T05:29:26.405Z_

<details><summary>↩ Tool result · `toolu_01YDcYvZmFbvRkQCigP9Qads`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    for layer_idx in range(n_layers):\\n        n_retained = len(keep_masks[layer_idx])\\n        per_head = []\\n        for t in q_outputs[layer_idx]:\\n            t = t.squeeze(0)  # [seq, n_retained * head_dim]\\n            t = t.view(t.shape[0], n_retained, head_dim)  # [seq, n_retained, head_dim]\\n            t = t.mean(dim=0)  # [n_retained, head_dim]\\n            per_head.append(t)\\n        activations[layer_idx] = torch.stack(per_head, dim=0).float()\\n        q_outputs[layer_idx] = None\\n\\n    return activations\\n\\n\\ndef compute_recoverability(pruned_acts, recovered_acts, cka_data, keep_masks,\\n                           n_heads_original=28):\\n    \\\"\\\"\\\"Compute per-pruned-head recoverability as activation shift of best retained head.\\\"\\\"\\\"\\n    attn_overlap = cka_data[\\\"attn_overlap\\\"]\\n    attn_cka_matrix = cka_data[\\\"attn_cka_matrix\\\"]\\n    results = []\\n\\n    for layer_idx in range(len(keep_masks)):\\n        retained = keep_masks[layer_idx]\\n        pruned_heads = sorted(set(range(n_heads_original)) - set(retained))\\n        if not pruned_heads:\\n            continue\\n\\n        cka_matrix = attn_cka_matrix[layer_idx]\\n\\n        for h_p in pruned_heads:\\n            sims = torch.tensor([cka_matrix[h_p, h_r].item() for h_r in retained])\\n            best_idx = sims.argmax().item()\\n            h_r = retained[best_idx]\\n            h_r_local = retained.index(h_r)\\n\\n            act_p = pruned_acts[layer_idx][:, h_r_local, :]\\n            act_r = recovered_acts[layer_idx][:, h_r_local, :]\\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\\n            activation_shift = 1.0 - cos_sim.mean().item()\\n\\n            results.append({\\n                \\\"layer\\\": layer_idx,\\n                \\\"pruned_head\\\": h_p,\\n                \\\"best_retained_head\\\": h_r,\\n                \\\"cka_overlap\\\": attn_overlap[layer_idx][h_p].item(),\\n                \\\"recoverability\\\": activation_shift,\\n                \\\"cka_similarity_to_retained\\\": sims[best_idx].item(),\\n            })\\n\\n    return results\\n\\n\\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    x, y = np.array(x), np.array(y)\\n    n = len(x)\\n    rhos = []\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        r, _ = stats.spearmanr(x[idx], y[idx])\\n        if not np.isnan(r):\\n            rhos.append(r)\\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\\n\\n\\ndef permutation_test(x, y, n_perm=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    x, y = np.array(x), np.array(y)\\n    observed, _ = stats.spearmanr(x, y)\\n    count = 0\\n    for _ in range(n_perm):\\n        r, _ = stats.spearmanr(x, rng.permutation(y))\\n        if abs(r) >= abs(observed):\\n            count += 1\\n    return count / n_perm\\n\\n\\ndef make_scatter_plot(results, rho, p_value, ci, perm_p, output_path):\\n    try:\\n        import matplotlib\\n        matplotlib.use(\\\"Agg\\\")\\n        import matplotlib.pyplot as plt\\n    except ImportError:\\n        logger.warning(\\\"matplotlib not available, skipping scatter plot\\\")\\n        return\\n\\n    fh = [r[\\\"cka_overlap\\\"] for r in results]\\n    rec = [r[\\\"recoverability\\\"] for r in results]\\n    layers = [r[\\\"layer\\\"] for r in results]\\n\\n    fig, ax = plt.subplots(figsize=(8, 6))\\n    sc = ax.scatter(fh, rec, c=layers, cmap=\\\"viridis\\\", alpha=0.7,\\n                    edgecolors=\\\"k\\\", linewidths=0.3, s=30)\\n    plt.colorbar(sc, ax=ax, label=\\\"Layer index\\\")\\n    ax.set_xlabel(\\\"F(h_p) — CKA overlap of pruned head\\\")\\n    ax.set_ylabel(\\\"Recoverability — activation shift of best retained head\\\")\\n\\n    verdict = \\\"PASS\\\" if rho >= 0.4 else (\\\"WARNING\\\" if rho >= 0.3 else \\\"FAIL\\\")\\n    ax.set_title(\\n        f\\\"CKA Overlap vs RLVR Recoverability\\\\n\\\"\\n        f\\\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \\\"\\n        f\\\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\\\"\\n    )\\n    plt.tight_layout()\\n    plt.savefig(output_path, dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n    logger.info(f\\\"Scatter plot saved to {output_path}\\\")\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Correlation a\\n\\n... [截断: 输出过长，省略 842 字符] ...\\n\\n of calibration samples\\\")\\n    parser.add_argument(\\\"--output_dir\\\", default=\\\"results/analysis/\\\",\\n                        help=\\\"Output directory\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42)\\n    parser.add_argument(\\\"--dtype\\\", type=str, default=\\\"bfloat16\\\",\\n                        choices=[\\\"float16\\\", \\\"bfloat16\\\", \\\"float32\\\"])\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(\\\"cuda\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    torch_dtype = {\\\"float16\\\": torch.float16, \\\"bfloat16\\\": torch.bfloat16,\\n                   \\\"float32\\\": torch.float32}[args.dtype]\\n\\n    logger.info(\\\"Loading CKA scores...\\\")\\n    cka_data = torch.load(args.cka_scores_path, map_location=\\\"cpu\\\", weights_only=True)\\n    if \\\"attn_cka_matrix\\\" not in cka_data:\\n        raise ValueError(\\n            \\\"CKA scores missing 'attn_cka_matrix'. \\\"\\n            \\\"Re-run cka_overlap.py to generate pairwise CKA matrices.\\\"\\n        )\\n\\n    logger.info(\\\"Loading pruning metadata...\\\")\\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\\\"cpu\\\",\\n                              weights_only=True)\\n    keep_masks = pruning_meta[\\\"attn_keep_masks\\\"]\\n\\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\\n    logger.info(f\\\"Loaded {len(calibration_data)} calibration samples\\\")\\n\\n    logger.info(f\\\"Loading pruned model from {args.pruned_model_path}\\\")\\n    pruned_model = load_pruned_model(\\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\\n    )\\n    logger.info(\\\"Collecting activations from pruned model...\\\")\\n    pruned_acts = collect_retained_head_activations(\\n        pruned_model, calibration_data, keep_masks, device\\n    )\\n    del pruned_model\\n    torch.cuda.empty_cache()\\n\\n    logger.info(f\\\"Loading recovered model from {args.recovered_model_path}\\\")\\n    recovered_model = load_pruned_model(\\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\\n    )\\n    logger.info(\\\"Collecting activations from recovered model...\\\")\\n    recovered_acts = collect_retained_head_activations(\\n        recovered_model, calibration_data, keep_masks, device\\n    )\\n    del recovered_model\\n    torch.cuda.empty_cache()\\n\\n    logger.info(\\\"Computing recoverability scores...\\\")\\n    n_heads = 28\\n    results = compute_recoverability(\\n        pruned_acts, recovered_acts, cka_data, keep_masks, n_heads\\n    )\\n    del pruned_acts, recovered_acts\\n    logger.info(f\\\"Computed recoverability for {len(results)} pruned heads\\\")\\n\\n    fh = [r[\\\"cka_overlap\\\"] for r in results]\\n    rec = [r[\\\"recoverability\\\"] for r in results]\\n    rho, p_value = stats.spearmanr(fh, rec)\\n    ci = bootstrap_spearman(fh, rec, seed=args.seed)\\n    perm_p = permutation_test(fh, rec, seed=args.seed)\\n\\n    verdict = \\\"PASS\\\" if rho >= 0.4 else (\\\"WARNING\\\" if rho >= 0.3 else \\\"FAIL\\\")\\n\\n    os.makedirs(args.output_dir, exist_ok=True)\\n    output = {\\n        \\\"spearman_rho\\\": rho,\\n        \\\"p_value\\\": p_value,\\n        \\\"bootstrap_ci_95\\\": ci,\\n        \\\"permutation_p_value\\\": perm_p,\\n        \\\"n_pruned_heads\\\": len(results),\\n        \\\"mvp_verdict\\\": verdict,\\n        \\\"per_head_data\\\": results,\\n    }\\n    json_path = os.path.join(args.output_dir, \\\"correlation_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2)\\n    logger.info(f\\\"Results saved to {json_path}\\\")\\n\\n    plot_path = os.path.join(args.output_dir, \\\"fh_vs_recoverability.png\\\")\\n    make_scatter_plot(results, rho, p_value, ci, perm_p, plot_path)\\n\\n    print(f\\\"\\\\n{'='*50}\\\")\\n    print(\\\"MVP Correlation Analysis Results\\\")\\n    print(f\\\"{'='*50}\\\")\\n    print(f\\\"Spearman rho:      {rho:.4f}\\\")\\n    print(f\\\"p-value:           {p_value:.2e}\\\")\\n    print(f\\\"95% CI:            [{ci[0]:.4f}, {ci[1]:.4f}]\\\")\\n    print(f\\\"Permutation p:     {perm_p:.4f}\\\")\\n    print(f\\\"N pruned heads:    {len(results)}\\\")\\n    print(f\\\"MVP Verdict:       {verdict}\\\")\\n    print(f\\\"{'='*50}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "59aed0dc-85e5-4f0f-af63-7a5215c6b28b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    for layer_idx in range(n_layers):\\\\n        n_retained = len(keep_masks[layer_idx])\\\\n        per_head = []\\\\n        for t in q_outputs[layer_idx]:\\\\n            t = t.squeeze(0)  # [seq, n_retained * head_dim]\\\\n            t = t.view(t.shape[0], n_retained, head_dim)  # [seq, n_retained, head_dim]\\\\n            t = t.mean(dim=0)  # [n_retained, head_dim]\\\\n            per_head.append(t)\\\\n        activations[layer_idx] = torch.stack(per_head, dim=0).float()\\\\n        q_outputs[layer_idx] = None\\\\n\\\\n    return activations\\\\n\\\\n\\\\ndef compute_recoverability(pruned_acts, recovered_acts, cka_data, keep_masks,\\\\n                           n_heads_original=28):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute per-pruned-head recoverability as activation shift of best retained head.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    attn_overlap = cka_data[\\\\\\\"attn_overlap\\\\\\\"]\\\\n    attn_cka_matrix = cka_data[\\\\\\\"attn_cka_matrix\\\\\\\"]\\\\n    results = []\\\\n\\\\n    for layer_idx in range(len(keep_masks)):\\\\n        retained = keep_masks[layer_idx]\\\\n        pruned_heads = sorted(set(range(n_heads_original)) - set(retained))\\\\n        if not pruned_heads:\\\\n            continue\\\\n\\\\n        cka_matrix = attn_cka_matrix[layer_idx]\\\\n\\\\n        for h_p in pruned_heads:\\\\n            sims = torch.tensor([cka_matrix[h_p, h_r].item() for h_r in retained])\\\\n            best_idx = sims.argmax().item()\\\\n            h_r = retained[best_idx]\\\\n            h_r_local = retained.index(h_r)\\\\n\\\\n            act_p = pruned_acts[layer_idx][:, h_r_local, :]\\\\n            act_r = recovered_acts[layer_idx][:, h_r_local, :]\\\\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\\\\n            activation_shift = 1.0 - cos_sim.mean().item()\\\\n\\\\n            results.append({\\\\n                \\\\\\\"layer\\\\\\\": layer_idx,\\\\n                \\\\\\\"pruned_head\\\\\\\": h_p,\\\\n                \\\\\\\"best_retained_head\\\\\\\": h_r,\\\\n                \\\\\\\"cka_overlap\\\\\\\": attn_overlap[layer_idx][h_p].item(),\\\\n                \\\\\\\"recoverability\\\\\\\": activation_shift,\\\\n                \\\\\\\"cka_similarity_to_retained\\\\\\\": sims[best_idx].item(),\\\\n            })\\\\n\\\\n    return results\\\\n\\\\n\\\\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\\\\n    rng = np.random.RandomState(seed)\\\\n    x, y = np.array(x), np.array(y)\\\\n    n = len(x)\\\\n    rhos = []\\\\n    for _ in range(n_bootstrap):\\\\n        idx = rng.choice(n, n, replace=True)\\\\n        r, _ = stats.spearmanr(x[idx], y[idx])\\\\n        if not np.isnan(r):\\\\n            rhos.append(r)\\\\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\\\\n\\\\n\\\\ndef permutation_test(x, y, n_perm=10000, seed=42):\\\\n    rng = np.random.RandomState(seed)\\\\n    x, y = np.array(x), np.array(y)\\\\n    observed, _ = stats.spearmanr(x, y)\\\\n    count = 0\\\\n    for _ in range(n_perm):\\\\n        r, _ = stats.spearmanr(x, rng.permutation(y))\\\\n        if abs(r) >= abs(observed):\\\\n            count += 1\\\\n    return count / n_perm\\\\n\\\\n\\\\ndef make_scatter_plot(results, rho, p_value, ci, perm_p, output_path):\\\\n    try:\\\\n        import matplotlib\\\\n        matplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\n        import matplotlib.pyplot as plt\\\\n    except ImportError:\\\\n        logger.warning(\\\\\\\"matplotlib not available, skipping scatter plot\\\\\\\")\\\\n        return\\\\n\\\\n    fh = [r[\\\\\\\"cka_overlap\\\\\\\"] for r in results]\\\\n    rec = [r[\\\\\\\"recoverability\\\\\\\"] for r in results]\\\\n    layers = [r[\\\\\\\"layer\\\\\\\"] for r in results]\\\\n\\\\n    fig, ax = plt.subplots(figsize=(8, 6))\\\\n    sc = ax.scatter(fh, rec, c=layers, cmap=\\\\\\\"viridis\\\\\\\", alpha=0.7,\\\\n                    edgecolors=\\\\\\\"k\\\\\\\", linewidths=0.3, s=30)\\\\n    plt.colorbar(sc, ax=ax, label=\\\\\\\"Layer index\\\\\\\")\\\\n    ax.set_xlabel(\\\\\\\"F(h_p) — CKA overlap of pruned head\\\\\\\")\\\\n    ax.set_ylabel(\\\\\\\"Recoverability — activation shift of best retained head\\\\\\\")\\\\n\\\\n    verdict = \\\\\\\"PASS\\\\\\\" if rho >= 0.4 else (\\\\\\\"WARNING\\\\\\\" if rho >= 0.3 else \\\\\\\"FAIL\\\\\\\")\\\\n    ax.set_title(\\\\n        f\\\\\\\"CKA Overlap vs RLVR Recoverability\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \\\\\\\"\\\\n        f\\\\\\\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\\\\\\\"\\\\n    )\\\\n    plt.tight_layout()\\\\n    plt.savefig(output_path, dpi=150, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.close()\\\\n    logger.info(f\\\\\\\"Scatter plot saved to {output_path}\\\\\\\")\\\\n\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(\\\\n        description=\\\\\\\"Correlation a\\\\n\\\\n... [截断: 输出过长，省略 842 字符] ...\\\\n\\\\n of calibration samples\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output_dir\\\\\\\", default=\\\\\\\"results/analysis/\\\\\\\",\\\\n                        help=\\\\\\\"Output directory\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    parser.add_argument(\\\\\\\"--dtype\\\\\\\", type=str, default=\\\\\\\"bfloat16\\\\\\\",\\\\n                        choices=[\\\\\\\"float16\\\\\\\", \\\\\\\"bfloat16\\\\\\\", \\\\\\\"float32\\\\\\\"])\\\\n    args = parser.parse_args()\\\\n\\\\n    set_seed(args.seed)\\\\n    device = torch.device(\\\\\\\"cuda\\\\\\\" if torch.cuda.is_available() else \\\\\\\"cpu\\\\\\\")\\\\n    torch_dtype = {\\\\\\\"float16\\\\\\\": torch.float16, \\\\\\\"bfloat16\\\\\\\": torch.bfloat16,\\\\n                   \\\\\\\"float32\\\\\\\": torch.float32}[args.dtype]\\\\n\\\\n    logger.info(\\\\\\\"Loading CKA scores...\\\\\\\")\\\\n    cka_data = torch.load(args.cka_scores_path, map_location=\\\\\\\"cpu\\\\\\\", weights_only=True)\\\\n    if \\\\\\\"attn_cka_matrix\\\\\\\" not in cka_data:\\\\n        raise ValueError(\\\\n            \\\\\\\"CKA scores missing 'attn_cka_matrix'. \\\\\\\"\\\\n            \\\\\\\"Re-run cka_overlap.py to generate pairwise CKA matrices.\\\\\\\"\\\\n        )\\\\n\\\\n    logger.info(\\\\\\\"Loading pruning metadata...\\\\\\\")\\\\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\\\\\\\"cpu\\\\\\\",\\\\n                              weights_only=True)\\\\n    keep_masks = pruning_meta[\\\\\\\"attn_keep_masks\\\\\\\"]\\\\n\\\\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\\\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\\\\n    logger.info(f\\\\\\\"Loaded {len(calibration_data)} calibration samples\\\\\\\")\\\\n\\\\n    logger.info(f\\\\\\\"Loading pruned model from {args.pruned_model_path}\\\\\\\")\\\\n    pruned_model = load_pruned_model(\\\\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\\\\n    )\\\\n    logger.info(\\\\\\\"Collecting activations from pruned model...\\\\\\\")\\\\n    pruned_acts = collect_retained_head_activations(\\\\n        pruned_model, calibration_data, keep_masks, device\\\\n    )\\\\n    del pruned_model\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    logger.info(f\\\\\\\"Loading recovered model from {args.recovered_model_path}\\\\\\\")\\\\n    recovered_model = load_pruned_model(\\\\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\\\\n    )\\\\n    logger.info(\\\\\\\"Collecting activations from recovered model...\\\\\\\")\\\\n    recovered_acts = collect_retained_head_activations(\\\\n        recovered_model, calibration_data, keep_masks, device\\\\n    )\\\\n    del recovered_model\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    logger.info(\\\\\\\"Computing recoverability scores...\\\\\\\")\\\\n    n_heads = 28\\\\n    results = compute_recoverability(\\\\n        pruned_acts, recovered_acts, cka_data, keep_masks, n_heads\\\\n    )\\\\n    del pruned_acts, recovered_acts\\\\n    logger.info(f\\\\\\\"Computed recoverability for {len(results)} pruned heads\\\\\\\")\\\\n\\\\n    fh = [r[\\\\\\\"cka_overlap\\\\\\\"] for r in results]\\\\n    rec = [r[\\\\\\\"recoverability\\\\\\\"] for r in results]\\\\n    rho, p_value = stats.spearmanr(fh, rec)\\\\n    ci = bootstrap_spearman(fh, rec, seed=args.seed)\\\\n    perm_p = permutation_test(fh, rec, seed=args.seed)\\\\n\\\\n    verdict = \\\\\\\"PASS\\\\\\\" if rho >= 0.4 else (\\\\\\\"WARNING\\\\\\\" if rho >= 0.3 else \\\\\\\"FAIL\\\\\\\")\\\\n\\\\n    os.makedirs(args.output_dir, exist_ok=True)\\\\n    output = {\\\\n        \\\\\\\"spearman_rho\\\\\\\": rho,\\\\n        \\\\\\\"p_value\\\\\\\": p_value,\\\\n        \\\\\\\"bootstrap_ci_95\\\\\\\": ci,\\\\n        \\\\\\\"permutation_p_value\\\\\\\": perm_p,\\\\n        \\\\\\\"n_pruned_heads\\\\\\\": len(results),\\\\n        \\\\\\\"mvp_verdict\\\\\\\": verdict,\\\\n        \\\\\\\"per_head_data\\\\\\\": results,\\\\n    }\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"correlation_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(output, f, indent=2)\\\\n    logger.info(f\\\\\\\"Results saved to {json_path}\\\\\\\")\\\\n\\\\n    plot_path = os.path.join(args.output_dir, \\\\\\\"fh_vs_recoverability.png\\\\\\\")\\\\n    make_scatter_plot(results, rho, p_value, ci, perm_p, plot_path)\\\\n\\\\n    print(f\\\\\\\"\\\\\\\\n{'='*50}\\\\\\\")\\\\n    print(\\\\\\\"MVP Correlation Analysis Results\\\\\\\")\\\\n    print(f\\\\\\\"{'='*50}\\\\\\\")\\\\n    print(f\\\\\\\"Spearman rho:      {rho:.4f}\\\\\\\")\\\\n    print(f\\\\\\\"p-value:           {p_value:.2e}\\\\\\\")\\\\n    print(f\\\\\\\"95% CI:            [{ci[0]:.4f}, {ci[1]:.4f}]\\\\\\\")\\\\n    print(f\\\\\\\"Permutation p:     {perm_p:.4f}\\\\\\\")\\\\n    print(f\\\\\\\"N pruned heads:    {len(results)}\\\\\\\")\\\\n    print(f\\\\\\\"MVP Verdict:       {verdict}\\\\\\\")\\\\n    print(f\\\\\\\"{'='*50}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    for layer_idx in range(n_layers):\\n        n_retained = len(keep_masks[layer_idx])\\n        per_head = []\\n        for t in q_outputs[layer_idx]:\\n            t = t.squeeze(0)  # [seq, n_retained * head_dim]\\n            t = t.view(t.shape[0], n_retained, head_dim)  # [seq, n_retained, head_dim]\\n            t = t.mean(dim=0)  # [n_retained, head_dim]\\n            per_head.append(t)\\n        activations[layer_idx] = torch.stack(per_head, dim=0).float()\\n        q_outputs[layer_idx] = None\\n\\n    return activations\\n\\n\\ndef compute_recoverability(pruned_acts, recovered_acts, cka_data, keep_masks,\\n                           n_heads_original=28):\\n    \\\"\\\"\\\"Compute per-pruned-head recoverability as activation shift of best retained head.\\\"\\\"\\\"\\n    attn_overlap = cka_data[\\\"attn_overlap\\\"]\\n    attn_cka_matrix = cka_data[\\\"attn_cka_matrix\\\"]\\n    results = []\\n\\n    for layer_idx in range(len(keep_masks)):\\n        retained = keep_masks[layer_idx]\\n        pruned_heads = sorted(set(range(n_heads_original)) - set(retained))\\n        if not pruned_heads:\\n            continue\\n\\n        cka_matrix = attn_cka_matrix[layer_idx]\\n\\n        for h_p in pruned_heads:\\n            sims = torch.tensor([cka_matrix[h_p, h_r].item() for h_r in retained])\\n            best_idx = sims.argmax().item()\\n            h_r = retained[best_idx]\\n            h_r_local = retained.index(h_r)\\n\\n            act_p = pruned_acts[layer_idx][:, h_r_local, :]\\n            act_r = recovered_acts[layer_idx][:, h_r_local, :]\\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\\n            activation_shift = 1.0 - cos_sim.mean().item()\\n\\n            results.append({\\n                \\\"layer\\\": layer_idx,\\n                \\\"pruned_head\\\": h_p,\\n                \\\"best_retained_head\\\": h_r,\\n                \\\"cka_overlap\\\": attn_overlap[layer_idx][h_p].item(),\\n                \\\"recoverability\\\": activation_shift,\\n                \\\"cka_similarity_to_retained\\\": sims[best_idx].item(),\\n            })\\n\\n    return results\\n\\n\\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    x, y = np.array(x), np.array(y)\\n    n = len(x)\\n    rhos = []\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        r, _ = stats.spearmanr(x[idx], y[idx])\\n        if not np.isnan(r):\\n            rhos.append(r)\\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\\n\\n\\ndef permutation_test(x, y, n_perm=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    x, y = np.array(x), np.array(y)\\n    observed, _ = stats.spearmanr(x, y)\\n    count = 0\\n    for _ in range(n_perm):\\n        r, _ = stats.spearmanr(x, rng.permutation(y))\\n        if abs(r) >= abs(observed):\\n            count += 1\\n    return count / n_perm\\n\\n\\ndef make_scatter_plot(results, rho, p_value, ci, perm_p, output_path):\\n    try:\\n        import matplotlib\\n        matplotlib.use(\\\"Agg\\\")\\n        import matplotlib.pyplot as plt\\n    except ImportError:\\n        logger.warning(\\\"matplotlib not available, skipping scatter plot\\\")\\n        return\\n\\n    fh = [r[\\\"cka_overlap\\\"] for r in results]\\n    rec = [r[\\\"recoverability\\\"] for r in results]\\n    layers = [r[\\\"layer\\\"] for r in results]\\n\\n    fig, ax = plt.subplots(figsize=(8, 6))\\n    sc = ax.scatter(fh, rec, c=layers, cmap=\\\"viridis\\\", alpha=0.7,\\n                    edgecolors=\\\"k\\\", linewidths=0.3, s=30)\\n    plt.colorbar(sc, ax=ax, label=\\\"Layer index\\\")\\n    ax.set_xlabel(\\\"F(h_p) — CKA overlap of pruned head\\\")\\n    ax.set_ylabel(\\\"Recoverability — activation shift of best retained head\\\")\\n\\n    verdict = \\\"PASS\\\" if rho >= 0.4 else (\\\"WARNING\\\" if rho >= 0.3 else \\\"FAIL\\\")\\n    ax.set_title(\\n        f\\\"CKA Overlap vs RLVR Recoverability\\\\n\\\"\\n        f\\\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \\\"\\n        f\\\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\\\"\\n    )\\n    plt.tight_layout()\\n    plt.savefig(output_path, dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n    logger.info(f\\\"Scatter plot saved to {output_path}\\\")\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Correlation a\\n\\n... [截断: 输出过长，省略 842 字符] ...\\n\\n of calibration samples\\\")\\n    parser.add_argument(\\\"--output_dir\\\", default=\\\"results/analysis/\\\",\\n                        help=\\\"Output directory\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42)\\n    parser.add_argument(\\\"--dtype\\\", type=str, default=\\\"bfloat16\\\",\\n                        choices=[\\\"float16\\\", \\\"bfloat16\\\", \\\"float32\\\"])\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(\\\"cuda\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    torch_dtype = {\\\"float16\\\": torch.float16, \\\"bfloat16\\\": torch.bfloat16,\\n                   \\\"float32\\\": torch.float32}[args.dtype]\\n\\n    logger.info(\\\"Loading CKA scores...\\\")\\n    cka_data = torch.load(args.cka_scores_path, map_location=\\\"cpu\\\", weights_only=True)\\n    if \\\"attn_cka_matrix\\\" not in cka_data:\\n        raise ValueError(\\n            \\\"CKA scores missing 'attn_cka_matrix'. \\\"\\n            \\\"Re-run cka_overlap.py to generate pairwise CKA matrices.\\\"\\n        )\\n\\n    logger.info(\\\"Loading pruning metadata...\\\")\\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\\\"cpu\\\",\\n                              weights_only=True)\\n    keep_masks = pruning_meta[\\\"attn_keep_masks\\\"]\\n\\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\\n    logger.info(f\\\"Loaded {len(calibration_data)} calibration samples\\\")\\n\\n    logger.info(f\\\"Loading pruned model from {args.pruned_model_path}\\\")\\n    pruned_model = load_pruned_model(\\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\\n    )\\n    logger.info(\\\"Collecting activations from pruned model...\\\")\\n    pruned_acts = collect_retained_head_activations(\\n        pruned_model, calibration_data, keep_masks, device\\n    )\\n    del pruned_model\\n    torch.cuda.empty_cache()\\n\\n    logger.info(f\\\"Loading recovered model from {args.recovered_model_path}\\\")\\n    recovered_model = load_pruned_model(\\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\\n    )\\n    logger.info(\\\"Collecting activations from recovered model...\\\")\\n    recovered_acts = collect_retained_head_activations(\\n        recovered_model, calibration_data, keep_masks, device\\n    )\\n    del recovered_model\\n    torch.cuda.empty_cache()\\n\\n    logger.info(\\\"Computing recoverability scores...\\\")\\n    n_heads = 28\\n    results = compute_recoverability(\\n        pruned_acts, recovered_acts, cka_data, keep_masks, n_heads\\n    )\\n    del pruned_acts, recovered_acts\\n    logger.info(f\\\"Computed recoverability for {len(results)} pruned heads\\\")\\n\\n    fh = [r[\\\"cka_overlap\\\"] for r in results]\\n    rec = [r[\\\"recoverability\\\"] for r in results]\\n    rho, p_value = stats.spearmanr(fh, rec)\\n    ci = bootstrap_spearman(fh, rec, seed=args.seed)\\n    perm_p = permutation_test(fh, rec, seed=args.seed)\\n\\n    verdict = \\\"PASS\\\" if rho >= 0.4 else (\\\"WARNING\\\" if rho >= 0.3 else \\\"FAIL\\\")\\n\\n    os.makedirs(args.output_dir, exist_ok=True)\\n    output = {\\n        \\\"spearman_rho\\\": rho,\\n        \\\"p_value\\\": p_value,\\n        \\\"bootstrap_ci_95\\\": ci,\\n        \\\"permutation_p_value\\\": perm_p,\\n        \\\"n_pruned_heads\\\": len(results),\\n        \\\"mvp_verdict\\\": verdict,\\n        \\\"per_head_data\\\": results,\\n    }\\n    json_path = os.path.join(args.output_dir, \\\"correlation_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2)\\n    logger.info(f\\\"Results saved to {json_path}\\\")\\n\\n    plot_path = os.path.join(args.output_dir, \\\"fh_vs_recoverability.png\\\")\\n    make_scatter_plot(results, rho, p_value, ci, perm_p, plot_path)\\n\\n    print(f\\\"\\\\n{'='*50}\\\")\\n    print(\\\"MVP Correlation Analysis Results\\\")\\n    print(f\\\"{'='*50}\\\")\\n    print(f\\\"Spearman rho:      {rho:.4f}\\\")\\n    print(f\\\"p-value:           {p_value:.2e}\\\")\\n    print(f\\\"95% CI:            [{ci[0]:.4f}, {ci[1]:.4f}]\\\")\\n    print(f\\\"Permutation p:     {perm_p:.4f}\\\")\\n    print(f\\\"N pruned heads:    {len(results)}\\\")\\n    print(f\\\"MVP Verdict:       {verdict}\\\")\\n    print(f\\\"{'='*50}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"
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
Now let me also read importance_score.py to understand MLP group size configuration, and the truncated middle of prune.py.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "6c13475c-10a2-4704-aec1-a7987b3c918f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYdZYVpLWrz5dqXHhB5PMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3671,
      "cache_read_input_tokens": 48530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3671
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MjSz8wUBR2nUAMn2XfRJfC`</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/recovery_aware_struct_prune/src/importance_score.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "54bb4e7a-6d20-4300-ba32-91afb496fc0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYdZYVpLWrz5dqXHhB5PMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3671,
      "cache_read_input_tokens": 48530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3671
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

_source line 47 · 2026-05-14T05:29:31.212Z_

<details><summary>↩ Tool result · `toolu_01MjSz8wUBR2nUAMn2XfRJfC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nGradient-based Importance Scoring for structured pruning.\\n\\nComputes Taylor-expansion importance I(g) = ||w * grad||_2 for each\\nGQA group and MLP channel group on calibration data.\\n\\nGQA group importance = sum of Q head importances (q_proj + o_proj) + KV head importance (k_proj + v_proj).\\n\\nInput:  model + calibration data (GSM8K train subset)\\nOutput: per-structure I(g) scores saved as dict in .pt file\\n        Keys: 'attn_importance' (dict[layer_idx -> tensor[n_kv_heads]]),\\n              'mlp_importance'  (dict[layer_idx -> tensor[n_mlp_groups]])\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    \\\"\\\"\\\"Load GSM8K train questions as calibration prompts with labels for loss computation.\\\"\\\"\\\"\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n\\n    encodings = []\\n    for example in ds:\\n        text = f\\\"Question: {example['question']}\\\\nAnswer: {example['answer']}\\\"\\n        ids = tokenizer(text, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef compute_importance(model, calibration_data, device):\\n    \\\"\\\"\\\"Compute gradient-based importance for GQA groups and MLP groups.\\n\\n    GQA group importance = sum(Q head Taylor scores) + KV head Taylor score.\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_layers = config.num_hidden_layers\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n    intermediate_size = config.intermediate_size\\n    n_mlp_groups = n_heads\\n    mlp_group_size = intermediate_size // n_mlp_groups\\n\\n    q_importance = {i: torch.zeros(n_heads, device=\\\"cpu\\\") for i in range(n_layers)}\\n    kv_importance = {i: torch.zeros(n_kv_heads, device=\\\"cpu\\\") for i in range(n_layers)}\\n    mlp_importance = {i: torch.zeros(n_mlp_groups, device=\\\"cpu\\\") for i in range(n_layers)}\\n\\n    model.train()\\n\\n    for batch_idx, enc in enumerate(calibration_data):\\n        input_ids = enc[\\\"input_ids\\\"].to(device)\\n        attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n        labels = input_ids.clone()\\n\\n        model.zero_grad()\\n        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)\\n        loss = outputs.loss\\n        loss.backward()\\n\\n        with torch.no_grad():\\n            for layer_idx in range(n_layers):\\n                layer = model.model.layers[layer_idx]\\n\\n                # Q head importance via q_proj: [n_heads*head_dim, hidden]\\n                q_weight = layer.self_attn.q_proj.weight\\n                q_grad = layer.self_attn.q_proj.weight.grad\\n                if q_grad is not None:\\n                    w = q_weight.view(n_heads, head_dim, -1)\\n                    g = q_grad.view(n_heads, head_dim, -1)\\n                    taylor = (w * g).float()\\n                    head_scores = taylor.view(n_heads, -1).norm(dim=1)\\n                    q_importance[layer_idx] += head_scores.cpu()\\n\\n                # Q head importance via o_proj: [hidden, n_heads*head_dim]\\n                o_w = layer.self_attn.o_proj.weight\\n                o_g = layer.self_attn.o_proj.weight.grad\\n                if o_g is not None:\\n                    w_r = o_w.view(-1, n_heads, head_dim)\\n                    g_r = o_g.view(-1, n_heads, head_dim)\\n                    taylor = (w_r * g_r).float()\\n                    head_scores = taylor.permute(1, 0, 2).reshape(n_heads, -1).norm(dim=1)\\n                    \\n\\n... [截断: 输出过长，省略 1634 字符] ...\\n\\n                    g_r = up_g[:usable].view(n_mlp_groups, mlp_group_size, -1)\\n                    taylor = (w_r * g_r).float()\\n                    group_scores = taylor.view(n_mlp_groups, -1).norm(dim=1)\\n                    mlp_importance[layer_idx] += group_scores.cpu()\\n\\n                # MLP importance via down_proj: [hidden, intermediate]\\n                down_w = layer.mlp.down_proj.weight\\n                down_g = layer.mlp.down_proj.weight.grad\\n                if down_g is not None:\\n                    usable = n_mlp_groups * mlp_group_size\\n                    w_r = down_w[:, :usable].view(-1, n_mlp_groups, mlp_group_size)\\n                    g_r = down_g[:, :usable].view(-1, n_mlp_groups, mlp_group_size)\\n                    taylor = (w_r * g_r).float()\\n                    group_scores = taylor.permute(1, 0, 2).reshape(n_mlp_groups, -1).norm(dim=1)\\n                    mlp_importance[layer_idx] += group_scores.cpu()\\n\\n        if (batch_idx + 1) % 50 == 0:\\n            logger.info(f\\\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\\\")\\n\\n    # Average over samples, then aggregate Q heads to GQA groups\\n    n = len(calibration_data)\\n    attn_importance = {}\\n    for layer_idx in range(n_layers):\\n        q_importance[layer_idx] /= n\\n        kv_importance[layer_idx] /= n\\n        mlp_importance[layer_idx] /= n\\n\\n        q_grouped = q_importance[layer_idx].view(n_kv_heads, heads_per_kv).sum(dim=1)\\n        attn_importance[layer_idx] = q_grouped + kv_importance[layer_idx]\\n\\n    return attn_importance, mlp_importance\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Compute gradient-based importance scores for RASP\\\")\\n    parser.add_argument(\\\"--model_path\\\", type=str, required=True, help=\\\"Path to pretrained model\\\")\\n    parser.add_argument(\\\"--output_path\\\", type=str, required=True, help=\\\"Output .pt file for importance scores\\\")\\n    parser.add_argument(\\\"--n_samples\\\", type=int, default=512, help=\\\"Number of calibration samples\\\")\\n    parser.add_argument(\\\"--max_length\\\", type=int, default=512, help=\\\"Max token length for calibration inputs\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--dtype\\\", type=str, default=\\\"bfloat16\\\", choices=[\\\"float16\\\", \\\"bfloat16\\\", \\\"float32\\\"])\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(\\\"cuda\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    dtype_map = {\\\"float16\\\": torch.float16, \\\"bfloat16\\\": torch.bfloat16, \\\"float32\\\": torch.float32}\\n    torch_dtype = dtype_map[args.dtype]\\n\\n    logger.info(f\\\"Loading model from {args.model_path}\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        args.model_path,\\n        torch_dtype=torch_dtype,\\n        device_map=device,\\n        trust_remote_code=True,\\n    )\\n\\n    n_kv_heads = model.config.num_key_value_heads\\n    heads_per_kv = model.config.num_attention_heads // n_kv_heads\\n    logger.info(f\\\"GQA config: {n_kv_heads} KV heads, {heads_per_kv} Q heads per group\\\")\\n\\n    logger.info(f\\\"Loading {args.n_samples} calibration samples\\\")\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\\n\\n    logger.info(\\\"Computing gradient-based importance scores...\\\")\\n    attn_importance, mlp_importance = compute_importance(model, calibration_data, device)\\n\\n    for layer_idx in range(model.config.num_hidden_layers):\\n        a = attn_importance[layer_idx]\\n        m = mlp_importance[layer_idx]\\n        logger.info(\\n            f\\\"  Layer {layer_idx}: attn GQA groups [{a.min():.6f}, {a.max():.6f}] (shape={a.shape}), \\\"\\n            f\\\"mlp [{m.min():.6f}, {m.max():.6f}]\\\"\\n        )\\n\\n    os.makedirs(os.path.dirname(args.output_path) or \\\".\\\", exist_ok=True)\\n    result = {\\\"attn_importance\\\": attn_importance, \\\"mlp_importance\\\": mlp_importance}\\n    torch.save(result, args.output_path)\\n    logger.info(f\\\"Saved importance scores to {args.output_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "f5f713c0-a9d1-4c99-8070-cf92b30e0b28",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nGradient-based Importance Scoring for structured pruning.\\\\n\\\\nComputes Taylor-expansion importance I(g) = ||w * grad||_2 for each\\\\nGQA group and MLP channel group on calibration data.\\\\n\\\\nGQA group importance = sum of Q head importances (q_proj + o_proj) + KV head importance (k_proj + v_proj).\\\\n\\\\nInput:  model + calibration data (GSM8K train subset)\\\\nOutput: per-structure I(g) scores saved as dict in .pt file\\\\n        Keys: 'attn_importance' (dict[layer_idx -> tensor[n_kv_heads]]),\\\\n              'mlp_importance'  (dict[layer_idx -> tensor[n_mlp_groups]])\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport logging\\\\nimport os\\\\nimport random\\\\n\\\\nimport numpy as np\\\\nimport torch\\\\nfrom datasets import load_dataset\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n)\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n\\\\ndef set_seed(seed: int):\\\\n    random.seed(seed)\\\\n    np.random.seed(seed)\\\\n    torch.manual_seed(seed)\\\\n    torch.cuda.manual_seed_all(seed)\\\\n\\\\n\\\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load GSM8K train questions as calibration prompts with labels for loss computation.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    ds = load_dataset(\\\\\\\"openai/gsm8k\\\\\\\", \\\\\\\"main\\\\\\\", split=\\\\\\\"train\\\\\\\")\\\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\\\n\\\\n    encodings = []\\\\n    for example in ds:\\\\n        text = f\\\\\\\"Question: {example['question']}\\\\\\\\nAnswer: {example['answer']}\\\\\\\"\\\\n        ids = tokenizer(text, return_tensors=\\\\\\\"pt\\\\\\\", truncation=True, max_length=max_length)\\\\n        encodings.append(ids)\\\\n    return encodings\\\\n\\\\n\\\\ndef compute_importance(model, calibration_data, device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute gradient-based importance for GQA groups and MLP groups.\\\\n\\\\n    GQA group importance = sum(Q head Taylor scores) + KV head Taylor score.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    config = model.config\\\\n    n_layers = config.num_hidden_layers\\\\n    n_heads = config.num_attention_heads\\\\n    n_kv_heads = config.num_key_value_heads\\\\n    head_dim = config.hidden_size // n_heads\\\\n    heads_per_kv = n_heads // n_kv_heads\\\\n    intermediate_size = config.intermediate_size\\\\n    n_mlp_groups = n_heads\\\\n    mlp_group_size = intermediate_size // n_mlp_groups\\\\n\\\\n    q_importance = {i: torch.zeros(n_heads, device=\\\\\\\"cpu\\\\\\\") for i in range(n_layers)}\\\\n    kv_importance = {i: torch.zeros(n_kv_heads, device=\\\\\\\"cpu\\\\\\\") for i in range(n_layers)}\\\\n    mlp_importance = {i: torch.zeros(n_mlp_groups, device=\\\\\\\"cpu\\\\\\\") for i in range(n_layers)}\\\\n\\\\n    model.train()\\\\n\\\\n    for batch_idx, enc in enumerate(calibration_data):\\\\n        input_ids = enc[\\\\\\\"input_ids\\\\\\\"].to(device)\\\\n        attention_mask = enc[\\\\\\\"attention_mask\\\\\\\"].to(device)\\\\n        labels = input_ids.clone()\\\\n\\\\n        model.zero_grad()\\\\n        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)\\\\n        loss = outputs.loss\\\\n        loss.backward()\\\\n\\\\n        with torch.no_grad():\\\\n            for layer_idx in range(n_layers):\\\\n                layer = model.model.layers[layer_idx]\\\\n\\\\n                # Q head importance via q_proj: [n_heads*head_dim, hidden]\\\\n                q_weight = layer.self_attn.q_proj.weight\\\\n                q_grad = layer.self_attn.q_proj.weight.grad\\\\n                if q_grad is not None:\\\\n                    w = q_weight.view(n_heads, head_dim, -1)\\\\n                    g = q_grad.view(n_heads, head_dim, -1)\\\\n                    taylor = (w * g).float()\\\\n                    head_scores = taylor.view(n_heads, -1).norm(dim=1)\\\\n                    q_importance[layer_idx] += head_scores.cpu()\\\\n\\\\n                # Q head importance via o_proj: [hidden, n_heads*head_dim]\\\\n                o_w = layer.self_attn.o_proj.weight\\\\n                o_g = layer.self_attn.o_proj.weight.grad\\\\n                if o_g is not None:\\\\n                    w_r = o_w.view(-1, n_heads, head_dim)\\\\n                    g_r = o_g.view(-1, n_heads, head_dim)\\\\n                    taylor = (w_r * g_r).float()\\\\n                    head_scores = taylor.permute(1, 0, 2).reshape(n_heads, -1).norm(dim=1)\\\\n                    \\\\n\\\\n... [截断: 输出过长，省略 1634 字符] ...\\\\n\\\\n                    g_r = up_g[:usable].view(n_mlp_groups, mlp_group_size, -1)\\\\n                    taylor = (w_r * g_r).float()\\\\n                    group_scores = taylor.view(n_mlp_groups, -1).norm(dim=1)\\\\n                    mlp_importance[layer_idx] += group_scores.cpu()\\\\n\\\\n                # MLP importance via down_proj: [hidden, intermediate]\\\\n                down_w = layer.mlp.down_proj.weight\\\\n                down_g = layer.mlp.down_proj.weight.grad\\\\n                if down_g is not None:\\\\n                    usable = n_mlp_groups * mlp_group_size\\\\n                    w_r = down_w[:, :usable].view(-1, n_mlp_groups, mlp_group_size)\\\\n                    g_r = down_g[:, :usable].view(-1, n_mlp_groups, mlp_group_size)\\\\n                    taylor = (w_r * g_r).float()\\\\n                    group_scores = taylor.permute(1, 0, 2).reshape(n_mlp_groups, -1).norm(dim=1)\\\\n                    mlp_importance[layer_idx] += group_scores.cpu()\\\\n\\\\n        if (batch_idx + 1) % 50 == 0:\\\\n            logger.info(f\\\\\\\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\\\\\\\")\\\\n\\\\n    # Average over samples, then aggregate Q heads to GQA groups\\\\n    n = len(calibration_data)\\\\n    attn_importance = {}\\\\n    for layer_idx in range(n_layers):\\\\n        q_importance[layer_idx] /= n\\\\n        kv_importance[layer_idx] /= n\\\\n        mlp_importance[layer_idx] /= n\\\\n\\\\n        q_grouped = q_importance[layer_idx].view(n_kv_heads, heads_per_kv).sum(dim=1)\\\\n        attn_importance[layer_idx] = q_grouped + kv_importance[layer_idx]\\\\n\\\\n    return attn_importance, mlp_importance\\\\n\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(description=\\\\\\\"Compute gradient-based importance scores for RASP\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--model_path\\\\\\\", type=str, required=True, help=\\\\\\\"Path to pretrained model\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output_path\\\\\\\", type=str, required=True, help=\\\\\\\"Output .pt file for importance scores\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--n_samples\\\\\\\", type=int, default=512, help=\\\\\\\"Number of calibration samples\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--max_length\\\\\\\", type=int, default=512, help=\\\\\\\"Max token length for calibration inputs\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42, help=\\\\\\\"Random seed\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--dtype\\\\\\\", type=str, default=\\\\\\\"bfloat16\\\\\\\", choices=[\\\\\\\"float16\\\\\\\", \\\\\\\"bfloat16\\\\\\\", \\\\\\\"float32\\\\\\\"])\\\\n    args = parser.parse_args()\\\\n\\\\n    set_seed(args.seed)\\\\n    device = torch.device(\\\\\\\"cuda\\\\\\\" if torch.cuda.is_available() else \\\\\\\"cpu\\\\\\\")\\\\n    dtype_map = {\\\\\\\"float16\\\\\\\": torch.float16, \\\\\\\"bfloat16\\\\\\\": torch.bfloat16, \\\\\\\"float32\\\\\\\": torch.float32}\\\\n    torch_dtype = dtype_map[args.dtype]\\\\n\\\\n    logger.info(f\\\\\\\"Loading model from {args.model_path}\\\\\\\")\\\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\\\n    model = AutoModelForCausalLM.from_pretrained(\\\\n        args.model_path,\\\\n        torch_dtype=torch_dtype,\\\\n        device_map=device,\\\\n        trust_remote_code=True,\\\\n    )\\\\n\\\\n    n_kv_heads = model.config.num_key_value_heads\\\\n    heads_per_kv = model.config.num_attention_heads // n_kv_heads\\\\n    logger.info(f\\\\\\\"GQA config: {n_kv_heads} KV heads, {heads_per_kv} Q heads per group\\\\\\\")\\\\n\\\\n    logger.info(f\\\\\\\"Loading {args.n_samples} calibration samples\\\\\\\")\\\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\\\\n\\\\n    logger.info(\\\\\\\"Computing gradient-based importance scores...\\\\\\\")\\\\n    attn_importance, mlp_importance = compute_importance(model, calibration_data, device)\\\\n\\\\n    for layer_idx in range(model.config.num_hidden_layers):\\\\n        a = attn_importance[layer_idx]\\\\n        m = mlp_importance[layer_idx]\\\\n        logger.info(\\\\n            f\\\\\\\"  Layer {layer_idx}: attn GQA groups [{a.min():.6f}, {a.max():.6f}] (shape={a.shape}), \\\\\\\"\\\\n            f\\\\\\\"mlp [{m.min():.6f}, {m.max():.6f}]\\\\\\\"\\\\n        )\\\\n\\\\n    os.makedirs(os.path.dirname(args.output_path) or \\\\\\\".\\\\\\\", exist_ok=True)\\\\n    result = {\\\\\\\"attn_importance\\\\\\\": attn_importance, \\\\\\\"mlp_importance\\\\\\\": mlp_importance}\\\\n    torch.save(result, args.output_path)\\\\n    logger.info(f\\\\\\\"Saved importance scores to {args.output_path}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nGradient-based Importance Scoring for structured pruning.\\n\\nComputes Taylor-expansion importance I(g) = ||w * grad||_2 for each\\nGQA group and MLP channel group on calibration data.\\n\\nGQA group importance = sum of Q head importances (q_proj + o_proj) + KV head importance (k_proj + v_proj).\\n\\nInput:  model + calibration data (GSM8K train subset)\\nOutput: per-structure I(g) scores saved as dict in .pt file\\n        Keys: 'attn_importance' (dict[layer_idx -> tensor[n_kv_heads]]),\\n              'mlp_importance'  (dict[layer_idx -> tensor[n_mlp_groups]])\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    \\\"\\\"\\\"Load GSM8K train questions as calibration prompts with labels for loss computation.\\\"\\\"\\\"\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n\\n    encodings = []\\n    for example in ds:\\n        text = f\\\"Question: {example['question']}\\\\nAnswer: {example['answer']}\\\"\\n        ids = tokenizer(text, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef compute_importance(model, calibration_data, device):\\n    \\\"\\\"\\\"Compute gradient-based importance for GQA groups and MLP groups.\\n\\n    GQA group importance = sum(Q head Taylor scores) + KV head Taylor score.\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_layers = config.num_hidden_layers\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n    intermediate_size = config.intermediate_size\\n    n_mlp_groups = n_heads\\n    mlp_group_size = intermediate_size // n_mlp_groups\\n\\n    q_importance = {i: torch.zeros(n_heads, device=\\\"cpu\\\") for i in range(n_layers)}\\n    kv_importance = {i: torch.zeros(n_kv_heads, device=\\\"cpu\\\") for i in range(n_layers)}\\n    mlp_importance = {i: torch.zeros(n_mlp_groups, device=\\\"cpu\\\") for i in range(n_layers)}\\n\\n    model.train()\\n\\n    for batch_idx, enc in enumerate(calibration_data):\\n        input_ids = enc[\\\"input_ids\\\"].to(device)\\n        attention_mask = enc[\\\"attention_mask\\\"].to(device)\\n        labels = input_ids.clone()\\n\\n        model.zero_grad()\\n        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)\\n        loss = outputs.loss\\n        loss.backward()\\n\\n        with torch.no_grad():\\n            for layer_idx in range(n_layers):\\n                layer = model.model.layers[layer_idx]\\n\\n                # Q head importance via q_proj: [n_heads*head_dim, hidden]\\n                q_weight = layer.self_attn.q_proj.weight\\n                q_grad = layer.self_attn.q_proj.weight.grad\\n                if q_grad is not None:\\n                    w = q_weight.view(n_heads, head_dim, -1)\\n                    g = q_grad.view(n_heads, head_dim, -1)\\n                    taylor = (w * g).float()\\n                    head_scores = taylor.view(n_heads, -1).norm(dim=1)\\n                    q_importance[layer_idx] += head_scores.cpu()\\n\\n                # Q head importance via o_proj: [hidden, n_heads*head_dim]\\n                o_w = layer.self_attn.o_proj.weight\\n                o_g = layer.self_attn.o_proj.weight.grad\\n                if o_g is not None:\\n                    w_r = o_w.view(-1, n_heads, head_dim)\\n                    g_r = o_g.view(-1, n_heads, head_dim)\\n                    taylor = (w_r * g_r).float()\\n                    head_scores = taylor.permute(1, 0, 2).reshape(n_heads, -1).norm(dim=1)\\n                    \\n\\n... [截断: 输出过长，省略 1634 字符] ...\\n\\n                    g_r = up_g[:usable].view(n_mlp_groups, mlp_group_size, -1)\\n                    taylor = (w_r * g_r).float()\\n                    group_scores = taylor.view(n_mlp_groups, -1).norm(dim=1)\\n                    mlp_importance[layer_idx] += group_scores.cpu()\\n\\n                # MLP importance via down_proj: [hidden, intermediate]\\n                down_w = layer.mlp.down_proj.weight\\n                down_g = layer.mlp.down_proj.weight.grad\\n                if down_g is not None:\\n                    usable = n_mlp_groups * mlp_group_size\\n                    w_r = down_w[:, :usable].view(-1, n_mlp_groups, mlp_group_size)\\n                    g_r = down_g[:, :usable].view(-1, n_mlp_groups, mlp_group_size)\\n                    taylor = (w_r * g_r).float()\\n                    group_scores = taylor.permute(1, 0, 2).reshape(n_mlp_groups, -1).norm(dim=1)\\n                    mlp_importance[layer_idx] += group_scores.cpu()\\n\\n        if (batch_idx + 1) % 50 == 0:\\n            logger.info(f\\\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\\\")\\n\\n    # Average over samples, then aggregate Q heads to GQA groups\\n    n = len(calibration_data)\\n    attn_importance = {}\\n    for layer_idx in range(n_layers):\\n        q_importance[layer_idx] /= n\\n        kv_importance[layer_idx] /= n\\n        mlp_importance[layer_idx] /= n\\n\\n        q_grouped = q_importance[layer_idx].view(n_kv_heads, heads_per_kv).sum(dim=1)\\n        attn_importance[layer_idx] = q_grouped + kv_importance[layer_idx]\\n\\n    return attn_importance, mlp_importance\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Compute gradient-based importance scores for RASP\\\")\\n    parser.add_argument(\\\"--model_path\\\", type=str, required=True, help=\\\"Path to pretrained model\\\")\\n    parser.add_argument(\\\"--output_path\\\", type=str, required=True, help=\\\"Output .pt file for importance scores\\\")\\n    parser.add_argument(\\\"--n_samples\\\", type=int, default=512, help=\\\"Number of calibration samples\\\")\\n    parser.add_argument(\\\"--max_length\\\", type=int, default=512, help=\\\"Max token length for calibration inputs\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--dtype\\\", type=str, default=\\\"bfloat16\\\", choices=[\\\"float16\\\", \\\"bfloat16\\\", \\\"float32\\\"])\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(\\\"cuda\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    dtype_map = {\\\"float16\\\": torch.float16, \\\"bfloat16\\\": torch.bfloat16, \\\"float32\\\": torch.float32}\\n    torch_dtype = dtype_map[args.dtype]\\n\\n    logger.info(f\\\"Loading model from {args.model_path}\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        args.model_path,\\n        torch_dtype=torch_dtype,\\n        device_map=device,\\n        trust_remote_code=True,\\n    )\\n\\n    n_kv_heads = model.config.num_key_value_heads\\n    heads_per_kv = model.config.num_attention_heads // n_kv_heads\\n    logger.info(f\\\"GQA config: {n_kv_heads} KV heads, {heads_per_kv} Q heads per group\\\")\\n\\n    logger.info(f\\\"Loading {args.n_samples} calibration samples\\\")\\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\\n\\n    logger.info(\\\"Computing gradient-based importance scores...\\\")\\n    attn_importance, mlp_importance = compute_importance(model, calibration_data, device)\\n\\n    for layer_idx in range(model.config.num_hidden_layers):\\n        a = attn_importance[layer_idx]\\n        m = mlp_importance[layer_idx]\\n        logger.info(\\n            f\\\"  Layer {layer_idx}: attn GQA groups [{a.min():.6f}, {a.max():.6f}] (shape={a.shape}), \\\"\\n            f\\\"mlp [{m.min():.6f}, {m.max():.6f}]\\\"\\n        )\\n\\n    os.makedirs(os.path.dirname(args.output_path) or \\\".\\\", exist_ok=True)\\n    result = {\\\"attn_importance\\\": attn_importance, \\\"mlp_importance\\\": mlp_importance}\\n    torch.save(result, args.output_path)\\n    logger.info(f\\\"Saved importance scores to {args.output_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"
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
Now I have a complete picture of all four files. Let me summarize what I know:

**cka_overlap.py**: 
- Already has `mlp_cka_matrix` in output ✓
- MLP groups: `n_groups` (default 28), `group_size = intermediate_size // n_groups`

**importance_score.py**:
- `n_mlp_groups = n_heads` (= 28 for Qwen2.5-7B)


- `mlp_group_size = intermediate_size // n_mlp_groups`

**prune.py**:
- Already saves `mlp_keep_masks` in `pruning_metadata.pt` ✓
- `prune_mlp_channels(model, mlp_keep_masks, n_mlp_groups=28)`

**correlation_analysis.py** (current state):
- Only handles attention-level recoverability
- `load_pruned_model` already calls both `prune_attention_heads` and `prune_mlp_channels` ✓
- Needs MLP-level analysis added

So I need to add MLP-level recoverability analysis to correlation_analysis.py, computing how well the pruned MLP channels can be recovered from the CKA overlap matrix, similar to what's already done for attention heads. I need to carefully handle how the pruned model's MLP activations are structured—since channels have already been removed, the gate_proj output will only contain the retained groups, so I'll need to reshape and aggregate those activations appropriately before computing recoverability metrics. I need to write the file locally first, then push it to the server via SSH. Let me trace through the current correlation_analysis.py flow more carefully—I'm loading CKA and pruning metadata, then collecting activations from both pruned and recovered models separately before computing recoverability metrics. I'll need to restructure this to gather both attention and MLP activations together from the pruned model before moving on.

Actually, the simpler approach is to load the pruned model once and run two separate forward passes on it—one for attention activations and one for MLP activations—then repeat that pattern for the recovered model. This avoids the overhead of loading the model multiple times while keeping the code changes manageable.

But I could be even more efficient by combining both hooks in a single forward pass. Let me write a unified function that registers hooks for both attention and MLP layers simultaneously, collects both activation sets in one pass, and returns them together.

Writing the combined activation collection function...

Actually, I need to think through the reshaping logic more carefully. For the MLP gate projections in the pruned model, the output will have shape `[batch, seq, n_retained_groups * group_size]`, and I need to reshape that back to `[batch, seq, n_retained_groups, group_size]` to properly align with the group structure.

The key insight is that `n_mlp_groups_original` is 28, and after pruning at each layer, I only have the retained groups specified in `mlp_keep_masks[i]`. The `group_size` is just the original intermediate size divided by 28. So I can compute the number of retained groups and reshape accordingly to get per-group activations, then mean-pool over the sequence dimension.

Now I'm writing the full updated correlation analysis file... Setting up the logger and defining utility functions to seed randomness across libraries and load calibration data from the GSM8K dataset by tokenizing question prompts.

Now I'm writing a function to load a structurally pruned model by reconstructing it from a base model and applying saved pruning masks to attention heads and MLP channels.

Loading the pruned weights... Still writing the hook logic... Continuing to set up the hook function that captures gate projection outputs, then registering hooks on each layer's MLP gate projection and running the model through calibration data to collect activations, logging progress every 50 samples.

Now I'm processing the collected gate outputs by inferring the group size from the tensor shape, reshaping and averaging the activations across samples to get per-group statistics for each layer, then storing these as float tensors in the activations dictionary.

I'm moving on to define a function that computes recoverability metrics for pruned attention heads by comparing their similarity to retained heads using CKA matrices, iterating through each layer to identify which heads were pruned and calculating activation shifts for the best-matching retained head. Still writing analysis code... I'm finishing up the results dictionary with the CKA overlap and recoverability metrics, then returning the full list. After that, I'm implementing a bootstrap function to compute confidence intervals for Spearman correlation coefficients by resampling the data multiple times and calculating the percentiles.

Now I'm adding a permutation test to assess statistical significance by shuffling one variable and counting how often the correlation is as extreme as the observed value. Then I'm starting a stats computation function that will tie these together to calculate the correlation, confidence interval, and p-value for pairs of overlap and recoverability measurements. Writing the scatter plot function... Finishing the axis labels and adding the statistical verdict to the title — I'm setting it to PASS, WARNING, or FAIL based on the correlation threshold, then including the correlation coefficient, confidence interval, p-values, and permutation test results before saving the figure.

Now I'm closing the plot and setting up the command-line argument parser for the main analysis script, which will accept paths to the base model, pruned model, recovered model, CKA scores file, and pruning mask.

Continuing with argument setup...

Now I'm loading the CKA scores from the checkpoint and validating that the attention CKA matrix is present, then loading the pruning metadata to extract the attention and MLP keep masks. I'm also initializing the tokenizer from the base model.

Loading calibration data and the pruned model...

Collecting attention and MLP activations from the pruned model, then doing the same for the recovered model to compare their outputs.

Now I'm computing recoverability metrics for both attention heads and MLP layers by comparing the activations between the pruned and recovered models, then cleaning up the intermediate data.

Computing statistics on the overlap and recoverability scores for each component type...

Now I'm aggregating the results across both attention and MLP layers, calculating combined statistics, and determining a pass/fail verdict based on the correlation threshold. Then I'm structuring the output to save both the aggregate metrics and the individual group data.

Generating visualization plots... Writing the summary output...

Actually, I'm realizing there's a potential issue with how I'm handling the GQA structure. The `n_heads_original` parameter is set to 28 by default, but that's the number of query heads, not the number of key-value heads. Since the attention masks store GQA group indices (0-3 for the 4 KV heads in Qwen2.5-7B), I should be using 4 as the reference, not 28. I'm realizing the issue with how the activations are being reshaped. The `head_dim` calculation divides the hidden size by the total number of attention heads, but when we're working with the pruned model that keeps only certain GQA groups, the `n_retained` value represents the number of retained groups (not individual heads), so reshaping to `[seq, n_retained, head_dim]` is treating each group as a single unit rather than accounting for the multiple Q heads per group.

This suggests `keep_masks` might actually store individual Q head indices rather than GQA group indices, which would resolve the dimension mismatch. I need to trace back through the prune.py code to see how `attn_keep_masks` is actually constructed to understand what it's indexing.

Looking at the CKA computation, it seems the overlap matrices are built from head activations grouped by GQA structure, producing CKA matrices with dimensions based on the number of KV heads.

For Qwen2.5-7B with 4 KV heads, the `attn_cka_matrix[layer_idx]` is a 4×4 matrix and `attn_overlap[layer_idx]` is a length-4 tensor. But in `compute_recoverability`, when indexing with `h_p` from pruned heads, there's a mismatch if `n_heads_original=28` since the keep_masks would have indices up to 28, not 4.

Looking at the main function, if `n_heads=28` and `keep_masks` contains GQA group indices (0-3), then accessing indices 4-27 on a 4×4 matrix would be out of bounds. This suggests either an existing bug or the code expects a different convention where keep_masks stores Q head indices instead. I'm realizing the issue might be in how the pruned head indices map back to the original matrix dimensions—when heads are removed, the indexing shifts, so I need to trace through exactly what `attn_keep_masks` actually stores to understand whether it's using original indices or remapped ones.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "7dda6c6f-cfe8-413b-8564-42b05e2f2805",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016thGePMRuwucsTjNMBoH7c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3304,
      "cache_read_input_tokens": 52201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3304
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

_source line 49_

需要看 prune.py 中间被截断的 unified ranking 部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "8ac009df-2859-43e7-ae69-9c2d2dd474fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016thGePMRuwucsTjNMBoH7c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3304,
      "cache_read_input_tokens": 52201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3304
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

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012ktxngGFMThjduDMpfe3Lf`</summary>

```json
{
  "server": "westb-23072",
  "command": "head -280 /root/recovery_aware_struct_prune/src/prune.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "8af098fa-96c5-434b-a96b-fdf274d9110a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016thGePMRuwucsTjNMBoH7c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3304,
      "cache_read_input_tokens": 52201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3304
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

_source line 51 · 2026-05-14T05:31:53.276Z_

<details><summary>↩ Tool result · `toolu_012ktxngGFMThjduDMpfe3Lf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nStructured Pruning for Qwen2.5 architecture (GQA-group granularity).\\n\\nRemoves GQA groups (7 Q heads + 1 KV head each) and MLP channel groups\\nbased on RASP or standard importance scores.\\n\\nInput:  pretrained model + pruning scores\\nOutput: pruned model saved to disk\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport copy\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef prune_attention_heads(model, attn_keep_masks: dict):\\n    \\\"\\\"\\\"Prune GQA groups from the model by slicing weight matrices in-place.\\n\\n    attn_keep_masks: dict[layer_idx -> list of GQA group indices to KEEP]\\n    Each GQA group = heads_per_kv Q heads + 1 KV head.\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n\\n    total_pruned_groups = 0\\n\\n    for layer_idx, keep_groups in attn_keep_masks.items():\\n        layer = model.model.layers[layer_idx]\\n        attn = layer.self_attn\\n        n_keep_groups = len(keep_groups)\\n        pruned_groups = n_kv_heads - n_keep_groups\\n\\n        # Expand GQA group indices to Q head weight indices\\n        q_indices = []\\n        for g in keep_groups:\\n            for qh in range(heads_per_kv):\\n                h = g * heads_per_kv + qh\\n                start = h * head_dim\\n                q_indices.extend(range(start, start + head_dim))\\n        q_indices = torch.tensor(q_indices, dtype=torch.long)\\n\\n        # KV head weight indices (1 per group)\\n        kv_indices = []\\n        for g in keep_groups:\\n            start = g * head_dim\\n            kv_indices.extend(range(start, start + head_dim))\\n        kv_indices = torch.tensor(kv_indices, dtype=torch.long)\\n\\n        # Slice q_proj: [n_heads*head_dim, hidden] -> [n_keep_q*head_dim, hidden]\\n        attn.q_proj.weight = torch.nn.Parameter(attn.q_proj.weight.data[q_indices])\\n        if attn.q_proj.bias is not None:\\n            attn.q_proj.bias = torch.nn.Parameter(attn.q_proj.bias.data[q_indices])\\n\\n        # Slice k_proj, v_proj: [n_kv*head_dim, hidden] -> [n_keep_kv*head_dim, hidden]\\n        attn.k_proj.weight = torch.nn.Parameter(attn.k_proj.weight.data[kv_indices])\\n        if attn.k_proj.bias is not None:\\n            attn.k_proj.bias = torch.nn.Parameter(attn.k_proj.bias.data[kv_indices])\\n\\n        attn.v_proj.weight = torch.nn.Parameter(attn.v_proj.weight.data[kv_indices])\\n        if attn.v_proj.bias is not None:\\n            attn.v_proj.bias = torch.nn.Parameter(attn.v_proj.bias.data[kv_indices])\\n\\n        # Slice o_proj: [hidden, n_heads*head_dim] -> [hidden, n_keep_q*head_dim]\\n        attn.o_proj.weight = torch.nn.Parameter(attn.o_proj.weight.data[:, q_indices])\\n\\n        # Update layer config\\n        n_keep_q = n_keep_groups * heads_per_kv\\n        attn.num_heads = n_keep_q\\n        attn.num_key_value_heads = n_keep_groups\\n        attn.head_dim = head_dim\\n\\n        total_pruned_groups += pruned_groups\\n\\n        if pruned_groups > 0:\\n            logger.info(\\n                f\\\"  Layer {layer_idx}: pruned {pruned_groups}/{n_kv_heads} GQA groups \\\"\\n                f\\\"({pruned_groups * heads_per_kv} Q heads, {pruned_groups} KV heads)\\\"\\n            )\\n\\n    logger.info(f\\\"Total attention pruning: {total_pruned_groups} GQA groups removed\\\")\\n\\n\\ndef prune_mlp_channels(model, mlp_keep_masks: dict, n_mlp_groups: int = 28):\\n    \\\"\\\"\\\"Prune MLP channel groups by slicing gate_proj, up_proj, and down_proj.\\\"\\\"\\\"\\n    config = model.config\\n    intermediate_size = config.intermediate_size\\n    group_size = intermediate_size // n_mlp_groups\\n\\n    total_pruned = 0\\n\\n    for layer_idx, keep_groups in mlp_keep_masks.items():\\n        layer = model.m\\n\\n... [截断: 输出过长，省略 3351 字符] ...\\n\\n\\\"Original model parameters: {original_params:,}\\\")\\n\\n    # Load scores\\n    importance_data = torch.load(args.importance_path, map_location=\\\"cpu\\\", weights_only=True)\\n    attn_importance = importance_data[\\\"attn_importance\\\"]\\n    mlp_importance = importance_data[\\\"mlp_importance\\\"]\\n\\n    if args.mode == \\\"rasp\\\":\\n        if args.cka_path is None:\\n            raise ValueError(\\\"--cka_path required for rasp mode\\\")\\n        cka_data = torch.load(args.cka_path, map_location=\\\"cpu\\\", weights_only=True)\\n        attn_overlap = cka_data[\\\"attn_overlap\\\"]\\n        mlp_overlap = cka_data[\\\"mlp_overlap\\\"]\\n        attn_scores = {}\\n        for k in attn_importance:\\n            attn_scores[k] = attn_importance[k].float() * (1.0 - attn_overlap[k].float()).pow(args.alpha)\\n        mlp_scores = {}\\n        for k in mlp_importance:\\n            mlp_scores[k] = mlp_importance[k].float() * (1.0 - mlp_overlap[k].float()).pow(args.alpha)\\n        logger.info(f\\\"Using RASP scoring with alpha={args.alpha}\\\")\\n    else:\\n        attn_scores = {k: v.float() for k, v in attn_importance.items()}\\n        mlp_scores = {k: v.float() for k, v in mlp_importance.items()}\\n        logger.info(\\\"Using standard importance-only scoring\\\")\\n\\n    # Architecture parameters\\n    config = model.config\\n    n_layers = config.num_hidden_layers\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n    hidden = config.hidden_size\\n    intermediate_size = config.intermediate_size\\n    n_gqa_groups = n_kv_heads\\n    n_mlp_groups = n_heads\\n    mlp_group_size = intermediate_size // n_mlp_groups\\n\\n    # Per-structure parameter counts\\n    attn_params_per_group = (heads_per_kv * 2 + 2) * head_dim * hidden\\n    mlp_params_per_group = mlp_group_size * hidden * 3\\n\\n    logger.info(f\\\"GQA groups: {n_gqa_groups}/layer, ~{attn_params_per_group:,} params each\\\")\\n    logger.info(f\\\"MLP groups: {n_mlp_groups}/layer, ~{mlp_params_per_group:,} params each\\\")\\n\\n    target_prune_params = original_params * args.sparsity\\n\\n    # Unified ranking: merge attention GQA groups and MLP groups\\n    all_entries = []\\n    for layer_idx in range(n_layers):\\n        for g in range(n_gqa_groups):\\n            score = attn_scores[layer_idx][g].item()\\n            all_entries.append((score, \\\"attn\\\", layer_idx, g, attn_params_per_group))\\n        for g in range(n_mlp_groups):\\n            score = mlp_scores[layer_idx][g].item()\\n            all_entries.append((score, \\\"mlp\\\", layer_idx, g, mlp_params_per_group))\\n\\n    all_entries.sort(key=lambda x: x[0])\\n\\n    # Greedily select structures to prune\\n    pruned_params = 0\\n    attn_prune_set = set()\\n    mlp_prune_set = set()\\n\\n    min_keep_attn = 1  # keep at least 1 GQA group per layer\\n    min_keep_mlp = 4\\n    attn_prune_count = {i: 0 for i in range(n_layers)}\\n    mlp_prune_count = {i: 0 for i in range(n_layers)}\\n\\n    for score, stype, layer_idx, struct_idx, params in all_entries:\\n        if pruned_params >= target_prune_params:\\n            break\\n        if stype == \\\"attn\\\":\\n            if attn_prune_count[layer_idx] >= n_gqa_groups - min_keep_attn:\\n                continue\\n            attn_prune_set.add((layer_idx, struct_idx))\\n            attn_prune_count[layer_idx] += 1\\n        else:\\n            if mlp_prune_count[layer_idx] >= n_mlp_groups - min_keep_mlp:\\n                continue\\n            mlp_prune_set.add((layer_idx, struct_idx))\\n            mlp_prune_count[layer_idx] += 1\\n        pruned_params += params\\n\\n    logger.info(f\\\"Target sparsity: {args.sparsity:.2%}, target params to prune: {target_prune_params:,.0f}\\\")\\n    logger.info(f\\\"Selected to prune: {len(attn_prune_set)} attn GQA groups, {len(mlp_prune_set)} MLP groups\\\")\\n    logger.info(f\\\"Estimated pruned params: {pruned_params:,.0f}\\\")\\n\\n    # Build keep masks\\n    attn_keep_masks = {}\\n    for layer_idx in range(n_layers):\\n        keep = [g for g in range(n_gqa_groups) if (layer_idx, g) not in attn_prune_set]\\n        attn_keep_masks[layer_idx] = keep\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "4c1070d7-3969-46c4-af06-5730609722bf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nStructured Pruning for Qwen2.5 architecture (GQA-group granularity).\\\\n\\\\nRemoves GQA groups (7 Q heads + 1 KV head each) and MLP channel groups\\\\nbased on RASP or standard importance scores.\\\\n\\\\nInput:  pretrained model + pruning scores\\\\nOutput: pruned model saved to disk\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport copy\\\\nimport logging\\\\nimport os\\\\nimport random\\\\n\\\\nimport numpy as np\\\\nimport torch\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n)\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n\\\\ndef set_seed(seed: int):\\\\n    random.seed(seed)\\\\n    np.random.seed(seed)\\\\n    torch.manual_seed(seed)\\\\n    torch.cuda.manual_seed_all(seed)\\\\n\\\\n\\\\ndef prune_attention_heads(model, attn_keep_masks: dict):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Prune GQA groups from the model by slicing weight matrices in-place.\\\\n\\\\n    attn_keep_masks: dict[layer_idx -> list of GQA group indices to KEEP]\\\\n    Each GQA group = heads_per_kv Q heads + 1 KV head.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    config = model.config\\\\n    n_heads = config.num_attention_heads\\\\n    n_kv_heads = config.num_key_value_heads\\\\n    head_dim = config.hidden_size // n_heads\\\\n    heads_per_kv = n_heads // n_kv_heads\\\\n\\\\n    total_pruned_groups = 0\\\\n\\\\n    for layer_idx, keep_groups in attn_keep_masks.items():\\\\n        layer = model.model.layers[layer_idx]\\\\n        attn = layer.self_attn\\\\n        n_keep_groups = len(keep_groups)\\\\n        pruned_groups = n_kv_heads - n_keep_groups\\\\n\\\\n        # Expand GQA group indices to Q head weight indices\\\\n        q_indices = []\\\\n        for g in keep_groups:\\\\n            for qh in range(heads_per_kv):\\\\n                h = g * heads_per_kv + qh\\\\n                start = h * head_dim\\\\n                q_indices.extend(range(start, start + head_dim))\\\\n        q_indices = torch.tensor(q_indices, dtype=torch.long)\\\\n\\\\n        # KV head weight indices (1 per group)\\\\n        kv_indices = []\\\\n        for g in keep_groups:\\\\n            start = g * head_dim\\\\n            kv_indices.extend(range(start, start + head_dim))\\\\n        kv_indices = torch.tensor(kv_indices, dtype=torch.long)\\\\n\\\\n        # Slice q_proj: [n_heads*head_dim, hidden] -> [n_keep_q*head_dim, hidden]\\\\n        attn.q_proj.weight = torch.nn.Parameter(attn.q_proj.weight.data[q_indices])\\\\n        if attn.q_proj.bias is not None:\\\\n            attn.q_proj.bias = torch.nn.Parameter(attn.q_proj.bias.data[q_indices])\\\\n\\\\n        # Slice k_proj, v_proj: [n_kv*head_dim, hidden] -> [n_keep_kv*head_dim, hidden]\\\\n        attn.k_proj.weight = torch.nn.Parameter(attn.k_proj.weight.data[kv_indices])\\\\n        if attn.k_proj.bias is not None:\\\\n            attn.k_proj.bias = torch.nn.Parameter(attn.k_proj.bias.data[kv_indices])\\\\n\\\\n        attn.v_proj.weight = torch.nn.Parameter(attn.v_proj.weight.data[kv_indices])\\\\n        if attn.v_proj.bias is not None:\\\\n            attn.v_proj.bias = torch.nn.Parameter(attn.v_proj.bias.data[kv_indices])\\\\n\\\\n        # Slice o_proj: [hidden, n_heads*head_dim] -> [hidden, n_keep_q*head_dim]\\\\n        attn.o_proj.weight = torch.nn.Parameter(attn.o_proj.weight.data[:, q_indices])\\\\n\\\\n        # Update layer config\\\\n        n_keep_q = n_keep_groups * heads_per_kv\\\\n        attn.num_heads = n_keep_q\\\\n        attn.num_key_value_heads = n_keep_groups\\\\n        attn.head_dim = head_dim\\\\n\\\\n        total_pruned_groups += pruned_groups\\\\n\\\\n        if pruned_groups > 0:\\\\n            logger.info(\\\\n                f\\\\\\\"  Layer {layer_idx}: pruned {pruned_groups}/{n_kv_heads} GQA groups \\\\\\\"\\\\n                f\\\\\\\"({pruned_groups * heads_per_kv} Q heads, {pruned_groups} KV heads)\\\\\\\"\\\\n            )\\\\n\\\\n    logger.info(f\\\\\\\"Total attention pruning: {total_pruned_groups} GQA groups removed\\\\\\\")\\\\n\\\\n\\\\ndef prune_mlp_channels(model, mlp_keep_masks: dict, n_mlp_groups: int = 28):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Prune MLP channel groups by slicing gate_proj, up_proj, and down_proj.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    config = model.config\\\\n    intermediate_size = config.intermediate_size\\\\n    group_size = intermediate_size // n_mlp_groups\\\\n\\\\n    total_pruned = 0\\\\n\\\\n    for layer_idx, keep_groups in mlp_keep_masks.items():\\\\n        layer = model.m\\\\n\\\\n... [截断: 输出过长，省略 3351 字符] ...\\\\n\\\\n\\\\\\\"Original model parameters: {original_params:,}\\\\\\\")\\\\n\\\\n    # Load scores\\\\n    importance_data = torch.load(args.importance_path, map_location=\\\\\\\"cpu\\\\\\\", weights_only=True)\\\\n    attn_importance = importance_data[\\\\\\\"attn_importance\\\\\\\"]\\\\n    mlp_importance = importance_data[\\\\\\\"mlp_importance\\\\\\\"]\\\\n\\\\n    if args.mode == \\\\\\\"rasp\\\\\\\":\\\\n        if args.cka_path is None:\\\\n            raise ValueError(\\\\\\\"--cka_path required for rasp mode\\\\\\\")\\\\n        cka_data = torch.load(args.cka_path, map_location=\\\\\\\"cpu\\\\\\\", weights_only=True)\\\\n        attn_overlap = cka_data[\\\\\\\"attn_overlap\\\\\\\"]\\\\n        mlp_overlap = cka_data[\\\\\\\"mlp_overlap\\\\\\\"]\\\\n        attn_scores = {}\\\\n        for k in attn_importance:\\\\n            attn_scores[k] = attn_importance[k].float() * (1.0 - attn_overlap[k].float()).pow(args.alpha)\\\\n        mlp_scores = {}\\\\n        for k in mlp_importance:\\\\n            mlp_scores[k] = mlp_importance[k].float() * (1.0 - mlp_overlap[k].float()).pow(args.alpha)\\\\n        logger.info(f\\\\\\\"Using RASP scoring with alpha={args.alpha}\\\\\\\")\\\\n    else:\\\\n        attn_scores = {k: v.float() for k, v in attn_importance.items()}\\\\n        mlp_scores = {k: v.float() for k, v in mlp_importance.items()}\\\\n        logger.info(\\\\\\\"Using standard importance-only scoring\\\\\\\")\\\\n\\\\n    # Architecture parameters\\\\n    config = model.config\\\\n    n_layers = config.num_hidden_layers\\\\n    n_heads = config.num_attention_heads\\\\n    n_kv_heads = config.num_key_value_heads\\\\n    head_dim = config.hidden_size // n_heads\\\\n    heads_per_kv = n_heads // n_kv_heads\\\\n    hidden = config.hidden_size\\\\n    intermediate_size = config.intermediate_size\\\\n    n_gqa_groups = n_kv_heads\\\\n    n_mlp_groups = n_heads\\\\n    mlp_group_size = intermediate_size // n_mlp_groups\\\\n\\\\n    # Per-structure parameter counts\\\\n    attn_params_per_group = (heads_per_kv * 2 + 2) * head_dim * hidden\\\\n    mlp_params_per_group = mlp_group_size * hidden * 3\\\\n\\\\n    logger.info(f\\\\\\\"GQA groups: {n_gqa_groups}/layer, ~{attn_params_per_group:,} params each\\\\\\\")\\\\n    logger.info(f\\\\\\\"MLP groups: {n_mlp_groups}/layer, ~{mlp_params_per_group:,} params each\\\\\\\")\\\\n\\\\n    target_prune_params = original_params * args.sparsity\\\\n\\\\n    # Unified ranking: merge attention GQA groups and MLP groups\\\\n    all_entries = []\\\\n    for layer_idx in range(n_layers):\\\\n        for g in range(n_gqa_groups):\\\\n            score = attn_scores[layer_idx][g].item()\\\\n            all_entries.append((score, \\\\\\\"attn\\\\\\\", layer_idx, g, attn_params_per_group))\\\\n        for g in range(n_mlp_groups):\\\\n            score = mlp_scores[layer_idx][g].item()\\\\n            all_entries.append((score, \\\\\\\"mlp\\\\\\\", layer_idx, g, mlp_params_per_group))\\\\n\\\\n    all_entries.sort(key=lambda x: x[0])\\\\n\\\\n    # Greedily select structures to prune\\\\n    pruned_params = 0\\\\n    attn_prune_set = set()\\\\n    mlp_prune_set = set()\\\\n\\\\n    min_keep_attn = 1  # keep at least 1 GQA group per layer\\\\n    min_keep_mlp = 4\\\\n    attn_prune_count = {i: 0 for i in range(n_layers)}\\\\n    mlp_prune_count = {i: 0 for i in range(n_layers)}\\\\n\\\\n    for score, stype, layer_idx, struct_idx, params in all_entries:\\\\n        if pruned_params >= target_prune_params:\\\\n            break\\\\n        if stype == \\\\\\\"attn\\\\\\\":\\\\n            if attn_prune_count[layer_idx] >= n_gqa_groups - min_keep_attn:\\\\n                continue\\\\n            attn_prune_set.add((layer_idx, struct_idx))\\\\n            attn_prune_count[layer_idx] += 1\\\\n        else:\\\\n            if mlp_prune_count[layer_idx] >= n_mlp_groups - min_keep_mlp:\\\\n                continue\\\\n            mlp_prune_set.add((layer_idx, struct_idx))\\\\n            mlp_prune_count[layer_idx] += 1\\\\n        pruned_params += params\\\\n\\\\n    logger.info(f\\\\\\\"Target sparsity: {args.sparsity:.2%}, target params to prune: {target_prune_params:,.0f}\\\\\\\")\\\\n    logger.info(f\\\\\\\"Selected to prune: {len(attn_prune_set)} attn GQA groups, {len(mlp_prune_set)} MLP groups\\\\\\\")\\\\n    logger.info(f\\\\\\\"Estimated pruned params: {pruned_params:,.0f}\\\\\\\")\\\\n\\\\n    # Build keep masks\\\\n    attn_keep_masks = {}\\\\n    for layer_idx in range(n_layers):\\\\n        keep = [g for g in range(n_gqa_groups) if (layer_idx, g) not in attn_prune_set]\\\\n        attn_keep_masks[layer_idx] = keep\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nStructured Pruning for Qwen2.5 architecture (GQA-group granularity).\\n\\nRemoves GQA groups (7 Q heads + 1 KV head each) and MLP channel groups\\nbased on RASP or standard importance scores.\\n\\nInput:  pretrained model + pruning scores\\nOutput: pruned model saved to disk\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport copy\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef prune_attention_heads(model, attn_keep_masks: dict):\\n    \\\"\\\"\\\"Prune GQA groups from the model by slicing weight matrices in-place.\\n\\n    attn_keep_masks: dict[layer_idx -> list of GQA group indices to KEEP]\\n    Each GQA group = heads_per_kv Q heads + 1 KV head.\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n\\n    total_pruned_groups = 0\\n\\n    for layer_idx, keep_groups in attn_keep_masks.items():\\n        layer = model.model.layers[layer_idx]\\n        attn = layer.self_attn\\n        n_keep_groups = len(keep_groups)\\n        pruned_groups = n_kv_heads - n_keep_groups\\n\\n        # Expand GQA group indices to Q head weight indices\\n        q_indices = []\\n        for g in keep_groups:\\n            for qh in range(heads_per_kv):\\n                h = g * heads_per_kv + qh\\n                start = h * head_dim\\n                q_indices.extend(range(start, start + head_dim))\\n        q_indices = torch.tensor(q_indices, dtype=torch.long)\\n\\n        # KV head weight indices (1 per group)\\n        kv_indices = []\\n        for g in keep_groups:\\n            start = g * head_dim\\n            kv_indices.extend(range(start, start + head_dim))\\n        kv_indices = torch.tensor(kv_indices, dtype=torch.long)\\n\\n        # Slice q_proj: [n_heads*head_dim, hidden] -> [n_keep_q*head_dim, hidden]\\n        attn.q_proj.weight = torch.nn.Parameter(attn.q_proj.weight.data[q_indices])\\n        if attn.q_proj.bias is not None:\\n            attn.q_proj.bias = torch.nn.Parameter(attn.q_proj.bias.data[q_indices])\\n\\n        # Slice k_proj, v_proj: [n_kv*head_dim, hidden] -> [n_keep_kv*head_dim, hidden]\\n        attn.k_proj.weight = torch.nn.Parameter(attn.k_proj.weight.data[kv_indices])\\n        if attn.k_proj.bias is not None:\\n            attn.k_proj.bias = torch.nn.Parameter(attn.k_proj.bias.data[kv_indices])\\n\\n        attn.v_proj.weight = torch.nn.Parameter(attn.v_proj.weight.data[kv_indices])\\n        if attn.v_proj.bias is not None:\\n            attn.v_proj.bias = torch.nn.Parameter(attn.v_proj.bias.data[kv_indices])\\n\\n        # Slice o_proj: [hidden, n_heads*head_dim] -> [hidden, n_keep_q*head_dim]\\n        attn.o_proj.weight = torch.nn.Parameter(attn.o_proj.weight.data[:, q_indices])\\n\\n        # Update layer config\\n        n_keep_q = n_keep_groups * heads_per_kv\\n        attn.num_heads = n_keep_q\\n        attn.num_key_value_heads = n_keep_groups\\n        attn.head_dim = head_dim\\n\\n        total_pruned_groups += pruned_groups\\n\\n        if pruned_groups > 0:\\n            logger.info(\\n                f\\\"  Layer {layer_idx}: pruned {pruned_groups}/{n_kv_heads} GQA groups \\\"\\n                f\\\"({pruned_groups * heads_per_kv} Q heads, {pruned_groups} KV heads)\\\"\\n            )\\n\\n    logger.info(f\\\"Total attention pruning: {total_pruned_groups} GQA groups removed\\\")\\n\\n\\ndef prune_mlp_channels(model, mlp_keep_masks: dict, n_mlp_groups: int = 28):\\n    \\\"\\\"\\\"Prune MLP channel groups by slicing gate_proj, up_proj, and down_proj.\\\"\\\"\\\"\\n    config = model.config\\n    intermediate_size = config.intermediate_size\\n    group_size = intermediate_size // n_mlp_groups\\n\\n    total_pruned = 0\\n\\n    for layer_idx, keep_groups in mlp_keep_masks.items():\\n        layer = model.m\\n\\n... [截断: 输出过长，省略 3351 字符] ...\\n\\n\\\"Original model parameters: {original_params:,}\\\")\\n\\n    # Load scores\\n    importance_data = torch.load(args.importance_path, map_location=\\\"cpu\\\", weights_only=True)\\n    attn_importance = importance_data[\\\"attn_importance\\\"]\\n    mlp_importance = importance_data[\\\"mlp_importance\\\"]\\n\\n    if args.mode == \\\"rasp\\\":\\n        if args.cka_path is None:\\n            raise ValueError(\\\"--cka_path required for rasp mode\\\")\\n        cka_data = torch.load(args.cka_path, map_location=\\\"cpu\\\", weights_only=True)\\n        attn_overlap = cka_data[\\\"attn_overlap\\\"]\\n        mlp_overlap = cka_data[\\\"mlp_overlap\\\"]\\n        attn_scores = {}\\n        for k in attn_importance:\\n            attn_scores[k] = attn_importance[k].float() * (1.0 - attn_overlap[k].float()).pow(args.alpha)\\n        mlp_scores = {}\\n        for k in mlp_importance:\\n            mlp_scores[k] = mlp_importance[k].float() * (1.0 - mlp_overlap[k].float()).pow(args.alpha)\\n        logger.info(f\\\"Using RASP scoring with alpha={args.alpha}\\\")\\n    else:\\n        attn_scores = {k: v.float() for k, v in attn_importance.items()}\\n        mlp_scores = {k: v.float() for k, v in mlp_importance.items()}\\n        logger.info(\\\"Using standard importance-only scoring\\\")\\n\\n    # Architecture parameters\\n    config = model.config\\n    n_layers = config.num_hidden_layers\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n    hidden = config.hidden_size\\n    intermediate_size = config.intermediate_size\\n    n_gqa_groups = n_kv_heads\\n    n_mlp_groups = n_heads\\n    mlp_group_size = intermediate_size // n_mlp_groups\\n\\n    # Per-structure parameter counts\\n    attn_params_per_group = (heads_per_kv * 2 + 2) * head_dim * hidden\\n    mlp_params_per_group = mlp_group_size * hidden * 3\\n\\n    logger.info(f\\\"GQA groups: {n_gqa_groups}/layer, ~{attn_params_per_group:,} params each\\\")\\n    logger.info(f\\\"MLP groups: {n_mlp_groups}/layer, ~{mlp_params_per_group:,} params each\\\")\\n\\n    target_prune_params = original_params * args.sparsity\\n\\n    # Unified ranking: merge attention GQA groups and MLP groups\\n    all_entries = []\\n    for layer_idx in range(n_layers):\\n        for g in range(n_gqa_groups):\\n            score = attn_scores[layer_idx][g].item()\\n            all_entries.append((score, \\\"attn\\\", layer_idx, g, attn_params_per_group))\\n        for g in range(n_mlp_groups):\\n            score = mlp_scores[layer_idx][g].item()\\n            all_entries.append((score, \\\"mlp\\\", layer_idx, g, mlp_params_per_group))\\n\\n    all_entries.sort(key=lambda x: x[0])\\n\\n    # Greedily select structures to prune\\n    pruned_params = 0\\n    attn_prune_set = set()\\n    mlp_prune_set = set()\\n\\n    min_keep_attn = 1  # keep at least 1 GQA group per layer\\n    min_keep_mlp = 4\\n    attn_prune_count = {i: 0 for i in range(n_layers)}\\n    mlp_prune_count = {i: 0 for i in range(n_layers)}\\n\\n    for score, stype, layer_idx, struct_idx, params in all_entries:\\n        if pruned_params >= target_prune_params:\\n            break\\n        if stype == \\\"attn\\\":\\n            if attn_prune_count[layer_idx] >= n_gqa_groups - min_keep_attn:\\n                continue\\n            attn_prune_set.add((layer_idx, struct_idx))\\n            attn_prune_count[layer_idx] += 1\\n        else:\\n            if mlp_prune_count[layer_idx] >= n_mlp_groups - min_keep_mlp:\\n                continue\\n            mlp_prune_set.add((layer_idx, struct_idx))\\n            mlp_prune_count[layer_idx] += 1\\n        pruned_params += params\\n\\n    logger.info(f\\\"Target sparsity: {args.sparsity:.2%}, target params to prune: {target_prune_params:,.0f}\\\")\\n    logger.info(f\\\"Selected to prune: {len(attn_prune_set)} attn GQA groups, {len(mlp_prune_set)} MLP groups\\\")\\n    logger.info(f\\\"Estimated pruned params: {pruned_params:,.0f}\\\")\\n\\n    # Build keep masks\\n    attn_keep_masks = {}\\n    for layer_idx in range(n_layers):\\n        keep = [g for g in range(n_gqa_groups) if (layer_idx, g) not in attn_prune_set]\\n        attn_keep_masks[layer_idx] = keep\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HifPHMPFaMxqPVyXf7P2ZV`</summary>

```json
{
  "server": "westb-23072",
  "command": "tail -n +275 /root/recovery_aware_struct_prune/src/prune.py",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "b2d542bf-7314-4075-8194-f64e2d75b073",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GnBaKQYjUD6HpZchx2F1wK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13825,
      "cache_read_input_tokens": 55505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13825
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

_source line 53 · 2026-05-14T05:31:56.945Z_

<details><summary>↩ Tool result · `toolu_01HifPHMPFaMxqPVyXf7P2ZV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    # Build keep masks\\n    attn_keep_masks = {}\\n    for layer_idx in range(n_layers):\\n        keep = [g for g in range(n_gqa_groups) if (layer_idx, g) not in attn_prune_set]\\n        attn_keep_masks[layer_idx] = keep\\n\\n    mlp_keep_masks = {}\\n    for layer_idx in range(n_layers):\\n        keep = [g for g in range(n_mlp_groups) if (layer_idx, g) not in mlp_prune_set]\\n        mlp_keep_masks[layer_idx] = keep\\n\\n    # Execute pruning\\n    logger.info(\\\"Pruning GQA groups...\\\")\\n    prune_attention_heads(model, attn_keep_masks)\\n\\n    logger.info(\\\"Pruning MLP channels...\\\")\\n    prune_mlp_channels(model, mlp_keep_masks, n_mlp_groups=n_mlp_groups)\\n\\n    pruned_params_actual = count_parameters(model)\\n    actual_sparsity = 1.0 - pruned_params_actual / original_params\\n    logger.info(\\n        f\\\"Pruned model parameters: {pruned_params_actual:,} \\\"\\n        f\\\"(actual sparsity: {actual_sparsity:.2%})\\\"\\n    )\\n\\n    # --- Update model config ---\\n    per_layer_q_heads = []\\n    per_layer_kv_heads = []\\n    for li in range(n_layers):\\n        layer_i = model.model.layers[li]\\n        per_layer_q_heads.append(layer_i.self_attn.num_heads)\\n        per_layer_kv_heads.append(layer_i.self_attn.num_key_value_heads)\\n\\n    unique_q = set(per_layer_q_heads)\\n    unique_kv = set(per_layer_kv_heads)\\n\\n    if len(unique_q) == 1 and len(unique_kv) == 1:\\n        model.config.num_attention_heads = per_layer_q_heads[0]\\n        model.config.num_key_value_heads = per_layer_kv_heads[0]\\n        logger.info(f\\\"Uniform pruning: config num_attention_heads={per_layer_q_heads[0]}, \\\"\\n                    f\\\"num_key_value_heads={per_layer_kv_heads[0]}\\\")\\n    else:\\n        model.config.num_attention_heads = min(per_layer_q_heads)\\n        model.config.num_key_value_heads = min(per_layer_kv_heads)\\n        model.config.per_layer_num_attention_heads = per_layer_q_heads\\n        model.config.per_layer_num_key_value_heads = per_layer_kv_heads\\n        logger.warning(\\n            f\\\"Non-uniform pruning: per-layer Q heads range \\\"\\n            f\\\"[{min(per_layer_q_heads)}, {max(per_layer_q_heads)}], \\\"\\n            f\\\"KV heads range [{min(per_layer_kv_heads)}, {max(per_layer_kv_heads)}]. \\\"\\n            f\\\"Per-layer counts stored in config.\\\"\\n        )\\n\\n    # Update intermediate_size for MLP pruning\\n    per_layer_intermediate = []\\n    for li in range(n_layers):\\n        new_intermediate = model.model.layers[li].mlp.gate_proj.weight.shape[0]\\n        per_layer_intermediate.append(new_intermediate)\\n\\n    unique_intermediate = set(per_layer_intermediate)\\n    if len(unique_intermediate) == 1:\\n        model.config.intermediate_size = per_layer_intermediate[0]\\n        logger.info(f\\\"Updated config intermediate_size={per_layer_intermediate[0]}\\\")\\n    else:\\n        model.config.intermediate_size = min(per_layer_intermediate)\\n        model.config.per_layer_intermediate_size = per_layer_intermediate\\n        logger.warning(f\\\"Non-uniform MLP: intermediate_size range \\\"\\n                       f\\\"[{min(per_layer_intermediate)}, {max(per_layer_intermediate)}]\\\")\\n\\n    # Forward pass validation\\n    embed_device = model.model.embed_tokens.weight.device\\n    with torch.no_grad():\\n        dummy_input = torch.randint(0, 1000, (1, 32)).to(embed_device)\\n        try:\\n            output = model(dummy_input)\\n            logger.info(f\\\"Forward pass validation OK, output shape: {output.logits.shape}\\\")\\n        except Exception as e:\\n            logger.error(f\\\"Forward pass FAILED after pruning: {e}\\\")\\n            raise RuntimeError(f\\\"Pruned model forward pass failed: {e}\\\")\\n\\n    # Print pruning statistics\\n    logger.info(\\\"=\\\" * 50)\\n    logger.info(\\\"PRUNING STATISTICS\\\")\\n    logger.info(f\\\"  Mode: {args.mode}\\\")\\n    logger.info(f\\\"  Attn GQA groups pruned: {len(attn_prune_set)} / {n_layers * n_gqa_groups}\\\")\\n    logger.info(f\\\"  MLP groups pruned: {len(mlp_prune_set)} / {n_layers * n_mlp_groups}\\\")\\n    logger.info(f\\\"  Target sparsity: {args.sparsity:.2%}\\\")\\n    logger.info(f\\\"  Actual sparsity: {actual_sparsity:.2%}\\\")\\n    logger.info(\\\"=\\\" * 50)\\n\\n    # Save\\n    logger.info(f\\\"Saving pruned model to {args.output_path}\\\")\\n    os.makedirs(args.output_path, exist_ok=True)\\n    model.save_pretrained(args.output_path)\\n    tokenizer.save_pretrained(args.output_path)\\n\\n    # Save pruning metadata\\n    metadata = {\\n        \\\"mode\\\": args.mode,\\n        \\\"sparsity_target\\\": args.sparsity,\\n        \\\"sparsity_actual\\\": actual_sparsity,\\n        \\\"alpha\\\": args.alpha if args.mode == \\\"rasp\\\" else None,\\n        \\\"original_params\\\": original_params,\\n        \\\"pruned_params\\\": pruned_params_actual,\\n        \\\"attn_keep_masks\\\": attn_keep_masks,\\n        \\\"mlp_keep_masks\\\": mlp_keep_masks,\\n        \\\"n_attn_groups_pruned\\\": len(attn_prune_set),\\n        \\\"n_mlp_groups_pruned\\\": len(mlp_prune_set),\\n    }\\n    torch.save(metadata, os.path.join(args.output_path, \\\"pruning_metadata.pt\\\"))\\n    logger.info(\\\"Done.\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "318bd348-cfc4-4890-8bc4-8bb3cf95e15e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    # Build keep masks\\\\n    attn_keep_masks = {}\\\\n    for layer_idx in range(n_layers):\\\\n        keep = [g for g in range(n_gqa_groups) if (layer_idx, g) not in attn_prune_set]\\\\n        attn_keep_masks[layer_idx] = keep\\\\n\\\\n    mlp_keep_masks = {}\\\\n    for layer_idx in range(n_layers):\\\\n        keep = [g for g in range(n_mlp_groups) if (layer_idx, g) not in mlp_prune_set]\\\\n        mlp_keep_masks[layer_idx] = keep\\\\n\\\\n    # Execute pruning\\\\n    logger.info(\\\\\\\"Pruning GQA groups...\\\\\\\")\\\\n    prune_attention_heads(model, attn_keep_masks)\\\\n\\\\n    logger.info(\\\\\\\"Pruning MLP channels...\\\\\\\")\\\\n    prune_mlp_channels(model, mlp_keep_masks, n_mlp_groups=n_mlp_groups)\\\\n\\\\n    pruned_params_actual = count_parameters(model)\\\\n    actual_sparsity = 1.0 - pruned_params_actual / original_params\\\\n    logger.info(\\\\n        f\\\\\\\"Pruned model parameters: {pruned_params_actual:,} \\\\\\\"\\\\n        f\\\\\\\"(actual sparsity: {actual_sparsity:.2%})\\\\\\\"\\\\n    )\\\\n\\\\n    # --- Update model config ---\\\\n    per_layer_q_heads = []\\\\n    per_layer_kv_heads = []\\\\n    for li in range(n_layers):\\\\n        layer_i = model.model.layers[li]\\\\n        per_layer_q_heads.append(layer_i.self_attn.num_heads)\\\\n        per_layer_kv_heads.append(layer_i.self_attn.num_key_value_heads)\\\\n\\\\n    unique_q = set(per_layer_q_heads)\\\\n    unique_kv = set(per_layer_kv_heads)\\\\n\\\\n    if len(unique_q) == 1 and len(unique_kv) == 1:\\\\n        model.config.num_attention_heads = per_layer_q_heads[0]\\\\n        model.config.num_key_value_heads = per_layer_kv_heads[0]\\\\n        logger.info(f\\\\\\\"Uniform pruning: config num_attention_heads={per_layer_q_heads[0]}, \\\\\\\"\\\\n                    f\\\\\\\"num_key_value_heads={per_layer_kv_heads[0]}\\\\\\\")\\\\n    else:\\\\n        model.config.num_attention_heads = min(per_layer_q_heads)\\\\n        model.config.num_key_value_heads = min(per_layer_kv_heads)\\\\n        model.config.per_layer_num_attention_heads = per_layer_q_heads\\\\n        model.config.per_layer_num_key_value_heads = per_layer_kv_heads\\\\n        logger.warning(\\\\n            f\\\\\\\"Non-uniform pruning: per-layer Q heads range \\\\\\\"\\\\n            f\\\\\\\"[{min(per_layer_q_heads)}, {max(per_layer_q_heads)}], \\\\\\\"\\\\n            f\\\\\\\"KV heads range [{min(per_layer_kv_heads)}, {max(per_layer_kv_heads)}]. \\\\\\\"\\\\n            f\\\\\\\"Per-layer counts stored in config.\\\\\\\"\\\\n        )\\\\n\\\\n    # Update intermediate_size for MLP pruning\\\\n    per_layer_intermediate = []\\\\n    for li in range(n_layers):\\\\n        new_intermediate = model.model.layers[li].mlp.gate_proj.weight.shape[0]\\\\n        per_layer_intermediate.append(new_intermediate)\\\\n\\\\n    unique_intermediate = set(per_layer_intermediate)\\\\n    if len(unique_intermediate) == 1:\\\\n        model.config.intermediate_size = per_layer_intermediate[0]\\\\n        logger.info(f\\\\\\\"Updated config intermediate_size={per_layer_intermediate[0]}\\\\\\\")\\\\n    else:\\\\n        model.config.intermediate_size = min(per_layer_intermediate)\\\\n        model.config.per_layer_intermediate_size = per_layer_intermediate\\\\n        logger.warning(f\\\\\\\"Non-uniform MLP: intermediate_size range \\\\\\\"\\\\n                       f\\\\\\\"[{min(per_layer_intermediate)}, {max(per_layer_intermediate)}]\\\\\\\")\\\\n\\\\n    # Forward pass validation\\\\n    embed_device = model.model.embed_tokens.weight.device\\\\n    with torch.no_grad():\\\\n        dummy_input = torch.randint(0, 1000, (1, 32)).to(embed_device)\\\\n        try:\\\\n            output = model(dummy_input)\\\\n            logger.info(f\\\\\\\"Forward pass validation OK, output shape: {output.logits.shape}\\\\\\\")\\\\n        except Exception as e:\\\\n            logger.error(f\\\\\\\"Forward pass FAILED after pruning: {e}\\\\\\\")\\\\n            raise RuntimeError(f\\\\\\\"Pruned model forward pass failed: {e}\\\\\\\")\\\\n\\\\n    # Print pruning statistics\\\\n    logger.info(\\\\\\\"=\\\\\\\" * 50)\\\\n    logger.info(\\\\\\\"PRUNING STATISTICS\\\\\\\")\\\\n    logger.info(f\\\\\\\"  Mode: {args.mode}\\\\\\\")\\\\n    logger.info(f\\\\\\\"  Attn GQA groups pruned: {len(attn_prune_set)} / {n_layers * n_gqa_groups}\\\\\\\")\\\\n    logger.info(f\\\\\\\"  MLP groups pruned: {len(mlp_prune_set)} / {n_layers * n_mlp_groups}\\\\\\\")\\\\n    logger.info(f\\\\\\\"  Target sparsity: {args.sparsity:.2%}\\\\\\\")\\\\n    logger.info(f\\\\\\\"  Actual sparsity: {actual_sparsity:.2%}\\\\\\\")\\\\n    logger.info(\\\\\\\"=\\\\\\\" * 50)\\\\n\\\\n    # Save\\\\n    logger.info(f\\\\\\\"Saving pruned model to {args.output_path}\\\\\\\")\\\\n    os.makedirs(args.output_path, exist_ok=True)\\\\n    model.save_pretrained(args.output_path)\\\\n    tokenizer.save_pretrained(args.output_path)\\\\n\\\\n    # Save pruning metadata\\\\n    metadata = {\\\\n        \\\\\\\"mode\\\\\\\": args.mode,\\\\n        \\\\\\\"sparsity_target\\\\\\\": args.sparsity,\\\\n        \\\\\\\"sparsity_actual\\\\\\\": actual_sparsity,\\\\n        \\\\\\\"alpha\\\\\\\": args.alpha if args.mode == \\\\\\\"rasp\\\\\\\" else None,\\\\n        \\\\\\\"original_params\\\\\\\": original_params,\\\\n        \\\\\\\"pruned_params\\\\\\\": pruned_params_actual,\\\\n        \\\\\\\"attn_keep_masks\\\\\\\": attn_keep_masks,\\\\n        \\\\\\\"mlp_keep_masks\\\\\\\": mlp_keep_masks,\\\\n        \\\\\\\"n_attn_groups_pruned\\\\\\\": len(attn_prune_set),\\\\n        \\\\\\\"n_mlp_groups_pruned\\\\\\\": len(mlp_prune_set),\\\\n    }\\\\n    torch.save(metadata, os.path.join(args.output_path, \\\\\\\"pruning_metadata.pt\\\\\\\"))\\\\n    logger.info(\\\\\\\"Done.\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    # Build keep masks\\n    attn_keep_masks = {}\\n    for layer_idx in range(n_layers):\\n        keep = [g for g in range(n_gqa_groups) if (layer_idx, g) not in attn_prune_set]\\n        attn_keep_masks[layer_idx] = keep\\n\\n    mlp_keep_masks = {}\\n    for layer_idx in range(n_layers):\\n        keep = [g for g in range(n_mlp_groups) if (layer_idx, g) not in mlp_prune_set]\\n        mlp_keep_masks[layer_idx] = keep\\n\\n    # Execute pruning\\n    logger.info(\\\"Pruning GQA groups...\\\")\\n    prune_attention_heads(model, attn_keep_masks)\\n\\n    logger.info(\\\"Pruning MLP channels...\\\")\\n    prune_mlp_channels(model, mlp_keep_masks, n_mlp_groups=n_mlp_groups)\\n\\n    pruned_params_actual = count_parameters(model)\\n    actual_sparsity = 1.0 - pruned_params_actual / original_params\\n    logger.info(\\n        f\\\"Pruned model parameters: {pruned_params_actual:,} \\\"\\n        f\\\"(actual sparsity: {actual_sparsity:.2%})\\\"\\n    )\\n\\n    # --- Update model config ---\\n    per_layer_q_heads = []\\n    per_layer_kv_heads = []\\n    for li in range(n_layers):\\n        layer_i = model.model.layers[li]\\n        per_layer_q_heads.append(layer_i.self_attn.num_heads)\\n        per_layer_kv_heads.append(layer_i.self_attn.num_key_value_heads)\\n\\n    unique_q = set(per_layer_q_heads)\\n    unique_kv = set(per_layer_kv_heads)\\n\\n    if len(unique_q) == 1 and len(unique_kv) == 1:\\n        model.config.num_attention_heads = per_layer_q_heads[0]\\n        model.config.num_key_value_heads = per_layer_kv_heads[0]\\n        logger.info(f\\\"Uniform pruning: config num_attention_heads={per_layer_q_heads[0]}, \\\"\\n                    f\\\"num_key_value_heads={per_layer_kv_heads[0]}\\\")\\n    else:\\n        model.config.num_attention_heads = min(per_layer_q_heads)\\n        model.config.num_key_value_heads = min(per_layer_kv_heads)\\n        model.config.per_layer_num_attention_heads = per_layer_q_heads\\n        model.config.per_layer_num_key_value_heads = per_layer_kv_heads\\n        logger.warning(\\n            f\\\"Non-uniform pruning: per-layer Q heads range \\\"\\n            f\\\"[{min(per_layer_q_heads)}, {max(per_layer_q_heads)}], \\\"\\n            f\\\"KV heads range [{min(per_layer_kv_heads)}, {max(per_layer_kv_heads)}]. \\\"\\n            f\\\"Per-layer counts stored in config.\\\"\\n        )\\n\\n    # Update intermediate_size for MLP pruning\\n    per_layer_intermediate = []\\n    for li in range(n_layers):\\n        new_intermediate = model.model.layers[li].mlp.gate_proj.weight.shape[0]\\n        per_layer_intermediate.append(new_intermediate)\\n\\n    unique_intermediate = set(per_layer_intermediate)\\n    if len(unique_intermediate) == 1:\\n        model.config.intermediate_size = per_layer_intermediate[0]\\n        logger.info(f\\\"Updated config intermediate_size={per_layer_intermediate[0]}\\\")\\n    else:\\n        model.config.intermediate_size = min(per_layer_intermediate)\\n        model.config.per_layer_intermediate_size = per_layer_intermediate\\n        logger.warning(f\\\"Non-uniform MLP: intermediate_size range \\\"\\n                       f\\\"[{min(per_layer_intermediate)}, {max(per_layer_intermediate)}]\\\")\\n\\n    # Forward pass validation\\n    embed_device = model.model.embed_tokens.weight.device\\n    with torch.no_grad():\\n        dummy_input = torch.randint(0, 1000, (1, 32)).to(embed_device)\\n        try:\\n            output = model(dummy_input)\\n            logger.info(f\\\"Forward pass validation OK, output shape: {output.logits.shape}\\\")\\n        except Exception as e:\\n            logger.error(f\\\"Forward pass FAILED after pruning: {e}\\\")\\n            raise RuntimeError(f\\\"Pruned model forward pass failed: {e}\\\")\\n\\n    # Print pruning statistics\\n    logger.info(\\\"=\\\" * 50)\\n    logger.info(\\\"PRUNING STATISTICS\\\")\\n    logger.info(f\\\"  Mode: {args.mode}\\\")\\n    logger.info(f\\\"  Attn GQA groups pruned: {len(attn_prune_set)} / {n_layers * n_gqa_groups}\\\")\\n    logger.info(f\\\"  MLP groups pruned: {len(mlp_prune_set)} / {n_layers * n_mlp_groups}\\\")\\n    logger.info(f\\\"  Target sparsity: {args.sparsity:.2%}\\\")\\n    logger.info(f\\\"  Actual sparsity: {actual_sparsity:.2%}\\\")\\n    logger.info(\\\"=\\\" * 50)\\n\\n    # Save\\n    logger.info(f\\\"Saving pruned model to {args.output_path}\\\")\\n    os.makedirs(args.output_path, exist_ok=True)\\n    model.save_pretrained(args.output_path)\\n    tokenizer.save_pretrained(args.output_path)\\n\\n    # Save pruning metadata\\n    metadata = {\\n        \\\"mode\\\": args.mode,\\n        \\\"sparsity_target\\\": args.sparsity,\\n        \\\"sparsity_actual\\\": actual_sparsity,\\n        \\\"alpha\\\": args.alpha if args.mode == \\\"rasp\\\" else None,\\n        \\\"original_params\\\": original_params,\\n        \\\"pruned_params\\\": pruned_params_actual,\\n        \\\"attn_keep_masks\\\": attn_keep_masks,\\n        \\\"mlp_keep_masks\\\": mlp_keep_masks,\\n        \\\"n_attn_groups_pruned\\\": len(attn_prune_set),\\n        \\\"n_mlp_groups_pruned\\\": len(mlp_prune_set),\\n    }\\n    torch.save(metadata, os.path.join(args.output_path, \\\"pruning_metadata.pt\\\"))\\n    logger.info(\\\"Done.\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the full picture:

**prune.py**:
- `n_gqa_groups = n_kv_heads` (= 4 for Qwen2.5-7B)
- `n_mlp_groups = n_heads` (= 28)
- `attn_keep_masks[layer_idx]` = list of GQA group indices to keep (0 to 3)
- `mlp_keep_masks[layer_idx]` = list of MLP group indices to keep (0 to 27)

**correlation_analysis.py (current)**:


I'm seeing the mismatch now—when `n_heads = 28` gets passed as `n_heads_original` to `compute_recoverability`, it's being subtracted against `attn_keep_masks` which only contains GQA group indices (0-3), not individual head indices. So if `attn_keep_masks[0] = [0, 1, 3]`, the pruned heads calculation treats those small group numbers as if they're head indices across the full range of 28, which is completely wrong.

The real issue is that `n_heads_original` should actually be `n_kv_heads` (4 in this case) to match what's in the keep masks. And then looking at `collect_retained_head_activations`, there's another problem—after pruning, the model config gets updated with the new number of attention heads, but the head dimension calculation might be using that updated config instead of the original one, which would throw off the reshaping logic. I'm checking the config update logic in prune.py to understand how num_attention_heads gets set after pruning, and I'm realizing the math doesn't work out — if we're keeping 3 GQA groups with 7 heads each, that gives us 21 attention heads, but dividing the hidden size of 3584 by 21 doesn't yield a clean head dimension. Let me trace through what's actually happening with Qwen2.5-7B's configuration. I'm realizing the core issue: `load_pruned_model` only updates the attention layer attributes directly but doesn't modify `model.config`, so when `collect_retained_head_activations` tries to compute `head_dim` from the config, it gets the wrong value due to integer division with the new `num_attention_heads`.

The actual problem is in the weight loading sequence—after pruning the model in-place, loading the saved state dict (which has pruned dimensions) onto already-pruned weights creates a shape mismatch.

Wait, let me reconsider the dimensions here. If `keep_masks[0]` has 3 retained heads and `q_proj` outputs shape `[seq, 2688]`, then reshaping to `[seq, 3, 128]` would require 384 total dimensions, not 2688. That's a fundamental incompatibility in how the pruning and reshaping are supposed to work together. I'm seeing a shape mismatch issue in the collect_retained_head_activations function. The q_proj output has shape [seq, 2688] after pruning, but the code tries to reshape it to [seq, 3, 128] using n_retained=3, which doesn't work mathematically. This suggests the keep_masks must actually contain individual Q head indices rather than GQA group indices, or there's an undetected bug in the existing implementation.

Looking at the prune.py code, the attn_keep_masks definitely store GQA group indices (0-3 range), so correlation_analysis.py appears to have a bug that hasn't surfaced yet—possibly because this code path hasn't been executed since the recent GQA group granularity changes.

The issue is that correlation_analysis.py still expects keep_masks to contain individual Q head indices from the old format. If it's working with 28 heads and keeping 21, the reshape logic works fine for that case, but the CKA matrix computation in compute_recoverability would break when trying to map between the old per-head indices and whatever the current keep_masks actually contains.

Let me trace through what's happening: the CKA overlap was computed at GQA group granularity (4x4 matrix), but the correlation analysis code seems to be operating at Q head granularity. I need to look more carefully at what collect_retained_head_activations is actually supposed to return and how it relates to the keep_masks format. The issue is that the code was designed for per-head granularity but needs to be adapted for GQA group-level operations instead. I need to rewrite the attention handling to properly reshape activations based on the number of retained GQA groups, and also add support for MLP group recoverability to complete the implementation. I'm realizing the issue: when we load the base model, its config has the original num_key_value_heads=4, and pruning the attention heads doesn't update model.config—only the layer-level attributes change. So I need to figure out what num_key_value_heads actually is after loading the pruned state dict, since the saved config would have the updated value but we're not reloading it.

For the GQA group collection, I'm working through the math: if we have 4 key-value heads originally and 28 query heads, that's 7 heads per KV group. After pruning to keep 3 groups, the q_proj output becomes [seq, 2688], which reshapes to [seq, 3, 896]—so we retain 3 GQA groups with a feature dimension of 896.

Now I'm planning the full rewrite of correlation_analysis.py, starting with the function to collect retained groups...

Writing collection functions... should be fine to derive from the model config since we're loading from the base model path. Let me add the `--n_gqa_groups` and `--n_mlp_groups` arguments as specified in the task description, though I should verify what the existing correlation_analysis.py expects.

Looking at the CKA data structure, it seems the hardcoded `n_heads = 28` in correlation_analysis.py is actually referring to the number of Q heads, but the CKA matrices are computed at the GQA group level (n_kv_heads), so there's a mismatch I need to reconcile.

Now I need to verify how the pruned model actually uses attention head dimensions during forward passes—whether it references the original config values or the actual layer dimensions after pruning. the attention forward uses `self.num_heads` (which is set on the module level). After `prune_attention_heads`, each layer's `self_attn.num_heads` is updated to `n_keep_groups * heads_per_kv`. So the forward pass should work correctly.

For my collection functions:
- `model.config.num_attention_heads` = 28 (original)
- `model.config.num_key_value_heads` = 4 (original)
- These are correct for computing head_dim and heads_per_kv

OK let me just write the file now.

Actually, I realize there's one more subtlety. After calling `load_pruned_model`, the model's attention layers are pruned, but model.config.num_attention_heads = 28. When I hook q_proj, the output will have the pruned dimension (e.g., 21*128 if keeping 3 groups). But I'm computing head_dim, heads_per_kv, and the retained group counts using the original config values, which is correct since the config doesn't get updated. Then I reshape the q_proj output from the pruned sequence length and retained head count into the proper grouped structure.

For the MLP, after pruning, gate_proj outputs the pruned intermediate dimension. The original intermediate_size is 18944, and with 28 groups that's 676 per group. So I need to use the original config values to compute group_size, then reshape accordingly.

Wait, 18944 divided by 28 gives 676.57, which isn't a whole number. Looking at how cka_overlap.py handles this, it truncates to 18928 (28 × 676) and discards the last 16 dimensions.

Now I'm realizing the same truncation happens in prune.py—the group_size becomes 676 through integer division, and the pruning logic slices based on these groups. So when I'm collecting MLP activations after pruning, if 24 of 28 groups are retained, the gate_proj output would be [seq, 16224]. The original intermediate_size stays 18944 in the config since we load the base model first, but the actual pruned dimensions follow this grouping scheme.

Rather than relying on the config value, I can derive the group_size directly from the gate output shape and the number of retained groups—that's more robust. Now I'm writing out the complete collection function with careful handling for all the edge cases.

Writing the analysis module... I'm defining a function to load calibration data from the GSM8K dataset, formatting each example as a question-answer prompt and tokenizing it with a specified max length. Then I'm starting to import the pruning utilities to load the pruned model with its metadata and specified dtype.

Loading the model and applying pruning masks...

Now I'm setting up a function to collect activations from the attention layers, specifically tracking the retained query projections grouped by key-value heads. Processing calibration data and extracting attention outputs...

Now I'm collecting the retained MLP activations by setting up hooks to capture gate projection outputs across all layers, organizing them by sample and MLP group. Processing gate outputs...

Now I'm moving into a function that computes attention recoverability by examining which retained groups best reconstruct the pruned ones, using CKA similarity matrices to find the closest matches for each pruned group. I'm finishing up the attention group results by adding the recoverability metric and similarity score, then moving on to compute the same recoverability metrics for MLP groups by iterating through each layer and comparing pruned groups against retained ones. Writing statistical utility functions... I'm defining a function that computes correlation statistics—it handles edge cases with small sample sizes by returning NaN values, then calculates Spearman's rho, bootstrap confidence intervals, and permutation p-values for larger datasets. After that, I'm setting up a scatter plot function that attempts to import matplotlib and gracefully handles cases where it's not available.

Building the scatter plot visualization... Finishing up the visualization by setting the title with the correlation statistics and verdict, then saving the plot to disk. Now I'm moving into the main function to set up the argument parser for the correlation analysis script.

Setting up command-line arguments... Setting up the data types and loading the CKA scores and pruning masks from the saved files to validate they contain the required keys.

Now I'm initializing the tokenizer and loading calibration samples, then setting up the pruned model to collect activation data from both attention and MLP layers using the retention masks.

Collecting activations from recovered model...

Now I'm computing recoverability metrics for both attention and MLP components by comparing the pruned and recovered activations, then cleaning up the intermediate data. Now I'm extracting the CKA overlap and recoverability values from the combined results, then computing correlation statistics to see how well these metrics align. I'm setting a verdict based on whether the Spearman correlation meets the threshold of 0.4 for a pass, 0.3 for a warning, or fails otherwise. Then I'm preparing to save all the results to the output directory.

Writing output files and generating plots... Writing summary output...

Actually, I'm realizing the two-pass approach is inefficient. Running separate forward passes for attention and MLP pruning means processing the same data twice, which adds up quickly—roughly 8-17 minutes total across both models. If I combine both hooks into a single forward pass, I can cut that down to 4-8 minutes. Let me refactor the activation collection to gather both attention and MLP activations simultaneously.

Setting up hook functions... Setting up forward hooks to capture activations...

Now I'm removing the hooks and processing the attention outputs layer by layer, reshaping the query tensors to group them by key-value heads and averaging across the sequence dimension, then stacking everything together and converting to float precision.

Processing MLP gate outputs similarly, reshaping them into groups based on the retained channels, averaging across the sequence, and stacking the results before returning both activation dictionaries.

Now I'm integrating this into the final implementation. I could keep separate functions for flexibility, but I'll stick with the combined approach for simplicity. I need to add the `n_gqa_groups` parameter—it's only needed during the recoverability computations which happen after the model loads, so I can derive it from the model config rather than requiring a CLI argument, though I'll keep it as an explicit arg with Qwen2.5-7B defaults for clarity.

Let me verify the indexing logic works correctly when we have pruned attention groups—if the original model has 4 groups and we're keeping indices [0, 1, 3], the pruned group 2 will correctly access the CKA matrix and overlap arrays. The logic checks out. I'll write this to the local system first before deploying to the server.

Actually, I'm wondering if I can optimize the forward passes—currently running two separate passes for each model, but maybe I could combine them with shared hooks to reduce redundant computation.

Wait, no—we need separate model instances for the pruned and recovered versions, so two forward passes is unavoidable. The real optimization is collecting both attention and MLP activations in a single pass per model instead of doing separate passes for each type. That cuts the runtime in half for the most expensive part of the process.

Let me finalize and save the file now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "6f0fe7c5-8539-4733-b540-9b5b13435335",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsW3kgdiv8Kj6HPyxfQxjM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2127,
      "cache_read_input_tokens": 69330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2127
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

_source line 55_

完全理解了所有文件。关键发现：

1. **cka_overlap.py**: `mlp_cka_matrix` 已存在 ✓
2. **prune.py**: `mlp_keep_masks` 已在 `pruning_metadata.pt` 中保存 ✓
3. **correlation_analysis.py**: 仅有 attention 级别分析，且现有的 `n_heads=28` 与 GQA group 粒度不匹配（CKA matrix 是 [4,4] 而非 [28,28]）
4. **importance_score.py**: `n_mlp_groups = n_heads = 28`, `group_size = intermediate_size // 28`

现在写扩展后的 correlation_analysis.py。修正 attention 的 GQA group 粒度问题，同时新增 MLP 级别分析和 combined 统计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "c189d54f-501d-4695-af77-7be95bf717b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsW3kgdiv8Kj6HPyxfQxjM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2127,
      "cache_read_input_tokens": 69330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2127
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

_source line 56_

<details open><summary>🔧 Tool call — Write · `toolu_01HSn94TjE9L9KcqyBUwi55Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/correlation_analysis.py",
  "content": "\"\"\"\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\n\nTests the hypothesis: pruned structures (GQA groups or MLP channel groups) with\nhigher CKA overlap F(g) are more effectively compensated by RLVR through their\nmost similar retained structure.\n\nMetric: for each pruned structure g_p, find the most CKA-similar retained\nstructure g_r, then measure g_r's activation shift between pruned and\nRLVR-recovered models.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nimport torch.nn.functional as F\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(saved_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(saved_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model\n\n\ndef collect_all_activations(model, calibration_data, attn_keep_masks, mlp_keep_masks, device):\n    \"\"\"Collect both GQA-group and MLP-group activations in a single forward pass.\n\n    Returns:\n        attn_acts: dict[layer_idx] -> tensor[n_samples, n_retained_gqa, heads_per_kv * head_dim]\n        mlp_acts:  dict[layer_idx] -> tensor[n_samples, n_retained_mlp, group_size]\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    head_dim = config.hidden_size // n_heads\n    heads_per_kv = n_heads // n_kv_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_q_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    def make_gate_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h1 = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_q_hook(i))\n        h2 = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_gate_hook(i))\n        hooks.extend([h1, h2])\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 50 == 0:\n                logger.info(f\"  Processed {idx + 1}/{len(calibration_data)} samples\")\n\n    for h in hooks:\n        h.remove()\n\n    attn_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained_gqa = len(attn_keep_masks[layer_idx])\n        per_group = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained_gqa * heads_per_kv * head_dim]\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv, head_dim)\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv * head_dim)\n            t = t.mean(dim=0)  # [n_retained_gqa, heads_per_kv * head_dim]\n            per_group.append(t)\n        attn_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    mlp_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained = len(mlp_keep_masks[layer_idx])\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained * group_size]\n            total_channels = t.shape[-1]\n            group_size = total_channels // n_retained\n            usable = n_retained * group_size\n            t = t[:, :usable].view(t.shape[0], n_retained, group_size)\n            t = t.mean(dim=0)  # [n_retained, group_size]\n            per_group.append(t)\n        mlp_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return attn_activations, mlp_activations\n\n\ndef compute_attn_recoverability(pruned_acts, recovered_acts, cka_data, attn_keep_masks,\n                                n_gqa_groups_original):\n    attn_overlap = cka_data[\"attn_overlap\"]\n    attn_cka_matrix = cka_data[\"attn_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(attn_keep_masks.keys()):\n        retained = attn_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_gqa_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = attn_cka_matrix[layer_idx]\n\n        for g_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[g_p, g_r].item() for g_r in retained])\n            best_idx = sims.argmax().item()\n            g_r = retained[best_idx]\n            g_r_local = retained.index(g_r)\n\n            act_p = pruned_acts[layer_idx][:, g_r_local, :]\n            act_r = recovered_acts[layer_idx][:, g_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"attention\",\n                \"pruned_group\": g_p,\n                \"best_retained_group\": g_r,\n                \"cka_overlap\": attn_overlap[layer_idx][g_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef compute_mlp_recoverability(pruned_acts, recovered_acts, cka_data, mlp_keep_masks,\n                               n_mlp_groups_original):\n    mlp_overlap = cka_data[\"mlp_overlap\"]\n    mlp_cka_matrix = cka_data[\"mlp_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(mlp_keep_masks.keys()):\n        retained = mlp_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_mlp_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = mlp_cka_matrix[layer_idx]\n\n        for m_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[m_p, m_r].item() for m_r in retained])\n            best_idx = sims.argmax().item()\n            m_r = retained[best_idx]\n            m_r_local = retained.index(m_r)\n\n            act_p = pruned_acts[layer_idx][:, m_r_local, :]\n            act_r = recovered_acts[layer_idx][:, m_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"mlp\",\n                \"pruned_group\": m_p,\n                \"best_retained_group\": m_r,\n                \"cka_overlap\": mlp_overlap[layer_idx][m_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    n = len(x)\n    rhos = []\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, n, replace=True)\n        r, _ = stats.spearmanr(x[idx], y[idx])\n        if not np.isnan(r):\n            rhos.append(r)\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\n\n\ndef permutation_test(x, y, n_perm=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    observed, _ = stats.spearmanr(x, y)\n    count = 0\n    for _ in range(n_perm):\n        r, _ = stats.spearmanr(x, rng.permutation(y))\n        if abs(r) >= abs(observed):\n            count += 1\n    return count / n_perm\n\n\ndef compute_correlation_stats(fh, rec, seed=42):\n    if len(fh) < 3:\n        return {\n            \"spearman_rho\": float(\"nan\"), \"p_value\": float(\"nan\"),\n            \"bootstrap_ci_95\": [float(\"nan\"), float(\"nan\")],\n            \"permutation_p_value\": float(\"nan\"),\n            \"n_pruned_groups\": len(fh),\n        }\n    rho, p_value = stats.spearmanr(fh, rec)\n    ci = bootstrap_spearman(fh, rec, seed=seed)\n    perm_p = permutation_test(fh, rec, seed=seed)\n    return {\n        \"spearman_rho\": rho, \"p_value\": p_value,\n        \"bootstrap_ci_95\": ci, \"permutation_p_value\": perm_p,\n        \"n_pruned_groups\": len(fh),\n    }\n\n\ndef make_scatter_plot(results, stat, output_path, title_prefix=\"\", color_by_type=False):\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n    except ImportError:\n        logger.warning(\"matplotlib not available, skipping scatter plot\")\n        return\n\n    fh = [r[\"cka_overlap\"] for r in results]\n    rec = [r[\"recoverability\"] for r in results]\n    rho = stat[\"spearman_rho\"]\n    p_value = stat[\"p_value\"]\n    ci = stat[\"bootstrap_ci_95\"]\n    perm_p = stat.get(\"permutation_p_value\", float(\"nan\"))\n\n    fig, ax = plt.subplots(figsize=(8, 6))\n\n    if color_by_type:\n        type_colors = {\"attention\": \"#1f77b4\", \"mlp\": \"#ff7f0e\"}\n        for stype, color in type_colors.items():\n            mask = [r[\"type\"] == stype for r in results]\n            x = [f for f, m in zip(fh, mask) if m]\n            y = [r for r, m in zip(rec, mask) if m]\n            if x:\n                ax.scatter(x, y, c=color, alpha=0.7, edgecolors=\"k\",\n                           linewidths=0.3, s=30, label=stype)\n        ax.legend()\n    else:\n        layers = [r[\"layer\"] for r in results]\n        sc = ax.scatter(fh, rec, c=layers, cmap=\"viridis\", alpha=0.7,\n                        edgecolors=\"k\", linewidths=0.3, s=30)\n        plt.colorbar(sc, ax=ax, label=\"Layer index\")\n\n    ax.set_xlabel(\"F(g) — CKA overlap of pruned structure\")\n    ax.set_ylabel(\"Recoverability — activation shift of best retained structure\")\n\n    verdict = \"PASS\" if rho >= 0.4 else (\"WARNING\" if rho >= 0.3 else \"FAIL\")\n    ax.set_title(\n        f\"{title_prefix}CKA Overlap vs RLVR Recoverability\\n\"\n        f\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \"\n        f\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\"\n    )\n    plt.tight_layout()\n    plt.savefig(output_path, dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    logger.info(f\"Scatter plot saved to {output_path}\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Correlation analysis: rho(CKA overlap, RLVR recoverability) \"\n                    \"for attention GQA groups and MLP channel groups\"\n    )\n    parser.add_argument(\"--base_model_path\", required=True,\n                        help=\"Path to original unpruned model\")\n    parser.add_argument(\"--pruned_model_path\", required=True,\n                        help=\"Path to pruned model (before RLVR)\")\n    parser.add_argument(\"--recovered_model_path\", required=True,\n                        help=\"Path to RLVR-recovered model\")\n    parser.add_argument(\"--cka_scores_path\", required=True,\n                        help=\"Path to CKA overlap .pt file\")\n    parser.add_argument(\"--pruning_mask_path\", required=True,\n                        help=\"Path to pruning_metadata.pt\")\n    parser.add_argument(\"--n_samples\", type=int, default=128,\n                        help=\"Number of calibration samples\")\n    parser.add_argument(\"--n_gqa_groups\", type=int, default=4,\n                        help=\"Number of original GQA groups (KV heads) per layer\")\n    parser.add_argument(\"--n_mlp_groups\", type=int, default=28,\n                        help=\"Number of original MLP channel groups per layer\")\n    parser.add_argument(\"--output_dir\", default=\"results/analysis/\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading CKA scores...\")\n    cka_data = torch.load(args.cka_scores_path, map_location=\"cpu\", weights_only=True)\n    for key in (\"attn_cka_matrix\", \"mlp_cka_matrix\"):\n        if key not in cka_data:\n            raise ValueError(f\"CKA scores missing '{key}'. Re-run cka_overlap.py.\")\n\n    logger.info(\"Loading pruning metadata...\")\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\"cpu\",\n                              weights_only=True)\n    attn_keep_masks = pruning_meta[\"attn_keep_masks\"]\n    mlp_keep_masks = pruning_meta[\"mlp_keep_masks\"]\n\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\n    logger.info(f\"Loaded {len(calibration_data)} calibration samples\")\n\n    # --- Pruned model ---\n    logger.info(f\"Loading pruned model from {args.pruned_model_path}\")\n    pruned_model = load_pruned_model(\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from pruned model...\")\n    pruned_attn_acts, pruned_mlp_acts = collect_all_activations(\n        pruned_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del pruned_model\n    torch.cuda.empty_cache()\n\n    # --- Recovered model ---\n    logger.info(f\"Loading recovered model from {args.recovered_model_path}\")\n    recovered_model = load_pruned_model(\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from recovered model...\")\n    recovered_attn_acts, recovered_mlp_acts = collect_all_activations(\n        recovered_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del recovered_model\n    torch.cuda.empty_cache()\n\n    # --- Attention recoverability ---\n    logger.info(\"Computing attention recoverability...\")\n    attn_results = compute_attn_recoverability(\n        pruned_attn_acts, recovered_attn_acts, cka_data,\n        attn_keep_masks, args.n_gqa_groups,\n    )\n    del pruned_attn_acts, recovered_attn_acts\n    logger.info(f\"Computed recoverability for {len(attn_results)} pruned GQA groups\")\n\n    # --- MLP recoverability ---\n    logger.info(\"Computing MLP recoverability...\")\n    mlp_results = compute_mlp_recoverability(\n        pruned_mlp_acts, recovered_mlp_acts, cka_data,\n        mlp_keep_masks, args.n_mlp_groups,\n    )\n    del pruned_mlp_acts, recovered_mlp_acts\n    logger.info(f\"Computed recoverability for {len(mlp_results)} pruned MLP groups\")\n\n    # --- Statistics ---\n    attn_fh = [r[\"cka_overlap\"] for r in attn_results]\n    attn_rec = [r[\"recoverability\"] for r in attn_results]\n    attn_stats = compute_correlation_stats(attn_fh, attn_rec, seed=args.seed)\n\n    mlp_fh = [r[\"cka_overlap\"] for r in mlp_results]\n    mlp_rec = [r[\"recoverability\"] for r in mlp_results]\n    mlp_stats = compute_correlation_stats(mlp_fh, mlp_rec, seed=args.seed)\n\n    combined_results = attn_results + mlp_results\n    combined_fh = [r[\"cka_overlap\"] for r in combined_results]\n    combined_rec = [r[\"recoverability\"] for r in combined_results]\n    combined_stats = compute_correlation_stats(combined_fh, combined_rec, seed=args.seed)\n    combined_stats[\"n_total_pruned\"] = len(combined_results)\n\n    combined_rho = combined_stats[\"spearman_rho\"]\n    verdict = \"PASS\" if combined_rho >= 0.4 else (\n        \"WARNING\" if combined_rho >= 0.3 else \"FAIL\")\n\n    # --- Save results ---\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    output = {\n        \"attention\": {**attn_stats, \"per_group_data\": attn_results},\n        \"mlp\": {**mlp_stats, \"per_group_data\": mlp_results},\n        \"combined\": combined_stats,\n        \"mvp_verdict\": verdict,\n    }\n    json_path = os.path.join(args.output_dir, \"correlation_results.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {json_path}\")\n\n    # --- Scatter plots ---\n    if attn_results:\n        make_scatter_plot(\n            attn_results, attn_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_attention.png\"),\n            title_prefix=\"Attention: \",\n        )\n    if mlp_results:\n        make_scatter_plot(\n            mlp_results, mlp_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_mlp.png\"),\n            title_prefix=\"MLP: \",\n        )\n    if combined_results:\n        make_scatter_plot(\n            combined_results, combined_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_combined.png\"),\n            title_prefix=\"Combined: \",\n            color_by_type=True,\n        )\n\n    # --- Summary ---\n    print(f\"\\n{'='*60}\")\n    print(\"Correlation Analysis Results (Attention + MLP)\")\n    print(f\"{'='*60}\")\n    if attn_results:\n        print(f\"  ATTENTION: rho={attn_stats['spearman_rho']:.4f}, \"\n              f\"p={attn_stats['p_value']:.2e}, N={len(attn_results)}\")\n    else:\n        print(\"  ATTENTION: no pruned groups\")\n    if mlp_results:\n        print(f\"  MLP:       rho={mlp_stats['spearman_rho']:.4f}, \"\n              f\"p={mlp_stats['p_value']:.2e}, N={len(mlp_results)}\")\n    else:\n        print(\"  MLP:       no pruned groups\")\n    print(f\"  COMBINED:  rho={combined_rho:.4f}, \"\n          f\"p={combined_stats['p_value']:.2e}, N={len(combined_results)}\")\n    print(f\"  95% CI:    [{combined_stats['bootstrap_ci_95'][0]:.4f}, \"\n          f\"{combined_stats['bootstrap_ci_95'][1]:.4f}]\")\n    print(f\"  MVP Verdict: {verdict}\")\n    print(f\"{'='*60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "c9c810fb-7006-4529-b500-120faef2f019",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsW3kgdiv8Kj6HPyxfQxjM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2127,
      "cache_read_input_tokens": 69330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2127
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

_source line 57 · 2026-05-14T05:36:19.105Z_

<details><summary>↩ Tool result · `toolu_01HSn94TjE9L9KcqyBUwi55Y`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/correlation_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "b3fd94d8-8889-4991-91c0-9e6cbc9642f0",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/correlation_analysis.py",
    "content": "\"\"\"\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\n\nTests the hypothesis: pruned structures (GQA groups or MLP channel groups) with\nhigher CKA overlap F(g) are more effectively compensated by RLVR through their\nmost similar retained structure.\n\nMetric: for each pruned structure g_p, find the most CKA-similar retained\nstructure g_r, then measure g_r's activation shift between pruned and\nRLVR-recovered models.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nimport torch.nn.functional as F\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(saved_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(saved_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model\n\n\ndef collect_all_activations(model, calibration_data, attn_keep_masks, mlp_keep_masks, device):\n    \"\"\"Collect both GQA-group and MLP-group activations in a single forward pass.\n\n    Returns:\n        attn_acts: dict[layer_idx] -> tensor[n_samples, n_retained_gqa, heads_per_kv * head_dim]\n        mlp_acts:  dict[layer_idx] -> tensor[n_samples, n_retained_mlp, group_size]\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    head_dim = config.hidden_size // n_heads\n    heads_per_kv = n_heads // n_kv_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_q_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    def make_gate_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h1 = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_q_hook(i))\n        h2 = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_gate_hook(i))\n        hooks.extend([h1, h2])\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 50 == 0:\n                logger.info(f\"  Processed {idx + 1}/{len(calibration_data)} samples\")\n\n    for h in hooks:\n        h.remove()\n\n    attn_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained_gqa = len(attn_keep_masks[layer_idx])\n        per_group = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained_gqa * heads_per_kv * head_dim]\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv, head_dim)\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv * head_dim)\n            t = t.mean(dim=0)  # [n_retained_gqa, heads_per_kv * head_dim]\n            per_group.append(t)\n        attn_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    mlp_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained = len(mlp_keep_masks[layer_idx])\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained * group_size]\n            total_channels = t.shape[-1]\n            group_size = total_channels // n_retained\n            usable = n_retained * group_size\n            t = t[:, :usable].view(t.shape[0], n_retained, group_size)\n            t = t.mean(dim=0)  # [n_retained, group_size]\n            per_group.append(t)\n        mlp_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return attn_activations, mlp_activations\n\n\ndef compute_attn_recoverability(pruned_acts, recovered_acts, cka_data, attn_keep_masks,\n                                n_gqa_groups_original):\n    attn_overlap = cka_data[\"attn_overlap\"]\n    attn_cka_matrix = cka_data[\"attn_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(attn_keep_masks.keys()):\n        retained = attn_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_gqa_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = attn_cka_matrix[layer_idx]\n\n        for g_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[g_p, g_r].item() for g_r in retained])\n            best_idx = sims.argmax().item()\n            g_r = retained[best_idx]\n            g_r_local = retained.index(g_r)\n\n            act_p = pruned_acts[layer_idx][:, g_r_local, :]\n            act_r = recovered_acts[layer_idx][:, g_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"attention\",\n                \"pruned_group\": g_p,\n                \"best_retained_group\": g_r,\n                \"cka_overlap\": attn_overlap[layer_idx][g_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef compute_mlp_recoverability(pruned_acts, recovered_acts, cka_data, mlp_keep_masks,\n                               n_mlp_groups_original):\n    mlp_overlap = cka_data[\"mlp_overlap\"]\n    mlp_cka_matrix = cka_data[\"mlp_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(mlp_keep_masks.keys()):\n        retained = mlp_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_mlp_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = mlp_cka_matrix[layer_idx]\n\n        for m_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[m_p, m_r].item() for m_r in retained])\n            best_idx = sims.argmax().item()\n            m_r = retained[best_idx]\n            m_r_local = retained.index(m_r)\n\n            act_p = pruned_acts[layer_idx][:, m_r_local, :]\n            act_r = recovered_acts[layer_idx][:, m_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"mlp\",\n                \"pruned_group\": m_p,\n                \"best_retained_group\": m_r,\n                \"cka_overlap\": mlp_overlap[layer_idx][m_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    n = len(x)\n    rhos = []\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, n, replace=True)\n        r, _ = stats.spearmanr(x[idx], y[idx])\n        if not np.isnan(r):\n            rhos.append(r)\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\n\n\ndef permutation_test(x, y, n_perm=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    observed, _ = stats.spearmanr(x, y)\n    count = 0\n    for _ in range(n_perm):\n        r, _ = stats.spearmanr(x, rng.permutation(y))\n        if abs(r) >= abs(observed):\n            count += 1\n    return count / n_perm\n\n\ndef compute_correlation_stats(fh, rec, seed=42):\n    if len(fh) < 3:\n        return {\n            \"spearman_rho\": float(\"nan\"), \"p_value\": float(\"nan\"),\n            \"bootstrap_ci_95\": [float(\"nan\"), float(\"nan\")],\n            \"permutation_p_value\": float(\"nan\"),\n            \"n_pruned_groups\": len(fh),\n        }\n    rho, p_value = stats.spearmanr(fh, rec)\n    ci = bootstrap_spearman(fh, rec, seed=seed)\n    perm_p = permutation_test(fh, rec, seed=seed)\n    return {\n        \"spearman_rho\": rho, \"p_value\": p_value,\n        \"bootstrap_ci_95\": ci, \"permutation_p_value\": perm_p,\n        \"n_pruned_groups\": len(fh),\n    }\n\n\ndef make_scatter_plot(results, stat, output_path, title_prefix=\"\", color_by_type=False):\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n    except ImportError:\n        logger.warning(\"matplotlib not available, skipping scatter plot\")\n        return\n\n    fh = [r[\"cka_overlap\"] for r in results]\n    rec = [r[\"recoverability\"] for r in results]\n    rho = stat[\"spearman_rho\"]\n    p_value = stat[\"p_value\"]\n    ci = stat[\"bootstrap_ci_95\"]\n    perm_p = stat.get(\"permutation_p_value\", float(\"nan\"))\n\n    fig, ax = plt.subplots(figsize=(8, 6))\n\n    if color_by_type:\n        type_colors = {\"attention\": \"#1f77b4\", \"mlp\": \"#ff7f0e\"}\n        for stype, color in type_colors.items():\n            mask = [r[\"type\"] == stype for r in results]\n            x = [f for f, m in zip(fh, mask) if m]\n            y = [r for r, m in zip(rec, mask) if m]\n            if x:\n                ax.scatter(x, y, c=color, alpha=0.7, edgecolors=\"k\",\n                           linewidths=0.3, s=30, label=stype)\n        ax.legend()\n    else:\n        layers = [r[\"layer\"] for r in results]\n        sc = ax.scatter(fh, rec, c=layers, cmap=\"viridis\", alpha=0.7,\n                        edgecolors=\"k\", linewidths=0.3, s=30)\n        plt.colorbar(sc, ax=ax, label=\"Layer index\")\n\n    ax.set_xlabel(\"F(g) — CKA overlap of pruned structure\")\n    ax.set_ylabel(\"Recoverability — activation shift of best retained structure\")\n\n    verdict = \"PASS\" if rho >= 0.4 else (\"WARNING\" if rho >= 0.3 else \"FAIL\")\n    ax.set_title(\n        f\"{title_prefix}CKA Overlap vs RLVR Recoverability\\n\"\n        f\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \"\n        f\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\"\n    )\n    plt.tight_layout()\n    plt.savefig(output_path, dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    logger.info(f\"Scatter plot saved to {output_path}\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Correlation analysis: rho(CKA overlap, RLVR recoverability) \"\n                    \"for attention GQA groups and MLP channel groups\"\n    )\n    parser.add_argument(\"--base_model_path\", required=True,\n                        help=\"Path to original unpruned model\")\n    parser.add_argument(\"--pruned_model_path\", required=True,\n                        help=\"Path to pruned model (before RLVR)\")\n    parser.add_argument(\"--recovered_model_path\", required=True,\n                        help=\"Path to RLVR-recovered model\")\n    parser.add_argument(\"--cka_scores_path\", required=True,\n                        help=\"Path to CKA overlap .pt file\")\n    parser.add_argument(\"--pruning_mask_path\", required=True,\n                        help=\"Path to pruning_metadata.pt\")\n    parser.add_argument(\"--n_samples\", type=int, default=128,\n                        help=\"Number of calibration samples\")\n    parser.add_argument(\"--n_gqa_groups\", type=int, default=4,\n                        help=\"Number of original GQA groups (KV heads) per layer\")\n    parser.add_argument(\"--n_mlp_groups\", type=int, default=28,\n                        help=\"Number of original MLP channel groups per layer\")\n    parser.add_argument(\"--output_dir\", default=\"results/analysis/\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading CKA scores...\")\n    cka_data = torch.load(args.cka_scores_path, map_location=\"cpu\", weights_only=True)\n    for key in (\"attn_cka_matrix\", \"mlp_cka_matrix\"):\n        if key not in cka_data:\n            raise ValueError(f\"CKA scores missing '{key}'. Re-run cka_overlap.py.\")\n\n    logger.info(\"Loading pruning metadata...\")\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\"cpu\",\n                              weights_only=True)\n    attn_keep_masks = pruning_meta[\"attn_keep_masks\"]\n    mlp_keep_masks = pruning_meta[\"mlp_keep_masks\"]\n\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\n    logger.info(f\"Loaded {len(calibration_data)} calibration samples\")\n\n    # --- Pruned model ---\n    logger.info(f\"Loading pruned model from {args.pruned_model_path}\")\n    pruned_model = load_pruned_model(\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from pruned model...\")\n    pruned_attn_acts, pruned_mlp_acts = collect_all_activations(\n        pruned_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del pruned_model\n    torch.cuda.empty_cache()\n\n    # --- Recovered model ---\n    logger.info(f\"Loading recovered model from {args.recovered_model_path}\")\n    recovered_model = load_pruned_model(\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from recovered model...\")\n    recovered_attn_acts, recovered_mlp_acts = collect_all_activations(\n        recovered_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del recovered_model\n    torch.cuda.empty_cache()\n\n    # --- Attention recoverability ---\n    logger.info(\"Computing attention recoverability...\")\n    attn_results = compute_attn_recoverability(\n        pruned_attn_acts, recovered_attn_acts, cka_data,\n        attn_keep_masks, args.n_gqa_groups,\n    )\n    del pruned_attn_acts, recovered_attn_acts\n    logger.info(f\"Computed recoverability for {len(attn_results)} pruned GQA groups\")\n\n    # --- MLP recoverability ---\n    logger.info(\"Computing MLP recoverability...\")\n    mlp_results = compute_mlp_recoverability(\n        pruned_mlp_acts, recovered_mlp_acts, cka_data,\n        mlp_keep_masks, args.n_mlp_groups,\n    )\n    del pruned_mlp_acts, recovered_mlp_acts\n    logger.info(f\"Computed recoverability for {len(mlp_results)} pruned MLP groups\")\n\n    # --- Statistics ---\n    attn_fh = [r[\"cka_overlap\"] for r in attn_results]\n    attn_rec = [r[\"recoverability\"] for r in attn_results]\n    attn_stats = compute_correlation_stats(attn_fh, attn_rec, seed=args.seed)\n\n    mlp_fh = [r[\"cka_overlap\"] for r in mlp_results]\n    mlp_rec = [r[\"recoverability\"] for r in mlp_results]\n    mlp_stats = compute_correlation_stats(mlp_fh, mlp_rec, seed=args.seed)\n\n    combined_results = attn_results + mlp_results\n    combined_fh = [r[\"cka_overlap\"] for r in combined_results]\n    combined_rec = [r[\"recoverability\"] for r in combined_results]\n    combined_stats = compute_correlation_stats(combined_fh, combined_rec, seed=args.seed)\n    combined_stats[\"n_total_pruned\"] = len(combined_results)\n\n    combined_rho = combined_stats[\"spearman_rho\"]\n    verdict = \"PASS\" if combined_rho >= 0.4 else (\n        \"WARNING\" if combined_rho >= 0.3 else \"FAIL\")\n\n    # --- Save results ---\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    output = {\n        \"attention\": {**attn_stats, \"per_group_data\": attn_results},\n        \"mlp\": {**mlp_stats, \"per_group_data\": mlp_results},\n        \"combined\": combined_stats,\n        \"mvp_verdict\": verdict,\n    }\n    json_path = os.path.join(args.output_dir, \"correlation_results.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {json_path}\")\n\n    # --- Scatter plots ---\n    if attn_results:\n        make_scatter_plot(\n            attn_results, attn_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_attention.png\"),\n            title_prefix=\"Attention: \",\n        )\n    if mlp_results:\n        make_scatter_plot(\n            mlp_results, mlp_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_mlp.png\"),\n            title_prefix=\"MLP: \",\n        )\n    if combined_results:\n        make_scatter_plot(\n            combined_results, combined_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_combined.png\"),\n            title_prefix=\"Combined: \",\n            color_by_type=True,\n        )\n\n    # --- Summary ---\n    print(f\"\\n{'='*60}\")\n    print(\"Correlation Analysis Results (Attention + MLP)\")\n    print(f\"{'='*60}\")\n    if attn_results:\n        print(f\"  ATTENTION: rho={attn_stats['spearman_rho']:.4f}, \"\n              f\"p={attn_stats['p_value']:.2e}, N={len(attn_results)}\")\n    else:\n        print(\"  ATTENTION: no pruned groups\")\n    if mlp_results:\n        print(f\"  MLP:       rho={mlp_stats['spearman_rho']:.4f}, \"\n              f\"p={mlp_stats['p_value']:.2e}, N={len(mlp_results)}\")\n    else:\n        print(\"  MLP:       no pruned groups\")\n    print(f\"  COMBINED:  rho={combined_rho:.4f}, \"\n          f\"p={combined_stats['p_value']:.2e}, N={len(combined_results)}\")\n    print(f\"  95% CI:    [{combined_stats['bootstrap_ci_95'][0]:.4f}, \"\n          f\"{combined_stats['bootstrap_ci_95'][1]:.4f}]\")\n    print(f\"  MVP Verdict: {verdict}\")\n    print(f\"{'='*60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Now I need to deploy this to the server. Let me use ssh_execute to write the file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "f22cbee9-abcc-4ca8-8f17-ece501594e11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfcWFpdeXGsQeawvNjQ3ho",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21528,
      "cache_read_input_tokens": 71457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21528
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

_source line 59_

部署到服务器。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "ded09c2d-7db5-487a-8f9a-8ca12e5dc062",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfcWFpdeXGsQeawvNjQ3ho",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21528,
      "cache_read_input_tokens": 71457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21528
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

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_017W96DRx92Wwq1FEwfPAWnu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/correlation_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "09c1d56e-ebea-4a37-977e-840c73d309c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfcWFpdeXGsQeawvNjQ3ho",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21528,
      "cache_read_input_tokens": 71457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21528
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

_source line 61 · 2026-05-14T05:36:24.570Z_

<details><summary>↩ Tool result · `toolu_017W96DRx92Wwq1FEwfPAWnu`</summary>

```text
1	"""
2	Correlation Analysis: rho(CKA overlap, RLVR recoverability).
3	
4	Tests the hypothesis: pruned structures (GQA groups or MLP channel groups) with
5	higher CKA overlap F(g) are more effectively compensated by RLVR through their
6	most similar retained structure.
7	
8	Metric: for each pruned structure g_p, find the most CKA-similar retained
9	structure g_r, then measure g_r's activation shift between pruned and
10	RLVR-recovered models.
11	"""
12	
13	import argparse
14	import json
15	import logging
16	import os
17	import random
18	
19	import numpy as np
20	import scipy.stats as stats
21	import torch
22	import torch.nn.functional as F
23	from datasets import load_dataset
24	from transformers import AutoModelForCausalLM, AutoTokenizer
25	
26	logging.basicConfig(
27	    level=logging.INFO,
28	    format="%(asctime)s [%(levelname)s] %(message)s",
29	)
30	logger = logging.getLogger(__name__)
31	
32	
33	def set_seed(seed: int):
34	    random.seed(seed)
35	    np.random.seed(seed)
36	    torch.manual_seed(seed)
37	    torch.cuda.manual_seed_all(seed)
38	
39	
40	def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
41	    ds = load_dataset("openai/gsm8k", "main", split="train")
42	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
43	    encodings = []
44	    for example in ds:
45	        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
46	        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
47	        encodings.append(ids)
48	    return encodings
49	
50	
51	def load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):
52	    logging.getLogger("prune").setLevel(logging.WARNING)
53	    from prune import prune_attention_heads, prune_mlp_channels
54	
55	    model = AutoModelForCausalLM.from_pretrained(
56	        base_model_path, torch_dtype=torch_dtype, device_map="cpu", trust_remote_code=True
57	    )
58	    prune_attention_heads(model, pruning_meta["attn_keep_masks"])
59	    prune_mlp_channels(model, pruning_meta["mlp_keep_masks"])
60	
61	    safetensor_files = sorted(
62	        [f for f in os.listdir(saved_model_path) if f.endswith(".safetensors")]
63	    )
64	    if safetensor_files:
65	        from safetensors.torch import load_file
66	        state_dict = {}
67	        for f in safetensor_files:
68	            state_dict.update(load_file(os.path.join(saved_model_path, f)))
69	    else:
70	        state_dict = torch.load(
71	            os.path.join(saved_model_path, "pytorch_model.bin"),
72	            map_location="cpu", weights_only=True,
73	        )
74	
75	    model.load_state_dict(state_dict)
76	    model.to(device)
77	    return model
78	
79	
80	def collect_all_activations(model, calibration_data, attn_keep_masks, mlp_keep_masks, device):
81	    """Collect both GQA-group and MLP-group activations in a single forward pass.
82	
83	    Returns:
84	        attn_acts: dict[layer_idx] -> tensor[n_samples, n_retained_gqa, heads_per_kv * head_dim]
85	        mlp_acts:  dict[layer_idx] -> tensor[n_samples, n_retained_mlp, group_size]
86	    """
87	    config = model.config
88	    n_layers = config.num_hidden_layers
89	    n_heads = config.num_attention_heads
90	    n_kv_heads = config.num_key_value_heads
91	    head_dim = config.hidden_size // n_heads
92	    heads_per_kv = n_heads // n_kv_heads
93	
94	    q_outputs = {i: [] for i in range(n_layers)}
95	    gate_outputs = {i: [] for i in range(n_layers)}
96	    hooks = []
97	
98	    def make_q_hook(layer_idx):
99	        def fn(module, inp, out):
100	            q_outputs[layer_idx].append(out.detach().cpu())
101	        return fn
102	
103	    def make_gate_hook(layer_idx):
104	        def fn(module, inp, out):
105	            gate_outputs[layer_idx].append(out.detach().cpu())
106	        return fn
107	
108	    for i in range(n_layers):
109	        h1 = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_q_hook(i))
110	        h2 = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_gate_hook(i))
111	        hooks.extend([h1, h2])
112	
113	    model.eval()
114	    with torch.no_grad():
115	        for idx, enc in enumerate(calibration_data):
116	            input_ids = enc["input_ids"].to(device)
117	            attention_mask = enc["attention_mask"].to(device)
118	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
119	            if (idx + 1) % 50 == 0:
120	                logger.info(f"  Processed {idx + 1}/{len(calibration_data)} samples")
121	
122	    for h in hooks:
123	        h.remove()
124	
125	    attn_activations = {}
126	    for layer_idx in range(n_layers):
127	        n_retained_gqa = len(attn_keep_masks[layer_idx])
128	        per_group = []
129	        for t in q_outputs[layer_idx]:
130	            t = t.squeeze(0)  # [seq, n_retained_gqa * heads_per_kv * head_dim]
131	            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv, head_dim)
132	            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv * head_dim)
133	            t = t.mean(dim=0)  # [n_retained_gqa, heads_per_kv * head_dim]
134	            per_group.append(t)
135	        attn_activations[layer_idx] = torch.stack(per_group, dim=0).float()
136	        q_outputs[layer_idx] = None
137	
138	    mlp_activations = {}
139	    for layer_idx in range(n_layers):
140	        n_retained = len(mlp_keep_masks[layer_idx])
141	        per_group = []
142	        for t in gate_outputs[layer_idx]:
143	            t = t.squeeze(0)  # [seq, n_retained * group_size]
144	            total_channels = t.shape[-1]
145	            group_size = total_channels // n_retained
146	            usable = n_retained * group_size
147	            t = t[:, :usable].view(t.shape[0], n_retained, group_size)
148	            t = t.mean(dim=0)  # [n_retained, group_size]
149	            per_group.append(t)
150	        mlp_activations[layer_idx] = torch.stack(per_group, dim=0).float()
151	        gate_outputs[layer_idx] = None
152	
153	    return attn_activations, mlp_activations
154	
155	
156	def compute_attn_recoverability(pruned_acts, recovered_acts, cka_data, attn_keep_masks,
157	                                n_gqa_groups_original):
158	    attn_overlap = cka_data["attn_overlap"]
159	    attn_cka_matrix = cka_data["attn_cka_matrix"]
160	    results = []
161	
162	    for layer_idx in sorted(attn_keep_masks.keys()):
163	        retained = attn_keep_masks[layer_idx]
164	        pruned_groups = sorted(set(range(n_gqa_groups_original)) - set(retained))
165	        if not pruned_groups:
166	            continue
167	
168	        cka_matrix = attn_cka_matrix[layer_idx]
169	
170	        for g_p in pruned_groups:
171	            sims = torch.tensor([cka_matrix[g_p, g_r].item() for g_r in retained])
172	            best_idx = sims.argmax().item()
173	            g_r = retained[best_idx]
174	            g_r_local = retained.index(g_r)
175	
176	            act_p = pruned_acts[layer_idx][:, g_r_local, :]
177	            act_r = recovered_acts[layer_idx][:, g_r_local, :]
178	            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)
179	            activation_shift = 1.0 - cos_sim.mean().item()
180	
181	            results.append({
182	                "layer": layer_idx,
183	                "type": "attention",
184	                "pruned_group": g_p,
185	                "best_retained_group": g_r,
186	                "cka_overlap": attn_overlap[layer_idx][g_p].item(),
187	                "recoverability": activation_shift,
188	                "cka_similarity_to_retained": sims[best_idx].item(),
189	            })
190	
191	    return results
192	
193	
194	def compute_mlp_recoverability(pruned_acts, recovered_acts, cka_data, mlp_keep_masks,
195	                               n_mlp_groups_original):
196	    mlp_overlap = cka_data["mlp_overlap"]
197	    mlp_cka_matrix = cka_data["mlp_cka_matrix"]
198	    results = []
199	
200	    for layer_idx in sorted(mlp_keep_masks.keys()):
201	        retained = mlp_keep_masks[layer_idx]
202	        pruned_groups = sorted(set(range(n_mlp_groups_original)) - set(retained))
203	        if not pruned_groups:
204	            continue
205	
206	        cka_matrix = mlp_cka_matrix[layer_idx]
207	
208	        for m_p in pruned_groups:
209	            sims = torch.tensor([cka_matrix[m_p, m_r].item() for m_r in retained])
210	            best_idx = sims.argmax().item()
211	            m_r = retained[best_idx]
212	            m_r_local = retained.index(m_r)
213	
214	            act_p = pruned_acts[layer_idx][:, m_r_local, :]
215	            act_r = recovered_acts[layer_idx][:, m_r_local, :]
216	            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)
217	            activation_shift = 1.0 - cos_sim.mean().item()
218	
219	            results.append({
220	                "layer": layer_idx,
221	                "type": "mlp",
222	                "pruned_group": m_p,
223	                "best_retained_group": m_r,
224	                "cka_overlap": mlp_overlap[layer_idx][m_p].item(),
225	                "recoverability": activation_shift,
226	                "cka_similarity_to_retained": sims[best_idx].item(),
227	            })
228	
229	    return results
230	
231	
232	def bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):
233	    rng = np.random.RandomState(seed)
234	    x, y = np.array(x), np.array(y)
235	    n = len(x)
236	    rhos = []
237	    for _ in range(n_bootstrap):
238	        idx = rng.choice(n, n, replace=True)
239	        r, _ = stats.spearmanr(x[idx], y[idx])
240	        if not np.isnan(r):
241	            rhos.append(r)
242	    return np.percentile(rhos, [2.5, 97.5]).tolist()
243	
244	
245	def permutation_test(x, y, n_perm=10000, seed=42):
246	    rng = np.random.RandomState(seed)
247	    x, y = np.array(x), np.array(y)
248	    observed, _ = stats.spearmanr(x, y)
249	    count = 0
250	    for _ in range(n_perm):
251	        r, _ = stats.spearmanr(x, rng.permutation(y))
252	        if abs(r) >= abs(observed):
253	            count += 1
254	    return count / n_perm
255	
256	
257	def compute_correlation_stats(fh, rec, seed=42):
258	    if len(fh) < 3:
259	        return {
260	            "spearman_rho": float("nan"), "p_value": float("nan"),
261	            "bootstrap_ci_95": [float("nan"), float("nan")],
262	            "permutation_p_value": float("nan"),
263	            "n_pruned_groups": len(fh),
264	        }
265	    rho, p_value = stats.spearmanr(fh, rec)
266	    ci = bootstrap_spearman(fh, rec, seed=seed)
267	    perm_p = permutation_test(fh, rec, seed=seed)
268	    return {
269	        "spearman_rho": rho, "p_value": p_value,
270	        "bootstrap_ci_95": ci, "permutation_p_value": perm_p,
271	        "n_pruned_groups": len(fh),
272	    }
273	
274	
275	def make_scatter_plot(results, stat, output_path, title_prefix="", color_by_type=False):
276	    try:
277	        import matplotlib
278	        matplotlib.use("Agg")
279	        import matplotlib.pyplot as plt
280	    except ImportError:
281	        logger.warning("matplotlib not available, skipping scatter plot")
282	        return
283	
284	    fh = [r["cka_overlap"] for r in results]
285	    rec = [r["recoverability"] for r in results]
286	    rho = stat["spearman_rho"]
287	    p_value = stat["p_value"]
288	    ci = stat["bootstrap_ci_95"]
289	    perm_p = stat.get("permutation_p_value", float("nan"))
290	
291	    fig, ax = plt.subplots(figsize=(8, 6))
292	
293	    if color_by_type:
294	        type_colors = {"attention": "#1f77b4", "mlp": "#ff7f0e"}
295	        for stype, color in type_colors.items():
296	            mask = [r["type"] == stype for r in results]
297	            x = [f for f, m in zip(fh, mask) if m]
298	            y = [r for r, m in zip(rec, mask) if m]
299	            if x:
300	                ax.scatter(x, y, c=color, alpha=0.7, edgecolors="k",
301	                           linewidths=0.3, s=30, label=stype)
302	        ax.legend()
303	    else:
304	        layers = [r["layer"] for r in results]
305	        sc = ax.scatter(fh, rec, c=layers, cmap="viridis", alpha=0.7,
306	                        edgecolors="k", linewidths=0.3, s=30)
307	        plt.colorbar(sc, ax=ax, label="Layer index")
308	
309	    ax.set_xlabel("F(g) — CKA overlap of pruned structure")
310	    ax.set_ylabel("Recoverability — activation shift of best retained structure")
311	
312	    verdict = "PASS" if rho >= 0.4 else ("WARNING" if rho >= 0.3 else "FAIL")
313	    ax.set_title(
314	        f"{title_prefix}CKA Overlap vs RLVR Recoverability\n"
315	        f"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], "
316	        f"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}"
317	    )
318	    plt.tight_layout()
319	    plt.savefig(output_path, dpi=150, bbox_inches="tight")
320	    plt.close()
321	    logger.info(f"Scatter plot saved to {output_path}")
322	
323	
324	def main():
325	    parser = argparse.ArgumentParser(
326	        description="Correlation analysis: rho(CKA overlap, RLVR recoverability) "
327	                    "for attention GQA groups and MLP channel groups"
328	    )
329	    parser.add_argument("--base_model_path", required=True,
330	                        help="Path to original unpruned model")
331	    parser.add_argument("--pruned_model_path", required=True,
332	                        help="Path to pruned model (before RLVR)")
333	    parser.add_argument("--recovered_model_path", required=True,
334	                        help="Path to RLVR-recovered model")
335	    parser.add_argument("--cka_scores_path", required=True,
336	                        help="Path to CKA overlap .pt file")
337	    parser.add_argument("--pruning_mask_path", required=True,
338	                        help="Path to pruning_metadata.pt")
339	    parser.add_argument("--n_samples", type=int, default=128,
340	                        help="Number of calibration samples")
341	    parser.add_argument("--n_gqa_groups", type=int, default=4,
342	                        help="Number of original GQA groups (KV heads) per layer")
343	    parser.add_argument("--n_mlp_groups", type=int, default=28,
344	                        help="Number of original MLP channel groups per layer")
345	    parser.add_argument("--output_dir", default="results/analysis/",
346	                        help="Output directory")
347	    parser.add_argument("--seed", type=int, default=42)
348	    parser.add_argument("--dtype", type=str, default="bfloat16",
349	                        choices=["float16", "bfloat16", "float32"])
350	    args = parser.parse_args()
351	
352	    set_seed(args.seed)
353	    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
354	    torch_dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16,
355	                   "float32": torch.float32}[args.dtype]
356	
357	    logger.info("Loading CKA scores...")
358	    cka_data = torch.load(args.cka_scores_path, map_location="cpu", weights_only=True)
359	    for key in ("attn_cka_matrix", "mlp_cka_matrix"):
360	        if key not in cka_data:
361	            raise ValueError(f"CKA scores missing '{key}'. Re-run cka_overlap.py.")
362	
363	    logger.info("Loading pruning metadata...")
364	    pruning_meta = torch.load(args.pruning_mask_path, map_location="cpu",
365	                              weights_only=True)
366	    attn_keep_masks = pruning_meta["attn_keep_masks"]
367	    mlp_keep_masks = pruning_meta["mlp_keep_masks"]
368	
369	    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)
370	    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)
371	    logger.info(f"Loaded {len(calibration_data)} calibration samples")
372	
373	    # --- Pruned model ---
374	    logger.info(f"Loading pruned model from {args.pruned_model_path}")
375	    pruned_model = load_pruned_model(
376	        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device
377	    )
378	    logger.info("Collecting activations from pruned model...")
379	    pruned_attn_acts, pruned_mlp_acts = collect_all_activations(
380	        pruned_model, calibration_data, attn_keep_masks, mlp_keep_masks, device
381	    )
382	    del pruned_model
383	    torch.cuda.empty_cache()
384	
385	    # --- Recovered model ---
386	    logger.info(f"Loading recovered model from {args.recovered_model_path}")
387	    recovered_model = load_pruned_model(
388	        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device
389	    )
390	    logger.info("Collecting activations from recovered model...")
391	    recovered_attn_acts, recovered_mlp_acts = collect_all_activations(
392	        recovered_model, calibration_data, attn_keep_masks, mlp_keep_masks, device
393	    )
394	    del recovered_model
395	    torch.cuda.empty_cache()
396	
397	    # --- Attention recoverability ---
398	    logger.info("Computing attention recoverability...")
399	    attn_results = compute_attn_recoverability(
400	        pruned_attn_acts, recovered_attn_acts, cka_data,
401	        attn_keep_masks, args.n_gqa_groups,
402	    )
403	    del pruned_attn_acts, recovered_attn_acts
404	    logger.info(f"Computed recoverability for {len(attn_results)} pruned GQA groups")
405	
406	    # --- MLP recoverability ---
407	    logger.info("Computing MLP recoverability...")
408	    mlp_results = compute_mlp_recoverability(
409	        pruned_mlp_acts, recovered_mlp_acts, cka_data,
410	        mlp_keep_masks, args.n_mlp_groups,
411	    )
412	    del pruned_mlp_acts, recovered_mlp_acts
413	    logger.info(f"Computed recoverability for {len(mlp_results)} pruned MLP groups")
414	
415	    # --- Statistics ---
416	    attn_fh = [r["cka_overlap"] for r in attn_results]
417	    attn_rec = [r["recoverability"] for r in attn_results]
418	    attn_stats = compute_correlation_stats(attn_fh, attn_rec, seed=args.seed)
419	
420	    mlp_fh = [r["cka_overlap"] for r in mlp_results]
421	    mlp_rec = [r["recoverability"] for r in mlp_results]
422	    mlp_stats = compute_correlation_stats(mlp_fh, mlp_rec, seed=args.seed)
423	
424	    combined_results = attn_results + mlp_results
425	    combined_fh = [r["cka_overlap"] for r in combined_results]
426	    combined_rec = [r["recoverability"] for r in combined_results]
427	    combined_stats = compute_correlation_stats(combined_fh, combined_rec, seed=args.seed)
428	    combined_stats["n_total_pruned"] = len(combined_results)
429	
430	    combined_rho = combined_stats["spearman_rho"]
431	    verdict = "PASS" if combined_rho >= 0.4 else (
432	        "WARNING" if combined_rho >= 0.3 else "FAIL")
433	
434	    # --- Save results ---
435	    os.makedirs(args.output_dir, exist_ok=True)
436	
437	    output = {
438	        "attention": {**attn_stats, "per_group_data": attn_results},
439	        "mlp": {**mlp_stats, "per_group_data": mlp_results},
440	        "combined": combined_stats,
441	        "mvp_verdict": verdict,
442	    }
443	    json_path = os.path.join(args.output_dir, "correlation_results.json")
444	    with open(json_path, "w") as f:
445	        json.dump(output, f, indent=2)
446	    logger.info(f"Results saved to {json_path}")
447	
448	    # --- Scatter plots ---
449	    if attn_results:
450	        make_scatter_plot(
451	            attn_results, attn_stats,
452	            os.path.join(args.output_dir, "fh_vs_recoverability_attention.png"),
453	            title_prefix="Attention: ",
454	        )
455	    if mlp_results:
456	        make_scatter_plot(
457	            mlp_results, mlp_stats,
458	            os.path.join(args.output_dir, "fh_vs_recoverability_mlp.png"),
459	            title_prefix="MLP: ",
460	        )
461	    if combined_results:
462	        make_scatter_plot(
463	            combined_results, combined_stats,
464	            os.path.join(args.output_dir, "fh_vs_recoverability_combined.png"),
465	            title_prefix="Combined: ",
466	            color_by_type=True,
467	        )
468	
469	    # --- Summary ---
470	    print(f"\n{'='*60}")
471	    print("Correlation Analysis Results (Attention + MLP)")
472	    print(f"{'='*60}")
473	    if attn_results:
474	        print(f"  ATTENTION: rho={attn_stats['spearman_rho']:.4f}, "
475	              f"p={attn_stats['p_value']:.2e}, N={len(attn_results)}")
476	    else:
477	        print("  ATTENTION: no pruned groups")
478	    if mlp_results:
479	        print(f"  MLP:       rho={mlp_stats['spearman_rho']:.4f}, "
480	              f"p={mlp_stats['p_value']:.2e}, N={len(mlp_results)}")
481	    else:
482	        print("  MLP:       no pruned groups")
483	    print(f"  COMBINED:  rho={combined_rho:.4f}, "
484	          f"p={combined_stats['p_value']:.2e}, N={len(combined_results)}")
485	    print(f"  95% CI:    [{combined_stats['bootstrap_ci_95'][0]:.4f}, "
486	          f"{combined_stats['bootstrap_ci_95'][1]:.4f}]")
487	    print(f"  MVP Verdict: {verdict}")
488	    print(f"{'='*60}")
489	
490	
491	if __name__ == "__main__":
492	    main()
493	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "7d9dbd89-c263-4f81-bc05-6fd6a3aecbfc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/correlation_analysis.py",
      "content": "\"\"\"\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\n\nTests the hypothesis: pruned structures (GQA groups or MLP channel groups) with\nhigher CKA overlap F(g) are more effectively compensated by RLVR through their\nmost similar retained structure.\n\nMetric: for each pruned structure g_p, find the most CKA-similar retained\nstructure g_r, then measure g_r's activation shift between pruned and\nRLVR-recovered models.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nimport torch.nn.functional as F\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(saved_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(saved_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model\n\n\ndef collect_all_activations(model, calibration_data, attn_keep_masks, mlp_keep_masks, device):\n    \"\"\"Collect both GQA-group and MLP-group activations in a single forward pass.\n\n    Returns:\n        attn_acts: dict[layer_idx] -> tensor[n_samples, n_retained_gqa, heads_per_kv * head_dim]\n        mlp_acts:  dict[layer_idx] -> tensor[n_samples, n_retained_mlp, group_size]\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    head_dim = config.hidden_size // n_heads\n    heads_per_kv = n_heads // n_kv_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_q_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    def make_gate_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h1 = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_q_hook(i))\n        h2 = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_gate_hook(i))\n        hooks.extend([h1, h2])\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 50 == 0:\n                logger.info(f\"  Processed {idx + 1}/{len(calibration_data)} samples\")\n\n    for h in hooks:\n        h.remove()\n\n    attn_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained_gqa = len(attn_keep_masks[layer_idx])\n        per_group = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained_gqa * heads_per_kv * head_dim]\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv, head_dim)\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv * head_dim)\n            t = t.mean(dim=0)  # [n_retained_gqa, heads_per_kv * head_dim]\n            per_group.append(t)\n        attn_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    mlp_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained = len(mlp_keep_masks[layer_idx])\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained * group_size]\n            total_channels = t.shape[-1]\n            group_size = total_channels // n_retained\n            usable = n_retained * group_size\n            t = t[:, :usable].view(t.shape[0], n_retained, group_size)\n            t = t.mean(dim=0)  # [n_retained, group_size]\n            per_group.append(t)\n        mlp_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return attn_activations, mlp_activations\n\n\ndef compute_attn_recoverability(pruned_acts, recovered_acts, cka_data, attn_keep_masks,\n                                n_gqa_groups_original):\n    attn_overlap = cka_data[\"attn_overlap\"]\n    attn_cka_matrix = cka_data[\"attn_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(attn_keep_masks.keys()):\n        retained = attn_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_gqa_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = attn_cka_matrix[layer_idx]\n\n        for g_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[g_p, g_r].item() for g_r in retained])\n            best_idx = sims.argmax().item()\n            g_r = retained[best_idx]\n            g_r_local = retained.index(g_r)\n\n            act_p = pruned_acts[layer_idx][:, g_r_local, :]\n            act_r = recovered_acts[layer_idx][:, g_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"attention\",\n                \"pruned_group\": g_p,\n                \"best_retained_group\": g_r,\n                \"cka_overlap\": attn_overlap[layer_idx][g_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef compute_mlp_recoverability(pruned_acts, recovered_acts, cka_data, mlp_keep_masks,\n                               n_mlp_groups_original):\n    mlp_overlap = cka_data[\"mlp_overlap\"]\n    mlp_cka_matrix = cka_data[\"mlp_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(mlp_keep_masks.keys()):\n        retained = mlp_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_mlp_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = mlp_cka_matrix[layer_idx]\n\n        for m_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[m_p, m_r].item() for m_r in retained])\n            best_idx = sims.argmax().item()\n            m_r = retained[best_idx]\n            m_r_local = retained.index(m_r)\n\n            act_p = pruned_acts[layer_idx][:, m_r_local, :]\n            act_r = recovered_acts[layer_idx][:, m_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"mlp\",\n                \"pruned_group\": m_p,\n                \"best_retained_group\": m_r,\n                \"cka_overlap\": mlp_overlap[layer_idx][m_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    n = len(x)\n    rhos = []\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, n, replace=True)\n        r, _ = stats.spearmanr(x[idx], y[idx])\n        if not np.isnan(r):\n            rhos.append(r)\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\n\n\ndef permutation_test(x, y, n_perm=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    observed, _ = stats.spearmanr(x, y)\n    count = 0\n    for _ in range(n_perm):\n        r, _ = stats.spearmanr(x, rng.permutation(y))\n        if abs(r) >= abs(observed):\n            count += 1\n    return count / n_perm\n\n\ndef compute_correlation_stats(fh, rec, seed=42):\n    if len(fh) < 3:\n        return {\n            \"spearman_rho\": float(\"nan\"), \"p_value\": float(\"nan\"),\n            \"bootstrap_ci_95\": [float(\"nan\"), float(\"nan\")],\n            \"permutation_p_value\": float(\"nan\"),\n            \"n_pruned_groups\": len(fh),\n        }\n    rho, p_value = stats.spearmanr(fh, rec)\n    ci = bootstrap_spearman(fh, rec, seed=seed)\n    perm_p = permutation_test(fh, rec, seed=seed)\n    return {\n        \"spearman_rho\": rho, \"p_value\": p_value,\n        \"bootstrap_ci_95\": ci, \"permutation_p_value\": perm_p,\n        \"n_pruned_groups\": len(fh),\n    }\n\n\ndef make_scatter_plot(results, stat, output_path, title_prefix=\"\", color_by_type=False):\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n    except ImportError:\n        logger.warning(\"matplotlib not available, skipping scatter plot\")\n        return\n\n    fh = [r[\"cka_overlap\"] for r in results]\n    rec = [r[\"recoverability\"] for r in results]\n    rho = stat[\"spearman_rho\"]\n    p_value = stat[\"p_value\"]\n    ci = stat[\"bootstrap_ci_95\"]\n    perm_p = stat.get(\"permutation_p_value\", float(\"nan\"))\n\n    fig, ax = plt.subplots(figsize=(8, 6))\n\n    if color_by_type:\n        type_colors = {\"attention\": \"#1f77b4\", \"mlp\": \"#ff7f0e\"}\n        for stype, color in type_colors.items():\n            mask = [r[\"type\"] == stype for r in results]\n            x = [f for f, m in zip(fh, mask) if m]\n            y = [r for r, m in zip(rec, mask) if m]\n            if x:\n                ax.scatter(x, y, c=color, alpha=0.7, edgecolors=\"k\",\n                           linewidths=0.3, s=30, label=stype)\n        ax.legend()\n    else:\n        layers = [r[\"layer\"] for r in results]\n        sc = ax.scatter(fh, rec, c=layers, cmap=\"viridis\", alpha=0.7,\n                        edgecolors=\"k\", linewidths=0.3, s=30)\n        plt.colorbar(sc, ax=ax, label=\"Layer index\")\n\n    ax.set_xlabel(\"F(g) — CKA overlap of pruned structure\")\n    ax.set_ylabel(\"Recoverability — activation shift of best retained structure\")\n\n    verdict = \"PASS\" if rho >= 0.4 else (\"WARNING\" if rho >= 0.3 else \"FAIL\")\n    ax.set_title(\n        f\"{title_prefix}CKA Overlap vs RLVR Recoverability\\n\"\n        f\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \"\n        f\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\"\n    )\n    plt.tight_layout()\n    plt.savefig(output_path, dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    logger.info(f\"Scatter plot saved to {output_path}\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Correlation analysis: rho(CKA overlap, RLVR recoverability) \"\n                    \"for attention GQA groups and MLP channel groups\"\n    )\n    parser.add_argument(\"--base_model_path\", required=True,\n                        help=\"Path to original unpruned model\")\n    parser.add_argument(\"--pruned_model_path\", required=True,\n                        help=\"Path to pruned model (before RLVR)\")\n    parser.add_argument(\"--recovered_model_path\", required=True,\n                        help=\"Path to RLVR-recovered model\")\n    parser.add_argument(\"--cka_scores_path\", required=True,\n                        help=\"Path to CKA overlap .pt file\")\n    parser.add_argument(\"--pruning_mask_path\", required=True,\n                        help=\"Path to pruning_metadata.pt\")\n    parser.add_argument(\"--n_samples\", type=int, default=128,\n                        help=\"Number of calibration samples\")\n    parser.add_argument(\"--n_gqa_groups\", type=int, default=4,\n                        help=\"Number of original GQA groups (KV heads) per layer\")\n    parser.add_argument(\"--n_mlp_groups\", type=int, default=28,\n                        help=\"Number of original MLP channel groups per layer\")\n    parser.add_argument(\"--output_dir\", default=\"results/analysis/\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading CKA scores...\")\n    cka_data = torch.load(args.cka_scores_path, map_location=\"cpu\", weights_only=True)\n    for key in (\"attn_cka_matrix\", \"mlp_cka_matrix\"):\n        if key not in cka_data:\n            raise ValueError(f\"CKA scores missing '{key}'. Re-run cka_overlap.py.\")\n\n    logger.info(\"Loading pruning metadata...\")\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\"cpu\",\n                              weights_only=True)\n    attn_keep_masks = pruning_meta[\"attn_keep_masks\"]\n    mlp_keep_masks = pruning_meta[\"mlp_keep_masks\"]\n\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\n    logger.info(f\"Loaded {len(calibration_data)} calibration samples\")\n\n    # --- Pruned model ---\n    logger.info(f\"Loading pruned model from {args.pruned_model_path}\")\n    pruned_model = load_pruned_model(\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from pruned model...\")\n    pruned_attn_acts, pruned_mlp_acts = collect_all_activations(\n        pruned_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del pruned_model\n    torch.cuda.empty_cache()\n\n    # --- Recovered model ---\n    logger.info(f\"Loading recovered model from {args.recovered_model_path}\")\n    recovered_model = load_pruned_model(\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from recovered model...\")\n    recovered_attn_acts, recovered_mlp_acts = collect_all_activations(\n        recovered_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del recovered_model\n    torch.cuda.empty_cache()\n\n    # --- Attention recoverability ---\n    logger.info(\"Computing attention recoverability...\")\n    attn_results = compute_attn_recoverability(\n        pruned_attn_acts, recovered_attn_acts, cka_data,\n        attn_keep_masks, args.n_gqa_groups,\n    )\n    del pruned_attn_acts, recovered_attn_acts\n    logger.info(f\"Computed recoverability for {len(attn_results)} pruned GQA groups\")\n\n    # --- MLP recoverability ---\n    logger.info(\"Computing MLP recoverability...\")\n    mlp_results = compute_mlp_recoverability(\n        pruned_mlp_acts, recovered_mlp_acts, cka_data,\n        mlp_keep_masks, args.n_mlp_groups,\n    )\n    del pruned_mlp_acts, recovered_mlp_acts\n    logger.info(f\"Computed recoverability for {len(mlp_results)} pruned MLP groups\")\n\n    # --- Statistics ---\n    attn_fh = [r[\"cka_overlap\"] for r in attn_results]\n    attn_rec = [r[\"recoverability\"] for r in attn_results]\n    attn_stats = compute_correlation_stats(attn_fh, attn_rec, seed=args.seed)\n\n    mlp_fh = [r[\"cka_overlap\"] for r in mlp_results]\n    mlp_rec = [r[\"recoverability\"] for r in mlp_results]\n    mlp_stats = compute_correlation_stats(mlp_fh, mlp_rec, seed=args.seed)\n\n    combined_results = attn_results + mlp_results\n    combined_fh = [r[\"cka_overlap\"] for r in combined_results]\n    combined_rec = [r[\"recoverability\"] for r in combined_results]\n    combined_stats = compute_correlation_stats(combined_fh, combined_rec, seed=args.seed)\n    combined_stats[\"n_total_pruned\"] = len(combined_results)\n\n    combined_rho = combined_stats[\"spearman_rho\"]\n    verdict = \"PASS\" if combined_rho >= 0.4 else (\n        \"WARNING\" if combined_rho >= 0.3 else \"FAIL\")\n\n    # --- Save results ---\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    output = {\n        \"attention\": {**attn_stats, \"per_group_data\": attn_results},\n        \"mlp\": {**mlp_stats, \"per_group_data\": mlp_results},\n        \"combined\": combined_stats,\n        \"mvp_verdict\": verdict,\n    }\n    json_path = os.path.join(args.output_dir, \"correlation_results.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {json_path}\")\n\n    # --- Scatter plots ---\n    if attn_results:\n        make_scatter_plot(\n            attn_results, attn_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_attention.png\"),\n            title_prefix=\"Attention: \",\n        )\n    if mlp_results:\n        make_scatter_plot(\n            mlp_results, mlp_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_mlp.png\"),\n            title_prefix=\"MLP: \",\n        )\n    if combined_results:\n        make_scatter_plot(\n            combined_results, combined_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_combined.png\"),\n            title_prefix=\"Combined: \",\n            color_by_type=True,\n        )\n\n    # --- Summary ---\n    print(f\"\\n{'='*60}\")\n    print(\"Correlation Analysis Results (Attention + MLP)\")\n    print(f\"{'='*60}\")\n    if attn_results:\n        print(f\"  ATTENTION: rho={attn_stats['spearman_rho']:.4f}, \"\n              f\"p={attn_stats['p_value']:.2e}, N={len(attn_results)}\")\n    else:\n        print(\"  ATTENTION: no pruned groups\")\n    if mlp_results:\n        print(f\"  MLP:       rho={mlp_stats['spearman_rho']:.4f}, \"\n              f\"p={mlp_stats['p_value']:.2e}, N={len(mlp_results)}\")\n    else:\n        print(\"  MLP:       no pruned groups\")\n    print(f\"  COMBINED:  rho={combined_rho:.4f}, \"\n          f\"p={combined_stats['p_value']:.2e}, N={len(combined_results)}\")\n    print(f\"  95% CI:    [{combined_stats['bootstrap_ci_95'][0]:.4f}, \"\n          f\"{combined_stats['bootstrap_ci_95'][1]:.4f}]\")\n    print(f\"  MVP Verdict: {verdict}\")\n    print(f\"{'='*60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 493,
      "startLine": 1,
      "totalLines": 493
    }
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01SipVgyW2WHu6eao9RgstRT`</summary>

```json
{
  "server": "westb-23072",
  "command": "cat > /root/recovery_aware_struct_prune/src/correlation_analysis.py << 'FILEEOF'\n\"\"\"\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\n\nTests the hypothesis: pruned structures (GQA groups or MLP channel groups) with\nhigher CKA overlap F(g) are more effectively compensated by RLVR through their\nmost similar retained structure.\n\nMetric: for each pruned structure g_p, find the most CKA-similar retained\nstructure g_r, then measure g_r's activation shift between pruned and\nRLVR-recovered models.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nimport torch.nn.functional as F\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(saved_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(saved_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model\n\n\ndef collect_all_activations(model, calibration_data, attn_keep_masks, mlp_keep_masks, device):\n    \"\"\"Collect both GQA-group and MLP-group activations in a single forward pass.\n\n    Returns:\n        attn_acts: dict[layer_idx] -> tensor[n_samples, n_retained_gqa, heads_per_kv * head_dim]\n        mlp_acts:  dict[layer_idx] -> tensor[n_samples, n_retained_mlp, group_size]\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    head_dim = config.hidden_size // n_heads\n    heads_per_kv = n_heads // n_kv_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_q_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    def make_gate_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h1 = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_q_hook(i))\n        h2 = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_gate_hook(i))\n        hooks.extend([h1, h2])\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 50 == 0:\n                logger.info(f\"  Processed {idx + 1}/{len(calibration_data)} samples\")\n\n    for h in hooks:\n        h.remove()\n\n    attn_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained_gqa = len(attn_keep_masks[layer_idx])\n        per_group = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained_gqa * heads_per_kv * head_dim]\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv, head_dim)\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv * head_dim)\n            t = t.mean(dim=0)  # [n_retained_gqa, heads_per_kv * head_dim]\n            per_group.append(t)\n        attn_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    mlp_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained = len(mlp_keep_masks[layer_idx])\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained * group_size]\n            total_channels = t.shape[-1]\n            group_size = total_channels // n_retained\n            usable = n_retained * group_size\n            t = t[:, :usable].view(t.shape[0], n_retained, group_size)\n            t = t.mean(dim=0)  # [n_retained, group_size]\n            per_group.append(t)\n        mlp_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return attn_activations, mlp_activations\n\n\ndef compute_attn_recoverability(pruned_acts, recovered_acts, cka_data, attn_keep_masks,\n                                n_gqa_groups_original):\n    attn_overlap = cka_data[\"attn_overlap\"]\n    attn_cka_matrix = cka_data[\"attn_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(attn_keep_masks.keys()):\n        retained = attn_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_gqa_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = attn_cka_matrix[layer_idx]\n\n        for g_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[g_p, g_r].item() for g_r in retained])\n            best_idx = sims.argmax().item()\n            g_r = retained[best_idx]\n            g_r_local = retained.index(g_r)\n\n            act_p = pruned_acts[layer_idx][:, g_r_local, :]\n            act_r = recovered_acts[layer_idx][:, g_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"attention\",\n                \"pruned_group\": g_p,\n                \"best_retained_group\": g_r,\n                \"cka_overlap\": attn_overlap[layer_idx][g_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef compute_mlp_recoverability(pruned_acts, recovered_acts, cka_data, mlp_keep_masks,\n                               n_mlp_groups_original):\n    mlp_overlap = cka_data[\"mlp_overlap\"]\n    mlp_cka_matrix = cka_data[\"mlp_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(mlp_keep_masks.keys()):\n        retained = mlp_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_mlp_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = mlp_cka_matrix[layer_idx]\n\n        for m_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[m_p, m_r].item() for m_r in retained])\n            best_idx = sims.argmax().item()\n            m_r = retained[best_idx]\n            m_r_local = retained.index(m_r)\n\n            act_p = pruned_acts[layer_idx][:, m_r_local, :]\n            act_r = recovered_acts[layer_idx][:, m_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"mlp\",\n                \"pruned_group\": m_p,\n                \"best_retained_group\": m_r,\n                \"cka_overlap\": mlp_overlap[layer_idx][m_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    n = len(x)\n    rhos = []\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, n, replace=True)\n        r, _ = stats.spearmanr(x[idx], y[idx])\n        if not np.isnan(r):\n            rhos.append(r)\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\n\n\ndef permutation_test(x, y, n_perm=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    observed, _ = stats.spearmanr(x, y)\n    count = 0\n    for _ in range(n_perm):\n        r, _ = stats.spearmanr(x, rng.permutation(y))\n        if abs(r) >= abs(observed):\n            count += 1\n    return count / n_perm\n\n\ndef compute_correlation_stats(fh, rec, seed=42):\n    if len(fh) < 3:\n        return {\n            \"spearman_rho\": float(\"nan\"), \"p_value\": float(\"nan\"),\n            \"bootstrap_ci_95\": [float(\"nan\"), float(\"nan\")],\n            \"permutation_p_value\": float(\"nan\"),\n            \"n_pruned_groups\": len(fh),\n        }\n    rho, p_value = stats.spearmanr(fh, rec)\n    ci = bootstrap_spearman(fh, rec, seed=seed)\n    perm_p = permutation_test(fh, rec, seed=seed)\n    return {\n        \"spearman_rho\": rho, \"p_value\": p_value,\n        \"bootstrap_ci_95\": ci, \"permutation_p_value\": perm_p,\n        \"n_pruned_groups\": len(fh),\n    }\n\n\ndef make_scatter_plot(results, stat, output_path, title_prefix=\"\", color_by_type=False):\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n    except ImportError:\n        logger.warning(\"matplotlib not available, skipping scatter plot\")\n        return\n\n    fh = [r[\"cka_overlap\"] for r in results]\n    rec = [r[\"recoverability\"] for r in results]\n    rho = stat[\"spearman_rho\"]\n    p_value = stat[\"p_value\"]\n    ci = stat[\"bootstrap_ci_95\"]\n    perm_p = stat.get(\"permutation_p_value\", float(\"nan\"))\n\n    fig, ax = plt.subplots(figsize=(8, 6))\n\n    if color_by_type:\n        type_colors = {\"attention\": \"#1f77b4\", \"mlp\": \"#ff7f0e\"}\n        for stype, color in type_colors.items():\n            mask = [r[\"type\"] == stype for r in results]\n            x = [f for f, m in zip(fh, mask) if m]\n            y = [r for r, m in zip(rec, mask) if m]\n            if x:\n                ax.scatter(x, y, c=color, alpha=0.7, edgecolors=\"k\",\n                           linewidths=0.3, s=30, label=stype)\n        ax.legend()\n    else:\n        layers = [r[\"layer\"] for r in results]\n        sc = ax.scatter(fh, rec, c=layers, cmap=\"viridis\", alpha=0.7,\n                        edgecolors=\"k\", linewidths=0.3, s=30)\n        plt.colorbar(sc, ax=ax, label=\"Layer index\")\n\n    ax.set_xlabel(\"F(g) — CKA overlap of pruned structure\")\n    ax.set_ylabel(\"Recoverability — activation shift of best retained structure\")\n\n    verdict = \"PASS\" if rho >= 0.4 else (\"WARNING\" if rho >= 0.3 else \"FAIL\")\n    ax.set_title(\n        f\"{title_prefix}CKA Overlap vs RLVR Recoverability\\n\"\n        f\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \"\n        f\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\"\n    )\n    plt.tight_layout()\n    plt.savefig(output_path, dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    logger.info(f\"Scatter plot saved to {output_path}\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Correlation analysis: rho(CKA overlap, RLVR recoverability) \"\n                    \"for attention GQA groups and MLP channel groups\"\n    )\n    parser.add_argument(\"--base_model_path\", required=True,\n                        help=\"Path to original unpruned model\")\n    parser.add_argument(\"--pruned_model_path\", required=True,\n                        help=\"Path to pruned model (before RLVR)\")\n    parser.add_argument(\"--recovered_model_path\", required=True,\n                        help=\"Path to RLVR-recovered model\")\n    parser.add_argument(\"--cka_scores_path\", required=True,\n                        help=\"Path to CKA overlap .pt file\")\n    parser.add_argument(\"--pruning_mask_path\", required=True,\n                        help=\"Path to pruning_metadata.pt\")\n    parser.add_argument(\"--n_samples\", type=int, default=128,\n                        help=\"Number of calibration samples\")\n    parser.add_argument(\"--n_gqa_groups\", type=int, default=4,\n                        help=\"Number of original GQA groups (KV heads) per layer\")\n    parser.add_argument(\"--n_mlp_groups\", type=int, default=28,\n                        help=\"Number of original MLP channel groups per layer\")\n    parser.add_argument(\"--output_dir\", default=\"results/analysis/\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading CKA scores...\")\n    cka_data = torch.load(args.cka_scores_path, map_location=\"cpu\", weights_only=True)\n    for key in (\"attn_cka_matrix\", \"mlp_cka_matrix\"):\n        if key not in cka_data:\n            raise ValueError(f\"CKA scores missing '{key}'. Re-run cka_overlap.py.\")\n\n    logger.info(\"Loading pruning metadata...\")\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\"cpu\",\n                              weights_only=True)\n    attn_keep_masks = pruning_meta[\"attn_keep_masks\"]\n    mlp_keep_masks = pruning_meta[\"mlp_keep_masks\"]\n\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\n    logger.info(f\"Loaded {len(calibration_data)} calibration samples\")\n\n    # --- Pruned model ---\n    logger.info(f\"Loading pruned model from {args.pruned_model_path}\")\n    pruned_model = load_pruned_model(\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from pruned model...\")\n    pruned_attn_acts, pruned_mlp_acts = collect_all_activations(\n        pruned_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del pruned_model\n    torch.cuda.empty_cache()\n\n    # --- Recovered model ---\n    logger.info(f\"Loading recovered model from {args.recovered_model_path}\")\n    recovered_model = load_pruned_model(\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from recovered model...\")\n    recovered_attn_acts, recovered_mlp_acts = collect_all_activations(\n        recovered_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del recovered_model\n    torch.cuda.empty_cache()\n\n    # --- Attention recoverability ---\n    logger.info(\"Computing attention recoverability...\")\n    attn_results = compute_attn_recoverability(\n        pruned_attn_acts, recovered_attn_acts, cka_data,\n        attn_keep_masks, args.n_gqa_groups,\n    )\n    del pruned_attn_acts, recovered_attn_acts\n    logger.info(f\"Computed recoverability for {len(attn_results)} pruned GQA groups\")\n\n    # --- MLP recoverability ---\n    logger.info(\"Computing MLP recoverability...\")\n    mlp_results = compute_mlp_recoverability(\n        pruned_mlp_acts, recovered_mlp_acts, cka_data,\n        mlp_keep_masks, args.n_mlp_groups,\n    )\n    del pruned_mlp_acts, recovered_mlp_acts\n    logger.info(f\"Computed recoverability for {len(mlp_results)} pruned MLP groups\")\n\n    # --- Statistics ---\n    attn_fh = [r[\"cka_overlap\"] for r in attn_results]\n    attn_rec = [r[\"recoverability\"] for r in attn_results]\n    attn_stats = compute_correlation_stats(attn_fh, attn_rec, seed=args.seed)\n\n    mlp_fh = [r[\"cka_overlap\"] for r in mlp_results]\n    mlp_rec = [r[\"recoverability\"] for r in mlp_results]\n    mlp_stats = compute_correlation_stats(mlp_fh, mlp_rec, seed=args.seed)\n\n    combined_results = attn_results + mlp_results\n    combined_fh = [r[\"cka_overlap\"] for r in combined_results]\n    combined_rec = [r[\"recoverability\"] for r in combined_results]\n    combined_stats = compute_correlation_stats(combined_fh, combined_rec, seed=args.seed)\n    combined_stats[\"n_total_pruned\"] = len(combined_results)\n\n    combined_rho = combined_stats[\"spearman_rho\"]\n    verdict = \"PASS\" if combined_rho >= 0.4 else (\n        \"WARNING\" if combined_rho >= 0.3 else \"FAIL\")\n\n    # --- Save results ---\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    output = {\n        \"attention\": {**attn_stats, \"per_group_data\": attn_results},\n        \"mlp\": {**mlp_stats, \"per_group_data\": mlp_results},\n        \"combined\": combined_stats,\n        \"mvp_verdict\": verdict,\n    }\n    json_path = os.path.join(args.output_dir, \"correlation_results.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {json_path}\")\n\n    # --- Scatter plots ---\n    if attn_results:\n        make_scatter_plot(\n            attn_results, attn_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_attention.png\"),\n            title_prefix=\"Attention: \",\n        )\n    if mlp_results:\n        make_scatter_plot(\n            mlp_results, mlp_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_mlp.png\"),\n            title_prefix=\"MLP: \",\n        )\n    if combined_results:\n        make_scatter_plot(\n            combined_results, combined_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_combined.png\"),\n            title_prefix=\"Combined: \",\n            color_by_type=True,\n        )\n\n    # --- Summary ---\n    print(f\"\\n{'='*60}\")\n    print(\"Correlation Analysis Results (Attention + MLP)\")\n    print(f\"{'='*60}\")\n    if attn_results:\n        print(f\"  ATTENTION: rho={attn_stats['spearman_rho']:.4f}, \"\n              f\"p={attn_stats['p_value']:.2e}, N={len(attn_results)}\")\n    else:\n        print(\"  ATTENTION: no pruned groups\")\n    if mlp_results:\n        print(f\"  MLP:       rho={mlp_stats['spearman_rho']:.4f}, \"\n              f\"p={mlp_stats['p_value']:.2e}, N={len(mlp_results)}\")\n    else:\n        print(\"  MLP:       no pruned groups\")\n    print(f\"  COMBINED:  rho={combined_rho:.4f}, \"\n          f\"p={combined_stats['p_value']:.2e}, N={len(combined_results)}\")\n    print(f\"  95% CI:    [{combined_stats['bootstrap_ci_95'][0]:.4f}, \"\n          f\"{combined_stats['bootstrap_ci_95'][1]:.4f}]\")\n    print(f\"  MVP Verdict: {verdict}\")\n    print(f\"{'='*60}\")\n\n\nif __name__ == \"__main__\":\n    main()\nFILEEOF\necho \"WRITE_OK: $?\"",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "a180852b-fb31-47bf-bd31-c5c60391c930",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzEfJJLcqC1mME7pjrZa5t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7692,
      "cache_read_input_tokens": 92985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7692
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

_source line 63 · 2026-05-14T05:37:46.419Z_

<details><summary>↩ Tool result · `toolu_01SipVgyW2WHu6eao9RgstRT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"WRITE_OK: 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "d78e06dd-6e08-47c0-b358-c09390cb09e8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"WRITE_OK: 0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.84}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"WRITE_OK: 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 64_

验证 --help 输出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "03f19e4c-2d74-45bc-afe8-fab43326d416",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSMx3KWeUb4fjs9PzCEZhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6708,
      "cache_read_input_tokens": 100677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6708
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

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01UE7e4iM4sTBNL14Zuim14T`</summary>

```json
{
  "server": "westb-23072",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune/src && python3 correlation_analysis.py --help",
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
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "1e445702-fe5e-4a0f-8b3f-54b6715cf621",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSMx3KWeUb4fjs9PzCEZhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6708,
      "cache_read_input_tokens": 100677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6708
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

_source line 66 · 2026-05-14T05:37:58.181Z_

<details><summary>↩ Tool result · `toolu_01UE7e4iM4sTBNL14Zuim14T`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: correlation_analysis.py [-h] --base_model_path BASE_MODEL_PATH\\n                               --pruned_model_path PRUNED_MODEL_PATH\\n                               --recovered_model_path RECOVERED_MODEL_PATH\\n                               --cka_scores_path CKA_SCORES_PATH\\n                               --pruning_mask_path PRUNING_MASK_PATH\\n                               [--n_samples N_SAMPLES]\\n                               [--n_gqa_groups N_GQA_GROUPS]\\n                               [--n_mlp_groups N_MLP_GROUPS]\\n                               [--output_dir OUTPUT_DIR] [--seed SEED]\\n                               [--dtype {float16,bfloat16,float32}]\\n\\nCorrelation analysis: rho(CKA overlap, RLVR recoverability) for attention GQA\\ngroups and MLP channel groups\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --base_model_path BASE_MODEL_PATH\\n                        Path to original unpruned model\\n  --pruned_model_path PRUNED_MODEL_PATH\\n                        Path to pruned model (before RLVR)\\n  --recovered_model_path RECOVERED_MODEL_PATH\\n                        Path to RLVR-recovered model\\n  --cka_scores_path CKA_SCORES_PATH\\n                        Path to CKA overlap .pt file\\n  --pruning_mask_path PRUNING_MASK_PATH\\n                        Path to pruning_metadata.pt\\n  --n_samples N_SAMPLES\\n                        Number of calibration samples\\n  --n_gqa_groups N_GQA_GROUPS\\n                        Number of original GQA groups (KV heads) per layer\\n  --n_mlp_groups N_MLP_GROUPS\\n                        Number of original MLP channel groups per layer\\n  --output_dir OUTPUT_DIR\\n                        Output directory\\n  --seed SEED\\n  --dtype {float16,bfloat16,float32}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "e6eab9a7-c91a-4da2-968e-708127524b06",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"usage: correlation_analysis.py [-h] --base_model_path BASE_MODEL_PATH\\\\n                               --pruned_model_path PRUNED_MODEL_PATH\\\\n                               --recovered_model_path RECOVERED_MODEL_PATH\\\\n                               --cka_scores_path CKA_SCORES_PATH\\\\n                               --pruning_mask_path PRUNING_MASK_PATH\\\\n                               [--n_samples N_SAMPLES]\\\\n                               [--n_gqa_groups N_GQA_GROUPS]\\\\n                               [--n_mlp_groups N_MLP_GROUPS]\\\\n                               [--output_dir OUTPUT_DIR] [--seed SEED]\\\\n                               [--dtype {float16,bfloat16,float32}]\\\\n\\\\nCorrelation analysis: rho(CKA overlap, RLVR recoverability) for attention GQA\\\\ngroups and MLP channel groups\\\\n\\\\noptions:\\\\n  -h, --help            show this help message and exit\\\\n  --base_model_path BASE_MODEL_PATH\\\\n                        Path to original unpruned model\\\\n  --pruned_model_path PRUNED_MODEL_PATH\\\\n                        Path to pruned model (before RLVR)\\\\n  --recovered_model_path RECOVERED_MODEL_PATH\\\\n                        Path to RLVR-recovered model\\\\n  --cka_scores_path CKA_SCORES_PATH\\\\n                        Path to CKA overlap .pt file\\\\n  --pruning_mask_path PRUNING_MASK_PATH\\\\n                        Path to pruning_metadata.pt\\\\n  --n_samples N_SAMPLES\\\\n                        Number of calibration samples\\\\n  --n_gqa_groups N_GQA_GROUPS\\\\n                        Number of original GQA groups (KV heads) per layer\\\\n  --n_mlp_groups N_MLP_GROUPS\\\\n                        Number of original MLP channel groups per layer\\\\n  --output_dir OUTPUT_DIR\\\\n                        Output directory\\\\n  --seed SEED\\\\n  --dtype {float16,bfloat16,float32}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"usage: correlation_analysis.py [-h] --base_model_path BASE_MODEL_PATH\\n                               --pruned_model_path PRUNED_MODEL_PATH\\n                               --recovered_model_path RECOVERED_MODEL_PATH\\n                               --cka_scores_path CKA_SCORES_PATH\\n                               --pruning_mask_path PRUNING_MASK_PATH\\n                               [--n_samples N_SAMPLES]\\n                               [--n_gqa_groups N_GQA_GROUPS]\\n                               [--n_mlp_groups N_MLP_GROUPS]\\n                               [--output_dir OUTPUT_DIR] [--seed SEED]\\n                               [--dtype {float16,bfloat16,float32}]\\n\\nCorrelation analysis: rho(CKA overlap, RLVR recoverability) for attention GQA\\ngroups and MLP channel groups\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --base_model_path BASE_MODEL_PATH\\n                        Path to original unpruned model\\n  --pruned_model_path PRUNED_MODEL_PATH\\n                        Path to pruned model (before RLVR)\\n  --recovered_model_path RECOVERED_MODEL_PATH\\n                        Path to RLVR-recovered model\\n  --cka_scores_path CKA_SCORES_PATH\\n                        Path to CKA overlap .pt file\\n  --pruning_mask_path PRUNING_MASK_PATH\\n                        Path to pruning_metadata.pt\\n  --n_samples N_SAMPLES\\n                        Number of calibration samples\\n  --n_gqa_groups N_GQA_GROUPS\\n                        Number of original GQA groups (KV heads) per layer\\n  --n_mlp_groups N_MLP_GROUPS\\n                        Number of original MLP channel groups per layer\\n  --output_dir OUTPUT_DIR\\n                        Output directory\\n  --seed SEED\\n  --dtype {float16,bfloat16,float32}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.77}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 67_

--help 验证通过。汇报：

### 1. cka_overlap.py — 无需修改
`mlp_cka_matrix` 已存在。输出包含 `attn_overlap`, `mlp_overlap`, `attn_cka_matrix`, `mlp_cka_matrix` 四个 key。

### 2. prune.py — 无需修改
`pruning_metadata.pt` 已包含 `attn_keep_masks` 和 `mlp_keep_masks`。

### 3. correlation_analysis.py — 重写完成

**修复的问题**：
- 旧代码用 `n_heads=28`（Q head 数）做 recoverability 计算，但 CKA matrix 是 `[4, 4]`（GQA group 粒度），会 index out of bounds。改为用 `--n_gqa_groups=4`，与 CKA matrix 和 pruning_metadata 的 GQA group 粒度对齐。

**新增内容**：
- `collect_all_activations()` — 单次 forward pass 同时 hook q_proj + gate_proj，收集 attention GQA group 和 MLP group 两种激活，避免重复推理
- `compute_attn_recoverability()` — GQA group 粒度的 attention recoverability
- `compute_mlp_recoverability()` — MLP group 粒度的 recoverability（hook gate_proj，按 group_size 切分 intermediate channels）
- `compute_correlation_stats()` — 统一的统计计算（Spearman rho + bootstrap CI + permutation test），处理 N<3 的退化情况
- 新增 `--n_gqa_groups`（default=4）和 `--n_mlp_groups`（default=28）参数

### 4. 输出格式
```json
{
  "attention": { "spearman_rho", "p_value", "bootstrap_ci_95", "permutation_p_value", "n_pruned_groups", "per_group_data" },
  "mlp":       { ... 同上 ... },
  "combined":  { ... + "n_total_pruned" },
  "mvp_verdict": "PASS/WARNING/FAIL"  // 基于 combined rho
}
```

Scatter plots：
- `fh_vs_recoverability_attention.png`（按 layer 着色）
- `fh_vs_recoverability_mlp.png`（按 layer 着色）
- `fh_vs_recoverability_combined.png`（按 attention/MLP 类型着色，蓝/橙区分）

### 5. --help 验证通过
新增参数 `--n_gqa_groups`, `--n_mlp_groups` 正确显示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "uuid": "8b5331d5-f9ad-4c4e-9dee-f59e5ca5621a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRNGwkYaRtyLiNZzAiHBKJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 107385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 859
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

_source line 68_

--help 验证通过。汇报：

### 1. cka_overlap.py — 无需修改
`mlp_cka_matrix` 已存在。输出包含 `attn_overlap`, `mlp_overlap`, `attn_cka_matrix`, `mlp_cka_matrix` 四个 key。

### 2. prune.py — 无需修改
`pruning_metadata.pt` 已包含 `attn_keep_masks` 和 `mlp_keep_masks`。

### 3. correlation_analysis.py — 重写完成

**修复的问题**：
- 旧代码用 `n_heads=28`（Q head 数）做 recoverability 计算，但 CKA matrix 是 `[4, 4]`（GQA group 粒度），会 index out of bounds。改为用 `--n_gqa_groups=4`，与 CKA matrix 和 pruning_metadata 的 GQA group 粒度对齐。

**新增内容**：
- `collect_all_activations()` — 单次 forward pass 同时 hook q_proj + gate_proj，收集 attention GQA group 和 MLP group 两种激活，避免重复推理
- `compute_attn_recoverability()` — GQA group 粒度的 attention recoverability
- `compute_mlp_recoverability()` — MLP group 粒度的 recoverability（hook gate_proj，按 group_size 切分 intermediate channels）
- `compute_correlation_stats()` — 统一的统计计算（Spearman rho + bootstrap CI + permutation test），处理 N<3 的退化情况
- 新增 `--n_gqa_groups`（default=4）和 `--n_mlp_groups`（default=28）参数

### 4. 输出格式
```json
{
  "attention": { "spearman_rho", "p_value", "bootstrap_ci_95", "permutation_p_value", "n_pruned_groups", "per_group_data" },
  "mlp":       { ... 同上 ... },
  "combined":  { ... + "n_total_pruned" },
  "mvp_verdict": "PASS/WARNING/FAIL"  // 基于 combined rho
}
```

Scatter plots：
- `fh_vs_recoverability_attention.png`（按 layer 着色）
- `fh_vs_recoverability_mlp.png`（按 layer 着色）
- `fh_vs_recoverability_combined.png`（按 attention/MLP 类型着色，蓝/橙区分）

### 5. --help 验证通过
新增参数 `--n_gqa_groups`, `--n_mlp_groups` 正确显示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 603587,
  "duration_api_ms": 588234,
  "num_turns": 23,
  "stop_reason": "end_turn",
  "session_id": "1aba2bb4-5791-4587-af50-c4d407e191c2",
  "total_cost_usd": 2.2119132500000003,
  "usage": {
    "input_tokens": 26,
    "cache_creation_input_tokens": 96403,
    "cache_read_input_tokens": 1059443,
    "output_tokens": 43053,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 96403,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 754,
        "cache_read_input_tokens": 107385,
        "cache_creation_input_tokens": 859,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 859
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3118,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003218,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 26,
      "outputTokens": 43053,
      "cacheReadInputTokens": 1059443,
      "cacheCreationInputTokens": 96403,
      "webSearchRequests": 0,
      "costUSD": 2.20869525,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ef7baca2-9791-4495-9ec4-c2a632ac9d57"
}
```

</details>

---
