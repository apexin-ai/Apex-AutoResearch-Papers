# verify docred ft dr reeval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 107
- **Recorded user turns:** 0
- **Tool calls:** 37
- **Original source:** `logs/workers/worker_verify_docred-ft-dr-reeval_20260523T114011.log`
- **Structured JSON:** [`ed2b24f4fced2cf25bca.json`](../../sessions/ed/ed2b24f4fced2cf25bca.json)

## Before a recorded user message

107 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
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
  "uuid": "e6e289b1-1e4d-4020-a2f0-c62fb3c243f9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/memory/"
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
    "resetsAt": 1779554400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "72738afa-e702-4bf0-9ac1-101b96b3d4a3",
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by finding the output files and evaluation scripts on the server. I'll do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "f4cf910e-c942-4988-b8fd-d30eff71084b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzDvUnc6g8vkBbWopAY1d5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12653,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12653
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TVhvRBBL1zfwfrhRz3dqtH`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
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
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "8d6df581-d56f-4bac-bee0-603a77e550e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzDvUnc6g8vkBbWopAY1d5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12653,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12653
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 6 · 2026-05-23T11:40:26.595Z_

<details><summary>↩ Tool result · `toolu_01TVhvRBBL1zfwfrhRz3dqtH`</summary>

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
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "cd9df894-9dab-4146-859c-d8536e1dcd90",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 7_

开始验证。先并行查找输出文件、评估脚本，以及从 registry 读取这 3 个实验的现有 metrics。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "59243dac-78f3-4f37-8152-5ca96f2e6ab6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wzATX84wz9LcdYtGR4SsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1547,
      "cache_read_input_tokens": 24494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1547
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EpFsXBE9FHLkSqnq62TEnJ`</summary>

```json
{
  "server": "westd-16980",
  "command": "ls -la /root/schema_semantic_constrained_ie/outputs/w8_*docred*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "53159ac4-946f-4c27-9d08-13a2da8811ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wzATX84wz9LcdYtGR4SsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1547,
      "cache_read_input_tokens": 24494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1547
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012axR18UrJhxjqurwUq3UyX`</summary>

```json
{
  "server": "westd-16980",
  "command": "ls -la /root/schema_semantic_constrained_ie/eval_d064.py /root/schema_semantic_constrained_ie/violation_checker.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "3afb0e6a-ee9f-44f2-8796-75c8bd01bc37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wzATX84wz9LcdYtGR4SsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1547,
      "cache_read_input_tokens": 24494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1547
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

_source line 10 · 2026-05-23T11:40:32.893Z_

<details><summary>↩ Tool result · `toolu_01EpFsXBE9FHLkSqnq62TEnJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root  9697858 May 16 14:37 /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_llama_docred.jsonl\\n-rw-r--r-- 1 root root 10260512 May 16 14:37 /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_qwen_docred.jsonl\\n-rw-r--r-- 1 root root      694 May 16 14:37 /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_report_llama_docred.json\\n-rw-r--r-- 1 root root      695 May 16 14:37 /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_report_qwen_docred.json\\n-rw-r--r-- 1 root root  9725208 May 16 20:26 /root/schema_semantic_constrained_ie/outputs/w8_llama_docred_ft_grammar_only.jsonl\\n-rw-r--r-- 1 root root  9691362 May 17 00:49 /root/schema_semantic_constrained_ie/outputs/w8_llama_docred_ft_semantic_only.jsonl\\n-rw-r--r-- 1 root root 10293417 May 22 15:34 /root/schema_semantic_constrained_ie/outputs/w8_qwen_docred_ft_grammar_only.jsonl\\n-rw-r--r-- 1 root root 10342701 May 22 15:34 /root/schema_semantic_constrained_ie/outputs/w8_qwen_docred_ft_semantic_only.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.54}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "8dd99b1c-feb9-48f3-b9e8-29e8593278d5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root  9697858 May 16 14:37 /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_llama_docred.jsonl\\\\n-rw-r--r-- 1 root root 10260512 May 16 14:37 /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_qwen_docred.jsonl\\\\n-rw-r--r-- 1 root root      694 May 16 14:37 /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_report_llama_docred.json\\\\n-rw-r--r-- 1 root root      695 May 16 14:37 /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_report_qwen_docred.json\\\\n-rw-r--r-- 1 root root  9725208 May 16 20:26 /root/schema_semantic_constrained_ie/outputs/w8_llama_docred_ft_grammar_only.jsonl\\\\n-rw-r--r-- 1 root root  9691362 May 17 00:49 /root/schema_semantic_constrained_ie/outputs/w8_llama_docred_ft_semantic_only.jsonl\\\\n-rw-r--r-- 1 root root 10293417 May 22 15:34 /root/schema_semantic_constrained_ie/outputs/w8_qwen_docred_ft_grammar_only.jsonl\\\\n-rw-r--r-- 1 root root 10342701 May 22 15:34 /root/schema_semantic_constrained_ie/outputs/w8_qwen_docred_ft_semantic_only.jsonl\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.54}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root  9697858 May 16 14:37 /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_llama_docred.jsonl\\n-rw-r--r-- 1 root root 10260512 May 16 14:37 /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_qwen_docred.jsonl\\n-rw-r--r-- 1 root root      694 May 16 14:37 /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_report_llama_docred.json\\n-rw-r--r-- 1 root root      695 May 16 14:37 /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_report_qwen_docred.json\\n-rw-r--r-- 1 root root  9725208 May 16 20:26 /root/schema_semantic_constrained_ie/outputs/w8_llama_docred_ft_grammar_only.jsonl\\n-rw-r--r-- 1 root root  9691362 May 17 00:49 /root/schema_semantic_constrained_ie/outputs/w8_llama_docred_ft_semantic_only.jsonl\\n-rw-r--r-- 1 root root 10293417 May 22 15:34 /root/schema_semantic_constrained_ie/outputs/w8_qwen_docred_ft_grammar_only.jsonl\\n-rw-r--r-- 1 root root 10342701 May 22 15:34 /root/schema_semantic_constrained_ie/outputs/w8_qwen_docred_ft_semantic_only.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.54}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T11:40:33.422Z_

<details><summary>↩ Tool result · `toolu_012axR18UrJhxjqurwUq3UyX`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 15988 May 22 15:29 /root/schema_semantic_constrained_ie/violation_checker.py\\n\", \"stderr\": \"ls: cannot access '/root/schema_semantic_constrained_ie/eval_d064.py': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "d34e9d7f-af54-4b01-b7ce-b8ccdc8c6e20",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 15988 May 22 15:29 /root/schema_semantic_constrained_ie/violation_checker.py\\\\n\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/schema_semantic_constrained_ie/eval_d064.py': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 15988 May 22 15:29 /root/schema_semantic_constrained_ie/violation_checker.py\\n\", \"stderr\": \"ls: cannot access '/root/schema_semantic_constrained_ie/eval_d064.py': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01JWwSmGWfFxite41f97ihim`</summary>

```json
{
  "filters": {
    "exp_id": "w8_qwen_docred_ft_semantic_only"
  },
  "project": "schema_semantic_constrained_ie",
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
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "40ae41d4-97f0-4dad-ac6b-791d2aa88018",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wzATX84wz9LcdYtGR4SsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1547,
      "cache_read_input_tokens": 24494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1547
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

_source line 13 · 2026-05-23T11:40:34.151Z_

<details><summary>↩ Tool result · `toolu_01JWwSmGWfFxite41f97ihim`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4782}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "5c7709cc-b20c-4452-b796-65022ae71c4d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4782}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4782}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0177YUQTBW6e3hAZ3zLhbEfS`</summary>

```json
{
  "filters": {
    "exp_id": "w8_llama_docred_ft_semantic_only"
  },
  "project": "schema_semantic_constrained_ie",
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
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "30f353b2-d71c-4be1-afcf-a1073b28ec12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wzATX84wz9LcdYtGR4SsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1547,
      "cache_read_input_tokens": 24494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1547
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

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01EyVfcczXKfQmcxy6ejoG7C`</summary>

```json
{
  "filters": {
    "exp_id": "w8_llama_docred_ft_grammar_only"
  },
  "project": "schema_semantic_constrained_ie",
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
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "9a2bd222-de3e-4e8d-a6fa-0a53385b0654",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wzATX84wz9LcdYtGR4SsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1547,
      "cache_read_input_tokens": 24494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1547
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

_source line 16 · 2026-05-23T11:40:35.730Z_

<details><summary>↩ Tool result · `toolu_0177YUQTBW6e3hAZ3zLhbEfS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5808}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "e3883b96-4d64-489f-9a27-7d3e5c68a7b2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5808}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5808}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T11:40:36.267Z_

<details><summary>↩ Tool result · `toolu_01EyVfcczXKfQmcxy6ejoG7C`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5249}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "4d7e00a6-6caa-402c-8b22-b2273e49e9e9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5249}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5249}}"
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
So:
1. Output files exist for all 3 experiments
2. `eval_d064.py` doesn't exist, but `violation_checker.py` does
3. None of the 3 experiments exist in the registry (0 results for all 3 filters)

Let me check the registry with different filters - the `filters` parameter might not support `exp_id` directly. Let me also check the violation_checker.py usage.

Wait, the registry returned 0 results for all 3 - these experiments might not be in the registry at all, or the filter format might be wrong. 

I should query the registry without any filters to see what experiments are actually stored there, and then look at violation_checker.py to understand how it works and whether there are existing report files that might contain the DR values I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "109bb589-7cdf-451e-af67-22c0300b9d5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbkiktHu4wuEyMcDDThFyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1636,
      "cache_read_input_tokens": 26041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1636
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

_source line 19_

输出文件都在，eval_d064.py 不存在，用 violation_checker.py。3 个实验在 registry 中没找到（filter 可能格式不对）。继续查看 violation_checker.py 用法和 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "3e391409-2c0e-454c-8f22-108c9eae2c38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbkiktHu4wuEyMcDDThFyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1636,
      "cache_read_input_tokens": 26041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1636
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

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Wgxd44kqqJ5H7m7M3RkMde`</summary>

```json
{
  "server": "westd-16980",
  "command": "head -80 /root/schema_semantic_constrained_ie/violation_checker.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "fbafa4ed-6ca1-4ca5-accb-20ea31e15071",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbkiktHu4wuEyMcDDThFyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1636,
      "cache_read_input_tokens": 26041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1636
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

_source line 21 · 2026-05-23T11:40:46.701Z_

<details><summary>↩ Tool result · `toolu_01Wgxd44kqqJ5H7m7M3RkMde`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"# WARNING: This checker is for SciERC only.\\n# For DocRED evaluation, use violation_checker_docred.py instead.\\n# Using this checker on DocRED outputs will produce false RV=100%\\n# because it iterates P-codes as relation names, not natural language labels.\\n\\\"\\\"\\\"Check ontology constraint violations in SciERC extraction outputs.\\n\\nViolation types (mutually exclusive per triple):\\n1. entity_type_violations      - entity type not in ontology's valid type list\\n2. relation_vocabulary_violations - relation name not in ontology (solvable by grammar-constrained decoding)\\n3. domain_range_violations     - relation name valid but (head_type, tail_type) violates constraints (OntoCoDec core target)\\n4. cross_field_consistency_violations - same entity mention has inconsistent types across relations\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\n\\ndef normalize_type(t, valid_types, type_map=None):\\n    \\\"\\\"\\\"Case-insensitive type matching with common aliases.\\\"\\\"\\\"\\n    if type_map is None:\\n        type_map = {\\n            \\\"otherscientificterm\\\": \\\"OtherScientificTerm\\\",\\n            \\\"other-scientificterm\\\": \\\"OtherScientificTerm\\\",\\n            \\\"other_scientific_term\\\": \\\"OtherScientificTerm\\\",\\n            \\\"scientificterm\\\": \\\"OtherScientificTerm\\\",\\n            \\\"other\\\": \\\"OtherScientificTerm\\\",\\n        }\\n    t_lower = t.strip().lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\")\\n    for vt in valid_types:\\n        if t_lower == vt.lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\"):\\n            return vt\\n    if t_lower in type_map:\\n        return type_map[t_lower]\\n    return None\\n\\n\\ndef normalize_relation(rel_name, valid_relation_types):\\n    \\\"\\\"\\\"Fuzzy-match a model-output relation name to the nearest ontology relation.\\n\\n    Match conditions (any one suffices):\\n    1. Exact match (case-insensitive, ignoring spaces/hyphens/underscores)\\n    2. Token overlap > 80%\\n    3. Levenshtein distance <= 2\\n\\n    Returns: (matched_name, is_fuzzy_match) or (None, False)\\n    \\\"\\\"\\\"\\n    rel_norm = rel_name.strip().lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\")\\n    for vrt in valid_relation_types:\\n        if rel_norm == vrt.lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\"):\\n            return vrt, False\\n\\n    rel_tokens = set(rel_name.strip().lower().replace(\\\"-\\\", \\\" \\\").replace(\\\"_\\\", \\\" \\\").split())\\n    for vrt in valid_relation_types:\\n        vrt_tokens = set(vrt.lower().replace(\\\"-\\\", \\\" \\\").replace(\\\"_\\\", \\\" \\\").split())\\n        if rel_tokens and vrt_tokens:\\n            overlap = len(rel_tokens & vrt_tokens)\\n            union = len(rel_tokens | vrt_tokens)\\n            if overlap / union > 0.8:\\n                return vrt, True\\n\\n    for vrt in valid_relation_types:\\n        if _levenshtein(rel_name.strip().lower(), vrt.lower()) <= 2:\\n            return vrt, True\\n\\n    return None, False\\n\\n\\ndef _levenshtein(s1, s2):\\n    if len(s1) < len(s2):\\n        return _levenshtein(s2, s1)\\n    if len(s2) == 0:\\n        return len(s1)\\n    prev_row = range(len(s2) + 1)\\n    for i, c1 in enumerate(s1):\\n        curr_row = [i + 1]\\n        for j, c2 in enumerate(s2):\\n            insertions = prev_row[j + 1] + 1\\n            deletions = curr_row[j] + 1\\n            substitutions = prev_row[j] + (c1 != c2)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "089525a4-d516-41c9-8eb1-312d53a15bca",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"# WARNING: This checker is for SciERC only.\\\\n# For DocRED evaluation, use violation_checker_docred.py instead.\\\\n# Using this checker on DocRED outputs will produce false RV=100%\\\\n# because it iterates P-codes as relation names, not natural language labels.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Check ontology constraint violations in SciERC extraction outputs.\\\\n\\\\nViolation types (mutually exclusive per triple):\\\\n1. entity_type_violations      - entity type not in ontology's valid type list\\\\n2. relation_vocabulary_violations - relation name not in ontology (solvable by grammar-constrained decoding)\\\\n3. domain_range_violations     - relation name valid but (head_type, tail_type) violates constraints (OntoCoDec core target)\\\\n4. cross_field_consistency_violations - same entity mention has inconsistent types across relations\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport argparse\\\\nimport json\\\\nfrom collections import defaultdict\\\\nfrom pathlib import Path\\\\n\\\\n\\\\ndef normalize_type(t, valid_types, type_map=None):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Case-insensitive type matching with common aliases.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    if type_map is None:\\\\n        type_map = {\\\\n            \\\\\\\"otherscientificterm\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n            \\\\\\\"other-scientificterm\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n            \\\\\\\"other_scientific_term\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n            \\\\\\\"scientificterm\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n            \\\\\\\"other\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n        }\\\\n    t_lower = t.strip().lower().replace(\\\\\\\" \\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"_\\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"-\\\\\\\", \\\\\\\"\\\\\\\")\\\\n    for vt in valid_types:\\\\n        if t_lower == vt.lower().replace(\\\\\\\" \\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"_\\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"-\\\\\\\", \\\\\\\"\\\\\\\"):\\\\n            return vt\\\\n    if t_lower in type_map:\\\\n        return type_map[t_lower]\\\\n    return None\\\\n\\\\n\\\\ndef normalize_relation(rel_name, valid_relation_types):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Fuzzy-match a model-output relation name to the nearest ontology relation.\\\\n\\\\n    Match conditions (any one suffices):\\\\n    1. Exact match (case-insensitive, ignoring spaces/hyphens/underscores)\\\\n    2. Token overlap > 80%\\\\n    3. Levenshtein distance <= 2\\\\n\\\\n    Returns: (matched_name, is_fuzzy_match) or (None, False)\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    rel_norm = rel_name.strip().lower().replace(\\\\\\\" \\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"_\\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"-\\\\\\\", \\\\\\\"\\\\\\\")\\\\n    for vrt in valid_relation_types:\\\\n        if rel_norm == vrt.lower().replace(\\\\\\\" \\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"_\\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"-\\\\\\\", \\\\\\\"\\\\\\\"):\\\\n            return vrt, False\\\\n\\\\n    rel_tokens = set(rel_name.strip().lower().replace(\\\\\\\"-\\\\\\\", \\\\\\\" \\\\\\\").replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\").split())\\\\n    for vrt in valid_relation_types:\\\\n        vrt_tokens = set(vrt.lower().replace(\\\\\\\"-\\\\\\\", \\\\\\\" \\\\\\\").replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\").split())\\\\n        if rel_tokens and vrt_tokens:\\\\n            overlap = len(rel_tokens & vrt_tokens)\\\\n            union = len(rel_tokens | vrt_tokens)\\\\n            if overlap / union > 0.8:\\\\n                return vrt, True\\\\n\\\\n    for vrt in valid_relation_types:\\\\n        if _levenshtein(rel_name.strip().lower(), vrt.lower()) <= 2:\\\\n            return vrt, True\\\\n\\\\n    return None, False\\\\n\\\\n\\\\ndef _levenshtein(s1, s2):\\\\n    if len(s1) < len(s2):\\\\n        return _levenshtein(s2, s1)\\\\n    if len(s2) == 0:\\\\n        return len(s1)\\\\n    prev_row = range(len(s2) + 1)\\\\n    for i, c1 in enumerate(s1):\\\\n        curr_row = [i + 1]\\\\n        for j, c2 in enumerate(s2):\\\\n            insertions = prev_row[j + 1] + 1\\\\n            deletions = curr_row[j] + 1\\\\n            substitutions = prev_row[j] + (c1 != c2)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"# WARNING: This checker is for SciERC only.\\n# For DocRED evaluation, use violation_checker_docred.py instead.\\n# Using this checker on DocRED outputs will produce false RV=100%\\n# because it iterates P-codes as relation names, not natural language labels.\\n\\\"\\\"\\\"Check ontology constraint violations in SciERC extraction outputs.\\n\\nViolation types (mutually exclusive per triple):\\n1. entity_type_violations      - entity type not in ontology's valid type list\\n2. relation_vocabulary_violations - relation name not in ontology (solvable by grammar-constrained decoding)\\n3. domain_range_violations     - relation name valid but (head_type, tail_type) violates constraints (OntoCoDec core target)\\n4. cross_field_consistency_violations - same entity mention has inconsistent types across relations\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\n\\ndef normalize_type(t, valid_types, type_map=None):\\n    \\\"\\\"\\\"Case-insensitive type matching with common aliases.\\\"\\\"\\\"\\n    if type_map is None:\\n        type_map = {\\n            \\\"otherscientificterm\\\": \\\"OtherScientificTerm\\\",\\n            \\\"other-scientificterm\\\": \\\"OtherScientificTerm\\\",\\n            \\\"other_scientific_term\\\": \\\"OtherScientificTerm\\\",\\n            \\\"scientificterm\\\": \\\"OtherScientificTerm\\\",\\n            \\\"other\\\": \\\"OtherScientificTerm\\\",\\n        }\\n    t_lower = t.strip().lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\")\\n    for vt in valid_types:\\n        if t_lower == vt.lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\"):\\n            return vt\\n    if t_lower in type_map:\\n        return type_map[t_lower]\\n    return None\\n\\n\\ndef normalize_relation(rel_name, valid_relation_types):\\n    \\\"\\\"\\\"Fuzzy-match a model-output relation name to the nearest ontology relation.\\n\\n    Match conditions (any one suffices):\\n    1. Exact match (case-insensitive, ignoring spaces/hyphens/underscores)\\n    2. Token overlap > 80%\\n    3. Levenshtein distance <= 2\\n\\n    Returns: (matched_name, is_fuzzy_match) or (None, False)\\n    \\\"\\\"\\\"\\n    rel_norm = rel_name.strip().lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\")\\n    for vrt in valid_relation_types:\\n        if rel_norm == vrt.lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\"):\\n            return vrt, False\\n\\n    rel_tokens = set(rel_name.strip().lower().replace(\\\"-\\\", \\\" \\\").replace(\\\"_\\\", \\\" \\\").split())\\n    for vrt in valid_relation_types:\\n        vrt_tokens = set(vrt.lower().replace(\\\"-\\\", \\\" \\\").replace(\\\"_\\\", \\\" \\\").split())\\n        if rel_tokens and vrt_tokens:\\n            overlap = len(rel_tokens & vrt_tokens)\\n            union = len(rel_tokens | vrt_tokens)\\n            if overlap / union > 0.8:\\n                return vrt, True\\n\\n    for vrt in valid_relation_types:\\n        if _levenshtein(rel_name.strip().lower(), vrt.lower()) <= 2:\\n            return vrt, True\\n\\n    return None, False\\n\\n\\ndef _levenshtein(s1, s2):\\n    if len(s1) < len(s2):\\n        return _levenshtein(s2, s1)\\n    if len(s2) == 0:\\n        return len(s1)\\n    prev_row = range(len(s2) + 1)\\n    for i, c1 in enumerate(s1):\\n        curr_row = [i + 1]\\n        for j, c2 in enumerate(s2):\\n            insertions = prev_row[j + 1] + 1\\n            deletions = curr_row[j] + 1\\n            substitutions = prev_row[j] + (c1 != c2)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_014UYKnJRLomQYn1hDLRDBcb`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "fields": [
    "exp_id",
    "metrics",
    "status"
  ],
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "af998ee0-6ecc-4b1d-b328-204801ce0cb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbkiktHu4wuEyMcDDThFyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1636,
      "cache_read_input_tokens": 26041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1636
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

_source line 23 · 2026-05-23T11:40:47.427Z_

<details><summary>↩ Tool result · `toolu_014UYKnJRLomQYn1hDLRDBcb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"sf2_70b_prompt_sensitivity\": {\"status\": \"DONE\", \"metrics\": {\"minimal_con\": {\"E_F1\": 37.22, \"R_F1\": 11.35, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.62}, \"minimal_unc\": {\"E_F1\": 37.51, \"R_F1\": 13.42, \"ET_pct\": 0.27, \"RV_pct\": 5.88, \"DR_pct\": 0.22, \"CF_pct\": 0}, \"detailed_con\": {\"E_F1\": 40.35, \"R_F1\": 11.16, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.75}, \"detailed_unc\": {\"E_F1\": 40.42, \"R_F1\": 11.12, \"ET_pct\": 0, \"RV_pct\": 0.26, \"DR_pct\": 4.57, \"CF_pct\": 0}}}, \"eval_70b_lora_docred_200_full_s2\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 36.45, \"R_P\": 31.25, \"R_R\": 43.72, \"E_F1\": 84.96, \"E_P\": 84.6, \"E_R\": 85.34, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 13, \"CF_pct\": 0.34, \"parse_fail_pct\": 0, \"pred_entities\": 3819, \"pred_relations\": 3546, \"entity_tp\": 3218, \"entity_fp\": 586, \"entity_fn\": 553, \"relation_tp\": 1104, \"relation_fp\": 2429, \"relation_fn\": 1421}}, \"sf2_qwen_int4_docred_s1\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 200, \"parse_failures\": 37, \"parse_fail_pct\": 18.5, \"total_entities_pred\": 2985, \"total_relations_pred\": 2385, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.1, \"E_P\": 84.87, \"E_R\": 66.93, \"E_F1\": 74.84, \"R_P\": 41.59, \"R_R\": 38.65, \"R_F1\": 40.07, \"et_violations\": 0, \"rv_violations\": 0, \"dr_violations\": 0, \"cf_violations\": 3}}, \"sf2_llama_int4_docred_s1\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.22, \"R-F1\": 48.04, \"E-F1\": 84.18, \"R-P\": 44.79, \"R-R\": 51.8, \"E-P\": 85.5, \"E-R\": 82.9, \"samples\": 200, \"parse_fail\": 5, \"parse_fail_pct\": 2.5, \"entities_pred\": 3669, \"relations_pred\": 2997}}, \"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"metrics\": {\"GoLLIE_ZS\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.83, \"E_F1\": 9.17, \"R_F1\": 0, \"pred_ents\": 241, \"pred_rels\": 5, \"docs_with_output\": 54}, \"OntoCoDec_Qwen_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.61, \"E_F1\": 66.43, \"R_F1\": 43.69}, \"OntoCoDec_Llama_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.62, \"E_F1\": 67.09, \"R_F1\": 45.47}}}, \"eval_70b_zs_docred_200_full_s1\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 5.34, \"E-F1\": 70.05, \"R-F1\": 13.25, \"PF%\": 0, \"entities_pred\": 3234, \"relations_pred\": 2637, \"triples_checked\": 2642}}, \"eval_70b_lora_docred_200_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 10.5, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.38, \"CF_pct\": 0.06, \"E_F1\": 80.13, \"E_P\": 85.16, \"E_R\": 75.66, \"R_F1\": 43.96, \"R_P\": 39.78, \"R_R\": 49.11, \"entities_pred\": 3362, \"relations_pred\": 3154}}, \"eval_70b_lora_docred_200_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 11, \"ET_pct\": 0, \"RV_pct\": 0.51, \"DR_pct\": 0, \"CF_pct\": 0.21, \"E_F1\": 80.06, \"E_P\": 85.21, \"E_R\": 75.5, \"R_F1\": 43.61, \"R_P\": 39.44, \"R_R\": 48.75, \"entities_pred\": 3351, \"relations_pred\": 3148}}, \"eval_70b_zs_docred_200_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities_pred\": 3242, \"relations_pred\": 2637, \"ET_pct\": 0, \"RV_pct\": 7.88, \"DR_pct\": 13.45, \"CF_count\": 0, \"fuzzy_matches\": 8, \"E_F1\": 70.14, \"E_P\": 75.85, \"E_R\": 65.23, \"R_F1\": 13.25, \"R_P\": 12.97, \"R_R\": 13.54}}, \"eval_70b_zs_docred_200_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_failures\": 1, \"entities_pred\": 3221, \"relations_pred\": 2609, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 17.03, \"CF_count\": 0, \"fuzzy_matches\": 0, \"E_F1\": 70.12, \"E_P\": 75.88, \"E_R\": 65.17, \"R_F1\": 13.23, \"R_P\": 12.99, \"R_R\": 13.47}}, \"eval_70b_zs_docred_200_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities\": 3240, \"relations\": 2596, \"ET_pct\": 0.12, \"RV_pct\": 8.24, \"DR_pct\": 1.66, \"CF_count\": 132, \"CF_pct\": 4.07, \"E_F1\": 70.1, \"E_P\": 75.87, \"E_R\": 65.15, \"R_F1\": 13.05, \"R_P\": 12.88, \"R_R\": 13.23, \"fuzzy_matches\": 8}}, \"eval_70b_lora_docred_200_beam4_s1\": {\"status\": \"DONE\", \"metrics\": {\"E-F1\": 85.57, \"E-P\": 85.45, \"E-R\": 85.68, \"R-F1\": 48.14, \"R-P\": 44.24, \"R-R\": 52.79, \"ET%\": 0, \"RV%\": 0, \"DR%\": 0, \"CF%\": 0, \"parse_fail\": \"1/200 (0.5%)\", \"entities_pred\": 3790, \"relations_pred\": 3030}}, \"eval_70b_lora_scierc_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"json_failure_rate\": 0, \"entities\": 1805, \"relations\": 1133, \"entity_type_violations\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violations\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violations\": 17, \"domain_range_violation_rate\": 0.015, \"cross_field_consistency_violations\": 0, \"fuzzy_relation_matches\": 0, \"entity_P\": 0.6272, \"entity_R\": 0.6707, \"entity_F1\": 0.6482, \"relation_P\": 0.4152, \"relation_R\": 0.4825, \"relation_F1\": 0.4463}}, \"eval_70b_zs_scierc_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 2353, \"relations\": 1483, \"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.4, \"CF_count\": 0, \"E_F1\": 35.22, \"E_P\": 30.13, \"E_R\": 42.38, \"R_F1\": 11.23, \"R_P\": 9.31, \"R_R\": 14.17, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_full_s2\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1531, \"relations\": 1027, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 18, \"E_F1\": 62.35, \"E_P\": 65.44, \"E_R\": 59.53, \"R_F1\": 36.28, \"R_P\": 35.35, \"R_R\": 37.27, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1806, \"relations\": 1133, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 9, \"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"parse_fail_pct\": 0}}, \"entity_order_ablation_qwen_scierc\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 67.05, \"E_P\": 65.23, \"E_R\": 68.98, \"R_F1\": 43.77, \"R_P\": 40.78, \"R_R\": 47.23, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 21, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1784, \"relations\": 1128, \"corrected_original_R_F1\": 43.77, \"corrected_original_E_F1\": 67.05, \"corrected_original_DR_pct\": 0, \"corrected_original_CF_count\": 21, \"corrected_delta_R_F1\": 0, \"corrected_delta_E_F1\": 0, \"raw_output_identical\": true, \"parsed_output_identical\": true, \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"}}, \"eval_70b_zs_scierc_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 11.37, \"DR_pct\": 1.01, \"RV_pct\": 0.6, \"ET_pct\": 0, \"CF_count\": 76, \"samples\": 551}}, \"eval_70b_zs_scierc_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 11.23, \"DR_pct\": 6.33, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 0, \"samples\": 551}}, \"eval_70b_lora_scierc_beam4_s1\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 64.89, \"E_P\": 62.29, \"E_R\": 67.72, \"R_F1\": 44.81, \"R_P\": 39.45, \"R_R\": 51.85, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 1, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1839, \"relations\": 1283}}, \"tcr_beam4_llama_scierc\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1803, \"relations\": 1194, \"entity_type_violations\": \"0/1803 (0.0%)\", \"relation_vocab_violations\": \"0/1194 (0.0%)\", \"domain_range_violations\": \"13/1194 (1.1%)\", \"cross_field_consistency\": 0, \"DR_pct\": 1.09, \"E_F1\": 68.02, \"E_P\": 65.88, \"E_R\": 70.29, \"R_F1\": 46.05, \"R_P\": 41.83, \"R_R\": 51.23, \"tcr_changed_selection\": \"0/551 (0.0%)\"}}, \"tcr_beam4_qwen_scierc\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1802, \"relations\": 1250, \"entity_type_violations\": \"0/1802 (0.0%)\", \"relation_vocab_violations\": \"0/1250 (0.0%)\", \"domain_range_violations\": \"23/1250 (1.8%)\", \"cross_field_consistency_violations\": 1, \"DR_pct\": 1.84, \"E_P\": 65.05, \"E_R\": 69.64, \"E_F1\": 67.26, \"R_P\": 39.36, \"R_R\": 50.51, \"R_F1\": 44.24, \"TCR_changed_selection\": \"0/551 (0.0%)\", \"all_candidates_TCR_1.0\": true}}, \"vllm_guided_json_scierc_zs\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 15.26, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.04, \"R-F1\": 8.75, \"E-F1\": 30.91, \"parse_fail%\": 0, \"total_samples\": 551, \"total_entities\": 2485, \"total_relations\": 1724, \"inference_time_s\": 108.5}}, \"eval_70b_lora_docred_200_s1_constrained\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 79.38, \"E_P\": 85.24, \"E_R\": 74.28, \"R_F1\": 43.95, \"R_P\": 40.48, \"R_R\": 48.08, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.18, \"parse_fail_pct\": 12.5, \"samples\": 200}}, \"d066_beam_sweep\": {\"status\": \"DONE\", \"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"}}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"}}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"}}}, \"count\": 30, \"total\": 164, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4922}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "e22ea932-f590-40b5-aacc-72059e1e7f2b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"sf2_70b_prompt_sensitivity\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"minimal_con\\\": {\\\"E_F1\\\": 37.22, \\\"R_F1\\\": 11.35, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.62}, \\\"minimal_unc\\\": {\\\"E_F1\\\": 37.51, \\\"R_F1\\\": 13.42, \\\"ET_pct\\\": 0.27, \\\"RV_pct\\\": 5.88, \\\"DR_pct\\\": 0.22, \\\"CF_pct\\\": 0}, \\\"detailed_con\\\": {\\\"E_F1\\\": 40.35, \\\"R_F1\\\": 11.16, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.75}, \\\"detailed_unc\\\": {\\\"E_F1\\\": 40.42, \\\"R_F1\\\": 11.12, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.26, \\\"DR_pct\\\": 4.57, \\\"CF_pct\\\": 0}}}, \\\"eval_70b_lora_docred_200_full_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"R_F1\\\": 36.45, \\\"R_P\\\": 31.25, \\\"R_R\\\": 43.72, \\\"E_F1\\\": 84.96, \\\"E_P\\\": 84.6, \\\"E_R\\\": 85.34, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 13, \\\"CF_pct\\\": 0.34, \\\"parse_fail_pct\\\": 0, \\\"pred_entities\\\": 3819, \\\"pred_relations\\\": 3546, \\\"entity_tp\\\": 3218, \\\"entity_fp\\\": 586, \\\"entity_fn\\\": 553, \\\"relation_tp\\\": 1104, \\\"relation_fp\\\": 2429, \\\"relation_fn\\\": 1421}}, \\\"sf2_qwen_int4_docred_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_samples\\\": 200, \\\"parse_failures\\\": 37, \\\"parse_fail_pct\\\": 18.5, \\\"total_entities_pred\\\": 2985, \\\"total_relations_pred\\\": 2385, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.1, \\\"E_P\\\": 84.87, \\\"E_R\\\": 66.93, \\\"E_F1\\\": 74.84, \\\"R_P\\\": 41.59, \\\"R_R\\\": 38.65, \\\"R_F1\\\": 40.07, \\\"et_violations\\\": 0, \\\"rv_violations\\\": 0, \\\"dr_violations\\\": 0, \\\"cf_violations\\\": 3}}, \\\"sf2_llama_int4_docred_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.22, \\\"R-F1\\\": 48.04, \\\"E-F1\\\": 84.18, \\\"R-P\\\": 44.79, \\\"R-R\\\": 51.8, \\\"E-P\\\": 85.5, \\\"E-R\\\": 82.9, \\\"samples\\\": 200, \\\"parse_fail\\\": 5, \\\"parse_fail_pct\\\": 2.5, \\\"entities_pred\\\": 3669, \\\"relations_pred\\\": 2997}}, \\\"sf2_llama_int4_scierc_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.94, \\\"R-F1\\\": 43.98, \\\"E-F1\\\": 67.54, \\\"samples\\\": 551, \\\"R-P\\\": 40.47, \\\"R-R\\\": 48.15, \\\"E-P\\\": 65.51, \\\"E-R\\\": 69.7}}, \\\"sf2_qwen_int4_scierc_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 1.1, \\\"R-F1\\\": 41.71, \\\"E-F1\\\": 67.05, \\\"samples\\\": 551, \\\"R-P\\\": 38.52, \\\"R-R\\\": 45.48, \\\"E-P\\\": 64.76, \\\"E-R\\\": 69.52}}, \\\"sf2_gollie_scierc_violation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"GoLLIE_ZS\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.83, \\\"E_F1\\\": 9.17, \\\"R_F1\\\": 0, \\\"pred_ents\\\": 241, \\\"pred_rels\\\": 5, \\\"docs_with_output\\\": 54}, \\\"OntoCoDec_Qwen_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.61, \\\"E_F1\\\": 66.43, \\\"R_F1\\\": 43.69}, \\\"OntoCoDec_Llama_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.62, \\\"E_F1\\\": 67.09, \\\"R_F1\\\": 45.47}}}, \\\"eval_70b_zs_docred_200_full_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 5.34, \\\"E-F1\\\": 70.05, \\\"R-F1\\\": 13.25, \\\"PF%\\\": 0, \\\"entities_pred\\\": 3234, \\\"relations_pred\\\": 2637, \\\"triples_checked\\\": 2642}}, \\\"eval_70b_lora_docred_200_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 10.5, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.38, \\\"CF_pct\\\": 0.06, \\\"E_F1\\\": 80.13, \\\"E_P\\\": 85.16, \\\"E_R\\\": 75.66, \\\"R_F1\\\": 43.96, \\\"R_P\\\": 39.78, \\\"R_R\\\": 49.11, \\\"entities_pred\\\": 3362, \\\"relations_pred\\\": 3154}}, \\\"eval_70b_lora_docred_200_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 11, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.51, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.21, \\\"E_F1\\\": 80.06, \\\"E_P\\\": 85.21, \\\"E_R\\\": 75.5, \\\"R_F1\\\": 43.61, \\\"R_P\\\": 39.44, \\\"R_R\\\": 48.75, \\\"entities_pred\\\": 3351, \\\"relations_pred\\\": 3148}}, \\\"eval_70b_zs_docred_200_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities_pred\\\": 3242, \\\"relations_pred\\\": 2637, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 7.88, \\\"DR_pct\\\": 13.45, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 8, \\\"E_F1\\\": 70.14, \\\"E_P\\\": 75.85, \\\"E_R\\\": 65.23, \\\"R_F1\\\": 13.25, \\\"R_P\\\": 12.97, \\\"R_R\\\": 13.54}}, \\\"eval_70b_zs_docred_200_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 1, \\\"entities_pred\\\": 3221, \\\"relations_pred\\\": 2609, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 17.03, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"E_F1\\\": 70.12, \\\"E_P\\\": 75.88, \\\"E_R\\\": 65.17, \\\"R_F1\\\": 13.23, \\\"R_P\\\": 12.99, \\\"R_R\\\": 13.47}}, \\\"eval_70b_zs_docred_200_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities\\\": 3240, \\\"relations\\\": 2596, \\\"ET_pct\\\": 0.12, \\\"RV_pct\\\": 8.24, \\\"DR_pct\\\": 1.66, \\\"CF_count\\\": 132, \\\"CF_pct\\\": 4.07, \\\"E_F1\\\": 70.1, \\\"E_P\\\": 75.87, \\\"E_R\\\": 65.15, \\\"R_F1\\\": 13.05, \\\"R_P\\\": 12.88, \\\"R_R\\\": 13.23, \\\"fuzzy_matches\\\": 8}}, \\\"eval_70b_lora_docred_200_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"E-F1\\\": 85.57, \\\"E-P\\\": 85.45, \\\"E-R\\\": 85.68, \\\"R-F1\\\": 48.14, \\\"R-P\\\": 44.24, \\\"R-R\\\": 52.79, \\\"ET%\\\": 0, \\\"RV%\\\": 0, \\\"DR%\\\": 0, \\\"CF%\\\": 0, \\\"parse_fail\\\": \\\"1/200 (0.5%)\\\", \\\"entities_pred\\\": 3790, \\\"relations_pred\\\": 3030}}, \\\"eval_70b_lora_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"json_failure_rate\\\": 0, \\\"entities\\\": 1805, \\\"relations\\\": 1133, \\\"entity_type_violations\\\": 0, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocab_violations\\\": 0, \\\"relation_vocab_violation_rate\\\": 0, \\\"domain_range_violations\\\": 17, \\\"domain_range_violation_rate\\\": 0.015, \\\"cross_field_consistency_violations\\\": 0, \\\"fuzzy_relation_matches\\\": 0, \\\"entity_P\\\": 0.6272, \\\"entity_R\\\": 0.6707, \\\"entity_F1\\\": 0.6482, \\\"relation_P\\\": 0.4152, \\\"relation_R\\\": 0.4825, \\\"relation_F1\\\": 0.4463}}, \\\"eval_70b_zs_scierc_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 2353, \\\"relations\\\": 1483, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.6, \\\"DR_pct\\\": 6.4, \\\"CF_count\\\": 0, \\\"E_F1\\\": 35.22, \\\"E_P\\\": 30.13, \\\"E_R\\\": 42.38, \\\"R_F1\\\": 11.23, \\\"R_P\\\": 9.31, \\\"R_R\\\": 14.17, \\\"parse_fail_pct\\\": 0}}, \\\"eval_70b_lora_scierc_full_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1531, \\\"relations\\\": 1027, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 18, \\\"E_F1\\\": 62.35, \\\"E_P\\\": 65.44, \\\"E_R\\\": 59.53, \\\"R_F1\\\": 36.28, \\\"R_P\\\": 35.35, \\\"R_R\\\": 37.27, \\\"parse_fail_pct\\\": 0}}, \\\"eval_70b_lora_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1806, \\\"relations\\\": 1133, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.6, \\\"CF_count\\\": 9, \\\"E_F1\\\": 64.86, \\\"E_P\\\": 62.74, \\\"E_R\\\": 67.12, \\\"R_F1\\\": 44.73, \\\"R_P\\\": 41.61, \\\"R_R\\\": 48.36, \\\"parse_fail_pct\\\": 0}}, \\\"entity_order_ablation_qwen_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"E_F1\\\": 67.05, \\\"E_P\\\": 65.23, \\\"E_R\\\": 68.98, \\\"R_F1\\\": 43.77, \\\"R_P\\\": 40.78, \\\"R_R\\\": 47.23, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 21, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1784, \\\"relations\\\": 1128, \\\"corrected_original_R_F1\\\": 43.77, \\\"corrected_original_E_F1\\\": 67.05, \\\"corrected_original_DR_pct\\\": 0, \\\"corrected_original_CF_count\\\": 21, \\\"corrected_delta_R_F1\\\": 0, \\\"corrected_delta_E_F1\\\": 0, \\\"raw_output_identical\\\": true, \\\"parsed_output_identical\\\": true, \\\"note\\\": \\\"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\\\"}}, \\\"eval_70b_zs_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"R_F1\\\": 11.37, \\\"DR_pct\\\": 1.01, \\\"RV_pct\\\": 0.6, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 76, \\\"samples\\\": 551}}, \\\"eval_70b_zs_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"R_F1\\\": 11.23, \\\"DR_pct\\\": 6.33, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 0, \\\"samples\\\": 551}}, \\\"eval_70b_lora_scierc_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"E_F1\\\": 64.89, \\\"E_P\\\": 62.29, \\\"E_R\\\": 67.72, \\\"R_F1\\\": 44.81, \\\"R_P\\\": 39.45, \\\"R_R\\\": 51.85, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 1, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1839, \\\"relations\\\": 1283}}, \\\"tcr_beam4_llama_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1803, \\\"relations\\\": 1194, \\\"entity_type_violations\\\": \\\"0/1803 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1194 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"13/1194 (1.1%)\\\", \\\"cross_field_consistency\\\": 0, \\\"DR_pct\\\": 1.09, \\\"E_F1\\\": 68.02, \\\"E_P\\\": 65.88, \\\"E_R\\\": 70.29, \\\"R_F1\\\": 46.05, \\\"R_P\\\": 41.83, \\\"R_R\\\": 51.23, \\\"tcr_changed_selection\\\": \\\"0/551 (0.0%)\\\"}}, \\\"tcr_beam4_qwen_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1802, \\\"relations\\\": 1250, \\\"entity_type_violations\\\": \\\"0/1802 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1250 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"23/1250 (1.8%)\\\", \\\"cross_field_consistency_violations\\\": 1, \\\"DR_pct\\\": 1.84, \\\"E_P\\\": 65.05, \\\"E_R\\\": 69.64, \\\"E_F1\\\": 67.26, \\\"R_P\\\": 39.36, \\\"R_R\\\": 50.51, \\\"R_F1\\\": 44.24, \\\"TCR_changed_selection\\\": \\\"0/551 (0.0%)\\\", \\\"all_candidates_TCR_1.0\\\": true}}, \\\"vllm_guided_json_scierc_zs\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"DR%\\\": 15.26, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.04, \\\"R-F1\\\": 8.75, \\\"E-F1\\\": 30.91, \\\"parse_fail%\\\": 0, \\\"total_samples\\\": 551, \\\"total_entities\\\": 2485, \\\"total_relations\\\": 1724, \\\"inference_time_s\\\": 108.5}}, \\\"eval_70b_lora_docred_200_s1_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"E_F1\\\": 79.38, \\\"E_P\\\": 85.24, \\\"E_R\\\": 74.28, \\\"R_F1\\\": 43.95, \\\"R_P\\\": 40.48, \\\"R_R\\\": 48.08, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.18, \\\"parse_fail_pct\\\": 12.5, \\\"samples\\\": 200}}, \\\"d066_beam_sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"scierc_qwen3_8b\\\": {\\\"k1_unc\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 2.11, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.494}, \\\"k1_con\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.5, \\\"avg_time\\\": 2.932}, \\\"k2_unc\\\": {\\\"E_F1\\\": 67.79, \\\"R_F1\\\": 44.75, \\\"DR_pct\\\": 1.54, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.954}, \\\"k2_con\\\": {\\\"E_F1\\\": 67.71, \\\"R_F1\\\": 44.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.11, \\\"avg_time\\\": 3.463}, \\\"k4_unc\\\": {\\\"E_F1\\\": 67.49, \\\"R_F1\\\": 43.72, \\\"DR_pct\\\": 1.89, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 3.485}, \\\"k4_con\\\": {\\\"E_F1\\\": 67.22, \\\"R_F1\\\": 43.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.069}, \\\"k8_unc\\\": {\\\"E_F1\\\": 66.4, \\\"R_F1\\\": 43.17, \\\"DR_pct\\\": 1.77, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.194}, \\\"k8_con\\\": {\\\"E_F1\\\": 66.36, \\\"R_F1\\\": 43.65, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 5.058}}, \\\"pareto_optimal\\\": \\\"k=2 con\\\", \\\"best_E_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 67.79}, \\\"best_R_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 44.75}}}, \\\"w8_llama_docred_ft_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"R_F1\\\": 43.72, \\\"R_P\\\": 38.57, \\\"R_R\\\": 50.44, \\\"parse_fail_pct\\\": 2.3, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\\\"}}, \\\"w8_llama_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"R_F1\\\": 43.85, \\\"R_P\\\": 38.85, \\\"R_R\\\": 50.31, \\\"parse_fail_pct\\\": 2.4, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\\\"}}, \\\"w8_qwen_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"R_F1\\\": 40.85, \\\"R_P\\\": 36.33, \\\"R_R\\\": 46.65, \\\"parse_fail_pct\\\": 7.52, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\\\"}}}, \\\"count\\\": 30, \\\"total\\\": 164, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4922}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"sf2_70b_prompt_sensitivity\": {\"status\": \"DONE\", \"metrics\": {\"minimal_con\": {\"E_F1\": 37.22, \"R_F1\": 11.35, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.62}, \"minimal_unc\": {\"E_F1\": 37.51, \"R_F1\": 13.42, \"ET_pct\": 0.27, \"RV_pct\": 5.88, \"DR_pct\": 0.22, \"CF_pct\": 0}, \"detailed_con\": {\"E_F1\": 40.35, \"R_F1\": 11.16, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.75}, \"detailed_unc\": {\"E_F1\": 40.42, \"R_F1\": 11.12, \"ET_pct\": 0, \"RV_pct\": 0.26, \"DR_pct\": 4.57, \"CF_pct\": 0}}}, \"eval_70b_lora_docred_200_full_s2\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 36.45, \"R_P\": 31.25, \"R_R\": 43.72, \"E_F1\": 84.96, \"E_P\": 84.6, \"E_R\": 85.34, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 13, \"CF_pct\": 0.34, \"parse_fail_pct\": 0, \"pred_entities\": 3819, \"pred_relations\": 3546, \"entity_tp\": 3218, \"entity_fp\": 586, \"entity_fn\": 553, \"relation_tp\": 1104, \"relation_fp\": 2429, \"relation_fn\": 1421}}, \"sf2_qwen_int4_docred_s1\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 200, \"parse_failures\": 37, \"parse_fail_pct\": 18.5, \"total_entities_pred\": 2985, \"total_relations_pred\": 2385, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.1, \"E_P\": 84.87, \"E_R\": 66.93, \"E_F1\": 74.84, \"R_P\": 41.59, \"R_R\": 38.65, \"R_F1\": 40.07, \"et_violations\": 0, \"rv_violations\": 0, \"dr_violations\": 0, \"cf_violations\": 3}}, \"sf2_llama_int4_docred_s1\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.22, \"R-F1\": 48.04, \"E-F1\": 84.18, \"R-P\": 44.79, \"R-R\": 51.8, \"E-P\": 85.5, \"E-R\": 82.9, \"samples\": 200, \"parse_fail\": 5, \"parse_fail_pct\": 2.5, \"entities_pred\": 3669, \"relations_pred\": 2997}}, \"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"metrics\": {\"GoLLIE_ZS\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.83, \"E_F1\": 9.17, \"R_F1\": 0, \"pred_ents\": 241, \"pred_rels\": 5, \"docs_with_output\": 54}, \"OntoCoDec_Qwen_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.61, \"E_F1\": 66.43, \"R_F1\": 43.69}, \"OntoCoDec_Llama_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.62, \"E_F1\": 67.09, \"R_F1\": 45.47}}}, \"eval_70b_zs_docred_200_full_s1\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 5.34, \"E-F1\": 70.05, \"R-F1\": 13.25, \"PF%\": 0, \"entities_pred\": 3234, \"relations_pred\": 2637, \"triples_checked\": 2642}}, \"eval_70b_lora_docred_200_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 10.5, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.38, \"CF_pct\": 0.06, \"E_F1\": 80.13, \"E_P\": 85.16, \"E_R\": 75.66, \"R_F1\": 43.96, \"R_P\": 39.78, \"R_R\": 49.11, \"entities_pred\": 3362, \"relations_pred\": 3154}}, \"eval_70b_lora_docred_200_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 11, \"ET_pct\": 0, \"RV_pct\": 0.51, \"DR_pct\": 0, \"CF_pct\": 0.21, \"E_F1\": 80.06, \"E_P\": 85.21, \"E_R\": 75.5, \"R_F1\": 43.61, \"R_P\": 39.44, \"R_R\": 48.75, \"entities_pred\": 3351, \"relations_pred\": 3148}}, \"eval_70b_zs_docred_200_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities_pred\": 3242, \"relations_pred\": 2637, \"ET_pct\": 0, \"RV_pct\": 7.88, \"DR_pct\": 13.45, \"CF_count\": 0, \"fuzzy_matches\": 8, \"E_F1\": 70.14, \"E_P\": 75.85, \"E_R\": 65.23, \"R_F1\": 13.25, \"R_P\": 12.97, \"R_R\": 13.54}}, \"eval_70b_zs_docred_200_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_failures\": 1, \"entities_pred\": 3221, \"relations_pred\": 2609, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 17.03, \"CF_count\": 0, \"fuzzy_matches\": 0, \"E_F1\": 70.12, \"E_P\": 75.88, \"E_R\": 65.17, \"R_F1\": 13.23, \"R_P\": 12.99, \"R_R\": 13.47}}, \"eval_70b_zs_docred_200_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities\": 3240, \"relations\": 2596, \"ET_pct\": 0.12, \"RV_pct\": 8.24, \"DR_pct\": 1.66, \"CF_count\": 132, \"CF_pct\": 4.07, \"E_F1\": 70.1, \"E_P\": 75.87, \"E_R\": 65.15, \"R_F1\": 13.05, \"R_P\": 12.88, \"R_R\": 13.23, \"fuzzy_matches\": 8}}, \"eval_70b_lora_docred_200_beam4_s1\": {\"status\": \"DONE\", \"metrics\": {\"E-F1\": 85.57, \"E-P\": 85.45, \"E-R\": 85.68, \"R-F1\": 48.14, \"R-P\": 44.24, \"R-R\": 52.79, \"ET%\": 0, \"RV%\": 0, \"DR%\": 0, \"CF%\": 0, \"parse_fail\": \"1/200 (0.5%)\", \"entities_pred\": 3790, \"relations_pred\": 3030}}, \"eval_70b_lora_scierc_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"json_failure_rate\": 0, \"entities\": 1805, \"relations\": 1133, \"entity_type_violations\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violations\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violations\": 17, \"domain_range_violation_rate\": 0.015, \"cross_field_consistency_violations\": 0, \"fuzzy_relation_matches\": 0, \"entity_P\": 0.6272, \"entity_R\": 0.6707, \"entity_F1\": 0.6482, \"relation_P\": 0.4152, \"relation_R\": 0.4825, \"relation_F1\": 0.4463}}, \"eval_70b_zs_scierc_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 2353, \"relations\": 1483, \"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.4, \"CF_count\": 0, \"E_F1\": 35.22, \"E_P\": 30.13, \"E_R\": 42.38, \"R_F1\": 11.23, \"R_P\": 9.31, \"R_R\": 14.17, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_full_s2\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1531, \"relations\": 1027, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 18, \"E_F1\": 62.35, \"E_P\": 65.44, \"E_R\": 59.53, \"R_F1\": 36.28, \"R_P\": 35.35, \"R_R\": 37.27, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1806, \"relations\": 1133, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 9, \"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"parse_fail_pct\": 0}}, \"entity_order_ablation_qwen_scierc\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 67.05, \"E_P\": 65.23, \"E_R\": 68.98, \"R_F1\": 43.77, \"R_P\": 40.78, \"R_R\": 47.23, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 21, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1784, \"relations\": 1128, \"corrected_original_R_F1\": 43.77, \"corrected_original_E_F1\": 67.05, \"corrected_original_DR_pct\": 0, \"corrected_original_CF_count\": 21, \"corrected_delta_R_F1\": 0, \"corrected_delta_E_F1\": 0, \"raw_output_identical\": true, \"parsed_output_identical\": true, \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"}}, \"eval_70b_zs_scierc_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 11.37, \"DR_pct\": 1.01, \"RV_pct\": 0.6, \"ET_pct\": 0, \"CF_count\": 76, \"samples\": 551}}, \"eval_70b_zs_scierc_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 11.23, \"DR_pct\": 6.33, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 0, \"samples\": 551}}, \"eval_70b_lora_scierc_beam4_s1\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 64.89, \"E_P\": 62.29, \"E_R\": 67.72, \"R_F1\": 44.81, \"R_P\": 39.45, \"R_R\": 51.85, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 1, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1839, \"relations\": 1283}}, \"tcr_beam4_llama_scierc\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1803, \"relations\": 1194, \"entity_type_violations\": \"0/1803 (0.0%)\", \"relation_vocab_violations\": \"0/1194 (0.0%)\", \"domain_range_violations\": \"13/1194 (1.1%)\", \"cross_field_consistency\": 0, \"DR_pct\": 1.09, \"E_F1\": 68.02, \"E_P\": 65.88, \"E_R\": 70.29, \"R_F1\": 46.05, \"R_P\": 41.83, \"R_R\": 51.23, \"tcr_changed_selection\": \"0/551 (0.0%)\"}}, \"tcr_beam4_qwen_scierc\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1802, \"relations\": 1250, \"entity_type_violations\": \"0/1802 (0.0%)\", \"relation_vocab_violations\": \"0/1250 (0.0%)\", \"domain_range_violations\": \"23/1250 (1.8%)\", \"cross_field_consistency_violations\": 1, \"DR_pct\": 1.84, \"E_P\": 65.05, \"E_R\": 69.64, \"E_F1\": 67.26, \"R_P\": 39.36, \"R_R\": 50.51, \"R_F1\": 44.24, \"TCR_changed_selection\": \"0/551 (0.0%)\", \"all_candidates_TCR_1.0\": true}}, \"vllm_guided_json_scierc_zs\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 15.26, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.04, \"R-F1\": 8.75, \"E-F1\": 30.91, \"parse_fail%\": 0, \"total_samples\": 551, \"total_entities\": 2485, \"total_relations\": 1724, \"inference_time_s\": 108.5}}, \"eval_70b_lora_docred_200_s1_constrained\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 79.38, \"E_P\": 85.24, \"E_R\": 74.28, \"R_F1\": 43.95, \"R_P\": 40.48, \"R_R\": 48.08, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.18, \"parse_fail_pct\": 12.5, \"samples\": 200}}, \"d066_beam_sweep\": {\"status\": \"DONE\", \"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"}}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"}}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"}}}, \"count\": 30, \"total\": 164, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4922}}"
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
I found the 3 experiments in the registry. Let me check their metrics:

1. **w8_qwen_docred_ft_semantic_only**: metrics have R_F1=40.85, but NO DR_pct field
2. **w8_llama_docred_ft_semantic_only**: metrics have R_F1=43.85, but NO DR_pct field
3. **w8_llama_docred_ft_grammar_only**: metrics have R_F1=43.72, but NO DR_pct field

So indeed, DR_pct is missing from all 3 experiments' registry entries, which confirms the problem.


Now I need to locate the DocRED-specific violation checker and look through the posthoc report files to see if DR values are already being calculated there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "49b08230-9fd4-4b52-9e57-41ad2cf6d74c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3u8ubxb9CtcKRwav1MFyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8378,
      "cache_read_input_tokens": 27677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8378
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

Registry 确认：3 个实验都没有 DR_pct 字段。violation_checker.py 头部说 SciERC 专用，DocRED 需要 `violation_checker_docred.py`。查找它。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "29e12efc-f4c9-449e-a11c-2f9f4334bdb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3u8ubxb9CtcKRwav1MFyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8378,
      "cache_read_input_tokens": 27677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8378
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014xsMtavfmiFvUc3PvjiUGy`</summary>

```json
{
  "server": "westd-16980",
  "command": "ls -la /root/schema_semantic_constrained_ie/violation_checker_docred.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "2663556f-2101-44b1-8974-d8e1853fcecb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3u8ubxb9CtcKRwav1MFyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8378,
      "cache_read_input_tokens": 27677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8378
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

_source line 27 · 2026-05-23T11:40:58.599Z_

<details><summary>↩ Tool result · `toolu_014xsMtavfmiFvUc3PvjiUGy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 15235 May 15 02:25 /root/schema_semantic_constrained_ie/violation_checker_docred.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "3fce4eca-7780-43f0-aa15-8549ed25c9a5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 15235 May 15 02:25 /root/schema_semantic_constrained_ie/violation_checker_docred.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 15235 May 15 02:25 /root/schema_semantic_constrained_ie/violation_checker_docred.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AMtKtPDQnHmUFe6yDJg5Zg`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_report_qwen_docred.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "44ceee9a-d6e9-40ef-b9a8-925312c9a627",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3u8ubxb9CtcKRwav1MFyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8378,
      "cache_read_input_tokens": 27677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8378
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

_source line 29 · 2026-05-23T11:40:59.550Z_

<details><summary>↩ Tool result · `toolu_01AMtKtPDQnHmUFe6yDJg5Zg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"docred\\\",\\n  \\\"total_samples\\\": 998,\\n  \\\"total_triples_before\\\": 15869,\\n  \\\"triples_kept\\\": 15705,\\n  \\\"triples_removed\\\": {\\n    \\\"relation_vocabulary\\\": 43,\\n    \\\"entity_type\\\": 0,\\n    \\\"domain_range\\\": 121,\\n    \\\"total\\\": 164\\n  },\\n  \\\"rejection_rate\\\": 0.0103,\\n  \\\"entity_f1\\\": {\\n    \\\"precision\\\": 0.8548,\\n    \\\"recall\\\": 0.792,\\n    \\\"f1\\\": 0.8222,\\n    \\\"tp\\\": 15422,\\n    \\\"gold\\\": 19471,\\n    \\\"pred\\\": 18041\\n  },\\n  \\\"relation_f1_before\\\": {\\n    \\\"precision\\\": 0.3643,\\n    \\\"recall\\\": 0.4663,\\n    \\\"f1\\\": 0.4091,\\n    \\\"tp\\\": 5666,\\n    \\\"gold\\\": 12151,\\n    \\\"pred\\\": 15552\\n  },\\n  \\\"relation_f1_after\\\": {\\n    \\\"precision\\\": 0.3676,\\n    \\\"recall\\\": 0.4662,\\n    \\\"f1\\\": 0.4111,\\n    \\\"tp\\\": 5665,\\n    \\\"gold\\\": 12151,\\n    \\\"pred\\\": 15410\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "3660af9b-cc74-49ab-ac38-948439e537c2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"dataset\\\\\\\": \\\\\\\"docred\\\\\\\",\\\\n  \\\\\\\"total_samples\\\\\\\": 998,\\\\n  \\\\\\\"total_triples_before\\\\\\\": 15869,\\\\n  \\\\\\\"triples_kept\\\\\\\": 15705,\\\\n  \\\\\\\"triples_removed\\\\\\\": {\\\\n    \\\\\\\"relation_vocabulary\\\\\\\": 43,\\\\n    \\\\\\\"entity_type\\\\\\\": 0,\\\\n    \\\\\\\"domain_range\\\\\\\": 121,\\\\n    \\\\\\\"total\\\\\\\": 164\\\\n  },\\\\n  \\\\\\\"rejection_rate\\\\\\\": 0.0103,\\\\n  \\\\\\\"entity_f1\\\\\\\": {\\\\n    \\\\\\\"precision\\\\\\\": 0.8548,\\\\n    \\\\\\\"recall\\\\\\\": 0.792,\\\\n    \\\\\\\"f1\\\\\\\": 0.8222,\\\\n    \\\\\\\"tp\\\\\\\": 15422,\\\\n    \\\\\\\"gold\\\\\\\": 19471,\\\\n    \\\\\\\"pred\\\\\\\": 18041\\\\n  },\\\\n  \\\\\\\"relation_f1_before\\\\\\\": {\\\\n    \\\\\\\"precision\\\\\\\": 0.3643,\\\\n    \\\\\\\"recall\\\\\\\": 0.4663,\\\\n    \\\\\\\"f1\\\\\\\": 0.4091,\\\\n    \\\\\\\"tp\\\\\\\": 5666,\\\\n    \\\\\\\"gold\\\\\\\": 12151,\\\\n    \\\\\\\"pred\\\\\\\": 15552\\\\n  },\\\\n  \\\\\\\"relation_f1_after\\\\\\\": {\\\\n    \\\\\\\"precision\\\\\\\": 0.3676,\\\\n    \\\\\\\"recall\\\\\\\": 0.4662,\\\\n    \\\\\\\"f1\\\\\\\": 0.4111,\\\\n    \\\\\\\"tp\\\\\\\": 5665,\\\\n    \\\\\\\"gold\\\\\\\": 12151,\\\\n    \\\\\\\"pred\\\\\\\": 15410\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"docred\\\",\\n  \\\"total_samples\\\": 998,\\n  \\\"total_triples_before\\\": 15869,\\n  \\\"triples_kept\\\": 15705,\\n  \\\"triples_removed\\\": {\\n    \\\"relation_vocabulary\\\": 43,\\n    \\\"entity_type\\\": 0,\\n    \\\"domain_range\\\": 121,\\n    \\\"total\\\": 164\\n  },\\n  \\\"rejection_rate\\\": 0.0103,\\n  \\\"entity_f1\\\": {\\n    \\\"precision\\\": 0.8548,\\n    \\\"recall\\\": 0.792,\\n    \\\"f1\\\": 0.8222,\\n    \\\"tp\\\": 15422,\\n    \\\"gold\\\": 19471,\\n    \\\"pred\\\": 18041\\n  },\\n  \\\"relation_f1_before\\\": {\\n    \\\"precision\\\": 0.3643,\\n    \\\"recall\\\": 0.4663,\\n    \\\"f1\\\": 0.4091,\\n    \\\"tp\\\": 5666,\\n    \\\"gold\\\": 12151,\\n    \\\"pred\\\": 15552\\n  },\\n  \\\"relation_f1_after\\\": {\\n    \\\"precision\\\": 0.3676,\\n    \\\"recall\\\": 0.4662,\\n    \\\"f1\\\": 0.4111,\\n    \\\"tp\\\": 5665,\\n    \\\"gold\\\": 12151,\\n    \\\"pred\\\": 15410\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KWQhpULKtnRPDC95GZn7oj`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/outputs/w8_ft_posthoc_report_llama_docred.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "7bed8f37-cf09-4d62-97f6-5876cf103659",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3u8ubxb9CtcKRwav1MFyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8378,
      "cache_read_input_tokens": 27677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8378
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

_source line 31 · 2026-05-23T11:41:00.374Z_

<details><summary>↩ Tool result · `toolu_01KWQhpULKtnRPDC95GZn7oj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"docred\\\",\\n  \\\"total_samples\\\": 998,\\n  \\\"total_triples_before\\\": 16171,\\n  \\\"triples_kept\\\": 16067,\\n  \\\"triples_removed\\\": {\\n    \\\"relation_vocabulary\\\": 24,\\n    \\\"entity_type\\\": 0,\\n    \\\"domain_range\\\": 80,\\n    \\\"total\\\": 104\\n  },\\n  \\\"rejection_rate\\\": 0.0064,\\n  \\\"entity_f1\\\": {\\n    \\\"precision\\\": 0.8498,\\n    \\\"recall\\\": 0.8306,\\n    \\\"f1\\\": 0.8401,\\n    \\\"tp\\\": 16173,\\n    \\\"gold\\\": 19471,\\n    \\\"pred\\\": 19032\\n  },\\n  \\\"relation_f1_before\\\": {\\n    \\\"precision\\\": 0.3862,\\n    \\\"recall\\\": 0.505,\\n    \\\"f1\\\": 0.4377,\\n    \\\"tp\\\": 6136,\\n    \\\"gold\\\": 12151,\\n    \\\"pred\\\": 15887\\n  },\\n  \\\"relation_f1_after\\\": {\\n    \\\"precision\\\": 0.3886,\\n    \\\"recall\\\": 0.5049,\\n    \\\"f1\\\": 0.4392,\\n    \\\"tp\\\": 6135,\\n    \\\"gold\\\": 12151,\\n    \\\"pred\\\": 15786\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "c864471a-a3a7-422a-a3a4-aa0616be530b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"dataset\\\\\\\": \\\\\\\"docred\\\\\\\",\\\\n  \\\\\\\"total_samples\\\\\\\": 998,\\\\n  \\\\\\\"total_triples_before\\\\\\\": 16171,\\\\n  \\\\\\\"triples_kept\\\\\\\": 16067,\\\\n  \\\\\\\"triples_removed\\\\\\\": {\\\\n    \\\\\\\"relation_vocabulary\\\\\\\": 24,\\\\n    \\\\\\\"entity_type\\\\\\\": 0,\\\\n    \\\\\\\"domain_range\\\\\\\": 80,\\\\n    \\\\\\\"total\\\\\\\": 104\\\\n  },\\\\n  \\\\\\\"rejection_rate\\\\\\\": 0.0064,\\\\n  \\\\\\\"entity_f1\\\\\\\": {\\\\n    \\\\\\\"precision\\\\\\\": 0.8498,\\\\n    \\\\\\\"recall\\\\\\\": 0.8306,\\\\n    \\\\\\\"f1\\\\\\\": 0.8401,\\\\n    \\\\\\\"tp\\\\\\\": 16173,\\\\n    \\\\\\\"gold\\\\\\\": 19471,\\\\n    \\\\\\\"pred\\\\\\\": 19032\\\\n  },\\\\n  \\\\\\\"relation_f1_before\\\\\\\": {\\\\n    \\\\\\\"precision\\\\\\\": 0.3862,\\\\n    \\\\\\\"recall\\\\\\\": 0.505,\\\\n    \\\\\\\"f1\\\\\\\": 0.4377,\\\\n    \\\\\\\"tp\\\\\\\": 6136,\\\\n    \\\\\\\"gold\\\\\\\": 12151,\\\\n    \\\\\\\"pred\\\\\\\": 15887\\\\n  },\\\\n  \\\\\\\"relation_f1_after\\\\\\\": {\\\\n    \\\\\\\"precision\\\\\\\": 0.3886,\\\\n    \\\\\\\"recall\\\\\\\": 0.5049,\\\\n    \\\\\\\"f1\\\\\\\": 0.4392,\\\\n    \\\\\\\"tp\\\\\\\": 6135,\\\\n    \\\\\\\"gold\\\\\\\": 12151,\\\\n    \\\\\\\"pred\\\\\\\": 15786\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"docred\\\",\\n  \\\"total_samples\\\": 998,\\n  \\\"total_triples_before\\\": 16171,\\n  \\\"triples_kept\\\": 16067,\\n  \\\"triples_removed\\\": {\\n    \\\"relation_vocabulary\\\": 24,\\n    \\\"entity_type\\\": 0,\\n    \\\"domain_range\\\": 80,\\n    \\\"total\\\": 104\\n  },\\n  \\\"rejection_rate\\\": 0.0064,\\n  \\\"entity_f1\\\": {\\n    \\\"precision\\\": 0.8498,\\n    \\\"recall\\\": 0.8306,\\n    \\\"f1\\\": 0.8401,\\n    \\\"tp\\\": 16173,\\n    \\\"gold\\\": 19471,\\n    \\\"pred\\\": 19032\\n  },\\n  \\\"relation_f1_before\\\": {\\n    \\\"precision\\\": 0.3862,\\n    \\\"recall\\\": 0.505,\\n    \\\"f1\\\": 0.4377,\\n    \\\"tp\\\": 6136,\\n    \\\"gold\\\": 12151,\\n    \\\"pred\\\": 15887\\n  },\\n  \\\"relation_f1_after\\\": {\\n    \\\"precision\\\": 0.3886,\\n    \\\"recall\\\": 0.5049,\\n    \\\"f1\\\": 0.4392,\\n    \\\"tp\\\": 6135,\\n    \\\"gold\\\": 12151,\\n    \\\"pred\\\": 15786\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
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
OK, the posthoc report files are for the "full" constrained experiments (w8_ft_posthoc_qwen_docred and w8_ft_posthoc_llama_docred), not the ablation experiments. These show the results of running posthoc filtering.

But I need DR violations for the 3 ablation experiments:
- w8_qwen_docred_ft_semantic_only
- w8_llama_docred_ft_semantic_only
- w8_llama_docred_ft_grammar_only

I need to use violation_checker_docred.py to compute DR. 

Let me look at how violation_checker_docred.py works to understand what inputs it needs and how to run it for these ablation experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "a51b4065-8a29-449e-a8af-09adeb700e27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tJTEa7CG1VVQX9xB7Wqe5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1938,
      "cache_read_input_tokens": 36055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1938
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

_source line 33_

posthoc 报告是 full constrained 版本的，不是 ablation 的。需要用 violation_checker_docred.py 对 3 个 ablation 输出重算 DR。先看用法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "eeb28356-8d72-48f8-857a-e655c5483caf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tJTEa7CG1VVQX9xB7Wqe5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1938,
      "cache_read_input_tokens": 36055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1938
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

_source line 34_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018bawPefQqBadWRSozVdCLW`</summary>

```json
{
  "server": "westd-16980",
  "command": "head -60 /root/schema_semantic_constrained_ie/violation_checker_docred.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "875040f6-ee1e-4d42-8bd2-c1b5de880767",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tJTEa7CG1VVQX9xB7Wqe5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1938,
      "cache_read_input_tokens": 36055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1938
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

_source line 35 · 2026-05-23T11:41:09.068Z_

<details><summary>↩ Tool result · `toolu_018bawPefQqBadWRSozVdCLW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Check ontology constraint violations in DocRED extraction outputs.\\n\\nViolation types (mutually exclusive per triple):\\n1. entity_type_violations      - entity type not in {PER, ORG, LOC, TIME, NUM, MISC}\\n2. relation_vocabulary_violations - relation name not in ontology (solvable by grammar-constrained decoding)\\n3. domain_range_violations     - relation name valid but (head_type, tail_type) violates constraints (OntoCoDec core target)\\n4. cross_field_consistency_violations - same entity mention has inconsistent types across relations\\n\\\"\\\"\\\"\\n\\nimport json\\nimport argparse\\nfrom collections import defaultdict, Counter\\nfrom pathlib import Path\\n\\n\\nVALID_ENTITY_TYPES = {\\\"PER\\\", \\\"ORG\\\", \\\"LOC\\\", \\\"TIME\\\", \\\"NUM\\\", \\\"MISC\\\"}\\n\\n\\n# DocRED uses abbreviated types; models sometimes generate full forms\\nENTITY_TYPE_ALIASES = {\\n    'PERSON': 'PER',\\n    'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG',\\n    'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC',\\n    'NUMBER': 'NUM',\\n    'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\n\\ndef normalize_entity_type(raw_type):\\n    \\\"\\\"\\\"Strip whitespace, uppercase, and apply alias mapping.\\\"\\\"\\\"\\n    t = raw_type.strip().upper()\\n    return ENTITY_TYPE_ALIASES.get(t, t)\\n\\n\\n\\ndef _levenshtein(s1, s2):\\n    if len(s1) < len(s2):\\n        return _levenshtein(s2, s1)\\n    if len(s2) == 0:\\n        return len(s1)\\n    prev_row = range(len(s2) + 1)\\n    for i, c1 in enumerate(s1):\\n        curr_row = [i + 1]\\n        for j, c2 in enumerate(s2):\\n            insertions = prev_row[j + 1] + 1\\n            deletions = curr_row[j] + 1\\n            substitutions = prev_row[j] + (c1 != c2)\\n            curr_row.append(min(insertions, deletions, substitutions))\\n        prev_row = curr_row\\n    return prev_row[-1]\\n\\n\\ndef load_constraints(path: str) -> dict:\\n    with open(path) as f:\\n        return json.load(f)\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "3d93d3c9-f433-4608-8fa9-514adfe2d3dc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"Check ontology constraint violations in DocRED extraction outputs.\\\\n\\\\nViolation types (mutually exclusive per triple):\\\\n1. entity_type_violations      - entity type not in {PER, ORG, LOC, TIME, NUM, MISC}\\\\n2. relation_vocabulary_violations - relation name not in ontology (solvable by grammar-constrained decoding)\\\\n3. domain_range_violations     - relation name valid but (head_type, tail_type) violates constraints (OntoCoDec core target)\\\\n4. cross_field_consistency_violations - same entity mention has inconsistent types across relations\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport json\\\\nimport argparse\\\\nfrom collections import defaultdict, Counter\\\\nfrom pathlib import Path\\\\n\\\\n\\\\nVALID_ENTITY_TYPES = {\\\\\\\"PER\\\\\\\", \\\\\\\"ORG\\\\\\\", \\\\\\\"LOC\\\\\\\", \\\\\\\"TIME\\\\\\\", \\\\\\\"NUM\\\\\\\", \\\\\\\"MISC\\\\\\\"}\\\\n\\\\n\\\\n# DocRED uses abbreviated types; models sometimes generate full forms\\\\nENTITY_TYPE_ALIASES = {\\\\n    'PERSON': 'PER',\\\\n    'PEOPLE': 'PER',\\\\n    'ORGANIZATION': 'ORG',\\\\n    'ORGANISATION': 'ORG',\\\\n    'LOCATION': 'LOC',\\\\n    'NUMBER': 'NUM',\\\\n    'NUMERICAL': 'NUM',\\\\n    'MISCELLANEOUS': 'MISC',\\\\n}\\\\n\\\\n\\\\ndef normalize_entity_type(raw_type):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Strip whitespace, uppercase, and apply alias mapping.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    t = raw_type.strip().upper()\\\\n    return ENTITY_TYPE_ALIASES.get(t, t)\\\\n\\\\n\\\\n\\\\ndef _levenshtein(s1, s2):\\\\n    if len(s1) < len(s2):\\\\n        return _levenshtein(s2, s1)\\\\n    if len(s2) == 0:\\\\n        return len(s1)\\\\n    prev_row = range(len(s2) + 1)\\\\n    for i, c1 in enumerate(s1):\\\\n        curr_row = [i + 1]\\\\n        for j, c2 in enumerate(s2):\\\\n            insertions = prev_row[j + 1] + 1\\\\n            deletions = curr_row[j] + 1\\\\n            substitutions = prev_row[j] + (c1 != c2)\\\\n            curr_row.append(min(insertions, deletions, substitutions))\\\\n        prev_row = curr_row\\\\n    return prev_row[-1]\\\\n\\\\n\\\\ndef load_constraints(path: str) -> dict:\\\\n    with open(path) as f:\\\\n        return json.load(f)\\\\n\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Check ontology constraint violations in DocRED extraction outputs.\\n\\nViolation types (mutually exclusive per triple):\\n1. entity_type_violations      - entity type not in {PER, ORG, LOC, TIME, NUM, MISC}\\n2. relation_vocabulary_violations - relation name not in ontology (solvable by grammar-constrained decoding)\\n3. domain_range_violations     - relation name valid but (head_type, tail_type) violates constraints (OntoCoDec core target)\\n4. cross_field_consistency_violations - same entity mention has inconsistent types across relations\\n\\\"\\\"\\\"\\n\\nimport json\\nimport argparse\\nfrom collections import defaultdict, Counter\\nfrom pathlib import Path\\n\\n\\nVALID_ENTITY_TYPES = {\\\"PER\\\", \\\"ORG\\\", \\\"LOC\\\", \\\"TIME\\\", \\\"NUM\\\", \\\"MISC\\\"}\\n\\n\\n# DocRED uses abbreviated types; models sometimes generate full forms\\nENTITY_TYPE_ALIASES = {\\n    'PERSON': 'PER',\\n    'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG',\\n    'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC',\\n    'NUMBER': 'NUM',\\n    'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\n\\ndef normalize_entity_type(raw_type):\\n    \\\"\\\"\\\"Strip whitespace, uppercase, and apply alias mapping.\\\"\\\"\\\"\\n    t = raw_type.strip().upper()\\n    return ENTITY_TYPE_ALIASES.get(t, t)\\n\\n\\n\\ndef _levenshtein(s1, s2):\\n    if len(s1) < len(s2):\\n        return _levenshtein(s2, s1)\\n    if len(s2) == 0:\\n        return len(s1)\\n    prev_row = range(len(s2) + 1)\\n    for i, c1 in enumerate(s1):\\n        curr_row = [i + 1]\\n        for j, c2 in enumerate(s2):\\n            insertions = prev_row[j + 1] + 1\\n            deletions = curr_row[j] + 1\\n            substitutions = prev_row[j] + (c1 != c2)\\n            curr_row.append(min(insertions, deletions, substitutions))\\n        prev_row = curr_row\\n    return prev_row[-1]\\n\\n\\ndef load_constraints(path: str) -> dict:\\n    with open(path) as f:\\n        return json.load(f)\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Let me see the argparse section to understand the CLI interface.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "31aab3fa-cd77-4c87-98ab-98220e9aaa44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018b4dyZfUZCUWf9D7ofd4WB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 37993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
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

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E5W1y4C3xXz22FYab2ZimE`</summary>

```json
{
  "server": "westd-16980",
  "command": "tail -80 /root/schema_semantic_constrained_ie/violation_checker_docred.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "04db75f8-256a-4ef3-ba3f-ff9aa0c3539e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018b4dyZfUZCUWf9D7ofd4WB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 37993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
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

_source line 38 · 2026-05-23T11:41:19.930Z_

<details><summary>↩ Tool result · `toolu_01E5W1y4C3xXz22FYab2ZimE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    domain_range_examples = []\\n    cross_field_examples = []\\n    for d in doc_results:\\n        if d.get(\\\"status\\\") != \\\"checked\\\":\\n            continue\\n\\n    all_examples = {\\\"entity_type_violations\\\": [], \\\"relation_vocabulary_violations\\\": [],\\n                    \\\"domain_range_violations\\\": [], \\\"cross_field_consistency_violations\\\": []}\\n    for rec in records:\\n        parsed = rec.get(\\\"parsed_output\\\")\\n        if parsed is None:\\n            continue\\n        violations, _ = check_document(parsed, constraints, rel_types, name_to_id)\\n        doc_id = rec.get(\\\"doc_id\\\", \\\"unknown\\\")\\n        for v in violations[\\\"entity_type\\\"]:\\n            if len(all_examples[\\\"entity_type_violations\\\"]) < 3:\\n                all_examples[\\\"entity_type_violations\\\"].append({\\\"doc_id\\\": doc_id, **v})\\n        for v in violations[\\\"relation_vocabulary\\\"]:\\n            if len(all_examples[\\\"relation_vocabulary_violations\\\"]) < 3:\\n                all_examples[\\\"relation_vocabulary_violations\\\"].append({\\\"doc_id\\\": doc_id, **v})\\n        for v in violations[\\\"domain_range\\\"]:\\n            if len(all_examples[\\\"domain_range_violations\\\"]) < 3:\\n                all_examples[\\\"domain_range_violations\\\"].append({\\\"doc_id\\\": doc_id, **v})\\n        for v in violations[\\\"cross_field_consistency\\\"]:\\n            if len(all_examples[\\\"cross_field_consistency_violations\\\"]) < 3:\\n                all_examples[\\\"cross_field_consistency_violations\\\"].append({\\\"doc_id\\\": doc_id, **v})\\n\\n    report = {\\n        \\\"summary\\\": {\\n            \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\",\\n            \\\"total_documents\\\": n_docs,\\n            \\\"documents_checked\\\": docs_checked,\\n            \\\"parse_failures\\\": parse_failures,\\n            \\\"json_parse_rate\\\": round(docs_checked / n_docs, 4) if n_docs else 0,\\n            \\\"total_triples_extracted\\\": total_triples,\\n            \\\"total_entities_extracted\\\": total_entities,\\n\\n            \\\"entity_type_violations\\\": total_entity_type_violations,\\n            \\\"entity_type_violation_rate\\\": round(total_entity_type_violations / total_entities, 4) if total_entities else 0,\\n\\n            \\\"relation_vocabulary_violations\\\": total_relation_vocab_violations,\\n            \\\"relation_vocabulary_violation_rate\\\": round(total_relation_vocab_violations / total_triples, 4) if total_triples else 0,\\n            \\\"relation_fuzzy_matches\\\": total_fuzzy_matches,\\n\\n            \\\"domain_range_violations\\\": total_domain_range_violations,\\n            \\\"domain_range_violation_rate\\\": round(total_domain_range_violations / total_triples, 4) if total_triples else 0,\\n\\n            \\\"cross_field_consistency_violations\\\": total_cross_field_violations,\\n            \\\"cross_field_consistency_violation_rate\\\": round(total_cross_field_violations / total_entities, 4) if total_entities else 0,\\n\\n            \\\"total_violations_any\\\": total_violations,\\n            \\\"total_violation_rate\\\": round(total_violations / max(total_entities + total_triples, 1), 4),\\n\\n            \\\"go_nogo_metric\\\": round(total_domain_range_violations / total_triples, 4) if total_triples else 0,\\n            \\\"go_nogo_metric_description\\\": \\\"per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)\\\",\\n        },\\n        \\\"per_relation_type\\\": per_relation_breakdown,\\n        \\\"examples\\\": all_examples,\\n        \\\"per_document_details\\\": doc_results,\\n    }\\n\\n    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)\\n    with open(args.output_path, \\\"w\\\") as f:\\n        json.dump(report, f, indent=2, ensure_ascii=False)\\n\\n    s = report[\\\"summary\\\"]\\n    print(\\\"=== Violation Report (DocRED) ===\\\")\\n    print(f\\\"Documents: {docs_checked} checked, {parse_failures} parse failures\\\")\\n    print(f\\\"Entities: {total_entities}, Triples: {total_triples}\\\")\\n    print(f\\\"\\\\nEntity type violations: {total_entity_type_violations} ({100*s['entity_type_violation_rate']:.1f}%)\\\")\\n    print(f\\\"Relation vocab violations: {total_relation_vocab_violations}/{total_triples} ({100*s['relation_vocabulary_violation_rate']:.1f}%)\\\")\\n    print(f\\\"Domain/range violations: {total_domain_range_violations}/{total_triples} ({100*s['domain_range_violation_rate']:.1f}%)\\\")\\n    print(f\\\"Cross-field consistency violations: {total_cross_field_violations}\\\")\\n    print(f\\\"Fuzzy relation matches: {total_fuzzy_matches}\\\")\\n    print(f\\\"\\\\nGo/No-go metric (D/R violation rate): {s['go_nogo_metric']:.4f}\\\")\\n    print(f\\\"Output: {args.output_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "b3232b81-41cf-47ee-b3b3-daed0b49f0b1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    domain_range_examples = []\\\\n    cross_field_examples = []\\\\n    for d in doc_results:\\\\n        if d.get(\\\\\\\"status\\\\\\\") != \\\\\\\"checked\\\\\\\":\\\\n            continue\\\\n\\\\n    all_examples = {\\\\\\\"entity_type_violations\\\\\\\": [], \\\\\\\"relation_vocabulary_violations\\\\\\\": [],\\\\n                    \\\\\\\"domain_range_violations\\\\\\\": [], \\\\\\\"cross_field_consistency_violations\\\\\\\": []}\\\\n    for rec in records:\\\\n        parsed = rec.get(\\\\\\\"parsed_output\\\\\\\")\\\\n        if parsed is None:\\\\n            continue\\\\n        violations, _ = check_document(parsed, constraints, rel_types, name_to_id)\\\\n        doc_id = rec.get(\\\\\\\"doc_id\\\\\\\", \\\\\\\"unknown\\\\\\\")\\\\n        for v in violations[\\\\\\\"entity_type\\\\\\\"]:\\\\n            if len(all_examples[\\\\\\\"entity_type_violations\\\\\\\"]) < 3:\\\\n                all_examples[\\\\\\\"entity_type_violations\\\\\\\"].append({\\\\\\\"doc_id\\\\\\\": doc_id, **v})\\\\n        for v in violations[\\\\\\\"relation_vocabulary\\\\\\\"]:\\\\n            if len(all_examples[\\\\\\\"relation_vocabulary_violations\\\\\\\"]) < 3:\\\\n                all_examples[\\\\\\\"relation_vocabulary_violations\\\\\\\"].append({\\\\\\\"doc_id\\\\\\\": doc_id, **v})\\\\n        for v in violations[\\\\\\\"domain_range\\\\\\\"]:\\\\n            if len(all_examples[\\\\\\\"domain_range_violations\\\\\\\"]) < 3:\\\\n                all_examples[\\\\\\\"domain_range_violations\\\\\\\"].append({\\\\\\\"doc_id\\\\\\\": doc_id, **v})\\\\n        for v in violations[\\\\\\\"cross_field_consistency\\\\\\\"]:\\\\n            if len(all_examples[\\\\\\\"cross_field_consistency_violations\\\\\\\"]) < 3:\\\\n                all_examples[\\\\\\\"cross_field_consistency_violations\\\\\\\"].append({\\\\\\\"doc_id\\\\\\\": doc_id, **v})\\\\n\\\\n    report = {\\\\n        \\\\\\\"summary\\\\\\\": {\\\\n            \\\\\\\"checker_version\\\\\\\": \\\\\\\"fixed_20260514_v2 (strip + alias + unique_et)\\\\\\\",\\\\n            \\\\\\\"total_documents\\\\\\\": n_docs,\\\\n            \\\\\\\"documents_checked\\\\\\\": docs_checked,\\\\n            \\\\\\\"parse_failures\\\\\\\": parse_failures,\\\\n            \\\\\\\"json_parse_rate\\\\\\\": round(docs_checked / n_docs, 4) if n_docs else 0,\\\\n            \\\\\\\"total_triples_extracted\\\\\\\": total_triples,\\\\n            \\\\\\\"total_entities_extracted\\\\\\\": total_entities,\\\\n\\\\n            \\\\\\\"entity_type_violations\\\\\\\": total_entity_type_violations,\\\\n            \\\\\\\"entity_type_violation_rate\\\\\\\": round(total_entity_type_violations / total_entities, 4) if total_entities else 0,\\\\n\\\\n            \\\\\\\"relation_vocabulary_violations\\\\\\\": total_relation_vocab_violations,\\\\n            \\\\\\\"relation_vocabulary_violation_rate\\\\\\\": round(total_relation_vocab_violations / total_triples, 4) if total_triples else 0,\\\\n            \\\\\\\"relation_fuzzy_matches\\\\\\\": total_fuzzy_matches,\\\\n\\\\n            \\\\\\\"domain_range_violations\\\\\\\": total_domain_range_violations,\\\\n            \\\\\\\"domain_range_violation_rate\\\\\\\": round(total_domain_range_violations / total_triples, 4) if total_triples else 0,\\\\n\\\\n            \\\\\\\"cross_field_consistency_violations\\\\\\\": total_cross_field_violations,\\\\n            \\\\\\\"cross_field_consistency_violation_rate\\\\\\\": round(total_cross_field_violations / total_entities, 4) if total_entities else 0,\\\\n\\\\n            \\\\\\\"total_violations_any\\\\\\\": total_violations,\\\\n            \\\\\\\"total_violation_rate\\\\\\\": round(total_violations / max(total_entities + total_triples, 1), 4),\\\\n\\\\n            \\\\\\\"go_nogo_metric\\\\\\\": round(total_domain_range_violations / total_triples, 4) if total_triples else 0,\\\\n            \\\\\\\"go_nogo_metric_description\\\\\\\": \\\\\\\"per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)\\\\\\\",\\\\n        },\\\\n        \\\\\\\"per_relation_type\\\\\\\": per_relation_breakdown,\\\\n        \\\\\\\"examples\\\\\\\": all_examples,\\\\n        \\\\\\\"per_document_details\\\\\\\": doc_results,\\\\n    }\\\\n\\\\n    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)\\\\n    with open(args.output_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(report, f, indent=2, ensure_ascii=False)\\\\n\\\\n    s = report[\\\\\\\"summary\\\\\\\"]\\\\n    print(\\\\\\\"=== Violation Report (DocRED) ===\\\\\\\")\\\\n    print(f\\\\\\\"Documents: {docs_checked} checked, {parse_failures} parse failures\\\\\\\")\\\\n    print(f\\\\\\\"Entities: {total_entities}, Triples: {total_triples}\\\\\\\")\\\\n    print(f\\\\\\\"\\\\\\\\nEntity type violations: {total_entity_type_violations} ({100*s['entity_type_violation_rate']:.1f}%)\\\\\\\")\\\\n    print(f\\\\\\\"Relation vocab violations: {total_relation_vocab_violations}/{total_triples} ({100*s['relation_vocabulary_violation_rate']:.1f}%)\\\\\\\")\\\\n    print(f\\\\\\\"Domain/range violations: {total_domain_range_violations}/{total_triples} ({100*s['domain_range_violation_rate']:.1f}%)\\\\\\\")\\\\n    print(f\\\\\\\"Cross-field consistency violations: {total_cross_field_violations}\\\\\\\")\\\\n    print(f\\\\\\\"Fuzzy relation matches: {total_fuzzy_matches}\\\\\\\")\\\\n    print(f\\\\\\\"\\\\\\\\nGo/No-go metric (D/R violation rate): {s['go_nogo_metric']:.4f}\\\\\\\")\\\\n    print(f\\\\\\\"Output: {args.output_path}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    domain_range_examples = []\\n    cross_field_examples = []\\n    for d in doc_results:\\n        if d.get(\\\"status\\\") != \\\"checked\\\":\\n            continue\\n\\n    all_examples = {\\\"entity_type_violations\\\": [], \\\"relation_vocabulary_violations\\\": [],\\n                    \\\"domain_range_violations\\\": [], \\\"cross_field_consistency_violations\\\": []}\\n    for rec in records:\\n        parsed = rec.get(\\\"parsed_output\\\")\\n        if parsed is None:\\n            continue\\n        violations, _ = check_document(parsed, constraints, rel_types, name_to_id)\\n        doc_id = rec.get(\\\"doc_id\\\", \\\"unknown\\\")\\n        for v in violations[\\\"entity_type\\\"]:\\n            if len(all_examples[\\\"entity_type_violations\\\"]) < 3:\\n                all_examples[\\\"entity_type_violations\\\"].append({\\\"doc_id\\\": doc_id, **v})\\n        for v in violations[\\\"relation_vocabulary\\\"]:\\n            if len(all_examples[\\\"relation_vocabulary_violations\\\"]) < 3:\\n                all_examples[\\\"relation_vocabulary_violations\\\"].append({\\\"doc_id\\\": doc_id, **v})\\n        for v in violations[\\\"domain_range\\\"]:\\n            if len(all_examples[\\\"domain_range_violations\\\"]) < 3:\\n                all_examples[\\\"domain_range_violations\\\"].append({\\\"doc_id\\\": doc_id, **v})\\n        for v in violations[\\\"cross_field_consistency\\\"]:\\n            if len(all_examples[\\\"cross_field_consistency_violations\\\"]) < 3:\\n                all_examples[\\\"cross_field_consistency_violations\\\"].append({\\\"doc_id\\\": doc_id, **v})\\n\\n    report = {\\n        \\\"summary\\\": {\\n            \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\",\\n            \\\"total_documents\\\": n_docs,\\n            \\\"documents_checked\\\": docs_checked,\\n            \\\"parse_failures\\\": parse_failures,\\n            \\\"json_parse_rate\\\": round(docs_checked / n_docs, 4) if n_docs else 0,\\n            \\\"total_triples_extracted\\\": total_triples,\\n            \\\"total_entities_extracted\\\": total_entities,\\n\\n            \\\"entity_type_violations\\\": total_entity_type_violations,\\n            \\\"entity_type_violation_rate\\\": round(total_entity_type_violations / total_entities, 4) if total_entities else 0,\\n\\n            \\\"relation_vocabulary_violations\\\": total_relation_vocab_violations,\\n            \\\"relation_vocabulary_violation_rate\\\": round(total_relation_vocab_violations / total_triples, 4) if total_triples else 0,\\n            \\\"relation_fuzzy_matches\\\": total_fuzzy_matches,\\n\\n            \\\"domain_range_violations\\\": total_domain_range_violations,\\n            \\\"domain_range_violation_rate\\\": round(total_domain_range_violations / total_triples, 4) if total_triples else 0,\\n\\n            \\\"cross_field_consistency_violations\\\": total_cross_field_violations,\\n            \\\"cross_field_consistency_violation_rate\\\": round(total_cross_field_violations / total_entities, 4) if total_entities else 0,\\n\\n            \\\"total_violations_any\\\": total_violations,\\n            \\\"total_violation_rate\\\": round(total_violations / max(total_entities + total_triples, 1), 4),\\n\\n            \\\"go_nogo_metric\\\": round(total_domain_range_violations / total_triples, 4) if total_triples else 0,\\n            \\\"go_nogo_metric_description\\\": \\\"per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)\\\",\\n        },\\n        \\\"per_relation_type\\\": per_relation_breakdown,\\n        \\\"examples\\\": all_examples,\\n        \\\"per_document_details\\\": doc_results,\\n    }\\n\\n    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)\\n    with open(args.output_path, \\\"w\\\") as f:\\n        json.dump(report, f, indent=2, ensure_ascii=False)\\n\\n    s = report[\\\"summary\\\"]\\n    print(\\\"=== Violation Report (DocRED) ===\\\")\\n    print(f\\\"Documents: {docs_checked} checked, {parse_failures} parse failures\\\")\\n    print(f\\\"Entities: {total_entities}, Triples: {total_triples}\\\")\\n    print(f\\\"\\\\nEntity type violations: {total_entity_type_violations} ({100*s['entity_type_violation_rate']:.1f}%)\\\")\\n    print(f\\\"Relation vocab violations: {total_relation_vocab_violations}/{total_triples} ({100*s['relation_vocabulary_violation_rate']:.1f}%)\\\")\\n    print(f\\\"Domain/range violations: {total_domain_range_violations}/{total_triples} ({100*s['domain_range_violation_rate']:.1f}%)\\\")\\n    print(f\\\"Cross-field consistency violations: {total_cross_field_violations}\\\")\\n    print(f\\\"Fuzzy relation matches: {total_fuzzy_matches}\\\")\\n    print(f\\\"\\\\nGo/No-go metric (D/R violation rate): {s['go_nogo_metric']:.4f}\\\")\\n    print(f\\\"Output: {args.output_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Unc6KagLL6CuwFiPNw5qTm`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"argparse\\|add_argument\\|def main\" /root/schema_semantic_constrained_ie/violation_checker_docred.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "62bf40ad-424d-4b68-baab-f212bc9b598e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGYGt2xPHWCiK7wWNkZfeS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1813,
      "cache_read_input_tokens": 39132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1813
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 40 · 2026-05-23T11:41:23.543Z_

<details><summary>↩ Tool result · `toolu_01Unc6KagLL6CuwFiPNw5qTm`</summary>

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
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "d38b6a9e-d43a-4fe7-8108-e15f1b88de6a",
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

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BeRAy5hVqNZJdCEzSkcgae`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"add_argument\" /root/schema_semantic_constrained_ie/violation_checker_docred.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "bfb710e9-fe28-4b57-a6b0-539a7d7922b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEvSSDK7WBfD2jqocmCGXd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 213,
      "cache_read_input_tokens": 40945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 213
      },
      "output_tokens": 67,
      "service_tier": "standard",
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

_source line 42 · 2026-05-23T11:41:25.953Z_

<details><summary>↩ Tool result · `toolu_01BeRAy5hVqNZJdCEzSkcgae`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"205:    parser.add_argument(\\\"--input_path\\\", type=str, default=\\\"outputs/raw_outputs_docred.jsonl\\\")\\n206:    parser.add_argument(\\\"--constraints_path\\\", type=str, default=\\\"data/docred/ontology_constraints_docred.json\\\")\\n207:    parser.add_argument(\\\"--output_path\\\", type=str, default=\\\"outputs/violation_report_docred.json\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "d5fb15bd-ffc9-43a6-816d-4ae3871ed1d5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"205:    parser.add_argument(\\\\\\\"--input_path\\\\\\\", type=str, default=\\\\\\\"outputs/raw_outputs_docred.jsonl\\\\\\\")\\\\n206:    parser.add_argument(\\\\\\\"--constraints_path\\\\\\\", type=str, default=\\\\\\\"data/docred/ontology_constraints_docred.json\\\\\\\")\\\\n207:    parser.add_argument(\\\\\\\"--output_path\\\\\\\", type=str, default=\\\\\\\"outputs/violation_report_docred.json\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"205:    parser.add_argument(\\\"--input_path\\\", type=str, default=\\\"outputs/raw_outputs_docred.jsonl\\\")\\n206:    parser.add_argument(\\\"--constraints_path\\\", type=str, default=\\\"data/docred/ontology_constraints_docred.json\\\")\\n207:    parser.add_argument(\\\"--output_path\\\", type=str, default=\\\"outputs/violation_report_docred.json\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Now I know the CLI interface:
- `--input_path`: path to the JSONL output file
- `--constraints_path`: path to ontology constraints (default: data/docred/ontology_constraints_docred.json)
- `--output_path`: where to write the violation report

I need to run this for the 3 files. Since the script writes an output file, I should use ssh_execute but write to /tmp to avoid modifying project files. Or better yet, let me check if I can just run it and capture stdout since it prints the summary.

Actually, it writes to output_path AND prints a summary. 

I'll execute all 3 evaluations in parallel using ssh_execute, directing the output files to /tmp.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "3adcd4ea-0904-43b4-9280-bb6815ba9c07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUXC8kQ1mtN5VTrfKYtv8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 41158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 44_

参数明确：`--input_path`, `--constraints_path`, `--output_path`。对 3 个文件运行评估，输出到 /tmp。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "97037039-bb0c-443f-8350-7b2153f6dd8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUXC8kQ1mtN5VTrfKYtv8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 41158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01ETHwmQCRr4V7P6BfwQpqiR`</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_qwen_docred_ft_semantic_only.jsonl --output_path /tmp/vr_qwen_semantic.json 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "95697719-56c4-4305-a40b-a6269a458677",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUXC8kQ1mtN5VTrfKYtv8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 41158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 46 · 2026-05-23T11:41:37.217Z_

<details><summary>↩ Tool result · `toolu_01ETHwmQCRr4V7P6BfwQpqiR`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_qwen_docred_ft_semantic_only.jsonl --output_path /tmp/vr_qwen_semantic.json 2>&1'\\n\\nExit code: 127\\n\\nStdout:\\n\\nbash: line 1: python: command not found\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "4f65f09e-7641-4812-80ce-2a7bdfe2881c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_qwen_docred_ft_semantic_only.jsonl --output_path /tmp/vr_qwen_semantic.json 2>&1'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\nbash: line 1: python: command not found\\\\n\\\\nStderr:\\\\n\\\\n\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_qwen_docred_ft_semantic_only.jsonl --output_path /tmp/vr_qwen_semantic.json 2>&1'\\n\\nExit code: 127\\n\\nStdout:\\n\\nbash: line 1: python: command not found\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01EnU8ktfP5ZVhGMjQFubeCi`</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_llama_docred_ft_semantic_only.jsonl --output_path /tmp/vr_llama_semantic.json 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "ee7bede1-4cd0-45b0-be37-f2549cff9d51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUXC8kQ1mtN5VTrfKYtv8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 41158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_016yqw4CbSxpPxRiQaSgydu1`</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_llama_docred_ft_grammar_only.jsonl --output_path /tmp/vr_llama_grammar.json 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "a25e099d-8f2d-4a5d-986a-197222a23b25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUXC8kQ1mtN5VTrfKYtv8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 41158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 49 · 2026-05-23T11:41:38.899Z_

<details><summary>↩ Tool result · `toolu_01EnU8ktfP5ZVhGMjQFubeCi`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_llama_docred_ft_semantic_only.jsonl --output_path /tmp/vr_llama_semantic.json 2>&1'\\n\\nExit code: 127\\n\\nStdout:\\n\\nbash: line 1: python: command not found\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.27}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "52d1bc4c-a128-4af3-a79e-3041ee04d3fb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_llama_docred_ft_semantic_only.jsonl --output_path /tmp/vr_llama_semantic.json 2>&1'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\nbash: line 1: python: command not found\\\\n\\\\nStderr:\\\\n\\\\n\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.27}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_llama_docred_ft_semantic_only.jsonl --output_path /tmp/vr_llama_semantic.json 2>&1'\\n\\nExit code: 127\\n\\nStdout:\\n\\nbash: line 1: python: command not found\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.27}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T11:41:39.909Z_

<details><summary>↩ Tool result · `toolu_016yqw4CbSxpPxRiQaSgydu1`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_llama_docred_ft_grammar_only.jsonl --output_path /tmp/vr_llama_grammar.json 2>&1'\\n\\nExit code: 127\\n\\nStdout:\\n\\nbash: line 1: python: command not found\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.0}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "b221446b-12e7-4861-82d4-ef957ac58ae4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_llama_docred_ft_grammar_only.jsonl --output_path /tmp/vr_llama_grammar.json 2>&1'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\nbash: line 1: python: command not found\\\\n\\\\nStderr:\\\\n\\\\n\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.0}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_llama_docred_ft_grammar_only.jsonl --output_path /tmp/vr_llama_grammar.json 2>&1'\\n\\nExit code: 127\\n\\nStdout:\\n\\nbash: line 1: python: command not found\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.0}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
`python` not found, probably need to use conda. The CLAUDE.md says this is an aml-train image that uses conda. Let me activate conda first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "8c947303-1e94-4c12-9e1f-ee4f70d87215",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01426Hbb3o71ZVyc5UygcQhu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 41471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1382
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

_source line 52_

需要激活 conda 环境。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "7a9c5b03-3461-4e1b-ba44-2eb63a94eec6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01426Hbb3o71ZVyc5UygcQhu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 41471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1382
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_013RjNThgDuMdSvc9Z6hE1u6`</summary>

```json
{
  "server": "westd-16980",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_qwen_docred_ft_semantic_only.jsonl --output_path /tmp/vr_qwen_semantic.json 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "d49eb9d5-9583-4484-a694-31274732e6ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01426Hbb3o71ZVyc5UygcQhu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 41471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1382
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01RQVHU8qpaSxa5a9VL7HjSj`</summary>

```json
{
  "server": "westd-16980",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_llama_docred_ft_semantic_only.jsonl --output_path /tmp/vr_llama_semantic.json 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "8fb236b3-39c9-4cfe-8838-aaee12504b71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01426Hbb3o71ZVyc5UygcQhu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 41471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1382
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

_source line 55 · 2026-05-23T11:41:47.195Z_

<details><summary>↩ Tool result · `toolu_013RjNThgDuMdSvc9Z6hE1u6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Violation Report (DocRED) ===\\nDocuments: 923 checked, 75 parse failures\\nEntities: 18025, Triples: 15909\\n\\nEntity type violations: 2 (0.0%)\\nRelation vocab violations: 37/15909 (0.2%)\\nDomain/range violations: 31/15909 (0.2%)\\nCross-field consistency violations: 32\\nFuzzy relation matches: 0\\n\\nGo/No-go metric (D/R violation rate): 0.0019\\nOutput: /tmp/vr_qwen_semantic.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "81ab0bf2-c2bf-4c22-9cd4-89abf16ac2c5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== Violation Report (DocRED) ===\\\\nDocuments: 923 checked, 75 parse failures\\\\nEntities: 18025, Triples: 15909\\\\n\\\\nEntity type violations: 2 (0.0%)\\\\nRelation vocab violations: 37/15909 (0.2%)\\\\nDomain/range violations: 31/15909 (0.2%)\\\\nCross-field consistency violations: 32\\\\nFuzzy relation matches: 0\\\\n\\\\nGo/No-go metric (D/R violation rate): 0.0019\\\\nOutput: /tmp/vr_qwen_semantic.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== Violation Report (DocRED) ===\\nDocuments: 923 checked, 75 parse failures\\nEntities: 18025, Triples: 15909\\n\\nEntity type violations: 2 (0.0%)\\nRelation vocab violations: 37/15909 (0.2%)\\nDomain/range violations: 31/15909 (0.2%)\\nCross-field consistency violations: 32\\nFuzzy relation matches: 0\\n\\nGo/No-go metric (D/R violation rate): 0.0019\\nOutput: /tmp/vr_qwen_semantic.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.49}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Bd9CFADfb7q7ykVuiZ74xM`</summary>

```json
{
  "server": "westd-16980",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w8_llama_docred_ft_grammar_only.jsonl --output_path /tmp/vr_llama_grammar.json 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "f0bb6e3b-8f26-4032-a5db-31c00b357161",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01426Hbb3o71ZVyc5UygcQhu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 41471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1382
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

_source line 57 · 2026-05-23T11:41:48.097Z_

<details><summary>↩ Tool result · `toolu_01RQVHU8qpaSxa5a9VL7HjSj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Violation Report (DocRED) ===\\nDocuments: 974 checked, 24 parse failures\\nEntities: 19099, Triples: 16038\\n\\nEntity type violations: 7 (0.0%)\\nRelation vocab violations: 24/16038 (0.1%)\\nDomain/range violations: 77/16038 (0.5%)\\nCross-field consistency violations: 31\\nFuzzy relation matches: 0\\n\\nGo/No-go metric (D/R violation rate): 0.0048\\nOutput: /tmp/vr_llama_semantic.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "c169235e-b5b4-47cd-b216-b3c21118f13a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== Violation Report (DocRED) ===\\\\nDocuments: 974 checked, 24 parse failures\\\\nEntities: 19099, Triples: 16038\\\\n\\\\nEntity type violations: 7 (0.0%)\\\\nRelation vocab violations: 24/16038 (0.1%)\\\\nDomain/range violations: 77/16038 (0.5%)\\\\nCross-field consistency violations: 31\\\\nFuzzy relation matches: 0\\\\n\\\\nGo/No-go metric (D/R violation rate): 0.0048\\\\nOutput: /tmp/vr_llama_semantic.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.89}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== Violation Report (DocRED) ===\\nDocuments: 974 checked, 24 parse failures\\nEntities: 19099, Triples: 16038\\n\\nEntity type violations: 7 (0.0%)\\nRelation vocab violations: 24/16038 (0.1%)\\nDomain/range violations: 77/16038 (0.5%)\\nCross-field consistency violations: 31\\nFuzzy relation matches: 0\\n\\nGo/No-go metric (D/R violation rate): 0.0048\\nOutput: /tmp/vr_llama_semantic.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-23T11:41:48.871Z_

<details><summary>↩ Tool result · `toolu_01Bd9CFADfb7q7ykVuiZ74xM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Violation Report (DocRED) ===\\nDocuments: 975 checked, 23 parse failures\\nEntities: 19116, Triples: 16199\\n\\nEntity type violations: 0 (0.0%)\\nRelation vocab violations: 0/16199 (0.0%)\\nDomain/range violations: 82/16199 (0.5%)\\nCross-field consistency violations: 16\\nFuzzy relation matches: 0\\n\\nGo/No-go metric (D/R violation rate): 0.0051\\nOutput: /tmp/vr_llama_grammar.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "c2c60faa-5e9f-4d1d-8fe8-e00e6e8ee72c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== Violation Report (DocRED) ===\\\\nDocuments: 975 checked, 23 parse failures\\\\nEntities: 19116, Triples: 16199\\\\n\\\\nEntity type violations: 0 (0.0%)\\\\nRelation vocab violations: 0/16199 (0.0%)\\\\nDomain/range violations: 82/16199 (0.5%)\\\\nCross-field consistency violations: 16\\\\nFuzzy relation matches: 0\\\\n\\\\nGo/No-go metric (D/R violation rate): 0.0051\\\\nOutput: /tmp/vr_llama_grammar.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.76}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== Violation Report (DocRED) ===\\nDocuments: 975 checked, 23 parse failures\\nEntities: 19116, Triples: 16199\\n\\nEntity type violations: 0 (0.0%)\\nRelation vocab violations: 0/16199 (0.0%)\\nDomain/range violations: 82/16199 (0.5%)\\nCross-field consistency violations: 16\\nFuzzy relation matches: 0\\n\\nGo/No-go metric (D/R violation rate): 0.0051\\nOutput: /tmp/vr_llama_grammar.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"
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
Now I have the results. Let me compile them:

1. **w8_qwen_docred_ft_semantic_only**: DR violations = 31/15909 = 0.0019 = 0.19%
   - Paper value: 0.21%
   - Recalculated: 0.19%
   - Deviation: -0.02pp

2. **w8_llama_docred_ft_semantic_only**: DR violations = 77/16038 = 0.0048 = 0.48%
   - Paper value: 0.30%
   - Recalculated: 0.48%
   - Deviation: +0.18pp — this is significant!

3. **w8_llama_docred_ft_grammar_only**: DR violations = 82/16199 = 0.0051 = 0.51%
   - Paper value: 0.51%
   - Recalculated: 0.51%
   - Deviation: 0.00pp — matches perfectly

The second model shows a notable discrepancy between the reported and recalculated violation rates, while the others align closely with the paper's values. The paper reports 0.30% for Llama semantic, but my recalculation shows 0.48%—a substantial gap. I'm wondering if there might be different versions of the violation checker being used, since the reviewer mentioned two separate violation report sets on the server. Let me examine the evaluation script more carefully to see if there's a classification mode parameter I'm missing, and review the full report JSON to understand how the violations are being counted. So 77/16038 = 0.004803... = 0.48%

But the paper claims 0.30%. That's a discrepancy of +0.18pp.

Let me check if there's a different version of the output file or if the issue is about different counting methods. Let me also check if there were previously generated violation reports.

Actually wait - maybe the paper value was computed from a different version of the checker? The checker says "checker_version: fixed_20260514_v2 (strip + alias + unique_et)". Maybe an older checker gave different results?

But the task says "用当前版本的评估脚本重算 DR 确认准确性" - use the current version. So if the current version gives 0.48%, that's what we should report.

Now I'm calculating the semantic DR reduction range. Looking at the unconstrained DR values for Qwen (0.76%) and Llama (0.49%), and comparing them against the semantic-only DR values I recalculated (0.19% and 0.48% respectively), I get reduction rates of 75.0% for Qwen but only 2.0% for Llama. That seems way too low compared to the claimed 39-72% range, so I need to reconsider where these unconstrained baseline values actually come from. I'm finding the unconstrained DR values in the posthoc reports I already have—the Qwen FT model removed 121 out of 15869 triples for domain_range violations (0.76%), and the Llama FT model removed 80 out of 16171 triples (0.49%), which matches the reported numbers exactly.

Now calculating the semantic-only DR reduction: for Qwen it's a 75% improvement, but for Llama I'm getting only 2% reduction, which contradicts the paper's claim of 39-72% improvement. Let me recheck the Llama semantic report more carefully—the paper reports 0.30% DR but my calculation shows 0.48%, so there's a discrepancy I need to resolve.

If the paper's 0.30% figure is correct, that would give us the 38.8% reduction matching the lower bound of their claimed range. The question is whether the checker version has been updated since the paper's results were generated, which might explain why I'm seeing different numbers. Let me examine the full JSON report for the Llama semantic case to understand where the difference comes from.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "24e9b55b-841e-42cc-a8cd-7e91f79504a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X9DQweHrtwD9pxGeLfARJd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 42853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1310
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

3 个结果都出来了。Llama semantic 的 DR 与论文值有较大偏差（0.48% vs 0.30%）。读详细报告确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "280254fe-21bd-42a9-aaf4-901d9a037561",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X9DQweHrtwD9pxGeLfARJd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 42853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1310
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GxFUKWj7CPhuzRH7obu94B`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"domain_range_violation\" /tmp/vr_llama_semantic.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "22ca8ef0-9609-4006-8561-946fb6699b12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X9DQweHrtwD9pxGeLfARJd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 42853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1310
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

_source line 62 · 2026-05-23T11:42:30.273Z_

<details><summary>↩ Tool result · `toolu_01GxFUKWj7CPhuzRH7obu94B`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"15:    \\\"domain_range_violations\\\": 77,\\n16:    \\\"domain_range_violation_rate\\\": 0.0048,\\n22:    \\\"go_nogo_metric_description\\\": \\\"per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)\\\"\\n27:      \\\"domain_range_violations\\\": 1,\\n32:      \\\"domain_range_violations\\\": 0,\\n37:      \\\"domain_range_violations\\\": 0,\\n42:      \\\"domain_range_violations\\\": 0,\\n47:      \\\"domain_range_violations\\\": 3,\\n52:      \\\"domain_range_violations\\\": 0,\\n57:      \\\"domain_range_violations\\\": 1,\\n62:      \\\"domain_range_violations\\\": 2,\\n67:      \\\"domain_range_violations\\\": 0,\\n72:      \\\"domain_range_violations\\\": 0,\\n77:      \\\"domain_range_violations\\\": 13,\\n82:      \\\"domain_range_violations\\\": 0,\\n87:      \\\"domain_range_violations\\\": 0,\\n92:      \\\"domain_range_violations\\\": 0,\\n97:      \\\"domain_range_violations\\\": 2,\\n102:      \\\"domain_range_violations\\\": 0,\\n107:      \\\"domain_range_violations\\\": 1,\\n112:      \\\"domain_range_violations\\\": 0,\\n117:      \\\"domain_range_violations\\\": 0,\\n122:      \\\"domain_range_violations\\\": 0,\\n127:      \\\"domain_range_violations\\\": 1,\\n132:      \\\"domain_range_violations\\\": 2,\\n137:      \\\"domain_range_violations\\\": 0,\\n142:      \\\"domain_range_violations\\\": 0,\\n147:      \\\"domain_range_violations\\\": 0,\\n152:      \\\"domain_range_violations\\\": 2,\\n157:      \\\"domain_range_violations\\\": 0,\\n162:      \\\"domain_range_violations\\\": 1,\\n167:      \\\"domain_range_violations\\\": 0,\\n172:      \\\"domain_range_violations\\\": 0,\\n177:      \\\"domain_range_violations\\\": 0,\\n182:      \\\"domain_range_violations\\\": 1,\\n187:      \\\"domain_range_violations\\\": 0,\\n192:      \\\"domain_range_violations\\\": 0,\\n197:      \\\"domain_range_violations\\\": 0,\\n202:      \\\"domain_range_violations\\\": 0,\\n207:      \\\"domain_range_violations\\\": 1,\\n212:      \\\"domain_range_violations\\\": 0,\\n217:      \\\"domain_range_violations\\\": 0,\\n222:      \\\"domain_range_violations\\\": 0,\\n227:      \\\"domain_range_violations\\\": 0,\\n232:      \\\"domain_range_violations\\\": 2,\\n237:      \\\"domain_range_violations\\\": 0,\\n242:      \\\"domain_range_violations\\\": 0,\\n247:      \\\"domain_range_violations\\\": 1,\\n252:      \\\"domain_range_violations\\\": 0,\\n257:      \\\"domain_range_violations\\\": 0,\\n262:      \\\"domain_range_violations\\\": 1,\\n267:      \\\"domain_range_violations\\\": 4,\\n272:      \\\"domain_range_violations\\\": 0,\\n277:      \\\"domain_range_violations\\\": 2,\\n282:      \\\"domain_range_violations\\\": 0,\\n287:      \\\"domain_range_violations\\\": 0,\\n292:      \\\"domain_range_violations\\\": 0,\\n297:      \\\"domain_range_violations\\\": 0,\\n302:      \\\"domain_range_violations\\\": 10,\\n307:      \\\"domain_range_violations\\\": 1,\\n312:      \\\"domain_range_violations\\\": 0,\\n317:      \\\"domain_range_violations\\\": 0,\\n322:      \\\"domain_range_violations\\\": 0,\\n327:      \\\"domain_range_violations\\\": 0,\\n332:      \\\"domain_range_violations\\\": 0,\\n337:      \\\"domain_range_violations\\\": 0,\\n342:      \\\"domain_range_violations\\\": 4,\\n347:      \\\"domain_range_violations\\\": 1,\\n352:      \\\"domain_range_violations\\\": 1,\\n357:      \\\"domain_range_violations\\\": 0,\\n362:      \\\"domain_range_violations\\\": 4,\\n367:      \\\"domain_range_violations\\\": 0,\\n372:      \\\"domain_range_violations\\\": 0,\\n377:      \\\"domain_range_violations\\\": 0,\\n382:      \\\"domain_range_violations\\\": 0,\\n387:      \\\"domain_range_violations\\\": 0,\\n392:      \\\"domain_range_violations\\\": 3,\\n397:      \\\"domain_range_violations\\\": 0,\\n402:      \\\"domain_range_violations\\\": 2,\\n407:      \\\"domain_range_violations\\\": 0,\\n412:      \\\"domain_range_violations\\\": 0,\\n417:      \\\"domain_range_violations\\\": 2,\\n422:      \\\"domain_range_violations\\\": 0,\\n427:      \\\"domain_range_violations\\\": 0,\\n432:      \\\"domain_range_violations\\\": 0,\\n437:      \\\"domain_range_violations\\\": 0,\\n442:      \\\"domain_range_violations\\\": 0,\\n447:      \\\"domain_range_violations\\\": 0,\\n452:      \\\"domain_range_violations\\\": 0,\\n457:      \\\"domain_range_violations\\\": 4,\\n462:      \\\"domain_range_violations\\\": 0,\\n467:      \\\"domain_range_violations\\\": 1,\\n472:      \\\"domain_range_violations\\\": 0,\\n477:      \\\"domain_range_violations\\\": 0,\\n482:      \\\"domain_range_violations\\\": 0,\\n487:      \\\"domain_range_violations\\\": 0,\\n492:      \\\"domain_range_violations\\\": 0,\\n497:      \\\"domain_range_violations\\\": 3,\\n502:     \\n\\n... [截断: 输出过长，省略 36489 字符] ...\\n\\n_range_violations\\\": 0,\\n8651:      \\\"domain_range_violations\\\": 0,\\n8660:      \\\"domain_range_violations\\\": 0,\\n8669:      \\\"domain_range_violations\\\": 0,\\n8678:      \\\"domain_range_violations\\\": 0,\\n8687:      \\\"domain_range_violations\\\": 0,\\n8696:      \\\"domain_range_violations\\\": 1,\\n8709:      \\\"domain_range_violations\\\": 0,\\n8718:      \\\"domain_range_violations\\\": 0,\\n8727:      \\\"domain_range_violations\\\": 0,\\n8740:      \\\"domain_range_violations\\\": 0,\\n8749:      \\\"domain_range_violations\\\": 0,\\n8758:      \\\"domain_range_violations\\\": 0,\\n8767:      \\\"domain_range_violations\\\": 0,\\n8776:      \\\"domain_range_violations\\\": 0,\\n8785:      \\\"domain_range_violations\\\": 0,\\n8794:      \\\"domain_range_violations\\\": 0,\\n8803:      \\\"domain_range_violations\\\": 0,\\n8812:      \\\"domain_range_violations\\\": 0,\\n8821:      \\\"domain_range_violations\\\": 0,\\n8830:      \\\"domain_range_violations\\\": 0,\\n8839:      \\\"domain_range_violations\\\": 0,\\n8848:      \\\"domain_range_violations\\\": 0,\\n8857:      \\\"domain_range_violations\\\": 0,\\n8866:      \\\"domain_range_violations\\\": 0,\\n8875:      \\\"domain_range_violations\\\": 0,\\n8884:      \\\"domain_range_violations\\\": 0,\\n8893:      \\\"domain_range_violations\\\": 0,\\n8902:      \\\"domain_range_violations\\\": 0,\\n8911:      \\\"domain_range_violations\\\": 0,\\n8920:      \\\"domain_range_violations\\\": 0,\\n8929:      \\\"domain_range_violations\\\": 0,\\n8942:      \\\"domain_range_violations\\\": 0,\\n8951:      \\\"domain_range_violations\\\": 0,\\n8960:      \\\"domain_range_violations\\\": 1,\\n8969:      \\\"domain_range_violations\\\": 0,\\n8978:      \\\"domain_range_violations\\\": 0,\\n8987:      \\\"domain_range_violations\\\": 0,\\n8996:      \\\"domain_range_violations\\\": 0,\\n9005:      \\\"domain_range_violations\\\": 0,\\n9014:      \\\"domain_range_violations\\\": 0,\\n9023:      \\\"domain_range_violations\\\": 0,\\n9032:      \\\"domain_range_violations\\\": 0,\\n9041:      \\\"domain_range_violations\\\": 0,\\n9050:      \\\"domain_range_violations\\\": 0,\\n9059:      \\\"domain_range_violations\\\": 0,\\n9068:      \\\"domain_range_violations\\\": 0,\\n9077:      \\\"domain_range_violations\\\": 0,\\n9086:      \\\"domain_range_violations\\\": 0,\\n9099:      \\\"domain_range_violations\\\": 0,\\n9108:      \\\"domain_range_violations\\\": 0,\\n9117:      \\\"domain_range_violations\\\": 0,\\n9126:      \\\"domain_range_violations\\\": 0,\\n9135:      \\\"domain_range_violations\\\": 0,\\n9144:      \\\"domain_range_violations\\\": 0,\\n9153:      \\\"domain_range_violations\\\": 0,\\n9162:      \\\"domain_range_violations\\\": 0,\\n9171:      \\\"domain_range_violations\\\": 0,\\n9180:      \\\"domain_range_violations\\\": 0,\\n9189:      \\\"domain_range_violations\\\": 0,\\n9198:      \\\"domain_range_violations\\\": 0,\\n9207:      \\\"domain_range_violations\\\": 0,\\n9216:      \\\"domain_range_violations\\\": 0,\\n9225:      \\\"domain_range_violations\\\": 0,\\n9234:      \\\"domain_range_violations\\\": 0,\\n9243:      \\\"domain_range_violations\\\": 0,\\n9252:      \\\"domain_range_violations\\\": 0,\\n9261:      \\\"domain_range_violations\\\": 0,\\n9270:      \\\"domain_range_violations\\\": 0,\\n9279:      \\\"domain_range_violations\\\": 0,\\n9288:      \\\"domain_range_violations\\\": 0,\\n9297:      \\\"domain_range_violations\\\": 0,\\n9306:      \\\"domain_range_violations\\\": 0,\\n9315:      \\\"domain_range_violations\\\": 0,\\n9324:      \\\"domain_range_violations\\\": 0,\\n9333:      \\\"domain_range_violations\\\": 0,\\n9342:      \\\"domain_range_violations\\\": 0,\\n9351:      \\\"domain_range_violations\\\": 0,\\n9360:      \\\"domain_range_violations\\\": 0,\\n9369:      \\\"domain_range_violations\\\": 0,\\n9378:      \\\"domain_range_violations\\\": 0,\\n9387:      \\\"domain_range_violations\\\": 3,\\n9396:      \\\"domain_range_violations\\\": 0,\\n9405:      \\\"domain_range_violations\\\": 0,\\n9414:      \\\"domain_range_violations\\\": 0,\\n9423:      \\\"domain_range_violations\\\": 0,\\n9432:      \\\"domain_range_violations\\\": 0,\\n9441:      \\\"domain_range_violations\\\": 0,\\n9450:      \\\"domain_range_violations\\\": 0,\\n9459:      \\\"domain_range_violations\\\": 0,\\n9468:      \\\"domain_range_violations\\\": 0,\\n9477:      \\\"domain_range_violations\\\": 0,\\n9486:      \\\"domain_range_violations\\\": 0,\\n9495:      \\\"domain_range_violations\\\": 0,\\n9504:      \\\"domain_range_violations\\\": 0,\\n9513:      \\\"domain_range_violations\\\": 0,\\n9522:      \\\"domain_range_violations\\\": 0,\\n9531:      \\\"domain_range_violations\\\": 0,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "b53dba12-ee93-496a-a54b-d8b51c82e05d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"15:    \\\\\\\"domain_range_violations\\\\\\\": 77,\\\\n16:    \\\\\\\"domain_range_violation_rate\\\\\\\": 0.0048,\\\\n22:    \\\\\\\"go_nogo_metric_description\\\\\\\": \\\\\\\"per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)\\\\\\\"\\\\n27:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n32:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n37:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n42:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n47:      \\\\\\\"domain_range_violations\\\\\\\": 3,\\\\n52:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n57:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n62:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n67:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n72:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n77:      \\\\\\\"domain_range_violations\\\\\\\": 13,\\\\n82:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n87:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n92:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n97:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n102:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n107:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n112:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n117:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n122:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n127:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n132:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n137:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n142:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n147:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n152:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n157:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n162:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n167:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n172:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n177:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n182:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n187:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n192:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n197:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n202:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n207:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n212:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n217:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n222:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n227:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n232:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n237:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n242:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n247:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n252:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n257:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n262:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n267:      \\\\\\\"domain_range_violations\\\\\\\": 4,\\\\n272:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n277:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n282:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n287:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n292:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n297:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n302:      \\\\\\\"domain_range_violations\\\\\\\": 10,\\\\n307:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n312:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n317:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n322:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n327:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n332:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n337:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n342:      \\\\\\\"domain_range_violations\\\\\\\": 4,\\\\n347:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n352:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n357:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n362:      \\\\\\\"domain_range_violations\\\\\\\": 4,\\\\n367:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n372:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n377:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n382:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n387:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n392:      \\\\\\\"domain_range_violations\\\\\\\": 3,\\\\n397:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n402:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n407:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n412:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n417:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n422:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n427:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n432:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n437:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n442:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n447:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n452:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n457:      \\\\\\\"domain_range_violations\\\\\\\": 4,\\\\n462:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n467:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n472:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n477:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n482:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n487:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n492:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n497:      \\\\\\\"domain_range_violations\\\\\\\": 3,\\\\n502:     \\\\n\\\\n... [截断: 输出过长，省略 36489 字符] ...\\\\n\\\\n_range_violations\\\\\\\": 0,\\\\n8651:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8660:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8669:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8678:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8687:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8696:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n8709:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8718:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8727:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8740:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8749:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8758:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8767:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8776:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8785:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8794:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8803:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8812:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8821:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8830:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8839:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8848:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8857:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8866:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8875:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8884:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8893:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8902:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8911:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8920:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8929:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8942:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8951:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8960:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n8969:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8978:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8987:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8996:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9005:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9014:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9023:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9032:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9041:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9050:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9059:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9068:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9077:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9086:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9099:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9108:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9117:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9126:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9135:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9144:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9153:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9162:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9171:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9180:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9189:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9198:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9207:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9216:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9225:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9234:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9243:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9252:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9261:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9270:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9279:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9288:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9297:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9306:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9315:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9324:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9333:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9342:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9351:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9360:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9369:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9378:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9387:      \\\\\\\"domain_range_violations\\\\\\\": 3,\\\\n9396:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9405:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9414:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9423:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9432:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9441:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9450:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9459:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9468:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9477:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9486:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9495:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9504:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9513:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9522:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9531:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.58}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"15:    \\\"domain_range_violations\\\": 77,\\n16:    \\\"domain_range_violation_rate\\\": 0.0048,\\n22:    \\\"go_nogo_metric_description\\\": \\\"per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)\\\"\\n27:      \\\"domain_range_violations\\\": 1,\\n32:      \\\"domain_range_violations\\\": 0,\\n37:      \\\"domain_range_violations\\\": 0,\\n42:      \\\"domain_range_violations\\\": 0,\\n47:      \\\"domain_range_violations\\\": 3,\\n52:      \\\"domain_range_violations\\\": 0,\\n57:      \\\"domain_range_violations\\\": 1,\\n62:      \\\"domain_range_violations\\\": 2,\\n67:      \\\"domain_range_violations\\\": 0,\\n72:      \\\"domain_range_violations\\\": 0,\\n77:      \\\"domain_range_violations\\\": 13,\\n82:      \\\"domain_range_violations\\\": 0,\\n87:      \\\"domain_range_violations\\\": 0,\\n92:      \\\"domain_range_violations\\\": 0,\\n97:      \\\"domain_range_violations\\\": 2,\\n102:      \\\"domain_range_violations\\\": 0,\\n107:      \\\"domain_range_violations\\\": 1,\\n112:      \\\"domain_range_violations\\\": 0,\\n117:      \\\"domain_range_violations\\\": 0,\\n122:      \\\"domain_range_violations\\\": 0,\\n127:      \\\"domain_range_violations\\\": 1,\\n132:      \\\"domain_range_violations\\\": 2,\\n137:      \\\"domain_range_violations\\\": 0,\\n142:      \\\"domain_range_violations\\\": 0,\\n147:      \\\"domain_range_violations\\\": 0,\\n152:      \\\"domain_range_violations\\\": 2,\\n157:      \\\"domain_range_violations\\\": 0,\\n162:      \\\"domain_range_violations\\\": 1,\\n167:      \\\"domain_range_violations\\\": 0,\\n172:      \\\"domain_range_violations\\\": 0,\\n177:      \\\"domain_range_violations\\\": 0,\\n182:      \\\"domain_range_violations\\\": 1,\\n187:      \\\"domain_range_violations\\\": 0,\\n192:      \\\"domain_range_violations\\\": 0,\\n197:      \\\"domain_range_violations\\\": 0,\\n202:      \\\"domain_range_violations\\\": 0,\\n207:      \\\"domain_range_violations\\\": 1,\\n212:      \\\"domain_range_violations\\\": 0,\\n217:      \\\"domain_range_violations\\\": 0,\\n222:      \\\"domain_range_violations\\\": 0,\\n227:      \\\"domain_range_violations\\\": 0,\\n232:      \\\"domain_range_violations\\\": 2,\\n237:      \\\"domain_range_violations\\\": 0,\\n242:      \\\"domain_range_violations\\\": 0,\\n247:      \\\"domain_range_violations\\\": 1,\\n252:      \\\"domain_range_violations\\\": 0,\\n257:      \\\"domain_range_violations\\\": 0,\\n262:      \\\"domain_range_violations\\\": 1,\\n267:      \\\"domain_range_violations\\\": 4,\\n272:      \\\"domain_range_violations\\\": 0,\\n277:      \\\"domain_range_violations\\\": 2,\\n282:      \\\"domain_range_violations\\\": 0,\\n287:      \\\"domain_range_violations\\\": 0,\\n292:      \\\"domain_range_violations\\\": 0,\\n297:      \\\"domain_range_violations\\\": 0,\\n302:      \\\"domain_range_violations\\\": 10,\\n307:      \\\"domain_range_violations\\\": 1,\\n312:      \\\"domain_range_violations\\\": 0,\\n317:      \\\"domain_range_violations\\\": 0,\\n322:      \\\"domain_range_violations\\\": 0,\\n327:      \\\"domain_range_violations\\\": 0,\\n332:      \\\"domain_range_violations\\\": 0,\\n337:      \\\"domain_range_violations\\\": 0,\\n342:      \\\"domain_range_violations\\\": 4,\\n347:      \\\"domain_range_violations\\\": 1,\\n352:      \\\"domain_range_violations\\\": 1,\\n357:      \\\"domain_range_violations\\\": 0,\\n362:      \\\"domain_range_violations\\\": 4,\\n367:      \\\"domain_range_violations\\\": 0,\\n372:      \\\"domain_range_violations\\\": 0,\\n377:      \\\"domain_range_violations\\\": 0,\\n382:      \\\"domain_range_violations\\\": 0,\\n387:      \\\"domain_range_violations\\\": 0,\\n392:      \\\"domain_range_violations\\\": 3,\\n397:      \\\"domain_range_violations\\\": 0,\\n402:      \\\"domain_range_violations\\\": 2,\\n407:      \\\"domain_range_violations\\\": 0,\\n412:      \\\"domain_range_violations\\\": 0,\\n417:      \\\"domain_range_violations\\\": 2,\\n422:      \\\"domain_range_violations\\\": 0,\\n427:      \\\"domain_range_violations\\\": 0,\\n432:      \\\"domain_range_violations\\\": 0,\\n437:      \\\"domain_range_violations\\\": 0,\\n442:      \\\"domain_range_violations\\\": 0,\\n447:      \\\"domain_range_violations\\\": 0,\\n452:      \\\"domain_range_violations\\\": 0,\\n457:      \\\"domain_range_violations\\\": 4,\\n462:      \\\"domain_range_violations\\\": 0,\\n467:      \\\"domain_range_violations\\\": 1,\\n472:      \\\"domain_range_violations\\\": 0,\\n477:      \\\"domain_range_violations\\\": 0,\\n482:      \\\"domain_range_violations\\\": 0,\\n487:      \\\"domain_range_violations\\\": 0,\\n492:      \\\"domain_range_violations\\\": 0,\\n497:      \\\"domain_range_violations\\\": 3,\\n502:     \\n\\n... [截断: 输出过长，省略 36489 字符] ...\\n\\n_range_violations\\\": 0,\\n8651:      \\\"domain_range_violations\\\": 0,\\n8660:      \\\"domain_range_violations\\\": 0,\\n8669:      \\\"domain_range_violations\\\": 0,\\n8678:      \\\"domain_range_violations\\\": 0,\\n8687:      \\\"domain_range_violations\\\": 0,\\n8696:      \\\"domain_range_violations\\\": 1,\\n8709:      \\\"domain_range_violations\\\": 0,\\n8718:      \\\"domain_range_violations\\\": 0,\\n8727:      \\\"domain_range_violations\\\": 0,\\n8740:      \\\"domain_range_violations\\\": 0,\\n8749:      \\\"domain_range_violations\\\": 0,\\n8758:      \\\"domain_range_violations\\\": 0,\\n8767:      \\\"domain_range_violations\\\": 0,\\n8776:      \\\"domain_range_violations\\\": 0,\\n8785:      \\\"domain_range_violations\\\": 0,\\n8794:      \\\"domain_range_violations\\\": 0,\\n8803:      \\\"domain_range_violations\\\": 0,\\n8812:      \\\"domain_range_violations\\\": 0,\\n8821:      \\\"domain_range_violations\\\": 0,\\n8830:      \\\"domain_range_violations\\\": 0,\\n8839:      \\\"domain_range_violations\\\": 0,\\n8848:      \\\"domain_range_violations\\\": 0,\\n8857:      \\\"domain_range_violations\\\": 0,\\n8866:      \\\"domain_range_violations\\\": 0,\\n8875:      \\\"domain_range_violations\\\": 0,\\n8884:      \\\"domain_range_violations\\\": 0,\\n8893:      \\\"domain_range_violations\\\": 0,\\n8902:      \\\"domain_range_violations\\\": 0,\\n8911:      \\\"domain_range_violations\\\": 0,\\n8920:      \\\"domain_range_violations\\\": 0,\\n8929:      \\\"domain_range_violations\\\": 0,\\n8942:      \\\"domain_range_violations\\\": 0,\\n8951:      \\\"domain_range_violations\\\": 0,\\n8960:      \\\"domain_range_violations\\\": 1,\\n8969:      \\\"domain_range_violations\\\": 0,\\n8978:      \\\"domain_range_violations\\\": 0,\\n8987:      \\\"domain_range_violations\\\": 0,\\n8996:      \\\"domain_range_violations\\\": 0,\\n9005:      \\\"domain_range_violations\\\": 0,\\n9014:      \\\"domain_range_violations\\\": 0,\\n9023:      \\\"domain_range_violations\\\": 0,\\n9032:      \\\"domain_range_violations\\\": 0,\\n9041:      \\\"domain_range_violations\\\": 0,\\n9050:      \\\"domain_range_violations\\\": 0,\\n9059:      \\\"domain_range_violations\\\": 0,\\n9068:      \\\"domain_range_violations\\\": 0,\\n9077:      \\\"domain_range_violations\\\": 0,\\n9086:      \\\"domain_range_violations\\\": 0,\\n9099:      \\\"domain_range_violations\\\": 0,\\n9108:      \\\"domain_range_violations\\\": 0,\\n9117:      \\\"domain_range_violations\\\": 0,\\n9126:      \\\"domain_range_violations\\\": 0,\\n9135:      \\\"domain_range_violations\\\": 0,\\n9144:      \\\"domain_range_violations\\\": 0,\\n9153:      \\\"domain_range_violations\\\": 0,\\n9162:      \\\"domain_range_violations\\\": 0,\\n9171:      \\\"domain_range_violations\\\": 0,\\n9180:      \\\"domain_range_violations\\\": 0,\\n9189:      \\\"domain_range_violations\\\": 0,\\n9198:      \\\"domain_range_violations\\\": 0,\\n9207:      \\\"domain_range_violations\\\": 0,\\n9216:      \\\"domain_range_violations\\\": 0,\\n9225:      \\\"domain_range_violations\\\": 0,\\n9234:      \\\"domain_range_violations\\\": 0,\\n9243:      \\\"domain_range_violations\\\": 0,\\n9252:      \\\"domain_range_violations\\\": 0,\\n9261:      \\\"domain_range_violations\\\": 0,\\n9270:      \\\"domain_range_violations\\\": 0,\\n9279:      \\\"domain_range_violations\\\": 0,\\n9288:      \\\"domain_range_violations\\\": 0,\\n9297:      \\\"domain_range_violations\\\": 0,\\n9306:      \\\"domain_range_violations\\\": 0,\\n9315:      \\\"domain_range_violations\\\": 0,\\n9324:      \\\"domain_range_violations\\\": 0,\\n9333:      \\\"domain_range_violations\\\": 0,\\n9342:      \\\"domain_range_violations\\\": 0,\\n9351:      \\\"domain_range_violations\\\": 0,\\n9360:      \\\"domain_range_violations\\\": 0,\\n9369:      \\\"domain_range_violations\\\": 0,\\n9378:      \\\"domain_range_violations\\\": 0,\\n9387:      \\\"domain_range_violations\\\": 3,\\n9396:      \\\"domain_range_violations\\\": 0,\\n9405:      \\\"domain_range_violations\\\": 0,\\n9414:      \\\"domain_range_violations\\\": 0,\\n9423:      \\\"domain_range_violations\\\": 0,\\n9432:      \\\"domain_range_violations\\\": 0,\\n9441:      \\\"domain_range_violations\\\": 0,\\n9450:      \\\"domain_range_violations\\\": 0,\\n9459:      \\\"domain_range_violations\\\": 0,\\n9468:      \\\"domain_range_violations\\\": 0,\\n9477:      \\\"domain_range_violations\\\": 0,\\n9486:      \\\"domain_range_violations\\\": 0,\\n9495:      \\\"domain_range_violations\\\": 0,\\n9504:      \\\"domain_range_violations\\\": 0,\\n9513:      \\\"domain_range_violations\\\": 0,\\n9522:      \\\"domain_range_violations\\\": 0,\\n9531:      \\\"domain_range_violations\\\": 0,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01B5dswT1ZQCJsAdwkdcTGT3`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"domain_range_violation\" /tmp/vr_qwen_semantic.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "ff060c06-d7ca-411d-889d-7d4fd7f9a19f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X9DQweHrtwD9pxGeLfARJd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 42853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1310
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

_source line 64_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Jg9jQuCoDoKncZa9amoEyx`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"domain_range_violation\" /tmp/vr_llama_grammar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "bf45dbea-ebbd-4d88-9b71-25a2323c83ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X9DQweHrtwD9pxGeLfARJd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 42853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1310
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

_source line 65 · 2026-05-23T11:42:31.133Z_

<details><summary>↩ Tool result · `toolu_01B5dswT1ZQCJsAdwkdcTGT3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"15:    \\\"domain_range_violations\\\": 31,\\n16:    \\\"domain_range_violation_rate\\\": 0.0019,\\n22:    \\\"go_nogo_metric_description\\\": \\\"per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)\\\"\\n27:      \\\"domain_range_violations\\\": 0,\\n32:      \\\"domain_range_violations\\\": 0,\\n37:      \\\"domain_range_violations\\\": 0,\\n42:      \\\"domain_range_violations\\\": 0,\\n47:      \\\"domain_range_violations\\\": 0,\\n52:      \\\"domain_range_violations\\\": 0,\\n57:      \\\"domain_range_violations\\\": 0,\\n62:      \\\"domain_range_violations\\\": 0,\\n67:      \\\"domain_range_violations\\\": 0,\\n72:      \\\"domain_range_violations\\\": 0,\\n77:      \\\"domain_range_violations\\\": 0,\\n82:      \\\"domain_range_violations\\\": 0,\\n87:      \\\"domain_range_violations\\\": 0,\\n92:      \\\"domain_range_violations\\\": 1,\\n97:      \\\"domain_range_violations\\\": 3,\\n102:      \\\"domain_range_violations\\\": 0,\\n107:      \\\"domain_range_violations\\\": 0,\\n112:      \\\"domain_range_violations\\\": 0,\\n117:      \\\"domain_range_violations\\\": 13,\\n122:      \\\"domain_range_violations\\\": 0,\\n127:      \\\"domain_range_violations\\\": 1,\\n132:      \\\"domain_range_violations\\\": 1,\\n137:      \\\"domain_range_violations\\\": 0,\\n142:      \\\"domain_range_violations\\\": 0,\\n147:      \\\"domain_range_violations\\\": 0,\\n152:      \\\"domain_range_violations\\\": 2,\\n157:      \\\"domain_range_violations\\\": 2,\\n162:      \\\"domain_range_violations\\\": 0,\\n167:      \\\"domain_range_violations\\\": 0,\\n172:      \\\"domain_range_violations\\\": 0,\\n177:      \\\"domain_range_violations\\\": 0,\\n182:      \\\"domain_range_violations\\\": 0,\\n187:      \\\"domain_range_violations\\\": 0,\\n192:      \\\"domain_range_violations\\\": 1,\\n197:      \\\"domain_range_violations\\\": 0,\\n202:      \\\"domain_range_violations\\\": 0,\\n207:      \\\"domain_range_violations\\\": 0,\\n212:      \\\"domain_range_violations\\\": 0,\\n217:      \\\"domain_range_violations\\\": 0,\\n222:      \\\"domain_range_violations\\\": 0,\\n227:      \\\"domain_range_violations\\\": 2,\\n232:      \\\"domain_range_violations\\\": 0,\\n237:      \\\"domain_range_violations\\\": 0,\\n242:      \\\"domain_range_violations\\\": 0,\\n247:      \\\"domain_range_violations\\\": 2,\\n252:      \\\"domain_range_violations\\\": 0,\\n257:      \\\"domain_range_violations\\\": 0,\\n262:      \\\"domain_range_violations\\\": 1,\\n267:      \\\"domain_range_violations\\\": 0,\\n272:      \\\"domain_range_violations\\\": 0,\\n277:      \\\"domain_range_violations\\\": 0,\\n282:      \\\"domain_range_violations\\\": 0,\\n287:      \\\"domain_range_violations\\\": 0,\\n292:      \\\"domain_range_violations\\\": 0,\\n297:      \\\"domain_range_violations\\\": 0,\\n302:      \\\"domain_range_violations\\\": 0,\\n307:      \\\"domain_range_violations\\\": 0,\\n312:      \\\"domain_range_violations\\\": 0,\\n317:      \\\"domain_range_violations\\\": 0,\\n322:      \\\"domain_range_violations\\\": 0,\\n327:      \\\"domain_range_violations\\\": 0,\\n332:      \\\"domain_range_violations\\\": 0,\\n337:      \\\"domain_range_violations\\\": 1,\\n342:      \\\"domain_range_violations\\\": 0,\\n347:      \\\"domain_range_violations\\\": 0,\\n352:      \\\"domain_range_violations\\\": 0,\\n357:      \\\"domain_range_violations\\\": 0,\\n362:      \\\"domain_range_violations\\\": 0,\\n367:      \\\"domain_range_violations\\\": 0,\\n372:      \\\"domain_range_violations\\\": 0,\\n377:      \\\"domain_range_violations\\\": 0,\\n382:      \\\"domain_range_violations\\\": 0,\\n387:      \\\"domain_range_violations\\\": 0,\\n392:      \\\"domain_range_violations\\\": 0,\\n397:      \\\"domain_range_violations\\\": 0,\\n402:      \\\"domain_range_violations\\\": 0,\\n407:      \\\"domain_range_violations\\\": 0,\\n412:      \\\"domain_range_violations\\\": 0,\\n417:      \\\"domain_range_violations\\\": 0,\\n422:      \\\"domain_range_violations\\\": 0,\\n427:      \\\"domain_range_violations\\\": 0,\\n432:      \\\"domain_range_violations\\\": 0,\\n437:      \\\"domain_range_violations\\\": 0,\\n442:      \\\"domain_range_violations\\\": 0,\\n447:      \\\"domain_range_violations\\\": 0,\\n452:      \\\"domain_range_violations\\\": 1,\\n457:      \\\"domain_range_violations\\\": 0,\\n462:      \\\"domain_range_violations\\\": 0,\\n467:      \\\"domain_range_violations\\\": 0,\\n472:      \\\"domain_range_violations\\\": 0,\\n477:      \\\"domain_range_violations\\\": 0,\\n482:      \\\"domain_range_violations\\\": 0,\\n487:      \\\"domain_range_violations\\\": 0,\\n492:      \\\"domain_range_violations\\\": 0,\\n497:      \\\"domain_range_violations\\\": 0,\\n502:      \\n\\n... [截断: 输出过长，省略 34557 字符] ...\\n\\n_range_violations\\\": 0,\\n8399:      \\\"domain_range_violations\\\": 0,\\n8408:      \\\"domain_range_violations\\\": 0,\\n8417:      \\\"domain_range_violations\\\": 0,\\n8426:      \\\"domain_range_violations\\\": 0,\\n8435:      \\\"domain_range_violations\\\": 0,\\n8444:      \\\"domain_range_violations\\\": 0,\\n8453:      \\\"domain_range_violations\\\": 0,\\n8462:      \\\"domain_range_violations\\\": 0,\\n8471:      \\\"domain_range_violations\\\": 1,\\n8480:      \\\"domain_range_violations\\\": 0,\\n8489:      \\\"domain_range_violations\\\": 0,\\n8498:      \\\"domain_range_violations\\\": 0,\\n8507:      \\\"domain_range_violations\\\": 0,\\n8516:      \\\"domain_range_violations\\\": 0,\\n8525:      \\\"domain_range_violations\\\": 0,\\n8534:      \\\"domain_range_violations\\\": 0,\\n8543:      \\\"domain_range_violations\\\": 0,\\n8552:      \\\"domain_range_violations\\\": 0,\\n8561:      \\\"domain_range_violations\\\": 0,\\n8570:      \\\"domain_range_violations\\\": 0,\\n8579:      \\\"domain_range_violations\\\": 0,\\n8588:      \\\"domain_range_violations\\\": 0,\\n8597:      \\\"domain_range_violations\\\": 0,\\n8606:      \\\"domain_range_violations\\\": 0,\\n8619:      \\\"domain_range_violations\\\": 0,\\n8632:      \\\"domain_range_violations\\\": 0,\\n8641:      \\\"domain_range_violations\\\": 0,\\n8650:      \\\"domain_range_violations\\\": 0,\\n8659:      \\\"domain_range_violations\\\": 0,\\n8668:      \\\"domain_range_violations\\\": 0,\\n8677:      \\\"domain_range_violations\\\": 0,\\n8686:      \\\"domain_range_violations\\\": 0,\\n8695:      \\\"domain_range_violations\\\": 0,\\n8704:      \\\"domain_range_violations\\\": 0,\\n8713:      \\\"domain_range_violations\\\": 0,\\n8722:      \\\"domain_range_violations\\\": 0,\\n8731:      \\\"domain_range_violations\\\": 0,\\n8740:      \\\"domain_range_violations\\\": 0,\\n8749:      \\\"domain_range_violations\\\": 0,\\n8758:      \\\"domain_range_violations\\\": 0,\\n8767:      \\\"domain_range_violations\\\": 0,\\n8776:      \\\"domain_range_violations\\\": 0,\\n8785:      \\\"domain_range_violations\\\": 0,\\n8794:      \\\"domain_range_violations\\\": 0,\\n8803:      \\\"domain_range_violations\\\": 0,\\n8812:      \\\"domain_range_violations\\\": 0,\\n8821:      \\\"domain_range_violations\\\": 0,\\n8830:      \\\"domain_range_violations\\\": 0,\\n8839:      \\\"domain_range_violations\\\": 0,\\n8848:      \\\"domain_range_violations\\\": 0,\\n8861:      \\\"domain_range_violations\\\": 0,\\n8874:      \\\"domain_range_violations\\\": 0,\\n8883:      \\\"domain_range_violations\\\": 0,\\n8892:      \\\"domain_range_violations\\\": 0,\\n8901:      \\\"domain_range_violations\\\": 0,\\n8910:      \\\"domain_range_violations\\\": 0,\\n8919:      \\\"domain_range_violations\\\": 0,\\n8928:      \\\"domain_range_violations\\\": 0,\\n8937:      \\\"domain_range_violations\\\": 0,\\n8946:      \\\"domain_range_violations\\\": 0,\\n8955:      \\\"domain_range_violations\\\": 0,\\n8964:      \\\"domain_range_violations\\\": 0,\\n8977:      \\\"domain_range_violations\\\": 0,\\n8986:      \\\"domain_range_violations\\\": 0,\\n8995:      \\\"domain_range_violations\\\": 0,\\n9008:      \\\"domain_range_violations\\\": 0,\\n9017:      \\\"domain_range_violations\\\": 0,\\n9026:      \\\"domain_range_violations\\\": 0,\\n9035:      \\\"domain_range_violations\\\": 0,\\n9044:      \\\"domain_range_violations\\\": 0,\\n9053:      \\\"domain_range_violations\\\": 0,\\n9062:      \\\"domain_range_violations\\\": 0,\\n9071:      \\\"domain_range_violations\\\": 0,\\n9080:      \\\"domain_range_violations\\\": 0,\\n9089:      \\\"domain_range_violations\\\": 0,\\n9098:      \\\"domain_range_violations\\\": 0,\\n9107:      \\\"domain_range_violations\\\": 0,\\n9116:      \\\"domain_range_violations\\\": 0,\\n9125:      \\\"domain_range_violations\\\": 0,\\n9134:      \\\"domain_range_violations\\\": 0,\\n9143:      \\\"domain_range_violations\\\": 0,\\n9152:      \\\"domain_range_violations\\\": 0,\\n9161:      \\\"domain_range_violations\\\": 0,\\n9170:      \\\"domain_range_violations\\\": 0,\\n9179:      \\\"domain_range_violations\\\": 0,\\n9188:      \\\"domain_range_violations\\\": 0,\\n9197:      \\\"domain_range_violations\\\": 0,\\n9210:      \\\"domain_range_violations\\\": 0,\\n9219:      \\\"domain_range_violations\\\": 0,\\n9228:      \\\"domain_range_violations\\\": 0,\\n9237:      \\\"domain_range_violations\\\": 0,\\n9246:      \\\"domain_range_violations\\\": 0,\\n9255:      \\\"domain_range_violations\\\": 0,\\n9264:      \\\"domain_range_violations\\\": 0,\\n9273:      \\\"domain_range_violations\\\": 0,\\n9282:      \\\"domain_range_violations\\\": 0,\\n9291:      \\\"domain_range_violations\\\": 0,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "ba7ddf1d-cbd2-4d4c-8950-f6d8edd19b4b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"15:    \\\\\\\"domain_range_violations\\\\\\\": 31,\\\\n16:    \\\\\\\"domain_range_violation_rate\\\\\\\": 0.0019,\\\\n22:    \\\\\\\"go_nogo_metric_description\\\\\\\": \\\\\\\"per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)\\\\\\\"\\\\n27:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n32:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n37:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n42:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n47:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n52:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n57:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n62:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n67:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n72:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n77:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n82:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n87:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n92:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n97:      \\\\\\\"domain_range_violations\\\\\\\": 3,\\\\n102:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n107:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n112:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n117:      \\\\\\\"domain_range_violations\\\\\\\": 13,\\\\n122:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n127:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n132:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n137:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n142:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n147:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n152:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n157:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n162:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n167:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n172:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n177:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n182:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n187:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n192:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n197:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n202:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n207:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n212:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n217:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n222:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n227:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n232:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n237:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n242:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n247:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n252:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n257:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n262:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n267:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n272:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n277:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n282:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n287:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n292:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n297:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n302:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n307:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n312:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n317:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n322:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n327:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n332:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n337:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n342:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n347:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n352:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n357:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n362:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n367:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n372:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n377:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n382:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n387:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n392:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n397:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n402:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n407:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n412:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n417:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n422:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n427:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n432:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n437:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n442:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n447:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n452:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n457:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n462:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n467:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n472:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n477:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n482:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n487:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n492:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n497:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n502:      \\\\n\\\\n... [截断: 输出过长，省略 34557 字符] ...\\\\n\\\\n_range_violations\\\\\\\": 0,\\\\n8399:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8408:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8417:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8426:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8435:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8444:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8453:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8462:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8471:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n8480:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8489:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8498:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8507:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8516:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8525:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8534:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8543:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8552:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8561:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8570:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8579:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8588:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8597:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8606:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8619:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8632:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8641:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8650:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8659:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8668:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8677:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8686:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8695:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8704:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8713:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8722:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8731:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8740:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8749:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8758:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8767:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8776:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8785:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8794:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8803:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8812:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8821:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8830:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8839:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8848:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8861:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8874:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8883:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8892:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8901:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8910:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8919:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8928:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8937:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8946:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8955:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8964:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8977:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8986:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8995:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9008:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9017:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9026:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9035:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9044:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9053:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9062:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9071:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9080:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9089:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9098:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9107:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9116:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9125:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9134:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9143:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9152:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9161:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9170:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9179:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9188:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9197:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9210:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9219:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9228:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9237:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9246:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9255:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9264:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9273:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9282:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9291:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"15:    \\\"domain_range_violations\\\": 31,\\n16:    \\\"domain_range_violation_rate\\\": 0.0019,\\n22:    \\\"go_nogo_metric_description\\\": \\\"per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)\\\"\\n27:      \\\"domain_range_violations\\\": 0,\\n32:      \\\"domain_range_violations\\\": 0,\\n37:      \\\"domain_range_violations\\\": 0,\\n42:      \\\"domain_range_violations\\\": 0,\\n47:      \\\"domain_range_violations\\\": 0,\\n52:      \\\"domain_range_violations\\\": 0,\\n57:      \\\"domain_range_violations\\\": 0,\\n62:      \\\"domain_range_violations\\\": 0,\\n67:      \\\"domain_range_violations\\\": 0,\\n72:      \\\"domain_range_violations\\\": 0,\\n77:      \\\"domain_range_violations\\\": 0,\\n82:      \\\"domain_range_violations\\\": 0,\\n87:      \\\"domain_range_violations\\\": 0,\\n92:      \\\"domain_range_violations\\\": 1,\\n97:      \\\"domain_range_violations\\\": 3,\\n102:      \\\"domain_range_violations\\\": 0,\\n107:      \\\"domain_range_violations\\\": 0,\\n112:      \\\"domain_range_violations\\\": 0,\\n117:      \\\"domain_range_violations\\\": 13,\\n122:      \\\"domain_range_violations\\\": 0,\\n127:      \\\"domain_range_violations\\\": 1,\\n132:      \\\"domain_range_violations\\\": 1,\\n137:      \\\"domain_range_violations\\\": 0,\\n142:      \\\"domain_range_violations\\\": 0,\\n147:      \\\"domain_range_violations\\\": 0,\\n152:      \\\"domain_range_violations\\\": 2,\\n157:      \\\"domain_range_violations\\\": 2,\\n162:      \\\"domain_range_violations\\\": 0,\\n167:      \\\"domain_range_violations\\\": 0,\\n172:      \\\"domain_range_violations\\\": 0,\\n177:      \\\"domain_range_violations\\\": 0,\\n182:      \\\"domain_range_violations\\\": 0,\\n187:      \\\"domain_range_violations\\\": 0,\\n192:      \\\"domain_range_violations\\\": 1,\\n197:      \\\"domain_range_violations\\\": 0,\\n202:      \\\"domain_range_violations\\\": 0,\\n207:      \\\"domain_range_violations\\\": 0,\\n212:      \\\"domain_range_violations\\\": 0,\\n217:      \\\"domain_range_violations\\\": 0,\\n222:      \\\"domain_range_violations\\\": 0,\\n227:      \\\"domain_range_violations\\\": 2,\\n232:      \\\"domain_range_violations\\\": 0,\\n237:      \\\"domain_range_violations\\\": 0,\\n242:      \\\"domain_range_violations\\\": 0,\\n247:      \\\"domain_range_violations\\\": 2,\\n252:      \\\"domain_range_violations\\\": 0,\\n257:      \\\"domain_range_violations\\\": 0,\\n262:      \\\"domain_range_violations\\\": 1,\\n267:      \\\"domain_range_violations\\\": 0,\\n272:      \\\"domain_range_violations\\\": 0,\\n277:      \\\"domain_range_violations\\\": 0,\\n282:      \\\"domain_range_violations\\\": 0,\\n287:      \\\"domain_range_violations\\\": 0,\\n292:      \\\"domain_range_violations\\\": 0,\\n297:      \\\"domain_range_violations\\\": 0,\\n302:      \\\"domain_range_violations\\\": 0,\\n307:      \\\"domain_range_violations\\\": 0,\\n312:      \\\"domain_range_violations\\\": 0,\\n317:      \\\"domain_range_violations\\\": 0,\\n322:      \\\"domain_range_violations\\\": 0,\\n327:      \\\"domain_range_violations\\\": 0,\\n332:      \\\"domain_range_violations\\\": 0,\\n337:      \\\"domain_range_violations\\\": 1,\\n342:      \\\"domain_range_violations\\\": 0,\\n347:      \\\"domain_range_violations\\\": 0,\\n352:      \\\"domain_range_violations\\\": 0,\\n357:      \\\"domain_range_violations\\\": 0,\\n362:      \\\"domain_range_violations\\\": 0,\\n367:      \\\"domain_range_violations\\\": 0,\\n372:      \\\"domain_range_violations\\\": 0,\\n377:      \\\"domain_range_violations\\\": 0,\\n382:      \\\"domain_range_violations\\\": 0,\\n387:      \\\"domain_range_violations\\\": 0,\\n392:      \\\"domain_range_violations\\\": 0,\\n397:      \\\"domain_range_violations\\\": 0,\\n402:      \\\"domain_range_violations\\\": 0,\\n407:      \\\"domain_range_violations\\\": 0,\\n412:      \\\"domain_range_violations\\\": 0,\\n417:      \\\"domain_range_violations\\\": 0,\\n422:      \\\"domain_range_violations\\\": 0,\\n427:      \\\"domain_range_violations\\\": 0,\\n432:      \\\"domain_range_violations\\\": 0,\\n437:      \\\"domain_range_violations\\\": 0,\\n442:      \\\"domain_range_violations\\\": 0,\\n447:      \\\"domain_range_violations\\\": 0,\\n452:      \\\"domain_range_violations\\\": 1,\\n457:      \\\"domain_range_violations\\\": 0,\\n462:      \\\"domain_range_violations\\\": 0,\\n467:      \\\"domain_range_violations\\\": 0,\\n472:      \\\"domain_range_violations\\\": 0,\\n477:      \\\"domain_range_violations\\\": 0,\\n482:      \\\"domain_range_violations\\\": 0,\\n487:      \\\"domain_range_violations\\\": 0,\\n492:      \\\"domain_range_violations\\\": 0,\\n497:      \\\"domain_range_violations\\\": 0,\\n502:      \\n\\n... [截断: 输出过长，省略 34557 字符] ...\\n\\n_range_violations\\\": 0,\\n8399:      \\\"domain_range_violations\\\": 0,\\n8408:      \\\"domain_range_violations\\\": 0,\\n8417:      \\\"domain_range_violations\\\": 0,\\n8426:      \\\"domain_range_violations\\\": 0,\\n8435:      \\\"domain_range_violations\\\": 0,\\n8444:      \\\"domain_range_violations\\\": 0,\\n8453:      \\\"domain_range_violations\\\": 0,\\n8462:      \\\"domain_range_violations\\\": 0,\\n8471:      \\\"domain_range_violations\\\": 1,\\n8480:      \\\"domain_range_violations\\\": 0,\\n8489:      \\\"domain_range_violations\\\": 0,\\n8498:      \\\"domain_range_violations\\\": 0,\\n8507:      \\\"domain_range_violations\\\": 0,\\n8516:      \\\"domain_range_violations\\\": 0,\\n8525:      \\\"domain_range_violations\\\": 0,\\n8534:      \\\"domain_range_violations\\\": 0,\\n8543:      \\\"domain_range_violations\\\": 0,\\n8552:      \\\"domain_range_violations\\\": 0,\\n8561:      \\\"domain_range_violations\\\": 0,\\n8570:      \\\"domain_range_violations\\\": 0,\\n8579:      \\\"domain_range_violations\\\": 0,\\n8588:      \\\"domain_range_violations\\\": 0,\\n8597:      \\\"domain_range_violations\\\": 0,\\n8606:      \\\"domain_range_violations\\\": 0,\\n8619:      \\\"domain_range_violations\\\": 0,\\n8632:      \\\"domain_range_violations\\\": 0,\\n8641:      \\\"domain_range_violations\\\": 0,\\n8650:      \\\"domain_range_violations\\\": 0,\\n8659:      \\\"domain_range_violations\\\": 0,\\n8668:      \\\"domain_range_violations\\\": 0,\\n8677:      \\\"domain_range_violations\\\": 0,\\n8686:      \\\"domain_range_violations\\\": 0,\\n8695:      \\\"domain_range_violations\\\": 0,\\n8704:      \\\"domain_range_violations\\\": 0,\\n8713:      \\\"domain_range_violations\\\": 0,\\n8722:      \\\"domain_range_violations\\\": 0,\\n8731:      \\\"domain_range_violations\\\": 0,\\n8740:      \\\"domain_range_violations\\\": 0,\\n8749:      \\\"domain_range_violations\\\": 0,\\n8758:      \\\"domain_range_violations\\\": 0,\\n8767:      \\\"domain_range_violations\\\": 0,\\n8776:      \\\"domain_range_violations\\\": 0,\\n8785:      \\\"domain_range_violations\\\": 0,\\n8794:      \\\"domain_range_violations\\\": 0,\\n8803:      \\\"domain_range_violations\\\": 0,\\n8812:      \\\"domain_range_violations\\\": 0,\\n8821:      \\\"domain_range_violations\\\": 0,\\n8830:      \\\"domain_range_violations\\\": 0,\\n8839:      \\\"domain_range_violations\\\": 0,\\n8848:      \\\"domain_range_violations\\\": 0,\\n8861:      \\\"domain_range_violations\\\": 0,\\n8874:      \\\"domain_range_violations\\\": 0,\\n8883:      \\\"domain_range_violations\\\": 0,\\n8892:      \\\"domain_range_violations\\\": 0,\\n8901:      \\\"domain_range_violations\\\": 0,\\n8910:      \\\"domain_range_violations\\\": 0,\\n8919:      \\\"domain_range_violations\\\": 0,\\n8928:      \\\"domain_range_violations\\\": 0,\\n8937:      \\\"domain_range_violations\\\": 0,\\n8946:      \\\"domain_range_violations\\\": 0,\\n8955:      \\\"domain_range_violations\\\": 0,\\n8964:      \\\"domain_range_violations\\\": 0,\\n8977:      \\\"domain_range_violations\\\": 0,\\n8986:      \\\"domain_range_violations\\\": 0,\\n8995:      \\\"domain_range_violations\\\": 0,\\n9008:      \\\"domain_range_violations\\\": 0,\\n9017:      \\\"domain_range_violations\\\": 0,\\n9026:      \\\"domain_range_violations\\\": 0,\\n9035:      \\\"domain_range_violations\\\": 0,\\n9044:      \\\"domain_range_violations\\\": 0,\\n9053:      \\\"domain_range_violations\\\": 0,\\n9062:      \\\"domain_range_violations\\\": 0,\\n9071:      \\\"domain_range_violations\\\": 0,\\n9080:      \\\"domain_range_violations\\\": 0,\\n9089:      \\\"domain_range_violations\\\": 0,\\n9098:      \\\"domain_range_violations\\\": 0,\\n9107:      \\\"domain_range_violations\\\": 0,\\n9116:      \\\"domain_range_violations\\\": 0,\\n9125:      \\\"domain_range_violations\\\": 0,\\n9134:      \\\"domain_range_violations\\\": 0,\\n9143:      \\\"domain_range_violations\\\": 0,\\n9152:      \\\"domain_range_violations\\\": 0,\\n9161:      \\\"domain_range_violations\\\": 0,\\n9170:      \\\"domain_range_violations\\\": 0,\\n9179:      \\\"domain_range_violations\\\": 0,\\n9188:      \\\"domain_range_violations\\\": 0,\\n9197:      \\\"domain_range_violations\\\": 0,\\n9210:      \\\"domain_range_violations\\\": 0,\\n9219:      \\\"domain_range_violations\\\": 0,\\n9228:      \\\"domain_range_violations\\\": 0,\\n9237:      \\\"domain_range_violations\\\": 0,\\n9246:      \\\"domain_range_violations\\\": 0,\\n9255:      \\\"domain_range_violations\\\": 0,\\n9264:      \\\"domain_range_violations\\\": 0,\\n9273:      \\\"domain_range_violations\\\": 0,\\n9282:      \\\"domain_range_violations\\\": 0,\\n9291:      \\\"domain_range_violations\\\": 0,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-23T11:42:31.669Z_

<details><summary>↩ Tool result · `toolu_01Jg9jQuCoDoKncZa9amoEyx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"15:    \\\"domain_range_violations\\\": 82,\\n16:    \\\"domain_range_violation_rate\\\": 0.0051,\\n22:    \\\"go_nogo_metric_description\\\": \\\"per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)\\\"\\n27:      \\\"domain_range_violations\\\": 1,\\n32:      \\\"domain_range_violations\\\": 0,\\n37:      \\\"domain_range_violations\\\": 8,\\n42:      \\\"domain_range_violations\\\": 0,\\n47:      \\\"domain_range_violations\\\": 1,\\n52:      \\\"domain_range_violations\\\": 0,\\n57:      \\\"domain_range_violations\\\": 1,\\n62:      \\\"domain_range_violations\\\": 1,\\n67:      \\\"domain_range_violations\\\": 0,\\n72:      \\\"domain_range_violations\\\": 0,\\n77:      \\\"domain_range_violations\\\": 16,\\n82:      \\\"domain_range_violations\\\": 0,\\n87:      \\\"domain_range_violations\\\": 0,\\n92:      \\\"domain_range_violations\\\": 1,\\n97:      \\\"domain_range_violations\\\": 2,\\n102:      \\\"domain_range_violations\\\": 0,\\n107:      \\\"domain_range_violations\\\": 3,\\n112:      \\\"domain_range_violations\\\": 0,\\n117:      \\\"domain_range_violations\\\": 0,\\n122:      \\\"domain_range_violations\\\": 0,\\n127:      \\\"domain_range_violations\\\": 1,\\n132:      \\\"domain_range_violations\\\": 1,\\n137:      \\\"domain_range_violations\\\": 0,\\n142:      \\\"domain_range_violations\\\": 0,\\n147:      \\\"domain_range_violations\\\": 0,\\n152:      \\\"domain_range_violations\\\": 1,\\n157:      \\\"domain_range_violations\\\": 4,\\n162:      \\\"domain_range_violations\\\": 0,\\n167:      \\\"domain_range_violations\\\": 0,\\n172:      \\\"domain_range_violations\\\": 2,\\n177:      \\\"domain_range_violations\\\": 0,\\n182:      \\\"domain_range_violations\\\": 1,\\n187:      \\\"domain_range_violations\\\": 0,\\n192:      \\\"domain_range_violations\\\": 1,\\n197:      \\\"domain_range_violations\\\": 0,\\n202:      \\\"domain_range_violations\\\": 0,\\n207:      \\\"domain_range_violations\\\": 1,\\n212:      \\\"domain_range_violations\\\": 0,\\n217:      \\\"domain_range_violations\\\": 0,\\n222:      \\\"domain_range_violations\\\": 0,\\n227:      \\\"domain_range_violations\\\": 0,\\n232:      \\\"domain_range_violations\\\": 2,\\n237:      \\\"domain_range_violations\\\": 0,\\n242:      \\\"domain_range_violations\\\": 0,\\n247:      \\\"domain_range_violations\\\": 0,\\n252:      \\\"domain_range_violations\\\": 0,\\n257:      \\\"domain_range_violations\\\": 0,\\n262:      \\\"domain_range_violations\\\": 1,\\n267:      \\\"domain_range_violations\\\": 2,\\n272:      \\\"domain_range_violations\\\": 0,\\n277:      \\\"domain_range_violations\\\": 4,\\n282:      \\\"domain_range_violations\\\": 0,\\n287:      \\\"domain_range_violations\\\": 0,\\n292:      \\\"domain_range_violations\\\": 0,\\n297:      \\\"domain_range_violations\\\": 0,\\n302:      \\\"domain_range_violations\\\": 8,\\n307:      \\\"domain_range_violations\\\": 2,\\n312:      \\\"domain_range_violations\\\": 0,\\n317:      \\\"domain_range_violations\\\": 0,\\n322:      \\\"domain_range_violations\\\": 0,\\n327:      \\\"domain_range_violations\\\": 0,\\n332:      \\\"domain_range_violations\\\": 0,\\n337:      \\\"domain_range_violations\\\": 0,\\n342:      \\\"domain_range_violations\\\": 0,\\n347:      \\\"domain_range_violations\\\": 1,\\n352:      \\\"domain_range_violations\\\": 2,\\n357:      \\\"domain_range_violations\\\": 0,\\n362:      \\\"domain_range_violations\\\": 0,\\n367:      \\\"domain_range_violations\\\": 0,\\n372:      \\\"domain_range_violations\\\": 1,\\n377:      \\\"domain_range_violations\\\": 0,\\n382:      \\\"domain_range_violations\\\": 0,\\n387:      \\\"domain_range_violations\\\": 0,\\n392:      \\\"domain_range_violations\\\": 0,\\n397:      \\\"domain_range_violations\\\": 0,\\n402:      \\\"domain_range_violations\\\": 0,\\n407:      \\\"domain_range_violations\\\": 0,\\n412:      \\\"domain_range_violations\\\": 0,\\n417:      \\\"domain_range_violations\\\": 1,\\n422:      \\\"domain_range_violations\\\": 2,\\n427:      \\\"domain_range_violations\\\": 0,\\n432:      \\\"domain_range_violations\\\": 0,\\n437:      \\\"domain_range_violations\\\": 0,\\n442:      \\\"domain_range_violations\\\": 0,\\n447:      \\\"domain_range_violations\\\": 0,\\n452:      \\\"domain_range_violations\\\": 0,\\n457:      \\\"domain_range_violations\\\": 4,\\n462:      \\\"domain_range_violations\\\": 0,\\n467:      \\\"domain_range_violations\\\": 2,\\n472:      \\\"domain_range_violations\\\": 0,\\n477:      \\\"domain_range_violations\\\": 1,\\n482:      \\\"domain_range_violations\\\": 0,\\n487:      \\\"domain_range_violations\\\": 0,\\n492:      \\\"domain_range_violations\\\": 0,\\n497:      \\\"domain_range_violations\\\": 3,\\n504:    \\\"d\\n\\n... [截断: 输出过长，省略 35955 字符] ...\\n\\n_range_violations\\\": 0,\\n8548:      \\\"domain_range_violations\\\": 0,\\n8557:      \\\"domain_range_violations\\\": 0,\\n8566:      \\\"domain_range_violations\\\": 0,\\n8575:      \\\"domain_range_violations\\\": 0,\\n8584:      \\\"domain_range_violations\\\": 0,\\n8593:      \\\"domain_range_violations\\\": 1,\\n8606:      \\\"domain_range_violations\\\": 0,\\n8615:      \\\"domain_range_violations\\\": 0,\\n8624:      \\\"domain_range_violations\\\": 0,\\n8637:      \\\"domain_range_violations\\\": 0,\\n8646:      \\\"domain_range_violations\\\": 0,\\n8655:      \\\"domain_range_violations\\\": 0,\\n8664:      \\\"domain_range_violations\\\": 0,\\n8673:      \\\"domain_range_violations\\\": 0,\\n8682:      \\\"domain_range_violations\\\": 0,\\n8691:      \\\"domain_range_violations\\\": 0,\\n8700:      \\\"domain_range_violations\\\": 0,\\n8709:      \\\"domain_range_violations\\\": 0,\\n8718:      \\\"domain_range_violations\\\": 0,\\n8727:      \\\"domain_range_violations\\\": 0,\\n8736:      \\\"domain_range_violations\\\": 0,\\n8745:      \\\"domain_range_violations\\\": 0,\\n8754:      \\\"domain_range_violations\\\": 0,\\n8763:      \\\"domain_range_violations\\\": 0,\\n8772:      \\\"domain_range_violations\\\": 0,\\n8781:      \\\"domain_range_violations\\\": 0,\\n8790:      \\\"domain_range_violations\\\": 0,\\n8799:      \\\"domain_range_violations\\\": 0,\\n8808:      \\\"domain_range_violations\\\": 0,\\n8817:      \\\"domain_range_violations\\\": 0,\\n8826:      \\\"domain_range_violations\\\": 0,\\n8839:      \\\"domain_range_violations\\\": 0,\\n8848:      \\\"domain_range_violations\\\": 0,\\n8857:      \\\"domain_range_violations\\\": 1,\\n8866:      \\\"domain_range_violations\\\": 0,\\n8875:      \\\"domain_range_violations\\\": 0,\\n8884:      \\\"domain_range_violations\\\": 0,\\n8893:      \\\"domain_range_violations\\\": 0,\\n8902:      \\\"domain_range_violations\\\": 0,\\n8911:      \\\"domain_range_violations\\\": 0,\\n8920:      \\\"domain_range_violations\\\": 0,\\n8929:      \\\"domain_range_violations\\\": 0,\\n8938:      \\\"domain_range_violations\\\": 0,\\n8947:      \\\"domain_range_violations\\\": 0,\\n8956:      \\\"domain_range_violations\\\": 0,\\n8965:      \\\"domain_range_violations\\\": 0,\\n8974:      \\\"domain_range_violations\\\": 0,\\n8983:      \\\"domain_range_violations\\\": 0,\\n8996:      \\\"domain_range_violations\\\": 0,\\n9005:      \\\"domain_range_violations\\\": 0,\\n9014:      \\\"domain_range_violations\\\": 0,\\n9023:      \\\"domain_range_violations\\\": 0,\\n9032:      \\\"domain_range_violations\\\": 0,\\n9041:      \\\"domain_range_violations\\\": 0,\\n9050:      \\\"domain_range_violations\\\": 0,\\n9059:      \\\"domain_range_violations\\\": 0,\\n9068:      \\\"domain_range_violations\\\": 0,\\n9077:      \\\"domain_range_violations\\\": 0,\\n9086:      \\\"domain_range_violations\\\": 0,\\n9095:      \\\"domain_range_violations\\\": 0,\\n9104:      \\\"domain_range_violations\\\": 0,\\n9113:      \\\"domain_range_violations\\\": 0,\\n9122:      \\\"domain_range_violations\\\": 0,\\n9131:      \\\"domain_range_violations\\\": 0,\\n9140:      \\\"domain_range_violations\\\": 0,\\n9149:      \\\"domain_range_violations\\\": 0,\\n9158:      \\\"domain_range_violations\\\": 0,\\n9167:      \\\"domain_range_violations\\\": 0,\\n9176:      \\\"domain_range_violations\\\": 0,\\n9185:      \\\"domain_range_violations\\\": 0,\\n9194:      \\\"domain_range_violations\\\": 0,\\n9203:      \\\"domain_range_violations\\\": 0,\\n9212:      \\\"domain_range_violations\\\": 0,\\n9221:      \\\"domain_range_violations\\\": 0,\\n9230:      \\\"domain_range_violations\\\": 0,\\n9239:      \\\"domain_range_violations\\\": 0,\\n9248:      \\\"domain_range_violations\\\": 0,\\n9257:      \\\"domain_range_violations\\\": 0,\\n9266:      \\\"domain_range_violations\\\": 0,\\n9275:      \\\"domain_range_violations\\\": 0,\\n9284:      \\\"domain_range_violations\\\": 3,\\n9293:      \\\"domain_range_violations\\\": 0,\\n9302:      \\\"domain_range_violations\\\": 0,\\n9311:      \\\"domain_range_violations\\\": 0,\\n9320:      \\\"domain_range_violations\\\": 0,\\n9329:      \\\"domain_range_violations\\\": 0,\\n9338:      \\\"domain_range_violations\\\": 0,\\n9347:      \\\"domain_range_violations\\\": 0,\\n9356:      \\\"domain_range_violations\\\": 0,\\n9365:      \\\"domain_range_violations\\\": 0,\\n9374:      \\\"domain_range_violations\\\": 0,\\n9383:      \\\"domain_range_violations\\\": 0,\\n9392:      \\\"domain_range_violations\\\": 0,\\n9401:      \\\"domain_range_violations\\\": 0,\\n9410:      \\\"domain_range_violations\\\": 0,\\n9419:      \\\"domain_range_violations\\\": 0,\\n9428:      \\\"domain_range_violations\\\": 0,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "a537c46d-8ea5-439d-a1eb-cf1c89cd233c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"15:    \\\\\\\"domain_range_violations\\\\\\\": 82,\\\\n16:    \\\\\\\"domain_range_violation_rate\\\\\\\": 0.0051,\\\\n22:    \\\\\\\"go_nogo_metric_description\\\\\\\": \\\\\\\"per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)\\\\\\\"\\\\n27:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n32:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n37:      \\\\\\\"domain_range_violations\\\\\\\": 8,\\\\n42:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n47:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n52:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n57:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n62:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n67:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n72:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n77:      \\\\\\\"domain_range_violations\\\\\\\": 16,\\\\n82:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n87:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n92:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n97:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n102:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n107:      \\\\\\\"domain_range_violations\\\\\\\": 3,\\\\n112:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n117:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n122:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n127:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n132:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n137:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n142:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n147:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n152:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n157:      \\\\\\\"domain_range_violations\\\\\\\": 4,\\\\n162:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n167:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n172:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n177:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n182:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n187:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n192:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n197:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n202:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n207:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n212:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n217:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n222:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n227:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n232:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n237:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n242:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n247:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n252:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n257:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n262:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n267:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n272:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n277:      \\\\\\\"domain_range_violations\\\\\\\": 4,\\\\n282:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n287:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n292:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n297:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n302:      \\\\\\\"domain_range_violations\\\\\\\": 8,\\\\n307:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n312:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n317:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n322:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n327:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n332:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n337:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n342:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n347:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n352:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n357:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n362:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n367:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n372:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n377:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n382:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n387:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n392:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n397:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n402:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n407:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n412:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n417:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n422:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n427:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n432:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n437:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n442:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n447:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n452:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n457:      \\\\\\\"domain_range_violations\\\\\\\": 4,\\\\n462:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n467:      \\\\\\\"domain_range_violations\\\\\\\": 2,\\\\n472:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n477:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n482:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n487:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n492:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n497:      \\\\\\\"domain_range_violations\\\\\\\": 3,\\\\n504:    \\\\\\\"d\\\\n\\\\n... [截断: 输出过长，省略 35955 字符] ...\\\\n\\\\n_range_violations\\\\\\\": 0,\\\\n8548:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8557:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8566:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8575:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8584:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8593:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n8606:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8615:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8624:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8637:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8646:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8655:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8664:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8673:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8682:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8691:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8700:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8709:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8718:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8727:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8736:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8745:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8754:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8763:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8772:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8781:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8790:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8799:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8808:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8817:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8826:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8839:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8848:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8857:      \\\\\\\"domain_range_violations\\\\\\\": 1,\\\\n8866:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8875:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8884:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8893:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8902:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8911:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8920:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8929:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8938:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8947:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8956:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8965:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8974:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8983:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n8996:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9005:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9014:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9023:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9032:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9041:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9050:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9059:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9068:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9077:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9086:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9095:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9104:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9113:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9122:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9131:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9140:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9149:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9158:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9167:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9176:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9185:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9194:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9203:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9212:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9221:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9230:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9239:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9248:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9257:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9266:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9275:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9284:      \\\\\\\"domain_range_violations\\\\\\\": 3,\\\\n9293:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9302:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9311:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9320:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9329:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9338:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9347:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9356:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9365:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9374:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9383:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9392:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9401:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9410:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9419:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n9428:      \\\\\\\"domain_range_violations\\\\\\\": 0,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"15:    \\\"domain_range_violations\\\": 82,\\n16:    \\\"domain_range_violation_rate\\\": 0.0051,\\n22:    \\\"go_nogo_metric_description\\\": \\\"per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)\\\"\\n27:      \\\"domain_range_violations\\\": 1,\\n32:      \\\"domain_range_violations\\\": 0,\\n37:      \\\"domain_range_violations\\\": 8,\\n42:      \\\"domain_range_violations\\\": 0,\\n47:      \\\"domain_range_violations\\\": 1,\\n52:      \\\"domain_range_violations\\\": 0,\\n57:      \\\"domain_range_violations\\\": 1,\\n62:      \\\"domain_range_violations\\\": 1,\\n67:      \\\"domain_range_violations\\\": 0,\\n72:      \\\"domain_range_violations\\\": 0,\\n77:      \\\"domain_range_violations\\\": 16,\\n82:      \\\"domain_range_violations\\\": 0,\\n87:      \\\"domain_range_violations\\\": 0,\\n92:      \\\"domain_range_violations\\\": 1,\\n97:      \\\"domain_range_violations\\\": 2,\\n102:      \\\"domain_range_violations\\\": 0,\\n107:      \\\"domain_range_violations\\\": 3,\\n112:      \\\"domain_range_violations\\\": 0,\\n117:      \\\"domain_range_violations\\\": 0,\\n122:      \\\"domain_range_violations\\\": 0,\\n127:      \\\"domain_range_violations\\\": 1,\\n132:      \\\"domain_range_violations\\\": 1,\\n137:      \\\"domain_range_violations\\\": 0,\\n142:      \\\"domain_range_violations\\\": 0,\\n147:      \\\"domain_range_violations\\\": 0,\\n152:      \\\"domain_range_violations\\\": 1,\\n157:      \\\"domain_range_violations\\\": 4,\\n162:      \\\"domain_range_violations\\\": 0,\\n167:      \\\"domain_range_violations\\\": 0,\\n172:      \\\"domain_range_violations\\\": 2,\\n177:      \\\"domain_range_violations\\\": 0,\\n182:      \\\"domain_range_violations\\\": 1,\\n187:      \\\"domain_range_violations\\\": 0,\\n192:      \\\"domain_range_violations\\\": 1,\\n197:      \\\"domain_range_violations\\\": 0,\\n202:      \\\"domain_range_violations\\\": 0,\\n207:      \\\"domain_range_violations\\\": 1,\\n212:      \\\"domain_range_violations\\\": 0,\\n217:      \\\"domain_range_violations\\\": 0,\\n222:      \\\"domain_range_violations\\\": 0,\\n227:      \\\"domain_range_violations\\\": 0,\\n232:      \\\"domain_range_violations\\\": 2,\\n237:      \\\"domain_range_violations\\\": 0,\\n242:      \\\"domain_range_violations\\\": 0,\\n247:      \\\"domain_range_violations\\\": 0,\\n252:      \\\"domain_range_violations\\\": 0,\\n257:      \\\"domain_range_violations\\\": 0,\\n262:      \\\"domain_range_violations\\\": 1,\\n267:      \\\"domain_range_violations\\\": 2,\\n272:      \\\"domain_range_violations\\\": 0,\\n277:      \\\"domain_range_violations\\\": 4,\\n282:      \\\"domain_range_violations\\\": 0,\\n287:      \\\"domain_range_violations\\\": 0,\\n292:      \\\"domain_range_violations\\\": 0,\\n297:      \\\"domain_range_violations\\\": 0,\\n302:      \\\"domain_range_violations\\\": 8,\\n307:      \\\"domain_range_violations\\\": 2,\\n312:      \\\"domain_range_violations\\\": 0,\\n317:      \\\"domain_range_violations\\\": 0,\\n322:      \\\"domain_range_violations\\\": 0,\\n327:      \\\"domain_range_violations\\\": 0,\\n332:      \\\"domain_range_violations\\\": 0,\\n337:      \\\"domain_range_violations\\\": 0,\\n342:      \\\"domain_range_violations\\\": 0,\\n347:      \\\"domain_range_violations\\\": 1,\\n352:      \\\"domain_range_violations\\\": 2,\\n357:      \\\"domain_range_violations\\\": 0,\\n362:      \\\"domain_range_violations\\\": 0,\\n367:      \\\"domain_range_violations\\\": 0,\\n372:      \\\"domain_range_violations\\\": 1,\\n377:      \\\"domain_range_violations\\\": 0,\\n382:      \\\"domain_range_violations\\\": 0,\\n387:      \\\"domain_range_violations\\\": 0,\\n392:      \\\"domain_range_violations\\\": 0,\\n397:      \\\"domain_range_violations\\\": 0,\\n402:      \\\"domain_range_violations\\\": 0,\\n407:      \\\"domain_range_violations\\\": 0,\\n412:      \\\"domain_range_violations\\\": 0,\\n417:      \\\"domain_range_violations\\\": 1,\\n422:      \\\"domain_range_violations\\\": 2,\\n427:      \\\"domain_range_violations\\\": 0,\\n432:      \\\"domain_range_violations\\\": 0,\\n437:      \\\"domain_range_violations\\\": 0,\\n442:      \\\"domain_range_violations\\\": 0,\\n447:      \\\"domain_range_violations\\\": 0,\\n452:      \\\"domain_range_violations\\\": 0,\\n457:      \\\"domain_range_violations\\\": 4,\\n462:      \\\"domain_range_violations\\\": 0,\\n467:      \\\"domain_range_violations\\\": 2,\\n472:      \\\"domain_range_violations\\\": 0,\\n477:      \\\"domain_range_violations\\\": 1,\\n482:      \\\"domain_range_violations\\\": 0,\\n487:      \\\"domain_range_violations\\\": 0,\\n492:      \\\"domain_range_violations\\\": 0,\\n497:      \\\"domain_range_violations\\\": 3,\\n504:    \\\"d\\n\\n... [截断: 输出过长，省略 35955 字符] ...\\n\\n_range_violations\\\": 0,\\n8548:      \\\"domain_range_violations\\\": 0,\\n8557:      \\\"domain_range_violations\\\": 0,\\n8566:      \\\"domain_range_violations\\\": 0,\\n8575:      \\\"domain_range_violations\\\": 0,\\n8584:      \\\"domain_range_violations\\\": 0,\\n8593:      \\\"domain_range_violations\\\": 1,\\n8606:      \\\"domain_range_violations\\\": 0,\\n8615:      \\\"domain_range_violations\\\": 0,\\n8624:      \\\"domain_range_violations\\\": 0,\\n8637:      \\\"domain_range_violations\\\": 0,\\n8646:      \\\"domain_range_violations\\\": 0,\\n8655:      \\\"domain_range_violations\\\": 0,\\n8664:      \\\"domain_range_violations\\\": 0,\\n8673:      \\\"domain_range_violations\\\": 0,\\n8682:      \\\"domain_range_violations\\\": 0,\\n8691:      \\\"domain_range_violations\\\": 0,\\n8700:      \\\"domain_range_violations\\\": 0,\\n8709:      \\\"domain_range_violations\\\": 0,\\n8718:      \\\"domain_range_violations\\\": 0,\\n8727:      \\\"domain_range_violations\\\": 0,\\n8736:      \\\"domain_range_violations\\\": 0,\\n8745:      \\\"domain_range_violations\\\": 0,\\n8754:      \\\"domain_range_violations\\\": 0,\\n8763:      \\\"domain_range_violations\\\": 0,\\n8772:      \\\"domain_range_violations\\\": 0,\\n8781:      \\\"domain_range_violations\\\": 0,\\n8790:      \\\"domain_range_violations\\\": 0,\\n8799:      \\\"domain_range_violations\\\": 0,\\n8808:      \\\"domain_range_violations\\\": 0,\\n8817:      \\\"domain_range_violations\\\": 0,\\n8826:      \\\"domain_range_violations\\\": 0,\\n8839:      \\\"domain_range_violations\\\": 0,\\n8848:      \\\"domain_range_violations\\\": 0,\\n8857:      \\\"domain_range_violations\\\": 1,\\n8866:      \\\"domain_range_violations\\\": 0,\\n8875:      \\\"domain_range_violations\\\": 0,\\n8884:      \\\"domain_range_violations\\\": 0,\\n8893:      \\\"domain_range_violations\\\": 0,\\n8902:      \\\"domain_range_violations\\\": 0,\\n8911:      \\\"domain_range_violations\\\": 0,\\n8920:      \\\"domain_range_violations\\\": 0,\\n8929:      \\\"domain_range_violations\\\": 0,\\n8938:      \\\"domain_range_violations\\\": 0,\\n8947:      \\\"domain_range_violations\\\": 0,\\n8956:      \\\"domain_range_violations\\\": 0,\\n8965:      \\\"domain_range_violations\\\": 0,\\n8974:      \\\"domain_range_violations\\\": 0,\\n8983:      \\\"domain_range_violations\\\": 0,\\n8996:      \\\"domain_range_violations\\\": 0,\\n9005:      \\\"domain_range_violations\\\": 0,\\n9014:      \\\"domain_range_violations\\\": 0,\\n9023:      \\\"domain_range_violations\\\": 0,\\n9032:      \\\"domain_range_violations\\\": 0,\\n9041:      \\\"domain_range_violations\\\": 0,\\n9050:      \\\"domain_range_violations\\\": 0,\\n9059:      \\\"domain_range_violations\\\": 0,\\n9068:      \\\"domain_range_violations\\\": 0,\\n9077:      \\\"domain_range_violations\\\": 0,\\n9086:      \\\"domain_range_violations\\\": 0,\\n9095:      \\\"domain_range_violations\\\": 0,\\n9104:      \\\"domain_range_violations\\\": 0,\\n9113:      \\\"domain_range_violations\\\": 0,\\n9122:      \\\"domain_range_violations\\\": 0,\\n9131:      \\\"domain_range_violations\\\": 0,\\n9140:      \\\"domain_range_violations\\\": 0,\\n9149:      \\\"domain_range_violations\\\": 0,\\n9158:      \\\"domain_range_violations\\\": 0,\\n9167:      \\\"domain_range_violations\\\": 0,\\n9176:      \\\"domain_range_violations\\\": 0,\\n9185:      \\\"domain_range_violations\\\": 0,\\n9194:      \\\"domain_range_violations\\\": 0,\\n9203:      \\\"domain_range_violations\\\": 0,\\n9212:      \\\"domain_range_violations\\\": 0,\\n9221:      \\\"domain_range_violations\\\": 0,\\n9230:      \\\"domain_range_violations\\\": 0,\\n9239:      \\\"domain_range_violations\\\": 0,\\n9248:      \\\"domain_range_violations\\\": 0,\\n9257:      \\\"domain_range_violations\\\": 0,\\n9266:      \\\"domain_range_violations\\\": 0,\\n9275:      \\\"domain_range_violations\\\": 0,\\n9284:      \\\"domain_range_violations\\\": 3,\\n9293:      \\\"domain_range_violations\\\": 0,\\n9302:      \\\"domain_range_violations\\\": 0,\\n9311:      \\\"domain_range_violations\\\": 0,\\n9320:      \\\"domain_range_violations\\\": 0,\\n9329:      \\\"domain_range_violations\\\": 0,\\n9338:      \\\"domain_range_violations\\\": 0,\\n9347:      \\\"domain_range_violations\\\": 0,\\n9356:      \\\"domain_range_violations\\\": 0,\\n9365:      \\\"domain_range_violations\\\": 0,\\n9374:      \\\"domain_range_violations\\\": 0,\\n9383:      \\\"domain_range_violations\\\": 0,\\n9392:      \\\"domain_range_violations\\\": 0,\\n9401:      \\\"domain_range_violations\\\": 0,\\n9410:      \\\"domain_range_violations\\\": 0,\\n9419:      \\\"domain_range_violations\\\": 0,\\n9428:      \\\"domain_range_violations\\\": 0,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
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
Now I have all 3 results confirmed. Let me also check the unconstrained baselines. The task says "Qwen=0.76%, Llama=0.49%" are verified in registry. But let me also run the checker on the unconstrained FT outputs to get the exact DR numbers from the same checker version, for consistency.

Actually, looking at the posthoc reports:
- Qwen FT unconstrained: domain_range triples_removed = 121 out of total_triples_before = 15869 → 121/15869 = 0.7626%


- Llama FT unconstrained: domain_range triples_removed = 80 out of total_triples_before = 16171 → 80/16171 = 0.4946%

But I need to be careful here—the posthoc reports come from a different filtering script, not violation_checker_docred.py, so they might use different logic for counting violations.

Let me focus on what the evaluation script actually reports. I should run the violation checker on the unconstrained FT outputs to get a proper baseline for comparison. Looking at the file list, I see the posthoc filtered outputs exist, but I need to check whether the raw unconstrained FT outputs are available separately. Looking at the file listing, I don't see an explicit unconstrained output file—just the posthoc-filtered versions and the ablation variants. The original unfiltered FT output must be stored elsewhere, so I need to track down where that's located to run it through the violation checker.

The task mentions unconstrained DR baselines of 0.76% for Qwen and 0.49% for Llama that are supposedly verified in the registry, but when I search through the registry entries I can find, I'm only seeing the fully constrained S1 experiments with 0% DR. I need to search more broadly across all 164 experiments to locate the actual unconstrained baseline results.

Wait, I'm realizing the posthoc reports actually contain the answer — they show violation counts from the unconstrained FT output before any filtering is applied, which gives exactly 0.76% for Qwen and 0.49% for Llama. These match the task's baseline numbers perfectly, so the unconstrained DR must be computed from the posthoc report's input state. For a proper comparison, I should run the unconstrained FT outputs through the violation checker to maintain consistency, though I'm not sure if those files exist as separate artifacts since the posthoc script takes the unconstrained output as its input.

Rather than chase down every file, let me work with what I have. Looking at my recalculated results, most experiments are tracking close to the paper's reported numbers, but the Llama semantic-only constraint shows a notable deviation of +0.18 percentage points that I need to investigate.

The discrepancy comes down to 77 violations in my calculation versus the 48 violations that would be needed to match the paper's 0.30% rate. This 29-violation gap suggests the checker version used here—which includes fixes applied on May 14—is catching more violations than whatever was used originally, likely because the updated version is more thorough in detecting constraint violations.

I need to account for the possibility that the paper's 0.30% might be an undercount, or that the posthoc report method and violation_checker approach are fundamentally different in how they count violations. Looking at the full picture: Qwen semantic is nearly aligned at 0.19% versus 0.21%, Llama grammar matches exactly at 0.51%, but Llama semantic shows this larger 0.18 percentage point gap. Let me now calculate the actual DR reduction using the recalculated values to see if the overall pattern still holds.

The Qwen semantic reduction comes out to 75%, but the Llama semantic reduction drops dramatically to just 2% with the corrected 0.48% violation rate—that's a massive discrepancy from the paper's claimed 39%. I need to verify whether the unconstrained baselines I'm using are actually correct, since I don't see separate unconstrained output files. The posthoc reports show the breakdown before filtering, so I should check whether there are additional output files I'm missing or if I need to reconsider how the baseline numbers were derived. I'll trust the registry values for the unconstrained baselines and use those to calculate the DR reduction against my recalculated semantic and grammar-only metrics. Let me verify by running the violation checker on the unconstrained outputs directly to ensure everything's consistent.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "590fa877-dcb9-47c2-b644-97d0d4b356a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CdVu5CDyuk24gqjKzeVyo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14230,
      "cache_read_input_tokens": 44163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14230
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

_source line 68_

Llama semantic 有显著偏差：0.48% vs 论文的 0.30%。需要确认 unconstrained 基线一致性。检查是否有 unconstrained FT 输出文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "70650825-8e23-4745-95e6-ab455ed7bdae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CdVu5CDyuk24gqjKzeVyo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14230,
      "cache_read_input_tokens": 44163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14230
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

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UCKva2S2tt8RFUNg4WTNDm`</summary>

```json
{
  "server": "westd-16980",
  "command": "ls -la /root/schema_semantic_constrained_ie/outputs/w8_*docred*unconstrained* /root/schema_semantic_constrained_ie/outputs/w8_*docred*full* /root/schema_semantic_constrained_ie/outputs/w8_*docred*baseline*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "9c4b7ab0-0f59-495e-91ea-a0c263eb1a2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CdVu5CDyuk24gqjKzeVyo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14230,
      "cache_read_input_tokens": 44163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14230
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

_source line 70_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013BBh75TYUknZZn3HbuMAEm`</summary>

```json
{
  "server": "westd-16980",
  "command": "head -5 /tmp/vr_llama_semantic.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "845136b4-89a5-4a17-900f-89b4c72a2883",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CdVu5CDyuk24gqjKzeVyo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14230,
      "cache_read_input_tokens": 44163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14230
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

_source line 71 · 2026-05-23T11:43:30.248Z_

<details><summary>↩ Tool result · `toolu_01UCKva2S2tt8RFUNg4WTNDm`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/schema_semantic_constrained_ie/outputs/w8_*docred*unconstrained*': No such file or directory\\nls: cannot access '/root/schema_semantic_constrained_ie/outputs/w8_*docred*full*': No such file or directory\\nls: cannot access '/root/schema_semantic_constrained_ie/outputs/w8_*docred*baseline*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "4db54b82-2aa5-4fb7-ab60-3ae6c1410ea5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/schema_semantic_constrained_ie/outputs/w8_*docred*unconstrained*': No such file or directory\\\\nls: cannot access '/root/schema_semantic_constrained_ie/outputs/w8_*docred*full*': No such file or directory\\\\nls: cannot access '/root/schema_semantic_constrained_ie/outputs/w8_*docred*baseline*': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/schema_semantic_constrained_ie/outputs/w8_*docred*unconstrained*': No such file or directory\\nls: cannot access '/root/schema_semantic_constrained_ie/outputs/w8_*docred*full*': No such file or directory\\nls: cannot access '/root/schema_semantic_constrained_ie/outputs/w8_*docred*baseline*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-23T11:43:30.776Z_

<details><summary>↩ Tool result · `toolu_013BBh75TYUknZZn3HbuMAEm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\",\\n    \\\"total_documents\\\": 998,\\n    \\\"documents_checked\\\": 974,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "7e75644b-0527-4894-8c51-35ebf5066f62",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"summary\\\\\\\": {\\\\n    \\\\\\\"checker_version\\\\\\\": \\\\\\\"fixed_20260514_v2 (strip + alias + unique_et)\\\\\\\",\\\\n    \\\\\\\"total_documents\\\\\\\": 998,\\\\n    \\\\\\\"documents_checked\\\\\\\": 974,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"checker_version\\\": \\\"fixed_20260514_v2 (strip + alias + unique_et)\\\",\\n    \\\"total_documents\\\": 998,\\n    \\\"documents_checked\\\": 974,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 73_

<details><summary>Logged reasoning block</summary>

```text
No unconstrained FT output files. The posthoc report was generated from a different pipeline, and I can't directly run violation_checker_docred.py on the unconstrained output because those files don't exist on disk.

But wait, I need to make sure the unconstrained baselines are consistent. Let me check if the posthoc report's DR counting logic matches violation_checker_docred.py's logic. The posthoc report shows:
- Qwen: 121 DR triples removed out of 15869 total = 0.76%
- Llama: 80 DR triples removed out of 16171 total = 0.49%


These percentages come from the posthoc filtering script, which might be using a different version of the checker or different logic than what I have access to. But the key insight is that the paper's claimed "39-72% DR reduction" with semantic-only constraints comes from comparing unconstrained to semantic-constrained rates: Qwen shows a 72.4% reduction (from 0.76% to 0.21%) and Llama shows a 38.8% reduction (from 0.49% to 0.30%), which matches that range.

However, when I recalculate with the updated values from the fixed checker version, the numbers shift dramatically—Qwen goes to 75% reduction but Llama drops to just 2%, which completely contradicts the paper's claim. This suggests either the original paper used different computation logic or the fixed checker version is revealing an error in their methodology. I need to determine whether the "fixed_20260514_v2" version is actually correct or if something else is happening with how the constraints were applied.

Looking at the file structure more carefully, the posthoc files appear to be separate from the ablation outputs—they're post-filtered versions of the full constrained models, while the ablation files specifically isolate semantic-only or grammar-only constraints.

The real issue is that the unconstrained baseline (0.76% and 0.49%) came from the posthoc script's internal counting method, but I'm now computing ablation violation rates using a different checker script. If these two scripts count violations differently, the comparison becomes unreliable. I should report these findings while flagging this methodological inconsistency and noting the significant discrepancy in the Llama semantic-only results.

Let me verify whether the posthoc script is available and how it actually counts DR violations, or search the registry more carefully for the unconstrained FT experiment results that should already be documented there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "40059ec4-cc69-464d-8be6-1404db543932",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TTFvzvmCTmxwsCxKodggAo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3361,
      "cache_read_input_tokens": 58393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3361
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

_source line 74_

没有 unconstrained FT 输出文件。需要确认 unconstrained 基线来源。查 registry 中 unconstrained FT DocRED 实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "7fff3991-deed-4ee5-a4c2-2361a32ffc04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TTFvzvmCTmxwsCxKodggAo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3361,
      "cache_read_input_tokens": 58393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3361
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

_source line 75_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_012NHa4vkJnThZa7PAobFDPh`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
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
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "9d3896e2-bc3f-4afb-8d38-966ebd396b26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TTFvzvmCTmxwsCxKodggAo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3361,
      "cache_read_input_tokens": 58393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3361
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

_source line 76 · 2026-05-23T11:43:58.236Z_

<details><summary>↩ Tool result · `toolu_012NHa4vkJnThZa7PAobFDPh`</summary>

```text
Error: result (64,490 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/301ce757-b612-46ff-a757-67ed2e0aceb1/tool-results/mcp-agent-ml-research-read_registry-1779536638218.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/301ce757-b612-46ff-a757-67ed2e0aceb1/tool-results/mcp-agent-ml-research-read_registry-1779536638218.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "2d244e7b-5984-4d2f-b515-7ca1dec85566",
  "tool_use_result": {
    "content": "Error: result (64,490 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/301ce757-b612-46ff-a757-67ed2e0aceb1/tool-results/mcp-agent-ml-research-read_registry-1779536638218.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/301ce757-b612-46ff-a757-67ed2e0aceb1/tool-results/mcp-agent-ml-research-read_registry-1779536638218.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"sf2_70b_prompt_sensitivity\": {\"metrics\": {\"minimal_con\": {\"E_F1\": 37.22, \"R_F1\": 11.35, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.62}, \"minimal_unc\": {\"E_F1\": 37.51, \"R_F1\": 13.42, \"ET_pct\": 0.27, \"RV_pct\": 5.88, \"DR_pct\": 0.22, \"CF_pct\": 0}, \"detailed_con\": {\"E_F1\": 40.35, \"R_F1\": 11.16, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.75}, \"detailed_unc\": {\"E_F1\": 40.42, \"R_F1\": 11.12, \"ET_pct\": 0, \"RV_pct\": 0.26, \"DR_pct\": 4.57, \"CF_pct\": 0}}}, \"eval_70b_lora_docred_200_full_s2\": {\"metrics\": {\"R_F1\": 36.45, \"R_P\": 31.25, \"R_R\": 43.72, \"E_F1\": 84.96, \"E_P\": 84.6, \"E_R\": 85.34, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 13, \"CF_pct\": 0.34, \"parse_fail_pct\": 0, \"pred_entities\": 3819, \"pred_relations\": 3546, \"entity_tp\": 3218, \"entity_fp\": 586, \"entity_fn\": 553, \"relation_tp\": 1104, \"relation_fp\": 2429, \"relation_fn\": 1421}}, \"sf2_qwen_int4_docred_s1\": {\"metrics\": {\"total_samples\": 200, \"parse_failures\": 37, \"parse_fail_pct\": 18.5, \"total_entities_pred\": 2985, \"total_relations_pred\": 2385, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.1, \"E_P\": 84.87, \"E_R\": 66.93, \"E_F1\": 74.84, \"R_P\": 41.59, \"R_R\": 38.65, \"R_F1\": 40.07, \"et_violations\": 0, \"rv_violations\": 0, \"dr_violations\": 0, \"cf_violations\": 3}}, \"sf2_llama_int4_docred_s1\": {\"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.22, \"R-F1\": 48.04, \"E-F1\": 84.18, \"R-P\": 44.79, \"R-R\": 51.8, \"E-P\": 85.5, \"E-R\": 82.9, \"samples\": 200, \"parse_fail\": 5, \"parse_fail_pct\": 2.5, \"entities_pred\": 3669, \"relations_pred\": 2997}}, \"sf2_llama_int4_scierc_s1\": {\"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}}, \"sf2_qwen_int4_scierc_s1\": {\"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}}, \"sf2_gollie_scierc_violation\": {\"metrics\": {\"GoLLIE_ZS\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.83, \"E_F1\": 9.17, \"R_F1\": 0, \"pred_ents\": 241, \"pred_rels\": 5, \"docs_with_output\": 54}, \"OntoCoDec_Qwen_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.61, \"E_F1\": 66.43, \"R_F1\": 43.69}, \"OntoCoDec_Llama_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.62, \"E_F1\": 67.09, \"R_F1\": 45.47}}}, \"eval_70b_zs_docred_200_full_s1\": {\"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 5.34, \"E-F1\": 70.05, \"R-F1\": 13.25, \"PF%\": 0, \"entities_pred\": 3234, \"relations_pred\": 2637, \"triples_checked\": 2642}}, \"eval_70b_lora_docred_200_grammar_only\": {\"metrics\": {\"samples\": 200, \"parse_fail_pct\": 10.5, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.38, \"CF_pct\": 0.06, \"E_F1\": 80.13, \"E_P\": 85.16, \"E_R\": 75.66, \"R_F1\": 43.96, \"R_P\": 39.78, \"R_R\": 49.11, \"entities_pred\": 3362, \"relations_pred\": 3154}}, \"eval_70b_lora_docred_200_semantic_only\": {\"metrics\": {\"samples\": 200, \"parse_fail_pct\": 11, \"ET_pct\": 0, \"RV_pct\": 0.51, \"DR_pct\": 0, \"CF_pct\": 0.21, \"E_F1\": 80.06, \"E_P\": 85.21, \"E_R\": 75.5, \"R_F1\": 43.61, \"R_P\": 39.44, \"R_R\": 48.75, \"entities_pred\": 3351, \"relations_pred\": 3148}}, \"eval_70b_zs_docred_200_unconstrained\": {\"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities_pred\": 3242, \"relations_pred\": 2637, \"ET_pct\": 0, \"RV_pct\": 7.88, \"DR_pct\": 13.45, \"CF_count\": 0, \"fuzzy_matches\": 8, \"E_F1\": 70.14, \"E_P\": 75.85, \"E_R\": 65.23, \"R_F1\": 13.25, \"R_P\": 12.97, \"R_R\": 13.54}}, \"eval_70b_zs_docred_200_grammar_only\": {\"metrics\": {\"samples\": 200, \"parse_failures\": 1, \"entities_pred\": 3221, \"relations_pred\": 2609, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 17.03, \"CF_count\": 0, \"fuzzy_matches\": 0, \"E_F1\": 70.12, \"E_P\": 75.88, \"E_R\": 65.17, \"R_F1\": 13.23, \"R_P\": 12.99, \"R_R\": 13.47}}, \"eval_70b_zs_docred_200_semantic_only\": {\"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities\": 3240, \"relations\": 2596, \"ET_pct\": 0.12, \"RV_pct\": 8.24, \"DR_pct\": 1.66, \"CF_count\": 132, \"CF_pct\": 4.07, \"E_F1\": 70.1, \"E_P\": 75.87, \"E_R\": 65.15, \"R_F1\": 13.05, \"R_P\": 12.88, \"R_R\": 13.23, \"fuzzy_matches\": 8}}, \"eval_70b_lora_docred_200_beam4_s1\": {\"metrics\": {\"E-F1\": 85.57, \"E-P\": 85.45, \"E-R\": 85.68, \"R-F1\": 48.14, \"R-P\": 44.24, \"R-R\": 52.79, \"ET%\": 0, \"RV%\": 0, \"DR%\": 0, \"CF%\": 0, \"parse_fail\": \"1/200 (0.5%)\", \"entities_pred\": 3790, \"relations_pred\": 3030}}, \"eval_70b_lora_scierc_grammar_only\": {\"metrics\": {\"samples\": 551, \"json_failures\": 0, \"json_failure_rate\": 0, \"entities\": 1805, \"relations\": 1133, \"entity_type_violations\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violations\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violations\": 17, \"domain_range_violation_rate\": 0.015, \"cross_field_consistency_violations\": 0, \"fuzzy_relation_matches\": 0, \"entity_P\": 0.6272, \"entity_R\": 0.6707, \"entity_F1\": 0.6482, \"relation_P\": 0.4152, \"relation_R\": 0.4825, \"relation_F1\": 0.4463}}, \"eval_70b_zs_scierc_unconstrained\": {\"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 2353, \"relations\": 1483, \"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.4, \"CF_count\": 0, \"E_F1\": 35.22, \"E_P\": 30.13, \"E_R\": 42.38, \"R_F1\": 11.23, \"R_P\": 9.31, \"R_R\": 14.17, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_full_s2\": {\"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1531, \"relations\": 1027, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 18, \"E_F1\": 62.35, \"E_P\": 65.44, \"E_R\": 59.53, \"R_F1\": 36.28, \"R_P\": 35.35, \"R_R\": 37.27, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_semantic_only\": {\"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1806, \"relations\": 1133, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 9, \"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"parse_fail_pct\": 0}}, \"entity_order_ablation_qwen_scierc\": {\"metrics\": {\"E_F1\": 67.05, \"E_P\": 65.23, \"E_R\": 68.98, \"R_F1\": 43.77, \"R_P\": 40.78, \"R_R\": 47.23, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 21, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1784, \"relations\": 1128, \"corrected_original_R_F1\": 43.77, \"corrected_original_E_F1\": 67.05, \"corrected_original_DR_pct\": 0, \"corrected_original_CF_count\": 21, \"corrected_delta_R_F1\": 0, \"corrected_delta_E_F1\": 0, \"raw_output_identical\": true, \"parsed_output_identical\": true, \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"}}, \"eval_70b_zs_scierc_semantic_only\": {\"metrics\": {\"R_F1\": 11.37, \"DR_pct\": 1.01, \"RV_pct\": 0.6, \"ET_pct\": 0, \"CF_count\": 76, \"samples\": 551}}, \"eval_70b_zs_scierc_grammar_only\": {\"metrics\": {\"R_F1\": 11.23, \"DR_pct\": 6.33, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 0, \"samples\": 551}}, \"eval_70b_lora_scierc_beam4_s1\": {\"metrics\": {\"E_F1\": 64.89, \"E_P\": 62.29, \"E_R\": 67.72, \"R_F1\": 44.81, \"R_P\": 39.45, \"R_R\": 51.85, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 1, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1839, \"relations\": 1283}}, \"tcr_beam4_llama_scierc\": {\"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1803, \"relations\": 1194, \"entity_type_violations\": \"0/1803 (0.0%)\", \"relation_vocab_violations\": \"0/1194 (0.0%)\", \"domain_range_violations\": \"13/1194 (1.1%)\", \"cross_field_consistency\": 0, \"DR_pct\": 1.09, \"E_F1\": 68.02, \"E_P\": 65.88, \"E_R\": 70.29, \"R_F1\": 46.05, \"R_P\": 41.83, \"R_R\": 51.23, \"tcr_changed_selection\": \"0/551 (0.0%)\"}}, \"tcr_beam4_qwen_scierc\": {\"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1802, \"relations\": 1250, \"entity_type_violations\": \"0/1802 (0.0%)\", \"relation_vocab_violations\": \"0/1250 (0.0%)\", \"domain_range_violations\": \"23/1250 (1.8%)\", \"cross_field_consistency_violations\": 1, \"DR_pct\": 1.84, \"E_P\": 65.05, \"E_R\": 69.64, \"E_F1\": 67.26, \"R_P\": 39.36, \"R_R\": 50.51, \"R_F1\": 44.24, \"TCR_changed_selection\": \"0/551 (0.0%)\", \"all_candidates_TCR_1.0\": true}}, \"vllm_guided_json_scierc_zs\": {\"metrics\": {\"DR%\": 15.26, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.04, \"R-F1\": 8.75, \"E-F1\": 30.91, \"parse_fail%\": 0, \"total_samples\": 551, \"total_entities\": 2485, \"total_relations\": 1724, \"inference_time_s\": 108.5}}, \"eval_70b_lora_docred_200_s1_constrained\": {\"metrics\": {\"E_F1\": 79.38, \"E_P\": 85.24, \"E_R\": 74.28, \"R_F1\": 43.95, \"R_P\": 40.48, \"R_R\": 48.08, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.18, \"parse_fail_pct\": 12.5, \"samples\": 200}}, \"d066_beam_sweep\": {\"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}}, \"w8_llama_docred_ft_grammar_only\": {\"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"}}, \"w8_llama_docred_ft_semantic_only\": {\"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"}}, \"w8_qwen_docred_ft_semantic_only\": {\"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"}}, \"r16_trie_qwen_ft_scierc\": {\"metrics\": {\"E_F1\": 64.4, \"E_P\": 66.8, \"E_R\": 62.16, \"R_F1\": 41.16, \"R_P\": 38.24, \"R_R\": 44.56, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 95.5, \"CF_pct\": 0.09, \"parse_fail_pct\": 9.1, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\"}}, \"r16_trie_llama_ft_scierc\": {\"metrics\": {\"E_F1\": 36.66, \"E_P\": 67.47, \"E_R\": 25.16, \"R_F1\": 19.95, \"R_P\": 41.42, \"R_R\": 13.14, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 15.2, \"CF_pct\": 0, \"parse_fail_pct\": 50.8, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\"}}, \"eval_70b_lora_docred_200_unconstrained\": {\"metrics\": {\"E_F1\": 80.34, \"E_P\": 85.13, \"E_R\": 76.05, \"R_F1\": 43.8, \"R_P\": 39.6, \"R_R\": 48.99, \"ET_pct\": 0, \"RV_pct\": 0.57, \"DR_pct\": 0.22, \"CF_pct\": 0.06, \"parse_fail_pct\": 10, \"samples\": 200, \"relations\": 3159, \"RV_count\": 18, \"DR_count\": 7, \"CF_count\": 2}}, \"eval_70b_lora_scierc_s1_constrained\": {\"metrics\": {\"entity_f1\": 0.6476, \"entity_precision\": 0.6266, \"entity_recall\": 0.6701, \"relation_f1\": 0.4453, \"relation_precision\": 0.4149, \"relation_recall\": 0.4805, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 15, \"parse_fail_pct\": 0, \"fuzzy_matches\": 0, \"num_samples\": 551, \"num_entities\": 1805, \"num_relations\": 1129}}, \"eval_70b_lora_scierc_unconstrained\": {\"metrics\": {\"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.5, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1806, \"relations\": 1133}}, \"r16_70b_docred_zs_s1\": {\"metrics\": {\"E_F1\": 69.11, \"R_F1\": 13.05, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.04, \"parse_fail_pct\": 0.1, \"samples\": 998, \"total_entities\": 16599, \"total_triples\": 13239, \"baseline_unc_DR_pct\": 14.98, \"baseline_unc_R_F1\": 13.01, \"note\": \"Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\"}}, \"d066_sweep_llama_beam8_unc\": {\"metrics\": {\"E_F1\": 85.77, \"E_P\": 85.7, \"E_R\": 85.84, \"R_F1\": 51.97, \"R_P\": 49.76, \"R_R\": 54.38, \"DR_pct\": 0, \"CF_pct\": 0.05, \"ET_pct\": 0, \"RV_pct\": 0.07, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3788, \"total_relations_pred\": 2779}}, \"d066_sweep_llama_beam2_s1\": {\"metrics\": {\"E_F1\": 85.6, \"E_P\": 85.29, \"E_R\": 85.92, \"R_F1\": 51.17, \"R_P\": 48.51, \"R_R\": 54.14, \"DR_pct\": 0, \"CF_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3814, \"total_relations_pred\": 2839}}, \"d066_sweep_llama_docred_beam4_s1\": {\"metrics\": {\"E-F1\": 85.61, \"E-P\": 85.48, \"E-R\": 85.73, \"R-F1\": 51.89, \"R-P\": 51.59, \"R-R\": 52.2, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"ET_pct\": 0, \"RV_pct\": 0, \"samples\": 200, \"parse_fail\": 1}}, \"r16_70b_lora_docred\": {\"metrics\": {\"eval_loss\": 0.0635, \"token_acc\": 97.94, \"steps_completed\": 1146, \"epochs\": 3, \"train_loss_start\": 0.147, \"train_loss_end\": 0.056}}, \"r16_70b_lora_scierc\": {\"metrics\": {\"eval_loss\": 0.0611, \"token_acc\": 97.78, \"steps_completed\": 663, \"epochs\": 3, \"train_loss_start\": 0.183, \"train_loss_end\": 0.041}}, \"r16_70b_scierc_zs_s1\": {\"metrics\": {\"E_F1\": 35.19, \"R_F1\": 11.24, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 3.5, \"parse_fail_pct\": 0, \"samples\": 551, \"baseline_unc_E_F1\": 35.21, \"baseline_unc_R_F1\": 11.15, \"baseline_unc_DR_pct\": 6.41, \"baseline_unc_RV_pct\": 0.61, \"baseline_unc_CF_pct\": 0}}, \"r14_qwen_docred_beam4_998\": {\"metrics\": {\"E_F1\": 58.19, \"R_F1\": 8.72, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 4.94, \"parse_fail_pct\": 3.51, \"samples\": 998, \"success\": 963, \"fail\": 35}}, \"r16_trie_llama_zs_scierc\": {\"metrics\": {\"E_F1\": 23.23, \"R_F1\": 2.9, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 84.4, \"CF_pct\": 0.36, \"parse_fail_pct\": 0, \"samples\": 551}}, \"r16_trie_qwen_zs_scierc\": {\"metrics\": {\"E_F1\": 30.97, \"R_F1\": 8.64, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 29.3, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551}}, \"r14_llama_docred_beam4_998\": {\"metrics\": {\"R_F1\": 8.83, \"E_F1\": 57.81, \"DR_pct\": 0, \"CF_pct\": 1, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 3.91, \"samples\": 998, \"success\": 959, \"fail\": 39, \"baseline_ZS_greedy_R_F1\": 6.27, \"baseline_ZS_greedy_E_F1\": 54.93, \"baseline_ZS_greedy_DR_pct\": 2.55, \"baseline_ZS_greedy_CF_pct\": 8.54}}, \"d066_sweep_llama_scierc_beam8_s1_551\": {\"metrics\": {\"E-F1\": 67.51, \"E-P\": 64.99, \"E-R\": 70.23, \"R-F1\": 44.95, \"R-P\": 40.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0, \"samples\": 551, \"note\": \"Reconcile false positive corrected. Eval with --dataset scierc confirmed.\"}}, \"d066_sweep_llama_scierc_beam4_s1_551\": {\"metrics\": {\"E-F1\": 68.06, \"E-P\": 65.96, \"E-R\": 70.29, \"R-F1\": 46.18, \"R-P\": 42.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"parse_fail\": 0, \"samples\": 551, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}}, \"d066_sweep_llama_docred_beam4_unc\": {\"metrics\": {\"E-F1\": 85.67, \"R-F1\": 52.65, \"DR_pct\": 0.04, \"CF_pct\": 0.08, \"PF_pct\": 0.5, \"samples\": 200}}, \"d066_sweep_llama_docred_beam1_s1\": {\"metrics\": {\"E-F1\": 85.43, \"R-F1\": 47.35, \"DR_pct\": 0, \"CF_pct\": 0.19, \"PF_pct\": 2, \"samples\": 200}}, \"d066_sweep_llama_beam8_s1\": {\"metrics\": {\"E-F1\": 85.76, \"R-F1\": 51.74, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"samples\": 200}}, \"d065_qwen_greedy_4096_r2\": {\"metrics\": {\"E-F1\": 81.87, \"R-F1\": 40.79, \"DR_pct\": 0, \"CF_pct\": 0.22, \"ET_pct\": 0, \"RV_pct\": 0, \"PF_pct\": 8.52, \"samples\": 998}}, \"d066_sweep_llama_scierc_beam2_s1_551\": {\"metrics\": {\"entity_f1\": 68.34, \"entity_p\": 66.59, \"entity_r\": 70.17, \"relation_f1\": 46.12, \"relation_p\": 42.73, \"relation_r\": 50.1, \"parse_fail_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.17, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}}, \"d066_sweep_llama_scierc_beam1_unc\": {\"metrics\": {\"total\": 275, \"success\": 275, \"fail\": 0, \"output_file\": \"llama_scierc_beam1_unconstrained.jsonl\", \"note\": \"INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\"}}, \"d066_sweep_llama_docred_beam1_unc\": {\"metrics\": {\"total\": 200, \"success\": 196, \"fail\": 4, \"output_file\": \"llama_docred_200_beam1_unconstrained.jsonl\"}}, \"d066_sweep_21461_gpu1\": {\"metrics\": {\"total\": 551, \"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"avg_time_s\": 5.058, \"output_file\": \"qwen_scierc_beam8_full_s1.jsonl\", \"note\": \"Actually ran on SciERC 551 docs (not DocRED 200 as originally recorded in hypothesis)\"}}, \"w5_llama_docred_lora_constrained_eval\": {\"metrics\": {\"total\": 998, \"parse_failures\": 25, \"parse_fail_rate\": 2.51, \"entities\": 19077, \"relations\": 16074, \"entity_f1\": 83.94, \"entity_precision\": 85, \"entity_recall\": 84.13, \"relation_f1_all_set\": 43.78, \"relation_precision_all_set\": 38.79, \"relation_recall_all_set\": 50.81, \"et_violations\": 0, \"et_violation_rate\": 0, \"rv_violations\": 0, \"rv_violation_rate\": 0, \"dr_violations\": 33, \"dr_violation_rate\": 0.21, \"CF_pct\": 0.21, \"delta_vs_unconstrained\": {\"delta_e_f1\": 0.01, \"delta_r_f1\": 0.06, \"delta_dr\": -0.28, \"note\": \"Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20.\"}, \"provenance\": \"eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.\"}}, \"d066_sweep_16980_gpu1\": {}, \"d065_qwen_greedy_4096\": {}, \"d066_docred_beam_sweep\": {}, \"d067_seed_variance\": {\"metrics\": {\"qwen_scierc_unc\": {\"E_F1\": \"66.94 ± 0.08\", \"R_F1\": \"43.25 ± 0.43\", \"DR\": \"2.06 ± 0.08\", \"CF\": \"0.00 ± 0.00\"}, \"qwen_scierc_con\": {\"E_F1\": \"66.94 ± 0.08\", \"R_F1\": \"43.22 ± 0.39\", \"DR\": \"0.00 ± 0.00\", \"CF\": \"0.48 ± 0.02\"}, \"llama_scierc_unc\": {\"E_F1\": \"67.99 ± 0.16\", \"R_F1\": \"45.38 ± 0.05\", \"DR\": \"1.04 ± 0.05\", \"CF\": \"0.00 ± 0.00\"}, \"llama_scierc_con\": {\"E_F1\": \"67.99 ± 0.16\", \"R_F1\": \"45.40 ± 0.05\", \"DR\": \"0.03 ± 0.04\", \"CF\": \"0.26 ± 0.02\"}, \"max_sigma_pp\": 0.43, \"greedy_deterministic\": true, \"snr_dr_improvement\": \">12x\", \"qwen_docred_status\": \"pending (not started)\", \"llama_scierc_seed456_con_status\": \"running (407/551)\"}}, \"d068_constraint_guided_beam_pilot\": {}, \"d064_docred_full_beam\": {}, \"d065_tcr_full\": {\"metrics\": {\"configs_tested\": 10, \"all_cf_eliminated\": true, \"scierc_all_dr_delta_max\": 0.28, \"docred_lora_dr_delta_max\": 0.14, \"docred_zs_llama_dr_delta\": 9.38, \"docred_zs_70b_dr_delta\": 4.2, \"docred_zs_qwen_dr_delta\": 1.53, \"fund_conflict_scierc_max\": 2.04, \"fund_conflict_docred_zs_max\": 22.78, \"fund_conflict_docred_lora_max\": 12.16, \"lora_ef1_cost_max\": 0.0075, \"zs_docred_ef1_cost_max\": 0.0598}}, \"d065_tcr_pilot\": {\"metrics\": {\"scierc_zs_qwen\": {\"cf_before\": 9.75, \"cf_after\": 0, \"dr_before\": 0.93, \"dr_after\": 1.21, \"ef1_delta\": -0.0129, \"fund_pct\": 2.04}, \"scierc_zs_llama\": {\"cf_before\": 6.4, \"cf_after\": 0, \"dr_before\": 0.08, \"dr_after\": 0.3, \"ef1_delta\": -0.0178, \"fund_pct\": 1.85}, \"scierc_lora_qwen\": {\"cf_before\": 1.19, \"cf_after\": 0, \"dr_before\": 0, \"dr_after\": 0, \"ef1_delta\": -0.0075, \"fund_pct\": 0}, \"scierc_lora_llama\": {\"cf_before\": 0.46, \"cf_after\": 0, \"dr_before\": 0.09, \"dr_after\": 0.09, \"ef1_delta\": -0.0018, \"fund_pct\": 0}, \"scierc_zs_mistral\": {\"cf_before\": 0.67, \"cf_after\": 0, \"dr_before\": 13.36, \"dr_after\": 12.87, \"ef1_delta\": 0.0005, \"fund_pct\": 0}, \"docred_zs_qwen\": {\"cf_before\": 13.11, \"cf_after\": 0, \"dr_before\": 10.21, \"dr_after\": 11.74, \"ef1_delta\": -0.0344, \"fund_pct\": 13.52}, \"docred_zs_llama\": {\"cf_before\": 23.71, \"cf_after\": 0, \"dr_before\": 2.55, \"dr_after\": 11.93, \"ef1_delta\": -0.0521, \"fund_pct\": 22.78}, \"docred_zs_70b\": {\"cf_before\": 11.61, \"cf_after\": 0, \"dr_before\": 0, \"dr_after\": 4.2, \"ef1_delta\": -0.0598, \"fund_pct\": 18.26}, \"docred_lora_qwen\": {\"cf_before\": 0.42, \"cf_after\": 0, \"dr_before\": 0.01, \"dr_after\": 0.14, \"ef1_delta\": -0.0016, \"fund_pct\": 12.16}, \"docred_lora_llama\": {\"cf_before\": 0.36, \"cf_after\": 0, \"dr_before\": 0.21, \"dr_after\": 0.2, \"ef1_delta\": -0.0017, \"fund_pct\": 11.59}, \"total_configs\": 10, \"all_cf_eliminated\": true}}, \"d063_gollie_violation_rate\": {\"metrics\": {\"gollie_DR\": 0, \"gollie_RV\": 0, \"gollie_ET\": 0, \"gollie_CF\": 0.67, \"gollie_entities\": 300, \"gollie_relations\": 7, \"gollie_empty_docs_pct\": 45, \"docs_tested\": 100}}, \"d062_full_ft_scierc\": {\"metrics\": {\"unconstrained\": {\"entity_f1\": 0.6478, \"relation_f1\": 0.3789, \"DR_pct\": 2.74, \"RV_pct\": 0.18, \"ET_pct\": 0, \"CF_pct\": 0}, \"constrained\": {\"entity_f1\": 0.6478, \"relation_f1\": 0.3789, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 1.31}, \"training\": {\"eval_loss_final\": 0.09459, \"epochs\": 3, \"total_steps\": 333, \"training_time\": \"21m49s\"}}}, \"d062_beam_latency\": {\"metrics\": {\"beam4_unconstrained_s_per_doc\": 3.446, \"beam4_constrained_s_per_doc\": 4.013, \"beam4_unconstrained_total_s\": 1898.7, \"beam4_constrained_total_s\": 2211, \"beam_greedy_ratio_unconstrained\": 1.319, \"beam_greedy_ratio_constrained\": 1.397, \"constraint_overhead_beam\": 1.165, \"constraint_overhead_greedy\": 1.1, \"greedy_unconstrained_s_per_doc\": 2.612, \"greedy_constrained_s_per_doc\": 2.873}}, \"d062_ontology_scalability\": {\"metrics\": {\"compile_small_total_s\": 0.334, \"compile_medium_total_s\": 0.322, \"compile_large_total_s\": 0.345, \"compile_xlarge_total_s\": 0.42, \"grammar_small_s\": 0.333, \"grammar_xlarge_s\": 0.365, \"semantic_small_s\": 0.0004, \"semantic_xlarge_s\": 0.017, \"overhead_small\": 1.02, \"overhead_medium\": 1.03, \"overhead_large\": 1.03, \"overhead_xlarge\": 1.03, \"failures\": 0}}, \"d062_cf_majority_voting\": {\"metrics\": {\"qwen_scierc_zs\": {\"cf_before\": 245, \"cf_after\": 201, \"dr_rate_before\": 0.0093, \"dr_rate_after\": 0.0324}, \"llama_scierc_zs\": {\"cf_before\": 162, \"cf_after\": 123, \"dr_rate_before\": 0.0008, \"dr_rate_after\": 0.0236}, \"qwen_docred_zs\": {\"cf_before\": 518, \"cf_after\": 21, \"dr_rate_before\": 0.1021, \"dr_rate_after\": 0.1466}, \"llama_docred_zs\": {\"cf_before\": 1358, \"cf_after\": 107, \"dr_rate_before\": 0.0255, \"dr_rate_after\": 0.1665}, \"qwen_scierc_ft\": {\"cf_before\": 21, \"cf_after\": 12, \"dr_rate_before\": 0, \"dr_rate_after\": 0.0071}, \"llama_scierc_ft\": {\"cf_before\": 8, \"cf_after\": 4, \"dr_rate_before\": 0.0009, \"dr_rate_after\": 0.0037}, \"qwen_docred_ft\": {\"cf_before\": 48, \"cf_after\": 3, \"dr_rate_before\": 0.0001, \"dr_rate_after\": 0.0044}, \"llama_docred_ft\": {\"cf_before\": 41, \"cf_after\": 2, \"dr_rate_before\": 0.0021, \"dr_rate_after\": 0.005}}}, \"p1_ee_ft_llama_r2\": {\"metrics\": {\"parse_rate_unconstrained\": 1, \"parse_rate_constrained\": 1, \"trigger_f1_unconstrained\": 0.2752, \"trigger_f1_constrained\": 0.2691, \"argument_f1_unconstrained\": 0.0998, \"argument_f1_constrained\": 0.0891, \"entity_f1\": 0, \"rov_rate_unconstrained\": 0.088, \"rov_rate_constrained\": 0, \"ac_rate_unconstrained\": 0.035, \"ac_rate_constrained\": 0.008, \"go_nogo_unconstrained\": 0.122, \"go_nogo_constrained\": 0.0078}}, \"p1_ee_ft_composability_r5\": {\"metrics\": {\"unconstrained\": {\"parse_rate\": 0.85, \"trigger_f1\": 0.3208, \"argument_f1\": 0.0785, \"rov_rate\": 0.3831, \"ac_rate\": 0.0268, \"go_nogo\": 0.41}, \"full_s1\": {\"parse_rate\": 0.95, \"trigger_f1\": 0.2672, \"argument_f1\": 0.0818, \"rov_rate\": 0, \"ac_rate\": 0, \"go_nogo\": 0}}}, \"p1_ee_ft_llama\": {}, \"p1_ee_ft_composability_r4\": {\"metrics\": {\"unconstrained\": {\"entity_f1\": 0, \"trigger_f1\": 0.4598, \"argument_f1\": 0.1581, \"rov\": 0.251, \"ac\": 0.06, \"cf\": 0, \"parse_rate\": 0.25}, \"full_s1\": {\"entity_f1\": 0.5823, \"trigger_f1\": 0.6, \"argument_f1\": 0.4667, \"rov\": 0, \"ac\": 0, \"cf\": 0.03, \"parse_rate\": 0.1}}}, \"w9_qwen_docred_zs_sampling_r2\": {}, \"70b_docred_constrained\": {\"metrics\": {\"ET_violation\": 0, \"RV_violation\": 0, \"DR_violation\": 0, \"CF_violation\": 7.01, \"entity_f1\": 69.05, \"entity_precision\": 75.03, \"entity_recall\": 63.95, \"relation_f1\": 13.07, \"relation_precision\": 12.54, \"relation_recall\": 13.64, \"parse_failures\": 1, \"docs_processed\": 997, \"total_docs\": 998, \"unique_entities\": 12207, \"total_triples\": 13249}}, \"70b_docred_unconstrained\": {\"metrics\": {\"entity_f1\": 69.03, \"entity_precision\": 75.03, \"entity_recall\": 63.92, \"relation_f1\": 13.03, \"relation_precision\": 12.43, \"relation_recall\": 13.69, \"ET_violation\": 0.02, \"RV_violation\": 7.8, \"DR_violation\": 15, \"CF_violation\": 0.07, \"parse_failures\": 0, \"docs_processed\": 998}}, \"p1_ee_ft_composability_r3\": {}, \"p1_ee_ft_composability_r2\": {}, \"p1_ee_ft_composability\": {}, \"p8c_ft_scierc_latency\": {\"metrics\": {\"unconstrained_mean_s\": 2.612, \"constrained_mean_s\": 2.873, \"unconstrained_median_s\": 2.355, \"constrained_median_s\": 2.624, \"overhead_mean_pct\": 10, \"overhead_median_pct\": 11.42, \"per_doc_ratio_mean\": 1.205, \"per_doc_ratio_median\": 1.117, \"num_docs\": 551, \"unconstrained_total_s\": 1439, \"constrained_total_s\": 1582.9}}, \"p8b_docred_latency\": {}, \"w9_qwen_docred_zs_sampling\": {}, \"w9_qwen_scierc_zs_sampling\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.75, \"CF_pct\": 9.9, \"E_F1\": 31.28, \"R_F1\": 7.42, \"parse_fail_rate\": 0, \"total_samples\": 551, \"note\": \"F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98, R_F1=8.36\"}}, \"p8_latency_overhead\": {\"metrics\": {\"samples\": 551, \"unconstrained_mean_s\": 4.163, \"unconstrained_median_s\": 4.106, \"unconstrained_total_s\": 2293.7, \"constrained_mean_s\": 4.71, \"constrained_median_s\": 4.644, \"constrained_total_s\": 2595, \"overhead_ratio_mean\": 1.131, \"overhead_ratio_median\": 1.131, \"overhead_ratio_p95_perdoc\": 1.262, \"overhead_pct\": 13.1}}, \"q1_llama_lora_scierc_beam4\": {\"metrics\": {\"ET_violation_rate\": 0, \"RV_violation_rate\": 0, \"DR_violation_rate\": 0, \"CF_violation_rate\": 0, \"entity_f1\": 67.94, \"relation_f1\": 46.11, \"samples\": 551, \"total_entities\": 1853, \"total_relations\": 727}}, \"70b_scierc_unconstrained\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.5, \"CF_count\": 0, \"CF_pct\": 0, \"E_F1\": 0.3517, \"E_P\": 0.3009, \"E_R\": 0.4232, \"R_F1\": 0.1122, \"R_P\": 0.0929, \"R_R\": 0.1417, \"total_entities\": 2353, \"total_relations\": 1485, \"parse_failures\": 0, \"samples\": 551}}, \"70b_scierc_constrained\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 86, \"CF_pct\": 3.66, \"E_F1\": 0.3514, \"E_P\": 0.3007, \"E_R\": 0.4226, \"R_F1\": 0.1124, \"R_P\": 0.0932, \"R_R\": 0.1417, \"total_entities\": 2351, \"total_relations\": 1481, \"parse_failures\": 0, \"samples\": 551}}, \"ee_mistral_wikievents_grammar_only_v3\": {\"metrics\": {\"parse_success\": \"218/246 (88.6%)\", \"parse_failures\": 28, \"ET\": 0, \"EV\": 0, \"RoV\": 64, \"AC\": 13.8, \"CF\": 1.1, \"go_no_go\": 77.73, \"entity_f1\": 0.1192, \"trigger_f1\": 0.0337, \"argument_f1\": 0.0027, \"code_version\": \"938-line (collision+exact-match fix)\", \"mode\": \"grammar_only\"}}, \"ee_mistral_wikievents_constrained_v3\": {\"metrics\": {\"parse_success\": \"218/246 (88.6%)\", \"parse_failures\": 28, \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 1.3, \"CF\": 14.9, \"go_no_go\": 1.26, \"entity_f1\": 0.1171, \"trigger_f1\": 0.0387, \"argument_f1\": 0.0031, \"code_version\": \"938-line (collision+exact-match fix)\", \"posthoc_args_removed\": 86, \"posthoc_ac_after\": 0}}, \"ee_llama_wikievents_constrained_v3\": {\"metrics\": {\"parse_success\": \"207/246 (84.1%)\", \"parse_failures\": 39, \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 3.8, \"CF\": 17.2, \"go_no_go\": 3.8, \"entity_f1\": 0.1763, \"trigger_f1\": 0.0748, \"argument_f1\": 0.0118, \"code_version\": \"938-line (collision+exact-match fix)\", \"posthoc_args_removed\": 173, \"posthoc_arg_f1\": 0.0118}}, \"ee_qwen_wikievents_constrained_v3\": {\"metrics\": {\"parse_success\": \"206/246 (83.7%)\", \"parse_failures\": 40, \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 2.1, \"CF\": 21.1, \"go_no_go\": 2.05, \"entity_f1\": 0.1409, \"trigger_f1\": 0.1339, \"argument_f1\": 0.0168, \"code_version\": \"938-line (collision+exact-match fix)\", \"posthoc_args_removed\": 109, \"posthoc_arg_f1\": 0.017, \"cf_voting_fix_rate\": \"15.9%\", \"cf_voting_entity_f1\": 0.1352}}, \"ee_mistral_wikievents_constrained_v2\": {\"metrics\": {\"parse_success\": \"178/246 (72.4%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 0.1, \"AC\": 16.6, \"CF\": 13.9, \"trigger_f1\": 0.0508, \"argument_f1\": 0.0047, \"entity_f1\": 0.1245, \"parse_failures\": 68, \"go_no_go\": 16.7}}, \"ee_qwen_wikievents_constrained\": {\"metrics\": {\"parse_success\": \"206/246 (83.7%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 0.3, \"AC\": 2.1, \"CF\": 21.1, \"trigger_f1\": 0.1339, \"argument_f1\": 0.0168, \"entity_f1\": 0.1409, \"parse_failures\": 40, \"go_no_go\": 2.4, \"note\": \"after retry with max_new_tokens=8192\"}}, \"ee_mistral_wikievents_constrained\": {\"metrics\": {\"parse_success\": \"184/246 (74.8%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 54.8, \"AC\": 19.2, \"CF\": 0.7, \"note\": \"grammar_only baseline (old code without semantic mask fix)\"}}, \"ee_llama_wikievents_constrained\": {\"metrics\": {\"parse_success\": \"215/246 (87.4%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 3.4, \"CF\": 15.5, \"trigger_f1\": 0.078, \"argument_f1\": 0.011, \"entity_f1\": 0.178, \"parse_failures\": 31, \"go_no_go\": 3.4, \"note\": \"after retry with max_new_tokens=8192\"}}, \"ee_mistral_wikievents_unconstrained\": {\"metrics\": {\"parse_success\": \"194/246 (78.9%)\", \"ET\": 0, \"EV\": 37.3, \"RoV\": 63.9, \"AC\": 0, \"CF\": 0, \"trigger_f1\": 0.0241, \"argument_f1\": 0, \"entity_f1\": 0}}, \"ee_llama_wikievents_unconstrained\": {\"metrics\": {\"parse_success\": \"226/246 (91.9%)\", \"ET\": 0, \"EV\": 10.5, \"RoV\": 88.8, \"AC\": 0.1, \"CF\": 0, \"trigger_f1\": 0.0572, \"argument_f1\": 0, \"entity_f1\": 0}}, \"ee_qwen_wikievents_unconstrained\": {\"metrics\": {\"parse_success\": \"218/246 (88.6%)\", \"ET\": 0, \"EV\": 24, \"RoV\": 74.9, \"AC\": 0.3, \"CF\": 0, \"trigger_f1\": 0.1184, \"argument_f1\": 0.0009, \"entity_f1\": 0}}, \"r4_prompt_detailed\": {\"metrics\": {\"unconstrained\": {\"ET_pct\": 0.22, \"RV_pct\": 0.45, \"DR_pct\": 11.07, \"E_F1\": 33.55, \"R_F1\": 10.48}, \"constrained\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.64, \"E_F1\": 33.56, \"R_F1\": 10.48}, \"DR_reduction_pct\": 94.2, \"delta_R_F1_pp\": 0, \"delta_E_F1_pp\": 0.01}}, \"r4_prompt_minimal\": {\"metrics\": {\"unconstrained\": {\"ET_pct\": 0.58, \"RV_pct\": 1.16, \"DR_pct\": 16.91, \"E_F1\": 31.98, \"R_F1\": 7.91}, \"constrained\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.92, \"E_F1\": 31.99, \"R_F1\": 7.85}, \"DR_reduction_pct\": 94.6, \"delta_R_F1_pp\": -0.06, \"delta_E_F1_pp\": 0.01}}, \"w10_qwen_scierc_ft_beam_4\": {\"metrics\": {\"DR\": 0, \"CF\": 0, \"total_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0, \"E_F1\": 66.88, \"E_P\": 64.69, \"E_R\": 69.22, \"R_F1\": 44.23, \"R_P\": 39.41, \"R_R\": 50.41, \"total_samples\": 551, \"json_parse_failures\": 0, \"total_entities\": 1802, \"total_relations\": 1246, \"vs_ft_greedy\": {\"baseline\": \"w5_lora_scierc_constrained_eval\", \"DR_delta\": \"0% → 0% (same)\", \"CF_delta\": \"1.18% → 0.0% (eliminated all violations)\", \"E_F1_delta\": \"67.05 → 66.88 (-0.17, negligible)\", \"R_F1_delta\": \"43.77 → 44.23 (+0.46, slight improvement)\"}, \"vs_zs_beam_k4\": {\"DR_delta\": \"0% → 0% (same)\", \"CF_delta\": \"0.53% → 0.0% (eliminated)\", \"E_F1_delta\": \"32.00 → 66.88 (+34.88)\", \"R_F1_delta\": \"8.56 → 44.23 (+35.67)\"}}}, \"w10_beam_ablation_k8\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.08, \"CF_count\": 2, \"E_F1\": 32.18, \"R_F1\": 8.39, \"E_P\": 26.95, \"E_R\": 39.93, \"R_P\": 6.54, \"R_R\": 11.7, \"parse_failures\": 0, \"total_samples\": 551, \"total_triples\": 1744, \"total_entities\": 2483, \"vs_greedy\": {\"DR_delta\": -0.93, \"CF_delta\": -9.82, \"E_F1_delta\": 1.2, \"R_F1_delta\": 0.03}, \"vs_beam_k4\": {\"DR_delta\": 0, \"CF_delta\": -0.45, \"E_F1_delta\": 0.18, \"R_F1_delta\": -0.17}}}, \"w9_mistral_docred_beam_50\": {\"metrics\": {\"ET_violation_rate\": 0, \"RV_violation_rate\": 0, \"DR_violation_rate\": 21.37, \"CF_violations\": 1, \"total_triples\": 524, \"total_entities\": 597, \"docs_checked\": 49, \"parse_failures\": 1, \"E_F1\": 51.78, \"E_P\": 65.2, \"E_R\": 42.94, \"R_F1\": 5.7, \"R_P\": 6.49, \"R_R\": 5.08, \"R_tp\": 34, \"R_gold\": 669, \"R_pred\": 524}}, \"w10_beam_ablation_k2\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.35, \"CF_count\": 71, \"CF_pct\": 4.12, \"E_F1\": 31.54, \"R_F1\": 8.75, \"parse_failures\": 0, \"total_samples\": 551, \"total_triples\": 1724, \"vs_greedy\": {\"DR_delta\": -0.58, \"CF_delta\": -5.78, \"E_F1_delta\": 0.56, \"R_F1_delta\": 0.39, \"note\": \"Greedy: DR=0.93%, CF=9.90%, E_F1=30.98, R_F1=8.36\"}, \"vs_beam_k4\": {\"DR_delta\": 0.35, \"CF_delta\": 3.59, \"E_F1_delta\": -0.46, \"R_F1_delta\": 0.19, \"note\": \"k=4: DR=0%, CF=0.53%, E_F1=32.00, R_F1=8.56\"}}}, \"w10_mistral_scierc_beam_551\": {\"metrics\": {\"total_samples\": 551, \"parse_failures\": 1, \"parse_rate\": 0.9982, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 13.79, \"CF_pct\": 0.57, \"E_P\": 23.04, \"E_R\": 31.64, \"E_F1\": 26.66, \"R_P\": 3.13, \"R_R\": 7.22, \"R_F1\": 4.37, \"total_entities\": 2294, \"total_triples\": 2241, \"vs_greedy\": {\"baseline\": \"w6_mistral_scierc_constrained\", \"greedy_DR\": 13.4, \"greedy_CF\": 1.27, \"greedy_E_F1\": 27.46, \"greedy_R_F1\": 3.67, \"delta_DR\": \"+0.39pp\", \"delta_CF\": \"-0.70pp\", \"delta_E_F1\": \"-0.80pp\", \"delta_R_F1\": \"+0.70pp\"}}}, \"w10_llama_docred_beam_50\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.94, \"E_F1\": 55.62, \"R_F1\": 9.47, \"parse_failures\": 3, \"parse_fail_rate\": 6, \"total_samples\": 50, \"vs_greedy_full_s1\": {\"DR_delta\": -2.57, \"CF_delta\": -11.19, \"E_F1_delta\": 0.61, \"R_F1_delta\": 3.2, \"note\": \"Greedy baseline: DR=2.57%, CF=12.13%, E_F1=55.01, R_F1=6.27\"}, \"checker_note\": \"Must use violation_checker_docred.py for DocRED (not violation_checker.py)\"}}, \"w10_type_consensus_docred_50\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 8.69, \"CF_pct\": 2.4, \"E_F1\": 59.08, \"R_F1\": 8.33, \"gtc_skip_total\": 601, \"gtc_skip_unique_entities\": 213, \"gtc_effective_corrections\": 0, \"delta_DR\": 0, \"delta_CF\": 0}}, \"w10_type_consensus_prototype\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36, \"gtc_skip_total\": 672, \"gtc_skip_unique_entities\": 258, \"gtc_effective_corrections\": 0, \"delta_DR\": 0, \"delta_CF\": 0}}, \"w9_qwen_scierc_stability_3seeds\": {\"metrics\": {\"seed_123\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36}, \"seed_456\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36}, \"seed_789\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36}, \"cross_seed_DR_std\": 0, \"cross_seed_DR_range\": 0, \"conclusion_note\": \"Greedy decoding is fully deterministic - seed has no effect on output. All metrics identical across 3 seeds.\"}}, \"w9_qwen_docred_beam_50\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.55, \"E_F1\": 58.64, \"R_F1\": 9.37, \"total_samples\": 50, \"parse_failures\": 3, \"parse_fail_rate\": 6, \"vs_greedy_full_s1\": {\"DR_delta\": -10.21, \"CF_delta\": -2.02, \"E_F1_delta\": -0.73, \"R_F1_delta\": 1.14, \"note\": \"Greedy full_s1 998 docs: DR=10.21%, CF=2.57%, E_F1=59.37, R_F1=8.23. Beam eliminates ALL DR on DocRED 96-type schema.\"}}}, \"w9_llama_scierc_beam_551\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.93, \"CF_count\": 15, \"E_F1\": 25.04, \"E_P\": 21.27, \"E_R\": 30.42, \"R_F1\": 3.33, \"R_P\": 2.68, \"R_R\": 4.41, \"total_entities\": 2398, \"total_relations\": 1606, \"parse_fail_rate\": 0, \"total_samples\": 551, \"vs_greedy_full_s1\": {\"DR_delta\": -0.08, \"CF_delta\": -5.63, \"E_F1_delta\": 1.55, \"R_F1_delta\": 0.79, \"note\": \"Greedy: DR=0.08%, CF=6.56%, E_F1=23.49%, R_F1=2.54%\"}}}, \"posthoc_filtering_baseline\": {\"metrics\": {\"docred_f1_before\": 7.74, \"docred_f1_after\": 9.61, \"docred_precision_before\": 6.55, \"docred_precision_after\": 11.22, \"docred_recall_before\": 9.46, \"docred_recall_after\": 8.4, \"docred_rejection_rate\": 0.481, \"docred_tp_before\": 1137, \"docred_tp_after\": 1010, \"docred_tp_lost\": 127, \"docred_et_residual\": 0.0247, \"scierc_f1_before\": 8.23, \"scierc_f1_after\": 8.63, \"scierc_rejection_rate\": 0.168, \"scierc_recall_before\": 11.4, \"scierc_recall_after\": 10.68, \"scierc_tp_before\": 111, \"scierc_tp_after\": 104}}, \"phase2_scierc_full_s2\": {\"metrics\": {\"total_samples\": 551, \"total_triples\": 1644, \"total_entities\": 2228, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0097, \"cross_field_consistency_violation_rate\": 0.0803, \"entity_precision\": 0.2797, \"entity_recall\": 0.3712, \"entity_f1\": 0.319, \"relation_precision\": 0.064, \"relation_recall\": 0.1078, \"relation_f1\": 0.0803, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"llama_docred_unconstrained_mt6144\": {\"metrics\": {\"ET_rate\": 0.13, \"RV_rate\": 15.89, \"DR_rate\": 26.18, \"DR_rate_eligible\": 31.15, \"CF_rate\": 0.17, \"entity_precision\": 61.19, \"entity_recall\": 51.06, \"entity_f1\": 55.67, \"relation_precision\": 5.18, \"relation_recall\": 7, \"relation_f1\": 5.95, \"parse_failures\": 67, \"documents_checked\": 931, \"total_documents\": 998, \"unique_entities\": 11534, \"total_triples\": 16584, \"dr_eligible_triples\": 13936, \"fuzzy_relation_matches\": 121}}, \"llama_docred_full_s1_mt6144\": {\"metrics\": {\"DR_rate_pct\": 2.57, \"RV_rate_pct\": 0, \"ET_rate_pct\": 0, \"CF_rate_pct\": 12.13, \"R_F1\": 6.25, \"R_precision\": 5.45, \"R_recall\": 7.32, \"E_F1\": 55.04, \"E_precision\": 61.41, \"E_recall\": 49.87, \"documents_total\": 998, \"documents_checked\": 908, \"parse_failures\": 90, \"triples\": 16471, \"unique_entities\": 11307, \"fallback_events\": 67911, \"wall_clock_seconds\": 23926, \"vs_unconstrained_mt6144\": {\"DR_delta_pp\": -23.61, \"DR_reduction_pct\": -90.2, \"R_F1_delta_pp\": 0.3, \"E_F1_delta_pp\": -0.63}, \"vs_full_s1_mt4096\": {\"DR_delta_pp\": 0.02, \"R_F1_delta_pp\": -0.02, \"E_F1_delta_pp\": 0.03, \"CF_delta_pp\": 0.11, \"parse_fail_delta\": -1}}}, \"beam_search_scierc_full_551\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.53, \"E_F1\": 32, \"R_F1\": 8.56, \"E_P\": 26.83, \"E_R\": 39.63, \"R_P\": 6.69, \"R_R\": 11.91, \"parse_fail_rate\": 0, \"total_entities\": 2476, \"total_relations\": 1737}}, \"w7_llama_scierc_ft_semantic_only\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.65, \"CF_count\": 2, \"E_F1\": 67.76, \"E_P\": 66.47, \"E_R\": 69.1, \"R_F1\": 45.47, \"R_P\": 43.24, \"R_R\": 47.95, \"total_entities\": 1757, \"total_relations\": 1081, \"json_parse_failures\": 0}}, \"w7_llama_scierc_ft_grammar_only\": {\"metrics\": {\"total_samples\": 551, \"json_parse_failures\": 0, \"total_entities\": 1757, \"total_relations\": 1082, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": {\"precision\": 0.6647, \"recall\": 0.691, \"f1\": 0.6776}, \"relation_f1\": {\"precision\": 0.432, \"recall\": 0.4795, \"f1\": 0.4545}}}, \"w7_qwen_scierc_ft_semantic_only\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 15, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4073, \"R_R\": 0.4713, \"R_F1\": 0.4369, \"DR_violations\": 7, \"delta_vs_grammar_only\": {\"DR_delta\": -1.3, \"note\": \"semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces DR by 68%\"}, \"delta_vs_unconstrained\": {\"DR_delta\": -1.35, \"note\": \"unconstrained DR=1.95% → semantic_only 0.6%\"}}}, \"w7_qwen_scierc_ft_grammar_only\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.9, \"CF_pct\": 0, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4087, \"R_R\": 0.4733, \"R_F1\": 0.4386, \"DR_violations\": 22, \"tokenizer_warning\": \"false_positive_transformers_4.57.6\"}}, \"w5_llama_lora_scierc_unconstrained_eval\": {\"metrics\": {\"total_samples\": 551, \"total_entities\": 1757, \"total_relations\": 1082, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"total_violation_rate\": 0.0042, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"entity_f1\": 0.6776, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"relation_f1\": 0.4545}}, \"w5_llama_lora_scierc_constrained_eval\": {\"metrics\": {\"domain_range_violation_rate\": 0.0009, \"relation_vocabulary_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0046, \"relation_f1\": 0.4547, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"entity_f1\": 0.6776, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"total_relations\": 1081, \"total_entities\": 1757, \"total_samples\": 551, \"parse_failures\": 0}}, \"w5_lora_scierc_constrained_eval\": {\"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0118, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4377, \"relation_precision\": 0.4078, \"relation_recall\": 0.4723, \"total_entities\": 1784, \"total_relations\": 1128, \"total_samples\": 551, \"cross_field_consistency_violations\": 21}}, \"w1_cf_fallback_scierc_pilot\": {\"metrics\": {\"ET\": 0, \"RV\": 0, \"DR\": 0.1478, \"CF\": 0.0004, \"R_F1\": 0.0823, \"R_P\": 0.0643, \"R_R\": 0.114, \"E_F1\": 0.3098, \"E_P\": 0.2598, \"E_R\": 0.3837, \"entities\": 2474, \"relations\": 1725, \"samples\": 551, \"grammar_first_fallback_rate\": 0.3664, \"cf_registry_fallback_rate\": 0.0448, \"total_mask_calls\": 17024, \"violation_budget_DR_CF\": 0.1482}}, \"w5_lora_scierc_training\": {\"metrics\": {\"train_loss\": 0.0634, \"eval_loss\": 0.0586, \"eval_token_accuracy\": 0.9816, \"eval_entropy\": 0.9635, \"train_runtime_sec\": 688.4, \"epochs\": 3, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\", \"merged_model_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\"}}, \"w8_qwen_docred_ft_grammar_only\": {\"metrics\": {\"E_F1\": 82.19, \"E_P\": 85.47, \"E_R\": 79.16, \"R_F1\": 40.85, \"R_P\": 36.27, \"R_R\": 46.77, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.61, \"CF_pct\": 0.11, \"parse_fail_rate\": 7.01, \"total_samples\": 998, \"parse_failures\": 70}}, \"w6_mistral_scierc_unconstrained\": {\"metrics\": {\"E_P\": 0.2402, \"E_R\": 0.3156, \"E_F1\": 0.2728, \"R_P\": 0.0295, \"R_R\": 0.0483, \"R_F1\": 0.0366, \"ET_pct\": 1.5, \"RV_pct\": 0, \"DR_pct\": 56.94, \"CF_pct\": 56.87, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2202, \"total_pred_relations\": 1593}}, \"w6_mistral_scierc_constrained\": {\"metrics\": {\"E_P\": 0.2437, \"E_R\": 0.3144, \"E_F1\": 0.2746, \"R_P\": 0.0292, \"R_R\": 0.0493, \"R_F1\": 0.0367, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 13.4, \"CF_pct\": 1.27, \"CF_count\": 21, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2162, \"total_pred_relations\": 1647, \"delta_vs_unconstrained\": {\"delta_E_F1\": 0.0018, \"delta_R_F1\": 0.0001, \"delta_ET\": -1.5, \"delta_RV\": 0, \"delta_DR\": -43.54, \"note\": \"Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%, ET=1.5%, RV=0%\"}}}, \"w8_ft_posthoc_baseline\": {\"metrics\": {\"ft_regime\": {\"qwen_scierc\": {\"R_F1_before\": 43.86, \"R_F1_posthoc\": 43.94, \"R_F1_constrained\": 43.77, \"reject_rate_pct\": 1.95, \"TP_lost\": 4}, \"llama_scierc\": {\"R_F1_before\": 45.45, \"R_F1_posthoc\": 45.23, \"R_F1_constrained\": 45.47, \"reject_rate_pct\": 1.11, \"TP_lost\": 5}, \"qwen_docred\": {\"R_F1_before\": 40.91, \"R_F1_posthoc\": 41.11, \"R_F1_constrained\": \"TBD\", \"reject_rate_pct\": 1.03, \"TP_lost\": 1}, \"llama_docred\": {\"R_F1_before\": 43.77, \"R_F1_posthoc\": 43.92, \"R_F1_constrained\": 44.23, \"reject_rate_pct\": 0.64, \"TP_lost\": 1}}, \"zs_regime\": {\"mistral_scierc\": {\"triples\": 1584, \"reject_pct\": 20.27, \"R_F1_before\": 0.0376, \"R_F1_posthoc\": 0.0394, \"R_F1_constrained\": 0.0367, \"TP_before\": 48, \"TP_after\": 44, \"TP_lost\": 4}, \"qwen_scierc\": {\"triples\": 1724, \"reject_pct\": 16.76, \"R_F1_before\": 0.0823, \"R_F1_posthoc\": 0.0863, \"R_F1_constrained\": 0.0836, \"TP_before\": 111, \"TP_after\": 104, \"TP_lost\": 7}, \"llama_scierc\": {\"triples\": 1274, \"reject_pct\": 13.89, \"R_F1_before\": 0.0268, \"R_F1_posthoc\": 0.0271, \"R_F1_constrained\": 0.0254, \"TP_before\": 30, \"TP_after\": 28, \"TP_lost\": 2}, \"qwen_docred\": {\"triples\": 17497, \"reject_pct\": 48.12, \"R_F1_before\": 0.0774, \"R_F1_posthoc\": 0.0961, \"R_F1_constrained\": 0.0823, \"TP_before\": 1137, \"TP_after\": 1010, \"TP_lost\": 127}, \"llama_docred\": {\"triples\": 16437, \"reject_pct\": 42.18, \"R_F1_before\": 0.0598, \"R_F1_posthoc\": 0.0744, \"R_F1_constrained\": 0.0627, \"TP_before\": 850, \"TP_after\": 802, \"TP_lost\": 48}, \"mistral_docred\": {\"triples\": 11836, \"reject_pct\": 73.73, \"R_F1_before\": 0.0434, \"R_F1_posthoc\": 0.0385, \"R_F1_constrained\": 0.0552, \"TP_before\": 518, \"TP_after\": 292, \"TP_lost\": 226, \"removed_RV\": 4172, \"removed_ET\": 3382, \"removed_DR\": 1173, \"note\": \"Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6% of TPs\"}}, \"key_finding\": \"ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation.\"}}, \"w6_mistral_docred_unconstrained\": {\"metrics\": {\"total_samples\": 998, \"parse_failures\": 7, \"parse_fail_rate\": 0.7, \"total_pred_entities\": 12580, \"total_pred_relations\": 11879, \"ET_pct\": 7.58, \"RV_pct\": 42.35, \"DR_pct\": 57.42, \"CF_pct\": 24.78, \"E_P\": 0.6221, \"E_R\": 0.3975, \"E_F1\": 0.4851, \"R_P\": 0.0447, \"R_R\": 0.0432, \"R_F1\": 0.0434, \"f1_method\": \"fuzzy_normalized\", \"f1_note\": \"Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98 additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\"}}, \"w6_mistral_docred_constrained\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 33.2, \"CF_pct\": 0.19, \"E_P\": 65.02, \"E_R\": 41.4, \"E_F1\": 50.59, \"R_P\": 5.67, \"R_R\": 5.37, \"R_F1\": 5.52, \"parse_fail_rate\": 0.8, \"total_samples\": 998, \"total_pred_entities\": 12535, \"total_pred_relations\": 11554, \"delta_vs_unconstrained\": {\"ET_pct\": -7.58, \"RV_pct\": -42.35, \"DR_pct\": -24.22, \"CF_pct\": -24.59, \"E_F1\": 2.08, \"R_F1\": 2.02}}}, \"w5_qwen_docred_lora_constrained_eval\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.01, \"CF_pct\": 0.41, \"E_F1\": 81.43, \"E_P\": 85.41, \"E_R\": 77.81, \"R_F1\": 40.56, \"R_P\": 36.35, \"R_R\": 45.86, \"parse_fail_rate\": 8.52, \"total_samples\": 998, \"success_samples\": 913, \"fail_samples\": 85, \"total_entities_pred\": 17799, \"total_relations_pred\": 15563, \"E_F1_excl_fail\": 85.69, \"R_F1_excl_fail\": 42.23, \"delta_vs_unconstrained\": {\"delta_DR\": -0.75, \"delta_RV\": -0.27, \"delta_R_F1\": -0.3, \"delta_R_F1_excl_fail\": 0.03, \"DR_reduction_pct\": 98.7, \"note\": \"Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20\"}}}, \"w5_llama_docred_sft_data_gen\": {\"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_size_mb\": 19, \"dev_size_mb\": 6.1}}, \"w1_cf_fallback_llama_docred\": {}, \"w1_cf_fallback_llama_scierc\": {}, \"w5_qwen_docred_lora_unconstrained_eval\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.27, \"DR_pct\": 0.76, \"CF_pct\": 0.12, \"E_F1\": 82.15, \"E_P\": 85.44, \"E_R\": 79.11, \"R_F1\": 40.86, \"R_P\": 36.41, \"R_R\": 46.56, \"parse_fail_rate\": 7.11, \"total_samples\": 998, \"success_samples\": 927, \"fail_samples\": 71, \"total_entities_pred\": 18091, \"total_relations_pred\": 15870, \"ET_pct_excl_fail\": 0, \"RV_pct_excl_fail\": 0.27, \"DR_pct_excl_fail\": 0.76, \"CF_pct_excl_fail\": 0.12, \"E_F1_excl_fail\": 85.72, \"E_P_excl_fail\": 85.44, \"E_R_excl_fail\": 86, \"R_F1_excl_fail\": 42.2, \"R_P_excl_fail\": 36.41, \"R_R_excl_fail\": 50.17}}, \"w5_llama_docred_lora_unconstrained_eval\": {\"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.15, \"DR_pct\": 0.49, \"E_F1\": 83.93, \"E_P\": 84.93, \"E_R\": 82.96, \"R_F1\": 43.72, \"R_P\": 38.59, \"R_R\": 50.41, \"parse_fail_rate\": 2.3, \"total_samples\": 998, \"total_entities_pred\": 19106, \"total_relations_pred\": 16171}}, \"w5_qwen_docred_lora_training\": {\"metrics\": {\"eval_loss\": 0.0614, \"eval_mean_token_accuracy\": 0.9804, \"eval_entropy\": 0.715, \"train_loss\": 0.0682, \"train_runtime_s\": 5825.6, \"epochs\": 3, \"adapter_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\", \"merged_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\"}}, \"w5_llama_docred_lora_training\": {\"metrics\": {\"train_loss\": 0.0572, \"eval_loss\": 0.0624, \"token_acc\": 98.06}}, \"w5_docred_sft_data_gen\": {\"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_entities\": 59493, \"train_relations\": 38180, \"dev_entities\": 19528, \"dev_relations\": 12275}}, \"w5_llama_lora_scierc_training\": {\"metrics\": {\"eval_loss\": 0.0595, \"eval_mean_token_accuracy\": 0.9817, \"eval_entropy\": 1.0565, \"train_loss\": 0.0501, \"train_runtime_sec\": 654.23, \"epochs\": 3, \"train_samples_per_second\": 8.08}}, \"w1_cf_fallback_docred\": {}, \"w5_lora_scierc_unconstrained_eval\": {\"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0195, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4386, \"relation_precision\": 0.4087, \"relation_recall\": 0.4733, \"total_entities\": 1784, \"total_relations\": 1128, \"domain_range_violations\": 22, \"go_nogo_metric\": 0.0195, \"dr_gate\": \"FAILED\"}}, \"llama_docred_full_s1\": {\"metrics\": {\"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"f1_method\": \"all_set\", \"violations\": {\"ET\": 0, \"RV\": 0, \"DR\": 2.55, \"CF\": 12.02}, \"f1\": {\"entity_f1\": 55.01, \"entity_precision\": 61.41, \"entity_recall\": 49.82, \"relation_f1\": 6.27, \"relation_precision\": 5.49, \"relation_recall\": 7.32}, \"counts\": {\"documents\": 998, \"documents_checked\": 907, \"parse_failures\": 91, \"unique_entities\": 11296, \"triples\": 16368}}}, \"llama_docred_unconstrained\": {\"metrics\": {\"checker_version\": \"fixed_20260514_v2\", \"f1_method\": \"all_set\", \"documents\": 998, \"documents_checked\": 930, \"parse_failures\": 68, \"unique_entities\": 11525, \"total_triples\": 16437, \"dr_eligible_triples\": 13789, \"ET_rate_pct\": 0.13, \"RV_rate_pct\": 16.03, \"DR_rate_pct\": 26.07, \"CF_rate_pct\": 0.17, \"entity_precision\": 61.22, \"entity_recall\": 51.02, \"entity_f1\": 55.65, \"relation_precision\": 5.22, \"relation_recall\": 7, \"relation_f1\": 5.98, \"fuzzy_relation_matches\": 121}}, \"phase2_docred_grammar_only\": {\"metrics\": {\"documents_checked\": 985, \"parse_failures\": 13, \"total_entities\": 20150, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.2617, \"cross_field_consistency_violation_rate\": 0.0007, \"relation_f1\": 8.31, \"relation_precision\": 7.06, \"relation_recall\": 10.12, \"entity_f1\": 59.38, \"entity_precision\": 58.47, \"entity_recall\": 60.32, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"llama_scierc_full_s1\": {\"metrics\": {\"samples\": 550, \"entities_extracted\": 2469, \"relations_extracted\": 1315, \"domain_range_violation_rate\": 0.0008, \"relation_vocab_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0656, \"total_violation_rate\": 0.0431, \"entity_f1\": 0.2349, \"entity_precision\": 0.1972, \"entity_recall\": 0.2902, \"relation_f1\": 0.0254, \"relation_precision\": 0.0221, \"relation_recall\": 0.0298, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"llama_scierc_unconstrained\": {\"metrics\": {\"entity_type_violation_rate\": 0, \"relation_vocab_violation_rate\": 0.0055, \"domain_range_violation_rate\": 0.1334, \"cross_field_consistency_violations\": 6, \"entity_f1\": 0.2356, \"entity_precision\": 0.1983, \"entity_recall\": 0.2902, \"relation_f1\": 0.0268, \"relation_precision\": 0.0236, \"relation_recall\": 0.031, \"total_entities\": 2451, \"total_relations\": 1274, \"json_parse_failures\": 1, \"samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_full_s1\": {\"metrics\": {\"total_samples\": 551, \"total_triples\": 1729, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0093, \"cross_field_consistency_violation_rate\": 0.099, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0836, \"relation_precision\": 0.0654, \"relation_recall\": 0.116, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_semantic_only\": {\"metrics\": {\"total_samples\": 551, \"total_triples\": 1726, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0151, \"domain_range_violation_rate\": 0.1165, \"cross_field_consistency_violation_rate\": 0.0271, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0815, \"relation_precision\": 0.0637, \"relation_recall\": 0.1129, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_grammar_only\": {\"metrics\": {\"total_samples\": 551, \"total_triples\": 1725, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.1484, \"cross_field_consistency_violation_rate\": 0.0008, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0823, \"relation_precision\": 0.0643, \"relation_recall\": 0.114, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_unconstrained\": {\"metrics\": {\"json_parse_rate\": 1, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0823, \"relation_precision\": 0.0644, \"relation_recall\": 0.114, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0139, \"domain_range_violation_rate\": 0.1537, \"cross_field_consistency_violation_rate\": 0.0008, \"total_triples\": 1724, \"total_entities\": 2474, \"total_samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_docred_full_s1\": {\"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20187, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.1021, \"cross_field_consistency_violation_rate\": 0.0257, \"entity_f1\": 59.37, \"entity_precision\": 58.45, \"entity_recall\": 59.63, \"relation_f1\": 8.23, \"relation_precision\": 6.99, \"relation_recall\": 10.01, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_docred_semantic_only\": {\"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20185, \"total_triples\": 17571, \"entity_type_violation_rate\": 0.0422, \"relation_vocabulary_violation_rate\": 0.2987, \"domain_range_violation_rate\": 0.1384, \"cross_field_consistency_violation_rate\": 0.0105, \"entity_f1\": 57.81, \"entity_precision\": 57.27, \"entity_recall\": 58.37, \"relation_f1\": 7.7, \"relation_precision\": 6.54, \"relation_recall\": 9.37, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.1044, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}}, \"phase2_docred_unconstrained\": {\"metrics\": {\"documents_checked\": 986, \"parse_failures\": 12, \"total_entities\": 20171, \"total_triples\": 17497, \"entity_type_violation_rate\": 0.0248, \"relation_vocabulary_violation_rate\": 0.2966, \"domain_range_violation_rate\": 0.1846, \"cross_field_consistency_violation_rate\": 0.001, \"entity_f1\": 58.15, \"entity_precision\": 57.26, \"entity_recall\": 58.32, \"relation_f1\": 7.74, \"relation_precision\": 6.55, \"relation_recall\": 9.46, \"unrecognized_relations\": 5189, \"f1_method\": \"all_set (includes OOV predictions in denominator)\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.0818, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}}, \"mvp_phase0_docred_schema_r2\": {}, \"phase2_s2_pilot50\": {\"metrics\": {\"domain_range_violation_rate\": 0.0205, \"relation_vocabulary_violation_rate\": 0, \"relation_f1\": 0.1008, \"samples\": 50, \"predicted_relations\": 146, \"true_positives\": 13, \"gold_relations\": 112, \"entity_f1_approx\": 0.29, \"note\": \"DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。\"}}, \"mvp_phase0_docred_schema\": {\"metrics\": {\"total_documents\": 998, \"documents_checked\": 943, \"parse_failures\": 55, \"json_parse_rate\": 0.9449, \"total_entities\": 19524, \"total_triples\": 16782, \"entity_type_violations\": 119, \"entity_type_violation_rate\": 0.0061, \"relation_vocabulary_violations\": 3090, \"relation_vocabulary_violation_rate\": 0.1841, \"relation_fuzzy_matches\": 85, \"domain_range_violations\": 2154, \"domain_range_violation_rate\": 0.1284, \"cross_field_consistency_violations\": 29, \"cross_field_consistency_violation_rate\": 0.0015, \"total_violations_any\": 5392, \"total_violation_rate\": 0.1485, \"go_nogo_metric_dr\": 0.1284}}, \"mvp_phase0_violation_rate_docred\": {\"metrics\": {\"total_docs\": 998, \"parsed_docs\": 962, \"json_parse_rate\": 0.964, \"total_entities\": 19099, \"total_triples\": 16540, \"entity_type_violation_rate\": 0.075, \"relation_vocabulary_violation_rate\": 0.289, \"domain_range_violation_rate\": 0.187, \"cross_field_consistency_violation_rate\": 0.0008, \"go_nogo_metric\": 0.187, \"fuzzy_matches\": 126, \"top_dr_violations_by_rate\": {\"P35_head_of_state\": 1, \"P710_participant\": 0.919, \"P172_ethnic_group\": 0.875}, \"top_dr_violations_by_count\": {\"P31_instance_of\": {\"violations\": 322, \"total\": 533, \"rate\": 0.604}, \"P1001_applies_to_jurisdiction\": {\"violations\": 264, \"total\": 594, \"rate\": 0.444}, \"P1344_participant_in\": {\"violations\": 194, \"total\": 312, \"rate\": 0.622}}}}, \"mvp_phase0_scierc_schema\": {\"metrics\": {\"domain_range_violation_rate\": 0.0578, \"relation_vocabulary_violation_rate\": 0.003, \"entity_type_violation_rate\": 0, \"total_violation_rate\": 0.0253, \"go_nogo_metric\": 0.0578, \"total_triples\": 1661, \"vs_minimal_dr_reduction\": -0.624, \"per_relation\": {\"Used-for\": {\"rate\": \"TBD\"}, \"Feature-of\": {\"delta_pp\": -22.3}, \"Part-of\": {\"delta_pp\": -22.5}, \"Compare\": {\"delta_pp\": -14.8}, \"Evaluate-for\": {\"delta_pp\": 5.8}}, \"mcnemar_all_significant\": true}}, \"mvp_phase0_violation_rate\": {\"metrics\": {\"total_triples\": 1724, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0139, \"domain_range_violation_rate\": 0.1537, \"cross_field_consistency_violation_rate\": 0.0008, \"go_nogo_metric\": 0.1537, \"entity_f1\": 0.3101, \"relation_f1\": 0.0823, \"per_relation\": {\"Used-for\": {\"total\": 787, \"dr_violations\": 6, \"rate\": 0.0076}, \"Conjunction\": {\"total\": 32, \"dr_violations\": 0, \"rate\": 0}, \"Hyponym-of\": {\"total\": 124, \"dr_violations\": 18, \"rate\": 0.1452}, \"Evaluate-for\": {\"total\": 133, \"dr_violations\": 32, \"rate\": 0.2406}, \"Part-of\": {\"total\": 72, \"dr_violations\": 18, \"rate\": 0.25}, \"Feature-of\": {\"total\": 486, \"dr_violations\": 163, \"rate\": 0.3354}, \"Compare\": {\"total\": 66, \"dr_violations\": 28, \"rate\": 0.4242}}}}}, \"count\": 162, \"total\": 162, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5165}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 77_

<details><summary>Logged reasoning block</summary>

```text
Too much data. Let me search specifically for unconstrained FT DocRED experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "f26699f8-ac6d-4f1f-bdf2-af43f5440792",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RycgPE11Lf1LZsATLBhxH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1605,
      "cache_read_input_tokens": 61754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1605
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

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01PbqqrpP7MfVDY3zCJPKqVK`</summary>

```json
{
  "command": "grep -i \"unconstrained\\|w8_qwen_docred_ft\\b\\|w8_llama_docred_ft\\b\\|w8.*docred.*ft.*unc\" /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/301ce757-b612-46ff-a757-67ed2e0aceb1/tool-results/mcp-agent-ml-research-read_registry-1779536638218.txt | head -30",
  "description": "Search registry dump for unconstrained FT DocRED experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "f1e93b5c-111b-411a-964d-e7644f838005",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RycgPE11Lf1LZsATLBhxH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1605,
      "cache_read_input_tokens": 61754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1605
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

_source line 79 · 2026-05-23T11:44:02.656Z_

<details><summary>↩ Tool result · `toolu_01PbqqrpP7MfVDY3zCJPKqVK`</summary>

```text
&lt;persisted-output>
Output too large (63KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/301ce757-b612-46ff-a757-67ed2e0aceb1/tool-results/b7h6s3r4u.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"sf2_70b_prompt_sensitivity\": {\"metrics\": {\"minimal_con\": {\"E_F1\": 37.22, \"R_F1\": 11.35, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.62}, \"minimal_unc\": {\"E_F1\": 37.51, \"R_F1\": 13.42, \"ET_pct\": 0.27, \"RV_pct\": 5.88, \"DR_pct\": 0.22, \"CF_pct\": 0}, \"detailed_con\": {\"E_F1\": 40.35, \"R_F1\": 11.16, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.75}, \"detailed_unc\": {\"E_F1\": 40.42, \"R_F1\": 11.12, \"ET_pct\": 0, \"RV_pct\": 0.26, \"DR_pct\": 4.57, \"CF_pct\": 0}}}, \"eval_70b_lora_docred_200_full_s2\": {\"metrics\": {\"R_F1\": 36.45, \"R_P\": 31.25, \"R_R\": 43.72, \"E_F1\": 84.96, \"E_P\": 84.6, \"E_R\": 85.34, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 13, \"CF_pct\": 0.34, \"parse_fail_pct\": 0, \"pred_entities\": 3819, \"pred_relations\": 3546, \"entity_tp\": 3218, \"entity_fp\": 586, \"entity_fn\": 553, \"relation_tp\": 1104, \"relation_fp\": 2429, \"relation_fn\": 1421}}, \"sf2_qwen_int4_docred_s1\": {\"metrics\": {\"total_samples\": 200, \"parse_failures\": 37, \"parse_fail_pct\": 18.5, \"total_entities_pred\": 2985, \"total_relations_pred\": 2385, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.1, \"E_P\": 84.87, \"E_R\": 66.93, \"E_F1\": 74.84, \"R_P\": 41.59, \"R_R\": 38.65, \"R_F1\": 40.07, \"et_violations\": 0, \"rv_violations\": 0, \"dr_violations\": 0, \"cf_violations\": 3}}, \"sf2_llama_int4_docred_s1\": {\"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.22, \"R-F1\": 48.04, \"E-F1\": 84.18, \"R-P\": 44.79, \"R-R\": 51.8, \"E-P\": 85.5, \"E-R\": 82.9, \"samples\": 200, \"parse_fail\": 5, \"parse_fail_pct\": 2.5, \"entities_pred\": 3669, \"relations_pred\": 2997}}, \"sf2_llama_int4_scierc_s1\": {\"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}}, \"sf2_qwen_int4_scierc_s1\": 
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "fb670cfd-a6c3-4f8c-a9d9-22f1b1ca1f50",
  "tool_use_result": {
    "stdout": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"sf2_70b_prompt_sensitivity\\\": {\\\"metrics\\\": {\\\"minimal_con\\\": {\\\"E_F1\\\": 37.22, \\\"R_F1\\\": 11.35, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.62}, \\\"minimal_unc\\\": {\\\"E_F1\\\": 37.51, \\\"R_F1\\\": 13.42, \\\"ET_pct\\\": 0.27, \\\"RV_pct\\\": 5.88, \\\"DR_pct\\\": 0.22, \\\"CF_pct\\\": 0}, \\\"detailed_con\\\": {\\\"E_F1\\\": 40.35, \\\"R_F1\\\": 11.16, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.75}, \\\"detailed_unc\\\": {\\\"E_F1\\\": 40.42, \\\"R_F1\\\": 11.12, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.26, \\\"DR_pct\\\": 4.57, \\\"CF_pct\\\": 0}}}, \\\"eval_70b_lora_docred_200_full_s2\\\": {\\\"metrics\\\": {\\\"R_F1\\\": 36.45, \\\"R_P\\\": 31.25, \\\"R_R\\\": 43.72, \\\"E_F1\\\": 84.96, \\\"E_P\\\": 84.6, \\\"E_R\\\": 85.34, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 13, \\\"CF_pct\\\": 0.34, \\\"parse_fail_pct\\\": 0, \\\"pred_entities\\\": 3819, \\\"pred_relations\\\": 3546, \\\"entity_tp\\\": 3218, \\\"entity_fp\\\": 586, \\\"entity_fn\\\": 553, \\\"relation_tp\\\": 1104, \\\"relation_fp\\\": 2429, \\\"relation_fn\\\": 1421}}, \\\"sf2_qwen_int4_docred_s1\\\": {\\\"metrics\\\": {\\\"total_samples\\\": 200, \\\"parse_failures\\\": 37, \\\"parse_fail_pct\\\": 18.5, \\\"total_entities_pred\\\": 2985, \\\"total_relations_pred\\\": 2385, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.1, \\\"E_P\\\": 84.87, \\\"E_R\\\": 66.93, \\\"E_F1\\\": 74.84, \\\"R_P\\\": 41.59, \\\"R_R\\\": 38.65, \\\"R_F1\\\": 40.07, \\\"et_violations\\\": 0, \\\"rv_violations\\\": 0, \\\"dr_violations\\\": 0, \\\"cf_violations\\\": 3}}, \\\"sf2_llama_int4_docred_s1\\\": {\\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.22, \\\"R-F1\\\": 48.04, \\\"E-F1\\\": 84.18, \\\"R-P\\\": 44.79, \\\"R-R\\\": 51.8, \\\"E-P\\\": 85.5, \\\"E-R\\\": 82.9, \\\"samples\\\": 200, \\\"parse_fail\\\": 5, \\\"parse_fail_pct\\\": 2.5, \\\"entities_pred\\\": 3669, \\\"relations_pred\\\": 2997}}, \\\"sf2_llama_int4_scierc_s1\\\": {\\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.94, \\\"R-F1\\\": 43.98, \\\"E-F1\\\": 67.54, \\\"samples\\\": 551, \\\"R-P\\\": 40.47, \\\"R-R\\\": 48.15, \\\"E-P\\\": 65.51, \\\"E-R\\\": 69.7}}, \\\"sf2_qwen_int4_scierc_s1\\\": {\\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 1.1, \\\"R-F1\\\": 41.71, \\\"E-F1\\\": 67.05, \\\"samples\\\": 551, \\\"R-P\\\": 38.52, \\\"R-R\\\": 45.48, \\\"E-P\\\": 64.76, \\\"E-R\\\": 69.52}}, \\\"sf2_gollie_scierc_violation\\\": {\\\"metrics\\\": {\\\"GoLLIE_ZS\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.83, \\\"E_F1\\\": 9.17, \\\"R_F1\\\": 0, \\\"pred_ents\\\": 241, \\\"pred_rels\\\": 5, \\\"docs_with_output\\\": 54}, \\\"OntoCoDec_Qwen_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.61, \\\"E_F1\\\": 66.43, \\\"R_F1\\\": 43.69}, \\\"OntoCoDec_Llama_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.62, \\\"E_F1\\\": 67.09, \\\"R_F1\\\": 45.47}}}, \\\"eval_70b_zs_docred_200_full_s1\\\": {\\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 5.34, \\\"E-F1\\\": 70.05, \\\"R-F1\\\": 13.25, \\\"PF%\\\": 0, \\\"entities_pred\\\": 3234, \\\"relations_pred\\\": 2637, \\\"triples_checked\\\": 2642}}, \\\"eval_70b_lora_docred_200_grammar_only\\\": {\\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 10.5, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.38, \\\"CF_pct\\\": 0.06, \\\"E_F1\\\": 80.13, \\\"E_P\\\": 85.16, \\\"E_R\\\": 75.66, \\\"R_F1\\\": 43.96, \\\"R_P\\\": 39.78, \\\"R_R\\\": 49.11, \\\"entities_pred\\\": 3362, \\\"relations_pred\\\": 3154}}, \\\"eval_70b_lora_docred_200_semantic_only\\\": {\\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 11, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.51, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.21, \\\"E_F1\\\": 80.06, \\\"E_P\\\": 85.21, \\\"E_R\\\": 75.5, \\\"R_F1\\\": 43.61, \\\"R_P\\\": 39.44, \\\"R_R\\\": 48.75, \\\"entities_pred\\\": 3351, \\\"relations_pred\\\": 3148}}, \\\"eval_70b_zs_docred_200_unconstrained\\\": {\\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities_pred\\\": 3242, \\\"relations_pred\\\": 2637, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 7.88, \\\"DR_pct\\\": 13.45, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 8, \\\"E_F1\\\": 70.14, \\\"E_P\\\": 75.85, \\\"E_R\\\": 65.23, \\\"R_F1\\\": 13.25, \\\"R_P\\\": 12.97, \\\"R_R\\\": 13.54}}, \\\"eval_70b_zs_docred_200_grammar_only\\\": {\\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 1, \\\"entities_pred\\\": 3221, \\\"relations_pred\\\": 2609, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 17.03, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"E_F1\\\": 70.12, \\\"E_P\\\": 75.88, \\\"E_R\\\": 65.17, \\\"R_F1\\\": 13.23, \\\"R_P\\\": 12.99, \\\"R_R\\\": 13.47}}, \\\"eval_70b_zs_docred_200_semantic_only\\\": {\\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities\\\": 3240, \\\"relations\\\": 2596, \\\"ET_pct\\\": 0.12, \\\"RV_pct\\\": 8.24, \\\"DR_pct\\\": 1.66, \\\"CF_count\\\": 132, \\\"CF_pct\\\": 4.07, \\\"E_F1\\\": 70.1, \\\"E_P\\\": 75.87, \\\"E_R\\\": 65.15, \\\"R_F1\\\": 13.05, \\\"R_P\\\": 12.88, \\\"R_R\\\": 13.23, \\\"fuzzy_matches\\\": 8}}, \\\"eval_70b_lora_docred_200_beam4_s1\\\": {\\\"metrics\\\": {\\\"E-F1\\\": 85.57, \\\"E-P\\\": 85.45, \\\"E-R\\\": 85.68, \\\"R-F1\\\": 48.14, \\\"R-P\\\": 44.24, \\\"R-R\\\": 52.79, \\\"ET%\\\": 0, \\\"RV%\\\": 0, \\\"DR%\\\": 0, \\\"CF%\\\": 0, \\\"parse_fail\\\": \\\"1/200 (0.5%)\\\", \\\"entities_pred\\\": 3790, \\\"relations_pred\\\": 3030}}, \\\"eval_70b_lora_scierc_grammar_only\\\": {\\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"json_failure_rate\\\": 0, \\\"entities\\\": 1805, \\\"relations\\\": 1133, \\\"entity_type_violations\\\": 0, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocab_violations\\\": 0, \\\"relation_vocab_violation_rate\\\": 0, \\\"domain_range_violations\\\": 17, \\\"domain_range_violation_rate\\\": 0.015, \\\"cross_field_consistency_violations\\\": 0, \\\"fuzzy_relation_matches\\\": 0, \\\"entity_P\\\": 0.6272, \\\"entity_R\\\": 0.6707, \\\"entity_F1\\\": 0.6482, \\\"relation_P\\\": 0.4152, \\\"relation_R\\\": 0.4825, \\\"relation_F1\\\": 0.4463}}, \\\"eval_70b_zs_scierc_unconstrained\\\": {\\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 2353, \\\"relations\\\": 1483, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.6, \\\"DR_pct\\\": 6.4, \\\"CF_count\\\": 0, \\\"E_F1\\\": 35.22, \\\"E_P\\\": 30.13, \\\"E_R\\\": 42.38, \\\"R_F1\\\": 11.23, \\\"R_P\\\": 9.31, \\\"R_R\\\": 14.17, \\\"parse_fail_pct\\\": 0}}, \\\"eval_70b_lora_scierc_full_s2\\\": {\\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1531, \\\"relations\\\": 1027, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 18, \\\"E_F1\\\": 62.35, \\\"E_P\\\": 65.44, \\\"E_R\\\": 59.53, \\\"R_F1\\\": 36.28, \\\"R_P\\\": 35.35, \\\"R_R\\\": 37.27, \\\"parse_fail_pct\\\": 0}}, \\\"eval_70b_lora_scierc_semantic_only\\\": {\\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1806, \\\"relations\\\": 1133, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.6, \\\"CF_count\\\": 9, \\\"E_F1\\\": 64.86, \\\"E_P\\\": 62.74, \\\"E_R\\\": 67.12, \\\"R_F1\\\": 44.73, \\\"R_P\\\": 41.61, \\\"R_R\\\": 48.36, \\\"parse_fail_pct\\\": 0}}, \\\"entity_order_ablation_qwen_scierc\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 67.05, \\\"E_P\\\": 65.23, \\\"E_R\\\": 68.98, \\\"R_F1\\\": 43.77, \\\"R_P\\\": 40.78, \\\"R_R\\\": 47.23, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 21, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1784, \\\"relations\\\": 1128, \\\"corrected_original_R_F1\\\": 43.77, \\\"corrected_original_E_F1\\\": 67.05, \\\"corrected_original_DR_pct\\\": 0, \\\"corrected_original_CF_count\\\": 21, \\\"corrected_delta_R_F1\\\": 0, \\\"corrected_delta_E_F1\\\": 0, \\\"raw_output_identical\\\": true, \\\"parsed_output_identical\\\": true, \\\"note\\\": \\\"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\\\"}}, \\\"eval_70b_zs_scierc_semantic_only\\\": {\\\"metrics\\\": {\\\"R_F1\\\": 11.37, \\\"DR_pct\\\": 1.01, \\\"RV_pct\\\": 0.6, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 76, \\\"samples\\\": 551}}, \\\"eval_70b_zs_scierc_grammar_only\\\": {\\\"metrics\\\": {\\\"R_F1\\\": 11.23, \\\"DR_pct\\\": 6.33, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 0, \\\"samples\\\": 551}}, \\\"eval_70b_lora_scierc_beam4_s1\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 64.89, \\\"E_P\\\": 62.29, \\\"E_R\\\": 67.72, \\\"R_F1\\\": 44.81, \\\"R_P\\\": 39.45, \\\"R_R\\\": 51.85, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 1, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1839, \\\"relations\\\": 1283}}, \\\"tcr_beam4_llama_scierc\\\": {\\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1803, \\\"relations\\\": 1194, \\\"entity_type_violations\\\": \\\"0/1803 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1194 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"13/1194 (1.1%)\\\", \\\"cross_field_consistency\\\": 0, \\\"DR_pct\\\": 1.09, \\\"E_F1\\\": 68.02, \\\"E_P\\\": 65.88, \\\"E_R\\\": 70.29, \\\"R_F1\\\": 46.05, \\\"R_P\\\": 41.83, \\\"R_R\\\": 51.23, \\\"tcr_changed_selection\\\": \\\"0/551 (0.0%)\\\"}}, \\\"tcr_beam4_qwen_scierc\\\": {\\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1802, \\\"relations\\\": 1250, \\\"entity_type_violations\\\": \\\"0/1802 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1250 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"23/1250 (1.8%)\\\", \\\"cross_field_consistency_violations\\\": 1, \\\"DR_pct\\\": 1.84, \\\"E_P\\\": 65.05, \\\"E_R\\\": 69.64, \\\"E_F1\\\": 67.26, \\\"R_P\\\": 39.36, \\\"R_R\\\": 50.51, \\\"R_F1\\\": 44.24, \\\"TCR_changed_selection\\\": \\\"0/551 (0.0%)\\\", \\\"all_candidates_TCR_1.0\\\": true}}, \\\"vllm_guided_json_scierc_zs\\\": {\\\"metrics\\\": {\\\"DR%\\\": 15.26, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.04, \\\"R-F1\\\": 8.75, \\\"E-F1\\\": 30.91, \\\"parse_fail%\\\": 0, \\\"total_samples\\\": 551, \\\"total_entities\\\": 2485, \\\"total_relations\\\": 1724, \\\"inference_time_s\\\": 108.5}}, \\\"eval_70b_lora_docred_200_s1_constrained\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 79.38, \\\"E_P\\\": 85.24, \\\"E_R\\\": 74.28, \\\"R_F1\\\": 43.95, \\\"R_P\\\": 40.48, \\\"R_R\\\": 48.08, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.18, \\\"parse_fail_pct\\\": 12.5, \\\"samples\\\": 200}}, \\\"d066_beam_sweep\\\": {\\\"metrics\\\": {\\\"scierc_qwen3_8b\\\": {\\\"k1_unc\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 2.11, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.494}, \\\"k1_con\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.5, \\\"avg_time\\\": 2.932}, \\\"k2_unc\\\": {\\\"E_F1\\\": 67.79, \\\"R_F1\\\": 44.75, \\\"DR_pct\\\": 1.54, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.954}, \\\"k2_con\\\": {\\\"E_F1\\\": 67.71, \\\"R_F1\\\": 44.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.11, \\\"avg_time\\\": 3.463}, \\\"k4_unc\\\": {\\\"E_F1\\\": 67.49, \\\"R_F1\\\": 43.72, \\\"DR_pct\\\": 1.89, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 3.485}, \\\"k4_con\\\": {\\\"E_F1\\\": 67.22, \\\"R_F1\\\": 43.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.069}, \\\"k8_unc\\\": {\\\"E_F1\\\": 66.4, \\\"R_F1\\\": 43.17, \\\"DR_pct\\\": 1.77, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.194}, \\\"k8_con\\\": {\\\"E_F1\\\": 66.36, \\\"R_F1\\\": 43.65, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 5.058}}, \\\"pareto_optimal\\\": \\\"k=2 con\\\", \\\"best_E_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 67.79}, \\\"best_R_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 44.75}}}, \\\"w8_llama_docred_ft_grammar_only\\\": {\\\"metrics\\\": {\\\"R_F1\\\": 43.72, \\\"R_P\\\": 38.57, \\\"R_R\\\": 50.44, \\\"parse_fail_pct\\\": 2.3, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\\\"}}, \\\"w8_llama_docred_ft_semantic_only\\\": {\\\"metrics\\\": {\\\"R_F1\\\": 43.85, \\\"R_P\\\": 38.85, \\\"R_R\\\": 50.31, \\\"parse_fail_pct\\\": 2.4, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\\\"}}, \\\"w8_qwen_docred_ft_semantic_only\\\": {\\\"metrics\\\": {\\\"R_F1\\\": 40.85, \\\"R_P\\\": 36.33, \\\"R_R\\\": 46.65, \\\"parse_fail_pct\\\": 7.52, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\\\"}}, \\\"r16_trie_qwen_ft_scierc\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 64.4, \\\"E_P\\\": 66.8, \\\"E_R\\\": 62.16, \\\"R_F1\\\": 41.16, \\\"R_P\\\": 38.24, \\\"R_R\\\": 44.56, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 95.5, \\\"CF_pct\\\": 0.09, \\\"parse_fail_pct\\\": 9.1, \\\"samples\\\": 551, \\\"note\\\": \\\"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\\\"}}, \\\"r16_trie_llama_ft_scierc\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 36.66, \\\"E_P\\\": 67.47, \\\"E_R\\\": 25.16, \\\"R_F1\\\": 19.95, \\\"R_P\\\": 41.42, \\\"R_R\\\": 13.14, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 15.2, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 50.8, \\\"samples\\\": 551, \\\"note\\\": \\\"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\\\"}}, \\\"eval_70b_lora_docred_200_unconstrained\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 80.34, \\\"E_P\\\": 85.13, \\\"E_R\\\": 76.05, \\\"R_F1\\\": 43.8, \\\"R_P\\\": 39.6, \\\"R_R\\\": 48.99, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.57, \\\"DR_pct\\\": 0.22, \\\"CF_pct\\\": 0.06, \\\"parse_fail_pct\\\": 10, \\\"samples\\\": 200, \\\"relations\\\": 3159, \\\"RV_count\\\": 18, \\\"DR_count\\\": 7, \\\"CF_count\\\": 2}}, \\\"eval_70b_lora_scierc_s1_constrained\\\": {\\\"metrics\\\": {\\\"entity_f1\\\": 0.6476, \\\"entity_precision\\\": 0.6266, \\\"entity_recall\\\": 0.6701, \\\"relation_f1\\\": 0.4453, \\\"relation_precision\\\": 0.4149, \\\"relation_recall\\\": 0.4805, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 15, \\\"parse_fail_pct\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"num_samples\\\": 551, \\\"num_entities\\\": 1805, \\\"num_relations\\\": 1129}}, \\\"eval_70b_lora_scierc_unconstrained\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 64.86, \\\"E_P\\\": 62.74, \\\"E_R\\\": 67.12, \\\"R_F1\\\": 44.73, \\\"R_P\\\": 41.61, \\\"R_R\\\": 48.36, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 1.5, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1806, \\\"relations\\\": 1133}}, \\\"r16_70b_docred_zs_s1\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 69.11, \\\"R_F1\\\": 13.05, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.04, \\\"parse_fail_pct\\\": 0.1, \\\"samples\\\": 998, \\\"total_entities\\\": 16599, \\\"total_triples\\\": 13239, \\\"baseline_unc_DR_pct\\\": 14.98, \\\"baseline_unc_R_F1\\\": 13.01, \\\"note\\\": \\\"Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\\\"}}, \\\"d066_sweep_llama_beam8_unc\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 85.77, \\\"E_P\\\": 85.7, \\\"E_R\\\": 85.84, \\\"R_F1\\\": 51.97, \\\"R_P\\\": 49.76, \\\"R_R\\\": 54.38, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.05, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.07, \\\"parse_fail_pct\\\": 0.5, \\\"total_samples\\\": 200, \\\"total_entities_pred\\\": 3788, \\\"total_relations_pred\\\": 2779}}, \\\"d066_sweep_llama_beam2_s1\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 85.6, \\\"E_P\\\": 85.29, \\\"E_R\\\": 85.92, \\\"R_F1\\\": 51.17, \\\"R_P\\\": 48.51, \\\"R_R\\\": 54.14, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"parse_fail_pct\\\": 0.5, \\\"total_samples\\\": 200, \\\"total_entities_pred\\\": 3814, \\\"total_relations_pred\\\": 2839}}, \\\"d066_sweep_llama_docred_beam4_s1\\\": {\\\"metrics\\\": {\\\"E-F1\\\": 85.61, \\\"E-P\\\": 85.48, \\\"E-R\\\": 85.73, \\\"R-F1\\\": 51.89, \\\"R-P\\\": 51.59, \\\"R-R\\\": 52.2, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"PF_pct\\\": 0.5, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"samples\\\": 200, \\\"parse_fail\\\": 1}}, \\\"r16_70b_lora_docred\\\": {\\\"metrics\\\": {\\\"eval_loss\\\": 0.0635, \\\"token_acc\\\": 97.94, \\\"steps_completed\\\": 1146, \\\"epochs\\\": 3, \\\"train_loss_start\\\": 0.147, \\\"train_loss_end\\\": 0.056}}, \\\"r16_70b_lora_scierc\\\": {\\\"metrics\\\": {\\\"eval_loss\\\": 0.0611, \\\"token_acc\\\": 97.78, \\\"steps_completed\\\": 663, \\\"epochs\\\": 3, \\\"train_loss_start\\\": 0.183, \\\"train_loss_end\\\": 0.041}}, \\\"r16_70b_scierc_zs_s1\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 35.19, \\\"R_F1\\\": 11.24, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 3.5, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"baseline_unc_E_F1\\\": 35.21, \\\"baseline_unc_R_F1\\\": 11.15, \\\"baseline_unc_DR_pct\\\": 6.41, \\\"baseline_unc_RV_pct\\\": 0.61, \\\"baseline_unc_CF_pct\\\": 0}}, \\\"r14_qwen_docred_beam4_998\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 58.19, \\\"R_F1\\\": 8.72, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 4.94, \\\"parse_fail_pct\\\": 3.51, \\\"samples\\\": 998, \\\"success\\\": 963, \\\"fail\\\": 35}}, \\\"r16_trie_llama_zs_scierc\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 23.23, \\\"R_F1\\\": 2.9, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 84.4, \\\"CF_pct\\\": 0.36, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551}}, \\\"r16_trie_qwen_zs_scierc\\\": {\\\"metrics\\\": {\\\"E_F1\\\": 30.97, \\\"R_F1\\\": 8.64, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 29.3, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551}}, \\\"r14_llama_docred_beam4_998\\\": {\\\"metrics\\\": {\\\"R_F1\\\": 8.83, \\\"E_F1\\\": 57.81, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 1, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"parse_fail_pct\\\": 3.91, \\\"samples\\\": 998, \\\"success\\\": 959, \\\"fail\\\": 39, \\\"baseline_ZS_greedy_R_F1\\\": 6.27, \\\"baseline_ZS_greedy_E_F1\\\": 54.93, \\\"baseline_ZS_greedy_DR_pct\\\": 2.55, \\\"baseline_ZS_greedy_CF_pct\\\": 8.54}}, \\\"d066_sweep_llama_scierc_beam8_s1_551\\\": {\\\"metrics\\\": {\\\"E-F1\\\": 67.51, \\\"E-P\\\": 64.99, \\\"E-R\\\": 70.23, \\\"R-F1\\\": 44.95, \\\"R-P\\\": 40.1, \\\"R-R\\\": 51.13, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"PF_pct\\\": 0, \\\"samples\\\": 551, \\\"note\\\": \\\"Reconcile false positive corrected. Eval with --dataset scierc confirmed.\\\"}}, \\\"d066_sweep_llama_scierc_beam4_s1_551\\\": {\\\"metrics\\\": {\\\"E-F1\\\": 68.06, \\\"E-P\\\": 65.96, \\\"E-R\\\": 70.29, \\\"R-F1\\\": 46.18, \\\"R-P\\\": 42.1, \\\"R-R\\\": 51.13, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"parse_fail\\\": 0, \\\"samples\\\": 551, \\\"note\\\": \\\"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\\\"}}, \\\"d066_sweep_llama_docred_beam4_unc\\\": {\\\"metrics\\\": {\\\"E-F1\\\": 85.67, \\\"R-F1\\\": 52.65, \\\"DR_pct\\\": 0.04, \\\"CF_pct\\\": 0.08, \\\"PF_pct\\\": 0.5, \\\"samples\\\": 200}}, \\\"d066_sweep_llama_docred_beam1_s1\\\": {\\\"metrics\\\": {\\\"E-F1\\\": 85.43, \\\"R-F1\\\": 47.35, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.19, \\\"PF_pct\\\": 2, \\\"samples\\\": 200}}, \\\"d066_sweep_llama_beam8_s1\\\": {\\\"metrics\\\": {\\\"E-F1\\\": 85.76, \\\"R-F1\\\": 51.74, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"PF_pct\\\": 0.5, \\\"samples\\\": 200}}, \\\"d065_qwen_greedy_4096_r2\\\": {\\\"metrics\\\": {\\\"E-F1\\\": 81.87, \\\"R-F1\\\": 40.79, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.22, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"PF_pct\\\": 8.52, \\\"samples\\\": 998}}, \\\"d066_sweep_llama_scierc_beam2_s1_551\\\": {\\\"metrics\\\": {\\\"entity_f1\\\": 68.34, \\\"entity_p\\\": 66.59, \\\"entity_r\\\": 70.17, \\\"relation_f1\\\": 46.12, \\\"relation_p\\\": 42.73, \\\"relation_r\\\": 50.1, \\\"parse_fail_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.17, \\\"note\\\": \\\"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\\\"}}, \\\"d066_sweep_llama_scierc_beam1_unc\\\": {\\\"metrics\\\": {\\\"total\\\": 275, \\\"success\\\": 275, \\\"fail\\\": 0, \\\"output_file\\\": \\\"llama_scierc_beam1_unconstrained.jsonl\\\", \\\"note\\\": \\\"INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\\\"}}, \\\"d066_sweep_llama_docred_beam1_unc\\\": {\\\"metrics\\\": {\\\"total\\\": 200, \\\"success\\\": 196, \\\"fail\\\": 4, \\\"output_file\\\": \\\"llama_docred_200_beam1_unconstrained.jsonl\\\"}}, \\\"d066_sweep_21461_gpu1\\\": {\\\"metrics\\\": {\\\"total\\\": 551, \\\"E_F1\\\": 66.36, \\\"R_F1\\\": 43.65, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"avg_time_s\\\": 5.058, \\\"output_file\\\": \\\"qwen_scierc_beam8_full_s1.jsonl\\\", \\\"note\\\": \\\"Actually ran on SciERC 551 docs (not DocRED 200 as originally recorded in hypothesis)\\\"}}, \\\"w5_llama_docred_lora_constrained_eval\\\": {\\\"metrics\\\": {\\\"total\\\": 998, \\\"parse_failures\\\": 25, \\\"parse_fail_rate\\\": 2.51, \\\"entities\\\": 19077, \\\"relations\\\": 16074, \\\"entity_f1\\\": 83.94, \\\"entity_precision\\\": 85, \\\"entity_recall\\\": 84.13, \\\"relation_f1_all_set\\\": 43.78, \\\"relation_precision_all_set\\\": 38.79, \\\"relation_recall_all_set\\\": 50.81, \\\"et_violations\\\": 0, \\\"et_violation_rate\\\": 0, \\\"rv_violations\\\": 0, \\\"rv_violation_rate\\\": 0, \\\"dr_violations\\\": 33, \\\"dr_violation_rate\\\": 0.21, \\\"CF_pct\\\": 0.21, \\\"delta_vs_unconstrained\\\": {\\\"delta_e_f1\\\": 0.01, \\\"delta_r_f1\\\": 0.06, \\\"delta_dr\\\": -0.28, \\\"note\\\": \\\"Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20.\\\"}, \\\"provenance\\\": \\\"eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.\\\"}}, \\\"d066_sweep_16980_gpu1\\\": {}, \\\"d065_qwen_greedy_4096\\\": {}, \\\"d066_docred_beam_sweep\\\": {}, \\\"d067_seed_variance\\\": {\\\"metrics\\\": {\\\"qwen_scierc_unc\\\": {\\\"E_F1\\\": \\\"66.94 ± 0.08\\\", \\\"R_F1\\\": \\\"43.25 ± 0.43\\\", \\\"DR\\\": \\\"2.06 ± 0.08\\\", \\\"CF\\\": \\\"0.00 ± 0.00\\\"}, \\\"qwen_scierc_con\\\": {\\\"E_F1\\\": \\\"66.94 ± 0.08\\\", \\\"R_F1\\\": \\\"43.22 ± 0.39\\\", \\\"DR\\\": \\\"0.00 ± 0.00\\\", \\\"CF\\\": \\\"0.48 ± 0.02\\\"}, \\\"llama_scierc_unc\\\": {\\\"E_F1\\\": \\\"67.99 ± 0.16\\\", \\\"R_F1\\\": \\\"45.38 ± 0.05\\\", \\\"DR\\\": \\\"1.04 ± 0.05\\\", \\\"CF\\\": \\\"0.00 ± 0.00\\\"}, \\\"llama_scierc_con\\\": {\\\"E_F1\\\": \\\"67.99 ± 0.16\\\", \\\"R_F1\\\": \\\"45.40 ± 0.05\\\", \\\"DR\\\": \\\"0.03 ± 0.04\\\", \\\"CF\\\": \\\"0.26 ± 0.02\\\"}, \\\"max_sigma_pp\\\": 0.43, \\\"greedy_deterministic\\\": true, \\\"snr_dr_improvement\\\": \\\">12x\\\", \\\"qwen_docred_status\\\": \\\"pending (not started)\\\", \\\"llama_scierc_seed456_con_status\\\": \\\"running (407/551)\\\"}}, \\\"d068_constraint_guided_beam_pilot\\\": {}, \\\"d064_docred_full_beam\\\": {}, \\\"d065_tcr_full\\\": {\\\"metrics\\\": {\\\"configs_tested\\\": 10, \\\"all_cf_eliminated\\\": true, \\\"scierc_all_dr_delta_max\\\": 0.28, \\\"docred_lora_dr_delta_max\\\": 0.14, \\\"docred_zs_llama_dr_delta\\\": 9.38, \\\"docred_zs_70b_dr_delta\\\": 4.2, \\\"docred_zs_qwen_dr_delta\\\": 1.53, \\\"fund_conflict_scierc_max\\\": 2.04, \\\"fund_conflict_docred_zs_max\\\": 22.78, \\\"fund_conflict_docred_lora_max\\\": 12.16, \\\"lora_ef1_cost_max\\\": 0.0075, \\\"zs_docred_ef1_cost_max\\\": 0.0598}}, \\\"d065_tcr_pilot\\\": {\\\"metrics\\\": {\\\"scierc_zs_qwen\\\": {\\\"cf_before\\\": 9.75, \\\"cf_after\\\": 0, \\\"dr_before\\\": 0.93, \\\"dr_after\\\": 1.21, \\\"ef1_delta\\\": -0.0129, \\\"fund_pct\\\": 2.04}, \\\"scierc_zs_llama\\\": {\\\"cf_before\\\": 6.4, \\\"cf_after\\\": 0, \\\"dr_before\\\": 0.08, \\\"dr_after\\\": 0.3, \\\"ef1_delta\\\": -0.0178, \\\"fund_pct\\\": 1.85}, \\\"scierc_lora_qwen\\\": {\\\"cf_before\\\": 1.19, \\\"cf_after\\\": 0, \\\"dr_before\\\": 0, \\\"dr_after\\\": 0, \\\"ef1_delta\\\": -0.0075, \\\"fund_pct\\\": 0}, \\\"scierc_lora_llama\\\": {\\\"cf_before\\\": 0.46, \\\"cf_after\\\": 0, \\\"dr_before\\\": 0.09, \\\"dr_after\\\": 0.09, \\\"ef1_delta\\\": -0.0018, \\\"fund_pct\\\": 0}, \\\"scierc_zs_mistral\\\": {\\\"cf_before\\\": 0.67, \\\"cf_after\\\": 0, \\\"dr_before\\\": 13.36, \\\"dr_after\\\": 12.87, \\\"ef1_delta\\\": 0.0005, \\\"fund_pct\\\": 0}, \\\"docred_zs_qwen\\\": {\\\"cf_before\\\": 13.11, \\\"cf_after\\\": 0, \\\"dr_before\\\": 10.21, \\\"dr_after\\\": 11.74, \\\"ef1_delta\\\": -0.0344, \\\"fund_pct\\\": 13.52}, \\\"docred_zs_llama\\\": {\\\"cf_before\\\": 23.71, \\\"cf_after\\\": 0, \\\"dr_before\\\": 2.55, \\\"dr_after\\\": 11.93, \\\"ef1_delta\\\": -0.0521, \\\"fund_pct\\\": 22.78}, \\\"docred_zs_70b\\\": {\\\"cf_before\\\": 11.61, \\\"cf_after\\\": 0, \\\"dr_before\\\": 0, \\\"dr_after\\\": 4.2, \\\"ef1_delta\\\": -0.0598, \\\"fund_pct\\\": 18.26}, \\\"docred_lora_qwen\\\": {\\\"cf_before\\\": 0.42, \\\"cf_after\\\": 0, \\\"dr_before\\\": 0.01, \\\"dr_after\\\": 0.14, \\\"ef1_delta\\\": -0.0016, \\\"fund_pct\\\": 12.16}, \\\"docred_lora_llama\\\": {\\\"cf_before\\\": 0.36, \\\"cf_after\\\": 0, \\\"dr_before\\\": 0.21, \\\"dr_after\\\": 0.2, \\\"ef1_delta\\\": -0.0017, \\\"fund_pct\\\": 11.59}, \\\"total_configs\\\": 10, \\\"all_cf_eliminated\\\": true}}, \\\"d063_gollie_violation_rate\\\": {\\\"metrics\\\": {\\\"gollie_DR\\\": 0, \\\"gollie_RV\\\": 0, \\\"gollie_ET\\\": 0, \\\"gollie_CF\\\": 0.67, \\\"gollie_entities\\\": 300, \\\"gollie_relations\\\": 7, \\\"gollie_empty_docs_pct\\\": 45, \\\"docs_tested\\\": 100}}, \\\"d062_full_ft_scierc\\\": {\\\"metrics\\\": {\\\"unconstrained\\\": {\\\"entity_f1\\\": 0.6478, \\\"relation_f1\\\": 0.3789, \\\"DR_pct\\\": 2.74, \\\"RV_pct\\\": 0.18, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0}, \\\"constrained\\\": {\\\"entity_f1\\\": 0.6478, \\\"relation_f1\\\": 0.3789, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 1.31}, \\\"training\\\": {\\\"eval_loss_final\\\": 0.09459, \\\"epochs\\\": 3, \\\"total_steps\\\": 333, \\\"training_time\\\": \\\"21m49s\\\"}}}, \\\"d062_beam_latency\\\": {\\\"metrics\\\": {\\\"beam4_unconstrained_s_per_doc\\\": 3.446, \\\"beam4_constrained_s_per_doc\\\": 4.013, \\\"beam4_unconstrained_total_s\\\": 1898.7, \\\"beam4_constrained_total_s\\\": 2211, \\\"beam_greedy_ratio_unconstrained\\\": 1.319, \\\"beam_greedy_ratio_constrained\\\": 1.397, \\\"constraint_overhead_beam\\\": 1.165, \\\"constraint_overhead_greedy\\\": 1.1, \\\"greedy_unconstrained_s_per_doc\\\": 2.612, \\\"greedy_constrained_s_per_doc\\\": 2.873}}, \\\"d062_ontology_scalability\\\": {\\\"metrics\\\": {\\\"compile_small_total_s\\\": 0.334, \\\"compile_medium_total_s\\\": 0.322, \\\"compile_large_total_s\\\": 0.345, \\\"compile_xlarge_total_s\\\": 0.42, \\\"grammar_small_s\\\": 0.333, \\\"grammar_xlarge_s\\\": 0.365, \\\"semantic_small_s\\\": 0.0004, \\\"semantic_xlarge_s\\\": 0.017, \\\"overhead_small\\\": 1.02, \\\"overhead_medium\\\": 1.03, \\\"overhead_large\\\": 1.03, \\\"overhead_xlarge\\\": 1.03, \\\"failures\\\": 0}}, \\\"d062_cf_majority_voting\\\": {\\\"metrics\\\": {\\\"qwen_scierc_zs\\\": {\\\"cf_before\\\": 245, \\\"cf_after\\\": 201, \\\"dr_rate_before\\\": 0.0093, \\\"dr_rate_after\\\": 0.0324}, \\\"llama_scierc_zs\\\": {\\\"cf_before\\\": 162, \\\"cf_after\\\": 123, \\\"dr_rate_before\\\": 0.0008, \\\"dr_rate_after\\\": 0.0236}, \\\"qwen_docred_zs\\\": {\\\"cf_before\\\": 518, \\\"cf_after\\\": 21, \\\"dr_rate_before\\\": 0.1021, \\\"dr_rate_after\\\": 0.1466}, \\\"llama_docred_zs\\\": {\\\"cf_before\\\": 1358, \\\"cf_after\\\": 107, \\\"dr_rate_before\\\": 0.0255, \\\"dr_rate_after\\\": 0.1665}, \\\"qwen_scierc_ft\\\": {\\\"cf_before\\\": 21, \\\"cf_after\\\": 12, \\\"dr_rate_before\\\": 0, \\\"dr_rate_after\\\": 0.0071}, \\\"llama_scierc_ft\\\": {\\\"cf_before\\\": 8, \\\"cf_after\\\": 4, \\\"dr_rate_before\\\": 0.0009, \\\"dr_rate_after\\\": 0.0037}, \\\"qwen_docred_ft\\\": {\\\"cf_before\\\": 48, \\\"cf_after\\\": 3, \\\"dr_rate_before\\\": 0.0001, \\\"dr_rate_after\\\": 0.0044}, \\\"llama_docred_ft\\\": {\\\"cf_before\\\": 41, \\\"cf_after\\\": 2, \\\"dr_rate_before\\\": 0.0021, \\\"dr_rate_after\\\": 0.005}}}, \\\"p1_ee_ft_llama_r2\\\": {\\\"metrics\\\": {\\\"parse_rate_unconstrained\\\": 1, \\\"parse_rate_constrained\\\": 1, \\\"trigger_f1_unconstrained\\\": 0.2752, \\\"trigger_f1_constrained\\\": 0.2691, \\\"argument_f1_unconstrained\\\": 0.0998, \\\"argument_f1_constrained\\\": 0.0891, \\\"entity_f1\\\": 0, \\\"rov_rate_unconstrained\\\": 0.088, \\\"rov_rate_constrained\\\": 0, \\\"ac_rate_unconstrained\\\": 0.035, \\\"ac_rate_constrained\\\": 0.008, \\\"go_nogo_unconstrained\\\": 0.122, \\\"go_nogo_constrained\\\": 0.0078}}, \\\"p1_ee_ft_composability_r5\\\": {\\\"metrics\\\": {\\\"unconstrained\\\": {\\\"parse_rate\\\": 0.85, \\\"trigger_f1\\\": 0.3208, \\\"argument_f1\\\": 0.0785, \\\"rov_rate\\\": 0.3831, \\\"ac_rate\\\": 0.0268, \\\"go_nogo\\\": 0.41}, \\\"full_s1\\\": {\\\"parse_rate\\\": 0.95, \\\"trigger_f1\\\": 0.2672, \\\"argument_f1\\\": 0.0818, \\\"rov_rate\\\": 0, \\\"ac_rate\\\": 0, \\\"go_nogo\\\": 0}}}, \\\"p1_ee_ft_llama\\\": {}, \\\"p1_ee_ft_composability_r4\\\": {\\\"metrics\\\": {\\\"unconstrained\\\": {\\\"entity_f1\\\": 0, \\\"trigger_f1\\\": 0.4598, \\\"argument_f1\\\": 0.1581, \\\"rov\\\": 0.251, \\\"ac\\\": 0.06, \\\"cf\\\": 0, \\\"parse_rate\\\": 0.25}, \\\"full_s1\\\": {\\\"entity_f1\\\": 0.5823, \\\"trigger_f1\\\": 0.6, \\\"argument_f1\\\": 0.4667, \\\"rov\\\": 0, \\\"ac\\\": 0, \\\"cf\\\": 0.03, \\\"parse_rate\\\": 0.1}}}, \\\"w9_qwen_docred_zs_sampling_r2\\\": {}, \\\"70b_docred_constrained\\\": {\\\"metrics\\\": {\\\"ET_violation\\\": 0, \\\"RV_violation\\\": 0, \\\"DR_violation\\\": 0, \\\"CF_violation\\\": 7.01, \\\"entity_f1\\\": 69.05, \\\"entity_precision\\\": 75.03, \\\"entity_recall\\\": 63.95, \\\"relation_f1\\\": 13.07, \\\"relation_precision\\\": 12.54, \\\"relation_recall\\\": 13.64, \\\"parse_failures\\\": 1, \\\"docs_processed\\\": 997, \\\"total_docs\\\": 998, \\\"unique_entities\\\": 12207, \\\"total_triples\\\": 13249}}, \\\"70b_docred_unconstrained\\\": {\\\"metrics\\\": {\\\"entity_f1\\\": 69.03, \\\"entity_precision\\\": 75.03, \\\"entity_recall\\\": 63.92, \\\"relation_f1\\\": 13.03, \\\"relation_precision\\\": 12.43, \\\"relation_recall\\\": 13.69, \\\"ET_violation\\\": 0.02, \\\"RV_violation\\\": 7.8, \\\"DR_violation\\\": 15, \\\"CF_violation\\\": 0.07, \\\"parse_failures\\\": 0, \\\"docs_processed\\\": 998}}, \\\"p1_ee_ft_composability_r3\\\": {}, \\\"p1_ee_ft_composability_r2\\\": {}, \\\"p1_ee_ft_composability\\\": {}, \\\"p8c_ft_scierc_latency\\\": {\\\"metrics\\\": {\\\"unconstrained_mean_s\\\": 2.612, \\\"constrained_mean_s\\\": 2.873, \\\"unconstrained_median_s\\\": 2.355, \\\"constrained_median_s\\\": 2.624, \\\"overhead_mean_pct\\\": 10, \\\"overhead_median_pct\\\": 11.42, \\\"per_doc_ratio_mean\\\": 1.205, \\\"per_doc_ratio_median\\\": 1.117, \\\"num_docs\\\": 551, \\\"unconstrained_total_s\\\": 1439, \\\"constrained_total_s\\\": 1582.9}}, \\\"p8b_docred_latency\\\": {}, \\\"w9_qwen_docred_zs_sampling\\\": {}, \\\"w9_qwen_scierc_zs_sampling\\\": {\\\"metrics\\\": {\\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.75, \\\"CF_pct\\\": 9.9, \\\"E_F1\\\": 31.28, \\\"R_F1\\\": 7.42, \\\"parse_fail_rate\\\": 0, \\\"total_samples\\\": 551, \\\"note\\\": \\\"F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98, R_F1=8.36\\\"}}, \\\"p8_latency_overhead\\\": {\\\"metrics\\\": {\\\"samples\\\": 551, \\\"unconstrained_mean_s\\\": 4.163, \\\"unconstrained_median_s\\\": 4.106, \\\"unconstrained_total_s\\\": 2293.7, \\\"constrained_mean_s\\\": 4.71, \\\"constrained_median_s\\\": 4.644, \\\"constrained_total_s\\\": 2595, \\\"overhead_ratio_mean\\\": 1.131, \\\"overhead_ratio_median\\\": 1.131, \\\"overhead_ratio_p95_perdoc\\\": 1.262, \\\"overhead_pct\\\": 13.1}}, \\\"q1_llama_lora_scierc_beam4\\\": {\\\"metrics\\\": {\\\"ET_violation_rate\\\": 0, \\\"RV_violation_rate\\\": 0, \\\"DR_violation_rate\\\": 0, \\\"CF_violation_rate\\\": 0, \\\"entity_f1\\\": 67.94, \\\"relation_f1\\\": 46.11, \\\"samples\\\": 551, \\\"total_entities\\\": 1853, \\\"total_relations\\\": 727}}, \\\"70b_scierc_unconstrained\\\": {\\\"metrics\\\": {\\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.6, \\\"DR_pct\\\": 6.5, \\\"CF_count\\\": 0, \\\"CF_pct\\\": 0, \\\"E_F1\\\": 0.3517, \\\"E_P\\\": 0.3009, \\\"E_R\\\": 0.4232, \\\"R_F1\\\": 0.1122, \\\"R_P\\\": 0.0929, \\\"R_R\\\": 0.1417, \\\"total_entities\\\": 2353, \\\"total_relations\\\": 1485, \\\"parse_failures\\\": 0, \\\"samples\\\": 551}}, \\\"70b_scierc_constrained\\\": {\\\"metrics\\\": {\\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 86, \\\"CF_pct\\\": 3.66, \\\"E_F1\\\": 0.3514, \\\"E_P\\\": 0.3007, \\\"E_R\\\": 0.4226, \\\"R_F1\\\": 0.1124, \\\"R_P\\\": 0.0932, \\\"R_R\\\": 0.1417, \\\"total_entities\\\": 2351, \\\"total_relations\\\": 1481, \\\"parse_failures\\\": 0, \\\"samples\\\": 551}}, \\\"ee_mistral_wikievents_grammar_only_v3\\\": {\\\"metrics\\\": {\\\"parse_success\\\": \\\"218/246 (88.6%)\\\", \\\"parse_failures\\\": 28, \\\"ET\\\": 0, \\\"EV\\\": 0, \\\"RoV\\\": 64, \\\"AC\\\": 13.8, \\\"CF\\\": 1.1, \\\"go_no_go\\\": 77.73, \\\"entity_f1\\\": 0.1192, \\\"trigger_f1\\\": 0.0337, \\\"argument_f1\\\": 0.0027, \\\"code_version\\\": \\\"938-line (collision+exact-match fix)\\\", \\\"mode\\\": \\\"grammar_only\\\"}}, \\\"ee_mistral_wikievents_constrained_v3\\\": {\\\"metrics\\\": {\\\"parse_success\\\": \\\"218/246 (88.6%)\\\", \\\"parse_failures\\\": 28, \\\"ET\\\": 0, \\\"EV\\\": 0, \\\"RoV\\\": 0, \\\"AC\\\": 1.3, \\\"CF\\\": 14.9, \\\"go_no_go\\\": 1.26, \\\"entity_f1\\\": 0.1171, \\\"trigger_f1\\\": 0.0387, \\\"argument_f1\\\": 0.0031, \\\"code_version\\\": \\\"938-line",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/301ce757-b612-46ff-a757-67ed2e0aceb1/tool-results/b7h6s3r4u.txt",
    "persistedOutputSize": 64559
  }
}
```

</details>

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Bash · `toolu_01257wnjo3r8ChqFtNubZjq6`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/301ce757-b612-46ff-a757-67ed2e0aceb1/tool-results/mcp-agent-ml-research-read_registry-1779536638218.txt') as f:\n    data = json.loads(json.loads(f.read())['result'])\nexps = data['data']['experiments']\n# Find w8 docred FT experiments\nfor k,v in exps.items():\n    if 'w8' in k and 'docred' in k:\n        m = v.get('metrics', {})\n        dr = None\n        for key in ['DR_pct', 'DR%']:\n            if key in m:\n                dr = m[key]\n        print(f'{k}: DR={dr}, metrics_keys={list(m.keys())[:10]}')\n\"\n",
  "description": "Extract w8 docred experiments from registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "2e2fad00-b735-4e4d-9a6c-3248a92dc4d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfCtaykAY9wfA4e2y7Q4LM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1520,
      "cache_read_input_tokens": 63359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1520
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

_source line 81 · 2026-05-23T11:44:11.557Z_

<details><summary>↩ Tool result · `toolu_01257wnjo3r8ChqFtNubZjq6`</summary>

```text
w8_llama_docred_ft_grammar_only: DR=None, metrics_keys=['R_F1', 'R_P', 'R_R', 'parse_fail_pct', 'samples', 'note']
w8_llama_docred_ft_semantic_only: DR=None, metrics_keys=['R_F1', 'R_P', 'R_R', 'parse_fail_pct', 'samples', 'note']
w8_qwen_docred_ft_semantic_only: DR=None, metrics_keys=['R_F1', 'R_P', 'R_R', 'parse_fail_pct', 'samples', 'note']
w8_qwen_docred_ft_grammar_only: DR=0.61, metrics_keys=['E_F1', 'E_P', 'E_R', 'R_F1', 'R_P', 'R_R', 'ET_pct', 'RV_pct', 'DR_pct', 'CF_pct']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "81770cda-7edb-43bf-b533-c1a272791d0a",
  "tool_use_result": {
    "stdout": "w8_llama_docred_ft_grammar_only: DR=None, metrics_keys=['R_F1', 'R_P', 'R_R', 'parse_fail_pct', 'samples', 'note']\nw8_llama_docred_ft_semantic_only: DR=None, metrics_keys=['R_F1', 'R_P', 'R_R', 'parse_fail_pct', 'samples', 'note']\nw8_qwen_docred_ft_semantic_only: DR=None, metrics_keys=['R_F1', 'R_P', 'R_R', 'parse_fail_pct', 'samples', 'note']\nw8_qwen_docred_ft_grammar_only: DR=0.61, metrics_keys=['E_F1', 'E_P', 'E_R', 'R_F1', 'R_P', 'R_R', 'ET_pct', 'RV_pct', 'DR_pct', 'CF_pct']",
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

_source line 82_

<details><summary>Logged reasoning block</summary>

```text
Interesting! There's a 4th experiment `w8_qwen_docred_ft_grammar_only` that DOES have DR_pct=0.61. But the 3 experiments I'm checking don't have DR_pct.

Now let me also find the unconstrained FT DocRED experiments in the registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "253b1488-1ae6-4f9a-ba55-2d9be6bdfa8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqvkBMtT1vFpNDWRhuNSF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 64879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 605
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

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_01MUwBRQ8KPtgHqTAF3LmhhY`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/301ce757-b612-46ff-a757-67ed2e0aceb1/tool-results/mcp-agent-ml-research-read_registry-1779536638218.txt') as f:\n    data = json.loads(json.loads(f.read())['result'])\nexps = data['data']['experiments']\n# Find unconstrained or posthoc docred FT experiments\nfor k,v in exps.items():\n    if 'docred' in k and ('unconstrained' in k or 'posthoc' in k or ('ft' in k and 'w8' in k)):\n        m = v.get('metrics', {})\n        dr = m.get('DR_pct', m.get('DR%', 'N/A'))\n        print(f'{k}: DR={dr}')\n\"\n",
  "description": "Find unconstrained/posthoc FT DocRED experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "7f9f322f-72d6-4ae2-b727-c9045da108c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqvkBMtT1vFpNDWRhuNSF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 64879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 605
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

_source line 84 · 2026-05-23T11:44:18.279Z_

<details><summary>↩ Tool result · `toolu_01MUwBRQ8KPtgHqTAF3LmhhY`</summary>

```text
eval_70b_zs_docred_200_unconstrained: DR=13.45
w8_llama_docred_ft_grammar_only: DR=N/A
w8_llama_docred_ft_semantic_only: DR=N/A
w8_qwen_docred_ft_semantic_only: DR=N/A
eval_70b_lora_docred_200_unconstrained: DR=0.22
70b_docred_unconstrained: DR=N/A
llama_docred_unconstrained_mt6144: DR=N/A
w8_qwen_docred_ft_grammar_only: DR=0.61
w6_mistral_docred_unconstrained: DR=57.42
w5_qwen_docred_lora_unconstrained_eval: DR=0.76
w5_llama_docred_lora_unconstrained_eval: DR=0.49
llama_docred_unconstrained: DR=N/A
phase2_docred_unconstrained: DR=N/A
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "70365da6-134f-4515-8291-9c99bced2b7c",
  "tool_use_result": {
    "stdout": "eval_70b_zs_docred_200_unconstrained: DR=13.45\nw8_llama_docred_ft_grammar_only: DR=N/A\nw8_llama_docred_ft_semantic_only: DR=N/A\nw8_qwen_docred_ft_semantic_only: DR=N/A\neval_70b_lora_docred_200_unconstrained: DR=0.22\n70b_docred_unconstrained: DR=N/A\nllama_docred_unconstrained_mt6144: DR=N/A\nw8_qwen_docred_ft_grammar_only: DR=0.61\nw6_mistral_docred_unconstrained: DR=57.42\nw5_qwen_docred_lora_unconstrained_eval: DR=0.76\nw5_llama_docred_lora_unconstrained_eval: DR=0.49\nllama_docred_unconstrained: DR=N/A\nphase2_docred_unconstrained: DR=N/A",
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

_source line 85_

<details><summary>Logged reasoning block</summary>

```text
Found them:
- w5_qwen_docred_lora_unconstrained_eval: DR=0.76%
- w5_llama_docred_lora_unconstrained_eval: DR=0.49%

These are the unconstrained baselines. They are from w5 (week 5), which is an earlier wave. But they have DR_pct values. The question is: were these computed with the same checker version?

Let me check those experiments' details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "dc31aaa9-0be8-4477-8a3a-61f24232bcdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TYtVkg3t8uCjf8s54Cykr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 65484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 703
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

_source line 86_

<details open><summary>🔧 Tool call — Bash · `toolu_01DBVqRNkfy9YFPQv8ZaLcjs`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/301ce757-b612-46ff-a757-67ed2e0aceb1/tool-results/mcp-agent-ml-research-read_registry-1779536638218.txt') as f:\n    data = json.loads(json.loads(f.read())['result'])\nexps = data['data']['experiments']\nfor k in ['w5_qwen_docred_lora_unconstrained_eval', 'w5_llama_docred_lora_unconstrained_eval']:\n    if k in exps:\n        print(f'=== {k} ===')\n        print(json.dumps(exps[k], indent=2))\n\"\n",
  "description": "Get full details of unconstrained baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "c83b9f27-76e8-4ab1-b2a1-44e498cd1c20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TYtVkg3t8uCjf8s54Cykr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 65484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 703
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

_source line 87 · 2026-05-23T11:44:24.089Z_

<details><summary>↩ Tool result · `toolu_01DBVqRNkfy9YFPQv8ZaLcjs`</summary>

```text
=== w5_qwen_docred_lora_unconstrained_eval ===
{
  "metrics": {
    "ET_pct": 0,
    "RV_pct": 0.27,
    "DR_pct": 0.76,
    "CF_pct": 0.12,
    "E_F1": 82.15,
    "E_P": 85.44,
    "E_R": 79.11,
    "R_F1": 40.86,
    "R_P": 36.41,
    "R_R": 46.56,
    "parse_fail_rate": 7.11,
    "total_samples": 998,
    "success_samples": 927,
    "fail_samples": 71,
    "total_entities_pred": 18091,
    "total_relations_pred": 15870,
    "ET_pct_excl_fail": 0,
    "RV_pct_excl_fail": 0.27,
    "DR_pct_excl_fail": 0.76,
    "CF_pct_excl_fail": 0.12,
    "E_F1_excl_fail": 85.72,
    "E_P_excl_fail": 85.44,
    "E_R_excl_fail": 86,
    "R_F1_excl_fail": 42.2,
    "R_P_excl_fail": 36.41,
    "R_R_excl_fail": 50.17
  }
}
=== w5_llama_docred_lora_unconstrained_eval ===
{
  "metrics": {
    "ET_pct": 0,
    "RV_pct": 0.15,
    "DR_pct": 0.49,
    "E_F1": 83.93,
    "E_P": 84.93,
    "E_R": 82.96,
    "R_F1": 43.72,
    "R_P": 38.59,
    "R_R": 50.41,
    "parse_fail_rate": 2.3,
    "total_samples": 998,
    "total_entities_pred": 19106,
    "total_relations_pred": 16171
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "c8b78202-5bbd-4b4c-b568-f5345c57a735",
  "tool_use_result": {
    "stdout": "=== w5_qwen_docred_lora_unconstrained_eval ===\n{\n  \"metrics\": {\n    \"ET_pct\": 0,\n    \"RV_pct\": 0.27,\n    \"DR_pct\": 0.76,\n    \"CF_pct\": 0.12,\n    \"E_F1\": 82.15,\n    \"E_P\": 85.44,\n    \"E_R\": 79.11,\n    \"R_F1\": 40.86,\n    \"R_P\": 36.41,\n    \"R_R\": 46.56,\n    \"parse_fail_rate\": 7.11,\n    \"total_samples\": 998,\n    \"success_samples\": 927,\n    \"fail_samples\": 71,\n    \"total_entities_pred\": 18091,\n    \"total_relations_pred\": 15870,\n    \"ET_pct_excl_fail\": 0,\n    \"RV_pct_excl_fail\": 0.27,\n    \"DR_pct_excl_fail\": 0.76,\n    \"CF_pct_excl_fail\": 0.12,\n    \"E_F1_excl_fail\": 85.72,\n    \"E_P_excl_fail\": 85.44,\n    \"E_R_excl_fail\": 86,\n    \"R_F1_excl_fail\": 42.2,\n    \"R_P_excl_fail\": 36.41,\n    \"R_R_excl_fail\": 50.17\n  }\n}\n=== w5_llama_docred_lora_unconstrained_eval ===\n{\n  \"metrics\": {\n    \"ET_pct\": 0,\n    \"RV_pct\": 0.15,\n    \"DR_pct\": 0.49,\n    \"E_F1\": 83.93,\n    \"E_P\": 84.93,\n    \"E_R\": 82.96,\n    \"R_F1\": 43.72,\n    \"R_P\": 38.59,\n    \"R_R\": 50.41,\n    \"parse_fail_rate\": 2.3,\n    \"total_samples\": 998,\n    \"total_entities_pred\": 19106,\n    \"total_relations_pred\": 16171\n  }\n}",
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

_source line 88_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the results:

**Unconstrained baselines (from registry, computed with an earlier checker version):**
- Qwen: DR=0.76%, total_relations_pred=15870 → DR violations ≈ 121
- Llama: DR=0.49%, total_relations_pred=16171 → DR violations ≈ 79

**Recalculated DR with violation_checker_docred.py (fixed_20260514_v2):**
1. w8_qwen_docred_ft_semantic_only: DR=31/15909=0.19%


2. w8_llama_docred_ft_semantic_only: DR=77/16038=0.48%
3. w8_llama_docred_ft_grammar_only: DR=82/16199=0.51%

I'm realizing the unconstrained baselines might have been computed with an older checker version too, so to be fully rigorous I should re-run those outputs through the current checker. The problem is the unconstrained output files aren't available on the server—only the posthoc-filtered versions exist. Looking at the posthoc reports though, I can see the Qwen posthoc data shows total_triples_before=15869 and domain_range metrics that might help me work around this.

Comparing the posthoc reports against the unconstrained registry entries, the numbers are remarkably close—the posthoc script's domain-range detection appears to align with whatever checker was used for the unconstrained evaluation. The real concern now is whether the current violation_checker_docred.py (v2 fixed) is detecting more violations than the previous version, which could skew my comparison.

Looking at the constrained results, grammar-only for Llama matches the paper's 0.51%, but semantic-only shows discrepancies—Qwen is off by 0.02pp and Llama is off by 0.18pp. The bigger problem is that the unconstrained outputs were never saved as files, only fed into the posthoc script, so I can't re-run them through the updated checker to ensure consistency.

Given that the experiment IDs suggest the unconstrained baselines were computed weeks earlier, the most practical approach is to report the recalculated DR values and note that they may reflect a checker version difference from the original paper.

But I'm noticing something odd with the Llama numbers—the unconstrained run shows 16171 total relations predicted, while the grammar-constrained version has 16199 triples. These should theoretically come from the same model with the same inference, just different decoding constraints, so the slight difference in triple counts suggests they might be from separate runs. Though actually, different constraints would naturally produce different outputs, so that discrepancy makes sense.

Looking at the posthoc report for Llama, it shows 80 domain_range violations removed out of 16171 triples—this is a posthoc operation that strips out constraint violations.

The current checker counts violations without removing them, and if the counting logic differs (like how entity types are normalized or relations are matched), the numbers could diverge. The checker was updated on May 14 to add stripping, aliasing, and unique entity type handling, which likely changed how violations are detected. For Llama semantic, I'm seeing 77 violations when I'd expect around 48 to hit 0.30%—that's roughly 29 extra violations, suggesting the fix actually increased detected violations. But for Llama grammar, 82 violations aligns with 0.51%, so the fix didn't shift those counts much.

This is getting tangled, so I'll just report what I've found and let the user make sense of it. I should try re-running the posthoc analysis to get fresh baseline numbers for the unconstrained outputs.

Actually, I'm realizing the w8_ft_posthoc files are post-filtered outputs, which means the posthoc script must have taken unconstrained outputs as input. Those unconstrained files might have been generated and consumed without being saved separately, or they could exist under different names. Let me check all the output files to see what's actually there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "189fe1b2-3d0e-4d02-a343-2d71ec8dfc35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmPCsmFYoui9Fp5ttDyu9k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 66187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

_source line 89_

需要确认 unconstrained 基线是否用同一版本 checker 计算。也检查是否有 unconstrained 输出文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "44643966-49f9-4009-b46f-5e9ccecc0370",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmPCsmFYoui9Fp5ttDyu9k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 66187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

_source line 90_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0189hVABgoBDK7u4mXChMm3R`</summary>

```json
{
  "server": "westd-16980",
  "command": "ls /root/schema_semantic_constrained_ie/outputs/w5*docred* /root/schema_semantic_constrained_ie/outputs/*qwen*docred*unc* /root/schema_semantic_constrained_ie/outputs/*llama*docred*unc*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "6a174606-872f-4741-a962-6655ac4812cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmPCsmFYoui9Fp5ttDyu9k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 66187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

_source line 91 · 2026-05-23T11:45:03.742Z_

<details><summary>↩ Tool result · `toolu_0189hVABgoBDK7u4mXChMm3R`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/outputs/analysis_llama_docred_unconstrained_mt6144_v2.json\\n/root/schema_semantic_constrained_ie/outputs/analysis_llama_docred_unconstrained_v2.json\\n/root/schema_semantic_constrained_ie/outputs/d066_llama_docred_lora_unc.json\\n/root/schema_semantic_constrained_ie/outputs/d066_qwen_docred_lora_unc.json\\n/root/schema_semantic_constrained_ie/outputs/llama_docred_unconstrained.jsonl\\n/root/schema_semantic_constrained_ie/outputs/llama_docred_unconstrained_mt6144.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval_cf_corrected.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_unconstrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_unconstrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_constrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_constrained_eval_cf_corrected.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "5cb8e6d9-152f-41f6-b44b-115a16dc1f6e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/schema_semantic_constrained_ie/outputs/analysis_llama_docred_unconstrained_mt6144_v2.json\\\\n/root/schema_semantic_constrained_ie/outputs/analysis_llama_docred_unconstrained_v2.json\\\\n/root/schema_semantic_constrained_ie/outputs/d066_llama_docred_lora_unc.json\\\\n/root/schema_semantic_constrained_ie/outputs/d066_qwen_docred_lora_unc.json\\\\n/root/schema_semantic_constrained_ie/outputs/llama_docred_unconstrained.jsonl\\\\n/root/schema_semantic_constrained_ie/outputs/llama_docred_unconstrained_mt6144.jsonl\\\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl\\\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval_cf_corrected.jsonl\\\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_unconstrained_eval.jsonl\\\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_unconstrained_eval.jsonl\\\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_constrained_eval.jsonl\\\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_constrained_eval_cf_corrected.jsonl\\\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl\\\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/outputs/analysis_llama_docred_unconstrained_mt6144_v2.json\\n/root/schema_semantic_constrained_ie/outputs/analysis_llama_docred_unconstrained_v2.json\\n/root/schema_semantic_constrained_ie/outputs/d066_llama_docred_lora_unc.json\\n/root/schema_semantic_constrained_ie/outputs/d066_qwen_docred_lora_unc.json\\n/root/schema_semantic_constrained_ie/outputs/llama_docred_unconstrained.jsonl\\n/root/schema_semantic_constrained_ie/outputs/llama_docred_unconstrained_mt6144.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval_cf_corrected.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_unconstrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_unconstrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_constrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_constrained_eval_cf_corrected.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl\\n/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 92_

<details><summary>Logged reasoning block</summary>

```text
The unconstrained output files exist:
- w5_qwen_docred_lora_unconstrained_eval.jsonl
- w5_llama_docred_lora_unconstrained_eval.jsonl

I should run violation_checker_docred.py on these to get the unconstrained DR with the SAME checker version. This will ensure a fair comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "b8aa087c-2160-41f6-b623-652b5a53f1e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HcSsaJGHHTsvXUDPLHnqkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2308,
      "cache_read_input_tokens": 67217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2308
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

_source line 93_

找到了！unconstrained 输出文件存在。用同一版本 checker 重算 unconstrained 基线，确保一致性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "c5bb016d-2a5b-4ccd-b4fe-72492d5e8252",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HcSsaJGHHTsvXUDPLHnqkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2308,
      "cache_read_input_tokens": 67217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2308
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

_source line 94_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01AQANrXjJXmHnrZ8b9Xjr85`</summary>

```json
{
  "server": "westd-16980",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl --output_path /tmp/vr_qwen_unc.json 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "359aef7a-49d8-402b-85a5-da03c928fb9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HcSsaJGHHTsvXUDPLHnqkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2308,
      "cache_read_input_tokens": 67217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2308
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

_source line 95_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01CsohvXXtXZdr4EcTp9A5B7`</summary>

```json
{
  "server": "westd-16980",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python violation_checker_docred.py --input_path outputs/w5_llama_docred_lora_unconstrained_eval.jsonl --output_path /tmp/vr_llama_unc.json 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "bd3501d5-3cbf-41a3-beca-32b0e57ca908",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HcSsaJGHHTsvXUDPLHnqkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2308,
      "cache_read_input_tokens": 67217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2308
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

_source line 96 · 2026-05-23T11:45:10.959Z_

<details><summary>↩ Tool result · `toolu_01AQANrXjJXmHnrZ8b9Xjr85`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Violation Report (DocRED) ===\\nDocuments: 927 checked, 71 parse failures\\nEntities: 18091, Triples: 15870\\n\\nEntity type violations: 0 (0.0%)\\nRelation vocab violations: 43/15870 (0.3%)\\nDomain/range violations: 121/15870 (0.8%)\\nCross-field consistency violations: 16\\nFuzzy relation matches: 0\\n\\nGo/No-go metric (D/R violation rate): 0.0076\\nOutput: /tmp/vr_qwen_unc.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "2a16eb39-4162-4549-ad7b-5ae4363f1d75",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== Violation Report (DocRED) ===\\\\nDocuments: 927 checked, 71 parse failures\\\\nEntities: 18091, Triples: 15870\\\\n\\\\nEntity type violations: 0 (0.0%)\\\\nRelation vocab violations: 43/15870 (0.3%)\\\\nDomain/range violations: 121/15870 (0.8%)\\\\nCross-field consistency violations: 16\\\\nFuzzy relation matches: 0\\\\n\\\\nGo/No-go metric (D/R violation rate): 0.0076\\\\nOutput: /tmp/vr_qwen_unc.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.91}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== Violation Report (DocRED) ===\\nDocuments: 927 checked, 71 parse failures\\nEntities: 18091, Triples: 15870\\n\\nEntity type violations: 0 (0.0%)\\nRelation vocab violations: 43/15870 (0.3%)\\nDomain/range violations: 121/15870 (0.8%)\\nCross-field consistency violations: 16\\nFuzzy relation matches: 0\\n\\nGo/No-go metric (D/R violation rate): 0.0076\\nOutput: /tmp/vr_qwen_unc.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-23T11:45:11.865Z_

<details><summary>↩ Tool result · `toolu_01CsohvXXtXZdr4EcTp9A5B7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Violation Report (DocRED) ===\\nDocuments: 975 checked, 23 parse failures\\nEntities: 19106, Triples: 16171\\n\\nEntity type violations: 0 (0.0%)\\nRelation vocab violations: 24/16171 (0.1%)\\nDomain/range violations: 80/16171 (0.5%)\\nCross-field consistency violations: 16\\nFuzzy relation matches: 0\\n\\nGo/No-go metric (D/R violation rate): 0.0049\\nOutput: /tmp/vr_llama_unc.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "e63056c9-8945-4f0b-9f6b-4861d2ced070",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== Violation Report (DocRED) ===\\\\nDocuments: 975 checked, 23 parse failures\\\\nEntities: 19106, Triples: 16171\\\\n\\\\nEntity type violations: 0 (0.0%)\\\\nRelation vocab violations: 24/16171 (0.1%)\\\\nDomain/range violations: 80/16171 (0.5%)\\\\nCross-field consistency violations: 16\\\\nFuzzy relation matches: 0\\\\n\\\\nGo/No-go metric (D/R violation rate): 0.0049\\\\nOutput: /tmp/vr_llama_unc.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== Violation Report (DocRED) ===\\nDocuments: 975 checked, 23 parse failures\\nEntities: 19106, Triples: 16171\\n\\nEntity type violations: 0 (0.0%)\\nRelation vocab violations: 24/16171 (0.1%)\\nDomain/range violations: 80/16171 (0.5%)\\nCross-field consistency violations: 16\\nFuzzy relation matches: 0\\n\\nGo/No-go metric (D/R violation rate): 0.0049\\nOutput: /tmp/vr_llama_unc.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 98_

<details><summary>Logged reasoning block</summary>

```text
Now I have consistent baselines from the SAME checker version (fixed_20260514_v2):

**Unconstrained baselines (re-verified with current checker):**
- Qwen unconstrained: DR = 121/15870 = 0.0076 = 0.76%
- Llama unconstrained: DR = 80/16171 = 0.0049 = 0.49%

These match exactly what was in the registry (0.76% and 0.49%), which is reassuring. The checker fix didn't change the unconstrained results.


Now looking at the ablation results with the current checker, I'm seeing the semantic-only and grammar-only variants for both models. I'm comparing these against the paper values to see how much deviation there is between what was reported and what I'm calculating now. Now I'm noticing a major discrepancy in the results — the Llama semantic-only constraint barely reduces DR violations at all, dropping from 0.49% to just 0.48%, which is only 3 violations out of thousands. That's suspiciously ineffective compared to Qwen's 75% reduction. I'm wondering if the semantic-only output file was actually generated with the correct constraint mode, or if something went wrong in the pipeline.

Actually, I think I see what's happening. The semantic-only constraint is supposed to restrict domain and range but not vocabulary, so invalid relation names can still slip through. If the model produces an unrecognized relation name, it might not even get checked for domain-range violations, which would mask the semantic constraint's effectiveness. Looking at the violation counts, the RV (relation vocabulary) violations stay at 24 for both unconstrained and semantic-only Llama, meaning the semantic constraint didn't change the invalid relation names at all.

The grammar-only constraint, by contrast, eliminated all RV violations but actually increased DR violations slightly, which makes sense since it controls vocabulary without checking domain-range compatibility. So the real question is why semantic constraints barely reduce DR violations for Llama on DocRED—it could be a model-specific limitation, a bug in the constraint application, or an issue with the output file itself. Let me check if the paper's reported value came from a different calculation or dataset.

Looking at the posthoc report, I see it shows the full constrained results (grammar plus semantic combined), not the semantic-only ablation I'm examining. The 0.30% figure might have been computed with an older version of the violation checker before the normalization fix that changed how entity types are processed.

Comparing the violation counts across versions, I notice the semantic-only mode shows more cross-field violations (31 versus 16 in unconstrained), which seems odd. The range violations stay consistent at 24, so it's possible the old checker was categorizing some violations differently—perhaps shifting between domain-range and cross-field classifications depending on how entity type uniqueness was handled. The current checker appears to be giving consistent results across these versions.

Since the fixed checker explicitly addresses these issues with stripping, aliasing, and unique entity type counting, and the unconstrained baselines match the paper exactly, I should treat these corrected values as authoritative. Computing the DR reduction with the consistent checker across all experiments gives me Qwen semantic at 75% reduction and Llama semantic at just 2% reduction—a much wider gap than the claimed 39-72% range. For Llama, the semantic constraint reduces violations by about 2.9%, which is much smaller than Qwen's 75% reduction. Let me verify this using the actual violation counts rather than the rounded percentages, since the triple counts differ between the unconstrained and semantic versions.

Now I need to document these corrected findings and update the registry with the proper DR values for all three experiments, making sure to preserve the existing metrics while adding the recalculated defeasible reasoning percentages. I'm looking at the verification notes for these model variants and noticing the old registry values had small deltas from the corrected eval script. Now I need to expand these entries with the violation breakdown metrics and update the notes to reflect the full verification details. Now I'm structuring the update to keep the existing fields intact while adding the violation metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "7fd05fe0-4df3-4b5d-972a-76d1dbab9c00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013H1coNfCxb4hsKkjgetbhP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 69525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 99_

Unconstrained 基线用同一 checker 重算结果完全一致（Qwen=0.76%, Llama=0.49%）。现在有完整一致的数据了。

汇总结果：

| 实验 | 论文 DR% | 重算 DR% | 偏差 | 需修正? |
|---|---|---|---|---|
| w8_qwen_docred_ft_semantic_only | 0.21 | 0.19 (31/15909) | -0.02pp | 轻微 |
| w8_llama_docred_ft_semantic_only | 0.30 | 0.48 (77/16038) | **+0.18pp** | **是** |
| w8_llama_docred_ft_grammar_only | 0.51 | 0.51 (82/16199) | 0.00pp | 否 |

**DR reduction 修正：**
- Qwen semantic: (0.76−0.19)/0.76 = **75.0%**
- Llama semantic: (0.49−0.48)/0.49 = **2.0%**
- 修正后范围：**2%--75%**，远非论文中的 "39--72%"

Llama semantic-only 的 DR 几乎没有降低（80→77 violations），是主要问题点。

现在更新 registry，回填修正的 DR 值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "57b0fada-0b18-42b3-8c02-91b9867383c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013H1coNfCxb4hsKkjgetbhP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 69525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 100_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_017tJjWhaFVh7g6m9hgiwDbQ`</summary>

```json
{
  "exp_id": "w8_qwen_docred_ft_semantic_only",
  "field": "metrics",
  "value": {
    "R_F1": 40.85,
    "R_P": 36.33,
    "R_R": 46.65,
    "parse_fail_pct": 7.52,
    "samples": 998,
    "ET_pct": 0.01,
    "RV_pct": 0.23,
    "DR_pct": 0.19,
    "CF_pct": 0.18,
    "dr_violations": 31,
    "total_triples": 15909,
    "total_entities": 18025,
    "note": "Re-verified 2026-05-22 R_F1 with eval_d064.py. DR_pct re-verified 2026-05-23 with violation_checker_docred.py (fixed_20260514_v2). Paper had DR=0.21%, corrected to 0.19%."
  },
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "6c468660-28ff-4b2d-8584-8950402be92f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013H1coNfCxb4hsKkjgetbhP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 69525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 101 · 2026-05-23T11:46:23.310Z_

<details><summary>↩ Tool result · `toolu_017tJjWhaFVh7g6m9hgiwDbQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"w8_qwen_docred_ft_semantic_only\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:08:59.297Z\", \"updated_at\": \"2026-05-23T11:46:22.923Z\", \"hypothesis\": \"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablation 有 Qwen 双模式数据。\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"server\": \"westd-21461\", \"data_path\": \"data/docred\", \"data_count\": 998, \"model_name\": \"qwen_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"qwen_lora_docred_merged\", \"eval_data\": \"docred_test_998\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:18:27.113Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:18:29.130284+00:00\"}]}, \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"ET_pct\": 0.01, \"RV_pct\": 0.23, \"DR_pct\": 0.19, \"CF_pct\": 0.18, \"dr_violations\": 31, \"total_triples\": 15909, \"total_entities\": 18025, \"note\": \"Re-verified 2026-05-22 R_F1 with eval_d064.py. DR_pct re-verified 2026-05-23 with violation_checker_docred.py (fixed_20260514_v2). Paper had DR=0.21%, corrected to 0.19%.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T16:22:28.075Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8573}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "66c0f22d-1594-49ec-b5dc-dc1a18752994",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"w8_qwen_docred_ft_semantic_only\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T10:08:59.297Z\\\", \\\"updated_at\\\": \\\"2026-05-23T11:46:22.923Z\\\", \\\"hypothesis\\\": \\\"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablation 有 Qwen 双模式数据。\\\", \\\"parent\\\": \\\"w5_qwen_docred_lora_training\\\", \\\"spec\\\": {\\\"command\\\": \\\"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/docred\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"qwen_lora_docred_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"qwen_lora_docred_merged\\\", \\\"eval_data\\\": \\\"docred_test_998\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"log_path\\\": \\\"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-16T16:18:27.113Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-16T16:18:29.130284+00:00\\\"}]}, \\\"metrics\\\": {\\\"R_F1\\\": 40.85, \\\"R_P\\\": 36.33, \\\"R_R\\\": 46.65, \\\"parse_fail_pct\\\": 7.52, \\\"samples\\\": 998, \\\"ET_pct\\\": 0.01, \\\"RV_pct\\\": 0.23, \\\"DR_pct\\\": 0.19, \\\"CF_pct\\\": 0.18, \\\"dr_violations\\\": 31, \\\"total_triples\\\": 15909, \\\"total_entities\\\": 18025, \\\"note\\\": \\\"Re-verified 2026-05-22 R_F1 with eval_d064.py. DR_pct re-verified 2026-05-23 with violation_checker_docred.py (fixed_20260514_v2). Paper had DR=0.21%, corrected to 0.19%.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-16T16:22:28.075Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8573}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"w8_qwen_docred_ft_semantic_only\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:08:59.297Z\", \"updated_at\": \"2026-05-23T11:46:22.923Z\", \"hypothesis\": \"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablation 有 Qwen 双模式数据。\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"server\": \"westd-21461\", \"data_path\": \"data/docred\", \"data_count\": 998, \"model_name\": \"qwen_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"qwen_lora_docred_merged\", \"eval_data\": \"docred_test_998\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:18:27.113Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:18:29.130284+00:00\"}]}, \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"ET_pct\": 0.01, \"RV_pct\": 0.23, \"DR_pct\": 0.19, \"CF_pct\": 0.18, \"dr_violations\": 31, \"total_triples\": 15909, \"total_entities\": 18025, \"note\": \"Re-verified 2026-05-22 R_F1 with eval_d064.py. DR_pct re-verified 2026-05-23 with violation_checker_docred.py (fixed_20260514_v2). Paper had DR=0.21%, corrected to 0.19%.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T16:22:28.075Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8573}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 102_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01RVSeDfwi8nbA8gcYMZoBKj`</summary>

```json
{
  "exp_id": "w8_llama_docred_ft_semantic_only",
  "field": "metrics",
  "value": {
    "R_F1": 43.85,
    "R_P": 38.85,
    "R_R": 50.31,
    "parse_fail_pct": 2.4,
    "samples": 998,
    "ET_pct": 0.04,
    "RV_pct": 0.15,
    "DR_pct": 0.48,
    "CF_pct": 0.16,
    "dr_violations": 77,
    "total_triples": 16038,
    "total_entities": 19099,
    "note": "Re-verified 2026-05-22 R_F1 with eval_d064.py. DR_pct re-verified 2026-05-23 with violation_checker_docred.py (fixed_20260514_v2). Paper had DR=0.30%, CORRECTED to 0.48% (+0.18pp). Major discrepancy."
  },
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "c5e0624f-d3c3-4a6f-a585-bab9fca674fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013H1coNfCxb4hsKkjgetbhP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 69525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 103 · 2026-05-23T11:46:26.028Z_

<details><summary>↩ Tool result · `toolu_01RVSeDfwi8nbA8gcYMZoBKj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"w8_llama_docred_ft_semantic_only\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:54:02.910Z\", \"updated_at\": \"2026-05-23T11:46:25.697Z\", \"hypothesis\": \"FT Llama DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.49% 降至 ~0.2-0.3%（参照 SciERC 模式：semantic_only 降 DR 42%）。完成后 DocRED FT ablation 有 Llama 双模式数据，2 模型 ×2 模式全部完备。\", \"parent\": \"w5_llama_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": 1, \"pid\": 361202, \"model_name\": \"Llama-3.1-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:49:59.199Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:50:01.253379+00:00\"}]}, \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"ET_pct\": 0.04, \"RV_pct\": 0.15, \"DR_pct\": 0.48, \"CF_pct\": 0.16, \"dr_violations\": 77, \"total_triples\": 16038, \"total_entities\": 19099, \"note\": \"Re-verified 2026-05-22 R_F1 with eval_d064.py. DR_pct re-verified 2026-05-23 with violation_checker_docred.py (fixed_20260514_v2). Paper had DR=0.30%, CORRECTED to 0.48% (+0.18pp). Major discrepancy.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"outputs/w8_llama_docred_ft_semantic_only.jsonl\", \"completed_at\": \"2026-05-16T16:55:22.088Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7862}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "574619a3-6ce7-4b46-a2ca-414aa7cd97ab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"w8_llama_docred_ft_semantic_only\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T10:54:02.910Z\\\", \\\"updated_at\\\": \\\"2026-05-23T11:46:25.697Z\\\", \\\"hypothesis\\\": \\\"FT Llama DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.49% 降至 ~0.2-0.3%（参照 SciERC 模式：semantic_only 降 DR 42%）。完成后 DocRED FT ablation 有 Llama 双模式数据，2 模型 ×2 模式全部完备。\\\", \\\"parent\\\": \\\"w5_llama_docred_lora_training\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\\\\\"\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": 1, \\\"pid\\\": 361202, \\\"model_name\\\": \\\"Llama-3.1-8B-LoRA-DocRED\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-16T16:49:59.199Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-16T16:50:01.253379+00:00\\\"}]}, \\\"metrics\\\": {\\\"R_F1\\\": 43.85, \\\"R_P\\\": 38.85, \\\"R_R\\\": 50.31, \\\"parse_fail_pct\\\": 2.4, \\\"samples\\\": 998, \\\"ET_pct\\\": 0.04, \\\"RV_pct\\\": 0.15, \\\"DR_pct\\\": 0.48, \\\"CF_pct\\\": 0.16, \\\"dr_violations\\\": 77, \\\"total_triples\\\": 16038, \\\"total_entities\\\": 19099, \\\"note\\\": \\\"Re-verified 2026-05-22 R_F1 with eval_d064.py. DR_pct re-verified 2026-05-23 with violation_checker_docred.py (fixed_20260514_v2). Paper had DR=0.30%, CORRECTED to 0.48% (+0.18pp). Major discrepancy.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"log_path\\\": \\\"outputs/w8_llama_docred_ft_semantic_only.jsonl\\\", \\\"completed_at\\\": \\\"2026-05-16T16:55:22.088Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7862}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"w8_llama_docred_ft_semantic_only\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:54:02.910Z\", \"updated_at\": \"2026-05-23T11:46:25.697Z\", \"hypothesis\": \"FT Llama DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.49% 降至 ~0.2-0.3%（参照 SciERC 模式：semantic_only 降 DR 42%）。完成后 DocRED FT ablation 有 Llama 双模式数据，2 模型 ×2 模式全部完备。\", \"parent\": \"w5_llama_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": 1, \"pid\": 361202, \"model_name\": \"Llama-3.1-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:49:59.199Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:50:01.253379+00:00\"}]}, \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"ET_pct\": 0.04, \"RV_pct\": 0.15, \"DR_pct\": 0.48, \"CF_pct\": 0.16, \"dr_violations\": 77, \"total_triples\": 16038, \"total_entities\": 19099, \"note\": \"Re-verified 2026-05-22 R_F1 with eval_d064.py. DR_pct re-verified 2026-05-23 with violation_checker_docred.py (fixed_20260514_v2). Paper had DR=0.30%, CORRECTED to 0.48% (+0.18pp). Major discrepancy.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"outputs/w8_llama_docred_ft_semantic_only.jsonl\", \"completed_at\": \"2026-05-16T16:55:22.088Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7862}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 104_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01DNmzAZ2viQg77bH6cPLFSJ`</summary>

```json
{
  "exp_id": "w8_llama_docred_ft_grammar_only",
  "field": "metrics",
  "value": {
    "R_F1": 43.72,
    "R_P": 38.57,
    "R_R": 50.44,
    "parse_fail_pct": 2.3,
    "samples": 998,
    "ET_pct": 0,
    "RV_pct": 0,
    "DR_pct": 0.51,
    "CF_pct": 0.08,
    "dr_violations": 82,
    "total_triples": 16199,
    "total_entities": 19116,
    "note": "Re-verified 2026-05-22 R_F1 with eval_d064.py. DR_pct re-verified 2026-05-23 with violation_checker_docred.py (fixed_20260514_v2). Matches paper DR=0.51%."
  },
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "aa17d7bd-6609-4627-b5e8-c23e64cc4faf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013H1coNfCxb4hsKkjgetbhP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 69525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 105 · 2026-05-23T11:46:28.167Z_

<details><summary>↩ Tool result · `toolu_01DNmzAZ2viQg77bH6cPLFSJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"w8_llama_docred_ft_grammar_only\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:34:25.909Z\", \"updated_at\": \"2026-05-23T11:46:27.840Z\", \"hypothesis\": \"FT Llama DocRED + grammar_only eval: FT 后 DR 残留 0.49%，grammar_only 能消除多少？如果 grammar_only 已足够则 semantic 层在 FT regime 边际价值小；如果不够则两层在 FT 后仍互补。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"llama_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"w5_llama_docred_lora\", \"eval_data\": \"docred_dev_998\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"/tmp/w8_llama_docred_ft_grammar_only.log\", \"completed_at\": \"2026-05-16T12:31:33.933Z\", \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.51, \"CF_pct\": 0.08, \"dr_violations\": 82, \"total_triples\": 16199, \"total_entities\": 19116, \"note\": \"Re-verified 2026-05-22 R_F1 with eval_d064.py. DR_pct re-verified 2026-05-23 with violation_checker_docred.py (fixed_20260514_v2). Matches paper DR=0.51%.\"}, \"parent\": \"w5_llama_docred_lora_training\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8349}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "4be5eb81-8618-4cef-a51e-64bd204089a1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"w8_llama_docred_ft_grammar_only\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T06:34:25.909Z\\\", \\\"updated_at\\\": \\\"2026-05-23T11:46:27.840Z\\\", \\\"hypothesis\\\": \\\"FT Llama DocRED + grammar_only eval: FT 后 DR 残留 0.49%，grammar_only 能消除多少？如果 grammar_only 已足够则 semantic 层在 FT regime 边际价值小；如果不够则两层在 FT 后仍互补。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"llama_lora_docred_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"w5_llama_docred_lora\\\", \\\"eval_data\\\": \\\"docred_dev_998\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"log_path\\\": \\\"/tmp/w8_llama_docred_ft_grammar_only.log\\\", \\\"completed_at\\\": \\\"2026-05-16T12:31:33.933Z\\\", \\\"metrics\\\": {\\\"R_F1\\\": 43.72, \\\"R_P\\\": 38.57, \\\"R_R\\\": 50.44, \\\"parse_fail_pct\\\": 2.3, \\\"samples\\\": 998, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.51, \\\"CF_pct\\\": 0.08, \\\"dr_violations\\\": 82, \\\"total_triples\\\": 16199, \\\"total_entities\\\": 19116, \\\"note\\\": \\\"Re-verified 2026-05-22 R_F1 with eval_d064.py. DR_pct re-verified 2026-05-23 with violation_checker_docred.py (fixed_20260514_v2). Matches paper DR=0.51%.\\\"}, \\\"parent\\\": \\\"w5_llama_docred_lora_training\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8349}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"w8_llama_docred_ft_grammar_only\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:34:25.909Z\", \"updated_at\": \"2026-05-23T11:46:27.840Z\", \"hypothesis\": \"FT Llama DocRED + grammar_only eval: FT 后 DR 残留 0.49%，grammar_only 能消除多少？如果 grammar_only 已足够则 semantic 层在 FT regime 边际价值小；如果不够则两层在 FT 后仍互补。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"llama_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"w5_llama_docred_lora\", \"eval_data\": \"docred_dev_998\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"/tmp/w8_llama_docred_ft_grammar_only.log\", \"completed_at\": \"2026-05-16T12:31:33.933Z\", \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.51, \"CF_pct\": 0.08, \"dr_violations\": 82, \"total_triples\": 16199, \"total_entities\": 19116, \"note\": \"Re-verified 2026-05-22 R_F1 with eval_d064.py. DR_pct re-verified 2026-05-23 with violation_checker_docred.py (fixed_20260514_v2). Matches paper DR=0.51%.\"}, \"parent\": \"w5_llama_docred_lora_training\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8349}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 106_

Registry 已更新。最终报告：

---

## 重验结果

所有 DR 值均用 **violation_checker_docred.py (fixed_20260514_v2)** 重算，包括 unconstrained 基线，确保一致可比。

| 实验 | 论文 DR% | 重算 DR% | 偏差 | 需修正? |
|---|---|---|---|---|
| w8_qwen_docred_ft_semantic_only | 0.21 | **0.19** (31/15909) | -0.02pp | 轻微，可接受 |
| w8_llama_docred_ft_semantic_only | 0.30 | **0.48** (77/16038) | **+0.18pp** | **必须修正** |
| w8_llama_docred_ft_grammar_only | 0.51 | **0.51** (82/16199) | 0.00pp | 匹配 |

## Unconstrained 基线验证（同一 checker）

| 模型 | 基线 DR% | 重算 DR% | 一致? |
|---|---|---|---|
| Qwen | 0.76 | 0.76 (121/15870) | 是 |
| Llama | 0.49 | 0.49 (80/16171) | 是 |

## Semantic DR Reduction 修正

| 模型 | 计算方式 | 论文隐含值 | 修正值 |
|---|---|---|---|
| Qwen | (0.76−0.19)/0.76 | 72% | **75%** |
| Llama | (0.49−0.48)/0.49 | 39% | **2%** |
| **Range** | | **39--72%** | **2--75%** |

## 影响

正文 claim "39--72% DR reduction" **不成立**。Llama semantic-only 仅减少 3 个 DR violation（80→77），reduction 仅 2%，远非 39%。这意味着 semantic constraint 对 FT Llama+DocRED 几乎无效。

论文中 0.30% 可能是用旧版 checker（未修正 entity type normalization）计算的结果。当前修正版 checker 多检出约 29 个 DR violation。

## 已完成

- 3 个实验的 DR_pct 已回填至 registry（含 ET/RV/CF 全量 violation 数据）
- 需要修正论文中 Llama semantic-only DR 值和 "39--72%" claim

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "uuid": "da4c6744-01a4-4146-b014-b94e6bc17f94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gy78X9TrFCpL9FahKxhnjg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7134,
      "cache_read_input_tokens": 70622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7134
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

_source line 107_

Registry 已更新。最终报告：

---

## 重验结果

所有 DR 值均用 **violation_checker_docred.py (fixed_20260514_v2)** 重算，包括 unconstrained 基线，确保一致可比。

| 实验 | 论文 DR% | 重算 DR% | 偏差 | 需修正? |
|---|---|---|---|---|
| w8_qwen_docred_ft_semantic_only | 0.21 | **0.19** (31/15909) | -0.02pp | 轻微，可接受 |
| w8_llama_docred_ft_semantic_only | 0.30 | **0.48** (77/16038) | **+0.18pp** | **必须修正** |
| w8_llama_docred_ft_grammar_only | 0.51 | **0.51** (82/16199) | 0.00pp | 匹配 |

## Unconstrained 基线验证（同一 checker）

| 模型 | 基线 DR% | 重算 DR% | 一致? |
|---|---|---|---|
| Qwen | 0.76 | 0.76 (121/15870) | 是 |
| Llama | 0.49 | 0.49 (80/16171) | 是 |

## Semantic DR Reduction 修正

| 模型 | 计算方式 | 论文隐含值 | 修正值 |
|---|---|---|---|
| Qwen | (0.76−0.19)/0.76 | 72% | **75%** |
| Llama | (0.49−0.48)/0.49 | 39% | **2%** |
| **Range** | | **39--72%** | **2--75%** |

## 影响

正文 claim "39--72% DR reduction" **不成立**。Llama semantic-only 仅减少 3 个 DR violation（80→77），reduction 仅 2%，远非 39%。这意味着 semantic constraint 对 FT Llama+DocRED 几乎无效。

论文中 0.30% 可能是用旧版 checker（未修正 entity type normalization）计算的结果。当前修正版 checker 多检出约 29 个 DR violation。

## 已完成

- 3 个实验的 DR_pct 已回填至 registry（含 ET/RV/CF 全量 violation 数据）
- 需要修正论文中 Llama semantic-only DR 值和 "39--72%" claim

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 385535,
  "duration_api_ms": 377269,
  "num_turns": 38,
  "stop_reason": "end_turn",
  "session_id": "301ce757-b612-46ff-a757-67ed2e0aceb1",
  "total_cost_usd": 1.38644725,
  "usage": {
    "input_tokens": 25,
    "cache_creation_input_tokens": 65915,
    "cache_read_input_tokens": 1001243,
    "output_tokens": 18880,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 65915,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 706,
        "cache_read_input_tokens": 70622,
        "cache_creation_input_tokens": 7134,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 7134
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1627,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001732,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 25,
      "outputTokens": 18880,
      "cacheReadInputTokens": 1001243,
      "cacheCreationInputTokens": 65915,
      "webSearchRequests": 0,
      "costUSD": 1.3847152500000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5957a74c-b860-449c-855c-ac7439e07151"
}
```

</details>

---
