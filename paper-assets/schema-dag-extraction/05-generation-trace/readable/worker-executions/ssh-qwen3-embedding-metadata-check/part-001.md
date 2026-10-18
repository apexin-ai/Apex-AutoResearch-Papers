# ssh qwen3 embedding metadata check — Part 1 of 54

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

[Transcript overview](../ssh-qwen3-embedding-metadata-check.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/fd/fd8a2cadee77b25777aa.json)

## Before a recorded user message

## Before a recorded user message

79 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
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
  "uuid": "5142f4c0-6a5e-45aa-8594-9de3149aa1b8",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "resetsAt": 1778836200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "09524986-a34e-4dbe-afdc-ba73f184c9db",
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to check which model was actually used to generate Few-NERD Qwen3 embeddings on the server. Let me execute the checks on the remote server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "11f9aaea-6909-4977-9f3a-b43ad231b1c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01423Qq1bA4Xyv7hjhvK2MGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11961,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11961
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Da2iw8jDFZAJjUd2JqoRZp`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "f2673cdc-5c28-451d-803b-00dd071e0b69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01423Qq1bA4Xyv7hjhvK2MGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11961,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11961
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

_source line 6 · 2026-05-15T09:07:59.697Z_

<details><summary>↩ Tool result · `toolu_01Da2iw8jDFZAJjUd2JqoRZp`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "3120ab9a-7167-4fd7-bbb9-92b993cda381",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 23
  }
}
```

</details>

---


### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me run the checks on the server. I'll start with checking the embedding file metadata and the source code in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "829550a4-953c-4689-bc29-93c07a12b18d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSi7ZApKX8U9ZZQf9TRDx6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 23802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LvG3VzDo3SsFBhAHM3Qukt`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && python3 -c \"\nimport torch\nd = torch.load('artifacts/type_embeddings.pt', map_location='cpu', weights_only=False)\nprint('=== type_embeddings.pt ===')\nprint('Keys:', list(d.keys()) if isinstance(d, dict) else type(d))\nif isinstance(d, dict):\n    for k,v in d.items():\n        if isinstance(v, torch.Tensor):\n            print(f'  {k}: shape={v.shape}, dtype={v.dtype}')\n        else:\n            print(f'  {k}: {v}')\n\"",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "3e49b88b-a2c2-4577-b09a-a4f8fc46700f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSi7ZApKX8U9ZZQf9TRDx6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 23802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
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

_source line 9 · 2026-05-15T09:08:04.630Z_

<details><summary>↩ Tool result · `toolu_01LvG3VzDo3SsFBhAHM3Qukt`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "2a565d5c-ab4f-4e24-a4cc-eefb92e95aed",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016SEB8my1RdXhhPy88Xtonp`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && python3 -c \"\nimport torch\nd2 = torch.load('artifacts/sim_matrix.pt', map_location='cpu', weights_only=False)\nprint('=== sim_matrix.pt ===')\nprint('Keys:', list(d2.keys()) if isinstance(d2, dict) else type(d2))\nif isinstance(d2, dict):\n    for k,v in d2.items():\n        if isinstance(v, torch.Tensor):\n            print(f'  {k}: shape={v.shape}, dtype={v.dtype}')\n        else:\n            print(f'  {k}: {v}')\n\"",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "c75d9e84-eb1a-4c14-9d1c-2950fa2f990f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSi7ZApKX8U9ZZQf9TRDx6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 23802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
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

_source line 11 · 2026-05-15T09:08:06.590Z_

<details><summary>↩ Tool result · `toolu_016SEB8my1RdXhhPy88Xtonp`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "c75c6c02-9666-4804-bec1-5c99f3c23f5f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KxKKPgX4tqnM4GNsyC8QQg`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && python3 -c \"\nimport torch\nd = torch.load('artifacts/maven_type_embeddings_qwen3.pt', map_location='cpu', weights_only=False)\nprint('=== maven_type_embeddings_qwen3.pt ===')\nprint('Keys:', list(d.keys()) if isinstance(d, dict) else type(d))\nif isinstance(d, dict):\n    for k,v in d.items():\n        if isinstance(v, torch.Tensor):\n            print(f'  {k}: shape={v.shape}, dtype={v.dtype}')\n        else:\n            print(f'  {k}: {v}')\n\"",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "4f8d7fab-59a8-41e3-8ef9-5af530d1bf66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSi7ZApKX8U9ZZQf9TRDx6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 23802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
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

_source line 13 · 2026-05-15T09:08:08.441Z_

<details><summary>↩ Tool result · `toolu_01KxKKPgX4tqnM4GNsyC8QQg`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "68adf114-ff66-4046-bfe2-cfceb599dfa6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TaJfTyCGkMyuJk9ULtd7rR`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && python3 -c \"\nimport torch\nd2 = torch.load('artifacts/maven_bcs_matrix_qwen3.pt', map_location='cpu', weights_only=False)\nprint('=== maven_bcs_matrix_qwen3.pt ===')\nprint('Keys:', list(d2.keys()) if isinstance(d2, dict) else type(d2))\nif isinstance(d2, dict):\n    for k,v in d2.items():\n        if isinstance(v, torch.Tensor):\n            print(f'  {k}: shape={v.shape}, dtype={v.dtype}')\n        else:\n            print(f'  {k}: {v}')\n\"",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "cf8a431c-5ca2-4c2e-946d-6bd6f1e8128d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSi7ZApKX8U9ZZQf9TRDx6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 23802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
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

_source line 15 · 2026-05-15T09:08:10.808Z_

<details><summary>↩ Tool result · `toolu_01TaJfTyCGkMyuJk9ULtd7rR`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "2d311bff-a155-4596-a544-7553711abd7a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015E4NTtQ9SictTdxtjxtYem`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/src/compute_type_embeddings.py",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "cba13783-31ec-4ba3-8274-248a65f99dc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSi7ZApKX8U9ZZQf9TRDx6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 23802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
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

_source line 17 · 2026-05-15T09:08:12.555Z_

<details><summary>↩ Tool result · `toolu_015E4NTtQ9SictTdxtjxtYem`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Compute type embeddings using a causal LM (e.g. Qwen3).\\n\\nInput: Type definitions JSON, pretrained model\\nOutput: {type_name: embedding_tensor} saved as .pt\\nDependencies: torch, transformers\\n\\\"\\\"\\\"\\nimport argparse\\nimport logging\\nfrom pathlib import Path\\n\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef compute_embeddings(\\n    model_path: str,\\n    type_definitions: dict,\\n    device: str = \\\"cuda:0\\\",\\n    batch_size: int = 8,\\n) -> dict:\\n    \\\"\\\"\\\"Compute mean-pooled last-layer hidden states for each type.\\n\\n    Args:\\n        model_path: Path to pretrained causal LM.\\n        type_definitions: {type_name: definition_text}.\\n        device: Torch device string.\\n        batch_size: Number of types to process at once.\\n\\n    Returns:\\n        Dict mapping type_name -> embedding tensor (1D, hidden_dim).\\n    \\\"\\\"\\\"\\n    logger.info(\\\"Loading model from %s\\\", model_path)\\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        model_path,\\n        torch_dtype=torch.bfloat16,\\n        device_map=device,\\n        trust_remote_code=True,\\n    )\\n    model.eval()\\n\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n\\n    type_names = list(type_definitions.keys())\\n    type_texts = [\\n        f\\\"Entity type: {name}. Definition: {defn}.\\\"\\n        for name, defn in type_definitions.items()\\n    ]\\n\\n    embeddings = {}\\n    for i in range(0, len(type_texts), batch_size):\\n        batch_names = type_names[i : i + batch_size]\\n        batch_texts = type_texts[i : i + batch_size]\\n\\n        inputs = tokenizer(\\n            batch_texts, return_tensors=\\\"pt\\\", padding=True, truncation=True, max_length=512\\n        ).to(device)\\n\\n        with torch.no_grad():\\n            outputs = model(**inputs, output_hidden_states=True)\\n\\n        last_hidden = outputs.hidden_states[-1]  # [B, seq_len, hidden_dim]\\n        attention_mask = inputs[\\\"attention_mask\\\"].unsqueeze(-1)  # [B, seq_len, 1]\\n        masked_hidden = last_hidden * attention_mask\\n        summed = masked_hidden.sum(dim=1)  # [B, hidden_dim]\\n        counts = attention_mask.sum(dim=1)  # [B, 1]\\n        mean_pooled = (summed / counts).cpu()  # [B, hidden_dim]\\n\\n        for j, name in enumerate(batch_names):\\n            embeddings[name] = mean_pooled[j]\\n\\n        logger.info(\\\"Computed embeddings for types %d-%d / %d\\\", i, i + len(batch_names), len(type_names))\\n\\n    return embeddings\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Compute type embeddings with a causal LM\\\")\\n    parser.add_argument(\\\"--model_path\\\", required=True, help=\\\"Path to pretrained model\\\")\\n    parser.add_argument(\\\"--types_file\\\", required=True, help=\\\"Type definitions JSON path\\\")\\n    parser.add_argument(\\\"--output_path\\\", required=True, help=\\\"Output .pt file path\\\")\\n    parser.add_argument(\\\"--device\\\", default=\\\"cuda:0\\\", help=\\\"Torch device\\\")\\n    parser.add_argument(\\\"--batch_size\\\", type=int, default=8, help=\\\"Batch size for encoding\\\")\\n    args = parser.parse_args()\\n\\n    logging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\n\\n    import json\\n    with open(args.types_file, \\\"r\\\") as f:\\n        type_definitions = json.load(f)\\n\\n    logger.info(\\\"Loaded %d type definitions\\\", len(type_definitions))\\n    embeddings = compute_embeddings(args.model_path, type_definitions, args.device, args.batch_size)\\n\\n    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)\\n    torch.save(embeddings, args.output_path)\\n    logger.info(\\\"Saved embeddings to %s\\\", args.output_path)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "2bca77bc-7a79-487c-ac67-84297f41603b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"Compute type embeddings using a causal LM (e.g. Qwen3).\\\\n\\\\nInput: Type definitions JSON, pretrained model\\\\nOutput: {type_name: embedding_tensor} saved as .pt\\\\nDependencies: torch, transformers\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport argparse\\\\nimport logging\\\\nfrom pathlib import Path\\\\n\\\\nimport torch\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n\\\\ndef compute_embeddings(\\\\n    model_path: str,\\\\n    type_definitions: dict,\\\\n    device: str = \\\\\\\"cuda:0\\\\\\\",\\\\n    batch_size: int = 8,\\\\n) -> dict:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute mean-pooled last-layer hidden states for each type.\\\\n\\\\n    Args:\\\\n        model_path: Path to pretrained causal LM.\\\\n        type_definitions: {type_name: definition_text}.\\\\n        device: Torch device string.\\\\n        batch_size: Number of types to process at once.\\\\n\\\\n    Returns:\\\\n        Dict mapping type_name -> embedding tensor (1D, hidden_dim).\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    logger.info(\\\\\\\"Loading model from %s\\\\\\\", model_path)\\\\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\\\\n    model = AutoModelForCausalLM.from_pretrained(\\\\n        model_path,\\\\n        torch_dtype=torch.bfloat16,\\\\n        device_map=device,\\\\n        trust_remote_code=True,\\\\n    )\\\\n    model.eval()\\\\n\\\\n    if tokenizer.pad_token is None:\\\\n        tokenizer.pad_token = tokenizer.eos_token\\\\n\\\\n    type_names = list(type_definitions.keys())\\\\n    type_texts = [\\\\n        f\\\\\\\"Entity type: {name}. Definition: {defn}.\\\\\\\"\\\\n        for name, defn in type_definitions.items()\\\\n    ]\\\\n\\\\n    embeddings = {}\\\\n    for i in range(0, len(type_texts), batch_size):\\\\n        batch_names = type_names[i : i + batch_size]\\\\n        batch_texts = type_texts[i : i + batch_size]\\\\n\\\\n        inputs = tokenizer(\\\\n            batch_texts, return_tensors=\\\\\\\"pt\\\\\\\", padding=True, truncation=True, max_length=512\\\\n        ).to(device)\\\\n\\\\n        with torch.no_grad():\\\\n            outputs = model(**inputs, output_hidden_states=True)\\\\n\\\\n        last_hidden = outputs.hidden_states[-1]  # [B, seq_len, hidden_dim]\\\\n        attention_mask = inputs[\\\\\\\"attention_mask\\\\\\\"].unsqueeze(-1)  # [B, seq_len, 1]\\\\n        masked_hidden = last_hidden * attention_mask\\\\n        summed = masked_hidden.sum(dim=1)  # [B, hidden_dim]\\\\n        counts = attention_mask.sum(dim=1)  # [B, 1]\\\\n        mean_pooled = (summed / counts).cpu()  # [B, hidden_dim]\\\\n\\\\n        for j, name in enumerate(batch_names):\\\\n            embeddings[name] = mean_pooled[j]\\\\n\\\\n        logger.info(\\\\\\\"Computed embeddings for types %d-%d / %d\\\\\\\", i, i + len(batch_names), len(type_names))\\\\n\\\\n    return embeddings\\\\n\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(description=\\\\\\\"Compute type embeddings with a causal LM\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--model_path\\\\\\\", required=True, help=\\\\\\\"Path to pretrained model\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--types_file\\\\\\\", required=True, help=\\\\\\\"Type definitions JSON path\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output_path\\\\\\\", required=True, help=\\\\\\\"Output .pt file path\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--device\\\\\\\", default=\\\\\\\"cuda:0\\\\\\\", help=\\\\\\\"Torch device\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--batch_size\\\\\\\", type=int, default=8, help=\\\\\\\"Batch size for encoding\\\\\\\")\\\\n    args = parser.parse_args()\\\\n\\\\n    logging.basicConfig(level=logging.INFO, format=\\\\\\\"%(asctime)s %(levelname)s %(message)s\\\\\\\")\\\\n\\\\n    import json\\\\n    with open(args.types_file, \\\\\\\"r\\\\\\\") as f:\\\\n        type_definitions = json.load(f)\\\\n\\\\n    logger.info(\\\\\\\"Loaded %d type definitions\\\\\\\", len(type_definitions))\\\\n    embeddings = compute_embeddings(args.model_path, type_definitions, args.device, args.batch_size)\\\\n\\\\n    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)\\\\n    torch.save(embeddings, args.output_path)\\\\n    logger.info(\\\\\\\"Saved embeddings to %s\\\\\\\", args.output_path)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Compute type embeddings using a causal LM (e.g. Qwen3).\\n\\nInput: Type definitions JSON, pretrained model\\nOutput: {type_name: embedding_tensor} saved as .pt\\nDependencies: torch, transformers\\n\\\"\\\"\\\"\\nimport argparse\\nimport logging\\nfrom pathlib import Path\\n\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef compute_embeddings(\\n    model_path: str,\\n    type_definitions: dict,\\n    device: str = \\\"cuda:0\\\",\\n    batch_size: int = 8,\\n) -> dict:\\n    \\\"\\\"\\\"Compute mean-pooled last-layer hidden states for each type.\\n\\n    Args:\\n        model_path: Path to pretrained causal LM.\\n        type_definitions: {type_name: definition_text}.\\n        device: Torch device string.\\n        batch_size: Number of types to process at once.\\n\\n    Returns:\\n        Dict mapping type_name -> embedding tensor (1D, hidden_dim).\\n    \\\"\\\"\\\"\\n    logger.info(\\\"Loading model from %s\\\", model_path)\\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        model_path,\\n        torch_dtype=torch.bfloat16,\\n        device_map=device,\\n        trust_remote_code=True,\\n    )\\n    model.eval()\\n\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n\\n    type_names = list(type_definitions.keys())\\n    type_texts = [\\n        f\\\"Entity type: {name}. Definition: {defn}.\\\"\\n        for name, defn in type_definitions.items()\\n    ]\\n\\n    embeddings = {}\\n    for i in range(0, len(type_texts), batch_size):\\n        batch_names = type_names[i : i + batch_size]\\n        batch_texts = type_texts[i : i + batch_size]\\n\\n        inputs = tokenizer(\\n            batch_texts, return_tensors=\\\"pt\\\", padding=True, truncation=True, max_length=512\\n        ).to(device)\\n\\n        with torch.no_grad():\\n            outputs = model(**inputs, output_hidden_states=True)\\n\\n        last_hidden = outputs.hidden_states[-1]  # [B, seq_len, hidden_dim]\\n        attention_mask = inputs[\\\"attention_mask\\\"].unsqueeze(-1)  # [B, seq_len, 1]\\n        masked_hidden = last_hidden * attention_mask\\n        summed = masked_hidden.sum(dim=1)  # [B, hidden_dim]\\n        counts = attention_mask.sum(dim=1)  # [B, 1]\\n        mean_pooled = (summed / counts).cpu()  # [B, hidden_dim]\\n\\n        for j, name in enumerate(batch_names):\\n            embeddings[name] = mean_pooled[j]\\n\\n        logger.info(\\\"Computed embeddings for types %d-%d / %d\\\", i, i + len(batch_names), len(type_names))\\n\\n    return embeddings\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Compute type embeddings with a causal LM\\\")\\n    parser.add_argument(\\\"--model_path\\\", required=True, help=\\\"Path to pretrained model\\\")\\n    parser.add_argument(\\\"--types_file\\\", required=True, help=\\\"Type definitions JSON path\\\")\\n    parser.add_argument(\\\"--output_path\\\", required=True, help=\\\"Output .pt file path\\\")\\n    parser.add_argument(\\\"--device\\\", default=\\\"cuda:0\\\", help=\\\"Torch device\\\")\\n    parser.add_argument(\\\"--batch_size\\\", type=int, default=8, help=\\\"Batch size for encoding\\\")\\n    args = parser.parse_args()\\n\\n    logging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\n\\n    import json\\n    with open(args.types_file, \\\"r\\\") as f:\\n        type_definitions = json.load(f)\\n\\n    logger.info(\\\"Loaded %d type definitions\\\", len(type_definitions))\\n    embeddings = compute_embeddings(args.model_path, type_definitions, args.device, args.batch_size)\\n\\n    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)\\n    torch.save(embeddings, args.output_path)\\n    logger.info(\\\"Saved embeddings to %s\\\", args.output_path)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.44}}"
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
The `ssh_read_only` tool blocks `&&` and `cd`. I need to use `python3 -c` with the full path, no `cd`. Let me adjust - the python3 -c commands use `&&` implicitly through `cd`. Let me use ssh_execute for the python commands since they need to change directory, or I can use absolute paths in the torch.load calls.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "81eaed15-e716-4c2f-a31e-a7b453fe6497",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144yBNP3RFm4NfehP7zV6kH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 24527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3117
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

代码已确认使用 `AutoModelForCausalLM` + mean pooling。现在检查 embedding 文件的实际维度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "f2b7a67c-bac7-4a1e-851a-56189cbd6fd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144yBNP3RFm4NfehP7zV6kH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 24527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3117
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016cBP6FNNWKLprLc4YuyDEu`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "python3 -c \"\nimport torch\nd = torch.load('/root/schema-dag-extraction/artifacts/type_embeddings.pt', map_location='cpu', weights_only=False)\nprint('=== type_embeddings.pt ===')\nprint('Type:', type(d))\nif isinstance(d, dict):\n    print('Keys count:', len(d))\n    for k,v in list(d.items())[:3]:\n        if isinstance(v, torch.Tensor):\n            print(f'  {k}: shape={v.shape}, dtype={v.dtype}')\n        else:\n            print(f'  {k}: {type(v)} = {v}')\n    meta_keys = [k for k in d if 'model' in k.lower() or 'meta' in k.lower() or 'config' in k.lower()]\n    if meta_keys:\n        print('Metadata keys:', meta_keys)\n        for mk in meta_keys:\n            print(f'  {mk}: {d[mk]}')\n\"",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "57d4de39-a871-41ae-91ca-fe3b227d59d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144yBNP3RFm4NfehP7zV6kH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 24527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3117
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

_source line 21 · 2026-05-15T09:08:21.906Z_

<details><summary>↩ Tool result · `toolu_016cBP6FNNWKLprLc4YuyDEu`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "e4a82181-1159-468d-b448-cdde4822772d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"bash: line 1: python3: command not found\\\\n\\\", \\\"return_code\\\": 127}, \\\"error\\\": \\\"exit code 127\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VasizpPooQ942jRUrU24eS`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "python3 -c \"\nimport torch\nd = torch.load('/root/schema-dag-extraction/artifacts/sim_matrix.pt', map_location='cpu', weights_only=False)\nprint('=== sim_matrix.pt ===')\nprint('Type:', type(d))\nif isinstance(d, dict):\n    for k,v in d.items():\n        if isinstance(v, torch.Tensor):\n            print(f'  {k}: shape={v.shape}, dtype={v.dtype}')\n        else:\n            print(f'  {k}: {v}')\nelif isinstance(d, torch.Tensor):\n    print(f'Tensor: shape={d.shape}, dtype={d.dtype}')\n\"",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "fcef3d91-bf0e-4047-ad6d-0c5891095026",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144yBNP3RFm4NfehP7zV6kH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 24527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3117
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

_source line 23 · 2026-05-15T09:08:23.818Z_

<details><summary>↩ Tool result · `toolu_01VasizpPooQ942jRUrU24eS`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "f627b5c8-9e6d-4c93-8f14-bfb7eb6424e1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"bash: line 1: python3: command not found\\\\n\\\", \\\"return_code\\\": 127}, \\\"error\\\": \\\"exit code 127\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011M4Ct4yG34rvS9nKpyepVz`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "python3 -c \"\nimport torch\nd = torch.load('/root/schema-dag-extraction/artifacts/maven_type_embeddings_qwen3.pt', map_location='cpu', weights_only=False)\nprint('=== maven_type_embeddings_qwen3.pt ===')\nprint('Type:', type(d))\nif isinstance(d, dict):\n    print('Keys count:', len(d))\n    for k,v in list(d.items())[:3]:\n        if isinstance(v, torch.Tensor):\n            print(f'  {k}: shape={v.shape}, dtype={v.dtype}')\n        else:\n            print(f'  {k}: {type(v)} = {v}')\n    meta_keys = [k for k in d if 'model' in k.lower() or 'meta' in k.lower() or 'config' in k.lower()]\n    if meta_keys:\n        print('Metadata keys:', meta_keys)\n        for mk in meta_keys:\n            print(f'  {mk}: {d[mk]}')\n\"",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "bf7736bd-8ec4-49dc-8c0b-5fe5c34462b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144yBNP3RFm4NfehP7zV6kH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 24527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3117
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

_source line 25 · 2026-05-15T09:08:26.621Z_

<details><summary>↩ Tool result · `toolu_011M4Ct4yG34rvS9nKpyepVz`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "8f93d3d2-ba55-4984-b86a-8d660bc04b83",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"bash: line 1: python3: command not found\\\\n\\\", \\\"return_code\\\": 127}, \\\"error\\\": \\\"exit code 127\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016zHpLQxFUmYVuTFn6ZUMiY`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "python3 -c \"\nimport torch\nd = torch.load('/root/schema-dag-extraction/artifacts/maven_bcs_matrix_qwen3.pt', map_location='cpu', weights_only=False)\nprint('=== maven_bcs_matrix_qwen3.pt ===')\nprint('Type:', type(d))\nif isinstance(d, dict):\n    for k,v in d.items():\n        if isinstance(v, torch.Tensor):\n            print(f'  {k}: shape={v.shape}, dtype={v.dtype}')\n        else:\n            print(f'  {k}: {v}')\nelif isinstance(d, torch.Tensor):\n    print(f'Tensor: shape={d.shape}, dtype={d.dtype}')\n\"",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "7efc1ad5-46b8-4edc-a9e2-de6a1d454383",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144yBNP3RFm4NfehP7zV6kH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 24527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3117
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

_source line 27 · 2026-05-15T09:08:28.246Z_

<details><summary>↩ Tool result · `toolu_016zHpLQxFUmYVuTFn6ZUMiY`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "a393c9f6-d94c-4396-bd9e-543525540d7a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"bash: line 1: python3: command not found\\\\n\\\", \\\"return_code\\\": 127}, \\\"error\\\": \\\"exit code 127\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.4}}"
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
The python3 command is not found because conda is not activated. I need to use `ssh_execute` to source conda first, or use the full path to python. Let me use `/root/miniconda3/bin/python3`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "e1e4bb3f-2b39-4a7a-ad91-2dfd67d3d1ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MdvJJeupGRhgnUzoqvzDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 27644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1951
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

需要用 conda 环境的 python。改用 ssh_execute。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "54d6c80b-6310-42df-a294-27108f64bffa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MdvJJeupGRhgnUzoqvzDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 27644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1951
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01GAyoXi1FXTNjkuzGjtfJvV`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport torch\nd = torch.load('/root/schema-dag-extraction/artifacts/type_embeddings.pt', map_location='cpu', weights_only=False)\nprint('=== type_embeddings.pt ===')\nprint('Type:', type(d))\nif isinstance(d, dict):\n    print('Keys count:', len(d))\n    for k,v in list(d.items())[:3]:\n        if isinstance(v, torch.Tensor):\n            print(f'  {k}: shape={v.shape}, dtype={v.dtype}')\n        else:\n            print(f'  {k}: {type(v)} = {v}')\n    meta_keys = [k for k in d if 'model' in k.lower() or 'meta' in k.lower() or 'config' in k.lower()]\n    if meta_keys:\n        print('Metadata keys:', meta_keys)\n        for mk in meta_keys:\n            print(f'  {mk}: {d[mk]}')\n\"\n",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "ce2fa2f9-3950-4f17-b273-1c18652437c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MdvJJeupGRhgnUzoqvzDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 27644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1951
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

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_015JtvjdLzEGp8aGzabP8VXp`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport torch\nd = torch.load('/root/schema-dag-extraction/artifacts/sim_matrix.pt', map_location='cpu', weights_only=False)\nprint('=== sim_matrix.pt ===')\nprint('Type:', type(d))\nif isinstance(d, dict):\n    for k,v in d.items():\n        if isinstance(v, torch.Tensor):\n            print(f'  {k}: shape={v.shape}, dtype={v.dtype}')\n        else:\n            print(f'  {k}: {v}')\nelif isinstance(d, torch.Tensor):\n    print(f'Tensor: shape={d.shape}, dtype={d.dtype}')\n\"\n",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "df69490f-d348-450f-b110-82d3f1162b95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MdvJJeupGRhgnUzoqvzDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 27644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1951
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01JP5caYBi1dHPkp2NstzeiE`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport torch\nd = torch.load('/root/schema-dag-extraction/artifacts/maven_type_embeddings_qwen3.pt', map_location='cpu', weights_only=False)\nprint('=== maven_type_embeddings_qwen3.pt ===')\nprint('Type:', type(d))\nif isinstance(d, dict):\n    print('Keys count:', len(d))\n    for k,v in list(d.items())[:3]:\n        if isinstance(v, torch.Tensor):\n            print(f'  {k}: shape={v.shape}, dtype={v.dtype}')\n        else:\n            print(f'  {k}: {type(v)} = {v}')\n    meta_keys = [k for k in d if 'model' in k.lower() or 'meta' in k.lower() or 'config' in k.lower()]\n    if meta_keys:\n        print('Metadata keys:', meta_keys)\n        for mk in meta_keys:\n            print(f'  {mk}: {d[mk]}')\n\"\n",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "e95d3c07-086b-43e5-9bcd-4199cebb5c14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MdvJJeupGRhgnUzoqvzDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 27644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1951
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

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01R7LwumJ4g7gWj6S7KEG5JF`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport torch\nd = torch.load('/root/schema-dag-extraction/artifacts/maven_bcs_matrix_qwen3.pt', map_location='cpu', weights_only=False)\nprint('=== maven_bcs_matrix_qwen3.pt ===')\nprint('Type:', type(d))\nif isinstance(d, dict):\n    for k,v in d.items():\n        if isinstance(v, torch.Tensor):\n            print(f'  {k}: shape={v.shape}, dtype={v.dtype}')\n        else:\n            print(f'  {k}: {v}')\nelif isinstance(d, torch.Tensor):\n    print(f'Tensor: shape={d.shape}, dtype={d.dtype}')\n\"\n",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "acb2724f-0087-49c8-9121-0d13538afa4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MdvJJeupGRhgnUzoqvzDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 27644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1951
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

_source line 34 · 2026-05-15T09:08:42.772Z_

<details><summary>↩ Tool result · `toolu_01GAyoXi1FXTNjkuzGjtfJvV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== type_embeddings.pt ===\\nType: &lt;class 'dict'>\\nKeys count: 66\\n  person-actor: shape=torch.Size([5120]), dtype=torch.bfloat16\\n  person-artist/author: shape=torch.Size([5120]), dtype=torch.bfloat16\\n  person-athlete: shape=torch.Size([5120]), dtype=torch.bfloat16\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "096ecfce-db3c-4b45-99af-31be168f6a18",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== type_embeddings.pt ===\\\\nType: &lt;class 'dict'>\\\\nKeys count: 66\\\\n  person-actor: shape=torch.Size([5120]), dtype=torch.bfloat16\\\\n  person-artist/author: shape=torch.Size([5120]), dtype=torch.bfloat16\\\\n  person-athlete: shape=torch.Size([5120]), dtype=torch.bfloat16\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== type_embeddings.pt ===\\nType: &lt;class 'dict'>\\nKeys count: 66\\n  person-actor: shape=torch.Size([5120]), dtype=torch.bfloat16\\n  person-artist/author: shape=torch.Size([5120]), dtype=torch.bfloat16\\n  person-athlete: shape=torch.Size([5120]), dtype=torch.bfloat16\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.49}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-15T09:08:51.311Z_

<details><summary>↩ Tool result · `toolu_015JtvjdLzEGp8aGzabP8VXp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== sim_matrix.pt ===\\nType: &lt;class 'dict'>\\n  sim_matrix: shape=torch.Size([66, 66]), dtype=torch.float32\\n  type_names: ['art-broadcastprogram', 'art-film', 'art-music', 'art-other', 'art-painting', 'art-writtenart', 'building-airport', 'building-hospital', 'building-hotel', 'building-library', 'building-other', 'building-restaurant', 'building-sportsfacility', 'building-theater', 'event-attack/battle/war/militaryconflict', 'event-disaster', 'event-election', 'event-other', 'event-protest', 'event-sportsevent', 'location-GPE', 'location-bodiesofwater', 'location-island', 'location-mountain', 'location-other', 'location-park', 'location-road/railway/highway/transit', 'organization-company', 'organization-education', 'organization-government/governmentagency', 'organization-media/newspaper', 'organization-other', 'organization-politicalparty', 'organization-religion', 'organization-showorganization', 'organization-sportsleague', 'organization-sportsteam', 'other-astronomything', 'other-award', 'other-biologything', 'other-chemicalthing', 'other-currency', 'other-disease', 'other-educationaldegree', 'other-god', 'other-language', 'other-law', 'other-livingthing', 'other-medical', 'person-actor', 'person-artist/author', 'person-athlete', 'person-director', 'person-other', 'person-politician', 'person-scholar', 'person-soldier', 'product-airplane', 'product-car', 'product-food', 'product-game', 'product-other', 'product-ship', 'product-software', 'product-train', 'product-weapon']\\n  type_to_idx: {'art-broadcastprogram': 0, 'art-film': 1, 'art-music': 2, 'art-other': 3, 'art-painting': 4, 'art-writtenart': 5, 'building-airport': 6, 'building-hospital': 7, 'building-hotel': 8, 'building-library': 9, 'building-other': 10, 'building-restaurant': 11, 'building-sportsfacility': 12, 'building-theater': 13, 'event-attack/battle/war/militaryconflict': 14, 'event-disaster': 15, 'event-election': 16, 'event-other': 17, 'event-protest': 18, 'event-sportsevent': 19, 'location-GPE': 20, 'location-bodiesofwater': 21, 'location-island': 22, 'location-mountain': 23, 'location-other': 24, 'location-park': 25, 'location-road/railway/highway/transit': 26, 'organization-company': 27, 'organization-education': 28, 'organization-government/governmentagency': 29, 'organization-media/newspaper': 30, 'organization-other': 31, 'organization-politicalparty': 32, 'organization-religion': 33, 'organization-showorganization': 34, 'organization-sportsleague': 35, 'organization-sportsteam': 36, 'other-astronomything': 37, 'other-award': 38, 'other-biologything': 39, 'other-chemicalthing': 40, 'other-currency': 41, 'other-disease': 42, 'other-educationaldegree': 43, 'other-god': 44, 'other-language': 45, 'other-law': 46, 'other-livingthing': 47, 'other-medical': 48, 'person-actor': 49, 'person-artist/author': 50, 'person-athlete': 51, 'person-director': 52, 'person-other': 53, 'person-politician': 54, 'person-scholar': 55, 'person-soldier': 56, 'product-airplane': 57, 'product-car': 58, 'product-food': 59, 'product-game': 60, 'product-other': 61, 'product-ship': 62, 'product-software': 63, 'product-train': 64, 'product-weapon': 65}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "da28e73b-f943-4e27-a5bd-4ec99001067f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== sim_matrix.pt ===\\\\nType: &lt;class 'dict'>\\\\n  sim_matrix: shape=torch.Size([66, 66]), dtype=torch.float32\\\\n  type_names: ['art-broadcastprogram', 'art-film', 'art-music', 'art-other', 'art-painting', 'art-writtenart', 'building-airport', 'building-hospital', 'building-hotel', 'building-library', 'building-other', 'building-restaurant', 'building-sportsfacility', 'building-theater', 'event-attack/battle/war/militaryconflict', 'event-disaster', 'event-election', 'event-other', 'event-protest', 'event-sportsevent', 'location-GPE', 'location-bodiesofwater', 'location-island', 'location-mountain', 'location-other', 'location-park', 'location-road/railway/highway/transit', 'organization-company', 'organization-education', 'organization-government/governmentagency', 'organization-media/newspaper', 'organization-other', 'organization-politicalparty', 'organization-religion', 'organization-showorganization', 'organization-sportsleague', 'organization-sportsteam', 'other-astronomything', 'other-award', 'other-biologything', 'other-chemicalthing', 'other-currency', 'other-disease', 'other-educationaldegree', 'other-god', 'other-language', 'other-law', 'other-livingthing', 'other-medical', 'person-actor', 'person-artist/author', 'person-athlete', 'person-director', 'person-other', 'person-politician', 'person-scholar', 'person-soldier', 'product-airplane', 'product-car', 'product-food', 'product-game', 'product-other', 'product-ship', 'product-software', 'product-train', 'product-weapon']\\\\n  type_to_idx: {'art-broadcastprogram': 0, 'art-film': 1, 'art-music': 2, 'art-other': 3, 'art-painting': 4, 'art-writtenart': 5, 'building-airport': 6, 'building-hospital': 7, 'building-hotel': 8, 'building-library': 9, 'building-other': 10, 'building-restaurant': 11, 'building-sportsfacility': 12, 'building-theater': 13, 'event-attack/battle/war/militaryconflict': 14, 'event-disaster': 15, 'event-election': 16, 'event-other': 17, 'event-protest': 18, 'event-sportsevent': 19, 'location-GPE': 20, 'location-bodiesofwater': 21, 'location-island': 22, 'location-mountain': 23, 'location-other': 24, 'location-park': 25, 'location-road/railway/highway/transit': 26, 'organization-company': 27, 'organization-education': 28, 'organization-government/governmentagency': 29, 'organization-media/newspaper': 30, 'organization-other': 31, 'organization-politicalparty': 32, 'organization-religion': 33, 'organization-showorganization': 34, 'organization-sportsleague': 35, 'organization-sportsteam': 36, 'other-astronomything': 37, 'other-award': 38, 'other-biologything': 39, 'other-chemicalthing': 40, 'other-currency': 41, 'other-disease': 42, 'other-educationaldegree': 43, 'other-god': 44, 'other-language': 45, 'other-law': 46, 'other-livingthing': 47, 'other-medical': 48, 'person-actor': 49, 'person-artist/author': 50, 'person-athlete': 51, 'person-director': 52, 'person-other': 53, 'person-politician': 54, 'person-scholar': 55, 'person-soldier': 56, 'product-airplane': 57, 'product-car': 58, 'product-food': 59, 'product-game': 60, 'product-other': 61, 'product-ship': 62, 'product-software': 63, 'product-train': 64, 'product-weapon': 65}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== sim_matrix.pt ===\\nType: &lt;class 'dict'>\\n  sim_matrix: shape=torch.Size([66, 66]), dtype=torch.float32\\n  type_names: ['art-broadcastprogram', 'art-film', 'art-music', 'art-other', 'art-painting', 'art-writtenart', 'building-airport', 'building-hospital', 'building-hotel', 'building-library', 'building-other', 'building-restaurant', 'building-sportsfacility', 'building-theater', 'event-attack/battle/war/militaryconflict', 'event-disaster', 'event-election', 'event-other', 'event-protest', 'event-sportsevent', 'location-GPE', 'location-bodiesofwater', 'location-island', 'location-mountain', 'location-other', 'location-park', 'location-road/railway/highway/transit', 'organization-company', 'organization-education', 'organization-government/governmentagency', 'organization-media/newspaper', 'organization-other', 'organization-politicalparty', 'organization-religion', 'organization-showorganization', 'organization-sportsleague', 'organization-sportsteam', 'other-astronomything', 'other-award', 'other-biologything', 'other-chemicalthing', 'other-currency', 'other-disease', 'other-educationaldegree', 'other-god', 'other-language', 'other-law', 'other-livingthing', 'other-medical', 'person-actor', 'person-artist/author', 'person-athlete', 'person-director', 'person-other', 'person-politician', 'person-scholar', 'person-soldier', 'product-airplane', 'product-car', 'product-food', 'product-game', 'product-other', 'product-ship', 'product-software', 'product-train', 'product-weapon']\\n  type_to_idx: {'art-broadcastprogram': 0, 'art-film': 1, 'art-music': 2, 'art-other': 3, 'art-painting': 4, 'art-writtenart': 5, 'building-airport': 6, 'building-hospital': 7, 'building-hotel': 8, 'building-library': 9, 'building-other': 10, 'building-restaurant': 11, 'building-sportsfacility': 12, 'building-theater': 13, 'event-attack/battle/war/militaryconflict': 14, 'event-disaster': 15, 'event-election': 16, 'event-other': 17, 'event-protest': 18, 'event-sportsevent': 19, 'location-GPE': 20, 'location-bodiesofwater': 21, 'location-island': 22, 'location-mountain': 23, 'location-other': 24, 'location-park': 25, 'location-road/railway/highway/transit': 26, 'organization-company': 27, 'organization-education': 28, 'organization-government/governmentagency': 29, 'organization-media/newspaper': 30, 'organization-other': 31, 'organization-politicalparty': 32, 'organization-religion': 33, 'organization-showorganization': 34, 'organization-sportsleague': 35, 'organization-sportsteam': 36, 'other-astronomything': 37, 'other-award': 38, 'other-biologything': 39, 'other-chemicalthing': 40, 'other-currency': 41, 'other-disease': 42, 'other-educationaldegree': 43, 'other-god': 44, 'other-language': 45, 'other-law': 46, 'other-livingthing': 47, 'other-medical': 48, 'person-actor': 49, 'person-artist/author': 50, 'person-athlete': 51, 'person-director': 52, 'person-other': 53, 'person-politician': 54, 'person-scholar': 55, 'person-soldier': 56, 'product-airplane': 57, 'product-car': 58, 'product-food': 59, 'product-game': 60, 'product-other': 61, 'product-ship': 62, 'product-software': 63, 'product-train': 64, 'product-weapon': 65}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.53}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-15T09:09:00.171Z_

<details><summary>↩ Tool result · `toolu_01JP5caYBi1dHPkp2NstzeiE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== maven_type_embeddings_qwen3.pt ===\\nType: &lt;class 'dict'>\\nKeys count: 168\\n  Achieve: shape=torch.Size([5120]), dtype=torch.bfloat16\\n  Action: shape=torch.Size([5120]), dtype=torch.bfloat16\\n  Adducing: shape=torch.Size([5120]), dtype=torch.bfloat16\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.85}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "c449d300-374a-4dba-a388-a51b38d69235",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== maven_type_embeddings_qwen3.pt ===\\\\nType: &lt;class 'dict'>\\\\nKeys count: 168\\\\n  Achieve: shape=torch.Size([5120]), dtype=torch.bfloat16\\\\n  Action: shape=torch.Size([5120]), dtype=torch.bfloat16\\\\n  Adducing: shape=torch.Size([5120]), dtype=torch.bfloat16\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.85}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== maven_type_embeddings_qwen3.pt ===\\nType: &lt;class 'dict'>\\nKeys count: 168\\n  Achieve: shape=torch.Size([5120]), dtype=torch.bfloat16\\n  Action: shape=torch.Size([5120]), dtype=torch.bfloat16\\n  Adducing: shape=torch.Size([5120]), dtype=torch.bfloat16\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.85}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-15T09:09:08.931Z_

<details><summary>↩ Tool result · `toolu_01R7LwumJ4g7gWj6S7KEG5JF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== maven_bcs_matrix_qwen3.pt ===\\nType: &lt;class 'dict'>\\n  similarity_matrix: shape=torch.Size([168, 168]), dtype=torch.float32\\n  type_names: ['Achieve', 'Action', 'Adducing', 'Agree_or_refuse_to_act', 'Aiming', 'Arranging', 'Arrest', 'Arriving', 'Assistance', 'Attack', 'Award', 'Bearing_arms', 'Becoming', 'Becoming_a_member', 'Being_in_operation', 'Besieging', 'Bodily_harm', 'Body_movement', 'Breathing', 'Bringing', 'Building', 'Carry_goods', 'Catastrophe', 'Causation', 'Cause_change_of_position_on_a_scale', 'Cause_change_of_strength', 'Cause_to_amalgamate', 'Cause_to_be_included', 'Cause_to_make_progress', 'Change', 'Change_event_time', 'Change_of_leadership', 'Change_sentiment', 'Change_tool', 'Check', 'Choosing', 'Collaboration', 'Come_together', 'Coming_to_be', 'Coming_to_believe', 'Commerce_buy', 'Commerce_pay', 'Commerce_sell', 'Commitment', 'Committing_crime', 'Communication', 'Competition', 'Confronting_problem', 'Connect', 'Conquering', 'Containing', 'Control', 'Convincing', 'Cost', 'Create_artwork', 'Creating', 'Criminal_investigation', 'Cure', 'Damaging', 'Death', 'Deciding', 'Defending', 'Departing', 'Destroying', 'Dispersal', 'Earnings_and_losses', 'Education_teaching', 'Emergency', 'Employment', 'Emptying', 'Escaping', 'Exchange', 'Expansion', 'Expend_resource', 'Expressing_publicly', 'Extradition', 'Filling', 'Forming_relationships', 'GetReady', 'Getting', 'GiveUp', 'Giving', 'Having_or_lacking_access', 'Hiding_objects', 'Hindering', 'Hold', 'Hostile_encounter', 'Imposing_obligation', 'Incident', 'Influence', 'Ingestion', 'Institutionalization', 'Judgment_communication', 'Justifying', 'Kidnapping', 'Killing', 'Know', 'Labeling', 'Legal_rulings', 'Legality', 'Lighting', 'Limiting', 'Manufacturing', 'Military_operation', 'Motion', 'Motion_directional', 'Name_conferral', 'Openness', 'Participation', 'Patrolling', 'Perception_active', 'Placing', 'Practice', 'Presence', 'Preserving', 'Preventing_or_letting', 'Prison', 'Process_end', 'Process_start', 'Protest', 'Publishing', 'Quarreling', 'Ratification', 'Receiving', 'Recording', 'Recovering', 'Reforming_a_system', 'Releasing', 'Removing', 'Renting', 'Reporting', 'Request', 'Rescuing', 'Research', 'Resolve_problem', 'Response', 'Reveal_secret', 'Revenge', 'Rewards_and_punishments', 'Risk', 'Rite', 'Robbery', 'Scouring', 'Scrutiny', 'Self_motion', 'Sending', 'Sign_agreement', 'Social_event', 'Statement', 'Submitting_documents', 'Supply', 'Supporting', 'Surrendering', 'Surrounding', 'Suspicion', 'Telling', 'Temporary_stay', 'Terrorism', 'Testing', 'Theft', 'Traveling', 'Use_firearm', 'Using', 'Violence', 'Vocalizations', 'Warning', 'Wearing', 'Writing']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.75}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "556dfefd-7664-41b1-a707-41022ec584bc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== maven_bcs_matrix_qwen3.pt ===\\\\nType: &lt;class 'dict'>\\\\n  similarity_matrix: shape=torch.Size([168, 168]), dtype=torch.float32\\\\n  type_names: ['Achieve', 'Action', 'Adducing', 'Agree_or_refuse_to_act', 'Aiming', 'Arranging', 'Arrest', 'Arriving', 'Assistance', 'Attack', 'Award', 'Bearing_arms', 'Becoming', 'Becoming_a_member', 'Being_in_operation', 'Besieging', 'Bodily_harm', 'Body_movement', 'Breathing', 'Bringing', 'Building', 'Carry_goods', 'Catastrophe', 'Causation', 'Cause_change_of_position_on_a_scale', 'Cause_change_of_strength', 'Cause_to_amalgamate', 'Cause_to_be_included', 'Cause_to_make_progress', 'Change', 'Change_event_time', 'Change_of_leadership', 'Change_sentiment', 'Change_tool', 'Check', 'Choosing', 'Collaboration', 'Come_together', 'Coming_to_be', 'Coming_to_believe', 'Commerce_buy', 'Commerce_pay', 'Commerce_sell', 'Commitment', 'Committing_crime', 'Communication', 'Competition', 'Confronting_problem', 'Connect', 'Conquering', 'Containing', 'Control', 'Convincing', 'Cost', 'Create_artwork', 'Creating', 'Criminal_investigation', 'Cure', 'Damaging', 'Death', 'Deciding', 'Defending', 'Departing', 'Destroying', 'Dispersal', 'Earnings_and_losses', 'Education_teaching', 'Emergency', 'Employment', 'Emptying', 'Escaping', 'Exchange', 'Expansion', 'Expend_resource', 'Expressing_publicly', 'Extradition', 'Filling', 'Forming_relationships', 'GetReady', 'Getting', 'GiveUp', 'Giving', 'Having_or_lacking_access', 'Hiding_objects', 'Hindering', 'Hold', 'Hostile_encounter', 'Imposing_obligation', 'Incident', 'Influence', 'Ingestion', 'Institutionalization', 'Judgment_communication', 'Justifying', 'Kidnapping', 'Killing', 'Know', 'Labeling', 'Legal_rulings', 'Legality', 'Lighting', 'Limiting', 'Manufacturing', 'Military_operation', 'Motion', 'Motion_directional', 'Name_conferral', 'Openness', 'Participation', 'Patrolling', 'Perception_active', 'Placing', 'Practice', 'Presence', 'Preserving', 'Preventing_or_letting', 'Prison', 'Process_end', 'Process_start', 'Protest', 'Publishing', 'Quarreling', 'Ratification', 'Receiving', 'Recording', 'Recovering', 'Reforming_a_system', 'Releasing', 'Removing', 'Renting', 'Reporting', 'Request', 'Rescuing', 'Research', 'Resolve_problem', 'Response', 'Reveal_secret', 'Revenge', 'Rewards_and_punishments', 'Risk', 'Rite', 'Robbery', 'Scouring', 'Scrutiny', 'Self_motion', 'Sending', 'Sign_agreement', 'Social_event', 'Statement', 'Submitting_documents', 'Supply', 'Supporting', 'Surrendering', 'Surrounding', 'Suspicion', 'Telling', 'Temporary_stay', 'Terrorism', 'Testing', 'Theft', 'Traveling', 'Use_firearm', 'Using', 'Violence', 'Vocalizations', 'Warning', 'Wearing', 'Writing']\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.75}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== maven_bcs_matrix_qwen3.pt ===\\nType: &lt;class 'dict'>\\n  similarity_matrix: shape=torch.Size([168, 168]), dtype=torch.float32\\n  type_names: ['Achieve', 'Action', 'Adducing', 'Agree_or_refuse_to_act', 'Aiming', 'Arranging', 'Arrest', 'Arriving', 'Assistance', 'Attack', 'Award', 'Bearing_arms', 'Becoming', 'Becoming_a_member', 'Being_in_operation', 'Besieging', 'Bodily_harm', 'Body_movement', 'Breathing', 'Bringing', 'Building', 'Carry_goods', 'Catastrophe', 'Causation', 'Cause_change_of_position_on_a_scale', 'Cause_change_of_strength', 'Cause_to_amalgamate', 'Cause_to_be_included', 'Cause_to_make_progress', 'Change', 'Change_event_time', 'Change_of_leadership', 'Change_sentiment', 'Change_tool', 'Check', 'Choosing', 'Collaboration', 'Come_together', 'Coming_to_be', 'Coming_to_believe', 'Commerce_buy', 'Commerce_pay', 'Commerce_sell', 'Commitment', 'Committing_crime', 'Communication', 'Competition', 'Confronting_problem', 'Connect', 'Conquering', 'Containing', 'Control', 'Convincing', 'Cost', 'Create_artwork', 'Creating', 'Criminal_investigation', 'Cure', 'Damaging', 'Death', 'Deciding', 'Defending', 'Departing', 'Destroying', 'Dispersal', 'Earnings_and_losses', 'Education_teaching', 'Emergency', 'Employment', 'Emptying', 'Escaping', 'Exchange', 'Expansion', 'Expend_resource', 'Expressing_publicly', 'Extradition', 'Filling', 'Forming_relationships', 'GetReady', 'Getting', 'GiveUp', 'Giving', 'Having_or_lacking_access', 'Hiding_objects', 'Hindering', 'Hold', 'Hostile_encounter', 'Imposing_obligation', 'Incident', 'Influence', 'Ingestion', 'Institutionalization', 'Judgment_communication', 'Justifying', 'Kidnapping', 'Killing', 'Know', 'Labeling', 'Legal_rulings', 'Legality', 'Lighting', 'Limiting', 'Manufacturing', 'Military_operation', 'Motion', 'Motion_directional', 'Name_conferral', 'Openness', 'Participation', 'Patrolling', 'Perception_active', 'Placing', 'Practice', 'Presence', 'Preserving', 'Preventing_or_letting', 'Prison', 'Process_end', 'Process_start', 'Protest', 'Publishing', 'Quarreling', 'Ratification', 'Receiving', 'Recording', 'Recovering', 'Reforming_a_system', 'Releasing', 'Removing', 'Renting', 'Reporting', 'Request', 'Rescuing', 'Research', 'Resolve_problem', 'Response', 'Reveal_secret', 'Revenge', 'Rewards_and_punishments', 'Risk', 'Rite', 'Robbery', 'Scouring', 'Scrutiny', 'Self_motion', 'Sending', 'Sign_agreement', 'Social_event', 'Statement', 'Submitting_documents', 'Supply', 'Supporting', 'Surrendering', 'Surrounding', 'Suspicion', 'Telling', 'Temporary_stay', 'Terrorism', 'Testing', 'Theft', 'Traveling', 'Use_firearm', 'Using', 'Violence', 'Vocalizations', 'Warning', 'Wearing', 'Writing']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.75}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 38_

再查一下是否有调用记录或 shell history 能确认 `--model_path` 传了什么。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "ab65bc73-b855-4325-a972-b3f5148665cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UGRLU1CR8FJUh7KZDhhBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4235,
      "cache_read_input_tokens": 29595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4235
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

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SKb7KtbsUb5H5aoWeFZEGc`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -r \"compute_type_embeddings\" /root/schema-dag-extraction/ --include=\"*.sh\" --include=\"*.py\" --include=\"*.log\" -l",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "c7ff9b1a-9086-4bb3-9d3b-639160c17405",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UGRLU1CR8FJUh7KZDhhBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4235,
      "cache_read_input_tokens": 29595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4235
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

_source line 40 · 2026-05-15T09:09:13.949Z_

<details><summary>↩ Tool result · `toolu_01SKb7KtbsUb5H5aoWeFZEGc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema-dag-extraction/src/run_experiment.py\\n/root/schema-dag-extraction/src/run_fewrel_formal.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "da3db13d-62b8-4a53-aa13-d6cf047f72cb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/schema-dag-extraction/src/run_experiment.py\\\\n/root/schema-dag-extraction/src/run_fewrel_formal.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/schema-dag-extraction/src/run_experiment.py\\n/root/schema-dag-extraction/src/run_fewrel_formal.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YTNRwCEW3guqqen2vArrPr`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -rn \"compute_type_embeddings\\|type_embeddings\\|model_path\" /root/schema-dag-extraction/scripts/ --include=\"*.sh\"",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "0046202d-fd1d-40c3-a4e8-8a7b2ba29cdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UGRLU1CR8FJUh7KZDhhBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4235,
      "cache_read_input_tokens": 29595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4235
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

_source line 42 · 2026-05-15T09:09:15.080Z_

<details><summary>↩ Tool result · `toolu_01YTNRwCEW3guqqen2vArrPr`</summary>

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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "69a868a0-c921-4690-a2f5-444c7093712e",
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

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KtKHhALXhMLqVmDYuKgaUF`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep \"compute_type_embeddings\" /root/.bash_history",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "a9e77261-1598-4829-8a19-4cdafc043bdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UGRLU1CR8FJUh7KZDhhBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4235,
      "cache_read_input_tokens": 29595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4235
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

_source line 44 · 2026-05-15T09:09:15.858Z_

<details><summary>↩ Tool result · `toolu_01KtKHhALXhMLqVmDYuKgaUF`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/.bash_history: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "60b20ca0-452e-49b5-9a37-88026bd0ea9b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"grep: /root/.bash_history: No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/.bash_history: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UGhtH34CNfTWGMTxB1XPxw`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -n \"compute_type_embeddings\\|model_path\\|Qwen\" /root/schema-dag-extraction/src/run_experiment.py",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "5a73690d-8a0f-4418-a286-125d3a0ce963",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011A4zvZxm1YruudiKGMbPET",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 33830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 785
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

_source line 46 · 2026-05-15T09:09:19.067Z_

<details><summary>↩ Tool result · `toolu_01UGhtH34CNfTWGMTxB1XPxw`</summary>

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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "b2b96e6c-cc5e-48c8-a220-7d8422d75dfd",
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

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SdVQabcQWEimsrdnwS8RpL`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -n \"compute_type_embeddings\\|model_path\\|Qwen\" /root/schema-dag-extraction/src/run_fewrel_formal.py",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "d7a6a358-a85d-4b43-9fb3-2a8ad7ef4278",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011A4zvZxm1YruudiKGMbPET",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 33830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 785
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

_source line 48 · 2026-05-15T09:09:20.026Z_

<details><summary>↩ Tool result · `toolu_01SdVQabcQWEimsrdnwS8RpL`</summary>

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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "f7134816-98f6-4653-a962-43294baa63b7",
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

_source line 49_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01F6TdVGGCvr9GmxTRvetbqe`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls /root/schema-dag-extraction/scripts/",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "73a02127-00d9-4f7a-b92f-b7b848f87837",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011A4zvZxm1YruudiKGMbPET",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 33830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 785
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

_source line 50 · 2026-05-15T09:09:21.283Z_

<details><summary>↩ Tool result · `toolu_01F6TdVGGCvr9GmxTRvetbqe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"compute_e5_embeddings.py\\ncompute_maven_qwen3_embeddings.py\\nrun_exp008.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.68}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "bbcda024-9726-44d7-8c51-e9562f9b4204",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"compute_e5_embeddings.py\\\\ncompute_maven_qwen3_embeddings.py\\\\nrun_exp008.sh\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.68}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"compute_e5_embeddings.py\\ncompute_maven_qwen3_embeddings.py\\nrun_exp008.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.68}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01H51AQzJBKjPTE6k84rfpLp`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/scripts/compute_maven_qwen3_embeddings.py",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "3fac7f15-f70b-4c13-9fa1-19860693e509",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNUCWTnkjSEnQtkCqNLrCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 34615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 843
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

_source line 52 · 2026-05-15T09:09:26.250Z_

<details><summary>↩ Tool result · `toolu_01H51AQzJBKjPTE6k84rfpLp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Compute Qwen3-32B mean-pooled embeddings for MAVEN 168 event types.\\\"\\\"\\\"\\nimport torch, json, sys, os\\nos.chdir(\\\"/root/schema-dag-extraction\\\")\\n\\nfrom transformers import AutoTokenizer, AutoModelForCausalLM\\n\\nmodel_path = \\\"/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\\"\\nprint(\\\"Loading tokenizer...\\\", flush=True)\\ntokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\\nprint(\\\"Loading model...\\\", flush=True)\\nmodel = AutoModelForCausalLM.from_pretrained(\\n    model_path, device_map=\\\"cuda:0\\\",\\n    torch_dtype=torch.bfloat16, trust_remote_code=True\\n)\\nmodel.eval()\\nprint(\\\"Model loaded.\\\", flush=True)\\n\\n# Get MAVEN types\\nimport pandas as pd\\ndf = pd.read_parquet(\\\"data/maven_parquet/valid.parquet\\\")\\ntypes = set()\\nfor ents in df['entities']:\\n    if ents is None:\\n        continue\\n    lst = json.loads(ents) if isinstance(ents, str) else ents\\n    if lst is None:\\n        continue\\n    for e in lst:\\n        types.add(e['type'])\\ntype_names = sorted(types)\\nprint(f\\\"Computing embeddings for {len(type_names)} types...\\\", flush=True)\\n\\nembeddings = {}\\nfor i, name in enumerate(type_names):\\n    inputs = tokenizer(name, return_tensors=\\\"pt\\\", padding=True, truncation=True).to(\\\"cuda:0\\\")\\n    with torch.no_grad():\\n        outputs = model(**inputs, output_hidden_states=True)\\n        hidden = outputs.hidden_states[-1]\\n        mask = inputs[\\\"attention_mask\\\"].unsqueeze(-1)\\n        emb = (hidden * mask).sum(dim=1) / mask.sum(dim=1)\\n        emb = emb.squeeze().cpu()\\n    embeddings[name] = emb\\n    if (i+1) % 20 == 0:\\n        print(f\\\"  {i+1}/{len(type_names)}\\\", flush=True)\\n\\nprint(f\\\"All {len(type_names)} done. dim={emb.shape[0]}, dtype={emb.dtype}\\\", flush=True)\\n\\n# Save embeddings (keep bfloat16 to match Few-NERD)\\ntorch.save(embeddings, \\\"artifacts/maven_type_embeddings_qwen3.pt\\\")\\nprint(f\\\"Saved embeddings to artifacts/maven_type_embeddings_qwen3.pt\\\", flush=True)\\n\\n# Compute BCS matrix\\nimport torch.nn.functional as F\\nE = torch.stack([embeddings[n] for n in type_names]).float()\\nE_norm = F.normalize(E, dim=1)\\nsim = E_norm @ E_norm.T\\nmask_tri = torch.triu(torch.ones_like(sim), diagonal=1).bool()\\nvals = sim[mask_tri]\\nprint(f\\\"BCS stats: mean={vals.mean():.4f}, std={vals.std():.4f}, min={vals.min():.4f}, max={vals.max():.4f}\\\")\\ntorch.save({\\\"similarity_matrix\\\": sim, \\\"type_names\\\": type_names}, \\\"artifacts/maven_bcs_matrix_qwen3.pt\\\")\\nprint(\\\"Saved BCS matrix to artifacts/maven_bcs_matrix_qwen3.pt\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "84e0b7ed-0f2a-45b0-aa31-5ad70f7d8a54",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Compute Qwen3-32B mean-pooled embeddings for MAVEN 168 event types.\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport torch, json, sys, os\\\\nos.chdir(\\\\\\\"/root/schema-dag-extraction\\\\\\\")\\\\n\\\\nfrom transformers import AutoTokenizer, AutoModelForCausalLM\\\\n\\\\nmodel_path = \\\\\\\"/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\\\\\\"\\\\nprint(\\\\\\\"Loading tokenizer...\\\\\\\", flush=True)\\\\ntokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\\\\nprint(\\\\\\\"Loading model...\\\\\\\", flush=True)\\\\nmodel = AutoModelForCausalLM.from_pretrained(\\\\n    model_path, device_map=\\\\\\\"cuda:0\\\\\\\",\\\\n    torch_dtype=torch.bfloat16, trust_remote_code=True\\\\n)\\\\nmodel.eval()\\\\nprint(\\\\\\\"Model loaded.\\\\\\\", flush=True)\\\\n\\\\n# Get MAVEN types\\\\nimport pandas as pd\\\\ndf = pd.read_parquet(\\\\\\\"data/maven_parquet/valid.parquet\\\\\\\")\\\\ntypes = set()\\\\nfor ents in df['entities']:\\\\n    if ents is None:\\\\n        continue\\\\n    lst = json.loads(ents) if isinstance(ents, str) else ents\\\\n    if lst is None:\\\\n        continue\\\\n    for e in lst:\\\\n        types.add(e['type'])\\\\ntype_names = sorted(types)\\\\nprint(f\\\\\\\"Computing embeddings for {len(type_names)} types...\\\\\\\", flush=True)\\\\n\\\\nembeddings = {}\\\\nfor i, name in enumerate(type_names):\\\\n    inputs = tokenizer(name, return_tensors=\\\\\\\"pt\\\\\\\", padding=True, truncation=True).to(\\\\\\\"cuda:0\\\\\\\")\\\\n    with torch.no_grad():\\\\n        outputs = model(**inputs, output_hidden_states=True)\\\\n        hidden = outputs.hidden_states[-1]\\\\n        mask = inputs[\\\\\\\"attention_mask\\\\\\\"].unsqueeze(-1)\\\\n        emb = (hidden * mask).sum(dim=1) / mask.sum(dim=1)\\\\n        emb = emb.squeeze().cpu()\\\\n    embeddings[name] = emb\\\\n    if (i+1) % 20 == 0:\\\\n        print(f\\\\\\\"  {i+1}/{len(type_names)}\\\\\\\", flush=True)\\\\n\\\\nprint(f\\\\\\\"All {len(type_names)} done. dim={emb.shape[0]}, dtype={emb.dtype}\\\\\\\", flush=True)\\\\n\\\\n# Save embeddings (keep bfloat16 to match Few-NERD)\\\\ntorch.save(embeddings, \\\\\\\"artifacts/maven_type_embeddings_qwen3.pt\\\\\\\")\\\\nprint(f\\\\\\\"Saved embeddings to artifacts/maven_type_embeddings_qwen3.pt\\\\\\\", flush=True)\\\\n\\\\n# Compute BCS matrix\\\\nimport torch.nn.functional as F\\\\nE = torch.stack([embeddings[n] for n in type_names]).float()\\\\nE_norm = F.normalize(E, dim=1)\\\\nsim = E_norm @ E_norm.T\\\\nmask_tri = torch.triu(torch.ones_like(sim), diagonal=1).bool()\\\\nvals = sim[mask_tri]\\\\nprint(f\\\\\\\"BCS stats: mean={vals.mean():.4f}, std={vals.std():.4f}, min={vals.min():.4f}, max={vals.max():.4f}\\\\\\\")\\\\ntorch.save({\\\\\\\"similarity_matrix\\\\\\\": sim, \\\\\\\"type_names\\\\\\\": type_names}, \\\\\\\"artifacts/maven_bcs_matrix_qwen3.pt\\\\\\\")\\\\nprint(\\\\\\\"Saved BCS matrix to artifacts/maven_bcs_matrix_qwen3.pt\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Compute Qwen3-32B mean-pooled embeddings for MAVEN 168 event types.\\\"\\\"\\\"\\nimport torch, json, sys, os\\nos.chdir(\\\"/root/schema-dag-extraction\\\")\\n\\nfrom transformers import AutoTokenizer, AutoModelForCausalLM\\n\\nmodel_path = \\\"/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\\"\\nprint(\\\"Loading tokenizer...\\\", flush=True)\\ntokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\\nprint(\\\"Loading model...\\\", flush=True)\\nmodel = AutoModelForCausalLM.from_pretrained(\\n    model_path, device_map=\\\"cuda:0\\\",\\n    torch_dtype=torch.bfloat16, trust_remote_code=True\\n)\\nmodel.eval()\\nprint(\\\"Model loaded.\\\", flush=True)\\n\\n# Get MAVEN types\\nimport pandas as pd\\ndf = pd.read_parquet(\\\"data/maven_parquet/valid.parquet\\\")\\ntypes = set()\\nfor ents in df['entities']:\\n    if ents is None:\\n        continue\\n    lst = json.loads(ents) if isinstance(ents, str) else ents\\n    if lst is None:\\n        continue\\n    for e in lst:\\n        types.add(e['type'])\\ntype_names = sorted(types)\\nprint(f\\\"Computing embeddings for {len(type_names)} types...\\\", flush=True)\\n\\nembeddings = {}\\nfor i, name in enumerate(type_names):\\n    inputs = tokenizer(name, return_tensors=\\\"pt\\\", padding=True, truncation=True).to(\\\"cuda:0\\\")\\n    with torch.no_grad():\\n        outputs = model(**inputs, output_hidden_states=True)\\n        hidden = outputs.hidden_states[-1]\\n        mask = inputs[\\\"attention_mask\\\"].unsqueeze(-1)\\n        emb = (hidden * mask).sum(dim=1) / mask.sum(dim=1)\\n        emb = emb.squeeze().cpu()\\n    embeddings[name] = emb\\n    if (i+1) % 20 == 0:\\n        print(f\\\"  {i+1}/{len(type_names)}\\\", flush=True)\\n\\nprint(f\\\"All {len(type_names)} done. dim={emb.shape[0]}, dtype={emb.dtype}\\\", flush=True)\\n\\n# Save embeddings (keep bfloat16 to match Few-NERD)\\ntorch.save(embeddings, \\\"artifacts/maven_type_embeddings_qwen3.pt\\\")\\nprint(f\\\"Saved embeddings to artifacts/maven_type_embeddings_qwen3.pt\\\", flush=True)\\n\\n# Compute BCS matrix\\nimport torch.nn.functional as F\\nE = torch.stack([embeddings[n] for n in type_names]).float()\\nE_norm = F.normalize(E, dim=1)\\nsim = E_norm @ E_norm.T\\nmask_tri = torch.triu(torch.ones_like(sim), diagonal=1).bool()\\nvals = sim[mask_tri]\\nprint(f\\\"BCS stats: mean={vals.mean():.4f}, std={vals.std():.4f}, min={vals.min():.4f}, max={vals.max():.4f}\\\")\\ntorch.save({\\\"similarity_matrix\\\": sim, \\\"type_names\\\": type_names}, \\\"artifacts/maven_bcs_matrix_qwen3.pt\\\")\\nprint(\\\"Saved BCS matrix to artifacts/maven_bcs_matrix_qwen3.pt\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SRyi4py4XHAunX8oR9Q8gL`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -rn \"compute_type_embeddings\\|type_embeddings\\|Qwen\" /root/schema-dag-extraction/src/run_experiment.py",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "b8198c7a-3311-43a1-8632-ada2e3cc0cb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNUCWTnkjSEnQtkCqNLrCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 34615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 843
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

_source line 54 · 2026-05-15T09:09:26.433Z_

<details><summary>↩ Tool result · `toolu_01SRyi4py4XHAunX8oR9Q8gL`</summary>

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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "1af58873-476a-4013-a88f-173c8f8ba748",
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

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UH33isFvDJxW17rUc8cbtq`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -rn \"compute_type_embeddings\\|type_embeddings\\|Qwen\" /root/schema-dag-extraction/src/run_fewrel_formal.py",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "7089c3cc-367f-49c7-8487-67742fa74be7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNUCWTnkjSEnQtkCqNLrCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 34615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 843
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

_source line 56 · 2026-05-15T09:09:27.575Z_

<details><summary>↩ Tool result · `toolu_01UH33isFvDJxW17rUc8cbtq`</summary>

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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "f7defe8f-3513-4fd1-a154-e3fe8338dbe2",
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

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JiDeKgmeR1si3LAVkxz4rn`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/scripts/run_exp008.sh",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "d4881e65-f989-4b08-ba2e-59d74b157264",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNUCWTnkjSEnQtkCqNLrCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 34615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 843
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

_source line 58 · 2026-05-15T09:09:28.638Z_

<details><summary>↩ Tool result · `toolu_01JiDeKgmeR1si3LAVkxz4rn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e\\nsource /root/miniconda3/etc/profile.d/conda.sh\\nconda activate base\\ncd /root/schema-dag-extraction\\n\\nCOMMON=\\\"--dataset fewnerd --prompt_version v2 --types_file configs/few_nerd_types.json --sim_matrix_path artifacts/sim_matrix.pt --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ --max_samples 1000 --max_model_len 4096 --output_dir artifacts/exp008\\\"\\n\\necho \\\"===== [$(date)] Starting exp-008: SDGD-zero =====\\\"\\npython3 src/run_sdgd_experiment.py --mode sdgd_zero $COMMON\\necho \\\"===== [$(date)] SDGD-zero done =====\\\"\\n\\necho \\\"===== [$(date)] Starting exp-008: single_pass =====\\\"\\npython3 src/run_sdgd_experiment.py --mode single_pass $COMMON\\necho \\\"===== [$(date)] single_pass done =====\\\"\\n\\necho \\\"===== [$(date)] Starting exp-008: random_batch =====\\\"\\npython3 src/run_sdgd_experiment.py --mode random_batch $COMMON\\necho \\\"===== [$(date)] random_batch done =====\\\"\\n\\necho \\\"===== [$(date)] Starting exp-008: per_type =====\\\"\\npython3 src/run_sdgd_experiment.py --mode per_type $COMMON\\necho \\\"===== [$(date)] per_type done =====\\\"\\n\\necho \\\"===== [$(date)] All exp-008 modes completed =====\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "67e85d5a-fc7d-4645-bd41-fc598f887ebf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/bin/bash\\\\nset -e\\\\nsource /root/miniconda3/etc/profile.d/conda.sh\\\\nconda activate base\\\\ncd /root/schema-dag-extraction\\\\n\\\\nCOMMON=\\\\\\\"--dataset fewnerd --prompt_version v2 --types_file configs/few_nerd_types.json --sim_matrix_path artifacts/sim_matrix.pt --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ --max_samples 1000 --max_model_len 4096 --output_dir artifacts/exp008\\\\\\\"\\\\n\\\\necho \\\\\\\"===== [$(date)] Starting exp-008: SDGD-zero =====\\\\\\\"\\\\npython3 src/run_sdgd_experiment.py --mode sdgd_zero $COMMON\\\\necho \\\\\\\"===== [$(date)] SDGD-zero done =====\\\\\\\"\\\\n\\\\necho \\\\\\\"===== [$(date)] Starting exp-008: single_pass =====\\\\\\\"\\\\npython3 src/run_sdgd_experiment.py --mode single_pass $COMMON\\\\necho \\\\\\\"===== [$(date)] single_pass done =====\\\\\\\"\\\\n\\\\necho \\\\\\\"===== [$(date)] Starting exp-008: random_batch =====\\\\\\\"\\\\npython3 src/run_sdgd_experiment.py --mode random_batch $COMMON\\\\necho \\\\\\\"===== [$(date)] random_batch done =====\\\\\\\"\\\\n\\\\necho \\\\\\\"===== [$(date)] Starting exp-008: per_type =====\\\\\\\"\\\\npython3 src/run_sdgd_experiment.py --mode per_type $COMMON\\\\necho \\\\\\\"===== [$(date)] per_type done =====\\\\\\\"\\\\n\\\\necho \\\\\\\"===== [$(date)] All exp-008 modes completed =====\\\\\\\"\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e\\nsource /root/miniconda3/etc/profile.d/conda.sh\\nconda activate base\\ncd /root/schema-dag-extraction\\n\\nCOMMON=\\\"--dataset fewnerd --prompt_version v2 --types_file configs/few_nerd_types.json --sim_matrix_path artifacts/sim_matrix.pt --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ --max_samples 1000 --max_model_len 4096 --output_dir artifacts/exp008\\\"\\n\\necho \\\"===== [$(date)] Starting exp-008: SDGD-zero =====\\\"\\npython3 src/run_sdgd_experiment.py --mode sdgd_zero $COMMON\\necho \\\"===== [$(date)] SDGD-zero done =====\\\"\\n\\necho \\\"===== [$(date)] Starting exp-008: single_pass =====\\\"\\npython3 src/run_sdgd_experiment.py --mode single_pass $COMMON\\necho \\\"===== [$(date)] single_pass done =====\\\"\\n\\necho \\\"===== [$(date)] Starting exp-008: random_batch =====\\\"\\npython3 src/run_sdgd_experiment.py --mode random_batch $COMMON\\necho \\\"===== [$(date)] random_batch done =====\\\"\\n\\necho \\\"===== [$(date)] Starting exp-008: per_type =====\\\"\\npython3 src/run_sdgd_experiment.py --mode per_type $COMMON\\necho \\\"===== [$(date)] per_type done =====\\\"\\n\\necho \\\"===== [$(date)] All exp-008 modes completed =====\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
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
Now let me also check the Few-NERD embedding generation. The `type_embeddings.pt` for Few-NERD also has dim=5120. Let me check if there's a script that generated it or if it was generated via `run_experiment.py` or `run_fewrel_formal.py`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "909187b1-20f4-4988-884a-d62e753438dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cPxd13ZhPk2a47kSMJ7rm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2402,
      "cache_read_input_tokens": 35458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2402
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

再确认 Few-NERD 的 embeddings 是怎么生成的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "fd4dfd67-0e46-40e3-b240-2cd1d5a0238f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cPxd13ZhPk2a47kSMJ7rm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2402,
      "cache_read_input_tokens": 35458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2402
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018E3rsK1MQzDsFU45NPscxF`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -rn \"type_embeddings\\|compute_embeddings\\|Qwen\\|model_path\\|Embedding\" /root/schema-dag-extraction/src/run_experiment.py",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "64c5b9c8-0b91-4e83-84f1-11a2c07caa03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cPxd13ZhPk2a47kSMJ7rm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2402,
      "cache_read_input_tokens": 35458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2402
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

_source line 62 · 2026-05-15T09:09:34.418Z_

<details><summary>↩ Tool result · `toolu_018E3rsK1MQzDsFU45NPscxF`</summary>

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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "d0259371-40a7-48aa-8d77-96c9ef6a0119",
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

_source line 63_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E9og3cXu6eq9yhHuuDZPcZ`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -n \"type_embeddings\" /root/schema-dag-extraction/src/run_experiment.py",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "22c7b791-ff5b-41a7-b0cd-4511b8919c58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUt4cm5ebNpkatmu8deSTe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 37860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 352
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

_source line 64 · 2026-05-15T09:09:38.199Z_

<details><summary>↩ Tool result · `toolu_01E9og3cXu6eq9yhHuuDZPcZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"95:        embeddings_path = str(output_dir / \\\"type_embeddings.pt\\\")\\n99:        logger.error(\\\"Run compute_type_embeddings.py first to avoid loading two models simultaneously.\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "00c8faf2-e07a-4759-a7ee-4da0d4e64c3e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"95:        embeddings_path = str(output_dir / \\\\\\\"type_embeddings.pt\\\\\\\")\\\\n99:        logger.error(\\\\\\\"Run compute_type_embeddings.py first to avoid loading two models simultaneously.\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"95:        embeddings_path = str(output_dir / \\\"type_embeddings.pt\\\")\\n99:        logger.error(\\\"Run compute_type_embeddings.py first to avoid loading two models simultaneously.\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012swbkRrfe7vpLkUkH9e5PC`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -n \"compute_embeddings\" /root/schema-dag-extraction/src/run_experiment.py",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "55075b40-b9f8-407a-91cc-ce3515e29fa6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUt4cm5ebNpkatmu8deSTe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 37860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 352
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

_source line 66 · 2026-05-15T09:09:39.188Z_

<details><summary>↩ Tool result · `toolu_012swbkRrfe7vpLkUkH9e5PC`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "11966284-8100-438c-8ca5-f7d989a2b7f1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SkYERQ3tScSYq39adoTT7Q`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -n \"Qwen\" /root/schema-dag-extraction/src/run_experiment.py",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "c30679a2-e665-48cd-9a30-c288a1f09a87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUt4cm5ebNpkatmu8deSTe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 37860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 352
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


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012fY6jkeQNerMgU7VC7Zvmd`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -n \"Embedding\" /root/schema-dag-extraction/src/run_experiment.py",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "5c4b5d68-07ef-422e-a461-1ca0da116657",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUt4cm5ebNpkatmu8deSTe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 37860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 352
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

_source line 69 · 2026-05-15T09:09:40.397Z_

<details><summary>↩ Tool result · `toolu_01SkYERQ3tScSYq39adoTT7Q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"24:    parser.add_argument(\\\"--model_path\\\", required=True, help=\\\"Path to Qwen3 model\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "da263b10-746f-492e-a666-b7911568edde",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"24:    parser.add_argument(\\\\\\\"--model_path\\\\\\\", required=True, help=\\\\\\\"Path to Qwen3 model\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.69}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"24:    parser.add_argument(\\\"--model_path\\\", required=True, help=\\\"Path to Qwen3 model\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-15T09:09:40.888Z_

<details><summary>↩ Tool result · `toolu_012fY6jkeQNerMgU7VC7Zvmd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"98:        logger.error(\\\"Embeddings file not found: %s\\\", embeddings_path)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "5ce0aa58-66bd-4af4-9217-839b4650c776",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"98:        logger.error(\\\\\\\"Embeddings file not found: %s\\\\\\\", embeddings_path)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.48}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"98:        logger.error(\\\"Embeddings file not found: %s\\\", embeddings_path)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me also check whether `artifacts/type_embeddings.pt` (the Few-NERD one) was generated by `compute_type_embeddings.py` (which also uses `AutoModelForCausalLM`). Let me also check if there's any mention of "Qwen3-Embedding" anywhere in the project.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "d589e5f5-4d13-4f84-90c2-de685f371b4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpHosBFuxkxe3AQiGJR9MM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 38212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1088
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

_source line 72_

最后确认项目中是否有任何 Qwen3-Embedding-0.6B 的引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "e9fae284-57ca-4ef3-bfea-f2a4d00d4f34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpHosBFuxkxe3AQiGJR9MM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 38212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1088
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

_source line 73_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Vve4zN8vSCVKd8uS7JWMjy`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -rn \"Qwen3-Embedding\" /root/schema-dag-extraction/",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "bf7d39b7-084c-4aa5-bbc8-f2e60c028a18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpHosBFuxkxe3AQiGJR9MM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 38212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1088
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

_source line 74_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BvfRAYhj41Az94EvK1sP1X`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -rn \"0.6B\" /root/schema-dag-extraction/",
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "50cc9d53-fdfd-486c-ab5e-bccdd20399d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpHosBFuxkxe3AQiGJR9MM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 38212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1088
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

_source line 75 · 2026-05-15T09:09:48.488Z_

<details><summary>↩ Tool result · `toolu_01Vve4zN8vSCVKd8uS7JWMjy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema-dag-extraction/artifacts/maven_minilm_pertype_analysis.json:985:    \\\"qwen3_model\\\": \\\"Qwen3-Embedding-0.6B\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.19}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "f9980923-746e-467c-8b57-632f2d1611c2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/schema-dag-extraction/artifacts/maven_minilm_pertype_analysis.json:985:    \\\\\\\"qwen3_model\\\\\\\": \\\\\\\"Qwen3-Embedding-0.6B\\\\\\\",\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.19}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/schema-dag-extraction/artifacts/maven_minilm_pertype_analysis.json:985:    \\\"qwen3_model\\\": \\\"Qwen3-Embedding-0.6B\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.19}}"
    }
  }
}
```

</details>

---


### Large event (continued)

````text
### Tool result

_source line 76 · 2026-05-15T09:10:36.181Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01BvfRAYhj41Az94EvK1sP1X`&lt;/summary>

```text
Error: result (21,757,406 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/e5aa1b6a-5750-45df-b880-a69389c91396/tool-results/mcp-agent-ml-research-ssh_read_only-1778836236138.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/e5aa1b6a-5750-45df-b880-a69389c91396/tool-results/mcp-agent-ml-research-ssh_read_only-1778836236138.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "e5aa1b6a-5750-45df-b880-a69389c91396",
  "uuid": "c84b4b7f-703d-4ecd-b948-2f6b31c1f4c8",
  "tool_use_result": {
    "content": "Error: result (21,757,406 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/e5aa1b6a-5750-45df-b880-a69389c91396/tool-results/mcp-agent-ml-research-ssh_read_only-1778836236138.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/e5aa1b6a-5750-45df-b880-a69389c91396/tool-results/mcp-agent-ml-research-ssh_read_only-1778836236138.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'grep -rn \\\"0.6B\\\" /root/schema-dag-extraction/'\\n\\nStdout:\\n\\n/root/schema-dag-extraction/data/fewrel/train_wiki.json:1:{\\\"P931\\\": [{\\\"tokens\\\": [\\\"Merpati\\\", \\\"flight\\\", \\\"106\\\", \\\"departed\\\", \\\"Jakarta\\\", \\\"(\\\", \\\"CGK\\\", \\\")\\\", \\\"on\\\", \\\"a\\\", \\\"domestic\\\", \\\"flight\\\", \\\"to\\\", \\\"Tanjung\\\", \\\"Pandan\\\", \\\"(\\\", \\\"TJQ\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"tjq\\\", \\\"Q1331049\\\", [[16]]], \\\"t\\\": [\\\"tanjung pandan\\\", \\\"Q3056359\\\", [[13, 14]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"name\\\", \\\"was\\\", \\\"at\\\", \\\"one\\\", \\\"point\\\", \\\"changed\\\", \\\"to\\\", \\\"Nottingham\\\", \\\"East\\\", \\\"Midlands\\\", \\\"Airport\\\", \\\"so\\\", \\\"as\\\", \\\"to\\\", \\\"include\\\", \\\"the\\\", \\\"name\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\"that\\\", \\\"is\\\", \\\"supposedly\\\", \\\"most\\\", \\\"internationally\\\", \\\"recognisable\\\", \\\",\\\", \\\"mainly\\\", \\\"due\\\", \\\"to\\\", \\\"the\\\", \\\"Robin\\\", \\\"Hood\\\", \\\"legend\\\", \\\".\\\"], \\\"h\\\": [\\\"east midlands airport\\\", \\\"Q8977\\\", [[9, 10, 11]]], \\\"t\\\": [\\\"nottingham\\\", \\\"Q41262\\\", [[8]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"a\\\", \\\"four\\\", \\\"-\\\", \\\"level\\\", \\\"stack\\\", \\\"interchange\\\", \\\"near\\\", \\\"Fort\\\", \\\"Lauderdale\\\", \\\"-\\\", \\\"Hollywood\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Fort\\\", \\\"Lauderdale\\\", \\\",\\\", \\\"Florida\\\", \\\".\\\"], \\\"h\\\": [\\\"fort lauderdale-hollywood international airport\\\", \\\"Q635361\\\", [[9, 10, 11, 12, 13, 14]]], \\\"t\\\": [\\\"fort lauderdale, florida\\\", \\\"Q165972\\\", [[16, 17, 18, 19]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"the\\\", \\\"main\\\", \\\"alternate\\\", \\\"of\\\", \\\"Jinnah\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Karachi\\\", \\\"with\\\", \\\"a\\\", \\\"distance\\\", \\\"of\\\", \\\"about\\\", \\\"350\\\", \\\"\\\\u00a0\\\", \\\"km/220\\\", \\\"miles\\\", \\\";\\\", \\\"well\\\", \\\"under\\\", \\\"an\\\", \\\"hour\\\", \\\"'s\\\", \\\"flight\\\", \\\"time\\\", \\\"in\\\", \\\"turboprop\\\", \\\"aircraft\\\", \\\".\\\"], \\\"h\\\": [\\\"jinnah international airport\\\", \\\"Q61052\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"karachi\\\", \\\"Q8660\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Nearby\\\", \\\"airports\\\", \\\"include\\\", \\\"Akwa\\\", \\\"Ibom\\\", \\\"Airport\\\", \\\"at\\\", \\\"Okobo\\\", \\\"and\\\", \\\"Margaret\\\", \\\"Ekpo\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Calabar\\\", \\\".\\\"], \\\"h\\\": [\\\"margaret ekpo international airport\\\", \\\"Q1030578\\\", [[9, 10, 11, 12]]], \\\"t\\\": [\\\"calabar\\\", \\\"Q844091\\\", [[14]]]}, {\\\"tokens\\\": [\\\"Pakyong\\\", \\\"Airport\\\", \\\",\\\", \\\"a\\\", \\\"Greenfield\\\", \\\"project\\\", \\\",\\\", \\\"is\\\", \\\"under\\\", \\\"construction\\\", \\\"southeast\\\", \\\"of\\\", \\\"Gangtok\\\", \\\".\\\"], \\\"h\\\": [\\\"pakyong airport\\\", \\\"Q7126092\\\", [[0, 1]]], \\\"t\\\": [\\\"gangtok\\\", \\\"Q186141\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"hub\\\", \\\"is\\\", \\\"Tinson\\\", \\\"Pen\\\", \\\"Aerodrome\\\", \\\"in\\\", \\\"Kingston\\\", \\\"(\\\", \\\"KTP\\\", \\\")\\\", \\\",\\\", \\\"and\\\", \\\"its\\\", \\\"other\\\", \\\"major\\\", \\\"gateway\\\", \\\"was\\\", \\\"Sangster\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Montego\\\", \\\"Bay\\\", \\\"(\\\", \\\"MBJ\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"tinson pen aerodrome\\\", \\\"Q2320308\\\", [[3, 4, 5]]], \\\"t\\\": [\\\"kingston\\\", \\\"Q34692\\\", [[7]]]}, {\\\"tokens\\\": [\\\"He\\\", \\\"has\\\", \\\"postage\\\", \\\"stamps\\\", \\\"issued\\\", \\\"in\\\", \\\"his\\\", \\\"honour\\\", \\\"and\\\", \\\"Noum\\\\u00e9rat\\\", \\\"\\\\u2013\\\", \\\"Moufdi\\\", \\\"Zakaria\\\", \\\"Airport\\\", \\\"in\\\", \\\"Gharda\\\\u00efa\\\", \\\",\\\", \\\"Algeria\\\", \\\"is\\\", \\\"named\\\", \\\"in\\\", \\\"his\\\", \\\"honour\\\", \\\".\\\"], \\\"h\\\": [\\\"noum\\\\u00e9rat \\\\u2013 moufdi zakaria airport\\\", \\\"Q1432199\\\", [[9, 10, 11, 12, 13]]], \\\"t\\\": [\\\"gharda\\\\u00efa\\\", \\\"Q622841\\\", [[15]]]}, {\\\"tokens\\\": [\\\"By\\\", \\\"Airway\\\", \\\";\\\", \\\"\\\\n\\\", \\\"Nearest\\\", \\\"airport\\\", \\\"is\\\", \\\"Kazi\\\", \\\"Nazrul\\\", \\\"Islam\\\", \\\"Airport\\\", \\\",\\\", \\\"Durgapur\\\", \\\"(\\\", \\\"RDP\\\", \\\")\\\", \\\"West\\\", \\\"Bengal\\\", \\\"and\\\", \\\"1\\\", \\\"hour\\\", \\\"drive\\\", \\\"from\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"kazi nazrul islam airport\\\", \\\"Q14941562\\\", [[7, 8, 9, 10]]], \\\"t\\\": [\\\"durgapur\\\", \\\"Q5088\\\", [[12]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"airport\\\", \\\"is\\\", \\\"Robin\\\", \\\"Hood\\\", \\\"Airport\\\", \\\"at\\\", \\\"Doncaster\\\", \\\"and\\\", \\\"the\\\", \\\"nearest\\\", \\\"train\\\", \\\"and\\\", \\\"bus\\\", \\\"stations\\\", \\\"are\\\", \\\"in\\\", \\\"Chesterfield\\\", \\\".\\\"], \\\"h\\\": [\\\"robin hood airport\\\", \\\"Q8996\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"doncaster\\\", \\\"Q58900\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Manchester\\\", \\\"boasts\\\", \\\"a\\\", \\\"large\\\", \\\"regional\\\", \\\"airport\\\", \\\",\\\", \\\"with\\\", \\\"scheduled\\\", \\\"commercial\\\", \\\"services\\\", \\\".\\\"], \\\"h\\\": [\\\"large regional airport\\\", \\\"Q180129\\\", [[3, 4, 5]]], \\\"t\\\": [\\\"manchester\\\", \\\"Q48370\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Route\\\", \\\"41\\\", \\\"ends\\\", \\\"just\\\", \\\"north\\\", \\\"of\\\", \\\"the\\\", \\\"Richmond\\\", \\\"-\\\", \\\"Pittsfield\\\", \\\"line\\\", \\\"at\\\", \\\"U.S.\\\", \\\"Route\\\", \\\"20\\\", \\\",\\\", \\\"just\\\", \\\"east\\\", \\\"of\\\", \\\"the\\\", \\\"Hancock\\\", \\\"Shaker\\\", \\\"Village\\\", \\\"in\\\", \\\"Hancock\\\", \\\"and\\\", \\\"southwest\\\", \\\"of\\\", \\\"Pittsfield\\\", \\\"'s\\\", \\\"airport\\\", \\\"and\\\", \\\"city\\\", \\\"center\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q7199486\\\", [[30]]], \\\"t\\\": [\\\"pittsfield\\\", \\\"Q49184\\\", [[9], [28]]]}, {\\\"tokens\\\": [\\\"Casilda\\\", \\\"is\\\", \\\"the\\\", \\\"southern\\\", \\\"terminus\\\", \\\"of\\\", \\\"the\\\", \\\"railway\\\", \\\"line\\\", \\\"which\\\", \\\"links\\\", \\\"Placetas\\\", \\\"and\\\", \\\"Fomento\\\", \\\"to\\\", \\\"Trinidad\\\", \\\",\\\", \\\"has\\\", \\\"a\\\", \\\"small\\\", \\\"harbor\\\", \\\",\\\", \\\"and\\\", \\\"is\\\", \\\"4\\\", \\\"km\\\", \\\"from\\\", \\\"Alberto\\\", \\\"Delgado\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"alberto delgado airport\\\", \\\"Q4711997\\\", [[27, 28, 29]]], \\\"t\\\": [\\\"trinidad\\\", \\\"Q319272\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Aeropark\\\", \\\"is\\\", \\\"an\\\", \\\"open\\\", \\\"-\\\", \\\"air\\\", \\\"aviation\\\", \\\"museum\\\", \\\"next\\\", \\\"to\\\", \\\"Ferenc\\\", \\\"Liszt\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Budapest\\\", \\\",\\\", \\\"Hungary\\\", \\\".\\\"], \\\"h\\\": [\\\"ferenc liszt international airport\\\", \\\"Q500945\\\", [[10, 11, 12, 13]]], \\\"t\\\": [\\\"budapest\\\", \\\"Q1781\\\", [[15]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"airport\\\", \\\"is\\\", \\\"the\\\", \\\"Menominee\\\", \\\"-\\\", \\\"Marinette\\\", \\\"Twin\\\", \\\"County\\\", \\\"Airport\\\", \\\"in\\\", \\\"Menominee\\\", \\\",\\\", \\\"Michigan\\\", \\\".\\\"], \\\"h\\\": [\\\"menominee-marinette twin county airport\\\", \\\"Q27308800\\\", [[5, 6, 7, 8, 9, 10]]], \\\"t\\\": [\\\"menominee, michigan\\\", \\\"Q2635319\\\", [[12, 13, 14]]]}, {\\\"tokens\\\": [\\\"Peshawar\\\", \\\"'s\\\", \\\"Bacha\\\", \\\"Khan\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"155\\\", \\\"kilometres\\\", \\\"away\\\", \\\"by\\\", \\\"road\\\", \\\".\\\"], \\\"h\\\": [\\\"bacha khan international airport\\\", \\\"Q1516769\\\", [[2, 3, 4, 5]]], \\\"t\\\": [\\\"peshawar\\\", \\\"Q1113311\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Currently\\\", \\\"it\\\", \\\"is\\\", \\\"the\\\", \\\"second\\\", \\\"largest\\\", \\\"airport\\\", \\\"in\\\", \\\"Kalimantan\\\", \\\"in\\\", \\\"terms\\\", \\\"of\\\", \\\"terminal\\\", \\\"size\\\", \\\",\\\", \\\"after\\\", \\\"Sultan\\\", \\\"Aji\\\", \\\"Muhammad\\\", \\\"Sulaiman\\\", \\\"Airport\\\", \\\"in\\\", \\\"Balikpapan\\\", \\\".\\\"], \\\"h\\\": [\\\"sultan aji muhammad sulaiman airport\\\", \\\"Q263652\\\", [[16, 17, 18, 19, 20]]], \\\"t\\\": [\\\"balikpapan\\\", \\\"Q14492\\\", [[22]]]}, {\\\"tokens\\\": [\\\"Presidente\\\", \\\"M\\\\u00e9dici\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"formerly\\\", \\\",\\\", \\\"was\\\", \\\"the\\\", \\\"airport\\\", \\\"that\\\", \\\"served\\\", \\\"Rio\\\", \\\"Branco\\\", \\\",\\\", \\\"Brazil\\\", \\\"until\\\", \\\"1999\\\", \\\",\\\", \\\"when\\\", \\\"Pl\\\\u00e1cido\\\", \\\"de\\\", \\\"Castro\\\", \\\"International\\\", \\\"Airport\\\", \\\"was\\\", \\\"opened\\\", \\\".\\\"], \\\"h\\\": [\\\"presidente m\\\\u00e9dici international airport\\\", \\\"Q6587048\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"rio branco\\\", \\\"Q171612\\\", [[12, 13]]]}, {\\\"tokens\\\": [\\\"Temple\\\", \\\"Bar\\\", \\\"Marina\\\", \\\"has\\\", \\\"its\\\", \\\"own\\\", \\\"post\\\", \\\"office\\\", \\\"with\\\", \\\"ZIP\\\", \\\"code\\\", \\\"86443.ZIP\\\", \\\"Code\\\", \\\"Lookup\\\", \\\"Temple\\\", \\\"Bar\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"near\\\", \\\"the\\\", \\\"marina\\\", \\\".\\\"], \\\"h\\\": [\\\"temple bar airport\\\", \\\"Q6588459\\\", [[14, 15, 16]]], \\\"t\\\": [\\\"temple bar marina\\\", \\\"Q7698447\\\", [[0, 1, 2]]]}, {\\\"tokens\\\": [\\\"Bishop\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Flint\\\", \\\"and\\\", \\\"Toledo\\\", \\\"Express\\\", \\\"Airport\\\", \\\"in\\\", \\\"Toledo\\\", \\\",\\\", \\\"Ohio\\\", \\\"are\\\", \\\"other\\\", \\\"commercial\\\", \\\"passenger\\\", \\\"airports\\\", \\\".\\\"], \\\"h\\\": [\\\"toledo express airport\\\", \\\"Q6588637\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"toledo, ohio\\\", \\\"Q49239\\\", [[10, 11, 12]]]}, {\\\"tokens\\\": [\\\"Greenbrier\\\", \\\"Valley\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"single\\\", \\\"runway\\\", \\\"airport\\\", \\\"3\\\", \\\"miles\\\", \\\"north\\\", \\\"of\\\", \\\"Lewisburg\\\", \\\",\\\", \\\"West\\\", \\\"Virginia\\\", \\\".\\\"], \\\"h\\\": [\\\"greenbrier valley airport\\\", \\\"Q3914326\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"lewisburg, west virginia\\\", \\\"Q731071\\\", [[12, 13, 14, 15]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"international\\\", \\\"airport\\\", \\\"of\\\", \\\"Chania\\\", \\\"(\\\", \\\"CHQ\\\", \\\"/\\\", \\\"LGSA\\\", \\\")\\\", \\\"bears\\\", \\\"Daskalogiannis\\\", \\\"'\\\", \\\"name\\\", \\\".\\\", \\\"Ioannis\\\", \\\"Daskalogiannis\\\", \\\"International\\\", \\\"Airport\\\", \\\"A\\\", \\\"memorial\\\", \\\"statue\\\", \\\"can\\\", \\\"be\\\", \\\"seen\\\", \\\"in\\\", \\\"his\\\", \\\"hometown\\\", \\\"Anopolis\\\", \\\".\\\"], \\\"h\\\": [\\\"international airport\\\", \\\"Q1232348\\\", [[1, 2], [17, 18]]], \\\"t\\\": [\\\"chania\\\", \\\"Q182299\\\", [[4]]]}, {\\\"tokens\\\": [\\\"2\\\", \\\"\\\\u2013\\\", \\\"30\\\", \\\"days\\\", \\\",\\\", \\\"also\\\", \\\"available\\\", \\\"at\\\", \\\"Gurney\\\", \\\"Airport\\\", \\\"(\\\", \\\"Alotau\\\", \\\")\\\", \\\"and\\\", \\\"Mount\\\", \\\"Hagen\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"gurney airport\\\", \\\"Q1069088\\\", [[8, 9]]], \\\"t\\\": [\\\"alotau\\\", \\\"Q568137\\\", [[11]]]}, {\\\"tokens\\\": [\\\"They\\\", \\\"are\\\", \\\"still\\\", \\\"deployed\\\", \\\"at\\\", \\\"Kisangani\\\", \\\"'s\\\", \\\"Bangoka\\\", \\\"airport\\\", \\\",\\\", \\\"where\\\", \\\"they\\\", \\\"appear\\\", \\\"to\\\", \\\"answer\\\", \\\"to\\\", \\\"no\\\", \\\"local\\\", \\\"commander\\\", \\\"and\\\", \\\"have\\\", \\\"caused\\\", \\\"trouble\\\", \\\"with\\\", \\\"MONUC\\\", \\\"troops\\\", \\\"there\\\", \\\".\\\"], \\\"h\\\": [\\\"bangoka airport\\\", \\\"Q27596\\\", [[7, 8]]], \\\"t\\\": [\\\"kisangani\\\", \\\"Q146723\\\", [[5]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airline\\\", \\\"is\\\", \\\"based\\\", \\\"at\\\", \\\"Alexandria\\\", \\\"'s\\\", \\\"Borg\\\", \\\"El\\\", \\\"Arab\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"borg el arab airport\\\", \\\"Q1194015\\\", [[7, 8, 9, 10]]], \\\"t\\\": [\\\"alexandria\\\", \\\"Q87\\\", [[5]]]}, {\\\"tokens\\\": [\\\"LIFESTAR\\\", \\\"2\\\", \\\"is\\\", \\\"based\\\", \\\"in\\\", \\\"Rockwood\\\", \\\",\\\", \\\"Tennessee\\\", \\\"at\\\", \\\"the\\\", \\\"Rockwood\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"rockwood municipal airport\\\", \\\"Q10851312\\\", [[10, 11, 12]]], \\\"t\\\": [\\\"rockwood, tennessee\\\", \\\"Q979056\\\", [[5, 6, 7]]]}, {\\\"tokens\\\": [\\\"Bluffton\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"the\\\", \\\"Savannah\\\", \\\"/\\\", \\\"Hilton\\\", \\\"Head\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Savannah\\\", \\\",\\\", \\\"Georgia\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"Hilton\\\", \\\"Head\\\", \\\"Island\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"savannah/hilton head international airport\\\", \\\"Q1432789\\\", [[5, 6, 7, 8, 9, 10]]], \\\"t\\\": [\\\"savannah, georgia\\\", \\\"Q83813\\\", [[16, 17, 18]]]}, {\\\"tokens\\\": [\\\"Air\\\", \\\"Costa\\\", \\\"Rica\\\", \\\"is\\\", \\\"a\\\", \\\"planned\\\", \\\"airline\\\", \\\"based\\\", \\\"in\\\", \\\"Juan\\\", \\\"Santamar\\\\u00eda\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"San\\\", \\\"Jos\\\\u00e9\\\", \\\",\\\", \\\"Costa\\\", \\\"Rica\\\", \\\".\\\"], \\\"h\\\": [\\\"juan santamar\\\\u00eda international airport\\\", \\\"Q555940\\\", [[9, 10, 11, 12]]], \\\"t\\\": [\\\"san jos\\\\u00e9\\\", \\\"Q3070\\\", [[14, 15]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Djibouti\\\", \\\"\\\\u2013\\\", \\\"Ambouli\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"the\\\", \\\"country\\\", \\\"'s\\\", \\\"only\\\", \\\"international\\\", \\\"airport\\\", \\\"in\\\", \\\"Djibouti\\\", \\\"City\\\", \\\"serves\\\", \\\"many\\\", \\\"intercontinental\\\", \\\"routes\\\", \\\"with\\\", \\\"scheduled\\\", \\\"and\\\", \\\"chartered\\\", \\\"flights\\\", \\\".\\\"], \\\"h\\\": [\\\"djibouti\\\\u2013ambouli international airport\\\", \\\"Q620706\\\", [[1, 2, 3, 4, 5]]], \\\"t\\\": [\\\"djibouti city\\\", \\\"Q3604\\\", [[14, 15]]]}, {\\\"tokens\\\": [\\\"An\\\", \\\"ASOS\\\", \\\"station\\\", \\\"was\\\", \\\"install\\\", \\\"at\\\", \\\"the\\\", \\\"Magic\\\", \\\"Valley\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"south\\\", \\\"of\\\", \\\"Twin\\\", \\\"Falls\\\", \\\",\\\", \\\"Idaho\\\", \\\"on\\\", \\\"January\\\", \\\"28\\\", \\\",\\\", \\\"1997\\\", \\\".\\\"], \\\"h\\\": [\\\"magic valley regional airport\\\", \\\"Q6730879\\\", [[7, 8, 9, 10]]], \\\"t\\\": [\\\"twin falls, idaho\\\", \\\"Q548384\\\", [[13, 14, 15, 16]]]}, {\\\"tokens\\\": [\\\"Abernathy\\\", \\\"Field\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"use\\\", \\\"airport\\\", \\\"owned\\\", \\\"by\\\", \\\"Giles\\\", \\\"County\\\", \\\"and\\\", \\\"the\\\", \\\"City\\\", \\\"of\\\", \\\"Pulaski\\\", \\\".\\\"], \\\"h\\\": [\\\"abernathy field\\\", \\\"Q428353\\\", [[0, 1]]], \\\"t\\\": [\\\"city of pulaski\\\", \\\"Q1410885\\\", [[13, 14, 15]]]}, {\\\"tokens\\\": [\\\"He\\\", \\\"died\\\", \\\"at\\\", \\\"43\\\", \\\"from\\\", \\\"injuries\\\", \\\"suffered\\\", \\\"in\\\", \\\"crash\\\", \\\"while\\\", \\\"piloting\\\", \\\"an\\\", \\\"ultralight\\\", \\\"aircraft\\\", \\\",\\\", \\\"soon\\\", \\\"after\\\", \\\"taking\\\", \\\"off\\\", \\\"from\\\", \\\"the\\\", \\\"Tuscola\\\", \\\"Area\\\", \\\"Airport\\\", \\\"near\\\", \\\"Caro\\\", \\\",\\\", \\\"Michigan\\\", \\\".\\\"], \\\"h\\\": [\\\"tuscola area airport\\\", \\\"Q7856724\\\", [[21, 22, 23]]], \\\"t\\\": [\\\"caro, michigan\\\", \\\"Q14032\\\", [[25, 26, 27]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"airport\\\", \\\"is\\\", \\\"Raja\\\", \\\"Bhoj\\\", \\\"Airport\\\", \\\"Bhopal\\\", \\\".\\\"], \\\"h\\\": [\\\"raja bhoj airport\\\", \\\"Q7285421\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"bhopal\\\", \\\"Q80989\\\", [[7]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airline\\\", \\\"'s\\\", \\\"hub\\\", \\\"is\\\", \\\"Maya\\\", \\\"-\\\", \\\"Maya\\\", \\\"Airport\\\", \\\",\\\", \\\"in\\\", \\\"Brazzaville\\\", \\\".\\\"], \\\"h\\\": [\\\"maya-maya airport\\\", \\\"Q644963\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"brazzaville\\\", \\\"Q3844\\\", [[11]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"1954\\\", \\\"USAF\\\", \\\"C-124\\\", \\\"transports\\\", \\\"assisted\\\", \\\"the\\\", \\\"French\\\", \\\"by\\\", \\\"airlifting\\\", \\\"500\\\", \\\"paratroop\\\", \\\"/\\\", \\\"commandos\\\", \\\"and\\\", \\\"their\\\", \\\"equipment\\\", \\\"to\\\", \\\"Indochina\\\", \\\",\\\", \\\"landing\\\", \\\"at\\\", \\\"Da\\\", \\\"Nang\\\", \\\"'s\\\", \\\"Tourane\\\", \\\"Airfield\\\", \\\".\\\"], \\\"h\\\": [\\\"tourane airfield\\\", \\\"Q773330\\\", [[25, 26]]], \\\"t\\\": [\\\"da nang\\\", \\\"Q25282\\\", [[22, 23]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"other\\\", \\\"airports\\\", \\\"in\\\", \\\"Tibet\\\", \\\"are\\\", \\\"Lhasa\\\", \\\"Gonggar\\\", \\\"Airport\\\", \\\"in\\\", \\\"Lhasa\\\", \\\",\\\", \\\"Qamdo\\\", \\\"Bamda\\\", \\\"Airport\\\", \\\"in\\\", \\\"Chamdo\\\", \\\"and\\\", \\\"Nyingchi\\\", \\\"Mainling\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"qamdo bamda airport\\\", \\\"Q531800\\\", [[12, 13, 14]]], \\\"t\\\": [\\\"chamdo\\\", \\\"Q1012419\\\", [[16]]]}, {\\\"tokens\\\": [\\\"After\\\", \\\"successfully\\\", \\\"transporting\\\", \\\"the\\\", \\\"patient\\\", \\\"from\\\", \\\"Tingwall\\\", \\\"Airport\\\", \\\"in\\\", \\\"the\\\", \\\"Shetland\\\", \\\"Islands\\\", \\\"to\\\", \\\"Inverness\\\", \\\",\\\", \\\"the\\\", \\\"pilot\\\", \\\",\\\", \\\"nurse\\\", \\\",\\\", \\\"and\\\", \\\"physician\\\", \\\"were\\\", \\\"returning\\\", \\\"to\\\", \\\"their\\\", \\\"home\\\", \\\"base\\\", \\\"in\\\", \\\"Tingwall\\\", \\\".\\\"], \\\"h\\\": [\\\"tingwall airport\\\", \\\"Q2875973\\\", [[6, 7]]], \\\"t\\\": [\\\"shetland islands\\\", \\\"Q47134\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"by\\\", \\\"State\\\", \\\"Highway\\\", \\\"947\\\", \\\"from\\\", \\\"Jamnagar\\\", \\\",\\\", \\\"where\\\", \\\"there\\\", \\\"is\\\", \\\"a\\\", \\\"domestic\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"domestic airport\\\", \\\"Q1595059\\\", [[13, 14]]], \\\"t\\\": [\\\"jamnagar\\\", \\\"Q1154\\\", [[7]]]}, {\\\"tokens\\\": [\\\"Diori\\\", \\\"Hamani\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"Niamey\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\"of\\\", \\\"Niger\\\", \\\".\\\"], \\\"h\\\": [\\\"diori hamani international airport\\\", \\\"Q905933\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"niamey\\\", \\\"Q3674\\\", [[8]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Quad\\\", \\\"City\\\", \\\"Airshow\\\", \\\"is\\\", \\\"an\\\", \\\"annual\\\", \\\"event\\\", \\\"at\\\", \\\"the\\\", \\\"Davenport\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"in\\\", \\\"Davenport\\\", \\\",\\\", \\\"Iowa\\\", \\\"and\\\", \\\"was\\\", \\\"the\\\", \\\"largest\\\", \\\"airshow\\\", \\\"in\\\", \\\"the\\\", \\\"state\\\", \\\"of\\\", \\\"Iowa\\\", \\\".\\\"], \\\"h\\\": [\\\"davenport municipal airport\\\", \\\"Q1707887\\\", [[10, 11, 12]]], \\\"t\\\": [\\\"davenport, iowa\\\", \\\"Q26887\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"1912\\\", \\\",\\\", \\\"Bell\\\", \\\"flew\\\", \\\"the\\\", \\\"first\\\", \\\"recorded\\\", \\\"flight\\\", \\\"into\\\", \\\"Billings\\\", \\\"Logan\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Billings\\\", \\\",\\\", \\\"Montana\\\", \\\".\\\"], \\\"h\\\": [\\\"billings logan international airport\\\", \\\"Q598269\\\", [[10, 11, 12, 13]]], \\\"t\\\": [\\\"billings, montana\\\", \\\"Q166304\\\", [[15, 16, 17]]]}, {\\\"tokens\\\": [\\\"Warsaw\\\", \\\"-\\\", \\\"Modlin\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"within\\\", \\\"the\\\", \\\"county\\\", \\\".\\\"], \\\"h\\\": [\\\"modlin airport\\\", \\\"Q1401995\\\", [[2, 3]]], \\\"t\\\": [\\\"warsaw\\\", \\\"Q270\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Tom\\\\u00e1s\\\", \\\"de\\\", \\\"Heres\\\", \\\"Airport\\\", \\\"(\\\", \\\",\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Ciudad\\\", \\\"Bol\\\\u00edvar\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\"of\\\", \\\"the\\\", \\\"Bol\\\\u00edvar\\\", \\\"state\\\", \\\"of\\\", \\\"Venezuela\\\", \\\".\\\"], \\\"h\\\": [\\\"tom\\\\u00e1s de heres airport\\\", \\\"Q1931117\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"ciudad bol\\\\u00edvar\\\", \\\"Q26906\\\", [[11, 12]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Rockford\\\", \\\"Airfest\\\", \\\"was\\\", \\\"a\\\", \\\"two\\\", \\\"-\\\", \\\"day\\\", \\\"air\\\", \\\"show\\\", \\\"that\\\", \\\"happened\\\", \\\"every\\\", \\\"year\\\", \\\"at\\\", \\\"Chicago\\\", \\\"Rockford\\\", \\\"International\\\", \\\"Airport\\\", \\\"located\\\", \\\"in\\\", \\\"Rockford\\\", \\\",\\\", \\\"Illinois\\\", \\\",\\\", \\\"USA\\\", \\\".\\\"], \\\"h\\\": [\\\"chicago rockford international airport\\\", \\\"Q1071990\\\", [[15, 16, 17, 18]]], \\\"t\\\": [\\\"rockford, illinois\\\", \\\"Q233892\\\", [[21, 22, 23]]]}, {\\\"tokens\\\": [\\\"Yolo\\\", \\\"County\\\", \\\"Airport\\\", \\\"is\\\", \\\"six\\\", \\\"miles\\\", \\\"northeast\\\", \\\"of\\\", \\\"Winters\\\", \\\",\\\", \\\"five\\\", \\\"miles\\\", \\\"northwest\\\", \\\"of\\\", \\\"Davis\\\", \\\"and\\\", \\\"five\\\", \\\"miles\\\", \\\"southwest\\\", \\\"of\\\", \\\"Woodland\\\", \\\",\\\", \\\"all\\\", \\\"in\\\", \\\"Yolo\\\", \\\"County\\\", \\\",\\\", \\\"California\\\", \\\".\\\"], \\\"h\\\": [\\\"yolo county airport\\\", \\\"Q10853689\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"davis\\\", \\\"Q668546\\\", [[14]]]}, {\\\"tokens\\\": [\\\"They\\\", \\\"are\\\", \\\"based\\\", \\\"at\\\", \\\"Newcastle\\\", \\\"Airport\\\", \\\",\\\", \\\"Tyne\\\", \\\"and\\\", \\\"Wear\\\", \\\",\\\", \\\"and\\\", \\\"at\\\", \\\"Carlisle\\\", \\\"Lake\\\", \\\"District\\\", \\\"Airport\\\", \\\",\\\", \\\"Cumbria\\\", \\\".\\\"], \\\"h\\\": [\\\"newcastle airport\\\", \\\"Q8975\\\", [[4, 5]]], \\\"t\\\": [\\\"tyne and wear\\\", \\\"Q23080\\\", [[7, 8, 9]]]}, {\\\"tokens\\\": [\\\"Noum\\\\u00e9a\\\", \\\"'s\\\", \\\"international\\\", \\\"airport\\\", \\\"is\\\", \\\"La\\\", \\\"Tontouta\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"from\\\", \\\"the\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"la tontouta international airport\\\", \\\"Q892783\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"noum\\\\u00e9a\\\", \\\"Q9733\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Zvartnots\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Yerevan\\\", \\\"'s\\\", \\\"international\\\", \\\"airport\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"near\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"Zvartnots\\\", \\\",\\\", \\\"as\\\", \\\"is\\\", \\\"the\\\", \\\"Zvartnots\\\", \\\"Cathedral\\\", \\\".\\\"], \\\"h\\\": [\\\"zvartnots international airport\\\", \\\"Q1124922\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"yerevan\\\", \\\"Q1953\\\", [[4]]]}, {\\\"tokens\\\": [\\\"Mohawk\\\", \\\"Valley\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"three\\\", \\\"nautical\\\", \\\"miles\\\", \\\"(\\\", \\\"6\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"northwest\\\", \\\"of\\\", \\\"the\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\"of\\\", \\\"Scotia\\\", \\\".\\\"], \\\"h\\\": [\\\"mohawk valley airport\\\", \\\"Q3565424\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"scotia\\\", \\\"Q1020602\\\", [[20]]]}, {\\\"tokens\\\": [\\\"M-553\\\", \\\"connects\\\", \\\"Marquette\\\", \\\"with\\\", \\\"Sawyer\\\", \\\"International\\\", \\\"Airport\\\", \\\"at\\\", \\\"the\\\", \\\"unincorporated\\\", \\\"community\\\", \\\"of\\\", \\\"K.I.\\\"], \\\"h\\\": [\\\"sawyer international airport\\\", \\\"Q4568758\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"marquette\\\", \\\"Q12443\\\", [[2]]]}, {\\\"tokens\\\": [\\\"Isiro\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Matari\\\", \\\"Airport\\\", \\\",\\\", \\\"a\\\", \\\"national\\\", \\\"airport\\\", \\\"with\\\", \\\"flights\\\", \\\"to\\\", \\\"Kinshasa\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\".\\\"], \\\"h\\\": [\\\"matari airport\\\", \\\"Q652383\\\", [[4, 5]]], \\\"t\\\": [\\\"isiro\\\", \\\"Q899873\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Canadair\\\", \\\"'s\\\", \\\"origins\\\", \\\"lie\\\", \\\"in\\\", \\\"the\\\", \\\"foundation\\\", \\\"of\\\", \\\"a\\\", \\\"manufacturing\\\", \\\"centre\\\", \\\"for\\\", \\\"Canadian\\\", \\\"Vickers\\\", \\\"in\\\", \\\"the\\\", \\\"Montreal\\\", \\\"suburb\\\", \\\"of\\\", \\\"Saint\\\", \\\"-\\\", \\\"Laurent\\\", \\\",\\\", \\\"at\\\", \\\"Cartierville\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"cartierville airport\\\", \\\"Q1961318\\\", [[24, 25]]], \\\"t\\\": [\\\"saint-laurent\\\", \\\"Q2117999\\\", [[19, 20, 21]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"wing\\\", \\\"headquarters\\\", \\\"is\\\", \\\"at\\\", \\\"the\\\", \\\"Rapid\\\", \\\"City\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Rapid\\\", \\\"City\\\", \\\",\\\", \\\"South\\\", \\\"Dakota\\\", \\\".\\\"], \\\"h\\\": [\\\"rapid city regional airport\\\", \\\"Q2876124\\\", [[6, 7, 8, 9]]], \\\"t\\\": [\\\"rapid city, south dakota\\\", \\\"Q213325\\\", [[11, 12, 13, 14, 15]]]}, {\\\"tokens\\\": [\\\"10,000\\\", \\\"at\\\", \\\"Baiyun\\\", \\\"Airport\\\", \\\"in\\\", \\\"Guangzhou\\\", \\\"were\\\", \\\"stranded\\\", \\\"after\\\", \\\"55\\\", \\\"flights\\\", \\\"were\\\", \\\"cancelled\\\", \\\".\\\"], \\\"h\\\": [\\\"baiyun airport\\\", \\\"Q44868\\\", [[2, 3]]], \\\"t\\\": [\\\"guangzhou\\\", \\\"Q16572\\\", [[5]]]}, {\\\"tokens\\\": [\\\"As\\\", \\\"of\\\", \\\"2013\\\", \\\",\\\", \\\"services\\\", \\\"between\\\", \\\"Bangkok\\\", \\\"and\\\", \\\"Los\\\", \\\"Angeles\\\", \\\"were\\\", \\\"served\\\", \\\"via\\\", \\\"Incheon\\\", \\\"International\\\", \\\"Airport\\\", \\\"near\\\", \\\"Seoul\\\", \\\",\\\", \\\"however\\\", \\\",\\\", \\\"it\\\", \\\"ended\\\", \\\"its\\\", \\\"service\\\", \\\"to\\\", \\\"the\\\", \\\"US\\\", \\\"on\\\", \\\"25\\\", \\\"October\\\", \\\"2015\\\", \\\".\\\"], \\\"h\\\": [\\\"incheon international airport\\\", \\\"Q20932\\\", [[13, 14, 15]]], \\\"t\\\": [\\\"seoul\\\", \\\"Q8684\\\", [[17]]]}, {\\\"tokens\\\": [\\\"C\\\\u00e9sar\\\", \\\"Gaviria\\\", \\\"Trujillo\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"In\\\\u00edrida\\\", \\\"in\\\", \\\"the\\\", \\\"Guain\\\\u00eda\\\", \\\"Department\\\", \\\"of\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"c\\\\u00e9sar gaviria trujillo airport\\\", \\\"Q1323400\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"in\\\\u00edrida\\\", \\\"Q130281\\\", [[11]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Solar\\\", \\\"Riser\\\", \\\"made\\\", \\\"the\\\", \\\"first\\\", \\\"man\\\", \\\"-\\\", \\\"carrying\\\", \\\"flight\\\", \\\"on\\\", \\\"solar\\\", \\\"power\\\", \\\"at\\\", \\\"noon\\\", \\\"on\\\", \\\"29\\\", \\\"April\\\", \\\"1979\\\", \\\"at\\\", \\\"Flabob\\\", \\\"Airport\\\", \\\"in\\\", \\\"Riverside\\\", \\\",\\\", \\\"California\\\", \\\".\\\"], \\\"h\\\": [\\\"flabob airport\\\", \\\"Q5456581\\\", [[20, 21]]], \\\"t\\\": [\\\"riverside, california\\\", \\\"Q49243\\\", [[23, 24, 25]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"aircraft\\\", \\\"involved\\\", \\\"was\\\", \\\"a\\\", \\\"Boeing\\\", \\\"737\\\", \\\"-\\\", \\\"3H4\\\", \\\"N387SW\\\", \\\",\\\", \\\"serial\\\", \\\"number\\\", \\\"26602\\\", \\\",\\\", \\\"operating\\\", \\\"a\\\", \\\"scheduled\\\", \\\"flight\\\", \\\"between\\\", \\\"Nashville\\\", \\\",\\\", \\\"Tennessee\\\", \\\"(\\\", \\\"KBNA\\\", \\\")\\\", \\\",\\\", \\\"and\\\", \\\"Baltimore\\\", \\\",\\\", \\\"Maryland\\\", \\\"(\\\", \\\"KBWI\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"kbwi\\\", \\\"Q94895\\\", [[32]]], \\\"t\\\": [\\\"baltimore, maryland\\\", \\\"Q5092\\\", [[28, 29, 30]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"base\\\", \\\"was\\\", \\\"Moi\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Mombasa\\\", \\\".\\\"], \\\"h\\\": [\\\"moi international airport\\\", \\\"Q392784\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"mombasa\\\", \\\"Q225641\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Leo\\\", \\\"Wattimena\\\", \\\"Airport\\\", \\\",\\\", \\\"formerly\\\", \\\"known\\\", \\\"as\\\", \\\"Pitu\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"private\\\", \\\"airport\\\", \\\"located\\\", \\\"on\\\", \\\"the\\\", \\\"southern\\\", \\\"coast\\\", \\\"of\\\", \\\"Morotai\\\", \\\"Island\\\", \\\",\\\", \\\"North\\\", \\\"Maluku\\\", \\\",\\\", \\\"Indonesia\\\", \\\".\\\"], \\\"h\\\": [\\\"leo wattimena airport\\\", \\\"Q4272507\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"morotai island\\\", \\\"Q19146\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"La\\\", \\\"Mina\\\", \\\"Airport\\\", \\\",\\\", \\\"or\\\", \\\"Jorge\\\", \\\"Isaacs\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Maicao\\\", \\\",\\\", \\\"a\\\", \\\"municipality\\\", \\\"in\\\", \\\"the\\\", \\\"La\\\", \\\"Guajira\\\", \\\"Department\\\", \\\"in\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"jorge isaacs airport\\\", \\\"Q2902722\\\", [[5, 6, 7]]], \\\"t\\\": [\\\"maicao\\\", \\\"Q1937427\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Bu\\\\u00f4n\\\", \\\"Ma\\\", \\\"Thu\\\\u1ed9t\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Buon\\\", \\\"Ma\\\", \\\"Thuot\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"buon ma thuot airport\\\", \\\"Q695570\\\", [[6, 7, 8, 9]]], \\\"t\\\": [\\\"bu\\\\u00f4n ma thu\\\\u1ed9t\\\", \\\"Q33469\\\", [[0, 1, 2]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"crash\\\", \\\"occurred\\\", \\\"off\\\", \\\"the\\\", \\\"coast\\\", \\\"of\\\", \\\"Jeju\\\", \\\"Island\\\", \\\"after\\\", \\\"the\\\", \\\"crew\\\", \\\"reported\\\", \\\"a\\\", \\\"fire\\\", \\\"in\\\", \\\"the\\\", \\\"cargo\\\", \\\"compartment\\\", \\\"and\\\", \\\"had\\\", \\\"been\\\", \\\"attempting\\\", \\\"to\\\", \\\"divert\\\", \\\"to\\\", \\\"Jeju\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"jeju international airport\\\", \\\"Q482497\\\", [[26, 27, 28]]], \\\"t\\\": [\\\"jeju island\\\", \\\"Q29151\\\", [[7, 8]]]}, {\\\"tokens\\\": [\\\"Childress\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"commercial\\\", \\\"airport\\\", \\\"located\\\", \\\"within\\\", \\\"city\\\", \\\"limits\\\", \\\",\\\", \\\"4\\\", \\\"miles\\\", \\\"west\\\", \\\"of\\\", \\\"central\\\", \\\"Childress\\\", \\\",\\\", \\\"Texas\\\", \\\".\\\"], \\\"h\\\": [\\\"childress municipal airport\\\", \\\"Q3274003\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"childress, texas\\\", \\\"Q982513\\\", [[17, 18, 19]]]}, {\\\"tokens\\\": [\\\"Jos\\\\u00e9\\\", \\\"Leonardo\\\", \\\"Chirino\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Coro\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\"of\\\", \\\"Falc\\\\u00f3n\\\", \\\"state\\\", \\\"in\\\", \\\"Venezuela\\\", \\\".\\\"], \\\"h\\\": [\\\"jos\\\\u00e9 leonardo chirino airport\\\", \\\"Q1322397\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"coro\\\", \\\"Q1134454\\\", [[9]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Mid\\\", \\\"-\\\", \\\"Atlantic\\\", \\\"Air\\\", \\\"Museum\\\", \\\"(\\\", \\\"MAAM\\\", \\\")\\\", \\\"is\\\", \\\"membership\\\", \\\"supported\\\", \\\"museum\\\", \\\"and\\\", \\\"aircraft\\\", \\\"restoration\\\", \\\"facility\\\", \\\"located\\\", \\\"at\\\", \\\"Reading\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Reading\\\", \\\",\\\", \\\"Pennsylvania\\\", \\\".\\\"], \\\"h\\\": [\\\"reading regional airport\\\", \\\"Q7300558\\\", [[19, 20, 21]]], \\\"t\\\": [\\\"reading, pennsylvania\\\", \\\"Q237896\\\", [[23, 24, 25]]]}, {\\\"tokens\\\": [\\\"Destinations\\\", \\\"served\\\", \\\"as\\\", \\\"of\\\", \\\"2014\\\", \\\"are\\\", \\\"London\\\", \\\"(\\\", \\\"Stansted\\\", \\\"&\\\", \\\"Luton\\\", \\\")\\\", \\\",\\\", \\\"Frankfurt\\\", \\\"-\\\", \\\"Hahn\\\", \\\"Airport\\\", \\\",\\\", \\\"Faro\\\", \\\",\\\", \\\"Portugal\\\", \\\"and\\\", \\\"Alicante\\\", \\\"all\\\", \\\"operated\\\", \\\"by\\\", \\\"Ryanair\\\", \\\".\\\"], \\\"h\\\": [\\\"stansted\\\", \\\"Q8709\\\", [[8]]], \\\"t\\\": [\\\"london\\\", \\\"Q84\\\", [[6]]]}, {\\\"tokens\\\": [\\\"Steamboat\\\", \\\"Springs\\\", \\\"Airport\\\", \\\"(\\\", \\\"Bob\\\", \\\"Adams\\\", \\\"Field\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"city\\\", \\\"owned\\\", \\\"airport\\\", \\\"three\\\", \\\"miles\\\", \\\"northwest\\\", \\\"of\\\", \\\"Steamboat\\\", \\\"Springs\\\", \\\",\\\", \\\"in\\\", \\\"Routt\\\", \\\"County\\\", \\\",\\\", \\\"Colorado\\\", \\\".\\\"], \\\"h\\\": [\\\"bob adams field\\\", \\\"Q7605416\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"steamboat springs\\\", \\\"Q984721\\\", [[0, 1], [17, 18]]]}, {\\\"tokens\\\": [\\\"Bullfrog\\\", \\\"Basin\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"airport\\\", \\\"located\\\", \\\"north\\\", \\\"of\\\", \\\"the\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\"of\\\", \\\"the\\\", \\\"Glen\\\", \\\"Canyon\\\", \\\"National\\\", \\\"Recreation\\\", \\\"Area\\\", \\\",\\\", \\\"in\\\", \\\"Kane\\\", \\\"County\\\", \\\",\\\", \\\"Utah\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"bullfrog basin airport\\\", \\\"Q3887489\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"glen canyon national recreation area\\\", \\\"Q1373278\\\", [[16, 17, 18, 19, 20]]]}, {\\\"tokens\\\": [\\\"Las\\\", \\\"Breas\\\", \\\"Airport\\\", \\\"(\\\", \\\",\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"south\\\", \\\"-\\\", \\\"southeast\\\", \\\"of\\\", \\\"Taltal\\\", \\\",\\\", \\\"a\\\", \\\"Pacific\\\", \\\"coastal\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Antofagasta\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"las breas airport\\\", \\\"Q16893977\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"taltal\\\", \\\"Q188049\\\", [[13]]]}, {\\\"tokens\\\": [\\\"There\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"the\\\", \\\"district\\\", \\\"located\\\", \\\"in\\\", \\\"Puttaparthi\\\", \\\",\\\", \\\"known\\\", \\\"as\\\", \\\"Sri\\\", \\\"Sathya\\\", \\\"Sai\\\", \\\"Airport\\\", \\\";\\\", \\\"however\\\", \\\"this\\\", \\\"airport\\\", \\\"currently\\\", \\\"has\\\", \\\"no\\\", \\\"scheduled\\\", \\\"service\\\", \\\".\\\"], \\\"h\\\": [\\\"sri sathya sai airport\\\", \\\"Q1939560\\\", [[13, 14, 15, 16]]], \\\"t\\\": [\\\"puttaparthi\\\", \\\"Q1068595\\\", [[9]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"1959\\\", \\\",\\\", \\\"the\\\", \\\"larger\\\", \\\"Boryspil\\\", \\\"International\\\", \\\"Airport\\\", \\\"was\\\", \\\"built\\\", \\\"near\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Boryspil\\\", \\\",\\\", \\\"gradually\\\", \\\"replacing\\\", \\\"Zhuliany\\\", \\\"as\\\", \\\"the\\\", \\\"main\\\", \\\"airport\\\", \\\"serving\\\", \\\"Kyiv\\\", \\\".\\\"], \\\"h\\\": [\\\"boryspil international airport\\\", \\\"Q477677\\\", [[5, 6, 7]]], \\\"t\\\": [\\\"kyiv\\\", \\\"Q1899\\\", [[24]]]}, {\\\"tokens\\\": [\\\"Badanjilin\\\", \\\"Airport\\\", \\\"is\\\", \\\"one\\\", \\\"of\\\", \\\"the\\\", \\\"three\\\", \\\"airports\\\", \\\"of\\\", \\\"Alxa\\\", \\\"League\\\", \\\"in\\\", \\\"western\\\", \\\"Inner\\\", \\\"Mongolia\\\", \\\",\\\", \\\"the\\\", \\\"other\\\", \\\"two\\\", \\\"being\\\", \\\"Alxa\\\", \\\"Left\\\", \\\"Banner\\\", \\\"Bayanhot\\\", \\\"Airport\\\", \\\"and\\\", \\\"Ejin\\\", \\\"Banner\\\", \\\"Taolai\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"alxa left banner bayanhot airport\\\", \\\"Q16258986\\\", [[20, 21, 22, 23, 24]]], \\\"t\\\": [\\\"alxa league\\\", \\\"Q449963\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"Capital\\\", \\\"City\\\", \\\"Airport\\\", \\\"(\\\", \\\"currently\\\", \\\"used\\\", \\\"by\\\", \\\"general\\\", \\\"aviation\\\", \\\";\\\", \\\"formerly\\\", \\\"Harrisburg\\\", \\\"'s\\\", \\\"principal\\\", \\\"airport\\\", \\\")\\\", \\\"and\\\", \\\"the\\\", \\\"New\\\", \\\"Cumberland\\\", \\\"Army\\\", \\\"Depot\\\", \\\"both\\\", \\\"lie\\\", \\\"in\\\", \\\"Fairview\\\", \\\"Township\\\", \\\".\\\"], \\\"h\\\": [\\\"capital city airport\\\", \\\"Q3274856\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"harrisburg\\\", \\\"Q25280\\\", [[11]]]}, {\\\"tokens\\\": [\\\"Meythet\\\", \\\"Airport\\\", \\\"in\\\", \\\"Annecy\\\", \\\"has\\\", \\\"Air\\\", \\\"France\\\", \\\"Regional\\\", \\\"round\\\", \\\"-\\\", \\\"trip\\\", \\\"service\\\", \\\"to\\\", \\\"Paris\\\", \\\"Orly\\\", \\\".\\\"], \\\"h\\\": [\\\"meythet airport\\\", \\\"Q1430810\\\", [[0, 1]]], \\\"t\\\": [\\\"annecy\\\", \\\"Q50189\\\", [[3]]]}, {\\\"tokens\\\": [\\\"During\\\", \\\"the\\\", \\\"late\\\", \\\"morning\\\", \\\"of\\\", \\\"April\\\", \\\"3\\\", \\\",\\\", \\\"1964\\\", \\\",\\\", \\\"a\\\", \\\"destructive\\\", \\\"tornado\\\", \\\"ripped\\\", \\\"through\\\", \\\"the\\\", \\\"City\\\", \\\"View\\\", \\\"section\\\", \\\"of\\\", \\\"northwestern\\\", \\\"Wichita\\\", \\\"Falls\\\", \\\"and\\\", \\\"neighboring\\\", \\\"Sheppard\\\", \\\"Air\\\", \\\"Force\\\", \\\"Base\\\", \\\".\\\"], \\\"h\\\": [\\\"sheppard air force base\\\", \\\"Q176146\\\", [[25, 26, 27, 28]]], \\\"t\\\": [\\\"wichita falls\\\", \\\"Q128349\\\", [[21, 22]]]}, {\\\"tokens\\\": [\\\"44\\\", \\\"-\\\", \\\"73287\\\", \\\")\\\", \\\"currently\\\", \\\"based\\\", \\\"at\\\", \\\"the\\\", \\\"Air\\\", \\\"Combat\\\", \\\"Museum\\\", \\\"at\\\", \\\"Abraham\\\", \\\"Lincoln\\\", \\\"Capital\\\", \\\"Airport\\\", \\\"in\\\", \\\"Springfield\\\", \\\",\\\", \\\"Illinois\\\", \\\".\\\"], \\\"h\\\": [\\\"abraham lincoln capital airport\\\", \\\"Q1320523\\\", [[12, 13, 14, 15]]], \\\"t\\\": [\\\"springfield\\\", \\\"Q28515\\\", [[17]]]}, {\\\"tokens\\\": [\\\"Employed\\\", \\\"by\\\", \\\"Australian\\\", \\\"National\\\", \\\"Airways\\\", \\\"(\\\", \\\"ANA\\\", \\\")\\\", \\\"after\\\", \\\"leaving\\\", \\\"the\\\", \\\"Air\\\", \\\"Force\\\", \\\",\\\", \\\"Lukis\\\", \\\"become\\\", \\\"airfield\\\", \\\"manager\\\", \\\"at\\\", \\\"Essendon\\\", \\\",\\\", \\\"Melbourne\\\", \\\".\\\"], \\\"h\\\": [\\\"essendon\\\", \\\"Q1319272\\\", [[19]]], \\\"t\\\": [\\\"melbourne\\\", \\\"Q3141\\\", [[21]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Laurel\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"publicly\\\", \\\"owned\\\", \\\"public\\\", \\\"-\\\", \\\"use\\\", \\\"airport\\\", \\\"in\\\", \\\"Laurel\\\", \\\",\\\", \\\"Montana\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"located\\\", \\\"southwest\\\", \\\"of\\\", \\\"downtown\\\", \\\"Billings\\\", \\\".\\\"], \\\"h\\\": [\\\"laurel municipal airport\\\", \\\"Q6499928\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"laurel, montana\\\", \\\"Q768628\\\", [[13, 14, 15]]]}, {\\\"tokens\\\": [\\\"Hualien\\\", \\\"City\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Hualien\\\", \\\"Airport\\\", \\\"located\\\", \\\"at\\\", \\\"the\\\", \\\"neighboring\\\", \\\"Xincheng\\\", \\\"Township\\\", \\\"of\\\", \\\"Hualien\\\", \\\"County\\\", \\\".\\\"], \\\"h\\\": [\\\"hualien airport\\\", \\\"Q703921\\\", [[5, 6]]], \\\"t\\\": [\\\"hualien city\\\", \\\"Q713310\\\", [[0, 1]]]}, {\\\"tokens\\\": [\\\"Merlin\\\", \\\"Airways\\\", \\\",\\\", \\\"Inc.\\\", \\\"is\\\", \\\"a\\\", \\\"cargo\\\", \\\"airline\\\", \\\"based\\\", \\\"in\\\", \\\"Rafael\\\", \\\"Hern\\\\u00e1ndez\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Aguadilla\\\", \\\",\\\", \\\"Puerto\\\", \\\"Rico\\\", \\\".\\\"], \\\"h\\\": [\\\"rafael hern\\\\u00e1ndez international airport\\\", \\\"Q2276582\\\", [[10, 11, 12, 13]]], \\\"t\\\": [\\\"aguadilla, puerto rico\\\", \\\"Q397826\\\", [[15, 16, 17, 18]]]}, {\\\"tokens\\\": [\\\"Due\\\", \\\"to\\\", \\\"the\\\", \\\"extensive\\\", \\\"military\\\", \\\"cooperation\\\", \\\"between\\\", \\\"both\\\", \\\"countries\\\", \\\",\\\", \\\"there\\\", \\\"are\\\", \\\"also\\\", \\\"around\\\", \\\"3,500\\\", \\\"American\\\", \\\"military\\\", \\\"personnel\\\", \\\"stationed\\\", \\\"at\\\", \\\"the\\\", \\\"Al\\\", \\\"Dhafra\\\", \\\"Air\\\", \\\"Base\\\", \\\"in\\\", \\\"Abu\\\", \\\"Dhabi\\\", \\\".\\\"], \\\"h\\\": [\\\"al dhafra air base\\\", \\\"Q2886453\\\", [[21, 22, 23, 24]]], \\\"t\\\": [\\\"abu dhabi\\\", \\\"Q1519\\\", [[26, 27]]]}, {\\\"tokens\\\": [\\\"Johan\\\", \\\"Pienaar\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Kuruman\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"Northern\\\", \\\"Cape\\\", \\\"province\\\", \\\",\\\", \\\"South\\\", \\\"Africa\\\", \\\".\\\"], \\\"h\\\": [\\\"johan pienaar airport\\\", \\\"Q1580098\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"kuruman\\\", \\\"Q1025965\\\", [[7]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"hub\\\", \\\"is\\\", \\\"at\\\", \\\"Shahjalal\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Dhaka\\\", \\\"and\\\", \\\"it\\\", \\\"also\\\", \\\"operates\\\", \\\"flights\\\", \\\"from\\\", \\\"its\\\", \\\"secondary\\\", \\\"hubs\\\", \\\"at\\\", \\\"Shah\\\", \\\"Amanat\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Chittagong\\\", \\\"and\\\", \\\"Osmani\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Sylhet\\\", \\\".\\\"], \\\"h\\\": [\\\"shah amanat international airport\\\", \\\"Q525609\\\", [[20, 21, 22, 23]]], \\\"t\\\": [\\\"chittagong\\\", \\\"Q376749\\\", [[25]]]}, {\\\"tokens\\\": [\\\"Nodaway\\\", \\\"County\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Northwest\\\", \\\"Missouri\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Maryville\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"a\\\", \\\"general\\\", \\\"aviation\\\", \\\"airport\\\", \\\"with\\\", \\\"no\\\", \\\"commercial\\\", \\\"service\\\", \\\".\\\"], \\\"h\\\": [\\\"northwest missouri regional airport\\\", \\\"Q7060119\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"maryville\\\", \\\"Q957284\\\", [[10]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"2007\\\", \\\",\\\", \\\"they\\\", \\\"moved\\\", \\\"to\\\", \\\"a\\\", \\\"new\\\", \\\"custom\\\", \\\"built\\\", \\\"facility\\\", \\\"at\\\", \\\"Portsmouth\\\", \\\"International\\\", \\\"Airport\\\", \\\"at\\\", \\\"Pease\\\", \\\"in\\\", \\\"Portsmouth\\\", \\\",\\\", \\\"New\\\", \\\"Hampshire\\\", \\\".\\\", \\\"Shir\\\", \\\"Haberman\\\", \\\"(\\\", \\\"2\\\", \\\"June\\\", \\\"2008\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"portsmouth international airport at pease\\\", \\\"Q6587102\\\", [[12, 13, 14, 15, 16]]], \\\"t\\\": [\\\"portsmouth, new hampshire\\\", \\\"Q49191\\\", [[18, 19, 20, 21]]]}, {\\\"tokens\\\": [\\\"Thai\\\", \\\"Airways\\\", \\\"International\\\", \\\"Flight\\\", \\\"311\\\", \\\"was\\\", \\\"a\\\", \\\"flight\\\", \\\"from\\\", \\\"Bangkok\\\", \\\",\\\", \\\"Thailand\\\", \\\"'s\\\", \\\"Don\\\", \\\"Mueang\\\", \\\"International\\\", \\\"Airport\\\", \\\"to\\\", \\\"Kathmandu\\\", \\\",\\\", \\\"Nepal\\\", \\\"'s\\\", \\\"Tribhuvan\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"tribhuvan international airport\\\", \\\"Q61066\\\", [[22, 23, 24]]], \\\"t\\\": [\\\"kathmandu\\\", \\\"Q3037\\\", [[18]]]}, {\\\"tokens\\\": [\\\"Most\\\", \\\"of\\\", \\\"the\\\", \\\"scheduled\\\", \\\"flights\\\", \\\"are\\\", \\\"to\\\", \\\"the\\\", \\\"Bahamas\\\", \\\",\\\", \\\"with\\\", \\\"flights\\\", \\\"to\\\", \\\"Albert\\\", \\\"Whitted\\\", \\\"Airport\\\", \\\"in\\\", \\\"St\\\", \\\"Petersburg\\\", \\\",\\\", \\\"Florida\\\", \\\".\\\"], \\\"h\\\": [\\\"albert whitted airport\\\", \\\"Q4711466\\\", [[13, 14, 15]]], \\\"t\\\": [\\\"st petersburg\\\", \\\"Q49236\\\", [[17, 18]]]}, {\\\"tokens\\\": [\\\"Mammoth\\\", \\\"Yosemite\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"town\\\", \\\"-\\\", \\\"owned\\\", \\\"public\\\", \\\"airport\\\", \\\"seven\\\", \\\"miles\\\", \\\"east\\\", \\\"of\\\", \\\"Mammoth\\\", \\\"Lakes\\\", \\\",\\\", \\\"in\\\", \\\"Mono\\\", \\\"County\\\", \\\",\\\", \\\"California\\\", \\\".\\\"], \\\"h\\\": [\\\"mammoth yosemite airport\\\", \\\"Q6745883\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"mammoth lakes\\\", \\\"Q983604\\\", [[14, 15]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"replaces\\\", \\\"Tena\\\", \\\"'s\\\", \\\"Mayor\\\", \\\"Galo\\\", \\\"de\\\", \\\"la\\\", \\\"Torre\\\", \\\"Airport\\\", \\\",\\\", \\\"which\\\", \\\"closed\\\", \\\"in\\\", \\\"2001\\\", \\\".\\\"], \\\"h\\\": [\\\"mayor galo de la torre airport\\\", \\\"Q22632230\\\", [[4, 5, 6, 7, 8, 9]]], \\\"t\\\": [\\\"tena\\\", \\\"Q994312\\\", [[2]]]}, {\\\"tokens\\\": [\\\"Alamosa\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"San\\\", \\\"Luis\\\", \\\"Valley\\\", \\\"Regional\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"san luis valley regional airport\\\", \\\"Q7414773\\\", [[4, 5, 6, 7, 8]]], \\\"t\\\": [\\\"alamosa\\\", \\\"Q1010247\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Dallas\\\", \\\"-\\\", \\\"Fort\\\", \\\"Worth\\\", \\\"Metroplex\\\", \\\"'s\\\", \\\"major\\\", \\\"international\\\", \\\"airport\\\", \\\",\\\", \\\"Dallas\\\", \\\"-\\\", \\\"Fort\\\", \\\"Worth\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"a\\\", \\\"short\\\", \\\"distance\\\", \\\"to\\\", \\\"the\\\", \\\"northwest\\\", \\\".\\\"], \\\"h\\\": [\\\"dallas-fort worth international airport\\\", \\\"Q459096\\\", [[11, 12, 13, 14, 15, 16]]], \\\"t\\\": [\\\"dallas-fort worth metroplex\\\", \\\"Q179295\\\", [[1, 2, 3, 4, 5]]]}, {\\\"tokens\\\": [\\\"P\\\\u00e9rigueux\\\", \\\"-\\\", \\\"Bassillac\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"the\\\", \\\"village\\\", \\\"of\\\", \\\"Bassillac\\\", \\\"in\\\", \\\"the\\\", \\\"Dordogne\\\", \\\"department\\\", \\\",\\\", \\\"Nouvelle\\\", \\\"-\\\", \\\"Aquitaine\\\", \\\"region\\\", \\\",\\\", \\\"France\\\", \\\".\\\"], \\\"h\\\": [\\\"bassillac airport\\\", \\\"Q1432520\\\", [[2, 3]]], \\\"t\\\": [\\\"p\\\\u00e9rigueux\\\", \\\"Q6588\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"main\\\", \\\"settlement\\\", \\\"is\\\", \\\"Seronera\\\", \\\",\\\", \\\"which\\\", \\\"houses\\\", \\\"the\\\", \\\"majority\\\", \\\"of\\\", \\\"research\\\", \\\"staff\\\", \\\"and\\\", \\\"the\\\", \\\"park\\\", \\\"'s\\\", \\\"main\\\", \\\"headquarters\\\", \\\",\\\", \\\"including\\\", \\\"its\\\", \\\"primary\\\", \\\"airstrip\\\", \\\".\\\"], \\\"h\\\": [\\\"airstrip\\\", \\\"Q7455033\\\", [[23]]], \\\"t\\\": [\\\"seronera\\\", \\\"Q6273481\\\", [[4]]]}, {\\\"tokens\\\": [\\\"Jakar\\\", \\\"is\\\", \\\"also\\\", \\\"the\\\", \\\"site\\\", \\\"of\\\", \\\"Bathpalathang\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"bathpalathang airport\\\", \\\"Q153191\\\", [[6, 7]]], \\\"t\\\": [\\\"jakar\\\", \\\"Q2468415\\\", [[0]]]}, {\\\"tokens\\\": [\\\"A\\\", \\\"runway\\\", \\\"at\\\", \\\"the\\\", \\\"Cape\\\", \\\"Canaveral\\\", \\\"Air\\\", \\\"Force\\\", \\\"Station\\\", \\\"is\\\", \\\"still\\\", \\\"known\\\", \\\"as\\\", \\\"the\\\", \\\"\\\\\\\"\\\", \\\"Skid\\\", \\\"Strip\\\", \\\"\\\\\\\"\\\", \\\".\\\"], \\\"h\\\": [\\\"\\\\\\\"skid strip\\\\\\\"\\\", \\\"Q3275436\\\", [[14, 15, 16, 17]]], \\\"t\\\": [\\\"cape canaveral air force station\\\", \\\"Q334465\\\", [[4, 5, 6, 7, 8]]]}, {\\\"tokens\\\": [\\\"Siglufj\\\\u00f6r\\\\u00f0ur\\\", \\\"Airport\\\", \\\"or\\\", \\\"Siglufjordur\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Siglufj\\\\u00f6r\\\\u00f0ur\\\", \\\",\\\", \\\"Iceland\\\", \\\".\\\"], \\\"h\\\": [\\\"siglufjordur airport\\\", \\\"Q2875922\\\", [[3, 4]]], \\\"t\\\": [\\\"siglufj\\\\u00f6r\\\\u00f0ur\\\", \\\"Q1887662\\\", [[0], [9]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"February\\\", \\\"1935\\\", \\\",\\\", \\\"Hardy\\\", \\\"entered\\\", \\\"aviation\\\", \\\"cadet\\\", \\\"training\\\", \\\"at\\\", \\\"Randolph\\\", \\\"Field\\\", \\\"in\\\", \\\"San\\\", \\\"Antonio\\\", \\\".\\\"], \\\"h\\\": [\\\"randolph field\\\", \\\"Q980034\\\", [[10, 11]]], \\\"t\\\": [\\\"san antonio\\\", \\\"Q975\\\", [[13, 14]]]}, {\\\"tokens\\\": [\\\"APS\\\", \\\"is\\\", \\\"headquartered\\\", \\\"at\\\", \\\"the\\\", \\\"Phoenix\\\", \\\"-\\\", \\\"Mesa\\\", \\\"Gateway\\\", \\\"Airport\\\", \\\"(\\\", \\\"KIWA\\\", \\\")\\\", \\\"in\\\", \\\"Mesa\\\", \\\",\\\", \\\"Arizona\\\", \\\".\\\"], \\\"h\\\": [\\\"phoenix-mesa gateway airport\\\", \\\"Q493759\\\", [[5, 6, 7, 8, 9]]], \\\"t\\\": [\\\"mesa, arizona\\\", \\\"Q49261\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"hub\\\", \\\"is\\\", \\\"Golos\\\\u00f3n\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"La\\\", \\\"Ceiba\\\", \\\".\\\"], \\\"h\\\": [\\\"golos\\\\u00f3n international airport\\\", \\\"Q2231517\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"la ceiba\\\", \\\"Q916536\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"March\\\", \\\"24\\\", \\\",\\\", \\\"the\\\", \\\"production\\\", \\\"moved\\\", \\\"to\\\", \\\"Raymond\\\", \\\",\\\", \\\"Mississippi\\\", \\\",\\\", \\\"where\\\", \\\"the\\\", \\\"crew\\\", \\\"filmed\\\", \\\"a\\\", \\\"scene\\\", \\\"at\\\", \\\"the\\\", \\\"John\\\", \\\"Bell\\\", \\\"Williams\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"john bell williams airport\\\", \\\"Q2901886\\\", [[20, 21, 22, 23]]], \\\"t\\\": [\\\"raymond, mississippi\\\", \\\"Q1779125\\\", [[8, 9, 10]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Bell\\\", \\\"430\\\", \\\"helicopter\\\", \\\"took\\\", \\\"off\\\", \\\"from\\\", \\\"Begumpet\\\", \\\"Airport\\\", \\\",\\\", \\\"Hyderabad\\\", \\\",\\\", \\\"and\\\", \\\"soon\\\", \\\"encountered\\\", \\\"bad\\\", \\\"weather\\\", \\\".\\\"], \\\"h\\\": [\\\"begumpet airport\\\", \\\"Q1657769\\\", [[7, 8]]], \\\"t\\\": [\\\"hyderabad\\\", \\\"Q1361\\\", [[10]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Visalia\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"city\\\", \\\"-\\\", \\\"owned\\\", \\\"airport\\\", \\\"for\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Visalia\\\", \\\",\\\", \\\"California\\\", \\\".\\\"], \\\"h\\\": [\\\"visalia municipal airport\\\", \\\"Q7935607\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"visalia, california\\\", \\\"Q495373\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"Stinson\\\", \\\"Field\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"closed\\\", \\\"airport\\\", \\\"located\\\", \\\"3\\\", \\\"miles\\\", \\\"northwest\\\", \\\"of\\\", \\\"Aberdeen\\\", \\\",\\\", \\\"Mississippi\\\", \\\".\\\"], \\\"h\\\": [\\\"stinson field municipal airport\\\", \\\"Q7617473\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"aberdeen, mississippi\\\", \\\"Q1065452\\\", [[12, 13, 14]]]}, {\\\"tokens\\\": [\\\"Sua\\\", \\\"Pan\\\", \\\"Airport\\\", \\\"or\\\", \\\"Sowa\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"west\\\", \\\"of\\\", \\\"Sowa\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Central\\\", \\\"District\\\", \\\"of\\\", \\\"Botswana\\\", \\\".\\\"], \\\"h\\\": [\\\"sua pan airport\\\", \\\"Q7630421\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"sowa\\\", \\\"Q141310\\\", [[4], [11]]]}, {\\\"tokens\\\": [\\\"They\\\", \\\"operated\\\", \\\"the\\\", \\\"first\\\", \\\"services\\\", \\\"to\\\", \\\"Dunedin\\\", \\\"'s\\\", \\\"new\\\", \\\"Momona\\\", \\\"Airport\\\", \\\"in\\\", \\\"1962\\\", \\\"until\\\", \\\"traffic\\\", \\\"built\\\", \\\"up\\\", \\\"enough\\\", \\\"to\\\", \\\"use\\\", \\\"the\\\", \\\"Viscounts\\\", \\\"there\\\", \\\".\\\"], \\\"h\\\": [\\\"momona airport\\\", \\\"Q1364375\\\", [[9, 10]]], \\\"t\\\": [\\\"dunedin\\\", \\\"Q133073\\\", [[6]]]}, {\\\"tokens\\\": [\\\"Tepper\\\", \\\"Aviation\\\", \\\",\\\", \\\"Inc.\\\", \\\"is\\\", \\\"based\\\", \\\"at\\\", \\\"the\\\", \\\"Bob\\\", \\\"Sikes\\\", \\\"Airport\\\", \\\"in\\\", \\\"Crestview\\\", \\\",\\\", \\\"Florida\\\", \\\".\\\"], \\\"h\\\": [\\\"bob sikes airport\\\", \\\"Q597487\\\", [[8, 9, 10]]], \\\"t\\\": [\\\"crestview, florida\\\", \\\"Q2153124\\\", [[12, 13, 14]]]}, {\\\"tokens\\\": [\\\"Northern\\\", \\\"Area\\\", \\\"CFTSU\\\", \\\"is\\\", \\\"based\\\", \\\"at\\\", \\\"HMNZS\\\", \\\"Philomel\\\", \\\"in\\\", \\\"Auckland\\\", \\\",\\\", \\\"Central\\\", \\\"Area\\\", \\\"CFTSU\\\", \\\"at\\\", \\\"RNZAF\\\", \\\"Base\\\", \\\"Ohakea\\\", \\\"near\\\", \\\"Palmerston\\\", \\\"North\\\", \\\"and\\\", \\\"Southern\\\", \\\"Area\\\", \\\"CFTSU\\\", \\\"at\\\", \\\"Burnham\\\", \\\"Military\\\", \\\"Camp\\\", \\\"just\\\", \\\"South\\\", \\\"of\\\", \\\"Christchurch\\\", \\\".\\\"], \\\"h\\\": [\\\"rnzaf base ohakea\\\", \\\"Q7277291\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"palmerston north\\\", \\\"Q212289\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"Br\\\\u010dko\\\", \\\"was\\\", \\\"a\\\", \\\"geographic\\\", \\\"point\\\", \\\"of\\\", \\\"contention\\\", \\\"in\\\", \\\"1996\\\", \\\"when\\\", \\\"the\\\", \\\"U.S\\\", \\\".-\\\", \\\"led\\\", \\\"Implementation\\\", \\\"Force\\\", \\\"(\\\", \\\"IFOR\\\", \\\")\\\", \\\"built\\\", \\\"Camp\\\", \\\"McGovern\\\", \\\"on\\\", \\\"the\\\", \\\"outskirts\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"camp mcgovern\\\", \\\"Q16890056\\\", [[20, 21]]], \\\"t\\\": [\\\"br\\\\u010dko\\\", \\\"Q322828\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Potomac\\\", \\\"Highlands\\\", \\\"Airport\\\", \\\"Authority\\\", \\\"is\\\", \\\"an\\\", \\\"Interstate\\\", \\\"Agency\\\", \\\"that\\\", \\\"operates\\\", \\\"the\\\", \\\"Greater\\\", \\\"Cumberland\\\", \\\"Regional\\\", \\\"Airport\\\", \\\",\\\", \\\"two\\\", \\\"miles\\\", \\\"south\\\", \\\"of\\\", \\\"Cumberland\\\", \\\",\\\", \\\"Maryland\\\", \\\"in\\\", \\\"the\\\", \\\"state\\\", \\\"of\\\", \\\"West\\\", \\\"Virginia\\\", \\\".\\\"], \\\"h\\\": [\\\"greater cumberland regional airport\\\", \\\"Q3913914\\\", [[12, 13, 14, 15]]], \\\"t\\\": [\\\"cumberland, maryland\\\", \\\"Q754868\\\", [[21, 22, 23]]]}, {\\\"tokens\\\": [\\\"Baucau\\\", \\\"Airport\\\", \\\",\\\", \\\"former\\\", \\\"Cakung\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"unattended\\\", \\\"airport\\\", \\\"located\\\", \\\"west\\\", \\\"of\\\", \\\"Baucau\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"East\\\", \\\"Timor\\\", \\\"(\\\", \\\"\\\\\\\"\\\", \\\"Timor\\\", \\\"-\\\", \\\"Leste\\\", \\\"\\\\\\\"\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"cakung airport\\\", \\\"Q1430948\\\", [[4, 5]]], \\\"t\\\": [\\\"baucau\\\", \\\"Q811130\\\", [[0], [14]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"operations\\\", \\\"initially\\\", \\\"focused\\\", \\\"on\\\", \\\"providing\\\", \\\"air\\\", \\\"service\\\", \\\"into\\\", \\\"Borrego\\\", \\\"Springs\\\", \\\",\\\", \\\"California\\\", \\\"via\\\", \\\"the\\\", \\\"Borrego\\\", \\\"Valley\\\", \\\"Airport\\\", \\\"from\\\", \\\"other\\\", \\\"destinations\\\", \\\"in\\\", \\\"southern\\\", \\\"California\\\", \\\"such\\\", \\\"as\\\", \\\"San\\\", \\\"Diego\\\", \\\"and\\\", \\\"Palm\\\", \\\"Springs\\\", \\\".\\\"], \\\"h\\\": [\\\"borrego valley airport\\\", \\\"Q3606044\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"borrego springs, california\\\", \\\"Q2049424\\\", [[9, 10, 11, 12]]]}, {\\\"tokens\\\": [\\\"Maria\\\", \\\"Cristina\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Balo\\\", \\\"-\\\", \\\"i\\\", \\\",\\\", \\\"Lanao\\\", \\\"del\\\", \\\"Norte\\\", \\\",\\\", \\\"and\\\", \\\"was\\\", \\\"the\\\", \\\"main\\\", \\\"airport\\\", \\\"of\\\", \\\"Iligan\\\", \\\"in\\\", \\\"the\\\", \\\"late\\\", \\\"1980s\\\", \\\".\\\"], \\\"h\\\": [\\\"maria cristina airport\\\", \\\"Q1031517\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"iligan\\\", \\\"Q285488\\\", [[21]]]}, {\\\"tokens\\\": [\\\"Ondangwa\\\", \\\"town\\\", \\\"has\\\", \\\"a\\\", \\\"population\\\", \\\"of\\\", \\\"36,800\\\", \\\"according\\\", \\\"to\\\", \\\"the\\\", \\\"2011\\\", \\\"census\\\", \\\"data\\\", \\\"and\\\", \\\"has\\\", \\\"a\\\", \\\"small\\\", \\\"airport\\\", \\\"serviced\\\", \\\"by\\\", \\\"two\\\", \\\"daily\\\", \\\"Air\\\", \\\"Namibia\\\", \\\"commercial\\\", \\\"flights\\\", \\\"from\\\", \\\"Windhoek\\\", \\\"\\\\u2019s\\\", \\\"Eros\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"eros airport\\\", \\\"Q1321635\\\", [[29, 30]]], \\\"t\\\": [\\\"windhoek\\\", \\\"Q3935\\\", [[27]]]}, {\\\"tokens\\\": [\\\"Despite\\\", \\\"his\\\", \\\"injury\\\", \\\",\\\", \\\"Cena\\\", \\\"attended\\\", \\\"the\\\", \\\"annual\\\", \\\"WWE\\\", \\\"'s\\\", \\\"\\\\\\\"\\\", \\\"Tribute\\\", \\\"to\\\", \\\"the\\\", \\\"Troops\\\", \\\"\\\\\\\"\\\", \\\"show\\\", \\\"filmed\\\", \\\"at\\\", \\\"Camp\\\", \\\"Speicher\\\", \\\"in\\\", \\\"Tikrit\\\", \\\",\\\", \\\"Iraq\\\", \\\"on\\\", \\\"December\\\", \\\"7\\\", \\\",\\\", \\\"and\\\", \\\"aired\\\", \\\"on\\\", \\\"December\\\", \\\"24\\\", \\\".\\\"], \\\"h\\\": [\\\"camp speicher\\\", \\\"Q5013269\\\", [[19, 20]]], \\\"t\\\": [\\\"tikrit\\\", \\\"Q165444\\\", [[22]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"mid-1951\\\", \\\",\\\", \\\"IMCO\\\", \\\"expanded\\\", \\\"to\\\", \\\"the\\\", \\\"Brady\\\", \\\",\\\", \\\"Texas\\\", \\\"area\\\", \\\",\\\", \\\"starting\\\", \\\"up\\\", \\\"Brady\\\", \\\"Aviation\\\", \\\"at\\\", \\\"Curtis\\\", \\\"Field\\\", \\\".\\\"], \\\"h\\\": [\\\"curtis field\\\", \\\"Q1656327\\\", [[17, 18]]], \\\"t\\\": [\\\"brady, texas\\\", \\\"Q981872\\\", [[7, 8, 9]]]}, {\\\"tokens\\\": [\\\"Every\\\", \\\"major\\\", \\\"form\\\", \\\"of\\\", \\\"transportation\\\", \\\"serves\\\", \\\"Long\\\", \\\"Island\\\", \\\",\\\", \\\"including\\\", \\\"three\\\", \\\"major\\\", \\\"airports\\\", \\\",\\\", \\\"railroads\\\", \\\"and\\\", \\\"subways\\\", \\\",\\\", \\\"and\\\", \\\"several\\\", \\\"major\\\", \\\"highways\\\", \\\".\\\"], \\\"h\\\": [\\\"airports\\\", \\\"Q937590\\\", [[12]]], \\\"t\\\": [\\\"long island\\\", \\\"Q18438\\\", [[6, 7]]]}, {\\\"tokens\\\": [\\\"While\\\", \\\"owned\\\", \\\"by\\\", \\\"Jenista\\\", \\\"the\\\", \\\"aircraft\\\", \\\"was\\\", \\\"destroyed\\\", \\\"in\\\", \\\"an\\\", \\\"accident\\\", \\\"on\\\", \\\"11\\\", \\\"June\\\", \\\"1994\\\", \\\"at\\\", \\\"the\\\", \\\"Jean\\\", \\\"Airport\\\", \\\"in\\\", \\\"Jean\\\", \\\",\\\", \\\"Nevada\\\", \\\".\\\"], \\\"h\\\": [\\\"jean airport\\\", \\\"Q2901394\\\", [[17, 18]]], \\\"t\\\": [\\\"jean, nevada\\\", \\\"Q3709757\\\", [[20, 21, 22]]]}, {\\\"tokens\\\": [\\\"Like\\\", \\\"the\\\", \\\"rest\\\", \\\"of\\\", \\\"the\\\", \\\"island\\\", \\\"of\\\", \\\"Trinidad\\\", \\\",\\\", \\\"Port\\\", \\\"of\\\", \\\"Spain\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"the\\\", \\\"Piarco\\\", \\\"International\\\", \\\"Airport\\\", \\\"located\\\", \\\"in\\\", \\\"Piarco\\\", \\\",\\\", \\\"approximately\\\", \\\"east\\\", \\\"of\\\", \\\"Port\\\", \\\"of\\\", \\\"Spain\\\", \\\".\\\"], \\\"h\\\": [\\\"piarco international airport\\\", \\\"Q788810\\\", [[16, 17, 18]]], \\\"t\\\": [\\\"port of spain\\\", \\\"Q39178\\\", [[9, 10, 11], [26, 27, 28]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"commercial\\\", \\\"airline\\\", \\\"airports\\\", \\\"are\\\", \\\"Alpena\\\", \\\"County\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"and\\\", \\\"Cherry\\\", \\\"Capital\\\", \\\"Airport\\\", \\\"(\\\", \\\"Traverse\\\", \\\"City\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"cherry capital airport\\\", \\\"Q1433080\\\", [[11, 12, 13]]], \\\"t\\\": [\\\"traverse city\\\", \\\"Q984544\\\", [[15, 16]]]}, {\\\"tokens\\\": [\\\"General\\\", \\\"aviation\\\", \\\"airports\\\", \\\"include\\\", \\\"Camarillo\\\", \\\"Airport\\\", \\\",\\\", \\\"approximately\\\", \\\"west\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\";\\\", \\\"Oxnard\\\", \\\"Airport\\\", \\\",\\\", \\\"approximately\\\", \\\"west\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\"in\\\", \\\"Oxnard\\\", \\\",\\\", \\\"California\\\", \\\";\\\", \\\"and\\\", \\\"Van\\\", \\\"Nuys\\\", \\\"Airport\\\", \\\",\\\", \\\"east\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"oxnard airport\\\", \\\"Q7115707\\\", [[13, 14]]], \\\"t\\\": [\\\"oxnard, california\\\", \\\"Q209338\\\", [[22, 23, 24]]]}, {\\\"tokens\\\": [\\\"AAI\\\", \\\"had\\\", \\\"earlier\\\", \\\"estimated\\\", \\\"a\\\", \\\"requirement\\\", \\\"of\\\", \\\"600\\\", \\\"acres\\\", \\\"of\\\", \\\"land\\\", \\\"for\\\", \\\"the\\\", \\\"first\\\", \\\"Phase\\\", \\\"and\\\", \\\"another\\\", \\\"790\\\", \\\"acres\\\", \\\"for\\\", \\\"the\\\", \\\"second\\\", \\\"Phase\\\", \\\"in\\\", \\\"lieu\\\", \\\"of\\\", \\\"the\\\", \\\"existing\\\", \\\"Jay\\\", \\\"Prakash\\\", \\\"Narayan\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Patna\\\", \\\".\\\"], \\\"h\\\": [\\\"jay prakash narayan international airport\\\", \\\"Q2673010\\\", [[28, 29, 30, 31, 32]]], \\\"t\\\": [\\\"patna\\\", \\\"Q80484\\\", [[34]]]}, {\\\"tokens\\\": [\\\"Pune\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\"IATA\\\", \\\":\\\", \\\"PNQ\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"civil\\\", \\\"enclave\\\", \\\"located\\\", \\\"at\\\", \\\"Lohegaon\\\", \\\"Air\\\", \\\"Base\\\", \\\",\\\", \\\"northeast\\\", \\\"of\\\", \\\"Pune\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"pnq\\\", \\\"Q1432525\\\", [[6]]], \\\"t\\\": [\\\"pune\\\", \\\"Q1538\\\", [[0], [20]]]}, {\\\"tokens\\\": [\\\"Presently\\\", \\\",\\\", \\\"the\\\", \\\"airport\\\", \\\"serving\\\", \\\"Araraquara\\\", \\\",\\\", \\\"Brazil\\\", \\\"is\\\", \\\"named\\\", \\\"Bartolomeu\\\", \\\"de\\\", \\\"Gusm\\\\u00e3o\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"bartolomeu de gusm\\\\u00e3o airport\\\", \\\"Q4784257\\\", [[10, 11, 12, 13]]], \\\"t\\\": [\\\"araraquara\\\", \\\"Q626247\\\", [[5]]]}, {\\\"tokens\\\": [\\\"Phu\\\", \\\"Bai\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"the\\\", \\\"largest\\\", \\\"domestic\\\", \\\"airport\\\", \\\"in\\\", \\\"terms\\\", \\\"of\\\", \\\"passengers\\\", \\\"per\\\", \\\"year\\\", \\\"is\\\", \\\"situated\\\", \\\"15\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\"south\\\", \\\"of\\\", \\\"Hu\\\\u1ebf\\\", \\\".\\\"], \\\"h\\\": [\\\"phu bai international airport\\\", \\\"Q160094\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"hu\\\\u1ebf\\\", \\\"Q36167\\\", [[22]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"the\\\", \\\"1970s\\\", \\\",\\\", \\\"the\\\", \\\"original\\\", \\\"airport\\\", \\\"in\\\", \\\"Taipei\\\", \\\"City\\\", \\\"\\\\u2014\\\", \\\"Taipei\\\", \\\"Songshan\\\", \\\"Airport\\\", \\\"\\\\u2014\\\", \\\"had\\\", \\\"become\\\", \\\"overcrowded\\\", \\\"and\\\", \\\"could\\\", \\\"not\\\", \\\"be\\\", \\\"expanded\\\", \\\"due\\\", \\\"to\\\", \\\"space\\\", \\\"limitations\\\", \\\".\\\"], \\\"h\\\": [\\\"taipei songshan airport\\\", \\\"Q702019\\\", [[11, 12, 13]]], \\\"t\\\": [\\\"taipei city\\\", \\\"Q1867\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Mid\\\", \\\"-\\\", \\\"America\\\", \\\"Air\\\", \\\"Museum\\\", \\\"is\\\", \\\"in\\\", \\\"southwest\\\", \\\"Kansas\\\", \\\",\\\", \\\"in\\\", \\\"Liberal\\\", \\\",\\\", \\\"Kansas\\\", \\\",\\\", \\\"at\\\", \\\"the\\\", \\\"Liberal\\\", \\\"Mid\\\", \\\"-\\\", \\\"America\\\", \\\"Regional\\\", \\\"Airport\\\", \\\",\\\", \\\"near\\\", \\\"U.S.\\\", \\\"Highway\\\", \\\"54\\\", \\\".\\\"], \\\"h\\\": [\\\"liberal mid-america regional airport\\\", \\\"Q6540690\\\", [[18, 19, 20, 21, 22, 23]]], \\\"t\\\": [\\\"liberal, kansas\\\", \\\"Q1003630\\\", [[12, 13, 14]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"broadcasts\\\", \\\"from\\\", \\\"the\\\", \\\"former\\\", \\\"KDLH\\\", \\\"tower\\\", \\\"on\\\", \\\"Duluth\\\", \\\"'s\\\", \\\"Observation\\\", \\\"Hill\\\", \\\".\\\"], \\\"h\\\": [\\\"kdlh\\\", \\\"Q3277758\\\", [[5]]], \\\"t\\\": [\\\"duluth\\\", \\\"Q485708\\\", [[8]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"closest\\\", \\\"airports\\\", \\\"are\\\", \\\"Chandigarh\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"located\\\", \\\"away\\\", \\\",\\\", \\\"and\\\", \\\"Sri\\\", \\\"Guru\\\", \\\"Ram\\\", \\\"Dass\\\", \\\"Jee\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"away\\\", \\\"in\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Amritsar\\\", \\\".\\\"], \\\"h\\\": [\\\"sri guru ram dass jee international airport\\\", \\\"Q385356\\\", [[12, 13, 14, 15, 16, 17, 18]]], \\\"t\\\": [\\\"amritsar\\\", \\\"Q48403\\\", [[25]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"A-23\\\", \\\"Arusha\\\", \\\"-\\\", \\\"Himo\\\", \\\"road\\\", \\\"runs\\\", \\\"east\\\", \\\"-\\\", \\\"west\\\", \\\"and\\\", \\\"enters\\\", \\\"the\\\", \\\"region\\\", \\\"near\\\", \\\"Kilimanjaro\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"kilimanjaro international airport\\\", \\\"Q1365099\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"arusha\\\", \\\"Q4301\\\", [[2]]]}, {\\\"tokens\\\": [\\\"Taravella\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"C\\\\u00f3rdoba\\\", \\\",\\\", \\\"to\\\", \\\"General\\\", \\\"Enrique\\\", \\\"Mosconi\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Comodoro\\\", \\\"Rivadavia\\\", \\\",\\\", \\\"with\\\", \\\"stopovers\\\", \\\"at\\\", \\\"Governor\\\", \\\"Francisco\\\", \\\"Gabrielli\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Mendoza\\\", \\\",\\\", \\\"and\\\", \\\"Presidente\\\", \\\"Per\\\\u00f3n\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Neuqu\\\\u00e9n\\\", \\\".\\\"], \\\"h\\\": [\\\"governor francisco gabrielli international airport\\\", \\\"Q1432029\\\", [[19, 20, 21, 22, 23]]], \\\"t\\\": [\\\"mendoza\\\", \\\"Q44237\\\", [[25]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"London\\\", \\\"qualifying\\\", \\\"competition\\\", \\\",\\\", \\\"the\\\", \\\"British\\\", \\\"Open\\\", \\\",\\\", \\\"was\\\", \\\"held\\\", \\\"August\\\", \\\"2011\\\", \\\"in\\\", \\\"Heathrow\\\", \\\"at\\\", \\\"Stoke\\\", \\\"Mandeville\\\", \\\",\\\", \\\"with\\\", \\\"Rudio\\\", \\\"competing\\\", \\\"to\\\", \\\"try\\\", \\\"to\\\", \\\"earn\\\", \\\"Spain\\\", \\\"one\\\", \\\"of\\\", \\\"the\\\", \\\"twenty\\\", \\\"qualifying\\\", \\\"sports\\\", \\\"on\\\", \\\"offer\\\", \\\".\\\"], \\\"h\\\": [\\\"heathrow\\\", \\\"Q8691\\\", [[14]]], \\\"t\\\": [\\\"london\\\", \\\"Q84\\\", [[1]]]}, {\\\"tokens\\\": [\\\"Breeder\\\", \\\"George\\\", \\\"Brunacini\\\", \\\"was\\\", \\\"notably\\\", \\\"killed\\\", \\\"in\\\", \\\"the\\\", \\\"August\\\", \\\"27\\\", \\\",\\\", \\\"2006\\\", \\\",\\\", \\\"crash\\\", \\\"of\\\", \\\"Comair\\\", \\\"Flight\\\", \\\"5191\\\", \\\"at\\\", \\\"Blue\\\", \\\"Grass\\\", \\\"Airport\\\", \\\"in\\\", \\\"Lexington\\\", \\\",\\\", \\\"Kentucky\\\", \\\".\\\"], \\\"h\\\": [\\\"blue grass airport\\\", \\\"Q598259\\\", [[19, 20, 21]]], \\\"t\\\": [\\\"lexington, kentucky\\\", \\\"Q49241\\\", [[23, 24, 25]]]}, {\\\"tokens\\\": [\\\"Aeroflot\\\", \\\"Flight\\\", \\\"498\\\", \\\"was\\\", \\\"originally\\\", \\\"scheduled\\\", \\\"to\\\", \\\"fly\\\", \\\"from\\\", \\\"Severomuysk\\\", \\\"to\\\", \\\"Baikal\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Ulan\\\", \\\"-\\\", \\\"Ude\\\", \\\",\\\", \\\"with\\\", \\\"a\\\", \\\"planned\\\", \\\"en\\\", \\\"-\\\", \\\"route\\\", \\\"stop\\\", \\\"at\\\", \\\"Nizhneangarsk\\\", \\\"Airport\\\", \\\"in\\\", \\\"Nizhneangarsk\\\", \\\".\\\"], \\\"h\\\": [\\\"baikal international airport\\\", \\\"Q2719346\\\", [[11, 12, 13]]], \\\"t\\\": [\\\"ulan-ude\\\", \\\"Q6816\\\", [[15, 16, 17]]]}, {\\\"tokens\\\": [\\\"Kbely\\\", \\\"Airport\\\", \\\"was\\\", \\\"built\\\", \\\"in\\\", \\\"1918\\\", \\\"and\\\", \\\"was\\\", \\\"Prague\\\", \\\"'s\\\", \\\"only\\\", \\\"airport\\\", \\\"until\\\", \\\"the\\\", \\\"construction\\\", \\\"of\\\", \\\"Ruzyn\\\\u011b\\\", \\\"Airport\\\", \\\"in\\\", \\\"1937\\\", \\\",\\\", \\\"on\\\", \\\"the\\\", \\\"northwest\\\", \\\"side\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"kbely airport\\\", \\\"Q1935013\\\", [[0, 1]]], \\\"t\\\": [\\\"prague\\\", \\\"Q1085\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Bikini\\\", \\\"Atoll\\\", \\\"Airport\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"Enyu\\\", \\\"Airfield\\\", \\\",\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"use\\\", \\\"airstrip\\\", \\\"at\\\", \\\"Enyu\\\", \\\"on\\\", \\\"Bikini\\\", \\\"Atoll\\\", \\\",\\\", \\\"Marshall\\\", \\\"Islands\\\", \\\".\\\"], \\\"h\\\": [\\\"enyu airfield\\\", \\\"Q598311\\\", [[7, 8]]], \\\"t\\\": [\\\"bikini atoll\\\", \\\"Q152225\\\", [[0, 1], [18, 19]]]}, {\\\"tokens\\\": [\\\"Retrieved\\\", \\\"on\\\", \\\"January\\\", \\\"26\\\", \\\",\\\", \\\"2011\\\", \\\".\\\", \\\"operating\\\", \\\"as\\\", \\\"Aerol\\\\u00ednea\\\", \\\"de\\\", \\\"Antioquia\\\", \\\"(\\\", \\\"ADA\\\", \\\")\\\", \\\",\\\", \\\"is\\\", \\\"a\\\", \\\"regional\\\", \\\"airline\\\", \\\"with\\\", \\\"its\\\", \\\"headquarters\\\", \\\"on\\\", \\\"the\\\", \\\"property\\\", \\\"of\\\", \\\"Olaya\\\", \\\"Herrera\\\", \\\"Airport\\\", \\\"in\\\", \\\"Medell\\\\u00edn\\\", \\\",\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"olaya herrera airport\\\", \\\"Q1431257\\\", [[27, 28, 29]]], \\\"t\\\": [\\\"medell\\\\u00edn\\\", \\\"Q48278\\\", [[31]]]}, {\\\"tokens\\\": [\\\"Littlefield\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Lamb\\\", \\\"County\\\", \\\",\\\", \\\"three\\\", \\\"nautical\\\", \\\"miles\\\", \\\"(\\\", \\\"6\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"west\\\", \\\"of\\\", \\\"the\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\"of\\\", \\\"Littlefield\\\", \\\",\\\", \\\"Texas\\\", \\\".\\\"], \\\"h\\\": [\\\"littlefield municipal airport\\\", \\\"Q6652959\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"littlefield, texas\\\", \\\"Q202736\\\", [[24, 25, 26]]]}, {\\\"tokens\\\": [\\\"Capit\\\\u00e1n\\\", \\\"Germ\\\\u00e1n\\\", \\\"Quiroga\\\", \\\"Guardia\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"San\\\", \\\"Borja\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Beni\\\", \\\"Department\\\", \\\"of\\\", \\\"Bolivia\\\", \\\".\\\"], \\\"h\\\": [\\\"capit\\\\u00e1n germ\\\\u00e1n quiroga guardia airport\\\", \\\"Q2875720\\\", [[0, 1, 2, 3, 4]]], \\\"t\\\": [\\\"san borja\\\", \\\"Q2307472\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"Moses\\\", \\\"Point\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"Elim\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"the\\\", \\\"Nome\\\", \\\"Census\\\", \\\"Area\\\", \\\"of\\\", \\\"the\\\", \\\"U.S.\\\", \\\"state\\\", \\\"of\\\", \\\"Alaska\\\", \\\".\\\"], \\\"h\\\": [\\\"moses point airport\\\", \\\"Q3886700\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"elim\\\", \\\"Q79557\\\", [[8]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"under\\\", \\\"the\\\", \\\"administration\\\", \\\"of\\\", \\\"Haixi\\\", \\\"Mongol\\\", \\\"and\\\", \\\"Tibetan\\\", \\\"Autonomous\\\", \\\"Prefecture\\\", \\\".The\\\", \\\"Huatugou\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Mangnai\\\", \\\".\\\"], \\\"h\\\": [\\\"huatugou airport\\\", \\\"Q3207552\\\", [[13, 14]]], \\\"t\\\": [\\\"mangnai\\\", \\\"Q1201941\\\", [[18]]]}, {\\\"tokens\\\": [\\\"Kulob\\\", \\\"Airport\\\", \\\"or\\\", \\\"Kulyab\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Kulob\\\", \\\"(\\\", \\\"also\\\", \\\"spelled\\\", \\\"Kulyab\\\", \\\")\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"the\\\", \\\"Khatlon\\\", \\\"province\\\", \\\"in\\\", \\\"Tajikistan\\\", \\\".\\\"], \\\"h\\\": [\\\"kulyab airport\\\", \\\"Q2231909\\\", [[3, 4]]], \\\"t\\\": [\\\"kulob\\\", \\\"Q132043\\\", [[0], [9]]]}, {\\\"tokens\\\": [\\\"Most\\\", \\\"trains\\\", \\\"from\\\", \\\"the\\\", \\\"Gold\\\", \\\"Coast\\\", \\\"run\\\", \\\"through\\\", \\\"to\\\", \\\"Brisbane\\\", \\\"Airport\\\", \\\",\\\", \\\"allowing\\\", \\\"tourists\\\", \\\"and\\\", \\\"locals\\\", \\\"access\\\", \\\"to\\\", \\\"more\\\", \\\"international\\\", \\\"destinations\\\", \\\"than\\\", \\\"from\\\", \\\"the\\\", \\\"Gold\\\", \\\"Coast\\\", \\\"'s\\\", \\\"own\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"own airport\\\", \\\"Q1175431\\\", [[27, 28]]], \\\"t\\\": [\\\"gold coast\\\", \\\"Q140075\\\", [[4, 5], [24, 25]]]}, {\\\"tokens\\\": [\\\"Soledad\\\", \\\"International\\\", \\\"Airport\\\", \\\"was\\\", \\\"the\\\", \\\"main\\\", \\\"airport\\\", \\\"of\\\", \\\"Barranquilla\\\", \\\",\\\", \\\"Colombia\\\", \\\"from\\\", \\\"1936\\\", \\\"to\\\", \\\"1981\\\", \\\"when\\\", \\\"it\\\", \\\"was\\\", \\\"replaced\\\", \\\"by\\\", \\\"Ernesto\\\", \\\"Cortissoz\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"ernesto cortissoz international airport\\\", \\\"Q645151\\\", [[20, 21, 22, 23]]], \\\"t\\\": [\\\"barranquilla\\\", \\\"Q62823\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Hubs\\\", \\\"of\\\", \\\"Panalpina\\\", \\\"are\\\", \\\"situated\\\", \\\"in\\\", \\\"Luxembourg\\\", \\\",\\\", \\\"at\\\", \\\"Findel\\\", \\\"Airport\\\", \\\",\\\", \\\"Prague\\\", \\\"and\\\", \\\"in\\\", \\\"Huntsville\\\", \\\",\\\", \\\"Alabama\\\", \\\",\\\", \\\"at\\\", \\\"Huntsville\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"huntsville international airport\\\", \\\"Q2213419\\\", [[20, 21, 22]]], \\\"t\\\": [\\\"huntsville, alabama\\\", \\\"Q79860\\\", [[15, 16, 17]]]}, {\\\"tokens\\\": [\\\"Maota\\\", \\\"Airport\\\", \\\"is\\\", \\\"the\\\", \\\"main\\\", \\\"airfield\\\", \\\"on\\\", \\\"the\\\", \\\"island\\\", \\\",\\\", \\\"located\\\", \\\"10\\\", \\\"minutes\\\", \\\"south\\\", \\\"of\\\", \\\"Salelologa\\\", \\\".\\\"], \\\"h\\\": [\\\"maota airport\\\", \\\"Q1030546\\\", [[0, 1]]], \\\"t\\\": [\\\"salelologa\\\", \\\"Q2214151\\\", [[15]]]}, {\\\"tokens\\\": [\\\"This\\\", \\\"new\\\", \\\"airport\\\", \\\"for\\\", \\\"West\\\", \\\"Java\\\", \\\"is\\\", \\\"set\\\", \\\"to\\\", \\\"replace\\\", \\\"the\\\", \\\"current\\\", \\\"airport\\\", \\\"in\\\", \\\"Bandung\\\", \\\",\\\", \\\"and\\\", \\\"is\\\", \\\"named\\\", \\\"\\\\\\\"\\\", \\\"Kertajati\\\", \\\"International\\\", \\\"Airport\\\", \\\"\\\\\\\"\\\", \\\".\\\"], \\\"h\\\": [\\\"kertajati international airport\\\", \\\"Q889070\\\", [[20, 21, 22]]], \\\"t\\\": [\\\"west java\\\", \\\"Q3724\\\", [[4, 5]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"2018\\\", \\\",\\\", \\\"Commercial\\\", \\\"Flight\\\", \\\"Again\\\", \\\"Started\\\", \\\"at\\\", \\\"Sonari\\\", \\\"Airport\\\", \\\"In\\\", \\\"Jamshedpur\\\", \\\".\\\"], \\\"h\\\": [\\\"sonari airport\\\", \\\"Q7560814\\\", [[8, 9]]], \\\"t\\\": [\\\"jamshedpur\\\", \\\"Q200054\\\", [[11]]]}, {\\\"tokens\\\": [\\\"Parna\\\\u00edba\\\", \\\"has\\\", \\\"an\\\", \\\"international\\\", \\\"airport\\\", \\\"with\\\", \\\"a\\\", \\\"runway\\\", \\\"of\\\", \\\"2500\\\", \\\"m\\\", \\\".\\\"], \\\"h\\\": [\\\"an international airport\\\", \\\"Q6587028\\\", [[2, 3, 4]]], \\\"t\\\": [\\\"parna\\\\u00edba\\\", \\\"Q1643864\\\", [[0]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"was\\\", \\\"further\\\", \\\"planned\\\", \\\"to\\\", \\\"fly\\\", \\\"them\\\", \\\"to\\\", \\\"Copenhagen\\\", \\\"from\\\", \\\"Damascus\\\", \\\"'s\\\", \\\"international\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"international airport\\\", \\\"Q570873\\\", [[12, 13]]], \\\"t\\\": [\\\"damascus\\\", \\\"Q3766\\\", [[10]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"district\\\", \\\"comprises\\\", \\\"Tob\\\\u00edas\\\", \\\"Bola\\\\u00f1os\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"San\\\", \\\"Jos\\\\u00e9\\\", \\\"'s\\\", \\\"domestic\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"tob\\\\u00edas bola\\\\u00f1os international airport\\\", \\\"Q3500191\\\", [[3, 4, 5, 6]]], \\\"t\\\": [\\\"san jos\\\\u00e9\\\", \\\"Q3070\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"Stands\\\", \\\"were\\\", \\\"specially\\\", \\\"erected\\\", \\\"for\\\", \\\"him\\\", \\\"at\\\", \\\"Luis\\\", \\\"Mu\\\\u00f1oz\\\", \\\"Mar\\\\u00edn\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"San\\\", \\\"Juan\\\", \\\",\\\", \\\"where\\\", \\\"he\\\", \\\"met\\\", \\\"with\\\", \\\"governor\\\", \\\"Carlos\\\", \\\"Romero\\\", \\\"Barcel\\\\u00f3\\\", \\\",\\\", \\\"and\\\", \\\"at\\\", \\\"Plaza\\\", \\\"Las\\\", \\\"Americas\\\", \\\".\\\"], \\\"h\\\": [\\\"luis mu\\\\u00f1oz mar\\\\u00edn international airport\\\", \\\"Q1360523\\\", [[7, 8, 9, 10, 11]]], \\\"t\\\": [\\\"san juan\\\", \\\"Q41211\\\", [[13, 14]]]}, {\\\"tokens\\\": [\\\"Monterrey\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"(\\\", \\\")\\\", \\\";\\\", \\\"ceremonial\\\", \\\"name\\\", \\\"General\\\", \\\"Mariano\\\", \\\"Escobedo\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"international\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"Apodaca\\\", \\\",\\\", \\\"Nuevo\\\", \\\"Le\\\\u00f3n\\\", \\\",\\\", \\\"Mexico\\\", \\\".\\\"], \\\"h\\\": [\\\"general mariano escobedo international airport\\\", \\\"Q767660\\\", [[9, 10, 11, 12, 13]]], \\\"t\\\": [\\\"monterrey\\\", \\\"Q81033\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Msalato\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"proposed\\\", \\\"international\\\", \\\"airport\\\", \\\"intended\\\", \\\"to\\\", \\\"serve\\\", \\\"the\\\", \\\"Tanzanian\\\", \\\"capital\\\", \\\"of\\\", \\\"Dodoma\\\", \\\".\\\"], \\\"h\\\": [\\\"msalato international airport\\\", \\\"Q16895494\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"dodoma\\\", \\\"Q3866\\\", [[17]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"aircraft\\\", \\\"involved\\\", \\\",\\\", \\\"an\\\", \\\"Antonov\\\", \\\"An-24\\\", \\\",\\\", \\\"was\\\", \\\"operating\\\", \\\"Angara\\\", \\\"Airlines\\\", \\\"'\\\", \\\"scheduled\\\", \\\"domestic\\\", \\\"service\\\", \\\"from\\\", \\\"Bogashevo\\\", \\\"Airport\\\", \\\",\\\", \\\"Tomsk\\\", \\\"to\\\", \\\"Surgut\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Surgut\\\", \\\".\\\"], \\\"h\\\": [\\\"bogashevo airport\\\", \\\"Q1322435\\\", [[17, 18]]], \\\"t\\\": [\\\"tomsk\\\", \\\"Q976\\\", [[20]]]}, {\\\"tokens\\\": [\\\"(\\\", \\\"IATA\\\", \\\"assigned\\\", \\\"PJC\\\", \\\"to\\\", \\\"Pedro\\\", \\\"Juan\\\", \\\"Caballero\\\", \\\"Airport\\\", \\\"in\\\", \\\"Pedro\\\", \\\"Juan\\\", \\\"Caballero\\\", \\\",\\\", \\\"Paraguay\\\", \\\".\\\"], \\\"h\\\": [\\\"pedro juan caballero airport\\\", \\\"Q1657937\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"pedro juan caballero, paraguay\\\", \\\"Q849292\\\", [[10, 11, 12, 13, 14]]]}, {\\\"tokens\\\": [\\\"This\\\", \\\"is\\\", \\\"approximately\\\", \\\",\\\", \\\"by\\\", \\\"air\\\", \\\",\\\", \\\"northeast\\\", \\\"of\\\", \\\"Jomo\\\", \\\"Kenyatta\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Nairobi\\\", \\\",\\\", \\\"the\\\", \\\"largest\\\", \\\"civilian\\\", \\\"airport\\\", \\\"in\\\", \\\"the\\\", \\\"country\\\", \\\".\\\"], \\\"h\\\": [\\\"jomo kenyatta international airport\\\", \\\"Q206349\\\", [[9, 10, 11, 12]]], \\\"t\\\": [\\\"nairobi\\\", \\\"Q3870\\\", [[14]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"San\\\", \\\"Pedro\\\", \\\"Sula\\\", \\\"in\\\", \\\"northwestern\\\", \\\"Honduras\\\", \\\",\\\", \\\"flooding\\\", \\\"covered\\\", \\\"several\\\", \\\"neighborhoods\\\", \\\"and\\\", \\\"the\\\", \\\"international\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"international airport\\\", \\\"Q2308399\\\", [[14, 15]]], \\\"t\\\": [\\\"san pedro sula\\\", \\\"Q274584\\\", [[1, 2, 3]]]}, {\\\"tokens\\\": [\\\"Hill\\\", \\\"had\\\", \\\"left\\\", \\\"his\\\", \\\"luggage\\\", \\\"at\\\", \\\"Lee\\\", \\\"Bird\\\", \\\"Field\\\", \\\"Airport\\\", \\\"in\\\", \\\"North\\\", \\\"Platte\\\", \\\",\\\", \\\"Nebraska\\\", \\\",\\\", \\\"containing\\\", \\\"drug\\\", \\\"paraphernalia\\\", \\\",\\\", \\\"glass\\\", \\\"tubes\\\", \\\"with\\\", \\\"cocaine\\\", \\\"and\\\", \\\"methamphetamine\\\", \\\"residue\\\", \\\".\\\"], \\\"h\\\": [\\\"lee bird field\\\", \\\"Q7056358\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"north platte, nebraska\\\", \\\"Q989960\\\", [[11, 12, 13, 14]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"1000\\\", \\\"hectare\\\", \\\"(\\\", \\\"2,472\\\", \\\"acres\\\", \\\")\\\", \\\"site\\\", \\\"is\\\", \\\"located\\\", \\\"12\\\", \\\"kilometers\\\", \\\"from\\\", \\\"Cartagena\\\", \\\"\\\\u2019s\\\", \\\"historic\\\", \\\"old\\\", \\\"city\\\", \\\"and\\\", \\\"8\\\", \\\"kilometers\\\", \\\"from\\\", \\\"Rafael\\\", \\\"N\\\\u00fa\\\\u00f1ez\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"rafael n\\\\u00fa\\\\u00f1ez international airport\\\", \\\"Q2670003\\\", [[22, 23, 24, 25]]], \\\"t\\\": [\\\"cartagena\\\", \\\"Q657461\\\", [[13]]]}, {\\\"tokens\\\": [\\\"Retrieved\\\", \\\"2007\\\", \\\"-\\\", \\\"07\\\", \\\"-\\\", \\\"22\\\", \\\".\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"Easton\\\", \\\"/\\\", \\\"Newnam\\\", \\\"Field\\\", \\\",\\\", \\\"ESN\\\", \\\"-\\\", \\\"Easton\\\", \\\"/\\\", \\\"Newnam\\\", \\\"Field\\\", \\\"at\\\", \\\"Maryland\\\", \\\"Aviation\\\", \\\"Authority\\\", \\\".\\\"], \\\"h\\\": [\\\"newnam field\\\", \\\"Q5330836\\\", [[13, 14], [20, 21]]], \\\"t\\\": [\\\"easton\\\", \\\"Q754306\\\", [[11], [18]]]}, {\\\"tokens\\\": [\\\"Altman\\\", \\\"was\\\", \\\"given\\\", \\\"clearance\\\", \\\"from\\\", \\\"the\\\", \\\"tower\\\", \\\"at\\\", \\\"Teterboro\\\", \\\"Airport\\\", \\\"in\\\", \\\"Teterboro\\\", \\\",\\\", \\\"New\\\", \\\"Jersey\\\", \\\"at\\\", \\\"11:48\\\", \\\"\\\\u00a0\\\", \\\"a.m.\\\", \\\"to\\\", \\\"take\\\", \\\"off\\\", \\\".\\\"], \\\"h\\\": [\\\"teterboro airport\\\", \\\"Q1433053\\\", [[8, 9]]], \\\"t\\\": [\\\"teterboro, new jersey\\\", \\\"Q936782\\\", [[11, 12, 13, 14]]]}, {\\\"tokens\\\": [\\\"Juan\\\", \\\"Enrique\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"west\\\", \\\"-\\\", \\\"southwest\\\", \\\"of\\\", \\\"Paine\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"the\\\", \\\"Santiago\\\", \\\"Metropolitan\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"juan enrique airport\\\", \\\"Q16896327\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"paine\\\", \\\"Q51070\\\", [[11]]]}, {\\\"tokens\\\": [\\\"Burnie\\\", \\\"Airport\\\", \\\",\\\", \\\"also\\\", \\\"called\\\", \\\"Burnie\\\", \\\"Wynyard\\\", \\\"Airport\\\", \\\"or\\\", \\\"Wynyard\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"a\\\", \\\"regional\\\", \\\"airport\\\", \\\"located\\\", \\\"adjacent\\\", \\\"to\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"Wynyard\\\", \\\",\\\", \\\"about\\\", \\\"west\\\", \\\"from\\\", \\\"Burnie\\\", \\\",\\\", \\\"Tasmania\\\", \\\",\\\", \\\"Australia\\\", \\\".\\\"], \\\"h\\\": [\\\"wynyard airport\\\", \\\"Q15540\\\", [[6, 7], [9, 10]]], \\\"t\\\": [\\\"burnie\\\", \\\"Q175262\\\", [[0], [5], [27]]]}, {\\\"tokens\\\": [\\\"Tirana\\\", \\\"International\\\", \\\"Airport\\\", \\\"N\\\\u00ebn\\\\u00eb\\\", \\\"Tereza\\\", \\\"(\\\", \\\",\\\", \\\")\\\", \\\",\\\", \\\"commonly\\\", \\\"Rinas\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"Albania\\\", \\\"'s\\\", \\\"main\\\", \\\"international\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"rinas international airport\\\", \\\"Q217226\\\", [[10, 11, 12]]], \\\"t\\\": [\\\"tirana\\\", \\\"Q19689\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Currently\\\", \\\",\\\", \\\"Rach\\\", \\\"Gia\\\", \\\"Airport\\\", \\\"is\\\", \\\"the\\\", \\\"biggest\\\", \\\"airport\\\", \\\"in\\\", \\\"R\\\\u1ea1ch\\\", \\\"Gi\\\\u00e1\\\", \\\".\\\"], \\\"h\\\": [\\\"rach gia airport\\\", \\\"Q1993204\\\", [[2, 3, 4]]], \\\"t\\\": [\\\"r\\\\u1ea1ch gi\\\\u00e1\\\", \\\"Q36093\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"\\\\\\\"\\\", \\\"Head\\\", \\\"Office\\\", \\\":\\\", \\\"Aerogem\\\", \\\"Aviation\\\", \\\"Ltd\\\", \\\"1\\\", \\\"Gemini\\\", \\\"Airlines\\\", \\\"Building\\\", \\\",\\\", \\\"Old\\\", \\\"Cargo\\\", \\\"Village\\\", \\\",\\\", \\\"Kotoka\\\", \\\"International\\\", \\\"Airport\\\", \\\"Accra\\\", \\\"\\\\\\\"\\\", \\\"It\\\", \\\"operates\\\", \\\"worldwide\\\", \\\"non\\\", \\\"-\\\", \\\"scheduled\\\", \\\"cargo\\\", \\\"flights\\\", \\\".\\\"], \\\"h\\\": [\\\"kotoka international airport\\\", \\\"Q177689\\\", [[16, 17, 18]]], \\\"t\\\": [\\\"accra\\\", \\\"Q3761\\\", [[19]]]}, {\\\"tokens\\\": [\\\"Madurai\\\", \\\"international\\\", \\\"Airport\\\", \\\"(\\\", \\\"IATA\\\", \\\":\\\", \\\"IXM\\\", \\\",\\\", \\\"ICAO\\\", \\\":\\\", \\\"VOMD\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"customs\\\", \\\"airport\\\", \\\"serving\\\", \\\"Madurai\\\", \\\"in\\\", \\\"the\\\", \\\"state\\\", \\\"of\\\", \\\"Tamil\\\", \\\"Nadu\\\", \\\".\\\"], \\\"h\\\": [\\\"vomd\\\", \\\"Q3465662\\\", [[10]]], \\\"t\\\": [\\\"madurai\\\", \\\"Q228405\\\", [[0], [17]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"base\\\", \\\"is\\\", \\\"Ford\\\", \\\"Airport\\\", \\\"in\\\", \\\"Iron\\\", \\\"Mountain\\\", \\\",\\\", \\\"Michigan\\\", \\\"and\\\", \\\"its\\\", \\\"air\\\", \\\"traffic\\\", \\\"control\\\", \\\"call\\\", \\\"sign\\\", \\\"Iron\\\", \\\"Air\\\", \\\"is\\\", \\\"derived\\\", \\\"from\\\", \\\"that\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"ford airport\\\", \\\"Q5467650\\\", [[4, 5]]], \\\"t\\\": [\\\"iron mountain, michigan\\\", \\\"Q567814\\\", [[7, 8, 9, 10]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"airports\\\", \\\"are\\\", \\\"at\\\", \\\"Poitiers\\\", \\\"(\\\", \\\"Poitiers\\\", \\\"-\\\", \\\"Biard\\\", \\\"Airport\\\", \\\")\\\", \\\"and\\\", \\\"Nantes\\\", \\\"(\\\", \\\"Nantes\\\", \\\"Atlantique\\\", \\\"Airport\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"biard airport\\\", \\\"Q1432405\\\", [[9, 10]]], \\\"t\\\": [\\\"poitiers\\\", \\\"Q6616\\\", [[5], [7]]]}, {\\\"tokens\\\": [\\\"Calhoun\\\", \\\"County\\\", \\\"Airport\\\", \\\",\\\", \\\"a\\\", \\\"general\\\", \\\"aviation\\\", \\\"airport\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"unincorporated\\\", \\\"Calhoun\\\", \\\"County\\\", \\\"northwest\\\", \\\"of\\\", \\\"Port\\\", \\\"Lavaca\\\", \\\".\\\"], \\\"h\\\": [\\\"calhoun county airport\\\", \\\"Q3813482\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"port lavaca\\\", \\\"Q982477\\\", [[17, 18]]]}, {\\\"tokens\\\": [\\\"Governador\\\", \\\"Aluizio\\\", \\\"Alves\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"the\\\", \\\"new\\\", \\\"airport\\\", \\\"that\\\", \\\"serves\\\", \\\"the\\\", \\\"metropolitan\\\", \\\"area\\\", \\\"of\\\", \\\"Natal\\\", \\\",\\\", \\\"was\\\", \\\"opened\\\", \\\"in\\\", \\\"2014\\\", \\\"and\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"municipality\\\", \\\".\\\"], \\\"h\\\": [\\\"governador aluizio alves international airport\\\", \\\"Q2090101\\\", [[0, 1, 2, 3, 4]]], \\\"t\\\": [\\\"natal\\\", \\\"Q131620\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Ordos\\\", \\\"Ejin\\\", \\\"Horo\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Ordos\\\", \\\"City\\\", \\\"in\\\", \\\"China\\\", \\\"'s\\\", \\\"Inner\\\", \\\"Mongolia\\\", \\\"Autonomous\\\", \\\"Region\\\", \\\".\\\"], \\\"h\\\": [\\\"ordos ejin horo airport\\\", \\\"Q3538450\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"ordos city\\\", \\\"Q570937\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"Rennell\\\", \\\"/\\\", \\\"Tingoa\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"Tigoa\\\", \\\"on\\\", \\\"Rennell\\\", \\\"Island\\\", \\\"in\\\", \\\"the\\\", \\\"Solomon\\\", \\\"Islands\\\", \\\".\\\"], \\\"h\\\": [\\\"tingoa airport\\\", \\\"Q3436133\\\", [[2, 3]]], \\\"t\\\": [\\\"tigoa\\\", \\\"Q987011\\\", [[8]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"subsequently\\\", \\\"became\\\", \\\"a\\\", \\\"non\\\", \\\"-\\\", \\\"flying\\\", \\\"general\\\", \\\"reserve\\\", \\\"squadron\\\", \\\"headquartered\\\", \\\"at\\\", \\\"RAAF\\\", \\\"Williams\\\", \\\"near\\\", \\\"Melbourne\\\", \\\".\\\"], \\\"h\\\": [\\\"raaf williams\\\", \\\"Q1551483\\\", [[12, 13]]], \\\"t\\\": [\\\"melbourne\\\", \\\"Q3141\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Nearby\\\", \\\"airports\\\", \\\"are\\\", \\\"San\\\", \\\"Pedro\\\", \\\"de\\\", \\\"Atacama\\\", \\\"Airport\\\", \\\"and\\\", \\\"Salar\\\", \\\"de\\\", \\\"Atacama\\\", \\\"Airport\\\", \\\"for\\\", \\\"private\\\", \\\"aircraft\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"larger\\\", \\\"El\\\", \\\"Loa\\\", \\\"Airport\\\", \\\"/\\\", \\\"Calama\\\", \\\"100\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\"away\\\", \\\"for\\\", \\\"scheduled\\\", \\\"aircraft\\\", \\\".\\\"], \\\"h\\\": [\\\"el loa airport\\\", \\\"Q3299637\\\", [[20, 21, 22]]], \\\"t\\\": [\\\"calama\\\", \\\"Q3685\\\", [[24]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"first\\\", \\\"community\\\", \\\"it\\\", \\\"enters\\\", \\\"is\\\", \\\"Grant\\\", \\\"-\\\", \\\"Valkaria\\\", \\\",\\\", \\\"with\\\", \\\"intersections\\\", \\\"with\\\", \\\"Micco\\\", \\\"Road\\\", \\\",\\\", \\\"followed\\\", \\\"by\\\", \\\"Valkaria\\\", \\\"Road\\\", \\\"just\\\", \\\"east\\\", \\\"of\\\", \\\"the\\\", \\\"Valkaria\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"valkaria airport\\\", \\\"Q7911753\\\", [[24, 25]]], \\\"t\\\": [\\\"grant-valkaria\\\", \\\"Q2154617\\\", [[6, 7, 8]]]}, {\\\"tokens\\\": [\\\"However\\\", \\\",\\\", \\\"the\\\", \\\"company\\\", \\\"'s\\\", \\\"contracts\\\", \\\"are\\\", \\\"managed\\\", \\\"from\\\", \\\"its\\\", \\\"office\\\", \\\"at\\\", \\\"Alliance\\\", \\\"Airport\\\", \\\"in\\\", \\\"Fort\\\", \\\"Worth\\\", \\\",\\\", \\\"Texas\\\", \\\".\\\"], \\\"h\\\": [\\\"alliance airport\\\", \\\"Q5472378\\\", [[12, 13]]], \\\"t\\\": [\\\"fort worth, texas\\\", \\\"Q16558\\\", [[15, 16, 17, 18]]]}, {\\\"tokens\\\": [\\\"Retiro\\\", \\\"Los\\\", \\\"Maitenes\\\", \\\"Airport\\\", \\\"(\\\", \\\",\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"northeast\\\", \\\"of\\\", \\\"Retiro\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Maule\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"los maitenes airport\\\", \\\"Q16899238\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"retiro\\\", \\\"Q56122\\\", [[0], [12]]]}, {\\\"tokens\\\": [\\\"Claremont\\\", \\\"Airport\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"Cecil\\\", \\\"County\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"located\\\", \\\"south\\\", \\\"of\\\", \\\"Elkton\\\", \\\",\\\", \\\"Maryland\\\", \\\".\\\"], \\\"h\\\": [\\\"cecil county airport\\\", \\\"Q19574884\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"elkton, maryland\\\", \\\"Q754338\\\", [[16, 17, 18]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"route\\\", \\\"between\\\", \\\"Gothenburg\\\", \\\"and\\\", \\\"Stockholm\\\", \\\"ended\\\", \\\"in\\\", \\\"January\\\", \\\"2015\\\", \\\"due\\\", \\\"to\\\", \\\"the\\\", \\\"sudden\\\", \\\"closure\\\", \\\"of\\\", \\\"G\\\\u00f6teborg\\\", \\\"City\\\", \\\"Airport\\\", \\\"by\\\", \\\"Swedavia\\\", \\\".\\\"], \\\"h\\\": [\\\"g\\\\u00f6teborg city airport\\\", \\\"Q844281\\\", [[16, 17, 18]]], \\\"t\\\": [\\\"gothenburg\\\", \\\"Q25287\\\", [[3]]]}, {\\\"tokens\\\": [\\\"David\\\", \\\"Jay\\\", \\\"Perry\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"town\\\", \\\"-\\\", \\\"owned\\\", \\\"public\\\", \\\"-\\\", \\\"use\\\", \\\"airport\\\", \\\"in\\\", \\\"Goldsby\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"McClain\\\", \\\"County\\\", \\\",\\\", \\\"Oklahoma\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"david jay perry airport\\\", \\\"Q1709203\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"goldsby\\\", \\\"Q2456775\\\", [[14]]]}, {\\\"tokens\\\": [\\\"Wiley\\\", \\\"Post\\\", \\\"Airport\\\", \\\"in\\\", \\\"Bethany\\\", \\\"and\\\", \\\"Max\\\", \\\"Westheimer\\\", \\\"Airport\\\", \\\"in\\\", \\\"Norman\\\", \\\"serve\\\", \\\"as\\\", \\\"reliever\\\", \\\"airports\\\", \\\"for\\\", \\\"Will\\\", \\\"Rogers\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"max westheimer airport\\\", \\\"Q10853586\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"norman\\\", \\\"Q40347\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Nearest\\\", \\\"airport\\\", \\\"to\\\", \\\"this\\\", \\\"airstrip\\\", \\\"is\\\", \\\"Savitri\\\", \\\"Jindal\\\", \\\"Airport\\\", \\\"in\\\", \\\"Angul\\\", \\\",\\\", \\\"Odisha\\\", \\\".\\\"], \\\"h\\\": [\\\"savitri jindal airport\\\", \\\"Q18355676\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"angul\\\", \\\"Q518237\\\", [[10]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"facility\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"west\\\", \\\"part\\\", \\\"of\\\", \\\"Regina\\\", \\\",\\\", \\\"Saskatchewan\\\", \\\",\\\", \\\"near\\\", \\\"the\\\", \\\"airport\\\", \\\",\\\", \\\"and\\\", \\\"consists\\\", \\\"of\\\", \\\"several\\\", \\\"buildings\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q1571015\\\", [[15]]], \\\"t\\\": [\\\"regina, saskatchewan\\\", \\\"Q2123\\\", [[9, 10, 11]]]}, {\\\"tokens\\\": [\\\"Also\\\", \\\",\\\", \\\"the\\\", \\\"service\\\", \\\"to\\\", \\\"Washington\\\", \\\"Dulles\\\", \\\"airport\\\", \\\"resumed\\\", \\\"1\\\", \\\"May\\\", \\\"2015\\\", \\\",\\\", \\\"with\\\", \\\"four\\\", \\\"flights\\\", \\\"weekly\\\", \\\".\\\"], \\\"h\\\": [\\\"dulles\\\", \\\"Q466835\\\", [[6]]], \\\"t\\\": [\\\"washington\\\", \\\"Q61\\\", [[5]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"2003\\\", \\\",\\\", \\\"Benoit\\\", \\\"produced\\\", \\\"two\\\", \\\"canvases\\\", \\\",\\\", \\\"\\\\\\\"\\\", \\\"Orly\\\", \\\"(\\\", \\\"South\\\", \\\")\\\", \\\"\\\\\\\"\\\", \\\",\\\", \\\"inspired\\\", \\\"by\\\", \\\"the\\\", \\\"Orly\\\", \\\"Airport\\\", \\\"in\\\", \\\"Paris\\\", \\\".\\\"], \\\"h\\\": [\\\"orly airport\\\", \\\"Q223416\\\", [[18, 19]]], \\\"t\\\": [\\\"paris\\\", \\\"Q90\\\", [[21]]]}, {\\\"tokens\\\": [\\\"Dr.\\\", \\\"Ferdinand\\\", \\\"Lumban\\\", \\\"Tobing\\\", \\\"Airport\\\", \\\"(\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"\\\\\\\"\\\", \\\"Pinangsori\\\", \\\"Airport\\\", \\\"\\\\\\\"\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Sibolga\\\", \\\"in\\\", \\\"the\\\", \\\"North\\\", \\\"Sumatra\\\", \\\"province\\\", \\\"of\\\", \\\"Indonesia\\\", \\\".\\\"], \\\"h\\\": [\\\"ferdinand lumban tobing airport\\\", \\\"Q4272430\\\", [[1, 2, 3, 4]]], \\\"t\\\": [\\\"sibolga\\\", \\\"Q5984\\\", [[21]]]}, {\\\"tokens\\\": [\\\"Franco\\\", \\\"Bianco\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"northwest\\\", \\\"of\\\", \\\"Cerro\\\", \\\"Sombrero\\\", \\\",\\\", \\\"a\\\", \\\"petroleum\\\", \\\"production\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Magallanes\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"franco bianco airport\\\", \\\"Q16891421\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"cerro sombrero\\\", \\\"Q1006493\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"has\\\", \\\"branches\\\", \\\"in\\\", \\\"Gros\\\", \\\"Islet\\\", \\\",\\\", \\\"Vieux\\\", \\\"Fort\\\", \\\",\\\", \\\"Soufri\\\\u00e8re\\\", \\\",\\\", \\\"and\\\", \\\"Castries\\\", \\\"(\\\", \\\"Bridge\\\", \\\"Street\\\", \\\"and\\\", \\\"the\\\", \\\"Waterfront\\\", \\\"Areas\\\", \\\")\\\", \\\"as\\\", \\\"well\\\", \\\"as\\\", \\\"a\\\", \\\"Bureau\\\", \\\"de\\\", \\\"Change\\\", \\\"at\\\", \\\"Hewanorra\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"hewanorra international airport\\\", \\\"Q1431475\\\", [[30, 31, 32]]], \\\"t\\\": [\\\"vieux fort\\\", \\\"Q1472864\\\", [[7, 8]]]}, {\\\"tokens\\\": [\\\"After\\\", \\\"leaving\\\", \\\"Brewster\\\", \\\",\\\", \\\"US\\\", \\\"97\\\", \\\"crosses\\\", \\\"the\\\", \\\"Okanogan\\\", \\\"River\\\", \\\"and\\\", \\\"passes\\\", \\\"Anderson\\\", \\\"Field\\\", \\\"to\\\", \\\"intersect\\\", \\\"SR\\\", \\\"17\\\", \\\"north\\\", \\\"of\\\", \\\"Fort\\\", \\\"Okanogan\\\", \\\"State\\\", \\\"Park\\\", \\\".\\\"], \\\"h\\\": [\\\"anderson field\\\", \\\"Q4754070\\\", [[12, 13]]], \\\"t\\\": [\\\"brewster\\\", \\\"Q1506880\\\", [[2]]]}, {\\\"tokens\\\": [\\\"Khorog\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Khorugh\\\", \\\"(\\\", \\\"also\\\", \\\"spelled\\\", \\\"Khorog\\\", \\\")\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"the\\\", \\\"Gorno\\\", \\\"-\\\", \\\"Badakhshan\\\", \\\"Autonomous\\\", \\\"Province\\\", \\\"in\\\", \\\"Tajikistan\\\", \\\".\\\"], \\\"h\\\": [\\\"khorog airport\\\", \\\"Q6402378\\\", [[0, 1]]], \\\"t\\\": [\\\"khorugh\\\", \\\"Q467501\\\", [[6]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"November\\\", \\\"2009\\\", \\\"a\\\", \\\"Shanghai\\\", \\\"woman\\\", \\\"threw\\\", \\\"gasoline\\\", \\\"bombs\\\", \\\"at\\\", \\\"government\\\", \\\"forklifts\\\", \\\"working\\\", \\\"on\\\", \\\"an\\\", \\\"expansion\\\", \\\"of\\\", \\\"the\\\", \\\"Hongqiao\\\", \\\"airport\\\", \\\"expansion\\\", \\\".\\\"], \\\"h\\\": [\\\"hongqiao airport\\\", \\\"Q421811\\\", [[18, 19]]], \\\"t\\\": [\\\"shanghai\\\", \\\"Q8686\\\", [[4]]]}, {\\\"tokens\\\": [\\\"Pinal\\\", \\\"Airpark\\\", \\\"is\\\", \\\"the\\\", \\\"home\\\", \\\"of\\\", \\\"Marana\\\", \\\"Aerospace\\\", \\\"Solutions\\\", \\\",\\\", \\\"Aircraft\\\", \\\"Demolition\\\", \\\",\\\", \\\"LLC\\\", \\\",\\\", \\\"Jet\\\", \\\"Yard\\\", \\\",\\\", \\\"LLC\\\", \\\",\\\", \\\"and\\\", \\\"Silverbell\\\", \\\"Army\\\", \\\"Heliport\\\", \\\"(\\\", \\\"SAHP\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"pinal airpark\\\", \\\"Q5353435\\\", [[0, 1]]], \\\"t\\\": [\\\"marana\\\", \\\"Q762743\\\", [[6]]]}, {\\\"tokens\\\": [\\\"Roseau\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Canefield\\\", \\\"Airport\\\", \\\",\\\", \\\"a\\\", \\\"nearby\\\", \\\"small\\\", \\\"aircraft\\\", \\\"airport\\\", \\\"that\\\", \\\"provides\\\", \\\"direct\\\", \\\"links\\\", \\\"to\\\", \\\"nearby\\\", \\\"islands\\\", \\\",\\\", \\\"as\\\", \\\"well\\\", \\\"as\\\", \\\"the\\\", \\\"larger\\\", \\\"Douglas\\\", \\\"\\\\u2013\\\", \\\"Charles\\\", \\\"Airport\\\", \\\"to\\\", \\\"the\\\", \\\"north\\\", \\\".\\\"], \\\"h\\\": [\\\"canefield airport\\\", \\\"Q1033097\\\", [[4, 5]]], \\\"t\\\": [\\\"roseau\\\", \\\"Q36281\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Aerov\\\\u00edas\\\", \\\"Nacionales\\\", \\\"'\\\", \\\"airplane\\\", \\\"was\\\", \\\"not\\\", \\\"able\\\", \\\"to\\\", \\\"perform\\\", \\\"its\\\", \\\"duty\\\", \\\"and\\\", \\\"Felix\\\", \\\"Juan\\\", \\\"Serralles\\\", \\\",\\\", \\\"who\\\", \\\"took\\\", \\\"off\\\", \\\"from\\\", \\\"Mercedita\\\", \\\"Airport\\\", \\\"in\\\", \\\"Ponce\\\", \\\",\\\", \\\"won\\\", \\\"the\\\", \\\"race\\\", \\\"for\\\", \\\"the\\\", \\\"Powelson\\\", \\\"Airlines\\\", \\\".\\\"], \\\"h\\\": [\\\"mercedita airport\\\", \\\"Q652578\\\", [[20, 21]]], \\\"t\\\": [\\\"ponce\\\", \\\"Q864024\\\", [[23]]]}, {\\\"tokens\\\": [\\\"Avelino\\\", \\\"Vieira\\\", \\\"Airport\\\", \\\"is\\\", \\\"the\\\", \\\"airport\\\", \\\"serving\\\", \\\"Arapoti\\\", \\\",\\\", \\\"Brazil\\\", \\\".\\\"], \\\"h\\\": [\\\"avelino vieira airport\\\", \\\"Q4784231\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"arapoti\\\", \\\"Q1805391\\\", [[7]]]}, {\\\"tokens\\\": [\\\"Beaumont\\\", \\\"One\\\", \\\"is\\\", \\\"co\\\", \\\"-\\\", \\\"based\\\", \\\"at\\\", \\\"32MI\\\", \\\"-\\\", \\\"William\\\", \\\"Beaumont\\\", \\\"Hospital\\\", \\\"Heliport\\\", \\\"and\\\", \\\"KVLL\\\", \\\"-\\\", \\\"Oakland\\\", \\\"/\\\", \\\"Troy\\\", \\\"Airport\\\", \\\"in\\\", \\\"Troy\\\", \\\",\\\", \\\"Michigan\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"kvll - oakland/troy airport\\\", \\\"Q2902372\\\", [[14, 15, 16, 17, 18, 19]]], \\\"t\\\": [\\\"troy, michigan\\\", \\\"Q990271\\\", [[21, 22, 23]]]}, {\\\"tokens\\\": [\\\"Dalton\\\", \\\"Airport\\\", \\\",\\\", \\\"a\\\", \\\"public\\\", \\\"use\\\", \\\"airport\\\", \\\"near\\\", \\\"Flushing\\\", \\\",\\\", \\\"also\\\", \\\"serves\\\", \\\"small\\\", \\\",\\\", \\\"privately\\\", \\\"owned\\\", \\\"planes\\\", \\\".\\\"], \\\"h\\\": [\\\"dalton airport\\\", \\\"Q5211664\\\", [[0, 1]]], \\\"t\\\": [\\\"flushing\\\", \\\"Q967748\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Chattanooga\\\", \\\"Metropolitan\\\", \\\"Airport\\\", \\\"officials\\\", \\\"and\\\", \\\"a\\\", \\\"Georgia\\\", \\\"state\\\", \\\"senator\\\", \\\"have\\\", \\\"proposed\\\", \\\"expansion\\\", \\\"of\\\", \\\"the\\\", \\\"airport\\\", \\\",\\\", \\\"located\\\", \\\"in\\\", \\\"Chattanooga\\\", \\\",\\\", \\\"Tennessee\\\", \\\",\\\", \\\"as\\\", \\\"a\\\", \\\"solution\\\", \\\"to\\\", \\\"Atlanta\\\", \\\"'s\\\", \\\"capacity\\\", \\\"needs\\\", \\\".\\\"], \\\"h\\\": [\\\"chattanooga metropolitan airport\\\", \\\"Q1708272\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"chattanooga, tennessee\\\", \\\"Q186702\\\", [[18, 19, 20]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Fulton\\\", \\\"County\\\", \\\"Airport\\\", \\\",\\\", \\\"often\\\", \\\"called\\\", \\\"Charlie\\\", \\\"Brown\\\", \\\"Field\\\", \\\"after\\\", \\\"politician\\\", \\\"Charles\\\", \\\"M.\\\", \\\"Brown\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"just\\\", \\\"west\\\", \\\"-\\\", \\\"southwest\\\", \\\"of\\\", \\\"Atlanta\\\", \\\"'s\\\", \\\"city\\\", \\\"limit\\\", \\\".\\\"], \\\"h\\\": [\\\"fulton county airport\\\", \\\"Q3274683\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"atlanta\\\", \\\"Q23556\\\", [[23]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"a\\\", \\\"short\\\", \\\"distance\\\", \\\"to\\\", \\\"the\\\", \\\"east\\\", \\\"of\\\", \\\"Vienna\\\", \\\"'s\\\", \\\"main\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"main airport\\\", \\\"Q32999\\\", [[11, 12]]], \\\"t\\\": [\\\"vienna\\\", \\\"Q1741\\\", [[9]]]}, {\\\"tokens\\\": [\\\"At\\\", \\\"11:00\\\", \\\"local\\\", \\\"time\\\", \\\"(\\\", \\\"02:00\\\", \\\"UTC\\\", \\\")\\\", \\\",\\\", \\\"Flight\\\", \\\"836\\\", \\\"overran\\\", \\\"the\\\", \\\"runway\\\", \\\"on\\\", \\\"landing\\\", \\\"at\\\", \\\"Rendani\\\", \\\"Airport\\\", \\\",\\\", \\\"Manokwari\\\", \\\",\\\", \\\"Indonesia\\\", \\\"on\\\", \\\"a\\\", \\\"scheduled\\\", \\\"domestic\\\", \\\"flight\\\", \\\"from\\\", \\\"Sorong\\\", \\\"Airport\\\", \\\",\\\", \\\"Sorong\\\", \\\".\\\"], \\\"h\\\": [\\\"rendani airport\\\", \\\"Q964835\\\", [[17, 18]]], \\\"t\\\": [\\\"manokwari\\\", \\\"Q848672\\\", [[20]]]}, {\\\"tokens\\\": [\\\"Mantz\\\", \\\"flew\\\", \\\"a\\\", \\\"Curtiss\\\", \\\"-\\\", \\\"Wright\\\", \\\"Travel\\\", \\\"Air\\\", \\\"Model\\\", \\\"16\\\", \\\"K\\\", \\\"in\\\", \\\"a\\\", \\\"spectacular\\\", \\\"stunt\\\", \\\",\\\", \\\"flying\\\", \\\"through\\\", \\\"a\\\", \\\"hangar\\\", \\\"at\\\", \\\"the\\\", \\\"Bishop\\\", \\\"Airport\\\", \\\",\\\", \\\"Bishop\\\", \\\",\\\", \\\"California\\\", \\\".\\\", \\\"Dwiggins\\\", \\\"1967\\\", \\\",\\\", \\\"pp\\\", \\\".\\\"], \\\"h\\\": [\\\"bishop airport\\\", \\\"Q4087670\\\", [[22, 23]]], \\\"t\\\": [\\\"bishop, california\\\", \\\"Q852658\\\", [[25, 26, 27]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"21\\\", \\\"May\\\", \\\"Mansfeld\\\", \\\"was\\\", \\\"posted\\\", \\\"to\\\", \\\"Tafraoui\\\", \\\"airfield\\\", \\\"near\\\", \\\"Oran\\\", \\\"in\\\", \\\"French\\\", \\\"Algeria\\\", \\\"for\\\", \\\"training\\\", \\\"on\\\", \\\"obsolescent\\\", \\\"Bloch\\\", \\\"MB.200\\\", \\\"and\\\", \\\"Bloch\\\", \\\"MB.210\\\", \\\"bomber\\\", \\\"aircraft\\\", \\\".\\\"], \\\"h\\\": [\\\"tafraoui airfield\\\", \\\"Q6588435\\\", [[7, 8]]], \\\"t\\\": [\\\"oran\\\", \\\"Q131818\\\", [[10]]]}, {\\\"tokens\\\": [\\\"There\\\", \\\"are\\\", \\\"three\\\", \\\"airstrips\\\", \\\":\\\", \\\"Kayonza\\\", \\\"Tea\\\", \\\"Factory\\\", \\\",\\\", \\\"Savannah\\\", \\\"Airstrip\\\", \\\"near\\\", \\\"Kihihi\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"Ishasha\\\", \\\"River\\\", \\\"Camp\\\", \\\"Airport\\\", \\\"in\\\", \\\"the\\\", \\\"Ishasha\\\", \\\"Sector\\\", \\\"of\\\", \\\"Queen\\\", \\\"Elizabeth\\\", \\\"National\\\", \\\"Park\\\", \\\".\\\"], \\\"h\\\": [\\\"ishasha river camp airport\\\", \\\"Q21974285\\\", [[16, 17, 18, 19]]], \\\"t\\\": [\\\"queen elizabeth national park\\\", \\\"Q530084\\\", [[25, 26, 27, 28]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Wakulla\\\", \\\"County\\\", \\\"Airport\\\", \\\"(\\\", \\\"2J0\\\", \\\")\\\", \\\",\\\", \\\"located\\\", \\\"south\\\", \\\"of\\\", \\\"Panacea\\\", \\\",\\\", \\\"is\\\", \\\"a\\\", \\\"small\\\", \\\"public\\\", \\\"-\\\", \\\"use\\\", \\\"airport\\\", \\\"with\\\", \\\"a\\\", \\\"single\\\", \\\",\\\", \\\"north\\\", \\\"-\\\", \\\"south\\\", \\\"turf\\\", \\\"runway\\\", \\\".\\\"], \\\"h\\\": [\\\"wakulla county airport\\\", \\\"Q5309352\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"panacea\\\", \\\"Q5306283\\\", [[11]]]}, {\\\"tokens\\\": [\\\"M\\\\u00e9rida\\\", \\\",\\\", \\\"a\\\", \\\"university\\\", \\\"and\\\", \\\"tourist\\\", \\\"town\\\", \\\"located\\\", \\\"high\\\", \\\"in\\\", \\\"the\\\", \\\"Andes\\\", \\\"mountains\\\", \\\",\\\", \\\"is\\\", \\\"surrounded\\\", \\\"by\\\", \\\"higher\\\", \\\"terrain\\\", \\\"with\\\", \\\"night\\\", \\\"flights\\\", \\\"prohibited\\\", \\\"at\\\", \\\"the\\\", \\\"nearby\\\", \\\"Alberto\\\", \\\"Carnevalli\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"alberto carnevalli airport\\\", \\\"Q2704391\\\", [[26, 27, 28]]], \\\"t\\\": [\\\"m\\\\u00e9rida\\\", \\\"Q23551\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"aircraft\\\", \\\"departed\\\", \\\"King\\\", \\\"Abdulaziz\\\", \\\"International\\\", \\\"Airport\\\", \\\"bound\\\", \\\"for\\\", \\\"Sadiq\\\", \\\"Abubakar\\\", \\\"III\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Sokoto\\\", \\\",\\\", \\\"but\\\", \\\"problems\\\", \\\"were\\\", \\\"reported\\\", \\\"shortly\\\", \\\"after\\\", \\\"takeoff\\\", \\\".\\\"], \\\"h\\\": [\\\"sadiq abubakar iii international airport\\\", \\\"Q922675\\\", [[9, 10, 11, 12, 13]]], \\\"t\\\": [\\\"sokoto\\\", \\\"Q336350\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Santa\\\", \\\"B\\\\u00e1rbara\\\", \\\"Airport\\\", \\\"(\\\", \\\",\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"east\\\", \\\"of\\\", \\\"Romeral\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Maule\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"santa b\\\\u00e1rbara airport\\\", \\\"Q16896455\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"romeral\\\", \\\"Q56124\\\", [[11]]]}, {\\\"tokens\\\": [\\\"Kisangani\\\", \\\"Simisini\\\", \\\"Air\\\", \\\"Base\\\", \\\"is\\\", \\\"a\\\", \\\"military\\\", \\\"airport\\\", \\\"in\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Kisangani\\\", \\\"in\\\", \\\"Democratic\\\", \\\"Republic\\\", \\\"of\\\", \\\"the\\\", \\\"Congo\\\", \\\".\\\"], \\\"h\\\": [\\\"simisini air base\\\", \\\"Q21974331\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"kisangani\\\", \\\"Q146723\\\", [[0], [12]]]}, {\\\"tokens\\\": [\\\"Jaro\\\", \\\"was\\\", \\\"a\\\", \\\"charter\\\", \\\"airline\\\", \\\"based\\\", \\\"at\\\", \\\"Aurel\\\", \\\"Vlaicu\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Bucharest\\\", \\\",\\\", \\\"Romania\\\", \\\".\\\"], \\\"h\\\": [\\\"aurel vlaicu international airport\\\", \\\"Q843229\\\", [[7, 8, 9, 10]]], \\\"t\\\": [\\\"bucharest\\\", \\\"Q19660\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Gautam\\\", \\\"Buddha\\\", \\\"Airport\\\", \\\"located\\\", \\\"in\\\", \\\"Siddharthanagar\\\", \\\"is\\\", \\\"the\\\", \\\"nearest\\\", \\\"airport\\\", \\\"from\\\", \\\"Sunwal\\\", \\\"connecting\\\", \\\"to\\\", \\\"Kathmandu\\\", \\\".\\\"], \\\"h\\\": [\\\"gautam buddha airport\\\", \\\"Q3275873\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"siddharthanagar\\\", \\\"Q1530936\\\", [[5]]]}, {\\\"tokens\\\": [\\\"Marianna\\\", \\\"/\\\", \\\"Lee\\\", \\\"County\\\", \\\"Airport\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"Steve\\\", \\\"Edwards\\\", \\\"Field\\\", \\\",\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"use\\\", \\\"airport\\\", \\\"in\\\", \\\"Lee\\\", \\\"County\\\", \\\",\\\", \\\"Arkansas\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"steve edwards field\\\", \\\"Q14681184\\\", [[9, 10, 11]]], \\\"t\\\": [\\\"marianna\\\", \\\"Q79582\\\", [[0]]]}, {\\\"tokens\\\": [\\\"FM\\\", \\\"691\\\", \\\"begins\\\", \\\"at\\\", \\\"an\\\", \\\"intersection\\\", \\\"with\\\", \\\"Perimeter\\\", \\\"Road\\\", \\\"near\\\", \\\"North\\\", \\\"Texas\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Sherman\\\", \\\"and\\\", \\\"has\\\", \\\"an\\\", \\\"intersection\\\", \\\"with\\\", \\\"FM\\\", \\\"1417\\\", \\\"just\\\", \\\"east\\\", \\\"of\\\", \\\"here\\\", \\\".\\\"], \\\"h\\\": [\\\"north texas regional airport\\\", \\\"Q7056982\\\", [[10, 11, 12, 13]]], \\\"t\\\": [\\\"sherman\\\", \\\"Q982379\\\", [[15]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"serves\\\", \\\"as\\\", \\\"the\\\", \\\"main\\\", \\\"route\\\", \\\"linking\\\", \\\"the\\\", \\\"cities\\\", \\\"of\\\", \\\"Limassol\\\", \\\"(\\\", \\\"with\\\", \\\"the\\\", \\\"biggest\\\", \\\"seaport\\\", \\\"on\\\", \\\"the\\\", \\\"island\\\", \\\")\\\", \\\"and\\\", \\\"Larnaca\\\", \\\"(\\\", \\\"with\\\", \\\"the\\\", \\\"largest\\\", \\\"airport\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q654636\\\", [[26]]], \\\"t\\\": [\\\"larnaca\\\", \\\"Q171882\\\", [[21]]]}, {\\\"tokens\\\": [\\\"Fukushima\\\", \\\"Airport\\\", \\\"in\\\", \\\"Sukagawa\\\", \\\"is\\\", \\\"the\\\", \\\"nearest\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"fukushima airport\\\", \\\"Q177473\\\", [[0, 1]]], \\\"t\\\": [\\\"sukagawa\\\", \\\"Q819664\\\", [[3]]]}, {\\\"tokens\\\": [\\\"Aviation\\\", \\\"fuel\\\", \\\"at\\\", \\\"Williams\\\", \\\"Field\\\", \\\"is\\\", \\\"pumped\\\", \\\"in\\\", \\\"a\\\", \\\"16\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\"(\\\", \\\"10\\\", \\\"\\\\u00a0\\\", \\\"mi\\\", \\\")\\\", \\\"flexible\\\", \\\"pipe\\\", \\\"from\\\", \\\"McMurdo\\\", \\\"Station\\\", \\\".\\\"], \\\"h\\\": [\\\"williams field\\\", \\\"Q2748837\\\", [[3, 4]]], \\\"t\\\": [\\\"mcmurdo station\\\", \\\"Q498627\\\", [[20, 21]]]}, {\\\"tokens\\\": [\\\"Ransome\\\", \\\"Airlines\\\", \\\"was\\\", \\\"a\\\", \\\"regional\\\", \\\"airline\\\", \\\"from\\\", \\\"the\\\", \\\"United\\\", \\\"States\\\", \\\",\\\", \\\"headquartered\\\", \\\"at\\\", \\\"Northeast\\\", \\\"Philadelphia\\\", \\\"Airport\\\", \\\"near\\\", \\\"Philadelphia\\\", \\\",\\\", \\\"Pennsylvania\\\", \\\".\\\"], \\\"h\\\": [\\\"northeast philadelphia airport\\\", \\\"Q2739991\\\", [[13, 14, 15]]], \\\"t\\\": [\\\"philadelphia, pennsylvania\\\", \\\"Q1345\\\", [[17, 18, 19]]]}, {\\\"tokens\\\": [\\\"Sharjah\\\", \\\"-\\\", \\\"SHJ\\\", \\\".\\\"], \\\"h\\\": [\\\"shj\\\", \\\"Q635826\\\", [[2]]], \\\"t\\\": [\\\"sharjah\\\", \\\"Q289693\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Veterans\\\", \\\"Airport\\\", \\\"of\\\", \\\"Southern\\\", \\\"Illinois\\\", \\\",\\\", \\\"formally\\\", \\\"known\\\", \\\"as\\\", \\\"the\\\", \\\"Williamson\\\", \\\"County\\\", \\\"Regional\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"five\\\", \\\"miles\\\", \\\"west\\\", \\\"of\\\", \\\"Marion\\\", \\\",\\\", \\\"in\\\", \\\"Williamson\\\", \\\"County\\\", \\\",\\\", \\\"Illinois\\\", \\\".\\\"], \\\"h\\\": [\\\"williamson county regional airport\\\", \\\"Q8021210\\\", [[10, 11, 12, 13]]], \\\"t\\\": [\\\"marion\\\", \\\"Q575399\\\", [[20]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airport\\\", \\\"at\\\", \\\"Saint\\\", \\\"-\\\", \\\"Denis\\\", \\\"was\\\", \\\"closed\\\", \\\",\\\", \\\"but\\\", \\\"reopened\\\", \\\"after\\\", \\\"the\\\", \\\"storm\\\", \\\"passed\\\", \\\"the\\\", \\\"island\\\", \\\";\\\", \\\"several\\\", \\\"flights\\\", \\\"were\\\", \\\"canceled\\\", \\\"as\\\", \\\"a\\\", \\\"result\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q17430\\\", [[1]]], \\\"t\\\": [\\\"saint-denis\\\", \\\"Q47045\\\", [[3, 4, 5]]]}, {\\\"tokens\\\": [\\\"McGinness\\\", \\\"Airport\\\", \\\"(\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"McGinness\\\", \\\"Field\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"closed\\\", \\\"public\\\", \\\"-\\\", \\\"use\\\", \\\"private\\\", \\\"airport\\\", \\\"located\\\", \\\"one\\\", \\\"mile\\\", \\\"from\\\", \\\"Columbia\\\", \\\",\\\", \\\"Pennsylvania\\\", \\\".\\\"], \\\"h\\\": [\\\"mcginness airport\\\", \\\"Q19876918\\\", [[0, 1]]], \\\"t\\\": [\\\"columbia\\\", \\\"Q1133892\\\", [[21]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Nicholas\\\", \\\"-\\\", \\\"Beazley\\\", \\\"Aircraft\\\", \\\"Company\\\", \\\"Museum\\\", \\\"resides\\\", \\\"at\\\", \\\"Marshall\\\", \\\"Memorial\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"in\\\", \\\"Marshall\\\", \\\",\\\", \\\"Missouri\\\", \\\",\\\", \\\"featuring\\\", \\\"a\\\", \\\"NB-3\\\", \\\"on\\\", \\\"display\\\", \\\".\\\"], \\\"h\\\": [\\\"marshall memorial municipal airport\\\", \\\"Q14704430\\\", [[9, 10, 11, 12]]], \\\"t\\\": [\\\"marshall, missouri\\\", \\\"Q954882\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"Al\\\", \\\"Hoceima\\\", \\\"'s\\\", \\\"Cherif\\\", \\\"Al\\\", \\\"Idrissi\\\", \\\"Airport\\\", \\\"and\\\", \\\"Tetouan\\\", \\\"'s\\\", \\\"Sania\\\", \\\"Ramel\\\", \\\"Airport\\\", \\\"also\\\", \\\"receive\\\", \\\"commercial\\\", \\\"flights\\\", \\\".\\\"], \\\"h\\\": [\\\"sania ramel airport\\\", \\\"Q1433058\\\", [[10, 11, 12]]], \\\"t\\\": [\\\"tetouan\\\", \\\"Q185157\\\", [[8]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"island\\\", \\\"\\\\u2019s\\\", \\\"main\\\", \\\"town\\\", \\\"is\\\", \\\"Ponta\\\", \\\"do\\\", \\\"Sol\\\", \\\"on\\\", \\\"the\\\", \\\"north\\\", \\\"coast\\\", \\\",\\\", \\\"home\\\", \\\"to\\\", \\\"the\\\", \\\"closed\\\", \\\"Agostinho\\\", \\\"Neto\\\", \\\"Airport\\\", \\\",\\\", \\\"while\\\", \\\"its\\\", \\\"ferry\\\", \\\"port\\\", \\\"is\\\", \\\"Porto\\\", \\\"Novo\\\", \\\"on\\\", \\\"the\\\", \\\"south\\\", \\\"coast\\\", \\\".\\\"], \\\"h\\\": [\\\"agostinho neto airport\\\", \\\"Q636824\\\", [[18, 19, 20]]], \\\"t\\\": [\\\"ponta do sol\\\", \\\"Q768314\\\", [[6, 7, 8]]]}, {\\\"tokens\\\": [\\\"Frans\\\", \\\"Kaisiepo\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"Biak\\\", \\\",\\\", \\\"Papua\\\", \\\",\\\", \\\"Indonesia\\\", \\\".\\\"], \\\"h\\\": [\\\"frans kaisiepo international airport\\\", \\\"Q2134812\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"biak\\\", \\\"Q855314\\\", [[11]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Kish\\\", \\\"International\\\", \\\"Airport\\\", \\\"serves\\\", \\\"as\\\", \\\"the\\\", \\\"entry\\\", \\\"point\\\", \\\"for\\\", \\\"the\\\", \\\"hundreds\\\", \\\"of\\\", \\\"thousands\\\", \\\"of\\\", \\\"tourists\\\", \\\"who\\\", \\\"come\\\", \\\"to\\\", \\\"Kish\\\", \\\"Island\\\", \\\".\\\"], \\\"h\\\": [\\\"kish international airport\\\", \\\"Q2670526\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"kish island\\\", \\\"Q221883\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"Cheongju\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"at\\\", \\\"Ipsang\\\", \\\"-\\\", \\\"ri\\\", \\\"(\\\", \\\"a\\\", \\\"township\\\", \\\")\\\", \\\",\\\", \\\"Naesu\\\", \\\"-\\\", \\\"eup\\\", \\\"(\\\", \\\"\\\\uc74d\\\", \\\";\\\", \\\"town\\\", \\\")\\\", \\\",\\\", \\\"Cheongwon\\\", \\\"-\\\", \\\"gu\\\", \\\",\\\", \\\"Cheongju\\\", \\\",\\\", \\\"Chungcheongbuk\\\", \\\"-\\\", \\\"do\\\", \\\".\\\"], \\\"h\\\": [\\\"cheongju international airport\\\", \\\"Q483675\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"cheongwon-gu\\\", \\\"Q42147\\\", [[23, 24, 25]]]}, {\\\"tokens\\\": [\\\"flyadeal\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"Saudi\\\", \\\"low\\\", \\\"-\\\", \\\"cost\\\", \\\"airline\\\", \\\"based\\\", \\\"at\\\", \\\"King\\\", \\\"Abdulaziz\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Jeddah\\\", \\\".\\\"], \\\"h\\\": [\\\"king abdulaziz international airport\\\", \\\"Q153592\\\", [[12, 13, 14, 15]]], \\\"t\\\": [\\\"jeddah\\\", \\\"Q374365\\\", [[17]]]}, {\\\"tokens\\\": [\\\"Nicoya\\\", \\\"has\\\", \\\"also\\\", \\\"an\\\", \\\"airport\\\", \\\"for\\\", \\\"domestic\\\", \\\"flights\\\", \\\"with\\\", \\\"no\\\", \\\"current\\\", \\\"scheduled\\\", \\\"services\\\", \\\".\\\"], \\\"h\\\": [\\\"an airport\\\", \\\"Q12694168\\\", [[3, 4]]], \\\"t\\\": [\\\"nicoya\\\", \\\"Q2486629\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Sheikh\\\", \\\"-\\\", \\\"ul\\\", \\\"-\\\", \\\"Alam\\\", \\\"International\\\", \\\"Airport\\\", \\\"at\\\", \\\"Srinagar\\\", \\\"is\\\", \\\"the\\\", \\\"nearest\\\", \\\"airport\\\", \\\",\\\", \\\"southeast\\\", \\\";\\\", \\\"The\\\", \\\"Jammu\\\", \\\"Airport\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"winter\\\", \\\"capital\\\", \\\"of\\\", \\\"the\\\", \\\"state\\\", \\\".\\\"], \\\"h\\\": [\\\"sheikh-ul-alam international airport\\\", \\\"Q2247528\\\", [[0, 1, 2, 3, 4, 5, 6]]], \\\"t\\\": [\\\"srinagar\\\", \\\"Q170115\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Bugungu\\\", \\\"Airstrip\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"Bugungu\\\", \\\"Wildlife\\\", \\\"Reserve\\\", \\\"in\\\", \\\"the\\\", \\\"Murchison\\\", \\\"Falls\\\", \\\"National\\\", \\\"Park\\\", \\\"in\\\", \\\"Uganda\\\", \\\".\\\"], \\\"h\\\": [\\\"bugungu airstrip\\\", \\\"Q21974272\\\", [[0, 1]]], \\\"t\\\": [\\\"murchison falls national park\\\", \\\"Q1893242\\\", [[12, 13, 14, 15]]]}, {\\\"tokens\\\": [\\\"June\\\", \\\"23\\\\u201326\\\", \\\",\\\", \\\"2009\\\", \\\"from\\\", \\\"Denver\\\", \\\"(\\\", \\\"APA\\\", \\\",\\\", \\\"Centennial\\\", \\\"Airport\\\", \\\")\\\", \\\"to\\\", \\\"Atlantic\\\", \\\",\\\", \\\"Iowa\\\", \\\"(\\\", \\\"AIO\\\", \\\",\\\", \\\"Atlantic\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\")\\\", \\\",\\\", \\\"a\\\", \\\"distance\\\", \\\"of\\\", \\\"2359.0\\\", \\\"\\\\u00a0\\\", \\\"nm/2714.7\\\", \\\"sm\\\", \\\".\\\"], \\\"h\\\": [\\\"atlantic municipal airport\\\", \\\"Q2902476\\\", [[19, 20, 21]]], \\\"t\\\": [\\\"atlantic, iowa\\\", \\\"Q756267\\\", [[13, 14, 15]]]}, {\\\"tokens\\\": [\\\"Canadian\\\", \\\"Forces\\\", \\\"Base\\\", \\\"Lahr\\\", \\\"(\\\", \\\"IATA\\\", \\\":\\\", \\\"LHA\\\", \\\",\\\", \\\"ICAO\\\", \\\":\\\", \\\"EDTL\\\", \\\",\\\", \\\"former\\\", \\\"code\\\", \\\"EDAN\\\", \\\")\\\", \\\"was\\\", \\\"a\\\", \\\"military\\\", \\\"operated\\\", \\\"commercial\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"Lahr\\\", \\\",\\\", \\\"Germany\\\", \\\".\\\"], \\\"h\\\": [\\\"edtl\\\", \\\"Q597321\\\", [[11]]], \\\"t\\\": [\\\"lahr\\\", \\\"Q7039\\\", [[3], [25]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"two\\\", \\\"outlets\\\", \\\"share\\\", \\\"studios\\\", \\\"on\\\", \\\"Moffett\\\", \\\"Street\\\", \\\"in\\\", \\\"Salinas\\\", \\\"behind\\\", \\\"the\\\", \\\"city\\\", \\\"'s\\\", \\\"airport\\\", \\\";\\\", \\\"KMUV\\\", \\\"'s\\\", \\\"transmitter\\\", \\\"is\\\", \\\"located\\\", \\\"on\\\", \\\"Fremont\\\", \\\"Peak\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q7404650\\\", [[14]]], \\\"t\\\": [\\\"salinas\\\", \\\"Q488125\\\", [[9]]]}, {\\\"tokens\\\": [\\\"A\\\\u00e9roport\\\", \\\"is\\\", \\\"the\\\", \\\"place\\\", \\\"of\\\", \\\"Gustaf\\\", \\\"III\\\", \\\"Airport\\\", \\\",\\\", \\\"in\\\", \\\"\\\\\\\"\\\", \\\"quartier\\\", \\\"\\\\\\\"\\\", \\\"Saint\\\", \\\"-\\\", \\\"Jean\\\", \\\"of\\\", \\\"Saint\\\", \\\"Barth\\\\u00e9lemy\\\", \\\"in\\\", \\\"the\\\", \\\"Caribbean\\\", \\\".\\\"], \\\"h\\\": [\\\"gustaf iii airport\\\", \\\"Q38805\\\", [[5, 6, 7]]], \\\"t\\\": [\\\"saint barth\\\\u00e9lemy\\\", \\\"Q25362\\\", [[17, 18]]]}, {\\\"tokens\\\": [\\\"Tempuling\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Tempuling\\\", \\\"district\\\", \\\",\\\", \\\"that\\\", \\\"serves\\\", \\\"Tembilahan\\\", \\\"and\\\", \\\"surrounding\\\", \\\"areas\\\", \\\".\\\"], \\\"h\\\": [\\\"tempuling airport\\\", \\\"Q18821722\\\", [[0, 1]]], \\\"t\\\": [\\\"tembilahan\\\", \\\"Q6542770\\\", [[10]]]}, {\\\"tokens\\\": [\\\"\\\\\\\"\\\", \\\"Shuangliu\\\", \\\"Airport\\\", \\\",\\\", \\\"Chengdu\\\", \\\",\\\", \\\"610202\\\", \\\",\\\", \\\"Sichuan\\\", \\\",\\\", \\\"China\\\", \\\"\\\\\\\"\\\", \\\"On\\\", \\\"28\\\", \\\"October\\\", \\\"2002\\\", \\\",\\\", \\\"China\\\", \\\"Southwest\\\", \\\"Airlines\\\", \\\"was\\\", \\\"merged\\\", \\\"into\\\", \\\"Air\\\", \\\"China\\\", \\\".\\\"], \\\"h\\\": [\\\"shuangliu airport\\\", \\\"Q387560\\\", [[1, 2]]], \\\"t\\\": [\\\"chengdu\\\", \\\"Q30002\\\", [[4]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"region\\\", \\\"'s\\\", \\\"second\\\", \\\"international\\\", \\\"airport\\\", \\\"at\\\", \\\"Cam\\\", \\\"Ranh\\\", \\\"(\\\", \\\"serving\\\", \\\"Nha\\\", \\\"Trang\\\", \\\"flights\\\", \\\"to\\\", \\\"various\\\", \\\"cities\\\", \\\"in\\\", \\\"Vietnam\\\", \\\",\\\", \\\"Guangzhou\\\", \\\",\\\", \\\"Shanghais\\\", \\\",\\\", \\\"Hong\\\", \\\"Kong\\\", \\\",\\\", \\\"etc\\\", \\\".\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"cam ranh\\\", \\\"Q25226\\\", [[7, 8]]], \\\"t\\\": [\\\"nha trang\\\", \\\"Q19491\\\", [[11, 12]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"hub\\\", \\\"and\\\", \\\"headquarters\\\", \\\"are\\\", \\\"at\\\", \\\"Bole\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Addis\\\", \\\"Ababa\\\", \\\",\\\", \\\"from\\\", \\\"where\\\", \\\"it\\\", \\\"serves\\\", \\\"a\\\", \\\"network\\\", \\\"of\\\", \\\"122\\\", \\\"passenger\\\", \\\"destinations\\\", \\\"\\\\u201420\\\", \\\"of\\\", \\\"them\\\", \\\"domestic\\\\u2014\\\", \\\"and\\\", \\\"44\\\", \\\"freighter\\\", \\\"destinations\\\", \\\".\\\"], \\\"h\\\": [\\\"bole international airport\\\", \\\"Q44923\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"addis ababa\\\", \\\"Q3624\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"Kangerlussuaq\\\", \\\"is\\\", \\\"one\\\", \\\"of\\\", \\\"the\\\", \\\"settlements\\\", \\\"in\\\", \\\"Greenland\\\", \\\"exhibiting\\\", \\\"stable\\\", \\\"population\\\", \\\"growth\\\", \\\"patterns\\\", \\\"over\\\", \\\"the\\\", \\\"past\\\", \\\"two\\\", \\\"decades\\\", \\\",\\\", \\\"with\\\", \\\"a\\\", \\\"dynamically\\\", \\\"growing\\\", \\\"tourism\\\", \\\"industry\\\", \\\",\\\", \\\"primarily\\\", \\\"thanks\\\", \\\"to\\\", \\\"the\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q631430\\\", [[30]]], \\\"t\\\": [\\\"kangerlussuaq\\\", \\\"Q1007098\\\", [[0]]]}, {\\\"tokens\\\": [\\\"As\\\", \\\"of\\\", \\\"21\\\", \\\"April\\\", \\\"2015\\\", \\\"12:00\\\", \\\"am\\\", \\\",\\\", \\\"the\\\", \\\"airport\\\", \\\"of\\\", \\\"\\\\u00d6rnsk\\\\u00f6ldsvik\\\", \\\"/\\\", \\\"Gide\\\\u00e5\\\", \\\"(\\\", \\\"OER\\\", \\\"/\\\", \\\"ESNO\\\", \\\")\\\", \\\"is\\\", \\\"run\\\", \\\"using\\\", \\\"remote\\\", \\\"ATC\\\", \\\"services\\\", \\\"from\\\", \\\"Sundsvall\\\", \\\"/\\\", \\\"Midlanda\\\", \\\"(\\\", \\\"SDL\\\", \\\"/\\\", \\\"ESNN\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"oer\\\", \\\"Q2673175\\\", [[15]]], \\\"t\\\": [\\\"\\\\u00f6rnsk\\\\u00f6ldsvik\\\", \\\"Q28327\\\", [[11]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Air\\\", \\\"Base\\\", \\\"Alpnach\\\", \\\"(\\\", \\\"ICAO\\\", \\\"code\\\", \\\"LSMA\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"Swiss\\\", \\\"Air\\\", \\\"Force\\\", \\\"airfield\\\", \\\"near\\\", \\\"the\\\", \\\"town\\\", \\\"Alpnach\\\", \\\"in\\\", \\\"Canton\\\", \\\"of\\\", \\\"Obwalden\\\", \\\"in\\\", \\\"Switzerland\\\", \\\".\\\"], \\\"h\\\": [\\\"lsma\\\", \\\"Q1934947\\\", [[7]]], \\\"t\\\": [\\\"alpnach\\\", \\\"Q69296\\\", [[3], [18]]]}, {\\\"tokens\\\": [\\\"Shah\\\", \\\"Makhdum\\\", \\\"Airport\\\", \\\"of\\\", \\\"Rajshahi\\\", \\\",\\\", \\\"is\\\", \\\"named\\\", \\\"after\\\", \\\"him\\\", \\\".\\\"], \\\"h\\\": [\\\"shah makhdum airport\\\", \\\"Q2875736\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"rajshahi\\\", \\\"Q322155\\\", [[4]]]}, {\\\"tokens\\\": [\\\"Cathay\\\", \\\"Pacific\\\", \\\"Flight\\\", \\\"780\\\", \\\"took\\\", \\\"off\\\", \\\"from\\\", \\\"runway\\\", \\\"28\\\", \\\"at\\\", \\\"Surabaya\\\", \\\"'s\\\", \\\"Juanda\\\", \\\"International\\\", \\\"Airport\\\", \\\"at\\\", \\\"08:24\\\", \\\"local\\\", \\\"time\\\", \\\"(\\\", \\\"01:24\\\", \\\"UTC\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"juanda international airport\\\", \\\"Q1431631\\\", [[12, 13, 14]]], \\\"t\\\": [\\\"surabaya\\\", \\\"Q11462\\\", [[10]]]}, {\\\"tokens\\\": [\\\"An\\\", \\\"earlier\\\", \\\"KCTB\\\", \\\"-\\\", \\\"FM\\\", \\\"in\\\", \\\"Cut\\\", \\\"Bank\\\", \\\",\\\", \\\"Montana\\\", \\\"on\\\", \\\"102.7\\\", \\\"FM\\\", \\\"had\\\", \\\"its\\\", \\\"license\\\", \\\"cancelled\\\", \\\"in\\\", \\\"1993\\\", \\\".\\\"], \\\"h\\\": [\\\"kctb\\\", \\\"Q1655488\\\", [[2]]], \\\"t\\\": [\\\"cut bank, montana\\\", \\\"Q968158\\\", [[6, 7, 8, 9]]]}, {\\\"tokens\\\": [\\\"Surkhet\\\", \\\"Airport\\\", \\\"near\\\", \\\"Birendranagar\\\", \\\"has\\\", \\\"scheduled\\\", \\\"flights\\\", \\\"to\\\", \\\"Kathmandu\\\", \\\",\\\", \\\"Nepalgunj\\\", \\\",\\\", \\\"Jumla\\\", \\\"and\\\", \\\"other\\\", \\\"districts\\\", \\\".\\\"], \\\"h\\\": [\\\"surkhet airport\\\", \\\"Q1756900\\\", [[0, 1]]], \\\"t\\\": [\\\"birendranagar\\\", \\\"Q865146\\\", [[3]]]}, {\\\"tokens\\\": [\\\"With\\\", \\\"the\\\", \\\"opening\\\", \\\"of\\\", \\\"the\\\", \\\"route\\\", \\\"to\\\", \\\"the\\\", \\\"airport\\\", \\\"station\\\", \\\",\\\", \\\"the\\\", \\\"U2\\\", \\\"Nuremberg\\\", \\\"city\\\", \\\"area\\\", \\\"is\\\", \\\"completed\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q265994\\\", [[8]]], \\\"t\\\": [\\\"nuremberg\\\", \\\"Q2090\\\", [[13]]]}, {\\\"tokens\\\": [\\\"Winds\\\", \\\"remained\\\", \\\"strong\\\", \\\"farther\\\", \\\"inland\\\", \\\";\\\", \\\"Ivato\\\", \\\"International\\\", \\\"Airport\\\", \\\"near\\\", \\\"the\\\", \\\"capital\\\", \\\"Antananarivo\\\", \\\"reported\\\", \\\"winds\\\", \\\"of\\\", \\\",\\\", \\\"and\\\", \\\"winds\\\", \\\"in\\\", \\\"the\\\", \\\"capital\\\", \\\"were\\\", \\\"likely\\\", \\\"stronger\\\", \\\".\\\"], \\\"h\\\": [\\\"ivato international airport\\\", \\\"Q670038\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"antananarivo\\\", \\\"Q3915\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Keshod\\\", \\\"Airport\\\", \\\"was\\\", \\\"built\\\", \\\"by\\\", \\\"the\\\", \\\"\\\\\\\"\\\", \\\"Nawab\\\", \\\"of\\\", \\\"Junagadh\\\", \\\"\\\\\\\"\\\", \\\",\\\", \\\"Mahabatkhanji\\\", \\\"III\\\", \\\"for\\\", \\\"his\\\", \\\"private\\\", \\\"use\\\", \\\",\\\", \\\"by\\\", \\\"acquiring\\\", \\\"land\\\", \\\"from\\\", \\\"Kotadias\\\", \\\"(\\\", \\\"the\\\", \\\"Patel\\\", \\\"community\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"keshod airport\\\", \\\"Q2722850\\\", [[0, 1]]], \\\"t\\\": [\\\"junagadh\\\", \\\"Q11864\\\", [[9]]]}, {\\\"tokens\\\": [\\\"Choshuenco\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Molco\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"molco airport\\\", \\\"Q16895275\\\", [[4, 5]]], \\\"t\\\": [\\\"choshuenco\\\", \\\"Q5105354\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Enshi\\\", \\\"Xujiaping\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Enshi\\\", \\\"City\\\", \\\",\\\", \\\"Hubei\\\", \\\"province\\\", \\\",\\\", \\\"China\\\", \\\".\\\"], \\\"h\\\": [\\\"enshi xujiaping airport\\\", \\\"Q1937966\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"enshi city\\\", \\\"Q1028110\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"Due\\\", \\\"to\\\", \\\"mudslides\\\", \\\"and\\\", \\\"flooding\\\", \\\",\\\", \\\"the\\\", \\\"flight\\\", \\\"was\\\", \\\"diverted\\\", \\\"to\\\", \\\"Arturo\\\", \\\"Michelena\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Valencia\\\", \\\".\\\"], \\\"h\\\": [\\\"arturo michelena international airport\\\", \\\"Q2231898\\\", [[11, 12, 13, 14]]], \\\"t\\\": [\\\"valencia\\\", \\\"Q54880\\\", [[16]]]}, {\\\"tokens\\\": [\\\"Sumba\\\", \\\"Timur\\\", \\\"'s\\\", \\\"Waingapu\\\", \\\"Airport\\\", \\\"'\\\", \\\"Umbu\\\", \\\"Mehang\\\", \\\"Kunda\\\", \\\"'\\\", \\\"(\\\", \\\"IATA\\\", \\\":\\\", \\\"WGP\\\", \\\"-\\\", \\\"ICAO\\\", \\\":\\\", \\\"WRRW\\\", \\\")\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Waingapu\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"town\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"ferries\\\", \\\"from\\\", \\\"nearby\\\", \\\"islands\\\", \\\".\\\"], \\\"h\\\": [\\\"wgp\\\", \\\"Q652704\\\", [[13]]], \\\"t\\\": [\\\"waingapu\\\", \\\"Q781361\\\", [[3], [22]]]}, {\\\"tokens\\\": [\\\"Linden\\\", \\\"Airport\\\", \\\",\\\", \\\"a\\\", \\\"general\\\", \\\"aviation\\\", \\\"facility\\\", \\\",\\\", \\\"is\\\", \\\"in\\\", \\\"nearby\\\", \\\"Linden\\\", \\\",\\\", \\\"New\\\", \\\"Jersey\\\", \\\".\\\"], \\\"h\\\": [\\\"linden airport\\\", \\\"Q10853379\\\", [[0, 1]]], \\\"t\\\": [\\\"linden, new jersey\\\", \\\"Q1004712\\\", [[11, 12, 13, 14]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airline\\\", \\\"operated\\\", \\\"its\\\", \\\"first\\\", \\\"scheduled\\\", \\\"flight\\\", \\\"between\\\", \\\"Youngstown\\\", \\\"\\\\u2013\\\", \\\"Warren\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Youngstown\\\", \\\",\\\", \\\"Ohio\\\", \\\"and\\\", \\\"O'Hare\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Chicago\\\", \\\"on\\\", \\\"July\\\", \\\"1\\\", \\\",\\\", \\\"2016\\\", \\\".\\\"], \\\"h\\\": [\\\"youngstown\\\\u2013warren regional airport\\\", \\\"Q8058655\\\", [[8, 9, 10, 11, 12]]], \\\"t\\\": [\\\"youngstown, ohio\\\", \\\"Q216820\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"Auckland\\\", \\\"has\\\", \\\"New\\\", \\\"Zealand\\\", \\\"'s\\\", \\\"largest\\\", \\\"commercial\\\", \\\"port\\\", \\\"(\\\", \\\"mostly\\\", \\\"used\\\", \\\"for\\\", \\\"international\\\", \\\"commerce\\\", \\\")\\\", \\\"and\\\", \\\"the\\\", \\\"country\\\", \\\"'s\\\", \\\"largest\\\", \\\"international\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"largest international airport\\\", \\\"Q45938\\\", [[19, 20, 21]]], \\\"t\\\": [\\\"auckland\\\", \\\"Q37100\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Bondoukou\\\", \\\"has\\\", \\\"an\\\", \\\"airport\\\", \\\",\\\", \\\"Soko\\\", \\\"Airport\\\", \\\",\\\", \\\"with\\\", \\\"IATA\\\", \\\"code\\\", \\\"\\\\\\\"\\\", \\\"BDK\\\", \\\"\\\\\\\"\\\", \\\".\\\"], \\\"h\\\": [\\\"soko airport\\\", \\\"Q7555134\\\", [[5, 6]]], \\\"t\\\": [\\\"bondoukou\\\", \\\"Q892276\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Frankfurt\\\", \\\"Airport\\\", \\\"(\\\", \\\"IATA\\\", \\\":\\\", \\\"FRA\\\", \\\")\\\", \\\"is\\\", \\\"the\\\", \\\"busiest\\\", \\\"airport\\\", \\\"in\\\", \\\"Germany\\\", \\\",\\\", \\\"located\\\", \\\"in\\\", \\\"Frankfurt\\\", \\\"am\\\", \\\"Main\\\", \\\",\\\", \\\"Hesse\\\", \\\".\\\"], \\\"h\\\": [\\\"frankfurt airport\\\", \\\"Q46033\\\", [[0, 1]]], \\\"t\\\": [\\\"frankfurt am main\\\", \\\"Q1794\\\", [[16, 17, 18]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"group\\\", \\\"was\\\", \\\"evacuated\\\", \\\"to\\\", \\\"Capodichino\\\", \\\"Airport\\\", \\\"near\\\", \\\"Naples\\\", \\\"for\\\", \\\"several\\\", \\\"weeks\\\", \\\"until\\\", \\\"they\\\", \\\"returned\\\", \\\"to\\\", \\\"the\\\", \\\"repaired\\\", \\\"base\\\", \\\"on\\\", \\\"25\\\", \\\"April\\\", \\\",\\\", \\\"remaining\\\", \\\"until\\\", \\\"10\\\", \\\"June\\\", \\\"1944\\\", \\\".\\\"], \\\"h\\\": [\\\"capodichino airport\\\", \\\"Q849383\\\", [[5, 6]]], \\\"t\\\": [\\\"naples\\\", \\\"Q2634\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Hanover\\\", \\\"County\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"airport\\\", \\\"located\\\", \\\"14\\\", \\\"miles\\\", \\\"(\\\", \\\"22\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"north\\\", \\\"of\\\", \\\"the\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\"of\\\", \\\"Richmond\\\", \\\",\\\", \\\"Virginia\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"hanover county municipal airport\\\", \\\"Q3884853\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"richmond\\\", \\\"Q43421\\\", [[23]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"plane\\\", \\\"stopped\\\", \\\"once\\\", \\\"in\\\", \\\"Missouri\\\", \\\"to\\\", \\\"refuel\\\", \\\"and\\\", \\\"subsequently\\\", \\\"landed\\\", \\\"at\\\", \\\"Dyersburg\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"in\\\", \\\"Dyersburg\\\", \\\",\\\", \\\"Tennessee\\\", \\\"at\\\", \\\"5\\\", \\\"p.m.\\\"], \\\"h\\\": [\\\"dyersburg municipal airport\\\", \\\"Q5318578\\\", [[12, 13, 14]]], \\\"t\\\": [\\\"dyersburg, tennessee\\\", \\\"Q1268670\\\", [[16, 17, 18]]]}, {\\\"tokens\\\": [\\\"Wyandot\\\", \\\"County\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"airport\\\", \\\"located\\\", \\\"four\\\", \\\"miles\\\", \\\"(\\\", \\\"5\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"northwest\\\", \\\"of\\\", \\\"Upper\\\", \\\"Sandusky\\\", \\\",\\\", \\\"Ohio\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"wyandot county airport\\\", \\\"Q24061424\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"upper sandusky\\\", \\\"Q1913338\\\", [[17, 18]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"23\\\", \\\"October\\\", \\\"2012\\\", \\\",\\\", \\\"a\\\", \\\"K-8\\\", \\\"Karakorum\\\", \\\"training\\\", \\\"plane\\\", \\\"lost\\\", \\\"directional\\\", \\\"control\\\", \\\"during\\\", \\\"take\\\", \\\"off\\\", \\\"from\\\", \\\"Julius\\\", \\\"Nyerere\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Dar\\\", \\\"es\\\", \\\"Salaam\\\", \\\".\\\"], \\\"h\\\": [\\\"julius nyerere international airport\\\", \\\"Q1411192\\\", [[17, 18, 19, 20]]], \\\"t\\\": [\\\"dar es salaam\\\", \\\"Q1960\\\", [[22, 23, 24]]]}, {\\\"tokens\\\": [\\\"Avenger\\\", \\\"Field\\\", \\\"is\\\", \\\"a\\\", \\\"Texas\\\", \\\"airport\\\", \\\"in\\\", \\\"Nolan\\\", \\\"County\\\", \\\",\\\", \\\"three\\\", \\\"miles\\\", \\\"west\\\", \\\"of\\\", \\\"the\\\", \\\"City\\\", \\\"of\\\", \\\"Sweetwater\\\", \\\",\\\", \\\"which\\\", \\\"owns\\\", \\\"it\\\", \\\".\\\"], \\\"h\\\": [\\\"avenger field\\\", \\\"Q2901599\\\", [[0, 1]]], \\\"t\\\": [\\\"city of sweetwater\\\", \\\"Q981845\\\", [[15, 16, 17]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"United\\\", \\\"States\\\", \\\"Air\\\", \\\"Force\\\", \\\"named\\\", \\\"a\\\", \\\"street\\\", \\\"in\\\", \\\"honor\\\", \\\"of\\\", \\\"Mock\\\", \\\"at\\\", \\\"Rickenbacker\\\", \\\"AFB\\\", \\\"(\\\", \\\"presently\\\", \\\"Rickenbacker\\\", \\\"Air\\\", \\\"National\\\", \\\"Guard\\\", \\\"Base\\\", \\\"and\\\", \\\"Rickenbacker\\\", \\\"International\\\", \\\"Airport\\\", \\\")\\\", \\\"in\\\", \\\"Lockbourne\\\", \\\",\\\", \\\"Ohio\\\", \\\"(\\\", \\\"near\\\", \\\"Columbus\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"rickenbacker international airport\\\", \\\"Q1432595\\\", [[23, 24, 25]]], \\\"t\\\": [\\\"columbus\\\", \\\"Q16567\\\", [[33]]]}, {\\\"tokens\\\": [\\\"Landing\\\", \\\"and\\\", \\\"take\\\", \\\"-\\\", \\\"off\\\", \\\"operations\\\", \\\"in\\\", \\\"the\\\", \\\"airport\\\", \\\"are\\\", \\\"carried\\\", \\\"out\\\", \\\"by\\\", \\\"Itaituba\\\", \\\"Air\\\", \\\"Navigation\\\", \\\"Group\\\", \\\"(\\\", \\\"GNA\\\", \\\"III\\\", \\\"-\\\", \\\"SBIH\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"sbih\\\", \\\"Q2902444\\\", [[21]]], \\\"t\\\": [\\\"itaituba\\\", \\\"Q655734\\\", [[13]]]}, {\\\"tokens\\\": [\\\"Iberia\\\", \\\"Airlines\\\", \\\"Flight\\\", \\\"401\\\", \\\"was\\\", \\\"a\\\", \\\"routine\\\", \\\"flight\\\", \\\"from\\\", \\\"Madrid\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Spain\\\", \\\"to\\\", \\\"Los\\\", \\\"Rodeos\\\", \\\"Airport\\\", \\\"in\\\", \\\"Tenerife\\\", \\\".\\\"], \\\"h\\\": [\\\"los rodeos airport\\\", \\\"Q932514\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"tenerife\\\", \\\"Q40846\\\", [[19]]]}, {\\\"tokens\\\": [\\\"Lake\\\", \\\"Cumberland\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Pulaski\\\", \\\"County\\\", \\\",\\\", \\\"on\\\", \\\"the\\\", \\\"southern\\\", \\\"end\\\", \\\"of\\\", \\\"Somerset\\\", \\\"'s\\\", \\\"US\\\", \\\"27\\\", \\\"business\\\", \\\"district\\\", \\\".\\\"], \\\"h\\\": [\\\"lake cumberland regional airport\\\", \\\"Q10853391\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"somerset\\\", \\\"Q2303714\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Services\\\", \\\"to\\\", \\\"the\\\", \\\"island\\\", \\\"run\\\", \\\"from\\\", \\\"San\\\", \\\"Juan\\\", \\\"'s\\\", \\\"Luis\\\", \\\"Mu\\\\u00f1oz\\\", \\\"Mar\\\\u00edn\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Ceiba\\\", \\\"Airport\\\", \\\"or\\\", \\\"Isla\\\", \\\"Grande\\\", \\\"Airport\\\", \\\"(\\\", \\\"20-\\\", \\\"to\\\", \\\"30-minute\\\", \\\"flight\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"isla grande airport\\\", \\\"Q5444795\\\", [[18, 19, 20]]], \\\"t\\\": [\\\"san juan\\\", \\\"Q41211\\\", [[6, 7]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"1\\\", \\\"-\\\", \\\"24\\\", \\\"was\\\", \\\"substantially\\\", \\\"damaged\\\", \\\"on\\\", \\\"25\\\", \\\"May\\\", \\\"1996\\\", \\\"at\\\", \\\"landing\\\", \\\"at\\\", \\\"the\\\", \\\"Mountain\\\", \\\"Valley\\\", \\\"Airport\\\", \\\",\\\", \\\"Tehachapi\\\", \\\",\\\", \\\"California\\\", \\\"when\\\", \\\"it\\\", \\\"collided\\\", \\\"with\\\", \\\"two\\\", \\\"other\\\", \\\"parked\\\", \\\"gliders\\\", \\\".\\\"], \\\"h\\\": [\\\"mountain valley airport\\\", \\\"Q3886257\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"tehachapi, california\\\", \\\"Q985253\\\", [[19, 20, 21]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"two\\\", \\\"highways\\\", \\\"continue\\\", \\\"northeast\\\", \\\"through\\\", \\\"Washington\\\", \\\"County\\\", \\\",\\\", \\\"where\\\", \\\"they\\\", \\\"pass\\\", \\\"Virginia\\\", \\\"Highlands\\\", \\\"Airport\\\", \\\"before\\\", \\\"entering\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"Abingdon\\\", \\\".\\\"], \\\"h\\\": [\\\"virginia highlands airport\\\", \\\"Q7934312\\\", [[12, 13, 14]]], \\\"t\\\": [\\\"abingdon\\\", \\\"Q137919\\\", [[20]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airport\\\", \\\"of\\\", \\\"B\\\\u00e9char\\\", \\\",\\\", \\\"Boudghene\\\", \\\"Ben\\\", \\\"Ali\\\", \\\"Lotfi\\\", \\\"Airport\\\", \\\"was\\\", \\\"named\\\", \\\"after\\\", \\\"him\\\", \\\".\\\"], \\\"h\\\": [\\\"boudghene ben ali lotfi airport\\\", \\\"Q2875808\\\", [[5, 6, 7, 8, 9]]], \\\"t\\\": [\\\"b\\\\u00e9char\\\", \\\"Q638704\\\", [[3]]]}, {\\\"tokens\\\": [\\\"Debre\\\", \\\"Marqos\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"an\\\", \\\"airport\\\", \\\"(\\\", \\\"ICAO\\\", \\\"code\\\", \\\"HADM\\\", \\\",\\\", \\\"IATA\\\", \\\"DBM\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q2875819\\\", [[6]]], \\\"t\\\": [\\\"debre marqos\\\", \\\"Q1024659\\\", [[0, 1]]]}, {\\\"tokens\\\": [\\\"After\\\", \\\"becoming\\\", \\\"airborne\\\", \\\"from\\\", \\\"Germ\\\\u00e1n\\\", \\\"Olano\\\", \\\"Airport\\\", \\\"Puerto\\\", \\\"Carre\\\\u00f1o\\\", \\\",\\\", \\\"Colombia\\\", \\\"it\\\", \\\"remained\\\", \\\"at\\\", \\\"very\\\", \\\"low\\\", \\\"altitude\\\", \\\"and\\\", \\\"crashed\\\", \\\"shortly\\\", \\\"afterwards\\\", \\\".\\\"], \\\"h\\\": [\\\"germ\\\\u00e1n olano airport\\\", \\\"Q1323338\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"puerto carre\\\\u00f1o\\\", \\\"Q130304\\\", [[7, 8]]]}, {\\\"tokens\\\": [\\\"Puerto\\\", \\\"Legu\\\\u00edzamo\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Caucay\\\\u00e1\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"caucay\\\\u00e1 airport\\\", \\\"Q1962669\\\", [[5, 6]]], \\\"t\\\": [\\\"puerto legu\\\\u00edzamo\\\", \\\"Q1525407\\\", [[0, 1]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Great\\\", \\\"State\\\", \\\"of\\\", \\\"Maine\\\", \\\"Air\\\", \\\"Show\\\", \\\"is\\\", \\\"an\\\", \\\"airshow\\\", \\\"held\\\", \\\"in\\\", \\\"August\\\", \\\"at\\\", \\\"Brunswick\\\", \\\"Executive\\\", \\\"Airport\\\", \\\"in\\\", \\\"Brunswick\\\", \\\",\\\", \\\"Maine\\\", \\\".\\\"], \\\"h\\\": [\\\"brunswick executive airport\\\", \\\"Q3886398\\\", [[14, 15, 16]]], \\\"t\\\": [\\\"brunswick, maine\\\", \\\"Q518466\\\", [[18, 19, 20]]]}, {\\\"tokens\\\": [\\\"To\\\", \\\"boost\\\", \\\"the\\\", \\\"twin\\\", \\\"town\\\", \\\"relationship\\\", \\\"with\\\", \\\"Zamboanga\\\", \\\"City\\\", \\\"and\\\", \\\"for\\\", \\\"the\\\", \\\"ASEAN\\\", \\\"spirit\\\", \\\"in\\\", \\\"the\\\", \\\"BIMP\\\", \\\"-\\\", \\\"EAGA\\\", \\\"region\\\", \\\",\\\", \\\"there\\\", \\\"is\\\", \\\"an\\\", \\\"international\\\", \\\"route\\\", \\\"from\\\", \\\"Sandakan\\\", \\\"to\\\", \\\"Zamboanga\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"zamboanga international airport\\\", \\\"Q1200033\\\", [[29, 30, 31]]], \\\"t\\\": [\\\"zamboanga city\\\", \\\"Q1629\\\", [[7, 8]]]}, {\\\"tokens\\\": [\\\"Cart\\\\u00ed\\\", \\\"Sugtupu\\\", \\\"can\\\", \\\"be\\\", \\\"reached\\\", \\\"by\\\", \\\"boat\\\", \\\"from\\\", \\\"the\\\", \\\"nearby\\\", \\\"onshore\\\", \\\"settlement\\\", \\\"of\\\", \\\"Carti\\\", \\\"and\\\", \\\"the\\\", \\\"Carti\\\", \\\"Airstrip\\\", \\\",\\\", \\\"which\\\", \\\"both\\\", \\\"are\\\", \\\"connected\\\", \\\"to\\\", \\\"the\\\", \\\"main\\\", \\\"Panamanian\\\", \\\"road\\\", \\\"network\\\", \\\".\\\"], \\\"h\\\": [\\\"carti airstrip\\\", \\\"Q19460881\\\", [[16, 17]]], \\\"t\\\": [\\\"cart\\\\u00ed sugtupu\\\", \\\"Q636822\\\", [[0, 1]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"couple\\\", \\\"then\\\", \\\"flew\\\", \\\"to\\\", \\\"Yellowknife\\\", \\\"Airport\\\", \\\",\\\", \\\"Yellowknife\\\", \\\",\\\", \\\"Northwest\\\", \\\"Territories\\\", \\\"arriving\\\", \\\"in\\\", \\\"the\\\", \\\"early\\\", \\\"evening\\\", \\\".\\\"], \\\"h\\\": [\\\"yellowknife airport\\\", \\\"Q2724008\\\", [[5, 6]]], \\\"t\\\": [\\\"yellowknife, northwest territories\\\", \\\"Q2061\\\", [[8, 9, 10, 11]]]}, {\\\"tokens\\\": [\\\"Tallman\\\", \\\"East\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"private\\\", \\\"airport\\\", \\\"in\\\", \\\"Tower\\\", \\\"City\\\", \\\",\\\", \\\"Pennsylvania\\\", \\\".\\\"], \\\"h\\\": [\\\"tallman east airport\\\", \\\"Q7680162\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"tower city, pennsylvania\\\", \\\"Q1187340\\\", [[8, 9, 10, 11]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"located\\\", \\\"at\\\", \\\"what\\\", \\\"is\\\", \\\"now\\\", \\\"the\\\", \\\"Erik\\\", \\\"Nielsen\\\", \\\"Whitehorse\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Whitehorse\\\", \\\",\\\", \\\"Yukon\\\", \\\".\\\"], \\\"h\\\": [\\\"erik nielsen whitehorse international airport\\\", \\\"Q1433251\\\", [[8, 9, 10, 11, 12]]], \\\"t\\\": [\\\"whitehorse, yukon\\\", \\\"Q2058\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"village\\\", \\\"is\\\", \\\"from\\\", \\\"Sri\\\", \\\"Guru\\\", \\\"Ram\\\", \\\"Dass\\\", \\\"Jee\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Amritsar\\\", \\\";\\\", \\\"the\\\", \\\"nearest\\\", \\\"airport\\\", \\\"is\\\", \\\"Sahnewal\\\", \\\"Airport\\\", \\\"in\\\", \\\"Ludhiana\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"located\\\", \\\"distant\\\", \\\".\\\"], \\\"h\\\": [\\\"sahnewal airport\\\", \\\"Q7399709\\\", [[18, 19]]], \\\"t\\\": [\\\"ludhiana\\\", \\\"Q200123\\\", [[21]]]}, {\\\"tokens\\\": [\\\"He\\\", \\\"was\\\", \\\"not\\\", \\\"aboard\\\", \\\"the\\\", \\\"airplane\\\", \\\"that\\\", \\\"crashed\\\", \\\"in\\\", \\\"Tunoshna\\\", \\\"Airport\\\", \\\"near\\\", \\\"Yaroslavl\\\", \\\"on\\\", \\\"7\\\", \\\"September\\\", \\\"2011\\\", \\\".\\\"], \\\"h\\\": [\\\"tunoshna airport\\\", \\\"Q1147420\\\", [[9, 10]]], \\\"t\\\": [\\\"yaroslavl\\\", \\\"Q2423\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Commodore\\\", \\\"Decatur\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"closed\\\", \\\"airport\\\", \\\"located\\\", \\\"2\\\", \\\"miles\\\", \\\"west\\\", \\\"-\\\", \\\"northwest\\\", \\\"of\\\", \\\"Bainbridge\\\", \\\",\\\", \\\"Georgia\\\", \\\".\\\"], \\\"h\\\": [\\\"commodore decatur airport\\\", \\\"Q5153221\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"bainbridge, georgia\\\", \\\"Q788794\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"La\\\", \\\"Florida\\\", \\\"Airport\\\", \\\"serves\\\", \\\"Tumaco\\\", \\\"with\\\", \\\"flights\\\", \\\"from\\\", \\\"Cali\\\", \\\".\\\"], \\\"h\\\": [\\\"la florida airport\\\", \\\"Q1977854\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"tumaco\\\", \\\"Q1005555\\\", [[4]]]}, {\\\"tokens\\\": [\\\"Sharp\\\", \\\"Airlines\\\", \\\"started\\\", \\\"in\\\", \\\"Portland\\\", \\\"by\\\", \\\"flying\\\", \\\"staff\\\", \\\"and\\\", \\\"employees\\\", \\\"from\\\", \\\"Portland\\\", \\\"Aluminium\\\", \\\"to\\\", \\\"Avalon\\\", \\\"Airport\\\", \\\",\\\", \\\"so\\\", \\\"they\\\", \\\"could\\\", \\\"link\\\", \\\"to\\\", \\\"the\\\", \\\"Point\\\", \\\"Henry\\\", \\\"Smelter\\\", \\\"near\\\", \\\"Geelong\\\", \\\".\\\"], \\\"h\\\": [\\\"avalon airport\\\", \\\"Q17896\\\", [[14, 15]]], \\\"t\\\": [\\\"geelong\\\", \\\"Q231765\\\", [[27]]]}, {\\\"tokens\\\": [\\\"Central\\\", \\\"Arkansas\\\", \\\"also\\\", \\\"has\\\", \\\"several\\\", \\\"smaller\\\", \\\"municipally\\\", \\\"owned\\\", \\\"general\\\", \\\"aviation\\\", \\\"airports\\\", \\\",\\\", \\\"including\\\", \\\"Conway\\\", \\\"Airport\\\", \\\"at\\\", \\\"Cantrell\\\", \\\"Field\\\", \\\"in\\\", \\\"Conway\\\", \\\",\\\", \\\"Saline\\\", \\\"County\\\", \\\"Regional\\\", \\\"in\\\", \\\"Benton\\\", \\\",\\\", \\\"and\\\", \\\"Grider\\\", \\\"Field\\\", \\\"in\\\", \\\"Pine\\\", \\\"Bluff\\\", \\\".\\\"], \\\"h\\\": [\\\"grider field\\\", \\\"Q5608629\\\", [[28, 29]]], \\\"t\\\": [\\\"pine bluff\\\", \\\"Q80012\\\", [[31, 32]]]}, {\\\"tokens\\\": [\\\"Moyne\\\", \\\"Aerodrome\\\", \\\"is\\\", \\\"an\\\", \\\"aerodrome\\\", \\\"situated\\\", \\\"north\\\", \\\"east\\\", \\\"of\\\", \\\"Thurles\\\", \\\",\\\", \\\"County\\\", \\\"Tipperary\\\", \\\"in\\\", \\\"Ireland\\\", \\\".\\\"], \\\"h\\\": [\\\"moyne aerodrome\\\", \\\"Q3886239\\\", [[0, 1]]], \\\"t\\\": [\\\"thurles\\\", \\\"Q383188\\\", [[9]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"new\\\", \\\"carrier\\\", \\\",\\\", \\\"announced\\\", \\\"in\\\", \\\"2015\\\", \\\",\\\", \\\"would\\\", \\\"be\\\", \\\"based\\\", \\\"at\\\", \\\"Senai\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Johor\\\", \\\"with\\\", \\\"a\\\", \\\"secondary\\\", \\\"hub\\\", \\\"at\\\", \\\"Kota\\\", \\\"Kinabalu\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Sabah\\\", \\\".\\\"], \\\"h\\\": [\\\"senai international airport\\\", \\\"Q3239110\\\", [[12, 13, 14]]], \\\"t\\\": [\\\"johor\\\", \\\"Q183032\\\", [[16]]]}, {\\\"tokens\\\": [\\\"Aktau\\\", \\\"has\\\", \\\"an\\\", \\\"international\\\", \\\"airport\\\", \\\",\\\", \\\"a\\\", \\\"railway\\\", \\\"station\\\", \\\",\\\", \\\"and\\\", \\\"a\\\", \\\"developed\\\", \\\"seaport\\\", \\\".\\\"], \\\"h\\\": [\\\"international airport\\\", \\\"Q1430826\\\", [[3, 4]]], \\\"t\\\": [\\\"aktau\\\", \\\"Q198989\\\", [[0]]]}, {\\\"tokens\\\": [\\\"LKVO\\\", \\\"is\\\", \\\"located\\\", \\\"15\\\", \\\"km\\\", \\\"North\\\", \\\"-\\\", \\\"West\\\", \\\"from\\\", \\\"the\\\", \\\"Capital\\\", \\\"of\\\", \\\"Prague\\\", \\\".\\\"], \\\"h\\\": [\\\"lkvo\\\", \\\"Q3487271\\\", [[0]]], \\\"t\\\": [\\\"prague\\\", \\\"Q1085\\\", [[12]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"show\\\", \\\"was\\\", \\\"filmed\\\", \\\"primarily\\\", \\\"at\\\", \\\"Northwest\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Roanoke\\\", \\\",\\\", \\\"Texas\\\", \\\".\\\"], \\\"h\\\": [\\\"northwest regional airport\\\", \\\"Q7060183\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"roanoke, texas\\\", \\\"Q969223\\\", [[10, 11, 12]]]}, {\\\"tokens\\\": [\\\"Arizona\\\", \\\"Helicopters\\\", \\\"was\\\", \\\"originally\\\", \\\"based\\\", \\\"out\\\", \\\"of\\\", \\\"Chandler\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"in\\\", \\\"Chandler\\\", \\\",\\\", \\\"Arizona\\\", \\\"and\\\", \\\"then\\\", \\\"moved\\\", \\\"to\\\", \\\"Scottsdale\\\", \\\"Airport\\\", \\\"in\\\", \\\"Scottsdale\\\", \\\",\\\", \\\"Arizona\\\", \\\".\\\"], \\\"h\\\": [\\\"scottsdale airport\\\", \\\"Q17567\\\", [[18, 19]]], \\\"t\\\": [\\\"scottsdale, arizona\\\", \\\"Q49221\\\", [[21, 22, 23]]]}, {\\\"tokens\\\": [\\\"Port\\\", \\\"Townsend\\\", \\\"Aero\\\", \\\"Museum\\\", \\\"is\\\", \\\"an\\\", \\\"aviation\\\", \\\"museum\\\", \\\"located\\\", \\\"at\\\", \\\"Jefferson\\\", \\\"County\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Port\\\", \\\"Townsend\\\", \\\",\\\", \\\"Washington\\\", \\\".\\\"], \\\"h\\\": [\\\"jefferson county international airport\\\", \\\"Q2902617\\\", [[10, 11, 12, 13]]], \\\"t\\\": [\\\"port townsend, washington\\\", \\\"Q1001828\\\", [[15, 16, 17, 18]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"plane\\\", \\\"took\\\", \\\"off\\\", \\\"from\\\", \\\"Batajnica\\\", \\\"Air\\\", \\\"Base\\\", \\\"in\\\", \\\"Belgrade\\\", \\\"and\\\", \\\"was\\\", \\\"en\\\", \\\"route\\\", \\\"to\\\", \\\"Sarajevo\\\", \\\"when\\\", \\\"it\\\", \\\"crashed\\\", \\\",\\\", \\\"ostensibly\\\", \\\"due\\\", \\\"to\\\", \\\"poor\\\", \\\"weather\\\", \\\"conditions\\\", \\\".\\\"], \\\"h\\\": [\\\"batajnica air base\\\", \\\"Q948600\\\", [[5, 6, 7]]], \\\"t\\\": [\\\"belgrade\\\", \\\"Q3711\\\", [[9]]]}, {\\\"tokens\\\": [\\\"OSU\\\", \\\"Don\\\", \\\"Scott\\\", \\\"Airport\\\", \\\"and\\\", \\\"Bolton\\\", \\\"Field\\\", \\\"are\\\", \\\"significant\\\", \\\"general\\\", \\\"-\\\", \\\"aviation\\\", \\\"facilities\\\", \\\"in\\\", \\\"the\\\", \\\"Columbus\\\", \\\"area\\\", \\\".\\\"], \\\"h\\\": [\\\"bolton field\\\", \\\"Q3886801\\\", [[5, 6]]], \\\"t\\\": [\\\"columbus\\\", \\\"Q16567\\\", [[15]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"aircraft\\\", \\\"took\\\", \\\"off\\\", \\\"from\\\", \\\"Luanda\\\", \\\"'s\\\", \\\"Quatro\\\", \\\"de\\\", \\\"Fevereiro\\\", \\\"Airport\\\", \\\"to\\\", \\\"Namibe\\\", \\\"Airport\\\", \\\",\\\", \\\"around\\\", \\\"420\\\", \\\"miles\\\", \\\"south\\\", \\\"from\\\", \\\"the\\\", \\\"capital\\\", \\\".\\\"], \\\"h\\\": [\\\"quatro de fevereiro airport\\\", \\\"Q598002\\\", [[7, 8, 9, 10]]], \\\"t\\\": [\\\"luanda\\\", \\\"Q3897\\\", [[5]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"1978\\\", \\\"a\\\", \\\"new\\\", \\\"section\\\", \\\"opened\\\", \\\",\\\", \\\"connecting\\\", \\\"former\\\", \\\"Road\\\", \\\"10\\\", \\\"(\\\", \\\"the\\\", \\\"Tel\\\", \\\"Aviv\\\", \\\"\\\\u2013\\\", \\\"Ben\\\", \\\"Gurion\\\", \\\"Airport\\\", \\\"road\\\", \\\")\\\", \\\"with\\\", \\\"Sha'ar\\\", \\\"HaGai\\\", \\\".\\\"], \\\"h\\\": [\\\"ben gurion airport\\\", \\\"Q181479\\\", [[16, 17, 18]]], \\\"t\\\": [\\\"tel aviv\\\", \\\"Q33935\\\", [[13, 14]]]}, {\\\"tokens\\\": [\\\"Snowden\\\", \\\"manages\\\", \\\"to\\\", \\\"depart\\\", \\\"from\\\", \\\"Hong\\\", \\\"Kong\\\", \\\",\\\", \\\"but\\\", \\\"his\\\", \\\"US\\\", \\\"passport\\\", \\\"is\\\", \\\"cancelled\\\", \\\"before\\\", \\\"he\\\", \\\"can\\\", \\\"connect\\\", \\\"to\\\", \\\"Havana\\\", \\\",\\\", \\\"stranding\\\", \\\"him\\\", \\\"in\\\", \\\"the\\\", \\\"Sheremetyevo\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Moscow\\\", \\\".\\\"], \\\"h\\\": [\\\"sheremetyevo international airport\\\", \\\"Q192733\\\", [[25, 26, 27]]], \\\"t\\\": [\\\"moscow\\\", \\\"Q649\\\", [[29]]]}, {\\\"tokens\\\": [\\\"Perry\\\", \\\"County\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Perry\\\", \\\"County\\\", \\\"Airport\\\", \\\"near\\\", \\\"Linden\\\", \\\".\\\"], \\\"h\\\": [\\\"perry county airport\\\", \\\"Q7169748\\\", [[5, 6, 7]]], \\\"t\\\": [\\\"linden\\\", \\\"Q2607529\\\", [[9]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"also\\\", \\\"has\\\", \\\"offices\\\", \\\"in\\\", \\\"Marsh\\\", \\\"Harbour\\\", \\\"Abaco\\\", \\\"Airport\\\", \\\",\\\", \\\"in\\\", \\\"Bimini\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"and\\\", \\\"in\\\", \\\"the\\\", \\\"Lynden\\\", \\\"Pindling\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Nassau\\\", \\\".\\\"], \\\"h\\\": [\\\"lynden pindling international airport\\\", \\\"Q1415006\\\", [[18, 19, 20, 21]]], \\\"t\\\": [\\\"nassau\\\", \\\"Q2467\\\", [[23]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Aviation\\\", \\\"Section\\\", \\\"maintains\\\", \\\"a\\\", \\\"base\\\", \\\"24\\\", \\\"hours\\\", \\\"per\\\", \\\"day\\\", \\\"at\\\", \\\"Long\\\", \\\"Island\\\", \\\"MacArthur\\\", \\\"Airport\\\", \\\"in\\\", \\\"Ronkonkoma\\\", \\\"and\\\", \\\"16\\\", \\\"hours\\\", \\\"per\\\", \\\"day\\\", \\\"at\\\", \\\"Gabreski\\\", \\\"Airport\\\", \\\"in\\\", \\\"Westhampton\\\", \\\"Beach\\\", \\\".\\\"], \\\"h\\\": [\\\"gabreski airport\\\", \\\"Q5482369\\\", [[23, 24]]], \\\"t\\\": [\\\"westhampton beach\\\", \\\"Q3453197\\\", [[26, 27]]]}, {\\\"tokens\\\": [\\\"Continental\\\", \\\"Airlines\\\", \\\"used\\\", \\\"to\\\", \\\"serve\\\", \\\"the\\\", \\\"Brackettville/\\\", \\\"Kinney\\\", \\\"County\\\", \\\"area\\\", \\\"via\\\", \\\"Del\\\", \\\"Rio\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Del\\\", \\\"Rio\\\", \\\",\\\", \\\"Texas\\\", \\\".\\\"], \\\"h\\\": [\\\"del rio international airport\\\", \\\"Q1657383\\\", [[11, 12, 13, 14]]], \\\"t\\\": [\\\"del rio, texas\\\", \\\"Q970792\\\", [[16, 17, 18, 19]]]}, {\\\"tokens\\\": [\\\"Cubana\\\", \\\"de\\\", \\\"Aviaci\\\\u00f3n\\\", \\\"Flight\\\", \\\"1216\\\", \\\"was\\\", \\\"a\\\", \\\"McDonnell\\\", \\\"Douglas\\\", \\\"DC-10\\\", \\\"that\\\", \\\"overran\\\", \\\"the\\\", \\\"runway\\\", \\\"at\\\", \\\"La\\\", \\\"Aurora\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Guatemala\\\", \\\"City\\\", \\\",\\\", \\\"on\\\", \\\"21\\\", \\\"December\\\", \\\"1999\\\", \\\".\\\"], \\\"h\\\": [\\\"la aurora international airport\\\", \\\"Q765608\\\", [[15, 16, 17, 18]]], \\\"t\\\": [\\\"guatemala city\\\", \\\"Q1555\\\", [[20, 21]]]}, {\\\"tokens\\\": [\\\"Havryshivka\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\"IATA\\\", \\\":\\\", \\\"VIN\\\", \\\",\\\", \\\"ICAO\\\", \\\":\\\", \\\"UKWW\\\", \\\")\\\", \\\"is\\\", \\\"situated\\\", \\\"near\\\", \\\"Vinnytsia\\\", \\\".\\\"], \\\"h\\\": [\\\"ukww\\\", \\\"Q4111595\\\", [[10]]], \\\"t\\\": [\\\"vinnytsia\\\", \\\"Q157144\\\", [[15]]]}, {\\\"tokens\\\": [\\\"LA\\\", \\\"\\\\u00a0\\\", \\\"1\\\", \\\"and\\\", \\\"LA\\\", \\\"\\\\u00a0\\\", \\\"10\\\", \\\"cross\\\", \\\"the\\\", \\\"New\\\", \\\"Roads\\\", \\\"city\\\", \\\"limits\\\", \\\"just\\\", \\\"after\\\", \\\"passing\\\", \\\"the\\\", \\\"False\\\", \\\"River\\\", \\\"Regional\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"false river regional airport\\\", \\\"Q5432665\\\", [[17, 18, 19, 20]]], \\\"t\\\": [\\\"new roads\\\", \\\"Q2276773\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"Upon\\\", \\\"its\\\", \\\"completion\\\", \\\",\\\", \\\"it\\\", \\\"was\\\", \\\"one\\\", \\\"of\\\", \\\"two\\\", \\\"major\\\", \\\"airfields\\\", \\\"in\\\", \\\"the\\\", \\\"Hanoi\\\", \\\"area\\\", \\\",\\\", \\\"the\\\", \\\"other\\\", \\\"being\\\", \\\"the\\\", \\\"(\\\", \\\"now\\\", \\\"-\\\", \\\"disused\\\", \\\")\\\", \\\"Bach\\\", \\\"Mai\\\", \\\"Airfield\\\", \\\".\\\"], \\\"h\\\": [\\\"bach mai airfield\\\", \\\"Q2886528\\\", [[25, 26, 27]]], \\\"t\\\": [\\\"hanoi\\\", \\\"Q1858\\\", [[13]]]}, {\\\"tokens\\\": [\\\"Shenandoah\\\", \\\"Valley\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"began\\\", \\\"free\\\", \\\"bus\\\", \\\"service\\\", \\\"between\\\", \\\"the\\\", \\\"airport\\\", \\\"and\\\", \\\"Harrisonburg\\\", \\\",\\\", \\\"Staunton\\\", \\\",\\\", \\\"and\\\", \\\"Waynesboro\\\", \\\"in\\\", \\\"March\\\", \\\"2004\\\", \\\".\\\"], \\\"h\\\": [\\\"shenandoah valley regional airport\\\", \\\"Q7494187\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"staunton\\\", \\\"Q502250\\\", [[14]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearby\\\", \\\"village\\\", \\\"of\\\", \\\"Long\\\", \\\"Banga\\\", \\\"is\\\", \\\"about\\\", \\\"four\\\", \\\"hour\\\\u2019\\\", \\\"walk\\\", \\\"away\\\", \\\",\\\", \\\"and\\\", \\\"has\\\", \\\"an\\\", \\\"airport\\\", \\\"and\\\", \\\"a\\\", \\\"clinic\\\", \\\"that\\\", \\\"serves\\\", \\\"the\\\", \\\"surrounding\\\", \\\"villages\\\", \\\"including\\\", \\\"Long\\\", \\\"Peluan\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q3503051\\\", [[16]]], \\\"t\\\": [\\\"long banga\\\", \\\"Q6672234\\\", [[4, 5]]]}, {\\\"tokens\\\": [\\\"There\\\", \\\"is\\\", \\\"an\\\", \\\"unscheduled\\\", \\\"and\\\", \\\"unused\\\", \\\"airport\\\", \\\"with\\\", \\\"a\\\", \\\"grass\\\", \\\"runway\\\", \\\"in\\\", \\\"Brei\\\\u00f0dalsv\\\\u00edk\\\", \\\",\\\", \\\"20\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\"(\\\", \\\"12\\\", \\\"\\\\u00a0\\\", \\\"mi\\\", \\\")\\\", \\\"from\\\", \\\"St\\\\u00f6\\\\u00f0varfj\\\\u00f6r\\\\u00f0ur\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q12692021\\\", [[6]]], \\\"t\\\": [\\\"brei\\\\u00f0dalsv\\\\u00edk\\\", \\\"Q2924383\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Located\\\", \\\"in\\\", \\\"the\\\", \\\"middle\\\", \\\"of\\\", \\\"the\\\", \\\"Melbourne\\\", \\\"Yard\\\", \\\"precinct\\\", \\\"in\\\", \\\"the\\\", \\\"suburb\\\", \\\"West\\\", \\\"Melbourne\\\", \\\"near\\\", \\\"North\\\", \\\"Melbourne\\\", \\\"station\\\", \\\",\\\", \\\"the\\\", \\\"site\\\", \\\"is\\\", \\\"now\\\", \\\"occupied\\\", \\\"by\\\", \\\"the\\\", \\\"Melbourne\\\", \\\"Steel\\\", \\\"Terminal\\\", \\\".\\\"], \\\"h\\\": [\\\"north melbourne station\\\", \\\"Q7056082\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"west melbourne\\\", \\\"Q12010545\\\", [[12, 13]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"also\\\", \\\"planned\\\", \\\"to\\\", \\\"convert\\\", \\\"and\\\", \\\"electrify\\\", \\\"the\\\", \\\"28\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\"Sassari\\\", \\\"-\\\", \\\"Alghero\\\", \\\"railway\\\", \\\"to\\\", \\\"allow\\\", \\\"the\\\", \\\"trams\\\", \\\"to\\\", \\\"reach\\\", \\\"the\\\", \\\"village\\\", \\\"of\\\", \\\"Olmedo\\\", \\\",\\\", \\\"Fertilia\\\", \\\"Airport\\\", \\\"and\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"Alghero\\\", \\\".\\\"], \\\"h\\\": [\\\"fertilia airport\\\", \\\"Q1321390\\\", [[27, 28]]], \\\"t\\\": [\\\"alghero\\\", \\\"Q166282\\\", [[14], [33]]]}, {\\\"tokens\\\": [\\\"Ashgabat\\\", \\\"has\\\", \\\"a\\\", \\\"modern\\\", \\\"international\\\", \\\"airport\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"the\\\", \\\"base\\\", \\\"of\\\", \\\"Turkmenistan\\\", \\\"Airlines\\\", \\\".\\\"], \\\"h\\\": [\\\"international airport\\\", \\\"Q1148527\\\", [[4, 5]]], \\\"t\\\": [\\\"ashgabat\\\", \\\"Q23438\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Aexpa\\\", \\\"S.A.\\\", \\\"is\\\", \\\"a\\\", \\\"charter\\\", \\\"airline\\\", \\\"based\\\", \\\"at\\\", \\\"Mateca\\\\u00f1a\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Pereira\\\", \\\",\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"mateca\\\\u00f1a international airport\\\", \\\"Q381688\\\", [[8, 9, 10]]], \\\"t\\\": [\\\"pereira\\\", \\\"Q51111\\\", [[12]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"26\\\", \\\"June\\\", \\\"2010\\\", \\\"the\\\", \\\"first\\\", \\\"batch\\\", \\\"of\\\", \\\"3\\\", \\\"F-16C\\\", \\\"/\\\", \\\"D\\\", \\\"Block\\\", \\\"52\\\", \\\"+\\\", \\\"fighters\\\", \\\"were\\\", \\\"delivered\\\", \\\"to\\\", \\\"PAF\\\", \\\"Base\\\", \\\"Shahbaz\\\", \\\",\\\", \\\"Jacobabad\\\", \\\".\\\"], \\\"h\\\": [\\\"paf base shahbaz\\\", \\\"Q3694521\\\", [[19, 20, 21]]], \\\"t\\\": [\\\"jacobabad\\\", \\\"Q1017696\\\", [[23]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Germans\\\", \\\"had\\\", \\\"captured\\\", \\\"the\\\", \\\"airfield\\\", \\\"\\\\\\\"\\\", \\\"Waalhaven\\\", \\\"\\\\\\\"\\\", \\\"in\\\", \\\"Rotterdam\\\", \\\"and\\\", \\\"\\\\\\\"\\\", \\\"Van\\\", \\\"Galen\\\", \\\"\\\\\\\"\\\", \\\"was\\\", \\\"ordered\\\", \\\"to\\\", \\\"bombard\\\", \\\"the\\\", \\\"airfield\\\", \\\".\\\"], \\\"h\\\": [\\\"waalhaven\\\", \\\"Q2262149\\\", [[7]]], \\\"t\\\": [\\\"rotterdam\\\", \\\"Q34370\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Southern\\\", \\\"North\\\", \\\"Sea\\\", \\\"services\\\", \\\"operate\\\", \\\"from\\\", \\\"Norwich\\\", \\\"(\\\", \\\"EGSH\\\", \\\")\\\", \\\",\\\", \\\"Humberside\\\", \\\"(\\\", \\\"EGNJ\\\", \\\")\\\", \\\"and\\\", \\\"Den\\\", \\\"Helder\\\", \\\"(\\\", \\\"EHKD\\\", \\\")\\\", \\\"with\\\", \\\"its\\\", \\\"support\\\", \\\"organisation\\\", \\\"based\\\", \\\"at\\\", \\\"Redhill\\\", \\\"(\\\", \\\"EGKR\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"egsh\\\", \\\"Q349673\\\", [[8]]], \\\"t\\\": [\\\"norwich\\\", \\\"Q130191\\\", [[6]]]}, {\\\"tokens\\\": [\\\"Kuwait\\\", \\\"City\\\", \\\"'s\\\", \\\"trade\\\", \\\"and\\\", \\\"transportation\\\", \\\"needs\\\", \\\"are\\\", \\\"served\\\", \\\"by\\\", \\\"Kuwait\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Mina\\\", \\\"Al\\\", \\\"-\\\", \\\"Shuwaik\\\", \\\"(\\\", \\\"Shuwaik\\\", \\\"Port\\\", \\\")\\\", \\\"and\\\", \\\"Mina\\\", \\\"Al\\\", \\\"Ahmadi\\\", \\\"(\\\", \\\"Ahmadi\\\", \\\"Port\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"kuwait international airport\\\", \\\"Q527157\\\", [[10, 11, 12]]], \\\"t\\\": [\\\"kuwait city\\\", \\\"Q35178\\\", [[0, 1]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"had\\\", \\\"been\\\", \\\"recorded\\\", \\\"at\\\", \\\"the\\\", \\\"band\\\", \\\"'s\\\", \\\"performance\\\", \\\"on\\\", \\\"8\\\", \\\"May\\\", \\\"1993\\\", \\\"at\\\", \\\"the\\\", \\\"Barker\\\", \\\"Hangar\\\", \\\"at\\\", \\\"Santa\\\", \\\"Monica\\\", \\\"Airport\\\", \\\"in\\\", \\\"Southern\\\", \\\"California\\\", \\\".\\\"], \\\"h\\\": [\\\"santa monica airport\\\", \\\"Q7419789\\\", [[18, 19, 20]]], \\\"t\\\": [\\\"southern california\\\", \\\"Q844837\\\", [[22, 23]]]}, {\\\"tokens\\\": [\\\"Santiago\\\", \\\"Vila\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Girardot\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"the\\\", \\\"Cundinamarca\\\", \\\"Department\\\", \\\"of\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"santiago vila airport\\\", \\\"Q5242807\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"girardot\\\", \\\"Q186193\\\", [[9]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"first\\\", \\\"use\\\", \\\"of\\\", \\\"Boreham\\\", \\\"airfield\\\", \\\"was\\\", \\\"by\\\", \\\"the\\\", \\\"394th\\\", \\\"Bombardment\\\", \\\"Group\\\", \\\",\\\", \\\"arriving\\\", \\\"from\\\", \\\"Kellogg\\\", \\\"AAF\\\", \\\",\\\", \\\"near\\\", \\\"Battle\\\", \\\"Creek\\\", \\\",\\\", \\\"Michigan\\\", \\\"on\\\", \\\"10\\\", \\\"March\\\", \\\"1944\\\", \\\".\\\"], \\\"h\\\": [\\\"kellogg aaf\\\", \\\"Q7945760\\\", [[15, 16]]], \\\"t\\\": [\\\"battle creek, michigan\\\", \\\"Q810998\\\", [[19, 20, 21, 22]]]}, {\\\"tokens\\\": [\\\"There\\\", \\\"are\\\", \\\"five\\\", \\\"primary\\\", \\\"commercial\\\", \\\"airports\\\", \\\"serving\\\", \\\"Moscow\\\", \\\":\\\", \\\"Sheremetyevo\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Domodedovo\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Bykovo\\\", \\\"Airport\\\", \\\",\\\", \\\"Zhukovsky\\\", \\\"International\\\", \\\"Airport\\\", \\\"and\\\", \\\"Vnukovo\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"bykovo airport\\\", \\\"Q1432096\\\", [[17, 18]]], \\\"t\\\": [\\\"moscow\\\", \\\"Q649\\\", [[7]]]}, {\\\"tokens\\\": [\\\"There\\\", \\\"are\\\", \\\"helicopter\\\", \\\"flights\\\", \\\"for\\\", \\\"passengers\\\", \\\",\\\", \\\"from\\\", \\\"the\\\", \\\"Ugolny\\\", \\\"Airport\\\", \\\"in\\\", \\\"Anadyr\\\", \\\",\\\", \\\"operated\\\", \\\"by\\\", \\\"Chukotavia\\\", \\\".\\\"], \\\"h\\\": [\\\"ugolny airport\\\", \\\"Q1843329\\\", [[9, 10]]], \\\"t\\\": [\\\"anadyr\\\", \\\"Q7978\\\", [[12]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"island\\\", \\\"is\\\", \\\"located\\\", \\\"within\\\", \\\"Penobscot\\\", \\\"Bay\\\", \\\"about\\\", \\\"20\\\", \\\"miles\\\", \\\"east\\\", \\\"of\\\", \\\"the\\\", \\\"mainland\\\", \\\"coast\\\", \\\"and\\\", \\\"is\\\", \\\"accessible\\\", \\\"by\\\", \\\"ferry\\\", \\\"from\\\", \\\"Rockland\\\", \\\"or\\\", \\\"by\\\", \\\"air\\\", \\\"taxi\\\", \\\"from\\\", \\\"Knox\\\", \\\"County\\\", \\\"Regional\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"knox county regional airport\\\", \\\"Q6423552\\\", [[27, 28, 29, 30]]], \\\"t\\\": [\\\"rockland\\\", \\\"Q2078053\\\", [[21]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"aircraft\\\", \\\"was\\\", \\\"conducting\\\", \\\"a\\\", \\\"flight\\\", \\\"from\\\", \\\"Depati\\\", \\\"Amir\\\", \\\"Airport\\\", \\\"in\\\", \\\"Pangkal\\\", \\\"Pinang\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\"of\\\", \\\"Bangka\\\", \\\"Belitung\\\", \\\"province\\\", \\\".\\\"], \\\"h\\\": [\\\"depati amir airport\\\", \\\"Q1530683\\\", [[7, 8, 9]]], \\\"t\\\": [\\\"pangkal pinang\\\", \\\"Q8179\\\", [[11, 12]]]}, {\\\"tokens\\\": [\\\"Carlos\\\", \\\"Manuel\\\", \\\"de\\\", \\\"C\\\\u00e9spedes\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"regional\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Bayamo\\\", \\\"in\\\", \\\"the\\\", \\\"Granma\\\", \\\"Province\\\", \\\"of\\\", \\\"Cuba\\\", \\\".\\\"], \\\"h\\\": [\\\"carlos manuel de c\\\\u00e9spedes airport\\\", \\\"Q3536540\\\", [[0, 1, 2, 3, 4]]], \\\"t\\\": [\\\"bayamo\\\", \\\"Q115382\\\", [[13]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"St\\\", \\\"Joseph\\\", \\\"Church\\\", \\\"Church\\\", \\\"of\\\", \\\"St.\\\", \\\"Joseph\\\", \\\"Dushanbe\\\", \\\",\\\", \\\"Tajikistan\\\", \\\"is\\\", \\\"a\\\", \\\"parish\\\", \\\"of\\\", \\\"the\\\", \\\"Roman\\\", \\\"Catholic\\\", \\\"Church\\\", \\\"located\\\", \\\"near\\\", \\\"the\\\", \\\"airport\\\", \\\"in\\\", \\\"Dushanbe\\\", \\\",\\\", \\\"Tajikistan\\\", \\\".\\\"], \\\"h\\\": [\\\"the airport\\\", \\\"Q532778\\\", [[21, 22]]], \\\"t\\\": [\\\"dushanbe\\\", \\\"Q9365\\\", [[8], [24]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"aircraft\\\", \\\"was\\\", \\\"completed\\\", \\\"in\\\", \\\"2014\\\", \\\"and\\\", \\\"arrived\\\", \\\"at\\\", \\\"Halim\\\", \\\"Perdanakusuma\\\", \\\"Airbase\\\", \\\"in\\\", \\\"Jakarta\\\", \\\"on\\\", \\\"10\\\", \\\"April\\\", \\\"2014\\\", \\\".\\\"], \\\"h\\\": [\\\"halim perdanakusuma airbase\\\", \\\"Q1032934\\\", [[9, 10, 11]]], \\\"t\\\": [\\\"jakarta\\\", \\\"Q3630\\\", [[13]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"base\\\", \\\"is\\\", \\\"Gino\\\", \\\"Lisa\\\", \\\"Airport\\\", \\\",\\\", \\\"Foggia\\\", \\\".\\\"], \\\"h\\\": [\\\"gino lisa airport\\\", \\\"Q1431308\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"foggia\\\", \\\"Q13464\\\", [[8]]]}, {\\\"tokens\\\": [\\\"\\\\\\\"\\\", \\\"Head\\\", \\\"Office\\\", \\\":\\\", \\\"Los\\\", \\\"Cerrillos\\\", \\\"Airport\\\", \\\",\\\", \\\"Santiago\\\", \\\",\\\", \\\"Chile\\\", \\\".\\\", \\\"\\\\\\\"\\\"], \\\"h\\\": [\\\"los cerrillos airport\\\", \\\"Q5659235\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"santiago\\\", \\\"Q2887\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Direct\\\", \\\"flights\\\", \\\"to\\\", \\\"the\\\", \\\"continent\\\", \\\"(\\\", \\\"Lisbon\\\", \\\")\\\", \\\"are\\\", \\\"provided\\\", \\\"by\\\", \\\"SATA\\\", \\\"International\\\", \\\"out\\\", \\\"of\\\", \\\"Santa\\\", \\\"Maria\\\", \\\"Airport\\\", \\\"located\\\", \\\"close\\\", \\\"to\\\", \\\"Vila\\\", \\\"do\\\", \\\"Porto\\\", \\\".\\\"], \\\"h\\\": [\\\"santa maria airport\\\", \\\"Q1432755\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"vila do porto\\\", \\\"Q1003164\\\", [[21, 22, 23]]]}, {\\\"tokens\\\": [\\\"SALSA\\\", \\\"d'Ha\\\\u00efti\\\", \\\"is\\\", \\\"a\\\", \\\"Haitian\\\", \\\"airline\\\", \\\"headquartered\\\", \\\"at\\\", \\\"Toussaint\\\", \\\"Louverture\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Port\\\", \\\"-\\\", \\\"au\\\", \\\"-\\\", \\\"Prince\\\", \\\",\\\", \\\"Haiti\\\", \\\".\\\"], \\\"h\\\": [\\\"toussaint louverture international airport\\\", \\\"Q794560\\\", [[8, 9, 10, 11]]], \\\"t\\\": [\\\"port-au-prince\\\", \\\"Q34261\\\", [[13, 14, 15, 16, 17]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"community\\\", \\\"is\\\", \\\"located\\\", \\\"along\\\", \\\"Red\\\", \\\"Lion\\\", \\\"Road\\\", \\\"(\\\", \\\"County\\\", \\\"Route\\\", \\\"641\\\", \\\")\\\", \\\"south\\\", \\\"of\\\", \\\"Vincentown\\\", \\\",\\\", \\\"to\\\", \\\"the\\\", \\\"west\\\", \\\"of\\\", \\\"U.S.\\\", \\\"Route\\\", \\\"206\\\", \\\",\\\", \\\"and\\\", \\\"southeast\\\", \\\"of\\\", \\\"the\\\", \\\"Red\\\", \\\"Lion\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"red lion airport\\\", \\\"Q7304523\\\", [[29, 30, 31]]], \\\"t\\\": [\\\"vincentown\\\", \\\"Q7932185\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Remaining\\\", \\\"aircraft\\\", \\\"transferred\\\", \\\"to\\\", \\\"Halfpenny\\\", \\\"Green\\\", \\\"airport\\\", \\\"to\\\", \\\"the\\\", \\\"southwest\\\", \\\"of\\\", \\\"Wolverhampton\\\", \\\".\\\"], \\\"h\\\": [\\\"halfpenny green airport\\\", \\\"Q3915261\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"wolverhampton\\\", \\\"Q126269\\\", [[11]]]}, {\\\"tokens\\\": [\\\"There\\\", \\\"are\\\", \\\"three\\\", \\\"airstrips\\\", \\\":\\\", \\\"Kayonza\\\", \\\"Tea\\\", \\\"Factory\\\", \\\",\\\", \\\"Savannah\\\", \\\"Airstrip\\\", \\\"near\\\", \\\"Kihihi\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"Ishasha\\\", \\\"River\\\", \\\"Camp\\\", \\\"Airport\\\", \\\"in\\\", \\\"the\\\", \\\"Ishasha\\\", \\\"Sector\\\", \\\"of\\\", \\\"Queen\\\", \\\"Elizabeth\\\", \\\"National\\\", \\\"Park\\\", \\\".\\\"], \\\"h\\\": [\\\"savannah airstrip\\\", \\\"Q17108392\\\", [[9, 10]]], \\\"t\\\": [\\\"kihihi\\\", \\\"Q6406018\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Caiari\\\", \\\"Airport\\\", \\\"was\\\", \\\"the\\\", \\\"first\\\", \\\"airport\\\", \\\"of\\\", \\\"Porto\\\", \\\"Velho\\\", \\\",\\\", \\\"Brazil\\\", \\\".\\\"], \\\"h\\\": [\\\"caiari airport\\\", \\\"Q3813497\\\", [[0, 1]]], \\\"t\\\": [\\\"porto velho\\\", \\\"Q172512\\\", [[7, 8]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"primary\\\", \\\"airport\\\", \\\"for\\\", \\\"the\\\", \\\"Virginia\\\", \\\"Peninsula\\\", \\\"is\\\", \\\"the\\\", \\\"Newport\\\", \\\"News\\\", \\\"/\\\", \\\"Williamsburg\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"newport news/williamsburg international airport\\\", \\\"Q6586790\\\", [[9, 10, 11, 12, 13, 14]]], \\\"t\\\": [\\\"virginia peninsula\\\", \\\"Q2553780\\\", [[5, 6]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Royal\\\", \\\"Victorian\\\", \\\"Aero\\\", \\\"Club\\\", \\\"is\\\", \\\"an\\\", \\\"Australian\\\", \\\"aero\\\", \\\"club\\\", \\\"based\\\", \\\"at\\\", \\\"Moorabbin\\\", \\\"Airport\\\", \\\"in\\\", \\\"Melbourne\\\", \\\".\\\"], \\\"h\\\": [\\\"moorabbin airport\\\", \\\"Q1232433\\\", [[12, 13]]], \\\"t\\\": [\\\"melbourne\\\", \\\"Q3141\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Also\\\", \\\",\\\", \\\"the\\\", \\\"next\\\", \\\"two\\\", \\\"closest\\\", \\\"airports\\\", \\\"are\\\", \\\"the\\\", \\\"Surigao\\\", \\\"Airport\\\", \\\"in\\\", \\\"Surigao\\\", \\\"City\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"Laguindingan\\\", \\\"Airport\\\", \\\"in\\\", \\\"Laguindingan\\\", \\\".\\\"], \\\"h\\\": [\\\"surigao airport\\\", \\\"Q7646281\\\", [[9, 10]]], \\\"t\\\": [\\\"surigao city\\\", \\\"Q1019949\\\", [[12, 13]]]}, {\\\"tokens\\\": [\\\"Ashton\\\", \\\"Larmond\\\", \\\"is\\\", \\\"charged\\\", \\\"with\\\", \\\"\\\\n\\\\n\\\\n\\\", \\\"Carlos\\\", \\\"Larmond\\\", \\\"is\\\", \\\"charged\\\", \\\"with\\\", \\\"\\\\n\\\\n\\\\n\\\", \\\"Carlos\\\", \\\"Larmond\\\", \\\"was\\\", \\\"arrested\\\", \\\"at\\\", \\\"the\\\", \\\"Montreal\\\", \\\"Pierre\\\", \\\"Elliott\\\", \\\"Trudeau\\\", \\\"International\\\", \\\"Airport\\\", \\\"as\\\", \\\"he\\\", \\\"was\\\", \\\"allegedly\\\", \\\"intending\\\", \\\"to\\\", \\\"travel\\\", \\\"overseas\\\", \\\"for\\\", \\\"terrorist\\\", \\\"purposes\\\", \\\".\\\"], \\\"h\\\": [\\\"pierre elliott trudeau international airport\\\", \\\"Q736627\\\", [[19, 20, 21, 22, 23]]], \\\"t\\\": [\\\"montreal\\\", \\\"Q340\\\", [[18]]]}, {\\\"tokens\\\": [\\\"Maloney\\\", \\\"opened\\\", \\\"his\\\", \\\"first\\\", \\\"aviation\\\", \\\"museum\\\", \\\"at\\\", \\\"Claremont\\\", \\\",\\\", \\\"California\\\", \\\"on\\\", \\\"January\\\", \\\"12\\\", \\\",\\\", \\\"1957\\\", \\\",\\\", \\\"and\\\", \\\"then\\\", \\\"moved\\\", \\\"to\\\", \\\"LA\\\", \\\"/\\\", \\\"Ontario\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Ontario\\\", \\\",\\\", \\\"California\\\", \\\"in\\\", \\\"the\\\", \\\"1960s\\\", \\\".\\\"], \\\"h\\\": [\\\"ontario international airport\\\", \\\"Q949831\\\", [[22, 23, 24]]], \\\"t\\\": [\\\"ontario, california\\\", \\\"Q488134\\\", [[26, 27, 28]]]}, {\\\"tokens\\\": [\\\"RAAF\\\", \\\"Williamtown\\\", \\\"employed\\\", \\\"approximately\\\", \\\"3,500\\\", \\\"personnel\\\", \\\",\\\", \\\"including\\\", \\\"military\\\", \\\",\\\", \\\"civilians\\\", \\\"and\\\", \\\"contractors\\\", \\\",\\\", \\\"and\\\", \\\"generated\\\", \\\"150\\\", \\\"\\\\u00a0\\\", \\\"million\\\", \\\"per\\\", \\\"annum\\\", \\\"by\\\", \\\"way\\\", \\\"of\\\", \\\"salaries\\\", \\\"in\\\", \\\"the\\\", \\\"Hunter\\\", \\\"Region\\\", \\\"economy\\\", \\\".\\\"], \\\"h\\\": [\\\"raaf williamtown\\\", \\\"Q17570\\\", [[0, 1]]], \\\"t\\\": [\\\"hunter region\\\", \\\"Q1638164\\\", [[27, 28]]]}, {\\\"tokens\\\": [\\\"Florence\\\", \\\"'s\\\", \\\"\\\\\\\"\\\", \\\"Amerigo\\\", \\\"Vespucci\\\", \\\"\\\\\\\"\\\", \\\"airport\\\", \\\"is\\\", \\\"to\\\", \\\"the\\\", \\\"east\\\", \\\".\\\"], \\\"h\\\": [\\\"\\\\\\\"amerigo vespucci\\\\\\\" airport\\\", \\\"Q707731\\\", [[2, 3, 4, 5, 6]]], \\\"t\\\": [\\\"florence\\\", \\\"Q2044\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Sanga\\\", \\\"-\\\", \\\"Sanga\\\", \\\"Airport\\\", \\\",\\\", \\\"the\\\", \\\"main\\\", \\\"airport\\\", \\\"of\\\", \\\"the\\\", \\\"province\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"municipality\\\", \\\"of\\\", \\\"Bongao\\\", \\\".\\\"], \\\"h\\\": [\\\"sanga-sanga airport\\\", \\\"Q1321647\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"bongao\\\", \\\"Q155195\\\", [[18]]]}, {\\\"tokens\\\": [\\\"Other\\\", \\\"airports\\\", \\\"in\\\", \\\"the\\\", \\\"area\\\", \\\"include\\\", \\\"Thebephatshwa\\\", \\\"Airport\\\", \\\",\\\", \\\"northwest\\\", \\\",\\\", \\\"and\\\", \\\"Sir\\\", \\\"Seretse\\\", \\\"Khama\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"southeast\\\", \\\"by\\\", \\\"Gaborone\\\", \\\".\\\"], \\\"h\\\": [\\\"sir seretse khama international airport\\\", \\\"Q1327949\\\", [[12, 13, 14, 15, 16]]], \\\"t\\\": [\\\"gaborone\\\", \\\"Q3919\\\", [[20]]]}, {\\\"tokens\\\": [\\\"Ch\\\\u00e2lons\\\", \\\"Vatry\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"minor\\\", \\\"international\\\", \\\"airport\\\", \\\"serving\\\", \\\"Ch\\\\u00e2lons\\\", \\\"-\\\", \\\"en\\\", \\\"-\\\", \\\"Champagne\\\", \\\"(\\\", \\\"formerly\\\", \\\"Ch\\\\u00e2lons\\\", \\\"-\\\", \\\"sur\\\", \\\"-\\\", \\\"Marne\\\", \\\")\\\", \\\"in\\\", \\\"northeastern\\\", \\\"France\\\", \\\".\\\"], \\\"h\\\": [\\\"ch\\\\u00e2lons vatry airport\\\", \\\"Q1837108\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"ch\\\\u00e2lons-en-champagne\\\", \\\"Q47135\\\", [[9, 10, 11, 12, 13]]]}, {\\\"tokens\\\": [\\\"Villa\\\", \\\"Independencia\\\", \\\"Airport\\\", \\\"serves\\\", \\\"Fray\\\", \\\"Bentos\\\", \\\";\\\", \\\"it\\\", \\\"has\\\", \\\",\\\", \\\"however\\\", \\\",\\\", \\\"no\\\", \\\"commercial\\\", \\\"air\\\", \\\"service\\\", \\\".\\\"], \\\"h\\\": [\\\"villa independencia airport\\\", \\\"Q25037266\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"fray bentos\\\", \\\"Q849835\\\", [[4, 5]]]}, {\\\"tokens\\\": [\\\"Twelfth\\\", \\\"Air\\\", \\\"Force\\\", \\\"combat\\\", \\\"engineers\\\", \\\"moved\\\", \\\"into\\\", \\\"Valence\\\", \\\"-\\\", \\\"Chabeuil\\\", \\\"Airport\\\", \\\"in\\\", \\\"late\\\", \\\"August\\\", \\\"1944\\\", \\\",\\\", \\\"and\\\", \\\"cleared\\\", \\\"the\\\", \\\"airport\\\", \\\"of\\\", \\\"mines\\\", \\\"and\\\", \\\"destroyed\\\", \\\"German\\\", \\\"aircraft\\\", \\\".\\\"], \\\"h\\\": [\\\"chabeuil airport\\\", \\\"Q2875976\\\", [[9, 10]]], \\\"t\\\": [\\\"valence\\\", \\\"Q8848\\\", [[7]]]}, {\\\"tokens\\\": [\\\"Jardines\\\", \\\"del\\\", \\\"Rey\\\", \\\"Airport\\\", \\\"is\\\", \\\"much\\\", \\\"closer\\\", \\\"to\\\", \\\"the\\\", \\\"resorts\\\", \\\"on\\\", \\\"Cayo\\\", \\\"Coco\\\", \\\"than\\\", \\\"M\\\\u00e1ximo\\\", \\\"G\\\\u00f3mez\\\", \\\"Airport\\\", \\\",\\\", \\\"which\\\", \\\"previously\\\", \\\"served\\\", \\\"the\\\", \\\"island\\\", \\\".\\\"], \\\"h\\\": [\\\"jardines del rey airport\\\", \\\"Q2895532\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"cayo coco\\\", \\\"Q1052012\\\", [[11, 12]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Heart\\\", \\\"of\\\", \\\"Georgia\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"three\\\", \\\"miles\\\", \\\"east\\\", \\\"of\\\", \\\"Eastman\\\", \\\"off\\\", \\\"of\\\", \\\"State\\\", \\\"Route\\\", \\\"46\\\", \\\".\\\"], \\\"h\\\": [\\\"heart of georgia regional airport\\\", \\\"Q14686649\\\", [[1, 2, 3, 4, 5]]], \\\"t\\\": [\\\"eastman\\\", \\\"Q1278280\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Macon\\\", \\\"County\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"use\\\", \\\"airport\\\", \\\"in\\\", \\\"Macon\\\", \\\"County\\\", \\\",\\\", \\\"North\\\", \\\"Carolina\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"macon county airport\\\", \\\"Q6724853\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"macon county, north carolina\\\", \\\"Q507575\\\", [[9, 10, 11, 12, 13]]]}, {\\\"tokens\\\": [\\\"Commercial\\\", \\\"air\\\", \\\"service\\\", \\\"is\\\", \\\"available\\\", \\\"at\\\", \\\"the\\\", \\\"Gogebic\\\", \\\"-\\\", \\\"Iron\\\", \\\"County\\\", \\\"Airport\\\", \\\"(\\\", \\\"IWD\\\", \\\")\\\", \\\"north\\\", \\\"of\\\", \\\"Ironwood\\\", \\\".\\\"], \\\"h\\\": [\\\"iwd\\\", \\\"Q3274027\\\", [[13]]], \\\"t\\\": [\\\"ironwood\\\", \\\"Q2002936\\\", [[17]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"airport\\\", \\\",\\\", \\\"Mangalore\\\", \\\"'s\\\", \\\"Bajpe\\\", \\\"Airport\\\", \\\"/\\\", \\\"IXE\\\", \\\",\\\", \\\"is\\\", \\\"10\\\", \\\"kilometres\\\", \\\"away\\\", \\\".\\\"], \\\"h\\\": [\\\"bajpe airport\\\", \\\"Q290527\\\", [[6, 7]]], \\\"t\\\": [\\\"mangalore\\\", \\\"Q127041\\\", [[4]]]}, {\\\"tokens\\\": [\\\"State\\\", \\\"Library\\\", \\\"station\\\", \\\"is\\\", \\\"to\\\", \\\"be\\\", \\\"located\\\", \\\"underground\\\", \\\"on\\\", \\\"the\\\", \\\"intersection\\\", \\\"of\\\", \\\"Swanston\\\", \\\"and\\\", \\\"La\\\", \\\"Trobe\\\", \\\"Streets\\\", \\\"in\\\", \\\"the\\\", \\\"Melbourne\\\", \\\"CBD\\\", \\\"above\\\", \\\"the\\\", \\\"existing\\\", \\\"Melbourne\\\", \\\"Central\\\", \\\"station\\\", \\\".\\\"], \\\"h\\\": [\\\"state library station\\\", \\\"Q29026643\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"melbourne cbd\\\", \\\"Q6811747\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"South\\\", \\\"Bend\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"South\\\", \\\"Bend\\\", \\\",\\\", \\\"Indiana\\\", \\\"is\\\", \\\"connected\\\", \\\"to\\\", \\\"downtown\\\", \\\"Chicago\\\", \\\"via\\\", \\\"a\\\", \\\"South\\\", \\\"Shore\\\", \\\"Line\\\", \\\"station\\\", \\\".\\\"], \\\"h\\\": [\\\"south bend international airport\\\", \\\"Q7566309\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"south bend, indiana\\\", \\\"Q486877\\\", [[5, 6, 7, 8]]]}, {\\\"tokens\\\": [\\\"Roseau\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Canefield\\\", \\\"Airport\\\", \\\",\\\", \\\"a\\\", \\\"nearby\\\", \\\"small\\\", \\\"aircraft\\\", \\\"airport\\\", \\\"that\\\", \\\"provides\\\", \\\"direct\\\", \\\"links\\\", \\\"to\\\", \\\"nearby\\\", \\\"islands\\\", \\\",\\\", \\\"as\\\", \\\"well\\\", \\\"as\\\", \\\"the\\\", \\\"larger\\\", \\\"Douglas\\\", \\\"\\\\u2013\\\", \\\"Charles\\\", \\\"Airport\\\", \\\"to\\\", \\\"the\\\", \\\"north\\\", \\\".\\\"], \\\"h\\\": [\\\"douglas\\\\u2013charles airport\\\", \\\"Q652545\\\", [[25, 26, 27, 28]]], \\\"t\\\": [\\\"roseau\\\", \\\"Q36281\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Along\\\", \\\"the\\\", \\\"I-5\\\", \\\"stretch\\\", \\\",\\\", \\\"Walter\\\", \\\"Wirth\\\", \\\"Lake\\\", \\\"and\\\", \\\"McNary\\\", \\\"Field\\\", \\\"(\\\", \\\"Salem\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\")\\\", \\\"are\\\", \\\"on\\\", \\\"the\\\", \\\"left\\\", \\\";\\\", \\\"near\\\", \\\"Route\\\", \\\"22\\\", \\\",\\\", \\\"the\\\", \\\"unincorporated\\\", \\\"neighborhood\\\", \\\"of\\\", \\\"Four\\\", \\\"Corners\\\", \\\"is\\\", \\\"on\\\", \\\"the\\\", \\\"right\\\", \\\".\\\"], \\\"h\\\": [\\\"mcnary field\\\", \\\"Q649827\\\", [[9, 10]]], \\\"t\\\": [\\\"salem\\\", \\\"Q43919\\\", [[12]]]}, {\\\"tokens\\\": [\\\"He\\\", \\\"was\\\", \\\"squadron\\\", \\\"commander\\\", \\\"by\\\", \\\"1997\\\", \\\",\\\", \\\"moving\\\", \\\"to\\\", \\\"Adisumarmo\\\", \\\"Airport\\\", \\\"in\\\", \\\"Surakarta\\\", \\\"and\\\", \\\"later\\\", \\\"to\\\", \\\"Adisucipto\\\", \\\"as\\\", \\\"he\\\", \\\"continued\\\", \\\"going\\\", \\\"up\\\", \\\"the\\\", \\\"ranks\\\", \\\".\\\"], \\\"h\\\": [\\\"adisumarmo airport\\\", \\\"Q283970\\\", [[9, 10]]], \\\"t\\\": [\\\"surakarta\\\", \\\"Q4803\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Goodland\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"(\\\", \\\"Renner\\\", \\\"Field\\\", \\\")\\\", \\\"is\\\", \\\"two\\\", \\\"miles\\\", \\\"north\\\", \\\"of\\\", \\\"Goodland\\\", \\\",\\\", \\\"in\\\", \\\"Sherman\\\", \\\"County\\\", \\\",\\\", \\\"Kansas\\\", \\\".\\\"], \\\"h\\\": [\\\"renner field\\\", \\\"Q3914081\\\", [[4, 5]]], \\\"t\\\": [\\\"goodland\\\", \\\"Q1931362\\\", [[0], [12]]]}, {\\\"tokens\\\": [\\\"Jos\\\\u00e9\\\", \\\"Celestino\\\", \\\"Mutis\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Bah\\\\u00eda\\\", \\\"Solano\\\", \\\",\\\", \\\"a\\\", \\\"municipality\\\", \\\"of\\\", \\\"the\\\", \\\"Choc\\\\u00f3\\\", \\\"Department\\\", \\\"in\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"jos\\\\u00e9 celestino mutis airport\\\", \\\"Q2902785\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"bah\\\\u00eda solano\\\", \\\"Q1579457\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"Ozamiz\\\", \\\"-\\\", \\\"Labo\\\", \\\"Airport\\\", \\\"also\\\", \\\"serves\\\", \\\"the\\\", \\\"cities\\\", \\\"of\\\", \\\"Oroquieta\\\", \\\"and\\\", \\\"Tangub\\\", \\\",\\\", \\\"some\\\", \\\"municipalities\\\", \\\"of\\\", \\\"Zamboanga\\\", \\\"del\\\", \\\"Sur\\\", \\\",\\\", \\\"Lanao\\\", \\\"del\\\", \\\"Norte\\\", \\\"and\\\", \\\"some\\\", \\\"parts\\\", \\\"of\\\", \\\"Lanao\\\", \\\"del\\\", \\\"Sur\\\", \\\".\\\"], \\\"h\\\": [\\\"labo airport\\\", \\\"Q6467125\\\", [[2, 3]]], \\\"t\\\": [\\\"ozamiz\\\", \\\"Q263837\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"A77\\\", \\\"is\\\", \\\"an\\\", \\\"important\\\", \\\"link\\\", \\\"from\\\", \\\"Glasgow\\\", \\\"to\\\", \\\"one\\\", \\\"of\\\", \\\"its\\\", \\\"two\\\", \\\"major\\\", \\\"airports\\\", \\\",\\\", \\\"Prestwick\\\", \\\"Airport\\\", \\\",\\\", \\\"and\\\", \\\"to\\\", \\\"the\\\", \\\"three\\\", \\\"main\\\", \\\"Northern\\\", \\\"Ireland\\\", \\\"ferry\\\", \\\"terminals\\\", \\\"at\\\", \\\"Stranraer\\\", \\\",\\\", \\\"Cairnryan\\\", \\\",\\\", \\\"and\\\", \\\"Troon\\\", \\\".\\\"], \\\"h\\\": [\\\"prestwick airport\\\", \\\"Q8992\\\", [[16, 17]]], \\\"t\\\": [\\\"glasgow\\\", \\\"Q4093\\\", [[7]]]}, {\\\"tokens\\\": [\\\"Trans\\\", \\\"Maldivian\\\", \\\"Airways\\\", \\\"(\\\", \\\"Pvt\\\", \\\")\\\", \\\"Ltd.\\\", \\\"(\\\", \\\"TMA\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"private\\\", \\\"airline\\\", \\\"headquartered\\\", \\\"on\\\", \\\"the\\\", \\\"grounds\\\", \\\"of\\\", \\\"Velana\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Mal\\\\u00e9\\\", \\\",\\\", \\\"Maldives.\\\\\\\"Contact\\\", \\\".\\\", \\\"\\\\\\\"\\\"], \\\"h\\\": [\\\"velana international airport\\\", \\\"Q29104\\\", [[19, 20, 21]]], \\\"t\\\": [\\\"mal\\\\u00e9\\\", \\\"Q9347\\\", [[23]]]}, {\\\"tokens\\\": [\\\"Owen\\\", \\\"Roberts\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"Grand\\\", \\\"Cayman\\\", \\\",\\\", \\\"Cayman\\\", \\\"Islands\\\", \\\".\\\"], \\\"h\\\": [\\\"owen roberts international airport\\\", \\\"Q665948\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"grand cayman\\\", \\\"Q737765\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"Diom\\\\u00edcio\\\", \\\"Freitas\\\", \\\"/\\\", \\\"Forquilhinha\\\", \\\"Airport\\\", \\\"is\\\", \\\"the\\\", \\\"airport\\\", \\\"serving\\\", \\\"Crici\\\\u00fama\\\", \\\",\\\", \\\"Brazil\\\", \\\",\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"adjoining\\\", \\\"municipality\\\", \\\"of\\\", \\\"Forquilhinha\\\", \\\".\\\"], \\\"h\\\": [\\\"forquilhinha airport\\\", \\\"Q959295\\\", [[3, 4]]], \\\"t\\\": [\\\"crici\\\\u00fama\\\", \\\"Q1439157\\\", [[9]]]}, {\\\"tokens\\\": [\\\"Felts\\\", \\\"Field\\\", \\\",\\\", \\\"the\\\", \\\"historic\\\", \\\"airfield\\\", \\\"of\\\", \\\"Spokane\\\", \\\",\\\", \\\"Washington\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"on\\\", \\\"the\\\", \\\"south\\\", \\\"bank\\\", \\\"of\\\", \\\"the\\\", \\\"Spokane\\\", \\\"River\\\", \\\"and\\\", \\\"east\\\", \\\"of\\\", \\\"Spokane\\\", \\\"proper\\\", \\\".\\\"], \\\"h\\\": [\\\"felts field\\\", \\\"Q5442691\\\", [[0, 1]]], \\\"t\\\": [\\\"spokane, washington\\\", \\\"Q187805\\\", [[7, 8, 9]]]}, {\\\"tokens\\\": [\\\"Diego\\\", \\\"Aracena\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Iquique\\\", \\\",\\\", \\\"capital\\\", \\\"of\\\", \\\"the\\\", \\\"Tarapac\\\\u00e1\\\", \\\"Region\\\", \\\"in\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"diego aracena international airport\\\", \\\"Q1431221\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"iquique\\\", \\\"Q14440\\\", [[10]]]}, {\\\"tokens\\\": [\\\"At\\\", \\\"the\\\", \\\"stopover\\\", \\\"in\\\", \\\"Novosibirsk\\\", \\\"at\\\", \\\"Tolmachevo\\\", \\\"Airport\\\", \\\",\\\", \\\"a\\\", \\\"new\\\", \\\"crew\\\", \\\"and\\\", \\\"aircraft\\\", \\\"took\\\", \\\"on\\\", \\\"the\\\", \\\"route\\\", \\\".\\\"], \\\"h\\\": [\\\"tolmachevo airport\\\", \\\"Q1328849\\\", [[6, 7]]], \\\"t\\\": [\\\"novosibirsk\\\", \\\"Q883\\\", [[4]]]}, {\\\"tokens\\\": [\\\"Los\\\", \\\"Perales\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Bah\\\\u00eda\\\", \\\"de\\\", \\\"Car\\\\u00e1quez\\\", \\\"in\\\", \\\"Manab\\\\u00ed\\\", \\\"Province\\\", \\\",\\\", \\\"Ecuador\\\", \\\".\\\"], \\\"h\\\": [\\\"los perales airport\\\", \\\"Q25037254\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"bah\\\\u00eda de car\\\\u00e1quez\\\", \\\"Q2749246\\\", [[10, 11, 12]]]}, {\\\"tokens\\\": [\\\"Growing\\\", \\\"up\\\", \\\",\\\", \\\"Mej\\\\u00eda\\\", \\\"lived\\\", \\\"with\\\", \\\"his\\\", \\\"parents\\\", \\\"and\\\", \\\"younger\\\", \\\"brother\\\", \\\"in\\\", \\\"a\\\", \\\"neighborhood\\\", \\\"called\\\", \\\"Herrera\\\", \\\",\\\", \\\"near\\\", \\\"Santo\\\", \\\"Domingo\\\", \\\"'s\\\", \\\"former\\\", \\\"airport\\\", \\\"of\\\", \\\"the\\\", \\\"same\\\", \\\"name\\\", \\\".\\\", \\\"Costa\\\", \\\",\\\", \\\"Brian\\\", \\\".\\\"], \\\"h\\\": [\\\"former airport\\\", \\\"Q2876065\\\", [[21, 22]]], \\\"t\\\": [\\\"santo domingo\\\", \\\"Q34820\\\", [[18, 19]]]}, {\\\"tokens\\\": [\\\"They\\\", \\\"later\\\", \\\"managed\\\", \\\"to\\\", \\\"repel\\\", \\\"the\\\", \\\"militants\\\", \\\"from\\\", \\\"capturing\\\", \\\"the\\\", \\\"airport\\\", \\\"in\\\", \\\"Benina\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q44553\\\", [[10]]], \\\"t\\\": [\\\"benina\\\", \\\"Q4888033\\\", [[12]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"The\\\", \\\"Valley\\\", \\\",\\\", \\\"just\\\", \\\"to\\\", \\\"the\\\", \\\"south\\\", \\\"of\\\", \\\"the\\\", \\\"house\\\", \\\"was\\\", \\\"also\\\", \\\"named\\\", \\\"as\\\", \\\"Wallblake\\\", \\\"Airport\\\", \\\",\\\", \\\"now\\\", \\\"renamed\\\", \\\"as\\\", \\\"Clayton\\\", \\\"J.\\\", \\\"Lloyd\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"wallblake airport\\\", \\\"Q1657604\\\", [[18, 19]]], \\\"t\\\": [\\\"the valley\\\", \\\"Q30994\\\", [[4, 5]]]}, {\\\"tokens\\\": [\\\"Rzesz\\\\u00f3w\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"an\\\", \\\"international\\\", \\\"airport\\\", \\\"and\\\", \\\"is\\\", \\\"a\\\", \\\"member\\\", \\\"of\\\", \\\"Eurocities\\\", \\\".\\\"], \\\"h\\\": [\\\"international airport\\\", \\\"Q1432651\\\", [[5, 6]]], \\\"t\\\": [\\\"rzesz\\\\u00f3w\\\", \\\"Q598\\\", [[0]]]}, {\\\"tokens\\\": [\\\"LIFESTAR\\\", \\\"currently\\\", \\\"operates\\\", \\\"5\\\", \\\"bases\\\", \\\"in\\\", \\\"the\\\", \\\"region\\\", \\\":\\\", \\\"LIFESTAR\\\", \\\"1\\\", \\\"is\\\", \\\"based\\\", \\\"in\\\", \\\"Morristown\\\", \\\",\\\", \\\"Tennessee\\\", \\\"at\\\", \\\"the\\\", \\\"Morristown\\\", \\\"Regional\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"morristown regional airport\\\", \\\"Q3612341\\\", [[19, 20, 21]]], \\\"t\\\": [\\\"morristown, tennessee\\\", \\\"Q2330995\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"base\\\", \\\"was\\\", \\\"Casablanca\\\", \\\"Mohammed\\\", \\\"V\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"with\\\", \\\"focus\\\", \\\"cities\\\", \\\"at\\\", \\\"Agadir\\\", \\\",\\\", \\\"Nador\\\", \\\",\\\", \\\"Paris\\\", \\\"and\\\", \\\"Tangier\\\", \\\".\\\"], \\\"h\\\": [\\\"mohammed v international airport\\\", \\\"Q955433\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"casablanca\\\", \\\"Q7903\\\", [[4]]]}, {\\\"tokens\\\": [\\\"Manhattan\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"(\\\", \\\"MHK\\\", \\\")\\\", \\\"in\\\", \\\"Manhattan\\\", \\\",\\\", \\\"Kansas\\\", \\\"is\\\", \\\"the\\\", \\\"next\\\", \\\"closest\\\", \\\"commercial\\\", \\\"airport\\\", \\\";\\\", \\\"Kansas\\\", \\\"City\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\"MCI\\\", \\\")\\\", \\\"in\\\", \\\"Kansas\\\", \\\"City\\\", \\\"is\\\", \\\"the\\\", \\\"closest\\\", \\\"major\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"manhattan regional airport\\\", \\\"Q4272488\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"manhattan, kansas\\\", \\\"Q856841\\\", [[7, 8, 9]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"hub\\\", \\\"is\\\", \\\"El\\\", \\\"Dorado\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Bogot\\\\u00e1\\\", \\\",\\\", \\\"and\\\", \\\"Jos\\\\u00e9\\\", \\\"Mar\\\\u00eda\\\", \\\"C\\\\u00f3rdova\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Medell\\\\u00edn\\\", \\\"is\\\", \\\"a\\\", \\\"focus\\\", \\\"-\\\", \\\"city\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"jos\\\\u00e9 mar\\\\u00eda c\\\\u00f3rdova international airport\\\", \\\"Q535161\\\", [[11, 12, 13, 14, 15]]], \\\"t\\\": [\\\"medell\\\\u00edn\\\", \\\"Q48278\\\", [[17]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"company\\\", \\\"gathered\\\", \\\"considerable\\\", \\\"venture\\\", \\\"capital\\\", \\\"from\\\", \\\"angel\\\", \\\"investors\\\", \\\"and\\\", \\\"opened\\\", \\\"a\\\", \\\"factory\\\", \\\"headquartered\\\", \\\"in\\\", \\\"a\\\", \\\"facility\\\", \\\"at\\\", \\\"Mojave\\\", \\\"Air\\\", \\\"and\\\", \\\"Space\\\", \\\"Port\\\", \\\"in\\\", \\\"Mojave\\\", \\\",\\\", \\\"California\\\", \\\".\\\"], \\\"h\\\": [\\\"mojave air and space port\\\", \\\"Q390522\\\", [[18, 19, 20, 21, 22]]], \\\"t\\\": [\\\"mojave, california\\\", \\\"Q1943133\\\", [[24, 25, 26]]]}, {\\\"tokens\\\": [\\\"Francisco\\\", \\\"S\\\\u00e1\\\", \\\"Carneiro\\\", \\\"Airport\\\", \\\"or\\\", \\\"simply\\\", \\\"Porto\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"international\\\", \\\"airport\\\", \\\"near\\\", \\\"Porto\\\", \\\"(\\\", \\\"Oporto\\\", \\\")\\\", \\\",\\\", \\\"Portugal\\\", \\\".\\\"], \\\"h\\\": [\\\"porto airport\\\", \\\"Q943743\\\", [[6, 7]]], \\\"t\\\": [\\\"oporto\\\", \\\"Q36433\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Raleigh\\\", \\\"-\\\", \\\"Durham\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\"RDU\\\", \\\")\\\", \\\",\\\", \\\"is\\\", \\\"to\\\", \\\"the\\\", \\\"west\\\", \\\".\\\"], \\\"h\\\": [\\\"rdu\\\", \\\"Q1192962\\\", [[6]]], \\\"t\\\": [\\\"raleigh\\\", \\\"Q41087\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"flight\\\", \\\"originated\\\", \\\"from\\\", \\\"Hato\\\", \\\"International\\\", \\\"Airport\\\", \\\"of\\\", \\\"Cura\\\\u00e7ao\\\", \\\"en\\\", \\\"route\\\", \\\"to\\\", \\\"the\\\", \\\"Flamingo\\\", \\\"International\\\", \\\"Airport\\\", \\\"on\\\", \\\"the\\\", \\\"sister\\\", \\\"island\\\", \\\"of\\\", \\\"Bonaire\\\", \\\".\\\"], \\\"h\\\": [\\\"flamingo international airport\\\", \\\"Q1430982\\\", [[13, 14, 15]]], \\\"t\\\": [\\\"bonaire\\\", \\\"Q25396\\\", [[21]]]}, {\\\"tokens\\\": [\\\"Located\\\", \\\"south\\\", \\\"in\\\", \\\"Santa\\\", \\\"Rosa\\\", \\\",\\\", \\\"it\\\", \\\"replaces\\\", \\\"the\\\", \\\"closed\\\", \\\"General\\\", \\\"Manuel\\\", \\\"Serrano\\\", \\\"Airport\\\", \\\"in\\\", \\\"Machala\\\", \\\",\\\", \\\"and\\\", \\\"is\\\", \\\"designed\\\", \\\"to\\\", \\\"handle\\\", \\\"international\\\", \\\"flights\\\", \\\"from\\\", \\\"Peru\\\", \\\".\\\"], \\\"h\\\": [\\\"general manuel serrano airport\\\", \\\"Q2374029\\\", [[10, 11, 12, 13]]], \\\"t\\\": [\\\"machala\\\", \\\"Q215080\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Villa\\\", \\\"Reynolds\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Villa\\\", \\\"Mercedes\\\", \\\",\\\", \\\"San\\\", \\\"Luis\\\", \\\",\\\", \\\"Argentina\\\", \\\".\\\"], \\\"h\\\": [\\\"villa reynolds airport\\\", \\\"Q7930472\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"villa mercedes\\\", \\\"Q1756745\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"FlyBranson\\\", \\\"Travel\\\", \\\",\\\", \\\"LLC\\\", \\\",\\\", \\\"branded\\\", \\\"as\\\", \\\"Branson\\\", \\\"Air\\\", \\\"Express\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"air\\\", \\\"travel\\\", \\\"marketing\\\", \\\"brand\\\", \\\",\\\", \\\"based\\\", \\\"at\\\", \\\"Branson\\\", \\\"Airport\\\", \\\"near\\\", \\\"Branson\\\", \\\",\\\", \\\"Missouri\\\", \\\".\\\"], \\\"h\\\": [\\\"branson airport\\\", \\\"Q1430977\\\", [[20, 21]]], \\\"t\\\": [\\\"branson, missouri\\\", \\\"Q898857\\\", [[23, 24, 25]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Italian\\\", \\\"post\\\", \\\"at\\\", \\\"Kufra\\\", \\\"included\\\", \\\"the\\\", \\\"Buma\\\", \\\"airfield\\\", \\\"and\\\", \\\"radio\\\", \\\"station\\\", \\\",\\\", \\\"used\\\", \\\"for\\\", \\\"air\\\", \\\"supply\\\", \\\"and\\\", \\\"communications\\\", \\\"with\\\", \\\"Italian\\\", \\\"East\\\", \\\"Africa\\\", \\\"and\\\", \\\"a\\\", \\\"fort\\\", \\\"at\\\", \\\"the\\\", \\\"nearby\\\", \\\"village\\\", \\\"of\\\", \\\"El\\\", \\\"Tag\\\", \\\".\\\"], \\\"h\\\": [\\\"buma airfield\\\", \\\"Q30542\\\", [[7, 8]]], \\\"t\\\": [\\\"kufra\\\", \\\"Q172114\\\", [[4]]]}, {\\\"tokens\\\": [\\\"Ahmad\\\", \\\"Yani\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\",\\\", \\\"serves\\\", \\\"Semarang\\\", \\\",\\\", \\\"Central\\\", \\\"Java\\\", \\\",\\\", \\\"Indonesia\\\", \\\".\\\"], \\\"h\\\": [\\\"ahmad yani international airport\\\", \\\"Q1457975\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"semarang\\\", \\\"Q11025\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Korean\\\", \\\"Air\\\", \\\"'s\\\", \\\"other\\\", \\\"hubs\\\", \\\"are\\\", \\\"at\\\", \\\"Jeju\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Jeju\\\", \\\"and\\\", \\\"Gimhae\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Busan\\\", \\\".\\\"], \\\"h\\\": [\\\"gimhae international airport\\\", \\\"Q483223\\\", [[13, 14, 15]]], \\\"t\\\": [\\\"busan\\\", \\\"Q16520\\\", [[17]]]}, {\\\"tokens\\\": [\\\"According\\\", \\\"to\\\", \\\"a\\\", \\\"NOTAM\\\", \\\"issued\\\", \\\"by\\\", \\\"CAA\\\", \\\",\\\", \\\"New\\\", \\\"Islamabad\\\", \\\"Airport\\\", \\\"(\\\", \\\"OPIS\\\", \\\")\\\", \\\"is\\\", \\\"established\\\", \\\"and\\\", \\\"will\\\", \\\"be\\\", \\\"operational\\\", \\\"from\\\", \\\"April\\\", \\\"16th\\\", \\\",\\\", \\\"2018\\\", \\\".\\\"], \\\"h\\\": [\\\"opis\\\", \\\"Q1190316\\\", [[12]]], \\\"t\\\": [\\\"islamabad\\\", \\\"Q1362\\\", [[9]]]}, {\\\"tokens\\\": [\\\"Manizales\\\", \\\"has\\\", \\\"a\\\", \\\"domestic\\\", \\\"airport\\\", \\\"called\\\", \\\"La\\\", \\\"Nubia\\\", \\\"Airport\\\", \\\"which\\\", \\\"has\\\", \\\"a\\\", \\\"runway\\\", \\\"of\\\", \\\"about\\\", \\\"1,400\\\", \\\"meters\\\", \\\"and\\\", \\\"provides\\\", \\\"services\\\", \\\"from\\\", \\\"6\\\", \\\"am\\\", \\\"to\\\", \\\"6\\\", \\\"pm\\\", \\\".\\\"], \\\"h\\\": [\\\"la nubia airport\\\", \\\"Q1936891\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"manizales\\\", \\\"Q235190\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Baiyun\\\", \\\"New\\\", \\\"Town\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"new\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\"(\\\", \\\"CBD\\\", \\\")\\\", \\\"in\\\", \\\"Baiyun\\\", \\\"District\\\", \\\",\\\", \\\"Guangzhou\\\", \\\",\\\", \\\"China\\\", \\\",\\\", \\\"located\\\", \\\"around\\\", \\\"the\\\", \\\"former\\\", \\\"Baiyun\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"former baiyun airport\\\", \\\"Q5613723\\\", [[25, 26, 27]]], \\\"t\\\": [\\\"guangzhou\\\", \\\"Q16572\\\", [[18]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"on\\\", \\\"the\\\", \\\"Katunayake\\\", \\\"-\\\", \\\"Colombo\\\", \\\"road\\\", \\\"(\\\", \\\"A03\\\", \\\")\\\", \\\"and\\\", \\\"is\\\", \\\"located\\\", \\\"a\\\", \\\"few\\\", \\\"miles\\\", \\\"from\\\", \\\"the\\\", \\\"Bandaranaike\\\", \\\"International\\\", \\\"Airport\\\", \\\"and\\\", \\\"Katunayake\\\", \\\"Export\\\", \\\"Processing\\\", \\\"Zone\\\", \\\".\\\"], \\\"h\\\": [\\\"bandaranaike international airport\\\", \\\"Q60900\\\", [[19, 20, 21]]], \\\"t\\\": [\\\"colombo\\\", \\\"Q35381\\\", [[6]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"international\\\", \\\"airport\\\", \\\"is\\\", \\\"the\\\", \\\"New\\\", \\\"Chitose\\\", \\\"Airport\\\", \\\"near\\\", \\\"Sapporo\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"nearest\\\", \\\"domestic\\\", \\\"airport\\\", \\\"is\\\", \\\"in\\\", \\\"Asahikawa\\\", \\\".\\\"], \\\"h\\\": [\\\"new chitose airport\\\", \\\"Q908296\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"sapporo\\\", \\\"Q37951\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Bremen\\\", \\\"has\\\", \\\"an\\\", \\\"international\\\", \\\"airport\\\", \\\"situated\\\", \\\"south\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\"centre\\\", \\\".\\\"], \\\"h\\\": [\\\"international airport\\\", \\\"Q665365\\\", [[3, 4]]], \\\"t\\\": [\\\"bremen\\\", \\\"Q24879\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Local\\\", \\\"airports\\\", \\\"include\\\", \\\"Darke\\\", \\\"County\\\", \\\"Airport\\\", \\\",\\\", \\\"seven\\\", \\\"miles\\\", \\\"away\\\", \\\"in\\\", \\\"Versailles\\\", \\\"and\\\", \\\"James\\\", \\\"M.\\\", \\\"Cox\\\", \\\"Dayton\\\", \\\"International\\\", \\\"Airport\\\", \\\"35\\\", \\\"miles\\\", \\\"away\\\", \\\"in\\\", \\\"Vandalia\\\", \\\".\\\"], \\\"h\\\": [\\\"darke county airport\\\", \\\"Q1709059\\\", [[3, 4, 5]]], \\\"t\\\": [\\\"versailles\\\", \\\"Q2538368\\\", [[11]]]}, {\\\"tokens\\\": [\\\"Presidential\\\", \\\"Airways\\\", \\\"(\\\", \\\"PAW\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"charter\\\", \\\"cargo\\\", \\\"and\\\", \\\"passenger\\\", \\\"airline\\\", \\\"currently\\\", \\\"based\\\", \\\"at\\\", \\\"Melbourne\\\", \\\"International\\\", \\\"Airport\\\", \\\"serving\\\", \\\"Melbourne\\\", \\\",\\\", \\\"Florida\\\", \\\",\\\", \\\"USA\\\", \\\".\\\"], \\\"h\\\": [\\\"melbourne international airport\\\", \\\"Q652030\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"melbourne, florida\\\", \\\"Q949779\\\", [[19, 20, 21]]]}, {\\\"tokens\\\": [\\\"Phoenix\\\", \\\"Goodyear\\\", \\\"Airport\\\", \\\"(\\\", \\\"formerly\\\", \\\"Goodyear\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"airport\\\", \\\"a\\\", \\\"mile\\\", \\\"southwest\\\", \\\"of\\\", \\\"Goodyear\\\", \\\",\\\", \\\"in\\\", \\\"Maricopa\\\", \\\"County\\\", \\\",\\\", \\\"Phoenix\\\", \\\",\\\", \\\"Arizona\\\", \\\".\\\"], \\\"h\\\": [\\\"phoenix goodyear airport\\\", \\\"Q7186890\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"phoenix, arizona\\\", \\\"Q16556\\\", [[23, 24, 25]]]}, {\\\"tokens\\\": [\\\"Alcides\\\", \\\"Fern\\\\u00e1ndez\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"commercial\\\", \\\"airport\\\", \\\"on\\\", \\\"the\\\", \\\"Caribbean\\\", \\\"coast\\\", \\\"serving\\\", \\\"to\\\", \\\"town\\\", \\\"of\\\", \\\"Acand\\\\u00ed\\\", \\\"in\\\", \\\"the\\\", \\\"Choco\\\", \\\"Department\\\", \\\"of\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"alcides fern\\\\u00e1ndez airport\\\", \\\"Q1936968\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"acand\\\\u00ed\\\", \\\"Q1575935\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Carter\\\", \\\"was\\\", \\\"assigned\\\", \\\"as\\\", \\\"an\\\", \\\"Instructor\\\", \\\"Pilot\\\", \\\"in\\\", \\\"the\\\", \\\"50th\\\", \\\"Flying\\\", \\\"Training\\\", \\\"Squadron\\\", \\\"at\\\", \\\"Columbus\\\", \\\"AFB\\\", \\\"in\\\", \\\"Columbus\\\", \\\",\\\", \\\"Mississippi\\\", \\\"flying\\\", \\\"the\\\", \\\"T-38\\\", \\\"Talon\\\", \\\".\\\"], \\\"h\\\": [\\\"columbus afb\\\", \\\"Q1657653\\\", [[14, 15]]], \\\"t\\\": [\\\"columbus, mississippi\\\", \\\"Q985648\\\", [[17, 18, 19]]]}, {\\\"tokens\\\": [\\\"Frans\\\", \\\"Sales\\\", \\\"Lega\\\", \\\"Airport\\\", \\\"or\\\", \\\"Ruteng\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"Ruteng\\\", \\\",\\\", \\\"Manggarai\\\", \\\"regency\\\", \\\",\\\", \\\"East\\\", \\\"Nusa\\\", \\\"Tenggara\\\", \\\".\\\"], \\\"h\\\": [\\\"frans sales lega airport\\\", \\\"Q12474050\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"ruteng\\\", \\\"Q1708604\\\", [[5], [12]]]}, {\\\"tokens\\\": [\\\"Pattimura\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"Ambon\\\", \\\"City\\\", \\\",\\\", \\\"Maluku\\\", \\\"Province\\\", \\\",\\\", \\\"Indonesia\\\", \\\".\\\"], \\\"h\\\": [\\\"pattimura airport\\\", \\\"Q2232506\\\", [[0, 1]]], \\\"t\\\": [\\\"ambon\\\", \\\"Q18970\\\", [[7]]]}, {\\\"tokens\\\": [\\\"El\\\", \\\"Mirador\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"just\\\", \\\"southeast\\\", \\\"of\\\", \\\"Puerto\\\", \\\"Varas\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"the\\\", \\\"Los\\\", \\\"Lagos\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"el mirador airport\\\", \\\"Q12692557\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"puerto varas\\\", \\\"Q51596\\\", [[12, 13]]]}, {\\\"tokens\\\": [\\\"Gansner\\\", \\\"Field\\\", \\\"is\\\", \\\"a\\\", \\\"general\\\", \\\"aviation\\\", \\\"airport\\\", \\\"located\\\", \\\"near\\\", \\\"Quincy\\\", \\\".\\\"], \\\"h\\\": [\\\"gansner field\\\", \\\"Q3274627\\\", [[0, 1]]], \\\"t\\\": [\\\"quincy\\\", \\\"Q1979185\\\", [[9]]]}, {\\\"tokens\\\": [\\\"Aeroframe\\\", \\\"Services\\\", \\\"was\\\", \\\"headquartered\\\", \\\"in\\\", \\\"Lake\\\", \\\"Charles\\\", \\\",\\\", \\\"Louisiana\\\", \\\"at\\\", \\\"Chennault\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"chennault international airport\\\", \\\"Q1708583\\\", [[10, 11, 12]]], \\\"t\\\": [\\\"lake charles, louisiana\\\", \\\"Q864106\\\", [[5, 6, 7, 8]]]}, {\\\"tokens\\\": [\\\"Al\\\", \\\"Hoceima\\\", \\\"'s\\\", \\\"Cherif\\\", \\\"Al\\\", \\\"Idrissi\\\", \\\"Airport\\\", \\\"and\\\", \\\"Tetouan\\\", \\\"'s\\\", \\\"Sania\\\", \\\"Ramel\\\", \\\"Airport\\\", \\\"also\\\", \\\"receive\\\", \\\"commercial\\\", \\\"flights\\\", \\\".\\\"], \\\"h\\\": [\\\"cherif al idrissi airport\\\", \\\"Q1370928\\\", [[3, 4, 5, 6]]], \\\"t\\\": [\\\"al hoceima\\\", \\\"Q310350\\\", [[0, 1]]]}, {\\\"tokens\\\": [\\\"Bathurst\\\", \\\"Island\\\", \\\"is\\\", \\\"the\\\", \\\"fifth\\\", \\\"-\\\", \\\"largest\\\", \\\"island\\\", \\\"of\\\", \\\"Australia\\\", \\\"and\\\", \\\"accessible\\\", \\\"by\\\", \\\"sea\\\", \\\"or\\\", \\\"air\\\", \\\".\\\"], \\\"h\\\": [\\\"air\\\", \\\"Q17607\\\", [[15]]], \\\"t\\\": [\\\"bathurst island\\\", \\\"Q810814\\\", [[0, 1]]]}, {\\\"tokens\\\": [\\\"Fatmawati\\\", \\\"Soekarno\\\", \\\"Airport\\\", \\\"in\\\", \\\"Bengkulu\\\", \\\",\\\", \\\"a\\\", \\\"major\\\", \\\"artery\\\", \\\"road\\\", \\\",\\\", \\\"and\\\", \\\"a\\\", \\\"hospital\\\", \\\",\\\", \\\"both\\\", \\\"in\\\", \\\"South\\\", \\\"Jakarta\\\", \\\"are\\\", \\\"named\\\", \\\"after\\\", \\\"her\\\", \\\".\\\"], \\\"h\\\": [\\\"fatmawati soekarno airport\\\", \\\"Q1880024\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"bengkulu\\\", \\\"Q8042\\\", [[4]]]}, {\\\"tokens\\\": [\\\"La\\\", \\\"Esperanza\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airstrip\\\", \\\"north\\\", \\\"-\\\", \\\"northeast\\\", \\\"of\\\", \\\"Marchig\\\\u00fce\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"O'Higgins\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"la esperanza airport\\\", \\\"Q16894649\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"marchig\\\\u00fce\\\", \\\"Q16921\\\", [[11]]]}, {\\\"tokens\\\": [\\\"Bindlacher\\\", \\\"Berg\\\", \\\"Airport\\\", \\\",\\\", \\\"or\\\", \\\"\\\\\\\"\\\", \\\"Verkehrslandeplatz\\\", \\\"Bayreuth\\\", \\\"\\\\\\\"\\\", \\\"in\\\", \\\"German\\\", \\\",\\\", \\\"is\\\", \\\"a\\\", \\\"regional\\\", \\\"airport\\\", \\\"in\\\", \\\"Bindlach\\\", \\\",\\\", \\\"Bavaria\\\", \\\"5\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\"northeast\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Bayreuth\\\", \\\".\\\"], \\\"h\\\": [\\\"bindlacher berg airport\\\", \\\"Q531596\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"bayreuth\\\", \\\"Q3923\\\", [[7], [28]]]}, {\\\"tokens\\\": [\\\"A\\\", \\\"plane\\\", \\\"headed\\\", \\\"from\\\", \\\"Tokyo\\\", \\\"'s\\\", \\\"Haneda\\\", \\\"Airport\\\", \\\"to\\\", \\\"Seoul\\\", \\\"'s\\\", \\\"Gimpo\\\", \\\"Airport\\\", \\\"with\\\", \\\"a\\\", \\\"Hallyu\\\", \\\"star\\\", \\\"on\\\", \\\"board\\\", \\\"runs\\\", \\\"into\\\", \\\"an\\\", \\\"unexpected\\\", \\\"storm\\\", \\\"and\\\", \\\"is\\\", \\\"in\\\", \\\"danger\\\", \\\"of\\\", \\\"crashing\\\", \\\".\\\"], \\\"h\\\": [\\\"gimpo airport\\\", \\\"Q482493\\\", [[11, 12]]], \\\"t\\\": [\\\"seoul\\\", \\\"Q8684\\\", [[9]]]}, {\\\"tokens\\\": [\\\"El\\\", \\\"Cardal\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"R\\\\u00edo\\\", \\\"Bueno\\\", \\\"commune\\\", \\\"in\\\", \\\"the\\\", \\\"Los\\\", \\\"Lagos\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"el cardal airport\\\", \\\"Q12692544\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"r\\\\u00edo bueno\\\", \\\"Q56126\\\", [[11, 12]]]}, {\\\"tokens\\\": [\\\"Enid\\\", \\\",\\\", \\\"Oklahoma\\\", \\\",\\\", \\\"Gentry\\\", \\\"'s\\\", \\\"home\\\", \\\"town\\\", \\\",\\\", \\\"named\\\", \\\"a\\\", \\\"street\\\", \\\"at\\\", \\\"the\\\", \\\"Enid\\\", \\\"Woodring\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"after\\\", \\\"him\\\", \\\".\\\"], \\\"h\\\": [\\\"enid woodring regional airport\\\", \\\"Q5378895\\\", [[14, 15, 16, 17]]], \\\"t\\\": [\\\"enid, oklahoma\\\", \\\"Q984361\\\", [[0, 1, 2]]]}, {\\\"tokens\\\": [\\\"Brighton\\\", \\\"City\\\", \\\"Airport\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"Shoreham\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"parish\\\", \\\"of\\\", \\\"Lancing\\\", \\\"in\\\", \\\"West\\\", \\\"Sussex\\\", \\\",\\\", \\\"England\\\", \\\".\\\"], \\\"h\\\": [\\\"brighton city airport\\\", \\\"Q735756\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"west sussex\\\", \\\"Q23287\\\", [[20, 21]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"head\\\", \\\"office\\\", \\\"is\\\", \\\"on\\\", \\\"the\\\", \\\"property\\\", \\\"of\\\", \\\"Nauru\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Yaren\\\", \\\"District\\\", \\\",\\\", \\\"and\\\", \\\"its\\\", \\\"operations\\\", \\\"office\\\", \\\"is\\\", \\\"in\\\", \\\"Brisbane\\\", \\\",\\\", \\\"Queensland\\\", \\\",\\\", \\\"Australia\\\", \\\".\\\"], \\\"h\\\": [\\\"nauru international airport\\\", \\\"Q534251\\\", [[8, 9, 10]]], \\\"t\\\": [\\\"yaren district\\\", \\\"Q31026\\\", [[12, 13]]]}, {\\\"tokens\\\": [\\\"Risner\\\", \\\"was\\\", \\\"recalled\\\", \\\"to\\\", \\\"active\\\", \\\"duty\\\", \\\"in\\\", \\\"February\\\", \\\"1951\\\", \\\"while\\\", \\\"assigned\\\", \\\"to\\\", \\\"the\\\", \\\"185th\\\", \\\"Tactical\\\", \\\"Fighter\\\", \\\"Squadron\\\", \\\"of\\\", \\\"the\\\", \\\"OKANG\\\", \\\"at\\\", \\\"Will\\\", \\\"Rogers\\\", \\\"Field\\\", \\\"in\\\", \\\"Oklahoma\\\", \\\"City\\\", \\\",\\\", \\\"Oklahoma\\\", \\\".\\\"], \\\"h\\\": [\\\"will rogers field\\\", \\\"Q1499872\\\", [[21, 22, 23]]], \\\"t\\\": [\\\"oklahoma city\\\", \\\"Q34863\\\", [[25, 26]]]}, {\\\"tokens\\\": [\\\"Three\\\", \\\"crews\\\", \\\"from\\\", \\\"the\\\", \\\"420th\\\", \\\"DBAP\\\", \\\"bombed\\\", \\\"K\\\\u00f6nigsberg\\\", \\\"during\\\", \\\"the\\\", \\\"nights\\\", \\\"of\\\", \\\"28\\\\u201329\\\", \\\"August\\\", \\\"and\\\", \\\"30\\\", \\\"August\\\\u20131\\\", \\\"September\\\", \\\"from\\\", \\\"Ramenskoye\\\", \\\"Airport\\\", \\\",\\\", \\\"southeast\\\", \\\"of\\\", \\\"Moscow\\\", \\\".\\\"], \\\"h\\\": [\\\"ramenskoye airport\\\", \\\"Q2388744\\\", [[19, 20]]], \\\"t\\\": [\\\"moscow\\\", \\\"Q649\\\", [[24]]]}, {\\\"tokens\\\": [\\\"VIP\\\", \\\"Ecuador\\\", \\\"was\\\", \\\"an\\\", \\\"airline\\\", \\\"based\\\", \\\"at\\\", \\\"Mariscal\\\", \\\"Sucre\\\", \\\"International\\\", \\\"Airport\\\", \\\"and\\\", \\\"headquartered\\\", \\\"in\\\", \\\"Quito\\\", \\\",\\\", \\\"Ecuador\\\", \\\".\\\"], \\\"h\\\": [\\\"mariscal sucre international airport\\\", \\\"Q7376063\\\", [[7, 8, 9, 10]]], \\\"t\\\": [\\\"quito\\\", \\\"Q2900\\\", [[14]]]}, {\\\"tokens\\\": [\\\"He\\\", \\\"attended\\\", \\\"local\\\", \\\"schools\\\", \\\"before\\\", \\\"he\\\", \\\"was\\\", \\\"admitted\\\", \\\"to\\\", \\\"the\\\", \\\"Kenya\\\", \\\"School\\\", \\\"of\\\", \\\"Flying\\\", \\\"at\\\", \\\"Wilson\\\", \\\"Airport\\\", \\\"in\\\", \\\"Nairobi\\\", \\\",\\\", \\\"Kenya\\\", \\\".\\\"], \\\"h\\\": [\\\"wilson airport\\\", \\\"Q1049288\\\", [[15, 16]]], \\\"t\\\": [\\\"nairobi\\\", \\\"Q3870\\\", [[18]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"the\\\", \\\"beginning\\\", \\\"of\\\", \\\"1939\\\", \\\",\\\", \\\"it\\\", \\\"opened\\\", \\\"a\\\", \\\"new\\\", \\\"line\\\", \\\"between\\\", \\\"Kolhapur\\\", \\\"and\\\", \\\"Juhu\\\", \\\"Aerodrome\\\", \\\"in\\\", \\\"Mumbai\\\", \\\".\\\"], \\\"h\\\": [\\\"juhu aerodrome\\\", \\\"Q674812\\\", [[14, 15]]], \\\"t\\\": [\\\"mumbai\\\", \\\"Q1156\\\", [[17]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Commonwealth\\\", \\\"Air\\\", \\\"Training\\\", \\\"Plan\\\", \\\"Museum\\\", \\\"is\\\", \\\"an\\\", \\\"aviation\\\", \\\"museum\\\", \\\"located\\\", \\\"at\\\", \\\"Brandon\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\",\\\", \\\"Brandon\\\", \\\",\\\", \\\"Manitoba\\\", \\\".\\\"], \\\"h\\\": [\\\"brandon municipal airport\\\", \\\"Q3502284\\\", [[12, 13, 14]]], \\\"t\\\": [\\\"brandon, manitoba\\\", \\\"Q61432\\\", [[16, 17, 18]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"1943\\\", \\\",\\\", \\\"she\\\", \\\"became\\\", \\\"commanding\\\", \\\"officer\\\", \\\"of\\\", \\\"the\\\", \\\"Long\\\", \\\"Beach\\\", \\\"6th\\\", \\\"Ferrying\\\", \\\"Group\\\", \\\"at\\\", \\\"Daugherty\\\", \\\"Field\\\", \\\"and\\\", \\\"the\\\", \\\"program\\\", \\\"was\\\", \\\"renamed\\\", \\\"to\\\", \\\"the\\\", \\\"Women\\\", \\\"Air\\\", \\\"-\\\", \\\"force\\\", \\\"Service\\\", \\\"Pilots\\\", \\\".\\\"], \\\"h\\\": [\\\"daugherty field\\\", \\\"Q1431943\\\", [[15, 16]]], \\\"t\\\": [\\\"long beach\\\", \\\"Q16739\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"Hex'Air\\\", \\\"was\\\", \\\"a\\\", \\\"French\\\", \\\"regional\\\", \\\"airline\\\", \\\"based\\\", \\\"at\\\", \\\"Le\\\", \\\"Puy\\\", \\\"\\\\u2013\\\", \\\"Loudes\\\", \\\"Airport\\\", \\\"in\\\", \\\"Le\\\", \\\"Puy\\\", \\\"-\\\", \\\"en\\\", \\\"-\\\", \\\"Velay\\\", \\\".\\\"], \\\"h\\\": [\\\"le puy \\\\u2013 loudes airport\\\", \\\"Q2876024\\\", [[8, 9, 10, 11, 12]]], \\\"t\\\": [\\\"le puy-en-velay\\\", \\\"Q184359\\\", [[14, 15, 16, 17, 18, 19]]]}, {\\\"tokens\\\": [\\\"Currently\\\", \\\"Biggin\\\", \\\"Hill\\\", \\\"and\\\", \\\"Lydd\\\", \\\"serve\\\", \\\"as\\\", \\\"\\\\\\\"\\\", \\\"outer\\\", \\\"\\\\\\\"\\\", \\\"airport\\\", \\\"for\\\", \\\"London\\\", \\\"(\\\", \\\"general\\\", \\\"passenger\\\", \\\"aviation\\\", \\\"across\\\", \\\"the\\\", \\\"south\\\", \\\"east\\\", \\\"uses\\\", \\\"Heathrow\\\", \\\",\\\", \\\"Gatwick\\\", \\\",\\\", \\\"Stansted\\\", \\\"and\\\", \\\"Luton\\\", \\\"airports\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"biggin hill\\\", \\\"Q1431935\\\", [[1, 2]]], \\\"t\\\": [\\\"london\\\", \\\"Q84\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Nearest\\\", \\\"Airport\\\", \\\"is\\\", \\\"Sanganer\\\", \\\"Airport\\\", \\\"in\\\", \\\"Jaipur\\\", \\\".\\\"], \\\"h\\\": [\\\"sanganer airport\\\", \\\"Q572387\\\", [[3, 4]]], \\\"t\\\": [\\\"jaipur\\\", \\\"Q66485\\\", [[6]]]}, {\\\"tokens\\\": [\\\"Los\\\", \\\"Pozos\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"San\\\", \\\"Gil\\\", \\\"in\\\", \\\"the\\\", \\\"Santander\\\", \\\"Department\\\", \\\"of\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"los pozos airport\\\", \\\"Q28163860\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"san gil\\\", \\\"Q1294128\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"Denis\\\", \\\"Island\\\", \\\"is\\\", \\\"privately\\\", \\\"owned\\\", \\\"and\\\", \\\"has\\\", \\\"a\\\", \\\"short\\\", \\\"airstrip\\\", \\\".\\\"], \\\"h\\\": [\\\"short airstrip\\\", \\\"Q1653962\\\", [[8, 9]]], \\\"t\\\": [\\\"denis island\\\", \\\"Q28920\\\", [[0, 1]]]}, {\\\"tokens\\\": [\\\"He\\\", \\\"was\\\", \\\"then\\\", \\\"moved\\\", \\\"to\\\", \\\"Jones\\\", \\\"Field\\\", \\\"in\\\", \\\"Bonham\\\", \\\",\\\", \\\"Texas\\\", \\\"for\\\", \\\"primary\\\", \\\"flight\\\", \\\"training\\\", \\\".\\\"], \\\"h\\\": [\\\"jones field\\\", \\\"Q2902318\\\", [[5, 6]]], \\\"t\\\": [\\\"bonham, texas\\\", \\\"Q144856\\\", [[8, 9, 10]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"aircraft\\\", \\\"crashed\\\", \\\"around\\\", \\\"21:30\\\", \\\"local\\\", \\\"time\\\", \\\"while\\\", \\\"on\\\", \\\"an\\\", \\\"NDB\\\", \\\"approach\\\", \\\"to\\\", \\\"Alf\\\\u00e9rez\\\", \\\"FAP\\\", \\\"Alfredo\\\", \\\"Vladimir\\\", \\\"Sara\\\", \\\"Bauer\\\", \\\"Airport\\\", \\\"at\\\", \\\"Andoas\\\", \\\".\\\"], \\\"h\\\": [\\\"alf\\\\u00e9rez fap alfredo vladimir sara bauer airport\\\", \\\"Q4723923\\\", [[13, 14, 15, 16, 17, 18, 19]]], \\\"t\\\": [\\\"andoas\\\", \\\"Q3649471\\\", [[21]]]}, {\\\"tokens\\\": [\\\"Mokuti\\\", \\\"Lodge\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Mokuti\\\", \\\"Lodge\\\", \\\"resort\\\", \\\"and\\\", \\\"the\\\", \\\"Etosha\\\", \\\"National\\\", \\\"Park\\\", \\\"in\\\", \\\"Namibia\\\", \\\".\\\"], \\\"h\\\": [\\\"mokuti lodge airport\\\", \\\"Q17090518\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"etosha national park\\\", \\\"Q675633\\\", [[12, 13, 14]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"full\\\", \\\"operation\\\", \\\"commercial\\\", \\\"airports\\\", \\\"are\\\", \\\"Bakersfield\\\", \\\"'s\\\", \\\"Meadows\\\", \\\"Field\\\", \\\"Airport\\\", \\\"to\\\", \\\"the\\\", \\\"South\\\", \\\",\\\", \\\"and\\\", \\\"Fresno\\\", \\\"'s\\\", \\\"Fresno\\\", \\\"Yosemite\\\", \\\"International\\\", \\\"Airport\\\", \\\"to\\\", \\\"the\\\", \\\"North\\\", \\\".\\\"], \\\"h\\\": [\\\"meadows field airport\\\", \\\"Q652265\\\", [[9, 10, 11]]], \\\"t\\\": [\\\"bakersfield\\\", \\\"Q49256\\\", [[7]]]}, {\\\"tokens\\\": [\\\"LAN\\\", \\\"has\\\", \\\"three\\\", \\\"daily\\\", \\\"flights\\\", \\\"from\\\", \\\"Santiago\\\", \\\"to\\\", \\\"Balmaceda\\\", \\\"Airport\\\", \\\",\\\", \\\"located\\\", \\\"from\\\", \\\"Coyhaique\\\", \\\".\\\"], \\\"h\\\": [\\\"balmaceda airport\\\", \\\"Q2901027\\\", [[8, 9]]], \\\"t\\\": [\\\"coyhaique\\\", \\\"Q3810\\\", [[13]]]}, {\\\"tokens\\\": [\\\"Ouarzazate\\\", \\\"has\\\", \\\"the\\\", \\\"busiest\\\", \\\"airport\\\", \\\"in\\\", \\\"the\\\", \\\"region\\\", \\\";\\\", \\\"the\\\", \\\"airports\\\", \\\"at\\\", \\\"Errachidia\\\", \\\"and\\\", \\\"Zagora\\\", \\\"also\\\", \\\"have\\\", \\\"commercial\\\", \\\"service\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q1432275\\\", [[4]]], \\\"t\\\": [\\\"ouarzazate\\\", \\\"Q505208\\\", [[0]]]}, {\\\"tokens\\\": [\\\"By\\\", \\\"May\\\", \\\"1987\\\", \\\",\\\", \\\"AirCal\\\", \\\"had\\\", \\\"introduced\\\", \\\"new\\\", \\\"flights\\\", \\\"serving\\\", \\\"Chicago\\\", \\\"(\\\", \\\"ORD\\\", \\\")\\\", \\\",\\\", \\\"Anchorage\\\", \\\"(\\\", \\\"ANC\\\", \\\")\\\", \\\",\\\", \\\"and\\\", \\\"its\\\", \\\"only\\\", \\\"international\\\", \\\"destination\\\", \\\",\\\", \\\"Vancouver\\\", \\\",\\\", \\\"British\\\", \\\"Columbia\\\", \\\",\\\", \\\"Canada\\\", \\\"(\\\", \\\"YVR\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"yvr\\\", \\\"Q321224\\\", [[33]]], \\\"t\\\": [\\\"vancouver\\\", \\\"Q24639\\\", [[26]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"12\\\", \\\"August\\\", \\\"1991\\\", \\\",\\\", \\\"the\\\", \\\"474th\\\", \\\"Air\\\", \\\"Base\\\", \\\"was\\\", \\\"re\\\", \\\"-\\\", \\\"established\\\", \\\"in\\\", \\\"Banja\\\", \\\"Luka\\\", \\\"and\\\", \\\"became\\\", \\\"responsible\\\", \\\"both\\\", \\\"for\\\", \\\"Mahovljani\\\", \\\"and\\\", \\\"Zaluzani\\\", \\\"airfields\\\", \\\".\\\"], \\\"h\\\": [\\\"mahovljani\\\", \\\"Q1430945\\\", [[21]]], \\\"t\\\": [\\\"banja luka\\\", \\\"Q131127\\\", [[14, 15]]]}, {\\\"tokens\\\": [\\\"Ngari\\\", \\\"Gunsa\\\", \\\"Airport\\\", \\\",\\\", \\\"near\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"Shiquanhe\\\", \\\",\\\", \\\"started\\\", \\\"operations\\\", \\\"on\\\", \\\"1\\\", \\\"July\\\", \\\"2010\\\", \\\",\\\", \\\"becoming\\\", \\\"the\\\", \\\"fourth\\\", \\\"civil\\\", \\\"airport\\\", \\\"in\\\", \\\"Tibet\\\", \\\".\\\"], \\\"h\\\": [\\\"ngari gunsa airport\\\", \\\"Q1432172\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"shiquanhe\\\", \\\"Q2279283\\\", [[8]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airport\\\", \\\"of\\\", \\\"Mekelle\\\", \\\",\\\", \\\"Alula\\\", \\\"Aba\\\", \\\"Nega\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"within\\\", \\\"the\\\", \\\"administrative\\\", \\\"boundaries\\\", \\\"of\\\", \\\"Qwiha\\\", \\\".\\\"], \\\"h\\\": [\\\"alula aba nega airport\\\", \\\"Q4737322\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"mekelle\\\", \\\"Q332319\\\", [[3]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"16\\\", \\\"January\\\", \\\"2017\\\", \\\",\\\", \\\"the\\\", \\\"Boeing\\\", \\\"747\\\", \\\"-\\\", \\\"400F\\\", \\\"flying\\\", \\\"this\\\", \\\"route\\\", \\\"crashed\\\", \\\"during\\\", \\\"landing\\\", \\\"at\\\", \\\"its\\\", \\\"scheduled\\\", \\\"stopover\\\", \\\"at\\\", \\\"Manas\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Bishkek\\\", \\\".\\\"], \\\"h\\\": [\\\"manas international airport\\\", \\\"Q32997\\\", [[21, 22, 23]]], \\\"t\\\": [\\\"bishkek\\\", \\\"Q9361\\\", [[25]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Hagerstown\\\", \\\"Branch\\\", \\\"Campus\\\", \\\"is\\\", \\\"located\\\", \\\"adjacent\\\", \\\"to\\\", \\\"the\\\", \\\"Hagerstown\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Hagerstown\\\", \\\",\\\", \\\"Maryland\\\", \\\".\\\"], \\\"h\\\": [\\\"hagerstown regional airport\\\", \\\"Q3914582\\\", [[9, 10, 11]]], \\\"t\\\": [\\\"hagerstown, maryland\\\", \\\"Q755559\\\", [[13, 14, 15]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"the\\\", \\\"morning\\\", \\\"of\\\", \\\"June\\\", \\\"15\\\", \\\"the\\\", \\\"group\\\", \\\"arrived\\\", \\\"together\\\", \\\"in\\\", \\\"Smolny\\\", \\\"(\\\", \\\"later\\\", \\\"Rzhevka\\\", \\\")\\\", \\\"Airport\\\", \\\"near\\\", \\\"Leningrad\\\", \\\",\\\", \\\"only\\\", \\\"to\\\", \\\"be\\\", \\\"arrested\\\", \\\"by\\\", \\\"the\\\", \\\"KGB.Beckerman\\\", \\\"(\\\", \\\"2010\\\", \\\")\\\", \\\",\\\", \\\"p.\\\", \\\"196\\\", \\\"-\\\", \\\"199\\\", \\\".\\\"], \\\"h\\\": [\\\"smolny (later rzhevka) airport\\\", \\\"Q2383453\\\", [[11, 12, 13, 14, 15, 16]]], \\\"t\\\": [\\\"leningrad\\\", \\\"Q656\\\", [[18]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Eloy\\\", \\\"Alfaro\\\", \\\"International\\\", \\\"Airport\\\", \\\"joins\\\", \\\"Manta\\\", \\\"with\\\", \\\"Quito\\\", \\\"and\\\", \\\"Guayaquil\\\", \\\".\\\"], \\\"h\\\": [\\\"eloy alfaro international airport\\\", \\\"Q1444671\\\", [[1, 2, 3, 4]]], \\\"t\\\": [\\\"manta\\\", \\\"Q990738\\\", [[6]]]}, {\\\"tokens\\\": [\\\"China\\\", \\\"Northern\\\", \\\"Airlines\\\", \\\"Flight\\\", \\\"6901\\\", \\\"(\\\", \\\"CJ6901\\\", \\\")\\\", \\\"was\\\", \\\"a\\\", \\\"McDonnell\\\", \\\"Douglas\\\", \\\"MD-82\\\", \\\"airliner\\\", \\\"from\\\", \\\"Beijing\\\", \\\"'s\\\", \\\"Capital\\\", \\\"International\\\", \\\"Airport\\\", \\\"to\\\", \\\"\\\\u00dcr\\\\u00fcmqi\\\", \\\"Diwopu\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Xinjiang\\\", \\\",\\\", \\\"China\\\", \\\".\\\"], \\\"h\\\": [\\\"capital international airport\\\", \\\"Q32190\\\", [[17, 18, 19]]], \\\"t\\\": [\\\"beijing\\\", \\\"Q956\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Flights\\\", \\\"by\\\", \\\"MASWings\\\", \\\"connect\\\", \\\"the\\\", \\\"airport\\\", \\\"to\\\", \\\"smaller\\\", \\\"towns\\\", \\\"or\\\", \\\"rural\\\", \\\"areas\\\", \\\"in\\\", \\\"East\\\", \\\"Malaysia\\\", \\\",\\\", \\\"and\\\", \\\"internationally\\\", \\\"to\\\", \\\"Juwata\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Tarakan\\\", \\\",\\\", \\\"Indonesia\\\", \\\".\\\"], \\\"h\\\": [\\\"juwata international airport\\\", \\\"Q2233018\\\", [[19, 20, 21]]], \\\"t\\\": [\\\"tarakan\\\", \\\"Q14501\\\", [[23]]]}, {\\\"tokens\\\": [\\\"Swazi\\\", \\\"Airways\\\", \\\"was\\\", \\\"an\\\", \\\"upcoming\\\", \\\"Swazi\\\", \\\"airline\\\", \\\"based\\\", \\\"at\\\", \\\"King\\\", \\\"Mswati\\\", \\\"III\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Manzini\\\", \\\".\\\"], \\\"h\\\": [\\\"king mswati iii international airport\\\", \\\"Q2285574\\\", [[9, 10, 11, 12, 13]]], \\\"t\\\": [\\\"manzini\\\", \\\"Q495730\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Terengganu\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Sultan\\\", \\\"Mahmud\\\", \\\"Airport\\\", \\\"located\\\", \\\"in\\\", \\\"Kuala\\\", \\\"Nerus\\\", \\\"District\\\", \\\".\\\"], \\\"h\\\": [\\\"sultan mahmud airport\\\", \\\"Q2233067\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"terengganu\\\", \\\"Q189701\\\", [[0]]]}, {\\\"tokens\\\": [\\\"A\\\", \\\"new\\\", \\\"international\\\", \\\"Airport\\\", \\\"in\\\", \\\"Marsa\\\", \\\"Alam\\\", \\\"was\\\", \\\"built\\\", \\\",\\\", \\\"about\\\", \\\"from\\\", \\\"Shalateen\\\", \\\"city\\\", \\\",\\\", \\\"which\\\", \\\"Egyptian\\\", \\\"policy\\\", \\\"makers\\\", \\\"intend\\\", \\\"to\\\", \\\"be\\\", \\\"the\\\", \\\"center\\\", \\\"of\\\", \\\"more\\\", \\\"development\\\", \\\"for\\\", \\\"the\\\", \\\"southern\\\", \\\"region\\\", \\\"included\\\", \\\"the\\\", \\\"Shalateen\\\", \\\"area\\\", \\\".\\\"], \\\"h\\\": [\\\"international airport\\\", \\\"Q123222\\\", [[2, 3]]], \\\"t\\\": [\\\"marsa alam\\\", \\\"Q1001901\\\", [[5, 6]]]}, {\\\"tokens\\\": [\\\"Casablanca\\\", \\\"Tit\\\", \\\"Mellil\\\", \\\"Airport\\\", \\\"(\\\", \\\",\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"Tit\\\", \\\"Mellil\\\", \\\",\\\", \\\"Morocco\\\", \\\",\\\", \\\"near\\\", \\\"Casablanca\\\", \\\".\\\"], \\\"h\\\": [\\\"tit mellil airport\\\", \\\"Q969543\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"casablanca\\\", \\\"Q7903\\\", [[0], [18]]]}, {\\\"tokens\\\": [\\\"Stuart\\\", \\\"Powell\\\", \\\"Field\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"-\\\", \\\"use\\\", \\\"airport\\\", \\\"located\\\", \\\"south\\\", \\\"of\\\", \\\"the\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\"of\\\", \\\"Danville\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"Boyle\\\", \\\"County\\\", \\\",\\\", \\\"Kentucky\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"stuart powell field\\\", \\\"Q7626968\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"danville\\\", \\\"Q988923\\\", [[17]]]}, {\\\"tokens\\\": [\\\"Sandra\\\", \\\"Scabini\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\",\\\", \\\"was\\\", \\\"an\\\", \\\"airstrip\\\", \\\"northeast\\\", \\\"of\\\", \\\"Punta\\\", \\\"Arenas\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\"of\\\", \\\"the\\\", \\\"Magallanes\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"sandra scabini airport\\\", \\\"Q16898872\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"punta arenas\\\", \\\"Q51599\\\", [[11, 12]]]}, {\\\"tokens\\\": [\\\"Dekese\\\", \\\"has\\\", \\\"an\\\", \\\"associated\\\", \\\"airport\\\", \\\"nearby\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q12692416\\\", [[4]]], \\\"t\\\": [\\\"dekese\\\", \\\"Q3021388\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Estonian\\\", \\\"final\\\", \\\"of\\\", \\\"the\\\", \\\"Eurovision\\\", \\\"Song\\\", \\\"Contest\\\", \\\"2002\\\", \\\"was\\\", \\\"held\\\", \\\"on\\\", \\\"26\\\", \\\"January\\\", \\\"at\\\", \\\"the\\\", \\\"Linnahall\\\", \\\"in\\\", \\\"Tallinn\\\", \\\",\\\", \\\"hosted\\\", \\\"by\\\", \\\"Marko\\\", \\\"Reikop\\\", \\\"and\\\", \\\"Karmel\\\", \\\"Eikner\\\", \\\".\\\"], \\\"h\\\": [\\\"linnahall\\\", \\\"Q1810907\\\", [[16]]], \\\"t\\\": [\\\"tallinn\\\", \\\"Q1770\\\", [[18]]]}, {\\\"tokens\\\": [\\\"Floyd\\\", \\\"Bennett\\\", \\\"Memorial\\\", \\\"Airport\\\", \\\"(\\\", \\\"FAA\\\", \\\":\\\", \\\"GFL\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"county\\\", \\\"owned\\\", \\\",\\\", \\\"public\\\", \\\"use\\\", \\\"airport\\\", \\\"located\\\", \\\"3\\\", \\\"\\\\u00a0\\\", \\\"nautical\\\", \\\"miles\\\", \\\"(\\\", \\\"6\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"northeast\\\", \\\"of\\\", \\\"Glens\\\", \\\"Falls\\\", \\\",\\\", \\\".\\\"], \\\"h\\\": [\\\"floyd bennett memorial airport\\\", \\\"Q5462388\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"glens falls\\\", \\\"Q1379621\\\", [[29, 30]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"flight\\\", \\\"originated\\\", \\\"at\\\", \\\"Idlewild\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\"now\\\", \\\"John\\\", \\\"F.\\\", \\\"Kennedy\\\", \\\"International\\\", \\\"Airport\\\", \\\")\\\", \\\"and\\\", \\\"crashed\\\", \\\"on\\\", \\\"approach\\\", \\\"to\\\", \\\"Brussels\\\", \\\"'s\\\", \\\"Zaventem\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"zaventem airport\\\", \\\"Q28934\\\", [[22, 23]]], \\\"t\\\": [\\\"brussels\\\", \\\"Q240\\\", [[20]]]}, {\\\"tokens\\\": [\\\"La\\\", \\\"Vanguardia\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Villavicencio\\\", \\\"in\\\", \\\"the\\\", \\\"Meta\\\", \\\"Department\\\", \\\"of\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"vanguardia airport\\\", \\\"Q6465644\\\", [[1, 2]]], \\\"t\\\": [\\\"villavicencio\\\", \\\"Q749224\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Los\\\", \\\"Angeles\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\"LAX\\\", \\\")\\\", \\\",\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"Westchester\\\", \\\"district\\\", \\\",\\\", \\\"is\\\", \\\"the\\\", \\\"primary\\\", \\\"commercial\\\", \\\"airport\\\", \\\"for\\\", \\\"commercial\\\", \\\"airlines\\\", \\\"in\\\", \\\"the\\\", \\\"county\\\", \\\"and\\\", \\\"the\\\", \\\"Greater\\\", \\\"Los\\\", \\\"Angeles\\\", \\\"Area\\\", \\\".\\\"], \\\"h\\\": [\\\"los angeles international airport\\\", \\\"Q8731\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"greater los angeles area\\\", \\\"Q1050826\\\", [[27, 28, 29, 30]]]}, {\\\"tokens\\\": [\\\"E5\\\", \\\"'s\\\", \\\"northern\\\", \\\"terminus\\\", \\\"is\\\", \\\"on\\\", \\\"Baltra\\\", \\\"Island\\\", \\\",\\\", \\\"at\\\", \\\"the\\\", \\\"Seymour\\\", \\\"Airport\\\", \\\";\\\", \\\"its\\\", \\\"southern\\\", \\\"terminus\\\", \\\"on\\\", \\\"Santa\\\", \\\"Cruz\\\", \\\"Island\\\", \\\",\\\", \\\"at\\\", \\\"El\\\", \\\"Garrapatero\\\", \\\"beach\\\", \\\".\\\"], \\\"h\\\": [\\\"seymour airport\\\", \\\"Q1186422\\\", [[11, 12]]], \\\"t\\\": [\\\"baltra island\\\", \\\"Q200772\\\", [[6, 7]]]}, {\\\"tokens\\\": [\\\"Yazoo\\\", \\\"County\\\", \\\"Airport\\\", \\\"is\\\", \\\"five\\\", \\\"miles\\\", \\\"northwest\\\", \\\"of\\\", \\\"Yazoo\\\", \\\"City\\\", \\\"in\\\", \\\"unincorporated\\\", \\\"Yazoo\\\", \\\"County\\\", \\\",\\\", \\\"Mississippi\\\", \\\".\\\"], \\\"h\\\": [\\\"yazoo county airport\\\", \\\"Q8050637\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"yazoo city\\\", \\\"Q983832\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"As\\\", \\\"of\\\", \\\"1996\\\", \\\",\\\", \\\"South\\\", \\\"Tarawa\\\", \\\"was\\\", \\\"almost\\\", \\\"continuously\\\", \\\"settled\\\", \\\"from\\\", \\\"the\\\", \\\"Bonriki\\\", \\\"International\\\", \\\"Airport\\\", \\\"through\\\", \\\"Bikenibeu\\\", \\\"to\\\", \\\"Bairiki\\\", \\\"in\\\", \\\"the\\\", \\\"west\\\", \\\".\\\"], \\\"h\\\": [\\\"bonriki international airport\\\", \\\"Q522496\\\", [[12, 13, 14]]], \\\"t\\\": [\\\"south tarawa\\\", \\\"Q131233\\\", [[4, 5]]]}, {\\\"tokens\\\": [\\\"An\\\", \\\"under\\\", \\\"construction\\\", \\\"highway\\\", \\\"bridge\\\", \\\"near\\\", \\\"Mexico\\\", \\\"City\\\", \\\"'s\\\", \\\"new\\\", \\\"international\\\", \\\"airport\\\", \\\"collapsed\\\", \\\"due\\\", \\\"to\\\", \\\"the\\\", \\\"shaking\\\", \\\".\\\"], \\\"h\\\": [\\\"new international airport\\\", \\\"Q18014849\\\", [[9, 10, 11]]], \\\"t\\\": [\\\"mexico city\\\", \\\"Q1489\\\", [[6, 7]]]}, {\\\"tokens\\\": [\\\"Chifeng\\\", \\\"'s\\\", \\\"airport\\\", \\\"has\\\", \\\"service\\\", \\\"to\\\", \\\"major\\\", \\\"cities\\\", \\\"such\\\", \\\"as\\\", \\\"Beijing\\\", \\\",\\\", \\\"Hohhot\\\", \\\",\\\", \\\"and\\\", \\\"other\\\", \\\"cities\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q1708732\\\", [[2]]], \\\"t\\\": [\\\"chifeng\\\", \\\"Q570829\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"general\\\", \\\"aviation\\\", \\\"airport\\\", \\\"is\\\", \\\"Turners\\\", \\\"Falls\\\", \\\"Airport\\\", \\\"in\\\", \\\"Montague\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"nearest\\\", \\\"national\\\", \\\"air\\\", \\\"service\\\", \\\"is\\\", \\\"at\\\", \\\"Bradley\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Connecticut\\\", \\\".\\\"], \\\"h\\\": [\\\"turners falls airport\\\", \\\"Q6588260\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"montague\\\", \\\"Q33180\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Superior\\\", \\\"Airways\\\", \\\"is\\\", \\\"a\\\", \\\"chartered\\\", \\\"air\\\", \\\"service\\\", \\\"based\\\", \\\"in\\\", \\\"Red\\\", \\\"Lake\\\", \\\",\\\", \\\"Ontario\\\", \\\",\\\", \\\"Canada\\\", \\\"at\\\", \\\"the\\\", \\\"Red\\\", \\\"Lake\\\", \\\"Airport\\\", \\\"in\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"Cochenour\\\", \\\".\\\"], \\\"h\\\": [\\\"red lake airport\\\", \\\"Q3912791\\\", [[17, 18, 19]]], \\\"t\\\": [\\\"red lake, ontario\\\", \\\"Q1018643\\\", [[9, 10, 11, 12]]]}, {\\\"tokens\\\": [\\\"Ujae\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"use\\\", \\\"airstrip\\\", \\\"at\\\", \\\"Ujae\\\", \\\"on\\\", \\\"Ujae\\\", \\\"Atoll\\\", \\\",\\\", \\\"Marshall\\\", \\\"Islands\\\", \\\".\\\"], \\\"h\\\": [\\\"ujae airport\\\", \\\"Q4381230\\\", [[0, 1]]], \\\"t\\\": [\\\"ujae atoll\\\", \\\"Q697802\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"Cholet\\\", \\\"Le\\\", \\\"Pontreau\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"the\\\", \\\"French\\\", \\\"department\\\", \\\"of\\\", \\\"Maine\\\", \\\"-\\\", \\\"et\\\", \\\"-\\\", \\\"Loire\\\", \\\",\\\", \\\"north\\\", \\\"-\\\", \\\"northeast\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Cholet\\\", \\\".\\\"], \\\"h\\\": [\\\"le pontreau airport\\\", \\\"Q2408589\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"cholet\\\", \\\"Q185066\\\", [[0], [25]]]}, {\\\"tokens\\\": [\\\"Jharkot\\\", \\\"and\\\", \\\"Jhong\\\", \\\"has\\\", \\\"post\\\", \\\"offices\\\", \\\",\\\", \\\"while\\\", \\\"there\\\", \\\"is\\\", \\\"a\\\", \\\"bank\\\", \\\",\\\", \\\"an\\\", \\\"airport\\\", \\\"and\\\", \\\"Nepalese\\\", \\\"Army\\\", \\\"'s\\\", \\\"High\\\", \\\"Altitude\\\", \\\"and\\\", \\\"Mountain\\\", \\\"Warfare\\\", \\\"School\\\", \\\"in\\\", \\\"Jomsom\\\", \\\".\\\"], \\\"h\\\": [\\\"an airport\\\", \\\"Q1431605\\\", [[13, 14]]], \\\"t\\\": [\\\"jomsom\\\", \\\"Q1702717\\\", [[26]]]}, {\\\"tokens\\\": [\\\"US\\\", \\\"50\\\", \\\"joins\\\", \\\"with\\\", \\\"State\\\", \\\"Route\\\", \\\"32\\\", \\\"near\\\", \\\"the\\\", \\\"Ohio\\\", \\\"University\\\", \\\"Bush\\\", \\\"Airport\\\", \\\"\\\\u2013\\\", \\\"Snyder\\\", \\\"Field\\\", \\\"in\\\", \\\"Albany\\\", \\\",\\\", \\\"west\\\", \\\"of\\\", \\\"Athens\\\", \\\".\\\"], \\\"h\\\": [\\\"bush airport\\\\u2013snyder field\\\", \\\"Q3913448\\\", [[11, 12, 13, 14, 15]]], \\\"t\\\": [\\\"athens\\\", \\\"Q755420\\\", [[21]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Island\\\", \\\"itself\\\", \\\"is\\\", \\\"located\\\", \\\"approximately\\\", \\\"35\\\", \\\"miles\\\", \\\"from\\\", \\\"Honiara\\\", \\\",\\\", \\\"and\\\", \\\"approximately\\\", \\\"15\\\", \\\"minutes\\\", \\\"from\\\", \\\"Henderson\\\", \\\"airfield\\\", \\\".\\\"], \\\"h\\\": [\\\"henderson airfield\\\", \\\"Q859876\\\", [[16, 17]]], \\\"t\\\": [\\\"honiara\\\", \\\"Q40921\\\", [[9]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airport\\\", \\\"is\\\", \\\"owned\\\", \\\"and\\\", \\\"operated\\\", \\\"by\\\", \\\"Store\\\", \\\"Norske\\\", \\\"Spitsbergen\\\", \\\"Kulkompani\\\", \\\",\\\", \\\"who\\\", \\\"use\\\", \\\"the\\\", \\\"airport\\\", \\\"to\\\", \\\"transport\\\", \\\"their\\\", \\\"coal\\\", \\\"mining\\\", \\\"workers\\\", \\\"from\\\", \\\"the\\\", \\\"company\\\", \\\"town\\\", \\\"to\\\", \\\"Longyearbyen\\\", \\\"and\\\", \\\"Svalbard\\\", \\\"Airport\\\", \\\",\\\", \\\"Longyear\\\", \\\".\\\"], \\\"h\\\": [\\\"svalbard airport, longyear\\\", \\\"Q59633\\\", [[29, 30, 31, 32]]], \\\"t\\\": [\\\"longyearbyen\\\", \\\"Q25923\\\", [[27]]]}, {\\\"tokens\\\": [\\\"Colmar\\\", \\\"-\\\", \\\"Houssen\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"Houssen\\\", \\\",\\\", \\\"north\\\", \\\"of\\\", \\\"Colmar\\\", \\\",\\\", \\\"both\\\", \\\"\\\\\\\"\\\", \\\"communes\\\", \\\"\\\\\\\"\\\", \\\"in\\\", \\\"the\\\", \\\"Haut\\\", \\\"-\\\", \\\"Rhin\\\", \\\"department\\\", \\\"of\\\", \\\"the\\\", \\\"Alsace\\\", \\\"region\\\", \\\"in\\\", \\\"France\\\", \\\".\\\"], \\\"h\\\": [\\\"houssen airport\\\", \\\"Q1431102\\\", [[2, 3]]], \\\"t\\\": [\\\"colmar\\\", \\\"Q130994\\\", [[0], [14]]]}, {\\\"tokens\\\": [\\\"Isla\\\", \\\"Picton\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"north\\\", \\\"of\\\", \\\"Quinta\\\", \\\"de\\\", \\\"Tilcoco\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"O'Higgins\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"isla picton airport\\\", \\\"Q16892756\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"quinta de tilcoco\\\", \\\"Q56112\\\", [[11, 12, 13]]]}, {\\\"tokens\\\": [\\\"\\\\\\\"\\\", \\\"Ministry\\\", \\\"of\\\", \\\"Public\\\", \\\"Works\\\", \\\"and\\\", \\\"Transport\\\", \\\"Department\\\", \\\"of\\\", \\\"Civil\\\", \\\"Aviation\\\", \\\"Vientiane\\\", \\\"/\\\", \\\"Wattay\\\", \\\"International\\\", \\\"Airport\\\", \\\"P.O.\\\"], \\\"h\\\": [\\\"wattay international airport\\\", \\\"Q221279\\\", [[13, 14, 15]]], \\\"t\\\": [\\\"vientiane\\\", \\\"Q9326\\\", [[11]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"official\\\", \\\"climate\\\", \\\"recording\\\", \\\"station\\\", \\\"in\\\", \\\"Malta\\\", \\\"is\\\", \\\"at\\\", \\\"Luqa\\\", \\\"Airport\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"a\\\", \\\"few\\\", \\\"miles\\\", \\\"inland\\\", \\\"from\\\", \\\"Valletta\\\", \\\".\\\"], \\\"h\\\": [\\\"luqa airport\\\", \\\"Q672289\\\", [[9, 10]]], \\\"t\\\": [\\\"valletta\\\", \\\"Q23800\\\", [[19]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"addition\\\", \\\",\\\", \\\"the\\\", \\\"cities\\\", \\\"of\\\", \\\"Midland\\\", \\\"and\\\", \\\"Bay\\\", \\\"City\\\", \\\"along\\\", \\\"with\\\", \\\"Saginaw\\\", \\\"jointly\\\", \\\"developed\\\", \\\"and\\\", \\\"began\\\", \\\"to\\\", \\\"operate\\\", \\\"an\\\", \\\"airport\\\", \\\"facility\\\", \\\"in\\\", \\\"nearby\\\", \\\"Tittabawassee\\\", \\\"Township\\\", \\\"that\\\", \\\"is\\\", \\\"now\\\", \\\"MBS\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"mbs international airport\\\", \\\"Q652272\\\", [[29, 30, 31]]], \\\"t\\\": [\\\"saginaw\\\", \\\"Q719\\\", [[12]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"1924\\\", \\\"Ford\\\", \\\"and\\\", \\\"Stout\\\", \\\"negotiated\\\", \\\"the\\\", \\\"building\\\", \\\"of\\\", \\\"Ford\\\", \\\"Airport\\\", \\\"in\\\", \\\"Dearborn\\\", \\\",\\\", \\\"Michigan\\\", \\\".\\\"], \\\"h\\\": [\\\"ford airport\\\", \\\"Q5467646\\\", [[9, 10]]], \\\"t\\\": [\\\"dearborn, michigan\\\", \\\"Q430464\\\", [[12, 13, 14]]]}, {\\\"tokens\\\": [\\\"March\\\", \\\"8\\\", \\\",\\\", \\\"2001\\\", \\\".\\\", \\\"and\\\", \\\"Plattsburgh\\\", \\\"-\\\", \\\"North\\\", \\\"Country\\\", \\\"Chamber\\\", \\\"of\\\", \\\"Commerce\\\", \\\"both\\\", \\\"favored\\\", \\\"the\\\", \\\"opening\\\", \\\"of\\\", \\\"a\\\", \\\"new\\\", \\\"commercial\\\", \\\"airport\\\", \\\"and\\\", \\\"closing\\\", \\\"the\\\", \\\"old\\\", \\\"Clinton\\\", \\\"County\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"clinton county airport\\\", \\\"Q1655515\\\", [[26, 27, 28]]], \\\"t\\\": [\\\"plattsburgh\\\", \\\"Q998669\\\", [[6]]]}, {\\\"tokens\\\": [\\\"Murtala\\\", \\\"Muhammed\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\"MMIA\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"international\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"Ikeja\\\", \\\",\\\", \\\"Lagos\\\", \\\"State\\\", \\\",\\\", \\\"Nigeria\\\", \\\",\\\", \\\"and\\\", \\\"is\\\", \\\"the\\\", \\\"major\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"entire\\\", \\\"state\\\", \\\".\\\"], \\\"h\\\": [\\\"murtala muhammed international airport\\\", \\\"Q1043631\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"ikeja\\\", \\\"Q1024647\\\", [[13]]]}, {\\\"tokens\\\": [\\\"Pierrefonds\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"located\\\", \\\"west\\\", \\\"-\\\", \\\"northwest\\\", \\\"of\\\", \\\"Saint\\\", \\\"-\\\", \\\"Pierre\\\", \\\"in\\\", \\\"R\\\\u00e9union\\\", \\\".\\\"], \\\"h\\\": [\\\"pierrefonds airport\\\", \\\"Q17431\\\", [[0, 1]]], \\\"t\\\": [\\\"saint-pierre\\\", \\\"Q249884\\\", [[12, 13, 14]]]}, {\\\"tokens\\\": [\\\"Tulihal\\\", \\\"Airport\\\", \\\",\\\", \\\"Changangei\\\", \\\",\\\", \\\"Imphal\\\", \\\",\\\", \\\"the\\\", \\\"only\\\", \\\"airport\\\", \\\"of\\\", \\\"Manipur\\\", \\\",\\\", \\\"connects\\\", \\\"directly\\\", \\\"with\\\", \\\"Delhi\\\", \\\",\\\", \\\"Kolkata\\\", \\\",\\\", \\\"Guwahati\\\", \\\",\\\", \\\"and\\\", \\\"Agartala\\\", \\\".\\\"], \\\"h\\\": [\\\"tulihal airport\\\", \\\"Q2247550\\\", [[0, 1]]], \\\"t\\\": [\\\"imphal\\\", \\\"Q208097\\\", [[5]]]}, {\\\"tokens\\\": [\\\"That\\\", \\\"same\\\", \\\"day\\\", \\\",\\\", \\\"he\\\", \\\"was\\\", \\\"flown\\\", \\\"from\\\", \\\"the\\\", \\\"General\\\", \\\"Lucio\\\", \\\"Blanco\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Reynosa\\\", \\\"to\\\", \\\"Mexico\\\", \\\"City\\\", \\\"under\\\", \\\"tight\\\", \\\"security\\\", \\\"and\\\", \\\"kept\\\", \\\"at\\\", \\\"the\\\", \\\"SEIDO\\\", \\\"installations\\\", \\\",\\\", \\\"Mexico\\\", \\\"'s\\\", \\\"organized\\\", \\\"crime\\\", \\\"investigatory\\\", \\\"agency\\\", \\\".\\\"], \\\"h\\\": [\\\"general lucio blanco international airport\\\", \\\"Q2232580\\\", [[9, 10, 11, 12, 13]]], \\\"t\\\": [\\\"reynosa\\\", \\\"Q738303\\\", [[15]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Niagara\\\", \\\"Aerospace\\\", \\\"Museum\\\", \\\"is\\\", \\\"an\\\", \\\"aviation\\\", \\\"museum\\\", \\\"located\\\", \\\"in\\\", \\\"Niagara\\\", \\\"Falls\\\", \\\",\\\", \\\"New\\\", \\\"York\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"old\\\", \\\"terminal\\\", \\\"building\\\", \\\"of\\\", \\\"the\\\", \\\"Niagara\\\", \\\"Falls\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"niagara falls international airport\\\", \\\"Q1984520\\\", [[23, 24, 25, 26]]], \\\"t\\\": [\\\"niagara falls, new york\\\", \\\"Q128133\\\", [[10, 11, 12, 13, 14]]]}, {\\\"tokens\\\": [\\\"A\\\", \\\"bus\\\", \\\"rapid\\\", \\\"transit\\\", \\\"system\\\", \\\"with\\\", \\\"services\\\", \\\"within\\\", \\\"SM\\\", \\\"Seaside\\\", \\\"City\\\", \\\",\\\", \\\"SM\\\", \\\"City\\\", \\\"Cebu\\\", \\\",\\\", \\\"Mactan\\\", \\\"-\\\", \\\"Cebu\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"to\\\", \\\"key\\\", \\\"cities\\\", \\\"along\\\", \\\"Metro\\\", \\\"Cebu\\\", \\\"and\\\", \\\"vice\\\", \\\"versa\\\", \\\".\\\"], \\\"h\\\": [\\\"mactan-cebu international airport\\\", \\\"Q1048704\\\", [[16, 17, 18, 19, 20]]], \\\"t\\\": [\\\"metro cebu\\\", \\\"Q1075343\\\", [[26, 27]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"addition\\\", \\\",\\\", \\\"RWJ\\\", \\\"Airpark\\\", \\\",\\\", \\\"a\\\", \\\"privately\\\", \\\"owned\\\", \\\"airport\\\", \\\"for\\\", \\\"public\\\", \\\"use\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Beach\\\", \\\"City\\\", \\\".\\\"], \\\"h\\\": [\\\"rwj airpark\\\", \\\"Q7278116\\\", [[3, 4]]], \\\"t\\\": [\\\"beach city\\\", \\\"Q812835\\\", [[17, 18]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Royal\\\", \\\"Navy\\\", \\\"maintained\\\", \\\"naval\\\", \\\"installations\\\", \\\"in\\\", \\\"Trincomalee\\\", \\\"and\\\", \\\"the\\\", \\\"Royal\\\", \\\"Air\\\", \\\"Force\\\", \\\"(\\\", \\\"RAF\\\", \\\")\\\", \\\"had\\\", \\\"established\\\", \\\"an\\\", \\\"aerodrome\\\", \\\"in\\\", \\\"China\\\", \\\"Bay\\\", \\\",\\\", \\\"Trincomalee\\\", \\\"long\\\", \\\"before\\\", \\\"the\\\", \\\"war\\\", \\\".\\\"], \\\"h\\\": [\\\"china bay\\\", \\\"Q7390732\\\", [[21, 22]]], \\\"t\\\": [\\\"trincomalee\\\", \\\"Q323873\\\", [[7], [24]]]}, {\\\"tokens\\\": [\\\"Paramillo\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"San\\\", \\\"Crist\\\\u00f3bal\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\"of\\\", \\\"the\\\", \\\"T\\\\u00e1chira\\\", \\\"state\\\", \\\"of\\\", \\\"Venezuela\\\", \\\".\\\"], \\\"h\\\": [\\\"paramillo airport\\\", \\\"Q5685452\\\", [[0, 1]]], \\\"t\\\": [\\\"san crist\\\\u00f3bal\\\", \\\"Q820235\\\", [[6, 7]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"headquarters\\\", \\\"of\\\", \\\"the\\\", \\\"NIRA\\\", \\\"are\\\", \\\"temporarily\\\", \\\"located\\\", \\\"at\\\", \\\"Independence\\\", \\\"Park\\\", \\\",\\\", \\\"Kololo\\\", \\\"Airstrip\\\", \\\",\\\", \\\"on\\\", \\\"Kololo\\\", \\\"Hill\\\", \\\",\\\", \\\"in\\\", \\\"Kampala\\\", \\\",\\\", \\\"Uganda\\\", \\\"'s\\\", \\\"capital\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"kololo airstrip\\\", \\\"Q10853684\\\", [[12, 13]]], \\\"t\\\": [\\\"kampala\\\", \\\"Q3894\\\", [[20]]]}, {\\\"tokens\\\": [\\\"Apart\\\", \\\"from\\\", \\\"the\\\", \\\"RTM\\\", \\\",\\\", \\\"there\\\", \\\"were\\\", \\\"two\\\", \\\"other\\\", \\\",\\\", \\\"smaller\\\", \\\",\\\", \\\"companies\\\", \\\"operating\\\", \\\"tramway\\\", \\\"networks\\\", \\\"in\\\", \\\"and\\\", \\\"around\\\", \\\"Rotterdam\\\", \\\"in\\\", \\\"the\\\", \\\"late\\\", \\\"nineteenth\\\", \\\"and\\\", \\\"early\\\", \\\"twentieth\\\", \\\"centuries\\\", \\\".\\\"], \\\"h\\\": [\\\"rtm\\\", \\\"Q656807\\\", [[3]]], \\\"t\\\": [\\\"rotterdam\\\", \\\"Q34370\\\", [[19]]]}, {\\\"tokens\\\": [\\\"Cascade\\\", \\\"Aerospace\\\", \\\"is\\\", \\\"headquartered\\\", \\\"in\\\", \\\"a\\\", \\\"facility\\\", \\\"at\\\", \\\"the\\\", \\\"Abbotsford\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"in\\\", \\\"Abbotsford\\\", \\\",\\\", \\\"British\\\", \\\"Columbia\\\", \\\",\\\", \\\"Canada\\\", \\\".\\\"], \\\"h\\\": [\\\"abbotsford international airport\\\", \\\"Q969671\\\", [[9, 10, 11]]], \\\"t\\\": [\\\"abbotsford, british columbia\\\", \\\"Q271730\\\", [[14, 15, 16, 17]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"new\\\", \\\"airport\\\", \\\",\\\", \\\"Qiemo\\\", \\\"Yudu\\\", \\\"Airport\\\", \\\",\\\", \\\"opened\\\", \\\"on\\\", \\\"19\\\", \\\"December\\\", \\\"2016\\\", \\\",\\\", \\\"where\\\", \\\"commercial\\\", \\\"air\\\", \\\"service\\\", \\\"to\\\", \\\"Qiemo\\\", \\\"Town\\\", \\\"resumed\\\", \\\".\\\"], \\\"h\\\": [\\\"qiemo yudu airport\\\", \\\"Q28127825\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"qiemo town\\\", \\\"Q3360588\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"Ambrolauri\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"an\\\", \\\"airport\\\", \\\",\\\", \\\"opened\\\", \\\"in\\\", \\\"January\\\", \\\"2017\\\", \\\",\\\", \\\"which\\\", \\\"can\\\", \\\"serve\\\", \\\"small\\\", \\\"planes\\\", \\\"carrying\\\", \\\"15\\\\u201320\\\", \\\"passengers\\\", \\\".\\\"], \\\"h\\\": [\\\"airport, opened in january 2017\\\", \\\"Q28797312\\\", [[5, 6, 7, 8, 9, 10]]], \\\"t\\\": [\\\"ambrolauri\\\", \\\"Q456842\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"aircraft\\\", \\\"was\\\", \\\"on\\\", \\\"a\\\", \\\"military\\\", \\\"flight\\\", \\\"from\\\", \\\"Gustavo\\\", \\\"Rizo\\\", \\\"Airport\\\", \\\",\\\", \\\"Baracoa\\\", \\\".\\\"], \\\"h\\\": [\\\"gustavo rizo airport\\\", \\\"Q3646815\\\", [[8, 9, 10]]], \\\"t\\\": [\\\"baracoa\\\", \\\"Q94775\\\", [[12]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"island\\\", \\\"\\\\u2019s\\\", \\\"main\\\", \\\"town\\\", \\\"is\\\", \\\"Cidade\\\", \\\"do\\\", \\\"Maio\\\", \\\"(\\\", \\\"formerly\\\", \\\"Vila\\\", \\\"do\\\", \\\"Maio\\\", \\\")\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"Porto\\\", \\\"Ingl\\\\u00eas\\\", \\\",\\\", \\\"near\\\", \\\"which\\\", \\\"its\\\", \\\"airport\\\", \\\",\\\", \\\"Maio\\\", \\\"Airport\\\", \\\"lies\\\", \\\".\\\"], \\\"h\\\": [\\\"maio airport\\\", \\\"Q2011846\\\", [[27, 28]]], \\\"t\\\": [\\\"cidade do maio\\\", \\\"Q489776\\\", [[6, 7, 8]]]}, {\\\"tokens\\\": [\\\"Inca\\\", \\\"Manco\\\", \\\"C\\\\u00e1pac\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"the\\\", \\\"nearest\\\", \\\"commercial\\\", \\\"airport\\\", \\\";\\\", \\\"it\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Juliaca\\\", \\\".\\\"], \\\"h\\\": [\\\"inca manco c\\\\u00e1pac international airport\\\", \\\"Q1286295\\\", [[0, 1, 2, 3, 4]]], \\\"t\\\": [\\\"juliaca\\\", \\\"Q696074\\\", [[15]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"commercial\\\", \\\"airport\\\", \\\"to\\\", \\\"this\\\", \\\"place\\\", \\\"is\\\", \\\"Swami\\\", \\\"Vivekananda\\\", \\\"Airport\\\", \\\",\\\", \\\"Raipur\\\", \\\"(\\\", \\\")\\\", \\\"and\\\", \\\"the\\\", \\\"nearest\\\", \\\"major\\\", \\\"railway\\\", \\\"station\\\", \\\"is\\\", \\\"Durg\\\", \\\"Junction\\\", \\\"railway\\\", \\\"station\\\", \\\"(\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"swami vivekananda airport\\\", \\\"Q1595087\\\", [[8, 9, 10]]], \\\"t\\\": [\\\"raipur\\\", \\\"Q372773\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Vietnam\\\", \\\"Airlines\\\", \\\"Flight\\\", \\\"815\\\", \\\"was\\\", \\\"a\\\", \\\"scheduled\\\", \\\"Vietnam\\\", \\\"Airlines\\\", \\\"flight\\\", \\\"from\\\", \\\"Ho\\\", \\\"Chi\\\", \\\"Minh\\\", \\\"City\\\", \\\"to\\\", \\\"Phnom\\\", \\\"Penh\\\", \\\"'s\\\", \\\"Pochentong\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"pochentong airport\\\", \\\"Q1054163\\\", [[19, 20]]], \\\"t\\\": [\\\"phnom penh\\\", \\\"Q1850\\\", [[16, 17]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Swan\\\", \\\"Island\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"was\\\", \\\"a\\\", \\\"joint\\\", \\\"civil\\\", \\\"-\\\", \\\"military\\\", \\\"airport\\\", \\\"that\\\", \\\"was\\\", \\\"operational\\\", \\\"in\\\", \\\"the\\\", \\\"Overlook\\\", \\\"neighborhood\\\", \\\"of\\\", \\\"Portland\\\", \\\",\\\", \\\"Oregon\\\", \\\".\\\"], \\\"h\\\": [\\\"swan island municipal airport\\\", \\\"Q16900962\\\", [[1, 2, 3, 4]]], \\\"t\\\": [\\\"portland, oregon\\\", \\\"Q6106\\\", [[20, 21, 22]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airline\\\", \\\"\\\\u2019s\\\", \\\"main\\\", \\\"base\\\", \\\"is\\\", \\\"at\\\", \\\"Majuro\\\", \\\"and\\\", \\\"operates\\\", \\\"flights\\\", \\\"to\\\", \\\"Bikini\\\", \\\"Atoll\\\", \\\",\\\", \\\"Enewetak\\\", \\\"Atoll\\\", \\\",\\\", \\\"Kwajalein\\\", \\\"Atoll\\\", \\\",\\\", \\\"Rongelap\\\", \\\"Atoll\\\", \\\"and\\\", \\\"Jeh\\\", \\\"and\\\", \\\"Woja\\\", \\\"on\\\", \\\"Ailinglaplap\\\", \\\"Atoll\\\", \\\".\\\"], \\\"h\\\": [\\\"woja\\\", \\\"Q8029103\\\", [[26]]], \\\"t\\\": [\\\"ailinglaplap atoll\\\", \\\"Q405165\\\", [[28, 29]]]}, {\\\"tokens\\\": [\\\"Other\\\", \\\"McMurdo\\\", \\\"Station\\\", \\\"airfields\\\", \\\"include\\\", \\\"the\\\", \\\"Ice\\\", \\\"Runway\\\", \\\"(\\\", \\\"October\\\", \\\"to\\\", \\\"December\\\", \\\")\\\", \\\"and\\\", \\\"Pegasus\\\", \\\"Field\\\", \\\"used\\\", \\\"in\\\", \\\"August\\\", \\\"and\\\", \\\"December\\\", \\\"through\\\", \\\"to\\\", \\\"February\\\", \\\"of\\\", \\\"each\\\", \\\"season\\\", \\\".\\\"], \\\"h\\\": [\\\"pegasus field\\\", \\\"Q3374224\\\", [[14, 15]]], \\\"t\\\": [\\\"mcmurdo station\\\", \\\"Q498627\\\", [[1, 2]]]}, {\\\"tokens\\\": [\\\"Regional\\\", \\\"bus\\\", \\\"service\\\", \\\"can\\\", \\\"be\\\", \\\"found\\\", \\\"in\\\", \\\"North\\\", \\\"Adams\\\", \\\",\\\", \\\"as\\\", \\\"can\\\", \\\"regional\\\", \\\"air\\\", \\\"service\\\", \\\"at\\\", \\\"Harriman\\\", \\\"-\\\", \\\"and\\\", \\\"-\\\", \\\"West\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"harriman-and-west airport\\\", \\\"Q3887968\\\", [[16, 17, 18, 19, 20, 21]]], \\\"t\\\": [\\\"north adams\\\", \\\"Q49185\\\", [[7, 8]]]}, {\\\"tokens\\\": [\\\"A\\\", \\\"Beech\\\", \\\"King\\\", \\\"Air\\\", \\\"A100\\\", \\\"of\\\", \\\"Skyjet\\\", \\\"Aviation\\\", \\\"collided\\\", \\\"with\\\", \\\"a\\\", \\\"UAV\\\", \\\"as\\\", \\\"the\\\", \\\"former\\\", \\\"was\\\", \\\"approaching\\\", \\\"Jean\\\", \\\"Lesage\\\", \\\"Airport\\\", \\\"near\\\", \\\"Quebec\\\", \\\"City\\\", \\\".\\\"], \\\"h\\\": [\\\"jean lesage airport\\\", \\\"Q794549\\\", [[17, 18, 19]]], \\\"t\\\": [\\\"quebec city\\\", \\\"Q2145\\\", [[21, 22]]]}, {\\\"tokens\\\": [\\\"Brescia\\\", \\\"\\\\\\\"\\\", \\\"Gabriele\\\", \\\"D'Annunzio\\\", \\\"\\\\\\\"\\\", \\\"Airport\\\", \\\"(\\\", \\\",\\\", \\\")\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"Montichiari\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Montichiari\\\", \\\",\\\", \\\"southeast\\\", \\\"of\\\", \\\"City\\\", \\\"of\\\", \\\"Brescia\\\", \\\",\\\", \\\"Italy\\\", \\\".\\\"], \\\"h\\\": [\\\"montichiari airport\\\", \\\"Q1430989\\\", [[13, 14]]], \\\"t\\\": [\\\"brescia\\\", \\\"Q6221\\\", [[0], [25]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Wonsan\\\", \\\"International\\\", \\\"Friendship\\\", \\\"Air\\\", \\\"Festival\\\", \\\"or\\\", \\\"Wonsan\\\", \\\"Air\\\", \\\"Festival\\\", \\\"is\\\", \\\"an\\\", \\\"air\\\", \\\"show\\\", \\\"first\\\", \\\"held\\\", \\\"in\\\", \\\"September\\\", \\\"2016\\\", \\\"at\\\", \\\"Kalma\\\", \\\"Airport\\\", \\\"in\\\", \\\"Wonsan\\\", \\\",\\\", \\\"North\\\", \\\"Korea\\\", \\\".\\\"], \\\"h\\\": [\\\"kalma airport\\\", \\\"Q488368\\\", [[20, 21]]], \\\"t\\\": [\\\"wonsan\\\", \\\"Q109374\\\", [[1], [7], [23]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"1990\\\", \\\",\\\", \\\"in\\\", \\\"order\\\", \\\"to\\\", \\\"support\\\", \\\"steadily\\\", \\\"increasing\\\", \\\"demand\\\", \\\",\\\", \\\"Frasca\\\", \\\"International\\\", \\\"again\\\", \\\"relocated\\\", \\\"to\\\", \\\"a\\\", \\\"office\\\", \\\"building\\\", \\\"and\\\", \\\"manufacturing\\\", \\\"facility\\\", \\\"in\\\", \\\"Urbana\\\", \\\",\\\", \\\"Illinois\\\", \\\",\\\", \\\"adjacent\\\", \\\"to\\\", \\\"Frasca\\\", \\\"Field\\\", \\\".\\\"], \\\"h\\\": [\\\"frasca field\\\", \\\"Q5493537\\\", [[29, 30]]], \\\"t\\\": [\\\"urbana, illinois\\\", \\\"Q462184\\\", [[23, 24, 25]]]}, {\\\"tokens\\\": [\\\"Iola\\\", \\\"Township\\\", \\\"contains\\\", \\\"three\\\", \\\"airports\\\", \\\"or\\\", \\\"landing\\\", \\\"strips\\\", \\\":\\\", \\\"Allen\\\", \\\"County\\\", \\\"Airport\\\", \\\",\\\", \\\"Allen\\\", \\\"County\\\", \\\"Hospital\\\", \\\"Airport\\\", \\\"and\\\", \\\"Womack\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"allen county airport\\\", \\\"Q4731599\\\", [[9, 10, 11]]], \\\"t\\\": [\\\"iola\\\", \\\"Q1913925\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airport\\\", \\\"is\\\", \\\"expected\\\", \\\"to\\\", \\\"cease\\\", \\\"civilian\\\", \\\"flights\\\", \\\"once\\\", \\\"Eilat\\\", \\\"'s\\\", \\\"new\\\", \\\"international\\\", \\\"airport\\\", \\\"in\\\", \\\"Timna\\\", \\\"opens\\\", \\\".\\\"], \\\"h\\\": [\\\"timna\\\", \\\"Q2896949\\\", [[15]]], \\\"t\\\": [\\\"eilat\\\", \\\"Q134762\\\", [[9]]]}, {\\\"tokens\\\": [\\\"Taravella\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"C\\\\u00f3rdoba\\\", \\\",\\\", \\\"to\\\", \\\"General\\\", \\\"Enrique\\\", \\\"Mosconi\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Comodoro\\\", \\\"Rivadavia\\\", \\\",\\\", \\\"with\\\", \\\"stopovers\\\", \\\"at\\\", \\\"Governor\\\", \\\"Francisco\\\", \\\"Gabrielli\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Mendoza\\\", \\\",\\\", \\\"and\\\", \\\"Presidente\\\", \\\"Per\\\\u00f3n\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Neuqu\\\\u00e9n\\\", \\\".\\\"], \\\"h\\\": [\\\"general enrique mosconi international airport\\\", \\\"Q3275909\\\", [[7, 8, 9, 10, 11]]], \\\"t\\\": [\\\"comodoro rivadavia\\\", \\\"Q221921\\\", [[13, 14]]]}, {\\\"tokens\\\": [\\\"McCarran\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"the\\\", \\\"world\\\", \\\"'s\\\", \\\"ninth\\\", \\\"busiest\\\", \\\"airport\\\", \\\"by\\\", \\\"traffic\\\", \\\"movements\\\", \\\",\\\", \\\"is\\\", \\\"five\\\", \\\"miles\\\", \\\"from\\\", \\\"downtown\\\", \\\"Las\\\", \\\"Vegas\\\", \\\",\\\", \\\"and\\\", \\\"is\\\", \\\"the\\\", \\\"only\\\", \\\"commercial\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"Las\\\", \\\"Vegas\\\", \\\"Valley\\\", \\\".\\\"], \\\"h\\\": [\\\"mccarran international airport\\\", \\\"Q853886\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"las vegas valley\\\", \\\"Q2624848\\\", [[30, 31, 32]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"base\\\", \\\"was\\\", \\\"at\\\", \\\"Tampere\\\", \\\"-\\\", \\\"Pirkkala\\\", \\\"Airport\\\", \\\"(\\\", \\\"TMP\\\", \\\")\\\", \\\",\\\", \\\"Tampere\\\", \\\".\\\"], \\\"h\\\": [\\\"pirkkala airport\\\", \\\"Q1126306\\\", [[7, 8]]], \\\"t\\\": [\\\"tampere\\\", \\\"Q40840\\\", [[5], [13]]]}, {\\\"tokens\\\": [\\\"Nyanga\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airstrip\\\", \\\"serving\\\", \\\"the\\\", \\\"village\\\", \\\"of\\\", \\\"Nianga\\\", \\\"in\\\", \\\"Kasai\\\", \\\"-\\\", \\\"Occidental\\\", \\\"Province\\\", \\\",\\\", \\\"Democratic\\\", \\\"Republic\\\", \\\"of\\\", \\\"the\\\", \\\"Congo\\\", \\\".\\\"], \\\"h\\\": [\\\"nyanga airport\\\", \\\"Q25036858\\\", [[0, 1]]], \\\"t\\\": [\\\"nianga\\\", \\\"Q25906220\\\", [[9]]]}, {\\\"tokens\\\": [\\\"Daocheng\\\", \\\"Yading\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Daocheng\\\", \\\"County\\\", \\\"in\\\", \\\"the\\\", \\\"Garz\\\\u00ea\\\", \\\"Tibetan\\\", \\\"Autonomous\\\", \\\"Prefecture\\\", \\\"of\\\", \\\"Sichuan\\\", \\\"province\\\", \\\",\\\", \\\"China\\\", \\\".\\\"], \\\"h\\\": [\\\"daocheng yading airport\\\", \\\"Q1708704\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"daocheng county\\\", \\\"Q1165396\\\", [[7, 8]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Akanu\\\", \\\"Ibiam\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Enugu\\\", \\\",\\\", \\\"the\\\", \\\"Akanu\\\", \\\"Ibiam\\\", \\\"Federal\\\", \\\"Polytechnic\\\", \\\",\\\", \\\"Unwana\\\", \\\",\\\", \\\"Ebonyi\\\", \\\"State\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"Francis\\\", \\\"Akanu\\\", \\\"Ibiam\\\", \\\"stadium\\\", \\\"University\\\", \\\"of\\\", \\\"Nigeria\\\", \\\",\\\", \\\"Nsukka\\\", \\\"are\\\", \\\"named\\\", \\\"after\\\", \\\"him\\\", \\\".\\\"], \\\"h\\\": [\\\"akanu ibiam international airport\\\", \\\"Q3497354\\\", [[1, 2, 3, 4]]], \\\"t\\\": [\\\"enugu\\\", \\\"Q465022\\\", [[6]]]}, {\\\"tokens\\\": [\\\"Prince\\\", \\\"Said\\\", \\\"Ibrahim\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\"French\\\", \\\":\\\", \\\"\\\\\\\"\\\", \\\"A\\\\u00e9roport\\\", \\\"international\\\", \\\"Moroni\\\", \\\"Prince\\\", \\\"Sa\\\\u00efd\\\", \\\"Ibrahim\\\", \\\"\\\\\\\"\\\", \\\",\\\", \\\"AIMPSI\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"international\\\", \\\"airport\\\", \\\"serving\\\", \\\"Moroni\\\", \\\"in\\\", \\\"Comoros\\\", \\\".\\\"], \\\"h\\\": [\\\"prince said ibrahim international airport\\\", \\\"Q653299\\\", [[0, 1, 2, 3, 4]]], \\\"t\\\": [\\\"moroni\\\", \\\"Q3901\\\", [[11], [24]]]}, {\\\"tokens\\\": [\\\"Since\\\", \\\"2008\\\", \\\"Eastern\\\", \\\"Airways\\\", \\\"has\\\", \\\"been\\\", \\\"providing\\\", \\\"fixed\\\", \\\"wing\\\", \\\"services\\\", \\\"to\\\", \\\"and\\\", \\\"from\\\", \\\"Aberdeen\\\", \\\"Airport\\\", \\\"and\\\", \\\"Scatsta\\\", \\\"Airport\\\", \\\"in\\\", \\\"Shetland\\\", \\\".\\\"], \\\"h\\\": [\\\"scatsta airport\\\", \\\"Q1915140\\\", [[16, 17]]], \\\"t\\\": [\\\"shetland\\\", \\\"Q47134\\\", [[19]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"city\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Carriel\\\", \\\"Sur\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Talcahuano\\\", \\\".\\\"], \\\"h\\\": [\\\"carriel sur international airport\\\", \\\"Q127721\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"talcahuano\\\", \\\"Q41997\\\", [[10]]]}, {\\\"tokens\\\": [\\\"State\\\", \\\"capital\\\", \\\"Shillong\\\", \\\"has\\\", \\\"an\\\", \\\"airport\\\", \\\"at\\\", \\\"Umroi\\\", \\\"from\\\", \\\"Shillong\\\", \\\"on\\\", \\\"the\\\", \\\"Guwahati\\\", \\\"-\\\", \\\"Shillong\\\", \\\"highway\\\", \\\".\\\"], \\\"h\\\": [\\\"umroi\\\", \\\"Q1931305\\\", [[7]]], \\\"t\\\": [\\\"shillong\\\", \\\"Q207752\\\", [[2], [9], [14]]]}, {\\\"tokens\\\": [\\\"Bar\\\", \\\"Harbor\\\", \\\"'s\\\", \\\"first\\\", \\\"crash\\\", \\\",\\\", \\\"on\\\", \\\"August\\\", \\\"16\\\", \\\",\\\", \\\"1976\\\", \\\",\\\", \\\"was\\\", \\\"on\\\", \\\"a\\\", \\\"cargo\\\", \\\"flight\\\", \\\"from\\\", \\\"Bangor\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Bangor\\\", \\\",\\\", \\\"Maine\\\", \\\",\\\", \\\"to\\\", \\\"Bar\\\", \\\"Harbor\\\", \\\".\\\"], \\\"h\\\": [\\\"bangor international airport\\\", \\\"Q591971\\\", [[18, 19, 20]]], \\\"t\\\": [\\\"bangor, maine\\\", \\\"Q327012\\\", [[22, 23, 24]]]}, {\\\"tokens\\\": [\\\"Blue\\\", \\\"Air\\\", \\\"is\\\", \\\"an\\\", \\\"airline\\\", \\\"headquartered\\\", \\\"in\\\", \\\"Bucharest\\\", \\\",\\\", \\\"with\\\", \\\"its\\\", \\\"main\\\", \\\"hubs\\\", \\\"at\\\", \\\"Henri\\\", \\\"Coand\\\\u0103\\\", \\\"International\\\", \\\"Airport\\\", \\\"and\\\", \\\"Turin\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"henri coand\\\\u0103 international airport\\\", \\\"Q257631\\\", [[14, 15, 16, 17]]], \\\"t\\\": [\\\"bucharest\\\", \\\"Q19660\\\", [[7]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"September\\\", \\\"4\\\", \\\",\\\", \\\"1971\\\", \\\",\\\", \\\"the\\\", \\\"aircraft\\\", \\\"serving\\\", \\\"the\\\", \\\"flight\\\", \\\"crashed\\\", \\\"into\\\", \\\"a\\\", \\\"mountain\\\", \\\"in\\\", \\\"Haines\\\", \\\"Borough\\\", \\\",\\\", \\\"near\\\", \\\"Juneau\\\", \\\",\\\", \\\"Alaska\\\", \\\"(\\\", \\\"JNU\\\", \\\"/\\\", \\\"PAJN\\\", \\\")\\\", \\\"on\\\", \\\"approach\\\", \\\"for\\\", \\\"landing\\\", \\\".\\\"], \\\"h\\\": [\\\"pajn\\\", \\\"Q2505424\\\", [[26]]], \\\"t\\\": [\\\"juneau, alaska\\\", \\\"Q29445\\\", [[20, 21, 22]]]}, {\\\"tokens\\\": [\\\"Guymon\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"city\\\", \\\"-\\\", \\\"owned\\\", \\\",\\\", \\\"public\\\", \\\"-\\\", \\\"use\\\", \\\"airport\\\", \\\"located\\\", \\\"two\\\", \\\"nautical\\\", \\\"miles\\\", \\\"(\\\", \\\"3.7\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"west\\\", \\\"of\\\", \\\"the\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\"of\\\", \\\"City\\\", \\\"of\\\", \\\"Guymon\\\", \\\"in\\\", \\\"Texas\\\", \\\"County\\\", \\\".\\\"], \\\"h\\\": [\\\"guymon municipal airport\\\", \\\"Q5622848\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"city of guymon\\\", \\\"Q1920861\\\", [[29, 30, 31]]]}, {\\\"tokens\\\": [\\\"Xiangxi\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"scheduled\\\", \\\"to\\\", \\\"be\\\", \\\"constructed\\\", \\\"to\\\", \\\"serve\\\", \\\"Xiangxi\\\", \\\"Tujia\\\", \\\"and\\\", \\\"Miao\\\", \\\"Autonomous\\\", \\\"Prefecture\\\", \\\"in\\\", \\\"Hunan\\\", \\\"Province\\\", \\\",\\\", \\\"China\\\", \\\".\\\"], \\\"h\\\": [\\\"xiangxi airport\\\", \\\"Q19659470\\\", [[0, 1]]], \\\"t\\\": [\\\"xiangxi tujia and miao autonomous prefecture\\\", \\\"Q763069\\\", [[13, 14, 15, 16, 17, 18]]]}, {\\\"tokens\\\": [\\\"Basic\\\", \\\"flying\\\", \\\"training\\\", \\\",\\\", \\\"under\\\", \\\"the\\\", \\\"instruction\\\", \\\"of\\\", \\\"USAAC\\\", \\\"and\\\", \\\"RAF\\\", \\\"flight\\\", \\\"instructors\\\", \\\",\\\", \\\"lasted\\\", \\\"nine\\\", \\\"to\\\", \\\"ten\\\", \\\"weeks\\\", \\\"at\\\", \\\"either\\\", \\\"Cochran\\\", \\\"Field\\\", \\\"at\\\", \\\"Macon\\\", \\\",\\\", \\\"Georgia\\\", \\\"or\\\", \\\"Gunter\\\", \\\"Field\\\", \\\",\\\", \\\"Montgomery\\\", \\\",\\\", \\\"Alabama\\\", \\\".\\\"], \\\"h\\\": [\\\"cochran field\\\", \\\"Q3565917\\\", [[21, 22]]], \\\"t\\\": [\\\"macon, georgia\\\", \\\"Q219656\\\", [[24, 25, 26]]]}, {\\\"tokens\\\": [\\\"An\\\", \\\"example\\\", \\\"of\\\", \\\"the\\\", \\\"AVN-8\\\", \\\"is\\\", \\\"maintained\\\", \\\"in\\\", \\\"airworthy\\\", \\\"condition\\\", \\\"by\\\", \\\"the\\\", \\\"Historic\\\", \\\"Aircraft\\\", \\\"Restoration\\\", \\\"Museum\\\", \\\"at\\\", \\\"Creve\\\", \\\"Coeur\\\", \\\"Airport\\\", \\\"near\\\", \\\"St\\\", \\\"Louis\\\", \\\"Missouri\\\", \\\".\\\"], \\\"h\\\": [\\\"creve coeur airport\\\", \\\"Q1654844\\\", [[17, 18, 19]]], \\\"t\\\": [\\\"st louis\\\", \\\"Q38022\\\", [[21, 22]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"closest\\\", \\\"airport\\\", \\\"of\\\", \\\"any\\\", \\\"type\\\", \\\"is\\\", \\\"Marlboro\\\", \\\"Airport\\\", \\\"in\\\", \\\"Marlborough\\\", \\\",\\\", \\\"the\\\", \\\"closest\\\", \\\"with\\\", \\\"scheduled\\\", \\\"flights\\\", \\\"is\\\", \\\"Worcester\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Worcester\\\", \\\"and\\\", \\\"the\\\", \\\"closest\\\", \\\"with\\\", \\\"international\\\", \\\"service\\\", \\\"is\\\", \\\"Logan\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Boston\\\", \\\".\\\"], \\\"h\\\": [\\\"marlboro airport\\\", \\\"Q652230\\\", [[7, 8]]], \\\"t\\\": [\\\"marlborough\\\", \\\"Q54189\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Enrique\\\", \\\"Pi\\\\u00f1eyro\\\", \\\"takes\\\", \\\"his\\\", \\\"camera\\\", \\\",\\\", \\\"secretly\\\", \\\",\\\", \\\"into\\\", \\\"the\\\", \\\"control\\\", \\\"tower\\\", \\\"of\\\", \\\"the\\\", \\\"Ministro\\\", \\\"Pistarini\\\", \\\"International\\\", \\\"Airport\\\", \\\"also\\\", \\\"-\\\", \\\"known\\\", \\\"-\\\", \\\"as\\\", \\\"Ezeiza\\\", \\\",\\\", \\\"the\\\", \\\"international\\\", \\\"airport\\\", \\\"at\\\", \\\"Buenos\\\", \\\"Aires\\\", \\\".\\\"], \\\"h\\\": [\\\"ministro pistarini international airport\\\", \\\"Q384788\\\", [[14, 15, 16, 17]]], \\\"t\\\": [\\\"buenos aires\\\", \\\"Q1486\\\", [[29, 30]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Baker\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"one\\\", \\\"nautical\\\", \\\"mile\\\", \\\"(\\\", \\\"1.15\\\", \\\"\\\\u00a0\\\", \\\"mi\\\", \\\",\\\", \\\"1.85\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"southeast\\\", \\\"of\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\"of\\\", \\\"the\\\", \\\"City\\\", \\\"of\\\", \\\"Baker\\\", \\\"..\\\", \\\"Federal\\\", \\\"Aviation\\\", \\\"Administration\\\", \\\".\\\"], \\\"h\\\": [\\\"baker municipal airport\\\", \\\"Q2902480\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"city of baker\\\", \\\"Q955228\\\", [[25, 26, 27]]]}, {\\\"tokens\\\": [\\\"Fritzlar\\\", \\\"Air\\\", \\\"Base\\\", \\\"(\\\", \\\"German\\\", \\\":\\\", \\\"\\\\\\\"\\\", \\\"Heeresflugplatz\\\", \\\"Fritzlar\\\", \\\"\\\\\\\"\\\", \\\",\\\", \\\"IATA\\\", \\\":\\\", \\\"FRZ\\\", \\\",\\\", \\\"ICAO\\\", \\\":\\\", \\\"ETHF\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"military\\\", \\\"air\\\", \\\"field\\\", \\\"of\\\", \\\"the\\\", \\\"German\\\", \\\"Army\\\", \\\"Aviation\\\", \\\"Corps\\\", \\\".\\\"], \\\"h\\\": [\\\"ethf\\\", \\\"Q830551\\\", [[17]]], \\\"t\\\": [\\\"fritzlar\\\", \\\"Q492503\\\", [[0], [8]]]}, {\\\"tokens\\\": [\\\"Tanout\\\", \\\"Airport\\\", \\\"(\\\", \\\"ICAO\\\", \\\":\\\", \\\"DRZT\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Tanout\\\", \\\"in\\\", \\\"Niger\\\", \\\".\\\"], \\\"h\\\": [\\\"drzt\\\", \\\"Q13417236\\\", [[5]]], \\\"t\\\": [\\\"tanout\\\", \\\"Q448966\\\", [[0], [11]]]}, {\\\"tokens\\\": [\\\"After\\\", \\\"Kolkata\\\", \\\"airport\\\", \\\"the\\\", \\\"metro\\\", \\\"route\\\", \\\"will\\\", \\\"pass\\\", \\\"through\\\", \\\"a\\\", \\\"land\\\", \\\"owned\\\", \\\"by\\\", \\\"a\\\", \\\"private\\\", \\\"company\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q388535\\\", [[2]]], \\\"t\\\": [\\\"kolkata\\\", \\\"Q1348\\\", [[1]]]}, {\\\"tokens\\\": [\\\"At\\\", \\\"the\\\", \\\"time\\\", \\\",\\\", \\\"air\\\", \\\"traffic\\\", \\\"in\\\", \\\"the\\\", \\\"area\\\", \\\"centered\\\", \\\"on\\\", \\\"Lunken\\\", \\\"Airport\\\", \\\"just\\\", \\\"southeast\\\", \\\"of\\\", \\\"central\\\", \\\"Cincinnati\\\", \\\".\\\"], \\\"h\\\": [\\\"lunken airport\\\", \\\"Q3275007\\\", [[11, 12]]], \\\"t\\\": [\\\"cincinnati\\\", \\\"Q43196\\\", [[17]]]}, {\\\"tokens\\\": [\\\"Mahayogi\\\", \\\"Gorakhnath\\\", \\\"Airport\\\", \\\"or\\\", \\\"Gorakhpur\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"Gorakhpur\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"state\\\", \\\"of\\\", \\\"Uttar\\\", \\\"Pradesh\\\", \\\",\\\", \\\"India\\\", \\\".\\\"], \\\"h\\\": [\\\"mahayogi gorakhnath airport\\\", \\\"Q970413\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"gorakhpur\\\", \\\"Q244415\\\", [[4], [11]]]}, {\\\"tokens\\\": [\\\"To\\\", \\\"support\\\", \\\"this\\\", \\\"demand\\\", \\\",\\\", \\\"a\\\", \\\"county\\\", \\\"airport\\\", \\\"was\\\", \\\"built\\\", \\\"southwest\\\", \\\"of\\\", \\\"Marquette\\\", \\\",\\\", \\\"northeast\\\", \\\"of\\\", \\\"Negaunee\\\", \\\".\\\"], \\\"h\\\": [\\\"county airport\\\", \\\"Q6772584\\\", [[6, 7]]], \\\"t\\\": [\\\"marquette\\\", \\\"Q12443\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Juan\\\", \\\"Jos\\\\u00e9\\\", \\\"Rond\\\\u00f3n\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"high\\\", \\\"-\\\", \\\"elevation\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"Paipa\\\", \\\"in\\\", \\\"the\\\", \\\"Boyac\\\\u00e1\\\", \\\"Department\\\", \\\"of\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"juan jos\\\\u00e9 rond\\\\u00f3n airport\\\", \\\"Q28163906\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"paipa\\\", \\\"Q1391867\\\", [[14]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Francisco\\\", \\\"Carle\\\", \\\"Airport\\\", \\\"at\\\", \\\"Jauja\\\", \\\"offers\\\", \\\"daily\\\", \\\"connections\\\", \\\"to\\\", \\\"Lima\\\", \\\"and\\\", \\\"is\\\", \\\"located\\\", \\\"45\\\", \\\"minutes\\\", \\\"via\\\", \\\"car\\\", \\\"from\\\", \\\"Huancayo\\\", \\\".\\\"], \\\"h\\\": [\\\"francisco carle airport\\\", \\\"Q1431582\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"jauja\\\", \\\"Q917434\\\", [[5]]]}, {\\\"tokens\\\": [\\\"Silvia\\\", \\\"Pinto\\\", \\\"was\\\", \\\"among\\\", \\\"the\\\", \\\"42\\\", \\\"passengers\\\", \\\"aboard\\\", \\\"Aeronor\\\", \\\"Flight\\\", \\\"304\\\", \\\"that\\\", \\\"crashed\\\", \\\"near\\\", \\\"La\\\", \\\"Serena\\\", \\\"'s\\\", \\\"La\\\", \\\"Florida\\\", \\\"Airport\\\", \\\"on\\\", \\\"9\\\", \\\"December\\\", \\\"1982\\\", \\\".\\\"], \\\"h\\\": [\\\"la florida airport\\\", \\\"Q581901\\\", [[17, 18, 19]]], \\\"t\\\": [\\\"la serena\\\", \\\"Q14467\\\", [[14, 15]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Township\\\", \\\"is\\\", \\\"mostly\\\", \\\"an\\\", \\\"L\\\", \\\"-\\\", \\\"shape\\\", \\\"around\\\", \\\"the\\\", \\\"southwest\\\", \\\"side\\\", \\\"of\\\", \\\"the\\\", \\\"City\\\", \\\"of\\\", \\\"Flint\\\", \\\"and\\\", \\\"split\\\", \\\"in\\\", \\\"two\\\", \\\"along\\\", \\\"I-69/I-75\\\", \\\"interchange\\\", \\\"south\\\", \\\"along\\\", \\\"Bishop\\\", \\\"Airport\\\", \\\"to\\\", \\\"Mundy\\\", \\\"Township\\\", \\\".\\\"], \\\"h\\\": [\\\"bishop airport\\\", \\\"Q597396\\\", [[26, 27]]], \\\"t\\\": [\\\"city of flint\\\", \\\"Q490584\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"\\\\\\\"\\\", \\\"Eagles\\\", \\\"Airlines\\\", \\\"Via\\\", \\\"Banchina\\\", \\\"dei\\\", \\\"Molini\\\", \\\",\\\", \\\"8\\\", \\\"30175\\\", \\\"VENEZIA\\\", \\\"-\\\", \\\"Marghera\\\", \\\"\\\\\\\"\\\", \\\"Its\\\", \\\"hub\\\", \\\"was\\\", \\\"Venice\\\", \\\"Marco\\\", \\\"Polo\\\", \\\"Airport\\\", \\\"(\\\", \\\"VCE\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"venice marco polo airport\\\", \\\"Q849347\\\", [[17, 18, 19, 20]]], \\\"t\\\": [\\\"venezia\\\", \\\"Q641\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Kannur\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"under\\\", \\\"construction\\\", \\\"at\\\", \\\"Mattannur\\\", \\\"in\\\", \\\"Kannur\\\", \\\"district\\\", \\\"is\\\", \\\"expected\\\", \\\"to\\\", \\\"be\\\", \\\"operational\\\", \\\"by\\\", \\\"the\\\", \\\"end\\\", \\\"of\\\", \\\"September\\\", \\\"2017\\\", \\\"and\\\", \\\"is\\\", \\\"located\\\", \\\"18\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\"south\\\", \\\"-\\\", \\\"west\\\", \\\"of\\\", \\\"Iritty\\\", \\\".\\\"], \\\"h\\\": [\\\"kannur international airport\\\", \\\"Q3595649\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"kannur district\\\", \\\"Q2980652\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"From\\\", \\\"the\\\", \\\"1970s\\\", \\\"to\\\", \\\"the\\\", \\\"1990s\\\", \\\"plans\\\", \\\"were\\\", \\\"sold\\\", \\\"by\\\", \\\"Falconar\\\", \\\"Aviation\\\", \\\"of\\\", \\\"Edmonton\\\", \\\"(\\\", \\\"downtown\\\", \\\"municipal\\\", \\\"airport\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"downtown municipal airport\\\", \\\"Q3270356\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"edmonton\\\", \\\"Q2096\\\", [[13]]]}, {\\\"tokens\\\": [\\\"As\\\", \\\"the\\\", \\\"road\\\", \\\"approaches\\\", \\\"Crystal\\\", \\\"River\\\", \\\"Airport\\\", \\\",\\\", \\\"one\\\", \\\"truly\\\", \\\"begins\\\", \\\"to\\\", \\\"feel\\\", \\\"that\\\", \\\"he\\\", \\\"or\\\", \\\"she\\\", \\\"has\\\", \\\"entered\\\", \\\"the\\\", \\\"City\\\", \\\"of\\\", \\\"Crystal\\\", \\\"River\\\", \\\",\\\", \\\"since\\\", \\\"the\\\", \\\"Airport\\\", \\\"serves\\\", \\\"as\\\", \\\"the\\\", \\\"unofficial\\\", \\\"southern\\\", \\\"border\\\", \\\".\\\"], \\\"h\\\": [\\\"crystal river airport\\\", \\\"Q1655407\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"city of crystal river\\\", \\\"Q994967\\\", [[20, 21, 22, 23]]]}, {\\\"tokens\\\": [\\\"Harihar\\\", \\\"also\\\", \\\"has\\\", \\\"a\\\", \\\"private\\\", \\\"airport\\\", \\\"owned\\\", \\\"by\\\", \\\"Aditya\\\", \\\"Birla\\\", \\\"Group\\\", \\\"on\\\", \\\"their\\\", \\\"grounds\\\", \\\"and\\\", \\\"often\\\", \\\"used\\\", \\\"by\\\", \\\"politicians\\\", \\\"and\\\", \\\"famous\\\", \\\"personalities\\\", \\\".\\\"], \\\"h\\\": [\\\"airport owned by aditya birla group\\\", \\\"Q3888153\\\", [[5, 6, 7, 8, 9, 10]]], \\\"t\\\": [\\\"harihar\\\", \\\"Q1708108\\\", [[0]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"has\\\", \\\"been\\\", \\\"reported\\\", \\\"that\\\", \\\"Mendes\\\", \\\"came\\\", \\\"to\\\", \\\"physical\\\", \\\"blows\\\", \\\"at\\\", \\\"the\\\", \\\"Portela\\\", \\\"Airport\\\", \\\"in\\\", \\\"Lisbon\\\", \\\"with\\\", \\\"Lu\\\\u00eds\\\", \\\"Figo\\\", \\\"'s\\\", \\\"agent\\\", \\\",\\\", \\\"Jos\\\\u00e9\\\", \\\"Veiga\\\", \\\",\\\", \\\"whose\\\", \\\"influence\\\", \\\"he\\\", \\\"was\\\", \\\"gradually\\\", \\\"supplanting\\\", \\\"at\\\", \\\"this\\\", \\\"time\\\", \\\".\\\"], \\\"h\\\": [\\\"portela airport\\\", \\\"Q403671\\\", [[12, 13]]], \\\"t\\\": [\\\"lisbon\\\", \\\"Q597\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Chinchero\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"under\\\", \\\"construction\\\", \\\"airport\\\", \\\"in\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"Chinchero\\\", \\\"District\\\", \\\",\\\", \\\"Cusco\\\", \\\"Region\\\", \\\",\\\", \\\"Per\\\\u00fa\\\", \\\".\\\"], \\\"h\\\": [\\\"chinchero international airport\\\", \\\"Q18343134\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"cusco region\\\", \\\"Q5582862\\\", [[15, 16]]]}, {\\\"tokens\\\": [\\\"Puerto\\\", \\\"Maldonado\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"the\\\", \\\"Padre\\\", \\\"Aldamiz\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"padre aldamiz international airport\\\", \\\"Q656854\\\", [[6, 7, 8, 9]]], \\\"t\\\": [\\\"puerto maldonado\\\", \\\"Q541435\\\", [[0, 1]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"plane\\\", \\\"crashed\\\", \\\"shortly\\\", \\\"after\\\", \\\"takeoff\\\", \\\"from\\\", \\\"Pulkovo\\\", \\\"Airport\\\", \\\"in\\\", \\\"Leningrad\\\", \\\".\\\"], \\\"h\\\": [\\\"pulkovo airport\\\", \\\"Q690122\\\", [[7, 8]]], \\\"t\\\": [\\\"leningrad\\\", \\\"Q656\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Gonzalo\\\", \\\"Mej\\\\u00eda\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"southwest\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Turbo\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"Antioquia\\\", \\\"Department\\\", \\\"of\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"gonzalo mej\\\\u00eda airport\\\", \\\"Q20462075\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"turbo\\\", \\\"Q727559\\\", [[11]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"full\\\", \\\"scale\\\", \\\"tunnel\\\", \\\"is\\\", \\\"located\\\", \\\"adjacent\\\", \\\"to\\\", \\\"Concord\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Concord\\\", \\\",\\\", \\\"North\\\", \\\"Carolina\\\", \\\".\\\"], \\\"h\\\": [\\\"concord regional airport\\\", \\\"Q1655287\\\", [[8, 9, 10]]], \\\"t\\\": [\\\"concord, north carolina\\\", \\\"Q1030184\\\", [[12, 13, 14, 15]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"administrative\\\", \\\"center\\\", \\\"of\\\", \\\"the\\\", \\\"municipality\\\", \\\"is\\\", \\\"in\\\", \\\"Sisimiut\\\", \\\"(\\\", \\\"formerly\\\", \\\"called\\\", \\\"Holsteinsborg\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"sisimiut\\\", \\\"Q2875938\\\", [[8]]], \\\"t\\\": [\\\"holsteinsborg\\\", \\\"Q208098\\\", [[12]]]}, {\\\"tokens\\\": [\\\"As\\\", \\\"of\\\", \\\"August\\\", \\\"2011\\\", \\\",\\\", \\\"three\\\", \\\"Lionhearts\\\", \\\"are\\\", \\\"registered\\\", \\\"in\\\", \\\"the\\\", \\\"United\\\", \\\"States\\\", \\\",\\\", \\\"with\\\", \\\"another\\\", \\\"example\\\", \\\"on\\\", \\\"display\\\", \\\"in\\\", \\\"an\\\", \\\"aviation\\\", \\\"museum\\\", \\\"at\\\", \\\"Tullahoma\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Tullahoma\\\", \\\",\\\", \\\"Tennessee\\\", \\\".\\\"], \\\"h\\\": [\\\"tullahoma regional airport\\\", \\\"Q7852144\\\", [[24, 25, 26]]], \\\"t\\\": [\\\"tullahoma, tennessee\\\", \\\"Q3292530\\\", [[28, 29, 30]]]}, {\\\"tokens\\\": [\\\"Perhaps\\\", \\\"Eastleigh\\\", \\\"'s\\\", \\\"best\\\", \\\"-\\\", \\\"known\\\", \\\"'\\\", \\\"resident\\\", \\\"'\\\", \\\"is\\\", \\\"the\\\", \\\"Spitfire\\\", \\\"aeroplane\\\", \\\"which\\\", \\\"was\\\", \\\"built\\\", \\\"in\\\", \\\"Southampton\\\", \\\"and\\\", \\\"first\\\", \\\"flown\\\", \\\"from\\\", \\\"Eastleigh\\\", \\\"Aerodrome\\\", \\\".\\\"], \\\"h\\\": [\\\"eastleigh aerodrome\\\", \\\"Q8988\\\", [[22, 23]]], \\\"t\\\": [\\\"southampton\\\", \\\"Q79848\\\", [[17]]]}, {\\\"tokens\\\": [\\\"Dang\\\", \\\"Xuan\\\", \\\"Dieu\\\", \\\",\\\", \\\"32\\\", \\\",\\\", \\\"and\\\", \\\"Ho\\\", \\\"Duc\\\", \\\"Hoa\\\", \\\",\\\", \\\"37\\\", \\\"were\\\", \\\"detained\\\", \\\"on\\\", \\\"July\\\", \\\"30\\\", \\\"at\\\", \\\"Tan\\\", \\\"Son\\\", \\\"Nhat\\\", \\\"airport\\\", \\\"in\\\", \\\"Ho\\\", \\\"Chi\\\", \\\"Minh\\\", \\\"City\\\", \\\".\\\"], \\\"h\\\": [\\\"tan son nhat airport\\\", \\\"Q478595\\\", [[18, 19, 20, 21]]], \\\"t\\\": [\\\"ho chi minh city\\\", \\\"Q1854\\\", [[23, 24, 25, 26]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"has\\\", \\\"its\\\", \\\"headquarters\\\", \\\"established\\\", \\\"in\\\", \\\"the\\\", \\\"Comodoro\\\", \\\"Arturo\\\", \\\"Merino\\\", \\\"Ben\\\\u00edtez\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Santiago\\\", \\\"de\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"comodoro arturo merino ben\\\\u00edtez international airport\\\", \\\"Q127671\\\", [[7, 8, 9, 10, 11, 12]]], \\\"t\\\": [\\\"santiago de chile\\\", \\\"Q2887\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"located\\\", \\\"southeast\\\", \\\"of\\\", \\\"Tracy\\\", \\\",\\\", \\\"at\\\", \\\"an\\\", \\\"elevation\\\", \\\"of\\\", \\\"59\\\", \\\"feet\\\", \\\"(\\\", \\\"18\\\", \\\"m\\\", \\\")\\\", \\\",\\\", \\\"and\\\", \\\"hosts\\\", \\\"the\\\", \\\"New\\\", \\\"Jerusalem\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"new jerusalem airport\\\", \\\"Q10853545\\\", [[21, 22, 23]]], \\\"t\\\": [\\\"tracy\\\", \\\"Q953409\\\", [[5]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"was\\\", \\\"headquartered\\\", \\\"at\\\", \\\"the\\\", \\\"Downtown\\\", \\\"Manhattan\\\", \\\"Heliport\\\", \\\",\\\", \\\"Pier\\\", \\\"6\\\", \\\"E\\\", \\\"River\\\", \\\"in\\\", \\\"Lower\\\", \\\"Manhattan\\\", \\\",\\\", \\\"New\\\", \\\"York\\\", \\\"City\\\", \\\".\\\"], \\\"h\\\": [\\\"downtown manhattan heliport\\\", \\\"Q1575175\\\", [[5, 6, 7]]], \\\"t\\\": [\\\"new york city\\\", \\\"Q60\\\", [[17, 18, 19]]]}, {\\\"tokens\\\": [\\\"Norfolk\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"(\\\", \\\"Karl\\\", \\\"Stefan\\\", \\\"Memorial\\\", \\\"Field\\\", \\\")\\\", \\\"is\\\", \\\"four\\\", \\\"miles\\\", \\\"southwest\\\", \\\"of\\\", \\\"Norfolk\\\", \\\",\\\", \\\"in\\\", \\\"Madison\\\", \\\"County\\\", \\\",\\\", \\\"Nebraska\\\", \\\".\\\"], \\\"h\\\": [\\\"karl stefan memorial field\\\", \\\"Q7051088\\\", [[4, 5, 6, 7]]], \\\"t\\\": [\\\"norfolk\\\", \\\"Q959951\\\", [[0], [14]]]}, {\\\"tokens\\\": [\\\"Arizona\\\", \\\"Helicopters\\\", \\\"was\\\", \\\"originally\\\", \\\"based\\\", \\\"out\\\", \\\"of\\\", \\\"Chandler\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"in\\\", \\\"Chandler\\\", \\\",\\\", \\\"Arizona\\\", \\\"and\\\", \\\"then\\\", \\\"moved\\\", \\\"to\\\", \\\"Scottsdale\\\", \\\"Airport\\\", \\\"in\\\", \\\"Scottsdale\\\", \\\",\\\", \\\"Arizona\\\", \\\".\\\"], \\\"h\\\": [\\\"chandler municipal airport\\\", \\\"Q1835578\\\", [[7, 8, 9]]], \\\"t\\\": [\\\"chandler, arizona\\\", \\\"Q49272\\\", [[11, 12, 13]]]}, {\\\"tokens\\\": [\\\"S\\\\u00e3o\\\", \\\"Paulo\\\", \\\"-\\\", \\\"Guarulhos\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\"GRU\\\", \\\")\\\", \\\",\\\", \\\"one\\\", \\\"of\\\", \\\"the\\\", \\\"main\\\", \\\"Brazilian\\\", \\\"airports\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"there\\\", \\\".\\\"], \\\"h\\\": [\\\"gru\\\", \\\"Q385406\\\", [[7]]], \\\"t\\\": [\\\"s\\\\u00e3o paulo\\\", \\\"Q174\\\", [[0, 1]]]}, {\\\"tokens\\\": [\\\"Alpine\\\", \\\"County\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"general\\\", \\\"aviation\\\", \\\"airport\\\", \\\"in\\\", \\\"the\\\", \\\"Eastern\\\", \\\"Sierra\\\", \\\"about\\\", \\\"from\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"Markleeville\\\", \\\".\\\"], \\\"h\\\": [\\\"alpine county airport\\\", \\\"Q2063727\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"markleeville\\\", \\\"Q1019532\\\", [[17]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Katajanokka\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"was\\\", \\\"the\\\", \\\"first\\\", \\\"airport\\\", \\\"in\\\", \\\"Finland\\\", \\\",\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"Katajanokka\\\", \\\"neighbourhood\\\", \\\"in\\\", \\\"Helsinki\\\", \\\".\\\"], \\\"h\\\": [\\\"katajanokka airport\\\", \\\"Q20732200\\\", [[1, 2]]], \\\"t\\\": [\\\"helsinki\\\", \\\"Q1757\\\", [[18]]]}, {\\\"tokens\\\": [\\\"At\\\", \\\"a\\\", \\\"junction\\\", \\\"northeast\\\", \\\"of\\\", \\\"the\\\", \\\"Huron\\\", \\\"County\\\", \\\"Memorial\\\", \\\"Airport\\\", \\\",\\\", \\\"M-19\\\", \\\"reaches\\\", \\\"its\\\", \\\"northern\\\", \\\"terminus\\\", \\\"at\\\", \\\"M-142\\\", \\\"just\\\", \\\"east\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Bad\\\", \\\"Axe\\\", \\\".\\\"], \\\"h\\\": [\\\"huron county memorial airport\\\", \\\"Q3085034\\\", [[6, 7, 8, 9]]], \\\"t\\\": [\\\"bad axe\\\", \\\"Q628503\\\", [[24, 25]]]}, {\\\"tokens\\\": [\\\"Taebukpo\\\", \\\"Ri\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"Pukp'o\\\", \\\"-\\\", \\\"ri\\\", \\\",\\\", \\\"Tosan\\\", \\\"County\\\", \\\",\\\", \\\"Hwanghae\\\", \\\"-\\\", \\\"bukto\\\", \\\",\\\", \\\"North\\\", \\\"Korea\\\", \\\".\\\"], \\\"h\\\": [\\\"taebukpo ri airport\\\", \\\"Q2649112\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"tosan county\\\", \\\"Q711044\\\", [[11, 12]]]}, {\\\"tokens\\\": [\\\"Puerto\\\", \\\"Ayacucho\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"the\\\", \\\"small\\\", \\\"Cacique\\\", \\\"Aramare\\\", \\\"Airport\\\", \\\",\\\", \\\"and\\\", \\\"has\\\", \\\"good\\\", \\\"bus\\\", \\\"connections\\\", \\\"to\\\", \\\"San\\\", \\\"Fernando\\\", \\\",\\\", \\\"El\\\", \\\"Burro\\\", \\\",\\\", \\\"San\\\", \\\"F\\\\u00e9lix\\\", \\\"and\\\", \\\"Ciudad\\\", \\\"Bol\\\\u00edvar\\\", \\\".\\\"], \\\"h\\\": [\\\"cacique aramare airport\\\", \\\"Q1927833\\\", [[7, 8, 9]]], \\\"t\\\": [\\\"puerto ayacucho\\\", \\\"Q372920\\\", [[0, 1]]]}, {\\\"tokens\\\": [\\\"Nor\\\\u00f0fj\\\\u00f6r\\\\u00f0ur\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Neskaupsta\\\\u00f0ur\\\", \\\",\\\", \\\"Iceland\\\", \\\".\\\"], \\\"h\\\": [\\\"nor\\\\u00f0fj\\\\u00f6r\\\\u00f0ur airport\\\", \\\"Q12694186\\\", [[0, 1]]], \\\"t\\\": [\\\"neskaupsta\\\\u00f0ur\\\", \\\"Q176728\\\", [[6]]]}, {\\\"tokens\\\": [\\\"Attractions\\\", \\\"in\\\", \\\"Sand\\\", \\\"Springs\\\", \\\"include\\\", \\\"the\\\", \\\"Keystone\\\", \\\"Ancient\\\", \\\"Forest\\\", \\\",\\\", \\\"Sand\\\", \\\"Springs\\\", \\\"Pogue\\\", \\\"Airport\\\", \\\",\\\", \\\"the\\\", \\\"Canyons\\\", \\\"at\\\", \\\"Blackjack\\\", \\\"Ridge\\\", \\\"Golf\\\", \\\"Course\\\", \\\"and\\\", \\\"easy\\\", \\\"access\\\", \\\"to\\\", \\\"Keystone\\\", \\\"State\\\", \\\"Park\\\", \\\".\\\"], \\\"h\\\": [\\\"pogue airport\\\", \\\"Q8017265\\\", [[12, 13]]], \\\"t\\\": [\\\"sand springs\\\", \\\"Q2220501\\\", [[2, 3], [10, 11]]]}, {\\\"tokens\\\": [\\\"Vopnafj\\\\u00f6r\\\\u00f0ur\\\", \\\"is\\\", \\\"on\\\", \\\"Route\\\", \\\"85\\\", \\\"and\\\", \\\"has\\\", \\\"an\\\", \\\"airport\\\", \\\"with\\\", \\\"scheduled\\\", \\\"flights\\\", \\\"to\\\", \\\"Akureyri\\\", \\\"on\\\", \\\"business\\\", \\\"days\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q2875989\\\", [[8]]], \\\"t\\\": [\\\"vopnafj\\\\u00f6r\\\\u00f0ur\\\", \\\"Q925686\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Kandahar\\\", \\\"International\\\", \\\"Airport\\\", \\\"(;\\\", \\\"referred\\\", \\\"to\\\", \\\"by\\\", \\\"ISAF\\\", \\\"as\\\", \\\"Kandahar\\\", \\\"Airfield\\\", \\\",\\\", \\\"KAF\\\", \\\")\\\", \\\"is\\\", \\\"located\\\", \\\"south\\\", \\\"-\\\", \\\"east\\\", \\\"of\\\", \\\"Kandahar\\\", \\\"City\\\", \\\"in\\\", \\\"Afghanistan\\\", \\\".\\\"], \\\"h\\\": [\\\"kandahar airfield\\\", \\\"Q33156\\\", [[9, 10]]], \\\"t\\\": [\\\"kandahar city\\\", \\\"Q45604\\\", [[20, 21]]]}, {\\\"tokens\\\": [\\\"Jorge\\\", \\\"Enrique\\\", \\\"Gonz\\\\u00e1lez\\\", \\\"Torres\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"San\\\", \\\"Jos\\\\u00e9\\\", \\\"del\\\", \\\"Guaviare\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\"of\\\", \\\"the\\\", \\\"Guaviare\\\", \\\"Department\\\", \\\"of\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"jorge enrique gonz\\\\u00e1lez torres airport\\\", \\\"Q2902825\\\", [[0, 1, 2, 3, 4]]], \\\"t\\\": [\\\"san jos\\\\u00e9 del guaviare\\\", \\\"Q864675\\\", [[11, 12, 13, 14]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Hallinportti\\\", \\\"Aviation\\\", \\\"Museum\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"aviation\\\", \\\"museum\\\", \\\",\\\", \\\"located\\\", \\\"at\\\", \\\"Halli\\\", \\\"Airport\\\", \\\"in\\\", \\\"Kuorevesi\\\", \\\",\\\", \\\"J\\\\u00e4ms\\\\u00e4\\\", \\\",\\\", \\\"Finland\\\", \\\".\\\"], \\\"h\\\": [\\\"halli airport\\\", \\\"Q2627988\\\", [[13, 14]]], \\\"t\\\": [\\\"j\\\\u00e4ms\\\\u00e4\\\", \\\"Q642696\\\", [[18]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Santiago\\\", \\\"Light\\\", \\\"Rail\\\", \\\"is\\\", \\\"a\\\", \\\"planned\\\", \\\"light\\\", \\\"rail\\\", \\\"system\\\", \\\"within\\\", \\\"the\\\", \\\"City\\\", \\\"of\\\", \\\"Santiago\\\", \\\"de\\\", \\\"los\\\", \\\"Caballeros\\\", \\\",\\\", \\\"Dominican\\\", \\\"Republic\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"Cibao\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"cibao international airport\\\", \\\"Q1431111\\\", [[24, 25, 26]]], \\\"t\\\": [\\\"santiago de los caballeros\\\", \\\"Q42763\\\", [[14, 15, 16, 17]]]}, {\\\"tokens\\\": [\\\"Tangier\\\", \\\"'s\\\", \\\"Ibn\\\", \\\"Battouta\\\", \\\"Airport\\\", \\\"is\\\", \\\"the\\\", \\\"busiest\\\", \\\"airport\\\", \\\"in\\\", \\\"the\\\", \\\"region\\\", \\\".\\\"], \\\"h\\\": [\\\"ibn battouta airport\\\", \\\"Q1433022\\\", [[2, 3, 4]]], \\\"t\\\": [\\\"tangier\\\", \\\"Q126148\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Continental\\\", \\\"Airlines\\\", \\\"Flight\\\", \\\"1883\\\", \\\"was\\\", \\\"a\\\", \\\"regularly\\\", \\\"scheduled\\\", \\\"domestic\\\", \\\"passenger\\\", \\\"flight\\\", \\\"to\\\", \\\"Newark\\\", \\\"from\\\", \\\"Orlando\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Orlando\\\", \\\",\\\", \\\"Florida\\\", \\\".\\\"], \\\"h\\\": [\\\"orlando international airport\\\", \\\"Q929859\\\", [[14, 15, 16]]], \\\"t\\\": [\\\"orlando, florida\\\", \\\"Q49233\\\", [[18, 19, 20]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Pacific\\\", \\\"Flying\\\", \\\"Club\\\", \\\"is\\\", \\\"a\\\", \\\"flight\\\", \\\"school\\\", \\\"based\\\", \\\"out\\\", \\\"of\\\", \\\"Boundary\\\", \\\"Bay\\\", \\\"Airport\\\", \\\"in\\\", \\\"Delta\\\", \\\",\\\", \\\"British\\\", \\\"Columbia\\\", \\\".\\\"], \\\"h\\\": [\\\"boundary bay airport\\\", \\\"Q829643\\\", [[11, 12, 13]]], \\\"t\\\": [\\\"delta, british columbia\\\", \\\"Q851838\\\", [[15, 16, 17, 18]]]}, {\\\"tokens\\\": [\\\"La\\\", \\\"Monta\\\\u00f1a\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airstrip\\\", \\\"east\\\", \\\"of\\\", \\\"Curic\\\\u00f3\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"the\\\", \\\"Maule\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"la monta\\\\u00f1a airport\\\", \\\"Q16890753\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"curic\\\\u00f3\\\", \\\"Q13030\\\", [[9]]]}, {\\\"tokens\\\": [\\\"For\\\", \\\"Air\\\", \\\"route\\\", \\\"Bhopal\\\", \\\"Raja\\\", \\\"Bhoj\\\", \\\"Airport\\\", \\\"and\\\", \\\"Indore\\\", \\\"Devi\\\", \\\"Ahilya\\\", \\\"Bai\\\", \\\"Holkar\\\", \\\"Airport\\\", \\\"are\\\", \\\"nearest\\\", \\\".\\\"], \\\"h\\\": [\\\"devi ahilya bai holkar airport\\\", \\\"Q1658243\\\", [[9, 10, 11, 12, 13]]], \\\"t\\\": [\\\"indore\\\", \\\"Q66616\\\", [[8]]]}, {\\\"tokens\\\": [\\\"There\\\", \\\"is\\\", \\\"also\\\", \\\"a\\\", \\\"heliport\\\", \\\"with\\\", \\\"the\\\", \\\"same\\\", \\\"name\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"village\\\", \\\"of\\\", \\\"Tasiusaq\\\", \\\"in\\\", \\\"the\\\", \\\"Kujalleq\\\", \\\"municipality\\\", \\\"in\\\", \\\"southern\\\", \\\"Greenland\\\", \\\".\\\"], \\\"h\\\": [\\\"heliport with the same name\\\", \\\"Q4993131\\\", [[4, 5, 6, 7, 8]]], \\\"t\\\": [\\\"tasiusaq\\\", \\\"Q736994\\\", [[14]]]}, {\\\"tokens\\\": [\\\"Allegiant\\\", \\\"operates\\\", \\\"a\\\", \\\"similar\\\", \\\"situation\\\", \\\"with\\\", \\\"Bellingham\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Bellingham\\\", \\\",\\\", \\\"Washington\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"close\\\", \\\"to\\\", \\\"Vancouver\\\", \\\".\\\"], \\\"h\\\": [\\\"bellingham international airport\\\", \\\"Q1657287\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"bellingham, washington\\\", \\\"Q430267\\\", [[10, 11, 12]]]}, {\\\"tokens\\\": [\\\"With\\\", \\\"then\\\", \\\",\\\", \\\"it\\\", \\\"organized\\\", \\\"an\\\", \\\"anti\\\", \\\"-\\\", \\\"submarine\\\", \\\"warfare\\\", \\\"flight\\\", \\\",\\\", \\\"initially\\\", \\\"based\\\", \\\"in\\\", \\\"the\\\", \\\"Aveiro\\\", \\\"Naval\\\", \\\"Air\\\", \\\"Station\\\", \\\"at\\\", \\\"the\\\", \\\"S\\\\u00e3o\\\", \\\"Jacinto\\\", \\\"Peninsula\\\", \\\".\\\"], \\\"h\\\": [\\\"s\\\\u00e3o jacinto peninsula\\\", \\\"Q972271\\\", [[22, 23, 24]]], \\\"t\\\": [\\\"aveiro\\\", \\\"Q485581\\\", [[16]]]}, {\\\"tokens\\\": [\\\"Marechal\\\", \\\"Rondon\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"which\\\", \\\"also\\\", \\\"serves\\\", \\\"Cuiab\\\\u00e1\\\", \\\"is\\\", \\\"located\\\", \\\"at\\\", \\\"V\\\\u00e1rzea\\\", \\\"Grande\\\", \\\".\\\"], \\\"h\\\": [\\\"marechal rondon international airport\\\", \\\"Q1030919\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"cuiab\\\\u00e1\\\", \\\"Q170762\\\", [[8]]]}, {\\\"tokens\\\": [\\\"An\\\", \\\"airport\\\", \\\"in\\\", \\\"nearby\\\", \\\"Slia\\\\u010d\\\", \\\"offers\\\", \\\"direct\\\", \\\"flights\\\", \\\"to\\\", \\\"Prague\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q1432898\\\", [[1]]], \\\"t\\\": [\\\"slia\\\\u010d\\\", \\\"Q258439\\\", [[4]]]}, {\\\"tokens\\\": [\\\"Gyumri\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"the\\\", \\\"international\\\", \\\"Shirak\\\", \\\"Airport\\\", \\\",\\\", \\\"about\\\", \\\"to\\\", \\\"the\\\", \\\"southeast\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\"centre\\\", \\\".\\\"], \\\"h\\\": [\\\"shirak airport\\\", \\\"Q1431399\\\", [[6, 7]]], \\\"t\\\": [\\\"gyumri\\\", \\\"Q199500\\\", [[0]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"Porto\\\", \\\"Alegre\\\", \\\"on\\\", \\\"June\\\", \\\"24\\\", \\\",\\\", \\\"around\\\", \\\"200\\\", \\\"protesters\\\", \\\"gathered\\\", \\\"in\\\", \\\"the\\\", \\\"city\\\", \\\"center\\\", \\\"and\\\", \\\"travelled\\\", \\\"toward\\\", \\\"the\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"the airport\\\", \\\"Q1432702\\\", [[18, 19]]], \\\"t\\\": [\\\"porto alegre\\\", \\\"Q40269\\\", [[1, 2]]]}, {\\\"tokens\\\": [\\\"For\\\", \\\"international\\\", \\\"flights\\\", \\\",\\\", \\\"a\\\", \\\"Beechjet\\\", \\\"400A\\\", \\\"is\\\", \\\"used\\\", \\\"from\\\", \\\"its\\\", \\\"base\\\", \\\"at\\\", \\\"Ilopango\\\", \\\"Airport\\\", \\\"in\\\", \\\"the\\\", \\\"capital\\\", \\\",\\\", \\\"San\\\", \\\"Salvador\\\", \\\".\\\"], \\\"h\\\": [\\\"ilopango airport\\\", \\\"Q588038\\\", [[13, 14]]], \\\"t\\\": [\\\"san salvador\\\", \\\"Q3110\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"He\\\", \\\"proposed\\\", \\\"the\\\", \\\"contribution\\\", \\\"in\\\", \\\"coordination\\\", \\\"with\\\", \\\"the\\\", \\\"City\\\", \\\"of\\\", \\\"U\\\\u017eice\\\", \\\"and\\\", \\\"eight\\\", \\\"other\\\", \\\"municipalities\\\", \\\"who\\\", \\\"offered\\\", \\\"to\\\", \\\"contribute\\\", \\\"an\\\", \\\"annual\\\", \\\"sum\\\", \\\"to\\\", \\\"Ponikve\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"ponikve airport\\\", \\\"Q2875789\\\", [[23, 24]]], \\\"t\\\": [\\\"u\\\\u017eice\\\", \\\"Q59473\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Las\\\", \\\"Flecheras\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"San\\\", \\\"Fernando\\\", \\\"de\\\", \\\"Apure\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\"of\\\", \\\"the\\\", \\\"Apure\\\", \\\"state\\\", \\\"in\\\", \\\"Venezuela\\\", \\\".\\\"], \\\"h\\\": [\\\"las flecheras airport\\\", \\\"Q6492201\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"san fernando de apure\\\", \\\"Q990764\\\", [[12, 13, 14, 15]]]}, {\\\"tokens\\\": [\\\"Buin\\\", \\\"Airport\\\", \\\"(\\\", \\\"IATA\\\", \\\":\\\", \\\"UBI\\\", \\\")\\\", \\\"was\\\", \\\"an\\\", \\\"airport\\\", \\\"located\\\", \\\"near\\\", \\\"Kara\\\", \\\",\\\", \\\"Bougainville\\\", \\\"Island\\\", \\\",\\\", \\\"Papua\\\", \\\"New\\\", \\\"Guinea\\\", \\\".\\\"], \\\"h\\\": [\\\"ubi\\\", \\\"Q4986699\\\", [[5]]], \\\"t\\\": [\\\"kara\\\", \\\"Q6367450\\\", [[12]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"1945\\\", \\\",\\\", \\\"two\\\", \\\"ZP-14\\\", \\\"replacement\\\", \\\"blimps\\\", \\\"were\\\", \\\"sent\\\", \\\"from\\\", \\\"Weeksville\\\", \\\",\\\", \\\"North\\\", \\\"Carolina\\\", \\\"to\\\", \\\"the\\\", \\\"Bermudas\\\", \\\"and\\\", \\\"Lajes\\\", \\\"before\\\", \\\"going\\\", \\\"on\\\", \\\"to\\\", \\\"Craw\\\", \\\"Field\\\", \\\"(\\\", \\\"Kenitra\\\", \\\"Air\\\", \\\"Base\\\", \\\")\\\", \\\"at\\\", \\\"Port\\\", \\\"Lyautey\\\", \\\".\\\"], \\\"h\\\": [\\\"craw field\\\", \\\"Q2876099\\\", [[23, 24]]], \\\"t\\\": [\\\"port lyautey\\\", \\\"Q478207\\\", [[31, 32]]]}, {\\\"tokens\\\": [\\\"Nnamdi\\\", \\\"Azikiwe\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"the\\\", \\\"main\\\", \\\"airport\\\", \\\"serving\\\", \\\"Abuja\\\", \\\"and\\\", \\\"the\\\", \\\"surrounding\\\", \\\"capital\\\", \\\"region\\\", \\\".\\\"], \\\"h\\\": [\\\"nnamdi azikiwe international airport\\\", \\\"Q525030\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"abuja\\\", \\\"Q3787\\\", [[9]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"base\\\", \\\"is\\\", \\\"\\\\n\\\", \\\"Presidente\\\", \\\"Carlos\\\", \\\"Ib\\\\u00e1\\\\u00f1ez\\\", \\\"del\\\", \\\"Campo\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Punta\\\", \\\"Arenas\\\", \\\".\\\"], \\\"h\\\": [\\\"presidente carlos ib\\\\u00e1\\\\u00f1ez del campo international airport\\\", \\\"Q919952\\\", [[5, 6, 7, 8, 9, 10, 11]]], \\\"t\\\": [\\\"punta arenas\\\", \\\"Q51599\\\", [[13, 14]]]}, {\\\"tokens\\\": [\\\"Earlier\\\", \\\"that\\\", \\\"day\\\", \\\"at\\\", \\\"Ngurah\\\", \\\"Rai\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Denpasar\\\", \\\",\\\", \\\"Indonesian\\\", \\\"police\\\", \\\"also\\\", \\\"arrested\\\", \\\"the\\\", \\\"following\\\", \\\"drug\\\", \\\"mules\\\", \\\"after\\\", \\\"they\\\", \\\"were\\\", \\\"found\\\", \\\"carrying\\\", \\\"various\\\", \\\"amounts\\\", \\\"of\\\", \\\"heroin\\\", \\\"concealed\\\", \\\"on\\\", \\\"their\\\", \\\"bodies\\\", \\\".\\\"], \\\"h\\\": [\\\"ngurah rai international airport\\\", \\\"Q1061846\\\", [[4, 5, 6, 7]]], \\\"t\\\": [\\\"denpasar\\\", \\\"Q11506\\\", [[9]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"5\\\", \\\"August\\\", \\\"2017\\\", \\\",\\\", \\\"he\\\", \\\"made\\\", \\\"his\\\", \\\"first\\\", \\\"official\\\", \\\"visit\\\", \\\"to\\\", \\\"Libya\\\", \\\"after\\\", \\\"assuming\\\", \\\"the\\\", \\\"role\\\", \\\"of\\\", \\\"the\\\", \\\"head\\\", \\\"of\\\", \\\"UNSMIL\\\", \\\"by\\\", \\\"arriving\\\", \\\"at\\\", \\\"Mitiga\\\", \\\"Airport\\\", \\\"in\\\", \\\"Tripoli\\\", \\\".\\\"], \\\"h\\\": [\\\"mitiga airport\\\", \\\"Q45000\\\", [[25, 26]]], \\\"t\\\": [\\\"tripoli\\\", \\\"Q3579\\\", [[28]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"privately\\\", \\\"owned\\\", \\\"by\\\", \\\"Lakeway\\\", \\\"Airpark\\\", \\\",\\\", \\\"Inc.\\\", \\\"and\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Lakeway\\\", \\\",\\\", \\\"Texas\\\", \\\".\\\"], \\\"h\\\": [\\\"lakeway airpark\\\", \\\"Q6479336\\\", [[5, 6]]], \\\"t\\\": [\\\"lakeway, texas\\\", \\\"Q974112\\\", [[13, 14, 15]]]}, {\\\"tokens\\\": [\\\"Benjam\\\\u00edn\\\", \\\"Rivera\\\", \\\"Noriega\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"use\\\", \\\"airport\\\", \\\"located\\\", \\\"on\\\", \\\"the\\\", \\\"island\\\", \\\"of\\\", \\\"Culebra\\\", \\\"in\\\", \\\"Puerto\\\", \\\"Rico\\\", \\\".\\\"], \\\"h\\\": [\\\"benjam\\\\u00edn rivera noriega airport\\\", \\\"Q620090\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"culebra\\\", \\\"Q775056\\\", [[14]]]}, {\\\"tokens\\\": [\\\"Rourkela\\\", \\\"also\\\", \\\"has\\\", \\\"a\\\", \\\"private\\\", \\\"airport\\\", \\\"maintained\\\", \\\"by\\\", \\\"SAIL\\\", \\\"which\\\", \\\"is\\\", \\\"used\\\", \\\"only\\\", \\\"for\\\", \\\"official\\\", \\\"purposes\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q7371313\\\", [[5]]], \\\"t\\\": [\\\"rourkela\\\", \\\"Q1012706\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Toronto\\\", \\\"/\\\", \\\"Buttonville\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"(\\\", \\\"IATA\\\", \\\":\\\", \\\"YKZ\\\", \\\")\\\", \\\"in\\\", \\\"Markham\\\", \\\"provides\\\", \\\"general\\\", \\\"aviation\\\", \\\"facilities\\\", \\\".\\\"], \\\"h\\\": [\\\"buttonville municipal airport\\\", \\\"Q2928993\\\", [[2, 3, 4]]], \\\"t\\\": [\\\"markham\\\", \\\"Q44016\\\", [[11]]]}, {\\\"tokens\\\": [\\\"At\\\", \\\"first\\\", \\\"the\\\", \\\"Trondheim\\\", \\\"route\\\", \\\"was\\\", \\\"flown\\\", \\\"to\\\", \\\"Lade\\\", \\\",\\\", \\\"but\\\", \\\"were\\\", \\\"quickly\\\", \\\"transferred\\\", \\\"to\\\", \\\"the\\\", \\\"current\\\", \\\"airport\\\", \\\"at\\\", \\\"V\\\\u00e6rnes\\\", \\\".\\\", \\\"Wisting\\\", \\\",\\\", \\\"1989\\\", \\\":\\\", \\\"71\\\", \\\"Loftlei\\\\u00f0ir\\\", \\\"started\\\", \\\"flights\\\", \\\"to\\\", \\\"Reykjav\\\\u00edk\\\", \\\"in\\\", \\\"1952\\\", \\\".\\\"], \\\"h\\\": [\\\"v\\\\u00e6rnes\\\", \\\"Q729886\\\", [[19]]], \\\"t\\\": [\\\"trondheim\\\", \\\"Q25804\\\", [[3]]]}, {\\\"tokens\\\": [\\\"Huffman\\\", \\\"Aviation\\\", \\\"was\\\", \\\"a\\\", \\\"flight\\\", \\\"-\\\", \\\"training\\\", \\\"school\\\", \\\"in\\\", \\\"Venice\\\", \\\",\\\", \\\"Florida\\\", \\\"at\\\", \\\"Venice\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"venice municipal airport\\\", \\\"Q7919997\\\", [[13, 14, 15]]], \\\"t\\\": [\\\"venice, florida\\\", \\\"Q57325\\\", [[9, 10, 11]]]}, {\\\"tokens\\\": [\\\"This\\\", \\\"car\\\", \\\",\\\", \\\"the\\\", \\\"\\\\\\\"\\\", \\\"Panorama\\\", \\\"City\\\", \\\"Special\\\", \\\"\\\\\\\"\\\", \\\",\\\", \\\"debuted\\\", \\\"at\\\", \\\"the\\\", \\\"first\\\", \\\"NHRA\\\", \\\"U.S.\\\", \\\"Nationals\\\", \\\"at\\\", \\\"the\\\", \\\"Great\\\", \\\"Bend\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"in\\\", \\\"Great\\\", \\\"Bend\\\", \\\",\\\", \\\"Kansas\\\", \\\"in\\\", \\\"1955.Taylor\\\", \\\",\\\", \\\"Thom\\\", \\\".\\\"], \\\"h\\\": [\\\"great bend municipal airport\\\", \\\"Q3914445\\\", [[19, 20, 21, 22]]], \\\"t\\\": [\\\"great bend, kansas\\\", \\\"Q1065459\\\", [[24, 25, 26, 27]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"2017\\\", \\\",\\\", \\\"The\\\", \\\"Texas\\\", \\\"Mile\\\", \\\"relocated\\\", \\\"to\\\", \\\"its\\\", \\\"new\\\", \\\"\\\\\\\"\\\", \\\"home\\\", \\\"\\\\\\\"\\\", \\\"at\\\", \\\"the\\\", \\\"Victoria\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Victoria\\\", \\\",\\\", \\\"Texas\\\", \\\".\\\"], \\\"h\\\": [\\\"victoria regional airport\\\", \\\"Q7926998\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"victoria, texas\\\", \\\"Q784496\\\", [[19, 20, 21]]]}, {\\\"tokens\\\": [\\\"Hoby\\\", \\\"Wolf\\\", \\\"Airport\\\", \\\",\\\", \\\",\\\", \\\"is\\\", \\\"a\\\", \\\"private\\\", \\\"airport\\\", \\\"located\\\", \\\"east\\\", \\\"of\\\", \\\"Eldersburg\\\", \\\",\\\", \\\"Maryland\\\", \\\".\\\"], \\\"h\\\": [\\\"hoby wolf airport\\\", \\\"Q19462343\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"eldersburg, maryland\\\", \\\"Q754876\\\", [[12, 13, 14]]]}, {\\\"tokens\\\": [\\\"Additionally\\\", \\\",\\\", \\\"the\\\", \\\"Ismail\\\", \\\"Mire\\\", \\\"International\\\", \\\"Airport\\\", \\\"began\\\", \\\"providing\\\", \\\"flights\\\", \\\"to\\\", \\\"and\\\", \\\"from\\\", \\\"Buuhoodle\\\", \\\"in\\\", \\\"April\\\", \\\"2014\\\", \\\".\\\"], \\\"h\\\": [\\\"ismail mire international airport\\\", \\\"Q25067584\\\", [[3, 4, 5, 6]]], \\\"t\\\": [\\\"buuhoodle\\\", \\\"Q1002700\\\", [[13]]]}, {\\\"tokens\\\": [\\\"TAB\\\", \\\"'s\\\", \\\"Base\\\", \\\"of\\\", \\\"operations\\\", \\\"was\\\", \\\"headquartered\\\", \\\"at\\\", \\\"El\\\", \\\"Alto\\\", \\\",\\\", \\\"adjacent\\\", \\\"to\\\", \\\"La\\\", \\\"Paz\\\", \\\"'s\\\", \\\"El\\\", \\\"Alto\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"el alto international airport\\\", \\\"Q1142225\\\", [[16, 17, 18, 19]]], \\\"t\\\": [\\\"la paz\\\", \\\"Q1491\\\", [[13, 14]]]}, {\\\"tokens\\\": [\\\"R\\\\u00fcgen\\\", \\\"Airport\\\", \\\"(\\\", \\\"\\\\\\\"\\\", \\\"Regionalflugplatz\\\", \\\"R\\\\u00fcgen\\\", \\\"\\\\\\\"\\\", \\\")\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"Bergen\\\", \\\"Airfield\\\", \\\"or\\\", \\\"G\\\\u00fcttin\\\", \\\"Airfield\\\", \\\"(\\\", \\\"\\\\\\\"\\\", \\\"Regionalflugplatz\\\", \\\"G\\\\u00fcttin\\\", \\\"\\\\\\\"\\\", \\\")\\\", \\\",\\\", \\\"(\\\", \\\"ICAO\\\", \\\":\\\", \\\"EDCG\\\\\\\"R\\\\u00fcgen\\\", \\\"Airport\\\", \\\"\\\\\\\"\\\", \\\"at\\\", \\\"www.fallingrain.com\\\", \\\".\\\"], \\\"h\\\": [\\\"bergen airfield\\\", \\\"Q832701\\\", [[12, 13]]], \\\"t\\\": [\\\"r\\\\u00fcgen\\\", \\\"Q3237\\\", [[0], [5]]]}, {\\\"tokens\\\": [\\\"Commercial\\\", \\\"aircraft\\\", \\\"fly\\\", \\\"into\\\", \\\"nearby\\\", \\\"Destin\\\", \\\"-\\\", \\\"Fort\\\", \\\"Walton\\\", \\\"Beach\\\", \\\"Airport\\\", \\\"/\\\", \\\"Eglin\\\", \\\"Air\\\", \\\"Force\\\", \\\"Base\\\", \\\",\\\", \\\"which\\\", \\\"also\\\", \\\"serves\\\", \\\"Fort\\\", \\\"Walton\\\", \\\"Beach\\\", \\\",\\\", \\\"Florida\\\", \\\".\\\"], \\\"h\\\": [\\\"eglin air force base\\\", \\\"Q1298115\\\", [[12, 13, 14, 15]]], \\\"t\\\": [\\\"fort walton beach, florida\\\", \\\"Q984368\\\", [[20, 21, 22, 23, 24]]]}, {\\\"tokens\\\": [\\\"Another\\\", \\\"alternative\\\", \\\"airport\\\", \\\"is\\\", \\\"the\\\", \\\"Sultan\\\", \\\"Abdul\\\", \\\"Halim\\\", \\\"Airport\\\", \\\",\\\", \\\"Alor\\\", \\\"Star\\\", \\\"(\\\", \\\"the\\\", \\\"state\\\", \\\"capital\\\", \\\"of\\\", \\\"Kedah\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"sultan abdul halim airport\\\", \\\"Q3235623\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"kedah\\\", \\\"Q188947\\\", [[17]]]}, {\\\"tokens\\\": [\\\"RAF\\\", \\\"Nutts\\\", \\\"Corner\\\", \\\"then\\\", \\\"became\\\", \\\"Belfast\\\", \\\"'s\\\", \\\"main\\\", \\\"airport\\\", \\\"(\\\", \\\"while\\\", \\\"Aldergrove\\\", \\\"would\\\", \\\"later\\\", \\\"become\\\", \\\"the\\\", \\\"primary\\\", \\\"airport\\\", \\\"in\\\", \\\"Northern\\\", \\\"Ireland\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"aldergrove\\\", \\\"Q8979\\\", [[11]]], \\\"t\\\": [\\\"belfast\\\", \\\"Q10686\\\", [[5]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"mall\\\", \\\"is\\\", \\\"about\\\", \\\"a\\\", \\\"15-minute\\\", \\\"drive\\\", \\\"from\\\", \\\"downtown\\\", \\\"Detroit\\\", \\\",\\\", \\\"Wayne\\\", \\\"State\\\", \\\"University\\\", \\\",\\\", \\\"or\\\", \\\"Metro\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"metro airport\\\", \\\"Q652505\\\", [[16, 17]]], \\\"t\\\": [\\\"detroit\\\", \\\"Q12439\\\", [[9]]]}, {\\\"tokens\\\": [\\\"Until\\\", \\\"December\\\", \\\"2011\\\", \\\"was\\\", \\\"based\\\", \\\"at\\\", \\\"the\\\", \\\"Airport\\\", \\\"of\\\", \\\"Mexico\\\", \\\"City\\\", \\\"and\\\", \\\"then\\\", \\\"has\\\", \\\"built\\\", \\\"new\\\", \\\"hangars\\\", \\\"and\\\", \\\"apron\\\", \\\"at\\\", \\\"the\\\", \\\"Capit\\\\u00e1n\\\", \\\"Rogelio\\\", \\\"Castillo\\\", \\\"National\\\", \\\"Airport\\\", \\\"located\\\", \\\"in\\\", \\\"Celaya\\\", \\\".\\\"], \\\"h\\\": [\\\"capit\\\\u00e1n rogelio castillo national airport\\\", \\\"Q3499964\\\", [[21, 22, 23, 24, 25]]], \\\"t\\\": [\\\"celaya\\\", \\\"Q580649\\\", [[28]]]}, {\\\"tokens\\\": [\\\"Daily\\\", \\\"Air\\\", \\\"is\\\", \\\"the\\\", \\\"only\\\", \\\"airline\\\", \\\"to\\\", \\\"offer\\\", \\\"flights\\\", \\\"from\\\", \\\"Taiwan\\\", \\\"Island\\\", \\\"through\\\", \\\"Taitung\\\", \\\"Airport\\\", \\\"in\\\", \\\"Taitung\\\", \\\"City\\\", \\\"to\\\", \\\"Orchid\\\", \\\"Island\\\", \\\"through\\\", \\\"its\\\", \\\"Lanyu\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"lanyu airport\\\", \\\"Q717735\\\", [[23, 24]]], \\\"t\\\": [\\\"orchid island\\\", \\\"Q701647\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"Cangyuan\\\", \\\"Washan\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Cangyuan\\\", \\\"Va\\\", \\\"Autonomous\\\", \\\"County\\\", \\\"in\\\", \\\"Lincang\\\", \\\",\\\", \\\"Yunnan\\\", \\\"province\\\", \\\",\\\", \\\"southwest\\\", \\\"China\\\", \\\".\\\"], \\\"h\\\": [\\\"cangyuan washan airport\\\", \\\"Q15838852\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"cangyuan va autonomous county\\\", \\\"Q1033239\\\", [[9, 10, 11, 12]]]}, {\\\"tokens\\\": [\\\"He\\\", \\\"named\\\", \\\"it\\\", \\\"\\\\\\\"\\\", \\\"Canberra\\\", \\\"\\\\\\\"\\\", \\\",\\\", \\\"and\\\", \\\"used\\\", \\\"it\\\", \\\"to\\\", \\\"start\\\", \\\"a\\\", \\\"charter\\\", \\\"operation\\\", \\\"out\\\", \\\"of\\\", \\\"Mascot\\\", \\\"Aerodrome\\\", \\\"in\\\", \\\"Sydney\\\", \\\".\\\"], \\\"h\\\": [\\\"mascot aerodrome\\\", \\\"Q17581\\\", [[17, 18]]], \\\"t\\\": [\\\"sydney\\\", \\\"Q3130\\\", [[20]]]}, {\\\"tokens\\\": [\\\"Together\\\", \\\"with\\\", \\\"Del\\\", \\\"Norte\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"the\\\", \\\"airport\\\", \\\"handles\\\", \\\"domestic\\\", \\\"and\\\", \\\"international\\\", \\\"operations\\\", \\\"for\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Monterrey\\\", \\\"and\\\", \\\"its\\\", \\\"metropolitan\\\", \\\"area\\\", \\\".\\\"], \\\"h\\\": [\\\"del norte international airport\\\", \\\"Q1657885\\\", [[2, 3, 4, 5]]], \\\"t\\\": [\\\"monterrey\\\", \\\"Q81033\\\", [[18]]]}, {\\\"tokens\\\": [\\\"Las\\\", \\\"Mercedes\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airstrip\\\", \\\"serving\\\", \\\"San\\\", \\\"Javier\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Maule\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"las mercedes airport\\\", \\\"Q16899715\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"san javier\\\", \\\"Q187831\\\", [[7, 8]]]}, {\\\"tokens\\\": [\\\"Silver\\\", \\\"City\\\", \\\"Airways\\\", \\\"dubbed\\\", \\\"this\\\", \\\"variant\\\", \\\"the\\\", \\\"\\\\\\\"\\\", \\\"Superfreighter\\\", \\\"\\\\\\\"\\\", \\\"and\\\", \\\"subsequently\\\", \\\"built\\\", \\\"an\\\", \\\"airport\\\", \\\"named\\\", \\\"\\\\\\\"\\\", \\\"Ferryfield\\\", \\\"\\\\\\\"\\\", \\\"at\\\", \\\"Lydd\\\", \\\"in\\\", \\\"Kent\\\", \\\",\\\", \\\"beginning\\\", \\\"air\\\", \\\"ferry\\\", \\\"services\\\", \\\"in\\\", \\\"1955\\\", \\\".\\\"], \\\"h\\\": [\\\"ferryfield\\\", \\\"Q1986577\\\", [[17]]], \\\"t\\\": [\\\"lydd\\\", \\\"Q1639689\\\", [[20]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airport\\\", \\\"'s\\\", \\\"former\\\", \\\"name\\\", \\\",\\\", \\\"Waterloo\\\", \\\"Regional\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"now\\\", \\\"used\\\", \\\"by\\\", \\\"Waterloo\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Waterloo\\\", \\\",\\\", \\\"Iowa\\\", \\\".\\\"], \\\"h\\\": [\\\"waterloo regional airport\\\", \\\"Q5927971\\\", [[6, 7, 8], [14, 15, 16]]], \\\"t\\\": [\\\"waterloo, iowa\\\", \\\"Q496381\\\", [[18, 19, 20]]]}, {\\\"tokens\\\": [\\\"Joensuu\\\", \\\"also\\\", \\\"has\\\", \\\"an\\\", \\\"airport\\\", \\\",\\\", \\\"with\\\", \\\"flights\\\", \\\"to\\\", \\\"Helsinki\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q370924\\\", [[4]]], \\\"t\\\": [\\\"joensuu\\\", \\\"Q186237\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Acheleia\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"village\\\", \\\"in\\\", \\\"the\\\", \\\"Paphos\\\", \\\"District\\\", \\\"of\\\", \\\"Cyprus\\\", \\\",\\\", \\\"located\\\", \\\"near\\\", \\\"to\\\", \\\"Paphos\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"paphos international airport\\\", \\\"Q1050707\\\", [[16, 17, 18]]], \\\"t\\\": [\\\"paphos district\\\", \\\"Q59133\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"Enniskillen\\\", \\\"/\\\", \\\"St\\\", \\\"Angelo\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"north\\\", \\\"of\\\", \\\"Enniskillen\\\", \\\",\\\", \\\"County\\\", \\\"Fermanagh\\\", \\\",\\\", \\\"Northern\\\", \\\"Ireland\\\", \\\".\\\"], \\\"h\\\": [\\\"st angelo airport\\\", \\\"Q3544931\\\", [[2, 3, 4]]], \\\"t\\\": [\\\"enniskillen\\\", \\\"Q990109\\\", [[0], [9]]]}, {\\\"tokens\\\": [\\\"Taravella\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"C\\\\u00f3rdoba\\\", \\\",\\\", \\\"to\\\", \\\"General\\\", \\\"Enrique\\\", \\\"Mosconi\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Comodoro\\\", \\\"Rivadavia\\\", \\\",\\\", \\\"with\\\", \\\"stopovers\\\", \\\"at\\\", \\\"Governor\\\", \\\"Francisco\\\", \\\"Gabrielli\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Mendoza\\\", \\\",\\\", \\\"and\\\", \\\"Presidente\\\", \\\"Per\\\\u00f3n\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Neuqu\\\\u00e9n\\\", \\\".\\\"], \\\"h\\\": [\\\"presidente per\\\\u00f3n international airport\\\", \\\"Q2600422\\\", [[28, 29, 30, 31]]], \\\"t\\\": [\\\"neuqu\\\\u00e9n\\\", \\\"Q44239\\\", [[33]]]}, {\\\"tokens\\\": [\\\"\\\\\\\"\\\", \\\"Wings\\\", \\\"\\\\\\\"\\\", \\\"was\\\", \\\"shot\\\", \\\"and\\\", \\\"completed\\\", \\\"on\\\", \\\"a\\\", \\\"budget\\\", \\\"of\\\", \\\"$\\\", \\\"2\\\", \\\"million\\\", \\\"at\\\", \\\"Kelly\\\", \\\"Field\\\", \\\",\\\", \\\"San\\\", \\\"Antonio\\\", \\\",\\\", \\\"Texas\\\", \\\"between\\\", \\\"September\\\", \\\"7\\\", \\\",\\\", \\\"1926\\\", \\\"and\\\", \\\"April\\\", \\\"7\\\", \\\",\\\", \\\"1927\\\", \\\".\\\"], \\\"h\\\": [\\\"kelly field\\\", \\\"Q10860401\\\", [[15, 16]]], \\\"t\\\": [\\\"san antonio, texas\\\", \\\"Q975\\\", [[18, 19, 20, 21]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"base\\\", \\\"was\\\", \\\"at\\\", \\\"Jos\\\\u00e9\\\", \\\"Mart\\\\u00ed\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Havana\\\", \\\".\\\", \\\"Flight\\\", \\\"International\\\", \\\"27\\\", \\\"March\\\", \\\"2007\\\"], \\\"h\\\": [\\\"jos\\\\u00e9 mart\\\\u00ed international airport\\\", \\\"Q381677\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"havana\\\", \\\"Q1563\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Melbourne\\\", \\\"Airport\\\", \\\",\\\", \\\"colloquially\\\", \\\"known\\\", \\\"as\\\", \\\"Tullamarine\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"the\\\", \\\"primary\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Melbourne\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"second\\\", \\\"busiest\\\", \\\"airport\\\", \\\"in\\\", \\\"Australia\\\", \\\".\\\"], \\\"h\\\": [\\\"tullamarine airport\\\", \\\"Q733738\\\", [[6, 7]]], \\\"t\\\": [\\\"melbourne\\\", \\\"Q3141\\\", [[0], [17]]]}, {\\\"tokens\\\": [\\\"Lukla\\\", \\\"contains\\\", \\\"a\\\", \\\"small\\\", \\\"airport\\\", \\\"servicing\\\", \\\"the\\\", \\\"region\\\", \\\",\\\", \\\"and\\\", \\\"a\\\", \\\"variety\\\", \\\"of\\\", \\\"shops\\\", \\\"and\\\", \\\"lodges\\\", \\\"catering\\\", \\\"to\\\", \\\"tourists\\\", \\\"and\\\", \\\"trekkers\\\", \\\",\\\", \\\"providing\\\", \\\"western\\\", \\\"-\\\", \\\"style\\\", \\\"meals\\\", \\\"and\\\", \\\"trail\\\", \\\"supplies\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q1043277\\\", [[4]]], \\\"t\\\": [\\\"lukla\\\", \\\"Q389190\\\", [[0]]]}, {\\\"tokens\\\": [\\\"During\\\", \\\"their\\\", \\\"flight\\\", \\\"they\\\", \\\"detoured\\\", \\\"towards\\\", \\\"Italy\\\", \\\"and\\\", \\\"landed\\\", \\\"at\\\", \\\"the\\\", \\\"Galatina\\\", \\\"Air\\\", \\\"Base\\\", \\\"in\\\", \\\"Lecce\\\", \\\".\\\"], \\\"h\\\": [\\\"galatina air base\\\", \\\"Q1934995\\\", [[11, 12, 13]]], \\\"t\\\": [\\\"lecce\\\", \\\"Q13386\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Daily\\\", \\\"Air\\\", \\\"is\\\", \\\"the\\\", \\\"only\\\", \\\"airline\\\", \\\"to\\\", \\\"offer\\\", \\\"flights\\\", \\\"from\\\", \\\"Taiwan\\\", \\\"Island\\\", \\\"through\\\", \\\"Taitung\\\", \\\"Airport\\\", \\\"in\\\", \\\"Taitung\\\", \\\"City\\\", \\\"to\\\", \\\"Orchid\\\", \\\"Island\\\", \\\"through\\\", \\\"its\\\", \\\"Lanyu\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"taitung airport\\\", \\\"Q708576\\\", [[13, 14]]], \\\"t\\\": [\\\"taitung city\\\", \\\"Q713381\\\", [[16, 17]]]}, {\\\"tokens\\\": [\\\"KWYS\\\", \\\"(\\\", \\\"920\\\", \\\"AM\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"radio\\\", \\\"station\\\", \\\"licensed\\\", \\\"to\\\", \\\"serve\\\", \\\"West\\\", \\\"Yellowstone\\\", \\\",\\\", \\\"Montana\\\", \\\".\\\"], \\\"h\\\": [\\\"kwys\\\", \\\"Q8051984\\\", [[0]]], \\\"t\\\": [\\\"west yellowstone, montana\\\", \\\"Q956110\\\", [[12, 13, 14, 15]]]}, {\\\"tokens\\\": [\\\"Three\\\", \\\"letters\\\", \\\"denote\\\", \\\"the\\\", \\\"administrative\\\", \\\"divisions\\\", \\\"(\\\", \\\"BJL\\\", \\\"would\\\", \\\"denote\\\", \\\"Banjul\\\", \\\")\\\", \\\",\\\", \\\"followed\\\", \\\"by\\\", \\\"four\\\", \\\"numbers\\\", \\\"and\\\", \\\"another\\\", \\\"letter\\\", \\\".\\\"], \\\"h\\\": [\\\"bjl\\\", \\\"Q753531\\\", [[7]]], \\\"t\\\": [\\\"banjul\\\", \\\"Q3726\\\", [[10]]]}, {\\\"tokens\\\": [\\\"At\\\", \\\"the\\\", \\\"end\\\", \\\"of\\\", \\\"October\\\", \\\"the\\\", \\\"Squadron\\\", \\\"moved\\\", \\\"to\\\", \\\"Gibraltar\\\", \\\"and\\\", \\\"on\\\", \\\"8\\\", \\\"November\\\", \\\",\\\", \\\"19\\\", \\\"Spitfires\\\", \\\"moved\\\", \\\"to\\\", \\\"the\\\", \\\"newly\\\", \\\"captured\\\", \\\"airfield\\\", \\\"at\\\", \\\"Maison\\\", \\\"Blanche\\\", \\\",\\\", \\\"Algiers\\\", \\\".\\\"], \\\"h\\\": [\\\"maison blanche\\\", \\\"Q623452\\\", [[24, 25]]], \\\"t\\\": [\\\"algiers\\\", \\\"Q3561\\\", [[27]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"Albany\\\", \\\",\\\", \\\"they\\\", \\\"pass\\\", \\\"the\\\", \\\"Southwest\\\", \\\"Georgia\\\", \\\"Regional\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"southwest georgia regional airport\\\", \\\"Q2875753\\\", [[6, 7, 8, 9]]], \\\"t\\\": [\\\"albany\\\", \\\"Q285599\\\", [[1]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"July\\\", \\\"the\\\", \\\"same\\\", \\\"year\\\", \\\",\\\", \\\"Moscow\\\", \\\"was\\\", \\\"first\\\", \\\"served\\\", \\\"by\\\", \\\"the\\\", \\\"carrier\\\", \\\"with\\\", \\\"flights\\\", \\\"to\\\", \\\"Domodedovo\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"domodedovo airport\\\", \\\"Q186614\\\", [[16, 17]]], \\\"t\\\": [\\\"moscow\\\", \\\"Q649\\\", [[6]]]}, {\\\"tokens\\\": [\\\"About\\\", \\\"300\\\", \\\"delays\\\", \\\"were\\\", \\\"reported\\\", \\\"at\\\", \\\"Toronto\\\", \\\"'s\\\", \\\"Pearson\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"pearson international airport\\\", \\\"Q242066\\\", [[8, 9, 10]]], \\\"t\\\": [\\\"toronto\\\", \\\"Q172\\\", [[6]]]}, {\\\"tokens\\\": [\\\"Chan\\\", \\\"Chan\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airstrip\\\", \\\"serving\\\", \\\"Choshuenco\\\", \\\",\\\", \\\"a\\\", \\\"small\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Los\\\", \\\"Lagos\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"chan chan airport\\\", \\\"Q16858927\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"choshuenco\\\", \\\"Q5105354\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Hickory\\\", \\\"Aviation\\\", \\\"Museum\\\", \\\"is\\\", \\\"an\\\", \\\"aerospace\\\", \\\"museum\\\", \\\"at\\\", \\\"the\\\", \\\"Hickory\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Hickory\\\", \\\",\\\", \\\"North\\\", \\\"Carolina\\\", \\\".\\\"], \\\"h\\\": [\\\"hickory regional airport\\\", \\\"Q3275605\\\", [[9, 10, 11]]], \\\"t\\\": [\\\"hickory, north carolina\\\", \\\"Q2028564\\\", [[13, 14, 15, 16]]]}, {\\\"tokens\\\": [\\\"Also\\\", \\\"known\\\", \\\"as\\\", \\\"Bud\\\", \\\"Frye\\\", \\\"Field\\\", \\\",\\\", \\\"\\\\n \\\", \\\"it\\\", \\\"is\\\", \\\"located\\\", \\\"two\\\", \\\"\\\\u00a0\\\", \\\"nautical\\\", \\\"miles\\\", \\\"(\\\", \\\"4\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"southeast\\\", \\\"of\\\", \\\"the\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\"of\\\", \\\"Madison\\\", \\\".\\\"], \\\"h\\\": [\\\"bud frye field\\\", \\\"Q14692752\\\", [[3, 4, 5]]], \\\"t\\\": [\\\"madison\\\", \\\"Q1913353\\\", [[27]]]}, {\\\"tokens\\\": [\\\"Flight\\\", \\\"3400\\\", \\\"was\\\", \\\"bound\\\", \\\"for\\\", \\\"Moline\\\", \\\",\\\", \\\"Il\\\", \\\".\\\", \\\",\\\", \\\"when\\\", \\\"it\\\", \\\"was\\\", \\\"diverted\\\", \\\"about\\\", \\\"9\\\", \\\"p.m.\\\", \\\"to\\\", \\\"Majors\\\", \\\"Airport\\\", \\\"in\\\", \\\"Greenville\\\", \\\".\\\"], \\\"h\\\": [\\\"majors airport\\\", \\\"Q10853404\\\", [[18, 19]]], \\\"t\\\": [\\\"greenville\\\", \\\"Q976490\\\", [[21]]]}, {\\\"tokens\\\": [\\\"Jackpot\\\", \\\"Airport\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"Hayden\\\", \\\"Field\\\", \\\",\\\", \\\"is\\\", \\\"a\\\", \\\"county\\\", \\\"owned\\\", \\\",\\\", \\\"public\\\", \\\"use\\\", \\\"airport\\\", \\\"located\\\", \\\"east\\\", \\\"of\\\", \\\"Jackpot\\\", \\\",\\\", \\\"in\\\", \\\"Elko\\\", \\\"County\\\", \\\",\\\", \\\"Nevada\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"hayden field\\\", \\\"Q2901128\\\", [[6, 7]]], \\\"t\\\": [\\\"jackpot\\\", \\\"Q2917481\\\", [[0], [20]]]}, {\\\"tokens\\\": [\\\"Precipitation\\\", \\\"peaked\\\", \\\"at\\\", \\\"at\\\", \\\"the\\\", \\\"Billy\\\", \\\"Mitchell\\\", \\\"Airport\\\", \\\"in\\\", \\\"Hatteras\\\", \\\".\\\"], \\\"h\\\": [\\\"billy mitchell airport\\\", \\\"Q597366\\\", [[5, 6, 7]]], \\\"t\\\": [\\\"hatteras\\\", \\\"Q3106552\\\", [[9]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"primary\\\", \\\"civilian\\\", \\\"airport\\\", \\\"of\\\", \\\"Northern\\\", \\\"Cyprus\\\", \\\",\\\", \\\"Ercan\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"directly\\\", \\\"north\\\", \\\"of\\\", \\\"the\\\", \\\"village\\\", \\\".\\\"], \\\"h\\\": [\\\"ercan international airport\\\", \\\"Q607230\\\", [[8, 9, 10]]], \\\"t\\\": [\\\"northern cyprus\\\", \\\"Q23681\\\", [[5, 6]]]}, {\\\"tokens\\\": [\\\"Clarksburg\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"the\\\", \\\"North\\\", \\\"Central\\\", \\\"West\\\", \\\"Virginia\\\", \\\"Airport\\\", \\\",\\\", \\\"approximately\\\", \\\"7\\\", \\\"miles\\\", \\\"east\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"north central west virginia airport\\\", \\\"Q7054774\\\", [[5, 6, 7, 8, 9]]], \\\"t\\\": [\\\"clarksburg\\\", \\\"Q1010199\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Vahitahi\\\", \\\"has\\\", \\\"a\\\", \\\"territorial\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"territorial airport\\\", \\\"Q16897548\\\", [[3, 4]]], \\\"t\\\": [\\\"vahitahi\\\", \\\"Q1811472\\\", [[0]]]}, {\\\"tokens\\\": [\\\"General\\\", \\\"DeWitt\\\", \\\"Spain\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"civil\\\", \\\"aviation\\\", \\\"airport\\\", \\\"just\\\", \\\"north\\\", \\\"of\\\", \\\"downtown\\\", \\\"Memphis\\\", \\\".\\\"], \\\"h\\\": [\\\"general dewitt spain airport\\\", \\\"Q3274365\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"memphis\\\", \\\"Q16563\\\", [[13]]]}, {\\\"tokens\\\": [\\\"Cassidy\\\", \\\",\\\", \\\"British\\\", \\\"Columbia\\\", \\\"is\\\", \\\"located\\\", \\\"south\\\", \\\"of\\\", \\\"Nanaimo\\\", \\\"on\\\", \\\"Vancouver\\\", \\\"Island\\\", \\\"and\\\", \\\"is\\\", \\\"home\\\", \\\"to\\\", \\\"the\\\", \\\"Ray\\\", \\\"Collishaw\\\", \\\"Air\\\", \\\"Terminal\\\", \\\",\\\", \\\"Nanaimo\\\", \\\"'s\\\", \\\"only\\\", \\\"airfield\\\", \\\".\\\"], \\\"h\\\": [\\\"ray collishaw air terminal\\\", \\\"Q64833\\\", [[17, 18, 19, 20]]], \\\"t\\\": [\\\"nanaimo\\\", \\\"Q16461\\\", [[8], [22]]]}, {\\\"tokens\\\": [\\\"Laredo\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"within\\\", \\\"the\\\", \\\"Laredo\\\", \\\"city\\\", \\\"limits\\\", \\\",\\\", \\\"while\\\", \\\"the\\\", \\\"Quetzalcoatl\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"nearby\\\", \\\"in\\\", \\\"Nuevo\\\", \\\"Laredo\\\", \\\"on\\\", \\\"the\\\", \\\"Mexican\\\", \\\"side\\\", \\\".\\\"], \\\"h\\\": [\\\"quetzalcoatl international airport\\\", \\\"Q2231559\\\", [[12, 13, 14]]], \\\"t\\\": [\\\"nuevo laredo\\\", \\\"Q328846\\\", [[18, 19]]]}, {\\\"tokens\\\": [\\\"Matthew\\\", \\\"Spain\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"use\\\", \\\"airport\\\", \\\"located\\\", \\\"near\\\", \\\"San\\\", \\\"Ignacio\\\", \\\",\\\", \\\"Cayo\\\", \\\"District\\\", \\\",\\\", \\\"Belize\\\", \\\".\\\"], \\\"h\\\": [\\\"matthew spain airport\\\", \\\"Q16894725\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"san ignacio\\\", \\\"Q724815\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"Robillard\\\", \\\"was\\\", \\\"then\\\", \\\"stationed\\\", \\\"at\\\", \\\"Curtiss\\\", \\\"Field\\\", \\\"at\\\", \\\"Mineola\\\", \\\",\\\", \\\"New\\\", \\\"York\\\", \\\"and\\\", \\\"met\\\", \\\"his\\\", \\\"future\\\", \\\"wife\\\", \\\",\\\", \\\"Alice\\\", \\\"Whilden\\\", \\\"Carrington\\\", \\\"there\\\", \\\".\\\"], \\\"h\\\": [\\\"curtiss field\\\", \\\"Q7366439\\\", [[5, 6]]], \\\"t\\\": [\\\"mineola, new york\\\", \\\"Q2349502\\\", [[8, 9, 10, 11]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"campus\\\", \\\"is\\\", \\\"situated\\\", \\\"on\\\", \\\"the\\\", \\\"Rajiv\\\", \\\"Rahadari\\\", \\\",\\\", \\\"Hyderabad\\\", \\\"-\\\", \\\"Karimnagar\\\", \\\"-\\\", \\\"Ramagundam\\\", \\\"Highway\\\", \\\")\\\", \\\"near\\\", \\\"the\\\", \\\"Hakimpet\\\", \\\"Air\\\", \\\"Force\\\", \\\"Station\\\", \\\".\\\"], \\\"h\\\": [\\\"hakimpet air force station\\\", \\\"Q3913389\\\", [[18, 19, 20, 21]]], \\\"t\\\": [\\\"hyderabad\\\", \\\"Q1361\\\", [[9]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"airport\\\", \\\"to\\\", \\\"Taxila\\\", \\\"is\\\", \\\"Islamabad\\\", \\\"'s\\\", \\\"Benazir\\\", \\\"Bhutto\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"located\\\", \\\"36.5\\\", \\\"kilometres\\\", \\\"away\\\", \\\".\\\"], \\\"h\\\": [\\\"benazir bhutto international airport\\\", \\\"Q816717\\\", [[8, 9, 10, 11]]], \\\"t\\\": [\\\"islamabad\\\", \\\"Q1362\\\", [[6]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"city\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Canal\\\", \\\"Bajo\\\", \\\"Carlos\\\", \\\"Hott\\\", \\\"Siebert\\\", \\\"Airport\\\", \\\",\\\", \\\"located\\\", \\\"near\\\", \\\"Osorno\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"El\\\", \\\"Tepual\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"located\\\", \\\"near\\\", \\\"Puerto\\\", \\\"Montt\\\", \\\".\\\"], \\\"h\\\": [\\\"el tepual international airport\\\", \\\"Q2756149\\\", [[18, 19, 20, 21]]], \\\"t\\\": [\\\"puerto montt\\\", \\\"Q36214\\\", [[25, 26]]]}, {\\\"tokens\\\": [\\\"Waynesville\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"at\\\", \\\"Forney\\\", \\\"Field\\\", \\\"serves\\\", \\\"the\\\", \\\"community\\\", \\\"with\\\", \\\"air\\\", \\\"service\\\", \\\".\\\"], \\\"h\\\": [\\\"forney field\\\", \\\"Q7976824\\\", [[4, 5]]], \\\"t\\\": [\\\"waynesville\\\", \\\"Q589670\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Ciudad\\\", \\\"Real\\\", \\\"Central\\\", \\\"Airport\\\", \\\",\\\", \\\"previously\\\", \\\"known\\\", \\\"as\\\", \\\"\\\\\\\"\\\", \\\"Don\\\", \\\"Quijote\\\", \\\"Airport\\\", \\\"\\\\\\\"\\\", \\\"and\\\", \\\"\\\\\\\"\\\", \\\"South\\\", \\\"Madrid\\\", \\\"Airport\\\", \\\"\\\\\\\"\\\", \\\",\\\", \\\"was\\\", \\\"an\\\", \\\"international\\\", \\\"airport\\\", \\\"south\\\", \\\"of\\\", \\\"Ciudad\\\", \\\"Real\\\", \\\"in\\\", \\\"Spain\\\", \\\".\\\"], \\\"h\\\": [\\\"don quijote airport\\\", \\\"Q1431113\\\", [[9, 10, 11]]], \\\"t\\\": [\\\"ciudad real\\\", \\\"Q15093\\\", [[0, 1], [26, 27]]]}, {\\\"tokens\\\": [\\\"Mariano\\\", \\\"Melgar\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"agricultural\\\", \\\"district\\\", \\\"of\\\", \\\"La\\\", \\\"Joya\\\", \\\"in\\\", \\\"the\\\", \\\"Arequipa\\\", \\\"Region\\\", \\\"of\\\", \\\"Peru\\\", \\\".\\\"], \\\"h\\\": [\\\"mariano melgar airport\\\", \\\"Q18472109\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"la joya\\\", \\\"Q2778747\\\", [[11, 12]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"July\\\", \\\"7\\\", \\\",\\\", \\\"2010\\\", \\\"a\\\", \\\"flight\\\", \\\"crew\\\", \\\"preparing\\\", \\\"to\\\", \\\"land\\\", \\\"in\\\", \\\"Hangzhou\\\", \\\"'s\\\", \\\"Xiaoshan\\\", \\\"Airport\\\", \\\"in\\\", \\\"China\\\", \\\"reported\\\", \\\"an\\\", \\\"UFO\\\", \\\".\\\"], \\\"h\\\": [\\\"xiaoshan airport\\\", \\\"Q1197691\\\", [[14, 15]]], \\\"t\\\": [\\\"hangzhou\\\", \\\"Q4970\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Opened\\\", \\\"in\\\", \\\"1942\\\", \\\",\\\", \\\"the\\\", \\\"base\\\", \\\"closed\\\", \\\"pursuant\\\", \\\"to\\\", \\\"BRAC\\\", \\\"action\\\", \\\"in\\\", \\\"1995\\\", \\\"and\\\", \\\"its\\\", \\\"airfield\\\", \\\"is\\\", \\\"now\\\", \\\"Griffiss\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"owned\\\", \\\"by\\\", \\\"Oneida\\\", \\\"County\\\", \\\".\\\"], \\\"h\\\": [\\\"griffiss international airport\\\", \\\"Q5608857\\\", [[18, 19, 20]]], \\\"t\\\": [\\\"oneida county\\\", \\\"Q115043\\\", [[24, 25]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"19\\\", \\\"August\\\", \\\"1998\\\", \\\",\\\", \\\"a\\\", \\\"Motor\\\", \\\"Sich\\\", \\\"An-12BP\\\", \\\",\\\", \\\"registration\\\", \\\"UR-11528\\\", \\\"was\\\", \\\"damaged\\\", \\\"beyond\\\", \\\"economic\\\", \\\"repair\\\", \\\"in\\\", \\\"a\\\", \\\"taxiing\\\", \\\"accident\\\", \\\"at\\\", \\\"Hang\\\", \\\"Nadim\\\", \\\"Airport\\\", \\\"in\\\", \\\"Batam\\\", \\\",\\\", \\\"Indonesia\\\", \\\".\\\"], \\\"h\\\": [\\\"hang nadim airport\\\", \\\"Q780450\\\", [[22, 23, 24]]], \\\"t\\\": [\\\"batam\\\", \\\"Q10103\\\", [[26]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"entrance\\\", \\\"line\\\", \\\"to\\\", \\\"the\\\", \\\"Outer\\\", \\\"Harbour\\\", \\\"extends\\\", \\\"from\\\", \\\"the\\\", \\\"breakwater\\\", \\\"just\\\", \\\"south\\\", \\\"of\\\", \\\"Pier\\\", \\\"A\\\", \\\"at\\\", \\\"Ogden\\\", \\\"Point\\\", \\\"in\\\", \\\"Victoria\\\", \\\"to\\\", \\\"Macaulay\\\", \\\"Point\\\", \\\"in\\\", \\\"Esquimalt\\\", \\\".\\\"], \\\"h\\\": [\\\"ogden point\\\", \\\"Q2901611\\\", [[17, 18]]], \\\"t\\\": [\\\"victoria\\\", \\\"Q2132\\\", [[20]]]}, {\\\"tokens\\\": [\\\"Brest\\\", \\\"Bretagne\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\",\\\", \\\"formerly\\\", \\\"known\\\", \\\"as\\\", \\\"Brest\\\", \\\"Guipavas\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"international\\\", \\\"airport\\\", \\\"serving\\\", \\\"Brest\\\", \\\",\\\", \\\"France\\\", \\\".\\\"], \\\"h\\\": [\\\"brest bretagne airport\\\", \\\"Q1191525\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"brest, france\\\", \\\"Q12193\\\", [[18, 19, 20]]]}, {\\\"tokens\\\": [\\\"Florida\\\", \\\"Wing\\\", \\\"headquarters\\\", \\\"is\\\", \\\"located\\\", \\\"at\\\", \\\"Lakeland\\\", \\\"Linder\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Lakeland\\\", \\\",\\\", \\\"Florida\\\", \\\".\\\"], \\\"h\\\": [\\\"lakeland linder regional airport\\\", \\\"Q10853394\\\", [[6, 7, 8, 9]]], \\\"t\\\": [\\\"lakeland, florida\\\", \\\"Q639452\\\", [[11, 12, 13]]]}, {\\\"tokens\\\": [\\\"Flights\\\", \\\"arrive\\\", \\\"in\\\", \\\"any\\\", \\\"of\\\", \\\"Washington\\\", \\\"'s\\\", \\\"three\\\", \\\"area\\\", \\\"airports\\\", \\\":\\\", \\\"Ronald\\\", \\\"Reagan\\\", \\\"Washington\\\", \\\"National\\\", \\\"Airport\\\", \\\",\\\", \\\"Baltimore\\\", \\\"/\\\", \\\"Washington\\\", \\\"International\\\", \\\"Thurgood\\\", \\\"Marshall\\\", \\\"Airport\\\", \\\",\\\", \\\"and\\\", \\\"Washington\\\", \\\"Dulles\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"ronald reagan washington national airport\\\", \\\"Q676576\\\", [[11, 12, 13, 14, 15]]], \\\"t\\\": [\\\"baltimore\\\", \\\"Q5092\\\", [[17]]]}, {\\\"tokens\\\": [\\\"Following\\\", \\\"the\\\", \\\"merger\\\", \\\"of\\\", \\\"the\\\", \\\"Cessna\\\", \\\"and\\\", \\\"Beechcraft\\\", \\\"employee\\\", \\\"flying\\\", \\\"clubs\\\", \\\",\\\", \\\"Cessna\\\", \\\"'s\\\", \\\"flying\\\", \\\"club\\\", \\\"has\\\", \\\"since\\\", \\\"moved\\\", \\\"from\\\", \\\"their\\\", \\\"previous\\\", \\\"base\\\", \\\"at\\\", \\\"Wichita\\\", \\\"Mid\\\", \\\"-\\\", \\\"Continental\\\", \\\"Airport\\\", \\\"to\\\", \\\"Beech\\\", \\\"Factory\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"beech factory airport\\\", \\\"Q1654828\\\", [[30, 31, 32]]], \\\"t\\\": [\\\"wichita\\\", \\\"Q49266\\\", [[24]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"closest\\\", \\\"major\\\", \\\"airport\\\", \\\"serving\\\", \\\"Coeur\\\", \\\"d'Alene\\\", \\\"and\\\", \\\"North\\\", \\\"Idaho\\\", \\\"is\\\", \\\"the\\\", \\\"Spokane\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"five\\\", \\\"airlines\\\", \\\"and\\\", \\\"is\\\", \\\"to\\\", \\\"the\\\", \\\"west\\\", \\\"in\\\", \\\"Spokane\\\", \\\",\\\", \\\"Washington\\\", \\\".\\\"], \\\"h\\\": [\\\"spokane international airport\\\", \\\"Q917528\\\", [[12, 13, 14]]], \\\"t\\\": [\\\"spokane, washington\\\", \\\"Q187805\\\", [[28, 29, 30]]]}, {\\\"tokens\\\": [\\\"Krim\\\", \\\"Belkacem\\\", \\\"Airport\\\", \\\"in\\\", \\\"Hassi\\\", \\\"Messaoud\\\", \\\"was\\\", \\\"named\\\", \\\"after\\\", \\\"him\\\", \\\".\\\"], \\\"h\\\": [\\\"krim belkacem airport\\\", \\\"Q25060\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"hassi messaoud\\\", \\\"Q1000139\\\", [[4, 5]]]}, {\\\"tokens\\\": [\\\"61\\\", \\\"Col\\\", \\\".\\\", \\\"Prados\\\", \\\"de\\\", \\\"la\\\", \\\"Capilla\\\", \\\"CP\\\", \\\"76176\\\", \\\"Quer\\\\u00e9taro\\\", \\\",\\\", \\\"Qro\\\", \\\".\\\", \\\"\\\\\\\"\\\"], \\\"h\\\": [\\\"qro\\\", \\\"Q1932794\\\", [[11]]], \\\"t\\\": [\\\"quer\\\\u00e9taro\\\", \\\"Q79754\\\", [[9]]]}, {\\\"tokens\\\": [\\\"Friedrichshafen\\\", \\\"has\\\", \\\"a\\\", \\\"local\\\", \\\"airport\\\", \\\"which\\\", \\\"offers\\\", \\\",\\\", \\\"among\\\", \\\"other\\\", \\\"services\\\", \\\",\\\", \\\"daily\\\", \\\"international\\\", \\\"connections\\\", \\\"provided\\\", \\\"mainly\\\", \\\"by\\\", \\\"Lufthansa\\\", \\\"CityLine\\\", \\\",\\\", \\\"Turkish\\\", \\\"Airlines\\\", \\\"and\\\", \\\"Germanwings\\\", \\\".\\\"], \\\"h\\\": [\\\"local airport\\\", \\\"Q682232\\\", [[3, 4]]], \\\"t\\\": [\\\"friedrichshafen\\\", \\\"Q4051\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Inter\\\", \\\"-\\\", \\\"city\\\", \\\"bus\\\", \\\"service\\\", \\\"to\\\", \\\"Fairmont\\\", \\\",\\\", \\\"Clarksburg\\\", \\\",\\\", \\\"Waynesburg\\\", \\\",\\\", \\\"PA\\\", \\\",\\\", \\\"Pittsburgh\\\", \\\",\\\", \\\"PA\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"Pittsburgh\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"achieved\\\", \\\"with\\\", \\\"the\\\", \\\"Gray\\\", \\\"Line\\\", \\\".\\\"], \\\"h\\\": [\\\"pittsburgh international airport\\\", \\\"Q1421504\\\", [[20, 21, 22]]], \\\"t\\\": [\\\"pittsburgh, pa\\\", \\\"Q1342\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"1st\\\", \\\"Combat\\\", \\\"Training\\\", \\\"Air\\\", \\\"Regiment\\\", \\\"relocated\\\", \\\"to\\\", \\\"Shtraklevo\\\", \\\"Air\\\", \\\"Base\\\", \\\"close\\\", \\\"to\\\", \\\"Ruse\\\", \\\"with\\\", \\\"two\\\", \\\"MiG-17\\\", \\\"squadrons\\\", \\\"and\\\", \\\"a\\\", \\\"third\\\", \\\"squadron\\\", \\\"relocated\\\", \\\"to\\\", \\\"Dolna\\\", \\\"Mitropoliya\\\", \\\".\\\"], \\\"h\\\": [\\\"shtraklevo air base\\\", \\\"Q2875909\\\", [[7, 8, 9]]], \\\"t\\\": [\\\"ruse\\\", \\\"Q160173\\\", [[12]]]}, {\\\"tokens\\\": [\\\"His\\\", \\\"unit\\\", \\\"was\\\", \\\"later\\\", \\\"transferred\\\", \\\"to\\\", \\\"Gabu\\\", \\\"Airfield\\\", \\\"in\\\", \\\"Laoag\\\", \\\",\\\", \\\"Philippines\\\", \\\"from\\\", \\\"where\\\", \\\"he\\\", \\\"attacked\\\", \\\"Japanese\\\", \\\"positions\\\", \\\"in\\\", \\\"northern\\\", \\\"Luzon\\\", \\\"and\\\", \\\"Okinawa\\\", \\\"until\\\", \\\"the\\\", \\\"end\\\", \\\"of\\\", \\\"the\\\", \\\"war\\\", \\\".\\\"], \\\"h\\\": [\\\"gabu airfield\\\", \\\"Q598033\\\", [[6, 7]]], \\\"t\\\": [\\\"laoag\\\", \\\"Q39738\\\", [[9]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"EAA\\\", \\\"AirVenture\\\", \\\"Museum\\\", \\\"in\\\", \\\"Oshkosh\\\", \\\",\\\", \\\"Wisconsin\\\", \\\"has\\\", \\\"an\\\", \\\"example\\\", \\\"on\\\", \\\"display\\\", \\\"at\\\", \\\"its\\\", \\\"Pioneer\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"pioneer airport\\\", \\\"Q24901808\\\", [[15, 16]]], \\\"t\\\": [\\\"oshkosh, wisconsin\\\", \\\"Q936741\\\", [[5, 6, 7]]]}, {\\\"tokens\\\": [\\\"Everglades\\\", \\\"Airpark\\\", \\\"in\\\", \\\"Everglades\\\", \\\"City\\\", \\\"was\\\", \\\"closed\\\", \\\"after\\\", \\\"high\\\", \\\"water\\\", \\\"reached\\\", \\\"the\\\", \\\"runway\\\", \\\".\\\"], \\\"h\\\": [\\\"everglades airpark\\\", \\\"Q5417132\\\", [[0, 1]]], \\\"t\\\": [\\\"everglades city\\\", \\\"Q994815\\\", [[3, 4]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airport\\\", \\\"of\\\", \\\"Donetsk\\\", \\\"was\\\", \\\"hit\\\", \\\"by\\\", \\\"\\\\\\\"\\\", \\\"Grad\\\", \\\"\\\\\\\"\\\", \\\"rockets\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q1431229\\\", [[1]]], \\\"t\\\": [\\\"donetsk\\\", \\\"Q43070\\\", [[3]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Le\\\", \\\"Sueur\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"on\\\", \\\"the\\\", \\\"south\\\", \\\"side\\\", \\\"of\\\", \\\"Le\\\", \\\"Sueur\\\", \\\",\\\", \\\"Minnesota\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"le sueur municipal airport\\\", \\\"Q6507708\\\", [[1, 2, 3, 4]]], \\\"t\\\": [\\\"le sueur, minnesota\\\", \\\"Q1924183\\\", [[13, 14, 15, 16]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"still\\\", \\\"airworthy\\\", \\\"and\\\", \\\"is\\\", \\\"on\\\", \\\"public\\\", \\\"display\\\", \\\"at\\\", \\\"the\\\", \\\"Shuttleworth\\\", \\\"Collection\\\", \\\"at\\\", \\\"Old\\\", \\\"Warden\\\", \\\"Aerodrome\\\", \\\"in\\\", \\\"Bedfordshire\\\", \\\".\\\"], \\\"h\\\": [\\\"old warden aerodrome\\\", \\\"Q17016016\\\", [[14, 15, 16]]], \\\"t\\\": [\\\"shuttleworth collection\\\", \\\"Q2280439\\\", [[11, 12]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"closest\\\", \\\"public\\\", \\\"airport\\\", \\\"is\\\", \\\"Laurel\\\", \\\"Airport\\\", \\\"in\\\", \\\"Laurel\\\", \\\",\\\", \\\"Delaware\\\", \\\".\\\"], \\\"h\\\": [\\\"laurel airport\\\", \\\"Q6499745\\\", [[5, 6]]], \\\"t\\\": [\\\"laurel, delaware\\\", \\\"Q755128\\\", [[8, 9, 10]]]}, {\\\"tokens\\\": [\\\"Coronel\\\", \\\"Felipe\\\", \\\"Varela\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"Catamarca\\\", \\\"Province\\\", \\\",\\\", \\\"Argentina\\\", \\\"serving\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"San\\\", \\\"Fernando\\\", \\\"del\\\", \\\"Valle\\\", \\\"de\\\", \\\"Catamarca\\\", \\\".\\\"], \\\"h\\\": [\\\"coronel felipe varela international airport\\\", \\\"Q1657365\\\", [[0, 1, 2, 3, 4]]], \\\"t\\\": [\\\"san fernando del valle de catamarca\\\", \\\"Q44162\\\", [[19, 20, 21, 22, 23, 24]]]}, {\\\"tokens\\\": [\\\"Autov\\\\u00eda\\\", \\\"T-11\\\", \\\"is\\\", \\\"a\\\", \\\"17,3\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\"long\\\", \\\"primary\\\", \\\"highway\\\", \\\"in\\\", \\\"Catalonia\\\", \\\"connecting\\\", \\\"Reus\\\", \\\"(\\\", \\\"and\\\", \\\"its\\\", \\\"airport\\\", \\\")\\\", \\\"and\\\", \\\"Tarragona\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q1332979\\\", [[17]]], \\\"t\\\": [\\\"reus\\\", \\\"Q487096\\\", [[13]]]}, {\\\"tokens\\\": [\\\"Tuskegee\\\", \\\"Airmen\\\", \\\"National\\\", \\\"Historic\\\", \\\"Site\\\", \\\",\\\", \\\"at\\\", \\\"Moton\\\", \\\"Field\\\", \\\"in\\\", \\\"Tuskegee\\\", \\\",\\\", \\\"Alabama\\\", \\\",\\\", \\\"commemorates\\\", \\\"the\\\", \\\"contributions\\\", \\\"of\\\", \\\"African\\\", \\\"American\\\", \\\"airmen\\\", \\\"in\\\", \\\"World\\\", \\\"War\\\", \\\"II\\\", \\\".\\\"], \\\"h\\\": [\\\"moton field\\\", \\\"Q3887824\\\", [[7, 8]]], \\\"t\\\": [\\\"tuskegee, alabama\\\", \\\"Q79718\\\", [[10, 11, 12]]]}, {\\\"tokens\\\": [\\\"This\\\", \\\"short\\\", \\\"autoroute\\\", \\\",\\\", \\\"only\\\", \\\"in\\\", \\\"length\\\", \\\",\\\", \\\"connects\\\", \\\"Aim\\\\u00e9\\\", \\\"C\\\\u00e9saire\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Le\\\", \\\"Lamentin\\\", \\\"to\\\", \\\"Fort\\\", \\\"-\\\", \\\"de\\\", \\\"-\\\", \\\"France\\\", \\\".\\\"], \\\"h\\\": [\\\"aim\\\\u00e9 c\\\\u00e9saire international airport\\\", \\\"Q651330\\\", [[9, 10, 11, 12]]], \\\"t\\\": [\\\"fort-de-france\\\", \\\"Q81621\\\", [[17, 18, 19, 20, 21]]]}, {\\\"tokens\\\": [\\\"During\\\", \\\"the\\\", \\\"1970s\\\", \\\",\\\", \\\"the\\\", \\\"station\\\", \\\"operated\\\", \\\"a\\\", \\\"satellite\\\", \\\"station\\\", \\\",\\\", \\\"KEKO\\\", \\\"-\\\", \\\"TV\\\", \\\"(\\\", \\\"channel\\\", \\\"10\\\", \\\")\\\", \\\"in\\\", \\\"Elko\\\", \\\".\\\"], \\\"h\\\": [\\\"keko\\\", \\\"Q5364362\\\", [[11]]], \\\"t\\\": [\\\"elko\\\", \\\"Q945084\\\", [[19]]]}, {\\\"tokens\\\": [\\\"Queen\\\", \\\"Tamar\\\", \\\"Airport\\\", \\\",\\\", \\\"or\\\", \\\"Mestia\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"a\\\", \\\"small\\\", \\\"airport\\\", \\\"serving\\\", \\\"Mestia\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"Samegrelo\\\", \\\"-\\\", \\\"Zemo\\\", \\\"Svaneti\\\", \\\",\\\", \\\"Georgia\\\", \\\".\\\"], \\\"h\\\": [\\\"queen tamar airport\\\", \\\"Q2875860\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"mestia\\\", \\\"Q1011051\\\", [[5], [13]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"network\\\", \\\"provides\\\", \\\"a\\\", \\\"connection\\\", \\\"for\\\", \\\"the\\\", \\\"port\\\", \\\"and\\\", \\\"airport\\\", \\\"precincts\\\", \\\"and\\\", \\\"commuters\\\", \\\"to\\\", \\\"the\\\", \\\"north\\\", \\\",\\\", \\\"south\\\", \\\",\\\", \\\"east\\\", \\\"and\\\", \\\"west\\\", \\\"of\\\", \\\"Brisbane\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q45523\\\", [[9]]], \\\"t\\\": [\\\"brisbane\\\", \\\"Q34932\\\", [[23]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"small\\\", \\\"airport\\\", \\\"serving\\\", \\\"Sogamoso\\\", \\\",\\\", \\\"Alberto\\\", \\\"Lleras\\\", \\\"Camargo\\\", \\\"Airport\\\", \\\"(\\\", \\\"IATA\\\", \\\"-\\\", \\\"code\\\", \\\":\\\", \\\"SOX\\\", \\\")\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"within\\\", \\\"the\\\", \\\"municipality\\\", \\\"Firavitoba\\\", \\\".\\\"], \\\"h\\\": [\\\"alberto lleras camargo airport\\\", \\\"Q28163847\\\", [[6, 7, 8, 9]]], \\\"t\\\": [\\\"sogamoso\\\", \\\"Q989996\\\", [[4]]]}, {\\\"tokens\\\": [\\\"Koundara\\\", \\\"town\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Sambailo\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"sambailo airport\\\", \\\"Q7408985\\\", [[5, 6]]], \\\"t\\\": [\\\"koundara\\\", \\\"Q985374\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Atico\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"Pacific\\\", \\\"coast\\\", \\\"Atico\\\", \\\"District\\\", \\\"in\\\", \\\"the\\\", \\\"Arequipa\\\", \\\"Region\\\", \\\"of\\\", \\\"Peru\\\", \\\".\\\"], \\\"h\\\": [\\\"atico airport\\\", \\\"Q28163426\\\", [[0, 1]]], \\\"t\\\": [\\\"atico district\\\", \\\"Q3314063\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"Furatena\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"Qu\\\\u00edpama\\\", \\\"in\\\", \\\"the\\\", \\\"Boyac\\\\u00e1\\\", \\\"Department\\\", \\\"of\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"furatena airport\\\", \\\"Q28163866\\\", [[0, 1]]], \\\"t\\\": [\\\"qu\\\\u00edpama\\\", \\\"Q1575472\\\", [[9]]]}, {\\\"tokens\\\": [\\\"Meanwhile\\\", \\\",\\\", \\\"their\\\", \\\"aircraft\\\", \\\"were\\\", \\\"assembled\\\", \\\"and\\\", \\\"test\\\", \\\"flown\\\", \\\"by\\\", \\\"CAMCO\\\", \\\"staff\\\", \\\"at\\\", \\\"Mingaladon\\\", \\\"Airport\\\", \\\"outside\\\", \\\"Rangoon\\\", \\\".\\\"], \\\"h\\\": [\\\"mingaladon airport\\\", \\\"Q174764\\\", [[13, 14]]], \\\"t\\\": [\\\"rangoon\\\", \\\"Q37995\\\", [[16]]]}, {\\\"tokens\\\": [\\\"PA\\\", \\\"981\\\", \\\"then\\\", \\\"turns\\\", \\\"northward\\\", \\\",\\\", \\\"meeting\\\", \\\"U.S.\\\", \\\"30\\\", \\\"outside\\\", \\\"Latrobe\\\", \\\",\\\", \\\"near\\\", \\\"the\\\", \\\"Arnold\\\", \\\"Palmer\\\", \\\"Regional\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"arnold palmer regional airport\\\", \\\"Q2902231\\\", [[14, 15, 16, 17]]], \\\"t\\\": [\\\"latrobe\\\", \\\"Q969307\\\", [[10]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Airport\\\", \\\"in\\\", \\\"Guntersville\\\", \\\",\\\", \\\"Alabama\\\", \\\"is\\\", \\\"called\\\", \\\"Joe\\\", \\\"Starnes\\\", \\\"Field\\\", \\\".\\\", \\\"Joe\\\", \\\"Starnes\\\", \\\"Field\\\", \\\"\\\\n\\\\n \\\", \\\"Retrieved\\\", \\\"on\\\", \\\"2010\\\", \\\"-\\\", \\\"01\\\", \\\"-\\\", \\\"02\\\"], \\\"h\\\": [\\\"joe starnes field\\\", \\\"Q5619447\\\", [[8, 9, 10], [12, 13, 14]]], \\\"t\\\": [\\\"guntersville, alabama\\\", \\\"Q79556\\\", [[3, 4, 5]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"base\\\", \\\"is\\\", \\\"Ajaccio\\\", \\\"-\\\", \\\"Campo\\\", \\\"dell\\\\u2019Oro\\\", \\\"Airport\\\", \\\",\\\", \\\"with\\\", \\\"hubs\\\", \\\"at\\\", \\\"Figari\\\", \\\"Sud\\\", \\\"-\\\", \\\"Corse\\\", \\\"Airport\\\", \\\",\\\", \\\"Bastia\\\", \\\"-\\\", \\\"Poretta\\\", \\\"Airport\\\", \\\"and\\\", \\\"Calvi\\\", \\\"-\\\", \\\"Sainte\\\", \\\"-\\\", \\\"Catherine\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"poretta airport\\\", \\\"Q1430951\\\", [[21, 22]]], \\\"t\\\": [\\\"bastia\\\", \\\"Q134698\\\", [[19]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airport\\\", \\\"serving\\\", \\\"international\\\", \\\"flights\\\", \\\"in\\\", \\\"El\\\", \\\"Salvador\\\", \\\"is\\\", \\\"Comalapa\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"comalapa international airport\\\", \\\"Q587675\\\", [[9, 10, 11]]], \\\"t\\\": [\\\"el salvador\\\", \\\"Q792\\\", [[6, 7]]]}, {\\\"tokens\\\": [\\\"Grove\\\", \\\"Field\\\", \\\"is\\\", \\\"a\\\", \\\"municipal\\\", \\\"airport\\\", \\\"located\\\", \\\"north\\\", \\\"of\\\", \\\"Camas\\\", \\\"and\\\", \\\"is\\\", \\\"named\\\", \\\"in\\\", \\\"honor\\\", \\\"of\\\", \\\"Ward\\\", \\\"Grove\\\", \\\".\\\"], \\\"h\\\": [\\\"grove field\\\", \\\"Q286727\\\", [[0, 1]]], \\\"t\\\": [\\\"camas\\\", \\\"Q1507709\\\", [[9]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"airports\\\", \\\"are\\\", \\\"Boire\\\", \\\"Field\\\", \\\"in\\\", \\\"Nashua\\\", \\\"and\\\", \\\"Manchester\\\", \\\"\\\\u2013\\\", \\\"Boston\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"along\\\", \\\"the\\\", \\\"border\\\", \\\"of\\\", \\\"Londonderry\\\", \\\"and\\\", \\\"Manchester\\\", \\\".\\\"], \\\"h\\\": [\\\"boire field\\\", \\\"Q3565926\\\", [[4, 5]]], \\\"t\\\": [\\\"nashua\\\", \\\"Q48274\\\", [[7]]]}, {\\\"tokens\\\": [\\\"However\\\", \\\",\\\", \\\"the\\\", \\\"13th\\\", \\\"sultan\\\", \\\"of\\\", \\\"Deli\\\", \\\"who\\\", \\\"was\\\", \\\"a\\\", \\\"lieutenant\\\", \\\"colonel\\\", \\\"in\\\", \\\"Indonesian\\\", \\\"Army\\\", \\\"died\\\", \\\"in\\\", \\\"an\\\", \\\"Army\\\", \\\"CN235\\\", \\\"plane\\\", \\\"crash\\\", \\\"at\\\", \\\"Malikus\\\", \\\"Saleh\\\", \\\"Airport\\\", \\\",\\\", \\\"Lhokseumawe\\\", \\\",\\\", \\\"Aceh\\\", \\\",\\\", \\\"on\\\", \\\"21\\\", \\\"July\\\", \\\"2005\\\", \\\".\\\"], \\\"h\\\": [\\\"malikus saleh airport\\\", \\\"Q12693774\\\", [[23, 24, 25]]], \\\"t\\\": [\\\"lhokseumawe\\\", \\\"Q5784\\\", [[27]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Trinidad\\\", \\\"non\\\", \\\"-\\\", \\\"directional\\\", \\\"beacon\\\", \\\"(\\\", \\\"Ident\\\", \\\":\\\", \\\"TDD\\\", \\\")\\\", \\\"is\\\", \\\"located\\\", \\\"on\\\", \\\"the\\\", \\\"field\\\", \\\".\\\", \\\"Trinidad\\\", \\\"VORTrinidad\\\", \\\"NDB\\\"], \\\"h\\\": [\\\"tdd\\\", \\\"Q2875743\\\", [[9]]], \\\"t\\\": [\\\"trinidad\\\", \\\"Q34986\\\", [[1], [17]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"Montego\\\", \\\"Bay\\\", \\\"the\\\", \\\"flights\\\", \\\"arrived\\\", \\\"and\\\", \\\"departed\\\", \\\"from\\\", \\\"the\\\", \\\"Sangster\\\", \\\"International\\\", \\\"Airport\\\", \\\"'s\\\", \\\"new\\\", \\\"domestic\\\", \\\"terminal\\\", \\\".\\\"], \\\"h\\\": [\\\"sangster international airport\\\", \\\"Q174140\\\", [[10, 11, 12]]], \\\"t\\\": [\\\"montego bay\\\", \\\"Q637555\\\", [[1, 2]]]}, {\\\"tokens\\\": [\\\"Rose\\\", \\\"Bay\\\", \\\"Water\\\", \\\"Airport\\\", \\\"(\\\", \\\"IATA\\\", \\\":\\\", \\\"RSE\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"Australian\\\", \\\"water\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"Sydney\\\", \\\"suburb\\\", \\\"of\\\", \\\"Rose\\\", \\\"Bay\\\", \\\",\\\", \\\"New\\\", \\\"South\\\", \\\"Wales\\\", \\\".\\\"], \\\"h\\\": [\\\"rose bay water airport\\\", \\\"Q28219774\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"sydney\\\", \\\"Q3130\\\", [[17]]]}, {\\\"tokens\\\": [\\\"Andrews\\\", \\\"County\\\", \\\"Airport\\\", \\\"is\\\", \\\"situated\\\", \\\"on\\\", \\\"260\\\", \\\"acres\\\", \\\"in\\\", \\\"Andrews\\\", \\\",\\\", \\\"Texas\\\", \\\",\\\", \\\"1-mile\\\", \\\"northeast\\\", \\\"of\\\", \\\"the\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\",\\\", \\\"and\\\", \\\"contains\\\", \\\"three\\\", \\\"runways\\\", \\\"and\\\", \\\"one\\\", \\\"helipad\\\", \\\".\\\"], \\\"h\\\": [\\\"andrews county airport\\\", \\\"Q4759072\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"andrews, texas\\\", \\\"Q509541\\\", [[9, 10, 11]]]}, {\\\"tokens\\\": [\\\"City\\\", \\\"Express\\\", \\\"was\\\", \\\"founded\\\", \\\"by\\\", \\\"Joseph\\\", \\\"Csumrik\\\", \\\"in\\\", \\\"1971\\\", \\\"as\\\", \\\"Otonabee\\\", \\\"Airways\\\", \\\"based\\\", \\\"at\\\", \\\"Peterborough\\\", \\\"Airport\\\", \\\"in\\\", \\\"Peterborough\\\", \\\",\\\", \\\"Ontario\\\", \\\".\\\"], \\\"h\\\": [\\\"peterborough airport\\\", \\\"Q905906\\\", [[14, 15]]], \\\"t\\\": [\\\"peterborough, ontario\\\", \\\"Q776930\\\", [[17, 18, 19]]]}, {\\\"tokens\\\": [\\\"This\\\", \\\"were\\\", \\\"mostly\\\", \\\"out\\\", \\\"of\\\", \\\"Copenhagen\\\", \\\"Airport\\\", \\\"to\\\", \\\"Stavanger\\\", \\\",\\\", \\\"Kristiansand\\\", \\\",\\\", \\\"G\\\\u00f6teborg\\\", \\\"Landvetter\\\", \\\"Airport\\\", \\\"and\\\", \\\"J\\\\u00f6nk\\\\u00f6ping\\\", \\\"Airport\\\", \\\",\\\", \\\"as\\\", \\\"well\\\", \\\"as\\\", \\\"between\\\", \\\"Oslo\\\", \\\"and\\\", \\\"Gothenburg\\\", \\\".\\\"], \\\"h\\\": [\\\"g\\\\u00f6teborg landvetter airport\\\", \\\"Q1137115\\\", [[12, 13, 14]]], \\\"t\\\": [\\\"gothenburg\\\", \\\"Q25287\\\", [[25]]]}, {\\\"tokens\\\": [\\\"D\\\\u00fcsseldorf\\\", \\\"'s\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"district\\\", \\\".\\\"], \\\"h\\\": [\\\"international airport\\\", \\\"Q58226\\\", [[2, 3]]], \\\"t\\\": [\\\"d\\\\u00fcsseldorf\\\", \\\"Q1718\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Like\\\", \\\"the\\\", \\\"rest\\\", \\\"of\\\", \\\"West\\\", \\\"Coast\\\", \\\"Tasmania\\\", \\\",\\\", \\\"Strahan\\\", \\\"Airport\\\", \\\"airspace\\\", \\\"is\\\", \\\"controlled\\\", \\\"from\\\", \\\"Melbourne\\\", \\\"Airport\\\", \\\"in\\\", \\\"Victoria\\\", \\\".\\\"], \\\"h\\\": [\\\"strahan airport\\\", \\\"Q15533\\\", [[8, 9]]], \\\"t\\\": [\\\"west coast tasmania\\\", \\\"Q7984754\\\", [[4, 5, 6]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"year\\\", \\\"1969\\\", \\\"was\\\", \\\"a\\\", \\\"critical\\\", \\\"point\\\", \\\"of\\\", \\\"aviation\\\", \\\"history\\\", \\\"of\\\", \\\"Samarinda\\\", \\\",\\\", \\\"when\\\", \\\"the\\\", \\\"story\\\", \\\"of\\\", \\\"Temindung\\\", \\\"began\\\", \\\".\\\"], \\\"h\\\": [\\\"temindung\\\", \\\"Q1932805\\\", [[17]]], \\\"t\\\": [\\\"samarinda\\\", \\\"Q14499\\\", [[11]]]}, {\\\"tokens\\\": [\\\"Aktion\\\", \\\"National\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Preveza\\\", \\\"and\\\", \\\"Lefkada\\\", \\\"in\\\", \\\"Greece\\\", \\\".\\\"], \\\"h\\\": [\\\"aktion national airport\\\", \\\"Q1430743\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"preveza\\\", \\\"Q213898\\\", [[7]]]}, {\\\"tokens\\\": [\\\"Lucknow\\\", \\\"-\\\", \\\"Jhansi\\\", \\\"Passenger\\\", \\\"(\\\", \\\"Between\\\", \\\"Lucknow\\\", \\\"/\\\", \\\"LKO\\\", \\\"and\\\", \\\"Jhansi\\\", \\\"/JHS\\\", \\\")\\\"], \\\"h\\\": [\\\"lko\\\", \\\"Q2672666\\\", [[8]]], \\\"t\\\": [\\\"lucknow\\\", \\\"Q47916\\\", [[0], [6]]]}, {\\\"tokens\\\": [\\\"Airport\\\", \\\"operations\\\", \\\"were\\\", \\\"shut\\\", \\\"down\\\", \\\"in\\\", \\\"November\\\", \\\"2008\\\", \\\"and\\\", \\\"transferred\\\", \\\"to\\\", \\\"the\\\", \\\"newly\\\", \\\"opened\\\", \\\"Jos\\\\u00e9\\\", \\\"Aponte\\\", \\\"de\\\", \\\"la\\\", \\\"Torre\\\", \\\"Airport\\\", \\\"in\\\", \\\"Ceiba\\\", \\\".\\\"], \\\"h\\\": [\\\"jos\\\\u00e9 aponte de la torre airport\\\", \\\"Q2901846\\\", [[14, 15, 16, 17, 18, 19]]], \\\"t\\\": [\\\"ceiba\\\", \\\"Q2307548\\\", [[21]]]}], \\\"P4552\\\": [{\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"approximately\\\", \\\"8\\\", \\\"km\\\", \\\"away\\\", \\\"from\\\", \\\"Mount\\\", \\\"Korbu\\\", \\\",\\\", \\\"the\\\", \\\"tallest\\\", \\\"mountain\\\", \\\"of\\\", \\\"the\\\", \\\"Titiwangsa\\\", \\\"Mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"mount korbu\\\", \\\"Q6921705\\\", [[7, 8]]], \\\"t\\\": [\\\"titiwangsa mountains\\\", \\\"Q581621\\\", [[15, 16]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"endemic\\\", \\\"to\\\", \\\"Kern\\\", \\\"County\\\", \\\",\\\", \\\"California\\\", \\\",\\\", \\\"where\\\", \\\"it\\\", \\\"is\\\", \\\"known\\\", \\\"from\\\", \\\"only\\\", \\\"two\\\", \\\"occurrences\\\", \\\"at\\\", \\\"Owens\\\", \\\"Peak\\\", \\\",\\\", \\\"one\\\", \\\"of\\\", \\\"the\\\", \\\"highest\\\", \\\"points\\\", \\\"of\\\", \\\"the\\\", \\\"Sierra\\\", \\\"Nevada\\\", \\\".\\\"], \\\"h\\\": [\\\"owens peak\\\", \\\"Q7114739\\\", [[18, 19]]], \\\"t\\\": [\\\"sierra nevada\\\", \\\"Q26777\\\", [[28, 29]]]}, {\\\"tokens\\\": [\\\"Dev\\\\u00ednska\\\", \\\"Kobyla\\\", \\\"and\\\", \\\"its\\\", \\\"surroundings\\\", \\\"are\\\", \\\"one\\\", \\\"of\\\", \\\"the\\\", \\\"four\\\", \\\"divisions\\\", \\\"of\\\", \\\"Dev\\\\u00edn\\\", \\\"Carpathians\\\", \\\",\\\", \\\"part\\\", \\\"of\\\", \\\"Little\\\", \\\"Carpathians\\\", \\\",\\\", \\\"itself\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Carpathian\\\", \\\"mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"dev\\\\u00ednska kobyla\\\", \\\"Q1207065\\\", [[0, 1]]], \\\"t\\\": [\\\"little carpathians\\\", \\\"Q426712\\\", [[17, 18]]]}, {\\\"tokens\\\": [\\\"Vindegga\\\", \\\"Spur\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"prominent\\\", \\\"ridge\\\", \\\"just\\\", \\\"south\\\", \\\"of\\\", \\\"Vindegghallet\\\", \\\"Glacier\\\", \\\"in\\\", \\\"the\\\", \\\"Humboldt\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Queen\\\", \\\"Maud\\\", \\\"Land\\\", \\\".\\\"], \\\"h\\\": [\\\"vindegghallet glacier\\\", \\\"Q7932323\\\", [[11, 12]]], \\\"t\\\": [\\\"humboldt mountains\\\", \\\"Q3445748\\\", [[15, 16]]]}, {\\\"tokens\\\": [\\\"Brattnipane\\\", \\\"Peaks\\\", \\\"is\\\", \\\"a\\\", \\\"group\\\", \\\"of\\\", \\\"peaks\\\", \\\",\\\", \\\"the\\\", \\\"highest\\\", \\\"high\\\", \\\",\\\", \\\"standing\\\", \\\"northwest\\\", \\\"of\\\", \\\"Mefjell\\\", \\\"Mountain\\\", \\\"in\\\", \\\"the\\\", \\\"S\\\\u00f8r\\\", \\\"Rondane\\\", \\\"Mountains\\\", \\\",\\\", \\\"and\\\", \\\"southeast\\\", \\\"of\\\", \\\"the\\\", \\\"isolated\\\", \\\"mountain\\\", \\\"Mount\\\", \\\"Romnaes\\\", \\\".\\\"], \\\"h\\\": [\\\"mount romnaes\\\", \\\"Q6923267\\\", [[29, 30]]], \\\"t\\\": [\\\"s\\\\u00f8r rondane mountains\\\", \\\"Q1815832\\\", [[19, 20, 21]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"San\\\", \\\"Ysidro\\\", \\\"Mountains\\\", \\\"are\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Peninsular\\\", \\\"Ranges\\\", \\\"System\\\", \\\".\\\"], \\\"h\\\": [\\\"san ysidro mountains\\\", \\\"Q7415401\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"peninsular ranges\\\", \\\"Q2068951\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"Sauris\\\", \\\"is\\\", \\\"situated\\\", \\\"within\\\", \\\"the\\\", \\\"Carnia\\\", \\\"mountain\\\", \\\"area\\\", \\\"of\\\", \\\"Friuli\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"Lumiei\\\", \\\"Valley\\\", \\\"(\\\", \\\"\\\\\\\"\\\", \\\"Val\\\", \\\"Lumiei\\\", \\\"\\\\\\\"\\\", \\\")\\\", \\\"of\\\", \\\"the\\\", \\\"Carnic\\\", \\\"Alps\\\", \\\",\\\", \\\"northwest\\\", \\\"of\\\", \\\"the\\\", \\\"Monte\\\", \\\"B\\\\u00ecvera\\\", \\\"massif\\\", \\\".\\\"], \\\"h\\\": [\\\"monte b\\\\u00ecvera\\\", \\\"Q3548146\\\", [[29, 30]]], \\\"t\\\": [\\\"carnic alps\\\", \\\"Q660390\\\", [[23, 24]]]}, {\\\"tokens\\\": [\\\"Kamskaya\\\", \\\"Peak\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\",\\\", \\\"at\\\", \\\",\\\", \\\"the\\\", \\\"highest\\\", \\\"peak\\\", \\\"of\\\", \\\"Dekefjellet\\\", \\\"Mountain\\\", \\\"in\\\", \\\"the\\\", \\\"Weyprecht\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Queen\\\", \\\"Maud\\\", \\\"Land\\\", \\\",\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"dekefjellet mountain\\\", \\\"Q5252790\\\", [[12, 13]]], \\\"t\\\": [\\\"weyprecht mountains\\\", \\\"Q5483275\\\", [[16, 17]]]}, {\\\"tokens\\\": [\\\"Solitary\\\", \\\"Mountain\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\"in\\\", \\\"the\\\", \\\"Big\\\", \\\"Salmon\\\", \\\"Range\\\", \\\"of\\\", \\\"the\\\", \\\"Pelly\\\", \\\"Mountains\\\", \\\"in\\\", \\\"southcentral\\\", \\\"Yukon\\\", \\\",\\\", \\\"Canada\\\", \\\",\\\", \\\"located\\\", \\\"southwest\\\", \\\"of\\\", \\\"Faro\\\", \\\".\\\"], \\\"h\\\": [\\\"big salmon range\\\", \\\"Q4906262\\\", [[7, 8, 9]]], \\\"t\\\": [\\\"pelly mountains\\\", \\\"Q2068206\\\", [[12, 13]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Tennessee\\\", \\\"River\\\", \\\"reaches\\\", \\\"easterly\\\", \\\"to\\\", \\\"the\\\", \\\"Ridge\\\", \\\"and\\\", \\\"Valley\\\", \\\"Province\\\", \\\"of\\\", \\\"the\\\", \\\"Great\\\", \\\"Smoky\\\", \\\"Mountains\\\", \\\",\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Blue\\\", \\\"Ridge\\\", \\\"Mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"great smoky mountains\\\", \\\"Q1360486\\\", [[13, 14, 15]]], \\\"t\\\": [\\\"blue ridge mountains\\\", \\\"Q166755\\\", [[20, 21, 22]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Petit\\\", \\\"Mont\\\", \\\"Collon\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\"of\\\", \\\"the\\\", \\\"Swiss\\\", \\\"Pennine\\\", \\\"Alps\\\", \\\",\\\", \\\"located\\\", \\\"south\\\", \\\"of\\\", \\\"Arolla\\\", \\\"in\\\", \\\"the\\\", \\\"canton\\\", \\\"of\\\", \\\"Valais\\\", \\\".\\\"], \\\"h\\\": [\\\"petit mont collon\\\", \\\"Q674348\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"pennine alps\\\", \\\"Q1270\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"Dunn\\\", \\\"Glacier\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"steep\\\", \\\"tributary\\\", \\\"glacier\\\", \\\"which\\\", \\\"drains\\\", \\\"the\\\", \\\"northwest\\\", \\\"slopes\\\", \\\"of\\\", \\\"Mount\\\", \\\"Casey\\\", \\\"and\\\", \\\"flows\\\", \\\"north\\\", \\\"to\\\", \\\"Icebreaker\\\", \\\"Glacier\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"Mountaineer\\\", \\\"Range\\\", \\\",\\\", \\\"Victoria\\\", \\\"Land\\\", \\\".\\\"], \\\"h\\\": [\\\"dunn glacier\\\", \\\"Q5315547\\\", [[0, 1]]], \\\"t\\\": [\\\"mountaineer range\\\", \\\"Q6925644\\\", [[26, 27]]]}, {\\\"tokens\\\": [\\\"Croll\\\", \\\"Glacier\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"tributary\\\", \\\"glacier\\\", \\\"flowing\\\", \\\"southeast\\\", \\\"along\\\", \\\"the\\\", \\\"north\\\", \\\"side\\\", \\\"of\\\", \\\"Handler\\\", \\\"Ridge\\\", \\\"into\\\", \\\"Trafalgar\\\", \\\"Glacier\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"Victory\\\", \\\"Mountains\\\", \\\",\\\", \\\"Victoria\\\", \\\"Land\\\", \\\".\\\"], \\\"h\\\": [\\\"trafalgar glacier\\\", \\\"Q7832415\\\", [[18, 19]]], \\\"t\\\": [\\\"victory mountains\\\", \\\"Q7608101\\\", [[23, 24]]]}, {\\\"tokens\\\": [\\\"Several\\\", \\\"small\\\", \\\"glaciers\\\", \\\"still\\\", \\\"persist\\\", \\\"in\\\", \\\"the\\\", \\\"Durmitor\\\", \\\"and\\\", \\\"Prokletije\\\", \\\"ranges\\\", \\\",\\\", \\\"the\\\", \\\"Dinaric\\\", \\\"Alps\\\", \\\"'\\\", \\\"highest\\\", \\\"massifs\\\", \\\".\\\"], \\\"h\\\": [\\\"durmitor\\\", \\\"Q212836\\\", [[7]]], \\\"t\\\": [\\\"dinaric alps\\\", \\\"Q189915\\\", [[13, 14]]]}, {\\\"tokens\\\": [\\\"Pen\\\", \\\"y\\\", \\\"Brynfforchog\\\", \\\"is\\\", \\\"subsidiary\\\", \\\"summit\\\", \\\"of\\\", \\\"Glasgwm\\\", \\\"in\\\", \\\"North\\\", \\\"Wales\\\", \\\"forming\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Aran\\\", \\\"range\\\", \\\"in\\\", \\\"southern\\\", \\\"Snowdonia\\\", \\\".\\\", \\\"Nuttall\\\", \\\",\\\", \\\"John\\\", \\\"&\\\", \\\"Anne\\\", \\\"(\\\", \\\"1999\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"glasgwm\\\", \\\"Q5566987\\\", [[7]]], \\\"t\\\": [\\\"snowdonia\\\", \\\"Q867913\\\", [[19]]]}, {\\\"tokens\\\": [\\\"Gould\\\", \\\"Spur\\\", \\\"is\\\", \\\"a\\\", \\\"spur\\\", \\\",\\\", \\\"long\\\", \\\",\\\", \\\"that\\\", \\\"extends\\\", \\\"from\\\", \\\"Navigator\\\", \\\"Peak\\\", \\\"to\\\", \\\"the\\\", \\\"south\\\", \\\"side\\\", \\\"of\\\", \\\"Splettstoesser\\\", \\\"Glacier\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"Heritage\\\", \\\"Range\\\", \\\"of\\\", \\\"the\\\", \\\"Ellsworth\\\", \\\"Mountains\\\", \\\",\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"navigator peak\\\", \\\"Q1972363\\\", [[11, 12]]], \\\"t\\\": [\\\"heritage range\\\", \\\"Q1522169\\\", [[23, 24]]]}, {\\\"tokens\\\": [\\\"Balakirev\\\", \\\"Glacier\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"Antarctic\\\", \\\"glacier\\\", \\\"flowing\\\", \\\"northeast\\\", \\\"into\\\", \\\"Schubert\\\", \\\"Inlet\\\", \\\"from\\\", \\\"the\\\", \\\"south\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Walton\\\", \\\"Mountains\\\", \\\",\\\", \\\"Alexander\\\", \\\"Island\\\", \\\".\\\"], \\\"h\\\": [\\\"balakirev glacier\\\", \\\"Q4849878\\\", [[0, 1]]], \\\"t\\\": [\\\"walton mountains\\\", \\\"Q7966766\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Colfax\\\", \\\"County\\\", \\\"about\\\", \\\"south\\\", \\\"of\\\", \\\"Baldy\\\", \\\"Mountain\\\", \\\"in\\\", \\\"the\\\", \\\"Cimarron\\\", \\\"Range\\\", \\\",\\\", \\\"a\\\", \\\"subrange\\\", \\\"of\\\", \\\"the\\\", \\\"Sangre\\\", \\\"de\\\", \\\"Cristo\\\", \\\"Mountains\\\", \\\"of\\\", \\\"New\\\", \\\"Mexico\\\", \\\".\\\"], \\\"h\\\": [\\\"baldy mountain\\\", \\\"Q4850647\\\", [[9, 10]]], \\\"t\\\": [\\\"sangre de cristo mountains\\\", \\\"Q2328749\\\", [[20, 21, 22, 23]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"highest\\\", \\\"elevation\\\", \\\"in\\\", \\\"the\\\", \\\"Innerste\\\", \\\"Uplands\\\", \\\"is\\\", \\\"the\\\", \\\"359\\\", \\\"\\\\u00a0\\\", \\\"m\\\", \\\"high\\\", \\\"Griesberg\\\", \\\"in\\\", \\\"the\\\", \\\"Hildesheim\\\", \\\"Forest\\\", \\\".\\\"], \\\"h\\\": [\\\"hildesheim forest\\\", \\\"Q1618461\\\", [[16, 17]]], \\\"t\\\": [\\\"innerste uplands\\\", \\\"Q1664079\\\", [[5, 6]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"north\\\", \\\"region\\\", \\\"of\\\", \\\"the\\\", \\\"county\\\", \\\"consists\\\", \\\"of\\\", \\\"the\\\", \\\"Wichita\\\", \\\"Mountains\\\", \\\"including\\\", \\\"Mount\\\", \\\"Scott\\\", \\\"and\\\", \\\"Mount\\\", \\\"Pinchot\\\", \\\"the\\\", \\\"area\\\", \\\"'s\\\", \\\"highest\\\", \\\"peaks\\\", \\\".\\\"], \\\"h\\\": [\\\"mount pinchot\\\", \\\"Q6922759\\\", [[15, 16]]], \\\"t\\\": [\\\"wichita mountains\\\", \\\"Q3305333\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"Towards\\\", \\\"the\\\", \\\"north\\\", \\\",\\\", \\\"the\\\", \\\"Black\\\", \\\"Forest\\\", \\\"only\\\", \\\"exceeds\\\", \\\"this\\\", \\\"height\\\", \\\"again\\\", \\\"in\\\", \\\"the\\\", \\\"area\\\", \\\"of\\\", \\\"the\\\", \\\"Schliffkopf\\\", \\\"and\\\", \\\"the\\\", \\\"Hornisgrinde\\\", \\\".\\\"], \\\"h\\\": [\\\"schliffkopf\\\", \\\"Q881889\\\", [[17]]], \\\"t\\\": [\\\"black forest\\\", \\\"Q4204\\\", [[5, 6]]]}, {\\\"tokens\\\": [\\\"Artesonraju\\\", \\\"has\\\", \\\"two\\\", \\\"distinguished\\\", \\\"climbing\\\", \\\"routes\\\", \\\";\\\", \\\"however\\\", \\\"due\\\", \\\"to\\\", \\\"their\\\", \\\"difficulties\\\", \\\",\\\", \\\"Artesonraju\\\", \\\"is\\\", \\\"seldom\\\", \\\"successfully\\\", \\\"climbed\\\", \\\"in\\\", \\\"comparison\\\", \\\"to\\\", \\\"other\\\", \\\"well\\\", \\\"known\\\", \\\"mountains\\\", \\\"in\\\", \\\"the\\\", \\\"Cordillera\\\", \\\"Blanca\\\", \\\".\\\"], \\\"h\\\": [\\\"artesonraju\\\", \\\"Q707934\\\", [[0], [13]]], \\\"t\\\": [\\\"cordillera blanca\\\", \\\"Q804330\\\", [[27, 28]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Borchgrevink\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\",\\\", \\\"high\\\", \\\",\\\", \\\"standing\\\", \\\"south\\\", \\\"of\\\", \\\"the\\\", \\\"Tanngarden\\\", \\\"Peaks\\\", \\\"in\\\", \\\"the\\\", \\\"S\\\\u00f8r\\\", \\\"Rondane\\\", \\\"Mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"tanngarden peaks\\\", \\\"Q7683684\\\", [[14, 15]]], \\\"t\\\": [\\\"s\\\\u00f8r rondane mountains\\\", \\\"Q1815832\\\", [[18, 19, 20]]]}, {\\\"tokens\\\": [\\\"Chimborazo\\\", \\\"is\\\", \\\"in\\\", \\\"the\\\", \\\"Cordillera\\\", \\\"Occidental\\\", \\\"of\\\", \\\"the\\\", \\\"Andes\\\", \\\"of\\\", \\\"central\\\", \\\"Ecuador\\\", \\\",\\\", \\\"150\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\"(\\\", \\\"93\\\", \\\"\\\\u00a0\\\", \\\"mi\\\", \\\")\\\", \\\"south\\\", \\\"-\\\", \\\"southwest\\\", \\\"of\\\", \\\"the\\\", \\\"capital\\\", \\\"Quito\\\", \\\".\\\"], \\\"h\\\": [\\\"chimborazo\\\", \\\"Q14081\\\", [[0]]], \\\"t\\\": [\\\"cordillera occidental\\\", \\\"Q779298\\\", [[4, 5]]]}, {\\\"tokens\\\": [\\\"Blake\\\", \\\"Rock\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"isolated\\\", \\\"rock\\\", \\\"lying\\\", \\\"south\\\", \\\"of\\\", \\\"the\\\", \\\"south\\\", \\\"end\\\", \\\"of\\\", \\\"Mackin\\\", \\\"Table\\\", \\\"in\\\", \\\"the\\\", \\\"Patuxent\\\", \\\"Range\\\", \\\",\\\", \\\"Pensacola\\\", \\\"Mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"mackin table\\\", \\\"Q6724497\\\", [[15, 16]]], \\\"t\\\": [\\\"pensacola mountains\\\", \\\"Q2913098\\\", [[22, 23]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Appalachian\\\", \\\"Trail\\\", \\\"passes\\\", \\\"through\\\", \\\"Caledonia\\\", \\\"State\\\", \\\"Park\\\", \\\"as\\\", \\\"it\\\", \\\"traverses\\\", \\\"the\\\", \\\"Appalachian\\\", \\\"Mountains\\\", \\\"between\\\", \\\"Georgia\\\", \\\"and\\\", \\\"Maine\\\", \\\".\\\"], \\\"h\\\": [\\\"appalachian trail\\\", \\\"Q620648\\\", [[1, 2]]], \\\"t\\\": [\\\"appalachian mountains\\\", \\\"Q93332\\\", [[12, 13]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Firlingane\\\", \\\"Nunataks\\\", \\\"(\\\", \\\"coordinates\\\", \\\":\\\", \\\"71\\\", \\\"\\\\u00b0\\\", \\\"52\\\\u2032S\\\", \\\"27\\\", \\\"\\\\u00b0\\\", \\\"7\\\\u2032E\\\", \\\")\\\", \\\"are\\\", \\\"four\\\", \\\"nunataks\\\", \\\"standing\\\", \\\"between\\\", \\\"Bulken\\\", \\\"Hill\\\", \\\"and\\\", \\\"Hesteskoen\\\", \\\"Nunatak\\\", \\\"in\\\", \\\"the\\\", \\\"S\\\\u00f8r\\\", \\\"Rondane\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"hesteskoen nunatak\\\", \\\"Q13728922\\\", [[21, 22]]], \\\"t\\\": [\\\"s\\\\u00f8r rondane mountains\\\", \\\"Q1815832\\\", [[25, 26, 27]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"2014\\\", \\\"the\\\", \\\"ministers\\\", \\\"met\\\", \\\"in\\\", \\\"Narva\\\", \\\",\\\", \\\"Estonia\\\", \\\";\\\", \\\"in\\\", \\\"2015\\\", \\\"-\\\", \\\"in\\\", \\\"High\\\", \\\"Tatras\\\", \\\"at\\\", \\\"\\\\u0160trbsk\\\\u00e9\\\", \\\"Pleso\\\", \\\",\\\", \\\"Slovakia\\\", \\\".\\\"], \\\"h\\\": [\\\"\\\\u0161trbsk\\\\u00e9 pleso\\\", \\\"Q392489\\\", [[17, 18]]], \\\"t\\\": [\\\"high tatras\\\", \\\"Q690323\\\", [[14, 15]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Cummings\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\"at\\\", \\\"the\\\", \\\"eastern\\\", \\\"end\\\", \\\"of\\\", \\\"Galan\\\", \\\"Ridge\\\", \\\"in\\\", \\\"the\\\", \\\"Dana\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Palmer\\\", \\\"Land\\\", \\\".\\\"], \\\"h\\\": [\\\"galan ridge\\\", \\\"Q5517927\\\", [[10, 11]]], \\\"t\\\": [\\\"dana mountains\\\", \\\"Q5214795\\\", [[14, 15]]]}, {\\\"tokens\\\": [\\\"Zittel\\\", \\\"Cliffs\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"set\\\", \\\"of\\\", \\\"cliffs\\\", \\\"rising\\\", \\\"to\\\", \\\"about\\\", \\\"1,400\\\", \\\"m\\\", \\\"in\\\", \\\"the\\\", \\\"northwest\\\", \\\"part\\\", \\\"of\\\", \\\"Du\\\", \\\"Toit\\\", \\\"Nunataks\\\", \\\",\\\", \\\"Read\\\", \\\"Mountains\\\", \\\",\\\", \\\"Shackleton\\\", \\\"Range\\\", \\\".\\\"], \\\"h\\\": [\\\"du toit nunataks\\\", \\\"Q5310080\\\", [[19, 20, 21]]], \\\"t\\\": [\\\"read mountains\\\", \\\"Q2913015\\\", [[23, 24]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Hainbach\\\", \\\"rises\\\", \\\"at\\\", \\\"a\\\", \\\"height\\\", \\\"of\\\", \\\"on\\\", \\\"the\\\", \\\"east\\\", \\\"flank\\\", \\\"of\\\", \\\"the\\\", \\\"Ro\\\\u00dfberg\\\", \\\"mountain\\\", \\\"(\\\", \\\")\\\", \\\"in\\\", \\\"the\\\", \\\"Haardt\\\", \\\",\\\", \\\"the\\\", \\\"eastern\\\", \\\"edge\\\", \\\"of\\\", \\\"the\\\", \\\"Palatinate\\\", \\\"Forest\\\", \\\"range\\\", \\\".\\\"], \\\"h\\\": [\\\"ro\\\\u00dfberg\\\", \\\"Q1359604\\\", [[13]]], \\\"t\\\": [\\\"haardt\\\", \\\"Q837186\\\", [[19]]]}, {\\\"tokens\\\": [\\\"High\\\", \\\"Raise\\\", \\\"is\\\", \\\"a\\\", \\\"fell\\\", \\\"in\\\", \\\"the\\\", \\\"English\\\", \\\"Lake\\\", \\\"District\\\", \\\",\\\", \\\"standing\\\", \\\"to\\\", \\\"the\\\", \\\"west\\\", \\\"of\\\", \\\"Haweswater\\\", \\\"Reservoir\\\", \\\"in\\\", \\\"the\\\", \\\"Far\\\", \\\"Eastern\\\", \\\"Fells\\\", \\\".\\\"], \\\"h\\\": [\\\"high raise\\\", \\\"Q3785531\\\", [[0, 1]]], \\\"t\\\": [\\\"lake district\\\", \\\"Q211778\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"Starbuck\\\", \\\"Cirque\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"remarkable\\\", \\\"cirque\\\", \\\",\\\", \\\"4\\\", \\\"nautical\\\", \\\"miles\\\", \\\"(\\\", \\\"7\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"wide\\\", \\\",\\\", \\\"between\\\", \\\"the\\\", \\\"base\\\", \\\"of\\\", \\\"Tentacle\\\", \\\"Ridge\\\", \\\"and\\\", \\\"Mount\\\", \\\"Hughes\\\", \\\"in\\\", \\\"Cook\\\", \\\"Mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"mount hughes\\\", \\\"Q6921355\\\", [[26, 27]]], \\\"t\\\": [\\\"cook mountains\\\", \\\"Q5166989\\\", [[29, 30]]]}, {\\\"tokens\\\": [\\\"Syningen\\\", \\\"Nunatak\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"nunatak\\\", \\\"1\\\", \\\"mile\\\", \\\"(\\\", \\\"1.6\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"south\\\", \\\"of\\\", \\\"See\\\", \\\"Nunatak\\\", \\\"in\\\", \\\"the\\\", \\\"eastern\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Hansen\\\", \\\"Mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"see nunatak\\\", \\\"Q7445518\\\", [[16, 17]]], \\\"t\\\": [\\\"hansen mountains\\\", \\\"Q5651051\\\", [[24, 25]]]}, {\\\"tokens\\\": [\\\"Harvey\\\", \\\"Summit\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"peak\\\", \\\"high\\\", \\\"at\\\", \\\"the\\\", \\\"head\\\", \\\"of\\\", \\\"McDermott\\\", \\\"Glacier\\\", \\\"in\\\", \\\"the\\\", \\\"Royal\\\", \\\"Society\\\", \\\"Range\\\", \\\"of\\\", \\\"Victoria\\\", \\\"Land\\\", \\\",\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"mcdermott glacier\\\", \\\"Q6800853\\\", [[12, 13]]], \\\"t\\\": [\\\"royal society range\\\", \\\"Q473357\\\", [[16, 17, 18]]]}, {\\\"tokens\\\": [\\\"Geologically\\\", \\\",\\\", \\\"the\\\", \\\"Vranica\\\", \\\"range\\\", \\\"is\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Dinaric\\\", \\\"Alps\\\", \\\"and\\\", \\\"formed\\\", \\\"largely\\\", \\\"of\\\", \\\"secondary\\\", \\\"and\\\", \\\"tertiary\\\", \\\"sedimentary\\\", \\\"rock\\\", \\\",\\\", \\\"mostly\\\", \\\"limestone\\\", \\\".\\\"], \\\"h\\\": [\\\"vranica\\\", \\\"Q1392085\\\", [[3]]], \\\"t\\\": [\\\"dinaric alps\\\", \\\"Q189915\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"These\\\", \\\"plant\\\", \\\"species\\\", \\\"are\\\", \\\"endemic\\\", \\\"to\\\", \\\"Southeast\\\", \\\"Dinaric\\\", \\\"mountains\\\", \\\"range\\\", \\\"of\\\", \\\"Bjela\\\\u0161nica\\\", \\\"and\\\", \\\"mountains\\\", \\\"of\\\", \\\"Herzegovina\\\", \\\"endemic\\\", \\\"center\\\", \\\"\\\\u2013\\\", \\\"Prenj\\\", \\\",\\\", \\\"\\\\u010cvrsnica\\\", \\\"(\\\", \\\"with\\\", \\\"the\\\", \\\"Plasa\\\", \\\")\\\", \\\",\\\", \\\"\\\\u010cabulja\\\", \\\",\\\", \\\"and\\\", \\\"Vele\\\\u017e\\\", \\\".\\\"], \\\"h\\\": [\\\"\\\\u010dabulja\\\", \\\"Q3499173\\\", [[28]]], \\\"t\\\": [\\\"dinaric mountains\\\", \\\"Q189915\\\", [[7, 8]]]}, {\\\"tokens\\\": [\\\"Baulch\\\", \\\"Peak\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"peak\\\", \\\"northeast\\\", \\\"of\\\", \\\"Claydon\\\", \\\"Peak\\\", \\\",\\\", \\\"marking\\\", \\\"the\\\", \\\"extremity\\\", \\\"of\\\", \\\"a\\\", \\\"spur\\\", \\\"descending\\\", \\\"north\\\", \\\"from\\\", \\\"Prince\\\", \\\"Andrew\\\", \\\"Plateau\\\", \\\",\\\", \\\"Queen\\\", \\\"Elizabeth\\\", \\\"Range\\\", \\\".\\\"], \\\"h\\\": [\\\"claydon peak\\\", \\\"Q5130082\\\", [[9, 10]]], \\\"t\\\": [\\\"queen elizabeth range\\\", \\\"Q3323150\\\", [[25, 26, 27]]]}, {\\\"tokens\\\": [\\\"Gluvreklett\\\", \\\"Glacier\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"glacier\\\", \\\"flowing\\\", \\\"northwest\\\", \\\"between\\\", \\\"Von\\\", \\\"Essen\\\", \\\"Mountain\\\", \\\"and\\\", \\\"Terningskarvet\\\", \\\"Mountain\\\", \\\"in\\\", \\\"the\\\", \\\"Gjelsvik\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Queen\\\", \\\"Maud\\\", \\\"Land\\\", \\\",\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"gluvreklett glacier\\\", \\\"Q11829778\\\", [[0, 1]]], \\\"t\\\": [\\\"gjelsvik mountains\\\", \\\"Q3445710\\\", [[18, 19]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Goodale\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\"with\\\", \\\"double\\\", \\\"summits\\\", \\\",\\\", \\\"high\\\", \\\",\\\", \\\"standing\\\", \\\"southeast\\\", \\\"of\\\", \\\"Mount\\\", \\\"Thorne\\\", \\\"in\\\", \\\"the\\\", \\\"Hays\\\", \\\"Mountains\\\", \\\"of\\\", \\\"the\\\", \\\"Queen\\\", \\\"Maud\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"mount thorne\\\", \\\"Q6924105\\\", [[16, 17]]], \\\"t\\\": [\\\"hays mountains\\\", \\\"Q5687208\\\", [[20, 21]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"flows\\\", \\\"from\\\", \\\"Tavan\\\", \\\"Bogd\\\", \\\"mountain\\\", \\\"of\\\", \\\"the\\\", \\\"Altai\\\", \\\"Mountains\\\", \\\"to\\\", \\\"Khar\\\", \\\"-\\\", \\\"Us\\\", \\\"Lake\\\", \\\".\\\"], \\\"h\\\": [\\\"tavan bogd\\\", \\\"Q143008\\\", [[3, 4]]], \\\"t\\\": [\\\"altai mountains\\\", \\\"Q5955\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"a\\\", \\\"subrange\\\", \\\"of\\\", \\\"the\\\", \\\"Queen\\\", \\\"Charlotte\\\", \\\"Mountains\\\", \\\"which\\\", \\\"in\\\", \\\"turn\\\", \\\"form\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Insular\\\", \\\"Mountains\\\", \\\".\\\", \\\"Crease\\\", \\\"Range\\\", \\\"in\\\", \\\"the\\\", \\\"Canadian\\\", \\\"Mountain\\\", \\\"Encyclopedia\\\"], \\\"h\\\": [\\\"queen charlotte mountains\\\", \\\"Q7270250\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"insular mountains\\\", \\\"Q386665\\\", [[16, 17]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"surrounding\\\", \\\"Desatoya\\\", \\\"Peak\\\", \\\"are\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Desatoya\\\", \\\"Mountains\\\", \\\"Wilderness\\\", \\\"Study\\\", \\\"Area\\\", \\\"which\\\", \\\"is\\\", \\\"administered\\\", \\\"by\\\", \\\"the\\\", \\\"Bureau\\\", \\\"of\\\", \\\"Land\\\", \\\"Management\\\", \\\".\\\"], \\\"h\\\": [\\\"desatoya peak\\\", \\\"Q5263639\\\", [[2, 3]]], \\\"t\\\": [\\\"desatoya mountains\\\", \\\"Q5263636\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Allen\\\", \\\"Young\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"prominent\\\", \\\"pyramidal\\\", \\\"mountain\\\", \\\",\\\", \\\"2,755\\\", \\\"m\\\", \\\",\\\", \\\"standing\\\", \\\"just\\\", \\\"south\\\", \\\"of\\\", \\\"Fegley\\\", \\\"Glacier\\\", \\\"and\\\", \\\"west\\\", \\\"of\\\", \\\"Lennox\\\", \\\"-\\\", \\\"King\\\", \\\"Glacier\\\", \\\"in\\\", \\\"the\\\", \\\"Holland\\\", \\\"Range\\\", \\\".\\\"], \\\"h\\\": [\\\"mount allen young\\\", \\\"Q6919368\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"holland range\\\", \\\"Q5881066\\\", [[29, 30]]]}, {\\\"tokens\\\": [\\\"Baillie\\\", \\\"Peak\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"peak\\\", \\\"over\\\", \\\"high\\\", \\\",\\\", \\\"located\\\", \\\"south\\\", \\\"-\\\", \\\"southeast\\\", \\\"of\\\", \\\"Mount\\\", \\\"Angier\\\", \\\"in\\\", \\\"the\\\", \\\"Moore\\\", \\\"Mountains\\\", \\\",\\\", \\\"Queen\\\", \\\"Elizabeth\\\", \\\"Range\\\", \\\",\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"mount angier\\\", \\\"Q9297193\\\", [[15, 16]]], \\\"t\\\": [\\\"moore mountains\\\", \\\"Q6908189\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Olympus\\\", \\\"or\\\", \\\"Olympus\\\", \\\"Cove\\\", \\\"is\\\", \\\"a\\\", \\\"neighborhood\\\", \\\"in\\\", \\\"Millcreek\\\", \\\",\\\", \\\"Utah\\\", \\\"built\\\", \\\"on\\\", \\\"the\\\", \\\"northwestern\\\", \\\"slopes\\\", \\\"of\\\", \\\"Mount\\\", \\\"Olympus\\\", \\\"of\\\", \\\"the\\\", \\\"Wasatch\\\", \\\"Range\\\", \\\".\\\"], \\\"h\\\": [\\\"mount olympus\\\", \\\"Q6922584\\\", [[0, 1], [18, 19]]], \\\"t\\\": [\\\"wasatch range\\\", \\\"Q1544388\\\", [[22, 23]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Nordhill\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"high\\\", \\\",\\\", \\\"sharp\\\", \\\"-\\\", \\\"pointed\\\", \\\"peak\\\", \\\"between\\\", \\\"Steel\\\", \\\"Peak\\\", \\\"and\\\", \\\"Kosky\\\", \\\"Peak\\\", \\\"in\\\", \\\"the\\\", \\\"east\\\", \\\"ridge\\\", \\\"of\\\", \\\"the\\\", \\\"Welch\\\", \\\"Mountains\\\", \\\",\\\", \\\"in\\\", \\\"Palmer\\\", \\\"Land\\\", \\\".\\\"], \\\"h\\\": [\\\"steel peak\\\", \\\"Q7425786\\\", [[13, 14]]], \\\"t\\\": [\\\"welch mountains\\\", \\\"Q7980553\\\", [[24, 25]]]}, {\\\"tokens\\\": [\\\"Kjelbotn\\\", \\\"Peak\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"peak\\\", \\\",\\\", \\\"high\\\", \\\",\\\", \\\"standing\\\", \\\"between\\\", \\\"Isachsen\\\", \\\"Mountain\\\", \\\"and\\\", \\\"Devold\\\", \\\"Peak\\\", \\\"in\\\", \\\"the\\\", \\\"S\\\\u00f8r\\\", \\\"Rondane\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"devold peak\\\", \\\"Q5267655\\\", [[15, 16]]], \\\"t\\\": [\\\"s\\\\u00f8r rondane mountains\\\", \\\"Q1815832\\\", [[19, 20, 21]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Lamadaya\\\", \\\"waterfalls\\\", \\\"is\\\", \\\"one\\\", \\\"of\\\", \\\"the\\\", \\\"best\\\", \\\"scenery\\\", \\\"in\\\", \\\"Cal\\\", \\\"Madow\\\", \\\".\\\"], \\\"h\\\": [\\\"lamadaya\\\", \\\"Q6480762\\\", [[1]]], \\\"t\\\": [\\\"cal madow\\\", \\\"Q1808897\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Huckle\\\", \\\"is\\\", \\\"the\\\", \\\"fourth\\\", \\\"highest\\\", \\\"mountain\\\", \\\"of\\\", \\\"Alexander\\\", \\\"Island\\\", \\\",\\\", \\\"proceeded\\\", \\\"by\\\", \\\"Mount\\\", \\\"Cupola\\\", \\\"and\\\", \\\"succeeded\\\", \\\"by\\\", \\\"Mount\\\", \\\"Paris\\\", \\\"in\\\", \\\"the\\\", \\\"nearby\\\", \\\"Rouen\\\", \\\"Mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"mount cupola\\\", \\\"Q7220636\\\", [[13, 14]]], \\\"t\\\": [\\\"rouen mountains\\\", \\\"Q7370759\\\", [[23, 24]]]}, {\\\"tokens\\\": [\\\"Bartlett\\\", \\\"Bench\\\", \\\"is\\\", \\\"a\\\", \\\"bare\\\", \\\",\\\", \\\"flat\\\", \\\"benchlike\\\", \\\"elevation\\\", \\\"which\\\", \\\"overlooks\\\", \\\"Bartlett\\\", \\\"Glacier\\\", \\\"from\\\", \\\"the\\\", \\\"east\\\", \\\",\\\", \\\"located\\\", \\\"south\\\", \\\"-\\\", \\\"southwest\\\", \\\"of\\\", \\\"Mount\\\", \\\"Ruth\\\", \\\"in\\\", \\\"the\\\", \\\"Queen\\\", \\\"Maud\\\", \\\"Mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"mount ruth\\\", \\\"Q11402625\\\", [[22, 23]]], \\\"t\\\": [\\\"queen maud mountains\\\", \\\"Q1796029\\\", [[26, 27, 28]]]}, {\\\"tokens\\\": [\\\"Vindegga\\\", \\\"Ridge\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"ridge\\\", \\\"of\\\", \\\"low\\\", \\\"peaks\\\", \\\"extending\\\", \\\"north\\\", \\\"from\\\", \\\"Huldreslottet\\\", \\\"Mountain\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"south\\\", \\\"part\\\", \\\"of\\\", \\\"Borg\\\", \\\"Massif\\\", \\\"in\\\", \\\"Queen\\\", \\\"Maud\\\", \\\"Land\\\", \\\".\\\"], \\\"h\\\": [\\\"huldreslottet mountain\\\", \\\"Q5935621\\\", [[13, 14]]], \\\"t\\\": [\\\"borg massif\\\", \\\"Q3298193\\\", [[21, 22]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Kerr\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\"about\\\", \\\"south\\\", \\\"of\\\", \\\"Mount\\\", \\\"Creighton\\\", \\\"in\\\", \\\"the\\\", \\\"Porthos\\\", \\\"Range\\\", \\\"of\\\", \\\"the\\\", \\\"Prince\\\", \\\"Charles\\\", \\\"Mountains\\\", \\\",\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"mount creighton\\\", \\\"Q6582559\\\", [[10, 11]]], \\\"t\\\": [\\\"porthos range\\\", \\\"Q7231792\\\", [[14, 15]]]}, {\\\"tokens\\\": [\\\"MGNP\\\", \\\"includes\\\", \\\"three\\\", \\\"of\\\", \\\"the\\\", \\\"eight\\\", \\\"Virunga\\\", \\\"Mountains\\\", \\\"volcanoes\\\", \\\":\\\", \\\"Mount\\\", \\\"Muhabura\\\", \\\",\\\", \\\"Mount\\\", \\\"Gahinga\\\", \\\",\\\", \\\"and\\\", \\\"Mount\\\", \\\"Sabyinyo\\\", \\\".\\\"], \\\"h\\\": [\\\"mount muhabura\\\", \\\"Q543030\\\", [[10, 11]]], \\\"t\\\": [\\\"virunga mountains\\\", \\\"Q751607\\\", [[6, 7]]]}, {\\\"tokens\\\": [\\\"Abus\\\", \\\"Valley\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"ice\\\", \\\"-\\\", \\\"free\\\", \\\"valley\\\", \\\"southeast\\\", \\\"of\\\", \\\"Turnstile\\\", \\\"Ridge\\\", \\\"at\\\", \\\"the\\\", \\\"north\\\", \\\"end\\\", \\\"of\\\", \\\"Britannia\\\", \\\"Range\\\", \\\".\\\"], \\\"h\\\": [\\\"turnstile ridge\\\", \\\"Q7856109\\\", [[12, 13]]], \\\"t\\\": [\\\"britannia range\\\", \\\"Q4969300\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"Cima\\\", \\\"dei\\\", \\\"Preti\\\", \\\"(\\\", \\\"Italian\\\", \\\":\\\", \\\"\\\\\\\"\\\", \\\"Priests\\\", \\\"'\\\", \\\"Peak\\\", \\\"\\\\\\\"\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\"in\\\", \\\"the\\\", \\\"Carnic\\\", \\\"Prealps\\\", \\\",\\\", \\\"the\\\", \\\"highest\\\", \\\"peak\\\", \\\"of\\\", \\\"the\\\", \\\"Friulian\\\", \\\"Dolomites\\\", \\\",\\\", \\\"Italy\\\", \\\".\\\"], \\\"h\\\": [\\\"cima dei preti\\\", \\\"Q936906\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"carnic prealps\\\", \\\"Q152928\\\", [[17, 18]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"collects\\\", \\\"plants\\\", \\\"local\\\", \\\"to\\\", \\\"the\\\", \\\"nearby\\\", \\\"Gran\\\", \\\"Sasso\\\", \\\"massif\\\", \\\"of\\\", \\\"the\\\", \\\"Apennine\\\", \\\"Mountains\\\", \\\",\\\", \\\"including\\\", \\\"hundreds\\\", \\\"of\\\", \\\"grass\\\", \\\"species\\\", \\\",\\\", \\\"false\\\", \\\"bilberry\\\", \\\",\\\", \\\"greater\\\", \\\"gentian\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"Apennine\\\", \\\"edelweiss\\\", \\\".\\\"], \\\"h\\\": [\\\"gran sasso\\\", \\\"Q216869\\\", [[7, 8]]], \\\"t\\\": [\\\"apennine mountains\\\", \\\"Q1285\\\", [[12, 13]]]}, {\\\"tokens\\\": [\\\"Kranz\\\", \\\"Peak\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"peak\\\", \\\"high\\\", \\\",\\\", \\\"standing\\\", \\\"northwest\\\", \\\"of\\\", \\\"Mount\\\", \\\"Przywitowski\\\", \\\",\\\", \\\"between\\\", \\\"the\\\", \\\"heads\\\", \\\"of\\\", \\\"Holdsworth\\\", \\\"Glacier\\\", \\\"and\\\", \\\"Bartlett\\\", \\\"Glacier\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"Queen\\\", \\\"Maud\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"bartlett glacier\\\", \\\"Q4865396\\\", [[22, 23]]], \\\"t\\\": [\\\"queen maud mountains\\\", \\\"Q1796029\\\", [[27, 28, 29]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"valley\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"San\\\", \\\"Bernardino\\\", \\\"Mountains\\\", \\\",\\\", \\\"includes\\\", \\\"Big\\\", \\\"Bear\\\", \\\"Lake\\\", \\\",\\\", \\\"Big\\\", \\\"Bear\\\", \\\"City\\\", \\\",\\\", \\\"Fawnskin\\\", \\\",\\\", \\\"Holcomb\\\", \\\"Valley\\\", \\\",\\\", \\\"Sugarloaf\\\", \\\",\\\", \\\"Erwin\\\", \\\"Lake\\\", \\\",\\\", \\\"Baldwin\\\", \\\"Lake\\\", \\\"and\\\", \\\"Lake\\\", \\\"Williams\\\", \\\".\\\"], \\\"h\\\": [\\\"big bear lake\\\", \\\"Q14681604\\\", [[10, 11, 12]]], \\\"t\\\": [\\\"san bernardino mountains\\\", \\\"Q1577959\\\", [[5, 6, 7]]]}, {\\\"tokens\\\": [\\\"Dornie\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"small\\\", \\\"former\\\", \\\"fishing\\\", \\\"village\\\", \\\"in\\\", \\\"the\\\", \\\"Kintail\\\", \\\"district\\\", \\\"in\\\", \\\"western\\\", \\\"Ross\\\", \\\"-\\\", \\\"shire\\\", \\\"Highlands\\\", \\\"of\\\", \\\"Scotland\\\", \\\",\\\", \\\"with\\\", \\\"a\\\", \\\"population\\\", \\\"of\\\", \\\"360\\\", \\\"(\\\", \\\"2006\\\", \\\"census\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"kintail\\\", \\\"Q1542784\\\", [[11]]], \\\"t\\\": [\\\"highlands\\\", \\\"Q106652\\\", [[18]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"lies\\\", \\\"on\\\", \\\"the\\\", \\\"southeastern\\\", \\\"slopes\\\", \\\"of\\\", \\\"two\\\", \\\"mountain\\\", \\\"ranges\\\", \\\"\\\\u2013\\\", \\\"the\\\", \\\"\\\\u015anie\\\\u017cnik\\\", \\\"Mountains\\\", \\\"and\\\", \\\"the\\\", \\\"Golden\\\", \\\"Mountains\\\", \\\"of\\\", \\\"the\\\", \\\"Eastern\\\", \\\"Sudetes\\\", \\\",\\\", \\\"which\\\", \\\"form\\\", \\\"the\\\", \\\"border\\\", \\\"with\\\", \\\"Poland\\\", \\\".\\\"], \\\"h\\\": [\\\"golden mountains\\\", \\\"Q1935661\\\", [[16, 17]]], \\\"t\\\": [\\\"eastern sudetes\\\", \\\"Q3492552\\\", [[20, 21]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Corneliussen\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\",\\\", \\\"high\\\", \\\",\\\", \\\"standing\\\", \\\"north\\\", \\\"of\\\", \\\"Mount\\\", \\\"Globus\\\", \\\"at\\\", \\\"the\\\", \\\"west\\\", \\\"end\\\", \\\"of\\\", \\\"the\\\", \\\"Allardyce\\\", \\\"Range\\\", \\\"of\\\", \\\"South\\\", \\\"Georgia\\\", \\\".\\\"], \\\"h\\\": [\\\"mount globus\\\", \\\"Q6920922\\\", [[13, 14]]], \\\"t\\\": [\\\"allardyce range\\\", \\\"Q1329317\\\", [[21, 22]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"latter\\\", \\\"is\\\", \\\"the\\\", \\\"height\\\", \\\"of\\\", \\\"the\\\", \\\"Michelsberg\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"the\\\", \\\"highest\\\", \\\"point\\\", \\\"in\\\", \\\"the\\\", \\\"borough\\\", \\\"and\\\", \\\"rises\\\", \\\"in\\\", \\\"the\\\", \\\"northwestern\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Ahr\\\", \\\"Hills\\\", \\\"(\\\", \\\"another\\\", \\\"region\\\", \\\"of\\\", \\\"the\\\", \\\"Eifel\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"michelsberg\\\", \\\"Q1649673\\\", [[7]]], \\\"t\\\": [\\\"ahr hills\\\", \\\"Q402861\\\", [[25, 26]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Boundary\\\", \\\"Peak\\\", \\\"Wilderness\\\", \\\"is\\\", \\\"a\\\", \\\"protected\\\", \\\"wilderness\\\", \\\"area\\\", \\\"in\\\", \\\"the\\\", \\\"White\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Esmeralda\\\", \\\"County\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"western\\\", \\\"section\\\", \\\"of\\\", \\\"the\\\", \\\"state\\\", \\\"of\\\", \\\"Nevada\\\", \\\"in\\\", \\\"the\\\", \\\"western\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"boundary peak\\\", \\\"Q573205\\\", [[1, 2]]], \\\"t\\\": [\\\"white mountains\\\", \\\"Q1433957\\\", [[11, 12]]]}, {\\\"tokens\\\": [\\\"Besides\\\", \\\"the\\\", \\\"peak\\\", \\\"at\\\", \\\"Mount\\\", \\\"Tipton\\\", \\\",\\\", \\\"the\\\", \\\"Cerbat\\\", \\\"Pinnacles\\\", \\\"is\\\", \\\"a\\\", \\\"rockscape\\\", \\\"attraction\\\", \\\"on\\\", \\\"the\\\", \\\"north\\\", \\\"of\\\", \\\"the\\\", \\\"Cerbat\\\", \\\"Mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"mount tipton\\\", \\\"Q6924123\\\", [[4, 5]]], \\\"t\\\": [\\\"cerbat mountains\\\", \\\"Q5063897\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"hill\\\", \\\"on\\\", \\\"the\\\", \\\"opposite\\\", \\\"side\\\", \\\"of\\\", \\\"the\\\", \\\"gorge\\\", \\\"to\\\", \\\"the\\\", \\\"west\\\", \\\",\\\", \\\"the\\\", \\\"Wittekindsberg\\\", \\\"(\\\", \\\")\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"the\\\", \\\"eastern\\\", \\\"guardian\\\", \\\"of\\\", \\\"the\\\", \\\"Wiehen\\\", \\\"Hills\\\", \\\",\\\", \\\"defines\\\", \\\"the\\\", \\\"western\\\", \\\"side\\\", \\\"of\\\", \\\"this\\\", \\\"gorge\\\", \\\".\\\"], \\\"h\\\": [\\\"wittekindsberg\\\", \\\"Q878081\\\", [[14]]], \\\"t\\\": [\\\"wiehen hills\\\", \\\"Q702826\\\", [[25, 26]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"highest\\\", \\\"point\\\", \\\"is\\\", \\\"Saddle\\\", \\\"Mountain\\\", \\\"at\\\", \\\"3,283\\\", \\\"feet\\\", \\\"(\\\", \\\"1,001\\\", \\\"m\\\", \\\")\\\", \\\",\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Northern\\\", \\\"Oregon\\\", \\\"Coast\\\", \\\"Range\\\", \\\".\\\"], \\\"h\\\": [\\\"saddle mountain\\\", \\\"Q7397701\\\", [[4, 5]]], \\\"t\\\": [\\\"northern oregon coast range\\\", \\\"Q2961794\\\", [[17, 18, 19, 20]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Elbert\\\", \\\"in\\\", \\\"the\\\", \\\"Sawatch\\\", \\\"Range\\\", \\\"is\\\", \\\"the\\\", \\\"highest\\\", \\\"peak\\\", \\\"of\\\", \\\"the\\\", \\\"Rocky\\\", \\\"Mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"mount elbert\\\", \\\"Q657225\\\", [[0, 1]]], \\\"t\\\": [\\\"sawatch range\\\", \\\"Q1478903\\\", [[4, 5]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"lies\\\", \\\"on\\\", \\\"the\\\", \\\"Ostravice\\\", \\\"River\\\", \\\"at\\\", \\\"the\\\", \\\"foot\\\", \\\"of\\\", \\\"Lys\\\\u00e1\\\", \\\"hora\\\", \\\",\\\", \\\"the\\\", \\\"highest\\\", \\\"mountain\\\", \\\"of\\\", \\\"the\\\", \\\"Moravian\\\", \\\"-\\\", \\\"Silesian\\\", \\\"Beskids\\\", \\\".\\\"], \\\"h\\\": [\\\"lys\\\\u00e1 hora\\\", \\\"Q1573557\\\", [[10, 11]]], \\\"t\\\": [\\\"moravian-silesian beskids\\\", \\\"Q1365195\\\", [[18, 19, 20, 21]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Gr\\\\u00fcnten\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"Oberallg\\\\u00e4u\\\", \\\"region\\\", \\\"of\\\", \\\"southern\\\", \\\"Bavaria\\\", \\\",\\\", \\\"and\\\", \\\"is\\\", \\\"one\\\", \\\"of\\\", \\\"the\\\", \\\"most\\\", \\\"northerly\\\", \\\"mountains\\\", \\\"of\\\", \\\"the\\\", \\\"Allg\\\\u00e4u\\\", \\\"Alps\\\", \\\".\\\"], \\\"h\\\": [\\\"gr\\\\u00fcnten\\\", \\\"Q205163\\\", [[1]]], \\\"t\\\": [\\\"allg\\\\u00e4u alps\\\", \\\"Q655747\\\", [[22, 23]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Farnham\\\", \\\"Group\\\", \\\"is\\\", \\\"a\\\", \\\"sub\\\", \\\"-\\\", \\\"range\\\", \\\"of\\\", \\\"the\\\", \\\"Purcell\\\", \\\"Mountains\\\", \\\",\\\", \\\"containing\\\", \\\"the\\\", \\\"highest\\\", \\\"summit\\\", \\\"of\\\", \\\"that\\\", \\\"range\\\", \\\",\\\", \\\"Mount\\\", \\\"Farnham\\\", \\\".\\\"], \\\"h\\\": [\\\"mount farnham\\\", \\\"Q6920728\\\", [[21, 22]]], \\\"t\\\": [\\\"purcell mountains\\\", \\\"Q2961786\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Andrews\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\",\\\", \\\"high\\\", \\\",\\\", \\\"standing\\\", \\\"between\\\", \\\"Mount\\\", \\\"Danforth\\\", \\\"and\\\", \\\"Mount\\\", \\\"Gerdel\\\", \\\"on\\\", \\\"the\\\", \\\"south\\\", \\\"side\\\", \\\"of\\\", \\\"Albanus\\\", \\\"Glacier\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"Queen\\\", \\\"Maud\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"mount gerdel\\\", \\\"Q6810732\\\", [[15, 16]]], \\\"t\\\": [\\\"queen maud mountains\\\", \\\"Q1796029\\\", [[27, 28, 29]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"T\\\\u00fcrnitz\\\", \\\"Alps\\\", \\\"(\\\", \\\")\\\", \\\"are\\\", \\\"a\\\", \\\"mountain\\\", \\\"range\\\", \\\"of\\\", \\\"the\\\", \\\"Northern\\\", \\\"Limestone\\\", \\\"Alps\\\", \\\"in\\\", \\\"southern\\\", \\\"Lower\\\", \\\"Austria\\\", \\\"and\\\", \\\"the\\\", \\\"adjacent\\\", \\\"state\\\", \\\"of\\\", \\\"Styria\\\", \\\".\\\"], \\\"h\\\": [\\\"t\\\\u00fcrnitz alps\\\", \\\"Q691932\\\", [[1, 2]]], \\\"t\\\": [\\\"northern limestone alps\\\", \\\"Q4935045\\\", [[11, 12, 13]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Damm\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"snow\\\", \\\"-\\\", \\\"covered\\\", \\\"mountain\\\", \\\",\\\", \\\"high\\\", \\\",\\\", \\\"between\\\", \\\"Heidemann\\\", \\\"Glacier\\\", \\\"and\\\", \\\"Nottarp\\\", \\\"Glacier\\\", \\\"in\\\", \\\"the\\\", \\\"Queen\\\", \\\"Elizabeth\\\", \\\"Range\\\", \\\".\\\"], \\\"h\\\": [\\\"nottarp glacier\\\", \\\"Q7063543\\\", [[17, 18]]], \\\"t\\\": [\\\"queen elizabeth range\\\", \\\"Q3323150\\\", [[21, 22, 23]]]}, {\\\"tokens\\\": [\\\"Howlock\\\", \\\"Mountain\\\", \\\"is\\\", \\\"a\\\", \\\"heavily\\\", \\\"eroded\\\", \\\"shield\\\", \\\"volcano\\\", \\\"in\\\", \\\"the\\\", \\\"Cascade\\\", \\\"Range\\\", \\\"of\\\", \\\"central\\\", \\\"Oregon\\\", \\\",\\\", \\\"located\\\", \\\"along\\\", \\\"the\\\", \\\"Cascade\\\", \\\"Crest\\\", \\\"just\\\", \\\"north\\\", \\\"of\\\", \\\"Mount\\\", \\\"Thielsen\\\", \\\".\\\"], \\\"h\\\": [\\\"mount thielsen\\\", \\\"Q1481220\\\", [[24, 25]]], \\\"t\\\": [\\\"cascade range\\\", \\\"Q4558\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"Coulter\\\", \\\"Glacier\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"steeply\\\", \\\"inclined\\\", \\\"glacier\\\", \\\",\\\", \\\"long\\\", \\\",\\\", \\\"flowing\\\", \\\"south\\\", \\\"from\\\", \\\"the\\\", \\\"Havre\\\", \\\"Mountains\\\", \\\",\\\", \\\"northern\\\", \\\"Alexander\\\", \\\"Island\\\", \\\",\\\", \\\"into\\\", \\\"Lazarev\\\", \\\"Bay\\\", \\\".\\\"], \\\"h\\\": [\\\"coulter glacier\\\", \\\"Q5176184\\\", [[0, 1]]], \\\"t\\\": [\\\"havre mountains\\\", \\\"Q12715362\\\", [[16, 17]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Lukens\\\", \\\"is\\\", \\\"in\\\", \\\"an\\\", \\\"area\\\", \\\"that\\\", \\\"was\\\", \\\"impacted\\\", \\\"by\\\", \\\"the\\\", \\\"2009\\\", \\\"Station\\\", \\\"Fire\\\", \\\"in\\\", \\\"the\\\", \\\"San\\\", \\\"Gabriel\\\", \\\"Mountains\\\", \\\",\\\", \\\"the\\\", \\\"largest\\\", \\\"wildfire\\\", \\\"in\\\", \\\"the\\\", \\\"history\\\", \\\"of\\\", \\\"Los\\\", \\\"Angeles\\\", \\\"County\\\", \\\".\\\"], \\\"h\\\": [\\\"mount lukens\\\", \\\"Q6921917\\\", [[0, 1]]], \\\"t\\\": [\\\"san gabriel mountains\\\", \\\"Q1419854\\\", [[16, 17, 18]]]}, {\\\"tokens\\\": [\\\"Mola\\\", \\\"de\\\", \\\"Colldejou\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\"chain\\\", \\\"in\\\", \\\"Catalonia\\\", \\\",\\\", \\\"Spain\\\", \\\"located\\\", \\\"north\\\", \\\"of\\\", \\\"the\\\", \\\"Serra\\\", \\\"de\\\", \\\"Llaberia\\\", \\\"in\\\", \\\"the\\\", \\\"Catalan\\\", \\\"Pre\\\", \\\"-\\\", \\\"Coastal\\\", \\\"Range\\\", \\\".\\\"], \\\"h\\\": [\\\"mola de colldejou\\\", \\\"Q6895629\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"catalan pre-coastal range\\\", \\\"Q520924\\\", [[20, 21, 22, 23, 24]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Southern\\\", \\\"bank\\\", \\\"of\\\", \\\"the\\\", \\\"Main\\\", \\\"stretches\\\", \\\"up\\\", \\\"to\\\", \\\"the\\\", \\\"mountain\\\", \\\"range\\\", \\\"of\\\", \\\"the\\\", \\\"Franconian\\\", \\\"Jura\\\", \\\"(\\\", \\\"Fr\\\\u00e4nkische\\\", \\\"Alb\\\", \\\")\\\", \\\"beneath\\\", \\\"the\\\", \\\"Staffelberg\\\", \\\"close\\\", \\\"to\\\", \\\"Bad\\\", \\\"Staffelstein\\\", \\\".\\\"], \\\"h\\\": [\\\"staffelberg\\\", \\\"Q1771083\\\", [[22]]], \\\"t\\\": [\\\"franconian jura\\\", \\\"Q669883\\\", [[14, 15]]]}, {\\\"tokens\\\": [\\\"Woodberry\\\", \\\"Nunataks\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"group\\\", \\\"of\\\", \\\"small\\\", \\\"nunataks\\\", \\\"1\\\", \\\"\\\\u00a0\\\", \\\"nautical\\\", \\\"mile\\\", \\\"(\\\", \\\"1.9\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"north\\\", \\\"of\\\", \\\"Lucas\\\", \\\"Nunatak\\\", \\\"in\\\", \\\"the\\\", \\\"Casey\\\", \\\"Range\\\", \\\",\\\", \\\"Framnes\\\", \\\"Mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"lucas nunatak\\\", \\\"Q6696243\\\", [[21, 22]]], \\\"t\\\": [\\\"framnes mountains\\\", \\\"Q5256660\\\", [[28, 29]]]}, {\\\"tokens\\\": [\\\"Many\\\", \\\"mountains\\\", \\\"in\\\", \\\"the\\\", \\\"Pacific\\\", \\\"Ranges\\\", \\\",\\\", \\\"including\\\", \\\"Mount\\\", \\\"Sir\\\", \\\"Francis\\\", \\\"Drake\\\", \\\"and\\\", \\\"Mount\\\", \\\"Queen\\\", \\\"Bess\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"Golden\\\", \\\"Hinde\\\", \\\"on\\\", \\\"Vancouver\\\", \\\"Island\\\", \\\",\\\", \\\"were\\\", \\\"named\\\", \\\"in\\\", \\\"the\\\", \\\"1930s\\\", \\\"as\\\", \\\"proposed\\\", \\\"by\\\", \\\"him\\\", \\\".\\\"], \\\"h\\\": [\\\"mount sir francis drake\\\", \\\"Q17019089\\\", [[8, 9, 10, 11]]], \\\"t\\\": [\\\"pacific ranges\\\", \\\"Q1285418\\\", [[4, 5]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"the\\\", \\\"north\\\", \\\"during\\\", \\\"this\\\", \\\"stretch\\\", \\\"is\\\", \\\"the\\\", \\\"mile\\\", \\\"-\\\", \\\"high\\\", \\\"Caliente\\\", \\\"Range\\\", \\\",\\\", \\\"which\\\", \\\"contains\\\", \\\"Caliente\\\", \\\"Mountain\\\", \\\",\\\", \\\"the\\\", \\\"highest\\\", \\\"peak\\\", \\\"in\\\", \\\"San\\\", \\\"Luis\\\", \\\"Obispo\\\", \\\"County\\\", \\\".\\\"], \\\"h\\\": [\\\"caliente mountain\\\", \\\"Q5019902\\\", [[16, 17]]], \\\"t\\\": [\\\"caliente range\\\", \\\"Q5019906\\\", [[11, 12]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Neretva\\\", \\\"springs\\\", \\\"are\\\", \\\"situated\\\", \\\"deep\\\", \\\"in\\\", \\\"the\\\", \\\"Dinaric\\\", \\\"Alps\\\", \\\"at\\\", \\\"the\\\", \\\"base\\\", \\\"of\\\", \\\"the\\\", \\\"Zelengora\\\", \\\"and\\\", \\\"Lebr\\\\u0161nik\\\", \\\"mountains\\\", \\\"under\\\", \\\"the\\\", \\\"village\\\", \\\"Jabuka\\\", \\\"and\\\", \\\"the\\\", \\\"saddle\\\", \\\"Gredelj\\\", \\\".\\\"], \\\"h\\\": [\\\"zelengora\\\", \\\"Q619701\\\", [[15]]], \\\"t\\\": [\\\"dinaric alps\\\", \\\"Q189915\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Ferrara\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\"in\\\", \\\"Antarctica\\\", \\\",\\\", \\\"high\\\", \\\",\\\", \\\"standing\\\", \\\"northeast\\\", \\\"of\\\", \\\"Vaca\\\", \\\"Nunatak\\\", \\\"in\\\", \\\"the\\\", \\\"Panzarini\\\", \\\"Hills\\\", \\\"portion\\\", \\\"of\\\", \\\"the\\\", \\\"Argentina\\\", \\\"Range\\\", \\\",\\\", \\\"in\\\", \\\"the\\\", \\\"Pensacola\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"vaca nunatak\\\", \\\"Q7907868\\\", [[13, 14]]], \\\"t\\\": [\\\"argentina range\\\", \\\"Q4789285\\\", [[22, 23]]]}, {\\\"tokens\\\": [\\\"Canopy\\\", \\\"Cliffs\\\", \\\"(\\\", \\\")\\\", \\\"are\\\", \\\"steep\\\", \\\"cliffs\\\", \\\"extending\\\", \\\"from\\\", \\\"Mount\\\", \\\"Allsup\\\", \\\"to\\\", \\\"Mount\\\", \\\"Ropar\\\", \\\"on\\\", \\\"the\\\", \\\"southeast\\\", \\\"side\\\", \\\"of\\\", \\\"Peletier\\\", \\\"Plateau\\\", \\\",\\\", \\\"Queen\\\", \\\"Elizabeth\\\", \\\"Range\\\", \\\".\\\"], \\\"h\\\": [\\\"mount allsup\\\", \\\"Q6919374\\\", [[9, 10]]], \\\"t\\\": [\\\"queen elizabeth range\\\", \\\"Q3323150\\\", [[22, 23, 24]]]}, {\\\"tokens\\\": [\\\"Conant\\\", \\\"Valley\\\", \\\"is\\\", \\\"a\\\", \\\"valley\\\", \\\"between\\\", \\\"Duncan\\\", \\\"Bluff\\\", \\\"and\\\", \\\"Communication\\\", \\\"Heights\\\", \\\"in\\\", \\\"the\\\", \\\"southern\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Darwin\\\", \\\"Mountains\\\", \\\";\\\", \\\"the\\\", \\\"valley\\\", \\\"mouth\\\", \\\"opens\\\", \\\"to\\\", \\\"Hatherton\\\", \\\"Glacier\\\", \\\".\\\"], \\\"h\\\": [\\\"communication heights\\\", \\\"Q5154099\\\", [[9, 10]]], \\\"t\\\": [\\\"darwin mountains\\\", \\\"Q5226004\\\", [[17, 18]]]}, {\\\"tokens\\\": [\\\"One\\\", \\\"of\\\", \\\"the\\\", \\\"White\\\", \\\"Mountains\\\", \\\"'\\\", \\\"major\\\", \\\"passes\\\", \\\",\\\", \\\"Kinsman\\\", \\\"Notch\\\", \\\"lies\\\", \\\"between\\\", \\\"Mount\\\", \\\"Moosilauke\\\", \\\"and\\\", \\\"Kinsman\\\", \\\"Ridge\\\", \\\"at\\\", \\\"just\\\", \\\"under\\\", \\\"above\\\", \\\"sea\\\", \\\"level\\\", \\\".\\\"], \\\"h\\\": [\\\"kinsman notch\\\", \\\"Q6414297\\\", [[9, 10]]], \\\"t\\\": [\\\"white mountains'\\\", \\\"Q1556007\\\", [[3, 4, 5]]]}, {\\\"tokens\\\": [\\\"Donald\\\", \\\"Ridge\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"narrow\\\", \\\"ridge\\\", \\\"extending\\\", \\\"south\\\", \\\"from\\\", \\\"Mount\\\", \\\"Capley\\\", \\\"in\\\", \\\"the\\\", \\\"Pioneer\\\", \\\"Heights\\\", \\\",\\\", \\\"Heritage\\\", \\\"Range\\\", \\\".\\\"], \\\"h\\\": [\\\"pioneer heights\\\", \\\"Q1256114\\\", [[15, 16]]], \\\"t\\\": [\\\"heritage range\\\", \\\"Q1522169\\\", [[18, 19]]]}, {\\\"tokens\\\": [\\\"There\\\", \\\"are\\\", \\\"10\\\", \\\"Munro\\\", \\\"mountains\\\", \\\"(\\\", \\\"mountains\\\", \\\"over\\\", \\\"3,000\\\", \\\"\\\\u00a0\\\", \\\"ft\\\", \\\")\\\", \\\"in\\\", \\\"the\\\", \\\"Mamores\\\", \\\"above\\\", \\\"Kinlochleven\\\", \\\"with\\\", \\\"Binnein\\\", \\\"Mor\\\", \\\"the\\\", \\\"highest\\\", \\\".\\\"], \\\"h\\\": [\\\"binnein mor\\\", \\\"Q3396990\\\", [[18, 19]]], \\\"t\\\": [\\\"mamores\\\", \\\"Q6745927\\\", [[14]]]}, {\\\"tokens\\\": [\\\"To\\\", \\\"the\\\", \\\"east\\\", \\\"of\\\", \\\"the\\\", \\\"peak\\\", \\\"lies\\\", \\\"the\\\", \\\"large\\\", \\\"icefield\\\", \\\"which\\\", \\\"forms\\\", \\\"the\\\", \\\"head\\\", \\\"of\\\", \\\"the\\\", \\\"Brady\\\", \\\"Glacier\\\", \\\",\\\", \\\"the\\\", \\\"southernmost\\\", \\\"of\\\", \\\"the\\\", \\\"large\\\", \\\"glaciers\\\", \\\"of\\\", \\\"the\\\", \\\"Saint\\\", \\\"Elias\\\", \\\"Mountains\\\", \\\".\\\"], \\\"h\\\": [\\\"brady glacier\\\", \\\"Q4955184\\\", [[16, 17]]], \\\"t\\\": [\\\"saint elias mountains\\\", \\\"Q48719\\\", [[27, 28, 29]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Howell\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\"south\\\", \\\"-\\\", \\\"southwest\\\", \\\"of\\\", \\\"Mount\\\", \\\"Borgeson\\\", \\\"in\\\", \\\"the\\\", \\\"Walker\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Thurston\\\", \\\"Island\\\", \\\",\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"mount borgeson\\\", \\\"Q12716971\\\", [[11, 12]]], \\\"t\\\": [\\\"walker mountains\\\", \\\"Q7962300\\\", [[15, 16]]]}, {\\\"tokens\\\": [\\\"Mount\\\", \\\"Kerckhove\\\", \\\"de\\\", \\\"Denterghem\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"mountain\\\", \\\",\\\", \\\"high\\\", \\\",\\\", \\\"just\\\", \\\"north\\\", \\\"of\\\", \\\"Mount\\\", \\\"Collard\\\", \\\"in\\\", \\\"the\\\", \\\"Belgica\\\", \\\"Mountains\\\", \\\"of\\\", \\\"Antarctica\\\", \\\".\\\"], \\\"h\\\": [\\\"mount collard\\\", \\\"Q6920207\\\", [[15, 16]]], \\\"t\\\": [\\\"belgica mountains\\\", \\\"Q815473\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"Titlis\\\", \\\"is\\\", \\\"the\\\", \\\"highest\\\", \\\"mountain\\\", \\\"in\\\", \\\"the\\\", \\\"portion\\\", \\\"of\\\", \\\"the\\\", \\\"Uri\\\", \\\"Alps\\\", \\\"north\\\", \\\"of\\\", \\\"the\\\", \\\"Susten\\\", \\\"Pass\\\", \\\".\\\"], \\\"h\\\": [\\\"titlis\\\", \\\"Q15138\\\", [[0]]], \\\"t\\\": [\\\"uri alps\\\", \\\"Q869491\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"Browns\\\", \\\"Butte\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"bare\\\", \\\"rock\\\", \\\"butte\\\", \\\"at\\\", \\\"the\\\", \\\"north\\\", \\\"side\\\", \\\"of\\\", \\\"the\\\", \\\"mouth\\\", \\\"of\\\", \\\"Koski\\\", \\\"Glacier\\\", \\\"in\\\", \\\"the\\\", \\\"Dominion\\\", \\\"Range\\\", \\
```

---
